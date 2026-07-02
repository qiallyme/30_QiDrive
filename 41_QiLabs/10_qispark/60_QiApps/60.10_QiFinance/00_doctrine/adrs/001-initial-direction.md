---
layout: page
title: 001 Initial Direction
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

# ADR 001: Initial Product Direction

## Status

Accepted

## Context

QiFinance began from the real problem of tracking money during financial instability, gig work, vehicle expenses, mixed personal/business spending, debt, and emergency cash flow.

## Decision

Build QiFinance as a double-entry-backed personal and gig-worker finance system with a simple UI.

## Consequences

- More complex data model than a simple budget app
- Better long-term correctness
- Supports splits, transfers, income breakdowns, debts, and reports
- Requires careful UX to hide accounting complexity
