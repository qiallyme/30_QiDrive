---
layout: page
title: "Supabase Module Placement"
slug: "supabase_module_placement"
created_at: "2026-06-13 13:42:40"
updated_at: "2026-07-16T06:49:33-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-009.json"
template_key: master-template
date: 2026-06-13
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a2da483-ff10-83ea-b5d4-7cc7d287760a"
canonical_ref: ""
---

# Supabase Module Placement

## Overview
- **Date**: 2026-06-13 13:42:40
- **Conversation ID**: `6a2da483-ff10-83ea-b5d4-7cc7d287760a`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> ok quick questions, i want to use github for my supabase project and i wanted to know what module supabaSE IS, is it in qisystem or qiconnect?

### Assistant
> Supabase should **not** live inside **QiConnect**.
> 
> **Correct placement: `QiSystem` / infrastructure layer** — with one nuance:
> 
> ## Supabase = QiSystem infrastructure
> 
> Put it under something like:
> 
> ```text
> 30_QiSystem/
>   40_data/
>     supabase/
>       migrations/
>       schemas/
>       policies/
>       seed/
>       functions/
> ```
> 
> or:
> 
> ```text
> 30_QiServer/
>   supabase/
> ```
> 
> depending on whether you’re organizing by **doctrine/module** or by **deployed server/runtime**.
> 
> ## Why not QiConnect?
> 
> **QiConnect** is for integrations and communication pathways:
> 
> - Gmail
> - Calendar
> - APIs
> - webhooks
> - external app sync
> - messaging
> - connectors
> - import/export flows
> 
> Supabase is not just “a connection.” It is your **system database/backend platform**.
> 
> So:
> 
> | Thing | Module |
> |---|---|
> | Supabase database schema | **QiSystem** |
> | Supabase migrations | **QiSystem** |
> | RLS policies | **QiSystem** |
> | Edge functions | **QiSystem**, unless integration-specific |
> | Gmail → Supabase sync | **QiConnect** |
> | Lyft/Hertz data import into Supabase | **QiConnect** |
> | QiLife reading/writing Supabase | **QiLife app layer using QiSystem backend** |
> 
> ## Clean rule
> 
> **QiSystem owns the database. QiConnect feeds the database. QiLife uses the database. QiDNA documents the database.**
> 
> That’s the clean architecture.
> 
> So for GitHub, I’d treat Supabase as part of either:
> 
> ```text
> 30_QiSystem
> ```
> 
> or if this repo is server-specific:
> 
> ```text
> 30_QiServer/supabase
> ```
> 
> But conceptually? **QiSystem.**

### User
> whre should i store all teh connection files and stuff and keys for this database, im not trying to be looking for the ish every time.

### Assistant
> Store them in **two places**, depending on whether they are **reference/config** or **actual secrets**.
> 
> ## Clean rule
> 
> **GitHub stores structure. Server/password manager stores secrets.**
> 
> Do **not** put real database passwords, service-role keys, JWT secrets, or `.env` files in GitHub. That will bite you later.
> 
> ---
> 
> ## Best structure
> 
> ### In the repo / QiSystem
> 
> This is where the Supabase project lives:
> 
> ```text
> 30_QiSystem/
>   40_data/
>     supabase/
>       README.md
>       connection-map.md
>       .env.example
>       supabase/
>         config.toml
>         migrations/
>         seed.sql
>         functions/
>         schemas/
>         policies/
>         sql/
> ```
> 
> This folder should contain:
> 
> | File | Purpose | Safe for GitHub? |
> |---|---|---|
> | `README.md` | What this Supabase project is | Yes |
> | `connection-map.md` | Where keys live, what apps use them | Yes, but no secret values |
> | `.env.example` | Template with fake values | Yes |
> | `supabase/config.toml` | Supabase CLI config | Usually yes |
> | `migrations/` | Database migration history | Yes |
> | `schemas/` | Canonical schema docs/sql | Yes |
> | `policies/` | RLS policy docs/sql | Yes |
> | `functions/` | Edge functions | Yes, unless secrets hardcoded |
> 
> ---
> 
> ## Actual secrets go here
> 
> ### On the server
> 
> Use a single predictable runtime secrets folder:
> 
> ```text
> /srv/qios/_secrets/supabase/
>   local.env
>   staging.env
>   prod.env
>   README.md
> ```
> 
> Then lock it down:
> 
> ```bash
> sudo mkdir -p /srv/qios/_secrets/supabase
> sudo chmod 700 /srv/qios/_secrets
> sudo chmod 700 /srv/qios/_secrets/supabase
> ```
> 
> For each env file:
> 
> ```bash
> sudo chmod 600 /srv/qios/_secrets/supabase/prod.env
> ```
> 
> That way you always know:
> 
> > Supabase secrets are in `/srv/qios/_secrets/supabase/`.
> 
> No hunting. No chaos goblin scavenger hunt.
> 
> ---
> 
> ## What goes in `.env.example`
> 
> Commit this:
> 
> ```env
> SUPABASE_URL=https://your-project.supabase.co
> SUPABASE_ANON_KEY=replace_me
> SUPABASE_SERVICE_ROLE_KEY=replace_me_do_not_commit_real_value
> SUPABASE_DB_HOST=db.your-project.supabase.co
> SUPABASE_DB_PORT=5432
> SUPABASE_DB_NAME=postgres
> SUPABASE_DB_USER=postgres
> SUPABASE_DB_PASSWORD=replace_me_do_not_commit_real_value
> DATABASE_URL=postgresql://postgres:replace_me@db.your-project.supabase.co:5432/postgres
> ```
> 
> But the real values go in:
> 
> ```text
> /srv/qios/_secrets/supabase/prod.env
> ```
> 
> and maybe your local machine:
> 
> ```text
> 30_QiSystem/40_data/supabase/.env.local
> ```
> 
> but `.env.local` must be ignored.
> 
> ---
> 
> ## Add this to `.gitignore`
> 
> ```gitignore
> .env
> .env.*
> !.env.example
> 
> **/secrets/
> **/_secrets/
> *.pem
> *.key
> *.p12
> *.crt
> 
> .supabase/
> ```
> 
> The exception keeps `.env.example` committed while blocking real env files.
> 
> ---
> 
> ## My recommended Qi architecture
> 
> Use this split:
> 
> ```text
> _QiOS_DNA/
>   30_QiSystem/
>     40_data/
>       supabase/
>         connection-map.md
>         schema-catalog.md
>         field-catalog.md
>         policy-catalog.md
> 
> 30_QiServer/
>   secrets-pointer.md
> ```
> 
> Actual server:
> 
> ```text
> /srv/qios/_secrets/supabase/prod.env
> ```
> 
> GitHub repo:
> 
> ```text
> 30_QiSystem/40_data/supabase/
> ```
> 
> ## The key distinction
> 
> **QiSystem owns Supabase.**  
> **QiServer holds runtime secrets.**  
> **QiDNA documents the map.**  
> **GitHub tracks everything except the actual keys.**
> 
> That’s the clean setup.

### User
> ok so i links supabase to the github to auto update production on push. thats good right. what do i need in the repo now for it to be helpful and here is hte

### Assistant
> Yes, that can be good — but only if the repo is migration-first and protected. Otherwise you just connected a loaded nail gun to production. I’ll give you the safe repo shape and the “do not skip this” guardrails.

### Assistant
> Yes — **linking Supabase to GitHub can be good**, especially for keeping schema changes versioned. But production auto-update is only good if you treat `main` like a protected deployment lane, not a playground.
> 
> Supabase’s GitHub integration can auto-deploy when you push or merge to the production branch. The important catch: it deploys **new migrations**, **Edge Functions declared in `config.toml`**, and **Storage buckets declared in `config.toml`**. It does **not** deploy everything — Auth/API settings and seed files are ignored by default for production. citeturn794432view0
> 
> ## What the repo needs now
> 
> At minimum, your repo needs this:
> 
> ```text
> 30_QiSystem/
>   40_data/
>     supabase/
>       README.md
>       connection-map.md
>       .env.example
>       supabase/
>         config.toml
>         migrations/
>         functions/
>         seed.sql
>         schemas/
>         policies/
>         storage/
>         tests/
> ```
> 
> But if Supabase is linked directly to the repo, it may expect the actual Supabase CLI folder to be at repo root:
> 
> ```text
> supabase/
>   config.toml
>   migrations/
>   functions/
>   seed.sql
> ```
> 
> So the clean move is:
> 
> ```text
> repo-root/
>   supabase/
>     config.toml
>     migrations/
>     functions/
>     seed.sql
> 
>   docs/
>     supabase/
>       README.md
>       connection-map.md
>       schema-catalog.md
>       field-catalog.md
>       policy-catalog.md
> 
>   .env.example
>   .gitignore
> ```
> 
> That keeps Supabase happy **and** keeps QiDNA organized.
> 
> ## The important files
> 
> | File / folder | Why it matters |
> |---|---|
> | `supabase/config.toml` | Supabase CLI/project config; created by `supabase init`. citeturn794432view1turn794432view3 |
> | `supabase/migrations/` | The actual database change history. This is the big one. |
> | `supabase/functions/` | Edge Functions, if you use them. |
> | `supabase/seed.sql` | Sample/dev seed data. Useful for preview/local, but not merged into production by default. citeturn794432view0 |
> | `.env.example` | Safe template showing what keys are needed, without real values. |
> | `docs/supabase/connection-map.md` | Your “where the hell is everything” map. |
> | `docs/supabase/schema-catalog.md` | Human-readable table/schema catalog. |
> | `docs/supabase/field-catalog.md` | Master field registry. |
> | `docs/supabase/policy-catalog.md` | RLS policy inventory. |
> 
> ## Do this before you trust production auto-deploy
> 
> ### 1. Turn on required checks in GitHub
> 
> Supabase specifically recommends requiring the Supabase integration check before merging so broken migrations cannot land in production. citeturn794432view0
> 
> Translation: **do not push straight to `main` like a goblin.**
> 
> Use:
> 
> ```text
> feature branch → pull request → Supabase check passes → merge to main → production deploys
> ```
> 
> ### 2. Never edit production manually unless you capture it
> 
> Supabase recommends local development with CLI/schema migrations so database changes are captured in version control. citeturn794432view2
> 
> So the rule is:
> 
> > Dashboard changes are temporary until they become migrations.
> 
> If you create tables in the Supabase Dashboard, immediately turn that into a migration with CLI diff/pull workflow.
> 
> ### 3. Keep secrets out of GitHub
> 
> Supabase docs say `config.toml` can reference environment variables, and `.env` should **not** be committed. citeturn794432view3
> 
> Your repo should have:
> 
> ```text
> .env.example
> ```
> 
> Not:
> 
> ```text
> .env
> .env.local
> prod.env
> service-role-key.txt
> database-password.txt
> ```
> 
> ## The repo should answer these questions fast
> 
> Your Supabase repo is “helpful” when it lets Future Cody answer:
> 
> 1. **What database is this?**
> 2. **What tables exist?**
> 3. **What fields are canonical?**
> 4. **What policies protect the tables?**
> 5. **What apps connect to it?**
> 6. **Where are the real keys stored?**
> 7. **How do I safely change production?**
> 
> That means you need these docs:
> 
> ```text
> docs/supabase/
>   README.md
>   connection-map.md
>   deployment-flow.md
>   schema-catalog.md
>   field-catalog.md
>   policy-catalog.md
>   app-integration-map.md
> ```
> 
> ## My exact recommendation for Qi
> 
> Use this as the mental model:
> 
> ```text
> GitHub repo:
>   supabase/                 ← what Supabase deploys
>   docs/supabase/            ← what Cody uses to understand it
> 
> QiDNA:
>   references/canonical docs ← published doctrine/catalog version
> 
> QiServer:
>   /srv/qios/_secrets/       ← real secrets only
> ```
> 
> ## Your next move
> 
> Put this in the repo first:
> 
> ```text
> supabase/
>   config.toml
>   migrations/
>   functions/
>   seed.sql
> 
> docs/supabase/
>   README.md
>   connection-map.md
>   deployment-flow.md
>   schema-catalog.md
>   field-catalog.md
>   policy-catalog.md
> 
> .env.example
> .gitignore
> ```
> 
> Then protect `main`.
> 
> That’s the difference between “GitHub auto-updates production” and “GitHub auto-breaks production.”

### User
> on adjustment i have this tree so far. what am i still missing and i want to start populating and migrating data. {

>   "name": "50_data",

>   "path": "c:\\QiLabs\\20_QiSystem\\50_data",

>   "type": "directory",

>   "children": [

>     {

>       "name": "supabase",

>       "type": "folder",

>       "children": [

>         {

>           "name": "50_database",

>           "type": "folder",

>           "children": [

>             {

>               "name": "functions",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "qivault-ingest",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.ts",

>                       "type": "file"

>                     }

>                   ]

>                 }

>               ]

>             },

>             {

>               "name": "migrations",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "001_ingestion_queue.sql",

>                   "type": "file"

>                 },

>                 {

>                   "name": "002_semantic_profile_file_level.sql",

>                   "type": "file"

>                 },

>                 {

>                   "name": "20260401000000_qione_admin_invite.sql",

>                   "type": "file"

>                 },

>                 {

>                   "name": "20260404000001_qios_modular_mode_pivot.sql",

>                   "type": "file"

>                 },

>                 {

>                   "name": "20260507045840_add_daily_care_notes.sql",

>                   "type": "file"

>                 },

>                 {

>                   "name": "20260508112922_medication_hold_and_inventory_workflows.sql",

>                   "type": "file"

>                 },

>                 {

>                   "name": "20260510090423_desktop_admin_admin_console_foundation.sql",

>                   "type": "file"

>                 },

>                 {

>                   "name": "qicase_schema.sql",

>                   "type": "file"

>                 },

>                 {

>                   "name": "qievidence.sql",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "policies",

>               "type": "folder"

>             },

>             {

>               "name": "schemas",

>               "type": "folder"

>             },

>             {

>               "name": "sql",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "is_admin.sql",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "config.toml",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": ".env.example",

>           "type": "file"

>         },

>         {

>           "name": "README.md",

>           "type": "file"

>         },

>         {

>           "name": "connection-map.md",

>           "type": "file"

>         }

>       ]

>     }

>   ],

>   "metadata": {

>     "generated": "2026-06-13T19:04:22.145Z",

>     "generator": "FileTree Pro Extension",

>     "version": "0.2.0",

>     "showIcons": false,

>     "maxDepth": 10

>   }

> }

### Assistant
> Your structure is close. The biggest issue I already see: you’re mixing “Supabase deployable project” and “QiSystem documentation wrapper.” That’s fixable, but we need to make the deployable path boring and predictable.

### Assistant
> You’re close. **The structure is workable, but you’re missing the “migration safety rails” and the “data loading pipeline.”** Right now it’s mostly a place where SQL files live. To start populating real data without making a mess, you need a few more layers.
> 
> ## First correction: your Supabase folder may be too deeply nested
> 
> You currently have:
> 
> ```text
> 20_QiSystem/
>   50_data/
>     supabase/
>       50_database/
>         config.toml
>         migrations/
>         functions/
> ```
> 
> That is clean for QiSystem organization, **but Supabase/GitHub usually expects the deployable Supabase project folder to look like this:**
> 
> ```text
> supabase/
>   config.toml
>   migrations/
>   functions/
> ```
> 
> Supabase docs show `supabase/config.toml` generated by `supabase init`, and GitHub integration runs migrations from the `migrations` subdirectory of the Supabase directory. citeturn282284search2turn282284search10
> 
> So I would not bury the actual deployable project under `50_database` unless you know the GitHub integration is configured to that path.
> 
> ## Recommended adjustment
> 
> Keep QiSystem docs where they are, but make the actual deployable folder predictable:
> 
> ```text
> 20_QiSystem/
>   50_data/
>     supabase/
>       README.md
>       connection-map.md
> 
>       supabase/              ← actual Supabase CLI/deploy folder
>         config.toml
>         migrations/
>         functions/
>         schemas/
>         seed.sql
> 
>       docs/
>         schema-catalog.md
>         field-catalog.md
>         policy-catalog.md
>         data-source-catalog.md
>         migration-runbook.md
> 
>       imports/
>         README.md
>         manifests/
>         templates/
>         samples/
> ```
> 
> Or if the GitHub repo root is only this Supabase project, then even better:
> 
> ```text
> repo-root/
>   supabase/
>     config.toml
>     migrations/
>     functions/
>     schemas/
>     seed.sql
> 
>   docs/
>     schema-catalog.md
>     field-catalog.md
>     policy-catalog.md
>     data-source-catalog.md
>     migration-runbook.md
> 
>   imports/
>     manifests/
>     templates/
>     samples/
> 
>   .env.example
>   .gitignore
>   README.md
> ```
> 
> ## What you are missing
> 
> ### 1. `seed.sql`
> 
> Add:
> 
> ```text
> supabase/seed.sql
> ```
> 
> This is for reproducible local/dev data. Supabase describes seeding as populating a database with initial data for reproducible local/testing environments. citeturn282284search7
> 
> Do **not** use this for all your real personal records. Use it for things like:
> 
> ```text
> default modules
> default statuses
> default source types
> default entity types
> admin bootstrap records
> safe fake examples
> ```
> 
> ### 2. `schemas/` needs actual canonical schema files
> 
> You have an empty `schemas` folder. Fill it.
> 
> Use:
> 
> ```text
> supabase/schemas/
>   00_extensions.sql
>   01_core.sql
>   02_qivault.sql
>   03_qicase.sql
>   04_qievidence.sql
>   05_qilife.sql
>   90_views.sql
>   99_grants.sql
> ```
> 
> Supabase supports declarative database schema files in `supabase/schemas`, then generating migrations from them. citeturn282284search4
> 
> This matters because:
> 
> > `schemas/` = desired final state  
> > `migrations/` = history of changes applied over time
> 
> Do not use migrations as your only source of truth. That gets ugly fast.
> 
> ### 3. `policies/` needs RLS source files
> 
> Your `policies` folder is empty. Fill it before loading sensitive data.
> 
> Suggested:
> 
> ```text
> supabase/policies/
>   qivault_policies.sql
>   qicase_policies.sql
>   qievidence_policies.sql
>   admin_policies.sql
>   service_role_policies.sql
> ```
> 
> For any table with personal, legal, financial, medical, family, client, or operational records: **RLS is not optional.**
> 
> ### 4. Add `imports/` for migration intake
> 
> This is the big missing piece for populating data.
> 
> Add:
> 
> ```text
> imports/
>   README.md
>   manifests/
>     2026-06-13_initial_import_manifest.csv
>   templates/
>     qibit_import_template.csv
>     evidence_import_template.csv
>     case_event_import_template.csv
>     contact_import_template.csv
>   samples/
>     sample_qibit_import.csv
> ```
> 
> Do **not** commit raw private exports unless they are sanitized. Real imports should live outside GitHub, probably:
> 
> ```text
> /srv/qios/intake/supabase/
> ```
> 
> or locally:
> 
> ```text
> C:\QiLabs\_LOCAL_ONLY\supabase-imports\
> ```
> 
> GitHub gets the **templates and manifests**, not the private guts.
> 
> ### 5. Add `migration-runbook.md`
> 
> You need one boring instruction file that tells Future Cody exactly how to change the database.
> 
> ```text
> docs/migration-runbook.md
> ```
> 
> It should answer:
> 
> ```text
> How to create a migration
> How to test locally
> How to push to GitHub
> How production gets updated
> How to roll back
> How to import data
> Where real secrets live
> What never goes in GitHub
> ```
> 
> ### 6. Add `data-source-catalog.md`
> 
> Before migrating data, make a source inventory.
> 
> ```text
> docs/data-source-catalog.md
> ```
> 
> Columns should be:
> 
> | Source | Type | Location | Owner | Sensitivity | Target Table | Import Status |
> |---|---|---|---|---|---|---|
> | Paperless exports | docs/files | `/srv/qios/intake/...` | Cody | high | `qivault_files` | pending |
> | Firefly III | finance | qiserver | Cody | high | `finance_transactions` | pending |
> | Medical care notes | notes | local/server | Cody | very high | `care_notes` | pending |
> | Legal evidence | docs/events | local/server | Cody | high | `qievidence_items` | pending |
> 
> This prevents “random CSV soup.” Random CSV soup is how systems die quietly.
> 
> ### 7. Add `generated/` or `types/`
> 
> Once you have tables, generate Supabase TypeScript types for your apps.
> 
> ```text
> supabase/types/
>   database.types.ts
> ```
> 
> This becomes useful for QiLife, QiAccess, admin console, ingest functions, etc.
> 
> ### 8. Fix migration naming
> 
> You currently have mixed naming:
> 
> ```text
> 001_ingestion_queue.sql
> 002_semantic_profile_file_level.sql
> 20260401000000_qione_admin_invite.sql
> ...
> qicase_schema.sql
> qievidence.sql
> ```
> 
> Going forward, use timestamped migration names only:
> 
> ```text
> 20260613193000_create_qivault_core.sql
> 20260613194500_create_import_batches.sql
> 20260613200000_create_qievidence_core.sql
> ```
> 
> Supabase migration examples use timestamped files under `supabase/migrations/`. citeturn282284search1turn282284search5
> 
> **Do not rename migrations that already ran in production** unless you know exactly what you’re doing. Just standardize from this point forward.
> 
> ## What I would add immediately
> 
> Your next tree should look like this:
> 
> ```text
> supabase/
>   config.toml
>   seed.sql
> 
>   migrations/
>     001_ingestion_queue.sql
>     002_semantic_profile_file_level.sql
>     20260401000000_qione_admin_invite.sql
>     20260404000001_qios_modular_mode_pivot.sql
>     20260507045840_add_daily_care_notes.sql
>     20260508112922_medication_hold_and_inventory_workflows.sql
>     20260510090423_desktop_admin_admin_console_foundation.sql
>     qicase_schema.sql
>     qievidence.sql
> 
>   schemas/
>     00_extensions.sql
>     01_core.sql
>     02_qivault.sql
>     03_qicase.sql
>     04_qievidence.sql
>     05_qilife.sql
>     90_views.sql
>     99_grants.sql
> 
>   policies/
>     00_rls_enable.sql
>     01_admin_policies.sql
>     02_qivault_policies.sql
>     03_qicase_policies.sql
>     04_qievidence_policies.sql
> 
>   functions/
>     qivault-ingest/
>       index.ts
>     _shared/
>       supabaseAdmin.ts
> 
>   types/
>     database.types.ts
> 
> docs/
>   schema-catalog.md
>   field-catalog.md
>   policy-catalog.md
>   data-source-catalog.md
>   migration-runbook.md
>   import-runbook.md
> 
> imports/
>   README.md
>   manifests/
>   templates/
>   samples/
> ```
> 
> For Edge Functions, Supabase recommends organizing functions under `supabase/functions`, with optional `_shared` code for shared function logic. citeturn282284search9
> 
> ## Data migration approach
> 
> Do **not** start by dumping final data straight into canonical tables. That is how you create permanent trash.
> 
> Use this flow:
> 
> ```text
> raw source file
>   ↓
> import batch
>   ↓
> staging table
>   ↓
> validation
>   ↓
> canonical table
>   ↓
> audit log
> ```
> 
> ### Add these migration tables first
> 
> You need:
> 
> ```text
> import_batches
> import_files
> import_errors
> source_records
> ```
> 
> Then domain-specific staging tables:
> 
> ```text
> staging_qivault_files
> staging_qicase_events
> staging_qievidence_items
> staging_contacts
> staging_finance_transactions
> ```
> 
> Then canonical tables:
> 
> ```text
> qibits
> qivault_files
> qicases
> qicase_events
> qievidence_items
> entities
> entity_links
> ```
> 
> ## My recommended first migration set
> 
> Start with these in order:
> 
> ```text
> 20260613190000_create_core_extensions.sql
> 20260613191000_create_admin_and_roles.sql
> 20260613192000_create_import_batches.sql
> 20260613193000_create_entities.sql
> 20260613194000_create_qibits.sql
> 20260613195000_create_qivault_files.sql
> 20260613200000_create_qicase_core.sql
> 20260613201000_create_qievidence_core.sql
> 20260613202000_enable_rls_baseline.sql
> ```
> 
> ## Practical next step
> 
> Before importing anything, create **one master intake table**:
> 
> ```sql
> create table if not exists public.import_batches (
>   id uuid primary key default gen_random_uuid(),
>   source_name text not null,
>   source_type text not null,
>   source_path text,
>   imported_by uuid,
>   import_status text not null default 'pending',
>   record_count integer default 0,
>   error_count integer default 0,
>   notes text,
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now()
> );
> ```
> 
> And one raw record table:
> 
> ```sql
> create table if not exists public.source_records (
>   id uuid primary key default gen_random_uuid(),
>   import_batch_id uuid references public.import_batches(id) on delete cascade,
>   source_record_id text,
>   source_table text,
>   source_payload jsonb not null,
>   normalized_payload jsonb,
>   target_table text,
>   target_id uuid,
>   processing_status text not null default 'pending',
>   error_message text,
>   created_at timestamptz not null default now(),
>   processed_at timestamptz
> );
> ```
> 
> That gives you a safe landing zone for messy data.
> 
> ## Bottom line
> 
> You are missing four critical things:
> 
> 1. **Canonical schema files** in `schemas/`
> 2. **RLS policy files** in `policies/`
> 3. **Import pipeline docs/templates/manifests**
> 4. **Staging/import tables before final tables**
> 
> Your current structure is a good shell. Now make it operational:
> 
> ```text
> schema first
> policies second
> import staging third
> canonical tables fourth
> real data last
> ```
> 
> Do it in that order or you’ll be cleaning up database glitter for weeks.

### User
> ok im giong to change the project name from 50_database to qisupabase and update the folder name to that.

### Assistant
> Yes — **`qisupabase` is better than `50_database`**.
> 
> `50_database` describes a layer.  
> `qisupabase` describes the actual project/module. Cleaner.
> 
> ## Approved structure
> 
> Use:
> 
> ```text
> 20_QiSystem/
>   50_data/
>     supabase/
>       qisupabase/
>         config.toml
>         migrations/
>         functions/
>         policies/
>         schemas/
>         sql/
> ```
> 
> That makes the hierarchy mean:
> 
> ```text
> QiSystem → data layer → Supabase platform → QiSupabase project
> ```
> 
> Good naming. Keep it.
> 
> ## But watch this one issue
> 
> If your Supabase GitHub integration expects the project folder to be named exactly:
> 
> ```text
> supabase/
> ```
> 
> then burying it as:
> 
> ```text
> supabase/qisupabase/
> ```
> 
> may cause deploy problems unless the integration lets you set the project directory.
> 
> So the strategic split is:
> 
> ### Best for Qi organization
> 
> ```text
> 20_QiSystem/50_data/supabase/qisupabase/
> ```
> 
> ### Best for Supabase auto-deploy compatibility
> 
> ```text
> repo-root/supabase/
> ```
> 
> ## My recommendation
> 
> Keep the folder name as **`qisupabase`**, but inside the GitHub repo, make sure the deployable Supabase folder is easy for tooling.
> 
> Option A — if this repo is only for Supabase:
> 
> ```text
> repo-root/
>   supabase/
>     config.toml
>     migrations/
>     functions/
>   docs/
>     qisupabase/
> ```
> 
> Option B — if this repo mirrors QiSystem structure:
> 
> ```text
> repo-root/
>   20_QiSystem/
>     50_data/
>       supabase/
>         qisupabase/
>           config.toml
>           migrations/
>           functions/
> ```
> 
> Only use Option B if Supabase/GitHub integration supports setting that nested project path.
> 
> ## Rename command
> 
> From:
> 
> ```bash
> cd /c/QiLabs/20_QiSystem/50_data/supabase
> mv 50_database qisupabase
> ```
> 
> Then check for path references:
> 
> ```bash
> grep -R "50_database" -n .
> ```
> 
> Update anything that still points to the old name.
> 
> ## Final naming rule
> 
> Use **`qisupabase`** for the project/module name.
> 
> Use **`supabase/`** only where the Supabase CLI or GitHub integration requires that exact folder convention.
> 
> Clean. Don’t let tooling bully the architecture — but don’t break deploy automation either.

### User
> ok give me a prompt for the ide to populate the general files we need to push and so i can see what supabase does.

### Assistant
> Paste this into your IDE agent/Aider/Codex. It tells it to **populate the safe general repo files** without touching secrets or doing anything destructive.
> 
> :::writing{variant="standard" id="49281"}
> You are working inside the QiSystem Supabase project.
> 
> Current intended project folder:
> 
> C:\QiLabs\20_QiSystem\50_data\supabase\qisupabase
> 
> Goal:
> Populate the basic Supabase repo structure so it is useful for GitHub/Supabase deployment testing, documentation, and future data migration work.
> 
> Important rules:
> 1. Do NOT add real secrets, passwords, Supabase service-role keys, database URLs, JWT secrets, API keys, or personal/private data.
> 2. Do NOT delete or rename existing migrations.
> 3. Do NOT rewrite existing migration files unless there is an obvious syntax-breaking issue, and if so, report it first.
> 4. Do NOT run production deploy commands.
> 5. Create missing folders and safe starter files only.
> 6. Use placeholder values in .env.example.
> 7. Keep this migration-first and GitHub-safe.
> 8. If there is already a file, update it carefully rather than replacing useful content.
> 
> Create or update this structure:
> 
> qisupabase/
>   README.md
>   connection-map.md
>   .env.example
>   .gitignore
>   config.toml
> 
>   migrations/
>     existing files stay untouched
>     add one new timestamped migration for import infrastructure only if no equivalent exists
> 
>   schemas/
>     00_extensions.sql
>     01_core.sql
>     02_imports.sql
>     03_qivault.sql
>     04_qicase.sql
>     05_qievidence.sql
>     90_views.sql
>     99_grants.sql
> 
>   policies/
>     00_rls_enable.sql
>     01_admin_policies.sql
>     02_import_policies.sql
>     03_qivault_policies.sql
>     04_qicase_policies.sql
>     05_qievidence_policies.sql
> 
>   sql/
>     is_admin.sql
>     updated_at_trigger.sql
> 
>   functions/
>     qivault-ingest/
>       index.ts
>     _shared/
>       supabaseAdmin.ts
> 
>   types/
>     README.md
> 
>   docs/
>     schema-catalog.md
>     field-catalog.md
>     policy-catalog.md
>     data-source-catalog.md
>     migration-runbook.md
>     import-runbook.md
>     deployment-flow.md
> 
>   imports/
>     README.md
>     manifests/
>       initial-import-manifest.csv
>     templates/
>       qibit_import_template.csv
>       evidence_import_template.csv
>       case_event_import_template.csv
>       contact_import_template.csv
>       file_import_template.csv
>     samples/
>       sample_qibit_import.csv
> 
> README.md should explain:
> - This is QiSupabase, the Supabase database/backend project for QiSystem.
> - Supabase is owned by QiSystem.
> - QiConnect feeds data into Supabase.
> - QiLife and other apps consume Supabase data.
> - Real secrets are not stored here.
> - Production changes should happen through migrations and protected GitHub branches.
> 
> connection-map.md should document:
> - Supabase dashboard URL placeholder
> - project ref placeholder
> - anon key location placeholder
> - service role key location placeholder
> - database password location placeholder
> - where local/server secrets are stored, using:
>   /srv/qios/_secrets/supabase/
> - connected apps:
>   QiLife
>   QiAccess
>   QiVault ingest
>   QiConnect integrations
> - no actual secrets
> 
> .env.example should include placeholder variables:
> SUPABASE_URL=
> SUPABASE_ANON_KEY=
> SUPABASE_SERVICE_ROLE_KEY=
> SUPABASE_DB_HOST=
> SUPABASE_DB_PORT=5432
> SUPABASE_DB_NAME=postgres
> SUPABASE_DB_USER=postgres
> SUPABASE_DB_PASSWORD=
> DATABASE_URL=
> 
> .gitignore should block:
> .env
> .env.*
> !.env.example
> **/_secrets/
> **/secrets/
> *.pem
> *.key
> *.p12
> *.crt
> node_modules/
> dist/
> .supabase/
> 
> docs/schema-catalog.md should create a starter catalog table with columns:
> Schema, Table, Purpose, Owner Module, Sensitivity, Status, Notes
> 
> docs/field-catalog.md should create a starter canonical field registry with columns:
> Field Name, Type, Meaning, Used In Tables, Required, Default, Notes
> 
> docs/policy-catalog.md should create a starter RLS/policy registry with columns:
> Table, RLS Enabled, Policy Name, Role, Operation, Rule Summary, Status
> 
> docs/data-source-catalog.md should create a starter source inventory with columns:
> Source, Type, Location, Owner, Sensitivity, Target Table, Import Status, Notes
> 
> docs/migration-runbook.md should document:
> - create migrations through Supabase CLI
> - test locally before pushing
> - never hand-edit production without capturing it in migration files
> - never commit secrets
> - protect main branch
> - use pull requests for production changes
> 
> docs/import-runbook.md should document the intended import flow:
> raw source file -> import batch -> source_records -> validation -> canonical table -> audit trail
> 
> docs/deployment-flow.md should document:
> feature branch -> PR -> Supabase checks -> merge to main -> Supabase deploys production
> 
> Create SQL helper file sql/updated_at_trigger.sql:
> - define a reusable updated_at trigger function
> 
> Create SQL helper file sql/is_admin.sql:
> - define or document a placeholder public.is_admin() function.
> - If an existing version exists, do not overwrite it; just preserve or comment.
> 
> Create schemas/ files as declarative placeholders with useful comments.
> Do not duplicate all migrations into schemas yet.
> Just create clean starter files explaining intended ownership.
> 
> Create policies/ files as placeholders with comments explaining RLS intent.
> Do not create open public access policies.
> 
> Add one new migration only if import infrastructure tables do not already exist.
> Name it with current timestamp format:
> YYYYMMDDHHMMSS_create_import_infrastructure.sql
> 
> The migration should safely create:
> 
> public.import_batches:
> - id uuid primary key default gen_random_uuid()
> - source_name text not null
> - source_type text not null
> - source_path text
> - imported_by uuid
> - import_status text not null default 'pending'
> - record_count integer default 0
> - error_count integer default 0
> - notes text
> - created_at timestamptz not null default now()
> - updated_at timestamptz not null default now()
> 
> public.source_records:
> - id uuid primary key default gen_random_uuid()
> - import_batch_id uuid references public.import_batches(id) on delete cascade
> - source_record_id text
> - source_table text
> - source_payload jsonb not null
> - normalized_payload jsonb
> - target_table text
> - target_id uuid
> - processing_status text not null default 'pending'
> - error_message text
> - created_at timestamptz not null default now()
> - processed_at timestamptz
> 
> Also:
> - enable RLS on both tables
> - do not create broad permissive policies
> - create indexes for import_batch_id, processing_status, source_table, target_table
> - create updated_at trigger for import_batches if helper function exists in the same migration or project
> 
> Create import templates as CSV headers only. No real data.
> 
> After making changes:
> 1. Show the final tree under qisupabase.
> 2. Show git status.
> 3. List every file created or changed.
> 4. Warn me if any real-looking secret was detected.
> 5. Do not push unless I explicitly tell you to push.
> :::
> 
> One extra thing: **before you push**, check whether Supabase is watching this nested path:
> 
> ```text
> 20_QiSystem/50_data/supabase/qisupabase
> ```
> 
> If Supabase expects the deployable folder to be named exactly `supabase/` at repo root, this structure may not deploy automatically. If that happens, we either adjust the GitHub integration path or add a thin root-level `supabase/` deploy folder.
