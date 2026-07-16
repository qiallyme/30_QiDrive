---
layout: page
title: Actions: Data Dependencies
slug: actions-data-dependencies
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
uid: 6d79dd2d98bb44dd92ffe048288cbc33
canonical_ref: ""
template_key: master-template
---

# Actions: Data Dependencies
*   **Reads/Writes**: Writes to `actions` and `action_steps` tables.
*   **Foreign Keys**: Relates to `qibits` via `source_qibit_id`, and `threads` via `thread_id`.
*   **Links**: Integrates with `people`, `money`, and `documents` tables via the central `links` schema.
