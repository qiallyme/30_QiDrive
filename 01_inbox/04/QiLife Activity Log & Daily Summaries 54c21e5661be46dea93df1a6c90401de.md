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