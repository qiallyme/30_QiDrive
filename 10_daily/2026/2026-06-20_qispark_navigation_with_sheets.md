---
layout: page
title: "QiSpark Navigation with Sheets"
slug: "qispark_navigation_with_sheets"
created_at: "2026-06-20 23:48:01"
updated_at: "2026-07-18T11:03:16-04:00"
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
date: 2026-06-20
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a376ced-244c-83ea-bf3c-d763bba04514"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# QiSpark Navigation with Sheets

## Overview
- **Date**: 2026-06-20 23:48:01
- **Conversation ID**: `6a376ced-244c-83ea-bf3c-d763bba04514`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> how do i work on the qispark navigation using sheets or is there another method.

### Assistant
> I’d treat this as a navigation architecture problem, not just a “where do pages go?” problem. The clean answer is probably: use Sheets as the temporary control panel, then generate the real nav from it.

### Assistant
> Yes — **Sheets is a good way to work on QiSpark navigation**, but only as the **control panel**, not the permanent truth.
> 
> The better architecture:
> 
> ```text
> Obsidian / Markdown = actual content
> Sheets / CSV = navigation registry
> docs.json / sidebar / website nav = generated output
> ```
> 
> Do **not** hand-edit navigation in three places. That’s how QiSpark becomes spaghetti with a logo.
> 
> ---
> 
> # Best Method: Navigation Registry Sheet
> 
> Create one Google Sheet called:
> 
> ```text
> QiSpark_Navigation_Registry
> ```
> 
> Each row = **one page, folder, section, or nav item**.
> 
> ## Minimum columns
> 
> Use this first. Don’t overbuild it.
> 
> | Column | Purpose |
> |---|---|
> | `nav_id` | Stable ID, never changes unless deleted |
> | `title` | Human-readable page title |
> | `nav_label` | Short menu label |
> | `type` | `section`, `page`, `index`, `redirect`, `archive` |
> | `parent_id` | What this item sits under |
> | `order` | Sort order |
> | `source_path` | Actual Markdown file path |
> | `public_path` | Website URL path |
> | `status` | `active`, `draft`, `needs_review`, `deprecated` |
> | `visibility` | `public`, `private`, `internal`, `hidden` |
> | `module` | QiSpark, QiDNA, QiSystem, QiServer, QiDrive, etc. |
> | `notes` | Messy thinking / unresolved issue |
> 
> That’s enough.
> 
> ---
> 
> # The Rule
> 
> **QiSpark should hold the thinking layer:**
> 
> ```text
> Doctrine
> Strategy
> Knowledge
> ADRs
> Prompts
> Planning
> Docs
> Navigation Standards
> ```
> 
> But it should **not** become the blob-storage junk drawer.
> 
> So:
> 
> ```text
> QiSpark = meaning, structure, documentation, decisions
> QiDrive / QiNexus = files, evidence, storage
> QiServer = runtime/infrastructure
> QiMemory = semantic/derived knowledge
> ```
> 
> That distinction matters. Otherwise every system starts eating every other system.
> 
> ---
> 
> # Suggested Sheet Tabs
> 
> Use 4 tabs only:
> 
> ## 1. `NAV_ITEMS`
> 
> The main registry.
> 
> This is where you map every page.
> 
> ## 2. `SECTIONS`
> 
> Top-level nav groups.
> 
> Example:
> 
> | section_id | label | order | purpose |
> |---|---:|---:|---|
> | start | Start Here | 10 | Entry point |
> | doctrine | Doctrine | 20 | Rules and principles |
> | architecture | Architecture | 30 | System map |
> | adr | ADRs | 40 | Decisions |
> | prompts | Prompts | 50 | Reusable instruction assets |
> | operations | Operations | 60 | How to work the system |
> 
> ## 3. `REDIRECTS`
> 
> For old names, stale routes, and renamed pages.
> 
> This is important because your naming has shifted a few times.
> 
> Example:
> 
> | old_path | new_path | reason |
> |---|---|---|
> | `/qios-start` | `/start` | Renamed for clarity |
> | `/qinexus` | `/qidrive` | Storage naming clarified |
> 
> ## 4. `AUDIT`
> 
> Use this to track cleanup.
> 
> | issue | page/path | action | priority |
> |---|---|---|---|
> | duplicate nav item | `/docs/index` | merge/remove | high |
> | stale root name | `00_QiEOS` | map to current canonical root | high |
> | blank nav entry | site sidebar | remove | medium |
> 
> ---
> 
> # The Actual Workflow
> 
> Do it like this:
> 
> ## Step 1 — Dump the current docs tree
> 
> Get a list of current Markdown files from the repo.
> 
> Something like:
> 
> ```text
> path
> title
> folder
> current_url
> ```
> 
> That becomes your raw import.
> 
> ## Step 2 — Paste into Sheets
> 
> Then add:
> 
> ```text
> parent_id
> order
> status
> visibility
> module
> notes
> ```
> 
> Now you can sort, filter, and see the whole damn mess clearly.
> 
> ## Step 3 — Mark each item
> 
> Every page gets one of these:
> 
> ```text
> active
> draft
> needs_review
> deprecated
> archive
> ```
> 
> No vague limbo. Limbo is where systems go to die.
> 
> ## Step 4 — Decide the canonical nav
> 
> For each page, answer:
> 
> ```text
> Where does this live?
> Should it appear in the sidebar?
> Is it public?
> Is it private?
> Is it old but preserved?
> ```
> 
> ## Step 5 — Export as CSV
> 
> Save it into the repo as something like:
> 
> ```text
> QiSpark/navigation/qispark_nav_registry.csv
> ```
> 
> or:
> 
> ```text
> docs/nav/qispark_nav_registry.csv
> ```
> 
> ## Step 6 — Generate site navigation from it
> 
> Later, Codex/Aider/script can convert that CSV into:
> 
> ```text
> docs.json
> sidebar config
> index pages
> redirect map
> ```
> 
> That keeps the nav consistent.
> 
> ---
> 
> # Better Than Sheets Long-Term
> 
> The strongest long-term method is:
> 
> ```text
> Markdown files with frontmatter
> +
> generated nav
> ```
> 
> Example page frontmatter:
> 
> ```yaml
> ---
> nav_id: doctrine.operating_rules
> title: Operating Rules
> nav_label: Operating Rules
> parent_id: doctrine
> order: 20
> status: active
> visibility: public
> module: QiSpark
> ---
> ```
> 
> Then the nav can be generated directly from the Markdown files.
> 
> That is cleaner because the page carries its own metadata.
> 
> But right now, because QiSpark naming and navigation still need reconciliation, **Sheets is better as the staging layer**.
> 
> ---
> 
> # My Recommendation
> 
> Use this sequence:
> 
> ```text
> 1. Sheets now
> 2. Clean nav decisions there
> 3. Export to CSV
> 4. Store CSV in repo
> 5. Generate docs.json/site nav from CSV
> 6. Later migrate metadata into Markdown frontmatter
> ```
> 
> That gives you control now without locking yourself into a brittle mess.
> 
> ---
> 
> # Simple Working Structure
> 
> I’d organize the QiSpark nav like this:
> 
> ```text
> Start Here
> Doctrine
> Architecture
> Standards
> ADRs
> Prompts
> Planning
> Operations
> Reference
> Archive
> ```
> 
> Where:
> 
> ```text
> Start Here = orientation
> Doctrine = principles / rules
> Architecture = system maps
> Standards = naming, files, schemas, nav rules
> ADRs = decisions
> Prompts = reusable AI/operator prompts
> Planning = roadmap, backlog, open loops
> Operations = how to use / maintain QiSpark
> Reference = glossaries, indexes, lookup pages
> Archive = preserved old stuff, not primary nav
> ```
> 
> ---
> 
> # The Key Principle
> 
> The Sheet should answer:
> 
> ```text
> What exists?
> What is canonical?
> Where does it belong?
> Should it show in navigation?
> What needs cleanup?
> ```
> 
> The site should only display the final answer.
> 
> The repo should preserve the truth.
> 
> The Sheet is the war room. Not the kingdom.

### User
> what about using markmind map instead,

### Assistant
> Yes, MarkMind can work — but I’d use it as the **thinking/map layer**, not the canonical navigation source. Let me sanity-check the current MarkMind shape/features so I don’t give you stale plugin advice.

### Assistant
> Yes — **MarkMind is actually better for the first pass**.
> 
> But I would **not** use it as the final navigation database unless the nav is very simple. Use it as the **visual architecture layer**.
> 
> The clean setup:
> 
> ```text
> MarkMind = think / group / reorder / see the system
> Sheets = audit / metadata / status / cleanup
> Markdown frontmatter or CSV = final machine-readable source
> docs.json/sidebar = generated output
> ```
> 
> # My verdict
> 
> Use **MarkMind first**, then Sheets/CSV after.
> 
> Why? Because QiSpark navigation is not just a list. It’s a mental model. A mind map helps you see:
> 
> ```text
> What belongs together
> What is duplicated
> What is missing
> What is too buried
> What should be archive
> What should be public vs internal
> ```
> 
> Sheets is good for control.  
> MarkMind is better for **designing the shape**.
> 
> ---
> 
> # Best QiSpark workflow with MarkMind
> 
> ## 1. Create one map file
> 
> Name it:
> 
> ```text
> 2026-06-20_QiSpark_Navigation_Map.md
> ```
> 
> Use MarkMind basic mode, not rich mode, at first.
> 
> MarkMind can create mind maps from Markdown files using YAML like `mindmap-plugin: basic`, and its basic mode outputs a structured Markdown format. citeturn134424search7
> 
> ```yaml
> ---
> mindmap-plugin: basic
> ---
> ```
> 
> Then structure it like this:
> 
> ```markdown
> # QiSpark Navigation
> 
> ## Start Here
> - Welcome
> - How to Use QiSpark
> - Current System Map
> - What Is Canonical?
> 
> ## Doctrine
> - Operating Rules
> - Naming Principles
> - Public vs Private Boundary
> - Decision Standards
> 
> ## Architecture
> - QiLabs Root Map
> - QiSpark Role
> - QiNexus / QiDrive Boundary
> - QiServer Boundary
> - QiApps Boundary
> 
> ## Standards
> - File Naming
> - Folder Naming
> - Markdown Format
> - Navigation Rules
> - Evidence Storage Rules
> 
> ## ADRs
> - Why QiSpark Exists
> - Why QiSpark Is Not Blob Storage
> - Why Navigation Is Generated
> - Why Private Records Stay Elsewhere
> 
> ## Prompts
> - System Prompts
> - Codex Prompts
> - Maintenance Prompts
> - Review Prompts
> 
> ## Operations
> - How to Add a Page
> - How to Deprecate a Page
> - How to Publish
> - How to Audit Navigation
> 
> ## Archive
> - Old Names
> - Deprecated Pages
> - Duplicate Concepts
> ```
> 
> That gives you the whole nav shape visually.
> 
> ---
> 
> # Why basic mode, not rich mode?
> 
> Because **basic mode stays closer to clean Markdown**.
> 
> MarkMind’s rich mode can support extra features like summaries, boundaries, related links, and free nodes, but its rich format includes Markdown plus JSON data. citeturn134424search1
> 
> That JSON can become annoying if you later want to parse the file into:
> 
> ```text
> CSV
> docs.json
> sidebar config
> site routes
> ```
> 
> So use:
> 
> ```text
> basic mode = canonical planning map
> rich mode = presentation / brainstorming / visual linking
> ```
> 
> Don’t let the pretty tool trap you. Pretty chaos is still chaos.
> 
> ---
> 
> # Where Sheets still wins
> 
> MarkMind is weak for structured metadata.
> 
> For example, this stuff belongs in Sheets or frontmatter:
> 
> | Field | Why MarkMind is awkward |
> |---|---|
> | `status` | active/draft/deprecated gets messy visually |
> | `visibility` | public/private/internal needs filtering |
> | `source_path` | long paths clutter the map |
> | `public_path` | URLs clutter the map |
> | `redirect_from` | old paths need structured rows |
> | `owner/module` | better as fields |
> | `audit_notes` | better as a table |
> 
> So don’t replace Sheets entirely unless you want to manually babysit the nav forever. Gross. No.
> 
> ---
> 
> # Best hybrid structure
> 
> Use **three layers**:
> 
> ```text
> 1. MarkMind map
>    → visual architecture
> 
> 2. Navigation registry CSV / Sheet
>    → structured metadata
> 
> 3. Markdown frontmatter
>    → final durable source
> ```
> 
> Eventually, the best end state is:
> 
> ```text
> Markdown file frontmatter generates navigation
> ```
> 
> Example:
> 
> ```yaml
> ---
> nav_id: doctrine.operating_rules
> title: Operating Rules
> nav_label: Operating Rules
> parent_id: doctrine
> order: 20
> status: active
> visibility: public
> module: QiSpark
> ---
> ```
> 
> But right now, because QiSpark naming still needs cleanup, MarkMind is a smarter staging tool.
> 
> ---
> 
> # The exact way I’d use it
> 
> ## Phase 1 — Map the ideal nav
> 
> Use MarkMind to create the **desired structure**, not the current messy structure.
> 
> Call the root:
> 
> ```text
> QiSpark Canonical Navigation
> ```
> 
> Not:
> 
> ```text
> Current Docs Mess
> ```
> 
> You’re designing the target state.
> 
> ---
> 
> ## Phase 2 — Add status markers manually
> 
> In the map, use simple labels:
> 
> ```text
> [ACTIVE]
> [DRAFT]
> [REVIEW]
> [ARCHIVE]
> [PRIVATE]
> ```
> 
> Example:
> 
> ```markdown
> ## Doctrine
> - [ACTIVE] Operating Rules
> - [REVIEW] Public vs Private Boundary
> - [DRAFT] Decision Standards
> ```
> 
> Keep it ugly-simple. No icons. No visual over-decoration. Your future self needs parseable clarity, not Pinterest.
> 
> ---
> 
> ## Phase 3 — Export/copy to Markdown
> 
> MarkMind supports copying rich-mode content as Markdown and exporting maps to HTML/PDF/image depending on mode/command. citeturn134424search1
> 
> For your use case, the important part is: **keep the map recoverable as Markdown**.
> 
> ---
> 
> ## Phase 4 — Convert to registry
> 
> Once the map feels right, turn it into a table:
> 
> | nav_id | title | parent | order | status | visibility |
> |---|---|---|---:|---|---|
> | start.welcome | Welcome | start | 10 | active | public |
> | doctrine.operating_rules | Operating Rules | doctrine | 10 | active | public |
> | architecture.qispark_role | QiSpark Role | architecture | 20 | review | public |
> 
> That registry becomes the control layer.
> 
> ---
> 
> # Better than MarkMind alone
> 
> If you want the strongest Obsidian-native system, do this:
> 
> ```text
> MarkMind map
> ↓
> Markdown outline
> ↓
> Dataview table / CSV
> ↓
> Generated docs nav
> ```
> 
> That gives you visual thinking **and** structured control.
> 
> ---
> 
> # My recommended QiSpark setup
> 
> Create these files:
> 
> ```text
> 10_QiSpark/
>   navigation/
>     2026-06-20_QiSpark_Navigation_Map.md
>     qispark_nav_registry.csv
>     qispark_redirects.csv
>     qispark_nav_audit.md
> ```
> 
> Use the map for structure.
> 
> Use the registry for truth.
> 
> Use the audit file for cleanup decisions.
> 
> ---
> 
> # Simple decision
> 
> Use **MarkMind instead of Sheets** when you are asking:
> 
> ```text
> Where should this belong?
> What is the shape of the system?
> What sections make sense?
> What am I missing?
> ```
> 
> Use **Sheets instead of MarkMind** when you are asking:
> 
> ```text
> What is active?
> What is public?
> What is the exact URL?
> What redirects exist?
> What order does the site generator need?
> What still needs cleanup?
> ```
> 
> So the real answer:
> 
> ```text
> MarkMind for architecture.
> Sheets/CSV for governance.
> Markdown/frontmatter for final source.
> Generated nav for the website.
> ```
> 
> That’s the cleanest path.

### User
> ok so really this goes off of #'' so first node is # node name, then under it ## name is a sub node and so forth, want to to update this one sections for me quicky but after you do the root first. ---
> title: Navigation Map
> section: 01_Q/99_system
> access_level: L1
> visibility: private
> ai_ingest: true
> status: active
> last_updated: 2026-05-24
> mindmap-plugin: basic
> 
> ---
> 
> # Navigation Map
> 
> ## 00_surface
> ### Public Cody / LinkedIn layer
> 
> ## 10_functional
>   	How to work with me
> 
> ## 20_personal
>   	Personal context and identity notes
> 
> ## 30_clinical
>   	Health, 
> 	ADHD, 
> 	anxiety, 
> 	stress-body response
> 
> ## 40_history
>   	Timeline, 
> 	life arcs, 
> 	major resets
> 
> ## 50_patterns
>   	Personality, 
> 	intuition, 
> 	blindspots, 
> 	recurring patterns
> 
> ## 60_relationships
>   	People, 
> 	roles, 
> 	trust, 
> 	boundaries
> 
> ## 70_trauma_recovery
>   	Structured trauma and recovery work
> 
> ## 80_legacy_meaning
>   	Meaning, 
>   	story, 
>   	spirituality, 
>   	legacy, 
>   	713
> 
> ## 90_locked
>   	### My eyes only
> 
> ## 99_system
> 	### Rules, 
> 	### templates, 
> 	### access control, 
> 	### AI instructions
> ```

### Assistant
> Yep. For MarkMind basic, **every node should be a heading**. Your current indented lines would act messy/loose, not clean child nodes.
> 
> I’d make the root:
> 
> ```markdown id="pat00r"
> # 01_Q Navigation Map
> ```
> 
> Then everything else nests under it.
> 
> Here’s the cleaned version:
> 
> :::writing{variant="standard" id="48291"}
> ---
> title: Navigation Map
> section: 01_Q/99_system
> access_level: L1
> visibility: private
> ai_ingest: true
> status: active
> last_updated: 2026-05-24
> mindmap-plugin: basic
> ---
> 
> # 01_Q Navigation Map
> 
> ## 00_surface
> ### Public Cody / LinkedIn Layer
> 
> ## 10_functional
> ### How to Work With Me
> ### Operating Preferences
> ### Communication Style
> ### Workflows and Collaboration Rules
> 
> ## 20_personal
> ### Personal Context
> ### Identity Notes
> ### Values
> ### Life Parameters
> 
> ## 30_clinical
> ### Health
> ### ADHD
> ### Anxiety
> ### Stress-Body Response
> ### Regulation Notes
> 
> ## 40_history
> ### Timeline
> ### Life Arcs
> ### Major Resets
> ### Key Transitions
> 
> ## 50_patterns
> ### Personality
> ### Intuition
> ### Blindspots
> ### Recurring Patterns
> ### Strengths and Risks
> 
> ## 60_relationships
> ### People
> ### Roles
> ### Trust
> ### Boundaries
> ### Relational Rules
> 
> ## 70_trauma_recovery
> ### Structured Trauma Work
> ### Recovery Work
> ### Safety Protocols
> ### Integration Notes
> 
> ## 80_legacy_meaning
> ### Meaning
> ### Story
> ### Spirituality
> ### Legacy
> ### 713
> 
> ## 90_locked
> ### My Eyes Only
> ### Restricted Notes
> ### Private Memory
> ### Sensitive Context
> 
> ## 99_system
> ### Rules
> ### Templates
> ### Access Control
> ### AI Instructions
> ### Navigation Standards
> ### Maintenance Notes
> :::
> 
> The important correction: **no tab-indented child text**. In this format:
> 
> ```markdown id="5ca2e8"
> # root
> ## main section
> ### child node
> #### deeper child node
> ```
> 
> That’s the hierarchy. Keep it brutally simple. MarkMind will behave better.

### User
> ok we can also indent them i think still, so if you were to try and give me the entire qilabs.qispark folder and file tree in markmin format in one shot then we can work on each piece.

### Assistant
> I’m going to give you a **target canonical MarkMind map**, not a claim that this exact tree already exists on disk. Treat this as the scaffold we can prune/rename section by section.

### Assistant
> Yes. Use this as the **first-pass master map**.
> 
> I’m making one strong assumption: **QiSpark is the docs/navigation/governance layer for QiLabs**, not the evidence vault or app runtime. So this is the **target tree**, not the current messy disk snapshot.
> 
> :::writing{variant="standard" id="91847"}
> ---
> title: QiSpark Folder and File Tree
> section: 10_QiSpark/99_system/navigation
> access_level: L1
> visibility: private
> ai_ingest: true
> status: draft
> last_updated: 2026-06-20
> mindmap-plugin: basic
> ---
> 
> # 10_QiSpark
> 
> ## 00_root_files
> ### README.md
> ### index.md
> ### codex.md
> ### docs.json
> ### package.json
> ### .gitignore
> ### .env.example
> ### CHANGELOG.md
> ### LICENSE.md
> 
> ## 01_navigation
> ### index.md
> ### 2026-06-20_QiSpark_Navigation_Map.md
> ### 2026-06-20_QiSpark_Folder_File_Tree.md
> ### qispark_nav_registry.csv
> ### qispark_redirects.csv
> ### qispark_nav_audit.md
> ### qispark_sidebar_rules.md
> ### qispark_public_private_map.md
> ### qispark_route_index.md
> ### qispark_deprecated_routes.md
> 
> ## 02_templates
> ### index.md
> ### page_template.md
> ### section_index_template.md
> ### adr_template.md
> ### codex_template.md
> ### prompt_template.md
> ### project_template.md
> ### audit_template.md
> ### glossary_template.md
> ### changelog_template.md
> ### system_rule_template.md
> ### access_control_template.md
> 
> ## 03_assets
> ### index.md
> ### logos
> #### qilabs_logo.svg
> #### qispark_logo.svg
> #### favicon.svg
> ### diagrams
> #### qilabs_system_map.svg
> #### qispark_role_map.svg
> #### qinexus_boundary_map.svg
> #### qiserver_boundary_map.svg
> ### screenshots
> #### README.md
> ### exports
> #### README.md
> 
> ## 04_public_site
> ### index.md
> ### public_home.md
> ### public_about_qilabs.md
> ### public_about_cody.md
> ### public_linkedin_layer.md
> ### public_services.md
> ### public_case_studies.md
> ### public_contact.md
> ### public_disclaimer.md
> 
> ## 05_private_site
> ### index.md
> ### private_home.md
> ### private_operating_context.md
> ### private_navigation_rules.md
> ### private_ai_instructions.md
> ### private_access_boundaries.md
> ### private_sensitive_context_index.md
> 
> ## 10_start_here
> ### index.md
> ### 00_welcome.md
> ### 10_what_qispark_is.md
> ### 20_how_to_use_qispark.md
> ### 30_current_status.md
> ### 40_what_is_canonical.md
> ### 50_open_loops.md
> ### 60_next_actions.md
> ### 90_archive.md
> 
> ## 20_doctrine
> ### index.md
> ### 00_doctrine_overview.md
> ### 10_operating_principles.md
> ### 20_truth_and_alignment_rules.md
> ### 30_leverage_and_systems_rules.md
> ### 40_naming_principles.md
> ### 50_modularity_principles.md
> ### 60_public_private_boundary.md
> ### 70_ai_collaboration_doctrine.md
> ### 80_human_override_rules.md
> ### 90_deprecated_doctrine.md
> 
> ## 30_architecture
> ### index.md
> ### 00_architecture_overview.md
> ### 10_qilabs_root_map.md
> ### 20_qispark_role.md
> ### 30_qidna_role.md
> ### 40_qiaccess_role.md
> ### 50_qisystem_role.md
> ### 60_qiserver_role.md
> ### 70_qicapture_role.md
> ### 80_qinexus_role.md
> ### 90_qiapp_qilife_role.md
> ### 100_qiconnect_role.md
> ### 110_boundaries_between_roots.md
> ### 120_data_flow_map.md
> ### 130_ai_ingestion_map.md
> ### 140_publication_map.md
> 
> ## 40_standards
> ### index.md
> ### 00_standards_overview.md
> ### 10_file_naming_standard.md
> ### 20_folder_naming_standard.md
> ### 30_markdown_standard.md
> ### 40_frontmatter_standard.md
> ### 50_navigation_standard.md
> ### 60_access_level_standard.md
> ### 70_visibility_standard.md
> ### 80_ai_ingest_standard.md
> ### 90_status_standard.md
> ### 100_tagging_standard.md
> ### 110_crosslinking_standard.md
> ### 120_archive_standard.md
> ### 130_evidence_storage_standard.md
> ### 140_export_standard.md
> 
> ## 50_adrs
> ### index.md
> ### 000_adr_index.md
> ### 001_why_qispark_exists.md
> ### 002_why_qispark_is_not_blob_storage.md
> ### 003_why_private_records_stay_outside_qispark.md
> ### 004_why_navigation_is_generated.md
> ### 005_why_markmind_is_used_for_mapping.md
> ### 006_why_sheets_csv_is_used_for_registry.md
> ### 007_why_markdown_frontmatter_becomes_source_of_truth.md
> ### 008_why_qinexus_holds_evidence.md
> ### 009_why_qiserver_holds_runtime.md
> ### 010_why_qilife_is_separate_from_qispark.md
> ### 099_deprecated_decisions.md
> 
> ## 60_prompts
> ### index.md
> ### 00_prompt_overview.md
> ### 10_system_prompts
> #### index.md
> #### qispark_system_prompt.md
> #### qilabs_system_prompt.md
> #### qidna_system_prompt.md
> #### qinexus_system_prompt.md
> #### qiserver_system_prompt.md
> ### 20_codex_prompts
> #### index.md
> #### repo_review_prompt.md
> #### nav_cleanup_prompt.md
> #### docs_generation_prompt.md
> #### folder_reconciliation_prompt.md
> #### frontmatter_audit_prompt.md
> ### 30_maintenance_prompts
> #### index.md
> #### weekly_review_prompt.md
> #### broken_links_prompt.md
> #### stale_docs_prompt.md
> #### rename_reconciliation_prompt.md
> #### archive_review_prompt.md
> ### 40_extraction_prompts
> #### index.md
> #### extract_doctrine_prompt.md
> #### extract_adr_prompt.md
> #### extract_tasks_prompt.md
> #### extract_file_tree_prompt.md
> #### extract_navigation_prompt.md
> ### 50_review_prompts
> #### index.md
> #### clarity_review_prompt.md
> #### contradiction_review_prompt.md
> #### privacy_review_prompt.md
> #### canonicality_review_prompt.md
> #### publishing_review_prompt.md
> 
> ## 70_operations
> ### index.md
> ### 00_operations_overview.md
> ### 10_how_to_add_a_page.md
> ### 20_how_to_add_a_section.md
> ### 30_how_to_update_navigation.md
> ### 40_how_to_deprecate_a_page.md
> ### 50_how_to_archive_content.md
> ### 60_how_to_publish_docs.md
> ### 70_how_to_run_a_nav_audit.md
> ### 80_how_to_review_public_private_boundaries.md
> ### 90_how_to_reconcile_names.md
> ### 100_how_to_prepare_ai_ingestion.md
> ### 110_how_to_restore_from_archive.md
> 
> ## 80_reference
> ### index.md
> ### 00_reference_overview.md
> ### glossary.md
> ### canonical_names.md
> ### root_folder_index.md
> ### route_index.md
> ### status_values.md
> ### access_levels.md
> ### visibility_values.md
> ### ai_ingest_values.md
> ### tag_index.md
> ### module_index.md
> ### acronym_index.md
> ### command_index.md
> ### link_index.md
> 
> ## 90_qilabs_roots
> 
> ### 01_QiDNA
> #### index.md
> #### codex.md
> #### 00_overview.md
> #### 10_identity_and_doctrine.md
> #### 20_operating_rules.md
> #### 30_memory_rules.md
> #### 40_personal_context_boundaries.md
> #### 50_ai_alignment_rules.md
> #### 60_qidna_navigation.md
> #### 99_system.md
> 
> ### 10_QiAccess
> #### index.md
> #### codex.md
> #### 00_overview.md
> #### 10_accounts.md
> #### 20_credentials_boundary.md
> #### 30_permissions.md
> #### 40_devices.md
> #### 50_recovery_paths.md
> #### 60_access_audit.md
> #### 99_system.md
> 
> ### 20_QiSystem
> #### index.md
> #### codex.md
> #### 00_overview.md
> #### 10_local_machine.md
> #### 20_repos.md
> #### 30_database.md
> #### 40_supabase.md
> #### 50_sqlite.md
> #### 60_sync_rules.md
> #### 70_system_jobs.md
> #### 99_system.md
> 
> ### 30_QiServer
> #### index.md
> #### codex.md
> #### 00_overview.md
> #### 10_server_role.md
> #### 20_runtime_services.md
> #### 30_ollama.md
> #### 40_aider.md
> #### 50_fastapi.md
> #### 60_lancedb.md
> #### 70_tmux.md
> #### 80_deployment.md
> #### 99_system.md
> 
> ### 40_QiCapture
> #### index.md
> #### codex.md
> #### 00_overview.md
> #### 10_inbox.md
> #### 20_voice_notes.md
> #### 30_screenshots.md
> #### 40_scans.md
> #### 50_web_clips.md
> #### 60_triage_rules.md
> #### 70_processing_pipeline.md
> #### 99_system.md
> 
> ### 50_QiNexus
> #### index.md
> #### codex.md
> #### 00_overview.md
> #### 10_drive_backed_storage.md
> #### 20_evidence_storage.md
> #### 30_records_boundary.md
> #### 40_mirror_folders.md
> #### 50_my_drive_mount.md
> #### 60_blob_rules.md
> #### 70_retrieval_rules.md
> #### 99_system.md
> 
> ### 60_QiApp_QiLife
> #### index.md
> #### codex.md
> #### 00_overview.md
> #### 10_life_dashboard.md
> #### 20_routines.md
> #### 30_tasks.md
> #### 40_finance.md
> #### 50_health.md
> #### 60_legal.md
> #### 70_relationships.md
> #### 80_gigi.md
> #### 90_mobile_mode.md
> #### 99_system.md
> 
> ### 70_QiConnect
> #### index.md
> #### codex.md
> #### 00_overview.md
> #### 10_contacts.md
> #### 20_clients.md
> #### 30_vendors.md
> #### 40_messages.md
> #### 50_email.md
> #### 60_calendar.md
> #### 70_crm.md
> #### 80_outreach.md
> #### 99_system.md
> 
> ## 91_qispark_internal_maps
> ### index.md
> ### 00_qispark_master_map.md
> ### 10_public_private_map.md
> ### 20_content_type_map.md
> ### 30_access_level_map.md
> ### 40_ai_ingest_map.md
> ### 50_route_map.md
> ### 60_dependency_map.md
> ### 70_cleanup_map.md
> ### 80_archive_map.md
> ### 90_future_map.md
> 
> ## 92_qispark_content_types
> ### index.md
> ### doctrine_pages.md
> ### architecture_pages.md
> ### adr_pages.md
> ### prompt_pages.md
> ### operational_pages.md
> ### reference_pages.md
> ### public_pages.md
> ### private_pages.md
> ### archive_pages.md
> 
> ## 93_qispark_registries
> ### index.md
> ### page_registry.csv
> ### section_registry.csv
> ### module_registry.csv
> ### route_registry.csv
> ### redirect_registry.csv
> ### status_registry.csv
> ### access_registry.csv
> ### ai_ingest_registry.csv
> ### owner_registry.csv
> ### cleanup_registry.csv
> 
> ## 94_qispark_audits
> ### index.md
> ### 2026-06-20_navigation_audit.md
> ### 2026-06-20_naming_audit.md
> ### 2026-06-20_public_private_audit.md
> ### 2026-06-20_ai_ingest_audit.md
> ### broken_links_audit.md
> ### duplicate_pages_audit.md
> ### stale_pages_audit.md
> ### orphan_pages_audit.md
> ### archive_candidates.md
> 
> ## 95_qispark_exports
> ### index.md
> ### html_exports
> #### README.md
> ### pdf_exports
> #### README.md
> ### csv_exports
> #### README.md
> ### json_exports
> #### README.md
> ### markdown_exports
> #### README.md
> 
> ## 96_qispark_scripts
> ### index.md
> ### generate_nav_from_csv.py
> ### generate_registry_from_markdown.py
> ### audit_frontmatter.py
> ### audit_broken_links.py
> ### audit_duplicate_titles.py
> ### generate_route_index.py
> ### generate_redirects.py
> ### export_markmind_outline.py
> ### README.md
> 
> ## 97_qispark_backlog
> ### index.md
> ### 00_backlog_overview.md
> ### 10_open_loops.md
> ### 20_cleanup_tasks.md
> ### 30_renaming_tasks.md
> ### 40_missing_pages.md
> ### 50_docs_to_write.md
> ### 60_prompts_to_create.md
> ### 70_scripts_to_build.md
> ### 80_publish_tasks.md
> ### 90_someday_maybe.md
> 
> ## 98_archive
> ### index.md
> ### old_navigation_maps
> #### README.md
> ### old_names
> #### README.md
> ### deprecated_pages
> #### README.md
> ### removed_routes
> #### README.md
> ### old_exports
> #### README.md
> ### legacy_qios_docs
> #### README.md
> 
> ## 99_system
> ### index.md
> ### 00_system_overview.md
> ### 10_qispark_system_rules.md
> ### 20_access_control.md
> ### 30_visibility_matrix.md
> ### 40_ai_ingest_rules.md
> ### 50_frontmatter_schema.md
> ### 60_navigation_schema.md
> ### 70_registry_schema.md
> ### 80_publish_pipeline.md
> ### 90_maintenance_schedule.md
> ### 100_error_handling.md
> ### 110_recovery_plan.md
> ### 120_changelog_policy.md
> ### 130_system_notes.md
> ### 999_do_not_delete.md
> :::
> 
> **Next move:** I’d work this from the top down in chunks:
> 
> ```text
> 1. Root files
> 2. Navigation
> 3. Templates
> 4. Core docs sections
> 5. QiLabs roots
> 6. Registries/audits/scripts
> 7. Archive/system
> ```
> 
> The only thing I’d challenge right now: **don’t let `90_qilabs_roots` become a second copy of every other root.** It should document the roots, not duplicate their actual contents. Otherwise QiSpark turns into QiNexus cosplay, and we are not doing that.

### User
> ok, so i first want to say, this is where we lock in something important i do not want generically named files anymore like index.md etc. i want to see index.namecontextetch.md

### Assistant
> Locked in.
> 
> From here forward for **QiSpark/QiLabs docs**, we should treat generic names as deprecated unless the framework absolutely requires them.
> 
> ## New naming rule
> 
> Instead of:
> 
> ```text
> index.md
> README.md
> overview.md
> template.md
> rules.md
> ```
> 
> Use:
> 
> ```text
> index.qispark_navigation.md
> readme.qispark_root.md
> overview.qilabs_roots.md
> template.adr_record.md
> rules.ai_ingest.md
> ```
> 
> ## Pattern
> 
> ```text
> {function}.{context}.md
> ```
> 
> Examples:
> 
> ```text
> index.qispark_start_here.md
> index.qispark_navigation.md
> map.qilabs_root_architecture.md
> registry.qispark_routes.csv
> audit.qispark_public_private.md
> template.qispark_page.md
> schema.qispark_frontmatter.md
> rules.qispark_access_control.md
> ```
> 
> ## Updated principle
> 
> The filename should answer:
> 
> ```text
> What is this?
> What context does it belong to?
> Why does it exist?
> ```
> 
> So yeah — **no more naked `index.md` unless the build system forces it**.
> 
> And even then, we can use either:
> 
> ```text
> index.md
> ```
> 
> only as a technical shim, with the real content in:
> 
> ```text
> index.qispark_navigation.md
> ```
> 
> or use frontmatter to point to the canonical named file.

### User
> ok, now let me see your updated tree and i think you should probably merge some of the .md files it looks overly bloated when our rules although strick are not complicated.

### Assistant
> Correct. The first tree was **too bloated**. It was useful for thinking, but not clean enough for actual QiSpark.
> 
> Here’s the tighter version:
> 
> ```text id="zcwcqg"
> Fewer files.
> Richer names.
> Merged rules.
> No generic index.md.
> No tiny-doc confetti.
> ```
> 
> :::writing{variant="standard" id="63928"}
> ---
> title: QiSpark Folder and File Tree
> section: 10_QiSpark/99_system/navigation
> access_level: L1
> visibility: private
> ai_ingest: true
> status: draft
> last_updated: 2026-06-20
> mindmap-plugin: basic
> ---
> 
> # 10_QiSpark
> 
> ## 00_root
> ### readme.qispark_root.md
> ### codex.qispark_ai_operating_context.md
> ### changelog.qispark_updates.md
> ### config.qispark_docs_site.json
> ### manifest.qispark_package.json
> ### env.qispark_example.env
> ### gitignore.qispark_repo.gitignore
> 
> ## 01_navigation
> ### map.qispark_navigation_markmind.md
> ### map.qispark_folder_file_tree.md
> ### registry.qispark_navigation.csv
> ### registry.qispark_redirects.csv
> ### audit.qispark_navigation_cleanup.md
> ### rules.qispark_navigation_routes_visibility.md
> 
> ## 02_templates
> ### templates.qispark_content_system.md
> #### Page Template
> #### Section Template
> #### ADR Template
> #### Prompt Template
> #### Audit Template
> #### Glossary Template
> #### Changelog Template
> #### Access Control Template
> 
> ## 03_assets
> ### assets.qispark_visual_index.md
> ### logos
> #### logo.qilabs.svg
> #### logo.qispark.svg
> #### favicon.qispark.svg
> ### diagrams
> #### diagram.qilabs_system_map.svg
> #### diagram.qispark_role_boundary.svg
> #### diagram.qilabs_data_flow.svg
> ### screenshots
> #### readme.qispark_screenshots.md
> ### exports
> #### readme.qispark_asset_exports.md
> 
> ## 04_public_layer
> ### public.qispark_site_pages.md
> #### Public Home
> #### About QiLabs
> #### About Cody
> #### LinkedIn Layer
> #### Services
> #### Case Studies
> #### Contact
> #### Public Disclaimer
> 
> ## 05_private_layer
> ### private.qispark_operating_context.md
> #### Private Home
> #### Operating Context
> #### AI Instructions
> #### Access Boundaries
> #### Sensitive Context Index
> #### Private Navigation Rules
> 
> ## 10_start_here
> ### guide.qispark_start_here.md
> #### Welcome
> #### What QiSpark Is
> #### How to Use QiSpark
> #### Current Status
> #### What Is Canonical
> #### Open Loops
> #### Next Actions
> 
> ## 20_doctrine
> ### doctrine.qispark_operating_principles.md
> #### Doctrine Overview
> #### Truth and Alignment Rules
> #### Leverage and Systems Rules
> #### Naming Principles
> #### Modularity Principles
> #### Public Private Boundary
> #### AI Collaboration Doctrine
> #### Human Override Rules
> 
> ## 30_architecture
> ### architecture.qilabs_system_map.md
> #### Architecture Overview
> #### QiLabs Root Map
> #### QiSpark Role
> #### Root Folder Boundaries
> #### Data Flow Map
> #### AI Ingestion Map
> #### Publication Map
> 
> ### architecture.qilabs_root_roles.md
> #### 01_QiDNA
> #### 10_QiAccess
> #### 20_QiSystem
> #### 30_QiServer
> #### 40_QiCapture
> #### 50_QiNexus
> #### 60_QiApp_QiLife
> #### 70_QiConnect
> 
> ## 40_standards
> ### standards.qispark_docs_and_files.md
> #### File Naming Standard
> #### Folder Naming Standard
> #### Markdown Standard
> #### Frontmatter Standard
> #### Crosslinking Standard
> #### Archive Standard
> #### Export Standard
> 
> ### standards.qispark_access_visibility_ai.md
> #### Access Levels
> #### Visibility Values
> #### AI Ingest Rules
> #### Status Values
> #### Public Private Rules
> #### Sensitive Context Rules
> 
> ## 50_decisions
> ### adr.qispark_architecture_decisions.md
> #### Why QiSpark Exists
> #### Why QiSpark Is Not Blob Storage
> #### Why Private Records Stay Outside QiSpark
> #### Why Navigation Is Generated
> #### Why MarkMind Is Used For Mapping
> #### Why Sheets CSV Is Used For Registry
> #### Why Markdown Frontmatter Becomes Source Of Truth
> #### Why QiNexus Holds Evidence
> #### Why QiServer Holds Runtime
> #### Deprecated Decisions
> 
> ## 60_prompts
> ### prompts.qispark_ai_system.md
> #### QiSpark System Prompt
> #### QiLabs System Prompt
> #### QiDNA System Prompt
> #### QiNexus System Prompt
> #### QiServer System Prompt
> 
> ### prompts.qispark_codex_and_maintenance.md
> #### Repo Review Prompt
> #### Navigation Cleanup Prompt
> #### Docs Generation Prompt
> #### Folder Reconciliation Prompt
> #### Frontmatter Audit Prompt
> #### Weekly Review Prompt
> #### Broken Links Prompt
> #### Stale Docs Prompt
> #### Archive Review Prompt
> 
> ### prompts.qispark_extraction_and_review.md
> #### Extract Doctrine Prompt
> #### Extract ADR Prompt
> #### Extract Tasks Prompt
> #### Extract File Tree Prompt
> #### Extract Navigation Prompt
> #### Clarity Review Prompt
> #### Contradiction Review Prompt
> #### Privacy Review Prompt
> #### Publishing Review Prompt
> 
> ## 70_operations
> ### operations.qispark_maintenance_playbook.md
> #### How To Add A Page
> #### How To Add A Section
> #### How To Update Navigation
> #### How To Deprecate A Page
> #### How To Archive Content
> #### How To Publish Docs
> #### How To Run A Navigation Audit
> #### How To Review Public Private Boundaries
> #### How To Reconcile Names
> #### How To Prepare AI Ingestion
> #### How To Restore From Archive
> 
> ## 80_reference
> ### reference.qispark_lookup_tables.md
> #### Glossary
> #### Canonical Names
> #### Root Folder Index
> #### Route Index
> #### Status Values
> #### Access Levels
> #### Visibility Values
> #### AI Ingest Values
> #### Tag Index
> #### Module Index
> #### Acronym Index
> #### Command Index
> #### Link Index
> 
> ## 90_registries
> ### registry.qispark_pages.csv
> ### registry.qispark_sections.csv
> ### registry.qispark_routes.csv
> ### registry.qispark_redirects.csv
> ### registry.qispark_status_access_visibility.csv
> ### registry.qispark_cleanup.csv
> 
> ## 91_audits
> ### audit.qispark_navigation_and_routes.md
> #### Navigation Audit
> #### Broken Links Audit
> #### Duplicate Pages Audit
> #### Stale Pages Audit
> #### Orphan Pages Audit
> 
> ### audit.qispark_naming_and_boundaries.md
> #### Naming Audit
> #### Public Private Audit
> #### AI Ingest Audit
> #### Root Boundary Audit
> #### Archive Candidate Review
> 
> ## 92_scripts
> ### scripts.qispark_automation_index.md
> ### generate.qispark_nav_from_csv.py
> ### generate.qispark_registry_from_markdown.py
> ### audit.qispark_frontmatter.py
> ### audit.qispark_links_duplicates.py
> ### generate.qispark_routes_redirects.py
> ### export.qispark_markmind_outline.py
> 
> ## 93_exports
> ### exports.qispark_index.md
> ### html_exports
> #### readme.qispark_html_exports.md
> ### pdf_exports
> #### readme.qispark_pdf_exports.md
> ### csv_exports
> #### readme.qispark_csv_exports.md
> ### json_exports
> #### readme.qispark_json_exports.md
> ### markdown_exports
> #### readme.qispark_markdown_exports.md
> 
> ## 97_backlog
> ### backlog.qispark_cleanup_and_build.md
> #### Open Loops
> #### Cleanup Tasks
> #### Renaming Tasks
> #### Missing Pages
> #### Docs To Write
> #### Prompts To Create
> #### Scripts To Build
> #### Publish Tasks
> #### Someday Maybe
> 
> ## 98_archive
> ### archive.qispark_legacy_index.md
> ### old_navigation_maps
> #### readme.qispark_old_navigation_maps.md
> ### old_names
> #### readme.qispark_old_names.md
> ### deprecated_pages
> #### readme.qispark_deprecated_pages.md
> ### removed_routes
> #### readme.qispark_removed_routes.md
> ### old_exports
> #### readme.qispark_old_exports.md
> ### legacy_qios_docs
> #### readme.qispark_legacy_qios_docs.md
> 
> ## 99_system
> ### system.qispark_rules_and_schemas.md
> #### System Overview
> #### QiSpark System Rules
> #### Access Control
> #### Visibility Matrix
> #### AI Ingest Rules
> #### Frontmatter Schema
> #### Navigation Schema
> #### Registry Schema
> #### Publish Pipeline
> #### Maintenance Schedule
> #### Error Handling
> #### Recovery Plan
> #### Changelog Policy
> #### Do Not Delete Notes
> :::
> 
> ## What changed
> 
> The main cleanup:
> 
> | Before | Now |
> |---|---|
> | Lots of `index.md` files | Context-rich filenames |
> | Separate tiny standards files | Merged standards documents |
> | Too many prompt files | Prompt bundles by use case |
> | Separate audit files for every issue | Two main audit docs |
> | Separate system rule docs | One system rules/schemas doc |
> | QiLabs roots duplicated too deeply | Root roles summarized in architecture |
> 
> ## My honest take
> 
> This is much better.
> 
> The previous version was **over-specified**. This version is strict enough to govern the system but not so granular that you drown in your own filing cabinet. That’s the line.

### User
> you missed something, in reality this shoudl be something more like qispark, then of course root but the build happens in the cloudflair but technically, we mirror the tru structure, so qilabs.workspace, then qispark then qiserver, then qivault, then in sispark you can start adding all the kb stuff thats no good for hungers ir resuin,

### Assistant
> Yes — that’s the missing layer.
> 
> I treated `10_QiSpark` like the root. That was wrong.
> 
> The actual model should be:
> 
> ```text
> qilabs.workspace
> ├── qispark
> ├── qiserver
> ├── qivault
> └── other roots/modules
> ```
> 
> And then:
> 
> ```text
> Cloudflare = build/deploy surface
> qilabs.workspace = source/workspace mirror
> qispark = knowledge/docs/navigation/governance layer
> qiserver = runtime/server layer
> qivault = storage/evidence/private records layer
> ```
> 
> So QiSpark should **mirror the true system structure conceptually**, but not become the place where all the real server/vault stuff lives.
> 
> Here’s the corrected MarkMind starting point:
> 
> :::writing{variant="standard" id="70438"}
> ---
> title: QiLabs Workspace Navigation Map
> section: qilabs.workspace/qispark/99_system/navigation
> access_level: L1
> visibility: private
> ai_ingest: true
> status: draft
> last_updated: 2026-06-20
> mindmap-plugin: basic
> ---
> 
> # qilabs.workspace
> 
> ## 00_root
> ### readme.qilabs_workspace.md
> ### codex.qilabs_workspace.md
> ### manifest.qilabs_workspace.json
> ### changelog.qilabs_workspace.md
> 
> ## qispark
> ### 00_root
> #### readme.qispark_root.md
> #### codex.qispark_ai_operating_context.md
> #### changelog.qispark_updates.md
> #### config.qispark_docs_site.json
> 
> ### 01_navigation
> #### map.qispark_navigation_markmind.md
> #### map.qispark_folder_file_tree.md
> #### registry.qispark_navigation.csv
> #### registry.qispark_redirects.csv
> #### audit.qispark_navigation_cleanup.md
> #### rules.qispark_navigation_routes_visibility.md
> 
> ### 10_start_here
> #### guide.qispark_start_here.md
> ##### Welcome
> ##### What QiSpark Is
> ##### How To Use QiSpark
> ##### What Is Canonical
> ##### Current System Status
> ##### Open Loops
> ##### Next Actions
> 
> ### 20_knowledge_base
> #### kb.qispark_core_context.md
> ##### QiSpark Purpose
> ##### QiLabs Purpose
> ##### Current Operating Model
> ##### Important Definitions
> ##### System Boundaries
> 
> #### kb.qispark_working_notes.md
> ##### Active Thinking
> ##### Unsorted Ideas
> ##### Draft Models
> ##### Questions To Resolve
> ##### Not Yet Canonical
> 
> #### kb.qispark_decision_context.md
> ##### Why This Structure Exists
> ##### What Changed
> ##### What Is Locked
> ##### What Is Still Fluid
> 
> ### 30_doctrine
> #### doctrine.qispark_operating_principles.md
> ##### Truth And Alignment
> ##### Leverage And Systems
> ##### Naming Principles
> ##### Modularity
> ##### AI Collaboration
> ##### Human Override Rules
> 
> ### 40_architecture
> #### architecture.qilabs_workspace_map.md
> ##### qilabs.workspace
> ##### qispark
> ##### qiserver
> ##### qivault
> ##### cloudflare_build_surface
> ##### data_flow
> ##### publishing_flow
> 
> #### architecture.qilabs_root_boundaries.md
> ##### QiSpark Boundary
> ##### QiServer Boundary
> ##### QiVault Boundary
> ##### Cloudflare Boundary
> ##### What Does Not Belong In QiSpark
> 
> ### 50_standards
> #### standards.qispark_docs_files_access.md
> ##### File Naming
> ##### Folder Naming
> ##### Markdown Format
> ##### Frontmatter
> ##### Visibility
> ##### Access Levels
> ##### AI Ingest
> ##### Status Values
> ##### Archive Rules
> 
> ### 60_decisions
> #### adr.qispark_architecture_decisions.md
> ##### Why qilabs.workspace Is The Root Mirror
> ##### Why Cloudflare Is Build Surface Only
> ##### Why QiSpark Holds Knowledge And Navigation
> ##### Why QiServer Holds Runtime
> ##### Why QiVault Holds Records And Evidence
> ##### Why Generic Filenames Are Deprecated
> ##### Why Rules Are Merged Instead Of Fragmented
> 
> ### 70_prompts
> #### prompts.qispark_ai_system.md
> ##### QiSpark System Prompt
> ##### QiLabs Workspace Prompt
> ##### Navigation Cleanup Prompt
> ##### Folder Reconciliation Prompt
> ##### Frontmatter Audit Prompt
> 
> #### prompts.qispark_review_extraction.md
> ##### Extract Navigation
> ##### Extract Decisions
> ##### Extract Tasks
> ##### Review Contradictions
> ##### Review Privacy
> ##### Review Canonicality
> 
> ### 80_operations
> #### operations.qispark_maintenance_playbook.md
> ##### Add A Page
> ##### Add A Section
> ##### Update Navigation
> ##### Deprecate A Page
> ##### Archive Content
> ##### Publish Docs
> ##### Run Navigation Audit
> ##### Reconcile Names
> 
> ### 90_reference
> #### reference.qispark_lookup_tables.md
> ##### Glossary
> ##### Canonical Names
> ##### Root Folder Index
> ##### Route Index
> ##### Access Levels
> ##### Visibility Values
> ##### AI Ingest Values
> ##### Status Values
> 
> ### 91_registries
> #### registry.qispark_pages.csv
> #### registry.qispark_sections.csv
> #### registry.qispark_routes.csv
> #### registry.qispark_redirects.csv
> #### registry.qispark_status_access_visibility.csv
> #### registry.qispark_cleanup.csv
> 
> ### 92_audits
> #### audit.qispark_navigation_routes_naming.md
> ##### Navigation Audit
> ##### Route Audit
> ##### Naming Audit
> ##### Duplicate Page Audit
> ##### Stale Page Audit
> ##### Orphan Page Audit
> 
> #### audit.qispark_boundaries_privacy_ingest.md
> ##### QiSpark Boundary Audit
> ##### Public Private Audit
> ##### AI Ingest Audit
> ##### Vault Leakage Audit
> ##### Server Leakage Audit
> 
> ### 93_scripts
> #### scripts.qispark_automation_index.md
> #### generate.qispark_nav_from_csv.py
> #### generate.qispark_registry_from_markdown.py
> #### audit.qispark_frontmatter.py
> #### audit.qispark_links_duplicates.py
> #### generate.qispark_routes_redirects.py
> #### export.qispark_markmind_outline.py
> 
> ### 94_exports
> #### exports.qispark_index.md
> ##### HTML Exports
> ##### PDF Exports
> ##### CSV Exports
> ##### JSON Exports
> ##### Markdown Exports
> 
> ### 97_backlog
> #### backlog.qispark_cleanup_and_build.md
> ##### Open Loops
> ##### Cleanup Tasks
> ##### Renaming Tasks
> ##### Missing Pages
> ##### Docs To Write
> ##### Scripts To Build
> ##### Publish Tasks
> 
> ### 98_archive
> #### archive.qispark_legacy_index.md
> ##### Old Navigation Maps
> ##### Old Names
> ##### Deprecated Pages
> ##### Removed Routes
> ##### Old Exports
> ##### Legacy QiOS Docs
> 
> ### 99_system
> #### system.qispark_rules_schemas_pipeline.md
> ##### System Rules
> ##### Access Control
> ##### Visibility Matrix
> ##### AI Ingest Rules
> ##### Frontmatter Schema
> ##### Navigation Schema
> ##### Registry Schema
> ##### Publish Pipeline
> ##### Recovery Plan
> ##### Do Not Delete Notes
> 
> ## qiserver
> ### 00_root
> #### readme.qiserver_root.md
> #### codex.qiserver_ai_operating_context.md
> 
> ### 10_runtime
> #### Runtime Services
> #### FastAPI
> #### Ollama
> #### Aider
> #### LanceDB
> #### Tmux
> #### Deployment
> 
> ### 20_data_services
> #### SQLite
> #### Supabase
> #### CSV Imports
> #### Vector Indexes
> #### API Connectors
> 
> ### 30_operations
> #### Server Setup
> #### Server Maintenance
> #### Logs
> #### Backups
> #### Recovery
> 
> ### 99_system
> #### qiserver_system_rules
> #### qiserver_boundary_notes
> 
> ## qivault
> ### 00_root
> #### readme.qivault_root.md
> #### codex.qivault_ai_operating_context.md
> 
> ### 10_records
> #### Private Records
> #### Legal Records
> #### Financial Records
> #### Medical Records
> #### Identity Records
> 
> ### 20_evidence
> #### Evidence Storage
> #### Exhibits
> #### Screenshots
> #### Messages
> #### PDFs
> #### Scans
> 
> ### 30_mirrors
> #### Google Drive Mirror
> #### Local Mirror
> #### Archive Mirror
> #### Export Mirror
> 
> ### 40_access
> #### Access Rules
> #### Sensitive Context Rules
> #### Retrieval Rules
> #### Redaction Rules
> 
> ### 99_system
> #### qivault_system_rules
> #### qivault_boundary_notes
> 
> ## cloudflare
> ### 00_build_surface
> #### Cloudflare Pages
> #### Build Output
> #### Public Site
> #### Routes
> #### Redirects
> 
> ### 10_not_source_truth
> #### Cloudflare Does Not Own The Workspace
> #### Cloudflare Does Not Define Canonical Structure
> #### Cloudflare Only Publishes The Approved Build
> 
> ## 99_workspace_system
> ### system.qilabs_workspace_boundaries.md
> #### Workspace Root Rules
> #### Root Relationship Rules
> #### Source Truth Rules
> #### Build Surface Rules
> #### Mirror Rules
> #### Cross Root Navigation Rules
> :::
> 
> ## Cleaner rule
> 
> The corrected model is:
> 
> | Layer | What it is | What it is not |
> |---|---|---|
> | `qilabs.workspace` | True workspace mirror/root | Not just a website |
> | `qispark` | KB, docs, doctrine, nav, maps, decisions | Not server runtime, not vault storage |
> | `qiserver` | Runtime, APIs, local/server infra | Not docs brain |
> | `qivault` | Private records/evidence/storage | Not public docs |
> | `cloudflare` | Build/deploy surface | Not canonical source |
> 
> And yes — **inside QiSpark is where the KB stuff goes**. The stuff that is useful for understanding, navigation, documentation, decisions, prompts, rules, and system memory.
> 
> Not evidence.  
> Not runtime.  
> Not raw private records.  
> Not random file dump.  
> 
> That was the structural correction.

### User
> you see how im trying to tighten up the white space and honestly this is still to starbuck ceo corporate bull crap filling, we nee dto ---
> 
> title: QiLabs Workspace Navigation Map
> section: qilabs.workspace/qispark/99_system/navigation
> access_level: L1
> visibility: private
> ai_ingest: true
> status: draft
> last_updated: 2026-06-20
> mindmap-plugin: basic
> ---------------------
> # qilabs
> 
> ## 00_qilabs.workspace
> ### _root
> - readme.qilabs_workspace.md
> - codex.qilabs_workspace.md
> - manifest.qilabs_workspace.json
> - changelog.qilabs_workspace.md
> 
> ## 01_qispark
> ### 00_root
> #### readme.qispark_root.md
> #### codex.qispark_ai_operating_context.md
> #### changelog.qispark_updates.md
> #### config.qispark_docs_site.json
> 
> ### 01_navigation
> #### map.qispark_navigation_markmind.md
> #### map.qispark_folder_file_tree.md
> #### registry.qispark_navigation.csv
> #### registry.qispark_redirects.csv
> #### audit.qispark_navigation_cleanup.md
> #### rules.qispark_navigation_routes_visibility.md
> 
> ### 10_start_here
> #### guide.qispark_start_here.md
> ##### Welcome
> ##### What QiSpark Is
> ##### How To Use QiSpark
> ##### What Is Canonical
> ##### Current System Status
> ##### Open Loops
> ##### Next Actions
> 
> ### 20_knowledge_base
> #### kb.qispark_core_context.md
> ##### QiSpark Purpose
> ##### QiLabs Purpose
> ##### Current Operating Model
> ##### Important Definitions
> ##### System Boundaries
> #### kb.qispark_working_notes.md
> ##### Active Thinking
> ##### Unsorted Ideas
> ##### Draft Models
> ##### Questions To Resolve
> ##### Not Yet Canonical
> #### kb.qispark_decision_context.md
> ##### Why This Structure Exists
> ##### What Changed
> ##### What Is Locked
> ##### What Is Still Fluid
> 
> ### 30_doctrine
> #### doctrine.qispark_operating_principles.md
> ##### Truth And Alignment
> ##### Leverage And Systems
> ##### Naming Principles
> ##### Modularity
> ##### AI Collaboration
> ##### Human Override Rules
> 
> ### 40_architecture
> #### architecture.qilabs_workspace_map.md
> ##### qilabs.workspace
> ##### qispark
> ##### qiserver
> ##### qivault
> ##### cloudflare_build_surface
> ##### data_flow
> ##### publishing_flow
> #### architecture.qilabs_root_boundaries.md
> ##### QiSpark Boundary
> ##### QiServer Boundary
> ##### QiVault Boundary
> ##### Cloudflare Boundary
> ##### What Does Not Belong In QiSpark
> 
> ### 50_standards
> #### standards.qispark_docs_files_access.md
> ##### File Naming
> ##### Folder Naming
> ##### Markdown Format
> ##### Frontmatter
> ##### Visibility
> ##### Access Levels
> ##### AI Ingest
> ##### Status Values
> ##### Archive Rules
> 
> ### 60_decisions
> #### adr.qispark_architecture_decisions.md
> ##### Why qilabs.workspace Is The Root Mirror
> ##### Why Cloudflare Is Build Surface Only
> ##### Why QiSpark Holds Knowledge And Navigation
> ##### Why QiServer Holds Runtime
> ##### Why QiVault Holds Records And Evidence
> ##### Why Generic Filenames Are Deprecated
> ##### Why Rules Are Merged Instead Of Fragmented
> 
> ### 70_prompts
> #### prompts.qispark_ai_system.md
> ##### QiSpark System Prompt
> ##### QiLabs Workspace Prompt
> ##### Navigation Cleanup Prompt
> ##### Folder Reconciliation Prompt
> ##### Frontmatter Audit Prompt
> #### prompts.qispark_review_extraction.md
> ##### Extract Navigation
> ##### Extract Decisions
> ##### Extract Tasks
> 
> ##### Review Contradictions
> ##### Review Privacy
> ##### Review Canonicality
> 
> ### 80_operations
> #### operations.qispark_maintenance_playbook.md
> ##### Add A Page
> ##### Add A Section
> ##### Update Navigation
> ##### Deprecate A Page
> ##### Archive Content
> ##### Publish Docs
> ##### Run Navigation Audit
> ##### Reconcile Names
> 
> ### 90_reference
> #### reference.qispark_lookup_tables.md
> ##### Glossary
> ##### Canonical Names
> ##### Root Folder Index
> ##### Route Index
> ##### Access Levels
> ##### Visibility Values
> ##### AI Ingest Values
> ##### Status Values
> 
> ### 91_registries
> #### registry.qispark_pages.csv
> #### registry.qispark_sections.csv
> #### registry.qispark_routes.csv
> #### registry.qispark_redirects.csv
> #### registry.qispark_status_access_visibility.csv
> #### registry.qispark_cleanup.csv
> 
> ### 92_audits
> #### audit.qispark_navigation_routes_naming.md
> ##### Navigation Audit
> ##### Route Audit
> ##### Naming Audit
> ##### Duplicate Page Audit
> ##### Stale Page Audit
> ##### Orphan Page Audit
> #### audit.qispark_boundaries_privacy_ingest.md
> ##### QiSpark Boundary Audit
> ##### Public Private Audit
> 
> ##### AI Ingest Audit
> ##### Vault Leakage Audit
> ##### Server Leakage Audit
> 
> ### 93_scripts
> #### scripts.qispark_automation_index.md
> #### generate.qispark_nav_from_csv.py
> #### generate.qispark_registry_from_markdown.py
> #### audit.qispark_frontmatter.py
> #### audit.qispark_links_duplicates.py
> #### generate.qispark_routes_redirects.py
> #### export.qispark_markmind_outline.py
> 
> ### 94_exports
> #### exports.qispark_index.md
> ##### HTML Exports
> ##### PDF Exports
> ##### CSV Exports
> ##### JSON Exports
> ##### Markdown Exports
> 
> ### 97_backlog
> #### backlog.qispark_cleanup_and_build.md
> ##### Open Loops
> ##### Cleanup Tasks
> ##### Renaming Tasks
> ##### Missing Pages
> ##### Docs To Write
> ##### Scripts To Build
> ##### Publish Tasks
> 
> ### 98_archive
> #### archive.qispark_legacy_index.md
> ##### Old Navigation Maps
> ##### Old Names
> ##### Deprecated Pages
> ##### Removed Routes
> ##### Old Exports
> ##### Legacy QiOS Docs
> 
> ### 99_system
> #### system.qispark_rules_schemas_pipeline.md
> ##### System Rules
> ##### Access Control
> ##### Visibility Matrix
> ##### AI Ingest Rules
> ##### Frontmatter Schema
> ##### Navigation Schema
> ##### Registry Schema
> ##### Publish Pipeline
> ##### Recovery Plan
> ##### Do Not Delete Notes
> 
> ## qiserver
> ### 00_root
> #### readme.qiserver_root.md
> #### codex.qiserver_ai_operating_context.md
> 
> ### 10_runtime
> #### Runtime Services
> #### FastAPI
> #### Ollama
> #### Aider
> #### LanceDB
> #### Tmux
> #### Deployment
> 
> ### 20_data_services
> #### SQLite
> #### Supabase
> #### CSV Imports
> 
> #### Vector ndexes
> 
> #### API Connectors
> 
> ### 30_operations
> 
> #### Server Setup
> 
> #### Server Maintenance
> 
> #### Logs
> 
> #### Backups
> 
> #### Recovery
> 
> ### 99_system
> 
> #### qiserver_system_rules
> 
> #### qiserver_boundary_notes
> 
> ## qivault
> 
> ### 00_root
> 
> #### readme.qivault_root.md
> 
> #### codex.qivault_ai_operating_context.md
> 
> ### 10_records
> 
> #### Private Records
> 
> #### Legal Records
> 
> #### Financial Records
> 
> #### Medical Records
> 
> #### Identity Records
> 
> ### 20_evidence
> 
> #### Evidence Storage
> 
> #### Exhibits
> 
> #### Screenshots
> 
> #### Messages
> 
> #### PDFs
> 
> #### Scans
> 
> ### 30_mirrors
> 
> #### Google Drive Mirror
> 
> #### Local Mirror
> 
> #### Archive Mirror
> 
> #### Export Mirror
> 
> ### 40_access
> 
> #### Access Rules
> 
> #### Sensitive Context Rules
> 
> #### Retrieval Rules
> 
> #### Redaction Rules
> 
> ### 99_system
> 
> #### qivault_system_rules
> 
> #### qivault_boundary_notes
> 
> ## cloudflare
> 
> ### 00_build_surface
> 
> #### Cloudflare Pages
> 
> #### Build Output
> 
> #### Public Site
> 
> #### Routes
> 
> #### Redirects
> 
> ### 10_not_source_truth
> 
> #### Cloudflare Does Not Own The Workspace
> 
> #### Cloudflare Does Not Define Canonical Structure
> 
> #### Cloudflare Only Publishes The Approved Build
> 
> ## 99_workspace_system
> 
> ### system.qilabs_workspace_boundaries.md
> 
> #### Workspace Root Rules
> 
> #### Root Relationship Rules
> 
> #### Source Truth Rules
> 
> #### Build Surface Rules
> 
> #### Mirror Rules
> 
> #### Cross Root Navigation Rules

### Assistant
> Yes. You’re right.
> 
> The problem is not just whitespace — it’s **vibe bloat**.
> 
> Too much of this:
> 
> ```text
> Current Operating Model
> Important Definitions
> Publication Map
> Root Relationship Rules
> Build Surface Rules
> ```
> 
> That sounds like a consultant got trapped in a Notion template. We need it more like:
> 
> ```text
> what_is_this.md
> rules.md
> map.md
> do_not_put_here.md
> open_loops.md
> ```
> 
> Cleaner. Sharper. Less corporate fog machine.
> 
> Here’s the tightened version using your structure: **headings for folders/nodes, bullets for file leaves**.
> 
> :::writing{variant="standard" id="58204"}
> ---
> title: QiLabs Workspace Map
> section: qilabs.workspace/qispark/99_system/nav
> access_level: L1
> visibility: private
> ai_ingest: true
> status: draft
> last_updated: 2026-06-20
> mindmap-plugin: basic
> ---
> 
> # qilabs
> 
> ## 00_qilabs.workspace
> ### _root
> - readme.qilabs_workspace.md
> - codex.qilabs_workspace.md
> - manifest.qilabs_workspace.json
> - changelog.qilabs_workspace.md
> 
> ## 01_qispark
> ### 00_root
> - readme.qispark_root.md
> - codex.qispark_ai.md
> - changelog.qispark.md
> - config.qispark_site.json
> 
> ### 01_nav
> - map.qispark_nav.md
> - map.qispark_tree.md
> - registry.qispark_nav.csv
> - registry.qispark_routes.csv
> - audit.qispark_nav.md
> - rules.qispark_nav.md
> 
> ### 10_start
> - guide.qispark_start.md
>   - what_this_is
>   - how_to_use_it
>   - what_is_canonical
>   - current_state
>   - open_loops
>   - next_moves
> 
> ### 20_kb
> - kb.qispark_context.md
>   - qispark
>   - qilabs
>   - terms
>   - boundaries
> - kb.qispark_notes.md
>   - active_thoughts
>   - rough_models
>   - questions
>   - not_canonical
> - kb.qispark_decisions.md
>   - locked
>   - changed
>   - still_fluid
> 
> ### 30_rules
> - rules.qispark_core.md
>   - truth
>   - leverage
>   - naming
>   - modularity
>   - ai_use
>   - human_override
> - rules.qispark_boundaries.md
>   - public_private
>   - qispark_not_vault
>   - qispark_not_server
>   - cloudflare_not_source
> 
> ### 40_maps
> - map.qilabs_workspace.md
>   - qilabs.workspace
>   - qispark
>   - qiserver
>   - qivault
>   - cloudflare
> - map.qilabs_flow.md
>   - capture
>   - vault
>   - spark
>   - server
>   - publish
> - map.qilabs_boundaries.md
>   - what_goes_where
>   - what_does_not_go_here
> 
> ### 50_standards
> - standards.qispark_docs.md
>   - filenames
>   - folders
>   - markdown
>   - frontmatter
>   - links
>   - archive
> - standards.qispark_access.md
>   - access_level
>   - visibility
>   - ai_ingest
>   - status
>   - sensitive_info
> 
> ### 60_adr
> - adr.qispark_structure.md
>   - why_workspace_root
>   - why_cloudflare_is_output
>   - why_qispark_is_kb
>   - why_qiserver_is_runtime
>   - why_qivault_is_records
>   - why_no_generic_filenames
>   - why_fewer_bigger_docs
> 
> ### 70_prompts
> - prompts.qispark_build.md
>   - nav_cleanup
>   - folder_reconcile
>   - docs_generate
>   - frontmatter_audit
> - prompts.qispark_extract.md
>   - extract_nav
>   - extract_decisions
>   - extract_tasks
>   - find_contradictions
>   - check_privacy
> 
> ### 80_ops
> - ops.qispark_maintenance.md
>   - add_page
>   - add_section
>   - update_nav
>   - deprecate_page
>   - archive_content
>   - publish
>   - audit
>   - reconcile_names
> 
> ### 90_ref
> - ref.qispark_tables.md
>   - glossary
>   - canonical_names
>   - root_index
>   - route_index
>   - access_values
>   - visibility_values
>   - ingest_values
>   - status_values
> 
> ### 91_registry
> - registry.qispark_pages.csv
> - registry.qispark_sections.csv
> - registry.qispark_routes.csv
> - registry.qispark_redirects.csv
> - registry.qispark_access.csv
> - registry.qispark_cleanup.csv
> 
> ### 92_audit
> - audit.qispark_nav_names.md
>   - nav
>   - routes
>   - names
>   - duplicates
>   - stale
>   - orphaned
> - audit.qispark_privacy_boundaries.md
>   - public_private
>   - ai_ingest
>   - vault_leak
>   - server_leak
> 
> ### 93_scripts
> - scripts.qispark_index.md
> - generate.qispark_nav.py
> - generate.qispark_registry.py
> - audit.qispark_frontmatter.py
> - audit.qispark_links.py
> - export.qispark_markmind.py
> 
> ### 94_exports
> - exports.qispark_index.md
>   - html
>   - pdf
>   - csv
>   - json
>   - markdown
> 
> ### 97_backlog
> - backlog.qispark.md
>   - open_loops
>   - cleanup
>   - renames
>   - missing_docs
>   - scripts
>   - publish
> 
> ### 98_archive
> - archive.qispark.md
>   - old_nav
>   - old_names
>   - deprecated
>   - removed_routes
>   - old_exports
>   - legacy_qios
> 
> ### 99_system
> - system.qispark.md
>   - rules
>   - schemas
>   - pipeline
>   - recovery
>   - do_not_delete
> 
> ## 02_qiserver
> ### 00_root
> - readme.qiserver_root.md
> - codex.qiserver_ai.md
> 
> ### 10_runtime
> - runtime.qiserver.md
>   - fastapi
>   - ollama
>   - aider
>   - lancedb
>   - tmux
>   - deploy
> 
> ### 20_data
> - data.qiserver.md
>   - sqlite
>   - supabase
>   - csv_imports
>   - vectors
>   - apis
> 
> ### 30_ops
> - ops.qiserver.md
>   - setup
>   - maintenance
>   - logs
>   - backups
>   - recovery
> 
> ### 99_system
> - system.qiserver.md
>   - rules
>   - boundaries
> 
> ## 03_qivault
> ### 00_root
> - readme.qivault_root.md
> - codex.qivault_ai.md
> 
> ### 10_records
> - records.qivault.md
>   - private
>   - legal
>   - money
>   - medical
>   - identity
> 
> ### 20_evidence
> - evidence.qivault.md
>   - exhibits
>   - screenshots
>   - messages
>   - pdfs
>   - scans
> 
> ### 30_mirrors
> - mirrors.qivault.md
>   - google_drive
>   - local
>   - archive
>   - exports
> 
> ### 40_access
> - access.qivault.md
>   - rules
>   - sensitive
>   - retrieval
>   - redaction
> 
> ### 99_system
> - system.qivault.md
>   - rules
>   - boundaries
> 
> ## 90_cloudflare
> ### 00_output
> - build.cloudflare.md
>   - pages
>   - output
>   - public_site
>   - routes
>   - redirects
> 
> ### 10_rules
> - rules.cloudflare.md
>   - not_source
>   - not_canonical
>   - publishes_only
> 
> ## 99_system
> ### _workspace
> - system.qilabs_workspace.md
>   - source_truth
>   - root_rules
>   - mirror_rules
>   - build_rules
>   - cross_root_nav
> :::
> 
> This is closer.
> 
> ## What I changed
> 
> - **Killed corporate labels**
> - **Collapsed bloated sections**
> - **Renamed `knowledge_base` to `kb`**
> - **Renamed `navigation` to `nav`**
> - **Renamed `operations` to `ops`**
> - **Used bullets for actual file leaves**
> - **Kept headings for folders / conceptual map nodes**
> - **Cut the pretend-enterprise language**
> 
> The real naming principle should be:
> 
> ```text
> short enough to scan
> specific enough to search
> plain enough to not annoy us later
> ```
> 
> And yes — `qispark` should feel like a **working brain map**, not a Deloitte deliverable.

### User
> ok i see the main folder right at the begigin but then there is nothing ins ide of those? qispark will be largers of course since qispark is the .md knowledge base.

### Assistant
> Yes. I overcorrected and made the sibling roots too thin.
> 
> The map should show:
> 
> ```text
> qilabs
> ├── workspace root
> ├── qispark = largest / .md KB brain
> ├── qiserver = runtime/server structure
> ├── qivault = records/evidence structure
> ├── cloudflare = build/output
> └── system = rules tying roots together
> ```
> 
> So here’s the better version: **compact, but with real contents under each main folder.**
> 
> :::writing{variant="standard" id="38174"}
> ---
> title: QiLabs Workspace Map
> section: qilabs.workspace/qispark/99_system/nav
> access_level: L1
> visibility: private
> ai_ingest: true
> status: draft
> last_updated: 2026-06-20
> mindmap-plugin: basic
> ---
> 
> # qilabs
> 
> ## 00_qilabs.workspace
> ### _root
> - readme.qilabs_workspace.md
> - codex.qilabs_workspace.md
> - manifest.qilabs_workspace.json
> - changelog.qilabs_workspace.md
> - map.qilabs_roots.md
> - rules.qilabs_source_truth.md
> 
> ### 00_inbox
> - inbox.qilabs.md
>   - raw_notes
>   - unsorted_docs
>   - needs_triage
>   - quick_captures
> 
> ### 01_registry
> - registry.qilabs_roots.csv
> - registry.qilabs_paths.csv
> - registry.qilabs_projects.csv
> - registry.qilabs_status.csv
> 
> ### 99_system
> - system.qilabs_workspace.md
>   - root_rules
>   - naming_rules
>   - source_truth
>   - mirror_rules
>   - cross_root_nav
> 
> ## 01_qispark
> ### 00_root
> - readme.qispark_root.md
> - codex.qispark_ai.md
> - changelog.qispark.md
> - config.qispark_site.json
> 
> ### 01_nav
> - map.qispark_nav.md
> - map.qispark_tree.md
> - registry.qispark_nav.csv
> - registry.qispark_routes.csv
> - registry.qispark_redirects.csv
> - audit.qispark_nav.md
> - rules.qispark_nav.md
> 
> ### 10_start
> - guide.qispark_start.md
>   - what_this_is
>   - how_to_use_it
>   - what_is_canonical
>   - current_state
>   - open_loops
>   - next_moves
> 
> ### 20_kb
> - kb.qispark_context.md
>   - qispark
>   - qilabs
>   - qiserver
>   - qivault
>   - cloudflare
>   - terms
>   - boundaries
> - kb.qispark_notes.md
>   - active_thoughts
>   - rough_models
>   - questions
>   - not_canonical
> - kb.qispark_decisions.md
>   - locked
>   - changed
>   - still_fluid
> - kb.qispark_sources.md
>   - what_counts
>   - what_does_not_count
>   - where_truth_lives
> 
> ### 21_life_os
> - life.qispark_context.md
>   - operating_rules
>   - priorities
>   - constraints
>   - routines
>   - capacity
>   - energy
> - life.qispark_plans.md
>   - current_plan
>   - weekly_map
>   - next_moves
>   - parked_threads
> - life.qispark_decisions.md
>   - life_adrs
>   - tradeoffs
>   - commitments
>   - reversals
> 
> ### 22_business
> - business.qispark_context.md
>   - offers
>   - positioning
>   - clients
>   - services
>   - ops
> - business.qispark_strategy.md
>   - leverage
>   - revenue
>   - systems
>   - assets
>   - pipeline
> - business.qispark_assets.md
>   - bios
>   - blurbs
>   - service_pages
>   - case_studies
>   - reusable_copy
> 
> ### 23_legal_admin
> - legal.qispark_context.md
>   - matters
>   - claims
>   - deadlines
>   - evidence_locations
>   - boundaries
> - admin.qispark_context.md
>   - accounts
>   - forms
>   - benefits
>   - filings
>   - requests
> - legal.qispark_templates.md
>   - letters
>   - disputes
>   - timelines
>   - declarations
>   - exhibit_notes
> 
> ### 24_people
> - people.qispark_context.md
>   - roles
>   - boundaries
>   - trust
>   - contact_rules
>   - history_notes
> - people.qispark_messages.md
>   - scripts
>   - boundaries
>   - replies
>   - escalation_paths
> 
> ### 25_projects
> - projects.qispark_index.md
>   - active
>   - paused
>   - waiting
>   - archived
> - projects.qispark_specs.md
>   - qios
>   - qilife
>   - qiconnect
>   - qinexus
>   - client_work
> - projects.qispark_logs.md
>   - decisions
>   - changes
>   - blockers
>   - next_steps
> 
> ### 30_rules
> - rules.qispark_core.md
>   - truth
>   - leverage
>   - naming
>   - modularity
>   - ai_use
>   - human_override
> - rules.qispark_boundaries.md
>   - public_private
>   - qispark_not_vault
>   - qispark_not_server
>   - cloudflare_not_source
> 
> ### 40_maps
> - map.qilabs_workspace.md
>   - qilabs.workspace
>   - qispark
>   - qiserver
>   - qivault
>   - cloudflare
> - map.qilabs_flow.md
>   - capture
>   - vault
>   - spark
>   - server
>   - publish
> - map.qilabs_boundaries.md
>   - what_goes_where
>   - what_does_not_go_here
> - map.qilabs_apps.md
>   - qilife
>   - qiconnect
>   - qinexus
>   - qidna
>   - qiaccess
> 
> ### 50_standards
> - standards.qispark_docs.md
>   - filenames
>   - folders
>   - markdown
>   - frontmatter
>   - links
>   - archive
> - standards.qispark_access.md
>   - access_level
>   - visibility
>   - ai_ingest
>   - status
>   - sensitive_info
> - standards.qispark_publish.md
>   - route_rules
>   - public_pages
>   - private_pages
>   - redirects
>   - exports
> 
> ### 60_adr
> - adr.qispark_structure.md
>   - why_workspace_root
>   - why_cloudflare_is_output
>   - why_qispark_is_kb
>   - why_qiserver_is_runtime
>   - why_qivault_is_records
>   - why_no_generic_filenames
>   - why_fewer_bigger_docs
> 
> ### 70_prompts
> - prompts.qispark_build.md
>   - nav_cleanup
>   - folder_reconcile
>   - docs_generate
>   - frontmatter_audit
> - prompts.qispark_extract.md
>   - extract_nav
>   - extract_decisions
>   - extract_tasks
>   - find_contradictions
>   - check_privacy
> - prompts.qispark_write.md
>   - clean_doc
>   - compress_notes
>   - make_timeline
>   - make_plan
>   - make_message
> 
> ### 80_ops
> - ops.qispark_maintenance.md
>   - add_page
>   - add_section
>   - update_nav
>   - deprecate_page
>   - archive_content
>   - publish
>   - audit
>   - reconcile_names
> 
> ### 90_ref
> - ref.qispark_tables.md
>   - glossary
>   - canonical_names
>   - root_index
>   - route_index
>   - access_values
>   - visibility_values
>   - ingest_values
>   - status_values
> 
> ### 91_registry
> - registry.qispark_pages.csv
> - registry.qispark_sections.csv
> - registry.qispark_routes.csv
> - registry.qispark_redirects.csv
> - registry.qispark_access.csv
> - registry.qispark_cleanup.csv
> 
> ### 92_audit
> - audit.qispark_nav_names.md
>   - nav
>   - routes
>   - names
>   - duplicates
>   - stale
>   - orphaned
> - audit.qispark_privacy_boundaries.md
>   - public_private
>   - ai_ingest
>   - vault_leak
>   - server_leak
> 
> ### 93_scripts
> - scripts.qispark_index.md
> - generate.qispark_nav.py
> - generate.qispark_registry.py
> - audit.qispark_frontmatter.py
> - audit.qispark_links.py
> - export.qispark_markmind.py
> 
> ### 94_exports
> - exports.qispark_index.md
>   - html
>   - pdf
>   - csv
>   - json
>   - markdown
> 
> ### 97_backlog
> - backlog.qispark.md
>   - open_loops
>   - cleanup
>   - renames
>   - missing_docs
>   - scripts
>   - publish
> 
> ### 98_archive
> - archive.qispark.md
>   - old_nav
>   - old_names
>   - deprecated
>   - removed_routes
>   - old_exports
>   - legacy_qios
> 
> ### 99_system
> - system.qispark.md
>   - rules
>   - schemas
>   - pipeline
>   - recovery
>   - do_not_delete
> 
> ## 02_qiserver
> ### 00_root
> - readme.qiserver_root.md
> - codex.qiserver_ai.md
> - changelog.qiserver.md
> - env.qiserver_example.env
> 
> ### 01_config
> - config.qiserver_runtime.md
> - config.qiserver_env.md
> - config.qiserver_ports.md
> - config.qiserver_paths.md
> 
> ### 10_runtime
> - runtime.qiserver.md
>   - fastapi
>   - ollama
>   - aider
>   - lancedb
>   - tmux
>   - deploy
> - service.qiserver_api.md
> - service.qiserver_llm.md
> - service.qiserver_vector.md
> 
> ### 20_data
> - data.qiserver.md
>   - sqlite
>   - supabase
>   - csv_imports
>   - vectors
>   - apis
> - schema.qiserver_sqlite.md
> - schema.qiserver_supabase.md
> - pipeline.qiserver_ingest.md
> 
> ### 30_apps
> - app.qilife_server.md
> - app.qiconnect_server.md
> - app.qinexus_server.md
> - app.qidna_server.md
> 
> ### 40_jobs
> - jobs.qiserver_sync.md
> - jobs.qiserver_backup.md
> - jobs.qiserver_ingest.md
> - jobs.qiserver_cleanup.md
> 
> ### 50_logs
> - logs.qiserver_index.md
>   - runtime_logs
>   - error_logs
>   - deploy_logs
>   - ingest_logs
> 
> ### 80_ops
> - ops.qiserver.md
>   - setup
>   - maintenance
>   - restart
>   - backups
>   - recovery
>   - troubleshooting
> 
> ### 99_system
> - system.qiserver.md
>   - rules
>   - boundaries
>   - do_not_put_here
> 
> ## 03_qivault
> ### 00_root
> - readme.qivault_root.md
> - codex.qivault_ai.md
> - changelog.qivault.md
> - rules.qivault_source_truth.md
> 
> ### 01_index
> - index.qivault_records.md
> - index.qivault_evidence.md
> - index.qivault_people.md
> - index.qivault_matters.md
> - index.qivault_exports.md
> 
> ### 10_records
> - records.qivault_identity.md
>   - ids
>   - licenses
>   - social_security
>   - immigration
> - records.qivault_legal.md
>   - claims
>   - notices
>   - filings
>   - court
> - records.qivault_money.md
>   - income
>   - bills
>   - taxes
>   - disputes
> - records.qivault_medical.md
>   - medical
>   - prescriptions
>   - visits
>   - insurance
> - records.qivault_housing.md
>   - leases
>   - utilities
>   - repairs
>   - notices
> 
> ### 20_evidence
> - evidence.qivault_index.md
>   - exhibits
>   - screenshots
>   - messages
>   - pdfs
>   - scans
>   - photos
>   - audio
>   - video
> - evidence.qivault_timelines.md
> - evidence.qivault_exhibits.md
> - evidence.qivault_sources.md
> 
> ### 30_people
> - people.qivault_index.md
>   - family
>   - clients
>   - vendors
>   - agencies
>   - doctors
>   - attorneys
> 
> ### 40_mirrors
> - mirrors.qivault.md
>   - google_drive
>   - local
>   - archive
>   - exports
> - mirror.qivault_google_drive.md
> - mirror.qivault_local.md
> - mirror.qivault_archive.md
> 
> ### 50_access
> - access.qivault.md
>   - rules
>   - sensitive
>   - retrieval
>   - redaction
>   - sharing
> - redaction.qivault_rules.md
> - retrieval.qivault_rules.md
> 
> ### 80_exports
> - exports.qivault_index.md
>   - pdf
>   - zip
>   - exhibit_packets
>   - csv
>   - json
> 
> ### 99_system
> - system.qivault.md
>   - rules
>   - boundaries
>   - do_not_put_here
> 
> ## 04_qicapture
> ### 00_root
> - readme.qicapture_root.md
> - codex.qicapture_ai.md
> 
> ### 10_inbox
> - inbox.qicapture.md
>   - voice
>   - screenshots
>   - scans
>   - notes
>   - webclips
>   - downloads
> 
> ### 20_triage
> - triage.qicapture_rules.md
>   - keep
>   - delete
>   - vault
>   - spark
>   - server
>   - archive
> 
> ### 30_processing
> - process.qicapture_pipeline.md
>   - rename
>   - tag
>   - summarize
>   - route
>   - ingest
> 
> ### 99_system
> - system.qicapture.md
>   - rules
>   - boundaries
> 
> ## 05_qiapps
> ### 00_root
> - readme.qiapps_root.md
> - codex.qiapps_ai.md
> 
> ### 10_qilife
> - app.qilife_spec.md
>   - dashboard
>   - routines
>   - tasks
>   - money
>   - health
>   - legal
>   - gigi
> 
> ### 20_qiconnect
> - app.qiconnect_spec.md
>   - contacts
>   - messages
>   - clients
>   - vendors
>   - crm
>   - outreach
> 
> ### 30_qinexus
> - app.qinexus_spec.md
>   - search
>   - retrieval
>   - records
>   - evidence
>   - semantic_index
> 
> ### 40_qidna
> - app.qidna_spec.md
>   - identity
>   - rules
>   - preferences
>   - memory
>   - ai_alignment
> 
> ### 50_qiaccess
> - app.qiaccess_spec.md
>   - accounts
>   - devices
>   - permissions
>   - recovery
>   - security
> 
> ### 99_system
> - system.qiapps.md
>   - app_boundaries
>   - shared_patterns
>   - do_not_mix
> 
> ## 90_cloudflare
> ### 00_output
> - build.cloudflare.md
>   - pages
>   - output
>   - public_site
>   - routes
>   - redirects
> 
> ### 10_site
> - site.cloudflare_routes.md
> - site.cloudflare_redirects.md
> - site.cloudflare_env.md
> - site.cloudflare_build_notes.md
> 
> ### 20_rules
> - rules.cloudflare.md
>   - not_source
>   - not_canonical
>   - publishes_only
>   - no_private_leaks
> 
> ## 99_system
> ### _workspace
> - system.qilabs_workspace.md
>   - source_truth
>   - root_rules
>   - mirror_rules
>   - build_rules
>   - cross_root_nav
> - audit.qilabs_workspace.md
>   - missing_roots
>   - naming_drift
>   - duplicate_paths
>   - boundary_leaks
> :::
> 
> This version makes the hierarchy more honest:
> 
> ```text
> qispark = biggest because it is the .md knowledge base
> qiserver = real server/runtime docs, but not every line of code
> qivault = real record/evidence structure, but not the files themselves
> qicapture = intake/triage layer
> qiapps = app specs layer
> cloudflare = output layer only
> ```
> 
> And yes, this is the right instinct: the first nodes should **not** be empty labels. They need enough substance that the whole map shows the actual QiLabs organism.

### User
> nope cloueflare is inside qiconnect inside qiserver or its own module in side of services inside of qiserer not a root level thin

### Assistant
> Yep. Correct correction.
> 
> **Cloudflare should not be root-level.**  
> It belongs inside the server/service layer.
> 
> The better model:
> 
> ```text
> qilabs
> ├── 00_qilabs.workspace
> ├── 01_qispark
> ├── 02_qiserver
> │   └── services
> │       ├── qiconnect
> │       └── cloudflare
> ├── 03_qivault
> ├── 04_qicapture
> ├── 05_qiapps
> └── 99_system
> ```
> 
> Or, if Cloudflare is mainly tied to the web/contact/public site layer:
> 
> ```text
> 02_qiserver
> └── services
>     └── qiconnect
>         └── cloudflare
> ```
> 
> My recommendation: **put it under `qiserver/services/cloudflare`**, unless it is specifically only serving QiConnect.
> 
> Here’s the corrected slice:
> 
> :::writing{variant="standard" id="75629"}
> ## 02_qiserver
> ### 00_root
> - readme.qiserver_root.md
> - codex.qiserver_ai.md
> - changelog.qiserver.md
> - env.qiserver_example.env
> 
> ### 01_config
> - config.qiserver_runtime.md
> - config.qiserver_env.md
> - config.qiserver_ports.md
> - config.qiserver_paths.md
> 
> ### 10_runtime
> - runtime.qiserver.md
>   - fastapi
>   - ollama
>   - aider
>   - lancedb
>   - tmux
>   - deploy
> 
> ### 20_data
> - data.qiserver.md
>   - sqlite
>   - supabase
>   - csv_imports
>   - vectors
>   - apis
> 
> ### 30_services
> - service.qiserver_api.md
>   - routes
>   - endpoints
>   - auth
>   - webhooks
> - service.qiserver_llm.md
>   - ollama
>   - prompts
>   - embeddings
>   - retrieval
> - service.qiserver_vector.md
>   - lancedb
>   - indexes
>   - search
>   - sync
> - service.qiserver_cloudflare.md
>   - pages
>   - workers
>   - routes
>   - redirects
>   - env
>   - deploy
>   - public_output
>   - not_source_truth
> 
> ### 40_qiconnect
> - app.qiconnect_server.md
>   - contacts
>   - messages
>   - clients
>   - vendors
>   - crm
>   - outreach
> - service.qiconnect_cloudflare.md
>   - public_pages
>   - contact_forms
>   - lead_routes
>   - redirects
>   - deployment
> 
> ### 50_jobs
> - jobs.qiserver_sync.md
> - jobs.qiserver_backup.md
> - jobs.qiserver_ingest.md
> - jobs.qiserver_cleanup.md
> 
> ### 60_logs
> - logs.qiserver_index.md
>   - runtime_logs
>   - error_logs
>   - deploy_logs
>   - ingest_logs
> 
> ### 80_ops
> - ops.qiserver.md
>   - setup
>   - maintenance
>   - restart
>   - backups
>   - recovery
>   - troubleshooting
> 
> ### 99_system
> - system.qiserver.md
>   - rules
>   - boundaries
>   - do_not_put_here
> :::
> 
> ## The rule
> 
> Cloudflare is:
> 
> ```text
> server/service/deploy infrastructure
> ```
> 
> Not:
> 
> ```text
> workspace root
> knowledge base
> vault
> source truth
> ```
> 
> So the root-level `90_cloudflare` node gets deleted.
> 
> If we keep a reference to it in QiSpark, it should only appear as a **map/reference entry**, like:
> 
> ```text
> qispark / maps / qiserver_cloudflare_deploy_flow
> ```
> 
> Not as a root folder. Good catch.

### User
> qi capture is now qimemory also sindie of qiserver somethwere, and ther eis no system 99 folder, that is wou qilabs workspace folder essentially.

### Assistant
> Yep. Locking that correction in.
> 
> The top level is now more like:
> 
> ```text
> qilabs
> ├── 00_qilabs.workspace
> ├── 01_qispark
> ├── 02_qiserver
> ├── 03_qivault
> └── 05_qiapps
> ```
> 
> No standalone:
> 
> ```text
> 04_qicapture
> 99_system
> 90_cloudflare
> ```
> 
> Those were wrong.
> 
> ## Corrected architecture
> 
> ```text
> qilabs
> ├── 00_qilabs.workspace
> │   ├── workspace rules
> │   ├── root registry
> │   ├── source truth
> │   ├── naming rules
> │   ├── mirror rules
> │   └── cross-root map
> │
> ├── 01_qispark
> │   └── markdown knowledge base / docs / maps / rules / prompts
> │
> ├── 02_qiserver
> │   ├── runtime
> │   ├── data
> │   ├── services
> │   │   ├── cloudflare
> │   │   ├── qiconnect
> │   │   └── qimemory
> │   ├── jobs
> │   ├── logs
> │   └── ops
> │
> ├── 03_qivault
> │   └── records / evidence / private source files
> │
> └── 05_qiapps
>     └── app specs / app-facing docs
> ```
> 
> ## Key corrections
> 
> | Wrong | Correct |
> |---|---|
> | `04_qicapture` root | Fold into `qiserver/services/qimemory` |
> | `90_cloudflare` root | Put under `qiserver/services/cloudflare` |
> | `99_system` root | Fold into `00_qilabs.workspace` |
> | QiSpark as whole workspace | QiSpark is the `.md` KB/docs layer |
> | Cloudflare as canonical source | Cloudflare is deploy/output service only |
> 
> ## Updated qiserver shape
> 
> ```text
> ## 02_qiserver
> ### 00_root
> - readme.qiserver_root.md
> - codex.qiserver_ai.md
> - changelog.qiserver.md
> - env.qiserver_example.env
> 
> ### 01_config
> - config.qiserver_runtime.md
> - config.qiserver_env.md
> - config.qiserver_ports.md
> - config.qiserver_paths.md
> 
> ### 10_runtime
> - runtime.qiserver.md
>   - fastapi
>   - ollama
>   - aider
>   - lancedb
>   - tmux
>   - deploy
> 
> ### 20_data
> - data.qiserver.md
>   - sqlite
>   - supabase
>   - csv_imports
>   - vectors
>   - apis
> 
> ### 30_services
> - service.qiserver_api.md
>   - routes
>   - endpoints
>   - auth
>   - webhooks
> 
> - service.qiserver_cloudflare.md
>   - pages
>   - workers
>   - routes
>   - redirects
>   - env
>   - deploy
>   - public_output
>   - not_source_truth
> 
> - service.qiserver_qiconnect.md
>   - contacts
>   - messages
>   - clients
>   - vendors
>   - crm
>   - outreach
>   - public_forms
> 
> - service.qiserver_qimemory.md
>   - capture
>   - ingest
>   - summarize
>   - embed
>   - classify
>   - route
>   - recall
>   - archive_pointer
> 
> ### 40_jobs
> - jobs.qiserver_sync.md
> - jobs.qiserver_backup.md
> - jobs.qiserver_ingest.md
> - jobs.qiserver_memory.md
> - jobs.qiserver_cleanup.md
> 
> ### 50_logs
> - logs.qiserver_index.md
>   - runtime
>   - errors
>   - deploy
>   - ingest
>   - memory
> 
> ### 80_ops
> - ops.qiserver.md
>   - setup
>   - maintenance
>   - restart
>   - backups
>   - recovery
>   - troubleshooting
> ```
> 
> And `00_qilabs.workspace` absorbs the old `99_system` stuff:
> 
> ```text
> ## 00_qilabs.workspace
> ### _root
> - readme.qilabs_workspace.md
> - codex.qilabs_workspace.md
> - manifest.qilabs_workspace.json
> - changelog.qilabs_workspace.md
> 
> ### 01_rules
> - rules.qilabs_workspace.md
>   - source_truth
>   - root_rules
>   - naming
>   - mirrors
>   - build_rules
>   - cross_root_nav
>   - do_not_mix
> 
> ### 02_registry
> - registry.qilabs_roots.csv
> - registry.qilabs_paths.csv
> - registry.qilabs_projects.csv
> - registry.qilabs_status.csv
> 
> ### 03_maps
> - map.qilabs_roots.md
> - map.qilabs_boundaries.md
> - map.qilabs_flow.md
> 
> ### 04_audit
> - audit.qilabs_workspace.md
>   - missing_roots
>   - naming_drift
>   - duplicate_paths
>   - boundary_leaks
> ```
> 
> That’s cleaner. `00_qilabs.workspace` is the workspace control layer. No extra fake “system” folder needed.

### User
> this seems much closure give me the full tree now to see if your on the right track.

### Assistant
> This version treats `00_qilabs.workspace` as the control layer, keeps `qispark` as the big Markdown KB, and puts both `qimemory` and `cloudflare` inside `qiserver`. No fake root-level system folder.

### Assistant
> Yes — this is much closer. I also trimmed the “corporate fog” and kept the tree readable.
> 
> Key assumptions in this draft:
> 
> ```text
> qispark = largest .md knowledge base
> qiserver = runtime/services/data layer
> qimemory = inside qiserver/services
> cloudflare = inside qiserver/services/qiconnect
> qivault = private records/evidence storage map
> 00_qilabs.workspace = workspace/system control layer
> ```
> 
> :::writing{variant="standard" id="27483"}
> ---
> title: QiLabs Workspace Map
> section: qilabs.workspace/qispark/01_nav
> access_level: L1
> visibility: private
> ai_ingest: true
> status: draft
> last_updated: 2026-06-20
> mindmap-plugin: basic
> ---
> 
> # qilabs
> 
> ## 00_qilabs.workspace
> ### _root
> - readme.qilabs_workspace.md
> - codex.qilabs_workspace.md
> - manifest.qilabs_workspace.json
> - changelog.qilabs_workspace.md
> - map.qilabs_roots.md
> - rules.qilabs_source_truth.md
> 
> ### 01_rules
> - rules.qilabs_workspace.md
>   - source_truth
>   - root_rules
>   - naming
>   - mirrors
>   - build_output
>   - cross_root_nav
>   - do_not_mix
> 
> ### 02_registry
> - registry.qilabs_roots.csv
> - registry.qilabs_paths.csv
> - registry.qilabs_projects.csv
> - registry.qilabs_status.csv
> - registry.qilabs_services.csv
> 
> ### 03_maps
> - map.qilabs_roots.md
>   - workspace
>   - qispark
>   - qiserver
>   - qivault
>   - qiapps
> - map.qilabs_boundaries.md
>   - what_goes_where
>   - what_does_not_go_where
> - map.qilabs_flow.md
>   - capture
>   - memory
>   - vault
>   - spark
>   - server
>   - publish
> - map.qilabs_names.md
>   - current_names
>   - old_names
>   - renamed
>   - deprecated
> 
> ### 04_inbox
> - inbox.qilabs.md
>   - raw_notes
>   - unsorted_docs
>   - quick_captures
>   - needs_triage
> 
> ### 05_audit
> - audit.qilabs_workspace.md
>   - missing_roots
>   - naming_drift
>   - duplicate_paths
>   - boundary_leaks
>   - stale_maps
> 
> ## 01_qispark
> ### 00_root
> - readme.qispark_root.md
> - codex.qispark_ai.md
> - changelog.qispark.md
> - config.qispark_site.json
> 
> ### 01_nav
> - map.qispark_nav.md
> - map.qispark_tree.md
> - registry.qispark_nav.csv
> - registry.qispark_routes.csv
> - registry.qispark_redirects.csv
> - audit.qispark_nav.md
> - rules.qispark_nav.md
> 
> ### 10_start
> - guide.qispark_start.md
>   - what_this_is
>   - how_to_use_it
>   - what_is_canonical
>   - current_state
>   - open_loops
>   - next_moves
> 
> ### 20_kb
> - kb.qispark_context.md
>   - qispark
>   - qilabs
>   - qiserver
>   - qivault
>   - qiapps
>   - terms
>   - boundaries
> - kb.qispark_notes.md
>   - active_thoughts
>   - rough_models
>   - questions
>   - not_canonical
> - kb.qispark_sources.md
>   - what_counts
>   - what_does_not_count
>   - where_truth_lives
> - kb.qispark_changes.md
>   - locked
>   - changed
>   - still_fluid
>   - parked
> 
> ### 21_life
> - life.qispark_context.md
>   - operating_rules
>   - priorities
>   - constraints
>   - capacity
>   - routines
>   - energy
> - life.qispark_plans.md
>   - current_plan
>   - weekly_map
>   - next_moves
>   - parked_threads
> - life.qispark_decisions.md
>   - tradeoffs
>   - commitments
>   - reversals
>   - lessons
> 
> ### 22_business
> - business.qispark_context.md
>   - positioning
>   - offers
>   - clients
>   - services
>   - ops
> - business.qispark_strategy.md
>   - leverage
>   - revenue
>   - systems
>   - assets
>   - pipeline
> - business.qispark_assets.md
>   - bios
>   - blurbs
>   - service_pages
>   - case_studies
>   - reusable_copy
> 
> ### 23_admin
> - admin.qispark_context.md
>   - accounts
>   - forms
>   - benefits
>   - filings
>   - requests
> - admin.qispark_templates.md
>   - letters
>   - disputes
>   - timelines
>   - declarations
>   - exhibit_notes
> 
> ### 24_legal
> - legal.qispark_context.md
>   - matters
>   - claims
>   - deadlines
>   - evidence_locations
>   - boundaries
> - legal.qispark_templates.md
>   - letters
>   - notices
>   - disputes
>   - timelines
>   - declarations
> 
> ### 25_people
> - people.qispark_context.md
>   - roles
>   - trust
>   - boundaries
>   - contact_rules
>   - history_notes
> - people.qispark_messages.md
>   - scripts
>   - replies
>   - boundaries
>   - escalation_paths
> 
> ### 26_projects
> - projects.qispark_index.md
>   - active
>   - waiting
>   - paused
>   - archived
> - projects.qispark_specs.md
>   - qios
>   - qilife
>   - qiconnect
>   - qinexus
>   - qidna
>   - client_work
> - projects.qispark_logs.md
>   - decisions
>   - changes
>   - blockers
>   - next_steps
> 
> ### 30_rules
> - rules.qispark_core.md
>   - truth
>   - leverage
>   - naming
>   - modularity
>   - ai_use
>   - human_override
> - rules.qispark_boundaries.md
>   - public_private
>   - qispark_not_vault
>   - qispark_not_server
>   - docs_not_evidence
>   - maps_not_runtime
> - rules.qispark_filenames.md
>   - no_generic_names
>   - context_names
>   - short_but_searchable
>   - legacy_exceptions
> 
> ### 40_maps
> - map.qilabs_workspace.md
>   - workspace
>   - qispark
>   - qiserver
>   - qivault
>   - qiapps
> - map.qilabs_flow.md
>   - capture
>   - memory
>   - vault
>   - spark
>   - server
>   - publish
> - map.qilabs_boundaries.md
>   - what_goes_where
>   - what_does_not_go_here
> - map.qilabs_apps.md
>   - qilife
>   - qiconnect
>   - qinexus
>   - qidna
>   - qiaccess
> 
> ### 50_standards
> - standards.qispark_docs.md
>   - filenames
>   - folders
>   - markdown
>   - frontmatter
>   - links
>   - archive
> - standards.qispark_access.md
>   - access_level
>   - visibility
>   - ai_ingest
>   - status
>   - sensitive_info
> - standards.qispark_publish.md
>   - route_rules
>   - public_pages
>   - private_pages
>   - redirects
>   - exports
> 
> ### 60_adr
> - adr.qispark_structure.md
>   - why_workspace_root
>   - why_qispark_is_kb
>   - why_qiserver_is_runtime
>   - why_qivault_is_records
>   - why_qimemory_lives_in_qiserver
>   - why_cloudflare_lives_under_qiserver
>   - why_no_generic_filenames
>   - why_fewer_bigger_docs
> 
> ### 70_prompts
> - prompts.qispark_build.md
>   - nav_cleanup
>   - folder_reconcile
>   - docs_generate
>   - frontmatter_audit
> - prompts.qispark_extract.md
>   - extract_nav
>   - extract_decisions
>   - extract_tasks
>   - find_contradictions
>   - check_privacy
> - prompts.qispark_write.md
>   - clean_doc
>   - compress_notes
>   - make_timeline
>   - make_plan
>   - make_message
> 
> ### 80_ops
> - ops.qispark_maintenance.md
>   - add_page
>   - add_section
>   - update_nav
>   - deprecate_page
>   - archive_content
>   - publish
>   - audit
>   - reconcile_names
> 
> ### 90_ref
> - ref.qispark_tables.md
>   - glossary
>   - canonical_names
>   - root_index
>   - route_index
>   - access_values
>   - visibility_values
>   - ingest_values
>   - status_values
> 
> ### 91_registry
> - registry.qispark_pages.csv
> - registry.qispark_sections.csv
> - registry.qispark_routes.csv
> - registry.qispark_redirects.csv
> - registry.qispark_access.csv
> - registry.qispark_cleanup.csv
> 
> ### 92_audit
> - audit.qispark_nav_names.md
>   - nav
>   - routes
>   - names
>   - duplicates
>   - stale
>   - orphaned
> - audit.qispark_privacy_boundaries.md
>   - public_private
>   - ai_ingest
>   - vault_leak
>   - server_leak
> 
> ### 93_scripts
> - scripts.qispark_index.md
> - generate.qispark_nav.py
> - generate.qispark_registry.py
> - audit.qispark_frontmatter.py
> - audit.qispark_links.py
> - export.qispark_markmind.py
> 
> ### 94_exports
> - exports.qispark_index.md
>   - html
>   - pdf
>   - csv
>   - json
>   - markdown
> 
> ### 97_backlog
> - backlog.qispark.md
>   - open_loops
>   - cleanup
>   - renames
>   - missing_docs
>   - scripts
>   - publish
> 
> ### 98_archive
> - archive.qispark.md
>   - old_nav
>   - old_names
>   - deprecated
>   - removed_routes
>   - old_exports
>   - legacy_qios
> 
> ## 02_qiserver
> ### 00_root
> - readme.qiserver_root.md
> - codex.qiserver_ai.md
> - changelog.qiserver.md
> - env.qiserver_example.env
> 
> ### 01_config
> - config.qiserver_runtime.md
> - config.qiserver_env.md
> - config.qiserver_ports.md
> - config.qiserver_paths.md
> - config.qiserver_secrets.example.md
> 
> ### 10_runtime
> - runtime.qiserver.md
>   - fastapi
>   - ollama
>   - aider
>   - lancedb
>   - tmux
>   - deploy
> - runtime.qiserver_processes.md
> - runtime.qiserver_ports.md
> 
> ### 20_data
> - data.qiserver.md
>   - sqlite
>   - supabase
>   - csv_imports
>   - vectors
>   - apis
> - schema.qiserver_sqlite.md
> - schema.qiserver_supabase.md
> - pipeline.qiserver_ingest.md
> - pipeline.qiserver_sync.md
> 
> ### 30_services
> #### qiconnect
> - service.qiserver_qiconnect.md
>   - contacts
>   - messages
>   - clients
>   - vendors
>   - crm
>   - outreach
>   - public_forms
> - service.qiconnect_cloudflare.md
>   - pages
>   - workers
>   - routes
>   - redirects
>   - env
>   - deploy
>   - public_output
>   - not_source_truth
> 
> #### qimemory
> - service.qiserver_qimemory.md
>   - capture
>   - ingest
>   - summarize
>   - embed
>   - classify
>   - route
>   - recall
>   - archive_pointer
> - pipeline.qimemory_capture.md
>   - voice
>   - screenshots
>   - notes
>   - webclips
>   - scans
>   - downloads
> - pipeline.qimemory_triage.md
>   - keep
>   - delete
>   - vault
>   - spark
>   - server
>   - archive
> - pipeline.qimemory_ingest.md
>   - rename
>   - tag
>   - summarize
>   - embed
>   - route
> 
> #### qiapi
> - service.qiserver_api.md
>   - routes
>   - endpoints
>   - auth
>   - webhooks
>   - healthcheck
> 
> #### qillm
> - service.qiserver_llm.md
>   - ollama
>   - prompts
>   - embeddings
>   - retrieval
>   - local_models
> 
> #### qivector
> - service.qiserver_vector.md
>   - lancedb
>   - indexes
>   - search
>   - sync
> 
> ### 40_apps_runtime
> - app.qilife_server.md
>   - dashboard_api
>   - routines
>   - tasks
>   - money
>   - health
>   - legal
> - app.qinexus_server.md
>   - search
>   - retrieval
>   - evidence_pointers
>   - semantic_index
> - app.qidna_server.md
>   - preferences
>   - rules
>   - memory_profile
>   - ai_alignment
> - app.qiaccess_server.md
>   - accounts
>   - devices
>   - permissions
>   - recovery
> 
> ### 50_jobs
> - jobs.qiserver_sync.md
> - jobs.qiserver_backup.md
> - jobs.qiserver_ingest.md
> - jobs.qiserver_memory.md
> - jobs.qiserver_cleanup.md
> - jobs.qiserver_deploy.md
> 
> ### 60_logs
> - logs.qiserver_index.md
>   - runtime
>   - errors
>   - deploy
>   - ingest
>   - memory
>   - sync
> 
> ### 80_ops
> - ops.qiserver.md
>   - setup
>   - maintenance
>   - restart
>   - backups
>   - recovery
>   - troubleshooting
> - ops.qiserver_deploy.md
>   - local
>   - cloudflare
>   - env
>   - rollback
> 
> ### 90_rules
> - rules.qiserver_boundaries.md
>   - runtime_not_kb
>   - server_not_vault
>   - service_boundaries
>   - secrets_never_public
>   - do_not_put_here
> 
> ## 03_qivault
> ### 00_root
> - readme.qivault_root.md
> - codex.qivault_ai.md
> - changelog.qivault.md
> - rules.qivault_source_truth.md
> 
> ### 01_index
> - index.qivault_records.md
> - index.qivault_evidence.md
> - index.qivault_people.md
> - index.qivault_matters.md
> - index.qivault_exports.md
> 
> ### 10_records
> - records.qivault_identity.md
>   - ids
>   - licenses
>   - social_security
>   - immigration
> - records.qivault_legal.md
>   - claims
>   - notices
>   - filings
>   - court
> - records.qivault_money.md
>   - income
>   - bills
>   - taxes
>   - disputes
> - records.qivault_medical.md
>   - medical
>   - prescriptions
>   - visits
>   - insurance
> - records.qivault_housing.md
>   - leases
>   - utilities
>   - repairs
>   - notices
> 
> ### 20_evidence
> - evidence.qivault_index.md
>   - exhibits
>   - screenshots
>   - messages
>   - pdfs
>   - scans
>   - photos
>   - audio
>   - video
> - evidence.qivault_timelines.md
> - evidence.qivault_exhibits.md
> - evidence.qivault_sources.md
> 
> ### 30_people
> - people.qivault_index.md
>   - family
>   - clients
>   - vendors
>   - agencies
>   - doctors
>   - attorneys
> 
> ### 40_mirrors
> - mirrors.qivault.md
>   - google_drive
>   - local
>   - archive
>   - exports
> - mirror.qivault_google_drive.md
> - mirror.qivault_local.md
> - mirror.qivault_archive.md
> 
> ### 50_access
> - access.qivault.md
>   - rules
>   - sensitive
>   - retrieval
>   - redaction
>   - sharing
> - redaction.qivault_rules.md
> - retrieval.qivault_rules.md
> 
> ### 80_exports
> - exports.qivault_index.md
>   - pdf
>   - zip
>   - exhibit_packets
>   - csv
>   - json
> 
> ### 90_rules
> - rules.qivault_boundaries.md
>   - vault_is_source_for_records
>   - vault_not_public
>   - vault_not_kb
>   - evidence_not_spark
>   - do_not_put_here
> 
> ## 04_qiapps
> ### 00_root
> - readme.qiapps_root.md
> - codex.qiapps_ai.md
> - changelog.qiapps.md
> 
> ### 10_qilife
> - spec.qilife_app.md
>   - dashboard
>   - routines
>   - tasks
>   - money
>   - health
>   - legal
>   - gigi
> - map.qilife_flows.md
> - backlog.qilife_app.md
> 
> ### 20_qiconnect
> - spec.qiconnect_app.md
>   - contacts
>   - messages
>   - clients
>   - vendors
>   - crm
>   - outreach
> - map.qiconnect_flows.md
> - backlog.qiconnect_app.md
> 
> ### 30_qinexus
> - spec.qinexus_app.md
>   - search
>   - retrieval
>   - records
>   - evidence
>   - semantic_index
> - map.qinexus_flows.md
> - backlog.qinexus_app.md
> 
> ### 40_qidna
> - spec.qidna_app.md
>   - identity
>   - rules
>   - preferences
>   - memory
>   - ai_alignment
> - map.qidna_flows.md
> - backlog.qidna_app.md
> 
> ### 50_qiaccess
> - spec.qiaccess_app.md
>   - accounts
>   - devices
>   - permissions
>   - recovery
>   - security
> - map.qiaccess_flows.md
> - backlog.qiaccess_app.md
> 
> ### 90_rules
> - rules.qiapps_boundaries.md
>   - app_specs_not_runtime
>   - app_specs_not_vault
>   - shared_patterns
>   - do_not_mix
> :::
> 
> ## What I changed from the wrong version
> 
> | Before | Now |
> |---|---|
> | `90_cloudflare` root | `02_qiserver / 30_services / qiconnect / service.qiconnect_cloudflare.md` |
> | `04_qicapture` root | `02_qiserver / 30_services / qimemory` |
> | `99_system` root | absorbed into `00_qilabs.workspace` |
> | Thin root folders | each top folder now has real contents |
> | Corporate labels | more functional names |
> 
> This is now structurally sane. Still draft, but the spine is finally behaving.

### User
> ok this is the very top approved as of now, # Approved Top
> # qilabs
> ## 00_qilabs.workspace
> ## 10_qispark
> ## 20_qiserver
> ## 30_qidrive (Currently "40_qivault")
> ## 40_qiapps (Currently "60_qiapps")

### Assistant
> Locked.
> 
> This is the **approved top spine** now:
> 
> ```markdown id="xz3amx"
> # qilabs
> 
> ## 00_qilabs.workspace
> 
> ## 10_qispark
> 
> ## 20_qiserver
> 
> ## 30_qidrive
> <!-- currently: 40_qivault -->
> 
> ## 40_qiapps
> <!-- currently: 60_qiapps -->
> ```
> 
> ## Translation rule
> 
> | Approved name | Current / legacy name | Meaning |
> |---|---|---|
> | `00_qilabs.workspace` | same | workspace control/root map |
> | `10_qispark` | same | Markdown KB/docs/governance |
> | `20_qiserver` | same | runtime/services/data |
> | `30_qidrive` | `40_qivault` | drive/storage/evidence layer |
> | `40_qiapps` | `60_qiapps` | app specs/apps layer |
> 
> And yes — **`qidrive` is better than `qivault`** for the top-level name. “Vault” sounds like only secrets/evidence. “Drive” is broader and maps better to storage/mirror/blob layer.

### User
> no this is important qiworkspace is only to store, workspace settings configs, extension, maybe act as the federated level for the "state" the other folder, its not the source of truth, its the workspace setup and quick start and maintence tool kit so lets try and make sure we do not bloat it for no reason and dont gorget to add your .why.name files with just a few lins of context.

### Assistant
> Yes — that correction matters.
> 
> I was still letting `00_qilabs.workspace` act like a hidden governance folder. Wrong. That belongs in **QiSpark**.
> 
> ## Correct role
> 
> ```text
> 00_qilabs.workspace = workspace setup + state pointers + maintenance toolkit
> 10_qispark = source of truth for docs, rules, maps, KB, decisions
> ```
> 
> So `00_qilabs.workspace` should stay **thin**.
> 
> ## Updated slice
> 
> :::writing{variant="standard" id="19482"}
> # qilabs
> 
> ## 00_qilabs.workspace
> ### _root
> - readme.qilabs_workspace.md
> - why.qilabs_workspace.md
> - quickstart.qilabs_workspace.md
> - changelog.qilabs_workspace.md
> 
> ### 01_settings
> - settings.workspace.code.md
> - settings.workspace.obsidian.md
> - settings.workspace.git.md
> - settings.workspace.env.example.md
> - why.workspace_settings.md
> 
> ### 02_configs
> - config.workspace.paths.json
> - config.workspace.roots.json
> - config.workspace.extensions.json
> - config.workspace.tasks.json
> - why.workspace_configs.md
> 
> ### 03_extensions
> - extensions.workspace_recommended.md
> - extensions.obsidian_plugins.md
> - extensions.vscode_plugins.md
> - why.workspace_extensions.md
> 
> ### 04_state
> - state.workspace_index.md
> - state.workspace_active_root.md
> - state.workspace_open_threads.md
> - state.workspace_last_known.md
> - why.workspace_state.md
> 
> ### 05_maintenance
> - toolkit.workspace_maintenance.md
> - checklist.workspace_health.md
> - checklist.workspace_sync.md
> - checklist.workspace_backup.md
> - why.workspace_maintenance.md
> 
> ### 06_bootstrap
> - bootstrap.workspace_setup.md
> - bootstrap.workspace_restore.md
> - bootstrap.workspace_new_machine.md
> - why.workspace_bootstrap.md
> :::
> 
> ## What does **not** belong there
> 
> ```text
> rules.qilabs_source_truth.md
> map.qilabs_boundaries.md
> adr.qispark_structure.md
> standards.qispark_docs.md
> registry.qispark_pages.csv
> kb.qispark_context.md
> ```
> 
> Those move to:
> 
> ```text
> 10_qispark
> ```
> 
> ## `.why.name.md` rule
> 
> Every major folder gets a tiny context file:
> 
> ```text
> why.qilabs_workspace.md
> why.workspace_settings.md
> why.workspace_configs.md
> why.workspace_state.md
> why.qispark.md
> why.qiserver.md
> why.qidrive.md
> why.qiapps.md
> ```
> 
> Each one should be **3–7 lines max**:
> 
> ```markdown
> # Why this exists
> 
> This folder stores workspace setup, configs, extensions, and quick-start tooling.
> 
> It does not store canonical documentation, evidence, runtime code, or app specs.
> 
> Canonical docs live in `10_qispark`.
> ```
> 
> That’s the move: **workspace is the launchpad, not the library.**

### User
> yes and to help you finish up the correction to this tree here is the current tree after i made some udpates now we need to grab or merge whats here ```

> 00_QiLabs.workspace/

> ├── .github

> │   ├── ISSUE_TEMPLATE

> │   │   ├── architecture_change.md

> │   │   ├── bug_report.md

> │   │   └── feature_request.md

> │   ├── workflows

> │   │   ├── ci.yml

> │   │   ├── docs.yml

> │   │   ├── lint.yml

> │   │   ├── migrations.yml

> │   │   ├── release.yml

> │   │   └── test.yml

> │   ├── CODEOWNERS

> │   └── pull_request_template.md

> ├── .qios

> │   └── docs_compiler.config.json

> ├── .vscode

> │   └── settings.json

> ├── 20_manifests

> │   ├── apps.manifest.json

> │   ├── connectors.manifest.json

> │   ├── domains.manifest.json

> │   ├── repos.manifest.json

> │   ├── services.manifest.json

> │   └── storage.manifest.json

> ├── 30_configs

> │   ├── .editorconfig

> │   ├── .gitignore

> │   ├── QiLabs.code-workspace

> │   └── vscode_settings.json

> ├── 50_scripts

> │   ├── ai

> │   │   ├── agents

> │   │   │   ├── agent_models.py

> │   │   │   └── agent_qios.py

> │   │   ├── memory

> │   │   │   └── memory_store.py

> │   │   ├── prompts

> │   │   │   └── prompt_gina.py

> │   │   └── rag

> │   │       └── rag_core.py

> │   ├── apps

> │   │   ├── calendar

> │   │   │   ├── calendar_create_event.py

> │   │   │   └── calendar_get_upcoming.py

> │   │   ├── mail

> │   │   │   ├── mail_get_recent.py

> │   │   │   └── mail_send.py

> │   │   ├── sms

> │   │   │   └── sms_send.py

> │   │   ├── vault

> │   │   │   ├── vault_append_note.py

> │   │   │   └── vault_create_note.py

> │   │   └── web

> │   │       ├── web_get.py

> │   │       └── web_search.py

> │   ├── core

> │   │   ├── auth

> │   │   │   ├── auth_check.ps1

> │   │   │   └── auth_secrets_check.ps1

> │   │   ├── docs

> │   │   │   └── usage.md

> │   │   ├── modules

> │   │   │   └── module_app_create.py

> │   │   ├── check_ffmpeg.py

> │   │   ├── core_base.py

> │   │   ├── core_qi_codex.py

> │   │   ├── core_qios_local.py

> │   │   └── ffmpeg_utils.py

> │   ├── db

> │   │   ├── db-migrate.ps1

> │   │   ├── db-reset.ps1

> │   │   ├── db-seed.ps1

> │   │   ├── db-start.ps1

> │   │   └── db-stop.ps1

> │   ├── deploy

> │   │   ├── scripts

> │   │   │   ├── deploy_all.ps1

> │   │   │   ├── deploy_critical.ps1

> │   │   │   └── deploy_git_autopush.ahk

> │   │   ├── sync

> │   │   │   ├── git_manifest.json

> │   │   │   ├── git_pusher.log

> │   │   │   ├── README.md

> │   │   │   ├── sync_dev_gdrive.py

> │   │   │   ├── sync_gdrive.ps1

> │   │   │   ├── sync_git_push.py

> │   │   │   ├── sync_index_content.ts

> │   │   │   ├── sync_lfs_disable.ps1

> │   │   │   └── sync_lfs_enable.ps1

> │   │   ├── workers

> │   │   │   ├── worker_deploy_all.ps1

> │   │   │   ├── worker_deploy.ps1

> │   │   │   └── worker_urls_get.ps1

> │   │   └── build_qios_chronicle.py

> │   ├── dev

> │   │   ├── check-env.ps1

> │   │   ├── check-env.sh

> │   │   ├── dev.ps1

> │   │   ├── dev.sh

> │   │   ├── start-ai-api.ps1

> │   │   ├── start-app-api.ps1

> │   │   ├── start-local-agent.ps1

> │   │   ├── start-local-agent.sh

> │   │   └── start-workers.ps1

> │   ├── flow

> │   │   ├── core

> │   │   │   └── setup_antigravity.py

> │   │   ├── health

> │   │   │   ├── health_check_status.py

> │   │   │   ├── health_check_worker_status.py

> │   │   │   └── health_check_workers.py

> │   │   ├── jobs

> │   │   │   └── job_runner.py

> │   │   ├── logs

> │   │   │   ├── log_build_error.ps1

> │   │   │   └── log_error_supabase.py

> │   │   ├── movers

> │   │   │   └── move_chatgpt_audio_registry.py

> │   │   ├── runners

> │   │   │   ├── run_agent_command.py

> │   │   │   ├── run_agent_service.py

> │   │   │   └── run_worker.py

> │   │   ├── schedulers

> │   │   │   ├── sched_install.ps1

> │   │   │   ├── sched_queue_load.py

> │   │   │   └── sched_windows_task.xml

> │   │   ├── step1_combine.py

> │   │   ├── step1_fast_combine.py

> │   │   ├── step2_convert.py

> │   │   ├── step2_flip.py

> │   │   ├── step3_enhance.py

> │   │   └── step3_filter.py

> │   ├── inbox

> │   │   ├── audit_inbox.ts

> │   │   ├── dedup_detect.ts

> │   │   ├── fix_inbox_names.ts

> │   │   ├── merge_plan.ts

> │   │   ├── normalize_inbox.ts

> │   │   └── run_inbox.ts

> │   ├── index

> │   │   ├── builders

> │   │   │   ├── index_build.ps1

> │   │   │   ├── index_immigration_example.py

> │   │   │   ├── index_timeline_713_build.js

> │   │   │   ├── index_timeline_build.js

> │   │   │   └── index_timeline_json_build.js

> │   │   ├── directory

> │   │   │   ├── compile

> │   │   │   │   ├── dir_code_compile_review.py

> │   │   │   │   ├── dir_timeline_load.js

> │   │   │   │   └── dir_tree_compile.py

> │   │   │   ├── create

> │   │   │   │   ├── dir_app_create.py

> │   │   │   │   ├── dir_canvas_create.py

> │   │   │   │   ├── dir_canvas_directory_create.py

> │   │   │   │   ├── dir_cloudflare_md_create.py

> │   │   │   │   ├── dir_node_new.bat

> │   │   │   │   ├── dir_registry_trash_summarize.py

> │   │   │   │   └── dir_stubs_create.py

> │   │   │   ├── flatten

> │   │   │   │   ├── dir_flatten.py

> │   │   │   │   └── dir_folders_ultra_clean.py

> │   │   │   ├── indices

> │   │   │   │   └── dir_indexes_generate.py

> │   │   │   └── maps

> │   │   │       ├── dir_map.py

> │   │   │       └── dir_slugs_map.py

> │   │   └── registry

> │   │       ├── reg_files_build.py

> │   │       └── reg_files_generate.ps1

> │   ├── ingest

> │   │   ├── audio

> │   │   │   └── audio_transcribe.py

> │   │   ├── files

> │   │   │   ├── file_md_body_move.py

> │   │   │   ├── file_realm_list.py

> │   │   │   └── file_scan_fs.py

> │   │   ├── inbox

> │   │   │   ├── inbox_audit.ts

> │   │   │   ├── inbox_downloads_rename.py

> │   │   │   ├── inbox_flatten.ps1

> │   │   │   ├── inbox_merge_plan.ts

> │   │   │   ├── inbox_names_fix.ts

> │   │   │   └── inbox_run.ts

> │   │   └── video

> │   │       ├── video_media_tree_merge.py

> │   │       └── video_mkvs_merge.py

> │   ├── pdf

> │   │   ├── process_inbox_pdfs.ts

> │   │   ├── process_pdf.ts

> │   │   └── validate_pdfs.ts

> │   ├── process

> │   │   ├── clean

> │   │   │   ├── clean_analysis.ps1

> │   │   │   ├── clean_app_roots.py

> │   │   │   ├── clean_comprehensive.ps1

> │   │   │   ├── clean_continue.ps1

> │   │   │   ├── clean_dedup_detect.ts

> │   │   │   ├── clean_duplicates_find.ps1

> │   │   │   ├── clean_duplicates_find.py

> │   │   │   ├── clean_duplicates_move.ps1

> │   │   │   ├── clean_housekeeper_run.py

> │   │   │   ├── clean_inbox_organize.py

> │   │   │   ├── clean_intake_trash.py

> │   │   │   ├── clean_qi_prefixes.py

> │   │   │   ├── clean_storage_bloat.py

> │   │   │   ├── clean_stubs_detect.py

> │   │   │   └── clean_violations.py

> │   │   ├── convert

> │   │   │   ├── csv

> │   │   │   │   ├── csv_convert.js

> │   │   │   │   ├── csv_convert.ps1

> │   │   │   │   ├── csv_md_check.py

> │   │   │   │   ├── csv_to_md.py

> │   │   │   │   ├── README.md

> │   │   │   │   └── USAGE.md

> │   │   │   ├── folders

> │   │   │   │   ├── folder_flatten_finish.ps1

> │   │   │   │   ├── folder_flatten_organize.ps1

> │   │   │   │   └── folder_flatten.py

> │   │   │   ├── json

> │   │   │   │   └── json_kb_generate.py

> │   │   │   ├── text

> │   │   │   │   └── text_extract.py

> │   │   │   ├── video

> │   │   │   │   └── video_mkv_enhance.py

> │   │   │   ├── zip

> │   │   │   │   └── zip_downloads_extract.py

> │   │   │   ├── convert_code_extract.py

> │   │   │   └── convert_errors_to_markdown.py

> │   │   ├── docs

> │   │   │   └── _Convert_csv_to_md.md

> │   │   ├── normalize

> │   │   │   ├── norm_files_sort.py

> │   │   │   ├── norm_inbox.ts

> │   │   │   └── norm_spaces_fix.py

> │   │   ├── pdf

> │   │   │   ├── pdf_inbox_process.ts

> │   │   │   ├── pdf_process.ts

> │   │   │   └── pdf_validate.ts

> │   │   ├── validate

> │   │   │   ├── valid_cloud.ps1

> │   │   │   ├── valid_compliance_check.py

> │   │   │   ├── valid_csv_md_compare.py

> │   │   │   ├── valid_csv_search.py

> │   │   │   ├── valid_db_examine.py

> │   │   │   ├── valid_drive_compare.py

> │   │   │   ├── valid_file_error_context.py

> │   │   │   ├── valid_housekeeping.ps1

> │   │   │   ├── valid_linter_run.py

> │   │   │   ├── valid_linter.py

> │   │   │   ├── valid_local.ps1

> │   │   │   └── valid_md_check.py

> │   │   ├── process_inbox_pdfs.ts

> │   │   └── safe_reorg.py

> │   ├── repo

> │   │   ├── examples

> │   │   ├── output

> │   │   ├── sys_docs_compiler_tool

> │   │   │   ├── .qios

> │   │   │   ├── scripts

> │   │   │   │   └── docs_build

> │   │   │   └── sys_docs_compiler

> │   │   ├── tests

> │   │   ├── enforce-structure.py

> │   │   ├── git_sync.py

> │   │   ├── lint-tree.py

> │   │   ├── print-tree.py

> │   │   ├── recursive_git_sync.py

> │   │   └── validate-paths.py

> │   ├── rules

> │   │   ├── audit_repo_rules.ts

> │   │   └── fix_repo_rules.ts

> │   ├── structure

> │   ├── sync

> │   │   ├── index_content.ts

> │   │   └── windows_task_scheduler.xml

> │   ├── tools

> │   │   ├── debug

> │   │   │   └── debug_maps.py

> │   │   ├── frontmatter

> │   │   │   ├── frontmatter_add.py

> │   │   │   ├── frontmatter_enforce.py

> │   │   │   ├── frontmatter_utils.py

> │   │   │   └── frontmatter_validate.ts

> │   │   ├── maps

> │   │   │   ├── map_3d_mindmap_run.bat

> │   │   │   ├── map_3d_real_run.bat

> │   │   │   └── map_3d_simple_run.bat

> │   │   ├── misc

> │   │   │   ├── scripts_rename_manifest.json

> │   │   │   └── scripts_rename_pass1.py

> │   │   ├── search

> │   │   │   └── search_processed_docs.py

> │   │   ├── ai_video_filter.py

> │   │   ├── backup_qidata.ps1

> │   │   ├── batch_processor.py

> │   │   ├── check_processed.py

> │   │   ├── enforce_fm.py

> │   │   ├── find_failed.py

> │   │   ├── flatten_enhance.py

> │   │   ├── flatten_trade.py

> │   │   ├── local_processor.py

> │   │   ├── pipeline_processor.py

> │   │   ├── repair_repo.ps1

> │   │   ├── repair_repo.sh

> │   │   ├── restore_qidata.ps1

> │   │   ├── test_abbreviations.py

> │   │   ├── test_gina_chat_simple.ps1

> │   │   ├── test_pipeline.ps1

> │   │   ├── tools_manifest.json

> │   │   ├── tree_snapshot.ps1

> │   │   ├── tree_snapshot.sh

> │   │   ├── unblock_all.bat

> │   │   ├── verify_env.ps1

> │   │   └── verify_env.sh

> │   ├── audit_structure.ps1

> │   ├── bootstrap_workspace.ps1

> │   ├── check_root_clean.ps1

> │   ├── export_file_inventory.ps1

> │   └── generate_tree.ps1

> ├── 99_quarantine

> │   ├── 70_templates

> │   │   ├── ADR_template.md

> │   │   ├── module_index_template.md

> │   │   ├── README_template.md

> │   │   └── runbook_template.md

> │   ├── json

> │   │   ├── eos_frontmatter.schema.json

> │   │   ├── eos-frontmatter-mapping.json

> │   │   ├── frontmatter.schema.json

> │   │   ├── git_manifest.json

> │   │   ├── mapping.json

> │   │   ├── QiRealms_seed.json

> │   │   ├── QiTagClasses_schema.json

> │   │   ├── QiTags_seed.json

> │   │   ├── repo_naming_policy.json

> │   │   └── systemInfoCMD.json

> │   ├── rules

> │   │   ├── audit_repo_rules.ts

> │   │   ├── fix_repo_rules.ts

> │   │   ├── repoRules.ts (const RepoRulesSchema, type RepoRules, func loadRepoRules)

> │   │   └── rulesRegistry.ts (type Severity, iface RepoRule, const RulesRegistry)

> │   └── yaml

> │       ├── csv_to_md_mappings.yaml

> │       ├── fs_scan_config.yaml

> │       ├── housekeeping.yaml

> │       ├── qi_codex.config.yaml

> │       ├── qi_prefix_map.yaml

> │       ├── qicompiler_config.yaml

> │       ├── qione_rag_routes.yaml

> │       ├── slugs_mapping.yaml

> │       └── tree_compiler_config.yaml

> ├── .env

> ├── .env.example

> ├── .gitkeep

> ├── .gitmodules

> ├── eslint.config.mjs

> ├── justfile

> ├── LICENSE

> ├── postcss.config.js

> ├── QiLabs.code-workspace

> ├── README.md

> ├── repo.rules.json

> ├── tailwind.config.ts

> ├── tsconfig.root.json

> └── vizvibe.mmd

> ```

> 
> tell me what files you want to see.

### Assistant
> Yes. This tree explains the mess.
> 
> **The main correction:** `00_QiLabs.workspace` currently contains way too much actual engine work. Most of `50_scripts` is not “workspace setup.” It belongs under `20_qiserver`, especially:
> 
> ```text
> ai
> apps
> db
> deploy
> flow
> ingest
> pdf
> process
> tools
> ```
> 
> Workspace should keep **repo/workspace setup, manifests, configs, bootstrap, light maintenance** — not the whole machine room.
> 
> ## Files I want to see first
> 
> Send these in this order. Don’t dump everything.
> 
> ### Batch 1 — workspace identity / current intent
> 
> ```text
> 00_QiLabs.workspace/README.md
> 00_QiLabs.workspace/repo.rules.json
> 00_QiLabs.workspace/.qios/docs_compiler.config.json
> 00_QiLabs.workspace/20_manifests/repos.manifest.json
> 00_QiLabs.workspace/20_manifests/services.manifest.json
> 00_QiLabs.workspace/20_manifests/apps.manifest.json
> 00_QiLabs.workspace/20_manifests/storage.manifest.json
> ```
> 
> Why: these tell us what the repo currently thinks it is.
> 
> ---
> 
> ### Batch 2 — workspace configs
> 
> ```text
> 00_QiLabs.workspace/30_configs/QiLabs.code-workspace
> 00_QiLabs.workspace/30_configs/vscode_settings.json
> 00_QiLabs.workspace/30_configs/.editorconfig
> 00_QiLabs.workspace/QiLabs.code-workspace
> 00_QiLabs.workspace/tsconfig.root.json
> 00_QiLabs.workspace/justfile
> ```
> 
> Why: these decide what actually needs to stay in `00_qilabs.workspace`.
> 
> ---
> 
> ### Batch 3 — script routing / what needs to move
> 
> ```text
> 00_QiLabs.workspace/50_scripts/repo/validate-paths.py
> 00_QiLabs.workspace/50_scripts/repo/lint-tree.py
> 00_QiLabs.workspace/50_scripts/repo/enforce-structure.py
> 00_QiLabs.workspace/50_scripts/repo/print-tree.py
> 00_QiLabs.workspace/50_scripts/export_file_inventory.ps1
> 00_QiLabs.workspace/50_scripts/generate_tree.ps1
> 00_QiLabs.workspace/50_scripts/check_root_clean.ps1
> 00_QiLabs.workspace/50_scripts/bootstrap_workspace.ps1
> ```
> 
> Why: these are the boundary tools. Some stay workspace. Some become server maintenance.
> 
> ---
> 
> ### Batch 4 — quarantine salvage
> 
> ```text
> 00_QiLabs.workspace/99_quarantine/json/frontmatter.schema.json
> 00_QiLabs.workspace/99_quarantine/json/repo_naming_policy.json
> 00_QiLabs.workspace/99_quarantine/json/mapping.json
> 00_QiLabs.workspace/99_quarantine/yaml/tree_compiler_config.yaml
> 00_QiLabs.workspace/99_quarantine/yaml/qi_prefix_map.yaml
> 00_QiLabs.workspace/99_quarantine/yaml/qicompiler_config.yaml
> 00_QiLabs.workspace/99_quarantine/70_templates/ADR_template.md
> 00_QiLabs.workspace/99_quarantine/70_templates/runbook_template.md
> ```
> 
> Why: quarantine probably contains the best raw material for QiSpark standards/templates.
> 
> ---
> 
> ## My immediate diagnosis
> 
> ### Keep in `00_qilabs.workspace`
> 
> ```text
> .github
> .qios
> .vscode
> 20_manifests
> 30_configs
> bootstrap_workspace.ps1
> check_root_clean.ps1
> generate_tree.ps1
> export_file_inventory.ps1
> QiLabs.code-workspace
> repo.rules.json
> justfile
> ```
> 
> ### Move out of workspace
> 
> Most of this should move to `20_qiserver`:
> 
> ```text
> 50_scripts/ai
> 50_scripts/apps
> 50_scripts/db
> 50_scripts/deploy
> 50_scripts/dev
> 50_scripts/flow
> 50_scripts/inbox
> 50_scripts/ingest
> 50_scripts/pdf
> 50_scripts/process
> 50_scripts/sync
> 50_scripts/tools
> ```
> 
> ### Split `99_quarantine`
> 
> Likely destinations:
> 
> ```text
> templates → 10_qispark
> schemas → 10_qispark or 20_qiserver depending use
> rules → 10_qispark if docs/governance, 20_qiserver if executable
> yaml configs → probably 00_workspace or 20_qiserver
> ```
> 
> ## The file I want first-first
> 
> Start with:
> 
> ```text
> 00_QiLabs.workspace/README.md
> ```
> 
> Then:
> 
> ```text
> 00_QiLabs.workspace/repo.rules.json
> ```
> 
> Those two will tell us whether we’re cleaning against the intended system or against old debris.

### Assistant
> I’ve got enough to make the first real call: your current workspace is mostly scaffolding, but the manifests are empty and the naming rules still permit old generic exceptions. I’m checking the config files now so the next tree doesn’t fight your actual tooling.

### Assistant
> Yep — this batch tells us the correction path.
> 
> ## What I see
> 
> ### 1. `00_QiLabs.workspace` is currently mostly a **toolbox shell**
> 
> The README is basically just a title, so there is no strong identity document yet. That means we are free to define it cleanly now instead of fighting old doctrine. fileciteturn0file1
> 
> ### 2. The manifests exist, but they are empty
> 
> These are currently placeholders:
> 
> ```text id="ksjqoh"
> apps.manifest.json
> connectors.manifest.json
> domains.manifest.json
> repos.manifest.json
> services.manifest.json
> storage.manifest.json
> ```
> 
> That is actually good. It means they can stay in `00_qilabs.workspace/20_manifests`, but they need real schema later. Right now they are just `{}`. fileciteturn0file3 fileciteturn0file4 fileciteturn0file5 fileciteturn0file6 fileciteturn0file7 fileciteturn0file8
> 
> ### 3. `repo.rules.json` is useful, but partially outdated
> 
> It already enforces the kind of naming you want:
> 
> ```text id="qdaufv"
> no spaces
> lowercase filenames
> allowed chars: a-z, 0-9, underscore, dash, dot
> max base length 50
> prefer underscore
> ```
> 
> But it still allows generic script exceptions:
> 
> ```text id="gq8kwk"
> README.md
> USAGE.md
> ```
> 
> That conflicts with your new rule. We should tighten that to allow generic files only when forced by tooling, otherwise use contextual names like `readme.qiserver_root.md` or `usage.qispark_nav.md`. fileciteturn0file0
> 
> ### 4. `docs_compiler.config.json` is close, but it needs the new root names
> 
> It already does some smart things:
> 
> ```text id="klkenh"
> preserve_hierarchy: true
> generate_index: true
> normalize_generated_markdown: true
> fix_source_markdown: false
> ```
> 
> That is good. It means the compiler can generate indexes without mutating source docs. But it still excludes older paths like `00_QiAccess/docs` and `01_Q/docs`, so we need to update it around the approved top spine. fileciteturn0file2
> 
> ---
> 
> # Immediate correction
> 
> The current tree says:
> 
> ```text id="me70ij"
> 00_QiLabs.workspace/
>   50_scripts/
>     ai/
>     apps/
>     db/
>     deploy/
>     dev/
>     flow/
>     inbox/
>     ingest/
>     pdf/
>     process/
>     tools/
> ```
> 
> That is the big issue.
> 
> Most of that is **not workspace setup**.
> 
> It should move conceptually to:
> 
> ```text id="ufvxw8"
> 20_qiserver/
> ```
> 
> Because it is runtime, automation, processing, ingest, deployment, AI, or service tooling.
> 
> ---
> 
> # Corrected merge model
> 
> ## Approved top
> 
> ```markdown id="r59h10"
> # qilabs
> 
> ## 00_qilabs.workspace
> ## 10_qispark
> ## 20_qiserver
> ## 30_qidrive
> <!-- currently: 40_qivault -->
> ## 40_qiapps
> <!-- currently: 60_qiapps -->
> ```
> 
> ---
> 
> # Updated `00_qilabs.workspace`
> 
> This is the lean version based on your actual uploaded tree.
> 
> ```markdown id="x8of7d"
> ## 00_qilabs.workspace
> 
> ### _root
> - readme.qilabs_workspace.md
> - why.qilabs_workspace.md
> - quickstart.qilabs_workspace.md
> - changelog.qilabs_workspace.md
> - qlabs.code_workspace
> - justfile
> 
> ### .github
> - codeowners.github.md
> - template.github_pull_request.md
> - why.github.md
> 
> #### issue_template
> - template.github_issue_architecture_change.md
> - template.github_issue_bug_report.md
> - template.github_issue_feature_request.md
> 
> #### workflows
> - workflow.github_ci.yml
> - workflow.github_docs.yml
> - workflow.github_lint.yml
> - workflow.github_migrations.yml
> - workflow.github_release.yml
> - workflow.github_test.yml
> 
> ### .qios
> - config.qios_docs_compiler.json
> - why.qios.md
> 
> ### .vscode
> - settings.vscode_workspace.json
> - why.vscode.md
> 
> ### 20_manifests
> - manifest.qilabs_apps.json
> - manifest.qilabs_connectors.json
> - manifest.qilabs_domains.json
> - manifest.qilabs_repos.json
> - manifest.qilabs_services.json
> - manifest.qilabs_storage.json
> - why.qilabs_manifests.md
> 
> ### 30_configs
> - config.workspace_editor.editorconfig
> - config.workspace_gitignore.gitignore
> - config.workspace_vscode.json
> - config.workspace_typescript.json
> - config.workspace_eslint.mjs
> - config.workspace_tailwind.ts
> - config.workspace_postcss.js
> - config.workspace_repo_rules.json
> - why.workspace_configs.md
> 
> ### 40_state
> - state.workspace_active.md
> - state.workspace_last_known.md
> - state.workspace_open_threads.md
> - why.workspace_state.md
> 
> ### 50_toolkit
> - bootstrap.workspace.ps1
> - check.workspace_root_clean.ps1
> - export.workspace_file_inventory.ps1
> - generate.workspace_tree.ps1
> - why.workspace_toolkit.md
> 
> ### 90_quarantine
> - quarantine.workspace_index.md
> - why.workspace_quarantine.md
> ```
> 
> ## Why this is better
> 
> `00_qilabs.workspace` now only holds:
> 
> ```text id="qn3fgd"
> workspace setup
> workspace configs
> manifests
> GitHub workflows
> editor settings
> bootstrap scripts
> light maintenance scripts
> state pointers
> quarantine holding area
> ```
> 
> It does **not** hold:
> 
> ```text id="lje2l8"
> AI runtime
> memory engine
> database scripts
> ingest scripts
> PDF processing
> deployment services
> app scripts
> vault scripts
> business logic
> docs KB
> ```
> 
> That stuff moves.
> 
> ---
> 
> # Where the current `50_scripts` should go
> 
> ## Move to `20_qiserver`
> 
> ```text id="xcnrq2"
> 50_scripts/ai        → 20_qiserver/30_services/qimemory + qillm
> 50_scripts/apps      → 20_qiserver/40_apps_runtime
> 50_scripts/db        → 20_qiserver/20_data
> 50_scripts/deploy    → 20_qiserver/50_deploy
> 50_scripts/dev       → 20_qiserver/10_runtime/dev
> 50_scripts/flow      → 20_qiserver/60_jobs
> 50_scripts/inbox     → 20_qiserver/30_services/qimemory/inbox
> 50_scripts/ingest    → 20_qiserver/30_services/qimemory/ingest
> 50_scripts/pdf       → 20_qiserver/30_services/qimemory/pdf
> 50_scripts/process   → 20_qiserver/30_services/qimemory/process
> 50_scripts/sync      → 20_qiserver/60_jobs/sync
> 50_scripts/tools     → split: workspace tools vs qiserver tools
> ```
> 
> ## Keep in `00_qilabs.workspace/50_toolkit`
> 
> Only these kinds of scripts stay:
> 
> ```text id="8oupm9"
> bootstrap_workspace.ps1
> check_root_clean.ps1
> export_file_inventory.ps1
> generate_tree.ps1
> tree_snapshot.ps1 / .sh
> verify_env.ps1 / .sh
> repair_repo.ps1 / .sh maybe
> ```
> 
> The rule is simple:
> 
> ```text id="cm8j7a"
> If it manages the workspace, it stays.
> If it runs the system, it moves to qiserver.
> ```
> 
> ---
> 
> # What I want to see next
> 
> Send these next — this is the highest leverage batch.
> 
> ## Batch 2 — structure enforcement scripts
> 
> ```text id="d6yjnp"
> 50_scripts/repo/enforce-structure.py
> 50_scripts/repo/validate-paths.py
> 50_scripts/repo/lint-tree.py
> 50_scripts/repo/print-tree.py
> 50_scripts/audit_structure.ps1
> 50_scripts/check_root_clean.ps1
> 50_scripts/generate_tree.ps1
> 50_scripts/bootstrap_workspace.ps1
> ```
> 
> These decide what needs to be rewritten for the approved top spine.
> 
> ## Batch 3 — quarantine rules/templates
> 
> ```text id="d0px8f"
> 99_quarantine/json/frontmatter.schema.json
> 99_quarantine/json/repo_naming_policy.json
> 99_quarantine/json/mapping.json
> 99_quarantine/yaml/tree_compiler_config.yaml
> 99_quarantine/yaml/qi_prefix_map.yaml
> 99_quarantine/yaml/qicompiler_config.yaml
> 99_quarantine/70_templates/ADR_template.md
> 99_quarantine/70_templates/runbook_template.md
> ```
> 
> This is where we salvage the real standards into `10_qispark`.
> 
> ## Batch 4 — if available, the current top trees for the other roots
> 
> ```text id="ex66l9"
> 10_QiSpark/
> 20_QiServer/
> 40_QiVault/
> 60_QiApps/
> ```
> 
> Even just `tree -L 3` is enough. I don’t need every file yet.
> 
> ---
> 
> # The uncomfortable truth
> 
> Your current `00_QiLabs.workspace` is not a workspace folder. It is a **workspace folder wearing a server backpack**.
> 
> We fix that by turning it into a lean launchpad and moving the engine into `20_qiserver`.
> 
> That is the right correction.

### User
> i dont want placeholders unless they absolutley provide something dier to my situation othersies im burning up lujo

### Assistant
> Absolutely. **Kill the placeholders.**
> 
> New rule:
> 
> ```text
> No placeholder unless it prevents confusion, protects data, or directly supports current work.
> ```
> 
> A file must earn its existence by doing one of these:
> 
> ```text
> 1. tells you what this folder is for
> 2. tells you what does NOT belong here
> 3. stores real config/state
> 4. runs real maintenance
> 5. prevents future breakage
> 6. maps an active migration/rename
> ```
> 
> Everything else is bloat.
> 
> ## So for `00_qilabs.workspace`, remove/avoid fake stuff like:
> 
> ```text
> state.workspace_open_threads.md
> state.workspace_last_known.md
> quarantine.workspace_index.md
> why.workspace_state.md
> manifest.qilabs_apps.json   if empty and unused
> manifest.qilabs_services.json if empty and unused
> ```
> 
> Empty `{}` manifests are not useful unless a script currently reads them. Otherwise they’re just little JSON ghosts haunting the repo.
> 
> ## Keep only this lean version
> 
> ```markdown
> # qilabs
> 
> ## 00_qilabs.workspace
> ### _root
> - readme.qilabs_workspace.md
> - why.qilabs_workspace.md
> - quickstart.qilabs_workspace.md
> - changelog.qilabs_workspace.md
> - qilabs.code-workspace
> - justfile
> 
> ### .github
> - CODEOWNERS
> - pull_request_template.md
> 
> #### ISSUE_TEMPLATE
> - architecture_change.md
> - bug_report.md
> - feature_request.md
> 
> #### workflows
> - ci.yml
> - docs.yml
> - lint.yml
> - migrations.yml
> - release.yml
> - test.yml
> 
> ### .qios
> - docs_compiler.config.json
> 
> ### .vscode
> - settings.json
> 
> ### 20_manifests
> - only_keep_if_used_by_scripts.json
> 
> ### 30_configs
> - .editorconfig
> - .gitignore
> - repo.rules.json
> - tsconfig.root.json
> - eslint.config.mjs
> - tailwind.config.ts
> - postcss.config.js
> 
> ### 50_toolkit
> - bootstrap_workspace.ps1
> - check_root_clean.ps1
> - export_file_inventory.ps1
> - generate_tree.ps1
> 
> ### 99_quarantine
> - only_until_sorted
> ```
> 
> ## `.why` rule, tightened
> 
> Only add `.why` files at **major boundary points**, not every folder.
> 
> Keep:
> 
> ```text
> why.qilabs_workspace.md
> why.qispark.md
> why.qiserver.md
> why.qidrive.md
> why.qiapps.md
> ```
> 
> Maybe:
> 
> ```text
> why.workspace_toolkit.md
> ```
> 
> Do **not** create a `.why` file for every tiny subfolder. That becomes documentation glitter.
> 
> ## Real move
> 
> For the current cleanup, I’d mark every file/folder as one of three actions:
> 
> ```text
> KEEP
> MOVE
> DELETE / QUARANTINE
> ```
> 
> No “someday placeholder” category. That category is where time goes to die.

### User
> ok, are you sure that the final final, ok, now that you are getting the hang of it you ready to try to do qispark all by your self. lets see that one

### Assistant
> Yes. I’m ready — but no, I’m not calling anything “final final” until it survives your eyes and a real folder pass. This version is my best QiSpark-only draft with the new rules: lean, useful, no empty theater.

### Assistant
> Yep. Here’s my **QiSpark-only attempt**.
> 
> This is not bloated with fake “maybe someday” files. It assumes:
> 
> ```text id="r1dbv5"
> 10_qispark = Markdown knowledge base
> not runtime
> not evidence storage
> not Cloudflare
> not workspace config
> not app code
> ```
> 
> :::writing{variant="standard" id="51328"}
> ---
> title: QiSpark Tree
> section: qilabs/10_qispark/01_nav
> access_level: L1
> visibility: private
> ai_ingest: true
> status: draft
> last_updated: 2026-06-20
> mindmap-plugin: basic
> ---
> 
> # 10_qispark
> 
> ## 00_root
> - readme.qispark_root.md
> - why.qispark.md
> - codex.qispark_ai.md
> - changelog.qispark.md
> 
> ## 01_nav
> - why.qispark_nav.md
> - map.qispark_nav.md
>   - public_nav
>   - private_nav
>   - kb_nav
>   - project_nav
>   - archive_nav
> - map.qispark_tree.md
>   - current_tree
>   - target_tree
>   - move_map
>   - rename_map
> - registry.qispark_nav.csv
> - registry.qispark_routes.csv
> - audit.qispark_nav.md
>   - missing_pages
>   - bad_names
>   - duplicate_nodes
>   - stale_routes
>   - empty_placeholders
> 
> ## 10_start
> - guide.qispark_start.md
>   - what_this_is
>   - how_to_use_it
>   - what_lives_here
>   - what_does_not_live_here
>   - current_state
>   - next_moves
> 
> ## 20_core
> - why.qispark_kb.md
> - kb.qispark_context.md
>   - qispark
>   - qilabs
>   - qiserver
>   - qidrive
>   - qiapps
>   - terms
>   - boundaries
> - kb.qispark_current_state.md
>   - locked
>   - changed
>   - still_fluid
>   - parked
> - kb.qispark_source_map.md
>   - what_counts_as_truth
>   - what_is_reference_only
>   - what_belongs_in_qidrive
>   - what_belongs_in_qiserver
>   - what_belongs_in_qiapps
> - notes.qispark_working.md
>   - active_thoughts
>   - rough_models
>   - questions
>   - not_canonical
> 
> ## 30_life
> - life.qispark_context.md
>   - operating_rules
>   - priorities
>   - constraints
>   - capacity
>   - routines
>   - energy
> - life.qispark_plan.md
>   - current_plan
>   - weekly_map
>   - next_moves
>   - parked_threads
> - life.qispark_decisions.md
>   - tradeoffs
>   - commitments
>   - reversals
>   - lessons
> 
> ## 31_business
> - business.qispark_context.md
>   - positioning
>   - offers
>   - clients
>   - services
>   - ops
> - business.qispark_strategy.md
>   - leverage
>   - revenue
>   - systems
>   - assets
>   - pipeline
> - business.qispark_copy.md
>   - bios
>   - blurbs
>   - service_pages
>   - case_studies
>   - reusable_language
> 
> ## 32_admin_legal
> - admin.qispark_context.md
>   - accounts
>   - forms
>   - benefits
>   - filings
>   - requests
> - legal.qispark_context.md
>   - matters
>   - claims
>   - deadlines
>   - evidence_locations
>   - boundaries
> - legal.qispark_templates.md
>   - letters
>   - notices
>   - disputes
>   - timelines
>   - declarations
> 
> ## 33_people
> - people.qispark_context.md
>   - roles
>   - trust
>   - boundaries
>   - contact_rules
>   - history_notes
> - people.qispark_messages.md
>   - scripts
>   - replies
>   - boundaries
>   - escalation_paths
> 
> ## 34_projects
> - projects.qispark_map.md
>   - active
>   - waiting
>   - paused
>   - archived
> - projects.qispark_specs.md
>   - qios
>   - qilife
>   - qiconnect
>   - qinexus
>   - qidna
>   - qiaccess
>   - client_work
> - projects.qispark_log.md
>   - decisions
>   - changes
>   - blockers
>   - next_steps
> 
> ## 40_qilabs
> - map.qilabs_roots.md
>   - 00_qilabs.workspace
>   - 10_qispark
>   - 20_qiserver
>   - 30_qidrive
>   - 40_qiapps
> - map.qilabs_flow.md
>   - memory
>   - drive
>   - spark
>   - server
>   - apps
>   - publish
> - map.qilabs_boundaries.md
>   - what_goes_where
>   - what_does_not_go_here
>   - current_names
>   - legacy_names
> - adr.qispark_structure.md
>   - why_qispark_is_kb
>   - why_workspace_is_setup_only
>   - why_qiserver_runs_services
>   - why_qidrive_holds_records
>   - why_qiapps_holds_app_specs
>   - why_no_generic_filenames
>   - why_no_empty_placeholders
> 
> ## 50_rules
> - why.qispark_rules.md
> - rules.qispark_core.md
>   - truth
>   - leverage
>   - naming
>   - modularity
>   - ai_use
>   - human_override
> - rules.qispark_boundaries.md
>   - qispark_not_drive
>   - qispark_not_server
>   - qispark_not_apps
>   - docs_not_evidence
>   - maps_not_runtime
> - rules.qispark_docs.md
>   - filenames
>   - folders
>   - markdown
>   - frontmatter
>   - links
>   - archive
> - rules.qispark_access.md
>   - access_level
>   - visibility
>   - ai_ingest
>   - status
>   - sensitive_info
>   - public_private
> 
> ## 60_prompts
> - prompts.qispark_build.md
>   - nav_cleanup
>   - folder_reconcile
>   - docs_generate
>   - frontmatter_audit
> - prompts.qispark_extract.md
>   - extract_nav
>   - extract_decisions
>   - extract_tasks
>   - find_contradictions
>   - check_privacy
> - prompts.qispark_write.md
>   - clean_doc
>   - compress_notes
>   - make_timeline
>   - make_plan
>   - make_message
> 
> ## 70_templates
> - templates.qispark_docs.md
>   - page
>   - section
>   - adr
>   - timeline
>   - message
>   - plan
>   - audit
> 
> ## 80_ops
> - ops.qispark_maintenance.md
>   - add_page
>   - add_section
>   - update_nav
>   - deprecate_page
>   - archive_content
>   - audit
>   - reconcile_names
> - ops.qispark_publish.md
>   - route_check
>   - private_check
>   - broken_links
>   - export_review
>   - handoff_to_qiserver
> 
> ## 90_ref
> - ref.qispark_tables.md
>   - glossary
>   - canonical_names
>   - root_index
>   - route_index
>   - access_values
>   - visibility_values
>   - ingest_values
>   - status_values
> - ref.qispark_legacy_names.md
>   - old_qivault
>   - old_qiapps
>   - old_qicapture
>   - old_cloudflare_root
>   - old_99_system
> 
> ## 91_registry
> - registry.qispark_pages.csv
> - registry.qispark_sections.csv
> - registry.qispark_routes.csv
> - registry.qispark_redirects.csv
> - registry.qispark_access.csv
> - registry.qispark_cleanup.csv
> 
> ## 92_audit
> - audit.qispark_structure.md
>   - nav
>   - routes
>   - names
>   - duplicates
>   - stale
>   - orphaned
> - audit.qispark_privacy.md
>   - public_private
>   - ai_ingest
>   - qidrive_leak
>   - qiserver_leak
>   - app_spec_leak
> 
> ## 98_archive
> - archive.qispark_legacy.md
>   - old_nav
>   - old_names
>   - deprecated_pages
>   - removed_routes
>   - legacy_qios
> :::
> 
> ## My read on this version
> 
> This is the first one that feels close.
> 
> The only section I’m mildly suspicious of is:
> 
> ```text id="y8mnmv"
> 91_registry
> ```
> 
> If those CSVs are not actively used soon, don’t create all of them. Start with only:
> 
> ```text id="ei690e"
> registry.qispark_nav.csv
> registry.qispark_routes.csv
> ```
> 
> Everything else can wait.
> 
> ## Hard rule
> 
> Do **not** create `98_archive` until there is actual legacy material to put there.
> 
> Do **not** create `70_templates` unless you are actually going to use the templates.
> 
> Do **not** create empty registries.
> 
> QiSpark should feel like:
> 
> ```text id="qp3zzl"
> the brain
> the map
> the rules
> the working doctrine
> ```
> 
> Not a decorative office supply cabinet.

### User
> the folders must mirror remember we was inside the workspace folder so that way more or less easy logic for your brai, qhen work sifts, simelin i did lower the cuswsoooooo

### Assistant
> Got it. The mistake was making QiSpark’s internal folders based on content categories first. QiSpark should mirror the approved QiLabs spine first, then put the relevant KB docs under each mirrored root.

### Assistant
> Exactly. That was the missing logic.
> 
> QiSpark should not start with:
> 
> ```text
> life / business / legal / projects / rules
> ```
> 
> That’s useful content, but it breaks the mirror.
> 
> QiSpark should start by mirroring the **approved QiLabs top spine**, because your brain should be able to shift between actual folders and KB folders without remapping reality every damn time.
> 
> So the QiSpark structure should be:
> 
> ```text
> 10_qispark
> ├── 00_qilabs.workspace
> ├── 10_qispark
> ├── 20_qiserver
> ├── 30_qidrive
> └── 40_qiapps
> ```
> 
> Then each section holds the `.md` brain/docs for that root.
> 
> Here’s the corrected QiSpark tree.
> 
> :::writing{variant="standard" id="41682"}
> ---
> title: QiSpark Mirror Tree
> section: qilabs/10_qispark/10_qispark/nav
> access_level: L1
> visibility: private
> ai_ingest: true
> status: draft
> last_updated: 2026-06-20
> mindmap-plugin: basic
> ---
> 
> # 10_qispark
> 
> ## _root
> - readme.qispark_root.md
> - why.qispark.md
> - codex.qispark_ai.md
> - changelog.qispark.md
> 
> ## 00_qilabs.workspace
> ### _root
> - why.qilabs_workspace.md
> - guide.qilabs_workspace_quickstart.md
> - map.qilabs_workspace_current.md
> - map.qilabs_workspace_target.md
> 
> ### cleanup
> - audit.qilabs_workspace_current_tree.md
>   - keep
>   - move
>   - delete
>   - quarantine
> - plan.qilabs_workspace_cleanup.md
>   - scripts_to_move
>   - configs_to_keep
>   - manifests_to_check
>   - quarantine_to_sort
> - rules.qilabs_workspace_scope.md
>   - setup_only
>   - configs
>   - extensions
>   - workspace_toolkit
>   - not_source_truth
>   - not_runtime
>   - not_kb
> 
> ### configs
> - notes.qilabs_workspace_configs.md
>   - github
>   - qios
>   - vscode
>   - manifests
>   - repo_rules
>   - docs_compiler
> 
> ## 10_qispark
> ### _root
> - why.qispark_kb.md
> - guide.qispark_start.md
> - map.qispark_current.md
> - map.qispark_target.md
> 
> ### nav
> - map.qispark_nav.md
>   - mirror_nav
>   - public_nav
>   - private_nav
>   - archive_nav
> - map.qispark_tree.md
>   - current_tree
>   - target_tree
>   - move_map
>   - rename_map
> - registry.qispark_nav.csv
> - registry.qispark_routes.csv
> - audit.qispark_nav.md
>   - bad_names
>   - duplicate_nodes
>   - stale_routes
>   - empty_placeholders
> 
> ### kb
> - kb.qispark_context.md
>   - qilabs
>   - workspace
>   - qispark
>   - qiserver
>   - qidrive
>   - qiapps
>   - terms
>   - boundaries
> - kb.qispark_current_state.md
>   - locked
>   - changed
>   - still_fluid
>   - parked
> - kb.qispark_source_map.md
>   - what_counts
>   - what_does_not_count
>   - where_truth_lives
>   - where_records_live
>   - where_runtime_lives
> 
> ### rules
> - rules.qispark_core.md
>   - truth
>   - leverage
>   - naming
>   - modularity
>   - ai_use
>   - human_override
> - rules.qispark_docs.md
>   - filenames
>   - folders
>   - markdown
>   - frontmatter
>   - links
>   - archive
> - rules.qispark_boundaries.md
>   - qispark_not_workspace
>   - qispark_not_server
>   - qispark_not_drive
>   - qispark_not_apps
>   - docs_not_evidence
>   - maps_not_runtime
> - rules.qispark_access.md
>   - access_level
>   - visibility
>   - ai_ingest
>   - status
>   - sensitive_info
>   - public_private
> 
> ### prompts
> - prompts.qispark_build.md
>   - nav_cleanup
>   - folder_reconcile
>   - docs_generate
>   - frontmatter_audit
> - prompts.qispark_extract.md
>   - extract_nav
>   - extract_decisions
>   - extract_tasks
>   - find_contradictions
>   - check_privacy
> - prompts.qispark_write.md
>   - clean_doc
>   - compress_notes
>   - make_timeline
>   - make_plan
>   - make_message
> 
> ### templates
> - templates.qispark_docs.md
>   - page
>   - section
>   - adr
>   - timeline
>   - message
>   - plan
>   - audit
> 
> ### ops
> - ops.qispark_maintenance.md
>   - add_page
>   - update_nav
>   - deprecate_page
>   - archive_content
>   - audit
>   - reconcile_names
> - ops.qispark_publish.md
>   - route_check
>   - private_check
>   - broken_links
>   - export_review
>   - handoff_to_qiserver
> 
> ### ref
> - ref.qispark_tables.md
>   - glossary
>   - canonical_names
>   - root_index
>   - route_index
>   - access_values
>   - visibility_values
>   - ingest_values
>   - status_values
> - ref.qispark_legacy_names.md
>   - qivault_to_qidrive
>   - qiapps_old_60
>   - qicapture_to_qimemory
>   - cloudflare_not_root
>   - old_99_system_removed
> 
> ### archive
> - archive.qispark_legacy.md
>   - old_nav
>   - old_names
>   - deprecated_pages
>   - removed_routes
>   - legacy_qios
> 
> ## 20_qiserver
> ### _root
> - why.qiserver.md
> - map.qiserver_current.md
> - map.qiserver_target.md
> - rules.qiserver_scope.md
> 
> ### migration
> - plan.qiserver_from_workspace_scripts.md
>   - ai
>   - apps
>   - db
>   - deploy
>   - dev
>   - flow
>   - inbox
>   - ingest
>   - pdf
>   - process
>   - sync
>   - tools
> - audit.qiserver_script_routes.md
>   - keep_in_workspace
>   - move_to_qiserver
>   - merge
>   - delete
>   - quarantine
> 
> ### runtime
> - notes.qiserver_runtime.md
>   - fastapi
>   - ollama
>   - aider
>   - lancedb
>   - tmux
>   - ports
>   - env
> - rules.qiserver_runtime.md
>   - server_runs_services
>   - secrets_never_public
>   - logs_not_docs
>   - runtime_not_kb
> 
> ### data
> - notes.qiserver_data.md
>   - sqlite
>   - supabase
>   - csv_imports
>   - vectors
>   - apis
> - map.qiserver_data_flow.md
>   - ingest
>   - normalize
>   - store
>   - embed
>   - retrieve
>   - sync
> 
> ### services
> - map.qiserver_services.md
>   - qiconnect
>   - qimemory
>   - qiapi
>   - qillm
>   - qivector
> 
> ### qiconnect
> - notes.qiserver_qiconnect.md
>   - contacts
>   - messages
>   - clients
>   - vendors
>   - crm
>   - outreach
> - notes.qiconnect_cloudflare.md
>   - pages
>   - workers
>   - routes
>   - redirects
>   - env
>   - deploy
>   - public_output
>   - not_source_truth
> 
> ### qimemory
> - why.qimemory.md
> - notes.qiserver_qimemory.md
>   - capture
>   - ingest
>   - summarize
>   - embed
>   - classify
>   - route
>   - recall
>   - archive_pointer
> - map.qimemory_pipeline.md
>   - voice
>   - screenshots
>   - notes
>   - webclips
>   - scans
>   - downloads
>   - triage
>   - route
> 
> ### ops
> - ops.qiserver_maintenance.md
>   - setup
>   - restart
>   - backup
>   - recovery
>   - troubleshooting
>   - deploy
> 
> ## 30_qidrive
> ### _root
> - why.qidrive.md
> - map.qidrive_current.md
> - map.qidrive_target.md
> - rules.qidrive_scope.md
> 
> ### migration
> - plan.qidrive_from_qivault.md
>   - current_40_qivault
>   - target_30_qidrive
>   - rename_plan
>   - path_risks
>   - links_to_update
> - audit.qidrive_storage.md
>   - records
>   - evidence
>   - exports
>   - mirrors
>   - duplicates
>   - sensitive_files
> 
> ### records
> - notes.qidrive_records.md
>   - identity
>   - legal
>   - money
>   - medical
>   - housing
>   - taxes
>   - benefits
> 
> ### evidence
> - notes.qidrive_evidence.md
>   - exhibits
>   - screenshots
>   - messages
>   - pdfs
>   - scans
>   - photos
>   - audio
>   - video
> - rules.qidrive_evidence.md
>   - evidence_lives_here
>   - docs_point_here
>   - do_not_duplicate_in_qispark
>   - redact_before_public
> 
> ### mirrors
> - notes.qidrive_mirrors.md
>   - google_drive
>   - local
>   - archive
>   - exports
> - rules.qidrive_access.md
>   - sensitive
>   - retrieval
>   - sharing
>   - redaction
> 
> ## 40_qiapps
> ### _root
> - why.qiapps.md
> - map.qiapps_current.md
> - map.qiapps_target.md
> - rules.qiapps_scope.md
> 
> ### migration
> - plan.qiapps_from_60_qiapps.md
>   - current_60_qiapps
>   - target_40_qiapps
>   - rename_plan
>   - app_boundaries
>   - links_to_update
> 
> ### qilife
> - spec.qiapps_qilife.md
>   - dashboard
>   - routines
>   - tasks
>   - money
>   - health
>   - legal
>   - gigi
> - map.qilife_flows.md
> - backlog.qilife.md
> 
> ### qiconnect
> - spec.qiapps_qiconnect.md
>   - contacts
>   - messages
>   - clients
>   - vendors
>   - crm
>   - outreach
> - map.qiconnect_flows.md
> - backlog.qiconnect.md
> 
> ### qinexus
> - spec.qiapps_qinexus.md
>   - search
>   - retrieval
>   - records
>   - evidence
>   - semantic_index
> - map.qinexus_flows.md
> - backlog.qinexus.md
> 
> ### qidna
> - spec.qiapps_qidna.md
>   - identity
>   - rules
>   - preferences
>   - memory
>   - ai_alignment
> - map.qidna_flows.md
> - backlog.qidna.md
> 
> ### qiaccess
> - spec.qiapps_qiaccess.md
>   - accounts
>   - devices
>   - permissions
>   - recovery
>   - security
> - map.qiaccess_flows.md
> - backlog.qiaccess.md
> :::
> 
> ## Why this is better
> 
> This mirrors the approved top:
> 
> ```text
> 00_qilabs.workspace
> 10_qispark
> 20_qiserver
> 30_qidrive
> 40_qiapps
> ```
> 
> So when you are working inside QiSpark, your brain sees the same system spine as the actual workspace.
> 
> ## Critical rule
> 
> Inside `10_qispark`, the folders are **not the real runtime folders**.
> 
> They are the **knowledge mirror** of the real folders.
> 
> So:
> 
> ```text
> 10_qispark/20_qiserver
> ```
> 
> means:
> 
> ```text
> docs, maps, rules, and plans ABOUT qiserver
> ```
> 
> Not:
> 
> ```text
> actual qiserver code
> ```
> 
> That keeps the logic clean. QiSpark mirrors the system without becoming the system.

### User
> ok so you ahve workspace, qispark and now let me see how you would do qiserver, please

### Assistant
> I’m going to treat this as the **actual `20_qiserver` root**, not the QiSpark mirror of it. So this is where the scripts/services from the current workspace should land.

### Assistant
> Yes. Here’s how I’d do **`20_qiserver`** now.
> 
> Design rule:
> 
> ```text
> 20_qiserver = runtime, services, data pipelines, deploy, jobs, logs, server ops
> ```
> 
> Not:
> 
> ```text
> KB docs
> evidence storage
> workspace setup
> app-spec brainstorming
> ```
> 
> :::writing{variant="standard" id="81736"}
> # 20_qiserver
> 
> ## _root
> - why.qiserver.md
> - readme.qiserver_root.md
> - codex.qiserver_ai.md
> - changelog.qiserver.md
> - env.qiserver.example.env
> - justfile
> 
> ## 00_config
> - config.qiserver_runtime.json
> - config.qiserver_paths.json
> - config.qiserver_ports.json
> - config.qiserver_services.json
> - config.qiserver_secrets.example.json
> 
> ## 10_runtime
> ### local
> - run.qiserver_dev.ps1
> - run.qiserver_dev.sh
> - run.qiserver_agent.ps1
> - run.qiserver_workers.ps1
> - check.qiserver_env.ps1
> - check.qiserver_env.sh
> 
> ### api
> - app.qiserver_fastapi.py
> - routes.qiserver_health.py
> - routes.qiserver_services.py
> - routes.qiserver_webhooks.py
> 
> ### process
> - runner.qiserver_command.py
> - runner.qiserver_service.py
> - runner.qiserver_worker.py
> - scheduler.qiserver_windows_task.xml
> - scheduler.qiserver_install.ps1
> 
> ## 20_data
> ### sqlite
> - schema.qiserver_sqlite.md
> - migrate.qiserver_sqlite.ps1
> - seed.qiserver_sqlite.ps1
> - reset.qiserver_sqlite.ps1
> - start.qiserver_sqlite.ps1
> - stop.qiserver_sqlite.ps1
> 
> ### supabase
> - schema.qiserver_supabase.md
> - migrate.qiserver_supabase.ps1
> - validate.qiserver_supabase.py
> - log.qiserver_supabase_error.py
> 
> ### csv
> - pipeline.qiserver_csv_import.md
> - convert.qiserver_csv_to_md.py
> - validate.qiserver_csv.py
> - compare.qiserver_csv_md.py
> 
> ### vectors
> - schema.qiserver_vectors.md
> - build.qiserver_vector_index.py
> - search.qiserver_vectors.py
> - sync.qiserver_vectors.py
> 
> ## 30_services
> ### qiapi
> - why.qiapi.md
> - service.qiapi.md
> - routes.qiapi.py
> - auth.qiapi_check.ps1
> - health.qiapi.py
> 
> ### qillm
> - why.qillm.md
> - service.qillm.md
> - models.qillm.py
> - prompts.qillm.py
> - rag.qillm_core.py
> 
> ### qivector
> - why.qivector.md
> - service.qivector.md
> - index.qivector_build.py
> - search.qivector_docs.py
> - sync.qivector_index.py
> 
> ### qimemory
> - why.qimemory.md
> - service.qimemory.md
> 
> #### capture
> - capture.qimemory_audio.py
> - capture.qimemory_files.py
> - capture.qimemory_web.py
> - capture.qimemory_screenshots.py
> 
> #### inbox
> - audit.qimemory_inbox.ts
> - normalize.qimemory_inbox.ts
> - dedup.qimemory_inbox.ts
> - rename.qimemory_inbox.py
> - run.qimemory_inbox.ts
> 
> #### ingest
> - ingest.qimemory_audio.py
> - ingest.qimemory_files.py
> - ingest.qimemory_pdf.ts
> - ingest.qimemory_video.py
> - ingest.qimemory_web.py
> 
> #### process
> - process.qimemory_clean.py
> - process.qimemory_normalize.py
> - process.qimemory_summarize.py
> - process.qimemory_classify.py
> - process.qimemory_route.py
> - process.qimemory_embed.py
> 
> #### recall
> - recall.qimemory_search.py
> - recall.qimemory_context.py
> - recall.qimemory_profile.py
> 
> ### qiconnect
> - why.qiconnect_server.md
> - service.qiconnect.md
> 
> #### contacts
> - service.qiconnect_contacts.py
> - sync.qiconnect_contacts.py
> 
> #### mail
> - service.qiconnect_mail.py
> - get.qiconnect_mail_recent.py
> - send.qiconnect_mail.py
> 
> #### calendar
> - service.qiconnect_calendar.py
> - get.qiconnect_calendar_upcoming.py
> - create.qiconnect_calendar_event.py
> 
> #### sms
> - service.qiconnect_sms.py
> - send.qiconnect_sms.py
> 
> #### web
> - service.qiconnect_web.py
> - get.qiconnect_web.py
> - search.qiconnect_web.py
> 
> #### cloudflare
> - why.qiconnect_cloudflare.md
> - service.qiconnect_cloudflare.md
> - deploy.qiconnect_cloudflare.ps1
> - deploy.qiconnect_workers.ps1
> - get.qiconnect_worker_urls.ps1
> - routes.qiconnect_cloudflare.json
> - redirects.qiconnect_cloudflare.json
> 
> ## 40_apps_runtime
> ### qilife
> - service.qilife_runtime.md
> - routes.qilife_api.py
> - jobs.qilife_sync.py
> 
> ### qinexus
> - service.qinexus_runtime.md
> - routes.qinexus_search.py
> - jobs.qinexus_index.py
> 
> ### qidna
> - service.qidna_runtime.md
> - routes.qidna_profile.py
> - jobs.qidna_sync.py
> 
> ### qiaccess
> - service.qiaccess_runtime.md
> - routes.qiaccess_auth.py
> - jobs.qiaccess_check.py
> 
> ## 50_jobs
> ### sync
> - job.qiserver_sync.py
> - sync.qiserver_git.py
> - sync.qiserver_gdrive.py
> - sync.qiserver_index.ts
> 
> ### backup
> - job.qiserver_backup.py
> - backup.qiserver_data.ps1
> - restore.qiserver_data.ps1
> 
> ### ingest
> - job.qiserver_ingest.py
> - queue.qiserver_ingest.py
> 
> ### cleanup
> - job.qiserver_cleanup.py
> - clean.qiserver_storage.py
> - clean.qiserver_duplicates.py
> 
> ### deploy
> - job.qiserver_deploy.py
> - deploy.qiserver_all.ps1
> - deploy.qiserver_critical.ps1
> 
> ## 60_tools
> ### repo
> - validate.qiserver_paths.py
> - lint.qiserver_tree.py
> - enforce.qiserver_structure.py
> - print.qiserver_tree.py
> 
> ### frontmatter
> - add.qiserver_frontmatter.py
> - validate.qiserver_frontmatter.ts
> - enforce.qiserver_frontmatter.py
> 
> ### maps
> - map.qiserver_tree.py
> - map.qiserver_slugs.py
> 
> ### debug
> - debug.qiserver_maps.py
> - test.qiserver_pipeline.ps1
> - verify.qiserver_env.ps1
> - verify.qiserver_env.sh
> 
> ## 70_logs
> - logs.qiserver.md
>   - runtime
>   - errors
>   - deploy
>   - ingest
>   - memory
>   - sync
> 
> ## 80_ops
> - ops.qiserver_maintenance.md
>   - setup
>   - start
>   - stop
>   - restart
>   - backup
>   - restore
>   - troubleshoot
> - ops.qiserver_deploy.md
>   - local
>   - cloudflare
>   - rollback
>   - env_check
> - ops.qiserver_migration_from_workspace.md
>   - scripts_to_move
>   - scripts_to_merge
>   - scripts_to_delete
>   - scripts_to_quarantine
> 
> ## 90_rules
> - rules.qiserver_scope.md
>   - runtime_lives_here
>   - services_live_here
>   - secrets_never_public
>   - qiserver_not_kb
>   - qiserver_not_drive
>   - qiserver_not_workspace
>   - logs_not_docs
>   - do_not_put_here
> :::
> 
> ## My cleanup call
> 
> From your current `00_QiLabs.workspace/50_scripts`, these move cleanly:
> 
> | Current | New home |
> |---|---|
> | `ai/memory`, `inbox`, `ingest`, `pdf`, `process` | `20_qiserver/30_services/qimemory` |
> | `ai/rag`, `ai/prompts`, `ai/agents` | `20_qiserver/30_services/qillm` |
> | `apps/calendar`, `apps/mail`, `apps/sms`, `apps/web` | `20_qiserver/30_services/qiconnect` |
> | `apps/vault` | probably `20_qiserver/30_services/qimemory` or `30_qidrive` depending whether it writes records |
> | `db` | `20_qiserver/20_data` |
> | `deploy`, `workers` | `20_qiserver/30_services/qiconnect/cloudflare` or `20_qiserver/50_jobs/deploy` |
> | `dev`, `flow/runners`, `flow/schedulers` | `20_qiserver/10_runtime` |
> | `sync`, backups, jobs | `20_qiserver/50_jobs` |
> | `frontmatter`, `maps`, `repo tools` | split between `20_qiserver/60_tools` and `00_qilabs.workspace/50_toolkit` |
> 
> ## I would not create all files immediately
> 
> The **folders are the important part**. The files should only exist when they map to something real from current `50_scripts` or immediately-needed docs.
> 
> The one set I would create immediately:
> 
> ```text
> why.qiserver.md
> rules.qiserver_scope.md
> ops.qiserver_migration_from_workspace.md
> ```
> 
> Because those prevent the same mess from reforming.

### User
> ok, so we are working in the real qiserver folder right now, not the spark markdown right, but the spark markdown folder for qiserver was done if so we can proceed with how to use our blob storage google drive and fnally the qiapps, tehn we can adit or idc

### Assistant
> Yes — correct.
> 
> The last `20_qiserver` tree was for the **real `20_qiserver` folder**, not the QiSpark mirror.
> 
> So the mental split is:
> 
> ```text
> 10_qispark/20_qiserver = markdown mirror ABOUT qiserver
> 20_qiserver = actual runtime/server/services folder
> ```
> 
> Now we can proceed to the real storage layer and apps layer:
> 
> ```text
> 30_qidrive = Google Drive/blob/storage/evidence layer
> 40_qiapps = app specs + app shells/frontends, not server runtime
> ```
> 
> # 30_qidrive
> 
> This is the real Google Drive/blob layer. It should store **files**, not deep doctrine. QiSpark can describe the files. QiServer can index/process them. QiDrive holds them.
> 
> :::writing{variant="standard" id="74021"}
> # 30_qidrive
> <!-- currently: 40_qivault -->
> 
> ## _root
> - why.qidrive.md
> - readme.qidrive_root.md
> - changelog.qidrive.md
> - rules.qidrive_scope.md
> 
> ## 00_index
> - index.qidrive_records.md
> - index.qidrive_evidence.md
> - index.qidrive_exports.md
> - index.qidrive_mirrors.md
> 
> ## 10_records
> ### identity
> - .why.identity.md
> - ids
> - licenses
> - social_security
> - immigration
> 
> ### legal
> - .why.legal.md
> - claims
> - notices
> - filings
> - court
> - contracts
> 
> ### money
> - .why.money.md
> - income
> - bills
> - taxes
> - disputes
> - receipts
> 
> ### medical
> - .why.medical.md
> - visits
> - prescriptions
> - insurance
> - hospital
> - care
> 
> ### housing
> - .why.housing.md
> - lease
> - utilities
> - repairs
> - notices
> - photos
> 
> ## 20_evidence
> ### exhibits
> - .why.exhibits.md
> - active
> - final
> - sent
> - archived
> 
> ### screenshots
> - .why.screenshots.md
> - messages
> - websites
> - apps
> - receipts
> - errors
> 
> ### messages
> - .why.messages.md
> - sms
> - email
> - messenger
> - whatsapp
> - transcripts
> 
> ### pdfs
> - .why.pdfs.md
> - forms
> - letters
> - notices
> - records
> - packets
> 
> ### media
> - .why.media.md
> - photos
> - audio
> - video
> - scans
> 
> ## 30_drive_mirror
> ### google_drive
> - .why.google_drive.md
> - my_drive
> - shared_with_me
> - exports
> - upload_queue
> 
> ### local_mirror
> - .why.local_mirror.md
> - active_sync
> - offline_cache
> - restore_points
> 
> ### archive_mirror
> - .why.archive_mirror.md
> - cold_storage
> - old_exports
> - deprecated_sets
> 
> ## 40_exports
> ### packets
> - .why.packets.md
> - legal_packets
> - exhibit_packets
> - client_packets
> - admin_packets
> 
> ### machine_exports
> - .why.machine_exports.md
> - csv
> - json
> - markdown
> - zip
> 
> ## 50_pointers
> - pointers.qidrive_files.csv
> - pointers.qidrive_evidence.csv
> - pointers.qidrive_records.csv
> 
> ## 90_rules
> - rules.qidrive_access.md
>   - private_by_default
>   - redact_before_public
>   - qidrive_holds_blobs
>   - qispark_holds_meaning
>   - qiserver_indexes_and_processes
>   - qiapps_request_through_qiserver
> :::
> 
> ## QiDrive rule
> 
> ```text
> QiDrive stores the thing.
> QiSpark explains the thing.
> QiServer processes the thing.
> QiApps display/use the thing.
> ```
> 
> That’s the clean split.
> 
> Do **not** put long explanations inside every folder. Use `.why.name.md` only where it prevents future confusion.
> 
> A `.why` file should be tiny:
> 
> ```markdown
> # Why this exists
> 
> This folder holds raw and final evidence files.
> 
> Do not write strategy or analysis here.
> Put explanations in QiSpark and pointers in QiServer/QiMemory.
> ```
> 
> # 40_qiapps
> 
> This is the real apps layer. Not server runtime. Not markdown KB. Not blob storage.
> 
> It holds app specs, UI/frontend shells, app-level configs, app maps, and backlogs. Runtime/API code belongs in `20_qiserver`.
> 
> :::writing{variant="standard" id="50263"}
> # 40_qiapps
> <!-- currently: 60_qiapps -->
> 
> ## _root
> - why.qiapps.md
> - readme.qiapps_root.md
> - changelog.qiapps.md
> - rules.qiapps_scope.md
> 
> ## 00_shared
> ### ui
> - .why.shared_ui.md
> - components
> - layouts
> - themes
> - icons
> 
> ### config
> - config.qiapps_shared.json
> - config.qiapps_routes.json
> 
> ### patterns
> - patterns.qiapps_navigation.md
> - patterns.qiapps_cards.md
> - patterns.qiapps_forms.md
> 
> ## 10_qilife
> - why.qilife.md
> - spec.qilife_app.md
> - map.qilife_flows.md
> - backlog.qilife.md
> 
> ### ui
> - dashboard
> - routines
> - tasks
> - money
> - health
> - legal
> - gigi
> 
> ### config
> - config.qilife_routes.json
> - config.qilife_views.json
> 
> ## 20_qiconnect
> - why.qiconnect.md
> - spec.qiconnect_app.md
> - map.qiconnect_flows.md
> - backlog.qiconnect.md
> 
> ### ui
> - contacts
> - messages
> - clients
> - vendors
> - crm
> - outreach
> 
> ### config
> - config.qiconnect_routes.json
> - config.qiconnect_views.json
> 
> ## 30_qinexus
> - why.qinexus.md
> - spec.qinexus_app.md
> - map.qinexus_flows.md
> - backlog.qinexus.md
> 
> ### ui
> - search
> - retrieval
> - records
> - evidence
> - semantic_index
> 
> ### config
> - config.qinexus_routes.json
> - config.qinexus_views.json
> 
> ## 40_qidna
> - why.qidna.md
> - spec.qidna_app.md
> - map.qidna_flows.md
> - backlog.qidna.md
> 
> ### ui
> - identity
> - rules
> - preferences
> - memory
> - ai_alignment
> 
> ### config
> - config.qidna_routes.json
> - config.qidna_views.json
> 
> ## 50_qiaccess
> - why.qiaccess.md
> - spec.qiaccess_app.md
> - map.qiaccess_flows.md
> - backlog.qiaccess.md
> 
> ### ui
> - accounts
> - devices
> - permissions
> - recovery
> - security
> 
> ### config
> - config.qiaccess_routes.json
> - config.qiaccess_views.json
> 
> ## 90_rules
> - rules.qiapps_boundaries.md
>   - apps_not_server_runtime
>   - apps_not_drive_storage
>   - apps_not_kb
>   - api_calls_go_to_qiserver
>   - files_come_from_qidrive_pointers
>   - docs_live_in_qispark
> :::
> 
> # The whole clean model
> 
> ```text
> 00_qilabs.workspace
> = setup, configs, extensions, quickstart, toolkit
> 
> 10_qispark
> = markdown KB, maps, docs, rules, decisions
> 
> 20_qiserver
> = runtime, APIs, services, memory, processing, Cloudflare deploy
> 
> 30_qidrive
> = Google Drive/blob/files/evidence/storage
> 
> 40_qiapps
> = app shells, UI, specs, app configs, app backlogs
> ```
> 
> ## My honest call
> 
> This is now coherent.
> 
> The thing to watch: **QiDrive can get messy fast** because “storage” invites hoarding. So the key rule is:
> 
> ```text
> Do not explain files in QiDrive.
> Do not duplicate files into QiSpark.
> Use pointers.
> ```
> 
> QiSpark can say:
> 
> ```text
> Evidence for X lives at qidrive://20_evidence/screenshots/messages/...
> ```
> 
> QiServer/QiMemory can index it.
> 
> QiApps can display it.
> 
> But the blob stays in QiDrive.

### User
> ok give me the full and finall and i ahve one reminder you will need to have the cadence folder for the obisidain pluggin, bosdiadina folders and runtime inside the spark and then we can audit.

### Assistant
> I’m folding your last reminder into the whole spine: QiSpark is not just docs, it is also the Obsidian working environment, so Cadence/Obsidian/runtime belongs inside `10_qispark`, not workspace.

### Assistant
> Yes. This is the **full current final candidate**.
> 
> I’m calling it **final candidate**, not holy scripture. We audit after. No empty-folder worship. If a folder/file does not earn its existence, we delete or don’t create it.
> 
> :::writing{variant="standard" id="64819"}
> ---
> title: QiLabs Final Candidate Tree
> section: qilabs/10_qispark/10_qispark/nav
> access_level: L1
> visibility: private
> ai_ingest: true
> status: final_candidate
> last_updated: 2026-06-20
> mindmap-plugin: basic
> ---
> 
> # qilabs
> 
> ## 00_qilabs.workspace
> ### _root
> - why.qilabs_workspace.md
> - readme.qilabs_workspace.md
> - quickstart.qilabs_workspace.md
> - changelog.qilabs_workspace.md
> - qilabs.code-workspace
> - justfile
> 
> ### .github
> #### issue_template
> - architecture_change.md
> - bug_report.md
> - feature_request.md
> #### workflows
> - ci.yml
> - docs.yml
> - lint.yml
> - migrations.yml
> - release.yml
> - test.yml
> - CODEOWNERS
> - pull_request_template.md
> 
> ### .qios
> - docs_compiler.config.json
> 
> ### .vscode
> - settings.json
> 
> ### 20_manifests
> - apps.manifest.json
> - connectors.manifest.json
> - domains.manifest.json
> - repos.manifest.json
> - services.manifest.json
> - storage.manifest.json
> 
> ### 30_configs
> - .editorconfig
> - .gitignore
> - repo.rules.json
> - tsconfig.root.json
> - eslint.config.mjs
> - tailwind.config.ts
> - postcss.config.js
> 
> ### 50_toolkit
> - bootstrap_workspace.ps1
> - check_root_clean.ps1
> - export_file_inventory.ps1
> - generate_tree.ps1
> - tree_snapshot.ps1
> - verify_env.ps1
> 
> ### 99_quarantine
> - hold_only_until_sorted
> 
> ## 10_qispark
> ### _root
> - why.qispark.md
> - readme.qispark_root.md
> - codex.qispark_ai.md
> - changelog.qispark.md
> 
> ### 00_obsidian
> #### _root
> - why.qispark_obsidian.md
> - guide.qispark_obsidian.md
> #### .obsidian
> - app.json
> - appearance.json
> - core-plugins.json
> - community-plugins.json
> - hotkeys.json
> - workspace.json
> #### plugins
> - plugins.qispark_obsidian.md
> - plugins.qispark_required.md
> - plugins.qispark_optional.md
> #### attachments
> - rules.qispark_attachments.md
> - inbox.attachments_qispark.md
> #### canvas
> - map.qispark_canvas_index.md
> - canvas.qilabs_spine.canvas
> - canvas.qispark_nav.canvas
> #### cadence
> - why.qispark_cadence.md
> - cadence.qispark_index.md
> - cadence.qispark_daily.md
> - cadence.qispark_weekly.md
> - cadence.qispark_monthly.md
> - cadence.qispark_review.md
> 
> ### 01_nav
> - why.qispark_nav.md
> - map.qispark_nav.md
>   - mirror_nav
>   - public_nav
>   - private_nav
>   - archive_nav
> - map.qispark_tree.md
>   - current_tree
>   - target_tree
>   - move_map
>   - rename_map
> - registry.qispark_nav.csv
> - registry.qispark_routes.csv
> - audit.qispark_nav.md
>   - bad_names
>   - duplicate_nodes
>   - stale_routes
>   - empty_placeholders
> 
> ### 10_qilabs.workspace
> - why.qispark_mirror_workspace.md
> - map.qilabs_workspace_current.md
> - map.qilabs_workspace_target.md
> - audit.qilabs_workspace_current_tree.md
>   - keep
>   - move
>   - delete
>   - quarantine
> - plan.qilabs_workspace_cleanup.md
>   - scripts_to_move
>   - configs_to_keep
>   - manifests_to_check
>   - quarantine_to_sort
> - rules.qilabs_workspace_scope.md
>   - setup_only
>   - configs
>   - extensions
>   - workspace_toolkit
>   - not_source_truth
>   - not_runtime
>   - not_kb
> - notes.qilabs_workspace_configs.md
>   - github
>   - qios
>   - vscode
>   - manifests
>   - repo_rules
>   - docs_compiler
> 
> ### 20_qispark
> - why.qispark_kb.md
> - guide.qispark_start.md
>   - what_this_is
>   - how_to_use_it
>   - what_lives_here
>   - what_does_not_live_here
>   - current_state
>   - next_moves
> - kb.qispark_context.md
>   - qilabs
>   - workspace
>   - qispark
>   - qiserver
>   - qidrive
>   - qiapps
>   - terms
>   - boundaries
> - kb.qispark_current_state.md
>   - locked
>   - changed
>   - still_fluid
>   - parked
> - kb.qispark_source_map.md
>   - what_counts
>   - what_does_not_count
>   - where_truth_lives
>   - where_records_live
>   - where_runtime_lives
> 
> ### 30_qiserver
> - why.qispark_mirror_qiserver.md
> - map.qiserver_current.md
> - map.qiserver_target.md
> - plan.qiserver_from_workspace_scripts.md
>   - ai
>   - apps
>   - db
>   - deploy
>   - dev
>   - flow
>   - inbox
>   - ingest
>   - pdf
>   - process
>   - sync
>   - tools
> - audit.qiserver_script_routes.md
>   - keep_in_workspace
>   - move_to_qiserver
>   - merge
>   - delete
>   - quarantine
> - notes.qiserver_runtime.md
>   - fastapi
>   - ollama
>   - aider
>   - lancedb
>   - tmux
>   - ports
>   - env
> - map.qiserver_services.md
>   - qiconnect
>   - qimemory
>   - qiapi
>   - qillm
>   - qivector
> - map.qimemory_pipeline.md
>   - capture
>   - ingest
>   - summarize
>   - embed
>   - classify
>   - route
>   - recall
> 
> ### 40_qidrive
> - why.qispark_mirror_qidrive.md
> - map.qidrive_current.md
> - map.qidrive_target.md
> - plan.qidrive_from_qivault.md
>   - current_40_qivault
>   - target_30_qidrive
>   - rename_plan
>   - path_risks
>   - links_to_update
> - notes.qidrive_records.md
>   - identity
>   - legal
>   - money
>   - medical
>   - housing
>   - taxes
>   - benefits
> - notes.qidrive_evidence.md
>   - exhibits
>   - screenshots
>   - messages
>   - pdfs
>   - scans
>   - photos
>   - audio
>   - video
> - rules.qidrive_evidence.md
>   - evidence_lives_here
>   - docs_point_here
>   - do_not_duplicate_in_qispark
>   - redact_before_public
> 
> ### 50_qiapps
> - why.qispark_mirror_qiapps.md
> - map.qiapps_current.md
> - map.qiapps_target.md
> - plan.qiapps_from_60_qiapps.md
>   - current_60_qiapps
>   - target_40_qiapps
>   - rename_plan
>   - app_boundaries
>   - links_to_update
> - spec.qiapps_qilife.md
>   - dashboard
>   - routines
>   - tasks
>   - money
>   - health
>   - legal
>   - gigi
> - spec.qiapps_qiconnect.md
>   - contacts
>   - messages
>   - clients
>   - vendors
>   - crm
>   - outreach
> - spec.qiapps_qinexus.md
>   - search
>   - retrieval
>   - records
>   - evidence
>   - semantic_index
> - spec.qiapps_qidna.md
>   - identity
>   - rules
>   - preferences
>   - memory
>   - ai_alignment
> - spec.qiapps_qiaccess.md
>   - accounts
>   - devices
>   - permissions
>   - recovery
>   - security
> 
> ### 60_rules
> - why.qispark_rules.md
> - rules.qispark_core.md
>   - truth
>   - leverage
>   - naming
>   - modularity
>   - ai_use
>   - human_override
> - rules.qispark_docs.md
>   - filenames
>   - folders
>   - markdown
>   - frontmatter
>   - links
>   - archive
> - rules.qispark_boundaries.md
>   - qispark_not_workspace
>   - qispark_not_server
>   - qispark_not_drive
>   - qispark_not_apps
>   - docs_not_evidence
>   - maps_not_runtime
> - rules.qispark_access.md
>   - access_level
>   - visibility
>   - ai_ingest
>   - status
>   - sensitive_info
>   - public_private
> 
> ### 70_prompts
> - prompts.qispark_build.md
>   - nav_cleanup
>   - folder_reconcile
>   - docs_generate
>   - frontmatter_audit
> - prompts.qispark_extract.md
>   - extract_nav
>   - extract_decisions
>   - extract_tasks
>   - find_contradictions
>   - check_privacy
> - prompts.qispark_write.md
>   - clean_doc
>   - compress_notes
>   - make_timeline
>   - make_plan
>   - make_message
> 
> ### 80_ops
> - ops.qispark_maintenance.md
>   - add_page
>   - update_nav
>   - deprecate_page
>   - archive_content
>   - audit
>   - reconcile_names
> - ops.qispark_publish.md
>   - route_check
>   - private_check
>   - broken_links
>   - export_review
>   - handoff_to_qiserver
> 
> ### 90_runtime
> - why.qispark_runtime.md
> - runtime.qispark_obsidian.md
>   - vault_open
>   - plugin_state
>   - cadence_state
>   - active_file
>   - workspace_layout
> - runtime.qispark_ai.md
>   - active_prompt
>   - active_context
>   - ingest_ready
>   - export_ready
> - runtime.qispark_publish.md
>   - docs_compile
>   - route_check
>   - private_check
>   - output_handoff
> 
> ### 91_ref
> - ref.qispark_tables.md
>   - glossary
>   - canonical_names
>   - root_index
>   - route_index
>   - access_values
>   - visibility_values
>   - ingest_values
>   - status_values
> - ref.qispark_legacy_names.md
>   - qivault_to_qidrive
>   - qiapps_old_60
>   - qicapture_to_qimemory
>   - cloudflare_not_root
>   - old_99_system_removed
> 
> ### 98_archive
> - archive.qispark_legacy.md
>   - old_nav
>   - old_names
>   - deprecated_pages
>   - removed_routes
>   - legacy_qios
> 
> ## 20_qiserver
> ### _root
> - why.qiserver.md
> - readme.qiserver_root.md
> - codex.qiserver_ai.md
> - changelog.qiserver.md
> - env.qiserver.example.env
> - justfile
> 
> ### 00_config
> - config.qiserver_runtime.json
> - config.qiserver_paths.json
> - config.qiserver_ports.json
> - config.qiserver_services.json
> - config.qiserver_secrets.example.json
> 
> ### 10_runtime
> #### local
> - run.qiserver_dev.ps1
> - run.qiserver_dev.sh
> - run.qiserver_agent.ps1
> - run.qiserver_workers.ps1
> - check.qiserver_env.ps1
> - check.qiserver_env.sh
> #### api
> - app.qiserver_fastapi.py
> - routes.qiserver_health.py
> - routes.qiserver_services.py
> - routes.qiserver_webhooks.py
> #### process
> - runner.qiserver_command.py
> - runner.qiserver_service.py
> - runner.qiserver_worker.py
> - scheduler.qiserver_windows_task.xml
> - scheduler.qiserver_install.ps1
> 
> ### 20_data
> #### sqlite
> - schema.qiserver_sqlite.md
> - migrate.qiserver_sqlite.ps1
> - seed.qiserver_sqlite.ps1
> - reset.qiserver_sqlite.ps1
> - start.qiserver_sqlite.ps1
> - stop.qiserver_sqlite.ps1
> #### supabase
> - schema.qiserver_supabase.md
> - migrate.qiserver_supabase.ps1
> - validate.qiserver_supabase.py
> - log.qiserver_supabase_error.py
> #### csv
> - pipeline.qiserver_csv_import.md
> - convert.qiserver_csv_to_md.py
> - validate.qiserver_csv.py
> - compare.qiserver_csv_md.py
> #### vectors
> - schema.qiserver_vectors.md
> - build.qiserver_vector_index.py
> - search.qiserver_vectors.py
> - sync.qiserver_vectors.py
> 
> ### 30_services
> #### qiapi
> - why.qiapi.md
> - service.qiapi.md
> - routes.qiapi.py
> - auth.qiapi_check.ps1
> - health.qiapi.py
> #### qillm
> - why.qillm.md
> - service.qillm.md
> - models.qillm.py
> - prompts.qillm.py
> - rag.qillm_core.py
> #### qivector
> - why.qivector.md
> - service.qivector.md
> - index.qivector_build.py
> - search.qivector_docs.py
> - sync.qivector_index.py
> #### qimemory
> - why.qimemory.md
> - service.qimemory.md
> ##### capture
> - capture.qimemory_audio.py
> - capture.qimemory_files.py
> - capture.qimemory_web.py
> - capture.qimemory_screenshots.py
> ##### inbox
> - audit.qimemory_inbox.ts
> - normalize.qimemory_inbox.ts
> - dedup.qimemory_inbox.ts
> - rename.qimemory_inbox.py
> - run.qimemory_inbox.ts
> ##### ingest
> - ingest.qimemory_audio.py
> - ingest.qimemory_files.py
> - ingest.qimemory_pdf.ts
> - ingest.qimemory_video.py
> - ingest.qimemory_web.py
> ##### process
> - process.qimemory_clean.py
> - process.qimemory_normalize.py
> - process.qimemory_summarize.py
> - process.qimemory_classify.py
> - process.qimemory_route.py
> - process.qimemory_embed.py
> ##### recall
> - recall.qimemory_search.py
> - recall.qimemory_context.py
> - recall.qimemory_profile.py
> #### qiconnect
> - why.qiconnect_server.md
> - service.qiconnect.md
> ##### contacts
> - service.qiconnect_contacts.py
> - sync.qiconnect_contacts.py
> ##### mail
> - service.qiconnect_mail.py
> - get.qiconnect_mail_recent.py
> - send.qiconnect_mail.py
> ##### calendar
> - service.qiconnect_calendar.py
> - get.qiconnect_calendar_upcoming.py
> - create.qiconnect_calendar_event.py
> ##### sms
> - service.qiconnect_sms.py
> - send.qiconnect_sms.py
> ##### web
> - service.qiconnect_web.py
> - get.qiconnect_web.py
> - search.qiconnect_web.py
> ##### cloudflare
> - why.qiconnect_cloudflare.md
> - service.qiconnect_cloudflare.md
> - deploy.qiconnect_cloudflare.ps1
> - deploy.qiconnect_workers.ps1
> - get.qiconnect_worker_urls.ps1
> - routes.qiconnect_cloudflare.json
> - redirects.qiconnect_cloudflare.json
> 
> ### 40_apps_runtime
> #### qilife
> - service.qilife_runtime.md
> - routes.qilife_api.py
> - jobs.qilife_sync.py
> #### qinexus
> - service.qinexus_runtime.md
> - routes.qinexus_search.py
> - jobs.qinexus_index.py
> #### qidna
> - service.qidna_runtime.md
> - routes.qidna_profile.py
> - jobs.qidna_sync.py
> #### qiaccess
> - service.qiaccess_runtime.md
> - routes.qiaccess_auth.py
> - jobs.qiaccess_check.py
> 
> ### 50_jobs
> #### sync
> - job.qiserver_sync.py
> - sync.qiserver_git.py
> - sync.qiserver_gdrive.py
> - sync.qiserver_index.ts
> #### backup
> - job.qiserver_backup.py
> - backup.qiserver_data.ps1
> - restore.qiserver_data.ps1
> #### ingest
> - job.qiserver_ingest.py
> - queue.qiserver_ingest.py
> #### cleanup
> - job.qiserver_cleanup.py
> - clean.qiserver_storage.py
> - clean.qiserver_duplicates.py
> #### deploy
> - job.qiserver_deploy.py
> - deploy.qiserver_all.ps1
> - deploy.qiserver_critical.ps1
> 
> ### 60_tools
> #### repo
> - validate.qiserver_paths.py
> - lint.qiserver_tree.py
> - enforce.qiserver_structure.py
> - print.qiserver_tree.py
> #### frontmatter
> - add.qiserver_frontmatter.py
> - validate.qiserver_frontmatter.ts
> - enforce.qiserver_frontmatter.py
> #### maps
> - map.qiserver_tree.py
> - map.qiserver_slugs.py
> #### debug
> - debug.qiserver_maps.py
> - test.qiserver_pipeline.ps1
> - verify.qiserver_env.ps1
> - verify.qiserver_env.sh
> 
> ### 70_logs
> - logs.qiserver.md
>   - runtime
>   - errors
>   - deploy
>   - ingest
>   - memory
>   - sync
> 
> ### 80_ops
> - ops.qiserver_maintenance.md
>   - setup
>   - start
>   - stop
>   - restart
>   - backup
>   - restore
>   - troubleshoot
> - ops.qiserver_deploy.md
>   - local
>   - cloudflare
>   - rollback
>   - env_check
> - ops.qiserver_migration_from_workspace.md
>   - scripts_to_move
>   - scripts_to_merge
>   - scripts_to_delete
>   - scripts_to_quarantine
> 
> ### 90_rules
> - rules.qiserver_scope.md
>   - runtime_lives_here
>   - services_live_here
>   - secrets_never_public
>   - qiserver_not_kb
>   - qiserver_not_drive
>   - qiserver_not_workspace
>   - logs_not_docs
>   - do_not_put_here
> 
> ## 30_qidrive
> ### _root
> - why.qidrive.md
> - readme.qidrive_root.md
> - changelog.qidrive.md
> - rules.qidrive_scope.md
> 
> ### 00_index
> - index.qidrive_records.md
> - index.qidrive_evidence.md
> - index.qidrive_exports.md
> - index.qidrive_mirrors.md
> 
> ### 10_records
> #### identity
> - .why.identity.md
> - ids
> - licenses
> - social_security
> - immigration
> #### legal
> - .why.legal.md
> - claims
> - notices
> - filings
> - court
> - contracts
> #### money
> - .why.money.md
> - income
> - bills
> - taxes
> - disputes
> - receipts
> #### medical
> - .why.medical.md
> - visits
> - prescriptions
> - insurance
> - hospital
> - care
> #### housing
> - .why.housing.md
> - lease
> - utilities
> - repairs
> - notices
> - photos
> 
> ### 20_evidence
> #### exhibits
> - .why.exhibits.md
> - active
> - final
> - sent
> - archived
> #### screenshots
> - .why.screenshots.md
> - messages
> - websites
> - apps
> - receipts
> - errors
> #### messages
> - .why.messages.md
> - sms
> - email
> - messenger
> - whatsapp
> - transcripts
> #### pdfs
> - .why.pdfs.md
> - forms
> - letters
> - notices
> - records
> - packets
> #### media
> - .why.media.md
> - photos
> - audio
> - video
> - scans
> 
> ### 30_drive_mirror
> #### google_drive
> - .why.google_drive.md
> - my_drive
> - shared_with_me
> - exports
> - upload_queue
> #### local_mirror
> - .why.local_mirror.md
> - active_sync
> - offline_cache
> - restore_points
> #### archive_mirror
> - .why.archive_mirror.md
> - cold_storage
> - old_exports
> - deprecated_sets
> 
> ### 40_exports
> #### packets
> - .why.packets.md
> - legal_packets
> - exhibit_packets
> - client_packets
> - admin_packets
> #### machine_exports
> - .why.machine_exports.md
> - csv
> - json
> - markdown
> - zip
> 
> ### 50_pointers
> - pointers.qidrive_files.csv
> - pointers.qidrive_evidence.csv
> - pointers.qidrive_records.csv
> 
> ### 90_rules
> - rules.qidrive_access.md
>   - private_by_default
>   - redact_before_public
>   - qidrive_holds_blobs
>   - qispark_holds_meaning
>   - qiserver_indexes_and_processes
>   - qiapps_request_through_qiserver
> 
> ## 40_qiapps
> ### _root
> - why.qiapps.md
> - readme.qiapps_root.md
> - changelog.qiapps.md
> - rules.qiapps_scope.md
> 
> ### 00_shared
> #### ui
> - .why.shared_ui.md
> - components
> - layouts
> - themes
> - icons
> #### config
> - config.qiapps_shared.json
> - config.qiapps_routes.json
> #### patterns
> - patterns.qiapps_navigation.md
> - patterns.qiapps_cards.md
> - patterns.qiapps_forms.md
> 
> ### 10_qilife
> - why.qilife.md
> - spec.qilife_app.md
> - map.qilife_flows.md
> - backlog.qilife.md
> #### ui
> - dashboard
> - routines
> - tasks
> - money
> - health
> - legal
> - gigi
> #### config
> - config.qilife_routes.json
> - config.qilife_views.json
> 
> ### 20_qiconnect
> - why.qiconnect.md
> - spec.qiconnect_app.md
> - map.qiconnect_flows.md
> - backlog.qiconnect.md
> #### ui
> - contacts
> - messages
> - clients
> - vendors
> - crm
> - outreach
> #### config
> - config.qiconnect_routes.json
> - config.qiconnect_views.json
> 
> ### 30_qinexus
> - why.qinexus.md
> - spec.qinexus_app.md
> - map.qinexus_flows.md
> - backlog.qinexus.md
> #### ui
> - search
> - retrieval
> - records
> - evidence
> - semantic_index
> #### config
> - config.qinexus_routes.json
> - config.qinexus_views.json
> 
> ### 40_qidna
> - why.qidna.md
> - spec.qidna_app.md
> - map.qidna_flows.md
> - backlog.qidna.md
> #### ui
> - identity
> - rules
> - preferences
> - memory
> - ai_alignment
> #### config
> - config.qidna_routes.json
> - config.qidna_views.json
> 
> ### 50_qiaccess
> - why.qiaccess.md
> - spec.qiaccess_app.md
> - map.qiaccess_flows.md
> - backlog.qiaccess.md
> #### ui
> - accounts
> - devices
> - permissions
> - recovery
> - security
> #### config
> - config.qiaccess_routes.json
> - config.qiaccess_views.json
> 
> ### 90_rules
> - rules.qiapps_boundaries.md
>   - apps_not_server_runtime
>   - apps_not_drive_storage
>   - apps_not_kb
>   - api_calls_go_to_qiserver
>   - files_come_from_qidrive_pointers
>   - docs_live_in_qispark
> :::
> 
> ## Audit flags before you build
> 
> I see **five things to check before creating folders**:
> 
> 1. **Empty manifests** in workspace: keep only if scripts read them now. Otherwise quarantine.
> 2. **QiSpark registries**: start with nav/routes only. More CSVs later.
> 3. **QiDrive pointer CSVs**: create only when you are ready to actually point to Drive blobs.
> 4. **QiApps config files**: only create configs for apps you are actively wiring.
> 5. **Archive folders**: don’t create until there is actual legacy content to move.
> 
> The spine is solid now:
> 
> ```text
> 00_qilabs.workspace = setup/toolkit
> 10_qispark = Obsidian/Markdown brain
> 20_qiserver = runtime/services
> 30_qidrive = Google Drive/blob storage
> 40_qiapps = app layer
> ```

### User
> ok you may want to do those checks and also where is my life timeline, my journals, events ect, where are we to store those, my creative mess like the sermons, 713, mirror, onions etc.

### Assistant
> Good catch. I did the infrastructure spine and accidentally underbuilt the actual *human material* QiSpark is supposed to hold. That is not optional — journals, life timeline, sermons, 713, mirror/onion language belong in Spark, with raw attachments in QiDrive.

### Assistant
> Yes — and this exposes the actual missing piece:
> 
> **QiSpark cannot only be system docs.**  
> It also needs your **living narrative layer**: journals, timelines, events, sermons, symbols, recurring language, creative fragments, and identity/story material.
> 
> That belongs in **`10_qispark`**, not `30_qidrive`, unless it is a raw attachment/audio/image/PDF.
> 
> ---
> 
> # Audit checks first
> 
> ## 1. Empty manifests: don’t create more of this
> 
> Your current manifests are empty `{}`. They only stay if scripts actively read them soon. Otherwise, quarantine or leave untouched until useful. No more JSON tombstones.
> 
> ## 2. Naming rules mostly agree with you
> 
> `repo.rules.json` already pushes lowercase, no spaces, limited characters, and underscore preference. But it still has generic exceptions like `README.md` and `USAGE.md`, which conflicts with the newer context-rich filename rule. Keep generic names only where tools force them. fileciteturn1file1
> 
> ## 3. Docs compiler is workable
> 
> The compiler preserves hierarchy, generates indexes, normalizes generated Markdown, and does **not** mutate source Markdown. That’s good. QiSpark can be the Obsidian/Markdown source without the compiler wrecking your notes. fileciteturn1file0
> 
> ## 4. README is not carrying the architecture yet
> 
> The current workspace README is basically just the title, so we are not fighting a mature existing doctrine. Good. We can define the roles cleanly now. fileciteturn1file2
> 
> ---
> 
> # Storage rule for your personal/creative material
> 
> Here’s the clean split:
> 
> | Thing | Goes where | Why |
> |---|---|---|
> | Life timeline | `10_qispark` | authored meaning / chronology |
> | Journals | `10_qispark` | Markdown working memory |
> | Events | `10_qispark` for event notes, `30_qidrive` for raw proof |
> | Sermons / Jesus savage / table-flipping pieces | `10_qispark` | creative writing / doctrine / voice |
> | 713 | `10_qispark` | symbol / meaning system |
> | Mirror / onion / recurring metaphors | `10_qispark` | symbolic language / creative lexicon |
> | Screenshots/audio/photos/PDFs | `30_qidrive` | blobs/evidence |
> | Search/index/AI processing | `20_qiserver/qimemory` | runtime processing |
> | App display | `40_qiapps` | UI/view layer |
> 
> The rule:
> 
> ```text
> QiSpark holds meaning.
> QiDrive holds files.
> QiServer processes.
> QiApps display.
> ```
> 
> ---
> 
> # Patch to QiSpark
> 
> Add this inside:
> 
> ```text
> 10_qispark / 20_qispark
> ```
> 
> Because this is **Spark-native human knowledge**, not a mirror of another root.
> 
> ```markdown
> ### life_stream
> - why.qispark_life_stream.md
> - timeline.qispark_life.md
>   - childhood
>   - resets
>   - housing
>   - work
>   - caregiving
>   - health
>   - relationships
>   - faith
>   - systems
> - events.qispark_life.md
>   - dated_events
>   - turning_points
>   - incidents
>   - wins
>   - losses
>   - unresolved
> - journal.qispark_current.md
>   - today
>   - this_week
>   - active_processing
>   - open_loops
> - journal.qispark_archive.md
>   - older_entries
>   - finished_threads
>   - raw_but_keep
> 
> ### creative
> - why.qispark_creative.md
> - creative.qispark_index.md
>   - sermons
>   - essays
>   - posts
>   - scripts
>   - fragments
>   - titles
> - sermons.qispark_drafts.md
>   - jesus_savage
>   - flip_the_table
>   - modern_parables
>   - faith_without_fluff
> - writing.qispark_fragments.md
>   - lines
>   - hooks
>   - analogies
>   - voice_notes
>   - unfinished
> - posts.qispark_social.md
>   - facebook
>   - linkedin
>   - threads
>   - captions
> 
> ### symbols
> - why.qispark_symbols.md
> - symbols.qispark_713.md
>   - meaning
>   - appearances
>   - patterns
>   - caution_notes
>   - writing_uses
> - symbols.qispark_mirror.md
>   - mirror
>   - reflection
>   - reversal
>   - self_other
>   - perception
> - symbols.qispark_onions.md
>   - layers
>   - peeling
>   - hidden_core
>   - emotional_logic
> - symbols.qispark_lexicon.md
>   - recurring_words
>   - personal_terms
>   - metaphors
>   - phrases
>   - shorthand
> 
> ### narrative
> - why.qispark_narrative.md
> - narrative.qispark_identity.md
>   - who_i_am
>   - what_i_am_building
>   - what_i_refuse
>   - what_i_keep_learning
> - narrative.qispark_themes.md
>   - survival
>   - systems
>   - faith
>   - betrayal
>   - repair
>   - agency
>   - legacy
> - narrative.qispark_arcs.md
>   - origin_arc
>   - reset_arc
>   - builder_arc
>   - caregiver_arc
>   - liberation_arc
> ```
> 
> ---
> 
> # Important correction to final tree
> 
> In the last full tree, this part was underbuilt:
> 
> ```text
> 10_qispark / 20_qispark
> ```
> 
> It should now be:
> 
> ```markdown
> ### 20_qispark
> - why.qispark_kb.md
> - guide.qispark_start.md
> - kb.qispark_context.md
> - kb.qispark_current_state.md
> - kb.qispark_source_map.md
> 
> #### life_stream
> - why.qispark_life_stream.md
> - timeline.qispark_life.md
> - events.qispark_life.md
> - journal.qispark_current.md
> - journal.qispark_archive.md
> 
> #### creative
> - why.qispark_creative.md
> - creative.qispark_index.md
> - sermons.qispark_drafts.md
> - writing.qispark_fragments.md
> - posts.qispark_social.md
> 
> #### symbols
> - why.qispark_symbols.md
> - symbols.qispark_713.md
> - symbols.qispark_mirror.md
> - symbols.qispark_onions.md
> - symbols.qispark_lexicon.md
> 
> #### narrative
> - why.qispark_narrative.md
> - narrative.qispark_identity.md
> - narrative.qispark_themes.md
> - narrative.qispark_arcs.md
> ```
> 
> ---
> 
> # What does **not** go there
> 
> Don’t dump raw files into QiSpark.
> 
> ```text
> voice recordings → 30_qidrive/media/audio
> screenshots → 30_qidrive/evidence/screenshots
> PDF records → 30_qidrive/records or evidence/pdfs
> medical/legal raw docs → 30_qidrive
> processed summaries → 10_qispark
> search/index state → 20_qiserver/qimemory
> ```
> 
> So, for example:
> 
> ```text
> Jesus table-flipping essay draft → 10_qispark/20_qispark/creative
> Voice note of you ranting it out → 30_qidrive/media/audio
> Transcript generated from that voice note → 20_qiserver/qimemory processes it
> Cleaned draft → 10_qispark/20_qispark/creative
> ```
> 
> That’s the clean loop.
> 
> ---
> 
> # My blunt audit note
> 
> The tree got too “system-brain” and forgot **Cody-brain**.
> 
> That’s not acceptable because QiSpark is supposed to hold the meaning layer. Your life timeline, journals, creative language, and symbolic systems are not side quests. They are part of the operating intelligence.
> 
> So yes: add `life_stream`, `creative`, `symbols`, and `narrative` inside QiSpark. Then audit.

### User
> ok, are you ready to reveal to me the full tree?

### Assistant
> Yes. This is the full tree as a **build/audit candidate**, not a command to create every listed file today. Anything that is not already real or immediately useful gets skipped, moved, or quarantined during audit.

### Assistant
> Here’s the full **current final candidate** as a MarkMind-style map.
> 
> Two guardrails before the tree:
> 
> 1. **Do not create empty folders/files just because they appear here.** This is the audit target.
> 2. **QiSpark mirrors the whole spine for Markdown thinking, but the real runtime/storage/app files live in their actual roots.**
> 
> The uploaded `repo.rules.json` already supports lowercase/no-space naming rules, and the docs compiler is already set to preserve hierarchy and generate indexes without rewriting source Markdown. That fits this structure. fileciteturn0file0 fileciteturn0file2
> 
> :::writing{variant="standard" id="51984"}
> ---
> title: QiLabs Full Tree
> section: qilabs/10_qispark/01_nav
> access_level: L1
> visibility: private
> ai_ingest: true
> status: final_candidate
> last_updated: 2026-06-20
> mindmap-plugin: basic
> ---
> 
> # qilabs
> 
> ## 00_qilabs.workspace
> 
> ### _root
> - why.qilabs_workspace.md
> - readme.qilabs_workspace.md
> - quickstart.qilabs_workspace.md
> - changelog.qilabs_workspace.md
> - qilabs.code-workspace
> - justfile
> 
> ### .github
> 
> #### issue_template
> - architecture_change.md
> - bug_report.md
> - feature_request.md
> 
> #### workflows
> - ci.yml
> - docs.yml
> - lint.yml
> - migrations.yml
> - release.yml
> - test.yml
> 
> #### root
> - codeowners.github
> - pull_request_template.md
> 
> ### .qios
> - docs_compiler.config.json
> 
> ### .vscode
> - settings.json
> 
> ### 20_manifests
> - apps.manifest.json
> - connectors.manifest.json
> - domains.manifest.json
> - repos.manifest.json
> - services.manifest.json
> - storage.manifest.json
> 
> ### 30_configs
> - .editorconfig
> - .gitignore
> - repo.rules.json
> - tsconfig.root.json
> - eslint.config.mjs
> - tailwind.config.ts
> - postcss.config.js
> - env.workspace.example.env
> 
> ### 50_toolkit
> - bootstrap_workspace.ps1
> - check_root_clean.ps1
> - export_file_inventory.ps1
> - generate_tree.ps1
> - tree_snapshot.ps1
> - verify_env.ps1
> 
> ### 99_quarantine
> - hold_only_until_sorted
> 
> ## 10_qispark
> 
> ### _root
> - why.qispark.md
> - readme.qispark_root.md
> - codex.qispark_ai.md
> - changelog.qispark.md
> 
> ### 00_obsidian
> 
> #### _root
> - why.qispark_obsidian.md
> - guide.qispark_obsidian.md
> 
> #### .obsidian
> - app.json
> - appearance.json
> - core-plugins.json
> - community-plugins.json
> - hotkeys.json
> - workspace.json
> 
> #### plugins
> - plugins.qispark_obsidian.md
> - plugins.qispark_required.md
> - plugins.qispark_optional.md
> 
> #### attachments
> - rules.qispark_attachments.md
> - inbox.attachments_qispark.md
> 
> #### canvas
> - map.qispark_canvas_index.md
> - canvas.qilabs_spine.canvas
> - canvas.qispark_nav.canvas
> 
> #### cadence
> - why.qispark_cadence.md
> - cadence.qispark_index.md
> - cadence.qispark_daily.md
> - cadence.qispark_weekly.md
> - cadence.qispark_monthly.md
> - cadence.qispark_review.md
> 
> ### 01_nav
> - why.qispark_nav.md
> - map.qispark_nav.md
>   - mirror_nav
>   - public_nav
>   - private_nav
>   - archive_nav
> - map.qispark_tree.md
>   - current_tree
>   - target_tree
>   - move_map
>   - rename_map
> - registry.qispark_nav.csv
> - registry.qispark_routes.csv
> - audit.qispark_nav.md
>   - bad_names
>   - duplicate_nodes
>   - stale_routes
>   - empty_placeholders
> 
> ### 10_qilabs.workspace
> - why.qispark_mirror_workspace.md
> - map.qilabs_workspace_current.md
> - map.qilabs_workspace_target.md
> - audit.qilabs_workspace_current_tree.md
>   - keep
>   - move
>   - delete
>   - quarantine
> - plan.qilabs_workspace_cleanup.md
>   - scripts_to_move
>   - configs_to_keep
>   - manifests_to_check
>   - quarantine_to_sort
> - rules.qilabs_workspace_scope.md
>   - setup_only
>   - configs
>   - extensions
>   - workspace_toolkit
>   - not_source_truth
>   - not_runtime
>   - not_kb
> - notes.qilabs_workspace_configs.md
>   - github
>   - qios
>   - vscode
>   - manifests
>   - repo_rules
>   - docs_compiler
> 
> ### 20_qispark
> 
> #### core
> - why.qispark_kb.md
> - guide.qispark_start.md
>   - what_this_is
>   - how_to_use_it
>   - what_lives_here
>   - what_does_not_live_here
>   - current_state
>   - next_moves
> - kb.qispark_context.md
>   - qilabs
>   - workspace
>   - qispark
>   - qiserver
>   - qidrive
>   - qiapps
>   - terms
>   - boundaries
> - kb.qispark_current_state.md
>   - locked
>   - changed
>   - still_fluid
>   - parked
> - kb.qispark_source_map.md
>   - what_counts
>   - what_does_not_count
>   - where_truth_lives
>   - where_records_live
>   - where_runtime_lives
> 
> #### life_stream
> - why.qispark_life_stream.md
> - timeline.qispark_life.md
>   - childhood
>   - resets
>   - housing
>   - work
>   - caregiving
>   - health
>   - relationships
>   - faith
>   - systems
> - events.qispark_life.md
>   - dated_events
>   - turning_points
>   - incidents
>   - wins
>   - losses
>   - unresolved
> - journal.qispark_current.md
>   - today
>   - this_week
>   - active_processing
>   - open_loops
> - journal.qispark_archive.md
>   - older_entries
>   - finished_threads
>   - raw_but_keep
> 
> #### creative
> - why.qispark_creative.md
> - creative.qispark_index.md
>   - sermons
>   - essays
>   - posts
>   - scripts
>   - fragments
>   - titles
> - sermons.qispark_drafts.md
>   - jesus_savage
>   - flip_the_table
>   - modern_parables
>   - faith_without_fluff
> - writing.qispark_fragments.md
>   - lines
>   - hooks
>   - analogies
>   - voice_notes
>   - unfinished
> - posts.qispark_social.md
>   - facebook
>   - linkedin
>   - captions
>   - drafts
> 
> #### symbols
> - why.qispark_symbols.md
> - symbols.qispark_713.md
>   - meaning
>   - appearances
>   - patterns
>   - caution_notes
>   - writing_uses
> - symbols.qispark_mirror.md
>   - mirror
>   - reflection
>   - reversal
>   - self_other
>   - perception
> - symbols.qispark_onions.md
>   - layers
>   - peeling
>   - hidden_core
>   - emotional_logic
> - symbols.qispark_lexicon.md
>   - recurring_words
>   - personal_terms
>   - metaphors
>   - phrases
>   - shorthand
> 
> #### narrative
> - why.qispark_narrative.md
> - narrative.qispark_identity.md
>   - who_i_am
>   - what_i_am_building
>   - what_i_refuse
>   - what_i_keep_learning
> - narrative.qispark_themes.md
>   - survival
>   - systems
>   - faith
>   - betrayal
>   - repair
>   - agency
>   - legacy
> - narrative.qispark_arcs.md
>   - origin_arc
>   - reset_arc
>   - builder_arc
>   - caregiver_arc
>   - liberation_arc
> 
> ### 30_qiserver
> - why.qispark_mirror_qiserver.md
> - map.qiserver_current.md
> - map.qiserver_target.md
> - plan.qiserver_from_workspace_scripts.md
>   - ai
>   - apps
>   - db
>   - deploy
>   - dev
>   - flow
>   - inbox
>   - ingest
>   - pdf
>   - process
>   - sync
>   - tools
> - audit.qiserver_script_routes.md
>   - keep_in_workspace
>   - move_to_qiserver
>   - merge
>   - delete
>   - quarantine
> - notes.qiserver_runtime.md
>   - fastapi
>   - ollama
>   - aider
>   - lancedb
>   - tmux
>   - ports
>   - env
> - map.qiserver_services.md
>   - qiconnect
>   - qimemory
>   - qiapi
>   - qillm
>   - qivector
> - map.qimemory_pipeline.md
>   - capture
>   - ingest
>   - summarize
>   - embed
>   - classify
>   - route
>   - recall
> 
> ### 40_qidrive
> - why.qispark_mirror_qidrive.md
> - map.qidrive_current.md
> - map.qidrive_target.md
> - plan.qidrive_from_qivault.md
>   - current_40_qivault
>   - target_30_qidrive
>   - rename_plan
>   - path_risks
>   - links_to_update
> - notes.qidrive_records.md
>   - identity
>   - legal
>   - money
>   - medical
>   - housing
>   - taxes
>   - benefits
> - notes.qidrive_evidence.md
>   - exhibits
>   - screenshots
>   - messages
>   - pdfs
>   - scans
>   - photos
>   - audio
>   - video
> - rules.qidrive_evidence.md
>   - evidence_lives_here
>   - docs_point_here
>   - do_not_duplicate_in_qispark
>   - redact_before_public
> 
> ### 50_qiapps
> - why.qispark_mirror_qiapps.md
> - map.qiapps_current.md
> - map.qiapps_target.md
> - plan.qiapps_from_60_qiapps.md
>   - current_60_qiapps
>   - target_40_qiapps
>   - rename_plan
>   - app_boundaries
>   - links_to_update
> - spec.qiapps_qilife.md
>   - dashboard
>   - routines
>   - tasks
>   - money
>   - health
>   - legal
>   - gigi
> - spec.qiapps_qiconnect.md
>   - contacts
>   - messages
>   - clients
>   - vendors
>   - crm
>   - outreach
> - spec.qiapps_qinexus.md
>   - search
>   - retrieval
>   - records
>   - evidence
>   - semantic_index
> - spec.qiapps_qidna.md
>   - identity
>   - rules
>   - preferences
>   - memory
>   - ai_alignment
> - spec.qiapps_qiaccess.md
>   - accounts
>   - devices
>   - permissions
>   - recovery
>   - security
> 
> ### 60_rules
> - why.qispark_rules.md
> - rules.qispark_core.md
>   - truth
>   - leverage
>   - naming
>   - modularity
>   - ai_use
>   - human_override
> - rules.qispark_docs.md
>   - filenames
>   - folders
>   - markdown
>   - frontmatter
>   - links
>   - archive
> - rules.qispark_boundaries.md
>   - qispark_not_workspace
>   - qispark_not_server
>   - qispark_not_drive
>   - qispark_not_apps
>   - docs_not_evidence
>   - maps_not_runtime
> - rules.qispark_access.md
>   - access_level
>   - visibility
>   - ai_ingest
>   - status
>   - sensitive_info
>   - public_private
> 
> ### 70_prompts
> - prompts.qispark_build.md
>   - nav_cleanup
>   - folder_reconcile
>   - docs_generate
>   - frontmatter_audit
> - prompts.qispark_extract.md
>   - extract_nav
>   - extract_decisions
>   - extract_tasks
>   - find_contradictions
>   - check_privacy
> - prompts.qispark_write.md
>   - clean_doc
>   - compress_notes
>   - make_timeline
>   - make_plan
>   - make_message
> 
> ### 80_ops
> - ops.qispark_maintenance.md
>   - add_page
>   - update_nav
>   - deprecate_page
>   - archive_content
>   - audit
>   - reconcile_names
> - ops.qispark_publish.md
>   - route_check
>   - private_check
>   - broken_links
>   - export_review
>   - handoff_to_qiserver
> 
> ### 90_runtime
> - why.qispark_runtime.md
> - runtime.qispark_obsidian.md
>   - vault_open
>   - plugin_state
>   - cadence_state
>   - active_file
>   - workspace_layout
> - runtime.qispark_ai.md
>   - active_prompt
>   - active_context
>   - ingest_ready
>   - export_ready
> - runtime.qispark_publish.md
>   - docs_compile
>   - route_check
>   - private_check
>   - output_handoff
> 
> ### 91_ref
> - ref.qispark_tables.md
>   - glossary
>   - canonical_names
>   - root_index
>   - route_index
>   - access_values
>   - visibility_values
>   - ingest_values
>   - status_values
> - ref.qispark_legacy_names.md
>   - qivault_to_qidrive
>   - qiapps_old_60
>   - qicapture_to_qimemory
>   - cloudflare_not_root
>   - old_99_system_removed
> 
> ### 98_archive
> - archive.qispark_legacy.md
>   - old_nav
>   - old_names
>   - deprecated_pages
>   - removed_routes
>   - legacy_qios
> 
> ## 20_qiserver
> 
> ### _root
> - why.qiserver.md
> - readme.qiserver_root.md
> - codex.qiserver_ai.md
> - changelog.qiserver.md
> - env.qiserver.example.env
> - justfile
> 
> ### 00_config
> - config.qiserver_runtime.json
> - config.qiserver_paths.json
> - config.qiserver_ports.json
> - config.qiserver_services.json
> - config.qiserver_secrets.example.json
> 
> ### 10_runtime
> 
> #### local
> - run.qiserver_dev.ps1
> - run.qiserver_dev.sh
> - run.qiserver_agent.ps1
> - run.qiserver_workers.ps1
> - check.qiserver_env.ps1
> - check.qiserver_env.sh
> 
> #### api
> - app.qiserver_fastapi.py
> - routes.qiserver_health.py
> - routes.qiserver_services.py
> - routes.qiserver_webhooks.py
> 
> #### process
> - runner.qiserver_command.py
> - runner.qiserver_service.py
> - runner.qiserver_worker.py
> - scheduler.qiserver_windows_task.xml
> - scheduler.qiserver_install.ps1
> 
> ### 20_data
> 
> #### sqlite
> - schema.qiserver_sqlite.md
> - migrate.qiserver_sqlite.ps1
> - seed.qiserver_sqlite.ps1
> - reset.qiserver_sqlite.ps1
> - start.qiserver_sqlite.ps1
> - stop.qiserver_sqlite.ps1
> 
> #### supabase
> - schema.qiserver_supabase.md
> - migrate.qiserver_supabase.ps1
> - validate.qiserver_supabase.py
> - log.qiserver_supabase_error.py
> 
> #### csv
> - pipeline.qiserver_csv_import.md
> - convert.qiserver_csv_to_md.py
> - validate.qiserver_csv.py
> - compare.qiserver_csv_md.py
> 
> #### vectors
> - schema.qiserver_vectors.md
> - build.qiserver_vector_index.py
> - search.qiserver_vectors.py
> - sync.qiserver_vectors.py
> 
> ### 30_services
> 
> #### qiapi
> - why.qiapi.md
> - service.qiapi.md
> - routes.qiapi.py
> - auth.qiapi_check.ps1
> - health.qiapi.py
> 
> #### qillm
> - why.qillm.md
> - service.qillm.md
> - models.qillm.py
> - prompts.qillm.py
> - rag.qillm_core.py
> 
> #### qivector
> - why.qivector.md
> - service.qivector.md
> - index.qivector_build.py
> - search.qivector_docs.py
> - sync.qivector_index.py
> 
> #### qimemory
> - why.qimemory.md
> - service.qimemory.md
> 
> ##### capture
> - capture.qimemory_audio.py
> - capture.qimemory_files.py
> - capture.qimemory_web.py
> - capture.qimemory_screenshots.py
> 
> ##### inbox
> - audit.qimemory_inbox.ts
> - normalize.qimemory_inbox.ts
> - dedup.qimemory_inbox.ts
> - rename.qimemory_inbox.py
> - run.qimemory_inbox.ts
> 
> ##### ingest
> - ingest.qimemory_audio.py
> - ingest.qimemory_files.py
> - ingest.qimemory_pdf.ts
> - ingest.qimemory_video.py
> - ingest.qimemory_web.py
> 
> ##### process
> - process.qimemory_clean.py
> - process.qimemory_normalize.py
> - process.qimemory_summarize.py
> - process.qimemory_classify.py
> - process.qimemory_route.py
> - process.qimemory_embed.py
> 
> ##### recall
> - recall.qimemory_search.py
> - recall.qimemory_context.py
> - recall.qimemory_profile.py
> 
> #### qiconnect
> - why.qiconnect_server.md
> - service.qiconnect.md
> 
> ##### contacts
> - service.qiconnect_contacts.py
> - sync.qiconnect_contacts.py
> 
> ##### mail
> - service.qiconnect_mail.py
> - get.qiconnect_mail_recent.py
> - send.qiconnect_mail.py
> 
> ##### calendar
> - service.qiconnect_calendar.py
> - get.qiconnect_calendar_upcoming.py
> - create.qiconnect_calendar_event.py
> 
> ##### sms
> - service.qiconnect_sms.py
> - send.qiconnect_sms.py
> 
> ##### web
> - service.qiconnect_web.py
> - get.qiconnect_web.py
> - search.qiconnect_web.py
> 
> ##### cloudflare
> - why.qiconnect_cloudflare.md
> - service.qiconnect_cloudflare.md
> - deploy.qiconnect_cloudflare.ps1
> - deploy.qiconnect_workers.ps1
> - get.qiconnect_worker_urls.ps1
> - routes.qiconnect_cloudflare.json
> - redirects.qiconnect_cloudflare.json
> 
> ### 40_apps_runtime
> 
> #### qilife
> - service.qilife_runtime.md
> - routes.qilife_api.py
> - jobs.qilife_sync.py
> 
> #### qinexus
> - service.qinexus_runtime.md
> - routes.qinexus_search.py
> - jobs.qinexus_index.py
> 
> #### qidna
> - service.qidna_runtime.md
> - routes.qidna_profile.py
> - jobs.qidna_sync.py
> 
> #### qiaccess
> - service.qiaccess_runtime.md
> - routes.qiaccess_auth.py
> - jobs.qiaccess_check.py
> 
> ### 50_jobs
> 
> #### sync
> - job.qiserver_sync.py
> - sync.qiserver_git.py
> - sync.qiserver_gdrive.py
> - sync.qiserver_index.ts
> 
> #### backup
> - job.qiserver_backup.py
> - backup.qiserver_data.ps1
> - restore.qiserver_data.ps1
> 
> #### ingest
> - job.qiserver_ingest.py
> - queue.qiserver_ingest.py
> 
> #### cleanup
> - job.qiserver_cleanup.py
> - clean.qiserver_storage.py
> - clean.qiserver_duplicates.py
> 
> #### deploy
> - job.qiserver_deploy.py
> - deploy.qiserver_all.ps1
> - deploy.qiserver_critical.ps1
> 
> ### 60_tools
> 
> #### repo
> - validate.qiserver_paths.py
> - lint.qiserver_tree.py
> - enforce.qiserver_structure.py
> - print.qiserver_tree.py
> 
> #### frontmatter
> - add.qiserver_frontmatter.py
> - validate.qiserver_frontmatter.ts
> - enforce.qiserver_frontmatter.py
> 
> #### maps
> - map.qiserver_tree.py
> - map.qiserver_slugs.py
> 
> #### debug
> - debug.qiserver_maps.py
> - test.qiserver_pipeline.ps1
> - verify.qiserver_env.ps1
> - verify.qiserver_env.sh
> 
> ### 70_logs
> - logs.qiserver.md
>   - runtime
>   - errors
>   - deploy
>   - ingest
>   - memory
>   - sync
> 
> ### 80_ops
> - ops.qiserver_maintenance.md
>   - setup
>   - start
>   - stop
>   - restart
>   - backup
>   - restore
>   - troubleshoot
> - ops.qiserver_deploy.md
>   - local
>   - cloudflare
>   - rollback
>   - env_check
> - ops.qiserver_migration_from_workspace.md
>   - scripts_to_move
>   - scripts_to_merge
>   - scripts_to_delete
>   - scripts_to_quarantine
> 
> ### 90_rules
> - rules.qiserver_scope.md
>   - runtime_lives_here
>   - services_live_here
>   - secrets_never_public
>   - qiserver_not_kb
>   - qiserver_not_drive
>   - qiserver_not_workspace
>   - logs_not_docs
>   - do_not_put_here
> 
> ## 30_qidrive
> <!-- currently: 40_qivault -->
> 
> ### _root
> - why.qidrive.md
> - readme.qidrive_root.md
> - changelog.qidrive.md
> - rules.qidrive_scope.md
> 
> ### 00_index
> - index.qidrive_records.md
> - index.qidrive_evidence.md
> - index.qidrive_exports.md
> - index.qidrive_mirrors.md
> 
> ### 10_records
> 
> #### identity
> - why.identity.md
> - ids
> - licenses
> - social_security
> - immigration
> 
> #### legal
> - why.legal.md
> - claims
> - notices
> - filings
> - court
> - contracts
> 
> #### money
> - why.money.md
> - income
> - bills
> - taxes
> - disputes
> - receipts
> 
> #### medical
> - why.medical.md
> - visits
> - prescriptions
> - insurance
> - hospital
> - care
> 
> #### housing
> - why.housing.md
> - lease
> - utilities
> - repairs
> - notices
> - photos
> 
> ### 20_evidence
> 
> #### exhibits
> - why.exhibits.md
> - active
> - final
> - sent
> - archived
> 
> #### screenshots
> - why.screenshots.md
> - messages
> - websites
> - apps
> - receipts
> - errors
> 
> #### messages
> - why.messages.md
> - sms
> - email
> - messenger
> - whatsapp
> - transcripts
> 
> #### pdfs
> - why.pdfs.md
> - forms
> - letters
> - notices
> - records
> - packets
> 
> #### media
> - why.media.md
> - photos
> - audio
> - video
> - scans
> 
> ### 30_drive_mirror
> 
> #### google_drive
> - why.google_drive.md
> - my_drive
> - shared_with_me
> - exports
> - upload_queue
> 
> #### local_mirror
> - why.local_mirror.md
> - active_sync
> - offline_cache
> - restore_points
> 
> #### archive_mirror
> - why.archive_mirror.md
> - cold_storage
> - old_exports
> - deprecated_sets
> 
> ### 40_exports
> 
> #### packets
> - why.packets.md
> - legal_packets
> - exhibit_packets
> - client_packets
> - admin_packets
> 
> #### machine_exports
> - why.machine_exports.md
> - csv
> - json
> - markdown
> - zip
> 
> ### 50_pointers
> - pointers.qidrive_files.csv
> - pointers.qidrive_evidence.csv
> - pointers.qidrive_records.csv
> 
> ### 90_rules
> - rules.qidrive_access.md
>   - private_by_default
>   - redact_before_public
>   - qidrive_holds_blobs
>   - qispark_holds_meaning
>   - qiserver_indexes_and_processes
>   - qiapps_request_through_qiserver
> 
> ## 40_qiapps
> <!-- currently: 60_qiapps -->
> 
> ### _root
> - why.qiapps.md
> - readme.qiapps_root.md
> - changelog.qiapps.md
> - rules.qiapps_scope.md
> 
> ### 00_shared
> 
> #### ui
> - why.shared_ui.md
> - components
> - layouts
> - themes
> - icons
> 
> #### config
> - config.qiapps_shared.json
> - config.qiapps_routes.json
> 
> #### patterns
> - patterns.qiapps_navigation.md
> - patterns.qiapps_cards.md
> - patterns.qiapps_forms.md
> 
> ### 10_qilife
> - why.qilife.md
> - spec.qilife_app.md
> - map.qilife_flows.md
> - backlog.qilife.md
> 
> #### ui
> - dashboard
> - routines
> - tasks
> - money
> - health
> - legal
> - gigi
> 
> #### config
> - config.qilife_routes.json
> - config.qilife_views.json
> 
> ### 20_qiconnect
> - why.qiconnect.md
> - spec.qiconnect_app.md
> - map.qiconnect_flows.md
> - backlog.qiconnect.md
> 
> #### ui
> - contacts
> - messages
> - clients
> - vendors
> - crm
> - outreach
> 
> #### config
> - config.qiconnect_routes.json
> - config.qiconnect_views.json
> 
> ### 30_qinexus
> - why.qinexus.md
> - spec.qinexus_app.md
> - map.qinexus_flows.md
> - backlog.qinexus.md
> 
> #### ui
> - search
> - retrieval
> - records
> - evidence
> - semantic_index
> 
> #### config
> - config.qinexus_routes.json
> - config.qinexus_views.json
> 
> ### 40_qidna
> - why.qidna.md
> - spec.qidna_app.md
> - map.qidna_flows.md
> - backlog.qidna.md
> 
> #### ui
> - identity
> - rules
> - preferences
> - memory
> - ai_alignment
> 
> #### config
> - config.qidna_routes.json
> - config.qidna_views.json
> 
> ### 50_qiaccess
> - why.qiaccess.md
> - spec.qiaccess_app.md
> - map.qiaccess_flows.md
> - backlog.qiaccess.md
> 
> #### ui
> - accounts
> - devices
> - permissions
> - recovery
> - security
> 
> #### config
> - config.qiaccess_routes.json
> - config.qiaccess_views.json
> 
> ### 90_rules
> - rules.qiapps_boundaries.md
>   - apps_not_server_runtime
>   - apps_not_drive_storage
>   - apps_not_kb
>   - api_calls_go_to_qiserver
>   - files_come_from_qidrive_pointers
>   - docs_live_in_qispark
> :::
> 
> ## Immediate audit cuts
> 
> Before making this real, cut these unless they are already useful:
> 
> | Area | Cut unless needed now |
> |---|---|
> | `00_qilabs.workspace/20_manifests` | any empty `{}` manifest not read by a script |
> | `10_qispark/98_archive` | if there is no actual legacy material |
> | `30_qidrive/50_pointers` | until pointers are actively being generated |
> | `40_qiapps/*/config` | until those apps are actually being wired |
> | `20_qiserver/* placeholder service files` | unless they map to existing scripts being moved |
> 
> The spine is now right:
> 
> ```text
> 00_qilabs.workspace = setup/toolkit
> 10_qispark = Obsidian + Markdown brain + life/creative/narrative layer
> 20_qiserver = runtime/services/qimemory/cloudflare
> 30_qidrive = Google Drive/blob/evidence/storage
> 40_qiapps = app shells/specs/UI layer
> ```

### User
> quick question what is the different between obsidian with a cadence plugin or similiar and affine, ???

### Assistant
> I’ll give you the practical difference, not a feature spreadsheet. The real question is: **which one should be your system brain vs visual/project workspace.**

### Assistant
> ## Clean difference
> 
> **Obsidian + Cadence** is better for your **QiSpark brain**.
> 
> **AFFiNE** is better for **visual planning, whiteboards, and collaborative project boards**.
> 
> They overlap, but they are not the same animal.
> 
> ---
> 
> # Obsidian + Cadence
> 
> Obsidian is basically:
> 
> ```text
> A folder of Markdown files
> +
> plugins
> +
> links/backlinks
> +
> canvas
> +
> local-first knowledge base
> ```
> 
> Obsidian is built around notes, vaults, Markdown, links, and extensibility. Obsidian’s newer Bases feature also lets you create database-like views from note properties, which matters for your nav/registry idea. citeturn731460search0turn731460search11
> 
> Cadence specifically is an Obsidian plugin/workspace approach for CRM, PRM, project management, daily planning, reminders, reports, and projects on top of plain Markdown. Its own description says it uses Markdown as the source of truth with no server/sync lock-in. citeturn731460search4turn731460search13
> 
> ## Translation for you
> 
> Obsidian + Cadence is best for:
> 
> ```text
> QiSpark
> journals
> daily/weekly cadence
> life timeline
> sermons
> symbols
> 713 / mirror / onion language
> rules
> frontmatter
> AI-ingestable Markdown
> Git/versioned knowledge
> local file control
> ```
> 
> The killer advantage: **your data is just files**.
> 
> That means it fits your architecture:
> 
> ```text
> 10_qispark = Markdown vault
> 20_qiserver = process/index it
> 30_qidrive = store blobs
> 40_qiapps = display/use it
> ```
> 
> No mystery database goblin hiding your brain in an app blob.
> 
> ---
> 
> # AFFiNE
> 
> AFFiNE is closer to:
> 
> ```text
> Notion + Miro + docs + whiteboard + database-ish workspace
> ```
> 
> AFFiNE describes itself as open-source, local-first knowledge base software combining docs, whiteboards, databases, and AI in one workspace. Its GitHub describes it as a privacy-focused, local-first, open-source alternative to Notion and Miro, with docs, canvas, and tables merged together. citeturn731460search8turn731460search17
> 
> AFFiNE is stronger when you want:
> 
> ```text
> big visual boards
> project planning
> whiteboard thinking
> diagrams
> team collaboration
> drag/drop docs + tables + canvas together
> presentation-ish planning
> ```
> 
> Its Edgeless/whiteboard mode is the main appeal. It is better when the structure is spatial, not textual. citeturn731460search18
> 
> ---
> 
> # The real decision
> 
> ## Use Obsidian when the thing is source truth
> 
> Use Obsidian for anything you want to become part of QiSpark’s durable brain:
> 
> ```text
> doctrine
> timeline
> journals
> creative writing
> rules
> decisions
> navigation
> frontmatter
> Markdown KB
> AI context
> ```
> 
> ## Use AFFiNE when the thing is a visual workspace
> 
> Use AFFiNE for:
> 
> ```text
> brainstorm boards
> visual strategy maps
> client journey maps
> app mock planning
> relationship diagrams
> workflow sketches
> messy spatial thinking
> ```
> 
> But I would **not** make AFFiNE the canonical QiSpark source.
> 
> Why? Because your whole system is becoming file/path/Markdown/frontmatter driven. Obsidian aligns with that. AFFiNE is more of a beautiful thinking surface.
> 
> ---
> 
> # My recommendation for your system
> 
> ```text
> Obsidian = QiSpark home base
> AFFiNE = optional visual lab
> ```
> 
> Use them like this:
> 
> | Layer | Tool | Why |
> |---|---|---|
> | Source truth Markdown | Obsidian | plain files, Git, frontmatter, AI-friendly |
> | Cadence/daily workflow | Obsidian + Cadence | daily/weekly rhythm inside the vault |
> | Life timeline/journals | Obsidian | searchable durable personal KB |
> | Sermons/713/mirror/onions | Obsidian | symbolic/narrative library |
> | Visual boards | AFFiNE | better canvas/whiteboard feel |
> | Final system maps | Obsidian/MarkMind/Canvas | closer to repo/nav structure |
> | Collaborative presentation boards | AFFiNE | smoother visual workspace |
> 
> ---
> 
> # Blunt answer
> 
> Do **not** replace Obsidian with AFFiNE for QiSpark.
> 
> That would be seductive but wrong.
> 
> AFFiNE is nicer for visual thinking. Obsidian is better for your actual architecture because QiSpark needs to be:
> 
> ```text
> portable
> parseable
> versionable
> AI-ingestable
> path-based
> frontmatter-aware
> Git-friendly
> ```
> 
> AFFiNE can be a side room.  
> Obsidian is the house.
