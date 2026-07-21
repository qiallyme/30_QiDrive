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