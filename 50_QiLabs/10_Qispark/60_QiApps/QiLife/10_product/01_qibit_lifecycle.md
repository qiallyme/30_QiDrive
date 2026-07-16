---
layout: page
title: QiBit Lifecycle
slug: qibit-lifecycle
status: publish
updated_at: "2026-07-16T06:49:40-04:00"
tags: []
  - qispark
source_type: manual
summary: ""
created_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: bed34f70d9d74f6d9e6c2cd4f30df39a
canonical_ref: ""
template_key: master-template
---

# QiBit Lifecycle

## Definition

A QiBit is one captured unit of life data.

It begins with:

**What happened-**

It may become a task, note, action, thread update, transaction, obligation, document reference, knowledge item, event, reminder, reflection, or no-action log.

## Lifecycle Questions

| Question | Function | Output |
|---|---|---|
| What- | Capture | raw capture, title, summary |
| Where- | Bucket | area/domain |
| Why- | Interpret | meaning, importance, consequence |
| Who- | Relate | people/entities |
| When- | Slot | date, schedule, future slot |
| How- | Breakdown | action, steps, process |
| Because- | Enrich | knowledge, documents, evidence |
| Then- | Act | action/task/work item |
| Done- | Resolve | outcome/completion |
| So what- | Reflect | lesson/pattern/decision |
| Find later- | Retrieve | tags, links, AI memory |

## QiBit Statuses

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

## Priority

Priority should be consequence-based.

| Priority | Meaning |
|---|---|
| critical | money/legal/safety/deadline risk |
| high | meaningful consequence soon |
| normal | needs handling but not on fire |
| low | useful but not required |
| someday | parking lot |

## Future Slots

```text
today
this_week
scheduled
waiting_on
someday
knowledge_base
archive
ignore
```

## QiBit Detail Page Sections

```text
QiBit Detail
├── What Happened
├── What It Means
├── Bucket / Queue
├── Thread / Case
├── Related People / Entities
├── Related Documents
├── Related Money
├── Action Required
├── Actions
├── Steps
├── Future Slot
├── Resolution
├── Reflection
└── Retrieval Tags / Links
```

## Example QiBit

Raw capture:

"Zai owes me $40 for gas."

Interpreted:

- What happened: Cody fronted or tracked gas involving Zai.
- Meaning: open reimbursement obligation.
- Bucket: 60 Finance.
- Related person: Zai.
- Action required: yes.
- Action: confirm/collect repayment.
- Future slot: waiting_on.
- Related money: obligation for $40.
- Retrieval: who owes me money, gas, Zai, reimbursement.
