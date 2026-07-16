---
layout: page
title: Data Dependencies
slug: ""
summary: ""
status: publish
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

# Calendar: Data Dependencies
*   **Reads**: Queries `actions` where `scheduled_for` is not null, `obligations` with due dates, and `events`.
*   **Writes**: Updates `scheduled_for` or `due_date` on `actions` and `obligations`.
