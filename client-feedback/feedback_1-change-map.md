# feedback_1 → change map

**Source:** [`client-feedback/feedback_1.md`](feedback_1.md) (Supreet, 26 Oct 2026) — copied into the repo from `~/Downloads` so this mapping has a stable reference.
**Targets:** [`landing.html`](../landing.html) (7.7 MB), [`admin/admin.html`](../admin/admin.html) (1.0 MB)
**Status:** **Batches 1–4 implemented and verified**; **Batch 5 audited and tooled but blocked on replacement images** — every P0 except **P0-8** (the watermarked image), plus G-1 and a responsive fix that unblocks mobile testing. Remaining: P0-8, all P1/P2.

Every one of the 22 actionable items (P0-1…P0-10, P1-1…P1-6, A1-1, P2-1…P2-5) is mapped below, plus the 11 Hold items verified as present-and-untouched. Section G lists findings that are **not** in the feedback.

---

## A. How these files are edited — read before touching anything

Both files are **single-file bundles**, not build outputs with a source project. README: *"The whole thing is one file… No server, no build step."* The last commit edited `landing.html` directly. So the bundle **is** the source.

Internal structure (same for both files):

| Line | Content |
| --- | --- |
| 1–367 | Loader shell (unpacker JS, loading overlay) — do not touch |
| 370 | `__bundler/manifest` — JSON of 32 base64 assets (images, fonts, React UMD) |
| 374 | `__bundler/ext_resources` — maps `stageImg0–3` to manifest UUIDs |
| 382 (landing) / 383+395 (admin) | `__bundler/template` — **the app**: JSON-escaped HTML + inline JS |

Practical consequences:

- **One giant line.** `landing.html` line 382 is 845 KB; admin's are 501 KB and 545 KB. Line numbers are useless — all locations below are **byte offsets** into the file. Offsets shift as you edit, so re-grep the quoted string rather than trusting a stale offset.
- **The markup is JSON-escaped.** `/` appears as `/`, quotes as `\"`, newlines as `\n`. Any replacement string must be escaped the same way or the bundle will not parse.
- **Templating is `sc-*` + `{{ }}`**, not React JSX: `<sc-if value="{{ prop }}">`, `<sc-for list="{{ xs }}" as="x">`, `sc-camel-on-click="{{ handler }}"`. Add conditionals with `sc-if`, not JS.
- **Copy lives in two different places** — either inline in the markup, or in JS data arrays near the end of the template (`FAQS`, `FACT_OPTIONS`, `STAGES`, `GDPR`, `DB_TABS`, `TREND_DATA`). Several items below need edits in both.
- Both files are valid UTF-8 and contain curly quotes (`’ “ ” —`). Keep them; don't normalise to ASCII.
- **`sc-if` is only honoured at block level, wrapping an element.** Learned the hard way in Batch 1: an `sc-if` placed inline around a *bare text node* inside a `<p>` is silently stripped by the engine and **its content renders anyway** — it fails open, which for a privacy or internal-note gate is the dangerous direction. Wrapping the text in a `<span>` did **not** help either. The fix is to lift the content into its own sibling element (e.g. a second `<p>`) and gate that. Anything gated must be verified in the browser, never assumed from the source.
- **The browser caches these files hard.** `http.server` serves `Last-Modified` and the browser will reuse a stale copy across edits, which reads exactly like "my change didn't work". Always reload with a cache-busting query (`?v=2`) after editing.
- **Admin props are declared in `data-props`**, an HTML-entity-encoded JSON blob on the `<script type="text/x-dc">` tag (≈ byte 810365). Props are read in `renderVals()` via `const p = this.props` and must be re-exported in that method's returned object to become a `{{ binding }}`. Three edits per new prop: declare, derive, expose.
- **Patch with a script that asserts each find matches exactly once, and write via a temp file then move.** A direct `open(path, 'w')` truncates the file *before* encoding, so a write that raises mid-way destroys it — which is how this document got wiped once and had to be rebuilt.

**Verification used for this map:** every quoted string in the feedback was grepped and confirmed present at the stated count (e.g. `affiliate offers` → exactly 2 hits, as the feedback says). Layout claims were checked by serving the files on `localhost:8777` and measuring in-page with JS at 1440×900.

---

## B. P0 — copy and assets the client must not see

> ### ✅ Batch 1 done — P0-1, P0-2, P0-3
>
> All three internal notes are now gated behind a new **`showAnnotations`** boolean prop on `admin/admin.html`, **default `false`**. The copy is preserved, not deleted, so it stays available for internal review.
>
> **Four edits, one file (`admin/admin.html`):**
>
> | Edit | Location | What |
> | --- | --- | --- |
> | Declare | `data-props` ≈ 810365 | `"showAnnotations":{"editor":"boolean","default":false,"tsType":"boolean","section":"Prototype notes"}` |
> | Derive | `renderVals()` ≈ 941427 | `const showAnnotations = p.showAnnotations === true;` — note `=== true`, so anything other than an explicit `true` stays off |
> | Expose | bindings object ≈ 991830 | `showAnnotations: showAnnotations,` beside `rowH` |
> | Gate | 3 sites | `<sc-if value="{{ showAnnotations }}" hint-placeholder-val="{{ false }}">` |
>
> **Verified in the browser at 1440×900**, with a positive control — the default was temporarily flipped to `true` to confirm all three notes *reappear*, then restored to `false`. This matters: "text is absent" alone would also be true if the gate had deleted it or the screen simply wasn't rendering.
>
> | Item | Screen | Default `false` | Forced `true` | Surroundings intact |
> | --- | --- | --- | --- | --- |
> | P0-1 | Sign-in | hidden ✅ | reappears ✅ | "Trouble getting in?" support line kept ✅ |
> | P0-2 | Articles | hidden ✅ | reappears ✅ | Articles table renders ✅ |
> | P0-3 | New article → Rewrite | hidden ✅ | reappears ✅ | Rewrite panel + "Morpheus returns a draft you edit" kept ✅ |
>
> Structural checks: `data-props` still parses as JSON; `sc-if` open/close balanced (163 → 166); line endings unchanged (397 LF, 0 CRLF); +655 bytes.
>
> ⚠️ **Naming overlap to be aware of.** `Landing_PRD.md` §3.6 declares a `showAnnotations` prop for **`landing.html`**, which is still unwired — nothing in this batch touched `landing.html`. The prop added here is a **separate, deliberately same-named** prop on `admin.html`. If landing-side annotations are built later, keep the two consistent rather than assuming one controls both.
>
> 📋 **Not recorded in a PRD.** The feedback asks for `Admin_PRD.md` §10–11 to be updated, but that file does not exist (§G-4 / §H-3). This box is the record until that question is settled.

> ### ✅ Batch 2 done — P0-4, P0-5, P0-6
>
> **16 copy edits across both files**, all verified in the browser. Worked from the primary source: `client-feedback/Documents/BestBaby_LD3B PRIVACY 26.10.19.docx` was extracted and read rather than relying on the feedback's paraphrase. Two clauses settled the batch:
>
> - *"held in an encrypted Private Vault accessible only to you and to Moira during your sessions, and inaccessible to BestBaby staff."*
> - *"International transfers. Some of BestBaby's service providers are based outside the UK."* — this is what makes the "UK servers" claim wrong, in LD3B's own words.
>
> **The scope was wider than the feedback stated.** The named sites were 1 (P0-4) + 2 (P0-5) + 6 (P0-6) = 9. A sweep for the underlying claim found **6 more** saying the same false thing, plus a 7th in the legal copy:
>
> | Extra | File | Was | Now |
> | --- | --- | --- | --- |
> | Database › Site settings row | admin | "localStorage only, never transmitted" | "Encrypted Private Vault — inaccessible to staff" |
> | Journal hint (Finance) | landing | "figures kept on this device" | "kept in your encrypted Private Vault" |
> | Hospital-bag tool body | landing | "the list is saved on this device" | "saved in your encrypted Private Vault" |
> | Budget tool body | landing | "figures never leave this device" | "stay in your encrypted Private Vault" |
> | Finance tool reassurance | landing | "budget figures stay on your device" | "stay in your encrypted Private Vault" |
> | Notepad vault line | landing | "Only you can read them." | "Only you — and Moira, during your sessions — can read them." |
>
> Fixing only the nine named sites would have left the prototype telling users their data is on their device in six other places.
>
> **False positives deliberately left alone** — these matched the search terms but are correct:
>
> | Kept | Why |
> | --- | --- |
> | 5 × `localStorage.getItem/setItem` in `landing.html` | real JS, not copy |
> | "We don't recognise this device." / "Open it on this device" (M1) | device *recognition*, not storage |
> | "cookies are small text files a website stores on your device" | cookies genuinely are on-device |
> | "your device handles it" (editorial essay) | unrelated prose |
> | Smart Tools line already reading "Moira only sees it in the moment you ask her" | already matches LD3B — left as the model phrasing |
>
> **P0-5 — the four legitimate `affiliate` mentions all survived** (Terms disclosure, "affiliated entities" liability clause, two Privacy passages tied to *stage/family* data). Confirmed by re-grep after the edit. Only the two health-observation sites changed.
>
> **Verified in the browser at 1440×900:** app boots with no console errors; Moira Facts "Allow" and the "What Moira can see" panel both render the LD3B wording with no "affiliate" on the page; Settings › Private vault reads correctly with the UK GDPR Article 9 sentence preserved; admin GDPR checklist item 4 reads exactly as specified.
>
> ⚠️ **One change is to legal copy — please confirm with BTO.** The embedded Privacy Notice also claimed *"encrypted at rest on our servers in the UK"*, contradicting LD3B's own International-transfers clause. It now reads *"encrypted at rest, and readable only by you and by Moira during your sessions."* It was applied as a **separate patch** so it can be reverted on its own without disturbing the other 15.
>
> 📌 **Three notes for the record:**
> - The admin Database "Site settings" row was corrected in source but **is not currently rendered** — that tab draws a bespoke panel (`isSetTab`) instead of the generic key/value table, so the row appears to be superseded data.
> - LD3B spells it "personalize" (US); the prototype uses UK spelling 16:5, so the new copy uses **"personalise"** to match house style.
> - "You can withdraw at any time." was **kept** on the Moira Facts "Allow" option. The feedback's quoted LD3B wording omits it, but it is accurate per LD3B and the Withdraw control exists — say if you would rather match the quote exactly.

> ### ✅ Batch 3 done — P0-7, G-1, P0-10
>
> **7 edits in `landing.html`**, all in service of one story: BestBaby is free, requires an account during the beta, and carries clearly identified affiliate links and sponsored space.
>
> Authority taken from the primary sources, not invented:
> - **LD3A (Terms, read from the .docx):** *"By creating an account and using the Platform, Users confirm they have read and agree to these Terms"* → an account is required. And *"BestBaby is currently free to use"* — note **currently**, which the new copy preserves.
> - **LD3A + the embedded Privacy Notice:** affiliate links *"will always be clearly identified"* and *"do not cost you anything"*. The new copy mirrors that phrasing rather than inventing a disclosure.
>
> | # | Where | Was | Now |
> | --- | --- | --- | --- |
> | P0-7a | FAQ "Do I need an account?" | "**No.** …works without signing in" | "**Yes.** During the private beta you need an account…" |
> | P0-7b | FAQ "Is BestBaby free?" | "…no paywall and **no advertising**" | free, no paywall, **clearly identified affiliate links + sponsored space** |
> | G-1 | FAQ "sell my data or run ads?" | "**No, and no.** …we do not run advertising or third-party ad trackers" | "We never sell your data" + honest on sponsored space, **never targeted from the Vault or Moira's observations** |
> | G-1b | Privacy "short version" bullet | "We do not run advertising or third-party ad trackers." | "We never use anything in your Private Vault for advertising." |
> | P0-10 | Essentials Market intro | "No pressure, no upsells." | "These are affiliate links: … a small commission at no extra cost to you." |
>
> **H9 is unresolved** (ad network vs own affiliate slot), so the copy says **"sponsored space"** and deliberately never names an ad network, nor promises "no trackers" — it reads correctly whichever way H9 lands. The ad slot was confirmed present on the article page before writing the copy.
>
> **Two Batch 2 escapees fixed here.** My Batch 2 sweep was case-sensitive and missed:
> - **Press boilerplate:** *"Personal data entered into BestBaby tools stays on **the reader's own** device"* — phrasing my `this device` / `your device` search never matched, and the worst place for it, since it is the text journalists copy.
> - **Privacy "short version":** *"…and **only you can read** them"* (lower-case `only`, so my `Only you can read` search skipped it) — now carries the Moira clause.
>
> A case-insensitive re-sweep now shows **zero** remaining instances of all six wrong-claim patterns.
>
> **Statements deliberately preserved:** "never shared with advertisers" (about Moira conversations), the Terms' anti-spam clause, LD3B's "never use for marketing, advertising… unless you give permission" (about the Vault), LD3A's "currently free to use", and the press fact "Free — to read, no paywall" (still true).
>
> ⚠️ **The FAQ and Press pages are unreachable.** `goFaq` and `goPress` are defined as bindings but have **zero `{{ }}` usages** anywhere in the template, and site search indexes only Articles / Guide topics / Smart Tools. So the P0-7 and G-1 copy is corrected but **cannot currently be reached in a demo walk-through**, and the press boilerplate likewise. This belongs with **P2-4** and is listed as §G-7. It also means P0-7 could not be verified in the browser — only in source.
>
> **Verified in the browser at 1440×900:** app boots with no console errors; the Essentials Market intro renders the new affiliate disclosure with "No pressure, no upsells" gone.

> ### ✅ Batch 4 done — P0-9, plus the fix that unblocks mobile
>
> **9 edits in `landing.html`.** The copy came from the source docs, which both carry the cookie block **verbatim and identically**:
>
> > COOKIES
> > BestBaby uses cookies to make our website work. We would like to set additional cookies to understand how you use our site and to improve your experience. Please see our cookies policy for further information.
> > ☐ Accept non-essential cookies   ☐ Reject non-essential cookies   More options
>
> **The feedback slightly overstated the problem, and the docs corrected it.** It says to drop the heading; the docs show there *is* a heading — a small-caps **COOKIES** label. So the invented "Cookies on BestBaby" was replaced with that label rather than removed. "cookies policy" is now the inline link, keeping the sentence verbatim while preserving the affordance.
>
> **1D and LD1 were already correct.** They each render an inline cookie block — same copy, same COOKIES label, checkbox controls from `cookieOpts` (already labelled "Accept non-essential cookies" / "Reject non-essential cookies") and a "More options" button. **Only the global floating banner was wrong**, along with the preferences modal and the Cookies Policy page. The banner now matches those two blocks exactly, which is what "same component on the banner, 1D and LD1" asks for.
>
> | # | Where | Was | Now |
> | --- | --- | --- | --- |
> | 1 | Banner heading | "Cookies on BestBaby" (Playfair 1.25rem) | **COOKIES** eyebrow, styled to match 1D/LD1 |
> | 2 | Banner body | BestBaby's own copy | client copy verbatim, "cookies policy" linked inline |
> | 3 | Banner links row | Cookies Policy + allaboutcookies.org | removed |
> | 4–6 | Banner buttons | Accept all / Reject non-essential / Manage preferences | **Accept non-essential cookies / Reject non-essential cookies / More options** |
> | 7 | Prefs modal footnote | allaboutcookies.org sentence | removed |
> | 8 | Prefs modal button | "Accept all" | "Accept non-essential cookies" |
> | 9 | Cookies Policy "More information" | "visit www.allaboutcookies.org" | points to Cookie preferences / Settings instead |
>
> `allaboutcookies` is now **0 occurrences**. All five references gone.
>
> ⚠️ **A separate one-token fix, found while testing this at mobile width.** The required 390×844 check kept reporting a 1280×2770 viewport — the page could not render narrow. The cause: the **private-beta gate section** carried a stray `width: 1280px` *alongside* its `max-width: 80rem`. It was **the only hard-coded px width among all 50 section containers** and the only such declaration in the file, and it forced the entire document to 1280px, so **no mobile width could ever render — for the whole prototype, not just the banner**.
>
> Removing it (applied as its own patch):
>
> | Width | Before | After |
> | --- | --- | --- |
> | 1440×900 | gate inner 1280px | gate inner 1280px, centred — **identical**, since `max-width: 80rem` = 1280px |
> | 390×844 | document forced to 1280, page scaled | viewport 390, `scrollWidth` 390, **no horizontal scroll** |
> | 375×812 | same breakage | banner 343px wide, buttons on one line |
>
> Zero desktop change, full responsiveness gained. **This unblocks the "390×844" half of the feedback's own "Done means"**, which no batch could have satisfied before.
>
> **Verified at 1440×900, 390×844 and 375×812:** banner renders the client copy with the three client button labels, no `allaboutcookies`, inline policy link, no horizontal scroll at any width. (The banner only appears until a choice is stored in `localStorage` as `bb_cookie_choice` — clear it to re-test.)
>
> 📌 **Maintenance note:** the banner and the two inline blocks are **three separate pieces of markup**, not one shared component. They now agree, but a future copy change must be made in all three. Worth consolidating if the cookie wording changes again.

### P0-1 · Admin sign-in footer — internal note ✅ done

| | |
| --- | --- |
| **File** | `admin/admin.html` ≈ byte **544330** |
| **Verified** | Rendered and screenshotted — was visible on the **sign-in screen**, the first thing anyone opening admin sees |

The `<p>` ended:

> Trouble getting in? Ask a Supervisor to check your account and password in Team, or email support@bestbaby.org. **Domain pending confirmation with Loucas (P-B8).**

**Done:** gated behind `showAnnotations`, support line kept.

The note could not stay inline — an `sc-if` around the bare sentence inside the `<p>` was stripped and the text rendered anyway (see §A). It was therefore **lifted into its own `<p>`** immediately after the support paragraph, inheriting the same 11.5px/`#9C9C9C` styling with `margin:8px 0 0`. When annotations are on it now reads as its own line rather than a trailing sentence — a cosmetic change to an internal-only note.

---

### P0-2 · Admin → Articles — P-B7 banner shown to everyone ✅ done

| | |
| --- | --- |
| **File** | `admin/admin.html` ≈ byte **564403** |
| **Verified** | Rendered — banner sat above the Articles table for every role |

Markup is a `div` with `border:1px dashed #E8E1D7`, a monospace `P-B7` chip and the "Aspect labels here are pending a character-for-character check…" paragraph.

**Done:** the whole dashed-border `div` (chip + paragraph, 710 chars) is wrapped in `<sc-if value="{{ showAnnotations }}" hint-placeholder-val="{{ false }}">`. Block-level, so the gate holds.

---

### P0-3 · Admin → New article, Rewrite panel — open question in the UI ✅ done

| | |
| --- | --- |
| **File** | `admin/admin.html` ≈ byte **604532** |
| **Markup** | `div` with `border:1px dashed #C8D9CC` |

> **Open question:** is "Rewrite in BestBaby voice" a different rewrite from Morpheus rewriting? Confirm before building them as separate behaviours.

**Done:** the dashed-border `div` (317 chars) is wrapped in the same block-level `sc-if`. The question itself stays tracked in feedback §5; the surrounding Rewrite panel and its "Morpheus returns a draft you edit — it never publishes on its own" copy are untouched.

---

### P0-4 · Admin → Stories GDPR checklist, item 4 ✅ done

| | |
| --- | --- |
| **File** | `admin/admin.html` ≈ byte **850122** |
| **Location** | **JS data array**, not markup — the `GDPR` checklist constant |

Was:

```js
{ title: "Journal privacy.", text: "Confirm journal entries stay in localStorage and are never transmitted." }
```

**Done —** `text` now reads:

> Confirm story submissions never include Journal or Private Vault content.

Source: LD3B §1–2. Verified rendering on the admin Stories screen.

---

### P0-5 · Moira Facts — "affiliate offers" on health observations ✅ done

| | |
| --- | --- |
| **File** | `landing.html`, **2 hits** (matches feedback exactly) |

| # | Offset | Context |
| --- | --- | --- |
| 1 | **7665579** | Markup — "What Moira can see" panel (renders on Journal › Personal information) |
| 2 | **7904484** | JS `FACT_OPTIONS` array, `key:"allow"` |

**Done —** both now use the LD3B wording, with "affiliate offers" removed:

> The observation to be used by BestBaby and Moira to personalise your experience and communications. BestBaby will only use this in the ways you have agreed to and will never share it with third parties for their own marketing purposes.

> ⚠️ **"affiliate" was NOT stripped globally** — 4 of the 6 occurrences are correct and were preserved:
> - **7929305** (Terms) — affiliate recommendations "will be clearly identified as such"
> - **7930792** — "affiliated entities" in a liability clause, unrelated
> - **7946278** and **7946840** (Privacy) — affiliate offers tied to **journey stage and family situation** data
>
> The violation is specifically **health observations** driving affiliate products. Stage/family data driving them is what the signed privacy notice describes. A blanket find-and-replace would have broken the legal copy and contradicted P0-10, which *requires* affiliate disclosure.

---

### P0-6 · Privacy copy — four contradictions of LD3B ✅ done

All in `landing.html`.

| Sub | Offset | Where | Was |
| --- | --- | --- | --- |
| (a) | **7444754** | Notepad empty state | "Write one above — **it stays on this device**." |
| (b) | **7999797** | JS tool-body fallback | `desc + " Everything you enter stays on this device."` |
| (c) | **7775768** | Settings → Private vault | "stored encrypted **on our UK servers. Only you can read them.**" |
| (c) | **7889725** | `FAQS` — "What happens to what I type into the tools?" | "encrypted **on our UK servers**, readable only by you" |
| (d) | **7396511** | SSHP "Smart tools for this stage" | "encrypted and **visible only to you**" |
| (d) | **7694616** | Tools index page | "encrypted in your Private Vault and **visible only to you**" |

**Done —** all six now use Private Vault wording with the Moira-during-sessions clause, e.g.:

> Stored encrypted in your Private Vault. Only you — and Moira, during your sessions — can read it.

"UK servers", "on our servers" and "visible only to you" are now **0 occurrences** in `landing.html`. The UK GDPR Article 9 sentence was **kept** wherever it appeared — that part is accurate. (b) is a JS concatenation, so the fix applies to every tool with no custom body.

See the Batch 2 box for the six **additional** sites found making the same claim.

---

### P0-7 · FAQ — two answers that are simply wrong ✅ done

| | |
| --- | --- |
| **File** | `landing.html`, `FAQS` array |

Both answers rewritten, plus the third (§G-1) and the Privacy bullet that said the same thing. See the Batch 3 box for the before/after table and the LD3A clauses that authorise the new wording.

> ⚠️ **Corrected but not reachable.** The FAQ route has no link anywhere in the template (§G-7), so this copy cannot be seen in a demo walk-through until P2-4 gives it a way in. Verified in source only.

---

### P0-8 · AI-generator watermark ⏸ blocked on replacement assets

**This is one asset, not three.** `stageImg2` is referenced **once** in the app, at ≈ 7813309:

```js
image: (typeof window !== "undefined" && window.__resources && window.__resources.stageImg2) || "assets/childbirth-banner.png"
```

…as `STAGES.birth.image`. The Birth SSHP banner, Birth article header and interior image all read that one field. **Replacing the single manifest entry fixes all three placements.**

#### Full image audit (Batch 5)

Every bundled image re-examined — not just viewed, but parsed for true format and embedded provenance. There are no inline `data:` images above 5 KB, so this is the complete inventory.

| Asset | Declared | **Actual** | Dimensions | AI provenance | Verdict |
| --- | --- | --- | --- | --- | --- |
| `stageImg0` Before Pregnancy | png | PNG | 1408×768 | — | clean |
| `stageImg1` placeholder | png | **JPEG** | 272×186 | — | clean; mime mislabelled |
| **`stageImg2` Birth** | png | **JPEG** | **1376×768** | **MiniMax, AIGC Label 1** | **visible watermark + metadata — replace** |
| **`stageImg3` First Years** | png | **JPEG** | **1376×768** | **MiniMax, AIGC Label 1** | **no visible watermark, but same AI provenance — see below** |
| `546b0682` Pregnancy | jpeg | JPEG | 1920×1080 | — | clean |
| `c03b5608` Finance | png | PNG | 800×600 | — | clean, but US dollars (§G-2) |
| `247b4630` Moira silhouette | png | PNG | 636×548 | — | clean |

Three findings the original pass missed:

1. **`stageImg3` (First Years) is also MiniMax-generated.** I earlier called it "clean" from looking at it — and visually it is, there is no watermark. But it carries the same embedded `{"AIGC":{"Label":"1","ContentProducer":"MiniMax"…}}` block as the Birth image. So "check all other images" turns up a **second** AI-generated stage image, not zero.
2. **The watermark is not the only marker.** `stageImg2` carries machine-readable AI provenance in an APP11/JUMBF segment. Removing the visible watermark would leave the file still declaring itself MiniMax-generated to any C2PA-aware tool (Chrome Content Credentials, Adobe, etc.).
3. **Three assets are mislabelled** `image/png` when they are actually JPEG (`stageImg1/2/3`). Harmless — browsers sniff content — but a replacement script keyed on the declared mime would propagate the error. The swap tool below sets mime from the file's real magic bytes.

#### Why this is not being "fixed" by cropping

The watermark sits bottom-right and could be cropped out. I have not done that, for two reasons worth a decision rather than an assumption:

- **Re-encoding strips the C2PA/AIGC provenance as a side effect.** That metadata is what marks the image as AI-generated. Removing it so AI imagery reads as photography is a disclosure decision on a health and parenting platform whose Terms promise evidence-based content — and whose own admin console has an "AI content watermark — metadata written on every AI-generated record" setting. Not a call to make silently.
- **The watermark is MiniMax's branding**, and free-tier generators generally require it. Removing it may breach their terms. That is a licensing question for BestBaby, not a design tweak.

**Options, for Loucas / BTO:**

| | Option | Notes |
| --- | --- | --- |
| **A** | Replace both with licensed stock or commissioned photography | Cleanest. Needs assets. **Recommended** |
| **B** | Re-generate on a MiniMax plan whose licence allows no watermark | Keeps the look; client cost; still AI, so still wants disclosure |
| **C** | Crop the watermark off `stageImg2` | Fast, but strips provenance and may breach MiniMax's terms. Leaves `stageImg3` untouched either way |

#### Sourcing spec — what a replacement needs

| | `stageImg2` (Birth) | `stageImg3` (First Years) | `c03b5608` (Finance, §G-2) |
| --- | --- | --- | --- |
| Size | **1376×768** or larger | **1376×768** or larger | **800×600** or larger |
| Aspect | 1.79 (≈16:9) | 1.79 (≈16:9) | 1.33 (4:3) |
| Format | JPEG or PNG | JPEG or PNG | JPEG or PNG |
| Budget | ≤ ~800 KB each, or the bundle grows | | |
| Subject | Birth / maternity setting, calm not clinical-alarming | Toddler / early years | Household budgeting — **£ sterling, not $** |

The layout uses `object-fit: cover` at roughly 16:9, so keep the subject centred; anything far off 1.79 will crop unpredictably. The tool warns when the aspect ratio shifts by more than 0.02.

#### Ready to go: `tools/swap-bundle-image.py`

Written and **tested end-to-end** this batch (dry run, real write to a throwaway copy, and the swapped bundle re-rendered cleanly in the browser with no console errors). It edits only the manifest line — a structural diff of a swapped bundle showed line 370 changed and all other 384 lines byte-identical.

```bash
python tools/swap-bundle-image.py --list
python tools/swap-bundle-image.py --target stageImg2 --file birth.jpg --dry-run
python tools/swap-bundle-image.py --target stageImg2 --file birth.jpg
```

It resolves friendly names or UUID prefixes, sets the declared mime from the real magic bytes, warns on aspect-ratio and resolution changes, **warns if the replacement itself carries AI provenance**, backs up to `.bak`, and writes via a temp file so a failed write cannot truncate the bundle.

---

### P0-9 · Cookie banner — use the client's copy ✅ done

| | |
| --- | --- |
| **File** | `landing.html`, the `<sc-if value="{{ cookieBanner }}">` block, the preferences modal, and the Cookies Policy doc |

Nine edits; see the Batch 4 box for the full before/after table, the verbatim doc copy, and the three widths it was checked at.

Headlines:
- The **COOKIES** label was kept (the docs have one — the feedback's "remove the heading" was a half-step).
- **1D and LD1 needed no change** — they were already correct. Only the floating banner, the prefs modal and the policy page were wrong.
- `allaboutcookies` is now **0 occurrences** across all five references.

> The choice is remembered in `localStorage` as `bb_cookie_choice`, so once dismissed the banner will not reappear — clear it to re-test.

---

### P0-10 · Essentials Market — no affiliate disclosure ✅ done

| | |
| --- | --- |
| **File** | `landing.html` ≈ **7677600** |

Was:

> Thoughtfully designed products made with the same evidence-based care as the guidance. **No pressure, no upsells.**

**Done —** now reads:

> Thoughtfully designed products, chosen with the same evidence-based care as the guidance. These are affiliate links: if you buy through one, BestBaby may earn a small commission at no extra cost to you. That is how we keep the platform free, and it never affects what we recommend.

Mirrors the Terms clause and the Privacy Notice's "at no cost to you / does not affect our editorial content" phrasing, so all three now agree. **Verified rendering** on the Market page.

---

## C. P1 — public site

### P1-1 · Missing screens — all four confirmed absent

Grep across `landing.html`: `Tier 3` **0**, `Tier 4` **0**, `Safety Care` **0**, `Your consents` **0**, `consents` **0**, `emergency contact` **0**. Nothing to edit — these are **new builds**.

| | Screen | Placeholder scope |
| --- | --- | --- |
| (a) | Tier 3 safety message | Inside the Moira drawer |
| (b) | Tier 4 **Safety Care** screen | Short message + crisis-resources block + 2 buttons back to SSLP |
| (c) | **"Your consents"** card | Settings, with a Withdraw button |
| (d) | **Emergency contact** card | Settings, optional |

Placeholder copy is fine (signed plan M2-D8–D10; LD2; LD3B). `Withdraw` already exists as a binding (8 uses in Moira Facts), so (c) can reuse that interaction pattern.

> The Settings page has no `consents` concept at all, so (c) and (d) are new cards in the Settings layout rather than edits to existing ones.

---

### P1-2 · Birth SSHP layout — measured, and the target is at risk

Measured at **1440×900** (rendered, JS-measured, fold = 900 px):

| Element | Top (px) | Status |
| --- | --- | --- |
| Hero section | 136 (height **458**) | |
| H1 "Birth is unpredictable…" | 211 | above fold |
| Banner image (578×289) | 174 | above fold |
| Moira invite box (height 180) | 381 | above fold |
| "Featured articles" heading | 626 | above fold |
| Featured card images | 781 (height 163) | **top 119 px visible** |
| Card kicker "Your Birth Choices" | 978 | **78 px below** |
| Card title "Exploring water birth…" | 1002 | **102 px below** |
| Card blurb | 1087 | **187 px below** |
| **"Your birth guide"** | **1409** | **509 px below** |

This reproduces Loucas's complaint exactly: only the heading and image tops clear the fold.

**Required:** featured cards **with blurbs** *and* the top of "Your birth guide" visible at 1440×900 → **"Your birth guide" must move from 1409 to ≤ ~880, a reclaim of ~530 px.**

> ⚠️ **The stated target likely isn't reachable by compacting the header alone.** Best-case budget:
>
> | Source | Realistic saving |
> | --- | --- |
> | Hero 458 → ~240 (smaller banner; explainer + Moira invite in one row) | ~218 px |
> | Tighter featured cards (image 163 → ~120, less padding) | ~90 px |
> | Section gap 1254 → 1409 cut to ~60 px | ~95 px |
> | Trim nav/trust band above hero | ~30 px |
> | **Total** | **~433 px** |
>
> That leaves roughly **100 px short**. Closing it needs one of: a more compact featured-card design (shorter blurb clamp), or reading "just a hint of Your Birth Guide" as the section's top edge/background rather than its heading. **Worth settling with Supreet before building** — see §H-1. The header compaction itself should proceed either way; it is the bulk of the win.

Loucas is sending a screenshot of his live Birth page — wait for it before finalising the header composition.

---

### P1-3 · SSLP Smart Tools section too tall

Measured on the SSLP at 1440×900:

| | |
| --- | --- |
| Section "Your Smart Tools" | top **2358**, height **469 px** |
| Phone mock block | top 2406, **373 × 385 px** |
| "Watch the tour" button | top **2726** (markup ≈ `landing.html` 7368646) |

**Change:**
1. Section height **469 → ~235 px** ("about half").
2. Shrink the phone mock proportionally (~373 → ~190 px).
3. Relabel **"Watch the tour"** → **"Smart Tools index video"** (currently the only occurrence of that string in the file).

---

### P1-4 · Moira disclaimer truncated — 3 markup sites cover 6 rendered places

The full disclaimer appears **9 times, always complete** (both sentences). The truncated version is a *different, shorter string* — `"Moira is an AI-powered companion. She is not a doctor, midwife, or medical professional."` with no second sentence:

| # | Offset | Location |
| --- | --- | --- |
| 1 | **7358265** | SSLP stage section Moira box |
| 2 | **7376913** | SSHP header Moira box |
| 3 | **7410169** | Article sidebar Moira box |

> The feedback names six places (SSLP + four SSHP headers + article sidebar). There are only **three markup sites** because the four SSHP headers render from one looped template. **Three edits fix all six.** Verified on the rendered Birth page: the Moira invite shows only the first sentence.

**Change:** append the second sentence —

> The guidance she provides is for informational and support purposes only. Always consult a qualified healthcare professional for medical advice.

— or link the short line to the full text. Two further short variants at 7888907 (FAQ) and 7896173 (Privacy) are **correct in context** and should be left alone; the FAQ one already carries "Always consult…" in the following paragraph.

---

### P1-5 · Off-palette cocoa and slate

`landing.html` — cocoa `#8B5E3C` **×5**, slate `#7A8B9A` **×4**:

| Offset | Where | Note |
| --- | --- | --- |
| 7444623 | Notepad "No notes yet." | cocoa |
| 7458365 | Notepad entry date | cocoa |
| 7849536 | Contacts — "Mum" / Family (`color`/`dark`/`tint`) | cocoa |
| 7906038 | Stories — entry tagged `stage:"Pregnancy"` | cocoa — should be Pregnancy `#E0A030` |
| 7849733, 7849950 | Contacts — Work, School/daycare | slate |
| 7906635 | Stories — entry tagged `stage:"First Years"` | slate — should be First Years `#377A91` |
| **7719800, 7719934** | **Press-kit "Stage palette" swatch** | **not named in the feedback** — see §G-3 |

Targets from `Landing_PRD.md` §2.1–2.2. The Stories entries carry an explicit `stage:` field, so they map directly onto stage tokens. Contacts categories are **not** stages — they need feature tokens or a neutral, chosen deliberately rather than by find-and-replace. Each entry has paired `color` / `dark` / `tint` values; update all three together.

> Offsets shifted slightly after Batch 2 — re-grep the hex values rather than seeking to these numbers.

---

### P1-6 · Finance colour too close to First Years teal

Finance `#1F6F76` vs First Years `#377A91`. Full colour family in `landing.html`:

| Token | Role | Count |
| --- | --- | --- |
| `#1F6F76` | base | **31** |
| `#13565C` | dark / hover | **13** |
| `#E5F0F1` | tint | **9** |
| | **Total** | **53** |

**Change:** Finance is a Smart Tool → move to Smart Tools rust `#A0522D` (§2.2), or another clearly distinct hue.

> **All 53 must move together.** Swapping only the 31 base occurrences leaves hover states and tinted panels teal. And `#A0522D` has **no documented dark or tint** in §2.2 — those must be defined and recorded in the PRD. Existing rusts in the file: `#A0522D` ×9, `#A35F43` ×7.
>
> Also note First Years' tint is `#E5F1F5` while Finance's is `#E5F0F1` — one character apart. Easy to mis-grep; use exact matches.

---

## D. P1 — admin

### A1-1 · Admin stage colours are the old palette

Counts in `admin/admin.html` confirm the old palette throughout and **zero** of the new tokens:

| Role | Old (present) | New target (§2.1–2.2) | Present? |
| --- | --- | --- | --- |
| Before Pregnancy | `#B07D8E` ×2 | `#B5838D` | 0 |
| Pregnancy | `#C2872F` ×1 | `#E0A030` | 0 |
| Birth | `#B34A2A` ×6 | `#C8382A` | 0 |
| First Years | `#4E7C85` ×1 | `#377A91` | 0 |
| Connection & Growth | `#4A3DB5` ×4 | `#7B2FF2` | 0 |
| Moira | `#4F6F52` ×5 | `#1E3A2B` | 0 |

**Change:** replace each old token with its §2.1–2.2 equivalent (19 occurrences total).

> ✅ **Good news found while doing Batch 1:** admin's palette is centralised in a single `const C = {…}` object just after the `data-props` tag — `before`, `preg`, `birth`, `first`, `moira`, `indigo`, `slate`, `cta` are each defined once there and referenced as `C.birth` etc. So A1-1 is mostly **a handful of edits in one object**, not 19 scattered replacements. Check for hard-coded hexes outside `C` before declaring it done.
>
> ⚠️ **`#1E3A2B` already appears 19× in admin** as the brand dark-green (`C.cta`), unrelated to Moira. Change `C.moira` from `#4F6F52` to `#1E3A2B`; do **not** treat existing `#1E3A2B` uses as already-migrated Moira styling.
>
> Note also that admin keeps separate "ink" variants (`pregInk`, `firstInk`) used for small label text on tints, with a comment explaining why. Preserve that distinction when swapping — the raw stage hue is for swatches and bars, the ink for text.

---

## E. P2 — polish

### P2-1 · SSLP fold

Measured at 1440×900:

| Element | Top (px) | |
| --- | --- | --- |
| Trust bar | 112 (height **55**) | |
| Hero section | 178 (height **463**) | ends 641 |
| "Latest for you" heading | **730** | above fold |
| Card block | 787 (height 532) | |
| Card image | 791 (height 202) | |
| Card kicker | 1012 | **112 px below** |
| **Card title** | **1049** | **149 px below** |

At **1366×768** the heading at 730 is barely visible and every card is below the fold — matching the complaint that the whole stage section is below the fold.

**Change:** reclaim **~160 px** from the header block + trust-bar description height so the card title clears 900. Smaller than P1-2's budget and comfortably achievable: trust bar 55 → ~36 and hero 463 → ~330 gets there.

---

### P2-2 · Per-page footers, and hide Admin

| | |
| --- | --- |
| **File** | `landing.html` ≈ **7777648** — `<a href="admin/admin.html">Admin</a>` |
| **Verified** | Rendered — the Admin link is in the global footer on signed-in pages |

There is **one** global footer in the markup, used by onboarding, 1D and M1. Required per-page footers (`Landing_PRD.md` §3.5):

| Page | Footer links |
| --- | --- |
| 1D Join the Beta | Privacy Notice · Terms of Use · Medical Disclaimer |
| LD1 Welcome | Privacy Notice · Terms of Use · Cookies Policy |
| LD2 Registration | BestBaby.Org Ltd · BetaContact@BestBaby.org · www.BestBaby.org |
| M1 Magic key | Company line only |

**Change:** make the footer variant-aware (an `sc-if` per route, or a footer-variant prop) and omit **Admin** on all four. §3.5 is already flagged *"to be discussed, and must be cleaned up before beta"* — this closes it.

---

### P2-3 · LD2 Continue should be disabled until Part 1 is ticked

`Still needed` appears **3×** in `landing.html` — the current pattern is an enabled-looking button that reports what's missing on click.

**Change:** render Continue greyed out (reduced opacity, `cursor:not-allowed`, `aria-disabled`) until the Part 1 consent box **and** required fields are complete. Doc: *"Continue is only active once the Part 1 consent box above is ticked."* Keep the "Still needed…" text as the explanation once enabled-but-incomplete, or drop it if the disabled state is self-explanatory.

---

### P2-4 · Click-through dead ends

Five separate defects; each needs its own fix:

| # | Defect | Note |
| --- | --- | --- |
| 1 | Guide cards and blog stories all open the same first article | Routing ignores the clicked item |
| 2 | "Open in your journal →" doesn't select the tool | 1 occurrence in `landing.html` |
| 3 | Search hits for guide topics land at the top of the stage page | Needs anchor/deep-link |
| 4 | Reviewer "Not available" page offers "Go to Dashboard", which Reviewers can't open | `admin/admin.html`, 1 occurrence each |
| 5 | Escape doesn't close most admin modals | Only **2** `keydown` handlers in the whole admin file — most modals have none |
| **6** | **FAQ and Press pages have no link at all** (§G-7) — found during Batch 3 | `goFaq` / `goPress` defined, never used; search doesn't index them |

(5) is the broadest: it needs a shared Escape handler across the modal components rather than five one-off patches. (6) matters more than it looks — **P0-7 is a P0 whose corrected copy nobody can reach** until the FAQ gets a link.

---

### P2-5 · Admin article rows — Stage and Category as dropdowns

| | |
| --- | --- |
| **Verified** | Rendered the Articles table as Supervisor |

Table columns are **TITLE · STAGE · ASPECT · EVIDENCE · STATUS**. Stage ("Birth", "First Years", "Pregnancy") and Aspect render as plain text. Filter dropdowns above the table already exist for *All stages / All categories / All aspects*, so `stageChips`, `catOptions` and `aspectOptions` are available to reuse as in-row `<sc-raw-select>` controls.

> ❓ **The table has no "Category" column** — it has **Aspect**. "Category" exists as a separate filter. So P2-5's "Stage and Category" is ambiguous: it may mean the Stage + Aspect columns as rendered, or Loucas may want a Category column added. **Needs confirming** — §H-2.

---

## F. Hold — verified present, do NOT change

All 11 confirmed in place; listed so a later pass doesn't "tidy" them by accident.

| # | Topic | Verified state |
| --- | --- | --- |
| H1 | Sign-in screen | Gate asks email + site password; Settings text matches |
| H2 | Moira consent prompts | No screen exists (0 hits) — correct, awaiting BTO |
| H3 | Moira Facts "Allow" option | Present in `FACT_OPTIONS`. **Batch 2 edited its wording only — the option itself stays** |
| H4 | Trust-bar labels | "Your Privacy First… Evidence-Based" (LP0) vs "Privacy First… Evidence Informed" (app) — both present, faithful to FE |
| H5 | "Terms of Service" vs "Terms of Use" | Mixed, as in the docs. Footer currently renders "Terms of Use" |
| H6 | "AI Created" evidence tier | Selectable in the editor, hidden from the filter |
| H7 | LD4 questionnaire | DOB free text; no partner-name field |
| H8 | LD2 copy | "Collected solely to process your application…" present |
| H9 | Ad space | 300×250 slot on the article page. **Note P0-7 must acknowledge it without committing to an ad network** |
| H10 | Team passwords | Masked with Show / Change (`m.pwShown`, `m.togglePw`) |
| H11 | Dialogue / Blog / Forum, admin Stories | Built; Phase 2 — no further effort |

**§6 "don't regress" — regression checklist for after the work:** header in user's stage colour with body in viewed stage colour · Journey dropdown solid colour bars · trust bar with SSLP-only descriptions · SSLP section order and verbatim Smart Tools / Moira / "Where science meets real life" copy · SSHP "{Stage} in Three Minutes", text Moira in headers, 4 featured cards with **full** blurbs, guide titles, "People often start with" · article page header bar, ⅔+⅓ with matching articles, Moira and ad space · Voice Moira on every signed-in page and none in onboarding · 1D has no journey questions · LD1/LD2/LD4 screens, SMS revealing a mobile field, trimester pre-selection · legal overlays without internal comments · admin pipeline, roles, For review / Pre-Published, Notifications with beta applications, Latest activity, no insights widgets.

> P1-2 and P2-1 both compact layouts that §6 protects (full blurbs, SSLP section order). Re-check this list after those two land — they are the most likely to cause a regression.

---

## G. Findings not in the feedback

| # | Finding | Recommendation |
| --- | --- | --- |
| **G-1** | **Third contradictory FAQ.** *"Do you sell my data or run ads?"* → *"No, and no."* contradicts the ad slot exactly as P0-7's two answers do | ✅ Fixed in Batch 3, together with a fourth instance in the Privacy "short version" bullets |
| **G-2** | **Finance image shows US dollars** (`c03b5608`, 800×600 PNG, no AI provenance): US banknotes and a `$` calculator, in a product that is UK-only throughout | ⏸ Needs a £-sterling replacement. Cropping cannot fix this — the dollars are central to the composition. Spec and tooling ready (see P0-8) |
| **G-3** | **Press-kit "Stage palette" swatch still shows the old palette** (7719800, 7719934): cocoa and slate presented as the official stage colours on the press page | Add to **P1-5**. A press kit publishing the wrong palette is worse than internal drift |
| **G-4** | **`Admin_PRD.md` does not exist.** The feedback's "update `Admin_PRD.md` §10–11" has no target | Confirm whether it was never committed or lives elsewhere — §H-3 |
| **G-5** | **`showAnnotations` declared but unused** (`Landing_PRD.md` §3.6, default `true`) | ✅ Applied for admin in Batch 1 as a separate same-named prop. The **landing-side** prop in §3.6 is still unwired |
| **G-6** | **Six more "on this device" / localStorage claims** beyond the six P0-6 names, plus the Privacy Notice's "UK servers" | ✅ Fixed in Batch 2, plus **two more** caught in Batch 3 that a case-sensitive search had missed |
| **G-9** | **`stageImg3` (First Years) is also MiniMax AI-generated** — same embedded AIGC provenance as the Birth image, but no visible watermark, so a visual check alone misses it. My first pass wrongly called it clean | Decide with P0-8: replace, or accept AI imagery with disclosure |
| **G-10** | **Three assets declare `image/png` but are JPEG** (`stageImg1/2/3`) | Cosmetic; browsers sniff. `tools/swap-bundle-image.py` corrects mime on any future swap |
| **G-8** | **A stray `width: 1280px`** on the private-beta gate section forced the whole document to 1280px, so no mobile width could render — the only hard-coded px width among 50 section containers | ✅ Removed in Batch 4. Desktop unchanged (`max-width: 80rem` = 1280px); 390×844 and 375×812 now render with no horizontal scroll |
| **G-7** | **The FAQ and Press pages are unreachable.** `goFaq` and `goPress` are defined as bindings but used **zero** times in the template; site search covers only Articles / Guide topics / Smart Tools | Add to **P2-4**. P0-7's corrected copy is invisible until there is a link. Other `go*` bindings also show zero direct uses but are reached via the generic `item.go` nav list, so the whole list needs checking rather than assuming all are dead |

---

## H. Questions to settle

1. **P1-2 target is ~100 px short** of what header compaction alone can deliver (see measurements). Accept a tighter featured-card design, or read "a hint of Your Birth Guide" as the section edge rather than the heading? *Also: Loucas's Birth-page screenshot hasn't arrived.*
2. **P2-5** — "Stage and **Category**" dropdowns, but the table renders Stage and **Aspect**. Which does Loucas mean, and should a Category column be added?
3. **`Admin_PRD.md`** is missing (G-4). Where should admin items be recorded?
4. **P0-9** — confirm the cookie banner currently renders on **1D** and **LD1**. If not, the component needs adding there, which is more than a copy change.
5. **Batch 2's legal-copy change** — the embedded Privacy Notice no longer claims UK servers. Needs BTO's nod; it is a separate patch and can be reverted alone.

---

## I. Suggested order

Grouped so related edits land together and each batch is independently checkable.

| Batch | Items | Why grouped |
| --- | --- | --- |
| ~~**1 — Internal notes**~~ ✅ | ~~P0-1, P0-2, P0-3~~ | **Done** — `showAnnotations` prop, default `false`, verified both ways |
| ~~**2 — Privacy & consent copy**~~ ✅ | ~~P0-4, P0-5, P0-6~~ | **Done** — 16 edits (9 named + 7 found); LD3B read from the .docx |
| ~~**3 — Commercial honesty**~~ ✅ | ~~P0-7 + G-1, P0-10~~ | **Done** — 7 edits; LD3A read from the .docx; 2 Batch 2 escapees swept up |
| ~~**4 — Cookie banner**~~ ✅ | ~~P0-9~~ | **Done** — 9 edits; 1D/LD1 were already right; plus the `width: 1280px` fix that unblocks mobile |
| **5 — Images** ⏸ | P0-8 **+ G-2 + G-9** | **Audited and tooled; blocked on assets.** Two AI-generated stage images and one US-dollars image need replacing — see P0-8 for the spec, options and `tools/swap-bundle-image.py` |
| **6 — Colour tokens** | P1-5 **+ G-3**, P1-6, A1-1 | Mechanical, high regression risk — do in one pass and re-screenshot every stage |
| **7 — Layout** | P1-2, P1-3, P2-1 | All fold work; measure at all three widths together. **Blocked on H-1** |
| **8 — Copy & new screens** | P1-4, P1-1 | P1-4 is 3 small edits; P1-1 is the only net-new build |
| **9 — Polish** | P2-2, P2-3, P2-4, P2-5 | Independent; P2-4 (5) and P2-5 are the largest. **P2-5 blocked on H-2** |

**Done means** (feedback): correct at **1440×900, 1366×768 and 390×844**, and no internal notes visible with default props. **390×844 was impossible to test until Batch 4** removed the stray fixed width (§G-8); the cookie banner has now been checked there, but **everything landed in Batches 1–3 still needs a mobile pass**, and 1366×768 has only been used for measurement, not sign-off.

After each batch, update the matching row in `Landing_PRD.md` §12 (and `Admin_PRD.md` §10–11 once H-3 is resolved).
