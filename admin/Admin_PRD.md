# PRD — BestBaby Admin Console

**Product Requirements Document** for `admin/admin.html`.

| | |
| --- | --- |
| Product | BestBaby.org: Admin console (back office) |
| Artefact | `admin/admin.html`, a self-unpacking offline bundle (~1 MB) |
| Status | Clickable design prototype. No backend, no persistence |
| Preview frame | 1440 × 940 |
| Companion doc | [`../Landing_PRD.md`](../Landing_PRD.md), the public site and signed-in platform |
| Last reviewed | 22 Oct 2026, against *BestBaby Back End 26.10.09* |

---

## 0. Source document

This PRD is aligned with the client's **BestBaby Back End 26.10.09** ("BE"), which describes the admin console as it works on the client's existing site and what they want in the final build. **Where the prototype and BE disagree, BE wins**; the differences are listed in §10.3.

BE also names the related public pages and onboarding documents; those are covered in [`../Landing_PRD.md`](../Landing_PRD.md).

> BE contains a team member's sign-in credentials in plain text. They are deliberately **not** copied into this PRD. Staff accounts must be provisioned in the real system, and the document should be stored somewhere access-controlled.

---

## 1. Overview

### 1.1 Purpose

The admin console is the private, role-based back office for the BestBaby.org team. It is where content is produced, reviewed and published. It is also where the AI companion Moira is supervised and where users, the team and site settings are managed.

Staff open it from the **Admin** link in the public site footer; the console then checks the email and password and admits the user according to their role (BE). Three principles are repeated throughout the UI:

1. **Access is role-based.** Each role sees only the screens it needs.
2. **Every sensitive action is logged** in an audit log that cannot be edited.
3. **AI output is always labelled.** Drafts from Morpheus, the AI drafting studio, are tagged *AI Created* and need a human sign-off before they can go live.

### 1.2 Scope

| In scope | Out of scope (for the prototype) |
| --- | --- |
| Staff sign-in and role preview | Real authentication, sessions and SSO |
| Editorial pipeline: Draft → For review → Pre-Published → Live | Persistence: all state resets on reload |
| Morpheus content studio (trend → sources → voice → draft) | Real web search, LLM or image-generation calls |
| Moira safety escalation and control point | The live Moira engine, tier keyword sets and crisis lists |
| Stories (user submissions) and their GDPR launch gate | Public story rendering |
| Affiliate catalogue, content gaps and trends | Affiliate tracking and analytics pipelines |
| Site users, Team, beta applications | Outbound email and invitation delivery |
| Notifications, Audit log, Database view, Documents | File storage, downloads and previews |

### 1.3 Goals

- **G1.** Content editors can take an article from an idea to submission without leaving the console.
- **G2.** Nothing medical or clinical reaches readers without a named medical reviewer's initials.
- **G3.** A safety escalation can be read, answered and closed by a person, and nothing leaves the platform without an explicit confirmation.
- **G4.** Supervisors can see and control who has access, and what each person did.
- **G5.** The taxonomy and the content inventory are visible in one place (the Database view).

---

## 2. Users and roles

### 2.1 Roles

| ID | Label | Summary |
| --- | --- | --- |
| `super_user` | **Supervisor** | Full access to all sections, including Users and Team. Can publish, feature and delete. Only role that can preview as another role. The site owner (LG) holds this role. |
| `content_editor` | **Content Editor** | Creates and edits **draft** articles and stories; uses the Morpheus Content Studio, Documents and Stories; submits articles for review by LG or a medical reviewer. Cannot edit published articles, publish or feature. |
| `medical_reviewer` | **Reviewer** | Access to **For review only**. Marks articles and stories that need changes (*TBR*) or initials them into Pre-Published for LG to review and publish. Review stamps use the account's initials automatically. Cannot create, edit or publish; no Morpheus, Documents or other sections. |
| `tech` | **Tech** | Full access to all sections; can publish and delete; **no** Users or Team. |

The user classifications offered in Site users are: User, Supervisor (BE: "Admin"), Tech, Reviewer, Content Editor.

### 2.2 Screen permissions

| Screen | Supervisor | Content Editor | Reviewer | Tech |
| --- | :-: | :-: | :-: | :-: |
| Dashboard, Articles, New article, Content Studio, Stories, Affiliate catalogue, Content gaps, Documents | ✓ | ✓ | – | ✓ |
| For review | ✓ | – | ✓ | ✓ |
| Pre-Published, Safety review, Moira control point, Notifications, Audit log, Database | ✓ | – | – | ✓ |
| Site users, Team | ✓ | – | – | – |

BE says a Content Editor's menu **cannot see** Users, Notifications, Database, Pre-Published, For review or Team, which the table above follows. The same BE role card also says Content Editors can "access Database, Documents & Stories" — see open question in §12.

### 2.3 Action permissions

| Capability | Roles |
| --- | --- |
| Approve into Pre-Published / mark Needs changes | Supervisor, Reviewer, Tech |
| Publish, take off site, feature, delete | Supervisor, Tech |
| Create and edit drafts | Supervisor, Content Editor, Tech |
| Publish a story immediately | Supervisor |
| Manage users, team, passwords and private papers | Supervisor |

**Rules**

- **R-ROLE-1.** A nav item is hidden when the role cannot open it. A nav group is hidden when all its children are hidden.
- **R-ROLE-2.** Opening a screen the role cannot reach shows *"Not available for this role"* with a way back.
- **R-ROLE-3.** "Preview as" is decided by the **signed-in** account's own role, not the role being previewed.
- **R-ROLE-4.** A user cannot delete themself, suspend themself, or demote their own Supervisor role.
- **R-ROLE-5.** Suspended accounts cannot sign in.

---

## 3. Information architecture

### 3.1 Shell

| Region | Requirements |
| --- | --- |
| **Sidebar** | Sticky, full height. "BestBaby" wordmark with an "ADMIN" eyebrow. Grouped navigation with icons and count badges. Collapses to a 72 px icon rail (238 px expanded); in rail mode group labels become rules and badges become dots. Footer link: **Back to site**. |
| **Header** (58 px, sticky) | Burger (≤ 980 px only); global search; **Preview as** role select (Supervisor only); account menu (initials avatar, name, "<Role> account", Profile, Log out). BE: the client likes the search ("if I can get it"); Preview as and the user info are **nice to have**, not required. |
| **Global search** | Placeholder *"Jump to an article, person or document…"*. Shows typed results after 2+ characters. |
| **Toast** | Bottom-centre pill, auto-hides after 3.2 s. |
| **Shared modals** | List drill-down, featured-slot assign, upload, picker, user detail, article preview, destructive confirm. |

### 3.2 Navigation

| Group | Items |
| --- | --- |
| — | Dashboard |
| **Content** | Articles · Content Studio · For review · Pre-Published · Stories |
| **Safety & Moira** | Safety review · Moira control point |
| **Commerce & insight** | Affiliate catalogue · Content gaps & trends |
| **People** | Site users · Team |
| **System** | Notifications · Audit log · Database · Documents |

"New article" has no nav item of its own; Articles stays highlighted while it is open.

**Badges:** For review (queue count), Pre-Published (queue count), Safety review (open flags), Stories (pending GDPR items), Content Studio ("9+").

### 3.3 Editor props

| Prop | Values | Effect |
| --- | --- | --- |
| `density` | `compact` (default) · `comfortable` | Articles table row height: 48 px or 60 px |
| `sidebarTone` | `dark` (default) · `light` | Sidebar `#1E3A2B` with ivory text, or white with charcoal text |
| `showBadges` | boolean, default `true` | Shows or hides nav badges and rail dots |

---

## 4. Functional requirements

Requirement IDs use the pattern `FR-<area>-<n>`.

### 4.1 Sign-in

Split screen: an auto-advancing hero carousel on the left, the sign-in form on the right.

| ID | Requirement |
| --- | --- |
| FR-AUTH-1 | Hero carousel with 4 slides (*Editorial control*, *AI drafting*, *Medical review*, *One database*). Advances every 6 s, pauses on hover, has dot controls with a progress fill. |
| FR-AUTH-2 | Fields: Email, Password. Button "Sign in" changes to "Signing in…" while busy. |
| FR-AUTH-3 | Validate email format (`^[^@\s]+@[^@\s]+\.[^@\s]+$`) and a non-empty password. |
| FR-AUTH-4 | Match the email case-insensitively against staff accounts. |
| FR-AUTH-5 | Error copy: *"Enter a valid email address."* · *"Enter your password."* · *"That email and password do not match an admin account. Ask a Supervisor to check your account in Team."* · *"This account is suspended. Ask a Supervisor to reinstate it."* |
| FR-AUTH-6 | On success, land on **Articles**, or **For review** for a Reviewer. Toast: *"Signed in as … · <Role>."* |
| FR-AUTH-7 | Footer: *"Forgotten your password? A Supervisor can reset it in Team."* and the support address. |
| FR-AUTH-8 | Logout clears the session and re-locks Team. |

Prototype only: a "Demo overlay" with one chip per role that fills in that account's credentials.

### 4.2 Dashboard

| ID | Requirement |
| --- | --- |
| FR-DASH-1 | Subtitle: "{n} articles · {n} active site users · previewing as {Role}". |
| FR-DASH-2 | **Needs your attention** cards (auto-fit grid, min 212 px): For review, Pre-Published, Unconfirmed aspect, Story submission, Unreviewed keywords. Show only cards the role can open and whose count is not zero. Each links to its screen. |
| FR-DASH-3 | Empty state: *"Nothing waiting on you / Every queue your role can reach is empty."* |
| FR-DASH-4 | **Editorial pipeline** strip: Drafts → For review → Pre-Published → Live, with clickable counts. A role without access gets *"Your role cannot open that queue."* |
| FR-DASH-5 | **Latest activity** feed — explicitly wanted by the client (BE). |
| FR-DASH-6 | Morpheus promo card ("Open Content Studio"), only for roles that can use Morpheus. |
| FR-DASH-7 | **Do not include** a content-insights section or an evidence-tier mix chart (BE: "I do not need that"). A sidebar of extra widgets is **to be decided**. |

### 4.3 Articles

**List**

| ID | Requirement |
| --- | --- |
| FR-ART-0 | Articles is the **landing screen** after sign-in. Editors and above can go straight to writing a **New article** from here (BE). |
| FR-ART-1 | Status stat chips: Needs attention, Drafts, Published, Featured, On the web, Was live on the web, All. Each shows a live count, and **clicking one shows the list of matching articles** (BE). |
| FR-ART-2 | "Needs attention" opens sub-chips: **All attention** (must always be available, BE), Aspect unconfirmed, Missing evidence tier, Missing medical review, Requires changes. |
| FR-ART-3 | Search over title, blurb, category, topics and author. Articles can be searched by **any part of the taxonomy** (BE asks for this to be reviewed carefully). |
| FR-ART-4 | Filters: Stage, Category (depends on stage), Topic (depends on stage and category), Format, Connection & Growth, Evidence tier (**AI Created excluded**, BE), Aspect, Featured (**Featured / Not featured only**, BE), Web status (**All, On the Web, Was Live, Not on Web, Never on the Web, Published – Not on Site, Featured – Not on Site**, BE). |
| FR-ART-5 | Default order: **Needs attention first, then drafts**, then the rest (BE). Other sorts: newest, oldest, title A–Z. "Clear filters" appears when any filter is set; show "{n} of {N} articles". |
| FR-ART-6 | Table columns: Title, Stage, Aspect, Evidence, Status. The title cell shows a stage-colour bar, the first warning as a pill (e.g. "Aspect unconfirmed +1"), and ★ if featured. |
| FR-ART-7 | Expanding a row shows (BE): the blurb; what is missing (warnings); **Stage, Category** (with dropdowns), **Evidence tier, Aspect, Format**, C&G, Featured, **Was live / On web**, **Topics** (first marked primary), **Author / who wrote it**, **who reviewed it**, Medically reviewed, **Published date**, Updated. |
| FR-ART-7a | **Legacy AI author.** Articles written by the old engine show a "⚠ Legacy AI Author" flag and "By: Morpheus / Moira engine — {date}", and a published state of "legacy" (BE example). |
| FR-ART-8 | 8 rows per page, with "Showing a–b of n" and Previous/Next. |
| FR-ART-9 | Empty state: *"No articles match these filters"* with Clear filters. |

**Row actions**

| Action | Shown to | Rule |
| --- | --- | --- |
| Edit | Roles that create articles | Hidden for a Content Editor when the article is live or published; "Read full article" is shown instead |
| Preview | Everyone | Opens the preview modal |
| Submit for review | Content Editor on a draft | Disabled while any warning other than *medical* remains; tooltip "Resolve: …" |
| Publish | Supervisor, Tech, on a non-live article | Disabled while **any** warning remains |
| Take off site | Supervisor, Tech, on a live article | Status → `off_site` |
| Feature / Unfeature | Supervisor, Tech | Toggles featured |
| Delete | Supervisor, Tech | Confirm: *"…and its revision history will be removed. This cannot be undone."* |

**Supporting panels**

| ID | Requirement |
| --- | --- |
| FR-ART-10 | **Returned with changes** panel lists items sent back, with the last reviewer note and "Returned by X · when". Action: *Fixed — resubmit for review*. |
| FR-ART-11 | **Bulk aspect backfill** (Supervisor, Tech): "{missing} of {total} articles still have an unconfirmed aspect", an "Only missing" filter, a per-row aspect select, and **Save all** (disabled until something is changed). Saving clears the *Aspect unconfirmed* warning. |
| FR-ART-12 | Banner P-B7: aspect labels are pending the Aspect Taxonomy Addendum check. |

### 4.4 New / Edit article

**Client workflow (BE).** On the client's current site, writing a new article works like this. The final build must support every step:

1. Pick a **stage**; the related **categories** drop down for that stage.
2. Toggle whether the article is **Connection & Growth** for this stage and category.
3. Pick one or more **topics** from the stage and category; **the first topic picked is the primary topic**.
4. Pick an **aspect** from a dropdown.
5. Enter **keywords**, then **Find Articles**.
6. The web is searched (make it as current and efficient as possible) for articles on parenting sites such as the NHS, BabyCenter and Parents.com; results list the **source and date**.
7. Open and read the **full** article, and **highlight the sections** to include. The writing instructions from the article engine are applied.
8. Pick the **voice**, then **Generate from sources** using the BestBaby article engine. The author's initials are attributed automatically.
9. The engine suggests a **title, slug, 40-word blurb** and the article, opened in edit mode. The article **always begins with an italic preamble**. The user can split paragraphs and change the voice.
10. **Rewrite with Morpheus** using one **or more** suggested prompts, or a custom prompt.
11. Add **references** and *Rewrite in BestBaby voice* (client asks whether this differs from Morpheus — §12).
12. **Images**: pictures found from the keywords. Choose a **header (main) picture**, **interior** pictures, or **save** for later; choices populate the sections above. Change keywords to search stock photos again, or **generate an AI image** by editing the suggested prompt and/or adding a reference image.
13. Check the **taxonomy** and initial **Created by**.
14. **Save** and open **Preview / Publish**: a mock article page where interior images are placed by paragraph and alignment, the main picture is adjusted, and the **Moira sidebar size** and **ad space** are set according to article length.
15. **Public preview** shows the page without the controls; unless edited, that is what is kept as the draft.
16. At the bottom, mark as **C&G** or **feature** it.

**Source extraction tool (BE).** "Read full article" must use a robust extractor. The client has a standalone tool (documented in `scripts/ARTICLE_EXTRACTION.md` on their side) that must be made to work in the editor:

| Requirement | Detail |
| --- | --- |
| Rendering | Playwright with Chromium; render JavaScript and wait for the page to load |
| Output | Clean Markdown with headline, subheadings, paragraphs and lists; author and publication date when available; the original source URL |
| Cleaning | Remove ads, sidebars and comments |
| Robustness | Handle blocked access, timeouts and malformed HTML **without bypassing access restrictions** |
| Warnings | Flag content that may be incomplete (shown as "Incomplete extraction") |

**Header**

- Title "New article" or "Editing draft"; "Created by {name} ({initials}) · recorded automatically".
- Readiness line: *Ready to publish* · *Ready — needs a medical review before it can go live* · *Ready to submit for review* · *Still needed: …*.
- Buttons: Editing preview, Public preview, Save draft, and a submit button labelled **Publish**, **Submit for medical review** or **Submit for review** depending on role and article.

**Main column**

| ID | Block | Requirement |
| --- | --- | --- |
| FR-ED-1 | Source search | Criteria chips (Stage, Category, C&G, Topics, Aspect, Keywords) and a keyword search. Each source shows an extraction badge: *Full text extracted*, *Incomplete extraction* or *Low-weight source*. Sections can be read and selected. **Generate title, blurb and draft** needs at least one selected section. |
| FR-ED-2 | Title \* | Playfair input; slug derived automatically; must be unique (case-insensitive). |
| FR-ED-3 | Blurb | About 40 words, shown on cards and in search. Counter "n / 40 words" turns clay above 45. |
| FR-ED-4 | Preamble | Italic standfirst. |
| FR-ED-5 | Body | Rich-text toolbar (B, I, U, H2, quote, lists, link, table), block style select, word count. |
| FR-ED-6 | Images | Stock search and **Generate with AI** (prompt, optional reference image). Each image gets a role: Not used, Main / header, Interior, Saved for later. Only one Main; an older Main moves to Saved. Interior images get "After paragraph N" and Left / Right / Full width. |
| FR-ED-7 | Layout | Main image focus (centre/top/bottom), Moira sidebar width (300/340/380 px), ad space (300×250, 300×600, none). |
| FR-ED-8 | Rewrite in BestBaby voice | Voice select (BestBaby voice, Moira — warm and personal, Plain and clinical), prompt presets, custom instruction, reference text and files (.txt .md .html .csv .json .pdf .docx). |

**Classification panel** (sticky, "n of 3 set")

| Field | Rule |
| --- | --- |
| Stage \* | 4 colour chips. Changing stage resets category and topics. |
| Aspect \* | 11 options. Internal only, never shown to readers. |
| Evidence tier \* | 6 chips. Internal only. |
| Read time | Minutes. |
| Format | Article, Guide, Checklist, Explainer, Video. |
| Category | Disabled until a stage is chosen. |
| Topics | Chips from the category; the first pick is marked primary. |
| Keywords | Free text. |
| Connection & Growth | Checkbox. |
| Feature this article | Supervisor and Tech only. |

**Sign-off**

- **FR-ED-9.** *Your initials \** must equal the signed-in account's initials (case-insensitive). Hint: "Must match your account initials (XX)."

**Preview modal**

- **FR-ED-10.** Two modes, *Editing preview* and *Public preview*. Shows the stage bar, main image, title, preamble, blurb, body with interior images floated after their paragraph, and an aside with a stage card, the Moira sidebar and an ad slot.
- **FR-ED-11.** Editing mode adds ✎ markers and layout controls, and a size hint: more than 900 words suggests a 380 px sidebar and a 300×600 ad; more than 450 words suggests 340 px and 300×250; otherwise 300 px and consider no ad.

### 4.5 Morpheus content studio

| ID | Requirement |
| --- | --- |
| FR-MOR-0 | **On opening, the Studio automatically searches the web** for what is trending (BE). Providers: OpenAI web search and Google Custom Search, **or any equivalent that does not incur cost**. On the client's site OpenAI works and Google does not. |
| FR-MOR-1 | Search providers bar: each provider *Not checked*, *Working* or *Failing*. **Run diagnostics** at the top shows a per-provider report with a suggested fix. |
| FR-MOR-2 | Three-step stepper: **Find a trend → Gather sources → Voice and generate**. A later step cannot be opened until the earlier one is done (*"Finish step N first."*). |
| FR-MOR-3 | Step 1: "Trending right now" cards per stage (top 3 searches with volumes), plus a search by stage, topic or custom keywords and **Suggest 6 searches**. **Find sources →** needs at least 1 trend. |
| FR-MOR-3a | Topic search per stage, or custom keywords (e.g. "measles"), returns **six variations of what parents are typing right now**; the user picks one or more, then searches for articles (BE). |
| FR-MOR-4 | Step 2: sources for the first trend; select sources. **Each source must open in full** — not a synopsis — with sections that can be highlighted for the article, exactly as in the New article tab (BE). **Set the voice →** needs at least 1 source. |
| FR-MOR-5 | Step 3: article brief (stage, aspect, working title, reader goal) and voice dials (Warmth, Evidence density, Reading age 9–11 / 12–14 / 15+). |
| FR-MOR-6 | **Generate draft** opens **the same edit-article screen as the New article tab** (BE), pre-filled, with tier = **AI Created**, keywords = chosen trends, and a body built from the highlighted sections plus a provenance sentence. |
| FR-MOR-7 | Copy rule: *"Every generated draft lands unpublished, tagged AI Created, and needs a human sign-off."* |

### 4.6 For review

| ID | Requirement |
| --- | --- |
| FR-REV-1 | Tabs: All, Articles, Stories, with counts. |
| FR-REV-2 | Card: title, kind/stage/aspect/tier pills, blurb, "Submitted by X · when · N words", review note history. Stories also show whether the GDPR acknowledgement is recorded. |
| FR-REV-3 | **Initial → Pre-Published** records the reviewer's initials and the note "Approved for Pre-Published." |
| FR-REV-4 | **Needs changes (TBR)** requires a note (*"The writer sees this note with the article."*) and returns the item to its author. |
| FR-REV-5 | A story without a GDPR acknowledgement cannot be accepted. |
| FR-REV-6 | Empty state: *"Nothing waiting for review."* |
| FR-REV-7 | After a TBR item is corrected, it comes back to the reviewer, who **must initial it** before it moves to Pre-Published (BE). |

### 4.7 Pre-Published

| ID | Requirement |
| --- | --- |
| FR-PRE-0 | Holds **articles and stories** that reviewers have initialled, awaiting final review and publishing by LG (BE). |
| FR-PRE-1 | Same cards as For review, plus an "Approved by XX" pill, and a counter "n waiting on final review". |
| FR-PRE-2 | **Publish** (Supervisor, Tech): the item leaves the queue; the article goes live, marked medically reviewed, with the approver recorded as reviewer. |
| FR-PRE-3 | **Send back to review** requires a note and clears the approval. |
| FR-PRE-4 | Other roles see *"Final publish is limited to the Supervisor and Tech."* |

### 4.8 Stories

| ID | Requirement |
| --- | --- |
| FR-STO-0 | All blog posts and stories submitted from the site come here for review before pre-publishing — or, for the Supervisor, direct publishing — to the **Blog** or **Forums**. Users sign off the GDPR considerations **before** they can submit (BE). |
| FR-STO-1 | **GDPR launch gate**: four items must be confirmed before public launch — Consent language, Lawful basis, Privacy policy, Journal privacy. |
| FR-STO-2 | **Link Stories in site navigation** is enabled only at 4/4. Unchecking any item takes Stories out of the navigation again. |
| FR-STO-3 | Submission tabs: All, Submitted, Under review, Approved, Published, Rejected. |
| FR-STO-4 | A submission lists what is missing before it can be published (Stage, Category, Topics, Evidence tier, Sign-off). Actions: Open & classify, Feature, Reject (confirm). |
| FR-STO-5 | Destination: Blog or Forums. Routing: *For review* (roles that create articles), *Pre-Published* (Supervisor, Tech), *Publish now* (Supervisor). All routes are disabled without the GDPR acknowledgement. |

### 4.9 Safety review

| ID | Requirement |
| --- | --- |
| FR-SAF-1 | Queue of conversations Moira escalated, with tier pill (Tier 4 dark red, Tier 3 clay), time, user, excerpt and an "Open n" counter. |
| FR-SAF-2 | Detail pane: transcript with the flagged turn highlighted, "Why this escalated", and a note that tier keyword sets and crisis resources are fixed in the engine. |
| FR-SAF-3 | Editable suggested response, kept per flag. It is sent as an **admin message, not as Moira**. |
| FR-SAF-4 | **Send what**: the response as written / crisis resources only (Samaritans, 111, 999) / a short check-in with no resources. |
| FR-SAF-5 | **To whom**: the user in their Moira conversation / the user by email / a saved emergency contact. The emergency contact needs prior consent on file and is available for **Tier 4 only**. |
| FR-SAF-6 | **When**: immediately / hold for a second admin to co-sign / tomorrow at 09:00. |
| FR-SAF-7 | **Nothing is sent until the admin confirms** in a summary panel ("Confirm before anything leaves the platform"). The flag closes as *Sent* or *Awaiting co-sign*. |
| FR-SAF-8 | **Mark as false positive** (confirm). The flag closes; the match stays in the safety log. |

### 4.10 Moira control point

| ID | Requirement |
| --- | --- |
| FR-MOI-1 | Shows the live version (e.g. v4.2 · 12 Sep 2026) and version history. |
| FR-MOI-2 | Editable **Persona** ("Tone only — never clinical authority") and **Topic and scope policy**. **Save as new version** creates a draft that the live engine picks up on deploy. |
| FR-MOI-3 | **Suppression list** of phrases Moira must never use, with add and remove. Seeds: "you should stop taking", "this is definitely", "diagnose", "safe dose". |
| FR-MOI-4 | **Not editable here** (locked): Tier 3 keywords, Tier 4 keywords, crisis resource list. Changing these is an engineering change with a compliance record. |

### 4.11 Affiliate catalogue

| ID | Requirement |
| --- | --- |
| FR-AFF-1 | Products offered in the Essentials Market, with "N products · n active". |
| FR-AFF-2 | Columns: Product and vendor, age/stage/goal tags, Price, Display order (↑ ↓), Active/Hidden toggle, Edit. Display order controls the Market grid. |
| FR-AFF-3 | **Add product** captures name, vendor, affiliate link, price, tags and active state. |

### 4.12 Content gaps & trends

| ID | Requirement |
| --- | --- |
| FR-GAP-1 | **Content gaps**: searches with no matching published article — topic, stage, search count, a bar, and **Draft with Morpheus**. |
| FR-GAP-2 | **Trending searches · last 7 days** with counts and change. |
| FR-GAP-3 | **Searched, nothing returned**. Morpheus triages these into the Studio queue; a person still writes the brief and approves the draft. |

### 4.13 Site users

| ID | Requirement |
| --- | --- |
| FR-USR-1 | Summary: "{n} accounts — {a} active, {p} pending an activation, {s} suspended". Beta access is invite-only. |
| FR-USR-2 | Filters: search (name, email, account ID, location, stage), classification (User or a team role), status (Pending, Active, Suspended). |
| FR-USR-3 | Table: Person, Location, Stage, Status (with classification and "You"), Joined, Actions. 10 per page. |
| FR-USR-4 | Actions: View; Activate (pending, Supervisor); Suspend / Reactivate (Supervisor, not on self; content stays in place); Delete (Supervisor, not on self; a record of the data category and date is kept for legal purposes). |
| FR-USR-5 | **Export CSV** (`bestbaby-users.csv`): Name, Email, Initials, Classification, Stage, Status, Location, Joined, Account. Audited. |
| FR-USR-6 | **User detail dialog**: counts (saved articles, comments, stories), 18 profile fields from onboarding (consents, cookies, sign-up source, journey, interests), and a *Manage account* form (display name, initials ≤ 3 upper-case, email, location, classification). Actions: Save profile, Send password reset link, Delete user. |
| FR-USR-7 | Role permission cards summarise what each role can do. |

### 4.14 Team

| ID | Requirement |
| --- | --- |
| FR-TEAM-1 | Team is behind a second password gate (*"Team is password protected"*). Opening it is audited. |
| FR-TEAM-2 | **Not all users are on the team, but every team member is a user** (BE). Team must be tied to Site users: role, initials and other details stay in sync in both places, and the Supervisor can edit any of them. |
| FR-TEAM-3 | **Add to team** from existing users (added as Content Editor). |
| FR-TEAM-4 | Table: Account, Initials (inline, ≤ 3), Role (select; cannot demote self), Password (Change; at least 6 characters), Can reach, Edit details, Preview. |
| FR-TEAM-5 | **Private papers** (Supervisor): a place for private documents such as contracts — upload, open, delete (BE). |
| FR-TEAM-6 | Role, initials and password changes are written to the audit log. |

### 4.15 Notifications

| ID | Requirement |
| --- | --- |
| FR-NOT-1 | **Beta applications** from the public "Join the Beta" form: name, status (Pending, Approved, Declined), date, Email, Country, preferred name, healthcare/childcare professional, heard about, cookies, reason for joining. |
| FR-NOT-2 | **Approve & invite** sends an invitation to Basic Registration. **Decline** (confirm) tells the applicant the beta is full and keeps only a minimal record. |
| FR-NOT-3 | Email rules (toggles): |

| Event | Sends to | Can turn off |
| --- | --- | :-: |
| Beta application received | App@BestBaby.org | ✓ |
| Story submitted from the public site | Content Editors | ✓ |
| Safety flag (Tier 3 or 4) | Supervisor and Tech | **No — always on** |
| Article submitted for review | Reviewers | ✓ |
| Article returned with changes | The author | ✓ |
| Approved into Pre-Published | Supervisor | ✓ |
| Article published | Author and reviewer | ✓ |

### 4.16 Audit log

| ID | Requirement |
| --- | --- |
| FR-AUD-1 | Sensitive actions only: publishing, deleting, role changes, suspensions and similar. **Entries cannot be edited.** |
| FR-AUD-2 | Columns: When (en-GB, e.g. "13 Oct 2026, 09:12"), Who (initials), Action, Item. Newest first. |
| FR-AUD-3 | Filter by person, action or item. |
| FR-AUD-4 | Audited today: publish, take off site, feature/unfeature, delete article; approve, mark changes, return to review; delete user, change classification, password reset, export users; open Team, change role, change password, add to team, delete private paper; approve/decline beta; publish story; suspend/restore user. |

### 4.17 Database (read-only view)

*"Read-only view of what the site is actually serving."*

| ID | Requirement |
| --- | --- |
| FR-DB-0 | The client asks for the Database page to keep this breakdown: **Full Taxonomy, Stages, Categories, Topics, Articles, Featured, Search, Documents, Site settings** (BE). |
| FR-DB-1 | Stat cards that switch tabs: Stages (4), Topics, Articles (live/drafts), Featured slots (filled/16), Search index, Documents. |
| FR-DB-2 | **Full Taxonomy**: Stages 4, Categories, Topics, Aspects 11, Formats 5, Evidence tiers 6. The categories must match the public site: **four per stage, 16 in total** (see FR-DB-7). |
| FR-DB-3 | **Stages**: ID, name, topic and article counts (drill-down), colour swatch. |
| FR-DB-4 | **Categories**: grouped by stage, with topic chips, article count, and an inline **keyword editor** (add with Enter, remove, case-insensitive de-duplication). |
| FR-DB-5 | **Topics**: active toggle, search, sort (Active first, A–Z, Most articles), rename, keywords, delete. 12 per page. |
| FR-DB-6 | **Articles**: Live, Drafts, Published but held off site, Missing aspect (blocks publishing). Each count opens a list. |
| FR-DB-7 | **Featured**: one slot per category, grouped by stage — **16 slots**, because every SSHP shows the four latest featured articles, one from each of its four categories (public FE spec). Assign, change or remove (confirm). The categories are: |

| Stage | Featured categories (public site) |
| --- | --- |
| Before Pregnancy | Readiness & Reality Check · Pathways to Parenting · Planning Ahead · Building Your Foundation |
| Pregnancy | 1st Trimester · 2nd Trimester · 3rd Trimester · Feathering the Nest |
| Birth | Your Birth Choices · Understanding Birth · Pain and Support Coping · Complications |
| First Years | 0 – 3 months · 3 – 12 months · 1 – 3 years · 3 – 5 years |

| ID | Requirement |
| --- | --- |
| FR-DB-8 | **Search**: test the search index; matches title, blurb, stage and aspect. |
| FR-DB-9 | **Documents**: story submissions and library files. |
| FR-DB-10 | **Site settings** for the public landing page: "Learn About Smart Tools" headline size (17/23/31 px, live preview), hero video show/hide and Vimeo ID (digits only), hero headline and subtitle. |
| FR-DB-11 | **Beta compliance holds** (read-only, enforced server-side): Calendar sync *Held*, NR5 special category consent *Enforced*, Moira AI watermark *On*. |

### 4.18 Documents

| ID | Requirement |
| --- | --- |
| FR-DOC-1 | Internal reference library. **Uploads are never served to readers.** |
| FR-DOC-2 | Libraries with per-role visibility. **Manage libraries**: create (name required and unique, description, roles), edit (rename re-maps files), delete (only non-fixed and empty). "Editorial" is fixed. |
| FR-DOC-3 | Filters: library pills with counts, file-name search, file type. |
| FR-DOC-4 | Table: File, Document type (Spec, Brief, Reference, Guide, Audit, Research — changeable), file type badge, Size, Uploaded, By, Actions (Preview, Download, Move, Delete). 10 per page. |
| FR-DOC-5 | Upload accepts DOCX, PDF, MD, CSV, TXT up to **10 MB**. Errors: wrong type, over 10 MB, duplicate name, no file chosen. |

---

## 5. Workflows

### 5.1 Editorial pipeline

```
          Save draft                Submit                Initial (reviewer)        Publish (Supervisor/Tech)
 [Draft] ───────────▶ [Draft] ─────────────▶ [For review] ───────────────▶ [Pre-Published] ───────────▶ [Live]
                                                │   ▲                          │                        │
                                Needs changes   │   │ Fixed — resubmit         │ Send back (note)       │ Take off site
                                  (note)        ▼   │                          ▼                        ▼
                                            [Requires changes]            [For review]             [Off site]
```

- **Direct publish.** A Supervisor or Tech whose article needs no medical review can publish straight from the editor.
- **Medical review is needed** when the aspect is *Medical & Clinical*, or the tier is *Scientific* or *Clinical Adjacent*, and the article has not been medically reviewed.
- **Submit from the list** (Content Editor) is blocked by any warning except *medical*. **Publish from the list** is blocked by any warning.
- Content Editors cannot edit live or published articles.

### 5.2 Stories

Submission → classify → GDPR acknowledgement check → For review / Pre-Published / Publish now (Blog or Forums). The Stories section only appears in public navigation after all four GDPR items are confirmed.

### 5.3 Safety escalation

Moira flags (Tier 3/4) → admin reads the transcript → edits the response → chooses what, to whom and when → **explicit confirm** → *Sent* or *Awaiting co-sign*. Alternatively → *False positive* (match stays logged).

### 5.4 Beta access

Public "Join the Beta" application → emailed to App@BestBaby.org → **Approve & invite** (Basic Registration invitation) or **Decline** → user becomes Active on approval or via **Activate** in Site users.

---

## 6. Data model

### 6.1 Entities

| Entity | Key fields |
| --- | --- |
| **Article** | title, slug, stage, category, topics[] (first is primary), aspect, tier, format, cg, featured, status, onSite, everLive, author, creator, reviewers[], medReviewed, blurb, preamble, body, keywords, images[], published, updated, warnings[] |
| **Queue item** | id, kind (Article / Story), title, stage, aspect, tier, by, when, words, blurb, at, reviewedBy, notes[], gdpr, dest |
| **User** | account ID (`bb-user-xxxx`), name, preferred name, initials, email, location, postal code, joined, last seen, sign-up source, stage, newsletter, marketing, special-category consent (NR5), age confirmed, registration complete, welcome acknowledged, cookies, healthcare professional, heard about, journey, interests, saved/comments/stories counts, status, classification |
| **Staff account** | user + role + password |
| **Beta application** | name, email, country, preferred name, professional, heard about, cookies, reason, applied date, status |
| **Safety flag** | id, tier, user, time, excerpt, transcript[], reason, draft response, done label |
| **Moira config** | version, persona, scope policy, suppression list |
| **Product** | name, vendor, tags[], price, display order, active |
| **Category / Topic** | stage, name, slug, keywords[], active |
| **Featured slot** | category → article, assigned date |
| **Document / Library** | name, ext, library, type, size, date, uploader / library name, slug, description, roles[], fixed |
| **Audit entry** | when, who, action, item |

### 6.2 Enumerations

| Enum | Values |
| --- | --- |
| Stage | Before Pregnancy · Pregnancy · Birth · First Years |
| Aspect (11) | Medical & Clinical · Emotional & Psychological · Practical & Logistical · Financial & Legal · Relational & Social · Nutritional & Physical · Baby & Child Development · Decision-making & Options · Cultural & Spiritual · Expert Research · Stories & Experience |
| Evidence tier | Scientific · Clinical Adjacent · Researched · Experience · Opinion · AI Created |
| Format | Article · Guide · Checklist · Explainer · Video |
| Article status | `draft` · `live` · `off_site` |
| Web status | On the Web · Featured – Not on Site · Published – Not on Site · Was Live · Never on the Web |
| Warning | Aspect unconfirmed · Missing evidence tier · Missing medical review · Requires changes |
| Queue stage | `review` · `pre` · `changes` |
| User status | Pending · Active · Suspended (Deleted counted) |
| Beta status | Pending · Approved · Declined |
| Safety tier / outcome | Tier 3 · Tier 4 / Sent · Awaiting co-sign · False positive · Resources sent |
| Document type | Spec · Brief · Reference · Guide · Audit · Research |

---

## 7. Business rules and validations

| ID | Rule |
| --- | --- |
| BR-1 | Article titles are unique, case-insensitive: *"Another article is already called '…'"*. |
| BR-2 | To submit, an article needs a title, stage, aspect, evidence tier and matching sign-off initials. Save draft needs only a title. |
| BR-3 | Changing stage resets category and topics. |
| BR-4 | Only one main image per article. |
| BR-5 | Aspect and evidence tier are internal and never shown to readers. AI Created is not a reader-facing filter. |
| BR-6 | Initials are at most 3 characters, stored upper-case. |
| BR-7 | Team passwords are at least 6 characters. |
| BR-8 | Vimeo ID is digits only. |
| BR-9 | Uploads: DOCX, PDF, MD, CSV, TXT; ≤ 10 MB; no duplicate name in a library. |
| BR-10 | A library must be empty before it is deleted; fixed libraries cannot be deleted. |
| BR-11 | Safety alert emails cannot be turned off. |
| BR-12 | The emergency-contact recipient is available only for Tier 4 flags, and only with prior consent on file. |
| BR-13 | Moira's tier keyword sets and crisis resource list cannot be edited in the console. |
| BR-14 | Stories cannot be linked in public navigation until all four GDPR items are confirmed. |

---

## 8. Non-functional requirements

### 8.1 Security and privacy

- **NFR-SEC-1.** Production must use server-side authentication, hashed passwords and a password **reset** flow. Passwords must never be shown (the prototype shows them in Team).
- **NFR-SEC-2.** Role checks must be enforced on the server, not only by hiding UI.
- **NFR-SEC-3.** The Team gate must not be a client-side constant.
- **NFR-SEC-4.** Deleting a user keeps only a record of the data category and date, for legal purposes.
- **NFR-SEC-5.** Special-category consent (NR5) is enforced server-side.

### 8.2 Auditability

- **NFR-AUD-1.** Every sensitive action is written to an append-only audit log with time, person and item.
- **NFR-AUD-2.** Safety sends, false positives, Moira config changes, product changes, taxonomy edits, document moves and deletes, settings changes, user activation and library changes **must also be audited** (they are not in the prototype).

### 8.3 Accessibility

- Visible focus ring: 2 px solid `#5A7A60`, offset 2 px.
- Honour `prefers-reduced-motion`.
- **Escape** must close every modal and overlay. Destructive confirms must be keyboard-reachable.
- Form fields must show an error state, not only a banner.

### 8.4 Responsive behaviour

| Breakpoint | Behaviour |
| --- | --- |
| ≤ 1180 px | Two-column split layouts become one column |
| ≤ 980 px | Sidebar becomes an off-canvas drawer (266 px) with scrim and burger; rail mode off; sign-in hero reduced to brand and tagline; modals align to top |
| ≤ 760 px | Header wraps; search takes a full row |
| ≤ 640 px | Three-column grids become two; "Preview as" label and account name hidden; H1 25 px |

Wide tables keep a minimum width (e.g. Articles 968 px, Users 1,040 px, Team 1,120 px) and scroll horizontally.

### 8.5 Offline packaging

The prototype ships as one self-unpacking HTML file with inlined fonts, images and React 18.3.1. It runs from `file://` with no network.

---

## 9. Design system

### 9.1 Colour

| Group | Tokens |
| --- | --- |
| Neutrals | ivory `#FAF7F2` (page) · linen `#F4EEE7` (table heads, chips) · sand `#E8E1D7` (borders, disabled) · char `#2E2E2E` (body) · charL `#6A6A6A` · charD `#1B1B1B` (headings) · mute `#9C9C9C` |
| Sage | sage900 `#2F3E37` · sage700 `#5A7A60` (links, focus) · sage50 `#F2F5F3` · sageSoft `#E8EFE9` · sage200 `#C8D9CC` |
| Primary action | cta `#1E3A2B` (hover `#2F5240`) |
| Clay (warning, danger) | clay `#C9A08A` · clayL `#E9D4C8` · clayD `#A67962` · clayM `#A35F43` · danger `#8C3820` |
| Stages | Before Pregnancy `#B07D8E` · Pregnancy `#C2872F` (ink `#8A5E14`) · Birth `#B34A2A` · First Years `#4E7C85` (ink `#3A5F67`) |
| Stage tints | `#F7EFF1` · `#FAF2E6` · `#F9EDE9` · `#ECF1F2` |
| Accents | moira `#4F6F52` · indigo `#4A3DB5` (C&G, AI images, editing markers) · slate `#7A8B9A` |

Stage labels use the darker ink variants for legibility.

### 9.2 Typography

| Use | Style |
| --- | --- |
| UI | Inter 400/500/600/700 |
| Brand, H1, card titles, big numbers, modal titles | Playfair Display 500/600/700 |
| Slugs, IDs, file badges | `ui-monospace` |
| H1 | Playfair 32 px / 600 / −0.015em (25 px on mobile) |
| Section eyebrow | 11 px / 700 / 0.13em / upper-case / `#9C9C9C` |
| Table header | 10.5 px / 700 / 0.1em / upper-case / `#6A6A6A` on `#F4EEE7` |
| Body | 12.5–14.5 px |
| Pills | 11 px / 600 |

### 9.3 Shape, spacing and elevation

- Radius: pills and buttons 9999 px · cards 14 px · modals 16 px · panels 10–12 px · inputs 9–10 px · small controls 7–8 px.
- Page padding 28 / 24 / 64 px. Card padding 16–22 px.
- Shadows: dropdowns `0 10px 28px rgba(0,0,0,.10–.12)` · modals `0 24px 60px rgba(0,0,0,.24)`. Scrim `rgba(27,27,27,.42–.55)`.

### 9.4 Components

- **Buttons:** Primary (`#1E3A2B` pill), Go (`#5A7A60`), Ghost (white with sand border), Danger (clay text and border), Disabled (sand, mute text).
- **Pills, chips, checkbox squares, radio cards, toggle switches** (44 × 26).
- **Tables:** CSS grid, fixed column templates, hover `#FAF7F2`, expandable rows with a rotating chevron.
- **Pager**, underline **tabs**, filter **pills with counts**.
- **Empty states:** a bold line with helper text, sometimes in a dashed box.
- **Confirm modal** with destructive styling; **toast** on `#2F3E37`.
- **Charts:** no library; pipeline counts with tinted bars and progress bars.

---

## 10. Prototype status

### 10.1 Simulated or stubbed

| Area | What is simulated |
| --- | --- |
| Sign-in | Client-side check against seeded staff, 450 ms fake delay; one shared demo password; Team PIN is a constant |
| Morpheus | Trends, sources, diagnostics and draft generation are canned. "Rewrite draft" only shows a toast |
| Images | Stock search and AI generation produce placeholder tiles |
| Editor | Rich-text toolbar and block select do nothing; Read time is not saved |
| Stories | One hard-coded "Test Story" with fixed tab counts |
| Toast-only actions | Profile, Add/Edit product, document Preview/Download, private paper Open, DB Refresh, password reset email, Morpheus "Also here" tools |
| Site settings | Change only local state, despite "take effect immediately" |
| Persistence | None; everything resets on reload |

### 10.2 Seed data

- 5 staff: Loucas George (Supervisor), Supreet (Tech), Dev account (Tech), Kathryn George (Content Editor), Anna Reid (Reviewer).
- 7 users (the staff plus a test user and one beta applicant).
- 18 articles (12 draft, 5 live, 1 off site; 3 featured).
- 4 review-queue items, 2 beta applications, 3 safety flags, 6 products, 9 categories / 120 topics, 9 featured slots, 9 documents in 4 libraries, 3 Moira versions.

### 10.3 Gaps against the Back End document

| # | BE requirement | Prototype today |
| --- | --- | --- |
| 1 | Categories match the public site: 4 per stage, 16 featured slots | **9 categories and 9 slots** (e.g. Birth has "Labour & Delivery" and "Postpartum Recovery"; First Years has "Sleep & Settling" and "Feeding & Nutrition") |
| 2 | Clicking a stat chip lists the matching articles | Chips filter the table in place — confirm this meets the request |
| 3 | Legacy AI-author articles flagged ("⚠ Legacy AI Author", "By: Morpheus / Moira engine") | Not modelled |
| 4 | Real web search for sources (NHS, BabyCenter, Parents.com…) with source and date | Four canned sources |
| 5 | Full-article extraction with Playwright/Chromium and incomplete-content warnings | Canned extracted sections |
| 6 | Morpheus searches automatically on opening; no-cost provider | Manual; diagnostics are canned |
| 7 | Edit/preview controls, AI rewrite with several prompts, image search and AI images | Present as UI; generation, rewriting and images are simulated |
| 8 | Team tied to Site users for all details | Role and initials sync; other details only through the user dialog |
| 9 | Team member names | Client refers to **Kathryn Riordan** as the Content Editor; the prototype seeds "Kathryn George" |
| 10 | Notifications show beta application emails | Present (Approve & invite / Decline) |
| 11 | No content-insights or evidence-tier-mix widgets | Not rendered (the code for them is unused) |

---

## 11. Known issues

| # | Issue | Impact |
| --- | --- | --- |
| 1 | `sidebarW` is used both for the shell sidebar width and the editor's Moira-sidebar width; the editor value wins | Sidebar width / rail may break on desktop |
| 2 | Two generations of render logic; older values are overridden and left as dead code | Maintainability |
| 3 | The Reviewer "Not available" page offers "Go to Dashboard", which Reviewers cannot open | Dead end |
| 4 | Dashboard "Unconfirmed aspect" counts every warning, including tier warnings | Wrong count |
| 5 | Audit seed uses initials "SK", which no account has (Supreet is "ST") | Data inconsistency |
| 6 | Two featuring mechanisms; assigning a slot clears the featured flag on articles not in a slot | Lost state |
| 7 | Hard-coded badges ("9+", Stories); Notifications badge never set | Misleading counts |
| 8 | Many actions are not audited (see NFR-AUD-2) | Contradicts "every action is logged" |
| 9 | Saving Moira config relabels the version but adds no history row; suppression phrases not de-duplicated | |
| 10 | Approving a beta applicant who is not in Users creates no user; approval exists in two places | Duplicate paths |
| 11 | Pending status pill uses the Active style in the user dialog | Visual |
| 12 | Documents type filter lists only DOCX and PDF, though MD, CSV and TXT uploads are accepted | Unfindable files |
| 13 | Content Editor role copy omits Safety, Moira and Audit from its hidden list | Copy |
| 14 | Escape does not close most modals; confirm modal has no backdrop close | Accessibility |
| 15 | Resolved safety flags can be sent again; co-sign has no second-admin step | Safety |
| 16 | Login fields never show an error state | Accessibility |
| 17 | List "Preview" shows title, blurb and stage only, no body | |
| 18 | "Draft with Morpheus" from Content gaps does not carry the topic | Extra work |
| 19 | Database: per-article table overwritten by the summary; Stages IDs are 1, 2, 3, 5 | |
| 20 | Story "Route to" can add duplicate queue entries | |

---

## 12. Open questions

| Ref | Question |
| --- | --- |
| P-B7 | Aspect labels must be checked against the *Aspect Taxonomy Addendum*. |
| P-B8 | Support email domain is pending confirmation with Loucas. |
| — | Is "Rewrite in BestBaby voice" in the editor different from Morpheus rewriting, or the same feature? |
| — | Should featuring be per-article, per category slot, or both? (see issue 6) |
| — | Which single place approves beta applicants: Notifications or Site users? |
| — | What does the second-admin co-sign flow look like for safety sends? |
| BE | Content Editor and the Database: the role card says Content Editors can "access Database, Documents & Stories", but the same card says their menu cannot see Database. Which is right? |
| BE | Team passwords: the client wants passwords "seen and changed" in Team. Production should store hashed passwords and offer a reset instead (NFR-SEC-1). Agree the approach with the client. |
| BE | Which no-cost web search provider replaces Google Custom Search? |
| BE | Should featured categories in Admin be renamed to the 16 public categories, or should Admin categories and featured categories be separate lists? |
| BE | Article sidebar widgets on the dashboard are "TBD". |

---

## 13. Production requirements (next steps)

1. Backend with persistence for every entity in §6, and server-side role enforcement.
2. Real authentication: hashed passwords, reset by email, session expiry, optional SSO.
3. Append-only audit log covering every action in NFR-AUD-2.
4. Real integrations: web search (a no-cost provider where possible), the Playwright/Chromium source extractor, LLM drafting, image generation and stock search, all with provenance and the *AI Created* label.
5. Align the taxonomy with the public site: four featured categories per stage, 16 featured slots.
6. Live Moira engine connection: versioned persona and policy deploys, safety flag ingestion, message and email delivery, co-sign workflow.
7. Working rich-text editor and image upload.
8. Outbound email for notification rules and beta invitations.
9. Fix the known issues in §11 and the gaps in §10.3.
