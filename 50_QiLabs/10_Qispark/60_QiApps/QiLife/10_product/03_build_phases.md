---
layout: page
title: QiLife Build Phases
slug: qilife-build-phases
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
uid: 806d851648d04f90ae2b1496d501de4f
canonical_ref: ""
template_key: master-template
---

# QiLife Build Phases

## Phase 0 - Review Docs

Goal: produce coherent product, architecture, and schema docs before coding.

## Phase 1 - Spine

Goal: build the core nervous system.

Build:

```text
App shell
Left nav
Center workspace
Context Dock shell
QiBit model
Buckets
Threads
Actions
Timeline
Inbox
Ask QiLife placeholder
```

Success criteria:

- User can capture a QiBit.
- QiBit appears on Timeline.
- QiBit can be assigned a bucket and thread.
- QiBit can create an action.
- Action can have steps.
- Context Dock can show placeholder context.
- Ask QiLife page exists with placeholder response.

## Phase 2 - Daily Command Layer

Goal: make the app useful every day.

Build:

```text
Today dashboard
Due and scheduled action views
Open loops
waiting_on items
Today's QiBits
Daily summary placeholder
Basic calendar view
Reflection prompt
```

Success criteria:

- User can see what matters today.
- User can see open loops and waiting_on items.
- User can see what happened today.

## Phase 3 - Context Layer

Goal: bring knowledge beside the work.

Build:

```text
Knowledge item CRUD
Markdown rendering
Linked note/reflection QiBits
Documents metadata
Person pages
Thread summaries
Context Dock enrichment
```

Success criteria:

- Knowledge can attach to buckets, threads, actions, QiBits, and people.
- Context Dock displays relevant linked knowledge.
- Central Knowledge page is navigable.

## Phase 4 - Money Layer

Goal: track transactions and obligations.

## Phase 5 - AI Layer

Goal: make AI useful and connected.

## Phase 6 - Import/Export and QiNexus Alignment

Goal: make data portable while preserving repo docs as canonical during build.
