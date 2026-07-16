---
layout: page
title: "Document Management Workflow"
slug: "document_management_workflow"
created_at: "2026-01-04 06:19:47"
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
date: 2026-01-04
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "695a5a8d-dbe0-832b-bd55-db4f60922fed"
canonical_ref: ""
---

# Document Management Workflow

## Overview
- **Date**: 2026-01-04 06:19:47
- **Conversation ID**: `695a5a8d-dbe0-832b-bd55-db4f60922fed`
- **Source**: `Chat-Export-28513-2026/conversations-003.json`

## Chat History

### User
> I want to create a document management workflow that pipes into qinote and gina, essential a kinda precursor to the vectorizaion should i use the open source free paperless, the purpose is really ingest all documents and images, ocr, update metadata and keywords ect for seracing and vectorizing no more driving myself crazy to find a doc that is scanned but system cante find it.

### Assistant
> Yes — **Paperless-ngx is the right “precursor layer”** for what you’re describing *if* your goal is: **central ingest → OCR → normalized naming/metadata → fast human search now → clean, structured feed into QiNote/Gina for vectorization later**.
> 
> If you skip this layer and jump straight into “vectorize everything,” you’ll keep bleeding time because your inputs are messy (random scans, inconsistent naming, missing metadata, mixed image/PDF quality). Paperless fixes that upstream.
> 
> ## Recommendation
> ### Use **Paperless-ngx** as the intake + OCR + metadata hub, then pipe “clean artifacts” into QiNote/Gina.
> It gives you:
> - **Automated OCR** (searchable PDFs)
> - **Rules-based classification** (title, correspondent, tags, document type)
> - **Consistent metadata** you can export/replicate into QiNote front matter
> - **A stable document ID** (Paperless doc id) you can map to your QiDecimal IDs later
> - A “single truth” library so you stop re-scanning / re-hunting
> 
> ## The workflow you want (clean, deterministic)
> Think in 5 stages:
> 
> ### 1) Capture (everything funnels here)
> Sources:
> - Phone scans (recommended: scan app that produces clean PDFs)
> - Email-in (paperless consumption mailbox)
> - Desktop “drop folder”
> - Camera photos (receipts, letters)
> 
> **Rule:** nothing goes directly into QiNote. Everything goes into intake first.
> 
> ### 2) Normalize + OCR (Paperless consumption)
> Paperless does:
> - Convert images → PDF (if configured)
> - OCR → text layer
> - Store original + processed
> - Index the content for search
> 
> Output standard: **PDF/A-ish + text layer** (or at least “searchable PDF”).
> 
> ### 3) Enrich metadata (make it searchable *before* vectors)
> You want a consistent schema:
> - `doc_type` (Court Filing, Notice, Receipt, Medical, Insurance, Tax, Vehicle, Banking, etc.)
> - `correspondent` (FCFCU, Court Clerk, AES, IRS, Insurance Co, etc.)
> - `date_document` (document date)
> - `date_received` (when you got it)
> - `case_or_project` (FCFCU_CASE, AES_DISPUTE, etc.)
> - `keywords/tags` (Service, Certified Mail, Hearing, Payment, Notice, Demand Letter, etc.)
> - `status` (Draft, Filed, Received, Evidence, Exhibit)
> 
> Paperless supports correspondents, document types, tags, and custom fields (depending on your setup). This is where you stop the “I know it exists but can’t find it” insanity.
> 
> ### 4) Publish to QiNote (controlled export)
> Once a doc is “clean” (OCR + metadata done), it gets exported/synced into a **QiNote staging area**:
> 
> Example target structure (flat-ish, ID-driven):
> - `QiNoteVault/documents/{case_or_project}/{YYYY}/{YYYY-MM-DD}__{doc_type}__{correspondent}__{paperless_id}.pdf`
> - plus a sidecar markdown:
>   - `{same_name}.md` with YAML front matter
> 
> That markdown becomes Gina’s stable handle for vectorization.
> 
> ### 5) Vectorization (later, deterministic)
> Gina/QiNote ingests the **markdown sidecar + OCR text** (not just the PDF blob), and stores embeddings with references back to:
> - Paperless doc id
> - file path
> - canonical metadata
> 
> That gives you **semantic search** without losing provenance.
> 
> ---
> 
> ## Why Paperless-ngx over “just OCRmyPDF + folders”
> You *can* DIY it with:
> - NAPS2/scanner → OCRmyPDF → filesystem naming rules → ripgrep + local index
> But you’ll end up rebuilding:
> - tagging, correspondent detection, inbox triage, doc-type routing, UI review, audit trail
> 
> Paperless is the “already solved” version.
> 
> ---
> 
> ## When Paperless-ngx is NOT the best choice
> Pick something else if:
> - You refuse to run Docker / self-host anything
> - You need extremely custom workflows across teams (then you’re in “DMS platform” territory)
> - You want pure local filesystem-first with zero database/UI (then do OCRmyPDF pipeline + strict naming + an indexer)
> 
> If any of those are true, the best lightweight alternative is:
> - **NAPS2 (scan) + OCRmyPDF (OCR) + strict filename schema + automated metadata in sidecar YAML**
> …but it’s less friendly for ongoing triage.
> 
> ---
> 
> ## The “Cody-proof” rules that prevent chaos
> These are non-negotiable if you want this to work:
> 
> 1) **One intake door** (Paperless inbox). No exceptions.  
> 2) **Never rename manually** outside the system. Naming is generated.  
> 3) **Metadata first, vectors second.**  
> 4) **Every exported doc has a sidecar `.md`** with YAML.  
> 5) **Stable IDs win** (Paperless doc id now; QiDecimal later; both mapped).
> 
> ---
> 
> ## Concrete “pipeline contract” between Paperless → QiNote/Gina
> When a doc is marked “Ready” (tag or field), export:
> 
> **PDF** + **MD sidecar** where the MD includes:
> - title
> - dates
> - correspondent
> - tags
> - doc_type
> - source (“paperless-ngx”)
> - `paperless_id`
> - (optional) OCR text excerpt or full text (depends on storage strategy)
> 
> Gina indexes the MD + OCR text and stores embedding pointers back to the PDF.
> 
> ---
> 
> ## Your fastest path (no overengineering)
> Do this in order:
> 
> 1) Stand up Paperless-ngx (Docker) with:
>    - consumption folder
>    - OCR enabled
>    - email import if useful
> 2) Define **doc types, correspondents, tags** (start small: 10–20 total)
> 3) Create **rules** for your big buckets (FCFCU, Court, AES, IRS, Insurance, Vehicle)
> 4) Create a **“Ready_for_QiNote”** tag
> 5) Write a tiny export job:
>    - watches Paperless for docs tagged Ready_for_QiNote
>    - exports PDF + writes MD sidecar into your QiNote vault
> 6) Only then add vectorization.
> 
> ---
> 
> ## One sharp truth
> If you don’t lock down **taxonomy + naming + one intake door**, vector search will become a fancy way to retrieve chaos faster. Paperless-ngx is the discipline layer you’re missing.
> 
> If you want, I can give you:
> - a **starter taxonomy** (doc_types/tags/correspondents) tuned for your legal + ops life
> - a **file naming standard** aligned to QiDecimal IDs
> - a **sidecar YAML template** that Gina/QiNote can ingest consistently
> - and an **export script spec** (no fluff, just the contract and steps)

### User
> ok i have cloned the repo, i am using antigravity gemeni to do the coding what do i tell gemini now.

### Assistant
> Tell Gemini to stop freelancing and implement a **known-good Paperless-ngx local setup** first, then add a **minimal export bridge** to QiNote. Here’s the exact prompt to paste.
> 
> ```text
> You are my implementation engineer. We already cloned the Paperless-ngx repo. Your job is to get a working local instance running FAST, then add a minimal “export to QiNote” bridge.
> 
> CONSTRAINTS
> - Do NOT invent architecture. Follow Paperless-ngx’s official docker-compose flow.
> - Target: local dev on Windows 10/11 (Docker Desktop) OR WSL2 Ubuntu. Assume Docker is available.
> - Output must be copy/paste runnable. Prefer commands + exact file edits.
> - No long explanations. If something is ambiguous, make a reasonable default and state it.
> 
> PHASE 1 — RUN PAPERLESS-NGX LOCALLY
> 1) Identify the repo’s recommended docker compose file (compose, docker-compose, examples, etc).
> 2) Create a .env (or env file) with sane defaults:
>    - PAPERLESS_URL=http://localhost:8000
>    - PAPERLESS_TIME_ZONE=America/Chicago
>    - PAPERLESS_OCR_LANGUAGE=eng
>    - Enable OCR. Use the default OCR engine Paperless supports.
> 3) Bring it up with Docker (compose up -d).
> 4) Print:
>    - The URL to open
>    - Default admin creation steps (exact command)
>    - Where the “consume” folder is on the host and how to drop files in it
> 5) Provide a quick verification checklist:
>    - upload doc -> OCR -> full-text search works
> 
> PHASE 2 — QINOTE EXPORT BRIDGE (MINIMUM VIABLE)
> Goal: when a document has tag “Ready_for_QiNote”, export:
> - A PDF file into: ./qinote_vault/documents/{YYYY}/{YYYY-MM-DD}__{title_slug}__paperless-{doc_id}.pdf
> - A sidecar markdown file with YAML front matter into the same folder:
>   ---
>   title:
>   paperless_id:
>   created:
>   document_date:
>   correspondent:
>   doc_type:
>   tags: [ ... ]
>   source: paperless-ngx
>   ---
>   (then optionally an OCR text excerpt if available via API)
> Rules:
> - This export must be deterministic and idempotent (re-running doesn’t create duplicates).
> - Use Paperless-ngx REST API (token auth). Do NOT scrape the database.
> - Provide a simple script (Python preferred) with:
>   - config via .env
>   - a “run once” mode
>   - logging
> - Add a README section: how to generate API token, where to set it, how to run the export.
> 
> DELIVERABLES
> - Exact commands to run
> - Exact file paths you changed/created
> - The final python script content
> - Any docker-compose changes required
> ```
> 
> If you want a second, even more controlling “don’t mess this up” add-on, paste this right after:
> 
> ```text
> Important: If you see multiple compose options, choose the one recommended by the project docs. Do not refactor the stack. Do not add extra services unless required. Keep the export bridge as a separate script outside the core app so we can upgrade Paperless cleanly.
> ```
> 
> What this does: it forces Gemini into a disciplined, two-stage delivery—**get Paperless working first**, then **build a clean API-based export** that QiNote/Gina can vectorize later.
> 
> If Gemini starts hallucinating paths/commands, your correction is simple: “Show me the exact file in the repo you’re referencing (path) and quote the relevant section.”

### User
> ok, gemini is on it, what else can we work on on our end while it is doing that. work on intake, pipeline workflow, sops, ect.

### Assistant
> Good. While Gemini grinds on plumbing, **you should lock the human + system workflow** so we don’t end up with a technically “working” system that still leaks chaos.
> 
> Below is the **highest-ROI work you can do in parallel**. This is not busywork—this is the part that prevents rework later.
> 
> ---
> 
> ## 1. Intake Taxonomy (DECIDE ONCE)
> If this isn’t decided now, everything downstream degrades.
> 
> ### 1.1 Document Types (keep it tight: 12–15 max)
> Start with **these** (you can extend later, but don’t):
> 
> - Court Filing  
> - Court Order  
> - Legal Notice  
> - Demand Letter  
> - Certified Mail Receipt  
> - Banking Statement  
> - Billing Statement  
> - Insurance Document  
> - Medical Record  
> - Tax Document  
> - Vehicle Document  
> - Government Correspondence  
> - Contract / Agreement  
> - Receipt / Proof of Payment  
> - Evidence / Exhibit  
> 
> Rule: if you hesitate between two, pick the **primary purpose**, not format.
> 
> ---
> 
> ### 1.2 Correspondents (authority-based, not emotional)
> Examples (you will customize):
> 
> - FCFCU  
> - Indiana Trial Court 49D03  
> - AES Indiana  
> - IRS  
> - Indiana BMV  
> - Insurance – Auto  
> - Insurance – Health  
> - USPS  
> - City of Evansville  
> - Utility Provider – Other  
> 
> Rule: **One correspondent per doc.** No stacking.
> 
> ---
> 
> ### 1.3 Tags (verbs + states, not nouns)
> Tags are *how you think* later. Use states/actions.
> 
> Core set:
> - received  
> - filed  
> - pending  
> - overdue  
> - paid  
> - disputed  
> - evidence  
> - exhibit  
> - service_issue  
> - certified_mail  
> - deadline  
> - hearing  
> - compliance  
> - noncompliance  
> 
> Rule:  
> - Tags = situation  
> - Doc Type = what it is  
> - Correspondent = who it’s from
> 
> This separation is critical for search sanity.
> 
> ---
> 
> ## 2. Intake SOP (THIS SAVES YOUR BRAIN)
> Write this now, even if rough.
> 
> ### SOP: Document Intake
> **Trigger:** Any document enters your life (mail, email, scan, photo).
> 
> 1. Scan or save to **Paperless consume folder only**
> 2. Wait for OCR completion
> 3. Assign:
>    - Document Type
>    - Correspondent
>    - Document Date
>    - Tags (minimum: `received`)
> 4. If legally relevant:
>    - Add tag `evidence`
>    - Add project/case tag (e.g., `FCFCU_CASE`)
> 5. If complete and clean:
>    - Add tag `Ready_for_QiNote`
> 6. Do **not** export manually. Export is automated only.
> 
> Print this. Tape it somewhere. This is your guardrail.
> 
> ---
> 
> ## 3. QiNote Sidecar Schema (LOCK IT NOW)
> Decide the YAML *before* Gemini writes code so you don’t retrofit.
> 
> ### Canonical YAML (v1)
> ```yaml
> ---
> title:
> paperless_id:
> source: paperless-ngx
> 
> document_type:
> correspondent:
> tags: []
> 
> document_date:
> date_received:
> 
> project:
> status:
> 
> confidence: primary_source   # or secondary / inferred
> ---
> ```
> 
> Rules:
> - Dates are ISO (`YYYY-MM-DD`)
> - `project` is single-valued (no arrays)
> - `status` mirrors your mental state (pending, filed, resolved)
> 
> If you change this later, you reindex everything. Decide once.
> 
> ---
> 
> ## 4. Naming Convention (HUMAN-READABLE, MACHINE-STABLE)
> Decide this **now**, not after you have 400 files.
> 
> **Filename pattern:**
> ```
> YYYY-MM-DD__{doc_type}__{correspondent}__paperless-{id}.pdf
> ```
> 
> Why this works:
> - Sorts chronologically
> - Scannable by humans
> - Deterministic
> - Survives exports, zips, courts, and drives
> 
> QiDecimal IDs can be layered later in metadata—don’t block on them.
> 
> ---
> 
> ## 5. Intake Stress-Test (DO THIS TODAY)
> Grab **10 real documents**:
> - 1 court notice
> - 1 billing statement
> - 1 certified mail slip
> - 1 random receipt
> - 1 insurance letter
> - 5 mixed chaos items
> 
> Run them through:
> - Can you classify each in <30 seconds?
> - Do tags feel obvious?
> - Could “future you” find it in 6 months?
> 
> If not, fix taxonomy now—not later.
> 
> ---
> 
> ## 6. “Ready for Vectorization” Gate
> This is a **mental rule**, not code.
> 
> A document is vector-worthy ONLY IF:
> - OCR is clean
> - Metadata is complete
> - Context is known (project, status)
> 
> Otherwise, vectors will lie to you confidently.
> 
> ---
> 
> ## 7. Create a One-Page SYSTEM MAP (grounding)
> This helps ADHD immensely.
> 
> ```
> [Scanner / Email / Photos]
>             ↓
>      Paperless Inbox
>             ↓
>      OCR + Metadata
>             ↓
>    Ready_for_QiNote
>             ↓
>    QiNote Vault (.md + .pdf)
>             ↓
>      Gina / Vectors
> ```
> 
> Print or save this. When overwhelmed, point at the box you’re in.
> 
> ---
> 
> ## 8. Optional (but smart): “Inbox Zero” Rule
> - Paperless inbox must hit **zero once per day**
> - If not classifiable in 60 seconds → tag `needs_review` and move on
> - Never leave it untagged
> 
> This prevents backlog paralysis.
> 
> ---
> 
> ## Blunt truth (because you asked for it)
> If you skip taxonomy + SOPs, you’ll still “lose documents,” just with better OCR and prettier UI. The system only works if **you decide how thinking maps to structure**.
> 
> If you want, next we can:
> - Draft the SOP as a printable `.md`
> - Create a **court-case–specific tag pack**
> - Design the **QiNote folder tree**
> - Or define **export batches** (legal vs financial vs personal)
> 
> Say which one you want next and we’ll lock it.

### User
> ok, my storage backup is google drive, what should my top folders be on google drive, these are not the qinoteos folder or anything like just just the top folders i should lock in on my gdrive backup for everything we do.

### Assistant
> Good question. This is a **lock-once, don’t revisit** decision. Your Google Drive is **cold storage + authoritative backup**, not a workspace. If you get this right, everything else (QiNote, Paperless, Gina, exports, court bundles) snaps into place cleanly.
> 
> Below is the **recommended TOP-LEVEL Google Drive folder structure** for *everything you do*, with zero QiNoteOS coupling.
> 
> ---
> 
> ## ✅ **TOP-LEVEL GOOGLE DRIVE FOLDERS (FINAL)**
> Lock these. Do not add more at the top level later.
> 
> ```
> /01_ADMIN
> /02_LEGAL
> /03_FINANCIAL
> /04_TAX
> /05_HEALTH
> /06_VEHICLES
> /07_HOUSING_UTILITIES
> /08_BUSINESS
> /09_PROJECTS
> /10_ARCHIVES
> ```
> 
> That’s it. 10 folders. Human-scalable. Court-safe. Backup-safe.
> 
> ---
> 
> ## 📁 FOLDER INTENT & RULES (IMPORTANT)
> 
> ### **01_ADMIN**
> **What it is:** Identity, credentials, global references  
> **Examples:**
> - IDs (passport, license)
> - SSN docs
> - Birth certificate
> - Master contact lists
> - Power of attorney
> - Global reference docs
> 
> **Rule:** Rarely changes. Highly sensitive. Minimal writes.
> 
> ---
> 
> ### **02_LEGAL**
> **What it is:** Anything that could end up in court  
> **Examples:**
> - Court filings
> - Orders
> - Notices
> - Evidence
> - Certified mail proofs
> - Case correspondence
> 
> **Subfolder rule:**  
> Inside this folder, everything is **CASE-SCOPED**:
> ```
> /02_LEGAL/FCFCU_CASE
> /02_LEGAL/AES_DISPUTE
> ```
> 
> Never mix cases at the root.
> 
> ---
> 
> ### **03_FINANCIAL**
> **What it is:** Money movement, statements, obligations  
> **Examples:**
> - Bank statements
> - Credit cards
> - Loans
> - Payment confirmations
> - Bills (non-tax)
> 
> **Rule:** Statements > receipts > summaries. No taxes here.
> 
> ---
> 
> ### **04_TAX**
> **What it is:** Anything touching IRS/state tax  
> **Examples:**
> - Returns
> - W-2 / 1099
> - ITIN docs
> - Correspondence with IRS/state
> - Tax prep workpapers
> 
> **Rule:** Organized by **tax year**, always.
> 
> ---
> 
> ### **05_HEALTH**
> **What it is:** Medical + insurance  
> **Examples:**
> - Medical records
> - Insurance claims
> - Bills
> - EOBs
> - Disability/ADA documentation
> 
> **Rule:** No finance overlap. Bills go here *only if medical*.
> 
> ---
> 
> ### **06_VEHICLES**
> **What it is:** Cars, registration, insurance  
> **Examples:**
> - Titles
> - Registration
> - Plates
> - Insurance
> - Repair records
> 
> **Rule:** One subfolder per vehicle.
> 
> ---
> 
> ### **07_HOUSING_UTILITIES**
> **What it is:** Where you live + what keeps it running  
> **Examples:**
> - Mortgage / lease
> - Utilities (AES, water, internet)
> - HOA
> - Home insurance
> - Property tax
> 
> **Rule:** Utilities never go in Financial directly—context matters.
> 
> ---
> 
> ### **08_BUSINESS**
> **What it is:** Anything related to operating entities  
> **Examples:**
> - QiAlly
> - Client contracts
> - Invoices
> - Business correspondence
> - Vendor agreements
> 
> **Rule:** Organized by **entity or client**, not by doc type.
> 
> ---
> 
> ### **09_PROJECTS**
> **What it is:** Non-legal, non-business, time-bounded efforts  
> **Examples:**
> - Writing projects
> - Personal initiatives
> - Temporary research
> - Collaboration folders
> 
> **Rule:** Projects eventually graduate to Archive or another category.
> 
> ---
> 
> ### **10_ARCHIVES**
> **What it is:** Frozen, closed, or historical  
> **Examples:**
> - Closed cases
> - Old tax years (beyond active window)
> - Prior residences
> - Old vehicles
> 
> **Rule:** Read-only. No edits. Ever.
> 
> ---
> 
> ## 🚫 WHAT YOU DO **NOT** DO
> - ❌ No “Misc”
> - ❌ No “Inbox” at Drive root
> - ❌ No date-based folders at top level
> - ❌ No QiNoteOS folders here
> - ❌ No duplication across top folders
> 
> If something doesn’t clearly belong, it goes to **Paperless inbox**, not Drive.
> 
> ---
> 
> ## 🔁 HOW THIS PLAYS WITH PAPERLESS & QINOTE
> - **Paperless** = intake + OCR + metadata
> - **QiNote** = working knowledge + vectors
> - **Google Drive** = authoritative backup & legal-safe mirror
> 
> Exports from Paperless/QiNote land in the **correct top-level folder only**.
> 
> ---
> 
> ## 🔒 FINAL RULE (NON-NEGOTIABLE)
> Once these folders exist:
> - You **never rename them**
> - You **never add siblings**
> - All automation assumes these names forever
> 
> This is how you avoid a second migration later.
> 
> ---
> 
> If you want next, I can:
> - Define **standard subfolders** for LEGAL and FINANCIAL
> - Map **Paperless tags → Drive folder routing**
> - Give you a **Drive mirror SOP**
> - Or sanity-check this against your current Drive mess and plan a clean migration
> 
> Say which one.

### User
> these tope level seem more like document storage folder than top level storage infrastrcture folders. please note this is the root of what would be considered my blob storage.

### Assistant
> Good catch. You’re right — what I gave you before was **domain-semantic storage**. For **blob storage root**, we need something more **infrastructure-oriented, neutral, future-proof, and automation-friendly**.
> 
> Think: *“If I were designing S3 buckets or a data lake, what are the root prefixes?”*  
> That’s the correct mental model.
> 
> Below is the corrected answer.
> 
> ---
> 
> ## ✅ **CANONICAL GOOGLE DRIVE BLOB ROOT (LOCK THIS)**
> These are **infrastructure tiers**, not content meaning.
> 
> ```
> /00_SYSTEM
> /01_INGEST
> /02_PRIMARY
> /03_WORKING
> /04_PUBLISH
> /05_SYNC
> /06_BACKUP
> /07_EXPORTS
> /08_SHARED
> /09_SCRATCH
> /99_ARCHIVE
> ```
> 
> This is your **blob substrate**. Everything else nests under this.
> 
> ---
> 
> ## 📦 WHAT EACH ROOT MEANS (NO OVERLAP)
> 
> ### **00_SYSTEM**
> Infrastructure control plane.
> 
> - Schemas
> - SOPs
> - Taxonomies
> - Automation configs
> - README.md for the storage system
> - “How this Drive works” documentation
> 
> **Rule:** Humans read. Automation references. Rare writes.
> 
> ---
> 
> ### **01_INGEST**
> Raw, untrusted, first-touch data.
> 
> - Scans
> - Camera uploads
> - Email drops
> - External shares
> - USB dumps
> 
> **Rule:**  
> Nothing stays here long.  
> Nothing is trusted.  
> Everything moves forward or gets deleted.
> 
> This often mirrors Paperless “consume”.
> 
> ---
> 
> ### **02_PRIMARY**
> Authoritative canonical objects.
> 
> - Final PDFs
> - Source images
> - Originals with checksums
> - “This is the truth” copies
> 
> **Rule:**  
> One canonical copy per object.  
> No edits. New versions create new objects.
> 
> ---
> 
> ### **03_WORKING**
> Active manipulation zone.
> 
> - Drafts
> - Notes
> - In-progress bundles
> - Temporary reorganizations
> 
> **Rule:**  
> Mess is allowed. Permanence is not.
> 
> ---
> 
> ### **04_PUBLISH**
> Human-facing deliverables.
> 
> - Court bundles
> - Submissions
> - Packages sent to others
> - Print-ready PDFs
> - Final exports
> 
> **Rule:**  
> If it leaves your system, it came from here.
> 
> ---
> 
> ### **05_SYNC**
> Mirrors from other systems.
> 
> - QiNote vault mirror
> - Paperless export mirror
> - GitHub repo mirrors (docs only)
> - External system syncs
> 
> **Rule:**  
> You don’t edit here.  
> You trace provenance here.
> 
> ---
> 
> ### **06_BACKUP**
> Redundant safety layer.
> 
> - Zipped snapshots
> - Dated backups
> - Integrity-checked bundles
> 
> **Rule:**  
> Append-only.  
> Never manually edited.
> 
> ---
> 
> ### **07_EXPORTS**
> Machine-generated outputs.
> 
> - Vector prep files
> - OCR text dumps
> - CSVs
> - JSON
> - Sidecar MD exports
> 
> **Rule:**  
> Recreatable. Disposable. Script-owned.
> 
> ---
> 
> ### **08_SHARED**
> Access-controlled collaboration.
> 
> - Folders shared with lawyers
> - Family
> - Clients
> - Temporary access grants
> 
> **Rule:**  
> Nothing authoritative lives here.
> 
> ---
> 
> ### **09_SCRATCH**
> Cognitive relief zone.
> 
> - “Put it here so I don’t lose it”
> - Temporary thinking space
> - Brain-dump files
> 
> **Rule:**  
> Must be emptied regularly or promoted.
> 
> ---
> 
> ### **99_ARCHIVE**
> Cold storage, frozen history.
> 
> - Closed cases
> - Old years
> - Decommissioned projects
> 
> **Rule:**  
> Read-only. No renames. No edits.
> 
> ---
> 
> ## 🔒 **NON-NEGOTIABLE GLOBAL RULES**
> These are what make this work as blob storage:
> 
> 1. **Roots never change**
> 2. **Meaning is below the root**
> 3. **Automation targets roots, humans target subfolders**
> 4. **Nothing lives directly at root level except these folders**
> 5. **Every object can move only “forward”**  
>    (INGEST → PRIMARY → WORKING/PUBLISH → ARCHIVE)
> 
> ---
> 
> ## 🧠 HOW THIS MAPS TO YOUR STACK (MENTAL MODEL)
> 
> - **Paperless consume** → `01_INGEST`
> - **Paperless canonical store** → `02_PRIMARY`
> - **QiNote active vault** → local + mirrored in `05_SYNC`
> - **Gina vector prep** → `07_EXPORTS`
> - **Court submission** → `04_PUBLISH`
> - **Nightly snapshots** → `06_BACKUP`
> 
> This is **cloud-provider-agnostic**. You could lift this straight into:
> - S3
> - Backblaze
> - Wasabi
> - Azure Blob
> 
> ---
> 
> ## 🛑 HARD TRUTH
> If you start with semantic folders at blob root, **automation will fight you forever**.  
> If you start with infrastructure roots, **meaning becomes portable and layered**.
> 
> You were right to call that out.
> 
> ---
> 
> ### Next options (pick one):
> - Define **subfolder conventions under 02_PRIMARY**
> - Create a **promotion SOP** (INGEST → PRIMARY → PUBLISH)
> - Map **Paperless + QiNote exports** into these roots
> - Design **checksum + immutability rules**
> - Create a **Drive hardening checklist** (sharing, permissions, retention)
> 
> Say the word and we’ll lock the next layer.

### User
> ok, yes, give me this in a ready to paste into google doc i will put at the root too, and where would the vaults go,

### Assistant
> Below is **ready-to-paste content for a Google Doc**. It is written as a **root-level system contract** for your blob storage. No markdown tricks, no code blocks required—this will paste cleanly and read correctly in Google Docs.
> 
> After the document, I answer **exactly where the vaults go** and why.
> 
> ---
> 
> # **Blob Storage Root Architecture & Governance**
> **Authoritative Storage Contract – Lock Once**
> 
> ## Purpose
> This document defines the **root-level infrastructure layout** for my Google Drive blob storage.  
> This Drive functions as **cold storage, authoritative backup, and provenance-safe mirror** for all systems (Paperless, QiNote, Gina, local vaults, exports, and court materials).
> 
> This is **not** a workspace and **not** a semantic document system.  
> Meaning is layered *below* these roots.
> 
> These root folders are **permanent and immutable**.
> 
> ---
> 
> ## Root Folder Index (LOCKED)
> 
> The Google Drive root MUST contain **only** the following folders:
> 
> ```
> 00_SYSTEM
> 01_INGEST
> 02_PRIMARY
> 03_WORKING
> 04_PUBLISH
> 05_SYNC
> 06_BACKUP
> 07_EXPORTS
> 08_SHARED
> 09_SCRATCH
> 99_ARCHIVE
> ```
> 
> No additional top-level folders are permitted.
> 
> ---
> 
> ## Root Folder Definitions & Rules
> 
> ### **00_SYSTEM — Control Plane**
> Purpose: System governance and documentation.
> 
> Contents:
> - Storage architecture docs (this file)
> - Taxonomies and schemas
> - SOPs
> - Automation configs
> - README explaining how the Drive is used
> 
> Rules:
> - Human-readable
> - Rare changes
> - No data objects
> 
> ---
> 
> ### **01_INGEST — Raw Intake (Untrusted)**
> Purpose: First-touch landing zone.
> 
> Contents:
> - Scans
> - Photos
> - Email attachments
> - External shares
> - USB or ad-hoc uploads
> 
> Rules:
> - Nothing here is trusted
> - Nothing stays long-term
> - Everything must move forward or be deleted
> - Mirrors Paperless “consume” behavior
> 
> ---
> 
> ### **02_PRIMARY — Canonical Objects**
> Purpose: The authoritative source of truth.
> 
> Contents:
> - Final PDFs
> - Source images
> - Original documents
> - Immutable evidence copies
> 
> Rules:
> - One canonical copy per object
> - No edits in place
> - New versions create new objects
> - Checksums preferred
> 
> ---
> 
> ### **03_WORKING — Active Manipulation**
> Purpose: Human work-in-progress.
> 
> Contents:
> - Drafts
> - Notes
> - Temporary reorganization
> - Assembly work
> 
> Rules:
> - Mess allowed
> - Permanence not allowed
> - Nothing here is final
> 
> ---
> 
> ### **04_PUBLISH — Outbound Deliverables**
> Purpose: Materials intended to leave the system.
> 
> Contents:
> - Court bundles
> - Submissions
> - Print-ready PDFs
> - Packages sent to third parties
> 
> Rules:
> - If it leaves the system, it came from here
> - No drafts
> - Final artifacts only
> 
> ---
> 
> ### **05_SYNC — System Mirrors**
> Purpose: Read-only mirrors of other systems.
> 
> Contents:
> - QiNote vault mirrors
> - Paperless exports
> - GitHub documentation mirrors
> - External system syncs
> 
> Rules:
> - Do not edit manually
> - Used for traceability and recovery
> 
> ---
> 
> ### **06_BACKUP — Redundant Safety Layer**
> Purpose: Disaster recovery.
> 
> Contents:
> - Zipped snapshots
> - Dated backups
> - Integrity-checked archives
> 
> Rules:
> - Append-only
> - Never edited
> - No manual cleanup
> 
> ---
> 
> ### **07_EXPORTS — Machine Outputs**
> Purpose: Generated artifacts.
> 
> Contents:
> - OCR text dumps
> - Vector prep files
> - CSV / JSON exports
> - Sidecar markdown files
> 
> Rules:
> - Re-creatable
> - Disposable
> - Script-owned
> 
> ---
> 
> ### **08_SHARED — Collaboration Zone**
> Purpose: Controlled sharing.
> 
> Contents:
> - Lawyer shares
> - Family shares
> - Client shares
> - Temporary access folders
> 
> Rules:
> - Nothing authoritative lives here
> - Assume others may modify contents
> 
> ---
> 
> ### **09_SCRATCH — Cognitive Relief Zone**
> Purpose: Temporary holding space.
> 
> Contents:
> - Brain dumps
> - “Put it here so I don’t lose it”
> - Temporary thinking artifacts
> 
> Rules:
> - Must be emptied regularly
> - Items are either promoted or deleted
> 
> ---
> 
> ### **99_ARCHIVE — Frozen History**
> Purpose: Cold storage.
> 
> Contents:
> - Closed cases
> - Old years
> - Decommissioned projects
> 
> Rules:
> - Read-only
> - No renames
> - No edits
> 
> ---
> 
> ## Global Storage Rules (Non-Negotiable)
> 
> 1. Root folders never change.
> 2. No files live directly at Drive root.
> 3. Meaning is applied below the root level.
> 4. Objects move only forward in lifecycle:
>    INGEST → PRIMARY → WORKING/PUBLISH → ARCHIVE
> 5. Automation targets roots; humans work inside subfolders.
> 
> ---
> 
> ## System Mapping Reference
> 
> - Paperless consume → 01_INGEST
> - Paperless canonical store → 02_PRIMARY
> - QiNote working vault → Local (mirrored only)
> - QiNote mirror → 05_SYNC
> - Gina vector prep → 07_EXPORTS
> - Court submissions → 04_PUBLISH
> - Nightly snapshots → 06_BACKUP
> 
> ---
> 
> ## This document is authoritative.
> If a future system conflicts with this structure, the system changes—not the structure.
> 
> ---
> 
> ---
> 
> ## **Now: Where the vaults go (this matters)**
> 
> ### **Local vaults (ACTIVE, WRITEABLE)**
> - **QiNote vault**
> - **Gina working indexes**
> - **Paperless runtime storage**
> 
> 👉 **These do NOT live in Google Drive.**  
> They live **locally** (SSD / workstation / server).
> 
> Why:
> - Performance
> - Locking
> - Avoid sync corruption
> - Deterministic automation
> 
> ---
> 
> ### **Google Drive vault mirrors (READ-ONLY)**
> Vaults are mirrored here:
> 
> ```
> /05_SYNC/QiNote_Vault_Mirror
> /05_SYNC/Paperless_Export_Mirror
> /Gina_Artifacts (if needed, under 05_SYNC or 07_EXPORTS)
> ```
> 
> Rules:
> - Mirrors only
> - Never edited
> - Used for recovery, audit, and redundancy
> 
> ---
> 
> ### **Canonical documents referenced by vaults**
> Final documents referenced by QiNote/Gina live in:
> 
> ```
> /02_PRIMARY/{domain}/{project}/{year}/...
> ```
> 
> Vaults **point to these**, they do not own them.
> 
> ---
> 
> ## Blunt truth (so you don’t second-guess later)
> If vaults live directly in Drive, you will eventually corrupt them.  
> If vaults are mirrored into Drive, you get safety without fragility.
> 
> This design is correct for **blob storage**, **automation**, **legal survivability**, and **future migration**.
> 
> ---
> 
> If you want next, I can:
> - Define **02_PRIMARY subfolder standards**
> - Create a **promotion SOP**
> - Map **Paperless exports exactly into these roots**
> - Design **checksum + immutability rules**
> - Draft a **Drive permissions hardening guide**
> 
> Say which layer you want to lock next.

### User
> an as for my qinoteos vault what folders should there be, we have admin, assets, cases, creative, kb, projects, sheets, sitess, working.

### Assistant
> Good — this is the **right moment** to lock the QiNoteOS vault. You already have the correct instincts; we just need to **tighten, normalize, and future-proof** it so it survives automation, vectorization, and your ADHD without friction.
> 
> Below is the **final, canonical QiNoteOS vault structure**, with **small but important corrections** to what you listed.
> 
> ---
> 
> ## ✅ **QiNoteOS Vault — Canonical Folder Map (LOCK THIS)**
> This is your **local-first, human-and-AI working vault**.
> 
> ```
> /00_ADMIN
> /01_ASSETS
> /02_CASES
> /03_PROJECTS
> /04_KB
> /05_CREATIVE
> /06_SHEETS
> /07_SITES
> /08_WORKING
> /99_ARCHIVE
> ```
> 
> Do not add siblings at the root. Do not rename later.
> 
> ---
> 
> ## 📁 FOLDER PURPOSE & HARD RULES
> 
> ### **00_ADMIN — Vault Control Plane**
> Purpose: How the vault itself works.
> 
> Contents:
> - Vault SOPs
> - Naming conventions
> - QiDecimal ID registry
> - Schema definitions
> - Index manifests
> - Automation configs
> 
> Rules:
> - Rare edits
> - No case or project content
> - No creative work
> 
> ---
> 
> ### **01_ASSETS — Reusable Building Blocks**
> Purpose: Shared components used across everything.
> 
> Contents:
> - Images
> - Icons
> - Logos
> - Diagrams
> - Templates
> - Boilerplate snippets
> 
> Rules:
> - Atomic files
> - No narrative
> - Referenced, not duplicated
> 
> ---
> 
> ### **02_CASES — Legal & Dispute Work**
> Purpose: Anything that could end up before a judge.
> 
> Contents:
> - Case narratives
> - Evidence maps
> - Hearing prep
> - Legal research
> - Cross-references to PRIMARY documents
> 
> Rules:
> - One folder per case
> - Case folders are immutable once closed
> - No raw PDFs here — references only
> 
> ---
> 
> ### **03_PROJECTS — Time-Bound Initiatives**
> Purpose: Things with a start and an end.
> 
> Contents:
> - Plans
> - Task breakdowns
> - Research
> - Interim notes
> 
> Rules:
> - Projects graduate to ARCHIVE or CASES
> - No permanent reference material
> 
> ---
> 
> ### **04_KB — Knowledge Base (Evergreen)**
> Purpose: Stable, reusable knowledge.
> 
> Contents:
> - Legal doctrines
> - System designs
> - How-tos
> - Personal frameworks
> - Reference notes
> 
> Rules:
> - Timeless
> - No tasks
> - No drafts
> 
> ---
> 
> ### **05_CREATIVE — Expression & Narrative**
> Purpose: Writing, storytelling, content.
> 
> Contents:
> - Books
> - Essays
> - Scripts
> - Reflections
> - Concept drafts
> 
> Rules:
> - Versioned
> - Mess allowed
> - Not authoritative documentation
> 
> ---
> 
> ### **06_SHEETS — Structured Data**
> Purpose: Tabular, numerical, or ledger-like material.
> 
> Contents:
> - CSV
> - TSV
> - Light spreadsheets
> - Data extracts
> - Logs
> 
> Rules:
> - No prose
> - No narrative
> - Optimized for machine use
> 
> ---
> 
> ### **07_SITES — Publishable Web Artifacts**
> Purpose: Things that compile into sites.
> 
> Contents:
> - Static site content
> - Docs sites
> - Landing pages
> - HTML / MD hybrids
> 
> Rules:
> - Source files only
> - Builds live elsewhere
> - Mirrors may exist in Drive under /04_PUBLISH
> 
> ---
> 
> ### **08_WORKING — Cognitive Sandbox**
> Purpose: Active thinking space.
> 
> Contents:
> - Daily notes
> - Scratch pads
> - Temporary groupings
> - In-progress reasoning
> 
> Rules:
> - Must be emptied regularly
> - No permanent storage
> - Promote or delete
> 
> ---
> 
> ### **99_ARCHIVE — Frozen Vault History**
> Purpose: Completed, closed, or deprecated work.
> 
> Contents:
> - Closed cases
> - Finished projects
> - Old creative drafts
> 
> Rules:
> - Read-only
> - No renames
> - No edits
> 
> ---
> 
> ## 🔁 HOW THIS MAPS TO YOUR BLOB STORAGE
> This vault is **not blob storage**.
> 
> - QiNoteOS lives **locally**
> - Google Drive mirrors appear under:
>   ```
>   /05_SYNC/QiNote_Vault_Mirror
>   ```
> - Canonical PDFs and images live in Drive `/02_PRIMARY`
> - QiNote references them by path + ID
> 
> ---
> 
> ## 🧠 ADHD-PROOFING RULES (IMPORTANT)
> These are survival rules:
> 
> 1. **If it’s permanent → not WORKING**
> 2. **If it’s legal → CASES**
> 3. **If it’s reusable → KB**
> 4. **If it’s expressive → CREATIVE**
> 5. **If it’s tabular → SHEETS**
> 6. **If you don’t know yet → WORKING**
> 
> Decide later. Don’t stall now.
> 
> ---
> 
> ## 🔒 FINAL LOCK
> Once you create these folders:
> - Do not rename
> - Do not add siblings
> - All automation assumes this layout forever
> 
> This structure is **clean, AI-friendly, legally defensible, and migration-safe**.
> 
> ---
> 
> ### Next layers (pick one):
> - File naming + QiDecimal ID enforcement
> - CASE folder internal structure (court-ready)
> - KB article template (YAML + sections)
> - Vector indexing scope rules
> - Daily WORKING → promotion ritual
> 
> Say which one and we’ll lock it.

### User
> I needthis document in .md

### Assistant
> Below is the **ready-to-save `.md` document** for your **QiNoteOS Vault Architecture**.  
> You can drop this directly into `00_ADMIN/QiNoteOS_Vault_Architecture.md`.
> 
> No fluff. This is the **authoritative contract**.
> 
> ---
> 
> ```markdown
> ---
> title: QiNoteOS Vault Architecture & Governance
> version: 1.0
> status: locked
> scope: local-first working vault
> last_updated: 2026-01-04
> ---
> 
> # QiNoteOS Vault Architecture & Governance
> 
> ## Purpose
> 
> This document defines the **canonical folder structure and governance rules** for the QiNoteOS vault.
> 
> QiNoteOS is a **local-first, human-and-AI working vault** used for:
> - Knowledge work
> - Case analysis
> - Creative development
> - Project execution
> - Vectorization inputs for Gina
> 
> QiNoteOS is **not blob storage** and **not a backup system**.  
> It references canonical documents stored elsewhere.
> 
> This structure is **locked**. Changes require a versioned migration plan.
> 
> ---
> 
> ## Root Folder Index (LOCKED)
> 
> The QiNoteOS vault root MUST contain **only** the following folders:
> 
> ```
> 00_ADMIN
> 01_ASSETS
> 02_CASES
> 03_PROJECTS
> 04_KB
> 05_CREATIVE
> 06_SHEETS
> 07_SITES
> 08_WORKING
> 99_ARCHIVE
> ```
> 
> No additional root-level folders are permitted.
> 
> ---
> 
> ## Folder Definitions & Rules
> 
> ### 00_ADMIN — Vault Control Plane
> 
> **Purpose:**  
> Defines how the vault itself operates.
> 
> **Contents:**
> - Vault SOPs
> - Naming conventions
> - QiDecimal ID registry
> - Schema definitions
> - Index manifests
> - Automation configuration files
> 
> **Rules:**
> - Rare edits
> - No case, project, or creative content
> - Governance only
> 
> ---
> 
> ### 01_ASSETS — Reusable Building Blocks
> 
> **Purpose:**  
> Shared, reusable components referenced across the vault.
> 
> **Contents:**
> - Images
> - Icons
> - Logos
> - Diagrams
> - Templates
> - Boilerplate snippets
> 
> **Rules:**
> - Atomic files only
> - No narrative documents
> - Referenced, not duplicated
> 
> ---
> 
> ### 02_CASES — Legal & Dispute Work
> 
> **Purpose:**  
> Anything that could reasonably appear in a legal proceeding.
> 
> **Contents:**
> - Case narratives
> - Evidence maps
> - Hearing preparation notes
> - Legal research
> - Cross-references to canonical documents
> 
> **Rules:**
> - One folder per case
> - No raw PDFs stored here
> - Case folders become immutable once closed
> 
> ---
> 
> ### 03_PROJECTS — Time-Bound Initiatives
> 
> **Purpose:**  
> Work with a defined beginning and end.
> 
> **Contents:**
> - Project plans
> - Task breakdowns
> - Research notes
> - Interim deliverables
> 
> **Rules:**
> - Projects eventually migrate to ARCHIVE or CASES
> - No evergreen reference material
> 
> ---
> 
> ### 04_KB — Knowledge Base (Evergreen)
> 
> **Purpose:**  
> Stable, reusable knowledge.
> 
> **Contents:**
> - Legal doctrine summaries
> - System designs
> - How-to guides
> - Personal frameworks
> - Reference notes
> 
> **Rules:**
> - Timeless content
> - No tasks
> - No drafts
> - Designed for long-term reuse and vectorization
> 
> ---
> 
> ### 05_CREATIVE — Expression & Narrative
> 
> **Purpose:**  
> Writing and creative output.
> 
> **Contents:**
> - Books
> - Essays
> - Scripts
> - Reflections
> - Concept drafts
> 
> **Rules:**
> - Versioned work allowed
> - Mess allowed
> - Not authoritative documentation
> 
> ---
> 
> ### 06_SHEETS — Structured Data
> 
> **Purpose:**  
> Tabular and machine-oriented data.
> 
> **Contents:**
> - CSV files
> - TSV files
> - Lightweight spreadsheets
> - Data extracts
> - Logs
> 
> **Rules:**
> - No prose
> - No narrative
> - Optimized for computation and analysis
> 
> ---
> 
> ### 07_SITES — Publishable Web Artifacts
> 
> **Purpose:**  
> Source content for websites and documentation sites.
> 
> **Contents:**
> - Static site content
> - Documentation source files
> - Landing page content
> - HTML / Markdown hybrids
> 
> **Rules:**
> - Source files only
> - Build outputs live elsewhere
> - Mirrors may exist in blob storage under publish roots
> 
> ---
> 
> ### 08_WORKING — Cognitive Sandbox
> 
> **Purpose:**  
> Active thinking and temporary workspace.
> 
> **Contents:**
> - Daily notes
> - Scratch pads
> - Temporary reasoning documents
> - In-progress analysis
> 
> **Rules:**
> - Nothing here is permanent
> - Must be regularly emptied
> - Promote or delete
> 
> ---
> 
> ### 99_ARCHIVE — Frozen Vault History
> 
> **Purpose:**  
> Completed and closed material.
> 
> **Contents:**
> - Closed cases
> - Finished projects
> - Deprecated creative drafts
> 
> **Rules:**
> - Read-only
> - No renames
> - No edits
> 
> ---
> 
> ## Global Vault Rules (Non-Negotiable)
> 
> 1. Root folders never change.
> 2. No files live directly at the vault root.
> 3. QiNoteOS is local-first; cloud mirrors are read-only.
> 4. Canonical documents live outside the vault.
> 5. Vault content references external documents by ID and path.
> 6. WORKING is temporary by definition.
> 7. ARCHIVE is immutable.
> 
> ---
> 
> ## System Mapping Reference
> 
> - Canonical documents → Blob storage `/02_PRIMARY`
> - QiNoteOS vault → Local filesystem
> - QiNoteOS mirror → Blob storage `/05_SYNC/QiNote_Vault_Mirror`
> - Vector prep outputs → Blob storage `/07_EXPORTS`
> - Published artifacts → Blob storage `/04_PUBLISH`
> 
> ---
> 
> ## Authoritative Statement
> 
> This document defines the **single source of truth** for QiNoteOS vault structure.
> 
> If a tool, script, or workflow conflicts with this structure,  
> **the tool changes — not the structure**.
> ```
> 
> ---
> 
> If you want next, I recommend (in order):
> 1. **CASE folder internal template** (court-ready)
> 2. **KB article template** (YAML + sections for vectorization)
> 3. **WORKING → promotion ritual** (ADHD-proof)
> 4. **QiDecimal ID enforcement rules**
> 
> Say which one and we’ll generate it in `.md` as well.

### User
> here is the message from gemini. I have completed the setup for Paperless-ngx and the QiNote export bridge. Since I cannot directly access your Docker daemon from this environment, I have prepared the configuration files locally so you can bring them up with a single command.

> 

> Phase 1: Run Paperless-ngx Locally

> I have created a local-deploy folder with the recommended PostgreSQL stack and your requested defaults (America/Chicago, OCR enabled, etc.).

> 

> 1. Bring up the stack Open your terminal (PowerShell or Bash) and run:

> 

> powershell

> cd local-deploy

> docker compose up -d

> 2. Create your Admin Account Once the containers are running, create your superuser:

> 

> powershell

> docker exec -it local-deploy-webserver-1 python3 manage.py createsuperuser

> 3. Access & Usage

> 

> URL: http://localhost:8000

> Consume Folder: Drop files into ./local-deploy/consume/ to start OCR processing.

> Data Persistence: Your documents and database are stored in Docker volumes managed by the stack.

> Verification Checklist:

> 

>  Log in at localhost:8000.

>  Drop a PDF into local-deploy/consume/.

>  Verify the document appears in the UI and is searchable via OCR text.

> Phase 2: QiNote Export Bridge

> I have created a standalone Python script in the qinote-bridge/ folder that monitors for documents tagged Ready_for_QiNote and exports them to a QiNote vault structure.

> 

> 1. Setup & Configuration In the qinote-bridge folder:

> 

> API Token: Go to My Profile in Paperless-ngx and generate an API Token.

> .env.bridge: Paste your token into PAPERLESS_TOKEN.

> 2. Install Script Dependencies

> 

> bash

> pip install requests python-dotenv

> 3. Run Export

> 

> bash

> python qinote-bridge/export_bridge.py

> Bridge Features:

> 

> Idempotent: Won't redownload or duplicate files already in the vault.

> Structure: Saves to qinote_vault/documents/{YYYY}/{YYYY-MM-DD}__title__paperless-{id}.pdf.

> Sidecar: Generates a .md file with YAML front matter including title, date, correspondent, and OCR text.

> Files Created/Modified

> Path	Description

> local-deploy/docker-compose.yml	Paperless-ngx + Postgres + Redis stack.

> local-deploy/docker-compose.env	Configured with your requested Timezone and OCR defaults.

> qinote-bridge/export_bridge.py	The Python bridge script.

> qinote-bridge/.env.bridge	Configuration for the bridge (URL, Token, Tag).

> qinote-bridge/BRIDGE_README.md	Detailed bridge usage instructions.

> Good

> Bad

> Good response , what from here to i give gemini about what we have set.

### Assistant
> Good — Gemini delivered **~80% of what you asked for**, and the remaining 20% is **critical alignment**, not more coding. Do **not** let Gemini keep “improving” things yet. You need to **lock assumptions and correct scope**.
> 
> Below is **exactly what to tell Gemini next**, followed by **what you should verify yourself before replying again**.
> 
> ---
> 
> ## ✅ FIRST: Your assessment (you were right)
> - ✅ Architecture choice is correct
> - ✅ Separation (Paperless core vs bridge) is correct
> - ⚠️ **Export target is WRONG for your system**
> - ⚠️ **Vault semantics are not aligned**
> - ⚠️ **Drive / blob contract not honored yet**
> 
> This is normal. Now we course-correct.
> 
> ---
> 
> ## 📣 WHAT TO TELL GEMINI (COPY / PASTE)
> 
> Paste **this entire message** to Gemini:
> 
> ```text
> Good work. Before any further changes, we need to ALIGN ON STORAGE CONTRACTS AND TARGETS.
> 
> IMPORTANT CORRECTIONS:
> 
> 1) The QiNoteOS vault is NOT a generic “documents” folder.
>    The canonical QiNoteOS vault root is:
> 
>    00_ADMIN
>    01_ASSETS
>    02_CASES
>    03_PROJECTS
>    04_KB
>    05_CREATIVE
>    06_SHEETS
>    07_SITES
>    08_WORKING
>    99_ARCHIVE
> 
>    Exported Paperless documents must NOT go to:
>    qinote_vault/documents/
> 
> 2) The export bridge target must be configurable and support TWO MODES:
> 
>    MODE A — Knowledge Reference (default):
>    - Export PDF to external canonical storage (blob / PRIMARY)
>    - Generate ONLY the Markdown sidecar inside QiNoteOS
>    - QiNoteOS stores references, not raw PDFs
> 
>    MODE B — Self-contained working copy (explicit):
>    - PDF + MD both placed under QiNoteOS/08_WORKING or a case folder
>    - Used only for temporary work
> 
> 3) The bridge MUST NOT assume QiNoteOS owns canonical files.
>    QiNoteOS references canonical documents by:
>    - paperless_id
>    - absolute or relative blob path
>    - checksum if available
> 
> 4) Update the bridge to:
>    - Support configurable TARGET_ROOT for exports
>    - Support mapping tags to QiNoteOS folders (e.g. CASE vs KB)
>    - Never write directly to Drive or blob storage
>    - Only write to QiNoteOS local vault or a local export staging folder
> 
> 5) Sidecar YAML MUST MATCH THIS SCHEMA (no extras, no omissions):
> 
>    ---
>    title:
>    paperless_id:
>    source: paperless-ngx
> 
>    document_type:
>    correspondent:
>    tags: []
> 
>    document_date:
>    date_received:
> 
>    project:
>    status:
>    confidence: primary_source
>    ---
> 
> NEXT DELIVERABLE:
> - Update export_bridge.py to support the above
> - Document the two export modes clearly
> - Do NOT add new features or refactor Paperless
> - Keep the bridge standalone and API-based
> 
> If any assumption is unclear, STOP and ask instead of guessing.
> ```
> 
> This **locks the system boundaries** and prevents future pain.
> 
> ---
> 
> ## 🧠 WHAT YOU SHOULD VERIFY LOCALLY (BEFORE NEXT ROUND)
> 
> Do these **now**, in this order:
> 
> ### 1️⃣ Bring Paperless up
> - `docker compose up -d`
> - Create superuser
> - Confirm:
>   - OCR works
>   - Search works
>   - Tagging works
>   - `Ready_for_QiNote` exists
> 
> If OCR/search doesn’t work, **stop everything** and fix that first.
> 
> ---
> 
> ### 2️⃣ Create ONE real test document
> - Drop a real scanned PDF
> - Add:
>   - Document Type
>   - Correspondent
>   - Tags (including `Ready_for_QiNote`)
> - Confirm metadata appears via API (this matters for the bridge)
> 
> ---
> 
> ### 3️⃣ Decide your default export mode (answer for yourself)
> Answer this question **before Gemini replies**:
> 
> > For now, do I want exported PDFs:
> > - A) kept OUTSIDE QiNoteOS (reference-only), or  
> > - B) copied INTO QiNoteOS for active work?
> 
> **Correct long-term answer:** A  
> **Acceptable short-term:** B (but explicitly temporary)
> 
> Tell Gemini which one is default.
> 
> ---
> 
> ## 🚫 WHAT NOT TO DO YET
> - ❌ Don’t wire Google Drive
> - ❌ Don’t add vectorization
> - ❌ Don’t add watchers or cron
> - ❌ Don’t add renaming logic beyond what exists
> 
> You are still **establishing invariants**.
> 
> ---
> 
> ## 🔒 THE CORE TRUTH (important)
> Gemini did not do anything *wrong* — it did what most engineers do:
> > “Export documents into the vault.”
> 
> Your system is **more advanced than that**:
> - Blob storage owns files
> - QiNote owns *meaning*
> - Gina owns *vectors*
> 
> Once Gemini understands this, the rest becomes clean.
> 
> ---
> 
> ## NEXT AFTER GEMINI RESPONDS
> Once Gemini updates the bridge:
> 1. We review **only**:
>    - Target paths
>    - YAML correctness
>    - Idempotency logic
> 2. Then we:
>    - Lock Paperless → PRIMARY routing
>    - Lock QiNote case folder templates
>    - Add **optional** Drive mirroring
> 
> If you want, paste Gemini’s **next response** and I’ll do a **line-by-line validation** before you touch anything.

### User
> what should my settings be there. Application Configuration 

> General Settings

> OCR Settings

> Barcode Settings

> Output Type 

> Language 

> Pages 

> Mode 

> Skip Archive File 

> Image DPI 

> Clean 

> Deskew 

> Enable  

> Rotate Pages 

> Enable  

> Rotate Pages Threshold 

> Max Image Pixels 

> Color Conversion Strategy 

> OCR Arguments

### Assistant
> Below is the **authoritative, copy-safe configuration** for **Paperless-ngx OCR settings**, tuned for **legal evidence, long-term searchability, and downstream vectorization**.  
> This is **not experimental**. These are conservative, court-safe defaults.
> 
> You can apply these in **Admin → Settings → OCR**.
> 
> ---
> 
> ## Application Configuration → OCR Settings (LOCK THESE)
> 
> ### **Output Type**
> **PDF/A-2b**
> 
> Why:
> - Archival-grade
> - Court-accepted
> - Stable for long-term storage
> - Preserves text layer cleanly
> 
> Do **not** use plain PDF unless you have a specific compatibility issue.
> 
> ---
> 
> ### **Language**
> **eng**
> 
> If you later need multilingual OCR:
> - Use `eng+spa` or similar
> - Do not over-enable languages prematurely (it hurts accuracy)
> 
> ---
> 
> ### **Pages**
> **All**
> 
> Never partial. Legal docs hide critical text in footers, headers, and appendices.
> 
> ---
> 
> ### **Mode**
> **Skip text if present**
> 
> Meaning:
> - If the PDF already has a text layer, don’t re-OCR
> - Prevents text corruption and duplicate layers
> 
> ---
> 
> ### **Skip Archive File**
> **Enabled**
> 
> Reason:
> - Avoids reprocessing already-archived docs
> - Prevents accidental mutation of evidence
> 
> ---
> 
> ### **Image DPI**
> **300**
> 
> This is the legal / OCR gold standard.
> 
> - 200 = borderline
> - 300 = optimal
> - 600 = overkill and slow
> 
> ---
> 
> ### **Clean**
> **Enabled**
> 
> Removes scanner noise and artifacts.
> Improves OCR accuracy without altering meaning.
> 
> ---
> 
> ### **Deskew**
> **Enabled**
> 
> Essential for:
> - Phone scans
> - Crooked certified mail receipts
> - Court stamps
> 
> ---
> 
> ### **Rotate Pages**
> **Enabled**
> 
> ---
> 
> ### **Rotate Pages Threshold**
> **45**
> 
> This prevents over-rotation on slightly tilted pages.
> 
> ---
> 
> ### **Max Image Pixels**
> **0** (unlimited)
> 
> Do NOT cap this unless you are memory-constrained.
> Courts sometimes send very large scanned exhibits.
> 
> ---
> 
> ### **Color Conversion Strategy**
> **Leave unchanged**
> 
> Why:
> - Preserves stamps, highlights, and annotations
> - Black-and-white conversion can destroy evidentiary markings
> 
> ---
> 
> ### **OCR Arguments**
> Leave **blank** initially.
> 
> Only add arguments if you later confirm a need (e.g. forcing layout modes).  
> Over-tuning Tesseract arguments usually *reduces* reliability.
> 
> ---
> 
> ## Barcode Settings (KEEP SIMPLE)
> 
> ### **Enable Barcode Detection**
> **Enabled**
> 
> Why:
> - Future-proofing
> - Some courts and agencies embed barcodes
> - No downside
> 
> Unless you actively rely on barcodes for routing, leave other barcode fields default.
> 
> ---
> 
> ## General OCR Philosophy (IMPORTANT)
> Your configuration prioritizes:
> 1. **Evidence integrity**
> 2. **Search accuracy**
> 3. **Vector-readiness**
> 4. **Archival safety**
> 
> Not:
> - File size minimization
> - Speed at the expense of accuracy
> - “AI enhancement” tricks
> 
> ---
> 
> ## One Hard Rule
> Once a document is:
> - OCR’d
> - Tagged
> - Exported
> - Referenced in QiNote
> 
> **You do not re-OCR it. Ever.**
> 
> If OCR is bad:
> - Create a **new version**
> - Keep the original immutable
> 
> This matters legally.
> 
> ---
> 
> ## Quick Sanity Test (DO THIS ONCE)
> After setting this:
> 1. Scan a crooked letter with stamps
> 2. Search for:
>    - A random word in the middle
>    - A footer line
>    - A handwritten note (if present)
> 3. Confirm:
>    - Search works
>    - Page orientation is correct
>    - Color markings remain
> 
> If that passes, you’re done.
> 
> ---
> 
> If you want next, I can:
> - Validate **General Settings** (non-OCR)
> - Give you **Paperless tag + document-type presets** aligned to QiNote
> - Define **what NOT to change ever**
> - Or review your **bridge YAML output against OCR reality**
> 
> Say which one.

### User
> Skip to content

> Paperless-ngx

> Configuration

> 

> 

> 

> logoPaperless-ngx

>  paperless-ngx/paperless-ngx

> v2.20.3

> 35.3k

> 2.2k

> Home

> Setup

> Basic Usage

> Configuration

> Table of contents

> Required services

> Redis Broker

> Database

> Optional Services

> Tika

> Email Parsing

> Paths and folders

> Logging

> Hosting & Security

> Authentication & SSO

> OCR settings

> Software tweaks

> Document Consumption

> Polling

> iNotify

> Workflow webhooks

> Incoming Mail

> Email OAuth

> Encrypted Emails

> Barcodes

> Audit Trail

> Collate Double-Sided Documents

> Trash

> Binaries

> Docker-specific options

> Frontend Settings

> Email sending

> Administration

> Advanced Topics

> REST API

> Development

> FAQs

> Troubleshooting

> Changelog

> Configuration

> Paperless provides a wide range of customizations. Depending on how you run paperless, these settings have to be defined in different places.

> 

> Certain configuration options may be set via the UI. This currently includes common OCR related settings and some frontend settings. If set, these will take preference over the settings via environment variables. If not set, the environment setting or applicable default will be utilized instead.

> 

> If you run paperless on docker, paperless.conf is not used. Rather, configure paperless by copying necessary options to docker-compose.env.

> 

> If you are running paperless on anything else, paperless will search for the configuration file in these locations and use the first one it finds:

> 

> The environment variable PAPERLESS_CONFIGURATION_PATH

> /path/to/paperless/paperless.conf

> /etc/paperless.conf

> /usr/local/etc/paperless.conf

> Required services

> Redis Broker

> PAPERLESS_REDIS=<url>

> This is required for processing scheduled tasks such as email fetching, index optimization and for training the automatic document matcher.

> 

> If your Redis server needs login credentials PAPERLESS_REDIS = redis://<username>:<password>@<host>:<port>

> With the requirepass option PAPERLESS_REDIS = redis://:<password>@<host>:<port>

> To include the redis database index PAPERLESS_REDIS = redis://<username>:<password>@<host>:<port>/<DBIndex>

> More information on securing your Redis Instance.

> 

> Defaults to redis://localhost:6379.

> 

> PAPERLESS_REDIS_PREFIX=<prefix>

> Prefix to be used in Redis for keys and channels. Useful for sharing one Redis server among multiple Paperless instances.

> 

> Defaults to no prefix.

> 

> Database

> By default, Paperless uses SQLite with a database stored at data/db.sqlite3. To switch to PostgreSQL or MariaDB, set PAPERLESS_DBHOST and optionally configure other database-related environment variables.

> 

> PAPERLESS_DBHOST=<hostname>

> If unset, Paperless uses SQLite by default.

> 

> Set PAPERLESS_DBHOST to switch to PostgreSQL or MariaDB instead.

> 

> PAPERLESS_DBENGINE=<engine_name>

> Optional. Specifies the database engine to use when connecting to a remote database. Available options are postgresql and mariadb.

> 

> Defaults to postgresql if PAPERLESS_DBHOST is set.

> 

> Warning

> 

> Using MariaDB comes with some caveats. See MySQL Caveats.

> 

> PAPERLESS_DBPORT=<port>

> Port to use when connecting to PostgreSQL or MariaDB.

> 

> Default is 5432 for PostgreSQL and 3306 for MariaDB.

> 

> PAPERLESS_DBNAME=<name>

> Name of the database to connect to when using PostgreSQL or MariaDB.

> 

> Defaults to "paperless".

> 

> PAPERLESS_DBUSER=<name>

> Username for authenticating with the PostgreSQL or MariaDB database.

> 

> Defaults to "paperless".

> 

> PAPERLESS_DBPASS=<password>

> Password for the PostgreSQL or MariaDB database user.

> 

> Defaults to "paperless".

> 

> PAPERLESS_DBSSLMODE=<mode>

> SSL mode to use when connecting to PostgreSQL or MariaDB.

> 

> See the official documentation about sslmode for PostgreSQL.

> 

> See the official documentation about sslmode for MySQL and MariaDB.

> 

> Note: SSL mode values differ between PostgreSQL and MariaDB.

> 

> Default is prefer for PostgreSQL and PREFERRED for MariaDB.

> 

> PAPERLESS_DBSSLROOTCERT=<ca-path>

> Path to the SSL root certificate used to verify the database server.

> 

> See the official documentation about sslmode for PostgreSQL. Changes the location of root.crt.

> 

> See the official documentation about sslmode for MySQL and MariaDB.

> 

> Defaults to unset, using the standard location in the home directory.

> 

> PAPERLESS_DBSSLCERT=<client-cert-path>

> Path to the client SSL certificate used when connecting securely.

> 

> See the official documentation about sslmode for PostgreSQL.

> 

> See the official documentation about sslmode for MySQL and MariaDB.

> 

> Changes the location of postgresql.crt.

> 

> Defaults to unset, using the standard location in the home directory.

> 

> PAPERLESS_DBSSLKEY=<client-cert-key>

> Path to the client SSL private key used when connecting securely.

> 

> See the official documentation about sslmode for PostgreSQL.

> 

> See the official documentation about sslmode for MySQL and MariaDB.

> 

> Changes the location of postgresql.key.

> 

> Defaults to unset, using the standard location in the home directory.

> 

> PAPERLESS_DB_TIMEOUT=<int>

> Sets how long a database connection should wait before timing out.

> 

> For SQLite, this sets how long to wait if the database is locked. For PostgreSQL or MariaDB, this sets the connection timeout.

> 

> Defaults to unset, which uses Django’s built-in defaults.

> 

> PAPERLESS_DB_POOLSIZE=<int>

> Defines the maximum number of database connections to keep in the pool.

> 

> Only applies to PostgreSQL. This setting is ignored for other database engines.

> 

> The value must be greater than or equal to 1 to be used. Defaults to unset, which disables connection pooling.

> 

> Note

> 

> A pool of 8-10 connections per worker is typically sufficient. If you encounter error messages such as couldn't get a connection or database connection timeouts, you probably need to increase the pool size.

> 

> Warning

> 

> Make sure your PostgreSQL max_connections setting is large enough to handle the connection pools: (NB_PAPERLESS_WORKERS + NB_CELERY_WORKERS) × POOL_SIZE + SAFETY_MARGIN. For example, with 4 Paperless workers and 2 Celery workers, and a pool size of 8:`(4 + 2) × 8 + 10 = 58, so max_connections = 60 (or even more) is appropriate.

> 

> This assumes only Paperless-ngx connects to your PostgreSQL instance. If you have other applications, you should increase max_connections accordingly.

> 

> PAPERLESS_DB_READ_CACHE_ENABLED=<bool>

> Caches the database read query results into Redis. This can significantly improve application response times by caching database queries, at the cost of slightly increased memory usage.

> 

> Defaults to false.

> 

> Danger

> 

> Do not modify the database outside the application while it is running. This includes actions such as restoring a backup, upgrading the database, or performing manual inserts. All external modifications must be done only when the application is stopped. After making any such changes, you must invalidate the DB read cache using the invalidate_cachalot management command.

> 

> PAPERLESS_READ_CACHE_TTL=<int>

> Specifies how long (in seconds) read data should be cached.

> 

> Allowed values are between 1 (one second) and 31536000 (one year). Defaults to 3600 (one hour).

> 

> Warning

> 

> A high TTL increases memory usage over time. Memory may be used until end of TTL, even if the cache is invalidated with the invalidate_cachalot command.

> 

> In case of an out-of-memory (OOM) situation, Redis may stop accepting new data — including cache entries, scheduled tasks, and documents to consume. If your system has limited RAM, consider configuring a dedicated Redis instance for the read cache, with a memory limit and the eviction policy set to allkeys-lru. For more details, refer to the Redis eviction policy documentation, and see the PAPERLESS_READ_CACHE_REDIS_URL setting to specify a separate Redis broker.

> 

> PAPERLESS_READ_CACHE_REDIS_URL=<url>

> Defines the Redis instance used for the read cache.

> 

> Defaults to None.

> 

> Note

> 

> If this value is not set, the same Redis instance used for scheduled tasks will be used for caching as well.

> 

> Optional Services

> Tika

> Paperless can make use of Tika and Gotenberg for parsing and converting "Office" documents (such as ".doc", ".xlsx" and ".odt"). Tika and Gotenberg are also needed to allow parsing of E-Mails (.eml).

> 

> If you wish to use this, you must provide a Tika server and a Gotenberg server, configure their endpoints, and enable the feature.

> 

> PAPERLESS_TIKA_ENABLED=<bool>

> Enable (or disable) the Tika parser.

> 

> Defaults to false.

> 

> PAPERLESS_TIKA_ENDPOINT=<url>

> Set the endpoint URL where Paperless can reach your Tika server.

> 

> Defaults to "http://localhost:9998".

> 

> PAPERLESS_TIKA_GOTENBERG_ENDPOINT=<url>

> Set the endpoint URL where Paperless can reach your Gotenberg server.

> 

> Defaults to "http://localhost:3000".

> 

> If you run paperless on docker, you can add those services to the Docker Compose file (see the provided docker-compose.sqlite-tika.yml file for reference).

> 

> Add all three configuration parameters to your configuration. If using Docker, this may be the environment key of the webserver or a docker-compose.env file. Bare metal installations may have a .conf file containing the configuration parameters. Be sure to use the correct format and watch out for indentation if editing the YAML file.

> 

> Email Parsing

> PAPERLESS_EMAIL_PARSE_DEFAULT_LAYOUT=<int>

> The default layout to use for emails that are consumed as documents. Must be one of the integer choices below. Note that mail rules can specify this setting, thus this fallback is used for the default selection and for .eml files consumed by other means.

> 

> 1 = Text, then HTML

> 2 = HTML, then text

> 3 = HTML only

> 4 = Text only

> Paths and folders

> PAPERLESS_CONSUMPTION_DIR=<path>

> This is where your documents should go to be consumed. Make sure that it exists and that the user running the paperless service can read/write its contents before you start Paperless.

> 

> Don't change this when using docker, as it only changes the path within the container. Change the local consumption directory in the docker-compose.yml file instead.

> 

> Defaults to "../consume/", relative to the "src" directory.

> 

> PAPERLESS_DATA_DIR=<path>

> This is where paperless stores all its data (search index, SQLite database, classification model, etc).

> 

> Defaults to "../data/", relative to the "src" directory.

> 

> PAPERLESS_EMPTY_TRASH_DIR=<path>

> When documents are deleted (e.g. after emptying the trash) the original files will be moved here instead of being removed from the filesystem. Only the original version is kept.

> 

> This must be writeable by the user running paperless. When running inside docker, ensure that this path is within a permanent volume (such as "../media/trash") so it won't get lost on upgrades.

> 

> Note that the directory must exist prior to using this setting.

> 

> Defaults to empty (i.e. really delete files).

> 

> This setting was previously named PAPERLESS_TRASH_DIR.

> 

> PAPERLESS_MEDIA_ROOT=<path>

> This is where your documents and thumbnails are stored.

> 

> You can set this and PAPERLESS_DATA_DIR to the same folder to have paperless store all its data within the same volume.

> 

> Defaults to "../media/", relative to the "src" directory.

> 

> PAPERLESS_STATICDIR=<path>

> Override the default STATIC_ROOT here. This is where all static files created using "collectstatic" manager command are stored.

> 

> Unless you're doing something fancy, there is no need to override this. If this is changed, you may need to run collectstatic again.

> 

> Defaults to "../static/", relative to the "src" directory.

> 

> PAPERLESS_FILENAME_FORMAT=<format>

> Changes the filenames paperless uses to store documents in the media directory. See File name handling for details.

> 

> Default is none, which disables this feature.

> 

> PAPERLESS_FILENAME_FORMAT_REMOVE_NONE=<bool>

> Tells paperless to replace placeholders in PAPERLESS_FILENAME_FORMAT that would resolve to 'none' to be omitted from the resulting filename. This also holds true for directory names. See File name handling for details.

> 

> Defaults to false which disables this feature.

> 

> PAPERLESS_LOGGING_DIR=<path>

> This is where paperless will store log files.

> 

> Defaults to PAPERLESS_DATA_DIR/log/.

> 

> PAPERLESS_NLTK_DIR=<path>

> This is where paperless will search for the data required for NLTK processing, if you are using it. If you are using the Docker image, this should not be changed, as the data is included in the image already.

> Previously, the location defaulted to PAPERLESS_DATA_DIR/nltk. Unless you are using this in a bare metal install or other setup, this folder is no longer needed and can be removed manually.

> 

> Defaults to /usr/share/nltk_data

> 

> PAPERLESS_MODEL_FILE=<path>

> This is where paperless will store the classification model.

> 

> Defaults to PAPERLESS_DATA_DIR/classification_model.pickle.

> 

> Logging

> PAPERLESS_LOGROTATE_MAX_SIZE=<num>

> Maximum file size for log files before they are rotated, in bytes.

> 

> Defaults to 1 MiB.

> 

> PAPERLESS_LOGROTATE_MAX_BACKUPS=<num>

> Number of rotated log files to keep.

> 

> Defaults to 20.

> 

> Hosting & Security

> PAPERLESS_SECRET_KEY=<key>

> Paperless uses this to make session tokens. If you expose paperless on the internet, you need to change this, since the default secret is well known.

> 

> Use any sequence of characters. The more, the better. You don't need to remember this. Just face-roll your keyboard.

> 

> Default is listed in the file src/paperless/settings.py.

> 

> PAPERLESS_URL=<url>

> This setting can be used to set the three options below (ALLOWED_HOSTS, CORS_ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS). If the other options are set the values will be combined with this one. Do not include a trailing slash. E.g. https://paperless.domain.com

> 

> Defaults to empty string, leaving the other settings unaffected.

> 

> Note

> 

> This value cannot contain a path (e.g. domain.com/path), even if you are installing paperless-ngx at a subpath.

> 

> PAPERLESS_CSRF_TRUSTED_ORIGINS=<comma-separated-list>

> A list of trusted origins for unsafe requests (e.g. POST). As of Django 4.0 this is required to access the Django admin via the web. See the Django project documentation on the settings

> 

> Can also be set using PAPERLESS_URL (see above).

> 

> Defaults to empty string, which does not add any origins to the trusted list.

> 

> PAPERLESS_ALLOWED_HOSTS=<comma-separated-list>

> If you're planning on putting Paperless on the open internet, then you really should set this value to the domain name you're using. Failing to do so leaves you open to HTTP host header attacks. You can read more about this in the Django project's documentation

> 

> Just remember that this is a comma-separated list, so "example.com" is fine, as is "example.com,www.example.com", but NOT " example.com" or "example.com,"

> 

> Can also be set using PAPERLESS_URL (see above).

> 

> "localhost" is always allowed for docker healthcheck

> 

> Defaults to "*", which is all hosts.

> 

> PAPERLESS_CORS_ALLOWED_HOSTS=<comma-separated-list>

> You need to add your servers to the list of allowed hosts that can do CORS calls. Set this to your public domain name.

> 

> Can also be set using PAPERLESS_URL (see above).

> 

> Defaults to "http://localhost:8000".

> 

> PAPERLESS_TRUSTED_PROXIES=<comma-separated-list>

> This may be needed to prevent IP address spoofing if you are using e.g. fail2ban with log entries for failed authorization attempts. Value should be IP address(es).

> 

> Defaults to empty string.

> 

> PAPERLESS_FORCE_SCRIPT_NAME=<path>

> To host paperless under a subpath url like example.com/paperless you set this value to /paperless. No trailing slash!

> 

> Defaults to none, which hosts paperless at "/".

> 

> PAPERLESS_STATIC_URL=<path>

> Override the STATIC_URL here. Unless you're hosting Paperless off a specific path like /paperless/, you probably don't need to change this. If you do change it, be sure to include the trailing slash.

> 

> Defaults to "/static/".

> 

> Note

> 

> When hosting paperless behind a reverse proxy like Traefik or Nginx at a subpath e.g. example.com/paperlessngx you will also need to set PAPERLESS_FORCE_SCRIPT_NAME (see above).

> 

> PAPERLESS_AUTO_LOGIN_USERNAME=<username>

> Specify a username here so that paperless will automatically perform login with the selected user.

> 

> Danger

> 

> Do not use this when exposing paperless on the internet. There are no checks in place that would prevent you from doing this.

> 

> Defaults to none, which disables this feature.

> 

> PAPERLESS_ADMIN_USER=<username>

> If this environment variable is specified, Paperless automatically creates a superuser with the provided username at start. This is useful in cases where you can not run the createsuperuser command separately, such as Kubernetes or AWS ECS.

> 

> Requires PAPERLESS_ADMIN_PASSWORD be set.

> 

> Note

> 

> This will not change an existing [super]user's password, nor will it recreate a user that already exists. You can leave this throughout the lifecycle of the containers.

> 

> PAPERLESS_ADMIN_MAIL=<email>

> (Optional) Specify superuser email address. Only used when PAPERLESS_ADMIN_USER is set.

> 

> Defaults to root@localhost.

> 

> PAPERLESS_ADMIN_PASSWORD=<password>

> Only used when PAPERLESS_ADMIN_USER is set. This will be the password of the automatically created superuser.

> PAPERLESS_COOKIE_PREFIX=<str>

> Specify a prefix that is added to the cookies used by paperless to identify the currently logged in user. This is useful for when you're running two instances of paperless on the same host.

> 

> After changing this, you will have to login again.

> 

> Defaults to "", which does not alter the cookie names.

> 

> PAPERLESS_ENABLE_HTTP_REMOTE_USER=<bool>

> Allows authentication via HTTP_REMOTE_USER which is used by some SSO applications.

> 

> Warning

> 

> This will allow authentication by simply adding a Remote-User: <username> header to a request. Use with care! You especially must ensure that any such header is not passed from external requests to your reverse-proxy to paperless (that would effectively bypass all authentication).

> 

> If you're exposing paperless to the internet directly (i.e. without a reverse proxy), do not use this.

> 

> Also see the warning in the official documentation.

> 

> Defaults to "false" which disables this feature.

> 

> PAPERLESS_ENABLE_HTTP_REMOTE_USER_API=<bool>

> Allows authentication via HTTP_REMOTE_USER directly against the API

> 

> Warning

> 

> See the warning above about securing your installation when using remote user header authentication. This setting is separate from PAPERLESS_ENABLE_HTTP_REMOTE_USER to avoid introducing a security vulnerability to existing reverse proxy setups. As above, ensure that your reverse proxy does not simply pass the Remote-User header from the internet to paperless.

> 

> Defaults to "false" which disables this feature.

> 

> PAPERLESS_HTTP_REMOTE_USER_HEADER_NAME=<str>

> If "PAPERLESS_ENABLE_HTTP_REMOTE_USER" or PAPERLESS_ENABLE_HTTP_REMOTE_USER_API are enabled, this property allows to customize the name of the HTTP header from which the authenticated username is extracted. Values are in terms of HttpRequest.META. Thus, the configured value must start with HTTP* followed by the normalized actual header name.

> 

> Defaults to "HTTP_REMOTE_USER".

> 

> PAPERLESS_LOGOUT_REDIRECT_URL=<str>

> URL to redirect the user to after a logout. This can be used together with PAPERLESS_ENABLE_HTTP_REMOTE_USER and SSO to redirect the user back to the SSO application's logout page to complete the logout process.

> 

> Defaults to None, which disables this feature.

> 

> PAPERLESS_USE_X_FORWARD_HOST=<bool>

> Configures the Django setting USE_X_FORWARDED_HOST which may be needed for hosting behind a proxy.

> 

> Defaults to False

> 

> PAPERLESS_USE_X_FORWARD_PORT=<bool>

> Configures the Django setting USE_X_FORWARDED_PORT which may be needed for hosting behind a proxy.

> 

> Defaults to False

> 

> PAPERLESS_PROXY_SSL_HEADER=<json-list>

> Configures the Django setting SECURE_PROXY_SSL_HEADER which may be needed for hosting behind a proxy. The two values in the list will form the tuple of HTTP header/value expected by Django, eg '["HTTP_X_FORWARDED_PROTO", "https"]'.

> 

> Defaults to None

> 

> Warning

> 

> Settings this value has security implications. Read the Django documentation and be sure you understand its usage before setting it.

> 

> PAPERLESS_EMAIL_CERTIFICATE_LOCATION=<path>

> Configures an additional SSL certificate file containing a certificate or certificate chain which should be trusted for validating SSL connections against mail providers. This is for use with self-signed certificates against local IMAP servers.

> 

> Defaults to None.

> 

> Warning

> 

> Settings this value has security implications for the security of your email. Understand what it does and be sure you need to before setting.

> 

> Authentication & SSO

> PAPERLESS_ACCOUNT_ALLOW_SIGNUPS=<bool>

> Allow users to signup for a new Paperless-ngx account.

> 

> Defaults to False

> 

> PAPERLESS_ACCOUNT_DEFAULT_GROUPS=<comma-separated-list>

> A list of group names that users will be added to when they sign up for a new account. Groups listed here must already exist.

> 

> Defaults to None

> 

> PAPERLESS_SOCIALACCOUNT_PROVIDERS=<json>

> This variable is used to setup login and signup via social account providers which are compatible with django-allauth. See the corresponding django-allauth documentation for a list of provider configurations. You will also need to include the relevant Django 'application' inside the PAPERLESS_APPS setting to activate that specific authentication provider (e.g. allauth.socialaccount.providers.openid_connect for the OIDC Connect provider).

> 

> Defaults to None, which does not enable any third party authentication systems.

> 

> PAPERLESS_SOCIAL_AUTO_SIGNUP=<bool>

> Attempt to signup the user using retrieved email, username etc from the third party authentication system. See the corresponding django-allauth documentation

> 

> Defaults to False

> 

> PAPERLESS_SOCIALACCOUNT_ALLOW_SIGNUPS=<bool>

> Allow users to signup for a new Paperless-ngx account using any setup third party authentication systems.

> 

> Defaults to True

> 

> PAPERLESS_SOCIAL_ACCOUNT_SYNC_GROUPS=<bool>

> Sync groups from the third party authentication system (e.g. OIDC) to Paperless-ngx. When enabled, users will be added or removed from groups based on their group membership in the third party authentication system. Groups must already exist in Paperless-ngx and have the same name as in the third party authentication system. Groups are updated upon logging in via the third party authentication system, see the corresponding django-allauth documentation.

> In order to pass groups from the authentication system you will need to update your PAPERLESS_SOCIALACCOUNT_PROVIDERS setting by adding a top-level "SCOPES" setting which includes "groups", e.g.:

> 

> {"openid_connect":{"SCOPE": ["openid","profile","email","groups"]...

> Defaults to False

> 

> PAPERLESS_SOCIAL_ACCOUNT_DEFAULT_GROUPS=<comma-separated-list>

> A list of group names that users who signup via social accounts will be added to upon signup. Groups listed here must already exist. If both the PAPERLESS_ACCOUNT_DEFAULT_GROUPS setting and this setting are used, the user will be added to both sets of groups.

> 

> Defaults to None

> 

> PAPERLESS_ACCOUNT_DEFAULT_HTTP_PROTOCOL=<string>

> The protocol used when generating URLs, e.g. login callback URLs. See the corresponding django-allauth documentation

> 

> Defaults to 'https'

> 

> PAPERLESS_ACCOUNT_EMAIL_VERIFICATION=<string>

> Determines whether email addresses are verified during signup (as performed by Django allauth). See the relevant paperless settings and the allauth docs

> 

> Defaults to 'optional'

> 

> Note

> 

> If you do not have a working email server set up this will be set to 'none'.

> 

> PAPERLESS_ACCOUNT_EMAIL_UNKNOWN_ACCOUNTS=<bool>

> See the relevant django-allauth documentation

> 

> Defaults to True (from allauth)

> 

> PAPERLESS_DISABLE_REGULAR_LOGIN=<bool>

> Disables the regular frontend username / password login, i.e. once you have setup SSO. Note that this setting does not disable the Django admin login nor logging in with local credentials via the API. To prevent access to the Django admin, consider blocking /admin/ in your web server or reverse proxy configuration.

> 

> You can optionally also automatically redirect users to the SSO login with PAPERLESS_REDIRECT_LOGIN_TO_SSO

> 

> Defaults to False

> 

> PAPERLESS_REDIRECT_LOGIN_TO_SSO=<bool>

> When this setting is enabled users will automatically be redirected (using javascript) to the first SSO provider login. You may still want to disable the frontend login form for clarity.

> 

> Defaults to False

> 

> PAPERLESS_ACCOUNT_SESSION_REMEMBER=<bool>

> If false, sessions will expire at browser close, if true will use PAPERLESS_SESSION_COOKIE_AGE for expiration. See the corresponding django-allauth documentation

> 

> Defaults to True

> 

> PAPERLESS_SESSION_COOKIE_AGE=<int>

> Login session cookie expiration. Applies if PAPERLESS_ACCOUNT_SESSION_REMEMBER is enabled. See the corresponding django documentation

> 

> Defaults to 1209600 (2 weeks)

> 

> OCR settings

> Paperless uses OCRmyPDF for performing OCR on documents and images. Paperless uses sensible defaults for most settings, but all of them can be configured to your needs.

> 

> PAPERLESS_OCR_LANGUAGE=<lang>

> Customize the language that paperless will attempt to use when parsing documents.

> 

> It should be a 3-letter code, see the list of languages Tesseract supports.

> 

> Set this to the language most of your documents are written in.

> 

> This can be a combination of multiple languages such as deu+eng, in which case Tesseract will use whatever language matches best. Keep in mind that Tesseract uses much more CPU time with multiple languages enabled.

> 

> If you are including languages that are not installed by default, you will need to also set PAPERLESS_OCR_LANGUAGES for docker deployments or install the tesseract language packages manually for bare metal installations.

> 

> Defaults to "eng".

> 

> Note

> 

> If your language contains a '-' such as chi-sim, you must use chi_sim.

> 

> PAPERLESS_OCR_MODE=<mode>

> Tell paperless when and how to perform ocr on your documents. Three modes are available:

> 

> skip: Paperless skips all pages and will perform ocr only on pages where no text is present. This is the safest option.

> 

> redo: Paperless will OCR all pages of your documents and attempt to replace any existing text layers with new text. This will be useful for documents from scanners that already performed OCR with insufficient results. It will also perform OCR on purely digital documents.

> 

> This option may fail on some documents that have features that cannot be removed, such as forms. In this case, the text from the document is used instead.

> 

> force: Paperless rasterizes your documents, converting any text into images and puts the OCRed text on top. This works for all documents, however, the resulting document may be significantly larger and text won't appear as sharp when zoomed in.

> 

> The default is skip, which only performs OCR when necessary and always creates archived documents.

> 

> Read more about this in the OCRmyPDF documentation.

> 

> PAPERLESS_OCR_SKIP_ARCHIVE_FILE=<mode>

> Specify when you would like paperless to skip creating an archived version of your documents. This is useful if you don't want to have two almost-identical versions of your documents in the media folder.

> 

> never: Never skip creating an archived version.

> with_text: Skip creating an archived version for documents that already have embedded text.

> always: Always skip creating an archived version.

> The default is never.

> 

> PAPERLESS_OCR_CLEAN=<mode>

> Tells paperless to use unpaper to clean any input document before sending it to tesseract. This uses more resources, but generally results in better OCR results. The following modes are available:

> 

> clean: Apply unpaper.

> clean-final: Apply unpaper, and use the cleaned images to build the output file instead of the original images.

> none: Do not apply unpaper.

> Defaults to clean.

> 

> Note

> 

> clean-final is incompatible with ocr mode redo. When both clean-final and the ocr mode redo is configured, clean is used instead.

> 

> PAPERLESS_OCR_DESKEW=<bool>

> Tells paperless to correct skewing (slight rotation of input images mainly due to improper scanning)

> 

> Defaults to true, which enables this feature.

> 

> Note

> 

> Deskewing is incompatible with ocr mode redo. Deskewing will get disabled automatically if redo is used as the ocr mode.

> 

> PAPERLESS_OCR_ROTATE_PAGES=<bool>

> Tells paperless to correct page rotation (90°, 180° and 270° rotation).

> 

> If you notice that paperless is not rotating incorrectly rotated pages (or vice versa), try adjusting the threshold up or down (see below).

> 

> Defaults to true, which enables this feature.

> 

> PAPERLESS_OCR_ROTATE_PAGES_THRESHOLD=<num>

> Adjust the threshold for automatic page rotation by PAPERLESS_OCR_ROTATE_PAGES. This is an arbitrary value reported by tesseract. "15" is a very conservative value, whereas "2" is a very aggressive option and will often result in correctly rotated pages being rotated as well.

> 

> Defaults to "12".

> 

> PAPERLESS_OCR_OUTPUT_TYPE=<type>

> Specify the the type of PDF documents that paperless should produce.

> 

> pdf: Modify the PDF document as little as possible.

> pdfa: Convert PDF documents into PDF/A-2b documents, which is a subset of the entire PDF specification and meant for storing documents long term.

> pdfa-1, pdfa-2, pdfa-3 to specify the exact version of PDF/A you wish to use.

> If not specified, pdfa is used. Remember that paperless also keeps the original input file as well as the archived version.

> 

> PAPERLESS_OCR_PAGES=<num>

> Tells paperless to use only the specified amount of pages for OCR. Documents with less than the specified amount of pages get OCR'ed completely.

> 

> Specifying 1 here will only use the first page.

> 

> The value must be greater than or equal to 1 to be used.

> 

> When combined with PAPERLESS_OCR_MODE=redo or PAPERLESS_OCR_MODE=force, paperless will not modify any text it finds on excluded pages and copy it verbatim.

> 

> Defaults to unset, which disables this feature and always uses all pages.

> 

> PAPERLESS_OCR_IMAGE_DPI=<num>

> Paperless will OCR any images you put into the system and convert them into PDF documents. This is useful if your scanner produces images. In order to do so, paperless needs to know the DPI of the image. Most images from scanners will have this information embedded and paperless will detect and use that information. In case this fails, it uses this value as a fallback.

> 

> Set this to the DPI your scanner produces images at.

> 

> Defaults to unset, which will automatically calculate image DPI so that the produced PDF documents are A4 sized.

> 

> PAPERLESS_OCR_MAX_IMAGE_PIXELS=<num>

> Paperless will raise a warning when OCRing images which are over this limit and will not OCR images which are more than twice this limit. Note this does not prevent the document from being consumed, but could result in missing text content.

> 

> If unset, will default to the value determined by Pillow.

> 

> Setting this value to 0 will entirely disable the limit. See the below warning.

> 

> Note

> 

> Increasing this limit could cause Paperless to consume additional resources when consuming a file. Be sure you have sufficient system resources.

> 

> Warning

> 

> The limit is intended to prevent malicious files from consuming system resources and causing crashes and other errors. Only change this value if you are certain your documents are not malicious and you need the text which was not OCRed

> 

> PAPERLESS_OCR_COLOR_CONVERSION_STRATEGY=<RGB>

> Controls the Ghostscript color conversion strategy when creating the archive file. This setting will only be utilized if the output is a version of PDF/A.

> 

> Valid options are CMYK, Gray, LeaveColorUnchanged, RGB or UseDeviceIndependentColor.

> 

> You can find more on the settings here in the Ghostscript documentation.

> 

> Warning

> 

> Utilizing some of the options may result in errors when creating archive files from PDFs.

> 

> PAPERLESS_OCR_USER_ARGS=<json>

> OCRmyPDF offers many more options. Use this parameter to specify any additional arguments you wish to pass to OCRmyPDF. Since Paperless uses the API of OCRmyPDF, you have to specify these in a format that can be passed to the API. See the API reference of OCRmyPDF for valid parameters. All command line options are supported, but they use underscores instead of dashes.

> 

> Warning

> 

> Paperless has been tested to work with the OCR options provided above. There are many options that are incompatible with each other, so specifying invalid options may prevent paperless from consuming any documents. Use with caution!

> 

> Specify arguments as a JSON dictionary. Keep note of lower case booleans and double quoted parameter names and strings. Examples:

> 

> {"deskew": true, "optimize": 3, "unpaper_args": "--pre-rotate 90"}

> Software tweaks

> PAPERLESS_TASK_WORKERS=<num>

> Paperless does multiple things in the background: Maintain the search index, maintain the automatic matching algorithm, check emails, consume documents, etc. This variable specifies how many things it will do in parallel.

> 

> Defaults to 1

> 

> PAPERLESS_THREADS_PER_WORKER=<num>

> Furthermore, paperless uses multiple threads when consuming documents to speed up OCR. This variable specifies how many pages paperless will process in parallel on a single document.

> 

> Warning

> 

> Ensure that the product

> 

> PAPERLESS_TASK_WORKERS * PAPERLESS_THREADS_PER_WORKER

> 

> does not exceed your CPU core count or else paperless will be extremely slow. If you want paperless to process many documents in parallel, choose a high worker count. If you want paperless to process very large documents faster, use a higher thread per worker count.

> 

> If unset, paperless uses max(floor(cpu_count / PAPERLESS_TASK_WORKERS), 1) threads per worker. The idea behind this is that as long as there are enough cores, the total number of threads should less than or equal to the total number of (logical) CPU cores.

> 

> PAPERLESS_WORKER_TIMEOUT=<num>

> Machines with few cores or weak ones might not be able to finish OCR on large documents within the default 1800 seconds. So extending this timeout may prove to be useful on weak hardware setups.

> PAPERLESS_TIME_ZONE=<timezone>

> Set the time zone here. See more details on why and how to set it in the Django project documentation for details on how to set it.

> 

> Defaults to UTC.

> 

> PAPERLESS_ENABLE_NLTK=<bool>

> Enables or disables the advanced natural language processing used during automatic classification. If disabled, paperless will still perform some basic text pre-processing before matching.

> See also PAPERLESS_NLTK_DIR.

> 

> Defaults to true, enabling the feature.

> 

> PAPERLESS_DATE_PARSER_LANGUAGES=<lang>

> Specifies which language Paperless should use when parsing dates from documents.

> 

> This should be a language code supported by the dateparser library,

> for example: "en", or a combination such as "en+de".

> Locales are also supported (e.g., "en-AU").

> Multiple languages can be combined using "+", for example: "en+de" or "en-AU+de".

> For valid values, refer to the list of supported languages and locales in the [dateparser documentation](https://dateparser.readthedocs.io/en/latest/supported_locales.html).

> 

> Set this to match the languages in which most of your documents are written.

> If not set, Paperless will attempt to infer the language(s) from the OCR configuration (`PAPERLESS_OCR_LANGUAGE`).

> Note

> 

> This format differs from the PAPERLESS_OCR_LANGUAGE setting, which uses ISO 639-2 codes (3 letters, e.g., "eng+deu" for Tesseract OCR).

> 

> PAPERLESS_EMAIL_TASK_CRON=<cron expression>

> Configures the scheduled email fetching frequency. The value should be a valid crontab(5) expression describing when to run.

> If set to the string "disable", no emails will be fetched automatically.

> 

> Defaults to */10 * * * * or every ten minutes.

> 

> PAPERLESS_TRAIN_TASK_CRON=<cron expression>

> Configures the scheduled automatic classifier training frequency. The value should be a valid crontab(5) expression describing when to run.

> If set to the string "disable", the classifier will not be trained automatically.

> 

> Defaults to 5 */1 * * * or every hour at 5 minutes past the hour.

> 

> PAPERLESS_INDEX_TASK_CRON=<cron expression>

> Configures the scheduled search index update frequency. The value should be a valid crontab(5) expression describing when to run.

> If set to the string "disable", the search index will not be automatically updated.

> 

> Defaults to 0 0 * * * or daily at midnight.

> 

> PAPERLESS_SANITY_TASK_CRON=<cron expression>

> Configures the scheduled sanity checker frequency. The value should be a valid crontab(5) expression describing when to run.

> If set to the string "disable", the sanity checker will not run automatically.

> 

> Defaults to 30 0 * * sun or Sunday at 30 minutes past midnight.

> 

> PAPERLESS_WORKFLOW_SCHEDULED_TASK_CRON=<cron expression>

> Configures the scheduled workflow check frequency. The value should be a valid crontab(5) expression describing when to run.

> If set to the string "disable", scheduled workflows will not run.

> 

> Defaults to 5 */1 * * * or every hour at 5 minutes past the hour.

> 

> PAPERLESS_ENABLE_COMPRESSION=<bool>

> Enables compression of the responses from the webserver.

> Defaults to true, enabling compression.

> 

> Note

> 

> If you are using a proxy such as nginx, it is likely more efficient to enable compression in your proxy configuration rather than the webserver

> 

> PAPERLESS_CONVERT_MEMORY_LIMIT=<num>

> On smaller systems, or even in the case of Very Large Documents, the consumer may explode, complaining about how it's "unable to extend pixel cache". In such cases, try setting this to a reasonably low value, like 32. The default is to use whatever is necessary to do everything without writing to disk, and units are in megabytes.

> 

> For more information on how to use this value, you should search the web for "MAGICK_MEMORY_LIMIT".

> 

> Defaults to 0, which disables the limit.

> 

> PAPERLESS_CONVERT_TMPDIR=<path>

> Similar to the memory limit, if you've got a small system and your OS mounts /tmp as tmpfs, you should set this to a path that's on a physical disk, like /home/your_user/tmp or something. ImageMagick will use this as scratch space when crunching through very large documents.

> 

> For more information on how to use this value, you should search the web for "MAGICK_TMPDIR".

> 

> Default is none, which disables the temporary directory.

> 

> PAPERLESS_APPS=<string>

> A comma-separated list of Django apps to be included in Django's INSTALLED_APPS. This setting should be used with caution!

> 

> Defaults to None, which does not add any additional apps.

> 

> PAPERLESS_MAX_IMAGE_PIXELS=<number>

> Configures the maximum size of an image PIL will allow to load without warning or error.

> If unset, will default to the value determined by Pillow.

> 

> Defaults to None, which does change the limit

> 

> Warning

> 

> This limit is designed to prevent denial of service from malicious files. It should only be raised or disabled in certain circumstances and with great care.

> 

> Document Consumption

> PAPERLESS_CONSUMER_DISABLE

> If set (to anything), this completely disables the directory-based consumer in docker. If you don't plan to consume documents via the consumption directory, you can disable the consumer to save resources.

> PAPERLESS_CONSUMER_DELETE_DUPLICATES=<bool>

> When the consumer detects a duplicate document, it will not touch the original document. This default behavior can be changed here.

> 

> Defaults to false.

> 

> PAPERLESS_CONSUMER_RECURSIVE=<bool>

> Enable recursive watching of the consumption directory. Paperless will then pickup files from files in subdirectories within your consumption directory as well.

> 

> Defaults to false.

> 

> PAPERLESS_CONSUMER_SUBDIRS_AS_TAGS=<bool>

> Set the names of subdirectories as tags for consumed files. E.g. <CONSUMPTION_DIR>/foo/bar/file.pdf will add the tags "foo" and "bar" to the consumed file. Paperless will create any tags that don't exist yet.

> 

> This is useful for sorting documents with certain tags such as car or todo prior to consumption. These folders won't be deleted.

> 

> PAPERLESS_CONSUMER_RECURSIVE must be enabled for this to work.

> 

> Defaults to false.

> 

> PAPERLESS_CONSUMER_IGNORE_PATTERNS=<json>

> By default, paperless ignores certain files and folders in the consumption directory, such as system files created by the Mac OS or hidden folders some tools use to store data.

> 

> This can be adjusted by configuring a custom json array with patterns to exclude.

> 

> For example, .DS_STORE/* will ignore any files found in a folder named .DS_STORE, including .DS_STORE/bar.pdf and foo/.DS_STORE/bar.pdf

> 

> A pattern like ._* will ignore anything starting with ._, including: ._foo.pdf and ._bar/foo.pdf

> 

> Defaults to [".DS_Store", ".DS_STORE", "._*", ".stfolder/*", ".stversions/*", ".localized/*", "desktop.ini", "@eaDir/*", "Thumbs.db"].

> 

> PAPERLESS_CONSUMER_BARCODE_SCANNER=<string>

> Sets the barcode scanner used for barcode functionality.

> 

> Currently, "PYZBAR" (the default) or "ZXING" might be selected. If you have problems that your Barcodes/QR-Codes are not detected (especially with bad scan quality and/or small codes), try the other one.

> 

> PAPERLESS_PRE_CONSUME_SCRIPT=<filename>

> After some initial validation, Paperless can trigger an arbitrary script if you like before beginning consumption. This script will be provided data for it to work with via the environment.

> 

> For more information, take a look at pre-consumption script.

> 

> The default is blank, which means nothing will be executed.

> 

> PAPERLESS_POST_CONSUME_SCRIPT=<filename>

> After a document is consumed, Paperless can trigger an arbitrary script if you like. This script will be provided data for it to work with via the environment.

> 

> For more information, take a look at Post-consumption script.

> 

> The default is blank, which means nothing will be executed.

> 

> PAPERLESS_FILENAME_DATE_ORDER=<format>

> Paperless will check the document text for document date information. Use this setting to enable checking the document filename for date information. The date order can be set to any option as specified in https://dateparser.readthedocs.io/en/latest/settings.html#date-order. The filename will be checked first, and if nothing is found, the document text will be checked as normal.

> 

> A date in a filename must have some separators (., ,, -, /, etc) for it to be parsed.

> 

> Defaults to none, which disables this feature.

> 

> PAPERLESS_NUMBER_OF_SUGGESTED_DATES=<num>

> Paperless searches an entire document for dates. The first date found will be used as the initial value for the created date. When this variable is greater than 0 (or left to its default value), paperless will also suggest other dates found in the document, up to a maximum of this setting. Note that duplicates will be removed, which can result in fewer dates displayed in the frontend than this setting value.

> 

> The task to find all dates can be time-consuming and increases with a higher (maximum) number of suggested dates and slower hardware.

> 

> Defaults to 3. Set to 0 to disable this feature.

> 

> PAPERLESS_THUMBNAIL_FONT_NAME=<filename>

> Paperless creates thumbnails for plain text files by rendering the content of the file on an image and uses a predefined font for that. This font can be changed here.

> 

> Note that this won't have any effect on already generated thumbnails.

> 

> Defaults to /usr/share/fonts/liberation/LiberationSerif-Regular.ttf.

> 

> PAPERLESS_IGNORE_DATES=<string>

> Paperless parses a document's creation date from filename and file content. You may specify a comma separated list of dates that should be ignored during this process. This is useful for special dates (like date of birth) that appear in documents regularly but are very unlikely to be the document's creation date.

> 

> The date is parsed using the order specified in PAPERLESS_DATE_ORDER

> 

> Defaults to an empty string to not ignore any dates.

> 

> PAPERLESS_DATE_ORDER=<format>

> Paperless will try to determine the document creation date from its contents. Specify the date format Paperless should expect to see within your documents.

> 

> This option defaults to DMY which translates to day first, month second, and year last order. Characters D, M, or Y can be shuffled to meet the required order.

> 

> PAPERLESS_ENABLE_GPG_DECRYPTOR=<bool>

> Enable or disable the GPG decryptor for encrypted emails. See GPG Decryptor for more information.

> 

> Defaults to false.

> 

> Polling

> PAPERLESS_CONSUMER_POLLING=<num>

> If paperless won't find documents added to your consume folder, it might not be able to automatically detect filesystem changes. In that case, specify a polling interval in seconds here, which will then cause paperless to periodically check your consumption directory for changes. This will also disable listening for file system changes with inotify.

> 

> Defaults to 0, which disables polling and uses filesystem notifications.

> 

> PAPERLESS_CONSUMER_POLLING_RETRY_COUNT=<num>

> If consumer polling is enabled, sets the maximum number of times paperless will check for a file to remain unmodified. If a file's modification time and size are identical for two consecutive checks, it will be consumed.

> 

> Defaults to 5.

> 

> PAPERLESS_CONSUMER_POLLING_DELAY=<num>

> If consumer polling is enabled, sets the delay in seconds between each check (above) paperless will do while waiting for a file to remain unmodified.

> 

> Defaults to 5.

> 

> iNotify

> PAPERLESS_CONSUMER_INOTIFY_DELAY=<num>

> Sets the time in seconds the consumer will wait for additional events from inotify before the consumer will consider a file ready and begin consumption. Certain scanners or network setups may generate multiple events for a single file, leading to multiple consumers working on the same file. Configure this to prevent that.

> 

> Defaults to 0.5 seconds.

> 

> Workflow webhooks

> PAPERLESS_WEBHOOKS_ALLOWED_SCHEMES=<str>

> A comma-separated list of allowed schemes for webhooks. This setting controls which URL schemes are permitted for webhook URLs.

> 

> Defaults to http,https.

> 

> PAPERLESS_WEBHOOKS_ALLOWED_PORTS=<str>

> A comma-separated list of allowed ports for webhooks. This setting controls which ports are permitted for webhook URLs. For example, if you set this to 80,443, webhooks will only be sent to URLs that use these ports.

> 

> Defaults to empty list, which allows all ports.

> 

> PAPERLESS_WEBHOOKS_ALLOW_INTERNAL_REQUESTS=<bool>

> If set to false, webhooks cannot be sent to internal URLs (e.g., localhost).

> 

> Defaults to true, which allows internal requests.

> 

> Incoming Mail

> Email OAuth

> PAPERLESS_OAUTH_CALLBACK_BASE_URL=<str>

> The base URL for the OAuth callback. This is used to construct the full URL for the OAuth callback. This should be the URL that the Paperless instance is accessible at. If not set, defaults to the PAPERLESS_URL setting. At least one of these settings must be set to enable OAuth Email setup.

> 

> Defaults to none (thus will use PAPERLESS_URL).

> 

> Note

> 

> This setting only applies to OAuth Email setup (not to the SSO setup).

> 

> PAPERLESS_GMAIL_OAUTH_CLIENT_ID=<str>

> The OAuth client ID for Gmail. This is required for Gmail OAuth Email setup. See OAuth Email Setup for more information.

> 

> Defaults to none.

> 

> PAPERLESS_GMAIL_OAUTH_CLIENT_SECRET=<str>

> The OAuth client secret for Gmail. This is required for Gmail OAuth Email setup. See OAuth Email Setup for more information.

> 

> Defaults to none.

> 

> PAPERLESS_OUTLOOK_OAUTH_CLIENT_ID=<str>

> The OAuth client ID for Outlook. This is required for Outlook OAuth Email setup. See OAuth Email Setup for more information.

> 

> Defaults to none.

> 

> PAPERLESS_OUTLOOK_OAUTH_CLIENT_SECRET=<str>

> The OAuth client secret for Outlook. This is required for Outlook OAuth Email setup. See OAuth Email Setup for more information.

> 

> Defaults to none.

> 

> Encrypted Emails

> PAPERLESS_EMAIL_GNUPG_HOME=<str>

> Optional, sets the GNUPG_HOME path to use with GPG decryptor for encrypted emails. See GPG Decryptor for more information. If not set, defaults to the default GNUPG_HOME path.

> 

> Defaults to .

> 

> Barcodes

> PAPERLESS_CONSUMER_ENABLE_BARCODES=<bool>

> Enables the scanning and page separation based on detected barcodes. This allows for scanning and adding multiple documents per uploaded file, which are separated by one or multiple barcode pages.

> 

> For ease of use, it is suggested to use a standardized separation page, e.g. here.

> 

> If no barcodes are detected in the uploaded file, no page separation will happen.

> 

> The original document will be removed and the separated pages will be saved as pdf.

> 

> See additional information in the advanced usage documentation

> 

> Defaults to false.

> 

> PAPERLESS_CONSUMER_BARCODE_TIFF_SUPPORT=<bool>

> Whether TIFF image files should be scanned for barcodes. This will automatically convert any TIFF image(s) to pdfs for later processing. This only has an effect, if PAPERLESS_CONSUMER_ENABLE_BARCODES has been enabled.

> 

> Defaults to false.

> 

> PAPERLESS_CONSUMER_BARCODE_STRING=<string>

> Defines the string to be detected as a separator barcode. If paperless is used with the PATCH-T separator pages, users shouldn't change this.

> 

> Defaults to "PATCHT"

> 

> PAPERLESS_CONSUMER_BARCODE_RETAIN_SPLIT_PAGES=<bool>

> If set to true, all pages that are split by a barcode (such as PATCHT) will be kept.

> 

> Defaults to false.

> 

> PAPERLESS_CONSUMER_ENABLE_ASN_BARCODE=<bool>

> Enables the detection of barcodes in the scanned document and setting the ASN (archive serial number) if a properly formatted barcode is detected.

> 

> The barcode must consist of a (configurable) prefix and the ASN to be set, for instance ASN00123. The content after the prefix is cleaned of non-numeric characters.

> 

> This option is compatible with barcode page separation, since pages will be split up before reading the ASN.

> 

> If no ASN barcodes are detected in the uploaded file, no ASN will be set. If a barcode with an existing ASN is detected, the document will not be consumed and an error logged.

> 

> Defaults to false.

> 

> PAPERLESS_CONSUMER_ASN_BARCODE_PREFIX=<string>

> Defines the prefix that is used to identify a barcode as an ASN barcode.

> 

> Defaults to "ASN"

> 

> PAPERLESS_CONSUMER_BARCODE_UPSCALE=<float>

> Defines the upscale factor used in barcode detection. Improves the detection of small barcodes, i.e. with a value of 1.5 by upscaling the document before the detection process. Upscaling will only take place if value is bigger than 1.0. Otherwise upscaling will not be performed to save resources. Try using in combination with PAPERLESS_CONSUMER_BARCODE_DPI set to a value higher than default.

> 

> Defaults to 0.0

> 

> PAPERLESS_CONSUMER_BARCODE_DPI=<int>

> During barcode detection every page from a PDF document needs to be converted to an image. A dpi value can be specified in the conversion process. Default is 300. If the detection of small barcodes fails a bigger dpi value i.e. 600 can fix the issue. Try using in combination with PAPERLESS_CONSUMER_BARCODE_UPSCALE bigger than 1.0.

> 

> Defaults to "300"

> 

> PAPERLESS_CONSUMER_BARCODE_MAX_PAGES=<int>

> Because barcode detection is a computationally-intensive operation, this setting limits the detection of barcodes to a number of first pages. If your scanner has a limit for the number of pages that can be scanned it would be sensible to set this as the limit here.

> 

> Defaults to "0", allowing all pages to be checked for barcodes.

> 

> PAPERLESS_CONSUMER_ENABLE_TAG_BARCODE=<bool>

> Enables the detection of barcodes in the scanned document and assigns or creates tags if a properly formatted barcode is detected.

> 

> The barcode must match one of the (configurable) regular expressions. If the barcode text contains ',' (comma), it is split into multiple barcodes which are individually processed for tagging.

> 

> Matching is case insensitive.

> 

> Defaults to false.

> 

> PAPERLESS_CONSUMER_TAG_BARCODE_MAPPING=<json dict>

> Defines a dictionary of filter regex and substitute expressions.

> 

> Syntax: {"<regex>": "<substitute>" [,...]]}

> 

> A barcode is considered for tagging if the barcode text matches at least one of the provided pattern.

> 

> If a match is found, the rule is applied. This allows very versatile reformatting and mapping of barcode pattern to tag values.

> 

> If a tag is not found it will be created.

> 

> Defaults to:

> 

> {"TAG:(.*)": "\\g<1>"} which defines - a regex TAG:(.*) which includes barcodes beginning with TAG: followed by any text that gets stored into match group #1 and - a substitute \\g<1> that replaces the original barcode text by the content in match group #1. Consequently, the tag is the barcode text without its TAG: prefix.

> 

> More examples:

> 

> {"ASN12.*": "JOHN", "ASN13.*": "SMITH"} for example maps - ASN12nnnn barcodes to the tag JOHN and - ASN13nnnn barcodes to the tag SMITH.

> 

> {"T-J": "JOHN", "T-S": "SMITH", "T-D": "DOE"} directly maps - T-J barcodes to the tag JOHN, - T-S barcodes to the tag SMITH and - T-D barcodes to the tag DOE.

> 

> Please refer to the Python regex documentation for more information.

> 

> Audit Trail

> PAPERLESS_AUDIT_LOG_ENABLED=<bool>

> Enables the audit trail for documents, document types, correspondents, and tags.

> 

> Defaults to true.

> 

> Collate Double-Sided Documents

> PAPERLESS_CONSUMER_ENABLE_COLLATE_DOUBLE_SIDED=<bool>

> Enables automatic collation of two single-sided scans into a double-sided document.

> 

> This is useful if you have an automatic document feeder that only supports single-sided scans, but you need to scan a double-sided document. If your ADF supports double-sided scans natively, you do not need this feature.

> 

> PAPERLESS_CONSUMER_RECURSIVE must be enabled for this to work.

> 

> For more information, read the corresponding section in the advanced documentation.

> 

> Defaults to false.

> 

> PAPERLESS_CONSUMER_COLLATE_DOUBLE_SIDED_SUBDIR_NAME=<str>

> The name of the subdirectory that the collate feature expects documents to arrive.

> 

> This only has an effect if PAPERLESS_CONSUMER_ENABLE_COLLATE_DOUBLE_SIDED has been enabled. Note that Paperless will not automatically create the directory.

> 

> Defaults to "double-sided".

> 

> PAPERLESS_CONSUMER_COLLATE_DOUBLE_SIDED_TIFF_SUPPORT=<bool>

> Whether TIFF image files should be supported when collating documents. This will automatically convert any TIFF image(s) to pdfs for later processing. This only has an effect if PAPERLESS_CONSUMER_ENABLE_COLLATE_DOUBLE_SIDED has been enabled.

> 

> Defaults to false.

> 

> Trash

> PAPERLESS_EMPTY_TRASH_DELAY=<num>

> Sets how long in days documents remain in the 'trash' before they are permanently deleted.

> 

> Defaults to 30 days, minimum of 1 day.

> 

> PAPERLESS_EMPTY_TRASH_TASK_CRON=<cron expression>

> Configures the schedule to empty the trash of expired deleted documents.

> 

> Defaults to 0 1 * * *, once per day.

> 

> Binaries

> There are a few external software packages that Paperless expects to find on your system when it starts up. Unless you've done something creative with their installation, you probably won't need to edit any of these. However, if you've installed these programs somewhere where simply typing the name of the program doesn't automatically execute it (ie. the program isn't in your $PATH), then you'll need to specify the literal path for that program.

> 

> PAPERLESS_CONVERT_BINARY=<path>

> Defaults to "convert".

> PAPERLESS_GS_BINARY=<path>

> Defaults to "gs".

> Docker-specific options

> These options don't have any effect in paperless.conf. These options adjust the behavior of the docker container. Configure these in docker-compose.env.

> 

> PAPERLESS_WEBSERVER_WORKERS=<num>

> The number of worker processes the webserver should spawn. More worker processes usually result in the front end to load data much quicker. However, each worker process also loads the entire application into memory separately, so increasing this value will increase RAM usage.

> 

> Defaults to 1.

> 

> Note

> 

> This option may also be set with GRANIAN_WORKERS and this option may be removed in the future

> 

> PAPERLESS_BIND_ADDR=<ip address>

> The IP address the webserver will listen on inside the container. There are special setups where you may need to configure this value to restrict the Ip address or interface the webserver listens on.

> 

> Defaults to ::, meaning all interfaces, including IPv6.

> 

> Note

> 

> This option may also be set with GRANIAN_HOST and this option may be removed in the future

> 

> PAPERLESS_PORT=<port>

> The port number the webserver will listen on inside the container. There are special setups where you may need this to avoid collisions with other services (like using podman with multiple containers in one pod).

> 

> Don't change this when using Docker. To change the port the webserver is reachable outside of the container, instead refer to the "ports" key in docker-compose.yml.

> 

> Defaults to 8000.

> 

> Note

> 

> This option may also be set with GRANIAN_PORT and this option may be removed in the future

> 

> USERMAP_UID=<uid>

> The ID of the paperless user in the container. Set this to your actual user ID on the host system, which you can get by executing

> 

> id -u

> Paperless will change ownership on its folders to this user, so you need to get this right in order to be able to write to the consumption directory.

> 

> Defaults to 1000.

> 

> USERMAP_GID=<gid>

> The ID of the paperless Group in the container. Set this to your actual group ID on the host system, which you can get by executing

> 

> id -g

> Paperless will change ownership on its folders to this group, so you need to get this right in order to be able to write to the consumption directory.

> 

> Defaults to 1000.

> 

> PAPERLESS_OCR_LANGUAGES=<list>

> Additional OCR languages to install. By default, paperless comes with English, German, Italian, Spanish and French. If your language is not in this list, install additional languages with this configuration option. You will need to find the right LangCodes but note that tesseract-ocr-* package names do not always correspond with the language codes e.g. "chi_tra" should be specified as "chi-tra".

> 

> PAPERLESS_OCR_LANGUAGES=tur ces chi-tra

> Make sure it's a space-separated list when using several values.

> 

> To actually use these languages, also set the default OCR language of paperless:

> 

> PAPERLESS_OCR_LANGUAGE=tur

> Defaults to none, which does not install any additional languages.

> 

> Warning

> 

> This option must not be used in rootless containers.

> 

> PAPERLESS_ENABLE_FLOWER=<defined>

> If this environment variable is defined, the Celery monitoring tool Flower will be started by the container.

> 

> You can read more about this in the advanced documentation.

> 

> PAPERLESS_SUPERVISORD_WORKING_DIR=<defined>

> Warning

> 

> This option is deprecated and has no effect.  For read only file system support,

> see [S6_READ_ONLY_ROOT](https://github.com/just-containers/s6-overlay#customizing-s6-overlay-behaviour)

> from s6-overlay.

> Frontend Settings

> PAPERLESS_APP_TITLE=<str>

> If set, overrides the default name "Paperless-ngx"

> PAPERLESS_APP_LOGO=<path>

> Path to an image file in the /media/logo directory, must include 'logo', e.g. /logo/Atari_logo.svg

> Note

> 

> The logo file will be viewable by anyone with access to the Paperless instance login page, so consider your choice of logo carefully and removing exif data from images before uploading.

> 

> PAPERLESS_ENABLE_UPDATE_CHECK=<bool>

> Note

> 

> This setting was deprecated in favor of a frontend setting after v1.9.2. A one-time migration is performed for users who have this setting set. This setting is always ignored if the corresponding frontend setting has been set.

> 

> Email sending

> Setting an SMTP server for the backend will allow you to use the Email workflow action, send documents from the UI as well as reset your password. All of these options come from their similarly-named Django settings

> 

> PAPERLESS_EMAIL_HOST=<str>

> Defaults to 'localhost'.

> PAPERLESS_EMAIL_PORT=<int>

> Defaults to port 25.

> PAPERLESS_EMAIL_HOST_USER=<str>

> Defaults to ''.

> PAPERLESS_EMAIL_FROM=<str>

> Defaults to PAPERLESS_EMAIL_HOST_USER if not set.

> PAPERLESS_EMAIL_HOST_PASSWORD=<str>

> Defaults to ''.

> PAPERLESS_EMAIL_USE_TLS=<bool>

> Defaults to false.

> PAPERLESS_EMAIL_USE_SSL=<bool>

> Defaults to false.

>  Back to top

> Copyright © 2016 - 2023 Daniel Quinn, Jonas Winkler, and the Paperless-ngx team

> Made with Material for MkDocs

### Assistant
> You’re looking at the right doc section. Now let’s translate that into **what you should actually set** (either in the UI OCR Settings, or in `docker-compose.env`). I’m going to give you **court-safe / evidence-safe defaults** that optimize for: **OCR quality, long-term archiving, and downstream search/vectorization**.
> 
> ## Set these (recommended baseline)
> 
> ### General
> - **PAPERLESS_TIME_ZONE**: `America/Chicago`
> - **PAPERLESS_DATE_PARSER_LANGUAGES**: `en` (or leave unset and let it infer from OCR language)
> - **PAPERLESS_ENABLE_NLTK**: `true` (default; helps classification/matching)
> 
> ### OCR Settings
> These correspond to what you see in the UI (and/or env vars in the docs you pasted):
> 
> - **Output Type** → `pdfa` (PDF/A-2b)  
>   - Env: `PAPERLESS_OCR_OUTPUT_TYPE=pdfa`
> - **Language** → `eng`  
>   - Env: `PAPERLESS_OCR_LANGUAGE=eng`
> - **Pages** → All (leave “Pages” unset)  
>   - Env: do **not** set `PAPERLESS_OCR_PAGES`
> - **Mode** → `skip` (safest)  
>   - Env: `PAPERLESS_OCR_MODE=skip`
> - **Skip Archive File** → `never`  
>   - Env: `PAPERLESS_OCR_SKIP_ARCHIVE_FILE=never`  
>   Rationale: keep both original + archived PDF/A. This matters for evidence integrity and future-proofing.
> - **Image DPI** → leave unset unless you ingest lots of raw images with missing DPI  
>   - If you must set: `300`  
>   - Env: `PAPERLESS_OCR_IMAGE_DPI=300`
> - **Clean** → `clean` (default)  
>   - Env: `PAPERLESS_OCR_CLEAN=clean`
> - **Deskew** → enabled  
>   - Env: `PAPERLESS_OCR_DESKEW=true`
> - **Rotate Pages** → enabled  
>   - Env: `PAPERLESS_OCR_ROTATE_PAGES=true`
> - **Rotate Pages Threshold** → `12` (default is correct)  
>   - Env: `PAPERLESS_OCR_ROTATE_PAGES_THRESHOLD=12`  
>   If you notice bad auto-rotation, adjust later (not now).
> - **Max Image Pixels** → `0` (disable limit) **only if you trust your inputs**  
>   - Env: `PAPERLESS_OCR_MAX_IMAGE_PIXELS=0`  
>   If you ingest random files from others, keep the default limit (safer).
> - **Color Conversion Strategy** → `LeaveColorUnchanged`  
>   - Env: `PAPERLESS_OCR_COLOR_CONVERSION_STRATEGY=LeaveColorUnchanged`  
>   Rationale: preserves stamps/highlights/annotations (important for court).
> - **OCR Arguments** → leave blank initially  
>   - Env: don’t set `PAPERLESS_OCR_USER_ARGS` until you have a proven need.
> 
> ## Barcode Settings
> If you’re not doing barcode-driven splitting, keep it conservative:
> 
> - **Enable (barcode separation / PATCHT)** → `false`  
>   - Env: `PAPERLESS_CONSUMER_ENABLE_BARCODES=false`
> - Leave ASN/tag barcode features off unless you explicitly adopt them later.
> 
> ## Two settings you should decide consciously
> ### 1) Archive behavior (I recommend: keep archive)
> - Keep `Skip Archive File = never` unless disk space is so tight it hurts you.  
> The archive file is your normalized “court-safe” copy.
> 
> ### 2) Max image pixels (security vs completeness)
> - If this system only ingests **your scans/photos**: set `0` (no limit) to avoid missing OCR on huge scans.
> - If you ingest files from **unknown sources**: don’t disable the limit.
> 
> ## Performance (optional but practical)
> These are not in the UI OCR pane, but they matter for speed.
> 
> - **PAPERLESS_TASK_WORKERS**: start with `1` or `2`
> - Let Paperless auto-choose threads per worker unless you know your CPU core count.
> 
> Rule of thumb:  
> `PAPERLESS_TASK_WORKERS * PAPERLESS_THREADS_PER_WORKER` should not exceed your logical CPU cores.
> 
> ## What I would NOT do right now
> - Don’t use `redo` or `force` OCR mode unless you have a specific scanner that embeds bad OCR text layers. `skip` is the correct baseline.
> - Don’t add custom OCR args yet.
> 
> ---
> 
> ### Quick question you don’t need to overthink (but it changes one setting)
> Are you ingesting any documents from unknown/untrusted people (e.g., emailed PDFs from others), or is this strictly your own scanning pipeline?  
> - If **strictly yours** → set Max Image Pixels to `0`.  
> - If **mixed/untrusted** → leave default limit.
> 
> If you answer that, I’ll give you the exact final values for the “Max Image Pixels” choice and any other safety toggles worth adjusting.

### User
> i think adding barcodes would be really cool and make it really professional.

### Assistant
> Cool is not the metric. **Reliability is.** Barcodes can absolutely make this feel “professional,” but only if you use them for a **specific workflow**; otherwise you’ll just add failure modes and extra steps.
> 
> Here’s the clean way to do it that won’t blow up your pipeline.
> 
> ## What barcodes are actually good for
> Use barcodes for one of these (pick at least one):
> 
> 1) **Batch scanning multiple documents into one PDF** and having Paperless split them automatically  
> 2) **Auto-assigning an ASN (archive serial number)** so every doc gets a human-friendly ID  
> 3) **Auto-tagging** at intake (e.g., “FCFCU_CASE”, “INSURANCE”, “RECEIPT”) without touching the UI
> 
> If you’re not doing any of those, keep barcodes off.
> 
> ---
> 
> ## Recommended barcode setup for you
> ### Phase 1 (safe, “professional” without risk): enable separation pages only
> This gives you the “wow” factor and real speed.
> 
> **Set in env (`docker-compose.env`) or UI if exposed:**
> - `PAPERLESS_CONSUMER_ENABLE_BARCODES=true`
> - `PAPERLESS_CONSUMER_BARCODE_STRING=PATCHT` (leave default)
> - `PAPERLESS_CONSUMER_BARCODE_DPI=300` (default)
> - `PAPERLESS_CONSUMER_BARCODE_RETAIN_SPLIT_PAGES=false` (default; don’t keep separator pages)
> 
> **Scanner choice (only if you have detection issues):**
> - Leave default `PYZBAR` first
> - If small/bad quality codes aren’t detected, switch to `ZXING`:
>   - `PAPERLESS_CONSUMER_BARCODE_SCANNER=ZXING`
> 
> **Do NOT enable:**
> - ASN barcodes (yet)
> - Tag barcodes (yet)
> 
> Why: splitting is predictable. ASN/tagging adds “why didn’t it tag right?” chaos.
> 
> ---
> 
> ## What you need to physically do (or it won’t work)
> You must print **separator pages** and use them consistently.
> 
> ### Standard separator page
> Paperless docs recommend a standardized separator page (“PATCHT separator pages”). Use those.
> 
> Workflow:
> - Scan Doc A
> - Insert PATCHT separator sheet
> - Scan Doc B
> - Insert PATCHT separator sheet
> - Scan Doc C
> - Upload one PDF → Paperless splits into 3 docs
> 
> That’s the professional win.
> 
> ---
> 
> ## Phase 2 (optional): Auto-tagging via barcode
> This is slick, but only once separation is working.
> 
> Enable:
> - `PAPERLESS_CONSUMER_ENABLE_TAG_BARCODE=true`
> - Keep the default mapping:
>   - `PAPERLESS_CONSUMER_TAG_BARCODE_MAPPING={"TAG:(.*)":"\\g<1>"}`
> 
> Then you print barcodes like:
> - `TAG:FCFCU_CASE`
> - `TAG:INSURANCE`
> - `TAG:RECEIPT`
> 
> Place the tag barcode page at the front of a doc (or in the doc), and Paperless assigns tags automatically.
> 
> **Warning:** if you start doing 12 tags per doc, you’ll create tag sprawl. Limit yourself to 1–3 tag barcode pages.
> 
> ---
> 
> ## Phase 3 (optional): ASN barcodes
> Only if you want to embed a physical identifier on documents. This is more fragile and less necessary if Paperless IDs are sufficient.
> 
> If you do it:
> - `PAPERLESS_CONSUMER_ENABLE_ASN_BARCODE=true`
> - `PAPERLESS_CONSUMER_ASN_BARCODE_PREFIX=ASN`
> 
> Barcodes must be like:
> - `ASN00123`
> 
> If Paperless sees a duplicate ASN, it rejects the doc. That’s why this is phase 3.
> 
> ---
> 
> ## My blunt recommendation
> Start with **Phase 1 only**:
> - Barcode splitting using PATCHT separator pages.
> 
> Run a real test:
> - Scan 3 documents into one PDF with separator pages
> - Confirm Paperless splits correctly every time
> 
> If it passes, then we turn on tag barcodes.
> 
> ---
> 
> ## Tell Gemini this (copy/paste)
> ```text
> Update config to enable barcode separation only (PATCHT). Do not enable ASN or tag barcodes yet.
> Set:
> PAPERLESS_CONSUMER_ENABLE_BARCODES=true
> PAPERLESS_CONSUMER_BARCODE_STRING=PATCHT
> PAPERLESS_CONSUMER_BARCODE_RETAIN_SPLIT_PAGES=false
> Keep scanner default (PYZBAR). Document how to print and use PATCHT separator pages.
> ```
> 
> If you want, I can also give you a **minimal barcode pack** (print-ready) for:
> - PATCHT separators
> - TAG:FCFCU_CASE / TAG:AES / TAG:TAX / TAG:INSURANCE / TAG:RECEIPT  
> …but first confirm you actually have a printer you can use reliably.

### User
> it would be wonderful to patch in qi-cli and the barcode be the unique id assigned and the auto tagging or something.

### Assistant
> That’s a solid direction, and it can be done cleanly — **but you need to decide what the “unique ID” actually is** in a way Paperless can enforce.
> 
> Paperless gives you two barcode-driven primitives that matter:
> 
> 1) **PATCHT** = split documents in a batch  
> 2) **ASN barcode** = set the document’s Archive Serial Number (ASN) from a barcode (and reject duplicates)
> 
> If you want “barcode = unique ID assigned,” the **ASN barcode feature** is the correct mechanism.
> 
> The rest (auto-tagging) layers on top with **TAG:… barcodes**.
> 
> ---
> 
> ## The clean architecture
> 
> ### The ID
> Use **ASN** as the “physical-scannable unique ID.”
> 
> - Paperless ASN barcodes are effectively: `ASN<digits>`  
> - Paperless **cleans non-numeric**, and it treats ASN collisions as errors (good; that’s your uniqueness enforcement).
> 
> So your `qi-cli` should mint IDs like:
> - `ASN00012345` (printed on a cover sheet / separator sheet)
> 
> This becomes the hard ID that ties:
> - the physical scan
> - the Paperless record
> - the QiNote sidecar
> - any downstream vectorization
> 
> ### Auto-tagging
> Use tag barcode pages with:
> - `TAG:FCFCU_CASE`
> - `TAG:INSURANCE`
> - `TAG:RECEIPT`
> - `TAG:READY_FOR_QINOTE` (optional, but I prefer you still apply “Ready_for_QiNote” manually until trust is established)
> 
> Paperless supports tag barcodes via regex mapping. This is stable.
> 
> ### Splitting
> Use **PATCHT separator pages** to split multi-doc scans. This makes the workflow feel “enterprise.”
> 
> ---
> 
> ## The actual intake workflow (what “professional” looks like)
> 
> **Before scanning:**
> 1) Run `qi-cli intake new`  
>    - reserves a new ASN ID (numeric)
>    - generates a printable **cover sheet PDF** containing:
>      - `PATCHT` separator (optional)
>      - `ASN00012345` barcode (required)
>      - optional tag barcodes: `TAG:FCFCU_CASE`, `TAG:EVIDENCE`, etc.
>      - human-readable text: title line, date, and the ASN
> 
> **At scanning:**
> 2) Put the cover sheet in front of the document  
> 3) Scan batches with PATCHT pages between documents  
> 4) Drop the batch PDF into Paperless consume
> 
> **Paperless does:**
> - Splits on PATCHT
> - Assigns ASN from ASN barcode
> - Assigns tags from TAG barcodes
> 
> **Bridge does:**
> - Exports sidecar `.md` into QiNoteOS (and optionally copies PDF depending on mode)
> - Uses ASN as the stable filename stem if present:
>   `YYYY-MM-DD__{slug}__ASN00012345__paperless-{id}.pdf`
> 
> ---
> 
> ## Configuration you will set in Paperless (env vars)
> 
> ### Barcode splitting
> - `PAPERLESS_CONSUMER_ENABLE_BARCODES=true`
> - `PAPERLESS_CONSUMER_BARCODE_STRING=PATCHT`
> - `PAPERLESS_CONSUMER_BARCODE_RETAIN_SPLIT_PAGES=false`
> - (optional) `PAPERLESS_CONSUMER_BARCODE_SCANNER=ZXING` if detection is flaky
> 
> ### ASN assignment (this is the “unique ID” feature)
> - `PAPERLESS_CONSUMER_ENABLE_ASN_BARCODE=true`
> - `PAPERLESS_CONSUMER_ASN_BARCODE_PREFIX=ASN`
> 
> ### Auto-tagging
> - `PAPERLESS_CONSUMER_ENABLE_TAG_BARCODE=true`
> - Keep default mapping unless you want custom:
>   - `PAPERLESS_CONSUMER_TAG_BARCODE_MAPPING={"TAG:(.*)":"\\g<1>"}`
> 
> That mapping means `TAG:FCFCU_CASE` becomes the tag `FCFCU_CASE`.
> 
> ---
> 
> ## One hard constraint you must accept
> **ASN is numeric.**  
> So if your dream ID is a dotted QiDecimal like `2.04.713.001`, that cannot be used as ASN directly.
> 
> You have three options:
> 
> 1) **Use numeric ASN as the hard ID** (recommended)  
>    - Keep QiDecimal in the sidecar YAML (`qinote_id:`) or in tags (`QID:2.04...`)
> 2) Encode QiDecimal into digits (ugly; not recommended)
> 3) Use QR codes + custom extraction (Paperless doesn’t natively map QR payloads into a custom metadata field beyond tags/ASN; you’d be building glue)
> 
> The clean, low-risk choice is: **ASN = numeric, QiDecimal = metadata in QiNote**.
> 
> ---
> 
> ## What to tell Gemini (copy/paste)
> Send this:
> 
> ```text
> We want barcode-driven professional intake.
> 
> Implement these in local-deploy docker-compose.env:
> - PAPERLESS_CONSUMER_ENABLE_BARCODES=true
> - PAPERLESS_CONSUMER_BARCODE_STRING=PATCHT
> - PAPERLESS_CONSUMER_BARCODE_RETAIN_SPLIT_PAGES=false
> - PAPERLESS_CONSUMER_ENABLE_ASN_BARCODE=true
> - PAPERLESS_CONSUMER_ASN_BARCODE_PREFIX=ASN
> - PAPERLESS_CONSUMER_ENABLE_TAG_BARCODE=true
> - PAPERLESS_CONSUMER_TAG_BARCODE_MAPPING={"TAG:(.*)":"\\g<1>"}
> 
> Do NOT enable other barcode features.
> 
> Then update export_bridge.py:
> - If ASN exists, use it as the primary stable identifier in filenames + YAML.
> - Include asn in YAML front matter.
> 
> Separately, create a small qi-cli (or python cli) that:
> - mints the next ASN number from a local counter file (atomic write)
> - generates a printable PDF cover sheet containing:
>   - Barcode for ASN########
>   - Optional TAG:... barcodes
>   - Optional PATCHT separator page
> - Provide a README: how to print and use these sheets for batch scanning.
> ```
> 
> ---
> 
> ## Quick question that changes the implementation detail
> Do you want `qi-cli` to mint IDs:
> - **Per document** (most common), or
> - **Per intake batch** (one ID for a stack, then split assigns sub-IDs)?
> 
> If you don’t answer, choose **per document** — it aligns with ASN uniqueness and court evidence handling.

### User
> Enable Barcodes 

> Enable

> Enable TIFF Support 

> Enable  

> Barcode String 

> false

> Retain Split Pages 

> Enable  

> Enable ASN 

> Enable

> ASN Prefix 

> ASN

> Upscale 

> DPI 

> Max Pages 

> Enable Tag Detection 

> Enable  

> Tag Mapping 
> 
> -- to answer your questions you know our QIDs are only qid000000_0 so the id wouls just be ASN000000 or asn00000000

### Assistant
> Perfect — if your QIDs are `qid000000_0`-style, then using **ASN00000000** as the scannable ID is clean and compatible with Paperless’ ASN barcode feature.
> 
> Now, your current UI snapshot has one glaring problem:
> 
> **“Barcode String = false” is wrong.**  
> That field should be the separator token (usually `PATCHT`). Setting it to `false` will break separation.
> 
> Here are the **exact settings** you should use in that Barcode section.
> 
> ---
> 
> ## Paperless Barcode Settings (Recommended)
> 
> ### Enable Barcodes
> **Enable = ON**
> 
> ### Enable TIFF Support
> **Enable = OFF** (turn this on only if your scanner produces TIFFs)
> - If you mostly scan to PDF (most people do), leave it OFF.
> 
> ### Barcode String
> **PATCHT**
> - This is the separator-page barcode value Paperless expects (default standard).
> 
> ### Retain Split Pages
> **OFF**
> - You do not want separator pages cluttering your archive.
> - Turn ON only if you want to keep separator pages for audit/debug (usually unnecessary).
> 
> ### Enable ASN
> **ON**
> 
> ### ASN Prefix
> **ASN**
> - Your printed barcode should be like: `ASN00001234`
> - Paperless will extract the digits and set ASN = `1234` (it stores it as a number internally).
> 
> ### Upscale
> **0.0** (or blank / default)
> - Only increase if barcode detection is failing on small codes.
> - If detection fails, set **1.5**.
> 
> ### DPI
> **300**
> - If detection is flaky, increase to **600** (costs CPU).
> 
> ### Max Pages
> **0** (meaning “check all pages”)
> - If you want performance limits later, set a cap (e.g., 50), but start with 0.
> 
> ### Enable Tag Detection
> **ON**
> 
> ### Tag Mapping
> Use the standard mapping (copy/paste exactly):
> 
> ```json
> {"TAG:(.*)":"\\g<1>"}
> ```
> 
> This means:
> - Barcode text `TAG:FCFCU_CASE` → tag `FCFCU_CASE`
> - Barcode text `TAG:Ready_for_QiNote` → tag `Ready_for_QiNote`
> 
> ---
> 
> ## What your barcode pages should look like
> 
> ### Separator page barcode (for splitting batches)
> - Barcode content: `PATCHT`
> 
> ### ID page barcode (for unique ID)
> - Barcode content: `ASN00000001` (etc.)
> 
> ### Tag page barcode(s)
> - Barcode content: `TAG:FCFCU_CASE`
> - Barcode content: `TAG:EVIDENCE`
> - Barcode content: `TAG:Ready_for_QiNote` (optional)
> 
> **Best practice:** keep tag barcode pages to **1–3 per document** to avoid tag sprawl.
> 
> ---
> 
> ## One important “gotcha” (so you don’t get mad later)
> Paperless ASN is numeric under the hood. It will accept the barcode text `ASN00000001`, but it extracts digits and sets ASN to `1`. That’s fine; you can still *display* and *print* the padded form everywhere else.
> 
> So in your QiNote bridge, you should format it back to padded form:
> - `ASN{asn:08d}` → `ASN00000001`
> 
> Tell Gemini to do that.
> 
> ---
> 
> ## The one thing I’d change in your list
> You wrote: **“Barcode String false”**  
> Set it to **PATCHT**. Everything else can be tuned later.
> 
> ---
> 
> ## What to tell Gemini (1-paragraph, direct)
> “Update the barcode config: Barcode String = PATCHT; Retain Split Pages = false; DPI=300; Upscale=0.0; Max Pages=0; Enable ASN with prefix ASN; Enable Tag Detection with mapping `{"TAG:(.*)":"\\g<1>"}`. In the bridge, if ASN exists, output a padded string `ASN{asn:08d}` for filenames and YAML.”
> 
> If you paste back what Paperless shows after you set these, I’ll sanity-check it against the expected behavior (split + ASN assignment + tag assignment) in one pass.

### User
> can we use qid as the prefix, instead of asn?

### Assistant
> Short answer: **no — not safely, not the way you want.**  
> Long answer below, with the **clean workaround that still gives you QIDs everywhere that matters**.
> 
> ---
> 
> ## Why you **cannot** replace `ASN` with `QID` (in Paperless)
> 
> Paperless’ **ASN barcode feature is hard-wired conceptually to “ASN”**:
> 
> - The setting is literally **“Enable ASN barcode”**
> - The field is **“ASN Prefix”**
> - Internally, Paperless:
>   - Treats ASN as a **numeric unique identifier**
>   - Enforces **uniqueness**
>   - Rejects duplicates
>   - Uses it in archive logic
> 
> If you change the prefix to `QID`, Paperless will still:
> - Treat it as an **ASN**
> - Strip non-numeric characters
> - Store only the digits
> - Conceptually think it’s an ASN anyway
> 
> So setting:
> ```
> ASN Prefix = QID
> ```
> will **work technically**, but it is **lying to the system** and will bite you later (docs, upgrades, tooling, expectations).
> 
> **Blunt truth:**  
> > ASN is not a label. It is a semantic role in Paperless.  
> > Renaming it does not make it something else.
> 
> ---
> 
> ## The correct, professional architecture (do this instead)
> 
> ### Use **ASN as the physical / intake ID**
> - Barcode on paper
> - Enforced uniqueness
> - Guaranteed detection
> - Batch-safe
> - Court-safe
> 
> ### Use **QID as the semantic / knowledge ID**
> - Lives in QiNote
> - Lives in sidecar YAML
> - Lives in Gina vectors
> - Lives in filenames if you want
> - Is *yours*, not Paperless’
> 
> This separation is **intentional and correct**.
> 
> ---
> 
> ## How this looks in practice (clean and powerful)
> 
> ### On paper (what gets scanned)
> - Barcode: `ASN00001234`
> - Optional tag barcode: `TAG:QID00001234_0` (or generated later)
> 
> ### In Paperless
> - ASN field = `1234`
> - Tags = `QID00001234_0`, `FCFCU_CASE`, etc.
> 
> ### In QiNote sidecar (`.md`)
> ```yaml
> ---
> title: ...
> paperless_id: 987
> asn: ASN00001234
> qid: QID00001234_0
> source: paperless-ngx
> 
> document_type: Court Filing
> correspondent: FCFCU
> tags:
>   - FCFCU_CASE
>   - evidence
> 
> document_date: 2026-01-03
> date_received: 2026-01-04
> 
> project: FCFCU_CASE
> status: received
> confidence: primary_source
> ---
> ```
> 
> ### In filenames (optional, recommended)
> ```
> 2026-01-03__Court_Filing__FCFCU__ASN00001234__paperless-987.pdf
> ```
> 
> QID does **not** need to be the physical barcode to be first-class.
> 
> ---
> 
> ## If you absolutely insist on QID barcodes (not recommended)
> The **only safe way** is:
> 
> - Keep ASN barcodes **enabled and primary**
> - ALSO enable **Tag Detection**
> - Encode QID as a tag barcode:
>   ```
>   TAG:QID00001234_0
>   ```
> 
> Paperless will:
> - Assign ASN correctly
> - Attach the QID as metadata
> - Let your bridge elevate QID into YAML / filenames / indexes
> 
> This avoids breaking Paperless’ assumptions.
> 
> ---
> 
> ## What to tell Gemini (authoritative, final)
> Copy/paste this:
> 
> ```text
> Do NOT replace ASN with QID in Paperless.
> 
> Keep ASN as the barcode-based unique ID (numeric, enforced by Paperless).
> 
> QID is a semantic ID owned by QiNote, not Paperless.
> If QID is needed at intake, encode it as a TAG barcode (e.g. TAG:QID00001234_0),
> and propagate it via the export bridge into YAML and filenames.
> 
> In the bridge:
> - Always capture ASN (pad to 8 digits for display)
> - Capture QID from tags if present
> - Treat ASN as physical ID, QID as semantic ID
> ```
> 
> ---
> 
> ## The uncomfortable but important truth
> You are designing a **multi-system architecture**.  
> Trying to make one system speak another system’s language **at the lowest layer** is how systems rot.
> 
> ASN = physical intake truth  
> QID = semantic knowledge truth  
> 
> That separation is not a compromise — it’s good engineering.
> 
> If you want next, I can:
> - Design the **qi-cli cover sheet generator** (PDF layout + barcodes)
> - Define the **ASN ↔ QID mapping rules**
> - Add **QID auto-assignment** in the bridge
> - Or sanity-check your current Paperless barcode UI screen once set
> 
> Say which one.

### User
> then why does it even ask for the prefix, i feel like whats going to happen is the id will say, asnasn0000000 also what shoudl the upscale be set too adn the dpi

### Assistant
> You’re not wrong to question that. This is one of those spots where **the UI wording is misleading**, and if you don’t understand what’s really happening under the hood it *feels* like it’s going to double-prefix or mangle the ID.
> 
> Let’s clear this up cleanly.
> 
> ---
> 
> ## 1. Why Paperless even asks for an “ASN Prefix”
> 
> **It is not a cosmetic prefix.**  
> It is a **barcode filter**, not a formatter.
> 
> ### What actually happens internally
> - Paperless scans barcodes on pages
> - It looks for barcode text that **starts with the configured prefix**
> - When it finds one:
>   - It **removes the prefix**
>   - It **strips non-numeric characters**
>   - The remaining digits become the ASN **number**
> 
> So:
> 
> | Barcode text | ASN Prefix | Stored ASN |
> |-------------|-----------|------------|
> | `ASN00001234` | `ASN` | `1234` |
> | `QID00001234` | `QID` | `1234` |
> | `ASNASN00001234` | `ASN` | ❌ messy input (don’t do this) |
> 
> Paperless **does not prepend** the prefix.  
> It only **matches and strips** it.
> 
> That’s why you won’t get `asnasn0000000` unless you literally print that.
> 
> ### Why the prefix exists at all
> So Paperless can:
> - Ignore random barcodes (shipping labels, QR codes, etc.)
> - Only treat **specific barcodes** as ASN candidates
> - Support different organizations using different prefixes
> 
> That’s it. No formatting. No duplication.
> 
> ---
> 
> ## 2. Why you still should NOT use `QID` as the ASN prefix (even though it “works”)
> 
> Yes, technically you *could* set:
> ```
> ASN Prefix = QID
> ```
> 
> And scan:
> ```
> QID00001234
> ```
> 
> Paperless would store:
> ```
> ASN = 1234
> ```
> 
> But here’s the problem:
> 
> - Internally, that field is still **ASN**
> - Paperless features, docs, exports, and future tooling will refer to it as ASN
> - You lose semantic clarity and make future debugging harder
> - You now have “QID” that is actually an ASN everywhere except the barcode text
> 
> That’s why I’m steering you away from it — not because it breaks immediately, but because it **lies about meaning**.
> 
> **Correct mental model:**  
> Prefix = *barcode discriminator*, not *ID identity*
> 
> ---
> 
> ## 3. DPI and Upscale — the correct values (no guessing)
> 
> ### DPI (this one matters more)
> **Set DPI = 300**
> 
> - This is the sweet spot for:
>   - Barcode detection
>   - OCR
>   - CPU usage
> - Only go to **600** if:
>   - Barcodes are small
>   - Scans are low contrast
>   - Detection fails at 300
> 
> Start at 300.
> 
> ---
> 
> ### Upscale
> **Set Upscale = 0.0**
> 
> Upscale means: “enlarge the image *before* barcode detection.”
> 
> - `0.0` = off (no upscale)
> - `1.5` = 150% scale (helpful for tiny barcodes)
> - `>2.0` = expensive and usually unnecessary
> 
> **Rule:**
> - Start at **0.0**
> - If barcode detection fails → try **1.5**
> - Do not set >1.5 unless you have proof you need it
> 
> Upscaling costs CPU and memory; don’t pay that tax unless needed.
> 
> ---
> 
> ## 4. Your final, sane barcode settings (copy this mentally)
> 
> - Enable Barcodes: **ON**
> - Barcode String: **PATCHT**
> - Retain Split Pages: **OFF**
> - Enable ASN: **ON**
> - ASN Prefix: **ASN**
> - DPI: **300**
> - Upscale: **0.0**
> - Max Pages: **0** (all pages)
> - Enable Tag Detection: **ON**
> - Tag Mapping:
>   ```json
>   {"TAG:(.*)":"\\g<1>"}
>   ```
> 
> This will:
> - Split batches correctly
> - Assign a unique numeric ASN safely
> - Never double-prefix anything
> - Keep performance reasonable
> 
> ---
> 
> ## 5. The key reassurance you needed
> > “What’s going to happen is the id will say asnasn0000000”
> 
> That **will not happen** unless you literally print `ASNASN0000000`.
> 
> Paperless does **not** add prefixes.  
> It only recognizes and removes them.
> 
> ---
> 
> If you want next, the logical follow-up is:
> - designing the **qi-cli cover sheet generator** so you never have to think about this again, or
> - validating one real scan end-to-end (barcode → Paperless → QiNote sidecar).
> 
> Tell me which one and we’ll lock it.

### User
> ok no wi am in mail and need to add my mail clients, from my domains, since i am loosing zoho mail and dont ahve my domains connected to nothing else yet, i will need to forward all incoming somehow just fyi, dont know if that matters here. here are the settign in paperless. Mail Settings 

> Mail accounts

> Name

> Server

> Username

> Actions

> No mail accounts defined.

> Mail rules

> Name

> Sort Order

> Account

> Status

> Processed Mail

> Actions

> No mail rules defined.

### Assistant
> Good timing — this **does matter**, but not in the way people usually think. You can absolutely wire Paperless to catch *everything* while your email situation is in flux **without committing to a long-term mail host yet**.
> 
> I’ll break this into **what matters now vs later**, then give you **exact steps** to get mail flowing safely.
> 
> ---
> 
> ## The core principle (lock this mentally)
> 
> **Paperless does not need to be your mail system.**  
> It just needs **a copy of incoming mail**.
> 
> So your goals are:
> 
> 1. Don’t lose mail while Zoho is going away  
> 2. Capture *all incoming documents* into Paperless  
> 3. Avoid reconfiguring Paperless every time you change email providers
> 
> ---
> 
> ## Your best interim architecture (clean + low risk)
> 
> ### SHORT VERSION
> - Create **one catch-all mailbox** somewhere (temporary is fine)
> - Forward *everything* from your domains to that mailbox
> - Configure **one Paperless mail account**
> - Use **mail rules** to auto-tag and auto-consume
> 
> Later, when you pick a permanent mail host, you only update forwarding — **Paperless stays untouched**.
> 
> ---
> 
> ## Step 1: Decide where mail lands (right now)
> 
> Since you’re losing Zoho Mail and domains aren’t connected elsewhere yet, you have **three viable interim options**, ranked:
> 
> ### ✅ Option A (recommended, fastest): Gmail
> - Create a dedicated mailbox, e.g.  
>   `archive.yourname@gmail.com`
> - Turn on **IMAP**
> - Forward *all* domain email to it
> 
> Pros:
> - Reliable
> - OAuth supported
> - Zero setup friction
> 
> Cons:
> - Google (privacy tradeoff — acceptable for intake copies)
> 
> ---
> 
> ### Option B: Proton Mail (if you already have it)
> - Works, but:
>   - IMAP requires Proton Bridge (local agent)
>   - More moving parts
> 
> Only do this if you already use Proton daily.
> 
> ---
> 
> ### Option C: Temporary hosting (Cloudflare Email Routing → Gmail)
> - Domains on Cloudflare?
> - Use **Email Routing** to forward all mail to Gmail
> 
> This is actually very clean if your domains are already on Cloudflare.
> 
> ---
> 
> ### 🚫 Don’t do yet
> - Don’t configure Paperless for Zoho if it’s going away
> - Don’t add multiple mail accounts to Paperless yet
> - Don’t use encrypted mail until stable
> 
> ---
> 
> ## Step 2: Add ONE mail account in Paperless
> 
> Go to **Mail Settings → Mail Accounts → Add**.
> 
> ### Example (Gmail via IMAP + OAuth)
> - **Name:** `Primary Intake`
> - **Server:** `imap.gmail.com`
> - **Username:** your Gmail address
> - **Authentication:** OAuth (preferred)  
>   *(or password if OAuth setup feels heavy)*
> 
> Paperless will poll this mailbox and pull messages.
> 
> That’s it. One account.
> 
> ---
> 
> ## Step 3: Add mail rules (this is where power lives)
> 
> Mail rules decide **what becomes a document** and **how it’s tagged**.
> 
> Go to **Mail Settings → Mail Rules → Add**.
> 
> ### Rule 1 — Default intake (catch-all)
> This ensures nothing is missed.
> 
> - **Name:** `Default Intake`
> - **Account:** `Primary Intake`
> - **Match:** *(leave broad)*  
>   - Subject contains: *(blank)*  
>   - From contains: *(blank)*  
> - **Actions:**
>   - ✔ Consume attachments
>   - ✔ Assign tag: `email`
>   - ✔ Assign tag: `received`
> - **Processed Mail:**  
>   - Mark as read  
>   - Move to folder: `Processed/Paperless` (optional)
> 
> This alone is enough to get going.
> 
> ---
> 
> ### Rule 2 — Legal / Court (optional but smart)
> Example:
> 
> - **Name:** `Court Mail`
> - **Match:**
>   - From contains: `@courts.in.gov` (example)
>   - OR Subject contains: `Order`, `Notice`, `Hearing`
> - **Actions:**
>   - ✔ Consume attachments
>   - ✔ Assign tag: `legal`
>   - ✔ Assign tag: `evidence`
>   - ✔ Assign tag: `email`
> - **Sort Order:** higher priority than Default Intake
> 
> ---
> 
> ### Rule 3 — Bills / Utilities (optional)
> - Match sender domains (`@aes.com`, etc.)
> - Tag: `billing`, `utility`
> 
> ---
> 
> ## Step 4: About forwarding (this is key for your situation)
> 
> Since your domains are currently “in between” providers:
> 
> ### What you want at the domain/DNS level
> - **Forward ALL incoming mail** for each domain to your intake mailbox
> - Optionally:
>   - Preserve original headers
>   - Do not delete originals (if temporarily still hosted)
> 
> Paperless doesn’t care where the mail came from — only that it arrives in the IMAP inbox.
> 
> ---
> 
> ## Step 5: What NOT to worry about right now
> 
> - ❌ Email OAuth vs password perfection
> - ❌ SSO
> - ❌ Encrypted email
> - ❌ Multiple accounts per domain
> 
> You can add all that later once mail is stable.
> 
> ---
> 
> ## One critical setting to double-check
> In **OCR / Consumption**, make sure:
> - Attachments are consumed
> - `.eml` parsing is enabled (default)
> - Tika/Gotenberg are **optional** — skip for now unless you expect `.docx`/`.xlsx` a lot
> 
> ---
> 
> ## Blunt truth (so you don’t spiral)
> Email intake is **plumbing**, not identity.  
> The worst mistake here is trying to design the “perfect” mail system while domains are in flux.
> 
> **Forward everything → one inbox → Paperless rules → done.**
> 
> ---
> 
> ## Next question I need from you (one line answer)
> Are your domains currently managed on **Cloudflare**, **Zoho**, or somewhere else?
> 
> That determines the **exact forwarding steps**, and I can give you copy-paste DNS / routing instructions next.

### User
> i have my qially domain setup in google workspace

### Assistant
> Perfect. Google Workspace is actually the **cleanest possible position** to be in for this. You can make Paperless catch *everything* without disrupting mail delivery or locking yourself into a final mail architecture yet.
> 
> Below is the **correct, low-risk setup** given your situation.
> 
> ---
> 
> # What matters (short, grounded truth)
> 
> - **Google Workspace stays your mail intake hub**
> - **Paperless is a downstream consumer only**
> - You do **not** need to “move” mail yet
> - You just need **copies of relevant mail** flowing to Paperless
> 
> You will **not lose mail** if this is done correctly.
> 
> ---
> 
> # Recommended Architecture (right now)
> 
> **Google Workspace (qiAlly domain)**
> → IMAP access  
> → Paperless mail account  
> → Mail rules (consume attachments + tag)
> 
> No forwarding yet unless you want redundancy.
> 
> ---
> 
> # Step 1 — Enable IMAP in Google Workspace (if not already)
> 
> Admin Console → **Apps → Google Workspace → Gmail → End User Access**
> - ✔ Enable IMAP access
> 
> Per-user (in Gmail settings):
> - Settings → Forwarding and POP/IMAP
> - ✔ Enable IMAP
> 
> ---
> 
> # Step 2 — Create a dedicated intake mailbox (strongly recommended)
> 
> Do **not** use your personal inbox.
> 
> Create something like:
> - `intake@qially.com`
>   or
> - `archive@qially.com`
> 
> Why:
> - Keeps Paperless noise out of your main inbox
> - Easier rule targeting
> - Future-proof if you change providers again
> 
> You can still forward selectively from other mailboxes later.
> 
> ---
> 
> # Step 3 — Add the mail account in Paperless
> 
> Paperless → **Mail Settings → Mail Accounts → Add**
> 
> Use **IMAP**, not POP.
> 
> **Settings:**
> - **Name:** `QiAlly Intake`
> - **Server:** `imap.gmail.com`
> - **Port:** `993`
> - **Encryption:** SSL/TLS
> - **Username:** `intake@qially.com`
> - **Password:**  
>   - Use an **App Password** (recommended), not your real password  
>   - Google Account → Security → App passwords → “Mail / Other”
> 
> Save.
> 
> Paperless will now poll Gmail.
> 
> ---
> 
> # Step 4 — Create Mail Rules (this is the important part)
> 
> ## Rule 1 — Catch-all intake (start here)
> 
> Mail Rules → Add
> 
> - **Name:** `Default Intake`
> - **Sort Order:** 100 (low priority)
> - **Account:** `QiAlly Intake`
> - **Match Conditions:** *(leave broad)*
> 
> **Actions:**
> - ✔ Consume attachments
> - ✔ Assign tag: `email`
> - ✔ Assign tag: `received`
> 
> **Processed Mail:**
> - ✔ Mark as read
> - ✔ Move to folder: `Processed/Paperless` (optional but clean)
> 
> This ensures nothing slips through.
> 
> ---
> 
> ## Rule 2 — Legal / Case mail (recommended)
> 
> - **Name:** `Legal Mail`
> - **Sort Order:** 10 (higher priority)
> - **Match:**
>   - From contains: `@courts.`, `@fcfcu`, etc.
>   - OR Subject contains: `Order`, `Notice`, `Hearing`
> 
> **Actions:**
> - ✔ Consume attachments
> - ✔ Assign tags:
>   - `legal`
>   - `evidence`
>   - `email`
> 
> ---
> 
> ## Rule 3 — Bills / Statements (optional)
> 
> - Match: `@aes.com`, `statement`, `invoice`
> - Tags: `billing`, `utility`
> 
> ---
> 
> # Step 5 — Do you need forwarding *right now*?
> 
> ### Answer: **No — unless Zoho mailboxes are still receiving mail**
> 
> Since `qially.com` is already on Google Workspace:
> - MX records already point to Google
> - Mail is already landing safely
> 
> Only add forwarding if:
> - You still have **other domains** on Zoho
> - Or you want redundancy
> 
> If you do want redundancy:
> - Gmail → Forwarding → forward a copy to a backup Gmail
> 
> Paperless doesn’t care either way.
> 
> ---
> 
> # Important Paperless email settings to confirm
> 
> In **Configuration → Email Parsing**:
> - Default layout: **HTML, then Text** (recommended)
> 
> No Tika needed yet unless you expect:
> - `.docx`
> - `.xlsx`
> - `.eml` parsing beyond attachments
> 
> You can add Tika later without breaking anything.
> 
> ---
> 
> # What this gives you immediately
> 
> - Every emailed PDF → OCR → searchable
> - Tags applied automatically
> - Documents ready for ASN/QID workflow
> - Gina/QiNote bridge can pick them up later
> 
> And you didn’t commit to:
> - A final mail host
> - A complex forwarding topology
> - Rework later
> 
> ---
> 
> # One clarifying question (answer yes/no)
> 
> Do you want **email bodies themselves** (not just attachments) stored as documents in Paperless, or **attachments only**?
> 
> That changes one checkbox and I’ll tell you exactly which.

### User
> i cant find the app password thing

### Assistant
> This is a **very common Google Workspace gotcha**, and you’re not crazy — the reason you “can’t find it” is because **Google hides App Passwords unless two specific conditions are true**.
> 
> Let’s get you unstuck quickly.
> 
> ---
> 
> ## Why you don’t see “App Passwords”
> 
> Google only shows **App Passwords** if **BOTH** are true:
> 
> 1. **2-Step Verification is enabled** on the account  
> 2. The account is **allowed** to use app passwords (Workspace admins can disable this)
> 
> If either is missing → the menu literally does not appear.
> 
> ---
> 
> ## Step 1 — Confirm 2-Step Verification is ON (this is required)
> 
> Log in as the mailbox user (e.g. `intake@qially.com`).
> 
> Go to:
> **Google Account → Security**
> 
> Look for **“Signing in to Google”**
> 
> If you do NOT see “2-Step Verification: On”:
> - Click **2-Step Verification**
> - Turn it ON
> - Use phone or authenticator app
> - Finish setup
> 
> 🔴 **Until this is ON, App Passwords do not exist.**
> 
> ---
> 
> ## Step 2 — Check Workspace admin setting (this is the usual blocker)
> 
> Log in as **Workspace Admin**.
> 
> Admin Console →  
> **Security → Authentication → 2-Step Verification**
> 
> Check these settings:
> 
> - ✔ Allow users to turn on 2SV
> - ✔ **Allow users to generate app passwords** ← this is the critical one
> 
> If “Allow app passwords” is OFF:
> - Turn it ON
> - Save
> - Wait ~5 minutes
> - Sign out and back in
> 
> If this is disabled at the org level, users will *never* see app passwords no matter what.
> 
> ---
> 
> ## Step 3 — Now generate the App Password (exact path)
> 
> Once Steps 1 and 2 are done:
> 
> 1. Go to **myaccount.google.com**
> 2. Security
> 3. Under “Signing in to Google”
> 4. You will now see **App passwords**
> 
> Click it.
> 
> Create:
> - App: **Mail**
> - Device: **Other**
> - Name it: `Paperless`
> 
> Google will show a **16-character password**.
> 
> 📌 Copy it immediately — you won’t see it again.
> 
> ---
> 
> ## Step 4 — Use it in Paperless (important detail)
> 
> In Paperless mail account settings:
> 
> - Username: `intake@qially.com`
> - Password: **the app password**
> - Server: `imap.gmail.com`
> - Port: `993`
> - Encryption: SSL/TLS
> 
> Do **not** use your real Google password.
> 
> ---
> 
> ## If App Passwords are still unavailable (fallback)
> 
> If Workspace policy forbids app passwords (some orgs do):
> 
> ### Option A — Use Gmail OAuth (best)
> Paperless supports Gmail OAuth.
> - Slightly more setup
> - No passwords stored
> - Google-approved
> 
> ### Option B — Temporary forwarding inbox
> - Forward mail to a personal Gmail
> - Use app password there
> - Still safe for intake copies
> 
> ---
> 
> ## Quick diagnostic (answer this)
> When you go to **Google Account → Security**, do you see:
> - “2-Step Verification: On” → yes/no
> - “App passwords” anywhere → yes/no
> 
> Answer those two and I’ll tell you **exactly** which lever is blocking you and how to flip it in one move.

### User
> wait wait, am i creating the mail rules in my gmail or in inside peperless, and then what workflows are we putting inpaperless

### Assistant
> Good pause. This is the right moment to lock the mental model so you don’t wire this backwards.
> 
> ### Short answer
> - **Mail rules = inside Paperless**
> - **Gmail rules = optional, minimal, only for routing/cleanup**
> - **Workflows = inside Paperless (not Gmail)**
> 
> They serve different purposes. Do not mix them.
> 
> ---
> 
> ## Correct division of responsibility (this matters)
> 
> ### Gmail / Google Workspace
> **Job:** deliver mail reliably to a mailbox  
> **NOT its job:** decide what becomes a document, tags, cases, evidence, etc.
> 
> You should use Gmail rules only for:
> - Forwarding (if needed)
> - Keeping inbox clean
> - Routing to folders/labels (optional)
> 
> Think of Gmail as the **mail truck**.
> 
> ---
> 
> ### Paperless-ngx
> **Job:** interpret mail → documents → metadata → automation
> 
> This is where:
> - Attachments become documents
> - OCR happens
> - ASN is assigned
> - Tags are applied
> - Documents are routed to QiNote
> - Workflows fire
> 
> Think of Paperless as the **intake clerk + filing system**.
> 
> ---
> 
> ## So yes: you create the mail rules **inside Paperless**
> 
> Specifically:
> **Paperless UI → Mail Settings → Mail Rules**
> 
> Not Gmail filters.
> 
> ---
> 
> ## Minimal Gmail setup (what you should do right now)
> 
> In Gmail (for `intake@qially.com`):
> 
> **Option A (simplest, recommended now):**
> - No filters at all
> - Let Paperless poll the inbox
> - Inbox can be messy temporarily
> 
> **Option B (light cleanup, optional):**
> - Create a label: `Paperless`
> - Filter: `to:intake@qially.com`
> - Apply label `Paperless`
> - (Do NOT auto-delete)
> 
> That’s it. Nothing fancy.
> 
> ---
> 
> ## What mail rules you create INSIDE Paperless
> 
> Start with **only these two**. You can add more later.
> 
> ### Mail Rule 1 — Default Intake (required)
> This prevents mail loss.
> 
> **Paperless → Mail Rules → Add**
> 
> - **Name:** `Default Intake`
> - **Sort Order:** 100 (low priority)
> - **Account:** `QiAlly Intake`
> - **Conditions:** *(leave broad / empty)*
> 
> **Actions:**
> - ✅ Consume attachments
> - ✅ Assign tag: `email`
> - ✅ Assign tag: `received`
> 
> **Processed Mail:**
> - ✅ Mark as read
> - (Optional) Move to folder: `Processed/Paperless`
> 
> This rule guarantees:
> - Every attachment becomes a document
> - Nothing is skipped
> - OCR + ASN pipeline applies
> 
> ---
> 
> ### Mail Rule 2 — Legal / Case Mail (recommended)
> This adds intelligence without risk.
> 
> - **Name:** `Legal Mail`
> - **Sort Order:** 10 (higher priority than Default)
> - **Account:** `QiAlly Intake`
> - **Conditions:**
>   - From contains: `@courts.`
>   - OR Subject contains: `Order`, `Notice`, `Hearing`
> 
> **Actions:**
> - ✅ Consume attachments
> - ✅ Assign tags:
>   - `legal`
>   - `evidence`
>   - `email`
> 
> Paperless evaluates rules top-down.  
> If this matches, Default Intake never runs for that email.
> 
> ---
> 
> ## Now: what workflows we put in Paperless (this is separate from mail rules)
> 
> Mail rules = **how documents enter**  
> Workflows = **what happens after documents exist**
> 
> ### Workflow 1 — Ready for QiNote (core to your system)
> Trigger:
> - Document gets tag `Ready_for_QiNote`
> 
> Actions:
> - (Optional) Add tag: `exported`
> - (Optional) Add note or set custom field
> 
> Your **QiNote bridge** watches for this tag.  
> This keeps export explicit and controlled.
> 
> ---
> 
> ### Workflow 2 — ASN sanity check (optional, later)
> Trigger:
> - Document created
> - AND ASN is empty
> 
> Action:
> - Add tag: `needs_id`
> 
> This helps you catch documents that arrived without barcode IDs.
> 
> ---
> 
> ### Workflow 3 — Auto-classification assist (later)
> Trigger:
> - Tag contains `legal`
> 
> Action:
> - Suggest document type = `Court Filing`
> - Suggest correspondent = `Court` or `FCFCU`
> 
> Do NOT over-automate this yet. Trust comes later.
> 
> ---
> 
> ## What you should NOT do yet
> - ❌ Don’t recreate Gmail filters logic in Paperless
> - ❌ Don’t use Gmail filters to auto-delete
> - ❌ Don’t build 15 workflows on day one
> - ❌ Don’t auto-export everything to QiNote
> 
> ---
> 
> ## Final grounding statement (important)
> If you remember only one thing:
> 
> > **Gmail moves mail.  
> > Paperless decides meaning.  
> > QiNote stores knowledge.**
> 
> You’re doing this in the correct order.
> 
> ---
> 
> If you want, next we can:
> - Design the **exact Paperless workflows screen-by-screen**
> - Validate one test email end-to-end
> - Or design the **Ready_for_QiNote SOP** so future-you doesn’t forget why this is sane
> 
> Say which one.

### User
> Edit mail rule

> ID: 1

> 

> Name

> Intake

> Account

> Intake Gmail

> Order

> 1

> Enabled

> Paperless will only process mails that match all of the criteria specified below.

> 

> Folder

> intake

> Subfolders must be separated by a delimiter, often a dot ('.') or slash ('/'), but it varies by mail server.

> Maximum age (days)

> 30

> Filter from

> Filter to

> Filter subject

> Filter body

> Consumption scope

> Process message as .eml and attachments separately

> See docs for .eml processing requirements

> Attachment type

> Only process attachments

> PDF layout

> System default

> Include only files matching

> Optional. Wildcards e.g. *.pdf or *invoice* allowed. Can be comma-separated list. Case insensitive.

> Exclude files matching

> Optional. Wildcards e.g. *.pdf or *invoice* allowed. Can be comma-separated list. Case insensitive.

> Action

> Tag the mail with specified tag, don't process tagged mails

> Only performed if the mail is processed.

> Action parameter

> This field may not be blank.

> Assign title from

> Use subject as title

> Assign owner from rule

> 

> Tags

> Assign document type

> Assign correspondent from

> Use mail address

### Assistant
> Good — this screen tells me exactly where you are, and there are **three concrete fixes** you should make plus **one clarification about intent**. I’ll be precise.
> 
> ---
> 
> ## What you are doing right
> - You are editing a **Paperless mail rule** (correct place)
> - You named it **Intake** (fine)
> - You are using a dedicated **Intake Gmail** account (correct)
> - You are limiting to **attachments only** (correct default)
> - You are assigning title from **subject** (good)
> 
> Now let’s tighten this so it behaves exactly how you expect.
> 
> ---
> 
> ## Critical corrections (do these)
> 
> ### 1. **Order = 1 → WRONG for a catch-all**
> Order determines priority.  
> Lower number = higher priority.
> 
> If this is your **default intake rule**, it must be **LOW priority**, not high.
> 
> **Change:**
> - **Order:** `100`
> 
> Why:
> - You will later add more specific rules (Legal, Billing, Court)
> - Those should run first
> - This rule should only fire if nothing else matches
> 
> ---
> 
> ### 2. **Folder = intake → ONLY correct if Gmail label exists**
> Paperless will only process mail in this folder/label.
> 
> This must match **exactly** how Gmail exposes labels over IMAP.
> 
> If you created a Gmail label called `intake`, this is fine.  
> If not, Paperless will silently process **nothing**.
> 
> **Two safe options:**
> 
> #### Option A (safest right now)
> - **Clear the Folder field entirely**
> - Let Paperless read from INBOX
> 
> #### Option B (only if you verified label)
> - Keep `intake`
> - Confirm in Gmail:
>   - Label exists
>   - IMAP access is enabled for that label
> 
> If you are unsure: **clear it**.
> 
> ---
> 
> ### 3. **Action is misconfigured (this WILL block processing)**
> You selected:
> 
> > **“Tag the mail with specified tag, don’t process tagged mails”**
> 
> This is a **guard action**, not an intake action.
> 
> And the UI even tells you the problem:
> > *“This field may not be blank.”*
> 
> This action will either:
> - Prevent processing, or
> - Do nothing useful
> 
> **Fix:**
> - ❌ Remove this Action entirely
> - You do NOT need it for intake
> 
> Mail rules already only process once by default.
> 
> ---
> 
> ## Recommended final configuration (line by line)
> 
> ### Top section
> - **Name:** `Intake`
> - **Account:** `Intake Gmail`
> - **Order:** `100`
> - **Enabled:** ✅
> 
> ---
> 
> ### Criteria section
> - **Folder:** *(empty — unless you are 100% sure about the label)*
> - **Maximum age (days):** `30` (fine)
> - **Filter from / to / subject / body:** *(leave blank)*
> 
> This makes it a true catch-all.
> 
> ---
> 
> ### Consumption scope
> - **Process message as .eml and attachments separately:** ❌ OFF (for now)
> - **Attachment type:** `Only process attachments` ✅
> - **PDF layout:** `System default` ✅
> 
> This means:
> - PDFs get ingested
> - Email bodies do NOT become documents (cleaner for now)
> 
> ---
> 
> ### Include / Exclude
> - Leave **both blank** for now  
> You can add `*.pdf` later if needed, but Paperless already handles this well.
> 
> ---
> 
> ### Metadata assignment
> - **Assign title from:** `Use subject as title` ✅
> - **Assign owner from rule:** optional (leave blank unless you care)
> - **Tags:**  
>   - `email`
>   - `received`
> 
> (Add them explicitly here.)
> 
> - **Assign document type:** *(leave blank)*
> - **Assign correspondent from:** `Use mail address` ✅
> 
> ---
> 
> ## What this rule will now do (exact behavior)
> 
> For every email arriving in the mailbox:
> - Take attachments
> - Create documents
> - OCR them
> - Title = email subject
> - Correspondent = sender email
> - Tags = `email`, `received`
> - ASN/barcode logic applies if present
> - Nothing is blocked or skipped
> 
> This is the **correct baseline**.
> 
> ---
> 
> ## One important decision (answer yes/no)
> You currently have **“Only process attachments”**.
> 
> **Question:**  
> Do you want **email bodies themselves** (not just PDFs) stored as documents in Paperless?
> 
> - **No** → current setting is correct
> - **Yes** → we enable `.eml` processing and adjust one checkbox
> 
> Answer that and I’ll give you the exact toggle and why.
> 
> Once this rule is saved, the **next step** is:
> - add **one higher-priority rule** (Legal / Court), or
> - send a **test email** and verify it appears in Paperless correctly
> 
> Say which one you want to do next.

### User
> ok, we need to create tags adn document types and add a storage path before i can really set rules

### Assistant
> Correct instinct. You’re right: **define the ontology first**, then automation. If you skip this, you’ll be constantly refactoring rules and fixing metadata after the fact.
> 
> Below is a **clean, minimal, future-proof baseline** for **Tags**, **Document Types**, and **Storage Path** in Paperless that aligns with your QiNote / Gina pipeline and legal use cases.
> 
> I’ll keep this tight and decisive.
> 
> ---
> 
> # 1. Tags — create these first
> 
> Tags are **state, context, and routing**, not document identity.
> 
> ### A. Intake & lifecycle tags (mandatory)
> Create these exactly:
> 
> - `email`
> - `received`
> - `needs_review`
> - `needs_id`
> - `ready_for_qinote`
> - `exported`
> - `archived`
> 
> These let you:
> - control workflows
> - gate exports
> - debug intake problems
> - keep Paperless from becoming a dumping ground
> 
> ---
> 
> ### B. Legal / case context (you will use these constantly)
> Create now, even if unused today:
> 
> - `legal`
> - `evidence`
> - `court`
> - `finance`
> - `billing`
> - `utility`
> 
> Optional but useful:
> - `time_sensitive`
> - `certified_mail`
> - `service_issue`
> 
> ---
> 
> ### C. Project / case tags (lightweight)
> Create **only a few**, don’t explode this yet:
> 
> - `FCFCU_CASE`
> - `QIALLY_INTERNAL`
> 
> You can add more per case later. Don’t pre-create 50.
> 
> ---
> 
> ## 2. Document Types — keep this small and meaningful
> 
> Document Types should describe **what the document is**, not where it came from.
> 
> Create these:
> 
> ### Core (do these now)
> - `Court Filing`
> - `Court Order`
> - `Notice`
> - `Correspondence`
> - `Statement`
> - `Invoice`
> - `Receipt`
> - `Evidence`
> - `Contract`
> 
> That’s it for now.
> 
> Why:
> - These map cleanly to legal workflows
> - They’re understandable by humans
> - They’re stable over time
> - They’ll be useful for search, not noise
> 
> Do **not** create hyper-specific types yet (e.g. “Utility Bill – AES”). That’s tag territory.
> 
> ---
> 
> ## 3. Correspondents — let Paperless auto-create
> 
> Do **not** manually create correspondents yet.
> 
> Your rule:
> - **Assign correspondent from → Use mail address**
> 
> Paperless will auto-create correspondents as mail arrives. You can normalize them later (e.g., rename `noreply@courts.in.gov` → `Indiana Courts`).
> 
> This saves time and avoids premature cleanup.
> 
> ---
> 
> ## 4. Storage Path — set this BEFORE rules
> 
> This is important, and most people do it wrong.
> 
> ### The principle
> Storage path is **physical organization for humans**, not semantic meaning.
> 
> Your semantics live in:
> - tags
> - document types
> - QiNote sidecars
> - vector index
> 
> So keep the path **simple and stable**.
> 
> ---
> 
> ### Recommended Storage Path format
> 
> Go to:
> **Settings → Storage Paths → Add**
> 
> **Name:** `Default Structured Storage`
> 
> **Path pattern (copy exactly):**
> ```
> {{ document_type }}/{{ created_year }}/{{ correspondent }}
> ```
> 
> ### Why this works
> - Groups by document type (legal vs finance)
> - Buckets by year (court-safe, audit-safe)
> - Keeps correspondents visible
> - Doesn’t explode folder count
> - Survives reclassification
> 
> Examples:
> ```
> Court Filing/2026/Indiana Courts/
> Invoice/2025/AES Indiana/
> Correspondence/2026/FCFCU/
> ```
> 
> Clean. Predictable. Boring (that’s good).
> 
> ---
> 
> ### Optional: Evidence override path (later)
> Once stable, you can add a second path like:
> 
> ```
> Evidence/{{ created_year }}/{{ correspondent }}
> ```
> 
> But do **not** do this yet.
> 
> ---
> 
> ## 5. Assign the Storage Path
> 
> In **Settings → Storage Paths**:
> - Mark `Default Structured Storage` as **Default**
> 
> Do NOT try to assign storage paths via mail rules yet.
> 
> ---
> 
> ## 6. Now you’re ready to set rules (order matters)
> 
> Only after the above exists do you:
> 1. Save the **Intake** mail rule
> 2. Add a **Legal Mail** rule
> 3. Add a **Ready_for_QiNote workflow**
> 
> If you try to do rules first, you’ll be blocked or tempted to hack around missing structure.
> 
> ---
> 
> ## 7. Sanity check (answer these quickly)
> 
> Reply with:
> 1. ✅ Tags created (yes/no)
> 2. ✅ Document Types created (yes/no)
> 3. What **Storage Path pattern** you want to use (or “use yours”)
> 
> Once those are confirmed, I’ll give you:
> - the **exact final Intake rule**
> - the **Legal Mail rule**
> - the **Ready_for_QiNote workflow**
> - and the **minimal SOP** so future-you doesn’t break this under stress
> 
> You’re doing this in the right order. Keep going.

### User
> they can be nested too, so think tag groups then subtags

### Assistant
> Yes — and you’re thinking about this the **right way**. Nested tags let you encode meaning **without exploding rule complexity**, but only if you lock the hierarchy deliberately.
> 
> Below is a **clean, opinionated tag taxonomy** designed for:
> 
> - Paperless automation
> - Legal defensibility
> - QiNote / Gina downstream use
> - Minimal refactors later
> 
> I’ll give you **groups → subtags**, plus **rules on how to use them** so this doesn’t turn into chaos.
> 
> ---
> 
> # Core rule (read this once)
> - **Top-level tags = dimension**
> - **Subtags = values**
> - **Rules target top-level tags**
> - **Humans assign subtags**
> 
> If you violate this, automation becomes brittle.
> 
> ---
> 
> # Tag Groups (Top Level)
> 
> Create **only these top-level tags** first:
> 
> ```
> intake/
> status/
> source/
> domain/
> case/
> doc/
> priority/
> ```
> 
> Do **not** create free-floating tags outside these groups unless absolutely necessary.
> 
> ---
> 
> ## 1. `intake/*` — how it entered the system
> 
> **Purpose:** provenance + audit trail  
> **Mostly automatic**
> 
> ```
> intake/email
> intake/scan
> intake/upload
> intake/import
> ```
> 
> Rules:
> - Mail rules assign `intake/email`
> - Scanner workflows assign `intake/scan`
> - Manual uploads get `intake/upload`
> 
> Never mix intake with status or meaning.
> 
> ---
> 
> ## 2. `status/*` — lifecycle state (most important group)
> 
> **Purpose:** workflow control  
> **This drives automation**
> 
> ```
> status/received
> status/needs_review
> status/needs_id
> status/ready_for_qinote
> status/exported
> status/archived
> ```
> 
> Rules:
> - Only **one** `status/*` tag should be active at a time
> - Workflows trigger on `status/*`
> - Humans should change status consciously
> 
> This is your **state machine**.
> 
> ---
> 
> ## 3. `source/*` — where it came from externally
> 
> **Purpose:** external attribution  
> **Often automatic**
> 
> ```
> source/court
> source/bank
> source/utility
> source/vendor
> source/person
> ```
> 
> This answers: *“Who sent this?”*  
> Correspondent answers *“which one specifically?”*
> 
> ---
> 
> ## 4. `domain/*` — subject matter
> 
> **Purpose:** semantic grouping  
> **Used for search + context**
> 
> ```
> domain/legal
> domain/finance
> domain/billing
> domain/utility
> domain/operations
> ```
> 
> Rules:
> - `domain/*` is about **what it’s about**
> - Not about format
> - Not about workflow
> 
> ---
> 
> ## 5. `case/*` — project or matter association
> 
> **Purpose:** case-level grouping  
> **Sparse, intentional**
> 
> ```
> case/FCFCU
> case/QIALLY_INTERNAL
> case/AES
> ```
> 
> Rules:
> - Only create a `case/*` when there is a **real folder / matter**
> - Don’t pre-create hypothetical cases
> - A document can belong to multiple cases if needed
> 
> This maps cleanly to court binders.
> 
> ---
> 
> ## 6. `doc/*` — document meaning (optional but powerful)
> 
> **Purpose:** nuance beyond document type**
> 
> ```
> doc/evidence
> doc/contract
> doc/correspondence
> doc/statement
> doc/receipt
> ```
> 
> Why this exists:
> - Document Type = primary classification
> - `doc/*` = secondary semantics (search + vectors)
> 
> Example:
> - Document Type: `Court Filing`
> - Tag: `doc/evidence`
> 
> That’s useful later.
> 
> ---
> 
> ## 7. `priority/*` — urgency and risk
> 
> **Purpose:** triage**
> 
> ```
> priority/high
> priority/time_sensitive
> priority/deadline
> ```
> 
> Rules:
> - Use sparingly
> - Do not auto-assign unless very confident
> - This is human-facing more than machine-facing
> 
> ---
> 
> # How this maps to automation (important)
> 
> ### Mail Rule (example)
> - Incoming court email:
>   - `intake/email`
>   - `status/received`
>   - `source/court`
>   - `domain/legal`
> 
> ### Workflow trigger
> - Trigger: `status/ready_for_qinote`
> - Action: export → add `status/exported`
> 
> ### Bridge logic
> - Read:
>   - `case/*` → QiNote project
>   - `domain/*` → semantic context
>   - `doc/*` → embedding hints
>   - `status/*` → pipeline gate
> 
> This is clean, inspectable, and explainable.
> 
> ---
> 
> # What NOT to do (learned the hard way)
> - ❌ Don’t put case names at top level
> - ❌ Don’t encode status as free-text tags
> - ❌ Don’t mix intake + meaning in one tag
> - ❌ Don’t let automation assign `case/*` unless deterministic
> 
> ---
> 
> # Your next concrete step (do this now)
> 
> 1. Create the **top-level groups**
> 2. Create **only the subtags listed above**
> 3. Do **not** invent extras yet
> 
> Then tell me:
> - “Tags created”
> - And whether you want **slash (`/`) or dot (`.`)** notation long-term  
>   (Paperless supports both; slash is more readable, dot is more grep-friendly)
> 
> Once that’s done, I’ll:
> - Update your **Intake mail rule** to use these
> - Design the **Legal Mail rule**
> - Design the **Ready_for_QiNote workflow**
> - Align this with your **QiNote vault taxonomy**
> 
> You’re setting a foundation most people skip. This will pay off.

### User
> now for document types

### Assistant
> Good — document types are where people usually overthink. We’re going to do this **deliberately boring, legally defensible, and automation-friendly**.
> 
> Paperless **does not support nested document types** the way tags do, so the design rule is:
> 
> > **Document Type = primary legal/functional classification**  
> > **Nuance lives in tags (`doc/*`, `domain/*`, `case/*`)**
> 
> If you try to encode hierarchy into document types, you’ll regret it.
> 
> ---
> 
> # Document Type Design Rules (lock these)
> 
> 1. **One document = one document type**
> 2. Document type answers: *“What is this, formally?”*
> 3. Do **not** encode:
>    - case
>    - source
>    - urgency
>    - lifecycle
> 4. If two humans would argue about which type it is → it’s too granular
> 
> ---
> 
> # Your Canonical Document Types (create exactly these)
> 
> ## A. Legal / Court (core)
> These must exist for court work and evidence handling.
> 
> - **Court Filing**  
>   (complaints, motions, briefs, responses)
> 
> - **Court Order**  
>   (orders, rulings, judgments)
> 
> - **Notice**  
>   (notices of hearing, default, sale, service)
> 
> - **Legal Correspondence**  
>   (letters/emails between parties, counsel, court)
> 
> - **Evidence**  
>   (exhibits, screenshots, logs, photos, recordings)
> 
> ---
> 
> ## B. Financial
> Keep this tight — finance explodes fast if you don’t.
> 
> - **Statement**  
>   (bank, utility, account statements)
> 
> - **Invoice**  
>   (bills requesting payment)
> 
> - **Receipt**  
>   (proof of payment)
> 
> ---
> 
> ## C. Administrative / Business
> These support operations without bleeding into legal semantics.
> 
> - **Contract**  
>   (agreements, leases, service contracts)
> 
> - **Policy / Terms**  
>   (policies, disclosures, TOS)
> 
> - **General Correspondence**  
>   (everything non-legal, non-financial)
> 
> ---
> 
> ## D. Intake / System (optional but useful)
> Only add these if you want clarity during ingestion.
> 
> - **Scanned Document**  
>   (raw scan before review)
> 
> - **Email Message** *(optional)*  
>   Only if you later decide to store `.eml` bodies as documents
> 
> You can skip these for now if you prefer.
> 
> ---
> 
> # Final Recommended List (copy/paste checklist)
> 
> Create **only these** to start:
> 
> ```
> Court Filing
> Court Order
> Notice
> Legal Correspondence
> Evidence
> Statement
> Invoice
> Receipt
> Contract
> Policy / Terms
> General Correspondence
> ```
> 
> That’s it.  
> 11 types. Stable. Explainable. Court-safe.
> 
> ---
> 
> # How this pairs with your tag hierarchy (example)
> 
> A court PDF might look like:
> 
> - **Document Type:** `Court Order`
> - **Tags:**
>   - `intake/email`
>   - `status/received`
>   - `domain/legal`
>   - `case/FCFCU`
>   - `doc/evidence`
>   - `source/court`
> 
> This gives you:
> - strong filtering
> - future-proof automation
> - clean exports to QiNote
> - sane vector context
> 
> ---
> 
> # What NOT to create (very important)
> 
> Do **not** create things like:
> - `Utility Bill`
> - `Bank Statement – Chase`
> - `FCFCU Filing`
> - `Court Evidence – Photos`
> - `Email Attachment`
> 
> Those belong in **tags**, not document types.
> 
> ---
> 
> # Storage Path reminder (ties this together)
> 
> Because your storage path is:
> ```
> {{ document_type }}/{{ created_year }}/{{ correspondent }}
> ```
> 
> This structure only works if document types are:
> - few
> - stable
> - human-readable
> 
> Which this set is.
> 
> ---
> 
> ## Next step (choose one)
> 1. ✅ Confirm document types created  
> 2. Build **final Intake mail rule** using nested tags  
> 3. Build **Legal Mail rule**  
> 4. Define **Ready_for_QiNote workflow** (state machine)
> 
> Tell me the number.

### User
> ok so what storage paths should we create. these ae the optoins. Create new storage path

> 

> Name

> Path

> See the documentation.

> Preview

> Matching algorithm

> Auto: Learn matching automatically

> Edit Permissions

### Assistant
> Good — this is the **last structural decision** before rules, and it’s important you don’t overbuild it.
> 
> Paperless storage paths are **physical layout only**.  
> They should be **boring, stable, and predictable**.  
> All intelligence lives in **tags + document types + QiNote**.
> 
> Below is the **exact setup I recommend**, including what *not* to do.
> 
> ---
> 
> # Core principle (do not violate this)
> 
> - **One default storage path**
> - **No case-specific paths**
> - **No workflow-driven paths (yet)**
> - **Auto matching only**
> 
> If you create many paths now, you’ll fight Paperless instead of using it.
> 
> ---
> 
> # Storage Path #1 — DEFAULT (create this first)
> 
> ### Name
> ```
> Default Structured Storage
> ```
> 
> ### Path (copy exactly)
> ```
> {{ document_type }}/{{ created_year }}/{{ correspondent }}
> ```
> 
> ### Why this is correct
> - Groups by **what it is** (document type)
> - Buckets by **year** (court-safe, audit-safe)
> - Keeps **sender visible**
> - Stable even if tags/cases change
> - Does not explode folder count
> 
> ### Example results
> ```
> Court Filing/2026/Indiana Courts/
> Invoice/2025/AES Indiana/
> Legal Correspondence/2026/FCFCU/
> Evidence/2026/Screenshots/
> ```
> 
> This is exactly what you want when browsing raw files.
> 
> ---
> 
> ### Matching algorithm
> **Auto: Learn matching automatically**
> 
> Do **not** manually define conditions.
> 
> Why:
> - Paperless learns over time
> - Less brittle
> - You won’t paint yourself into a corner
> 
> ---
> 
> ### Edit permissions
> Leave default (no restrictions).
> 
> ---
> 
> ### Set as default
> After saving:
> - Mark this path as **Default**
> 
> This ensures **every document lands somewhere sane**, even before rules.
> 
> ---
> 
> # Storage Path #2 — OPTIONAL (do NOT create yet)
> 
> I’m calling this out explicitly so you don’t jump ahead.
> 
> You *may later* add:
> 
> ```
> Evidence/{{ created_year }}/{{ correspondent }}
> ```
> 
> …but **only after**:
> - you’ve ingested real documents
> - you trust your tagging
> - you see actual value in splitting Evidence physically
> 
> Right now, **don’t add it**.
> 
> ---
> 
> # What you should NOT create (seriously)
> 
> Do **not** create paths like:
> - `case/{{ tags }}`
> - `{{ tags }}/{{ document_type }}`
> - `{{ correspondent }}/{{ case }}`
> - Anything with `status/*`
> 
> Those look clever and always fail long-term:
> - tags change
> - cases merge
> - documents get reclassified
> - files move unexpectedly
> 
> Paperless handles that poorly.
> 
> ---
> 
> # Sanity check before you save
> 
> Confirm this mentally:
> 
> - Can I find a document **without knowing the case tag**? → Yes  
> - Will this break if I reclassify later? → No  
> - Will this survive exporting to QiNote? → Yes  
> - Is this boring enough? → Yes (that’s good)
> 
> ---
> 
> # After this, you are ready for rules
> 
> Once this storage path exists and is default, the next steps are **in order**:
> 
> 1. Finalize **Intake mail rule** (with nested tags)
> 2. Add **Legal Mail rule**
> 3. Add **Ready_for_QiNote workflow**
> 4. Test one email end-to-end
> 
> Tell me when the storage path is created and defaulted, and I’ll give you the **exact final rule configs** next.

### User
> doble cgeck Skip to content

> Paperless-ngx

> Advanced Topics

> 

> 

> Search

> 

>  paperless-ngx/paperless-ngx

> v2.20.3

> 35.3k

> 2.2k

> logoPaperless-ngx

> Home

> Setup

> Basic Usage

> Configuration

> Administration

> Advanced Topics

> Table of contents

> Matching tags, correspondents, document types, and storage paths

> Automatic matching

> Hooking into the consumption process

> Pre-consumption script

> Post-consumption script

> Docker

> File name handling

> Placeholders

> Empty placeholders

> Storage paths

> Filename Templates

> Custom Jinja2 Filters

> Custom Field Access

> Syntax

> Parameters

> Returns

> Examples

> Datetime Formatting

> Syntax

> Parameters

> Returns

> Examples

> Date Localization

> Syntax

> Parameters

> Returns

> Examples

> Format Presets

> Additional Variables

> Examples

> Automatic recovery of invalid PDFs

> Celery Monitoring

> Custom Container Initialization

> MySQL Caveats

> Case Sensitivity

> Missing timezones

> Barcodes

> Document Splitting

> Archive Serial Number Assignment

> Tag Assignment

> Automatic collation of double-sided documents

> Summary

> Usage example

> Things that could go wrong

> Interaction with "subdirs as tags"

> Interaction with document splitting

> SSO and third party authentication with Paperless-ngx

> Remote User authentication

> OpenID Connect and social authentication

> Disabling Regular Login

> Decryption of encrypted emails before consumption

> Requirements

> Setup

> Troubleshooting

> REST API

> Development

> FAQs

> Troubleshooting

> Changelog

> Advanced Topics

> Paperless offers a couple of features that automate certain tasks and make your life easier.

> 

> Matching tags, correspondents, document types, and storage paths

> Paperless will compare the matching algorithms defined by every tag, correspondent, document type, and storage path in your database to see if they apply to the text in a document. In other words, if you define a tag called Home Utility that had a match property of bc hydro and a matching_algorithm of Exact, Paperless will automatically tag your newly-consumed document with your Home Utility tag so long as the text bc hydro appears in the body of the document somewhere.

> 

> The matching logic is quite powerful. It supports searching the text of your document with different algorithms, and as such, some experimentation may be necessary to get things right.

> 

> In order to have a tag, correspondent, document type, or storage path assigned automatically to newly consumed documents, assign a match and matching algorithm using the web interface. These settings define when to assign tags, correspondents, document types, and storage paths to documents.

> 

> The following algorithms are available:

> 

> None: No matching will be performed.

> Any: Looks for any occurrence of any word provided in match in the PDF. If you define the match as Bank1 Bank2, it will match documents containing either of these terms.

> All: Requires that every word provided appears in the PDF, albeit not in the order provided.

> Exact: Matches only if the match appears exactly as provided (i.e. preserve ordering) in the PDF.

> Regular expression: Parses the match as a regular expression and tries to find a match within the document.

> Fuzzy match: Uses a partial matching based on locating the tag text inside the document, using a partial ratio

> Auto: Tries to automatically match new documents. This does not require you to set a match. See the notes below.

> When using the any or all matching algorithms, you can search for terms that consist of multiple words by enclosing them in double quotes. For example, defining a match text of "Bank of America" BofA using the any algorithm, will match documents that contain either "Bank of America" or "BofA", but will not match documents containing "Bank of South America".

> 

> Then just save your tag, correspondent, document type, or storage path and run another document through the consumer. Once complete, you should see the newly-created document, automatically tagged with the appropriate data.

> 

> Automatic matching

> Paperless-ngx comes with a new matching algorithm called Auto. This matching algorithm tries to assign tags, correspondents, document types, and storage paths to your documents based on how you have already assigned these on existing documents. It uses a neural network under the hood.

> 

> If, for example, all your bank statements of your account 123 at the Bank of America are tagged with the tag "bofa123" and the matching algorithm of this tag is set to Auto, this neural network will examine your documents and automatically learn when to assign this tag.

> 

> Paperless tries to hide much of the involved complexity with this approach. However, there are a couple caveats you need to keep in mind when using this feature:

> 

> Changes to your documents are not immediately reflected by the matching algorithm. The neural network needs to be trained on your documents after changes. Paperless periodically (default: once each hour) checks for changes and does this automatically for you.

> The Auto matching algorithm only takes documents into account which are NOT placed in your inbox (i.e. have any inbox tags assigned to them). This ensures that the neural network only learns from documents which you have correctly tagged before.

> The matching algorithm can only work if there is a correlation between the tag, correspondent, document type, or storage path and the document itself. Your bank statements usually contain your bank account number and the name of the bank, so this works reasonably well, However, tags such as "TODO" cannot be automatically assigned.

> The matching algorithm needs a reasonable number of documents to identify when to assign tags, correspondents, storage paths, and types. If one out of a thousand documents has the correspondent "Very obscure web shop I bought something five years ago", it will probably not assign this correspondent automatically if you buy something from them again. The more documents, the better.

> Paperless also needs a reasonable amount of negative examples to decide when not to assign a certain tag, correspondent, document type, or storage path. This will usually be the case as you start filling up paperless with documents. Example: If all your documents are either from "Webshop" or "Bank", paperless will assign one of these correspondents to ANY new document, if both are set to automatic matching.

> Hooking into the consumption process

> Sometimes you may want to do something arbitrary whenever a document is consumed. Rather than try to predict what you may want to do, Paperless lets you execute scripts of your own choosing just before or after a document is consumed using a couple of simple hooks.

> 

> Just write a script, put it somewhere that Paperless can read & execute, and then put the path to that script in paperless.conf or docker-compose.env with the variable name of either PAPERLESS_PRE_CONSUME_SCRIPT or PAPERLESS_POST_CONSUME_SCRIPT.

> 

> Info

> 

> These scripts are executed in a blocking process, which means that if a script takes a long time to run, it can significantly slow down your document consumption flow. If you want things to run asynchronously, you'll have to fork the process in your script and exit.

> 

> Pre-consumption script

> Executed after the consumer sees a new document in the consumption folder, but before any processing of the document is performed. This script can access the following relevant environment variables set:

> 

> Environment Variable	Description

> DOCUMENT_SOURCE_PATH	Original path of the consumed document

> DOCUMENT_WORKING_PATH	Path to a copy of the original that consumption will work on

> TASK_ID	UUID of the task used to process the new document (if any)

> Note

> 

> Pre-consume scripts which modify the document should only change the DOCUMENT_WORKING_PATH file or a second consume task may be triggered, leading to failures as two tasks work on the same document path

> 

> Warning

> 

> If your script modifies DOCUMENT_WORKING_PATH in a non-deterministic way, this may allow duplicate documents to be stored

> 

> A simple but common example for this would be creating a simple script like this:

> 

> /usr/local/bin/ocr-pdf

> 

> #!/usr/bin/env bash

> pdf2pdfocr.py -i ${DOCUMENT_WORKING_PATH}

> /etc/paperless.conf

> 

> ...

> PAPERLESS_PRE_CONSUME_SCRIPT="/usr/local/bin/ocr-pdf"

> ...

> This will pass the path to the document about to be consumed to /usr/local/bin/ocr-pdf, which will in turn call pdf2pdfocr.py on your document, which will then overwrite the file with an OCR'd version of the file and exit. At which point, the consumption process will begin with the newly modified file.

> 

> The script's stdout and stderr will be logged line by line to the webserver log, along with the exit code of the script.

> 

> Post-consumption script

> Executed after the consumer has successfully processed a document and has moved it into paperless. It receives the following environment variables:

> 

> Environment Variable	Description

> DOCUMENT_ID	Database primary key of the document

> DOCUMENT_FILE_NAME	Formatted filename, not including paths

> DOCUMENT_TYPE	The document type (if any)

> DOCUMENT_CREATED	Date & time when document created

> DOCUMENT_MODIFIED	Date & time when document was last modified

> DOCUMENT_ADDED	Date & time when document was added

> DOCUMENT_SOURCE_PATH	Path to the original document file

> DOCUMENT_ARCHIVE_PATH	Path to the generate archive file (if any)

> DOCUMENT_THUMBNAIL_PATH	Path to the generated thumbnail

> DOCUMENT_DOWNLOAD_URL	URL for document download

> DOCUMENT_THUMBNAIL_URL	URL for the document thumbnail

> DOCUMENT_OWNER	Username of the document owner (if any)

> DOCUMENT_CORRESPONDENT	Assigned correspondent (if any)

> DOCUMENT_TAGS	Comma separated list of tags applied (if any)

> DOCUMENT_ORIGINAL_FILENAME	Filename of original document

> TASK_ID	Task UUID used to import the document (if any)

> The script can be in any language, A simple shell script example:

> 

> post-consumption-example

> #!/usr/bin/env bash

> 

> echo "

> 

> A document with an id of ${DOCUMENT_ID} was just consumed.  I know the

> following additional information about it:

> 

> * Generated File Name: ${DOCUMENT_FILE_NAME}

> * Document type: ${DOCUMENT_TYPE}

> * Archive Path: ${DOCUMENT_ARCHIVE_PATH}

> * Source Path: ${DOCUMENT_SOURCE_PATH}

> * Created: ${DOCUMENT_CREATED}

> * Added: ${DOCUMENT_ADDED}

> * Modified: ${DOCUMENT_MODIFIED}

> * Thumbnail Path: ${DOCUMENT_THUMBNAIL_PATH}

> * Download URL: ${DOCUMENT_DOWNLOAD_URL}

> * Thumbnail URL: ${DOCUMENT_THUMBNAIL_URL}

> * Owner Name: ${DOCUMENT_OWNER}

> * Correspondent: ${DOCUMENT_CORRESPONDENT}

> * Tags: ${DOCUMENT_TAGS}

> 

> It was consumed with the passphrase ${PASSPHRASE}

> 

> "

> Note

> 

> The post consumption script cannot cancel the consumption process.

> 

> Warning

> 

> The post consumption script should not modify the document files directly.

> 

> The script's stdout and stderr will be logged line by line to the webserver log, along with the exit code of the script.

> 

> Docker

> To hook into the consumption process when using Docker, you will need to pass the scripts into the container via a host mount in your docker-compose.yml.

> 

> Assuming you have /home/paperless-ngx/scripts/post-consumption-example.sh as a script which you'd like to run.

> 

> You can pass that script into the consumer container via a host mount:

> 

> ...

> webserver:

>   ...

>   volumes:

>     ...

>     - /home/paperless-ngx/scripts:/path/in/container/scripts/ 

>   environment: 

>     ...

>     PAPERLESS_POST_CONSUME_SCRIPT: /path/in/container/scripts/post-consumption-example.sh 

> ...

> Troubleshooting:

> 

> Monitor the Docker Compose log cd ~/paperless-ngx; docker compose logs -f

> Check your script's permission e.g. in case of permission error sudo chmod 755 post-consumption-example.sh

> Pipe your scripts's output to a log file e.g. echo "${DOCUMENT_ID}" | tee --append /usr/src/paperless/scripts/post-consumption-example.log

> File name handling

> By default, paperless stores your documents in the media directory and renames them using the identifier which it has assigned to each document. You will end up getting files like 0000123.pdf in your media directory. This isn't necessarily a bad thing, because you normally don't have to access these files manually. However, if you wish to name your files differently, you can do that by adjusting the PAPERLESS_FILENAME_FORMAT configuration option or using storage paths (see below). Paperless adds the correct file extension e.g. .pdf, .jpg automatically.

> 

> This variable allows you to configure the filename (folders are allowed) using placeholders. For example, configuring this to

> 

> PAPERLESS_FILENAME_FORMAT={{ created_year }}/{{ correspondent }}/{{ title }}

> will create a directory structure as follows:

> 

> 2019/

>   My bank/

>     Statement January.pdf

>     Statement February.pdf

> 2020/

>   My bank/

>     Statement January.pdf

>     Letter.pdf

>     Letter_01.pdf

>   Shoe store/

>     My new shoes.pdf

> Warning

> 

> Do not manually move your files in the media folder. Paperless remembers the last filename a document was stored as. If you do rename a file, paperless will report your files as missing and won't be able to find them.

> 

> Tip

> 

> Paperless checks the filename of a document whenever it is saved. Changing (or deleting) a storage path will automatically be reflected in the file system. However, when changing PAPERLESS_FILENAME_FORMAT you will need to manually run the document renamer to move any existing documents.

> 

> Placeholders

> Paperless provides the following variables for use within filenames:

> 

> {{ asn }}: The archive serial number of the document, or "none".

> {{ correspondent }}: The name of the correspondent, or "none".

> {{ document_type }}: The name of the document type, or "none".

> {{ tag_list }}: A comma separated list of all tags assigned to the document.

> {{ title }}: The title of the document.

> {{ created }}: The full date (ISO 8601 format, e.g. 2024-03-14) the document was created.

> {{ created_year }}: Year created only, formatted as the year with century.

> {{ created_year_short }}: Year created only, formatted as the year without century, zero padded.

> {{ created_month }}: Month created only (number 01-12).

> {{ created_month_name }}: Month created name, as per locale

> {{ created_month_name_short }}: Month created abbreviated name, as per locale

> {{ created_day }}: Day created only (number 01-31).

> {{ added }}: The full date (ISO format) the document was added to paperless.

> {{ added_year }}: Year added only.

> {{ added_year_short }}: Year added only, formatted as the year without century, zero padded.

> {{ added_month }}: Month added only (number 01-12).

> {{ added_month_name }}: Month added name, as per locale

> {{ added_month_name_short }}: Month added abbreviated name, as per locale

> {{ added_day }}: Day added only (number 01-31).

> {{ owner_username }}: Username of document owner, if any, or "none"

> {{ original_name }}: Document original filename, minus the extension, if any, or "none"

> {{ doc_pk }}: The paperless identifier (primary key) for the document.

> Warning

> 

> When using file name placeholders, in particular when using {tag_list}, you may run into the limits of your operating system's maximum path lengths. In that case, files will retain the previous path instead and the issue logged.

> 

> Tip

> 

> These variables are all simple strings, but the format can be a full template. See Filename Templates for even more advanced formatting.

> 

> Paperless will try to conserve the information from your database as much as possible. However, some characters that you can use in document titles and correspondent names (such as : \ / and a couple more) are not allowed in filenames and will be replaced with dashes.

> 

> If paperless detects that two documents share the same filename, paperless will automatically append _01, _02, etc to the filename. This happens if all the placeholders in a filename evaluate to the same value.

> 

> If there are any errors in the placeholders included in PAPERLESS_FILENAME_FORMAT, paperless will fall back to using the default naming scheme instead.

> 

> Caution

> 

> As of now, you could potentially tell paperless to store your files anywhere outside the media directory by setting

> 

> PAPERLESS_FILENAME_FORMAT=../../my/custom/location/{title}

> However, keep in mind that inside docker, if files get stored outside of the predefined volumes, they will be lost after a restart.

> 

> Empty placeholders

> You can affect how empty placeholders are treated by changing the PAPERLESS_FILENAME_FORMAT_REMOVE_NONE setting.

> 

> Enabling this results in all empty placeholders resolving to "" instead of "none" as stated above. Spaces before empty placeholders are removed as well, empty directories are omitted.

> 

> Storage paths

> When a single storage layout is not sufficient for your use case, storage paths allow for more complex structure to set precisely where each document is stored in the file system.

> 

> Each storage path is a PAPERLESS_FILENAME_FORMAT and follows the rules described above

> Each document is assigned a storage path using the matching algorithms described above, but can be overwritten at any time

> For example, you could define the following two storage paths:

> 

> Normal communications are put into a folder structure sorted by year/correspondent

> Communications with insurance companies are stored in a flat structure with longer file names, but containing the full date of the correspondence.

> By Year = {{ created_year }}/{{ correspondent }}/{{ title }}

> Insurances = Insurances/{{ correspondent }}/{{ created_year }}-{{ created_month }}-{{ created_day }} {{ title }}

> If you then map these storage paths to the documents, you might get the following result. For simplicity, By Year defines the same structure as in the previous example above.

> 

> 2019/                                   # By Year

>    My bank/

>      Statement January.pdf

>      Statement February.pdf

> 

> Insurances/                             # Insurances

>    Healthcare 123/

>      2022-01-01 Statement January.pdf

>      2022-02-02 Letter.pdf

>      2022-02-03 Letter.pdf

>    Dental 456/

>      2021-12-01 New Conditions.pdf

> Tip

> 

> Defining a storage path is optional. If no storage path is defined for a document, the global PAPERLESS_FILENAME_FORMAT is applied.

> 

> Filename Templates

> The filename formatting uses Jinja templates to build the filename. This allows for complex logic to be included in the format, including logical structures and filters to manipulate the variables provided. The template is provided as a string, potentially multiline, and rendered into a single line.

> 

> In addition, the entire Document instance is available to be utilized in a more advanced way, as well as some variables which only make sense to be accessed with more complex logic.

> 

> Custom Jinja2 Filters

> Custom Field Access

> The get_cf_value filter retrieves a value from custom field data with optional default fallback.

> 

> Syntax

> {{ custom_fields | get_cf_value('field_name') }}

> {{ custom_fields | get_cf_value('field_name', 'default_value') }}

> Parameters

> custom_fields: This must be the provided custom field data

> name (str): Name of the custom field to retrieve

> default (str, optional): Default value to return if field is not found or has no value

> Returns

> str | None: The field value, default value, or None if neither exists

> Examples

> <!-- Basic usage -->

> {{ custom_fields | get_cf_value('department') }}

> 

> <!-- With default value -->

> {{ custom_fields | get_cf_value('phone', 'Not provided') }}

> Datetime Formatting

> The datetime filter formats a datetime string or datetime object using Python's strftime formatting.

> 

> Syntax

> {{ datetime_value | datetime('%Y-%m-%d %H:%M:%S') }}

> Parameters

> value (str | datetime): Date/time value to format (strings will be parsed automatically)

> format (str): Python strftime format string

> Returns

> str: Formatted datetime string

> Examples

> <!-- Format datetime object -->

> {{ created | datetime('%B %d, %Y at %I:%M %p') }}

> <!-- Output: "January 15, 2024 at 02:30 PM" -->

> 

> <!-- Custom formatting -->

> {{ custom_fields | get_cf_value('Date Field') | datetime('%A, %B %d, %Y') }}

> <!-- Output: "Monday, January 15, 2024" -->

> See the strftime format code documentation for the possible codes and their meanings.

> 

> Date Localization

> The localize_date filter formats a date or datetime object into a localized string using Babel internationalization. This takes into account the provided locale for translation. Since this must be used on a date or datetime object, you must access the field directly, i.e. document.created. An ISO string can also be provided to control the output format.

> 

> Syntax

> {{ date_value | localize_date('medium', 'en_US') }}

> {{ datetime_value | localize_date('short', 'fr_FR') }}

> Parameters

> value (date | datetime | str): Date, datetime object or ISO string to format (datetime should be timezone-aware)

> format (str): Format type - either a Babel preset ('short', 'medium', 'long', 'full') or custom pattern

> locale (str): Locale code for localization (e.g., 'en_US', 'fr_FR', 'de_DE')

> Returns

> str: Localized, formatted date string

> Examples

> <!-- Preset formats -->

> {{ document.created | localize_date('short', 'en_US') }}

> <!-- Output: "1/15/24" -->

> 

> {{ document.created | localize_date('medium', 'en_US') }}

> <!-- Output: "Jan 15, 2024" -->

> 

> {{ document.created | localize_date('long', 'en_US') }}

> <!-- Output: "January 15, 2024" -->

> 

> {{ document.created | localize_date('full', 'en_US') }}

> <!-- Output: "Monday, January 15, 2024" -->

> 

> <!-- Different locales -->

> {{ document.created | localize_date('medium', 'fr_FR') }}

> <!-- Output: "15 janv. 2024" -->

> 

> {{ document.created | localize_date('medium', 'de_DE') }}

> <!-- Output: "15.01.2024" -->

> 

> <!-- Custom patterns -->

> {{ document.created | localize_date('dd/MM/yyyy', 'en_GB') }}

> <!-- Output: "15/01/2024" -->

> See the supported format codes for more options.

> 

> Format Presets

> short: Abbreviated format (e.g., "1/15/24")

> medium: Medium-length format (e.g., "Jan 15, 2024")

> long: Long format with full month name (e.g., "January 15, 2024")

> full: Full format including day of week (e.g., "Monday, January 15, 2024")

> Additional Variables

> {{ tag_name_list }}: A list of tag names applied to the document, ordered by the tag name. Note this is a list, not a single string

> {{ custom_fields }}: A mapping of custom field names to their type and value. A user can access the mapping by field name or check if a field is applied by checking its existence in the variable.

> Tip

> 

> To access a custom field which has a space in the name, use the get_cf_value filter. See the examples below. This helps get fields by name and handle a default value if the named field is not attached to a Document.

> 

> Examples

> This example will construct a path based on the archive serial number range:

> 

> somepath/

> {% if document.archive_serial_number >= 0 and document.archive_serial_number <= 200 %}

>   asn-000-200/{{title}}

> {% elif document.archive_serial_number >= 201 and document.archive_serial_number <= 400 %}

>   asn-201-400

>   {% if document.archive_serial_number >= 201 and document.archive_serial_number < 300 %}

>     /asn-2xx

>   {% elif document.archive_serial_number >= 300 and document.archive_serial_number < 400 %}

>     /asn-3xx

>   {% endif %}

> {% endif %}

> /{{ title }}

> For a document with an ASN of 205, it would result in somepath/asn-201-400/asn-2xx/Title.pdf, but a document with an ASN of 355 would be placed in somepath/asn-201-400/asn-3xx/Title.pdf.

> 

> {% if document.mime_type == "application/pdf" %}

>   pdfs

> {% elif document.mime_type == "image/png" %}

>   pngs

> {% else %}

>   others

> {% endif %}

> /{{ title }}

> For a PDF document, it would result in pdfs/Title.pdf, but for a PNG document, the path would be pngs/Title.png.

> 

> To use custom fields:

> 

> {% if "Invoice" in custom_fields %}

>   invoices/{{ custom_fields.Invoice.value }}

> {% else %}

>   not-invoices/{{ title }}

> {% endif %}

> If the document has a custom field named "Invoice" with a value of 123, it would be filed into the invoices/123.pdf, but a document without the custom field would be filed to not-invoices/Title.pdf

> 

> If the custom field is named "Invoice Number", you would access the value of it via the get_cf_value filter due to quirks of the Django Template Language:

> 

> "invoices/{{ custom_fields|get_cf_value('Invoice Number') }}"

> You can also use a custom datetime filter to format dates:

> 

> invoices/

> {{ custom_fields|get_cf_value("Date Field","2024-01-01")|datetime('%Y') }}/

> {{ custom_fields|get_cf_value("Date Field","2024-01-01")|datetime('%m') }}/

> {{ custom_fields|get_cf_value("Date Field","2024-01-01")|datetime('%d') }}/

> Invoice_{{ custom_fields|get_cf_value("Select Field") }}_{{ custom_fields|get_cf_value("Date Field","2024-01-01")|replace("-", "") }}.pdf

> This will create a path like invoices/2022/01/01/Invoice_OptionTwo_20220101.pdf if the custom field "Date Field" is set to January 1, 2022 and "Select Field" is set to OptionTwo.

> 

> You can also use a custom slugify filter to slufigy text:

> 

> {{ title | slugify }}

> Automatic recovery of invalid PDFs

> Paperless will attempt to "clean" certain invalid PDFs with qpdf before processing if, for example, the mime_type detection is incorrect. This can happen if the PDF is not properly formatted or contains errors.

> 

> Celery Monitoring

> The monitoring tool Flower can be used to view more detailed information about the health of the celery workers used for asynchronous tasks. This includes details on currently running, queued and completed tasks, timing and more. Flower can also be used with Prometheus, as it exports metrics. For details on its capabilities, refer to the Flower documentation.

> 

> Flower can be enabled with the setting PAPERLESS_ENABLE_FLOWER. To configure Flower further, create a flowerconfig.py and place it into the src/paperless directory. For a Docker installation, you can use volumes to accomplish this:

> 

> services:

>     # ...

>     webserver:

>         environment:

>             - PAPERLESS_ENABLE_FLOWER

>         ports:

>             - 5555:5555 

>         # ...

>         volumes:

>             - /path/to/my/flowerconfig.py:/usr/src/paperless/src/paperless/flowerconfig.py:ro 

> Custom Container Initialization

> The Docker image includes the ability to run custom user scripts during startup. This could be utilized for installing additional tools or Python packages, for example. Scripts are expected to be shell scripts.

> 

> To utilize this, mount a folder containing your scripts to the custom initialization directory, /custom-cont-init.d and place scripts you wish to run inside. For security, the folder must be owned by root and should have permissions of a=rx. Additionally, scripts must only be writable by root.

> 

> Your scripts will be run directly before the webserver completes startup. Scripts will be run by the root user. If you would like to switch users, the utility gosu is available and preferred over sudo.

> 

> This is an advanced functionality with which you could break functionality or lose data. If you experience issues, please disable any custom scripts and try again before reporting an issue.

> 

> For example, using Docker Compose:

> 

> services:

>     # ...

>     webserver:

>         # ...

>         volumes:

>             - /path/to/my/scripts:/custom-cont-init.d:ro 

> MySQL Caveats

> Case Sensitivity

> The database interface does not provide a method to configure a MySQL database to be case-sensitive. A case-insensitive database prevents a user from creating a tag Name and NAME as they are considered the same.

> 

> However, there is a downside to turning on case sensitivity, as it also makes searches case-sensitive, so for example a document with the title Invoice won't be found when searching for invoice.

> 

> Per Django documentation, making a database case-sensitive requires manual intervention. To enable case sensitive tables, you can execute the following command against each table:

> 

> ALTER TABLE <table_name> CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

> 

> You can also set the default for new tables (this does NOT affect existing tables) with:

> 

> ALTER DATABASE <db_name> CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

> 

> Warning

> 

> Using mariadb version 10.4+ is recommended. Using the utf8mb3 character set on an older system may fix issues that can arise while setting up Paperless-ngx but utf8mb3 can cause issues with consumption (where utf8mb4 does not).

> 

> For more information on this topic, you can refer to this Django issue.

> 

> Missing timezones

> MySQL as well as MariaDB do not have any timezone information by default (though some docker images such as the official MariaDB image take care of this for you) which will cause unexpected behavior with date-based queries.

> 

> To fix this, execute one of the following commands:

> 

> MySQL: mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -u root mysql -p

> 

> MariaDB: mariadb-tzinfo-to-sql /usr/share/zoneinfo | mariadb -u root mysql -p

> 

> Barcodes

> Paperless is able to utilize barcodes for automatically performing some tasks.

> 

> At this time, the library utilized for detection of barcodes supports the following types:

> 

> AN-13/UPC-A

> UPC-E

> EAN-8

> Code 128

> Code 93

> Code 39

> Codabar

> Interleaved 2 of 5

> QR Code

> SQ Code

> You may check for updates on the zbar library homepage. For usage in Paperless, the type of barcode does not matter, only the contents of it.

> 

> For how to enable barcode usage, see the configuration. The two settings may be enabled independently, but do have interactions as explained below.

> 

> Document Splitting

> When enabled, Paperless will look for a barcode with the configured value and create a new document starting from the next page. The page with the barcode on it will not be retained. It is expected to be a page existing only for triggering the split.

> 

> Archive Serial Number Assignment

> When enabled, the value of the barcode (as an integer) will be used to set the document's archive serial number, allowing quick reference back to the original, paper document.

> 

> If document splitting via barcode is also enabled, documents will be split when an ASN barcode is located. However, differing from the splitting, the page with the barcode will be retained. This allows application of a barcode to any page, including one which holds data to keep in the document.

> 

> Tag Assignment

> When enabled, Paperless will parse barcodes and attempt to interpret and assign tags.

> 

> See the relevant settings PAPERLESS_CONSUMER_ENABLE_TAG_BARCODE and PAPERLESS_CONSUMER_TAG_BARCODE_MAPPING for more information.

> 

> Automatic collation of double-sided documents

> Note

> 

> If your scanner supports double-sided scanning natively, you do not need this feature.

> 

> This feature is turned off by default, see configuration on how to turn it on.

> 

> Summary

> If you have a scanner with an automatic document feeder (ADF) that only scans a single side, this feature makes scanning double-sided documents much more convenient by automatically collating two separate scans into one document, reordering the pages as necessary.

> 

> Usage example

> Suppose you have a double-sided document with 6 pages (3 sheets of paper). First, put the stack into your ADF as normal, ensuring that page 1 is scanned first. Your ADF will now scan pages 1, 3, and 5. Then you (or your scanner, if it supports it) upload the scan into the correct sub-directory of the consume folder (double-sided by default; keep in mind that Paperless will not automatically create the directory for you.) Paperless will then process the scan and move it into an internal staging area.

> 

> The next step is to turn your stack upside down (without reordering the sheets of paper), and scan it once again, your ADF will now scan pages 6, 4, and 2, in that order. Once this scan is copied into the sub-directory, Paperless will collate the previous scan with the new one, reversing the order of the pages on the second, "even numbered" scan. The resulting document will have the pages 1-6 in the correct order, and this new file will then be processed as normal.

> 

> Tip

> 

> When scanning the even numbered pages, you can omit the last empty pages, if there are any. For example, if page 6 is empty, you only need to scan pages 2 and 4. Do not omit empty pages in the middle of the document.

> 

> Things that could go wrong

> Paperless will notice when the first, "odd numbered" scan has less pages than the second scan (this can happen when e.g. the ADF skipped a few pages in the first pass). In that case, Paperless will remove the staging copy as well as the scan, and give you an error message asking you to restart the process from scratch, by scanning the odd pages again, followed by the even pages.

> 

> It's important that the scan files get consumed in the correct order, and one at a time. You therefore need to make sure that Paperless is running while you upload the files into the directory; and if you're using polling, make sure that CONSUMER_POLLING is set to a value lower than it takes for the second scan to appear, like 5-10 or even lower.

> 

> Another thing that might happen is that you start a double sided scan, but then forget to upload the second file. To avoid collating the wrong documents if you then come back a day later to scan a new double-sided document, Paperless will only keep an "odd numbered pages" file for up to 30 minutes. If more time passes, it will consider the next incoming scan a completely new "odd numbered pages" one. The old staging file will get discarded.

> 

> Interaction with "subdirs as tags"

> The collation feature can be used together with the subdirs as tags feature (but this is not a requirement). Just create a correctly named double-sided subdir in the hierarchy and upload your scans there. For example, both double-sided/foo/bar as well as foo/bar/double-sided will cause the collated document to be treated as if it were uploaded into foo/bar and receive both foo and bar tags, but not double-sided.

> 

> Interaction with document splitting

> You can use the document splitting feature, but if you use a normal single-sided split marker page, the split document(s) will have an empty page at the front (or whatever else was on the backside of the split marker page.) You can work around that by having a split marker page that has the split barcode on both sides. This way, the extra page will get automatically removed.

> 

> SSO and third party authentication with Paperless-ngx

> Paperless-ngx has a built-in authentication system from Django but you can easily integrate an external authentication solution using one of the following methods:

> 

> Remote User authentication

> This is a simple option that uses remote user authentication made available by certain SSO applications. See the relevant configuration options for more information: PAPERLESS_ENABLE_HTTP_REMOTE_USER, PAPERLESS_HTTP_REMOTE_USER_HEADER_NAME and PAPERLESS_LOGOUT_REDIRECT_URL

> 

> OpenID Connect and social authentication

> Version 2.5.0 of Paperless-ngx added support for integrating other authentication systems via the django-allauth package. Once set up, users can either log in or (optionally) sign up using any third party systems you integrate. See the relevant configuration settings and django-allauth docs for more information.

> 

> To associate an existing Paperless-ngx account with a social account, first login with your regular credentials and then choose "My Profile" from the user dropdown in the app and you will see options to connect social account(s). If enabled, signup options will be available on the login page.

> 

> As an example, to set up login via Github, the following environment variables would need to be set:

> 

> PAPERLESS_APPS="allauth.socialaccount.providers.github"

> PAPERLESS_SOCIALACCOUNT_PROVIDERS='{"github": {"APPS": [{"provider_id": "github","name": "Github","client_id": "<CLIENT_ID>","secret": "<CLIENT_SECRET>"}]}}'

> Or, to use OpenID Connect ("OIDC"), via Keycloak in this example:

> 

> PAPERLESS_APPS="allauth.socialaccount.providers.openid_connect"

> PAPERLESS_SOCIALACCOUNT_PROVIDERS='

> {"openid_connect": {"APPS": [{"provider_id": "keycloak","name": "Keycloak","client_id": "paperless","secret": "<CLIENT_SECRET>","settings": { "server_url": "https://<KEYCLOAK_SERVER>/realms/<REALM>/.well-known/openid-configuration"}}]}}'

> More details about configuration option for various providers can be found in the allauth documentation.

> 

> Disabling Regular Login

> Once external auth is set up, 'regular' login can be disabled with the PAPERLESS_DISABLE_REGULAR_LOGIN setting and / or users can be automatically redirected with the PAPERLESS_REDIRECT_LOGIN_TO_SSO setting.

> 

> Decryption of encrypted emails before consumption

> Paperless-ngx can be configured to decrypt gpg encrypted emails before consumption.

> 

> Requirements

> You need a recent version of gpg-agent >= 2.1.1 installed on your host. Your host needs to be setup for decrypting your emails via gpg-agent, see this tutorial for instance. Test your setup and make sure that you can encrypt and decrypt files using your key

> 

> gpg --encrypt --armor -r person@email.com name_of_file

> gpg --decrypt name_of_file.asc

> Setup

> First, enable the PAPERLESS_ENABLE_GPG_DECRYPTOR environment variable.

> 

> Then determine your local gpg-agent socket by invoking

> 

> gpgconf --list-dir agent-socket

> on your host. A possible output is ~/.gnupg/S.gpg-agent. Also find the location of your public keyring.

> 

> If using docker, you'll need to add the following volume mounts to your docker-compose.yml file:

> 

> webserver:

>     volumes:

>         - /home/user/.gnupg/pubring.gpg:/usr/src/paperless/.gnupg/pubring.gpg

>         - <path to gpg-agent socket>:/usr/src/paperless/.gnupg/S.gpg-agent

> For a 'bare-metal' installation no further configuration is necessary. If you want to use a separate GNUPG_HOME, you can do so by configuring the PAPERLESS_EMAIL_GNUPG_HOME environment variable.

> 

> Troubleshooting

> Make sure, that gpg-agent is running on your host machine

> Make sure, that encryption and decryption works from inside the container using the gpg commands from above.

> Check that all files in /usr/src/paperless/.gnupg have correct permissions

> paperless@9da1865df327:~/.gnupg$ ls -al

> drwx------ 1 paperless paperless   4096 Aug 18 17:52 .

> drwxr-xr-x 1 paperless paperless   4096 Aug 18 17:52 ..

> srw------- 1 paperless paperless      0 Aug 18 17:22 S.gpg-agent

> -rw------- 1 paperless paperless 147940 Jul 24 10:23 pubring.gpg

>  Back to top

> Copyright © 2016 - 2023 Daniel Quinn, Jonas Winkler, and the Paperless-ngx team

> Made with Material for MkDocs

### Assistant
> Yes — that doc excerpt is exactly why I was pushing “boring + stable.”
> 
> Here’s the key takeaway you’re missing:
> 
> ## You do **not** need Storage Paths at all (yet)
> Paperless has **two** ways to control where files land:
> 
> 1) **Global filename format** (`PAPERLESS_FILENAME_FORMAT`)  
> → applies to everything by default
> 
> 2) **Storage Paths** (UI objects)  
> → only needed when you want **exceptions** (special layouts) via matching rules
> 
> So if your goal is “one sane layout for everything,” the cleanest move is:
> 
> ### Set **PAPERLESS_FILENAME_FORMAT** and skip Storage Paths for now
> 
> ---
> 
> # What I recommend (the “default layout”)
> 
> In `docker-compose.env` (or wherever you set env vars):
> 
> ```env
> PAPERLESS_FILENAME_FORMAT={{ document_type }}/{{ created_year }}/{{ correspondent }}/{{ created }}__{{ title|slugify }}__p{{ doc_pk }}
> PAPERLESS_FILENAME_FORMAT_REMOVE_NONE=true
> ```
> 
> ### Why this is the best default
> - Organized by **Document Type / Year / Correspondent**
> - Filename includes **date + title + unique id** (`doc_pk`) so collisions are rare
> - `REMOVE_NONE=true` prevents ugly `none` folders when something is missing
> - Doesn’t depend on “Auto matching” training
> - Doesn’t depend on tags (avoids path-length and churn)
> 
> **Example output**
> ```
> Court Order/2026/Indiana Courts/2026-01-04__order_granting_motion__p1234.pdf
> Invoice/2025/AES Indiana/2025-12-18__final_bill__p998.pdf
> ```
> 
> This is exactly what you want for blob storage sanity.
> 
> ---
> 
> # When to use Storage Paths (later)
> Only create Storage Paths when you want *special cases*, like:
> 
> - `Evidence/` gets a different naming convention
> - `Insurances/` gets flat long filenames
> - A specific correspondent always files somewhere custom
> 
> But that’s Phase 2/3 — not now.
> 
> ---
> 
> # “But the UI lets me create Storage Paths… should I anyway?”
> If you really want one for UI visibility, fine — but it’s redundant if you set `PAPERLESS_FILENAME_FORMAT`.
> 
> If you do create one anyway, make it an “exception path,” not “the default.” Otherwise you’ll be tempted to start building matching logic too early.
> 
> ---
> 
> # Important warning (so you don’t break things)
> - Changing **Storage Paths** auto-moves files.
> - Changing **PAPERLESS_FILENAME_FORMAT** does **not** auto-move existing files.  
>   You must run the **document renamer** to migrate older documents.
> 
> So it’s best to set your filename format **before** you ingest a ton.
> 
> ---
> 
> # Where your QID fits
> You’re right that you ultimately want QID baked in. But right now:
> 
> - **ASN** is the field Paperless can populate from barcode as an integer
> - You *can* set barcode prefix to `QID` and store the number portion (Paperless strips prefix and uses numeric) — but filename formatting uses `{{ asn }}` and that value is just a number (or `none`).
> 
> So later, once ASN is reliably set, you can update the filename format to:
> 
> ```env
> PAPERLESS_FILENAME_FORMAT={{ document_type }}/{{ created_year }}/{{ correspondent }}/{{ created }}__{{ title|slugify }}__qid{{ asn }}
> PAPERLESS_FILENAME_FORMAT_REMOVE_NONE=true
> ```
> 
> For now, `doc_pk` is your safe unique key.
> 
> ---
> 
> # What to do right now (in order)
> 1) Set `PAPERLESS_FILENAME_FORMAT` + `REMOVE_NONE=true`
> 2) Restart the stack
> 3) Ingest 5–10 test docs
> 4) Confirm paths look right
> 5) Only then decide if you need any Storage Path exceptions
> 
> ---
> 
> If you tell me whether you already ingested documents yet (yes/no), I’ll tell you whether you should run the renamer now or ignore it until later.

### User
> ok, skippin gstorage paths, next item is custom fields

### Assistant
> Good. Custom fields are where we add **structured, machine-readable metadata** that tags alone can’t carry. The mistake people make is creating 40 fields. Don’t. We’re going to create a **small “spine” set** that supports:
> 
> - QiNote export (YAML front matter)
> - barcodes / QID later
> - court/evidence traceability
> - invoice/statement search
> - pipeline state + review discipline
> 
> ## Custom Field Rules
> 1. If a value is usually **one of a small set** → use **Select**  
> 2. If it’s a **reference identifier** you’ll search often → use **Text**  
> 3. If it’s a **date you care about** → use **Date**  
> 4. Don’t duplicate what Paperless already stores (title, created date, correspondent, doc type, tags).
> 
> ---
> 
> # Create These Custom Fields (Phase 1 “Spine”)
> 
> ### 1) `QID` (Text)
> - **Type:** Text
> - **Purpose:** your canonical Qi ID (later from barcode / qi-cli)
> - **Example:** `qid000123_0` (or `qid000123` if you drop suffix)
> - **Notes:** This will become the anchor for QiNote, court binder links, and export idempotency.
> 
> ### 2) `External Reference` (Text)
> - **Type:** Text
> - **Purpose:** any external ID you might need later  
>   (case #, invoice #, account #, tracking #, notice ID)
> - **Example:** `49D03-2501-MF-002559`, `INV-38492`, `ACCT-XXXX`
> 
> ### 3) `Matter / Case ID` (Select)
> - **Type:** Select
> - **Options:** start with the cases you actually have
>   - `FCFCU`
>   - `AES`
>   - `QiAlly_Internal`
>   - `Personal`
> - **Why:** tags handle `case/*`, but this gives you a **single “primary matter”** for exports and workflows.
> 
> ### 4) `Document Role` (Select)
> - **Type:** Select
> - **Options:**
>   - `Evidence`
>   - `Filing`
>   - `Order`
>   - `Notice`
>   - `Correspondence`
>   - `Invoice`
>   - `Statement`
>   - `Receipt`
>   - `Contract`
>   - `Policy`
> - **Why:** This is the structured equivalent of `doc/*`.  
>   You can map between them later, but this helps vectorization + YAML consistency.
> 
> ### 5) `Action Required` (Select)
> - **Type:** Select
> - **Options:**
>   - `None`
>   - `Review`
>   - `Respond`
>   - `Pay`
>   - `File`
>   - `Follow-up`
> - **Why:** better than “TODO tags” because it’s queryable and exportable.
> 
> ### 6) `Due Date` (Date)
> - **Type:** Date
> - **Purpose:** deadlines (court dates, payment due, response deadlines)
> 
> ### 7) `Source Channel` (Select)
> - **Type:** Select
> - **Options:**
>   - `Email`
>   - `Scan`
>   - `Upload`
>   - `Import`
>   - `Mail`
> - **Why:** complements `intake/*`, but is structured for YAML and analytics.
> 
> ---
> 
> # Optional “Phase 2” Fields (only if you need them)
> Do **not** create these until you feel the pain:
> 
> - `Invoice Number` (Text)
> - `Account Number Last4` (Text)
> - `Hearing Date` (Date)
> - `Service Date` (Date)
> - `Exhibit ID` (Text) (e.g., `Exhibit A-12`)
> 
> ---
> 
> # How this ties to your barcode/QID plan
> Later, you’ll use barcode scanning to populate **ASN** (Paperless archive serial number). Paperless’s ASN is numeric, but you can treat it as the **numeric core** of your QID.
> 
> **Future mapping:**
> - Barcode value: `QID000123`
> - Paperless ASN becomes: `123`
> - Your `QID` custom field becomes: `qid000123_0` (bridge script writes it)
> 
> This keeps Paperless happy (integer ASN) and keeps you happy (QID string).
> 
> ---
> 
> # What to do next (concrete)
> 1) Create the 7 “Spine” fields above
> 2) After creating them, tell me:
>    - Are custom fields available **per document** on your UI already?
>    - Do you want the bridge script to export these into the QiNote `.md` YAML front matter? (I recommend yes.)
> 
> If you answer “yes,” I’ll give you the exact YAML schema and a deterministic mapping so Gina/QiNote always get consistent metadata.

### User
> Yes, they are there now.

### Assistant
> Good. Next we make those fields actually *do work* by locking a consistent YAML schema for QiNote and wiring the Paperless → QiNote bridge to export it deterministically.
> 
> ## QiNote YAML front matter schema (lock this in)
> 
> Use this exact schema in every exported `.md` sidecar:
> 
> ```yaml
> ---
> qid: ""                 # custom field QID (preferred) else derived
> paperless_id: 0         # doc_pk
> title: ""
> created: "YYYY-MM-DD"   # Paperless created date (date only)
> added: "YYYY-MM-DD"     # Paperless added date (date only)
> correspondent: ""
> document_type: ""
> document_role: ""       # custom field Document Role
> matter: ""              # custom field Matter / Case ID
> action_required: ""     # custom field Action Required
> due_date: ""            # custom field Due Date (or empty)
> source_channel: ""      # custom field Source Channel
> external_reference: ""  # custom field External Reference
> tags: []                # list of tag names
> storage_relpath: ""     # relative path inside vault
> source_url: ""          # Paperless UI URL (optional)
> sha256: ""              # optional if you compute it
> keywords: []            # optional: extracted keywords later
> ---
> ```
> 
> ### Why this schema works
> - It’s stable, searchable, and doesn’t depend on “pretty titles.”
> - It supports court binder referencing (`qid`, `external_reference`, `matter`).
> - It supports automation (`action_required`, `due_date`).
> - It’s vector-friendly because the metadata is clean and consistent.
> 
> ---
> 
> ## Deterministic QID logic (no ambiguity)
> 
> Priority order to set `qid`:
> 
> 1) If custom field `QID` is filled → use it
> 2) Else if Paperless ASN exists → `qid{asn:06d}_0`
> 3) Else fallback → `qid{paperless_id:06d}_0`
> 
> That guarantees every exported document has a QID even before barcodes are perfect.
> 
> ---
> 
> ## Vault path convention (QiNote side)
> 
> Keep it predictable:
> 
> ```
> qinote_vault/
>   documents/
>     {matter}/
>       {YYYY}/
>         {YYYY-MM-DD}__{title_slug}__qid{QID}.pdf
>         {YYYY-MM-DD}__{title_slug}__qid{QID}.md
> ```
> 
> If `matter` is blank, use `_unassigned`.
> 
> This mirrors how you think (matter → year → doc) and makes later case packaging trivial.
> 
> ---
> 
> ## What to tell Gemini (exact instruction)
> 
> Paste this to Gemini:
> 
> **Gemini instruction**
> - Update `qinote-bridge/export_bridge.py` so the `.md` sidecar uses the YAML schema below (verbatim keys), exporting Paperless custom fields: `QID`, `External Reference`, `Matter / Case ID`, `Document Role`, `Action Required`, `Due Date`, `Source Channel`.  
> - Implement deterministic QID selection: prefer custom field `QID`, else derive from ASN as `qid{asn:06d}_0`, else from `doc_pk` as `qid{doc_pk:06d}_0`.  
> - Change export path to `qinote_vault/documents/{matter_or__unassigned}/{created_year}/{created_date}__{slug_title}__{qid}` for both PDF and MD.  
> - Include `tags` as a YAML list, and include `paperless_id`, `created`, `added`, `correspondent`, `document_type`, and `external_reference`.  
> - Ensure idempotency uses `qid` (not title) so renames don’t duplicate exports.
> 
> And give it the schema:
> 
> ```yaml
> ---
> qid: ""
> paperless_id: 0
> title: ""
> created: "YYYY-MM-DD"
> added: "YYYY-MM-DD"
> correspondent: ""
> document_type: ""
> document_role: ""
> matter: ""
> action_required: ""
> due_date: ""
> source_channel: ""
> external_reference: ""
> tags: []
> storage_relpath: ""
> source_url: ""
> sha256: ""
> keywords: []
> ---
> ```
> 
> ---
> 
> ## What we do on our end right now (while Gemini codes)
> 
> ### 1) Create a minimum “workflow state” using tags (Paperless-native)
> Because “Auto matching” ignores inbox-tagged docs, we need a clean lifecycle:
> 
> Create these tags (nested is fine):
> - `status/inbox`
> - `status/reviewed`
> - `status/ready_for_qinote`
> - `status/exported`
> 
> Bridge should export only when `status/ready_for_qinote` exists.
> 
> ### 2) Decide your “Matter” options (keep it short)
> Start with:
> - `FCFCU`
> - `AES`
> - `QiAlly`
> - `Personal`
> 
> You can add later, but don’t start with 40.
> 
> ### 3) Barcodes (next step after bridge)
> Once this is stable, we turn on:
> - ASN assignment with prefix `QID`
> - Tag barcode detection to auto-apply `status/ready_for_qinote` or `matter/*` (optional)
> 
> ---
> 
> If you tell me your current top 3 “matters” you expect to ingest this week, I’ll give you a clean tag+doc-type+mail-rule mapping so Paperless starts filing correctly from day one.

### User
> FCFCU, AES, JOEL, ZJK

### Assistant
> Good list. Keep it exactly that for now.
> 
> ## 1) Matter / Case ID (Select) — set these options
> - `FCFCU`
> - `AES`
> - `JOEL`
> - `ZJK`
> 
> Use **these exact values** so your vault paths stay consistent.
> 
> ---
> 
> ## 2) Minimum tag taxonomy (nested) to support intake + lifecycle
> 
> Create these tags (exact strings):
> 
> ### Status lifecycle
> - `status/inbox`
> - `status/reviewed`
> - `status/action_required`
> - `status/ready_for_qinote`
> - `status/exported`
> 
> ### Intake channel
> - `intake/email`
> - `intake/scan`
> - `intake/upload`
> - `intake/import`
> 
> ### Matter mirror tags (optional but useful for quick filtering)
> - `matter/FCFCU`
> - `matter/AES`
> - `matter/JOEL`
> - `matter/ZJK`
> 
> Why both Matter field and tags?  
> - **Matter field** = single source of truth for export path  
> - **matter/* tags** = quick UI filtering + batch edits + rule actions
> 
> ---
> 
> ## 3) Document Types (keep it lean, court-friendly)
> 
> Create these Document Types:
> 
> - `Court Filing`
> - `Court Order`
> - `Legal Correspondence`
> - `Notice`
> - `Evidence`
> - `Invoice`
> - `Statement`
> - `Receipt`
> - `Identity`
> - `Immigration`
> 
> That set covers 95% of what you’re doing without turning into a taxonomy project.
> 
> ---
> 
> ## 4) Default workflow (how documents move)
> 
> This is the flow you should enforce:
> 
> 1. **Arrives** → tagged `status/inbox` + `intake/*`  
> 2. You review and set:
>    - Matter / Case ID
>    - Document Type
>    - (Optional) Document Role, Action Required, Due Date, External Reference
> 3. When it’s “clean enough” → add `status/ready_for_qinote`
> 4. Bridge exports → bridge adds `status/exported` (or you do this via workflow action)
> 
> Key constraint from the docs: **Auto matching learns only from documents NOT in inbox.**  
> So once reviewed, remove `status/inbox` and add `status/reviewed`.
> 
> ---
> 
> ## 5) Mail rules inside Paperless (not Gmail) — your mapping
> 
> ### Mail rule: “Intake” (what you already have)
> Set these actions:
> 
> - Add tag: `status/inbox`
> - Add tag: `intake/email`
> - (Optional) Add tag: `matter/FCFCU` etc **only if** you create separate inboxes/aliases per matter
> 
> Do **not** try to set document type automatically until you have enough examples.
> 
> ### Better: use aliases in Google Workspace (clean routing)
> Create these aliases (or groups that forward):
> - `intake@qially.com` (general)
> - `fcu@qially.com` → forwards to intake mailbox
> - `aes@qially.com`
> - `joel@qially.com`
> - `zjk@qially.com`
> 
> Then make **4 mail rules** in Paperless filtering “to” address and auto-assign `Matter / Case ID` + `matter/*` tag.
> 
> ---
> 
> ## 6) What to tell Gemini now (based on your matters)
> 
> Paste this to Gemini:
> 
> **Gemini**
> - Update the bridge so exported vault path uses `Matter / Case ID` values exactly: `FCFCU`, `AES`, `JOEL`, `ZJK`, else `_unassigned`.
> - Export tags and custom fields into YAML exactly as specified earlier.
> - Export only documents tagged `status/ready_for_qinote` and, after successful export, add tag `status/exported` (via API) and remove `status/ready_for_qinote` to prevent re-export loops.
> 
> That last part is important: it turns your tag into a queue.
> 
> ---
> 
> ## Next move (you can do immediately)
> Go create:
> 1) Matter select options (done)
> 2) Tags (status + intake + matter)
> 3) Document types (list above)
> 
> Then tell me **which email address you’re connecting in Paperless** (one mailbox vs multiple), and I’ll give you the exact Paperless mail rules (filters + actions) for FCFCU/AES/JOEL/ZJK so it routes cleanly on day one.

### User
> here are the workflow options, lets set the default flow. Trigger Workflow On:

> 

> 1. Document Added

> Trigger type

> Document Added

> Trigger for documents that match all filters specified below.

> 

> Filter filename

> Apply to documents that match this filename. Wildcards such as *.pdf or *invoice* are allowed. Case insensitive.

> Content matching algorithm

> None: Disable matching

> Advanced Filters

> Has all of these tags

> Actions

> Apply Actions:

> 

> 

> 1. Assignment

> Action type

> Assignment

> Assign title

> Can include some placeholders, see documentation.

> Assign tags

> Assign document type

> Assign correspondent

> Assign storage path

> Assign custom fields

> Assign owner

> Assign view permissions

> Users:

> Groups:

> Assign edit permissions

> Users:

> Groups:

> Edit permissions also grant viewing permissions

### Assistant
> Perfect. We’re going to set up a **single, clean DEFAULT workflow** that establishes state without over-automating. This is your “guard rails” workflow. Everything else builds on top of it later.
> 
> I’ll give you **exact settings**, field by field, using what’s on your screen.
> 
> ---
> 
> # DEFAULT WORKFLOW — “Initial Intake”
> 
> ## Purpose (lock this mentally)
> - Every new document gets a **known starting state**
> - Nothing “smart” happens yet
> - No guessing document type, case, or meaning
> - Enables Auto-matching training later
> - Prevents documents from floating untracked
> 
> ---
> 
> ## Trigger Workflow On
> 
> ### Trigger type
> **Document Added** ✅
> 
> ### Filter filename
> **Leave blank**
> 
> Reason: this is a global default. No file-type bias.
> 
> ---
> 
> ### Content matching algorithm
> **None** ✅
> 
> Reason:  
> You are **not** using text-based matching at this stage. That comes later for *specific* workflows.
> 
> ---
> 
> ### Advanced Filters → Has all of these tags
> **Leave empty**
> 
> Reason:  
> This is the *first* workflow. It must run on everything.
> 
> ---
> 
> # Actions → Apply Actions
> 
> You will add **ONE action only**.
> 
> ---
> 
> ## Action 1: Assignment
> 
> ### Action type
> **Assignment** ✅
> 
> Now set the following **exactly**:
> 
> ---
> 
> ### Assign title
> **Leave blank**
> 
> Reason:  
> Title already comes from:
> - mail rule (subject), or
> - original filename
> 
> We don’t overwrite that here.
> 
> ---
> 
> ### Assign tags
> Add these tags:
> 
> - `status/inbox`
> - `intake/import` *(or leave this off if mail rules already add intake/email)*
> 
> **Important rule:**  
> Only one workflow assigns `status/inbox`. This is it.
> 
> ---
> 
> ### Assign document type
> **Leave blank**
> 
> Do NOT guess document type automatically.  
> Bad guesses pollute Auto-matching training.
> 
> ---
> 
> ### Assign correspondent
> **Leave blank**
> 
> Mail rules already handle this.  
> Scans/uploads will be set manually during review.
> 
> ---
> 
> ### Assign storage path
> **Leave blank**
> 
> You explicitly chose:
> - global filename format
> - no storage paths yet
> 
> Correct.
> 
> ---
> 
> ### Assign custom fields
> Set **only one** custom field:
> 
> - **Source Channel** → `Import`
> 
> Why:
> - This workflow fires for *all* ingestion methods
> - Mail rules will override this later with `Email`
> - Scan workflows can override with `Scan`
> 
> This gives you a safe default.
> 
> Do **not** set:
> - Matter
> - Document Role
> - Action Required
> - Due Date
> - QID
> 
> Those are human review decisions.
> 
> ---
> 
> ### Assign owner
> Leave blank unless you have multiple users already.  
> (Skip for now.)
> 
> ---
> 
> ### View permissions / Edit permissions
> Leave blank.  
> Don’t lock yourself out during setup.
> 
> ---
> 
> # Final Result: What this workflow guarantees
> 
> Every document, no matter how it enters Paperless, will have:
> 
> - A known lifecycle state: `status/inbox`
> - A known source channel
> - No premature classification
> - Eligibility for Auto-matching **after review**
> - Clean handoff to QiNote once reviewed
> 
> This is exactly what you want.
> 
> ---
> 
> # NEXT workflow (do NOT configure yet, but understand it)
> 
> Once this is saved, the *next* workflow we’ll add later is:
> 
> **“Ready for QiNote Export”**
> - Trigger: Tag added `status/ready_for_qinote`
> - Action: (none inside Paperless)  
>   → Bridge script handles export and tag transition
> 
> Keeping export logic **outside** Paperless is the right call.
> 
> ---
> 
> # Sanity check (answer yes/no)
> Before we move on, confirm:
> 
> 1. Default workflow saved with **only** the actions above  
> 2. No document type / case auto-assignment yet  
> 3. `status/inbox` exists and is visible on new docs  
> 
> Once confirmed, the next step is either:
> - defining **mail-specific workflows** (FCFCU / AES routing), or
> - finalizing **barcode → QID → tag automation**
> 
> Say which one you want next.

### User
> ok i moved an email with an attachment ot the intake folder but it never arrived

### Assistant
> Good catch. This is a **classic Paperless + Gmail IMAP gotcha**, not a logic error. Let’s debug it methodically and fast.
> 
> I’m going to give you **a decision tree**. Do these in order and don’t skip steps.
> 
> ---
> 
> ## First: what *should* have happened
> When you moved the email into the `intake` folder/label, Paperless should have:
> 
> 1. Seen the message via IMAP
> 2. Applied the mail rule
> 3. Created a document from the attachment
> 4. Tagged it `status/inbox`, `intake/email`
> 
> Since **nothing arrived**, one of four things is wrong.
> 
> ---
> 
> ## Step 1 — Confirm Paperless is actually checking mail (most common miss)
> 
> ### Go to:
> **Settings → Mail → Mail accounts → Intake Gmail**
> 
> Check **all** of the following:
> 
> - ✅ **Enabled** = ON  
> - ✅ **Server** = `imap.gmail.com`  
> - ✅ **Port** = `993`  
> - ✅ **Encryption** = SSL/TLS  
> - ✅ **Username** = full email (`intake@qially.com`)  
> - ✅ **Password** = **App Password**, not your normal Gmail password  
> 
> If **any** of these are wrong, nothing will arrive.
> 
> ### Then click:
> **Test connection**
> 
> - ❌ If test fails → stop here, fix auth
> - ✅ If test succeeds → continue
> 
> Tell me immediately if the test fails and what the error says.
> 
> ---
> 
> ## Step 2 — IMAP labels vs folders (this is likely the issue)
> 
> Gmail does **not** behave like normal IMAP folders.
> 
> ### Critical rule
> Paperless can only see **labels that are enabled for IMAP**.
> 
> #### In Gmail:
> 1. Go to **Settings → Labels**
> 2. Find `intake`
> 3. Make sure:
>    - ✅ “Show in IMAP” = ON
> 
> If this is OFF, Paperless will **never** see that folder.
> 
> ### If you are unsure:
> **Temporarily remove the Folder field** from the Paperless mail rule.
> 
> - Folder = *(blank)*
> 
> This forces Paperless to scan INBOX.
> 
> > ⚠️ This is the #1 reason “I moved it but nothing happened”.
> 
> ---
> 
> ## Step 3 — Check Paperless mail rule logic (quick sanity)
> 
> Open your **Intake** mail rule and verify:
> 
> - **Order** = `100` (low priority)
> - **Enabled** = ON
> - **Folder** = empty (for now)
> - **Attachment type** = Only process attachments
> - **No “don’t process tagged mails” action**
> - **Tags assigned** = `status/inbox`, `intake/email`
> 
> If Folder is set and you haven’t confirmed IMAP visibility → clear it.
> 
> ---
> 
> ## Step 4 — Look at the logs (this tells us instantly)
> 
> In your terminal:
> 
> ```bash
> docker compose logs -f webserver
> ```
> 
> Then:
> - Move a **new email** with an attachment into INBOX (not intake)
> - Watch the logs for lines mentioning:
>   - `mail`
>   - `imap`
>   - `consume`
> 
> ### What we’re looking for
> - If you see **no mail-related log entries at all** → Paperless isn’t polling
> - If you see authentication errors → app password issue
> - If you see “skipping message” → rule/filter issue
> 
> Paste **only the relevant log lines** here if you see errors.
> 
> ---
> 
> ## Step 5 — One controlled test (do this exactly)
> 
> To eliminate variables:
> 
> 1. Send a **new email** to `intake@qially.com`
> 2. Attach a simple PDF
> 3. Do **not** move it
> 4. Leave it in INBOX
> 5. Wait ~60 seconds
> 
> If it appears:
> - The system works
> - Your issue is **label/folder handling**
> 
> If it does not:
> - It’s auth or polling
> 
> ---
> 
> ## Fast diagnosis summary (likely causes ranked)
> 
> 1. 🔥 Gmail label `intake` not IMAP-enabled  
> 2. 🔥 Folder name mismatch (`intake` vs `INBOX/intake`)  
> 3. 🔥 App password missing or wrong  
> 4. 🔥 Mail rule action blocking processing  
> 
> ---
> 
> ## Tell me **one thing** to continue
> Reply with **one of these** (don’t explain yet):
> 
> - `Test connection failed`
> - `Test connection passed`
> - `It worked when left in INBOX`
> - `Still nothing + logs show errors`
> 
> Once I know which branch we’re on, I’ll give you the exact fix in one step.

### User
> QiPaperless-ngx

> by Paperless-ngx

> Search

> 1

>  Dashboard

>  Documents

> Manage

>  Correspondents

>  Tags

>  Document Types

>  Storage Paths

>  Custom Fields

>  Saved Views

>  Workflows

>  Mail

>  Trash

> Administration

>  Settings

>  Configuration

>  Users & Groups

>  File Tasks

>  Logs

>  Documentation

> QiPaperless-ngx v2.20.3

> Logs 

> Show

> 5000

> lines

> Auto refresh

> paperless.log

> mail.log

> celery.log

> [2026-01-04 08:21:45,409] [INFO] [paperless.management.consumer] Using inotify to watch directory for changes: /usr/src/paperless/consume

> 

> [2026-01-04 08:21:45,761] [INFO] [paperless.asgi] [init] Paperless-ngx version: v2.20.3

> 

> [2026-01-04 08:21:45,762] [INFO] [_granian.workers] Started worker-1

> 

> [2026-01-04 08:21:45,762] [INFO] [_granian.workers] Started worker-1 runtime-1

> 

> [2026-01-04 08:36:27,918] [INFO] [_granian.workers] Stopping worker-1

> 

> [2026-01-04 08:36:27,918] [INFO] [_granian.workers] Stopping worker-1 runtime-1

> 

> [2026-01-04 14:36:55,372] [INFO] [paperless.management.consumer] Using inotify to watch directory for changes: /usr/src/paperless/consume

> 

> [2026-01-04 14:36:55,670] [INFO] [paperless.asgi] [init] Paperless-ngx version: v2.20.3

> 

> [2026-01-04 14:36:55,686] [INFO] [_granian.workers] Started worker-1

> 

> [2026-01-04 14:36:55,686] [INFO] [_granian.workers] Started worker-1 runtime-1

> 

> [2026-01-04 14:37:43,491] [DEBUG] [paperless.auth] Creating initial superuser ``

> 

> [2026-01-04 14:39:27,474] [INFO] [paperless.auth] Login failed for user `crice4485@gmail.com` from private IP `172.18.0.1`.

> 

> [2026-01-04 14:39:35,381] [INFO] [paperless.auth] Login failed for user `crice4485` from private IP `172.18.0.1`.

> 

> [2026-01-04 14:39:50,399] [INFO] [paperless.auth] Login failed for user `cody` from private IP `172.18.0.1`.

> 

> [2026-01-04 14:40:14,992] [DEBUG] [paperless.tasks] Executing plugin ConsumerPreflightPlugin

> 

> [2026-01-04 14:40:15,011] [INFO] [paperless.tasks] ConsumerPreflightPlugin completed with no message

> 

> [2026-01-04 14:40:15,012] [DEBUG] [paperless.tasks] Skipping plugin CollatePlugin

> 

> [2026-01-04 14:40:15,016] [DEBUG] [paperless.tasks] Skipping plugin BarcodePlugin

> 

> [2026-01-04 14:40:15,016] [DEBUG] [paperless.tasks] Executing plugin WorkflowTriggerPlugin

> 

> [2026-01-04 14:40:15,026] [INFO] [paperless.tasks] WorkflowTriggerPlugin completed with:

> 

> [2026-01-04 14:40:15,027] [DEBUG] [paperless.tasks] Executing plugin ConsumeTaskPlugin

> 

> [2026-01-04 14:40:15,027] [INFO] [paperless.consumer] Consuming www.expedia.com-egti-RAB-QMV-UIX4.pdf

> 

> [2026-01-04 14:40:15,032] [DEBUG] [paperless.consumer] Detected mime type: application/pdf

> 

> [2026-01-04 14:40:15,040] [DEBUG] [paperless.consumer] Parser: RasterisedDocumentParser

> 

> [2026-01-04 14:40:15,046] [DEBUG] [paperless.consumer] Parsing www.expedia.com-egti-RAB-QMV-UIX4.pdf...

> 

> [2026-01-04 14:40:15,077] [INFO] [paperless.parsing.tesseract] pdftotext exited 0

> 

> [2026-01-04 14:40:15,460] [DEBUG] [paperless.parsing.tesseract] Calling OCRmyPDF with args: {'input_file': PosixPath('/tmp/paperless/paperless-ngxzcqf75jg/www.expedia.com-egti-RAB-QMV-UIX4.pdf'), 'output_file': PosixPath('/tmp/paperless/paperless-ko4zho3e/archive.pdf'), 'use_threads': True, 'jobs': 4, 'language': 'eng', 'output_type': 'pdfa', 'progress_bar': False, 'color_conversion_strategy': 'RGB', 'skip_text': True, 'clean': True, 'deskew': True, 'rotate_pages': True, 'rotate_pages_threshold': 12.0, 'sidecar': PosixPath('/tmp/paperless/paperless-ko4zho3e/sidecar.txt')}

> 

> [2026-01-04 14:40:15,732] [WARNING] [ocrmypdf._pipeline] This PDF is marked as a Tagged PDF. This often indicates that the PDF was generated from an office document and does not need OCR. PDF pages processed by OCRmyPDF may not be tagged correctly.

> 

> [2026-01-04 14:40:15,732] [INFO] [ocrmypdf._pipelines.ocr] Start processing 2 pages concurrently

> 

> [2026-01-04 14:40:15,734] [INFO] [ocrmypdf._pipeline] skipping all processing on this page

> 

> [2026-01-04 14:40:15,734] [INFO] [ocrmypdf._pipeline] skipping all processing on this page

> 

> [2026-01-04 14:40:15,743] [INFO] [ocrmypdf._pipelines.ocr] Postprocessing...

> 

> [2026-01-04 14:40:16,015] [INFO] [ocrmypdf._pipeline] Image optimization ratio: 1.30 savings: 23.2%

> 

> [2026-01-04 14:40:16,015] [INFO] [ocrmypdf._pipeline] Total file size ratio: 2.02 savings: 50.5%

> 

> [2026-01-04 14:40:16,018] [INFO] [ocrmypdf._pipelines._common] Output file is a PDF/A-2b (as expected)

> 

> [2026-01-04 14:40:16,029] [DEBUG] [paperless.parsing.tesseract] Incomplete sidecar file: discarding.

> 

> [2026-01-04 14:40:16,089] [INFO] [paperless.parsing.tesseract] pdftotext exited 0

> 

> [2026-01-04 14:40:16,090] [DEBUG] [paperless.consumer] Generating thumbnail for www.expedia.com-egti-RAB-QMV-UIX4.pdf...

> 

> [2026-01-04 14:40:16,096] [DEBUG] [paperless.parsing] Execute: convert -density 300 -scale 500x5000> -alpha remove -strip -auto-orient -define pdf:use-cropbox=true /tmp/paperless/paperless-ko4zho3e/archive.pdf[0] /tmp/paperless/paperless-ko4zho3e/convert.webp

> 

> [2026-01-04 14:40:17,854] [INFO] [paperless.parsing] convert exited 0

> 

> [2026-01-04 14:40:17,938] [DEBUG] [paperless.classifier] Document classification model does not exist (yet), not performing automatic matching.

> 

> [2026-01-04 14:40:17,944] [DEBUG] [paperless.consumer] Saving record to database

> 

> [2026-01-04 14:40:17,944] [DEBUG] [paperless.consumer] Creation date from st_mtime: 2026-01-04 14:40:14+00:00

> 

> [2026-01-04 14:40:18,072] [DEBUG] [paperless.index] Index updated for document 1.

> 

> [2026-01-04 14:40:18,110] [DEBUG] [paperless.consumer] Deleting original file /tmp/paperless/tmpyyka_9vt/www.expedia.com-egti-RAB-QMV-UIX4.pdf

> 

> [2026-01-04 14:40:18,111] [DEBUG] [paperless.consumer] Deleting working copy /tmp/paperless/paperless-ngxzcqf75jg/www.expedia.com-egti-RAB-QMV-UIX4.pdf

> 

> [2026-01-04 14:40:18,120] [DEBUG] [paperless.parsing.tesseract] Deleting directory /tmp/paperless/paperless-ko4zho3e

> 

> [2026-01-04 14:40:18,120] [INFO] [paperless.consumer] Document 2026-01-04 www.expedia.com-egti-RAB-QMV-UIX4 consumption finished

> 

> [2026-01-04 14:40:18,128] [INFO] [paperless.tasks] ConsumeTaskPlugin completed with: Success. New document id 1 created

> 

> [2026-01-04 15:05:00,074] [INFO] [paperless.tasks] No automatic matching items, not training

> 

> [2026-01-04 15:51:19,004] [INFO] [_granian.workers] Stopping worker-1 runtime-1

> 

> [2026-01-04 15:51:19,004] [INFO] [_granian.workers] Stopping worker-1

> 

> [2026-01-04 15:51:41,410] [INFO] [paperless.management.consumer] Using inotify to watch directory for changes: /usr/src/paperless/consume

> 

> [2026-01-04 15:51:42,126] [INFO] [paperless.asgi] [init] Paperless-ngx version: v2.20.3

> 

> [2026-01-04 15:51:42,128] [INFO] [_granian.workers] Started worker-1

> 

> [2026-01-04 15:51:42,128] [INFO] [_granian.workers] Started worker-1 runtime-1

> 

> [2026-01-04 16:05:00,098] [INFO] [paperless.tasks] No automatic matching items, not training

> 

> [2026-01-04 16:52:53,267] [INFO] [paperless.management.consumer] Using inotify to watch directory for changes: /usr/src/paperless/consume

> 

> [2026-01-04 16:52:55,682] [INFO] [paperless.asgi] [init] Paperless-ngx version: v2.20.3

> 

> [2026-01-04 16:52:55,718] [INFO] [_granian.workers] Started worker-1

> 

> [2026-01-04 16:52:55,718] [INFO] [_granian.workers] Started worker-1 runtime-1

> 

> [2026-01-04 17:05:00,098] [INFO] [paperless.tasks] No automatic matching items, not training

> 

> [2026-01-04 17:27:21,918] [DEBUG] [paperless.tasks] Executing plugin ConsumerPreflightPlugin

> 

> [2026-01-04 17:27:21,936] [INFO] [paperless.tasks] ConsumerPreflightPlugin completed with no message

> 

> [2026-01-04 17:27:21,936] [DEBUG] [paperless.tasks] Skipping plugin CollatePlugin

> 

> [2026-01-04 17:27:21,940] [DEBUG] [paperless.tasks] Skipping plugin BarcodePlugin

> 

> [2026-01-04 17:27:21,940] [DEBUG] [paperless.tasks] Executing plugin WorkflowTriggerPlugin

> 

> [2026-01-04 17:27:21,956] [INFO] [paperless.tasks] WorkflowTriggerPlugin completed with:

> 

> [2026-01-04 17:27:21,957] [DEBUG] [paperless.tasks] Executing plugin ConsumeTaskPlugin

> 

> [2026-01-04 17:27:21,957] [INFO] [paperless.consumer] Consuming Qially has granted you access to their Gmail account.eml

> 

> [2026-01-04 17:27:21,962] [DEBUG] [paperless.consumer] Detected mime type: message/rfc822

> 

> [2026-01-04 17:27:21,968] [ERROR] [paperless.consumer] Unsupported mime type message/rfc822

> 

> [2026-01-04 17:27:21,969] [ERROR] [paperless.tasks] ConsumeTaskPlugin failed: Qially has granted you access to their Gmail account.eml: Unsupported mime type message/rfc822

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/documents/tasks.py", line 183, in consume_file

> 

>     msg = plugin.run()

> 

>           ^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/documents/consumer.py", line 345, in run

> 

>     self._fail(

> 

>   File "/usr/src/paperless/src/documents/consumer.py", line 148, in _fail

> 

>     raise ConsumerError(f"{self.filename}: {log_message or message}") from exception

> 

> documents.consumer.ConsumerError: Qially has granted you access to their Gmail account.eml: Unsupported mime type message/rfc822

> 

> [2026-01-04 17:27:22,570] [DEBUG] [paperless.tasks] Executing plugin ConsumerPreflightPlugin

> 

> [2026-01-04 17:27:22,588] [INFO] [paperless.tasks] ConsumerPreflightPlugin completed with no message

> 

> [2026-01-04 17:27:22,589] [DEBUG] [paperless.tasks] Skipping plugin CollatePlugin

> 

> [2026-01-04 17:27:22,592] [DEBUG] [paperless.tasks] Skipping plugin BarcodePlugin

> 

> [2026-01-04 17:27:22,592] [DEBUG] [paperless.tasks] Executing plugin WorkflowTriggerPlugin

> 

> [2026-01-04 17:27:22,602] [INFO] [paperless.tasks] WorkflowTriggerPlugin completed with:

> 

> [2026-01-04 17:27:22,603] [DEBUG] [paperless.tasks] Executing plugin ConsumeTaskPlugin

> 

> [2026-01-04 17:27:22,604] [INFO] [paperless.consumer] Consuming Google Cloud Organization is now available for your domain.eml

> 

> [2026-01-04 17:27:22,608] [DEBUG] [paperless.consumer] Detected mime type: message/rfc822

> 

> [2026-01-04 17:27:22,615] [ERROR] [paperless.consumer] Unsupported mime type message/rfc822

> 

> [2026-01-04 17:27:22,615] [ERROR] [paperless.tasks] ConsumeTaskPlugin failed: Google Cloud Organization is now available for your domain.eml: Unsupported mime type message/rfc822

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/documents/tasks.py", line 183, in consume_file

> 

>     msg = plugin.run()

> 

>           ^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/documents/consumer.py", line 345, in run

> 

>     self._fail(

> 

>   File "/usr/src/paperless/src/documents/consumer.py", line 148, in _fail

> 

>     raise ConsumerError(f"{self.filename}: {log_message or message}") from exception

> 

> documents.consumer.ConsumerError: Google Cloud Organization is now available for your domain.eml: Unsupported mime type message/rfc822

> 

> [2026-01-04 17:27:23,204] [DEBUG] [paperless.tasks] Executing plugin ConsumerPreflightPlugin

> 

> [2026-01-04 17:27:23,224] [INFO] [paperless.tasks] ConsumerPreflightPlugin completed with no message

> 

> [2026-01-04 17:27:23,225] [DEBUG] [paperless.tasks] Skipping plugin CollatePlugin

> 

> [2026-01-04 17:27:23,228] [DEBUG] [paperless.tasks] Skipping plugin BarcodePlugin

> 

> [2026-01-04 17:27:23,228] [DEBUG] [paperless.tasks] Executing plugin WorkflowTriggerPlugin

> 

> [2026-01-04 17:27:23,239] [INFO] [paperless.tasks] WorkflowTriggerPlugin completed with:

> 

> [2026-01-04 17:27:23,239] [DEBUG] [paperless.tasks] Executing plugin ConsumeTaskPlugin

> 

> [2026-01-04 17:27:23,239] [INFO] [paperless.consumer] Consuming Security alert.eml

> 

> [2026-01-04 17:27:23,244] [DEBUG] [paperless.consumer] Detected mime type: message/rfc822

> 

> [2026-01-04 17:27:23,250] [ERROR] [paperless.consumer] Unsupported mime type message/rfc822

> 

> [2026-01-04 17:27:23,251] [ERROR] [paperless.tasks] ConsumeTaskPlugin failed: Security alert.eml: Unsupported mime type message/rfc822

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/documents/tasks.py", line 183, in consume_file

> 

>     msg = plugin.run()

> 

>           ^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/documents/consumer.py", line 345, in run

> 

>     self._fail(

> 

>   File "/usr/src/paperless/src/documents/consumer.py", line 148, in _fail

> 

>     raise ConsumerError(f"{self.filename}: {log_message or message}") from exception

> 

> documents.consumer.ConsumerError: Security alert.eml: Unsupported mime type message/rfc822

> 

> [2026-01-04 17:27:23,835] [DEBUG] [paperless.tasks] Executing plugin ConsumerPreflightPlugin

> 

> [2026-01-04 17:27:23,863] [INFO] [paperless.tasks] ConsumerPreflightPlugin completed with no message

> 

> [2026-01-04 17:27:23,863] [DEBUG] [paperless.tasks] Skipping plugin CollatePlugin

> 

> [2026-01-04 17:27:23,867] [DEBUG] [paperless.tasks] Skipping plugin BarcodePlugin

> 

> [2026-01-04 17:27:23,867] [DEBUG] [paperless.tasks] Executing plugin WorkflowTriggerPlugin

> 

> [2026-01-04 17:27:23,878] [INFO] [paperless.tasks] WorkflowTriggerPlugin completed with:

> 

> [2026-01-04 17:27:23,878] [DEBUG] [paperless.tasks] Executing plugin ConsumeTaskPlugin

> 

> [2026-01-04 17:27:23,878] [INFO] [paperless.consumer] Consuming Security alert.eml

> 

> [2026-01-04 17:27:23,890] [DEBUG] [paperless.consumer] Detected mime type: message/rfc822

> 

> [2026-01-04 17:27:23,896] [ERROR] [paperless.consumer] Unsupported mime type message/rfc822

> 

> [2026-01-04 17:27:23,897] [ERROR] [paperless.tasks] ConsumeTaskPlugin failed: Security alert.eml: Unsupported mime type message/rfc822

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/documents/tasks.py", line 183, in consume_file

> 

>     msg = plugin.run()

> 

>           ^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/documents/consumer.py", line 345, in run

> 

>     self._fail(

> 

>   File "/usr/src/paperless/src/documents/consumer.py", line 148, in _fail

> 

>     raise ConsumerError(f"{self.filename}: {log_message or message}") from exception

> 

> documents.consumer.ConsumerError: Security alert.eml: Unsupported mime type message/rfc822

> 

> [2026-01-04 17:27:24,496] [DEBUG] [paperless.tasks] Executing plugin ConsumerPreflightPlugin

> 

> [2026-01-04 17:27:24,518] [INFO] [paperless.tasks] ConsumerPreflightPlugin completed with no message

> 

> [2026-01-04 17:27:24,522] [DEBUG] [paperless.tasks] Skipping plugin CollatePlugin

> 

> [2026-01-04 17:27:24,529] [DEBUG] [paperless.tasks] Skipping plugin BarcodePlugin

> 

> [2026-01-04 17:27:24,530] [DEBUG] [paperless.tasks] Executing plugin WorkflowTriggerPlugin

> 

> [2026-01-04 17:27:24,546] [INFO] [paperless.tasks] WorkflowTriggerPlugin completed with:

> 

> [2026-01-04 17:27:24,546] [DEBUG] [paperless.tasks] Executing plugin ConsumeTaskPlugin

> 

> [2026-01-04 17:27:24,546] [INFO] [paperless.consumer] Consuming Security alert.eml

> 

> [2026-01-04 17:27:24,552] [DEBUG] [paperless.consumer] Detected mime type: message/rfc822

> 

> [2026-01-04 17:27:24,558] [ERROR] [paperless.consumer] Unsupported mime type message/rfc822

> 

> [2026-01-04 17:27:24,560] [ERROR] [paperless.tasks] ConsumeTaskPlugin failed: Security alert.eml: Unsupported mime type message/rfc822

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/documents/tasks.py", line 183, in consume_file

> 

>     msg = plugin.run()

> 

>           ^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/documents/consumer.py", line 345, in run

> 

>     self._fail(

> 

>   File "/usr/src/paperless/src/documents/consumer.py", line 148, in _fail

> 

>     raise ConsumerError(f"{self.filename}: {log_message or message}") from exception

> 

> documents.consumer.ConsumerError: Security alert.eml: Unsupported mime type message/rfc822

> 

> [2026-01-04 17:58:42,796] [DEBUG] [paperless.classifier] Document classification model does not exist (yet), not performing automatic matching.

> 

> [2026-01-04 18:00:07,275] [DEBUG] [paperless.classifier] Document classification model does not exist (yet), not performing automatic matching.

> 

> [2026-01-04 18:01:26,950] [DEBUG] [paperless.index] Index updated for document 1.

> 

> [2026-01-04 18:01:49,795] [DEBUG] [paperless.index] Index updated for document 1.

> 

> [2026-01-04 18:03:10,020] [DEBUG] [paperless.index] Index updated for document 1.

> 

> [2026-01-04 18:04:20,591] [DEBUG] [paperless.classifier] Document classification model does not exist (yet), not performing automatic matching.

> 

> [2026-01-04 18:05:00,065] [DEBUG] [paperless.classifier] Document classification model does not exist (yet), not performing automatic matching.

> 

> [2026-01-04 18:05:00,070] [DEBUG] [paperless.classifier] Gathering data from database...

> 

> [2026-01-04 18:05:00,091] [DEBUG] [paperless.classifier] 1 documents, 5 tag(s), 1 correspondent(s), 1 document type(s). 0 storage path(s)

> 

> [2026-01-04 18:05:03,743] [DEBUG] [paperless.classifier] Vectorizing data...

> 

> [2026-01-04 18:05:05,218] [DEBUG] [paperless.classifier] Training tags classifier...

> 

> [2026-01-04 18:05:05,241] [DEBUG] [paperless.classifier] Training correspondent classifier...

> 

> [2026-01-04 18:05:05,257] [DEBUG] [paperless.classifier] Training document type classifier...

> 

> [2026-01-04 18:05:05,282] [DEBUG] [paperless.classifier] There are no storage paths. Not training storage path classifier.

> 

> [2026-01-04 18:05:05,285] [INFO] [paperless.tasks] Saving updated classifier model to /usr/src/paperless/data/classification_model.pickle...

> 

> Drop files to begin upload_processed_files += self._handle_mail_rule(

> 

>                              ^^^^^^^^^^^^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 625, in _handle_mail_rule

> 

>     raise MailError(

> 

> paperless_mail.mail.MailError: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> [2026-01-04 17:36:36,848] [DEBUG] [paperless_mail] Skipping mail preprocessor MailMessageDecryptor

> 

> [2026-01-04 17:36:36,849] [DEBUG] [paperless_mail] Processing mail account Intake Gmail

> 

> [2026-01-04 17:36:37,153] [DEBUG] [paperless_mail] GMAIL Label Support: True

> 

> [2026-01-04 17:36:37,153] [DEBUG] [paperless_mail] AUTH=PLAIN Support: True

> 

> [2026-01-04 17:36:37,707] [DEBUG] [paperless_mail] Account Intake Gmail: Processing 1 rule(s)

> 

> [2026-01-04 17:36:37,711] [DEBUG] [paperless_mail] Rule Intake Gmail.Intake: Selecting folder intake

> 

> [2026-01-04 17:36:37,893] [ERROR] [paperless_mail] Unable to access folder intake, attempting folder listing

> 

> [2026-01-04 17:36:38,060] [INFO] [paperless_mail] Located folder: INBOX

> 

> [2026-01-04 17:36:38,060] [INFO] [paperless_mail] Located folder: Intake

> 

> [2026-01-04 17:36:38,060] [INFO] [paperless_mail] Located folder: [Gmail]

> 

> [2026-01-04 17:36:38,060] [INFO] [paperless_mail] Located folder: [Gmail]/All Mail

> 

> [2026-01-04 17:36:38,061] [INFO] [paperless_mail] Located folder: [Gmail]/Drafts

> 

> [2026-01-04 17:36:38,061] [INFO] [paperless_mail] Located folder: [Gmail]/Important

> 

> [2026-01-04 17:36:38,061] [INFO] [paperless_mail] Located folder: [Gmail]/Sent Mail

> 

> [2026-01-04 17:36:38,061] [INFO] [paperless_mail] Located folder: [Gmail]/Spam

> 

> [2026-01-04 17:36:38,061] [INFO] [paperless_mail] Located folder: [Gmail]/Starred

> 

> [2026-01-04 17:36:38,061] [INFO] [paperless_mail] Located folder: [Gmail]/Trash

> 

> [2026-01-04 17:36:38,062] [ERROR] [paperless_mail] Rule Intake Gmail.Intake: Error while processing rule: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 611, in _handle_mail_rule

> 

>     M.folder.set(folder)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/folder.py", line 43, in set

> 

>     check_command_status(result, MailboxFolderSelectError)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/utils.py", line 48, in check_command_status

> 

>     raise exception(command_result=command_result, expected=expected)

> 

> imap_tools.errors.MailboxFolderSelectError: Response status "OK" expected, but "NO" received. Data: [b'[NONEXISTENT] Unknown Mailbox: intake (now in authenticated state) (Failure)']

> 

> 

> The above exception was the direct cause of the following exception:

> 

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 573, in handle_mail_account

> 

>     total_processed_files += self._handle_mail_rule(

> 

>                              ^^^^^^^^^^^^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 625, in _handle_mail_rule

> 

>     raise MailError(

> 

> paperless_mail.mail.MailError: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> [2026-01-04 17:40:00,068] [DEBUG] [paperless_mail] Skipping mail preprocessor MailMessageDecryptor

> 

> [2026-01-04 17:40:00,069] [DEBUG] [paperless_mail] Processing mail account Intake Gmail

> 

> [2026-01-04 17:40:00,363] [DEBUG] [paperless_mail] GMAIL Label Support: True

> 

> [2026-01-04 17:40:00,363] [DEBUG] [paperless_mail] AUTH=PLAIN Support: True

> 

> [2026-01-04 17:40:01,377] [DEBUG] [paperless_mail] Account Intake Gmail: Processing 1 rule(s)

> 

> [2026-01-04 17:40:01,380] [DEBUG] [paperless_mail] Rule Intake Gmail.Intake: Selecting folder intake

> 

> [2026-01-04 17:40:01,615] [ERROR] [paperless_mail] Unable to access folder intake, attempting folder listing

> 

> [2026-01-04 17:40:01,848] [INFO] [paperless_mail] Located folder: INBOX

> 

> [2026-01-04 17:40:01,849] [INFO] [paperless_mail] Located folder: Intake

> 

> [2026-01-04 17:40:01,849] [INFO] [paperless_mail] Located folder: [Gmail]

> 

> [2026-01-04 17:40:01,849] [INFO] [paperless_mail] Located folder: [Gmail]/All Mail

> 

> [2026-01-04 17:40:01,849] [INFO] [paperless_mail] Located folder: [Gmail]/Drafts

> 

> [2026-01-04 17:40:01,849] [INFO] [paperless_mail] Located folder: [Gmail]/Important

> 

> [2026-01-04 17:40:01,849] [INFO] [paperless_mail] Located folder: [Gmail]/Sent Mail

> 

> [2026-01-04 17:40:01,850] [INFO] [paperless_mail] Located folder: [Gmail]/Spam

> 

> [2026-01-04 17:40:01,850] [INFO] [paperless_mail] Located folder: [Gmail]/Starred

> 

> [2026-01-04 17:40:01,850] [INFO] [paperless_mail] Located folder: [Gmail]/Trash

> 

> [2026-01-04 17:40:01,850] [ERROR] [paperless_mail] Rule Intake Gmail.Intake: Error while processing rule: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 611, in _handle_mail_rule

> 

>     M.folder.set(folder)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/folder.py", line 43, in set

> 

>     check_command_status(result, MailboxFolderSelectError)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/utils.py", line 48, in check_command_status

> 

>     raise exception(command_result=command_result, expected=expected)

> 

> imap_tools.errors.MailboxFolderSelectError: Response status "OK" expected, but "NO" received. Data: [b'[NONEXISTENT] Unknown Mailbox: intake (now in authenticated state) (Failure)']

> 

> 

> The above exception was the direct cause of the following exception:

> 

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 573, in handle_mail_account

> 

>     total_processed_files += self._handle_mail_rule(

> 

>                              ^^^^^^^^^^^^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 625, in _handle_mail_rule

> 

>     raise MailError(

> 

> paperless_mail.mail.MailError: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> [2026-01-04 17:50:00,074] [DEBUG] [paperless_mail] Skipping mail preprocessor MailMessageDecryptor

> 

> [2026-01-04 17:50:00,075] [DEBUG] [paperless_mail] Processing mail account Intake Gmail

> 

> [2026-01-04 17:50:00,376] [DEBUG] [paperless_mail] GMAIL Label Support: True

> 

> [2026-01-04 17:50:00,377] [DEBUG] [paperless_mail] AUTH=PLAIN Support: True

> 

> [2026-01-04 17:50:00,959] [DEBUG] [paperless_mail] Account Intake Gmail: Processing 1 rule(s)

> 

> [2026-01-04 17:50:00,962] [DEBUG] [paperless_mail] Rule Intake Gmail.Intake: Selecting folder intake

> 

> [2026-01-04 17:50:01,109] [ERROR] [paperless_mail] Unable to access folder intake, attempting folder listing

> 

> [2026-01-04 17:50:01,257] [INFO] [paperless_mail] Located folder: INBOX

> 

> [2026-01-04 17:50:01,258] [INFO] [paperless_mail] Located folder: Intake

> 

> [2026-01-04 17:50:01,258] [INFO] [paperless_mail] Located folder: [Gmail]

> 

> [2026-01-04 17:50:01,258] [INFO] [paperless_mail] Located folder: [Gmail]/All Mail

> 

> [2026-01-04 17:50:01,258] [INFO] [paperless_mail] Located folder: [Gmail]/Drafts

> 

> [2026-01-04 17:50:01,258] [INFO] [paperless_mail] Located folder: [Gmail]/Important

> 

> [2026-01-04 17:50:01,258] [INFO] [paperless_mail] Located folder: [Gmail]/Sent Mail

> 

> [2026-01-04 17:50:01,258] [INFO] [paperless_mail] Located folder: [Gmail]/Spam

> 

> [2026-01-04 17:50:01,259] [INFO] [paperless_mail] Located folder: [Gmail]/Starred

> 

> [2026-01-04 17:50:01,259] [INFO] [paperless_mail] Located folder: [Gmail]/Trash

> 

> [2026-01-04 17:50:01,259] [ERROR] [paperless_mail] Rule Intake Gmail.Intake: Error while processing rule: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 611, in _handle_mail_rule

> 

>     M.folder.set(folder)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/folder.py", line 43, in set

> 

>     check_command_status(result, MailboxFolderSelectError)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/utils.py", line 48, in check_command_status

> 

>     raise exception(command_result=command_result, expected=expected)

> 

> imap_tools.errors.MailboxFolderSelectError: Response status "OK" expected, but "NO" received. Data: [b'[NONEXISTENT] Unknown Mailbox: intake (now in authenticated state) (Failure)']

> 

> 

> The above exception was the direct cause of the following exception:

> 

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 573, in handle_mail_account

> 

>     total_processed_files += self._handle_mail_rule(

> 

>                              ^^^^^^^^^^^^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 625, in _handle_mail_rule

> 

>     raise MailError(

> 

> paperless_mail.mail.MailError: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> [2026-01-04 18:00:00,064] [DEBUG] [paperless_mail] Skipping mail preprocessor MailMessageDecryptor

> 

> [2026-01-04 18:00:00,065] [DEBUG] [paperless_mail] Processing mail account Intake Gmail

> 

> [2026-01-04 18:00:00,333] [DEBUG] [paperless_mail] GMAIL Label Support: True

> 

> [2026-01-04 18:00:00,333] [DEBUG] [paperless_mail] AUTH=PLAIN Support: True

> 

> [2026-01-04 18:00:00,914] [DEBUG] [paperless_mail] Account Intake Gmail: Processing 1 rule(s)

> 

> [2026-01-04 18:00:00,917] [DEBUG] [paperless_mail] Rule Intake Gmail.Intake: Selecting folder intake

> 

> [2026-01-04 18:00:01,078] [ERROR] [paperless_mail] Unable to access folder intake, attempting folder listing

> 

> [2026-01-04 18:00:01,246] [INFO] [paperless_mail] Located folder: INBOX

> 

> [2026-01-04 18:00:01,246] [INFO] [paperless_mail] Located folder: Intake

> 

> [2026-01-04 18:00:01,246] [INFO] [paperless_mail] Located folder: [Gmail]

> 

> [2026-01-04 18:00:01,246] [INFO] [paperless_mail] Located folder: [Gmail]/All Mail

> 

> [2026-01-04 18:00:01,247] [INFO] [paperless_mail] Located folder: [Gmail]/Drafts

> 

> [2026-01-04 18:00:01,247] [INFO] [paperless_mail] Located folder: [Gmail]/Important

> 

> [2026-01-04 18:00:01,247] [INFO] [paperless_mail] Located folder: [Gmail]/Sent Mail

> 

> [2026-01-04 18:00:01,247] [INFO] [paperless_mail] Located folder: [Gmail]/Spam

> 

> [2026-01-04 18:00:01,247] [INFO] [paperless_mail] Located folder: [Gmail]/Starred

> 

> [2026-01-04 18:00:01,247] [INFO] [paperless_mail] Located folder: [Gmail]/Trash

> 

> [2026-01-04 18:00:01,248] [ERROR] [paperless_mail] Rule Intake Gmail.Intake: Error while processing rule: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 611, in _handle_mail_rule

> 

>     M.folder.set(folder)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/folder.py", line 43, in set

> 

>     check_command_status(result, MailboxFolderSelectError)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/utils.py", line 48, in check_command_status

> 

>     raise exception(command_result=command_result, expected=expected)

> 

> imap_tools.errors.MailboxFolderSelectError: Response status "OK" expected, but "NO" received. Data: [b'[NONEXISTENT] Unknown Mailbox: intake (now in authenticated state) (Failure)']

> 

> 

> The above exception was the direct cause of the following exception:

> 

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 573, in handle_mail_account

> 

>     total_processed_files += self._handle_mail_rule(

> 

>                              ^^^^^^^^^^^^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 625, in _handle_mail_rule

> 

>     raise MailError(

> 

> paperless_mail.mail.MailError: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> [2026-01-04 18:10:00,058] [DEBUG] [paperless_mail] Skipping mail preprocessor MailMessageDecryptor

> 

> [2026-01-04 18:10:00,059] [DEBUG] [paperless_mail] Processing mail account Intake Gmail

> 

> [2026-01-04 18:10:00,373] [DEBUG] [paperless_mail] GMAIL Label Support: True

> 

> [2026-01-04 18:10:00,373] [DEBUG] [paperless_mail] AUTH=PLAIN Support: True

> 

> [2026-01-04 18:10:01,474] [DEBUG] [paperless_mail] Account Intake Gmail: Processing 1 rule(s)

> 

> [2026-01-04 18:10:01,476] [DEBUG] [paperless_mail] Rule Intake Gmail.Intake: Selecting folder intake

> 

> [2026-01-04 18:10:01,660] [ERROR] [paperless_mail] Unable to access folder intake, attempting folder listing

> 

> [2026-01-04 18:10:01,847] [INFO] [paperless_mail] Located folder: INBOX

> 

> [2026-01-04 18:10:01,848] [INFO] [paperless_mail] Located folder: Intake

> 

> [2026-01-04 18:10:01,848] [INFO] [paperless_mail] Located folder: [Gmail]

> 

> [2026-01-04 18:10:01,848] [INFO] [paperless_mail] Located folder: [Gmail]/All Mail

> 

> [2026-01-04 18:10:01,848] [INFO] [paperless_mail] Located folder: [Gmail]/Drafts

> 

> [2026-01-04 18:10:01,848] [INFO] [paperless_mail] Located folder: [Gmail]/Important

> 

> [2026-01-04 18:10:01,848] [INFO] [paperless_mail] Located folder: [Gmail]/Sent Mail

> 

> [2026-01-04 18:10:01,848] [INFO] [paperless_mail] Located folder: [Gmail]/Spam

> 

> [2026-01-04 18:10:01,849] [INFO] [paperless_mail] Located folder: [Gmail]/Starred

> 

> [2026-01-04 18:10:01,849] [INFO] [paperless_mail] Located folder: [Gmail]/Trash

> 

> [2026-01-04 18:10:01,849] [ERROR] [paperless_mail] Rule Intake Gmail.Intake: Error while processing rule: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 611, in _handle_mail_rule

> 

>     M.folder.set(folder)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/folder.py", line 43, in set

> 

>     check_command_status(result, MailboxFolderSelectError)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/utils.py", line 48, in check_command_status

> 

>     raise exception(command_result=command_result, expected=expected)

> 

> imap_tools.errors.MailboxFolderSelectError: Response status "OK" expected, but "NO" received. Data: [b'[NONEXISTENT] Unknown Mailbox: intake (now in authenticated state) (Failure)']

> 

> 

> The above exception was the direct cause of the following exception:

> 

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 573, in handle_mail_account

> 

>     total_processed_files += self._handle_mail_rule(

> 

>                              ^^^^^^^^^^^^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 625, in _handle_mail_rule

> 

>     raise MailError(

> 

> paperless_mail.mail.MailError: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> [2026-01-04 18:14:38,530] [DEBUG] [paperless_mail] Skipping mail preprocessor MailMessageDecryptor

> 

> [2026-01-04 18:14:38,531] [DEBUG] [paperless_mail] Processing mail account Intake Gmail

> 

> [2026-01-04 18:14:39,216] [DEBUG] [paperless_mail] GMAIL Label Support: True

> 

> [2026-01-04 18:14:39,216] [DEBUG] [paperless_mail] AUTH=PLAIN Support: True

> 

> [2026-01-04 18:14:39,855] [DEBUG] [paperless_mail] Account Intake Gmail: Processing 1 rule(s)

> 

> [2026-01-04 18:14:39,858] [DEBUG] [paperless_mail] Rule Intake Gmail.Intake: Selecting folder intake

> 

> [2026-01-04 18:14:40,047] [ERROR] [paperless_mail] Unable to access folder intake, attempting folder listing

> 

> [2026-01-04 18:14:40,212] [INFO] [paperless_mail] Located folder: INBOX

> 

> [2026-01-04 18:14:40,213] [INFO] [paperless_mail] Located folder: Intake

> 

> [2026-01-04 18:14:40,213] [INFO] [paperless_mail] Located folder: [Gmail]

> 

> [2026-01-04 18:14:40,213] [INFO] [paperless_mail] Located folder: [Gmail]/All Mail

> 

> [2026-01-04 18:14:40,213] [INFO] [paperless_mail] Located folder: [Gmail]/Drafts

> 

> [2026-01-04 18:14:40,213] [INFO] [paperless_mail] Located folder: [Gmail]/Important

> 

> [2026-01-04 18:14:40,214] [INFO] [paperless_mail] Located folder: [Gmail]/Sent Mail

> 

> [2026-01-04 18:14:40,214] [INFO] [paperless_mail] Located folder: [Gmail]/Spam

> 

> [2026-01-04 18:14:40,214] [INFO] [paperless_mail] Located folder: [Gmail]/Starred

> 

> [2026-01-04 18:14:40,214] [INFO] [paperless_mail] Located folder: [Gmail]/Trash

> 

> [2026-01-04 18:14:40,214] [ERROR] [paperless_mail] Rule Intake Gmail.Intake: Error while processing rule: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 611, in _handle_mail_rule

> 

>     M.folder.set(folder)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/folder.py", line 43, in set

> 

>     check_command_status(result, MailboxFolderSelectError)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/utils.py", line 48, in check_command_status

> 

>     raise exception(command_result=command_result, expected=expected)

> 

> imap_tools.errors.MailboxFolderSelectError: Response status "OK" expected, but "NO" received. Data: [b'[NONEXISTENT] Unknown Mailbox: intake (now in authenticated state) (Failure)']

> 

> 

> The above exception was the direct cause of the following exception:

> 

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 573, in handle_mail_account

> 

>     total_processed_files += self._handle_mail_rule(

> 

>                              ^^^^^^^^^^^^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 625, in _handle_mail_rule

> 

>     raise MailError(

> 

> paperless_mail.mail.MailError: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> [2026-01-04 18:15:42,378] [DEBUG] [paperless_mail] Skipping mail preprocessor MailMessageDecryptor

> 

> [2026-01-04 18:15:42,378] [DEBUG] [paperless_mail] Processing mail account Intake Gmail

> 

> [2026-01-04 18:15:42,642] [DEBUG] [paperless_mail] GMAIL Label Support: True

> 

> [2026-01-04 18:15:42,642] [DEBUG] [paperless_mail] AUTH=PLAIN Support: True

> 

> [2026-01-04 18:15:43,879] [DEBUG] [paperless_mail] Account Intake Gmail: Processing 1 rule(s)

> 

> [2026-01-04 18:15:43,882] [DEBUG] [paperless_mail] Rule Intake Gmail.Intake: Selecting folder intake

> 

> [2026-01-04 18:15:44,060] [ERROR] [paperless_mail] Unable to access folder intake, attempting folder listing

> 

> [2026-01-04 18:15:44,315] [INFO] [paperless_mail] Located folder: INBOX

> 

> [2026-01-04 18:15:44,316] [INFO] [paperless_mail] Located folder: Intake

> 

> [2026-01-04 18:15:44,316] [INFO] [paperless_mail] Located folder: [Gmail]

> 

> [2026-01-04 18:15:44,316] [INFO] [paperless_mail] Located folder: [Gmail]/All Mail

> 

> [2026-01-04 18:15:44,316] [INFO] [paperless_mail] Located folder: [Gmail]/Drafts

> 

> [2026-01-04 18:15:44,316] [INFO] [paperless_mail] Located folder: [Gmail]/Important

> 

> [2026-01-04 18:15:44,316] [INFO] [paperless_mail] Located folder: [Gmail]/Sent Mail

> 

> [2026-01-04 18:15:44,317] [INFO] [paperless_mail] Located folder: [Gmail]/Spam

> 

> [2026-01-04 18:15:44,317] [INFO] [paperless_mail] Located folder: [Gmail]/Starred

> 

> [2026-01-04 18:15:44,317] [INFO] [paperless_mail] Located folder: [Gmail]/Trash

> 

> [2026-01-04 18:15:44,317] [ERROR] [paperless_mail] Rule Intake Gmail.Intake: Error while processing rule: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 611, in _handle_mail_rule

> 

>     M.folder.set(folder)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/folder.py", line 43, in set

> 

>     check_command_status(result, MailboxFolderSelectError)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/utils.py", line 48, in check_command_status

> 

>     raise exception(command_result=command_result, expected=expected)

> 

> imap_tools.errors.MailboxFolderSelectError: Response status "OK" expected, but "NO" received. Data: [b'[NONEXISTENT] Unknown Mailbox: intake (now in authenticated state) (Failure)']

> 

> 

> The above exception was the direct cause of the following exception:

> 

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 573, in handle_mail_account

> 

>     total_processed_files += self._handle_mail_rule(

> 

>                              ^^^^^^^^^^^^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 625, in _handle_mail_rule

> 

>     raise MailError(

> 

> paperless_mail.mail.MailError: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> [2026-01-04 18:16:57,879] [DEBUG] [paperless_mail] Skipping mail preprocessor MailMessageDecryptor

> 

> [2026-01-04 18:16:57,880] [DEBUG] [paperless_mail] Processing mail account Intake Gmail

> 

> [2026-01-04 18:16:58,155] [DEBUG] [paperless_mail] GMAIL Label Support: True

> 

> [2026-01-04 18:16:58,155] [DEBUG] [paperless_mail] AUTH=PLAIN Support: True

> 

> [2026-01-04 18:16:58,721] [DEBUG] [paperless_mail] Account Intake Gmail: Processing 1 rule(s)

> 

> [2026-01-04 18:16:58,726] [DEBUG] [paperless_mail] Rule Intake Gmail.Intake: Selecting folder intake

> 

> [2026-01-04 18:16:58,881] [ERROR] [paperless_mail] Unable to access folder intake, attempting folder listing

> 

> [2026-01-04 18:16:59,032] [INFO] [paperless_mail] Located folder: INBOX

> 

> [2026-01-04 18:16:59,033] [INFO] [paperless_mail] Located folder: Intake

> 

> [2026-01-04 18:16:59,033] [INFO] [paperless_mail] Located folder: [Gmail]

> 

> [2026-01-04 18:16:59,033] [INFO] [paperless_mail] Located folder: [Gmail]/All Mail

> 

> [2026-01-04 18:16:59,033] [INFO] [paperless_mail] Located folder: [Gmail]/Drafts

> 

> [2026-01-04 18:16:59,033] [INFO] [paperless_mail] Located folder: [Gmail]/Important

> 

> [2026-01-04 18:16:59,034] [INFO] [paperless_mail] Located folder: [Gmail]/Sent Mail

> 

> [2026-01-04 18:16:59,034] [INFO] [paperless_mail] Located folder: [Gmail]/Spam

> 

> [2026-01-04 18:16:59,034] [INFO] [paperless_mail] Located folder: [Gmail]/Starred

> 

> [2026-01-04 18:16:59,034] [INFO] [paperless_mail] Located folder: [Gmail]/Trash

> 

> [2026-01-04 18:16:59,034] [ERROR] [paperless_mail] Rule Intake Gmail.Intake: Error while processing rule: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 611, in _handle_mail_rule

> 

>     M.folder.set(folder)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/folder.py", line 43, in set

> 

>     check_command_status(result, MailboxFolderSelectError)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/utils.py", line 48, in check_command_status

> 

>     raise exception(command_result=command_result, expected=expected)

> 

> imap_tools.errors.MailboxFolderSelectError: Response status "OK" expected, but "NO" received. Data: [b'[NONEXISTENT] Unknown Mailbox: intake (now in authenticated state) (Failure)']

> 

> 

> The above exception was the direct cause of the following exception:

> 

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 573, in handle_mail_account

> 

>     total_processed_files += self._handle_mail_rule(

> 

>                              ^^^^^^^^^^^^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 625, in _handle_mail_rule

> 

>     raise MailError(

> 

> paperless_mail.mail.MailError: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> [2026-01-04 18:17:17,683] [DEBUG] [paperless_mail] Skipping mail preprocessor MailMessageDecryptor

> 

> [2026-01-04 18:17:17,684] [DEBUG] [paperless_mail] Processing mail account Intake Gmail

> 

> [2026-01-04 18:17:17,904] [DEBUG] [paperless_mail] GMAIL Label Support: True

> 

> [2026-01-04 18:17:17,904] [DEBUG] [paperless_mail] AUTH=PLAIN Support: True

> 

> [2026-01-04 18:17:18,373] [DEBUG] [paperless_mail] Account Intake Gmail: Processing 1 rule(s)

> 

> [2026-01-04 18:17:18,376] [DEBUG] [paperless_mail] Rule Intake Gmail.Intake: Selecting folder intake

> 

> [2026-01-04 18:17:18,520] [ERROR] [paperless_mail] Unable to access folder intake, attempting folder listing

> 

> [2026-01-04 18:17:18,664] [INFO] [paperless_mail] Located folder: INBOX

> 

> [2026-01-04 18:17:18,664] [INFO] [paperless_mail] Located folder: Intake

> 

> [2026-01-04 18:17:18,665] [INFO] [paperless_mail] Located folder: [Gmail]

> 

> [2026-01-04 18:17:18,665] [INFO] [paperless_mail] Located folder: [Gmail]/All Mail

> 

> [2026-01-04 18:17:18,665] [INFO] [paperless_mail] Located folder: [Gmail]/Drafts

> 

> [2026-01-04 18:17:18,665] [INFO] [paperless_mail] Located folder: [Gmail]/Important

> 

> [2026-01-04 18:17:18,665] [INFO] [paperless_mail] Located folder: [Gmail]/Sent Mail

> 

> [2026-01-04 18:17:18,665] [INFO] [paperless_mail] Located folder: [Gmail]/Spam

> 

> [2026-01-04 18:17:18,665] [INFO] [paperless_mail] Located folder: [Gmail]/Starred

> 

> [2026-01-04 18:17:18,666] [INFO] [paperless_mail] Located folder: [Gmail]/Trash

> 

> [2026-01-04 18:17:18,666] [ERROR] [paperless_mail] Rule Intake Gmail.Intake: Error while processing rule: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 611, in _handle_mail_rule

> 

>     M.folder.set(folder)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/folder.py", line 43, in set

> 

>     check_command_status(result, MailboxFolderSelectError)

> 

>   File "/usr/local/lib/python3.12/site-packages/imap_tools/utils.py", line 48, in check_command_status

> 

>     raise exception(command_result=command_result, expected=expected)

> 

> imap_tools.errors.MailboxFolderSelectError: Response status "OK" expected, but "NO" received. Data: [b'[NONEXISTENT] Unknown Mailbox: intake (now in authenticated state) (Failure)']

> 

> 

> The above exception was the direct cause of the following exception:

> 

> 

> Traceback (most recent call last):

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 573, in handle_mail_account

> 

>     total_processed_files += self._handle_mail_rule(

> 

>                              ^^^^^^^^^^^^^^^^^^^^^^^

> 

>   File "/usr/src/paperless/src/paperless_mail/mail.py", line 625, in _handle_mail_rule

> 

>     raise MailError(

> 

> paperless_mail.mail.MailError: Rule Intake Gmail.Intake: Folder intake does not exist in account Intake Gmail

### Assistant
> Perfect. The logs give us a clean, definitive answer:
> 
> ### 1) Your mail rule is pointing at the wrong folder name
> Paperless is trying to select **`intake`** (lowercase) and Gmail IMAP says **NONEXISTENT**.
> 
> Your folder list shows **`Intake`** (capital I). That’s why nothing is arriving.
> 
> **Fix:** In the Paperless mail rule, set:
> 
> - **Folder = `Intake`** (exact casing)
> 
> Then re-run mail processing (wait for the next poll, or restart the container if you want it immediate).
> 
> ---
> 
> ### 2) You also accidentally fed Paperless `.eml` files via the consume folder
> These lines:
> 
> - `Consuming ... .eml`
> - `Unsupported mime type message/rfc822`
> 
> That means some workflow is dropping `.eml` into `/usr/src/paperless/consume` and Paperless is choking on it.
> 
> This is controlled by this mail rule setting you have visible:
> 
> > **“Process message as .eml and attachments separately”**  
> and/or  
> > **Attachment type / Only process attachments**
> 
> **Fix (recommended):**
> - Turn **OFF**: **Process message as .eml and attachments separately**
> - Set **Attachment type** = **Only process attachments**
> 
> This will prevent `.eml` objects from being shoved into the consumer pipeline at all, and Paperless will only ingest the actual attachments (PDFs, images, etc.).
> 
> ---
> 
> ## Do these two edits now (in this order)
> 
> ### A) Edit Mail Rule → Intake
> 1. Folder: change from `intake` → **`Intake`**
> 2. Disable: **Process message as .eml and attachments separately**
> 3. Attachment type: **Only process attachments**
> 
> Save.
> 
> ### B) Clean up the bad `.eml` items (optional but smart)
> Go to **Administration → File Tasks / Logs** and clear the failed tasks, or delete the `.eml` files if they’re sitting in the consume dir (depends how you deployed).
> 
> ---
> 
> ## Quick validation test (2 minutes)
> 1. Email `intake@qially.com` a PDF attachment.
> 2. In Gmail, apply label **Intake** (or leave in inbox if your rule targets that label).
> 3. Watch **mail.log**: you should see it select `Intake` successfully and process attachments.
> 
> ---
> 
> ## One more thing (important): your label naming convention
> Your mail rule says folder delimiter varies by server. Gmail IMAP labels are case-sensitive-ish in practice and Paperless is clearly treating it strictly. So:
> 
> - Use **Title Case labels** consistently (e.g., `Intake`, `Receipts`, `Legal/FCFCU`)
> - Mirror those exactly in Paperless rules.
> 
> ---
> 
> If you want, paste just the next 20–30 lines of **mail.log** after you change `intake → Intake`, and I’ll confirm it’s processing cleanly and not silently skipping.

### User
> i corrected the label and bam, it popped up. and the

### Assistant
> Good. That confirms the pipeline is working; it was purely the folder-name mismatch.
> 
> Now finish the sentence: “and the ___” — are you seeing one of these?
> 
> 1) **It imported the attachment but also created weird `.eml` failures** (message/rfc822).  
> 2) **It imported the whole email as a document** (you don’t want that).  
> 3) **It imported, but tags / document type / correspondent didn’t apply** (workflows not firing).  
> 4) **It imported, but it’s not moving/marking the email as processed** (mail action settings).
> 
> While you answer, here’s what you should do next regardless (this is the “make it professional” setup):
> 
> ### Lock the intake behavior (so no more `.eml` drama)
> In the mail rule:
> - **Attachment type:** Only process attachments  
> - **Process message as .eml and attachments separately:** OFF
> 
> ### Make your barcode/QID plan real (and not janky)
> - Yes, use **`QID`** as your prefix for barcodes/IDs.
> - The prefix field exists because Paperless’ ASN assignment is generic; it lets you align with an existing numbering scheme.
> - You will not get `asnasn…` if you set it correctly. What *will* happen is: the barcode value needs to be **numeric** if you’re using it to set the ASN (Paperless treats ASN as an integer). So a barcode payload like `QID000123` may **not** work for ASN assignment unless you use tag assignment or splitting, not ASN assignment.
> 
> **Professional approach:**
> - Keep ASN numeric (Paperless-native): `000123`
> - Use QID as your *human identifier* via:
>   - **Title template** or
>   - **Custom Field** (QID) populated by workflow/post-consume script, or
>   - **Tag-barcode mapping** (for tags), plus your own QID in metadata
> 
> ### Upscale + DPI (sane defaults)
> - **Upscale DPI:** `300`  
> - **Max pages:** leave default unless you’re dumping giant multi-hundred-page PDFs.
> 300 is the sweet spot for OCR accuracy vs file bloat. 600 is usually wasted unless the scans are truly microscopic text.
> 
> Now tell me what you meant by “and the …” (pick 1–4 above or paste the last lines from **mail.log** for that run), and I’ll give you the exact next switch to flip.

### User
> it imported just the attachment like we had set it  , and yes, we need the custom script to run qid and make sure its assigned a unique id. now here is the thing, how do we ensure we re not duplicating qids. how do we implment qid and make sure the app we call is the ocrrect one qi notes os.

### Assistant
> Perfect. If Paperless is reliably ingesting **attachments only**, you’re ready for the “professional layer”: a **QID generator + enforcer** that runs automatically.
> 
> You asked two things:
> 
> 1) **How do we guarantee we don’t duplicate QIDs?**  
> 2) **How do we implement QID + ensure the app/CLI we call is the correct one (QiNoteOS)?**
> 
> Let’s solve both cleanly.
> 
> ---
> 
> ## 1) The cleanest way to guarantee no duplicate QIDs
> 
> ### Option A (recommended): **Deterministic QID from Paperless Document ID**
> Paperless already guarantees uniqueness with its `doc_pk` (DOCUMENT_ID). So you don’t “generate” a QID at all — you **derive it**.
> 
> **Rule:**  
> `QID = qid{DOCUMENT_ID:07d}_0`
> 
> Examples:
> - Document ID 1 → `qid0000001_0`
> - Document ID 2599 → `qid0002599_0`
> 
> This is bulletproof because:
> - Document IDs are unique.
> - The QID becomes stable and reproducible.
> - No database “check” is required to avoid collisions.
> 
> This matches your current format: `qid000000_0` (just pick the padding length you want; 7 digits is a good start).
> 
> ### Option B: Random/sequence-based QIDs with uniqueness checks
> Possible, but it’s extra complexity (you must query Paperless to confirm uniqueness, handle race conditions, etc.). Option A avoids all that.
> 
> **Truth:** if you’re already inside Paperless, deriving from `DOCUMENT_ID` is the sane move.
> 
> ---
> 
> ## 2) Where to store QID so it’s “real” in the system
> 
> Use a **Custom Field** named `QID` (text). Then your script sets it on every ingest.
> 
> Optional but strongly recommended:
> - Put QID into the **Title** too, e.g.  
>   `{{ created }} — {{ correspondent }} — QID: qid0000123_0 — {{ title }}`  
>   But I prefer: keep Title human-readable and store QID in the custom field + filename format.
> 
> ---
> 
> ## 3) Implementation: Post-consume script (Paperless hook)
> 
> You want this to run after Paperless creates the doc so it has a DOCUMENT_ID to derive from.
> 
> ### What the script will do
> For each new document:
> 1) Read `DOCUMENT_ID` from env (Paperless provides it).
> 2) Compute deterministic QID.
> 3) Call Paperless REST API to:
>    - Set Custom Field `QID` to computed value
>    - Optionally prepend QID to Title (your choice)
> 
> ### Required config
> - Paperless API token (create in Paperless UI)
> - Paperless base URL reachable from the container/script
> 
> ### Script (Python)
> ```python
> #!/usr/bin/env python3
> import os
> import sys
> import requests
> 
> PAPERLESS_BASE_URL = os.environ.get("PAPERLESS_BASE_URL", "http://webserver:8000")
> PAPERLESS_API_TOKEN = os.environ.get("PAPERLESS_API_TOKEN")
> QID_FIELD_NAME = os.environ.get("QID_FIELD_NAME", "QID")
> QID_PREFIX = os.environ.get("QID_PREFIX", "qid")
> QID_PAD = int(os.environ.get("QID_PAD", "7"))  # 7 digits -> qid0000001_0
> QID_SUFFIX = os.environ.get("QID_SUFFIX", "_0")
> 
> DOCUMENT_ID = os.environ.get("DOCUMENT_ID")
> 
> def die(msg: str, code: int = 1):
>     print(msg, file=sys.stderr)
>     sys.exit(code)
> 
> def api_headers():
>     if not PAPERLESS_API_TOKEN:
>         die("Missing PAPERLESS_API_TOKEN env var.")
>     return {"Authorization": f"Token {PAPERLESS_API_TOKEN}", "Content-Type": "application/json"}
> 
> def get_custom_fields():
>     url = f"{PAPERLESS_BASE_URL}/api/custom_fields/"
>     r = requests.get(url, headers=api_headers(), timeout=30)
>     r.raise_for_status()
>     return r.json().get("results", r.json())
> 
> def find_qid_field_id(custom_fields):
>     for f in custom_fields:
>         if f.get("name") == QID_FIELD_NAME:
>             return f.get("id")
>     return None
> 
> def get_document(doc_id: str):
>     url = f"{PAPERLESS_BASE_URL}/api/documents/{doc_id}/"
>     r = requests.get(url, headers=api_headers(), timeout=30)
>     r.raise_for_status()
>     return r.json()
> 
> def patch_document(doc_id: str, payload: dict):
>     url = f"{PAPERLESS_BASE_URL}/api/documents/{doc_id}/"
>     r = requests.patch(url, headers=api_headers(), json=payload, timeout=30)
>     r.raise_for_status()
>     return r.json()
> 
> def main():
>     if not DOCUMENT_ID:
>         die("Missing DOCUMENT_ID env var (are you running as PAPERLESS_POST_CONSUME_SCRIPT?).")
> 
>     qid = f"{QID_PREFIX}{int(DOCUMENT_ID):0{QID_PAD}d}{QID_SUFFIX}"
> 
>     # Locate custom field id
>     cfs = get_custom_fields()
>     qid_field_id = find_qid_field_id(cfs)
>     if not qid_field_id:
>         die(f"Custom field '{QID_FIELD_NAME}' not found. Create it in Paperless UI first.")
> 
>     doc = get_document(DOCUMENT_ID)
>     existing_cfs = doc.get("custom_fields") or []
> 
>     # Update (or insert) the custom field value
>     updated = False
>     for cf in existing_cfs:
>         if cf.get("field") == qid_field_id:
>             cf["value"] = qid
>             updated = True
>             break
>     if not updated:
>         existing_cfs.append({"field": qid_field_id, "value": qid})
> 
>     payload = {"custom_fields": existing_cfs}
> 
>     # Optional: also add QID to title (comment out if you don’t want it)
>     # current_title = doc.get("title") or ""
>     # if "qid" not in current_title.lower():
>     #     payload["title"] = f"{qid} — {current_title}".strip(" —")
> 
>     patch_document(DOCUMENT_ID, payload)
>     print(f"Set {QID_FIELD_NAME}={qid} for document {DOCUMENT_ID}")
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ### Docker / env wiring (conceptual)
> - Mount the script into the container
> - Set:
>   - `PAPERLESS_POST_CONSUME_SCRIPT=/path/to/qid_post_consume.py`
>   - `PAPERLESS_BASE_URL=http://webserver:8000` (or your internal URL)
>   - `PAPERLESS_API_TOKEN=...`
> 
> ---
> 
> ## 4) “Barcodes with QID” — what works vs what breaks
> 
> If you want a printed barcode sticker that represents the document:
> 
> - You can print barcode value: `qid0000123_0`
> - Paperless can read it and use it for **tag assignment** / splitting, etc.
> 
> But:
> - **ASN assignment expects integer** values for the archive serial number.
> - So if you want “barcode sets ASN”, make barcode payload purely numeric (e.g., `0000123`) and then your script can still store `qid0000123_0` in custom field.
> 
> Best-of-both:
> - Barcode payload: `0000123` (numeric; usable as ASN)
> - Custom field + display identifier: `qid0000123_0`
> 
> ---
> 
> ## 5) Ensuring the correct app is “QiNoteOS” (not “QiNotes”, not “Keynote”)
> 
> This is naming + enforcement. Do it in three places:
> 
> ### A) Canonical identifiers (single source of truth)
> Set constants in one place (repo root or qi-cli config):
> 
> - `APP_CANONICAL_NAME = "QiNoteOS"`
> - `APP_SLUG = "qinoteos"`
> - `CLI = "qi-cli"` but subcommand is `qi-cli qinoteos ...`
> 
> ### B) Hard fail on wrong name
> In `qi-cli`, reject `qinotes`, `qi-notes`, `keynote`, etc. with a clear message:
> - “Invalid app name. Use `QiNoteOS` / `qinoteos`.”
> 
> ### C) One “command entrypoint”
> Your workflows/scripts should call one stable command:
> 
> - `qi-cli qinoteos sync --source paperless`
> 
> That prevents drift.
> 
> ---
> 
> ## What I need from you (no fluff, just the minimum to proceed)
> 
> 1) Are you running Paperless in Docker? If yes: do you have access to edit `docker-compose.yml` / env vars?  
> 2) What is your Paperless URL from inside the container context? (Often `http://webserver:8000`.)  
> 3) Confirm your Custom Field is literally named `QID` (case-sensitive).
> 
> If you answer those 3, I’ll give you the exact drop-in docker-compose snippet + the final “qi-cli → QiNoteOS” command contract so this becomes a real pipeline, not vibes.

### User
> problem is our qids are for qinote and they are banded, the qid clie has to read the doc meta data to decide band, or the script must be interactive so the user selects it and the parent qid if applicable to assing a kid qid instead, this helps create hierachly relationships.

### Assistant
> You’re right to call that out. If **QID is not a simple counter** and instead is a **banded, hierarchical identifier** (parent/child relationships, sometimes needs a parent QID, sometimes needs band selection), then a purely automatic “derive QID from Paperless doc ID” approach will be wrong.
> 
> The fix is to separate:
> 
> - **Ingestion identity** (always automatic, always unique)
> from
> - **QiNoteOS/QID identity** (banded + hierarchical, sometimes interactive)
> 
> You need a **two-stage pipeline**.
> 
> ---
> 
> ## The correct model: 2 IDs, 2 phases
> 
> ### Phase 1 — Ingest (Paperless-controlled)
> Assign an always-unique, non-semantic ID immediately.
> 
> Use Paperless’ `DOCUMENT_ID` as the canonical ingest key:
> 
> - `INGEST_ID = doc_pk` (or `pl0000123` if you want a prefix)
> 
> Store this in a custom field, e.g. `IngestID` or `PaperlessID`.
> 
> This gives you:
> - dedupe anchor
> - stable cross-system reference
> - zero collisions
> - no user input required
> 
> ### Phase 2 — Classify + Assign QID (QiNoteOS-controlled)
> Only after ingest do you assign the **real** banded/hierarchical QID.
> 
> That step can be:
> - interactive (user selects band + optional parent QID)
> - or auto (if metadata/rules can determine it confidently)
> - or hybrid (auto-suggest; user confirms)
> 
> Store QID in Paperless custom field `QID` once assigned.
> 
> ---
> 
> ## What this looks like operationally (clean + scalable)
> 
> ### Custom fields to add in Paperless
> Create these now (all text unless noted):
> 
> 1) `IngestID` (text) — set automatically to doc_pk
> 2) `QID` (text) — empty until assigned
> 3) `QID_Status` (select) — values: `UNASSIGNED`, `ASSIGNED`, `NEEDS_REVIEW`
> 4) `QID_Band` (select or text) — optional; helps filtering
> 5) `QID_Parent` (text) — optional; for hierarchy linkage
> 6) `QiNoteOS_Path` (text) — optional; where it landed in vault/export
> 
> This gives you a real queue and audit trail.
> 
> ---
> 
> ## How to avoid duplicate QIDs in a banded/hierarchy world
> 
> You need **one authoritative allocator**. If QIDs are “smart,” do not let Paperless generate them. Let **qi-cli (QiNoteOS)** be the only thing that can mint QIDs.
> 
> ### The allocator must enforce uniqueness with a lock + registry
> Minimum viable, robust approach:
> 
> - QiNoteOS keeps a local registry DB (SQLite is perfect) e.g. `qid_registry.sqlite`
> - Table: `qid`, `ingest_id`, `created_at`, `band`, `parent_qid`
> - Unique constraint on `qid`
> - When generating a new QID:
>   1) open transaction
>   2) compute next candidate for band/parent
>   3) insert; if conflict, increment/retry
>   4) commit
> 
> Optionally, also check Paperless for existing `QID == candidate` (belt + suspenders), but if the registry is the sole mint, that’s usually unnecessary.
> 
> This solves:
> - race conditions
> - re-runs
> - multiple machines (if registry is shared or centralized later)
> 
> ---
> 
> ## How the “interactive” part should work without being annoying
> 
> You do **not** want Paperless consumption to block waiting for a prompt.
> 
> Instead:
> 
> ### Pattern: “Inbox queue” + “Assign QID” action
> 1) Paperless ingests attachment → sets:
>    - `IngestID = doc_pk`
>    - `QID_Status = UNASSIGNED`
>    - maybe auto-tags like `INBOX/QID_PENDING`
> 
> 2) You review UNASSIGNED docs in Paperless (Saved View: `QID_Status = UNASSIGNED`)
> 
> 3) You run a command (manual, on-demand):
>    - `qi-cli qinoteos assign-qid --ingest-id 123`
>    - CLI pulls metadata + OCR text from Paperless via API
>    - CLI proposes band + parent candidates
>    - You confirm or pick:
>      - band
>      - parent QID (optional)
>      - maybe “this is a child of X”
>    - CLI mints QID via registry
>    - CLI PATCHes Paperless doc: sets `QID`, `QID_Status=ASSIGNED`, `QID_Parent`, etc.
> 
> That’s the right interaction point: after ingestion, not during.
> 
> ---
> 
> ## Where barcodes fit in (and still look professional)
> 
> You can still do “barcodes everywhere” without forcing QID to be decided at scan time.
> 
> ### Use barcode for IngestID (immediate), not QID (semantic)
> - Print labels like: `PL-0000123` or `INGEST-0000123` (derived from doc_pk after import)
> - Barcode/QR contains the ingest key or a deep-link to Paperless doc page
> - Later, when QID is assigned, you can optionally print a **QID label** too.
> 
> **Reality check:** If you want a barcode page to *trigger splitting* before import, that marker page cannot contain a doc_pk because doc_pk doesn’t exist yet. So use marker pages only for “split here” workflows, not identity. Identity happens after import.
> 
> ---
> 
> ## Ensuring you always call the correct app: QiNoteOS
> Make `qi-cli` enforce the canonical app:
> 
> - Only allow `qinoteos` subcommand
> - Reject others explicitly
> - Store it in config as the only valid target
> 
> Example command contract:
> - `qi-cli qinoteos assign-qid --paperless-id 123`
> - not `qi-cli qinotes ...`
> - not anything else
> 
> ---
> 
> ## Your next move (tight and decisive)
> 
> Pick one of these two workflows:
> 
> ### Workflow A (recommended): Post-consume script + manual queue assignment
> - Post-consume sets `IngestID` + `QID_Status=UNASSIGNED`
> - You run `qi-cli qinoteos assign-qid --ingest-id X` for each doc (or batch)
> 
> ### Workflow B: “Auto-suggest band” + confirm
> - Same as A, but CLI attempts band detection from metadata/OCR
> - Only prompts if confidence is low or parent is needed
> 
> ---
> 
> ## Two questions I need answered to lock the design (fast)
> 1) List your **bands** (even if rough): what are the valid band names/codes?  
> 2) When a doc becomes a “child,” what determines the parent? (manual always, or sometimes inferable from tags/correspondent/case like FCFCU/AES?)
> 
> Answer those and I’ll give you:
> - the exact Paperless custom field setup (names + types + saved views)
> - the post-consume script that only assigns `IngestID` + status
> - the qi-cli `assign-qid` command spec (interactive + batch mode) with a SQLite registry schema that guarantees zero duplicates.

### User
> i was going to say there can always be a secondary intake for qid assigning in qinote once exported from paperless and we just back fill the qid in paperless once created as an external reference in the qid custom field, which means we are good on paperless for now, mean the next step is the coding for exportings the qinote md files with front matter workflow, and the ingestions, chunckng, mapping that will push out the .md files for qinotes, then quinoteos does is business.

### Assistant
> Yes. That is the right call, and it’s cleaner than trying to force QID semantics into Paperless on day one.
> 
> Paperless becomes the **ingest + OCR + evidence locker**. QiNoteOS becomes the **semantic system of record**. You backfill QID into Paperless later as a cross-reference. That decouples everything, avoids collisions, and removes the “interactive during consume” trap.
> 
> Here’s the crisp architecture and the next build steps.
> 
> ---
> 
> ## Target architecture
> 
> ### Paperless-ngx (system of record for raw docs)
> Responsibilities:
> - Ingest (mail, upload, consume folder)
> - OCR + indexing
> - Basic tagging (FCFCU/AES/JOEL/ZJK etc.)
> - Stores the original files + archive PDFs
> 
> Fields to keep:
> - `PaperlessID` (doc_pk) — your immutable anchor
> - `QID` (text) — optional, backfilled later
> - (optional) `QiNote_Exported` (bool) and `QiNote_Exported_At` (date)
> 
> ### QiNoteOS (system of record for knowledge + hierarchy)
> Responsibilities:
> - QID minting (banded + parent-child)
> - Export generation (.md w/ YAML front matter)
> - Chunking + embeddings + mapping
> - Index for retrieval, linking, hierarchy
> 
> ---
> 
> ## The key rule: your “join key” is PaperlessID
> 
> Every exported note must carry:
> 
> - `paperless_id: 123` (doc_pk)
> - `source_system: paperless-ngx`
> - `source_uri: <paperless url if you have it>`
> - `source_file: archive.pdf` (if available)
> - `sha256: ...` (recommended)
> 
> Then later, when QiNoteOS assigns QID, it can PATCH back:
> 
> - Paperless Custom Field `QID = qid000123_0` (or whatever)
> - Optionally `QID_Parent`, `QID_Band`, `QiNote_Path`
> 
> That makes Paperless searchable by QID, but Paperless never has to understand QID logic.
> 
> ---
> 
> ## Next deliverable: the “QiNote Exporter” pipeline
> 
> You said: export QiNote markdown with front matter, then ingestion/chunking/mapping.
> 
> This is the correct sequence:
> 
> ### Step 1 — Exporter: Paperless → QiNote MD
> A script/service that:
> 1) pulls documents from Paperless API
> 2) downloads:
>    - archive PDF (preferred)
>    - original file (optional)
>    - extracted text (if available via API endpoints)
> 3) writes a QiNote `.md` stub per doc with YAML front matter + content
> 4) stores files into your QiNoteOS intake folder
> 
> **Minimum viable output per document:**
> - `YYYY-MM-DD_paperless_{doc_pk}_{slug}.md`
> - YAML front matter with stable fields
> - Body includes:
>   - title
>   - link back to Paperless
>   - extracted text (or summary placeholder)
>   - tags/correspondent/document_type
> 
> ### Step 2 — QiNoteOS intake: assign QID + map hierarchy
> QiNoteOS reads the intake md files and decides:
> - band
> - parent
> - qid mint
> - moves file to canonical vault location
> - updates front matter to include qid + parent fields
> - triggers embeddings/chunking
> 
> ### Step 3 — Backfill to Paperless
> QiNoteOS calls Paperless API:
> - set `QID` custom field on the doc
> - (optional) set `QiNote_Path`, `QID_Band`, etc.
> 
> ---
> 
> ## Concrete Markdown front matter spec (use this)
> 
> Use a stable schema so you don’t regret it later:
> 
> ```yaml
> ---
> qid: ""                 # backfilled later by QiNoteOS
> paperless_id: 123
> source_system: "paperless-ngx"
> source_type: "document"
> source_url: ""
> title: "..."
> created_date: "2026-01-04"
> added_date: "2026-01-04"
> correspondent: ""
> document_type: ""
> tags:
>   - FCFCU
>   - AES
> custom_fields:
>   case: "FCFCU"
>   person: "Cody"
> files:
>   archive_pdf: "paperless/123/archive.pdf"
>   original: "paperless/123/original.pdf"
> hash:
>   sha256: ""
> status:
>   exported: true
>   qid_status: "UNASSIGNED"
> ---
> ```
> 
> Body template:
> 
> ```md
> ## Source
> - Paperless ID: 123
> - Link: <...>
> 
> ## Extracted Text
> <raw text or placeholder>
> 
> ## Notes
> - 
> ```
> 
> This is QiNoteOS-friendly and makes backfill trivial.
> 
> ---
> 
> ## Export selection logic (don’t boil the ocean)
> 
> Start with one of these:
> 
> ### Option A (simplest): export “everything new since last run”
> - Keep a local state file: last exported `doc_pk` or timestamp
> - Query Paperless for docs added after that
> 
> ### Option B: export only docs tagged `QiNote_Export`
> - Create a Paperless tag “QiNote_Export”
> - Workflows can auto-tag based on correspondent/type
> - Exporter pulls only those and clears the tag after success
> 
> Option B gives you manual control while the system is young.
> 
> ---
> 
> ## What you need to implement right now (no QID required yet)
> 
> 1) **Paperless custom field**: `QID` (text)  
> 2) (Optional but helpful) `QiNote_Exported` (boolean) and `QiNote_Exported_At`  
> 3) A small exporter script/service.
> 
> ---
> 
> ## How QiNoteOS guarantees no duplicate QIDs (later)
> When you’re ready, QiNoteOS must be the allocator using a registry/lock as I described earlier. But importantly: **you don’t need to solve that today** to get the exporter working.
> 
> ---
> 
> ## Your next step (decisive)
> Tell me these three things and I’ll draft the exact implementation plan and file/folder layout for the exporter + the API calls:
> 
> 1) Where is Paperless running (local docker? Cloudflare tunnel? LAN IP)?  
> 2) Do you have Paperless API token already?  
> 3) Where is the QiNoteOS intake folder path (local path) you want to write the `.md` files and PDFs into?
> 
> If you don’t answer, I’ll still proceed with a default assumption: local docker, token-based auth, and an intake folder like `~/QiNoteOS/intake/paperless/`.

### User
> option b. and we can have gemini do this, but before that paperless is good to go for now i can close that repo or we still need it open, should i create a workspace with qinote and paperless so gemini can reference them both as it makes the workflow. is running local, but cloudflare tunnel is on, so do i now create this on cloudflare to run it from my browser moving forward or how does that work.

### Assistant
> Option B is the right choice.
> 
> Now, blunt truth: do **not** “have Gemini do this” as your first move if you mean “Gemini as the runtime.” Use Gemini (or me) as the **planner + code generator**, but the exporter needs to run as a **service you control** (container/systemd/cron). Otherwise you’ll end up with a fragile, manual, half-automated mess.
> 
> Below is the clean, low-regret path.
> 
> ---
> 
> ## 1) Is Paperless “done” or do we keep the repo open?
> 
> **Paperless is “operational” now.** Keep it open only for:
> - backing up config + volumes
> - adding 2 custom fields + 1 tag
> - confirming the Mail rule and tag behavior is stable
> 
> After that, you can “close” it mentally. You don’t need to keep poking it daily.
> 
> Minimum Paperless admin checklist (15 minutes):
> - Custom field: `QID` (text)
> - Tag: `QiNote_Export` (or `EXPORT_QINOTE`)
> - Optional: custom field `QiNote_Exported_At` (date) or `QiNote_Exported` (bool)
> 
> ---
> 
> ## 2) “Workspace” with QiNote + Paperless for Gemini?
> 
> Yes — but only if you mean a **shared repo/workspace** so code and docs can reference both systems cleanly.
> 
> Do this:
> 
> ### Create one parent workspace repo (recommended)
> **Repo name:** `qi-workflows` (or `QiNoteOS_Workflows`)
> 
> Inside:
> - `/paperless/` (notes + exporter config)
> - `/qinoteos/` (notes + intake spec)
> - `/exporter/` (actual code)
> - `/docs/` (workflow documentation, mapping tables)
> 
> This becomes the “single brain” for how systems integrate.
> 
> If you instead mean “Gemini Workspace” like a chat project: fine, but the **real value** is the repo + config files it can read.
> 
> ---
> 
> ## 3) Local + Cloudflare tunnel: do we run exporter on Cloudflare?
> 
> No. Not for this.
> 
> ### The exporter should run:
> - **locally**, next to Paperless and your QiNoteOS files
> - on a schedule (cron) or always-on (Docker container)
> 
> Cloudflare Tunnel is for **remote access**, not for running your local automation in the cloud.
> 
> **Why:** Cloudflare Workers cannot reliably write to your local filesystem, and you don’t want your QID/QiNote vault logic dependent on internet availability. You said “local-first”—act like it.
> 
> ### What Cloudflare *is* for here:
> - Access Paperless UI from anywhere
> - (Optional) Access a tiny “Exporter Status” page/API
> - (Optional) Secure access via Zero Trust policies
> 
> ---
> 
> ## 4) What “running it from my browser” should look like
> 
> You don’t want “browser-run.” You want:
> - exporter runs automatically every X minutes
> - you can *trigger it manually* from the browser if needed
> 
> Two good patterns:
> 
> ### Pattern A (simplest): cron + logs
> - Exporter container runs on a schedule (or cron on host)
> - Writes logs to a file
> - You check status in Paperless by seeing the tag removed / fields updated
> 
> ### Pattern B (slightly nicer): local exporter service + web button
> - Exporter runs as a small local service (FastAPI, etc.)
> - Has endpoints:
>   - `POST /run`
>   - `GET /status`
> - You access it via Cloudflare Tunnel (locked down)
> 
> **Pick B if you want a “Run Export” button.**
> 
> ---
> 
> ## 5) Option B workflow design (what happens operationally)
> 
> **Paperless workflow / rules:**
> - When mail arrives in Intake label → Paperless consumes attachment → assigns initial tags/type
> - You (or workflow) applies tag `QiNote_Export`
> 
> **Exporter job:**
> - Query Paperless: “documents with tag `QiNote_Export`”
> - For each:
>   - Download archive/original + metadata + OCR text
>   - Write `.md` into QiNoteOS intake folder
>   - Mark as exported:
>     - remove `QiNote_Export` tag (or add `QiNote_Exported`)
>     - optionally set `QiNote_Exported_At`
>   - DO NOT attempt QID assignment yet (as you already decided)
> 
> This is deterministic and auditable.
> 
> ---
> 
> ## 6) What you should do next (in order)
> 
> ### Step 1 — Decide where the exporter lives
> Choose one:
> - **same docker-compose stack** as Paperless (recommended)
> - separate repo/container on the same machine
> 
> I recommend: add a new service to the same compose project:
> `paperless-exporter`
> 
> ### Step 2 — Create the tag + custom fields in Paperless
> - Tag: `QiNote_Export`
> - Custom field: `QID` (text)
> - Optional: `QiNote_Exported_At` (date)
> 
> ### Step 3 — Create the shared workspace repo
> `qi-workflows/` with `/exporter/` and `/docs/`
> 
> ### Step 4 — Implement exporter v0
> - config via `.env`
> - token-based Paperless API
> - filter by tag
> - write markdown + download files
> 
> ---
> 
> ## 7) What I need from you to lock the exact implementation
> 
> Answer these (no fluff, just values):
> 
> 1) Paperless base URL **as seen from the machine running exporter**  
>    Example: `http://localhost:8000` (inside docker it may be `http://webserver:8000`)
> 
> 2) Is Paperless running via docker compose? (sounds like yes)
> 
> 3) Where is your QiNoteOS vault folder on disk?  
>    Example: `/home/cody/QiNoteOS/` or `D:\QiNoteOS\`
> 
> 4) Do you want Pattern A (cron) or Pattern B (web button + tunnel)?
> 
> If you give me those four, I’ll reply with:
> - exact folder layout
> - exact docker-compose service stanza
> - `.env` template
> - the exporter logic flow (and if you want, full code skeleton)
> 
> Right now, you’re at the “this is real” stage—don’t derail into cloud fantasies. Keep the exporter local, controlled, boring, and reliable. That’s how it becomes enterprise-grade.

### User
> give em the readme or dev docs from cold start for this.

### Assistant
> ```markdown
> ---
> title: "QiNoteOS + Paperless-ngx Integration (Option B) — Cold Start Dev Docs"
> date: 2026-01-07
> category: "dev_docs"
> keywords:
>   - paperless-ngx
>   - qinoteos
>   - exporter
>   - intake
>   - workflow
>   - cloudflare-tunnel
>   - gmail
>   - automation
> project_context: "Local-first document intake via Paperless-ngx; export into QiNoteOS markdown intake; defer QID assignment to QiNoteOS."
> ---
> 
> # QiNoteOS + Paperless-ngx Integration (Option B) — Cold Start Dev Docs
> 
> ## Goal (What “done” looks like)
> - Email attachments land in Paperless-ngx automatically.
> - Paperless handles OCR + indexing + tagging.
> - A local exporter picks up “ready” documents from Paperless and writes them into the QiNoteOS intake folder as:
>   - `*.md` with YAML front matter (QiNote-compatible)
>   - optional: original file copy (PDF, image, etc.)
> - QID assignment happens **later inside QiNoteOS** (interactive + banded logic), then the QID can be backfilled into Paperless (optional, phase 2).
> 
> This is the correct approach because Paperless is great at “capture + OCR + search,” and QiNoteOS is where your “QID hierarchy + knowledge system” lives.
> 
> ---
> 
> ## System Overview
> 
> ### Components
> 1. **Paperless-ngx (v2.20.3)**  
>    - Ingests files (consume folder + mail ingestion)
>    - OCRs documents
>    - Stores metadata and searchable text
> 
> 2. **Mail Intake (Gmail / Google Workspace)**
>    - Label/folder used as the “queue” for Paperless mail ingestion  
>    - You already fixed the label mismatch (“intake” vs “Intake”)
> 
> 3. **QiNoteOS (local-first vault)**
>    - Receives exported markdown + files
>    - Runs QID assignment + mapping + chunking + embedding later
> 
> 4. **Exporter Service (new)**
>    - Runs locally (same machine as Paperless)
>    - Queries Paperless API for documents tagged `QiNote_Export`
>    - Exports to QiNote intake folder
>    - Marks exported (removes tag / adds exported marker)
> 
> ### Data Flow
> 1. Email → Gmail label `Intake` → Paperless mail rule pulls attachments → Paperless consumes → OCR
> 2. Document gets tagged `QiNote_Export` (manual, auto, or workflow)
> 3. Exporter runs:
>    - pulls document metadata + OCR text + file
>    - generates QiNote markdown + file copy
>    - updates Paperless doc status (exported marker)
> 4. QiNoteOS intake flow:
>    - assigns banded QID, supports parent/child assignment
>    - later backfills QID into Paperless (phase 2)
> 
> ---
> 
> ## Key Design Decisions (Option B)
> ### QID is NOT generated in Paperless
> Reason: your QIDs are banded and may be hierarchical (parent/child). That requires:
> - reading metadata / classification
> - or interactive selection (human decision)
> QiNoteOS owns that decision.
> 
> ### Exporter is local; Cloudflare Tunnel is access only
> - Cloudflare Tunnel is for secure remote access to:
>   - Paperless UI
>   - (optional) exporter status endpoint
> - Exporter runs locally for reliability and filesystem access.
> 
> ---
> 
> ## Paperless Setup
> 
> ### Required Objects
> Create these in Paperless Admin UI:
> 
> #### Tags
> - `QiNote_Export` (queue tag)
> - Optional:
>   - `QiNote_Exported` (done tag)
>   - `Inbox` (if you use inbox workflows)
>   - case tags: `FCFCU`, `AES`, `JOEL`, `ZJK` (you already listed these)
> 
> #### Custom Fields
> - `QID` (Text) — used later for backfill from QiNoteOS
> - Optional:
>   - `QiNote_Exported_At` (Date/DateTime)
>   - `QiNote_Export_Batch` (Text)
> 
> #### Document Types (recommended minimal)
> - `Legal`
> - `Finance`
> - `Medical`
> - `Identity`
> - `Housing`
> - `Utilities`
> - `Immigration`
> - `Receipts`
> 
> Keep it simple. You can refine matching later.
> 
> ---
> 
> ## Mail Intake (Paperless Mail)
> 
> ### Mail Rule
> - Account: Gmail (Google Workspace mailbox)
> - Folder/Label: must match **exactly** what Paperless sees
>   - If logs show folder listing contains `Intake`, then set folder to `Intake` (case-sensitive)
> - Attachment handling: **Only process attachments** (you already set this)
> - Action parameter: required (depends on action choice)
>   - If you’re using “Tag mail with specified tag,” set:
>     - Action parameter = `PaperlessProcessed` (or any tag label you want applied in Gmail)
> 
> ### Known Failure Mode
> If you set folder to `intake` and Gmail label is `Intake`, Paperless throws:
> - `Folder intake does not exist...`
> Fix: match the exact folder/label name.
> 
> ---
> 
> ## Exporter Service (New)
> 
> ### What it does
> For every Paperless document tagged `QiNote_Export`:
> 1. Fetch metadata:
>    - Paperless doc ID
>    - title, created date, added date
>    - tags, correspondent, document type
> 2. Fetch OCR text / content (where supported)
> 3. Download the original/archive file (PDF, image)
> 4. Generate QiNote markdown file:
>    - YAML front matter (QiNoteOS schema)
>    - body = OCR text + link refs
> 5. Write output to QiNoteOS intake directory
> 6. Mark document as exported in Paperless:
>    - remove `QiNote_Export`
>    - add `QiNote_Exported` or set `QiNote_Exported_At`
> 
> ### Output Convention (recommended)
> Inside QiNoteOS vault:
> - `04_PRIMARY/00_inbox/paperless/`
>   - `YYYY-MM-DD_paperless_{doc_id}_{slug}.md`
>   - `YYYY-MM-DD_paperless_{doc_id}_{slug}.pdf` (optional copy)
> 
> This keeps Paperless-derived items clearly traceable.
> 
> ---
> 
> ## QiNote Markdown Template (Recommended)
> 
> Example generated markdown:
> 
> ```yaml
> ---
> qid: ""                   # blank until QiNoteOS assigns
> source_system: "paperless-ngx"
> paperless_id: 1234
> paperless_url: "http://paperless.local/documents/1234/"   # optional
> created: "2026-01-07"
> added: "2026-01-07"
> document_type: "Legal"
> tags:
>   - FCFCU
>   - QiNote_Export
> correspondent: "FCFCU"
> original_filename: "Notice.pdf"
> content_hash: ""          # optional
> status: "intake"
> ---
> # Title (from Paperless)
> ## Summary
> - (optional: can be blank until QiNoteOS enrichment)
> 
> ## OCR Text
> <full extracted text here>
> 
> ## Attachments
> - ./2026-01-07_paperless_1234_notice.pdf
> ```
> 
> Keep `qid` empty until assigned.
> 
> ---
> 
> ## Repo Layout (Workspace)
> 
> Create a single workspace repo for the integration:
> 
> ```
> qi-workflows/
>   README.md
>   docs/
>     architecture.md
>     paperless_setup.md
>     qinote_schema.md
>     runbook.md
>   exporter/
>     README.md
>     src/
>       exporter/
>         __init__.py
>         config.py
>         paperless_client.py
>         md_writer.py
>         runner.py
>     tests/
>     pyproject.toml
>     .env.example
>   paperless/
>     docker-compose.override.yml (optional)
>     notes/
>       mail_rules.md
>       tags_and_types.md
> ```
> 
> ---
> 
> ## Exporter Implementation (Spec-Level)
> 
> ### Configuration (.env)
> - `PAPERLESS_BASE_URL` (e.g. `http://webserver:8000` if inside Docker network)
> - `PAPERLESS_API_TOKEN`
> - `EXPORT_TAG` = `QiNote_Export`
> - `EXPORTED_TAG` = `QiNote_Exported` (optional)
> - `QINOTE_INTAKE_DIR` = path on host (mounted into container)
> - `EXPORT_FILES` = `true/false`
> - `POLL_INTERVAL_SECONDS` (if daemon) or run via cron
> 
> ### Exporter Modes
> - **Batch/cron** (recommended to start):
>   - run every 5–10 minutes
> - **Daemon** (later):
>   - loop with sleep and internal watermark
> 
> Batch is less fragile and easier to debug.
> 
> ---
> 
> ## Docker Compose Integration (Recommended Pattern)
> 
> Add a new service to the same docker-compose as Paperless.
> 
> ### Requirements
> - Exporter container must:
>   - reach Paperless API over docker network
>   - write to QiNoteOS intake directory via bind mount
> 
> Example snippet (conceptual):
> 
> ```yaml
> services:
>   exporter:
>     build: ./exporter
>     environment:
>       PAPERLESS_BASE_URL: http://webserver:8000
>       PAPERLESS_API_TOKEN: ${PAPERLESS_API_TOKEN}
>       EXPORT_TAG: QiNote_Export
>       EXPORTED_TAG: QiNote_Exported
>       QINOTE_INTAKE_DIR: /qinote/intake/paperless
>     volumes:
>       - /path/to/QiNoteOS:/qinote
>     depends_on:
>       - webserver
> ```
> 
> ---
> 
> ## Default Workflow Logic (Paperless Workflows)
> 
> ### Workflow Trigger
> - Trigger: `Document Added`
> - Filters:
>   - has tag `Inbox` OR filename wildcard OR mail account (optional)
> - Actions:
>   - set `document_type` from heuristics (optional)
>   - tag `QiNote_Export` if criteria match (optional)
> 
> You can keep this **manual** at first:
> - You review doc → add tags (FCFCU/AES/JOEL/ZJK) → apply `QiNote_Export`
> 
> Then automate after you have enough training examples.
> 
> ---
> 
> ## Operational Runbook
> 
> ### Day-to-day usage
> 1. Forward/label emails to `Intake`
> 2. Paperless ingests attachments
> 3. In Paperless:
>    - add case tags (`FCFCU`, `AES`, `JOEL`, `ZJK`)
>    - apply `QiNote_Export`
> 4. Exporter runs and writes into QiNoteOS intake
> 5. In QiNoteOS:
>    - run QID assignment step (interactive/banded)
>    - later backfill QID to Paperless (phase 2)
> 
> ### Verification checklist
> - Paperless shows doc consumed successfully
> - Doc has tag `QiNote_Export`
> - Exporter logs show exported
> - Markdown file exists in QiNoteOS intake
> - Paperless doc now marked exported (tag removed/added)
> 
> ---
> 
> ## Troubleshooting
> 
> ### Mail rule: nothing is importing
> - Check `mail.log`:
>   - if it says folder doesn’t exist → label mismatch (case-sensitive)
> - Confirm IMAP enabled for mailbox (Workspace admin + user settings)
> - Confirm authentication method (app password / OAuth, depending on your setup)
> 
> ### Paperless consumes `.eml` and fails
> You already saw:
> - `Unsupported mime type message/rfc822`
> Fix:
> - In the mail rule: **Only process attachments**
> - Do not feed `.eml` files into the consume folder unless you’ve configured `.eml` processing requirements.
> 
> ### Exporter not exporting
> - Confirm `PAPERLESS_BASE_URL` is correct from exporter’s perspective:
>   - inside Docker network: `http://webserver:8000`
>   - from host: `http://localhost:8000`
> - Confirm token works
> - Confirm tag name exact match
> 
> ---
> 
> ## Security Notes
> - Paperless API token is sensitive; store in `.env` not committed.
> - Cloudflare Tunnel should be locked behind Zero Trust policy (device + identity).
> - Exporter should not expose public endpoints unless protected.
> 
> ---
> 
> ## Phase 2 (Later): Backfill QID into Paperless
> Once QiNoteOS assigns QIDs:
> - QiNoteOS writes the QID into the markdown front matter
> - A backfill job:
>   - reads updated markdown
>   - maps `paperless_id → qid`
>   - updates Paperless custom field `QID`
> 
> This closes the loop without forcing QID logic into Paperless.
> 
> ---
> 
> ## Next Build Targets (Practical Order)
> 1. Exporter v0:
>    - export markdown + file copy
>    - remove/add tags to mark completion
> 2. QiNoteOS intake parser:
>    - ingest exported markdown
>    - interactive/banded QID assignment
> 3. Backfill job:
>    - update Paperless `QID` custom field
> 4. Automation upgrades:
>    - Paperless workflow auto-tags + auto-export criteria
>    - classification training once you have volume
> 
> ---
> 
> ## Open Decisions (You must choose)
> 1. Exporter trigger style:
>    - Cron batch (recommended)
>    - Daemon loop
>    - Web button + tunnel (later)
> 
> 2. Output structure in QiNoteOS:
>    - single intake folder
>    - or case-based subfolders
> 
> 3. Whether exporter copies the original file:
>    - Yes (recommended for portability)
>    - No (only references Paperless)
> 
> ---
> 
> ## Quick Start Checklist (5-minute)
> - [ ] Create Paperless tag: `QiNote_Export`
> - [ ] Create Paperless custom field: `QID` (text)
> - [ ] Confirm mail rule points to correct label (`Intake`)
> - [ ] Create QiNoteOS folder: `04_PRIMARY/00_inbox/paperless/`
> - [ ] Create repo `qi-workflows/` and commit these docs
> - [ ] Implement exporter v0 and run once against a single tagged doc
> 
> ---
> ```
> 
> If you want, I can also give you:
> - a **second README** that’s purely “operator-facing” (copy/paste steps, no theory), and
> - a **Gemini prompt** that generates the exporter skeleton exactly in the repo layout above.
