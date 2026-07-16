---
layout: page
title: Event Flows
slug: event-flows
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
uid: eacc41c665d44bc7a906d5c2df7e6181
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Event Flows

## Save Transaction

```text
User submits form
  → validate required fields
  → validate split balance
  → insert transaction
  → insert split lines
  → refresh dashboard/reports
```

## Import CSV

```text
Upload CSV
  → parse rows
  → map fields
  → create draft transactions
  → user reviews
  → confirm/save
```
