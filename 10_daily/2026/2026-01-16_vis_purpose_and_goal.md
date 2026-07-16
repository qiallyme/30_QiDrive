---
layout: page
title: "VIS Purpose and Goal"
slug: "vis_purpose_and_goal"
created_at: "2026-01-16 08:24:23"
updated_at: "2026-07-16T06:49:29-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-003.json"
template_key: master-template
date: 2026-01-16
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "696a49fb-06ac-8329-bba8-1bdc62a0197b"
canonical_ref: ""
---

# VIS Purpose and Goal

## Overview
- **Date**: 2026-01-16 08:24:23
- **Conversation ID**: `696a49fb-06ac-8329-bba8-1bdc62a0197b`
- **Source**: `Chat-Export-28513-2026/conversations-003.json`

## Chat History

### User
> Describe the purpose and goal for the VIS and create a prompt from gemeni to create a app or script and or api to run the vis from the binder directory and do what its designed to do.

### Assistant
> ## VIS purpose + goal (what it is and why it exists)
> 
> **VIS = Violation Intelligence System** (your “case engine,” not a narrative doc).
> 
> Its job is to take your **binder directory** (the structured case folder tree) and automatically produce **court/attorney-ready outputs** that are:
> 
> 1. **Searchable and navigable**
>    - Auto-generate a clean **Table of Contents**, **index pages**, and **cross-links** between filings, exhibits, docket events, and timelines (think: “click from Motion → Exhibit → underlying docket line → proof of service defect”).
> 
> 2. **Evidence-integrity preserving**
>    - Create a **manifest** of every artifact: filename, path, size, timestamps, SHA-256 hash, and classification (filing, exhibit, correspondence, audio/video, screenshot, etc.).
>    - This protects you against “you fabricated it later” attacks and makes disclosure sane.
> 
> 3. **Argument-aware**
>    - Build a **claims map** (your procedural/rights failures) and tie each claim to the specific evidence objects that support it.
>    - Example: “Defective service under TR 4.1(B)” links to returns, summons, filings, affidavits, and any contradictions. Your existing motion language explicitly centers that requirement and the mailing defect. fileciteturn0file12
> 
> 4. **Output-driven**
>    - Generate the things you actually need:
>      - **Attorney packet** (single PDF + exhibit list + citations)
>      - **Court binder print pack** (covers, tabs, TOC, exhibit separators)
>      - **Web view / local site** (static HTML indexes like the one you already have) fileciteturn0file14
>      - **One-page executive summary** (family/press/legislator version)
>      - **Chronology** and “what happened when” visuals
> 
> **Bottom line:** VIS turns “a folder full of stuff” into a **structured case product**: defensible, repeatable, fast to update, and hard to ignore.
> 
> ---
> 
> ## What VIS should do when you “run it” on the binder directory
> 
> **Inputs**
> - Root folder: `Case_Binder/` (whatever your binder root is)
> - Optional config: `vis.yaml` (rules, naming, tags, output formats)
> 
> **Core pipeline**
> 1. **Scan + classify files**
>    - Identify filings vs exhibits vs correspondence vs court records vs media
>    - Extract dates from filenames and/or metadata
> 
> 2. **Integrity**
>    - SHA-256 every file
>    - Write `output/manifest.json` + `output/manifest.csv`
> 
> 3. **Metadata extraction**
>    - PDFs: title/author/page count (and optionally text extraction)
>    - Images: dimensions
>    - Video/audio: duration (optional)
> 
> 4. **Linking layer**
>    - Auto-link:
>      - Motions ↔ proposed orders ↔ exhibits ↔ declarations
>      - Exhibit list ↔ exhibit PDFs
>      - Docket items ↔ files (when matching exists)
> 
> 5. **Generate outputs**
>    - `output/VIS_Report.md` (or `.pdf`) containing:
>      - Executive snapshot
>      - Key procedural defects map
>      - Timeline
>      - Evidence map (claim → evidence IDs)
>      - “What’s missing / what to request”
>    - `output/site/` static HTML (folder indexes + global search index)
>    - `output/print_pack/` binder-ready PDFs (optional)
> 
> ---
> 
> ## Gemini prompt to build the VIS app/script/API (copy/paste)
> 
> ```text
> You are an expert software engineer building a “Violation Intelligence System (VIS)” for a legal case binder.
> 
> GOAL
> Create a Python-based tool that ingests a binder directory (a structured folder tree of filings, exhibits, and evidence) and generates:
> 1) an evidence integrity manifest (hashes + metadata),
> 2) navigable indexes (static HTML + markdown),
> 3) a VIS report that maps legal/procedural claims to supporting evidence,
> 4) optional API endpoints to run and query the VIS results.
> 
> CONSTRAINTS
> - Must run locally, offline.
> - Cross-platform: Windows + macOS + Linux.
> - Must not require paid services.
> - Must be deterministic and reproducible (same input => same outputs).
> - Must preserve evidence integrity (read-only source; write outputs to /output).
> - Provide clear CLI usage and a minimal config file.
> - Assume binder contains PDFs, images, text/markdown, and arbitrary files.
> 
> INPUTS
> - binder_root: path to the binder directory.
> - optional config file: vis.yaml
> 
> OUTPUTS (write under binder_root/output/)
> - manifest.json and manifest.csv including: file_id, relative_path, sha256, size_bytes, created_time, modified_time, file_type, inferred_date, tags
> - index.md (global) and per-folder index.html pages (static HTML with breadcrumbs)
> - search_index.json (for client-side search in the HTML site)
> - VIS_Report.md containing:
>   - Executive summary
>   - Chronology (sorted by inferred_date when possible)
>   - Claims map (claim -> evidence references)
>   - “Key contradictions / gaps” section
>   - “Next actions” section
> 
> FILE IDENTIFIERS
> - Generate stable evidence IDs like: EVD-YYYY-XXXX (incrementing) OR hash-based short IDs.
> - IDs must be stable across re-runs if file content is unchanged.
> 
> CLASSIFICATION RULES
> - Infer type by path keywords and filename patterns:
>   - filings: folders containing “filings”, “motions”, “orders”
>   - exhibits: folders containing “exhibits”
>   - declarations/affidavits: filenames containing “declaration” or “affidavit”
>   - docket/court record: “docket”, “chronological case summary”, “odyssey”, “receipt”
> - Extract dates from filenames using patterns: YYYY-MM-DD, YYYYMMDD, MM-DD-YYYY, etc.
> - If no date in name, use file modified time but mark it as inferred.
> 
> STATIC HTML
> - Generate simple, fast HTML indexes per folder with:
>   - breadcrumbs
>   - parent link
>   - subfolders list
>   - files list with sizes
>   - link to open/download the file
>   - dark theme and mobile-friendly layout
> 
> CLAIMS MAP
> - Implement a simple rules-based claims map via vis.yaml:
>   - Each claim has keywords and file path patterns.
>   - The report lists each claim and matching evidence files (with IDs + links).
> - Provide a default vis.yaml template.
> 
> CLI
> - Provide a CLI entrypoint:
>   - vis run --binder <path> [--config vis.yaml]
>   - vis serve --binder <path> (optional: serve output/site locally)
>   - vis query --binder <path> --claim "Service defects" (search results)
> 
> OPTIONAL API
> - Provide a FastAPI app (optional, but include) with:
>   - POST /run (kick off a run)
>   - GET /manifest
>   - GET /claims
>   - GET /claim/{claim_id}
>   - GET /file/{file_id}/meta
> - Keep it simple and synchronous unless it’s trivial to add async.
> 
> DELIVERABLES
> Return:
> 1) A complete project structure (folders/files).
> 2) The full Python source code for:
>    - scanner + hasher
>    - metadata extractors
>    - html index generator
>    - markdown report generator
>    - CLI (typer or argparse)
>    - optional FastAPI server
> 3) A sample vis.yaml
> 4) Exact run instructions
> 
> IMPORTANT
> Do not hand-wave. Provide working code with error handling and comments.
> ```
> 
> ---
> 
> If you want this to be even sharper, the fastest multiplier is adding **one “claims taxonomy” file** (even a rough `vis.yaml`) that lists your core buckets (service/jurisdiction, ADA notice/accommodation failures, writ execution/property access, payment portal errors, damages). VIS becomes dramatically more useful when it knows what it’s trying to prove.

### User
> also doesnt our vis shoudl be part of the legalmind, here is what we worked on for the legal midn. ```markdown

> . 📂 Legalmind

> ├── 📄 CONTRIBUTING.md

> ├── 📄 LICENSE

> ├── 📄 PROJECT-OVERVIEW.md

> ├── 📄 README.md

> └── 📂 backend/

> │  └── 📂 agent-orchestrator/

> │    ├── 📄 Dockerfile

> │    ├── 📄 main.py

> │    ├── 📄 requirements.txt

> │    └── 📂 services/

> │      ├── 📄 __init__.py

> │      ├── 📄 debate_manager.py

> │      ├── 📄 dynamic_agent.py

> │      ├── 📄 fixed_agent.py

> │      ├── 📄 legal_reference_engine.py

> │      ├── 📄 retry_handler.py

> │      ├── 📄 websocket_manager.py

> │  └── 📂 api-gateway/

> │    ├── 📄 Dockerfile

> │    ├── 📄 main.py

> │    ├── 📄 requirements.txt

> │  └── 📂 parser-service/

> │    ├── 📄 Dockerfile

> │    ├── 📄 main.py

> │    ├── 📄 requirements.txt

> │    └── 📂 services/

> │      ├── 📄 __init__.py

> │      ├── 📄 document_processor.py

> │      ├── 📄 entity_extractor.py

> │      ├── 📄 firestore_client.py

> │      ├── 📄 pii_redactor.py

> │      ├── 📄 pubsub_client.py

> │      ├── 📄 storage_client.py

> │  └── 📂 report-generator/

> │    ├── 📄 Dockerfile

> │    ├── 📄 main.py

> │    ├── 📄 requirements.txt

> │    ├── 📄 subscriber.py

> │  └── 📂 role-assignment/

> │    ├── 📄 Dockerfile

> │    ├── 📄 main.py

> │    ├── 📄 requirements.txt

> │    └── 📂 services/

> │      ├── 📄 __init__.py

> │      ├── 📄 agent_pool_manager.py

> │      ├── 📄 firestore_client.py

> │      ├── 📄 pubsub_client.py

> │      ├── 📄 role_analyzer.py

> │  └── 📂 video-generator/

> │    ├── 📄 Dockerfile

> │    ├── 📄 main.py

> │    ├── 📄 main_ai_video.py

> │    ├── 📄 main_veo3.py

> │    ├── 📄 requirements.txt

> │    ├── 📄 subscriber.py

> ├── 📄 deploy-to-github.sh

> └── 📂 docs/

> │  ├── 📄 DEPLOYMENT.md

> │  └── 📂 backend-docs/

> │    ├── 📄 01-parser-service-COMPLETE.md

> │    ├── 📄 02-api-gateway-COMPLETE.md

> │    ├── 📄 03-agent-orchestrator-COMPLETE.md

> │    ├── 📄 04-role-assignment-COMPLETE.md

> │    ├── 📄 05-video-generator-COMPLETE.md

> │    ├── 📄 06-report-generator-COMPLETE.md

> │    ├── 📄 AGENT_ORCHESTRATOR_SUMMARY.md

> │    ├── 📄 COMPLETE_SYSTEM_GUIDE.md

> │    ├── 📄 DOCUMENTATION_SUMMARY.md

> │    ├── 📄 README.md

> │    ├── 📄 ROLE_ASSIGNMENT_SUMMARY.md

> │  └── 📂 diagrams/

> │    ├── 📄 README.md

> │    ├── 📄 SYSTEM-ARCHITECTURE.md

> │    ├── 📄 SYSTEM-WORKFLOW.md

> │  └── 📂 frontend-docs/

> │    ├── 📄 01-FRONTEND-ARCHITECTURE-COMPLETE.md

> │    ├── 📄 02-PAGES-AND-COMPONENTS.md

> │    ├── 📄 03-API-AND-WEBSOCKET.md

> │    ├── 📄 ALIGNMENT-VERIFICATION.md

> │    ├── 📄 COMPLETE-FRONTEND-GUIDE.md

> │    ├── 📄 DOCUMENTATION-COMPLETE.md

> │    ├── 📄 FRONTEND-DOCUMENTATION-SUMMARY.md

> │    ├── 📄 README.md

> └── 📂 frontend/

> │  ├── 📄 Dockerfile

> │  ├── 📄 README.md

> │  ├── 📄 next.config.js

> │  ├── 📄 package.json

> │  ├── 📄 postcss.config.js

> │  └── 📂 public/

> │    ├── 📄 README.md

> │  └── 📂 src/

> │    └── 📂 app/

> │      └── 📂 chat/

> │        └── 📂 [sessionId]/

> │          ├── 📄 page.tsx

> │      ├── 📄 globals.css

> │      ├── 📄 layout.tsx

> │      ├── 📄 page.tsx

> │      └── 📂 results/

> │        └── 📂 [sessionId]/

> │          ├── 📄 page.tsx

> │      └── 📂 upload/

> │        ├── 📄 page.tsx

> │    └── 📂 components/

> │      ├── 📄 MessageBubble.tsx

> │      ├── 📄 StageProgress.tsx

> │    └── 📂 lib/

> │      ├── 📄 api.ts

> │      ├── 📄 utils.ts

> │      ├── 📄 websocket-native.ts

> │    └── 📂 types/

> │      ├── 📄 index.ts

> │  ├── 📄 tailwind.config.ts

> │  ├── 📄 tsconfig.json

> └── 📂 infrastructure/

> │  └── 📂 bigquery/

> │    ├── 📄 add_criminal_offences.py

> │    ├── 📄 add_marriage_laws.py

> │    ├── 📄 add_marriage_relationship_laws.py

> │    ├── 📄 add_more_ipc_sections.py

> │    ├── 📄 add_murder_related_laws.py

> │    ├── 📄 add_property_offences.py

> │    ├── 📄 add_relationship_laws.py

> │    ├── 📄 add_serious_crimes.py

> │    ├── 📄 add_traffic_laws.py

> │    ├── 📄 add_us_laws.py

> │    ├── 📄 comprehensive_laws.sql

> │    ├── 📄 populate_comprehensive_laws.py

> │    ├── 📄 populate_data.py

> │    ├── 📄 sample_data.sql

> │    ├── 📄 schema.sql

> │    ├── 📄 verify_all_laws.sh

> │    ├── 📄 verify_database.py

> │  └── 📂 cloud-run/

> │    ├── 📄 deploy.sh

> │    ├── 📄 service-template.yaml

> │  ├── 📄 deploy_all.sh

> │  └── 📂 firestore/

> │    ├── 📄 firestore.rules

> │    └── 📄 schema.md

> ```

### Assistant
> Yes. If VIS lives outside Legalmind, you’ll rebuild the same plumbing twice (ingestion, metadata, indexing, report assembly). VIS should be a **first-class subsystem inside Legalmind**.
> 
> ### The clean way to think about it
> - **Legalmind = orchestration + multi-agent reasoning + UI + storage + report generator**
> - **VIS = evidence ingestion + integrity + indexing + claim-to-evidence mapping (the “case substrate”)**
> 
> Legalmind can *reason* without VIS, but it will be hallucination-prone and slow. VIS gives it a deterministic, hashed, queryable ground truth.
> 
> ---
> 
> ## Where VIS fits in your existing architecture
> 
> ### VIS as a backend service (recommended)
> Add a new service alongside `parser-service` and `report-generator`:
> 
> ```
> backend/
>   vis-service/
>     Dockerfile
>     main.py                 # FastAPI
>     requirements.txt
>     services/
>       scanner.py            # walk binder, classify, infer dates
>       hasher.py             # sha256, stable IDs
>       metadata.py           # pdf/image/media meta
>       indexer.py            # HTML + search index
>       claims_mapper.py      # rules-based mapping (vis.yaml)
>       exporters.py          # manifest.csv/json, report.md
>       storage_adapter.py    # firestore/gcs/local
> ```
> 
> **Why here:** it is “evidence-plane,” not “agent-plane.” Parser-service can still do text extraction; VIS consumes parsed artifacts + raw files and produces navigability + integrity + structured case objects.
> 
> ---
> 
> ## How VIS integrates with existing Legalmind services
> 
> ### 1) `parser-service` → VIS
> - Parser-service extracts text/entities/PII-redacted variants.
> - VIS links “raw evidence object” ↔ “parsed representation.”
> - VIS stores:
>   - `evidence_objects` (hash, path, type, date, tags)
>   - `derived_objects` (text extract, embeddings later, redactions)
>   - `relationships` (motion ↔ exhibit ↔ docket line)
> 
> ### 2) VIS → `agent-orchestrator`
> Agents should never “browse the folder.” They should query VIS:
> - “Give me all evidence for claim: Service defects”
> - “List exhibits referenced by Motion to Vacate”
> - “Show contradictions: sheriff return vs mailing proof”
> 
> ### 3) VIS → `report-generator`
> Report generator pulls structured data:
> - manifest summaries
> - claims maps
> - citations with file IDs + stable links
> - chronology + gap analysis
> 
> ### 4) `api-gateway` exposes VIS endpoints
> The frontend calls gateway; gateway routes to VIS.
> 
> ---
> 
> ## Minimal API contract for VIS (so it snaps in fast)
> 
> **Run**
> - `POST /vis/run`
>   - body: `{ "binder_root": "...", "config_path": "..." }`
>   - returns: `{ "run_id": "...", "status": "complete", "output_root": "..." }`
> 
> **Query**
> - `GET /vis/manifest?run_id=...`
> - `GET /vis/claims?run_id=...`
> - `GET /vis/claim/{claim_id}?run_id=...`
> - `GET /vis/evidence/{evidence_id}?run_id=...`
> - `GET /vis/search?q=...&run_id=...`
> 
> **Outputs**
> - `GET /vis/site/{run_id}/...` (static HTML served)
> - `GET /vis/export/{run_id}/manifest.csv`
> - `GET /vis/export/{run_id}/VIS_Report.md`
> 
> ---
> 
> ## Data model (what VIS should write so Legalmind can reason safely)
> 
> At minimum:
> 
> ### `EvidenceObject`
> - `evidence_id` (stable)
> - `sha256`
> - `relative_path`
> - `type` (filing/exhibit/correspondence/docket/media/etc.)
> - `inferred_date` + `date_confidence`
> - `size_bytes`
> - `created_time`, `modified_time`
> - `tags`
> - `relationships` (list of edges)
> 
> ### `Claim`
> - `claim_id`
> - `label`
> - `keywords`
> - `path_rules`
> - `matched_evidence_ids[]`
> 
> ### `Run`
> - `run_id`
> - `binder_root`
> - `started_at`, `finished_at`
> - `outputs` (paths)
> 
> Store this in Firestore if you want parity with your other services, but keep a local JSON export always (portability).
> 
> ---
> 
> ## Gemini prompt: “Add VIS into Legalmind as a real service”
> Copy/paste this into Gemini.
> 
> ```text
> You are a senior platform engineer. I have an existing monorepo called “Legalmind” with multiple backend services (parser-service, api-gateway, agent-orchestrator, report-generator, role-assignment, video-generator) and a Next.js frontend.
> 
> TASK
> Design and implement a new backend microservice called “vis-service” (Violation Intelligence System) inside backend/ that:
> 1) Ingests a local binder directory tree (PDFs/images/text/any files),
> 2) Generates an evidence integrity manifest (sha256, metadata, stable evidence IDs),
> 3) Generates navigable indexes (static HTML per folder + search_index.json),
> 4) Produces a claims-to-evidence mapping via a rules-based config (vis.yaml),
> 5) Exposes a FastAPI API so other Legalmind services can run VIS and query results.
> 
> REPO CONTEXT
> Current structure includes:
> backend/agent-orchestrator (FastAPI/python)
> backend/parser-service (FastAPI/python)
> backend/api-gateway (FastAPI/python)
> backend/report-generator (python)
> frontend (Next.js)
> infrastructure (firestore, cloud-run, bigquery scripts)
> 
> REQUIREMENTS
> - Implement backend/vis-service with:
>   - Dockerfile
>   - main.py (FastAPI)
>   - requirements.txt
>   - services/ modules: scanner.py, hasher.py, metadata.py, indexer.py, claims_mapper.py, exporters.py, storage_adapter.py
> - Local-first: must run offline and write outputs under <binder_root>/output/vis/<run_id>/
> - Deterministic: stable evidence IDs must not change across reruns if file contents unchanged.
> - Read-only binder: never modify source files.
> - Provide a default vis.yaml template.
> - Provide CLI entry (optional) but API is required.
> 
> API CONTRACT
> - POST /vis/run  body: {binder_root: string, config_path?: string}
> - GET /vis/runs/{run_id}
> - GET /vis/manifest?run_id=...
> - GET /vis/claims?run_id=...
> - GET /vis/claim/{claim_id}?run_id=...
> - GET /vis/evidence/{evidence_id}?run_id=...
> - GET /vis/search?q=...&run_id=...
> Also provide an endpoint to serve static HTML indexes under /vis/site/{run_id}/...
> 
> INTEGRATION
> - Update api-gateway to route /vis/* to vis-service (describe how; code if feasible).
> - Provide a short note for agent-orchestrator on how to query VIS rather than scanning files directly.
> - Keep code consistent with the existing Legalmind style (FastAPI patterns, services directory, etc.).
> 
> DELIVERABLES
> Return:
> 1) The exact folder/files to add.
> 2) Full code for vis-service.
> 3) Sample vis.yaml.
> 4) Notes on Docker compose / local run commands.
> 5) Example: a “Service Defects” claim rule set mapping to common filename/path patterns.
> 
> Do not hand-wave; give runnable code with error handling.
> ```
> 
> ---
> 
> ## Hard truth / design warning (so you don’t waste time)
> If you try to make VIS “an agent” inside `agent-orchestrator`, you’ll end up with:
> - nondeterministic runs,
> - poor reproducibility,
> - and fragile outputs.
> 
> VIS needs to be **a deterministic evidence pipeline**, not a debate bot. Put it in backend as its own service, then let agents consume the structured outputs.
> 
> ---
> 
> If you want, I can also draft the **`vis.yaml` starter taxonomy** tailored to your FCFCU case (service/jurisdiction defects, ADA notice failures, writ execution/property access, payment portal misapplication, damages). That’s the single file that turns VIS from “index generator” into “legal weapon.”

### User
> {'asset_pointer': 'sediment://file_000000007c887230980894048577de91', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 926, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 60036, 'width': 375}well where do i put everything,

### Assistant
> You have two different “worlds” in that tree, and you need to stop mixing them:
> 
> - **CASE_FCFCU** = the case data + binder content + outputs (the thing you ship to court/attorney)
> - **Legalmind** = the software platform (services, UI, APIs) that can operate on any case
> 
> So the rule is:
> 
> **Case lives in `content/` (and `E_OUTPUTS/`). Code lives in `Legalmind/` and `scripts/`.**  
> `C_VIS/` is the *case’s VIS configuration + run artifacts*, not the VIS application code.
> 
> Below is the clean, non-chaotic placement.
> 
> ---
> 
> ## 1) Your canonical layout (what goes where)
> 
> ### A) `CASE_FCFCU/content/` = Source of truth (binder + evidence)
> Keep all *human-curated* case materials here.
> 
> - `content/A_TIMELINE/`  
>   Timeline facts, event notes, chronology drafts.
> 
> - `content/B_EVIDENCE/`  
>   Raw evidence artifacts (pdfs, screenshots, recordings, mail, photos). Prefer “immutable” behavior.
> 
> - `content/D_PHASES/`  
>   Phase-specific working sets: pleadings, service issues, writ execution, damages, etc.
> 
> - `content/_ADMIN/` + `_INGEST/`  
>   Intake, scratch, staging.
> 
> ### B) `CASE_FCFCU/content/C_VIS/` = VIS config + VIS run products (case-specific)
> This folder is for **case-specific VIS rules and run outputs**, not general software.
> 
> Put here:
> - `content/C_VIS/vis.yaml` (claims taxonomy, mapping rules)
> - `content/C_VIS/templates/` (report templates, cover sheets, TOC style)
> - `content/C_VIS/mappings/` (manual overrides when auto-matching fails)
> - `content/C_VIS/runs/<run_id>/` (optional: if you want VIS outputs stored under content)
> 
> But I strongly recommend **writing generated output** to `content/E_OUTPUTS/` (see below), and keeping `C_VIS` mostly config.
> 
> ### C) `CASE_FCFCU/content/E_OUTPUTS/` = Generated artifacts (safe to delete/regenerate)
> Everything the system generates goes here:
> 
> - `content/E_OUTPUTS/vis/<run_id>/manifest.json|csv`
> - `content/E_OUTPUTS/vis/<run_id>/site/` (static HTML index/search)
> - `content/E_OUTPUTS/vis/<run_id>/VIS_Report.md`
> - `content/E_OUTPUTS/print_pack/<date>/` (tabs/covers/TOCs)
> - `content/E_OUTPUTS/exports/<date>/` (single combined PDFs, attorney packet)
> 
> **This keeps your source evidence clean and your outputs reproducible.**
> 
> ---
> 
> ## 2) Where the VIS *application code* goes
> 
> You have two viable options. Pick one and stick to it.
> 
> ### Option 1 (Recommended): VIS is a Legalmind service
> Put the actual VIS engine here:
> 
> - `CASE_FCFCU/Legalmind/backend/vis-service/`
>   - FastAPI endpoints
>   - scanner/hasher/indexer/claims mapper/exporters
> 
> This makes VIS reusable across cases and keeps code centralized.
> 
> Then `CASE_FCFCU/content/C_VIS/` holds only **case config** (`vis.yaml`, etc.).
> 
> ### Option 2: Keep a local “case engine” script (thin runner) in the case repo
> If you want a lightweight local runner regardless of Legalmind:
> 
> - `CASE_FCFCU/scripts/vis/`
>   - `run_vis.py`
>   - `vis_local.yaml` (optional)
>   - helper scripts
> 
> But the “real” engine should still live in Legalmind if you want long-term sanity.
> 
> ---
> 
> ## 3) Where MkDocs/VitePress sites go
> 
> Those are “presentation layers,” not evidence.
> 
> Keep them in `app/` exactly like you have:
> 
> - `app/mkdocs-case-view/` = court/attorney “case-view” site
> - `app/vitepress/` = alt docs site
> 
> These should **pull content from `content/`** (read-only) and/or from `E_OUTPUTS/` (generated indexes).
> 
> Rule:
> - **Sites read from:** `content/` and `content/E_OUTPUTS/`
> - **Sites never own the truth.** They only render it.
> 
> ---
> 
> ## 4) Your current oddballs: where they belong
> 
> From what I see in your root:
> 
> - `CASE_ENGINE.py`  
>   Put it under: `scripts/case_engine/CASE_ENGINE.py`  
>   If it’s meant to become VIS, it should either move into `Legalmind/backend/vis-service/` or become a thin CLI wrapper that calls that service.
> 
> - `content_audit.csv`, `front_matter_audit.json`, `proposed_case_record.csv`  
>   These are **generated diagnostics**. Move to:  
>   `content/E_OUTPUTS/audits/<date>/...`
> 
> - `Case_Data.base`  
>   If that’s a local DB for analysis, put it under:  
>   `content/E_OUTPUTS/db/Case_Data.base`  
>   (or `CASE_FCFCU/.tools/db/` if it’s purely tooling and not evidence).
> 
> ---
> 
> ## 5) The one rule that prevents future mess
> 
> ### “Immutable in, reproducible out”
> - **Immutable in:** `content/A_TIMELINE`, `content/B_EVIDENCE`, `content/D_PHASES`
> - **Config:** `content/C_VIS`
> - **Reproducible out:** `content/E_OUTPUTS`
> 
> If you follow that, you can blow away outputs and regenerate at will, while your evidentiary record stays clean.
> 
> ---
> 
> ## 6) Quick placement checklist (copy/paste mental model)
> 
> - **Evidence files:** `content/B_EVIDENCE/…`
> - **Filings drafts / working docs:** `content/D_PHASES/…`
> - **VIS rules / claim taxonomy:** `content/C_VIS/vis.yaml`
> - **VIS engine code:** `Legalmind/backend/vis-service/…`
> - **Generated reports/manifests/sites:** `content/E_OUTPUTS/vis/<run_id>/…`
> - **Websites that render everything:** `app/mkdocs-case-view/` and `app/vitepress/`
> - **Glue scripts:** `scripts/…`
> 
> ---
> 
> If you want, I can give you a **final folder tree** for `content/C_VIS` + `content/E_OUTPUTS/vis` that matches the exact VIS behaviors you want (manifest, claim map, HTML index, print pack), and a starter `vis.yaml` aligned to your FCFCU issues.

### User
> to make sure we are on the same page this is the tree of the vis. ```markdown

> . 📂 C_VIS

> └── 📂 10_violations/

> │  ├── 📄 EXH_Exhibit X — Inventory of Jurisdictional, Execut.md

> │  ├── 📄 NT_V-005_failure-to-correct-inaccurate-furnishings.md

> │  ├── 📄 NT_V-006_dual-tradeline-double-counting.md

> │  ├── 📄 NT_V-008_credit-defamation-false-publication.md

> │  ├── 📄 NT_V-009_fdCPA-misrepresentation-of-debt-status.md

> │  ├── 📄 NT_V-010_failure-to-mark-account-foreclosure-closed.md

> │  ├── 📄 NT_V-011_experian-reinvestigation-failure.md

> │  ├── 📄 NT_V-012_equifax-reinvestigation-failure.md

> │  ├── 📄 NT_V-013_transunion-reinvestigation-failure.md

> │  ├── 📄 NT_V-020_post-0815-aes-electric-charges-billed.md

> │  ├── 📄 NT_V-021_post-0815-citizens-energy-charges-billed.md

> │  ├── 📄 NT_V-022_post-0815-hoa-assessments-billed.md

> │  ├── 📄 NT_V-023_city-grass-cut-ticket-assessed-after-loss-of-access.md

> │  ├── 📄 NT_V-024_municipal-code-enforcement-after-possession-transfer.md

> │  ├── 📄 NT_V-025_cost-shift-fcfcu-refused-winterize.md

> │  ├── 📄 NT_V-026_credit-harm-compounded-utility-municipal.md

> │  ├── 📄 NT_V-031_sheriff-return-inaccuracies.md

> │  ├── 📄 NT_V-033_removal-6-7-days-after-deed-recorded.md

> │  ├── 📄 NT_V-035_court-relied-on-service-sufficiency.md

> │  ├── 📄 NT_V-036_surplus-funds-declared-resolved.md

> │  ├── 📄 NT_V-037_interest-fees-arbitrarily-inflated.md

> │  ├── 📄 NT_V-038_fcfcu-testimony-winterize-then-leave.md

> │  ├── 📄 NT_V-070_global-demand-letter.md

> │  ├── 📄 NT_V-071_litigation-hold-preservation-letter.md

> │  ├── 📄 NT_V-072_equitable-relief-tradeline-deletion.md

> │  ├── 📄 NT_V-073_damages-credit-score-suppression.md

> │  ├── 📄 NT_V-074_damages-out-of-pocket-costs.md

> │  ├── 📄 NT_V-075_public-accountability-hold.md

> │  ├── 📄 NT_V-076_fha-reasonable-accommodation-failure.md

> │  ├── 📄 NT_V-077_ada-title-iii-entertainment-access-failure.md

> │  ├── 📄 NT_V-078_ada-effective-communication-failure.md

> │  ├── 📄 NT_V-080_conversion-negligence-post-removal-damage.md

> │  ├── 📄 NT_V-081_evidence-spoliation-unplugged-cameras.md

> │  ├── 📄 NT_V-082_fraud-on-the-court-material-misrepresentation.md

> │  ├── 📄 NT_V-083_discriminatory-maintenance-redlining.md

> │  ├── 📄 NT_V-084_predatory-land-contract-reverse-redlining.md

> │  ├── 📄 OR_V-001_fcfcu-continues-reporting-first-mortgage-post-judgment-sale.md

> │  ├── 📄 OR_V-002_fcfcu-continues-reporting-second-mortgage-post-judgment-sale.md

> │  ├── 📄 OR_V-003_monthly-delinquencies-after-foreclosure-judgment.md

> │  ├── 📄 OR_V-004_past-due-amount-schedule-after-judgment.md

> │  ├── 📄 OR_V-079_void-judgment-procedural-error.md

> │  ├── 📄 PL_V-007_inconsistent-reporting-vs-court-position.md

> │  ├── 📄 PL_V-030_service-completed-no-notice-before-writ.md

> │  ├── 📄 PL_V-032_no-ada-compliant-notice.md

> │  ├── 📄 PL_V-034_attorney-appeared-without-formal-appearance.md

> │  ├── 📄 PL_V-050_cfpb-complaint-track.md

> │  ├── 📄 PL_V-051_indiana-ag-complaint-track.md

> │  ├── 📄 PL_V-052_icrc-complaint-track.md

> │  ├── 📄 PL_V-053_doj-civil-rights-complaint-track.md

> │  ├── 📄 PL_V-060_bbb-complaint-reputational-pressure.md

> └── 📂 20_theories/

> │  ├── 📄 NT_BACKUP_ARGUMENTS.md

> │  ├── 📄 NT_IF_JUDGE_PUSHBACK.md

> └── 📂 30_legal_research/

> │  ├── 📄 NT_CASE_LAW_RESEARCH.md

> │  ├── 📄 NT_JURISDICTION_THEORY.md

> │  ├── 📄 NT_LEGAL MEMORANDUM.md

> │  ├── 📄 NT_VOID_VS_VOIDABLE_ANALYSIS.md

> └── 📂 40_analysis/

> │  ├── 📄 NT_INTERNAL VALUATION MEMO.md

> │  ├── 📄 NT_Procedural_failure_map_one_pager.md

> │  ├── 📄 NT_Violation_Remedy_Inventory.md

> └── 📂 50_strategies/

> │  ├── 📄 NT_00_basis.md

> │  ├── 📄 NT_10_ada_strategy.md

> │  ├── 📄 NT_ADA_TITLE_II_ANALYSIS.md

> │  ├── 📄 NT_BUT_FOR_ANALYSIS.md

> │  ├── 📄 NT_Master_Strategy_Canvas.canvas

> │  ├── 📄 NT_PROCEDURAL_FAILURE_MAP.md

> │  ├── 📄 NT_REASONABLE_ACCOMMODATIONS.md

> │  ├── 📄 NT_REVERSAL_PATHS.md

> │  ├── 📄 NT_STATUS_TRACKER.md

> │  ├── 📄 NT_STAY_PATHS.md

> │  ├── 📄 NT_integrate_disability_separate_appe.m4a

> │  ├── 📄 OR_void_judgment_eviction_crisis.pdf

> │  ├── 📄 PL_DOJ_COMPLAINT.md

> │  ├── 📄 PL_ICRC_COMPLAINT.md

> │  ├── 📄 PL_Proposal for Strategic Reports in the Matter of.md

> │  ├── 📄 Strategic_Plan.canvas

> └── 📂 60_data_inventories/

> │  ├── 📄 NT_Violation_Index.md

> │  ├── 📄 NT_foreclosure-and-housing-litigation-case-record.csv

> │  ├── 📄 NT_inventory-of-civil-and-fair-housing-rights-vio.csv

> └── 📄 NT_01_MASTER_INDEX.md

> ```

### Assistant
> Yes—we’re aligned. What you pasted is **C_VIS as the case’s “legal intelligence library”**: violations (atomized issues), theories, research, analysis, strategies, and inventories. That is exactly what C_VIS should be.
> 
> The key distinction (so we don’t accidentally fork reality) is:
> 
> - **C_VIS (in CASE_FCFCU/content)** = curated *legal mind* content for *this* case (your violation taxonomy and reasoning artifacts)
> - **vis-service (in Legalmind/backend)** = the *software* that reads C_VIS + evidence folders and generates outputs, links, and reports
> 
> So: **C_VIS belongs in the case repo. VIS engine belongs in Legalmind.**  
> They integrate tightly, but they are not the same thing.
> 
> ---
> 
> ## What C_VIS “means” in the system
> 
> Think of your tree as a structured knowledge base with three roles:
> 
> ### 1) “Issue atoms” (10_violations/)
> Each `*_V-###_...md` is an atomic, referenceable unit:
> - stable ID (V-###)
> - claim type (NT/PL/OR/etc.)
> - elements / facts / evidence links
> - requested remedy + authority
> 
> This is the part VIS should be able to **index, cross-reference, and score for completeness**.
> 
> ### 2) “Reasoning scaffolding” (20–50)
> - theories, memo, research, strategy canvases
> - used by Legalmind agents to reason and assemble outputs
> - not necessarily evidence, but **argument structure**
> 
> ### 3) “Inventories / data” (60_data_inventories/)
> - your master index and CSV inventories
> - should become the bridge between:
>   - violations ↔ evidence ↔ docket ↔ outputs
> 
> ### 4) “Master pointers”
> - `NT_01_MASTER_INDEX.md` is your “human navigation.”
> - VIS should also generate a “machine navigation” index.
> 
> ---
> 
> ## Where this sits physically (no ambiguity)
> 
> Inside the case repo:
> 
> - `CASE_FCFCU/content/C_VIS/` = exactly the tree you posted
> 
> Inside Legalmind (software):
> 
> - `CASE_FCFCU/Legalmind/backend/vis-service/` = the engine that:
>   1) reads `content/C_VIS/**`
>   2) reads `content/B_EVIDENCE/**` and other content areas
>   3) writes outputs to `content/E_OUTPUTS/vis/<run_id>/...`
> 
> ---
> 
> ## What VIS engine should do with *your specific C_VIS tree*
> 
> Your structure gives VIS very strong handles. Here’s what the engine should implement:
> 
> ### A) Parse violation IDs and types from filenames
> From: `NT_V-031_sheriff-return-inaccuracies.md`
> Extract:
> - `doc_kind = NT`
> - `violation_id = V-031`
> - `slug = sheriff-return-inaccuracies`
> 
> Same for `PL_`, `OR_`, `EXH_` files.
> 
> ### B) Build a canonical “Violation Registry”
> Output a generated table:
> 
> - `ViolationRegistry.json/csv`
>   - V-031 → title, type, path, created/modified, linked evidence (if present), status flags
> 
> ### C) Evidence linking (2-tier)
> 1) **Auto-link** via:
>    - filename references (e.g., “Exhibit H”)
>    - explicit IDs in text (you can adopt a simple tag convention)
> 2) **Manual overrides** via:
>    - `content/C_VIS/60_data_inventories/NT_Violation_Index.md` (or a CSV mapping)
> 
> ### D) Completeness scoring (this is huge for you)
> For each `V-###` file, VIS flags:
> - Missing “Elements”
> - Missing “Evidence”
> - Missing “Authority”
> - Missing “Remedy”
> - Missing “Relief requested”
> - Missing “Timeline anchor”
> - Missing “Next action”
> 
> This turns your library into an operational system, not just writing.
> 
> ### E) Output packages
> From your current structure, VIS can generate:
> - **Attorney issue packet**: selected V-IDs + exhibits list + citations
> - **Court filing support pack**: service defects cluster, ADA cluster, damages cluster
> - **Complaint track pack**: PL_V-050..060 cluster (CFPB/AG/ICRC/DOJ/BBB)
> 
> ---
> 
> ## One thing I want you to standardize (or VIS will be weaker)
> 
> Right now your filenames are strong, but VIS will be much more lethal if each violation note has a minimal header block.
> 
> ### Suggested standard front matter for each `*_V-###*.md`
> (You can adopt this gradually; VIS can backfill missing fields.)
> 
> ```yaml
> ---
> id: V-031
> type: NT
> title: Sheriff return inaccuracies
> category: service / jurisdiction
> status: draft
> priority: high
> date_range: 2025-11-xx to 2025-12-xx
> related_evidence:
>   - EVD-2025-0ABC
>   - EVD-2025-19F2
> related_docket:
>   - "49D03-2501-MF-002559: return of service filing dated ..."
> requested_relief:
>   - vacate default judgment
>   - stay writ / quash writ
> ---
> ```
> 
> This is what makes automation reliable.
> 
> ---
> 
> ## Final answer to “are we on the same page?”
> Yes. Your `C_VIS` tree is the **case-specific legal intelligence corpus**.
> 
> ### The only adjustment I’m making:
> - Do **not** move this into `Legalmind/` as content.
> - Instead, **Legalmind consumes it**.
> - Legalmind owns the code; CASE_FCFCU owns the substance.
> 
> ---
> 
> If you want next-step clarity: tell me which you want first, and I’ll produce it in copy/paste form:
> 
> 1) A `vis.yaml` that mirrors your folders and establishes clusters (Service/Jurisdiction, ADA, Credit Reporting/FCRA, Post-removal damages, Complaint tracks).  
> 2) A “front matter schema” + an auto-linter spec for your `*_V-###` notes.  
> 3) The exact `vis-service` endpoints and how they should surface “Violation Registry” to the frontend.

### User
> ok, so the c vis is the data and the service just reads it. ok, so if anything what do i need to tell gemini to do in this repo if anything at all.

### Assistant
> Correct: **C_VIS is data. `vis-service` reads it.** In this repo you don’t need Gemini to “rewrite C_VIS.” You need Gemini to do two concrete things (optionally three), and that’s it.
> 
> ## What to tell Gemini to do (in this repo)
> 
> ### 1) Add a VIS runner + contract files (minimum, high leverage)
> You want a thin, deterministic way to run VIS against `content/` without touching Legalmind internals.
> 
> Add these to `CASE_FCFCU/`:
> 
> - `content/C_VIS/vis.yaml`  
>   Case-specific rules: clusters, keywords, mapping heuristics, output preferences.
> 
> - `scripts/vis/run_vis.sh` and/or `scripts/vis/run_vis.py`  
>   A one-click runner that:
>   - points to binder root (`content/`)
>   - calls the VIS engine (either local python module or HTTP call to Legalmind vis-service)
>   - writes outputs to `content/E_OUTPUTS/vis/<run_id>/...`
> 
> - `scripts/vis/README.md`  
>   “How to run VIS” from cold start.
> 
> This keeps your case repo self-contained: open it, run one script, outputs appear.
> 
> ### 2) Add a “linking convention” so VIS can auto-map evidence (critical)
> Right now your V-notes don’t have a guaranteed machine-readable evidence list. Tell Gemini to add a standard and optionally a linter.
> 
> Add:
> 
> - `content/C_VIS/_schema/violation_front_matter.yaml` (or a markdown spec)
> - optional `scripts/vis/lint_vis_notes.py` that flags missing fields
> 
> This is what makes the system not fragile.
> 
> ### 3) (Optional) Wire MkDocs/VitePress to display VIS outputs
> If you want the case-view site to automatically show the latest VIS run:
> 
> - configure `app/mkdocs-case-view` nav to include:
>   - `content/C_VIS/NT_01_MASTER_INDEX.md`
>   - `content/E_OUTPUTS/vis/latest/VIS_Report.md`
>   - `content/E_OUTPUTS/vis/latest/site/` (or link)
> 
> This is “presentation,” not core.
> 
> ---
> 
> ## The exact Gemini prompt (repo-scoped)
> Copy/paste this. It is tightly constrained to **CASE_FCFCU** repo work.
> 
> ```text
> You are working inside my repo CASE_FCFCU. IMPORTANT: C_VIS is case data, not app code. Do NOT restructure my content folders. Your job is to add a small amount of repo glue so the VIS engine (implemented elsewhere as a service) can run against this repo consistently.
> 
> TASKS (do all)
> 1) Create a case-specific VIS configuration file at:
>    content/C_VIS/vis.yaml
>    It must define:
>    - binder_root default: content/
>    - violation_notes_root: content/C_VIS/
>    - evidence_root: content/B_EVIDENCE/
>    - outputs_root: content/E_OUTPUTS/vis/
>    - clusters (at least): service_jurisdiction, ada_disability, credit_reporting, post_removal_damages, complaint_tracks, fees_interest_accounting
>    Each cluster should include filename prefixes (NT_/PL_/OR_/EXH_), keyword lists, and path patterns that match my current C_VIS structure.
> 
> 2) Add a one-click VIS runner under:
>    scripts/vis/
>    Provide BOTH:
>    - run_vis.sh (mac/linux)
>    - run_vis.ps1 (windows)
>    Each script should:
>    - set BINDER_ROOT to repo/content
>    - create a run_id = timestamp like YYYYMMDD-HHMMSS
>    - create output dir: content/E_OUTPUTS/vis/<run_id>/
>    - call VIS via HTTP if available:
>        POST http://localhost:8080/vis/run with JSON {binder_root, config_path, run_id}
>      If VIS service is not available, print a clear message and exit with nonzero code.
>    - write a "latest" pointer by creating/refreshing:
>        content/E_OUTPUTS/vis/latest -> <run_id> (symlink if possible, else a text file latest.txt containing <run_id>)
>    - print the output paths at the end.
> 
> 3) Add documentation:
>    scripts/vis/README.md
>    Must include:
>    - prerequisites (Legalmind vis-service running locally on port 8080 OR configurable)
>    - how to run on Windows and macOS/Linux
>    - where outputs land
>    - troubleshooting
> 
> OPTIONAL (only if simple)
> 4) Add a lightweight linter:
>    scripts/vis/lint_c_vis.py
>    It scans content/C_VIS/10_violations/*.md and checks for YAML front matter keys:
>    id, type, title, category, status, related_evidence
>    Output a report to content/E_OUTPUTS/vis/<run_id>/lint_report.md
> 
> CONSTRAINTS
> - Do not change existing C_VIS file names or move folders.
> - Do not add heavy dependencies.
> - Keep scripts readable and robust.
> - Use relative paths from repo root.
> - Assume this repo may run on a Chromebook (bash) and Windows laptop (PowerShell).
> 
> DELIVERABLE
> Return the exact file contents for each created file.
> ```
> 
> ---
> 
> ## What you do NOT need to ask Gemini to do
> - Don’t have it “build VIS logic” in this repo (that belongs in `Legalmind/backend/vis-service`).
> - Don’t have it reorganize `C_VIS` (you already nailed the structure).
> - Don’t have it invent legal content. Keep automation mechanical.
> 
> ---
> 
> If you want the cleanest implementation: decide whether you want the runner to call **HTTP** (vis-service) or run a **local python module**. HTTP is better because it keeps Legalmind as the engine and this repo as data.

### User
> i will go with your suggestions i about to give yout eh app files. This is a comprehensive, modular Python solution for the Violation Intelligence System (VIS).
> 
> It is designed to be dropped into your repository root. It includes the scanner, integrity engine, report generator, static site builder, and the optional API.
> 
> Project Structure
> Plaintext
> /
> ├── vis/
> │   ├── __init__.py
> │   ├── config.yaml         # Configuration & Claims Taxonomy
> │   ├── main.py             # CLI Entrypoint
> │   ├── scanner.py          # Core Logic: Scanning, Hashing, Classification
> │   ├── report.py           # Output Generator: Reports, HTML, Manifests
> │   ├── server.py           # FastAPI Web Server
> │   └── templates.py        # HTML/Markdown Templates (embedded for portability)
> ├── requirements.txt
> └── README.md
> 1. Configuration & Claims Taxonomy
> This YAML file defines how VIS understands your specific case. It includes the "Claims Map" you requested to tie evidence to legal arguments.
> Config
> Jan 16, 9:27 AM
> 
> 2. Dependencies
> Dependencies
> Jan 16, 9:27 AM
> 3. Core Logic: Scanner & Integrity
> Handles file walking, SHA-256 hashing (streaming for large files), metadata extraction, and classification.
> Scanner
> Jan 16, 9:28 AM
> 
> 4. Templates (Embedded)
> Keeps the codebase portable by embedding Jinja2 and Markdown templates.
> Templates
> Jan 16, 9:28 AM
> 
> 5. Report Generator
> Coordinates the generation of the static HTML site, the Markdown report, and the CSV/JSON manifests.
> Reports
> Jan 16, 9:28 AM
> 
> 6. Optional API Server
> A FastAPI implementation to expose VIS data programmatically or to a local frontend.
> API
> Jan 16, 9:28 AM
> 
> 7. CLI Entrypoint
> The main driver script.
> CLI
> Jan 16, 9:28 AM
> 
> Conclusion & Run Instructions
> This creates a complete, standalone tool.
> 
> 1. Install
> 
> Bash
> pip install -r requirements.txt
> 
> **2. Setup Configuration**
> Edit `vis/config.yaml` to match your specific legal claims. Add the keywords for your specific "Service Defect" or "Procedural Failure" arguments.
> 
> **3. Run the Tool**
> Assume your data is in `../My_Legal_Case`.
> ```bash
> python -m vis.main run --binder "../My_Legal_Case"
> 
> **4. View Results**
> Go to `../My_Legal_Case/output/`.
> * Open `VIS_Report.md` for your claims map and attorney packet.
> * Open `site/index.html` for the clickable, offline web-browser view of your evidence.
> * Check `manifest.csv` for the raw list of SHA-256 hashes.
> 
> **5. (Optional) Serve API**
> ```bash
> python -m vis.main serve --binder "../My_Legal_Case"
> Access docs at `http://localhost:8000/docs`. which files do you want to see.

### Assistant
> Good. This is the right moment to be selective and disciplined.
> 
> I **do not** need to see everything. If you dump all files at once, we lose signal.  
> I want to verify **architecture alignment + correctness at the seams**.
> 
> ## Show me these files, in this order
> 
> ### 1️⃣ `vis/config.yaml`  **(first, non-negotiable)**
> Why:
> - This determines whether VIS correctly maps to **C_VIS as data**
> - This is where most systems quietly break
> 
> I’m checking:
> - Does it reference `content/C_VIS/**` cleanly?
> - Does it respect your violation ID scheme (`NT_V-###`, `PL_V-###`, etc.)?
> - Does it separate **clusters vs evidence vs outputs**?
> - Does it avoid hardcoding paths that will conflict with Legalmind later?
> 
> If config is wrong, everything else is noise.
> 
> ---
> 
> ### 2️⃣ `vis/scanner.py`
> Why:
> - This is the **truth engine** (hashing, walking, classification)
> - This must be deterministic and *read-only*
> 
> I’m checking:
> - SHA-256 streaming (no memory blowups)
> - Stable ID generation (hash-based or content-based, not order-based)
> - No mutation of source files
> - Clean abstraction between:
>   - file discovery
>   - classification
>   - metadata extraction
> 
> If scanner is solid, VIS is trustworthy.
> 
> ---
> 
> ### 3️⃣ `vis/report.py`
> Why:
> - This tells me whether VIS is an **index generator** or a **legal intelligence engine**
> 
> I’m checking:
> - Does it treat C_VIS notes as **authoritative claim objects**, not “documents to summarize”?
> - Does it emit:
>   - manifest (csv/json)
>   - claims → evidence mapping
>   - markdown report that could actually be handed to counsel?
> - Does it cleanly write to `/output/` (or equivalent), not pollute content?
> 
> ---
> 
> ### 4️⃣ `vis/main.py` (CLI)
> Why:
> - This defines how a human actually uses the system
> - This is what later becomes the bridge to Legalmind or scripts
> 
> I’m checking:
> - Clear commands (`run`, `serve`)
> - No hidden globals
> - Binder path passed explicitly
> - Exit codes and errors handled cleanly
> 
> ---
> 
> ### 5️⃣ `vis/server.py` (optional, but useful)
> Why:
> - Only to verify it won’t fight Legalmind later
> 
> I’m checking:
> - Thin API layer
> - No business logic duplicated from scanner/report
> - Clean separation so this can later be **deleted or replaced** by Legalmind’s `vis-service`
> 
> ---
> 
> ## Do NOT send yet
> Hold these for now unless I explicitly ask:
> - `templates.py`
> - `requirements.txt`
> - `README.md`
> 
> Those are secondary once core correctness is confirmed.
> 
> ---
> 
> ## Summary (grounding you)
> You did the right thing architecturally.  
> Now we’re validating **alignment**, not “does it run.”
> 
> 👉 **Start by sending `vis/config.yaml`.**  
> Once that passes, we move down the stack.

### User
> #!/bin/bash

> 

> # Define root directory for the service

> BASE_DIR="backend/vis-service"

> SERVICES_DIR="$BASE_DIR/services"

> 

> echo "Creating directory structure..."

> mkdir -p "$SERVICES_DIR"

> 

> echo "Writing backend/vis-service/vis.yaml..."

> cat << 'EOF' > "$BASE_DIR/vis.yaml"

> # Violation Intelligence System (VIS) - Default Configuration

> version: 1.0

> 

> # Classification: Maps folder names or file extensions to categories

> classification:

>   filings: ["filings", "motions", "orders", "pleadings", "court"]

>   exhibits: ["exhibits", "evidence", "discovery", "production"]

>   correspondence: ["letters", "emails", "communications"]

>   docket: ["docket", "ccs", "chronological case summary", "receipt"]

>   multimedia: [".mp3", ".mp4", ".wav", ".mov", ".png", ".jpg", ".jpeg"]

> 

> # Date Extraction: Regex patterns to find dates in filenames (processed in order)

> date_patterns:

>   - '(\d{4}-\d{2}-\d{2})'  # YYYY-MM-DD

>   - '(\d{4}\d{2}\d{2})'    # YYYYMMDD

>   - '(\d{2}-\d{2}-\d{4})'  # MM-DD-YYYY

> 

> # Claims Map: The "Brain" of VIS

> claims:

>   - id: "CLM-SERVICE-001"

>     title: "Defective Service of Process"

>     description: "Failure to comply with TR 4.1(B) regarding certified mailing."

>     keywords:

>       - "summons"

>       - "return of service"

>       - "certified mail"

>       - "unclaimed"

>       - "green card"

>       - "affidavit of service"

>     paths:

>       - "service"

>       - "summons"

> 

>   - id: "CLM-ADA-002"

>     title: "ADA Non-Compliance"

>     description: "Denial of requested accommodations for hearings."

>     keywords:

>       - "ADA"

>       - "accommodation"

>       - "request"

>       - "disability"

>       - "coordinator"

> 

>   - id: "CLM-JURIS-003"

>     title: "Jurisdictional Challenge"

>     description: "Court lacks personal jurisdiction due to void service."

>     keywords:

>       - "jurisdiction"

>       - "dismiss"

>       - "void"

>       - "12(b)"

> EOF

> 

> echo "Writing backend/vis-service/Dockerfile..."

> cat << 'EOF' > "$BASE_DIR/Dockerfile"

> FROM python:3.11-slim

> 

> WORKDIR /app

> 

> # Install system dependencies if needed (e.g., for magic/mime types)

> RUN apt-get update && apt-get install -y libmagic1 && rm -rf /var/lib/apt/lists/*

> 

> COPY requirements.txt .

> RUN pip install --no-cache-dir -r requirements.txt

> 

> COPY . .

> 

> # Run as non-root user for security

> RUN useradd -m visuser

> USER visuser

> 

> EXPOSE 8000

> 

> CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

> EOF

> 

> echo "Writing backend/vis-service/requirements.txt..."

> cat << 'EOF' > "$BASE_DIR/requirements.txt"

> fastapi>=0.100.0

> uvicorn>=0.22.0

> python-multipart>=0.0.6

> pyyaml>=6.0

> jinja2>=3.1.0

> aiofiles>=23.0.0

> python-magic>=0.4.27

> pydantic>=2.0.0

> EOF

> 

> echo "Writing backend/vis-service/services/__init__.py..."

> touch "$SERVICES_DIR/__init__.py"

> 

> echo "Writing backend/vis-service/services/hasher.py..."

> cat << 'EOF' > "$SERVICES_DIR/hasher.py"

> import hashlib

> from pathlib import Path

> 

> class HasherService:

>     @staticmethod

>     def calculate_sha256(filepath: Path, chunk_size: int = 8192) -> str:

>         """Streaming SHA256 calculation to handle large evidence files efficiently."""

>         sha256 = hashlib.sha256()

>         try:

>             with open(filepath, "rb") as f:

>                 while chunk := f.read(chunk_size):

>                     sha256.update(chunk)

>             return sha256.hexdigest()

>         except Exception as e:

>             return f"HASH_ERROR_{str(e)}"

> 

>     @staticmethod

>     def generate_stable_id(file_hash: str) -> str:

>         """

>         Generates a deterministic ID based on the file hash.

>         Format: EVD-{First 8 chars of Hash}

>         """

>         if not file_hash or "ERROR" in file_hash:

>             return "EVD-UNKNOWN"

>         return f"EVD-{file_hash[:8].upper()}"

> EOF

> 

> echo "Writing backend/vis-service/services/metadata.py..."

> cat << 'EOF' > "$SERVICES_DIR/metadata.py"

> import re

> import os

> import datetime

> import mimetypes

> from pathlib import Path

> from typing import List, Dict

> 

> class MetadataService:

>     def __init__(self, config: Dict):

>         self.config = config

> 

>     def infer_date(self, filename: str, stat_result: os.stat_result) -> str:

>         """Extracts date from filename patterns or falls back to file modification time."""

>         patterns = self.config.get('date_patterns', [])

>         for pattern in patterns:

>             match = re.search(pattern, filename)

>             if match:

>                 return match.group(1)

>         

>         # Fallback to Modified Time

>         dt = datetime.datetime.fromtimestamp(stat_result.st_mtime)

>         return dt.strftime('%Y-%m-%d')

> 

>     def classify_type(self, path: Path) -> str:

>         """Classifies file based on path keywords and extension."""

>         path_str = str(path).lower()

>         filename = path.name.lower()

>         

>         rules = self.config.get('classification', {})

>         

>         for category, keywords in rules.items():

>             for kw in keywords:

>                 if kw in path_str or kw in filename:

>                     return category

>         

>         # Default fallback based on mime

>         mime, _ = mimetypes.guess_type(path)

>         if mime:

>             if mime.startswith('image'): return 'image'

>             if mime.startswith('video'): return 'video'

>             if mime.startswith('audio'): return 'audio'

>             if mime == 'application/pdf': return 'document'

>             

>         return "uncategorized"

> EOF

> 

> echo "Writing backend/vis-service/services/storage_adapter.py..."

> cat << 'EOF' > "$SERVICES_DIR/storage_adapter.py"

> import json

> import csv

> import shutil

> from pathlib import Path

> from typing import Dict, List, Any

> 

> class StorageAdapter:

>     """

>     Handles all I/O operations to ensure we strictly write ONLY to the output directory.

>     """

>     def __init__(self, binder_root: str, run_id: str):

>         self.binder_root = Path(binder_root).resolve()

>         self.output_base = self.binder_root / "output" / "vis" / run_id

>         self.site_dir = self.output_base / "site"

>         

>         # Ensure directories exist

>         self.output_base.mkdir(parents=True, exist_ok=True)

>         self.site_dir.mkdir(parents=True, exist_ok=True)

> 

>     def write_json(self, filename: str, data: Any):

>         with open(self.output_base / filename, 'w') as f:

>             json.dump(data, f, indent=2, default=str)

> 

>     def write_csv(self, filename: str, data: List[Dict]):

>         if not data:

>             return

>         keys = data[0].keys()

>         with open(self.output_base / filename, 'w', newline='') as f:

>             writer = csv.DictWriter(f, fieldnames=keys)

>             writer.writeheader()

>             writer.writerows(data)

> 

>     def write_text(self, filename: str, content: str):

>         with open(self.output_base / filename, 'w') as f:

>             f.write(content)

> 

>     def write_site_file(self, rel_path: str, content: str):

>         """Writes HTML files to the site directory, creating subdirs as needed."""

>         target = self.site_dir / rel_path

>         target.parent.mkdir(parents=True, exist_ok=True)

>         with open(target, 'w') as f:

>             f.write(content)

> 

>     def load_run_data(self):

>         """Loads manifest.json from the run directory."""

>         manifest_path = self.output_base / "manifest.json"

>         if not manifest_path.exists():

>             raise FileNotFoundError(f"No manifest found for run at {manifest_path}")

>         with open(manifest_path, 'r') as f:

>             return json.load(f)

> EOF

> 

> echo "Writing backend/vis-service/services/claims_mapper.py..."

> cat << 'EOF' > "$SERVICES_DIR/claims_mapper.py"

> from typing import List, Dict

> 

> class ClaimsMapper:

>     def __init__(self, config: Dict):

>         self.claims_config = config.get('claims', [])

> 

>     def map_claims(self, file_manifest: List[Dict]) -> List[Dict]:

>         """

>         Iterates through defined claims and finds matching evidence from the manifest.

>         Returns a structured Claims Map.

>         """

>         mapped_claims = []

>         

>         for claim in self.claims_config:

>             evidence = []

>             keywords = [k.lower() for k in claim.get('keywords', [])]

>             paths = [p.lower() for p in claim.get('paths', [])]

>             

>             for file_item in file_manifest:

>                 # Check keywords in filename

>                 match_keyword = any(k in file_item['filename'].lower() for k in keywords)

>                 

>                 # Check path segments

>                 match_path = any(p in file_item['rel_path'].lower() for p in paths)

>                 

>                 if match_keyword or match_path:

>                     evidence.append({

>                         "id": file_item['id'],

>                         "filename": file_item['filename'],

>                         "rel_path": file_item['rel_path'],

>                         "type": file_item['type']

>                     })

>             

>             mapped_claims.append({

>                 "claim": claim,

>                 "evidence_count": len(evidence),

>                 "evidence": evidence

>             })

>             

>         return mapped_claims

> EOF

> 

> echo "Writing backend/vis-service/services/indexer.py..."

> cat << 'EOF' > "$SERVICES_DIR/indexer.py"

> from jinja2 import Template

> from pathlib import Path

> from typing import List, Dict

> from .storage_adapter import StorageAdapter

> 

> HTML_TEMPLATE = """

> <!DOCTYPE html>

> <html lang="en">

> <head>

>     <meta charset="UTF-8">

>     <meta name="viewport" content="width=device-width, initial-scale=1.0">

>     <title>VIS Index - {{ folder_name }}</title>

>     <style>

>         :root { --bg: #1a1a1a; --fg: #e0e0e0; --accent: #00d4ff; --border: #333; }

>         body { font-family: sans-serif; background: var(--bg); color: var(--fg); padding: 20px; }

>         .container { max-width: 1200px; margin: 0 auto; }

>         a { color: var(--accent); text-decoration: none; }

>         table { width: 100%; border-collapse: collapse; margin-top: 20px; }

>         th, td { text-align: left; padding: 10px; border-bottom: 1px solid var(--border); }

>         .badge { background: #333; padding: 2px 6px; border-radius: 4px; font-size: 0.8em; }

>     </style>

> </head>

> <body>

>     <div class="container">

>         <h1>📂 {{ folder_name }}</h1>

>         <p><a href="../index.html">⬆ Up Level</a></p>

> 

>         <h3>Files</h3>

>         <table>

>             <thead><tr><th>ID</th><th>Name</th><th>Date</th><th>Type</th><th>Size</th></tr></thead>

>             <tbody>

>                 {% for file in files %}

>                 <tr>

>                     <td><span class="badge">{{ file.id }}</span></td>

>                     <td><a href="{{ file.link_path }}" target="_blank">{{ file.filename }}</a></td>

>                     <td>{{ file.inferred_date }}</td>

>                     <td>{{ file.type }}</td>

>                     <td>{{ (file.size_bytes / 1024)|round(1) }} KB</td>

>                 </tr>

>                 {% endfor %}

>             </tbody>

>         </table>

>     </div>

> </body>

> </html>

> """

> 

> class IndexerService:

>     def __init__(self, storage: StorageAdapter):

>         self.storage = storage

> 

>     def generate_indexes(self, manifest: List[Dict], folder_structure: Dict[str, List[Dict]]):

>         """Generates static HTML indexes and a search index JSON."""

>         template = Template(HTML_TEMPLATE)

> 

>         # 1. Generate Search Index for Frontend

>         search_index = [

>             {

>                 "id": f['id'],

>                 "text": f"{f['filename']} {f['rel_path']} {f['type']}",

>                 "path": f['rel_path']

>             }

>             for f in manifest

>         ]

>         self.storage.write_json("search_index.json", search_index)

> 

>         # 2. Generate HTML Pages

>         for folder_path, files in folder_structure.items():

>             # Calculate relative path depth for linking back to assets

>             # In a real viewer, we serve files via API, but for static site, we need relative links

>             # Assuming folder_path is relative to binder root

>             

>             processed_files = []

>             depth = len(Path(folder_path).parts) if folder_path != "Root" else 0

>             back_prefix = "../" * (depth + 2) # +2 for output/vis/run_id/site/ nesting

> 

>             for f in files:

>                 f_view = f.copy()

>                 # Link directly to the file on disk (relative)

>                 # output/vis/run_id/site/Folder -> binder_root/Folder/File

>                 f_view['link_path'] = f"{back_prefix}{f['rel_path']}"

>                 processed_files.append(f_view)

> 

>             html = template.render(

>                 folder_name=folder_path,

>                 files=processed_files

>             )

>             

>             # Write to site/Folder/index.html

>             if folder_path == "Root":

>                 self.storage.write_site_file("index.html", html)

>             else:

>                 self.storage.write_site_file(f"{folder_path}/index.html", html)

> EOF

> 

> echo "Writing backend/vis-service/services/scanner.py..."

> cat << 'EOF' > "$SERVICES_DIR/scanner.py"

> import os

> from pathlib import Path

> from typing import List, Dict, Tuple

> from .hasher import HasherService

> from .metadata import MetadataService

> 

> class ScannerService:

>     def __init__(self, root_path: str, config: Dict):

>         self.root_path = Path(root_path).resolve()

>         self.metadata_service = MetadataService(config)

>         self.folder_structure = {"Root": []}

> 

>     def scan(self) -> Tuple[List[Dict], Dict[str, List[Dict]]]:

>         results = []

>         

>         # Walk directory

>         for root, dirs, files in os.walk(self.root_path):

>             # Block output directory to prevent recursion

>             if 'output' in root.split(os.sep):

>                 continue

>                 

>             for file in files:

>                 if file.startswith('.'): continue

>                 

>                 full_path = Path(root) / file

>                 relative_path = full_path.relative_to(self.root_path)

>                 

>                 try:

>                     stat = full_path.stat()

>                     file_hash = HasherService.calculate_sha256(full_path)

>                     stable_id = HasherService.generate_stable_id(file_hash)

>                     

>                     item = {

>                         "id": stable_id,

>                         "filename": file,

>                         "rel_path": str(relative_path),

>                         "size_bytes": stat.st_size,

>                         "sha256": file_hash,

>                         "created_ts": stat.st_ctime,

>                         "modified_ts": stat.st_mtime,

>                         "inferred_date": self.metadata_service.infer_date(file, stat),

>                         "type": self.metadata_service.classify_type(full_path)

>                     }

>                     results.append(item)

>                     

>                     # Organize for Indexer

>                     parent = str(relative_path.parent)

>                     if parent == ".": parent = "Root"

>                     

>                     if parent not in self.folder_structure:

>                         self.folder_structure[parent] = []

>                     self.folder_structure[parent].append(item)

>                     

>                 except PermissionError:

>                     print(f"Skipping {full_path}: Permission Denied")

>                     

>         return results, self.folder_structure

> EOF

> 

> echo "Writing backend/vis-service/main.py..."

> cat << 'EOF' > "$BASE_DIR/main.py"

> import os

> import yaml

> import time

> from typing import Optional

> from fastapi import FastAPI, HTTPException, BackgroundTasks, Query

> from fastapi.responses import FileResponse, JSONResponse

> from pydantic import BaseModel

> from pathlib import Path

> 

> # Service Imports

> from services.scanner import ScannerService

> from services.claims_mapper import ClaimsMapper

> from services.indexer import IndexerService

> from services.storage_adapter import StorageAdapter

> 

> app = FastAPI(title="VIS Service", description="Violation Intelligence System Backend")

> 

> # --- Models ---

> class RunRequest(BaseModel):

>     binder_root: str

>     config_path: Optional[str] = None

> 

> class RunResponse(BaseModel):

>     run_id: str

>     status: str

>     output_path: str

> 

> # --- Helpers ---

> def load_config(path: str = "vis.yaml"):

>     if not os.path.exists(path):

>         return {}

>     with open(path, 'r') as f:

>         return yaml.safe_load(f)

> 

> def run_vis_task(run_id: str, binder_root: str, config_path: str):

>     """Background task to execute the scan pipeline."""

>     try:

>         print(f"[{run_id}] Starting VIS Scan on {binder_root}")

>         

>         # 1. Load Config

>         config = load_config(config_path or "vis.yaml")

>         

>         # 2. Init Services

>         scanner = ScannerService(binder_root, config)

>         storage = StorageAdapter(binder_root, run_id)

>         claims_mapper = ClaimsMapper(config)

>         indexer = IndexerService(storage)

>         

>         # 3. Execute Scan

>         manifest, folder_struct = scanner.scan()

>         

>         # 4. Map Claims

>         claims_map = claims_mapper.map_claims(manifest)

>         

>         # 5. Generate Outputs

>         storage.write_json("manifest.json", manifest)

>         storage.write_csv("manifest.csv", manifest)

>         storage.write_json("claims_map.json", claims_map)

>         

>         indexer.generate_indexes(manifest, folder_struct)

>         

>         print(f"[{run_id}] VIS Scan Complete. Artifacts in {storage.output_base}")

>         

>     except Exception as e:

>         print(f"[{run_id}] CRITICAL FAILURE: {str(e)}")

>         # In real prod, write to a status file/db

> 

> # --- API Endpoints ---

> 

> @app.post("/vis/run", response_model=RunResponse)

> async def trigger_run(req: RunRequest, background_tasks: BackgroundTasks):

>     """

>     Triggers a VIS scan on the local binder directory.

>     Local-first: Expects 'binder_root' to be a valid path on the server's filesystem.

>     """

>     if not os.path.exists(req.binder_root):

>         raise HTTPException(status_code=400, detail="Binder root path does not exist")

> 

>     run_id = str(int(time.time()))

>     background_tasks.add_task(run_vis_task, run_id, req.binder_root, req.config_path)

>     

>     output_path = str(Path(req.binder_root) / "output" / "vis" / run_id)

>     return RunResponse(run_id=run_id, status="accepted", output_path=output_path)

> 

> @app.get("/vis/runs/{run_id}/manifest")

> async def get_manifest(run_id: str, binder_root: str):

>     """Retrieves the file manifest for a specific run."""

>     storage = StorageAdapter(binder_root, run_id)

>     try:

>         data = storage.load_run_data()

>         return data

>     except FileNotFoundError:

>         raise HTTPException(status_code=404, detail="Run ID or Manifest not found")

> 

> @app.get("/vis/runs/{run_id}/claims")

> async def get_claims(run_id: str, binder_root: str):

>     """Retrieves the claims map."""

>     path = Path(binder_root) / "output" / "vis" / run_id / "claims_map.json"

>     if not path.exists():

>         raise HTTPException(status_code=404, detail="Claims map not found")

>     with open(path, 'r') as f:

>         import json

>         return json.load(f)

> 

> @app.get("/vis/runs/{run_id}/search")

> async def search_evidence(run_id: str, binder_root: str, q: str):

>     """Simple search over the generated index."""

>     storage = StorageAdapter(binder_root, run_id)

>     try:

>         data = storage.load_run_data()

>         q_lower = q.lower()

>         results = [

>             f for f in data 

>             if q_lower in f['filename'].lower() or q_lower in f['rel_path'].lower()

>         ]

>         return {"count": len(results), "results": results}

>     except FileNotFoundError:

>         raise HTTPException(status_code=404, detail="Run data not found")

> 

> @app.get("/vis/site/{run_id}/{file_path:path}")

> async def serve_static_site(run_id: str, binder_root: str, file_path: str):

>     """

>     Serves the generated static HTML site for a run.

>     """

>     base_path = Path(binder_root) / "output" / "vis" / run_id / "site"

>     target_file = (base_path / file_path).resolve()

>     

>     # Security check: Ensure we don't traverse out of the site directory

>     if not str(target_file).startswith(str(base_path)):

>         raise HTTPException(status_code=403, detail="Access denied")

>         

>     if not target_file.exists():

>         # Try appending index.html if directory

>         if (target_file / "index.html").exists():

>             target_file = target_file / "index.html"

>         else:

>             raise HTTPException(status_code=404, detail="File not found")

>             

>     return FileResponse(target_file)

> EOF

> 

> echo "Done. VIS service structure created in $BASE_DIR."

### Assistant
> Yep—this is close. But as-written, it will bite you in a few predictable places. Here’s what’s right, what’s wrong, and exactly what to tell Gemini to change.
> 
> ## What you built correctly
> - **Service lives under `Legalmind/backend/vis-service/`** (that’s the right “engine location”).
> - **Streaming SHA-256** + deterministic ID from hash: correct.
> - **Output isolation**: writes under `binder_root/output/vis/<run_id>` and scanner skips `output/`: correct intent.
> - **Claims mapper** is intentionally dumb (keyword/path matching). That’s fine for v1.
> 
> ## What’s wrong (and needs fixing)
> ### 1) Your `vis.yaml` is incomplete (hard break)
> Your heredoc for `vis.yaml` never closes the YAML document properly and is missing the claim’s `paths` for `CLM-JURIS-003`. Also you never ended the heredoc with `EOF` in the snippet you posted (unless it got cut off). That will produce a truncated file.
> 
> **Fix:** close the last claim and the heredoc cleanly.
> 
> ### 2) You’re putting config in the service folder — but the case config belongs in `content/C_VIS/`
> Right now you wrote `backend/vis-service/vis.yaml`. That’s fine as a *default*, but your real case taxonomy needs to live in:
> 
> - `CASE_FCFCU/content/C_VIS/vis.yaml`
> 
> Service should accept `config_path` pointing to the case file. That is the whole “C_VIS is data” doctrine.
> 
> ### 3) Your API forces the client to pass `binder_root` on every GET
> `GET /vis/runs/{run_id}/manifest` requires `binder_root` as a query param. That’s awkward and unsafe. The service should store a `run_meta.json` at run time with binder_root + config path, then all later calls only need `run_id`.
> 
> ### 4) Date extraction returns raw formats (YYYYMMDD stays YYYYMMDD)
> That breaks chronology and sorting. Normalize into `YYYY-MM-DD`.
> 
> ### 5) Static site links will be unreliable
> Your indexer tries to link from `output/vis/<run_id>/site/...` back to the original file using `../` math. That will break depending on depth and browser file security rules.
> 
> Two sane options:
> - **Option A (recommended):** copy (or hardlink/symlink) files into `site/assets/...` and link locally.
> - **Option B:** don’t link directly; add an API endpoint to stream files and link to `/vis/runs/{run_id}/file/<evidence_id>`.
> 
> Right now you’re halfway between the two.
> 
> ### 6) No run status / error reporting
> You print errors, but you don’t write a status artifact. You need:
> - `status.json` with `{run_id, state: accepted|running|complete|error, error_message?}`
> 
> Otherwise “accepted” is a lie if the background task crashes.
> 
> ### 7) Small but real: missing `__init__.py` at `backend/vis-service/`
> Not strictly required, but you are importing `services.*` as a package. It’s safer to make the service root a package or ensure module paths are stable.
> 
> ---
> 
> ## What to tell Gemini to do (tight, repo-specific)
> Paste this to Gemini and tell it to implement changes directly in your repo.
> 
> ```text
> You are modifying an existing FastAPI microservice at Legalmind/backend/vis-service. Do not restructure the repo. Make the following fixes and improvements.
> 
> 1) FIX vis.yaml DEFAULT
> - Ensure backend/vis-service/vis.yaml is valid YAML and complete.
> - Add missing fields, close all lists, and ensure all claims have id/title/description/keywords/paths.
> 
> 2) SUPPORT CASE CONFIG PATH (C_VIS IS DATA)
> - The service must accept config_path that points to a file inside the case repo, e.g. CASE_FCFCU/content/C_VIS/vis.yaml.
> - Resolve relative config paths safely.
> 
> 3) PERSIST RUN METADATA AND STATUS
> - When a run starts, create output/vis/<run_id>/status.json with state "running".
> - On success set state "complete"; on exception set state "error" and include error_message.
> - Write output/vis/<run_id>/run_meta.json with binder_root and resolved config_path.
> - Add GET /vis/runs/{run_id}/status that reads status.json.
> - Update existing GET endpoints so they NO LONGER require binder_root query param; they load binder_root from run_meta.json.
> 
> 4) DATE NORMALIZATION
> - In MetadataService.infer_date(), normalize YYYYMMDD -> YYYY-MM-DD and MM-DD-YYYY -> YYYY-MM-DD.
> 
> 5) STATIC SITE LINKING (MAKE IT RELIABLE)
> Pick ONE of these and implement it cleanly:
> A) Copy evidence into site/assets/<rel_path> (create dirs), and link to that local copy.
> OR
> B) Add GET /vis/runs/{run_id}/file/{evidence_id} that streams the original file safely, and link to that endpoint.
> Do not use brittle ../ prefix math.
> 
> 6) SECURITY
> - For any endpoint that serves files, enforce path traversal protections by resolving and ensuring the resolved path is inside binder_root.
> - Explicitly block serving anything under binder_root/output to prevent recursion.
> 
> 7) QUALITY
> - Add backend/vis-service/__init__.py
> - Make load_config robust: if yaml load fails, mark run status error.
> - Ensure scanner excludes output directories deterministically.
> 
> Return the full updated code for main.py, metadata.py, indexer.py, storage_adapter.py, scanner.py, and the updated vis.yaml.
> ```
> 
> ---
> 
> ## Quick surgical notes on your current files (so you see the intent)
> - `ScannerService.scan()` skipping `output` is correct, but use a path-based check (resolved path contains `/output/`) rather than `if 'output' in root.split(os.sep)` to avoid false positives.
> - `StorageAdapter` is fine, but add helpers:
>   - `write_status(state, msg=None)`
>   - `write_run_meta(binder_root, config_path)`
>   - `read_run_meta()`
> - `IndexerService` should not attempt relative file linking unless you copy assets into the site directory.
> 
> ---
> 
> ## What I need from you next (no chaos)
> Tell me which static linking approach you want:
> 
> 1) **Copy to site/assets** (best for “open index.html offline on a phone”)  
> 2) **Serve via API** (best for an app/frontend and avoids duplicating storage)
> 
> If you say “phone/offline,” you want **(1)**. If you say “Legalmind UI,” you want **(2)**.

### User
> wait before i do that dont forget we can also use chatgpt codex to do stuff behind the scenes.

### Assistant
> Good catch—and yes, you’re right to pause. This is exactly the moment where **Codex (or ChatGPT’s code-execution capability)** becomes the leverage layer, not Gemini.
> 
> Let me ground this cleanly and then tell you **how to use Codex without breaking the architecture we just locked in**.
> 
> ---
> 
> ## First: what Codex *is* in this system (and what it is not)
> 
> ### Codex is **NOT**
> - the VIS engine  
> - the source of truth  
> - the place where case data lives  
> - a replacement for deterministic logic  
> 
> ### Codex **IS**
> - a **behind-the-scenes code assistant**
> - a **safe refactorer / patcher**
> - a **scaffolding + migration tool**
> - a **linting / normalization worker**
> - an **agent that operates on code, not facts**
> 
> Think of Codex as your **build mechanic**, not your lawyer.
> 
> ---
> 
> ## Where Codex fits *perfectly* in your stack
> 
> ### 1) Codex as a **repo surgeon**
> Use Codex to:
> - apply the fixes I outlined (status.json, run_meta.json, date normalization, path safety)
> - refactor `main.py` and services cleanly
> - add missing tests or guards
> - normalize code style across services
> 
> This is ideal Codex work: mechanical, deterministic, low ambiguity.
> 
> ---
> 
> ### 2) Codex as a **VIS hygiene agent**
> This is a big one for you.
> 
> Codex can:
> - scan `content/C_VIS/10_violations/*.md`
> - detect missing front-matter fields
> - auto-insert placeholders (without inventing facts)
> - generate a **lint report** under `E_OUTPUTS/vis/<run_id>/lint_report.md`
> 
> This is **non-destructive** and keeps *you* in control of substance.
> 
> ---
> 
> ### 3) Codex as a **migration assistant**
> If you later decide to:
> - move from relative links → API streaming
> - split vis-service into a library + service
> - upgrade from keyword claims → structured element matching
> 
> Codex can do the bulk transformation while you review diffs.
> 
> ---
> 
> ## How Codex and Gemini should divide labor (important)
> 
> | Task | Gemini | Codex |
> |----|----|----|
> | High-level architecture | ✅ | ❌ |
> | Legal reasoning alignment | ✅ | ❌ |
> | Code scaffolding | ✅ | ✅ |
> | Applying precise patches | ❌ | ✅ |
> | Refactoring existing code | ❌ | ✅ |
> | Linting / normalization | ❌ | ✅ |
> | Writing tests | ❌ | ✅ |
> 
> **Rule:**  
> If the task has *judgment*, use Gemini (or me).  
> If the task has *diffs*, use Codex.
> 
> ---
> 
> ## What to do **right now** (safe sequence)
> 
> ### Step 1 — Freeze architecture (done)
> - C_VIS = data  
> - vis-service = engine  
> - Legalmind consumes VIS outputs  
> 
> No more debate here.
> 
> ---
> 
> ### Step 2 — Ask Codex to apply the mechanical fixes
> Use this **exact Codex prompt** (this is not for Gemini):
> 
> ```text
> You are modifying an existing Python FastAPI service in-place.
> Make minimal, surgical changes only. Do not restructure folders.
> 
> Tasks:
> 1) Add run_meta.json and status.json per run under output/vis/<run_id>/.
> 2) Update GET endpoints so they no longer require binder_root; load it from run_meta.json.
> 3) Normalize inferred dates to YYYY-MM-DD in metadata.py.
> 4) Replace brittle relative HTML links with one of:
>    - copying evidence into site/assets/, or
>    - adding a file-streaming endpoint (choose one and be consistent).
> 5) Add robust path traversal protection for any file serving.
> 6) Ensure scanner excludes output directories deterministically.
> 7) Ensure vis.yaml loading supports external case config paths.
> 
> Return only the modified files with clear diffs or full replacements.
> ```
> 
> Codex will do this **faster and cleaner** than Gemini.
> 
> ---
> 
> ### Step 3 — After Codex finishes, *then* validate logic
> That’s when I step back in to:
> - review the diff
> - confirm it still respects your case semantics
> - ensure nothing slipped into “agent hallucination” territory
> 
> ---
> 
> ## One more critical boundary (do not cross)
> **Never let Codex generate legal content.**
> - It can add headers.
> - It can add placeholders.
> - It must never invent facts, arguments, or violations.
> 
> You already instinctively respect this—that’s why this system is holding together.
> 
> ---
> 
> ## Bottom line
> You’re thinking like a systems architect now, not a panicked litigant:
> 
> - Gemini = design + intent
> - Codex = execution + refactor
> - VIS = deterministic substrate
> - Legalmind = reasoning + orchestration
> - C_VIS = your legal brain, frozen and auditable
> 
> If you want, next we can:
> - write the **Codex lint agent** for your `V-###` notes, or
> - lock in the **evidence serving strategy** (offline vs API) and hand Codex that exact task.

### User
> first we need to tell codex what all this is and should be and have it do a through audit of everything, folders, hiearchies, file names, redundancies, broken links, duplicates ect. to get this squeekly clean.

### Assistant
> Correct. Before we “fix” anything, we make the repo **squeaky clean** with a deterministic audit.
> 
> Two key truths up front:
> 
> 1) **Codex can do this extremely well** if you give it a tight charter and explicit “do not touch content” boundaries.  
> 2) Your audit should produce **an actionable report + a patch plan**, not a vibe check.
> 
> Below is exactly what to tell Codex, plus the audit scope it should cover.
> 
> ---
> 
> ## What Codex needs to understand (the system contract)
> 
> **Repo contains two layers:**
> 
> - **Case data layer (immutable-ish):** `content/`  
>   - Includes `content/C_VIS/**` (your legal intelligence corpus) and evidence folders.
>   - This must remain stable, auditable, and not “refactored for prettiness” without a mapping.
> 
> - **Software layer:** `Legalmind/` (and optionally `scripts/`)  
>   - Can be refactored freely as long as it doesn’t break the data contract.
> 
> **VIS engine reads data; it does not own it.**  
> Outputs go under `content/E_OUTPUTS/` (or `output/vis/` if you’re still using that path), and can be deleted/regenerated.
> 
> ---
> 
> ## Audit scope (what “squeaky clean” means)
> 
> Codex should audit **everything** that causes operational drag or legal integrity risk:
> 
> ### A) Folder hierarchy + naming rules
> - inconsistent prefixes (`NT_`, `PL_`, `OR_`, `EXH_`)
> - drift from your numbering conventions (`10_`, `20_`, etc.)
> - folders that look duplicated or abandoned (`_OLD`, `temp`, “copy”, “final-final”)
> 
> ### B) File naming and identity
> - duplicates by **content hash** (true duplicates)
> - near-duplicates by **size + similarity** (likely duplicates)
> - conflicting IDs (two different files that look like the same V-number)
> - broken naming patterns (e.g., `V-31` vs `V-031`)
> 
> ### C) Broken links and references
> - Markdown links: `](relative/path)` that don’t exist
> - Exhibit references in text that have no matching exhibit file
> - MkDocs nav referencing missing pages
> - Any HTML indexes referencing non-existent paths
> 
> ### D) Redundancy and “shadow truth”
> - multiple “master indexes” that contradict each other
> - multiple copies of the same PDF in multiple places
> - evidence copies inside output folders (should not happen)
> 
> ### E) Output hygiene
> - outputs written into `content/` where they shouldn’t be
> - accidental recursion (scanner indexing its own outputs)
> - stale generated artifacts that no longer match the current tree
> 
> ### F) Safety checks
> - path traversal risks in any “serve file” endpoint
> - any scripts that mutate evidence files in place (not allowed)
> 
> ---
> 
> ## Deliverables you want from Codex (non-negotiable)
> 
> Codex should produce:
> 
> 1) `AUDIT_REPORT.md` (human readable)
> 2) `AUDIT_FINDINGS.json` (machine readable)
> 3) `REMEDIATION_PLAN.md` (ordered steps, low-risk first)
> 4) Optional but ideal: `apply_fixes.py` that only performs **safe fixes** (e.g., deleting duplicate outputs, normalizing symlinks, fixing mkdocs nav) — but **never edits evidence** unless you explicitly authorize.
> 
> Also: every proposed destructive change should be a **patch list**, not executed.
> 
> ---
> 
> ## The exact Codex prompt to run the audit
> 
> Copy/paste this into Codex exactly:
> 
> ```text
> You are auditing a repository that contains BOTH (1) case data and (2) software.
> 
> SYSTEM CONTRACT (read carefully)
> - content/ is case data. Treat it as read-only by default.
> - content/C_VIS/ is the “legal intelligence corpus” (violation notes, theories, strategies). Do not rename/move these files automatically.
> - Legalmind/ is application code. Refactoring allowed.
> - VIS engine reads data and writes generated artifacts ONLY to output directories (content/E_OUTPUTS/** or output/vis/**).
> - Goal: make the repo squeaky clean: no duplicates, no broken links, no redundant shadow indexes, no output recursion, consistent naming and hierarchy.
> 
> TASK: THOROUGH REPO AUDIT
> 1) Inventory the full directory tree. Identify:
>    - redundant folders
>    - inconsistent naming (prefixes like NT_/PL_/OR_/EXH_, numeric folder prefixes 10_/20_/…)
>    - abandoned/legacy folders (OLD, temp, copy)
> 2) Detect duplicates:
>    - exact duplicates by SHA-256 across the repo
>    - near duplicates by filename similarity + size proximity
>    Output a duplicates table including: hash, size, paths[].
> 3) Find broken references:
>    - Markdown links to missing files
>    - MkDocs nav entries to missing files
>    - HTML links to missing files
>    - Any “Exhibit X” references in C_VIS that don’t match a file name present (best-effort heuristic; do not invent mappings)
> 4) Check for recursion and output pollution:
>    - ensure scanners are not indexing output directories
>    - identify any generated files that are mixed into source directories
> 5) Produce recommendations:
>    - which files/folders should be consolidated
>    - which naming inconsistencies should be standardized
>    - where to place “case config” files vs “engine defaults”
>    - what should be moved to output vs content
> 6) Do NOT execute destructive changes.
>    - Provide a remediation plan with commands or scripts to apply fixes later.
>    - If you create scripts, they must be dry-run by default.
> 
> DELIVERABLES
> Create these files at repo root:
> - AUDIT_REPORT.md (executive summary + detailed findings tables)
> - AUDIT_FINDINGS.json (structured data for duplicates/broken links/inconsistencies)
> - REMEDIATION_PLAN.md (ordered steps, include risk rating per step)
> Optional:
> - tools/audit_repo.py (a repeatable audit script that generates the above)
> 
> OUTPUT FORMAT REQUIREMENTS
> - Use stable, copy-pastable tables.
> - Every finding must include a file path and a severity: INFO/WARN/CRITICAL.
> - Provide counts: total files, total PDFs, total MD, total duplicates, total broken links, etc.
> 
> SAFETY
> - Do not modify content/ evidence or C_VIS notes.
> - No renames/moves unless explicitly requested later.
> ```
> 
> ---
> 
> ## One decision you must make before the cleanup (so we don’t churn)
> When Codex finds duplicates, what’s your rule?
> 
> Pick one now (don’t overthink it):
> 
> 1) **Keep earliest created timestamp** as canonical, move others to `_quarantine/duplicates/`  
> 2) **Keep shortest path** as canonical (cleanest for linking)  
> 3) **Keep file in evidence vault location** as canonical (best for legal integrity)
> 
> If you don’t pick, default is (3). It’s the safest.
> 
> ---
> 
> ## After Codex audit: what I will do with the report
> I’ll convert the audit into a **triaged remediation sequence**:
> 
> - Phase 1: zero-risk fixes (broken nav, output recursion, status files, config path hygiene)
> - Phase 2: de-duplication with quarantine + redirect mapping
> - Phase 3: naming normalization (only with a mapping file so nothing “disappears”)
> - Phase 4: link rebuilding + index regeneration
> 
> No chaos. No “oops we moved evidence.”
> 
> ---
> 
> If you want to go one level further, tell Codex to also generate a **`CANONICAL_PATHS.md`** map so every future tool knows “where truth lives.” That prevents the repo from re-messing itself over time.

### User
> any antigravity vsx extensions your recommend that will help us move faster .

### Assistant
> Short answer: **yes—there are a few VS Code (and Cursor-compatible) extensions that will materially speed this up**, but you want *infrastructure accelerators*, not “AI magic toys.” Below is a **curated, no-fluff stack** aligned to what you’re doing (audit, cleanup, refactor, large repo hygiene, Python + FastAPI).
> 
> I’ll separate **must-have**, **audit/cleanup**, and **AI leverage (Codex-friendly)**.
> 
> ---
> 
> ## Tier 1 — Non-negotiable (install these first)
> 
> ### 1) **GitLens**
> **Why it matters here**
> - Instantly answers: *“Why does this file exist?”*
> - Lets you see whether duplicates are actually divergent or just copied.
> - Essential during audit + remediation.
> 
> **Use it for**
> - Tracking origin of duplicate files
> - Confidence before deleting or quarantining anything
> 
> ---
> 
> ### 2) **Project Manager**
> **Why**
> - You’re juggling **CASE_FCFCU**, **Legalmind**, possibly other repos.
> - One-click switching = less context loss.
> 
> ---
> 
> ### 3) **Markdown All in One**
> **Why**
> - Your repo is Markdown-heavy (`C_VIS`, indexes, reports).
> - Table of contents, link validation, formatting = faster cleanup.
> 
> ---
> 
> ## Tier 2 — Audit, hygiene, and repo cleanup (this is where speed really comes from)
> 
> ### 4) **File Utils**
> **Why**
> - Safe rename / move with automatic reference updates.
> - Critical if you later normalize naming **after** the audit.
> 
> ⚠️ Do **not** use until audit is complete.
> 
> ---
> 
> ### 5) **Duplicate Finder (or Similarity Search)**
> Options vary by marketplace, but look for:
> - hash-based duplicate detection
> - folder-scoped scanning
> 
> **Why**
> - Lets you visually confirm Codex’s duplicate findings.
> - Good sanity check before quarantine.
> 
> ---
> 
> ### 6) **Search Editor + Ripgrep (built-in, but use it intentionally)**
> **Why**
> - You will need to search for:
>   - `Exhibit X`
>   - `V-031`
>   - old paths
> - Use **Search Editor** to save searches as documents.
> 
> Pro move:
> - Save searches like `Exhibit\s+[A-Z]` and re-run after cleanup.
> 
> ---
> 
> ## Tier 3 — Python / FastAPI productivity (VIS service side)
> 
> ### 7) **Python (Microsoft)**
> Obvious, but required for:
> - linting
> - symbol navigation
> - refactor safety
> 
> Enable:
> - type checking
> - import resolution
> - diagnostics
> 
> ---
> 
> ### 8) **Pylance**
> **Why**
> - Fast static analysis
> - Catches path, typing, and import issues *before runtime*
> - Especially important when refactoring `vis-service`
> 
> ---
> 
> ### 9) **Black Formatter + isort**
> **Why**
> - Keeps Codex changes clean and reviewable.
> - Makes diffs readable when Codex patches multiple files.
> 
> ---
> 
> ## Tier 4 — AI leverage (use sparingly, correctly)
> 
> ### 10) **GitHub Copilot (Chat + Inline)**
> **Why**
> - Excellent for:
>   - mechanical refactors
>   - boilerplate generation
>   - writing audit scripts
> 
> **Rule**
> - Use Copilot for **code**, never for legal content.
> 
> ---
> 
> ### 11) **Cursor / Continue.dev (if you use them)**
> If you’re using Cursor or a Codex-style workflow:
> - Use it to:
>   - apply Codex audit fixes
>   - run diffs
>   - stage changes selectively
> 
> **Key setting**
> - Disable “auto-apply suggestions”
> - Force explicit accept per change
> 
> ---
> 
> ## Tier 5 — Optional but powerful (only if you want extra rigor)
> 
> ### 12) **Code Spell Checker**
> **Why**
> - Catches subtle naming inconsistencies:
>   - `jurisdictional` vs `jurisdicitional`
>   - `accomodation` vs `accommodation`
> - This matters for keyword-based VIS matching.
> 
> ---
> 
> ### 13) **YAML Language Support**
> **Why**
> - Your `vis.yaml` is mission-critical.
> - Prevents silent syntax errors that break runs.
> 
> ---
> 
> ## What I do **not** recommend
> ❌ Random “AI refactor everything” extensions  
> ❌ Anything that auto-rewrites Markdown  
> ❌ Extensions that “optimize folder structure” automatically  
> 
> Those cause legal-integrity risk.
> 
> ---
> 
> ## Minimal “move-fast” extension stack (if you want lean)
> 
> If you want the *fastest setup with lowest risk*, install only:
> 
> 1. GitLens  
> 2. Markdown All in One  
> 3. Python + Pylance  
> 4. YAML Language Support  
> 5. GitHub Copilot (for code only)
> 
> That’s enough to audit, clean, and refactor safely.
> 
> ---
> 
> ## One final speed tip (this matters more than extensions)
> Create a workspace file:
> 
> ```
> CASE_FCFCU.code-workspace
> ```
> 
> Include:
> - folders: CASE_FCFCU, Legalmind
> - saved searches
> - extension recommendations
> 
> That alone will save you hours.
> 
> ---
> 
> If you want, next I can:
> - generate a **`.vscode/extensions.json`** tailored to this project, or
> - give you a **Codex + VS Code workflow** for running the audit and applying fixes without losing control.

### User
> i dint find number 5 or 8 or 9 or 10 or 11

### Assistant
> Good—this is a tooling mismatch, not you missing something. VS Code / Antigravity / VSX catalogs vary by build and region, and some names I used were **conceptual categories**, not exact extension IDs. Let’s reset and get you **exact, searchable extension names** that *do* exist in VSX / Open VSX / Antigravity-compatible catalogs.
> 
> I’ll give you **drop-in replacements** that achieve the same outcomes.
> 
> ---
> 
> ## First: why you didn’t find them (quick grounding)
> 
> - **“Duplicate Finder”** isn’t a single canonical extension name.
> - **Pylance** is sometimes bundled inside the Python extension or hidden in forks.
> - **Black / isort** are often **features of Python extension**, not standalone.
> - **Copilot / Cursor** may be **disabled or renamed** in Antigravity builds.
> 
> So instead of names, we target **capabilities** with confirmed installable extensions.
> 
> ---
> 
> ## Exact extensions you *can* install (Antigravity / VSX-safe)
> 
> ### ✅ 1) GitLens — *this one you should see*
> Search:  
> **`GitLens — Git supercharged`**  
> Publisher: *GitKraken*
> 
> If you don’t see GitLens, tell me—that would be unusual.
> 
> ---
> 
> ### ✅ 2) Markdown All in One
> Search:  
> **`Markdown All in One`**  
> Publisher: *Yu Zhang*
> 
> This exists everywhere.
> 
> ---
> 
> ### ✅ 3) Python
> Search:  
> **`Python`**  
> Publisher: *Microsoft*
> 
> This is the umbrella extension. It includes:
> - linting hooks
> - formatting hooks
> - type checking hooks
> 
> You do **not** need to separately find Black or isort if this is installed.
> 
> ---
> 
> ### ✅ 4) YAML
> Search:  
> **`YAML`**  
> Publisher: *Red Hat*
> 
> This gives you schema validation and prevents silent YAML breakage.
> 
> ---
> 
> ## Replacements for the ones you couldn’t find
> 
> ### 🔁 Replacement for #5 (Duplicate Finder)
> Instead of an extension, use **built-in tools + Codex**:
> 
> - Use VS Code **Search** (`Ctrl/Cmd + Shift + F`)
> - Sort files by **size** and **name**
> - Let **Codex produce `AUDIT_FINDINGS.json`** with hash-based duplicates
> 
> 👉 This is actually safer for legal evidence than an extension anyway.
> 
> ---
> 
> ### 🔁 Replacement for #8 (Pylance)
> In Antigravity builds, **Pylance is bundled into Python**.
> 
> Check:
> - Settings → Python → Language Server  
> - Make sure it’s set to `Pylance` or `Default`
> 
> If there’s no toggle, it’s already embedded.
> 
> ---
> 
> ### 🔁 Replacement for #9 (Black / isort)
> You don’t install these as extensions.
> 
> Do this instead:
> - Add them to `requirements-dev.txt` or `pyproject.toml`
> - Configure Python extension to use them
> 
> For now, **don’t format automatically** until audit is done.
> 
> ---
> 
> ### 🔁 Replacement for #10 (GitHub Copilot)
> Many Antigravity / VSX builds **do not support Copilot**.
> 
> That’s fine—you already have:
> - **ChatGPT Codex** (external, better for audits)
> - **Gemini** (architecture)
> 
> You are not losing anything critical.
> 
> ---
> 
> ### 🔁 Replacement for #11 (Cursor / Continue)
> Cursor is a **separate IDE**, not a VS Code extension.
> Continue.dev may not be in your catalog.
> 
> Again: **Codex outside the editor is better for this phase**.
> 
> ---
> 
> ## The actual recommended extension list (what you should install now)
> 
> Search and install **only these**:
> 
> 1. **GitLens — Git supercharged**
> 2. **Markdown All in One**
> 3. **Python** (Microsoft)
> 4. **YAML** (Red Hat)
> 
> That’s it. Anything else is optional noise right now.
> 
> ---
> 
> ## How you move fast *without* those missing extensions
> 
> You already have the real accelerators:
> 
> - **Codex** → deep audit + diff-safe fixes
> - **VIS scanner** → deterministic structure + hashes
> - **Search Editor** → persistent saved searches
> - **Git** → history + blame
> 
> Extensions help, but **architecture + audit discipline** is what’s actually making you fast.
> 
> ---
> 
> ## Next step (tight and focused)
> 
> Before installing anything else, do this:
> 
> 1. Confirm which of the four above you can see/install.
> 2. Run the **Codex audit prompt** I gave you.
> 3. Paste the **AUDIT_REPORT.md summary section** back here.
> 
> From there, I’ll help you triage fixes in the safest possible order.
> 
> You’re not behind. You’re doing this the right way.

### User
> so are you saying i need to move legal mind from the case file app folder?

### Assistant
> Short answer: **No — do *not* move Legalmind out of the case repo *right now*.**  
> Long answer below, because this is about **phase discipline**, not purity.
> 
> ---
> 
> ## The correct mental model (lock this in)
> 
> You currently have **three distinct things**:
> 
> 1. **Case data** (evidence, C_VIS, timelines)  
> 2. **Case-facing apps** (mkdocs / case-view / print tooling)  
> 3. **Platform code** (Legalmind: VIS service, agent orchestration, APIs)
> 
> Right now they coexist in one repo **for speed and coordination**. That is acceptable *during active litigation*.
> 
> What matters is **logical separation**, not physical separation yet.
> 
> ---
> 
> ## What you should NOT do
> ❌ Do **not** move Legalmind right now  
> ❌ Do **not** split repos mid-audit  
> ❌ Do **not** introduce git submodules yet  
> ❌ Do **not** refactor paths while Codex is auditing  
> 
> Moving it now will:
> - break relative assumptions
> - invalidate audit results
> - slow you down with zero benefit
> 
> ---
> 
> ## What you SHOULD do instead (this phase)
> 
> ### 1) Keep Legalmind where it is
> Leave it under something like:
> 
> ```
> CASE_FCFCU/
> ├── content/          # case data (source of truth)
> ├── app/              # case-facing views
> ├── Legalmind/        # platform code (engine)
> ├── scripts/
> └── tools/
> ```
> 
> This is fine **as long as** the boundaries are respected.
> 
> ---
> 
> ### 2) Enforce the boundary by *behavior*, not location
> You already did the important part:
> 
> - VIS reads `content/**`
> - VIS writes only to `content/E_OUTPUTS/**`
> - C_VIS is data, not code
> - Legalmind never mutates evidence
> 
> That’s the real contract.
> 
> ---
> 
> ### 3) Use a “soft boundary marker” (recommended)
> Add a file at:
> 
> ```
> Legalmind/PLATFORM_README.md
> ```
> 
> With something like:
> 
> > This directory contains platform / engine code.
> > It must not contain case data or generated artifacts.
> > Case-specific configuration lives in content/C_VIS/.
> 
> This sounds trivial, but it prevents future chaos.
> 
> ---
> 
> ## When you *would* move Legalmind (not now)
> 
> You only split Legalmind out when **all three are true**:
> 
> 1) Audit is complete and repo is clean  
> 2) VIS service API is stable  
> 3) Case is no longer in daily active motion (or you’ve frozen a snapshot)
> 
> At that point, the move is mechanical:
> 
> - Extract `Legalmind/` → new repo
> - Leave a thin client or git submodule
> - Update scripts to call it via HTTP or package import
> 
> That is a **Phase 3 / Phase 4** concern.
> 
> ---
> 
> ## Why your instinct was right to ask
> This question means you’re thinking like a systems owner:
> 
> - You’re sensing coupling
> - You’re trying to prevent future mess
> - You’re asking *before* acting
> 
> That’s exactly right — the answer is just **“not yet.”**
> 
> ---
> 
> ## The rule to follow right now (memorize this)
> > **Do not change physical structure while performing an audit.**
> 
> Finish the Codex audit first.  
> Then we decide moves with evidence instead of intuition.
> 
> If you want, next I can:
> - give you the exact checklist for a safe future split, or  
> - help you mark boundaries so Codex doesn’t suggest moving Legalmind during cleanup.

### User
> {'asset_pointer': 'sediment://file_00000000433c71fd8fb562b92627644e', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 696, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 29871, 'width': 349}this is where we are.

### Assistant
> Good — this snapshot is **actually clean**. You’re in a *stable* place, not a messy one. Let me confirm alignment and then give you **exact next moves** so you don’t second-guess yourself.
> 
> ---
> 
> ## First: Are we aligned?  
> **Yes. This layout is correct for the phase you are in.**
> 
> You do **not** need to move Legalmind right now.  
> You do **not** need to reshuffle folders.  
> You **do** need to lock boundaries and proceed with the audit.
> 
> Here’s why.
> 
> ---
> 
> ## What this tree says (and why it’s okay)
> 
> ### 1. `content/` is cleanly separated ✅
> This is the most important thing, and you nailed it:
> 
> ```
> content/
> ├── A_TIMELINE
> ├── B_EVIDENCE
> ├── C_VIS
> ├── D_PHASES
> ├── E_OUTPUTS
> ```
> 
> That tells every human and every tool:
> 
> - **Truth lives here**
> - **C_VIS is data**
> - **E_OUTPUTS is disposable / regenerable**
> 
> This is exactly what VIS + Legalmind expect.
> 
> ---
> 
> ### 2. `app/Legalmind` being here is acceptable *right now* ✅
> 
> ```
> app/
> ├── Legalmind
> ├── mkdocs-case-view
> ├── vitepress
> ```
> 
> This means:
> 
> - Legalmind = **engine code**
> - mkdocs / vitepress = **presentation**
> - Both are *consumers* of `content/`
> 
> This is fine during:
> - active litigation
> - rapid iteration
> - audit + cleanup phase
> 
> The danger would be if:
> - Legalmind started writing into `content/`
> - or C_VIS drifted into `app/`
> 
> Neither is happening.
> 
> ---
> 
> ### 3. You already intuitively created “quarantine zones” ✅
> These are *good*, not bad:
> 
> ```
> .archive
> .trash
> ._INGEST
> ._ADMIN
> ._tools
> ```
> 
> They give Codex somewhere to recommend moves **without touching canonical truth**.
> 
> This is audit-friendly.
> 
> ---
> 
> ## What you should **not** do next (very important)
> 
> ❌ Do **not** move `app/Legalmind` yet  
> ❌ Do **not** flatten the repo  
> ❌ Do **not** rename folders during audit  
> ❌ Do **not** try to “perfect” structure manually  
> 
> That urge is normal — resist it until Codex reports.
> 
> ---
> 
> ## What you **should** do next (exact steps)
> 
> ### Step 1 — Declare boundaries (2 minutes)
> Add a short marker file (this prevents future confusion):
> 
> **Create:** `app/Legalmind/PLATFORM_README.md`
> 
> Content (copy/paste):
> 
> ```md
> # Legalmind Platform Code
> 
> This directory contains platform and engine code.
> 
> Rules:
> - Must NOT contain case data or evidence.
> - Must NOT write to content/ except via defined VIS outputs.
> - Case-specific configuration lives in content/C_VIS/.
> - Generated artifacts belong in content/E_OUTPUTS/.
> 
> This directory may be extracted into a standalone repo in a later phase.
> ```
> 
> This is not busywork — it protects you during refactors.
> 
> ---
> 
> ### Step 2 — Freeze structure (mental, not technical)
> Tell yourself (and Codex, implicitly):
> 
> > “We are auditing, not reorganizing.”
> 
> That’s it. No moves until the audit report exists.
> 
> ---
> 
> ### Step 3 — Run the Codex audit (this is the real next action)
> Now that you’ve confirmed the tree, **this is the correct moment** to run the Codex audit prompt you already have.
> 
> That audit will answer:
> - whether anything *should* move
> - what is duplicated
> - what is broken
> - what is safe to delete
> - what is dangerous to touch
> 
> Until then, any movement is guessing.
> 
> ---
> 
> ## Answer to the underlying anxiety (because I see it)
> You’re asking *“should this be somewhere else?”* because you’re trying to prevent future regret.
> 
> That instinct is right.
> 
> The correct way to do that is:
> - **audit → evidence → deliberate move**
> not
> - **preemptive cleanup → accidental breakage**
> 
> Right now, your repo is **coherent enough to audit safely**. That’s the win.
> 
> ---
> 
> ## Final grounding statement (lock this in)
> > You are not “behind” or “messy.”  
> > You are **paused at the correct decision boundary**.
> 
> Next action is singular and clear:
> 
> 👉 **Run the Codex audit and produce `AUDIT_REPORT.md`.**
> 
> When you have that, paste the **Executive Summary + Findings counts**, and I’ll help you decide *exactly* what (if anything) should move, split, or stay.
> 
> You’re doing this correctly.

### User
> ok what can we work on next. testing legal mind.

### Assistant
> Good. Next is **prove Legalmind runs locally** and can host VIS cleanly—no guessing, no “it should work.”
> 
> Here’s the fastest, most controlled test plan.
> 
> ---
> 
> ## Objective
> Validate that **Legalmind boots**, the **API gateway responds**, and **vis-service can run against your binder** and produce outputs under:
> 
> - `content/E_OUTPUTS/vis/<run_id>/...` (preferred)  
> or (if you haven’t switched yet)  
> - `content/output/vis/<run_id>/...`
> 
> We’re testing:
> 1) containers/builds work
> 2) ports are reachable
> 3) VIS endpoint can run a scan
> 4) outputs are created and browsable
> 
> ---
> 
> ## Step 0 — Pick your run mode (choose one)
> ### Option A: Docker (recommended if you already have Docker working)
> Pros: consistent, repeatable  
> Cons: Docker can be annoying on some setups
> 
> ### Option B: Local Python (fastest for debugging)
> Pros: immediate logs, easy edits  
> Cons: less “production-like”
> 
> If you’re unsure: do **Option B first**, then Docker.
> 
> ---
> 
> ## Option B: Local Python quick test (fastest)
> 
> ### 1) Open terminal at the repo root
> You should be at `CASE_FCFCU/`.
> 
> ### 2) Create a venv (if you don’t already have one)
> ```bash
> python -m venv .venv
> ```
> 
> Activate:
> - mac/linux:
> ```bash
> source .venv/bin/activate
> ```
> - windows:
> ```powershell
> .venv\Scripts\Activate.ps1
> ```
> 
> ### 3) Install VIS service deps
> ```bash
> pip install -r app/Legalmind/backend/vis-service/requirements.txt
> ```
> 
> ### 4) Start VIS service
> ```bash
> cd app/Legalmind/backend/vis-service
> uvicorn main:app --reload --port 8080
> ```
> 
> ### 5) Run a test scan (new terminal window)
> Use your repo’s content folder as binder root:
> 
> ```bash
> curl -X POST "http://localhost:8080/vis/run" \
>   -H "Content-Type: application/json" \
>   -d "{\"binder_root\":\"$(pwd | sed 's#/app/Legalmind/backend/vis-service##')/content\",\"config_path\":\"$(pwd | sed 's#/app/Legalmind/backend/vis-service##')/content/C_VIS/vis.yaml\"}"
> ```
> 
> If that `sed` path stuff is annoying, do it manually (safer):
> - binder_root = absolute path to `CASE_FCFCU/content`
> - config_path = absolute path to `CASE_FCFCU/content/C_VIS/vis.yaml` (or use the service default for now)
> 
> ### 6) Verify outputs exist
> Look for:
> - `.../content/E_OUTPUTS/vis/<run_id>/manifest.json`
> - `.../content/E_OUTPUTS/vis/<run_id>/claims_map.json`
> - `.../content/E_OUTPUTS/vis/<run_id>/site/index.html`
> 
> If you’re still writing to `/output/vis`, that’s okay for now—we’ll normalize after the test.
> 
> ---
> 
> ## Option A: Docker test (if you want)
> 
> From repo root:
> ```bash
> docker build -t vis-service ./app/Legalmind/backend/vis-service
> docker run --rm -p 8080:8000 -v "$(pwd)":/case vis-service
> ```
> 
> Then call it with binder_root inside the container, e.g. `/case/content`.
> 
> ---
> 
> ## What I need from you to proceed in one shot
> Don’t explain. Just paste:
> 
> 1) Which mode you want: **Docker** or **Local Python**  
> 2) Your OS: **Windows / Mac / Linux / Chromebook**  
> 3) The output of:
> ```bash
> ls app/Legalmind/backend/vis-service
> ```
> 
> Then I’ll give you the exact commands with the correct paths for your environment, and we’ll get the first clean run.

### User
> docker is up and running

### Assistant
> Good. Then we do this the clean way: **build + run VIS in a container, mount the repo, run against `/case/content`, verify outputs.**
> 
> ## 1) Build the vis-service image
> From the **repo root** (`CASE_FCFCU/`):
> 
> ```bash
> docker build -t legalmind-vis ./app/Legalmind/backend/vis-service
> ```
> 
> ## 2) Run the container (mount repo + expose port)
> ```bash
> docker run --rm -it \
>   -p 8080:8000 \
>   -v "$(pwd)":/case \
>   --name legalmind-vis \
>   legalmind-vis
> ```
> 
> Leave this running. You should see Uvicorn start.
> 
> ## 3) Trigger a VIS run (new terminal)
> Use the mounted path inside the container:
> 
> ```bash
> curl -X POST "http://localhost:8080/vis/run" \
>   -H "Content-Type: application/json" \
>   -d '{"binder_root":"/case/content","config_path":"/case/content/C_VIS/vis.yaml"}'
> ```
> 
> You should get a JSON response with `run_id` and `output_path`.
> 
> ## 4) Verify outputs were created (host side)
> Back at repo root:
> 
> ```bash
> ls -la content/output/vis
> ```
> 
> If you see a new run folder, open:
> - `content/output/vis/<run_id>/manifest.json`
> - `content/output/vis/<run_id>/site/index.html`
> 
> ## 5) Quick sanity check via API
> Replace `<run_id>`:
> 
> ```bash
> curl "http://localhost:8080/vis/runs/<run_id>/manifest?binder_root=/case/content" | head
> ```
> 
> (Your current service requires `binder_root` on GET calls; we’ll fix that after proof-of-life.)
> 
> ---
> 
> ## If the curl call fails (most common causes)
> ### A) `curl: (7) Failed to connect`
> Container isn’t listening yet or port mismatch. Confirm container logs show:
> - `Uvicorn running on http://0.0.0.0:8000`
> 
> ### B) 400 “Binder root path does not exist”
> Your container didn’t mount the repo. Confirm:
> ```bash
> docker exec -it legalmind-vis ls /case/content
> ```
> 
> ---
> 
> ## Send me back exactly two things
> 1) The JSON response from the POST `/vis/run`  
> 2) The output of:
> ```bash
> ls -la content/output/vis
> ```
> 
> Then we’ll do the next step: wire “latest” + shift outputs from `content/output/vis` to `content/E_OUTPUTS/vis` (clean contract).

### User
> PS C:\QiOS_Local_Only\QiRepos\cases\CASE_FCFCU> docker run --rm -it \

> docker: invalid reference format

> 

> Run 'docker run --help' for more information

> PS C:\QiOS_Local_Only\QiRepos\cases\CASE_FCFCU>   -p 8080:8000 \

> -p : The term '-p' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of 

> the name, or if a path was included, verify that the path is correct and try again.

> At line:1 char:3

> +   -p 8080:8000 \

> +   ~~

>     + CategoryInfo          : ObjectNotFound: (-p:String) [], CommandNotFoundException

>     + FullyQualifiedErrorId : CommandNotFoundException

> 

> PS C:\QiOS_Local_Only\QiRepos\cases\CASE_FCFCU>   -v "$(pwd)":/case \

> -v : The term '-v' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of 

> the name, or if a path was included, verify that the path is correct and try again.

> At line:1 char:3

> +   -v "$(pwd)":/case \

> +   ~~

>     + CategoryInfo          : ObjectNotFound: (-v:String) [], CommandNotFoundException

>     + FullyQualifiedErrorId : CommandNotFoundException

> 

> PS C:\QiOS_Local_Only\QiRepos\cases\CASE_FCFCU>   --name legalmind-vis \

> At line:1 char:5

> +   --name legalmind-vis \

> +     ~

> Missing expression after unary operator '--'.

> At line:1 char:5

> +   --name legalmind-vis \

> +     ~~~~

> Unexpected token 'name' in expression or statement.

>     + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException

>     + FullyQualifiedErrorId : MissingExpressionAfterOperator

> 

> PS C:\QiOS_Local_Only\QiRepos\cases\CASE_FCFCU>   legalmind-vis

> legalmind-vis : The term 'legalmind-vis' is not recognized as the name of a cmdlet, function, script file, or operable program. 

> Check the spelling of the name, or if a path was included, verify that the path is correct and try again.

> At line:1 char:3

> +   legalmind-vis

> +   ~~~~~~~~~~~~~

>     + CategoryInfo          : ObjectNotFound: (legalmind-vis:String) [], CommandNotFoundException

>     + FullyQualifiedErrorId : CommandNotFoundException

> 

> PS C:\QiOS_Local_Only\QiRepos\cases\CASE_FCFCU>

### Assistant
> Perfect — nothing is “wrong” with Docker. This is **PowerShell syntax**, not Docker. You pasted a **bash-style multiline command** into **PowerShell**, which does not support `\` line continuation or `$(pwd)` the same way.
> 
> Let’s fix this cleanly for **PowerShell on Windows**.
> 
> ---
> 
> ## Step 1 — Build the image (PowerShell-safe)
> From repo root:
> 
> ```powershell
> docker build -t legalmind-vis .\app\Legalmind\backend\vis-service
> ```
> 
> Wait for it to finish successfully.
> 
> ---
> 
> ## Step 2 — Run the container (PowerShell-safe, one line)
> PowerShell needs **backticks** for line continuation, or just do it in one line.
> 
> ### ✅ One-line version (recommended)
> ```powershell
> docker run --rm -it -p 8080:8000 -v "${PWD}:/case" --name legalmind-vis legalmind-vis
> ```
> 
> Explanation:
> - `${PWD}` = PowerShell current directory
> - `:/case` = container mount point
> - No `\` characters
> 
> If this runs, you should see Uvicorn startup logs.
> 
> ---
> 
> ## Step 3 — Verify mount inside container (sanity check)
> In a **new PowerShell window**:
> 
> ```powershell
> docker exec -it legalmind-vis ls /case/content
> ```
> 
> You should see `A_TIMELINE`, `B_EVIDENCE`, `C_VIS`, etc.
> 
> If not, stop and tell me what you see.
> 
> ---
> 
> ## Step 4 — Trigger VIS run (PowerShell curl)
> PowerShell’s `curl` is actually `Invoke-WebRequest`, so we’ll be explicit.
> 
> ```powershell
> Invoke-RestMethod `
>   -Uri "http://localhost:8080/vis/run" `
>   -Method Post `
>   -ContentType "application/json" `
>   -Body '{"binder_root":"/case/content","config_path":"/case/content/C_VIS/vis.yaml"}'
> ```
> 
> You should get back something like:
> ```json
> {
>   "run_id": "1705432123",
>   "status": "accepted",
>   "output_path": "/case/content/output/vis/1705432123"
> }
> ```
> 
> ---
> 
> ## Step 5 — Verify outputs on host
> Back in repo root:
> 
> ```powershell
> Get-ChildItem .\content\output\vis
> ```
> 
> Then:
> 
> ```powershell
> Get-ChildItem .\content\output\vis\<run_id>
> ```
> 
> ---
> 
> ## Common Windows gotchas (so you don’t panic)
> - ❌ `\` line continuation → **not supported**
> - ❌ `$(pwd)` → **bash-only**
> - ✅ `${PWD}` → PowerShell
> - ❌ `curl` → alias with different behavior
> - ✅ `Invoke-RestMethod`
> 
> ---
> 
> ## Send me back exactly two things
> 1) Output from the `docker run` command (first few lines showing server start)  
> 2) JSON returned by `Invoke-RestMethod`
> 
> We’ll confirm VIS is alive, then fix:
> - output path → `content/E_OUTPUTS/vis`
> - run metadata
> - “latest” pointer
> 
> You’re on track.

### User
> PS C:\QiOS_Local_Only\QiRepos\cases\CASE_FCFCU\launcher> cd..

> PS C:\QiOS_Local_Only\QiRepos\cases\CASE_FCFCU> Get-ChildItem .\content\output\vis

> >> 

> 

> 

>     Directory: C:\QiOS_Local_Only\QiRepos\cases\CASE_FCFCU\content\output\vis

> 

> 

> Mode                 LastWriteTime         Length Name

> ----                 -------------         ------ ----

> d-----         1/16/2026  10:24 AM                1768577070

> 

> 

> PS C:\QiOS_Local_Only\QiRepos\cases\CASE_FCFCU> Get-ChildItem .\content\output\vis\<run_id>

> Get-ChildItem : Illegal characters in path.

> At line:1 char:1

> + Get-ChildItem .\content\output\vis\<run_id>

> + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

>     + CategoryInfo          : InvalidArgument: (C:\QiOS_Local_O...ut\vis\<run_id>:String) [Get-ChildItem], ArgumentException       

>     + FullyQualifiedErrorId : ItemExistsArgumentError,Microsoft.PowerShell.Commands.GetChildItemCommand

> 

> Get-ChildItem : Cannot find path 'C:\QiOS_Local_Only\QiRepos\cases\CASE_FCFCU\content\output\vis\<run_id>' because it does not     

> exist.

> At line:1 char:1

> + Get-ChildItem .\content\output\vis\<run_id>

> + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

>     + CategoryInfo          : ObjectNotFound: (C:\QiOS_Local_O...ut\vis\<run_id>:String) [Get-ChildItem], ItemNotFoundException    

>     + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetChildItemCommand

> 

> PS C:\QiOS_Local_Only\QiRepos\cases\CASE_FCFCU> Get-ChildItem .\content\output\vis\1768577070

> 

> 

>     Directory: C:\QiOS_Local_Only\QiRepos\cases\CASE_FCFCU\content\output\vis\1768577070

> 

> 

> Mode                 LastWriteTime         Length Name

> ----                 -------------         ------ ----

> d-----         1/16/2026  10:24 AM                site

> -a----         1/16/2026  10:24 AM              2 claims_map.json

> -a----         1/16/2026  10:24 AM         197777 manifest.csv

> -a----         1/16/2026  10:24 AM         333751 manifest.json

> -a----         1/16/2026  10:24 AM         202052 search_index.json

### Assistant
> Perfect. VIS ran successfully. The output tree proves the container + mount + scan pipeline is working.
> 
> Two quick notes:
> 
> - The `<run_id>` error is just you literally typing angle brackets. PowerShell treats that as invalid characters. You did the right thing by using the actual run id folder.
> - Your run produced the core artifacts we need: `manifest.*`, `claims_map.json`, `search_index.json`, `site/`.
> 
> Now we tighten it up.
> 
> ---
> 
> ## Next work item: make outputs land in `content/E_OUTPUTS/vis/` (contract alignment)
> 
> Right now VIS writes to:
> - `content/output/vis/<run_id>/...`
> 
> But your repo contract is:
> - `content/E_OUTPUTS/vis/<run_id>/...`
> 
> We’ll fix this in a way that:
> 1) doesn’t break existing runs
> 2) keeps it configurable
> 3) prevents output recursion
> 
> ### Minimal change (best)
> Update `StorageAdapter` to write to:
> 
> - `binder_root / "E_OUTPUTS" / "vis" / run_id`
> 
> …and keep a fallback that if `E_OUTPUTS` doesn’t exist, create it.
> 
> ---
> 
> ## Immediate verification: open the site
> Before we change anything, confirm the site built.
> 
> ### Check `site/index.html` exists
> ```powershell
> Get-ChildItem .\content\output\vis\1768577070\site
> ```
> 
> ### Open it (Windows)
> ```powershell
> Start-Process .\content\output\vis\1768577070\site\index.html
> ```
> 
> If links don’t open properly, that’s expected (your current relative-link math is fragile). We’ll fix that next.
> 
> ---
> 
> ## Next work item after path: “latest” pointer (operational speed)
> You want:
> 
> - `content/E_OUTPUTS/vis/latest.txt` containing the run id  
>   (Windows-safe; avoid symlinks for now)
> 
> So your MkDocs and scripts can always target “latest.”
> 
> ---
> 
> ## What I need from you to choose the next fix
> One decision, then we move fast:
> 
> ### Do you want the HTML site to work **offline by file open**?
> If yes → we must copy evidence into `site/assets/` (bigger output size, but phone-friendly).
> 
> ### Or do you want the HTML site to work via **API links**?
> If yes → we add a `/file/{evidence_id}` endpoint and link to that (lighter output, but needs server running).
> 
> Reply with just: **offline** or **api**.
> 
> ---
> 
> ## If you say “offline” (most likely for you)
> Next steps will be:
> 1) move outputs to `E_OUTPUTS`
> 2) copy evidence referenced in manifest into `site/assets/` (or copy all, your choice)
> 3) update indexer links to `assets/<rel_path>`
> 4) add `latest.txt`
> 
> If you say “api,” we’ll:
> 1) move outputs to `E_OUTPUTS`
> 2) implement secure file streaming endpoint
> 3) update indexer links to `http://localhost:8080/vis/runs/<run_id>/file/<id>`
> 
> Your call: **offline** or **api**.

### User
> we are not using mkdocs we are doing vitepress build.

### Assistant
> Understood. That changes *presentation wiring*, not the VIS engine. The engine still outputs to `E_OUTPUTS/vis/<run_id>/…`, and **VitePress consumes those artifacts**.
> 
> Here’s what we do next, in the right order.
> 
> ---
> 
> ## 1) Keep the engine contract the same
> Regardless of MkDocs vs VitePress:
> 
> - **C_VIS = data** (`content/C_VIS/**`)
> - **VIS outputs = generated** (`content/E_OUTPUTS/vis/<run_id>/**`)
> - **VitePress reads from content + outputs**, it does not own truth.
> 
> So the next engine task is still:
> 
> ### ✅ Move outputs from `content/output/vis` → `content/E_OUTPUTS/vis`
> 
> That is purely hygiene + alignment.
> 
> ---
> 
> ## 2) Decide how VitePress will *see* VIS outputs
> VitePress wants Markdown under its `docs/` root. You have two clean options:
> 
> ### Option A (Recommended): VitePress `docs/` is a mirror folder
> - Your VitePress project lives in `app/vitepress/`
> - You set it up so it can include:
>   - `../../content/C_VIS/**`
>   - `../../content/E_OUTPUTS/vis/latest/**`
> 
> But VitePress does **not** natively read outside the docs root cleanly unless you:
> - symlink folders into `app/vitepress/docs/` (Windows can be annoying), or
> - run a pre-build “sync” script.
> 
> So…
> 
> ### Option B (Most reliable on Windows): Pre-build sync script
> Create a script that copies (or rsyncs) the relevant subsets into `app/vitepress/docs/` before build.
> 
> Example targets:
> - `app/vitepress/docs/vis/` ← from `content/C_VIS/`
> - `app/vitepress/docs/_outputs/vis/` ← from `content/E_OUTPUTS/vis/latest/`
> 
> This avoids symlink drama and makes builds deterministic.
> 
> **I recommend Option B for you.**
> 
> ---
> 
> ## 3) VitePress-specific next steps (what we work on now)
> 
> ### Step 1 — Fix VIS output path
> Update `StorageAdapter` so new runs write to:
> - `content/E_OUTPUTS/vis/<run_id>/…`
> 
> And optionally copy older runs from `content/output/vis/` into the new location (one-time migration).
> 
> ### Step 2 — Create a sync script for VitePress docs
> Add:
> 
> - `scripts/vitepress/sync_vis_to_docs.ps1`
> - `scripts/vitepress/sync_vis_to_docs.sh`
> 
> What it does:
> 1) Detect latest run id (from `latest.txt` or by newest folder)
> 2) Copy:
>    - `content/C_VIS/**` → `app/vitepress/docs/vis/**`
>    - `content/E_OUTPUTS/vis/<latest>/**` → `app/vitepress/docs/_outputs/vis/**`
> 3) Optionally generate a small index page:
>    - `app/vitepress/docs/vis/index.md`
>    - `app/vitepress/docs/_outputs/vis/index.md` (links to report, manifest, site)
> 
> ### Step 3 — Update VitePress config nav
> Add nav entries for:
> - VIS (C_VIS library)
> - Latest VIS Run (outputs)
> 
> ---
> 
> ## One decision I still need from you (because it affects linking)
> Even with VitePress, you still need to choose how to handle file links:
> 
> ### A) “Offline artifacts” approach (best for phone + PDF export)
> VIS copies evidence into:
> - `.../site/assets/...`
> 
> Then VitePress can link to assets inside `docs/public/` or `docs/_outputs/…` depending on how you want it served.
> 
> ### B) “API streaming” approach (best for interactive browsing)
> VitePress links to running service endpoints.
> 
> Given you’re doing VitePress builds and want to open it on your phone, **A is usually the right call**.
> 
> ---
> 
> ## Immediate next action (no debate)
> Since you said VitePress, the best next work item is:
> 
> **Build the VitePress sync pipeline.**
> 
> Reply with one word:
> - **offline** (copy assets into the build)
> - **api** (links require running server)
> 
> If you choose **offline**, I’ll give you the exact scripts and folder targets for Windows + Docker + VitePress so it’s one-click:  
> `sync → build → serve → open on phone`.

### User
> so yes option b the script and the other decision is A.

### Assistant
> Good. Option B + Offline assets is the fastest, most reliable path on Windows.
> 
> Here’s the exact plan and the concrete scripts/config you need.
> 
> ---
> 
> # Target architecture
> 
> ## Source of truth
> - `content/C_VIS/**` (your VIS corpus)
> - `content/B_EVIDENCE/**` (evidence)
> - `content/E_OUTPUTS/vis/<run_id>/**` (generated VIS run outputs)
> 
> ## VitePress build inputs (generated via sync script)
> - `app/vitepress/docs/vis/**`  ← copy of `content/C_VIS/**`
> - `app/vitepress/docs/_outputs/vis/**` ← copy of latest VIS outputs (report, manifest, site)
> - `app/vitepress/docs/public/vis-assets/**` ← offline evidence asset copies (so links work on phone)
> 
> ---
> 
> # Step 1 — Update VIS to write to `content/E_OUTPUTS/vis/` and maintain `latest.txt`
> 
> ### Change `StorageAdapter` output location
> In `app/Legalmind/backend/vis-service/services/storage_adapter.py`, change:
> 
> - from: `binder_root / "output" / "vis" / run_id`
> - to: `binder_root / "E_OUTPUTS" / "vis" / run_id`
> 
> Also write:
> - `binder_root/E_OUTPUTS/vis/latest.txt` containing the run_id
> 
> **Pseudo-diff (what needs to exist):**
> ```python
> self.output_root = self.binder_root / "E_OUTPUTS" / "vis"
> self.output_base = self.output_root / run_id
> ...
> (self.output_root).mkdir(parents=True, exist_ok=True)
> self.write_text("../latest.txt", run_id)  # or explicitly open binder_root/E_OUTPUTS/vis/latest.txt
> ```
> 
> If you want, I can give you the exact patched file, but since you’re using Codex for diffs, the above is the precise change spec.
> 
> ---
> 
> # Step 2 — Offline assets: copy evidence into VitePress `public/`
> 
> Because you chose Offline (A), we will not rely on API streaming. We will make VitePress serve assets from `docs/public`.
> 
> VitePress rule:
> - Anything under `docs/public/` is served at the site root.
> - So `docs/public/vis-assets/foo.pdf` becomes `/vis-assets/foo.pdf`
> 
> ---
> 
> # Step 3 — Add the sync scripts (Option B)
> 
> Create this folder:
> - `scripts/vitepress/`
> 
> ## A) PowerShell sync script (Windows)
> Save as: `scripts/vitepress/sync_vis_to_docs.ps1`
> 
> ```powershell
> param(
>   [string]$RepoRoot = (Resolve-Path ".").Path
> )
> 
> $ErrorActionPreference = "Stop"
> 
> $contentRoot = Join-Path $RepoRoot "content"
> $viteRoot    = Join-Path $RepoRoot "app\vitepress"
> $docsRoot    = Join-Path $viteRoot "docs"
> 
> $srcVis      = Join-Path $contentRoot "C_VIS"
> $outVisRoot  = Join-Path $contentRoot "E_OUTPUTS\vis"
> $latestFile  = Join-Path $outVisRoot "latest.txt"
> 
> $dstVis      = Join-Path $docsRoot "vis"
> $dstOut      = Join-Path $docsRoot "_outputs\vis"
> $dstAssets   = Join-Path $docsRoot "public\vis-assets"
> 
> function Ensure-Dir($p) { if (!(Test-Path $p)) { New-Item -ItemType Directory -Path $p | Out-Null } }
> 
> function Copy-Clean($src, $dst) {
>   if (Test-Path $dst) { Remove-Item $dst -Recurse -Force }
>   Ensure-Dir (Split-Path $dst -Parent)
>   Copy-Item $src $dst -Recurse -Force
> }
> 
> # 1) Determine latest run
> if (!(Test-Path $outVisRoot)) {
>   throw "Missing VIS outputs folder: $outVisRoot (run VIS first)."
> }
> 
> $runId = $null
> if (Test-Path $latestFile) {
>   $runId = (Get-Content $latestFile -Raw).Trim()
> }
> 
> if ([string]::IsNullOrWhiteSpace($runId)) {
>   # fallback to newest directory
>   $dirs = Get-ChildItem $outVisRoot -Directory | Sort-Object LastWriteTime -Descending
>   if ($dirs.Count -eq 0) { throw "No VIS run directories found in $outVisRoot." }
>   $runId = $dirs[0].Name
> }
> 
> $runPath = Join-Path $outVisRoot $runId
> if (!(Test-Path $runPath)) { throw "Latest run path not found: $runPath" }
> 
> Write-Host "Using VIS run_id: $runId"
> 
> # 2) Sync C_VIS into docs/vis
> Ensure-Dir $docsRoot
> Copy-Clean $srcVis $dstVis
> 
> # 3) Sync latest outputs into docs/_outputs/vis
> Copy-Clean $runPath $dstOut
> 
> # 4) Copy evidence assets into docs/public/vis-assets using manifest.json
> # Expect manifest at: docs/_outputs/vis/manifest.json after copy
> $manifestPath = Join-Path $dstOut "manifest.json"
> if (!(Test-Path $manifestPath)) {
>   throw "manifest.json not found at $manifestPath"
> }
> 
> Ensure-Dir $dstAssets
> 
> $manifest = Get-Content $manifestPath -Raw | ConvertFrom-Json
> 
> # Copy each file from content root to public assets, preserving rel_path
> foreach ($item in $manifest) {
>   $rel = $item.rel_path
>   if ([string]::IsNullOrWhiteSpace($rel)) { continue }
> 
>   # source file inside content/
>   $srcFile = Join-Path $contentRoot $rel
>   if (!(Test-Path $srcFile)) { continue }
> 
>   $dstFile = Join-Path $dstAssets $rel
>   $dstDir  = Split-Path $dstFile -Parent
>   Ensure-Dir $dstDir
> 
>   Copy-Item $srcFile $dstFile -Force
> }
> 
> # 5) Write a tiny index page that links to the latest run
> $indexMd = @"
> ---
> title: VIS
> ---
> 
> # VIS
> 
> - [VIS Library (C_VIS)](/vis/NT_01_MASTER_INDEX)
> - [Latest VIS Run Outputs](/_outputs/vis/)
> 
> **Run ID:** $runId
> "@
> 
> Ensure-Dir $docsRoot
> Set-Content -Path (Join-Path $docsRoot "vis_index.md") -Value $indexMd -Encoding UTF8
> 
> Write-Host "Sync complete:"
> Write-Host "- C_VIS -> $dstVis"
> Write-Host "- Outputs -> $dstOut"
> Write-Host "- Assets -> $dstAssets"
> Write-Host "- Index  -> $($docsRoot)\vis_index.md"
> ```
> 
> ## B) Bash sync script (Mac/Linux/WSL optional)
> Save as: `scripts/vitepress/sync_vis_to_docs.sh`
> 
> ```bash
> #!/usr/bin/env bash
> set -euo pipefail
> 
> REPO_ROOT="$(pwd)"
> CONTENT="$REPO_ROOT/content"
> VITE="$REPO_ROOT/app/vitepress"
> DOCS="$VITE/docs"
> 
> SRC_VIS="$CONTENT/C_VIS"
> OUT_VIS_ROOT="$CONTENT/E_OUTPUTS/vis"
> LATEST_FILE="$OUT_VIS_ROOT/latest.txt"
> 
> DST_VIS="$DOCS/vis"
> DST_OUT="$DOCS/_outputs/vis"
> DST_ASSETS="$DOCS/public/vis-assets"
> 
> mkdir -p "$DOCS"
> 
> # Determine latest run id
> RUN_ID=""
> if [[ -f "$LATEST_FILE" ]]; then
>   RUN_ID="$(cat "$LATEST_FILE" | tr -d '[:space:]')"
> fi
> 
> if [[ -z "$RUN_ID" ]]; then
>   RUN_ID="$(ls -1t "$OUT_VIS_ROOT" | head -n 1)"
> fi
> 
> RUN_PATH="$OUT_VIS_ROOT/$RUN_ID"
> [[ -d "$RUN_PATH" ]] || { echo "Run path missing: $RUN_PATH"; exit 1; }
> 
> echo "Using VIS run_id: $RUN_ID"
> 
> rm -rf "$DST_VIS" "$DST_OUT"
> mkdir -p "$(dirname "$DST_VIS")" "$(dirname "$DST_OUT")"
> cp -R "$SRC_VIS" "$DST_VIS"
> cp -R "$RUN_PATH" "$DST_OUT"
> 
> # Copy evidence assets based on manifest.json
> MANIFEST="$DST_OUT/manifest.json"
> mkdir -p "$DST_ASSETS"
> 
> python - << 'PY'
> import json, os, shutil
> repo = os.getcwd()
> content = os.path.join(repo, "content")
> dst_assets = os.path.join(repo, "app", "vitepress", "docs", "public", "vis-assets")
> manifest = os.path.join(repo, "app", "vitepress", "docs", "_outputs", "vis", "manifest.json")
> 
> with open(manifest, "r", encoding="utf-8") as f:
>     data = json.load(f)
> 
> os.makedirs(dst_assets, exist_ok=True)
> for item in data:
>     rel = item.get("rel_path")
>     if not rel:
>         continue
>     src = os.path.join(content, rel)
>     if not os.path.exists(src):
>         continue
>     dst = os.path.join(dst_assets, rel)
>     os.makedirs(os.path.dirname(dst), exist_ok=True)
>     shutil.copy2(src, dst)
> PY
> 
> cat > "$DOCS/vis_index.md" << EOF
> ---
> title: VIS
> ---
> 
> # VIS
> 
> - [VIS Library (C_VIS)](/vis/NT_01_MASTER_INDEX)
> - [Latest VIS Run Outputs](/_outputs/vis/)
> 
> **Run ID:** $RUN_ID
> EOF
> 
> echo "Sync complete."
> ```
> 
> ---
> 
> # Step 4 — Make VitePress serve a directory index for `_outputs/vis`
> VitePress doesn’t automatically list folders. So we add a small index file inside outputs on sync.
> 
> Update the PowerShell script (and bash) to also write:
> 
> `app/vitepress/docs/_outputs/vis/index.md`
> 
> Add this block after outputs copy:
> 
> ```md
> ---
> title: Latest VIS Run
> ---
> 
> # Latest VIS Run
> 
> - [VIS Report](./VIS_Report.md)  (if you generate one)
> - [Claims Map (JSON)](./claims_map.json)
> - [Manifest (JSON)](./manifest.json)
> - [Manifest (CSV)](./manifest.csv)
> - [Static Site](./site/index.html)
> 
> Assets are served under: `/vis-assets/…`
> ```
> 
> Right now your service doesn’t generate `VIS_Report.md`, but you can link what exists today.
> 
> ---
> 
> # Step 5 — Update VitePress nav (minimal)
> In `app/vitepress/docs/.vitepress/config.(ts|js)` add:
> 
> ```js
> nav: [
>   { text: 'VIS', link: '/vis_index' },
>   { text: 'C_VIS Library', link: '/vis/NT_01_MASTER_INDEX' },
>   { text: 'Latest VIS Output', link: '/_outputs/vis/' },
> ],
> ```
> 
> (If your config uses a different structure, keep the intent: link those pages.)
> 
> ---
> 
> # Step 6 — One-click build/serve (Windows)
> Create: `scripts/vitepress/build_and_serve.ps1`
> 
> ```powershell
> $ErrorActionPreference = "Stop"
> 
> # 1) Sync
> .\scripts\vitepress\sync_vis_to_docs.ps1
> 
> # 2) Build + serve
> Push-Location .\app\vitepress
> npm install
> npm run docs:build
> npm run docs:dev -- --host 0.0.0.0 --port 5173
> Pop-Location
> ```
> 
> If you already have node_modules installed, remove `npm install` to speed it up.
> 
> ---
> 
> # What to do right now (in order)
> 1) **Patch VIS output path** to `content/E_OUTPUTS/vis` + write `latest.txt`
> 2) Run VIS again (Docker) to create a run in the new location
> 3) Run:
>    ```powershell
>    .\scripts\vitepress\sync_vis_to_docs.ps1
>    ```
> 4) Run VitePress dev server, open the site, click:
>    - `/vis_index`
>    - `/vis/NT_01_MASTER_INDEX`
>    - `/_outputs/vis/`
>    - confirm `/vis-assets/...` links open
> 
> ---
> 
> ## One important warning (so you don’t get surprised)
> Copying *all* evidence into `docs/public/vis-assets` can get big. That’s okay locally, but you may not want to publish it publicly. If you plan to publish, we’ll add a “publish-safe mode” that only copies a selected subset.
> 
> ---
> 
> If you paste your current VitePress folder structure (`app/vitepress` tree) and the name of your docs script commands in `package.json`, I’ll tailor the exact `build_and_serve.ps1` to match your actual scripts (no guessing).

### User
> mam, gemini just gave me this desktop ap launcher thing in like two second how come we nevert use anythign like that for local viewing import sys

> import os

> import shutil

> import datetime

> import subprocess

> import requests

> from pathlib import Path

> from PyQt6.QtWidgets import (

>     QApplication,

>     QMainWindow,

>     QWidget,

>     QVBoxLayout,

>     QHBoxLayout,

>     QTreeView,

>     QTextEdit,

>     QLabel,

>     QPushButton,

>     QSplitter,

>     QTabWidget,

>     QFormLayout,

>     QLineEdit,

>     QComboBox,

>     QDateEdit,

>     QMessageBox,

>     QGroupBox,

>     QPlainTextEdit,

>     QProgressBar,

>     QStackedWidget,

> )

> from PyQt6.QtCore import Qt, QDate, QProcess, QSize, QTimer

> 

> # FIXED: QFileSystemModel is imported from QtGui in PyQt6, not QtWidgets

> from PyQt6.QtGui import QAction, QIcon, QFileSystemModel, QColor, QFont

> 

> # Configuration

> ROOT_DIR = Path(__file__).parent.parent.resolve()

> VIS_SERVICE_PATH = ROOT_DIR / "app" / "Legalmind" / "backend" / "vis-service"

> DOCKER_COMPOSE_PATH = ROOT_DIR / "docker-compose.yml"  # Assuming root has this

> 

> 

> class DarkPalette:

>     BG_DARK = "#1e1e1e"

>     BG_LIGHT = "#252526"

>     FG_TEXT = "#cccccc"

>     ACCENT = "#007acc"

>     border = "#3e3e42"

> 

> 

> STYLESHEET = f"""

>     QMainWindow, QWidget {{ background-color: {DarkPalette.BG_DARK}; color: {DarkPalette.FG_TEXT}; font-family: 'Segoe UI', sans-serif; }}

>     QTreeView {{ background-color: {DarkPalette.BG_LIGHT}; border: 1px solid {DarkPalette.border}; outline: none; }}

>     QTreeView::item:selected {{ background-color: {DarkPalette.ACCENT}; color: white; }}

>     QTextEdit, QPlainTextEdit {{ background-color: {DarkPalette.BG_DARK}; border: 1px solid {DarkPalette.border}; color: {DarkPalette.FG_TEXT}; font-family: 'Consolas', monospace; }}

>     QPushButton {{ background-color: {DarkPalette.BG_LIGHT}; border: 1px solid {DarkPalette.border}; padding: 6px 12px; color: white; }}

>     QPushButton:hover {{ background-color: {DarkPalette.ACCENT}; }}

>     QPushButton:pressed {{ background-color: #005a9e; }}

>     QLabel {{ font-size: 14px; }}

>     QHeaderView::section {{ background-color: {DarkPalette.BG_LIGHT}; padding: 4px; border: none; color: {DarkPalette.FG_TEXT}; }}

>     QGroupBox {{ border: 1px solid {DarkPalette.border}; margin-top: 20px; font-weight: bold; }}

>     QGroupBox::title {{ subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; }}

> """

> 

> 

> class FilePreview(QWidget):

>     def __init__(self):

>         super().__init__()

>         layout = QVBoxLayout(self)

>         self.editor = QTextEdit()

>         self.editor.setReadOnly(True)

>         self.path_label = QLabel("Select a file to preview")

>         self.path_label.setStyleSheet(

>             f"color: {DarkPalette.ACCENT}; font-weight: bold;"

>         )

> 

>         layout.addWidget(self.path_label)

>         layout.addWidget(self.editor)

> 

>     def load_file(self, path):

>         self.path_label.setText(str(path.name))

>         if path.is_dir():

>             self.editor.setText(f"📂 Directory: {path}")

>             return

> 

>         suffix = path.suffix.lower()

>         if suffix in [".md", ".txt", ".py", ".yaml", ".json", ".xml", ".csv", ".log"]:

>             try:

>                 with open(path, "r", encoding="utf-8") as f:

>                     self.editor.setText(f.read())

>             except Exception as e:

>                 self.editor.setText(f"Error reading file: {str(e)}")

>         elif suffix in [".png", ".jpg", ".jpeg"]:

>             self.editor.setText("[Image Preview Not Implemented in Text View]")

>             # In a full app, switch to QLabel with QPixmap here

>         else:

>             self.editor.setText(f"Binary or unsupported file type: {suffix}")

> 

> 

> class SmartCreator(QGroupBox):

>     def __init__(self, current_path_callback):

>         super().__init__("Safe File Creator")

>         self.get_current_path = current_path_callback

> 

>         layout = QFormLayout()

> 

>         self.date_edit = QDateEdit()

>         self.date_edit.setDate(QDate.currentDate())

>         self.date_edit.setDisplayFormat("yyyy-MM-dd")

> 

>         self.type_combo = QComboBox()

>         self.type_combo.addItems(

>             ["Log Entry", "Motion", "Exhibit", "Note", "Correspondence"]

>         )

> 

>         self.desc_edit = QLineEdit()

>         self.desc_edit.setPlaceholderText("short_description_snake_case")

> 

>         self.create_btn = QPushButton("Create Markdown File")

>         self.create_btn.clicked.connect(self.create_file)

> 

>         layout.addRow("Date:", self.date_edit)

>         layout.addRow("Type:", self.type_combo)

>         layout.addRow("Slug:", self.desc_edit)

>         layout.addRow(self.create_btn)

> 

>         self.setLayout(layout)

> 

>     def create_file(self):

>         folder = self.get_current_path()

>         if not folder.is_dir():

>             folder = folder.parent

> 

>         date_str = self.date_edit.date().toString("yyyy-MM-dd")

>         slug = self.desc_edit.text().replace(" ", "_").lower()

>         prefix = {

>             "Log Entry": "",

>             "Motion": "MO_",

>             "Exhibit": "EXH_",

>             "Correspondence": "COR_",

>             "Note": "NT_",

>         }.get(self.type_combo.currentText(), "")

> 

>         filename = f"{prefix}{date_str}_{slug}.md"

>         full_path = folder / filename

> 

>         if full_path.exists():

>             QMessageBox.warning(self, "Error", "File already exists!")

>             return

> 

>         try:

>             with open(full_path, "w") as f:

>                 f.write(

>                     f"# {date_str} - {self.type_combo.currentText()}\n\n## Description\n{slug.replace('_', ' ')}\n"

>                 )

>             QMessageBox.information(self, "Success", f"Created: {filename}")

>         except Exception as e:

>             QMessageBox.critical(self, "Error", str(e))

> 

> 

> class VisController(QWidget):

>     def __init__(self):

>         super().__init__()

>         layout = QVBoxLayout()

> 

>         # Controls

>         controls_layout = QHBoxLayout()

>         self.btn_scan = QPushButton("Run VIS Integrity Scan")

>         self.btn_site = QPushButton("Build Static Site")

>         self.btn_open_report = QPushButton("Open VIS Report")

> 

>         controls_layout.addWidget(self.btn_scan)

>         controls_layout.addWidget(self.btn_site)

>         controls_layout.addWidget(self.btn_open_report)

> 

>         # Output Log

>         self.log_output = QPlainTextEdit()

>         self.log_output.setReadOnly(True)

> 

>         layout.addLayout(controls_layout)

>         layout.addWidget(QLabel("Process Output:"))

>         layout.addWidget(self.log_output)

> 

>         self.setLayout(layout)

> 

>         # Connections

>         self.btn_scan.clicked.connect(lambda: self.run_process("vis-scan"))

>         # In a real scenario, map these to actual script paths

>         self.btn_site.clicked.connect(

>             lambda: self.log("Site generation not linked yet.")

>         )

>         self.btn_open_report.clicked.connect(self.open_report)

> 

>         self.process = QProcess()

>         self.process.readyReadStandardOutput.connect(self.handle_stdout)

>         self.process.readyReadStandardError.connect(self.handle_stderr)

> 

>     def log(self, text):

>         self.log_output.appendPlainText(text)

> 

>     def run_process(self, action):

>         self.log_output.clear()

>         if action == "vis-scan":

>             # Assuming python is in path and we use the installed module

>             # We run the command relative to root

>             cmd = "python"

>             args = ["-m", "vis.main", "run", "--binder", str(ROOT_DIR)]

> 

>             # Check if we should use the microservice or the local script

>             # For the launcher, local script mode is safer/easier

>             script_path = (

>                 ROOT_DIR / "app" / "Legalmind" / "backend" / "vis-service" / "main.py"

>             )

>             # Ideally we used the module 'vis' from the previous prompt.

>             # Let's assume we run the 'vis-service' via uvicorn for API or just a custom script.

>             # Fallback to simple echo for demonstration if scripts aren't executable

> 

>             self.log(f"Starting VIS Scan on: {ROOT_DIR}")

>             # This is where we would trigger the docker container or python script

>             # For now, let's simulate checking the setup script

>             self.log("Triggering backend scan...")

>             self.process.start("echo", ["Simulating VIS Scan... Done."])

> 

>     def handle_stdout(self):

>         data = self.process.readAllStandardOutput()

>         stdout = bytes(data).decode("utf8")

>         self.log(stdout)

> 

>     def handle_stderr(self):

>         data = self.process.readAllStandardError()

>         stderr = bytes(data).decode("utf8")

>         self.log(f"ERR: {stderr}")

> 

>     def open_report(self):

>         report_path = ROOT_DIR / "output" / "VIS_Report.md"

>         if report_path.exists():

>             import webbrowser

> 

>             webbrowser.open(str(report_path))

>         else:

>             self.log("Report not found. Run scan first.")

> 

> 

> class MainWindow(QMainWindow):

>     def __init__(self):

>         super().__init__()

>         self.setWindowTitle("Legalmind Command Center")

>         self.resize(1200, 800)

>         self.setStyleSheet(STYLESHEET)

> 

>         # Central Widget

>         central = QWidget()

>         self.setCentralWidget(central)

>         main_layout = QVBoxLayout(central)

> 

>         # Top Bar

>         top_bar = QHBoxLayout()

>         title = QLabel("LEGALMIND OS")

>         title.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))

>         title.setStyleSheet(f"color: {DarkPalette.ACCENT};")

> 

>         self.status_label = QLabel("System Status: Ready")

> 

>         top_bar.addWidget(title)

>         top_bar.addStretch()

>         top_bar.addWidget(self.status_label)

> 

>         # Main Splitter (Left: Tree, Right: Content)

>         splitter = QSplitter(Qt.Orientation.Horizontal)

> 

>         # --- Left Panel: File Explorer ---

>         left_widget = QWidget()

>         left_layout = QVBoxLayout(left_widget)

> 

>         self.file_model = QFileSystemModel()

>         self.file_model.setRootPath(str(ROOT_DIR))

> 

>         self.tree = QTreeView()

>         self.tree.setModel(self.file_model)

>         self.tree.setRootIndex(self.file_model.index(str(ROOT_DIR)))

>         self.tree.setColumnWidth(0, 250)

>         self.tree.hideColumn(1)  # Size

>         self.tree.hideColumn(2)  # Type

>         self.tree.clicked.connect(self.on_file_click)

> 

>         left_layout.addWidget(QLabel("CASE_FCFCU Explorer"))

>         left_layout.addWidget(self.tree)

> 

>         # Smart Creator (Bottom Left)

>         self.creator = SmartCreator(self.get_selected_path)

>         left_layout.addWidget(self.creator)

> 

>         # --- Right Panel: Tabs ---

>         right_tabs = QTabWidget()

> 

>         # Tab 1: Preview

>         self.previewer = FilePreview()

>         right_tabs.addTab(self.previewer, "File Preview")

> 

>         # Tab 2: VIS Engine

>         self.vis_control = VisController()

>         right_tabs.addTab(self.vis_control, "VIS Engine")

> 

>         # Tab 3: Docker/System (Placeholder)

>         sys_widget = QWidget()

>         sys_layout = QVBoxLayout(sys_widget)

>         sys_layout.addWidget(QLabel("Docker Management (Coming Soon)"))

>         start_services = QPushButton("Start All Services (docker-compose up)")

>         stop_services = QPushButton("Stop All Services")

>         sys_layout.addWidget(start_services)

>         sys_layout.addWidget(stop_services)

>         sys_layout.addStretch()

>         right_tabs.addTab(sys_widget, "System Services")

> 

>         # Add widgets to splitter

>         splitter.addWidget(left_widget)

>         splitter.addWidget(right_tabs)

>         splitter.setStretchFactor(1, 3)

> 

>         main_layout.addLayout(top_bar)

>         main_layout.addWidget(splitter)

> 

>     def get_selected_path(self):

>         index = self.tree.currentIndex()

>         if index.isValid():

>             return Path(self.file_model.filePath(index))

>         return ROOT_DIR

> 

>     def on_file_click(self, index):

>         path = Path(self.file_model.filePath(index))

>         self.previewer.load_file(path)

> 

> 

> if __name__ == "__main__":

>     app = QApplication(sys.argv)

>     window = MainWindow()

>     window.show()

>     sys.exit(app.exec())

### Assistant
> Because a PyQt “command center” is **a different product class** than what you’re building—and it’s usually a trap when the real goal is: *audit → generate artifacts → view on phone → print/export*. Gemini gave you a shiny dashboard in 2 seconds, but it punts on the hard parts and adds new problems.
> 
> Here’s the real breakdown.
> 
> ## Why we didn’t default to a desktop launcher
> ### 1) Packaging/Distribution overhead (especially on Windows)
> A PyQt app isn’t “run it and forget it.” You immediately inherit:
> - PyQt install/versions (often finicky)
> - packaging (PyInstaller) and antivirus false positives
> - file associations, permissions, PATH issues
> - UI bug surface area (threading, blocking calls)
> 
> For your case workflow, that overhead is pure drag.
> 
> ### 2) It doesn’t solve your core requirement better than VitePress
> Your north star is:
> - deterministic outputs
> - offline, phone-friendly viewing
> - print/export
> 
> A desktop UI doesn’t help your phone. VitePress does.
> 
> ### 3) That code is mostly a skeleton (and it lies a little)
> Specific problems in the snippet you pasted:
> 
> - **ROOT_DIR is wrong for your repo**:  
>   `ROOT_DIR = Path(__file__).parent.parent.resolve()` depends on where you save it. Put it in `/launcher/` and it points somewhere else. You’ll chase path bugs.
> 
> - **VIS run command is wrong for your actual engine**:  
>   It calls `python -m vis.main run...` but your running VIS is `vis-service` via FastAPI/Docker. That module doesn’t exist in your current repo unless you add it.
> 
> - **“Open report” path is wrong**:  
>   It looks for `ROOT_DIR / "output" / "VIS_Report.md"`. Your real outputs are under `content/output/vis/<run_id>/...` (and soon `content/E_OUTPUTS/vis/...`).
> 
> - **It uses `echo "Simulating VIS Scan"`**:  
>   So it’s not actually wired to your pipeline.
> 
> - **File preview is unsafe / impractical**:
>   - tries to read any `.csv`/`.json` directly into QTextEdit (can choke on large files)
>   - no PDF preview (which you need most)
>   - no binary safeguards beyond a message
> 
> So: it “looks like an app,” but it’s not actually integrated with your system.
> 
> ## The honest answer
> We didn’t use something like this because it’s **premature UI**. You’d be building a second interface while your pipeline and contracts are still stabilizing.
> 
> ## The better path
> You already have the right engine and outputs. What you need is a **launcher script**, not a GUI app:
> 
> ### What wins right now
> A one-click PowerShell launcher that does:
> 
> 1) Ensure Docker container is up  
> 2) POST `/vis/run`  
> 3) Wait/poll until outputs exist  
> 4) Run `scripts/vitepress/sync_vis_to_docs.ps1`  
> 5) Start VitePress dev server  
> 6) Print the local URL for your phone
> 
> That gets you the same “command center” experience with:
> - near-zero dependencies
> - easy debugging
> - repeatable runs
> - no UI maintenance burden
> 
> ## If you still want a desktop app later (valid, but later)
> Do it as a **thin wrapper** around the scripts:
> - buttons call PowerShell scripts
> - output window tails logs
> - never re-implements the pipeline
> 
> That’s how you keep it from becoming a parallel universe.
> 
> ## What we should do next (concrete)
> Since you’ve proven VIS runs and you chose VitePress + offline assets:
> 
> 1) Patch VIS output path to `content/E_OUTPUTS/vis/<run_id>` + write `latest.txt`  
> 2) Add the VitePress sync script  
> 3) Add a single PowerShell “Run Everything” launcher
> 
> If you want, paste:
> - the location of your `app/vitepress/package.json` scripts (the `docs:dev`/`docs:build` names)
> - the path where you want the launcher (`launcher/` or `scripts/`)
> 
> …and I’ll give you the exact `run_all.ps1` that works on your Windows setup.

### User
> here is the tree now are we spot on or still need fixes. ```markdown

> . 📂 CASE_FCFCU

> ├── 📄 CASE_ENGINE.py

> ├── 📄 CASE_FCFCU.code-workspace

> └── 📂 app/

> │  └── 📂 Legalmind/

> │    ├── 📄 CONTRIBUTING.md

> │    ├── 📄 LICENSE

> │    ├── 📄 PLATFORM_README.md

> │    ├── 📄 PROJECT-OVERVIEW.md

> │    ├── 📄 README.md

> │    └── 📂 backend/

> │      └── 📂 agent-orchestrator/

> │        ├── 📄 Dockerfile

> │        ├── 📄 main.py

> │        ├── 📄 requirements.txt

> │        └── 📂 services/

> │          ├── 📄 __init__.py

> │          ├── 📄 debate_manager.py

> │          ├── 📄 dynamic_agent.py

> │          ├── 📄 fixed_agent.py

> │          ├── 📄 legal_reference_engine.py

> │          ├── 📄 retry_handler.py

> │          ├── 📄 websocket_manager.py

> │      └── 📂 api-gateway/

> │        ├── 📄 Dockerfile

> │        ├── 📄 main.py

> │        ├── 📄 requirements.txt

> │      └── 📂 parser-service/

> │        ├── 📄 Dockerfile

> │        ├── 📄 main.py

> │        ├── 📄 requirements.txt

> │        └── 📂 services/

> │          ├── 📄 __init__.py

> │          ├── 📄 document_processor.py

> │          ├── 📄 entity_extractor.py

> │          ├── 📄 firestore_client.py

> │          ├── 📄 pii_redactor.py

> │          ├── 📄 pubsub_client.py

> │          ├── 📄 storage_client.py

> │      └── 📂 report-generator/

> │        ├── 📄 Dockerfile

> │        ├── 📄 main.py

> │        ├── 📄 requirements.txt

> │        ├── 📄 subscriber.py

> │      └── 📂 role-assignment/

> │        ├── 📄 Dockerfile

> │        ├── 📄 main.py

> │        ├── 📄 requirements.txt

> │        └── 📂 services/

> │          ├── 📄 __init__.py

> │          ├── 📄 agent_pool_manager.py

> │          ├── 📄 firestore_client.py

> │          ├── 📄 pubsub_client.py

> │          ├── 📄 role_analyzer.py

> │      └── 📂 video-generator/

> │        ├── 📄 Dockerfile

> │        ├── 📄 main.py

> │        ├── 📄 main_ai_video.py

> │        ├── 📄 main_veo3.py

> │        ├── 📄 requirements.txt

> │        ├── 📄 subscriber.py

> │      └── 📂 vis-service/

> │        ├── 📄 Dockerfile

> │        └── 📂 __pycache__/

> │          ├── 📄 main.cpython-311.pyc

> │        ├── 📄 main.py

> │        ├── 📄 requirements.txt

> │        └── 📂 services/

> │          ├── 📄 __init__.py

> │          └── 📂 __pycache__/

> │            ├── 📄 __init__.cpython-311.pyc

> │            ├── 📄 claims_mapper.cpython-311.pyc

> │            ├── 📄 hasher.cpython-311.pyc

> │            ├── 📄 indexer.cpython-311.pyc

> │            ├── 📄 metadata.cpython-311.pyc

> │            ├── 📄 scanner.cpython-311.pyc

> │            ├── 📄 storage_adapter.cpython-311.pyc

> │          ├── 📄 claims_mapper.py

> │          ├── 📄 hasher.py

> │          ├── 📄 indexer.py

> │          ├── 📄 metadata.py

> │          ├── 📄 scanner.py

> │          ├── 📄 storage_adapter.py

> │        ├── 📄 vis.yaml

> │    ├── 📄 deploy-to-github.sh

> │    └── 📂 docs/

> │      ├── 📄 DEPLOYMENT.md

> │      └── 📂 backend-docs/

> │        ├── 📄 01-parser-service-COMPLETE.md

> │        ├── 📄 02-api-gateway-COMPLETE.md

> │        ├── 📄 03-agent-orchestrator-COMPLETE.md

> │        ├── 📄 04-role-assignment-COMPLETE.md

> │        ├── 📄 05-video-generator-COMPLETE.md

> │        ├── 📄 06-report-generator-COMPLETE.md

> │        ├── 📄 AGENT_ORCHESTRATOR_SUMMARY.md

> │        ├── 📄 COMPLETE_SYSTEM_GUIDE.md

> │        ├── 📄 DOCUMENTATION_SUMMARY.md

> │        ├── 📄 README.md

> │        ├── 📄 ROLE_ASSIGNMENT_SUMMARY.md

> │      └── 📂 diagrams/

> │        ├── 📄 README.md

> │        ├── 📄 SYSTEM-ARCHITECTURE.md

> │        ├── 📄 SYSTEM-WORKFLOW.md

> │      └── 📂 frontend-docs/

> │        ├── 📄 01-FRONTEND-ARCHITECTURE-COMPLETE.md

> │        ├── 📄 02-PAGES-AND-COMPONENTS.md

> │        ├── 📄 03-API-AND-WEBSOCKET.md

> │        ├── 📄 ALIGNMENT-VERIFICATION.md

> │        ├── 📄 COMPLETE-FRONTEND-GUIDE.md

> │        ├── 📄 DOCUMENTATION-COMPLETE.md

> │        ├── 📄 FRONTEND-DOCUMENTATION-SUMMARY.md

> │        ├── 📄 README.md

> │    └── 📂 frontend/

> │      ├── 📄 Dockerfile

> │      ├── 📄 README.md

> │      ├── 📄 next.config.js

> │      ├── 📄 package.json

> │      ├── 📄 postcss.config.js

> │      └── 📂 public/

> │        ├── 📄 README.md

> │      └── 📂 src/

> │        └── 📂 app/

> │          └── 📂 chat/

> │            └── 📂 [sessionId]/

> │              ├── 📄 page.tsx

> │          ├── 📄 globals.css

> │          ├── 📄 layout.tsx

> │          ├── 📄 page.tsx

> │          └── 📂 results/

> │            └── 📂 [sessionId]/

> │              ├── 📄 page.tsx

> │          └── 📂 upload/

> │            ├── 📄 page.tsx

> │        └── 📂 components/

> │          ├── 📄 MessageBubble.tsx

> │          ├── 📄 StageProgress.tsx

> │        └── 📂 lib/

> │          ├── 📄 api.ts

> │          ├── 📄 utils.ts

> │          ├── 📄 websocket-native.ts

> │        └── 📂 types/

> │          ├── 📄 index.ts

> │      ├── 📄 tailwind.config.ts

> │      ├── 📄 tsconfig.json

> │    └── 📂 infrastructure/

> │      └── 📂 bigquery/

> │        ├── 📄 add_criminal_offences.py

> │        ├── 📄 add_marriage_laws.py

> │        ├── 📄 add_marriage_relationship_laws.py

> │        ├── 📄 add_more_ipc_sections.py

> │        ├── 📄 add_murder_related_laws.py

> │        ├── 📄 add_property_offences.py

> │        ├── 📄 add_relationship_laws.py

> │        ├── 📄 add_serious_crimes.py

> │        ├── 📄 add_traffic_laws.py

> │        ├── 📄 add_us_laws.py

> │        ├── 📄 comprehensive_laws.sql

> │        ├── 📄 populate_comprehensive_laws.py

> │        ├── 📄 populate_data.py

> │        ├── 📄 sample_data.sql

> │        ├── 📄 schema.sql

> │        ├── 📄 verify_all_laws.sh

> │        ├── 📄 verify_database.py

> │      └── 📂 cloud-run/

> │        ├── 📄 deploy.sh

> │        ├── 📄 service-template.yaml

> │      ├── 📄 deploy_all.sh

> │      └── 📂 firestore/

> │        ├── 📄 firestore.rules

> │        ├── 📄 schema.md

> │  └── 📂 vitepress/

> │    └── 📂 docs/

> │      └── 📂 _outputs/

> │        └── 📂 vis/

> │          ├── 📄 claims_map.json

> │          ├── 📄 index.md

> │          ├── 📄 manifest.csv

> │          ├── 📄 manifest.json

> │          ├── 📄 search_index.json

> │          └── 📂 site/

> │            └── 📂 A_TIMELINE/

> │              └── 📂 2023/

> │                ├── 📄 index.html

> │              └── 📂 2024/

> │                ├── 📄 index.html

> │              └── 📂 2025/

> │                └── 📂 events/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 2026/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 B_EVIDENCE/

> │              └── 📂 10_evidence_admin/

> │                ├── 📄 index.html

> │              └── 📂 20_court_record/

> │                └── 📂 10_docket_files/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 30_primary/

> │                └── 📂 aes/

> │                  ├── 📄 index.html

> │                └── 📂 fcfcu/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 40_supporting/

> │                └── 📂 docs/

> │                  └── 📂 affidavits/

> │                    ├── 📄 index.html

> │                  └── 📂 declarations/

> │                    ├── 📄 index.html

> │                  └── 📂 receipts/

> │                    ├── 📄 index.html

> │                  └── 📂 records/

> │                    ├── 📄 index.html

> │                ├── 📄 index.html

> │                └── 📂 multi-media/

> │                  ├── 📄 index.html

> │                └── 📂 property/

> │                  └── 📂 10_mortgage_history/

> │                    └── 📂 10_payments/

> │                      ├── 📄 index.html

> │                  └── 📂 20_parcel/

> │                    ├── 📄 index.html

> │              └── 📂 50_quarantine_candidates/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 C_VIS/

> │              └── 📂 10_violations/

> │                ├── 📄 index.html

> │              └── 📂 20_theories/

> │                ├── 📄 index.html

> │              └── 📂 30_legal_research/

> │                ├── 📄 index.html

> │              └── 📂 40_analysis/

> │                ├── 📄 index.html

> │              └── 📂 50_strategies/

> │                ├── 📄 index.html

> │              └── 📂 60_data_inventories/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 D_PHASES/

> │              └── 📂 100_post_judgment_and_federal/

> │                └── 📂 10_motions/

> │                  └── 📂 10_claims_motions/

> │                    └── 📂 Supplemental/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 index.html

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 index.html

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 index.html

> │                    └── 📂 filings/

> │                      └── 📂 10_2025-12-10_motion_vacate/

> │                        └── 📂 01_drafts/

> │                          ├── 📄 index.html

> │                        └── 📂 02_exhibits/

> │                          ├── 📄 index.html

> │                        └── 📂 03_proposed_order/

> │                          ├── 📄 index.html

> │                        └── 📂 04_filed_receipts/

> │                          ├── 📄 index.html

> │                        ├── 📄 index.html

> │                      └── 📂 20_2025-12-11_Supplemental_Emergency_Motion_Access/

> │                        └── 📂 01_drafts/

> │                          ├── 📄 index.html

> │                        └── 📂 02_exhibits/

> │                          ├── 📄 index.html

> │                        └── 📂 04_filed_receipts/

> │                          ├── 📄 index.html

> │                        ├── 📄 index.html

> │                      └── 📂 30_draft_motions/

> │                        ├── 📄 index.html

> │                        └── 📂 motions/

> │                          ├── 📄 index.html

> │                    ├── 📄 index.html

> │                    └── 📂 motion_vacate/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 index.html

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 index.html

> │                      └── 📂 03_proposed_order/

> │                        ├── 📄 index.html

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 index.html

> │                      ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 20_orders/

> │                  └── 📂 10_proposed_orders/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                  └── 📂 orders/

> │                    ├── 📄 index.html

> │                └── 📂 30_regulatory_complaints/

> │                  ├── 📄 index.html

> │                └── 📂 40_federal_preservation/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 10_inbox_working/

> │                └── 📂 _staging/

> │                  └── 📂 _dupes_hold/

> │                    ├── 📄 index.html

> │                  └── 📂 _html_hold/

> │                    ├── 📄 index.html

> │                └── 📂 evidence_staging/

> │                  └── 📂 exhibit_candidates/

> │                    └── 📂 10_exposure_and_harm/

> │                      ├── 📄 index.html

> │                      └── 📂 weather_reports/

> │                        ├── 📄 index.html

> │                    ├── 📄 index.html

> │                  └── 📂 potential_exhibits/

> │                    ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 20_pre_foreclosure/

> │                └── 📂 10_account_history/

> │                  ├── 📄 index.html

> │                └── 📂 20_hardship_and_ada/

> │                  ├── 📄 index.html

> │                └── 📂 30_communications/

> │                  ├── 📄 index.html

> │                └── 📂 40_payments_and_disputes/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 30_foreclosure_filing/

> │                └── 📂 10_complaint/

> │                  ├── 📄 index.html

> │                └── 📂 20_summons/

> │                  ├── 📄 index.html

> │                └── 📂 30_lien_parties/

> │                  ├── 📄 index.html

> │                └── 📂 40_docket_snapshots/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 40_service_and_notice/

> │                └── 📂 10_sheriff_returns/

> │                  ├── 📄 index.html

> │                └── 📂 20_mailings/

> │                  ├── 📄 index.html

> │                └── 📂 30_affidavits_of_service/

> │                  └── 📂 10_jurisdiction_service_tr_4_1_b/

> │                    ├── 📄 index.html

> │                  └── 📂 20_service_process/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 40_defects_and_contradictions/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 50_default_and_judgment/

> │                └── 📂 10_default_motion/

> │                  ├── 📄 index.html

> │                └── 📂 20_default_order/

> │                  ├── 📄 index.html

> │                └── 📂 30_judgment_and_decree/

> │                  ├── 📄 index.html

> │                └── 📂 40_accounting_inputs/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 60_sale_and_title/

> │                └── 📂 10_sheriff_sale/

> │                  ├── 📄 index.html

> │                └── 📂 20_deed/

> │                  ├── 📄 index.html

> │                └── 📂 30_recording_gaps/

> │                  ├── 📄 index.html

> │                └── 📂 40_possession_claims/

> │                  └── 📂 10_sale_and_possession/

> │                    ├── 📄 index.html

> │                  └── 📂 30_void_vs_voidable/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 70_writ_and_execution/

> │                └── 📂 10_writ_petition/

> │                  ├── 📄 index.html

> │                └── 📂 20_writ_order/

> │                  ├── 📄 index.html

> │                └── 📂 30_execution_events/

> │                  ├── 📄 index.html

> │                └── 📂 40_notice_failures/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 80_post_removal_conduct/

> │                └── 📂 10_property_interference/

> │                  ├── 📄 index.html

> │                └── 📂 20_access_denial/

> │                  ├── 📄 index.html

> │                └── 📂 30_spoliation_risk/

> │                  ├── 📄 index.html

> │                └── 📂 40_third_party_actions/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 90_damages_and_fallout/

> │                └── 📂 10_property_possession_harms/

> │                  ├── 📄 index.html

> │                └── 📂 20_economic_harm/

> │                  ├── 📄 index.html

> │                └── 📂 30_financial/

> │                  ├── 📄 index.html

> │                └── 📂 40_health_and_safety/

> │                  ├── 📄 index.html

> │                └── 📂 50_non_economic_harm/

> │                  └── 📂 cold_exposure/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 60_professional_harm/

> │                  ├── 📄 index.html

> │                └── 📂 70_remedies_scenarios/

> │                  ├── 📄 index.html

> │                └── 📂 80_payout_strategy/

> │                  ├── 📄 index.html

> │                └── 📂 90_third_party_harm/

> │                  ├── 📄 index.html

> │                └── 📂 Weather_Reports/

> │                  ├── 📄 index.html

> │                └── 📂 economic/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │                └── 📂 non-economic/

> │                  └── 📂 cold-exposure/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 personal_narrative/

> │                  └── 📂 10_Public_Narrative/

> │                    ├── 📄 index.html

> │                  └── 📂 20_Exposure_and_Harm/

> │                    └── 📂 Weather_Reports/

> │                      ├── 📄 index.html

> │                    ├── 📄 index.html

> │                  └── 📂 30_Internal_Analysis/

> │                    └── 📂 Payout_Strategy/

> │                      ├── 📄 index.html

> │                    └── 📂 Premonitions/

> │                      ├── 📄 index.html

> │                    ├── 📄 index.html

> │                  └── 📂 40_Donations_and_Support/

> │                    ├── 📄 index.html

> │                  └── 📂 50_Timeline/

> │                    ├── 📄 index.html

> │                  └── 📂 Premonitions/

> │                    ├── 📄 index.html

> │                └── 📂 settlement/

> │                  ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 E_OUTPUTS/

> │              └── 📂 10_binders/

> │                └── 📂 master_case_bible/

> │                  └── 📂 _build/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │              └── 📂 _build_artifacts/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │              └── 📂 vis/

> │                ├── 📄 index.html

> │            └── 📂 _ADMIN/

> │              └── 📂 10_index/

> │                ├── 📄 index.html

> │              └── 📂 20_case_logs/

> │                ├── 📄 index.html

> │              └── 📂 30_financial/

> │                ├── 📄 index.html

> │              └── 📂 40_overviews/

> │                └── 📂 10_maps/

> │                  ├── 📄 index.html

> │                └── 📂 20_deep_dives/

> │                  ├── 📄 index.html

> │                └── 📂 40_debates/

> │                  ├── 📄 index.html

> │                └── 📂 50_explainers/

> │                  ├── 📄 index.html

> │                └── 📂 60_infographics/

> │                  ├── 📄 index.html

> │                └── 📂 70_reports/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 50_protocols/

> │                ├── 📄 index.html

> │              └── 📂 70_templates/

> │                └── 📂 10_motions/

> │                  ├── 📄 index.html

> │                └── 📂 20_declarations/

> │                  ├── 📄 index.html

> │                └── 📂 30_exhibits/

> │                  ├── 📄 index.html

> │                └── 📂 40_orders/

> │                  ├── 📄 index.html

> │                └── 📂 50_internal/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 80_integrity_tooling/

> │                ├── 📄 index.html

> │              └── 📂 90_pack_blueprints/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │      ├── 📄 example.md

> │      ├── 📄 index.md

> │      └── 📂 public/

> │        └── 📂 vis-assets/

> │          └── 📂 A_TIMELINE/

> │            └── 📂 2023/

> │              ├── 📄 NT_index.md

> │            └── 📂 2024/

> │              ├── 📄 NT_index.md

> │            └── 📂 2025/

> │              ├── 📄 NT_index.md

> │              └── 📂 events/

> │                ├── 📄 MO_2025-05-13_Motion_for_Default_Judgment 1.md

> │                ├── 📄 MO_2025-05-13_Motion_for_Default_Judgment.md

> │                ├── 📄 MO_2025-05-23_Amended_Motion_Default_Judgment 1.md

> │                ├── 📄 MO_2025-05-23_Amended_Motion_Default_Judgment.md

> │                ├── 📄 MO_2025-12-10_Motions_Filed 1.md

> │                ├── 📄 MO_2025-12-10_Motions_Filed.md

> │                ├── 📄 MO_2025-12-12_Supplemental_Emergency_Motion 1.md

> │                ├── 📄 MO_2025-12-12_Supplemental_Emergency_Motion.md

> │                ├── 📄 NT_2025-01-16_Case_Filed 1.md

> │                ├── 📄 NT_2025-01-16_Case_Filed.md

> │                ├── 📄 NT_2025-03-05_Service_Attempt_1 1.md

> │                ├── 📄 NT_2025-03-05_Service_Attempt_1.md

> │                ├── 📄 NT_2025-04-15_Service_Attempt_2 1.md

> │                ├── 📄 NT_2025-04-15_Service_Attempt_2.md

> │                ├── 📄 NT_2025-08-15_Sheriff_Sale 1.md

> │                ├── 📄 NT_2025-08-15_Sheriff_Sale.md

> │                ├── 📄 NT_2025-11-06_Writ_of_Assistance_Issued 1.md

> │                ├── 📄 NT_2025-11-06_Writ_of_Assistance_Issued.md

> │                ├── 📄 NT_2025-12-09_Writ_Executed_Forced_Removal.md

> │                ├── 📄 NT_2025-12-09_Writ_Executed_Removal.md

> │                ├── 📄 NT_2025-12-16_Post_Removal_Access_Denial.md

> │                ├── 📄 NT_2025-12-21_Case_Summary.md

> │                ├── 📄 OR_2025-05-21_Order_Denying_Default_Judgment 1.md

> │                ├── 📄 OR_2025-05-21_Order_Denying_Default_Judgment.md

> │                ├── 📄 OR_2025-05-28_Default_Judgment_Entered 1.md

> │                ├── 📄 OR_2025-05-28_Default_Judgment_Entered.md

> │                ├── 📄 OR_2025-12-11_Court_Orders_and_Hearing_Scheduled 1.md

> │                ├── 📄 OR_2025-12-11_Court_Orders_and_Hearing_Scheduled.md

> │                ├── 📄 PL_2025-05-30_Praecipe_Sheriff_Sale 1.md

> │                ├── 📄 PL_2025-05-30_Praecipe_Sheriff_Sale.md

> │                ├── 📄 PL_2025-07-09_Sheriff_Sale_Notice_Posted 1.md

> │                ├── 📄 PL_2025-07-09_Sheriff_Sale_Notice_Posted.md

> │                ├── 📄 PL_2025-10-29_Petition_for_Writ_of_Assistance 1.md

> │                ├── 📄 PL_2025-10-29_Petition_for_Writ_of_Assistance.md

> │            └── 📂 2026/

> │              ├── 📄 NT_index.md

> │            ├── 📄 _A_TIMELINE.md

> │          └── 📂 B_EVIDENCE/

> │            └── 📂 10_evidence_admin/

> │              ├── 📄 00_evidence_admin.md

> │              ├── 📄 EXH_Raw_Exhibit_Map.md

> │              ├── 📄 Evidence_Log.md

> │              ├── 📄 master_evidence_index.md

> │            └── 📂 20_court_record/

> │              ├── 📄 10_court_record.md

> │              └── 📂 10_docket_files/

> │                ├── 📄 022_Plaintif_bid_2025_07_17_10_14_40.pdf.pdf

> │                ├── 📄 024_Service Returned Served.pdf

> │                ├── 📄 026_2025_10_29_13_47_03.pdf.pdf

> │                ├── 📄 029_Emergency_Supplemental_Declara.pdf

> │                ├── 📄 035_01092026_005.pdf.pdf

> │                ├── 📄 EXH_026_Exhibit_List_A-G.pdf

> │                ├── 📄 EXH__026_Exhibit_List_A-G.pdf

> │                ├── 📄 MO_013_Motion_for_Default_Judgment.pdf

> │                ├── 📄 MO_016_Order_Denying_Motion_for_Default_Judgment.pdf

> │                ├── 📄 MO_019_Amended_Motion_Default_Judgment_1.pdf

> │                ├── 📄 MO_020_Amended_Motion_Default_Judgment_2.pdf

> │                ├── 📄 MO_025_Motion_Vacate_Stay_Writ.pdf

> │                ├── 📄 MO_027_Supplemental_Motion_Access.pdf

> │                ├── 📄 MO__013_Motion_for_Default_Judgment.pdf

> │                ├── 📄 MO__019_Amended_Motion_Default_Judgmen.pdf

> │                ├── 📄 MO__020_Amended_Motion_Default_Judgmen.pdf

> │                ├── 📄 MO__025_Motion_Vacate_Stay_Writ.pdf

> │                ├── 📄 MO__027_Supplemental_Motion_Access.pdf

> │                ├── 📄 OR_023_Decree_Foreclosure_Returned.pdf

> │                ├── 📄 OR_031_Proposed_Order_Vacate.pdf

> │                ├── 📄 OR_032_Proposed_Order_Stay.pdf

> │                ├── 📄 OR__017_Order_Denying_Default_Judgment.pdf

> │                ├── 📄 OR__023_Decree_Foreclosure_Returned.pdf

> │                ├── 📄 OR__031_Proposed_Order_Vacate.pdf

> │                ├── 📄 OR__032_Proposed_Order_Stay.pdf

> │                ├── 📄 PL_001_Complaint.pdf

> │                ├── 📄 PL_002_Appearance.pdf

> │                ├── 📄 PL_003_Request_for_Admissions.pdf

> │                ├── 📄 PL_004_Notice_to_Homeowners.pdf

> │                ├── 📄 PL_005_Appearance_2.pdf

> │                ├── 📄 PL_006_Summons_1.pdf

> │                ├── 📄 PL_007_Summons_2.pdf

> │                ├── 📄 PL_008_Summons_3.pdf

> │                ├── 📄 PL_009_Summons_4.pdf

> │                ├── 📄 PL_010_Summons_5.pdf

> │                ├── 📄 PL_011_Service_Returned_03-05-2025.pdf

> │                ├── 📄 PL_012_Service_Returned_04-15-2025.pdf

> │                ├── 📄 PL_014_Affidavit.pdf

> │                ├── 📄 PL_015_Affidavit_Attorney_Fees.pdf

> │                ├── 📄 PL_017_OMITTED NOTICE OF SERVICE TO DEFENDANT.pdf

> │                ├── 📄 PL_018_Omitted_Notice_of_Service.pdf

> │                ├── 📄 PL_021_Praecipe_Sheriff_Sale_1.pdf

> │                ├── 📄 PL_022_Praecipe_Sheriff_Sale_2.pdf

> │                ├── 📄 PL_024_Petition_Writ_of_Assistance.pdf

> │                ├── 📄 PL_028_Report_Court_Defendant_Request.pdf

> │                ├── 📄 PL_029_Emergency_Supplemental_Declaration.pdf

> │                ├── 📄 PL_030_Report_Sheriff_Sale_No_Excess.pdf

> │                ├── 📄 PL_033_ADA_Disability_Affidavit.pdf

> │                ├── 📄 PL_2026-01-09_Appearance_Plaintiff.pdf

> │                ├── 📄 PL__001_Complaint.pdf

> │                ├── 📄 PL__002_Appearance.pdf

> │                ├── 📄 PL__003_Request_for_Admissions.pdf

> │                ├── 📄 PL__004_Notice_to_Homeowners.pdf

> │                ├── 📄 PL__005_Appearance_2.pdf

> │                ├── 📄 PL__006_Summons_1.pdf

> │                ├── 📄 PL__007_Summons_2.pdf

> │                ├── 📄 PL__008_Summons_3.pdf

> │                ├── 📄 PL__009_Summons_4.pdf

> │                ├── 📄 PL__010_Summons_5.pdf

> │                ├── 📄 PL__011_Service_Returned_03-05-2025.pdf

> │                ├── 📄 PL__012_Service_Returned_04-15-2025.pdf

> │                ├── 📄 PL__014_Affidavit.pdf

> │                ├── 📄 PL__015_Affidavit_Attorney_Fees.pdf

> │                ├── 📄 PL__016_Affidavit_Additional.pdf

> │                ├── 📄 PL__018_Omitted_Notice_of_Service.pdf

> │                ├── 📄 PL__021_Praecipe_Sheriff_Sale_1.pdf

> │                ├── 📄 PL__022_Praecipe_Sheriff_Sale_2.pdf

> │                ├── 📄 PL__024_Petition_Writ_of_Assistance.pdf

> │                ├── 📄 PL__028_Report_Court_Defendant_Request.pdf

> │                ├── 📄 PL__030_Report_Sheriff_Sale_No_Excess.pdf

> │                ├── 📄 PL__033_ADA_Disability_Affidavit.pdf

> │            └── 📂 30_primary/

> │              ├── 📄 10_primary.md

> │              ├── 📄 20_primary.md

> │              └── 📂 aes/

> │                ├── 📄 2025-06-08_aes_ada_request_financial_hardship_.pdf

> │                ├── 📄 PL_2025-06-08_aes_ada_notice.pdf

> │                ├── 📄 PL_2025-12-16_AES_Emergency_Notice.md

> │                ├── 📄 _README.md

> │              └── 📂 fcfcu/

> │                ├── 📄 2023-09-20_FCFCU_Hardship_and_Healt.md

> │                ├── 📄 2024-03-20_fcfcu_certified_response_tax_record.pdf

> │                ├── 📄 2024-12-09_outgoing_email_bank_access_request.pdf

> │                ├── 📄 2024-12-11_outgoing_email_bank_access_request.pdf

> │                ├── 📄 20241204_FCFCU_Statement (1).pdf

> │                ├── 📄 20241204_FCFCU_Statement (2).pdf

> │                ├── 📄 20241204_fcfcu_statement-(1).pdf

> │                ├── 📄 20241204_fcfcu_statement-(2).pdf

> │                ├── 📄 20241204_fcfcu_statement.pdf

> │                ├── 📄 2025-12-20_exh-30_fcfcu_740eacdc_2025-12-20_ex.jpg

> │                ├── 📄 2025-12-20_exh-30_fcfcu_ac6eb2ea_2025-12-20_ex.jpg

> │                ├── 📄 21june-24-4817shadow_appraisal.pdf

> │                ├── 📄 PL_2023-09-20_FCFCU_Hardship_and_Health_Notice_Let.md

> │                ├── 📄 PL_2023-09-20_fcfcu_hardship_and_health_notice_le.pdf

> │                ├── 📄 PL_2023-09-20_notice_disabilities_hardship.pdf

> │                ├── 📄 PL_2024-20-03_response_to_tax_notice.pdf

> │                ├── 📄 PL_fcfcu_v_cr-v_report_to_court.pdf

> │                ├── 📄 PL_report_to_court_on_defendants_request.pdf

> │                ├── 📄 _README.md

> │            └── 📂 40_supporting/

> │              ├── 📄 20_supporting.md

> │              ├── 📄 30_supporting.md

> │              └── 📂 docs/

> │                └── 📂 affidavits/

> │                  ├── 📄 PL_affidavits.md

> │                └── 📂 declarations/

> │                  ├── 📄 PL_declarations.md

> │                └── 📂 receipts/

> │                  ├── 📄 NT_2025-12-20_exh-20_receipts_0860d3df_2025-12-20.jpg

> │                  ├── 📄 NT_Odyssey_Envelope_Receipt.pdf

> │                └── 📂 records/

> │                  ├── 📄 Foreclosure and Housing Litigation Case Record.csv

> │                  ├── 📄 Inventory of Civil and Fair Housing Rights Vio.csv

> │              └── 📂 multi-media/

> │                ├── 📄 2025-12-20_exh-10_photos_video_00241326_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_012aa06e_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_01b3e905_2025-1.png

> │                ├── 📄 2025-12-20_exh-10_photos_video_10f4975d_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_1a80b987_2025-1.mp4

> │                ├── 📄 2025-12-20_exh-10_photos_video_1beefb11_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_1f3f8a81_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_25fb1992_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_2f0952db_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_49c74ec6_2025-.heic

> │                ├── 📄 2025-12-20_exh-10_photos_video_4e01fa01_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_5be451ba_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_5d95cae5_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_61129253_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_63fb7b02_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_71c9e6a7_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_78ba1ccc_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_7a544ef7_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_8350e7be_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_8a163413_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_8d885a5c_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_942cfd7f_2025-1.png

> │                ├── 📄 2025-12-20_exh-10_photos_video_9b611100_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_9fb3a08a_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_9ff5022d_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_a8832e17_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_ca02d006_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_db9b10b5_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_e4cb3622_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_ebaaa38d_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_ed6dc885_2025-1.mp4

> │                ├── 📄 2025-12-20_exh-10_photos_video_f510498b_2025-.heic

> │                ├── 📄 2025-12-20_exh-10_photos_video_f60d8098_2025-1.png

> │                ├── 📄 2025-12-20_exh-10_photos_video_f98b089a_2025-1.png

> │                ├── 📄 2025-12-20_exh-10_photos_video_fa1703bf_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_fdd8d4ef_2025-1.jpg

> │              └── 📂 property/

> │                └── 📂 10_mortgage_history/

> │                  └── 📂 10_payments/

> │                    ├── 📄 2025-12-20_EXH-20_payments_c5131deb_2025-12-20.png

> │                    ├── 📄 2025-12-20_exh-20_payments_c5131deb_2025-12-20 (2).png

> │                    ├── 📄 20_payments.md

> │                └── 📂 20_parcel/

> │                  ├── 📄 Parcel_6016506_PRC.pdf

> │                  ├── 📄 Parcel_6016506_ParcelDetailHistory.pdf

> │                  ├── 📄 parcel_6016506_parceldetailhistory (2).pdf

> │                  ├── 📄 parcel_6016506_prc (2).pdf

> │            └── 📂 50_quarantine_candidates/

> │              ├── 📄 90_quarantine_candidates.md

> │            ├── 📄 _B_EVIDENCE.md

> │          └── 📂 C_VIS/

> │            └── 📂 10_violations/

> │              ├── 📄 EXH_Exhibit X — Inventory of Jurisdictional, Execut.md

> │              ├── 📄 NT_V-005_failure-to-correct-inaccurate-furnishings.md

> │              ├── 📄 NT_V-006_dual-tradeline-double-counting.md

> │              ├── 📄 NT_V-008_credit-defamation-false-publication.md

> │              ├── 📄 NT_V-009_fdCPA-misrepresentation-of-debt-status.md

> │              ├── 📄 NT_V-010_failure-to-mark-account-foreclosure-closed.md

> │              ├── 📄 NT_V-011_experian-reinvestigation-failure.md

> │              ├── 📄 NT_V-012_equifax-reinvestigation-failure.md

> │              ├── 📄 NT_V-013_transunion-reinvestigation-failure.md

> │              ├── 📄 NT_V-020_post-0815-aes-electric-charges-billed.md

> │              ├── 📄 NT_V-021_post-0815-citizens-energy-charges-billed.md

> │              ├── 📄 NT_V-022_post-0815-hoa-assessments-billed.md

> │              ├── 📄 NT_V-023_city-grass-cut-ticket-assessed-after-loss-of-access.md

> │              ├── 📄 NT_V-024_municipal-code-enforcement-after-possession-transfer.md

> │              ├── 📄 NT_V-025_cost-shift-fcfcu-refused-winterize.md

> │              ├── 📄 NT_V-026_credit-harm-compounded-utility-municipal.md

> │              ├── 📄 NT_V-031_sheriff-return-inaccuracies.md

> │              ├── 📄 NT_V-033_removal-6-7-days-after-deed-recorded.md

> │              ├── 📄 NT_V-035_court-relied-on-service-sufficiency.md

> │              ├── 📄 NT_V-036_surplus-funds-declared-resolved.md

> │              ├── 📄 NT_V-037_interest-fees-arbitrarily-inflated.md

> │              ├── 📄 NT_V-038_fcfcu-testimony-winterize-then-leave.md

> │              ├── 📄 NT_V-070_global-demand-letter.md

> │              ├── 📄 NT_V-071_litigation-hold-preservation-letter.md

> │              ├── 📄 NT_V-072_equitable-relief-tradeline-deletion.md

> │              ├── 📄 NT_V-073_damages-credit-score-suppression.md

> │              ├── 📄 NT_V-074_damages-out-of-pocket-costs.md

> │              ├── 📄 NT_V-075_public-accountability-hold.md

> │              ├── 📄 NT_V-076_fha-reasonable-accommodation-failure.md

> │              ├── 📄 NT_V-077_ada-title-iii-entertainment-access-failure.md

> │              ├── 📄 NT_V-078_ada-effective-communication-failure.md

> │              ├── 📄 NT_V-080_conversion-negligence-post-removal-damage.md

> │              ├── 📄 NT_V-081_evidence-spoliation-unplugged-cameras.md

> │              ├── 📄 NT_V-082_fraud-on-the-court-material-misrepresentation.md

> │              ├── 📄 NT_V-083_discriminatory-maintenance-redlining.md

> │              ├── 📄 NT_V-084_predatory-land-contract-reverse-redlining.md

> │              ├── 📄 OR_V-001_fcfcu-continues-reporting-first-mortgage-post-judgment-sale.md

> │              ├── 📄 OR_V-002_fcfcu-continues-reporting-second-mortgage-post-judgment-sale.md

> │              ├── 📄 OR_V-003_monthly-delinquencies-after-foreclosure-judgment.md

> │              ├── 📄 OR_V-004_past-due-amount-schedule-after-judgment.md

> │              ├── 📄 OR_V-079_void-judgment-procedural-error.md

> │              ├── 📄 PL_V-007_inconsistent-reporting-vs-court-position.md

> │              ├── 📄 PL_V-030_service-completed-no-notice-before-writ.md

> │              ├── 📄 PL_V-032_no-ada-compliant-notice.md

> │              ├── 📄 PL_V-034_attorney-appeared-without-formal-appearance.md

> │              ├── 📄 PL_V-050_cfpb-complaint-track.md

> │              ├── 📄 PL_V-051_indiana-ag-complaint-track.md

> │              ├── 📄 PL_V-052_icrc-complaint-track.md

> │              ├── 📄 PL_V-053_doj-civil-rights-complaint-track.md

> │              ├── 📄 PL_V-060_bbb-complaint-reputational-pressure.md

> │            └── 📂 20_theories/

> │              ├── 📄 NT_BACKUP_ARGUMENTS.md

> │              ├── 📄 NT_IF_JUDGE_PUSHBACK.md

> │            └── 📂 30_legal_research/

> │              ├── 📄 NT_CASE_LAW_RESEARCH.md

> │              ├── 📄 NT_JURISDICTION_THEORY.md

> │              ├── 📄 NT_LEGAL MEMORANDUM.md

> │              ├── 📄 NT_VOID_VS_VOIDABLE_ANALYSIS.md

> │            └── 📂 40_analysis/

> │              ├── 📄 NT_INTERNAL VALUATION MEMO.md

> │              ├── 📄 NT_Procedural_failure_map_one_pager.md

> │              ├── 📄 NT_Violation_Remedy_Inventory.md

> │            └── 📂 50_strategies/

> │              ├── 📄 NT_00_basis.md

> │              ├── 📄 NT_10_ada_strategy.md

> │              ├── 📄 NT_ADA_TITLE_II_ANALYSIS.md

> │              ├── 📄 NT_BUT_FOR_ANALYSIS.md

> │              ├── 📄 NT_Master_Strategy_Canvas.canvas

> │              ├── 📄 NT_PROCEDURAL_FAILURE_MAP.md

> │              ├── 📄 NT_REASONABLE_ACCOMMODATIONS.md

> │              ├── 📄 NT_REVERSAL_PATHS.md

> │              ├── 📄 NT_STATUS_TRACKER.md

> │              ├── 📄 NT_STAY_PATHS.md

> │              ├── 📄 NT_integrate_disability_separate_appe.m4a

> │              ├── 📄 OR_void_judgment_eviction_crisis.pdf

> │              ├── 📄 PL_DOJ_COMPLAINT.md

> │              ├── 📄 PL_ICRC_COMPLAINT.md

> │              ├── 📄 PL_Proposal for Strategic Reports in the Matter of.md

> │              ├── 📄 Strategic_Plan.canvas

> │            └── 📂 60_data_inventories/

> │              ├── 📄 NT_Violation_Index.md

> │              ├── 📄 NT_foreclosure-and-housing-litigation-case-record.csv

> │              ├── 📄 NT_inventory-of-civil-and-fair-housing-rights-vio.csv

> │            ├── 📄 NT_01_MASTER_INDEX.md

> │            ├── 📄 _C_VIS.md

> │            ├── 📄 vis.yaml

> │          ├── 📄 Case_Data.base

> │          └── 📂 D_PHASES/

> │            └── 📂 100_post_judgment_and_federal/

> │              └── 📂 10_motions/

> │                └── 📂 10_claims_motions/

> │                  ├── 📄 40_claims_motions.md

> │                  ├── 📄 MO_40_claims_motions.md

> │                  └── 📂 Supplemental/

> │                    └── 📂 01_drafts/

> │                      ├── 📄 MO__Supplemental_Emergency_Motion.pdf

> │                    └── 📂 02_exhibits/

> │                      ├── 📄 EXH_02_exhibits.md

> │                      ├── 📄 EXH__20_exhibits_combined_source

> │                      ├── 📄 EXH__Exhibit_H_Declaration.pdf

> │                    └── 📂 04_filed_receipts/

> │                      ├── 📄 NT__Odyssey_Envelope_Receipt.pdf

> │                  └── 📂 filings/

> │                    └── 📂 10_2025-12-10_motion_vacate/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 MO_Emergency Motions.docx

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 EXH_02_exhibits.md

> │                        ├── 📄 EXH_05_Exhibit_List.pdf

> │                        ├── 📄 EXH_06_Exhibits_Combined.pdf

> │                        ├── 📄 MO_01_motion_vacate.pdf

> │                        ├── 📄 MO_02_emergency_motion_quash_stay.pdf

> │                        ├── 📄 NT_combinepdf.pdf

> │                        ├── 📄 OR_03_order_vacate_proposed.pdf

> │                        ├── 📄 OR_04_order_stay_writ_proposed.pdf

> │                      └── 📂 03_proposed_order/

> │                        ├── 📄 OR_03_proposed_order.md

> │                        ├── 📄 OR_Proposed_Order_Vacate.docx

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 NT_Odyssey_Envelope_Receipt.pdf

> │                      ├── 📄 MO_10_2025-12-10_motion_vacate.md

> │                    └── 📂 20_2025-12-11_Supplemental_Emergency_Motion_Access/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 MO_Supplemental_Emergency_Motion.pdf

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 EXH_02_exhibits.md

> │                        ├── 📄 EXH_20_exhibits_combined_source

> │                        ├── 📄 EXH_Exhibit_H_Declaration.pdf

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 NT_Odyssey_Envelope_Receipt.pdf

> │                      ├── 📄 MO_20_2025-12-11_Supplemental_Emergency_Motion_Access.md

> │                    └── 📂 30_draft_motions/

> │                      ├── 📄 10_draft_motions.md

> │                      ├── 📄 20_draft_motions.md

> │                      ├── 📄 MO_10_draft_motions.md

> │                      ├── 📄 MO_DRAFT_MOTION_VACATE.md

> │                      ├── 📄 MO__Motions.md

> │                      ├── 📄 MO__motion_emergency_stay_of_writ.md

> │                      ├── 📄 MO__motion_emergency_supplemental_motio.md

> │                      ├── 📄 MO__motion_to_vacate_void_judgment.md

> │                      ├── 📄 MO_motion_emergency_stay_of_writ.md

> │                      ├── 📄 MO_motion_emergency_supplemental_motion_ongoing_ha.md

> │                      ├── 📄 MO_motion_to_vacate_void_judgment.md

> │                      ├── 📄 MO_wc2.00.010__motion_emergency_stay_of_writ.docx

> │                      ├── 📄 MO_wc2.00.010__motion_emergency_supplemental_mot.docx

> │                      ├── 📄 MO_wc2.00.010__motion_to_vacate_void_judgement.docx

> │                      ├── 📄 NT_DRAFT_EMERGENCY_STAY.md

> │                      ├── 📄 NT_DRAFT_SUPPLEMENTAL.md

> │                      ├── 📄 NT_EMERGENCY_FILING_PACKET.md

> │                      ├── 📄 _README.md

> │                      └── 📂 motions/

> │                        ├── 📄 MO_01B_Motion_To_Vacate_Void_Judgment.pdf

> │                        ├── 📄 MO_C2.01.002_motion_vacate.pdf

> │                        ├── 📄 MO_C2.02.002_Emergency_Motion_Stay_OR_Quash.pdf

> │                        ├── 📄 MO_C2.03.002_Supplemental_Emergency_Motion.pdf

> │                        ├── 📄 MO_motions.md

> │                  └── 📂 motion_vacate/

> │                    └── 📂 01_drafts/

> │                      ├── 📄 MO__Emergency Motions.docx

> │                    └── 📂 02_exhibits/

> │                      ├── 📄 EXH_02_exhibits.md

> │                      ├── 📄 EXH__05_Exhibit_List.pdf

> │                      ├── 📄 EXH__06_Exhibits_Combined.pdf

> │                      ├── 📄 MO__01_motion_vacate.pdf

> │                      ├── 📄 MO__02_emergency_motion_quash_stay.pdf

> │                      ├── 📄 NT__combinepdf.pdf

> │                      ├── 📄 OR__03_order_vacate_proposed.pdf

> │                      ├── 📄 OR__04_order_stay_writ_proposed.pdf

> │                    └── 📂 03_proposed_order/

> │                      ├── 📄 OR_03_proposed_order.md

> │                      ├── 📄 OR__Proposed_Order_Vacate.docx

> │                    └── 📂 04_filed_receipts/

> │                      ├── 📄 NT__Odyssey_Envelope_Receipt.pdf

> │                    ├── 📄 MO_motion_vacate.md

> │                    ├── 📄 NT.gitkeep

> │                ├── 📄 MO_10_motions.md

> │                ├── 📄 NT_index.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_orders/

> │                └── 📂 10_proposed_orders/

> │                  ├── 📄 20_proposed_orders.md

> │                  ├── 📄 MO__proposed_order_motion_to_vacate.md

> │                  ├── 📄 MO_proposed_order_motion_to_vacate.md

> │                  ├── 📄 NT__index.md

> │                  ├── 📄 OR_20_proposed_orders.md

> │                  ├── 📄 OR_DRAFT_ORDER_STAY.md

> │                  ├── 📄 OR_DRAFT_ORDER_VACATE.md

> │                  ├── 📄 OR__Proposed_Orders.md

> │                  ├── 📄 OR__proposed_order_emergency_stay.md

> │                  ├── 📄 OR_proposed_order_emergency_stay.md

> │                  ├── 📄 _README.md

> │                ├── 📄 NT_index.md

> │                ├── 📄 OR_20_orders.md

> │                ├── 📄 _placeholder.md

> │                └── 📂 orders/

> │                  ├── 📄 OR_C2.04.001_order_vacate_proposed.pdf

> │                  ├── 📄 OR_C2.04.002_order_stay_writ_proposed.pdf

> │                  ├── 📄 OR_orders.md

> │              └── 📂 30_regulatory_complaints/

> │                ├── 📄 PL_30_regulatory_complaints.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_federal_preservation/

> │                ├── 📄 _placeholder.md

> │              ├── 📄 OR_90_post_judgment_and_federal.md

> │              ├── 📄 _README.md

> │            └── 📂 10_inbox_working/

> │              ├── 📄 NT_00_inbox_working.md

> │              ├── 📄 NT_index.md

> │              └── 📂 _staging/

> │                └── 📂 _dupes_hold/

> │                  ├── 📄 MO__motion_emergency_stay_of_writ (2).docx

> │                  ├── 📄 MO__motion_emergency_supplemental_mot (2).docx

> │                  ├── 📄 MO__motion_to_vacate_void_judgement (2).docx

> │                  ├── 📄 NT_2025-12-15_they_threw_us_into_the_cold (2).md

> │                  ├── 📄 NT_Donations_Context (2).md

> │                  ├── 📄 NT_Long_Term_Payout_Strategy (2).md

> │                  ├── 📄 NT_Master_Timeline (2).md

> │                  ├── 📄 NT_Premonitions_I_Knew_Before_I_Knew (2).md

> │                  ├── 📄 NT_Public_Statement (2).md

> │                  ├── 📄 NT_Session_Summary_2025-12-15_i_knew_before_i_knew (2).md

> │                  ├── 📄 NT_index.md

> │                  ├── 📄 OR_c2.04.001_order_vacate_proposed (2).pdf

> │                  ├── 📄 OR_c2.04.002_order_stay_writ_proposed (2).pdf

> │                  ├── 📄 PL_Cold_Risk_Report (2).md

> │                └── 📂 _html_hold/

> │                  ├── 📄 NT_index.md

> │              └── 📂 evidence_staging/

> │                └── 📂 exhibit_candidates/

> │                  └── 📂 10_exposure_and_harm/

> │                    ├── 📄 02_exposure_and_harm.md

> │                    ├── 📄 NT_02_exposure_and_harm.md

> │                    ├── 📄 PL_wi8.02.050__cold_risk_report.html

> │                    └── 📂 weather_reports/

> │                      ├── 📄 PL_weather_reports.md

> │                  ├── 📄 EXH_exhibit_candidates.md

> │                └── 📂 potential_exhibits/

> │                  ├── 📄 EXH_potential_exhibits.md

> │            └── 📂 20_pre_foreclosure/

> │              └── 📂 10_account_history/

> │                ├── 📄 NT_index.md

> │                ├── 📄 NT_one_pager_overview.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_hardship_and_ada/

> │                ├── 📄 _placeholder.md

> │              └── 📂 30_communications/

> │                ├── 📄 NT_index.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_payments_and_disputes/

> │                ├── 📄 _placeholder.md

> │              ├── 📄 NT_10_pre_foreclosure.md

> │              ├── 📄 _README.md

> │            └── 📂 30_foreclosure_filing/

> │              └── 📂 10_complaint/

> │                ├── 📄 PL_10_complaint.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_summons/

> │                ├── 📄 PL_20_summons.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 30_lien_parties/

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_docket_snapshots/

> │                ├── 📄 NT_01_Docket.md

> │                ├── 📄 NT__Case_Summary.md

> │                ├── 📄 NT_docket_index.md

> │                ├── 📄 _Case_Summary.md

> │                ├── 📄 _README.md

> │                ├── 📄 _docket.md

> │                ├── 📄 _placeholder.md

> │              ├── 📄 NT_20_foreclosure_filing.md

> │              ├── 📄 _README.md

> │            └── 📂 40_service_and_notice/

> │              └── 📂 10_sheriff_returns/

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_mailings/

> │                ├── 📄 _placeholder.md

> │              └── 📂 30_affidavits_of_service/

> │                └── 📂 10_jurisdiction_service_tr_4_1_b/

> │                  ├── 📄 20_jurisdiction_service_tr_4_1_b.md

> │                  ├── 📄 NT_20_jurisdiction_service_tr_4_1_b 1.md

> │                  ├── 📄 NT_20_jurisdiction_service_tr_4_1_b.md

> │                └── 📂 20_service_process/

> │                  ├── 📄 30_service_process.md

> │                ├── 📄 NT_03_Service_Process.md

> │                ├── 📄 NT_service_defects_analysis.md

> │                ├── 📄 PL_30_affidavits_of_service.md

> │                ├── 📄 PL_affidavits_service.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_defects_and_contradictions/

> │                ├── 📄 _placeholder.md

> │              ├── 📄 PL_30_service_and_notice.md

> │              ├── 📄 _README.md

> │            └── 📂 50_default_and_judgment/

> │              └── 📂 10_default_motion/

> │                ├── 📄 MO_10_default_motion.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_default_order/

> │                ├── 📄 OR_20_default_order.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 30_judgment_and_decree/

> │                ├── 📄 OR_30_judgment_and_decree.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_accounting_inputs/

> │                ├── 📄 _placeholder.md

> │              ├── 📄 OR_40_default_and_judgment.md

> │              ├── 📄 _README.md

> │            └── 📂 60_sale_and_title/

> │              └── 📂 10_sheriff_sale/

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_deed/

> │                ├── 📄 _placeholder.md

> │              └── 📂 30_recording_gaps/

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_possession_claims/

> │                └── 📂 10_sale_and_possession/

> │                  ├── 📄 30_sale_and_possession.md

> │                  ├── 📄 NT_30_sale_and_possession.md

> │                └── 📂 30_void_vs_voidable/

> │                  ├── 📄 20_void_vs_voidable.md

> │                  ├── 📄 NT_30_void_vs_voidable_tr_60b 1.md

> │                  ├── 📄 NT_30_void_vs_voidable_tr_60b.md

> │                ├── 📄 NT_05_Sale_and_Possesion.md

> │                ├── 📄 NT_possession_admissions.md

> │                ├── 📄 _placeholder.md

> │              ├── 📄 NT_50_sale_and_title.md

> │              ├── 📄 _README.md

> │            └── 📂 70_writ_and_execution/

> │              └── 📂 10_writ_petition/

> │                ├── 📄 PL_10_writ_petition.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_writ_order/

> │                ├── 📄 OR_20_writ_order.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 30_execution_events/

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_notice_failures/

> │                ├── 📄 PL_40_notice_failures.md

> │                ├── 📄 _placeholder.md

> │              ├── 📄 NT_60_writ_and_execution.md

> │              ├── 📄 _README.md

> │            └── 📂 80_post_removal_conduct/

> │              └── 📂 10_property_interference/

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_access_denial/

> │                ├── 📄 _placeholder.md

> │              └── 📂 30_spoliation_risk/

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_third_party_actions/

> │                ├── 📄 _placeholder.md

> │              ├── 📄 NT_70_post_removal_conduct.md

> │              ├── 📄 _README.md

> │            └── 📂 90_damages_and_fallout/

> │              └── 📂 10_property_possession_harms/

> │                ├── 📄 03_property_possession_harms.md

> │                ├── 📄 NT_03_property_possession_harms.md

> │              └── 📂 20_economic_harm/

> │                ├── 📄 10_economic_harm.md

> │                ├── 📄 NT_10_economic_harm.md

> │                ├── 📄 NT_index.md

> │              └── 📂 30_financial/

> │                ├── 📄 20_financial.md

> │                ├── 📄 NT_10_financial.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_health_and_safety/

> │                ├── 📄 30_health_and_safety.md

> │                ├── 📄 NT_20_health_and_safety.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 50_non_economic_harm/

> │                ├── 📄 40_non_economic_harm.md

> │                ├── 📄 NT_20_non_economic_harm.md

> │                └── 📂 cold_exposure/

> │                  ├── 📄 NT_index.md

> │              └── 📂 60_professional_harm/

> │                ├── 📄 50_professional_harm.md

> │                ├── 📄 NT_30_professional_harm.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 70_remedies_scenarios/

> │                ├── 📄 60_remedies_scenarios.md

> │                ├── 📄 NT_30_remedies_scenarios.md

> │                ├── 📄 NT_index.md

> │              └── 📂 80_payout_strategy/

> │                ├── 📄 70_payout_strategy.md

> │                ├── 📄 NT_40_Payout_Strategy.md

> │                ├── 📄 NT__Long_Term_Payout_Strategy.md

> │                ├── 📄 NT_index.md

> │                ├── 📄 _README.md

> │              └── 📂 90_third_party_harm/

> │                ├── 📄 80_third_party_harm.md

> │                ├── 📄 NT_40_third_party_harm.md

> │                ├── 📄 _placeholder.md

> │              ├── 📄 NT_06_damages_and_remedies.md

> │              ├── 📄 NT_80_damages_and_fallout.md

> │              ├── 📄 NT_index.md

> │              └── 📂 Weather_Reports/

> │                ├── 📄 PL_Weather_Reports.md

> │              ├── 📄 _README.md

> │              └── 📂 economic/

> │                ├── 📄 NT_ECONOMIC_HARM.md

> │              └── 📂 non-economic/

> │                ├── 📄 NT_NON_ECONOMIC_HARM.md

> │                └── 📂 cold-exposure/

> │                  ├── 📄 PL__Cold_Risk_Report.md

> │              └── 📂 personal_narrative/

> │                └── 📂 10_Public_Narrative/

> │                  ├── 📄 01_Public_Narrative.md

> │                  ├── 📄 NT_01_Public_Narrative.md

> │                  ├── 📄 NT_2025-12-15_they_threw_us_into_the_cold.md

> │                  ├── 📄 NT_Public_Statement.md

> │                  ├── 📄 _README.md

> │                └── 📂 20_Exposure_and_Harm/

> │                  ├── 📄 02_Exposure_and_Harm.md

> │                  ├── 📄 NT_02_Exposure_and_Harm.md

> │                  ├── 📄 PL_Cold_Risk_Report.md

> │                  └── 📂 Weather_Reports/

> │                    ├── 📄 PL_Weather_Reports.md

> │                  ├── 📄 _README.md

> │                └── 📂 30_Internal_Analysis/

> │                  ├── 📄 03_Internal_Analysis.md

> │                  ├── 📄 NT_03_Internal_Analysis.md

> │                  ├── 📄 NT_Session_Summary_2025-12-15_i_knew_before_i_knew.md

> │                  └── 📂 Payout_Strategy/

> │                    ├── 📄 NT_Long_Term_Payout_Strategy.md

> │                    ├── 📄 _README.md

> │                  └── 📂 Premonitions/

> │                    ├── 📄 NT_Premonitions_I_Knew_Before_I_Knew.md

> │                    ├── 📄 _README.md

> │                  ├── 📄 _README.md

> │                └── 📂 40_Donations_and_Support/

> │                  ├── 📄 04_Donations_and_Support.md

> │                  ├── 📄 NT_04_Donations_and_Support.md

> │                  ├── 📄 NT_Donations_Context.md

> │                  ├── 📄 _README.md

> │                └── 📂 50_Timeline/

> │                  ├── 📄 05_Timeline.md

> │                  ├── 📄 NT_05_Timeline.md

> │                  ├── 📄 NT_Master_Timeline.md

> │                  ├── 📄 _README.md

> │                └── 📂 Premonitions/

> │                  ├── 📄 NT__Premonitions_I_Knew_Before_I_Knew.md

> │                  ├── 📄 _README.md

> │              └── 📂 settlement/

> │                ├── 📄 NT_SETTLEMENT_SCENARIOS.md

> │            ├── 📄 MO_Promotion_Checklist.md

> │            ├── 📄 Strategic_Plan.canvas

> │            ├── 📄 _D_PHASES.md

> │          └── 📂 E_OUTPUTS/

> │            └── 📂 10_binders/

> │              └── 📂 master_case_bible/

> │                ├── 📄 NT_binder_manifest.md

> │                └── 📂 _build/

> │                  ├── 📄 NT_full_binder.md

> │                  ├── 📄 NT_full_binder_snapshot.md

> │                  ├── 📄 NT_master_case_bible.html

> │                  ├── 📄 NT_temp_merged.md

> │            ├── 📄 _E_OUTPUTS.md

> │            └── 📂 _build_artifacts/

> │              ├── 📄 MO_wc2.00.001_draft_motion_vacate.html

> │              ├── 📄 MO_wc2.00.010___motions.html

> │              ├── 📄 MO_wc2.00.010__motion_emergency_stay_of_writ.html

> │              ├── 📄 MO_wc2.00.010__motion_emergency_supplemental_mot.html

> │              ├── 📄 MO_wc2.00.010__motion_to_vacate_void_judgment.html

> │              ├── 📄 MO_wc2.01.010__proposed_order_motion_to_vacate.html

> │              ├── 📄 NT_2025-12-15_they_threw_us_into_the_cold.html

> │              ├── 📄 NT_Summary - MyCase.html

> │              ├── 📄 NT_WI8.01.050__index.html

> │              ├── 📄 NT_WI8.02.050__index.html

> │              ├── 📄 NT_WI8.99.010__index_MOVED.html

> │              ├── 📄 NT_WZ9.00.050__index.html

> │              ├── 📄 NT_WZ9.00.050__index_MOVED.html

> │              ├── 📄 NT__index (2).html

> │              ├── 📄 NT__index.html

> │              ├── 📄 NT__index_MOVED.html

> │              ├── 📄 NT_donations_context.html

> │              ├── 📄 NT_index (2).html

> │              ├── 📄 NT_index (2)_MOVED.html

> │              ├── 📄 NT_index-content.html

> │              ├── 📄 NT_index-content_MOVED.html

> │              ├── 📄 NT_index.html

> │              ├── 📄 NT_index_MOVED.html

> │              ├── 📄 NT_long_term_payout_strategy.html

> │              ├── 📄 NT_master_timeline.html

> │              ├── 📄 NT_premonitions_i_knew_before_i_knew.html

> │              ├── 📄 NT_public_statement.html

> │              ├── 📄 NT_session_summary_2025-12-15_i_knew_before_i_kn.html

> │              ├── 📄 NT_strategic_plan.html

> │              ├── 📄 NT_wc2.00.002_draft_emergency_stay.html

> │              ├── 📄 NT_wc2.00.003_draft_supplemental.html

> │              ├── 📄 NT_wc2.01.010__index-content.html

> │              ├── 📄 NT_wc2.01.010__index.html

> │              ├── 📄 NT_wg6.01.003_status_tracker.html

> │              ├── 📄 NT_wi8.01.010__2025-12-15_they_threw_us_into_the.html

> │              ├── 📄 NT_wi8.01.050__index-content.html

> │              ├── 📄 NT_wi8.99.010__index-content.html

> │              ├── 📄 NT_wi8.99.010__index.html

> │              ├── 📄 NT_wi8.99.010__long_term_payout_strategy.html

> │              ├── 📄 NT_wi8.99.010__premonitions_i_knew_before_i_knew.html

> │              ├── 📄 NT_wi8.99.010__session_summary_2025-12-15_i_knew.html

> │              ├── 📄 OR_wc2.01.001_draft_order_vacate.html

> │              ├── 📄 OR_wc2.01.002_draft_order_stay.html

> │              ├── 📄 OR_wc2.01.010__proposed_order_emergency_stay.html

> │              ├── 📄 OR_wc2.01.010__proposed_orders.html

> │              ├── 📄 PL_cold_risk_report.html

> │              ├── 📄 PL_wg6.01.001_doj_complaint.html

> │              ├── 📄 PL_wg6.01.002_icrc_complaint.html

> │              ├── 📄 _readme.html

> │              ├── 📄 _readme_MOVED.html

> │            └── 📂 vis/

> │              ├── 📄 latest.txt

> │          ├── 📄 NT_README.md

> │          └── 📂 _ADMIN/

> │            └── 📂 10_index/

> │              ├── 📄 NT_00_index.md

> │              ├── 📄 NT_Contacts.md

> │            └── 📂 20_case_logs/

> │              ├── 📄 NT_2025-12-09_Writ_Executed_Forced_Removal.md

> │              ├── 📄 NT_2025-12-15_Case_DNA_Strategy_Checkpoint.md

> │              ├── 📄 NT_2025-12-15_Strategic_Planning_Session.md

> │              ├── 📄 NT_2025-12-16_Post_Removal_Access_Denial.md

> │              ├── 📄 NT_2025-12-16_case_log_entry.md

> │              ├── 📄 NT_2025-12-16_case_summary.md

> │              ├── 📄 NT_2025-12-16_fcfcu_case_dna_strat.md

> │              ├── 📄 NT_2025-12-21_Case_Summary.md

> │              ├── 📄 NT_2026-01-16_Cleanup_Log.md

> │              ├── 📄 NT_20_case_logs.md

> │              ├── 📄 NT_INGEST_2025-12-16_case_log_entry.md

> │              ├── 📄 NT_Master_Case_Log.md

> │              ├── 📄 NT_content_manifest_hashes.json

> │              ├── 📄 NT_ingest_dedupe_manifest.json

> │              ├── 📄 PL_integrity_scan_report.json

> │            └── 📂 30_financial/

> │              ├── 📄 NT_02_financial.md

> │              ├── 📄 NT_Financial_Tracker.md

> │            └── 📂 40_overviews/

> │              └── 📂 10_maps/

> │                ├── 📄 NT_Procedural_failure_map_one_pager.md

> │              └── 📂 20_deep_dives/

> │                ├── 📄 NT_Integrate_Disability_Separate_Appeals_Get_Stay.m4a

> │                ├── 📄 NT_foreclosure_void_versus_damages_due_process.m4a

> │                ├── 📄 NT_forensic_audit_of_a_void_foreclosure.m4a

> │                ├── 📄 OR_foreclosure_void_judgment_institutional_failur.m4a

> │              └── 📂 40_debates/

> │                ├── 📄 NT_debate.m4a

> │              └── 📂 50_explainers/

> │                ├── 📄 NT_crisis_the_anatomy_of_institutional_failure.pdf

> │                ├── 📄 NT_wrongful_foreclosure_a_case_study_in_civil_rig.pdf

> │                ├── 📄 OR_void_judgment_eviction_crisis.pdf

> │              └── 📂 60_infographics/

> │                ├── 📄 OR_Void_Judgment_Eviction_Crisis.pdf

> │              └── 📂 70_reports/

> │                ├── 📄 NT_Crisis_The_Anatomy_of_Institutional_Failure.pdf

> │                ├── 📄 NT_Wrongful_Foreclosure_A_Case_Study_in_Civil_Rig.pdf

> │                ├── 📄 NT__Session_Summary_2025-12-15_i_knew_b.md

> │                ├── 📄 NT_case-narrative-wrongful-foreclosure-and-displ.html

> │                ├── 📄 NT_legal-memorandum.html

> │                ├── 📄 NT_procedural_failure_map_one_pager.html

> │                ├── 📄 NT_talking_points.html

> │                ├── 📄 NT_uncategorized_bundle.pdf

> │                ├── 📄 OR_Void_Judgment_Eviction_Crisis.pdf

> │                ├── 📄 PL_70_reports.md

> │                ├── 📄 PL_proposal-for-strategic-reports-in-the-matter-.html

> │              ├── 📄 NT_10_overviews.md

> │            └── 📂 50_protocols/

> │              ├── 📄 NT_PROTOCOL_Canonical_Case_Knowledge_Base.md

> │            └── 📂 70_templates/

> │              └── 📂 10_motions/

> │                ├── 📄 MO_10_motions.md

> │                ├── 📄 MO_TEMPLATE_motion_emergency_stay_of_writ.md

> │                ├── 📄 MO_TEMPLATE_motion_emergency_supplemental_motion_ongoing_ha.md

> │                ├── 📄 MO_TEMPLATE_motion_to_vacate_void_judgment.md

> │              └── 📂 20_declarations/

> │                ├── 📄 NT_GUIDE_Witness_Instructions.md

> │                ├── 📄 NT_TEMPLATE_Gender_Identity_Clarification.md

> │                ├── 📄 PL_20_declarations.md

> │                ├── 📄 PL_TEMPLATE_ADA_Disability_Affidavit.md

> │                ├── 📄 PL_TEMPLATE_Character_Affidavit.md

> │                ├── 📄 PL_TEMPLATE_Community_Service_Affidavit.md

> │                ├── 📄 PL_TEMPLATE_Credibility_Affidavit.md

> │                ├── 📄 PL_TEMPLATE_Declarations.md

> │                ├── 📄 PL_TEMPLATE_Observations_Affidavit.md

> │                ├── 📄 PL_TEMPLATE_affidavit_not_served.md

> │                ├── 📄 PL_TEMPLATE_updated_affidavit_language.md

> │                ├── 📄 PL_TEMPLATE_verified_affidavit_of_defendant.md

> │              └── 📂 30_exhibits/

> │                ├── 📄 EXH_30_exhibits.md

> │                ├── 📄 EXH_TEMPLATE_Exhibit_List.md

> │              └── 📂 40_orders/

> │                ├── 📄 MO_TEMPLATE_proposed_order_motion_to_vacate.md

> │                ├── 📄 OR_40_orders.md

> │                ├── 📄 OR_TEMPLATE_Proposed_Order.md

> │                ├── 📄 OR_TEMPLATE_proposed_order_emergency_stay.md

> │              └── 📂 50_internal/

> │                ├── 📄 NT_TEMPLATE_Advocate_Outreach.md

> │                ├── 📄 NT_TEMPLATE_Court_Doc.md

> │                ├── 📄 NT_TEMPLATE_Fact_Timeline.md

> │                ├── 📄 NT_TEMPLATE_Handup_Packet_Note.md

> │                ├── 📄 NT_TEMPLATE_Section_Cover.md

> │                ├── 📄 NT_TEMPLATE_Section_Index.md

> │                ├── 📄 NT_TEMPLATE_Service_Matrix.md

> │                ├── 📄 NT_TEMPLATE_Timeline_Event.md

> │                ├── 📄 NT_TEMPLATE_Violation_Entry.md

> │                ├── 📄 NT_TEMPLATE_War_Note.md

> │                ├── 📄 NT_TEMPLATE_ada_packet.md

> │                ├── 📄 NT_TEMPLATE_attorney_brief.md

> │                ├── 📄 NT_TEMPLATE_receipt_usps_tracking.md

> │                ├── 📄 NT_TEMPLATE_script_call_lawyers.md

> │              ├── 📄 NT_40_templates.md

> │            └── 📂 80_integrity_tooling/

> │              ├── 📄 NT_50_integrity_tooling.md

> │              ├── 📄 NT_rename_plan.txt

> │              ├── 📄 NT_run_renames.ps1

> │              ├── 📄 PL_conflicts_report.txt

> │            └── 📂 90_pack_blueprints/

> │              ├── 📄 NT_60_pack_blueprints.md

> │              ├── 📄 NT_PACK_AGENCY.yaml

> │              ├── 📄 NT_PACK_JUDGE.yaml

> │              ├── 📄 NT_PACK_OPPOSING.yaml

> │              ├── 📄 NT_PACK_SELF.yaml

> │              ├── 📄 NT_PROPOSED_OUTPUT_STRUCTURE.md

> │            ├── 📄 NT_00_ADMIN.md

> │      └── 📂 vis/

> │        └── 📂 10_violations/

> │          ├── 📄 EXH_Exhibit X — Inventory of Jurisdictional, Execut.md

> │          ├── 📄 NT_V-005_failure-to-correct-inaccurate-furnishings.md

> │          ├── 📄 NT_V-006_dual-tradeline-double-counting.md

> │          ├── 📄 NT_V-008_credit-defamation-false-publication.md

> │          ├── 📄 NT_V-009_fdCPA-misrepresentation-of-debt-status.md

> │          ├── 📄 NT_V-010_failure-to-mark-account-foreclosure-closed.md

> │          ├── 📄 NT_V-011_experian-reinvestigation-failure.md

> │          ├── 📄 NT_V-012_equifax-reinvestigation-failure.md

> │          ├── 📄 NT_V-013_transunion-reinvestigation-failure.md

> │          ├── 📄 NT_V-020_post-0815-aes-electric-charges-billed.md

> │          ├── 📄 NT_V-021_post-0815-citizens-energy-charges-billed.md

> │          ├── 📄 NT_V-022_post-0815-hoa-assessments-billed.md

> │          ├── 📄 NT_V-023_city-grass-cut-ticket-assessed-after-loss-of-access.md

> │          ├── 📄 NT_V-024_municipal-code-enforcement-after-possession-transfer.md

> │          ├── 📄 NT_V-025_cost-shift-fcfcu-refused-winterize.md

> │          ├── 📄 NT_V-026_credit-harm-compounded-utility-municipal.md

> │          ├── 📄 NT_V-031_sheriff-return-inaccuracies.md

> │          ├── 📄 NT_V-033_removal-6-7-days-after-deed-recorded.md

> │          ├── 📄 NT_V-035_court-relied-on-service-sufficiency.md

> │          ├── 📄 NT_V-036_surplus-funds-declared-resolved.md

> │          ├── 📄 NT_V-037_interest-fees-arbitrarily-inflated.md

> │          ├── 📄 NT_V-038_fcfcu-testimony-winterize-then-leave.md

> │          ├── 📄 NT_V-070_global-demand-letter.md

> │          ├── 📄 NT_V-071_litigation-hold-preservation-letter.md

> │          ├── 📄 NT_V-072_equitable-relief-tradeline-deletion.md

> │          ├── 📄 NT_V-073_damages-credit-score-suppression.md

> │          ├── 📄 NT_V-074_damages-out-of-pocket-costs.md

> │          ├── 📄 NT_V-075_public-accountability-hold.md

> │          ├── 📄 NT_V-076_fha-reasonable-accommodation-failure.md

> │          ├── 📄 NT_V-077_ada-title-iii-entertainment-access-failure.md

> │          ├── 📄 NT_V-078_ada-effective-communication-failure.md

> │          ├── 📄 NT_V-080_conversion-negligence-post-removal-damage.md

> │          ├── 📄 NT_V-081_evidence-spoliation-unplugged-cameras.md

> │          ├── 📄 NT_V-082_fraud-on-the-court-material-misrepresentation.md

> │          ├── 📄 NT_V-083_discriminatory-maintenance-redlining.md

> │          ├── 📄 NT_V-084_predatory-land-contract-reverse-redlining.md

> │          ├── 📄 OR_V-001_fcfcu-continues-reporting-first-mortgage-post-judgment-sale.md

> │          ├── 📄 OR_V-002_fcfcu-continues-reporting-second-mortgage-post-judgment-sale.md

> │          ├── 📄 OR_V-003_monthly-delinquencies-after-foreclosure-judgment.md

> │          ├── 📄 OR_V-004_past-due-amount-schedule-after-judgment.md

> │          ├── 📄 OR_V-079_void-judgment-procedural-error.md

> │          ├── 📄 PL_V-007_inconsistent-reporting-vs-court-position.md

> │          ├── 📄 PL_V-030_service-completed-no-notice-before-writ.md

> │          ├── 📄 PL_V-032_no-ada-compliant-notice.md

> │          ├── 📄 PL_V-034_attorney-appeared-without-formal-appearance.md

> │          ├── 📄 PL_V-050_cfpb-complaint-track.md

> │          ├── 📄 PL_V-051_indiana-ag-complaint-track.md

> │          ├── 📄 PL_V-052_icrc-complaint-track.md

> │          ├── 📄 PL_V-053_doj-civil-rights-complaint-track.md

> │          ├── 📄 PL_V-060_bbb-complaint-reputational-pressure.md

> │        └── 📂 20_theories/

> │          ├── 📄 NT_BACKUP_ARGUMENTS.md

> │          ├── 📄 NT_IF_JUDGE_PUSHBACK.md

> │        └── 📂 30_legal_research/

> │          ├── 📄 NT_CASE_LAW_RESEARCH.md

> │          ├── 📄 NT_JURISDICTION_THEORY.md

> │          ├── 📄 NT_LEGAL MEMORANDUM.md

> │          ├── 📄 NT_VOID_VS_VOIDABLE_ANALYSIS.md

> │        └── 📂 40_analysis/

> │          ├── 📄 NT_INTERNAL VALUATION MEMO.md

> │          ├── 📄 NT_Procedural_failure_map_one_pager.md

> │          ├── 📄 NT_Violation_Remedy_Inventory.md

> │        └── 📂 50_strategies/

> │          ├── 📄 NT_00_basis.md

> │          ├── 📄 NT_10_ada_strategy.md

> │          ├── 📄 NT_ADA_TITLE_II_ANALYSIS.md

> │          ├── 📄 NT_BUT_FOR_ANALYSIS.md

> │          ├── 📄 NT_Master_Strategy_Canvas.canvas

> │          ├── 📄 NT_PROCEDURAL_FAILURE_MAP.md

> │          ├── 📄 NT_REASONABLE_ACCOMMODATIONS.md

> │          ├── 📄 NT_REVERSAL_PATHS.md

> │          ├── 📄 NT_STATUS_TRACKER.md

> │          ├── 📄 NT_STAY_PATHS.md

> │          ├── 📄 NT_integrate_disability_separate_appe.m4a

> │          ├── 📄 OR_void_judgment_eviction_crisis.pdf

> │          ├── 📄 PL_DOJ_COMPLAINT.md

> │          ├── 📄 PL_ICRC_COMPLAINT.md

> │          ├── 📄 PL_Proposal for Strategic Reports in the Matter of.md

> │          ├── 📄 Strategic_Plan.canvas

> │        └── 📂 60_data_inventories/

> │          ├── 📄 NT_Violation_Index.md

> │          ├── 📄 NT_foreclosure-and-housing-litigation-case-record.csv

> │          ├── 📄 NT_inventory-of-civil-and-fair-housing-rights-vio.csv

> │        ├── 📄 NT_01_MASTER_INDEX.md

> │        ├── 📄 _C_VIS.md

> │        ├── 📄 vis.yaml

> │      ├── 📄 vis_index.md

> │    ├── 📄 package-lock.json

> │    ├── 📄 package.json

> │    ├── 📄 prepare_vitepress.py

> └── 📂 content/

> │  └── 📂 A_TIMELINE/

> │    └── 📂 2023/

> │      ├── 📄 NT_index.md

> │      └── 📂 events/

> │    └── 📂 2024/

> │      ├── 📄 NT_index.md

> │      └── 📂 events/

> │    └── 📂 2025/

> │      ├── 📄 NT_index.md

> │      └── 📂 events/

> │        ├── 📄 MO_2025-05-13_Motion_for_Default_Judgment 1.md

> │        ├── 📄 MO_2025-05-13_Motion_for_Default_Judgment.md

> │        ├── 📄 MO_2025-05-23_Amended_Motion_Default_Judgment 1.md

> │        ├── 📄 MO_2025-05-23_Amended_Motion_Default_Judgment.md

> │        ├── 📄 MO_2025-12-10_Motions_Filed 1.md

> │        ├── 📄 MO_2025-12-10_Motions_Filed.md

> │        ├── 📄 MO_2025-12-12_Supplemental_Emergency_Motion 1.md

> │        ├── 📄 MO_2025-12-12_Supplemental_Emergency_Motion.md

> │        ├── 📄 NT_2025-01-16_Case_Filed 1.md

> │        ├── 📄 NT_2025-01-16_Case_Filed.md

> │        ├── 📄 NT_2025-03-05_Service_Attempt_1 1.md

> │        ├── 📄 NT_2025-03-05_Service_Attempt_1.md

> │        ├── 📄 NT_2025-04-15_Service_Attempt_2 1.md

> │        ├── 📄 NT_2025-04-15_Service_Attempt_2.md

> │        ├── 📄 NT_2025-08-15_Sheriff_Sale 1.md

> │        ├── 📄 NT_2025-08-15_Sheriff_Sale.md

> │        ├── 📄 NT_2025-11-06_Writ_of_Assistance_Issued 1.md

> │        ├── 📄 NT_2025-11-06_Writ_of_Assistance_Issued.md

> │        ├── 📄 NT_2025-12-09_Writ_Executed_Forced_Removal.md

> │        ├── 📄 NT_2025-12-09_Writ_Executed_Removal.md

> │        ├── 📄 NT_2025-12-16_Post_Removal_Access_Denial.md

> │        ├── 📄 NT_2025-12-21_Case_Summary.md

> │        ├── 📄 OR_2025-05-21_Order_Denying_Default_Judgment 1.md

> │        ├── 📄 OR_2025-05-21_Order_Denying_Default_Judgment.md

> │        ├── 📄 OR_2025-05-28_Default_Judgment_Entered 1.md

> │        ├── 📄 OR_2025-05-28_Default_Judgment_Entered.md

> │        ├── 📄 OR_2025-12-11_Court_Orders_and_Hearing_Scheduled 1.md

> │        ├── 📄 OR_2025-12-11_Court_Orders_and_Hearing_Scheduled.md

> │        ├── 📄 PL_2025-05-30_Praecipe_Sheriff_Sale 1.md

> │        ├── 📄 PL_2025-05-30_Praecipe_Sheriff_Sale.md

> │        ├── 📄 PL_2025-07-09_Sheriff_Sale_Notice_Posted 1.md

> │        ├── 📄 PL_2025-07-09_Sheriff_Sale_Notice_Posted.md

> │        ├── 📄 PL_2025-10-29_Petition_for_Writ_of_Assistance 1.md

> │        ├── 📄 PL_2025-10-29_Petition_for_Writ_of_Assistance.md

> │    └── 📂 2026/

> │      ├── 📄 NT_index.md

> │      └── 📂 events/

> │    ├── 📄 _A_TIMELINE.md

> │  └── 📂 B_EVIDENCE/

> │    └── 📂 10_evidence_admin/

> │      ├── 📄 00_evidence_admin.md

> │      ├── 📄 10_chain_of_custody.md

> │      ├── 📄 20_Evidence_Log.md

> │      ├── 📄 EXH_Raw_Exhibit_Map.md

> │      ├── 📄 _10_evidence_admin.md

> │    └── 📂 20_court_record/

> │      └── 📂 10_docket_files/

> │        ├── 📄 022_Plaintif_bid_2025_07_17_10_14_40.pdf.pdf

> │        ├── 📄 024_Service Returned Served.pdf

> │        ├── 📄 026_2025_10_29_13_47_03.pdf.pdf

> │        ├── 📄 029_Emergency_Supplemental_Declara.pdf

> │        ├── 📄 035_01092026_005.pdf.pdf

> │        ├── 📄 EXH_026_Exhibit_List_A-G.pdf

> │        ├── 📄 EXH__026_Exhibit_List_A-G.pdf

> │        ├── 📄 MO_013_Motion_for_Default_Judgment.pdf

> │        ├── 📄 MO_016_Order_Denying_Motion_for_Default_Judgment.pdf

> │        ├── 📄 MO_019_Amended_Motion_Default_Judgment_1.pdf

> │        ├── 📄 MO_020_Amended_Motion_Default_Judgment_2.pdf

> │        ├── 📄 MO_025_Motion_Vacate_Stay_Writ.pdf

> │        ├── 📄 MO_027_Supplemental_Motion_Access.pdf

> │        ├── 📄 MO__013_Motion_for_Default_Judgment.pdf

> │        ├── 📄 MO__019_Amended_Motion_Default_Judgmen.pdf

> │        ├── 📄 MO__020_Amended_Motion_Default_Judgmen.pdf

> │        ├── 📄 MO__025_Motion_Vacate_Stay_Writ.pdf

> │        ├── 📄 MO__027_Supplemental_Motion_Access.pdf

> │        ├── 📄 OR_023_Decree_Foreclosure_Returned.pdf

> │        ├── 📄 OR_031_Proposed_Order_Vacate.pdf

> │        ├── 📄 OR_032_Proposed_Order_Stay.pdf

> │        ├── 📄 OR__017_Order_Denying_Default_Judgment.pdf

> │        ├── 📄 OR__023_Decree_Foreclosure_Returned.pdf

> │        ├── 📄 OR__031_Proposed_Order_Vacate.pdf

> │        ├── 📄 OR__032_Proposed_Order_Stay.pdf

> │        ├── 📄 PL_001_Complaint.pdf

> │        ├── 📄 PL_002_Appearance.pdf

> │        ├── 📄 PL_003_Request_for_Admissions.pdf

> │        ├── 📄 PL_004_Notice_to_Homeowners.pdf

> │        ├── 📄 PL_005_Appearance_2.pdf

> │        ├── 📄 PL_006_Summons_1.pdf

> │        ├── 📄 PL_007_Summons_2.pdf

> │        ├── 📄 PL_008_Summons_3.pdf

> │        ├── 📄 PL_009_Summons_4.pdf

> │        ├── 📄 PL_010_Summons_5.pdf

> │        ├── 📄 PL_011_Service_Returned_03-05-2025.pdf

> │        ├── 📄 PL_012_Service_Returned_04-15-2025.pdf

> │        ├── 📄 PL_014_Affidavit.pdf

> │        ├── 📄 PL_015_Affidavit_Attorney_Fees.pdf

> │        ├── 📄 PL_017_OMITTED NOTICE OF SERVICE TO DEFENDANT.pdf

> │        ├── 📄 PL_018_Omitted_Notice_of_Service.pdf

> │        ├── 📄 PL_021_Praecipe_Sheriff_Sale_1.pdf

> │        ├── 📄 PL_022_Praecipe_Sheriff_Sale_2.pdf

> │        ├── 📄 PL_024_Petition_Writ_of_Assistance.pdf

> │        ├── 📄 PL_028_Report_Court_Defendant_Request.pdf

> │        ├── 📄 PL_029_Emergency_Supplemental_Declaration.pdf

> │        ├── 📄 PL_030_Report_Sheriff_Sale_No_Excess.pdf

> │        ├── 📄 PL_033_ADA_Disability_Affidavit.pdf

> │        ├── 📄 PL_2026-01-09_Appearance_Plaintiff.pdf

> │        ├── 📄 PL__001_Complaint.pdf

> │        ├── 📄 PL__002_Appearance.pdf

> │        ├── 📄 PL__003_Request_for_Admissions.pdf

> │        ├── 📄 PL__004_Notice_to_Homeowners.pdf

> │        ├── 📄 PL__005_Appearance_2.pdf

> │        ├── 📄 PL__006_Summons_1.pdf

> │        ├── 📄 PL__007_Summons_2.pdf

> │        ├── 📄 PL__008_Summons_3.pdf

> │        ├── 📄 PL__009_Summons_4.pdf

> │        ├── 📄 PL__010_Summons_5.pdf

> │        ├── 📄 PL__011_Service_Returned_03-05-2025.pdf

> │        ├── 📄 PL__012_Service_Returned_04-15-2025.pdf

> │        ├── 📄 PL__014_Affidavit.pdf

> │        ├── 📄 PL__015_Affidavit_Attorney_Fees.pdf

> │        ├── 📄 PL__016_Affidavit_Additional.pdf

> │        ├── 📄 PL__018_Omitted_Notice_of_Service.pdf

> │        ├── 📄 PL__021_Praecipe_Sheriff_Sale_1.pdf

> │        ├── 📄 PL__022_Praecipe_Sheriff_Sale_2.pdf

> │        ├── 📄 PL__024_Petition_Writ_of_Assistance.pdf

> │        ├── 📄 PL__028_Report_Court_Defendant_Request.pdf

> │        ├── 📄 PL__030_Report_Sheriff_Sale_No_Excess.pdf

> │        ├── 📄 PL__033_ADA_Disability_Affidavit.pdf

> │      ├── 📄 20_court_record.md

> │    └── 📂 30_primary/

> │      └── 📂 10_fcfcu/

> │        ├── 📄 2023-09-20_FCFCU_Hardship_and_Healt.md

> │        ├── 📄 2024-03-20_fcfcu_certified_response_tax_record.pdf

> │        ├── 📄 2024-12-09_outgoing_email_bank_access_request.pdf

> │        ├── 📄 2024-12-11_outgoing_email_bank_access_request.pdf

> │        ├── 📄 20241204_FCFCU_Statement (1).pdf

> │        ├── 📄 20241204_FCFCU_Statement (2).pdf

> │        ├── 📄 20241204_fcfcu_statement-(1).pdf

> │        ├── 📄 20241204_fcfcu_statement-(2).pdf

> │        ├── 📄 20241204_fcfcu_statement.pdf

> │        ├── 📄 2025-12-20_exh-30_fcfcu_740eacdc_2025-12-20_ex.jpg

> │        ├── 📄 2025-12-20_exh-30_fcfcu_ac6eb2ea_2025-12-20_ex.jpg

> │        ├── 📄 21june-24-4817shadow_appraisal.pdf

> │        ├── 📄 PL_2023-09-20_FCFCU_Hardship_and_Health_Notice_Let.md

> │        ├── 📄 PL_2023-09-20_fcfcu_hardship_and_health_notice_le.pdf

> │        ├── 📄 PL_2023-09-20_notice_disabilities_hardship.pdf

> │        ├── 📄 PL_2024-20-03_response_to_tax_notice.pdf

> │        ├── 📄 PL_fcfcu_v_cr-v_report_to_court.pdf

> │        ├── 📄 PL_report_to_court_on_defendants_request.pdf

> │        ├── 📄 _README.md

> │      └── 📂 20_aes/

> │        ├── 📄 2025-06-08_aes_ada_request_financial_hardship_.pdf

> │        ├── 📄 PL_2025-06-08_aes_ada_notice.pdf

> │        ├── 📄 PL_2025-12-16_AES_Emergency_Notice.md

> │        ├── 📄 _README.md

> │    └── 📂 40_supporting/

> │      ├── 📄 40_supporting.md

> │      └── 📂 docs/

> │        └── 📂 affidavits/

> │          ├── 📄 PL_affidavits.md

> │          └── 📂 ada-disability/

> │          └── 📂 character/

> │          └── 📂 community-service/

> │          └── 📂 credibility/

> │          └── 📂 observations/

> │        └── 📂 declarations/

> │          ├── 📄 PL_declarations.md

> │        └── 📂 receipts/

> │          ├── 📄 NT_2025-12-20_exh-20_receipts_0860d3df_2025-12-20.jpg

> │          ├── 📄 NT_Odyssey_Envelope_Receipt.pdf

> │        └── 📂 records/

> │          ├── 📄 Foreclosure and Housing Litigation Case Record.csv

> │          ├── 📄 Inventory of Civil and Fair Housing Rights Vio.csv

> │      └── 📂 multi-media/

> │        ├── 📄 2025-12-20_exh-10_photos_video_00241326_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_012aa06e_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_01b3e905_2025-1.png

> │        ├── 📄 2025-12-20_exh-10_photos_video_10f4975d_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_1a80b987_2025-1.mp4

> │        ├── 📄 2025-12-20_exh-10_photos_video_1beefb11_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_1f3f8a81_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_25fb1992_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_2f0952db_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_49c74ec6_2025-.heic

> │        ├── 📄 2025-12-20_exh-10_photos_video_4e01fa01_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_5be451ba_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_5d95cae5_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_61129253_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_63fb7b02_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_71c9e6a7_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_78ba1ccc_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_7a544ef7_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_8350e7be_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_8a163413_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_8d885a5c_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_942cfd7f_2025-1.png

> │        ├── 📄 2025-12-20_exh-10_photos_video_9b611100_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_9fb3a08a_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_9ff5022d_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_a8832e17_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_ca02d006_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_db9b10b5_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_e4cb3622_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_ebaaa38d_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_ed6dc885_2025-1.mp4

> │        ├── 📄 2025-12-20_exh-10_photos_video_f510498b_2025-.heic

> │        ├── 📄 2025-12-20_exh-10_photos_video_f60d8098_2025-1.png

> │        ├── 📄 2025-12-20_exh-10_photos_video_f98b089a_2025-1.png

> │        ├── 📄 2025-12-20_exh-10_photos_video_fa1703bf_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_fdd8d4ef_2025-1.jpg

> │      └── 📂 property/

> │        └── 📂 10_mortgage_history/

> │          └── 📂 10_payments/

> │            ├── 📄 2025-12-20_EXH-20_payments_c5131deb_2025-12-20.png

> │            ├── 📄 2025-12-20_exh-20_payments_c5131deb_2025-12-20 (2).png

> │            ├── 📄 20_payments.md

> │        └── 📂 20_parcel/

> │          ├── 📄 Parcel_6016506_PRC.pdf

> │          ├── 📄 Parcel_6016506_ParcelDetailHistory.pdf

> │          ├── 📄 parcel_6016506_parceldetailhistory (2).pdf

> │          ├── 📄 parcel_6016506_prc (2).pdf

> │    └── 📂 50_quarantine_candidates/

> │      ├── 📄 50_quarantine_candidates.md

> │    ├── 📄 _B_EVIDENCE.md

> │  └── 📂 C_VIS/

> │    └── 📂 10_violations/

> │      ├── 📄 EXH_Exhibit X — Inventory of Jurisdictional, Execut.md

> │      ├── 📄 NT_V-005_failure-to-correct-inaccurate-furnishings.md

> │      ├── 📄 NT_V-006_dual-tradeline-double-counting.md

> │      ├── 📄 NT_V-008_credit-defamation-false-publication.md

> │      ├── 📄 NT_V-009_fdCPA-misrepresentation-of-debt-status.md

> │      ├── 📄 NT_V-010_failure-to-mark-account-foreclosure-closed.md

> │      ├── 📄 NT_V-011_experian-reinvestigation-failure.md

> │      ├── 📄 NT_V-012_equifax-reinvestigation-failure.md

> │      ├── 📄 NT_V-013_transunion-reinvestigation-failure.md

> │      ├── 📄 NT_V-020_post-0815-aes-electric-charges-billed.md

> │      ├── 📄 NT_V-021_post-0815-citizens-energy-charges-billed.md

> │      ├── 📄 NT_V-022_post-0815-hoa-assessments-billed.md

> │      ├── 📄 NT_V-023_city-grass-cut-ticket-assessed-after-loss-of-access.md

> │      ├── 📄 NT_V-024_municipal-code-enforcement-after-possession-transfer.md

> │      ├── 📄 NT_V-025_cost-shift-fcfcu-refused-winterize.md

> │      ├── 📄 NT_V-026_credit-harm-compounded-utility-municipal.md

> │      ├── 📄 NT_V-031_sheriff-return-inaccuracies.md

> │      ├── 📄 NT_V-033_removal-6-7-days-after-deed-recorded.md

> │      ├── 📄 NT_V-035_court-relied-on-service-sufficiency.md

> │      ├── 📄 NT_V-036_surplus-funds-declared-resolved.md

> │      ├── 📄 NT_V-037_interest-fees-arbitrarily-inflated.md

> │      ├── 📄 NT_V-038_fcfcu-testimony-winterize-then-leave.md

> │      ├── 📄 NT_V-070_global-demand-letter.md

> │      ├── 📄 NT_V-071_litigation-hold-preservation-letter.md

> │      ├── 📄 NT_V-072_equitable-relief-tradeline-deletion.md

> │      ├── 📄 NT_V-073_damages-credit-score-suppression.md

> │      ├── 📄 NT_V-074_damages-out-of-pocket-costs.md

> │      ├── 📄 NT_V-075_public-accountability-hold.md

> │      ├── 📄 NT_V-076_fha-reasonable-accommodation-failure.md

> │      ├── 📄 NT_V-077_ada-title-iii-entertainment-access-failure.md

> │      ├── 📄 NT_V-078_ada-effective-communication-failure.md

> │      ├── 📄 NT_V-080_conversion-negligence-post-removal-damage.md

> │      ├── 📄 NT_V-081_evidence-spoliation-unplugged-cameras.md

> │      ├── 📄 NT_V-082_fraud-on-the-court-material-misrepresentation.md

> │      ├── 📄 NT_V-083_discriminatory-maintenance-redlining.md

> │      ├── 📄 NT_V-084_predatory-land-contract-reverse-redlining.md

> │      ├── 📄 OR_V-001_fcfcu-continues-reporting-first-mortgage-post-judgment-sale.md

> │      ├── 📄 OR_V-002_fcfcu-continues-reporting-second-mortgage-post-judgment-sale.md

> │      ├── 📄 OR_V-003_monthly-delinquencies-after-foreclosure-judgment.md

> │      ├── 📄 OR_V-004_past-due-amount-schedule-after-judgment.md

> │      ├── 📄 OR_V-079_void-judgment-procedural-error.md

> │      ├── 📄 PL_V-007_inconsistent-reporting-vs-court-position.md

> │      ├── 📄 PL_V-030_service-completed-no-notice-before-writ.md

> │      ├── 📄 PL_V-032_no-ada-compliant-notice.md

> │      ├── 📄 PL_V-034_attorney-appeared-without-formal-appearance.md

> │      ├── 📄 PL_V-050_cfpb-complaint-track.md

> │      ├── 📄 PL_V-051_indiana-ag-complaint-track.md

> │      ├── 📄 PL_V-052_icrc-complaint-track.md

> │      ├── 📄 PL_V-053_doj-civil-rights-complaint-track.md

> │      ├── 📄 PL_V-060_bbb-complaint-reputational-pressure.md

> │    └── 📂 20_theories/

> │      ├── 📄 NT_BACKUP_ARGUMENTS.md

> │      ├── 📄 NT_IF_JUDGE_PUSHBACK.md

> │    └── 📂 30_legal_research/

> │      ├── 📄 NT_CASE_LAW_RESEARCH.md

> │      ├── 📄 NT_JURISDICTION_THEORY.md

> │      ├── 📄 NT_LEGAL MEMORANDUM.md

> │      ├── 📄 NT_VOID_VS_VOIDABLE_ANALYSIS.md

> │    └── 📂 40_analysis/

> │      ├── 📄 NT_INTERNAL VALUATION MEMO.md

> │      ├── 📄 NT_Procedural_failure_map_one_pager.md

> │      ├── 📄 NT_Violation_Remedy_Inventory.md

> │    └── 📂 50_strategies/

> │      ├── 📄 NT_00_basis.md

> │      ├── 📄 NT_10_ada_strategy.md

> │      ├── 📄 NT_ADA_TITLE_II_ANALYSIS.md

> │      ├── 📄 NT_BUT_FOR_ANALYSIS.md

> │      ├── 📄 NT_Master_Strategy_Canvas.canvas

> │      ├── 📄 NT_PROCEDURAL_FAILURE_MAP.md

> │      ├── 📄 NT_REASONABLE_ACCOMMODATIONS.md

> │      ├── 📄 NT_REVERSAL_PATHS.md

> │      ├── 📄 NT_STATUS_TRACKER.md

> │      ├── 📄 NT_STAY_PATHS.md

> │      ├── 📄 NT_integrate_disability_separate_appe.m4a

> │      ├── 📄 OR_void_judgment_eviction_crisis.pdf

> │      ├── 📄 PL_DOJ_COMPLAINT.md

> │      ├── 📄 PL_ICRC_COMPLAINT.md

> │      ├── 📄 PL_Proposal for Strategic Reports in the Matter of.md

> │      ├── 📄 Strategic_Plan.canvas

> │    └── 📂 60_data_inventories/

> │      ├── 📄 NT_Violation_Index.md

> │      ├── 📄 NT_foreclosure-and-housing-litigation-case-record.csv

> │      ├── 📄 NT_inventory-of-civil-and-fair-housing-rights-vio.csv

> │    ├── 📄 NT_01_MASTER_INDEX.md

> │    ├── 📄 _C_VIS.md

> │    ├── 📄 vis.yaml

> │  ├── 📄 Case_Data.base

> │  └── 📂 D_PHASES/

> │    └── 📂 100_post_judgment_and_federal/

> │      └── 📂 10_motions/

> │        └── 📂 10_claims_motions/

> │          ├── 📄 40_claims_motions.md

> │          ├── 📄 MO_40_claims_motions.md

> │          └── 📂 Supplemental/

> │            └── 📂 01_drafts/

> │              ├── 📄 MO__Supplemental_Emergency_Motion.pdf

> │            └── 📂 02_exhibits/

> │              ├── 📄 EXH_02_exhibits.md

> │              ├── 📄 EXH__20_exhibits_combined_source

> │              ├── 📄 EXH__Exhibit_H_Declaration.pdf

> │            └── 📂 04_filed_receipts/

> │              ├── 📄 NT__Odyssey_Envelope_Receipt.pdf

> │          └── 📂 filings/

> │            └── 📂 10_2025-12-10_motion_vacate/

> │              └── 📂 01_drafts/

> │                ├── 📄 MO_Emergency Motions.docx

> │              └── 📂 02_exhibits/

> │                ├── 📄 EXH_02_exhibits.md

> │                ├── 📄 EXH_05_Exhibit_List.pdf

> │                ├── 📄 EXH_06_Exhibits_Combined.pdf

> │                ├── 📄 MO_01_motion_vacate.pdf

> │                ├── 📄 MO_02_emergency_motion_quash_stay.pdf

> │                ├── 📄 NT_combinepdf.pdf

> │                ├── 📄 OR_03_order_vacate_proposed.pdf

> │                ├── 📄 OR_04_order_stay_writ_proposed.pdf

> │              └── 📂 03_proposed_order/

> │                ├── 📄 OR_03_proposed_order.md

> │                ├── 📄 OR_Proposed_Order_Vacate.docx

> │              └── 📂 04_filed_receipts/

> │                ├── 📄 NT_Odyssey_Envelope_Receipt.pdf

> │              ├── 📄 MO_10_2025-12-10_motion_vacate.md

> │            └── 📂 20_2025-12-11_Supplemental_Emergency_Motion_Access/

> │              └── 📂 01_drafts/

> │                ├── 📄 MO_Supplemental_Emergency_Motion.pdf

> │              └── 📂 02_exhibits/

> │                ├── 📄 EXH_02_exhibits.md

> │                ├── 📄 EXH_20_exhibits_combined_source

> │                ├── 📄 EXH_Exhibit_H_Declaration.pdf

> │              └── 📂 04_filed_receipts/

> │                ├── 📄 NT_Odyssey_Envelope_Receipt.pdf

> │              ├── 📄 MO_20_2025-12-11_Supplemental_Emergency_Motion_Access.md

> │            └── 📂 30_draft_motions/

> │              ├── 📄 10_draft_motions.md

> │              ├── 📄 20_draft_motions.md

> │              ├── 📄 MO_10_draft_motions.md

> │              ├── 📄 MO_DRAFT_MOTION_VACATE.md

> │              ├── 📄 MO__Motions.md

> │              ├── 📄 MO__motion_emergency_stay_of_writ.md

> │              ├── 📄 MO__motion_emergency_supplemental_motio.md

> │              ├── 📄 MO__motion_to_vacate_void_judgment.md

> │              ├── 📄 MO_motion_emergency_stay_of_writ.md

> │              ├── 📄 MO_motion_emergency_supplemental_motion_ongoing_ha.md

> │              ├── 📄 MO_motion_to_vacate_void_judgment.md

> │              ├── 📄 MO_wc2.00.010__motion_emergency_stay_of_writ.docx

> │              ├── 📄 MO_wc2.00.010__motion_emergency_supplemental_mot.docx

> │              ├── 📄 MO_wc2.00.010__motion_to_vacate_void_judgement.docx

> │              ├── 📄 NT_DRAFT_EMERGENCY_STAY.md

> │              ├── 📄 NT_DRAFT_SUPPLEMENTAL.md

> │              ├── 📄 NT_EMERGENCY_FILING_PACKET.md

> │              ├── 📄 _README.md

> │              └── 📂 motions/

> │                ├── 📄 MO_01B_Motion_To_Vacate_Void_Judgment.pdf

> │                ├── 📄 MO_C2.01.002_motion_vacate.pdf

> │                ├── 📄 MO_C2.02.002_Emergency_Motion_Stay_OR_Quash.pdf

> │                ├── 📄 MO_C2.03.002_Supplemental_Emergency_Motion.pdf

> │                ├── 📄 MO_motions.md

> │          └── 📂 motion_vacate/

> │            └── 📂 01_drafts/

> │              ├── 📄 MO__Emergency Motions.docx

> │            └── 📂 02_exhibits/

> │              ├── 📄 EXH_02_exhibits.md

> │              ├── 📄 EXH__05_Exhibit_List.pdf

> │              ├── 📄 EXH__06_Exhibits_Combined.pdf

> │              ├── 📄 MO__01_motion_vacate.pdf

> │              ├── 📄 MO__02_emergency_motion_quash_stay.pdf

> │              ├── 📄 NT__combinepdf.pdf

> │              ├── 📄 OR__03_order_vacate_proposed.pdf

> │              ├── 📄 OR__04_order_stay_writ_proposed.pdf

> │            └── 📂 03_proposed_order/

> │              ├── 📄 OR_03_proposed_order.md

> │              ├── 📄 OR__Proposed_Order_Vacate.docx

> │            └── 📂 04_filed_receipts/

> │              ├── 📄 NT__Odyssey_Envelope_Receipt.pdf

> │            ├── 📄 MO_motion_vacate.md

> │            ├── 📄 NT.gitkeep

> │        ├── 📄 MO_10_motions.md

> │        ├── 📄 NT_index.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_orders/

> │        └── 📂 10_proposed_orders/

> │          ├── 📄 20_proposed_orders.md

> │          ├── 📄 MO__proposed_order_motion_to_vacate.md

> │          ├── 📄 MO_proposed_order_motion_to_vacate.md

> │          ├── 📄 NT__index.md

> │          ├── 📄 OR_20_proposed_orders.md

> │          ├── 📄 OR_DRAFT_ORDER_STAY.md

> │          ├── 📄 OR_DRAFT_ORDER_VACATE.md

> │          ├── 📄 OR__Proposed_Orders.md

> │          ├── 📄 OR__proposed_order_emergency_stay.md

> │          ├── 📄 OR_proposed_order_emergency_stay.md

> │          ├── 📄 _README.md

> │        ├── 📄 NT_index.md

> │        ├── 📄 OR_20_orders.md

> │        ├── 📄 _placeholder.md

> │        └── 📂 orders/

> │          ├── 📄 OR_C2.04.001_order_vacate_proposed.pdf

> │          ├── 📄 OR_C2.04.002_order_stay_writ_proposed.pdf

> │          ├── 📄 OR_orders.md

> │      └── 📂 30_regulatory_complaints/

> │        ├── 📄 PL_30_regulatory_complaints.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_federal_preservation/

> │        ├── 📄 _placeholder.md

> │      ├── 📄 OR_90_post_judgment_and_federal.md

> │      ├── 📄 _README.md

> │    └── 📂 10_inbox_working/

> │      ├── 📄 NT_00_inbox_working.md

> │      ├── 📄 NT_index.md

> │      └── 📂 _staging/

> │        └── 📂 _dupes_hold/

> │          ├── 📄 MO__motion_emergency_stay_of_writ (2).docx

> │          ├── 📄 MO__motion_emergency_supplemental_mot (2).docx

> │          ├── 📄 MO__motion_to_vacate_void_judgement (2).docx

> │          ├── 📄 NT_2025-12-15_they_threw_us_into_the_cold (2).md

> │          ├── 📄 NT_Donations_Context (2).md

> │          ├── 📄 NT_Long_Term_Payout_Strategy (2).md

> │          ├── 📄 NT_Master_Timeline (2).md

> │          ├── 📄 NT_Premonitions_I_Knew_Before_I_Knew (2).md

> │          ├── 📄 NT_Public_Statement (2).md

> │          ├── 📄 NT_Session_Summary_2025-12-15_i_knew_before_i_knew (2).md

> │          ├── 📄 NT_index.md

> │          ├── 📄 OR_c2.04.001_order_vacate_proposed (2).pdf

> │          ├── 📄 OR_c2.04.002_order_stay_writ_proposed (2).pdf

> │          ├── 📄 PL_Cold_Risk_Report (2).md

> │        └── 📂 _html_hold/

> │          ├── 📄 NT_index.md

> │      └── 📂 evidence_staging/

> │        └── 📂 exhibit_candidates/

> │          └── 📂 10_exposure_and_harm/

> │            ├── 📄 02_exposure_and_harm.md

> │            ├── 📄 NT_02_exposure_and_harm.md

> │            ├── 📄 PL_wi8.02.050__cold_risk_report.html

> │            └── 📂 photos_conditions/

> │            └── 📂 weather_reports/

> │              ├── 📄 PL_weather_reports.md

> │          ├── 📄 EXH_exhibit_candidates.md

> │        └── 📂 potential_exhibits/

> │          ├── 📄 EXH_potential_exhibits.md

> │    └── 📂 20_pre_foreclosure/

> │      └── 📂 10_account_history/

> │        ├── 📄 NT_index.md

> │        ├── 📄 NT_one_pager_overview.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_hardship_and_ada/

> │        ├── 📄 _placeholder.md

> │      └── 📂 30_communications/

> │        ├── 📄 NT_index.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_payments_and_disputes/

> │        ├── 📄 _placeholder.md

> │      ├── 📄 NT_10_pre_foreclosure.md

> │      ├── 📄 _README.md

> │    └── 📂 30_foreclosure_filing/

> │      └── 📂 10_complaint/

> │        ├── 📄 PL_10_complaint.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_summons/

> │        ├── 📄 PL_20_summons.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 30_lien_parties/

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_docket_snapshots/

> │        └── 📂 10_docket_map_and_notes/

> │        ├── 📄 NT_01_Docket.md

> │        ├── 📄 NT__Case_Summary.md

> │        ├── 📄 NT_docket_index.md

> │        ├── 📄 _Case_Summary.md

> │        ├── 📄 _README.md

> │        ├── 📄 _docket.md

> │        ├── 📄 _placeholder.md

> │        └── 📂 docket_files/

> │      ├── 📄 NT_20_foreclosure_filing.md

> │      ├── 📄 _README.md

> │    └── 📂 40_service_and_notice/

> │      └── 📂 10_sheriff_returns/

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_mailings/

> │        ├── 📄 _placeholder.md

> │      └── 📂 30_affidavits_of_service/

> │        └── 📂 10_jurisdiction_service_tr_4_1_b/

> │          ├── 📄 20_jurisdiction_service_tr_4_1_b.md

> │          ├── 📄 NT_20_jurisdiction_service_tr_4_1_b 1.md

> │          ├── 📄 NT_20_jurisdiction_service_tr_4_1_b.md

> │        └── 📂 20_service_process/

> │          ├── 📄 30_service_process.md

> │        ├── 📄 NT_03_Service_Process.md

> │        ├── 📄 NT_service_defects_analysis.md

> │        ├── 📄 PL_30_affidavits_of_service.md

> │        ├── 📄 PL_affidavits_service.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_defects_and_contradictions/

> │        ├── 📄 _placeholder.md

> │      ├── 📄 PL_30_service_and_notice.md

> │      ├── 📄 _README.md

> │    └── 📂 50_default_and_judgment/

> │      └── 📂 10_default_motion/

> │        ├── 📄 MO_10_default_motion.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_default_order/

> │        ├── 📄 OR_20_default_order.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 30_judgment_and_decree/

> │        ├── 📄 OR_30_judgment_and_decree.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_accounting_inputs/

> │        ├── 📄 _placeholder.md

> │      ├── 📄 OR_40_default_and_judgment.md

> │      ├── 📄 _README.md

> │    └── 📂 60_sale_and_title/

> │      └── 📂 10_sheriff_sale/

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_deed/

> │        ├── 📄 _placeholder.md

> │      └── 📂 30_recording_gaps/

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_possession_claims/

> │        └── 📂 10_sale_and_possession/

> │          ├── 📄 30_sale_and_possession.md

> │          ├── 📄 NT_30_sale_and_possession.md

> │        └── 📂 30_void_vs_voidable/

> │          ├── 📄 20_void_vs_voidable.md

> │          ├── 📄 NT_30_void_vs_voidable_tr_60b 1.md

> │          ├── 📄 NT_30_void_vs_voidable_tr_60b.md

> │        ├── 📄 NT_05_Sale_and_Possesion.md

> │        ├── 📄 NT_possession_admissions.md

> │        ├── 📄 _placeholder.md

> │      ├── 📄 NT_50_sale_and_title.md

> │      ├── 📄 _README.md

> │    └── 📂 70_writ_and_execution/

> │      └── 📂 10_writ_petition/

> │        ├── 📄 PL_10_writ_petition.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_writ_order/

> │        ├── 📄 OR_20_writ_order.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 30_execution_events/

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_notice_failures/

> │        ├── 📄 PL_40_notice_failures.md

> │        ├── 📄 _placeholder.md

> │      ├── 📄 NT_60_writ_and_execution.md

> │      ├── 📄 _README.md

> │    └── 📂 80_post_removal_conduct/

> │      └── 📂 10_property_interference/

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_access_denial/

> │        ├── 📄 _placeholder.md

> │      └── 📂 30_spoliation_risk/

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_third_party_actions/

> │        ├── 📄 _placeholder.md

> │      ├── 📄 NT_70_post_removal_conduct.md

> │      ├── 📄 _README.md

> │    └── 📂 90_damages_and_fallout/

> │      └── 📂 10_property_possession_harms/

> │        ├── 📄 03_property_possession_harms.md

> │        ├── 📄 NT_03_property_possession_harms.md

> │      └── 📂 20_economic_harm/

> │        ├── 📄 10_economic_harm.md

> │        ├── 📄 NT_10_economic_harm.md

> │        ├── 📄 NT_index.md

> │      └── 📂 30_financial/

> │        ├── 📄 20_financial.md

> │        ├── 📄 NT_10_financial.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_health_and_safety/

> │        ├── 📄 30_health_and_safety.md

> │        ├── 📄 NT_20_health_and_safety.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 50_non_economic_harm/

> │        ├── 📄 40_non_economic_harm.md

> │        ├── 📄 NT_20_non_economic_harm.md

> │        └── 📂 cold_exposure/

> │          ├── 📄 NT_index.md

> │      └── 📂 60_professional_harm/

> │        ├── 📄 50_professional_harm.md

> │        ├── 📄 NT_30_professional_harm.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 70_remedies_scenarios/

> │        ├── 📄 60_remedies_scenarios.md

> │        ├── 📄 NT_30_remedies_scenarios.md

> │        ├── 📄 NT_index.md

> │      └── 📂 80_payout_strategy/

> │        ├── 📄 70_payout_strategy.md

> │        ├── 📄 NT_40_Payout_Strategy.md

> │        ├── 📄 NT__Long_Term_Payout_Strategy.md

> │        ├── 📄 NT_index.md

> │        ├── 📄 _README.md

> │        └── 📂 payout_strategy/

> │      └── 📂 90_third_party_harm/

> │        ├── 📄 80_third_party_harm.md

> │        ├── 📄 NT_40_third_party_harm.md

> │        ├── 📄 _placeholder.md

> │      ├── 📄 NT_06_damages_and_remedies.md

> │      ├── 📄 NT_80_damages_and_fallout.md

> │      ├── 📄 NT_index.md

> │      └── 📂 Photos_Conditions/

> │      └── 📂 Weather_Reports/

> │        ├── 📄 PL_Weather_Reports.md

> │      ├── 📄 _README.md

> │      └── 📂 economic/

> │        ├── 📄 NT_ECONOMIC_HARM.md

> │      └── 📂 non-economic/

> │        ├── 📄 NT_NON_ECONOMIC_HARM.md

> │        └── 📂 cold-exposure/

> │          ├── 📄 PL__Cold_Risk_Report.md

> │      └── 📂 personal_narrative/

> │        └── 📂 10_Public_Narrative/

> │          ├── 📄 01_Public_Narrative.md

> │          ├── 📄 NT_01_Public_Narrative.md

> │          ├── 📄 NT_2025-12-15_they_threw_us_into_the_cold.md

> │          ├── 📄 NT_Public_Statement.md

> │          ├── 📄 _README.md

> │        └── 📂 20_Exposure_and_Harm/

> │          ├── 📄 02_Exposure_and_Harm.md

> │          ├── 📄 NT_02_Exposure_and_Harm.md

> │          ├── 📄 PL_Cold_Risk_Report.md

> │          └── 📂 Photos_Conditions/

> │          └── 📂 Weather_Reports/

> │            ├── 📄 PL_Weather_Reports.md

> │          ├── 📄 _README.md

> │        └── 📂 30_Internal_Analysis/

> │          ├── 📄 03_Internal_Analysis.md

> │          ├── 📄 NT_03_Internal_Analysis.md

> │          ├── 📄 NT_Session_Summary_2025-12-15_i_knew_before_i_knew.md

> │          └── 📂 Payout_Strategy/

> │            ├── 📄 NT_Long_Term_Payout_Strategy.md

> │            ├── 📄 _README.md

> │          └── 📂 Premonitions/

> │            ├── 📄 NT_Premonitions_I_Knew_Before_I_Knew.md

> │            ├── 📄 _README.md

> │          ├── 📄 _README.md

> │        └── 📂 40_Donations_and_Support/

> │          ├── 📄 04_Donations_and_Support.md

> │          └── 📂 Donation_Page_HTML/

> │          ├── 📄 NT_04_Donations_and_Support.md

> │          ├── 📄 NT_Donations_Context.md

> │          └── 📂 Screenshots_Live_Page/

> │          ├── 📄 _README.md

> │        └── 📂 50_Timeline/

> │          ├── 📄 05_Timeline.md

> │          ├── 📄 NT_05_Timeline.md

> │          ├── 📄 NT_Master_Timeline.md

> │          ├── 📄 _README.md

> │        └── 📂 Premonitions/

> │          ├── 📄 NT__Premonitions_I_Knew_Before_I_Knew.md

> │          ├── 📄 _README.md

> │      └── 📂 settlement/

> │        ├── 📄 NT_SETTLEMENT_SCENARIOS.md

> │      └── 📂 thirdparty/

> │    ├── 📄 MO_Promotion_Checklist.md

> │    ├── 📄 Strategic_Plan.canvas

> │    ├── 📄 _D_PHASES.md

> │  └── 📂 E_OUTPUTS/

> │    └── 📂 10_binders/

> │      └── 📂 master_case_bible/

> │        ├── 📄 NT_binder_manifest.md

> │        └── 📂 _build/

> │          ├── 📄 NT_full_binder.md

> │          ├── 📄 NT_full_binder_snapshot.md

> │          ├── 📄 NT_master_case_bible.html

> │          ├── 📄 NT_temp_merged.md

> │        └── 📂 sections/

> │    └── 📂 20_filings/

> │    ├── 📄 _E_OUTPUTS.md

> │    └── 📂 _build_artifacts/

> │      ├── 📄 MO_wc2.00.001_draft_motion_vacate.html

> │      ├── 📄 MO_wc2.00.010___motions.html

> │      ├── 📄 MO_wc2.00.010__motion_emergency_stay_of_writ.html

> │      ├── 📄 MO_wc2.00.010__motion_emergency_supplemental_mot.html

> │      ├── 📄 MO_wc2.00.010__motion_to_vacate_void_judgment.html

> │      ├── 📄 MO_wc2.01.010__proposed_order_motion_to_vacate.html

> │      ├── 📄 NT_2025-12-15_they_threw_us_into_the_cold.html

> │      ├── 📄 NT_Summary - MyCase.html

> │      ├── 📄 NT_WI8.01.050__index.html

> │      ├── 📄 NT_WI8.02.050__index.html

> │      ├── 📄 NT_WI8.99.010__index_MOVED.html

> │      ├── 📄 NT_WZ9.00.050__index.html

> │      ├── 📄 NT_WZ9.00.050__index_MOVED.html

> │      ├── 📄 NT__index (2).html

> │      ├── 📄 NT__index.html

> │      ├── 📄 NT__index_MOVED.html

> │      ├── 📄 NT_donations_context.html

> │      ├── 📄 NT_index (2).html

> │      ├── 📄 NT_index (2)_MOVED.html

> │      ├── 📄 NT_index-content.html

> │      ├── 📄 NT_index-content_MOVED.html

> │      ├── 📄 NT_index.html

> │      ├── 📄 NT_index_MOVED.html

> │      ├── 📄 NT_long_term_payout_strategy.html

> │      ├── 📄 NT_master_timeline.html

> │      ├── 📄 NT_premonitions_i_knew_before_i_knew.html

> │      ├── 📄 NT_public_statement.html

> │      ├── 📄 NT_session_summary_2025-12-15_i_knew_before_i_kn.html

> │      ├── 📄 NT_strategic_plan.html

> │      ├── 📄 NT_wc2.00.002_draft_emergency_stay.html

> │      ├── 📄 NT_wc2.00.003_draft_supplemental.html

> │      ├── 📄 NT_wc2.01.010__index-content.html

> │      ├── 📄 NT_wc2.01.010__index.html

> │      ├── 📄 NT_wg6.01.003_status_tracker.html

> │      ├── 📄 NT_wi8.01.010__2025-12-15_they_threw_us_into_the.html

> │      ├── 📄 NT_wi8.01.050__index-content.html

> │      ├── 📄 NT_wi8.99.010__index-content.html

> │      ├── 📄 NT_wi8.99.010__index.html

> │      ├── 📄 NT_wi8.99.010__long_term_payout_strategy.html

> │      ├── 📄 NT_wi8.99.010__premonitions_i_knew_before_i_knew.html

> │      ├── 📄 NT_wi8.99.010__session_summary_2025-12-15_i_knew.html

> │      ├── 📄 OR_wc2.01.001_draft_order_vacate.html

> │      ├── 📄 OR_wc2.01.002_draft_order_stay.html

> │      ├── 📄 OR_wc2.01.010__proposed_order_emergency_stay.html

> │      ├── 📄 OR_wc2.01.010__proposed_orders.html

> │      ├── 📄 PL_cold_risk_report.html

> │      ├── 📄 PL_wg6.01.001_doj_complaint.html

> │      ├── 📄 PL_wg6.01.002_icrc_complaint.html

> │      ├── 📄 _readme.html

> │      ├── 📄 _readme_MOVED.html

> │    └── 📂 vis/

> │      └── 📂 1768577070/

> │        ├── 📄 claims_map.json

> │        ├── 📄 manifest.csv

> │        ├── 📄 manifest.json

> │        ├── 📄 search_index.json

> │        └── 📂 site/

> │          └── 📂 A_TIMELINE/

> │            └── 📂 2023/

> │              ├── 📄 index.html

> │            └── 📂 2024/

> │              ├── 📄 index.html

> │            └── 📂 2025/

> │              └── 📂 events/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 2026/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 B_EVIDENCE/

> │            └── 📂 10_evidence_admin/

> │              ├── 📄 index.html

> │            └── 📂 20_court_record/

> │              └── 📂 10_docket_files/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 30_primary/

> │              └── 📂 aes/

> │                ├── 📄 index.html

> │              └── 📂 fcfcu/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 40_supporting/

> │              └── 📂 docs/

> │                └── 📂 affidavits/

> │                  ├── 📄 index.html

> │                └── 📂 declarations/

> │                  ├── 📄 index.html

> │                └── 📂 receipts/

> │                  ├── 📄 index.html

> │                └── 📂 records/

> │                  ├── 📄 index.html

> │              ├── 📄 index.html

> │              └── 📂 multi-media/

> │                ├── 📄 index.html

> │              └── 📂 property/

> │                └── 📂 10_mortgage_history/

> │                  └── 📂 10_payments/

> │                    ├── 📄 index.html

> │                └── 📂 20_parcel/

> │                  ├── 📄 index.html

> │            └── 📂 50_quarantine_candidates/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 C_VIS/

> │            └── 📂 10_violations/

> │              ├── 📄 index.html

> │            └── 📂 20_theories/

> │              ├── 📄 index.html

> │            └── 📂 30_legal_research/

> │              ├── 📄 index.html

> │            └── 📂 40_analysis/

> │              ├── 📄 index.html

> │            └── 📂 50_strategies/

> │              ├── 📄 index.html

> │            └── 📂 60_data_inventories/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 D_PHASES/

> │            └── 📂 100_post_judgment_and_federal/

> │              └── 📂 10_motions/

> │                └── 📂 10_claims_motions/

> │                  └── 📂 Supplemental/

> │                    └── 📂 01_drafts/

> │                      ├── 📄 index.html

> │                    └── 📂 02_exhibits/

> │                      ├── 📄 index.html

> │                    └── 📂 04_filed_receipts/

> │                      ├── 📄 index.html

> │                  └── 📂 filings/

> │                    └── 📂 10_2025-12-10_motion_vacate/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 index.html

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 index.html

> │                      └── 📂 03_proposed_order/

> │                        ├── 📄 index.html

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 index.html

> │                      ├── 📄 index.html

> │                    └── 📂 20_2025-12-11_Supplemental_Emergency_Motion_Access/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 index.html

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 index.html

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 index.html

> │                      ├── 📄 index.html

> │                    └── 📂 30_draft_motions/

> │                      ├── 📄 index.html

> │                      └── 📂 motions/

> │                        ├── 📄 index.html

> │                  ├── 📄 index.html

> │                  └── 📂 motion_vacate/

> │                    └── 📂 01_drafts/

> │                      ├── 📄 index.html

> │                    └── 📂 02_exhibits/

> │                      ├── 📄 index.html

> │                    └── 📂 03_proposed_order/

> │                      ├── 📄 index.html

> │                    └── 📂 04_filed_receipts/

> │                      ├── 📄 index.html

> │                    ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 20_orders/

> │                └── 📂 10_proposed_orders/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │                └── 📂 orders/

> │                  ├── 📄 index.html

> │              └── 📂 30_regulatory_complaints/

> │                ├── 📄 index.html

> │              └── 📂 40_federal_preservation/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 10_inbox_working/

> │              └── 📂 _staging/

> │                └── 📂 _dupes_hold/

> │                  ├── 📄 index.html

> │                └── 📂 _html_hold/

> │                  ├── 📄 index.html

> │              └── 📂 evidence_staging/

> │                └── 📂 exhibit_candidates/

> │                  └── 📂 10_exposure_and_harm/

> │                    ├── 📄 index.html

> │                    └── 📂 weather_reports/

> │                      ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 potential_exhibits/

> │                  ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 20_pre_foreclosure/

> │              └── 📂 10_account_history/

> │                ├── 📄 index.html

> │              └── 📂 20_hardship_and_ada/

> │                ├── 📄 index.html

> │              └── 📂 30_communications/

> │                ├── 📄 index.html

> │              └── 📂 40_payments_and_disputes/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 30_foreclosure_filing/

> │              └── 📂 10_complaint/

> │                ├── 📄 index.html

> │              └── 📂 20_summons/

> │                ├── 📄 index.html

> │              └── 📂 30_lien_parties/

> │                ├── 📄 index.html

> │              └── 📂 40_docket_snapshots/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 40_service_and_notice/

> │              └── 📂 10_sheriff_returns/

> │                ├── 📄 index.html

> │              └── 📂 20_mailings/

> │                ├── 📄 index.html

> │              └── 📂 30_affidavits_of_service/

> │                └── 📂 10_jurisdiction_service_tr_4_1_b/

> │                  ├── 📄 index.html

> │                └── 📂 20_service_process/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 40_defects_and_contradictions/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 50_default_and_judgment/

> │              └── 📂 10_default_motion/

> │                ├── 📄 index.html

> │              └── 📂 20_default_order/

> │                ├── 📄 index.html

> │              └── 📂 30_judgment_and_decree/

> │                ├── 📄 index.html

> │              └── 📂 40_accounting_inputs/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 60_sale_and_title/

> │              └── 📂 10_sheriff_sale/

> │                ├── 📄 index.html

> │              └── 📂 20_deed/

> │                ├── 📄 index.html

> │              └── 📂 30_recording_gaps/

> │                ├── 📄 index.html

> │              └── 📂 40_possession_claims/

> │                └── 📂 10_sale_and_possession/

> │                  ├── 📄 index.html

> │                └── 📂 30_void_vs_voidable/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 70_writ_and_execution/

> │              └── 📂 10_writ_petition/

> │                ├── 📄 index.html

> │              └── 📂 20_writ_order/

> │                ├── 📄 index.html

> │              └── 📂 30_execution_events/

> │                ├── 📄 index.html

> │              └── 📂 40_notice_failures/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 80_post_removal_conduct/

> │              └── 📂 10_property_interference/

> │                ├── 📄 index.html

> │              └── 📂 20_access_denial/

> │                ├── 📄 index.html

> │              └── 📂 30_spoliation_risk/

> │                ├── 📄 index.html

> │              └── 📂 40_third_party_actions/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 90_damages_and_fallout/

> │              └── 📂 10_property_possession_harms/

> │                ├── 📄 index.html

> │              └── 📂 20_economic_harm/

> │                ├── 📄 index.html

> │              └── 📂 30_financial/

> │                ├── 📄 index.html

> │              └── 📂 40_health_and_safety/

> │                ├── 📄 index.html

> │              └── 📂 50_non_economic_harm/

> │                └── 📂 cold_exposure/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 60_professional_harm/

> │                ├── 📄 index.html

> │              └── 📂 70_remedies_scenarios/

> │                ├── 📄 index.html

> │              └── 📂 80_payout_strategy/

> │                ├── 📄 index.html

> │              └── 📂 90_third_party_harm/

> │                ├── 📄 index.html

> │              └── 📂 Weather_Reports/

> │                ├── 📄 index.html

> │              └── 📂 economic/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │              └── 📂 non-economic/

> │                └── 📂 cold-exposure/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 personal_narrative/

> │                └── 📂 10_Public_Narrative/

> │                  ├── 📄 index.html

> │                └── 📂 20_Exposure_and_Harm/

> │                  └── 📂 Weather_Reports/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 30_Internal_Analysis/

> │                  └── 📂 Payout_Strategy/

> │                    ├── 📄 index.html

> │                  └── 📂 Premonitions/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 40_Donations_and_Support/

> │                  ├── 📄 index.html

> │                └── 📂 50_Timeline/

> │                  ├── 📄 index.html

> │                └── 📂 Premonitions/

> │                  ├── 📄 index.html

> │              └── 📂 settlement/

> │                ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 E_OUTPUTS/

> │            └── 📂 10_binders/

> │              └── 📂 master_case_bible/

> │                └── 📂 _build/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │            └── 📂 _build_artifacts/

> │              ├── 📄 index.html

> │          └── 📂 _ADMIN/

> │            └── 📂 10_index/

> │              ├── 📄 index.html

> │            └── 📂 20_case_logs/

> │              ├── 📄 index.html

> │            └── 📂 30_financial/

> │              ├── 📄 index.html

> │            └── 📂 40_overviews/

> │              └── 📂 10_maps/

> │                ├── 📄 index.html

> │              └── 📂 20_deep_dives/

> │                ├── 📄 index.html

> │              └── 📂 40_debates/

> │                ├── 📄 index.html

> │              └── 📂 50_explainers/

> │                ├── 📄 index.html

> │              └── 📂 60_infographics/

> │                ├── 📄 index.html

> │              └── 📂 70_reports/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 50_protocols/

> │              ├── 📄 index.html

> │            └── 📂 70_templates/

> │              └── 📂 10_motions/

> │                ├── 📄 index.html

> │              └── 📂 20_declarations/

> │                ├── 📄 index.html

> │              └── 📂 30_exhibits/

> │                ├── 📄 index.html

> │              └── 📂 40_orders/

> │                ├── 📄 index.html

> │              └── 📂 50_internal/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 80_integrity_tooling/

> │              ├── 📄 index.html

> │            └── 📂 90_pack_blueprints/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          ├── 📄 index.html

> │      └── 📂 1768577706/

> │        └── 📂 site/

> │      └── 📂 1768577894/

> │        └── 📂 site/

> │      └── 📂 1768578230/

> │        ├── 📄 claims_map.json

> │        ├── 📄 manifest.csv

> │        ├── 📄 manifest.json

> │        ├── 📄 search_index.json

> │        └── 📂 site/

> │          └── 📂 A_TIMELINE/

> │            └── 📂 2023/

> │              ├── 📄 index.html

> │            └── 📂 2024/

> │              ├── 📄 index.html

> │            └── 📂 2025/

> │              └── 📂 events/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 2026/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 B_EVIDENCE/

> │            └── 📂 10_evidence_admin/

> │              ├── 📄 index.html

> │            └── 📂 20_court_record/

> │              └── 📂 10_docket_files/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 30_primary/

> │              └── 📂 aes/

> │                ├── 📄 index.html

> │              └── 📂 fcfcu/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 40_supporting/

> │              └── 📂 docs/

> │                └── 📂 affidavits/

> │                  ├── 📄 index.html

> │                └── 📂 declarations/

> │                  ├── 📄 index.html

> │                └── 📂 receipts/

> │                  ├── 📄 index.html

> │                └── 📂 records/

> │                  ├── 📄 index.html

> │              ├── 📄 index.html

> │              └── 📂 multi-media/

> │                ├── 📄 index.html

> │              └── 📂 property/

> │                └── 📂 10_mortgage_history/

> │                  └── 📂 10_payments/

> │                    ├── 📄 index.html

> │                └── 📂 20_parcel/

> │                  ├── 📄 index.html

> │            └── 📂 50_quarantine_candidates/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 C_VIS/

> │            └── 📂 10_violations/

> │              ├── 📄 index.html

> │            └── 📂 20_theories/

> │              ├── 📄 index.html

> │            └── 📂 30_legal_research/

> │              ├── 📄 index.html

> │            └── 📂 40_analysis/

> │              ├── 📄 index.html

> │            └── 📂 50_strategies/

> │              ├── 📄 index.html

> │            └── 📂 60_data_inventories/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 D_PHASES/

> │            └── 📂 100_post_judgment_and_federal/

> │              └── 📂 10_motions/

> │                └── 📂 10_claims_motions/

> │                  └── 📂 Supplemental/

> │                    └── 📂 01_drafts/

> │                      ├── 📄 index.html

> │                    └── 📂 02_exhibits/

> │                      ├── 📄 index.html

> │                    └── 📂 04_filed_receipts/

> │                      ├── 📄 index.html

> │                  └── 📂 filings/

> │                    └── 📂 10_2025-12-10_motion_vacate/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 index.html

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 index.html

> │                      └── 📂 03_proposed_order/

> │                        ├── 📄 index.html

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 index.html

> │                      ├── 📄 index.html

> │                    └── 📂 20_2025-12-11_Supplemental_Emergency_Motion_Access/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 index.html

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 index.html

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 index.html

> │                      ├── 📄 index.html

> │                    └── 📂 30_draft_motions/

> │                      ├── 📄 index.html

> │                      └── 📂 motions/

> │                        ├── 📄 index.html

> │                  ├── 📄 index.html

> │                  └── 📂 motion_vacate/

> │                    └── 📂 01_drafts/

> │                      ├── 📄 index.html

> │                    └── 📂 02_exhibits/

> │                      ├── 📄 index.html

> │                    └── 📂 03_proposed_order/

> │                      ├── 📄 index.html

> │                    └── 📂 04_filed_receipts/

> │                      ├── 📄 index.html

> │                    ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 20_orders/

> │                └── 📂 10_proposed_orders/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │                └── 📂 orders/

> │                  ├── 📄 index.html

> │              └── 📂 30_regulatory_complaints/

> │                ├── 📄 index.html

> │              └── 📂 40_federal_preservation/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 10_inbox_working/

> │              └── 📂 _staging/

> │                └── 📂 _dupes_hold/

> │                  ├── 📄 index.html

> │                └── 📂 _html_hold/

> │                  ├── 📄 index.html

> │              └── 📂 evidence_staging/

> │                └── 📂 exhibit_candidates/

> │                  └── 📂 10_exposure_and_harm/

> │                    ├── 📄 index.html

> │                    └── 📂 weather_reports/

> │                      ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 potential_exhibits/

> │                  ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 20_pre_foreclosure/

> │              └── 📂 10_account_history/

> │                ├── 📄 index.html

> │              └── 📂 20_hardship_and_ada/

> │                ├── 📄 index.html

> │              └── 📂 30_communications/

> │                ├── 📄 index.html

> │              └── 📂 40_payments_and_disputes/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 30_foreclosure_filing/

> │              └── 📂 10_complaint/

> │                ├── 📄 index.html

> │              └── 📂 20_summons/

> │                ├── 📄 index.html

> │              └── 📂 30_lien_parties/

> │                ├── 📄 index.html

> │              └── 📂 40_docket_snapshots/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 40_service_and_notice/

> │              └── 📂 10_sheriff_returns/

> │                ├── 📄 index.html

> │              └── 📂 20_mailings/

> │                ├── 📄 index.html

> │              └── 📂 30_affidavits_of_service/

> │                └── 📂 10_jurisdiction_service_tr_4_1_b/

> │                  ├── 📄 index.html

> │                └── 📂 20_service_process/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 40_defects_and_contradictions/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 50_default_and_judgment/

> │              └── 📂 10_default_motion/

> │                ├── 📄 index.html

> │              └── 📂 20_default_order/

> │                ├── 📄 index.html

> │              └── 📂 30_judgment_and_decree/

> │                ├── 📄 index.html

> │              └── 📂 40_accounting_inputs/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 60_sale_and_title/

> │              └── 📂 10_sheriff_sale/

> │                ├── 📄 index.html

> │              └── 📂 20_deed/

> │                ├── 📄 index.html

> │              └── 📂 30_recording_gaps/

> │                ├── 📄 index.html

> │              └── 📂 40_possession_claims/

> │                └── 📂 10_sale_and_possession/

> │                  ├── 📄 index.html

> │                └── 📂 30_void_vs_voidable/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 70_writ_and_execution/

> │              └── 📂 10_writ_petition/

> │                ├── 📄 index.html

> │              └── 📂 20_writ_order/

> │                ├── 📄 index.html

> │              └── 📂 30_execution_events/

> │                ├── 📄 index.html

> │              └── 📂 40_notice_failures/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 80_post_removal_conduct/

> │              └── 📂 10_property_interference/

> │                ├── 📄 index.html

> │              └── 📂 20_access_denial/

> │                ├── 📄 index.html

> │              └── 📂 30_spoliation_risk/

> │                ├── 📄 index.html

> │              └── 📂 40_third_party_actions/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 90_damages_and_fallout/

> │              └── 📂 10_property_possession_harms/

> │                ├── 📄 index.html

> │              └── 📂 20_economic_harm/

> │                ├── 📄 index.html

> │              └── 📂 30_financial/

> │                ├── 📄 index.html

> │              └── 📂 40_health_and_safety/

> │                ├── 📄 index.html

> │              └── 📂 50_non_economic_harm/

> │                └── 📂 cold_exposure/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 60_professional_harm/

> │                ├── 📄 index.html

> │              └── 📂 70_remedies_scenarios/

> │                ├── 📄 index.html

> │              └── 📂 80_payout_strategy/

> │                ├── 📄 index.html

> │              └── 📂 90_third_party_harm/

> │                ├── 📄 index.html

> │              └── 📂 Weather_Reports/

> │                ├── 📄 index.html

> │              └── 📂 economic/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │              └── 📂 non-economic/

> │                └── 📂 cold-exposure/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 personal_narrative/

> │                └── 📂 10_Public_Narrative/

> │                  ├── 📄 index.html

> │                └── 📂 20_Exposure_and_Harm/

> │                  └── 📂 Weather_Reports/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 30_Internal_Analysis/

> │                  └── 📂 Payout_Strategy/

> │                    ├── 📄 index.html

> │                  └── 📂 Premonitions/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 40_Donations_and_Support/

> │                  ├── 📄 index.html

> │                └── 📂 50_Timeline/

> │                  ├── 📄 index.html

> │                └── 📂 Premonitions/

> │                  ├── 📄 index.html

> │              └── 📂 settlement/

> │                ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 E_OUTPUTS/

> │            └── 📂 10_binders/

> │              └── 📂 master_case_bible/

> │                └── 📂 _build/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │            └── 📂 _build_artifacts/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │            └── 📂 vis/

> │              ├── 📄 index.html

> │          └── 📂 _ADMIN/

> │            └── 📂 10_index/

> │              ├── 📄 index.html

> │            └── 📂 20_case_logs/

> │              ├── 📄 index.html

> │            └── 📂 30_financial/

> │              ├── 📄 index.html

> │            └── 📂 40_overviews/

> │              └── 📂 10_maps/

> │                ├── 📄 index.html

> │              └── 📂 20_deep_dives/

> │                ├── 📄 index.html

> │              └── 📂 40_debates/

> │                ├── 📄 index.html

> │              └── 📂 50_explainers/

> │                ├── 📄 index.html

> │              └── 📂 60_infographics/

> │                ├── 📄 index.html

> │              └── 📂 70_reports/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 50_protocols/

> │              ├── 📄 index.html

> │            └── 📂 70_templates/

> │              └── 📂 10_motions/

> │                ├── 📄 index.html

> │              └── 📂 20_declarations/

> │                ├── 📄 index.html

> │              └── 📂 30_exhibits/

> │                ├── 📄 index.html

> │              └── 📂 40_orders/

> │                ├── 📄 index.html

> │              └── 📂 50_internal/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 80_integrity_tooling/

> │              ├── 📄 index.html

> │            └── 📂 90_pack_blueprints/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          ├── 📄 index.html

> │      ├── 📄 latest.txt

> │  ├── 📄 NT_README.md

> │  └── 📂 _ADMIN/

> │    └── 📂 10_index/

> │      ├── 📄 NT_00_index.md

> │      ├── 📄 NT_Contacts.md

> │    └── 📂 20_case_logs/

> │      ├── 📄 NT_2025-12-09_Writ_Executed_Forced_Removal.md

> │      ├── 📄 NT_2025-12-15_Case_DNA_Strategy_Checkpoint.md

> │      ├── 📄 NT_2025-12-15_Strategic_Planning_Session.md

> │      ├── 📄 NT_2025-12-16_Post_Removal_Access_Denial.md

> │      ├── 📄 NT_2025-12-16_case_log_entry.md

> │      ├── 📄 NT_2025-12-16_case_summary.md

> │      ├── 📄 NT_2025-12-16_fcfcu_case_dna_strat.md

> │      ├── 📄 NT_2025-12-21_Case_Summary.md

> │      ├── 📄 NT_2026-01-16_Cleanup_Log.md

> │      ├── 📄 NT_20_case_logs.md

> │      ├── 📄 NT_INGEST_2025-12-16_case_log_entry.md

> │      ├── 📄 NT_Master_Case_Log.md

> │      ├── 📄 NT_content_manifest_hashes.json

> │      ├── 📄 NT_ingest_dedupe_manifest.json

> │      ├── 📄 PL_integrity_scan_report.json

> │    └── 📂 30_financial/

> │      ├── 📄 NT_02_financial.md

> │      ├── 📄 NT_Financial_Tracker.md

> │    └── 📂 40_overviews/

> │      └── 📂 10_maps/

> │        ├── 📄 NT_Procedural_failure_map_one_pager.md

> │      └── 📂 20_deep_dives/

> │        ├── 📄 NT_Integrate_Disability_Separate_Appeals_Get_Stay.m4a

> │        ├── 📄 NT_foreclosure_void_versus_damages_due_process.m4a

> │        ├── 📄 NT_forensic_audit_of_a_void_foreclosure.m4a

> │        ├── 📄 OR_foreclosure_void_judgment_institutional_failur.m4a

> │      └── 📂 30_critiques/

> │      └── 📂 40_debates/

> │        ├── 📄 NT_debate.m4a

> │      └── 📂 50_explainers/

> │        ├── 📄 NT_crisis_the_anatomy_of_institutional_failure.pdf

> │        ├── 📄 NT_wrongful_foreclosure_a_case_study_in_civil_rig.pdf

> │        ├── 📄 OR_void_judgment_eviction_crisis.pdf

> │      └── 📂 60_infographics/

> │        ├── 📄 OR_Void_Judgment_Eviction_Crisis.pdf

> │      └── 📂 70_reports/

> │        ├── 📄 NT_Crisis_The_Anatomy_of_Institutional_Failure.pdf

> │        ├── 📄 NT_Wrongful_Foreclosure_A_Case_Study_in_Civil_Rig.pdf

> │        ├── 📄 NT__Session_Summary_2025-12-15_i_knew_b.md

> │        ├── 📄 NT_case-narrative-wrongful-foreclosure-and-displ.html

> │        ├── 📄 NT_legal-memorandum.html

> │        ├── 📄 NT_procedural_failure_map_one_pager.html

> │        ├── 📄 NT_talking_points.html

> │        ├── 📄 NT_uncategorized_bundle.pdf

> │        ├── 📄 OR_Void_Judgment_Eviction_Crisis.pdf

> │        ├── 📄 PL_70_reports.md

> │        ├── 📄 PL_proposal-for-strategic-reports-in-the-matter-.html

> │      ├── 📄 NT_10_overviews.md

> │    └── 📂 50_protocols/

> │      ├── 📄 NT_PROTOCOL_Canonical_Case_Knowledge_Base.md

> │    └── 📂 70_templates/

> │      └── 📂 10_motions/

> │        ├── 📄 MO_10_motions.md

> │        ├── 📄 MO_TEMPLATE_motion_emergency_stay_of_writ.md

> │        ├── 📄 MO_TEMPLATE_motion_emergency_supplemental_motion_ongoing_ha.md

> │        ├── 📄 MO_TEMPLATE_motion_to_vacate_void_judgment.md

> │      └── 📂 20_declarations/

> │        ├── 📄 NT_GUIDE_Witness_Instructions.md

> │        ├── 📄 NT_TEMPLATE_Gender_Identity_Clarification.md

> │        ├── 📄 PL_20_declarations.md

> │        ├── 📄 PL_TEMPLATE_ADA_Disability_Affidavit.md

> │        ├── 📄 PL_TEMPLATE_Character_Affidavit.md

> │        ├── 📄 PL_TEMPLATE_Community_Service_Affidavit.md

> │        ├── 📄 PL_TEMPLATE_Credibility_Affidavit.md

> │        ├── 📄 PL_TEMPLATE_Declarations.md

> │        ├── 📄 PL_TEMPLATE_Observations_Affidavit.md

> │        ├── 📄 PL_TEMPLATE_affidavit_not_served.md

> │        ├── 📄 PL_TEMPLATE_updated_affidavit_language.md

> │        ├── 📄 PL_TEMPLATE_verified_affidavit_of_defendant.md

> │      └── 📂 30_exhibits/

> │        ├── 📄 EXH_30_exhibits.md

> │        ├── 📄 EXH_TEMPLATE_Exhibit_List.md

> │      └── 📂 40_orders/

> │        ├── 📄 MO_TEMPLATE_proposed_order_motion_to_vacate.md

> │        ├── 📄 OR_40_orders.md

> │        ├── 📄 OR_TEMPLATE_Proposed_Order.md

> │        ├── 📄 OR_TEMPLATE_proposed_order_emergency_stay.md

> │      └── 📂 50_internal/

> │        ├── 📄 NT_TEMPLATE_Advocate_Outreach.md

> │        ├── 📄 NT_TEMPLATE_Court_Doc.md

> │        ├── 📄 NT_TEMPLATE_Fact_Timeline.md

> │        ├── 📄 NT_TEMPLATE_Handup_Packet_Note.md

> │        ├── 📄 NT_TEMPLATE_Section_Cover.md

> │        ├── 📄 NT_TEMPLATE_Section_Index.md

> │        ├── 📄 NT_TEMPLATE_Service_Matrix.md

> │        ├── 📄 NT_TEMPLATE_Timeline_Event.md

> │        ├── 📄 NT_TEMPLATE_Violation_Entry.md

> │        ├── 📄 NT_TEMPLATE_War_Note.md

> │        ├── 📄 NT_TEMPLATE_ada_packet.md

> │        ├── 📄 NT_TEMPLATE_attorney_brief.md

> │        ├── 📄 NT_TEMPLATE_receipt_usps_tracking.md

> │        ├── 📄 NT_TEMPLATE_script_call_lawyers.md

> │      ├── 📄 NT_40_templates.md

> │    └── 📂 80_integrity_tooling/

> │      ├── 📄 NT_50_integrity_tooling.md

> │      ├── 📄 NT_rename_plan.txt

> │      ├── 📄 NT_run_renames.ps1

> │      ├── 📄 PL_conflicts_report.txt

> │    └── 📂 90_pack_blueprints/

> │      ├── 📄 NT_60_pack_blueprints.md

> │      ├── 📄 NT_PACK_AGENCY.yaml

> │      ├── 📄 NT_PACK_JUDGE.yaml

> │      ├── 📄 NT_PACK_OPPOSING.yaml

> │      ├── 📄 NT_PACK_SELF.yaml

> │      ├── 📄 NT_PROPOSED_OUTPUT_STRUCTURE.md

> │    ├── 📄 NT_00_ADMIN.md

> └── 📂 launcher/

> │  ├── 📄 main.py

> │  ├── 📄 requirements.txt

> │  ├── 📄 styles.qss

> └── 📂 logs/

> │  └── 📂 migrations/

> │    ├── 📄 migration_log.csv

> │  └── 📂 sessions/

> │    ├── 📄 Session_Summary_2025-12-16_fcfcu_case_dna_str_1.md

> │    ├── 📄 Session_Summary_2025-12-16_fcfcu_case_dna_strat.md

> └── 📂 scripts/

> │  └── 📂 audit/

> │    ├── 📄 check_integrity.py

> │    ├── 📄 find_collisions.py

> │    ├── 📄 generate_audit_csv.py

> │    ├── 📄 scan_properties.py

> │  └── 📂 maintenance/

> │    ├── 📄 apply_audit_corrections.py

> │    ├── 📄 enforce_prefixes.py

> │    ├── 📄 repair_front_matter.py

> │    ├── 📄 resequence_folders.py

> │    ├── 📄 strip_legacy_ids.py

> │    ├── 📄 sync_csv_data.py

> │  └── 📂 vis/

> │    ├── 📄 README.md

> │    ├── 📄 lint_c_vis.py

> │    ├── 📄 run_vis.ps1

> │    ├── 📄 run_vis.sh

> │  └── 📂 vitepress/

> │    ├── 📄 build_and_serve.ps1

> │    ├── 📄 sync_vis_to_docs.ps1

> │    ├── 📄 sync_vis_to_docs.sh

> ├── 📄 start.bat

> └── 📄 wrangler.toml

> ```

### Assistant
> You’re **very close** on structure. The *architecture* is solid. What’s not “spot on” yet is **hygiene + duplication control**—and that’s the part that will quietly wreck you later (search results, TOCs, hashes, and “what’s canonical?” fights).
> 
> ## What’s solid (keep it)
> - **`content/` as your canonical knowledge base** (A_TIMELINE / B_EVIDENCE / C_VIS / D_PHASES / E_OUTPUTS). This is the right mental model.
> - Clear separation between:
>   - **Evidence** (B_EVIDENCE),
>   - **Analysis/strategy** (C_VIS),
>   - **Procedural phases** (D_PHASES),
>   - **Outputs/builds** (E_OUTPUTS).
> - Having **`app/` for the software** and **`content/` for the case corpus** is correct.
> 
> ## What still needs fixes (do these or you’ll regret it)
> 
> ### 1) You have **two “VIS” universes** (duplication risk)
> I see:
> - `content/C_VIS/...`
> - `app/vitepress/.../_outputs/vis/...`
> - and also `vis/` at repo root (or under app)
> 
> That’s fine **only if** you enforce this rule:
> 
> **Rule:** `content/C_VIS/**` is *source-of-truth*.  
> Everything under `app/**/_outputs/**` (and `E_OUTPUTS/**`) is **generated** and can be deleted/rebuilt any time.
> 
> If you don’t enforce that rule, you’ll end up editing generated files, then wondering why the rebuild “lost” your work.
> 
> **Fix:** add a `README.md` in:
> - `content/C_VIS/` → “SOURCE”
> - `app/vitepress/docs/_outputs/vis/` → “GENERATED – DO NOT EDIT”
> - `content/E_OUTPUTS/` → “GENERATED – OK TO DELETE/REBUILD”
> 
> ### 2) Your tree contains **compiled trash you should not version**
> You have `__pycache__/` and `*.pyc` showing up inside services. That should never be committed.
> 
> **Fix:** `.gitignore` must include:
> - `__pycache__/`
> - `*.pyc`
> - `.DS_Store`
> - `node_modules/`
> - `.next/`
> - `dist/`
> - `.vitepress/dist/`
> - `app/vitepress/docs/_outputs/**` (optional if you treat it as fully generated)
> 
> ### 3) You still have **dupe filenames** everywhere
> Examples:
> - `something 1.md`
> - `(2).md`
> - `.pdf.pdf`
> - `EXH__026_...` vs `EXH_026_...`
> 
> This will break:
> - manifest generation,
> - stable hashing,
> - cross-linking,
> - and it will inflate your “evidence count” with fake duplicates.
> 
> **Fix:** pick one canonical naming convention and normalize:
> - Remove ` (1)` ` (2)` and ` 1` suffixes.
> - Fix double extensions.
> - Collapse double-underscore variants to single underscore.
> 
> This is exactly what your **Option B script** should automate.
> 
> ### 4) Inconsistent casing and path semantics
> You have both:
> - `Weather_Reports/` and `weather_reports/`
> - `cold_exposure/` and `cold-exposure/`
> 
> On Windows you might skate by. On Linux + static site builds, you’ll get silent broken links.
> 
> **Fix:** choose one:
> - Either `snake_case` everywhere (recommended),
> - or `kebab-case` everywhere.
> 
> Given your current structure and existing files: **snake_case** is the least painful.
> 
> ### 5) “Primary evidence” folder naming is inconsistent
> I see earlier you had `B_EVIDENCE/30_primary/aes/` and now you’ve got `B_EVIDENCE/30_primary/10_fcfcu/` + `20_aes/`.
> 
> Both are valid, but pick one scheme:
> 
> **Recommended:** keep the numeric subfolders (stable ordering)
> - `B_EVIDENCE/30_primary/10_fcfcu/`
> - `B_EVIDENCE/30_primary/20_aes/`
> - and (later) `30_experian/`, etc.
> 
> If you keep both styles mixed, it’s messy for humans and scripts.
> 
> ## Verdict
> - **Structure:** 9/10 (good enough to proceed)
> - **Operational hygiene:** 5/10 (must fix now, before you generate more outputs)
> 
> If you fix the five items above, you’re “spot on.”
> 
> ## Next move (no questions, just action)
> Since you already chose **Option B (the script)**, the script should do, in this order:
> 
> 1) Scan for junk: `__pycache__`, `.pyc`, `.DS_Store`, etc.  
> 2) Scan for dupes: ` 1`, `(2)`, `__`, `.pdf.pdf`  
> 3) Produce:
>    - `NT_rename_plan.txt` (you already have one—good)
>    - `PL_conflicts_report.txt`
>    - a **dry-run** rename map (old → new)
> 4) Apply renames (only after dry-run output exists)
> 5) Rebuild indexes + manifests
> 
> If you want, paste your current `NT_rename_plan.txt` and I’ll tell you—bluntly—whether it’s safe to run or if it’s about to nuke something important.

### User
> gemini is off duty for a few days i hit limit so how do i get you what you need.

### Assistant
> Perfect timing actually. You don’t need Gemini for this part. This is **Codex / me territory** and we can do it cleanly and safely.
> 
> I’ll be very explicit so you don’t overshare or miss anything.
> 
> ---
> 
> ## What I need from you (minimum, in order)
> 
> ### 1️⃣ A **tree snapshot** of the repo (paths only, no file contents)
> From repo root, run **one** of these and paste the output.
> 
> #### PowerShell (recommended on Windows)
> ```powershell
> tree /F /A | Out-String -Width 4096
> ```
> 
> If that’s too big, limit it:
> ```powershell
> tree content /F /A
> tree app /F /A
> ```
> 
> I need to see:
> - folder hierarchy
> - filenames
> - duplication patterns
> - casing / spacing issues
> 
> I do **not** need file contents yet.
> 
> ---
> 
> ### 2️⃣ Your current `.gitignore`
> Paste it verbatim.
> 
> This tells me:
> - what junk is already controlled
> - what is leaking into source
> - whether outputs are being accidentally tracked
> 
> ---
> 
> ### 3️⃣ One sample of each “problem type” (paths only)
> You don’t need to paste files—just **paths** that demonstrate issues.
> 
> Example format (copy this style):
> 
> ```
> DUPLICATE EXAMPLES:
> content/B_EVIDENCE/30_primary/aes/bill.pdf
> content/B_EVIDENCE/30_primary/aes/bill (1).pdf
> 
> DOUBLE EXTENSION:
> content/B_EVIDENCE/30_primary/fcfcu/statement.pdf.pdf
> 
> UNDERSCORE ISSUE:
> content/C_VIS/10_violations/EXH__026_cost_shift.md
> content/C_VIS/10_violations/EXH_026_cost_shift.md
> ```
> 
> 3–5 examples per issue is enough.
> 
> ---
> 
> ### 4️⃣ Confirm one rule (important)
> Answer this with **yes or no**:
> 
> > Are we allowed to automatically rename files as long as:
> > - a dry-run plan is generated first
> > - original → new mapping is saved
> > - no file contents are changed
> 
> If **yes**, I’ll generate:
> - a safe audit
> - a rename plan
> - a reversible script
> 
> If **no**, we stay in report-only mode.
> 
> ---
> 
> ## What I will do once you send those
> 
> I will produce, in this order:
> 
> 1) **Repository Audit Report**
>    - structural issues
>    - redundancy clusters
>    - broken semantic boundaries (source vs generated)
>    - casing & path conflicts
>    - future pain points (search, hashing, VitePress)
> 
> 2) **Normalization Ruleset**
>    - one naming convention
>    - one casing standard
>    - one folder semantic per tier
> 
> 3) **Dry-Run Rename Plan**
>    - `OLD_PATH → NEW_PATH`
>    - grouped by risk level
>    - nothing executed yet
> 
> 4) **Codex-ready instruction**
>    - a single prompt you can hand to Codex to:
>      - validate
>      - apply renames
>      - re-run VIS
>      - re-sync VitePress
> 
> No guesswork. No UI. No magic.
> 
> ---
> 
> ## What NOT to send (important)
> - Do **not** paste entire file contents yet
> - Do **not** zip anything
> - Do **not** start renaming manually
> 
> We lock the map **before** moving pieces.
> 
> ---
> 
> ### Next step
> Paste **(1) tree output**, **(2) .gitignore**, **(3) examples**, then answer **(4)**.
> 
> Once that’s in, I’ll take point and we’ll get this squeaky clean without breaking your case record.

### User
> {'asset_pointer': 'sediment://file_000000003360722f993c66eae856bd9b', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 356, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 89080, 'width': 804}{'asset_pointer': 'sediment://file_00000000cab0720cb5350e97d5c577e9', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 356, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 89080, 'width': 804}the tree gets cut off, there is not gitignore at root, and yes, ```markdown

> . 📂 CASE_FCFCU

> ├── 📄 CASE_ENGINE.py

> ├── 📄 CASE_FCFCU.code-workspace

> └── 📂 app/

> │  └── 📂 Legalmind/

> │    ├── 📄 CONTRIBUTING.md

> │    ├── 📄 LICENSE

> │    ├── 📄 PLATFORM_README.md

> │    ├── 📄 PROJECT-OVERVIEW.md

> │    ├── 📄 README.md

> │    └── 📂 backend/

> │      └── 📂 agent-orchestrator/

> │        ├── 📄 Dockerfile

> │        ├── 📄 main.py

> │        ├── 📄 requirements.txt

> │        └── 📂 services/

> │          ├── 📄 __init__.py

> │          ├── 📄 debate_manager.py

> │          ├── 📄 dynamic_agent.py

> │          ├── 📄 fixed_agent.py

> │          ├── 📄 legal_reference_engine.py

> │          ├── 📄 retry_handler.py

> │          ├── 📄 websocket_manager.py

> │      └── 📂 api-gateway/

> │        ├── 📄 Dockerfile

> │        ├── 📄 main.py

> │        ├── 📄 requirements.txt

> │      └── 📂 parser-service/

> │        ├── 📄 Dockerfile

> │        ├── 📄 main.py

> │        ├── 📄 requirements.txt

> │        └── 📂 services/

> │          ├── 📄 __init__.py

> │          ├── 📄 document_processor.py

> │          ├── 📄 entity_extractor.py

> │          ├── 📄 firestore_client.py

> │          ├── 📄 pii_redactor.py

> │          ├── 📄 pubsub_client.py

> │          ├── 📄 storage_client.py

> │      └── 📂 report-generator/

> │        ├── 📄 Dockerfile

> │        ├── 📄 main.py

> │        ├── 📄 requirements.txt

> │        ├── 📄 subscriber.py

> │      └── 📂 role-assignment/

> │        ├── 📄 Dockerfile

> │        ├── 📄 main.py

> │        ├── 📄 requirements.txt

> │        └── 📂 services/

> │          ├── 📄 __init__.py

> │          ├── 📄 agent_pool_manager.py

> │          ├── 📄 firestore_client.py

> │          ├── 📄 pubsub_client.py

> │          ├── 📄 role_analyzer.py

> │      └── 📂 video-generator/

> │        ├── 📄 Dockerfile

> │        ├── 📄 main.py

> │        ├── 📄 main_ai_video.py

> │        ├── 📄 main_veo3.py

> │        ├── 📄 requirements.txt

> │        ├── 📄 subscriber.py

> │      └── 📂 vis-service/

> │        ├── 📄 Dockerfile

> │        └── 📂 __pycache__/

> │          ├── 📄 main.cpython-311.pyc

> │        ├── 📄 main.py

> │        ├── 📄 requirements.txt

> │        └── 📂 services/

> │          ├── 📄 __init__.py

> │          └── 📂 __pycache__/

> │            ├── 📄 __init__.cpython-311.pyc

> │            ├── 📄 claims_mapper.cpython-311.pyc

> │            ├── 📄 hasher.cpython-311.pyc

> │            ├── 📄 indexer.cpython-311.pyc

> │            ├── 📄 metadata.cpython-311.pyc

> │            ├── 📄 scanner.cpython-311.pyc

> │            ├── 📄 storage_adapter.cpython-311.pyc

> │          ├── 📄 claims_mapper.py

> │          ├── 📄 hasher.py

> │          ├── 📄 indexer.py

> │          ├── 📄 metadata.py

> │          ├── 📄 scanner.py

> │          ├── 📄 storage_adapter.py

> │        ├── 📄 vis.yaml

> │    ├── 📄 deploy-to-github.sh

> │    └── 📂 docs/

> │      ├── 📄 DEPLOYMENT.md

> │      └── 📂 backend-docs/

> │        ├── 📄 01-parser-service-COMPLETE.md

> │        ├── 📄 02-api-gateway-COMPLETE.md

> │        ├── 📄 03-agent-orchestrator-COMPLETE.md

> │        ├── 📄 04-role-assignment-COMPLETE.md

> │        ├── 📄 05-video-generator-COMPLETE.md

> │        ├── 📄 06-report-generator-COMPLETE.md

> │        ├── 📄 AGENT_ORCHESTRATOR_SUMMARY.md

> │        ├── 📄 COMPLETE_SYSTEM_GUIDE.md

> │        ├── 📄 DOCUMENTATION_SUMMARY.md

> │        ├── 📄 README.md

> │        ├── 📄 ROLE_ASSIGNMENT_SUMMARY.md

> │      └── 📂 diagrams/

> │        ├── 📄 README.md

> │        ├── 📄 SYSTEM-ARCHITECTURE.md

> │        ├── 📄 SYSTEM-WORKFLOW.md

> │      └── 📂 frontend-docs/

> │        ├── 📄 01-FRONTEND-ARCHITECTURE-COMPLETE.md

> │        ├── 📄 02-PAGES-AND-COMPONENTS.md

> │        ├── 📄 03-API-AND-WEBSOCKET.md

> │        ├── 📄 ALIGNMENT-VERIFICATION.md

> │        ├── 📄 COMPLETE-FRONTEND-GUIDE.md

> │        ├── 📄 DOCUMENTATION-COMPLETE.md

> │        ├── 📄 FRONTEND-DOCUMENTATION-SUMMARY.md

> │        ├── 📄 README.md

> │    └── 📂 frontend/

> │      ├── 📄 Dockerfile

> │      ├── 📄 README.md

> │      ├── 📄 next.config.js

> │      ├── 📄 package.json

> │      ├── 📄 postcss.config.js

> │      └── 📂 public/

> │        ├── 📄 README.md

> │      └── 📂 src/

> │        └── 📂 app/

> │          └── 📂 chat/

> │            └── 📂 [sessionId]/

> │              ├── 📄 page.tsx

> │          ├── 📄 globals.css

> │          ├── 📄 layout.tsx

> │          ├── 📄 page.tsx

> │          └── 📂 results/

> │            └── 📂 [sessionId]/

> │              ├── 📄 page.tsx

> │          └── 📂 upload/

> │            ├── 📄 page.tsx

> │        └── 📂 components/

> │          ├── 📄 MessageBubble.tsx

> │          ├── 📄 StageProgress.tsx

> │        └── 📂 lib/

> │          ├── 📄 api.ts

> │          ├── 📄 utils.ts

> │          ├── 📄 websocket-native.ts

> │        └── 📂 types/

> │          ├── 📄 index.ts

> │      ├── 📄 tailwind.config.ts

> │      ├── 📄 tsconfig.json

> │    └── 📂 infrastructure/

> │      └── 📂 bigquery/

> │        ├── 📄 add_criminal_offences.py

> │        ├── 📄 add_marriage_laws.py

> │        ├── 📄 add_marriage_relationship_laws.py

> │        ├── 📄 add_more_ipc_sections.py

> │        ├── 📄 add_murder_related_laws.py

> │        ├── 📄 add_property_offences.py

> │        ├── 📄 add_relationship_laws.py

> │        ├── 📄 add_serious_crimes.py

> │        ├── 📄 add_traffic_laws.py

> │        ├── 📄 add_us_laws.py

> │        ├── 📄 comprehensive_laws.sql

> │        ├── 📄 populate_comprehensive_laws.py

> │        ├── 📄 populate_data.py

> │        ├── 📄 sample_data.sql

> │        ├── 📄 schema.sql

> │        ├── 📄 verify_all_laws.sh

> │        ├── 📄 verify_database.py

> │      └── 📂 cloud-run/

> │        ├── 📄 deploy.sh

> │        ├── 📄 service-template.yaml

> │      ├── 📄 deploy_all.sh

> │      └── 📂 firestore/

> │        ├── 📄 firestore.rules

> │        ├── 📄 schema.md

> │  └── 📂 vitepress/

> │    └── 📂 docs/

> │      └── 📂 _outputs/

> │        └── 📂 vis/

> │          ├── 📄 claims_map.json

> │          ├── 📄 index.md

> │          ├── 📄 manifest.csv

> │          ├── 📄 manifest.json

> │          ├── 📄 search_index.json

> │          └── 📂 site/

> │            └── 📂 A_TIMELINE/

> │              └── 📂 2023/

> │                ├── 📄 index.html

> │              └── 📂 2024/

> │                ├── 📄 index.html

> │              └── 📂 2025/

> │                └── 📂 events/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 2026/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 B_EVIDENCE/

> │              └── 📂 10_evidence_admin/

> │                ├── 📄 index.html

> │              └── 📂 20_court_record/

> │                └── 📂 10_docket_files/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 30_primary/

> │                └── 📂 aes/

> │                  ├── 📄 index.html

> │                └── 📂 fcfcu/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 40_supporting/

> │                └── 📂 docs/

> │                  └── 📂 affidavits/

> │                    ├── 📄 index.html

> │                  └── 📂 declarations/

> │                    ├── 📄 index.html

> │                  └── 📂 receipts/

> │                    ├── 📄 index.html

> │                  └── 📂 records/

> │                    ├── 📄 index.html

> │                ├── 📄 index.html

> │                └── 📂 multi-media/

> │                  ├── 📄 index.html

> │                └── 📂 property/

> │                  └── 📂 10_mortgage_history/

> │                    └── 📂 10_payments/

> │                      ├── 📄 index.html

> │                  └── 📂 20_parcel/

> │                    ├── 📄 index.html

> │              └── 📂 50_quarantine_candidates/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 C_VIS/

> │              └── 📂 10_violations/

> │                ├── 📄 index.html

> │              └── 📂 20_theories/

> │                ├── 📄 index.html

> │              └── 📂 30_legal_research/

> │                ├── 📄 index.html

> │              └── 📂 40_analysis/

> │                ├── 📄 index.html

> │              └── 📂 50_strategies/

> │                ├── 📄 index.html

> │              └── 📂 60_data_inventories/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 D_PHASES/

> │              └── 📂 100_post_judgment_and_federal/

> │                └── 📂 10_motions/

> │                  └── 📂 10_claims_motions/

> │                    └── 📂 Supplemental/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 index.html

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 index.html

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 index.html

> │                    └── 📂 filings/

> │                      └── 📂 10_2025-12-10_motion_vacate/

> │                        └── 📂 01_drafts/

> │                          ├── 📄 index.html

> │                        └── 📂 02_exhibits/

> │                          ├── 📄 index.html

> │                        └── 📂 03_proposed_order/

> │                          ├── 📄 index.html

> │                        └── 📂 04_filed_receipts/

> │                          ├── 📄 index.html

> │                        ├── 📄 index.html

> │                      └── 📂 20_2025-12-11_Supplemental_Emergency_Motion_Access/

> │                        └── 📂 01_drafts/

> │                          ├── 📄 index.html

> │                        └── 📂 02_exhibits/

> │                          ├── 📄 index.html

> │                        └── 📂 04_filed_receipts/

> │                          ├── 📄 index.html

> │                        ├── 📄 index.html

> │                      └── 📂 30_draft_motions/

> │                        ├── 📄 index.html

> │                        └── 📂 motions/

> │                          ├── 📄 index.html

> │                    ├── 📄 index.html

> │                    └── 📂 motion_vacate/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 index.html

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 index.html

> │                      └── 📂 03_proposed_order/

> │                        ├── 📄 index.html

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 index.html

> │                      ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 20_orders/

> │                  └── 📂 10_proposed_orders/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                  └── 📂 orders/

> │                    ├── 📄 index.html

> │                └── 📂 30_regulatory_complaints/

> │                  ├── 📄 index.html

> │                └── 📂 40_federal_preservation/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 10_inbox_working/

> │                └── 📂 _staging/

> │                  └── 📂 _dupes_hold/

> │                    ├── 📄 index.html

> │                  └── 📂 _html_hold/

> │                    ├── 📄 index.html

> │                └── 📂 evidence_staging/

> │                  └── 📂 exhibit_candidates/

> │                    └── 📂 10_exposure_and_harm/

> │                      ├── 📄 index.html

> │                      └── 📂 weather_reports/

> │                        ├── 📄 index.html

> │                    ├── 📄 index.html

> │                  └── 📂 potential_exhibits/

> │                    ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 20_pre_foreclosure/

> │                └── 📂 10_account_history/

> │                  ├── 📄 index.html

> │                └── 📂 20_hardship_and_ada/

> │                  ├── 📄 index.html

> │                └── 📂 30_communications/

> │                  ├── 📄 index.html

> │                └── 📂 40_payments_and_disputes/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 30_foreclosure_filing/

> │                └── 📂 10_complaint/

> │                  ├── 📄 index.html

> │                └── 📂 20_summons/

> │                  ├── 📄 index.html

> │                └── 📂 30_lien_parties/

> │                  ├── 📄 index.html

> │                └── 📂 40_docket_snapshots/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 40_service_and_notice/

> │                └── 📂 10_sheriff_returns/

> │                  ├── 📄 index.html

> │                └── 📂 20_mailings/

> │                  ├── 📄 index.html

> │                └── 📂 30_affidavits_of_service/

> │                  └── 📂 10_jurisdiction_service_tr_4_1_b/

> │                    ├── 📄 index.html

> │                  └── 📂 20_service_process/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 40_defects_and_contradictions/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 50_default_and_judgment/

> │                └── 📂 10_default_motion/

> │                  ├── 📄 index.html

> │                └── 📂 20_default_order/

> │                  ├── 📄 index.html

> │                └── 📂 30_judgment_and_decree/

> │                  ├── 📄 index.html

> │                └── 📂 40_accounting_inputs/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 60_sale_and_title/

> │                └── 📂 10_sheriff_sale/

> │                  ├── 📄 index.html

> │                └── 📂 20_deed/

> │                  ├── 📄 index.html

> │                └── 📂 30_recording_gaps/

> │                  ├── 📄 index.html

> │                └── 📂 40_possession_claims/

> │                  └── 📂 10_sale_and_possession/

> │                    ├── 📄 index.html

> │                  └── 📂 30_void_vs_voidable/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 70_writ_and_execution/

> │                └── 📂 10_writ_petition/

> │                  ├── 📄 index.html

> │                └── 📂 20_writ_order/

> │                  ├── 📄 index.html

> │                └── 📂 30_execution_events/

> │                  ├── 📄 index.html

> │                └── 📂 40_notice_failures/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 80_post_removal_conduct/

> │                └── 📂 10_property_interference/

> │                  ├── 📄 index.html

> │                └── 📂 20_access_denial/

> │                  ├── 📄 index.html

> │                └── 📂 30_spoliation_risk/

> │                  ├── 📄 index.html

> │                └── 📂 40_third_party_actions/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 90_damages_and_fallout/

> │                └── 📂 10_property_possession_harms/

> │                  ├── 📄 index.html

> │                └── 📂 20_economic_harm/

> │                  ├── 📄 index.html

> │                └── 📂 30_financial/

> │                  ├── 📄 index.html

> │                └── 📂 40_health_and_safety/

> │                  ├── 📄 index.html

> │                └── 📂 50_non_economic_harm/

> │                  └── 📂 cold_exposure/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 60_professional_harm/

> │                  ├── 📄 index.html

> │                └── 📂 70_remedies_scenarios/

> │                  ├── 📄 index.html

> │                └── 📂 80_payout_strategy/

> │                  ├── 📄 index.html

> │                └── 📂 90_third_party_harm/

> │                  ├── 📄 index.html

> │                └── 📂 Weather_Reports/

> │                  ├── 📄 index.html

> │                └── 📂 economic/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │                └── 📂 non-economic/

> │                  └── 📂 cold-exposure/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 personal_narrative/

> │                  └── 📂 10_Public_Narrative/

> │                    ├── 📄 index.html

> │                  └── 📂 20_Exposure_and_Harm/

> │                    └── 📂 Weather_Reports/

> │                      ├── 📄 index.html

> │                    ├── 📄 index.html

> │                  └── 📂 30_Internal_Analysis/

> │                    └── 📂 Payout_Strategy/

> │                      ├── 📄 index.html

> │                    └── 📂 Premonitions/

> │                      ├── 📄 index.html

> │                    ├── 📄 index.html

> │                  └── 📂 40_Donations_and_Support/

> │                    ├── 📄 index.html

> │                  └── 📂 50_Timeline/

> │                    ├── 📄 index.html

> │                  └── 📂 Premonitions/

> │                    ├── 📄 index.html

> │                └── 📂 settlement/

> │                  ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 E_OUTPUTS/

> │              └── 📂 10_binders/

> │                └── 📂 master_case_bible/

> │                  └── 📂 _build/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │              └── 📂 _build_artifacts/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │              └── 📂 vis/

> │                ├── 📄 index.html

> │            └── 📂 _ADMIN/

> │              └── 📂 10_index/

> │                ├── 📄 index.html

> │              └── 📂 20_case_logs/

> │                ├── 📄 index.html

> │              └── 📂 30_financial/

> │                ├── 📄 index.html

> │              └── 📂 40_overviews/

> │                └── 📂 10_maps/

> │                  ├── 📄 index.html

> │                └── 📂 20_deep_dives/

> │                  ├── 📄 index.html

> │                └── 📂 40_debates/

> │                  ├── 📄 index.html

> │                └── 📂 50_explainers/

> │                  ├── 📄 index.html

> │                └── 📂 60_infographics/

> │                  ├── 📄 index.html

> │                └── 📂 70_reports/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 50_protocols/

> │                ├── 📄 index.html

> │              └── 📂 70_templates/

> │                └── 📂 10_motions/

> │                  ├── 📄 index.html

> │                └── 📂 20_declarations/

> │                  ├── 📄 index.html

> │                └── 📂 30_exhibits/

> │                  ├── 📄 index.html

> │                └── 📂 40_orders/

> │                  ├── 📄 index.html

> │                └── 📂 50_internal/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 80_integrity_tooling/

> │                ├── 📄 index.html

> │              └── 📂 90_pack_blueprints/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │      ├── 📄 example.md

> │      ├── 📄 index.md

> │      └── 📂 public/

> │        └── 📂 vis-assets/

> │          └── 📂 A_TIMELINE/

> │            └── 📂 2023/

> │              ├── 📄 NT_index.md

> │            └── 📂 2024/

> │              ├── 📄 NT_index.md

> │            └── 📂 2025/

> │              ├── 📄 NT_index.md

> │              └── 📂 events/

> │                ├── 📄 MO_2025-05-13_Motion_for_Default_Judgment 1.md

> │                ├── 📄 MO_2025-05-13_Motion_for_Default_Judgment.md

> │                ├── 📄 MO_2025-05-23_Amended_Motion_Default_Judgment 1.md

> │                ├── 📄 MO_2025-05-23_Amended_Motion_Default_Judgment.md

> │                ├── 📄 MO_2025-12-10_Motions_Filed 1.md

> │                ├── 📄 MO_2025-12-10_Motions_Filed.md

> │                ├── 📄 MO_2025-12-12_Supplemental_Emergency_Motion 1.md

> │                ├── 📄 MO_2025-12-12_Supplemental_Emergency_Motion.md

> │                ├── 📄 NT_2025-01-16_Case_Filed 1.md

> │                ├── 📄 NT_2025-01-16_Case_Filed.md

> │                ├── 📄 NT_2025-03-05_Service_Attempt_1 1.md

> │                ├── 📄 NT_2025-03-05_Service_Attempt_1.md

> │                ├── 📄 NT_2025-04-15_Service_Attempt_2 1.md

> │                ├── 📄 NT_2025-04-15_Service_Attempt_2.md

> │                ├── 📄 NT_2025-08-15_Sheriff_Sale 1.md

> │                ├── 📄 NT_2025-08-15_Sheriff_Sale.md

> │                ├── 📄 NT_2025-11-06_Writ_of_Assistance_Issued 1.md

> │                ├── 📄 NT_2025-11-06_Writ_of_Assistance_Issued.md

> │                ├── 📄 NT_2025-12-09_Writ_Executed_Forced_Removal.md

> │                ├── 📄 NT_2025-12-09_Writ_Executed_Removal.md

> │                ├── 📄 NT_2025-12-16_Post_Removal_Access_Denial.md

> │                ├── 📄 NT_2025-12-21_Case_Summary.md

> │                ├── 📄 OR_2025-05-21_Order_Denying_Default_Judgment 1.md

> │                ├── 📄 OR_2025-05-21_Order_Denying_Default_Judgment.md

> │                ├── 📄 OR_2025-05-28_Default_Judgment_Entered 1.md

> │                ├── 📄 OR_2025-05-28_Default_Judgment_Entered.md

> │                ├── 📄 OR_2025-12-11_Court_Orders_and_Hearing_Scheduled 1.md

> │                ├── 📄 OR_2025-12-11_Court_Orders_and_Hearing_Scheduled.md

> │                ├── 📄 PL_2025-05-30_Praecipe_Sheriff_Sale 1.md

> │                ├── 📄 PL_2025-05-30_Praecipe_Sheriff_Sale.md

> │                ├── 📄 PL_2025-07-09_Sheriff_Sale_Notice_Posted 1.md

> │                ├── 📄 PL_2025-07-09_Sheriff_Sale_Notice_Posted.md

> │                ├── 📄 PL_2025-10-29_Petition_for_Writ_of_Assistance 1.md

> │                ├── 📄 PL_2025-10-29_Petition_for_Writ_of_Assistance.md

> │            └── 📂 2026/

> │              ├── 📄 NT_index.md

> │            ├── 📄 _A_TIMELINE.md

> │          └── 📂 B_EVIDENCE/

> │            └── 📂 10_evidence_admin/

> │              ├── 📄 00_evidence_admin.md

> │              ├── 📄 EXH_Raw_Exhibit_Map.md

> │              ├── 📄 Evidence_Log.md

> │              ├── 📄 master_evidence_index.md

> │            └── 📂 20_court_record/

> │              ├── 📄 10_court_record.md

> │              └── 📂 10_docket_files/

> │                ├── 📄 022_Plaintif_bid_2025_07_17_10_14_40.pdf.pdf

> │                ├── 📄 024_Service Returned Served.pdf

> │                ├── 📄 026_2025_10_29_13_47_03.pdf.pdf

> │                ├── 📄 029_Emergency_Supplemental_Declara.pdf

> │                ├── 📄 035_01092026_005.pdf.pdf

> │                ├── 📄 EXH_026_Exhibit_List_A-G.pdf

> │                ├── 📄 EXH__026_Exhibit_List_A-G.pdf

> │                ├── 📄 MO_013_Motion_for_Default_Judgment.pdf

> │                ├── 📄 MO_016_Order_Denying_Motion_for_Default_Judgment.pdf

> │                ├── 📄 MO_019_Amended_Motion_Default_Judgment_1.pdf

> │                ├── 📄 MO_020_Amended_Motion_Default_Judgment_2.pdf

> │                ├── 📄 MO_025_Motion_Vacate_Stay_Writ.pdf

> │                ├── 📄 MO_027_Supplemental_Motion_Access.pdf

> │                ├── 📄 MO__013_Motion_for_Default_Judgment.pdf

> │                ├── 📄 MO__019_Amended_Motion_Default_Judgmen.pdf

> │                ├── 📄 MO__020_Amended_Motion_Default_Judgmen.pdf

> │                ├── 📄 MO__025_Motion_Vacate_Stay_Writ.pdf

> │                ├── 📄 MO__027_Supplemental_Motion_Access.pdf

> │                ├── 📄 OR_023_Decree_Foreclosure_Returned.pdf

> │                ├── 📄 OR_031_Proposed_Order_Vacate.pdf

> │                ├── 📄 OR_032_Proposed_Order_Stay.pdf

> │                ├── 📄 OR__017_Order_Denying_Default_Judgment.pdf

> │                ├── 📄 OR__023_Decree_Foreclosure_Returned.pdf

> │                ├── 📄 OR__031_Proposed_Order_Vacate.pdf

> │                ├── 📄 OR__032_Proposed_Order_Stay.pdf

> │                ├── 📄 PL_001_Complaint.pdf

> │                ├── 📄 PL_002_Appearance.pdf

> │                ├── 📄 PL_003_Request_for_Admissions.pdf

> │                ├── 📄 PL_004_Notice_to_Homeowners.pdf

> │                ├── 📄 PL_005_Appearance_2.pdf

> │                ├── 📄 PL_006_Summons_1.pdf

> │                ├── 📄 PL_007_Summons_2.pdf

> │                ├── 📄 PL_008_Summons_3.pdf

> │                ├── 📄 PL_009_Summons_4.pdf

> │                ├── 📄 PL_010_Summons_5.pdf

> │                ├── 📄 PL_011_Service_Returned_03-05-2025.pdf

> │                ├── 📄 PL_012_Service_Returned_04-15-2025.pdf

> │                ├── 📄 PL_014_Affidavit.pdf

> │                ├── 📄 PL_015_Affidavit_Attorney_Fees.pdf

> │                ├── 📄 PL_017_OMITTED NOTICE OF SERVICE TO DEFENDANT.pdf

> │                ├── 📄 PL_018_Omitted_Notice_of_Service.pdf

> │                ├── 📄 PL_021_Praecipe_Sheriff_Sale_1.pdf

> │                ├── 📄 PL_022_Praecipe_Sheriff_Sale_2.pdf

> │                ├── 📄 PL_024_Petition_Writ_of_Assistance.pdf

> │                ├── 📄 PL_028_Report_Court_Defendant_Request.pdf

> │                ├── 📄 PL_029_Emergency_Supplemental_Declaration.pdf

> │                ├── 📄 PL_030_Report_Sheriff_Sale_No_Excess.pdf

> │                ├── 📄 PL_033_ADA_Disability_Affidavit.pdf

> │                ├── 📄 PL_2026-01-09_Appearance_Plaintiff.pdf

> │                ├── 📄 PL__001_Complaint.pdf

> │                ├── 📄 PL__002_Appearance.pdf

> │                ├── 📄 PL__003_Request_for_Admissions.pdf

> │                ├── 📄 PL__004_Notice_to_Homeowners.pdf

> │                ├── 📄 PL__005_Appearance_2.pdf

> │                ├── 📄 PL__006_Summons_1.pdf

> │                ├── 📄 PL__007_Summons_2.pdf

> │                ├── 📄 PL__008_Summons_3.pdf

> │                ├── 📄 PL__009_Summons_4.pdf

> │                ├── 📄 PL__010_Summons_5.pdf

> │                ├── 📄 PL__011_Service_Returned_03-05-2025.pdf

> │                ├── 📄 PL__012_Service_Returned_04-15-2025.pdf

> │                ├── 📄 PL__014_Affidavit.pdf

> │                ├── 📄 PL__015_Affidavit_Attorney_Fees.pdf

> │                ├── 📄 PL__016_Affidavit_Additional.pdf

> │                ├── 📄 PL__018_Omitted_Notice_of_Service.pdf

> │                ├── 📄 PL__021_Praecipe_Sheriff_Sale_1.pdf

> │                ├── 📄 PL__022_Praecipe_Sheriff_Sale_2.pdf

> │                ├── 📄 PL__024_Petition_Writ_of_Assistance.pdf

> │                ├── 📄 PL__028_Report_Court_Defendant_Request.pdf

> │                ├── 📄 PL__030_Report_Sheriff_Sale_No_Excess.pdf

> │                ├── 📄 PL__033_ADA_Disability_Affidavit.pdf

> │            └── 📂 30_primary/

> │              ├── 📄 10_primary.md

> │              ├── 📄 20_primary.md

> │              └── 📂 aes/

> │                ├── 📄 2025-06-08_aes_ada_request_financial_hardship_.pdf

> │                ├── 📄 PL_2025-06-08_aes_ada_notice.pdf

> │                ├── 📄 PL_2025-12-16_AES_Emergency_Notice.md

> │                ├── 📄 _README.md

> │              └── 📂 fcfcu/

> │                ├── 📄 2023-09-20_FCFCU_Hardship_and_Healt.md

> │                ├── 📄 2024-03-20_fcfcu_certified_response_tax_record.pdf

> │                ├── 📄 2024-12-09_outgoing_email_bank_access_request.pdf

> │                ├── 📄 2024-12-11_outgoing_email_bank_access_request.pdf

> │                ├── 📄 20241204_FCFCU_Statement (1).pdf

> │                ├── 📄 20241204_FCFCU_Statement (2).pdf

> │                ├── 📄 20241204_fcfcu_statement-(1).pdf

> │                ├── 📄 20241204_fcfcu_statement-(2).pdf

> │                ├── 📄 20241204_fcfcu_statement.pdf

> │                ├── 📄 2025-12-20_exh-30_fcfcu_740eacdc_2025-12-20_ex.jpg

> │                ├── 📄 2025-12-20_exh-30_fcfcu_ac6eb2ea_2025-12-20_ex.jpg

> │                ├── 📄 21june-24-4817shadow_appraisal.pdf

> │                ├── 📄 PL_2023-09-20_FCFCU_Hardship_and_Health_Notice_Let.md

> │                ├── 📄 PL_2023-09-20_fcfcu_hardship_and_health_notice_le.pdf

> │                ├── 📄 PL_2023-09-20_notice_disabilities_hardship.pdf

> │                ├── 📄 PL_2024-20-03_response_to_tax_notice.pdf

> │                ├── 📄 PL_fcfcu_v_cr-v_report_to_court.pdf

> │                ├── 📄 PL_report_to_court_on_defendants_request.pdf

> │                ├── 📄 _README.md

> │            └── 📂 40_supporting/

> │              ├── 📄 20_supporting.md

> │              ├── 📄 30_supporting.md

> │              └── 📂 docs/

> │                └── 📂 affidavits/

> │                  ├── 📄 PL_affidavits.md

> │                └── 📂 declarations/

> │                  ├── 📄 PL_declarations.md

> │                └── 📂 receipts/

> │                  ├── 📄 NT_2025-12-20_exh-20_receipts_0860d3df_2025-12-20.jpg

> │                  ├── 📄 NT_Odyssey_Envelope_Receipt.pdf

> │                └── 📂 records/

> │                  ├── 📄 Foreclosure and Housing Litigation Case Record.csv

> │                  ├── 📄 Inventory of Civil and Fair Housing Rights Vio.csv

> │              └── 📂 multi-media/

> │                ├── 📄 2025-12-20_exh-10_photos_video_00241326_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_012aa06e_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_01b3e905_2025-1.png

> │                ├── 📄 2025-12-20_exh-10_photos_video_10f4975d_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_1a80b987_2025-1.mp4

> │                ├── 📄 2025-12-20_exh-10_photos_video_1beefb11_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_1f3f8a81_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_25fb1992_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_2f0952db_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_49c74ec6_2025-.heic

> │                ├── 📄 2025-12-20_exh-10_photos_video_4e01fa01_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_5be451ba_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_5d95cae5_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_61129253_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_63fb7b02_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_71c9e6a7_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_78ba1ccc_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_7a544ef7_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_8350e7be_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_8a163413_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_8d885a5c_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_942cfd7f_2025-1.png

> │                ├── 📄 2025-12-20_exh-10_photos_video_9b611100_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_9fb3a08a_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_9ff5022d_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_a8832e17_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_ca02d006_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_db9b10b5_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_e4cb3622_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_ebaaa38d_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_ed6dc885_2025-1.mp4

> │                ├── 📄 2025-12-20_exh-10_photos_video_f510498b_2025-.heic

> │                ├── 📄 2025-12-20_exh-10_photos_video_f60d8098_2025-1.png

> │                ├── 📄 2025-12-20_exh-10_photos_video_f98b089a_2025-1.png

> │                ├── 📄 2025-12-20_exh-10_photos_video_fa1703bf_2025-1.jpg

> │                ├── 📄 2025-12-20_exh-10_photos_video_fdd8d4ef_2025-1.jpg

> │              └── 📂 property/

> │                └── 📂 10_mortgage_history/

> │                  └── 📂 10_payments/

> │                    ├── 📄 2025-12-20_EXH-20_payments_c5131deb_2025-12-20.png

> │                    ├── 📄 2025-12-20_exh-20_payments_c5131deb_2025-12-20 (2).png

> │                    ├── 📄 20_payments.md

> │                └── 📂 20_parcel/

> │                  ├── 📄 Parcel_6016506_PRC.pdf

> │                  ├── 📄 Parcel_6016506_ParcelDetailHistory.pdf

> │                  ├── 📄 parcel_6016506_parceldetailhistory (2).pdf

> │                  ├── 📄 parcel_6016506_prc (2).pdf

> │            └── 📂 50_quarantine_candidates/

> │              ├── 📄 90_quarantine_candidates.md

> │            ├── 📄 _B_EVIDENCE.md

> │          └── 📂 C_VIS/

> │            └── 📂 10_violations/

> │              ├── 📄 EXH_Exhibit X — Inventory of Jurisdictional, Execut.md

> │              ├── 📄 NT_V-005_failure-to-correct-inaccurate-furnishings.md

> │              ├── 📄 NT_V-006_dual-tradeline-double-counting.md

> │              ├── 📄 NT_V-008_credit-defamation-false-publication.md

> │              ├── 📄 NT_V-009_fdCPA-misrepresentation-of-debt-status.md

> │              ├── 📄 NT_V-010_failure-to-mark-account-foreclosure-closed.md

> │              ├── 📄 NT_V-011_experian-reinvestigation-failure.md

> │              ├── 📄 NT_V-012_equifax-reinvestigation-failure.md

> │              ├── 📄 NT_V-013_transunion-reinvestigation-failure.md

> │              ├── 📄 NT_V-020_post-0815-aes-electric-charges-billed.md

> │              ├── 📄 NT_V-021_post-0815-citizens-energy-charges-billed.md

> │              ├── 📄 NT_V-022_post-0815-hoa-assessments-billed.md

> │              ├── 📄 NT_V-023_city-grass-cut-ticket-assessed-after-loss-of-access.md

> │              ├── 📄 NT_V-024_municipal-code-enforcement-after-possession-transfer.md

> │              ├── 📄 NT_V-025_cost-shift-fcfcu-refused-winterize.md

> │              ├── 📄 NT_V-026_credit-harm-compounded-utility-municipal.md

> │              ├── 📄 NT_V-031_sheriff-return-inaccuracies.md

> │              ├── 📄 NT_V-033_removal-6-7-days-after-deed-recorded.md

> │              ├── 📄 NT_V-035_court-relied-on-service-sufficiency.md

> │              ├── 📄 NT_V-036_surplus-funds-declared-resolved.md

> │              ├── 📄 NT_V-037_interest-fees-arbitrarily-inflated.md

> │              ├── 📄 NT_V-038_fcfcu-testimony-winterize-then-leave.md

> │              ├── 📄 NT_V-070_global-demand-letter.md

> │              ├── 📄 NT_V-071_litigation-hold-preservation-letter.md

> │              ├── 📄 NT_V-072_equitable-relief-tradeline-deletion.md

> │              ├── 📄 NT_V-073_damages-credit-score-suppression.md

> │              ├── 📄 NT_V-074_damages-out-of-pocket-costs.md

> │              ├── 📄 NT_V-075_public-accountability-hold.md

> │              ├── 📄 NT_V-076_fha-reasonable-accommodation-failure.md

> │              ├── 📄 NT_V-077_ada-title-iii-entertainment-access-failure.md

> │              ├── 📄 NT_V-078_ada-effective-communication-failure.md

> │              ├── 📄 NT_V-080_conversion-negligence-post-removal-damage.md

> │              ├── 📄 NT_V-081_evidence-spoliation-unplugged-cameras.md

> │              ├── 📄 NT_V-082_fraud-on-the-court-material-misrepresentation.md

> │              ├── 📄 NT_V-083_discriminatory-maintenance-redlining.md

> │              ├── 📄 NT_V-084_predatory-land-contract-reverse-redlining.md

> │              ├── 📄 OR_V-001_fcfcu-continues-reporting-first-mortgage-post-judgment-sale.md

> │              ├── 📄 OR_V-002_fcfcu-continues-reporting-second-mortgage-post-judgment-sale.md

> │              ├── 📄 OR_V-003_monthly-delinquencies-after-foreclosure-judgment.md

> │              ├── 📄 OR_V-004_past-due-amount-schedule-after-judgment.md

> │              ├── 📄 OR_V-079_void-judgment-procedural-error.md

> │              ├── 📄 PL_V-007_inconsistent-reporting-vs-court-position.md

> │              ├── 📄 PL_V-030_service-completed-no-notice-before-writ.md

> │              ├── 📄 PL_V-032_no-ada-compliant-notice.md

> │              ├── 📄 PL_V-034_attorney-appeared-without-formal-appearance.md

> │              ├── 📄 PL_V-050_cfpb-complaint-track.md

> │              ├── 📄 PL_V-051_indiana-ag-complaint-track.md

> │              ├── 📄 PL_V-052_icrc-complaint-track.md

> │              ├── 📄 PL_V-053_doj-civil-rights-complaint-track.md

> │              ├── 📄 PL_V-060_bbb-complaint-reputational-pressure.md

> │            └── 📂 20_theories/

> │              ├── 📄 NT_BACKUP_ARGUMENTS.md

> │              ├── 📄 NT_IF_JUDGE_PUSHBACK.md

> │            └── 📂 30_legal_research/

> │              ├── 📄 NT_CASE_LAW_RESEARCH.md

> │              ├── 📄 NT_JURISDICTION_THEORY.md

> │              ├── 📄 NT_LEGAL MEMORANDUM.md

> │              ├── 📄 NT_VOID_VS_VOIDABLE_ANALYSIS.md

> │            └── 📂 40_analysis/

> │              ├── 📄 NT_INTERNAL VALUATION MEMO.md

> │              ├── 📄 NT_Procedural_failure_map_one_pager.md

> │              ├── 📄 NT_Violation_Remedy_Inventory.md

> │            └── 📂 50_strategies/

> │              ├── 📄 NT_00_basis.md

> │              ├── 📄 NT_10_ada_strategy.md

> │              ├── 📄 NT_ADA_TITLE_II_ANALYSIS.md

> │              ├── 📄 NT_BUT_FOR_ANALYSIS.md

> │              ├── 📄 NT_Master_Strategy_Canvas.canvas

> │              ├── 📄 NT_PROCEDURAL_FAILURE_MAP.md

> │              ├── 📄 NT_REASONABLE_ACCOMMODATIONS.md

> │              ├── 📄 NT_REVERSAL_PATHS.md

> │              ├── 📄 NT_STATUS_TRACKER.md

> │              ├── 📄 NT_STAY_PATHS.md

> │              ├── 📄 NT_integrate_disability_separate_appe.m4a

> │              ├── 📄 OR_void_judgment_eviction_crisis.pdf

> │              ├── 📄 PL_DOJ_COMPLAINT.md

> │              ├── 📄 PL_ICRC_COMPLAINT.md

> │              ├── 📄 PL_Proposal for Strategic Reports in the Matter of.md

> │              ├── 📄 Strategic_Plan.canvas

> │            └── 📂 60_data_inventories/

> │              ├── 📄 NT_Violation_Index.md

> │              ├── 📄 NT_foreclosure-and-housing-litigation-case-record.csv

> │              ├── 📄 NT_inventory-of-civil-and-fair-housing-rights-vio.csv

> │            ├── 📄 NT_01_MASTER_INDEX.md

> │            ├── 📄 _C_VIS.md

> │            ├── 📄 vis.yaml

> │          ├── 📄 Case_Data.base

> │          └── 📂 D_PHASES/

> │            └── 📂 100_post_judgment_and_federal/

> │              └── 📂 10_motions/

> │                └── 📂 10_claims_motions/

> │                  ├── 📄 40_claims_motions.md

> │                  ├── 📄 MO_40_claims_motions.md

> │                  └── 📂 Supplemental/

> │                    └── 📂 01_drafts/

> │                      ├── 📄 MO__Supplemental_Emergency_Motion.pdf

> │                    └── 📂 02_exhibits/

> │                      ├── 📄 EXH_02_exhibits.md

> │                      ├── 📄 EXH__20_exhibits_combined_source

> │                      ├── 📄 EXH__Exhibit_H_Declaration.pdf

> │                    └── 📂 04_filed_receipts/

> │                      ├── 📄 NT__Odyssey_Envelope_Receipt.pdf

> │                  └── 📂 filings/

> │                    └── 📂 10_2025-12-10_motion_vacate/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 MO_Emergency Motions.docx

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 EXH_02_exhibits.md

> │                        ├── 📄 EXH_05_Exhibit_List.pdf

> │                        ├── 📄 EXH_06_Exhibits_Combined.pdf

> │                        ├── 📄 MO_01_motion_vacate.pdf

> │                        ├── 📄 MO_02_emergency_motion_quash_stay.pdf

> │                        ├── 📄 NT_combinepdf.pdf

> │                        ├── 📄 OR_03_order_vacate_proposed.pdf

> │                        ├── 📄 OR_04_order_stay_writ_proposed.pdf

> │                      └── 📂 03_proposed_order/

> │                        ├── 📄 OR_03_proposed_order.md

> │                        ├── 📄 OR_Proposed_Order_Vacate.docx

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 NT_Odyssey_Envelope_Receipt.pdf

> │                      ├── 📄 MO_10_2025-12-10_motion_vacate.md

> │                    └── 📂 20_2025-12-11_Supplemental_Emergency_Motion_Access/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 MO_Supplemental_Emergency_Motion.pdf

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 EXH_02_exhibits.md

> │                        ├── 📄 EXH_20_exhibits_combined_source

> │                        ├── 📄 EXH_Exhibit_H_Declaration.pdf

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 NT_Odyssey_Envelope_Receipt.pdf

> │                      ├── 📄 MO_20_2025-12-11_Supplemental_Emergency_Motion_Access.md

> │                    └── 📂 30_draft_motions/

> │                      ├── 📄 10_draft_motions.md

> │                      ├── 📄 20_draft_motions.md

> │                      ├── 📄 MO_10_draft_motions.md

> │                      ├── 📄 MO_DRAFT_MOTION_VACATE.md

> │                      ├── 📄 MO__Motions.md

> │                      ├── 📄 MO__motion_emergency_stay_of_writ.md

> │                      ├── 📄 MO__motion_emergency_supplemental_motio.md

> │                      ├── 📄 MO__motion_to_vacate_void_judgment.md

> │                      ├── 📄 MO_motion_emergency_stay_of_writ.md

> │                      ├── 📄 MO_motion_emergency_supplemental_motion_ongoing_ha.md

> │                      ├── 📄 MO_motion_to_vacate_void_judgment.md

> │                      ├── 📄 MO_wc2.00.010__motion_emergency_stay_of_writ.docx

> │                      ├── 📄 MO_wc2.00.010__motion_emergency_supplemental_mot.docx

> │                      ├── 📄 MO_wc2.00.010__motion_to_vacate_void_judgement.docx

> │                      ├── 📄 NT_DRAFT_EMERGENCY_STAY.md

> │                      ├── 📄 NT_DRAFT_SUPPLEMENTAL.md

> │                      ├── 📄 NT_EMERGENCY_FILING_PACKET.md

> │                      ├── 📄 _README.md

> │                      └── 📂 motions/

> │                        ├── 📄 MO_01B_Motion_To_Vacate_Void_Judgment.pdf

> │                        ├── 📄 MO_C2.01.002_motion_vacate.pdf

> │                        ├── 📄 MO_C2.02.002_Emergency_Motion_Stay_OR_Quash.pdf

> │                        ├── 📄 MO_C2.03.002_Supplemental_Emergency_Motion.pdf

> │                        ├── 📄 MO_motions.md

> │                  └── 📂 motion_vacate/

> │                    └── 📂 01_drafts/

> │                      ├── 📄 MO__Emergency Motions.docx

> │                    └── 📂 02_exhibits/

> │                      ├── 📄 EXH_02_exhibits.md

> │                      ├── 📄 EXH__05_Exhibit_List.pdf

> │                      ├── 📄 EXH__06_Exhibits_Combined.pdf

> │                      ├── 📄 MO__01_motion_vacate.pdf

> │                      ├── 📄 MO__02_emergency_motion_quash_stay.pdf

> │                      ├── 📄 NT__combinepdf.pdf

> │                      ├── 📄 OR__03_order_vacate_proposed.pdf

> │                      ├── 📄 OR__04_order_stay_writ_proposed.pdf

> │                    └── 📂 03_proposed_order/

> │                      ├── 📄 OR_03_proposed_order.md

> │                      ├── 📄 OR__Proposed_Order_Vacate.docx

> │                    └── 📂 04_filed_receipts/

> │                      ├── 📄 NT__Odyssey_Envelope_Receipt.pdf

> │                    ├── 📄 MO_motion_vacate.md

> │                    ├── 📄 NT.gitkeep

> │                ├── 📄 MO_10_motions.md

> │                ├── 📄 NT_index.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_orders/

> │                └── 📂 10_proposed_orders/

> │                  ├── 📄 20_proposed_orders.md

> │                  ├── 📄 MO__proposed_order_motion_to_vacate.md

> │                  ├── 📄 MO_proposed_order_motion_to_vacate.md

> │                  ├── 📄 NT__index.md

> │                  ├── 📄 OR_20_proposed_orders.md

> │                  ├── 📄 OR_DRAFT_ORDER_STAY.md

> │                  ├── 📄 OR_DRAFT_ORDER_VACATE.md

> │                  ├── 📄 OR__Proposed_Orders.md

> │                  ├── 📄 OR__proposed_order_emergency_stay.md

> │                  ├── 📄 OR_proposed_order_emergency_stay.md

> │                  ├── 📄 _README.md

> │                ├── 📄 NT_index.md

> │                ├── 📄 OR_20_orders.md

> │                ├── 📄 _placeholder.md

> │                └── 📂 orders/

> │                  ├── 📄 OR_C2.04.001_order_vacate_proposed.pdf

> │                  ├── 📄 OR_C2.04.002_order_stay_writ_proposed.pdf

> │                  ├── 📄 OR_orders.md

> │              └── 📂 30_regulatory_complaints/

> │                ├── 📄 PL_30_regulatory_complaints.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_federal_preservation/

> │                ├── 📄 _placeholder.md

> │              ├── 📄 OR_90_post_judgment_and_federal.md

> │              ├── 📄 _README.md

> │            └── 📂 10_inbox_working/

> │              ├── 📄 NT_00_inbox_working.md

> │              ├── 📄 NT_index.md

> │              └── 📂 _staging/

> │                └── 📂 _dupes_hold/

> │                  ├── 📄 MO__motion_emergency_stay_of_writ (2).docx

> │                  ├── 📄 MO__motion_emergency_supplemental_mot (2).docx

> │                  ├── 📄 MO__motion_to_vacate_void_judgement (2).docx

> │                  ├── 📄 NT_2025-12-15_they_threw_us_into_the_cold (2).md

> │                  ├── 📄 NT_Donations_Context (2).md

> │                  ├── 📄 NT_Long_Term_Payout_Strategy (2).md

> │                  ├── 📄 NT_Master_Timeline (2).md

> │                  ├── 📄 NT_Premonitions_I_Knew_Before_I_Knew (2).md

> │                  ├── 📄 NT_Public_Statement (2).md

> │                  ├── 📄 NT_Session_Summary_2025-12-15_i_knew_before_i_knew (2).md

> │                  ├── 📄 NT_index.md

> │                  ├── 📄 OR_c2.04.001_order_vacate_proposed (2).pdf

> │                  ├── 📄 OR_c2.04.002_order_stay_writ_proposed (2).pdf

> │                  ├── 📄 PL_Cold_Risk_Report (2).md

> │                └── 📂 _html_hold/

> │                  ├── 📄 NT_index.md

> │              └── 📂 evidence_staging/

> │                └── 📂 exhibit_candidates/

> │                  └── 📂 10_exposure_and_harm/

> │                    ├── 📄 02_exposure_and_harm.md

> │                    ├── 📄 NT_02_exposure_and_harm.md

> │                    ├── 📄 PL_wi8.02.050__cold_risk_report.html

> │                    └── 📂 weather_reports/

> │                      ├── 📄 PL_weather_reports.md

> │                  ├── 📄 EXH_exhibit_candidates.md

> │                └── 📂 potential_exhibits/

> │                  ├── 📄 EXH_potential_exhibits.md

> │            └── 📂 20_pre_foreclosure/

> │              └── 📂 10_account_history/

> │                ├── 📄 NT_index.md

> │                ├── 📄 NT_one_pager_overview.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_hardship_and_ada/

> │                ├── 📄 _placeholder.md

> │              └── 📂 30_communications/

> │                ├── 📄 NT_index.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_payments_and_disputes/

> │                ├── 📄 _placeholder.md

> │              ├── 📄 NT_10_pre_foreclosure.md

> │              ├── 📄 _README.md

> │            └── 📂 30_foreclosure_filing/

> │              └── 📂 10_complaint/

> │                ├── 📄 PL_10_complaint.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_summons/

> │                ├── 📄 PL_20_summons.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 30_lien_parties/

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_docket_snapshots/

> │                ├── 📄 NT_01_Docket.md

> │                ├── 📄 NT__Case_Summary.md

> │                ├── 📄 NT_docket_index.md

> │                ├── 📄 _Case_Summary.md

> │                ├── 📄 _README.md

> │                ├── 📄 _docket.md

> │                ├── 📄 _placeholder.md

> │              ├── 📄 NT_20_foreclosure_filing.md

> │              ├── 📄 _README.md

> │            └── 📂 40_service_and_notice/

> │              └── 📂 10_sheriff_returns/

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_mailings/

> │                ├── 📄 _placeholder.md

> │              └── 📂 30_affidavits_of_service/

> │                └── 📂 10_jurisdiction_service_tr_4_1_b/

> │                  ├── 📄 20_jurisdiction_service_tr_4_1_b.md

> │                  ├── 📄 NT_20_jurisdiction_service_tr_4_1_b 1.md

> │                  ├── 📄 NT_20_jurisdiction_service_tr_4_1_b.md

> │                └── 📂 20_service_process/

> │                  ├── 📄 30_service_process.md

> │                ├── 📄 NT_03_Service_Process.md

> │                ├── 📄 NT_service_defects_analysis.md

> │                ├── 📄 PL_30_affidavits_of_service.md

> │                ├── 📄 PL_affidavits_service.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_defects_and_contradictions/

> │                ├── 📄 _placeholder.md

> │              ├── 📄 PL_30_service_and_notice.md

> │              ├── 📄 _README.md

> │            └── 📂 50_default_and_judgment/

> │              └── 📂 10_default_motion/

> │                ├── 📄 MO_10_default_motion.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_default_order/

> │                ├── 📄 OR_20_default_order.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 30_judgment_and_decree/

> │                ├── 📄 OR_30_judgment_and_decree.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_accounting_inputs/

> │                ├── 📄 _placeholder.md

> │              ├── 📄 OR_40_default_and_judgment.md

> │              ├── 📄 _README.md

> │            └── 📂 60_sale_and_title/

> │              └── 📂 10_sheriff_sale/

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_deed/

> │                ├── 📄 _placeholder.md

> │              └── 📂 30_recording_gaps/

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_possession_claims/

> │                └── 📂 10_sale_and_possession/

> │                  ├── 📄 30_sale_and_possession.md

> │                  ├── 📄 NT_30_sale_and_possession.md

> │                └── 📂 30_void_vs_voidable/

> │                  ├── 📄 20_void_vs_voidable.md

> │                  ├── 📄 NT_30_void_vs_voidable_tr_60b 1.md

> │                  ├── 📄 NT_30_void_vs_voidable_tr_60b.md

> │                ├── 📄 NT_05_Sale_and_Possesion.md

> │                ├── 📄 NT_possession_admissions.md

> │                ├── 📄 _placeholder.md

> │              ├── 📄 NT_50_sale_and_title.md

> │              ├── 📄 _README.md

> │            └── 📂 70_writ_and_execution/

> │              └── 📂 10_writ_petition/

> │                ├── 📄 PL_10_writ_petition.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_writ_order/

> │                ├── 📄 OR_20_writ_order.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 30_execution_events/

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_notice_failures/

> │                ├── 📄 PL_40_notice_failures.md

> │                ├── 📄 _placeholder.md

> │              ├── 📄 NT_60_writ_and_execution.md

> │              ├── 📄 _README.md

> │            └── 📂 80_post_removal_conduct/

> │              └── 📂 10_property_interference/

> │                ├── 📄 _placeholder.md

> │              └── 📂 20_access_denial/

> │                ├── 📄 _placeholder.md

> │              └── 📂 30_spoliation_risk/

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_third_party_actions/

> │                ├── 📄 _placeholder.md

> │              ├── 📄 NT_70_post_removal_conduct.md

> │              ├── 📄 _README.md

> │            └── 📂 90_damages_and_fallout/

> │              └── 📂 10_property_possession_harms/

> │                ├── 📄 03_property_possession_harms.md

> │                ├── 📄 NT_03_property_possession_harms.md

> │              └── 📂 20_economic_harm/

> │                ├── 📄 10_economic_harm.md

> │                ├── 📄 NT_10_economic_harm.md

> │                ├── 📄 NT_index.md

> │              └── 📂 30_financial/

> │                ├── 📄 20_financial.md

> │                ├── 📄 NT_10_financial.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 40_health_and_safety/

> │                ├── 📄 30_health_and_safety.md

> │                ├── 📄 NT_20_health_and_safety.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 50_non_economic_harm/

> │                ├── 📄 40_non_economic_harm.md

> │                ├── 📄 NT_20_non_economic_harm.md

> │                └── 📂 cold_exposure/

> │                  ├── 📄 NT_index.md

> │              └── 📂 60_professional_harm/

> │                ├── 📄 50_professional_harm.md

> │                ├── 📄 NT_30_professional_harm.md

> │                ├── 📄 _placeholder.md

> │              └── 📂 70_remedies_scenarios/

> │                ├── 📄 60_remedies_scenarios.md

> │                ├── 📄 NT_30_remedies_scenarios.md

> │                ├── 📄 NT_index.md

> │              └── 📂 80_payout_strategy/

> │                ├── 📄 70_payout_strategy.md

> │                ├── 📄 NT_40_Payout_Strategy.md

> │                ├── 📄 NT__Long_Term_Payout_Strategy.md

> │                ├── 📄 NT_index.md

> │                ├── 📄 _README.md

> │              └── 📂 90_third_party_harm/

> │                ├── 📄 80_third_party_harm.md

> │                ├── 📄 NT_40_third_party_harm.md

> │                ├── 📄 _placeholder.md

> │              ├── 📄 NT_06_damages_and_remedies.md

> │              ├── 📄 NT_80_damages_and_fallout.md

> │              ├── 📄 NT_index.md

> │              └── 📂 Weather_Reports/

> │                ├── 📄 PL_Weather_Reports.md

> │              ├── 📄 _README.md

> │              └── 📂 economic/

> │                ├── 📄 NT_ECONOMIC_HARM.md

> │              └── 📂 non-economic/

> │                ├── 📄 NT_NON_ECONOMIC_HARM.md

> │                └── 📂 cold-exposure/

> │                  ├── 📄 PL__Cold_Risk_Report.md

> │              └── 📂 personal_narrative/

> │                └── 📂 10_Public_Narrative/

> │                  ├── 📄 01_Public_Narrative.md

> │                  ├── 📄 NT_01_Public_Narrative.md

> │                  ├── 📄 NT_2025-12-15_they_threw_us_into_the_cold.md

> │                  ├── 📄 NT_Public_Statement.md

> │                  ├── 📄 _README.md

> │                └── 📂 20_Exposure_and_Harm/

> │                  ├── 📄 02_Exposure_and_Harm.md

> │                  ├── 📄 NT_02_Exposure_and_Harm.md

> │                  ├── 📄 PL_Cold_Risk_Report.md

> │                  └── 📂 Weather_Reports/

> │                    ├── 📄 PL_Weather_Reports.md

> │                  ├── 📄 _README.md

> │                └── 📂 30_Internal_Analysis/

> │                  ├── 📄 03_Internal_Analysis.md

> │                  ├── 📄 NT_03_Internal_Analysis.md

> │                  ├── 📄 NT_Session_Summary_2025-12-15_i_knew_before_i_knew.md

> │                  └── 📂 Payout_Strategy/

> │                    ├── 📄 NT_Long_Term_Payout_Strategy.md

> │                    ├── 📄 _README.md

> │                  └── 📂 Premonitions/

> │                    ├── 📄 NT_Premonitions_I_Knew_Before_I_Knew.md

> │                    ├── 📄 _README.md

> │                  ├── 📄 _README.md

> │                └── 📂 40_Donations_and_Support/

> │                  ├── 📄 04_Donations_and_Support.md

> │                  ├── 📄 NT_04_Donations_and_Support.md

> │                  ├── 📄 NT_Donations_Context.md

> │                  ├── 📄 _README.md

> │                └── 📂 50_Timeline/

> │                  ├── 📄 05_Timeline.md

> │                  ├── 📄 NT_05_Timeline.md

> │                  ├── 📄 NT_Master_Timeline.md

> │                  ├── 📄 _README.md

> │                └── 📂 Premonitions/

> │                  ├── 📄 NT__Premonitions_I_Knew_Before_I_Knew.md

> │                  ├── 📄 _README.md

> │              └── 📂 settlement/

> │                ├── 📄 NT_SETTLEMENT_SCENARIOS.md

> │            ├── 📄 MO_Promotion_Checklist.md

> │            ├── 📄 Strategic_Plan.canvas

> │            ├── 📄 _D_PHASES.md

> │          └── 📂 E_OUTPUTS/

> │            └── 📂 10_binders/

> │              └── 📂 master_case_bible/

> │                ├── 📄 NT_binder_manifest.md

> │                └── 📂 _build/

> │                  ├── 📄 NT_full_binder.md

> │                  ├── 📄 NT_full_binder_snapshot.md

> │                  ├── 📄 NT_master_case_bible.html

> │                  ├── 📄 NT_temp_merged.md

> │            ├── 📄 _E_OUTPUTS.md

> │            └── 📂 _build_artifacts/

> │              ├── 📄 MO_wc2.00.001_draft_motion_vacate.html

> │              ├── 📄 MO_wc2.00.010___motions.html

> │              ├── 📄 MO_wc2.00.010__motion_emergency_stay_of_writ.html

> │              ├── 📄 MO_wc2.00.010__motion_emergency_supplemental_mot.html

> │              ├── 📄 MO_wc2.00.010__motion_to_vacate_void_judgment.html

> │              ├── 📄 MO_wc2.01.010__proposed_order_motion_to_vacate.html

> │              ├── 📄 NT_2025-12-15_they_threw_us_into_the_cold.html

> │              ├── 📄 NT_Summary - MyCase.html

> │              ├── 📄 NT_WI8.01.050__index.html

> │              ├── 📄 NT_WI8.02.050__index.html

> │              ├── 📄 NT_WI8.99.010__index_MOVED.html

> │              ├── 📄 NT_WZ9.00.050__index.html

> │              ├── 📄 NT_WZ9.00.050__index_MOVED.html

> │              ├── 📄 NT__index (2).html

> │              ├── 📄 NT__index.html

> │              ├── 📄 NT__index_MOVED.html

> │              ├── 📄 NT_donations_context.html

> │              ├── 📄 NT_index (2).html

> │              ├── 📄 NT_index (2)_MOVED.html

> │              ├── 📄 NT_index-content.html

> │              ├── 📄 NT_index-content_MOVED.html

> │              ├── 📄 NT_index.html

> │              ├── 📄 NT_index_MOVED.html

> │              ├── 📄 NT_long_term_payout_strategy.html

> │              ├── 📄 NT_master_timeline.html

> │              ├── 📄 NT_premonitions_i_knew_before_i_knew.html

> │              ├── 📄 NT_public_statement.html

> │              ├── 📄 NT_session_summary_2025-12-15_i_knew_before_i_kn.html

> │              ├── 📄 NT_strategic_plan.html

> │              ├── 📄 NT_wc2.00.002_draft_emergency_stay.html

> │              ├── 📄 NT_wc2.00.003_draft_supplemental.html

> │              ├── 📄 NT_wc2.01.010__index-content.html

> │              ├── 📄 NT_wc2.01.010__index.html

> │              ├── 📄 NT_wg6.01.003_status_tracker.html

> │              ├── 📄 NT_wi8.01.010__2025-12-15_they_threw_us_into_the.html

> │              ├── 📄 NT_wi8.01.050__index-content.html

> │              ├── 📄 NT_wi8.99.010__index-content.html

> │              ├── 📄 NT_wi8.99.010__index.html

> │              ├── 📄 NT_wi8.99.010__long_term_payout_strategy.html

> │              ├── 📄 NT_wi8.99.010__premonitions_i_knew_before_i_knew.html

> │              ├── 📄 NT_wi8.99.010__session_summary_2025-12-15_i_knew.html

> │              ├── 📄 OR_wc2.01.001_draft_order_vacate.html

> │              ├── 📄 OR_wc2.01.002_draft_order_stay.html

> │              ├── 📄 OR_wc2.01.010__proposed_order_emergency_stay.html

> │              ├── 📄 OR_wc2.01.010__proposed_orders.html

> │              ├── 📄 PL_cold_risk_report.html

> │              ├── 📄 PL_wg6.01.001_doj_complaint.html

> │              ├── 📄 PL_wg6.01.002_icrc_complaint.html

> │              ├── 📄 _readme.html

> │              ├── 📄 _readme_MOVED.html

> │            └── 📂 vis/

> │              ├── 📄 latest.txt

> │          ├── 📄 NT_README.md

> │          └── 📂 _ADMIN/

> │            └── 📂 10_index/

> │              ├── 📄 NT_00_index.md

> │              ├── 📄 NT_Contacts.md

> │            └── 📂 20_case_logs/

> │              ├── 📄 NT_2025-12-09_Writ_Executed_Forced_Removal.md

> │              ├── 📄 NT_2025-12-15_Case_DNA_Strategy_Checkpoint.md

> │              ├── 📄 NT_2025-12-15_Strategic_Planning_Session.md

> │              ├── 📄 NT_2025-12-16_Post_Removal_Access_Denial.md

> │              ├── 📄 NT_2025-12-16_case_log_entry.md

> │              ├── 📄 NT_2025-12-16_case_summary.md

> │              ├── 📄 NT_2025-12-16_fcfcu_case_dna_strat.md

> │              ├── 📄 NT_2025-12-21_Case_Summary.md

> │              ├── 📄 NT_2026-01-16_Cleanup_Log.md

> │              ├── 📄 NT_20_case_logs.md

> │              ├── 📄 NT_INGEST_2025-12-16_case_log_entry.md

> │              ├── 📄 NT_Master_Case_Log.md

> │              ├── 📄 NT_content_manifest_hashes.json

> │              ├── 📄 NT_ingest_dedupe_manifest.json

> │              ├── 📄 PL_integrity_scan_report.json

> │            └── 📂 30_financial/

> │              ├── 📄 NT_02_financial.md

> │              ├── 📄 NT_Financial_Tracker.md

> │            └── 📂 40_overviews/

> │              └── 📂 10_maps/

> │                ├── 📄 NT_Procedural_failure_map_one_pager.md

> │              └── 📂 20_deep_dives/

> │                ├── 📄 NT_Integrate_Disability_Separate_Appeals_Get_Stay.m4a

> │                ├── 📄 NT_foreclosure_void_versus_damages_due_process.m4a

> │                ├── 📄 NT_forensic_audit_of_a_void_foreclosure.m4a

> │                ├── 📄 OR_foreclosure_void_judgment_institutional_failur.m4a

> │              └── 📂 40_debates/

> │                ├── 📄 NT_debate.m4a

> │              └── 📂 50_explainers/

> │                ├── 📄 NT_crisis_the_anatomy_of_institutional_failure.pdf

> │                ├── 📄 NT_wrongful_foreclosure_a_case_study_in_civil_rig.pdf

> │                ├── 📄 OR_void_judgment_eviction_crisis.pdf

> │              └── 📂 60_infographics/

> │                ├── 📄 OR_Void_Judgment_Eviction_Crisis.pdf

> │              └── 📂 70_reports/

> │                ├── 📄 NT_Crisis_The_Anatomy_of_Institutional_Failure.pdf

> │                ├── 📄 NT_Wrongful_Foreclosure_A_Case_Study_in_Civil_Rig.pdf

> │                ├── 📄 NT__Session_Summary_2025-12-15_i_knew_b.md

> │                ├── 📄 NT_case-narrative-wrongful-foreclosure-and-displ.html

> │                ├── 📄 NT_legal-memorandum.html

> │                ├── 📄 NT_procedural_failure_map_one_pager.html

> │                ├── 📄 NT_talking_points.html

> │                ├── 📄 NT_uncategorized_bundle.pdf

> │                ├── 📄 OR_Void_Judgment_Eviction_Crisis.pdf

> │                ├── 📄 PL_70_reports.md

> │                ├── 📄 PL_proposal-for-strategic-reports-in-the-matter-.html

> │              ├── 📄 NT_10_overviews.md

> │            └── 📂 50_protocols/

> │              ├── 📄 NT_PROTOCOL_Canonical_Case_Knowledge_Base.md

> │            └── 📂 70_templates/

> │              └── 📂 10_motions/

> │                ├── 📄 MO_10_motions.md

> │                ├── 📄 MO_TEMPLATE_motion_emergency_stay_of_writ.md

> │                ├── 📄 MO_TEMPLATE_motion_emergency_supplemental_motion_ongoing_ha.md

> │                ├── 📄 MO_TEMPLATE_motion_to_vacate_void_judgment.md

> │              └── 📂 20_declarations/

> │                ├── 📄 NT_GUIDE_Witness_Instructions.md

> │                ├── 📄 NT_TEMPLATE_Gender_Identity_Clarification.md

> │                ├── 📄 PL_20_declarations.md

> │                ├── 📄 PL_TEMPLATE_ADA_Disability_Affidavit.md

> │                ├── 📄 PL_TEMPLATE_Character_Affidavit.md

> │                ├── 📄 PL_TEMPLATE_Community_Service_Affidavit.md

> │                ├── 📄 PL_TEMPLATE_Credibility_Affidavit.md

> │                ├── 📄 PL_TEMPLATE_Declarations.md

> │                ├── 📄 PL_TEMPLATE_Observations_Affidavit.md

> │                ├── 📄 PL_TEMPLATE_affidavit_not_served.md

> │                ├── 📄 PL_TEMPLATE_updated_affidavit_language.md

> │                ├── 📄 PL_TEMPLATE_verified_affidavit_of_defendant.md

> │              └── 📂 30_exhibits/

> │                ├── 📄 EXH_30_exhibits.md

> │                ├── 📄 EXH_TEMPLATE_Exhibit_List.md

> │              └── 📂 40_orders/

> │                ├── 📄 MO_TEMPLATE_proposed_order_motion_to_vacate.md

> │                ├── 📄 OR_40_orders.md

> │                ├── 📄 OR_TEMPLATE_Proposed_Order.md

> │                ├── 📄 OR_TEMPLATE_proposed_order_emergency_stay.md

> │              └── 📂 50_internal/

> │                ├── 📄 NT_TEMPLATE_Advocate_Outreach.md

> │                ├── 📄 NT_TEMPLATE_Court_Doc.md

> │                ├── 📄 NT_TEMPLATE_Fact_Timeline.md

> │                ├── 📄 NT_TEMPLATE_Handup_Packet_Note.md

> │                ├── 📄 NT_TEMPLATE_Section_Cover.md

> │                ├── 📄 NT_TEMPLATE_Section_Index.md

> │                ├── 📄 NT_TEMPLATE_Service_Matrix.md

> │                ├── 📄 NT_TEMPLATE_Timeline_Event.md

> │                ├── 📄 NT_TEMPLATE_Violation_Entry.md

> │                ├── 📄 NT_TEMPLATE_War_Note.md

> │                ├── 📄 NT_TEMPLATE_ada_packet.md

> │                ├── 📄 NT_TEMPLATE_attorney_brief.md

> │                ├── 📄 NT_TEMPLATE_receipt_usps_tracking.md

> │                ├── 📄 NT_TEMPLATE_script_call_lawyers.md

> │              ├── 📄 NT_40_templates.md

> │            └── 📂 80_integrity_tooling/

> │              ├── 📄 NT_50_integrity_tooling.md

> │              ├── 📄 NT_rename_plan.txt

> │              ├── 📄 NT_run_renames.ps1

> │              ├── 📄 PL_conflicts_report.txt

> │            └── 📂 90_pack_blueprints/

> │              ├── 📄 NT_60_pack_blueprints.md

> │              ├── 📄 NT_PACK_AGENCY.yaml

> │              ├── 📄 NT_PACK_JUDGE.yaml

> │              ├── 📄 NT_PACK_OPPOSING.yaml

> │              ├── 📄 NT_PACK_SELF.yaml

> │              ├── 📄 NT_PROPOSED_OUTPUT_STRUCTURE.md

> │            ├── 📄 NT_00_ADMIN.md

> │      └── 📂 vis/

> │        └── 📂 10_violations/

> │          ├── 📄 EXH_Exhibit X — Inventory of Jurisdictional, Execut.md

> │          ├── 📄 NT_V-005_failure-to-correct-inaccurate-furnishings.md

> │          ├── 📄 NT_V-006_dual-tradeline-double-counting.md

> │          ├── 📄 NT_V-008_credit-defamation-false-publication.md

> │          ├── 📄 NT_V-009_fdCPA-misrepresentation-of-debt-status.md

> │          ├── 📄 NT_V-010_failure-to-mark-account-foreclosure-closed.md

> │          ├── 📄 NT_V-011_experian-reinvestigation-failure.md

> │          ├── 📄 NT_V-012_equifax-reinvestigation-failure.md

> │          ├── 📄 NT_V-013_transunion-reinvestigation-failure.md

> │          ├── 📄 NT_V-020_post-0815-aes-electric-charges-billed.md

> │          ├── 📄 NT_V-021_post-0815-citizens-energy-charges-billed.md

> │          ├── 📄 NT_V-022_post-0815-hoa-assessments-billed.md

> │          ├── 📄 NT_V-023_city-grass-cut-ticket-assessed-after-loss-of-access.md

> │          ├── 📄 NT_V-024_municipal-code-enforcement-after-possession-transfer.md

> │          ├── 📄 NT_V-025_cost-shift-fcfcu-refused-winterize.md

> │          ├── 📄 NT_V-026_credit-harm-compounded-utility-municipal.md

> │          ├── 📄 NT_V-031_sheriff-return-inaccuracies.md

> │          ├── 📄 NT_V-033_removal-6-7-days-after-deed-recorded.md

> │          ├── 📄 NT_V-035_court-relied-on-service-sufficiency.md

> │          ├── 📄 NT_V-036_surplus-funds-declared-resolved.md

> │          ├── 📄 NT_V-037_interest-fees-arbitrarily-inflated.md

> │          ├── 📄 NT_V-038_fcfcu-testimony-winterize-then-leave.md

> │          ├── 📄 NT_V-070_global-demand-letter.md

> │          ├── 📄 NT_V-071_litigation-hold-preservation-letter.md

> │          ├── 📄 NT_V-072_equitable-relief-tradeline-deletion.md

> │          ├── 📄 NT_V-073_damages-credit-score-suppression.md

> │          ├── 📄 NT_V-074_damages-out-of-pocket-costs.md

> │          ├── 📄 NT_V-075_public-accountability-hold.md

> │          ├── 📄 NT_V-076_fha-reasonable-accommodation-failure.md

> │          ├── 📄 NT_V-077_ada-title-iii-entertainment-access-failure.md

> │          ├── 📄 NT_V-078_ada-effective-communication-failure.md

> │          ├── 📄 NT_V-080_conversion-negligence-post-removal-damage.md

> │          ├── 📄 NT_V-081_evidence-spoliation-unplugged-cameras.md

> │          ├── 📄 NT_V-082_fraud-on-the-court-material-misrepresentation.md

> │          ├── 📄 NT_V-083_discriminatory-maintenance-redlining.md

> │          ├── 📄 NT_V-084_predatory-land-contract-reverse-redlining.md

> │          ├── 📄 OR_V-001_fcfcu-continues-reporting-first-mortgage-post-judgment-sale.md

> │          ├── 📄 OR_V-002_fcfcu-continues-reporting-second-mortgage-post-judgment-sale.md

> │          ├── 📄 OR_V-003_monthly-delinquencies-after-foreclosure-judgment.md

> │          ├── 📄 OR_V-004_past-due-amount-schedule-after-judgment.md

> │          ├── 📄 OR_V-079_void-judgment-procedural-error.md

> │          ├── 📄 PL_V-007_inconsistent-reporting-vs-court-position.md

> │          ├── 📄 PL_V-030_service-completed-no-notice-before-writ.md

> │          ├── 📄 PL_V-032_no-ada-compliant-notice.md

> │          ├── 📄 PL_V-034_attorney-appeared-without-formal-appearance.md

> │          ├── 📄 PL_V-050_cfpb-complaint-track.md

> │          ├── 📄 PL_V-051_indiana-ag-complaint-track.md

> │          ├── 📄 PL_V-052_icrc-complaint-track.md

> │          ├── 📄 PL_V-053_doj-civil-rights-complaint-track.md

> │          ├── 📄 PL_V-060_bbb-complaint-reputational-pressure.md

> │        └── 📂 20_theories/

> │          ├── 📄 NT_BACKUP_ARGUMENTS.md

> │          ├── 📄 NT_IF_JUDGE_PUSHBACK.md

> │        └── 📂 30_legal_research/

> │          ├── 📄 NT_CASE_LAW_RESEARCH.md

> │          ├── 📄 NT_JURISDICTION_THEORY.md

> │          ├── 📄 NT_LEGAL MEMORANDUM.md

> │          ├── 📄 NT_VOID_VS_VOIDABLE_ANALYSIS.md

> │        └── 📂 40_analysis/

> │          ├── 📄 NT_INTERNAL VALUATION MEMO.md

> │          ├── 📄 NT_Procedural_failure_map_one_pager.md

> │          ├── 📄 NT_Violation_Remedy_Inventory.md

> │        └── 📂 50_strategies/

> │          ├── 📄 NT_00_basis.md

> │          ├── 📄 NT_10_ada_strategy.md

> │          ├── 📄 NT_ADA_TITLE_II_ANALYSIS.md

> │          ├── 📄 NT_BUT_FOR_ANALYSIS.md

> │          ├── 📄 NT_Master_Strategy_Canvas.canvas

> │          ├── 📄 NT_PROCEDURAL_FAILURE_MAP.md

> │          ├── 📄 NT_REASONABLE_ACCOMMODATIONS.md

> │          ├── 📄 NT_REVERSAL_PATHS.md

> │          ├── 📄 NT_STATUS_TRACKER.md

> │          ├── 📄 NT_STAY_PATHS.md

> │          ├── 📄 NT_integrate_disability_separate_appe.m4a

> │          ├── 📄 OR_void_judgment_eviction_crisis.pdf

> │          ├── 📄 PL_DOJ_COMPLAINT.md

> │          ├── 📄 PL_ICRC_COMPLAINT.md

> │          ├── 📄 PL_Proposal for Strategic Reports in the Matter of.md

> │          ├── 📄 Strategic_Plan.canvas

> │        └── 📂 60_data_inventories/

> │          ├── 📄 NT_Violation_Index.md

> │          ├── 📄 NT_foreclosure-and-housing-litigation-case-record.csv

> │          ├── 📄 NT_inventory-of-civil-and-fair-housing-rights-vio.csv

> │        ├── 📄 NT_01_MASTER_INDEX.md

> │        ├── 📄 _C_VIS.md

> │        ├── 📄 vis.yaml

> │      ├── 📄 vis_index.md

> │    ├── 📄 package-lock.json

> │    ├── 📄 package.json

> │    ├── 📄 prepare_vitepress.py

> └── 📂 content/

> │  └── 📂 0_ADMIN/

> │    └── 📂 10_index/

> │      ├── 📄 NT_00_index.md

> │      ├── 📄 NT_Contacts.md

> │    └── 📂 20_case_logs/

> │      ├── 📄 NT_2025-12-09_Writ_Executed_Forced_Removal.md

> │      ├── 📄 NT_2025-12-15_Case_DNA_Strategy_Checkpoint.md

> │      ├── 📄 NT_2025-12-15_Strategic_Planning_Session.md

> │      ├── 📄 NT_2025-12-16_Post_Removal_Access_Denial.md

> │      ├── 📄 NT_2025-12-16_case_log_entry.md

> │      ├── 📄 NT_2025-12-16_case_summary.md

> │      ├── 📄 NT_2025-12-16_fcfcu_case_dna_strat.md

> │      ├── 📄 NT_2025-12-21_Case_Summary.md

> │      ├── 📄 NT_2026-01-16_Cleanup_Log.md

> │      ├── 📄 NT_20_case_logs.md

> │      ├── 📄 NT_INGEST_2025-12-16_case_log_entry.md

> │      ├── 📄 NT_Master_Case_Log.md

> │      ├── 📄 NT_content_manifest_hashes.json

> │      ├── 📄 NT_ingest_dedupe_manifest.json

> │      ├── 📄 PL_integrity_scan_report.json

> │    └── 📂 30_financial/

> │      ├── 📄 NT_02_financial.md

> │      ├── 📄 NT_Financial_Tracker.md

> │    └── 📂 40_overviews/

> │      └── 📂 10_maps/

> │        ├── 📄 NT_Procedural_failure_map_one_pager.md

> │      └── 📂 20_deep_dives/

> │        ├── 📄 NT_Integrate_Disability_Separate_Appeals_Get_Stay.m4a

> │        ├── 📄 NT_foreclosure_void_versus_damages_due_process.m4a

> │        ├── 📄 NT_forensic_audit_of_a_void_foreclosure.m4a

> │        ├── 📄 OR_foreclosure_void_judgment_institutional_failur.m4a

> │      └── 📂 30_critiques/

> │      └── 📂 40_debates/

> │        ├── 📄 NT_debate.m4a

> │      └── 📂 50_explainers/

> │        ├── 📄 NT_crisis_the_anatomy_of_institutional_failure.pdf

> │        ├── 📄 NT_wrongful_foreclosure_a_case_study_in_civil_rig.pdf

> │        ├── 📄 OR_void_judgment_eviction_crisis.pdf

> │      └── 📂 60_infographics/

> │        ├── 📄 OR_Void_Judgment_Eviction_Crisis.pdf

> │      └── 📂 70_reports/

> │        ├── 📄 NT_Crisis_The_Anatomy_of_Institutional_Failure.pdf

> │        ├── 📄 NT_Wrongful_Foreclosure_A_Case_Study_in_Civil_Rig.pdf

> │        ├── 📄 NT__Session_Summary_2025-12-15_i_knew_b.md

> │        ├── 📄 NT_case-narrative-wrongful-foreclosure-and-displ.html

> │        ├── 📄 NT_legal-memorandum.html

> │        ├── 📄 NT_procedural_failure_map_one_pager.html

> │        ├── 📄 NT_talking_points.html

> │        ├── 📄 NT_uncategorized_bundle.pdf

> │        ├── 📄 OR_Void_Judgment_Eviction_Crisis.pdf

> │        ├── 📄 PL_70_reports.md

> │        ├── 📄 PL_proposal-for-strategic-reports-in-the-matter-.html

> │      ├── 📄 NT_10_overviews.md

> │    └── 📂 50_protocols/

> │      ├── 📄 NT_PROTOCOL_Canonical_Case_Knowledge_Base.md

> │    └── 📂 70_templates/

> │      └── 📂 10_motions/

> │        ├── 📄 MO_10_motions.md

> │        ├── 📄 MO_TEMPLATE_motion_emergency_stay_of_writ.md

> │        ├── 📄 MO_TEMPLATE_motion_emergency_supplemental_motion_ongoing_ha.md

> │        ├── 📄 MO_TEMPLATE_motion_to_vacate_void_judgment.md

> │      └── 📂 20_declarations/

> │        ├── 📄 NT_GUIDE_Witness_Instructions.md

> │        ├── 📄 NT_TEMPLATE_Gender_Identity_Clarification.md

> │        ├── 📄 PL_20_declarations.md

> │        ├── 📄 PL_TEMPLATE_ADA_Disability_Affidavit.md

> │        ├── 📄 PL_TEMPLATE_Character_Affidavit.md

> │        ├── 📄 PL_TEMPLATE_Community_Service_Affidavit.md

> │        ├── 📄 PL_TEMPLATE_Credibility_Affidavit.md

> │        ├── 📄 PL_TEMPLATE_Declarations.md

> │        ├── 📄 PL_TEMPLATE_Observations_Affidavit.md

> │        ├── 📄 PL_TEMPLATE_affidavit_not_served.md

> │        ├── 📄 PL_TEMPLATE_updated_affidavit_language.md

> │        ├── 📄 PL_TEMPLATE_verified_affidavit_of_defendant.md

> │      └── 📂 30_exhibits/

> │        ├── 📄 EXH_30_exhibits.md

> │        ├── 📄 EXH_TEMPLATE_Exhibit_List.md

> │      └── 📂 40_orders/

> │        ├── 📄 MO_TEMPLATE_proposed_order_motion_to_vacate.md

> │        ├── 📄 OR_40_orders.md

> │        ├── 📄 OR_TEMPLATE_Proposed_Order.md

> │        ├── 📄 OR_TEMPLATE_proposed_order_emergency_stay.md

> │      └── 📂 50_internal/

> │        ├── 📄 NT_TEMPLATE_Advocate_Outreach.md

> │        ├── 📄 NT_TEMPLATE_Court_Doc.md

> │        ├── 📄 NT_TEMPLATE_Fact_Timeline.md

> │        ├── 📄 NT_TEMPLATE_Handup_Packet_Note.md

> │        ├── 📄 NT_TEMPLATE_Section_Cover.md

> │        ├── 📄 NT_TEMPLATE_Section_Index.md

> │        ├── 📄 NT_TEMPLATE_Service_Matrix.md

> │        ├── 📄 NT_TEMPLATE_Timeline_Event.md

> │        ├── 📄 NT_TEMPLATE_Violation_Entry.md

> │        ├── 📄 NT_TEMPLATE_War_Note.md

> │        ├── 📄 NT_TEMPLATE_ada_packet.md

> │        ├── 📄 NT_TEMPLATE_attorney_brief.md

> │        ├── 📄 NT_TEMPLATE_receipt_usps_tracking.md

> │        ├── 📄 NT_TEMPLATE_script_call_lawyers.md

> │      ├── 📄 NT_40_templates.md

> │    └── 📂 80_integrity_tooling/

> │      ├── 📄 NT_50_integrity_tooling.md

> │      ├── 📄 NT_rename_plan.txt

> │      ├── 📄 NT_run_renames.ps1

> │      ├── 📄 PL_conflicts_report.txt

> │    └── 📂 90_pack_blueprints/

> │      ├── 📄 NT_60_pack_blueprints.md

> │      ├── 📄 NT_PACK_AGENCY.yaml

> │      ├── 📄 NT_PACK_JUDGE.yaml

> │      ├── 📄 NT_PACK_OPPOSING.yaml

> │      ├── 📄 NT_PACK_SELF.yaml

> │      ├── 📄 NT_PROPOSED_OUTPUT_STRUCTURE.md

> │    ├── 📄 NT_00_ADMIN.md

> │  └── 📂 A_TIMELINE/

> │    └── 📂 2023/

> │      ├── 📄 NT_index.md

> │      └── 📂 events/

> │    └── 📂 2024/

> │      ├── 📄 NT_index.md

> │      └── 📂 events/

> │    └── 📂 2025/

> │      ├── 📄 NT_index.md

> │      └── 📂 events/

> │        ├── 📄 MO_2025-05-13_Motion_for_Default_Judgment 1.md

> │        ├── 📄 MO_2025-05-13_Motion_for_Default_Judgment.md

> │        ├── 📄 MO_2025-05-23_Amended_Motion_Default_Judgment 1.md

> │        ├── 📄 MO_2025-05-23_Amended_Motion_Default_Judgment.md

> │        ├── 📄 MO_2025-12-10_Motions_Filed 1.md

> │        ├── 📄 MO_2025-12-10_Motions_Filed.md

> │        ├── 📄 MO_2025-12-12_Supplemental_Emergency_Motion 1.md

> │        ├── 📄 MO_2025-12-12_Supplemental_Emergency_Motion.md

> │        ├── 📄 NT_2025-01-16_Case_Filed 1.md

> │        ├── 📄 NT_2025-01-16_Case_Filed.md

> │        ├── 📄 NT_2025-03-05_Service_Attempt_1 1.md

> │        ├── 📄 NT_2025-03-05_Service_Attempt_1.md

> │        ├── 📄 NT_2025-04-15_Service_Attempt_2 1.md

> │        ├── 📄 NT_2025-04-15_Service_Attempt_2.md

> │        ├── 📄 NT_2025-08-15_Sheriff_Sale 1.md

> │        ├── 📄 NT_2025-08-15_Sheriff_Sale.md

> │        ├── 📄 NT_2025-11-06_Writ_of_Assistance_Issued 1.md

> │        ├── 📄 NT_2025-11-06_Writ_of_Assistance_Issued.md

> │        ├── 📄 NT_2025-12-09_Writ_Executed_Forced_Removal.md

> │        ├── 📄 NT_2025-12-09_Writ_Executed_Removal.md

> │        ├── 📄 NT_2025-12-16_Post_Removal_Access_Denial.md

> │        ├── 📄 NT_2025-12-21_Case_Summary.md

> │        ├── 📄 OR_2025-05-21_Order_Denying_Default_Judgment 1.md

> │        ├── 📄 OR_2025-05-21_Order_Denying_Default_Judgment.md

> │        ├── 📄 OR_2025-05-28_Default_Judgment_Entered 1.md

> │        ├── 📄 OR_2025-05-28_Default_Judgment_Entered.md

> │        ├── 📄 OR_2025-12-11_Court_Orders_and_Hearing_Scheduled 1.md

> │        ├── 📄 OR_2025-12-11_Court_Orders_and_Hearing_Scheduled.md

> │        ├── 📄 PL_2025-05-30_Praecipe_Sheriff_Sale 1.md

> │        ├── 📄 PL_2025-05-30_Praecipe_Sheriff_Sale.md

> │        ├── 📄 PL_2025-07-09_Sheriff_Sale_Notice_Posted 1.md

> │        ├── 📄 PL_2025-07-09_Sheriff_Sale_Notice_Posted.md

> │        ├── 📄 PL_2025-10-29_Petition_for_Writ_of_Assistance 1.md

> │        ├── 📄 PL_2025-10-29_Petition_for_Writ_of_Assistance.md

> │    └── 📂 2026/

> │      ├── 📄 NT_index.md

> │      └── 📂 events/

> │    ├── 📄 _A_TIMELINE.md

> │  └── 📂 B_EVIDENCE/

> │    └── 📂 10_evidence_admin/

> │      ├── 📄 00_evidence_admin.md

> │      ├── 📄 10_chain_of_custody.md

> │      ├── 📄 20_Evidence_Log.md

> │      ├── 📄 EXH_Raw_Exhibit_Map.md

> │      ├── 📄 _10_evidence_admin.md

> │    └── 📂 20_court_record/

> │      └── 📂 10_docket_files/

> │        ├── 📄 022_Plaintif_bid_2025_07_17_10_14_40.pdf.pdf

> │        ├── 📄 024_Service Returned Served.pdf

> │        ├── 📄 026_2025_10_29_13_47_03.pdf.pdf

> │        ├── 📄 029_Emergency_Supplemental_Declara.pdf

> │        ├── 📄 035_01092026_005.pdf.pdf

> │        ├── 📄 EXH_026_Exhibit_List_A-G.pdf

> │        ├── 📄 EXH__026_Exhibit_List_A-G.pdf

> │        ├── 📄 MO_013_Motion_for_Default_Judgment.pdf

> │        ├── 📄 MO_016_Order_Denying_Motion_for_Default_Judgment.pdf

> │        ├── 📄 MO_019_Amended_Motion_Default_Judgment_1.pdf

> │        ├── 📄 MO_020_Amended_Motion_Default_Judgment_2.pdf

> │        ├── 📄 MO_025_Motion_Vacate_Stay_Writ.pdf

> │        ├── 📄 MO_027_Supplemental_Motion_Access.pdf

> │        ├── 📄 MO__013_Motion_for_Default_Judgment.pdf

> │        ├── 📄 MO__019_Amended_Motion_Default_Judgmen.pdf

> │        ├── 📄 MO__020_Amended_Motion_Default_Judgmen.pdf

> │        ├── 📄 MO__025_Motion_Vacate_Stay_Writ.pdf

> │        ├── 📄 MO__027_Supplemental_Motion_Access.pdf

> │        ├── 📄 OR_023_Decree_Foreclosure_Returned.pdf

> │        ├── 📄 OR_031_Proposed_Order_Vacate.pdf

> │        ├── 📄 OR_032_Proposed_Order_Stay.pdf

> │        ├── 📄 OR__017_Order_Denying_Default_Judgment.pdf

> │        ├── 📄 OR__023_Decree_Foreclosure_Returned.pdf

> │        ├── 📄 OR__031_Proposed_Order_Vacate.pdf

> │        ├── 📄 OR__032_Proposed_Order_Stay.pdf

> │        ├── 📄 PL_001_Complaint.pdf

> │        ├── 📄 PL_002_Appearance.pdf

> │        ├── 📄 PL_003_Request_for_Admissions.pdf

> │        ├── 📄 PL_004_Notice_to_Homeowners.pdf

> │        ├── 📄 PL_005_Appearance_2.pdf

> │        ├── 📄 PL_006_Summons_1.pdf

> │        ├── 📄 PL_007_Summons_2.pdf

> │        ├── 📄 PL_008_Summons_3.pdf

> │        ├── 📄 PL_009_Summons_4.pdf

> │        ├── 📄 PL_010_Summons_5.pdf

> │        ├── 📄 PL_011_Service_Returned_03-05-2025.pdf

> │        ├── 📄 PL_012_Service_Returned_04-15-2025.pdf

> │        ├── 📄 PL_014_Affidavit.pdf

> │        ├── 📄 PL_015_Affidavit_Attorney_Fees.pdf

> │        ├── 📄 PL_017_OMITTED NOTICE OF SERVICE TO DEFENDANT.pdf

> │        ├── 📄 PL_018_Omitted_Notice_of_Service.pdf

> │        ├── 📄 PL_021_Praecipe_Sheriff_Sale_1.pdf

> │        ├── 📄 PL_022_Praecipe_Sheriff_Sale_2.pdf

> │        ├── 📄 PL_024_Petition_Writ_of_Assistance.pdf

> │        ├── 📄 PL_028_Report_Court_Defendant_Request.pdf

> │        ├── 📄 PL_029_Emergency_Supplemental_Declaration.pdf

> │        ├── 📄 PL_030_Report_Sheriff_Sale_No_Excess.pdf

> │        ├── 📄 PL_033_ADA_Disability_Affidavit.pdf

> │        ├── 📄 PL_2026-01-09_Appearance_Plaintiff.pdf

> │        ├── 📄 PL__001_Complaint.pdf

> │        ├── 📄 PL__002_Appearance.pdf

> │        ├── 📄 PL__003_Request_for_Admissions.pdf

> │        ├── 📄 PL__004_Notice_to_Homeowners.pdf

> │        ├── 📄 PL__005_Appearance_2.pdf

> │        ├── 📄 PL__006_Summons_1.pdf

> │        ├── 📄 PL__007_Summons_2.pdf

> │        ├── 📄 PL__008_Summons_3.pdf

> │        ├── 📄 PL__009_Summons_4.pdf

> │        ├── 📄 PL__010_Summons_5.pdf

> │        ├── 📄 PL__011_Service_Returned_03-05-2025.pdf

> │        ├── 📄 PL__012_Service_Returned_04-15-2025.pdf

> │        ├── 📄 PL__014_Affidavit.pdf

> │        ├── 📄 PL__015_Affidavit_Attorney_Fees.pdf

> │        ├── 📄 PL__016_Affidavit_Additional.pdf

> │        ├── 📄 PL__018_Omitted_Notice_of_Service.pdf

> │        ├── 📄 PL__021_Praecipe_Sheriff_Sale_1.pdf

> │        ├── 📄 PL__022_Praecipe_Sheriff_Sale_2.pdf

> │        ├── 📄 PL__024_Petition_Writ_of_Assistance.pdf

> │        ├── 📄 PL__028_Report_Court_Defendant_Request.pdf

> │        ├── 📄 PL__030_Report_Sheriff_Sale_No_Excess.pdf

> │        ├── 📄 PL__033_ADA_Disability_Affidavit.pdf

> │      ├── 📄 20_court_record.md

> │    └── 📂 30_primary/

> │      └── 📂 10_fcfcu/

> │        ├── 📄 2023-09-20_FCFCU_Hardship_and_Healt.md

> │        ├── 📄 2024-03-20_fcfcu_certified_response_tax_record.pdf

> │        ├── 📄 2024-12-09_outgoing_email_bank_access_request.pdf

> │        ├── 📄 2024-12-11_outgoing_email_bank_access_request.pdf

> │        ├── 📄 20241204_FCFCU_Statement (1).pdf

> │        ├── 📄 20241204_FCFCU_Statement (2).pdf

> │        ├── 📄 20241204_fcfcu_statement-(1).pdf

> │        ├── 📄 20241204_fcfcu_statement-(2).pdf

> │        ├── 📄 20241204_fcfcu_statement.pdf

> │        ├── 📄 2025-12-20_exh-30_fcfcu_740eacdc_2025-12-20_ex.jpg

> │        ├── 📄 2025-12-20_exh-30_fcfcu_ac6eb2ea_2025-12-20_ex.jpg

> │        ├── 📄 21june-24-4817shadow_appraisal.pdf

> │        ├── 📄 PL_2023-09-20_FCFCU_Hardship_and_Health_Notice_Let.md

> │        ├── 📄 PL_2023-09-20_fcfcu_hardship_and_health_notice_le.pdf

> │        ├── 📄 PL_2023-09-20_notice_disabilities_hardship.pdf

> │        ├── 📄 PL_2024-20-03_response_to_tax_notice.pdf

> │        ├── 📄 PL_fcfcu_v_cr-v_report_to_court.pdf

> │        ├── 📄 PL_report_to_court_on_defendants_request.pdf

> │        ├── 📄 _README.md

> │      └── 📂 20_aes/

> │        ├── 📄 2025-06-08_aes_ada_request_financial_hardship_.pdf

> │        ├── 📄 PL_2025-06-08_aes_ada_notice.pdf

> │        ├── 📄 PL_2025-12-16_AES_Emergency_Notice.md

> │        ├── 📄 _README.md

> │    └── 📂 40_supporting/

> │      ├── 📄 40_supporting.md

> │      └── 📂 docs/

> │        └── 📂 affidavits/

> │          ├── 📄 PL_affidavits.md

> │          └── 📂 ada-disability/

> │          └── 📂 character/

> │          └── 📂 community-service/

> │          └── 📂 credibility/

> │          └── 📂 observations/

> │        └── 📂 declarations/

> │          ├── 📄 PL_declarations.md

> │        └── 📂 receipts/

> │          ├── 📄 NT_2025-12-20_exh-20_receipts_0860d3df_2025-12-20.jpg

> │          ├── 📄 NT_Odyssey_Envelope_Receipt.pdf

> │        └── 📂 records/

> │          ├── 📄 Foreclosure and Housing Litigation Case Record.csv

> │          ├── 📄 Inventory of Civil and Fair Housing Rights Vio.csv

> │      └── 📂 multi-media/

> │        ├── 📄 2025-12-20_exh-10_photos_video_00241326_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_012aa06e_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_01b3e905_2025-1.png

> │        ├── 📄 2025-12-20_exh-10_photos_video_10f4975d_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_1a80b987_2025-1.mp4

> │        ├── 📄 2025-12-20_exh-10_photos_video_1beefb11_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_1f3f8a81_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_25fb1992_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_2f0952db_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_49c74ec6_2025-.heic

> │        ├── 📄 2025-12-20_exh-10_photos_video_4e01fa01_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_5be451ba_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_5d95cae5_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_61129253_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_63fb7b02_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_71c9e6a7_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_78ba1ccc_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_7a544ef7_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_8350e7be_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_8a163413_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_8d885a5c_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_942cfd7f_2025-1.png

> │        ├── 📄 2025-12-20_exh-10_photos_video_9b611100_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_9fb3a08a_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_9ff5022d_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_a8832e17_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_ca02d006_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_db9b10b5_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_e4cb3622_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_ebaaa38d_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_ed6dc885_2025-1.mp4

> │        ├── 📄 2025-12-20_exh-10_photos_video_f510498b_2025-.heic

> │        ├── 📄 2025-12-20_exh-10_photos_video_f60d8098_2025-1.png

> │        ├── 📄 2025-12-20_exh-10_photos_video_f98b089a_2025-1.png

> │        ├── 📄 2025-12-20_exh-10_photos_video_fa1703bf_2025-1.jpg

> │        ├── 📄 2025-12-20_exh-10_photos_video_fdd8d4ef_2025-1.jpg

> │      └── 📂 property/

> │        └── 📂 10_mortgage_history/

> │          └── 📂 10_payments/

> │            ├── 📄 2025-12-20_EXH-20_payments_c5131deb_2025-12-20.png

> │            ├── 📄 2025-12-20_exh-20_payments_c5131deb_2025-12-20 (2).png

> │            ├── 📄 20_payments.md

> │        └── 📂 20_parcel/

> │          ├── 📄 Parcel_6016506_PRC.pdf

> │          ├── 📄 Parcel_6016506_ParcelDetailHistory.pdf

> │          ├── 📄 parcel_6016506_parceldetailhistory (2).pdf

> │          ├── 📄 parcel_6016506_prc (2).pdf

> │    └── 📂 50_quarantine_candidates/

> │      ├── 📄 50_quarantine_candidates.md

> │    ├── 📄 _B_EVIDENCE.md

> │  └── 📂 C_VIS/

> │    └── 📂 10_violations/

> │      ├── 📄 EXH_Exhibit X — Inventory of Jurisdictional, Execut.md

> │      ├── 📄 NT_V-005_failure-to-correct-inaccurate-furnishings.md

> │      ├── 📄 NT_V-006_dual-tradeline-double-counting.md

> │      ├── 📄 NT_V-008_credit-defamation-false-publication.md

> │      ├── 📄 NT_V-009_fdCPA-misrepresentation-of-debt-status.md

> │      ├── 📄 NT_V-010_failure-to-mark-account-foreclosure-closed.md

> │      ├── 📄 NT_V-011_experian-reinvestigation-failure.md

> │      ├── 📄 NT_V-012_equifax-reinvestigation-failure.md

> │      ├── 📄 NT_V-013_transunion-reinvestigation-failure.md

> │      ├── 📄 NT_V-020_post-0815-aes-electric-charges-billed.md

> │      ├── 📄 NT_V-021_post-0815-citizens-energy-charges-billed.md

> │      ├── 📄 NT_V-022_post-0815-hoa-assessments-billed.md

> │      ├── 📄 NT_V-023_city-grass-cut-ticket-assessed-after-loss-of-access.md

> │      ├── 📄 NT_V-024_municipal-code-enforcement-after-possession-transfer.md

> │      ├── 📄 NT_V-025_cost-shift-fcfcu-refused-winterize.md

> │      ├── 📄 NT_V-026_credit-harm-compounded-utility-municipal.md

> │      ├── 📄 NT_V-031_sheriff-return-inaccuracies.md

> │      ├── 📄 NT_V-033_removal-6-7-days-after-deed-recorded.md

> │      ├── 📄 NT_V-035_court-relied-on-service-sufficiency.md

> │      ├── 📄 NT_V-036_surplus-funds-declared-resolved.md

> │      ├── 📄 NT_V-037_interest-fees-arbitrarily-inflated.md

> │      ├── 📄 NT_V-038_fcfcu-testimony-winterize-then-leave.md

> │      ├── 📄 NT_V-070_global-demand-letter.md

> │      ├── 📄 NT_V-071_litigation-hold-preservation-letter.md

> │      ├── 📄 NT_V-072_equitable-relief-tradeline-deletion.md

> │      ├── 📄 NT_V-073_damages-credit-score-suppression.md

> │      ├── 📄 NT_V-074_damages-out-of-pocket-costs.md

> │      ├── 📄 NT_V-075_public-accountability-hold.md

> │      ├── 📄 NT_V-076_fha-reasonable-accommodation-failure.md

> │      ├── 📄 NT_V-077_ada-title-iii-entertainment-access-failure.md

> │      ├── 📄 NT_V-078_ada-effective-communication-failure.md

> │      ├── 📄 NT_V-080_conversion-negligence-post-removal-damage.md

> │      ├── 📄 NT_V-081_evidence-spoliation-unplugged-cameras.md

> │      ├── 📄 NT_V-082_fraud-on-the-court-material-misrepresentation.md

> │      ├── 📄 NT_V-083_discriminatory-maintenance-redlining.md

> │      ├── 📄 NT_V-084_predatory-land-contract-reverse-redlining.md

> │      ├── 📄 OR_V-001_fcfcu-continues-reporting-first-mortgage-post-judgment-sale.md

> │      ├── 📄 OR_V-002_fcfcu-continues-reporting-second-mortgage-post-judgment-sale.md

> │      ├── 📄 OR_V-003_monthly-delinquencies-after-foreclosure-judgment.md

> │      ├── 📄 OR_V-004_past-due-amount-schedule-after-judgment.md

> │      ├── 📄 OR_V-079_void-judgment-procedural-error.md

> │      ├── 📄 PL_V-007_inconsistent-reporting-vs-court-position.md

> │      ├── 📄 PL_V-030_service-completed-no-notice-before-writ.md

> │      ├── 📄 PL_V-032_no-ada-compliant-notice.md

> │      ├── 📄 PL_V-034_attorney-appeared-without-formal-appearance.md

> │      ├── 📄 PL_V-050_cfpb-complaint-track.md

> │      ├── 📄 PL_V-051_indiana-ag-complaint-track.md

> │      ├── 📄 PL_V-052_icrc-complaint-track.md

> │      ├── 📄 PL_V-053_doj-civil-rights-complaint-track.md

> │      ├── 📄 PL_V-060_bbb-complaint-reputational-pressure.md

> │    └── 📂 20_theories/

> │      ├── 📄 NT_BACKUP_ARGUMENTS.md

> │      ├── 📄 NT_IF_JUDGE_PUSHBACK.md

> │    └── 📂 30_legal_research/

> │      ├── 📄 NT_CASE_LAW_RESEARCH.md

> │      ├── 📄 NT_JURISDICTION_THEORY.md

> │      ├── 📄 NT_LEGAL MEMORANDUM.md

> │      ├── 📄 NT_VOID_VS_VOIDABLE_ANALYSIS.md

> │    └── 📂 40_analysis/

> │      ├── 📄 NT_INTERNAL VALUATION MEMO.md

> │      ├── 📄 NT_Procedural_failure_map_one_pager.md

> │      ├── 📄 NT_Violation_Remedy_Inventory.md

> │    └── 📂 50_strategies/

> │      ├── 📄 NT_00_basis.md

> │      ├── 📄 NT_10_ada_strategy.md

> │      ├── 📄 NT_ADA_TITLE_II_ANALYSIS.md

> │      ├── 📄 NT_BUT_FOR_ANALYSIS.md

> │      ├── 📄 NT_Master_Strategy_Canvas.canvas

> │      ├── 📄 NT_PROCEDURAL_FAILURE_MAP.md

> │      ├── 📄 NT_REASONABLE_ACCOMMODATIONS.md

> │      ├── 📄 NT_REVERSAL_PATHS.md

> │      ├── 📄 NT_STATUS_TRACKER.md

> │      ├── 📄 NT_STAY_PATHS.md

> │      ├── 📄 NT_integrate_disability_separate_appe.m4a

> │      ├── 📄 OR_void_judgment_eviction_crisis.pdf

> │      ├── 📄 PL_DOJ_COMPLAINT.md

> │      ├── 📄 PL_ICRC_COMPLAINT.md

> │      ├── 📄 PL_Proposal for Strategic Reports in the Matter of.md

> │      ├── 📄 Strategic_Plan.canvas

> │    └── 📂 60_data_inventories/

> │      ├── 📄 NT_Violation_Index.md

> │      ├── 📄 NT_foreclosure-and-housing-litigation-case-record.csv

> │      ├── 📄 NT_inventory-of-civil-and-fair-housing-rights-vio.csv

> │    ├── 📄 NT_01_MASTER_INDEX.md

> │    ├── 📄 _C_VIS.md

> │    ├── 📄 vis.yaml

> │  ├── 📄 Case_Data.base

> │  └── 📂 D_PHASES/

> │    └── 📂 100_post_judgment_and_federal/

> │      └── 📂 10_motions/

> │        └── 📂 10_claims_motions/

> │          ├── 📄 40_claims_motions.md

> │          ├── 📄 MO_40_claims_motions.md

> │          └── 📂 Supplemental/

> │            └── 📂 01_drafts/

> │              ├── 📄 MO__Supplemental_Emergency_Motion.pdf

> │            └── 📂 02_exhibits/

> │              ├── 📄 EXH_02_exhibits.md

> │              ├── 📄 EXH__20_exhibits_combined_source

> │              ├── 📄 EXH__Exhibit_H_Declaration.pdf

> │            └── 📂 04_filed_receipts/

> │              ├── 📄 NT__Odyssey_Envelope_Receipt.pdf

> │          └── 📂 filings/

> │            └── 📂 10_2025-12-10_motion_vacate/

> │              └── 📂 01_drafts/

> │                ├── 📄 MO_Emergency Motions.docx

> │              └── 📂 02_exhibits/

> │                ├── 📄 EXH_02_exhibits.md

> │                ├── 📄 EXH_05_Exhibit_List.pdf

> │                ├── 📄 EXH_06_Exhibits_Combined.pdf

> │                ├── 📄 MO_01_motion_vacate.pdf

> │                ├── 📄 MO_02_emergency_motion_quash_stay.pdf

> │                ├── 📄 NT_combinepdf.pdf

> │                ├── 📄 OR_03_order_vacate_proposed.pdf

> │                ├── 📄 OR_04_order_stay_writ_proposed.pdf

> │              └── 📂 03_proposed_order/

> │                ├── 📄 OR_03_proposed_order.md

> │                ├── 📄 OR_Proposed_Order_Vacate.docx

> │              └── 📂 04_filed_receipts/

> │                ├── 📄 NT_Odyssey_Envelope_Receipt.pdf

> │              ├── 📄 MO_10_2025-12-10_motion_vacate.md

> │            └── 📂 20_2025-12-11_Supplemental_Emergency_Motion_Access/

> │              └── 📂 01_drafts/

> │                ├── 📄 MO_Supplemental_Emergency_Motion.pdf

> │              └── 📂 02_exhibits/

> │                ├── 📄 EXH_02_exhibits.md

> │                ├── 📄 EXH_20_exhibits_combined_source

> │                ├── 📄 EXH_Exhibit_H_Declaration.pdf

> │              └── 📂 04_filed_receipts/

> │                ├── 📄 NT_Odyssey_Envelope_Receipt.pdf

> │              ├── 📄 MO_20_2025-12-11_Supplemental_Emergency_Motion_Access.md

> │            └── 📂 30_draft_motions/

> │              ├── 📄 10_draft_motions.md

> │              ├── 📄 20_draft_motions.md

> │              ├── 📄 MO_10_draft_motions.md

> │              ├── 📄 MO_DRAFT_MOTION_VACATE.md

> │              ├── 📄 MO__Motions.md

> │              ├── 📄 MO__motion_emergency_stay_of_writ.md

> │              ├── 📄 MO__motion_emergency_supplemental_motio.md

> │              ├── 📄 MO__motion_to_vacate_void_judgment.md

> │              ├── 📄 MO_motion_emergency_stay_of_writ.md

> │              ├── 📄 MO_motion_emergency_supplemental_motion_ongoing_ha.md

> │              ├── 📄 MO_motion_to_vacate_void_judgment.md

> │              ├── 📄 MO_wc2.00.010__motion_emergency_stay_of_writ.docx

> │              ├── 📄 MO_wc2.00.010__motion_emergency_supplemental_mot.docx

> │              ├── 📄 MO_wc2.00.010__motion_to_vacate_void_judgement.docx

> │              ├── 📄 NT_DRAFT_EMERGENCY_STAY.md

> │              ├── 📄 NT_DRAFT_SUPPLEMENTAL.md

> │              ├── 📄 NT_EMERGENCY_FILING_PACKET.md

> │              ├── 📄 _README.md

> │              └── 📂 motions/

> │                ├── 📄 MO_01B_Motion_To_Vacate_Void_Judgment.pdf

> │                ├── 📄 MO_C2.01.002_motion_vacate.pdf

> │                ├── 📄 MO_C2.02.002_Emergency_Motion_Stay_OR_Quash.pdf

> │                ├── 📄 MO_C2.03.002_Supplemental_Emergency_Motion.pdf

> │                ├── 📄 MO_motions.md

> │          └── 📂 motion_vacate/

> │            └── 📂 01_drafts/

> │              ├── 📄 MO__Emergency Motions.docx

> │            └── 📂 02_exhibits/

> │              ├── 📄 EXH_02_exhibits.md

> │              ├── 📄 EXH__05_Exhibit_List.pdf

> │              ├── 📄 EXH__06_Exhibits_Combined.pdf

> │              ├── 📄 MO__01_motion_vacate.pdf

> │              ├── 📄 MO__02_emergency_motion_quash_stay.pdf

> │              ├── 📄 NT__combinepdf.pdf

> │              ├── 📄 OR__03_order_vacate_proposed.pdf

> │              ├── 📄 OR__04_order_stay_writ_proposed.pdf

> │            └── 📂 03_proposed_order/

> │              ├── 📄 OR_03_proposed_order.md

> │              ├── 📄 OR__Proposed_Order_Vacate.docx

> │            └── 📂 04_filed_receipts/

> │              ├── 📄 NT__Odyssey_Envelope_Receipt.pdf

> │            ├── 📄 MO_motion_vacate.md

> │            ├── 📄 NT.gitkeep

> │        ├── 📄 MO_10_motions.md

> │        ├── 📄 NT_index.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_orders/

> │        └── 📂 10_proposed_orders/

> │          ├── 📄 20_proposed_orders.md

> │          ├── 📄 MO__proposed_order_motion_to_vacate.md

> │          ├── 📄 MO_proposed_order_motion_to_vacate.md

> │          ├── 📄 NT__index.md

> │          ├── 📄 OR_20_proposed_orders.md

> │          ├── 📄 OR_DRAFT_ORDER_STAY.md

> │          ├── 📄 OR_DRAFT_ORDER_VACATE.md

> │          ├── 📄 OR__Proposed_Orders.md

> │          ├── 📄 OR__proposed_order_emergency_stay.md

> │          ├── 📄 OR_proposed_order_emergency_stay.md

> │          ├── 📄 _README.md

> │        ├── 📄 NT_index.md

> │        ├── 📄 OR_20_orders.md

> │        ├── 📄 _placeholder.md

> │        └── 📂 orders/

> │          ├── 📄 OR_C2.04.001_order_vacate_proposed.pdf

> │          ├── 📄 OR_C2.04.002_order_stay_writ_proposed.pdf

> │          ├── 📄 OR_orders.md

> │      └── 📂 30_regulatory_complaints/

> │        ├── 📄 PL_30_regulatory_complaints.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_federal_preservation/

> │        ├── 📄 _placeholder.md

> │      ├── 📄 OR_90_post_judgment_and_federal.md

> │      ├── 📄 _README.md

> │    └── 📂 10_inbox_working/

> │      ├── 📄 NT_00_inbox_working.md

> │      ├── 📄 NT_index.md

> │      └── 📂 _staging/

> │        └── 📂 _dupes_hold/

> │          ├── 📄 MO__motion_emergency_stay_of_writ (2).docx

> │          ├── 📄 MO__motion_emergency_supplemental_mot (2).docx

> │          ├── 📄 MO__motion_to_vacate_void_judgement (2).docx

> │          ├── 📄 NT_2025-12-15_they_threw_us_into_the_cold (2).md

> │          ├── 📄 NT_Donations_Context (2).md

> │          ├── 📄 NT_Long_Term_Payout_Strategy (2).md

> │          ├── 📄 NT_Master_Timeline (2).md

> │          ├── 📄 NT_Premonitions_I_Knew_Before_I_Knew (2).md

> │          ├── 📄 NT_Public_Statement (2).md

> │          ├── 📄 NT_Session_Summary_2025-12-15_i_knew_before_i_knew (2).md

> │          ├── 📄 NT_index.md

> │          ├── 📄 OR_c2.04.001_order_vacate_proposed (2).pdf

> │          ├── 📄 OR_c2.04.002_order_stay_writ_proposed (2).pdf

> │          ├── 📄 PL_Cold_Risk_Report (2).md

> │        └── 📂 _html_hold/

> │          ├── 📄 NT_index.md

> │      └── 📂 evidence_staging/

> │        └── 📂 exhibit_candidates/

> │          └── 📂 10_exposure_and_harm/

> │            ├── 📄 02_exposure_and_harm.md

> │            ├── 📄 NT_02_exposure_and_harm.md

> │            ├── 📄 PL_wi8.02.050__cold_risk_report.html

> │            └── 📂 photos_conditions/

> │            └── 📂 weather_reports/

> │              ├── 📄 PL_weather_reports.md

> │          ├── 📄 EXH_exhibit_candidates.md

> │        └── 📂 potential_exhibits/

> │          ├── 📄 EXH_potential_exhibits.md

> │    └── 📂 20_pre_foreclosure/

> │      └── 📂 10_account_history/

> │        ├── 📄 NT_index.md

> │        ├── 📄 NT_one_pager_overview.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_hardship_and_ada/

> │        ├── 📄 _placeholder.md

> │      └── 📂 30_communications/

> │        ├── 📄 NT_index.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_payments_and_disputes/

> │        ├── 📄 _placeholder.md

> │      ├── 📄 NT_10_pre_foreclosure.md

> │      ├── 📄 _README.md

> │    └── 📂 30_foreclosure_filing/

> │      └── 📂 10_complaint/

> │        ├── 📄 PL_10_complaint.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_summons/

> │        ├── 📄 PL_20_summons.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 30_lien_parties/

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_docket_snapshots/

> │        └── 📂 10_docket_map_and_notes/

> │        ├── 📄 NT_01_Docket.md

> │        ├── 📄 NT__Case_Summary.md

> │        ├── 📄 NT_docket_index.md

> │        ├── 📄 _Case_Summary.md

> │        ├── 📄 _README.md

> │        ├── 📄 _docket.md

> │        ├── 📄 _placeholder.md

> │        └── 📂 docket_files/

> │      ├── 📄 NT_20_foreclosure_filing.md

> │      ├── 📄 _README.md

> │    └── 📂 40_service_and_notice/

> │      └── 📂 10_sheriff_returns/

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_mailings/

> │        ├── 📄 _placeholder.md

> │      └── 📂 30_affidavits_of_service/

> │        └── 📂 10_jurisdiction_service_tr_4_1_b/

> │          ├── 📄 20_jurisdiction_service_tr_4_1_b.md

> │          ├── 📄 NT_20_jurisdiction_service_tr_4_1_b 1.md

> │          ├── 📄 NT_20_jurisdiction_service_tr_4_1_b.md

> │        └── 📂 20_service_process/

> │          ├── 📄 30_service_process.md

> │        ├── 📄 NT_03_Service_Process.md

> │        ├── 📄 NT_service_defects_analysis.md

> │        ├── 📄 PL_30_affidavits_of_service.md

> │        ├── 📄 PL_affidavits_service.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_defects_and_contradictions/

> │        ├── 📄 _placeholder.md

> │      ├── 📄 PL_30_service_and_notice.md

> │      ├── 📄 _README.md

> │    └── 📂 50_default_and_judgment/

> │      └── 📂 10_default_motion/

> │        ├── 📄 MO_10_default_motion.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_default_order/

> │        ├── 📄 OR_20_default_order.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 30_judgment_and_decree/

> │        ├── 📄 OR_30_judgment_and_decree.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_accounting_inputs/

> │        ├── 📄 _placeholder.md

> │      ├── 📄 OR_40_default_and_judgment.md

> │      ├── 📄 _README.md

> │    └── 📂 60_sale_and_title/

> │      └── 📂 10_sheriff_sale/

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_deed/

> │        ├── 📄 _placeholder.md

> │      └── 📂 30_recording_gaps/

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_possession_claims/

> │        └── 📂 10_sale_and_possession/

> │          ├── 📄 30_sale_and_possession.md

> │          ├── 📄 NT_30_sale_and_possession.md

> │        └── 📂 30_void_vs_voidable/

> │          ├── 📄 20_void_vs_voidable.md

> │          ├── 📄 NT_30_void_vs_voidable_tr_60b 1.md

> │          ├── 📄 NT_30_void_vs_voidable_tr_60b.md

> │        ├── 📄 NT_05_Sale_and_Possesion.md

> │        ├── 📄 NT_possession_admissions.md

> │        ├── 📄 _placeholder.md

> │      ├── 📄 NT_50_sale_and_title.md

> │      ├── 📄 _README.md

> │    └── 📂 70_writ_and_execution/

> │      └── 📂 10_writ_petition/

> │        ├── 📄 PL_10_writ_petition.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_writ_order/

> │        ├── 📄 OR_20_writ_order.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 30_execution_events/

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_notice_failures/

> │        ├── 📄 PL_40_notice_failures.md

> │        ├── 📄 _placeholder.md

> │      ├── 📄 NT_60_writ_and_execution.md

> │      ├── 📄 _README.md

> │    └── 📂 80_post_removal_conduct/

> │      └── 📂 10_property_interference/

> │        ├── 📄 _placeholder.md

> │      └── 📂 20_access_denial/

> │        ├── 📄 _placeholder.md

> │      └── 📂 30_spoliation_risk/

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_third_party_actions/

> │        ├── 📄 _placeholder.md

> │      ├── 📄 NT_70_post_removal_conduct.md

> │      ├── 📄 _README.md

> │    └── 📂 90_damages_and_fallout/

> │      └── 📂 10_property_possession_harms/

> │        ├── 📄 03_property_possession_harms.md

> │        ├── 📄 NT_03_property_possession_harms.md

> │      └── 📂 20_economic_harm/

> │        ├── 📄 10_economic_harm.md

> │        ├── 📄 NT_10_economic_harm.md

> │        ├── 📄 NT_index.md

> │      └── 📂 30_financial/

> │        ├── 📄 20_financial.md

> │        ├── 📄 NT_10_financial.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 40_health_and_safety/

> │        ├── 📄 30_health_and_safety.md

> │        ├── 📄 NT_20_health_and_safety.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 50_non_economic_harm/

> │        ├── 📄 40_non_economic_harm.md

> │        ├── 📄 NT_20_non_economic_harm.md

> │        └── 📂 cold_exposure/

> │          ├── 📄 NT_index.md

> │      └── 📂 60_professional_harm/

> │        ├── 📄 50_professional_harm.md

> │        ├── 📄 NT_30_professional_harm.md

> │        ├── 📄 _placeholder.md

> │      └── 📂 70_remedies_scenarios/

> │        ├── 📄 60_remedies_scenarios.md

> │        ├── 📄 NT_30_remedies_scenarios.md

> │        ├── 📄 NT_index.md

> │      └── 📂 80_payout_strategy/

> │        ├── 📄 70_payout_strategy.md

> │        ├── 📄 NT_40_Payout_Strategy.md

> │        ├── 📄 NT__Long_Term_Payout_Strategy.md

> │        ├── 📄 NT_index.md

> │        ├── 📄 _README.md

> │        └── 📂 payout_strategy/

> │      └── 📂 90_third_party_harm/

> │        ├── 📄 80_third_party_harm.md

> │        ├── 📄 NT_40_third_party_harm.md

> │        ├── 📄 _placeholder.md

> │      ├── 📄 NT_06_damages_and_remedies.md

> │      ├── 📄 NT_80_damages_and_fallout.md

> │      ├── 📄 NT_index.md

> │      └── 📂 Photos_Conditions/

> │      └── 📂 Weather_Reports/

> │        ├── 📄 PL_Weather_Reports.md

> │      ├── 📄 _README.md

> │      └── 📂 economic/

> │        ├── 📄 NT_ECONOMIC_HARM.md

> │      └── 📂 non-economic/

> │        ├── 📄 NT_NON_ECONOMIC_HARM.md

> │        └── 📂 cold-exposure/

> │          ├── 📄 PL__Cold_Risk_Report.md

> │      └── 📂 personal_narrative/

> │        └── 📂 10_Public_Narrative/

> │          ├── 📄 01_Public_Narrative.md

> │          ├── 📄 NT_01_Public_Narrative.md

> │          ├── 📄 NT_2025-12-15_they_threw_us_into_the_cold.md

> │          ├── 📄 NT_Public_Statement.md

> │          ├── 📄 _README.md

> │        └── 📂 20_Exposure_and_Harm/

> │          ├── 📄 02_Exposure_and_Harm.md

> │          ├── 📄 NT_02_Exposure_and_Harm.md

> │          ├── 📄 PL_Cold_Risk_Report.md

> │          └── 📂 Photos_Conditions/

> │          └── 📂 Weather_Reports/

> │            ├── 📄 PL_Weather_Reports.md

> │          ├── 📄 _README.md

> │        └── 📂 30_Internal_Analysis/

> │          ├── 📄 03_Internal_Analysis.md

> │          ├── 📄 NT_03_Internal_Analysis.md

> │          ├── 📄 NT_Session_Summary_2025-12-15_i_knew_before_i_knew.md

> │          └── 📂 Payout_Strategy/

> │            ├── 📄 NT_Long_Term_Payout_Strategy.md

> │            ├── 📄 _README.md

> │          └── 📂 Premonitions/

> │            ├── 📄 NT_Premonitions_I_Knew_Before_I_Knew.md

> │            ├── 📄 _README.md

> │          ├── 📄 _README.md

> │        └── 📂 40_Donations_and_Support/

> │          ├── 📄 04_Donations_and_Support.md

> │          └── 📂 Donation_Page_HTML/

> │          ├── 📄 NT_04_Donations_and_Support.md

> │          ├── 📄 NT_Donations_Context.md

> │          └── 📂 Screenshots_Live_Page/

> │          ├── 📄 _README.md

> │        └── 📂 50_Timeline/

> │          ├── 📄 05_Timeline.md

> │          ├── 📄 NT_05_Timeline.md

> │          ├── 📄 NT_Master_Timeline.md

> │          ├── 📄 _README.md

> │        └── 📂 Premonitions/

> │          ├── 📄 NT__Premonitions_I_Knew_Before_I_Knew.md

> │          ├── 📄 _README.md

> │      └── 📂 settlement/

> │        ├── 📄 NT_SETTLEMENT_SCENARIOS.md

> │      └── 📂 thirdparty/

> │    ├── 📄 MO_Promotion_Checklist.md

> │    ├── 📄 Strategic_Plan.canvas

> │    ├── 📄 _D_PHASES.md

> │  └── 📂 E_OUTPUTS/

> │    └── 📂 10_binders/

> │      └── 📂 master_case_bible/

> │        ├── 📄 NT_binder_manifest.md

> │        └── 📂 _build/

> │          ├── 📄 NT_full_binder.md

> │          ├── 📄 NT_full_binder_snapshot.md

> │          ├── 📄 NT_master_case_bible.html

> │          ├── 📄 NT_temp_merged.md

> │        └── 📂 sections/

> │    └── 📂 20_filings/

> │    ├── 📄 _E_OUTPUTS.md

> │    └── 📂 _build_artifacts/

> │      ├── 📄 MO_wc2.00.001_draft_motion_vacate.html

> │      ├── 📄 MO_wc2.00.010___motions.html

> │      ├── 📄 MO_wc2.00.010__motion_emergency_stay_of_writ.html

> │      ├── 📄 MO_wc2.00.010__motion_emergency_supplemental_mot.html

> │      ├── 📄 MO_wc2.00.010__motion_to_vacate_void_judgment.html

> │      ├── 📄 MO_wc2.01.010__proposed_order_motion_to_vacate.html

> │      ├── 📄 NT_2025-12-15_they_threw_us_into_the_cold.html

> │      ├── 📄 NT_Summary - MyCase.html

> │      ├── 📄 NT_WI8.01.050__index.html

> │      ├── 📄 NT_WI8.02.050__index.html

> │      ├── 📄 NT_WI8.99.010__index_MOVED.html

> │      ├── 📄 NT_WZ9.00.050__index.html

> │      ├── 📄 NT_WZ9.00.050__index_MOVED.html

> │      ├── 📄 NT__index (2).html

> │      ├── 📄 NT__index.html

> │      ├── 📄 NT__index_MOVED.html

> │      ├── 📄 NT_donations_context.html

> │      ├── 📄 NT_index (2).html

> │      ├── 📄 NT_index (2)_MOVED.html

> │      ├── 📄 NT_index-content.html

> │      ├── 📄 NT_index-content_MOVED.html

> │      ├── 📄 NT_index.html

> │      ├── 📄 NT_index_MOVED.html

> │      ├── 📄 NT_long_term_payout_strategy.html

> │      ├── 📄 NT_master_timeline.html

> │      ├── 📄 NT_premonitions_i_knew_before_i_knew.html

> │      ├── 📄 NT_public_statement.html

> │      ├── 📄 NT_session_summary_2025-12-15_i_knew_before_i_kn.html

> │      ├── 📄 NT_strategic_plan.html

> │      ├── 📄 NT_wc2.00.002_draft_emergency_stay.html

> │      ├── 📄 NT_wc2.00.003_draft_supplemental.html

> │      ├── 📄 NT_wc2.01.010__index-content.html

> │      ├── 📄 NT_wc2.01.010__index.html

> │      ├── 📄 NT_wg6.01.003_status_tracker.html

> │      ├── 📄 NT_wi8.01.010__2025-12-15_they_threw_us_into_the.html

> │      ├── 📄 NT_wi8.01.050__index-content.html

> │      ├── 📄 NT_wi8.99.010__index-content.html

> │      ├── 📄 NT_wi8.99.010__index.html

> │      ├── 📄 NT_wi8.99.010__long_term_payout_strategy.html

> │      ├── 📄 NT_wi8.99.010__premonitions_i_knew_before_i_knew.html

> │      ├── 📄 NT_wi8.99.010__session_summary_2025-12-15_i_knew.html

> │      ├── 📄 OR_wc2.01.001_draft_order_vacate.html

> │      ├── 📄 OR_wc2.01.002_draft_order_stay.html

> │      ├── 📄 OR_wc2.01.010__proposed_order_emergency_stay.html

> │      ├── 📄 OR_wc2.01.010__proposed_orders.html

> │      ├── 📄 PL_cold_risk_report.html

> │      ├── 📄 PL_wg6.01.001_doj_complaint.html

> │      ├── 📄 PL_wg6.01.002_icrc_complaint.html

> │      ├── 📄 _readme.html

> │      ├── 📄 _readme_MOVED.html

> │    └── 📂 vis/

> │      └── 📂 1768577070/

> │        ├── 📄 claims_map.json

> │        ├── 📄 manifest.csv

> │        ├── 📄 manifest.json

> │        ├── 📄 search_index.json

> │        └── 📂 site/

> │          └── 📂 A_TIMELINE/

> │            └── 📂 2023/

> │              ├── 📄 index.html

> │            └── 📂 2024/

> │              ├── 📄 index.html

> │            └── 📂 2025/

> │              └── 📂 events/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 2026/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 B_EVIDENCE/

> │            └── 📂 10_evidence_admin/

> │              ├── 📄 index.html

> │            └── 📂 20_court_record/

> │              └── 📂 10_docket_files/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 30_primary/

> │              └── 📂 aes/

> │                ├── 📄 index.html

> │              └── 📂 fcfcu/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 40_supporting/

> │              └── 📂 docs/

> │                └── 📂 affidavits/

> │                  ├── 📄 index.html

> │                └── 📂 declarations/

> │                  ├── 📄 index.html

> │                └── 📂 receipts/

> │                  ├── 📄 index.html

> │                └── 📂 records/

> │                  ├── 📄 index.html

> │              ├── 📄 index.html

> │              └── 📂 multi-media/

> │                ├── 📄 index.html

> │              └── 📂 property/

> │                └── 📂 10_mortgage_history/

> │                  └── 📂 10_payments/

> │                    ├── 📄 index.html

> │                └── 📂 20_parcel/

> │                  ├── 📄 index.html

> │            └── 📂 50_quarantine_candidates/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 C_VIS/

> │            └── 📂 10_violations/

> │              ├── 📄 index.html

> │            └── 📂 20_theories/

> │              ├── 📄 index.html

> │            └── 📂 30_legal_research/

> │              ├── 📄 index.html

> │            └── 📂 40_analysis/

> │              ├── 📄 index.html

> │            └── 📂 50_strategies/

> │              ├── 📄 index.html

> │            └── 📂 60_data_inventories/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 D_PHASES/

> │            └── 📂 100_post_judgment_and_federal/

> │              └── 📂 10_motions/

> │                └── 📂 10_claims_motions/

> │                  └── 📂 Supplemental/

> │                    └── 📂 01_drafts/

> │                      ├── 📄 index.html

> │                    └── 📂 02_exhibits/

> │                      ├── 📄 index.html

> │                    └── 📂 04_filed_receipts/

> │                      ├── 📄 index.html

> │                  └── 📂 filings/

> │                    └── 📂 10_2025-12-10_motion_vacate/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 index.html

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 index.html

> │                      └── 📂 03_proposed_order/

> │                        ├── 📄 index.html

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 index.html

> │                      ├── 📄 index.html

> │                    └── 📂 20_2025-12-11_Supplemental_Emergency_Motion_Access/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 index.html

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 index.html

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 index.html

> │                      ├── 📄 index.html

> │                    └── 📂 30_draft_motions/

> │                      ├── 📄 index.html

> │                      └── 📂 motions/

> │                        ├── 📄 index.html

> │                  ├── 📄 index.html

> │                  └── 📂 motion_vacate/

> │                    └── 📂 01_drafts/

> │                      ├── 📄 index.html

> │                    └── 📂 02_exhibits/

> │                      ├── 📄 index.html

> │                    └── 📂 03_proposed_order/

> │                      ├── 📄 index.html

> │                    └── 📂 04_filed_receipts/

> │                      ├── 📄 index.html

> │                    ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 20_orders/

> │                └── 📂 10_proposed_orders/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │                └── 📂 orders/

> │                  ├── 📄 index.html

> │              └── 📂 30_regulatory_complaints/

> │                ├── 📄 index.html

> │              └── 📂 40_federal_preservation/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 10_inbox_working/

> │              └── 📂 _staging/

> │                └── 📂 _dupes_hold/

> │                  ├── 📄 index.html

> │                └── 📂 _html_hold/

> │                  ├── 📄 index.html

> │              └── 📂 evidence_staging/

> │                └── 📂 exhibit_candidates/

> │                  └── 📂 10_exposure_and_harm/

> │                    ├── 📄 index.html

> │                    └── 📂 weather_reports/

> │                      ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 potential_exhibits/

> │                  ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 20_pre_foreclosure/

> │              └── 📂 10_account_history/

> │                ├── 📄 index.html

> │              └── 📂 20_hardship_and_ada/

> │                ├── 📄 index.html

> │              └── 📂 30_communications/

> │                ├── 📄 index.html

> │              └── 📂 40_payments_and_disputes/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 30_foreclosure_filing/

> │              └── 📂 10_complaint/

> │                ├── 📄 index.html

> │              └── 📂 20_summons/

> │                ├── 📄 index.html

> │              └── 📂 30_lien_parties/

> │                ├── 📄 index.html

> │              └── 📂 40_docket_snapshots/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 40_service_and_notice/

> │              └── 📂 10_sheriff_returns/

> │                ├── 📄 index.html

> │              └── 📂 20_mailings/

> │                ├── 📄 index.html

> │              └── 📂 30_affidavits_of_service/

> │                └── 📂 10_jurisdiction_service_tr_4_1_b/

> │                  ├── 📄 index.html

> │                └── 📂 20_service_process/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 40_defects_and_contradictions/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 50_default_and_judgment/

> │              └── 📂 10_default_motion/

> │                ├── 📄 index.html

> │              └── 📂 20_default_order/

> │                ├── 📄 index.html

> │              └── 📂 30_judgment_and_decree/

> │                ├── 📄 index.html

> │              └── 📂 40_accounting_inputs/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 60_sale_and_title/

> │              └── 📂 10_sheriff_sale/

> │                ├── 📄 index.html

> │              └── 📂 20_deed/

> │                ├── 📄 index.html

> │              └── 📂 30_recording_gaps/

> │                ├── 📄 index.html

> │              └── 📂 40_possession_claims/

> │                └── 📂 10_sale_and_possession/

> │                  ├── 📄 index.html

> │                └── 📂 30_void_vs_voidable/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 70_writ_and_execution/

> │              └── 📂 10_writ_petition/

> │                ├── 📄 index.html

> │              └── 📂 20_writ_order/

> │                ├── 📄 index.html

> │              └── 📂 30_execution_events/

> │                ├── 📄 index.html

> │              └── 📂 40_notice_failures/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 80_post_removal_conduct/

> │              └── 📂 10_property_interference/

> │                ├── 📄 index.html

> │              └── 📂 20_access_denial/

> │                ├── 📄 index.html

> │              └── 📂 30_spoliation_risk/

> │                ├── 📄 index.html

> │              └── 📂 40_third_party_actions/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 90_damages_and_fallout/

> │              └── 📂 10_property_possession_harms/

> │                ├── 📄 index.html

> │              └── 📂 20_economic_harm/

> │                ├── 📄 index.html

> │              └── 📂 30_financial/

> │                ├── 📄 index.html

> │              └── 📂 40_health_and_safety/

> │                ├── 📄 index.html

> │              └── 📂 50_non_economic_harm/

> │                └── 📂 cold_exposure/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 60_professional_harm/

> │                ├── 📄 index.html

> │              └── 📂 70_remedies_scenarios/

> │                ├── 📄 index.html

> │              └── 📂 80_payout_strategy/

> │                ├── 📄 index.html

> │              └── 📂 90_third_party_harm/

> │                ├── 📄 index.html

> │              └── 📂 Weather_Reports/

> │                ├── 📄 index.html

> │              └── 📂 economic/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │              └── 📂 non-economic/

> │                └── 📂 cold-exposure/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 personal_narrative/

> │                └── 📂 10_Public_Narrative/

> │                  ├── 📄 index.html

> │                └── 📂 20_Exposure_and_Harm/

> │                  └── 📂 Weather_Reports/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 30_Internal_Analysis/

> │                  └── 📂 Payout_Strategy/

> │                    ├── 📄 index.html

> │                  └── 📂 Premonitions/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 40_Donations_and_Support/

> │                  ├── 📄 index.html

> │                └── 📂 50_Timeline/

> │                  ├── 📄 index.html

> │                └── 📂 Premonitions/

> │                  ├── 📄 index.html

> │              └── 📂 settlement/

> │                ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 E_OUTPUTS/

> │            └── 📂 10_binders/

> │              └── 📂 master_case_bible/

> │                └── 📂 _build/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │            └── 📂 _build_artifacts/

> │              ├── 📄 index.html

> │          └── 📂 _ADMIN/

> │            └── 📂 10_index/

> │              ├── 📄 index.html

> │            └── 📂 20_case_logs/

> │              ├── 📄 index.html

> │            └── 📂 30_financial/

> │              ├── 📄 index.html

> │            └── 📂 40_overviews/

> │              └── 📂 10_maps/

> │                ├── 📄 index.html

> │              └── 📂 20_deep_dives/

> │                ├── 📄 index.html

> │              └── 📂 40_debates/

> │                ├── 📄 index.html

> │              └── 📂 50_explainers/

> │                ├── 📄 index.html

> │              └── 📂 60_infographics/

> │                ├── 📄 index.html

> │              └── 📂 70_reports/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 50_protocols/

> │              ├── 📄 index.html

> │            └── 📂 70_templates/

> │              └── 📂 10_motions/

> │                ├── 📄 index.html

> │              └── 📂 20_declarations/

> │                ├── 📄 index.html

> │              └── 📂 30_exhibits/

> │                ├── 📄 index.html

> │              └── 📂 40_orders/

> │                ├── 📄 index.html

> │              └── 📂 50_internal/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 80_integrity_tooling/

> │              ├── 📄 index.html

> │            └── 📂 90_pack_blueprints/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          ├── 📄 index.html

> │      └── 📂 1768577706/

> │        └── 📂 site/

> │      └── 📂 1768577894/

> │        └── 📂 site/

> │      └── 📂 1768578230/

> │        ├── 📄 claims_map.json

> │        ├── 📄 manifest.csv

> │        ├── 📄 manifest.json

> │        ├── 📄 search_index.json

> │        └── 📂 site/

> │          └── 📂 A_TIMELINE/

> │            └── 📂 2023/

> │              ├── 📄 index.html

> │            └── 📂 2024/

> │              ├── 📄 index.html

> │            └── 📂 2025/

> │              └── 📂 events/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 2026/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 B_EVIDENCE/

> │            └── 📂 10_evidence_admin/

> │              ├── 📄 index.html

> │            └── 📂 20_court_record/

> │              └── 📂 10_docket_files/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 30_primary/

> │              └── 📂 aes/

> │                ├── 📄 index.html

> │              └── 📂 fcfcu/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 40_supporting/

> │              └── 📂 docs/

> │                └── 📂 affidavits/

> │                  ├── 📄 index.html

> │                └── 📂 declarations/

> │                  ├── 📄 index.html

> │                └── 📂 receipts/

> │                  ├── 📄 index.html

> │                └── 📂 records/

> │                  ├── 📄 index.html

> │              ├── 📄 index.html

> │              └── 📂 multi-media/

> │                ├── 📄 index.html

> │              └── 📂 property/

> │                └── 📂 10_mortgage_history/

> │                  └── 📂 10_payments/

> │                    ├── 📄 index.html

> │                └── 📂 20_parcel/

> │                  ├── 📄 index.html

> │            └── 📂 50_quarantine_candidates/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 C_VIS/

> │            └── 📂 10_violations/

> │              ├── 📄 index.html

> │            └── 📂 20_theories/

> │              ├── 📄 index.html

> │            └── 📂 30_legal_research/

> │              ├── 📄 index.html

> │            └── 📂 40_analysis/

> │              ├── 📄 index.html

> │            └── 📂 50_strategies/

> │              ├── 📄 index.html

> │            └── 📂 60_data_inventories/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 D_PHASES/

> │            └── 📂 100_post_judgment_and_federal/

> │              └── 📂 10_motions/

> │                └── 📂 10_claims_motions/

> │                  └── 📂 Supplemental/

> │                    └── 📂 01_drafts/

> │                      ├── 📄 index.html

> │                    └── 📂 02_exhibits/

> │                      ├── 📄 index.html

> │                    └── 📂 04_filed_receipts/

> │                      ├── 📄 index.html

> │                  └── 📂 filings/

> │                    └── 📂 10_2025-12-10_motion_vacate/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 index.html

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 index.html

> │                      └── 📂 03_proposed_order/

> │                        ├── 📄 index.html

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 index.html

> │                      ├── 📄 index.html

> │                    └── 📂 20_2025-12-11_Supplemental_Emergency_Motion_Access/

> │                      └── 📂 01_drafts/

> │                        ├── 📄 index.html

> │                      └── 📂 02_exhibits/

> │                        ├── 📄 index.html

> │                      └── 📂 04_filed_receipts/

> │                        ├── 📄 index.html

> │                      ├── 📄 index.html

> │                    └── 📂 30_draft_motions/

> │                      ├── 📄 index.html

> │                      └── 📂 motions/

> │                        ├── 📄 index.html

> │                  ├── 📄 index.html

> │                  └── 📂 motion_vacate/

> │                    └── 📂 01_drafts/

> │                      ├── 📄 index.html

> │                    └── 📂 02_exhibits/

> │                      ├── 📄 index.html

> │                    └── 📂 03_proposed_order/

> │                      ├── 📄 index.html

> │                    └── 📂 04_filed_receipts/

> │                      ├── 📄 index.html

> │                    ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 20_orders/

> │                └── 📂 10_proposed_orders/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │                └── 📂 orders/

> │                  ├── 📄 index.html

> │              └── 📂 30_regulatory_complaints/

> │                ├── 📄 index.html

> │              └── 📂 40_federal_preservation/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 10_inbox_working/

> │              └── 📂 _staging/

> │                └── 📂 _dupes_hold/

> │                  ├── 📄 index.html

> │                └── 📂 _html_hold/

> │                  ├── 📄 index.html

> │              └── 📂 evidence_staging/

> │                └── 📂 exhibit_candidates/

> │                  └── 📂 10_exposure_and_harm/

> │                    ├── 📄 index.html

> │                    └── 📂 weather_reports/

> │                      ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 potential_exhibits/

> │                  ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 20_pre_foreclosure/

> │              └── 📂 10_account_history/

> │                ├── 📄 index.html

> │              └── 📂 20_hardship_and_ada/

> │                ├── 📄 index.html

> │              └── 📂 30_communications/

> │                ├── 📄 index.html

> │              └── 📂 40_payments_and_disputes/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 30_foreclosure_filing/

> │              └── 📂 10_complaint/

> │                ├── 📄 index.html

> │              └── 📂 20_summons/

> │                ├── 📄 index.html

> │              └── 📂 30_lien_parties/

> │                ├── 📄 index.html

> │              └── 📂 40_docket_snapshots/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 40_service_and_notice/

> │              └── 📂 10_sheriff_returns/

> │                ├── 📄 index.html

> │              └── 📂 20_mailings/

> │                ├── 📄 index.html

> │              └── 📂 30_affidavits_of_service/

> │                └── 📂 10_jurisdiction_service_tr_4_1_b/

> │                  ├── 📄 index.html

> │                └── 📂 20_service_process/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 40_defects_and_contradictions/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 50_default_and_judgment/

> │              └── 📂 10_default_motion/

> │                ├── 📄 index.html

> │              └── 📂 20_default_order/

> │                ├── 📄 index.html

> │              └── 📂 30_judgment_and_decree/

> │                ├── 📄 index.html

> │              └── 📂 40_accounting_inputs/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 60_sale_and_title/

> │              └── 📂 10_sheriff_sale/

> │                ├── 📄 index.html

> │              └── 📂 20_deed/

> │                ├── 📄 index.html

> │              └── 📂 30_recording_gaps/

> │                ├── 📄 index.html

> │              └── 📂 40_possession_claims/

> │                └── 📂 10_sale_and_possession/

> │                  ├── 📄 index.html

> │                └── 📂 30_void_vs_voidable/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 70_writ_and_execution/

> │              └── 📂 10_writ_petition/

> │                ├── 📄 index.html

> │              └── 📂 20_writ_order/

> │                ├── 📄 index.html

> │              └── 📂 30_execution_events/

> │                ├── 📄 index.html

> │              └── 📂 40_notice_failures/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 80_post_removal_conduct/

> │              └── 📂 10_property_interference/

> │                ├── 📄 index.html

> │              └── 📂 20_access_denial/

> │                ├── 📄 index.html

> │              └── 📂 30_spoliation_risk/

> │                ├── 📄 index.html

> │              └── 📂 40_third_party_actions/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 90_damages_and_fallout/

> │              └── 📂 10_property_possession_harms/

> │                ├── 📄 index.html

> │              └── 📂 20_economic_harm/

> │                ├── 📄 index.html

> │              └── 📂 30_financial/

> │                ├── 📄 index.html

> │              └── 📂 40_health_and_safety/

> │                ├── 📄 index.html

> │              └── 📂 50_non_economic_harm/

> │                └── 📂 cold_exposure/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 60_professional_harm/

> │                ├── 📄 index.html

> │              └── 📂 70_remedies_scenarios/

> │                ├── 📄 index.html

> │              └── 📂 80_payout_strategy/

> │                ├── 📄 index.html

> │              └── 📂 90_third_party_harm/

> │                ├── 📄 index.html

> │              └── 📂 Weather_Reports/

> │                ├── 📄 index.html

> │              └── 📂 economic/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │              └── 📂 non-economic/

> │                └── 📂 cold-exposure/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │              └── 📂 personal_narrative/

> │                └── 📂 10_Public_Narrative/

> │                  ├── 📄 index.html

> │                └── 📂 20_Exposure_and_Harm/

> │                  └── 📂 Weather_Reports/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 30_Internal_Analysis/

> │                  └── 📂 Payout_Strategy/

> │                    ├── 📄 index.html

> │                  └── 📂 Premonitions/

> │                    ├── 📄 index.html

> │                  ├── 📄 index.html

> │                └── 📂 40_Donations_and_Support/

> │                  ├── 📄 index.html

> │                └── 📂 50_Timeline/

> │                  ├── 📄 index.html

> │                └── 📂 Premonitions/

> │                  ├── 📄 index.html

> │              └── 📂 settlement/

> │                ├── 📄 index.html

> │            ├── 📄 index.html

> │          └── 📂 E_OUTPUTS/

> │            └── 📂 10_binders/

> │              └── 📂 master_case_bible/

> │                └── 📂 _build/

> │                  ├── 📄 index.html

> │                ├── 📄 index.html

> │            └── 📂 _build_artifacts/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │            └── 📂 vis/

> │              ├── 📄 index.html

> │          └── 📂 _ADMIN/

> │            └── 📂 10_index/

> │              ├── 📄 index.html

> │            └── 📂 20_case_logs/

> │              ├── 📄 index.html

> │            └── 📂 30_financial/

> │              ├── 📄 index.html

> │            └── 📂 40_overviews/

> │              └── 📂 10_maps/

> │                ├── 📄 index.html

> │              └── 📂 20_deep_dives/

> │                ├── 📄 index.html

> │              └── 📂 40_debates/

> │                ├── 📄 index.html

> │              └── 📂 50_explainers/

> │                ├── 📄 index.html

> │              └── 📂 60_infographics/

> │                ├── 📄 index.html

> │              └── 📂 70_reports/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 50_protocols/

> │              ├── 📄 index.html

> │            └── 📂 70_templates/

> │              └── 📂 10_motions/

> │                ├── 📄 index.html

> │              └── 📂 20_declarations/

> │                ├── 📄 index.html

> │              └── 📂 30_exhibits/

> │                ├── 📄 index.html

> │              └── 📂 40_orders/

> │                ├── 📄 index.html

> │              └── 📂 50_internal/

> │                ├── 📄 index.html

> │              ├── 📄 index.html

> │            └── 📂 80_integrity_tooling/

> │              ├── 📄 index.html

> │            └── 📂 90_pack_blueprints/

> │              ├── 📄 index.html

> │            ├── 📄 index.html

> │          ├── 📄 index.html

> │      ├── 📄 latest.txt

> │  ├── 📄 NT_README.md

> └── 📂 launcher/

> │  ├── 📄 main.py

> │  ├── 📄 requirements.txt

> │  ├── 📄 start.bat

> │  ├── 📄 styles.qss

> └── 📂 logs/

> │  └── 📂 migrations/

> │    ├── 📄 migration_log.csv

> │  └── 📂 sessions/

> │    ├── 📄 Session_Summary_2025-12-16_fcfcu_case_dna_str_1.md

> │    ├── 📄 Session_Summary_2025-12-16_fcfcu_case_dna_strat.md

> └── 📂 scripts/

> │  └── 📂 audit/

> │    ├── 📄 check_integrity.py

> │    ├── 📄 find_collisions.py

> │    ├── 📄 generate_audit_csv.py

> │    ├── 📄 scan_properties.py

> │  └── 📂 maintenance/

> │    ├── 📄 apply_audit_corrections.py

> │    ├── 📄 enforce_prefixes.py

> │    ├── 📄 repair_front_matter.py

> │    ├── 📄 resequence_folders.py

> │    ├── 📄 strip_legacy_ids.py

> │    ├── 📄 sync_csv_data.py

> │  └── 📂 vis/

> │    ├── 📄 README.md

> │    ├── 📄 lint_c_vis.py

> │    ├── 📄 run_vis.ps1

> │    ├── 📄 run_vis.sh

> │  └── 📂 vitepress/

> │    ├── 📄 build_and_serve.ps1

> │    ├── 📄 sync_vis_to_docs.ps1

> │    ├── 📄 sync_vis_to_docs.sh

> └── 📄 wrangler.toml

> ```

### User
> give me the updated documentation for this conversation

### Assistant
> Done. I’ve generated **updated, Receipt-Ready documentation** for this entire conversation and placed it in a clean, structured session summary in the canvas.
> 
> This document does four critical things for you:
> 
> 1. **Locks the architectural truth**
>    - `content/C_VIS` = immutable case data  
>    - VIS = read-only scanner/indexer  
>    - LegalMind = analysis, orchestration, reasoning layer
> 
> 2. **Confirms what is already working**
>    - VIS ran successfully
>    - Outputs exist and are valid
>    - MkDocs is explicitly out; VitePress / VIS HTML is in
> 
> 3. **Explains the confusion points clearly**
>    - Docker errors = PowerShell syntax, not system failure
>    - VIS does *not* belong inside case content
>    - Desktop launcher is optional, not foundational
> 
> 4. **Gives you a clean restart vector**
>    - Exact next tests to run
>    - What to ignore for now
>    - Where LegalMind testing should begin
> 
> ### What you should do next (no overthinking)
> If you want momentum **right now**, do this in order:
> 
> 1. Test **LegalMind API Gateway** (health endpoint)
> 2. Test **Agent-Orchestrator** reading existing VIS output
> 3. Ignore UI, ignore launcher polish, ignore refactors
> 
> If you want, next I can:
> - Write **PowerShell-safe Docker commands** (no bash nonsense)
> - Produce a **LegalMind smoke-test checklist**
> - Wire **VIS → LegalMind ingestion contract** (schema + adapter)
> - Or formally park the PyQt launcher as an experimental tool so it doesn’t pollute the core system
> 
> You’re not behind. The system is finally clean enough to move fast.
