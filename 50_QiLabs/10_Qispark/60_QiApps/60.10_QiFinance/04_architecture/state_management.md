---
layout: page
title: State Management
slug: state-management
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
uid: d699ffdbf926424ebd82b2cceb17a4b8
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
