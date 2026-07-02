---
layout: page
title: Actions: Data Dependencies
slug: actions-data-dependencies
status: active
updated_at: "2026-06-29"
tags:
  - qispark
source_type: manual
summary: ""
created_at: ""
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
template_key: master-template
---

# Actions: Data Dependencies
*   **Reads/Writes**: Writes to `actions` and `action_steps` tables.
*   **Foreign Keys**: Relates to `qibits` via `source_qibit_id`, and `threads` via `thread_id`.
*   **Links**: Integrates with `people`, `money`, and `documents` tables via the central `links` schema.
