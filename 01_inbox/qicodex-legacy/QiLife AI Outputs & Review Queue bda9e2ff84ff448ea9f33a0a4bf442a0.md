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