# QiCode Legacy Archive & Historical Drafts Master

> **Consolidated Archive of Migration Notes, Legacy Specs & Compiled Drafts**

## QiCode Migration Notes

---
title: "QiCode Migration Notes"
aliases:
  - "QiCode Reconciliation Notes"
system: "QiOS"
document_type: "migration-record"
status: "active-record"
version: "1.0"
canonical: false
updated: "2026-07-18"
source:
  - "Original compiled doctrine"
  - "Intermediate cleaned draft"
  - "Final split package"
tags:
  - "qicode"
  - "migration"
  - "archive"
---
> **Parent:** [[00 - QiCode Home|QiCode Home]]
> **Related:** [[QiCode Registry|Final Registry]] · [[QiCode Numbering Standard|Numbering Standard]]

# QiCode Migration Notes

## Why the Source Could Not Remain One Document

The supplied compilation mixed four different jobs:

1. a master numbered registry;
2. active QiLife doctrine and schema content;
3. outline-only records for unrelated domains; and
4. legacy or quarantined material.

It also reused section numbers, repeated source metadata, scattered QiLife content across Titles 01, 03, 04, and 05, and placed a legacy QiLife specification under Security.

## Final Package Decision

- The registry now contains the map, status, and canonical destination only.
- Full QiLife content is split into six focused canonical documents.
- Outline-only sections remain in the registry without fabricated body text.
- Legacy QiLife material is quarantined.
- The original and intermediate compilation are preserved unchanged under `Sources`.

## QiLife Renumbering from the Intermediate Cleaned Draft

| Intermediate code | Final code | Canonical document |
| --- | --- | --- |
| `06.01.001` | `06.01.001` | QiLife Doctrine |
| `06.01.005` | `06.01.002` | QiLife Doctrine |
| `06.01.002–004` | `06.02.001–003` | QiLife Architecture |
| `06.02.001–013` | `06.03.001–013` | QiLife Data Model |
| `06.03.001–004` | `06.04.001–004` | QiLife Workflows |
| `06.04.001–012` | `06.05.001–012` | QiLife Product Surfaces |
| `06.05.001–003` | `06.06.001–003` | QiLife Deferred Finance Bridge |

## Original Collision Repairs Retained

| Original issue | Final treatment |
| --- | --- |
| Repeated `00.01.001–005` IDs | Unique registry order under Chapter 00.01 |
| Repeated `01.01.001–003` IDs | Unique registry order under Chapter 01.01 |
| `05.01` used as parent and section | Treated only as a chapter |
| `07.02` reused by security and QiLife legacy spec | Security remains active; legacy QiLife moved to archive |

## Unresolved Vocabulary

`payment_note`, `bill_note`, and `money_issue` appear in the deferred finance source but not in the canonical QiBit type list. They remain descriptive patterns, not valid `qibit_type` values, until deliberately added or removed.

## Source Preservation Rule

Do not edit the two files in `90 - Archive/Sources` when correcting active doctrine. They exist to show what was actually supplied and how the final structure was derived.

---

## QiLife App Spec - Legacy

---
title: "QiLife App Spec — Legacy"
aliases:
  - "Legacy QiLife App Spec"
system: "QiOS"
document_type: "legacy-specification"
status: "quarantined"
version: "1.0"
canonical: false
updated: "2026-07-18"
source:
  - "Original QiCode compiled doctrine"
tags:
  - "qicode"
  - "qilife"
  - "archive"
  - "legacy"
---
> **Parent:** [[QiCode Migration Notes|QiCode Migration Notes]]
> **Related:** [[QiLife Doctrine|Current Doctrine]]

# QiLife App Spec — Legacy

> [!danger] Quarantined
> This outline originally appeared under Title 07 — Security & Access. It is not active doctrine and must not be implemented unless a section is reviewed and promoted into the current Title 06 documents.

## Original Registry Location

- `§ 07.02 — QiLife App Spec`
- `§ 07.02.001 — Vision & Architecture`
- `§ 07.02.002 — Foundations & Environment`
- `§ 07.02.003 — Core Modules`
- `§ 07.02.004 — UI & Interaction`
- `§ 07.02.005 — Workflows & Automation`
- `§ 07.02.006 — Expansion & Collab`
- `§ 07.02.007 — DNA & Documentation`

## Current Disposition

| Legacy topic | Current canonical destination |
| --- | --- |
| Vision & Architecture | [[QiCode/02 - QiLife/QiLife Doctrine|QiLife Doctrine]] and [[QiCode/02 - QiLife/QiLife Architecture|QiLife Architecture]] |
| Foundations & Environment | [[QiCode/02 - QiLife/QiLife Architecture|QiLife Architecture]] |
| Core Modules | [[QiCode/02 - QiLife/QiLife Data Model|QiLife Data Model]] |
| UI & Interaction | [[QiCode/02 - QiLife/QiLife Product Surfaces|QiLife Product Surfaces]] |
| Workflows & Automation | [[QiCode/02 - QiLife/QiLife Workflows|QiLife Workflows]] |
| Expansion & Collaboration | Not ratified |
| DNA & Documentation | [[QiCode/01 - Registry/QiCode Governance|QiCode Governance]] |

No substantive body text was present in the supplied legacy outline. Nothing has been invented to fill that gap.

---

## QiCode Combined Cleaned Draft

# QiCode Doctrine & Registry

> **Status:** Working canonical compilation  
> **System:** QiOS  
> **Source:** QiCode Documentation database + reconciled QiLife Data Model Spine  
> **Version:** Cleaned Draft V1  
> **Purpose:** Provide one readable registry while keeping the full QiLife doctrine in its proper title.

## Document Rules

- Every section number in this compilation is unique.
- Chapter names use readable titles instead of database slugs.
- Outline-only records remain listed without invented body text.
- QiLife doctrine is consolidated under **Title 06 — QiLife** rather than scattered across architecture, records, workflow, and security titles.
- Repeated source metadata is stated once here instead of repeated beneath every merged section.
- Legacy QiLife specifications are quarantined under **Title 90 — Archive & Quarantine**.
- Raw source text should be retained separately for migration and audit purposes.

## Title Registry

| Title | Domain |
| --- | --- |
| 00 | General Provisions |
| 01 | Doctrine & Principles |
| 02 | Governance & Standards |
| 03 | System Architecture |
| 04 | Chronicle & Records |
| 05 | Operations & Workflows |
| 06 | QiLife |
| 07 | Security & Access |
| 08 | Finance & Assets |
| 09 | Legal Matters |
| 10 | Publication & Works |
| 90 | Archive & Quarantine |
| 99 | Experimental |

---

## Title 00 — General Provisions

### Chapter 00.01 — QiEOS Protocol v2.0

#### § 00.01.001 — Purpose

#### § 00.01.002 — Scope

#### § 00.01.003 — Definitions

#### § 00.01.004 — Realm Structure

#### § 00.01.005 — Hierarchy & Authority

#### § 00.01.006 — QiDecimal System

#### § 00.01.007 — QiCodex Unified Decimal Registry

#### § 00.01.008 — Numbering Rules

#### § 00.01.009 — Citation Format

#### § 00.01.010 — Privacy & Sovereignty

### Chapter 00.02 — Naming, Status & File Conventions

#### § 00.02.001 — Naming Rules

#### § 00.02.002 — Canonical Terms

#### § 00.02.003 — Retired Terms

#### § 00.02.004 — Status Labels

#### § 00.02.005 — File Conventions

---

## Title 01 — Doctrine & Principles

### Chapter 01.01 — Qi Doctrine & Principles

#### § 01.01.001 — Core Doctrine

#### § 01.01.002 — System Purpose

#### § 01.01.003 — Founding Principles

#### § 01.01.004 — Principle of Awareness

#### § 01.01.005 — Principle of Presence

#### § 01.01.006 — Modularity

#### § 01.01.007 — Minimum Viable Structure

#### § 01.01.008 — Human-First Operations

### Chapter 01.02 — Decision Rules

#### § 01.02.001 — Merge Before Splitting

#### § 01.02.002 — Properties Before New Tables

#### § 01.02.003 — Folders Must Earn Existence

#### § 01.02.004 — No Placeholder Architecture

#### § 01.02.005 — Archive Instead of Deleting

---

## Title 02 — Governance & Standards

### Chapter 02.01 — Decisions, Standards & Templates

#### § 02.01.001 — Decision Records

#### § 02.01.002 — Standards

#### § 02.01.003 — Templates

#### § 02.01.004 — Forms

#### § 02.01.005 — Versioning

### Chapter 02.02 — Change Control & Deprecation

#### § 02.02.001 — Change Requests

#### § 02.02.002 — Migration Rules

#### § 02.02.003 — Deprecation Rules

#### § 02.02.004 — Supersession

#### § 02.02.005 — Review Cycle

#### § 02.02.006 — Versioning & Continuity

#### § 02.02.007 — Updates & Ratification

---

## Title 03 — System Architecture

### Chapter 03.01 — QiLabs Root Model

#### § 03.01.001 — Canonical Root Structure

#### § 03.01.002 — Workspace Layer

#### § 03.01.003 — Docs Layer

#### § 03.01.004 — Runtime Layer

#### § 03.01.005 — Records Layer

#### § 03.01.006 — Apps Layer

### Chapter 03.02 — QiSpark Documentation & Landing

#### § 03.02.001 — QiSpark Scope

#### § 03.02.002 — Docs Site Role

#### § 03.02.003 — Landing Page Role

#### § 03.02.004 — QiDNA Placement

#### § 03.02.005 — Navigation Model

### Chapter 03.03 — QiServer Runtime & Cloudflare

#### § 03.03.001 — QiServer Scope

#### § 03.03.002 — Cockpit

#### § 03.03.003 — Runtime Services

#### § 03.03.004 — Cloudflare & Zero Trust

#### § 03.03.005 — Backups, Secrets & Recovery

### Chapter 03.04 — QiDrive Records & Evidence

#### § 03.04.001 — QiDrive Scope

#### § 03.04.002 — Drive Mirror

#### § 03.04.003 — Evidence Libraries

#### § 03.04.004 — Retention

#### § 03.04.005 — Export Bundles

### Chapter 03.05 — QiApps, Projects & Integrations

#### § 03.05.001 — QiApps Scope

#### § 03.05.002 — App Registry

#### § 03.05.003 — Project Standards

#### § 03.05.004 — Shared Components

#### § 03.05.005 — External Integrations

#### § 03.05.006 — QiLife Placement Reference

QiLife is an application within **QiApps**. Its complete operating doctrine and data model are defined in **Title 06 — QiLife**.

---

## Title 04 — Chronicle & Records

### Chapter 04.01 — Timeline, Journal & Chronicle

#### § 04.01.001 — Chronicle Purpose

#### § 04.01.002 — Timeline Events

#### § 04.01.003 — Journal Entries

#### § 04.01.004 — Daily Logs

#### § 04.01.005 — Incident Logs

#### § 04.01.006 — Relationship Notes

#### § 04.01.007 — Decision Notes

#### § 04.01.008 — Evidence Links

#### § 04.01.009 — Review & Reconstruction

#### § 04.01.010 — QiLife Chronicle Reference

QiLife-specific timeline projection rules are defined in **§ 06.03.001**.

### Chapter 04.02 — Records, Metadata & Links

#### § 04.02.001 — Record Definition

#### § 04.02.002 — Record Types

#### § 04.02.003 — Metadata

#### § 04.02.004 — Tags

#### § 04.02.005 — Links & Relationships

#### § 04.02.006 — QiLife Records Reference

QiLife-specific object definitions are defined in **Chapter 06.02**.

### Chapter 04.03 — Evidence, Audit, Import & Export

#### § 04.03.001 — Evidence Definition

#### § 04.03.002 — Audit Trail

#### § 04.03.003 — Retention Rules

#### § 04.03.004 — Import Standard

#### § 04.03.005 — Export Standard

#### § 04.03.006 — QiLife Audit Reference

QiLife activity logs and daily summaries are defined in **§§ 06.02.011–06.02.013**.

---

## Title 05 — Operations & Workflows

### Chapter 05.01 — QiAlly Delivery OS

#### § 05.01.001 — Workflow Standard

#### § 05.01.002 — SOP Standard

#### § 05.01.003 — Routine Standard

#### § 05.01.004 — Checklist Standard

#### § 05.01.005 — Runbook Standard

#### § 05.01.006 — QiLife Workflow Reference

QiLife threads, actions, review workflows, and build order are defined in **Title 06**.

### Chapter 05.02 — Maintenance, Incidents & Deployment

#### § 05.02.001 — Maintenance

#### § 05.02.002 — Incident Levels

#### § 05.02.003 — Recovery Process

#### § 05.02.004 — Deployment Process

#### § 05.02.005 — Rollback Process

---

## Title 06 — QiLife

> **Status:** Active Doctrine  
> **Version:** Reconciled V1  
> **System:** QiOS  
> **Parent:** QiApps  
> **Source:** Consolidated from the QiLife Data Model Spine

### Chapter 06.01 — Purpose, Placement & Boundaries

#### § 06.01.001 — Purpose & Operating Doctrine

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

#### § 06.01.002 — Position in QiOS

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

#### § 06.01.003 — Canonical Placement

- **Application home:** `QiApps/QiLife`
- **Documentation home:** `QiSpark/docs`
- **File backbone:** `QiDrive`

QiLife remains in the application layer. Doctrine and published documentation belong in QiSpark; files belong in QiDrive; runtime services belong in QiServer; synchronization pathways belong in QiConnect; inactive versions belong in QiArchive.

#### § 06.01.004 — Database Portability

QiLife’s data model must remain database-portable.

It may begin locally with SQLite for speed, but the schema must be able to move to PostgreSQL or Supabase without conceptual redesign.

#### § 06.01.005 — Core V1 Scope

QiLife V1 starts with capture, buckets, threads, actions, people, events, documents, links, and review.

Do not start with:

- finance;
- advanced AI; or
- perfect UI.

### Chapter 06.02 — Core V1 Data Model

#### § 06.02.001 — Core Tables

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

#### § 06.02.002 — QiBits

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

#### § 06.02.003 — Buckets

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

#### § 06.02.004 — Threads

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

#### § 06.02.005 — Actions & Action Steps

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

#### § 06.02.006 — People

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

#### § 06.02.007 — Events

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

#### § 06.02.008 — Documents

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

#### § 06.02.009 — Knowledge Items

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

#### § 06.02.010 — Links

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

#### § 06.02.011 — Activity Log

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

#### § 06.02.012 — AI Outputs

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

#### § 06.02.013 — Daily Summaries

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

### Chapter 06.03 — Views, Review & Workflow

#### § 06.03.001 — Timeline Projection

The timeline is not a standalone table. It is a view or feed built from timestamped canonical records.

| Record Type | Timeline Timestamp |
| --- | --- |
| QiBit | `COALESCE(happened_at, captured_at, created_at)` |
| Action | `completed_at`, otherwise `scheduled_for`, otherwise `created_at` |
| Event | `start_time` |
| Daily Summary | `date` |
| Activity Log | `occurred_at` |

Documents, people, and knowledge items may appear in context panes and search results without becoming first-class timeline rows.

#### § 06.03.002 — Human-in-the-Loop Truth Layers

QiLife must preserve the difference between:

1. raw input;
2. AI interpretation;
3. user-approved canonical records;
4. derived summaries; and
5. system logs.

No layer may silently overwrite another.

#### § 06.03.003 — AI Review Queue

```text
Raw QiBit
  → AI suggestion
  → Review queue
  → Cody approves, edits, or rejects
  → Canonical record update
  → Activity log entry
```

No AI-generated recommendation may silently change canonical records.

#### § 06.03.004 — Build Order

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

### Chapter 06.04 — Product Surfaces

These sections define application surfaces. Their detailed body content remains pending unless separately ratified.

#### § 06.04.001 — Inbox

#### § 06.04.002 — Today

#### § 06.04.003 — Calendar

#### § 06.04.004 — Tasks

#### § 06.04.005 — Activities

#### § 06.04.006 — Routines

#### § 06.04.007 — People & Relationships

#### § 06.04.008 — Communication History

#### § 06.04.009 — Projects & Workbench

#### § 06.04.010 — Notes & Creative Work

#### § 06.04.011 — Research

#### § 06.04.012 — Outputs

### Chapter 06.05 — Deferred Finance Bridge

#### § 06.05.001 — Boundary

Specialized finance tables are not part of QiLife core V1. They belong to a later **QiFinance** module or bridge.

QiLife may still capture financial or obligation-related information as QiBits, including:

- `transaction_seed`;
- `obligation_seed`;
- `receipt`;
- `payment_note`;
- `bill_note`; and
- `money_issue`.

The last three values are descriptive capture patterns unless later added to the canonical `qibit_type` registry.

#### § 06.05.002 — Deferred Transactions

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

#### § 06.05.003 — Deferred Obligations

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

## Title 07 — Security & Access

### Chapter 07.01 — Accounts, Permissions & Devices

#### § 07.01.001 — Account Registry

#### § 07.01.002 — Roles

#### § 07.01.003 — Permissions

#### § 07.01.004 — Devices

#### § 07.01.005 — Access Review

### Chapter 07.02 — Secrets, Incidents & Recovery

#### § 07.02.001 — Passwords

#### § 07.02.002 — API Keys

#### § 07.02.003 — Recovery Codes

#### § 07.02.004 — Security Incidents

#### § 07.02.005 — Credential Rotation

---

## Title 08 — Finance & Assets

### Chapter 08.01 — Finance, Inventory & Reimbursements

#### § 08.01.001 — Accounts

#### § 08.01.002 — Transactions

#### § 08.01.003 — Receipts

#### § 08.01.004 — Inventory

#### § 08.01.005 — Reimbursements

### Chapter 08.02 — Assets, Debts & Reports

#### § 08.02.001 — Assets

#### § 08.02.002 — Property

#### § 08.02.003 — Debts

#### § 08.02.004 — Claims

#### § 08.02.005 — Reports

---

## Title 09 — Legal Matters

### Chapter 09.01 — Contracts, Notices & Housing

#### § 09.01.001 — Contracts

#### § 09.01.002 — Agreements

#### § 09.01.003 — Notices

#### § 09.01.004 — Housing Records

#### § 09.01.005 — Deadlines

### Chapter 09.02 — Disputes, Claims & Client Matters

#### § 09.02.001 — Disputes

#### § 09.02.002 — Claims

#### § 09.02.003 — Evidence Packets

#### § 09.02.004 — Client Matters

#### § 09.02.005 — Case Timelines

---

## Title 10 — Publication & Works

### Chapter 10.01 — Publication Registry

#### § 10.01.001 — Work Types

#### § 10.01.002 — Draft Status

#### § 10.01.003 — Publication Status

#### § 10.01.004 — Platforms

#### § 10.01.005 — Canonical Versions

### Chapter 10.02 — Series, Books, Posts & Pages

#### § 10.02.001 — Series

#### § 10.02.002 — Books

#### § 10.02.003 — Chapters

#### § 10.02.004 — Essays & Posts

#### § 10.02.005 — Public Pages

---

## Title 90 — Archive & Quarantine

### Chapter 90.01 — Archive, Deprecation & Cleanup

#### § 90.01.001 — Archive Rules

#### § 90.01.002 — Superseded Items

#### § 90.01.003 — Deprecated Items

#### § 90.01.004 — Quarantine

#### § 90.01.005 — Cleanup Rules

### Chapter 90.02 — Quarantined Legacy Specifications

#### § 90.02.001 — Legacy QiLife App Spec

**Original location:** Title 07, under Security & Access  
**Current status:** Quarantined pending reconciliation against Title 06

Legacy outline:

- Vision & Architecture
- Foundations & Environment
- Core Modules
- UI & Interaction
- Workflows & Automation
- Expansion & Collaboration
- DNA & Documentation

This legacy outline must not be treated as active doctrine unless a specific item is reviewed, reconciled, and promoted into Title 06.

---

## Title 99 — Experimental

### Chapter 99.01 — Prototypes, Research & Parking Lot

#### § 99.01.001 — Prototypes

#### § 99.01.002 — Research

#### § 99.01.003 — Future Concepts

#### § 99.01.004 — Evaluation

#### § 99.01.005 — Promote or Kill Rules

---

## Migration Notes

### Numbering Collisions Resolved

The source compilation reused several section IDs. This cleaned draft assigns unique numbers and treats container-like entries as chapter headings where appropriate.

| Source collision | Resolution in this draft |
| --- | --- |
| `00.01.001` used for Purpose and Realm Structure | Reordered and uniquely numbered under Chapter 00.01 |
| `00.01.002` used for QiDecimal System and Scope | Reordered and uniquely numbered under Chapter 00.01 |
| `00.01.003` used for Definitions and Hierarchy & Authority | Reordered and uniquely numbered under Chapter 00.01 |
| `00.01.004` used for Citation Format and Privacy & Sovereignty | Reordered and uniquely numbered under Chapter 00.01 |
| `00.01.005` used for Registry and Numbering Rules | Reordered and uniquely numbered under Chapter 00.01 |
| `01.01.001–003` each reused | Reordered and uniquely numbered under Chapter 01.01 |
| `05.01` used as both a parent and numbered section | Treated as Chapter 05.01 |
| `07.02` reused for Security and legacy QiLife | Legacy QiLife moved to Chapter 90.02 |

### Content Consolidation

The following QiLife material was moved into Title 06:

- purpose and operating doctrine;
- position within QiOS;
- core V1 data model;
- QiBits and timeline projection;
- buckets, documents, knowledge items, and links;
- people and events;
- activity log and daily summaries;
- threads, actions, and build order;
- AI outputs and review queue; and
- deferred finance bridge.

### Source Preservation

This document is a cleaned working compilation, not a substitute for the raw database export. Retain the original compilation as migration evidence until the database section IDs and hierarchy are updated.

---

## QiCode Compiled Doctrine - Original

# QiCode Documentation — Compiled Doctrine

<aside>
📌

Compiled from the QiCode_Documentation database. Organized by title, chapter, and section heading.

</aside>

## Title 00 — General Provisions

### Chapter: scope_definitions_numbering

#### § 00.01 — QiEOS Protocol v2.0

#### § 00.01.001 — Purpose

#### § 00.01.001 — Realm Structure

#### § 00.01.002 — QiDecimal System

#### § 00.01.002 — Scope

#### § 00.01.003 — Definitions

#### § 00.01.003 — Hierarchy & Authority

#### § 00.01.004 — Citation Format

#### § 00.01.004 — Privacy & Sovereignty

#### § 00.01.005 — QiCodex Unified Decimal Registry

#### § 00.01.005 — Numbering Rules

### Chapter: naming_status_conventions

#### § 00.02.001 — Naming Rules

#### § 00.02.002 — Canonical Terms

#### § 00.02.003 — Retired Terms

#### § 00.02.004 — Status Labels

#### § 00.02.005 — File Conventions

## Title 01 — Doctrine & Principles

### Chapter: qi_doctrine_principles

#### § 01.01.001 — Principle of Awareness

#### § 01.01.001 — Core Doctrine

#### § 01.01.002 — Principle of Presence

#### § 01.01.002 — System Purpose

#### § 01.01.003 — Founding Principles

#### § 01.01.003 — Modularity

#### § 01.01.004 — Minimum Viable Structure

#### § 01.01.005 — Human-First Operations

#### § 01.01.006 — QiLife Purpose & Operating Doctrine

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

#### Purpose

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

#### Doctrine Rules

- IDs use **ULIDs** for user-created records.
- Static lookup tables may use stable text keys.
- Raw capture is preserved.
- AI output is stored separately from approved truth.
- Timeline is a projection, not a separate core table.
- Files live in QiDrive; QiLife stores metadata and links.
- Notes and reflections are QiBit types, not separate tables.
- Finance-specific records are deferred unless needed.
- Properties, tags, metadata, and links should be used before creating more tables.

#### Final Operating Rule

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

### Chapter: decision_rules

#### § 01.02.001 — Merge Before Splitting

#### § 01.02.002 — Properties Before New Tables

#### § 01.02.003 — Folders Must Earn Existence

#### § 01.02.004 — No Placeholder Architecture

#### § 01.02.005 — Archive Instead of Deleting

## Title 02 — Governance & Standards

### Chapter: decisions_standards_templates

#### § 02.01.001 — Decision Records

#### § 02.01.002 — Standards

#### § 02.01.003 — Templates

#### § 02.01.004 — Forms

#### § 02.01.005 — Versioning

### Chapter: change_control_deprecation

#### § 02.02.001 — Change Requests

#### § 02.02.002 — Migration Rules

#### § 02.02.003 — Deprecation Rules

#### § 02.02.004 — Supersession

#### § 02.02.005 — Review Cycle

#### § 02.02.006 — Versioning & Continuity

#### § 02.02.007 — Updates & Ratification

## Title 03 — System Architecture

### Chapter: qilabs_root_model

#### § 03.01.001 — Canonical Root Structure

#### § 03.01.002 — Workspace Layer

#### § 03.01.003 — Docs Layer

#### § 03.01.004 — Runtime Layer

#### § 03.01.005 — Records Layer

#### § 03.01.006 — Apps Layer

### Chapter: qispark_docs_landing

#### § 03.02.001 — QiSpark Scope

#### § 03.02.002 — Docs Site Role

#### § 03.02.003 — Landing Page Role

#### § 03.02.004 — QiDNA Placement

#### § 03.02.005 — Navigation Model

### Chapter: qiserver_runtime_cloudflare

#### § 03.03.001 — QiServer Scope

#### § 03.03.002 — Cockpit

#### § 03.03.003 — Runtime Services

#### § 03.03.004 — Cloudflare / Zero Trust

#### § 03.03.005 — Backups, Secrets & Recovery

### Chapter: qidrive_records_evidence

#### § 03.04.001 — QiDrive Scope

#### § 03.04.002 — Drive Mirror

#### § 03.04.003 — Evidence Libraries

#### § 03.04.004 — Retention

#### § 03.04.005 — Export Bundles

### Chapter: qiapps_projects_integrations

#### § 03.05.001 — QiApps Scope

#### § 03.05.002 — App Registry

#### § 03.05.003 — Project Standards

#### § 03.05.004 — Shared Components

#### § 03.05.005 — External Integrations

#### § 03.05.006 — QiLife App Placement

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

#### Position in QiOS

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

#### App Placement

- **App Home:** `QiApps/QiLife`
- **Docs Home:** `QiSpark/docs`
- **File Backbone:** QiDrive

#### Architecture Rule

QiLife is the app-layer operating system for living records. It should stay inside **QiApps**, while doctrine and published documentation live in **QiSpark**, files live in **QiDrive**, runtime services live in **QiServer**, sync pathways live in **QiConnect**, and inactive versions live in **QiArchive**.

#### § 03.05.007 — QiLife Core V1 Data Model

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

#### Database Doctrine

QiLife’s model should remain database-portable.

It may begin locally with SQLite for speed, but the schema should be able to move to Postgres / Supabase without conceptual rewrite.

#### Core V1 Tables

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

#### Core Object Map

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

#### Core V1 Rule

QiLife starts with capture, buckets, threads, actions, people, documents, links, and review.

Do not start with finance.

Do not start with advanced AI.

Do not start with perfect UI.

## Title 04 — Chronicle & Records

### Chapter: timeline_journal_chronicle

#### § 04.01.001 — Chronicle Purpose

#### § 04.01.002 — Timeline Events

#### § 04.01.003 — Journal Entries

#### § 04.01.004 — Daily Logs

#### § 04.01.005 — Incident Logs

#### § 04.01.006 — Relationship Notes

#### § 04.01.007 — Decision Notes

#### § 04.01.008 — Evidence Links

#### § 04.01.009 — Review / Reconstruction

#### § 04.01.010 — QiLife QiBits & Timeline Projection

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

#### Timeline Projection

Timeline is not its own table.

Timeline is a view/feed built from timestamped records.

#### Timeline Timestamp Rules

| Record Type | Timeline Timestamp Rule |
| --- | --- |
| QiBit | `COALESCE(happened_at, captured_at, created_at)` |
| Action | `completed_at` if present, else `scheduled_for`, else `created_at` |
| Event | `start_time` |
| Daily Summary | `date` |
| Activity Log | `occurred_at` |

Documents, people, and knowledge items may appear in context panes and search results without becoming first-class timeline rows.

#### QiBits

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

#### QiBit Types

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

#### QiBit Statuses

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

#### Sacred Rule

`raw_capture` is the original truth. Summaries and interpretations are editable. The raw capture is not overwritten.

### Chapter: records_metadata_links

#### § 04.02.001 — Record Definition

#### § 04.02.002 — Record Types

#### § 04.02.003 — Metadata

#### § 04.02.004 — Tags

#### § 04.02.005 — Links & Relationships

#### § 04.02.006 — QiLife Buckets, Documents, Knowledge & Links

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

#### Records, Metadata, and Links

QiLife records should clarify what something is, where it belongs, and what it relates to before creating new structures.

#### Buckets

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

#### Seed Buckets

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

#### Bucket Meanings

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

#### Documents

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

#### Document Rule

QiDrive stores the file.

QiLife stores:

- what it is
- where it is
- what it relates to
- whether it matters
- how to retrieve it

#### Knowledge Items

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

#### Knowledge Types

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

#### Repo Docs Rule

Docs imported from QiSpark or app repos are read-only in QiLife unless edited at their source.

QiLife can index and reference docs, but it should not silently fork doctrine.

#### Links

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

#### Common Relationships

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

#### Link Rule

Use links before duplicating data.

#### § 04.02.007 — QiLife People & Events

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

#### People

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

#### People Types

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

#### People Rule

Do not create separate tables for vendors, agencies, government contacts, care team, and organizations.

Use one table with `type`, `relationship`, `role`, tags, and metadata.

#### Events

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

#### Event Statuses

```
scheduled
completed
cancelled
missed
archived
```

#### Event Rule

Events may sync with Google Calendar later through QiConnect.

QiLife should not assume Google Calendar is the only calendar source.

### Chapter: evidence_audit_import_export

#### § 04.03.001 — Evidence Definition

#### § 04.03.002 — Audit Trail

#### § 04.03.003 — Retention Rules

#### § 04.03.004 — Import Standard

#### § 04.03.005 — Export Standard

#### § 04.03.006 — QiLife Activity Log & Daily Summaries

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

#### Audit Trail

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

#### Activity Log Rule

The activity log records what changed.

It should not replace notes, summaries, or timeline projections.

#### Daily Summaries

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

#### Daily Summary Rule

Daily summaries are retrieval and reflection helpers.

They do not replace raw QiBits, activity logs, or source records.

#### Activity Log vs Daily Summaries vs Reflections

| Object | Meaning |
| --- | --- |
| `activity_log` | Append-only record of changes |
| `daily_summaries` | Synthesized day-level reviews |
| `qibits.reflection` | User-authored or AI-assisted reflection tied to a captured item |

Do not merge these.

They serve different jobs.

## Title 05 — Operations & Workflows

### Chapter: workflows_sops_routines

#### § 05.01 — QiAlly Delivery OS

#### § 05.01.001 — Workflow Standard

#### § 05.01.002 — SOP Standard

#### § 05.01.003 — Routine Standard

#### § 05.01.004 — Checklist Standard

#### § 05.01.005 — Runbook Standard

#### § 05.01.006 — QiLife Threads, Actions & Build Order

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

#### Threads

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

#### Thread Statuses

```
open
active
waiting_on
resolved
closed
archived
```

#### Thread Rule

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

#### Actions

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

#### Action Statuses

```
open
in_progress
waiting_on
scheduled
completed
cancelled
archived
```

#### Action Rule

If it requires doing something, it becomes an action.

If it is just context, it remains a QiBit, knowledge item, document, event, or thread note.

#### Action Steps

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

#### Build Order

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

#### § 05.01.007 — QiLife AI Outputs & Review Queue

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

#### AI Outputs

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

#### AI Rule

AI may suggest.

AI may not silently approve itself.

Approved AI output should create or update canonical records through a reviewed action.

#### Human-in-the-Loop Doctrine

QiLife must preserve the difference between:

- raw input
- AI interpretation
- user-approved records
- derived summaries
- system logs

#### Approval Flow

```
Raw QiBit
  -> AI suggestion
  -> Review queue
  -> Cody approves / edits / rejects
  -> Canonical record update
  -> Activity log entry
```

#### Rule

No silent canonical changes from AI.

### Chapter: maintenance_incidents_deployment

#### § 05.02.001 — Maintenance

#### § 05.02.002 — Incident Levels

#### § 05.02.003 — Recovery Process

#### § 05.02.004 — Deployment Process

#### § 05.02.005 — Rollback Process

#### § 05.02.006 — QiLife Deferred Finance Bridge

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Deferred  

**Version:** Reconciled V1

#### Deferred / Not Core V1

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

#### Deferred: `transactions`

Transactions are not QiLife core V1.

They belong to a later QiFinance module or bridge.

QiLife may capture transaction-related seeds as QiBits.

#### Deferred Table Sketch

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

#### Rule

Do not build this into QiLife core until there is a clear reason.

For now, use finance app exports, documents, QiBits, and links.

#### Deferred: `obligations`

Obligations are not QiLife core V1.

They belong to a later QiFinance / legal / agreements module if needed.

QiLife may capture obligation-related seeds as QiBits or actions.

#### Deferred Table Sketch

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

#### Statuses

```
open
partial
waiting_on
resolved
disputed
archived
```

#### Rule

If it is just “someone owes something,” capture it as a QiBit or Action first.

Create a full obligations table only when tracking becomes too frequent or too important to handle through QiBits, actions, threads, and links.

## Title 06 — QiLife

### Chapter: planner_activities_routines

#### § 06.01.001 — Inbox

#### § 06.01.002 — Today

#### § 06.01.003 — Calendar

#### § 06.01.004 — Tasks

#### § 06.01.005 — Activities

#### § 06.01.006 — Routines

### Chapter: erm_people_vendors_government

#### § 06.02.001 — People

#### § 06.02.002 — Vendors

#### § 06.02.003 — Government

#### § 06.02.004 — Relationships

#### § 06.02.005 — Communication History

### Chapter: workbench_projects_creative

#### § 06.03.001 — Projects

#### § 06.03.002 — Notes

#### § 06.03.003 — Creative Work

#### § 06.03.004 — Research

#### § 06.03.005 — Outputs

## Title 07 — Security & Access

### Chapter: accounts_permissions_devices

#### § 07.01.001 — Account Registry

#### § 07.01.002 — Roles

#### § 07.01.003 — Permissions

#### § 07.01.004 — Devices

#### § 07.01.005 — Access Review

### Chapter: secrets_incidents_recovery

#### § 07.02.001 — Passwords

#### § 07.02.002 — API Keys

#### § 07.02.003 — Recovery Codes

#### § 07.02.004 — Security Incidents

#### § 07.02.005 — Credential Rotation

### Chapter: qiapps_projects_integrations / legacy QiLife App Spec

#### § 07.02 — QiLife App Spec

#### § 07.02.001 — Vision & Architecture

#### § 07.02.002 — Foundations & Environment

#### § 07.02.003 — Core Modules

#### § 07.02.004 — UI & Interaction

#### § 07.02.005 — Workflows & Automation

#### § 07.02.006 — Expansion & Collab

#### § 07.02.007 — DNA & Documentation

## Title 08 — Finance & Assets

### Chapter: finance_inventory_reimbursements

#### § 08.01.001 — Accounts

#### § 08.01.002 — Transactions

#### § 08.01.003 — Receipts

#### § 08.01.004 — Inventory

#### § 08.01.005 — Reimbursements

### Chapter: assets_debts_reports

#### § 08.02.001 — Assets

#### § 08.02.002 — Property

#### § 08.02.003 — Debts

#### § 08.02.004 — Claims

#### § 08.02.005 — Reports

## Title 09 — Legal Matters

### Chapter: contracts_notices_housing

#### § 09.01.001 — Contracts

#### § 09.01.002 — Agreements

#### § 09.01.003 — Notices

#### § 09.01.004 — Housing Records

#### § 09.01.005 — Deadlines

### Chapter: disputes_claims_client_matters

#### § 09.02.001 — Disputes

#### § 09.02.002 — Claims

#### § 09.02.003 — Evidence Packets

#### § 09.02.004 — Client Matters

#### § 09.02.005 — Case Timelines

## Title 10 — Publication & Works

### Chapter: publication_registry

#### § 10.01.001 — Work Types

#### § 10.01.002 — Draft Status

#### § 10.01.003 — Publication Status

#### § 10.01.004 — Platforms

#### § 10.01.005 — Canonical Versions

### Chapter: series_books_posts_pages

#### § 10.02.001 — Series

#### § 10.02.002 — Books

#### § 10.02.003 — Chapters

#### § 10.02.004 — Essays / Posts

#### § 10.02.005 — Public Pages

## Title 90 — Archive & Quarantine

### Chapter: archive_deprecated_quarantine

#### § 90.01.001 — Archive Rules

#### § 90.01.002 — Superseded Items

#### § 90.01.003 — Deprecated Items

#### § 90.01.004 — Quarantine

#### § 90.01.005 — Cleanup Rules

## Title 99 — Experimental

### Chapter: prototypes_research_parking_lot

#### § 99.01.001 — Prototypes

#### § 99.01.002 — Research

#### § 99.01.003 — Future Concepts

#### § 99.01.004 — Evaluation

#### § 99.01.005 — Promote / Kill Rules

---

## Compilation Notes

- This document preserves the database order by QiCode.
- Entries with available body content are included under their section headings.
- Entries that currently function as outline records are represented by title, chapter, and section heading.
- Superseded combined source content was not duplicated where the newer split active sections already contain the merged content.

---
