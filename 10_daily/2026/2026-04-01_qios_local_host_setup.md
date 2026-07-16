---
layout: page
title: "QiOS Local Host Setup"
slug: "qios_local_host_setup"
created_at: "2026-04-01 16:18:07"
updated_at: "2026-07-16T06:49:31-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-005.json"
template_key: master-template
date: 2026-04-01
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69cd8b8c-a424-832b-9971-7995762b8f9b"
canonical_ref: ""
---

# QiOS Local Host Setup

## Overview
- **Date**: 2026-04-01 16:18:07
- **Conversation ID**: `69cd8b8c-a424-832b-9971-7995762b8f9b`
- **Source**: `Chat-Export-28513-2026/conversations-005.json`

## Chat History

### User
> ok now i am starting to run into this  server issue over and over, so we need a qios, blueprint aligned server on my pc that can handle actual and eventually all my server needs temporarily

### Assistant
> I’m grounding this against your blueprint first, then I’m going to turn it into a concrete local server shape you can actually run on the PC without fighting the architecture.

### Assistant
> I’ve got the shape now. The blueprint already gives you the bones; the missing piece is making it an actual stable local host instead of a pile of fragile dev processes.

### Assistant
> Yes. You need a **real local control server**, not a rotating mess of `pnpm dev`, Vite, random Python processes, and half-alive ports.
> 
> And no, the answer is **not** “make your PC the permanent everything server.”  
> For QiOS alignment, your PC should be the **local runtime + control plane**, while Supabase stays the canonical metadata/system-of-record layer. That split is already in your blueprint: local runtime handles file watcher, ingest, OCR, extraction, chunking, embeddings, and a local API; cloud handles canonical metadata, app APIs, and retrieval surfaces. fileciteturn2file1
> 
> # The clean answer
> 
> Build a **QiOS Local Host** on your PC with **one entrypoint** and **managed services** behind it.
> 
> ## What it should be
> 
> ### 1. Local gateway
> One local reverse proxy in front of everything.
> 
> Use this as the only public-facing thing on your machine:
> 
> - `http://qios.local` → landing/status
> - `http://admin.qios.local` → local admin UI
> - `http://api.qios.local` → FastAPI control plane
> - `http://portal.qios.local` → local QiOne portal build
> - `http://docs.qios.local` → local blueprint/docs preview
> 
> Why: stop hitting random ports directly. One gateway gives you stable routing, cleaner logs, fewer collisions, and one place to debug.
> 
> ### 2. Local control API
> This is the machine-local brainstem.
> 
> Your blueprint already calls for a **Local API** on the machine-local side, with endpoints like:
> 
> - `GET /status`
> - `POST /ingest`
> - `GET /queue`
> - `POST /retry/{archive_id}`
> - `GET /archive/{id}`
> 
> and it explicitly frames this as the engine-side control API for the local runtime. fileciteturn2file1
> 
> So don’t invent a new pattern. Use that.
> 
> ### 3. Worker services
> These should be separate long-running services, not stuffed into the web server.
> 
> Minimum set:
> 
> - file watcher
> - ingest worker
> - OCR/extraction worker
> - embedding worker
> - sync worker
> - retry/repair worker
> 
> That matches the blueprint’s local runtime + worker model and keeps failures visible/stateful/retryable instead of silently dying in one overloaded process. fileciteturn2file1turn2file2
> 
> ### 4. Built frontends, not dev servers
> For anything you use daily, stop depending on raw dev servers.
> 
> - Build React/Vite apps
> - Serve the built assets behind the gateway
> - Keep `vite dev` only for active feature work
> 
> Your admin surface in the blueprint is already described as a standalone local admin control plane tied to the FastAPI local server. fileciteturn2file1  
> That means the architecture wants a stable local admin surface, not a forever-dev server.
> 
> ---
> 
> # What this server should handle now
> 
> ## On the PC
> These belong local, per blueprint:
> 
> - file intake
> - queue inspection
> - OCR
> - extraction
> - chunking
> - embeddings
> - local logs
> - machine health
> - manual ingest/retry controls
> - local admin plane
> 
> The blueprint also gives you the expected working directory under `C:/QiData/` with `inbox`, `processing`, `reviewed`, `failed`, `manifests`, `extracted_text`, `embeddings_cache`, `logs`, and `model_cache`. fileciteturn2file1turn2file2
> 
> ## In Supabase / cloud
> These should **stay** there:
> 
> - canonical metadata
> - archive registration records
> - tenant/RBAC
> - app-facing domain data
> - pgvector-backed retrieval index
> - tenant-scoped portal data
> 
> That boundary is explicit in the blueprint. Local writes upward; cloud serves app surfaces. fileciteturn2file1
> 
> ---
> 
> # What not to do
> 
> ## Do not make one giant monolith
> Bad move.
> 
> If one Python app is doing:
> - gateway
> - API
> - workers
> - websockets
> - ingestion
> - embeddings
> - file watching
> - admin rendering
> 
> then one crash takes down everything and debugging turns into hell.
> 
> ## Do not let frontends write directly to `qiarchive`
> The blueprint is blunt here: frontend/app/integration writes must not bypass the pipeline. Archive record state is pipeline-owned. fileciteturn2file1
> 
> ## Do not keep using raw Vite as “the server”
> That is dev tooling, not stable local infrastructure.
> 
> ## Do not blur local runtime and canonical backend
> Your blueprint already corrected that confusion. The canonical backend is Supabase-based, not “whatever happens to be running on the PC today.” fileciteturn2file1
> 
> ---
> 
> # The server shape I recommend
> 
> ## A. Gateway layer
> Use a reverse proxy as the single entrypoint.
> 
> Role:
> - route subdomains
> - terminate local HTTP
> - standardize logs
> - hide port sprawl
> - optionally expose selected services through tunnel later
> 
> ## B. Service manager layer
> You need supervised processes, not hand-started terminals.
> 
> Use a service manager so these restart automatically:
> 
> - `qios-api`
> - `qios-watcher`
> - `qios-ingest-worker`
> - `qios-embed-worker`
> - `qios-sync-worker`
> - `qios-admin-ui`
> - `qios-portal-local`
> 
> ## C. Runtime layer
> Split by responsibility:
> 
> ### `python_local/api`
> - FastAPI control plane
> - status, queue, retry, ingest, archive lookup
> 
> ### `python_local/file_pipeline`
> - watcher
> - scanner
> - normalization
> - ingest orchestration
> 
> ### `python_local/services`
> - OCR
> - parsing
> - embedding
> - metadata enrichment
> 
> ### `python_local/jobs`
> - retry
> - scheduled sync
> - cleanup
> - health audits
> 
> That lines up with the blueprint’s recommended local Python shape and the open decision to lock `python_local/file_pipeline` and local API endpoints. fileciteturn2file0turn2file1
> 
> ## D. UI layer
> - `admin.qios.local` → local admin control plane
> - `portal.qios.local` → local QiOne preview/build
> - `docs.qios.local` → blueprint/docs preview
> - `status.qios.local` → machine + queue + dependency health
> 
> ---
> 
> # Minimal local topology
> 
> ```text
> [ Browser ]
>     |
>     v
> [ Local Gateway / Reverse Proxy ]
>     |---- admin.qios.local  -> Admin UI (built React)
>     |---- api.qios.local    -> FastAPI Local Control API
>     |---- portal.qios.local -> QiOne local build
>     |---- docs.qios.local   -> MkDocs / static docs
>     |
>     v
> [ Service Manager ]
>     |---- qios-api
>     |---- qios-watcher
>     |---- qios-ingest
>     |---- qios-embed
>     |---- qios-sync
>     |
>     v
> [ C:/QiData/* ]  <->  [ Supabase ]
> ```
> 
> ---
> 
> # The blunt truth about your recurring “server issue”
> 
> You likely do **not** have a “server problem.”  
> You have a **process topology problem**.
> 
> Symptoms usually look like:
> - ports stepping on each other
> - dev servers dying silently
> - Python env drift
> - frontend expecting local backend shape that changed
> - services starting in the wrong order
> - local state scattered across repo folders instead of one runtime root
> - random manual startups with no restart policy
> 
> The fix is not more debugging inside the same chaos.  
> The fix is **one gateway, supervised services, one local data root, one control API, one health dashboard**.
> 
> ---
> 
> # What to lock into the blueprint next
> 
> You asked for blueprint alignment, so here’s the exact doctrine move:
> 
> ## Add a new named concept
> **QiOS Local Host**  
> A machine-local service plane that implements the blueprint’s local runtime and local admin control plane.
> 
> ## It should define
> - one gateway
> - one control API
> - supervised workers
> - one local runtime root (`C:/QiData`)
> - stable local hostnames
> - local-only admin exposure
> - strict separation from canonical cloud metadata
> 
> ## It should not define
> - permanent replacement for Supabase
> - direct frontend writes to `qiarchive`
> - public exposure of admin/control plane
> - ad hoc ports as architectural surface
> 
> ---
> 
> # My recommendation stack
> 
> Not brand-hype. Just practical.
> 
> ## Best fit
> - **Reverse proxy:** Caddy
> - **Local API:** FastAPI
> - **Workers:** Python services
> - **Frontend serving:** built static assets behind gateway
> - **Process supervision:** Windows service manager
> - **Canonical backend:** Supabase
> - **Queue/cache later if needed:** Redis
> - **Graph later if needed:** Neo4j
> 
> Why this fits:
> - matches your existing FastAPI + React direction
> - matches local/cloud boundary in blueprint
> - avoids Docker-everything overhead unless you actually need it
> - lets you stabilize fast without redesigning QiOS
> 
> ---
> 
> # Priority order
> 
> ## Phase 1 — stop the bleeding
> Do this first.
> 
> 1. Create one local gateway
> 2. Standardize hostnames
> 3. Move all local state under `C:/QiData`
> 4. Run FastAPI as the only local control API
> 5. Put workers under supervision
> 6. Build admin UI and serve it stably
> 
> ## Phase 2 — make it QiOS-clean
> 1. Lock local API contract
> 2. Lock worker contracts
> 3. Lock service startup order
> 4. Lock health checks
> 5. Lock structured logs
> 
> ## Phase 3 — make it future-capable
> 1. Add queue broker if needed
> 2. Add tunnel only for selected services
> 3. Add local auth guard for admin
> 4. Add service dashboard
> 5. Add deployment scripts
> 
> ---
> 
> # Decision
> 
> **Yes: build the local server.**  
> But build it as a **QiOS Local Host / Local Control Plane**, not as “my PC becomes one giant app server.”
> 
> That is the blueprint-aligned move. The blueprint already expects:
> - local runtime,
> - local API,
> - local admin control plane,
> - `C:/QiData` working root,
> - visible and retryable pipeline states,
> - and a strict split between local processing and canonical cloud truth. fileciteturn2file0turn2file1turn2file2
> 
> If you want, next I’ll turn this into the **actual blueprint patch text** with sections, naming, and a concrete local server tree you can drop straight into QiOS.

### User
> lets do it, and we have tailscale if we need that later.

### Assistant
> I’m pulling the exact blueprint anchors now so I can write the patch clean instead of hand-waving it. After that I’ll give you the insert-ready doctrine text and the repo/runtime shape.

### Assistant
> Good. Tailscale stays in the design as an **access overlay later**, not as the runtime itself. The runtime is still **PC local host + Supabase canonical backend**. Tailscale only becomes the private door into that local host when you want remote access. That keeps you aligned with the existing local/cloud split, the local control API, the `C:/QiData` working root, the Local Admin Control Plane, and the rule that pipeline state stays visible/stateful/retryable. fileciteturn4file1 fileciteturn4file2 fileciteturn0file0
> 
> # Lock this decision
> 
> ## New architectural decision
> **QiOS Local Host** is the temporary machine-local server plane for Cody’s PC.
> 
> It is:
> - the stable local runtime for ingest, OCR, extraction, chunking, embeddings, sync, and operator controls
> - fronted by a single local gateway
> - backed by supervised local services
> - writing upward to Supabase as canonical metadata truth
> 
> It is not:
> - a replacement for Supabase
> - a public internet-facing admin server
> - a license to let frontends or tools bypass the pipeline and write raw archive state
> 
> That stays consistent with the blueprint’s current model: local runtime does watcher/ingest/OCR/extraction/chunking/embeddings/local API; cloud remains canonical metadata, retrieval, and app-facing surfaces. fileciteturn4file1 fileciteturn4file2
> 
> ---
> 
> # Best blueprint move
> 
> Your blueprint is too flat now. Split `05_compute` and `06_applications` one level deeper.
> 
> ## Recommended structure update
> 
> ```text
> 05_compute/
> ├── 00_index.md
> ├── 01_apis/
> │   ├── 010_local_apis.md
> │   ├── 020_app_apis.md
> │   ├── 030_integration_apis.md
> │   └── 040_worker_events.md
> ├── 02_pipelines/
> │   ├── 010_ingestion_pipeline.md
> │   ├── 020_pipeline_states.md
> │   └── 030_failure_retry.md
> ├── 03_workers/
> │   ├── 010_worker_model.md
> │   ├── 020_worker_registry.md
> │   └── 030_worker_supervision.md
> ├── 04_runtime/
> │   ├── 010_runtime_overview.md
> │   ├── 020_local_runtime.md
> │   ├── 030_cloud_runtime.md
> │   ├── 040_qios_local_host.md
> │   ├── 050_environment_variables.md
> │   └── 060_bootstrap_validation.md
> └── 05_integrations/
>     ├── 010_integrations_overview.md
>     └── 020_access_overlays.md
> 
> 06_applications/
> ├── 00_index.md
> ├── 01_web/
> │   └── 010_web_surface.md
> ├── 02_portal/
> │   ├── 010_portal_overview.md
> │   ├── 020_local_admin_control_plane.md
> │   └── 030_multi_tenant_portal.md
> ├── 03_admin/
> │   ├── 010_admin_surface.md
> │   └── 020_admin_guardrails.md
> ├── 04_interfaces/
> │   ├── 010_search_ui.md
> │   ├── 020_review_ui.md
> │   ├── 030_archive_ui.md
> │   └── 040_chatbot_ui.md
> └── 05_tools/
>     ├── 010_tools_overview.md
>     └── 020_cli_contract.md
> ```
> 
> This respects your “start another level down” requirement and keeps the runtime doctrine from being buried in one giant page.
> 
> ---
> 
> # Insert-ready blueprint patch
> 
> ## File: `05_compute/04_runtime/040_qios_local_host.md`
> 
> ```markdown
> # QiOS Local Host
> 
> ## Purpose
> QiOS Local Host is the machine-local server plane that runs on the operator/developer PC and provides a stable execution environment for local QiOS runtime responsibilities.
> 
> It exists to stop ad hoc development-server sprawl, reduce port collisions, centralize health visibility, and provide one consistent local control surface during local development and heavy compute periods.
> 
> QiOS Local Host is a runtime boundary implementation of the existing Local Runtime doctrine. It does not replace the canonical cloud backend.
> 
> ## Constitutional Fit
> QiOS Local Host exists because the blueprint already defines:
> 
> - Local runtime responsibilities: file watcher, ingest pipeline, OCR, extraction, chunking, embeddings, and local API
> - A machine-local working directory rooted at `C:/QiData/`
> - A Local Admin Control Plane with a FastAPI local server and a local admin UI
> - A hard local ↔ cloud boundary in which local runtime writes upward to cloud truth and never redefines canonical records
> 
> ## Primary Role
> QiOS Local Host is the temporary but real local server plane for:
> 
> - machine-local file intake
> - queue and pipeline control
> - OCR and extraction
> - deterministic chunking
> - local embeddings
> - retry and repair execution
> - sync orchestration
> - system status and operator controls
> - stable local routing for local surfaces
> 
> ## Non-Goals
> QiOS Local Host is not:
> 
> - the canonical metadata system of record
> - a replacement for Supabase
> - the public delivery surface
> - a justification for direct frontend writes into `qiarchive`
> - a monolithic “everything server”
> 
> ## Architectural Rule
> QiOS Local Host must remain subordinate to the existing QiOS runtime boundary:
> 
> - Local runtime performs machine-local processing
> - Cloud runtime remains canonical for metadata, retrieval, and app-facing serving
> - Derived layers remain non-canonical
> - Admin and pipeline controls must not be exposed publicly
> 
> ## Core Shape
> QiOS Local Host consists of four parts:
> 
> 1. Local Gateway
> 2. Local Control API
> 3. Supervised Local Workers
> 4. Local Operator Surfaces
> 
> ### 1. Local Gateway
> A single local reverse proxy must front all local services.
> 
> Purpose:
> - stable local hostnames
> - one entrypoint
> - unified routing
> - cleaner logs
> - less port chaos
> - easier future private remote access
> 
> Recommended local hostnames:
> - `qios.local`
> - `api.qios.local`
> - `admin.qios.local`
> - `portal.qios.local`
> - `docs.qios.local`
> 
> Direct use of raw ports is acceptable during active development, but host-based routing is the architectural target.
> 
> ### 2. Local Control API
> The Local Control API is the canonical machine-local control plane.
> 
> It must own:
> - machine health and readiness checks
> - queue visibility
> - ingest triggering
> - retry triggering
> - archive lookup
> - local path/config status
> 
> Minimum endpoint contract:
> - `GET /status`
> - `GET /queue`
> - `POST /ingest`
> - `POST /retry/{archive_id}`
> - `GET /archive/{id}`
> 
> The Local Control API must never redefine canonical records. It coordinates pipeline execution and state visibility only.
> 
> ### 3. Supervised Local Workers
> Workers running on the PC must be long-running supervised services, not ad hoc terminal sessions.
> 
> Minimum local worker categories:
> - file watcher
> - ingest orchestrator
> - OCR/extraction worker
> - embedding worker
> - retry/repair worker
> - sync worker
> 
> Each worker must:
> - have a stable worker slug
> - declare input and output shape
> - write visible state
> - write failure state
> - use canonical IDs where applicable
> - never bypass the pipeline contract
> 
> ### 4. Local Operator Surfaces
> QiOS Local Host may expose local operator surfaces behind the Local Gateway:
> 
> - local admin control plane
> - queue/system status screen
> - archive inspection UI
> - local docs/blueprint preview
> - local portal preview build
> 
> These surfaces are operator/developer tools, not public delivery surfaces.
> 
> ## Local Data Root
> QiOS Local Host must use one machine-local working root:
> 
> `C:/QiData/`
> 
> Minimum subdirectories:
> - `inbox/`
> - `processing/`
> - `reviewed/`
> - `failed/`
> - `manifests/`
> - `extracted_text/`
> - `embeddings_cache/`
> - `logs/`
> - `model_cache/`
> - `exports/` (non-canonical only)
> 
> No local service may invent an alternate hidden working root without explicit documentation.
> 
> ## Service Supervision Rule
> All long-running local services must be restartable and observable.
> 
> Minimum supervised service set:
> - `qios-gateway`
> - `qios-api`
> - `qios-watcher`
> - `qios-ingest`
> - `qios-extract`
> - `qios-embed`
> - `qios-retry`
> - `qios-sync`
> 
> Development servers may exist, but they are not the architectural runtime target.
> 
> ## Boundary Law
> QiOS Local Host may:
> - read and process local files
> - write metadata upward to canonical systems
> - trigger and monitor worker execution
> - provide operator visibility
> 
> QiOS Local Host may not:
> - become canonical truth for tenant/domain records
> - bypass Supabase Auth and platform identity rules
> - expose admin surfaces publicly
> - let app UIs write raw archive state outside the pipeline
> 
> ## Security Rule
> Local operator surfaces must be treated as privileged.
> 
> Requirements:
> - local-only by default
> - elevated-role access only
> - no public exposure by default
> - no service-role leakage into frontend code
> - sensitive logs stored locally and intentionally
> 
> ## Access Overlay Rule
> Private remote access may be added later through an access overlay such as Tailscale.
> 
> Access overlays are allowed only as transport and access mechanisms.
> They are not runtime replacements and do not change the local/cloud boundary.
> 
> If used, the overlay must:
> - front only approved local surfaces
> - avoid public exposure
> - preserve admin/operator-only access rules
> 
> ## Success Criteria
> QiOS Local Host is considered alive when:
> 
> - gateway resolves local hostnames correctly
> - Local Control API responds successfully
> - local worker supervision is active
> - `C:/QiData/` root is valid and healthy
> - a test file can enter `inbox/`, register through the pipeline, and appear in canonical archive state
> - admin/operator surfaces show live pipeline state
> 
> ## Failure Criteria
> QiOS Local Host is considered unhealthy when:
> 
> - workers require manual terminal babysitting
> - services are started from undocumented locations
> - raw ports are the only stable access pattern
> - local files are processed outside `C:/QiData/`
> - retries are not visible/stateful
> - frontend code bypasses the pipeline contract
> ```
> 
> ---
> 
> ## File: `06_applications/02_portal/020_local_admin_control_plane.md`
> 
> ```markdown
> # Local Admin Control Plane
> 
> ## Purpose
> The Local Admin Control Plane is the operator-facing local administration surface for QiOS Local Host.
> 
> It is used to:
> - orchestrate local workers
> - monitor queue state
> - validate runtime readiness
> - inspect pipeline failures
> - trigger manual ingest and retry flows
> - preview local system health during development and heavy compute periods
> 
> ## Position in the Stack
> The Local Admin Control Plane is a local operator surface.
> 
> It is:
> - not the public web
> - not the tenant portal
> - not canonical data storage
> - not a substitute for cloud app APIs
> 
> It sits on top of:
> - Local Gateway
> - Local Control API
> - supervised local workers
> - `C:/QiData/` runtime state
> 
> ## Minimum Capabilities
> The Local Admin Control Plane must show:
> 
> - system health
> - required environment variable status
> - required directory status
> - inbox queue state
> - ingest trigger control
> - retry trigger control
> - pipeline error visibility
> - worker status visibility
> 
> ## Source of Truth Rule
> The Local Admin Control Plane may display:
> - local runtime state
> - canonical archive state
> - job state
> - worker state
> 
> It may not invent shadow records or act as a second truth layer.
> 
> All state-changing actions must go through:
> - the Local Control API
> - the pipeline contract
> - canonical job and archive state tracking where applicable
> 
> ## Exposure Rule
> The Local Admin Control Plane is privileged and operator-only.
> 
> It must:
> - stay local by default
> - never be exposed publicly
> - use elevated access only
> - remain auditable where state-changing actions occur
> 
> ## Remote Access Rule
> If private remote access is later enabled, it must be done through an approved private access overlay.
> 
> Tailscale is acceptable for this role.
> 
> Tailscale may provide private access to:
> - `admin.qios.local`
> - `api.qios.local`
> - approved status surfaces
> 
> Tailscale does not change the rule that the Local Admin Control Plane is private and operator-only.
> ```
> 
> ---
> 
> ## File: `05_compute/05_integrations/020_access_overlays.md`
> 
> ```markdown
> # Access Overlays
> 
> ## Purpose
> Access overlays provide private connectivity into approved QiOS surfaces without changing the canonical runtime model.
> 
> They are transport and access layers only.
> 
> ## Rule
> Access overlays do not:
> - replace local runtime
> - replace cloud runtime
> - redefine service ownership
> - make private admin surfaces public
> - alter canonical data boundaries
> 
> ## Approved Use
> An access overlay may be used for:
> - private remote access to the Local Admin Control Plane
> - private remote access to the Local Control API
> - private operator access to local status and queue views
> - secure access to machine-local troubleshooting surfaces
> 
> ## Example: Tailscale
> Tailscale is an acceptable private access overlay for QiOS Local Host.
> 
> Permitted role:
> - private network path to approved local services
> 
> Not permitted role:
> - canonical identity layer
> - app runtime substitute
> - public exposure mechanism
> - bypass around local security rules
> 
> ## Guardrails
> When an access overlay is enabled:
> 
> - admin surfaces remain operator-only
> - service-role secrets remain backend-only
> - no tenant data is broadly exposed
> - local hostnames and routes remain stable
> - overlay access is documented as optional, not foundational
> ```
> 
> ---
> 
> # Repo/runtime shape to lock next
> 
> This is the local runtime tree I’d lock now:
> 
> ```text
> python_local/
> ├── api/
> │   ├── main.py
> │   ├── routes/
> │   │   ├── status.py
> │   │   ├── queue.py
> │   │   ├── ingest.py
> │   │   ├── retry.py
> │   │   └── archive.py
> │   ├── schemas/
> │   └── services/
> ├── file_pipeline/
> │   ├── scanner/
> │   ├── registrar/
> │   ├── normalizer/
> │   ├── extractor/
> │   ├── chunker/
> │   ├── embedder/
> │   ├── router/
> │   └── retry/
> ├── workers/
> │   ├── watcher_worker.py
> │   ├── ingest_worker.py
> │   ├── extract_worker.py
> │   ├── embed_worker.py
> │   ├── retry_worker.py
> │   └── sync_worker.py
> ├── services/
> │   ├── supabase_client.py
> │   ├── manifest_service.py
> │   ├── health_service.py
> │   ├── log_service.py
> │   └── config_service.py
> ├── jobs/
> │   ├── schedules.py
> │   └── repair_jobs.py
> └── config/
>     ├── settings.py
>     ├── paths.py
>     └── runtime_contract.py
> ```
> 
> And the local host routing target:
> 
> ```text
> qios.local         -> status / landing
> api.qios.local     -> FastAPI Local Control API
> admin.qios.local   -> Local Admin Control Plane
> portal.qios.local  -> local QiOne build
> docs.qios.local    -> local blueprint/docs preview
> ```
> 
> ---
> 
> # The part I would explicitly add as law
> 
> These are the non-negotiables:
> 
> - one local gateway
> - one local data root
> - one local control API
> - supervised workers only
> - no raw archive writes from frontends
> - no public admin exposure
> - Tailscale optional later, private only
> 
> That is the actual fix. Anything softer just recreates the same server mess with prettier words.
> 
> ---
> 
> # Immediate execution order
> 
> ## First
> Lock the blueprint text above.
> 
> ## Second
> Implement these in code/config:
> 
> 1. local gateway
> 2. stable hostnames
> 3. FastAPI control API cleanup to match the locked contract
> 4. worker supervision
> 5. admin UI behind gateway
> 6. `C:/QiData` validation and health checks
> 
> ## Third
> Add Tailscale only after the local host is stable.
> 
> Do **not** use Tailscale as a band-aid for a broken local process model. That would be dumb and it would just let you remotely access broken stuff faster.
> 
> If you want, next I’ll turn this into a **full patch map by file path** against your current blueprint tree so you can paste each section exactly where it belongs.

### User
> before i do anything lets fix the directory mamm, those folders and files everything shoudl build off or add to as it to deeper so would the local api stuff be first, then admin, then web or soemthing.

### Assistant
> I’m fixing the hierarchy first. That’s the right move, because if the tree is wrong, every later server decision gets shoved into the wrong home and the mess just grows downward.

### Assistant
> Found the real issue: you’re mixing **ownership structure** with **build order**. That’s why the tree feels mushy. The directory map should be **what owns what**, and then we define a separate execution order on top of it.

### Assistant
> No. Do **not** organize the tree as “API first, then admin, then web.”
> 
> That is **build order thinking**, and it will screw up the repo.
> 
> The repo should be **ownership-first**. The blueprint already says placement is based on operational ownership, not technical convenience, and every object should have one clear home. It also explicitly lists locking `python_local/file_pipeline` and the local API endpoints as open decisions, which means those are foundational contracts, not random folders to tuck under admin. fileciteturn6file0 fileciteturn6file1
> 
> # The right model
> 
> ## Separate these two things
> 
> ### 1. Directory map = ownership
> Where code lives based on what it **is**
> 
> ### 2. Build order = dependency
> What gets built **first**
> 
> Those are not the same.
> 
> ---
> 
> # The repo should be shaped like this
> 
> This is the clean version I’d lock.
> 
> ```text id="9vodf2"
> /
> ├── apps/                     # user-facing applications
> │   ├── admin-portal/         # local/internal operator UI
> │   ├── qione-portal/         # authenticated tenant portal
> │   ├── archive-ui/           # archive/review/search surface if split out
> │   └── setup-ui/             # onboarding/setup surface if split out later
> │
> ├── sites/                    # public or semi-static sites
> │   ├── qios-docs/            # blueprint / docs site
> │   ├── qially-web/           # public marketing / intake / public pages
> │   └── status-site/          # optional public status page
> │
> ├── python_local/             # machine-local runtime
> │   ├── api/                  # FastAPI local control plane
> │   ├── file_pipeline/        # detect -> register -> extract -> chunk -> embed
> │   ├── services/             # local runtime services used by api/pipeline
> │   ├── jobs/                 # scheduled and repair jobs
> │   ├── workers/              # machine-local worker entrypoints
> │   └── config/               # local settings, paths, contracts
> │
> ├── python_core/              # reusable python libs/tooling
> │   ├── extractors/
> │   ├── processors/
> │   ├── embeddings/
> │   ├── models/
> │   └── utils/
> │
> ├── workers/                  # cloud/edge/background workers, not local machine runtime
> │   ├── graph-projection/
> │   ├── retrieval-orchestrator/
> │   ├── metadata-enrichment/
> │   └── sync-connectors/
> │
> ├── packages/                 # shared TS/JS packages
> │   ├── ui/
> │   ├── config/
> │   ├── auth/
> │   ├── api-client/
> │   └── types/
> │
> ├── infra/                    # deploy/runtime infrastructure
> │   ├── gateway/
> │   ├── process-supervision/
> │   ├── tailscale/
> │   └── env/
> │
> ├── data/                     # local non-canonical data/bootstrap/dev helpers only
> │   ├── seeds/
> │   ├── fixtures/
> │   └── manifests/
> │
> ├── supabase/                 # canonical db migrations, policies, edge functions if retained
> │   ├── migrations/
> │   ├── functions/
> │   ├── seed/
> │   └── config.toml
> │
> ├── scripts/                  # repo and ops scripts
> │   ├── validate/
> │   ├── bootstrap/
> │   ├── repair/
> │   └── dev/
> │
> └── docs/                     # doctrine / blueprint source
>     ├── 00_genesis/
>     ├── 01_governance/
>     ├── 02_architecture/
>     ├── 03_structure/
>     ├── 04_data/
>     ├── 05_compute/
>     ├── 06_applications/
>     └── 07_operations/
> ```
> 
> ---
> 
> # The key call you need to make
> 
> ## `python_local/api` is **not** under admin
> It belongs under `python_local` because it is a **machine-local control plane**, not a UI surface.
> 
> The blueprint is very explicit:
> 
> - local APIs are machine-local control for pipeline state, file processing, and local state
> - apps are user-facing surfaces
> - admin is an internal operational dashboard surface
> - the Local Admin Control Plane is a standalone React/Vite admin portal that talks to the FastAPI local server
> 
> That means:
> 
> - **API owns control**
> - **admin owns UI**
> - **admin depends on API**
> - **web does not own either one** fileciteturn6file1turn6file2
> 
> So the relationship is:
> 
> ```text id="u8bzf8"
> python_local/api  --> machine-local control plane
> apps/admin-portal --> operator UI that consumes that API
> sites/*           --> public/static web, separate concern
> ```
> 
> ---
> 
> # Correct dependency order
> 
> This is the order to build, not the folder nesting.
> 
> ## Phase 1 — spine/runtime first
> 1. `python_local/config`
> 2. `python_local/file_pipeline`
> 3. `python_local/services`
> 4. `python_local/api`
> 5. `supabase/migrations` for the archive/runtime contract
> 
> Why: the blueprint’s first meaningful milestone is the spine being alive: Local Inbox → QiArchive Registration → Extraction → Local Embedding → App Search. It also says the next smart move is to make Spine & Runtime and Flows & Pipelines executable, and lists `python_local/file_pipeline` plus local API shape among the next decisions to lock. fileciteturn5file2 fileciteturn6file1turn6file2
> 
> ## Phase 2 — operator surfaces
> 6. `apps/admin-portal`
> 7. `apps/archive-ui` / review/search surfaces if separate
> 
> Why: admin is for operators and pipeline monitoring, not the foundation itself. It sits on top of the runtime. fileciteturn6file1turn6file2
> 
> ## Phase 3 — tenant-facing app surfaces
> 8. `apps/qione-portal`
> 
> Why: portal is the delivery surface on top of platform/domain/core, not the runtime base. fileciteturn6file1turn6file2
> 
> ## Phase 4 — public web/docs
> 9. `sites/qially-web`
> 10. `sites/qios-docs`
> 11. public status pages
> 
> Why: these are least foundational to getting the system alive.
> 
> ---
> 
> # So the hierarchy answer is:
> 
> ## Ownership hierarchy
> ### Core local runtime
> - `python_local/config`
> - `python_local/file_pipeline`
> - `python_local/services`
> - `python_local/jobs`
> - `python_local/workers`
> - `python_local/api`
> 
> ### App surfaces
> - `apps/admin-portal`
> - `apps/qione-portal`
> - optional archive/review/search UIs
> 
> ### Public/static surfaces
> - `sites/*`
> 
> That matches the blueprint’s split between:
> - local runtime
> - app surfaces
> - web surfaces
> - tools/interfaces/admin as distinct concerns. fileciteturn6file1turn6file2
> 
> ---
> 
> # The mistake to avoid
> 
> ## Bad
> ```text id="5pn9w2"
> apps/
>   admin/
>     api/
>     web/
> ```
> 
> Why it’s bad:
> - makes API look like an admin implementation detail
> - collapses runtime into UI
> - breaks the local/cloud/runtime boundary
> - makes future automation and workers look “secondary”
> 
> ## Good
> ```text id="c96dbz"
> python_local/
>   api/
>   file_pipeline/
>   services/
>   workers/
> 
> apps/
>   admin-portal/
>   qione-portal/
> 
> sites/
>   qially-web/
>   qios-docs/
> ```
> 
> ---
> 
> # One cleanup you should make in the blueprint itself
> 
> Your blueprint currently has a topology inconsistency.
> 
> It mentions:
> 
> - canonical repo topology like `/apps`, `/sites`, `/workers`, etc.
> - older references to `/python/qiarchive`
> - newer references to `/python_local/...`
> 
> That needs to be reconciled now, or you’ll keep second-guessing the tree. The blueprint also already says drift between formal architecture and implemented code must be flagged and resolved. fileciteturn6file0turn6file1
> 
> ## My recommendation
> Lock this as the final Python split:
> 
> - `python_local/` = machine-local runtime only
> - `python_core/` = reusable Python libraries
> - `workers/` = cloud/edge/background workers, not the local machine runtime
> 
> That is way cleaner than stuffing everything under one vague `python/`.
> 
> ---
> 
> # Final answer to your exact question
> 
> ## Should local API stuff be first, then admin, then web?
> **In build order: yes, basically.**  
> **In directory nesting: no.**
> 
> ### Build order
> 1. `python_local/config`
> 2. `python_local/file_pipeline`
> 3. `python_local/services`
> 4. `python_local/api`
> 5. `apps/admin-portal`
> 6. `apps/qione-portal`
> 7. `sites/*`
> 
> ### Directory ownership
> - Local API lives under `python_local/api`
> - Admin lives under `apps/admin-portal`
> - Web lives under `sites/`
> 
> That is the clean, QiOS-aligned map.
> 
> Next move should be locking the **final root tree + final `python_local` subtree** before we touch any more server or gateway design.

### User
> wait wait we are drifting again, im going to give you one root folder at a time to fix. lets get this right first. then i have 3 more.

### Assistant
> Agreed. We stop drifting.
> 
> We do **one root folder only**, lock it, then move to the next. No cross-repo redesign while we’re fixing that one root.
> 
> I can see the tree dumps you uploaded for roots like `infra`, `packages`, `python_core`, `python_local`, `QiData`, `data`, `scripts`, and `_qios_master_blueprint`. fileciteturn7file0 fileciteturn7file1 fileciteturn7file3 fileciteturn7file5 fileciteturn7file6
> 
> For each root, I’ll give you only four things:
> 
> 1. **What stays**
> 2. **What moves out**
> 3. **What gets renamed/merged**
> 4. **Final locked tree for that root**
> 
> Send the **first root name** exactly as you want to fix it, like:
> 
> - `python_local`
> - `packages`
> - `infra`
> - `scripts`
> 
> My recommendation is to start with **`python_local`** or **`data`**, because those are where runtime chaos usually multiplies fastest.

### User
> yes

### Assistant
> I’m taking “yes” as permission to start with `python_local` since that’s the highest-chaos root and the blueprint explicitly says to lock `python_local/file_pipeline` and the local API shape next.

### Assistant
> Good. We start with **`python_local`** and lock it hard.
> 
> The blueprint is actually clear on this: `python_local` is supposed to be the **machine-local runtime layer**, and the next open decisions explicitly include locking `python_local/file_pipeline` and the local API endpoints. It also gives the recommended shape as `api/`, `file_pipeline/`, `services/`, `jobs/`, and `config/`. fileciteturn9file6 fileciteturn9file2
> 
> Your current `python_local` root already has the right skeleton, but it also has drift: a second API stack, a cloud-style `app-api`, a worker orchestrator, generated reorg artifacts, and duplicate runtime layers living inside `services/`. fileciteturn9file0 fileciteturn9file7 fileciteturn9file8
> 
> # Root 1: `python_local`
> 
> ## 1) What stays
> 
> These belong in `python_local` and should remain there:
> 
> - `api/`
> - `config/`
> - `file_pipeline/`
> - `jobs/`
> - local runtime helper services like:
>   - `fs_service.py`
>   - `ocr_service.py`
>   - `ollama_client.py`
> 
> Why: the blueprint says local runtime owns file watcher, ingest pipeline, OCR, extraction, chunking, embeddings, and the **Local API control plane**. fileciteturn9file2turn9file3
> 
> ---
> 
> ## 2) What moves out
> 
> These do **not** belong in `python_local` as a locked root:
> 
> ### Move out of `python_local`
> - `services/app-api/`
> - `services/worker-orchestrator/`
> - `reorg_output/`
> 
> ### Move out or quarantine pending next root decision
> - `services/ai-api/`
> 
> ### Delete / ignore
> - all `__pycache__/`
> 
> Why:
> - `app-api` is not machine-local runtime; the blueprint distinguishes **Local APIs** from **App APIs**, and app APIs are cloud-hosted/frontend-facing, not part of the local runtime root. fileciteturn9file3
> - `worker-orchestrator` is async orchestration, queue/scheduler/event behavior, which belongs with worker infrastructure, not the local runtime root. fileciteturn9file3
> - `reorg_output/` is generated artifact trash, not source.
> - `ai-api` is only allowed to stay if you deliberately define it as a **machine-only local retrieval service**. Right now it reads like a second stack, so it should not stay by default. fileciteturn9file0
> 
> ---
> 
> ## 3) What gets renamed / merged
> 
> This is the part that matters most.
> 
> ## Rule:
> **`python_local` gets one runtime, one API surface, one pipeline. Not three.**
> 
> ### Merge these
> - `services/local-agent/app/api/*` → merge into top-level `api/`
> - `services/local-agent/app/workers/*` → merge into `jobs/` or `file_pipeline/` depending on role
> - `services/local-agent/app/runtime/*` → split into:
>   - `jobs/` for dispatcher/supervisor/retry-style logic
>   - `services/` for reusable helpers
>   - `config/` for paths/config/bootstrap constants
> 
> ### Rename these
> Top-level `api/` should stop using flat route file names like:
> - `routes_health.py`
> - `routes_ingest.py`
> - `routes_jobs.py`
> - `routes_search.py`
> 
> and become:
> 
> ```text id="8w7pl1"
> api/
>   main.py
>   routes/
>     health.py
>     ingest.py
>     jobs.py
>     search.py
>     queue.py
>     archive.py
> ```
> 
> Why: you currently have a top-level API and then a second API inside `local-agent`. That’s exactly the kind of duplicated logic the blueprint says not to allow. fileciteturn9file6
> 
> ### Move out of `file_pipeline`
> - `graph_project.py`
> 
> Why: graph projection is defined in the blueprint as a worker/async continuation concern, not part of the core local ingest pipeline. fileciteturn9file3
> 
> ---
> 
> ## 4) Final locked tree for `python_local`
> 
> This is the version I would lock.
> 
> ```text id="r4eqho"
> python_local/
> ├── README.md
> ├── api/
> │   ├── main.py
> │   ├── routes/
> │   │   ├── health.py
> │   │   ├── ingest.py
> │   │   ├── jobs.py
> │   │   ├── queue.py
> │   │   ├── search.py
> │   │   └── archive.py
> │   ├── schemas/
> │   └── deps.py
> ├── config/
> │   ├── settings.yaml
> │   ├── prefixes.yaml
> │   ├── paths.py
> │   ├── logging.py
> │   └── bootstrap.py
> ├── file_pipeline/
> │   ├── __init__.py
> │   ├── __main__.py
> │   ├── api_client.py
> │   ├── archive.py
> │   ├── chunk.py
> │   ├── classify.py
> │   ├── config.py
> │   ├── embed.py
> │   ├── extract.py
> │   ├── ingest.py
> │   ├── models.py
> │   ├── route.py
> │   ├── state_machine.py
> │   ├── watcher.py
> │   └── tests/
> │       └── test_pipeline.py
> ├── jobs/
> │   ├── runner.py
> │   ├── dispatcher.py
> │   ├── supervisor.py
> │   ├── retry.py
> │   ├── repair.py
> │   ├── sync.py
> │   ├── ingest_worker.py
> │   ├── extract_worker.py
> │   ├── chunk_worker.py
> │   ├── embed_worker.py
> │   ├── ocr_worker.py
> │   └── backup_worker.py
> ├── services/
> │   ├── fs_service.py
> │   ├── ocr_service.py
> │   ├── ollama_client.py
> │   ├── auth.py
> │   ├── heartbeat.py
> │   ├── queue.py
> │   ├── dropzone.py
> │   └── local_agent/
> │       ├── README.md
> │       ├── agent.py
> │       ├── models.py
> │       └── tests/
> └── tests/
>     ├── test_health.py
>     ├── test_dispatcher.py
>     ├── test_watchers.py
>     └── test_assignments.py
> ```
> 
> ---
> 
> # The blunt call
> 
> Your current `python_local` root is trying to be:
> 
> - the local runtime
> - a second app API
> - a worker platform
> - a local agent app
> - a reorg artifact dump
> 
> That’s why it feels wrong.
> 
> ## The locked rule for this root is:
> **`python_local` = one machine-local runtime root only.**
> 
> Not cloud API services.  
> Not generated reorg files.  
> Not duplicate API stacks.  
> Not async orchestration that belongs in `workers/`.
> 
> That matches the blueprint’s local runtime doctrine and the explicit open decisions to lock `python_local/file_pipeline` and local API shape next. fileciteturn9file2turn9file5
> 
> If you want, I’ll do the next step on this same root: a **line-by-line move map** for current `python_local` → locked `python_local`.

### User
> is this still relevant to the current qi systems

### Assistant
> I’m checking it against the current doctrine, not just the title, because some of the old stuff is still useful even when the center of gravity has shifted.

### Assistant
> Yes — but **only partially**.
> 
> The clean answer is:
> 
> **Relevant for QiAccess Start as the front door? Yes.**  
> **Relevant as the full doctrine for the current Qi systems stack? No.**
> 
> Why:
> 
> Your `qi_os_home_blueprint.md` is still solid on the **front-door model**:
> - QiAccess Start as the operational entry point
> - Start / Access split
> - qiserver + Wiki.js + QiNexus mental model
> - repo docs vs Wiki.js source-of-truth split
> - QiNexus root order and storage doctrine fileciteturn11file0 fileciteturn11file1 fileciteturn11file3
> 
> That part is still useful because it defines the **user-facing operating model**.
> 
> But it is **not enough for the current Qi systems** because the actual system has clearly moved beyond “static front door only” into:
> - local runtime
> - local APIs
> - file pipeline
> - local agent / workers
> - QiData runtime directories
> - infra with Docker, Supabase, Tailscale, tests, and bootstrap rules fileciteturn7file3 fileciteturn7file4 fileciteturn7file0
> 
> So the stale parts are the parts where that doc says things like:
> - “keep it static first”
> - “no Supabase yet”
> - don’t add persistence unless needed fileciteturn11file4
> 
> That is **not fully current anymore**, because your current tree already includes:
> - `infra/supabase/` with migrations and functions fileciteturn7file0
> - `python_local/api/`, `python_local/file_pipeline/`, and local services fileciteturn7file3
> - `data/` and `QiData/` runtime/state directories fileciteturn7file8 fileciteturn7file4
> 
> So here’s the truth:
> 
> ## Still current
> - QiAccess Start as front door
> - Start vs Access boundary
> - qiserver / Wiki.js / QiNexus relationship
> - anti-chaos “what job does this part do?” rule
> - repo docs vs Wiki.js split
> - storage root order and bucket meaning fileciteturn11file0 fileciteturn11file2 fileciteturn11file3
> 
> ## No longer sufficient as master doctrine
> - static-first as the whole strategy
> - “no Supabase yet”
> - treating the system like mostly a launcher/dashboard
> - not accounting for local runtime, workers, pipeline, infra, and machine-local server responsibilities fileciteturn11file4 fileciteturn7file3 fileciteturn7file0
> 
> ## Best way to treat it now
> Treat `qi_os_home_blueprint.md` as:
> 
> **QiAccess Start / Front Door doctrine**, not **master Qi systems doctrine**.
> 
> Meaning:
> - keep it for product model, UX, navigation, naming, access boundaries, and storage framing
> - do **not** use it as the final authority for runtime architecture, local host design, worker orchestration, infra, or pipeline design
> 
> That broader architecture now lives closer to the newer system structure and blueprint roots like:
> - `_qios_master_blueprint/docs/05_compute/*`
> - `python_local/`
> - `infra/`
> - `data/` / `QiData/` fileciteturn7file6 fileciteturn7file3 fileciteturn7file0 fileciteturn7file8
> 
> So the verdict is:
> 
> **Yes, still relevant.**  
> But **only as the front-door/product doctrine layer**.  
> It should be **demoted from master blueprint status** for the current Qi systems stack.
> 
> Next best move is to relabel it mentally as:
> 
> **“QiAccess Start Front Door Blueprint”**  
> instead of  
> **“current Qi systems blueprint.”**
