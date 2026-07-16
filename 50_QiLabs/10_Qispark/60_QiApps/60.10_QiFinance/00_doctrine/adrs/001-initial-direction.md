---
layout: page
title: 001 Initial Direction
slug: 001-initial-direction
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
uid: 8fa5fffc839b41148f9ca93d41bff9f6
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
