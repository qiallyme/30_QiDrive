---
layout: page
title: Index.architecture
slug: index-architecture
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
uid: 9b224a18815c4785894ba70e8c8bc8df
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Architecture Overview

QiFinance uses a simple web app architecture with a durable accounting model underneath.

## Layers

```text
UI
  ↓
State / Forms
  ↓
Domain Services
  ↓
Ledger Validation
  ↓
Supabase/Postgres
```
