# BestBaby — Landing & Platform Prototype

A clickable, self-contained prototype of the BestBaby.org platform: a science-backed
companion for the parenting journey, from before conception through the first five years.

The whole thing is one file — [`BestBaby Landing V6 (offline).html`](BestBaby%20Landing%20V6%20%28offline%29.html)
(~7.7 MB). No server, no build step, no network access required.

## Quick start

Open the HTML file in any modern browser (double-click, or drag it into a tab).

A loading overlay reads "Unpacking…" for a moment while the bundle rehydrates itself,
then the private-beta gate appears.

### Signing in to the demo

The gate at the top of the landing page asks for an email and a site password.

| Field | Value |
| --- | --- |
| Site password | `bestbaby` |
| Seeded account | `nadia@bestbaby.org` or `loucas@bestbaby.org` |

Where the gate sends you depends on the email:

- **A seeded account** → straight into the signed-in platform (stage home page).
- **An unknown but valid email** → the eight-screen new-registration flow (`nr1`).
- **A known account on an unrecognised device** → the magic-link screen (`m1`).

A wrong password or malformed email is rejected in place. Everything is evaluated in the
browser; there is no backend.

## What's in the prototype

### Public / pre-sign-in

| Route | Page |
| --- | --- |
| `lp0` | Landing page with the private-beta gate |
| `beta` | Beta waiting-list application |
| `nr1` | New registration — 8 screens, including a hard consent gate at NR5 |
| `m1` | Magic-link sent / resend |
| `nr7` | Welcome video (a 2-minute simulated player) |

### Signed-in platform

| Route | Page |
| --- | --- |
| `stage` | Stage home page — the main hub |
| `article` | Article reader |
| `journal` | Your Journal — Today, To-do, Tools, Finance, Personal information |
| `calendar` | Calendar & Notepad |
| `contacts` | Your Contacts (care team, family, work & school) |
| `moira-space` | Your Moira — the AI companion's space |
| `moira-facts` | What Moira has observed about you, with confirm/edit/delete |
| `dialogue` | Dialogue, Blog & Forum — stories, drafts, messages, events |
| `market` | Essentials Market |
| `search` | Search across stages and content types |
| `settings` | Account settings |
| `tool` / `tools` | Individual interactive tools and the tool index |

### Marketing & legal

`about`, `faq`, `contact`, `press`, `careers`, plus Terms, Privacy and Cookies documents
rendered in an overlay. A cookie banner and preferences modal are wired up.

## The four stages

Content is organised around four life stages, each with its own palette, banner image,
guide structure, article set, tool list and Moira prompts:

| Stage | Colour | Window |
| --- | --- | --- |
| Before Pregnancy | `#B5838D` | Before |
| Pregnancy | `#E0A030` | 40 weeks |
| Birth | `#C8382A` | The day |
| First Years | `#377A91` | 0–5 yrs |

Each stage carries a `guide` of themed sections (e.g. *Readiness & reality check*,
*First trimester*, *Understanding birth*, *Toddler*), each holding numbered topic cards
with four bullets apiece.

## Interactive tools

Several tools are genuinely functional rather than static mock-ups:

- **Due date calculator** — 280 days from the last period
- **Fertility window** — derived from cycle length
- **Week-by-week coach** — milestones matched to the due date
- **Kick counter** and **contraction timer** — live session timers
- **Hospital bag checklist** — grouped, tickable, with custom items
- **Birth preferences** — builds a handover document
- **Budget & finances** — a five-step planner (location → healthcare → income →
  expenses → summary) seeded with realistic figures
- **Milestone tracker**, **sleep helper**, **sibling transition**, **genetic risk quiz**,
  **lifestyle audit**, **doctor visit prep**, **sensory play**, **music & movement**,
  **nutrition planners**, **early development screener**

## Build-preview props

The prototype exposes editor-adjustable props, grouped into three sections. They are read
from the component's `data-props` attribute and drive the initial state:

**Patch review**
- `showAnnotations` (boolean, default `true`) — design annotations overlay
- `userStage` (enum, default `before-pregnancy`) — which stage you land in

**Stage home pages**
- `showSectionBar` (boolean, default `false`) — sticky in-page section nav
- `cgPanel` (enum: `research` | `video` | `articles`, default `research`)

**Build review**
- `showBuildControls` (boolean, default `false`) — exposes the device-state toggle on the gate
- `deviceRecognized` (boolean, default `false`) — skips the gate straight to the platform
- `startRoute` (enum, default `lp0`) — jump directly to any of `lp0`, `sslp`, `nr1`,
  `beta`, `stage`, `article`, `settings`, `journal`, `calendar`, `moira-space`,
  `moira-facts`, `m1`, `nr7`, `cookies`

Opened as a plain file, the defaults apply.

## Local storage

The prototype persists a small amount of state under these keys:

| Key | Holds |
| --- | --- |
| `bb_accounts` | Registered demo accounts |
| `bb_device_emails` | Emails treated as recognised on this device |
| `bb_cookie_choice` | Cookie banner decision |
| `bb_landing_video_seen_at` | Timestamp of the welcome video |

Clear site data for the file's origin to reset the demo to a first-visit state.

## How the offline bundle works

The file is a self-unpacking bundle rather than hand-written HTML. Its structure:

- A small loader script in `<head>`
- `<script type="__bundler/manifest">` — every asset as base64 (images, WOFF2 font
  subsets for Inter and Caveat, the React UMD builds)
- `<script type="__bundler/ext_resources">` — the four stage banner images plus
  React 18.3.1 and ReactDOM 18.3.1 (`react.production.min.js`, `react-dom.production.min.js`)
- `<script type="__bundler/template">` — the real document, JSON-encoded
- `<script type="__bundler/page_order">` — empty; there are no nested page bundles

On `DOMContentLoaded` the loader mints blob URLs for every asset, substitutes the UUID
placeholders in the template, swaps the document, and runs the app. Because every asset is
inlined, it works from `file://` with no network connection.

The app itself is a single class component in Claude's declarative-component (`x-dc`)
format: markup with `{{ }}` bindings and `<sc-if>` conditionals, driven by a `<script
type="text/x-dc">` block holding the content constants, state and handlers.

### Editing it

The bundled file is not a practical editing target — the template is a single
800 KB JSON-encoded line. To inspect or modify it, decode the `__bundler/template`
script's JSON payload to get readable HTML, then re-encode.

## Caveats

This is a design prototype, not a product build:

- No backend, API or persistence beyond `localStorage`
- The site password is a hard-coded string in client-side source; it gates a demo, not data
- Moira's responses, the welcome video and the magic-link flow are all simulated
- Content is illustrative and is **not** medical advice
