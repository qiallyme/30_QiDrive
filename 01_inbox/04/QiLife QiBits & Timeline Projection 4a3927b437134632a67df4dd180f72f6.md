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