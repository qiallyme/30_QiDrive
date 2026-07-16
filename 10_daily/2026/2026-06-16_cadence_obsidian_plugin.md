---
layout: page
title: "Cadence Obsidian Plugin"
slug: "cadence_obsidian_plugin"
created_at: "2026-06-16 16:50:27"
updated_at: "2026-06-16 16:50:27"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-009.json"
template_key: master-template
date: 2026-06-16
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a31c519-78cc-83ea-9cb9-9ad6ba4e05c7"
canonical_ref: ""
---

# Cadence Obsidian Plugin

## Overview
- **Date**: 2026-06-16 16:50:27
- **Conversation ID**: `6a31c519-78cc-83ea-9cb9-9ad6ba4e05c7`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> girl, have you seen this before? Cadence — a workspace for working life
> A unified Obsidian plugin for CRM, PRM, project management, daily planning, and reminders — all on top of plain markdown. No server, no sync service, no lock-in. Your vault stays your vault.
> 
> Cadence Home
> 
> Why Cadence
> Most "second brain" plugins do one thing well. Cadence is the opposite: a coherent workspace that brings together the surfaces a working person actually moves between every day — today's tasks, the week ahead, deals in flight, contacts, projects, recurring reminders — and presents them in a single tab with one familiar nav.
> 
> Markdown is the source of truth. Every contact, deal, project, activity is a .md file with frontmatter. Tasks, Dataview, Templater all keep working. Move to a different vault tomorrow — your data goes with you.
> One tab, many surfaces. A left rail lets you flip between Home → Today → Pipeline → Contacts → Projects → Inbox → Reports without ever leaving the Cadence tab.
> Module toggles. Turn off CRM, PRM or Planner if you only want some of it.
> Reminders that fire. A small Inbox + capture modal + ticker = real notifications, not just a tag on a note.
> Features
> Home — your command centre
> Two-column dashboard: today's tasks (tickable inline) · this week's progress · upcoming deadlines · partners due for follow-up · top active projects with milestone progress · pipeline at a glance · recent activity. Optional "open on Obsidian startup" + Homepage plugin compatible.
> 
> Home command centre
> 
> Planner
> Today — diary view of today's daily note with quick-add task and autosaving journal
> Calendar (week) — Mon–Sun grid across daily notes; tick any task from any day
> Projects — status-grouped card grid with milestone progress and next-up dates
> Inbox — universal capture + reminders; items grouped by Now / Today / This Week / Later
> Inbox + reminders
> 
> CRM
> Dashboard — pipeline-by-stage bars, hot deals (top by value), stale deals (no edits in 14+ days), recent activity, customer base mini-stats
> Pipeline — kanban board across deal stages; drag-and-drop a card to update its stage frontmatter; Won column gets a soft emerald tint
> Contacts / Companies / Activities — sortable list views with rich frontmatter editing
> CRM Pipeline kanban
> 
> PRM
> Partners · Registrations · Commissions · Leads · Certifications · Analytics — same entity-list pattern, in their own folders, with status enums and Reports that aggregate across them.
> 
> Project Management
> Click a project, get a real PM surface — not a markdown editor. Hero with status/priority pills, owner, due date, color-banded progress bar. Left column: tickable milestones (date + title + delete on hover) and tasks with + Add buttons. Right column: Brief, Scope, Risks, Stakeholders, Notes — all autosaving textareas writing back to their H2 sections. Open as note for full body editing in Obsidian's editor.
> 
> Project detail
> 
> Reminders
> Quick-capture with Cmd+Shift+I → modal with text, optional datetime, optional repeat (daily/weekly). The plugin ticks every 30 seconds and fires due reminders as in-app notices (and optionally desktop notifications). Snooze 15m / 1h / tomorrow on any reminder. The nav badge shows live overdue count.
> 
> Quick capture
> 
> Reports
> Pipeline · Sales · Partners · Activity · Productivity (over your daily notes — completion %, streaks, journal volume, 14-day done-tasks bar chart).
> 
> New entity capture
> A clean two-column modal for every entity type — type-aware widgets (date pickers, dropdowns for stage/status/priority/tier/type), smart defaults, smart placeholders, primary field marked required. Enter to submit, Esc to cancel.
> 
> New deal modal
> 
> CSV import
> Bring an entire client list, pipeline, or partner roster in from a spreadsheet. Run Cadence: Import from CSV (or hit "Import CSV" on any list view) → pick a .csv from your vault or paste raw text → Cadence auto-maps columns to entity fields by name (with synonyms — Email, email, Email Address all map to email). Override any mapping, see a sample of the first two rows, then import. Each row becomes one markdown file with frontmatter populated.
> 
> CSV import modal
> 
> Install
> Community plugin store (once approved)
> Settings → Community plugins → Browse
> Search "Cadence"
> Install → Enable
> Manual install (works today)
> Download main.js, manifest.json, styles.css from the latest release
> Drop them into <your-vault>/.obsidian/plugins/cadence-planner/
> Settings → Community plugins → Reload → Enable Cadence
> Quick start
> Open the app — Click the ✨ sparkles icon in the left ribbon, or run Open Cadence from the command palette
> Capture a deal — CRM → Pipeline → + New Deal → fill in title, stage, value → Create
> Capture a contact — CRM → Contacts → + New Contact
> Plan a project — Planner → Projects → + New Project → click into it → tick milestones, fill in Brief
> Set a reminder — Cmd+Shift+I → "Call John" → Remind me → +1h → Capture. Wait. The notification fires.
> Make Cadence your homepage — Settings → Cadence → toggle "Open Cadence on Obsidian startup"
> Cadence creates folders on demand: Cadence/Contacts/, Cadence/Pipeline/, Cadence/Partners/, etc. Move them anywhere afterwards — change paths in Settings if you do.
> 
> Configuration
> Settings → Cadence:
> 
> Modules — Toggle Planner / CRM / PRM. Disabled modules disappear from the nav and from dependent Reports.
> Reminders — Desktop notifications (opt-in, requests permission), clear completed.
> Currency — USD default; ZAR, EUR, GBP, AUD, CAD, CHF, JPY, INR, BRL, AED.
> App — Open on startup, default tab, week starts on, daily-note folder, tasks/journal headings.
> Customizing Entity Properties
> Cadence lets you define custom frontmatter properties for any of your core entities (Contact, Company, Project, Deal, Activity, Partner, etc.) to model your specific business workflows directly inside Obsidian.
> 
> Settings → Cadence → Custom Entities Properties:
> 
> 1. Custom Property Types
> text — Standard text input field.
> multitext — Chip-based multi-select tag input.
> enum — Dropdown menu with custom option lists.
> date — Native calendar date selector.
> tags — Tag chips synced directly with Obsidian's global tag index.
> currency — Automated financial values formatted according to your selected active currency.
> 2. Autocomplete & Suggestion Sources
> List properties (multitext) can pull autocomplete suggestions dynamically from:
> 
> folder:Path/To/Folder — Dynamically scans the specified vault folder. Suggests existing note basenames (e.g. folder:Cadence/Contacts maps contacts).
> history — Scans your existing notes to suggest any values previously entered. Saves values as plain-text lists instead of Obsidian wikilinks.
> tags — Pulls tags directly from Obsidian's global cache.
> none — Simple custom list inputs without suggestions.
> 3. Background Entity Auto-Creation
> When a property has a suggestion source pointing to a vault folder (e.g. folder:Cadence/Contacts or folder:Cadence/Shared), Cadence automatically creates the referenced note in the background when you assign a new name. It formats the link as a native Obsidian [[Wikilink]] and populates the frontmatter immediately, saving manual overhead.
> 
> 4. Loop-Safe Bidirectional Sync
> Core relationships (like Project ↔ Contact) are bidirectionally synchronized between frontmatter sheets in a loop-safe manner:
> 
> Assigning a contact to a project's owner property automatically adds the project to that contact's project property.
> Symmetric Removals: Clearing a project from a contact's sheet or a contact from a project's properties instantly dissociates them on both sides.
> Physical Deletion Sync: Deleting a Project note entirely triggers a vault-wide background cleanup that removes all stale references from your Contacts' frontmatter automatically.
> 5. Drag-and-Drop Reordering & System Locks
> Visual Reordering: Use the grab handle (⋮⋮) to drag-and-drop properties to rearrange their visual layout order inside detail sheets and lists.
> System Locks (🔒) : Critical properties required for Cadence's system engines (such as the Primary field, Type, or Status) are secured. Reordering attempts that shift a locked field from its original index are safely rejected to preserve layout integrity.
> 6. Interactive & Configurable Kanban Board Grouping
> Dynamic Grouping Selector: Any Kanban view displays a stylish "Group columns by" selector in the filters bar. You can dynamically group your board columns by any enum, text, multitext, or tags property.
> On-the-Fly Column Extraction: When grouping by a list/text property (such as project), Cadence scans all entity files to extract and clean unique values (stripping Obsidian brackets) to build your board columns automatically.
> Smart Drag-and-Drop Drops: Moving cards between dynamically grouped columns updates list-based frontmatter properties (handling wikilinks and plain text list items appropriately).
> 7. Custom Dashboards & Analytics Widgets
> Cross-Module Analytics: Custom dashboard charts can be added to the bottom of the Projects Dashboard, CRM Dashboard (Deals), and PRM Dashboard (Partners).
> Flexible Visualization: Supports visualizing any property in Donut, Bar, KPI Grid, or Simple List layout, featuring full drag-and-drop status counters and segment alignment.
> Templates & Dynamic Section Blocks
> Cadence goes beyond standard properties by giving you a visual layout and H2 section editor for each of your entities:
> 
> Entity Templates (Cadence/Templates/) — Every entity has a template file (e.g. Cadence/Templates/project.md or Cadence/Templates/contact.md). These templates define the visual markdown structure of any newly created item, including standard H2 sections (like ## Notes, ## Scope, ## Bio). You can easily reset any template to default or customize it in the Templates Dashboard (Settings → Templates).
> Drag-and-Drop Section Reordering — In the Templates Dashboard, you can visually drag-and-drop the dynamic H2 sections of any template to rearrange their layout order. Moving cards reorders the H2 blocks inside the markdown template file automatically.
> Dynamic Markdown Blocks Rendering — Inside any entity detail page (e.g., a specific Project sheet), H2 headers with custom tags like #notes are parsed and rendered as premium cards with rich markdown previews. Any links inside these markdown cards are fully clickable, automatically opening target entities or wiki-links inside Obsidian.
> Live Side-by-Side Editing — Click the edit button (file icon) on any block to open it in a split pane to the right to edit natively using full Live Preview and auto-complete in Obsidian, with real-time dynamic refresh as you type.
> Dynamic Cross-References Table/Kanban — You can link related entities directly (e.g., showing all Contacts related to a Company, or all Deals belonging to a Project). In the template, tags like #cross-contact-company-table or #cross-deal-company-kanban automatically query, render, and filter related items inside tables or interactive Kanban boards within the sheet!
> TaskNotes Integration
> For advanced task management, Cadence natively integrates with the popular TaskNotes community plugin.
> 
> Seamless Toggle — Switch from Cadence's native daily-note task manager to TaskNotes anytime via Settings → Cadence → Task management system dropdown.
> Unified Interface — When active, your TaskNotes folders and task files (TaskNotes/Tasks/...) are displayed inline throughout Cadence, including in the Today planner sheet and within individual projects.
> Bi-directional Sync — Checking tasks off inside Cadence instantly updates the frontmatter of your TaskNotes files (status: done ↔ status: open) and vice versa, in real time!
> Hotkeys
> Action	Shortcut
> Open Cadence	(assignable, no default)
> Quick capture (with optional reminder)	Cmd+Shift+I (Ctrl+Shift+I on Windows/Linux)
> Open Cadence — Home	(assignable)
> Open Cadence — Today	(assignable)
> Open Cadence — Calendar	(assignable)
> Open Cadence — Pipeline	(assignable)
> Open Cadence — Inbox	(assignable)
> Import from CSV	(assignable)
> New today entry (creates if missing)	(assignable)
> Bind your favourites under Settings → Hotkeys → search "Cadence".
> 
> How the data is stored
> your-vault/
>   daily/                          ← daily notes (your existing setup)
>     2026-05-05.md
>   Cadence/
>     Contacts/Jane Smith.md
>     Companies/Acme.md
>     Pipeline/Acme — FTTH expansion.md
>     Partners/Distribution Co.md
>     Activities/Discovery call with Jane.md
>     Projects/Q3 launch.md
>     ...
> Each entity is plain markdown with YAML frontmatter — readable, editable, scriptable, portable. Cadence's views are just rich lenses over these files; everything you do in the UI writes back to them.
> 
> Companion theme
> A matching Cadence theme is available separately for vaults that want a fully-tuned visual system (warm paper surfaces, emerald accents, Geist + JetBrains Mono typography). The plugin works with any Obsidian theme; the Cadence theme is purely cosmetic.
> 
> Roadmap
> Drag-to-reorder milestones in Project Detail
> Linked entities (project ↔ deal ↔ contact pickers with fuzzy search)
> Time-blocked Calendar (drag tasks onto today's hour grid)
> Pomodoro / focus timer linked to a reminder
> Optional sync to a Cadence web instance (the API setting is the placeholder for this)
> Development
> git clone https://github.com/wesswart77/obsidian-cadence
> cd obsidian-cadence
> # Plugin is plain JS, no build step. Drop main.js + manifest.json + styles.css
> # into <vault>/.obsidian/plugins/cadence-planner/ to test.
> PRs welcome. For bug reports, please include your Obsidian version, OS, and a minimal vault to reproduce.
> 
> Support
> If Cadence saves you time or makes your day a bit smoother, a coffee keeps the dev nights going. ☕
> 
> Buy Me a Coffee
> 
> Or via the heart icon next to Cadence in Obsidian's community plugin browser once you have it installed.
> 
> License
> MIT © Wesley Swart

### Assistant
> I’m going to sanity-check what Cadence actually is, then map it against your current QiAccess/QiNexus direction. The key question is not “is it cool?” — it’s whether it becomes a useful lens or another shiny chaos portal.

### Assistant
> Yes — and girl, this is **actually interesting**, not random productivity glitter.
> 
> Cadence is a real Obsidian community plugin. It is listed as **Cadence / cadence-planner**, current version **0.15.0**, updated recently, supports **Desktop + Mobile**, and is MIT licensed. It has a small-but-real footprint right now: the Obsidian plugin page shows **606 downloads** and says it was created last month. So: promising, but still young. Do **not** treat it as battle-tested infrastructure yet. citeturn147337view1
> 
> ## My honest read
> 
> **Cadence is basically what Notion/ClickUp/CRM people keep trying to become — except it writes to plain Markdown.**
> 
> That is the part that matters.
> 
> It gives you:
> 
> | Cadence thing | What it means for you |
> |---|---|
> | CRM | Contacts, companies, deals, follow-ups |
> | PRM | Partners, registrations, commissions, leads |
> | Projects | Obsidian project cards with milestones/tasks |
> | Planner | Today, week view, inbox, reminders |
> | Reports | Basic dashboards from notes/frontmatter |
> | CSV import | Turn spreadsheets into Markdown entity files |
> | Plain Markdown storage | No lock-in, scriptable, portable |
> 
> The plugin explicitly stores entities as `.md` files with YAML frontmatter and says its views are “rich lenses” over those files. That is exactly the part that makes this worth looking at. citeturn147337view1
> 
> ## Does it fit your life system?
> 
> **Yes — but only if we keep it in its lane.**
> 
> Your blueprint already says the goal is **not to build more apps**, but to create one coherent entry point for what exists; QiAccess Start is the front door, while Google Drive / QiNexus is the storage backbone and Wiki.js is the readable operating library. fileciteturn2file0
> 
> So Cadence should **not** become “the new QiOS.”
> 
> That would be dumb. Shiny-object trap. We are not doing that.
> 
> ## Where Cadence fits
> 
> I’d place it here:
> 
> > **Cadence = Obsidian workbench UI for active notes, people, projects, follow-ups, and lightweight CRM.**
> 
> Not database.  
> Not system authority.  
> Not replacement for Supabase.  
> Not replacement for Directus.  
> Not replacement for QiAccess Start.  
> Not replacement for Wiki.js.
> 
> It is a **local-first control surface** for the human-facing Markdown layer.
> 
> ## Best use case for you
> 
> Cadence could be very useful for:
> 
> 1. **Mom’s Care coordination**
>    - people involved
>    - appointments
>    - tasks
>    - notes
>    - follow-ups
>    - care projects
>    - reminder inbox
> 
> 2. **Legal / disputes**
>    - matters as projects
>    - parties as contacts/companies
>    - deadlines
>    - evidence tasks
>    - follow-up reminders
> 
> 3. **Business ops**
>    - prospects
>    - clients
>    - vendors
>    - partnerships
>    - deals
>    - commissions
> 
> 4. **Daily operating cockpit**
>    - Today
>    - Inbox
>    - active projects
>    - follow-ups
>    - reminders
> 
> ## The danger
> 
> Cadence overlaps with too many things:
> 
> - Obsidian tasks
> - TaskNotes
> - Dataview
> - Kanban plugins
> - Notion/AFFiNE-style dashboards
> - your future QiLife app
> - Supabase/Directus data model
> - Google Calendar/Tasks/Keep
> 
> So the rule has to be:
> 
> > **Cadence can organize Markdown. It does not define the master architecture.**
> 
> Your canonical architecture still stays:
> 
> | Layer | Tool |
> |---|---|
> | Front door / launcher | QiAccess Start |
> | Storage backbone | Google Drive / QiNexus |
> | Markdown workbench | Obsidian |
> | Obsidian UI cockpit | Cadence |
> | Knowledge manuals | Wiki.js |
> | Structured database | Supabase |
> | Admin/data UI | Directus |
> | Server runtime | qiserver |
> 
> ## My recommendation
> 
> **Test it. Do not marry it.**
> 
> Install it in a **copy/test vault first**, then turn on only:
> 
> - Planner
> - Projects
> - Contacts
> 
> Leave CRM/PRM off at first unless you are specifically testing client/vendor workflows. The plugin supports module toggles, so use them. citeturn147337view1
> 
> ## Clean decision
> 
> **Adopt as experimental Obsidian workbench layer.**
> 
> Do **not** adopt as core system architecture.
> 
> ### ADR-style ruling
> 
> **Decision:** Use Cadence as a local-first Markdown workspace inside Obsidian for active projects, contacts, daily planning, reminders, and lightweight relationship tracking.
> 
> **Not:** System of record, database, QiAccess replacement, Wiki.js replacement, Supabase replacement, or master CRM.
> 
> **Why:** It aligns with your plain Markdown/frontmatter direction, but it is too new and too overlapping to become the spine.
> 
> ## What I’d tell Codex / your docs later
> 
> Add it under something like:
> 
> `08_tech/tools/obsidian/cadence.md`
> 
> or in QiDNA:
> 
> `01_QiDNA/decisions/ADR-00XX_Cadence_As_Obsidian_Workbench_Layer.md`
> 
> The one-line doctrine:
> 
> > Cadence is an Obsidian-based working cockpit for Markdown entities; QiAccess remains the front door, QiNexus remains the storage model, Wiki.js remains the readable manual layer, and Supabase/Directus remain the structured data path.
> 
> Bottom line: **yes, this is worth testing. But don’t let her get promoted before probation.**

### User
> Well, the reason I was looking at it because immediately I knew exactly where to click, I knew exactly what to do. It was very intuitive, it was snappy, it was fast. And I was thinking, like, not necessarily to replace anything, I was thinking, hmm, if it's open source, can we fork it? And can we, like, you know, piggyback off of this guy's already designed? Because the design is perfect. It's like literally, like, what I need. At least this is what it felt like at first.

### Assistant
> That instinct is correct. You’re not chasing the product — you’re recognizing a **working interaction pattern** that already solved part of your UX problem. I’m going to separate “forkable design leverage” from “don’t accidentally inherit plugin-shaped limitations.”

### Assistant
> Yes. **That is the correct reason to care about it.**
> 
> Not because “Cadence is another tool.”  
> Because **Cadence proves a UI pattern that your brain instantly understood.**
> 
> That matters.
> 
> ## The real opportunity
> 
> Cadence should become a **UX donor**, not your new architecture.
> 
> Meaning:
> 
> > Fork it, study it, possibly customize it — but do not let it become the spine of QiOS.
> 
> The repo is public, the Obsidian plugin page lists it as **MIT licensed**, and the project itself says it is plain JavaScript with no build step: `main.js`, `manifest.json`, and `styles.css` dropped into an Obsidian plugin folder. That makes it very forkable and very easy to inspect. citeturn556065view0turn556065view1
> 
> ## Why it felt right immediately
> 
> Because it already has the exact interaction model you keep describing:
> 
> | Cadence pattern | Why it clicked for you |
> |---|---|
> | One tab | No scattered plugin hopping |
> | Left rail nav | “I know where to click” |
> | Home / Today / Pipeline / Contacts / Projects / Inbox / Reports | Life/work surfaces grouped like an operating cockpit |
> | Cards + lists + modals | Fast capture without folder spelunking |
> | Plain Markdown + frontmatter | Still scriptable, portable, Obsidian-native |
> | Reminders + quick capture | Reduces the “where did that thought go?” tax |
> 
> Cadence’s own description says its left rail flips between Home, Today, Pipeline, Contacts, Projects, Inbox, and Reports, and that Markdown/frontmatter remains the source of truth. citeturn556065view1
> 
> That is why it felt snappy: it is mostly a local UI lens over files, not some bloated web app asking permission from six APIs before showing you a button.
> 
> ## My ruling
> 
> **Yes: fork it.**
> 
> But fork it under a controlled experiment.
> 
> Not:
> 
> > “We are rebuilding QiLife inside Cadence.”
> 
> Instead:
> 
> > “We are using Cadence as a live UX prototype and local Markdown workbench for QiLife/QiAccess patterns.”
> 
> That distinction matters. Otherwise, congratulations, we invented another hallway in the haunted mansion.
> 
> ## Best path
> 
> ### Track 1 — Fork Cadence as-is
> 
> Make a fork called something like:
> 
> - `obsidian-qicadence`
> - `qiworkbench-obsidian`
> - `qilife-obsidian-workbench`
> 
> Purpose:
> 
> - test the UI
> - rename modules
> - adjust folders
> - map entity types to your world
> - learn how the interaction works
> - keep Obsidian as the runtime
> 
> This is the fastest way to see value.
> 
> ### Track 2 — Extract the design pattern into QiAccess / QiLife
> 
> This is the strategic move.
> 
> Your QiAccess blueprint already says the main goal is **not to build more apps**, but to create one coherent entry point where you can see what exists, know where to go, launch tools, access docs, and reuse the pattern later for Mom’s Care. fileciteturn4file0
> 
> Cadence gives you the **shape**:
> 
> ```text
> Left rail
> → Home
> → Today
> → Inbox
> → Projects
> → People
> → Pipeline / Matters / Care
> → Reports
> ```
> 
> QiAccess gives you the **system boundary**:
> 
> ```text
> Front door
> Launcher
> Access control
> Server tools
> Storage
> Wiki.js
> Roadmap
> Blueprint
> ```
> 
> So we do **not** let Cadence replace QiAccess. We let it influence the UX.
> 
> ## What I would change for your fork
> 
> Cadence default:
> 
> ```text
> Home
> Today
> Pipeline
> Contacts
> Projects
> Inbox
> Reports
> ```
> 
> Qi version:
> 
> ```text
> Home
> Today
> Inbox
> Projects
> People
> Mom’s Care
> Legal
> Finance
> Tech
> Reports
> ```
> 
> Or, even cleaner:
> 
> ```text
> Home
> Today
> Capture
> Work
> People
> Care
> Matters
> Money
> Systems
> Reports
> ```
> 
> That second one is more you. Less corporate SaaS cosplay.
> 
> ## What not to copy blindly
> 
> ### Do not inherit CRM-first thinking
> 
> Cadence has CRM/PRM baked in. Useful, but your current center is **life ops, care, legal, finance, tech, and family**, not sales pipeline. Your blueprint already demotes CRM/client-platform thinking and makes Cody, household/family, Mom’s care, legal/finance, knowledge/files, and tech/server systems the active priority order. fileciteturn4file0
> 
> So in your fork:
> 
> | Cadence term | Qi translation |
> |---|---|
> | Contacts | People |
> | Companies | Organizations |
> | Deals | Opportunities / Matters / Cases |
> | Pipeline | Workstream / Matter Board |
> | Partners | Support Network / Vendors |
> | Activities | Events / Interactions |
> | Projects | Projects |
> | Inbox | Capture |
> 
> ## Legal / license sanity
> 
> Because it is MIT licensed, you can generally fork, modify, reuse, and redistribute the code, including commercially, as long as you preserve the copyright and license notice. The Obsidian plugin page lists Cadence’s license as MIT. citeturn556065view1
> 
> Translation: **yes, you can piggyback. Just don’t be tacky. Attribute the original author, keep the license notice, rename your fork, and don’t pretend you designed the whole thing from scratch.**
> 
> ## The better strategic phrase
> 
> Do not say:
> 
> > “We’re using Cadence.”
> 
> Say:
> 
> > “We’re evaluating Cadence as the reference implementation for the QiLife local-first workbench UI.”
> 
> That keeps your architecture clean.
> 
> ## Decision
> 
> **Fork it. Study it. Use it as the prototype.**
> 
> But the doctrine is:
> 
> > **Cadence is the proof-of-feel. QiAccess/QiLife remains the system.**
> 
> That feeling you had — “I immediately knew what to do” — is not fluff. That is the product signal. Capture it before we bury it under architecture sludge.

### User
> did you looka t the code, its like a couple files and some style, its like just a view. we can total copy this over our own data and vuala,

### Assistant
> You’re right to challenge that. I had looked at the project description/package shape, not done a proper code pass. I’m going to verify the repo structure now so we don’t make architecture decisions off vibes and screenshots.

### Assistant
> You’re **mostly right** — and I’ll correct myself plainly:
> 
> ## No, I had not done a real code pass before.
> 
> I had looked at the repo shape and description. Now I checked the actual files, and yes: **it is basically one big Obsidian view plugin.**
> 
> The repo has the key files you said:
> 
> - `main.js`
> - `manifest.json`
> - `styles.css`
> - `README.md`
> - `LICENSE`
> - screenshots/docs
> 
> GitHub shows `main.js`, `manifest.json`, and `styles.css` directly in the repo file list. citeturn518211view0
> 
> ## You’re right about the architecture
> 
> The top of `main.js` literally describes Cadence as a:
> 
> > “Single unified view with internal tab nav”
> 
> It also says the source of truth is Markdown files, and that it is **plain JS with no build step**, loaded directly by Obsidian. citeturn507332view0
> 
> So yes — this is not some giant SaaS stack. It is closer to:
> 
> ```text
> Obsidian plugin shell
> + nav config
> + entity registry
> + markdown/frontmatter helpers
> + view renderers
> + fallback CSS
> ```
> 
> And the nav structure is just a `NAV_GROUPS` array with grouped items like Home, Planner, Projects, CRM, PRM, Workflow, Reports, Settings. citeturn507332view0
> 
> That means the **first obvious hack** is exactly what you said:
> 
> ```text
> Replace Cadence's entity model
> with QiLife / QiNexus / MomCare / Legal / Finance entities
> and reuse the view shell.
> ```
> 
> ## But here’s the one thing I’m not letting you gloss over
> 
> It is not *only* a view.
> 
> It is a view **plus Obsidian file operations**.
> 
> The `main.js` has an `ENTITIES` registry defining folders, labels, fields, columns, enum options, etc. It also has settings, daily note logic, TaskNotes helpers, folder creation helpers, template creation helpers, and Markdown/frontmatter behavior. citeturn507332view0
> 
> So the correct statement is:
> 
> > **Cadence is a lightweight local app shell over Markdown/frontmatter, not just CSS.**
> 
> Still very forkable. But not “copy three buttons and done.”
> 
> ## The move depends where we want to use it
> 
> ### If we want this inside Obsidian
> 
> Then yes. **Fork it and mutate it.**
> 
> This is the fastest win.
> 
> We rename:
> 
> | Cadence | Qi version |
> |---|---|
> | Contacts | People |
> | Companies | Organizations |
> | Deals/Pipeline | Matters / Workstreams |
> | Projects | Projects |
> | Activities | Events / Interactions |
> | Partners | Support Network / Vendors |
> | Planner | Daily Ops |
> | Reports | Dashboards |
> 
> Then change folders from:
> 
> ```text
> Cadence/Contacts
> Cadence/Projects
> Cadence/Pipeline
> ```
> 
> to something like:
> 
> ```text
> QiLife/People
> QiLife/Projects
> QiLife/Matters
> QiLife/Care
> QiLife/Finance
> QiLife/Legal
> QiLife/Systems
> ```
> 
> That is very realistic.
> 
> ### If we want this inside QiAccess / QiLife web app
> 
> Then no, not copy-paste directly.
> 
> Because Cadence is written as an **Obsidian plugin**, not a normal React/Vite/Next app. It uses Obsidian’s plugin runtime, vault APIs, metadata cache, file manager, and workspace view system.
> 
> So for QiAccess, the smart move is:
> 
> ```text
> Use Cadence as UX reference + logic donor,
> not literal runtime dependency.
> ```
> 
> We can port the shape:
> 
> ```text
> Left rail
> Single tab/workspace
> Cards
> Entity lists
> Kanban surfaces
> Capture modal
> Reports
> Project detail view
> ```
> 
> But the data backend would become:
> 
> ```text
> Supabase / local files / API / Google Drive index
> ```
> 
> instead of Obsidian’s vault API.
> 
> ## My updated ruling
> 
> You were right.
> 
> This is more useful than I first framed it.
> 
> **Cadence is not just a tool to test. Cadence is a scaffold.**
> 
> But the clean strategy is two-track:
> 
> ## Track A — Quick fork for Obsidian
> 
> Use it immediately as:
> 
> ```text
> QiWorkbench for Obsidian
> ```
> 
> Purpose:
> 
> - local Markdown cockpit
> - Mom Care notes
> - legal matters
> - people
> - projects
> - reminders
> - daily ops
> 
> This gives you usable workflow now.
> 
> ## Track B — Port the design to QiAccess/QiLife
> 
> Use Cadence as the design prototype for your actual app:
> 
> ```text
> QiAccess Start / QiLife web app
> ```
> 
> Purpose:
> 
> - same intuitive UI
> - your data model
> - Supabase/Directus later
> - server/web/mobile path
> 
> ## The first thing I’d tell Codex
> 
> Use this framing:
> 
> ```text
> Inspect the Cadence Obsidian plugin architecture and create a QiLife fork plan.
> 
> Goal:
> Use Cadence as a local-first Obsidian workbench scaffold, not as the final QiLife architecture.
> 
> Tasks:
> 1. Clone or fork https://github.com/wesswart77/obsidian-cadence.
> 2. Identify the core config surfaces:
>    - NAV_GROUPS
>    - ENTITIES
>    - DEFAULT_SETTINGS
>    - folder paths
>    - render functions for entity lists, dashboards, kanban, project detail, inbox, and reports.
> 3. Create a mapping from Cadence entities to QiLife entities:
>    - contact -> person
>    - company -> organization
>    - deal -> matter/workstream
>    - project -> project
>    - activity -> interaction/event
>    - partner -> support/vendor
> 4. Rename plugin branding from Cadence to QiWorkbench.
> 5. Change default folders from Cadence/* to QiLife/*.
> 6. Keep MIT license attribution intact.
> 7. Do not add Supabase, server sync, or external APIs yet.
> 8. Produce a short report listing:
>    - files changed
>    - config objects changed
>    - views that are reusable immediately
>    - views that are too CRM-specific
>    - safest next edits
> ```
> 
> ## Bottom line
> 
> Yes, girl.
> 
> This is absolutely a **“copy the pattern over our data and voilà”** situation — **inside Obsidian first**.
> 
> For the web app, it is more like:
> 
> > “copy the product logic and interaction model, then rebuild the runtime cleanly.”
> 
> Still huge leverage. This is not a distraction. This is a valid shortcut.

### User
> could we use this map and essentially use the same field names and links and such and create that into our database, or keep using the markdown and it syncs with obsidian, that means we ahve durable postgres and pack your data and go aon blob storage. or what ever you just said.

### Assistant
> Yes — this is the architecture fork in the road. The smart answer is probably **both**, but with one clear authority layer so we don’t create a sync monster.

### Assistant
> Yes. **This is the right architecture.**
> 
> Not “Cadence replaces our system.”  
> More like:
> 
> > **Cadence gives us the entity map + UI pattern. We turn that into a QiLife data contract that can live in both Markdown and Postgres.**
> 
> That gives you the holy combo:
> 
> ```text
> Obsidian Markdown = human-readable, portable, editable
> Postgres / Supabase = durable structured database
> Blob storage / Drive = files, evidence, docs, attachments
> QiAccess / QiLife UI = clean front door over the same data
> ```
> 
> And yes — that means **pack your data and go**. No hostage app. No Notion prison. No “export coming soon” clown show.
> 
> ---
> 
> # The clean model
> 
> ## Use Cadence-style fields as the “frontmatter contract”
> 
> Each note/entity has predictable fields:
> 
> ```yaml
> id: person_01J...
> type: person
> name: Jane Smith
> status: active
> tags:
>   - caregiver
>   - family
> related_projects:
>   - "[[Mom Care Plan]]"
> related_matters:
>   - "[[Humana Claim]]"
> created_at: 2026-06-16
> updated_at: 2026-06-16
> source: obsidian
> ```
> 
> That same structure maps to Postgres:
> 
> ```text
> people
> projects
> matters
> organizations
> interactions
> tasks
> reminders
> files
> relationships
> ```
> 
> So the Markdown is not random notes anymore. It becomes **portable database-shaped Markdown**.
> 
> ---
> 
> # The answer: use both
> 
> ## Best architecture
> 
> | Layer | Job |
> |---|---|
> | Markdown files | Human-readable source, Obsidian editing, portable notes |
> | YAML frontmatter | Structured metadata |
> | Markdown body | Narrative, notes, context, H2 sections |
> | Postgres/Supabase | Durable queryable database |
> | Blob storage / Drive | PDFs, images, evidence, exports, attachments |
> | Sync/indexer | Keeps Markdown and Postgres aligned |
> | QiAccess/QiLife | The app UI over the data |
> 
> Your own blueprint already says Google Drive / QiNexus is the storage backbone, and that canonical truth can live in app source code, repo docs, database records when used, Google Drive source files, and designated Wiki.js operating pages. fileciteturn6file0
> 
> So this fits. It does **not** fight the doctrine.
> 
> ---
> 
> # The critical rule
> 
> Do **not** make both Markdown and Postgres equally authoritative.
> 
> That creates a sync demon.
> 
> The sane path is:
> 
> ## Phase 1: Markdown is the writable source
> 
> Obsidian/Cadence-style Markdown is where you edit.
> 
> Postgres is a **mirror/index**.
> 
> ```text
> Obsidian Markdown
> → sync parser
> → Postgres tables
> → QiAccess/QiLife views
> ```
> 
> This is safest because you can start immediately.
> 
> ## Phase 2: Postgres becomes structured authority for some domains
> 
> Later, for things like meds, transactions, care logs, legal evidence, or finance records, Postgres becomes the source.
> 
> Markdown becomes a readable/generated view.
> 
> ```text
> Postgres
> → markdown exporter
> → Obsidian-readable notes
> ```
> 
> That’s not for day one. Don’t overbuild. But yes, that is where this can go.
> 
> ---
> 
> # The actual system shape
> 
> ## 1. Markdown file
> 
> Example:
> 
> ```text
> QiLife/People/Jane_Smith.md
> ```
> 
> ```yaml
> ---
> id: person_01JABC
> type: person
> name: Jane Smith
> role: nurse
> status: active
> phone: ""
> email: ""
> tags:
>   - mom-care
>   - medical
> projects:
>   - "[[Mom Care Plan]]"
> matters: []
> created_at: 2026-06-16
> updated_at: 2026-06-16
> ---
> ```
> 
> ```markdown
> ## Summary
> 
> Jane is one of Mom's care contacts.
> 
> ## Notes
> 
> ## Follow Ups
> 
> ## Related Files
> ```
> 
> ## 2. Postgres row
> 
> ```text
> people
> - id
> - display_name
> - role
> - status
> - phone
> - email
> - tags
> - md_path
> - created_at
> - updated_at
> ```
> 
> ## 3. Relationship table
> 
> ```text
> entity_relationships
> - id
> - from_entity_id
> - from_entity_type
> - to_entity_id
> - to_entity_type
> - relationship_type
> - source
> ```
> 
> Example:
> 
> ```text
> Jane Smith → supports → Mom Care Plan
> Humana Claim → relates_to → Mom Care Plan
> Doctor Visit → involves → Jane Smith
> ```
> 
> ## 4. Blob/file table
> 
> ```text
> files
> - id
> - title
> - file_type
> - storage_provider
> - storage_path
> - drive_file_id
> - related_entity_id
> - related_entity_type
> - checksum
> - created_at
> ```
> 
> So the PDF lives in Drive / blob storage, but the database knows it exists.
> 
> ---
> 
> # What to copy from Cadence
> 
> Copy the **conceptual map**, not every field blindly.
> 
> ## Good Cadence patterns to steal
> 
> | Pattern | Use it? | Why |
> |---|---:|---|
> | Entity registry | Yes | Perfect for QiLife types |
> | Folder-per-entity-type | Yes | Obsidian-friendly |
> | YAML frontmatter | Yes | Portable metadata |
> | Markdown H2 sections | Yes | Human-readable body |
> | Linked entities | Yes | Core to your life system |
> | Dashboards | Yes | Great UI pattern |
> | Kanban grouping | Yes | Useful for matters/projects |
> | CSV import | Hell yes | Data migration shortcut |
> | CRM/PRM labels | Rename | Too business-coded |
> 
> ---
> 
> # QiLife entity map
> 
> I’d define your entities like this:
> 
> | Qi Entity | Markdown folder | Postgres table |
> |---|---|---|
> | Person | `QiLife/People/` | `people` |
> | Organization | `QiLife/Organizations/` | `organizations` |
> | Project | `QiLife/Projects/` | `projects` |
> | Matter | `QiLife/Matters/` | `matters` |
> | Care Item | `QiLife/Care/` | `care_items` |
> | Interaction | `QiLife/Interactions/` | `interactions` |
> | Task | `QiLife/Tasks/` | `tasks` |
> | Reminder | `QiLife/Reminders/` | `reminders` |
> | File Record | `QiLife/Files/` | `file_records` |
> | Account | `QiLife/Accounts/` | `accounts` |
> | Transaction | `QiLife/Finance/Transactions/` | `transactions` |
> 
> Cadence’s `Contacts`, `Projects`, `Pipeline`, `Activities`, and `Reports` become your:
> 
> ```text
> People
> Projects
> Matters
> Interactions
> Reports
> ```
> 
> That’s the move.
> 
> ---
> 
> # The piece that makes it durable
> 
> Every entity needs a stable ID.
> 
> Do **not** rely only on file path or note title.
> 
> Bad:
> 
> ```yaml
> name: Mom Care Plan
> ```
> 
> Good:
> 
> ```yaml
> id: project_01JABCXYZ
> type: project
> title: Mom Care Plan
> ```
> 
> Why?
> 
> Because names change. Paths change. Folders get reorganized. Your database cannot freak out every time you rename a note like a dramatic intern.
> 
> Stable IDs make this portable.
> 
> ---
> 
> # The sync rule
> 
> Each Markdown file should have:
> 
> ```yaml
> id:
> type:
> title/name:
> status:
> created_at:
> updated_at:
> sync_status:
> postgres_id:
> content_hash:
> ```
> 
> The sync tool compares:
> 
> ```text
> file modified time
> frontmatter updated_at
> content_hash
> postgres updated_at
> ```
> 
> Then decides:
> 
> ```text
> new file → insert database row
> changed file → update database row
> deleted file → mark archived, do not hard delete
> database-only record → optionally generate Markdown file
> ```
> 
> ---
> 
> # The best first version
> 
> Do **not** build the full sync engine first.
> 
> First version should be dumb and safe:
> 
> ```text
> Markdown → Postgres only
> ```
> 
> One-way import.
> 
> That gives you:
> 
> - Obsidian still works
> - Cadence-style UI still works
> - Supabase gets populated
> - Directus can see/edit structured records
> - QiAccess can read data
> - no scary two-way conflict handling yet
> 
> Then later:
> 
> ```text
> Postgres → Markdown export
> ```
> 
> Then much later:
> 
> ```text
> two-way sync with conflict rules
> ```
> 
> Do not start with two-way sync unless you want to summon a demon wearing a YAML wig.
> 
> ---
> 
> # My recommendation
> 
> ## Adopt this architecture:
> 
> > **QiLife uses Markdown-frontmatter entities as the portable human layer, Postgres as the durable structured layer, and blob/Drive storage as the file layer. Cadence’s entity map and UI become the prototype for the Markdown workbench.**
> 
> That is coherent.
> 
> That is powerful.
> 
> That is not overcomplicated if we phase it correctly.
> 
> ---
> 
> # Immediate next step
> 
> Tell Codex this:
> 
> ```text
> We are evaluating Cadence as a reference implementation for QiLife’s Markdown entity workbench.
> 
> Goal:
> Create a QiLife entity contract that can exist as both:
> 1. Obsidian Markdown files with YAML frontmatter
> 2. Supabase/Postgres tables with stable IDs and relationships
> 
> Do not build two-way sync yet.
> 
> Tasks:
> 1. Inspect Cadence’s entity registry, folder model, frontmatter fields, and relationship/link behavior.
> 2. Create docs/architecture/qilife_markdown_postgres_model.md.
> 3. Define QiLife entity types:
>    - person
>    - organization
>    - project
>    - matter
>    - care_item
>    - interaction
>    - task
>    - reminder
>    - file_record
>    - account
>    - transaction
> 4. For each entity, define:
>    - Markdown folder path
>    - required frontmatter fields
>    - optional frontmatter fields
>    - matching Postgres table name
>    - relationship fields
> 5. Require stable IDs for every entity.
> 6. Design a one-way sync path:
>    Markdown frontmatter/body → parser → Postgres mirror tables.
> 7. Keep Google Drive / QiNexus as the file/blob storage layer.
> 8. Do not replace QiAccess Start.
> 9. Do not make Postgres and Markdown both authoritative yet.
> 10. Produce an ADR recommending Markdown-first with Postgres mirror for v1.
> ```
> 
> Bottom line:
> 
> **Yes. This is the bridge.**
> 
> Cadence gives us the pattern.  
> Obsidian gives us portable Markdown.  
> Postgres gives us durable structure.  
> Drive/blob storage gives us files.  
> QiAccess/QiLife gives us the front door.
> 
> That is the actual stack.

### User
> ok so since codex already has access to qilife i just donwloaded the code into a folder at root of qilife so codex can see it.

### Assistant
> Perfect. Now don’t let Codex “blend” it into QiLife like spaghetti. Treat the Cadence folder as a **reference/vendor source**, inspect it, then deliberately extract the map, UI shell, and fields.

### Assistant
> Perfect. That is exactly the right move.
> 
> Now give Codex a **controlled assignment**: inspect Cadence, extract the reusable pattern, and **do not mutate QiLife yet** unless it creates docs or an isolated prototype branch. Your blueprint already says QiAccess/QiLife should stay focused on one coherent entry point, not random app sprawl, and it also preserves “metadata before automation,” “local-first where appropriate,” and “human-readable naming with machine-stable identity.” fileciteturn7file0
> 
> Here’s the copy/paste prompt:
> 
> :::writing{variant="standard" id="58241"}
> You are working inside the QiLife repository.
> 
> Context:
> I downloaded the Cadence Obsidian plugin source into a folder at the root of QiLife so you can inspect it. Treat Cadence as a reference/vendor source, not as QiLife source code yet.
> 
> Goal:
> Analyze Cadence as a possible UI/data-pattern donor for QiLife. We want to learn from its left-rail workspace, entity registry, Markdown/frontmatter model, dashboards, project surfaces, capture modal, reminders, kanban/list views, and styling.
> 
> Hard rules:
> 1. Do not merge Cadence code directly into the QiLife app yet.
> 2. Do not rename QiLife architecture around Cadence.
> 3. Do not add Supabase sync yet.
> 4. Do not build two-way sync.
> 5. Preserve existing QiLife routes, working app behavior, and docs.
> 6. Keep Cadence attribution/license intact if any code is copied later.
> 7. If making changes, keep them isolated to docs, analysis files, or a clearly named prototype folder.
> 
> Tasks:
> 1. Locate the downloaded Cadence folder at the QiLife root.
> 2. Inspect its main files, especially:
>    - main.js
>    - styles.css
>    - manifest.json
>    - README.md
>    - LICENSE
> 3. Identify the main config/architecture objects:
>    - nav groups
>    - entity registry
>    - entity folders
>    - frontmatter fields
>    - dashboard/report logic
>    - project detail logic
>    - capture/reminder logic
>    - markdown parsing/writing helpers
>    - Obsidian-specific APIs
> 4. Create this document:
>    docs/architecture/cadence_reference_analysis.md
> 
> Include:
> - What Cadence does well
> - What parts are reusable as-is
> - What parts are Obsidian-specific and cannot be directly used in QiLife web app
> - What UI patterns should be copied
> - What data patterns should be copied
> - What field names/entities map cleanly to QiLife
> - What should be renamed for QiLife
> - What should be avoided
> 
> 5. Create this document:
>    docs/architecture/qilife_markdown_entity_contract.md
> 
> Define a proposed QiLife Markdown/frontmatter contract for:
> - person
> - organization
> - project
> - matter
> - care_item
> - interaction
> - task
> - reminder
> - file_record
> - account
> - transaction
> 
> For each entity define:
> - markdown folder path
> - required frontmatter fields
> - optional frontmatter fields
> - relationship fields
> - matching future Postgres table name
> - notes about Obsidian compatibility
> 
> 6. Create this ADR:
>    docs/decisions/ADR-00XX_cadence_as_qilife_workbench_reference.md
> 
> Decision:
> Cadence is used as a reference implementation and possible Obsidian workbench scaffold for QiLife, not as the master architecture.
> 
> Include:
> - status: proposed
> - context
> - decision
> - consequences
> - why not replacing QiLife/QiAccess
> - why Markdown/frontmatter remains useful
> - why Postgres/Supabase should be treated as a later durable mirror, not day-one authority
> 
> 7. Optional prototype only if low-risk:
> Create an isolated prototype folder:
>    prototypes/cadence_qilife_mapping/
> 
> Inside it, create:
> - entityMap.ts or entityMap.json
> - navMap.ts or navMap.json
> - README.md
> 
> Do not wire it into production routes yet.
> 
> Deliverables:
> - docs/architecture/cadence_reference_analysis.md
> - docs/architecture/qilife_markdown_entity_contract.md
> - docs/decisions/ADR-00XX_cadence_as_qilife_workbench_reference.md
> - optional prototypes/cadence_qilife_mapping/
> 
> After completing, summarize:
> - files created
> - key findings
> - recommended next step
> - any risks or code areas that should not be touched yet
> :::
> 
> ## Folder hygiene
> 
> If you dropped it directly like:
> 
> ```text
> QiLife/obsidian-cadence/
> ```
> 
> That’s okay for now.
> 
> But I’d eventually move/reference it as:
> 
> ```text
> QiLife/vendor/obsidian-cadence/
> ```
> 
> or:
> 
> ```text
> QiLife/reference/obsidian-cadence/
> ```
> 
> My preference:
> 
> ```text
> QiLife/reference/obsidian-cadence/
> ```
> 
> Because **vendor** implies dependency. **Reference** says “look, learn, borrow carefully.”
> 
> ## What we are doing right now
> 
> We are not building the final database yet.
> 
> We are extracting:
> 
> ```text
> Cadence UI pattern
> + Cadence frontmatter/entity model
> + QiLife entity names
> + future Postgres table alignment
> = QiLife data contract
> ```
> 
> That is the leverage move. Not vibes. Not chaos. Actual usable architecture.

### User
> lets tell it to do a branch inside the same repo this way we have v1 front and back, apha cadence etc.

### Assistant
> Yes. **Correct move.**
> 
> But tiny correction: don’t make a “branch inside the repo” as a folder. Make an actual **Git branch** in the same QiLife repo.
> 
> Use this structure:
> 
> | Branch | Purpose |
> |---|---|
> | `main` | current stable QiLife v1 front/back |
> | `alpha/cadence-workbench` | Cadence experiment branch |
> | later: `prototype/qilife-markdown-sync` | Markdown/Postgres sync experiment |
> | later: `feature/qilife-entity-contract` | production-ready data contract |
> 
> Give Codex this:
> 
> :::writing{variant="standard" id="48392"}
> We are going to create a Git branch inside the existing QiLife repo for the Cadence experiment.
> 
> Goal:
> Keep current QiLife v1 front/back stable on main, and create an isolated alpha branch where we inspect and adapt Cadence patterns without contaminating production code.
> 
> Branch name:
> alpha/cadence-workbench
> 
> Instructions:
> 1. Check current Git status.
> 2. If there are uncommitted changes, show them and do not discard anything.
> 3. Create and switch to a new branch:
> 
> git checkout -b alpha/cadence-workbench
> 
> 4. Confirm the branch:
> 
> git branch --show-current
> 
> 5. Treat the downloaded Cadence folder at the QiLife repo root as reference source.
> 6. Move it only if safe into:
> 
> reference/obsidian-cadence/
> 
> If moving it would break anything or cause confusion, leave it where it is and document its current path.
> 
> 7. Do not merge Cadence into the production QiLife app yet.
> 8. Do not alter main branch.
> 9. Do not add Supabase sync yet.
> 10. Do not build two-way sync.
> 11. Do not replace QiLife architecture with Cadence architecture.
> 
> Work to complete on this branch:
> 1. Analyze Cadence’s structure:
>    - main.js
>    - styles.css
>    - manifest.json
>    - README.md
>    - LICENSE
> 
> 2. Create:
> 
> docs/architecture/cadence_reference_analysis.md
> 
> Include:
> - repo/file structure
> - core nav model
> - entity registry model
> - Markdown/frontmatter behavior
> - UI surfaces worth copying
> - Obsidian-specific code that cannot be reused directly in QiLife web app
> - styling patterns worth borrowing
> - risk areas
> 
> 3. Create:
> 
> docs/architecture/qilife_markdown_entity_contract.md
> 
> Define QiLife Markdown/frontmatter entities:
> - person
> - organization
> - project
> - matter
> - care_item
> - interaction
> - task
> - reminder
> - file_record
> - account
> - transaction
> 
> For each define:
> - folder path
> - required frontmatter fields
> - optional fields
> - relationship fields
> - future Postgres table name
> - Obsidian compatibility notes
> 
> 4. Create:
> 
> docs/decisions/ADR-00XX_cadence_as_qilife_workbench_reference.md
> 
> Decision:
> Cadence is being used as a reference implementation and possible Obsidian workbench scaffold for QiLife, not as the master architecture.
> 
> Include:
> - status: proposed
> - context
> - decision
> - consequences
> - why QiLife/QiAccess are not being replaced
> - why Markdown/frontmatter is useful
> - why Postgres/Supabase should come later as a durable mirror/index, not immediate two-way authority
> 
> 5. Optional isolated prototype only:
> Create:
> 
> prototypes/cadence_qilife_mapping/
> 
> Inside it create:
> - README.md
> - entityMap.json
> - navMap.json
> 
> This prototype should map Cadence concepts to QiLife concepts without wiring anything into production routes.
> 
> Expected branch outcome:
> This branch should contain analysis, ADRs, entity contracts, and maybe an isolated prototype map. It should not change production QiLife behavior yet.
> 
> After finishing, report:
> - current branch name
> - files created
> - files moved
> - whether Cadence was moved to reference/obsidian-cadence/
> - key findings
> - recommended next branch/action
> :::
> 
> ## The branch doctrine
> 
> This is the right split:
> 
> ```text
> main
> = QiLife v1 stable front/back
> 
> alpha/cadence-workbench
> = inspect, map, prototype, steal the good parts
> 
> feature/qilife-workbench-ui
> = later production implementation
> 
> feature/qilife-markdown-postgres-sync
> = later data sync
> ```
> 
> Do **not** let Codex start rewriting the app yet. First branch is reconnaissance + contract. Then we build from that.

### User
> im out of credits for codex, already for the next 3 days, what should we do, what if we try the agent, or even gemini can do it and we can reimport to the server later.

### Assistant
> Yes. **Don’t freeze for 3 days. Codex being out of credits just means we change lanes.**
> 
> The move is:
> 
> > **Use Gemini / local agent for reconnaissance + docs + isolated prototype maps. Do not let it rewrite QiLife production code.**
> 
> That work is mostly reading, mapping, documenting, and making JSON contracts. Perfect for Gemini or another agent.
> 
> ## Best path right now
> 
> ### Use Gemini or your IDE agent for:
> 
> - Cadence code inspection
> - entity map extraction
> - frontmatter field mapping
> - QiLife entity contract
> - ADR draft
> - isolated prototype folder
> - Markdown docs
> 
> ### Do **not** use Gemini/agent yet for:
> 
> - rewriting QiLife routes
> - wiring Supabase
> - two-way sync
> - changing production app behavior
> - moving architecture around like a raccoon in a pantry
> 
> That is how we keep it useful instead of cursed.
> 
> ---
> 
> # Local branch first
> 
> Run this yourself in the QiLife repo:
> 
> ```powershell
> cd C:\QiLabs\60_QiApp_QiLife
> git status
> git checkout -b alpha/cadence-workbench
> git branch --show-current
> ```
> 
> If your actual QiLife path is different, adjust the `cd`.
> 
> Then optionally move Cadence into reference:
> 
> ```powershell
> mkdir reference
> Move-Item .\obsidian-cadence .\reference\obsidian-cadence
> ```
> 
> Only do that if the folder is actually named `obsidian-cadence`.
> 
> ---
> 
> # What to use while Codex is blocked
> 
> ## Ranked options
> 
> | Option | Use for | Risk | My call |
> |---|---|---:|---|
> | Gemini | reading/mapping docs | Low | Use it now |
> | IDE agent | small repo changes | Medium | Use carefully |
> | ChatGPT here | architecture/prompt/doc shaping | Low | Use for control |
> | Manual edits | branch setup/docs | Low | Good enough |
> | Wait for Codex | deeper app wiring | Low | Save for later |
> 
> ## Recommendation
> 
> Use **Gemini/agent for the branch work**, then when Codex credits return, have Codex review the branch and clean it up.
> 
> That gives us momentum without letting a different model go feral.
> 
> ---
> 
> # Give Gemini / agent this prompt
> 
> Use this exactly:
> 
> ```text
> You are working inside the QiLife repository on branch alpha/cadence-workbench.
> 
> Context:
> Codex is temporarily unavailable, so your job is to perform a safe analysis and prototype pass only.
> 
> There is a downloaded copy of the Cadence Obsidian plugin somewhere near the root of this repo, possibly in:
> - obsidian-cadence/
> - cadence/
> - reference/obsidian-cadence/
> 
> Cadence is being evaluated as a UI/data-pattern donor for QiLife.
> 
> Hard rules:
> 1. Do not modify production QiLife routes.
> 2. Do not rewrite the app.
> 3. Do not wire Cadence into the app.
> 4. Do not add Supabase sync.
> 5. Do not build two-way sync.
> 6. Do not delete existing files.
> 7. Keep all changes isolated to docs/architecture, docs/decisions, and prototypes/cadence_qilife_mapping.
> 8. Preserve MIT license attribution if copying any code or excerpts.
> 
> Your tasks:
> 
> 1. Find the Cadence source folder.
> 
> 2. Inspect:
> - main.js
> - styles.css
> - manifest.json
> - README.md
> - LICENSE
> 
> 3. Create:
> docs/architecture/cadence_reference_analysis.md
> 
> Include:
> - Cadence file structure
> - what main.js does
> - nav model
> - entity registry model
> - Markdown/frontmatter behavior
> - capture/reminder behavior
> - dashboard/list/kanban/project-detail patterns
> - Obsidian-specific APIs that cannot be reused directly in QiLife web app
> - styling/layout patterns worth copying
> - risk areas
> 
> 4. Create:
> docs/architecture/qilife_markdown_entity_contract.md
> 
> Define QiLife Markdown/frontmatter contracts for:
> - person
> - organization
> - project
> - matter
> - care_item
> - interaction
> - task
> - reminder
> - file_record
> - account
> - transaction
> 
> For each entity include:
> - markdown folder path
> - required frontmatter fields
> - optional frontmatter fields
> - relationship fields
> - future Postgres table name
> - Obsidian compatibility notes
> 
> Important:
> Every entity must have:
> - id
> - type
> - title or name
> - status
> - created_at
> - updated_at
> - source
> - tags
> 
> Stable IDs are required. Do not rely only on filenames.
> 
> 5. Create:
> docs/decisions/ADR-00XX_cadence_as_qilife_workbench_reference.md
> 
> Decision:
> Cadence is a reference implementation and possible Obsidian workbench scaffold for QiLife. It is not replacing QiLife, QiAccess, Supabase, Directus, Wiki.js, or the main architecture.
> 
> Include:
> - status: proposed
> - context
> - decision
> - consequences
> - what we are adopting
> - what we are not adopting
> - why Markdown/frontmatter matters
> - why Postgres should come later as a durable mirror/index
> - why two-way sync is deferred
> 
> 6. Create optional isolated prototype:
> prototypes/cadence_qilife_mapping/
> 
> Inside it create:
> - README.md
> - entityMap.json
> - navMap.json
> 
> The prototype should map Cadence concepts to QiLife concepts.
> 
> Cadence to QiLife mapping:
> - Contacts -> People
> - Companies -> Organizations
> - Deals/Pipeline -> Matters or Workstreams
> - Projects -> Projects
> - Activities -> Interactions
> - Partners -> Support Network / Vendors
> - Inbox -> Capture
> - Reports -> Dashboards
> - Planner -> Daily Ops
> 
> 7. After finishing, provide a summary:
> - branch name
> - files created
> - files changed
> - Cadence folder path found
> - key findings
> - recommended next step
> - risks
> ```
> 
> ---
> 
> # After Gemini/agent finishes
> 
> Run:
> 
> ```powershell
> git status
> git diff --stat
> git add docs prototypes reference
> git commit -m "analyze cadence as qilife workbench reference"
> ```
> 
> Then push the branch:
> 
> ```powershell
> git push -u origin alpha/cadence-workbench
> ```
> 
> Later, on the server:
> 
> ```bash
> cd /path/to/qilife
> git fetch origin
> git checkout alpha/cadence-workbench
> ```
> 
> Or don’t deploy it yet. Since this branch should be docs/prototype only, there may be nothing to run.
> 
> ---
> 
> # The better workflow while Codex is down
> 
> For the next 3 days, use Gemini/agent only for **low-risk branch work**:
> 
> ## Today
> 
> Create:
> 
> ```text
> docs/architecture/cadence_reference_analysis.md
> docs/architecture/qilife_markdown_entity_contract.md
> docs/decisions/ADR-00XX_cadence_as_qilife_workbench_reference.md
> prototypes/cadence_qilife_mapping/
> ```
> 
> ## Tomorrow
> 
> Have Gemini create:
> 
> ```text
> docs/architecture/qilife_postgres_mirror_model.md
> docs/architecture/qilife_markdown_sync_phases.md
> ```
> 
> ## Later, when Codex returns
> 
> Codex reviews the branch, normalizes docs, and decides whether to port anything into the actual app.
> 
> ---
> 
> # Strategic ruling
> 
> Use Gemini. Use the agent. **But make them operate in a sandboxed branch.**
> 
> No production rewrite.  
> No sync engine.  
> No architecture coup.  
> No “vuala” becoming “why is my app dead?”
> 
> We are extracting the gold first. Then Codex can do the surgery later.

### User
> ok so now antigravity the ide agent now has full access to supabase too to start building the tables and migrating data over, here is the out put from teh first command. PS C:\QiLabs\60_QiApps\52_QiApp_QiLife> git status
> On branch alpha/qicadence
> Changes not staged for commit:
>   (use "git add/rm <file>..." to update what will be committed)
>   (use "git restore <file>..." to discard changes in working directory)
>         deleted:    QiCadence/.github/workflows/attest.yml
>         deleted:    QiCadence/.gitignore
>         deleted:    QiCadence/.vscode/settings.json
>         deleted:    QiCadence/LICENSE
>         deleted:    QiCadence/README.md
>         deleted:    QiCadence/SUBMISSION.md
>         deleted:    QiCadence/docs/screenshots/01-home.png
>         deleted:    QiCadence/docs/screenshots/02-inbox.png
>         deleted:    QiCadence/docs/screenshots/03-pipeline.png
>         deleted:    QiCadence/docs/screenshots/04-project.png
>         deleted:    QiCadence/docs/screenshots/05-capture.png
>         deleted:    QiCadence/docs/screenshots/06-new-deal.png
>         deleted:    QiCadence/docs/screenshots/07-import.png
>         deleted:    QiCadence/main.js
>         deleted:    QiCadence/manifest.json
>         deleted:    QiCadence/styles.css
>         deleted:    QiCadence/versions.json
>         modified:   vizvibe.mmd
> 
> Untracked files:
>   (use "git add <file>..." to include in what will be committed)
>         docs/
>         prototypes/
>         reference/
> 
> no changes added to commit (use "git add" and/or "git commit -a")
> PS C:\QiLabs\60_QiApps\52_QiApp_QiLife> git diff --stat
> warning: in the working copy of 'vizvibe.mmd', LF will be replaced by CRLF the next time Git touches it
>  QiCadence/.github/workflows/attest.yml     |    32 -
>  QiCadence/.gitignore                       |     8 -
> :...skipping...
> warning: in the working copy of 'vizvibe.mmd', LF will be replaced by CRLF the next time Git touches it
>  QiCadence/.github/workflows/attest.yml     |    32 -
>  QiCadence/.gitignore                       |     8 -
>  QiCadence/.vscode/settings.json            |     3 -
>  QiCadence/LICENSE                          |    21 -
>  QiCadence/README.md                        |   252 -
>  QiCadence/SUBMISSION.md                    |   160 -
>  QiCadence/docs/screenshots/01-home.png:...skipping...
> warning: in the working copy of 'vizvibe.mmd', LF will be replaced by CRLF the next time Git touches it
>  QiCadence/.github/workflows/attest.yml     |    32 -
>  QiCadence/.gitignore                       |     8 -
>  QiCadence/.vscode/settings.json            |     3 -
>  QiCadence/LICENSE                          |    21 -
>  QiCadence/README.md                        |   252 -
>  QiCadence/SUBMISSION.md                    |   160 -
>  QiCadence/docs/screenshots/01-home.png     |   Bin 1218299 -> 0 bytes
> :...skipping...
> warning: in the working copy of 'vizvibe.mmd', LF will be replaced by CRLF the next time Git touches it
>  QiCadence/.github/workflows/attest.yml     |    32 -
>  QiCadence/.gitignore                       |     8 -
>  QiCadence/.vscode/settings.json            |     3 -
>  QiCadence/LICENSE                          |    21 -
>  QiCadence/README.md                        |   252 -
>  QiCadence/SUBMISSION.md                    |   160 -
>  QiCadence/docs/screenshots/01-home.png     |   Bin 1218299 -> 0 bytes
>  QiCadence/docs/screenshots/02-inbox.pn            :
> warning: in the working copy of 'vizvibe.mmd', LF will be replaced by CRLF the next time Git touches it
>  QiCadence/.github/workflows/attest.yml     |    32 -
>  QiCadence/.gitignore                       |     8 -
>  QiCadence/.vscode/settings.json            |     3 -
>  QiCadence/LICENSE                          |    21 -
>  QiCadence/README.md                        |   252 -
>  QiCadence/SUBMISSION.md                    |   160 -
>  QiCadence/docs/screenshots/01-home.png     |   Bin 1218299 -> 0 bytes
>  QiCadence/docs/screenshots/02-inbox.png    |   Bin   :
> warning: in the working copy of 'vizvibe.mmd', LF will be replaced by CRLF the next time Git touches it
>  QiCadence/.github/workflows/attest.yml     |    32 -
>  QiCadence/.gitignore                       |     8 -
>  QiCadence/.vscode/settings.json            |     3 -
>  QiCadence/LICENSE                          |    21 -
>  QiCadence/README.md                        |   252 -
>  QiCadence/SUBMISSION.md                    |   160 -
>  QiCadence/docs/screenshots/01-home.png     |   Bin 1218299 -> 0 bytes
>  QiCadence/docs/screenshots/02-inbox.png    |   Bin 1218293 -> 0 bytes
> :
> warning: in the working copy of 'vizvibe.mmd', LF will be replaced by CRLF the next time Git touches it
>  QiCadence/.github/workflows/attest.yml     |    32 -
>  QiCadence/.gitignore                       |     8 -
>  QiCadence/.vscode/settings.json            |     3 -
>  QiCadence/LICENSE                          |    21 -
>  QiCadence/README.md                        |   252 -
>  QiCadence/SUBMISSION.md                    |   160 -
>  QiCadence/docs/screenshots/01-home.png     |   Bin 1218299 -> 0 bytes
>  QiCadence/docs/screenshots/02-inbox.png    |   Bin 1218293 -> 0 bytes
>  QiCadence/docs/screenshots/03-pipeline.png |   Bin 1218293 -> 0 bytes
>  QiCadence/docs/screenshots/04-project.png  |   Bin 1018413 -> 0 bytes
>  QiCadence/docs/screenshots/05-capture.png  |   Bin 1223072 -> 0 bytes
> :
> warning: in the working copy of 'vizvibe.mmd', LF will be replaced by CRLF the next time Git touches it
>  QiCadence/.github/workflows/attest.yml     |    32 -
>  QiCadence/.gitignore                       |     8 -
>  QiCadence/.vscode/settings.json            |     3 -
>  QiCadence/LICENSE                          |    21 -
>  QiCadence/README.md                        |   252 -
>  QiCadence/SUBMISSION.md                    |   160 -
>  QiCadence/docs/screenshots/01-home.png     |   Bin 1218299 -> 0 bytes
>  QiCadence/docs/screenshots/02-inbox.png    |   Bin 1218293 -> 0 bytes
>  QiCadence/docs/screenshots/03-pipeline.png |   Bin 1218293 -> 0 bytes
>  QiCadence/docs/screenshots/04-project.png  |   Bin 1018413 -> 0 bytes
>  QiCadence/docs/screenshots/05-capture.png  |   Bin 1223072 -> 0 bytes
> :
> warning: in the working copy of 'vizvibe.mmd', LF will be replaced by CRLF the next time Git touches it
>  QiCadence/.github/workflows/attest.yml     |    32 -
>  QiCadence/.gitignore                       |     8 -
>  QiCadence/.vscode/settings.json            |     3 -
>  QiCadence/LICENSE                          |    21 -
>  QiCadence/README.md                        |   252 -
>  QiCadence/SUBMISSION.md                    |   160 -
>  QiCadence/docs/screenshots/01-home.png     |   Bin 1218299 -> 0 bytes
>  QiCadence/docs/screenshots/02-inbox.png    |   Bin 1218293 -> 0 bytes
>  QiCadence/docs/screenshots/03-pipeline.png |   Bin 1218293 -> 0 bytes
>  QiCadence/docs/screenshots/04-project.png  |   Bin 1018413 -> 0 bytes
>  QiCadence/docs/screenshots/05-capture.png  |   Bin 1223072 -> 0 bytes
> :
> warning: in the working copy of 'vizvibe.mmd', LF will be replaced by CRLF the next time Git touches it
>  QiCadence/.github/workflows/attest.yml     |    32 -
>  QiCadence/.gitignore                       |     8 -
>  QiCadence/.vscode/settings.json            |     3 -
>  QiCadence/LICENSE                          |    21 -
>  QiCadence/README.md                        |   252 -
>  QiCadence/SUBMISSION.md                    |   160 -
>  QiCadence/docs/screenshots/01-home.png     |   Bin 1218299 -> 0 bytes
>  QiCadence/docs/screenshots/02-inbox.png    |   Bin 1218293 -> 0 bytes
>  QiCadence/docs/screenshots/03-pipeline.png |   Bin 1218293 -> 0 bytes
>  QiCadence/docs/screenshots/04-project.png  |   Bin 1018413 -> 0 bytes
>  QiCadence/docs/screenshots/05-capture.png  |   Bin 1223072 -> 0 bytes
>  QiCadence/docs/screenshots/06-new-deal.png |   Bin 1037313 -> 0 bytes
>  QiCadence/docs/screenshots/07-import.png   |   Bin 1024570 -> 0 bytes
>  QiCadence/main.js                          | 12122 ---------------------------
>  QiCadence/manifest.json                    |    11 -
> :
> warning: in the working copy of 'vizvibe.mmd', LF will be replaced by CRLF the next time Git touches it
>  QiCadence/.github/workflows/attest.yml     |    32 -
>  QiCadence/.gitignore                       |     8 -
>  QiCadence/.vscode/settings.json            |     3 -
>  QiCadence/LICENSE                          |    21 -
>  QiCadence/README.md                        |   252 -
>  QiCadence/SUBMISSION.md                    |   160 -
>  QiCadence/docs/screenshots/01-home.png     |   Bin 1218299 -> 0 bytes
>  QiCadence/docs/screenshots/02-inbox.png    |   Bin 1218293 -> 0 bytes
>  QiCadence/docs/screenshots/03-pipeline.png |   Bin 1218293 -> 0 bytes
>  QiCadence/docs/screenshots/04-project.png  |   Bin 1018413 -> 0 bytes
>  QiCadence/docs/screenshots/05-capture.png  |   Bin 1223072 -> 0 bytes
>  QiCadence/docs/screenshots/06-new-deal.png |   Bin 1037313 -> 0 bytes
>  QiCadence/docs/screenshots/07-import.png   |   Bin 1024570 -> 0 bytes
>  QiCadence/main.js                          | 12122 ---------------------------
>  QiCadence/manifest.json                    |    11 -
> :
> warning: in the working copy of 'vizvibe.mmd', LF will be replaced by CRLF the next time Git touches it
>  QiCadence/.github/workflows/attest.yml     |    32 -
>  QiCadence/.gitignore                       |     8 -
>  QiCadence/.vscode/settings.json            |     3 -
>  QiCadence/LICENSE                          |    21 -
>  QiCadence/README.md                        |   252 -
>  QiCadence/SUBMISSION.md                    |   160 -
>  QiCadence/docs/screenshots/01-home.png     |   Bin 1218299 -> 0 bytes
>  QiCadence/docs/screenshots/02-inbox.png    |   Bin 1218293 -> 0 bytes
>  QiCadence/docs/screenshots/03-pipeline.png |   Bin 1218293 -> 0 bytes
>  QiCadence/docs/screenshots/04-project.png  |   Bin 1018413 -> 0 bytes
>  QiCadence/docs/screenshots/05-capture.png  |   Bin 1223072 -> 0 bytes
>  QiCadence/docs/screenshots/06-new-deal.png |   Bin 1037313 -> 0 bytes
>  QiCadence/docs/screenshots/07-import.png   |   Bin 1024570 -> 0 bytes
>  QiCadence/main.js                          | 12122 ---------------------------
>  QiCadence/manifest.json                    |    11 -
> '
> PS C:\QiLabs\60_QiApps\52_QiApp_QiLife> git push -u origin alpha/qicadence        
> Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
> remote: This repository moved. Please use the new location:
> remote:   https://github.com/qiallyme/52_QiApp_QiLife.git
> remote: 
> remote: Create a pull request for 'alpha/qicadence' on GitHub by visiting:
> remote:      https://github.com/qiallyme/52_QiApp_QiLife/pull/new/alpha/qicadence
> remote: 
> To https://github.com/qiallyme/qilife.git
>  * [new branch]      alpha/qicadence -> alpha/qicadence
> branch 'alpha/qicadence' set up to track 'origin/alpha/qicadence'.
> PS C:\QiLabs\60_QiApps\52_QiApp_QiLife>  
> :

### Assistant
> That output is not scary, but it is telling us something important: the branch exists and pushed, but your actual Cadence move/docs/prototypes are **not committed yet**. So right now GitHub has the branch pointer, not the work.

### Assistant
> Yep. Here’s what happened.
> 
> ## What your output means
> 
> ### 1. You are on the right branch
> 
> ```powershell
> On branch alpha/qicadence
> ```
> 
> Good. That branch exists.
> 
> ### 2. The branch was pushed, but your work was **not**
> 
> This line:
> 
> ```powershell
> Total 0 (delta 0)
> ```
> 
> means you pushed the branch pointer, not the changed files. Nothing has been committed yet.
> 
> ### 3. `QiCadence/` was deleted from its old tracked location
> 
> Git sees all of this:
> 
> ```text
> deleted: QiCadence/main.js
> deleted: QiCadence/styles.css
> deleted: QiCadence/README.md
> ...
> ```
> 
> That probably means the agent moved `QiCadence/` into:
> 
> ```text
> reference/
> ```
> 
> or copied/reorganized it there.
> 
> That is fine **if intentional**, but it needs to be committed as a move, not left dirty.
> 
> ### 4. `docs/`, `prototypes/`, and `reference/` are untracked
> 
> That means the agent likely created the exact kind of docs/prototype structure we wanted.
> 
> Good.
> 
> ### 5. `vizvibe.mmd` is modified
> 
> That is separate. Do **not** blindly commit it unless you know why it changed.
> 
> ### 6. Your GitHub remote is stale
> 
> Git says:
> 
> ```text
> remote: This repository moved. Please use the new location:
> https://github.com/qiallyme/52_QiApp_QiLife.git
> ```
> 
> So fix the remote. Not urgent, but do it now before it becomes haunted.
> 
> ---
> 
> # Do this next
> 
> Run this first:
> 
> ```powershell
> git status --short
> git diff --name-status
> git remote -v
> ```
> 
> Then inspect whether Cadence exists under `reference/`:
> 
> ```powershell
> Get-ChildItem .\reference -Recurse -Depth 2
> ```
> 
> If you see something like:
> 
> ```text
> reference/obsidian-cadence/main.js
> reference/obsidian-cadence/styles.css
> reference/obsidian-cadence/LICENSE
> ```
> 
> then the move is fine.
> 
> ---
> 
> # Fix the GitHub remote
> 
> Run:
> 
> ```powershell
> git remote set-url origin https://github.com/qiallyme/52_QiApp_QiLife.git
> git remote -v
> ```
> 
> ---
> 
> # If the move was intentional
> 
> Stage the deleted old folder plus the new reference/docs/prototype files:
> 
> ```powershell
> git add -A QiCadence reference docs prototypes
> ```
> 
> Do **not** add `vizvibe.mmd` yet unless the agent explains it.
> 
> Check staged files:
> 
> ```powershell
> git diff --cached --stat
> git status
> ```
> 
> Then commit:
> 
> ```powershell
> git commit -m "analyze qicadence as qilife workbench reference"
> git push
> ```
> 
> ---
> 
> # If the move was NOT intentional
> 
> Restore the deleted `QiCadence/` folder:
> 
> ```powershell
> git restore QiCadence
> ```
> 
> Then only stage docs/prototypes/reference if they are correct:
> 
> ```powershell
> git add docs prototypes reference
> git commit -m "add qicadence reference analysis and entity contract"
> git push
> ```
> 
> ---
> 
> # Deal with `vizvibe.mmd`
> 
> Ask the agent what changed, or inspect it:
> 
> ```powershell
> git diff -- vizvibe.mmd
> ```
> 
> If it is accidental:
> 
> ```powershell
> git restore vizvibe.mmd
> ```
> 
> If it is intentional:
> 
> ```powershell
> git add vizvibe.mmd
> git commit -m "update vizvibe diagram"
> git push
> ```
> 
> Do not bundle it into the Cadence analysis commit unless it directly belongs. Clean commits save lives.
> 
> ---
> 
> # About Antigravity having Supabase access
> 
> That is powerful, but dangerous. Do **not** let it freestyle directly in Supabase.
> 
> The rule:
> 
> > **Schema first. Migration files first. Live database second. Data migration third.**
> 
> Tell Antigravity this:
> 
> :::writing{variant="standard" id="92746"}
> You are working inside the QiLife repo on branch alpha/qicadence.
> 
> You now have access to Supabase, but do not directly freestyle changes in the live database.
> 
> Goal:
> Create a safe QiLife alpha database foundation based on the QiLife Markdown entity contract and Cadence-inspired entity model.
> 
> Hard rules:
> 1. Do not modify production app routes yet.
> 2. Do not build two-way sync.
> 3. Do not migrate real user data until the schema/migrations are reviewed.
> 4. Do not store secrets in the repo.
> 5. Do not make direct untracked Supabase changes without creating migration files.
> 6. Prefer SQL migration files committed to the repo.
> 7. Use an alpha/dev namespace or schema if possible.
> 8. Every table must use stable IDs and timestamps.
> 9. Keep Markdown/frontmatter compatibility in mind.
> 10. Postgres is the durable mirror/index for now, not the only authority.
> 
> First tasks:
> 1. Inspect the new docs:
>    - docs/architecture/cadence_reference_analysis.md
>    - docs/architecture/qilife_markdown_entity_contract.md
>    - docs/decisions/ADR-00XX_cadence_as_qilife_workbench_reference.md
>    - prototypes/cadence_qilife_mapping/
> 
> 2. Create a Supabase migration plan document:
>    docs/architecture/qilife_supabase_alpha_schema_plan.md
> 
> Include:
> - proposed schema name
> - proposed tables
> - relationships
> - indexes
> - RLS assumptions
> - import/migration phases
> - risks
> - what data should not be migrated yet
> 
> 3. Create SQL migration files only after the plan:
>    supabase/migrations/YYYYMMDDHHMMSS_create_qilife_alpha_core.sql
> 
> Core alpha tables:
> - entities
> - people
> - organizations
> - projects
> - matters
> - care_items
> - interactions
> - tasks
> - reminders
> - file_records
> - accounts
> - transactions
> - entity_relationships
> - entity_links
> - source_documents
> - import_batches
> 
> 4. Every domain table should include:
> - id
> - entity_id if using shared entity registry
> - type
> - status
> - title or name
> - tags
> - source
> - markdown_path
> - frontmatter_json
> - body_markdown
> - created_at
> - updated_at
> - archived_at
> 
> 5. Create relationship support:
> - entity_relationships should support from_entity_id, to_entity_id, relationship_type, confidence/source, created_at, updated_at.
> 
> 6. Create import tracking:
> - import_batches
> - source_documents
> - checksum/hash fields where useful
> 
> 7. Do not import CSVs or Markdown files yet.
> 8. Do not apply migrations to production until explicitly approved.
> 9. After creating the migration files, report:
>    - files created
>    - tables proposed
>    - whether anything was applied to Supabase
>    - risks
>    - next recommended action
> :::
> 
> ## My ruling
> 
> Right now your priority order is:
> 
> 1. **Clean up Git state**
> 2. **Commit the Cadence analysis branch**
> 3. **Make Antigravity write Supabase migration plans/files**
> 4. **Review before applying**
> 5. **Then migrate data**
> 
> Do not skip straight to data migration. That would be the fastest way to make a beautiful mess with a Postgres accent.

### User
> PS C:\QiLabs\60_QiApps\52_QiApp_QiLife> git status --short
>  D QiCadence/.github/workflows/attest.yml
>  D QiCadence/.gitignore
>  D QiCadence/.vscode/settings.json
>  D QiCadence/LICENSE
>  D QiCadence/README.md
>  D QiCadence/SUBMISSION.md
>  D QiCadence/docs/screenshots/01-home.png
>  D QiCadence/docs/screenshots/02-inbox.png
>  D QiCadence/docs/screenshots/03-pipeline.png
>  D QiCadence/docs/screenshots/04-project.png
>  D QiCadence/docs/screenshots/05-capture.png
>  D QiCadence/docs/screenshots/06-new-deal.png
>  D QiCadence/docs/screenshots/07-import.png
>  D QiCadence/main.js
>  D QiCadence/manifest.json
>  D QiCadence/styles.css
>  D QiCadence/versions.json
>  M vizvibe.mmd
> ?? docs/
> ?? prototypes/
> ?? reference/
> PS C:\QiLabs\60_QiApps\52_QiApp_QiLife> git diff --name-status
> warning: in the working copy of 'vizvibe.mmd', LF will be replaced by CRLF the next time Git touches it
> D       QiCadence/.github/workflows/attest.yml
> D       QiCadence/.gitignore
> D       QiCadence/.vscode/settings.json
> D       QiCadence/LICENSE
> D       QiCadence/README.md
> D       QiCadence/SUBMISSION.md
> D       QiCadence/docs/screenshots/01-home.png
> D       QiCadence/docs/screenshots/02-inbox.png
> D       QiCadence/docs/screenshots/03-pipeline.png
> D       QiCadence/docs/screenshots/04-project.png
> D       QiCadence/docs/screenshots/05-capture.png
> D       QiCadence/docs/screenshots/06-new-deal.png
> D       QiCadence/docs/screenshots/07-import.png
> D       QiCadence/main.js
> D       QiCadence/manifest.json
> D       QiCadence/styles.css
> D       QiCadence/versions.json
> M       vizvibe.mmd
> (END)

### Assistant
> You’re currently stuck in Git’s pager. First:
> 
> ```powershell
> q
> ```
> 
> That exits the `(END)` screen.
> 
> ## What this means
> 
> Git sees:
> 
> ```text
> D  QiCadence/...
> ?? reference/
> ?? docs/
> ?? prototypes/
> M  vizvibe.mmd
> ```
> 
> Translation:
> 
> - `QiCadence/` was **deleted from its old tracked location**
> - new folders `reference/`, `docs/`, and `prototypes/` were created but are **not tracked yet**
> - `vizvibe.mmd` changed separately
> - This is probably fine **if QiCadence was moved into `reference/`**
> 
> Now verify.
> 
> ## Run this next
> 
> ```powershell
> Get-ChildItem .\reference -Recurse -Depth 2
> ```
> 
> You’re looking for something like:
> 
> ```text
> reference/obsidian-cadence/main.js
> reference/obsidian-cadence/styles.css
> reference/obsidian-cadence/LICENSE
> ```
> 
> or:
> 
> ```text
> reference/QiCadence/main.js
> ```
> 
> ## If Cadence is inside `reference/`
> 
> Then stage the move/docs/prototypes, but leave `vizvibe.mmd` alone for now:
> 
> ```powershell
> git add -A QiCadence reference docs prototypes
> git status --short
> git diff --cached --stat
> git commit -m "analyze qicadence as qilife workbench reference"
> git push
> ```
> 
> That will commit the deletion of old `QiCadence/` and the addition of the new `reference/` copy as one clean “move/reference” commit.
> 
> ## Then handle `vizvibe.mmd`
> 
> Inspect it:
> 
> ```powershell
> git diff -- vizvibe.mmd
> ```
> 
> If accidental:
> 
> ```powershell
> git restore vizvibe.mmd
> ```
> 
> If intentional:
> 
> ```powershell
> git add vizvibe.mmd
> git commit -m "update vizvibe diagram"
> git push
> ```
> 
> ## Also fix your remote
> 
> Git already warned you the repo moved. Run:
> 
> ```powershell
> git remote set-url origin https://github.com/qiallyme/52_QiApp_QiLife.git
> git remote -v
> ```
> 
> ## Do not do this yet
> 
> Do **not** run:
> 
> ```powershell
> git add .
> ```
> 
> Not yet. That would scoop `vizvibe.mmd` into the Cadence commit and make the commit messy. Clean commit, clean brain.

### User
> ok we are back, now let me make sure what should i tell the ide to do nwo.

### Assistant
> Yes. Tell the IDE agent to do **three things only right now**:
> 
> 1. **Clean/stabilize the Git branch**
> 2. **Commit the Cadence reference/docs/prototype work**
> 3. **Create Supabase schema plan + migration files, but do not migrate real data yet**
> 
> Do **not** let it start rewriting the app yet. We are still setting the foundation.
> 
> Copy/paste this into Antigravity:
> 
> :::writing{variant="standard" id="77426"}
> You are working inside:
> 
> C:\QiLabs\60_QiApps\52_QiApp_QiLife
> 
> Current branch should be:
> 
> alpha/qicadence
> 
> Goal:
> Stabilize the current QiCadence/Cadence reference work, commit it cleanly, then prepare the QiLife Supabase alpha schema plan and migration files. Do not rewrite the app yet.
> 
> Hard rules:
> 1. Do not modify production QiLife routes or frontend behavior.
> 2. Do not directly apply Supabase changes until migration files are created and reviewed.
> 3. Do not migrate real data yet.
> 4. Do not build two-way sync.
> 5. Do not delete existing work unless verifying it was intentionally moved.
> 6. Do not commit unrelated changes with the Cadence/Supabase work.
> 7. Do not store secrets, API keys, service role keys, or local env values in the repo.
> 
> Step 1 — Inspect Git state:
> Run:
> 
> git status --short
> git branch --show-current
> git remote -v
> 
> Confirm we are on:
> 
> alpha/qicadence
> 
> If not, stop and report.
> 
> Step 2 — Fix remote if needed:
> If origin still points to the old moved repo, update it to:
> 
> https://github.com/qiallyme/52_QiApp_QiLife.git
> 
> Use:
> 
> git remote set-url origin https://github.com/qiallyme/52_QiApp_QiLife.git
> 
> Step 3 — Verify QiCadence was moved, not lost:
> The old tracked folder QiCadence/ currently appears deleted. Check whether its contents now exist under:
> 
> reference/
> reference/obsidian-cadence/
> reference/QiCadence/
> 
> Specifically verify these files exist somewhere under reference/:
> 
> main.js
> styles.css
> manifest.json
> README.md
> LICENSE
> 
> If the files exist under reference/, treat the QiCadence deletion as an intentional move.
> 
> If they do not exist, stop and report. Do not commit deletion.
> 
> Step 4 — Inspect docs/prototypes:
> Verify the new folders:
> 
> docs/
> prototypes/
> reference/
> 
> List what was created.
> 
> Specifically look for:
> 
> docs/architecture/cadence_reference_analysis.md
> docs/architecture/qilife_markdown_entity_contract.md
> docs/decisions/ADR-00XX_cadence_as_qilife_workbench_reference.md
> prototypes/cadence_qilife_mapping/
> 
> If any of these are missing, create them before committing.
> 
> Step 5 — Handle vizvibe.mmd separately:
> There is a modified file:
> 
> vizvibe.mmd
> 
> Inspect the diff:
> 
> git diff -- vizvibe.mmd
> 
> If the change is unrelated to QiCadence/Cadence/Supabase schema work, restore it:
> 
> git restore vizvibe.mmd
> 
> If it is clearly related and intentional, report what changed and keep it for a separate commit later. Do not include it in the Cadence reference commit unless it is directly part of the Cadence mapping.
> 
> Step 6 — Commit Cadence reference work:
> Stage only the Cadence/reference/docs/prototype work:
> 
> git add -A QiCadence reference docs prototypes
> 
> Do not use git add .
> 
> Then run:
> 
> git status --short
> git diff --cached --stat
> 
> If staged changes look correct, commit:
> 
> git commit -m "analyze qicadence as qilife workbench reference"
> 
> Then push:
> 
> git push -u origin alpha/qicadence
> 
> Step 7 — Create Supabase alpha schema plan:
> After the Cadence reference commit is clean, create:
> 
> docs/architecture/qilife_supabase_alpha_schema_plan.md
> 
> This document should define a safe alpha database foundation based on the QiLife Markdown entity contract.
> 
> Include:
> - purpose
> - schema strategy
> - whether to use public tables or a dedicated ql_alpha schema
> - table list
> - relationship model
> - indexes
> - RLS assumptions
> - import phases
> - data migration risks
> - what not to migrate yet
> - rollback notes
> 
> Core tables to plan:
> - entities
> - people
> - organizations
> - projects
> - matters
> - care_items
> - interactions
> - tasks
> - reminders
> - file_records
> - accounts
> - transactions
> - entity_relationships
> - entity_links
> - source_documents
> - import_batches
> - tags
> - entity_tags
> 
> Step 8 — Create SQL migration file:
> Create a timestamped migration file under the repo’s Supabase migrations folder.
> 
> First locate the existing Supabase folder. It may be one of:
> 
> supabase/migrations/
> 20_QiSystem/50_data/supabase/qisupabase/migrations/
> qisupabase/migrations/
> 
> Do not invent a new migrations folder if one already exists.
> 
> Create a migration named like:
> 
> YYYYMMDDHHMMSS_create_qilife_alpha_core.sql
> 
> The migration should:
> - create the alpha/core tables
> - use uuid primary keys where appropriate
> - include stable entity IDs
> - include timestamps
> - include archived_at for soft deletion
> - include markdown_path, frontmatter_json, body_markdown where useful
> - include source/source_system fields
> - include indexes for entity type, status, tags, relationships, markdown_path
> - include updated_at triggers if the project already has a standard pattern
> - avoid destructive SQL
> - avoid importing any data
> 
> Step 9 — RLS:
> If the project already has RLS conventions, follow them.
> 
> If not, add comments/placeholders but do not create overly permissive policies.
> 
> Do not expose private life/care/legal/finance data publicly.
> 
> Step 10 — Do not apply to Supabase yet unless explicitly approved:
> Create the migration file, but do not run it against live Supabase unless I explicitly say to apply it.
> 
> Step 11 — Final report:
> After completing, report:
> 
> - current branch
> - remote URL
> - whether QiCadence was moved to reference/
> - files created
> - files changed
> - files committed
> - migration file path
> - whether anything was applied to Supabase
> - remaining uncommitted files
> - next recommended action
> :::
> 
> ## Your next command after the agent finishes
> 
> Run:
> 
> ```powershell
> git status --short
> ```
> 
> What we want to see after the first commit:
> 
> ```text
> clean
> ```
> 
> or only the Supabase plan/migration files showing as new/modified.
> 
> ## Important
> 
> Antigravity having Supabase access is useful, but dangerous. Right now it should create **migration files**, not cowboy-click tables into the live database.
> 
> Schema first.  
> Migration files second.  
> Review third.  
> Apply fourth.  
> Import data last.
> 
> No haunted Postgres today.

### User
> ok an after that is done.

### Assistant
> After that is done, the next move is **not data migration yet**.
> 
> The next move is:
> 
> ## Phase 2: Review → Apply Alpha Schema → Seed Fake/Test Data → Build Read-Only QiLife Workbench View
> 
> Order matters.
> 
> ```text
> 1. Confirm Git is clean
> 2. Review migration SQL
> 3. Apply migration to Supabase alpha/dev only
> 4. Insert tiny fake test data
> 5. Verify tables in Supabase
> 6. Build read-only UI surface using the new entity model
> 7. Then decide import strategy for real Markdown/CSV data
> ```
> 
> No real data until the schema proves itself.
> 
> ---
> 
> ## What to tell the IDE agent after Phase 1 finishes
> 
> Use this after it reports the Cadence docs + Supabase migration files are created/committed.
> 
> :::writing{variant="standard" id="31847"}
> You are still working inside:
> 
> C:\QiLabs\60_QiApps\52_QiApp_QiLife
> 
> Branch:
> 
> alpha/qicadence
> 
> Phase 2 Goal:
> Review and safely apply the QiLife alpha Supabase schema, seed minimal fake data, and create a read-only QiLife Workbench prototype surface. Do not migrate real data yet.
> 
> Hard rules:
> 1. Do not migrate real user/care/legal/finance data yet.
> 2. Do not build two-way sync.
> 3. Do not modify production routes unless using a clearly isolated alpha route.
> 4. Do not store secrets in the repo.
> 5. Do not create destructive migrations.
> 6. Do not apply anything to production Supabase unless explicitly confirmed this is the intended dev/alpha project.
> 7. Keep all new app work isolated behind an alpha/prototype route or feature flag.
> 
> Step 1 — Confirm clean branch:
> Run:
> 
> git status --short
> git branch --show-current
> 
> If there are uncommitted files from Phase 1, stop and report them.
> 
> Step 2 — Review Supabase migration:
> Find the migration created in Phase 1, likely named:
> 
> *_create_qilife_alpha_core.sql
> 
> Review for:
> - no DROP statements
> - no destructive ALTER statements
> - no real data inserts
> - stable IDs
> - entities table
> - entity_relationships table
> - source_documents/import_batches tables
> - timestamps
> - archived_at
> - markdown_path
> - frontmatter_json
> - body_markdown
> - indexes
> - safe RLS comments or policies
> 
> If the migration looks unsafe, stop and report.
> 
> Step 3 — Apply migration to Supabase alpha/dev:
> Only apply the migration if the connected Supabase project is confirmed to be the QiLife alpha/dev project.
> 
> Use the project’s established Supabase workflow.
> 
> If Supabase CLI is configured, prefer:
> 
> supabase migration up
> 
> or the repo’s existing migration command.
> 
> If the workflow is different, report the exact command before running.
> 
> Step 4 — Create tiny fake seed data only:
> Create a seed file, not real data.
> 
> Use fake examples only:
> - one person
> - one organization
> - one project
> - one matter
> - one care_item
> - one interaction
> - one task
> - one reminder
> - one file_record
> - one relationship between entities
> 
> Create this as a repo file, for example:
> 
> supabase/seed/qilife_alpha_fake_seed.sql
> 
> or wherever this repo stores seed files.
> 
> Do not insert real personal, medical, legal, financial, or family data.
> 
> Step 5 — Apply fake seed only if safe:
> Apply the fake seed to alpha/dev Supabase only.
> 
> Verify rows exist.
> 
> Step 6 — Create a read-only prototype data layer:
> Create an isolated prototype data reader for the new QiLife entity model.
> 
> Do not wire it into main production behavior.
> 
> Possible location:
> 
> src/features/alpha_qilife_workbench/
> src/features/alpha_qilife_workbench/data/
> src/features/alpha_qilife_workbench/components/
> 
> Create:
> - README.md
> - entityTypes.ts
> - entityQueries.ts
> - AlphaWorkbenchPage or equivalent prototype component
> 
> The prototype should read from Supabase and show:
> - entity counts
> - people
> - projects
> - matters
> - tasks/reminders
> - relationships
> 
> Read-only only. No create/update/delete UI yet.
> 
> Step 7 — Route isolation:
> If adding a route, use an obvious alpha route such as:
> 
> /alpha/qilife-workbench
> 
> or whatever route pattern this app already uses.
> 
> Label it clearly:
> 
> QiLife Workbench Alpha
> 
> Step 8 — Do not copy Cadence UI wholesale yet:
> Use the Cadence-inspired structure:
> - left rail
> - dashboard cards
> - entity lists
> - project/matter cards
> - inbox/task section
> 
> But keep implementation minimal and clean.
> 
> Step 9 — Commit Phase 2:
> After successful schema apply, fake seed, and read-only alpha UI prototype, run:
> 
> git status --short
> git diff --stat
> 
> Commit with:
> 
> git add -A
> git commit -m "create qilife alpha workbench schema prototype"
> git push
> 
> Step 10 — Final report:
> Report:
> - current branch
> - migration applied? yes/no
> - Supabase project/environment used
> - seed applied? yes/no
> - fake rows created
> - files created/changed
> - alpha route created
> - whether app still builds
> - remaining risks
> - next recommended step
> :::
> 
> ---
> 
> ## Then Phase 3 is data import planning
> 
> Only after the fake data works:
> 
> ```text
> Markdown/frontmatter importer
> CSV importer
> Google Drive / QiNexus file indexer
> Firefly finance import
> Mom care import
> Legal matter import
> ```
> 
> But not all at once. First importer should be **Markdown/frontmatter → Supabase**, one-way.
> 
> ## The next big decision
> 
> After Phase 2, we choose the source-of-truth mode:
> 
> | Mode | Meaning | My pick |
> |---|---|---|
> | Markdown-first | Obsidian edits files, Supabase mirrors | Best for now |
> | Supabase-first | App edits database, Markdown exports | Later |
> | Two-way sync | Both edit both | Not yet, demon portal |
> 
> So after Phase 2, tell the agent:
> 
> > Build a one-way Markdown/frontmatter importer prototype.
> 
> Not two-way. Not yet. We are not summoning YAML Satan before breakfast.

### User
> while its working on that i really wanted to start using open claw. OpenClaw 2026.6.6 (8c802aa) — Deployed locally, trusted globally, debugged eternally.
> 
> |
> o
> 17:52:46 [gateway] loading configuration…
> 17:52:50 [gateway] resolving authentication…
> 17:52:50 [gateway] starting...
> 17:52:59 [gateway] starting HTTP server...
> 17:52:59 [health-monitor] started (interval: 300s, startup-grace: 60s, channel-connect-grace: 120s)
> 17:53:00 [gateway] agent model: openai/gpt-5.5 (thinking=medium, fast=off)
> 17:53:00 [gateway] http server listening (8 plugins: browser, canvas, device-pair, file-transfer, memory-core, parallel, phone-control, talk-voice; 10.0s)
> 17:53:00 [gateway] log file: C:\Users\codyr\AppData\Local\Temp\openclaw\openclaw-2026-06-16.log
> 17:53:00 [gateway] security warning: dangerous config flags enabled: gateway.controlUi.allowInsecureAuth=true. Run `openclaw security audit`.
> 17:53:00 [gateway] starting channels and sidecars...
> 17:53:03 [hooks] loaded 5 internal hook handlers
> 17:53:04 [gateway] ready
> 17:53:04 [heartbeat] started
> 17:53:12 [gateway] provider auth state pre-warmed in 3003ms eventLoopMax=41.3ms
> 17:53:14 [gateway] agent runtime plugins pre-warmed in 299ms

### Assistant
> OpenClaw is up, but that warning is the part I care about first. It says the gateway is ready, but insecure control UI auth is enabled — usable locally, not something to casually expose.

### Assistant
> Yes — **it’s running.** Your log shows the gateway is ready.
> 
> But before you start giving it keys to the kingdom, here’s the sane path.
> 
> ## What your log says
> 
> ```text
> [gateway] ready
> [heartbeat] started
> agent model: openai/gpt-5.5
> 8 plugins: browser, canvas, device-pair, file-transfer, memory-core, parallel, phone-control, talk-voice
> security warning: gateway.controlUi.allowInsecureAuth=true
> ```
> 
> Translation:
> 
> > OpenClaw is live locally, with browser/file/phone-style control plugins enabled. That is powerful. Treat it like a baby sysadmin with scissors.
> 
> OpenClaw’s own site frames it as an assistant that can actually perform tasks, not just chat, so the security boundary matters more than usual. citeturn207523search1
> 
> ## First thing: run the security audit
> 
> Do this before connecting it to important stuff:
> 
> ```powershell
> openclaw security audit
> ```
> 
> The specific warning:
> 
> ```text
> gateway.controlUi.allowInsecureAuth=true
> ```
> 
> is not automatically fatal, but it is a **local compatibility mode**. OpenClaw’s docs say it allows Control UI auth without device identity when loaded over insecure HTTP on localhost, and they recommend HTTPS/Tailscale Serve or opening the UI on `127.0.0.1`. citeturn207523search0
> 
> So for now:
> 
> ```text
> Use:       http://127.0.0.1:PORT
> Avoid:     LAN IP exposure
> Avoid:     public Cloudflare tunnel
> Avoid:     random phone/browser access until paired securely
> ```
> 
> ## My recommended “safe first use” mode
> 
> For the first session, let OpenClaw do **low-risk local work** only:
> 
> ### Good first tasks
> 
> - summarize folders
> - inspect repo structure
> - read docs
> - draft plans
> - organize notes
> - generate markdown files
> - create non-sensitive checklists
> - test browser/canvas behavior
> 
> ### Do **not** let it do yet
> 
> - Supabase schema changes
> - Git commits/pushes
> - deleting/moving folders
> - Gmail/calendar actions
> - phone-control actions
> - file-transfer with private docs
> - anything involving secrets, tokens, medical/legal/financial data
> 
> Not because it’s bad — because it has hands now. Hands need rules.
> 
> ## What I’d use it for while Antigravity works
> 
> Give OpenClaw a safe mission like this:
> 
> ```text
> You are running locally as an assistant for QiLife planning.
> 
> Do not modify files yet.
> 
> Your job is read-only analysis first.
> 
> Inspect the local QiLife project folder and help me understand:
> 1. the current repo structure
> 2. where the Cadence/QiCadence reference folder is
> 3. what docs/prototypes exist
> 4. what Supabase migration files exist
> 5. what still needs review before applying migrations
> 
> Rules:
> - Do not delete, move, rename, commit, push, or apply migrations.
> - Do not read .env files or secrets.
> - Do not send data externally except through the configured model call.
> - Summarize findings in plain English.
> - Ask before performing any write action.
> ```
> 
> That gives you value without letting it go full raccoon.
> 
> ## Then test one tiny write action
> 
> After read-only analysis works, use a harmless file:
> 
> ```text
> Create a local scratch note at:
> 
> scratch/openclaw_test_note.md
> 
> Include:
> - current date
> - OpenClaw startup status
> - plugins observed from the log
> - next safe actions
> 
> Do not edit any existing files.
> ```
> 
> If that works, you’ve proven the loop.
> 
> ## Important security posture
> 
> OpenClaw-style agent frameworks are useful because they can operate across browser, files, messaging, and local tools. That same tool surface creates risks from prompt injection, unsafe tool execution, plugin behavior, and overbroad local access; recent security research specifically calls out those categories for OpenClaw-like agent runtimes. citeturn207523academia46turn207523academia45
> 
> So the operating rule is:
> 
> > **OpenClaw can help coordinate. Antigravity can build. Git controls what becomes real. Supabase only changes through reviewed migrations.**
> 
> That’s the clean chain.
> 
> ## Immediate next steps
> 
> Run:
> 
> ```powershell
> openclaw security audit
> ```
> 
> Then open the Control UI locally using `127.0.0.1`, not a public URL.
> 
> Then give it the read-only QiLife inspection prompt above. Keep it away from Supabase and Git writes until it proves it can follow rules.

### User
> ◇
> 
> 🦞 OpenClaw 2026.6.6 (8c802aa) — Claws out, commit in—let's ship something mildly responsible.
> 
> OpenClaw security audit
> Summary: 0 critical · 3 warn · 1 info
> Run deeper: openclaw security audit --deep
> 
> WARN
> gateway.trusted_proxies_missing Reverse proxy headers are not trusted
>   gateway.bind is loopback and gateway.trustedProxies is empty. If you expose the Control UI through a reverse proxy, configure trusted proxies so local-client checks cannot be spoofed.
>   Fix: Set gateway.trustedProxies to your proxy IPs or keep the Control UI local-only.
> gateway.control_ui.insecure_auth Control UI insecure auth toggle enabled
>   gateway.controlUi.allowInsecureAuth=true does not bypass secure context or device identity checks; only dangerouslyDisableDeviceAuth disables Control UI device identity checks.
>   Fix: Disable it or switch to HTTPS (Tailscale Serve) or localhost.
> config.insecure_or_dangerous_flags Insecure or dangerous config flag enabled
>   Detected enabled flag: gateway.controlUi.allowInsecureAuth=true.
>   Fix: Disable this flag when not actively debugging, or keep deployment scoped to trusted/local-only networks.
> 
> INFO
> summary.attack_surface Attack surface summary
>   groups: open=0, allowlist=0
> tools.elevated: enabled
> hooks.webhooks: disabled
> hooks.internal: enabled
> browser control: enabled
> trust model: personal assistant (one trusted operator boundary), not hostile multi-tenant on one shared gateway
> PS C:\Users\codyr>

### Assistant
> Good. This is **not a panic situation**.
> 
> ## Audit verdict
> 
> You have:
> 
> ```text
> 0 critical
> 3 warnings
> 1 info
> ```
> 
> That means OpenClaw is usable **as long as you keep it local-only right now**.
> 
> The important line:
> 
> ```text
> gateway.bind is loopback
> ```
> 
> That means it is bound to your machine, not openly listening to the whole network. Good.
> 
> The risky part:
> 
> ```text
> gateway.controlUi.allowInsecureAuth=true
> tools.elevated: enabled
> browser control: enabled
> ```
> 
> Translation:
> 
> > OpenClaw can do powerful local actions, and the Control UI has a debugging/insecure-auth flag enabled. Fine for local testing. Bad idea if exposed through Tailscale Serve, Cloudflare, LAN, or reverse proxy without tightening it.
> 
> ## Do this now
> 
> ### 1. Run the deeper audit
> 
> ```powershell
> openclaw security audit --deep
> ```
> 
> If that comes back with no criticals, we’re green for controlled local testing.
> 
> ---
> 
> ### 2. Keep it local-only for now
> 
> Use it from:
> 
> ```text
> 127.0.0.1 / localhost
> ```
> 
> Do **not** expose it through:
> 
> ```text
> Cloudflare Tunnel
> Tailscale Serve
> LAN IP
> public domain
> reverse proxy
> ```
> 
> until we disable insecure auth or configure trusted proxies properly.
> 
> ---
> 
> ### 3. First OpenClaw assignment should be read-only
> 
> Give OpenClaw this:
> 
> ```text
> You are helping me inspect my local QiLife project.
> 
> Operate in read-only mode first.
> 
> Project path:
> C:\QiLabs\60_QiApps\52_QiApp_QiLife
> 
> Tasks:
> 1. Inspect the repo structure.
> 2. Confirm the current Git branch.
> 3. Identify where the QiCadence/Cadence reference files are located.
> 4. Identify docs, prototypes, and Supabase migration files related to QiLife alpha/Cadence work.
> 5. Summarize what exists and what still needs review.
> 
> Rules:
> - Do not modify, delete, move, rename, commit, push, or apply migrations.
> - Do not read .env files or secrets.
> - Do not touch Supabase.
> - Do not run destructive commands.
> - Ask before any write action.
> ```
> 
> That gives it something useful without letting it drive a forklift through your repo.
> 
> ---
> 
> ## What the warnings actually mean
> 
> | Warning | Meaning | Action |
> |---|---|---|
> | `trusted_proxies_missing` | Only matters if you expose through reverse proxy | Ignore while local-only |
> | `control_ui.insecure_auth` | Debug/insecure auth flag enabled | Disable before exposing |
> | `insecure_or_dangerous_flags` | Same underlying issue | Keep local or turn it off |
> 
> ## My ruling
> 
> You can start using OpenClaw **now**, but only in this mode:
> 
> ```text
> Local-only
> Read-only first
> No Supabase
> No Git writes
> No secrets
> No phone/file-transfer actions yet
> ```
> 
> Once it proves it can follow instructions, let it create a harmless scratch file. Then maybe let it inspect docs. But do **not** let it touch migrations or live database yet.
> 
> Keep Antigravity on the build lane.  
> Use OpenClaw as your local scout.

### User
> {'asset_pointer': 'sediment://file_000000009d34722f9a541d0cfcea7183', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 857, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 72702, 'width': 1018}cadence in obsidian also allows for some customization,

### Assistant
> Yes — **this changes the read.**
> 
> Cadence is not just a pretty view. It has a **mini schema/configuration engine** hiding in plain sight.
> 
> From your screenshot, Cadence supports:
> 
> | Feature | Why it matters |
> |---|---|
> | Custom navigation pages | User-defined sections, labels, icons, layouts |
> | Sidebar section assignment | Planner / CRM / PRM-style grouping |
> | Default layout per page | Table, board, etc. |
> | Custom entity properties | User-editable fields per entity type |
> | Technical frontmatter keys | Clean bridge to Markdown + database fields |
> | Field types | text, enum/select, tags, date, etc. |
> | Options/source column | Enum values, folder sources, history sources |
> | Locked system fields | Protects core properties like `name`, `status`, `priority` |
> 
> That is **exactly** the thing we need to steal conceptually.
> 
> ## The important architecture upgrade
> 
> Do **not** make the QiLife database only a bunch of fixed tables.
> 
> Make it:
> 
> ```text
> core tables
> + entity registry
> + configurable property definitions
> + custom field values / JSONB
> + nav/page config
> ```
> 
> That way QiLife can grow without needing a schema migration every time you decide:
> 
> > “Actually, Mom Care needs Oxygen Vendor, Insurance Contact, Care Risk Level, and Preferred Hospital.”
> 
> Because girl, you absolutely will decide that. And you’ll be right.
> 
> ## The clean database pattern
> 
> ### 1. Stable core tables
> 
> These are the boring durable tables:
> 
> ```text
> entities
> people
> organizations
> projects
> matters
> care_items
> tasks
> reminders
> file_records
> entity_relationships
> ```
> 
> ### 2. Config tables
> 
> These copy the Cadence customization idea:
> 
> ```text
> entity_types
> entity_property_definitions
> entity_property_options
> navigation_pages
> entity_view_configs
> entity_layout_configs
> ```
> 
> ### 3. Flexible values
> 
> For custom fields, use either:
> 
> ```text
> entity_property_values
> ```
> 
> or:
> 
> ```text
> custom_fields jsonb
> ```
> 
> My recommendation for alpha:
> 
> > **Use core columns + `custom_fields jsonb` first. Add `entity_property_values` later only if needed.**
> 
> Do not over-normalize yet. That’s how systems become a tax form wearing a trench coat.
> 
> ## What this means for QiLife
> 
> QiLife entities should have:
> 
> ```yaml
> ---
> id: project_01J...
> type: project
> title: Mom Care Plan
> status: active
> priority: high
> tags:
>   - mom-care
> custom_fields:
>   insurance_plan: Humana
>   oxygen_vendor: Example Vendor
>   next_review_date: 2026-06-20
> ---
> ```
> 
> And in Postgres:
> 
> ```text
> projects
> - id
> - entity_id
> - title
> - status
> - priority
> - tags
> - custom_fields jsonb
> - markdown_path
> - frontmatter_json
> - body_markdown
> ```
> 
> Then the UI reads `entity_property_definitions` to know how to render fields.
> 
> That gives you Cadence-style customization without hardcoding every life situation into the schema.
> 
> ## Tell the IDE agent this next
> 
> Add this to the current Supabase/schema task.
> 
> :::writing{variant="standard" id="41982"}
> Update the QiLife alpha schema plan to account for Cadence-style customization.
> 
> New context:
> Cadence’s Obsidian settings UI supports custom navigation pages and custom entity properties. Each entity type can have configurable properties with:
> - display label
> - technical frontmatter key
> - field type
> - options/source
> - locked/system fields
> - visual ordering
> - sidebar section
> - default layout
> - icon
> 
> QiLife should adopt this concept as a configurable metadata layer.
> 
> Update the Supabase alpha schema plan and migration proposal to include these concepts safely.
> 
> Add/plan these config tables:
> 1. entity_types
>    - id
>    - key
>    - label
>    - description
>    - default_folder_path
>    - default_table_name
>    - icon
>    - is_system
>    - is_enabled
>    - sort_order
>    - created_at
>    - updated_at
> 
> 2. entity_property_definitions
>    - id
>    - entity_type_key
>    - property_key
>    - label
>    - field_type
>    - options_json
>    - source_type
>    - source_config_json
>    - is_required
>    - is_system
>    - is_locked
>    - is_hidden
>    - sort_order
>    - maps_to_column
>    - frontmatter_key
>    - created_at
>    - updated_at
> 
> 3. navigation_pages
>    - id
>    - key
>    - label
>    - sidebar_section
>    - default_layout
>    - icon
>    - entity_type_key
>    - route_path
>    - is_system
>    - is_enabled
>    - sort_order
>    - created_at
>    - updated_at
> 
> 4. entity_view_configs
>    - id
>    - entity_type_key
>    - view_key
>    - view_type
>    - group_by_property
>    - sort_by_property
>    - filters_json
>    - visible_properties_json
>    - layout_json
>    - is_default
>    - created_at
>    - updated_at
> 
> Also update core entity/domain tables to support:
> - custom_fields jsonb
> - frontmatter_json jsonb
> - markdown_path
> - body_markdown
> - source_system
> - archived_at
> 
> Important design rule:
> Do not create a physical SQL column for every custom Cadence-style property. Use stable columns for core fields and custom_fields jsonb for flexible extension fields. Later, frequently queried custom properties can be promoted to real columns through migrations.
> 
> Update:
> - docs/architecture/qilife_supabase_alpha_schema_plan.md
> - the alpha migration file if already created
> - prototypes/cadence_qilife_mapping/entityMap.json if appropriate
> 
> Do not apply the migration to live Supabase yet unless explicitly approved.
> :::
> 
> ## My ruling
> 
> This is the better model:
> 
> ```text
> Cadence UI customization
> → QiLife metadata/config tables
> → Markdown frontmatter contract
> → Supabase durable mirror
> → QiLife Workbench renders from config
> ```
> 
> That means QiLife can eventually let you customize:
> 
> ```text
> People
> Care
> Legal
> Finance
> Projects
> Vendors
> Claims
> Appointments
> Medications
> Documents
> ```
> 
> without rebuilding the whole app every time.
> 
> So yes — **this screenshot is important.**
> 
> This is not just “Cadence has settings.”  
> This is **Cadence showing us how to make QiLife configurable without turning it into chaos soup.**

### User
> Ran command: `git diff --name-only HEAD~1 HEAD`
> Searched for "_create_qilife_alpha_core.sql"
> Ran command: `Get-ChildItem -Recurse -Filter "*_create_qilife_alpha_core.sql" -ErrorAction SilentlyContinue | Select-Object FullName`
> Ran command: `Get-ChildItem -Recurse -Filter "*.sql" -ErrorAction SilentlyContinue | Select-Object FullName`
> Ran command: `git log -n 50 --oneline`
> Listed directory db
> Viewed qilife_markdown_entity_contract.md:1-334
> Listed directory api
> Listed directory routes
> Listed directory core
> Viewed config.py:1-41
> Viewed .env.local
> Viewed .env.production:1-2
> Used tool: list_permissions
> Used MCP tool: supabase/get_project_url
> Used MCP tool: supabase/list_migrations
> Ran command: `Get-ChildItem -Recurse -Filter "*migration*" -ErrorAction SilentlyContinue | Select-Object FullName`
> Listed directory alembic
> Viewed models.py:1-272
> Ran command: `Get-ChildItem -Recurse -Filter "*supabase*" -ErrorAction SilentlyContinue | Select-Object FullName`
> Listed directory __pycache__
> Ran command: `git log --grep="migration" --oneline`
> Ran command: `git log -p -S "CREATE TABLE" --oneline`
> Ran command: `Get-ChildItem -Recurse -Filter "*.sql" -Force -ErrorAction SilentlyContinue | Select-Object FullName`
> Ran command: `git log --all --grep="qilife_alpha_core" --oneline`
> Ran command: `git branch -a`
> Ran command: `Get-ChildItem -Recurse -Filter "*alpha*" -ErrorAction SilentlyContinue | Select-Object FullName`
> Ran command: `Get-ChildItem -Recurse -Filter "*core*" -ErrorAction SilentlyContinue | Select-Object FullName`
> Ran command: `Get-ChildItem -Recurse -Filter "*.md" -ErrorAction SilentlyContinue | Select-Object FullName`
> Ran command: `git log --all --name-only | Select-String "\.sql"`
> Ran command: `git branch -a --contains 7015752`
> Viewed ADR-0001_cadence_as_qilife_workbench_reference.md:1-125
> Viewed cadence_reference_analysis.md:1-303
> Viewed package.json:1-25
> Listed directory services
> Viewed types.ts:1-205
> Used MCP tool: supabase/list_tables
> Ran command: `supabase status`
> Ran command: `git status --short; git branch --show-current`
> Viewed qilife_markdown_entity_contract.md:190-250
> Edited 20260616183000_create_qilife_alpha_core.sql
> Viewed 20260616183000_create_qilife_alpha_core.sql:1-81
> Viewed 20260616183000_create_qilife_alpha_core.sql:1-81
> Used MCP tool: supabase/execute_sql
> Edited qilife_alpha_fake_seed.sql
> Viewed qilife_alpha_fake_seed.sql:1-82
> Used MCP tool: supabase/execute_sql
> Used MCP tool: supabase/execute_sql
> Used MCP tool: supabase/execute_sql
> Viewed client.ts:1-50
> Viewed main.tsx:1-15
> Used MCP tool: supabase/get_publishable_keys
> Edited README.md
> Edited entityTypes.ts
> Edited entityQueries.ts
> Edited AlphaWorkbenchPage.tsx
> Viewed App.tsx:70-136
> Edited App.tsx
> Viewed App.tsx:1-25
> Edited App.tsx
> Viewed App.tsx:1-5
> Edited App.tsx
> Ran command: `npm run build`
> Used tool: schedule
> Viewed task-195.log:1-6
> Used tool: schedule
> Viewed task-195.log:1-7
> Used tool: schedule
> Viewed task-195.log:1-7
> Used tool: manage_task
> Used tool: schedule
> Viewed vizvibe.mmd:1-121
> Edited vizvibe.mmd
> Ran command: `git status --short`
> Ran command: `git diff --stat`
> Ran command: `git add -A; git commit -m "create qilife alpha workbench schema prototype"`
> Ran command: `git push`
> 
> Here is the final report for the completion of Phase 2:
> 
> ### 📊 Phase 2 Implementation Summary
> 
> - **Current Branch**: `alpha/qicadence`
> - **Migration Applied**: **Yes**. Staged safely without destructive drops, creating `qilife_buckets`, `qilife_entities`, and `qilife_entity_relationships` tables.
> - **Supabase Environment**: QiLife Alpha/Dev (`https://emnskvvajdlqixwzjfsm.supabase.co`).
> - **Seed Applied**: **Yes**. Minimal mock seed successfully executed via public REST connection.
> - **Fake Rows Created**:
>   - `qibit`: 1
>   - `document`: 1
>   - `thread`: 2 (1 project, 1 health matter)
>   - `person`: 1 (Dr. Alice Vance)
>   - `company`: 1 (Apex Innovators Inc)
>   - `action`: 2 (1 task, 1 reminder)
>   - `activity`: 1
>   - `relationships`: 3 (linking threads to contacts and action items)
> - **Isolated Alpha Route**: `/alpha/qilife-workbench` (renders the custom read-only stats, dashboard card metrics, entity lists, and relationship arrows).
> - **Compilation Status**: **App still builds** (`npm run build` completed cleanly in 9.88s).
> - **Files Created/Changed**:
>   - `supabase/migrations/20260616183000_create_qilife_alpha_core.sql` (Schema DDL)
>   - `supabase/seed/qilife_alpha_fake_seed.sql` (Idempotent mock insert statements)
>   - `frontend/src/features/alpha_qilife_workbench/` (Feature directory with `README.md`, `entityTypes.ts`, `entityQueries.ts`, and component views)
>   - `frontend/src/App.tsx` (Route integration with lazy-loaded Suspense entry point)
>   - `vizvibe.mmd` (Updated visual context mapping)
> 
> ---
> 
> ### ⚠️ Remaining Risks & Recommended Next Steps
> 
> 1. **Client-side Credentials Security**: The Supabase client connection is established directly using the public `anon` key inside `entityQueries.ts`. Safe for an alpha/dev environment, but moving forward we will ensure environment variables control all API target configurations.
> 2. **Read-Only Lock**: No write functions are wired up yet to sync local UI interactions back to the database.
> 3. **Next Recommended Step**: Implement the **write path/crud mutation handlers** to sync state back to Supabase tables from the workbench surface (whilst keeping actual user/personal data strictly isolated).

### Assistant
> Okay. Good news: **Phase 2 shipped.**
> 
> Bad news: the agent’s “next recommended step” is **wrong**.
> 
> Do **not** go straight to CRUD/write handlers yet. That is how you accidentally create a public editable life database with a cute UI and no brakes.
> 
> ## My read of what happened
> 
> ### Good
> 
> - Branch: `alpha/qicadence`
> - Supabase alpha/dev project used
> - Migration applied
> - Fake seed applied
> - Read-only alpha route created: `/alpha/qilife-workbench`
> - App builds
> - Work committed and pushed
> 
> That is a real milestone. We now have:
> 
> ```text
> Cadence-inspired UI pattern
> → QiLife alpha database
> → fake data
> → read-only workbench route
> ```
> 
> That’s valid.
> 
> ## But three things need attention
> 
> ### 1. It applied Supabase changes
> 
> That’s okay **only because it says alpha/dev**, but we need to verify the schema and RLS now. No guessing.
> 
> ### 2. It used only broad tables
> 
> It created:
> 
> ```text
> qilife_buckets
> qilife_entities
> qilife_entity_relationships
> ```
> 
> That is more of an **entity registry model**, not the full table model we originally listed.
> 
> That may actually be fine for alpha, but we need to decide:
> 
> | Model | Meaning |
> |---|---|
> | Generic entity model | Flexible, fast, Cadence-like |
> | Dedicated tables | Better for finance/care/legal precision |
> | Hybrid | Best long-term |
> 
> My vote: **hybrid**, but alpha can stay generic for now.
> 
> ### 3. It says next step is CRUD
> 
> Nope. Next step is:
> 
> ```text
> Audit → secure → document → verify read-only → then design controlled write path
> ```
> 
> Not CRUD yet.
> 
> ## Immediate next command
> 
> Run this locally:
> 
> ```powershell
> git status --short
> git log -1 --oneline
> ```
> 
> We want clean status.
> 
> Then open the alpha route and test:
> 
> ```text
> /alpha/qilife-workbench
> ```
> 
> Make sure it loads fake data only.
> 
> ## Tell the IDE agent this next
> 
> Use this. This is the **audit/lockdown phase**, not new feature phase.
> 
> :::writing{variant="standard" id="62914"}
> You are working inside:
> 
> C:\QiLabs\60_QiApps\52_QiApp_QiLife
> 
> Branch:
> 
> alpha/qicadence
> 
> Phase 2 is complete. Now perform Phase 2.5: audit, security review, and schema alignment.
> 
> Do not build CRUD yet.
> 
> Hard rules:
> 1. Do not add create/update/delete UI yet.
> 2. Do not migrate real data.
> 3. Do not add two-way sync.
> 4. Do not expose private data.
> 5. Do not store Supabase keys directly in source files.
> 6. Do not make new database changes until the current schema is reviewed.
> 7. Do not read or print secrets from .env files.
> 
> Tasks:
> 
> 1. Confirm Git state:
> Run:
> git status --short
> git log -1 --oneline
> git branch --show-current
> 
> Report whether the branch is clean.
> 
> 2. Review the migration:
> Open:
> supabase/migrations/20260616183000_create_qilife_alpha_core.sql
> 
> Create a review document:
> docs/architecture/qilife_alpha_schema_review.md
> 
> Include:
> - exact tables created
> - exact columns created
> - indexes created
> - triggers created
> - RLS enabled or not
> - policies created or not
> - whether tables are in public schema or another schema
> - whether anon users can read/write
> - whether the schema matches the Markdown entity contract
> - gaps compared to the Cadence-style custom property model
> 
> 3. Review Supabase security:
> Using Supabase metadata/tools only, verify:
> - tables created
> - RLS status for each table
> - policies for each table
> - whether anon key can select fake data
> - whether anon key can insert/update/delete
> - whether service role key is used anywhere in frontend code
> 
> Do not expose key values in the report.
> 
> 4. Fix frontend Supabase config:
> Inspect:
> frontend/src/features/alpha_qilife_workbench/entityQueries.ts
> or wherever the Supabase client is being used.
> 
> If the Supabase URL or anon key is hardcoded in source, replace them with environment variables using the project’s existing Vite/env convention.
> 
> Use something like:
> VITE_SUPABASE_URL
> VITE_SUPABASE_ANON_KEY
> 
> Do not commit actual key values.
> 
> Update documentation with required env var names only.
> 
> 5. Confirm read-only behavior:
> Verify the alpha workbench only performs SELECT/read operations.
> Report every Supabase operation used by the alpha feature.
> 
> 6. Schema alignment:
> Compare current DB model:
> - qilife_buckets
> - qilife_entities
> - qilife_entity_relationships
> 
> against the planned model:
> - entity_types
> - entity_property_definitions
> - navigation_pages
> - entity_view_configs
> - entities
> - entity_relationships
> - source_documents
> - import_batches
> - optional future domain tables
> 
> Recommend whether to:
> A. keep current generic model for alpha,
> B. add config tables in a second migration,
> C. replace current model before going further.
> 
> Do not apply the recommendation yet.
> 
> 7. Update docs:
> Create or update:
> docs/architecture/qilife_alpha_schema_review.md
> docs/architecture/qilife_alpha_security_review.md
> docs/architecture/qilife_alpha_next_steps.md
> 
> 8. Build:
> Run:
> npm run build
> 
> 9. Commit:
> If only docs/env-safe code changes were made, commit with:
> 
> git add -A
> git commit -m "review and secure qilife alpha workbench schema"
> git push
> 
> 10. Final report:
> Report:
> - branch
> - git status
> - tables audited
> - RLS status
> - whether anon can write
> - whether frontend keys are env-based
> - whether app builds
> - files changed
> - recommended next step
> :::
> 
> ## What comes after the audit
> 
> Only after the audit says:
> 
> ```text
> RLS safe
> anon cannot write
> frontend uses env vars
> read-only confirmed
> fake data only
> schema documented
> ```
> 
> Then the next phase is **not full CRUD**.
> 
> It is:
> 
> ## Phase 3: Config Tables + Cadence Customization Model
> 
> Because your screenshot showed the important thing: Cadence supports configurable entity properties and custom nav pages.
> 
> So next we add:
> 
> ```text
> entity_types
> entity_property_definitions
> navigation_pages
> entity_view_configs
> ```
> 
> Then QiLife can render fields dynamically instead of hardcoding everything.
> 
> ## The correct next roadmap
> 
> ```text
> Phase 2.5 — Audit/security/schema review
> Phase 3 — Add configurable metadata tables
> Phase 4 — Build read-only config-driven workbench UI
> Phase 5 — Markdown/frontmatter importer, one-way
> Phase 6 — controlled write path
> Phase 7 — real data migration
> ```
> 
> ## Bottom line
> 
> The agent did useful work. But its “let’s build CRUD now” suggestion is premature.
> 
> We are not giving the raccoon a credit card yet.  
> First we check the locks.

### User
> I think even like for now this solves like a major issues and its almost like we found eachother, i can keep markdown text as it is and use cadence, and still do all my other backend stuff without worrying about the front end, so i can test this a bit how could i do the front matter yaml and stuff to really see what cadence would be like using and then i take my time on my own app or how good of an idea is what we are diong essentially mapping cadence to our backend?

### Assistant
> Yes. **This is a very good idea — as long as we name it correctly.**
> 
> What we found is not “Cadence replaces QiLife.”
> 
> What we found is:
> 
> > **Cadence can be your usable Markdown workbench today, while QiLife/Supabase becomes the durable backend mirror over time.**
> 
> That solves a huge frontend problem. You can start **living in the system now** instead of waiting for your custom app to become perfect. That aligns with the QiAccess doctrine: the goal is not to build more apps; the goal is one coherent operating system where you can see what exists, know where to go, and manage real life without chaos. fileciteturn8file0
> 
> ## The clean architecture
> 
> Use this mental model:
> 
> | Layer | Job |
> |---|---|
> | **Cadence in Obsidian** | Your usable daily workbench now |
> | **Markdown files** | Human-readable portable records |
> | **YAML frontmatter** | Structured fields Cadence and scripts can read |
> | **Supabase/Postgres** | Durable indexed backend mirror |
> | **QiLife app** | Your custom long-term front door/workbench |
> | **Drive/QiNexus/blob storage** | PDFs, exports, screenshots, evidence, attachments |
> 
> So yes:
> 
> ```text
> Cadence = front-end/workbench now
> Markdown = portable source layer
> Supabase = durable structured mirror
> QiLife = custom app later
> ```
> 
> That is not duct tape. That is actually elegant.
> 
> ## The key rule
> 
> For now:
> 
> > **Markdown/Cadence is the place you work. Supabase mirrors it.**
> 
> Not two-way yet.
> 
> Do **not** make Supabase and Markdown both equally editable yet. That becomes a sync demon.
> 
> ---
> 
> # How to test Cadence properly
> 
> Do a small real-feeling test. Not your whole life. Not 10,000 records. Just enough to feel the workflow.
> 
> ## Create this structure in your vault
> 
> Use Cadence’s expected folders first, because that lets you test the plugin without fighting it:
> 
> ```text
> Cadence/
>   Contacts/
>   Companies/
>   Projects/
>   Pipeline/
>   Activities/
>   Inbox/
> ```
> 
> Later we can rename/customize to `QiLife/People`, `QiLife/Matters`, etc. But first, make Cadence happy and see how it feels.
> 
> ---
> 
> # Starter frontmatter examples
> 
> ## 1. Project example
> 
> File:
> 
> ```text
> Cadence/Projects/Mom Care Plan.md
> ```
> 
> ```yaml
> ---
> id: project_mom_care_plan_001
> type: project
> name: Mom Care Plan
> status: active
> priority: high
> owner: "[[Cody]]"
> due: 2026-06-30
> tags:
>   - mom-care
>   - health
>   - operations
> related_contacts:
>   - "[[Dr Alice Vance]]"
> related_companies:
>   - "[[Humana]]"
> source: obsidian
> sync_status: local-first
> created_at: 2026-06-16
> updated_at: 2026-06-16
> custom_fields:
>   domain: care
>   risk_level: high
>   next_review_date: 2026-06-20
> ---
> ```
> 
> ```markdown
> ## Brief
> 
> Central operating plan for Mom’s care, appointments, medication questions, supplies, insurance issues, and follow-ups.
> 
> ## Scope
> 
> - Track contacts
> - Track open care issues
> - Track appointments
> - Track documents
> - Track follow-ups
> 
> ## Risks
> 
> - Missed medication changes
> - Unclear responsibility
> - Insurance delays
> - Hospital discharge confusion
> 
> ## Notes
> 
> ```
> 
> ---
> 
> ## 2. Contact example
> 
> File:
> 
> ```text
> Cadence/Contacts/Dr Alice Vance.md
> ```
> 
> ```yaml
> ---
> id: person_dr_alice_vance_001
> type: contact
> name: Dr Alice Vance
> status: active
> priority: high
> role: Primary Care Doctor
> email: ""
> phone: ""
> company: "[[Example Clinic]]"
> projects:
>   - "[[Mom Care Plan]]"
> tags:
>   - medical
>   - mom-care
> source: obsidian
> sync_status: local-first
> created_at: 2026-06-16
> updated_at: 2026-06-16
> custom_fields:
>   entity_kind: person
>   preferred_contact_method: phone
>   next_follow_up: 2026-06-20
> ---
> ```
> 
> ```markdown
> ## Summary
> 
> Primary care contact for Mom’s care coordination.
> 
> ## Notes
> 
> ## Questions
> 
> - Confirm medication list.
> - Confirm recent hospital discharge instructions.
> - Confirm oxygen/supply plan.
> ```
> 
> ---
> 
> ## 3. Company / organization example
> 
> File:
> 
> ```text
> Cadence/Companies/Humana.md
> ```
> 
> ```yaml
> ---
> id: org_humana_001
> type: company
> name: Humana
> status: active
> priority: high
> website: ""
> phone: ""
> tags:
>   - insurance
>   - mom-care
> source: obsidian
> sync_status: local-first
> created_at: 2026-06-16
> updated_at: 2026-06-16
> custom_fields:
>   entity_kind: organization
>   insurance_type: medicare_advantage
>   member_related: true
> ---
> ```
> 
> ```markdown
> ## Summary
> 
> Insurance organization related to Mom’s care plan, approvals, denials, benefits, and plan coordination.
> 
> ## Notes
> 
> ## Related Issues
> 
> ```
> 
> ---
> 
> ## 4. Matter / pipeline example
> 
> Cadence calls this `Pipeline` or `Deals`, but for you, use it as **matters/workstreams**.
> 
> File:
> 
> ```text
> Cadence/Pipeline/Humana Care Plan Follow Up.md
> ```
> 
> ```yaml
> ---
> id: matter_humana_care_plan_follow_up_001
> type: deal
> name: Humana Care Plan Follow Up
> stage: active
> status: active
> priority: high
> value: 0
> company: "[[Humana]]"
> contact: "[[Dr Alice Vance]]"
> project: "[[Mom Care Plan]]"
> tags:
>   - insurance
>   - care-plan
>   - follow-up
> source: obsidian
> sync_status: local-first
> created_at: 2026-06-16
> updated_at: 2026-06-16
> custom_fields:
>   entity_kind: matter
>   matter_type: care_insurance
>   deadline: 2026-06-21
>   desired_outcome: written care plan confirmation
> ---
> ```
> 
> ```markdown
> ## Summary
> 
> Follow-up matter for confirming what Humana should have provided, what care plan exists, and what next action is required.
> 
> ## Timeline
> 
> ## Evidence
> 
> ## Next Action
> 
> Call Humana and ask for written care plan / case management documentation.
> ```
> 
> ---
> 
> ## 5. Activity / interaction example
> 
> File:
> 
> ```text
> Cadence/Activities/2026-06-16 Call With Humana.md
> ```
> 
> ```yaml
> ---
> id: activity_20260616_call_humana_001
> type: activity
> name: 2026-06-16 Call With Humana
> status: logged
> activity_type: call
> date: 2026-06-16
> company: "[[Humana]]"
> project: "[[Mom Care Plan]]"
> matter: "[[Humana Care Plan Follow Up]]"
> contacts: []
> tags:
>   - call
>   - insurance
>   - mom-care
> source: obsidian
> sync_status: local-first
> created_at: 2026-06-16
> updated_at: 2026-06-16
> custom_fields:
>   outcome: pending
>   follow_up_required: true
> ---
> ```
> 
> ```markdown
> ## Summary
> 
> Called Humana about care plan coordination.
> 
> ## What Happened
> 
> ## Promises Made
> 
> ## Follow Up
> 
> ```
> 
> ---
> 
> # The field naming strategy
> 
> Use two layers:
> 
> ## Cadence-compatible fields
> 
> These are fields Cadence likely expects:
> 
> ```yaml
> name:
> status:
> priority:
> stage:
> company:
> contact:
> project:
> tags:
> due:
> date:
> value:
> ```
> 
> ## QiLife durable fields
> 
> These are your system fields:
> 
> ```yaml
> id:
> type:
> source:
> sync_status:
> created_at:
> updated_at:
> custom_fields:
> ```
> 
> That gives you both:
> 
> ```text
> Cadence can read it now.
> QiLife/Supabase can map it later.
> ```
> 
> That is the trick.
> 
> ---
> 
> # How this maps to Supabase
> 
> Each Markdown note becomes one row in `qilife_entities`.
> 
> Example:
> 
> | Markdown | Supabase |
> |---|---|
> | `id` | `stable_id` or `external_id` |
> | `type` | `entity_type` |
> | `name` | `title` |
> | `status` | `status` |
> | `tags` | `tags` / `custom_fields.tags` |
> | whole YAML | `frontmatter_json` |
> | markdown body | `body_markdown` |
> | file path | `markdown_path` |
> | wikilinks | `qilife_entity_relationships` |
> 
> So this:
> 
> ```yaml
> project: "[[Mom Care Plan]]"
> company: "[[Humana]]"
> ```
> 
> eventually becomes:
> 
> ```text
> Humana Care Plan Follow Up
> → related_to
> Mom Care Plan
> 
> Humana Care Plan Follow Up
> → involves
> Humana
> ```
> 
> That is exactly the bridge.
> 
> ---
> 
> # How good is this idea?
> 
> ## Very good — with boundaries.
> 
> This is probably one of the better architecture turns we’ve made because it gives you:
> 
> - immediate usability
> - portable Markdown
> - a low-friction front end
> - backend independence
> - Obsidian compatibility
> - Supabase durability later
> - no waiting for a custom UI before using the system
> 
> It also avoids the classic trap:
> 
> > “I need to build my perfect app before I can organize my life.”
> 
> No, ma’am. That trap eats years.
> 
> Cadence lets you start now.
> 
> ## But here’s the warning
> 
> Cadence should not become the **only** source of truth for everything forever.
> 
> It is great for:
> 
> ```text
> people
> projects
> matters
> activities
> notes
> follow-ups
> light tasks
> daily planning
> ```
> 
> It is not enough by itself for:
> 
> ```text
> finance ledger integrity
> medication safety tracking
> legal evidence chain
> permissioned family access
> audit logs
> multi-user approval workflows
> structured reporting at scale
> ```
> 
> That stuff belongs in Supabase/QiLife later.
> 
> ---
> 
> # What I’d do today
> 
> ## Test with 10 notes only
> 
> Create:
> 
> ```text
> 2 Contacts
> 2 Companies
> 2 Projects
> 2 Pipeline/Matters
> 2 Activities
> ```
> 
> Then use Cadence for a full day.
> 
> Track:
> 
> ```text
> Can I find things fast?
> Can I capture fast?
> Do links feel natural?
> Do statuses make sense?
> Do I know what to click?
> Does it reduce friction?
> ```
> 
> If yes, we lock Cadence in as the **Obsidian workbench layer**.
> 
> ---
> 
> # Suggested status values
> 
> Keep these boring and consistent.
> 
> ## General statuses
> 
> ```yaml
> status: active
> ```
> 
> Options:
> 
> ```text
> active
> on_hold
> waiting
> done
> archived
> ```
> 
> ## Priority
> 
> ```yaml
> priority: high
> ```
> 
> Options:
> 
> ```text
> low
> medium
> high
> urgent
> ```
> 
> ## Matter stage
> 
> ```yaml
> stage: active
> ```
> 
> Options:
> 
> ```text
> inbox
> active
> waiting
> blocked
> resolved
> archived
> ```
> 
> ## Activity status
> 
> ```yaml
> status: logged
> ```
> 
> Options:
> 
> ```text
> planned
> logged
> needs_follow_up
> closed
> ```
> 
> ---
> 
> # The doctrine
> 
> Use this:
> 
> ```text
> Cadence is the working cockpit.
> Markdown is the portable human-readable layer.
> Supabase is the durable mirror.
> QiLife is the long-term custom app.
> ```
> 
> That is the cleanest version of what we’re doing.
> 
> Bottom line: **yes, this is a damn good idea.** It lets you stop waiting on the app and start generating clean structured data today. The custom app can grow from your actual usage instead of your imagination trying to predict every workflow upfront.

### User
> but to actually be able to use it correctly i need to open qilabs as the vault but obsidian wont open so we need to hone in the obsidian ignore, i imagine it like the apps, and node modules chocking it.

### Assistant
> Yes. **You’re diagnosing it correctly.** Opening all of `C:\QiLabs` as an Obsidian vault means Obsidian is probably choking on repo garbage: `node_modules`, `.git`, build folders, screenshots, caches, Python envs, etc.
> 
> Obsidian’s built-in excluded files setting is stored in `.obsidian/app.json` under `userIgnoreFilters`, and examples specifically show `/node_modules/` there. citeturn663720search7turn663720search0 The annoying truth: Obsidian’s built-in exclusion can behave like a soft exclude, so for giant dev folders it may not fully solve every indexing problem; File Ignore / Advanced Exclude-style plugins use a stronger dot-prefix/hidden-folder approach. citeturn663720search1turn663720search8
> 
> ## The immediate fix
> 
> Create the Obsidian config **before opening Obsidian**.
> 
> Run this in PowerShell:
> 
> ```powershell
> cd C:\QiLabs
> 
> New-Item -ItemType Directory -Force .obsidian | Out-Null
> 
> $appJsonPath = ".obsidian\app.json"
> 
> if (Test-Path $appJsonPath) {
>   Copy-Item $appJsonPath ".obsidian\app.backup.$((Get-Date).ToString('yyyyMMddHHmmss')).json"
>   $app = Get-Content $appJsonPath -Raw | ConvertFrom-Json
> } else {
>   $app = [PSCustomObject]@{}
> }
> 
> $ignore = @(
>   "/node_modules/",
>   "/\.git/",
>   "/\.next/",
>   "/dist/",
>   "/build/",
>   "/coverage/",
>   "/out/",
>   "/target/",
>   "/\.turbo/",
>   "/\.vite/",
>   "/\.cache/",
>   "/\.pnpm-store/",
>   "/\.yarn/",
>   "/\.venv/",
>   "/venv/",
>   "/env/",
>   "/__pycache__/",
>   "/\.pytest_cache/",
>   "/\.mypy_cache/",
>   "/\.ruff_cache/",
>   "/\.idea/",
>   "/\.vscode/",
>   "/\.supabase/",
>   "/\.vercel/",
>   "/\.netlify/",
>   "/logs/",
>   "/tmp/",
>   "/temp/",
>   "/reference/obsidian-cadence/docs/screenshots/",
>   "/QiCadence/docs/screenshots/"
> )
> 
> $app | Add-Member -NotePropertyName userIgnoreFilters -NotePropertyValue $ignore -Force
> 
> $app | ConvertTo-Json -Depth 10 | Set-Content $appJsonPath -Encoding UTF8
> 
> Get-Content $appJsonPath
> ```
> 
> Then open Obsidian and choose:
> 
> ```text
> C:\QiLabs
> ```
> 
> as the vault.
> 
> ## After Obsidian opens
> 
> Go to:
> 
> ```text
> Settings → Files and links
> ```
> 
> Then check:
> 
> ```text
> Excluded files
> ```
> 
> Make sure the ignore list is there.
> 
> Also turn off:
> 
> ```text
> Detect all file extensions
> ```
> 
> That keeps Obsidian from trying to be cute and showing every random code/config file.
> 
> ## The cleaner long-term pattern
> 
> For `C:\QiLabs` as vault, your Obsidian rule should be:
> 
> ```text
> Index Markdown, docs, templates, notes, and Cadence entities.
> Ignore build artifacts, dependencies, caches, screenshots, binary blobs, and repo internals.
> ```
> 
> So we keep visible:
> 
> ```text
> docs/
> prototypes/
> *.md
> Cadence/
> QiLife/
> .obsidian/plugins/cadence-planner/
> ```
> 
> And suppress:
> 
> ```text
> node_modules/
> .git/
> dist/
> build/
> .cache/
> .venv/
> __pycache__/
> screenshots/
> ```
> 
> ## Tell the IDE agent this
> 
> :::writing{variant="standard" id="20864"}
> We need to make C:\QiLabs usable as an Obsidian vault without Obsidian choking on development folders.
> 
> Goal:
> Create or update C:\QiLabs\.obsidian\app.json with safe userIgnoreFilters for repo/build/dependency/cache folders.
> 
> Hard rules:
> 1. Do not delete any project files.
> 2. Do not move app folders.
> 3. Do not rename node_modules, .git, or source folders.
> 4. Do not install plugins yet.
> 5. Back up any existing .obsidian/app.json before editing.
> 6. Preserve existing app.json settings where possible.
> 7. Only add/update userIgnoreFilters.
> 
> Add these ignore patterns:
> - /node_modules/
> - /\.git/
> - /\.next/
> - /dist/
> - /build/
> - /coverage/
> - /out/
> - /target/
> - /\.turbo/
> - /\.vite/
> - /\.cache/
> - /\.pnpm-store/
> - /\.yarn/
> - /\.venv/
> - /venv/
> - /env/
> - /__pycache__/
> - /\.pytest_cache/
> - /\.mypy_cache/
> - /\.ruff_cache/
> - /\.idea/
> - /\.vscode/
> - /\.supabase/
> - /\.vercel/
> - /\.netlify/
> - /logs/
> - /tmp/
> - /temp/
> - /reference/obsidian-cadence/docs/screenshots/
> - /QiCadence/docs/screenshots/
> 
> After editing:
> 1. Print the final .obsidian/app.json.
> 2. Confirm it is valid JSON.
> 3. Report whether app.json was created or updated.
> 4. Report backup path if one was created.
> :::
> 
> ## My recommendation
> 
> Start with the built-in `userIgnoreFilters` first. If Obsidian still opens slow or freezes, then install **File Ignore** or **Advanced Exclude** and hard-hide `node_modules`, `.git`, and build folders.
> 
> Do not hard-hide real QiLabs folders yet. We only hide obvious junk first. That keeps the vault useful without making your system disappear from itself.

### User
> this is what is currently there. {
>   "alwaysUpdateLinks": true,
>   "showUnsupportedFiles": true,
>   "promptDelete": false,
>   "showInlineTitle": false
> }

### Assistant
> Yes — that file is tiny and easy to fix.
> 
> Your current issue is probably this:
> 
> ```json
> "showUnsupportedFiles": true
> ```
> 
> That tells Obsidian to care about way more repo junk than it needs to. For `C:\QiLabs`, that should be **false**.
> 
> Replace your `.obsidian/app.json` with this:
> 
> :::writing{variant="standard" id="61482"}
> {
>   "alwaysUpdateLinks": true,
>   "showUnsupportedFiles": false,
>   "promptDelete": false,
>   "showInlineTitle": false,
>   "userIgnoreFilters": [
>     "/node_modules/",
>     "/\\.git/",
>     "/\\.next/",
>     "/dist/",
>     "/build/",
>     "/coverage/",
>     "/out/",
>     "/target/",
>     "/\\.turbo/",
>     "/\\.vite/",
>     "/\\.cache/",
>     "/\\.pnpm-store/",
>     "/\\.yarn/",
>     "/\\.venv/",
>     "/venv/",
>     "/env/",
>     "/__pycache__/",
>     "/\\.pytest_cache/",
>     "/\\.mypy_cache/",
>     "/\\.ruff_cache/",
>     "/\\.idea/",
>     "/\\.vscode/",
>     "/\\.supabase/",
>     "/\\.vercel/",
>     "/\\.netlify/",
>     "/logs/",
>     "/tmp/",
>     "/temp/",
>     "/reference/obsidian-cadence/docs/screenshots/",
>     "/QiCadence/docs/screenshots/"
>   ]
> }
> :::
> 
> ## Fast PowerShell way
> 
> From `C:\QiLabs`:
> 
> ```powershell
> cd C:\QiLabs
> 
> Copy-Item .obsidian\app.json ".obsidian\app.backup.$((Get-Date).ToString('yyyyMMddHHmmss')).json"
> 
> @'
> {
>   "alwaysUpdateLinks": true,
>   "showUnsupportedFiles": false,
>   "promptDelete": false,
>   "showInlineTitle": false,
>   "userIgnoreFilters": [
>     "/node_modules/",
>     "/\\.git/",
>     "/\\.next/",
>     "/dist/",
>     "/build/",
>     "/coverage/",
>     "/out/",
>     "/target/",
>     "/\\.turbo/",
>     "/\\.vite/",
>     "/\\.cache/",
>     "/\\.pnpm-store/",
>     "/\\.yarn/",
>     "/\\.venv/",
>     "/venv/",
>     "/env/",
>     "/__pycache__/",
>     "/\\.pytest_cache/",
>     "/\\.mypy_cache/",
>     "/\\.ruff_cache/",
>     "/\\.idea/",
>     "/\\.vscode/",
>     "/\\.supabase/",
>     "/\\.vercel/",
>     "/\\.netlify/",
>     "/logs/",
>     "/tmp/",
>     "/temp/",
>     "/reference/obsidian-cadence/docs/screenshots/",
>     "/QiCadence/docs/screenshots/"
>   ]
> }
> '@ | Set-Content .obsidian\app.json -Encoding UTF8
> ```
> 
> ## Then reopen Obsidian
> 
> Open:
> 
> ```text
> C:\QiLabs
> ```
> 
> as the vault.
> 
> If it still chokes, the next step is a stronger ignore plugin, but don’t jump there yet. First fix the obvious problem: **stop showing unsupported files and ignore repo/build folders.**

### User
> even ignoring all that it still wont load, can you look online and see the best way to handle this? other wise we may have to think about how we handle the obsidian vault without getting silod out of the other data.

### Assistant
> Yes — after checking, the answer is pretty clear:
> 
> ## Do **not** open `C:\QiLabs` as the Obsidian vault.
> 
> That is the wrong battlefield.
> 
> You were right that `node_modules`, app repos, `.git`, build outputs, screenshots, cache folders, etc. are choking it. But the deeper issue is that Obsidian’s normal “Excluded files” setting is not a true `.gitignore`-style hard ignore. People have been reporting this exact dev-repo problem for years: one forum post describes a monorepo with `node_modules` containing **250k files and 6,000 Markdown files**, and Obsidian choking even when users tried exclusion rules. citeturn197063view3
> 
> There are plugins like **File Ignore** and **Advanced Exclude** that try to hard-exclude folders. File Ignore says it helps avoid lag by hiding folders with dot-prefix behavior, and Advanced Exclude says it can truly remove folders from Obsidian’s index and file panes. citeturn197063view1turn197063view2 But here’s the problem: **if Obsidian cannot open the vault reliably, plugins are not the foundation.** They are a bandage after the patient is already on the floor.
> 
> So we stop trying to make all of `QiLabs` be Obsidian.
> 
> ## The better architecture
> 
> Use a **curated Obsidian vault**, not the whole system root.
> 
> Something like:
> 
> ```text
> C:\QiLabs\50_QiNexus\My Drive\13_system\obsidian\QiLife_Workbench_Vault
> ```
> 
> or shorter:
> 
> ```text
> C:\QiLabs\50_QiNexus\My Drive\QiLife_Workbench
> ```
> 
> That vault contains only:
> 
> ```text
> 00_inbox/
> 01_daily/
> 02_people/
> 03_projects/
> 04_matters/
> 05_care/
> 06_finance/
> 07_legal/
> 08_tech/
> 09_files/
> 10_templates/
> Cadence/
> .obsidian/
> ```
> 
> And it **does not contain**:
> 
> ```text
> node_modules/
> .git/
> dist/
> build/
> Supabase local cache/
> app repos/
> binary screenshots/
> random exported junk/
> ```
> 
> This keeps Obsidian fast, while QiLabs stays the real system.
> 
> ## “But I don’t want it siloed”
> 
> Correct. We do **not** silo it.
> 
> We connect it through IDs, links, and sync.
> 
> ### Vault role
> 
> ```text
> Obsidian / Cadence = human workbench
> ```
> 
> ### QiLabs role
> 
> ```text
> QiLabs = apps, repos, server code, architecture, migrations
> ```
> 
> ### QiNexus role
> 
> ```text
> QiNexus / Drive = storage backbone and portable files
> ```
> 
> ### Supabase role
> 
> ```text
> Supabase = durable structured mirror/index
> ```
> 
> So your Obsidian vault becomes a **curated cockpit**, not a separate universe.
> 
> ## The key rule
> 
> Do not put the whole repo inside the vault.
> 
> Instead:
> 
> ```text
> Vault contains clean Markdown entities.
> Markdown entities reference repos/files by path, ID, URL, or Drive link.
> Supabase indexes the frontmatter.
> QiLife app reads the same Supabase data later.
> ```
> 
> That is how we avoid silos.
> 
> ## Example
> 
> A note in the vault:
> 
> ```text
> 04_matters/Humana_Care_Plan_Follow_Up.md
> ```
> 
> Frontmatter:
> 
> ```yaml
> ---
> id: matter_humana_care_plan_follow_up_001
> type: matter
> title: Humana Care Plan Follow Up
> status: active
> priority: high
> source: obsidian
> sync_status: local_first
> qilabs_refs:
>   - path: "C:/QiLabs/60_QiApps/52_QiApp_QiLife"
>     label: "QiLife app repo"
>   - path: "C:/QiLabs/50_QiNexus/My Drive/07_legal"
>     label: "Legal storage bucket"
> supabase_entity_id: ""
> tags:
>   - mom-care
>   - insurance
> created_at: 2026-06-16
> updated_at: 2026-06-16
> ---
> ```
> 
> Body:
> 
> ```markdown
> ## Summary
> 
> Follow-up matter related to care plan documentation and insurance coordination.
> 
> ## Related System Links
> 
> - QiLife app repo: file:///C:/QiLabs/60_QiApps/52_QiApp_QiLife
> - QiNexus legal bucket: file:///C:/QiLabs/50_QiNexus/My%20Drive/07_legal
> 
> ## Notes
> 
> ```
> 
> That gives you access without forcing Obsidian to index the whole damn kingdom.
> 
> ## The practical setup
> 
> ### Step 1 — Create the clean vault
> 
> Run:
> 
> ```powershell
> $vault = "C:\QiLabs\50_QiNexus\My Drive\QiLife_Workbench"
> 
> New-Item -ItemType Directory -Force "$vault\.obsidian" | Out-Null
> New-Item -ItemType Directory -Force "$vault\00_inbox" | Out-Null
> New-Item -ItemType Directory -Force "$vault\01_daily" | Out-Null
> New-Item -ItemType Directory -Force "$vault\02_people" | Out-Null
> New-Item -ItemType Directory -Force "$vault\03_projects" | Out-Null
> New-Item -ItemType Directory -Force "$vault\04_matters" | Out-Null
> New-Item -ItemType Directory -Force "$vault\05_care" | Out-Null
> New-Item -ItemType Directory -Force "$vault\06_finance" | Out-Null
> New-Item -ItemType Directory -Force "$vault\07_legal" | Out-Null
> New-Item -ItemType Directory -Force "$vault\08_tech" | Out-Null
> New-Item -ItemType Directory -Force "$vault\09_files" | Out-Null
> New-Item -ItemType Directory -Force "$vault\10_templates" | Out-Null
> New-Item -ItemType Directory -Force "$vault\Cadence" | Out-Null
> ```
> 
> ### Step 2 — Create app config
> 
> ```powershell
> @'
> {
>   "alwaysUpdateLinks": true,
>   "showUnsupportedFiles": false,
>   "promptDelete": false,
>   "showInlineTitle": false,
>   "userIgnoreFilters": [
>     "/node_modules/",
>     "/\\.git/",
>     "/dist/",
>     "/build/",
>     "/coverage/",
>     "/out/",
>     "/target/",
>     "/\\.cache/",
>     "/\\.vite/",
>     "/\\.turbo/",
>     "/__pycache__/",
>     "/\\.venv/",
>     "/venv/",
>     "/env/",
>     "/logs/",
>     "/tmp/",
>     "/temp/"
>   ]
> }
> '@ | Set-Content "$vault\.obsidian\app.json" -Encoding UTF8
> ```
> 
> ### Step 3 — Open this as the Obsidian vault
> 
> Open:
> 
> ```text
> C:\QiLabs\50_QiNexus\My Drive\QiLife_Workbench
> ```
> 
> Not:
> 
> ```text
> C:\QiLabs
> ```
> 
> ## What about Cadence?
> 
> Install/enable Cadence inside this clean vault.
> 
> Let Cadence create its default folders, or point its settings to your cleaner folders if it supports it.
> 
> For first test, keep it simple:
> 
> ```text
> Cadence/Contacts/
> Cadence/Companies/
> Cadence/Projects/
> Cadence/Pipeline/
> Cadence/Activities/
> Cadence/Inbox/
> ```
> 
> Once it works, we map:
> 
> ```text
> Cadence/Contacts  →  02_people
> Cadence/Projects  →  03_projects
> Cadence/Pipeline  →  04_matters
> Cadence/Activities → activity/interactions
> ```
> 
> ## The long-term bridge
> 
> We create a script later:
> 
> ```text
> QiLife_Workbench Markdown
> → parse YAML/frontmatter
> → upsert into Supabase qilife_entities
> → index relationships from wikilinks
> → preserve markdown_path
> ```
> 
> This means:
> 
> - you work in Obsidian/Cadence
> - the backend gets durable data
> - QiLife app can render it
> - Drive/QiNexus keeps the files portable
> - no giant vault choking
> - no data silo
> 
> ## Do not use symlinks yet
> 
> Obsidian can work with symlinks/junctions, but the docs/search results warn to use them at your own risk and strongly advise caution. citeturn243118search33
> 
> For your system, symlinks are tempting but dangerous because:
> 
> ```text
> one bad linked folder → Obsidian indexes the whole repo again
> ```
> 
> So the better first pattern is:
> 
> ```text
> curated vault + file links + later sync/import scripts
> ```
> 
> Not symlink spaghetti.
> 
> ## My ruling
> 
> The best setup is:
> 
> ```text
> QiLabs root = not an Obsidian vault
> QiLife_Workbench = Obsidian/Cadence vault
> QiNexus/Drive = storage backbone
> Supabase = durable mirror
> QiLife app = future frontend
> ```
> 
> This is cleaner, faster, safer, and not siloed.
> 
> Trying to force all of `C:\QiLabs` into Obsidian is a waste of time. That’s not integration — that’s making Obsidian eat a server closet.

### User
> i was ablel to open up the mydrive or qivault which is weired because its the largest folder yet it opened, so there has to be another issue that causes obsidian not to want to load.

### Assistant
> Yep — **that changes the diagnosis.**
> 
> If `My Drive / QiVault` opens and `C:\QiLabs` doesn’t, this is probably **not just size**. It’s likely one of these:
> 
> | Likely cause | Why |
> |---|---|
> | Broken/cursed `C:\QiLabs\.obsidian` config | Obsidian may be crashing on workspace/plugin/theme state |
> | Plugin crash | Obsidian forum reports blank/black/white vault failures can be plugin-related; one common fix path is disabling plugins first. citeturn755849search1 |
> | Workspace crash | A bad `workspace.json` can make a vault hang on “loading workspace” |
> | Symlink/junction loop | A linked folder may be making Obsidian recurse into hell |
> | Unsupported files being indexed | Excluded files are not always a true hard ignore; users report Obsidian still choking on dev folders even with exclusions. citeturn755849search4 |
> | One specific toxic folder | Could be `node_modules`, `.git`, generated docs, huge screenshots, or a plugin dev folder |
> 
> So now we debug it like adults. Annoying, but clean.
> 
> ---
> 
> # Step 1: Nuke the vault config temporarily
> 
> This is the fastest test.
> 
> Close Obsidian completely.
> 
> Then run:
> 
> ```powershell
> cd C:\QiLabs
> 
> $stamp = Get-Date -Format "yyyyMMddHHmmss"
> 
> if (Test-Path ".obsidian") {
>   Rename-Item ".obsidian" ".obsidian_DISABLED_$stamp"
> }
> 
> New-Item -ItemType Directory -Force ".obsidian" | Out-Null
> 
> @'
> {
>   "alwaysUpdateLinks": true,
>   "showUnsupportedFiles": false,
>   "promptDelete": false,
>   "showInlineTitle": false,
>   "userIgnoreFilters": [
>     "/node_modules/",
>     "/\\.git/",
>     "/\\.next/",
>     "/dist/",
>     "/build/",
>     "/coverage/",
>     "/out/",
>     "/target/",
>     "/\\.turbo/",
>     "/\\.vite/",
>     "/\\.cache/",
>     "/\\.pnpm-store/",
>     "/\\.yarn/",
>     "/\\.venv/",
>     "/venv/",
>     "/env/",
>     "/__pycache__/",
>     "/\\.pytest_cache/",
>     "/\\.mypy_cache/",
>     "/\\.ruff_cache/",
>     "/\\.idea/",
>     "/\\.vscode/",
>     "/\\.supabase/",
>     "/\\.vercel/",
>     "/\\.netlify/",
>     "/logs/",
>     "/tmp/",
>     "/temp/"
>   ]
> }
> '@ | Set-Content ".obsidian\app.json" -Encoding UTF8
> 
> @'
> []
> '@ | Set-Content ".obsidian\community-plugins.json" -Encoding UTF8
> ```
> 
> Then try opening `C:\QiLabs` again.
> 
> ## Read the result
> 
> ### If it opens
> 
> Then the problem was your old `.obsidian` config, plugin, theme, or workspace.
> 
> That means we **do not restore the whole old `.obsidian` folder**. We cherry-pick only safe pieces later.
> 
> ### If it still does not open
> 
> Then the problem is in the folder tree itself: symlink loop, huge unsupported folder, permissions issue, cursed generated folder, etc.
> 
> ---
> 
> # Step 2: Check for symlinks/junctions
> 
> Run:
> 
> ```powershell
> cd C:\QiLabs
> 
> Get-ChildItem -Force -Recurse -ErrorAction SilentlyContinue |
>   Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint } |
>   Select-Object FullName, Attributes
> ```
> 
> If this returns a bunch of linked folders, that may be the real demon.
> 
> Especially watch for links pointing back into:
> 
> ```text
> C:\QiLabs
> C:\Users\codyr
> Google Drive
> OneDrive
> node_modules
> ```
> 
> A symlink loop can make Obsidian think the vault never ends.
> 
> ---
> 
> # Step 3: Find the worst folders
> 
> Run this from `C:\QiLabs`:
> 
> ```powershell
> cd C:\QiLabs
> 
> Get-ChildItem -Directory -Force | ForEach-Object {
>   $path = $_.FullName
>   $files = (Get-ChildItem $path -Recurse -File -Force -ErrorAction SilentlyContinue | Measure-Object).Count
>   [PSCustomObject]@{
>     Folder = $_.Name
>     Files = $files
>   }
> } | Sort-Object Files -Descending | Format-Table -AutoSize
> ```
> 
> This tells us what folder is probably choking it.
> 
> If one app folder has 150k files because of `node_modules`, we isolate that.
> 
> ---
> 
> # Step 4: Test by temporarily hiding suspect folders
> 
> Do **not delete anything**. Rename temporarily.
> 
> Example:
> 
> ```powershell
> cd C:\QiLabs
> 
> Rename-Item "60_QiApps" "_HOLD_60_QiApps"
> ```
> 
> Try opening Obsidian.
> 
> If it opens, the issue is inside `60_QiApps`.
> 
> Then put it back:
> 
> ```powershell
> Rename-Item "_HOLD_60_QiApps" "60_QiApps"
> ```
> 
> Then test subfolders inside `60_QiApps`.
> 
> This is binary search. Boring but effective.
> 
> ---
> 
> # My current bet
> 
> Given your setup, my bet is:
> 
> ## Most likely
> 
> `C:\QiLabs\.obsidian` had a bad workspace/plugin config.
> 
> ## Second likely
> 
> `60_QiApps` or another repo folder has a file-count explosion or symlink/junction issue.
> 
> ## Third likely
> 
> Obsidian is touching unsupported files even though you told it not to, because Obsidian’s built-in exclude is not a perfect hard ignore. People specifically complain that excluded folders can still affect indexing/parsing behavior. citeturn755849search4
> 
> ---
> 
> # Strategic answer
> 
> If the clean `.obsidian` reset fixes it, then yes, we can use `C:\QiLabs` as the vault.
> 
> If it still fails, stop forcing it. Use:
> 
> ```text
> QiNexus / My Drive = Obsidian vault
> QiLabs repos = linked/reference paths
> Supabase = durable mirror
> QiLife app = frontend later
> ```
> 
> That still avoids silos. It just doesn’t make Obsidian eat your whole dev environment like a goat with admin access.
> 
> First test: **rename `.obsidian` and create the clean config.** That tells us which universe we’re in.

### User
> how do i make this really work for me Owner avatar
> obsidian-cadence
> Public
> wesswart77/obsidian-cadence
> Go to file
> t
> T
> Name		
> wesswart77
> wesswart77
> v0.15.0 — analytics widgets + custom entities (PR #4 by @Jumitti); in…
> 035b3de
>  · 
> 2 weeks ago
> .github/workflows
> v0.13.12 — scope entity enumeration to folders; add release attestati…
> last month
> .vscode
> Create new sidebar section "Projects"
> 3 weeks ago
> docs/screenshots
> Initial release of Cadence v0.13.4
> last month
> .gitignore
> Support TaskNotes
> 3 weeks ago
> LICENSE
> Initial release of Cadence v0.13.4
> last month
> README.md
> update REAMDME.md
> 3 weeks ago
> SUBMISSION.md
> Initial release of Cadence v0.13.4
> last month
> main.js
> v0.15.0 — analytics widgets + custom entities (PR #4 by @Jumitti); in…
> 2 weeks ago
> manifest.json
> v0.15.0 — analytics widgets + custom entities (PR #4 by @Jumitti); in…
> 2 weeks ago
> styles.css
> template for daily note
> 3 weeks ago
> versions.json
> v0.15.0 — analytics widgets + custom entities (PR #4 by @Jumitti); in…
> 2 weeks ago
> Repository files navigation
> README
> MIT license
> Cadence — a workspace for working life
> A unified Obsidian plugin for CRM, PRM, project management, daily planning, and reminders — all on top of plain markdown. No server, no sync service, no lock-in. Your vault stays your vault.
> 
> Cadence Home
> 
> Why Cadence
> Most "second brain" plugins do one thing well. Cadence is the opposite: a coherent workspace that brings together the surfaces a working person actually moves between every day — today's tasks, the week ahead, deals in flight, contacts, projects, recurring reminders — and presents them in a single tab with one familiar nav.
> 
> Markdown is the source of truth. Every contact, deal, project, activity is a .md file with frontmatter. Tasks, Dataview, Templater all keep working. Move to a different vault tomorrow — your data goes with you.
> One tab, many surfaces. A left rail lets you flip between Home → Today → Pipeline → Contacts → Projects → Inbox → Reports without ever leaving the Cadence tab.
> Module toggles. Turn off CRM, PRM or Planner if you only want some of it.
> Reminders that fire. A small Inbox + capture modal + ticker = real notifications, not just a tag on a note.
> Features
> Home — your command centre
> Two-column dashboard: today's tasks (tickable inline) · this week's progress · upcoming deadlines · partners due for follow-up · top active projects with milestone progress · pipeline at a glance · recent activity. Optional "open on Obsidian startup" + Homepage plugin compatible.
> 
> Home command centre
> 
> Planner
> Today — diary view of today's daily note with quick-add task and autosaving journal
> Calendar (week) — Mon–Sun grid across daily notes; tick any task from any day
> Projects — status-grouped card grid with milestone progress and next-up dates
> Inbox — universal capture + reminders; items grouped by Now / Today / This Week / Later
> Inbox + reminders
> 
> CRM
> Dashboard — pipeline-by-stage bars, hot deals (top by value), stale deals (no edits in 14+ days), recent activity, customer base mini-stats
> Pipeline — kanban board across deal stages; drag-and-drop a card to update its stage frontmatter; Won column gets a soft emerald tint
> Contacts / Companies / Activities — sortable list views with rich frontmatter editing
> CRM Pipeline kanban
> 
> PRM
> Partners · Registrations · Commissions · Leads · Certifications · Analytics — same entity-list pattern, in their own folders, with status enums and Reports that aggregate across them.
> 
> Project Management
> Click a project, get a real PM surface — not a markdown editor. Hero with status/priority pills, owner, due date, color-banded progress bar. Left column: tickable milestones (date + title + delete on hover) and tasks with + Add buttons. Right column: Brief, Scope, Risks, Stakeholders, Notes — all autosaving textareas writing back to their H2 sections. Open as note for full body editing in Obsidian's editor.
> 
> Project detail
> 
> Reminders
> Quick-capture with Cmd+Shift+I → modal with text, optional datetime, optional repeat (daily/weekly). The plugin ticks every 30 seconds and fires due reminders as in-app notices (and optionally desktop notifications). Snooze 15m / 1h / tomorrow on any reminder. The nav badge shows live overdue count.
> 
> Quick capture
> 
> Reports
> Pipeline · Sales · Partners · Activity · Productivity (over your daily notes — completion %, streaks, journal volume, 14-day done-tasks bar chart).
> 
> New entity capture
> A clean two-column modal for every entity type — type-aware widgets (date pickers, dropdowns for stage/status/priority/tier/type), smart defaults, smart placeholders, primary field marked required. Enter to submit, Esc to cancel.
> 
> New deal modal
> 
> CSV import
> Bring an entire client list, pipeline, or partner roster in from a spreadsheet. Run Cadence: Import from CSV (or hit "Import CSV" on any list view) → pick a .csv from your vault or paste raw text → Cadence auto-maps columns to entity fields by name (with synonyms — Email, email, Email Address all map to email). Override any mapping, see a sample of the first two rows, then import. Each row becomes one markdown file with frontmatter populated.
> 
> CSV import modal
> 
> Install
> Community plugin store (once approved)
> Settings → Community plugins → Browse
> Search "Cadence"
> Install → Enable
> Manual install (works today)
> Download main.js, manifest.json, styles.css from the latest release
> Drop them into <your-vault>/.obsidian/plugins/cadence-planner/
> Settings → Community plugins → Reload → Enable Cadence
> Quick start
> Open the app — Click the ✨ sparkles icon in the left ribbon, or run Open Cadence from the command palette
> Capture a deal — CRM → Pipeline → + New Deal → fill in title, stage, value → Create
> Capture a contact — CRM → Contacts → + New Contact
> Plan a project — Planner → Projects → + New Project → click into it → tick milestones, fill in Brief
> Set a reminder — Cmd+Shift+I → "Call John" → Remind me → +1h → Capture. Wait. The notification fires.
> Make Cadence your homepage — Settings → Cadence → toggle "Open Cadence on Obsidian startup"
> Cadence creates folders on demand: Cadence/Contacts/, Cadence/Pipeline/, Cadence/Partners/, etc. Move them anywhere afterwards — change paths in Settings if you do.
> 
> Configuration
> Settings → Cadence:
> 
> Modules — Toggle Planner / CRM / PRM. Disabled modules disappear from the nav and from dependent Reports.
> Reminders — Desktop notifications (opt-in, requests permission), clear completed.
> Currency — USD default; ZAR, EUR, GBP, AUD, CAD, CHF, JPY, INR, BRL, AED.
> App — Open on startup, default tab, week starts on, daily-note folder, tasks/journal headings.
> Customizing Entity Properties
> Cadence lets you define custom frontmatter properties for any of your core entities (Contact, Company, Project, Deal, Activity, Partner, etc.) to model your specific business workflows directly inside Obsidian.
> 
> Settings → Cadence → Custom Entities Properties:
> 
> 1. Custom Property Types
> text — Standard text input field.
> multitext — Chip-based multi-select tag input.
> enum — Dropdown menu with custom option lists.
> date — Native calendar date selector.
> tags — Tag chips synced directly with Obsidian's global tag index.
> currency — Automated financial values formatted according to your selected active currency.
> 2. Autocomplete & Suggestion Sources
> List properties (multitext) can pull autocomplete suggestions dynamically from:
> 
> folder:Path/To/Folder — Dynamically scans the specified vault folder. Suggests existing note basenames (e.g. folder:Cadence/Contacts maps contacts).
> history — Scans your existing notes to suggest any values previously entered. Saves values as plain-text lists instead of Obsidian wikilinks.
> tags — Pulls tags directly from Obsidian's global cache.
> none — Simple custom list inputs without suggestions.
> 3. Background Entity Auto-Creation
> When a property has a suggestion source pointing to a vault folder (e.g. folder:Cadence/Contacts or folder:Cadence/Shared), Cadence automatically creates the referenced note in the background when you assign a new name. It formats the link as a native Obsidian [[Wikilink]] and populates the frontmatter immediately, saving manual overhead.
> 
> 4. Loop-Safe Bidirectional Sync
> Core relationships (like Project ↔ Contact) are bidirectionally synchronized between frontmatter sheets in a loop-safe manner:
> 
> Assigning a contact to a project's owner property automatically adds the project to that contact's project property.
> Symmetric Removals: Clearing a project from a contact's sheet or a contact from a project's properties instantly dissociates them on both sides.
> Physical Deletion Sync: Deleting a Project note entirely triggers a vault-wide background cleanup that removes all stale references from your Contacts' frontmatter automatically.
> 5. Drag-and-Drop Reordering & System Locks
> Visual Reordering: Use the grab handle (⋮⋮) to drag-and-drop properties to rearrange their visual layout order inside detail sheets and lists.
> System Locks (🔒) : Critical properties required for Cadence's system engines (such as the Primary field, Type, or Status) are secured. Reordering attempts that shift a locked field from its original index are safely rejected to preserve layout integrity.
> 6. Interactive & Configurable Kanban Board Grouping
> Dynamic Grouping Selector: Any Kanban view displays a stylish "Group columns by" selector in the filters bar. You can dynamically group your board columns by any enum, text, multitext, or tags property.
> On-the-Fly Column Extraction: When grouping by a list/text property (such as project), Cadence scans all entity files to extract and clean unique values (stripping Obsidian brackets) to build your board columns automatically.
> Smart Drag-and-Drop Drops: Moving cards between dynamically grouped columns updates list-based frontmatter properties (handling wikilinks and plain text list items appropriately).
> 7. Custom Dashboards & Analytics Widgets
> Cross-Module Analytics: Custom dashboard charts can be added to the bottom of the Projects Dashboard, CRM Dashboard (Deals), and PRM Dashboard (Partners).
> Flexible Visualization: Supports visualizing any property in Donut, Bar, KPI Grid, or Simple List layout, featuring full drag-and-drop status counters and segment alignment.
> Templates & Dynamic Section Blocks
> Cadence goes beyond standard properties by giving you a visual layout and H2 section editor for each of your entities:
> 
> Entity Templates (Cadence/Templates/) — Every entity has a template file (e.g. Cadence/Templates/project.md or Cadence/Templates/contact.md). These templates define the visual markdown structure of any newly created item, including standard H2 sections (like ## Notes, ## Scope, ## Bio). You can easily reset any template to default or customize it in the Templates Dashboard (Settings → Templates).
> Drag-and-Drop Section Reordering — In the Templates Dashboard, you can visually drag-and-drop the dynamic H2 sections of any template to rearrange their layout order. Moving cards reorders the H2 blocks inside the markdown template file automatically.
> Dynamic Markdown Blocks Rendering — Inside any entity detail page (e.g., a specific Project sheet), H2 headers with custom tags like #notes are parsed and rendered as premium cards with rich markdown previews. Any links inside these markdown cards are fully clickable, automatically opening target entities or wiki-links inside Obsidian.
> Live Side-by-Side Editing — Click the edit button (file icon) on any block to open it in a split pane to the right to edit natively using full Live Preview and auto-complete in Obsidian, with real-time dynamic refresh as you type.
> Dynamic Cross-References Table/Kanban — You can link related entities directly (e.g., showing all Contacts related to a Company, or all Deals belonging to a Project). In the template, tags like #cross-contact-company-table or #cross-deal-company-kanban automatically query, render, and filter related items inside tables or interactive Kanban boards within the sheet!
> TaskNotes Integration
> For advanced task management, Cadence natively integrates with the popular TaskNotes community plugin.
> 
> Seamless Toggle — Switch from Cadence's native daily-note task manager to TaskNotes anytime via Settings → Cadence → Task management system dropdown.
> Unified Interface — When active, your TaskNotes folders and task files (TaskNotes/Tasks/...) are displayed inline throughout Cadence, including in the Today planner sheet and within individual projects.
> Bi-directional Sync — Checking tasks off inside Cadence instantly updates the frontmatter of your TaskNotes files (status: done ↔ status: open) and vice versa, in real time!
> Hotkeys
> Action	Shortcut
> Open Cadence	(assignable, no default)
> Quick capture (with optional reminder)	Cmd+Shift+I (Ctrl+Shift+I on Windows/Linux)
> Open Cadence — Home	(assignable)
> Open Cadence — Today	(assignable)
> Open Cadence — Calendar	(assignable)
> Open Cadence — Pipeline	(assignable)
> Open Cadence — Inbox	(assignable)
> Import from CSV	(assignable)
> New today entry (creates if missing)	(assignable)
> Bind your favourites under Settings → Hotkeys → search "Cadence".
> 
> How the data is stored
> your-vault/
>   daily/                          ← daily notes (your existing setup)
>     2026-05-05.md
>   Cadence/
>     Contacts/Jane Smith.md
>     Companies/Acme.md
>     Pipeline/Acme — FTTH expansion.md
>     Partners/Distribution Co.md
>     Activities/Discovery call with Jane.md
>     Projects/Q3 launch.md
>     ...
> Each entity is plain markdown with YAML frontmatter — readable, editable, scriptable, portable. Cadence's views are just rich lenses over these files; everything you do in the UI writes back to them.
> 
> Companion theme
> A matching Cadence theme is available separately for vaults that want a fully-tuned visual system (warm paper surfaces, emerald accents, Geist + JetBrains Mono typography). The plugin works with any Obsidian theme; the Cadence theme is purely cosmetic.
> 
> Roadmap
> Drag-to-reorder milestones in Project Detail
> Linked entities (project ↔ deal ↔ contact pickers with fuzzy search)
> Time-blocked Calendar (drag tasks onto today's hour grid)
> Pomodoro / focus timer linked to a reminder
> Optional sync to a Cadence web instance (the API setting is the placeholder for this)
> Development
> git clone https://github.com/wesswart77/obsidian-cadence
> cd obsidian-cadence
> # Plugin is plain JS, no build step. Drop main.js + manifest.json + styles.css
> # into <vault>/.obsidian/plugins/cadence-planner/ to test.
> PRs welcome. For bug reports, please include your Obsidian version, OS, and a minimal vault to reproduce.
> 
> Support
> If Cadence saves you time or makes your day a bit smoother, a coffee keeps the dev nights going. ☕
> 
> Buy Me a Coffee
> 
> Or via the heart icon next to Cadence in Obsidian's community plugin browser once you have it installed.
> 
> License
> MIT © Wesley Swart

### Assistant
> Yes. This can work for you **right now**, but only if we stop treating Cadence like “a plugin” and start treating it like a **working cockpit over structured Markdown**.
> 
> The move is:
> 
> > **Use Cadence as your daily/active workbench. Use QiLife/Supabase as the durable backend/index. Use QiNexus/My Drive as the storage layer.**
> 
> Do **not** wait for the custom QiLife frontend to be done. That’s the trap.
> 
> ---
> 
> # The setup that makes sense for you
> 
> Since `My Drive / QiVault` opens in Obsidian and `C:\QiLabs` does not, use **My Drive / QiVault as the Obsidian layer**.
> 
> Do **not** force `C:\QiLabs` into Obsidian right now.
> 
> ## Working model
> 
> ```text
> My Drive / QiVault
> = Obsidian + Cadence working vault
> 
> C:\QiLabs
> = apps, code, repos, server/dev work
> 
> Supabase
> = durable database mirror/index
> 
> QiLife app
> = custom UI later
> ```
> 
> This avoids the silo problem because your Markdown records will contain stable IDs, paths, links, and frontmatter that can sync into Supabase later.
> 
> ---
> 
> # Recommended Cadence folder setup
> 
> Inside the Obsidian vault, create one clean root for the workbench:
> 
> ```text
> 13_system/obsidian/QiLife_Workbench/
> ```
> 
> Then inside it:
> 
> ```text
> 13_system/obsidian/QiLife_Workbench/
>   00_inbox/
>   01_daily/
>   Cadence/
>     Contacts/
>     Companies/
>     Projects/
>     Pipeline/
>     Activities/
>     Partners/
>     Inbox/
>     Templates/
> ```
> 
> Why keep the `Cadence/` folder? Because for testing, let Cadence stay close to its defaults. Don’t fight it before you know what parts you like.
> 
> Later we can rename/move:
> 
> ```text
> Cadence/Contacts   → QiLife/People
> Cadence/Pipeline   → QiLife/Matters
> Cadence/Projects   → QiLife/Projects
> Cadence/Activities → QiLife/Interactions
> ```
> 
> But for the first week, don’t over-customize. Let it breathe.
> 
> ---
> 
> # How to make it actually useful
> 
> ## Turn on these modules
> 
> In Cadence settings:
> 
> | Module | Use? | Why |
> |---|---:|---|
> | Planner | Yes | Daily actions, inbox, today |
> | CRM | Yes, but renamed mentally | People, organizations, matters |
> | PRM | Maybe later | Vendors/support network, not today |
> | TaskNotes | Not yet | Extra complexity; test native Cadence first |
> 
> Start with:
> 
> ```text
> Planner: ON
> CRM: ON
> PRM: OFF
> TaskNotes integration: OFF
> ```
> 
> Do not turn everything on like a buffet gremlin.
> 
> ---
> 
> # Your Cadence translation map
> 
> Cadence says business words. You translate them into life-ops words.
> 
> | Cadence | Your meaning |
> |---|---|
> | Contacts | People |
> | Companies | Organizations |
> | Deals / Pipeline | Matters / Workstreams |
> | Projects | Projects |
> | Activities | Interactions / Events |
> | Partners | Support network / vendors |
> | Inbox | Capture |
> | Reports | Dashboards |
> 
> So when Cadence says “Deal,” you can use it as:
> 
> ```text
> legal matter
> care issue
> insurance follow-up
> business opportunity
> dispute
> claim
> open loop
> ```
> 
> That is the hack.
> 
> ---
> 
> # The frontmatter rule
> 
> Every note should have **two field layers**:
> 
> ## 1. Cadence-friendly fields
> 
> These make the plugin work:
> 
> ```yaml
> name:
> status:
> priority:
> stage:
> company:
> contact:
> project:
> tags:
> date:
> due:
> value:
> ```
> 
> ## 2. QiLife durable fields
> 
> These make your backend/sync work later:
> 
> ```yaml
> id:
> type:
> source:
> sync_status:
> created_at:
> updated_at:
> custom_fields:
> qilabs_refs:
> storage_refs:
> supabase_entity_id:
> ```
> 
> That way:
> 
> ```text
> Cadence can use it today.
> Supabase can understand it tomorrow.
> QiLife can render it later.
> ```
> 
> ---
> 
> # Starter templates to use
> 
> ## Project template
> 
> Create:
> 
> ```text
> 13_system/obsidian/QiLife_Workbench/Cadence/Projects/Mom Care Plan.md
> ```
> 
> ```yaml
> ---
> id: project_mom_care_plan_001
> type: project
> name: Mom Care Plan
> status: active
> priority: high
> owner: "[[Cody]]"
> due: 2026-06-30
> tags:
>   - mom-care
>   - health
>   - operations
> source: obsidian
> sync_status: local_first
> created_at: 2026-06-18
> updated_at: 2026-06-18
> custom_fields:
>   domain: care
>   risk_level: high
>   next_review_date: 2026-06-20
> qilabs_refs:
>   - path: "C:/QiLabs/60_QiApps/52_QiApp_QiLife"
>     label: "QiLife app repo"
> ---
> ```
> 
> ```markdown
> ## Brief
> 
> Central operating plan for Mom’s care, appointments, medications, supplies, insurance issues, and follow-ups.
> 
> ## Scope
> 
> - Care contacts
> - Open care issues
> - Appointment tracking
> - Document tracking
> - Follow-ups
> 
> ## Risks
> 
> - Missed medication changes
> - Confusing discharge instructions
> - Insurance delays
> - Responsibility confusion
> 
> ## Notes
> 
> ```
> 
> ---
> 
> ## Person/contact template
> 
> ```yaml
> ---
> id: person_dr_alice_vance_001
> type: contact
> name: Dr Alice Vance
> status: active
> priority: high
> role: Primary Care Doctor
> company: "[[Example Clinic]]"
> email: ""
> phone: ""
> projects:
>   - "[[Mom Care Plan]]"
> tags:
>   - medical
>   - mom-care
> source: obsidian
> sync_status: local_first
> created_at: 2026-06-18
> updated_at: 2026-06-18
> custom_fields:
>   entity_kind: person
>   preferred_contact_method: phone
>   next_follow_up: 2026-06-20
> ---
> ```
> 
> ```markdown
> ## Summary
> 
> Primary care contact for Mom’s care coordination.
> 
> ## Notes
> 
> ## Questions
> 
> - Confirm medication list.
> - Confirm recent discharge instructions.
> - Confirm oxygen/supply plan.
> ```
> 
> ---
> 
> ## Matter / pipeline template
> 
> Use Cadence Pipeline for your “matters.”
> 
> ```yaml
> ---
> id: matter_humana_care_plan_follow_up_001
> type: deal
> name: Humana Care Plan Follow Up
> stage: active
> status: active
> priority: high
> value: 0
> company: "[[Humana]]"
> project: "[[Mom Care Plan]]"
> tags:
>   - insurance
>   - mom-care
>   - follow-up
> source: obsidian
> sync_status: local_first
> created_at: 2026-06-18
> updated_at: 2026-06-18
> custom_fields:
>   entity_kind: matter
>   matter_type: care_insurance
>   desired_outcome: written care plan confirmation
>   deadline: 2026-06-21
> ---
> ```
> 
> ```markdown
> ## Summary
> 
> Follow-up matter for confirming what care plan exists, what Humana should provide, and what action is required.
> 
> ## Timeline
> 
> ## Evidence
> 
> ## Next Action
> 
> Call Humana and ask for written care plan / case management documentation.
> ```
> 
> ---
> 
> # Your first real Cadence test
> 
> Do **not** import your whole life yet.
> 
> Create only:
> 
> ```text
> 2 contacts
> 2 companies
> 2 projects
> 2 pipeline matters
> 2 activities
> ```
> 
> Suggested first 10:
> 
> ```text
> Contacts:
> - Cody
> - Dr Alice Vance
> 
> Companies:
> - Humana
> - Example Clinic
> 
> Projects:
> - Mom Care Plan
> - QiLife Alpha Workbench
> 
> Pipeline / Matters:
> - Humana Care Plan Follow Up
> - QiLife Cadence Mapping
> 
> Activities:
> - 2026-06-18 Cadence Setup Session
> - 2026-06-18 Supabase Alpha Review
> ```
> 
> Then use it for one day.
> 
> The test question is:
> 
> > “Does this reduce friction, or did we just make prettier clutter?”
> 
> If it reduces friction, we lock it in.
> 
> ---
> 
> # Custom properties to add first
> 
> In Cadence custom entity properties, add only a few.
> 
> ## For Projects
> 
> | Label | Frontmatter key | Type |
> |---|---|---|
> | Domain | `domain` | enum |
> | Risk Level | `risk_level` | enum |
> | Next Review | `next_review_date` | date |
> | Related Matter | `related_matter` | multitext / folder source |
> 
> Domain options:
> 
> ```text
> care
> legal
> finance
> tech
> business
> personal
> ```
> 
> Risk level:
> 
> ```text
> low
> medium
> high
> critical
> ```
> 
> ## For Contacts
> 
> | Label | Frontmatter key | Type |
> |---|---|---|
> | Role | `role` | text |
> | Relationship Type | `relationship_type` | enum |
> | Preferred Contact | `preferred_contact_method` | enum |
> | Next Follow Up | `next_follow_up` | date |
> 
> Relationship type:
> 
> ```text
> family
> medical
> legal
> finance
> vendor
> support
> client
> friend
> unknown
> ```
> 
> ## For Pipeline / Matters
> 
> | Label | Frontmatter key | Type |
> |---|---|---|
> | Matter Type | `matter_type` | enum |
> | Desired Outcome | `desired_outcome` | text |
> | Deadline | `deadline` | date |
> | Evidence Folder | `evidence_folder` | text |
> 
> Matter type:
> 
> ```text
> care
> legal
> finance
> tech
> business
> dispute
> admin
> ```
> 
> ---
> 
> # Cadence settings I’d use
> 
> ## App
> 
> ```text
> Open Cadence on startup: ON
> Default tab: Home
> Week starts on: Monday
> Daily note folder: 13_system/obsidian/QiLife_Workbench/01_daily
> ```
> 
> ## Reminders
> 
> ```text
> Desktop notifications: ON
> Clear completed: ON
> ```
> 
> ## Hotkeys
> 
> Set these:
> 
> | Action | Hotkey |
> |---|---|
> | Open Cadence | `Ctrl+Alt+C` |
> | Quick Capture | `Ctrl+Shift+I` |
> | Open Today | `Ctrl+Alt+T` |
> | Open Inbox | `Ctrl+Alt+I` |
> 
> ---
> 
> # How this maps to the backend
> 
> Eventually your importer does this:
> 
> ```text
> Markdown note
> → parse YAML frontmatter
> → parse body markdown
> → extract wikilinks
> → upsert into Supabase qilife_entities
> → upsert relationships
> → preserve markdown_path
> ```
> 
> So a note like:
> 
> ```yaml
> id: matter_humana_care_plan_follow_up_001
> type: deal
> name: Humana Care Plan Follow Up
> project: "[[Mom Care Plan]]"
> company: "[[Humana]]"
> ```
> 
> becomes:
> 
> ```text
> qilife_entities:
> - matter_humana_care_plan_follow_up_001
> 
> qilife_entity_relationships:
> - Humana Care Plan Follow Up → related_to → Mom Care Plan
> - Humana Care Plan Follow Up → involves → Humana
> ```
> 
> That is why this is not siloed.
> 
> ---
> 
> # My honest verdict
> 
> This is a **very good working-system move**.
> 
> You found a front end that is:
> 
> - fast
> - local
> - intuitive
> - Markdown-native
> - customizable
> - not locked into someone else’s cloud
> - immediately usable
> 
> And we already have the backend path:
> 
> - Supabase alpha schema
> - fake seed
> - read-only QiLife Workbench route
> - entity mirror concept
> 
> So the plan is not “use Cadence forever instead of QiLife.”
> 
> The plan is:
> 
> ```text
> Use Cadence now.
> Generate clean structured Markdown.
> Mirror it to Supabase later.
> Let QiLife app mature from real usage.
> ```
> 
> That is how you avoid building fantasy software for imaginary workflows.
> 
> Start small. Use it for one day. If it clicks after 10 notes and 20 captures, we scale it.

### User
> this is all cadence is, how do we take this and use the same logic but for my use case as a possible qilife seed.

### Assistant
> Yes. **Now we’re looking at the actual thing.** Cadence is not magic. It is basically:
> 
> ```text
> settings JSON
> + nav registry
> + entity registry
> + Markdown/frontmatter scanner
> + template generator
> + generic list/kanban/detail renderers
> + CSS shell
> ```
> 
> That is **extremely usable as a QiLife seed**.
> 
> Cadence’s manifest literally says the plugin is a Markdown source-of-truth workspace with no server required, and your uploaded `main.js` confirms it is one unified Obsidian view with internal navigation and plain JavaScript loaded directly by Obsidian. fileciteturn11file2 fileciteturn11file1
> 
> ## The real move
> 
> We do **not** “copy Cadence and hope.”
> 
> We extract the pattern into a **QiLife Workbench Seed**:
> 
> ```text
> Cadence concept
> → QiLife naming
> → QiLife entity contract
> → Obsidian/Cadence-compatible markdown
> → Supabase mirror shape
> → later QiLife app UI
> ```
> 
> This becomes your bridge.
> 
> ---
> 
> # What to steal from Cadence
> 
> ## 1. The nav model
> 
> Cadence has `NAV_GROUPS`: Home, Planner, Projects, CRM, PRM, Workflow, Reports, Settings. fileciteturn11file1
> 
> For QiLife, the nav seed becomes:
> 
> ```text
> Home
> Daily Ops
> Capture
> People
> Projects
> Care
> Matters
> Money
> Systems
> Reports
> Settings
> ```
> 
> Cadence’s CRM/PRM words are just costumes. We strip the business SaaS cosplay off.
> 
> ---
> 
> ## 2. The entity registry
> 
> Cadence’s `ENTITIES` object is the prize. Each entity has:
> 
> ```text
> folder
> label
> plural
> fields
> columns
> ```
> 
> The code says each entity is a folder of Markdown notes with a known frontmatter shape, and generic list/render views sit on top of that same entity data. fileciteturn11file1
> 
> QiLife needs the same pattern:
> 
> ```text
> person
> organization
> project
> matter
> care_item
> interaction
> task
> reminder
> file_record
> account
> transaction
> ```
> 
> That means QiLife can generate:
> 
> - Obsidian folders
> - Markdown templates
> - Supabase tables/rows
> - UI cards
> - list views
> - kanban views
> - reports
> 
> from the same seed.
> 
> ---
> 
> ## 3. The settings/data model
> 
> Your uploaded `data.json` already shows the useful pattern:
> 
> - daily note folder
> - journal heading
> - tasks heading
> - enabled modules
> - reminders
> - dashboard widgets
> - custom pages
> - page layouts
> - kanban grouping
> - custom entity fields fileciteturn11file0
> 
> That is exactly what QiLife needs as:
> 
> ```text
> qilife.seed.json
> ```
> 
> Not hardcoded everywhere. One seed file.
> 
> ---
> 
> ## 4. The relationship logic
> 
> Cadence reads wikilinks like:
> 
> ```yaml
> project:
>   - "[[Mom Care Plan]]"
> company:
>   - "[[Humana]]"
> ```
> 
> Its helper logic parses wikilink values and resolves entity values from frontmatter. fileciteturn10file9
> 
> QiLife should do the same:
> 
> ```text
> Markdown wikilink
> → parsed relationship
> → Supabase relationship row
> → QiLife graph/report/dashboard later
> ```
> 
> That is your “pack your data and go” model.
> 
> ---
> 
> # The QiLife seed structure
> 
> Create this in the QiLife repo:
> 
> ```text
> seeds/qilife_workbench/
>   README.md
>   qilife.seed.json
>   nav.seed.json
>   entities.seed.json
>   templates/
>     person.md
>     organization.md
>     project.md
>     matter.md
>     care_item.md
>     interaction.md
>     task.md
>     reminder.md
>     file_record.md
>     account.md
>     transaction.md
>   examples/
>     people/
>     projects/
>     matters/
>     care/
>   supabase/
>     seed_qilife_entity_types.sql
>     seed_qilife_property_definitions.sql
>     seed_qilife_navigation_pages.sql
> ```
> 
> That is clean. It separates:
> 
> ```text
> Cadence reference code
> from
> QiLife seed model
> ```
> 
> ---
> 
> # Cadence → QiLife translation
> 
> | Cadence entity | QiLife entity | Purpose |
> |---|---|---|
> | `contact` | `person` | people, doctors, family, vendors, clients |
> | `company` | `organization` | companies, hospitals, agencies, courts |
> | `project` | `project` | active work containers |
> | `deal` | `matter` | legal matters, care issues, disputes, admin workstreams |
> | `activity` | `interaction` | calls, meetings, notes, events |
> | `partner` | `support_provider` / `organization` | vendors, helpers, partner orgs |
> | `commission` | `transaction` | money/event record later |
> | `registration` | `filing` / `document_event` | legal/admin submissions |
> | `lead` | probably skip | too sales-specific |
> | `sequence` | workflow | later automation |
> 
> Do **not** carry every Cadence entity forward. That is how clutter reproduces.
> 
> ---
> 
> # The QiLife seed JSON
> 
> This is the kind of seed we want:
> 
> ```json
> {
>   "app": {
>     "name": "QiLife Workbench",
>     "defaultTab": "home",
>     "dailyNoteFolder": "02_timeline/daily",
>     "journalHeading": "## Journal",
>     "tasksHeading": "## Today",
>     "weekStartsOn": 1,
>     "sourceMode": "markdown_first",
>     "databaseMode": "supabase_mirror"
>   },
>   "modules": {
>     "daily_ops": true,
>     "people": true,
>     "projects": true,
>     "care": true,
>     "matters": true,
>     "finance": true,
>     "systems": true,
>     "reports": true
>   },
>   "navGroups": [
>     {
>       "id": "home",
>       "label": "",
>       "items": [
>         {
>           "id": "home",
>           "label": "Home",
>           "icon": "home",
>           "desc": "Command center for today, priorities, projects, matters, and follow-ups."
>         }
>       ]
>     },
>     {
>       "id": "daily_ops",
>       "label": "Daily Ops",
>       "items": [
>         {
>           "id": "daily.inbox",
>           "label": "Inbox",
>           "icon": "inbox",
>           "entity": "capture_item"
>         },
>         {
>           "id": "daily.today",
>           "label": "Today",
>           "icon": "sun",
>           "entity": "daily_note"
>         }
>       ]
>     },
>     {
>       "id": "core",
>       "label": "Core",
>       "items": [
>         {
>           "id": "people",
>           "label": "People",
>           "icon": "users",
>           "entity": "person"
>         },
>         {
>           "id": "organizations",
>           "label": "Organizations",
>           "icon": "building-2",
>           "entity": "organization"
>         },
>         {
>           "id": "projects",
>           "label": "Projects",
>           "icon": "folder-kanban",
>           "entity": "project"
>         },
>         {
>           "id": "matters",
>           "label": "Matters",
>           "icon": "scale",
>           "entity": "matter"
>         }
>       ]
>     },
>     {
>       "id": "life",
>       "label": "Life Ops",
>       "items": [
>         {
>           "id": "care",
>           "label": "Care",
>           "icon": "heart-pulse",
>           "entity": "care_item"
>         },
>         {
>           "id": "money",
>           "label": "Money",
>           "icon": "wallet",
>           "entity": "transaction"
>         },
>         {
>           "id": "systems",
>           "label": "Systems",
>           "icon": "server",
>           "entity": "system_item"
>         }
>       ]
>     },
>     {
>       "id": "reports",
>       "label": "Reports",
>       "items": [
>         {
>           "id": "reports.graph",
>           "label": "Graph",
>           "icon": "network"
>         },
>         {
>           "id": "reports.productivity",
>           "label": "Productivity",
>           "icon": "bar-chart-3"
>         }
>       ]
>     }
>   ]
> }
> ```
> 
> That is the seed version of `NAV_GROUPS`.
> 
> ---
> 
> # The QiLife entity seed
> 
> This is the important part.
> 
> ```json
> {
>   "entities": {
>     "person": {
>       "folder": "04_people",
>       "label": "Person",
>       "plural": "People",
>       "primaryField": "name",
>       "columns": ["name", "role", "organization", "status", "last_contact"],
>       "fields": [
>         { "key": "id", "label": "ID", "type": "text", "locked": true },
>         { "key": "type", "label": "Type", "type": "text", "locked": true },
>         { "key": "name", "label": "Name", "type": "text", "primary": true },
>         { "key": "status", "label": "Status", "type": "enum", "options": ["active", "waiting", "inactive", "archived"] },
>         { "key": "role", "label": "Role", "type": "multitext" },
>         { "key": "organization", "label": "Organization", "type": "multitext", "suggestionSource": "folder:05_organizations" },
>         { "key": "project", "label": "Project", "type": "multitext", "suggestionSource": "folder:03_projects" },
>         { "key": "last_contact", "label": "Last Contact", "type": "date" },
>         { "key": "tags", "label": "Tags", "type": "tags" }
>       ]
>     },
>     "project": {
>       "folder": "03_projects",
>       "label": "Project",
>       "plural": "Projects",
>       "primaryField": "name",
>       "columns": ["name", "domain", "status", "priority", "owner", "due"],
>       "fields": [
>         { "key": "id", "label": "ID", "type": "text", "locked": true },
>         { "key": "type", "label": "Type", "type": "text", "locked": true },
>         { "key": "name", "label": "Name", "type": "text", "primary": true },
>         { "key": "domain", "label": "Domain", "type": "enum", "options": ["care", "legal", "finance", "tech", "business", "personal"] },
>         { "key": "status", "label": "Status", "type": "enum", "options": ["active", "on_hold", "waiting", "backlog", "done", "archived"] },
>         { "key": "priority", "label": "Priority", "type": "enum", "options": ["low", "medium", "high", "urgent"] },
>         { "key": "owner", "label": "Owner", "type": "multitext", "suggestionSource": "folder:04_people" },
>         { "key": "started", "label": "Started", "type": "date" },
>         { "key": "due", "label": "Due", "type": "date" },
>         { "key": "tags", "label": "Tags", "type": "tags" }
>       ]
>     },
>     "matter": {
>       "folder": "07_legal/matters",
>       "label": "Matter",
>       "plural": "Matters",
>       "primaryField": "title",
>       "columns": ["title", "matter_type", "stage", "priority", "organization", "deadline"],
>       "fields": [
>         { "key": "id", "label": "ID", "type": "text", "locked": true },
>         { "key": "type", "label": "Type", "type": "text", "locked": true },
>         { "key": "title", "label": "Title", "type": "text", "primary": true },
>         { "key": "matter_type", "label": "Matter Type", "type": "enum", "options": ["care", "legal", "finance", "tech", "admin", "dispute", "business"] },
>         { "key": "stage", "label": "Stage", "type": "enum", "options": ["inbox", "active", "waiting", "blocked", "resolved", "archived"] },
>         { "key": "priority", "label": "Priority", "type": "enum", "options": ["low", "medium", "high", "urgent"] },
>         { "key": "organization", "label": "Organization", "type": "multitext", "suggestionSource": "folder:05_organizations" },
>         { "key": "person", "label": "Person", "type": "multitext", "suggestionSource": "folder:04_people" },
>         { "key": "project", "label": "Project", "type": "multitext", "suggestionSource": "folder:03_projects" },
>         { "key": "deadline", "label": "Deadline", "type": "date" },
>         { "key": "tags", "label": "Tags", "type": "tags" }
>       ]
>     }
>   }
> }
> ```
> 
> That is how we translate Cadence’s `ENTITIES` into QiLife.
> 
> ---
> 
> # The backend seed
> 
> The same file can seed Supabase config tables:
> 
> ```text
> entity_types
> entity_property_definitions
> navigation_pages
> entity_view_configs
> ```
> 
> So one QiLife seed drives:
> 
> ```text
> Obsidian folder/template setup
> + Cadence-like UI
> + Supabase metadata tables
> + QiLife app config
> ```
> 
> That is the entire move.
> 
> ---
> 
> # The logic we reuse
> 
> ## Cadence logic
> 
> ```text
> entity registry
> → list files in folder
> → read frontmatter
> → render generic list/table/card/kanban
> → open detail view
> → update frontmatter
> → parse links
> → show reports/widgets
> ```
> 
> ## QiLife logic
> 
> ```text
> entity registry
> → list Markdown notes OR query Supabase
> → read frontmatter_json
> → render generic list/table/card/kanban
> → open detail surface
> → controlled write path later
> → parse relationships
> → reports/widgets
> ```
> 
> Same brain. Different body.
> 
> ---
> 
> # What I would tell the IDE agent to build
> 
> Do **not** tell it to rewrite QiLife. Tell it to create a seed package.
> 
> ```text
> Create a QiLife Workbench Seed package inspired by Cadence.
> 
> Inputs:
> - reference/obsidian-cadence/main.js
> - reference/obsidian-cadence/data.json
> - docs/architecture/qilife_markdown_entity_contract.md
> - existing alpha Supabase schema
> 
> Goal:
> Extract Cadence's config-driven logic into QiLife seed files, not production app behavior yet.
> 
> Create:
> 1. seeds/qilife_workbench/README.md
> 2. seeds/qilife_workbench/qilife.seed.json
> 3. seeds/qilife_workbench/nav.seed.json
> 4. seeds/qilife_workbench/entities.seed.json
> 5. seeds/qilife_workbench/templates/*.md
> 6. seeds/qilife_workbench/supabase/seed_qilife_entity_types.sql
> 7. seeds/qilife_workbench/supabase/seed_qilife_property_definitions.sql
> 8. seeds/qilife_workbench/supabase/seed_qilife_navigation_pages.sql
> 
> Rules:
> - Do not replace QiLife production routes.
> - Do not build CRUD.
> - Do not migrate real data.
> - Do not delete Cadence attribution.
> - Use Cadence as a reference implementation only.
> - Keep QiLife names centered on life/care/legal/finance/tech, not sales CRM.
> - Keep Markdown/frontmatter compatible with Obsidian.
> - Use stable IDs.
> - Use custom fields/jsonb for flexible properties.
> - Supabase remains a mirror/index until write strategy is approved.
> 
> Cadence to QiLife mapping:
> - contact -> person
> - company -> organization
> - project -> project
> - deal/pipeline -> matter
> - activity -> interaction
> - partner -> support_provider or organization
> - commission -> transaction
> - registration -> document_event or filing
> - sequence -> workflow
> 
> Seed entities:
> - person
> - organization
> - project
> - matter
> - care_item
> - interaction
> - task
> - reminder
> - file_record
> - account
> - transaction
> - system_item
> 
> After creating files:
> - validate JSON
> - summarize mappings
> - recommend which seed files should load into Supabase first
> ```
> 
> ---
> 
> # My blunt recommendation
> 
> This is **the right seed path**.
> 
> Not because Cadence is perfect. It isn’t.
> 
> Because Cadence has already solved the shape:
> 
> ```text
> One nav
> Many entity folders
> Frontmatter schema
> Generic renderers
> Custom fields
> Dashboards
> Kanban
> Daily notes
> Reminders
> ```
> 
> And your system needs exactly that, except centered around:
> 
> ```text
> Cody
> family
> Mom care
> legal
> finance
> tech
> projects
> files
> daily operations
> ```
> 
> Your own QiAccess blueprint already says the current system is about your actual life — family, care, legal, finance, knowledge, tech, and daily action — not an imaginary business/client platform. fileciteturn10file2
> 
> So yes: **Cadence becomes the seed logic. QiLife becomes the durable system.**
> 
> The short doctrine:
> 
> ```text
> Use Cadence's engine pattern.
> Replace the nouns.
> Preserve Markdown.
> Mirror to Supabase.
> Let QiLife mature from actual usage.
> ```
> 
> That is the cleanest path we’ve found.

### User
> this is a mess, just give me what folders should be inside qispark, keeping in mind this is for the qieos, proncipal overall rules, and guies ect, as everuthing else will be in its mirror folder seperately.

### Assistant
> Yes. Clean reset.
> 
> **QiSpark should be the QiEOS / doctrine / rules / guide layer only.**  
> No app code, no server docs, no data migrations, no client/matter files, no duplicated module docs.
> 
> ## `C:\QiLabs\10_QiSpark`
> 
> ```text
> 10_QiSpark/
> ├── 00_workspace/
> ├── 10_qieos_core/
> ├── 20_principles/
> ├── 30_rules_standards/
> ├── 40_guides_playbooks/
> ├── 50_architecture_maps/
> ├── 60_registries_indexes/
> ├── 70_templates_prompts/
> ├── 80_qiaccess_start/
> └── 90_archive/
> ```
> 
> ## What each folder is for
> 
> | Folder | Purpose |
> |---|---|
> | `00_workspace/` | QiSpark index, current working notes, changelog, roadmap, temporary planning docs |
> | `10_qieos_core/` | The actual QiEOS doctrine: vision, purpose, OS model, definitions, “what this system is” |
> | `20_principles/` | Core principles, decision principles, design principles, life/system values |
> | `30_rules_standards/` | Global rules: naming rules, folder rules, file rules, security rules, documentation standards |
> | `40_guides_playbooks/` | Human guides and playbooks: “how to use QiLabs,” “how to organize files,” “how to work with agents” |
> | `50_architecture_maps/` | Big-picture maps only: QiLabs root map, module map, data-flow map, not app-specific docs |
> | `60_registries_indexes/` | Canonical indexes: module registry, folder registry, glossary, ADR index, prompt index |
> | `70_templates_prompts/` | Global templates and reusable prompts used across the whole system |
> | `80_qiaccess_start/` | Simple QiAccess landing/start page only — HTML launcher, icons, links, config |
> | `90_archive/` | Old QiSpark/QiEOS material that should not be deleted yet but is no longer current |
> 
> ## What does **not** belong in QiSpark
> 
> ```text
> App code
> Supabase migrations
> Database schemas for specific apps
> Server setup docs
> Docker configs
> Client legal files
> Mom care records
> Finance ledgers
> Random exports
> Screenshots/evidence
> Project-specific README files
> ```
> 
> Those go in their mirror/domain folders:
> 
> ```text
> 20_QiSystem/     → system/data/backend rules
> 30_QiServer/     → server/docker/self-hosted docs
> 40_QiCapture/    → ingestion/capture workflows
> 50_QiNexus/      → Drive/blob/life records
> 60_QiApps/       → app-specific docs and code
> ```
> 
> ## My clean ruling
> 
> QiSpark is the **constitution + operating manual + start page**.
> 
> Everything else lives where it actually operates.
> 
> So the structure should stay small, boring, and authoritative:
> 
> ```text
> QiSpark = why + rules + guides + maps + templates + start
> Other folders = actual systems and domain work
> ```

### User
> qi spartk is the docs mam, where we go to make sure everythign is following the rules and what hour plan is ect.

### Assistant
> You’re right. I framed it too narrow.
> 
> **QiSpark is the docs + governance command center.**  
> It is where we check:
> 
> ```text
> What are the rules?
> What is the plan?
> What is the current structure?
> What standards are we following?
> What did we decide?
> What should agents/Codex/Gemini follow?
> ```
> 
> So QiSpark should be the **documentation brain** of QiLabs/QiEOS — not just “principles.”
> 
> # Corrected `10_QiSpark` folder structure
> 
> ```text
> 10_QiSpark/
> ├── 00_home/
> ├── 01_qieos/
> ├── 02_master_plan/
> ├── 03_rules/
> ├── 04_standards/
> ├── 05_guides/
> ├── 06_architecture/
> ├── 07_modules/
> ├── 08_decisions/
> ├── 09_agents_prompts/
> ├── 10_templates/
> ├── 11_audits_reviews/
> ├── 12_changelog/
> ├── 13_qiaccess_start/
> └── 90_archive/
> ```
> 
> ## What each folder means
> 
> | Folder | What goes here |
> |---|---|
> | `00_home/` | QiSpark homepage, master index, “start here,” current status |
> | `01_qieos/` | QiEOS doctrine, definitions, operating system model, big-picture philosophy |
> | `02_master_plan/` | Current roadmap, phase plan, hour-by-hour/day-by-day plans, priorities |
> | `03_rules/` | Hard rules: folder rules, naming rules, safety rules, data rules, agent rules |
> | `04_standards/` | Standards for Markdown, frontmatter, schemas, file names, docs, commits |
> | `05_guides/` | Human-readable guides: how to use QiLabs, how to file things, how to work the system |
> | `06_architecture/` | Global architecture maps, QiLabs root structure, data flow, system diagrams |
> | `07_modules/` | Docs indexes for each module: QiSpark, QiSystem, QiServer, QiNexus, QiApps, etc. |
> | `08_decisions/` | ADRs and decision records: why we chose Supabase, Cadence, Obsidian, etc. |
> | `09_agents_prompts/` | Codex/Gemini/OpenClaw prompts, agent rules, reusable task prompts |
> | `10_templates/` | Global doc templates, index templates, ADR templates, folder templates |
> | `11_audits_reviews/` | Structure audits, repo reviews, migration reviews, checklist outputs |
> | `12_changelog/` | What changed, when, and why |
> | `13_qiaccess_start/` | QiAccess simple HTML landing/start page and its docs/config |
> | `90_archive/` | Old docs that are not current but should not be deleted yet |
> 
> # The rule
> 
> QiSpark can **describe and govern everything**, but it should not **store the working data for everything**.
> 
> So:
> 
> ```text
> QiSpark = rules, docs, plans, maps, decisions, guides
> Mirror folders = actual work, code, records, data, evidence
> ```
> 
> Example:
> 
> ```text
> 10_QiSpark/07_modules/30_qiserver.md
> ```
> 
> can explain what QiServer is supposed to contain.
> 
> But actual server files stay in:
> 
> ```text
> 30_QiServer/
> ```
> 
> Same thing:
> 
> ```text
> 10_QiSpark/07_modules/60_qiapps.md
> ```
> 
> can explain QiApps rules.
> 
> But actual app code stays in:
> 
> ```text
> 60_QiApps/
> ```
> 
> # My corrected definition
> 
> **QiSpark is the documentation and governance layer for QiEOS.**
> 
> It contains:
> 
> ```text
> rules
> plans
> guides
> standards
> architecture
> decisions
> agent prompts
> audits
> module indexes
> QiAccess start page
> ```
> 
> It does **not** contain:
> 
> ```text
> app code
> server configs
> real life records
> legal evidence
> finance ledgers
> Supabase migrations
> raw imports
> node projects
> ```
> 
> That is the clean version.

### User
> {'asset_pointer': 'sediment://file_0000000065dc722f9146c9ae6ca1ae70', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 905, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 113005, 'width': 660}seems bloated and where do i put those loose files.

### Assistant
> Yes, this is bloated. The issue is **not that the docs are bad** — it’s that QiSpark root became a dumping ground.
> 
> ## Rule for QiSpark root
> 
> The root should have **almost no loose files**.
> 
> Keep only:
> 
> ```text
> 10_QiSpark/
> ├── 00_home/
> ├── 01_qieos/
> ├── 02_masterplan/
> ├── 03_principles/
> ├── 04_rules/
> ├── 05_standards/
> ├── 06_architecture/
> ├── 07_guides/
> ├── 08_services/
> ├── 09_decisions/
> ├── 10_prompts/
> ├── 11_templates/
> ├── 12_registries/
> ├── 13_schemas/
> ├── 14_reports/
> └── 90_archive/
> ```
> 
> I would **remove/merge these top-level folders**:
> 
> | Current folder | What to do |
> |---|---|
> | `20_blueprints` | Move under `06_architecture/blueprints/` |
> | `30_roadmaps` | Move under `02_masterplan/roadmaps/` |
> | `40_reports` | Rename/move to `14_reports/` |
> | `50_schemas` | Rename/move to `13_schemas/` |
> | `70_registries` | Rename to `12_registries/` |
> | `70_strategy` | Move under `02_masterplan/strategy/` |
> 
> Two `70_` folders is already a smell. Fix that.
> 
> ---
> 
> # Where the loose files go
> 
> ## Move to `00_home/`
> 
> | File | Destination |
> |---|---|
> | `_index.md` | `00_home/_index.md` |
> 
> This is the QiSpark front door.
> 
> ---
> 
> ## Move to `12_registries/taxonomy/`
> 
> These are classification/index docs.
> 
> | File | Destination |
> |---|---|
> | `20_bands.md` | `12_registries/taxonomy/20_bands.md` |
> | `30_domains.md` | `12_registries/taxonomy/30_domains.md` |
> | `35_subdomains.md` | `12_registries/taxonomy/35_subdomains.md` |
> 
> These are “what categories exist?” docs.
> 
> ---
> 
> ## Move to `06_architecture/data/`
> 
> These explain how data moves or exists in the system.
> 
> | File | Destination |
> |---|---|
> | `40_data.md` | `06_architecture/data/40_data.md` |
> | `45_data_pipelines.md` | `06_architecture/data/45_data_pipelines.md` |
> | `160_vectorization_pipeline.md` | `06_architecture/data/160_vectorization_pipeline.md` |
> 
> ---
> 
> ## Move to `06_architecture/maps/`
> 
> | File | Destination |
> |---|---|
> | `60_directory_tree.md` | `06_architecture/maps/60_directory_tree.md` |
> | `65_qiaccess_map.md` | `06_architecture/maps/65_qiaccess_map.md` |
> | `65_qiaccess_map.mmd` | `06_architecture/maps/65_qiaccess_map.mmd` |
> 
> These are global maps, not root files.
> 
> ---
> 
> ## Move to `13_schemas/`
> 
> These are structure/model/schema docs.
> 
> | File | Destination |
> |---|---|
> | `70_object_model.md` | `13_schemas/70_object_model.md` |
> | `75_objects.md` | `13_schemas/75_objects.md` |
> | `90_schema.md` | `13_schemas/90_schema.md` |
> | `100_metadata.md` | `13_schemas/100_metadata.md` |
> | `110_front_matter.md` | `13_schemas/110_front_matter.md` |
> 
> This folder is for “how our structured docs/data should look.”
> 
> ---
> 
> ## Move to `04_rules/`
> 
> These are hard operating rules.
> 
> | File | Destination |
> |---|---|
> | `120_storage.md` | `04_rules/storage/120_storage.md` |
> | `130_placement_rules.md` | `04_rules/placement/130_placement_rules.md` |
> | `Access_And_Exposure_Rules.md` | `04_rules/security/Access_And_Exposure_Rules.md` |
> | `policies.md` | `04_rules/policies/policies.md` |
> 
> ---
> 
> ## Move to `05_standards/`
> 
> These are formatting/process standards.
> 
> | File | Destination |
> |---|---|
> | `140_exports.md` | `05_standards/exports/140_exports.md` |
> | `150_evidence.md` | `05_standards/evidence/150_evidence.md` |
> 
> Evidence files themselves do **not** belong here. This is only the standard for how evidence should be named, stored, indexed, and referenced.
> 
> ---
> 
> # Clean QiSpark meaning
> 
> QiSpark should answer:
> 
> ```text
> What is QiEOS?
> What is the current plan?
> What are the rules?
> What are the standards?
> Where does something belong?
> What did we decide?
> What should agents follow?
> What is the current architecture?
> ```
> 
> QiSpark should **not** hold:
> 
> ```text
> actual app code
> actual server configs
> actual legal evidence
> actual finance records
> actual care records
> actual Supabase migrations
> actual project working files
> ```
> 
> It can have the **rules and maps** for those things. The real content lives in the mirror folders.
> 
> ---
> 
> # Final cleaned root
> 
> After cleanup, it should feel like this:
> 
> ```text
> 10_QiSpark/
> ├── 00_home/
> │   └── _index.md
> ├── 01_qieos/
> ├── 02_masterplan/
> │   ├── roadmaps/
> │   ├── strategy/
> │   └── hour_plans/
> ├── 03_principles/
> ├── 04_rules/
> │   ├── placement/
> │   ├── policies/
> │   ├── security/
> │   └── storage/
> ├── 05_standards/
> │   ├── evidence/
> │   └── exports/
> ├── 06_architecture/
> │   ├── blueprints/
> │   ├── data/
> │   └── maps/
> ├── 07_guides/
> ├── 08_services/
> ├── 09_decisions/
> ├── 10_prompts/
> ├── 11_templates/
> ├── 12_registries/
> │   └── taxonomy/
> ├── 13_schemas/
> ├── 14_reports/
> └── 90_archive/
> ```
> 
> ## My ruling
> 
> The loose files are mostly **not random**. They are old QiEOS/QiSpark spine docs that need to be filed.
> 
> Do **not** delete them yet.  
> Move them into the folders above.  
> Then root becomes clean, and QiSpark becomes what it should be:
> 
> > **the docs/governance brain for the whole QiEOS system.**

### User
> also dont gforget that this docs site is not just the techncial shit, its how i manage and navigate my life so all my life parameters and stuff are part of this.

### Assistant
> Exactly. **QiSpark is not a dev docs site.** It is your **life operating manual + system governance site**.
> 
> So the distinction is:
> 
> ```text
> QiSpark = how Cody’s life/system is supposed to run
> QiNexus/QiVault = the actual files, evidence, records, documents
> QiLife/Cadence = the active working cockpit
> QiSystem/QiServer/QiApps = the technical implementation
> ```
> 
> ## Correct QiSpark scope
> 
> QiSpark should include both:
> 
> | Area | Belongs in QiSpark? | Example |
> |---|---:|---|
> | QiEOS doctrine | Yes | “What is QiEOS?” |
> | Folder rules | Yes | “Where does a legal document go?” |
> | Technical standards | Yes | frontmatter, naming, schemas |
> | Agent instructions | Yes | Codex/Gemini/OpenClaw rules |
> | Life parameters | **Yes** | sleep rules, work blocks, care priorities, safety constraints |
> | Daily/weekly planning method | **Yes** | hour plan, triage rules, reset routine |
> | Actual legal evidence | No | goes in QiNexus legal |
> | Actual finance ledger | No | goes in finance system/QiNexus |
> | Actual care records | No | goes in QiNexus/Care/QiLife |
> 
> ## Add this folder
> 
> Your structure needs a dedicated life-ops section:
> 
> ```text
> 10_QiSpark/
> ├── 00_home/
> ├── 01_qieos/
> ├── 02_masterplan/
> ├── 03_principles/
> ├── 04_rules/
> ├── 05_standards/
> ├── 06_architecture/
> ├── 07_guides/
> ├── 08_life_parameters/
> ├── 09_services/
> ├── 10_decisions/
> ├── 11_prompts/
> ├── 12_templates/
> ├── 13_registries/
> ├── 14_schemas/
> ├── 15_reports/
> └── 90_archive/
> ```
> 
> I would rename your current `08_services` to `09_services`, because **life parameters are more central than services**.
> 
> ## What goes in `08_life_parameters/`
> 
> ```text
> 08_life_parameters/
> ├── 00_index.md
> ├── 10_identity_context.md
> ├── 20_priorities.md
> ├── 30_constraints.md
> ├── 40_capacity_energy.md
> ├── 50_daily_operating_rules.md
> ├── 60_weekly_rhythm.md
> ├── 70_caregiving_rules.md
> ├── 80_money_rules.md
> ├── 90_relationship_boundaries.md
> ├── 100_safety_rules.md
> └── 110_decision_filters.md
> ```
> 
> ## Plain-English meaning
> 
> This folder answers:
> 
> ```text
> What matters most right now?
> What can I realistically do in a day?
> What do I do when I’m tired?
> What gets priority: money, mom, app, sleep, legal, food?
> What are my hard boundaries?
> What rules keep me safe?
> How do I decide what to work on next?
> What should agents know before planning my day?
> ```
> 
> That absolutely belongs in QiSpark.
> 
> ## The corrected doctrine
> 
> QiSpark should govern:
> 
> ```text
> technical system
> life system
> planning system
> file system
> agent system
> decision system
> ```
> 
> But it should not store every raw record.
> 
> So yes:
> 
> > QiSpark is the docs site for **how your life and QiEOS operate**, not just “technical shit.”
> 
> That means life parameters are first-class docs, not random personal notes.

### User
> ok but you didnt tell me where the files need to go to.

### Assistant
> You’re right. Here is the **actual filing map**.
> 
> ## Final QiSpark root folders
> 
> Use this root:
> 
> ```text
> 10_QiSpark/
> ├── 00_home/
> ├── 01_qieos/
> ├── 02_masterplan/
> ├── 03_principles/
> ├── 04_rules/
> ├── 05_standards/
> ├── 06_architecture/
> ├── 07_guides/
> ├── 08_life_parameters/
> ├── 09_services/
> ├── 10_decisions/
> ├── 11_prompts/
> ├── 12_templates/
> ├── 13_registries/
> ├── 14_schemas/
> ├── 15_reports/
> └── 90_archive/
> ```
> 
> ---
> 
> # Move your existing folders like this
> 
> | Current folder | Move / rename to |
> |---|---|
> | `00_home` | keep |
> | `01_qieos` | keep |
> | `02_masterplan` | keep |
> | `03_principles` | keep |
> | `04_rules` | keep |
> | `05_standards` | keep |
> | `06_arcitecture` | rename to `06_architecture` |
> | `07_guides` | keep |
> | `08_services` | rename/move to `09_services` |
> | `09_decisions` | rename/move to `10_decisions` |
> | `10_prompts` | rename/move to `11_prompts` |
> | `11_templates` | rename/move to `12_templates` |
> | `20_blueprints` | move into `06_architecture/20_blueprints/` |
> | `30_roadmaps` | move into `02_masterplan/30_roadmaps/` |
> | `40_reports` | move into `15_reports/` |
> | `50_schemas` | move into `14_schemas/` |
> | `70_registries` | move into `13_registries/` |
> | `70_strategy` | move into `02_masterplan/20_strategy/` |
> | `90_archive` | keep |
> 
> Create new:
> 
> ```text
> 08_life_parameters/
> ```
> 
> ---
> 
> # Move the loose root files here
> 
> ## Home
> 
> | File | Destination |
> |---|---|
> | `_index.md` | `00_home/_index.md` |
> 
> ---
> 
> ## Registries / taxonomy
> 
> | File | Destination |
> |---|---|
> | `20_bands.md` | `13_registries/10_taxonomy/20_bands.md` |
> | `30_domains.md` | `13_registries/10_taxonomy/30_domains.md` |
> | `35_subdomains.md` | `13_registries/10_taxonomy/35_subdomains.md` |
> 
> ---
> 
> ## Architecture / data maps
> 
> | File | Destination |
> |---|---|
> | `40_data.md` | `06_architecture/30_data/40_data.md` |
> | `45_data_pipelines.md` | `06_architecture/30_data/45_data_pipelines.md` |
> | `160_vectorization_pipeline.md` | `06_architecture/30_data/160_vectorization_pipeline.md` |
> 
> ---
> 
> ## Architecture / system maps
> 
> | File | Destination |
> |---|---|
> | `60_directory_tree.md` | `06_architecture/10_maps/60_directory_tree.md` |
> | `65_qiaccess_map.md` | `06_architecture/10_maps/65_qiaccess_map.md` |
> | `65_qiaccess_map.mmd` | `06_architecture/10_maps/65_qiaccess_map.mmd` |
> 
> ---
> 
> ## Schemas / structured docs
> 
> | File | Destination |
> |---|---|
> | `70_object_model.md` | `14_schemas/10_object_model/70_object_model.md` |
> | `75_objects.md` | `14_schemas/10_object_model/75_objects.md` |
> | `90_schema.md` | `14_schemas/20_schema/90_schema.md` |
> | `100_metadata.md` | `14_schemas/30_metadata/100_metadata.md` |
> | `110_front_matter.md` | `14_schemas/40_frontmatter/110_front_matter.md` |
> 
> ---
> 
> ## Rules
> 
> | File | Destination |
> |---|---|
> | `120_storage.md` | `04_rules/20_storage/120_storage.md` |
> | `130_placement_rules.md` | `04_rules/10_placement/130_placement_rules.md` |
> | `Access_And_Exposure_Rules.md` | `04_rules/30_security/Access_And_Exposure_Rules.md` |
> | `policies.md` | `04_rules/40_policies/policies.md` |
> 
> ---
> 
> ## Standards
> 
> | File | Destination |
> |---|---|
> | `140_exports.md` | `05_standards/20_exports/140_exports.md` |
> | `150_evidence.md` | `05_standards/30_evidence/150_evidence.md` |
> 
> ---
> 
> # Add life parameter files here
> 
> Create these in:
> 
> ```text
> 08_life_parameters/
> ```
> 
> ```text
> 08_life_parameters/
> ├── 00_index.md
> ├── 10_identity_context.md
> ├── 20_priorities.md
> ├── 30_constraints.md
> ├── 40_capacity_energy.md
> ├── 50_daily_operating_rules.md
> ├── 60_weekly_rhythm.md
> ├── 70_caregiving_rules.md
> ├── 80_money_rules.md
> ├── 90_relationship_boundaries.md
> ├── 100_safety_rules.md
> └── 110_decision_filters.md
> ```
> 
> These are not “random personal notes.” These are the rules for how your life system runs.
> 
> ---
> 
> # Clean root after moving
> 
> After cleanup, the root should **not** have all those loose files.
> 
> It should look like:
> 
> ```text
> 10_QiSpark/
> ├── 00_home/
> ├── 01_qieos/
> ├── 02_masterplan/
> ├── 03_principles/
> ├── 04_rules/
> ├── 05_standards/
> ├── 06_architecture/
> ├── 07_guides/
> ├── 08_life_parameters/
> ├── 09_services/
> ├── 10_decisions/
> ├── 11_prompts/
> ├── 12_templates/
> ├── 13_registries/
> ├── 14_schemas/
> ├── 15_reports/
> └── 90_archive/
> ```
> 
> That’s the clean version: **QiSpark root = categories only. Files go inside the category folders.**

### User
> here is what i currently have {
>   "name": "10_QiSpark",
>   "path": "c:\\QiLabs\\10_QiSpark",
>   "type": "directory",
>   "children": [
>     {
>       "name": "QiDNA",
>       "type": "folder",
>       "children": [
>         {
>           "name": "docs",
>           "type": "folder",
>           "children": [
>             {
>               "name": "00_QiLabs.workspace",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "codex.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "10_QiSpark",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "archive",
>                   "type": "folder"
>                 },
>                 {
>                   "name": "blueprints",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "100_metadata.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "10_identity (2).md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "10_identity.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "10_infrastructure_layout.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "110_front_matter.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "20_bands.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "20_structure.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "20_system_model (2).md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "20_system_model.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "30_component_map (2).md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "30_component_map.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "30_domains.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "35_subdomains.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "40_service_boundaries (2).md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "40_service_boundaries.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "50_data_flow (2).md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "50_data_flow.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "60_device_model (2).md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "60_device_model.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "60_directory_tree.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "65_qiaccess_map.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "65_qiaccess_map.mmd",
>                       "type": "file"
>                     },
>                     {
>                       "name": "70_runtime_zones (2).md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "70_runtime_zones.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "App_Flow.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "Data_Flow.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "Mom_Care_Blueprint.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "QiConnect_Blueprint.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "QiLabs_Blueprint.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "QiMemory_Blueprint.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "QiVault_Blueprint.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "Runtime_Zones.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "Security_Model.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "Service_Map.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "System_Map.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index (2).md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "cases.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "qilabs_final_target_tree.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "decisions",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "0001_personal_lifedesk_model.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "0002_qibit_as_atomic_unit.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "0003_timeline_as_spine.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "0004_context_dock_over_wiki.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "0005_repo_docs_indexed_in_app.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "0006_clean_core_with_legacy_bridge.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "0007_app_managed_storage_and_sync.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "0008_managed_document_vault_dup_allergic.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "0009_agent_first_copilot_cockpit.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "0010_spaces_for_scoped_shared_access.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0000_template.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0001_QiLabs_Root_Model.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0001_QiOS_DNA_As_Master_Doctrine_Repo.mdx",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0001_blueprint_scope.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0002_QiAccess_As_QiSpark_HTML_Landing_Page.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0002_single_domain_rule.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0003_WikiJS_As_Knowledge_Base.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0003_band_model.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0004_Google_Drive_As_Storage_Backbone.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0004_single_account_modular_mode.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0005_QiVault_As_QiNexus_Home.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0005_fleet_orchestration.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0006_QiMemory_As_Semantic_Layer.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0006_QiSystem_Numbering_Bands.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0006_narrative_and_knowledge_consolidation.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0007_unified_front_matter_and_progressive_doc_topology.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0008_qilabs_root.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0009_backup_server_control_plane_and_public_edge_pattern.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0010_qios_namespace_as_routing_metadata_layer.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0011_homepage_powered_qiaccess.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0012_data_strategy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0013_folder_documentation_model.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0014_topology_constraints.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0015_build_strategy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0016_ai_auditor_role.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0017_canonical_vocabulary_and_v1_direction.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0018_supabase_qilife_data_authority.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ADR-0019_directus_as_supabase_admin_and_api_layer.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_Decisions.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "guides",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "45_data_pipelines.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "Docker_Basics.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "HTML_CSS_JS_Basics.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "Local_AI_Basics.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "React_App_Flow.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "Supabase_Basics.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "home",
>                   "type": "folder"
>                 },
>                 {
>                   "name": "masterplan",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "150_qievidence.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "build_sequence.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "positioning.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "priorities.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "system_principles.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "modules",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "10_productivity",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "activitywatch.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "n8n.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "qiledger.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "solidtime.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "120_storage.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "160_vectorization_pipeline.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "40_data.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "70_object_model.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "75_objects.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "service_apps.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "services_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "principles",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "00_principles.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "140_exports.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "prompts",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "chatgpt",
>                       "type": "folder"
>                     },
>                     {
>                       "name": "codex",
>                       "type": "folder"
>                     },
>                     {
>                       "name": "gemini",
>                       "type": "folder"
>                     },
>                     {
>                       "name": "prompt_library",
>                       "type": "folder"
>                     },
>                     {
>                       "name": "prompt_log.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "qieos",
>                   "type": "folder"
>                 },
>                 {
>                   "name": "registries",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "100_metadata.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "10_infrastructure_layout.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "110_front_matter.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "120_storage.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "130_placement_rules.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "140_exports.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "150_qievidence.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "160_vectorization_pipeline.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "2026-05-18_qios_namespace_registry_merged_v2.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "20_bands.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "30_domains.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "40_subdomains.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "60_directory_tree.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "70_object_model.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "80_objects.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "90_schema.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "QiRealms_seed.json",
>                       "type": "file"
>                     },
>                     {
>                       "name": "QiTagClasses_schema.json",
>                       "type": "file"
>                     },
>                     {
>                       "name": "QiTags_seed.json",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "band_registry.schema.json",
>                       "type": "file"
>                     },
>                     {
>                       "name": "band_registry.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "band_registry_v2.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "deprecation_registry.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "domain_registry.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "folder_registry.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "infrastructure_registry.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "namespace_registry.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "realms_registry.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "registry_folders.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "registry_realms.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "sensitivity_classification.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "slugs_mapping.json",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "reports",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "10_logs",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "10_changelog.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "2026-05-16_dev_session_directory_markmind_mapper.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "2026-05-17_open_loop_reset_paperless_ingestion_runbook.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "70_repo_sync_status_20260516.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "INTEGRATION_COMPLETE.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "integration_summary.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "launcher_ui_mindmap.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "markdownlint_analysis_genesis.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "markdownlint_analysis_remaining.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "markdownlint_final_analysis.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "markdownlint_quick_reference.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "markdownlint_review_summary.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "markdownlint_summary.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "20_notes",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "discussion26-07-01.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "30_prompts",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "cockpit_gui_prompt.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "40_reconciliation",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "2026-06-09_codex_reconciliation_brief.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "2026-06-09_initial_reconciliation.mdx",
>                           "type": "file"
>                         },
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "50_superseeded",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "10_from_30_qiserver_docs",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "10_docs",
>                               "type": "folder",
>                               "children": [
>                                 {
>                                   "name": "QiAlly Call Ecosystem & Gina Voice Architecture.md",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "_index.md",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "ui_contracts_v1.md",
>                                   "type": "file"
>                                 }
>                               ]
>                             },
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "20_from_30_qiserver_json_review",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "10_json",
>                               "type": "folder",
>                               "children": [
>                                 {
>                                   "name": "bio_contact_info.json",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "client_memberships_rows.json",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "intake_form_schema.json",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "kb_spaces_rows.json",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "message_feedback.json",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "portfolio-content.json",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "portfolio-projects.json",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "systemInfoCMD.json",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "user.json",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "voice_mapper_rules.json",
>                                   "type": "file"
>                                 }
>                               ]
>                             }
>                           ]
>                         },
>                         {
>                           "name": "30_from_30_qiserver_legacy",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "10_legacy",
>                               "type": "folder",
>                               "children": [
>                                 {
>                                   "name": "QiCodex.csv",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "manifest.txt",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "opensourcetools.txt",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "qios_00_genesis.canvas",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "qios_runtime_mindmap.canvas",
>                                   "type": "file"
>                                 }
>                               ]
>                             },
>                             {
>                               "name": "index.html",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "40_from_30_qiserver_prompts",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "10_qios_cursor_prompts",
>                               "type": "folder",
>                               "children": [
>                                 {
>                                   "name": "_index.md",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "index.html",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "install_ingestion_worker.md",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "project_prompt.md.md",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "qicompiler_add_prompt.md",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "qicompiler_orchestrator_prompt.md",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "qimatrix_csv_prompt.md",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "qimatrix_sql_prompt.md",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "qimatrix_yaml_prompt.md",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "step3_tree_compiler_prompt.md",
>                                   "type": "file"
>                                 },
>                                 {
>                                   "name": "user_prompt.md.md",
>                                   "type": "file"
>                                 }
>                               ]
>                             },
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "2025-11-18_qicodex_protocol_batch_overview.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "40_legacy_csv_migration_plan.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "50_legacy_salvage.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "QiAccess_Start_Blueprint.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "README.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "gina_n8n_workflows.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "qi_os_home_blueprint.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "tech_stack_markmind.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "2026-05-24_qiaccess_homepage_conversion_report.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "2026-05-24_qiaccess_homepage_local_validation_report.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "2026-05-24_qilinks_admin_and_visual_map_plan.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "30_migration_notes.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "Current_Project_State.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "roadmaps",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "Mom_Care_Roadmap.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "QiAccess_Roadmap.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "QiLabs_Roadmap.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "QiMemory_Roadmap.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "rules",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "130_placement_rules.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "20_glossary.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "Access_And_Exposure_Rules.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "Source_of_Truth_Rules.mdx",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index (2).md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "active_runtime_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "agent_governance_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "bootstrap_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "content_metadata_profile (2).yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "content_metadata_profile.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "contribution_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "eos_frontmatter.schema.json",
>                       "type": "file"
>                     },
>                     {
>                       "name": "front_matter_schema_v1.csv",
>                       "type": "file"
>                     },
>                     {
>                       "name": "frontmatter.schema.json",
>                       "type": "file"
>                     },
>                     {
>                       "name": "fs_ignore.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "fs_ignore_v1.csv",
>                       "type": "file"
>                     },
>                     {
>                       "name": "legacy_quarantine_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "lifecycle_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "master_schema_governance.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "merge_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "naming_rules (2).yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "naming_rules.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "pdf_standards.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "placement_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "policies.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "qinexus_freeze_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "qios_constitution_schema_v1.json",
>                       "type": "file"
>                     },
>                     {
>                       "name": "qios_constitution_v1.json",
>                       "type": "file"
>                     },
>                     {
>                       "name": "qios_matrix.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "qios_rules_v1.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "qios_rules_v1_1.csv",
>                       "type": "file"
>                     },
>                     {
>                       "name": "registry_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "repo_rules (2).yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "repo_rules.yaml",
>                       "type": "file"
>                     },
>                     {
>                       "name": "root_navigation_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "security_data_access_policy.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "schemas",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "90_schema.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "DATABASE_OVERVIEW.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "QiLife_Data_Spine.mdx",
>                       "type": "file"
>                     },
>                     {
>                       "name": "SCHEMA_CATALOG.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_Schema.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "band_registry.schema.json",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "templates",
>                   "type": "folder"
>                 },
>                 {
>                   "name": "README.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "20_QiServer",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "10_ai_compute",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "neo4j.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "ollama.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "open_webui.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "qdrant.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "20_cockpit",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "cockpit_command_menu.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "30_infrastructure",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "10_cockpit",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "cockpit_command_menu.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "cloudflare.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "docker_compose.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "gethomepage.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "portainer.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "tailscale.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "uptime_kuma.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "40_manifests",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "QiSpark_File_Manifest.mdx",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "50_tools",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "operator_tools.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "60_workers",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "system_workers.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "2026-06-08_qilife_governance_audit.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "60_qiaccess_start_legacy_quarantine.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "QiAccess_Server_Runbook.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "Service_Map.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_20_QiServer.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "cloudflare.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "current_project_state.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "docker_compose.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "gethomepage.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "portainer.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "public_interfaces.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qiserver_runbook.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "runtime.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "runtime_profile.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "server_data_source.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "tailscale.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "uptime_kuma.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "30_QiMemory",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "100_paperless",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "10_ingestion",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "10_paperless",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "20_drive_imports",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "30_manual_uploads",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "40_email_exports",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "50_web_clips",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "file_inventory_scanner.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "qiingest_pipeline.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "routing_approval_flow.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "110_pipelines",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "data_pipelines.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "120_tools",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "10_paperless",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "nocodb.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "obsidian_qidocs.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "wikijs.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "20_extraction",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "10_ocr_text",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "20_markdown_exports",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "30_transcripts",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "40_metadata",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "50_clean_text",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "30_chunking",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "10_chunk_manifests",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "20_chunk_rules",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "30_source_maps",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "40_quality_checks",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "40_embeddings",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "10_qdrant",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "20_embedding_models",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "30_collection_manifests",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "40_rebuild_logs",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "50_vector_quality_tests",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "50_graphs",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "10_graphify",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "20_markmap",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "30_entity_maps",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "40_relationship_exports",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "50_graph_quality_reports",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "60_retrieval",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "10_rag_profiles",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "20_query_logs",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "30_retrieval_tests",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "40_prompt_contexts",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "50_source_citation_tests",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "70_memory",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "10_gina_profiles",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "20_durable_facts",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "30_session_summaries",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "40_preference_maps",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "50_context_packs",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "80_sync_backups",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "10_index_snapshots",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "20_backup_manifests",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "30_restore_points",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "40_sync_manifests",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "90_legacy_tools",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "nocodb.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "obsidian_qidocs.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "wikijs.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "_30_QiMemory.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "40_QiVault",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "00_inbox",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "01_workbench",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "02_timeline",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "03_life",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "2026-05-18_birthday_boundaries_and_the_cost_of_carrying_everything.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "05_business",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "06_finance",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "07_legal",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "08_tech",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "09_assets",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_markmind_export.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_markmind_export_with_content.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "master_map.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "10_data",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "11_reference",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "12_archive",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "13_system",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "23_My_Drive_Model",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "index.mdx",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "_40_QiVault.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "50_QiConnect",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "10_apis",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "portal_api.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "20_integrations",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "external_integrations.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "30_workflows",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "Automation_Backlog.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "Core_Workflows.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "QiIngest_Pipeline.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "_50_QiConnect.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "external_integrations.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "60_QiApps",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "10_GINA",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "20_QiAccess",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "overview.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "wiki_publish_plan.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "30_QiJourney",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "index.mdx",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "40_QiLife",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "00_overview",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "00_qilife_canvas.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "01_product_doctrine.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "02_glossary.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "100_planning",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "build_checklist.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "open_questions.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "validation_checklist.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "10_product",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "00_master_build_spec.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "01_qibit_lifecycle.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "02_user_flows.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "03_build_phases.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "04_build_doctrine.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "05_agent_first_product_doctrine.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "20_architecture",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "00_information_architecture.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "01_app_shell.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "02_context_dock.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "03_knowledge_model.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "04_repo_docs_to_inapp_knowledge.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "05_storage_and_sync_control_center.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "06_spaces_and_scoped_access.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "07_agent_copilot_architecture.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "30_data_model",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "00_data_model_spine.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "01_qibits.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "02_threads_actions.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "03_people_money_documents.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "04_knowledge_links.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "05_seed_data.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "06_database_stability_strategy.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "07_legacy_data_bridge.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "08_storage_sync_settings.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "09_document_vault_and_dedupe.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "10_spaces_access_schema.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "40_ui_flows",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "00_app_flow_and_screens.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "01_capture_ingestion_review_flow.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "02_cockpit_and_agent_flow.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "50_modules",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "100_money",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ai_behaviors.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "context_dock.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "data_dependencies.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ui_flow.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "10_actions",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ai_behaviors.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "context_dock.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "data_dependencies.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ui_flow.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "110_people",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ai_behaviors.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "context_dock.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "data_dependencies.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ui_flow.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "120_qibits",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ai_behaviors.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "context_dock.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "data_dependencies.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ui_flow.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "130_review",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "140_spaces",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "150_storage",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "160_threads",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ai_behaviors.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "context_dock.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "data_dependencies.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ui_flow.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "170_timeline",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ai_behaviors.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "context_dock.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "data_dependencies.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ui_flow.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "20_agent",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "30_ask_qilife",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ai_behaviors.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "context_dock.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "data_dependencies.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ui_flow.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "40_calendar",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ai_behaviors.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "context_dock.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "data_dependencies.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ui_flow.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "50_capture",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "60_documents",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ai_behaviors.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "context_dock.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "data_dependencies.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ui_flow.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "70_inbox",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ai_behaviors.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "context_dock.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "data_dependencies.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ui_flow.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "80_ingestion",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "90_knowledge",
>                           "type": "folder",
>                           "children": [
>                             {
>                               "name": "_index.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ai_behaviors.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "context_dock.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "data_dependencies.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "overview.md",
>                               "type": "file"
>                             },
>                             {
>                               "name": "ui_flow.md",
>                               "type": "file"
>                             }
>                           ]
>                         },
>                         {
>                           "name": "00_module_map.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "60_ai_layer",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "00_ai_layer_blueprint.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "01_ai_service_contracts.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "02_ai_review_workflow.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "70_deployment",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "00_local_dev.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "01_future_docker.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "02_future_qiserver.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "80_prompts",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "00_codex_build_prompt_v1.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "01_codex_review_prompt.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "02_will_be_done_research_prompt.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "90_decisions",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "0001_personal_lifedesk_model.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "0002_qibit_as_atomic_unit.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "0003_timeline_as_spine.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "0004_context_dock_over_wiki.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "0005_repo_docs_indexed_in_app.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "0006_clean_core_with_legacy_bridge.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "0007_app_managed_storage_and_sync.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "0008_managed_document_vault_dup_allergic.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "0009_agent_first_copilot_cockpit.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "0010_spaces_for_scoped_shared_access.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "_QiLife.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "index.mdx",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "50_Sites",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "10_legacy_static_site",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "_site.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "index.html",
>                           "type": "file"
>                         },
>                         {
>                           "name": "script.js",
>                           "type": "file"
>                         },
>                         {
>                           "name": "style.css",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "60_applications",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "10_CareLite",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "20_qinote",
>                       "type": "folder",
>                       "children": [
>                         {
>                           "name": "_index.md",
>                           "type": "file"
>                         },
>                         {
>                           "name": "qinote_salvage_extract.md",
>                           "type": "file"
>                         }
>                       ]
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "admin.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "carelite.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "firefly.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "portal.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "roadmap.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "70_interfaces",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "public_interfaces.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "80_productivity",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "activitywatch.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "n8n.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "qiledger.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "solidtime.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "_60_QiApps.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "stylesheets",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "custom.css",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "index.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "site",
>           "type": "folder"
>         },
>         {
>           "name": "mkdocs.yml",
>           "type": "file"
>         },
>         {
>           "name": "number_folders.py",
>           "type": "file"
>         },
>         {
>           "name": "rebuild_nav.py",
>           "type": "file"
>         },
>         {
>           "name": "requirements.txt",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "_start_here",
>       "type": "folder",
>       "children": [
>         {
>           "name": "assets",
>           "type": "folder",
>           "children": [
>             {
>               "name": "fonts",
>               "type": "folder"
>             },
>             {
>               "name": "icons",
>               "type": "folder"
>             },
>             {
>               "name": "images",
>               "type": "folder"
>             }
>           ]
>         },
>         {
>           "name": "css",
>           "type": "folder",
>           "children": [
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "data",
>           "type": "folder",
>           "children": [
>             {
>               "name": "links.json",
>               "type": "file"
>             },
>             {
>               "name": "priorities.json",
>               "type": "file"
>             },
>             {
>               "name": "sections.json",
>               "type": "file"
>             },
>             {
>               "name": "services.json",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "docs",
>           "type": "folder",
>           "children": [
>             {
>               "name": "QiAccess_Landing_Page_Map.md",
>               "type": "file"
>             },
>             {
>               "name": "QiAccess_Link_Rules.md",
>               "type": "file"
>             },
>             {
>               "name": "QiAccess_Start_Blueprint.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "js",
>           "type": "folder",
>           "children": [
>             {
>               "name": "main.js",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "README.md",
>           "type": "file"
>         },
>         {
>           "name": "index.html",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "assets",
>       "type": "folder",
>       "children": [
>         {
>           "name": "diagrams",
>           "type": "folder",
>           "children": [
>             {
>               "name": "2026-05-17_supabase_markmind.md",
>               "type": "file"
>             },
>             {
>               "name": "blueprint_map.md",
>               "type": "file"
>             },
>             {
>               "name": "diagrams.md",
>               "type": "file"
>             },
>             {
>               "name": "markmind-data.json",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "exports",
>           "type": "folder"
>         },
>         {
>           "name": "images",
>           "type": "folder",
>           "children": [
>             {
>               "name": "_QiOS_Master_Document.jpg",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "templates",
>           "type": "folder",
>           "children": [
>             {
>               "name": "_index.md",
>               "type": "file"
>             },
>             {
>               "name": "adr_template.md",
>               "type": "file"
>             },
>             {
>               "name": "appendix_template.md",
>               "type": "file"
>             },
>             {
>               "name": "artifact_template.md",
>               "type": "file"
>             },
>             {
>               "name": "dev_session_template.md",
>               "type": "file"
>             },
>             {
>               "name": "note_template.md",
>               "type": "file"
>             },
>             {
>               "name": "operational_template.md",
>               "type": "file"
>             },
>             {
>               "name": "page_template.md",
>               "type": "file"
>             },
>             {
>               "name": "registry_reference_template.md",
>               "type": "file"
>             },
>             {
>               "name": "standard_template.md",
>               "type": "file"
>             },
>             {
>               "name": "templates.md",
>               "type": "file"
>             }
>           ]
>         }
>       ]
>     },
>     {
>       "name": "tools",
>       "type": "folder",
>       "children": [
>         {
>           "name": "testing",
>           "type": "folder",
>           "children": [
>             {
>               "name": "momscare",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "2026-05-17_momcare_app_qa_checklist.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "qiaccessstart",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "2026-05-17_qiaccess_start_qa_checklist.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qiaccessstart.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "40_dev_testing.md",
>               "type": "file"
>             },
>             {
>               "name": "Access_And_Exposure_Rules.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "_index.md",
>           "type": "file"
>         },
>         {
>           "name": "build.js",
>           "type": "file"
>         },
>         {
>           "name": "build_docs_json.py",
>           "type": "file"
>         },
>         {
>           "name": "build_folder_indexes.py",
>           "type": "file"
>         },
>         {
>           "name": "cleanup_qispark.py",
>           "type": "file"
>         },
>         {
>           "name": "code_extractor.py",
>           "type": "file"
>         },
>         {
>           "name": "operator_tools.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": ".gitignore",
>       "type": "file"
>     },
>     {
>       "name": "Assistant.md",
>       "type": "file"
>     },
>     {
>       "name": "README.md",
>       "type": "file"
>     },
>     {
>       "name": "codex.md",
>       "type": "file"
>     },
>     {
>       "name": "skills-lock.json",
>       "type": "file"
>     }
>   ],
>   "metadata": {
>     "generated": "2026-06-18T19:04:39.448Z",
>     "generator": "FileTree Pro Extension",
>     "version": "0.2.0",
>     "showIcons": false,
>     "maxDepth": 10
>   }
> }

### Assistant
> Yes. Now I see the real problem.
> 
> You currently have **three different things mixed together**:
> 
> ```text
> 10_QiSpark/
> ├── QiDNA/          ← actual MkDocs documentation site source
> ├── _start_here/    ← QiAccess Start landing page
> ├── assets/         ← shared images/templates/diagrams
> ├── tools/          ← scripts/build tools
> └── loose root files
> ```
> 
> That is why it feels messy. **QiDNA should not be a folder inside QiSpark.** QiSpark *is* the docs/governance site. So we flatten this.
> 
> # Final clean `10_QiSpark` root
> 
> Your root should be:
> 
> ```text
> 10_QiSpark/
> ├── docs/
> ├── qiaccess_start/
> ├── assets/
> ├── tools/
> ├── site/
> ├── .gitignore
> ├── README.md
> ├── codex.md
> ├── mkdocs.yml
> ├── requirements.txt
> └── skills-lock.json
> ```
> 
> That’s it.
> 
> Root should **not** have `QiDNA/` anymore.
> 
> ---
> 
> # Main move
> 
> ## Rename/move this:
> 
> ```text
> 10_QiSpark/QiDNA/docs/
> ```
> 
> to:
> 
> ```text
> 10_QiSpark/docs/
> ```
> 
> Then move:
> 
> ```text
> 10_QiSpark/QiDNA/mkdocs.yml
> 10_QiSpark/QiDNA/requirements.txt
> 10_QiSpark/QiDNA/number_folders.py
> 10_QiSpark/QiDNA/rebuild_nav.py
> 10_QiSpark/QiDNA/site/
> ```
> 
> up to:
> 
> ```text
> 10_QiSpark/
> ```
> 
> Then archive the empty old `QiDNA/` wrapper.
> 
> ---
> 
> # What goes inside `docs/`
> 
> Inside `docs/`, use this:
> 
> ```text
> docs/
> ├── index.md
> ├── 00_home/
> ├── 01_qieos/
> ├── 02_masterplan/
> ├── 03_principles/
> ├── 04_rules/
> ├── 05_standards/
> ├── 06_architecture/
> ├── 07_guides/
> ├── 08_life_parameters/
> ├── 09_services/
> ├── 10_decisions/
> ├── 11_prompts/
> ├── 12_templates/
> ├── 13_registries/
> ├── 14_schemas/
> ├── 15_reports/
> ├── 16_module_maps/
> ├── stylesheets/
> └── 90_archive/
> ```
> 
> This keeps QiSpark as the **docs/governance/life navigation site**.
> 
> ---
> 
> # Move map from your current tree
> 
> ## Current `QiDNA/docs/10_QiSpark/`
> 
> Move these like this:
> 
> | Current path | New path |
> |---|---|
> | `QiDNA/docs/10_QiSpark/home/` | `docs/00_home/` |
> | `QiDNA/docs/10_QiSpark/qieos/` | `docs/01_qieos/` |
> | `QiDNA/docs/10_QiSpark/masterplan/` | `docs/02_masterplan/` |
> | `QiDNA/docs/10_QiSpark/roadmaps/` | `docs/02_masterplan/30_roadmaps/` |
> | `QiDNA/docs/10_QiSpark/principles/` | `docs/03_principles/` |
> | `QiDNA/docs/10_QiSpark/rules/` | `docs/04_rules/` |
> | `QiDNA/docs/10_QiSpark/guides/` | `docs/07_guides/` |
> | `QiDNA/docs/10_QiSpark/modules/` | `docs/09_services/` or `docs/16_module_maps/` depending on file |
> | `QiDNA/docs/10_QiSpark/decisions/` | `docs/10_decisions/` |
> | `QiDNA/docs/10_QiSpark/prompts/` | `docs/11_prompts/` |
> | `QiDNA/docs/10_QiSpark/templates/` | `docs/12_templates/` |
> | `QiDNA/docs/10_QiSpark/registries/` | `docs/13_registries/` |
> | `QiDNA/docs/10_QiSpark/schemas/` | `docs/14_schemas/` |
> | `QiDNA/docs/10_QiSpark/reports/` | `docs/15_reports/` |
> | `QiDNA/docs/10_QiSpark/archive/` | `docs/90_archive/` |
> | `QiDNA/docs/10_QiSpark/README.md` | `docs/00_home/README.md` |
> 
> ---
> 
> # Blueprints split
> 
> Your current `blueprints/` folder is a mixture. File it like this:
> 
> ## Global architecture blueprints
> 
> Move to:
> 
> ```text
> docs/06_architecture/20_blueprints/
> ```
> 
> Files:
> 
> ```text
> 10_infrastructure_layout.md
> 20_structure.md
> 20_system_model.md
> 30_component_map.md
> 40_service_boundaries.md
> 50_data_flow.md
> 60_device_model.md
> 70_runtime_zones.md
> App_Flow.md
> Data_Flow.md
> Runtime_Zones.md
> Security_Model.md
> Service_Map.md
> System_Map.md
> QiLabs_Blueprint.md
> qilabs_final_target_tree.md
> ```
> 
> ## Taxonomy / registries
> 
> Move to:
> 
> ```text
> docs/13_registries/10_taxonomy/
> ```
> 
> Files:
> 
> ```text
> 20_bands.md
> 30_domains.md
> 35_subdomains.md
> ```
> 
> ## Schemas / frontmatter
> 
> Move to:
> 
> ```text
> docs/14_schemas/
> ```
> 
> Files:
> 
> ```text
> 100_metadata.md
> 110_front_matter.md
> ```
> 
> ## Life or domain blueprints
> 
> Move to:
> 
> ```text
> docs/08_life_parameters/90_domain_blueprints/
> ```
> 
> Files:
> 
> ```text
> Mom_Care_Blueprint.md
> QiVault_Blueprint.md
> QiMemory_Blueprint.md
> QiConnect_Blueprint.md
> ```
> 
> Why? Because those are not just technical docs. They describe how your life system is supposed to work.
> 
> ## QiAccess blueprint
> 
> Move to:
> 
> ```text
> docs/06_architecture/30_qiaccess/
> ```
> 
> Files:
> 
> ```text
> 65_qiaccess_map.md
> 65_qiaccess_map.mmd
> QiAccess_Start_Blueprint.md
> ```
> 
> ---
> 
> # Module mirror docs
> 
> These folders currently live under:
> 
> ```text
> QiDNA/docs/
> ├── 20_QiServer/
> ├── 30_QiMemory/
> ├── 40_QiVault/
> ├── 50_QiConnect/
> └── 60_QiApps/
> ```
> 
> Move them to:
> 
> ```text
> docs/16_module_maps/
> ├── 20_qiserver/
> ├── 30_qimemory/
> ├── 40_qivault/
> ├── 50_qiconnect/
> └── 60_qiapps/
> ```
> 
> These are **docs-site mirrors**, not the actual working folders.
> 
> The rule:
> 
> ```text
> docs/16_module_maps/ = what each module is supposed to be
> C:\QiLabs\<module>/ = the actual module
> ```
> 
> That avoids duplication confusion.
> 
> ---
> 
> # QiAccess Start
> 
> Rename this:
> 
> ```text
> _start_here/
> ```
> 
> to:
> 
> ```text
> qiaccess_start/
> ```
> 
> Keep its structure:
> 
> ```text
> qiaccess_start/
> ├── assets/
> ├── css/
> ├── data/
> ├── docs/
> ├── js/
> ├── README.md
> └── index.html
> ```
> 
> Then later the docs can link to it from:
> 
> ```text
> docs/06_architecture/30_qiaccess/
> ```
> 
> ---
> 
> # Assets
> 
> Keep root assets, but clean them:
> 
> ```text
> assets/
> ├── diagrams/
> ├── exports/
> ├── images/
> └── templates/
> ```
> 
> But move the reusable document templates out of `assets/templates/` into:
> 
> ```text
> docs/12_templates/
> ```
> 
> So:
> 
> | Current | New |
> |---|---|
> | `assets/templates/adr_template.md` | `docs/12_templates/adr_template.md` |
> | `assets/templates/note_template.md` | `docs/12_templates/note_template.md` |
> | `assets/templates/page_template.md` | `docs/12_templates/page_template.md` |
> | `assets/templates/standard_template.md` | `docs/12_templates/standard_template.md` |
> | `assets/templates/dev_session_template.md` | `docs/12_templates/dev_session_template.md` |
> | `assets/templates/operational_template.md` | `docs/12_templates/operational_template.md` |
> 
> Keep actual images/diagrams in `assets/`.
> 
> ---
> 
> # Tools
> 
> Keep this:
> 
> ```text
> tools/
> ```
> 
> But testing docs should move into reports/guides.
> 
> | Current | New |
> |---|---|
> | `tools/testing/qiaccessstart/2026-05-17_qiaccess_start_qa_checklist.md` | `docs/15_reports/20_qa/qiaccess_start/2026-05-17_qiaccess_start_qa_checklist.md` |
> | `tools/testing/momscare/2026-05-17_momcare_app_qa_checklist.md` | `docs/15_reports/20_qa/mom_care/2026-05-17_momcare_app_qa_checklist.md` |
> | `tools/testing/Access_And_Exposure_Rules.md` | `docs/04_rules/30_security/Access_And_Exposure_Rules.md` |
> 
> Scripts stay in tools:
> 
> ```text
> tools/build.js
> tools/build_docs_json.py
> tools/build_folder_indexes.py
> tools/cleanup_qispark.py
> tools/code_extractor.py
> ```
> 
> ---
> 
> # Root loose files
> 
> | Current file | Destination |
> |---|---|
> | `Assistant.md` | `docs/11_prompts/assistant/Assistant.md` |
> | `codex.md` | Keep root `codex.md` if it controls agent behavior |
> | `README.md` | Keep root `README.md` |
> | `skills-lock.json` | Keep root |
> | `.gitignore` | Keep root |
> 
> ---
> 
> # Add life parameters folder
> 
> Create:
> 
> ```text
> docs/08_life_parameters/
> ├── 00_index.md
> ├── 10_identity_context.md
> ├── 20_priorities.md
> ├── 30_constraints.md
> ├── 40_capacity_energy.md
> ├── 50_daily_operating_rules.md
> ├── 60_hour_plan.md
> ├── 70_weekly_rhythm.md
> ├── 80_caregiving_rules.md
> ├── 90_money_rules.md
> ├── 100_relationship_boundaries.md
> ├── 110_safety_rules.md
> └── 120_decision_filters.md
> ```
> 
> This is where your real-life operating parameters go.
> 
> Not raw evidence. Not private documents. But the **rules your life system follows**.
> 
> ---
> 
> # Clean final picture
> 
> ```text
> 10_QiSpark/
> ├── docs/
> │   ├── index.md
> │   ├── 00_home/
> │   ├── 01_qieos/
> │   ├── 02_masterplan/
> │   ├── 03_principles/
> │   ├── 04_rules/
> │   ├── 05_standards/
> │   ├── 06_architecture/
> │   ├── 07_guides/
> │   ├── 08_life_parameters/
> │   ├── 09_services/
> │   ├── 10_decisions/
> │   ├── 11_prompts/
> │   ├── 12_templates/
> │   ├── 13_registries/
> │   ├── 14_schemas/
> │   ├── 15_reports/
> │   ├── 16_module_maps/
> │   ├── stylesheets/
> │   └── 90_archive/
> ├── qiaccess_start/
> ├── assets/
> ├── tools/
> ├── site/
> ├── .gitignore
> ├── README.md
> ├── codex.md
> ├── mkdocs.yml
> ├── requirements.txt
> └── skills-lock.json
> ```
> 
> ## My ruling
> 
> The main cleanup is simple:
> 
> > **Promote `QiDNA/docs` to `docs`, move `QiDNA` out of the way, rename `_start_here` to `qiaccess_start`, and make `docs/08_life_parameters` first-class.**
> 
> That gives you one clean docs site, not a docs site trapped inside another docs folder wearing a fake mustache.
