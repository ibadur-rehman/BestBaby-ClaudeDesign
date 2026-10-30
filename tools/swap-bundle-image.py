#!/usr/bin/env python3
"""Replace one image inside a BestBaby single-file bundle.

The bundles (index.html, admin/index.html) carry their assets base64-encoded in a
`__bundler/manifest` JSON blob, keyed by UUID. `__bundler/ext_resources` maps friendly
names (stageImg0..3) onto those UUIDs. This swaps one entry in place and sets the
declared mime from the file's real magic bytes, so the manifest stays honest.

    # see what is in there
    python tools/swap-bundle-image.py --list

    # dry run, then do it
    python tools/swap-bundle-image.py --target stageImg2 --file new-birth.jpg --dry-run
    python tools/swap-bundle-image.py --target stageImg2 --file new-birth.jpg

Target may be a friendly name (stageImg2) or a UUID prefix (c03b5608).
Writes via a temp file and os.replace, so a failed write cannot truncate the bundle.
"""
import argparse, base64, json, os, re, shutil, struct, sys, tempfile

MAGIC = [
    (b'\x89PNG\r\n\x1a\n', 'image/png',  'PNG'),
    (b'\xff\xd8',          'image/jpeg', 'JPEG'),
    (b'GIF87a',            'image/gif',  'GIF'),
    (b'GIF89a',            'image/gif',  'GIF'),
]


def sniff(b):
    if b[:4] == b'RIFF' and b[8:12] == b'WEBP':
        return 'image/webp', 'WEBP'
    for sig, mime, name in MAGIC:
        if b.startswith(sig):
            return mime, name
    return None, None


def dimensions(b):
    mime, kind = sniff(b)
    try:
        if kind == 'PNG':
            i = 8
            while i + 8 <= len(b):
                ln = struct.unpack('>I', b[i:i + 4])[0]
                if b[i + 4:i + 8] == b'IHDR':
                    return struct.unpack('>II', b[i + 8:i + 16])
                i += 12 + ln
        elif kind == 'JPEG':
            i = 2
            while i < len(b) - 9:
                if b[i] != 0xFF:
                    i += 1
                    continue
                m = b[i + 1]
                if m in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                         0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                    h, w = struct.unpack('>HH', b[i + 5:i + 9])
                    return w, h
                if m in (0xD8, 0xD9) or 0xD0 <= m <= 0xD7:
                    i += 2
                    continue
                i += 2 + struct.unpack('>H', b[i + 2:i + 4])[0]
    except Exception:
        pass
    return None, None


def ai_provenance(b):
    """Return the AI content-producer named in embedded C2PA/AIGC metadata, if any."""
    head = b[:120000].decode('latin1', 'replace')
    m = re.search(r'\{"AIGC":\{"Label":"(\d)","ContentProducer":"([^"]+)"', head)
    return m.group(2) if m else None


def load(bundle):
    lines = open(bundle, encoding='utf-8').read().split('\n')
    man_i = next(i for i, l in enumerate(lines)
                 if l.strip().startswith('{"') and len(l) > 100000)
    ext_i = next((i for i, l in enumerate(lines)
                  if l.strip().startswith('[{"id":"')), None)
    names = {}
    if ext_i is not None:
        for e in json.loads(lines[ext_i]):
            names[e['id']] = e['uuid']
    return lines, man_i, json.loads(lines[man_i]), names


def resolve(target, man, names):
    if target in names:
        return names[target]
    hits = [u for u in man if u.startswith(target)]
    if len(hits) == 1:
        return hits[0]
    if not hits:
        sys.exit('No manifest entry matches %r. Use --list.' % target)
    sys.exit('%r is ambiguous: %s' % (target, ', '.join(h[:8] for h in hits)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bundle', default='index.html')
    ap.add_argument('--target', help='stageImg2, or a UUID prefix')
    ap.add_argument('--file', help='replacement image on disk')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--no-backup', action='store_true')
    a = ap.parse_args()

    lines, man_i, man, names = load(a.bundle)
    by_uuid = {v: k for k, v in names.items()}

    if a.list or not (a.target and a.file):
        print('%-10s %-10s %-7s %-12s %-9s %s'
              % ('name', 'declared', 'actual', 'dims', 'AI', 'uuid'))
        print('-' * 80)
        for u, m in man.items():
            if not m['mime'].startswith('image'):
                continue
            raw = base64.b64decode(m['data'])
            _, kind = sniff(raw)
            w, h = dimensions(raw)
            prov = ai_provenance(raw)
            print('%-10s %-10s %-7s %-12s %-9s %s'
                  % (by_uuid.get(u, ''), m['mime'].split('/')[1], kind or '?',
                     ('%sx%s' % (w, h)) if w else '?', prov or '-', u))
        if not a.list:
            print('\nPass --target and --file to replace one.')
        return

    uuid = resolve(a.target, man, names)
    old = base64.b64decode(man[uuid]['data'])
    new = open(a.file, 'rb').read()

    mime, kind = sniff(new)
    if not mime:
        sys.exit('%s is not a recognised image (png/jpeg/gif/webp).' % a.file)

    ow, oh = dimensions(old)
    nw, nh = dimensions(new)
    print('target   %s (%s)' % (uuid, by_uuid.get(uuid, 'unnamed')))
    print('current  %-6s %sx%s  %.0f KB  declared %s'
          % (sniff(old)[1], ow, oh, len(old) / 1024, man[uuid]['mime']))
    print('new      %-6s %sx%s  %.0f KB  -> will declare %s'
          % (kind, nw, nh, len(new) / 1024, mime))

    if ow and nw:
        oar, nar = ow / oh, nw / nh
        if abs(oar - nar) > 0.02:
            print('WARNING  aspect ratio changes %.3f -> %.3f; the layout crops to the '
                  'old shape, so framing may shift.' % (oar, nar))
        if nw < ow or nh < oh:
            print('WARNING  new image is smaller than the old one (%sx%s < %sx%s); it may '
                  'look soft on retina displays.' % (nw, nh, ow, oh))

    prov = ai_provenance(new)
    if prov:
        print('WARNING  replacement carries embedded AI provenance (ContentProducer: %s). '
              'If the point was to remove AI-generator branding, this does not.' % prov)

    if a.dry_run:
        print('\ndry run - nothing written.')
        return

    man[uuid] = {'mime': mime, 'compressed': False,
                 'data': base64.b64encode(new).decode('ascii')}
    lines[man_i] = json.dumps(man, separators=(',', ':'))

    if not a.no_backup:
        shutil.copyfile(a.bundle, a.bundle + '.bak')
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(os.path.abspath(a.bundle)),
                               suffix='.tmp')
    os.close(fd)
    with open(tmp, 'w', encoding='utf-8', newline='') as f:
        f.write('\n'.join(lines))
    os.replace(tmp, a.bundle)
    print('\nwritten to %s%s' % (a.bundle, '' if a.no_backup else ' (backup: .bak)'))


if __name__ == '__main__':
    main()
