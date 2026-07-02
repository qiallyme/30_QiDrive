---
layout: page
title: Testing
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

# Testing Strategy

## MVP Tests

- Transaction balances
- Split validation
- Account totals
- Dashboard calculations
- Import parsing later

## Manual Smoke Test

Create a Lyft deposit split:

```text
Dr Checking 100
Cr Lyft Income 80
Cr Tips Income 20
```

Confirm dashboard reflects income and cash correctly.
