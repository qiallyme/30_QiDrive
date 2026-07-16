---
layout: page
title: "QiAccess Start Directory"
slug: "qiaccess_start_directory"
created_at: "2026-06-18 13:00:45"
updated_at: "2026-06-18 13:00:45"
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
date: 2026-06-18
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a343243-afb0-83ea-8aeb-939e1214e28c"
canonical_ref: ""
---

# QiAccess Start Directory

## Overview
- **Date**: 2026-06-18 13:00:45
- **Conversation ID**: `6a343243-afb0-83ea-8aeb-939e1214e28c`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> i can find the full directory tree we are supposed to follow.

### Assistant
> We already have enough to anchor the structure. The danger is chasing old trees and rebuilding the wrong thing, so I’m going to separate **QiNexus/Drive**, **app repo**, and **repo docs** instead of blending them.

### Assistant
> Yes — the **active structure authority** we have is the **QiAccess Start Blueprint**, not the older business/client QiOS tree. The file says QiAccess Start is now the operational front door, and the old client/platform model is demoted. fileciteturn0file0 fileciteturn1file1
> 
> ## The directory model to follow
> 
> ### 1. QiLabs root — working system layer
> 
> Use this as the high-level root model:
> 
> ```text
> C:\QiLabs
> ├── 01_QiDNA
> ├── 10_QiAccess
> ├── 20_QiSystem
> ├── 30_QiServer
> ├── 40_QiCapture
> ├── 50_QiNexus
> ├── 60_QiApp_QiLife
> └── 70_QiConnect
> ```
> 
> That is the **local system/module layer**.
> 
> ---
> 
> ### 2. QiNexus / Google Drive — file storage backbone
> 
> Inside QiNexus / Drive, the canonical root order is:
> 
> ```text
> 00_inbox
> 01_workbench
> 02_timeline
> 03_life
> 04_people
> 05_business
> 06_finance
> 07_legal
> 08_tech
> 09_assets
> 10_data
> 11_reference
> 12_archive
> 13_system
> ```
> 
> The blueprint is clear: **do not casually add new root folders**. Active work goes in `01_workbench`, reusable files in `09_assets`, structured exports in `10_data`, and completed/frozen material in `12_archive`. fileciteturn1file0
> 
> ---
> 
> ### 3. QiAccess Start app repo — React/app structure
> 
> For the actual app, the doctrine is:
> 
> ```text
> src
> ├── app
> ├── layouts
> ├── pages
> ├── components
> │   └── ui
> ├── lib
> ├── styles
> └── features
>     ├── 00_dashboard
>     ├── 01_start
>     ├── 02_access
>     ├── 03_qiserver
>     ├── 04_knowledge_base
>     ├── 05_storage
>     ├── 06_roadmap
>     └── 07_blueprint
> ```
> 
> Standard React folders stay unnumbered. System feature modules get numbered. Each feature should have:
> 
> ```text
> components/
> data/
> README.md
> ```
> 
> The mental model is:
> 
> ```text
> Route → Page → Feature → Component → Data
> ```
> 
> That is the clean rule. Anything else is probably noise unless it has a job. fileciteturn1file2
> 
> ---
> 
> ### 4. Repo docs — source-of-truth docs
> 
> The active blueprint belongs here:
> 
> ```text
> docs
> ├── 00_blueprint
> │   └── QiAccess_Start_Blueprint.md
> ├── 01_roadmap
> │   └── QiRoadmap.md
> ├── 02_architecture
> │   ├── System_Map.md
> │   ├── App_Flow.md
> │   ├── Service_Map.md
> │   └── Runtime_Zones.md
> ├── 03_storage
> │   ├── Google_Drive_Buckets.md
> │   └── QiNexus_Model.md
> ├── 04_decisions
> │   ├── ADR-0001_QiAccess_Start_As_Operational_Front_Door.md
> │   ├── ADR-0002_Start_Access_Boundary.md
> │   ├── ADR-0003_WikiJS_As_Knowledge_Base.md
> │   ├── ADR-0004_Google_Drive_As_Storage_Backbone.md
> │   └── ADR-0005_QiNexus_As_Personal_PARA_Model.md
> ├── 05_operations
> │   ├── Qiserver_Runbook.md
> │   └── Access_And_Exposure_Rules.md
> └── 06_learning_notes
>     └── React_App_Flow.md
> ```
> 
> The blueprint says repo docs define **how the system is built**, while Wiki.js explains **how the system is used**. fileciteturn1file3
> 
> ---
> 
> ## To find it locally
> 
> Run this in PowerShell:
> 
> ```powershell
> Get-ChildItem C:\QiLabs -Recurse -File |
> Where-Object {
>   $_.Name -match "blueprint|target|tree|structure|folder|roadmap|architecture"
> } |
> Select-Object FullName
> ```
> 
> Also search specifically:
> 
> ```powershell
> Get-ChildItem C:\QiLabs -Recurse -File -Filter "QiAccess_Start_Blueprint.md" |
> Select-Object FullName
> ```
> 
> ## The no-BS answer
> 
> The “full directory tree” is probably split across multiple docs, but the **active doctrine** is this:
> 
> - **QiLabs root** = local system modules.
> - **QiNexus root order** = Drive/file organization.
> - **QiAccess Start app structure** = React app structure.
> - **Repo docs tree** = engineering truth.
> - **Wiki.js** = readable manual, not canonical architecture.
> 
> Do **not** follow the older client/tenant/business blueprint as the master anymore. It is ancestor material, not the current operating center.

### User
> {'asset_pointer': 'sediment://file_00000000587c720ca3c0cca187d72062', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 260, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 11020, 'width': 271}this is the top.

### Assistant
> Perfect. **This is the real top-level tree. Use this, not the older one.**
> 
> The current top is cleaner:
> 
> ```text
> C:\QiLabs
> ├── 00_QiLabs.workspace
> ├── 10_QiSpark
> ├── 20_QiServer
> ├── 30_QiMemory
> ├── 40_QiVault
> ├── 50_QiConnect
> └── 60_QiApps
> ```
> 
> ## What each root should mean
> 
> | Folder | Job |
> |---|---|
> | `00_QiLabs.workspace` | Workspace config, VS Code/Cursor workspace files, root indexes, repo map |
> | `10_QiSpark` | Planning, doctrine, blueprints, prompts, strategy, product thinking |
> | `20_QiServer` | Server infrastructure, Docker, Cloudflare, Tailscale, backups, deployment |
> | `30_QiMemory` | Knowledge base, Wiki.js exports, AI memory, vector/graph notes, semantic layer |
> | `40_QiVault` | File storage backbone, Google Drive mirror, QiNexus, documents, assets, data |
> | `50_QiConnect` | Integrations, APIs, sync jobs, connectors, automations |
> | `60_QiApps` | Actual apps: QiAccess Start, Mom’s Care, QiLife, dashboards, tools |
> 
> ## The important correction
> 
> Earlier structure like this:
> 
> ```text
> 01_QiDNA
> 10_QiAccess
> 20_QiSystem
> 30_QiServer
> 40_QiCapture
> 50_QiNexus
> 60_QiApp_QiLife
> 70_QiConnect
> ```
> 
> is now **legacy / ancestor naming**.
> 
> Your current tree has absorbed those jobs into cleaner modules:
> 
> | Old idea | Current folder |
> |---|---|
> | QiDNA / doctrine | `10_QiSpark` |
> | QiAccess Start | `60_QiApps` app, with doctrine in `10_QiSpark` |
> | QiServer | `20_QiServer` |
> | QiMemory / knowledge | `30_QiMemory` |
> | QiNexus / Drive / storage | `40_QiVault` |
> | QiConnect / integrations | `50_QiConnect` |
> | QiLife / Mom’s Care / tools | `60_QiApps` |
> 
> ## Where QiAccess Start should live
> 
> The **app code** should live here:
> 
> ```text
> C:\QiLabs\60_QiApps\QiAccess_Start
> ```
> 
> The **doctrine/docs** for it can live here:
> 
> ```text
> C:\QiLabs\10_QiSpark\docs\QiAccess_Start
> ```
> 
> The blueprint says QiAccess Start is the operational front door and should centralize access, services, Wiki.js links, storage links, care, legal, finance, and system tools. fileciteturn0file0
> 
> ## What I would do next
> 
> Do **not** rename this top-level tree again. That’s how we get folder whiplash.
> 
> Instead, create one master file:
> 
> ```text
> C:\QiLabs\00_QiLabs.workspace\QiLabs_Master_Tree.md
> ```
> 
> And put this in it:
> 
> ```markdown
> # QiLabs Master Tree
> 
> ## Canonical Top Level
> 
> - 00_QiLabs.workspace
> - 10_QiSpark
> - 20_QiServer
> - 30_QiMemory
> - 40_QiVault
> - 50_QiConnect
> - 60_QiApps
> 
> ## Rule
> 
> This is the active top-level structure. Older names such as QiDNA, QiAccess, QiSystem, QiCapture, QiNexus, and QiApp_QiLife are ancestor concepts unless explicitly mapped into the current folders.
> 
> ## Folder Jobs
> 
> ### 00_QiLabs.workspace
> Workspace config, root indexes, maps, manifests, and repo-level navigation.
> 
> ### 10_QiSpark
> Doctrine, strategy, blueprints, prompts, planning, product concepts, and architecture thinking.
> 
> ### 20_QiServer
> Server infrastructure, deployment, Docker, Cloudflare, Tailscale, backups, service configs, and runbooks.
> 
> ### 30_QiMemory
> Knowledge base, semantic memory, Wiki.js content, vector/graph design, ontology, embeddings, and AI-readable reference layers.
> 
> ### 40_QiVault
> Storage backbone, Google Drive mirror, QiNexus, documents, files, data exports, assets, archives, and evidence packets.
> 
> ### 50_QiConnect
> Integrations, connectors, sync jobs, APIs, automations, webhooks, and cross-system bridges.
> 
> ### 60_QiApps
> Actual user-facing and internal apps, including QiAccess Start, Mom’s Care, QiLife, dashboards, and tools.
> ```
> 
> Clean. Stable. Actually usable.

### User
> do this in canvas and lets start with waht should be in the root of qilabs.

### Assistant
> Done — I made the starter Obsidian canvas for the **QiLabs root**:
> 
> [Download QiLabs_Root_Canvas.canvas](sandbox:/mnt/data/QiLabs_Root_Canvas.canvas)
> 
> ## QiLabs root should stay this clean
> 
> ```text
> C:\QiLabs
> ├── 00_QiLabs.workspace
> ├── 10_QiSpark
> ├── 20_QiServer
> ├── 30_QiMemory
> ├── 40_QiVault
> ├── 50_QiConnect
> └── 60_QiApps
> ```
> 
> ## What belongs directly in `C:\QiLabs`
> 
> Only root-level control files:
> 
> ```text
> C:\QiLabs
> ├── 00_QiLabs.workspace
> ├── 10_QiSpark
> ├── 20_QiServer
> ├── 30_QiMemory
> ├── 40_QiVault
> ├── 50_QiConnect
> ├── 60_QiApps
> ├── README.md
> ├── QiLabs.code-workspace
> ├── STRUCTURE.md
> ├── SYSTEM_MAP.md
> ├── CHANGELOG.md
> ├── .gitignore
> └── .editorconfig
> ```
> 
> ## What does **not** belong in root
> 
> No loose chaos:
> 
> ```text
> random_exports/
> screenshots/
> old_qidna/
> old_qisystem/
> test_app/
> mom_care_notes.md
> drive_dump/
> untitled folder/
> ```
> 
> Root is not a junk drawer. Root is the map.
> 
> ## Root folder job map
> 
> | Folder | Job |
> |---|---|
> | `00_QiLabs.workspace` | Workspace config, master indexes, repo maps, navigation manifests |
> | `10_QiSpark` | Blueprints, doctrine, prompts, strategy, planning, ADRs |
> | `20_QiServer` | qiserver runtime, Docker, Cloudflare, Tailscale, backups, deployment |
> | `30_QiMemory` | Wiki.js, semantic memory, vector/graph layer, ontology, retrieval design |
> | `40_QiVault` | Google Drive mirror, QiNexus, documents, evidence, assets, data, archives |
> | `50_QiConnect` | APIs, integrations, sync jobs, automations, connectors |
> | `60_QiApps` | QiAccess Start, Mom’s Care, QiLife, dashboards, actual apps |
> 
> The blueprint backs the same basic doctrine: QiAccess Start is the operational front door, Google Drive/QiNexus is the storage backbone, repo docs are engineering truth, and Wiki.js is the readable manual layer. fileciteturn0file0

### User
> i want this in markdown mind map.

### Assistant
> Done.
> 
> [Download QiLabs_Root_Mindmap.md](sandbox:/mnt/data/QiLabs_Root_Mindmap.md)
> 
> This is **Markmap-friendly Markdown** and should also work cleanly in Obsidian as a collapsible outline/mind map source.

### User
> can you try and give me the full tree of qilabs please.

### Assistant
> Yes. Here’s the **full target tree** I’d standardize as the working QiLabs structure.
> 
> I also made it downloadable:
> 
> [Download QiLabs_Full_Target_Tree.md](sandbox:/mnt/data/QiLabs_Full_Target_Tree.md)
> 
> This is a **target/canonical tree**, not a live scan of your disk. I can only see the screenshot you showed, so I’m building from your real top-level folders plus the active QiAccess doctrine. The blueprint says the system center is now Cody’s actual life, family/care/legal/finance/knowledge/tech, with QiAccess Start as the front door, qiserver as runtime, Wiki.js as readable knowledge base, and Google Drive/QiNexus as storage backbone. fileciteturn3file0
> 
> ```text
> C:\QiLabs
> ├── README.md
> ├── QiLabs.code-workspace
> ├── STRUCTURE.md
> ├── SYSTEM_MAP.md
> ├── CHANGELOG.md
> ├── .gitignore
> ├── .editorconfig
> │
> ├── 00_QiLabs.workspace
> │   ├── README.md
> │   ├── 00_indexes
> │   ├── 10_maps
> │   ├── 20_manifests
> │   ├── 30_workspace_files
> │   ├── 40_environment
> │   ├── 50_scripts
> │   └── 90_archive
> │
> ├── 10_QiSpark
> │   ├── README.md
> │   ├── 00_inbox
> │   ├── 10_blueprints
> │   ├── 20_roadmaps
> │   ├── 30_architecture
> │   ├── 40_decisions
> │   ├── 50_prompts
> │   ├── 60_strategy
> │   ├── 70_learning_notes
> │   └── 90_archive
> │
> ├── 20_QiServer
> │   ├── README.md
> │   ├── 00_inventory
> │   ├── 10_infrastructure
> │   ├── 20_docker
> │   ├── 30_cloudflare
> │   ├── 40_tailscale
> │   ├── 50_services
> │   ├── 60_backups
> │   ├── 70_monitoring
> │   ├── 80_runbooks
> │   └── 90_archive
> │
> ├── 30_QiMemory
> │   ├── README.md
> │   ├── 00_index
> │   ├── 10_wikijs
> │   ├── 20_ontology
> │   ├── 30_vector
> │   ├── 40_graph
> │   ├── 50_ai_memory
> │   ├── 60_semantic_profiles
> │   ├── 70_retrieval
> │   ├── 80_exports
> │   └── 90_archive
> │
> ├── 40_QiVault
> │   ├── README.md
> │   ├── 00_vault_admin
> │   ├── My Drive
> │   │   ├── 00_inbox
> │   │   ├── 01_workbench
> │   │   ├── 02_timeline
> │   │   ├── 03_life
> │   │   ├── 04_people
> │   │   ├── 05_business
> │   │   ├── 06_finance
> │   │   ├── 07_legal
> │   │   ├── 08_tech
> │   │   ├── 09_assets
> │   │   ├── 10_data
> │   │   ├── 11_reference
> │   │   ├── 12_archive
> │   │   └── 13_system
> │   └── 90_archive
> │
> ├── 50_QiConnect
> │   ├── README.md
> │   ├── 00_index
> │   ├── 10_connectors
> │   ├── 20_apis
> │   ├── 30_sync_jobs
> │   ├── 40_automations
> │   ├── 50_webhooks
> │   ├── 60_import_export
> │   ├── 70_provider_configs
> │   ├── 80_logs
> │   └── 90_archive
> │
> └── 60_QiApps
>     ├── README.md
>     ├── 00_app_index
>     ├── 10_QiAccess_Start
>     ├── 20_QiLife
>     ├── 30_Moms_Care
>     ├── 40_Family_OS
>     ├── 50_Internal_Tools
>     ├── 60_Dashboards
>     └── 90_archive
> ```
> 
> ## The important app subtree
> 
> Inside `60_QiApps\10_QiAccess_Start`, use this:
> 
> ```text
> 10_QiAccess_Start
> ├── README.md
> ├── package.json
> ├── vite.config.ts
> ├── tsconfig.json
> ├── index.html
> ├── public
> ├── docs
> │   ├── 00_blueprint
> │   ├── 01_roadmap
> │   ├── 02_architecture
> │   ├── 03_storage
> │   ├── 04_decisions
> │   ├── 05_operations
> │   └── 06_learning_notes
> └── src
>     ├── app
>     ├── layouts
>     ├── pages
>     ├── components
>     │   └── ui
>     ├── lib
>     ├── styles
>     └── features
>         ├── 00_dashboard
>         ├── 01_start
>         ├── 02_access
>         ├── 03_qiserver
>         ├── 04_knowledge_base
>         ├── 05_storage
>         ├── 06_roadmap
>         └── 07_blueprint
> ```
> 
> Each feature folder should have:
> 
> ```text
> components
> data
> README.md
> ```
> 
> ## The placement rule
> 
> Use this when something new appears:
> 
> | Thing | Home |
> |---|---|
> | doctrine, prompts, blueprints, strategy | `10_QiSpark` |
> | server, Docker, Cloudflare, Tailscale, backups | `20_QiServer` |
> | Wiki.js, semantic memory, graph/vector stuff | `30_QiMemory` |
> | files, docs, evidence, Drive mirror, data exports | `40_QiVault` |
> | APIs, connectors, sync jobs, automations | `50_QiConnect` |
> | apps, dashboards, tools, front doors | `60_QiApps` |
> | root maps, manifests, workspace config | `00_QiLabs.workspace` |
> 
> No more folder whiplash. This tree is sane.

### User
> ok there shoudl be no files in teh root of qilabs, all configs and files should be inside the qilabs workspace folder, update that also qiaccess is inside of qispartk now as a simple html landing page.

### Assistant
> Correct. That’s cleaner.
> 
> I updated the structure with two major corrections:
> 
> 1. **No files directly inside `C:\QiLabs`**
> 2. **QiAccess lives inside `10_QiSpark` as a simple HTML landing page**, not inside `60_QiApps`
> 
> Downloads:
> 
> [QiLabs_Full_Target_Tree_v2.md](sandbox:/mnt/data/QiLabs_Full_Target_Tree_v2.md)
> 
> [QiLabs_Root_Mindmap_v2.md](sandbox:/mnt/data/QiLabs_Root_Mindmap_v2.md)
> 
> ## Updated root
> 
> ```text
> C:\QiLabs
> ├── 00_QiLabs.workspace
> ├── 10_QiSpark
> ├── 20_QiServer
> ├── 30_QiMemory
> ├── 40_QiVault
> ├── 50_QiConnect
> └── 60_QiApps
> ```
> 
> ## Root-level files now move here
> 
> ```text
> C:\QiLabs\00_QiLabs.workspace
> ├── README.md
> ├── 00_indexes
> ├── 10_maps
> ├── 20_manifests
> ├── 30_configs
> ├── 40_environment
> ├── 50_scripts
> ├── 60_logs
> ├── 70_templates
> └── 90_archive
> ```
> 
> So things like this:
> 
> ```text
> README.md
> QiLabs.code-workspace
> STRUCTURE.md
> SYSTEM_MAP.md
> CHANGELOG.md
> .gitignore
> .editorconfig
> ```
> 
> now live under `00_QiLabs.workspace`, mostly in:
> 
> ```text
> 00_QiLabs.workspace\30_configs
> 00_QiLabs.workspace\10_maps
> 00_QiLabs.workspace\00_indexes
> ```
> 
> ## QiAccess now lives here
> 
> ```text
> C:\QiLabs\10_QiSpark\10_QiAccess
> ├── README.md
> ├── index.html
> ├── assets
> ├── css
> ├── js
> ├── data
> └── docs
> ```
> 
> That’s the right move **as long as QiAccess is just a simple HTML landing page**. If it becomes a full React/Vite app later, then it graduates to `60_QiApps`. Until then, keeping it in QiSpark is cleaner.

### User
> ok, but you need the tree to be part of the mind map with all sub folders and everything that should be in there.

### Assistant
> Yes — that was the missing part.
> 
> I made a **full Markmap-style mind map** where the **entire tree is part of the mind map**, including the root folders, subfolders, and the key files that should live inside them.
> 
> Download it here:
> 
> [QiLabs_Full_Tree_Mindmap_v3.md](sandbox:/mnt/data/QiLabs_Full_Tree_Mindmap_v3.md)
> 
> What’s in it:
> - `C:\QiLabs` root
> - every root module
> - major subfolders
> - expected files
> - QiAccess correctly placed under `10_QiSpark`
> - `00_QiLabs.workspace` holding all root configs/files
> - full `My Drive` / QiNexus bucket tree
> - app structure under `60_QiApps`
> 
> If you want, next I can do either:
> 
> 1. a **more expanded version** with even deeper subfolders for each module, or  
> 2. a **cleaned “final canonical” version** with only the folders you are 95% sure you want to keep.
