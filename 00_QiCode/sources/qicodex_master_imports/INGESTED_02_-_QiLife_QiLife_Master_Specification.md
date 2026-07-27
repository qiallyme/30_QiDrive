# QiLife Master Specification & Data Model Suite

> **Complete Consolidated Master Specification for QiLife Application, Architecture & Data Model**

## 04_QiLife_Master_Specification

# QiLife Master Specification & Data Model Spine

> **Consolidated Master Specification for QiLife Application & Core Engine**

## CHAPTER — QiLife App Spec

# CHAPTER — QiLife App Spec

Notes: Placed under existing chapter: qiapps_projects_integrations.
QiCode: § 07.02
Parent: Title 07 — Security & Access (Title%2007%20%E2%80%94%20Security%20&%20Access%208fbdb5a7433844f48ad0b371ccbee59b.md)
Status: active
Type: Chapter

---

# QiLife App Spec

## Chapter Purpose

This chapter defines the vision, architecture, modules, interface, workflows, expansion model, and documentation requirements for the QiLife app.

## Plain-English Summary

QiLife is the final organizer: a real second brain that remembers, organizes, and acts. It is not a chatbot or a gimmick. It is a sovereignty system built to connect files, notes, activity, communication, memory, and automation into one usable app.

## Scope

This chapter covers:

- Vision and architecture
- Foundations and environment
- Core modules
- UI and interaction
- Workflows and automation
- Expansion and collaboration
- DNA and documentation

This chapter does not cover:

- Full client delivery operations
- QiCode legal/governance language
- Published marketing copy
- Individual code implementation tickets

Those belong in their own specs, SOPs, or project tasks.

## Dependency

Before this chapter:

- QiEOS Protocol
- QiFileFlow naming and folder structure
- QiAlly technical stack decisions

After this chapter:

- Feature specs
- Module SOPs
- GitHub issues/tasks
- App deployment docs
- User onboarding templates

---

## § 5.10.001 — Vision & Architecture

### Rule

QiLife is designed as a true assistant that remembers, organizes, and acts.

### Meaning

QiLife is not just productivity software. It is a personal operating layer for memory, files, notes, daily activity, communication, and decision support.

### Mission

QiLife is the final organizer — a real second brain. Not a chatbot. Not a gimmick. A true assistant that *remembers*, *organizes*, and *acts*.

This isn’t productivity. **This is sovereignty.**

### Modular Pillars

- QiFileFlow™
- QiNote™
- QiLifeFeed™
- QiCall™
- QiMind™

### Architecture Prompts to Define

- Core philosophy: EmpowerQ, Orbit system, quantum logic
- User types
- Overall system diagram
- Tools and tech stack
- Constraints: privacy, offline fallback, OS, speed, security

---

## § 5.10.002 — Foundations & Environment

### Rule

The app needs stable foundations before feature expansion.

### Meaning

Before building the house, lay the pipes. The environment, naming, secrets, and utilities need to be clear before modules multiply.

### Foundation Areas

- Folder structure: local + cloud + Notion mirrors
- `.env` configs and secrets handling
- Git + GitHub best practices
- Dev environment: VS Code, Python, Copilot, Notion API, Google Drive API, OCR
- Shared utilities: `src/common/`
- Naming conventions: files, folders, commits, branches, databases

### Minimum Standard

No module should be considered stable until its environment, dependencies, configuration, and naming conventions are documented.

---

## § 5.10.003 — Core Modules

### Rule

Each core module must have a clear purpose, input/output, trigger, logic, and integration map.

### Meaning

Build the brain, heart, and lungs as modular systems. Each module should be alive on its own but connected to the full QiLife body.

### Mini Flow Per Submodule

- Purpose
- Input / output
- Trigger and flow
- Key logic/functions
- Integration map

### Modules

| Module | Function |
| --- | --- |
| QiFileFlow™ | File detection, OCR, rename, and move |
| QiNote™ | Note creation, structure, templates, tagging, and semantic map |
| QiLifeFeed™ | Daily activity logs, media summaries, and event contexting |
| QiCall™ | Twilio AI assistant for SMS/calls |
| QiMind™ | Vector DB, embeddings, semantic search, and memory retrieval |

---

## § 5.10.004 — UI & Interaction

### Rule

The interface should make the system easy to command, review, and trust.

### Meaning

QiLife needs a usable front door. The interface should support visual review, module control, prompts, alerts, and multiple input modes.

### UI Areas

- Streamlit current UI
- Splash screen / dashboard / module toggles
- Local vs web vs mobile access
- Notifications, prompts, alerts
- Voice, keyboard, visual triggers
- App icons, names, branding logic: Quin, Qi, etc.

---

## § 5.10.005 — Workflows & Automation

### Rule

QiLife should convert recurring routines into reliable automated workflows.

### Meaning

The rituals, rhythms, and habits should be baked into code where automation reduces friction without hiding accountability.

### Workflow Candidates

- Daily Digest creation via QiLifeFeed
- Screenshot to Notion pipeline
- File deduplication and cleanup
- Google Drive + Notion roundtrip
- Task/project linking
- Memory triggers, such as: “Find that doc from yesterday about…”

### Minimum Standard

Each workflow needs a trigger, input, output, error path, and review point.

---

## § 5.10.006 — Expansion & Collaboration

### Rule

QiLife should be designed for future users, clients, devices, and modules without losing system integrity.

### Meaning

Let others live in the genius without giving them the keys to every private room.

### Expansion Areas

- User management, permissions, and share logic
- Templates for other users or clients
- Deployment scripts for install/setup on a new device
- Mobile version and PWA logic
- Scaffolding for future modules: QiLedger, QiClient, QiBuilder

---

## § 5.10.007 — DNA & Documentation

### Rule

Every module needs documentation, recovery logic, and security expectations.

### Meaning

Record everything so nothing breaks silently. Documentation protects continuity, collaboration, and future rebuilds.

### Required Documentation

- Backup and recovery strategy
- Comments in code
- Final blueprint export: PDF + interactive map
- Internal wiki for every module
- Security audits: keys, PII handling, encryption plan
- SOPs in Notion

---

## Related References

- QiEOS Protocol
- QiFileFlow™
- QiNote™
- QiLifeFeed™
- QiCall™
- QiMind™
- Notion API
- Google Drive API
- Twilio
- Streamlit

## Open Questions

- What is the first shippable MVP?
- Which module should be built first: QiFileFlow™, QiNote™, or QiLifeFeed™?
- What needs to stay local-only for privacy?
- What belongs in Notion versus GitHub versus Drive?

## Notes

Keep QiLife modular. If a feature cannot explain its purpose, input, output, trigger, and review point, it is not ready to build.

---

## QiLife Purpose & Operating Doctrine

# QiLife Purpose & Operating Doctrine

Notes: Merged QiLife purpose, lean spine doctrine, and final operating rule from the former combined data model document.
QiCode: § 01.01.006
Sort Key: 01.01.006
Status: active
Tags: Core, Registry/Archive
Type: Rule
Version: Reconciled V1

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

## Purpose

QiLife is the private life operating app inside **QiApps**.

It exists to capture, organize, relate, retrieve, and act on Cody’s real-life information.

QiLife is not:

- the docs site
- the file drive
- the server
- a full finance system
- a CRM

QiLife is the structured life operating layer.

It answers:

> What came in, what does it mean, who or what is connected, what needs action, and where does it belong?
> 

## Doctrine Rules

- IDs use **ULIDs** for user-created records.
- Static lookup tables may use stable text keys.
- Raw capture is preserved.
- AI output is stored separately from approved truth.
- Timeline is a projection, not a separate core table.
- Files live in QiDrive; QiLife stores metadata and links.
- Notes and reflections are QiBit types, not separate tables.
- Finance-specific records are deferred unless needed.
- Properties, tags, metadata, and links should be used before creating more tables.

## Final Operating Rule

QiLife should make Cody’s life easier to operate.

If a table, field, module, or feature does not help Cody capture, clarify, connect, act, retrieve, review, or preserve truth, it does not belong in V1.

Keep the spine lean.

Use properties before tables.

Use links before duplication.

Use threads before fake modules.

Use QiDrive for files.

Use QiSpark for docs.

Use QiLife for living operations.

Use QiFinance later when the finance system earns its own module.

---

## QiLife Core V1 Data Model

# QiLife Core V1 Data Model

Notes: Merged database portability doctrine, true V1 tables, and core object map.
QiCode: § 03.05.007
Sort Key: 03.05.007
Status: active
Tags: Core, Hubs, Registry/Archive
Type: Standard
Version: Reconciled V1

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

## Database Doctrine

QiLife’s model should remain database-portable.

It may begin locally with SQLite for speed, but the schema should be able to move to Postgres / Supabase without conceptual rewrite.

## Core V1 Tables

These are the true QiLife V1 core tables:

```
qibits
buckets
threads
actions
action_steps
people
events
documents
knowledge_items
links
activity_log
ai_outputs
daily_summaries
```

## Core Object Map

| Table | Job |
| --- | --- |
| `qibits` | Atomic captured life input |
| `buckets` | Top-level life/file domains aligned to QiDrive |
| `threads` | Ongoing situations, cases, projects, storylines |
| `actions` | Tasks and work orders |
| `action_steps` | Subtasks inside actions |
| `people` | People, vendors, agencies, organizations |
| `events` | Calendar/scheduled or historical events |
| `documents` | Metadata for files stored in QiDrive |
| `knowledge_items` | Durable reference notes, templates, guides |
| `links` | Polymorphic relationship map |
| `activity_log` | Append-only operational history |
| `ai_outputs` | AI suggestions awaiting approval |
| `daily_summaries` | Synthesized day-level reviews |

## Core V1 Rule

QiLife starts with capture, buckets, threads, actions, people, documents, links, and review.

Do not start with finance.

Do not start with advanced AI.

Do not start with perfect UI.

---

## QiLife Data Model Spine

# QiLife Data Model Spine

Notes: Superseded after being broken down and merged into the appropriate existing QiCode chapters: Doctrine, Architecture, Chronicle & Records, and Operations.
QiCode: § 03.05.006
Sort Key: 03.05.006
Status: superseded
Tags: Core, Hubs, Registry/Archive
Type: Standard
Version: Reconciled V1

**System:** QiOS  

**Parent App:** QiLife  

**App Home:** `QiApps/QiLife`  

**Docs Home:** `QiSpark/docs`  

**File Backbone:** QiDrive  

**Status:** Active Doctrine  

**Version:** Reconciled V1

## 01. Purpose

This document defines the core data model for **QiLife**, the private life operating app inside **QiApps**.

QiLife exists to capture, organize, relate, retrieve, and act on Cody’s real-life information.

QiLife is not:

- the docs site
- the file drive
- the server
- a full finance system
- a CRM

QiLife is the structured life operating layer.

It answers:

> What came in, what does it mean, who or what is connected, what needs action, and where does it belong?
> 

## 02. Position in QiOS

```
QiOS
├── QiSpark
│   └── homepage, docs, doctrine, maps, guides, bookmarks
│
├── QiApps
│   └── QiLife, MomCare, utilities, dashboards, experiments
│
├── QiDrive
│   └── files, evidence, documents, assets, exports, archives
│
├── QiServer
│   └── runtime, cockpit, docker, databases, services, local AI
│
├── QiConnect
│   └── Google, GitHub, Supabase, imports, exports, sync jobs
│
└── QiArchive
    └── old systems, deprecated builds, frozen exports
```

QiLife lives in **QiApps**. QiSpark documents it. QiDrive stores related files. QiServer may run it. QiConnect may sync into it. QiArchive preserves inactive versions.

## 03. Database Doctrine

QiLife’s model should remain database-portable.

It may begin locally with SQLite for speed, but the schema should be able to move to Postgres / Supabase without conceptual rewrite.

### Canonical Rules

- IDs use **ULIDs** for user-created records.
- Static lookup tables may use stable text keys.
- Raw capture is preserved.
- AI output is stored separately from approved truth.
- Timeline is a projection, not a separate core table.
- Files live in QiDrive; QiLife stores metadata and links.
- Notes and reflections are QiBit types, not separate tables.
- Finance-specific records are deferred unless needed.
- Properties, tags, metadata, and links should be used before creating more tables.

## 04. Core V1 Tables

These are the true QiLife V1 core tables:

```
qibits
buckets
threads
actions
action_steps
people
events
documents
knowledge_items
links
activity_log
ai_outputs
daily_summaries
```

### Deferred / Not Core V1

```
transactions
obligations
```

These are not deleted from the concept. They are demoted.

They belong to a later **QiFinance** module or bridge.

QiLife may still capture financial or obligation-related information as QiBits using:

- `transaction_seed`
- `obligation_seed`
- `receipt`
- `payment_note`
- `bill_note`
- `money_issue`

But the specialized finance tables should not be part of QiLife core V1.

## 05. Core Object Map

| Table | Job |
| --- | --- |
| `qibits` | Atomic captured life input |
| `buckets` | Top-level life/file domains aligned to QiDrive |
| `threads` | Ongoing situations, cases, projects, storylines |
| `actions` | Tasks and work orders |
| `action_steps` | Subtasks inside actions |
| `people` | People, vendors, agencies, organizations |
| `events` | Calendar/scheduled or historical events |
| `documents` | Metadata for files stored in QiDrive |
| `knowledge_items` | Durable reference notes, templates, guides |
| `links` | Polymorphic relationship map |
| `activity_log` | Append-only operational history |
| `ai_outputs` | AI suggestions awaiting approval |
| `daily_summaries` | Synthesized day-level reviews |

## 06. Timeline Projection

Timeline is not its own table.

Timeline is a view/feed built from timestamped records.

### Timeline Timestamp Rules

| Record Type | Timeline Timestamp Rule |
| --- | --- |
| QiBit | `COALESCE(happened_at, captured_at, created_at)` |
| Action | `completed_at` if present, else `scheduled_for`, else `created_at` |
| Event | `start_time` |
| Daily Summary | `date` |
| Activity Log | `occurred_at` |

Documents, people, and knowledge items may appear in context panes and search results without becoming first-class timeline rows.

## 07. `qibits`

The atomic captured life item.

A QiBit preserves raw input before interpretation.

```
qibits
├── id
├── title
├── raw_capture
├── summary
├── meaning
├── qibit_type
├── bucket_key
├── thread_id
├── status
├── priority
├── importance
├── emotional_load
├── action_required
├── suggested_action
├── future_slot
├── happened_at
├── captured_at
├── resolved_at
├── retrieval_summary
├── reflection
├── tags_json
├── metadata_json
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

### QiBit Types

```
note
message
call
problem
idea
decision
task_seed
event_seed
appointment
document_seed
receipt
transaction_seed
obligation_seed
knowledge
reflection
observation
journal
other
```

### Statuses

```
new
triaged
open
in_progress
waiting_on
scheduled
resolved
closed
reference
ignored
archived
```

### Sacred Rule

`raw_capture` is the original truth. Summaries and interpretations are editable. The raw capture is not overwritten.

## 08. `buckets`

Buckets are the top-level operating domains aligned to QiDrive.

Use stable keys matching the folder names.

```
buckets
├── key
├── name
├── slug
├── folder_path
├── sort_order
├── description
├── is_system
├── created_at
└── updated_at
```

### Seed Buckets

```
00_inbox
01_workbench
02_timeline
03_life
04_people
05_business
06_finance
07_legal
08_tech
09_assets
10_data
11_reference
12_archive
13_system
```

### Bucket Meanings

| Bucket | Meaning |
| --- | --- |
| `00_inbox` | Temporary unprocessed capture |
| `01_workbench` | Active projects, drafts, builds, work |
| `02_timeline` | Daily logs, chronology, events, summaries |
| `03_life` | Household, wellness, routines, personal operations |
| `04_people` | People, vendors, agencies, relationships |
| `05_business` | Ventures, brand, client-adjacent material |
| `06_finance` | Finance references, exports, planning, bridge data |
| `07_legal` | Legal matters, evidence, research, filings |
| `08_tech` | Systems, servers, apps, config, code notes |
| `09_assets` | Media, templates, reusable visual/design assets |
| `10_data` | Datasets, CSVs, schemas, logs, exports |
| `11_reference` | Guides, examples, laws, research, outside references |
| `12_archive` | Inactive or completed material |
| `13_system` | Manifests, indexes, rules, automation records |

## 09. `threads`

Threads are ongoing situations, cases, projects, or storylines.

```
threads
├── id
├── title
├── description
├── bucket_key
├── status
├── priority
├── next_action
├── due_date
├── started_at
├── closed_at
├── tags_json
├── metadata_json
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

### Statuses

```
open
active
waiting_on
resolved
closed
archived
```

### Thread Rule

Use threads before creating new modules.

A thread can represent:

- house issue
- care situation
- legal issue
- personal project
- technical build
- ongoing conflict
- document packet
- creative work
- unresolved problem

## 10. `actions`

Actions are tasks or work orders.

```
actions
├── id
├── title
├── description
├── source_qibit_id
├── bucket_key
├── thread_id
├── assigned_to_person_id
├── status
├── priority
├── energy
├── context
├── due_date
├── scheduled_for
├── completed_at
├── resolution_note
├── tags_json
├── metadata_json
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

### Statuses

```
open
in_progress
waiting_on
scheduled
completed
cancelled
archived
```

### Action Rule

If it requires doing something, it becomes an action.

If it is just context, it remains a QiBit, knowledge item, document, event, or thread note.

## 11. `action_steps`

Subtasks or ordered steps within an action.

```
action_steps
├── id
├── action_id
├── title
├── description
├── status
├── sort_order
├── completed_at
├── created_at
└── updated_at
```

Use steps only when an action needs breakdown.

Do not turn every tiny thing into a step by default.

## 12. `people`

People is a broad entity/contact model.

It is not CRM.

```
people
├── id
├── display_name
├── legal_name
├── type
├── relationship
├── role
├── email
├── phone
├── address
├── notes
├── tags_json
├── metadata_json
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

### People Types

```
person
family
friend
vendor
government
organization
agency
care_provider
legal_contact
financial_contact
service_provider
neighbor
unknown
```

### People Rule

Do not create separate tables for vendors, agencies, government contacts, care team, and organizations.

Use one table with `type`, `relationship`, `role`, tags, and metadata.

## 13. `events`

Events are scheduled or historical calendar-visible items.

```
events
├── id
├── title
├── description
├── start_time
├── end_time
├── location
├── bucket_key
├── thread_id
├── status
├── source_qibit_id
├── external_calendar_id
├── external_event_id
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

### Statuses

```
scheduled
completed
cancelled
missed
archived
```

### Event Rule

Events may sync with Google Calendar later through QiConnect.

QiLife should not assume Google Calendar is the only calendar source.

## 14. `documents`

Documents are metadata records for files stored in QiDrive.

QiLife does not store the file itself unless there is a specific technical reason.

```
documents
├── id
├── title
├── file_path
├── drive_url
├── source
├── document_type
├── bucket_key
├── thread_id
├── file_hash
├── mime_type
├── size_bytes
├── notes
├── extracted_text
├── summary
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

### Document Rule

QiDrive stores the file.

QiLife stores:

- what it is
- where it is
- what it relates to
- whether it matters
- how to retrieve it

## 15. `knowledge_items`

Durable reference material, templates, guides, and reusable notes.

```
knowledge_items
├── id
├── title
├── body_markdown
├── bucket_key
├── module_key
├── knowledge_type
├── source_type
├── source_path
├── confidence
├── visibility
├── tags_json
├── metadata_json
├── last_synced_at
├── sync_hash
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

### Knowledge Types

```
guide
template
checklist
reference
rule
note
summary
external_source
```

### Repo Docs Rule

Docs imported from QiSpark or app repos are read-only in QiLife unless edited at their source.

QiLife can index and reference docs, but it should not silently fork doctrine.

## 16. `links`

The polymorphic relationship table.

Links connect anything to anything.

```
links
├── id
├── source_type
├── source_id
├── target_type
├── target_id
├── relationship
├── created_at
└── updated_at
```

### Common Relationships

```
relates_to
belongs_to
caused_by
evidence_for
follow_up_to
blocks
blocked_by
mentions
supports
contradicts
duplicates
derived_from
stored_at
assigned_to
```

### Link Rule

Use links before duplicating data.

## 17. `activity_log`

Append-only operational history.

```
activity_log
├── id
├── occurred_at
├── actor
├── action
├── entity_type
├── entity_id
├── summary
├── before_json
├── after_json
├── source
└── created_at
```

### Activity Log Rule

The activity log records what changed.

It should not replace notes, summaries, or timeline projections.

## 18. `ai_outputs`

AI recommendations and generated results.

```
ai_outputs
├── id
├── source_type
├── source_id
├── ai_task
├── prompt_snapshot
├── output_json
├── confidence
├── accepted
├── rejected
├── reviewed_at
├── reviewed_by
├── created_records_json
├── created_at
└── updated_at
```

### AI Rule

AI may suggest.

AI may not silently approve itself.

Approved AI output should create or update canonical records through a reviewed action.

## 19. `daily_summaries`

Synthesized day-level summaries.

```
daily_summaries
├── id
├── date
├── summary_markdown
├── ai_summary_json
├── reviewed
├── reviewed_at
├── created_at
└── updated_at
```

### Daily Summary Rule

Daily summaries are retrieval and reflection helpers.

They do not replace raw QiBits, activity logs, or source records.

## 20. Deferred: `transactions`

Transactions are not QiLife core V1.

They belong to a later QiFinance module or bridge.

QiLife may capture transaction-related seeds as QiBits.

### Deferred Table Sketch

```
transactions
├── id
├── date
├── amount_cents
├── currency
├── direction
├── from_label
├── to_label
├── category
├── bucket_key
├── thread_id
├── status
├── notes
├── evidence_document_id
├── source_qibit_id
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

### Rule

Do not build this into QiLife core until there is a clear reason.

For now, use finance app exports, documents, QiBits, and links.

## 21. Deferred: `obligations`

Obligations are not QiLife core V1.

They belong to a later QiFinance / legal / agreements module if needed.

QiLife may capture obligation-related seeds as QiBits or actions.

### Deferred Table Sketch

```
obligations
├── id
├── owed_by_label
├── owed_to_label
├── obligation_type
├── amount_cents
├── currency
├── reason
├── status
├── due_date
├── related_transaction_id
├── source_qibit_id
├── created_at
├── updated_at
├── resolved_at
├── archived_at
└── deleted_at
```

### Statuses

```
open
partial
waiting_on
resolved
disputed
archived
```

### Rule

If it is just “someone owes something,” capture it as a QiBit or Action first.

Create a full obligations table only when tracking becomes too frequent or too important to handle through QiBits, actions, threads, and links.

## 22. Activity Log vs Daily Summaries vs Reflections

| Object | Meaning |
| --- | --- |
| `activity_log` | Append-only record of changes |
| `daily_summaries` | Synthesized day-level reviews |
| `qibits.reflection` | User-authored or AI-assisted reflection tied to a captured item |

Do not merge these.

They serve different jobs.

## 23. Human-in-the-Loop Doctrine

QiLife must preserve the difference between:

- raw input
- AI interpretation
- user-approved records
- derived summaries
- system logs

### Approval Flow

```
Raw QiBit
  -> AI suggestion
  -> Review queue
  -> Cody approves / edits / rejects
  -> Canonical record update
  -> Activity log entry
```

### Rule

No silent canonical changes from AI.

## 24. Build Order

Build QiLife in this order:

```
1. qibits
2. buckets
3. threads
4. actions
5. action_steps
6. people
7. events
8. documents
9. links
10. activity_log
11. ai_outputs
12. daily_summaries
```

Then later:

```
13. QiFinance bridge
14. transactions
15. obligations
16. richer reports
17. advanced automation
```

Do not start with finance.

Do not start with advanced AI.

Do not start with perfect UI.

Start with capture, buckets, threads, actions, people, documents, links, and review.

## 25. Final Operating Rule

QiLife should make Cody’s life easier to operate.

If a table, field, module, or feature does not help Cody capture, clarify, connect, act, retrieve, review, or preserve truth, it does not belong in V1.

Keep the spine lean.

Use properties before tables.

Use links before duplication.

Use threads before fake modules.

Use QiDrive for files.

Use QiSpark for docs.

Use QiLife for living operations.

Use QiFinance later when the finance system earns its own module.

## Placement Notes

This doctrine belongs primarily under **Title 03 — System Architecture**, because it defines the QiLife app’s data-model spine and its place inside QiOS.

It also cross-references:

- **Title 01 — Doctrine & Principles** for human-first, truth-preserving, lean-system rules.
- **Title 04 — Chronicle & Records** for timeline, QiBits, documents, activity logs, and daily summaries.
- **Title 05 — Operations & Workflows** for actions, action steps, build order, and review flow.

---

## QiLife App Placement

# QiLife App Placement

Notes: Merged QiLife placement in QiOS, app home, docs home, and system boundary roles.
QiCode: § 03.05.006
Sort Key: 03.05.006
Status: active
Tags: Core, Hubs, Registry/Archive
Type: Standard
Version: Reconciled V1

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

## Position in QiOS

```
QiOS
├── QiSpark
│   └── homepage, docs, doctrine, maps, guides, bookmarks
│
├── QiApps
│   └── QiLife, MomCare, utilities, dashboards, experiments
│
├── QiDrive
│   └── files, evidence, documents, assets, exports, archives
│
├── QiServer
│   └── runtime, cockpit, docker, databases, services, local AI
│
├── QiConnect
│   └── Google, GitHub, Supabase, imports, exports, sync jobs
│
└── QiArchive
    └── old systems, deprecated builds, frozen exports
```

QiLife lives in **QiApps**.

QiSpark documents it.

QiDrive stores related files.

QiServer may run it.

QiConnect may sync into it.

QiArchive preserves inactive versions.

## App Placement

- **App Home:** `QiApps/QiLife`
- **Docs Home:** `QiSpark/docs`
- **File Backbone:** QiDrive

## Architecture Rule

QiLife is the app-layer operating system for living records. It should stay inside **QiApps**, while doctrine and published documentation live in **QiSpark**, files live in **QiDrive**, runtime services live in **QiServer**, sync pathways live in **QiConnect**, and inactive versions live in **QiArchive**.

---

## QiLife Buckets, Documents, Knowledge & Links

# QiLife Buckets, Documents, Knowledge & Links

Notes: Merged bucket model, document metadata model, knowledge item model, and polymorphic links doctrine.
QiCode: § 04.02.006
Sort Key: 04.02.006
Status: active
Tags: Core, KB/SOPs, Registry/Archive
Type: Standard
Version: Reconciled V1

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

## Records, Metadata, and Links

QiLife records should clarify what something is, where it belongs, and what it relates to before creating new structures.

## Buckets

Buckets are the top-level operating domains aligned to QiDrive.

Use stable keys matching the folder names.

```
buckets
├── key
├── name
├── slug
├── folder_path
├── sort_order
├── description
├── is_system
├── created_at
└── updated_at
```

## Seed Buckets

```
00_inbox
01_workbench
02_timeline
03_life
04_people
05_business
06_finance
07_legal
08_tech
09_assets
10_data
11_reference
12_archive
13_system
```

## Bucket Meanings

| Bucket | Meaning |
| --- | --- |
| `00_inbox` | Temporary unprocessed capture |
| `01_workbench` | Active projects, drafts, builds, work |
| `02_timeline` | Daily logs, chronology, events, summaries |
| `03_life` | Household, wellness, routines, personal operations |
| `04_people` | People, vendors, agencies, relationships |
| `05_business` | Ventures, brand, client-adjacent material |
| `06_finance` | Finance references, exports, planning, bridge data |
| `07_legal` | Legal matters, evidence, research, filings |
| `08_tech` | Systems, servers, apps, config, code notes |
| `09_assets` | Media, templates, reusable visual/design assets |
| `10_data` | Datasets, CSVs, schemas, logs, exports |
| `11_reference` | Guides, examples, laws, research, outside references |
| `12_archive` | Inactive or completed material |
| `13_system` | Manifests, indexes, rules, automation records |

## Documents

Documents are metadata records for files stored in QiDrive.

QiLife does not store the file itself unless there is a specific technical reason.

```
documents
├── id
├── title
├── file_path
├── drive_url
├── source
├── document_type
├── bucket_key
├── thread_id
├── file_hash
├── mime_type
├── size_bytes
├── notes
├── extracted_text
├── summary
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

## Document Rule

QiDrive stores the file.

QiLife stores:

- what it is
- where it is
- what it relates to
- whether it matters
- how to retrieve it

## Knowledge Items

Durable reference material, templates, guides, and reusable notes.

```
knowledge_items
├── id
├── title
├── body_markdown
├── bucket_key
├── module_key
├── knowledge_type
├── source_type
├── source_path
├── confidence
├── visibility
├── tags_json
├── metadata_json
├── last_synced_at
├── sync_hash
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

## Knowledge Types

```
guide
template
checklist
reference
rule
note
summary
external_source
```

## Repo Docs Rule

Docs imported from QiSpark or app repos are read-only in QiLife unless edited at their source.

QiLife can index and reference docs, but it should not silently fork doctrine.

## Links

The polymorphic relationship table.

Links connect anything to anything.

```
links
├── id
├── source_type
├── source_id
├── target_type
├── target_id
├── relationship
├── created_at
└── updated_at
```

## Common Relationships

```
relates_to
belongs_to
caused_by
evidence_for
follow_up_to
blocks
blocked_by
mentions
supports
contradicts
duplicates
derived_from
stored_at
assigned_to
```

## Link Rule

Use links before duplicating data.

---

## QiLife Threads, Actions & Build Order

# QiLife Threads, Actions & Build Order

Notes: Merged threads, actions, action steps, and QiLife build order.
QiCode: § 05.01.006
Sort Key: 05.01.006
Status: active
Tags: Core, Hubs
Type: Workflow
Version: Reconciled V1

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

## Threads

Threads are ongoing situations, cases, projects, or storylines.

```
threads
├── id
├── title
├── description
├── bucket_key
├── status
├── priority
├── next_action
├── due_date
├── started_at
├── closed_at
├── tags_json
├── metadata_json
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

## Thread Statuses

```
open
active
waiting_on
resolved
closed
archived
```

## Thread Rule

Use threads before creating new modules.

A thread can represent:

- house issue
- care situation
- legal issue
- personal project
- technical build
- ongoing conflict
- document packet
- creative work
- unresolved problem

## Actions

Actions are tasks or work orders.

```
actions
├── id
├── title
├── description
├── source_qibit_id
├── bucket_key
├── thread_id
├── assigned_to_person_id
├── status
├── priority
├── energy
├── context
├── due_date
├── scheduled_for
├── completed_at
├── resolution_note
├── tags_json
├── metadata_json
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

## Action Statuses

```
open
in_progress
waiting_on
scheduled
completed
cancelled
archived
```

## Action Rule

If it requires doing something, it becomes an action.

If it is just context, it remains a QiBit, knowledge item, document, event, or thread note.

## Action Steps

Subtasks or ordered steps within an action.

```
action_steps
├── id
├── action_id
├── title
├── description
├── status
├── sort_order
├── completed_at
├── created_at
└── updated_at
```

Use steps only when an action needs breakdown.

Do not turn every tiny thing into a step by default.

## Build Order

Build QiLife in this order:

```
1. qibits
2. buckets
3. threads
4. actions
5. action_steps
6. people
7. events
8. documents
9. links
10. activity_log
11. ai_outputs
12. daily_summaries
```

Then later:

```
13. QiFinance bridge
14. transactions
15. obligations
16. richer reports
17. advanced automation
```

---

## QiLife People & Events

# QiLife People & Events

Notes: Merged people/contact model and events/calendar-visible model.
QiCode: § 04.02.007
Sort Key: 04.02.007
Status: active
Tags: Core, Hubs
Type: Record Type
Version: Reconciled V1

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

## People

People is a broad entity/contact model.

It is not CRM.

```
people
├── id
├── display_name
├── legal_name
├── type
├── relationship
├── role
├── email
├── phone
├── address
├── notes
├── tags_json
├── metadata_json
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

## People Types

```
person
family
friend
vendor
government
organization
agency
care_provider
legal_contact
financial_contact
service_provider
neighbor
unknown
```

## People Rule

Do not create separate tables for vendors, agencies, government contacts, care team, and organizations.

Use one table with `type`, `relationship`, `role`, tags, and metadata.

## Events

Events are scheduled or historical calendar-visible items.

```
events
├── id
├── title
├── description
├── start_time
├── end_time
├── location
├── bucket_key
├── thread_id
├── status
├── source_qibit_id
├── external_calendar_id
├── external_event_id
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

## Event Statuses

```
scheduled
completed
cancelled
missed
archived
```

## Event Rule

Events may sync with Google Calendar later through QiConnect.

QiLife should not assume Google Calendar is the only calendar source.

---

## QiLife Activity Log & Daily Summaries

# QiLife Activity Log & Daily Summaries

Notes: Merged activity log, daily summaries, and reflection separation rules.
QiCode: § 04.03.006
Sort Key: 04.03.006
Status: active
Tags: Core, Registry/Archive
Type: Standard
Version: Reconciled V1

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

## Audit Trail

The activity log is append-only operational history.

```
activity_log
├── id
├── occurred_at
├── actor
├── action
├── entity_type
├── entity_id
├── summary
├── before_json
├── after_json
├── source
└── created_at
```

## Activity Log Rule

The activity log records what changed.

It should not replace notes, summaries, or timeline projections.

## Daily Summaries

Synthesized day-level summaries.

```
daily_summaries
├── id
├── date
├── summary_markdown
├── ai_summary_json
├── reviewed
├── reviewed_at
├── created_at
└── updated_at
```

## Daily Summary Rule

Daily summaries are retrieval and reflection helpers.

They do not replace raw QiBits, activity logs, or source records.

## Activity Log vs Daily Summaries vs Reflections

| Object | Meaning |
| --- | --- |
| `activity_log` | Append-only record of changes |
| `daily_summaries` | Synthesized day-level reviews |
| `qibits.reflection` | User-authored or AI-assisted reflection tied to a captured item |

Do not merge these.

They serve different jobs.

---

## QiLife AI Outputs & Review Queue

# QiLife AI Outputs & Review Queue

Notes: Merged AI output schema, human-in-the-loop doctrine, approval flow, and no-silent-canonical-change rule.
QiCode: § 05.01.007
Sort Key: 05.01.007
Status: active
Tags: Core, Registry/Archive
Type: Workflow
Version: Reconciled V1

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

## AI Outputs

AI recommendations and generated results.

```
ai_outputs
├── id
├── source_type
├── source_id
├── ai_task
├── prompt_snapshot
├── output_json
├── confidence
├── accepted
├── rejected
├── reviewed_at
├── reviewed_by
├── created_records_json
├── created_at
└── updated_at
```

## AI Rule

AI may suggest.

AI may not silently approve itself.

Approved AI output should create or update canonical records through a reviewed action.

## Human-in-the-Loop Doctrine

QiLife must preserve the difference between:

- raw input
- AI interpretation
- user-approved records
- derived summaries
- system logs

## Approval Flow

```
Raw QiBit
  -> AI suggestion
  -> Review queue
  -> Cody approves / edits / rejects
  -> Canonical record update
  -> Activity log entry
```

## Rule

No silent canonical changes from AI.

---

## QiLife QiBits & Timeline Projection

# QiLife QiBits & Timeline Projection

Notes: Merged timeline projection rules, QiBit schema, QiBit types, statuses, and raw capture rule.
QiCode: § 04.01.010
Sort Key: 04.01.010
Status: active
Tags: Core, Hubs
Type: Record Type
Version: Reconciled V1

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

## Timeline Projection

Timeline is not its own table.

Timeline is a view/feed built from timestamped records.

## Timeline Timestamp Rules

| Record Type | Timeline Timestamp Rule |
| --- | --- |
| QiBit | `COALESCE(happened_at, captured_at, created_at)` |
| Action | `completed_at` if present, else `scheduled_for`, else `created_at` |
| Event | `start_time` |
| Daily Summary | `date` |
| Activity Log | `occurred_at` |

Documents, people, and knowledge items may appear in context panes and search results without becoming first-class timeline rows.

## QiBits

The atomic captured life item.

A QiBit preserves raw input before interpretation.

```
qibits
├── id
├── title
├── raw_capture
├── summary
├── meaning
├── qibit_type
├── bucket_key
├── thread_id
├── status
├── priority
├── importance
├── emotional_load
├── action_required
├── suggested_action
├── future_slot
├── happened_at
├── captured_at
├── resolved_at
├── retrieval_summary
├── reflection
├── tags_json
├── metadata_json
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

### QiBit Types

```
note
message
call
problem
idea
decision
task_seed
event_seed
appointment
document_seed
receipt
transaction_seed
obligation_seed
knowledge
reflection
observation
journal
other
```

### QiBit Statuses

```
new
triaged
open
in_progress
waiting_on
scheduled
resolved
closed
reference
ignored
archived
```

## Sacred Rule

`raw_capture` is the original truth. Summaries and interpretations are editable. The raw capture is not overwritten.

---

## QiLife Deferred Finance Bridge

# QiLife Deferred Finance Bridge

Notes: Merged deferred transactions and obligations doctrine for future QiFinance bridge.
QiCode: § 05.02.006
Sort Key: 05.02.006
Status: active
Tags: Core, Registry/Archive
Type: Reference
Version: Reconciled V1

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Deferred  

**Version:** Reconciled V1

## Deferred / Not Core V1

```
transactions
obligations
```

These are not deleted from the concept. They are demoted.

They belong to a later **QiFinance** module or bridge.

QiLife may still capture financial or obligation-related information as QiBits using:

- `transaction_seed`
- `obligation_seed`
- `receipt`
- `payment_note`
- `bill_note`
- `money_issue`

But the specialized finance tables should not be part of QiLife core V1.

## Deferred: `transactions`

Transactions are not QiLife core V1.

They belong to a later QiFinance module or bridge.

QiLife may capture transaction-related seeds as QiBits.

### Deferred Table Sketch

```
transactions
├── id
├── date
├── amount_cents
├── currency
├── direction
├── from_label
├── to_label
├── category
├── bucket_key
├── thread_id
├── status
├── notes
├── evidence_document_id
├── source_qibit_id
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

### Rule

Do not build this into QiLife core until there is a clear reason.

For now, use finance app exports, documents, QiBits, and links.

## Deferred: `obligations`

Obligations are not QiLife core V1.

They belong to a later QiFinance / legal / agreements module if needed.

QiLife may capture obligation-related seeds as QiBits or actions.

### Deferred Table Sketch

```
obligations
├── id
├── owed_by_label
├── owed_to_label
├── obligation_type
├── amount_cents
├── currency
├── reason
├── status
├── due_date
├── related_transaction_id
├── source_qibit_id
├── created_at
├── updated_at
├── resolved_at
├── archived_at
└── deleted_at
```

### Statuses

```
open
partial
waiting_on
resolved
disputed
archived
```

### Rule

If it is just “someone owes something,” capture it as a QiBit or Action first.

Create a full obligations table only when tracking becomes too frequent or too important to handle through QiBits, actions, threads, and links.

---

## QiLifeFeed™ (daily activity logs, media summaries,

# QiLifeFeed™ (daily activity logs, media summaries, event contexting)

---

---

## QiLife Doctrine

---
title: "QiLife Doctrine"
aliases:
  - "QiLife Purpose and Doctrine"
system: "QiOS"
document_type: "doctrine"
status: "active-doctrine"
version: "1.0"
canonical: true
updated: "2026-07-18"
source:
  - "QiCode Documentation database"
  - "QiLife Data Model Spine"
tags:
  - "qicode"
  - "qios"
  - "qilife"
---
> **Parent:** [[00 - QiCode Home|QiCode Home]]
> **Related:** [[QiLife Architecture|Architecture]] · [[QiLife Data Model|Data Model]] · [[QiLife Workflows|Workflows]]

# QiLife Doctrine

> **Title:** 06 — QiLife  
> **Chapter:** 06.01 — Purpose, Boundaries & Scope

This document is the canonical statement of what QiLife is, what it is not, and what belongs in V1.

## § 06.01.001 — Purpose & Operating Doctrine

QiLife is the private life operating application inside **QiApps**.

It exists to capture, organize, relate, retrieve, review, and act on real-life information.

QiLife is not:

- the documentation site;
- the file drive;
- the server or runtime layer;
- a full finance system; or
- a CRM.

QiLife is the structured life-operating layer. It answers:

> What came in? What does it mean? Who or what is connected? What requires action? Where does it belong?

##### Doctrine Rules

- User-created records use **ULIDs**.
- Static lookup tables may use stable text keys.
- Raw capture is preserved.
- AI output is stored separately from approved truth.
- The timeline is a projection, not a separate core table.
- Files live in QiDrive; QiLife stores metadata and links.
- Notes and reflections are QiBit types, not separate tables.
- Finance-specific records remain outside QiLife core unless the need is proven.
- Properties, tags, metadata, and links should be used before creating more tables.

##### Final Operating Rule

QiLife should make life easier to operate.

A table, field, module, or feature does not belong in V1 unless it helps capture, clarify, connect, act, retrieve, review, or preserve truth.

Keep the spine lean:

- Use properties before tables.
- Use links before duplication.
- Use threads before fake modules.
- Use QiDrive for files.
- Use QiSpark for documentation.
- Use QiLife for living operations.
- Use QiFinance when finance earns its own specialized module.

## § 06.01.002 — Core V1 Scope

QiLife V1 starts with capture, buckets, threads, actions, people, events, documents, links, and review.

Do not start with:

- finance;
- advanced AI; or
- perfect UI.

---

## QiLife Architecture

---
title: "QiLife Architecture"
aliases:
  - "QiLife Placement and Architecture"
system: "QiOS"
document_type: "architecture"
status: "active-doctrine"
version: "1.0"
canonical: true
updated: "2026-07-18"
source:
  - "QiCode Documentation database"
  - "QiLife Data Model Spine"
tags:
  - "qicode"
  - "qios"
  - "qilife"
---
> **Parent:** [[00 - QiCode Home|QiCode Home]]
> **Related:** [[QiLife Doctrine|Doctrine]] · [[QiLife Data Model|Data Model]] · [[QiLife Workflows|Workflows]]

# QiLife Architecture

> **Title:** 06 — QiLife  
> **Chapter:** 06.02 — Architecture & Placement

This document defines QiLife’s position within QiOS, its canonical homes, and its database portability boundary.

## § 06.02.001 — Position in QiOS

```text
QiOS
├── QiSpark
│   └── homepage, docs, doctrine, maps, guides, bookmarks
├── QiApps
│   └── QiLife, MomCare, utilities, dashboards, experiments
├── QiDrive
│   └── files, evidence, documents, assets, exports, archives
├── QiServer
│   └── runtime, cockpit, containers, databases, services, local AI
├── QiConnect
│   └── Google, GitHub, Supabase, imports, exports, sync jobs
└── QiArchive
    └── old systems, deprecated builds, frozen exports
```

QiLife lives in **QiApps**.

- QiSpark documents it.
- QiDrive stores its related files.
- QiServer may run it.
- QiConnect may synchronize data into or out of it.
- QiArchive preserves inactive versions.

## § 06.02.002 — Canonical Placement

- **Application home:** `QiApps/QiLife`
- **Documentation home:** `QiSpark/docs`
- **File backbone:** `QiDrive`

QiLife remains in the application layer. Doctrine and published documentation belong in QiSpark; files belong in QiDrive; runtime services belong in QiServer; synchronization pathways belong in QiConnect; inactive versions belong in QiArchive.

## § 06.02.003 — Database Portability

QiLife’s data model must remain database-portable.

It may begin locally with SQLite for speed, but the schema must be able to move to PostgreSQL or Supabase without conceptual redesign.

---

## QiLife Data Model

---
title: "QiLife Data Model"
aliases:
  - "QiLife Core V1 Data Model"
system: "QiOS"
document_type: "data-model"
status: "active-doctrine"
version: "1.0"
canonical: true
updated: "2026-07-18"
source:
  - "QiCode Documentation database"
  - "QiLife Data Model Spine"
tags:
  - "qicode"
  - "qios"
  - "qilife"
---
> **Parent:** [[00 - QiCode Home|QiCode Home]]
> **Related:** [[QiLife Doctrine|Doctrine]] · [[QiLife Architecture|Architecture]] · [[QiLife Workflows|Workflows]]

# QiLife Data Model

> **Title:** 06 — QiLife  
> **Chapter:** 06.03 — Core V1 Data Model

This document is the canonical schema-level model for QiLife V1. It defines responsibilities and boundaries, not vendor-specific SQL.

## § 06.03.001 — Core Tables

The canonical V1 tables are:

```text
qibits
buckets
threads
actions
action_steps
people
events
documents
knowledge_items
links
activity_log
ai_outputs
daily_summaries
```

| Table | Responsibility |
| --- | --- |
| `qibits` | Atomic captured life input |
| `buckets` | Top-level operating domains aligned to QiDrive |
| `threads` | Ongoing situations, cases, projects, or storylines |
| `actions` | Tasks and work orders |
| `action_steps` | Ordered subtasks within actions |
| `people` | People, vendors, agencies, and organizations |
| `events` | Scheduled or historical calendar-visible events |
| `documents` | Metadata for files stored in QiDrive |
| `knowledge_items` | Durable references, templates, guides, and notes |
| `links` | Polymorphic relationship map |
| `activity_log` | Append-only operational history |
| `ai_outputs` | AI suggestions awaiting review |
| `daily_summaries` | Synthesized day-level reviews |

## § 06.03.002 — QiBits

A QiBit is the atomic captured life item. It preserves the raw input before interpretation.

```text
qibits
├── id
├── title
├── raw_capture
├── summary
├── meaning
├── qibit_type
├── bucket_key
├── thread_id
├── status
├── priority
├── importance
├── emotional_load
├── action_required
├── suggested_action
├── future_slot
├── happened_at
├── captured_at
├── resolved_at
├── retrieval_summary
├── reflection
├── tags_json
├── metadata_json
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

##### QiBit Types

```text
note
message
call
problem
idea
decision
task_seed
event_seed
appointment
document_seed
receipt
transaction_seed
obligation_seed
knowledge
reflection
observation
journal
other
```

##### QiBit Statuses

```text
new
triaged
open
in_progress
waiting_on
scheduled
resolved
closed
reference
ignored
archived
```

##### Sacred Rule

`raw_capture` is the original truth. Summaries and interpretations are editable; the raw capture is not overwritten.

## § 06.03.003 — Buckets

Buckets are top-level operating domains aligned to QiDrive. Use stable keys matching the folder names.

```text
buckets
├── key
├── name
├── slug
├── folder_path
├── sort_order
├── description
├── is_system
├── created_at
└── updated_at
```

##### Seed Buckets

```text
00_inbox
01_workbench
02_timeline
03_life
04_people
05_business
06_finance
07_legal
08_tech
09_assets
10_data
11_reference
12_archive
13_system
```

| Bucket | Meaning |
| --- | --- |
| `00_inbox` | Temporary, unprocessed capture |
| `01_workbench` | Active projects, drafts, builds, and work |
| `02_timeline` | Daily logs, chronology, events, and summaries |
| `03_life` | Household, wellness, routines, and personal operations |
| `04_people` | People, vendors, agencies, and relationships |
| `05_business` | Ventures, brands, and client-adjacent material |
| `06_finance` | Finance references, exports, planning, and bridge data |
| `07_legal` | Legal matters, evidence, research, and filings |
| `08_tech` | Systems, servers, applications, configuration, and code notes |
| `09_assets` | Media, templates, and reusable visual or design assets |
| `10_data` | Datasets, CSVs, schemas, logs, and exports |
| `11_reference` | Guides, examples, laws, research, and outside references |
| `12_archive` | Inactive or completed material |
| `13_system` | Manifests, indexes, rules, and automation records |

## § 06.03.004 — Threads

Threads represent ongoing situations, cases, projects, or storylines.

```text
threads
├── id
├── title
├── description
├── bucket_key
├── status
├── priority
├── next_action
├── due_date
├── started_at
├── closed_at
├── tags_json
├── metadata_json
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

##### Thread Statuses

```text
open
active
waiting_on
resolved
closed
archived
```

##### Thread Rule

Use threads before creating new modules.

A thread may represent a:

- housing issue;
- care situation;
- legal matter;
- personal project;
- technical build;
- ongoing conflict;
- document packet;
- creative work; or
- unresolved problem.

## § 06.03.005 — Actions & Action Steps

Actions are tasks or work orders.

```text
actions
├── id
├── title
├── description
├── source_qibit_id
├── bucket_key
├── thread_id
├── assigned_to_person_id
├── status
├── priority
├── energy
├── context
├── due_date
├── scheduled_for
├── completed_at
├── resolution_note
├── tags_json
├── metadata_json
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

##### Action Statuses

```text
open
in_progress
waiting_on
scheduled
completed
cancelled
archived
```

If something requires doing, it becomes an action. If it is only context, it remains a QiBit, knowledge item, document, event, or thread note.

Action steps are ordered subtasks within an action.

```text
action_steps
├── id
├── action_id
├── title
├── description
├── status
├── sort_order
├── completed_at
├── created_at
└── updated_at
```

Use steps only when an action genuinely needs decomposition. Do not turn every small task into a step by default.

## § 06.03.006 — People

`people` is a broad entity and contact model. It is not a CRM.

```text
people
├── id
├── display_name
├── legal_name
├── type
├── relationship
├── role
├── email
├── phone
├── address
├── notes
├── tags_json
├── metadata_json
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

##### People Types

```text
person
family
friend
vendor
government
organization
agency
care_provider
legal_contact
financial_contact
service_provider
neighbor
unknown
```

Do not create separate tables for vendors, agencies, government contacts, care teams, and organizations. Use one table with `type`, `relationship`, `role`, tags, and metadata.

## § 06.03.007 — Events

Events are scheduled or historical calendar-visible items.

```text
events
├── id
├── title
├── description
├── start_time
├── end_time
├── location
├── bucket_key
├── thread_id
├── status
├── source_qibit_id
├── external_calendar_id
├── external_event_id
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

##### Event Statuses

```text
scheduled
completed
cancelled
missed
archived
```

Events may later synchronize with Google Calendar through QiConnect. QiLife must not assume Google Calendar is the only calendar source.

## § 06.03.008 — Documents

Documents are metadata records for files stored in QiDrive. QiLife does not store the file itself unless there is a specific technical reason.

```text
documents
├── id
├── title
├── file_path
├── drive_url
├── source
├── document_type
├── bucket_key
├── thread_id
├── file_hash
├── mime_type
├── size_bytes
├── notes
├── extracted_text
├── summary
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

QiDrive stores the file. QiLife stores:

- what it is;
- where it is;
- what it relates to;
- whether it matters; and
- how to retrieve it.

## § 06.03.009 — Knowledge Items

Knowledge items contain durable references, templates, guides, and reusable notes.

```text
knowledge_items
├── id
├── title
├── body_markdown
├── bucket_key
├── module_key
├── knowledge_type
├── source_type
├── source_path
├── confidence
├── visibility
├── tags_json
├── metadata_json
├── last_synced_at
├── sync_hash
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

##### Knowledge Types

```text
guide
template
checklist
reference
rule
note
summary
external_source
```

##### Repository Documentation Rule

Documentation imported from QiSpark or application repositories is read-only in QiLife unless edited at its source. QiLife may index and reference documentation, but it must not silently fork doctrine.

## § 06.03.010 — Links

Links form the polymorphic relationship map and may connect any supported record to any other supported record.

```text
links
├── id
├── source_type
├── source_id
├── target_type
├── target_id
├── relationship
├── created_at
└── updated_at
```

##### Common Relationships

```text
relates_to
belongs_to
caused_by
evidence_for
follow_up_to
blocks
blocked_by
mentions
supports
contradicts
duplicates
derived_from
stored_at
assigned_to
```

Use links before duplicating data.

## § 06.03.011 — Activity Log

The activity log is append-only operational history.

```text
activity_log
├── id
├── occurred_at
├── actor
├── action
├── entity_type
├── entity_id
├── summary
├── before_json
├── after_json
├── source
└── created_at
```

The activity log records what changed. It does not replace notes, summaries, or timeline projections.

## § 06.03.012 — AI Outputs

AI outputs contain recommendations and generated results awaiting review.

```text
ai_outputs
├── id
├── source_type
├── source_id
├── ai_task
├── prompt_snapshot
├── output_json
├── confidence
├── accepted
├── rejected
├── reviewed_at
├── reviewed_by
├── created_records_json
├── created_at
└── updated_at
```

AI may suggest. AI may not silently approve itself.

Approved AI output must create or update canonical records through a reviewed action.

## § 06.03.013 — Daily Summaries

Daily summaries are synthesized day-level reviews.

```text
daily_summaries
├── id
├── date
├── summary_markdown
├── ai_summary_json
├── reviewed
├── reviewed_at
├── created_at
└── updated_at
```

Daily summaries support retrieval and reflection. They do not replace raw QiBits, activity logs, or source records.

| Object | Responsibility |
| --- | --- |
| `activity_log` | Append-only record of changes |
| `daily_summaries` | Synthesized day-level reviews |
| `qibits.reflection` | User-authored or AI-assisted reflection tied to a captured item |

These objects must not be merged; they serve different purposes.

---

## QiLife Product Surfaces

---
title: "QiLife Product Surfaces"
aliases:
  - "QiLife UI Surfaces"
system: "QiOS"
document_type: "product-surface-registry"
status: "outline-only"
version: "1.0"
canonical: true
updated: "2026-07-18"
source:
  - "QiCode Documentation database"
  - "QiLife Data Model Spine"
tags:
  - "qicode"
  - "qios"
  - "qilife"
---
> **Parent:** [[00 - QiCode Home|QiCode Home]]
> **Related:** [[QiLife Doctrine|Doctrine]] · [[QiLife Data Model|Data Model]] · [[QiLife Workflows|Workflows]]

# QiLife Product Surfaces

> **Title:** 06 — QiLife  
> **Chapter:** 06.05 — Product Surfaces

> [!warning] Outline only
> These surfaces are registered, but detailed behavior is not yet ratified. This file intentionally does not invent requirements.

## § 06.05.001 — Inbox

## § 06.05.002 — Today

## § 06.05.003 — Calendar

## § 06.05.004 — Tasks

## § 06.05.005 — Activities

## § 06.05.006 — Routines

## § 06.05.007 — People & Relationships

## § 06.05.008 — Communication History

## § 06.05.009 — Projects & Workbench

## § 06.05.010 — Notes & Creative Work

## § 06.05.011 — Research

## § 06.05.012 — Outputs

---

## QiLife Workflows

---
title: "QiLife Workflows"
aliases:
  - "QiLife Views Review and Build Order"
system: "QiOS"
document_type: "workflow-doctrine"
status: "active-doctrine"
version: "1.0"
canonical: true
updated: "2026-07-18"
source:
  - "QiCode Documentation database"
  - "QiLife Data Model Spine"
tags:
  - "qicode"
  - "qios"
  - "qilife"
---
> **Parent:** [[00 - QiCode Home|QiCode Home]]
> **Related:** [[QiLife Doctrine|Doctrine]] · [[QiLife Architecture|Architecture]] · [[QiLife Data Model|Data Model]]

# QiLife Workflows

> **Title:** 06 — QiLife  
> **Chapter:** 06.04 — Views, Review & Build Order

This document defines derived views, truth-layer separation, AI approval flow, and implementation sequence.

## § 06.04.001 — Timeline Projection

The timeline is not a standalone table. It is a view or feed built from timestamped canonical records.

| Record Type | Timeline Timestamp |
| --- | --- |
| QiBit | `COALESCE(happened_at, captured_at, created_at)` |
| Action | `completed_at`, otherwise `scheduled_for`, otherwise `created_at` |
| Event | `start_time` |
| Daily Summary | `date` |
| Activity Log | `occurred_at` |

Documents, people, and knowledge items may appear in context panes and search results without becoming first-class timeline rows.

## § 06.04.002 — Human-in-the-Loop Truth Layers

QiLife must preserve the difference between:

1. raw input;
2. AI interpretation;
3. user-approved canonical records;
4. derived summaries; and
5. system logs.

No layer may silently overwrite another.

## § 06.04.003 — AI Review Queue

```text
Raw QiBit
  → AI suggestion
  → Review queue
  → Cody approves, edits, or rejects
  → Canonical record update
  → Activity log entry
```

No AI-generated recommendation may silently change canonical records.

## § 06.04.004 — Build Order

Build QiLife in this order:

```text
1. qibits
2. buckets
3. threads
4. actions
5. action_steps
6. people
7. events
8. documents
9. links
10. activity_log
11. ai_outputs
12. daily_summaries
```

Later phases may add:

```text
13. QiFinance bridge
14. transactions
15. obligations
16. richer reports
17. advanced automation
```

---

## QiLife Deferred Finance Bridge

---
title: "QiLife Deferred Finance Bridge"
aliases:
  - "QiLife Finance Bridge"
system: "QiOS"
document_type: "deferred-specification"
status: "deferred"
version: "1.0"
canonical: true
updated: "2026-07-18"
source:
  - "QiCode Documentation database"
  - "QiLife Data Model Spine"
tags:
  - "qicode"
  - "qios"
  - "qilife"
---
> **Parent:** [[00 - QiCode Home|QiCode Home]]
> **Related:** [[QiLife Doctrine|Doctrine]] · [[QiLife Data Model|Data Model]] · [[QiLife Workflows|Workflows]]

# QiLife Deferred Finance Bridge

> **Title:** 06 — QiLife  
> **Chapter:** 06.06 — Deferred Finance Bridge

This document preserves deferred finance concepts without making them part of QiLife core V1.

## § 06.06.001 — Boundary

Specialized finance tables are not part of QiLife core V1. They belong to a later **QiFinance** module or bridge.

QiLife may still capture financial or obligation-related information as QiBits, including:

- `transaction_seed`;
- `obligation_seed`;
- `receipt`;
- `payment_note`;
- `bill_note`; and
- `money_issue`.

The last three values are descriptive capture patterns unless later added to the canonical `qibit_type` registry.

## § 06.06.002 — Deferred Transactions

Transactions are not part of QiLife core V1. QiLife may capture transaction-related seeds as QiBits and connect them to documents, actions, or threads.

##### Deferred Table Sketch

```text
transactions
├── id
├── date
├── amount_cents
├── currency
├── direction
├── from_label
├── to_label
├── category
├── bucket_key
├── thread_id
├── status
├── notes
├── evidence_document_id
├── source_qibit_id
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

Do not build this table into QiLife core until a clear operational need exists. Until then, use QiFinance exports, documents, QiBits, and links.

## § 06.06.003 — Deferred Obligations

Obligations are not part of QiLife core V1. They may later belong to QiFinance, legal, or agreement-specific modules.

##### Deferred Table Sketch

```text
obligations
├── id
├── owed_by_label
├── owed_to_label
├── obligation_type
├── amount_cents
├── currency
├── reason
├── status
├── due_date
├── related_transaction_id
├── source_qibit_id
├── created_at
├── updated_at
├── resolved_at
├── archived_at
└── deleted_at
```

##### Deferred Obligation Statuses

```text
open
partial
waiting_on
resolved
disputed
archived
```

If the requirement is only “someone owes something,” capture it first as a QiBit or action. Create a dedicated obligations table only when the volume or importance cannot be handled through QiBits, actions, threads, and links.

---

---
