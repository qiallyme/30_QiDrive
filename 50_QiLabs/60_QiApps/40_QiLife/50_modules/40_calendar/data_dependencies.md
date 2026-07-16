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
uid: da061adcbe8e4265845872342998da92
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Calendar: Data Dependencies
*   **Reads**: Queries `actions` where `scheduled_for` is not null, `obligations` with due dates, and `events`.
*   **Writes**: Updates `scheduled_for` or `due_date` on `actions` and `obligations`.
