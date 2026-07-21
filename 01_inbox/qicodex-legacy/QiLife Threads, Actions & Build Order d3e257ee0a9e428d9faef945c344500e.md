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