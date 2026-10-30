# PRD — BestBaby Landing & Platform

**Product Requirements Document** for `index.html`.

| | |
| --- | --- |
| Product | BestBaby.org: public landing page, private-beta access, onboarding and the signed-in platform |
| Artefact | `index.html`, a self-unpacking offline bundle (~7.7 MB) |
| Status | Clickable design prototype. No backend; a little state in `localStorage` |
| Preview frame | 1440 × 1024 |
| Companion doc | [`admin/Admin_PRD.md`](admin/Admin_PRD.md), the staff admin console |
| Last reviewed | 22 Oct 2026, against the client documents dated 26.10.18–26.10.19 |

---

## 0. Source documents

This PRD is aligned with the client requirement documents below. **Where the prototype and a source document disagree, the source document wins**, and the difference is listed in §12.

| Ref | Document | Covers |
| --- | --- | --- |
| **FE** | BESTBABY Front End REVISED 26.10.19 | Colour rules, header and navigation, SSLP, SSHP (all four stages), article page |
| **OB** | On-Boarding 26.10.19 | LP0, sign-in routing diagram, onboarding sequence, SSLP/SSHP section and video map, article layout |
| **1D** | BestBaby_Page1D 26.10.18 | Join the Beta application |
| **M1** | BestBaby_Page M1_26.10.18 | Magic-link page |
| **LD1** | BestBaby_LD1_Welcome 26.10.19 | Onboarding step 1: Welcome |
| **LD2** | BestBaby_LD2 Reg Consent 26.10.18 | Onboarding step 2: Basic Registration & Consent |
| **LD3A** | BestBaby_LD3A TOS 26.10.19 (Working Draft v5) | Terms of Service |
| **LD3B** | BestBaby_LD3B PRIVACY 26.10.19 (Working Draft v5) | Privacy Notice |
| **LD4** | BestBaby_LD4 Journey 26.10.19 (two copies; identical apart from the closing line) | Onboarding step 3: Your Personal Journey |
| **BE** | BestBaby Back End 26.10.09 | Admin console — see [`admin/Admin_PRD.md`](admin/Admin_PRD.md) |

> "LD" legal documents may change with legal review (OB). The footer on every page is still **to be discussed** (FE, OB).

---

## 1. Overview

### 1.1 Purpose

BestBaby.org is *"an AI-assisted resource for pregnancy, childbirth, and parenting. Practical information, emotional support, and evidence-based guidance — all in one place."* (OB, LP0)

It is *"a science-backed, emotionally honest companion for every stage of the parenting journey — from the first conversation about whether to have a family, through pregnancy, birth, and the early years."* (LD1)

It combines four things:

1. **An editorial library** organised by stage, with guides and articles reviewed by an editorial and clinical panel.
2. **Smart Tools**: private, interactive planners, calculators and checklists, designed to work with Moira and the Journal.
3. **A personal organiser**: Journal, Calendar & Notepad, Contacts, Personal information.
4. **Moira**, an AI companion — in text or voice — that answers questions and records observations the user can confirm, edit or delete.

### 1.2 Audience

- People thinking about a family, by any route: natural conception, fertility assessment, IVF/assisted conception, egg freezing, donor conception, surrogacy, adoption, fostering.
- Pregnant people and their partners.
- Parents of children aged 0–5.
- Nine "who is on this journey with you" options are recognised (LD4, §4.6).
- The product is UK-first (UK GDPR, company registered in Scotland, governed by Scots law). Postal code is used to direct users to local guidance, e.g. NHS pathways for the UK "or equivalent guidance for users elsewhere" (LD3B). The finance tool also supports the US.
- Users must be **18 or older** (LD2, LD3A).

### 1.3 Value proposition

Families are smaller and more scattered, and the knowledge once passed between generations is harder to reach. *"BestBaby … brings together the warmth and wisdom families used to pass down, joined with everything science has learned since — and puts it in your pocket … Not to replace your instincts. To support them."* (LD1)

| Brand value | Meaning in the product |
| --- | --- |
| Evidence-based | Content carries an evidence tier and is reviewed before publishing |
| Warm and calm | Supportive tone; Moira speaks gently and without judgement |
| Inclusive | Every family structure and route to parenthood |
| Honest | Moira is labelled as AI and is "not a doctor, midwife, or medical professional" |
| Practical | Tools produce plans, lists and numbers, not just reading |

**Business model:** BestBaby is currently **free** (LD3A). Some content and emails may include clearly identified affiliate links to third-party products, from which BestBaby may earn a small commission — *"This is how we are able to keep BestBaby free."* (LD2, LD3B). The article page includes an **ad space** (FE, OB).

### 1.4 Goals

- **G1.** Let invited beta users get from the landing page to their own stage content quickly. Basic Registration and the onboarding video happen **once** only.
- **G2.** Collect only the data needed, with explicit, time-stamped consent for special category data (UK GDPR Art. 9(2)(a)) **before** any journey data is collected.
- **G3.** Give each stage a clear home: featured articles, a structured guide, Connection & Growth, Smart Tools and Moira.
- **G4.** Keep the user in control of what Moira knows about them. Moira never stores or acts on an observation without asking first.
- **G5.** Gather beta applications and feedback to shape the product.
- **G6.** Respect the fold: page layouts must minimise how much important content falls below the fold on both computer and phone screens (FE).

### 1.5 Scope

| In scope | Out of scope (for the prototype) |
| --- | --- |
| Public landing page and private-beta gate | Real authentication and email delivery |
| Beta application, 3-step onboarding, magic link, onboarding video | Server-side storage of onboarding answers |
| Stage landing and stage home pages, articles, search | Real article bodies (published from Admin) |
| Journal, Calendar & Notepad, Contacts, Moira space and facts | Calendar sync (held until a data processing agreement exists) |
| Smart Tools (see §6) | Live Moira AI, voice, dictation |
| Dialogue/Blog, Essentials Market, Settings | Messaging, events, purchases |
| Cookies, legal overlays, marketing pages | Real cookie gating and analytics |
| — | C&G stage pages and topic pages with video (**to be built**, FE) |

---

## 2. Colour and visual hierarchy

### 2.1 Stage colours

*"All four stages must be very different and distinctive visually."* (FE)

| Stage | ID | Required hue (FE) | Colour | Dark | Tint | Header bar | Window |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Before Pregnancy | `before-pregnancy` | Soft mauve / dusty rose | `#B5838D` | `#8A5562` | `#F7EDEF` | `#9A6370` (darkened for contrast) | Before |
| Pregnancy | `pregnancy` | Warm amber | `#E0A030` | `#86560A` | `#FDF3E0` | `#E0A030` with dark ink | 40 weeks |
| Birth | `birth` | Terracotta red | `#C8382A` | `#962A1C` | `#FBEAE6` | `#C8382A` | The day |
| First Years | `first-years` | Teal / slate blue | `#377A91` | `#285A6C` | `#E5F1F5` | `#377A91` | 0–5 yrs |

### 2.2 Feature colours

Features keep their own colour regardless of stage (FE).

| Feature | Requirement (FE) | Colour |
| --- | --- | --- |
| Moira | Deep forest green (no change) | `#1E3A2B` |
| Connection & Growth | A **more dynamic** colour — upgraded from muted lavender to reflect the infant-stimulation focus | `#7B2FF2` (CTA `#FFB547`) |
| Smart Tools | Terracotta / rust brown (no change) | `#A0522D` |

### 2.3 Colour rules

| ID | Rule (FE, OB) |
| --- | --- |
| R-COL-1 | The **header bar** (logo + main menu) is always the colour of the **user's registered stage**, on every page, including when they are viewing another stage. |
| R-COL-2 | The **main content area** reflects the stage **currently being viewed**. |
| R-COL-3 | Do not colour every surface with the stage colour. Use **light backgrounds with stage-coloured accents** to keep text readable. |
| R-COL-4 | Moira, Smart Tools and Connection & Growth keep their own feature colours on every page. |
| R-COL-5 | In **The Journey** dropdown the stage colours must be bold enough to tell apart: each stage title sits on a **coloured bar with black or white text**. |

The user therefore always has two signals: *where I am in my journey* (header) and *what content I am exploring* (page body). The SSLP explains these rules to the user ("How BestBaby is laid out").

---

## 3. Routes and information architecture

### 3.1 Route map

| Group | Route | Page | Doc |
| --- | --- | --- | --- |
| **Public** | `lp0` | Landing page with the private-beta gate | OB |
| | `beta` | Join the Beta application (Page 1D) | 1D |
| | `nr1` | Onboarding: LD1 Welcome → LD2 Registration & Consent → LD4 Journey | LD1, LD2, LD4 |
| | `m1` | Magic key (unrecognised device) | M1 |
| | `nr7` | Onboarding video (one-time) | OB, LD4 |
| **Signed in** | `sslp` | Stage-Specific Landing Page — **the index page of the site** | FE, OB |
| | `stage` | Stage-Specific Home Page (SSHP) | FE, OB |
| | `article` | Article page | FE, OB |
| | `journal` | Your Journal: Today, To-do, Tools, Finance, Personal information | |
| | `calendar` | Calendar & Notepad | |
| | `contacts` | Your Contacts | |
| | `moira-space` | Your Moira | |
| | `moira-facts` | Moira Facts — confirm, edit, delete | LD3B |
| | `dialogue` | Dialogue, Blog & Forum | |
| | `market` | Essentials Market | |
| | `search` | Search | |
| | `settings` | Settings | |
| | `tools` / `tool` | Tool index and tool detail | |
| | `soon` | Coming soon placeholder | |
| **Marketing** | `about`, `faq`, `contact`, `press`, `careers` | Marketing pages | |
| **Legal** | Overlays: Terms of Service (LD3A), Privacy Notice (LD3B), Medical Disclaimer. Route: `cookies` | Legal | |

**Route guard.** A signed-out user who opens any route other than the public and legal ones is sent to `lp0`.

### 3.2 Trust bar

A simple bar sits **under the header menu** on every page, with an icon next to each marker (FE, OB).

| Page | Markers | Descriptions |
| --- | --- | --- |
| LP0 | Your Privacy First · GDPR Compliant · Evidence-Based · Expert Reviewed | No |
| **SSLP only** | Same markers **with descriptions** (below) | Yes |
| SSHP, article, other app pages | Privacy First · GDPR Compliant · Evidence Informed · Expert Reviewed | No |

SSLP descriptions (FE):

| Marker | Description |
| --- | --- |
| GDPR compliant | Your data is encrypted and never shared for marketing. |
| Evidence-based | Information grounded in clinical research and expert review. |
| Your privacy first | You control what you share and how it's used. |
| Expert Reviewed | Written with clinical guidance, so you can trust what you read. |

### 3.3 Public header (landing)

- Dark green (`#1E3A2B`) bar with the "BestBaby.Org" wordmark (Playfair).
- Four stage pills. Each opens a teaser: name, window, phase line, blurb and "Sign in to open →", which scrolls to the gate. Teasers are generic; **LP0 shows no personalised content**, because there is no consent yet to process journey-stage data (OB).
- "Private Beta" link to the gate.
- Stage pills are hidden on onboarding and the onboarding video.

### 3.4 App header (signed in)

**Main bar** — the user's stage colour (R-COL-1). Items are **equally spaced across the bar, left to right** (FE), and keep their visual icons:

| Item | Destination |
| --- | --- |
| **BestBaby.Org** | Always the SSLP |
| **The Journey** | Dropdown of the four stages (coloured bars, R-COL-5). Notes that your own stage is changed in Settings. |
| Back | Previous page (history of up to 30 entries; dimmed when empty) |
| **Home** | The user's SSHP |
| **Your Journal** | Journal *(contents to be discussed, FE)* |
| **Your Moira** | Moira space *(to be discussed, FE)* |
| Search | Search |
| Settings | Settings |

**Second bar** (stage dark colour): Your Contacts · Calendar & Notepad · Dialogue Blog & Forum · Essentials Market · About.

Client direction on the second bar (FE):

- The **Essentials Market must not be hidden in a dropdown**.
- **Dialogue, Blog & Forum should be more prominent.**
- A second bar under the header is the preferred way to achieve this. Grouping Contacts, Calendar and Notepad under one item (called "Organizer" or "Tools") is acceptable, but with a second bar they can sit there directly.
- Dialogue/Blog/Forum and the Market are still **to be discussed**.

**Other chrome:**

- Optional sticky section bar on the SSHP (Featured · The guide · Connection & Growth · Smart tools · Moira). The client is happy to drop it if the page becomes too busy (FE).
- **Voice Moira** floats in the **lower-right corner of every page** in the signed-in experience (FE). It does **not** appear during onboarding (OB).

### 3.5 Footer

- **Status: to be discussed, and must be cleaned up before beta** (FE, OB).
- LP0 footer must contain: Privacy Notice, Terms, Medical Disclaimer, company info (OB).
- Company line used across the client pages: *"BestBaby.org · BestBaby.Org Ltd · Registered in Scotland · SC899830"*.
- **Admin** link: opens the staff admin console (BE).
- Prototype today: Privacy Notice · Terms of Use · Cookies Policy · Medical Disclaimer · Cookie preferences · Admin, plus a medical disclaimer paragraph.

Per-page footer links specified by the client:

| Page | Footer links |
| --- | --- |
| 1D Join the Beta | Privacy Notice · Terms of Use · Medical Disclaimer |
| LD1 Welcome | Privacy Notice · Terms of Use · Cookies Policy |
| LD2 Registration | BestBaby.Org Ltd · BetaContact@BestBaby.org · www.BestBaby.org |
| M1 Magic key | Company line only |

### 3.6 Editor props

| Prop | Type, default | Effect |
| --- | --- | --- |
| `showAnnotations` | boolean, `true` | Intended to show design annotations. No annotation markup exists yet. |
| `userStage` | enum, `before-pregnancy` | The user's starting stage |
| `showSectionBar` | boolean, `false` | Sticky in-page section bar on stage pages |
| `cgPanel` | `research` · `video` · `articles` | Right-hand panel of Connection & Growth |
| `showBuildControls` | boolean, `false` | Gate routing matrix and device toggle; magic-link state previews; video debug; onboarding database-field note |
| `deviceRecognized` | boolean, `false` | Starts signed in on `sslp` and treats every device as recognised |
| `startRoute` | enum, `lp0` | Opening route: `lp0`, `sslp`, `nr1`, `beta`, `stage`, `article`, `settings`, `journal`, `calendar`, `moira-space`, `moira-facts`, `m1`, `nr7`, `cookies` |

---

## 4. Public experience and onboarding

### 4.1 Landing page (`lp0`)

What LP0 must do (OB):

- **Join the Beta** → Page 1D, an application with email capture.
- **Sign in** → SSLP, Magic Key (M1) or Onboarding, depending on the routing rules in §4.2.
- **No personalised content.**

| # | Section | Requirements |
| --- | --- | --- |
| 1 | Public header | See §3.3 |
| 2 | Trust bar | Your Privacy First · GDPR Compliant · Evidence-Based · Expert Reviewed, with icons |
| 3 | Hero | "Private Beta" eyebrow; H1 **"Guidance for every stage"**; value line (§1.1); CTAs **Join the Beta** and **Sign in**; **main video** "BestBaby Video" |
| 4 | Gate (`#gate`) | "You've reached BestBaby.org." Email, Site password, Continue. Links to Terms of Use and Privacy Notice. "Just stumbled in? Join the Beta". |
| 5 | Manifesto | **"Help us build what you need."** Ends with an invitation to join the Private Beta. |
| 6 | Footer | See §3.5 |
| 7 | Cookie banner | See §7.2 |

### 4.2 Sign-in routing

The platform checks whether the **email** is recognised and whether the **device** is recognised (OB).

| Device | Email | Password | Destination |
| --- | --- | --- | --- |
| Recognised | Recognised | Recognised | **SSLP** directly |
| Unrecognised | Recognised | Recognised | **Magic Key (M1)** → SSLP |
| — | Unrecognised | Recognised | **Onboarding** (LD1 → LD2 → LD4 → onboarding video → SSLP) |
| — | — | Not recognised | Stay on the gate with an error; offer Join the Beta |
| — | — | (Join the Beta clicked) | **Page 1D** application |

| ID | Requirement |
| --- | --- |
| FR-GATE-1 | Trim and lower-case the email; validate the format. Error: *"Enter a valid email address"* and *"Your email is collected solely to set up your account."* (LD3B: the email is collected before registration only to set up the account.) |
| FR-GATE-2 | Compare the password case-insensitively. Error: *"That password is not recognised"* … *"New here? Use Join the Beta below."* The email is checked first. |
| FR-GATE-3 | **All users must complete Basic Registration before they can access the site** (FE). |
| FR-GATE-4 | After onboarding, **every later sign-in goes to the SSLP, not the stage home page** (FE). |

### 4.3 Join the Beta (`beta`, Page 1D)

**Heading:** *"Join the BestBaby Beta."* Intro: *"We read every application personally. If we think you're a good fit, we'll be in touch within a few days."*

| Field | Rule |
| --- | --- |
| First name \*, Last name \* | Required |
| Email address \* | Required, valid format |
| Country \* | Required; hint "e.g. United Kingdom, France, Germany" |
| What should we call you | Optional |
| Are you a healthcare or childcare professional? | Optional, Yes / No |
| How did you hear about BestBaby? | Optional: A friend or family member · Social media · Search engine · A healthcare professional · Other |
| Why would you like to join the BestBaby Beta? \* | Required. Hint: "Tell us what you're hoping to find, what's missing, or what you'd most want BestBaby to help you with." Placeholder "Tell us in your own words…" |
| Cookies | Accept / Reject non-essential, More options |

| ID | Requirement |
| --- | --- |
| FR-1D-1 | **This page must not ask for journey-stage information.** That is health-related, GDPR-regulated data, and there is no consent yet (FE). |
| FR-1D-2 | Privacy line under the "About you" fields: *"Collected solely to process your application and, if approved, to set up your account."* |
| FR-1D-3 | Button: **"Submit My Application →"**. Confirmation: *"We'll be in touch soon. Thank you for your interest in BestBaby."* |
| FR-1D-4 | Each application is **emailed to App@BestBaby.org** and stored (OB, FE). It appears in Admin → Notifications for approval. |
| FR-1D-5 | Missing required fields are listed as *"Still needed: …"*. |
| FR-1D-6 | Footer: company line; Privacy Notice · Terms of Use · Medical Disclaimer. |

### 4.4 Onboarding sequence

| Step | Screen | Doc |
| --- | --- | --- |
| 1 | **Welcome**, with audio in Moira's voice | LD1 |
| 2 | **Basic Registration & Consent**, linking the Terms of Service and Privacy Notice | LD2, LD3A, LD3B |
| 3 | **Your Personal Journey** questionnaire | LD4 |
| 4 | **Onboarding video** — one-time, plays only as part of onboarding | OB |
| → | SSLP | |

Rules:

- **There is no Moira on any onboarding page** (FE). The only Moira presence is the recorded welcome audio.
- Registration and the video are seen **once only** (FE).
- Header: "Step N of 3 · {Welcome | Basic Registration & Consent | Your Personal Journey}", with a progress bar.
- LD1 tells users what follows: two short screens, *"both just a click, no downloads, no signatures. About three minutes in total"*, then a video — *"Then you're in."*

### 4.5 Step 1 — Welcome (LD1)

- Eyebrow "Private Beta"; H1 **"Welcome to the Inner Circle."**
- Intro: invited users are *"the people who will help us build it"*, not beta testers.
- "Listen to Moira" plays the welcome in Moira's recorded voice.
- Six sections: **What BestBaby is · Something has changed · Every journey here is different · How we use what you tell us · Your privacy · What comes next.**
- "Your privacy" commitments: information is **never sold or shared**; if a user leaves the beta, their information is **removed from active use immediately**, keeping only a minimal opt-out record so they are not contacted again.
- *"Check off the two boxes below to continue."*

| ID | Requirement |
| --- | --- |
| FR-LD1-1 | Cookie choice: Accept non-essential · Reject non-essential · More options. Copy: "BestBaby uses cookies to make our website work. We would like to set additional cookies to understand how you use our site and to improve your experience. Please see our cookies policy for further information." |
| FR-LD1-2 | Checkbox: *"I've read and understood the information above and would like to continue."* — **recorded and time-stamped**. |
| FR-LD1-3 | Continue is enabled only when a cookie choice exists **and** the box is ticked. Error: *"Please choose a cookie option and tick the box to continue."* |
| FR-LD1-4 | Footer: company line; Privacy Notice · Terms of Use · Cookies Policy. |

### 4.6 Step 2 — Basic Registration & Consent (LD2)

**About you**

| Field | Rule |
| --- | --- |
| Email address \* | Pre-filled from the gate and **locked**. "Your email address was saved when you entered the site." |
| First name \*, Last name \* | Required (may be pre-filled from the beta application) |
| Preferred name \* | "What would you like Moira to call you?" — "The name Moira will use when talking with you. Can be a first name, nickname, anything." Always collected fresh. |
| Postal code \* | e.g. "EH1 1YZ". "Helps us tailor content and guidance to where you are." *(Pending confirmation by Lynn — BTO flag.)* |
| Age confirmation \* | "Yes, I confirm I am 18 or older." — "You must confirm your age to create a BestBaby account." |
| Healthcare or childcare professional? | Optional, Yes / No |
| How did you hear about BestBaby? | Optional: Invited · A friend or family member · Social media · Search engine · A healthcare professional · Other |

**Consent — Processing of Special Category Personal Data and Marketing**

Intro: the next steps ask about family and journey; this is health-related information protected under UK data protection law; BestBaby needs permission before collecting it; it will not be used for marketing unless separately agreed.

| Part | Item | Rule |
| --- | --- | --- |
| 1 | **c1** "I agree to BestBaby's Terms of Use and have read the Privacy Notice." | **Required.** Must link to the Terms of Service (LD3A) and Privacy Notice (LD3B). |
| 1 | **c2** "I consent to BestBaby collecting and using my journey and family situation information to personalise my BestBaby experience, as described above." | **Required.** Explicit consent under **UK GDPR Art. 9(2)(a)**, equivalent to a standalone consent form. Withdraw any time via **BetaContact@BestBaby.org** or account settings. Without it, registration cannot proceed. |
| 2 | Marketing by **email** | Optional |
| 2 | Marketing by **text** | Optional. Ticking it reveals a mobile number field; the number is collected **only** if the user opts in. |

Part 2 copy must say that marketing is entirely optional and does not affect access; that offers may include products from carefully selected third-party partners from which BestBaby may earn a small commission; that personal data is **not shared with third parties for their own direct marketing**; and how to opt out (unsubscribe link; reply **STOP**; BetaContact@BestBaby.org).

| ID | Requirement |
| --- | --- |
| FR-LD2-1 | **Continue is active only once the Part 1 consents (and required fields) are complete.** Part 2 never blocks progress. |
| FR-LD2-2 | A failed click lists *"Still needed: …"*. |
| FR-LD2-3 | Written to the database on completion: `firstName`, `lastName`, `preferredName`, `postalCode`, `ageConfirmed: true`, `ageConfirmedAt`, `registrationCompleteAt` — plus each consent with its timestamp. |
| FR-LD2-4 | Footer: BestBaby.Org Ltd · BetaContact@BestBaby.org · www.BestBaby.org. |

### 4.7 Step 3 — Your Personal Journey (LD4)

Intro: *"Tell us a little about your family and where you are right now. This sets up your personal BestBaby home page and helps Moira understand how to support you from the very first conversation."*

**Who is on this journey with you?** Prefer not to say · Just me — solo parent · Me and my partner · Me and my wife / female partner · Me and my husband / male partner · Co-parenting (not together) · Adoptive or foster parent · Surrogacy journey · Other.

**Where are you right now?** \* — four stage cards; the user picks one. This sets the user's stage.

| Card | Subtitle | Stage |
| --- | --- | --- |
| Before pregnancy | Planning, trying to conceive | `before-pregnancy` |
| Pregnant | Expecting, any trimester | `pregnancy` |
| Preparing for birth | Third trimester or birth planning | `birth` |
| Already a parent | Newborn through early years | `first-years` |

**Follow-up by stage** (interest menus are multi-select):

| Stage | Follow-up |
| --- | --- |
| **Before pregnancy** | "What is your primary interest right now?" — Natural conception — just starting out · Fertility assessment — understanding my timeline · IVF or assisted conception · Egg freezing · Donor conception — sperm, egg, or embryo · Surrogacy · Adoption — domestic or international · Fostering · Still deciding — I want to explore my options · Prefer not to say |
| **Pregnant** | Due date: **Month \*** and **Year \***, hint *"Approximate is fine — estimates change with scans"*. The platform calculates the trimester and pre-selects its card, which the user can confirm or change. |
| **Preparing for birth** | Seven interests: Birth options — hospital, home, water birth · Pain relief and anaesthesia — understanding my choices · Complications — what to watch for and when to call · My baby's movements and wellbeing · My mental health and birth fears — including post-partum depression · Getting ready practically and financially · Your baby's senses before birth — what they can already hear and feel |
| **Already a parent** | "Do you already have children?" \* — No — this will be my first / Yes. If Yes, child cards with **Add a child** (unlimited): first name (optional), date of birth (optional text, hint "e.g. March 2023 or 2 years old"), sex (optional: Girl / Boy / Other / Prefer not to say). Then six interests: My baby's development and milestones · Sleep — for them and for me · Feeding — breast, bottle, weaning · My mental health and recovery — including post-partum depression · Financial planning for your child — childcare, healthcare, education and beyond · Stimulation and play — helping my baby's brain grow |

**Trimester cards** (canonical boundaries, LD4):

| Card | Weeks | Covers |
| --- | --- | --- |
| First | 1–12 | Baby's early development, nutrition and supplements, medications, mental health, budgeting, early brain development |
| Second | 13–27 | Baby's development and the anatomy scan, health and body, nutrition, mental health, maternity leave and finances, what the baby can already sense |
| Third | 28–40+ | Birth options, pain relief and anaesthesia, complications, baby's movements, mental health and birth fears, the cost of birth, talking to your baby before they arrive |

| ID | Requirement |
| --- | --- |
| FR-LD4-1 | Reject due dates outside the next ten months: *"Please choose a due date within the next ten months."* |
| FR-LD4-2 | "Prefer not to say" in an interest list excludes the other options. |
| FR-LD4-3 | **Create my BestBaby account**: the account is fully created, **all consents are recorded**, and the user goes to the onboarding video, which ends on the SSLP. |
| FR-LD4-4 | Every answer on this screen (who, stage, interests, due date, trimester, children) is stored as consented journey data. A partner's first name, if given, is used only by Moira to personalise conversations (LD3B). |

### 4.8 Magic Key (`m1`, Page M1)

Copy (M1):

- Eyebrow "Private Beta", envelope icon.
- **"We don't recognise this device."**
- *"That's okay — it just means you're on a new phone, computer, or browser."*
- *"We've sent a one-time access link to your email address. Open it on this device to continue straight through to BestBaby — no password needed."*
- **"Can't find the email?"** *"Check your spam or junk folder. The link expires after 15 minutes — if it's gone, you can request a new one below."*
- **↺ Send a new link** · **← Back to sign in**.
- Footer: company line.

| ID | Requirement |
| --- | --- |
| FR-M1-1 | The link is single-use and expires after **15 minutes**. |
| FR-M1-2 | Sending a new link invalidates the previous one: *"A new link is on its way. Your previous link no longer works."* |
| FR-M1-3 | Expired or used links show *"This link has expired"* / *"This link has already been used"*, each with Send a new link. |
| FR-M1-4 | Opening a valid link on the device marks it as recognised and lands on the **SSLP**. |

### 4.9 Onboarding video (`nr7`)

- One-time video *"introducing BestBaby and how it came to be"* (LD1). Prototype title: *"How BestBaby started and how it works"*, 2 minutes.
- Plays **only** as part of onboarding (OB). On first view it autoplays; **Continue →** appears after 20 s or at the end. The view is time-stamped on the account.
- At its end the user goes to their **SSLP** (LD4).

### 4.10 Sign-out

From Settings. Returns to the landing page and clears the Moira chat, gate fields and session. The device stays recognised.

---

## 5. Signed-in experience

### 5.1 SSLP — Stage-Specific Landing Page (`sslp`)

The **index page of the site**. It explains how the UI is designed and works (FE). Header and trust bar as in §3.2 and §3.4 (trust bar **with descriptions**).

| # | Section | Requirements |
| --- | --- | --- |
| 1 | **Header section** | Text *"You don't have to navigate this alone."* / *"Thoughtful, confidential guidance without pressure or judgment."*, the **"How BestBaby is laid out"** legend (§2.3), and the **index video** (3 min). Client approves the current text and legend. |
| 2 | **Stage-specific section** | Layout: **Featured article blurb · SSHP video + Moira text invite · Featured article blurb** — the two latest featured articles from the user's stage sit **either side** of the stage video and the Moira text box. Plus "Go to your {stage} home page →". |
| 3 | **Explore the journey cue** | Arrows **just above the fold** pointing down to the stages, so users know there is more below. |
| 4 | **Explore the journey** | Four stage boxes with short text. Each opens that stage's SSHP. The header stays the user's own stage colour. |
| 5 | **Connection & Growth** | Under the stages, in its own distinctive colour. Text plus the **C&G index video**, which explains infant stimulation and how Connection & Growth runs through all four stages. |
| 6 | **Smart Tools** | Keep the phone mock-up showing some of the tools. **Make the section smaller.** Text below. **ST index video.** |
| 7 | **Moira** | Exact text below. **Moira index video.** |
| 8 | **Where science meets real life** | Exact text below. |
| 9 | Footer | To be discussed |

**Smart Tools text** (FE):

> **Your Smart Tools**
> A personal Calendar and Notepad, a Financial Planner, a Kick Counter, and more — each one designed to work with Moira and your Journal, not alongside them as an afterthought. Open the phone to see how they fit together.

**Moira text** (FE, OB):

> **A note about Moira**
> A knowledgeable, warm and confidential companion — in your words, or in her voice.
> Moira is here to help you understand what you're reading, think through your options, and find the right next step. She comes in two forms — Moira text, if you'd rather type, and Moira voice, if you'd rather talk. Either way, your conversation stays private.
> *(followed by the standard Moira disclaimer, §7.1)*

**Where science meets real life** (FE, OB):

> A grounded, compassionate guide for pregnancy, birth, and the early years.
> BestBaby was built for the moments when you need more than a search result. A place where you can understand what research actually says, draw on the wisdom that parents and grandparents have carried forward, and feel supported rather than overwhelmed.
> Moira is here as a steady, knowledgeable companion — not a clinician, but the kind of informed friend who helps you think things through at your own pace. The tools bring order to the practical questions. The content gives you something solid to stand on.
> Whatever stage you are at, you do not have to figure this out alone.

### 5.2 SSHP — Stage-Specific Home Page (`stage`)

Header menu as §3.4, in the **user's** stage colour, with the simple trust bar (no descriptions). The rest of the page uses the colours of the **stage being viewed**, except the feature colours (FE).

| # | Section | Requirements |
| --- | --- | --- |
| 1 | **Header section** | Stage pill, title, intro, **Moira text** box, banner image, **Stage explainer "{Stage} in Three Minutes"** (3-minute stage video — not "Two Minutes"). |
| — | **Fold** | Either the featured articles are visible under the header **above the fold**, or at least their **titles show above the fold as a tease**. For Birth, the header, featured articles **and a hint of the guide** sit above the fold. The page must not be "poorly cut" by the fold. |
| 2 | **Featured articles** (`#featured`) | **Four** latest published featured articles, **one from each of the stage's four categories** (table below). **The full blurb must always show.** Add the article's header image where possible, but never at the expense of the blurb. Plus "All articles in this stage →" and in-stage search. |
| 3 | **Guide** (`#guide`) | Keep the current layout. Clicking a topic opens an **article page for now**; later this may become a topic page with a video. Possible guide videos are listed below. |
| 4 | **Connection & Growth** (`#growth`) | Leads to the stage's infant-stimulation page (**to be built**). Keep "What the research points to"; it may be replaced by a video or two C&G articles (`cgPanel`). Per-stage C&G video. |
| 5 | **Smart Tools** (`#tools`) | The stage's tools, set up to interact with the Journal and Moira (**to be built**). |
| 6 | **Moira** (`#moira`) | Encourages use of Moira. Keep **"People often start with"** prompt chips. Use the standard Moira disclaimer (§7.1). |
| 7 | Footer | To be discussed |

**Featured categories per stage** (FE)

| Stage | Category 1 | Category 2 | Category 3 | Category 4 |
| --- | --- | --- | --- | --- |
| Before Pregnancy | Readiness & Reality Check | Pathways to Parenting | Planning Ahead | Building Your Foundation |
| Pregnancy | 1st Trimester | 2nd Trimester | 3rd Trimester | Feathering the Nest |
| Birth | Your Birth Choices | Understanding Birth | Pain and Support Coping | Complications |
| First Years | 0 – 3 months | 3 – 12 months | 1 – 3 years | 3 – 5 years |

**Guide titles and planned videos** (FE, OB)

| Stage | Guide title | Possible guide videos | Header video |
| --- | --- | --- | --- |
| Before Pregnancy | Your Preparation Guide | Reality Check · Pathways | SSHP Before Pregnancy (3 min) |
| Pregnancy | Your Pregnancy Journey | 1st · 2nd · 3rd Trimester | SSHP Pregnancy (3 min) |
| Birth | Your Birth Guide | Understanding Birth · Pain and Coping · Recovery | SSHP Birth (3 min) |
| First Years | Your First Years Guide | Newborn · Toddler · Growing Up | SSHP First Years (3 min) |

Each stage also has a C&G video (SSHP CG {Stage}).

**Stage content model.** Each stage has: name, colours, explainer video, title and intro, banner image, four featured articles (one per category), a guide (title, intro, sections of numbered cards with four bullets each), Connection & Growth copy, a tool list and three Moira prompts.

| Stage | Guide structure (prototype) | Guide cards | Tools |
| --- | --- | --- | --- |
| Before Pregnancy | Readiness (4), Pathways (7) | 11 | 8 |
| Pregnancy | First / Second / Third trimester (6 each) | 18 | 4 |
| Birth | 4 sections × 4 | 16 | 4 |
| First Years | 4 age bands × (Practical, Looking after you) | 8 | 10 |

### 5.3 Article page (`article`)

Header menu as §3.4 in the **user's** stage colour, with the simple trust bar (FE).

| Region | Requirements (FE, OB) |
| --- | --- |
| **Article header bar** | Background = the **article's** stage colour. Three lines: the article's **Stage**, its **Topic**, its **Short title**. |
| **Header image** | The article's header image. It must work on desktop, phone and in blurb cards **without needing to be re-cropped**. |
| **Left ⅔** | Long title · Category · *Italic blurb* · Main article with interior pictures |
| **Right ⅓** | Header in the article's stage colour showing **Category** and **Stage** · **3 featured matching articles** · **Moira** · **Ad space** · **3 more featured matching articles** |
| Footer | To be discussed |

- "About This Article": "Reviewed by BestBaby editorial and clinical review panel", topic, stage.
- Body, images, Moira sidebar width and ad size are set in the Admin article editor.
- Prototype inventory: 4 categories × (1 lead + 3 latest) = 16 titles per stage, 64 in total.

### 5.4 Journal (`journal`)

*Contents to be discussed with the client (FE).*

| Tab | Requirements |
| --- | --- |
| **Today** | Dated entry (handwritten-style font); Save entry; Dictate instead; "Moira's check-in" for the stage; recent entries that reopen in the editor |
| **To-do** | Toggleable items with tags; add with text and tag (Care, Health, Work, Family, Money, Home); Enter saves, Esc cancels |
| **Tools** | Every tool grouped by stage, de-duplicated; the active tool on the right; "Done · back to Moira". Note: *"Anything a tool saves lands in Personal information for you to review first."* |
| **Finance** | Budget & finances planner (§6.4) |
| **Personal information** | Fact cards with status and a "Choose what happens" menu (§5.8); "Add a detail" (label from 8 types, value, "Confirm now"); link to "What Moira can see" |

### 5.5 Calendar & Notepad (`calendar`)

- Banner: Google and Apple calendar sync is **held** until a data processing agreement is in place (also listed as a beta compliance hold in Admin).
- **Calendar:** Monday-first month grid; today tinted; appointment dots in the stage colour; month navigation; "This month" list; Add an appointment; "Questions for next visit" checklist and notes.
- **Notepad:** note field (Save, or Ctrl/Cmd + Enter; disabled when empty); time-stamped history with delete and count; Ask Moira.

### 5.6 Contacts (`contacts`)

- Search across name, category, phone and email.
- Filters: All · Essential · Care team (OB-GYN, Midwife/doula, Hospital, Pharmacy) · Family · Work & school.
- Contact card: name, category icon and colour, phone (tap to call), email, Essential badge. Inline edit of phone and email, toggle Essential, Remove.
- **Add a contact:** name, type (8 categories), phone, email, Mark as essential. Rules: name required and unique; at least a phone **or** an email (*"Add a name and at least a phone number or an email."*). New contacts appear first.
- Aside: next appointments; Private vault ("Unlock with PIN" — arrives with the Private Vault release).

### 5.7 Your Moira (`moira-space`)

*To be discussed with the client (FE).*

- Intro and disclaimer.
- Observation cards (e.g. pregnancy stage, symptoms, preferences, care team): source, text, status pill, relative time, "Review in Moira Facts →".
- "How this works"; **Opt out of observations**.

### 5.8 Moira Facts (`moira-facts`) — user control over AI-held data

*"Moira will never store or act on any observation without asking you first."* If Moira notices something relevant — a **health inference**, e.g. gestational diabetes or anxiety — she says what she noticed and asks whether to remember it (LD3B).

- Counters: N pending · N confirmed · N allowed.
- Every observation has these choices (LD3B §2):

| Choice | Effect |
| --- | --- |
| **Edit / Correct** | Edit or correct the observation; saved items show "Corrected by you" |
| **Confirm** | Moira may use it to personalise guidance. **BestBaby does not see it**, and it does not affect communications. |
| **Allow** (dropdown) | BestBaby **and** Moira may use it to personalise the experience **and communications**, only in agreed ways, never shared with third parties for their own marketing. Can be withdrawn (returns to Confirmed). |
| **Leave pending** | Nothing is stored in the Private Vault and nothing is used until the user decides |
| **Delete entirely** | Permanent. A deletion record keeps **only the category of data and the date** |

- Confirmed observations are held in the **Private Vault**: private by default, encrypted, not visible to BestBaby, never used commercially without permission.
- Observations are labelled as AI-generated.
- The user can change any choice at any time on this page.

### 5.9 Dialogue, Blog & Forum (`dialogue`)

*Placement in the navigation is to be discussed; it should be more prominent (FE).*

- Tabs: **Blog** (stories with stage, title, excerpt, author, city, date) · **Write a story** (title, story, review-consent checkbox, Submit, Save draft, drafts list) · **Messages** and **Events** ("not open yet").
- Before submitting a story, the user **signs off on the GDPR considerations** (BE). Submissions go to Admin → Stories for review and are published to the **Blog** or **Forums**.
- LD1 invites users to *"Use the blog. Read what others are writing."*

### 5.10 Essentials Market (`market`)

*Must not be hidden in a dropdown; still to be discussed (FE).*

- "Opens later this year" with email capture.
- Product cards: category, "Coming soon", price, **Notify me**. The catalogue and display order are managed in Admin → Affiliate catalogue.
- Affiliate recommendations are clearly identified as such (LD3A, LD3B).

### 5.11 Search (`search`)

| ID | Requirement |
| --- | --- |
| FR-SRCH-1 | Index: articles (16 per stage), guide topics (one per card), Smart Tools (26) — about 143 records. |
| FR-SRCH-2 | Every query word must appear in title, blurb, kicker or stage name. Rank +2 for each word found in the title. At most 40 results. |
| FR-SRCH-3 | Filters: stage (All + 4) and type tabs (All, Articles, Guide topics, Smart Tools) with counts. |
| FR-SRCH-4 | Empty query: popular searches — Folic acid, Sleep, Epidural, Budget, Solid food, Anatomy scan. |
| FR-SRCH-5 | No results: *"No results for …"* with Ask Moira and Clear search. |
| FR-SRCH-6 | Results open the article, the tool in the Journal, or the guide section. |

### 5.12 Settings (`settings`)

| Section | Requirements |
| --- | --- |
| Your stage | Four buttons; changes the header colour and home stage; saved to the account |
| Moira interests | Removable chips (seeded from the LD4 interests) |
| GDPR preferences | Toggles, off by default: Aggregate usage statistics · Help improve Moira (de-identified conversation review) |
| Consents | View and **withdraw** the special category consent (c2) and marketing consents (LD2, LD3B) |
| Cookies | Status (Not chosen yet / Essential only / Essential and non-essential) and Cookie preferences |
| Your data | **Export everything in my vault** (self-export, LD3B) · Request erasure |
| Marketing | Marketing email · Marketing SMS (reply STOP, or BetaContact@BestBaby.org) — reflects the LD2 choices |
| Account | Avatar, name, email, how sign-in works, **Sign out**; Private vault note |

### 5.13 Tools index and tool detail (`tools`, `tool`)

- Index: four stage groups listing every tool; link to Calendar; "Ask Moira which to use"; "Private by default".
- Detail: title and description, *"Everything you enter is encrypted in your Private Vault"*, tool disclaimer where needed (e.g. Kick counter, linking to the Medical Disclaimer), and **Open in your journal →** which must open that tool.

---

## 6. Smart Tools

Every tool is designed to **interact with the Journal and Moira**, not sit alongside them (FE). All tools end with **Ask Moira for insight**. Health tools say they are estimates, not diagnoses.

### 6.1 Before Pregnancy

| Tool | Inputs | Rules and outputs |
| --- | --- | --- |
| **Fertility window** | Cycle length, 21–35 days (default 28) | Ovulation day = cycle − 14. Window = days (ov − 4) to (ov + 1); default Days 10–15. "An estimate, not a diagnosis." |
| **Preconception checklist** | 19 items: Medical 6, Lifestyle 5, Financial & practical 4, Emotional & relational 4 | Tick items, show "why?", per-group counts, overall x/19 progress bar |
| **Doctor visit prep** | 4 topics × 4 suggested questions, plus your own | Build "Your list" (de-duplicated, removable, counted) |
| **Genetic risk quiz** | 5 steps: ethnic background, family history, previous pregnancies, related by blood, age at conception | At least one answer per step. Summary: "What to discuss with your doctor". No risk score. "None" / "Prefer not to say" must be exclusive. |
| **Lifestyle audit** | 11 questions: Nutrition, Movement, Sleep, Substances, Stress & support | Each answer = Strong / Worth a look / Worth raising. Verdict: 0 flags "well set up for conception"; ≤ 2 "Mostly solid…"; otherwise "A few areas stand out…" |
| **Timeline planner** | Target conception date (≥ 28 days ahead) | 10 steps with lead times 90, 90, 75, 60, 60, 45, 30, 30, 14, 0 days; date = target − lead; label "N months before" (lead divisible by 30), else "N weeks before"; 0 = "Target month" |
| **Nutrition planner** | Weight (kg/lb), height (cm/in), 6 fertility factors (iron, vitamin D, omega-3, period regularity, PCOS, thyroid), 6 habits | Habit map: Strong / Room to build / Focus here (bar 100 / 60 / 25 %); plan: Emphasise, Limit, This week; **Download plan as PDF** (print view) |
| **Budget planner** | — | Opens Journal → Finance |

### 6.2 Pregnancy

| Tool | Inputs | Rules and outputs |
| --- | --- | --- |
| **Due date calculator** | First day of last period (LMP) | Due date = LMP + 280 days. Weeks along = whole weeks since LMP + days. Trimester uses the **canonical LD4 boundaries**: weeks 1–12 First, 13–27 Second, 28+ Third. |
| **Week-by-week coach** | Week 4–42 | Trimester label and three cards: Fetal development, Maternal changes, Sensory development. Defaults to the user's due date. |
| **Kick counter** | Start session, tap to count | Guidance: ten movements in two hours. Session timer, end and save. Not-a-medical-device disclaimer. |
| **Contraction timer** | Start / Stop | Live m:ss (announced to screen readers). Log each contraction's length and time, newest first. Shows spacing / frequency. Clear history. |

### 6.3 Birth

| Tool | Requirements |
| --- | --- |
| **Hospital bag checklist** | 14 starter items in three groups (For you, For baby, For your partner). Tick, remove, add custom items to a group, "x of y packed". Saved. |
| **Birth preferences** | 16 choices in four groups: environment, support team, pain management, interventions. "N preferences chosen". Save to Personal information and produce a handover document. |
| **Partner support guide** | Five labour stages (Early, Active, Transition, Pushing, After birth), 5–6 tips each |

### 6.4 Finance — Budget & finances (Journal → Finance)

Five steps with a clickable stepper: **Location → Healthcare → Income → Expenses → Summary**. Running totals are visible on every step.

| Step | Inputs |
| --- | --- |
| Location | Country (UK or US) and region; optional postcode/zip; optional "Save your details" (name, email, phone) |
| Healthcare | Country-specific intro and three optional cost items with ranges |
| Income (annual) | Your income, partner income, parental leave pay, savings, side income, benefits |
| Expenses (monthly) | 15 fields in Housing, Transport, Food, Lifestyle, Debt, with group totals |
| Summary | Results below, first-year typical cost ranges by country, Export as PDF, Ask Moira to read this |

**Formulas**

- Monthly income = (annual + partner + side + benefits) ÷ 12, rounded.
- Monthly expenses = sum of the 15 fields.
- Surplus = income − expenses (teal if ≥ 0, red if negative).
- Savings runway = savings ÷ monthly expenses, in months, rounded.
- Currency symbol and number format follow the chosen country (£ en-GB, $ en-US).

### 6.5 First Years

| Tool | Requirements |
| --- | --- |
| **Milestone tracker** | Ages 2, 4, 6, 9, 12 months; items in Social/emotional, Language, Movement; "x of y seen at age" |
| **Early development screener** | Ages 2, 4, 6, 9, 12, 18, 24 months; each item Yes / Not yet / Not sure. When all answered: 0 "Not yet" = no concern; 1 = worth a passing mention; ≥ 2 = *"Bring this list to your health visitor or GP."* |
| **Stimulation planner** | 5 age bands × Cognitive, Sensory, Motor |
| **Sensory play ideas**, **Music & movement** | 5 age bands × 3 activities with "how" |
| **Sleep battles helper** | 3 ages × 3–4 issues → 3 strategies |
| **Sibling transition** | 4 ages of the older child → preparation ideas, what to expect, helpful tips |
| **Communication helper** | 5 disagreement topics → note, conversation opener, 4 phrases |
| **Child nutrition planner** | 6 habits logged ("n of 6") and a plan |

---

## 7. Moira, cookies and legal

### 7.1 Moira

**Standard disclaimer** — use this exact wording on every Moira surface (FE):

> The same gentle reminder applies to Moira text and Moira voice.
> Moira is an AI-powered companion. She is not a doctor, midwife, or medical professional. The guidance she provides is for informational and support purposes only. Always consult a qualified healthcare professional for medical advice.

| ID | Requirement |
| --- | --- |
| FR-MOIRA-1 | Two forms: **Moira text** (type) and **Moira voice** (talk). Conversations stay private. |
| FR-MOIRA-2 | **Voice Moira** button in the lower-right corner of every signed-in page (FE). |
| FR-MOIRA-3 | Text drawer: right-hand panel (`min(420px, 100%)`, green gradient), *"Moira · Private · always on your side"*, greeting *"Hello. What would you like to understand about {stage}?"*, stage prompts, message list, input with Send (Enter sends). |
| FR-MOIRA-4 | Every Moira response is produced by AI and **identified as such** (LD3B). |
| FR-MOIRA-5 | Moira never stores or acts on an observation without asking first (§5.8). |
| FR-MOIRA-6 | **No Moira on onboarding pages** (FE). |
| FR-MOIRA-7 | Moira uses the user's **preferred name** (LD2) and, if given, a partner's first name (LD3B). |
| FR-MOIRA-8 | Only the minimum, de-identified information needed is sent to the external AI provider; voice is processed by a specialist voice provider, de-identified where technically possible (LD3B). |
| FR-MOIRA-9 | Entry points: inline Ask boxes (SSLP, SSHP, article), "People often start with" chips, the Voice Moira button, tool "Ask Moira" buttons, FAQ, Contact and Search empty states. |
| FR-MOIRA-10 | Persona, scope policy, suppression list and safety escalation are controlled in Admin → Moira control point and Safety review. |
| FR-MOIRA-11 | The chat is cleared on sign-out. |

### 7.2 Cookies

- **Banner** on every route until a choice exists. Copy (1D, LD1): *"BestBaby uses cookies to make our website work. We would like to set additional cookies to understand how you use our site and to improve your experience. Please see our cookies policy for further information."* Options: **Accept non-essential**, **Reject non-essential**, **More options** (preferences).
- **Preferences modal:** Essential (always on), Non-essential toggle, Save preferences or Accept all; closes on backdrop click or Esc.
- The choice is stored with a timestamp and can also be made on Page 1D and onboarding step 1.
- Non-essential cookies and analytics must **not** load until accepted.

### 7.3 Terms of Service (LD3A, Working Draft v5)

| Topic | Requirement |
| --- | --- |
| Role | BestBaby and Moira provide educational information and personalised guidance. **Nothing is medical advice, diagnosis or treatment.** User-submitted information is not independently checked. |
| Eligibility | Users confirm they are **18 or older** |
| Use of platform | Personal parenting, pregnancy and family support only; standard prohibitions (no copying, reverse-engineering, reselling, spam, malware, unlawful or offensive use); posted content must be true and accurate |
| User content | Users grant BestBaby a non-exclusive, worldwide, perpetual, irrevocable, royalty-free licence; BestBaby may remove content without notice |
| Accounts and fees | **Free.** Advance notice and full details before any paid feature |
| Affiliate links | Editorially curated affiliate recommendations are clearly identified |
| Data protection | BestBaby is controller. Users must not give special category data about others without their consent, unless they hold parental responsibility (a partner's first name for personalisation is allowed) |
| Liability | "As is"; no indirect or consequential losses; **aggregate liability capped at £10,000** |
| Termination | Either party: **28 days'** written notice; immediately for material breach not remedied within **14 days** |
| Law | **Scots law; Scottish courts have exclusive jurisdiction** |
| Schedule 1 — Beta | Accepted on first use; platform may contain bugs; Private Vault protected by **AES-256 field-level encryption**; no obligation to release commercially; testers give feedback (perpetual licence) and keep the platform **confidential** |

The document is titled *Terms of Service*; links elsewhere say *Terms of Use*. Use one name consistently (see §13).

### 7.4 Privacy Notice (LD3B, Working Draft v5)

| Topic | Requirement |
| --- | --- |
| Controller | BestBaby.Org Ltd, Scotland. Contact: **BetaContact@BestBaby.org** |
| Before registration | Email, solely to set up the account (short notice at email capture); limited contact data from giveaways/enquiries; IP address for security and operation |
| At registration | Name, email, **postal code** (to direct users to local guidance, e.g. NHS pathways and UK maternity rights), age |
| With specific consent | Journey stage, family situation, who is on the journey, topics of interest; children's first name, age and optional details; optional partner first name (Moira only) |
| Not collected | Payment details (a future payment provider would collect them directly) |
| After sign-up | Information shared with Moira or in tools may include special category data; **never collected or used without specific consent** |
| **Private Vault** | Special category data collected after sign-up, or not consented for BestBaby use, is held in an encrypted vault **accessible only to the user and to Moira during sessions, inaccessible to BestBaby staff**. Consented journey-stage data is held separately in account data. |
| Purposes | Contract (provide the service, administer the account); legitimate interest (enquiries, security, service information); **consent** for special category data and marketing |
| Marketing | Only with explicit consent; affiliate offers only if specifically consented; journey data used for marketing only with separate permission; withdraw any time |
| Recipients | Contracted service providers (hosting, cloud); external AI provider (minimum, de-identified data); voice provider; health advisers review **content only** and never access personal data; legal requirements; change of ownership (vault protections unchanged) |
| Transfers | Some providers are outside the UK; adequate safeguards required |
| Security | Encryption at rest and in transit; vault adds AES-256 field-level encryption |
| Retention | Duration of use **plus six years**; non-registered contacts no longer than needed and at most six years |
| Deletion | Content deleted; a record of **category and date** kept for legal purposes |
| Rights | Access, correct, delete, control what Moira uses, restrict, object, portability (structured, machine-readable), withdraw consent, no significant automated decisions. **Response within one month.** Complaints to the ICO (Wycliffe House, Water Lane, Wilmslow, SK9 5AF · ico.org.uk · 0303 123 1113) |
| Required to register | Name, email, postal code, age, journey stage and some family information |

Open legal points in the draft are listed in §13.

### 7.5 Marketing pages

| Page | Content |
| --- | --- |
| About | Mission, *"Everything you need, in the order you need it."*, five values, hello@bestbaby.org |
| FAQ | Topic filter (All, Using the site, Moira, Privacy, Our content); 12 accordion Q&As; Ask Moira; urgent-care note |
| Contact | hello@, editorial@, press@, privacy@; form (name, email, topic, message); response times (2 working days / 1 / 1 / 30 days); urgent note |
| Press | Fact sheet, boilerplate with Copy, media contact, brand assets, coverage |
| Careers | Perks and example roles, apply via careers@bestbaby.org |

All marketing pages must be linked from the footer once the footer is agreed.

---

## 8. Data and storage

### 8.1 Entities

| Entity | Fields |
| --- | --- |
| **Beta application** (1D) | first, last, email, country, call name, professional, heard about, why, cookie choice, applied at; status (Pending / Approved / Declined) |
| **Account** (LD2) | email, firstName, lastName, preferredName, postalCode, ageConfirmed, ageConfirmedAt, registrationCompleteAt, professional, heard about, onboarding-read timestamp (LD1), cookie choice, videoSeenAt |
| **Consent record** | type (terms/privacy c1 · special category c2 · marketing email · marketing text), given, timestamp, withdrawn-at |
| **Mobile number** | Only when marketing by text is opted in |
| **Journey profile** (LD4) | who, stage, interests[], due month/year, trimester, hasKids, children[{name, dob, sex}], partner first name |
| **Device** | recognised emails for this device |
| **Journal** | entries, to-dos {text, tag, done}, notes {text, time} |
| **Contact** | name, category, phone, email, essential |
| **Appointment** | date, title, place |
| **Moira observation / fact** | category, text, source, status (pending · confirmed · allowed), corrected, time — stored in the Private Vault once confirmed |
| **Deletion record** | category, date (no content) |
| **Tool data** | per tool (LMP, cycle, bag items, preferences, budget inputs…) |
| **Story** | title, body, stage, GDPR sign-off, destination (Blog / Forums), status |

### 8.2 Local storage (prototype)

| Key | Holds |
| --- | --- |
| `bb_accounts` | `{ [email]: {first, last, pref, stage, createdAt, videoSeenAt} }` |
| `bb_device_emails` | Emails recognised on this device |
| `bb_cookie_choice` | `{ nonEssential, at }` |

Clearing site data resets the demo to a first visit.

### 8.3 Seed data (prototype)

- Accounts: nadia@bestbaby.org, loucas@bestbaby.org (default user: Nadia).
- 7 contacts, 3 appointments, 2 notes, 3 journal entries, 5 to-dos.
- 4 Moira observations; 4 personal facts (Due date 8 Mar 2027, Care team, Monthly budget, Cycle length 28 days).
- 4 blog stories, 2 drafts, 4 market products, 12 FAQs.
- Fictional Edinburgh setting.

---

## 9. Non-functional requirements

### 9.1 Privacy and security

| ID | Requirement |
| --- | --- |
| NFR-PRIV-1 | No journey or health data is requested before the c2 consent — **not on LP0 and not on Page 1D** (FE, LD2). |
| NFR-PRIV-2 | Every consent is stored with a timestamp and can be withdrawn; withdrawal of c2 stops personalisation. |
| NFR-PRIV-3 | Private Vault: AES-256 field-level encryption, accessible only to the user and Moira during sessions, **inaccessible to BestBaby staff**. All data encrypted at rest and in transit (LD3B). |
| NFR-PRIV-4 | Users can **self-export** vault data and request account data in a machine-readable format; requests answered within **one month**. |
| NFR-PRIV-5 | Erasure keeps only category and date. Leaving the beta removes data from active use immediately, keeping a minimal opt-out record (LD1). |
| NFR-PRIV-6 | Data retained for the period of use plus six years (LD3B). |
| NFR-PRIV-7 | Transfers outside the UK only with adequate safeguards (LD3B). |
| NFR-PRIV-8 | Data is never sold, and never shared with third parties for their own marketing (LD1, LD2, LD3B). |
| NFR-PRIV-9 | Production replaces the shared site password with real authentication and genuine single-use, 15-minute magic links. |
| NFR-PRIV-10 | Calendar sync stays off until a data processing agreement is signed. |

### 9.2 Layout and the fold

- Design for both computer and phone screens and **minimise what falls below the fold** (FE).
- SSLP: arrows above the fold point to Explore the journey.
- SSHP: featured articles, or at least their titles, above the fold (§5.2).
- Article header images must work in every format without re-cropping.

### 9.3 Accessibility

**Present:** skip link to `#main`; `aria-current` on nav; `aria-expanded`, `aria-pressed`, `role=tablist/tab`, `role=menu`; `role=dialog aria-modal` on cookie modal, legal overlay, film and Moira drawer; visible focus ring (`#6E9275`, 2 px, 2 px offset); Esc closes overlays in order; `aria-live` on the contraction timer; darker stage inks for contrast.

**Required:**

- Focus trap and focus return in every dialog; move focus on route change.
- Meaningful `aria-label`s on icons (not raw icon names).
- Do not letter-space text that screen readers will spell out ("P R I V A T E   B E T A" — used in every client mock-up, so keep the look but give it a plain-text accessible name).
- Checkbox semantics for custom checkboxes.
- `aria-live` for validation messages and Moira replies.
- Label every input.

### 9.4 Responsive behaviour

| Breakpoint | Change |
| --- | --- |
| ≤ 1280 px | Four-up features → 2 columns |
| ≤ 1180 px | App nav collapses to a burger |
| ≤ 1000 px | SSLP three-column and tools grids stack |
| ≤ 900 px | Article stacks; public stage pills on their own scrollable row; second bar moves into the burger |
| ≤ 760 px | Section padding 18/44 px; H1 2 rem, H2 1.5 rem; stage banner and intro hidden; trust markers 2 columns without descriptions |
| ≥ 761 px and height ≤ 800 px | Compressed hero; banner at 21:9 |
| ≤ 700 px | Article hero 4:3 |
| ≤ 640 px | Voice Moira becomes an icon |
| ≤ 560 px | Features → 1 column |

Grids use `repeat(auto-fit, minmax(min(Npx, 100%), 1fr))`.

### 9.5 Offline packaging

The prototype is one self-unpacking HTML file. Images, WOFF2 fonts (Inter, Playfair Display, Caveat, Kalam) and React 18.3.1 are inlined; it runs from `file://` with no network.

---

## 10. Design system

### 10.1 Colour

| Group | Values |
| --- | --- |
| Brand / Moira green | `#1E3A2B` (primary, public header, Moira) · hover `#2F5240` · deep `#132A1E` · Moira accent `#8FB39A` |
| Muted greens | `#2F3E37` · `#4F6F52` · `#5A7A60` · `#F2F5F3` · `#E8EFE9` · `#EDF2EE` |
| Neutrals | page `#FAF7F2` · surface `#F8F6F2` · borders `#EDE6DE`, `#DED4C8` · text `#1F1F1F` · headings `#1B1B1B` · secondary `#444444` · muted `#6E6A64` |
| Connection & Growth | `#7B2FF2` · `#5A16C9` · ink `#2A1060` · CTA `#FFB547` (hover `#FFC468`) |
| Smart Tools | `#A0522D` · `#A35F43` |
| Finance | `#1F6F76` · `#13565C` · `#E5F0F1` |
| Error | `#C8382A` · `#962A1C` · `#FBEAE6` |
| Stages | See §2.1 |
| Brand mark | Gold/amber "best baby" logo with a sleeping-baby oval (used on the client page mock-ups) |

### 10.2 Typography

| Font | Use |
| --- | --- |
| Inter 400/500/600/700 | All UI. Eyebrows 12.5 px upper-case 0.14em; body and buttons ~15.2 px |
| Playfair Display 700 | Logo and headings. H1 2.4–3.2 rem, H2 1.75–2.6 rem, −0.01 to −0.02em; Georgia fallback |
| Caveat 500 | Handwritten Moira notes |
| Kalam | Journal entries |

### 10.3 Shape, spacing, motion

- Radius: pills 999 px · cards 12–16 px · numbered badges 10 px · chips 6 px.
- Shadows: cards `0 4px 12px rgba(0,0,0,.06)`; overlays `0 8px 24px rgba(0,0,0,.24–.28)`.
- Max widths: 80 rem (main), 84 rem (app bar); 72 / 44 / 40 / 34 rem for content.
- Section padding: 48–72 px vertical, 24 px horizontal.
- Motion: fade-in heroes (0.5 s), sliding Moira drawer, bobbing explore cue, 0.2 s hover lift.

### 10.4 Components

Pill buttons (primary green; secondary white with `#DED4C8` border) · pill toggles with ✓ and `aria-pressed` · stage cards with a colour bar · numbered guide cards · eyebrow and status pills · underline and segmented tabs · 5-step stepper · progress bars · toggle switches · action menus · inline confirm-delete panels · "Still needed: …" validation · right drawer · centred modals · video placeholder modal · Lucide icons.

---

## 11. Video inventory

All videos are still in production; the prototype shows placeholders (*"Coming soon · video is still in production"*).

| Page | Video | Length |
| --- | --- | --- |
| LP0 | Main video — "What is BestBaby?" | — |
| LD1 | Welcome audio in Moira's voice | — |
| Onboarding | Onboarding video — one-time | ~2 min |
| SSLP | Index video · SSHP stage video · C&G index video · Smart Tools index video · Moira index video | Index 3 min |
| SSHP × 4 | "{Stage} in Three Minutes" header video | 3 min |
| SSHP × 4 | C&G stage video | — |
| SSHP guides | Reality Check, Pathways · 1st/2nd/3rd Trimester · Understanding Birth, Pain and Coping, Recovery · Newborn, Toddler, Growing Up (all "possible") | — |

---

## 12. Prototype status against the requirements

### 12.1 Already aligned

- Stage colours and feature colours (§2), including the upgraded C&G purple.
- Header in the user's stage colour; body in the viewed stage colour.
- The Journey dropdown shows each stage title on a solid stage-colour bar with black or white text (R-COL-5).
- Trust bar labels per page, with descriptions on the SSLP only.
- Sign-in routing to SSLP / M1 / onboarding; registration and video once only.
- Page 1D fields (no journey questions), LD1, LD2 and LD4 fields and options, M1 copy.
- SSLP layout (article · video + Moira · article), copy for Smart Tools, Moira and "Where science meets real life".
- SSHP: "{Stage} in Three Minutes", the 16 featured categories, guide titles, "People often start with", standard Moira disclaimer.
- Article page: header bar with stage/topic/short title, ⅔ / ⅓ layout with featured articles, Moira and ad space.
- Voice Moira on every signed-in page.

### 12.2 Gaps against the source documents

| # | Requirement | Prototype today |
| --- | --- | --- |
| 1 | Trimester boundaries 1–12 / 13–27 / 28–40+ everywhere (LD4) | Due-date tool uses ≤ 13 / ≤ 26; guide copy uses 1–13 / 14–26 / 27–40+ |
| 2 | All LD4 answers and LD2 consents stored with timestamps | Only names, stage and timestamps are saved; other answers and marketing consents are lost and not shown in Settings |
| 3 | Smart Tools section on the SSLP should be smaller (FE) | Not yet reduced |
| 4 | SSHP fold behaviour: featured articles or their titles above the fold (FE) | Needs checking on laptop and phone heights |
| 5 | Featured cards show the **full** blurb (FE) | Check that blurbs are not truncated |
| 6 | Essentials Market not in a dropdown; Dialogue more prominent (FE) | Both in the second bar; final placement to be discussed |
| 7 | Onboarding video ends on the SSLP | Matches; but "Reset to first visit" (build control) does not reset |
| 8 | Moira Facts choices follow LD3B §2 (Edit/Correct, Confirm, Allow, Leave pending, Delete entirely) | Matches §2; LD3B §7 still uses older labels (see §13) |
| 9 | Vault self-export (LD3B) | "Export everything in my vault" is a stub |
| 10 | Consent withdrawal in Settings (LD2, LD3B) | Not present |
| 11 | Footer cleaned up before beta (FE, OB) | Still the prototype footer |

### 12.3 Simulated or stubbed

| Area | Status |
| --- | --- |
| Gate | Shared site password in client code; seeded emails always count as a recognised device |
| Beta application, magic link | Nothing is sent; no real expiry |
| Moira | Fixed reply: *"Moira isn't connected in this preview yet…"*; observations are seeded; no voice |
| Videos | Placeholders |
| Article bodies | Placeholder |
| Stubs | Journal Save/Dictate · Calendar month navigation and Add appointment · Vault PIN · Opt out of observations · Export vault, Request erasure · Story Submit/Save draft · Market Notify · Contact form · Finance save details and Export PDF · Birth preferences Save |
| Cookies | Choice stored, but nothing is actually gated |
| Dates | "Today" is fixed at 13 Aug 2026 in tools and calendar; onboarding uses the real date |

### 12.4 Known issues

| # | Issue |
| --- | --- |
| 1 | The routing matrix lists a "join" password path that is not implemented |
| 2 | "Open in your journal →" on a tool page does not select the tool |
| 3 | Guide cards and blog stories all open the stage's first article |
| 4 | Search hits for guide topics go to the top of the stage page, not the section |
| 5 | Calendar lists a September appointment under "This month" (August) |
| 6 | Kick counter has no timer and "Save session" only resets |
| 7 | Contraction timer shows no spacing or frequency |
| 8 | Week-by-week coach is not linked to the due date |
| 9 | Birth preferences produces no document; hospital bag is not saved |
| 10 | Finance ignores parental leave pay; uses en-US formatting for £; defaults to US; seeded fact "$2,493" differs from the computed $2,413 |
| 11 | Changing stage in Settings does not persist for seeded accounts |
| 12 | Genetic quiz does not make "None" / "Prefer not to say" exclusive |
| 13 | Nutrition plans are static and ignore inputs |
| 14 | Press "Copy boilerplate" copies only the first sentence |
| 15 | FAQ, Press and Careers have no inbound links; Contact and Tools are linked only from the FAQ |
| 16 | `showAnnotations` has no effect |
| 17 | Dead code: legacy 8-screen NR1–NR8 flow, gate success cards, route-based privacy and terms pages (the unused terms page says Irish law) |
| 18 | Off-palette stage colours in Stories and Contacts (`#8B5E3C`, `#7A8B9A`) |

---

## 13. Open questions and contradictions

| # | Topic | Detail | Source |
| --- | --- | --- | --- |
| 1 | Footer | Content and links to be agreed and cleaned up before beta | FE, OB |
| 2 | Journal, Your Moira, Dialogue, Market | Contents and navigation placement still to be discussed | FE |
| 3 | Trust bar wording | "Evidence-Based" (LP0, SSLP) vs "Evidence Informed" (SSHP, article); "Your Privacy First" vs "Privacy First" | FE |
| 4 | Terms name | Document is "Terms of Service"; links say "Terms of Use" | LD2, LD3A |
| 5 | Moira choices wording | LD3B §2 lists Edit/Correct, Confirm, Allow, Leave pending, Delete entirely; LD3B §7 still says "Moira only / Moira and BestBaby / Leave it pending / Delete entirely" | LD3B |
| 6 | Postal code | Collection pending confirmation by Lynn (BTO flag) | LD2 |
| 7 | Vault self-export | Supreet to confirm it is built; Lynn to confirm it satisfies Art. 20. Legal comment: subject-access requests (Art. 15) must still be answered, and portability covers all data, not only the vault | LD3B |
| 8 | Responding entity | The legal comment says *Media Marketing Investments Ltd* would respond to subject-access requests; the notice names BestBaby.Org Ltd as controller | LD3B |
| 9 | Data location | Prototype copy says "stays on this device" (tools, notes, finance, press) and "UK servers"; LD3B says data is encrypted in the vault and some providers are outside the UK | LD3B |
| 10 | Advertising | Article page has ad space (FE) but the prototype FAQ says "no advertising" — FAQ copy must change | FE |
| 11 | FAQ "Do I need an account? No…" | Contradicts the mandatory beta gate and registration (FE) | FE |
| 12 | Contact addresses | App@BestBaby.org (applications), BetaContact@BestBaby.org (consent, privacy, marketing opt-out) are confirmed; hello@, privacy@, editorial@, press@ in the prototype need confirming | 1D, LD2, LD3B |
| 13 | Topic and C&G pages | Guide topics may get their own pages with video; each stage's C&G infant-stimulation page is to be built | FE |
| 14 | Placeholders | "[Year]", "[Name]", "[registered address]", "[Publication]", "[Your parental leave policy]", and "[insert link]" in LD2/LD3A/LD3B | — |
| 15 | Finance default | Should the finance tool default to the UK? | — |
| 16 | Stage colours in Admin | Admin uses slightly different stage hex values (e.g. Before Pregnancy `#B07D8E` vs `#B5838D`) | — |

---

## 14. Production requirements (next steps)

1. Real authentication: per-user accounts, device recognition, single-use 15-minute magic links, email delivery (magic links, App@BestBaby.org application emails).
2. Server-side storage for every entity in §8.1, with consent records and the Private Vault protections in §9.1.
3. Persist every LD2 and LD4 answer and consent with timestamps; show and allow withdrawal of consents in Settings.
4. Connect Moira (text and voice) to the live engine with AI labelling, the observation-consent model in §5.8, and the standard disclaimer.
5. Article bodies, featured articles (four per stage, one per category) and images from the Admin CMS.
6. Produce and embed the videos in §11.
7. Real cookie gating, then analytics only after consent.
8. Finalise the footer, navigation placement and legal texts (§13), and fix the gaps in §12.2 and issues in §12.4.
