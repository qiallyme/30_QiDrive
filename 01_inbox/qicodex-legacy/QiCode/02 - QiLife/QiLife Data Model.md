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
