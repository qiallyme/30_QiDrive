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