---
layout: page
title: Event Flows
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
