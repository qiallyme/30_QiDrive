---
layout: page
title: State Management
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

# State Management

## MVP Recommendation

Keep state simple:

- Server data from Supabase queries
- Local form state for transaction entry
- Derived dashboard values from query results

## Avoid

- Global state bloat
- Duplicating ledger totals in multiple places
- Making UI state the financial source of truth
