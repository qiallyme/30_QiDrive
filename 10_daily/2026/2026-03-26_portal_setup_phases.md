---
layout: page
title: "Portal Setup Phases"
slug: "portal_setup_phases"
created_at: "2026-03-26 13:22:35"
updated_at: "2026-07-18T11:03:14-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-005.json"
template_key: master-template
date: 2026-03-26
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69c57931-2c5c-8330-bb4a-aed8680f0697"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Portal Setup Phases

## Overview
- **Date**: 2026-03-26 13:22:35
- **Conversation ID**: `69c57931-2c5c-8330-bb4a-aed8680f0697`
- **Source**: `Chat-Export-28513-2026/conversations-005.json`

## Chat History

### User
> is there a way where we first get the portal working for me then layer on the clients, and you know we can always just do subdomains for client portals or wait that doesnt solve it or does it? no cause then we would need to have alll those in the dns. girl help me get this portal atleast workings.

### Assistant
> Yes. That is exactly how you should do it.
> 
> Right now you are mixing **platform architecture** with **tenant rollout**, and that is why it feels bigger than it needs to be.
> 
> ## The move
> 
> Build this in **2 phases**:
> 
> ### Phase 1 — Owner portal only
> Get **one working internal portal** for **you** first.
> 
> That means:
> 
> - login
> - dashboard
> - navigation
> - profile/settings
> - document area
> - tasks / tickets / notices / whatever your core objects are
> - role handling in a simple way, even if there is only one real role at first
> 
> This gives you:
> 
> - a real shell
> - working auth
> - working database patterns
> - working UI structure
> - proof that the app is alive
> 
> Until this exists, “client portal” is mostly fiction.
> 
> ---
> 
> ### Phase 2 — Add clients as tenants
> Once your own portal works, you layer in:
> 
> - organizations / tenants
> - client records tied to tenant_id
> - role-based access
> - client-scoped documents and views
> - invitations
> - branded or semi-branded portal views later
> 
> That is the clean order.
> 
> ## About subdomains
> 
> Subdomains **can** solve part of it, but not the part you’re stuck on right now.
> 
> ### What subdomains are good for
> They help with:
> 
> - cleaner branding  
>   `client1.qially.com`
> - white-label feel
> - future separation of tenant experiences
> - optional custom routing later
> 
> ### What they do **not** solve
> They do **not** solve:
> 
> - auth
> - tenancy model
> - permissions
> - database structure
> - portal UI
> - role logic
> - file access rules
> 
> So no, you do **not** need to start by creating a million DNS records.
> 
> Also: you would not necessarily need a manual DNS entry for every client if you use a **wildcard subdomain** like:
> 
> - `*.qially.com`
> 
> Then the app can resolve tenant from the subdomain dynamically.
> 
> Example:
> 
> - `acme.qially.com`
> - `rodriguez.qially.com`
> - `smithtax.qially.com`
> 
> All using one wildcard DNS record.
> 
> But again: **don’t start there**.
> 
> Start with either:
> 
> - `portal.qially.com`
> - or even `/portal` on the main app
> 
> That’s enough.
> 
> ## Best architecture for your stage
> 
> You need this:
> 
> ### Simple starting route structure
> - `app.qially.com` or `portal.qially.com`
> - one codebase
> - one auth system
> - one database
> - one dashboard shell
> 
> Then later you add:
> 
> - tenant-aware routing
> - optional subdomain resolution
> - custom branding per tenant if needed
> 
> ## The cleanest MVP
> 
> This is the version I’d push you toward:
> 
> ### Stack
> - **Next.js**
> - **Supabase Auth**
> - **Supabase Postgres**
> - **Supabase Storage**
> - deploy on **Cloudflare** or **Vercel** first for speed
> - keep it boring
> 
> ### MVP object model
> You do **not** need a giant schema first. Start with:
> 
> - `profiles`
> - `organizations`
> - `organization_members`
> - `clients` or just use `organizations` for client entities
> - `documents`
> - `tasks`
> - `tickets` or `requests`
> 
> Minimum viable idea:
> 
> - **profiles** = users
> - **organizations** = tenant/workspace
> - **organization_members** = which user belongs to which org and role
> - everything else gets `organization_id`
> 
> That’s the core.
> 
> ## Practical rollout path
> 
> ### Step 1
> Make the app work for **you only**
> 
> You log in and see:
> 
> - Dashboard
> - Clients
> - Documents
> - Tasks
> - Requests
> 
> Even if half the pages are placeholders.
> 
> ### Step 2
> Add `organization_id` everywhere important
> 
> Even if only your org exists at first.
> 
> That prevents rebuild pain later.
> 
> ### Step 3
> Add second role type
> 
> For example:
> 
> - owner/admin
> - client
> 
> You don’t even need fancy RBAC at first. Just enough to hide things.
> 
> ### Step 4
> Invite one test client
> 
> Not ten. One.
> 
> ### Step 5
> Only after that, decide whether clients need:
> 
> - same portal under one domain with scoped login
> - subdomains
> - custom domains later
> 
> ## What I think you should **not** do
> 
> Do **not**:
> 
> - build white-labeling first
> - build subdomain logic first
> - build fancy multi-tenant onboarding first
> - over-model every future use case
> - wait for perfect architecture before getting a dashboard live
> 
> That is how this drifts into another cemetery of almost-systems.
> 
> ## Your actual decision
> 
> Pick one of these and stop waffling:
> 
> ### Option A — Fastest
> **Single portal, no subdomains yet**
> - `portal.qially.com`
> - everyone logs into same app
> - tenant scope handled in database
> - easiest MVP
> 
> This is what I recommend.
> 
> ### Option B — Slightly more future-ready
> **Wildcard subdomain support later**
> - build same as Option A
> - later add `*.qially.com`
> - app detects tenant from hostname
> 
> Good, but later.
> 
> ### Option C — Overkill for now
> **Separate app instances per client**
> Bad idea right now. Too much maintenance, too much drift, too much ADHD tax.
> 
> ## The blunt truth
> 
> You do **not** have a subdomain problem.
> 
> You have an **MVP sequencing** problem.
> 
> You need a working portal shell first. One door. One user. One database pattern. Then tenants.
> 
> ## The build order I’d use
> 
> 1. Auth works  
> 2. Protected app layout works  
> 3. Sidebar/nav works  
> 4. Dashboard works  
> 5. Clients list works  
> 6. Document upload/list works  
> 7. Task/request tracking works  
> 8. `organization_id` wired in  
> 9. role restrictions  
> 10. invite a client  
> 11. optional subdomains later
> 
> ## Recommendation
> 
> Do this:
> 
> **Build one internal portal at `portal.qially.com` with tenant-aware data model from day one, but no client-facing subdomains yet.**
> 
> That gives you:
> - fast launch
> - less complexity
> - no DNS circus
> - no rework disaster later
> 
> If you want, next I’ll map the **exact folder structure, schema, and route plan** for the MVP so you can hand it to Cursor and start shipping instead of marinating in architecture soup.

### User
> while i have gemini working on the portal, lets work on the file and folder cleaning and renaming, organization then ingestion into the supabase postgres and s3 and graph for the ai graph rag, lets get this part done technically we are workin gon qiarchive right now.

### Assistant
> Yes. That is the right parallel track.
> 
> Portal UI can cook in Gemini.  
> **QiArchive** is the substrate. If the archive is messy, the portal and the AI both become liars.
> 
> So the real job is:
> 
> # QiArchive pipeline
> 
> **1. Normalize files**  
> **2. Assign durable IDs**  
> **3. Extract metadata**  
> **4. Push blobs to storage**  
> **5. Push rows to Postgres**  
> **6. Push nodes/edges to graph**  
> **7. Generate embeddings + chunk index**  
> **8. Expose retrieval layer for RAG**
> 
> Do **not** start with “AI graph RAG magic.”  
> Start with **clean file identity**. Everything else hangs off that.
> 
> ---
> 
> # What we are actually building
> 
> Think in 4 layers:
> 
> ## Layer 1 — Filesystem truth
> Your local/Drive archive with cleaned names and stable IDs.
> 
> ## Layer 2 — Structured metadata truth
> Supabase Postgres tables describing every file, chunk, entity, tag, relation, source, and ingestion event.
> 
> ## Layer 3 — Blob truth
> S3-compatible storage for raw files, previews, extracted text, thumbnails, OCR artifacts, JSON metadata dumps.
> 
> ## Layer 4 — Retrieval truth
> Embeddings + graph edges + metadata filters for AI recall.
> 
> If Layer 1 is sloppy, everything downstream is contaminated.
> 
> ---
> 
> # First decision: what is the canonical source?
> 
> You need one answer.
> 
> For QiArchive, I would use:
> 
> - **Local working vault / staging folder** as canonical during cleanup
> - **S3 storage** as canonical blob store after ingest
> - **Postgres** as canonical metadata index
> - **Drive** as sync/distribution, not truth
> 
> That matters because otherwise you will end up with:
> - same doc renamed in 4 places
> - broken references
> - duplicate embeddings
> - graph nodes pointing to dead files
> 
> ---
> 
> # The right order
> 
> ## Phase A — File cleanup and normalization
> Do this first.
> 
> ### Goals
> - remove naming chaos
> - collapse duplicates
> - make IDs immutable
> - separate file identity from file title
> 
> ### Rule
> **Filename is for humans. ID is for machines.**
> Never make the filename carry the whole system.
> 
> ---
> 
> # Recommended folder strategy
> 
> Given your style, do **not** do deep folder nesting.  
> Use a **flat-ish controlled hierarchy**.
> 
> Something like:
> 
> ```text
> QiArchive/
>   00_inbox/
>   01_staging/
>   02_archive/
>   03_exports/
>   04_logs/
>   05_scripts/
>   06_schemas/
> ```
> 
> Inside `02_archive/`, keep high-level buckets only:
> 
> ```text
> 02_archive/
>   legal/
>   tax/
>   business/
>   personal/
>   media/
>   reference/
> ```
> 
> Then let **metadata do the heavy lifting**, not folders.
> 
> That means:
> - category
> - project
> - client
> - matter
> - year
> - doc_type
> - language
> - source
> - status
> 
> Do **not** create 900 nested folders because your future self will hate you.
> 
> ---
> 
> # File naming standard
> 
> You already prefer short, consistent names. Good. Stick to that.
> 
> ## Formula
> ```text
> {qid}_{short_slug}.{ext}
> ```
> 
> Example:
> ```text
> QI-LEGAL-000184_motion_to_continue.pdf
> QI-TAX-000982_2023_w2_summary.pdf
> QI-BIZ-000411_square_fee_export.csv
> ```
> 
> ## Rules
> - lowercase
> - underscores only
> - no spaces
> - no dates unless the date is intrinsic to the document
> - no version soup like `final_FINAL_realfinal2`
> - no client full names in every filename unless necessary
> - slug should be descriptive but short
> 
> ## Important
> The **QID** stays forever.  
> The slug can change later if needed.
> 
> That means:
> - references
> - embeddings
> - graph nodes
> - citations
> - UI routes
> 
> all anchor to **QID**, not filename.
> 
> ---
> 
> # Metadata should carry the nuance, not the filename
> 
> Each file should get structured metadata like:
> 
> ```json
> {
>   "qid": "QI-LEGAL-000184",
>   "title": "Motion to Continue Hearing",
>   "category": "legal",
>   "project": "fcfcu_case",
>   "matter": "49D03-2501-MF-002559",
>   "doc_type": "motion",
>   "date_doc": "2026-03-22",
>   "date_ingested": "2026-03-26",
>   "source": "manual_upload",
>   "language": "en",
>   "status": "final",
>   "confidentiality": "private",
>   "checksum_sha256": "...",
>   "mime_type": "application/pdf"
> }
> ```
> 
> That is what makes the system usable.
> 
> ---
> 
> # Rename workflow
> 
> Do **not** bulk rename raw source files blindly. That is how you lose context.
> 
> Use a 3-step rename flow:
> 
> ## Step 1 — inventory
> Scan all files and produce a manifest:
> - current path
> - current filename
> - extension
> - size
> - modified date
> - checksum
> - probable category
> - probable duplicate group
> 
> ## Step 2 — review mapping
> Create a review table:
> - old path
> - proposed qid
> - proposed new filename
> - category
> - confidence
> - rename approved?
> 
> ## Step 3 — apply rename + log it
> Store rename history:
> - qid
> - old_path
> - new_path
> - renamed_at
> - renamed_by
> - checksum_before
> - checksum_after
> 
> That log matters.
> 
> ---
> 
> # Duplicate handling
> 
> This part needs discipline.
> 
> You have 3 duplicate types:
> 
> ## 1. Exact duplicates
> Same checksum. Easy. Keep one canonical file, mark the others as duplicate_of.
> 
> ## 2. Near duplicates
> Same content, slightly different filename or timestamps.
> 
> ## 3. Versioned variants
> Actually different files. Don’t merge them by accident.
> 
> ## Rule
> Never delete automatically unless exact duplicate and safely archived.
> 
> Use fields like:
> - `is_duplicate`
> - `canonical_file_id`
> - `version_group`
> - `version_label`
> 
> ---
> 
> # Database model for Supabase
> 
> Here is the core schema I’d start with.
> 
> ## `archive_files`
> One row per file.
> 
> Fields:
> - `id` uuid
> - `qid` text unique
> - `storage_key` text
> - `original_filename` text
> - `current_filename` text
> - `title` text
> - `slug` text
> - `category` text
> - `project` text
> - `matter` text
> - `doc_type` text
> - `source` text
> - `status` text
> - `language` text
> - `mime_type` text
> - `extension` text
> - `size_bytes` bigint
> - `checksum_sha256` text
> - `date_doc` date
> - `date_created_fs` timestamptz
> - `date_modified_fs` timestamptz
> - `date_ingested` timestamptz
> - `is_duplicate` boolean
> - `canonical_file_id` uuid nullable
> - `extracted_text_key` text
> - `ocr_text_key` text
> - `metadata_json` jsonb
> - `created_at`
> - `updated_at`
> 
> ## `archive_chunks`
> One row per chunk.
> 
> Fields:
> - `id` uuid
> - `file_id` uuid
> - `chunk_index` int
> - `chunk_text` text
> - `token_count` int
> - `char_count` int
> - `page_start` int nullable
> - `page_end` int nullable
> - `section_label` text
> - `embedding` vector
> - `chunk_hash` text
> - `metadata_json` jsonb
> - `created_at`
> 
> ## `archive_entities`
> Extracted people, orgs, places, statutes, accounts, cases, etc.
> 
> Fields:
> - `id`
> - `normalized_name`
> - `display_name`
> - `entity_type`
> - `metadata_json`
> 
> ## `archive_chunk_entities`
> Join table.
> 
> Fields:
> - `chunk_id`
> - `entity_id`
> - `mention_text`
> - `confidence`
> 
> ## `archive_relations`
> Graph edges.
> 
> Fields:
> - `id`
> - `from_entity_id`
> - `to_entity_id`
> - `relation_type`
> - `weight`
> - `source_chunk_id`
> - `metadata_json`
> 
> ## `archive_ingestion_runs`
> Track each ingest run.
> 
> Fields:
> - `id`
> - `run_type`
> - `source_path`
> - `status`
> - `files_scanned`
> - `files_ingested`
> - `files_skipped`
> - `files_failed`
> - `started_at`
> - `finished_at`
> - `log_key`
> 
> ## `archive_tags`
> Optional if you want flexible tagging.
> 
> ---
> 
> # Storage layout in S3
> 
> Keep it boring and deterministic.
> 
> ```text
> qiarchive/
>   raw/{qid}/original.ext
>   text/{qid}/extracted.txt
>   text/{qid}/ocr.txt
>   meta/{qid}/metadata.json
>   preview/{qid}/thumb.webp
>   preview/{qid}/page_001.webp
>   ingest_runs/{run_id}/manifest.json
>   ingest_runs/{run_id}/errors.json
> ```
> 
> Do not store everything with random names.  
> Use path predictability.
> 
> ---
> 
> # Graph strategy
> 
> Do not overbuild a separate graph database first unless you truly need one now.
> 
> Blunt truth: for your stage, **Postgres + pgvector + relation tables** is enough.
> 
> You can represent a graph with:
> - `archive_entities`
> - `archive_relations`
> - `archive_chunk_entities`
> 
> That already gives you:
> - “show all docs mentioning FCFCU”
> - “show all chunks linked to Marion County”
> - “find relations between account conveyance and foreclosure transfer timeline”
> - “trace entity network for a case”
> 
> Only move to Neo4j or something similar when:
> - graph traversals become central
> - you need deep relationship exploration at scale
> - Postgres joins become painful
> 
> Right now, separate graph DB is probably a distraction tax.
> 
> ---
> 
> # RAG architecture
> 
> Use hybrid retrieval.
> 
> ## Retrieval stack
> 1. metadata filter  
> 2. full-text search  
> 3. vector similarity  
> 4. graph/entity expansion  
> 5. reranking
> 
> ### Example flow
> User asks:
> “Show the timeline of surplus fund contradictions in the FCFCU case.”
> 
> System should:
> - filter `project = fcfcu_case`
> - search chunks for `surplus`, `credit bid`, `nunc pro tunc`, `32-29-7-9`
> - vector retrieve semantically similar chunks
> - expand related entities like `FCFCU`, `Sheriff Sale`, `Marion Superior Court 3`
> - rerank for final answer set
> 
> That is better than “vector only.”  
> Vector-only RAG gets dumb fast.
> 
> ---
> 
> # The ingestion pipeline
> 
> Here is the practical pipeline.
> 
> ## Stage 0 — scan
> Walk the filesystem and collect:
> - path
> - size
> - checksum
> - extension
> - mtime
> - probable MIME
> - probable text extractability
> 
> ## Stage 1 — classify
> Guess:
> - category
> - doc_type
> - project
> - language
> - confidence
> 
> Do this with rules first.  
> AI later for unresolved items.
> 
> ## Stage 2 — assign QID
> Every canonical file gets a QID.
> 
> ## Stage 3 — rename / relocate
> Move from inbox/staging into archive path.
> 
> ## Stage 4 — upload blob
> Push original to S3.
> 
> ## Stage 5 — extract text
> - PDFs: embedded text first
> - OCR only if needed
> - DOCX / TXT / MD / HTML directly
> - CSV / XLSX structured parse
> 
> ## Stage 6 — normalize text
> Clean headers, footers, repeated whitespace, page junk.
> 
> ## Stage 7 — chunk
> Chunk by structure, not just raw token count.
> 
> Prefer:
> - heading aware
> - page aware
> - section aware
> 
> ## Stage 8 — embed
> Store embeddings in `archive_chunks`.
> 
> ## Stage 9 — entity extraction
> People, organizations, dates, case numbers, statutes, account numbers, addresses.
> 
> ## Stage 10 — relation extraction
> Generate edges like:
> - `FCFCU -> filed -> nunc_pro_tunc_motion`
> - `surplus_funds -> governed_by -> IC_32_29_7_9`
> - `account_6016506CV... -> transferred_to -> new_owner`
> 
> ## Stage 11 — index and log
> Record success/failure per file.
> 
> ---
> 
> # Classification rules first, AI second
> 
> Do not let AI classify everything from day one. Wasteful and inconsistent.
> 
> Use rules like:
> - path contains `/legal/` -> category legal
> - filename contains `motion`, `order`, `notice` -> doc_type legal_filing
> - filename contains `1099`, `w2`, `it40`, `1040` -> tax
> - extension `.eml` -> correspondence
> - contains cause number pattern -> link to matter
> 
> Then use AI only for:
> - title cleanup
> - ambiguous category
> - entity extraction
> - summary generation
> - relation inference
> 
> That keeps cost down and consistency up.
> 
> ---
> 
> # Minimum viable naming dictionary
> 
> You need controlled vocab now or drift will eat you alive.
> 
> ## `category`
> - legal
> - tax
> - business
> - personal
> - finance
> - reference
> - media
> - admin
> 
> ## `doc_type`
> - motion
> - order
> - notice
> - letter
> - email
> - invoice
> - receipt
> - statement
> - return
> - worksheet
> - transcript
> - screenshot
> - video
> - audio
> - memo
> - contract
> - intake
> - report
> 
> ## `status`
> - raw
> - staged
> - reviewed
> - final
> - duplicate
> - archived
> 
> ## `source`
> - manual_upload
> - google_drive
> - email_export
> - scanner
> - generated
> - scraped
> - migration
> 
> Do not freestyle these in production.
> 
> ---
> 
> # What to do this week
> 
> Here is the sane sequence.
> 
> ## Sprint 1 — cleanup foundation
> - create `QiArchive/` root structure
> - create naming rules
> - create metadata vocabulary
> - scan existing files into manifest
> - detect exact duplicates
> - generate proposed rename map
> 
> ## Sprint 2 — canonicalization
> - approve/adjust rename map
> - assign QIDs
> - rename and move files
> - write metadata sidecars if needed
> - log rename history
> 
> ## Sprint 3 — ingest MVP
> - create Supabase tables
> - create S3 bucket structure
> - upload canonical files
> - extract text
> - store file rows + chunk rows
> 
> ## Sprint 4 — retrieval MVP
> - add pgvector
> - generate embeddings
> - add full-text index
> - test search + filter + semantic search
> 
> ## Sprint 5 — graph layer
> - extract entities
> - create relation edges
> - test graph-assisted retrieval
> 
> That is the right order.
> 
> ---
> 
> # Do not do these things
> 
> ## Do not:
> - invent 30 folder levels
> - encode all metadata into filenames
> - use dates inconsistently
> - rename without manifest + rollback path
> - OCR everything by default
> - build a separate graph DB before basic retrieval works
> - ingest garbage before cleaning identity
> - let Gemini or any AI freestyle schema names across the system
> 
> That last one is how you get schema drift and duplicate systems.
> 
> ---
> 
> # Your immediate deliverables
> 
> You need these 6 artifacts first:
> 
> ## 1. `qiarchive_folder_map.md`
> Defines root folder structure and purpose.
> 
> ## 2. `qiarchive_naming_rules.md`
> Defines QID format, filename rules, slug rules, forbidden patterns.
> 
> ## 3. `qiarchive_vocab.json`
> Controlled vocab for category/doc_type/status/source/project.
> 
> ## 4. `qiarchive_manifest.csv`
> Inventory of current files.
> 
> ## 5. `qiarchive_rename_map.csv`
> Old path -> new QID -> new path.
> 
> ## 6. `qiarchive_schema.sql`
> Supabase schema for files/chunks/entities/relations/ingestion runs.
> 
> Without those, you are still “thinking about a system,” not building one.
> 
> ---
> 
> # My recommendation
> 
> Start with this exact technical stance:
> 
> ## Canonical model
> - **Local staging** for cleanup
> - **Supabase Postgres** for metadata
> - **S3-compatible bucket** for blobs
> - **pgvector + Postgres relations** for RAG and graph
> - **No separate graph DB yet**
> 
> That is lean, coherent, and ADHD-safe.
> 
> ---
> 
> # The next move
> 
> We should do this in order:
> 
> ## Next artifact set
> 1. finalize **QID format**
> 2. finalize **folder map**
> 3. finalize **filename pattern**
> 4. draft **Supabase schema**
> 5. draft **manifest + rename workflow**
> 6. then generate the actual cleanup scripts
> 
> Here is the blunt answer:  
> You do **not** need more ideas. You need the **spec** before the scripts.
> 
> I can draft the full **QiArchive technical spec v1** right now in a clean handoff format so you can feed it straight into Cursor/Gemini.

### User
> also keep in mind qiarchive is a combination of the interface in the portal, the ddata layers, the workers, and python, i dont know if we consilidate all that or keep is spearte but hereis the current full qilabs tree

### Assistant
> Yes: **consolidate the system, not the concerns**.
> 
> That tree is already telling on itself. You do **not** have one clean platform yet. You have at least **three overlapping gravitational centers**:
> 
> - `Atrium-main` = mature-ish portal/app product with API, web, database package, email package, e2e, and file/document workflows. fileciteturn1file2
> - `QiData` = a separate data-processing workspace with inbox, extracted text, manifests, logs, failed, reviewed, embeddings cache, and processing stages. fileciteturn1file3
> - `QiMonoRepo_v2` = your newer “everything” platform direction with qione app routes for admin, ai, documents, objects, chronicle, tax, API routes, and broader feature modules. fileciteturn1file3
> 
> And deeper in the uploaded tree, you also already have **dedicated workers** plus **supabase migrations/functions** living in another slice of the repo, which confirms the architecture is trying to become a platform, not a single app. fileciteturn1file1
> 
> ## Blunt answer
> 
> **Do not keep this as separate islands.**  
> Also **do not mash everything into one giant app folder.**
> 
> The right move is:
> 
> # Recommended structure
> 
> ## One monorepo
> QiArchive should live inside **one canonical monorepo**.
> 
> ## Separate bounded layers inside it
> Keep these concerns distinct:
> 
> - **apps/** → user-facing UIs
> - **workers/** → ingestion, embedding, graph, metadata jobs
> - **packages/** → shared schemas, types, utilities, client SDKs
> - **supabase/** → migrations, SQL, functions, policies
> - **python/** → heavy ingestion/parsing/OCR/repair scripts
> - **data/** → runtime staging only, not source-of-truth code
> - **docs/** → ADRs, schema maps, naming rules, ingestion specs
> 
> That is the difference between **organized modularity** and **repo sprawl**.
> 
> ---
> 
> # What QiArchive actually is
> 
> You said it right:
> 
> QiArchive is a combination of:
> 
> - portal interface
> - data layers
> - workers
> - python
> - graph / RAG / retrieval backend
> 
> That means QiArchive is **not** just a page in the portal.  
> It is a **platform capability**.
> 
> So architecturally:
> 
> ## QiArchive should be a domain
> Not a repo by itself, and not a random feature folder.
> 
> Think:
> 
> - `apps/qione` or `apps/portal` → QiArchive UI surfaces
> - `workers/ingestion`, `workers/embedder`, `workers/resource_graph` → QiArchive processing plane
> - `packages/qiarchive-core` → shared types, content identity, chunk schemas, metadata contracts
> - `packages/qirag` → retrieval logic, graph traversal helpers, ranking logic
> - `python/qiarchive` → text extraction, OCR fallback, rename pipeline, manifests, batch repair
> - `supabase/migrations` → archive tables, chunk tables, entity tables, relations, queue tables
> 
> That is clean.
> 
> ---
> 
> # What your tree says is going wrong
> 
> ## 1. Duplicate platform intent
> You have `Atrium-main` and `QiMonoRepo_v2` both trying to be the real app platform. That is drift. fileciteturn1file2turn1file3
> 
> ## 2. Data pipeline detached from product
> `QiData` is acting like a sidecar processing bunker instead of a governed ingestion runtime. fileciteturn1file3
> 
> ## 3. Workers and migrations are already platform-level
> The workers folder includes ingestion, embedder, metadata naming, orchestrator, resource graph, semantic router, and self-heal. That is not “just a script pile.” That is an execution layer. fileciteturn1file1
> 
> ## 4. Docs already imply you know this
> The tree includes architecture docs, governance docs, ADRs, content identity, canonical repo tree, and inbox ingestion pipeline docs. So the problem is not lack of concept. The problem is **multiple half-canonical implementations**. fileciteturn1file0
> 
> That is classic schema drift / repo drift.
> 
> ---
> 
> # The decision
> 
> ## Do this
> **Promote one repo to canonical.**
> 
> From what you showed, **`QiMonoRepo_v2` should probably become the canonical future repo** because it already reflects your broader system vision: admin, ai, chronicle, documents, objects, tax, settings, workers visibility, API routes, and modular features. fileciteturn1file3
> 
> ## Do not do this
> - don’t keep growing Atrium and QiMonoRepo in parallel
> - don’t leave QiData as a permanently separate mystery warehouse
> - don’t scatter Supabase schema across random app subtrees
> - don’t keep Python outside the architecture map like it’s “temporary”
> 
> Temporary is how permanent mess gets born.
> 
> ---
> 
> # My recommended target layout
> 
> Something like this:
> 
> ```text
> QiLabs/
>   apps/
>     qione/                  # main portal / admin / user interface
>     public-site/            # optional marketing or public utilities later
> 
>   workers/
>     ingestion/
>     metadata_naming/
>     embedder/
>     resource_graph/
>     semantic_router/
>     orchestrator/
>     self_heal/
> 
>   packages/
>     qiarchive-core/         # content identity, metadata contracts, shared types
>     qirag/                  # retrieval, ranking, graph query helpers
>     qidb/                   # db access layer / repositories / SQL wrappers
>     ui/                     # shared UI if needed
>     shared/                 # generic shared utils only
> 
>   python/
>     qiarchive/
>       scan/
>       rename/
>       extract/
>       ocr/
>       manifests/
>       repair/
> 
>   supabase/
>     migrations/
>     functions/
>     seeds/
>     policies/
> 
>   data/
>     inbox/
>     staging/
>     reviewed/
>     failed/
>     manifests/
>     logs/
>     extracted_text/
>     embeddings_cache/
> 
>   docs/
>     architecture/
>     adr/
>     schema/
>     governance/
>     runbooks/
> ```
> 
> That gives you one roof, with clean operational boundaries.
> 
> ---
> 
> # Rule of thumb
> 
> ## Keep separate
> Keep these separate as **execution concerns**:
> 
> - UI code
> - worker code
> - Python processing
> - SQL/migrations
> - runtime data folders
> 
> ## Consolidate
> Consolidate these as **system governance**:
> 
> - one repo
> - one naming system
> - one content identity model
> - one schema authority
> - one ingestion contract
> - one source of truth for queue/status states
> - one canonical docs/ADR path
> 
> ---
> 
> # Specific recommendation for your current assets
> 
> ## Atrium-main
> Do **not** keep building it as a first-class future platform unless you decide it is the winner. Right now it looks more like:
> - a strong reference implementation
> - a donor repo
> - a migration source
> 
> It has useful patterns for auth, documents, files, portal separation, settings, and tests. But if QiMonoRepo is your actual future direction, then Atrium should be mined, not worshipped. fileciteturn1file2
> 
> ## QiData
> Keep the **runtime folders**, but move the concept under the canonical repo as `/data` or `/runtime/qiarchive`.  
> That folder structure is useful operationally, but it should not live as a spiritually separate system. fileciteturn1file3
> 
> ## workers
> Promote them into first-class platform modules under the canonical monorepo. They already deserve that. fileciteturn1file1
> 
> ## Python
> Keep Python separate from TS/Next codebase concerns, but inside the monorepo.  
> Why? Because:
> - OCR
> - parsing
> - bulk rename
> - manifest generation
> - file repair
> - maybe embeddings/local ML jobs
> 
> are all perfectly reasonable in Python and do not belong awkwardly stuffed into Next route handlers.
> 
> ---
> 
> # The architecture stance I’d lock
> 
> ## QiArchive = domain
> QiArchive is a domain spanning UI + ingestion + retrieval + graph.
> 
> ## QiOne = app shell
> QiOne is the shell through which you manage and use that domain.
> 
> ## Supabase = canonical metadata + queue + auth + policy layer
> Not just a dumb backend.
> 
> ## S3/R2 = blob layer
> Raw files, previews, text artifacts.
> 
> ## Workers = async execution plane
> Ingestion, embedding, graph updates, self-healing.
> 
> ## Python = batch and heavy processing plane
> Not the main app, but not disposable either.
> 
> That is clean and actually scalable.
> 
> ---
> 
> # What I would cut immediately
> 
> 1. **Pick one canonical app repo this week.**
>    Probably `QiMonoRepo_v2`.
> 
> 2. **Freeze architecture drift.**
>    No new feature gets added to both Atrium and QiMonoRepo.
> 
> 3. **Define migration classes:**
>    - keep
>    - merge
>    - archive
>    - reference-only
>    - delete later
> 
> 4. **Move QiData under the canonical structure conceptually.**
>    Even if physical move happens later.
> 
> 5. **Write one `qiarchive_architecture_lock.md`.**
>    One page. No poetry. Just:
>    - canonical repo
>    - domain boundaries
>    - runtime folders
>    - schema authority
>    - worker authority
>    - naming authority
> 
> ---
> 
> # My recommendation in one line
> 
> **Consolidate into one monorepo, keep UI / workers / Python / data runtime as separate bounded layers, and treat QiArchive as a platform domain inside QiOne rather than a separate floating project.**
> 
> That is the least stupid path.
> 
> ## Next best move
> 
> Paste the rest of the tree if you want, but even from this, the real next step is not more browsing. It is producing a **repo decision matrix**:
> 
> - what stays in canonical
> - what gets merged
> - what gets archived
> - what becomes reference-only
> 
> I can draft that matrix from this tree right now.

### User
> that want the mission the mission was to get the local stuff up and running and deployable from some admin tinkintor ui if needed or a agenet to talk to the admin portal so when i git clone this into another machine it can be ran and start working on that machine too.

### Assistant
> Yep. That changes the target.
> 
> You are not trying to design the perfect forever architecture first.  
> You are trying to make **QiLabs portable, bootable, and operable locally on any new machine** with minimal nonsense.
> 
> That means the mission is:
> 
> # Actual mission
> 
> **A cloned repo should be able to:**
> 
> 1. boot locally on another machine
> 2. provision or connect required services
> 3. run the admin portal
> 4. run the workers
> 5. run Python ingestion jobs
> 6. point at local or remote storage/db
> 7. let you control the system from one admin UI or agent layer
> 8. be deployable later without rewriting the whole thing
> 
> That is a **developer operations and runtime bootstrap problem**, not just a folder cleanup problem.
> 
> ---
> 
> # So the right architecture question is not:
> 
> “Should QiArchive be one thing or many things?”
> 
> It is:
> 
> # Better question
> 
> **What structure lets this repo be cloned onto another machine and become usable fast?**
> 
> That means you optimize for:
> 
> - reproducible startup
> - environment consistency
> - service orchestration
> - local-first operability
> - deployability
> - admin control plane
> 
> ---
> 
> # Correct framing
> 
> You need **one operational monorepo** with **multiple services**, plus a **single control surface**.
> 
> ## One repo
> Because clone-and-run matters.
> 
> ## Multiple services
> Because UI, workers, DB, storage, and Python jobs are not the same thing.
> 
> ## One control surface
> Because your ADHD will hate a system that requires remembering 8 terminals and 14 commands.
> 
> ---
> 
> # What the system should look like
> 
> ## Control plane
> This is the thing you interact with.
> 
> Could be:
> 
> - admin portal UI
> - Tinkitor-style internal ops panel
> - agent interface attached to admin portal
> - CLI wrapper with dashboards/logs/status
> 
> This is where you:
> - see service status
> - trigger ingestion
> - run repair jobs
> - review rename maps
> - manage queues
> - inspect graph jobs
> - monitor embeddings
> - view storage/db health
> - run bootstrap/setup tasks
> 
> That is your **admin operations layer**.
> 
> ---
> 
> # The core requirement
> 
> When you clone to another machine, you should be able to do roughly this:
> 
> ```bash
> git clone ...
> cd qilabs
> cp .env.example .env
> just setup
> just dev
> ```
> 
> Or:
> 
> ```bash
> pnpm install
> docker compose up -d
> pnpm dev
> ```
> 
> Or one wrapper script:
> 
> ```bash
> ./scripts/bootstrap_local.sh
> ```
> 
> If the system cannot do that, it is not portable enough yet.
> 
> ---
> 
> # Your target state
> 
> ## Repo contains
> - app code
> - workers
> - Python tools
> - infrastructure config
> - local bootstrap scripts
> - environment templates
> - admin control plane
> - docs/runbooks
> 
> ## Repo does not require
> - mystery manual steps
> - memory-based setup
> - hidden local dependencies
> - random external state you forgot about
> - “oh yeah also install this weird thing first”
> 
> That last one kills portability.
> 
> ---
> 
> # Recommended structure
> 
> ```text
> QiLabs/
>   apps/
>     admin-portal/
>     api/
> 
>   workers/
>     ingestion/
>     embedding/
>     graph/
>     repair/
> 
>   python/
>     qiarchive/
> 
>   packages/
>     core/
>     db/
>     shared/
>     agent-sdk/
> 
>   infra/
>     docker/
>     compose/
>     scripts/
>     env/
> 
>   supabase/
>     migrations/
>     seed/
>     functions/
> 
>   data/
>     inbox/
>     staging/
>     processed/
>     manifests/
>     logs/
> 
>   docs/
>     setup/
>     runbooks/
>     architecture/
> ```
> 
> This is not about elegance. It is about **cloneability**.
> 
> ---
> 
> # What needs to be local vs remote
> 
> You need to decide what can run locally and what can stay hosted.
> 
> ## Local-capable
> These should run locally for dev and portability:
> 
> - admin UI
> - API
> - Python jobs
> - workers
> - local Postgres or Supabase local stack
> - local S3-compatible storage like MinIO if needed
> - vector extension / pgvector
> - local file staging folders
> 
> ## Optional remote in dev
> Can be remote if you want less setup pain:
> 
> - hosted Supabase
> - hosted object storage
> - external embedding APIs
> - auth provider if Supabase handles it
> 
> But if the mission is **clone to another machine and it works**, then the repo should support:
> 
> ### Mode A — local-only
> Everything needed can run on the machine.
> 
> ### Mode B — hybrid
> Local app/workers, remote Supabase/storage.
> 
> That flexibility is what you want.
> 
> ---
> 
> # Best practical model
> 
> ## Use profiles / modes
> 
> ### `local`
> - local Postgres
> - local MinIO
> - local workers
> - local Python
> - local admin portal
> 
> ### `hybrid`
> - hosted Supabase
> - hosted S3/R2
> - local portal/workers/python
> 
> ### `prod`
> - deployed portal/api
> - hosted db/storage
> - remote workers
> 
> This makes the system portable without forcing every machine to be prod-like.
> 
> ---
> 
> # The admin portal’s job
> 
> The admin portal should not just be “client portal admin pages.”
> 
> It should also be your **ops cockpit**.
> 
> ## Minimum ops pages
> You need pages for:
> 
> - system status
> - ingestion queue
> - file inventory
> - rename review
> - storage browser
> - embeddings status
> - graph/entity jobs
> - failed jobs
> - settings / env summary
> - worker health
> - task runner / job trigger panel
> 
> That is your Tinkitor-style layer.
> 
> ---
> 
> # Agent vs UI
> 
> You mentioned maybe an admin Tinkitor UI or an agent talking to admin portal.
> 
> Correct answer: **both, but in order**.
> 
> ## First
> Build the UI control plane.
> 
> Because:
> - deterministic
> - inspectable
> - easier to debug
> - easier to expose buttons/actions/logs
> 
> ## Then
> Add an agent layer on top of the same admin actions.
> 
> So the agent can:
> - trigger ingest
> - summarize failures
> - propose rename rules
> - answer “what broke”
> - suggest graph rebuild
> - inspect stuck jobs
> 
> But the agent should call the **same underlying job/action endpoints** the UI uses.
> 
> Do not build magic agent-only actions first. That gets messy fast.
> 
> ---
> 
> # What must be standardized now
> 
> To make clone-and-run real, you need these artifacts:
> 
> ## 1. `.env.example`
> Every required variable documented.
> 
> Group them like:
> - app
> - database
> - storage
> - auth
> - embeddings
> - workers
> - python
> - paths
> 
> ## 2. `docker-compose.local.yml`
> For local infra services:
> - postgres
> - minio
> - redis if needed
> - optional qdrant if you insist, though I’d avoid for now
> - mailhog optional
> - worker dependencies
> 
> ## 3. `bootstrap script`
> One command to:
> - verify tools
> - install deps
> - create folders
> - copy env
> - start local services
> - run migrations
> - seed minimal data
> 
> ## 4. `Makefile` or `justfile`
> Human-friendly commands:
> - `just setup`
> - `just dev`
> - `just workers`
> - `just python`
> - `just migrate`
> - `just seed`
> - `just status`
> - `just clean`
> 
> ## 5. `runbook`
> A dead simple file:
> - first boot
> - common issues
> - how to reset
> - where logs live
> - how to switch between local/hybrid/prod
> 
> ---
> 
> # Strong recommendation on orchestration
> 
> Use **Docker Compose for local infra**, not necessarily for everything.
> 
> ### Good Compose candidates
> - postgres
> - minio
> - redis
> - optional worker queue infra
> 
> ### Fine to run directly on host
> - Next app
> - Node workers
> - Python scripts
> 
> That gives you fast iteration without over-containerizing development.
> 
> If you try to dockerize every tiny thing from day one, you’ll burn time.
> 
> ---
> 
> # What the bootstrap should do
> 
> Here is the actual sequence your repo should support.
> 
> ## `setup`
> - check Node, pnpm, Python, Docker
> - install JS deps
> - create Python venv or uv environment
> - install Python deps
> - create data folders
> - copy `.env.example` if `.env` missing
> - start Docker infra
> - wait for DB/storage readiness
> - run migrations
> - seed initial admin user / sample workspace
> - print URLs and credentials
> 
> ## `dev`
> - run admin portal
> - run API if separate
> - run workers in watch mode
> - expose local logs/status
> 
> ## `status`
> - check DB
> - check storage
> - check workers
> - check queue backlog
> - check ingestion folders
> 
> This is what makes the repo operational.
> 
> ---
> 
> # What not to do
> 
> ## Do not
> - make local startup depend on memory
> - bury runtime paths in random scripts
> - hardcode machine-specific absolute paths
> - require 6 separate manual app launches
> - split control logic across multiple half-admin tools
> - mix admin portal and client portal concerns too early
> 
> The admin portal needs to be your control center first. Client stuff is later.
> 
> ---
> 
> # Clean architecture for your mission
> 
> ## QiOne / Admin Portal
> Your interface.
> 
> ## QiArchive Core
> Shared contracts:
> - file identity
> - metadata schema
> - chunk schema
> - ingestion state
> - relation/entity schema
> 
> ## Workers
> Async execution:
> - ingest
> - embed
> - graph build
> - self-heal
> - reindex
> 
> ## Python
> Heavy local/batch file handling:
> - scan
> - rename
> - OCR
> - parse
> - manifest generation
> - repair
> 
> ## Infra
> Portable local services:
> - db
> - storage
> - queue
> 
> That’s the right split.
> 
> ---
> 
> # The real MVP
> 
> You do **not** need the whole dream system first.
> 
> You need this working:
> 
> ### On a fresh machine:
> - clone repo
> - run setup
> - open admin portal
> - see system status
> - drop files into inbox
> - run ingest
> - store metadata in db
> - store blobs in storage
> - view results in admin UI
> 
> That is the MVP.
> 
> Once that works, you can layer:
> - agent controls
> - graph enrichment
> - better retrieval
> - client-facing access
> 
> ---
> 
> # The concrete decision
> 
> So no, the mission is **not** primarily “clean the repo tree.”
> 
> The mission is:
> 
> # Revised mission statement
> 
> **Create a portable local-first QiLabs runtime where the admin portal acts as the control plane for QiArchive ingestion, workers, storage, and data services, so the repo can be cloned to another machine and become operational with minimal setup.**
> 
> That is the spec.
> 
> ---
> 
> # What we should define next
> 
> We need to lock 5 things:
> 
> ## 1. Canonical runtime map
> What services exist, and which are:
> - required local
> - optional local
> - remote-compatible
> 
> ## 2. Bootstrap contract
> Exactly what `setup` and `dev` do.
> 
> ## 3. Env contract
> All required variables and defaults.
> 
> ## 4. Control plane scope
> What the admin portal can trigger/view/manage in v1.
> 
> ## 5. Repo layout
> Organized around runtime, not just code aesthetics.
> 
> ---
> 
> # Best next move
> 
> I’d do this next, in order:
> 
> 1. **Write the runtime service map**
> 2. **Write the clone-and-run bootstrap spec**
> 3. **Write the monorepo layout spec**
> 4. **Write the admin control-plane scope**
> 5. **Then generate the actual folder map + scripts**
> 
> That is the shortest path to a system you can actually move between machines instead of another brilliant diagram.
> 
> If you want, I’ll draft the **QiLabs Local Runtime Spec v1** in a clean handoff format you can feed straight into Gemini/Cursor.

### User
> host as much as we can for free or really cheaply

### Assistant
> Yes. That should be the rule:
> 
> # Host the expensive parts only when they prove value
> 
> For your setup, the cheapest sane path is:
> 
> ## Free or nearly-free stack
> - **Cloudflare Pages/Workers** for the admin portal and lightweight APIs. Static asset requests on Pages are free/unlimited, and the free Workers plan includes **100k requests/day**. citeturn116522search2turn486553search3turn486553search9
> - **Cloudflare R2** for object storage when you need hosted blobs. The free tier includes **10 GB-month storage**, **1M Class A ops**, and **10M Class B ops**, with no egress fees listed for R2. citeturn486553search7
> - **Supabase Free** for auth + Postgres + light storage while you are still proving the model. Supabase Free currently includes **2 free projects**, **500 MB database per project**, **1 GB storage**, **50,000 MAU**, **5 GB egress**, and **500,000 Edge Function invocations**. citeturn116522search3turn116522search1turn116522search0
> - **Resend Free** for transactional email. Their free tier shows **3,000 emails/month** and **100/day**. citeturn116522search4
> 
> That is the cheapest hosted core that still feels real.
> 
> # What I would not host early
> - Don’t pay for Railway unless you actually need always-on workers or background services that can’t live elsewhere. Railway’s free plan is only **$1 of free resources**, and the paid Hobby plan starts at **$5/month** with usage-based billing on top. citeturn486553search1
> - Don’t jump to Vercel unless the UI deployment experience is meaningfully better for this repo. Vercel Hobby is free, but once you start leaning on compute and bandwidth, it becomes easier to drift into usage ceilings. Their Hobby plan includes **1M function invocations**, **4 CPU-hours**, and **100 GB/month data transfer**. citeturn486553search0turn486553search5
> 
> # Best cost strategy for you
> 
> ## Phase 1 — cheapest practical setup
> - Host **portal UI** on Cloudflare Pages
> - Host **light API endpoints / admin actions** on Cloudflare Workers
> - Host **auth + Postgres** on Supabase Free
> - Host **files/blobs** on Cloudflare R2
> - Run **Python ingestion, rename jobs, OCR, graph builds, heavy workers locally** on your machine
> 
> This keeps the costly and noisy compute local, while the user-facing stuff stays online cheaply. That is probably your best move right now. citeturn116522search2turn486553search3turn486553search7turn116522search3
> 
> ## Phase 2 — small paid upgrade only when needed
> Your first likely paid upgrade is probably:
> - **Supabase Pro** if you outgrow the **500 MB DB** or need projects that won’t pause, since Free projects are limited and can hit read-only behavior when the DB exceeds the free disk limit. citeturn116522search3turn116522search7
> 
> That means your first real spend is likely:
> - **$25/month-ish class** for Supabase Pro if needed
> - maybe **$5/month Cloudflare Workers paid** later if free quotas stop being enough. Cloudflare’s paid Workers plan has a **$5/month minimum**. citeturn486553search3
> 
> # My blunt recommendation
> 
> ## Host now
> - **Cloudflare Pages/Workers**
> - **Cloudflare R2**
> - **Supabase Free**
> - **Resend Free**
> 
> ## Keep local for now
> - ingestion workers
> - embeddings jobs
> - graph builds
> - OCR/parsing
> - bulk repair scripts
> - admin-only heavy tasks
> 
> ## Avoid for now
> - always-on Railway services
> - overusing Vercel for backend compute
> - paying for multiple overlapping platforms “just in case”
> 
> You’re trying to stay lean, so don’t buy uptime for jobs that can run from your own machine.
> 
> # The actual architecture I’d use
> 
> ## Hosted
> - `portal.qially.com` → Cloudflare Pages
> - admin/server actions/light API → Cloudflare Workers
> - auth/db → Supabase
> - blob storage → R2
> - email → Resend
> 
> ## Local
> - Python pipeline
> - worker orchestration
> - local staging folders
> - batch ingestion
> - embeddings/graph rebuilds
> 
> That gives you a **cheap hybrid** instead of pretending everything has to be cloud-native on day one.
> 
> # Important catch
> Supabase Free is fine for MVP, but **500 MB database** is not a lot once you start storing chunk metadata, embeddings-related bookkeeping, logs, entities, and relations. Also, their docs say free projects can enter **read-only mode** when they exceed the free DB limit. citeturn116522search3turn116522search7
> 
> So the money-saving move is:
> 
> - keep **raw files in R2**
> - keep **extracted text artifacts in R2**
> - keep **DB rows lean**
> - do **not** bloat Postgres with junk you could store as files
> 
> That matters.
> 
> # Decision
> If you want the cheapest sensible stack, this is it:
> 
> **Cloudflare Pages + Workers + R2 + Supabase Free + Resend Free, with heavy workers local until they earn the right to be hosted.**
> 
> That’s the least stupid cost structure.
> 
> Next, I can turn that into a **hosted-vs-local service matrix** for QiLabs so you know exactly what runs where.

### User
> yes, lets do it an dget it going i want something working asap.

### Assistant
> Good. I set up the runtime spec in canvas so we have a single source of truth to build from.
> 
> ## What we do now
> 
> We stop theorizing and start with the **boot path**.
> 
> ### Immediate build order
> 1. **Pick the canonical repo root**
>    - probably `QiMonoRepo_v2` unless you already know another folder is the winner
> 
> 2. **Create the runtime skeleton inside it**
>    - `apps/admin-portal`
>    - `workers/`
>    - `python/qiarchive`
>    - `data/`
>    - `supabase/`
>    - `infra/scripts`
> 
> 3. **Get one thing running first**
>    - admin portal boots locally
>    - connects to Supabase
>    - shows a basic `/admin/system` page
>    - confirms env + DB + storage status
> 
> 4. **Then wire QiArchive v1**
>    - inbox folder
>    - scan script
>    - manifest generation
>    - one ingest action from admin UI
> 
> ## The real MVP
> You do **not** need the whole monster online this week.
> 
> You need this:
> 
> - clone repo
> - install deps
> - run setup
> - run dev
> - open admin portal
> - click ingest
> - see a file appear in inventory
> 
> That’s it. That’s the first win.
> 
> ## What I already locked
> I created the **QiLabs Local Runtime Spec v1** in canvas. That gives us:
> - hosted vs local split
> - repo structure
> - bootstrap contract
> - control plane scope
> - implementation order
> - hard rules to stop drift
> 
> ## Fastest next step
> Paste the **current full QiLabs tree** here, and I’ll turn it into a **keep / merge / archive / move** map so you know exactly what to do first instead of wandering around the repo.
