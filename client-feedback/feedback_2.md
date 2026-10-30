# BestBaby UI prototypes — review feedback, round 2 (30 Oct 2026)

**For:** Ibadur (implementation in Claude Code)
**From:** Supreet
**Verified:** live https://best-baby.vercel.app/ and `/admin` as deployed on 30 Oct (bundle templates hashed and matched against the live files). Round 1 was 26 Oct.
**How:** diffed both templates against the 26 Oct bundle, then clicked through at 1440×900, 1366×768 and 390×844, including onboarding, Settings, Birth SSHP, article page and admin as all four roles.

**Scope (unchanged):** UI prototype only — layout, copy, colours, images, click-through. Demo data only needs to be plausible. No backend items.

---

## 1. Summary

| Status | Items |
|---|---|
| ✅ Closed | P0-1, P0-2, P0-3, P0-4, P0-5, P0-6, P0-7, P0-9, P0-10, P1-4, A1-1, P2-3 (see note) |
| 🟡 Partly done | P0-8 watermarks, P1-1 missing screens, P1-2 Birth layout, P1-5 colours, P1-6 Finance colour, P2-1 SSLP fold, P2-2 footers, P2-4 dead ends, P2-5 admin dropdowns |
| ❌ Not done | P1-3 Smart Tools section size |
| 🆕 New issues introduced | N1–N5 below — **N1 and N2 break the demo walk-through, so fix them first** |

P2-3 note: the LD2 Continue button was already dimmed (opacity 0.55) in round 1. The round-1 item was based on the button's `disabled` attribute rather than how it looks, so it's closed with no change needed.

---

## 2. New issues introduced in this round (fix first)

| # | Where | Problem | Fix |
|---|---|---|---|
| N1 | Footer **Admin** link | Gone from **every** page, including LP0 and the SSLP. It's wrapped in `<sc-if value="{{ showAdminLink }}">` but `showAdminLink` is never defined in the logic, so it's always falsy. Also, its new target `admin/admin.html` returns **404** on Vercel | Define `showAdminLink` (true on public and app pages, false on onboarding / 1D / M1, as round 1 asked) and point the link at `/admin` |
| N2 | Admin → **Back to site** | Now goes to `../landing.html`, which returns **404** on Vercel (the old `../index.html` worked) | Point it at `/` |
| N3 | **Safety Care screen and Tier 3 message can't be reached** | Markup is there, but `isSafetyCare` and `showTier3` are never set anywhere, so neither ever renders. No route, prop or build control leads to them | Add a way to show them: a `startRoute: "safety-care"` option plus a build-control toggle for the Tier 3 message in the Moira drawer |
| N4 | Admin → Articles, row Stage dropdown | Options include **"Postpartum"** and **"Connection & Growth"**, which aren't stages. The Aspect dropdown next to it has only the current value | Stage options: Before Pregnancy, Pregnancy, Birth, First Years only. Aspect: the 11 aspects |
| N5 | Settings → Your consents | Shows "Marketing communications — **Active**" while the Marketing email/SMS toggles on the same page are off | Make the demo state agree (e.g. "Not given" / "Off"), or drop the marketing row and point to the toggles |

---

## 3. Still open from round 1

| # | Where | Now (30 Oct) | Still needed |
|---|---|---|---|
| P0-8 | AI watermarks ("MINIMAX \| Hailuo AI") | The image files are unchanged (same bytes). The Birth banner and article header now crop the mark out, but it is still visible on **all four Birth featured cards** and the **article interior image** | Replace the image itself (or re-crop and re-export it) so no view shows the mark. Check the other stage images |
| P1-1 | Safety screens (content) | Placeholders exist but are unreachable (N3). Once visible: **(a) Tier 3 copy is wrong for Tier 3.** It says *"something worth discussing with your midwife or GP at your next appointment"* and offers *"Yes, help me prepare"*. Tier 3 is the **urgent** tier (e.g. heavy bleeding, reduced movement): the message should point to triage / NHS 111 / 999 **now**, and the AI conversation ends, so no follow-up buttons. **(b) Safety Care resources:** "Crisis Text Line — Text SHOUT to 85258" mixes two services. Shout is UK (text SHOUT to 85258); Crisis Text Line is US (text HOME to 741741). Add NHS 111. **(c) Buttons:** the signed plan wording is *"I'm okay — take me back to the site"* and *"I need a moment — I'll come back later"*, both going to the SSLP; currently "Return to {stage}" and "Go home". **(d)** Drop the 🚨 and 💚 emoji and the off-palette greens (`#4CAF50`, `#2D5A3D`); use the Moira and Birth tokens | Fix (a)–(d). Placeholder tone is fine, but these four would be read as the intended behaviour |
| P1-2 | Birth SSHP | Header is compact; at 1440×900 the four featured cards now show image, category and the start of the title. Blurbs and the top of "Your birth guide" are still below the fold (worse at 1366×768). On mobile, the heading now sits tight against the Moira box | Tighten further (e.g. shorter card images on Birth, or a 2-row header) so blurbs and a hint of the guide are visible at 1440×900. Restore the small gap under the heading on mobile |
| P1-3 | SSLP Smart Tools section | Got **taller**: 469 px → 492 px at 1440 wide (grid changed to auto-fit and padding went 48 → 64). Phone shrank 210 → 170 px. "Watch the tour" label unchanged | Target roughly 240–280 px tall at 1440×900: restore the 48 px padding and a two-column layout with text left, phone right. Label the button "Watch the Smart Tools video" |
| P1-5 | Off-palette / stage colours | Old cocoa and slate are gone, but the **Pregnancy** blog story now uses Smart Tools rust `#A0522D` (it should be Pregnancy amber `#E0A030`). Contacts "Work / School" use First Years teal for non-stage categories. One `#7A8B9A` is left in admin | Stage-tagged items use their own stage token. Non-stage categories use neutrals, not stage or feature colours |
| P1-6 | Finance colour | Accents switched to rust. Teal tints remain: step background `#E5F0F1`, borders `rgba(31,111,118,…)`, note box `#F4FAFB` | Swap the tints to the rust family (e.g. `#F6ECE6` bg, `rgba(160,82,45,.2)` borders) |
| P2-1 | SSLP fold | At 1440×900 the "Latest for you" heading is now visible, but the card titles aren't. At 1366×768 the trust-bar descriptions hide (good), but the card titles are still below the fold | Slightly smaller hero video and heading, so card titles show at 1440×900 |
| P2-2 | Per-page footers | Admin link hidden on onboarding (but also everywhere — N1). Onboarding/1D/M1 still use the global footer (e.g. LD1 shows Medical Disclaimer + Cookie preferences, not the client's Privacy Notice · Terms of Use · Cookies Policy) | Apply the per-page footers from `Landing_PRD.md` §3.5 |
| P2-4 | Click-through dead ends | Escape now closes admin modals ✅. **Reviewer "Not available" button** was relabelled "Go to Articles" but still calls `go("dashboard")`, and Reviewers can't open either; send them to For review. **Landing:** no code change found for guide cards / blog stories all opening the same article, "Open in your journal →" not selecting the tool, or guide-topic search hits landing at the top of the page | Fix as described in round 1 |
| P2-5 | Admin article dropdowns | Dropdowns were added to the **table row** (with N4's problems); the **expanded row** still shows Category as plain text | Category dropdown filtered by Stage, in the expanded row (where BE's card is) or in the table row, consistently |

Minor, optional: the Privacy page still says *"Moira only sees an entry in the moment you ask her about it"*, while Moira Facts shows observations taken "from your journal". Consider *"Moira only uses what you have agreed to"*.

---

## 4. Closed — don't regress

P0-1 P-B8 note removed · P0-2 P-B7 banner behind `showAnnotations` (default off) · P0-3 open-question note removed · P0-4 Stories journal-privacy line · P0-5 "affiliate offers" removed from Allow (both places) · P0-6 all "on this device" / "UK servers, only you" copy now says vault + Moira · P0-7 FAQ account and ads answers · P0-9 cookie banner copy and button labels · P0-10 Market affiliate disclosure · P1-4 full Moira disclaimer on SSLP, SSHP and article boxes · A1-1 admin palette tokens · Settings consents and emergency-contact cards render correctly at all three sizes, with no horizontal scroll.

Plus everything in round 1's "Things that are right" list, which is still true.

---

## 5. Hold — decisions pending (do NOT change yet)

Unchanged from round 1.

| # | Topic | Why it's on hold |
|---|---|---|
| H1 | Gate "site password" copy | Signed plan promises passwordless magic links; gate copy may change to an invite-link flow |
| H2 | Moira consent prompts (journal reading, interest profiling, health observations) | Proposal: ask the first time each is needed. Wording needs BTO |
| H3 | Moira Facts "Allow" option | BTO to approve whether it stays |
| H4 | Trust-bar labels (Evidence-Based vs Evidence Informed) | Loucas to pick one |
| H5 | "Terms of Service" vs "Terms of Use" | Loucas/BTO to pick one |
| H6 | "AI Created" evidence tier | Confirming whether Loucas wants it removed entirely |
| H7 | LD4 questionnaire logic/copy | Raising with Loucas |
| H8 | LD2 copy ("…process your application…", "subscription") | Raising with Loucas |
| H9 | Ad space | Ad network vs own affiliate slot undecided |
| H10 | Team passwords | Agreeing "reset only" with Loucas |
| H11 | Dialogue / Blog / Forum and admin Stories | Phase 2 in the contract; no more effort |
