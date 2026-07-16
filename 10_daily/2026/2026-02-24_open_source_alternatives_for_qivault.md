---
layout: page
title: "Open-source alternatives for QiVault"
slug: "open_source_alternatives_for_qivault"
created_at: "2026-02-24 03:03:11"
updated_at: "2026-07-16T06:49:30-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-004.json"
template_key: master-template
date: 2026-02-24
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "699d694e-8aa8-832f-a8f2-84d799d94a40"
canonical_ref: ""
---

# Open-source alternatives for QiVault

## Overview
- **Date**: 2026-02-24 03:03:11
- **Conversation ID**: `699d694e-8aa8-832f-a8f2-84d799d94a40`
- **Source**: `Chat-Export-28513-2026/conversations-004.json`

## Chat History

### User
> zotero i really like how organized and rigid it is, it reminds me of a more rigid notion with linking and cross between paperlessngx and file manager. is there amything else free open source to have something like this for my qivault?

### Assistant
> You’re not wrong. **Zotero** hits that sweet spot of:
> 
> - Structured metadata  
> - Real file attachments  
> - Cross-linking  
> - Deterministic hierarchy  
> - Search that actually works  
> 
> If you’re building **QiVault** as a sovereign evidence + knowledge system, here are the best **free / open-source** options that feel similar — ranked by how close they are to what you like.
> 
> ---
> 
> ## 1️⃣ Obsidian (Free, not fully open-source but local-first)
> 
> **Closest to “rigid Notion but real files.”**
> 
> - Markdown files = actual files
> - Backlinks + graph view
> - YAML front matter (perfect for your QiDecimal schema)
> - Works beautifully with Git + Drive
> - Massive plugin ecosystem
> 
> Why this fits QiVault:
> - You can treat each document like a Zotero item
> - Attach PDFs directly
> - Use Dataview plugin for structured queries
> - Build cross-linked evidence maps
> 
> Weakness:
> - No native PDF metadata extraction
> - Needs plugins for advanced structure
> 
> If your brain likes rigid but flexible systems, this is strong.
> 
> ---
> 
> ## 2️⃣ Logseq (Fully open source, local-first)
> 
> Very similar to Obsidian but block-based.
> 
> - True bidirectional linking
> - Journaling + graph view
> - Good for “moments” / timeline systems (QiChronicle energy)
> 
> Better for:
> - Thinking systems
> - Less ideal for heavy document vaulting
> 
> ---
> 
> ## 3️⃣ Paperless-ngx (You already know this)
> 
> image_group{"layout":"carousel","aspect_ratio":"1:1","query":["Paperless-ngx dashboard","Paperless-ngx document view","Paperless-ngx tags interface","Paperless-ngx OCR processing screen"],"num_per_query":1}
> 
> Best for:
> - OCR
> - Automatic tagging
> - Deterministic document intake
> - Immutable-ish archive feel
> 
> If QiVault = evidence vault + ingestion pipeline  
> Paperless-ngx should be your **intake engine**, not your thinking layer.
> 
> ---
> 
> ## 4️⃣ Docspell (Underrated alternative to Paperless)
> 
> image_group{"layout":"carousel","aspect_ratio":"1:1","query":["Docspell dashboard","Docspell document tagging interface","Docspell OCR preview","Docspell metadata editing screen"],"num_per_query":1}
> 
> Open source document management system.
> 
> Stronger metadata model than Paperless.
> More “structured archive” feeling.
> Less popular, smaller ecosystem.
> 
> If you want more rigidity and workflow logic — this is interesting.
> 
> ---
> 
> ## 5️⃣ Mayan EDMS
> 
> image_group{"layout":"carousel","aspect_ratio":"1:1","query":["Mayan EDMS dashboard","Mayan EDMS document metadata view","Mayan EDMS workflow interface","Mayan EDMS versioning screen"],"num_per_query":1}
> 
> Enterprise-grade open source document system.
> 
> Pros:
> - Versioning
> - Workflows
> - Strong permission model
> 
> Cons:
> - Heavy
> - Overkill unless you’re running a law firm
> 
> This is “court-ready archive mode.”
> 
> ---
> 
> ## 6️⃣ SilverBullet
> 
> Lightweight, local, markdown knowledge base.
> 
> Cleaner than Obsidian.
> Less plugin chaos.
> Feels closer to structured note system.
> 
> But:
> Not strong for document vaulting.
> 
> ---
> 
> # If I Design QiVault Around You
> 
> Given everything you’re building:
> 
> - Legal case Bible
> - Evidence integrity
> - Immutable hashes
> - Cross-linking narrative layers
> - AI ingestion later
> 
> Here’s the clean architecture:
> 
> ### 🔥 Layer 1 – Intake & OCR
> Paperless-ngx
> 
> ### 🧠 Layer 2 – Knowledge + Linking
> Obsidian (or SilverBullet)
> 
> ### 🏛 Layer 3 – Immutable Archive
> Git repo + hash index + cold storage
> 
> ---
> 
> # Brutal Truth
> 
> There is no single open-source tool that perfectly combines:
> 
> - Zotero’s metadata rigidity  
> - Paperless OCR intake  
> - Notion linking  
> - Immutable file vault  
> - AI-ready schema  
> 
> You will build that hybrid.
> 
> And honestly?  
> You already are.
> 
> ---
> 
> # Strategic Question
> 
> What is QiVault supposed to be primarily?
> 
> A) Evidence locker  
> B) Knowledge brain  
> C) AI memory substrate  
> D) Client-facing vault  
> E) All of the above (in layers)
> 
> Answer that and I’ll give you the cleanest stack with zero bloat.

### User
> maya seems like doing too much, silver bullet aint doing nothing, obsidian just is an editor, paperless only does ocr and tagging, but meee, to much to set up i rather script that, doc spell on the surface looks and feel like zotero

### Assistant
> Good. That’s a clear instinct.
> 
> You don’t want:
> - A thinker (Obsidian)
> - A giant enterprise dinosaur (Mayan)
> - A half-tool (SilverBullet)
> - A black box intake robot (Paperless)
> 
> You want:
> 
> **Rigid. Deterministic. Metadata-first. File-attached. Searchable. Structured.**
> Like Zotero — but sovereign.
> 
> That’s why Docspell feels right to you.
> 
> ---
> 
> # What Docspell Actually Is
> 
> image_group{"layout":"carousel","aspect_ratio":"1:1","query":["Docspell dashboard clean UI","Docspell document metadata form","Docspell tag and folder system","Docspell OCR preview interface"],"num_per_query":1}
> 
> It’s basically:
> 
> - Metadata-first document system
> - File attachments stored cleanly
> - OCR integration
> - Tag + folder + custom fields
> - Deterministic search
> - Open source
> - Postgres backend
> 
> It feels closer to Zotero than Paperless does because:
> 
> - You can control metadata schema
> - It doesn’t try to be “auto magic everything”
> - It feels more database-backed than automation-backed
> 
> ---
> 
> # Why Your Brain Likes It
> 
> Because you think in:
> 
> - Structured nodes
> - Named artifacts
> - Controlled fields
> - Schema first
> - Deterministic retrieval
> 
> You don’t want:
> “AI just figure it out.”
> 
> You want:
> “If X exists, it must follow Y structure.”
> 
> That’s system architecture brain.
> 
> ---
> 
> # Now the Real Question
> 
> Is Docspell the core of QiVault?
> 
> Or just the intake/metadata UI?
> 
> Because here’s the truth:
> 
> Docspell = UI over Postgres + file store.
> 
> If you’re already running Supabase or Postgres, you could:
> 
> - Design your own schema
> - Build a lightweight UI in your QiOne launcher
> - Store files in object storage
> - Hash them
> - Attach metadata tables
> - Build your own “Zotero-like” module
> 
> And it would be cleaner long term.
> 
> ---
> 
> # Brutal Tradeoff Table
> 
> | Option | Setup Effort | Control | Long-Term Fit |
> |---------|--------------|----------|----------------|
> | Docspell | Medium | High | Good |
> | Custom QiVault module | High | Total | Best |
> | Paperless | Medium | Medium | Intake only |
> | Obsidian | Low | High (manual) | Brain only |
> 
> ---
> 
> # What I Think Is Actually Happening
> 
> You don’t want another tool.
> 
> You want:
> 
> QiVault =  
> Zotero UI +  
> Git integrity +  
> Postgres schema +  
> Object storage +  
> Vector embeddings later.
> 
> Docspell feels attractive because it’s the closest thing that already exists.
> 
> But it won’t integrate naturally with your QiOne ecosystem unless you wrap it.
> 
> ---
> 
> # Clean Path If You Want Minimal Chaos
> 
> Option A — Fast:
> Run Docspell as QiVault v0.
> Use it as structured document manager.
> Later integrate via API.
> 
> Option B — Strategic:
> Design the QiVault schema now.
> Build minimal admin UI.
> Script ingestion.
> Add OCR pipeline.
> Add hash integrity.
> Add embedding layer later.
> 
> Given your monorepo brain and need for cohesion?
> 
> Option B is more aligned.
> Option A scratches the itch faster.
> 
> ---
> 
> Now answer this:
> 
> Do you want QiVault to be:
> 
> 1) A tool you use  
> or  
> 2) Infrastructure everything else plugs into?
> 
> That determines everything.

### User
> compare with logseq, cause loq sec feels like a lean notino and that not what i need.  we we aleady set up the pipeline on our own, i guess really we just need a wrapper "UI" and object storage with integrity. so why can we just download the repo files fro docspell and make it our own so we are not starting from scratch.

### Assistant
> You’re thinking correctly.
> 
> You **don’t need a note system**.  
> You already built ingestion.  
> You already think in schema.  
> 
> You need:
> 
> > A deterministic document UI + metadata layer + object storage + integrity.
> 
> That’s not Logseq.
> 
> ---
> 
> # Logseq vs Docspell (For QiVault)
> 
> ## Logseq
> 
> image_group{"layout":"carousel","aspect_ratio":"1:1","query":["Logseq graph view","Logseq block editing interface","Logseq journal page example","Logseq backlink panel"],"num_per_query":1}
> 
> **What it is:**
> - Block-based markdown notebook
> - Graph thinking tool
> - Bidirectional linking
> - Local files
> 
> **What it is NOT:**
> - Structured document management
> - Deterministic metadata schema
> - File vault with integrity controls
> - Object storage aware
> 
> Logseq = thinking engine  
> QiVault = evidence system
> 
> Wrong category.
> 
> ---
> 
> ## Docspell
> 
> image_group{"layout":"carousel","aspect_ratio":"1:1","query":["Docspell document dashboard","Docspell metadata form","Docspell tag system","Docspell document search interface"],"num_per_query":1}
> 
> **What it is:**
> - Metadata-first document system
> - Structured fields
> - File attachment management
> - OCR integration
> - Postgres backend
> - API-driven
> 
> This is infrastructure-adjacent.
> 
> ---
> 
> # The Real Question You Asked
> 
> > Why not just download Docspell and fork it so we don’t start from scratch?
> 
> You absolutely can.
> 
> It’s open source (GPL).
> You can fork it.
> Strip what you don’t need.
> Re-theme it.
> Point storage to your object store.
> Modify schema.
> 
> That is a completely rational move.
> 
> ---
> 
> # But Here’s the Strategic Reality
> 
> Docspell is:
> 
> - Scala backend
> - Complex service architecture
> - Designed as a standalone system
> - Opinionated about workflow
> 
> If you fork it, you’re adopting:
> - Its stack
> - Its upgrade path
> - Its architecture constraints
> - Its dependency tree
> 
> That’s not “wrapper UI.”
> 
> That’s inheriting a product.
> 
> ---
> 
> # What You Actually Need
> 
> Based on what you said:
> 
> You already have:
> - Ingestion pipeline
> - File normalization
> - OCR plan
> - Naming rules
> - Dedup logic
> 
> So QiVault now needs:
> 
> 1. Postgres schema
> 2. Object storage (Drive, S3, R2, whatever)
> 3. Hash + integrity table
> 4. Minimal CRUD admin UI
> 5. Search layer
> 
> That’s it.
> 
> That is 20% of Docspell.
> 
> ---
> 
> # Brutal Strategic Comparison
> 
> | Path | Speed | Long-Term Control | Cognitive Load |
> |------|-------|------------------|----------------|
> | Fork Docspell | Medium | Medium | High |
> | Build Minimal UI Over Your Schema | Medium | Total | Clean |
> | Use Docspell Unmodified | Fast | Low | Medium |
> 
> If you fork it, you are now maintaining a document platform.
> 
> If you build thin UI over your DB, you are maintaining infrastructure.
> 
> Given how your brain works?
> 
> Infrastructure wins.
> 
> ---
> 
> # Cleaner Approach
> 
> Instead of forking Docspell:
> 
> Study it.
> 
> Borrow:
> - Their metadata modeling
> - Their search UX patterns
> - Their tagging system
> - Their document lifecycle logic
> 
> Then implement:
> 
> QiVault:
> - documents table
> - document_files table
> - document_hashes table
> - document_tags table
> - object_storage bucket
> - integrity verification script
> - simple React admin panel inside QiOne
> 
> Now it plugs into:
> - QiChronicle
> - AI embeddings
> - Case Bible
> - Client portals
> 
> No silo.
> 
> ---
> 
> # The Core Insight
> 
> You are not looking for a tool.
> 
> You are building a substrate.
> 
> Docspell is a tool.
> QiVault needs to be infrastructure.
> 
> If you just need UI and storage with integrity, you are 70% done already.
> 
> Now decide:
> 
> Do you want to maintain someone else’s document engine  
> or  
> own your vault layer completely?
> 
> Be honest.

### User
> well at the very least im going to peak at their code and get an idea of how they did there and im fure there are some file sthat might be useful.

### Assistant
> That’s the correct move.
> 
> Not “adopt it.”  
> Not “fork it.”  
> 
> **Reverse-engineer it.**
> 
> You’re harvesting patterns, not inheriting a stack.
> 
> ---
> 
> ## What To Look At Inside Docspell
> 
> When you open the repo, ignore 70% of it.
> 
> Focus only on:
> 
> ### 1️⃣ Data Model
> 
> Look for:
> - `Document`
> - `Attachment`
> - `Item`
> - `Tag`
> - `Folder`
> - `User`
> - `Metadata`
> - `CustomFields`
> 
> You want to understand:
> 
> - How they normalize metadata
> - How they attach files to records
> - Whether files are first-class or attachments
> - How tagging relationships are structured (many-to-many tables)
> 
> Steal the schema logic, not the implementation.
> 
> ---
> 
> ### 2️⃣ Storage Abstraction Layer
> 
> Find:
> - Where files are written
> - Whether storage is abstracted (filesystem vs S3)
> - How they track file location vs metadata
> - Whether they hash files at ingest
> 
> You care about:
> - File path logic
> - Object storage abstraction
> - Dedup detection method
> - Hashing strategy (SHA-256, etc.)
> 
> ---
> 
> ### 3️⃣ Search Layer
> 
> Check:
> - Are they using Postgres full-text?
> - Elastic?
> - Custom indexing?
> 
> You don’t need their whole engine.
> You need to understand how they model searchable fields.
> 
> ---
> 
> ### 4️⃣ Metadata Flexibility
> 
> Very important.
> 
> Do they:
> - Allow dynamic fields?
> - Or are fields hard-coded?
> 
> QiVault needs:
> Controlled schema + extensible fields.
> 
> ---
> 
> # What NOT To Get Distracted By
> 
> Ignore:
> - Auth system
> - Deployment scripts
> - UI theming
> - Workflow automations
> - Background job orchestration
> - Docker complexity
> 
> You’re not building Docspell.
> You’re extracting architectural DNA.
> 
> ---
> 
> # The Cleanest Strategy
> 
> Open repo.
> Map:
> 
> - Core entities
> - Relationships
> - File storage abstraction
> - Hashing model
> 
> Then build:
> 
> ```
> documents
> document_files
> document_hashes
> document_tags
> tags
> custom_fields
> document_field_values
> ```
> 
> Inside your QiOne Postgres.
> 
> Wrap with:
> Minimal React admin panel.
> 
> That’s your sovereign Zotero.
> 
> ---
> 
> # Important Reality Check
> 
> If Docspell’s core is too heavy or too entangled, that’s data.
> 
> If their data model is elegant and clean, you adapt it.
> 
> Either way, you win.
> 
> ---
> 
> You’re not looking for a tool anymore.
> 
> You’re benchmarking architecture.
> 
> When you open the repo, send me:
> 
> - The main model files
> - The schema definitions
> - Their file storage abstraction
> 
> And I’ll tell you in 2 minutes what’s worth stealing and what’s trash.

### User
> you see anything in the docs you would like to read to see how we can do our own QiDocSpell {

>   "name": "docs",

>   "path": "c:\\QiLabs\\docspell-master\\website\\docs",

>   "type": "directory",

>   "children": [

>     {

>       "name": "addons",

>       "type": "folder",

>       "children": [

>         {

>           "name": "_index.md",

>           "type": "file"

>         },

>         {

>           "name": "basics.md",

>           "type": "file"

>         },

>         {

>           "name": "control.md",

>           "type": "file"

>         },

>         {

>           "name": "using.md",

>           "type": "file"

>         },

>         {

>           "name": "writing.md",

>           "type": "file"

>         }

>       ]

>     },

>     {

>       "name": "api",

>       "type": "folder",

>       "children": [

>         {

>           "name": "_index.md",

>           "type": "file"

>         },

>         {

>           "name": "intro.md",

>           "type": "file"

>         },

>         {

>           "name": "upload.md",

>           "type": "file"

>         }

>       ]

>     },

>     {

>       "name": "configure",

>       "type": "folder",

>       "children": [

>         {

>           "name": "_index.md",

>           "type": "file"

>         },

>         {

>           "name": "admin-endpoint.md",

>           "type": "file"

>         },

>         {

>           "name": "authentication.md",

>           "type": "file"

>         },

>         {

>           "name": "baseurl.md",

>           "type": "file"

>         },

>         {

>           "name": "bind.md",

>           "type": "file"

>         },

>         {

>           "name": "custom-mapping.md",

>           "type": "file"

>         },

>         {

>           "name": "database.md",

>           "type": "file"

>         },

>         {

>           "name": "defaults.md",

>           "type": "file"

>         },

>         {

>           "name": "file-backends.md",

>           "type": "file"

>         },

>         {

>           "name": "file-processing.md",

>           "type": "file"

>         },

>         {

>           "name": "fulltext-search.md",

>           "type": "file"

>         },

>         {

>           "name": "main.md",

>           "type": "file"

>         },

>         {

>           "name": "registration.md",

>           "type": "file"

>         }

>       ]

>     },

>     {

>       "name": "dev",

>       "type": "folder",

>       "children": [

>         {

>           "name": "adr",

>           "type": "folder",

>           "children": [

>             {

>               "name": "0000_use_markdown_architectural_decision_records.md",

>               "type": "file"

>             },

>             {

>               "name": "0001_components.md",

>               "type": "file"

>             },

>             {

>               "name": "0002_component_interaction.md",

>               "type": "file"

>             },

>             {

>               "name": "0003_encryption.md",

>               "type": "file"

>             },

>             {

>               "name": "0004_iso8601vsEpoch.md",

>               "type": "file"

>             },

>             {

>               "name": "0005_job-executor.md",

>               "type": "file"

>             },

>             {

>               "name": "0006_more-file-types.md",

>               "type": "file"

>             },

>             {

>               "name": "0007_convert_html_files.md",

>               "type": "file"

>             },

>             {

>               "name": "0008_convert_plain_text.md",

>               "type": "file"

>             },

>             {

>               "name": "0009_convert_office_docs.md",

>               "type": "file"

>             },

>             {

>               "name": "0010_convert_image_files.md",

>               "type": "file"

>             },

>             {

>               "name": "0011_extract_text.md",

>               "type": "file"

>             },

>             {

>               "name": "0012_periodic_tasks.md",

>               "type": "file"

>             },

>             {

>               "name": "0013_archive_files.md",

>               "type": "file"

>             },

>             {

>               "name": "0014_fulltext_search_engine.md",

>               "type": "file"

>             },

>             {

>               "name": "0015_convert_pdf_files.md",

>               "type": "file"

>             },

>             {

>               "name": "0016_custom_fields.md",

>               "type": "file"

>             },

>             {

>               "name": "_index.md",

>               "type": "file"

>             },

>             {

>               "name": "process-files.png",

>               "type": "file"

>             },

>             {

>               "name": "process-files.puml",

>               "type": "file"

>             },

>             {

>               "name": "template.md",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "_index.md",

>           "type": "file"

>         },

>         {

>           "name": "add-language.md",

>           "type": "file"

>         },

>         {

>           "name": "building.md",

>           "type": "file"

>         },

>         {

>           "name": "development.md",

>           "type": "file"

>         },

>         {

>           "name": "documentation.md",

>           "type": "file"

>         },

>         {

>           "name": "translation.md",

>           "type": "file"

>         }

>       ]

>     },

>     {

>       "name": "feed",

>       "type": "folder",

>       "children": [

>         {

>           "name": "_index.md",

>           "type": "file"

>         }

>       ]

>     },

>     {

>       "name": "jsonminiquery",

>       "type": "folder",

>       "children": [

>         {

>           "name": "_index.md",

>           "type": "file"

>         }

>       ]

>     },

>     {

>       "name": "query",

>       "type": "folder",

>       "children": [

>         {

>           "name": "_index.md",

>           "type": "file"

>         }

>       ]

>     },

>     {

>       "name": "tools",

>       "type": "folder",

>       "children": [

>         {

>           "name": "_index.md",

>           "type": "file"

>         },

>         {

>           "name": "android.md",

>           "type": "file"

>         },

>         {

>           "name": "cli.md",

>           "type": "file"

>         },

>         {

>           "name": "ds4e.md",

>           "type": "file"

>         },

>         {

>           "name": "paperless-import.md",

>           "type": "file"

>         },

>         {

>           "name": "smtpgateway.md",

>           "type": "file"

>         }

>       ]

>     },

>     {

>       "name": "webapp",

>       "type": "folder",

>       "children": [

>         {

>           "name": "_index.md",

>           "type": "file"

>         },

>         {

>           "name": "autotagging.md",

>           "type": "file"

>         },

>         {

>           "name": "bookmarks.md",

>           "type": "file"

>         },

>         {

>           "name": "curate.md",

>           "type": "file"

>         },

>         {

>           "name": "customfields.md",

>           "type": "file"

>         },

>         {

>           "name": "dashboards.md",

>           "type": "file"

>         },

>         {

>           "name": "download-all.md",

>           "type": "file"

>         },

>         {

>           "name": "emailsettings.md",

>           "type": "file"

>         },

>         {

>           "name": "finding.md",

>           "type": "file"

>         },

>         {

>           "name": "itemcard-customize.md",

>           "type": "file"

>         },

>         {

>           "name": "mailitem.md",

>           "type": "file"

>         },

>         {

>           "name": "merge.md",

>           "type": "file"

>         },

>         {

>           "name": "metadata.md",

>           "type": "file"

>         },

>         {

>           "name": "multiedit.md",

>           "type": "file"

>         },

>         {

>           "name": "notification.md",

>           "type": "file"

>         },

>         {

>           "name": "notifydueitems.md",

>           "type": "file"

>         },

>         {

>           "name": "processing.md",

>           "type": "file"

>         },

>         {

>           "name": "scanmailbox.md",

>           "type": "file"

>         },

>         {

>           "name": "share.md",

>           "type": "file"

>         },

>         {

>           "name": "totp.md",

>           "type": "file"

>         },

>         {

>           "name": "uploading.md",

>           "type": "file"

>         }

>       ]

>     },

>     {

>       "name": "_index.md",

>       "type": "file"

>     }

>   ],

>   "metadata": {

>     "generated": "2026-02-24T09:41:12.441Z",

>     "generator": "FileTree Pro Extension",

>     "version": "0.2.0",

>     "showIcons": false,

>     "maxDepth": 10

>   }

> }

### Assistant
> Yes. There’s a very obvious “read these first” set in that tree that will tell you 80% of how Docspell thinks, and therefore what you want to copy for a QiDocSpell.
> 
> ## Read first (core architecture you can steal)
> 
> ### 1) `dev/adr/0001_components.md`
> Tells you what the system *is*, in terms of separable components (webapp, job runner, backend services). This is your “what do we actually need vs throw away” filter.
> 
> ### 2) `dev/adr/0002_component_interaction.md`
> This is the wiring diagram: what calls what, and when. This is where you’ll see their boundary decisions (API vs internal, async jobs, queues, etc.). Super relevant because you already have a pipeline and just need a UI wrapper.
> 
> ### 3) `configure/file-backends.md`
> This is directly your “object storage wrapper” answer.
> You’re looking for:
> - what backends they support
> - how they abstract storage
> - how they reference stored blobs from DB (path/key patterns)
> - any integrity/hashing assumptions
> 
> ### 4) `configure/file-processing.md` + `configure/file-processing.md` (and `configure/file-processing.md` if there’s separate “file-processing” vs “file-processing” pages—your tree shows `file-processing.md`)
> This is ingestion workflow: stages, conversions, OCR, text extraction, archive behavior. You want their *state machine*, not their tooling.
> 
> ### 5) `configure/fulltext-search.md` + `dev/adr/0014_fulltext_search_engine.md`
> This will tell you what search model they chose (Postgres FTS vs Elastic vs something else), and what tables/fields they index.
> 
> For QiDocSpell, you want:
> - “good enough” full-text search now (Postgres FTS)
> - vector later (pgvector / Supabase)
> 
> ### 6) `dev/adr/0016_custom_fields.md` + `webapp/customfields.md`
> This is huge for you. Your brain likes rigid schema *plus* extensibility.
> You want to copy:
> - how they model custom fields (EAV vs JSONB vs typed tables)
> - how they keep it queryable without becoming a mess
> 
> ### 7) `api/upload.md`
> This tells you the contract for getting documents in. Even if you don’t copy it, it’s the cleanest blueprint for your own upload endpoint(s) and client-side UI.
> 
> ---
> 
> ## Read second (features you’ll want in QiDocSpell v1)
> 
> ### `webapp/merge.md`
> If they do merge well (dedup + merge metadata + keep originals), steal the UX + the data model idea.
> 
> ### `webapp/metadata.md` + `webapp/finding.md`
> This is your “Zotero-feel” layer: item card, filters, advanced search patterns.
> 
> ### `configure/custom-mapping.md`
> If they support mapping extracted OCR/text into metadata fields, that’s your bridge between “pipeline output” and “curation UI”.
> 
> ### `configure/database.md`
> Not because you’ll use their stack, but because it reveals:
> - core tables
> - how they represent “document vs attachment”
> - how they store derived text / OCR outputs
> 
> ---
> 
> ## Read last (mostly skip unless needed)
> - `addons/*` (unless you want plugin-like behavior)
> - `tools/*` (android, cli, smtp gateway) unless those match your workflows
> - `webapp/*` things like email settings, scan mailbox, totp, share — useful later, not for QiVault core
> 
> ---
> 
> # What you’re actually extracting for QiDocSpell
> 
> You’re building 3 things:
> 
> ## A) Data model (Postgres)
> Minimum tables you’re likely to need (Docspell will confirm naming/relationships):
> - `documents` (the item)
> - `files` (one-to-many: original, derivatives, OCR text artifact, thumbnails)
> - `tags` + `document_tags`
> - `correspondents` (optional but nice—Zotero-ish)
> - `custom_fields` + `document_custom_field_values` (or JSONB if you choose)
> - `integrity_hashes` (sha256 per file, plus size + mime + created_at)
> - `processing_jobs` (status machine)
> 
> ## B) Storage abstraction (object store)
> - key format (stable, deterministic)
> - immutability policy (write-once, never overwrite originals)
> - derivative naming (thumbnails, extracted text, OCR PDF)
> 
> ## C) UI workflow (curate → tag → verify)
> - “inbox” view (unprocessed/needs review)
> - document card editing
> - merge/dedup UI
> - bulk edit
> 
> Docspell docs will show you how they solved B + C without turning it into Notion.
> 
> ---
> 
> ## If you want the fastest next step
> Paste the contents (raw text) of these 6 files and I’ll translate them directly into a QiDocSpell blueprint (schema + storage keys + UI screens):
> 
> 1. `dev/adr/0001_components.md`  
> 2. `dev/adr/0002_component_interaction.md`  
> 3. `configure/file-backends.md`  
> 4. `configure/file-processing.md`  
> 5. `dev/adr/0016_custom_fields.md`  
> 6. `api/upload.md`  
> 
> That’s the shortest path from “peek” to “we can build this cleanly.”

### User
> rememver we are using supabase and we have the optoin to use cloudflare, we have railway and drive. and this technically would be a module of qione, what do i tell the ide to scaffold this and make sure it alines with the rest.

### Assistant
> Tell the IDE to scaffold **QiVault Docs (QiDocSpell module)** as a QiOne module with: Supabase Postgres as system-of-record, object storage abstraction (Supabase Storage + optional Cloudflare R2 + optional Google Drive), integrity (SHA-256), and a lean admin UI focused on curate/search/tag/merge. No note-taking features.
> 
> Use this prompt.
> 
> ```text
> You are scaffolding a new module inside the QiOne monorepo: "qivault-docs" (QiDocSpell-like document vault UI).
> This is NOT a Notion/Logseq/Obsidian notes app. It is a metadata-first document vault: ingest → curate → tag → search → integrity → dedup/merge.
> 
> STACK + CONSTRAINTS
> - Monorepo: QiOne. Follow existing repo conventions for apps/modules, env vars, linting, formatting, routing, auth, roles.
> - Frontend: React + Vite (same as other QiOne modules) with a clean admin UI.
> - Backend: Supabase (Postgres + Auth + Storage). Use Supabase client on the frontend and edge functions only when needed.
> - Optional infra hooks (must be abstracted, not hardwired):
>   - Cloudflare R2 as alternate object store
>   - Google Drive as alternate/cold storage backbone
>   - Railway for workers/jobs if needed
> - Module must work with Supabase-only in v0. Optional backends are behind an interface.
> 
> GOAL
> Create a Docspell-like UI wrapper around our existing ingestion pipeline outputs:
> - Show "Inbox" (needs review), "Curated", "Archived"
> - Document detail page: metadata, tags, correspondents, dates, custom fields, attachments, derived artifacts
> - Search/filter: tags, date ranges, type, correspondent, status, text search
> - Multi-edit, merge/dedup (v1)
> - Integrity: every stored blob has sha256, size, mime, created_at; never overwrite originals; derivatives are separate blobs
> - API: minimal endpoints for upload + status updates + verification (Supabase Edge Functions or a small service)
> 
> DELIVERABLES
> 1) Create folder/app scaffolding aligned with QiOne conventions.
> 2) Create database migrations (SQL) for Supabase:
>    - documents
>    - document_files
>    - tags
>    - document_tags
>    - correspondents
>    - custom_fields
>    - document_custom_field_values
>    - ingestion_jobs
>    - file_integrity (sha256 etc.)
>    - dedup_candidates (optional table stub)
>    Include indexes for search, and enable Postgres full-text search on extracted text.
> 3) Implement RLS policies for multi-tenant (QiOne users/roles) with at least:
>    - owner access
>    - admin access
>    - (optional) shared read access
> 4) Storage abstraction:
>    - interface IBlobStore with implementations:
>      - SupabaseStorageBlobStore (default)
>      - R2BlobStore (stub)
>      - DriveBlobStore (stub)
>    - key naming convention: /{tenant_id}/{yyyy}/{mm}/{doc_id}/{file_id}/{variant}
>    - variants: original, ocr_pdf, extracted_text, thumbnail, preview_jpg
> 5) UI routes/pages (React Router or repo standard):
>    - /qivault-docs/inbox
>    - /qivault-docs/search
>    - /qivault-docs/document/:id
>    - /qivault-docs/tags
>    - /qivault-docs/settings (custom fields, correspondents)
> 6) Seed/demo data scripts for local dev.
> 7) README for this module: setup, env vars, running, migration apply, storage backends.
> 8) A “contract” folder documenting how the ingestion pipeline drops outputs into this module (tables/files) so both sides stay aligned.
> 
> INTEGRATION REQUIREMENTS
> - Auth must reuse QiOne authentication (Supabase Auth) and match existing user/role model.
> - Module must register itself in the QiOne launcher/navigation the same way other modules do.
> - Use the same UI component library and styling approach as the rest of QiOne.
> - No bespoke one-off patterns; follow existing patterns for data fetching, error handling, logging.
> 
> IMPLEMENTATION PHASING
> - v0: inbox + document detail + tags + basic search + upload endpoint + integrity hashing on upload
> - v1: multi-edit + merge/dedup + correspondents + custom fields UI
> - v2: R2/Drive storage backends + scheduled integrity verification job + embeddings pipeline integration
> 
> OUTPUT FORMAT
> - Produce:
>   A) directory tree you created
>   B) migrations SQL
>   C) key TypeScript interfaces (BlobStore, Document types)
>   D) initial React pages/components stubs
>   E) RLS policy SQL
>   F) README
> Do not include placeholders like "TODO: fill later" except where explicitly marked as stub (R2/Drive implementations).
> ```
> 
> If your IDE has access to your repo, that prompt is enough to generate a coherent first cut that aligns with QiOne.
> 
> If it doesn’t (it’s “blind”), add this small preface line at the top of the prompt:
> 
> ```text
> Before scaffolding, inspect the existing QiOne repo to copy conventions for: module registration in launcher/nav, env var naming, Supabase client initialization, routing, and UI component patterns. Mirror those patterns exactly.
> ```

### User
> in mmodules i see some postgres, in there anything else we might find usefull. # File Tree: modules

> 

> **Generated:** 2/24/2026, 3:46:14 AM

> **Root Path:** `c:\QiLabs\docspell-master\modules`

> 

> ```

> ├── addonlib

> │   └── src

> │       ├── main

> │       │   └── scala

> │       │       └── docspell

> │       │           └── addons

> │       │               ├── runner

> │       │               │   ├── CollectOut.scala

> │       │               │   ├── DockerBuilder.scala

> │       │               │   ├── DockerRunner.scala

> │       │               │   ├── NSpawnBuilder.scala

> │       │               │   ├── NixFlakeRunner.scala

> │       │               │   ├── RunnerUtil.scala

> │       │               │   └── TrivialRunner.scala

> │       │               ├── AddonArchive.scala

> │       │               ├── AddonExecutionResult.scala

> │       │               ├── AddonExecutor.scala

> │       │               ├── AddonExecutorConfig.scala

> │       │               ├── AddonLoggerExtension.scala

> │       │               ├── AddonMeta.scala

> │       │               ├── AddonRef.scala

> │       │               ├── AddonResult.scala

> │       │               ├── AddonRunner.scala

> │       │               ├── AddonTriggerType.scala

> │       │               ├── Context.scala

> │       │               ├── InputEnv.scala

> │       │               ├── Middleware.scala

> │       │               ├── RunnerType.scala

> │       │               └── package.scala

> │       └── test

> │           ├── resources

> │           │   ├── docspell-addon-single-file.zip

> │           │   ├── docspell-dummy-addon-master.zip

> │           │   └── minimal-addon.zip

> │           └── scala

> │               └── docspell

> │                   └── addons

> │                       ├── AddonArchiveTest.scala

> │                       ├── AddonExecutorTest.scala

> │                       ├── AddonGenerator.scala

> │                       ├── AddonMetaTest.scala

> │                       ├── AddonOutputTest.scala

> │                       ├── AddonRunnerTest.scala

> │                       └── Fixtures.scala

> ├── analysis

> │   └── src

> │       ├── main

> │       │   └── scala

> │       │       └── docspell

> │       │           └── analysis

> │       │               ├── classifier

> │       │               │   ├── ClassifierModel.scala

> │       │               │   ├── StanfordTextClassifier.scala

> │       │               │   ├── TextClassifier.scala

> │       │               │   └── TextClassifierConfig.scala

> │       │               ├── contact

> │       │               │   ├── Contact.scala

> │       │               │   ├── Domain.scala

> │       │               │   └── Tld.scala

> │       │               ├── date

> │       │               │   ├── DateFind.scala

> │       │               │   └── MonthName.scala

> │       │               ├── nlp

> │       │               │   ├── Annotator.scala

> │       │               │   ├── BasicCRFAnnotator.scala

> │       │               │   ├── LabelConverter.scala

> │       │               │   ├── PipelineCache.scala

> │       │               │   ├── Properties.scala

> │       │               │   ├── StanfordNerAnnotator.scala

> │       │               │   └── StanfordNerSettings.scala

> │       │               ├── split

> │       │               │   ├── TextSplitter.scala

> │       │               │   └── Word.scala

> │       │               ├── NlpSettings.scala

> │       │               ├── TextAnalyser.scala

> │       │               └── TextAnalysisConfig.scala

> │       └── test

> │           ├── resources

> │           │   └── test.ser.gz

> │           └── scala

> │               └── docspell

> │                   └── analysis

> │                       ├── classifier

> │                       │   └── StanfordTextClassifierSuite.scala

> │                       ├── contact

> │                       │   └── ContactAnnotateSpec.scala

> │                       ├── date

> │                       │   └── DateFindTest.scala

> │                       ├── nlp

> │                       │   ├── BaseCRFAnnotatorSuite.scala

> │                       │   └── StanfordNerAnnotatorSuite.scala

> │                       ├── split

> │                       │   └── TestSplitterSpec.scala

> │                       └── Env.scala

> ├── backend

> │   └── src

> │       ├── main

> │       │   └── scala

> │       │       └── docspell

> │       │           └── backend

> │       │               ├── auth

> │       │               │   ├── AuthToken.scala

> │       │               │   ├── Login.scala

> │       │               │   ├── RememberToken.scala

> │       │               │   ├── ShareToken.scala

> │       │               │   └── TokenUtil.scala

> │       │               ├── codec

> │       │               │   └── ItemQueryCodec.scala

> │       │               ├── fulltext

> │       │               │   └── CreateIndex.scala

> │       │               ├── item

> │       │               │   └── Merge.scala

> │       │               ├── joex

> │       │               │   ├── AddonEnvConfig.scala

> │       │               │   ├── AddonOps.scala

> │       │               │   ├── AddonPostProcess.scala

> │       │               │   ├── AddonPrepare.scala

> │       │               │   ├── FindJobOwnerAccount.scala

> │       │               │   └── LoggerExtension.scala

> │       │               ├── msg

> │       │               │   └── Topics.scala

> │       │               ├── ops

> │       │               │   ├── search

> │       │               │   │   ├── OSearch.scala

> │       │               │   │   └── QueryParseResult.scala

> │       │               │   ├── AddonRunConfigError.scala

> │       │               │   ├── AddonRunConfigValidate.scala

> │       │               │   ├── AddonValidate.scala

> │       │               │   ├── AddonValidationError.scala

> │       │               │   ├── OAddons.scala

> │       │               │   ├── OAttachment.scala

> │       │               │   ├── OClientSettings.scala

> │       │               │   ├── OCollective.scala

> │       │               │   ├── OCustomFields.scala

> │       │               │   ├── ODownloadAll.scala

> │       │               │   ├── OEquipment.scala

> │       │               │   ├── OFileRepository.scala

> │       │               │   ├── OFolder.scala

> │       │               │   ├── OFulltext.scala

> │       │               │   ├── OItem.scala

> │       │               │   ├── OItemLink.scala

> │       │               │   ├── OItemSearch.scala

> │       │               │   ├── OJob.scala

> │       │               │   ├── OJoex.scala

> │       │               │   ├── OMail.scala

> │       │               │   ├── ONode.scala

> │       │               │   ├── ONotification.scala

> │       │               │   ├── OOrganization.scala

> │       │               │   ├── OQueryBookmarks.scala

> │       │               │   ├── OShare.scala

> │       │               │   ├── OSource.scala

> │       │               │   ├── OTag.scala

> │       │               │   ├── OTotp.scala

> │       │               │   ├── OUpload.scala

> │       │               │   ├── OUserTask.scala

> │       │               │   └── WildcardString.scala

> │       │               ├── signup

> │       │               │   ├── Config.scala

> │       │               │   ├── ExternalAccount.scala

> │       │               │   ├── NewInviteResult.scala

> │       │               │   ├── OSignup.scala

> │       │               │   ├── RegisterData.scala

> │       │               │   └── SignupResult.scala

> │       │               ├── task

> │       │               │   └── DownloadZipArgs.scala

> │       │               ├── AttachedEvent.scala

> │       │               ├── BackendApp.scala

> │       │               ├── BackendCommands.scala

> │       │               ├── Common.scala

> │       │               ├── Config.scala

> │       │               ├── JobFactory.scala

> │       │               ├── MailAddressCodec.scala

> │       │               └── PasswordCrypt.scala

> │       └── test

> │           └── scala

> │               └── docspell

> │                   └── backend

> │                       └── auth

> │                           └── AuthTokenTest.scala

> ├── common

> │   └── src

> │       ├── main

> │       │   └── scala

> │       │       └── docspell

> │       │           └── common

> │       │               ├── bc

> │       │               │   ├── AttachmentAction.scala

> │       │               │   ├── BackendCommand.scala

> │       │               │   ├── BackendCommandRunner.scala

> │       │               │   └── ItemAction.scala

> │       │               ├── exec

> │       │               │   ├── Args.scala

> │       │               │   ├── Env.scala

> │       │               │   ├── ExternalCommand.scala

> │       │               │   ├── SysCmd.scala

> │       │               │   └── SysExec.scala

> │       │               ├── syntax

> │       │               │   ├── EitherSyntax.scala

> │       │               │   ├── FileSyntax.scala

> │       │               │   ├── StreamSyntax.scala

> │       │               │   ├── StringSyntax.scala

> │       │               │   └── package.scala

> │       │               ├── util

> │       │               │   ├── Directory.scala

> │       │               │   ├── File.scala

> │       │               │   ├── Random.scala

> │       │               │   ├── ResourceUse.scala

> │       │               │   ├── SignUtil.scala

> │       │               │   ├── Zip.scala

> │       │               │   └── ZipImpl.scala

> │       │               ├── AccountId.scala

> │       │               ├── AccountInfo.scala

> │       │               ├── AccountSource.scala

> │       │               ├── AllPreviewsArgs.scala

> │       │               ├── Banner.scala

> │       │               ├── BaseJsonCodecs.scala

> │       │               ├── Binary.scala

> │       │               ├── ByteSize.scala

> │       │               ├── CollectiveId.scala

> │       │               ├── CollectiveState.scala

> │       │               ├── ContactKind.scala

> │       │               ├── ConvertAllPdfArgs.scala

> │       │               ├── CustomFieldType.scala

> │       │               ├── DataType.scala

> │       │               ├── Direction.scala

> │       │               ├── DocspellSystem.scala

> │       │               ├── DownloadAllType.scala

> │       │               ├── DownloadState.scala

> │       │               ├── Duration.scala

> │       │               ├── EmptyTrashArgs.scala

> │       │               ├── EnvMode.scala

> │       │               ├── EquipmentUse.scala

> │       │               ├── FileCategory.scala

> │       │               ├── FileCopyTaskArgs.scala

> │       │               ├── FileIntegrityCheckArgs.scala

> │       │               ├── FileKey.scala

> │       │               ├── FileKeyPart.scala

> │       │               ├── FileName.scala

> │       │               ├── FileStoreConfig.scala

> │       │               ├── FileStoreType.scala

> │       │               ├── Glob.scala

> │       │               ├── Hash.scala

> │       │               ├── IdRef.scala

> │       │               ├── Ident.scala

> │       │               ├── ItemAddonTaskArgs.scala

> │       │               ├── ItemQueryString.scala

> │       │               ├── ItemState.scala

> │       │               ├── JobState.scala

> │       │               ├── JvmInfo.scala

> │       │               ├── Language.scala

> │       │               ├── LearnClassifierArgs.scala

> │       │               ├── LenientUri.scala

> │       │               ├── ListType.scala

> │       │               ├── LogLevel.scala

> │       │               ├── MailSendConfig.scala

> │       │               ├── MakePageCountArgs.scala

> │       │               ├── MakePreviewArgs.scala

> │       │               ├── MetaProposal.scala

> │       │               ├── MetaProposalList.scala

> │       │               ├── MetaProposalType.scala

> │       │               ├── MimeType.scala

> │       │               ├── MimeTypeHint.scala

> │       │               ├── NerDateLabel.scala

> │       │               ├── NerLabel.scala

> │       │               ├── NerLabelSpan.scala

> │       │               ├── NerTag.scala

> │       │               ├── NlpMode.scala

> │       │               ├── NodeType.scala

> │       │               ├── OrgUse.scala

> │       │               ├── Password.scala

> │       │               ├── PersonRef.scala

> │       │               ├── PersonUse.scala

> │       │               ├── Pools.scala

> │       │               ├── Priority.scala

> │       │               ├── ProcessItemArgs.scala

> │       │               ├── ReIndexTaskArgs.scala

> │       │               ├── ReProcessItemArgs.scala

> │       │               ├── ScanMailboxArgs.scala

> │       │               ├── ScheduledAddonTaskArgs.scala

> │       │               ├── SearchMode.scala

> │       │               ├── TaskArguments.scala

> │       │               ├── ThreadFactories.scala

> │       │               ├── Timestamp.scala

> │       │               ├── UrlMatcher.scala

> │       │               ├── UrlReader.scala

> │       │               └── UserState.scala

> │       └── test

> │           └── scala

> │               └── docspell

> │                   └── common

> │                       ├── bc

> │                       │   └── BackendCommandTest.scala

> │                       ├── exec

> │                       │   └── ExternalCommandTest.scala

> │                       ├── util

> │                       │   ├── DirectoryTest.scala

> │                       │   └── SignUtilTest.scala

> │                       ├── FileNameTest.scala

> │                       ├── GlobTest.scala

> │                       ├── LenientUriTest.scala

> │                       ├── MetaProposalListTest.scala

> │                       ├── MimeTypeTest.scala

> │                       ├── NerLabelSpanTest.scala

> │                       └── UrlMatcherTest.scala

> ├── config

> │   └── src

> │       ├── main

> │       │   └── scala

> │       │       └── docspell

> │       │           └── config

> │       │               ├── ConfigFactory.scala

> │       │               ├── EnvConfig.scala

> │       │               ├── FtsType.scala

> │       │               ├── Implicits.scala

> │       │               ├── PgFtsConfig.scala

> │       │               └── Validation.scala

> │       └── test

> │           ├── resources

> │           │   └── reference.conf

> │           └── scala

> │               └── docspell

> │                   └── config

> │                       ├── EnvConfigTest.scala

> │                       └── ValidationTest.scala

> ├── convert

> │   └── src

> │       ├── main

> │       │   └── scala

> │       │       └── docspell

> │       │           └── convert

> │       │               ├── extern

> │       │               │   ├── ExternConv.scala

> │       │               │   ├── OcrMyPdf.scala

> │       │               │   ├── OcrMyPdfConfig.scala

> │       │               │   ├── Tesseract.scala

> │       │               │   ├── TesseractConfig.scala

> │       │               │   ├── Unoconv.scala

> │       │               │   ├── UnoconvConfig.scala

> │       │               │   ├── Weasyprint.scala

> │       │               │   ├── WeasyprintConfig.scala

> │       │               │   ├── WkHtmlPdf.scala

> │       │               │   └── WkHtmlPdfConfig.scala

> │       │               ├── flexmark

> │       │               │   ├── Markdown.scala

> │       │               │   └── MarkdownConfig.scala

> │       │               ├── Conversion.scala

> │       │               ├── ConversionResult.scala

> │       │               ├── ConvertConfig.scala

> │       │               ├── RemovePdfEncryption.scala

> │       │               └── SanitizeHtml.scala

> │       └── test

> │           └── scala

> │               └── docspell

> │                   └── convert

> │                       ├── extern

> │                       │   └── ExternConvTest.scala

> │                       ├── ConversionTest.scala

> │                       ├── FileChecks.scala

> │                       └── RemovePdfEncryptionTest.scala

> ├── extract

> │   └── src

> │       ├── main

> │       │   ├── java

> │       │   │   └── org

> │       │   │       └── apache

> │       │   │           └── tika

> │       │   │               ├── exception

> │       │   │               │   └── WriteLimitReachedException.java

> │       │   │               ├── parser

> │       │   │               │   ├── odf

> │       │   │               │   │   ├── FlatOpenDocumentMacroHandler.java

> │       │   │               │   │   ├── NSNormalizerContentHandler.java

> │       │   │               │   │   ├── OpenDocumentBodyHandler.java

> │       │   │               │   │   ├── OpenDocumentContentParser.java

> │       │   │               │   │   ├── OpenDocumentMacroHandler.java

> │       │   │               │   │   ├── OpenDocumentManifestHandler.java

> │       │   │               │   │   ├── OpenDocumentMetaParser.java

> │       │   │               │   │   └── OpenDocumentParser.java

> │       │   │               │   └── xml

> │       │   │               │       ├── AbstractMetadataHandler.java

> │       │   │               │       ├── AttributeDependantMetadataHandler.java

> │       │   │               │       ├── AttributeMetadataHandler.java

> │       │   │               │       ├── DcXMLParser.java

> │       │   │               │       ├── ElementMetadataHandler.java

> │       │   │               │       ├── FictionBookParser.java

> │       │   │               │       ├── MetadataHandler.java

> │       │   │               │       ├── TextAndAttributeXMLParser.java

> │       │   │               │       └── XMLParser.java

> │       │   │               └── utils

> │       │   │                   └── StringUtils.java

> │       │   └── scala

> │       │       └── docspell

> │       │           └── extract

> │       │               ├── internal

> │       │               │   └── Text.scala

> │       │               ├── ocr

> │       │               │   ├── Ocr.scala

> │       │               │   ├── OcrConfig.scala

> │       │               │   ├── OcrType.scala

> │       │               │   └── TextExtract.scala

> │       │               ├── odf

> │       │               │   ├── OdfExtract.scala

> │       │               │   └── OdfType.scala

> │       │               ├── pdfbox

> │       │               │   ├── PdfLoader.scala

> │       │               │   ├── PdfMetaData.scala

> │       │               │   ├── PdfboxExtract.scala

> │       │               │   ├── PdfboxPreview.scala

> │       │               │   └── PreviewConfig.scala

> │       │               ├── poi

> │       │               │   ├── PoiExtract.scala

> │       │               │   └── PoiType.scala

> │       │               ├── rtf

> │       │               │   └── RtfExtract.scala

> │       │               ├── ExtractConfig.scala

> │       │               ├── ExtractResult.scala

> │       │               ├── Extraction.scala

> │       │               ├── PdfConfig.scala

> │       │               └── PdfExtract.scala

> │       └── test

> │           └── scala

> │               └── docspell

> │                   └── extract

> │                       ├── ocr

> │                       │   └── TextExtractionSuite.scala

> │                       ├── odf

> │                       │   └── OdfExtractTest.scala

> │                       ├── pdfbox

> │                       │   ├── PdfMetaDataTest.scala

> │                       │   ├── PdfboxExtractTest.scala

> │                       │   └── PdfboxPreviewTest.scala

> │                       ├── poi

> │                       │   └── PoiExtractTest.scala

> │                       └── rtf

> │                           └── RtfExtractTest.scala

> ├── files

> │   └── src

> │       ├── main

> │       │   ├── java

> │       │   │   └── org

> │       │   │       └── apache

> │       │   │           └── tika

> │       │   │               └── parser

> │       │   │                   └── txt

> │       │   │                       ├── IOUtils.java

> │       │   │                       └── Icu4jEncodingDetector.java

> │       │   └── scala

> │       │       └── docspell

> │       │           └── files

> │       │               ├── Dimension.scala

> │       │               ├── FileSupport.scala

> │       │               ├── ImageSize.scala

> │       │               └── TikaMimetype.scala

> │       └── test

> │           ├── resources

> │           │   ├── bombs

> │           │   │   ├── 20K-gray.jpeg

> │           │   │   ├── 20K-gray.png

> │           │   │   ├── 20K-rgb.jpeg

> │           │   │   └── 20K-rgb.png

> │           │   ├── camera

> │           │   │   ├── letter-en.jpg

> │           │   │   ├── letter-en.png

> │           │   │   └── letter-en.tiff

> │           │   ├── examples

> │           │   │   ├── letter-ita.txt

> │           │   │   ├── sample.doc

> │           │   │   ├── sample.docx

> │           │   │   ├── sample.ods

> │           │   │   ├── sample.odt

> │           │   │   ├── sample.rtf

> │           │   │   ├── sample.xls

> │           │   │   └── sample.xlsx

> │           │   ├── scanner

> │           │   │   ├── jfif.jpg

> │           │   │   ├── pdf13.pdf

> │           │   │   └── pdfa14.pdf

> │           │   ├── secured

> │           │   │   ├── encrypted-test123.pdf

> │           │   │   └── protected-test123.pdf

> │           │   ├── keywords.pdf

> │           │   ├── large-file.pdf

> │           │   ├── letter-de.html

> │           │   ├── letter-de.md

> │           │   ├── letter-de.pdf

> │           │   ├── letter-de.txt

> │           │   ├── letter-en.pdf

> │           │   ├── letter-en.txt

> │           │   ├── letters.zip

> │           │   ├── zip-dirs-one.zip

> │           │   └── zip-dirs.zip

> │           └── scala

> │               └── docspell

> │                   └── files

> │                       ├── ExampleFilesSupport.scala

> │                       ├── ImageSizeTest.scala

> │                       ├── Playing.scala

> │                       ├── TestFiles.scala

> │                       ├── TikaMimetypeTest.scala

> │                       └── ZipTest.scala

> ├── fts-client

> │   └── src

> │       └── main

> │           └── scala

> │               └── docspell

> │                   └── ftsclient

> │                       ├── FtsClient.scala

> │                       ├── FtsMigration.scala

> │                       ├── FtsQuery.scala

> │                       ├── FtsResult.scala

> │                       └── TextData.scala

> ├── fts-psql

> │   └── src

> │       ├── main

> │       │   ├── resources

> │       │   │   └── db

> │       │   │       └── psqlfts

> │       │   │           ├── V2.0.0__initial_schema.sql

> │       │   │           └── V2.1.0__collective_id.sql

> │       │   └── scala

> │       │       └── docspell

> │       │           └── ftspsql

> │       │               ├── DbMigration.scala

> │       │               ├── DoobieMeta.scala

> │       │               ├── FtsRecord.scala

> │       │               ├── FtsRepository.scala

> │       │               ├── PgQueryParser.scala

> │       │               ├── PsqlConfig.scala

> │       │               ├── PsqlFtsClient.scala

> │       │               ├── RankNormalization.scala

> │       │               ├── SearchResult.scala

> │       │               └── SearchSummary.scala

> │       └── test

> │           └── scala

> │               └── docspell

> │                   └── ftspsql

> │                       ├── MigrationTest.scala

> │                       ├── PgFixtures.scala

> │                       └── PsqlFtsClientTest.scala

> ├── fts-solr

> │   └── src

> │       └── main

> │           └── scala

> │               └── docspell

> │                   └── ftssolr

> │                       ├── DocIdResult.scala

> │                       ├── Field.scala

> │                       ├── JsonCodec.scala

> │                       ├── QueryData.scala

> │                       ├── SetFields.scala

> │                       ├── SetFolder.scala

> │                       ├── SolrConfig.scala

> │                       ├── SolrFtsClient.scala

> │                       ├── SolrMigration.scala

> │                       ├── SolrQuery.scala

> │                       ├── SolrSetup.scala

> │                       ├── SolrUpdate.scala

> │                       └── VersionDoc.scala

> ├── joex

> │   └── src

> │       ├── main

> │       │   ├── resources

> │       │   │   └── reference.conf

> │       │   └── scala

> │       │       └── docspell

> │       │           └── joex

> │       │               ├── addon

> │       │               │   ├── AddonTaskExtension.scala

> │       │               │   ├── GenericItemAddonTask.scala

> │       │               │   ├── ItemAddonTask.scala

> │       │               │   ├── Result.scala

> │       │               │   └── ScheduledAddonTask.scala

> │       │               ├── analysis

> │       │               │   ├── NerFile.scala

> │       │               │   └── RegexNerFile.scala

> │       │               ├── download

> │       │               │   ├── DownloadZipTask.scala

> │       │               │   └── Result.scala

> │       │               ├── emptytrash

> │       │               │   ├── EmptyTrashTask.scala

> │       │               │   └── Result.scala

> │       │               ├── extract

> │       │               │   └── JsoupSanitizer.scala

> │       │               ├── filecopy

> │       │               │   ├── FileCopyTask.scala

> │       │               │   └── FileIntegrityCheckTask.scala

> │       │               ├── fts

> │       │               │   ├── FtsContext.scala

> │       │               │   ├── FtsWork.scala

> │       │               │   ├── Migration.scala

> │       │               │   ├── MigrationTask.scala

> │       │               │   ├── ReIndexTask.scala

> │       │               │   └── package.scala

> │       │               ├── hk

> │       │               │   ├── CheckNodesTask.scala

> │       │               │   ├── CleanupDownloadsTask.scala

> │       │               │   ├── CleanupInvitesTask.scala

> │       │               │   ├── CleanupJobsTask.scala

> │       │               │   ├── CleanupRememberMeTask.scala

> │       │               │   ├── CleanupResult.scala

> │       │               │   ├── HouseKeepingConfig.scala

> │       │               │   ├── HouseKeepingTask.scala

> │       │               │   └── IntegrityCheckTask.scala

> │       │               ├── learn

> │       │               │   ├── ClassifierName.scala

> │       │               │   ├── Classify.scala

> │       │               │   ├── LearnClassifierTask.scala

> │       │               │   ├── LearnItemEntities.scala

> │       │               │   ├── LearnTags.scala

> │       │               │   ├── SelectItems.scala

> │       │               │   └── StoreClassifierModel.scala

> │       │               ├── mail

> │       │               │   ├── EmilHeader.scala

> │       │               │   └── ReadMail.scala

> │       │               ├── multiupload

> │       │               │   ├── MultiUploadArchiveTask.scala

> │       │               │   └── Result.scala

> │       │               ├── notify

> │       │               │   ├── PeriodicDueItemsTask.scala

> │       │               │   ├── PeriodicQueryTask.scala

> │       │               │   ├── TaskOperations.scala

> │       │               │   └── YamuscaConverter.scala

> │       │               ├── pagecount

> │       │               │   ├── AllPageCountTask.scala

> │       │               │   └── MakePageCountTask.scala

> │       │               ├── pdfconv

> │       │               │   ├── ConvertAllPdfTask.scala

> │       │               │   └── PdfConvTask.scala

> │       │               ├── preview

> │       │               │   ├── AllPreviewsTask.scala

> │       │               │   └── MakePreviewTask.scala

> │       │               ├── process

> │       │               │   ├── AttachmentPageCount.scala

> │       │               │   ├── AttachmentPreview.scala

> │       │               │   ├── ConvertPdf.scala

> │       │               │   ├── CreateItem.scala

> │       │               │   ├── CrossCheckProposals.scala

> │       │               │   ├── DuplicateCheck.scala

> │       │               │   ├── EvalProposals.scala

> │       │               │   ├── ExtractArchive.scala

> │       │               │   ├── FindProposal.scala

> │       │               │   ├── ItemData.scala

> │       │               │   ├── ItemHandler.scala

> │       │               │   ├── LinkProposal.scala

> │       │               │   ├── ProcessItem.scala

> │       │               │   ├── ReProcessItem.scala

> │       │               │   ├── RemoveEmptyItem.scala

> │       │               │   ├── RunAddons.scala

> │       │               │   ├── SaveProposals.scala

> │       │               │   ├── SetGivenData.scala

> │       │               │   ├── TextAnalysis.scala

> │       │               │   └── TextExtraction.scala

> │       │               ├── routes

> │       │               │   ├── InfoRoutes.scala

> │       │               │   ├── InternalHeader.scala

> │       │               │   └── JoexRoutes.scala

> │       │               ├── scanmailbox

> │       │               │   └── ScanMailboxTask.scala

> │       │               ├── updatecheck

> │       │               │   ├── MakeMail.scala

> │       │               │   ├── ThisVersion.scala

> │       │               │   ├── UpdateCheck.scala

> │       │               │   ├── UpdateCheckConfig.scala

> │       │               │   └── UpdateCheckTask.scala

> │       │               ├── Config.scala

> │       │               ├── ConfigFile.scala

> │       │               ├── JoexApp.scala

> │       │               ├── JoexAppImpl.scala

> │       │               ├── JoexServer.scala

> │       │               ├── JoexTasks.scala

> │       │               └── Main.scala

> │       └── test

> │           └── scala

> │               └── docspell

> │                   └── joex

> │                       ├── analysis

> │                       │   └── NerFileTest.scala

> │                       ├── extract

> │                       │   └── JsoupSanitizerTest.scala

> │                       └── updatecheck

> │                           └── UpdateCheckTest.scala

> ├── joexapi

> │   └── src

> │       └── main

> │           ├── resources

> │           │   └── joex-openapi.yml

> │           └── scala

> │               └── docspell

> │                   └── joexapi

> │                       └── client

> │                           └── JoexClient.scala

> ├── jsonminiq

> │   └── src

> │       ├── main

> │       │   └── scala

> │       │       └── docspell

> │       │           └── jsonminiq

> │       │               ├── Format.scala

> │       │               ├── JsonMiniQuery.scala

> │       │               └── Parser.scala

> │       └── test

> │           └── scala

> │               └── docspell

> │                   └── jsonminiq

> │                       ├── Fixtures.scala

> │                       ├── FormatTest.scala

> │                       ├── JsonMiniQueryTest.scala

> │                       └── ParserTest.scala

> ├── logging

> │   ├── api

> │   │   └── src

> │   │       ├── main

> │   │       │   └── scala

> │   │       │       └── docspell

> │   │       │           └── logging

> │   │       │               ├── AndThenLogger.scala

> │   │       │               ├── CapturedLogger.scala

> │   │       │               ├── LazyMap.scala

> │   │       │               ├── Level.scala

> │   │       │               ├── LogConfig.scala

> │   │       │               ├── LogEvent.scala

> │   │       │               ├── Logger.scala

> │   │       │               └── LoggerExtension.scala

> │   │       └── test

> │   │           └── scala

> │   │               └── docspell

> │   │                   └── logging

> │   │                       ├── CapturedLoggerTest.scala

> │   │                       ├── LazyMapTest.scala

> │   │                       └── TestLogger.scala

> │   └── scribe

> │       └── src

> │           ├── main

> │           │   └── scala

> │           │       └── docspell

> │           │           └── logging

> │           │               ├── impl

> │           │               │   ├── JsonWriter.scala

> │           │               │   ├── LogfmtWriter.scala

> │           │               │   ├── Record.scala

> │           │               │   ├── ScribeConfigure.scala

> │           │               │   └── ScribeWrapper.scala

> │           │               └── package.scala

> │           └── test

> │               └── scala

> │                   └── docspell

> │                       └── logging

> │                           └── TestLoggingConfig.scala

> ├── notification

> │   ├── api

> │   │   └── src

> │   │       └── main

> │   │           └── scala

> │   │               └── docspell

> │   │                   └── notification

> │   │                       └── api

> │   │                           ├── Channel.scala

> │   │                           ├── ChannelRef.scala

> │   │                           ├── ChannelType.scala

> │   │                           ├── Event.scala

> │   │                           ├── EventContext.scala

> │   │                           ├── EventExchange.scala

> │   │                           ├── EventMessage.scala

> │   │                           ├── EventReader.scala

> │   │                           ├── EventSink.scala

> │   │                           ├── NotificationBackend.scala

> │   │                           ├── NotificationChannel.scala

> │   │                           ├── NotificationModule.scala

> │   │                           ├── PeriodicDueItemsArgs.scala

> │   │                           └── PeriodicQueryArgs.scala

> │   └── impl

> │       └── src

> │           ├── main

> │           │   └── scala

> │           │       └── docspell

> │           │           └── notification

> │           │               └── impl

> │           │                   ├── context

> │           │                   │   ├── BasicData.scala

> │           │                   │   ├── DeleteFieldValueCtx.scala

> │           │                   │   ├── ItemSelectionCtx.scala

> │           │                   │   ├── JobDoneCtx.scala

> │           │                   │   ├── JobSubmittedCtx.scala

> │           │                   │   ├── SetFieldValueCtx.scala

> │           │                   │   ├── Syntax.scala

> │           │                   │   └── TagsChangedCtx.scala

> │           │                   ├── AbstractEventContext.scala

> │           │                   ├── DbEventContext.scala

> │           │                   ├── EmailBackend.scala

> │           │                   ├── EventContextSyntax.scala

> │           │                   ├── EventNotify.scala

> │           │                   ├── ExampleEventContext.scala

> │           │                   ├── GotifyBackend.scala

> │           │                   ├── HttpPostBackend.scala

> │           │                   ├── HttpSend.scala

> │           │                   ├── Markdown.scala

> │           │                   ├── MatrixBackend.scala

> │           │                   ├── NotificationBackendImpl.scala

> │           │                   └── NotificationModuleImpl.scala

> │           └── test

> │               └── scala

> │                   └── docspell

> │                       └── notification

> │                           └── impl

> │                               └── context

> │                                   └── TagsChangedCtxTest.scala

> ├── oidc

> │   └── src

> │       ├── main

> │       │   └── scala

> │       │       └── docspell

> │       │           └── oidc

> │       │               ├── AccessToken.scala

> │       │               ├── CodeFlow.scala

> │       │               ├── CodeFlowConfig.scala

> │       │               ├── CodeFlowRoutes.scala

> │       │               ├── Jwt.scala

> │       │               ├── OnUserInfo.scala

> │       │               ├── ProviderConfig.scala

> │       │               ├── SignatureAlgo.scala

> │       │               ├── StateParam.scala

> │       │               └── UserInfoDecoder.scala

> │       └── test

> │           └── scala

> │               └── docspell

> │                   └── oidc

> │                       └── StateParamTest.scala

> ├── pubsub

> │   ├── api

> │   │   └── src

> │   │       └── main

> │   │           └── scala

> │   │               └── docspell

> │   │                   └── pubsub

> │   │                       └── api

> │   │                           ├── Message.scala

> │   │                           ├── MessageHead.scala

> │   │                           ├── PubSub.scala

> │   │                           ├── PubSubT.scala

> │   │                           ├── Topic.scala

> │   │                           └── TypedTopic.scala

> │   └── naive

> │       └── src

> │           ├── main

> │           │   └── scala

> │           │       └── docspell

> │           │           └── pubsub

> │           │               └── naive

> │           │                   ├── NaivePubSub.scala

> │           │                   └── PubSubConfig.scala

> │           └── test

> │               └── scala

> │                   └── docspell

> │                       └── pubsub

> │                           └── naive

> │                               ├── Fixtures.scala

> │                               ├── HttpClientOps.scala

> │                               ├── NaivePubSubTest.scala

> │                               └── Topics.scala

> ├── query

> │   ├── js

> │   │   └── src

> │   │       └── main

> │   │           └── scala

> │   │               └── docspell

> │   │                   └── query

> │   │                       └── js

> │   │                           └── JSItemQueryParser.scala

> │   └── shared

> │       └── src

> │           ├── main

> │           │   └── scala

> │           │       └── docspell

> │           │           └── query

> │           │               ├── internal

> │           │               │   ├── AttrParser.scala

> │           │               │   ├── BasicParser.scala

> │           │               │   ├── Constants.scala

> │           │               │   ├── DateParser.scala

> │           │               │   ├── ExprParser.scala

> │           │               │   ├── ExprString.scala

> │           │               │   ├── ExprUtil.scala

> │           │               │   ├── MacroParser.scala

> │           │               │   ├── OperatorParser.scala

> │           │               │   ├── SimpleExprParser.scala

> │           │               │   └── StringUtil.scala

> │           │               ├── Date.scala

> │           │               ├── FulltextExtract.scala

> │           │               ├── ItemQuery.scala

> │           │               ├── ItemQueryDsl.scala

> │           │               ├── ItemQueryParser.scala

> │           │               └── ParseFailure.scala

> │           └── test

> │               └── scala

> │                   └── docspell

> │                       └── query

> │                           ├── internal

> │                           │   ├── AttrParserTest.scala

> │                           │   ├── BasicParserTest.scala

> │                           │   ├── DateParserTest.scala

> │                           │   ├── ExprParserTest.scala

> │                           │   ├── ExprStringTest.scala

> │                           │   ├── ItemQueryParserTest.scala

> │                           │   ├── MacroParserTest.scala

> │                           │   ├── OperatorParserTest.scala

> │                           │   ├── SimpleExprParserTest.scala

> │                           │   └── ValueHelper.scala

> │                           ├── FulltextExtractTest.scala

> │                           └── ItemQueryGen.scala

> ├── restapi

> │   └── src

> │       └── main

> │           ├── resources

> │           │   └── docspell-openapi.yml

> │           └── scala

> │               └── docspell

> │                   └── restapi

> │                       ├── codec

> │                       │   ├── ChannelEihterCodec.scala

> │                       │   └── ItemQueryJson.scala

> │                       └── model

> │                           └── NotificationChannel.scala

> ├── restserver

> │   └── src

> │       ├── main

> │       │   ├── resources

> │       │   │   ├── docspell

> │       │   │   │   └── restserver

> │       │   │   │       └── no-preview.svg

> │       │   │   └── reference.conf

> │       │   ├── scala

> │       │   │   └── docspell

> │       │   │       └── restserver

> │       │   │           ├── auth

> │       │   │           │   ├── CookieData.scala

> │       │   │           │   ├── OpenId.scala

> │       │   │           │   ├── RememberCookieData.scala

> │       │   │           │   └── ShareCookieData.scala

> │       │   │           ├── conv

> │       │   │           │   ├── AddonValidationSupport.scala

> │       │   │           │   ├── Conversions.scala

> │       │   │           │   ├── MultiIdSupport.scala

> │       │   │           │   └── NonEmptyListSupport.scala

> │       │   │           ├── http4s

> │       │   │           │   ├── BinaryUtil.scala

> │       │   │           │   ├── ClientRequestInfo.scala

> │       │   │           │   ├── ContentDisposition.scala

> │       │   │           │   ├── EnvMiddleware.scala

> │       │   │           │   ├── InternalHeader.scala

> │       │   │           │   ├── NoCacheMiddleware.scala

> │       │   │           │   ├── QueryParam.scala

> │       │   │           │   ├── ResponseGenerator.scala

> │       │   │           │   ├── Responses.scala

> │       │   │           │   └── ThrowableResponseMapper.scala

> │       │   │           ├── routes

> │       │   │           │   ├── AddonArchiveRoutes.scala

> │       │   │           │   ├── AddonRoutes.scala

> │       │   │           │   ├── AddonRunConfigRoutes.scala

> │       │   │           │   ├── AddonRunRoutes.scala

> │       │   │           │   ├── AdminAuth.scala

> │       │   │           │   ├── AttachmentMultiRoutes.scala

> │       │   │           │   ├── AttachmentRoutes.scala

> │       │   │           │   ├── Authenticate.scala

> │       │   │           │   ├── BookmarkRoutes.scala

> │       │   │           │   ├── CalEventCheckRoutes.scala

> │       │   │           │   ├── CheckFileRoutes.scala

> │       │   │           │   ├── ClientSettingsRoutes.scala

> │       │   │           │   ├── CollectiveRoutes.scala

> │       │   │           │   ├── CustomFieldRoutes.scala

> │       │   │           │   ├── DownloadAllRoutes.scala

> │       │   │           │   ├── EquipmentRoutes.scala

> │       │   │           │   ├── FileRepositoryRoutes.scala

> │       │   │           │   ├── FolderRoutes.scala

> │       │   │           │   ├── FullTextIndexRoutes.scala

> │       │   │           │   ├── InfoRoutes.scala

> │       │   │           │   ├── IntegrationEndpointRoutes.scala

> │       │   │           │   ├── ItemLinkRoutes.scala

> │       │   │           │   ├── ItemMultiRoutes.scala

> │       │   │           │   ├── ItemRoutes.scala

> │       │   │           │   ├── ItemSearchPart.scala

> │       │   │           │   ├── JobQueueRoutes.scala

> │       │   │           │   ├── LoginRoutes.scala

> │       │   │           │   ├── MailSendRoutes.scala

> │       │   │           │   ├── MailSettingsRoutes.scala

> │       │   │           │   ├── NotificationRoutes.scala

> │       │   │           │   ├── NotifyDueItemsRoutes.scala

> │       │   │           │   ├── OrganizationRoutes.scala

> │       │   │           │   ├── PeriodicQueryRoutes.scala

> │       │   │           │   ├── PersonRoutes.scala

> │       │   │           │   ├── RegisterRoutes.scala

> │       │   │           │   ├── ScanMailboxRoutes.scala

> │       │   │           │   ├── SentMailRoutes.scala

> │       │   │           │   ├── ShareAttachmentRoutes.scala

> │       │   │           │   ├── ShareAuth.scala

> │       │   │           │   ├── ShareItemRoutes.scala

> │       │   │           │   ├── ShareRoutes.scala

> │       │   │           │   ├── ShareSearchRoutes.scala

> │       │   │           │   ├── SourceRoutes.scala

> │       │   │           │   ├── TagRoutes.scala

> │       │   │           │   ├── TotpRoutes.scala

> │       │   │           │   ├── UploadRoutes.scala

> │       │   │           │   └── UserRoutes.scala

> │       │   │           ├── webapp

> │       │   │           │   ├── Flags.scala

> │       │   │           │   ├── TemplateRoutes.scala

> │       │   │           │   ├── Templates.scala

> │       │   │           │   └── WebjarRoutes.scala

> │       │   │           ├── ws

> │       │   │           │   ├── Background.scala

> │       │   │           │   ├── InputMessage.scala

> │       │   │           │   ├── OutputEvent.scala

> │       │   │           │   ├── OutputEventEncoder.scala

> │       │   │           │   └── WebSocketRoutes.scala

> │       │   │           ├── Config.scala

> │       │   │           ├── ConfigFile.scala

> │       │   │           ├── Main.scala

> │       │   │           ├── RestApp.scala

> │       │   │           ├── RestAppImpl.scala

> │       │   │           ├── RestServer.scala

> │       │   │           └── Subscriptions.scala

> │       │   └── templates

> │       │       ├── doc.html

> │       │       ├── index.html

> │       │       └── sw.js

> │       └── test

> │           └── scala

> │               └── docspell

> │                   └── restserver

> │                       └── http4s

> │                           └── ContentDispositionTest.scala

> ├── scheduler

> │   ├── api

> │   │   └── src

> │   │       ├── main

> │   │       │   └── scala

> │   │       │       └── docspell

> │   │       │           └── scheduler

> │   │       │               ├── msg

> │   │       │               │   ├── CancelJob.scala

> │   │       │               │   ├── JobDone.scala

> │   │       │               │   ├── JobSubmitted.scala

> │   │       │               │   ├── JobsNotify.scala

> │   │       │               │   └── PeriodicTaskNotify.scala

> │   │       │               ├── usertask

> │   │       │               │   ├── UserTask.scala

> │   │       │               │   ├── UserTaskScope.scala

> │   │       │               │   └── UserTaskStore.scala

> │   │       │               ├── Context.scala

> │   │       │               ├── CountingScheme.scala

> │   │       │               ├── FindJobOwner.scala

> │   │       │               ├── Job.scala

> │   │       │               ├── JobStore.scala

> │   │       │               ├── JobStoreModule.scala

> │   │       │               ├── JobTask.scala

> │   │       │               ├── JobTaskRegistry.scala

> │   │       │               ├── JobTaskResult.scala

> │   │       │               ├── JobTaskResultEncoder.scala

> │   │       │               ├── PeriodicScheduler.scala

> │   │       │               ├── PeriodicSchedulerConfig.scala

> │   │       │               ├── PermanentError.scala

> │   │       │               ├── Scheduler.scala

> │   │       │               ├── SchedulerConfig.scala

> │   │       │               ├── SchedulerModule.scala

> │   │       │               └── Task.scala

> │   │       └── test

> │   │           └── scala

> │   │               └── docspell

> │   │                   └── scheduler

> │   │                       └── CountingSchemeSpec.scala

> │   └── impl

> │       └── src

> │           ├── main

> │           │   └── scala

> │           │       └── docspell

> │           │           └── scheduler

> │           │               └── impl

> │           │                   ├── ContextImpl.scala

> │           │                   ├── JobQueue.scala

> │           │                   ├── JobStoreImpl.scala

> │           │                   ├── JobStoreModuleBuilder.scala

> │           │                   ├── JobStorePublish.scala

> │           │                   ├── LogEvent.scala

> │           │                   ├── LogSink.scala

> │           │                   ├── Marked.scala

> │           │                   ├── PeriodicSchedulerBuilder.scala

> │           │                   ├── PeriodicSchedulerImpl.scala

> │           │                   ├── PeriodicTaskStore.scala

> │           │                   ├── QJob.scala

> │           │                   ├── QUserTask.scala

> │           │                   ├── QueueLogger.scala

> │           │                   ├── SchedulerBuilder.scala

> │           │                   ├── SchedulerImpl.scala

> │           │                   ├── SchedulerModuleBuilder.scala

> │           │                   └── UserTaskStoreImpl.scala

> │           └── test

> │               └── scala

> │                   └── docspell

> │                       └── scheduler

> │                           └── impl

> │                               └── QJobTest.scala

> ├── store

> │   └── src

> │       ├── main

> │       │   ├── resources

> │       │   │   └── db

> │       │   │       ├── fixups

> │       │   │       │   ├── h2

> │       │   │       │   │   └── V1.33.0__fix_reorganize_files.sql

> │       │   │       │   ├── mariadb

> │       │   │       │   │   └── V1.33.0__fix_reorganize_files.sql

> │       │   │       │   └── postgresql

> │       │   │       │       └── V1.33.0__fix_reorganize_files.sql

> │       │   │       └── migration

> │       │   │           ├── h2

> │       │   │           │   ├── V1.0.0__initial_database.sql

> │       │   │           │   ├── V1.1.0__useremail.sql

> │       │   │           │   ├── V1.10.0__attachment_preview.sql

> │       │   │           │   ├── V1.11.0__pdf_pages.sql

> │       │   │           │   ├── V1.12.0__upload_data.sql

> │       │   │           │   ├── V1.13.0__custom_fields.sql

> │       │   │           │   ├── V1.14.0__person_org.sql

> │       │   │           │   ├── V1.15.0__rememberme.sql

> │       │   │           │   ├── V1.16.0__add_imap_oauth.sql

> │       │   │           │   ├── V1.17.0__meta_language.sql

> │       │   │           │   ├── V1.18.0__classifier_model.sql

> │       │   │           │   ├── V1.19.0__add_classify_meta.sql

> │       │   │           │   ├── V1.19.1__remove_enabled.sql

> │       │   │           │   ├── V1.2.0__origin_source.sql

> │       │   │           │   ├── V1.20.0__personuse.sql

> │       │   │           │   ├── V1.20.1__equipment_description.sql

> │       │   │           │   ├── V1.20.2__org_shortname.sql

> │       │   │           │   ├── V1.20.3__node_seen.sql

> │       │   │           │   ├── V1.20.4__source_lang.sql

> │       │   │           │   ├── V1.21.0__cast_function.sql

> │       │   │           │   ├── V1.21.1__equip_org_use.sql

> │       │   │           │   ├── V1.22.0__add_task_name.sql

> │       │   │           │   ├── V1.23.0__clientsettings.sql

> │       │   │           │   ├── V1.24.0__drop_fts_migration.sql

> │       │   │           │   ├── V1.25.0__add_empty_trash.sql

> │       │   │           │   ├── V1.25.1__fix_periodic_submitter_value.sql

> │       │   │           │   ├── V1.25.2__add_trash_min_age.sql

> │       │   │           │   ├── V1.25.3__delete_corrupt_trash_task.sql

> │       │   │           │   ├── V1.25.4__add_source_attachonly.sql

> │       │   │           │   ├── V1.26.0__missing_indexes.sql

> │       │   │           │   ├── V1.26.1__totp.sql

> │       │   │           │   ├── V1.26.2__openid.sql

> │       │   │           │   ├── V1.26.3__filestore.sql

> │       │   │           │   ├── V1.27.0__collective_passwords.sql

> │       │   │           │   ├── V1.27.1__item_share.sql

> │       │   │           │   ├── V1.28.0__pubsub.sql

> │       │   │           │   ├── V1.28.1__intern_settings.sql

> │       │   │           │   ├── V1.29.0__reset_classifier_file.sql

> │       │   │           │   ├── V1.29.1__notification.sql

> │       │   │           │   ├── V1.3.0__periodic_job.sql

> │       │   │           │   ├── V1.30.0__clientsettings_collective.sql

> │       │   │           │   ├── V1.31.0__query_bookmark.sql

> │       │   │           │   ├── V1.31.1__gotify_prio.sql

> │       │   │           │   ├── V1.32.0__notification_channel_name.sql

> │       │   │           │   ├── V1.32.1__notification_hook_multi_channel.sql

> │       │   │           │   ├── V1.33.0__reorganize_file_ids.sql

> │       │   │           │   ├── V1.34.0__item_relation.sql

> │       │   │           │   ├── V1.35.0__download_query.sql

> │       │   │           │   ├── V1.35.1__password_length.sql

> │       │   │           │   ├── V1.36.0__addons.sql

> │       │   │           │   ├── V1.38.0__more_indexes.sql

> │       │   │           │   ├── V1.38.1__remove_unused_column.sql

> │       │   │           │   ├── V1.38.2__rememberme.sql

> │       │   │           │   ├── V1.39.0__collective_id.sql

> │       │   │           │   ├── V1.39.1__file_meta_migration.sql

> │       │   │           │   ├── V1.39.3__rename_value.sql

> │       │   │           │   ├── V1.4.0__attachment_archive.sql

> │       │   │           │   ├── V1.5.0__userimap.sql

> │       │   │           │   ├── V1.6.0__integration_enabled.sql

> │       │   │           │   ├── V1.7.0__fts-migration.sql

> │       │   │           │   ├── V1.8.0__folders.sql

> │       │   │           │   ├── V1.9.0__updated_column.sql

> │       │   │           │   ├── V1.9.1__classifier.sql

> │       │   │           │   ├── V1.9.3__joblog_counter.sql

> │       │   │           │   └── V1.9.4__unique_equipments.sql

> │       │   │           ├── mariadb

> │       │   │           │   ├── V1.0.0__initial_database.sql

> │       │   │           │   ├── V1.1.0__useremail.sql

> │       │   │           │   ├── V1.10.0__attachment_preview.sql

> │       │   │           │   ├── V1.11.0__pdf_pages.sql

> │       │   │           │   ├── V1.12.0__upload_data.sql

> │       │   │           │   ├── V1.13.0__custom_fields.sql

> │       │   │           │   ├── V1.14.0__person_org.sql

> │       │   │           │   ├── V1.15.0__rememberme.sql

> │       │   │           │   ├── V1.16.0__add_imap_oauth.sql

> │       │   │           │   ├── V1.17.0__meta_language.sql

> │       │   │           │   ├── V1.18.0__classifier_model.sql

> │       │   │           │   ├── V1.19.0__add_classify_meta.sql

> │       │   │           │   ├── V1.19.1__remove_enabled.sql

> │       │   │           │   ├── V1.2.0__origin_source.sql

> │       │   │           │   ├── V1.20.0__personuse.sql

> │       │   │           │   ├── V1.20.1__equipment_description.sql

> │       │   │           │   ├── V1.20.2__org_shortname.sql

> │       │   │           │   ├── V1.20.3__node_seen.sql

> │       │   │           │   ├── V1.20.4__source_lang.sql

> │       │   │           │   ├── V1.21.0__cast_function.sql

> │       │   │           │   ├── V1.21.1__equip_org_use.sql

> │       │   │           │   ├── V1.22.0__add_task_name.sql

> │       │   │           │   ├── V1.23.0__clientsettings.sql

> │       │   │           │   ├── V1.24.0__drop_fts_migration.sql

> │       │   │           │   ├── V1.25.0__add_empty_trash.sql

> │       │   │           │   ├── V1.25.1__fix_periodic_submitter_value.sql

> │       │   │           │   ├── V1.25.2__add_trash_min_age.sql

> │       │   │           │   ├── V1.25.3__delete_corrupt_trash_task.sql

> │       │   │           │   ├── V1.25.4__add_source_attachonly.sql

> │       │   │           │   ├── V1.26.0__missing_indexes.sql

> │       │   │           │   ├── V1.26.1__totp.sql

> │       │   │           │   ├── V1.26.2__openid.sql

> │       │   │           │   ├── V1.26.3__filestore.sql

> │       │   │           │   ├── V1.27.0__collective_passwords.sql

> │       │   │           │   ├── V1.27.1__item_share.sql

> │       │   │           │   ├── V1.28.0__pubsub.sql

> │       │   │           │   ├── V1.28.1__intern_settings.sql

> │       │   │           │   ├── V1.29.0__reset_classifier_file.sql

> │       │   │           │   ├── V1.29.1__notification.sql

> │       │   │           │   ├── V1.3.0__periodic_job.sql

> │       │   │           │   ├── V1.30.0__clientsettings_collective.sql

> │       │   │           │   ├── V1.31.0__query_bookmark.sql

> │       │   │           │   ├── V1.31.1__gotify_prio.sql

> │       │   │           │   ├── V1.32.0__notification_channel_name.sql

> │       │   │           │   ├── V1.32.1__notification_hook_multi_channel.sql

> │       │   │           │   ├── V1.33.0__reorganize_file_ids.sql

> │       │   │           │   ├── V1.34.0__item_relation.sql

> │       │   │           │   ├── V1.35.0__download_query.sql

> │       │   │           │   ├── V1.35.1__password_length.sql

> │       │   │           │   ├── V1.36.0__addons.sql

> │       │   │           │   ├── V1.38.0__more_indexes.sql

> │       │   │           │   ├── V1.38.1__remove_unused_column.sql

> │       │   │           │   ├── V1.38.2__rememberme.sql

> │       │   │           │   ├── V1.39.0__collective_id.sql

> │       │   │           │   ├── V1.39.1__file_meta_migration.sql

> │       │   │           │   ├── V1.39.3__rename_value.sql

> │       │   │           │   ├── V1.4.0__attachment_archive.sql

> │       │   │           │   ├── V1.5.0__userimap.sql

> │       │   │           │   ├── V1.6.0__integration_enabled.sql

> │       │   │           │   ├── V1.6.1__fix_timestamp_columns.sql

> │       │   │           │   ├── V1.7.0__fts-migration.sql

> │       │   │           │   ├── V1.7.1__fix_item_date.sql

> │       │   │           │   ├── V1.8.0__folders.sql

> │       │   │           │   ├── V1.9.0__updated_column.sql

> │       │   │           │   ├── V1.9.1__classifier.sql

> │       │   │           │   ├── V1.9.2__fix_text_length.sql

> │       │   │           │   ├── V1.9.3__joblog_counter.sql

> │       │   │           │   └── V1.9.4__unique_equipments.sql

> │       │   │           └── postgresql

> │       │   │               ├── V1.0.0__initial_database.sql

> │       │   │               ├── V1.1.0__useremail.sql

> │       │   │               ├── V1.10.0__attachment_preview.sql

> │       │   │               ├── V1.11.0__pdf_pages.sql

> │       │   │               ├── V1.12.0__upload_data.sql

> │       │   │               ├── V1.13.0__custom_fields.sql

> │       │   │               ├── V1.14.0__person_org.sql

> │       │   │               ├── V1.15.0__rememberme.sql

> │       │   │               ├── V1.16.0__add_imap_oauth.sql

> │       │   │               ├── V1.17.0__meta_language.sql

> │       │   │               ├── V1.18.0__classifier_model.sql

> │       │   │               ├── V1.19.0__add_classify_meta.sql

> │       │   │               ├── V1.19.1__remove_enabled.sql

> │       │   │               ├── V1.2.0__origin_source.sql

> │       │   │               ├── V1.20.0__personuse.sql

> │       │   │               ├── V1.20.1__equipment_description.sql

> │       │   │               ├── V1.20.2__org_shortname.sql

> │       │   │               ├── V1.20.3__node_seen.sql

> │       │   │               ├── V1.20.4__source_lang.sql

> │       │   │               ├── V1.21.0__cast_function.sql

> │       │   │               ├── V1.21.1__equip_org_use.sql

> │       │   │               ├── V1.22.0__add_task_name.sql

> │       │   │               ├── V1.23.0__clientsettings.sql

> │       │   │               ├── V1.24.0__drop_fts_migration.sql

> │       │   │               ├── V1.25.0__add_empty_trash.sql

> │       │   │               ├── V1.25.1__fix_periodic_submitter_value.sql

> │       │   │               ├── V1.25.2__add_trash_min_age.sql

> │       │   │               ├── V1.25.3__delete_corrupt_trash_task.sql

> │       │   │               ├── V1.25.4__add_source_attachonly.sql

> │       │   │               ├── V1.26.0__missing_indexes.sql

> │       │   │               ├── V1.26.1__totp.sql

> │       │   │               ├── V1.26.2__openid.sql

> │       │   │               ├── V1.26.3__filestore.sql

> │       │   │               ├── V1.27.0__collective_passwords.sql

> │       │   │               ├── V1.27.1__item_share.sql

> │       │   │               ├── V1.28.0__pubsub.sql

> │       │   │               ├── V1.28.1__intern_settings.sql

> │       │   │               ├── V1.29.0__reset_classifier_file.sql

> │       │   │               ├── V1.29.1__notification.sql

> │       │   │               ├── V1.3.0__periodic_job.sql

> │       │   │               ├── V1.30.0__clientsettings_collective.sql

> │       │   │               ├── V1.31.0__query_bookmark.sql

> │       │   │               ├── V1.31.1__gotify_prio.sql

> │       │   │               ├── V1.32.0__notification_channel_name.sql

> │       │   │               ├── V1.32.1__notification_hook_multi_channel.sql

> │       │   │               ├── V1.33.0__reorganize_file_ids.sql

> │       │   │               ├── V1.34.0__item_relation.sql

> │       │   │               ├── V1.35.0__download_query.sql

> │       │   │               ├── V1.35.1__password_length.sql

> │       │   │               ├── V1.36.0__addons.sql

> │       │   │               ├── V1.38.0__more_indexes.sql

> │       │   │               ├── V1.38.1__remove_unused_column.sql

> │       │   │               ├── V1.38.2__rememberme.sql

> │       │   │               ├── V1.39.0__collective_id.sql

> │       │   │               ├── V1.39.1__file_meta_migration.sql

> │       │   │               ├── V1.39.3__rename_value.sql

> │       │   │               ├── V1.4.0__attachment_archive.sql

> │       │   │               ├── V1.5.0__userimap.sql

> │       │   │               ├── V1.6.0__integration_enabled.sql

> │       │   │               ├── V1.7.0__fts-migration.sql

> │       │   │               ├── V1.8.0__folders.sql

> │       │   │               ├── V1.9.0__updated_column.sql

> │       │   │               ├── V1.9.1__classifier.sql

> │       │   │               ├── V1.9.3__joblog_counter.sql

> │       │   │               └── V1.9.4__unique_equipments.sql

> │       │   └── scala

> │       │       ├── db

> │       │       │   └── migration

> │       │       │       ├── common

> │       │       │       │   ├── JsonCodecs.scala

> │       │       │       │   ├── MigrateCollectiveIdTaskArgs.scala

> │       │       │       │   ├── MigrateDueItemTasks.scala

> │       │       │       │   ├── MigrateNotifyTasks.scala

> │       │       │       │   └── TransactorSupport.scala

> │       │       │       ├── data

> │       │       │       │   ├── AllPreviewsArgs.scala

> │       │       │       │   ├── ConvertAllPdfArgs.scala

> │       │       │       │   ├── DownloadZipArgs.scala

> │       │       │       │   ├── EmptyTrashArgs.scala

> │       │       │       │   ├── FileIntegrityCheckArgs.scala

> │       │       │       │   ├── ItemAddonTaskArgs.scala

> │       │       │       │   ├── LearnClassifierArgs.scala

> │       │       │       │   ├── NotifyDueItemsArgs.scala

> │       │       │       │   ├── PeriodicDueItemsArgs.scala

> │       │       │       │   ├── PeriodicDueItemsArgsOld.scala

> │       │       │       │   ├── PeriodicQueryArgs.scala

> │       │       │       │   ├── PeriodicQueryArgsOld.scala

> │       │       │       │   ├── ProcessItemArgs.scala

> │       │       │       │   ├── ReIndexTaskArgs.scala

> │       │       │       │   ├── ScanMailboxArgs.scala

> │       │       │       │   ├── ScheduledAddonTaskArgs.scala

> │       │       │       │   └── package.scala

> │       │       │       ├── h2

> │       │       │       │   ├── V1_29_2__MigrateNotifyTask.scala

> │       │       │       │   ├── V1_32_2__MigrateChannels.scala

> │       │       │       │   └── V1_39_2__MigrateTasks.scala

> │       │       │       ├── mariadb

> │       │       │       │   ├── V1_29_2__MigrateNotifyTask.scala

> │       │       │       │   ├── V1_32_2__MigrateChannels.scala

> │       │       │       │   └── V1_39_2__MigrateTasks.scala

> │       │       │       └── postgresql

> │       │       │           ├── V1_29_2__MigrateNotifyTask.scala

> │       │       │           ├── V1_32_2__MigrateChannels.scala

> │       │       │           └── V1_39_2__MigrateTasks.scala

> │       │       └── docspell

> │       │           └── store

> │       │               ├── file

> │       │               │   ├── AttributeStore.scala

> │       │               │   ├── BinnyUtils.scala

> │       │               │   ├── FileMetadata.scala

> │       │               │   ├── FileRepository.scala

> │       │               │   ├── FileRepositoryConfig.scala

> │       │               │   ├── FileRepositoryImpl.scala

> │       │               │   └── FileUrlReader.scala

> │       │               ├── fts

> │       │               │   ├── ContextEntry.scala

> │       │               │   ├── RFtsResult.scala

> │       │               │   └── TempFtsOps.scala

> │       │               ├── impl

> │       │               │   ├── h2

> │       │               │   │   └── CastNumericFun.scala

> │       │               │   ├── DoobieLogging.scala

> │       │               │   ├── DoobieMeta.scala

> │       │               │   └── StoreImpl.scala

> │       │               ├── migrate

> │       │               │   └── FlywayMigrate.scala

> │       │               ├── qb

> │       │               │   ├── generator

> │       │               │   │   ├── ItemQueryGenerator.scala

> │       │               │   │   └── Tables.scala

> │       │               │   ├── impl

> │       │               │   │   ├── CommonBuilder.scala

> │       │               │   │   ├── ConditionBuilder.scala

> │       │               │   │   ├── DBFunctionBuilder.scala

> │       │               │   │   ├── FromExprBuilder.scala

> │       │               │   │   ├── SelectBuilder.scala

> │       │               │   │   └── SelectExprBuilder.scala

> │       │               │   ├── Batch.scala

> │       │               │   ├── Column.scala

> │       │               │   ├── Condition.scala

> │       │               │   ├── CteBind.scala

> │       │               │   ├── DBFunction.scala

> │       │               │   ├── DML.scala

> │       │               │   ├── DSL.scala

> │       │               │   ├── FromExpr.scala

> │       │               │   ├── GroupBy.scala

> │       │               │   ├── Operator.scala

> │       │               │   ├── OrderBy.scala

> │       │               │   ├── Select.scala

> │       │               │   ├── SelectExpr.scala

> │       │               │   ├── Setter.scala

> │       │               │   └── TableDef.scala

> │       │               ├── queries

> │       │               │   ├── AttachedFile.scala

> │       │               │   ├── AttachmentLight.scala

> │       │               │   ├── CategoryCount.scala

> │       │               │   ├── ChannelMap.scala

> │       │               │   ├── CustomValue.scala

> │       │               │   ├── FieldStats.scala

> │       │               │   ├── FolderCount.scala

> │       │               │   ├── FtsSupport.scala

> │       │               │   ├── IdRefCount.scala

> │       │               │   ├── ItemData.scala

> │       │               │   ├── ItemFieldValue.scala

> │       │               │   ├── ItemFileMeta.scala

> │       │               │   ├── ListItem.scala

> │       │               │   ├── ListItemWithTags.scala

> │       │               │   ├── QAttachment.scala

> │       │               │   ├── QCollective.scala

> │       │               │   ├── QCustomField.scala

> │       │               │   ├── QFolder.scala

> │       │               │   ├── QItem.scala

> │       │               │   ├── QJobQueue.scala

> │       │               │   ├── QLogin.scala

> │       │               │   ├── QMails.scala

> │       │               │   ├── QMoveAttachment.scala

> │       │               │   ├── QNotification.scala

> │       │               │   ├── QOrganization.scala

> │       │               │   ├── QPeriodicTask.scala

> │       │               │   ├── QUser.scala

> │       │               │   ├── Query.scala

> │       │               │   ├── QueryWildcard.scala

> │       │               │   ├── SearchSummary.scala

> │       │               │   ├── SelectedItem.scala

> │       │               │   ├── TagCount.scala

> │       │               │   └── TextAndTag.scala

> │       │               ├── records

> │       │               │   ├── AddonRunConfigData.scala

> │       │               │   ├── AddonRunConfigResolved.scala

> │       │               │   ├── RAddonArchive.scala

> │       │               │   ├── RAddonRunConfig.scala

> │       │               │   ├── RAddonRunConfigAddon.scala

> │       │               │   ├── RAddonRunConfigTrigger.scala

> │       │               │   ├── RAttachment.scala

> │       │               │   ├── RAttachmentArchive.scala

> │       │               │   ├── RAttachmentMeta.scala

> │       │               │   ├── RAttachmentPreview.scala

> │       │               │   ├── RAttachmentSource.scala

> │       │               │   ├── RClassifierModel.scala

> │       │               │   ├── RClassifierSetting.scala

> │       │               │   ├── RClientSettingsCollective.scala

> │       │               │   ├── RClientSettingsUser.scala

> │       │               │   ├── RCollective.scala

> │       │               │   ├── RCollectivePassword.scala

> │       │               │   ├── RContact.scala

> │       │               │   ├── RCustomField.scala

> │       │               │   ├── RCustomFieldValue.scala

> │       │               │   ├── RDownloadQuery.scala

> │       │               │   ├── REmptyTrashSetting.scala

> │       │               │   ├── REquipment.scala

> │       │               │   ├── RFileMeta.scala

> │       │               │   ├── RFolder.scala

> │       │               │   ├── RFolderMember.scala

> │       │               │   ├── RInternalSetting.scala

> │       │               │   ├── RInvitation.scala

> │       │               │   ├── RItem.scala

> │       │               │   ├── RItemLink.scala

> │       │               │   ├── RItemProposal.scala

> │       │               │   ├── RJob.scala

> │       │               │   ├── RJobGroupUse.scala

> │       │               │   ├── RJobLog.scala

> │       │               │   ├── RNode.scala

> │       │               │   ├── RNotificationChannel.scala

> │       │               │   ├── RNotificationChannelGotify.scala

> │       │               │   ├── RNotificationChannelHttp.scala

> │       │               │   ├── RNotificationChannelMail.scala

> │       │               │   ├── RNotificationChannelMatrix.scala

> │       │               │   ├── RNotificationHook.scala

> │       │               │   ├── RNotificationHookChannel.scala

> │       │               │   ├── RNotificationHookEvent.scala

> │       │               │   ├── ROrganization.scala

> │       │               │   ├── RPeriodicTask.scala

> │       │               │   ├── RPerson.scala

> │       │               │   ├── RPubSub.scala

> │       │               │   ├── RQueryBookmark.scala

> │       │               │   ├── RRememberMe.scala

> │       │               │   ├── RSentMail.scala

> │       │               │   ├── RSentMailItem.scala

> │       │               │   ├── RShare.scala

> │       │               │   ├── RSource.scala

> │       │               │   ├── RTag.scala

> │       │               │   ├── RTagItem.scala

> │       │               │   ├── RTagSource.scala

> │       │               │   ├── RTotp.scala

> │       │               │   ├── RUser.scala

> │       │               │   ├── RUserEmail.scala

> │       │               │   ├── RUserImap.scala

> │       │               │   ├── SourceData.scala

> │       │               │   └── TagItemName.scala

> │       │               ├── syntax

> │       │               │   └── MimeTypes.scala

> │       │               ├── AddResult.scala

> │       │               ├── Db.scala

> │       │               ├── JdbcConfig.scala

> │       │               ├── SchemaMigrateConfig.scala

> │       │               ├── Store.scala

> │       │               └── UpdateResult.scala

> │       └── test

> │           ├── resources

> │           │   └── docspell-0.24.0-dump-h2-1.24.0-2021-07-13-2307.sql

> │           └── scala

> │               └── docspell

> │                   └── store

> │                       ├── fts

> │                       │   └── TempFtsOpsTest.scala

> │                       ├── generator

> │                       │   └── ItemQueryGeneratorTest.scala

> │                       ├── migrate

> │                       │   └── MigrateTest.scala

> │                       ├── qb

> │                       │   ├── impl

> │                       │   │   ├── ConditionBuilderTest.scala

> │                       │   │   ├── DSLTest.scala

> │                       │   │   └── SelectBuilderTest.scala

> │                       │   ├── model

> │                       │   │   ├── CourseRecord.scala

> │                       │   │   └── PersonRecord.scala

> │                       │   └── QueryBuilderTest.scala

> │                       ├── queries

> │                       │   └── QueryWildcardTest.scala

> │                       ├── DatabaseTest.scala

> │                       ├── Docker.scala

> │                       └── StoreFixture.scala

> ├── totp

> │   └── src

> │       ├── main

> │       │   └── scala

> │       │       └── docspell

> │       │           └── totp

> │       │               ├── Key.scala

> │       │               ├── Mac.scala

> │       │               ├── OnetimePassword.scala

> │       │               ├── PassLength.scala

> │       │               ├── Settings.scala

> │       │               └── Totp.scala

> │       └── test

> │           └── scala

> │               └── docspell

> │                   └── totp

> │                       ├── KeyTest.scala

> │                       └── TotpTest.scala

> └── webapp

>     ├── src

>     │   └── main

>     │       ├── elm

>     │       │   ├── App

>     │       │   │   ├── Data.elm

>     │       │   │   ├── Update.elm

>     │       │   │   └── View2.elm

>     │       │   ├── Comp

>     │       │   │   ├── ItemDetail

>     │       │   │   │   ├── AddFilesForm.elm

>     │       │   │   │   ├── ConfirmModalView.elm

>     │       │   │   │   ├── EditForm.elm

>     │       │   │   │   ├── FieldTabState.elm

>     │       │   │   │   ├── FormChange.elm

>     │       │   │   │   ├── ItemInfoHeader.elm

>     │       │   │   │   ├── Model.elm

>     │       │   │   │   ├── MultiEditMenu.elm

>     │       │   │   │   ├── Notes.elm

>     │       │   │   │   ├── RunAddonForm.elm

>     │       │   │   │   ├── ShowQrCode.elm

>     │       │   │   │   ├── SingleAttachment.elm

>     │       │   │   │   ├── Update.elm

>     │       │   │   │   └── View2.elm

>     │       │   │   ├── AddonArchiveForm.elm

>     │       │   │   ├── AddonArchiveManage.elm

>     │       │   │   ├── AddonArchiveTable.elm

>     │       │   │   ├── AddonRunConfigForm.elm

>     │       │   │   ├── AddonRunConfigManage.elm

>     │       │   │   ├── AddonRunConfigTable.elm

>     │       │   │   ├── AddressForm.elm

>     │       │   │   ├── AttachmentMeta.elm

>     │       │   │   ├── Basic.elm

>     │       │   │   ├── BasicSizeField.elm

>     │       │   │   ├── BookmarkChooser.elm

>     │       │   │   ├── BookmarkDropdown.elm

>     │       │   │   ├── BookmarkManage.elm

>     │       │   │   ├── BookmarkQueryForm.elm

>     │       │   │   ├── BookmarkQueryManage.elm

>     │       │   │   ├── BookmarkTable.elm

>     │       │   │   ├── BoxEdit.elm

>     │       │   │   ├── BoxMessageEdit.elm

>     │       │   │   ├── BoxQueryEdit.elm

>     │       │   │   ├── BoxQueryView.elm

>     │       │   │   ├── BoxSearchQueryInput.elm

>     │       │   │   ├── BoxStatsEdit.elm

>     │       │   │   ├── BoxStatsView.elm

>     │       │   │   ├── BoxUploadEdit.elm

>     │       │   │   ├── BoxUploadView.elm

>     │       │   │   ├── BoxView.elm

>     │       │   │   ├── CalEventInput.elm

>     │       │   │   ├── ChangePasswordForm.elm

>     │       │   │   ├── ChannelForm.elm

>     │       │   │   ├── ChannelMenu.elm

>     │       │   │   ├── ChannelRefInput.elm

>     │       │   │   ├── ClassifierSettingsForm.elm

>     │       │   │   ├── CollectiveSettingsForm.elm

>     │       │   │   ├── ColorTagger.elm

>     │       │   │   ├── ConfirmModal.elm

>     │       │   │   ├── ContactField.elm

>     │       │   │   ├── CustomFieldForm.elm

>     │       │   │   ├── CustomFieldInput.elm

>     │       │   │   ├── CustomFieldManage.elm

>     │       │   │   ├── CustomFieldMultiInput.elm

>     │       │   │   ├── CustomFieldTable.elm

>     │       │   │   ├── DashboardEdit.elm

>     │       │   │   ├── DashboardManage.elm

>     │       │   │   ├── DashboardView.elm

>     │       │   │   ├── DatePicker.elm

>     │       │   │   ├── DetailEdit.elm

>     │       │   │   ├── DownloadAll.elm

>     │       │   │   ├── Dropdown.elm

>     │       │   │   ├── Dropzone.elm

>     │       │   │   ├── DueItemsTaskForm.elm

>     │       │   │   ├── DueItemsTaskList.elm

>     │       │   │   ├── DueItemsTaskManage.elm

>     │       │   │   ├── EmailInput.elm

>     │       │   │   ├── EmailSettingsForm.elm

>     │       │   │   ├── EmailSettingsManage.elm

>     │       │   │   ├── EmailSettingsTable.elm

>     │       │   │   ├── EmptyTrashForm.elm

>     │       │   │   ├── EquipmentForm.elm

>     │       │   │   ├── EquipmentManage.elm

>     │       │   │   ├── EquipmentTable.elm

>     │       │   │   ├── EventSample.elm

>     │       │   │   ├── ExpandCollapse.elm

>     │       │   │   ├── FieldListSelect.elm

>     │       │   │   ├── FixedDropdown.elm

>     │       │   │   ├── FolderDetail.elm

>     │       │   │   ├── FolderManage.elm

>     │       │   │   ├── FolderSelect.elm

>     │       │   │   ├── FolderTable.elm

>     │       │   │   ├── ImapSettingsForm.elm

>     │       │   │   ├── ImapSettingsManage.elm

>     │       │   │   ├── ImapSettingsTable.elm

>     │       │   │   ├── IntField.elm

>     │       │   │   ├── ItemCard.elm

>     │       │   │   ├── ItemCardList.elm

>     │       │   │   ├── ItemColumnDropdown.elm

>     │       │   │   ├── ItemColumnView.elm

>     │       │   │   ├── ItemDetail.elm

>     │       │   │   ├── ItemLinkForm.elm

>     │       │   │   ├── ItemMail.elm

>     │       │   │   ├── ItemMerge.elm

>     │       │   │   ├── ItemSearchInput.elm

>     │       │   │   ├── KeyInput.elm

>     │       │   │   ├── LinkTarget.elm

>     │       │   │   ├── MarkdownInput.elm

>     │       │   │   ├── MenuBar.elm

>     │       │   │   ├── NotificationChannelManage.elm

>     │       │   │   ├── NotificationChannelTable.elm

>     │       │   │   ├── NotificationGotifyForm.elm

>     │       │   │   ├── NotificationHookForm.elm

>     │       │   │   ├── NotificationHookManage.elm

>     │       │   │   ├── NotificationHookTable.elm

>     │       │   │   ├── NotificationHttpForm.elm

>     │       │   │   ├── NotificationMailForm.elm

>     │       │   │   ├── NotificationMatrixForm.elm

>     │       │   │   ├── NotificationTest.elm

>     │       │   │   ├── OrgForm.elm

>     │       │   │   ├── OrgManage.elm

>     │       │   │   ├── OrgTable.elm

>     │       │   │   ├── OtpSetup.elm

>     │       │   │   ├── PasswordInput.elm

>     │       │   │   ├── PeriodicQueryTaskForm.elm

>     │       │   │   ├── PeriodicQueryTaskList.elm

>     │       │   │   ├── PeriodicQueryTaskManage.elm

>     │       │   │   ├── PersonForm.elm

>     │       │   │   ├── PersonManage.elm

>     │       │   │   ├── PersonTable.elm

>     │       │   │   ├── PowerSearchInput.elm

>     │       │   │   ├── Progress.elm

>     │       │   │   ├── PublishItems.elm

>     │       │   │   ├── ScanMailboxForm.elm

>     │       │   │   ├── ScanMailboxList.elm

>     │       │   │   ├── ScanMailboxManage.elm

>     │       │   │   ├── SearchMenu.elm

>     │       │   │   ├── SearchStatsView.elm

>     │       │   │   ├── SentMails.elm

>     │       │   │   ├── ShareForm.elm

>     │       │   │   ├── ShareMail.elm

>     │       │   │   ├── ShareManage.elm

>     │       │   │   ├── SharePasswordForm.elm

>     │       │   │   ├── ShareTable.elm

>     │       │   │   ├── ShareView.elm

>     │       │   │   ├── SimpleTextInput.elm

>     │       │   │   ├── SourceForm.elm

>     │       │   │   ├── SourceManage.elm

>     │       │   │   ├── SourceTable.elm

>     │       │   │   ├── StringListInput.elm

>     │       │   │   ├── Tabs.elm

>     │       │   │   ├── TagDropdown.elm

>     │       │   │   ├── TagForm.elm

>     │       │   │   ├── TagManage.elm

>     │       │   │   ├── TagSelect.elm

>     │       │   │   ├── TagTable.elm

>     │       │   │   ├── UiSettingsForm.elm

>     │       │   │   ├── UiSettingsManage.elm

>     │       │   │   ├── UiSettingsMigrate.elm

>     │       │   │   ├── UploadForm.elm

>     │       │   │   ├── UrlCopy.elm

>     │       │   │   ├── UserForm.elm

>     │       │   │   ├── UserManage.elm

>     │       │   │   ├── UserTable.elm

>     │       │   │   └── YesNoDimmer.elm

>     │       │   ├── Data

>     │       │   │   ├── AccountScope.elm

>     │       │   │   ├── AddonTrigger.elm

>     │       │   │   ├── AppEvent.elm

>     │       │   │   ├── BasicSize.elm

>     │       │   │   ├── Bookmarks.elm

>     │       │   │   ├── Box.elm

>     │       │   │   ├── BoxContent.elm

>     │       │   │   ├── CalEvent.elm

>     │       │   │   ├── ChannelRef.elm

>     │       │   │   ├── ChannelType.elm

>     │       │   │   ├── Color.elm

>     │       │   │   ├── ContactType.elm

>     │       │   │   ├── CustomFieldChange.elm

>     │       │   │   ├── CustomFieldOrder.elm

>     │       │   │   ├── CustomFieldType.elm

>     │       │   │   ├── Dashboard.elm

>     │       │   │   ├── Dashboards.elm

>     │       │   │   ├── Direction.elm

>     │       │   │   ├── DownloadAllState.elm

>     │       │   │   ├── DownloadFileType.elm

>     │       │   │   ├── DropdownStyle.elm

>     │       │   │   ├── Environment.elm

>     │       │   │   ├── EquipmentOrder.elm

>     │       │   │   ├── EquipmentUse.elm

>     │       │   │   ├── EventType.elm

>     │       │   │   ├── Fields.elm

>     │       │   │   ├── Flags.elm

>     │       │   │   ├── FolderOrder.elm

>     │       │   │   ├── Icons.elm

>     │       │   │   ├── ItemArrange.elm

>     │       │   │   ├── ItemColumn.elm

>     │       │   │   ├── ItemIds.elm

>     │       │   │   ├── ItemNav.elm

>     │       │   │   ├── ItemQuery.elm

>     │       │   │   ├── ItemSelection.elm

>     │       │   │   ├── ItemTemplate.elm

>     │       │   │   ├── Items.elm

>     │       │   │   ├── Language.elm

>     │       │   │   ├── ListType.elm

>     │       │   │   ├── Money.elm

>     │       │   │   ├── NotificationChannel.elm

>     │       │   │   ├── OrgUse.elm

>     │       │   │   ├── OrganizationOrder.elm

>     │       │   │   ├── Pdf.elm

>     │       │   │   ├── PersonOrder.elm

>     │       │   │   ├── PersonUse.elm

>     │       │   │   ├── Priority.elm

>     │       │   │   ├── QueryParseResult.elm

>     │       │   │   ├── SSLType.elm

>     │       │   │   ├── SearchMode.elm

>     │       │   │   ├── ServerEvent.elm

>     │       │   │   ├── SourceState.elm

>     │       │   │   ├── TagOrder.elm

>     │       │   │   ├── TimeZone.elm

>     │       │   │   ├── UiSettings.elm

>     │       │   │   ├── UiTheme.elm

>     │       │   │   ├── UserState.elm

>     │       │   │   └── Validated.elm

>     │       │   ├── Messages

>     │       │   │   ├── Comp

>     │       │   │   │   ├── ItemDetail

>     │       │   │   │   │   ├── AddFilesForm.elm

>     │       │   │   │   │   ├── ConfirmModal.elm

>     │       │   │   │   │   ├── EditForm.elm

>     │       │   │   │   │   ├── ItemInfoHeader.elm

>     │       │   │   │   │   ├── MultiEditMenu.elm

>     │       │   │   │   │   ├── Notes.elm

>     │       │   │   │   │   ├── RunAddonForm.elm

>     │       │   │   │   │   └── SingleAttachment.elm

>     │       │   │   │   ├── AddonArchiveForm.elm

>     │       │   │   │   ├── AddonArchiveManage.elm

>     │       │   │   │   ├── AddonArchiveTable.elm

>     │       │   │   │   ├── AddonRunConfigForm.elm

>     │       │   │   │   ├── AddonRunConfigManage.elm

>     │       │   │   │   ├── AddonRunConfigTable.elm

>     │       │   │   │   ├── AddressForm.elm

>     │       │   │   │   ├── AttachmentMeta.elm

>     │       │   │   │   ├── BookmarkChooser.elm

>     │       │   │   │   ├── BookmarkDropdown.elm

>     │       │   │   │   ├── BookmarkManage.elm

>     │       │   │   │   ├── BookmarkQueryForm.elm

>     │       │   │   │   ├── BookmarkQueryManage.elm

>     │       │   │   │   ├── BookmarkTable.elm

>     │       │   │   │   ├── BoxEdit.elm

>     │       │   │   │   ├── BoxMessageEdit.elm

>     │       │   │   │   ├── BoxQueryEdit.elm

>     │       │   │   │   ├── BoxQueryView.elm

>     │       │   │   │   ├── BoxSearchQueryInput.elm

>     │       │   │   │   ├── BoxStatsEdit.elm

>     │       │   │   │   ├── BoxStatsView.elm

>     │       │   │   │   ├── BoxUploadEdit.elm

>     │       │   │   │   ├── BoxUploadView.elm

>     │       │   │   │   ├── BoxView.elm

>     │       │   │   │   ├── CalEventInput.elm

>     │       │   │   │   ├── ChangePasswordForm.elm

>     │       │   │   │   ├── ChannelForm.elm

>     │       │   │   │   ├── ChannelRefInput.elm

>     │       │   │   │   ├── ClassifierSettingsForm.elm

>     │       │   │   │   ├── CollectiveSettingsForm.elm

>     │       │   │   │   ├── CustomFieldForm.elm

>     │       │   │   │   ├── CustomFieldInput.elm

>     │       │   │   │   ├── CustomFieldManage.elm

>     │       │   │   │   ├── CustomFieldMultiInput.elm

>     │       │   │   │   ├── CustomFieldTable.elm

>     │       │   │   │   ├── DashboardEdit.elm

>     │       │   │   │   ├── DashboardManage.elm

>     │       │   │   │   ├── DashboardView.elm

>     │       │   │   │   ├── DetailEdit.elm

>     │       │   │   │   ├── DownloadAll.elm

>     │       │   │   │   ├── Dropzone.elm

>     │       │   │   │   ├── DueItemsTaskForm.elm

>     │       │   │   │   ├── DueItemsTaskList.elm

>     │       │   │   │   ├── DueItemsTaskManage.elm

>     │       │   │   │   ├── EmailSettingsForm.elm

>     │       │   │   │   ├── EmailSettingsManage.elm

>     │       │   │   │   ├── EmailSettingsTable.elm

>     │       │   │   │   ├── EmptyTrashForm.elm

>     │       │   │   │   ├── EquipmentForm.elm

>     │       │   │   │   ├── EquipmentManage.elm

>     │       │   │   │   ├── EquipmentTable.elm

>     │       │   │   │   ├── EventSample.elm

>     │       │   │   │   ├── ExpandCollapse.elm

>     │       │   │   │   ├── FolderDetail.elm

>     │       │   │   │   ├── FolderManage.elm

>     │       │   │   │   ├── FolderSelect.elm

>     │       │   │   │   ├── FolderTable.elm

>     │       │   │   │   ├── HttpError.elm

>     │       │   │   │   ├── ImapSettingsForm.elm

>     │       │   │   │   ├── ImapSettingsManage.elm

>     │       │   │   │   ├── ImapSettingsTable.elm

>     │       │   │   │   ├── ItemCard.elm

>     │       │   │   │   ├── ItemCardList.elm

>     │       │   │   │   ├── ItemColumnDropdown.elm

>     │       │   │   │   ├── ItemDetail.elm

>     │       │   │   │   ├── ItemLinkForm.elm

>     │       │   │   │   ├── ItemMail.elm

>     │       │   │   │   ├── ItemMerge.elm

>     │       │   │   │   ├── ItemSearchInput.elm

>     │       │   │   │   ├── NotificationChannelManage.elm

>     │       │   │   │   ├── NotificationChannelTable.elm

>     │       │   │   │   ├── NotificationGotifyForm.elm

>     │       │   │   │   ├── NotificationHookForm.elm

>     │       │   │   │   ├── NotificationHookManage.elm

>     │       │   │   │   ├── NotificationHookTable.elm

>     │       │   │   │   ├── NotificationHttpForm.elm

>     │       │   │   │   ├── NotificationMailForm.elm

>     │       │   │   │   ├── NotificationMatrixForm.elm

>     │       │   │   │   ├── OrgForm.elm

>     │       │   │   │   ├── OrgManage.elm

>     │       │   │   │   ├── OrgTable.elm

>     │       │   │   │   ├── OtpSetup.elm

>     │       │   │   │   ├── PeriodicQueryTaskForm.elm

>     │       │   │   │   ├── PeriodicQueryTaskList.elm

>     │       │   │   │   ├── PeriodicQueryTaskManage.elm

>     │       │   │   │   ├── PersonForm.elm

>     │       │   │   │   ├── PersonManage.elm

>     │       │   │   │   ├── PersonTable.elm

>     │       │   │   │   ├── PublishItems.elm

>     │       │   │   │   ├── ScanMailboxForm.elm

>     │       │   │   │   ├── ScanMailboxManage.elm

>     │       │   │   │   ├── ScanMailboxTable.elm

>     │       │   │   │   ├── SearchMenu.elm

>     │       │   │   │   ├── SearchStatsView.elm

>     │       │   │   │   ├── SentMails.elm

>     │       │   │   │   ├── ShareForm.elm

>     │       │   │   │   ├── ShareMail.elm

>     │       │   │   │   ├── ShareManage.elm

>     │       │   │   │   ├── SharePasswordForm.elm

>     │       │   │   │   ├── ShareTable.elm

>     │       │   │   │   ├── ShareView.elm

>     │       │   │   │   ├── SourceForm.elm

>     │       │   │   │   ├── SourceManage.elm

>     │       │   │   │   ├── SourceTable.elm

>     │       │   │   │   ├── TagDropdown.elm

>     │       │   │   │   ├── TagForm.elm

>     │       │   │   │   ├── TagManage.elm

>     │       │   │   │   ├── TagSelect.elm

>     │       │   │   │   ├── TagTable.elm

>     │       │   │   │   ├── UiSettingsForm.elm

>     │       │   │   │   ├── UiSettingsManage.elm

>     │       │   │   │   ├── UploadForm.elm

>     │       │   │   │   ├── UserForm.elm

>     │       │   │   │   ├── UserManage.elm

>     │       │   │   │   └── UserTable.elm

>     │       │   │   ├── Data

>     │       │   │   │   ├── AccountScope.elm

>     │       │   │   │   ├── BoxContent.elm

>     │       │   │   │   ├── ChannelType.elm

>     │       │   │   │   ├── Color.elm

>     │       │   │   │   ├── ContactType.elm

>     │       │   │   │   ├── CustomFieldType.elm

>     │       │   │   │   ├── Direction.elm

>     │       │   │   │   ├── DownloadFileType.elm

>     │       │   │   │   ├── EquipmentUse.elm

>     │       │   │   │   ├── EventType.elm

>     │       │   │   │   ├── Fields.elm

>     │       │   │   │   ├── ItemColumn.elm

>     │       │   │   │   ├── Language.elm

>     │       │   │   │   ├── OrgUse.elm

>     │       │   │   │   ├── PdfMode.elm

>     │       │   │   │   ├── PersonUse.elm

>     │       │   │   │   └── SSLType.elm

>     │       │   │   ├── Page

>     │       │   │   │   ├── CollectiveSettings.elm

>     │       │   │   │   ├── Dashboard.elm

>     │       │   │   │   ├── DefaultDashboard.elm

>     │       │   │   │   ├── ItemDetail.elm

>     │       │   │   │   ├── Login.elm

>     │       │   │   │   ├── ManageData.elm

>     │       │   │   │   ├── NewInvite.elm

>     │       │   │   │   ├── Queue.elm

>     │       │   │   │   ├── Register.elm

>     │       │   │   │   ├── Search.elm

>     │       │   │   │   ├── SearchSideMenu.elm

>     │       │   │   │   ├── Share.elm

>     │       │   │   │   ├── ShareDetail.elm

>     │       │   │   │   ├── Upload.elm

>     │       │   │   │   └── UserSettings.elm

>     │       │   │   ├── App.elm

>     │       │   │   ├── Basics.elm

>     │       │   │   ├── DateFormat.elm

>     │       │   │   └── UiLanguage.elm

>     │       │   ├── Page

>     │       │   │   ├── CollectiveSettings

>     │       │   │   │   ├── Data.elm

>     │       │   │   │   ├── Update.elm

>     │       │   │   │   └── View2.elm

>     │       │   │   ├── Dashboard

>     │       │   │   │   ├── Data.elm

>     │       │   │   │   ├── DefaultDashboard.elm

>     │       │   │   │   ├── SideMenu.elm

>     │       │   │   │   ├── Update.elm

>     │       │   │   │   └── View.elm

>     │       │   │   ├── ItemDetail

>     │       │   │   │   ├── Data.elm

>     │       │   │   │   ├── Update.elm

>     │       │   │   │   └── View2.elm

>     │       │   │   ├── Login

>     │       │   │   │   ├── Data.elm

>     │       │   │   │   ├── Update.elm

>     │       │   │   │   └── View2.elm

>     │       │   │   ├── ManageData

>     │       │   │   │   ├── Data.elm

>     │       │   │   │   ├── Update.elm

>     │       │   │   │   └── View2.elm

>     │       │   │   ├── NewInvite

>     │       │   │   │   ├── Data.elm

>     │       │   │   │   ├── Update.elm

>     │       │   │   │   └── View2.elm

>     │       │   │   ├── Queue

>     │       │   │   │   ├── Data.elm

>     │       │   │   │   ├── Update.elm

>     │       │   │   │   └── View2.elm

>     │       │   │   ├── Register

>     │       │   │   │   ├── Data.elm

>     │       │   │   │   ├── Update.elm

>     │       │   │   │   └── View2.elm

>     │       │   │   ├── Search

>     │       │   │   │   ├── Data.elm

>     │       │   │   │   ├── SideMenu.elm

>     │       │   │   │   ├── Update.elm

>     │       │   │   │   └── View2.elm

>     │       │   │   ├── Share

>     │       │   │   │   ├── Data.elm

>     │       │   │   │   ├── LoadMore.elm

>     │       │   │   │   ├── Menubar.elm

>     │       │   │   │   ├── Results.elm

>     │       │   │   │   ├── Sidebar.elm

>     │       │   │   │   ├── TopContent.elm

>     │       │   │   │   ├── Update.elm

>     │       │   │   │   └── View.elm

>     │       │   │   ├── ShareDetail

>     │       │   │   │   ├── Data.elm

>     │       │   │   │   ├── Update.elm

>     │       │   │   │   └── View.elm

>     │       │   │   ├── Upload

>     │       │   │   │   ├── Data.elm

>     │       │   │   │   ├── Update.elm

>     │       │   │   │   └── View2.elm

>     │       │   │   └── UserSettings

>     │       │   │       ├── Data.elm

>     │       │   │       ├── Update.elm

>     │       │   │       └── View2.elm

>     │       │   ├── Util

>     │       │   │   ├── Address.elm

>     │       │   │   ├── Contact.elm

>     │       │   │   ├── CustomField.elm

>     │       │   │   ├── Duration.elm

>     │       │   │   ├── File.elm

>     │       │   │   ├── Folder.elm

>     │       │   │   ├── Html.elm

>     │       │   │   ├── Http.elm

>     │       │   │   ├── Item.elm

>     │       │   │   ├── ItemDragDrop.elm

>     │       │   │   ├── List.elm

>     │       │   │   ├── Maybe.elm

>     │       │   │   ├── Person.elm

>     │       │   │   ├── Result.elm

>     │       │   │   ├── Size.elm

>     │       │   │   ├── String.elm

>     │       │   │   ├── Tag.elm

>     │       │   │   └── Update.elm

>     │       │   ├── Api.elm

>     │       │   ├── Main.elm

>     │       │   ├── Messages.elm

>     │       │   ├── Page.elm

>     │       │   ├── Ports.elm

>     │       │   └── Styles.elm

>     │       ├── styles

>     │       │   ├── custom-components.css

>     │       │   ├── custom-utilities.css

>     │       │   ├── index.css

>     │       │   └── keep.txt

>     │       └── webjar

>     │           ├── favicon

>     │           │   ├── android-icon-144x144.png

>     │           │   ├── android-icon-192x192.png

>     │           │   ├── android-icon-36x36.png

>     │           │   ├── android-icon-48x48.png

>     │           │   ├── android-icon-512x512.png

>     │           │   ├── android-icon-72x72.png

>     │           │   ├── android-icon-96x96.png

>     │           │   ├── apple-icon-114x114.png

>     │           │   ├── apple-icon-120x120.png

>     │           │   ├── apple-icon-144x144.png

>     │           │   ├── apple-icon-152x152.png

>     │           │   ├── apple-icon-180x180.png

>     │           │   ├── apple-icon-57x57.png

>     │           │   ├── apple-icon-60x60.png

>     │           │   ├── apple-icon-72x72.png

>     │           │   ├── apple-icon-76x76.png

>     │           │   ├── apple-icon-precomposed.png

>     │           │   ├── apple-icon.png

>     │           │   ├── browserconfig.xml

>     │           │   ├── favicon-16x16.png

>     │           │   ├── favicon-32x32.png

>     │           │   ├── favicon-96x96.png

>     │           │   ├── favicon.ico

>     │           │   ├── manifest.json

>     │           │   ├── ms-icon-144x144.png

>     │           │   ├── ms-icon-150x150.png

>     │           │   ├── ms-icon-310x310.png

>     │           │   └── ms-icon-70x70.png

>     │           ├── img

>     │           │   ├── logo-400.png

>     │           │   ├── logo-96.png

>     │           │   ├── logo-mc-400.png

>     │           │   ├── logo-mc-96.png

>     │           │   ├── logo-only-mc.svg

>     │           │   └── logo-only.svg

>     │           ├── docspell.css

>     │           └── docspell.js

>     ├── elm-analyse.json

>     ├── elm-package.json

>     ├── elm.json

>     ├── package-lock.json

>     ├── package.json

>     ├── postcss.config.js

>     └── tailwind.config.js

> ```

> 

> ---

> *Generated by FileTree Pro Extension*

### Assistant
> Yes. There’s a ton in there worth stealing—but not the way you think. You’re not stealing “Postgres.” You’re stealing **patterns**: storage keys, integrity checks, dedup logic, query DSL, and job orchestration boundaries.
> 
> Here’s what in `modules/` is most useful for building a QiDocSpell module on Supabase + optional Cloudflare/R2/Drive.
> 
> ## Highest-value targets (read these first)
> 
> ### 1) `store/` — migrations + core data model (the real gold)
> **Why:** This is where their *actual schema evolution* lives. You can lift table concepts, relationships, indexing strategy, and how they represent “items vs attachments vs metadata vs proposals vs jobs”.
> 
> Read:
> - `modules/store/src/main/resources/db/migration/postgresql/V1.0.0__initial_database.sql`
> - `V1.13.0__custom_fields.sql`
> - `V1.10.0__attachment_preview.sql` (previews/derivatives)
> - `V1.11.0__pdf_pages.sql` (page counts)
> - `V1.33.0__reorganize_file_ids.sql` and `fixups/*reorganize_files.sql` (how they corrected storage keys over time)
> - `V1.34.0__item_relation.sql` (linking items—this is your “Zotero-ish crosslink”)
> - `V1.7.0__fts-migration.sql` + anything FTS related (how they model searchable extracted text)
> 
> **What you extract for QiVault:**
> - table shapes you’ll reimplement in Supabase
> - constraints and indexes
> - how they model “derived artifacts” (preview, extracted text, etc.)
> - how they keep integrity and avoid overwrite/reorg bugs
> 
> ### 2) `common/` — file key + hash + integrity primitives (steal these ideas)
> **Why:** This folder contains the concepts you want to replicate: `FileKey`, `Hash`, `FileIntegrityCheckArgs`, `FileStoreConfig`, etc. It tells you how they think about immutability and verification.
> 
> Look at:
> - `modules/common/.../FileKey.scala`
> - `FileStoreConfig.scala`, `FileStoreType.scala`
> - `Hash.scala`
> - `FileIntegrityCheckArgs.scala`
> 
> **Translate to QiOne:**
> - `blob_key` format in DB
> - `sha256`, `bytes`, `mime`, `created_at` required on insert
> - nightly integrity verification job (later)
> 
> ### 3) `joex/` — the processing pipeline state machine (copy the workflow)
> You already have a pipeline, but Docspell’s job tree shows a clean separation of concerns and *where to persist state*.
> 
> Read:
> - `modules/joex/.../process/ProcessItem.scala` + `ItemHandler.scala`
> - `DuplicateCheck.scala` (dedup logic)
> - `TextExtraction.scala`, `TextAnalysis.scala`
> - `preview/*` and `pagecount/*`
> - `filecopy/FileIntegrityCheckTask.scala`
> - `hk/IntegrityCheckTask.scala` (housekeeping)
> 
> **What you take:**
> - job statuses + transitions
> - when to generate thumbnails/previews/pagecount
> - dedup candidate generation
> 
> ### 4) `fts-psql/` — Postgres FTS implementation details
> This is perfect because you’re on Supabase Postgres.
> 
> Read:
> - `modules/fts-psql/src/main/resources/db/psqlfts/V2.0.0__initial_schema.sql`
> - `PsqlFtsClient.scala`, `PgQueryParser.scala`
> 
> **What you take:**
> - how they normalize text into searchable records
> - ranking strategy (optional)
> - schema: one row per doc? per attachment? per page? etc.
> 
> ### 5) `query/` — their query DSL (optional but powerful)
> This is how they avoid “Notion filters” and instead have a compact query language. If you want “rigid but powerful search,” this is it.
> 
> Read:
> - `modules/query/shared/.../ItemQueryDsl.scala`
> - `ItemQueryParser.scala`
> 
> **QiOne translation:**
> - you can implement a simplified query syntax in TS
> - convert into SQL where clauses + FTS query
> 
> ---
> 
> ## “Maybe later” but still useful
> 
> ### `restapi/` and `restserver/`
> The OpenAPI specs are valuable as a blueprint for your own endpoints even if you never run their server.
> 
> Read:
> - `modules/restapi/src/main/resources/docspell-openapi.yml`
> - `modules/joexapi/src/main/resources/joex-openapi.yml`
> 
> ### `convert/` + `extract/` + `files/`
> If your ingestion pipeline needs to expand beyond PDFs, these show the conversion/extraction matrix and what tools they relied on (tesseract, unoconv, pdfbox, tika). But you said you’d rather script that—so use these as a checklist, not code to copy.
> 
> ---
> 
> ## What’s NOT worth your time (for QiDocSpell)
> - `webapp/` (it’s Elm; you’re not adopting that UI stack)
> - `oidc/`, `totp/` (auth concerns—Supabase already handles)
> - `notification/` (nice but not core)
> - `pubsub/` (unless you want eventing later)
> - `addonlib/` (unless you want plugin execution later)
> 
> ---
> 
> # What to tell the IDE to do next (aligned with QiOne)
> 
> You want it to *study Docspell’s schema + fts + pipeline concepts*, then scaffold QiVault Docs module accordingly.
> 
> Use this prompt:
> 
> ```text
> We are building QiVault Docs (QiDocSpell-like) as a module inside QiOne using Supabase Postgres/Auth/Storage.
> Before scaffolding, inspect Docspell source (local path c:\QiLabs\docspell-master\modules) ONLY to extract:
> - core schema concepts from modules/store migrations (postgresql)
> - file key + hash + integrity concepts from modules/common
> - FTS schema concepts from modules/fts-psql
> - job/state machine concepts from modules/joex (process + integrity tasks)
> Do NOT adopt Scala/Elm code; translate concepts into our existing QiOne patterns.
> 
> Now implement in QiOne:
> 1) New module app: qivault-docs (React+Vite) registered in the QiOne launcher/nav using existing module registration conventions.
> 2) Supabase migrations implementing Docspell-inspired tables:
>    - documents
>    - document_files (variants: original, ocr_pdf, extracted_text, thumbnail, preview)
>    - tags + document_tags
>    - correspondents
>    - custom_fields + document_custom_field_values
>    - ingestion_jobs (status/state machine)
>    - file_integrity (sha256, bytes, mime, storage_backend, blob_key)
>    - fts_documents (or equivalent) using Postgres full-text search (tsvector), modeled after Docspell fts-psql approach
> 3) RLS policies consistent with QiOne tenancy rules.
> 4) Storage abstraction interface BlobStore with default Supabase implementation and stubs for Cloudflare R2 + Google Drive.
> 5) UI pages: inbox, search, document detail, tags, settings (custom fields/correspondents)
> 6) Minimal upload endpoint (Supabase Edge Function) that:
>    - accepts file
>    - computes sha256 + bytes + mime
>    - writes to storage with deterministic key
>    - inserts DB rows atomically
> 7) README and “pipeline contract” docs.
> 
> Output: directory tree, SQL migrations, RLS SQL, core TS types/interfaces, and React page stubs.
> ```
> 
> ---
> 
> ## If you only peek at *one* thing in modules
> Peek at:
> 
> `modules/store/src/main/resources/db/migration/postgresql/V1.0.0__initial_database.sql`
> 
> That single file will reveal the actual “Docspell brain”—what they consider an item, how they attach files, and what metadata they store.
> 
> If you paste just that SQL file content, I can tell you exactly which tables to copy conceptually and which ones to ignore for QiVault v0.

### User
> ok, im ready for an ui, alredy wrap it with tauri or electron?

### Assistant
> Tauri. Electron is overkill for what you’re building and will punish you on RAM/battery and update complexity.
> 
> ### Decision
> - **Pick Tauri** if you want a desktop shell for your existing React+Vite module and you care about speed, footprint, and “feels like a real app.”
> - **Only pick Electron** if you need deep Node integrations everywhere, lots of existing Electron plugins, or you’re basically shipping a Chromium app with heavy desktop APIs.
> 
> For QiOne + Supabase + optional Drive/R2, **Tauri is the clean fit**.
> 
> ---
> 
> ## What “desktop app” should actually do (and what it shouldn’t)
> You don’t need desktop for “a UI.” You need desktop for:
> - drag/drop folders + big batch imports
> - background uploads (even when window minimized)
> - local hot-cache (preview files, thumbnails)
> - offline-ish browsing of already-synced docs
> - OS file picker + filesystem watch (optional)
> 
> If you aren’t doing those, ship it as a web app first and wrap later.
> 
> ---
> 
> ## Recommended path (fast + aligned)
> ### v0 (now): Web UI first
> - Build `qivault-docs` as a QiOne module in the browser.
> - Use Supabase Storage + DB, get Inbox/Search/Detail solid.
> - This proves schema, search, and curation.
> 
> ### v1 (desktop): Wrap with Tauri
> - Add a `apps/qione-desktop/` (or `apps/qivault-desktop/`) wrapper.
> - Reuse the same UI bundle.
> - Add only the desktop-only features (bulk ingest, local cache, background tasks).
> 
> This avoids locking your architecture into desktop constraints too early.
> 
> ---
> 
> ## Tell the IDE to scaffold Tauri wrapper (copy/paste)
> ```text
> Add a desktop wrapper for the existing QiOne module "qivault-docs" using Tauri v2.
> 
> Requirements:
> - Create a new app package in the monorepo: apps/qione-desktop (or apps/qivault-desktop if repo convention prefers)
> - Frontend: reuse the existing React+Vite build from qione (or mount only qivault-docs routes)
> - Tauri capabilities:
>   1) File system access for selecting files/folders
>   2) Drag-and-drop import into "Inbox"
>   3) Local cache directory for previews/thumbnails (store cache path in config)
>   4) Background upload queue (persist queue state locally; retries; show status)
>   5) Minimal secure bridge API (Rust commands) for: select_folder, list_files, compute_sha256, read_file_stream, write_cache, open_in_os
> 
> Security:
> - Disable arbitrary shell execution.
> - Use allowlist for FS directories and commands.
> - Do not embed Supabase service role keys in the app.
> - Use user auth via Supabase (PKCE) and store session securely.
> 
> Output:
> - Directory tree
> - Tauri config
> - Rust command stubs + TS bindings
> - Desktop-only UI components: ImportPanel, UploadQueue, CacheSettings
> - README with dev/build steps for Windows 11
> ```
> 
> ---
> 
> ## One critical warning (so you don’t shoot yourself)
> If you do desktop *and* cloud, you must decide where hashing happens:
> - **Best**: hash locally in Tauri (Rust) before upload → store sha256 in DB → detect duplicates early.
> - Web-only hashing works, but big files + memory = pain.
> 
> ---
> 
> If you want the “minimum viable desktop” right now: **Tauri wrapper + folder picker + bulk import + local hashing + upload queue**. Everything else can stay web.

### User
> isnt the issue communicating from teh browser to the file system but if we are using our databse and just drafging dropping previewing then we are good no? but we ahve to have a desktop agent for monitory folders and such or our ingest is what i upload.

### Assistant
> Yes—if your workflow is “I manually upload/drag-drop files into the UI,” you do **not** need a desktop wrapper. A web app is enough.
> 
> ### What the browser can do fine (no desktop agent)
> - Drag/drop files into the page
> - Upload to Supabase Storage
> - Show previews (PDF/image) after upload
> - Run OCR/extraction server-side (Railway/Worker) after upload
> - Tag/curate/search in the UI
> 
> That covers “Zotero-like curation” as long as you accept: **ingest only happens when you upload**.
> 
> ### What the browser cannot do (or does badly)
> These are the real reasons to use Tauri/Electron:
> - **Monitor folders** (watch filesystem continuously)
> - **Background ingest** while the UI is closed/minimized
> - **Ingest huge folders smoothly** (browser memory limits, throttling, tab sleeps)
> - **Local hot cache** that persists and works offline
> - **True filesystem integration** (move/rename files on disk, keep in sync)
> 
> So you’re exactly right: the “issue” is only there if you want **folder watching + always-on ingestion**.
> 
> ---
> 
> ## Pick your mode (simple vs powerful)
> 
> ### Mode A — “Upload-only” (recommended v0)
> - No desktop app.
> - Ingest is exactly what you upload/drag-drop.
> - Add a “Bulk Import” screen that accepts folder drops (works in modern browsers) and uploads in chunks with resumable logic.
> 
> This is the fastest path to a working QiVault UI.
> 
> ### Mode B — “Watched folders” (v1)
> - Add a **desktop agent** (Tauri service or small Python agent) that:
>   - watches configured folders
>   - hashes files
>   - uploads + creates DB rows
>   - reports status to the UI
> 
> UI becomes optional; ingest continues regardless.
> 
> ---
> 
> ## Practical recommendation
> Do **Mode A now**. You’re trying to get a rigid Zotero-ish UI running. Don’t invent a background agent until the schema + UI are stable.
> 
> Then, if you still want watching:
> - add a lightweight agent later.
> 
> ---
> 
> ## If you want folder-drop in the browser (without desktop)
> You can still do it:
> - Drag a folder into Chrome/Edge → you can traverse files via the File System Access API (best) or directory entries (older).
> - Then upload sequentially with concurrency limits + progress.
> 
> The only “gotcha”: browser support varies and you don’t get real-time watching.
> 
> ---
> 
> ## “Tell the IDE” prompt for Mode A (web-only, no desktop)
> ```text
> Implement QiVault Docs ingest as web-only (no Tauri/Electron).
> 
> Add an Import page:
> - supports drag/drop of files and folders (use File System Access API when available; fallback to file-only)
> - computes sha256 client-side (WebCrypto) for each file before upload
> - uploads to Supabase Storage with deterministic blob_key
> - inserts DB rows: documents + document_files + file_integrity + ingestion_jobs
> - shows progress UI with retry and pause/resume
> - dedup behavior: if sha256 already exists for tenant, flag as duplicate and skip upload (or attach as alternate)
> 
> Do not implement folder watching. Ingest is only what user uploads.
> ```
> 
> ---
> 
> If you tell me which browsers you actually care about (Chrome only vs “must work on Safari”), I’ll give you the exact technical path for folder uploads without desktop, and what to avoid.

### User
> mode a, keeps is mobile and eplicit desktop trash is not automatically added. i like it.

### Assistant
> Mode A is the right call.
> 
> ## Mode A contract (so the build stays clean)
> - **Ingest is explicit**: only what the user selects/drops/uploads.
> - **No background watchers**.
> - **Mobile-first**: camera scan + file upload work; folder-drop is “nice-to-have” on desktop browsers.
> 
> ## What to build (QiVault Docs module inside QiOne)
> ### Pages
> 1) **Inbox (Import)**
> - Upload button (files, camera, scan)
> - Drag/drop zone (desktop)
> - Queue with progress + retry
> - “Duplicate detected” banner per file (sha256 match)
> 
> 2) **Library (Browse)**
> - Filters: tag, correspondent, date, type
> - Saved searches
> 
> 3) **Search**
> - Keyword + advanced filters
> - FTS results (title/snippet/highlights)
> 
> 4) **Document Detail**
> - Preview
> - Metadata edit (tags, correspondent, custom fields)
> - Attachments/variants list: `original`, `ocr_pdf`, `extracted_text`, `thumbnail`, `preview`
> - Integrity panel (sha256, size, storage key)
> 
> 5) **Settings**
> - Custom fields schema
> - Storage backends (default Supabase; stubs for R2/Drive)
> - Export/download all
> 
> ## Minimal backend pieces
> - Supabase tables: `documents`, `document_files`, `file_integrity`, `tags`, `document_tags`, `custom_fields`, `document_custom_field_values`, `ingestion_jobs`
> - Supabase Storage bucket: `qivault`
> - Edge Function (optional but recommended): `upload_finalize` to do atomic DB writes after storage upload
> - Postgres FTS table/view for extracted text
> 
> ## “Tell the IDE” scaffold prompt (Mode A, mobile-first)
> ```text
> Scaffold QiVault Docs as a QiOne module (web-only, mobile-first). No Tauri/Electron. No folder watching.
> 
> Stack:
> - React + Vite module inside QiOne
> - Supabase Auth + Postgres + Storage
> - Optional Cloudflare later (do not hard-depend)
> 
> Deliverables:
> 1) apps/qione (existing) + new module route: /vault/docs
> 2) UI pages: InboxImport, Library, Search, DocumentDetail, Settings
> 3) Upload flow (mobile-first):
>    - file picker supports camera capture on mobile
>    - drag/drop for desktop
>    - compute sha256 client-side (WebCrypto) and size/mime
>    - check duplicates by sha256 via RPC or indexed query
>    - upload to Supabase Storage with deterministic key: tenant_id/sha256[:2]/sha256/filename
>    - insert DB rows atomically (Edge Function or single transaction via RPC)
>    - create ingestion_job row for server-side processing (OCR/extract/thumbnail)
> 4) Postgres:
>    - migrations for documents/document_files/file_integrity/tags/custom_fields/ingestion_jobs
>    - RLS policies for tenant isolation
>    - FTS: store extracted text in a table with tsvector index
> 5) Processing hooks:
>    - create placeholders for OCR/extract pipeline integration (Railway worker endpoint), but do not require it to run
> 
> Output:
> - directory tree
> - SQL migrations + RLS
> - TS types
> - core components: UploadDropzone, UploadQueue, DuplicateBadge, DocPreview
> - README with dev steps
> ```
> 
> ## Non-negotiable design choices (keeps it Zotero-rigid)
> - **sha256 is the identity** of the binary (immutable)
> - file variants are separate records (no overwriting)
> - deterministic storage keys (no random UUID junk)
> - dedup happens before upload when possible; after upload as a safety net
> 
> If you want, paste your current QiOne repo tree (top-level `apps/` + `packages/`) and I’ll align the exact paths/names so the scaffold matches your existing conventions.

### User
> you kow how i always want to view things in a timeline, i almost need to have a event table or databse that i can track event and sync calendars too, to crate differnt views and filter and such timelines. what do yyou recommend, make my own Events module or what?

### Assistant
> Make your own module. Trying to force “timeline brain” into a document system (or into Google Calendar as the database) will keep annoying you forever.
> 
> The clean move is:
> 
> ## Recommendation
> Build a **QiChronicle module** (your timeline OS) and let everything else (QiVault Docs, QiHome, case work, caregiving) **emit events into it**.
> 
> Docs don’t become your timeline. They **generate timeline entries**.
> 
> ---
> 
> ## Architecture that won’t paint you into a corner
> 
> ### Source of truth
> - **Supabase Postgres** = canonical events database.
> 
> ### Views
> - Timeline (Markwhen-style)
> - Calendar grid (day/week/month)
> - List + filters
> - “Context lanes” (Case, Mom, Work, Money, Health, Admin)
> 
> ### Sync strategy
> - **One-way export first**: QiChronicle → ICS feed(s) that Google/Apple can subscribe to.
> - **Two-way sync later** (harder): Google Calendar ↔ QiChronicle, with conflict rules.
> 
> One-way gets you 80% of value with 20% of effort.
> 
> ---
> 
> ## Event model you actually need (not Google’s model)
> Google Calendar is “appointments.” You need “moments” + “tasks” + “deadlines” + “communications” + “evidence” + “financial events.”
> 
> So define a single `events` table that can represent:
> - meeting
> - deadline
> - payment
> - incident
> - filing
> - phone call
> - message
> - document created/uploaded
> - status change
> 
> …and attach objects to it.
> 
> ---
> 
> ## Minimal schema (Supabase) that supports everything
> You can start with 3 tables and expand.
> 
> ### 1) `events`
> Core record.
> 
> Suggested columns:
> - `id` uuid pk
> - `tenant_id` uuid
> - `created_by` uuid
> - `title` text
> - `kind` text (meeting|deadline|payment|incident|note|doc|call|message|task)
> - `status` text (planned|done|canceled|void)
> - `start_at` timestamptz
> - `end_at` timestamptz null
> - `all_day` boolean default false
> - `timezone` text null
> - `location` text null
> - `description` text null
> - `tags` text[] default '{}'
> - `context` jsonb default '{}'  (case_id, project, people, etc.)
> - `source` text (manual|qivault|qihome|import|calendar_sync)
> - `source_ref` text null (id in source system)
> - `visibility` text (private|shared)
> - `created_at`, `updated_at`
> 
> ### 2) `event_links`
> Attach anything to an event without schema wars.
> 
> - `id` uuid pk
> - `tenant_id` uuid
> - `event_id` uuid fk events
> - `target_type` text (document|person|org|payment|file|url|case|note)
> - `target_id` uuid null
> - `target_url` text null
> - `label` text null
> 
> ### 3) `calendar_feeds`
> For ICS export + later sync.
> 
> - `id` uuid pk
> - `tenant_id` uuid
> - `name` text
> - `filter` jsonb (kinds/tags/context lanes)
> - `secret` text (unlisted feed token)
> - `created_at`
> 
> Then generate:
> - `GET /calendar/:secret.ics` (Cloudflare Worker is perfect for this)
> 
> ---
> 
> ## How this plugs into your “Mode A” document UI
> When a document is uploaded/processed:
> - Create an event automatically:
>   - kind=`doc`
>   - start_at = upload timestamp (or doc date if extracted)
>   - link to the document in `event_links`
> - If OCR finds a due date or “court date” later, create:
>   - kind=`deadline` with extracted date
>   - status=`planned`
>   - link to that document as evidence
> 
> That’s the Zotero “rigid linking” vibe, but for time.
> 
> ---
> 
> ## What to tell the IDE to build (scaffold prompt)
> ```text
> Create a new QiOne module: QiChronicle (timeline + calendar).
> 
> Stack:
> - React + Vite module inside QiOne
> - Supabase Postgres/Auth
> - Cloudflare Worker endpoint for ICS feed export
> 
> Features (v0):
> 1) Events CRUD with filters (kind, tags, status, date range, context)
> 2) Views:
>    - Timeline view (vertical)
>    - Calendar view (month + agenda list)
>    - List view with saved filters
> 3) Event linking:
>    - event_links table and UI to attach documents/urls/people
> 4) ICS export:
>    - calendar_feeds table
>    - Cloudflare Worker route GET /calendar/:secret.ics that returns VEVENTs
>    - Support feed filters (kinds/tags/context)
> 5) “Emit event” integration point:
>    - Provide a small TS helper that other modules can call (QiVault Docs emits kind=doc events)
> 
> Deliver:
> - SQL migrations + RLS
> - Module routes + page components
> - Worker code for ICS export
> - README
> ```
> 
> ---
> 
> ## Hard truth
> If you skip building QiChronicle and keep trying to “timeline” inside every other module, you’ll rebuild the same feature 6 times and hate all 6 versions.
> 
> Build **one timeline database**. Everything else feeds it.
> 
> If you want, paste what you called the record in your earlier “moments” schema (you said you disliked “event”). I’ll give you a naming set that fits your tone and doesn’t collide with calendar semantics.

### User
> PS C:\QiLabs\_QiOne_MonoRepo_Astro> pnpm dev

> 

> > qione@ dev C:\QiLabs\_QiOne_MonoRepo_Astro

> > turbo run dev

> 

> • turbo 2.8.10

>  WARNING  stale pid file at "C:\\Users\\Lisa\\AppData\\Local\\Temp\\turbod\\4a6dbcc52e0013bb\\turbod.pid"

>   × Found `pipeline` field instead of `tasks`.

>     ╭─[turbo.json:3:17]

>   2 │         "$schema": "https://turbo.build/schema.json",

>   3 │ ╭─▶     "pipeline": {

>   4 │ │           "build": {

>   5 │ │               "dependsOn": [

>   6 │ │                   "^build"

>   7 │ │               ],

>   8 │ │               "outputs": [

>   9 │ │                   "dist/**",

>  10 │ │                   ".astro/**"

>  11 │ │               ]

>  12 │ │           },

>  13 │ │           "dev": {

>  14 │ │               "cache": false,

>  15 │ │               "persistent": true

>  16 │ │           },

>  17 │ │           "clean": {

>  18 │ │               "cache": false

>  19 │ │           },

>  20 │ │           "index": {

>  21 │ │               "cache": false

>  22 │ │           },

>  23 │ │           "rules": {

>  24 │ │               "cache": false

>  25 │ │           },

>  26 │ │           "pdf": {

>  27 │ │               "cache": false

>  28 │ │           },

>  29 │ │           "inbox:audit": {

>  30 │ │               "cache": false

>  31 │ │           },

>  32 │ │           "inbox:fix": {

>  33 │ │               "cache": false

>  34 │ │           },

>  35 │ │           "inbox:pdf": {

>  36 │ │               "cache": false

>  37 │ │           },

>  38 │ │           "inbox:normalize": {

>  39 │ │               "cache": false

>  40 │ │           }

>  41 │ ├─▶     }

>     · ╰──── Rename `pipeline` field to `tasks`

>  42 │     }

>     ╰────

>   help: Changed in 2.0: `pipeline` has been renamed to `tasks`.

> 

>  ELIFECYCLE  Command failed with exit code 1.

> PS C:\QiLabs\_QiOne_MonoRepo_Astro>

### Assistant
> Turbo v2 expects `tasks`, not `pipeline`. Fix is mechanical.
> 
> ## 1) Patch `turbo.json`
> Open `turbo.json` and change the top-level key `pipeline` → `tasks`.
> 
> Example (minimal diff):
> 
> ```json
> {
>   "$schema": "https://turbo.build/schema.json",
>   "tasks": {
>     "build": {
>       "dependsOn": ["^build"],
>       "outputs": ["dist/**", ".astro/**"]
>     },
>     "dev": {
>       "cache": false,
>       "persistent": true
>     },
>     "clean": { "cache": false },
>     "index": { "cache": false },
>     "rules": { "cache": false },
>     "pdf": { "cache": false },
>     "inbox:audit": { "cache": false },
>     "inbox:fix": { "cache": false },
>     "inbox:pdf": { "cache": false },
>     "inbox:normalize": { "cache": false }
>   }
> }
> ```
> 
> That should stop the hard error.
> 
> ---
> 
> ## 2) Clear the stale Turbo daemon pid (optional but good)
> That warning won’t usually break anything, but since it’s already complaining:
> 
> ```powershell
> Remove-Item -Recurse -Force "$env:TEMP\turbod" -ErrorAction SilentlyContinue
> ```
> 
> ---
> 
> ## 3) Run again
> ```powershell
> pnpm dev
> ```
> 
> ---
> 
> ## If it still fails after that
> Run this to verify what turbo version is actually being used and confirm config is picked up:
> 
> ```powershell
> pnpm turbo --version
> Get-Content .\turbo.json
> ```
> 
> If you paste your current `turbo.json` contents, I’ll return the corrected full file exactly as it should be.

### User
> {

>     "$schema": "https://turbo.build/schema.json",

>     "tasks": {

>         "build": {

>             "dependsOn": [

>                 "^build"

>             ],

>             "outputs": [

>                 "dist/**",

>                 ".astro/**"

>             ]

>         },

>         "dev": {

>             "cache": false,

>             "persistent": true

>         },

>         "clean": {

>             "cache": false

>         },

>         "index": {

>             "cache": false

>         },

>         "rules": {

>             "cache": false

>         },

>         "pdf": {

>             "cache": false

>         },

>         "inbox:audit": {

>             "cache": false

>         },

>         "inbox:fix": {

>             "cache": false

>         },

>         "inbox:pdf": {

>             "cache": false

>         },

>         "inbox:normalize": {

>             "cache": false

>         }

>     }

> }

### Assistant
> Your `turbo.json` is correct now. The error you pasted earlier was from before you renamed `pipeline` → `tasks`.
> 
> Two likely issues now:
> 
> ---
> 
> ## 1️⃣ Turbo daemon stale state (most common after schema change)
> 
> Kill it cleanly:
> 
> ```powershell
> pnpm turbo kill
> Remove-Item -Recurse -Force "$env:TEMP\turbod" -ErrorAction SilentlyContinue
> ```
> 
> Then run:
> 
> ```powershell
> pnpm dev
> ```
> 
> ---
> 
> ## 2️⃣ Version mismatch (repo expecting Turbo < 2)
> 
> Check:
> 
> ```powershell
> pnpm turbo --version
> ```
> 
> If it says **2.x**, you’re fine.
> 
> If the repo’s `package.json` has an older turbo pinned (like 1.x), but global turbo is 2.x, weirdness can happen.
> 
> Run:
> 
> ```powershell
> pnpm list turbo
> ```
> 
> If needed, align it explicitly in root `package.json`:
> 
> ```json
> "devDependencies": {
>   "turbo": "^2.8.10"
> }
> ```
> 
> Then:
> 
> ```powershell
> pnpm install
> ```
> 
> ---
> 
> ## 3️⃣ Clean reinstall (if still failing)
> 
> Sometimes Turborepo caches get funky after schema changes.
> 
> ```powershell
> rd /s /q node_modules
> del pnpm-lock.yaml
> pnpm install
> pnpm dev
> ```
> 
> ---
> 
> ## Sanity Check
> 
> Your current `turbo.json` is valid for Turbo v2:
> 
> - `tasks` ✅
> - `persistent: true` on dev ✅
> - `outputs` defined for build ✅
> 
> There is nothing syntactically wrong in that file.
> 
> ---
> 
> If it still errors, paste:
> 
> - Full new error output (after rename)
> - Root `package.json`
> - `pnpm turbo --version`
> 
> We’ll zero it in fast.

### User
> im looking at this https://docspell.org/docs/install/docker/#start-docspell and its got like bunch of differnt types and options or soemthing so im lost.

### Assistant
> Good. Pause. Breathe. That page is not for you right now.
> 
> Docspell’s Docker page looks overwhelming because it’s describing **every possible deployment topology**:
> 
> - Full stack
> - Separate services
> - With Joex (job executor)
> - Without Joex
> - With PostgreSQL
> - With external PostgreSQL
> - With reverse proxy
> - With addons
> - With SMTP
> - With OIDC
> - With multiple users
> - With encryption
> - With background workers
> - With file backends
> - Etc.
> 
> You don’t need 80% of that.
> 
> You are not deploying a production document SaaS.
> 
> You are peeking at architecture.
> 
> ---
> 
> ## What Docspell actually consists of
> 
> Core components:
> 
> 1. **REST server** – the API + main backend  
> 2. **Joex** – background job processor (OCR, text extraction, dedup, etc.)  
> 3. **Postgres** – database  
> 4. **File backend** – filesystem or S3  
> 5. **Web app** – frontend  
> 
> That’s it.
> 
> All the variations on the Docker page are just “how do you want to wire these together.”
> 
> ---
> 
> ## Why it feels overwhelming
> 
> Because Docspell is:
> 
> - A multi-service Scala system
> - Designed for self-hosting
> - Designed for multi-user setups
> - Designed to scale
> 
> You are building:
> > A Supabase-backed module inside QiOne.
> 
> Different category entirely.
> 
> ---
> 
> ## What you should extract from that page
> 
> Not “how to install.”
> 
> Look at:
> - Which services exist
> - Which are required
> - Which are optional
> - How files are stored
> - How background jobs are separated
> 
> You want conceptual separation, not Docker commands.
> 
> ---
> 
> ## Reality check
> 
> If you were to install Docspell just to “see how it feels,” the simplest stack is:
> 
> - 1 container: Docspell
> - 1 container: Postgres
> - Local file storage
> 
> That’s it.
> 
> But that teaches you nothing about your QiOne integration.
> 
> ---
> 
> ## Important strategic question
> 
> Are you:
> 
> A) Trying to evaluate Docspell UX by running it?  
> B) Trying to understand architecture by reading install docs?  
> C) Trying to decide whether to abandon building your own and just use Docspell?
> 
> Because those are different motivations.
> 
> ---
> 
> ## Here’s the blunt truth
> 
> If your goal is:
> 
> > “Should I just use Docspell instead of building QiVault?”
> 
> Then:
> Run it locally with the simplest docker-compose.
> Click around.
> Feel it.
> 
> If your goal is:
> 
> > “How do I design QiVault correctly?”
> 
> Then:
> The Docker page is mostly noise.
> 
> ---
> 
> ## What I recommend
> 
> Don’t install yet.
> 
> Instead:
> 
> Open:
> - `modules/store` (schema)
> - `modules/common` (file key + hash)
> - `modules/joex` (job pipeline)
> 
> That gives you 90% of the insight without spinning up anything.
> 
> ---
> 
> If you want, tell me what triggered this—was it:
> 
> - “This looks too complex, maybe I shouldn’t build my own?”
> - “Maybe I should just self-host Docspell and move on?”
> - “I’m overwhelmed by architecture decisions again?”
> 
> Be honest. That tells me which direction to push you.

### User
> i want a app on web, data online, storage online, if my pc blows up oh well setup.

### Assistant
> Perfect. That’s the correct priority: **web app + online DB + online storage + disposable laptop**. Your PC can explode into confetti and you still log in and keep moving. Humans should do this more often, but they love suffering.
> 
> Here’s the clean architecture that matches what you just said.
> 
> ## The “PC can die, I don’t care” stack (recommended)
> ### Core
> - **Web app (QiOne module UI)**: Cloudflare Pages (Astro/React)
> - **Auth + DB**: Supabase (Postgres + Auth + RLS)
> - **File storage**: *Either*
>   - **Supabase Storage** (simple, integrated, fine for most)
>   - **Cloudflare R2** (cheaper at scale, great for big archives)
>   - **Google Drive** (optional “backbone backup”, not your primary app storage)
> - **Background jobs** (OCR, PDF preview gen, embeddings, dedupe):
>   - **Cloudflare Workers + Queues** (Cloudflare-first)
>   - or **Railway worker** (if you want a “real server” worker that runs longer tasks)
> 
> ### What you *avoid*
> - Anything that requires local state as the source of truth
> - “Desktop-only” workflows as required dependencies
> 
> ---
> 
> ## Ingestion model choices (you already named them)
> ### Mode A: Web-only ingestion (your “PC can die” dream)
> - You ingest by:
>   - Drag/drop in the browser
>   - Email forward to an ingest address (optional)
>   - Mobile upload (camera scans, etc.)
> - System does:
>   - Hash + store file
>   - Create “document” record
>   - Run pipeline async: OCR/extract, classify, rename suggestion, link to “events” timeline if needed
> 
> **Pros:** no desktop agent required, simplest, resilient  
> **Cons:** folder-watch automation doesn’t exist unless you add it later
> 
> This is the correct default.
> 
> ### Mode B: Folder-watch agent (later, optional)
> - A tiny desktop agent watches `INBOX/` and uploads.
> - If your PC dies, you just reinstall agent later. The data is already online.
> 
> **Pros:** effortless ingestion from local chaos  
> **Cons:** you’re back in “local system integration” territory
> 
> You can add this later without changing your data model if you design it right.
> 
> ---
> 
> ## What to tell the IDE agent to scaffold (QiOne-aligned)
> You want a module that fits your monorepo and doesn’t go rogue. Here’s the instruction set you give the IDE agent.
> 
> ```txt
> SCAFFOLD A NEW QIONE MODULE: "qi_ingest"
> 
> Goal:
> A web-first ingestion + searchable document registry. Data online in Supabase. Files stored online. PC can die, no local dependency.
> 
> Monorepo assumptions:
> - Turborepo + pnpm workspace.
> - Existing apps live under /apps, shared libs under /packages.
> - Cloudflare Pages deployment for web.
> - Supabase for Postgres/Auth/RLS.
> - Optional background worker via Cloudflare Worker or Railway.
> 
> Deliverables:
> 1) apps/web-qione (existing) gets a new route/page: /ingest and /library
> 2) packages/db: add Supabase SQL migrations + typed schema (Drizzle or Kysely or plain SQL + generated types)
> 3) packages/sdk: shared TS client for Supabase queries + storage upload helpers
> 4) packages/ui: shared components for uploader, file cards, filters, timeline view
> 5) apps/worker (optional): background processor for OCR/extract/embed/dedupe with a job queue
> 
> Database schema (Supabase):
> - documents (id uuid pk, owner_id uuid, created_at, source, original_filename, mime, size, sha256, storage_bucket, storage_path, status, title, summary, doc_date, tags jsonb)
> - document_pages (id, document_id, page_no, preview_path, text)
> - ingest_jobs (id, document_id, job_type, status, attempts, error, started_at, finished_at)
> - events (id, owner_id, occurred_at, event_type, title, notes, related_document_id nullable)
> - rules (id, owner_id, name, enabled, priority, match_json, action_json)  // for smart triage later
> 
> RLS:
> - owner_id = auth.uid() on all user-owned tables
> 
> Web UI:
> - Upload dropzone -> creates document row -> uploads file -> sets status "queued"
> - Library view with search + filters + timeline toggle
> - Document detail with preview (pdf/image), extracted text, metadata, suggested name
> 
> Background:
> - After upload, enqueue jobs: extract_text, generate_preview, embed, dedupe_check
> - For now stub OCR/extract with placeholders but wire the pipeline and statuses.
> 
> Monorepo tooling:
> - turbo tasks: dev/build/lint/test for module
> - follow existing lint/format conventions (biome/eslint)
> - env management: .env.example, read SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY (server only)
> 
> Output:
> Create all files and wiring so `pnpm dev` runs and the new routes render, upload works end-to-end, and records appear in Supabase.
> ```
> 
> That prompt is “scaffold me a real system” instead of “make me vibes.”
> 
> ---
> 
> ## Storage decision (pick one now so you don’t thrash)
> If you want minimal decisions today:
> 
> **Use Supabase Storage first.**
> - It’s integrated
> - Signed URLs are easy
> - Permissions map nicely with RLS patterns (even though storage policies are their own thing)
> 
> Later, if you’re storing massive archives and want cheaper egress/cost control:
> **Move binaries to Cloudflare R2**, keep metadata in Supabase.
> 
> Google Drive stays as:
> - **backup backbone** or
> - a separate “import source”
> Not your primary store.
> 
> ---
> 
> ## About your “Events / Timeline brain”
> Yes: build your own **Events** table/module. Don’t try to force calendar sync as your primary data model.
> 
> **Your system-of-record is your Events table.**
> Calendar sync is a view/export/import layer.
> 
> Minimal event model:
> - `occurred_at` (timestamp)
> - `event_type` (enum-ish)
> - `title`
> - `notes`
> - `related_document_id` (nullable FK)
> - later: `external_calendar_event_id` for sync mapping
> 
> That gives you:
> - timeline
> - filters
> - “show me everything related to this document/case/client”
> - “calendar is optional”
> 
> ---
> 
> ## What you do next (no dithering)
> 1) **Implement Mode A** (web upload + online pipeline) first.
> 2) Add **Events module** beside it (even minimal).
> 3) Only then consider **desktop agent** if you still care.
> 
> Because the fastest way out of chaos is: **get ingestion online and searchable**, not perfect, just working.
> 
> And yes, your earlier Turbo error was real and you already fixed it by renaming `pipeline` → `tasks`. That’s the kind of dumb paper cut that makes people start new repos. Don’t.

### User
> dont need folder watch ill upload, give me the end game repo setup no guess work just what must we have.

### Assistant
> Good. Folder watch is how you accidentally build a second job you never asked for.
> 
> Here’s the **end-game repo setup** for a **web-only ingestion app** (upload in browser), **online DB**, **online storage**, **background processing**, **timeline/events**, and **zero “guesswork” extras**. This is the minimum *complete* system that won’t paint you into a corner.
> 
> ---
> 
> ## End-game monorepo (what must exist)
> 
> ```
> _QiOne_MonoRepo_Astro/
> ├─ turbo.json
> ├─ package.json
> ├─ pnpm-workspace.yaml
> ├─ .env.example
> ├─ README.md
> 
> ├─ apps/
> │  ├─ web/                         # The actual product UI (Astro + React islands)
> │  │  ├─ astro.config.mjs
> │  │  ├─ src/
> │  │  │  ├─ pages/
> │  │  │  │  ├─ ingest.astro        # Upload + triage
> │  │  │  │  ├─ library.astro       # Search/browse
> │  │  │  │  ├─ doc/[id].astro      # Doc detail/preview/text
> │  │  │  │  └─ events.astro        # Timeline / filters
> │  │  │  ├─ components/
> │  │  │  └─ styles/
> │  │  └─ public/
> │  └─ worker/                      # Background pipeline (Cloudflare Workers)
> │     ├─ wrangler.toml
> │     └─ src/
> │        ├─ index.ts               # Queue consumer + HTTP entry
> │        └─ jobs/
> │           ├─ extract_text.ts     # PDF/text extraction
> │           ├─ make_previews.ts    # thumbnails/images (or stub)
> │           ├─ embed.ts            # embeddings (optional, but slot exists)
> │           └─ dedupe.ts           # sha256 collision check
> 
> ├─ packages/
> │  ├─ db/                          # DB schema, migrations, types
> │  │  ├─ migrations/               # SQL migrations (Supabase-compatible)
> │  │  ├─ seed/                     # optional local seed scripts
> │  │  └─ schema.md                 # human-readable schema + conventions
> │  ├─ sdk/                         # Shared client logic (Supabase + upload helpers)
> │  │  └─ src/
> │  │     ├─ supabase_client.ts     # browser client
> │  │     ├─ documents.ts           # CRUD + search
> │  │     ├─ events.ts              # timeline queries
> │  │     ├─ storage.ts             # upload + signed url
> │  │     └─ jobs.ts                # enqueue job requests
> │  ├─ ui/                          # Shared UI components
> │  │  └─ src/
> │  │     ├─ Uploader.tsx
> │  │     ├─ DocumentCard.tsx
> │  │     ├─ Timeline.tsx
> │  │     └─ Filters.tsx
> │  └─ config/                      # Shared lint/tsconfig conventions
> │     ├─ tsconfig.base.json
> │     └─ biome.json (or eslint config)
> 
> └─ ops/
>    ├─ supabase/
>    │  ├─ README.md                 # how to apply migrations + policies
>    │  └─ policies.sql              # RLS + storage policies (source of truth)
>    └─ cloudflare/
>       ├─ README.md                 # how to deploy Pages + Worker + Queue
>       └─ env.md                    # env vars and where they live
> ```
> 
> That’s it. If you don’t have those pieces, you’re either missing core functionality or hiding it in random places like a raccoon.
> 
> ---
> 
> ## What must be true for the system to be “real”
> ### 1) Supabase is the system of record
> **Required tables** (minimum viable end-game):
> 
> - `documents`
> - `document_blobs` (or inline fields on documents if you want fewer tables)
> - `document_text` (extracted text, chunking later)
> - `events`
> - `job_runs` (or `ingest_jobs`)
> 
> You can add `rules` later, but it’s not required for “upload → search → timeline.”
> 
> ### 2) Storage is online and linked by path
> Binary files go to:
> - Supabase Storage bucket `docs` (recommended default)
> 
> DB row stores:
> - `bucket`
> - `path`
> - `sha256`
> - `mime`
> - `size`
> - `status`
> 
> ### 3) Pipeline is async, not “do everything on upload”
> Upload should do only:
> - compute hash (client or worker)
> - create DB record
> - upload file
> - enqueue jobs
> 
> Worker does:
> - extract text
> - create preview assets (even if stubbed initially)
> - embeddings (optional slot)
> - dedupe check
> 
> ### 4) Timeline is first-class
> `events` exists on day 1, even if you only add events manually at first.
> 
> ---
> 
> ## Deployment surface (what must exist)
> ### Cloudflare
> - **Pages**: deploy `apps/web`
> - **Worker + Queue**: deploy `apps/worker`
>   - Queue: `ingest-jobs` (consumer = worker)
> 
> ### Supabase
> - Project
> - Storage bucket(s)
> - RLS policies for tables
> - Storage policies for bucket access
> 
> ---
> 
> ## Environment variables (must exist, no magic)
> ### Web (public-safe)
> - `PUBLIC_SUPABASE_URL`
> - `PUBLIC_SUPABASE_ANON_KEY`
> 
> ### Worker (server secrets)
> - `SUPABASE_URL`
> - `SUPABASE_SERVICE_ROLE_KEY`
> - (optional) `OPENAI_API_KEY` or `VOYAGE_API_KEY` if doing embeddings
> - (optional) `PREVIEW_SERVICE_KEY` if you offload PDF rendering
> 
> No desktop secrets. No local “it works on my machine” nonsense.
> 
> ---
> 
> ## Why not Tauri/Electron (for your stated end game)
> Because you said: **web app, data online, storage online, PC can die.**
> Desktop wrappers add:
> - extra build pipelines
> - signing, packaging, updates
> - platform weirdness
> - and they solve a problem you explicitly said you don’t have (filesystem integration)
> 
> If later you want a “nice app icon,” wrap it then. Not now.
> 
> ---
> 
> ## Non-negotiable conventions (or you’ll hate yourself later)
> - One source of truth for DB: `packages/db/migrations`
> - One source of truth for policies: `ops/supabase/policies.sql`
> - All file references stored as `(bucket, path)` in DB
> - All UI uses `packages/sdk` methods, not raw queries scattered everywhere
> - All background status is visible on the document detail page
> 
> ---
> 
> If you build exactly this, you can:
> - upload 200 files in a day
> - search instantly (metadata now, extracted text soon)
> - see everything in timeline views
> - survive laptop death
> - add “rules” later without rewriting the world

### User
> and we organize the files based on tags or something no, like doesnt matter where the blob is organization is done by tagging hmmmm not sure,

### Assistant
> Correct instinct. **Blob location should be boring.** Organization should live in the database, not in your storage paths. Humans love pretending folder trees are “systems.” They’re not, they’re rituals.
> 
> ### The clean model
> - **Storage path = immutable, dumb, stable**
>   - Basically: `docs/{tenant}/{yyyy}/{mm}/{sha256}.{ext}`
>   - Or even flatter: `docs/{tenant}/{sha256}`
> - **Organization = DB metadata**
>   - Tags, entities, relationships, events, status, confidence, whatever.
> 
> So yes: **it doesn’t matter where the blob is** as long as you can fetch it fast and you never lose it.
> 
> ---
> 
> ## What “organization by tags” looks like (in DB)
> You need three things:
> 
> ### 1) Document core
> - `documents(id, title, created_at, source, status, sha256, mime, size, storage_bucket, storage_path, ...)`
> 
> ### 2) Tags (many-to-many)
> - `tags(id, name, color?, kind?)`
> - `document_tags(document_id, tag_id, confidence, created_by, created_at)`
> 
> Why `confidence`? Because AI tags are guesses. Human tags are law.
> 
> ### 3) Entities (optional but worth it early)
> Tags alone get messy. Entities keep it sane.
> 
> - `entities(id, type, name)`  (type: person, org, case, client, property, court, etc.)
> - `document_entities(document_id, entity_id, role?, confidence)`
> 
> This lets you filter like:
> - “All docs related to FCFCU AND property damage”
> - “All docs mentioning Miguel”
> - “Everything for Client X for tax year 2024”
> 
> ---
> 
> ## Folder-like views without folders
> You can generate “virtual folders” from tag rules:
> 
> - **Views** table (saved filters):
>   - `views(id, name, query_json)`
>   - Example query_json:
>     ```json
>     {
>       "tags_all": ["tax", "2024"],
>       "tags_any": ["1099", "w2"],
>       "entities_any": [{"type":"client","name":"Sara"}],
>       "status": ["ready","needs-review"]
>     }
>     ```
> 
> In the UI it *feels* like folders. Under the hood it’s just saved filters. Which is what folders wish they were.
> 
> ---
> 
> ## When storage paths DO matter
> Only for:
> - **dedupe + integrity**: sha256-based paths make duplicates obvious
> - **performance**: avoid deeply nested weirdness, keep it predictable
> - **portability**: if you ever migrate storage providers, you don’t want semantic paths you’ll regret
> 
> But for “where does it belong?”: **never in the path.**
> 
> ---
> 
> ## Recommendation for you (simple + future-proof)
> Do this:
> 
> ### Blob path
> `docs/{sha256}.{ext}` (or with year/month if you want)
> - Stable
> - Dedup-friendly
> - Doesn’t encode meaning
> 
> ### Organization
> - `tags`
> - `entities`
> - `events` (for timeline)
> - `collections/views` (saved filters)
> 
> This gives you:
> - “Inbox” view (status = `new`)
> - “Needs triage” view (missing tags or low confidence)
> - Case timelines (events filtered by entity:case)
> - Tax year buckets (tags: `tax/2024`, entity: `client:Sara`)
> 
> ---
> 
> ### The one trap
> If you rely on **only** tags, you’ll end up with a chaotic folksonomy like:
> `legal`, `lawsuit`, `court`, `case`, `fcfcu`, `FCFCU`, `bank`, `foreclosure`…
> 
> So: **tags + entities** is the sweet spot. Tags for themes, entities for “who/what this is about.”
> 
> That’s the difference between “organized” and “a vibe.”

### User
> I like this idea, one question the year month where does that come from upload date?

### Assistant
> Good question. This is where people accidentally bake bad assumptions into storage forever.
> 
> Short answer:
> 
> **The year/month in the storage path should come from upload time — not document date.**
> 
> Now I’ll explain why so you don’t regret this later.
> 
> ---
> 
> ## What the year/month is for (in storage)
> 
> It is **not** for human organization.
> 
> It is for:
> - Storage distribution
> - Operational sanity
> - Rough temporal grouping for infrastructure
> - Future migrations / cold storage policies
> 
> It is infrastructure metadata. Not business meaning.
> 
> ---
> 
> ## Why NOT use document date
> 
> Document date can be:
> - Extracted wrong
> - Missing
> - Backdated (e.g., 2017 tax doc uploaded in 2026)
> - Changed later after OCR improves
> - Multiple dates inside one document
> 
> If you encode that into the blob path:
> - You’ll either need to move files (bad)
> - Or you’ll have mismatches (worse)
> 
> Blobs should never move unless absolutely necessary.
> 
> ---
> 
> ## Correct model
> 
> ### Storage path
> Use upload timestamp:
> 
> ```
> docs/{tenant}/{yyyy}/{mm}/{sha256}.{ext}
> ```
> 
> Example:
> ```
> docs/user123/2026/02/a9f3...c2.pdf
> ```
> 
> Stable.
> Predictable.
> Never changes.
> 
> ---
> 
> ## Document date lives in DB
> 
> In `documents` table:
> 
> ```
> doc_date          (nullable)
> upload_date       (not null)
> extracted_dates   (jsonb array)
> ```
> 
> Your UI can:
> - Sort by doc_date
> - Filter by doc_date
> - Generate timeline from doc_date
> - Fall back to upload_date if missing
> 
> But storage never changes.
> 
> ---
> 
> ## Even cleaner option (if you want max purity)
> 
> You can remove year/month entirely:
> 
> ```
> docs/{tenant}/{sha256}.{ext}
> ```
> 
> Modern object storage doesn’t need directory sharding like old filesystems did.
> 
> Year/month is mostly aesthetic now.
> 
> If you’re not dealing with millions per month, you don’t even need it.
> 
> ---
> 
> ## My actual recommendation for you
> 
> Given your scale and goal:
> 
> Use:
> 
> ```
> docs/{sha256}.{ext}
> ```
> 
> No tenant prefix if RLS handles isolation.
> No year/month.
> No semantic naming.
> 
> Keep it dead simple.
> 
> ---
> 
> ## Mental model to lock in
> 
> Storage path = immutable content address  
> Database = meaning  
> Tags/entities/events = organization  
> Views = UX illusion of folders  
> 
> Blobs are rocks.
> Metadata is intelligence.
> 
> ---
> 
> If you want, I can give you the exact “final form” documents table that cleanly separates:
> - upload timestamp
> - document date
> - event date
> - processing state
> - integrity hash
> 
> No ambiguity, no future rewrites.

### User
> understood. ok, are we ready to build this and it work today, we are not going to give the ide all this to do it will take 5 hours, give me rock solid ai prompts to give to gemini seperatly and have it build the pieces i can put into the directory tree with all the placeholders you will build, then ill have the ide make sure its all connected correctly.

### Assistant
> Yes, you can have something working **today**. Not “perfect,” not “Docspell clone,” but **upload → DB row → blob stored → list + preview link** and a stubbed pipeline. That’s the 80/20 that stops the bleeding.
> 
> You’re right: don’t hand Gemini the whole universe. Give it **small, surgical prompts** that each output **files you can drop into the repo**.
> 
> Below are **rock-solid prompts** you can paste into Gemini **one at a time**. Each prompt tells it exactly what to produce, where to put it, and what placeholders to leave.
> 
> ---
> 
> ## Prompt 0 (Rules of engagement for Gemini)
> Use this first so it behaves.
> 
> ```text
> You are generating code for a Turborepo monorepo called _QiOne_MonoRepo_Astro.
> 
> Hard rules:
> - Output ONLY code files, each preceded by: === path/to/file ===
> - No explanations, no commentary.
> - Use placeholders instead of secrets (e.g. SUPABASE_URL, SUPABASE_ANON_KEY).
> - Do not invent non-existent repo files. Only create what I request.
> - Use TypeScript wherever possible.
> - Keep it minimal but working.
> 
> If you need environment variables, put them in .env.example and reference via process.env.* (server) or import.meta.env.* (web).
> ```
> 
> ---
> 
> ## Prompt 1 (DB schema + policies, Supabase-first)
> This creates the foundation. Don’t skip it.
> 
> ```text
> Create Supabase SQL migrations for a minimal “QiVault Docs” system.
> 
> Deliverables:
> 1) === packages/db/migrations/0001_qivault_docs.sql ===
>    - Enable pgcrypto extension if needed.
>    - Create tables:
>      - documents (
>          id uuid primary key default gen_random_uuid(),
>          created_at timestamptz not null default now(),
>          uploaded_at timestamptz not null default now(),
>          title text null,
>          source text null,              -- 'upload', later email, etc
>          status text not null default 'new',   -- new|processing|ready|error
>          sha256 text not null,
>          mime text not null,
>          size_bytes bigint not null,
>          bucket text not null default 'docs',
>          path text not null,            -- storage path
>          doc_date date null,
>          notes text null,
>          meta jsonb not null default '{}'::jsonb
>        )
>      - tags (id uuid pk default gen_random_uuid(), name text unique not null)
>      - document_tags (
>          document_id uuid references documents(id) on delete cascade,
>          tag_id uuid references tags(id) on delete cascade,
>          confidence real not null default 1.0,
>          created_at timestamptz not null default now(),
>          created_by text not null default 'user',
>          primary key (document_id, tag_id)
>        )
>      - events (
>          id uuid pk default gen_random_uuid(),
>          created_at timestamptz not null default now(),
>          occurred_at timestamptz not null,
>          title text not null,
>          kind text not null default 'note',
>          doc_id uuid null references documents(id) on delete set null,
>          meta jsonb not null default '{}'::jsonb
>        )
>    - Indexes:
>      - documents(sha256) unique
>      - documents(status)
>      - events(occurred_at desc)
>      - tags(name)
> 2) === ops/supabase/policies.sql ===
>    - RLS enabled for documents, tags, document_tags, events.
>    - Minimal policies for single-user prototype:
>      - allow authenticated users full CRUD on all rows.
>    - Also include storage bucket policy guidance comment for bucket 'docs' (authenticated read/write).
> 
> Notes:
> - Keep it Supabase compatible.
> - No multi-tenant yet. No organizations. Minimal working.
> Output only the two files.
> ```
> 
> ---
> 
> ## Prompt 2 (Shared Supabase SDK wrapper)
> This is how you avoid sprinkling Supabase calls everywhere.
> 
> ```text
> Create a shared TypeScript SDK package for Supabase access.
> 
> Deliverables:
> 1) === packages/sdk/src/supabase_client.ts ===
>    - Exports createBrowserClient() using @supabase/supabase-js
>    - Reads import.meta.env.PUBLIC_SUPABASE_URL and PUBLIC_SUPABASE_ANON_KEY
>    - Throws a clear error if missing
> 2) === packages/sdk/src/storage.ts ===
>    - uploadDocumentFile(file: File, sha256Hex: string): Promise<{bucket:string; path:string;}>
>    - Uses bucket 'docs'
>    - Path format: `${sha256Hex}${ext}` where ext is derived from file.name if present, else empty.
>    - Uses supabase.storage.from(bucket).upload(path, file, { upsert:false, contentType:file.type })
>    - If upload fails because file exists, treat as OK (idempotent) and return same path.
>    - Also export getSignedUrl(bucket, path, expiresSeconds=3600)
> 3) === packages/sdk/src/documents.ts ===
>    - createDocumentRecord(payload) inserts into documents with status='new'
>    - listDocuments({limit, status}) returns newest first
>    - getDocument(id) returns document row
>    - setDocumentStatus(id, status, metaPatch?) updates
> 4) === packages/sdk/src/events.ts ===
>    - createEvent({occurred_at,title,kind,doc_id?,meta?})
>    - listEvents({limit}) order by occurred_at desc
> 5) === packages/sdk/src/index.ts === exports everything
> 
> Also provide:
> 6) === packages/sdk/package.json ===
> 7) === packages/sdk/tsconfig.json === (extends workspace base placeholder)
> 8) === packages/sdk/README.md === minimal usage
> 
> Assume pnpm workspace. Use ESM. Keep code minimal and working.
> Output only the files.
> ```
> 
> ---
> 
> ## Prompt 3 (Web app pages: Upload + Library list + Doc detail)
> This gives you the “works today” UI.
> 
> ```text
> Create minimal Astro + React islands pages for:
> - Upload/ingest
> - Library list
> - Document detail with preview link (signed URL)
> 
> Deliverables (Astro app at apps/web):
> 1) === apps/web/src/pages/ingest.astro ===
>    - Page with a React component <Uploader />
> 2) === apps/web/src/pages/library.astro ===
>    - Lists recent documents (20) using a React component <LibraryList />
> 3) === apps/web/src/pages/doc/[id].astro ===
>    - Document detail page. Shows fields and a “Open File” link using signed URL.
> 4) === apps/web/src/components/Uploader.tsx ===
>    - Drag/drop + file picker
>    - For each file:
>      - compute sha256 in browser (use crypto.subtle.digest)
>      - call uploadDocumentFile(file, sha256)
>      - call createDocumentRecord with { sha256, mime, size_bytes, bucket, path, title:file.name, source:'upload', status:'new' }
>      - show a success list with created document IDs linking to /doc/{id}
> 5) === apps/web/src/components/LibraryList.tsx ===
>    - Calls listDocuments({limit:20})
>    - Renders DocumentCard list linking to /doc/{id}
> 6) === apps/web/src/components/DocDetail.tsx ===
>    - Fetches doc by id
>    - Creates signed URL and shows “Open File”
> 7) === apps/web/src/components/DocumentCard.tsx === minimal card
> 8) === apps/web/src/env.d.ts === for import.meta.env typing
> 
> Constraints:
> - Use packages/sdk for all Supabase calls.
> - No server-side API routes required. Client-only is OK for now.
> - Keep styling basic (Tailwind optional; if used, include minimal setup notes in README only, not extra files unless requested).
> - Handle errors visibly.
> Output only the files.
> ```
> 
> ---
> 
> ## Prompt 4 (Worker skeleton: job queue + processing stub)
> Even if you don’t turn it on today, scaffold it so you’re not rebuilding later.
> 
> ```text
> Create a Cloudflare Worker app skeleton at apps/worker that will later process ingestion jobs.
> 
> Deliverables:
> 1) === apps/worker/wrangler.toml ===
>    - placeholders for name, compatibility_date
>    - placeholders for QUEUE binding called INGEST_QUEUE
>    - env vars placeholders for SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY
> 2) === apps/worker/src/index.ts ===
>    - Exports queue handler and fetch handler
>    - Queue message type: { document_id: string }
>    - On message:
>      - mark document status = 'processing'
>      - (stub) pretend to extract text
>      - mark status = 'ready'
>      - record an event in events table: kind='system', title='Processed document', occurred_at=now, doc_id
>    - Uses Supabase REST calls with service role (no supabase-js required, keep it simple):
>      - POST/PATCH via fetch to Supabase REST endpoints
>      - Include apikey and Authorization Bearer service key
> 3) === apps/worker/src/supabase_rest.ts ===
>    - tiny helper for REST calls (select/update/insert) with error handling
> 
> Keep it minimal, working, and with placeholders.
> Output only the files.
> ```
> 
> ---
> 
> ## Prompt 5 (Root workspace plumbing: turbo + workspace + .env.example)
> This is the glue so the repo doesn’t act like a feral cat.
> 
> ```text
> Create the root workspace plumbing files for a pnpm + turborepo monorepo.
> 
> Deliverables:
> 1) === pnpm-workspace.yaml ===
>    - include apps/* and packages/*
> 2) === turbo.json ===
>    - tasks: dev, build, lint
>    - dev: persistent true, cache false
> 3) === package.json === (root)
>    - private true
>    - packageManager pnpm
>    - scripts:
>      - dev: turbo run dev
>      - build: turbo run build
>      - lint: turbo run lint
> 4) === .env.example ===
>    - PUBLIC_SUPABASE_URL=
>    - PUBLIC_SUPABASE_ANON_KEY=
>    - SUPABASE_URL=
>    - SUPABASE_SERVICE_ROLE_KEY=
> 5) === packages/config/tsconfig.base.json === minimal
> 6) === packages/config/biome.json === minimal (or eslint config if you prefer, pick one)
> 
> Assume apps/web already has Astro config. Keep minimal and working.
> Output only the files.
> ```
> 
> ---
> 
> # What you will have after these prompts
> Today, you’ll get:
> - `/ingest` upload UI
> - `/library` list UI
> - `/doc/:id` detail + signed “open file”
> - Supabase tables + RLS
> - Storage bucket usage
> - Worker skeleton ready for later
> 
> That’s the “I can breathe now” baseline.
> 
> ---
> 
> ## Two practical notes (because reality exists)
> 1) **Supabase Storage policies**: you’ll need to set bucket `docs` and allow authenticated read/write. The policies file includes guidance, but you may still have to click once in the dashboard because Supabase loves “security theater.”
> 2) **Dedupe behavior**: unique `sha256` prevents duplicate DB rows. Upload handles “file exists” gracefully.
> 
> ---
> 
> If you run those prompts in order, you’ll be assembling Lego bricks, not summoning a cathedral.

### User
> and why am i not just installing docspell and hosting it?

### Assistant
> Because Docspell is **a whole grown-up document management system**, and what you asked for is **“I want ingestion + searchable truth + links to originals, online, today”**. Those overlap… but they’re not the same thing, and Docspell comes with baggage (the useful kind *and* the annoying kind).
> 
> ### Why you *would* just install Docspell
> If your #1 pain is “I drop PDFs in, it OCRs, it’s searchable, I can tag it, I can find it later” then Docspell is basically **exactly that**.
> 
> Docspell gives you:
> - Web UI + upload + “curate items” workflow (review metadata/tags after ingest).
> - OCR + processing via the **joex** job executor container (it ships with the OCR tooling baked in). citeturn2view0  
> - Full stack docker-compose available (includes **PostgreSQL + full-text search** in the compose setup). citeturn2view0  
> - Optional “integration endpoint” so tools (or automations) can upload with a header secret. citeturn2view0  
> 
> If you want something working **today** with minimal invention, Docspell is the “stop building your own toaster” option.
> 
> ### Why you *wouldn’t* (your actual stated endgame)
> You said:
> > “web app, data online, storage online, if my pc blows up oh well.”
> 
> That means you’re signing up for:
> - Hosting Docspell somewhere (VPS, home server, whatever) **with persistent storage volumes**.
> - Backups (Docspell itself recommends DB backups before upgrading; downgrades aren’t supported). citeturn2view0  
> - Multiple moving parts: restserver + joex + DB + search service, and configuration secrets. citeturn2view0  
> 
> Also: your bigger plan isn’t “a DMS.” You want:
> - **Rules-based triage**
> - **Event registry + timeline views + calendar sync**
> - **Tax return module**
> - A single source of truth across QiOne/QiNote/QiVault
> 
> Docspell won’t magically become your **master event brain**. It’ll be a really good document vault… sitting next to the system you actually need.
> 
> ### The real trade: “Docspell-first” vs “Supabase-first”
> #### Option 1: Docspell-first (fastest relief)
> Use Docspell as your ingestion + OCR + search UI immediately.
> - You upload in the web UI (no folder watching required).
> - Organization is tags/metadata inside Docspell (which you already vibe with).
> - Later, you **pull metadata into Supabase** (or push from Docspell) to power timelines, tax tracking, etc.
> 
> This is the “bandage that actually stops the bleeding” approach.
> 
> #### Option 2: Supabase-first (your unified platform)
> Build your own slim web app:
> - Upload -> Supabase Storage
> - Metadata -> Postgres tables
> - OCR optional (add later)
> - Tags power everything (views, filters, timelines)
> - Events module is native and first-class
> 
> This is cleaner for your long-term architecture, but it’s slower to reach “it just works.”
> 
> ### Why not Tauri/Electron right now?
> Because you *just* decided you don’t need folder watching and you want “PC blows up, oh well.” Desktop wrappers mainly matter when you need filesystem privileges and offline/local workflows. If ingestion is **web upload** and storage is **online**, a desktop shell is extra complexity cosplay.
> 
> ### What I recommend (no fantasies, just outcome)
> **Docspell-first for ingestion + search, Supabase for your “master registry” layer.**
> - Docspell handles: “Is this in here? What does it say? Show me the PDF.”
> - Supabase handles: “This belongs to Case FCFCU, Phase C-02, Event type ‘Filing’, date X, linked docs A/B/C, timeline view, reminders, calendar sync.”
> 
> Docspell becomes your *document engine*. Supabase becomes your *truth model*.
> 
> ### Your “year/month folder” question
> In a Supabase-first world: default it to **upload date** (stable, always present).
> In a Docspell-first world: you can still *display* year/month based on upload/ingest timestamp, regardless of where the blob lives. (Your “organization is tags” instinct is right: physical blob location should be irrelevant most of the time.)
> 
> If you want the blunt answer: you’re not “just installing Docspell” because you don’t want *a document app*. You want *an operating system*. Docspell can be a component of that, not the whole thing.

### User
> ok im building give me the document about this chat

### Assistant
> Your session artifact is ready:
> 
> **Download here:**  
> [QiVault_Web_First_Architecture_Decision_Artifact.zip](sandbox:/mnt/data/QiVault_Web_First_Architecture_Decision_Artifact.zip)
> 
> This locks in the architecture decisions so future-you doesn’t try to rebuild Docspell at 2:17 AM because Turbo yelled at you again.
