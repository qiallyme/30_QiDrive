---
layout: page
title: Data Dependencies
slug: ""
summary: ""
status: active
created_at: ""
updated_at: ""
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Actions: Data Dependencies
*   **Reads/Writes**: Writes to `actions` and `action_steps` tables.
*   **Foreign Keys**: Relates to `qibits` via `source_qibit_id`, and `threads` via `thread_id`.
*   **Links**: Integrates with `people`, `money`, and `documents` tables via the central `links` schema.
