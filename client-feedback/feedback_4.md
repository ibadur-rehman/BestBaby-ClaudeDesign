# BestBaby UI prototypes — review feedback, round 3 (30 Oct 2026, afternoon)

**For:** Ibadur (implementation in Claude Code)
**From:** Supreet
**Verified:** live https://best-baby.vercel.app/ and `/admin` as re-deployed on 30 Oct afternoon. Templates, loader and resources were hashed and matched against the live files. Diffed against the round-2 build, then clicked through.

**Scope (unchanged):** UI prototype only — layout, copy, colours, images, click-through. Demo data only needs to be plausible.

---

## 1. Summary

Good round — most of round 2 is closed. **Five items are left, and one new small issue.** The watermarked image is the one to prioritise, since it's visible to anyone who opens a Birth page.

| Status | Items |
|---|---|
| ✅ Closed this round | N1 Admin footer link (→ `/admin`, hidden on 1D / onboarding / M1) · N2 admin Back to site (→ `/`) · N4 Stage dropdown (4 stages only) · P1-1 Tier 3 message (correct urgent copy, Call 111 / 999, reachable via toggle) · P1-5 Pregnancy story colour · P2-2 per-page footers · P2-4 Reviewer button (→ For review), blog stories open different articles, tool deep-link, guide-topic search hits · plus the optional items: consents "Not given", Shout / NHS 111 labels, signed-plan button wording, emoji removed, Finance teal tints, Contacts neutrals |
| 🟡 Still open | R1 watermark · R2 Safety Care screen unreachable · R3 Smart Tools size · R4 guide cards · R5 Birth fold |
| 🆕 New (small) | X1 broken editor props · X2 Tier 3 toggle visible to everyone |

---

## 2. Still open

| # | Where | Now | Fix |
|---|---|---|---|
| R1 | **AI watermark ("MINIMAX \| Hailuo AI")** | The image file is still the same bytes; only the crop changed (`object-position: center 20%`). The mark is still clearly visible on **all four Birth featured cards** and on the **article interior image** | Replace the image asset (re-export a cropped or clean version) instead of adjusting the CSS crop. Recheck every place the image appears |
| R2 | **Safety Care screen (Tier 4)** | Built and the content is right, but nothing in the walk-through opens it. It's only selectable as `startRoute: "safety-care"` in the editor props, and that props block is broken (X1) | Add a visible demo entry point, e.g. a small link inside the Tier 3 notice, *"Demo: show Tier 4 Safety Care screen"*, or a build-controls toggle |
| R3 | **SSLP Smart Tools section** | 475 px tall at 1440 wide (469 in round 1, 492 in round 2), so effectively unchanged. Loucas: *"too big overall"* | Aim for about half: e.g. 32 px vertical padding and a smaller phone (~130 px wide, or show only its top half). Target ≤ 280 px tall at 1440×900 |
| R4 | **Guide cards ("Explore →")** | All guide cards on the stage home page still open the same first article ("Navigating the financial landscape of adoption") | Give each guide card its own article (any plausible article from the same stage is fine) |
| R5 | **Birth SSHP fold** | Better: at 1440×900 the four featured titles show, plus the first line of one blurb. The top of "Your birth guide" is still below the fold | One more step: e.g. shorter featured-card images on Birth only (16:9 → 21:9), so the blurbs and a hint of the guide show |

---

## 3. New in this round (small)

| # | Where | Problem | Fix |
|---|---|---|---|
| X1 | Landing page editor props (`data-props` on the `text/x-dc` script) | The `startRoute` options list is garbled (repeated `"nr7","cookies"quot;…` fragments), so the props JSON no longer parses. The live site still renders, but the editor's props panel (and the `safety-care` option) will likely fail | Restore valid JSON: `[..., "nr7", "cookies", "safety-care"]` |
| X2 | "Toggle Tier 3 safety notice" button | Shown to every user under the Moira boxes on the SSLP, SSHP and article page — a dev control in client-facing UI | Show it only when `showBuildControls` is on, or label it **"Demo: show Tier 3 notice"** so Loucas knows it's a review aid |

---

## 4. Optional — leftovers (only if time allows)

- Admin row Aspect dropdown lists aspects that don't match the 11 in `Admin_PRD.md` §6.2 (e.g. it has "Environmental & Safety", "Sexual & Reproductive", "Rights & Advocacy" and is missing "Decision-making & Options", "Expert Research", "Stories & Experience").
- Admin expanded row: Category still plain text (round-2 P2-5).
- SSLP fold at 1440×900: the "Latest for you" heading shows, but not the card titles.
- 1D / LD1 / M1 company line now uses the LD2 variant (BetaContact email). The client's 1D, LD1 and M1 pages use *"BestBaby.Org Ltd · Registered in Scotland · SC899830"*.
- Privacy page line *"Moira only sees an entry in the moment you ask her about it"* vs journal observations in Moira Facts.

---

## 5. Hold — decisions pending (do NOT change yet)

Unchanged: H1 gate "site password" copy · H2 Moira consent prompts · H3 Moira Facts "Allow" · H4 trust-bar labels · H5 Terms of Service vs Terms of Use · H6 "AI Created" tier · H7 LD4 logic/copy · H8 LD2 copy · H9 ad space · H10 Team passwords · H11 Dialogue / Blog / Forum and Stories (Phase 2).
