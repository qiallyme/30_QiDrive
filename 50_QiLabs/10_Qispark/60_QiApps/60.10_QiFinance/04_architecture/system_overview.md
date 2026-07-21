---
layout: page
title: System Overview
slug: system-overview
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
uid: dccb818627264b3a859990ac33effacd
canonical_ref: ""
source_type: manual
template_key: master-template
---

# System Overview

## Primary Flow

1. User creates or imports a transaction.
2. App builds split lines.
3. Ledger validator checks balance.
4. Data is saved to Supabase.
5. Dashboard and reports derive from splits.

## Design Intent

Reports should not rely on duplicated summary data unless cached. The ledger is the truth.
