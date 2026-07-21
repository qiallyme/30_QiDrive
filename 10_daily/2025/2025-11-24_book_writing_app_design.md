---
layout: page
title: "Book writing app design"
slug: "book_writing_app_design"
created_at: "2025-11-24 15:11:39"
updated_at: "2026-07-18T11:03:12-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-001.json"
template_key: master-template
date: 2025-11-24
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6924c922-f12c-832d-b130-98c786e07821"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Book writing app design

## Overview
- **Date**: 2025-11-24 15:11:39
- **Conversation ID**: `6924c922-f12c-832d-b130-98c786e07821`
- **Source**: `Chat-Export-28513-2026/conversations-001.json`

## Chat History

### User
> let build a book writting app, heres what it will do, i can dump chat logs, activity history, calendar events, notes, jorunals, videos, pdfs, etc. and give the ai a prompt that asks, what is the books focus, the arc, what the purpose is, the intended audience, the tone, etc, etc, it will ask the order, how long, how many chapters, ect, then it will create a full book with chapters, and sections, prologues ect, and it will create an outline first for approval, the subtopics of each major chapter or point/topic, then it will organize the raw data accordingly find key thems and assets then provide a very short sample of content for each part for approval once approved it will take the ocntext of the content, the summaries, then interavily and reinforcingly write sections, review, update oultine get approvale then add the approved section as the context for the section now ignoring the raw content replacing it with the final draft section that will not be added to the rest of the raw content and so on until there is a full and amazing final book non-fiction or whatever depending on the request.

### Assistant
> Cool, so you want an app that eats your entire digital life, turns it into an organized narrative, and doesn’t accidentally fuse your grocery list into Chapter 7. Totally normal. Let’s design it properly so it’s not another “AI magic happens here” corpse of a project.
> 
> Here’s a tight, buildable blueprint for a **Book Writing / Life-to-Manuscript** app.
> 
> ---
> 
> ## 1) Core Product Idea (what this thing *is*)
> A guided pipeline that:
> 1. **Ingests raw personal data** (chat logs, notes, journals, calendar, PDFs, videos, etc.)
> 2. **Extracts themes + timeline + entities**
> 3. **Builds a book proposal + outline**
> 4. **Runs an approval loop**
> 5. **Generates drafts chapter-by-chapter**
> 6. **Locks approved text into “final context”**
> 7. Repeats until full manuscript + export
> 
> Key design rule: **raw data is evidence; approved draft becomes truth.**  
> So the AI doesn’t keep re-litigating old logs once a section is finalized.
> 
> ---
> 
> ## 2) MVP Scope (so you actually ship)
> ### MVP v0.1 features
> **Ingestion**
> - Upload: `.txt/.md`, `.pdf`, `.docx`, `.json` (chat exports), `.ics` (calendar), images for OCR
> - Manual paste box for quick dumps
> - Folder/vault picker if local-first
> 
> **Library & Index**
> - Auto-chunking + embeddings
> - Basic metadata editor (date, source, people, tags)
> - Search + filters
> 
> **Book Builder Wizard**
> - Prompt interview: focus, arc, purpose, tone, audience, length, chapter count, POV, etc.
> - Generates:
>   - book proposal (1–2 pages)
>   - outline (chapters + subtopics)
>   - “evidence map” (which raw chunks support which chapter)
> 
> **Approval Loop**
> - Outline approval UI (accept/edit/reorder)
> - Chapter “micro-sample” approval (tiny draft per section)
> - Then full section drafting
> 
> **Drafting Studio**
> - One chapter at a time
> - Inline comments / revision requests
> - “Approve & lock” button
> 
> **Export**
> - Markdown + DOCX + PDF
> - Outline + evidence appendix optional
> 
> That’s enough to be useful without turning into a self-aware publishing house.
> 
> ---
> 
> ## 3) System Architecture (practical, not cosplay)
> ### Components
> 1. **Client App (PWA/desktop-friendly)**
>    - Library view
>    - Outline editor
>    - Drafting studio
> 
> 2. **Ingestion & Processing Worker**
>    - OCR / transcription jobs
>    - Chunk + embed
>    - Metadata extraction
> 
> 3. **Vector Store + Metadata DB**
>    - Store chunks + embeddings
>    - Track provenance + approvals
> 
> 4. **Orchestrator (“Book Engine”)**
>    - Runs the multi-step writing loop
>    - Maintains state machine
> 
> ### Recommended stack (aligned with your usual vibe)
> - **Frontend:** React + Vite + Tailwind
> - **Backend:** Cloudflare Workers + Durable Objects (stateful flows)
> - **DB:** Cloudflare D1 (metadata) + Vectorize (embeddings)
> - **Files:** R2 bucket
> - **Optional local-first cache:** SQLite/DuckDB mirror for hot data
> 
> Yes, it’s modular, cheap, and won’t randomly bill you $900 for breathing.
> 
> ---
> 
> ## 4) Data Model (so the AI doesn’t hallucinate structure)
> Think in three layers: **Raw → Structured → Final**
> 
> ### Tables / Collections
> **raw_items**
> - id
> - type (chat, journal, calendar, pdf, video, note, image)
> - source_name
> - created_at / imported_at
> - text_content (or pointer to transcript/OCR)
> - file_ref (R2 key)
> - metadata_json (people, places, tags, etc.)
> 
> **chunks**
> - id
> - raw_item_id
> - chunk_text
> - embedding_vector
> - chunk_order
> - extracted_entities_json
> - timestamp_range (if detectable)
> 
> **book_projects**
> - id
> - title_working
> - focus
> - arc
> - audience
> - tone
> - pov
> - length_target
> - chapter_count
> - status (proposing / outlining / drafting / revising / done)
> 
> **outline_nodes**
> - id
> - book_id
> - parent_id (null for chapters)
> - node_type (prologue, chapter, section, epilogue)
> - title
> - goal
> - order_index
> - status (proposed / approved / locked)
> 
> **evidence_links**
> - id
> - outline_node_id
> - chunk_id
> - relevance_score
> - note
> 
> **draft_sections**
> - id
> - outline_node_id
> - draft_text
> - draft_version
> - status (sample / drafted / revised / approved / locked)
> - editor_notes
> 
> **final_context**
> - book_id
> - stitched_text (or list of approved draft_sections)
> - last_updated
> 
> This is the “approved text replaces raw context” rule made real.
> 
> ---
> 
> ## 5) The Book Engine (state machine)
> You want deterministic stages, not vibes.
> 
> ### States
> 1. **INGESTING**
> 2. **ANALYZING**
>    - timeline extraction
>    - theme clustering
>    - entity graph
> 3. **INTERVIEWING**
>    - asks user book-shaping questions
> 4. **PROPOSING**
>    - outputs focus/arc/purpose/audience/tone doc
> 5. **OUTLINING**
>    - outputs structure
> 6. **OUTLINE_APPROVAL**
> 7. **EVIDENCE_MAPPING**
> 8. **MICRO_SAMPLING**
>    - 1–3 paragraphs per section
> 9. **SAMPLE_APPROVAL**
> 10. **DRAFTING_SECTION**
> 11. **SECTION_REVIEW**
> 12. **LOCK_SECTION**
>    - move draft into final_context
> 13. loop 10–12 until done
> 14. **MANUSCRIPT_REVIEW**
> 15. **EXPORTING**
> 
> Durable Object holds the book’s current state + pointers to where you are.
> 
> ---
> 
> ## 6) Prompting Strategy (the secret sauce)
> You don’t want one mega-prompt. You want **prompt packets** per stage.
> 
> ### A. Interview Prompt (structured Q&A)
> System message:  
> - You are a book architect. Ask only necessary questions.  
> - Return answers as JSON.
> 
> Output JSON like:
> ```json
> {
>   "focus": "...",
>   "arc": ["Phase 1", "Phase 2", "Phase 3"],
>   "purpose": "...",
>   "audience": "...",
>   "tone": ["candid", "hopeful"],
>   "length_target_words": 65000,
>   "chapter_count": 12,
>   "pov": "first",
>   "constraints": ["no real names", "avoid medical detail"]
> }
> ```
> 
> ### B. Outline Prompt
> Inputs:
> - interview JSON
> - top themes summary
> - timeline beats
> - any user constraints
> 
> Output:
> - outline_nodes list with goals + ordering
> 
> ### C. Evidence Map Prompt
> Inputs:
> - outline
> - theme clusters
> - top chunks per theme
> 
> Output:
> - evidence_links (chapter ↔ chunk matches)
> 
> ### D. Micro-sample Prompt
> Inputs:
> - one outline node
> - its evidence chunks (only)
> - tone + pov rules
> - things to avoid
> 
> Output:
> - tiny sample + bullet list of what fullest section will cover
> 
> ### E. Draft Prompt (iterative)
> Inputs:
> - outline node
> - evidence chunks
> - **final_context so far** (to keep continuity)
> - user-approved micro-sample (as guidance)
> 
> Output:
> - full section draft
> 
> ### F. Review Prompt
> Inputs:
> - drafted section
> - outline goal
> - continuity constraints
> 
> Output:
> - revision suggestions + risk flags (e.g., “this contradicts Chapter 2”)
> 
> ---
> 
> ## 7) UI Flow (what the human actually sees)
> ### Screens
> 1. **Library**
>    - upload/paste
>    - ingestion status
>    - filter by source/date/type
> 
> 2. **Book Projects**
>    - new project wizard
>    - list of projects
> 
> 3. **Outline Studio**
>    - drag/drop hierarchy
>    - approve/edit buttons
>    - show attached evidence count per node
> 
> 4. **Samples Review**
>    - card per section
>    - approve / ask rewrite / edit manually
> 
> 5. **Drafting Studio**
>    - left: outline tree + progress
>    - center: draft editor
>    - right: evidence viewer (read-only)
>    - buttons: revise, approve & lock, regenerate (with reason)
> 
> 6. **Manuscript View**
>    - stitched final text
>    - export options
> 
> ---
> 
> ## 8) Safety / Reality Checks (so it doesn’t ruin your life)
> - **Provenance always visible.** Every paragraph should trace to evidence or be clearly labeled “inferred.”
> - **Personal data boundary:** local-first option by default. Cloud sync opt-in only.
> - **Copyright / 3rd-party text:** if you ingest books/articles, AI should summarize, not paste them. The app should warn you when a chunk looks copyrighted.
> - **Delusion-safe writing:** if raw logs contain paranoia/false beliefs, drafting prompt must treat them as *experiences*, not facts (e.g., “I felt watched” vs “they were watching me”).
> 
> ---
> 
> ## 9) Build Plan (brutally realistic)
> ### Phase 1: Skeleton (1 week of real work)
> - Library UI + upload
> - Store raw_items in DB + files in R2
> - Chunking + embeddings worker
> - Search
> 
> ### Phase 2: Book Wizard + Outline (1–2 weeks)
> - Interview flow
> - Theme/timeline extraction
> - Outline generation
> - Approval UI
> 
> ### Phase 3: Evidence Map + Samples (1–2 weeks)
> - Evidence linking
> - Micro-samples
> - Sample approval loop
> 
> ### Phase 4: Drafting Loop (2–4 weeks)
> - Section drafting
> - Review/regenerate
> - Locking into final_context
> - Manuscript stitching
> 
> ### Phase 5: Export polish (few days)
> - DOCX/PDF export
> - Appendix options
> 
> ---
> 
> ## 10) Extra features you’ll want next (not MVP)
> - Multi-book “universe” mode (reuse evidence across projects)
> - Character/people anonymizer (“Luis” → “L.” globally)
> - Timeline visualizer with chapter overlays
> - Style mimic presets (memoir, business, spiritual, academic)
> - Co-author mode for interviews
> - Voice dictation directly into evidence
> 
> ---
> 
> If you want, next step is I can spit out:
> 1. A repo folder structure that matches your QiOS/QiNote style  
> 2. The exact Durable Object state schema + Worker routes  
> 3. The UI component map (React routes + views)  
> 
> But I’m not going to ask you to “clarify requirements” because you already did. This is enough to start cutting code instead of dreaming about it.

### User
> go ahead and give me the full details dev docs techinical which i will drop into cursor and see how it does.

### Assistant
> Alright, here’s your full technical dev doc in **strict Markdown** so you can yeet it into Cursor and watch the sparks fly. I’m not babysitting it after, but this is a real spec, not a Pinterest vision board.
> 
> ```markdown
> ---
> date: 2025-11-24
> title: Book Writing App (Life-to-Manuscript Engine) - Technical Dev Docs
> category: Development
> keywords: BookEngine, RAG, Cloudflare, Vectorize, DurableObjects
> project_context: QiBook (Book Writing App)
> ---
> 
> # Book Writing App (Life-to-Manuscript Engine)
> A local-first + cloud-orchestrated AI book-writing system that ingests raw personal data, generates an approved outline, maps evidence, drafts iteratively, and locks approved text into final context until a complete manuscript is produced.
> 
> ---
> 
> ## 1. Product Goals & Non-Goals
> 
> ### Goals
> - Ingest heterogeneous personal data (chat logs, journals, notes, calendar, PDFs, videos, images).
> - Auto-structure into themes, timeline beats, entities.
> - Guide user through an interview to shape the book (focus, arc, tone, audience, length, structure).
> - Generate outline for approval.
> - Evidence-map raw chunks to outline nodes.
> - Draft per-section with micro-sample approvals.
> - “Approve & Lock” sections into final manuscript context.
> - Export finished manuscript (MD, DOCX, PDF).
> 
> ### Non-Goals (v0.x)
> - Real-time collaborative editing.
> - Full authoring suite replacement (Scrivener-tier).
> - Auto publishing/distribution.
> - Full graph UI (optional later).
> 
> ---
> 
> ## 2. High-Level Architecture
> 
> ### 2.1 Components
> 1. **Client App (React PWA)**
>    - Library / Ingestion UI
>    - Book Project Wizard
>    - Outline Studio
>    - Evidence Viewer
>    - Drafting Studio
>    - Manuscript Viewer & Export
> 
> 2. **Ingestion Worker (Cloudflare Worker)**
>    - Handles uploads + metadata
>    - OCR/transcription job queue
>    - Chunking + embeddings
>    - Stores raw items in R2 and metadata in D1
>    - Writes embeddings to Vectorize index
> 
> 3. **Vector Store**
>    - Cloudflare Vectorize: semantic retrieval for chunks.
> 
> 4. **Metadata DB**
>    - Cloudflare D1: raw_items, chunks, projects, outline_nodes, evidence_links, drafts.
> 
> 5. **Book Engine Orchestrator**
>    - Cloudflare Durable Object holding per-book state machine.
>    - Calls LLM in staged prompt packets.
>    - Writes outputs to D1.
> 
> ### 2.2 Data Flow
> Ingestion → Chunk+Embed → Theme/Timeline extraction → Interview → Proposal → Outline → Approval → Evidence map → Micro-samples → Approval → Draft+Review → Lock → Loop → Manuscript review → Export.
> 
> ### 2.3 Key Rule
> **Raw data is evidence. Approved drafts are truth.**
> Once a section is approved, raw evidence for that section is no longer included in future drafting context, to avoid recontamination / contradictions.
> 
> ---
> 
> ## 3. Repo Structure (QiOS-friendly)
> 
> ```
> qibook/
>   apps/
>     web/                         # React client
>       src/
>         routes/
>         components/
>         features/
>         lib/
>         styles/
>       public/
>       vite.config.ts
>       package.json
>   workers/
>     api/                         # Cloudflare Worker API
>       src/
>         routes/
>         services/
>         prompts/
>         utils/
>         index.ts
>       wrangler.toml
>   durable/
>     book-engine/                 # Durable Object orchestrator
>       src/
>         engine.ts
>         state.ts
>         prompts/
>         index.ts
>       wrangler.toml
>   db/
>     schema.sql                   # D1 schema
>     migrations/
>   shared/
>     types/
>       index.ts
>     constants/
>     validators/
>   scripts/
>     local_ingest.py              # optional local-first ingest tooling
>     export_docx.py               # export helpers
>   README.md
> ```
> 
> ---
> 
> ## 4. Database Schema (D1)
> 
> > Use migrations. Keep JSON columns for flexibility.
> 
> ### 4.1 raw_items
> Stores uploaded/hydrated sources.
> 
> ```sql
> CREATE TABLE raw_items (
>   id TEXT PRIMARY KEY,
>   type TEXT NOT NULL,               -- chat | journal | calendar | pdf | video | note | image | audio
>   source_name TEXT,
>   title TEXT,
>   created_at TEXT,                  -- original creation time if detectable
>   imported_at TEXT NOT NULL,
>   text_content TEXT,                -- OCR/transcript/extracted text
>   file_ref TEXT,                    -- R2 key
>   metadata_json TEXT                -- JSON: {people, tags, language, etc.}
> );
> ```
> 
> ### 4.2 chunks
> Vectorized segments derived from raw_items.
> 
> ```sql
> CREATE TABLE chunks (
>   id TEXT PRIMARY KEY,
>   raw_item_id TEXT NOT NULL,
>   chunk_text TEXT NOT NULL,
>   chunk_order INTEGER,
>   embedding_id TEXT,                -- Vectorize doc id
>   extracted_entities_json TEXT,     -- JSON: {people, places, topics}
>   timestamp_range_json TEXT,        -- JSON: {start, end}
>   FOREIGN KEY(raw_item_id) REFERENCES raw_items(id)
> );
> ```
> 
> ### 4.3 book_projects
> Root record per book.
> 
> ```sql
> CREATE TABLE book_projects (
>   id TEXT PRIMARY KEY,
>   working_title TEXT NOT NULL,
>   focus TEXT,
>   arc_json TEXT,                    -- JSON array
>   purpose TEXT,
>   audience TEXT,
>   tone_json TEXT,                   -- JSON array
>   pov TEXT,                         -- first | third | mixed
>   length_target_words INTEGER,
>   chapter_count INTEGER,
>   constraints_json TEXT,            -- JSON array
>   status TEXT NOT NULL,             -- proposing | outlining | drafting | revising | done
>   created_at TEXT NOT NULL,
>   updated_at TEXT NOT NULL
> );
> ```
> 
> ### 4.4 outline_nodes
> Hierarchical outline tree.
> 
> ```sql
> CREATE TABLE outline_nodes (
>   id TEXT PRIMARY KEY,
>   book_id TEXT NOT NULL,
>   parent_id TEXT,
>   node_type TEXT NOT NULL,          -- prologue | chapter | section | epilogue | appendix
>   title TEXT NOT NULL,
>   goal TEXT,
>   order_index INTEGER NOT NULL,
>   status TEXT NOT NULL,             -- proposed | approved | locked
>   metadata_json TEXT,               -- JSON: {word_target, style_notes}
>   FOREIGN KEY(book_id) REFERENCES book_projects(id),
>   FOREIGN KEY(parent_id) REFERENCES outline_nodes(id)
> );
> ```
> 
> ### 4.5 evidence_links
> Many-to-many mapping outline nodes to chunks.
> 
> ```sql
> CREATE TABLE evidence_links (
>   id TEXT PRIMARY KEY,
>   outline_node_id TEXT NOT NULL,
>   chunk_id TEXT NOT NULL,
>   relevance_score REAL,
>   note TEXT,
>   FOREIGN KEY(outline_node_id) REFERENCES outline_nodes(id),
>   FOREIGN KEY(chunk_id) REFERENCES chunks(id)
> );
> ```
> 
> ### 4.6 draft_sections
> Versioned drafts for nodes.
> 
> ```sql
> CREATE TABLE draft_sections (
>   id TEXT PRIMARY KEY,
>   outline_node_id TEXT NOT NULL,
>   draft_text TEXT NOT NULL,
>   draft_version INTEGER NOT NULL,
>   status TEXT NOT NULL,             -- sample | drafted | revised | approved | locked
>   editor_notes TEXT,
>   created_at TEXT NOT NULL,
>   FOREIGN KEY(outline_node_id) REFERENCES outline_nodes(id)
> );
> ```
> 
> ### 4.7 final_context
> Stitched approved text.
> 
> ```sql
> CREATE TABLE final_context (
>   book_id TEXT PRIMARY KEY,
>   stitched_text TEXT,
>   updated_at TEXT NOT NULL,
>   FOREIGN KEY(book_id) REFERENCES book_projects(id)
> );
> ```
> 
> ---
> 
> ## 5. Vectorize Index
> - Index name: `qibook_chunks`
> - Document id = chunks.embedding_id
> - Payload fields:
>   - chunk_id
>   - raw_item_id
>   - type
>   - created_at
>   - title
>   - tags
> - Use topK = 20 by default.
> 
> ---
> 
> ## 6. API (Worker)
> 
> ### 6.1 Routes
> 
> #### Ingestion
> - `POST /api/raw-items/upload`
>   - multipart upload
>   - stores file to R2
>   - creates raw_items record
>   - enqueues processing job
> 
> - `POST /api/raw-items/paste`
>   - { type, source_name, title, text_content, created_at? }
> 
> - `GET /api/raw-items`
>   - filters: type, date range, tags, search
> 
> - `GET /api/raw-items/:id`
> 
> #### Processing
> - `POST /api/process/:raw_item_id`
>   - run extract → chunk → embed → store
>   - can be internally triggered by queue
> 
> #### Book Projects
> - `POST /api/books`
>   - { working_title }
> 
> - `GET /api/books`
> - `GET /api/books/:id`
> - `PATCH /api/books/:id`
>   - update interview answers, status, etc.
> 
> #### Outline
> - `GET /api/books/:id/outline`
> - `POST /api/books/:id/outline/generate`
> - `PATCH /api/outline/:node_id`
> - `POST /api/outline/:node_id/reorder`
> 
> #### Evidence
> - `POST /api/books/:id/evidence/map`
> - `GET /api/outline/:node_id/evidence`
> 
> #### Drafting
> - `POST /api/outline/:node_id/sample`
> - `POST /api/outline/:node_id/draft`
> - `POST /api/outline/:node_id/review`
> - `POST /api/outline/:node_id/approve`
> - `POST /api/outline/:node_id/lock`
> 
> #### Manuscript
> - `GET /api/books/:id/manuscript`
> - `POST /api/books/:id/export`
>   - { format: md|docx|pdf }
> 
> ---
> 
> ## 7. Ingestion Pipeline
> 
> ### 7.1 File Types
> - **Text**: txt, md, json, csv
> - **Docs**: pdf, docx
> - **Calendar**: ics
> - **Media**: mp4, mov, mp3, wav
> - **Images**: png, jpg (OCR)
> 
> ### 7.2 Steps
> 1. **Extract text**
>    - pdf/docx: text extraction
>    - images: OCR
>    - audio/video: transcription
> 
> 2. **Chunk**
>    - target 500-1200 tokens per chunk
>    - overlap 50-100 tokens
>    - chunk_order assigned sequentially
>    - attempt timestamp inference for chats/calendars/journals
> 
> 3. **Embed**
>    - call embeddings endpoint
>    - upsert to Vectorize with embedding_id
> 
> 4. **Entity/theme pre-pass**
>    - fast LLM pass per raw_item to extract:
>      - people
>      - places
>      - topics
>      - sentiment/energy
>      - time markers
> 
> ---
> 
> ## 8. Book Engine Durable Object
> 
> ### 8.1 State Machine
> ```ts
> type EngineState =
>   | "INGESTING"
>   | "ANALYZING"
>   | "INTERVIEWING"
>   | "PROPOSING"
>   | "OUTLINING"
>   | "OUTLINE_APPROVAL"
>   | "EVIDENCE_MAPPING"
>   | "MICRO_SAMPLING"
>   | "SAMPLE_APPROVAL"
>   | "DRAFTING_SECTION"
>   | "SECTION_REVIEW"
>   | "LOCK_SECTION"
>   | "MANUSCRIPT_REVIEW"
>   | "EXPORTING"
>   | "DONE";
> ```
> 
> ### 8.2 Stored State (Durable Object)
> ```ts
> interface BookEngineState {
>   bookId: string;
>   currentState: EngineState;
>   outlineCursorNodeId?: string;   // node being worked on
>   lastActionAt: string;
>   pendingUserApproval: null | {
>     type: "outline" | "sample" | "draft";
>     nodeId?: string;
>     payloadRef: string;           // pointer to D1 record
>   };
>   runHistory: Array<{
>     state: EngineState;
>     startedAt: string;
>     endedAt?: string;
>     status: "ok" | "error";
>     errorMsg?: string;
>   }>;
> }
> ```
> 
> ### 8.3 Engine Methods
> - `analyzeBook(bookId)`
>   - builds theme clusters + timeline + top entities
> - `runInterview(bookId)`
>   - generates structured Q&A
> - `generateProposal(bookId)`
> - `generateOutline(bookId)`
> - `awaitOutlineApproval(bookId)`
> - `mapEvidence(bookId)`
> - `createMicroSample(nodeId)`
> - `awaitSampleApproval(nodeId)`
> - `draftSection(nodeId)`
> - `reviewSection(nodeId)`
> - `approveSection(nodeId)`
> - `lockSection(nodeId)`
> - `stitchManuscript(bookId)`
> - `exportManuscript(bookId, format)`
> 
> ### 8.4 Loop Logic
> Pseudo:
> ```ts
> while (exists outline_node where status != "locked") {
>   node = next approved node not locked
>   sample = createMicroSample(node)
>   await approval
>   draft = draftSection(node)
>   review = reviewSection(node)
>   await approval/revision
>   lockSection(node)
> }
> stitchManuscript()
> ```
> 
> ---
> 
> ## 9. Prompt Packets (LLM)
> 
> > Prompts should live in `workers/api/src/prompts` and `durable/book-engine/src/prompts`.
> > Each stage uses *only required inputs*.
> 
> ### 9.1 Theme + Timeline Extraction
> **Input:** top N chunks by recency/diversity  
> **Output JSON:**
> ```json
> {
>   "themes": [
>     {"name":"Identity & Belonging","summary":"...","supporting_chunk_ids":[...]},
>     {"name":"Resets & Reinvention","summary":"...","supporting_chunk_ids":[...]}
>   ],
>   "timeline_beats": [
>     {"date":"2018-06","event":"Moved to X","chunk_ids":[...]},
>     {"date":"2021-03","event":"Business launch","chunk_ids":[...]}
>   ],
>   "entities": {
>     "people":[{"name":"Ron","aliases":["R."],"chunk_ids":[...]}],
>     "places":[...],
>     "orgs":[...]
>   }
> }
> ```
> 
> ### 9.2 Interview Prompt
> System:
> - You are a book architect.
> - Ask only necessary questions.
> - Return JSON.
> User:
> - Provide Qs sequentially or single batch.
> 
> Output:
> ```json
> {
>   "focus": "...",
>   "arc": ["Phase 1","Phase 2","Phase 3"],
>   "purpose": "...",
>   "audience": "...",
>   "tone": ["candid","hopeful"],
>   "length_target_words": 65000,
>   "chapter_count": 12,
>   "pov": "first",
>   "constraints": ["no legal advice tone", "anonymize names"]
> }
> ```
> 
> ### 9.3 Proposal Prompt
> Input:
> - interview JSON
> - themes/timeline/entities summary
> 
> Output markdown:
> - working title
> - 1-2 page proposal
> - promise to reader
> - structure overview
> 
> ### 9.4 Outline Prompt
> Input:
> - interview JSON
> - proposal summary
> - themes
> - timeline beats
> 
> Output JSON list:
> ```json
> [
>   {
>     "node_type":"prologue",
>     "title":"...",
>     "goal":"...",
>     "order_index":0,
>     "children":[]
>   },
>   {
>     "node_type":"chapter",
>     "title":"Chapter 1: ...",
>     "goal":"...",
>     "order_index":1,
>     "children":[
>       {"node_type":"section","title":"...","goal":"...","order_index":0}
>     ]
>   }
> ]
> ```
> 
> ### 9.5 Evidence Mapping Prompt
> Input:
> - one outline node
> - candidate chunks from Vectorize semantic search (query = node.goal + title)
> 
> Output:
> ```json
> {
>   "outline_node_id":"...",
>   "links":[
>     {"chunk_id":"...","relevance_score":0.91,"note":"key example of conflict"},
>     {"chunk_id":"...","relevance_score":0.78,"note":"supports transition"}
>   ]
> }
> ```
> 
> ### 9.6 Micro-sample Prompt
> Input:
> - node + evidence chunks only
> - tone/pov
> 
> Output:
> - 1-3 paragraphs sample
> - bullets of full-section plan
> - risks/ambiguities list
> 
> ### 9.7 Draft Prompt
> Input:
> - node
> - evidence chunks
> - **final_context so far**
> - approved micro-sample
> 
> Output:
> - full section draft markdown
> 
> ### 9.8 Review Prompt
> Input:
> - draft
> - node goal
> - continuity rules
> 
> Output JSON:
> ```json
> {
>   "issues":[{"type":"continuity","detail":"contradicts Chapter 2"}],
>   "revision_suggestions":[ "...", "..." ],
>   "quality_score": 0-100
> }
> ```
> 
> ---
> 
> ## 10. Client App UX / Routes
> 
> ### Routes
> - `/library`
> - `/books`
> - `/books/:id/wizard`
> - `/books/:id/outline`
> - `/books/:id/samples`
> - `/books/:id/draft/:nodeId`
> - `/books/:id/manuscript`
> 
> ### Key Components
> - `LibraryUploader`
> - `RawItemTable`
> - `BookWizard`
> - `OutlineTreeEditor`
> - `EvidencePanel`
> - `SampleCards`
> - `DraftEditor`
> - `ManuscriptViewer`
> - `ExportDialog`
> 
> ### Drafting Studio Layout
> - Left: Outline Tree + Progress
> - Center: Editor (current draft)
> - Right: Evidence (read-only chunks list + citations)
> 
> ---
> 
> ## 11. Approval & Locking Semantics
> 
> ### Approve Outline
> - status: `proposed -> approved`
> - DO engine proceeds to evidence mapping.
> 
> ### Approve Sample
> - draft_sections.status: `sample -> approved`
> - engine can draft full section using micro-sample as style anchor.
> 
> ### Approve Draft
> - draft_sections.status: `drafted/revised -> approved`
> - once approved, user can “Lock Section.”
> 
> ### Lock Section (critical)
> 1. outline_nodes.status = `locked`
> 2. latest approved draft_sections.status = `locked`
> 3. final_context.stitched_text is regenerated by concatenating all locked sections in outline order.
> 4. **Future drafts receive only stitched_text, not raw evidence from locked nodes.**
> 
> ---
> 
> ## 12. Export
> 
> ### Markdown
> - use stitched_text as canonical.
> - include YAML front matter for book.
> 
> ### DOCX / PDF
> - server-side export using a worker-compatible renderer or an offline script.
> - For v0.x: allow “Export MD then convert locally” fallback.
> 
> ---
> 
> ## 13. Error Handling & Observability
> 
> ### Logs to store per book
> - state transitions with timestamps
> - last 5 errors
> - current queue of unfinished nodes
> - evidence mapping coverage (% of nodes with >=3 chunks)
> 
> ### Failure Modes
> - OCR/transcription failure: raw_item stays “text_content null” with retry.
> - Embedding error: chunk flagged “embedding_id null” + retry.
> - Outline hallucination: user edits and re-approves; engine continues from new outline.
> - Contradiction in drafts: review prompt must flag.
> 
> ---
> 
> ## 14. Security & Privacy
> 
> - Local-first default. Cloud sync only for selected sources.
> - All raw_items retain provenance. UI shows source per evidence chunk.
> - “Anonymize names” constraint triggers:
>   - pre-pass entity scrub
>   - post-draft redaction pass
> - Avoid reproducing copyrighted third-party text:
>   - If detected long verbatim blocks, auto-rewrite into summary.
> 
> ---
> 
> ## 15. Implementation Checklist
> 
> ### Worker API
> - [ ] R2 upload + raw_items insert
> - [ ] process job (extract/chunk/embed)
> - [ ] Vectorize upsert + search helpers
> - [ ] CRUD for books/outline/drafts
> - [ ] export endpoints
> 
> ### Durable Object
> - [ ] state persistence
> - [ ] analyze → interview → proposal → outline chain
> - [ ] approval waiters (poll D1 or webhook style)
> - [ ] evidence map + micro-sample + draft loops
> - [ ] locking + stitching
> 
> ### Frontend
> - [ ] library UI
> - [ ] wizard UI with JSON answers
> - [ ] outline editor + approval
> - [ ] samples approval
> - [ ] drafting studio + lock button
> - [ ] manuscript view + export
> 
> ---
> 
> ## 16. Future Enhancements (post-MVP)
> - Multi-book universe mode
> - Timeline visualizer overlayed with outline
> - Style presets + per-node voice control
> - Co-author interview mode
> - Graph UI for theme/entity exploration
> - Agentic “chapter planner” that suggests reorder/refocus
> 
> ---
> End of technical spec.
> ```
> 
> There. Full dev docs, no fluff, no “TBD vibes.” If Cursor spins up something cursed, that’s on the robot you hired.

### User
> this will all be local only using local llm etc. please make it local and portable. sorry i forgot to say that.

### Assistant
> Got it. You want **zero cloud, zero remote calls, fully local, portable**. So we rip out Workers/Durable Objects/Vectorize/R2 and replace with a local orchestrator + local stores + local LLM runtime. Here’s the corrected dev doc you can drop into Cursor.
> 
> ```markdown
> ---
> date: 2025-11-24
> title: Book Writing App (Local-Only Life-to-Manuscript Engine) - Technical Dev Docs
> category: Development
> keywords: LocalRAG, SQLite, LocalLLM, Orchestrator, PortableApp
> project_context: QiBook (Local Book Writing App)
> ---
> 
> # Book Writing App (Local-Only Life-to-Manuscript Engine)
> A **fully offline, portable** AI book-writing system that ingests raw personal data, generates an approved outline, maps evidence, drafts iteratively, and locks approved text into final context until a complete manuscript is produced.
> 
> **No cloud services. No external APIs. Everything runs on the user's machine.**
> 
> ---
> 
> ## 1. Product Goals & Non-Goals
> 
> ### Goals
> - Ingest heterogeneous personal data (chat logs, journals, notes, calendar, PDFs, videos, images, audio).
> - Auto-structure into themes, timeline beats, entities.
> - Guided interview to shape book (focus, arc, tone, audience, length, structure).
> - Outline generation for approval.
> - Evidence-map raw chunks to outline nodes.
> - Micro-sample approvals, then full drafting.
> - “Approve & Lock” sections into final manuscript context.
> - Export finished manuscript (MD, DOCX, PDF).
> - **Portable vault**: project is a folder you can move/copy/zip.
> 
> ### Non-Goals (v0.x)
> - Multi-device sync.
> - Real-time collaboration.
> - Publishing/distribution.
> - Heavy graph visualization.
> 
> ---
> 
> ## 2. Local-Only Architecture
> 
> ### 2.1 Components
> 1. **Desktop App UI**
>    - React-based UI
>    - Runs in **Electron** or **Tauri** shell
>    - Talks to local backend over localhost IPC/HTTP
> 
> 2. **Local Backend Orchestrator**
>    - **Python FastAPI** (recommended) or Node backend
>    - Handles ingestion, chunking, embeddings, retrieval, writing loops
>    - Runs as a bundled local service with the app
> 
> 3. **Local Datastores**
>    - **SQLite** for metadata + drafts + outline + state
>    - **Local vector DB** for embeddings:
>      - preferred: **LanceDB** (file-based, fast, portable)
>      - alternatives: **Chroma (persistent)** or **FAISS + SQLite mapping**
> 
> 4. **Local Model Runtimes**
>    - **LLM**: llama.cpp / Ollama / LM Studio (configurable)
>    - **Embeddings**: local embedding model (e.g., BGE, E5, nomic-embed)
>    - **ASR (audio/video)**: Whisper.cpp / faster-whisper local
>    - **OCR (images/PDF scans)**: Tesseract local
>    - **PDF text**: pdfplumber / pymupdf local
>    - **DOCX**: python-docx local
> 
> ### 2.2 Data Flow
> Ingest → Extract text (OCR/ASR if needed) → Chunk → Embed → Store → Analyze themes/timeline/entities → Interview → Proposal → Outline → Approval → Evidence map → Micro-samples → Approval → Draft+Review → Lock → Loop → Manuscript review → Export.
> 
> ### 2.3 Key Rule
> **Raw data is evidence. Approved drafts are truth.**
> Once a section is locked, its raw evidence is excluded from future drafting context.
> 
> ---
> 
> ## 3. Repo Structure (Portable Vault-first)
> 
> ```
> qibook/
>   app/
>     desktop/                      # Electron/Tauri shell + React UI
>       src/
>         routes/
>         components/
>         features/
>         lib/
>       public/
>       package.json
>       vite.config.ts
>   backend/
>     qibook_api/                   # FastAPI service
>       main.py
>       routes/
>       services/
>         ingest.py
>         extract.py
>         chunk.py
>         embed.py
>         retrieval.py
>         engine.py
>         export.py
>       prompts/
>       utils/
>     requirements.txt
>   models/
>     README.md                     # local model placement + config
>   vault/                          # default local data root (portable)
>     projects/
>       <book_id>/
>         raw/
>         chunks/
>         drafts/
>         exports/
>         manifests/
>     global.sqlite                 # optional shared db
>     lancedb/                      # vector store files
>   scripts/
>     run_dev.sh
>     build_portable.sh
>   README.md
> ```
> 
> **Portability rule:** A book project lives under `vault/projects/<book_id>/` and can be moved anywhere.
> 
> ---
> 
> ## 4. SQLite Schema (Local)
> 
> ### 4.1 raw_items
> ```sql
> CREATE TABLE raw_items (
>   id TEXT PRIMARY KEY,
>   type TEXT NOT NULL,               -- chat | journal | calendar | pdf | video | note | image | audio
>   source_name TEXT,
>   title TEXT,
>   created_at TEXT,
>   imported_at TEXT NOT NULL,
>   text_content TEXT,
>   file_path TEXT,                   -- local filesystem path
>   metadata_json TEXT
> );
> ```
> 
> ### 4.2 chunks
> ```sql
> CREATE TABLE chunks (
>   id TEXT PRIMARY KEY,
>   raw_item_id TEXT NOT NULL,
>   chunk_text TEXT NOT NULL,
>   chunk_order INTEGER,
>   embedding_id TEXT,                -- vector db doc id
>   extracted_entities_json TEXT,
>   timestamp_range_json TEXT,
>   FOREIGN KEY(raw_item_id) REFERENCES raw_items(id)
> );
> ```
> 
> ### 4.3 book_projects
> ```sql
> CREATE TABLE book_projects (
>   id TEXT PRIMARY KEY,
>   working_title TEXT NOT NULL,
>   focus TEXT,
>   arc_json TEXT,
>   purpose TEXT,
>   audience TEXT,
>   tone_json TEXT,
>   pov TEXT,
>   length_target_words INTEGER,
>   chapter_count INTEGER,
>   constraints_json TEXT,
>   status TEXT NOT NULL,             -- proposing | outlining | drafting | revising | done
>   created_at TEXT NOT NULL,
>   updated_at TEXT NOT NULL
> );
> ```
> 
> ### 4.4 outline_nodes
> ```sql
> CREATE TABLE outline_nodes (
>   id TEXT PRIMARY KEY,
>   book_id TEXT NOT NULL,
>   parent_id TEXT,
>   node_type TEXT NOT NULL,          -- prologue | chapter | section | epilogue | appendix
>   title TEXT NOT NULL,
>   goal TEXT,
>   order_index INTEGER NOT NULL,
>   status TEXT NOT NULL,             -- proposed | approved | locked
>   metadata_json TEXT,
>   FOREIGN KEY(book_id) REFERENCES book_projects(id),
>   FOREIGN KEY(parent_id) REFERENCES outline_nodes(id)
> );
> ```
> 
> ### 4.5 evidence_links
> ```sql
> CREATE TABLE evidence_links (
>   id TEXT PRIMARY KEY,
>   outline_node_id TEXT NOT NULL,
>   chunk_id TEXT NOT NULL,
>   relevance_score REAL,
>   note TEXT,
>   FOREIGN KEY(outline_node_id) REFERENCES outline_nodes(id),
>   FOREIGN KEY(chunk_id) REFERENCES chunks(id)
> );
> ```
> 
> ### 4.6 draft_sections
> ```sql
> CREATE TABLE draft_sections (
>   id TEXT PRIMARY KEY,
>   outline_node_id TEXT NOT NULL,
>   draft_text TEXT NOT NULL,
>   draft_version INTEGER NOT NULL,
>   status TEXT NOT NULL,             -- sample | drafted | revised | approved | locked
>   editor_notes TEXT,
>   created_at TEXT NOT NULL,
>   FOREIGN KEY(outline_node_id) REFERENCES outline_nodes(id)
> );
> ```
> 
> ### 4.7 final_context
> ```sql
> CREATE TABLE final_context (
>   book_id TEXT PRIMARY KEY,
>   stitched_text TEXT,
>   updated_at TEXT NOT NULL,
>   FOREIGN KEY(book_id) REFERENCES book_projects(id)
> );
> ```
> 
> ---
> 
> ## 5. Local Vector Store (LanceDB preferred)
> 
> ### 5.1 Storage
> - Path: `vault/lancedb/`
> - Table: `chunks`
> - Columns:
>   - embedding (vector)
>   - chunk_id
>   - raw_item_id
>   - type
>   - created_at
>   - title
>   - tags
> 
> ### 5.2 Retrieval
> - Similarity search topK = 20
> - Filter by:
>   - type
>   - date ranges
>   - raw_item_id
>   - tags/entities (if present)
> 
> ---
> 
> ## 6. Local API (FastAPI)
> 
> ### 6.1 Routes
> **Ingestion**
> - `POST /api/raw-items/upload`
> - `POST /api/raw-items/paste`
> - `GET /api/raw-items`
> - `GET /api/raw-items/{id}`
> 
> **Processing**
> - `POST /api/process/{raw_item_id}`
> 
> **Book Projects**
> - `POST /api/books`
> - `GET /api/books`
> - `GET /api/books/{id}`
> - `PATCH /api/books/{id}`
> 
> **Outline**
> - `GET /api/books/{id}/outline`
> - `POST /api/books/{id}/outline/generate`
> - `PATCH /api/outline/{node_id}`
> - `POST /api/outline/{node_id}/reorder`
> 
> **Evidence**
> - `POST /api/books/{id}/evidence/map`
> - `GET /api/outline/{node_id}/evidence`
> 
> **Drafting**
> - `POST /api/outline/{node_id}/sample`
> - `POST /api/outline/{node_id}/draft`
> - `POST /api/outline/{node_id}/review`
> - `POST /api/outline/{node_id}/approve`
> - `POST /api/outline/{node_id}/lock`
> 
> **Manuscript**
> - `GET /api/books/{id}/manuscript`
> - `POST /api/books/{id}/export`
> 
> ---
> 
> ## 7. Ingestion Pipeline (Offline)
> 
> ### 7.1 Extractors
> - **PDF text**: pymupdf or pdfplumber
> - **Scanned PDFs / Images**: Tesseract OCR
> - **Audio / Video**: faster-whisper or whisper.cpp (local)
> - **DOCX**: python-docx
> - **ICS Calendar**: ics + date normalization
> - **Chat exports**: JSON/CSV parser per platform
> 
> ### 7.2 Steps
> 1. Extract text to raw_items.text_content
> 2. Chunk (500–1200 tokens, 50–100 overlap)
> 3. Embed each chunk using local embedding model
> 4. Upsert embeddings to LanceDB and map ids in SQLite
> 5. Quick entity/theme pre-pass per raw_item
> 
> ---
> 
> ## 8. Local Book Engine (Orchestrator)
> 
> ### 8.1 State Machine
> ```py
> ENGINE_STATES = [
>   "INGESTING",
>   "ANALYZING",
>   "INTERVIEWING",
>   "PROPOSING",
>   "OUTLINING",
>   "OUTLINE_APPROVAL",
>   "EVIDENCE_MAPPING",
>   "MICRO_SAMPLING",
>   "SAMPLE_APPROVAL",
>   "DRAFTING_SECTION",
>   "SECTION_REVIEW",
>   "LOCK_SECTION",
>   "MANUSCRIPT_REVIEW",
>   "EXPORTING",
>   "DONE"
> ]
> ```
> 
> ### 8.2 Stored State (SQLite)
> Create a simple table:
> ```sql
> CREATE TABLE engine_state (
>   book_id TEXT PRIMARY KEY,
>   current_state TEXT NOT NULL,
>   outline_cursor_node_id TEXT,
>   pending_approval_json TEXT,
>   run_history_json TEXT,
>   updated_at TEXT NOT NULL
> );
> ```
> 
> ### 8.3 Engine Loop
> ```py
> while has_unlocked_nodes(book_id):
>     node = next_node(book_id)
>     sample = create_micro_sample(node)
>     wait_for_user_approval(sample)
> 
>     draft = draft_section(node)
>     review = review_section(node)
>     wait_for_user_approval(draft, review)
> 
>     lock_section(node)   # stitches into final_context
> stitch_manuscript(book_id)
> ```
> 
> ---
> 
> ## 9. Local Prompt Packets
> 
> ### Model Access
> Your backend should support adapters:
> - `llama.cpp` CLI
> - `ollama` HTTP local
> - `lmstudio` local API
> 
> Expose a single internal call:
> ```py
> llm.generate(prompt, system=None, temperature=0.7, max_tokens=...)
> ```
> 
> ### Stages
> Same packet strategy as before, but inputs come from local DB + local retrieval only:
> 
> 1. Theme + Timeline Extraction ⇒ JSON themes/entities/beats
> 2. Interview Prompt ⇒ JSON book spec
> 3. Proposal Prompt ⇒ markdown proposal
> 4. Outline Prompt ⇒ JSON tree
> 5. Evidence Mapping Prompt ⇒ JSON links from retrieved chunks
> 6. Micro-sample Prompt ⇒ short draft per node
> 7. Draft Prompt ⇒ full section
> 8. Review Prompt ⇒ JSON issues + suggestions
> 
> ---
> 
> ## 10. UI Routes (Desktop)
> 
> - `/library`
> - `/books`
> - `/books/:id/wizard`
> - `/books/:id/outline`
> - `/books/:id/samples`
> - `/books/:id/draft/:nodeId`
> - `/books/:id/manuscript`
> 
> ---
> 
> ## 11. Portability Rules
> 
> A project is portable if:
> - All raw files are referenced by **relative paths inside project folder**.
> - SQLite DB is inside `vault/` or inside the project’s `manifests/`.
> - Vector DB files sit in `vault/lancedb/` and can be rebuilt if missing.
> - Exports live in `projects/<book_id>/exports/`.
> 
> **Optional "Pack Project":**
> - Zip `projects/<book_id>/` + `global.sqlite` subset + embeddings.
> 
> ---
> 
> ## 12. Export (Offline)
> 
> ### Markdown
> - final_context.stitched_text is canonical output.
> 
> ### DOCX / PDF
> - Use local converters:
>   - `pandoc` if installed
>   - python-docx + reportlab fallback
> - The app should detect availability and choose best path.
> 
> ---
> 
> ## 13. Observability (Local)
> 
> - Store per-book logs in SQLite or `projects/<book_id>/manifests/log.jsonl`
> - Track:
>   - state transitions
>   - last errors
>   - queue of nodes
>   - evidence coverage
> 
> ---
> 
> ## 14. Security & Privacy
> 
> - No network calls by default.
> - Explicit toggle required to enable any remote model (future).
> - Raw provenance always available.
> - Draft prompts treat implausible beliefs as experiences, not facts.
> 
> ---
> 
> ## 15. Implementation Checklist
> 
> ### Backend
> - [ ] Local file registry + raw_items insert
> - [ ] Extract text per type
> - [ ] Chunker
> - [ ] Local embeddings + LanceDB upsert
> - [ ] Retrieval helpers
> - [ ] Book Engine state machine
> - [ ] CRUD for books/outline/drafts/evidence
> - [ ] Local export pipeline
> 
> ### Desktop UI
> - [ ] Library uploader + status
> - [ ] Wizard + interview JSON
> - [ ] Outline editor + approval
> - [ ] Samples review
> - [ ] Drafting studio + lock
> - [ ] Manuscript viewer + export
> - [ ] Project pack/unpack
> 
> ---
> 
> ## 16. Future Enhancements
> - Plug-in model manager UI
> - Theme/entity graph view
> - Timeline visualizer
> - Style presets per node
> - Multi-book universe mode
> - Co-author workflows
> - Optional LAN sync (still local-first)
> 
> ---
> End of local-only technical spec.
> ```
> 
> There. Now it’s an offline beast you can carry around on a USB drive like the world’s nerdiest grimoire. If Cursor tries to sneak cloud junk back in, slap its hand with this spec.

### User
> Setting up the project structure and initializing core components.
> 
> 
> [2 tools called]
> 
> 
> Fixing PowerShell directory creation:
> 
> 
> [1 tool called]
> 
> 
> Creating the backend foundation: database schema, FastAPI app, and core services.
> 
> 
> [11 tools called]
> 
> 
> Fixing imports and creating API routes:
> 
> 
> [2 tools called]
> 
> 
> Fixing import issues and creating API routes:
> 
> 
> [8 tools called]
> 
> 
> Creating the frontend skeleton and setup files:
> 
> 
> [17 tools called]
> 
> 
> Fixing a few remaining issues:
> 
> 
> [7 tools called]
> 
> 
> Removing the unused import:
> 
> 
> [2 tools called]
> 
> 
> **Foundation complete.** Built:
> 
> ## What's Ready
> 
> **Backend (FastAPI)**
> - SQLite schema initialization with all tables
> - Database utilities with JSON serialization
> - Core services: ingest, extract, chunk, embeddings, retrieval, engine
> - Local LLM adapter (Ollama/LM Studio/llama.cpp)
> - LanceDB vector store integration
> - API routes: raw items, books
> - Configuration system for local-only runtime
> 
> **Frontend (React + TypeScript)**
> - Vite setup with TypeScript
> - React Router with basic routes
> - Layout component
> - Library and Books pages (skeleton)
> - API client setup
> 
> **Infrastructure**
> - Project structure matching DEV.md spec
> - Vault directory for portable data
> - Requirements.txt with dependencies
> - README with setup instructions
> - Development scripts
> 
> ## Next Steps
> 
> 1. Test the backend: `cd app/backend && python -m qibook_api.main`
> 2. Test the frontend: `cd app/desktop && npm install && npm run dev`
> 3. Add remaining routes: outline generation, evidence mapping, drafting
> 4. Build UI features: upload interface, outline editor, drafting studio
> 5. Wire up the engine: connect state machine to UI
> 
> The architecture is local-only, portable, and ready for feature development. All core services are in place.

### Assistant
> Nice, Cursor didn’t faceplant. That’s genuinely progress in a universe that hates us. Here’s what to do next so this doesn’t stall out as a “foundation complete” museum exhibit.
> 
> ---
> 
> ## 0) Reality check on what you have
> You’ve got:
> - ingestion + chunk + embed + retrieval + engine *stubs*
> - LanceDB wired
> - LLM adapter wired
> - minimal routes + frontend shell
> 
> Translation: **the skeleton breathes, but it can’t walk.** Next sprint is “make the loop real.”
> 
> ---
> 
> ## 1) Backend next steps (priority order)
> 
> ### 1.1 Add the missing API routes
> You already listed them. Do them in this order because each unlocks the next:
> 
> 1. **Outline routes**
>    - `POST /api/books/{id}/outline/generate`
>    - `GET /api/books/{id}/outline`
>    - `PATCH /api/outline/{node_id}`
>    - `POST /api/outline/{node_id}/reorder`
> 
> 2. **Evidence routes**
>    - `POST /api/books/{id}/evidence/map`
>    - `GET /api/outline/{node_id}/evidence`
> 
> 3. **Draft routes**
>    - `POST /api/outline/{node_id}/sample`
>    - `POST /api/outline/{node_id}/draft`
>    - `POST /api/outline/{node_id}/review`
>    - `POST /api/outline/{node_id}/approve`
>    - `POST /api/outline/{node_id}/lock`
> 
> 4. **Manuscript routes**
>    - `GET /api/books/{id}/manuscript`
>    - `POST /api/books/{id}/export`
> 
> Don’t overthink validation yet, just make sure the route contracts match your spec.
> 
> ---
> 
> ### 1.2 Make the Engine actually orchestrate
> Right now it’s probably a polite function pretending to be a state machine. You need:
> 
> - `engine_state` table usage
> - a **single entrypoint** like:
>   - `POST /api/books/{id}/engine/run?until=OUTLINE_APPROVAL`
> - and a “resume from pending approval” version:
>   - `POST /api/books/{id}/engine/resume`
> 
> **Key behavior**:
> - If engine hits approval state, it stops and records `pending_approval_json`.
> - UI flips the status to approved, then calls `/resume`.
> 
> This keeps you from threading async nonsense into a local app.
> 
> ---
> 
> ### 1.3 Stabilize retrieval before you draft
> If retrieval is trash, your book will be trash, just faster.
> 
> Implement:
> - `retrieval.search(query, filters, top_k)`
> - `retrieval.for_outline_node(node)`:
>   1. build query = `node.title + node.goal + themes`
>   2. search LanceDB
>   3. return best chunks with scores
> 
> Also add:
> - minimum evidence rule: if < 3 good chunks, flag node as “thin evidence” so UI can warn you.
> 
> ---
> 
> ## 2) Frontend next steps (tie to backend)
> 
> ### 2.1 Library page becomes real
> Add:
> - upload dropzone
> - paste modal
> - ingestion status list (poll `/raw-items`)
> - “process now” button if an item is unprocessed
> 
> You don’t need pretty. You need **usable**.
> 
> ---
> 
> ### 2.2 Book Wizard tab
> Flow:
> 1. create book
> 2. “Run Analysis” button
> 3. show themes/timeline preview
> 4. Interview form (from engine output JSON)
> 5. “Generate Outline” button
> 
> Wizard is basically a UI wrapper around engine states.
> 
> ---
> 
> ### 2.3 Outline Studio
> Features:
> - tree view (chapters/sections)
> - drag/drop reorder
> - edit title/goal inline
> - “Approve Outline” button
> 
> Also show:
> - evidence count per node once mapped
> - locked status
> 
> ---
> 
> ### 2.4 Drafting Studio (minimum viable)
> Layout:
> - left: outline tree with progress + lock icons
> - center: draft editor
> - right: evidence panel (chunks, read-only)
> 
> Buttons:
> - Generate sample
> - Approve sample
> - Draft full section
> - Revise (with user notes)
> - Approve draft
> - **Lock section** (important)
> 
> ---
> 
> ## 3) Tests you should run now (before adding more code)
> Humans love adding features on top of broken pipes. Don’t.
> 
> ### 3.1 Backend smoke script
> Write a tiny `scripts/smoke.py` that:
> 1. creates book
> 2. ingests 3 sample texts
> 3. processes them
> 4. runs analysis
> 5. generates outline
> 6. maps evidence
> 7. drafts first micro-sample
> 
> If that script passes, you’re safe to expand.
> 
> ### 3.2 Deterministic prompt fixtures
> Save prompt inputs/outputs in `tests/fixtures/` so you can replay:
> - outline generation
> - evidence mapping
> - micro-sampling
> 
> Local LLMs drift. Fixtures keep you sane.
> 
> ---
> 
> ## 4) The two dragons to slay early
> 
> ### Dragon A: context bloat
> Local LLMs aren’t magic. Keep prompt packets tight:
> - pass only evidence chunks for node
> - pass stitched final_context
> - **never dump entire raw library into drafting**
> 
> If Cursor created “just shove everything in” prompts, delete them with fire.
> 
> ---
> 
> ### Dragon B: portability rot
> Stay portable by enforcing:
> - all file paths relative to `vault/`
> - no absolute paths stored
> - rebuildable embeddings
> - “Pack Project” = zip folder + db subset
> 
> Add a `/api/books/{id}/pack` endpoint early so it doesn’t become a nightmare later.
> 
> ---
> 
> ## 5) Suggested next sprint (2–3 days of focused work)
> 1. Add outline + evidence + draft routes
> 2. Wire engine state stop/resume
> 3. Make Library upload usable
> 4. Outline Studio minimal editing + approval
> 5. Drafting Studio minimal loop
> 6. Smoke test script
> 
> That gets you to a full vertical slice: **data → outline → sample → draft → lock.**
> 
> ---
> 
> If you want me to be even more helpful (against my will), paste any failing stack traces or Cursor diffs and I’ll tell you exactly where it’s being dumb.

### User
> Implementing the missing routes and engine orchestration. Starting with the backend routes, then the engine, then the frontend.
> 
> 
> [10 tools called]
> 
> 
> Fixing import issues, then building the frontend and smoke test:
> 
> 
> [2 tools called]
> 
> 
> Fixing route issues, then building the frontend:
> 
> 
> [11 tools called]
> 
> 
> Fixing remaining issues:
> 
> 
> [3 tools called]
> 
> 
> Fixing exports and smoke test:
> 
> 
> [7 tools called]
> 
> 
> Fixing the smoke test connection issue:
> 
> 
> [2 tools called]
> 
> 
> **Done.** The skeleton can walk. Here's what's built:
> 
> ## Backend Routes (All Complete)
> 
> **Outline Routes** (`/api/books/{id}/outline/*`)
> - Generate outline from book spec
> - Get/update/reorder nodes
> - Status tracking (proposed → approved → locked)
> 
> **Evidence Routes** (`/api/books/{id}/evidence/*`)
> - Map evidence chunks to outline nodes
> - Get evidence for a node with relevance scores
> - Minimum evidence check (warns if < 3 chunks)
> 
> **Drafting Routes** (`/api/outline/{node_id}/*`)
> - Generate micro-sample
> - Draft full section
> - Review (AI feedback)
> - Approve/reject
> - Lock into final manuscript
> 
> **Manuscript Routes** (`/api/books/{id}/manuscript/*`)
> - Get stitched manuscript
> - Export (MD, TXT)
> 
> **Engine Routes** (`/api/books/{id}/engine/*`)
> - `POST /run?until=STATE` - Run state machine to target
> - `POST /resume` - Resume from pending approval
> - `GET /state` - Get current state
> 
> ## Engine Orchestration
> 
> State machine with stop/resume:
> - Stops at approval states (`OUTLINE_APPROVAL`, `SAMPLE_APPROVAL`, `SECTION_REVIEW`)
> - Records `pending_approval_json` for UI
> - Resume advances after approval
> 
> ## Retrieval Improvements
> 
> - `search(query, filters, top_k)` with filters
> - `for_outline_node(node_id)` - node-specific evidence
> - Minimum evidence check (warns on thin evidence)
> 
> ## Frontend Components
> 
> **Library** - Upload/paste, status list, drag-drop
> 
> **Book Wizard** - Create → Analyze → Interview → Outline flow
> 
> **Outline Studio** - Tree view, inline edit, approve, evidence count
> 
> **Drafting Studio** - 3-panel layout:
> - Left: Outline tree with progress
> - Center: Draft editor
> - Right: Evidence panel (read-only)
> 
> ## Smoke Test
> 
> `scripts/smoke.py` tests:
> 1. Schema init
> 2. Book creation
> 3. Ingestion
> 4. Chunking
> 5. Embedding (graceful if not configured)
> 6. Retrieval
> 7. LLM (graceful if not running)
> 8. Evidence mapping
> 
> ## Next Steps
> 
> 1. Run smoke test: `python scripts/smoke.py`
> 2. Start backend: `cd app/backend && python -m qibook_api.main`
> 3. Start frontend: `cd app/desktop && npm install && npm run dev`
> 4. Test the loop: Upload → Create Book → Generate Outline → Map Evidence → Draft → Lock
> 
> The full vertical slice is wired: data → outline → sample → draft → lock. The engine stops at approvals and resumes cleanly.

### Assistant
> Well look at that, you did the thing. The app is officially past “hopeful skeleton” and into “a creature that walks upright and doesn’t bite strangers.” Now we switch from construction to **making it reliable, pleasant, and actually book-quality.**
> 
> Here’s what you should do next, in the order that will save you the most pain.
> 
> ---
> 
> ## 1) Make the loop *truthy* (quality + guardrails)
> 
> ### 1.1 Add “thin evidence” UX enforcement
> You already warn if <3 chunks. Now make that actionable:
> - In Outline Studio, show a **red badge** + tooltip: “Thin evidence. Add sources or edit goal.”
> - In Drafting Studio, **disable Draft Full Section** until:
>   - user overrides, OR
>   - evidence >= 3, OR
>   - user manually adds evidence.
> 
> This prevents the LLM from making up Chapter 4 out of vibes and trauma echoes.
> 
> ### 1.2 Add a “manual evidence attach” control
> Let the user search and pin chunks to a node:
> - search box → retrieval.search()
> - results list → “Attach to node”
> - creates evidence_links row
> 
> Because sometimes the model misses the obvious thing sitting in your logs.
> 
> ### 1.3 Freeze locked sections hard
> After lock:
> - hide raw evidence from prompt builder
> - store a hash of locked draft text in DB
> - if user edits locked text, it becomes a **new version** not an overwrite
> 
> You want immutable truth snapshots, not “final drafts” that mutate like a crypto rugpull.
> 
> ---
> 
> ## 2) Improve local model ergonomics (so users don’t hate you)
> 
> ### 2.1 Model status panel (in Settings)
> Show:
> - LLM provider detected (Ollama / LM Studio / llama.cpp)
> - model name
> - context length estimate
> - embeddings model status
> - Whisper/OCR availability
> - last error
> 
> And a giant “Test LLM” button that runs:
> - tiny prompt → latency + token output test
> 
> ### 2.2 Fallback modes
> Your smoke test is graceful. Make UI graceful too:
> - If embeddings missing: allow ingest + outline, but disable evidence mapping with a clear message.
> - If LLM missing: allow library management, but wizard says “No LLM detected.”
> 
> Don’t silently fail. Humans already do that on their own.
> 
> ---
> 
> ## 3) Portability polish (your “carry it anywhere” promise)
> 
> ### 3.1 Pack / Unpack project in UI
> Add buttons:
> - **Pack Project** → zip project folder + db subset + manifest.json
> - **Import Project** → unzip into vault/projects/
> 
> Manifest should include:
> ```json
> {
>   "book_id": "...",
>   "working_title": "...",
>   "created_at": "...",
>   "schema_version": "0.1.0",
>   "embeddings_present": true,
>   "files": ["raw/...", "drafts/...", "exports/..."]
> }
> ```
> 
> ### 3.2 Rebuild embeddings tool
> If embeddings absent, allow:
> - “Rebuild Vector Index”  
>   loops through chunks → embed → insert LanceDB.
> 
> Because portability means not crying if someone deletes `/lancedb`.
> 
> ---
> 
> ## 4) Writing quality upgrades (the difference between “draft” and “book”)
> 
> ### 4.1 Add “style anchor”
> Let user pick/describe a style once:
> - store in book_projects.metadata_json
> - auto-inject into every draft prompt
> 
> Example:
> - “Candid memoir, contemporary, sharp but warm, short paragraphs, no academic tone.”
> 
> Local LLMs *need* consistency. This helps.
> 
> ### 4.2 Add continuity checker pass
> Before approve/lock:
> - run review prompt with:
>   - node goal
>   - current draft
>   - stitched final_context
> - flag:
>   - contradictions
>   - timeline drift
>   - repeated anecdotes
>   - tone mismatch
> 
> Show flags in UI as a checklist. User can override. But at least they see the landmines.
> 
> ### 4.3 Section word targets
> Add per-node targets:
> - default from book length / chapter count
> - user editable
> - drafts should aim for ±15%
> 
> That stops the LLM from writing a 7k word prologue and a 400 word climax.
> 
> ---
> 
> ## 5) QA Sprint (don’t skip because you’re excited)
> 
> Run these tests *now*:
> 
> ### 5.1 Nasty ingestion test
> - 1 messy chat export
> - 1 scanned PDF
> - 1 calendar `.ics`
> - 1 audio clip
> - 1 long journal markdown
> 
> Goal: no crashes, everything lands as raw_items, chunks exist.
> 
> ### 5.2 Outline edit resilience
> - generate outline
> - delete a chapter
> - reorder
> - rename
> - approve
> - map evidence again
> - draft
> 
> Goal: engine doesn’t freak out or reference deleted nodes.
> 
> ### 5.3 Locking correctness
> - lock chapter 1 section
> - draft chapter 2 section
> - verify prompts do NOT include raw evidence from locked section
> 
> If that fails, your core rule is broken.
> 
> ---
> 
> ## 6) Packaging (so it’s actually an app, not a science project)
> 
> Pick your poison (quietly, without a religious war):
> - **Electron** if you want easy shipping now
> - **Tauri** if you want smaller binaries and less RAM crimes
> 
> Do:
> - one-click installer
> - set vault location on first run
> - auto-start local backend
> 
> Because nobody wants to run 3 terminal commands to write a book.
> 
> ---
> 
> ## 7) What I’d do *after* all that
> - Timeline visualizer overlayed with outline
> - Entity anonymizer pass
> - “chapter summary so far” generator for marketing blurbs
> - Multi-book universe mode (reuse evidence)
> 
> But not before the above. You’re building a book factory, not a demo.
> 
> ---
> 
> You’ve got a working vertical slice already. Now make it *trustworthy, portable, and book-good*. The rest is polishing, not reinvention.

### User
> next give me what you do after all that.

### Assistant
> Alright, here’s the “after all that” roadmap. This is the part where your walking skeleton becomes a professional authoring monster that people would actually pay for, not just admire in your repo like a taxidermy project.
> 
> I’m putting this in the *right* order: stuff that compounds value first, shiny toys later.
> 
> ---
> 
> ## Phase 6: Make it *feel* like a real writing partner
> ### 6.1 Chapter Recap + Running Context
> Auto-generate a short “so far” recap after every locked section:
> - stored as `running_summary` per chapter + whole book
> - injected into future draft prompts
> - visible in UI for the user
> 
> Why: local models drift. Recaps keep narrative coherence tight without bloating context.
> 
> ### 6.2 Style Drift Monitor
> Add a cheap pass that checks tone consistency:
> - compare new draft to style anchor
> - score + highlight drift (“too formal”, “too bitter”, “too bland”)
> - one-click “re-tone this section”
> 
> Why: memoir tone matters. This stops the LLM from randomly roleplaying a textbook author.
> 
> ### 6.3 “Narrative Heatmap”
> Per outline node, show:
> - evidence density (how much raw support)
> - emotional intensity (sentiment variance)
> - topic coverage vs outline goal
> 
> Why: helps you see weak chapters before you write them.
> 
> ---
> 
> ## Phase 7: Timeline + Theme Intelligence (the big multiplier)
> ### 7.1 Timeline Visualizer
> UI view:
> - events extracted from evidence
> - draggable to correct dates
> - chapters overlaid on time
> 
> Then allow:
> - “assign this event to Chapter 3”
> - “merge duplicate events”
> - “flag timeline gaps”
> 
> Why: nonfiction lives or dies on timeline clarity. This makes the app *different*.
> 
> ### 7.2 Theme Bookmap
> Interactive theme clusters:
> - click theme → see supporting evidence chunks
> - “promote theme to chapter”
> - “merge themes”
> - “theme appears in chapters A/B/C” indicator
> 
> Why: gives you power to shape arc instead of just accepting the AI’s guess.
> 
> ---
> 
> ## Phase 8: Privacy-first editing superpowers
> ### 8.1 Global Anonymizer / Redactor
> Rules engine:
> - entity list from extraction
> - user chooses replacements:
>   - “real name → initials”
>   - “company → ‘the firm’”
>   - “address → ‘my old neighborhood’”
> 
> Apply as:
> - pre-draft anonymization
> - post-draft scrub pass
> - export-time scrub
> 
> Why: if you’re using real life data, you need a “don’t get sued or dragged” button.
> 
> ### 8.2 Sensitive-content Guardrails
> Local classifier pass:
> - flags medical/legal/mental-health specifics
> - suggests phrasing as *experience*, not *fact*
> - allows user override
> 
> Why: keeps memoir truthful without turning into a courtroom exhibit.
> 
> ---
> 
> ## Phase 9: Author workflow features (aka “how writers actually work”)
> ### 9.1 Multi-draft branching
> Let user branch a node:
> - Draft A / Draft B
> - compare diff
> - pick winner → lock
> 
> Why: writers try angles. This supports craft, not linear obedience.
> 
> ### 9.2 Scene/Section cards
> Kanban-ish optional view:
> - each section as a card
> - status (thin evidence / sampled / drafted / locked)
> - drag to reorder
> 
> Why: some brains need visual flow, not trees.
> 
> ### 9.3 “Voice Notes → Evidence” quick capture
> In-app recorder:
> - record thought
> - auto-transcribe local
> - auto-tag to current chapter
> 
> Why: best nonfiction comes from mid-walk brain lightning.
> 
> ---
> 
> ## Phase 10: Multi-book universe mode
> This is where QiOS vibes kick in hard.
> 
> ### 10.1 Shared Evidence Library
> Allow:
> - one raw library feeding multiple books
> - evidence chunks can be linked across projects
> - “this chunk already used in Book X, Chapter Y” warning
> 
> Why: you’re not writing *one* thing. You’re building a canon.
> 
> ### 10.2 Canon / Continuity Manager
> When a chunk is used:
> - it becomes a “canon reference”
> - future books can cite it, not rewrite it
> - optional export of canon appendix
> 
> Why: prevents contradiction across a series.
> 
> ---
> 
> ## Phase 11: Publishing-grade output
> ### 11.1 Export templates
> Add formats:
> - manuscript standard (12pt Times, double spaced)
> - Kindle-ready EPUB
> - audiobook script format (dialogue + pauses)
> - “submission packet” bundle (proposal + outline + sample chapters)
> 
> Why: makes the app usable for *real* publishing workflows.
> 
> ### 11.2 Front-matter + Back-matter builder
> Guided generation:
> - preface
> - acknowledgements
> - glossary
> - appendix
> - references (auto-linked to evidence)
> 
> Why: nonfiction needs scaffolding. This makes it pro-level.
> 
> ---
> 
> ## Phase 12: Plugin ecosystem (so you stop hardcoding everything)
> ### 12.1 Parser plugins
> Let users add:
> - new chat export formats
> - new calendar sources
> - niche doc types
> 
> Config-driven registry:
> ```json
> {
>   "parsers": [
>     {"type":"whatsapp_json","entrypoint":"parsers/whatsapp.py"}
>   ]
> }
> ```
> 
> ### 12.2 Prompt plugins
> Allow per-project prompt overrides without editing core code.
> 
> Why: you’re going to want custom engines for different books. Don’t fork yourself into misery.
> 
> ---
> 
> ## If you want one “north star” statement:
> After the foundation, you build **three things**:
> 1. **Better understanding of life data** (timeline, themes, canon)
> 2. **Better control for the author** (branching, cards, anonymizer)
> 3. **Publishing-level outputs** (templates, bundles, EPUB)
> 
> Everything else is decoration.
> 
> Now go ship the next phase before your ambition eats your calendar.

### User
> now what

### Assistant
> Alright, now we’re in the phase where most developers freeze because the skeleton is walking, the roadmap is huge, and your ADHD brain is whispering, “What if we rebuild all of this in a different framework?” No. We’re not doing chaos today.
> 
> Here’s the **exact next moves**, in the order that actually moves the project forward and keeps your life sane.
> 
> ---
> 
> # 1) Stabilize the “Vertical Slice”  
> Your app runs end-to-end, but you need to confirm it works on **real** mixed content.
> 
> ## Do this next:
> ### 1.1 Create a “Real-World Test Project”
> Use:
> - One exported chat log  
> - One journal file  
> - One screenshot (OCR)  
> - One PDF (scanned)  
> - One audio note  
> 
> Then run:
> 1. Ingest everything  
> 2. Process  
> 3. Run analysis  
> 4. Generate outline  
> 5. Map evidence  
> 6. Generate sample  
> 7. Draft a full section  
> 8. Lock  
> 
> If anything feels weird, slow, or brittle?  
> Log it. Fix it. Move on.
> 
> ### Why now:
> If this cracks later, it will crack *after* you’ve built 20 more features. Fixing the foundation later is hell.
> 
> ---
> 
> # 2) Improve UI polish on the core flow (not sexy but crucial)
> The loop works, but the UI probably feels awkward, empty, or confusing.
> 
> ## Add minimal polish:
> - **Loader states** (outline generating, drafting, etc.)
> - **Disable buttons** during engine run
> - **Snackbars/toasts** for success/failure  
> - **Progress indicator** on outline nodes (proposed/approved/locked)
> - **Evidence count badges** (green: OK, yellow: thin, red: missing)
> 
> ### Why:
> This takes the user from “what is happening” to “I understand what the app is doing.”
> 
> Do this before any new big features.
> 
> ---
> 
> # 3) Add the Two Power Tools That Unlock Everything Else
> 
> These are the first *new* features to build:
> 
> ---
> 
> ## 3.1 **Manual Evidence Manager** (Feature #1)
> This is non-negotiable.
> 
> Every section should show:
> - Search box
> - Search results
> - Button: “Attach this to section”
> - Button: “Detach”
> - Evidence list with relevance scores
> 
> ### Why:
> You MUST give users control.  
> Automatic evidence mapping is never perfect.  
> This prevents hallucinated chapters and garbage drafts.
> 
> Everything else downstream depends on this.
> 
> ---
> 
> ## 3.2 **Style Anchor System** (Feature #2)
> Add a tiny, simple feature:
> - Let user enter a writing style (or choose from presets)
> - Save it per book
> - Auto-inject into drafting prompts
> 
> Even something like:
> > “Candid, introspective memoir tone. Short, emotional sentences. No academic wording.”
> 
> ### Why:
> This solves 80% of “tone drift” problems.  
> Local LLMs especially need this.
> 
> ---
> 
> # 4) Add the Real **Drafting Review Loop**
> It exists, but now you refine it:
> 
> ### Add:
> - A “change requests” box  
> - A “revise with notes” button  
> - A “compare last two drafts” diff viewer  
> - Auto-run the continuity checker  
> 
> ### Why:
> Drafting is iterative.  
> Right now you have the pieces; this lets you actually *use* them.
> 
> ---
> 
> # 5) Start Phase 2 Feature Work (Timeline Visualizer)
> 
> Don’t go full UI crazy. Start with backend.
> 
> ### 5.1 Build backend extraction:
> Store events in SQLite:
> ```
> events (
>   id TEXT,
>   book_id TEXT,
>   date TEXT,
>   description TEXT,
>   source_chunk_id TEXT
> )
> ```
> 
> ### 5.2 Build minimal UI:
> - A chronological list
> - Each event linking back to its chunk
> - “Assign to chapter” button
> 
> ### Why:
> This becomes the backbone for narrative structure, coherence, memory management, and “canon.”
> 
> ---
> 
> # 6) Add Export Templates (Pro-level but simple)
> Start small:
> - Export as Markdown (already)
> - Export as TXT (already)
> - Add DOCX via python-docx template
> - Add a “Publisher Standard Manuscript” option:
>   - 12pt Times
>   - Double-spaced
>   - Indented paragraphs
>   - Title pages
> 
> ### Why:
> This lets you hand your manuscript to another human being without shame.
> 
> ---
> 
> # 7) Clean Up Dev Experience
> Do this BEFORE new features get messy:
> 
> ### Add:
> - Prettier / Black / isort / Ruff config
> - Unified logging decorator
> - Error boundary middleware for backend
> - A `.env.local` for model paths and vault settings
> - “Rebuild project” script
> 
> ### Why:
> Once the project grows, chaos grows exponentially unless you tame it now.
> 
> ---
> 
> # 8) Add “Pack Project” + “Unpack Project”
> This is the feature clients will drool over.
> 
> ### Function:
> - Zip:
>   - project folder
>   - SQLite subset
>   - metadata
> - Unzip:
>   - checks schema version
>   - imports safely
>   - rebuild embeddings if missing
> 
> ### Why:
> Your app becomes portable, sharable, future-proof.
> 
> ---
> 
> # 9) After all that?  
> **Then** you start working on the cool stuff:
> - Theme map (interactive)
> - Heatmap of emotional intensity
> - Branching drafts
> - Universe mode
> - Canon manager
> - Voice-note quick capture
> - EPUB export
> - Assistant commentary mode
> - Multi-pass editing modes (line edit, structural edit, voice consistency pass)
> - Publishing submission packet generator
> 
> But NOT before you finish the foundational enhancements above.
> 
> ---
> 
> # TL;DR – What You Do NEXT, No Thinking Required
> 
> ## **Do these in order:**
> 
> 1. Run real-world ingestion test  
> 2. Add UI polish to the core loop  
> 3. Implement:  
>    - Manual Evidence Manager  
>    - Style Anchor System  
> 4. Complete the Drafting Review Loop  
> 5. Build minimal Timeline Visualizer  
> 6. Add DOCX export template  
> 7. Improve developer tooling  
> 8. Add Pack & Unpack  
> 9. THEN move on to advanced features
> 
> You’re not guessing anymore. You’re building an actual book creation engine now.
> 
> If you want, I can also give you:
> - Full feature tickets  
> - Cursor-ready code tasks  
> - UI mockups  
> - Prompt pack updates  
> - Timeline schema  
> - Pack/unpack scripts  
> 
> Just tell me which direction you want to sprint next.

### User
> then after that.

### Assistant
> Alright, Q — you’ve built the base, stabilized the loop, added evidence control, style anchors, drafting discipline, timeline intelligence, export quality, portability, and DEX polish.  
> 
> You want to know **what comes *after* all that?**
> 
> This is where your app stops being “a cool local writing tool” and becomes a **full creative intelligence system** — a personal author OS.
> 
> Here’s the path forward, phase by phase, in the exact order that yields the smartest, most powerful evolution of your tool.
> 
> ---
> 
> # **PHASE 13: The Book Intelligence Layer**  
> This is where the app stops being a book builder and starts *thinking like a book.*
> 
> ## **13.1 Structural Editing Engine**  
> After drafts are locked, add an AI pass that evaluates the entire manuscript for:
> - pacing
> - redundancy
> - weak chapters
> - emotional arc consistency
> - logic flow
> - chapter-to-chapter transitions
> - theme reinforcement
> 
> Outputs actionable notes:
> > “Ch. 4 introduces a theme that doesn’t reappear until Ch. 9. Suggest merging or bridging.”
> 
> This makes the app a **real editor**, not just a writer.
> 
> ---
> 
> ## **13.2 Global Theme-Arc Alignment**
> Auto-generate:
> - theme usage frequency charts  
> - chapter-by-chapter theme presence  
> - missing beats  
> - overused beats  
> - “theme heat” timeline  
> 
> Allows you to see if the *message* of the book is actually being delivered.
> 
> ---
> 
> ## **13.3 Character/People Maps (for memoir/biography)**
> Local LLM extracts:
> - important people  
> - relationships  
> - recurring conflicts  
> - emotional impact
> 
> Builds a visual network graph:
> - nodes: people  
> - edges: roles, relationships, conflicts  
> - frequency heat  
> 
> This strengthens storytelling clarity.
> 
> ---
> 
> # **PHASE 14: Narrative Simulation & Scenario Explorer**
> Now we let the app show “alternate reality writing futures.”
> 
> ## **14.1 Outline Recombiner**
> Given your existing outline, generate:
> - 3 alternate outlines  
> - 3 alternate chapter orders  
> - 3 alternate arcs or emphasis patterns  
> 
> You decide if any alternate structure is better.
> 
> ## **14.2 “What If...” Scenario Testing**
> Ask:
> > “What if the book went darker here?”  
> > “What if Chapter 5 was about X instead?”  
> > “What if the tone was more raw or more business-forward?”
> 
> The system predicts:
> - pacing effects  
> - coherence impacts  
> - tonal consequences  
> 
> This is like having a story consultant in the room.
> 
> ---
> 
> # **PHASE 15: Intelligent Revision Modes**
> Introduce different types of editing modes, like a human editor with hats:
> 
> ## **15.1 Line Editor Mode**
> Tightens:
> - voice consistency  
> - clarity  
> - rhythm  
> - sentence structure  
> 
> ## **15.2 Copyeditor Mode**
> Fixes:
> - grammar  
> - spelling  
> - redundancies  
> - formatting  
> 
> ## **15.3 Developmental Editor Mode**
> Examines:
> - message clarity  
> - emotional beats  
> - narrative logic  
> - audience alignment  
> 
> These modes treat your manuscript differently — not everything is “generate more words.”
> 
> ---
> 
> # **PHASE 16: Multi-Book Universe Builder**
> You’re writing multiple works tied together (EmpowerQNow, 713, memoir arcs, business books, spiritual material).  
> This is where your tool becomes **QiOS for Books**.
> 
> ## **16.1 Shared Evidence Universe**
> One evidence library that feeds multiple books.
> 
> ## **16.2 Book Canon System**
> When a chunk becomes a canonical reference:
> - it’s labeled  
> - tracked  
> - available to future books  
> 
> This prevents contradictions across your story world.
> 
> ## **16.3 Franchise Arc Intelligence**
> Visual map of:
> - themes across books  
> - character arcs across books  
> - core messages  
> - changes across works  
> 
> This is how major authors keep multi-series consistent.
> 
> ---
> 
> # **PHASE 17: The Author Workbench**
> You’ve got writing. Now add the tools around it.
> 
> ## **17.1 Idea Inbox**
> A place for random:
> - thoughts  
> - notes  
> - dream logs  
> - voice memos  
> - quotes  
> 
> Auto-tagged and suggested into:
> - chapters  
> - themes  
> - timelines  
> 
> ## **17.2 Concept Generator**
> Take a theme and generate:
> - analogies  
> - metaphors  
> - stories  
> - examples  
> - parables  
> - spiritual reflections  
> 
> This gives your writing depth.
> 
> ---
> 
> # **PHASE 18: Publishing & Marketing System**
> When the book is done, you need a real launch environment.
> 
> ## **18.1 Marketing Asset Factory**
> Generate:
> - book summary  
> - chapter summaries  
> - pull quotes  
> - author bio variations  
> - social media clips  
> - short-form hooks  
> - email sequences  
> - press release drafts  
> 
> ## **18.2 Cover Concept Generator**
> AI-driven:
> - compositional ideas  
> - style variations  
> - typography pairings  
> 
> (Using Sora/DALL·E locally where possible.)
> 
> ## **18.3 Metadata & Distribution Pack**
> Generate:
> - ISBN metadata  
> - Amazon KDP metadata  
> - BISAC categories  
> - loglines  
> - SEO keywords  
> 
> Ready to upload anywhere.
> 
> ---
> 
> # **PHASE 19: The “Inner Voice” Mode**
> This is advanced, but powerful.
> 
> Let the app:
> - learn your personal writing voice  
> - build a style model  
> - keep outputs aligned  
> - optionally generate “thinking mode” reflections as you write  
> 
> This becomes your **private co-author.**
> 
> ---
> 
> # **PHASE 20: Full Autonomy Mode (optional)**  
> This is the “Auto Write While You Sleep” feature.
> 
> You specify:
> - chapter  
> - angle  
> - style  
> - constraints  
> 
> You hit *Run.*  
> The system:
> - pulls evidence  
> - builds sample  
> - writes draft  
> - reviews draft  
> - polishes  
> - flags issues  
> 
> And delivers a readable chapter by morning.
> 
> This is optional because too much autonomy can get creepy if misused.
> 
> ---
> 
> # **TL;DR — After All That**
> 
> You evolve from:
> 
> **Phase 1–12:**  
> A high-quality book drafting system.
> 
> Into:
> 
> **Phase 13–20:**  
> A full-fledged, local-first, AI-powered **author operating system** that:
> - understands your life  
> - understands your themes  
> - understands your writing voice  
> - maintains narrative integrity across books  
> - and supports the entire publishing process end-to-end.
> 
> This is when your tool stops being “book software.”  
> It becomes a **creative intelligence companion** — an extension of your own mind.
> 
> ---
> 
> If you want, I can give you:
> - a phased development plan  
> - tickets for Cursor  
> - UI mockups  
> - backend schema extensions  
> - or even the full **QiBookOS 1.0** roadmap in QiDecimal codes.
> 
> Just say the word and I’ll drop it.

### User
> yes, pleae all of it.

### Assistant
> Alright, you asked for **all of it**, so here’s the whole unholy bundle: phased development plan, Cursor-ready tickets, UI mockups (text wireframes), backend schema extensions, and a full QiDecimal-coded roadmap. It’s local-only, portable, and assumes your current vertical slice is working.
> 
> ```markdown
> ---
> date: 2025-11-24
> title: QiBookOS Roadmap + Tickets + Schema + UI Mockups
> category: Development
> keywords: QiBookOS, LocalRAG, Roadmap, Tickets, Schema
> project_context: QiBook (Local Book Writing App)
> ---
> 
> # QiBookOS 1.0 → 2.0 Master Roadmap (Local-Only)
> 
> You have a working vertical slice:
> **data → outline → evidence → sample → draft → approve → lock → stitch → export**.
> 
> Now we scale it into a full author operating system without breaking portability or your sanity.
> 
> ---
> 
> ## 1) Phased Development Plan (Realistic, Compounding Value)
> 
> ### Phase A (Stabilize + Control) — 1–2 sprints
> **Goal:** make core loop trustworthy and author-controllable.
> 
> - Manual Evidence Manager (search/pin/detach)
> - Style Anchor System (per-book voice)
> - Thin Evidence gating (warnings + optional hard block)
> - Locking immutability + version history
> - Model status panel + graceful fallbacks
> - Pack/Unpack projects + rebuild embeddings
> - Smoke tests expanded to messy multi-modal inputs
> - Minimal UX polish (progress, loaders, disable rules)
> 
> **Exit Criteria:**  
> You can run a real memoir book through the loop without hallucination, tone drift, or UX confusion.
> 
> ---
> 
> ### Phase B (Timeline + Theme Intelligence) — 1–2 sprints
> **Goal:** the system *understands* life data as structure.
> 
> - Timeline backend extraction + event table
> - Timeline UI list → then visualizer
> - Theme Map (clusters, coverage, chapter presence)
> - Evidence heat badges (density per node)
> - Chapter recap / running summary generation
> 
> **Exit Criteria:**  
> You can see where chapters are thin, out-of-order, or missing beats before drafting.
> 
> ---
> 
> ### Phase C (Author Workflow Pro Tools) — 2–3 sprints
> **Goal:** support real writer behavior.
> 
> - Draft branching (A/B drafts)
> - Diff viewer
> - Section cards / Kanban view
> - Word target enforcement per node
> - Continuity checker as required pre-lock pass
> - Voice notes → evidence capture
> 
> **Exit Criteria:**  
> Writing feels like a studio, not a form submission app.
> 
> ---
> 
> ### Phase D (Publishing + Launch Factory) — 1–2 sprints
> **Goal:** finished books ship cleanly.
> 
> - DOCX + Publisher manuscript template
> - EPUB export
> - Back-matter builder (acknowledgements, glossary, refs)
> - Submission packet bundle
> - Marketing asset factory (blurbs, hooks, quotes)
> 
> **Exit Criteria:**  
> You can generate a publish-ready book plus launch assets without leaving the app.
> 
> ---
> 
> ### Phase E (Universe + Canon) — ongoing
> **Goal:** multi-book consistency and canon intelligence.
> 
> - Shared evidence universe
> - Canon labels + cross-project warnings
> - Franchise arc maps (themes/people across books)
> - Global anonymizer rules across universe
> 
> **Exit Criteria:**  
> You can write a 15-book series without contradicting yourself or redoing work.
> 
> ---
> 
> ## 2) Cursor-Ready Ticket Backlog (Ordered)
> 
> Each ticket is small enough for Cursor to implement directly.
> 
> ### Sprint A1 — Control & Trust
> **A1-01 Manual Evidence Search UI**  
> - Add search input to EvidencePanel.  
> - Call `GET /api/search?query=&filters=`.  
> - Render results w/ relevance score.  
> - Button “Attach to Node” → POST evidence_links.
> 
> **A1-02 Manual Evidence Attach/Detach API**  
> - `POST /api/outline/{node_id}/evidence/attach` {chunk_id}  
> - `POST /api/outline/{node_id}/evidence/detach` {chunk_id}  
> - Ensure uniqueness constraint.
> 
> **A1-03 Thin Evidence Gating**  
> - If evidence_links < 3, disable “Draft Full Section” unless override toggle.  
> - Add override confirmation modal.
> 
> **A1-04 Style Anchor Storage + Injection**  
> - UI: Style box in Wizard.  
> - Store in book_projects.metadata_json.style_anchor.  
> - Engine: inject into every sample/draft prompt packet.
> 
> **A1-05 Locked Section Immutability**  
> - Prevent edits to locked draft_sections unless “Create new version.”  
> - Add `draft_version++` on edit.
> 
> **A1-06 Model Status Panel**  
> - Settings route with provider detection.  
> - Show model name, ctx length estimate, embedding model status.  
> - “Test LLM” button.
> 
> **A1-07 Pack Project Endpoint + UI**  
> - `/api/books/{id}/pack` creates zip into exports/.  
> - UI button downloads.  
> - Include manifest.json.
> 
> **A1-08 Import Project Flow**  
> - UI import zip.  
> - Backend unzip into vault/projects/.  
> - Validate schema_version.  
> - If embeddings missing, mark rebuild needed.
> 
> **A1-09 Rebuild Embeddings Tool**  
> - Button per book: loops chunks → embed → LanceDB upsert.
> 
> ---
> 
> ### Sprint B1 — Timeline Intelligence
> **B1-01 events table + model**  
> - Add schema (see section 4).  
> - Create CRUD.
> 
> **B1-02 Event Extraction Service**  
> - From themes/timeline pass, store events in DB.  
> - Deduplicate by (date, description similarity).
> 
> **B1-03 Timeline List UI**  
> - Show events chronologically.  
> - Link back to source chunk.  
> - “Assign to outline node” button.
> 
> **B1-04 Timeline Visualizer v0**  
> - Simple vertical timeline with chapter overlays.
> 
> **B1-05 Running Recap Generator**  
> - After each lock, generate chapter recap + global recap.  
> - Store in book_projects.metadata_json.running_summary.
> 
> ---
> 
> ### Sprint C1 — Writer Studio Tools
> **C1-01 Draft Branching**  
> - Allow multiple drafts per node: branch_id field.  
> - UI: create branch A/B.
> 
> **C1-02 Diff Viewer**  
> - Show line-diff between drafts.
> 
> **C1-03 Kanban Section Cards**  
> - Cards by status (proposed/approved/drafted/locked).  
> - Drag reorder updates order_index.
> 
> **C1-04 Word Target System**  
> - Auto-compute targets per node.  
> - UI editable.  
> - Draft prompts aim for ±15%.
> 
> **C1-05 Continuity Checker Required Pre-Lock**  
> - Run review pass against stitched final_context.  
> - Block lock unless user overrides flagged contradictions.
> 
> **C1-06 Voice Notes Capture**  
> - Record audio → local ASR → raw_item auto-tagged to current node.
> 
> ---
> 
> ### Sprint D1 — Publishing + Launch
> **D1-01 DOCX Export Template**  
> - python-docx template file.  
> - styles: manuscript standard.
> 
> **D1-02 EPUB Export**  
> - pandoc if installed, fallback to ebooklib.
> 
> **D1-03 Back-matter Builder**  
> - Wizard for acknowledgements, glossary, appendix.  
> - Stored as outline_nodes type=appendix/backmatter.
> 
> **D1-04 Submission Packet Bundle**  
> - Zip: proposal + outline + sample chapters + manuscript.
> 
> **D1-05 Marketing Asset Factory**  
> - Generate blurbs, hooks, social posts, chapter teasers.
> 
> ---
> 
> ### Sprint E1 — Universe Mode
> **E1-01 Shared Evidence Library**  
> - Allow multiple books to reference raw_items/chunks.  
> - evidence_links includes book_id for clarity.
> 
> **E1-02 Canon Labeling**  
> - Add canon flag on chunks.  
> - Warn when reusing canon chunk in new context.
> 
> **E1-03 Franchise Arc Map UI**  
> - Heatmap themes across books.  
> - People graph across books.
> 
> ---
> 
> ## 3) UI Mockups (Text Wireframes)
> 
> ### 3.1 Library
> ```
> [Library]
> ---------------------------------------------------
> + Upload Files   + Paste Text   + Record Audio
> ---------------------------------------------------
> Filters: Type ▼  Date ▼  Tags ▼  Search [_________]
> 
> RAW ITEMS LIST
> ---------------------------------------------------
> | Type | Title            | Imported | Status |
> | chat | WhatsApp Export  | 11/24    | Ready  |
> | pdf  | Lease Scan       | 11/24    | OCRing |
> | note | Journal_2025.md  | 11/24    | Ready  |
> ---------------------------------------------------
> [Process Selected] [Rebuild Embeddings]
> ```
> 
> ### 3.2 Book Wizard
> ```
> [New Book Wizard]
> Step 1: Book Setup
> - Working Title: [______________]
> - Style Anchor:  [______________]
> - Constraints:   [ + Add ]
> 
> [Run Analysis]
> Themes preview | Timeline preview
> 
> Step 2: Interview
> Q1 ... [answer]
> Q2 ... [answer]
> [Save Spec]
> 
> Step 3: Outline
> [Generate Outline]
> [Outline Tree Preview]
> [Approve Outline]
> ```
> 
> ### 3.3 Outline Studio
> ```
> [Outline Studio]
> Left: Tree
> -----------------------------------
> > Prologue (approved)
> > Ch1: ______ (drafted)
>    - 1.1 ______ (locked ✅)
>    - 1.2 ______ (approved)
> > Ch2: ______ (thin evidence ⚠️)
> -----------------------------------
> 
> Right: Node Editor
> Title: [____________]
> Goal:  [____________]
> Word Target: [ 2500 ]
> Evidence: 2 chunks ⚠️  [Search & Attach]
> [Approve Node] [Lock Node]
> ```
> 
> ### 3.4 Drafting Studio
> ```
> [Drafting Studio]
> ---------------------------------------------------------
> | Outline Tree | Draft Editor | Evidence Panel          |
> ---------------------------------------------------------
> [Sample] [Approve Sample]
> [Draft Section] [Revise w/ Notes] [Approve Draft] [LOCK]
> 
> Evidence Panel:
> - chunk A (0.91) [open]
> - chunk B (0.78) [open]
> - chunk C (0.74) [open]
> [Search & Attach]
> ```
> 
> ### 3.5 Timeline
> ```
> [Timeline]
> ---------------------------------------------------
> 2020-06  Moved to Indy          [src] [assign to Ch1]
> 2021-03  Started QiAlly         [src] [assign to Ch2]
> 2023-09  Major Reset #3         [src] [assign to Ch5]
> ---------------------------------------------------
> [Open Visual Timeline]
> ```
> 
> ---
> 
> ## 4) Backend Schema Extensions (Local)
> 
> ### 4.1 events
> ```sql
> CREATE TABLE events (
>   id TEXT PRIMARY KEY,
>   book_id TEXT NOT NULL,
>   date TEXT,                        -- ISO or partial (YYYY-MM)
>   description TEXT NOT NULL,
>   source_chunk_id TEXT,
>   confidence REAL,
>   assigned_outline_node_id TEXT,    -- nullable
>   metadata_json TEXT,
>   FOREIGN KEY(book_id) REFERENCES book_projects(id),
>   FOREIGN KEY(source_chunk_id) REFERENCES chunks(id),
>   FOREIGN KEY(assigned_outline_node_id) REFERENCES outline_nodes(id)
> );
> ```
> 
> ### 4.2 draft_branches
> ```sql
> CREATE TABLE draft_branches (
>   id TEXT PRIMARY KEY,
>   outline_node_id TEXT NOT NULL,
>   label TEXT NOT NULL,              -- "A", "B", "Alt POV", etc.
>   created_at TEXT NOT NULL,
>   FOREIGN KEY(outline_node_id) REFERENCES outline_nodes(id)
> );
> ```
> 
> Add to draft_sections:
> ```sql
> ALTER TABLE draft_sections ADD COLUMN branch_id TEXT;
> ```
> 
> ### 4.3 canon_chunks (universe mode)
> ```sql
> CREATE TABLE canon_chunks (
>   chunk_id TEXT PRIMARY KEY,
>   canon_label TEXT,                 -- "Origin Story", "Lesson 1", etc.
>   notes TEXT,
>   created_at TEXT NOT NULL,
>   FOREIGN KEY(chunk_id) REFERENCES chunks(id)
> );
> ```
> 
> ### 4.4 running_summaries
> (optional separate table, or metadata_json on book_projects)
> ```sql
> CREATE TABLE running_summaries (
>   id TEXT PRIMARY KEY,
>   book_id TEXT NOT NULL,
>   outline_node_id TEXT,             -- null for global
>   summary_text TEXT NOT NULL,
>   updated_at TEXT NOT NULL,
>   FOREIGN KEY(book_id) REFERENCES book_projects(id)
> );
> ```
> 
> ---
> 
> ## 5) QiDecimal-Coded Roadmap (QiBookOS)
> 
> > 0 = Foundation (done).  
> > 1 = Control. 2 = Intelligence. 3 = Studio Tools. 4 = Publishing. 5 = Universe. 6 = Autonomy.
> 
> ### 0.00.00 FOUNDATION (DONE)
> - 0.01.00 Local ingestion + processing pipeline
> - 0.02.00 SQLite schema + LanceDB
> - 0.03.00 LLM/embeddings adapters
> - 0.04.00 Engine stop/resume orchestration
> - 0.05.00 Vertical slice UI
> 
> ### 1.00.00 CONTROL & TRUST
> - 1.01.00 Manual Evidence Manager
> - 1.02.00 Thin Evidence gating + override
> - 1.03.00 Style Anchor system
> - 1.04.00 Lock immutability + versioning
> - 1.05.00 Model status + fallbacks
> - 1.06.00 Pack/Unpack projects
> - 1.07.00 Rebuild vector index tool
> 
> ### 2.00.00 LIFE INTELLIGENCE
> - 2.01.00 Timeline extraction + events DB
> - 2.02.00 Timeline UI + overlays
> - 2.03.00 Theme Map clusters
> - 2.04.00 Evidence heat/density per node
> - 2.05.00 Running recap generator
> 
> ### 3.00.00 AUTHOR STUDIO
> - 3.01.00 Draft branching A/B
> - 3.02.00 Diff viewer
> - 3.03.00 Section Kanban
> - 3.04.00 Word target enforcement
> - 3.05.00 Continuity checker pre-lock
> - 3.06.00 Voice notes → evidence capture
> - 3.07.00 Scenario outline recombiner (alt outlines)
> 
> ### 4.00.00 PUBLISHING & LAUNCH
> - 4.01.00 DOCX manuscript export templates
> - 4.02.00 EPUB export
> - 4.03.00 Back-matter builder
> - 4.04.00 Submission packet bundler
> - 4.05.00 Marketing asset factory
> - 4.06.00 Metadata/BISAC/KDP pack
> 
> ### 5.00.00 UNIVERSE / CANON
> - 5.01.00 Shared evidence library across books
> - 5.02.00 Canon chunk labeling + warnings
> - 5.03.00 Franchise arc map (themes across books)
> - 5.04.00 Cross-book people/relationship graph
> - 5.05.00 Global anonymizer rules
> 
> ### 6.00.00 AUTONOMY (OPTIONAL, DANGEROUSLY FUN)
> - 6.01.00 Full auto-draft mode per chapter
> - 6.02.00 Structural editor pass (pacing/redundancy)
> - 6.03.00 Revision modes (line/copy/developmental)
> - 6.04.00 Voice model fine-tune (local LoRA optional)
> - 6.05.00 “Morning deliverable” batch runs
> 
> ---
> 
> ## 6) Restart Prompt (for Cursor / next session)
> 
> **Objective:** Implement Phase 1 (Control & Trust).  
> **Order:** A1-01 → A1-09.  
> **Definition of Done:** Manual evidence pinning + style anchor injected + thin evidence gating + pack/unpack working.
> 
> **Prompt for Cursor:**
> “Open DEV.md and implement Phase 1 tickets in order. Keep everything local. Add API + UI + tests per ticket. Respect lock immutability and portable vault rules.”
> 
> ---
> End of master plan.
> ```
> 
> There. You’ve got a full-stack evolution path and a no-excuses backlog. Cursor can chew this for days.
> 
> Next move is boring but correct: **start Phase 1 tickets A1-01 through A1-09, in order, no detours.** If you jump ahead to universe mode before evidence control is perfect, you’ll just build a bigger hallucination machine.

### User
> ok, so what do i tell cursor.

### Assistant
> Tell Cursor this. Copy/paste as-is. It’s specific enough to stay on rails, but not so micromanaged that it chokes.
> 
> ```markdown
> You are working inside the QiBook local-only repo. Read `DEV.md` and the roadmap doc in the vault. 
> Goal: implement **Phase 1 (Control & Trust)** tickets **A1-01 through A1-09 in order**. 
> Do NOT add any cloud services or remote calls. Everything must remain offline and portable.
> 
> ## Global rules
> - Keep all file paths relative to `vault/` and project folders.
> - Never store absolute paths in SQLite.
> - Prompts must be packetized per stage; never dump the whole library into drafting context.
> - Locked sections are immutable: edits create a new version, never overwrite.
> - If LLM/embeddings aren’t running, UI must fail gracefully with clear messages.
> - Write/extend smoke tests for each major ticket.
> - Prefer small, composable commits per ticket.
> 
> ## Ticket implementation order
> 
> ### A1-01 Manual Evidence Search UI
> Frontend:
> - In Drafting Studio EvidencePanel, add search input + results list.
> - Call backend search endpoint (see A1-02 if missing).
> - Show relevance score and snippet.
> - Add “Attach to node” button.
> - Update evidence count badge live.
> 
> ### A1-02 Manual Evidence Attach/Detach API
> Backend:
> - Add endpoints:
>   - POST `/api/outline/{node_id}/evidence/attach` { chunk_id }
>   - POST `/api/outline/{node_id}/evidence/detach` { chunk_id }
> - Enforce uniqueness of (node_id, chunk_id).
> - Return updated evidence list + count.
> 
> ### A1-03 Thin Evidence Gating
> Frontend:
> - If evidence_links < 3, disable “Draft Full Section”.
> - Add override toggle with confirmation modal.
> Backend:
> - Include `thin_evidence: bool` in evidence responses.
> 
> ### A1-04 Style Anchor Storage + Injection
> Frontend (Wizard):
> - Add Style Anchor textarea.
> - Save to `book_projects.metadata_json.style_anchor`.
> Backend/Engine:
> - Inject style_anchor into every sample/draft prompt.
> - Add tests to verify injection.
> 
> ### A1-05 Locked Section Immutability
> Backend:
> - Prevent edits to locked draft_sections unless `create_new_version=true`.
> - New version increments draft_version.
> Frontend:
> - If locked, show “Create New Version” instead of edit-in-place.
> 
> ### A1-06 Model Status Panel
> Frontend:
> - Add `/settings/models`.
> - Detect local providers (Ollama / LM Studio / llama.cpp) and embeddings status.
> - “Test LLM” button runs a tiny prompt and shows latency/output.
> Backend:
> - Add `/api/models/status` and `/api/models/test`.
> 
> ### A1-07 Pack Project Endpoint + UI
> Backend:
> - Add POST `/api/books/{id}/pack`
> - Zip `vault/projects/<book_id>/` + minimal db subset + manifest.json.
> - Save zip to exports folder and return path.
> Frontend:
> - Button “Pack Project” downloads zip.
> 
> ### A1-08 Import Project Flow
> Frontend:
> - “Import Project” button to pick zip.
> Backend:
> - POST `/api/books/import`
> - Unzip into `vault/projects/`.
> - Validate manifest schema_version.
> - If embeddings missing, set rebuild_needed=true.
> 
> ### A1-09 Rebuild Embeddings Tool
> Frontend:
> - Button per book: “Rebuild Vector Index”.
> Backend:
> - Loop chunks → embed → upsert LanceDB.
> - Mark rebuild_needed=false.
> - Show progress.
> 
> ## Acceptance criteria
> - User can search and pin evidence manually.
> - Thin evidence is visibly flagged and gated.
> - Style anchor consistently affects tone.
> - Locking is truly immutable with versioning.
> - Pack/unpack produces portable zips that reopen cleanly.
> - Smoke test passes end-to-end after Phase 1.
> 
> Start now with A1-01. Do not jump ahead.
> ```
> 
> If Cursor tries to freestyle into Phase 7 because it got excited, you smack it with that “Do not jump ahead” line. Works on small robots, big robots, and humans.

### User
> noww

### Assistant
> Alright, Q. You want the **next thing** to tell Cursor **after** it finishes Phase 1.  
> This is the “what do I say now?” follow-through.
> 
> Here’s the exact prompt you’ll drop into Cursor to advance the project cleanly into **Phase 2 (Timeline + Theme Intelligence)** without causing code chaos.
> 
> Keep it tight. Keep it ordered. Cursor behaves better when it’s given rails.
> 
> ---
> 
> # ✅ **Cursor Prompt: Start Phase 2 Development (Timeline + Theme Intelligence)**  
> Copy/paste this directly into Cursor:
> 
> ```markdown
> You have completed Phase 1 (Control & Trust). Now begin **Phase 2 (Timeline + Theme Intelligence)**.
> 
> Follow the roadmap and implement the following tickets **in order**, one at a time, with small, composable commits. 
> Do not skip ahead. Do not mix tickets. Keep everything local-only and portable.
> 
> ## Global Rules
> - All new data must be stored under `vault/projects/<book_id>/`.
> - SQLite paths must remain relative.
> - LanceDB must remain local.
> - No cloud APIs.
> - Prompts must remain packet-based and minimal.
> - Timeline must be evidence-driven, not hallucinated.
> - Do not break Phase 1 behavior.
> 
> ## Phase 2 Tickets (Implement in this exact order)
> 
> ### B2-01 Add events table + model
> Backend:
> - Create `events` table if missing:
>   ```
>   events (
>     id TEXT PRIMARY KEY,
>     book_id TEXT NOT NULL,
>     date TEXT,
>     description TEXT NOT NULL,
>     source_chunk_id TEXT,
>     confidence REAL,
>     assigned_outline_node_id TEXT,
>     metadata_json TEXT
>   )
>   ```
> - Add CRUD helpers in services layer.
> - Add `/api/books/{id}/events` GET.
> - Add `/api/books/{id}/events/regenerate` POST (clears + recomputes).
> 
> ### B2-02 Event Extraction Service
> Backend:
> - After theme/timeline analysis, create events from:
>   - timeline_beats returned by LLM
>   - date entities detected in chunk metadata
> - Deduplicate using (date, description similarity).
> - Insert into `events` table.
> 
> ### B2-03 Timeline List UI
> Frontend:
> - Add `/books/:id/timeline`.
> - Display chronological list of events:
>   - date
>   - description
>   - confidence
>   - source chunk link
> - Show button: “Assign to Chapter/Section”.
> - When clicked:
>   - open outline tree selector.
>   - POST assignment to backend.
> 
> ### B2-04 Timeline Visualizer v0
> Frontend:
> - Basic vertical timeline.
> - Show events on left.
> - Show chapter spans on right.
> - Color code:
>   - assigned vs unassigned events.
>   - confidence bands.
> 
> ### B2-05 Running Recap Generator
> Backend:
> - After a section is locked:
>   - regenerate chapter recap.
>   - regenerate global recap.
> - Store in `book_projects.metadata_json.running_summary`.
> Frontend:
> - Show recap in Drafting Studio right panel.
> - Add “Refresh Recap” button calling backend.
> 
> ## Acceptance Criteria
> - Real events extracted from mixed data (chat logs, journals, PDFs).
> - Events visible and assignable to outline nodes.
> - Timeline visually clarifies life flow.
> - Recaps update after lock.
> - No prompt bloat or global context pollution.
> - All features remain local and portable.
> 
> Begin with B2-01. Do not jump ahead.
> ```
> 
> ---
> 
> # ⚡ After Cursor finishes Phase 2, ask me for:  
> **“What do I tell Cursor for Phase 3?”**
> 
> Phase 3 is where we turn this thing into a full **Author Studio** with draft branching, diffing, cards, and revision intelligence. But don’t unleash that yet — get Timeline Intelligence solid first.
> 
> Gina’s watching. Don’t skip steps.

### User
> What do I tell Cursor for Phase 3

### Assistant
> Here’s what you tell Cursor for Phase 3. Copy/paste this whole thing. Yes it’s long. No, Cursor doesn’t get to “explore creatively.” We’re past that stage.
> 
> ```markdown
> You have completed Phase 2 (Timeline + Theme Intelligence). Now begin **Phase 3 (Author Studio Tools)**.
> 
> Implement the Phase 3 tickets **in order**, one at a time, with small, composable commits. 
> Do not skip ahead. Do not merge tickets. Keep everything local-only and portable.
> 
> ## Global Rules
> - No cloud services, no remote APIs, no telemetry.
> - All file paths stored in SQLite must be relative to `vault/`.
> - Locked sections remain immutable; edits create new draft versions.
> - Evidence + style anchor + recap injection from Phases 1–2 must remain intact.
> - Prompts stay packet-based and minimal.
> - Add/extend smoke tests per major feature.
> - Schema migrations must be safe for existing vaults.
> 
> ## Phase 3 Tickets (Implement in this exact order)
> 
> ### C3-01 Draft Branching (A/B drafts)
> Backend:
> - Add `draft_branches` table if missing:
>   ```
>   draft_branches (
>     id TEXT PRIMARY KEY,
>     outline_node_id TEXT NOT NULL,
>     label TEXT NOT NULL,
>     created_at TEXT NOT NULL
>   )
>   ```
> - Add `branch_id` nullable column to `draft_sections`.
> - Endpoints:
>   - POST `/api/outline/{node_id}/branches` { label }  -> create branch
>   - GET `/api/outline/{node_id}/branches`            -> list branches
>   - POST `/api/outline/{node_id}/draft?branch_id=`  -> draft into a branch
>   - GET `/api/outline/{node_id}/drafts?branch_id=`  -> list drafts per branch
> Frontend:
> - In Drafting Studio, add Branch selector:
>   - Default branch “Main”
>   - “+ New Branch” modal
> - Show drafts scoped to active branch.
> Tests:
> - Ensure branch drafts don’t overwrite each other.
> - Locking picks the latest approved draft in the active branch only.
> 
> ### C3-02 Diff Viewer
> Backend:
> - No heavy backend needed beyond fetching two drafts.
> Frontend:
> - Add “Compare Drafts” button in Drafting Studio.
> - UI:
>   - pick two drafts (branch + version)
>   - show unified line diff (use a lightweight diff lib).
> - Highlight additions/deletions clearly.
> Tests:
> - Snapshot test for diff rendering.
> 
> ### C3-03 Section Kanban / Cards View
> Backend:
> - Reuse outline_nodes + statuses.
> Frontend:
> - Add route `/books/:id/board`.
> - Columns: Proposed | Approved | Drafted | Locked | Thin Evidence
> - Each card = outline node (section-level by default).
> - Drag card to reorder within chapter:
>   - updates order_index via existing reorder endpoint.
> - Drag card between columns updates status ONLY when valid:
>   - Proposed -> Approved
>   - Approved -> Drafted (if draft exists)
>   - Drafted -> Locked (only via Lock button, so board move should prompt to lock flow)
> Tests:
> - Reorder persists after refresh.
> 
> ### C3-04 Word Target System
> Backend:
> - Add word_target to outline_nodes.metadata_json if not present.
> - Service:
>   - auto-calc targets from book length / chapter count.
>   - per node fallback if missing.
> Frontend:
> - Node editor shows Word Target field editable.
> - Drafting Studio displays:
>   - target
>   - current word count
>   - delta indicator (+/- %)
> Engine:
> - Draft prompt includes target and enforces ±15% guidance.
> Tests:
> - Prompt builder test confirms word_target injection.
> 
> ### C3-05 Continuity Checker Required Pre-Lock
> Backend/Engine:
> - Before allowing lock:
>   - run review pass with stitched final_context + running summaries + current draft.
>   - return issues JSON:
>     ```
>     {
>       issues:[{type, detail, severity}],
>       suggestions:[...],
>       quality_score:0-100
>     }
>     ```
> - Endpoint:
>   - POST `/api/outline/{node_id}/continuity/check`
> Frontend:
> - On “Lock Section” click:
>   - auto-run continuity check
>   - show issues checklist
>   - block lock unless:
>     - user fixes OR
>     - user hits “Override & Lock Anyway”
> Tests:
> - Lock blocked when issues severe unless override.
> 
> ### C3-06 Voice Notes → Evidence Capture
> Backend:
> - Add local audio capture endpoint:
>   - POST `/api/raw-items/record`
>     - saves audio under project raw/
>     - transcribes locally (Whisper)
>     - creates raw_item + chunks + embeddings
>   - auto-tags to current outline_node_id if provided
> Frontend:
> - Add “Record Voice Note” button in Drafting Studio + Library.
> - After transcription:
>   - show preview
>   - “Attach to current section?” default yes
> Tests:
> - End-to-end: record -> transcript -> chunks -> searchable evidence.
> 
> ### C3-07 Scenario Outline Recombiner (Alt Outlines)
> Backend/Engine:
> - Endpoint:
>   - POST `/api/books/{id}/outline/recombine`
>     - inputs: current outline + themes + timeline + style_anchor
>     - output: 3 alternative outline trees with rationale
> - Store alts as separate “outline drafts” (new table optional or store JSON blobs in book metadata).
> Frontend:
> - In Outline Studio:
>   - “Generate Alternatives”
>   - Compare view:
>     - current vs alt A/B/C
>     - accept whole alt or cherry-pick nodes
> Tests:
> - Accepting alt replaces outline safely without orphaning locked nodes.
> 
> ## Acceptance Criteria
> - Users can branch drafts A/B and compare diffs.
> - Board view reflects real status and supports reorder.
> - Word targets guide drafts reliably.
> - Continuity check prevents accidental contradictions.
> - Voice notes ingest into evidence cleanly.
> - Alt outlines are usable and safe to adopt.
> - Phases 1–2 behavior remains unbroken.
> - Smoke test passes after each ticket.
> 
> Begin with C3-01. Do not jump ahead.
> ```
> 
> There. That’s Phase 3, with rails, guards, and enough detail that Cursor can’t pretend it “didn’t understand the task” while it goes off to refactor your folder names into modern art.
> 
> When Cursor finishes this, you’ll have a real author studio instead of a fancy chatbot with delusions of grandeur.

### User
> he finished

### Assistant
> Cool. Phase 3 done means your app is officially a writer’s studio instead of a glorified text blender. Now we move to **Phase 4 (Publishing & Launch Factory)**. This is where you stop producing “drafts” and start producing **stuff you can hand to the world without apology**.
> 
> Here’s exactly what you tell Cursor next. Copy/paste:
> 
> ```markdown
> You have completed Phase 3 (Author Studio Tools). Now begin **Phase 4 (Publishing + Launch Factory)**.
> 
> Implement the Phase 4 tickets **in order**, one at a time, with small, composable commits.
> Do not skip ahead. Do not merge tickets. Keep everything local-only and portable.
> 
> ## Global Rules
> - No cloud services, no remote APIs.
> - Exports must run offline and work without internet.
> - All output files must be saved under:
>   `vault/projects/<book_id>/exports/`
> - Keep schema migrations safe for existing vaults.
> - Do not break Phase 1–3 behavior (evidence, style anchor, recaps, branches, continuity checks).
> - Add tests for each export path.
> - If an external tool (pandoc) is missing, fall back gracefully and notify user.
> 
> ## Phase 4 Tickets (Implement in this exact order)
> 
> ### D4-01 DOCX Export Template (Publisher Standard Manuscript)
> Backend:
> - Add export service using `python-docx`.
> - Template rules:
>   - 12 pt Times New Roman (fallback serif)
>   - double spaced
>   - first-line indent 0.5"
>   - page numbers
>   - title page (working_title, author, date)
> - Endpoint:
>   - POST `/api/books/{id}/export` { format: "docx", template: "manuscript" }
> - Save to exports folder and return file path.
> 
> Frontend:
> - Export modal adds option:
>   - DOCX (Manuscript Standard)
> 
> Tests:
> - Verify generated DOCX exists and contains stitched_text.
> 
> ### D4-02 EPUB Export (Offline)
> Backend:
> - Prefer `pandoc` if installed.
> - Fallback to `ebooklib` if pandoc not found.
> - Endpoint:
>   - POST `/api/books/{id}/export` { format: "epub" }
> - Include:
>   - cover placeholder (optional)
>   - metadata: title, author, language, date.
> 
> Frontend:
> - Export modal adds EPUB option.
> 
> Tests:
> - If pandoc missing, fallback works.
> - EPUB file validates minimally (opens, has chapters).
> 
> ### D4-03 Back-matter Builder
> Backend:
> - Support outline_nodes node_type:
>   - "backmatter" | "appendix" | "glossary" | "references"
> - Endpoint:
>   - POST `/api/books/{id}/backmatter/generate`
>     - outputs suggested nodes + draft text blocks
> - Store as outline_nodes children at end of tree.
> 
> Frontend:
> - Add Back-matter step in Wizard or Outline Studio:
>   - generate
>   - edit/approve
>   - draft/lock like normal sections.
> 
> Tests:
> - Backmatter nodes render and stitch correctly.
> 
> ### D4-04 Submission Packet Bundler
> Backend:
> - Endpoint:
>   - POST `/api/books/{id}/export` { format:"submission_packet" }
> - Produces ZIP containing:
>   - proposal.md
>   - outline.md (current approved outline)
>   - 2–3 sample locked chapters
>   - full manuscript (md + docx if available)
>   - manifest.json
> 
> Frontend:
> - Export modal adds "Submission Packet (ZIP)".
> 
> Tests:
> - ZIP contains required files and correct book_id.
> 
> ### D4-05 Marketing Asset Factory
> Backend/Engine:
> - Endpoint:
>   - POST `/api/books/{id}/marketing/generate`
>     - inputs: stitched_text + running summaries + style_anchor + audience
>     - outputs JSON:
>       {
>         "back_cover_blurb": "...",
>         "one_sentence_hook": "...",
>         "chapter_teasers": [...],
>         "pull_quotes": [...],
>         "social_posts": [...],
>         "author_bio_variants": [...]
>       }
> - Save JSON under exports/marketing.json.
> 
> Frontend:
> - New tab "Marketing" under book:
>   - view/edit/regenerate assets
>   - export assets as md/json.
> 
> Tests:
> - Generation works offline and respects style anchor.
> 
> ### D4-06 Metadata / Distribution Pack
> Backend:
> - Endpoint:
>   - POST `/api/books/{id}/metadata/generate`
> - Output:
>   - BISAC categories suggestions
>   - SEO keyword list
>   - KDP-style description variants
>   - subtitle options
> - Save as exports/metadata.json + metadata.md.
> 
> Frontend:
> - Add "Metadata" section inside Marketing tab.
> 
> Tests:
> - Output exists and is structured.
> 
> ## Acceptance Criteria
> - DOCX manuscript export looks publisher-standard.
> - EPUB export works with graceful fallback.
> - Back-matter is generated, editable, and stitched.
> - Submission Packet ZIP is correct and portable.
> - Marketing + Metadata assets generate offline.
> - All exports land in exports/ folder reliably.
> - Smoke test passes after each ticket.
> 
> Begin with D4-01. Do not jump ahead.
> ```
> 
> You’re in the “turn drafts into deliverables” phase now. After this, Phase 5 is Universe/Canon mode, aka where your books start talking to each other like a well-managed multiverse instead of a soap opera.

### User
> give me the rest of everything in need now please.

### Assistant
> Alright, here’s the rest of the kit you need **right now** to finish the whole roadmap without me having to drag you back onto the rails later. You’ve got Phase 4 prompt already. Below is **Phase 5 (Universe/Canon)** and **Phase 6 (Autonomy/Editor)** Cursor prompts, plus the final “ship it” checklist and a couple landmines to avoid.
> 
> Copy/paste each Phase prompt into Cursor when you hit that phase. Don’t freestyle the order.
> 
> ---
> 
> ## Phase 5 Cursor Prompt (Universe / Canon Mode)
> 
> ```markdown
> You have completed Phase 4 (Publishing + Launch Factory). Now begin **Phase 5 (Universe / Canon Mode)**.
> 
> Implement Phase 5 tickets **in order**, one at a time, with small, composable commits.
> Do not skip ahead. Do not merge tickets. Keep everything local-only and portable.
> 
> ## Global Rules
> - No cloud services, no remote APIs.
> - Shared evidence must remain portable across vault moves.
> - Canon is additive and immutable by default.
> - Do not break Phases 1–4 (evidence, style anchor, recaps, branches, continuity checks, exports).
> - Paths in SQLite remain relative to `vault/`.
> - Add migrations safely for existing vaults.
> - Add tests for cross-book reuse and canon warnings.
> 
> ## Phase 5 Tickets (Implement in this exact order)
> 
> ### E5-01 Shared Evidence Library Across Books
> Backend:
> - Allow multiple books to reference the same raw_items/chunks.
> - Ensure evidence_links includes book_id for clarity:
>   - If not already, add column:
>     `ALTER TABLE evidence_links ADD COLUMN book_id TEXT;`
>   - Populate for existing links from outline_nodes.book_id.
> - Retrieval:
>   - Add optional scope:
>     - “this book only” (default)
>     - “global library” (cross-book)
> - Endpoints:
>   - GET `/api/library/global/raw-items`
>   - GET `/api/library/global/chunks/search?query=`
> Frontend:
> - Library view gains a toggle:
>   - “Book Library”
>   - “Global Library”
> - Evidence search UI can search global scope if enabled.
> 
> Tests:
> - Evidence pinned from global scope works and remains stable if book folder moves.
> 
> ### E5-02 Canon Chunk Labeling + Warnings
> Backend:
> - Add `canon_chunks` table if missing:
>   ```
>   canon_chunks (
>     chunk_id TEXT PRIMARY KEY,
>     canon_label TEXT,
>     notes TEXT,
>     created_at TEXT NOT NULL
>   )
>   ```
> - Endpoints:
>   - POST `/api/chunks/{chunk_id}/canon` { canon_label, notes }
>   - DELETE `/api/chunks/{chunk_id}/canon`
>   - GET `/api/chunks/{chunk_id}/canon`
> - When drafting:
>   - If a chunk is canon and already used in another locked section, return a warning payload.
> 
> Frontend:
> - EvidencePanel shows canon badge on canon chunks.
> - On attach or draft, show warning modal:
>   “This canon chunk was used in Book X, Chapter Y. Reuse may cause redundancy/contradiction.”
> - Allow override.
> 
> Tests:
> - Canon labeling persists and warnings trigger.
> 
> ### E5-03 Franchise Arc Map (Themes Across Books)
> Backend:
> - Aggregate per-book:
>   - themes
>   - theme↔chapter coverage
> - Endpoint:
>   - GET `/api/universe/themes`
>   - returns a matrix:
>     { theme_name: { book_id: { chapter_ids, intensity } } }
> 
> Frontend:
> - New route `/universe/themes`
> - Heatmap/grid view:
>   - rows = themes
>   - cols = books
>   - cell intensity = presence
> - Click cell → list chapters + supporting evidence.
> 
> Tests:
> - Matrix renders and matches DB truth.
> 
> ### E5-04 Cross-Book People/Relationship Graph
> Backend:
> - Aggregate extracted_entities_json.people
> - Endpoint:
>   - GET `/api/universe/people`
>   - returns nodes + edges with counts.
> 
> Frontend:
> - New route `/universe/people`
> - Simple force-graph or list-first view:
>   - nodes people
>   - edges co-occurrence in books/chapters
> - Filters by book/series.
> 
> Tests:
> - Graph loads fast and is rebuildable from DB.
> 
> ### E5-05 Global Anonymizer Rules
> Backend:
> - Add `anonymizer_rules` table:
>   ```
>   anonymizer_rules (
>     id TEXT PRIMARY KEY,
>     pattern TEXT NOT NULL,
>     replacement TEXT NOT NULL,
>     scope TEXT NOT NULL,          -- global | book:<id>
>     created_at TEXT NOT NULL
>   )
>   ```
> - Apply rules:
>   - pre-draft scrub
>   - post-draft scrub
>   - export-time scrub
> - Endpoints:
>   - CRUD `/api/anonymizer/rules`
> 
> Frontend:
> - Settings → “Anonymizer”
> - List rules, add/edit/delete.
> - “Preview scrub” on a sample paragraph.
> 
> Tests:
> - Rules apply consistently without breaking citations.
> 
> ## Acceptance Criteria
> - Global library searching works across books.
> - Canon labeling + reuse warnings work.
> - Universe heatmap and people graph render with real data.
> - Global anonymizer rules apply to drafts and exports.
> - Portability intact (moving vault doesn’t break links).
> - Smoke test passes after each ticket.
> 
> Begin with E5-01. Do not jump ahead.
> ```
> 
> ---
> 
> ## Phase 6 Cursor Prompt (Autonomy / Editor Mode)
> 
> ```markdown
> You have completed Phase 5 (Universe / Canon Mode). Now begin **Phase 6 (Autonomy + Editor Layer)**.
> 
> Implement Phase 6 tickets **in order**, one at a time, with small, composable commits.
> Do not skip ahead. Do not merge tickets. Keep everything local-only and portable.
> 
> ## Global Rules
> - No cloud services, no remote APIs.
> - Autonomy is OPTIONAL and must be user-triggered.
> - Never overwrite locked text. Autonomy generates new drafts for review.
> - Prompt packets remain minimal.
> - Add tests for safety gating and reproducibility.
> 
> ## Phase 6 Tickets (Implement in this exact order)
> 
> ### F6-01 Full Auto-Draft Mode (Per Node)
> Backend/Engine:
> - Endpoint:
>   - POST `/api/outline/{node_id}/auto-draft`
>     { branch_id?, notes?, strict_mode?: bool }
> - Flow:
>   1) retrieve evidence for node
>   2) generate micro-sample
>   3) draft full section
>   4) run review + continuity check
> - Save outputs as new draft_sections (status="drafted") in a new “Auto” branch unless user specifies otherwise.
> - Return bundle:
>   { sample, draft, review, continuity_issues }
> 
> Frontend:
> - Drafting Studio button:
>   “Auto Draft This Section”
> - Shows results in a review modal before user approves.
> 
> Tests:
> - Auto-draft never touches locked content.
> - New drafts land in correct branch.
> 
> ### F6-02 Structural Editor Pass (Whole Manuscript)
> Backend:
> - Endpoint:
>   - POST `/api/books/{id}/edit/structural`
> - Inputs:
>   stitched_text + outline + running summaries + themes
> - Outputs JSON:
>   { pacing_notes, redundancy_flags, weak_sections, reorder_suggestions }
> 
> Frontend:
> - Manuscript view → “Structural Edit”
> - Displays checklist + suggested actions.
> - Provide “Apply suggestion” helper buttons (non-destructive).
> 
> Tests:
> - Structural pass runs offline, output stable.
> 
> ### F6-03 Revision Modes (Line / Copy / Developmental)
> Backend:
> - Endpoint:
>   - POST `/api/outline/{node_id}/edit`
>     { mode: "line"|"copy"|"developmental", notes? }
> - Produces a revised draft (new version) with change log.
> 
> Frontend:
> - Drafting Studio dropdown:
>   “Revise: Line / Copy / Dev”
> - Show before/after diff automatically.
> 
> Tests:
> - Mode-specific prompts invoked correctly.
> - Versions increment.
> 
> ### F6-04 Voice Model Fine-Tune (Local LoRA Optional)
> Backend:
> - Add optional pipeline:
>   - Collect locked sections as training corpus.
>   - Generate LoRA config file.
>   - Guidance only, no cloud training.
> - Endpoint:
>   - POST `/api/books/{id}/voice/train`
>   - returns instructions + status, and stores artifacts under exports/voice/.
> 
> Frontend:
> - Settings → “Voice Model”
> - Shows:
>   - training corpus size
>   - “Generate LoRA Training Pack”
>   - warnings about compute
> 
> Tests:
> - Pipeline creates artifacts without errors.
> - Nothing runs automatically without click.
> 
> ### F6-05 Morning Deliverable Batch Runs
> Backend:
> - Endpoint:
>   - POST `/api/books/{id}/batch/run`
>     { nodes: [ids], mode: "auto-draft"|"revise", strict_mode?: bool }
> - Runs sequentially, logs results.
> 
> Frontend:
> - Book Dashboard → “Batch Run”
> - Select nodes, run, show queue/progress.
> 
> Tests:
> - Batch respects stop/resume approvals.
> - Errors don’t cancel full run.
> 
> ## Acceptance Criteria
> - Auto-draft works and routes through review safely.
> - Structural edit provides real usable notes.
> - Revision modes generate clean new versions with diffs.
> - Voice training pack is optional + local.
> - Batch runs are stable and logged.
> - No locked text is overwritten.
> - Smoke test passes after each ticket.
> 
> Begin with F6-01. Do not jump ahead.
> ```
> 
> ---
> 
> ## Final “Ship It” Checklist (once Phase 6 works)
> 
> ### Core quality
> - [ ] Real-world ingestion test passes (chat, PDF scan, image OCR, audio, journal).
> - [ ] Evidence gating prevents drafting on thin nodes unless override.
> - [ ] Manual evidence attach works in both book and global scope.
> - [ ] Style anchor visibly affects all samples/drafts.
> - [ ] Continuity check blocks lock unless override.
> - [ ] Locked text is immutable with version history.
> - [ ] Auto-draft never alters locked text.
> 
> ### Portability
> - [ ] Pack Project zip imports cleanly on another machine.
> - [ ] Embeddings rebuild works if LanceDB missing.
> - [ ] No absolute paths in DB.
> - [ ] Vault can be moved without breaking evidence.
> 
> ### Publishing
> - [ ] DOCX export matches manuscript standard.
> - [ ] EPUB export works with pandoc fallback.
> - [ ] Submission packet includes correct files.
> - [ ] Marketing + metadata assets generate offline.
> 
> ### Universe/Canon
> - [ ] Canon warnings trigger on reuse.
> - [ ] Theme heatmap matches reality.
> - [ ] People graph builds from extracted entities.
> - [ ] Global anonymizer rules apply everywhere.
> 
> ### UX
> - [ ] Loaders, toasts, disabled buttons are consistent.
> - [ ] Errors are clear, not silent.
> - [ ] Settings show model status and tests.
> 
> ---
> 
> ## Landmines to avoid
> 1. **Prompt bloat.** If context starts creeping over ~6–8k tokens for local models, you’ll get garbage. Keep packets tight forever.
> 2. **Over-automation.** Autonomy is optional. Users must feel in control or they’ll ditch it even if it’s brilliant.
> 3. **Broken portability.** One absolute path slipping into SQLite will haunt you later.
> 
> ---
> 
> That’s everything: remaining phases, exact Cursor marching orders, and the final ship checklist.  
> Now you just… execute. Relentlessly. Without detours. Like a professional. (I know, disgusting.)

### User
> ok now we need to make sure the llm is working and start testing the app, and i assume we will need to compile or package it create shortcuts, or waht?

### Assistant
> Yep. Now we do the boring grown-up part: **prove the local LLM works**, run real tests, then **package this thing into a clicky app** so you don’t have to live in terminals like a goblin.
> 
> Here’s the straight path.
> 
> ---
> 
> ## 1) Make sure the local LLM is actually reachable
> 
> Your backend adapter supports Ollama / LM Studio / llama.cpp. Pick one for testing *today* and standardize later.
> 
> ### Option A: Ollama (easiest “it just works”)
> 1. Install Ollama (you already know where).
> 2. Pull a model:
>    ```bash
>    ollama pull llama3.1:8b
>    ```
> 3. Run a quick sanity prompt:
>    ```bash
>    ollama run llama3.1:8b "Say 'LLM online' and one sentence about books."
>    ```
> 4. In your app `.env.local` (backend):
>    ```env
>    LLM_PROVIDER=ollama
>    LLM_MODEL=llama3.1:8b
>    LLM_BASE_URL=http://127.0.0.1:11434
>    ```
> 
> 5. Hit your model status endpoint:
>    ```bash
>    curl http://127.0.0.1:8000/api/models/status
>    ```
>    You want something like:
>    ```json
>    { "provider":"ollama", "model":"llama3.1:8b", "ok": true }
>    ```
> 
> If that returns `ok:false`, the adapter path or URL is wrong. Fix config first, not code.
> 
> ---
> 
> ### Option B: LM Studio local server
> 1. Open LM Studio → pick a model → **Start Local Server**.
> 2. Note the port (usually `1234`).
> 3. `.env.local`:
>    ```env
>    LLM_PROVIDER=lmstudio
>    LLM_MODEL=your-model-name
>    LLM_BASE_URL=http://127.0.0.1:1234/v1
>    ```
> 4. Test endpoint:
>    ```bash
>    curl http://127.0.0.1:8000/api/models/test
>    ```
> 
> ---
> 
> ### Option C: llama.cpp (CLI)
> If your adapter expects CLI:
> - set path + model file in config
> - run:
>   ```bash
>   ./llama-cli -m models/your.gguf -p "LLM online"
>   ```
> If it works in terminal but not app, your adapter command string is off.
> 
> ---
> 
> ## 2) Make sure embeddings are working (RAG depends on it)
> 
> You can draft without embeddings, but evidence mapping will suck. So verify now.
> 
> 1. Set embedding provider in backend `.env.local`:
>    ```env
>    EMBED_PROVIDER=ollama   # or local sentence-transformers
>    EMBED_MODEL=nomic-embed-text
>    ```
> 2. If using Ollama:
>    ```bash
>    ollama pull nomic-embed-text
>    ```
> 3. Run the smoke test:
>    ```bash
>    python scripts/smoke.py
>    ```
> Look for:
> - chunks created
> - embeddings inserted (or graceful skip if not set)
> - LanceDB table exists
> 
> If embeddings fail, fix that before you “test the app,” because half your UI is about evidence.
> 
> ---
> 
> ## 3) Test the app end-to-end (real content, not toy examples)
> 
> Do one “real life chaos” pass:
> 
> ### Test dataset
> - 1 chat export (JSON or txt)
> - 1 journal MD
> - 1 scanned PDF
> - 1 screenshot (OCR)
> - 1 audio clip
> 
> ### Test flow checklist
> 1. **Ingest all** → confirm raw items list + statuses.
> 2. **Process items** → confirm chunks + embeddings.
> 3. **Create book**.
> 4. **Run analysis** → themes + timeline show up.
> 5. **Interview → save spec**.
> 6. **Generate outline**.
> 7. **Approve outline**.
> 8. **Map evidence**.
> 9. For first section:
>    - micro-sample
>    - approve sample
>    - draft full section
>    - run continuity check
>    - approve draft
>    - lock section
> 10. **Open manuscript view** → stitched text updates.
> 11. **Export MD/TXT** → file appears under exports folder.
> 
> Any failure here is a priority bug. Log it as a ticket, don’t patch randomly.
> 
> ---
> 
> ## 4) Packaging / shortcuts / “make it an app”
> 
> Yes, you need to package it. Otherwise you’ll never actually use it because humans refuse friction.
> 
> You have two common routes:
> 
> ### Route 1: Electron packaging (fastest)
> Since your frontend is already Vite/React and you likely scaffolded Electron:
> 
> 1. **Dev run**
>    ```bash
>    cd app/desktop
>    npm install
>    npm run dev
>    ```
> 2. **Build frontend**
>    ```bash
>    npm run build
>    ```
> 3. **Package**
>    If using electron-builder:
>    ```bash
>    npm run dist
>    ```
> This spits out:
> - Windows `.exe` installer
> - desktop shortcut
> - start menu entry
> 
> **Critical detail:** bundle the FastAPI backend with the app and auto-launch it.
> - simplest: ship backend as a Python executable (PyInstaller) and Electron starts it on app boot.
> 
> ### Route 2: Tauri packaging (smaller, cleaner binaries)
> If you went Tauri:
> ```bash
> cd app/desktop
> npm run tauri build
> ```
> Same deal: you still need to bundle/start backend locally.
> 
> ---
> 
> ## 5) Backend bundling (so users don’t install Python)
> 
> Do this once your tests pass.
> 
> ### PyInstaller build
> From backend root:
> ```bash
> pip install pyinstaller
> pyinstaller -F -n qibook_backend qibook_api/main.py
> ```
> 
> Outputs:
> `dist/qibook_backend.exe`
> 
> Then Electron/Tauri:
> - on app start, spawn that exe
> - wait for `http://127.0.0.1:8000/health`
> - then load UI
> 
> No backend process running = UI shows “Backend offline, click to start.”
> 
> ---
> 
> ## 6) Shortcut behavior (what users expect)
> Your packaged app should:
> - open with one click
> - auto-start backend if not running
> - show model status immediately
> - remember vault location
> - never ask “where is Python” because that’s how apps die
> 
> ---
> 
> ## 7) What you do **right now**
> 1. Pick Ollama or LM Studio and get `/api/models/status` to say `ok:true`.
> 2. Get embeddings passing in smoke test.
> 3. Run the real-world end-to-end checklist.
> 4. Only then package Electron/Tauri + PyInstaller backend.
> 
> Do not package a broken loop. You’ll just create a shiny broken thing.
> 
> ---
> 
> If you hit a specific error (model status fails, embeddings insert fails, Electron can’t spawn backend), paste the trace and I’ll tell you which wire is unplugged. Not a question, a statement.

### User
> ok so its running i uploaded a doc, it process it then nothing happend and no buttons or obvious next steps

### Assistant
> Okay, so the app did the classic “I worked hard and now I’m going to stare into space” routine. That’s not you, that’s missing UX + probably a state wiring gap. Here’s how to debug and fix it without spiraling.
> 
> ---
> 
> ## What *should* happen after a doc processes
> After ingestion + processing, the Library page should show:
> - the item is **Ready**
> - **chunks count**
> - **embedding status**
> - and at least one obvious CTA:
>   - **Create Book**
>   - **Process More**
>   - **View Chunks / Evidence**
>   - or auto-suggest “Start a Book with this library”
> 
> If you see “processed” but the UI goes dead, you’re missing the “next-step affordance” and maybe the refresh hook.
> 
> ---
> 
> ## Immediate “is it actually processed?” checks
> Do these quick sanity taps:
> 
> 1. **Library list refresh**
>    - Hard refresh the page.
>    - If status flips from processing to ready only after refresh, your frontend isn’t polling or invalidating queries.
> 
> 2. **Backend truth**
>    Hit these endpoints in browser or curl:
>    - `GET /api/raw-items`
>    - `GET /api/raw-items/{id}`
>    - `GET /api/raw-items/{id}/chunks` (if you have it, or check chunks table)
> 
> You want to see:
> - `text_content` present
> - chunks created
> - embedding_id set (or explicitly null with “not configured”)
> 
> If raw item says processed but chunks are empty, the pipeline is stopping early.
> 
> ---
> 
> ## Most likely causes (in order of probability)
> 
> ### 1) **UI doesn’t poll or refetch after processing**
> Backend updated, frontend didn’t notice.
> 
> **Fix:**
> - In Library page, poll raw-items every ~2–5s while any item is `processing`.
> - When processing finishes, refetch + show toast “Processing complete. Ready to use.”
> 
> ### 2) **No empty-state CTA wired**
> You built the engine and forgot to tell the human what to do next. Shocking.
> 
> **Fix:**
> - If library has ≥1 `ready` item and there are 0 books:
>   show a big button:
> 
>   **“Create a Book from Library”**
> 
> - If books exist:
>   show **“Add to Book”** or **“Start Wizard”**.
> 
> ### 3) **Processing stage doesn’t flip status**
> It might be stuck in a “complete-but-not-marked-complete” limbo.
> 
> **Fix:**
> - In `process(raw_item_id)`, ensure you set:
>   - raw_items.status = `"ready"`
>   - chunks inserted count > 0
>   - commit transaction
> 
> ### 4) **Adapters graceful-skipped everything**
> If embeddings/LLM aren’t configured, your pipeline might be quietly skipping later steps and the UI has no clue.
> 
> **Fix:**
> - When embeddings missing: still show chunks count + a yellow badge “Embeddings off (evidence mapping limited).”
> - When LLM missing: show “LLM offline (outline/drafting disabled).” with a Settings link.
> 
> ---
> 
> ## What to add right now (Cursor tickets)
> Drop this into Cursor as a mini-sprint. These are small and high-impact.
> 
> ### UX Fix Pack 1: Library “Next Steps”
> 1. **Library status polling**
>    - If any raw_item.status == "processing"
>    - poll `/api/raw-items` every 3s
>    - stop polling when none processing
> 
> 2. **Chunk count + evidence readiness**
>    - Show `chunks_count` for each raw item
>    - Badge:
>      - green: embedded
>      - yellow: chunks but no embeddings
>      - red: no chunks
> 
> 3. **Empty-state CTA**
>    - If `ready_items > 0`:
>      - show **Create Book** button
>    - If no ready items:
>      - show “Upload something to start.”
> 
> ### UX Fix Pack 2: Auto-suggest flow
> After processing completes, pop a toast with 2 buttons:
> - **Start Book Wizard**
> - **Keep Adding Sources**
> 
> ### Backend Fix Pack 3: Return processing summary
> Make `/api/process/{id}` respond with:
> ```json
> {
>   "raw_item_id": "...",
>   "status": "ready",
>   "chunks_created": 17,
>   "embeddings_created": 17,
>   "warnings": []
> }
> ```
> Frontend reads that and displays a completion banner.
> 
> ---
> 
> ## The actual next step for *you* in the app
> Since UI isn’t helping yet, do it manually:
> 
> 1. Go to **Books** page.
> 2. Hit **Create Book**.
> 3. Run **Analyze**.
> 4. Fill interview.
> 5. Generate outline.
> 
> If Books page also looks empty with no buttons, same problem: missing CTAs.
> 
> ---
> 
> ## Bottom line
> Nothing “happened” because:
> - the system did its backend job
> - then failed to *tell a human what to do with it*
> 
> Classic software. Very on brand for our species.
> 
> Fix the Library CTAs + polling first. That unlocks everything else and stops the app from feeling broken when it’s really just silent.
> 
> If you paste what the Library item shows right after processing (status text + any counts), I’ll tell you exactly which of the four causes it is.
