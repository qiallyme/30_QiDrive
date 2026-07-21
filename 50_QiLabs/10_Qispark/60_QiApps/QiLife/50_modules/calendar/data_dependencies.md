---
layout: page
title: Calendar: Data Dependencies
slug: calendar-data-dependencies
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
uid: d91412eda59046d5b77899e233ecedfe
canonical_ref: ""
template_key: master-template
---

# Calendar: Data Dependencies
*   **Reads**: Queries `actions` where `scheduled_for` is not null, `obligations` with due dates, and `events`.
*   **Writes**: Updates `scheduled_for` or `due_date` on `actions` and `obligations`.
