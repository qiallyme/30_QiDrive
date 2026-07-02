---
layout: page
title: Calendar: Data Dependencies
slug: calendar-data-dependencies
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

# Calendar: Data Dependencies
*   **Reads**: Queries `actions` where `scheduled_for` is not null, `obligations` with due dates, and `events`.
*   **Writes**: Updates `scheduled_for` or `due_date` on `actions` and `obligations`.
