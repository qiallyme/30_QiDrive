---
layout: page
title: Index.architecture
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
