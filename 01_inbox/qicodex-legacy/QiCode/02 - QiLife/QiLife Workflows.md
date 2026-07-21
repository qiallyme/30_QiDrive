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
