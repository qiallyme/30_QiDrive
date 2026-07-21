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