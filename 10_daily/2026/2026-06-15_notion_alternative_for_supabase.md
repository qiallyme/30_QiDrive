---
layout: page
title: "Notion Alternative for Supabase"
slug: "notion_alternative_for_supabase"
created_at: "2026-06-15 08:29:15"
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
date: 2026-06-15
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a2ffe14-949c-83ea-9163-357743caa64a"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Notion Alternative for Supabase

## Overview
- **Date**: 2026-06-15 08:29:15
- **Conversation ID**: `6a2ffe14-949c-83ea-9163-357743caa64a`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> ok i feel like if i try to use notion again im giong to drive myself crazy, what alternative do i have today that can still integrate or migrate to supabase.

### Assistant
> You’re right to avoid Notion today. It’s powerful, but for your current state it will become a “decorate the operating system” trap instead of getting data into the system. I’ll ground this around **fast capture now + clean migration to Supabase later**.

### Assistant
> Yes. **Do not use Notion today.** It will absolutely turn into a shrine-building exercise and eat your brain.
> 
> ## Best alternative today: **Google Sheets as staging + Supabase as the real database**
> 
> That is the cleanest move.
> 
> Why:
> 
> - **Fastest capture layer**
> - Easy dropdowns / conditional formatting
> - Easy CSV export
> - Easy for you to inspect without building UI
> - Supabase can import CSV directly into tables through the Table Editor. citeturn992409search0
> - Supabase auto-generates APIs from your database schema later, so the sheet can disappear once the app/admin UI exists. citeturn992409search1
> - Google Sheets has a real API and Apps Script if you later want automation. citeturn598050search0turn598050search1
> 
> ## My recommendation
> 
> Use this stack:
> 
> ```text
> Obsidian = narrative / docs / plans / human-readable notes
> Google Sheets = structured staging tables
> Supabase = canonical database
> GitHub repo = schema, migrations, docs, scripts
> ```
> 
> That gives each tool one job. No blurry Notion chaos.
> 
> ## Today’s setup
> 
> Create one Google Sheet:
> 
> ```text
> QiSystem_Staging
> ```
> 
> Tabs:
> 
> | Tab | Purpose | Later Supabase table |
> |---|---|---|
> | `00_inbox` | Dump anything fast | `stg_inbox` |
> | `10_people_orgs` | people, companies, agencies, doctors, vendors | `people`, `organizations` |
> | `20_transactions` | money imports, Firefly exports, COA work | `transactions`, `accounts`, `categories`, `tags` |
> | `30_care_events` | mom care events, hospitalizations, calls, meds notes | `care_events` |
> | `40_documents` | files, evidence, PDFs, letters, receipts | `documents` |
> | `50_tasks` | follow-ups, calls, deadlines | `tasks` |
> | `90_lookup_values` | statuses, types, tags, categories | lookup tables |
> 
> ## Universal columns for every tab
> 
> Use these first so migration stays sane:
> 
> ```text
> entry_id
> created_at
> source_system
> source_file
> record_type
> title
> description
> event_date
> person
> organization
> amount
> category
> tags
> status
> priority
> supabase_target_table
> migration_status
> notes
> ```
> 
> For `migration_status`, use a dropdown:
> 
> ```text
> new
> needs_cleanup
> ready_to_import
> imported
> archived
> ```
> 
> ## Best no-code-ish alternatives ranked
> 
> | Tool | Use it? | Why |
> |---|---:|---|
> | **Google Sheets** | **Yes, today** | Fastest, cleanest, lowest-friction staging layer |
> | **Supabase Studio directly** | Yes, after schema exists | Good canonical DB editor, not great for messy capture |
> | **NocoDB** | Maybe later | Can connect to external PostgreSQL, so it can sit over Supabase/Postgres if configured carefully. citeturn992409search3 |
> | **Baserow** | Maybe, but not first | Nice Airtable-like database; exports CSV/JSON and has API, but it becomes another database to migrate. citeturn992409search22turn992409search23 |
> | **Airtable** | Avoid unless necessary | Polished, but can become a paid silo. Not worth it for your current goal |
> | **Retool/Appsmith** | Later | Better once Supabase schema exists and you need an admin dashboard |
> 
> ## The blunt call
> 
> **Use Google Sheets today.**  
> Not because it is sexy. Because it is boring, portable, and hard to over-romanticize.
> 
> Your real architecture should be:
> 
> ```text
> Messy reality → Google Sheets staging → cleaned CSV/import script → Supabase canonical tables → app/admin UI
> ```
> 
> Not:
> 
> ```text
> Messy reality → Notion → dashboards → templates → vibes → existential collapse
> ```
> 
> For today, build the staging sheet and start entering data. Supabase comes after the columns stabilize.

### User
> they are saying online is to use affine, it can even be self hosted.

### Assistant
> AFFiNE is worth checking, but we need to separate **“cool Notion/whiteboard replacement”** from **“good Supabase staging layer.”** I’ll verify what it actually supports now and then give you the practical call.

### Assistant
> People online are **not wrong**. AFFiNE is a real option. But here’s the sharp distinction:
> 
> ## AFFiNE is good for **thinking**.  
> ## Supabase is good for **truth**.
> 
> AFFiNE combines docs, whiteboards, databases, and AI in a local-first workspace, and it is positioned as an open-source Notion/Miro alternative. It also supports self-hosting, including Docker-based deployment with Postgres/Redis per its docs/search results. citeturn388488view4turn388488view3turn501305search0
> 
> But I would **not** make AFFiNE your main Supabase staging layer today.
> 
> Why? Because AFFiNE’s internal data model is its own workspace/block/collaboration system, not your clean `people`, `transactions`, `care_events`, `documents`, `tasks` schema. Their own roadmap says they are **working toward** direct Markdown-file workflows, which means that open-file interoperability is still an evolving direction, not something I’d bet your canonical system on today. citeturn388488view2
> 
> ## My call
> 
> Use AFFiNE like this:
> 
> ```text
> AFFiNE = visual thinking, maps, planning, dashboards, project brain
> Supabase = canonical data
> Google Sheets / CSV = fast staging/import layer
> Obsidian = long-form notes, care docs, evidence narratives
> ```
> 
> Do **not** use AFFiNE as:
> 
> ```text
> Primary database
> Migration authority
> Financial transaction staging layer
> Medical/care event source of truth
> Supabase schema source
> ```
> 
> That path gets cute fast. Cute is the enemy right now.
> 
> ## Where AFFiNE actually fits for you
> 
> AFFiNE could be excellent for:
> 
> | Use Case | Good Fit? | Why |
> |---|---:|---|
> | QiOS system maps | **Yes** | Whiteboard + docs together |
> | Mom care plan overview | **Yes** | Visual dashboard / timeline / care map |
> | App architecture thinking | **Yes** | Better than Notion for canvas-style reasoning |
> | Daily command center | Maybe | Only if you keep it brutally simple |
> | Supabase data staging | **No** | Too indirect and likely to create migration friction |
> | Firefly/finance category normalization | **No** | Needs tables/CSV/Supabase, not blocks |
> | Legal/evidence packet tracking | Maybe | Good as visual index, not source of record |
> 
> ## Better architecture
> 
> ```text
> Capture messy thoughts → AFFiNE / Obsidian
> Capture structured rows → Google Sheets
> Clean/import → Supabase
> Display/manage later → custom app, NocoDB, Retool, or Supabase Studio
> ```
> 
> ## The exact rule
> 
> Use **AFFiNE for pages and maps**.
> 
> Use **Google Sheets for rows**.
> 
> Use **Supabase for records**.
> 
> That means:
> 
> ```text
> AFFiNE page:
> "Mom Care System Overview"
> 
> Links to:
> - Google Sheet: care event staging
> - Supabase table: care_events
> - Obsidian folder: Mom_Care_Plan
> - GitHub schema file: care_schema.sql
> ```
> 
> AFFiNE becomes the **control room**, not the warehouse.
> 
> ## Should you self-host it today?
> 
> Bluntly: **No, not today.**
> 
> Self-hosting is powerful, but today it adds:
> 
> - Docker
> - updates
> - volumes
> - Postgres
> - Redis
> - backups
> - auth
> - domain/config headaches
> 
> That’s another rabbit hole wearing a cute open-source hat.
> 
> Use AFFiNE desktop/cloud first to test the workflow. If it proves useful for two weeks, then self-host. Not before.
> 
> ## Today’s move
> 
> Set up this stack:
> 
> ```text
> 1. AFFiNE
>    Workspace: QiOS Command Center
> 
> 2. Google Sheet
>    File: QiSystem_Staging
> 
> 3. Supabase
>    Project: canonical database
> 
> 4. Obsidian
>    Vault/folder: human docs, care plan, evidence, long notes
> ```
> 
> Inside AFFiNE, make only **five pages**:
> 
> ```text
> 00_Command_Center
> 10_QiSystem_Map
> 20_Mom_Care_Map
> 30_Finance_Data_Map
> 40_App_Backlog
> ```
> 
> That’s it. No templates festival. No aesthetic productivity cosplay.
> 
> ## Final verdict
> 
> AFFiNE is a **yes** as a Notion alternative.
> 
> AFFiNE is a **no** as your Supabase migration backbone.
> 
> Your backbone should still be:
> 
> ```text
> CSV / Sheets → Supabase migrations/imports → app UI
> ```
> 
> AFFiNE can sit on top as the visual brain. Not underneath as the data foundation.

### User
> https://docs.affine.pro/self-host-affine/ we should be able to link the affine to the supabase as its postgres etc.

### Assistant
> Yes — **technically, we should be able to point self-hosted AFFiNE at Supabase Postgres**.
> 
> But the important correction is:
> 
> ## That does **not** mean AFFiNE becomes your Supabase data layer.
> 
> It means:
> 
> ```text
> AFFiNE app → uses Supabase Postgres as AFFiNE’s internal database
> ```
> 
> Not:
> 
> ```text
> AFFiNE pages/databases → cleanly become your QiSystem tables
> ```
> 
> AFFiNE will still create and manage **its own internal tables/migrations**. You’d be using Supabase as the storage backend for AFFiNE, not as a clean bridge into your canonical app schema.
> 
> ## The practical read
> 
> AFFiNE’s self-host setup uses Docker Compose with AFFiNE server plus dependencies like **Postgres**, **Redis**, persistent storage, and config. Its compose examples use a `DATABASE_URL` pointing to Postgres and `REDIS_SERVER_HOST` pointing to Redis. citeturn100464search1turn100464search0
> 
> Supabase does provide normal Postgres connection strings. For a long-running container like AFFiNE, Supabase says the **direct connection** is best for persistent backend services, while the **session pooler** is the fallback for IPv4-only environments. Do **not** use transaction pooling unless you know AFFiNE’s DB client is compatible, because Supabase says transaction mode does not support prepared statements. citeturn151842view2
> 
> ## My architecture call
> 
> ### Best version
> 
> ```text
> Supabase Project 1: qisupabase
> Canonical QiSystem data
> - people
> - orgs
> - transactions
> - care_events
> - documents
> - tasks
> - tags
> - categories
> 
> Supabase Project 2: affine_backend
> AFFiNE internal app database only
> - AFFiNE tables
> - AFFiNE migrations
> - AFFiNE user/workspace/doc metadata
> ```
> 
> Do **not** put AFFiNE’s internal tables inside your main QiSystem Supabase project. That’s asking for schema clutter and migration hell.
> 
> ## Why separate projects?
> 
> Because AFFiNE is not a table editor. It is a whole application with its own backend assumptions.
> 
> Risks if you point AFFiNE at your main Supabase database:
> 
> | Risk | Why it matters |
> |---|---|
> | **Schema pollution** | AFFiNE creates internal tables you do not control |
> | **Migration collisions** | AFFiNE migrations and your app migrations live in the same DB |
> | **Backup confusion** | Restoring AFFiNE could accidentally affect canonical data |
> | **Security confusion** | Supabase RLS/auth assumptions are not the same as AFFiNE’s app auth |
> | **False integration** | You may think AFFiNE data is usable app data when it is really block/workspace internals |
> 
> Also, Supabase hosted Postgres does **not** give full superuser access. Supabase says the default `postgres` role is provided, but true superuser access is withheld, and some superuser-only operations are unsupported. That may or may not matter for AFFiNE, but it is another reason to isolate experiments. citeturn113396view0
> 
> ## So yes, but here’s the sane plan
> 
> ### Phase 1 — Test AFFiNE normally
> 
> Run AFFiNE with its default Docker Postgres first.
> 
> ```text
> AFFiNE → local Docker Postgres
> ```
> 
> Goal: confirm you even like the workflow.
> 
> ### Phase 2 — Move AFFiNE DB to separate Supabase project
> 
> Create a separate Supabase project:
> 
> ```text
> affine_backend
> ```
> 
> Then modify AFFiNE’s compose/env so:
> 
> ```text
> DATABASE_URL=Supabase direct/session connection string
> REDIS_SERVER_HOST=local Redis container
> storage/config=local mounted volumes
> ```
> 
> Keep Redis local unless you want another managed dependency.
> 
> ### Phase 3 — Link AFFiNE to QiSystem by references, not database merging
> 
> Inside AFFiNE pages, link to:
> 
> ```text
> Supabase table docs
> Google Sheet staging docs
> Obsidian care notes
> GitHub schema files
> QiSystem dashboards
> ```
> 
> AFFiNE becomes the **command room**.
> 
> Supabase remains the **source of truth**.
> 
> ## The blunt verdict
> 
> You’re right that this is possible.
> 
> But do **not** treat it as a magic Notion-to-Supabase bridge. That’s the trap.
> 
> Use it like this:
> 
> ```text
> AFFiNE = visual operating room
> Supabase = canonical database
> Sheets/CSV = migration staging
> Obsidian = durable notes/docs
> ```
> 
> The clean move today:
> 
> ```text
> 1. Self-host AFFiNE with default Docker Postgres first.
> 2. Test whether it helps or distracts.
> 3. If useful, create separate Supabase project just for AFFiNE.
> 4. Keep QiSystem canonical data in qisupabase.
> ```
> 
> That gives you flexibility without letting AFFiNE squat inside your real database like a raccoon in the walls.

### User
> ok, if we cant pipe the actual tables like how i describes then it can stay live in the container and we can use qiconnect for a workflow integration to update or mirror the data in supabase since that is our source of turth.

### Assistant
> That’s the correct pivot. The move is **not database-level coupling**; it’s **workflow-level integration**, with QiConnect acting like the translator/bus between AFFiNE and Supabase.

### Assistant
> Exactly. **That is the sane architecture.**
> 
> AFFiNE can live in its own container with its own internal Postgres/Redis stack. Official AFFiNE positioning is docs + whiteboards + databases in a local-first workspace, and it supports self-hosted Docker deployment. citeturn294052view2 The self-host docs also treat Postgres/storage backup as AFFiNE infrastructure, which reinforces the point: that DB is AFFiNE’s app brain, not our canonical business schema. citeturn382992search0turn382992search12
> 
> ## Correct model
> 
> ```text
> AFFiNE container
>   ↓
> AFFiNE internal Postgres
>   ↓
> QiConnect adapter / workflow layer
>   ↓
> Supabase canonical tables
> ```
> 
> Not this:
> 
> ```text
> AFFiNE tables = QiSystem tables
> ```
> 
> That second one is messy. We don’t need it.
> 
> ---
> 
> # Final architecture call
> 
> ## AFFiNE’s job
> 
> AFFiNE becomes the **visual workspace / command room**:
> 
> ```text
> maps
> dashboards
> planning boards
> care overviews
> system diagrams
> project notes
> whiteboards
> ```
> 
> ## Supabase’s job
> 
> Supabase remains the **source of truth**:
> 
> ```text
> people
> organizations
> care_events
> tasks
> documents
> transactions
> categories
> tags
> projects
> claims
> evidence
> ```
> 
> ## QiConnect’s job
> 
> QiConnect becomes the **bridge / translator / sync bus**:
> 
> ```text
> AFFiNE capture → QiConnect normalize → Supabase insert/update
> Supabase records → QiConnect summarize → AFFiNE dashboard/page reference
> ```
> 
> That is clean. That is modular. That does not let AFFiNE squat inside the sacred database like a glitter raccoon.
> 
> ---
> 
> # Direction of truth
> 
> This matters.
> 
> ## Allowed
> 
> ```text
> AFFiNE → staging/inbox → review → Supabase
> ```
> 
> Example:
> 
> You write a care note in AFFiNE:
> 
> ```text
> Mom had breathing issue after medication change.
> Need to call doctor.
> ```
> 
> QiConnect turns that into:
> 
> ```text
> record_type: care_event
> person: Mom
> event_type: medication_observation
> status: needs_review
> target_table: care_events
> ```
> 
> Then it goes into a Supabase staging table first.
> 
> ## Also allowed
> 
> ```text
> Supabase → AFFiNE summary/dashboard
> ```
> 
> Example:
> 
> Supabase has canonical records. QiConnect generates an AFFiNE page:
> 
> ```text
> Mom Care Dashboard
> - Open tasks
> - Recent hospitalizations
> - Medication questions
> - Next doctor call
> ```
> 
> ## Dangerous
> 
> ```text
> AFFiNE internal DB ↔ Supabase canonical DB
> ```
> 
> That becomes brittle because AFFiNE owns its internal schema. If AFFiNE updates, your sync can break.
> 
> ---
> 
> # QiConnect module shape
> 
> Put this under:
> 
> ```text
> C:\QiLabs\70_QiConnect\affine
> ```
> 
> Recommended structure:
> 
> ```text
> 70_QiConnect/
>   affine/
>     README.md
>     affine_adapter_spec.md
>     mappings/
>       affine_to_supabase.yml
>       supabase_to_affine.yml
>     scripts/
>       export_affine_capture.py
>       normalize_affine_capture.py
>       push_to_supabase.py
>       generate_affine_dashboard.py
>     logs/
>       .gitkeep
>     samples/
>       affine_capture_sample.json
>       supabase_payload_sample.json
> ```
> 
> ---
> 
> # Supabase tables we should add later
> 
> For the bridge itself:
> 
> ```text
> qiconnect_sources
> qiconnect_sync_runs
> qiconnect_sync_events
> qiconnect_external_refs
> qiconnect_mappings
> qiconnect_capture_inbox
> ```
> 
> The key table is:
> 
> ```text
> qiconnect_capture_inbox
> ```
> 
> That is where AFFiNE content lands **before** becoming real records.
> 
> Columns:
> 
> ```text
> id
> source_system
> source_workspace
> source_page_id
> source_block_id
> raw_title
> raw_text
> detected_record_type
> suggested_target_table
> normalized_payload
> confidence_score
> review_status
> created_at
> processed_at
> supabase_record_id
> notes
> ```
> 
> Review statuses:
> 
> ```text
> new
> needs_review
> approved
> synced
> rejected
> archived
> ```
> 
> ---
> 
> # The rule
> 
> ## AFFiNE is allowed to inspire records.
> 
> ## AFFiNE is not allowed to be the record.
> 
> That’s the whole architecture in one sentence.
> 
> ---
> 
> # Better naming
> 
> This integration should be called:
> 
> ```text
> QiConnect AFFiNE Bridge
> ```
> 
> or more formally:
> 
> ```text
> qiconnect_affine_bridge
> ```
> 
> Role:
> 
> ```text
> Visual workspace integration adapter for syncing AFFiNE notes, maps, and planning artifacts into Supabase-backed QiSystem records.
> ```
> 
> ---
> 
> # Today’s decision
> 
> Do this:
> 
> ```text
> 1. Run AFFiNE self-hosted in its own container stack.
> 2. Keep its internal Postgres local/container-managed.
> 3. Do not point it at qisupabase.
> 4. Add QiConnect bridge spec.
> 5. Use Supabase as the canonical truth.
> 6. Use AFFiNE for visual command-center work.
> ```
> 
> That’s the right split. Clean, powerful, not stupid.

### User
> ok, so help me get this on the server, quickly codex can do it this is one of the apps we use but its not our build, so does it go under system and services or under qiapps

### Assistant
> Placement answer first: **server deployment goes under `30_QiServer`**, while the integration/mirroring logic goes under `70_QiConnect`. It is **not** a QiApp because we didn’t build AFFiNE as a product module.

### Assistant
> Yes — **AFFiNE goes under `30_QiServer`, not QiApps.**
> 
> ## Placement decision
> 
> Use this split:
> 
> ```text
> 30_QiServer/
>   40_services/
>     affine/
>       docker-compose.yml
>       .env.example
>       README.md
>       backups/
>       data/
>       config/
>       storage/
> ```
> 
> And later:
> 
> ```text
> 70_QiConnect/
>   affine/
>     affine_bridge_spec.md
>     mappings/
>     scripts/
> ```
> 
> ## Why
> 
> AFFiNE is **not our app**. It is a **third-party/open-source service we operate**.
> 
> So:
> 
> | Thing | Goes where |
> |---|---|
> | AFFiNE Docker deployment | `30_QiServer/40_services/affine` |
> | AFFiNE volumes, config, backups | `30_QiServer/40_services/affine` |
> | AFFiNE → Supabase sync/mirror workflow | `70_QiConnect/affine` |
> | QiLife app code we build | `60_QiApp_QiLife` / QiApps |
> | Supabase canonical schema | `20_QiSystem/50_data/supabase/qisupabase` |
> 
> AFFiNE’s official self-host path uses Docker Compose and depends on Postgres/Redis/persistent storage, so treating it as an operated server service is the right classification. citeturn357256search0turn718160search2
> 
> ---
> 
> # Paste this into Codex
> 
> :::writing{variant="standard" id="48291"}
> Goal:
> Install/self-host AFFiNE as a QiServer-managed third-party service, not as a QiApp.
> 
> Classification:
> AFFiNE is an operated external/open-source service. It belongs under:
> 
> C:\QiLabs\30_QiServer\40_services\affine
> 
> Do NOT place it under QiApps / QiLife app code.
> 
> QiSystem architecture rule:
> - Supabase remains the canonical source of truth.
> - AFFiNE keeps its own internal Postgres/Redis/container data.
> - Do NOT point AFFiNE at the main QiSystem Supabase database.
> - Future AFFiNE-to-Supabase syncing belongs under:
>   C:\QiLabs\70_QiConnect\affine
> 
> Tasks:
> 
> 1. Create this folder structure if missing:
> 
> C:\QiLabs\30_QiServer\40_services\affine
> C:\QiLabs\30_QiServer\40_services\affine\data
> C:\QiLabs\30_QiServer\40_services\affine\config
> C:\QiLabs\30_QiServer\40_services\affine\storage
> C:\QiLabs\30_QiServer\40_services\affine\backups
> C:\QiLabs\30_QiServer\40_services\affine\logs
> 
> 2. Add deployment files:
> - docker-compose.yml
> - .env.example
> - README.md
> - .gitignore
> 
> 3. Use the official AFFiNE recommended Docker Compose/self-hosting docs as the source of truth:
> https://docs.affine.pro/self-host-affine/
> https://docs.affine.pro/self-host-affine/install/docker-compose-recommend
> 
> 4. The Docker stack should run AFFiNE with its required services:
> - AFFiNE server
> - Postgres
> - Redis
> - persistent storage/config volumes
> 
> 5. Use safe defaults:
> - Expose AFFiNE on local/server port 3010 unless the official docs require otherwise.
> - Use named containers prefixed with qiserver_affine_ or affine_.
> - Use persistent bind mounts or named volumes so updates do not wipe data.
> - Do not hardcode secrets.
> - Put real values only in .env, and commit only .env.example.
> - Add .env to .gitignore.
> 
> 6. .env.example should include placeholders for:
> - AFFINE_REVISION
> - PORT
> - AFFINE_SERVER_HOST
> - AFFINE_SERVER_HTTPS
> - AFFINE_SERVER_EXTERNAL_URL
> - POSTGRES_USER
> - POSTGRES_PASSWORD
> - POSTGRES_DB
> - DATABASE_URL
> - REDIS_SERVER_HOST
> - any required AFFiNE admin/config variables from the official docs
> 
> 7. README.md should explain:
> - What AFFiNE is used for in QiLabs
> - Why it lives under 30_QiServer instead of QiApps
> - That AFFiNE is not the canonical database
> - That Supabase is still the source of truth
> - Start command:
>   docker compose up -d
> - Stop command:
>   docker compose down
> - Logs command:
>   docker compose logs -f
> - Backup notes for Postgres and storage
> - Future QiConnect bridge location:
>   C:\QiLabs\70_QiConnect\affine
> 
> 8. If this is being run on the actual server:
> - Check Docker and Docker Compose availability.
> - Do not overwrite existing AFFiNE data.
> - If docker-compose.yml already exists, back it up before editing.
> - Start the stack only after validating the compose file.
> - Run:
>   docker compose config
>   docker compose up -d
>   docker compose ps
>   docker compose logs --tail=100
> 
> 9. If Cloudflare Tunnel or reverse proxy config exists under QiServer, do not modify it destructively.
> Instead, add a short TODO in README.md for routing:
> - affine.qially.com or another chosen subdomain
> - local target: http://localhost:3010
> 
> 10. After setup, report:
> - files created
> - whether Docker stack started successfully
> - exposed local URL
> - any required next steps
> - any missing domain/proxy configuration
> :::
> 
> ---
> 
> ## One more structural note
> 
> If you already have a services folder convention, match it. Otherwise use:
> 
> ```text
> 30_QiServer/40_services/affine
> ```
> 
> That’s clean and consistent.
> 
> ## The operating rule
> 
> ```text
> AFFiNE = hosted workspace service
> QiConnect = integration bridge
> Supabase = truth database
> QiApps = stuff we build
> ```
> 
> Do that and the system stays sane.

### User
> ok, so quickly number one i need my notes space things im working on, and it needs to mirror the qidna and then my moms workspace for all her care stuff, med interactions updated ect. how should it be built

### Assistant
> You need **two workspaces**, not twenty. One for *your operating brain/QiDNA mirror*, one for *mom’s care command center*. Keep AFFiNE visual and human-facing; keep Supabase canonical and auditable.

### Assistant
> Yes. Build it as **two AFFiNE workspaces**, with **Supabase as truth** and **QiConnect as the sync/review layer**.
> 
> AFFiNE can combine docs, whiteboards, and database-style pages, and it supports self-hosting, so it’s a good command-center layer. But export/migration is still not as clean as plain Markdown/CSV; there are community requests around full workspace export and table export, so we should not make AFFiNE the canonical database. citeturn314634search2turn314634search7turn314634search13
> 
> # The build
> 
> ```text
> AFFiNE
> ├─ Workspace 1: QiOS Command Center
> │  └─ mirrors QiDNA structure visually
> │
> └─ Workspace 2: Mom Care Command Center
>    └─ care plan, meds, interactions, doctors, events, evidence
> ```
> 
> Then:
> 
> ```text
> AFFiNE capture
>   ↓
> QiConnect AFFiNE Bridge
>   ↓
> Supabase staging table
>   ↓
> Reviewed canonical Supabase record
> ```
> 
> Do **not** try to make AFFiNE itself the database. Use it as the human cockpit.
> 
> ---
> 
> # Workspace 1: `QiOS Command Center`
> 
> Purpose: your notes, active work, system maps, and QiDNA mirror.
> 
> ## Pages
> 
> ```text
> 00_Command_Center
> 01_QiDNA_Mirror
> 10_QiAccess
> 20_QiSystem
> 30_QiServer
> 40_QiCapture
> 50_QiNexus
> 60_QiApp_QiLife
> 70_QiConnect
> 90_Active_Work
> 99_Inbox
> ```
> 
> ## What `01_QiDNA_Mirror` means
> 
> It should **mirror the structure**, not duplicate every file.
> 
> Correct:
> 
> ```text
> QiDNA_Mirror page
> ├─ root map
> ├─ links to repo paths
> ├─ links to canonical docs
> ├─ current status
> ├─ gaps / contradictions
> └─ next actions
> ```
> 
> Wrong:
> 
> ```text
> Copy every Markdown file into AFFiNE
> ```
> 
> That becomes Notion disease in a new outfit.
> 
> ## Page template for each Qi module
> 
> Each root page should have:
> 
> ```text
> Module:
> Purpose:
> Canonical repo path:
> Supabase schema/tables:
> Related services:
> Related apps:
> Open decisions:
> Active tasks:
> Source links:
> Last reviewed:
> ```
> 
> Example:
> 
> ```text
> 20_QiSystem
> 
> Purpose:
> Canonical data, schemas, governance, Supabase, system logic.
> 
> Canonical repo path:
> C:\QiLabs\20_QiSystem
> 
> Related Supabase:
> qisupabase
> 
> Related QiConnect bridges:
> AFFiNE Bridge
> Firefly Bridge
> Google Sheets Importer
> 
> Open decisions:
> - canonical financial category model
> - mom care schema
> - document/evidence model
> ```
> 
> ---
> 
> # Workspace 2: `Mom Care Command Center`
> 
> Purpose: everything for your mom’s care, but structured so it can migrate to Supabase.
> 
> ## Pages
> 
> ```text
> 00_Care_Command_Center
> 01_Current_Care_Plan
> 02_Medications
> 03_Med_Interaction_Reviews
> 04_Symptoms_Vitals_Log
> 05_Hospitalizations
> 06_Doctors_Providers
> 07_Tasks_Calls_Followups
> 08_Documents_Evidence
> 09_Insurance_Humana
> 10_Daily_Care_Log
> 99_Inbox
> ```
> 
> This gives you the front-end friendly workspace while still mapping to real tables later.
> 
> ---
> 
> # Mom workspace: core tables
> 
> ## `02_Medications`
> 
> Fields:
> 
> ```text
> med_name
> dose
> route
> frequency
> time_of_day
> prescriber
> reason
> start_date
> stop_date
> status
> pharmacy
> last_confirmed_date
> notes
> ```
> 
> Status values:
> 
> ```text
> active
> paused
> stopped
> needs_doctor_review
> unknown
> ```
> 
> ## `03_Med_Interaction_Reviews`
> 
> This is where you handle the “updated interactions” issue safely.
> 
> Fields:
> 
> ```text
> review_id
> medication_a
> medication_b
> interaction_concern
> severity_source_label
> source_used
> checked_date
> checked_by
> symptoms_observed
> question_for_doctor
> doctor_response
> doctor_verified_date
> action_taken
> status
> notes
> ```
> 
> Status:
> 
> ```text
> new
> needs_review
> doctor_question_ready
> doctor_verified
> resolved
> archived
> ```
> 
> Important rule:
> 
> ```text
> AFFiNE can track medication concerns.
> Supabase can store medication records.
> Only doctor/pharmacist confirmation changes the actual medication plan.
> ```
> 
> No cowboy medicine. We organize the war room; we do not play pharmacist.
> 
> ## `10_Daily_Care_Log`
> 
> Fields:
> 
> ```text
> date
> time
> event_type
> what_happened
> symptoms
> oxygen_notes
> food_water
> medication_note
> caregiver_action
> followup_needed
> priority
> supabase_status
> ```
> 
> Event types:
> 
> ```text
> symptom
> medication
> doctor_call
> hospital
> insurance
> caregiver
> task
> document
> conversation
> safety
> ```
> 
> ---
> 
> # Supabase mapping
> 
> Later, QiConnect maps AFFiNE content into these Supabase tables:
> 
> ```text
> people
> organizations
> care_medications
> care_medication_reviews
> care_events
> care_tasks
> care_documents
> care_hospitalizations
> care_provider_contacts
> qiconnect_capture_inbox
> qiconnect_external_refs
> ```
> 
> AFFiNE page IDs should become external references, not primary truth.
> 
> ```text
> qiconnect_external_refs
> ├─ source_system = affine
> ├─ source_workspace = mom_care
> ├─ source_page_id
> ├─ source_block_id
> ├─ supabase_table
> ├─ supabase_record_id
> └─ sync_status
> ```
> 
> ---
> 
> # How the mirror should work
> 
> ## From AFFiNE to Supabase
> 
> Use this flow:
> 
> ```text
> AFFiNE note/page
>   ↓
> export / API / scraper / manual copy first
>   ↓
> qiconnect_capture_inbox
>   ↓
> normalize
>   ↓
> review
>   ↓
> canonical Supabase table
> ```
> 
> Everything lands in staging first. No direct blind sync.
> 
> ## From Supabase to AFFiNE
> 
> Use summaries only:
> 
> ```text
> Supabase canonical care records
>   ↓
> QiConnect summary generator
>   ↓
> AFFiNE dashboard block/page
> ```
> 
> Example dashboard output:
> 
> ```text
> Mom Care Dashboard
> 
> Open urgent items:
> - Call pulmonologist about oxygen/medication concern
> - Confirm hospital discharge medication list
> - Review Humana care plan gap
> 
> Recent events:
> - 2026-06-10 ED visit
> - 2026-06-10 to 2026-06-12 hospitalization
> 
> Medication review:
> - 3 active concerns
> - 1 doctor-verified
> - 2 need pharmacist review
> ```
> 
> ---
> 
> # Build rule
> 
> ## AFFiNE holds:
> 
> ```text
> thinking
> maps
> dashboards
> working notes
> care overview
> visual timeline
> questions for doctors
> ```
> 
> ## Supabase holds:
> 
> ```text
> canonical records
> auditable history
> tables
> IDs
> statuses
> review flags
> source references
> ```
> 
> ## Obsidian holds:
> 
> ```text
> long-form narratives
> printable care plans
> formal documents
> evidence packets
> doctor-call scripts
> ```
> 
> ---
> 
> # Server/repo placement
> 
> ```text
> 30_QiServer/
>   40_services/
>     affine/
>       docker-compose.yml
>       .env.example
>       README.md
>       storage/
>       backups/
> 
> 70_QiConnect/
>   affine/
>     README.md
>     mappings/
>       qidna_workspace_map.yml
>       mom_care_workspace_map.yml
>     templates/
>       medication_review_template.md
>       care_event_template.md
>       qidna_module_template.md
>     scripts/
>       affine_export_to_inbox.py
>       normalize_affine_capture.py
>       push_affine_to_supabase.py
> ```
> 
> ---
> 
> # Minimum viable version today
> 
> Do **not** overbuild.
> 
> Create only this first:
> 
> ## AFFiNE Workspace 1
> 
> ```text
> QiOS Command Center
> ```
> 
> Pages:
> 
> ```text
> 00_Command_Center
> 01_QiDNA_Mirror
> 90_Active_Work
> 99_Inbox
> ```
> 
> ## AFFiNE Workspace 2
> 
> ```text
> Mom Care Command Center
> ```
> 
> Pages:
> 
> ```text
> 00_Care_Command_Center
> 02_Medications
> 03_Med_Interaction_Reviews
> 10_Daily_Care_Log
> 99_Inbox
> ```
> 
> That is enough to start. Anything more today is a trap.
> 
> ---
> 
> # Codex instruction
> 
> Paste this:
> 
> ```text
> Goal:
> Set up the AFFiNE workspace architecture documentation and QiConnect mapping scaffolding.
> 
> AFFiNE is hosted as a third-party service under:
> C:\QiLabs\30_QiServer\40_services\affine
> 
> AFFiNE is not a QiApp and is not the canonical database.
> 
> Create QiConnect scaffolding under:
> C:\QiLabs\70_QiConnect\affine
> 
> Create these files:
> 
> 1. C:\QiLabs\70_QiConnect\affine\README.md
> 2. C:\QiLabs\70_QiConnect\affine\workspace_architecture.md
> 3. C:\QiLabs\70_QiConnect\affine\mappings\qidna_workspace_map.yml
> 4. C:\QiLabs\70_QiConnect\affine\mappings\mom_care_workspace_map.yml
> 5. C:\QiLabs\70_QiConnect\affine\templates\qidna_module_template.md
> 6. C:\QiLabs\70_QiConnect\affine\templates\care_event_template.md
> 7. C:\QiLabs\70_QiConnect\affine\templates\medication_review_template.md
> 
> Architecture:
> - AFFiNE has two main workspaces:
>   1. QiOS Command Center
>   2. Mom Care Command Center
> 
> QiOS Command Center pages:
> - 00_Command_Center
> - 01_QiDNA_Mirror
> - 10_QiAccess
> - 20_QiSystem
> - 30_QiServer
> - 40_QiCapture
> - 50_QiNexus
> - 60_QiApp_QiLife
> - 70_QiConnect
> - 90_Active_Work
> - 99_Inbox
> 
> Mom Care Command Center pages:
> - 00_Care_Command_Center
> - 01_Current_Care_Plan
> - 02_Medications
> - 03_Med_Interaction_Reviews
> - 04_Symptoms_Vitals_Log
> - 05_Hospitalizations
> - 06_Doctors_Providers
> - 07_Tasks_Calls_Followups
> - 08_Documents_Evidence
> - 09_Insurance_Humana
> - 10_Daily_Care_Log
> - 99_Inbox
> 
> Rules:
> - AFFiNE is a visual workspace and capture layer.
> - Supabase is the source of truth.
> - QiConnect moves reviewed/normalized AFFiNE content into Supabase.
> - Do not directly couple AFFiNE internal Postgres tables to Supabase canonical tables.
> - AFFiNE content should first land in qiconnect_capture_inbox before becoming canonical data.
> - Medication interaction records must be tracked as care review items, not automatic medical instructions.
> - Medication changes require doctor/pharmacist verification.
> 
> Add mapping notes for future Supabase tables:
> - qiconnect_capture_inbox
> - qiconnect_external_refs
> - care_medications
> - care_medication_reviews
> - care_events
> - care_tasks
> - care_documents
> - care_hospitalizations
> - people
> - organizations
> 
> Do not add secrets.
> Do not edit existing migrations.
> Do not deploy anything.
> Only create safe documentation/scaffolding files.
> ```
> 
> # Final call
> 
> Build it like this:
> 
> ```text
> AFFiNE = cockpit
> QiConnect = translator
> Supabase = truth
> Obsidian = printable/legal/narrative archive
> ```
> 
> For your brain today: **two workspaces, five starter pages each, nothing fancy.**

### User
> girl hold up what is all that, im confusion, hey reql quick, give me a prompt to have gemini create the single source of truth app for management of my moms care, has to ingest dicharge paper work, find contradictions, errors, insights, interactions and provide suggestions. wholist care plan like the five poing documetn i sent them ect.

### Assistant
> Yep — I overbuilt the architecture answer. For Gemini, you need **one clean product prompt** that says: build the care-command app, ingest paperwork, reconcile contradictions, and generate a doctor-safe care plan.

### Assistant
> Paste this into Gemini:
> 
> :::writing{variant="standard" id="74826"}
> You are helping me design and build a single-source-of-truth care management app for my mother’s care.
> 
> Goal:
> Create an app that helps me manage my mother’s full care picture in one place. It must ingest discharge paperwork, hospital records, medication lists, insurance/Humana care plans, doctor notes, symptom logs, and my own care notes. It should extract structured information, find contradictions, identify risks, surface insights, and generate a holistic care plan.
> 
> Important:
> This app must not pretend to be a doctor. It can identify concerns, contradictions, possible medication interactions, missing follow-ups, and questions to ask a doctor/pharmacist. Medication changes must always be marked as “needs doctor/pharmacist verification.”
> 
> Core app purpose:
> Build a “Mom Care Command Center” that acts as:
> 1. A source of truth for her care
> 2. A document ingestion system
> 3. A medication reconciliation tool
> 4. A contradiction/error detector
> 5. A holistic care plan generator
> 6. A task/follow-up tracker
> 7. A doctor-call preparation tool
> 8. A timeline of hospitalizations, symptoms, medication changes, and care events
> 
> Primary users:
> - Me, her son/caregiver
> - Potentially doctors, nurses, social workers, insurance care managers, and family members later
> 
> Core features:
> 
> 1. Document ingestion
> The app must accept:
> - PDF discharge papers
> - photos/scans of paperwork
> - medication lists
> - after-visit summaries
> - hospital discharge summaries
> - Humana/insurance care plan documents
> - doctor instructions
> - lab/vitals documents
> - my own typed or voice notes
> 
> For each document, extract:
> - document type
> - date
> - facility/provider
> - diagnoses
> - medication changes
> - active medication list
> - stopped medications
> - allergies
> - follow-up instructions
> - appointments
> - symptoms mentioned
> - vitals/labs if available
> - red flag instructions
> - home care instructions
> - oxygen/COPD-related instructions
> - insurance/care coordination requirements
> - tasks created from the document
> 
> 2. Contradiction and error detection
> The app should compare new documents against existing records and flag:
> - medication dose conflicts
> - medication frequency conflicts
> - medications listed as both active and stopped
> - duplicate medications
> - missing medications from a later discharge list
> - discharge instructions that conflict with current care plan
> - follow-up dates that were missed or not scheduled
> - diagnosis changes or inconsistencies
> - conflicting oxygen/COPD instructions
> - provider instructions that contradict each other
> - insurance care plan gaps
> - missing home health services
> - missing transportation, DME, oxygen, therapy, nursing, or caregiver supports
> - safety risks based on symptoms/events
> 
> Each contradiction should include:
> - what conflicts
> - source document A
> - source document B
> - why it matters
> - confidence level
> - suggested next action
> - who to ask: doctor, pharmacist, nurse, insurance, home health, etc.
> 
> 3. Medication management
> Create a medication module that tracks:
> - medication name
> - dose
> - route
> - frequency
> - time of day
> - reason/condition
> - prescriber
> - start date
> - stop date
> - active/paused/stopped/unknown status
> - source document
> - last confirmed date
> - pharmacy
> - notes
> 
> The app should perform medication reconciliation:
> - current active list
> - hospital discharge list
> - old list
> - pharmacy list
> - caregiver-observed list
> 
> The app should flag possible interactions and concerns, including:
> - duplicate therapy
> - sedating combinations
> - blood pressure risks
> - COPD/respiratory risk concerns
> - kidney/liver caution if labs indicate concern
> - medications that may worsen confusion, dizziness, falls, or breathing
> 
> For every medication interaction or concern, the app must say:
> - “Possible concern — verify with doctor/pharmacist”
> - severity
> - evidence/source
> - what question to ask
> - whether urgent or routine
> 
> 4. Holistic care plan generator
> The app should generate a holistic care plan similar to a five-point care plan. It should organize care into major areas such as:
> 
> A. Medical stability
> - diagnoses
> - medications
> - breathing/COPD/oxygen concerns
> - red flags
> - hospital follow-up
> - labs/vitals monitoring
> 
> B. Daily home care
> - meals
> - hydration
> - hygiene
> - mobility
> - fall prevention
> - oxygen safety
> - home environment
> - caregiver schedule
> 
> C. Medication safety
> - active medication list
> - unknowns
> - contradictions
> - questions for pharmacist/doctor
> - verification status
> 
> D. Services and insurance
> - Humana/insurance care plan
> - home health nursing
> - PT/OT
> - caregiver hours
> - transportation
> - DME/oxygen supplies
> - care manager contacts
> 
> E. Family/caregiver operations
> - tasks
> - boundaries
> - emergency plan
> - communication log
> - who is responsible for what
> - next calls to make
> 
> The care plan should be printable and exportable as Markdown/PDF.
> 
> 5. Timeline
> Create a timeline that combines:
> - hospitalizations
> - ED visits
> - medication changes
> - symptoms
> - falls/near falls
> - breathing issues
> - doctor calls
> - insurance calls
> - home health visits
> - important documents
> - caregiver notes
> 
> Each timeline item should link back to its source document or note.
> 
> 6. Task and call tracker
> The app should automatically generate tasks from documents and contradictions:
> - schedule follow-up appointment
> - call doctor
> - call pharmacist
> - confirm medication
> - request records
> - call Humana
> - ask about home health
> - check oxygen supplies
> - verify discharge instructions
> - prepare questions before appointment
> 
> Each task should have:
> - priority
> - due date
> - responsible person
> - status
> - related document
> - related care issue
> - notes
> 
> 7. Doctor/pharmacist question generator
> For any contradiction, medication issue, symptom pattern, or care gap, generate a plain-English question list:
> - “Can you confirm whether she should still be taking ___?”
> - “The discharge paperwork says ___, but the prior list says ___. Which is correct?”
> - “Is this combination safe given her COPD/oxygen use?”
> - “Should home health nursing/PT/OT be ordered?”
> - “What symptoms mean we should go to the ER?”
> 
> 8. Insight engine
> The app should surface:
> - urgent risks
> - repeated issues
> - missing follow-ups
> - care plan gaps
> - changes after hospitalization
> - medication changes after discharge
> - mismatches between insurance plan and real care needs
> - patterns in symptoms or hospitalizations
> - caregiver overload risks
> 
> 9. Data architecture
> Use Supabase/Postgres as the canonical source of truth.
> 
> Suggested tables:
> - people
> - providers
> - organizations
> - documents
> - document_extractions
> - care_events
> - hospitalizations
> - diagnoses
> - medications
> - medication_orders
> - medication_reconciliation_items
> - medication_interaction_reviews
> - allergies
> - symptoms
> - vitals
> - tasks
> - appointments
> - insurance_plan_items
> - care_plan_sections
> - care_plan_recommendations
> - contradictions
> - source_references
> - audit_log
> 
> Every extracted fact must preserve:
> - source document ID
> - source page/section if available
> - extracted text snippet
> - extraction confidence
> - reviewed/unreviewed status
> - who confirmed it
> - when confirmed
> 
> 10. Safety and trust requirements
> The app must:
> - never silently overwrite medical information
> - preserve all original documents
> - track sources for every claim
> - clearly separate extracted facts from AI interpretation
> - require human review before marking something as confirmed
> - mark medical suggestions as “discussion points,” not instructions
> - support audit history
> - support export/backup
> 
> 11. UI requirements
> Create a simple dashboard with:
> - urgent issues
> - medication concerns
> - open contradictions
> - next tasks
> - upcoming appointments
> - latest discharge summary
> - current care plan
> - recent timeline events
> - doctor-call prep button
> 
> Main sections:
> - Dashboard
> - Documents
> - Medications
> - Contradictions
> - Care Plan
> - Timeline
> - Tasks
> - Providers
> - Insurance/Humana
> - Doctor Questions
> - Settings
> 
> 12. Build request
> Please produce:
> 1. Product requirements document
> 2. Recommended database schema
> 3. Core user flows
> 4. UI layout
> 5. MVP feature list
> 6. Risk/safety guardrails
> 7. Technical architecture using Supabase/Postgres
> 8. Document ingestion pipeline
> 9. AI extraction/reconciliation workflow
> 10. Example screens/components
> 11. Suggested implementation plan
> 12. Any missing questions I need to answer before building
> 
> Optimize for a caregiver who is overwhelmed and needs clarity fast. The app should reduce chaos, not create another complicated system.
> :::
> 
> That’s the clean version. It tells Gemini to build the **actual thing** instead of wandering into “wellness dashboard” fluff.

### User
> so i need to be able to share this with my mom, she can suggest changes or add comments, but only i can approve them to take effect, and the system must adjust all the scheduls accordingly based on those chagnes. handle tapers ect.

### Assistant
> Yes. Add this to the Gemini prompt. This is the missing governance layer.
> 
> The key rule:
> 
> **Your mom can suggest. You approve. The system recalculates only after approval. Medication tapers require doctor/pharmacist verification before becoming active.**
> 
> :::writing{variant="standard" id="59384"}
> Additional requirement: Shared review and approval workflow
> 
> The app must support shared access with role-based permissions.
> 
> Roles:
> 
> 1. Owner / Primary Care Manager
> - This is me.
> - I have final approval authority.
> - Only I can approve changes that affect the active care plan, schedules, medication plan, tasks, or official records.
> - I can accept, reject, edit, or defer suggested changes.
> 
> 2. Care Recipient / Mom
> - My mother can view her care plan, schedule, medication list, tasks, notes, and documents that I choose to share.
> - She can add comments, suggest corrections, propose changes, flag something as wrong, or add context.
> - Her changes must not directly overwrite the canonical care plan.
> - Her suggestions must enter a review queue.
> 
> 3. Optional future roles
> - Doctor
> - Pharmacist
> - Nurse
> - Social worker
> - Insurance care manager
> - Family member
> Each role should have configurable permissions.
> 
> Core rule:
> No suggested change becomes active until approved by the Owner.
> 
> Approval workflow:
> 
> When my mom suggests a change, the system should create a pending change request.
> 
> Each change request should include:
> - suggested_by
> - suggested_date
> - change_type
> - affected_area
> - current_value
> - proposed_value
> - reason_for_change
> - related document or note
> - possible downstream effects
> - risk level
> - requires_medical_verification true/false
> - approval_status
> - approved_by
> - approved_at
> - effective_date
> - notes
> 
> Approval statuses:
> - draft
> - pending_review
> - needs_more_info
> - needs_doctor_or_pharmacist_verification
> - approved
> - rejected
> - superseded
> - archived
> 
> Change types:
> - medication_change
> - medication_taper
> - schedule_change
> - appointment_change
> - care_task_change
> - symptom_update
> - provider_update
> - insurance_update
> - document_correction
> - care_plan_note
> - emergency_plan_change
> 
> Schedule recalculation:
> 
> When an approved change affects the care plan, the system must automatically recalculate affected schedules.
> 
> This includes:
> - medication times
> - taper schedules
> - meal timing
> - oxygen checks
> - vitals checks
> - caregiver visits
> - home health visits
> - doctor follow-ups
> - transportation timing
> - task due dates
> - reminder timing
> - conflict detection between appointments, medications, meals, sleep, caregiver availability, and transportation
> 
> The system must show:
> - what schedule changed
> - why it changed
> - what records were affected
> - what conflicts were created or resolved
> - what needs human review
> 
> No silent changes:
> The system must never silently alter the active schedule. It must show a clear diff before and after approval.
> 
> Medication taper handling:
> 
> The app must support medication taper plans, but it must treat them as medically sensitive.
> 
> A taper plan should include:
> - medication name
> - starting dose
> - taper reason
> - taper ordered_by
> - source document or provider instruction
> - start date
> - end date
> - dose steps
> - schedule per step
> - monitoring instructions
> - warning signs
> - what to do if symptoms worsen
> - verification status
> - related doctor/pharmacist contact
> - active/inactive status
> 
> Taper step example structure:
> - step_number
> - start_date
> - end_date
> - dose
> - frequency
> - time_of_day
> - instructions
> - monitoring_notes
> - status
> 
> Medication taper safety rule:
> A taper cannot become active unless it is marked as verified by a doctor/pharmacist or clearly sourced from official discharge/provider instructions.
> 
> The app can draft a taper schedule from provider instructions, but it must label it:
> “Draft schedule — requires verification before use”
> unless already verified from an official source.
> 
> When a taper is approved and verified, the app should:
> - update the medication schedule
> - create taper reminders
> - create symptom monitoring tasks
> - flag overlapping medications or interactions
> - create doctor/pharmacist follow-up questions if needed
> - preserve the previous medication plan in history
> - show a timeline of the taper
> 
> Contradiction handling for suggestions:
> 
> If my mom suggests something that conflicts with:
> - discharge paperwork
> - doctor instructions
> - medication list
> - insurance care plan
> - prior approved care plan
> - pharmacy record
> - appointment schedule
> 
> The system must flag the contradiction before approval.
> 
> It should show:
> - the conflict
> - the sources involved
> - why it matters
> - suggested next action
> - whether medical verification is needed
> 
> Examples:
> - Mom says she stopped a medication, but discharge papers list it as active.
> - Mom says she takes a medication once daily, but pharmacy label says twice daily.
> - Mom wants to move a medication time, but it conflicts with food/other medication instructions.
> - Mom says she does not need oxygen, but discharge instructions require oxygen use.
> - Mom says an appointment is unnecessary, but discharge paperwork requires follow-up.
> 
> Commenting system:
> 
> Every care plan section, medication, task, schedule item, document, contradiction, and timeline event should support comments.
> 
> Comments should be threaded and include:
> - author
> - timestamp
> - related record
> - comment text
> - resolved/unresolved status
> - linked change request if applicable
> 
> The app should allow a comment to be converted into a change request.
> 
> Versioning:
> 
> The care plan must be versioned.
> 
> Every approved change should create:
> - new care plan version
> - audit log entry
> - before/after comparison
> - source reference
> - approval record
> - effective date
> 
> The app should allow viewing:
> - current active care plan
> - pending proposed changes
> - history of previous care plan versions
> - why something changed
> - who approved it
> - what source justified it
> 
> Dashboard additions:
> 
> Add a “Pending Changes” section to the dashboard with:
> - mom’s suggestions
> - medical changes needing verification
> - schedule changes waiting approval
> - contradictions created by suggestions
> - comments needing response
> - taper plans needing confirmation
> 
> Add a “Review Impact” button that shows:
> - affected medications
> - affected tasks
> - affected schedules
> - affected appointments
> - affected reminders
> - new risks or contradictions
> 
> Required UX behavior:
> 
> The app should make this simple:
> 1. Mom suggests a change.
> 2. System checks for conflicts.
> 3. System shows the impact.
> 4. I approve, reject, or request verification.
> 5. If approved, the system updates the care plan and recalculates schedules.
> 6. The system keeps a full audit trail.
> 
> Core principle:
> My mom can participate in her care plan, but the system must protect against accidental, contradictory, unsafe, or unverified changes.
> :::
> 
> Bluntly: this is **critical**. Without this approval layer, the app becomes a shared editable mess, and that’s exactly how medication errors happen.
> 
> Use this model:
> 
> ```text
> Mom suggests → system checks → Cody approves → schedule updates → audit trail preserved
> ```
> 
> Not:
> 
> ```text
> Mom edits → care plan changes → everybody confused
> ```
> 
> That second one is chaos with a login screen.

### User
> quick question does onenote from microsoft fit naywhere in my life.

### Assistant
> I’ll keep this practical: OneNote is not your source of truth. It may fit as a **low-friction scratchpad**, especially if you’re already in Microsoft/phone mode.

### Assistant
> Yes, **OneNote fits — but only in one narrow lane**.
> 
> ## My verdict
> 
> Use OneNote as:
> 
> ```text
> Fast handwritten / phone / messy capture
> ```
> 
> Do **not** use OneNote as:
> 
> ```text
> source of truth
> database
> care plan system
> QiDNA mirror
> Supabase staging layer
> formal evidence archive
> ```
> 
> ## Where OneNote fits in your life
> 
> ### Good use cases
> 
> | Use | Verdict |
> |---|---|
> | Quick notes while driving/working | **Yes** |
> | Handwritten notes with stylus/touchscreen | **Yes** |
> | Voice-call notes | **Yes** |
> | Temporary scratchpad before cleanup | **Yes** |
> | Mom appointment notes during a call | **Maybe** |
> | Long-term care database | **No** |
> | Medication management | **No** |
> | QiSystem canonical docs | **No** |
> | Supabase migration staging | **No** |
> 
> OneNote is organized around notebooks, sections, and pages, which is useful for messy note capture. Microsoft also has Graph API access to notebooks/sections/pages, so automation is possible, but it is not clean enough to make it your core system. citeturn155572search9turn155572search2
> 
> ## The actual role
> 
> Make OneNote your **field notebook**.
> 
> ```text
> Real life happens
>   ↓
> OneNote quick capture
>   ↓
> daily/weekly cleanup
>   ↓
> AFFiNE / Obsidian / Supabase
> ```
> 
> Examples:
> 
> ```text
> Mom said oxygen company called
> Passenger told me useful app idea
> Doctor said “call pharmacy”
> Random QiSystem folder idea
> Receipt note
> Phone number / address / appointment note
> ```
> 
> Then later you process it.
> 
> ## Why not use it as the main system?
> 
> Because export and portability are annoying. Microsoft’s own support says notebook export through OneNote for the web is limited to notebooks stored on personal OneDrive accounts. citeturn155572search1
> 
> Also, shared notebooks allow people with access to edit content, which is exactly what you **do not** want for mom’s care source-of-truth approval workflow. citeturn155572search6
> 
> ## Your clean stack
> 
> ```text
> OneNote = messy capture
> AFFiNE = visual workspace / command center
> Obsidian = durable written notes and printable docs
> Google Sheets = structured staging
> Supabase = source of truth
> QiConnect = sync/integration layer
> ```
> 
> ## Rule for you
> 
> Use OneNote only when the alternative is **not capturing the thought at all**.
> 
> If you are sitting down to organize, do **not** open OneNote. Open AFFiNE, Obsidian, Sheets, or Supabase.
> 
> Bluntly: OneNote is a **napkin**, not the kitchen.

### User
> ok and why am i deciding on using selrf hosted affine instead of free tier nothion.

### Assistant
> Good question. This is a real decision, not vibes: **Notion free is easier today; self-hosted AFFiNE gives you more ownership/control if this becomes infrastructure.** I’ll verify the current facts, then give you the clean call.

### Assistant
> Because **Notion Free is convenient**, but **self-hosted AFFiNE fits the kind of system you’re building**.
> 
> The clean reason:
> 
> ```text
> Notion Free = rented workspace
> Self-hosted AFFiNE = operated workspace service inside QiServer
> Supabase = actual source of truth
> ```
> 
> ## Why not just Notion Free?
> 
> Notion Free is fine for casual notes. It gives individuals unlimited pages/blocks, but Free has a **5 MB file upload limit**, **7-day page history**, and **10 external guests**. For a care system involving discharge PDFs, scans, comments, version history, and shared review, those limits start mattering fast. citeturn516177view0
> 
> Also, Notion becomes dangerous for your brain because it encourages:
> 
> ```text
> database tweaking
> template hunting
> workspace decorating
> dashboard cosplay
> ```
> 
> And you already know that road. It’s paved with “I’ll just fix the sidebar real quick” and then suddenly it’s 3:17 AM.
> 
> ## Why AFFiNE instead?
> 
> AFFiNE is closer to what you keep trying to build: docs + whiteboards + database-style structure + visual planning in one local-first workspace. AFFiNE describes itself as an open-source Notion/Miro alternative combining docs, whiteboards, databases, and AI, with more control over data through local-first/self-hosted workflows. citeturn516177view3
> 
> Its pricing page also says self-hosting is available, local/FOSS use includes unlimited local workspaces and editing, and self-hosting gives full data control with limits bound mostly by your infrastructure. citeturn516177view2
> 
> ## The real strategic reason
> 
> You are not choosing AFFiNE because it is “better Notion.”
> 
> You are choosing it because it fits your architecture:
> 
> ```text
> 30_QiServer = hosts AFFiNE
> 70_QiConnect = syncs/reviews/mirrors important data
> 20_QiSystem/Supabase = source of truth
> Obsidian = durable printable docs
> ```
> 
> Notion does not fit that as cleanly because it is a SaaS workspace you rent. Useful, yes. But not part of your operated system.
> 
> ## But here’s the correction
> 
> Self-hosted AFFiNE is **not automatically the best choice today**.
> 
> Use this rule:
> 
> | Situation | Use |
> |---|---|
> | Need fastest possible notes today | **Notion Free or OneNote** |
> | Need visual command center you control | **AFFiNE** |
> | Need canonical care records | **Supabase** |
> | Need printable care plan / evidence docs | **Obsidian / Markdown** |
> | Need mom to suggest changes but not overwrite truth | **Custom care app over Supabase** |
> 
> ## My actual recommendation
> 
> Use **AFFiNE self-hosted** for your **workspace cockpit**, not the medical truth system.
> 
> Use **Supabase/custom app** for mom’s care source of truth.
> 
> So the decision is:
> 
> ```text
> Use AFFiNE because you want control, self-hosting, visual maps, and QiServer alignment.
> 
> Do not use AFFiNE because you think it magically solves the care app.
> ```
> 
> ## Blunt verdict
> 
> If this is just “I need somewhere to write notes,” use Notion Free and move on.
> 
> If this is “I’m building my long-term operating system and mom-care command center,” use self-hosted AFFiNE as a QiServer service.
> 
> Given your actual trajectory, **AFFiNE makes more strategic sense**.
> 
> But do not get cute: **AFFiNE is the cockpit. Supabase is the truth.**

### User
> ok i am inside codex in the tmux, what do i tell it to get affine up and running and viewable and usuable from my phone in minutes not horus.

### Assistant
> Yes. Tell Codex this **exactly**. The goal is **temporary viewable-from-phone first**, clean routing later. AFFiNE’s official self-host docs recommend Docker Compose, and the setup runs the AFFiNE server with dependencies like Postgres/Redis, so Codex should use the official compose path rather than inventing a stack. citeturn961700search0turn961700search1
> 
> :::writing{variant="standard" id="19384"}
> Goal:
> Get AFFiNE self-hosted, running, and viewable from my phone as fast as possible. Prioritize working access in minutes. Clean permanent domain/proxy can be handled later.
> 
> Context:
> AFFiNE is a third-party service we operate under QiServer, not a QiApp.
> 
> Expected location:
> Use the existing QiLabs root if found. Prefer:
> 
> /srv/QiLabs/30_QiServer/40_services/affine
> 
> If /srv/QiLabs does not exist, search for QiLabs. If no QiLabs root exists on this server, use:
> 
> ~/QiLabs/30_QiServer/40_services/affine
> 
> Rules:
> - Do not connect AFFiNE to the main QiSystem Supabase database.
> - Use AFFiNE’s own bundled/local Postgres/Redis through Docker Compose.
> - Do not hardcode secrets into committed files.
> - Do not destructively edit existing Cloudflare/reverse proxy config.
> - Do not spend time making the perfect production setup.
> - Get it running locally first on port 3010.
> - Then make it reachable from my phone using the fastest safe method.
> 
> Tasks:
> 
> 1. Check requirements:
> - docker --version
> - docker compose version
> - curl --version
> 
> If Docker or Docker Compose is missing, report that clearly and stop. Do not try a huge install unless it is already obvious this server supports it.
> 
> 2. Create service folder:
> 
> mkdir -p /srv/QiLabs/30_QiServer/40_services/affine
> 
> Or use the detected QiLabs root.
> 
> 3. Go into the AFFiNE service folder.
> 
> 4. Download the official current AFFiNE Docker Compose files:
> 
> curl -fsSL -o docker-compose.yml https://github.com/toeverything/affine/releases/latest/download/docker-compose.yml
> curl -fsSL -o .env https://github.com/toeverything/affine/releases/latest/download/default.env.example
> 
> If either download fails, report the failure and try the official docs page:
> https://docs.affine.pro/self-host-affine/
> https://docs.affine.pro/self-host-affine/install/docker-compose-recommend
> 
> 5. Configure .env for fast local use:
> - Set AFFINE_REVISION=stable if the variable exists.
> - Set PORT=3010 if the variable exists.
> - Set external/server URL to the best temporary URL available.
> - If we are using direct IP, use http://SERVER_PUBLIC_IP:3010.
> - If we are using a Cloudflare quick tunnel, use the tunnel URL after it is generated.
> - Do not configure SMTP or AI right now.
> - Do not overconfigure.
> 
> 6. Start AFFiNE:
> 
> docker compose config
> docker compose pull
> docker compose up -d
> docker compose ps
> docker compose logs --tail=120
> 
> 7. Confirm local access:
> Check whether AFFiNE responds locally:
> 
> curl -I http://localhost:3010 || curl -I http://127.0.0.1:3010
> 
> 8. Make it viewable from my phone using the fastest available option:
> 
> Option A — preferred if cloudflared is installed:
> Run a temporary Cloudflare quick tunnel in its own tmux session:
> 
> tmux new-session -d -s affine-tunnel 'cloudflared tunnel --url http://localhost:3010'
> 
> Then show me the tunnel URL from logs:
> 
> tmux capture-pane -pt affine-tunnel -S -200
> 
> Look for the https://*.trycloudflare.com URL.
> 
> Option B — if direct public IP access is already available:
> Show me:
> http://SERVER_PUBLIC_IP:3010
> 
> Only open firewall port 3010 if this server already uses ufw/firewalld and it is straightforward. If unsure, do not mess with firewall rules; report the issue.
> 
> Option C — if there is already an existing reverse proxy or named Cloudflare tunnel:
> Do not edit destructively. Add a TODO only:
> affine.qially.com -> http://localhost:3010
> 
> 9. Create a quick README.md in the AFFiNE folder with:
> - What this service is
> - Start command
> - Stop command
> - Logs command
> - Local URL
> - Temporary phone URL if created
> - Permanent routing TODO
> - Backup TODO
> - Note: AFFiNE is not the canonical care database; Supabase is source of truth
> 
> 10. Final report:
> Give me only:
> - AFFiNE status: running/not running
> - Local URL
> - Phone URL
> - Folder path used
> - Docker containers running
> - Any immediate issue blocking access
> - Next one thing I should do
> :::
> 
> After Codex runs it, your only job is:
> 
> ```text
> Open the phone URL
> Create the first admin/user account
> Make two workspaces:
> 1. QiOS Command Center
> 2. Mom Care Command Center
> ```
> 
> Do **not** start building the whole care app inside AFFiNE tonight. Get the cockpit online first.

### User
> also since i am heavy into google, i think we mirror contact using google contacts like link them becaue we already use the drive as our storage blob location qinexus, it make sense to synergize their other tools, like google calendar, google tasks, google keep for notes, and sheets ect.

### Assistant
> Yes — that’s the right instinct. Since QiNexus is already Drive-backed, Google should become your **identity/schedule/capture ecosystem**, while Supabase stays the canonical record layer. I’ll pin the Google pieces to what each one is actually good for, because Google Keep is useful but not the same kind of API-backed system as Calendar/Contacts/Sheets.

### Assistant
> Yes. **Google should absolutely be part of QiConnect.** That’s not random tool sprawl — that’s leverage.
> 
> But the rule stays the same:
> 
> ```text
> Google = daily-life operating layer
> QiNexus/Drive = blob/file storage
> QiConnect = sync/mirror layer
> Supabase = canonical source of truth
> AFFiNE/Obsidian = human workspace/docs
> ```
> 
> ## The clean Google role map
> 
> | Google tool | Best role | Supabase mirror? | Canonical? |
> |---|---|---:|---:|
> | **Google Drive** | File/blob storage for QiNexus | Yes | For files, yes-ish |
> | **Google Contacts** | Real-world people/contact source | Yes | Usually Google first, Supabase mirror |
> | **Google Calendar** | Appointments, reminders, care schedule visibility | Yes | Shared schedule layer |
> | **Google Tasks** | Lightweight personal task execution | Yes | Supabase should own care tasks |
> | **Google Sheets** | Staging tables / import review / quick grids | Yes | Temporary staging only |
> | **Google Keep** | Quick capture notes | Maybe/manual | No |
> 
> Google’s APIs make most of this reasonable: People API can read/manage/sync contacts, Calendar API exposes calendar data/events, Tasks API has REST resources for tasklists/tasks, Sheets API can create/read/write spreadsheet data, and Drive API can upload/download/search files. citeturn345168search0turn345168search1turn345168search2turn192520search0turn192520search1
> 
> ## The architecture
> 
> ```text
> Google Contacts ─┐
> Google Calendar ─┤
> Google Tasks ────┤
> Google Sheets ───┤
> Google Drive ────┤
> Google Keep ─────┘
>         ↓
>      QiConnect
>         ↓
>    Supabase mirror / canonical records
>         ↓
> Mom Care App / QiLife / dashboards
> ```
> 
> ## The important distinction
> 
> ### Contacts
> 
> For contacts, I’d let **Google Contacts be the daily source**, because your phone already lives there.
> 
> Then Supabase stores mirrored/enriched records:
> 
> ```text
> google_contact_id
> display_name
> phone
> email
> relationship_type
> role
> organization
> care_context
> last_synced_at
> supabase_person_id
> ```
> 
> Example labels/groups:
> 
> ```text
> Mom Care / Doctors
> Mom Care / Pharmacy
> Mom Care / Humana
> Mom Care / Home Health
> QiLabs / Vendors
> QiLabs / Clients
> ```
> 
> ### Calendar
> 
> Google Calendar should be the **human-facing schedule**, especially for appointments and reminders you need on your phone.
> 
> Supabase should store the structured care schedule:
> 
> ```text
> care_schedule_items
> appointments
> medication_schedule_items
> transportation_events
> home_health_visits
> ```
> 
> Then QiConnect pushes approved items to Google Calendar.
> 
> ### Tasks
> 
> Google Tasks is fine for “do this today” execution. But care tasks should originate in Supabase, especially if they come from discharge instructions or medication contradictions.
> 
> Flow:
> 
> ```text
> Supabase care_tasks → Google Tasks
> Google completion status → Supabase task status
> ```
> 
> ### Sheets
> 
> Sheets remains your **staging grid**, especially for imports, med lists, Firefly-style exports, and quick cleanup. The Sheets API can create spreadsheets and read/write values, so it is a clean bridge tool. citeturn192520search0
> 
> ### Keep
> 
> Keep is the messy one. Google does have a Keep API, but the docs frame it for **enterprise admin/security use cases**, not as a normal consumer note automation backbone. citeturn345168search4turn345168search19
> 
> So Keep’s role should be:
> 
> ```text
> quick capture only
> ```
> 
> Not source-of-truth. Not automated care database. Not formal archive.
> 
> ## Where this lives
> 
> Put all Google integration under:
> 
> ```text
> 70_QiConnect/google/
> ```
> 
> Suggested structure:
> 
> ```text
> 70_QiConnect/
>   google/
>     README.md
>     google_integration_map.md
>     contacts/
>       README.md
>       contact_sync_spec.md
>     calendar/
>       README.md
>       calendar_sync_spec.md
>     tasks/
>       README.md
>       task_sync_spec.md
>     sheets/
>       README.md
>       sheets_staging_spec.md
>     drive/
>       README.md
>       qinexus_drive_blob_spec.md
>     keep/
>       README.md
>       keep_capture_policy.md
> ```
> 
> ## The rule that keeps this from becoming a circus
> 
> ```text
> Google tools are interfaces.
> Supabase is the record.
> QiConnect is the treaty between them.
> ```
> 
> ## The smart build order
> 
> 1. **Contacts mirror first**  
>    Doctors, pharmacies, Humana, home health, family, vendors.
> 
> 2. **Calendar sync second**  
>    Appointments, home health visits, med review calls, transport windows.
> 
> 3. **Tasks sync third**  
>    Care follow-ups, discharge checklist items, doctor questions.
> 
> 4. **Drive/QiNexus already counts**  
>    Keep using Drive as blob storage for documents.
> 
> 5. **Sheets as staging**  
>    For imports and cleanup.
> 
> 6. **Keep last, and lightly**  
>    Only as an inbox. Don’t let it become another brain swamp.
> 
> ## Bottom line
> 
> Yes — Google ecosystem integration belongs in QiConnect.
> 
> Not because “Google cute.” Because your phone, contacts, calendar, Drive, and daily reminders already live there. That’s real leverage.
> 
> Use this model:
> 
> ```text
> Google = where life happens
> Supabase = where truth lives
> QiConnect = how truth and life stay synced
> ```

### User
> so we need the adr for this and affine and the codex prompt to get affine up and running with everythign i need now, tailscale ect.

### Assistant
> Got it. We’re going to lock this into **two ADRs + one Codex prompt**: one for AFFiNE placement/role, one for Google/QiConnect integration, then a fast server deployment prompt using Docker + Tailscale-first access.

### Assistant
> Yep. We need **two ADRs** and **one Codex prompt**.
> 
> I checked the current docs: AFFiNE’s self-host path is Docker Compose; Tailscale Serve is the right private phone-access layer, while Funnel is the public-internet option if you explicitly need it. Google Contacts/Calendar/Tasks/Sheets/Drive all have official APIs suitable for QiConnect mirroring. citeturn397523search0turn397523search6turn397523search12turn397523search2turn974451search0turn397523search5turn122124search1turn974451search2turn974451search9
> 
> ## ADR 001 — AFFiNE placement / role
> 
> :::writing{variant="document" id="38492"}
> # ADR-001: Self-host AFFiNE as a QiServer Workspace Service
> 
> ## Status
> 
> Accepted
> 
> ## Context
> 
> QiLabs needs a fast, visual, human-facing workspace for notes, maps, planning, care coordination, and active work. The workspace must support personal operations, QiDNA/QiSystem planning, and a separate Mom Care workspace.
> 
> AFFiNE is a third-party open-source workspace application. It is not a QiLabs-built product module and should not be treated as a QiApp.
> 
> AFFiNE has its own internal application database and service dependencies. Its internal tables should not be coupled directly to the canonical QiSystem Supabase schema.
> 
> ## Decision
> 
> Self-host AFFiNE under QiServer as an operated third-party service.
> 
> Canonical location:
> 
> `30_QiServer/40_services/affine`
> 
> AFFiNE will be used as:
> 
> - Visual workspace
> - Notes cockpit
> - Whiteboard/planning surface
> - QiDNA mirror/dashboard
> - Mom Care workspace surface
> - Human-readable command center
> 
> AFFiNE will not be used as:
> 
> - Canonical database
> - Supabase replacement
> - Medical source of truth
> - Financial source of truth
> - Direct schema authority
> - QiApp product code
> 
> Supabase remains the canonical source of truth for structured care, system, finance, and operational data.
> 
> QiConnect will handle future mirroring/sync between AFFiNE and Supabase using reviewed workflows.
> 
> ## Architecture
> 
> `AFFiNE → QiConnect review/staging → Supabase canonical tables`
> 
> AFFiNE may produce or display records, but approved structured records live in Supabase.
> 
> AFFiNE should initially run with its own local/container Postgres and Redis stack.
> 
> Do not point AFFiNE at the primary QiSystem Supabase database.
> 
> ## Access
> 
> Use Tailscale first for private access from phone and trusted devices.
> 
> Preferred access model:
> 
> - Local server: `http://localhost:3010`
> - Tailscale private access: via Tailscale Serve or direct Tailscale IP/MagicDNS
> - Public access later: Cloudflare Tunnel or Tailscale Funnel only after auth/security review
> 
> ## Consequences
> 
> Benefits:
> 
> - Fast deployment
> - Self-hosted control
> - Clean QiServer placement
> - No Notion-style vendor lock-in as core infrastructure
> - Keeps Supabase clean
> - Supports future QiConnect bridge
> 
> Tradeoffs:
> 
> - Requires Docker/Tailscale/server maintenance
> - AFFiNE internal data is not automatically canonical
> - Backup strategy must include AFFiNE Postgres/storage volumes
> - Public sharing requires careful security handling
> 
> ## Follow-up Tasks
> 
> - Create service folder under QiServer
> - Deploy AFFiNE with Docker Compose
> - Configure Tailscale access
> - Create workspace templates:
>   - QiOS Command Center
>   - Mom Care Command Center
> - Add future QiConnect AFFiNE bridge scaffolding under `70_QiConnect/affine`
> :::
> 
> ## ADR 002 — Google ecosystem + QiConnect
> 
> :::writing{variant="document" id="73518"}
> # ADR-002: Use Google Workspace Tools as Daily-Life Interfaces Mirrored Through QiConnect
> 
> ## Status
> 
> Accepted
> 
> ## Context
> 
> QiLabs already uses Google Drive as the blob/storage layer for QiNexus. The user also heavily uses Google Contacts, Calendar, Tasks, Sheets, and potentially Keep in daily life.
> 
> These tools are already integrated into the user’s phone and workflow. Instead of replacing them, QiLabs should mirror and coordinate them through QiConnect while keeping Supabase as the canonical structured record layer.
> 
> ## Decision
> 
> Use Google tools as daily-life interfaces, not as the entire source of truth.
> 
> Google tools will be integrated through QiConnect.
> 
> Role map:
> 
> - Google Drive: QiNexus blob/file storage
> - Google Contacts: daily contact/address book layer
> - Google Calendar: human-facing schedule and appointment layer
> - Google Tasks: execution/reminder layer for approved tasks
> - Google Sheets: staging/import/review grid layer
> - Google Keep: lightweight quick-capture inbox only
> 
> Supabase remains canonical for structured records.
> 
> QiConnect handles synchronization, enrichment, linking, deduplication, and audit references.
> 
> ## Architecture
> 
> `Google Tools → QiConnect → Supabase`
> 
> and, where appropriate:
> 
> `Supabase approved records → QiConnect → Google Calendar/Tasks/Contacts`
> 
> ## Source-of-Truth Rules
> 
> ### Contacts
> 
> Google Contacts may remain the daily-life contact source.
> 
> Supabase stores mirrored/enriched people/provider records.
> 
> Examples:
> 
> - doctors
> - pharmacies
> - Humana contacts
> - home health contacts
> - family
> - vendors
> - clients
> 
> ### Calendar
> 
> Google Calendar is the visible schedule layer.
> 
> Supabase stores canonical care appointments, medication review calls, follow-ups, and schedule items.
> 
> Approved Supabase schedule records may sync outward to Google Calendar.
> 
> ### Tasks
> 
> Google Tasks is the execution checklist layer.
> 
> Supabase owns care tasks, follow-up tasks, contradiction review tasks, and approval-required tasks.
> 
> Approved tasks may sync to Google Tasks.
> 
> ### Sheets
> 
> Google Sheets is used for staging/import review only.
> 
> Sheets are not canonical.
> 
> ### Drive
> 
> Google Drive is the blob layer for documents, uploads, PDFs, images, and source files.
> 
> Supabase stores metadata, references, extracted facts, and document IDs.
> 
> ### Keep
> 
> Google Keep is permitted only as a temporary capture inbox.
> 
> Keep is not canonical and should not be relied on for formal automation until explicitly supported by a stable workflow.
> 
> ## Consequences
> 
> Benefits:
> 
> - Uses tools already active in daily life
> - Reduces duplicate data entry
> - Makes phone-based operations easier
> - Preserves Supabase as the clean database layer
> - Supports Mom Care app workflows
> - Supports future automation and mirroring
> 
> Risks:
> 
> - Sync conflicts must be handled carefully
> - Google OAuth/security must be scoped tightly
> - Medical/care records require audit trails
> - Comments/suggestions must not overwrite approved care plans directly
> 
> ## Required Future Tables
> 
> Potential Supabase tables:
> 
> - qiconnect_sources
> - qiconnect_external_refs
> - qiconnect_sync_runs
> - qiconnect_sync_events
> - google_contacts_mirror
> - google_calendar_event_links
> - google_task_links
> - google_drive_file_refs
> - google_sheet_import_batches
> 
> ## Approval Rule
> 
> For Mom Care workflows:
> 
> Google tools may create or surface suggestions, reminders, and tasks.
> 
> Only approved changes in the care app/Supabase may alter the canonical care plan, medication schedule, taper schedule, or active care instructions.
> :::
> 
> ## Codex prompt — get AFFiNE running now with Tailscale
> 
> Paste this into Codex in tmux:
> 
> :::writing{variant="standard" id="61947"}
> Goal:
> Get AFFiNE self-hosted, running, viewable, and usable from my phone quickly using Docker Compose and Tailscale. Prioritize a working private-access deployment over perfect production polish.
> 
> Important classification:
> AFFiNE is a third-party workspace service operated by QiServer. It is not a QiApp.
> 
> Correct location:
> Prefer:
> 
> `/srv/QiLabs/30_QiServer/40_services/affine`
> 
> If `/srv/QiLabs` does not exist, search for the QiLabs root. If no QiLabs root exists, use:
> 
> `~/QiLabs/30_QiServer/40_services/affine`
> 
> Rules:
> - Do not connect AFFiNE to the main QiSystem Supabase database.
> - Use AFFiNE’s own Docker Compose stack with its own Postgres/Redis/storage.
> - Do not edit existing production reverse proxy or Cloudflare configs destructively.
> - Do not spend time building a perfect production deployment.
> - Get local access working first.
> - Then get private phone access working through Tailscale.
> - Only use Tailscale Funnel if I explicitly ask for public internet access.
> - Do not commit secrets.
> - Create `.env.example`, but keep the real `.env` uncommitted.
> - Do not overwrite existing AFFiNE data if already present.
> 
> Phase 1: inspect environment
> 
> Run:
> 
> ```bash
> pwd
> whoami
> hostname
> uname -a
> docker --version || true
> docker compose version || true
> tailscale version || true
> cloudflared --version || true
> ```
> 
> If Docker or Docker Compose is missing, report it clearly. If this is a Debian/Ubuntu server with sudo available, ask before installing Docker. Do not start a huge installation without confirming.
> 
> Phase 2: create AFFiNE service directory
> 
> Use the best detected QiLabs root.
> 
> ```bash
> mkdir -p /srv/QiLabs/30_QiServer/40_services/affine
> cd /srv/QiLabs/30_QiServer/40_services/affine
> mkdir -p data config storage backups logs
> ```
> 
> If `/srv/QiLabs` is not valid, use the detected/created fallback path and report it.
> 
> Phase 3: pull official AFFiNE Docker Compose files
> 
> Inside the AFFiNE folder, download the official latest release compose/env files:
> 
> ```bash
> curl -fsSL -o docker-compose.yml "https://github.com/toeverything/affine/releases/latest/download/docker-compose.yml"
> curl -fsSL -o .env "https://github.com/toeverything/affine/releases/latest/download/default.env.example"
> ```
> 
> If those fail, stop and report the exact failure. Do not invent a Docker Compose file from memory unless the official file cannot be downloaded and I explicitly approve a fallback.
> 
> Phase 4: configure fast local access
> 
> Edit `.env` safely.
> 
> Set values if the variables exist:
> 
> ```bash
> AFFINE_REVISION=stable
> PORT=3010
> AFFINE_SERVER_HOST=0.0.0.0
> AFFINE_SERVER_HTTPS=false
> AFFINE_SERVER_EXTERNAL_URL=http://localhost:3010
> ```
> 
> Do not configure SMTP, AI keys, OAuth, or production domain right now.
> 
> Create `.gitignore`:
> 
> ```bash
> cat > .gitignore <<'EOF'
> .env
> data/
> config/
> storage/
> backups/
> logs/
> *.log
> EOF
> ```
> 
> Create `.env.example` from `.env` with obvious secret placeholders if needed.
> 
> Phase 5: start AFFiNE
> 
> Run:
> 
> ```bash
> docker compose config
> docker compose pull
> docker compose up -d
> docker compose ps
> docker compose logs --tail=160
> ```
> 
> Then test:
> 
> ```bash
> curl -I http://localhost:3010 || curl -I http://127.0.0.1:3010
> ```
> 
> If AFFiNE uses a different mapped port according to the compose file, detect and report the actual port using:
> 
> ```bash
> docker compose ps
> docker ps --format 'table {{.Names}}\t{{.Ports}}\t{{.Status}}'
> ```
> 
> Phase 6: install/configure Tailscale only if needed
> 
> Check whether Tailscale is installed:
> 
> ```bash
> tailscale status || true
> ```
> 
> If Tailscale is installed but not connected, run:
> 
> ```bash
> sudo tailscale up --ssh
> ```
> 
> Show me the login URL if one appears.
> 
> If Tailscale is not installed and this is Debian/Ubuntu with sudo available, install using the official install script:
> 
> ```bash
> curl -fsSL https://tailscale.com/install.sh | sh
> sudo tailscale up --ssh
> ```
> 
> If sudo is unavailable or install fails, report the blocker.
> 
> Phase 7: make AFFiNE reachable privately from my phone
> 
> After Tailscale is connected, get the Tailscale IP and hostname:
> 
> ```bash
> tailscale ip -4
> tailscale status
> hostname
> ```
> 
> First access method:
> Tell me to open this from my phone while connected to Tailscale:
> 
> ```text
> http://TAILSCALE_IP:3010
> ```
> 
> Then attempt Tailscale Serve for a cleaner HTTPS/private tailnet URL:
> 
> ```bash
> tailscale serve --bg http://127.0.0.1:3010
> tailscale serve status
> ```
> 
> Report whatever HTTPS/MagicDNS URL Tailscale gives.
> 
> Do not enable Tailscale Funnel unless explicitly requested.
> 
> Phase 8: optional temporary public access fallback
> 
> Only if Tailscale is unavailable and cloudflared is already installed, create a temporary Cloudflare quick tunnel:
> 
> ```bash
> tmux new-session -d -s affine-tunnel 'cloudflared tunnel --url http://localhost:3010'
> sleep 5
> tmux capture-pane -pt affine-tunnel -S -200
> ```
> 
> Report the `trycloudflare.com` URL.
> 
> Do not make this the permanent setup.
> 
> Phase 9: create quick README
> 
> Create `README.md` in the AFFiNE service folder:
> 
> Include:
> - AFFiNE purpose in QiLabs
> - Why it lives under `30_QiServer/40_services/affine`
> - Start command: `docker compose up -d`
> - Stop command: `docker compose down`
> - Logs command: `docker compose logs -f`
> - Local URL
> - Tailscale phone URL
> - Backup TODO
> - Reverse proxy/domain TODO
> - Note: AFFiNE is not the canonical care database; Supabase remains source of truth
> 
> Phase 10: final report
> 
> Give me a short final report with only:
> 
> 1. AFFiNE running: yes/no
> 2. Folder path used
> 3. Local URL
> 4. Tailscale phone URL
> 5. Tailscale Serve URL, if available
> 6. Docker containers/status
> 7. Any blocker
> 8. Next single action for me
> 
> Expected user action after success:
> - Open AFFiNE from phone
> - Create account
> - Create two workspaces:
>   1. QiOS Command Center
>   2. Mom Care Command Center
> :::
> 
> ## Your real next move
> 
> Run the prompt. When Codex gives you the URL, open it from your phone **with Tailscale on**.
> 
> Do **not** start routing public domains tonight unless AFFiNE is already working privately. Public polish before private success is how we summon the tech goblins.

### User
> we should also start tracking the prompts too in .md just ot know what we sent, in the dna. ok, give me that setup to ill copy paste your response into the ide.

### Assistant
> Yes. **Prompt tracking belongs in QiDNA**, because prompts are part of the operating system’s decision/history layer.
> 
> Put it here:
> 
> ```text
> C:\QiLabs\01_QiDNA\90_ai_prompts
> ```
> 
> Use this Codex/IDE prompt:
> 
> :::writing{variant="standard" id="52718"}
> Goal:
> Create a clean AI prompt tracking system inside QiDNA so we can preserve important prompts sent to Codex, Gemini, ChatGPT, Claude, local agents, IDE agents, and future automation tools.
> 
> Location:
> Use the current QiLabs root. Preferred path:
> 
> C:\QiLabs\01_QiDNA\90_ai_prompts
> 
> If the locked root is named differently in this repo, use the current QiDNA root and report the exact path used.
> 
> Purpose:
> This folder stores important prompts as Markdown files so we know:
> - what was sent
> - to which AI/tool
> - when it was sent
> - why it was sent
> - what repo/module it affected
> - whether it was executed
> - what result happened
> - what follow-up is needed
> 
> Rules:
> - Do not store API keys, secrets, credentials, tokens, passwords, private medical documents, or raw sensitive records in prompt files.
> - If a prompt references sensitive material, summarize the context and link to the proper secure/source location instead of copying full sensitive content.
> - Do not overwrite existing prompt files.
> - Use Markdown.
> - Use underscores, no spaces, in filenames.
> - Use date-prefixed filenames.
> - Keep this compatible with Obsidian and normal GitHub viewing.
> 
> Create this structure:
> 
> C:\QiLabs\01_QiDNA\90_ai_prompts
> C:\QiLabs\01_QiDNA\90_ai_prompts\00_index
> C:\QiLabs\01_QiDNA\90_ai_prompts\10_codex
> C:\QiLabs\01_QiDNA\90_ai_prompts\20_gemini
> C:\QiLabs\01_QiDNA\90_ai_prompts\30_chatgpt
> C:\QiLabs\01_QiDNA\90_ai_prompts\40_claude
> C:\QiLabs\01_QiDNA\90_ai_prompts\50_local_agents
> C:\QiLabs\01_QiDNA\90_ai_prompts\60_templates
> C:\QiLabs\01_QiDNA\90_ai_prompts\70_prompt_chains
> C:\QiLabs\01_QiDNA\90_ai_prompts\80_results_notes
> C:\QiLabs\01_QiDNA\90_ai_prompts\90_archive
> 
> Create these files:
> 
> 1. C:\QiLabs\01_QiDNA\90_ai_prompts\README.md
> 
> Include:
> - What this folder is for
> - What belongs here
> - What does not belong here
> - Naming convention
> - How to log a prompt
> - How to link prompt chains
> - Reminder that secrets/sensitive raw records do not belong here
> 
> 2. C:\QiLabs\01_QiDNA\90_ai_prompts\00_index\prompt_register.md
> 
> Create a table with columns:
> 
> | Date | Prompt ID | Tool | Title | Related Module | Status | Result | Follow-up |
> |---|---|---|---|---|---|---|---|
> 
> Add starter rows for:
> - AFFiNE server deployment prompt
> - AFFiNE ADR / placement prompt
> - Google QiConnect ADR prompt
> - Mom Care app Gemini product prompt
> 
> Use status values:
> - drafted
> - sent
> - running
> - completed
> - failed
> - superseded
> - archived
> 
> 3. C:\QiLabs\01_QiDNA\90_ai_prompts\60_templates\prompt_log_template.md
> 
> Template content:
> 
> # Prompt Log: {{title}}
> 
> ## Metadata
> 
> - Prompt ID:
> - Date:
> - Tool:
> - Model/Agent:
> - Conversation/Session:
> - Related QiLabs Module:
> - Related Repo Path:
> - Status:
> - Priority:
> - Created By:
> - Last Updated:
> 
> ## Purpose
> 
> What this prompt was meant to accomplish.
> 
> ## Context
> 
> Relevant background. Do not include secrets or raw sensitive records.
> 
> ## Prompt Sent
> 
> ```text
> Paste prompt here.
> ```
> 
> ## Expected Output
> 
> What the agent/model was supposed to produce.
> 
> ## Actual Result
> 
> What happened after the prompt was run.
> 
> ## Files Created or Modified
> 
> | Path | Created/Modified | Notes |
> |---|---|---|
> 
> ## Decisions Made
> 
> - 
> 
> ## Follow-up Needed
> 
> - 
> 
> ## Safety / Privacy Notes
> 
> - 
> 
> ## Related Prompts
> 
> - 
> 
> 4. C:\QiLabs\01_QiDNA\90_ai_prompts\60_templates\prompt_chain_template.md
> 
> Template content:
> 
> # Prompt Chain: {{chain_title}}
> 
> ## Chain Purpose
> 
> What this chain is trying to accomplish.
> 
> ## Related Project / Module
> 
> - Module:
> - Repo Path:
> - System Area:
> 
> ## Prompt Sequence
> 
> | Step | Date | Prompt ID | Tool | Purpose | Result | Next |
> |---|---|---|---|---|---|---|
> 
> ## Current State
> 
> What is true now.
> 
> ## Open Threads
> 
> - 
> 
> ## Final Outcome
> 
> Document the final result when complete.
> 
> 5. C:\QiLabs\01_QiDNA\90_ai_prompts\10_codex\2026-06-15_affine_server_deploy_prompt.md
> 
> Create a prompt log for the AFFiNE Docker/Tailscale deployment prompt. If the exact prompt is available in the conversation or clipboard, paste it into the “Prompt Sent” section. If not available, create the metadata and leave:
> 
> ```text
> TODO: Paste final AFFiNE deployment prompt here.
> ```
> 
> Use:
> - Prompt ID: PROMPT-2026-06-15-001
> - Tool: Codex
> - Related Module: 30_QiServer
> - Related Repo Path: 30_QiServer/40_services/affine
> - Status: drafted
> 
> 6. C:\QiLabs\01_QiDNA\90_ai_prompts\20_gemini\2026-06-15_mom_care_single_source_of_truth_app.md
> 
> Create a prompt log for the Gemini Mom Care app product prompt.
> 
> Use:
> - Prompt ID: PROMPT-2026-06-15-002
> - Tool: Gemini
> - Related Module: Mom Care / QiLife / QiSystem
> - Related Repo Path: TBD
> - Status: drafted
> 
> If the exact prompt is not available, leave:
> ```text
> TODO: Paste final Gemini Mom Care app prompt here.
> ```
> 
> 7. C:\QiLabs\01_QiDNA\90_ai_prompts\30_chatgpt\2026-06-15_affine_google_adr_setup.md
> 
> Create a prompt log for the ADR setup covering:
> - AFFiNE as QiServer service
> - Google ecosystem as QiConnect integration layer
> 
> Use:
> - Prompt ID: PROMPT-2026-06-15-003
> - Tool: ChatGPT
> - Related Module: 01_QiDNA / 30_QiServer / 70_QiConnect
> - Status: drafted
> 
> 8. C:\QiLabs\01_QiDNA\90_ai_prompts\70_prompt_chains\2026-06-15_affine_qiconnect_google_setup_chain.md
> 
> Create a prompt chain file that links:
> 
> - PROMPT-2026-06-15-001 AFFiNE server deployment prompt
> - PROMPT-2026-06-15-002 Mom Care single-source app Gemini prompt
> - PROMPT-2026-06-15-003 AFFiNE/Google ADR setup prompt
> 
> Purpose:
> Track the setup of AFFiNE, QiConnect Google integration, and Mom Care app direction.
> 
> 9. Update or create:
> C:\QiLabs\01_QiDNA\90_ai_prompts\00_index\prompt_register.md
> 
> Add all created starter prompts to the register.
> 
> Naming convention:
> Use:
> 
> YYYY-MM-DD_short_descriptive_title.md
> 
> Examples:
> - 2026-06-15_affine_server_deploy_prompt.md
> - 2026-06-15_mom_care_single_source_of_truth_app.md
> - 2026-06-15_google_qiconnect_adr.md
> 
> Prompt ID convention:
> Use:
> 
> PROMPT-YYYY-MM-DD-###
> 
> // Example:
> PROMPT-2026-06-15-001
> 
> Also create a short file:
> C:\QiLabs\01_QiDNA\90_ai_prompts\README_PROMPT_RULES.md
> 
> Include these rules:
> 
> # Prompt Tracking Rules
> 
> 1. Important prompts get logged.
> 2. Prompts that change architecture, schemas, deployment, medical/care systems, finance systems, legal/evidence workflows, or production services must be logged.
> 3. Do not log secrets.
> 4. Do not log raw sensitive records unless explicitly necessary and approved.
> 5. Prefer summaries plus source references for sensitive context.
> 6. Every logged prompt should have a status.
> 7. Every prompt that results in file changes should list changed files.
> 8. Superseded prompts should be marked, not deleted.
> 9. Prompt chains should be used when multiple prompts are part of one larger build.
> 10. QiDNA stores decision/prompt history; operational code belongs in the relevant module.
> 
> After creating files, report:
> - folders created
> - files created
> - exact QiDNA path used
> - any existing files skipped
> - what I should paste manually if exact prompt text was not available
> :::
> 
> This is the right move. **Prompts are now part of the system history**, not random chat confetti.
