---
layout: page
title: Data Dependencies
slug: data-dependencies
summary: ""
status: publish
created_at: "2026-07-16T06:19:39-04:00"
updated_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 6bdf9574291f479bab81b6bd6c292e5f
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Actions: Data Dependencies
*   **Reads/Writes**: Writes to `actions` and `action_steps` tables.
*   **Foreign Keys**: Relates to `qibits` via `source_qibit_id`, and `threads` via `thread_id`.
*   **Links**: Integrates with `people`, `money`, and `documents` tables via the central `links` schema.
