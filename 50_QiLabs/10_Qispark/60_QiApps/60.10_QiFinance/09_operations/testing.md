---
layout: page
title: Testing
slug: testing
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
uid: 6462b86f2e554d14bb158bb4b7d4d1a8
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
