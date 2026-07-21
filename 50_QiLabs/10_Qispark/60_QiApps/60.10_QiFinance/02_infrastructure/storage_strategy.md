---
layout: page
title: Storage Strategy
slug: storage-strategy
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
uid: 9c5cb90a1f07439d875a45a617beb7ea
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Storage Strategy

## Source of Truth

Supabase Postgres.

## Future File Storage

Supabase Storage for:

- Receipts
- Statements
- CSV imports
- Export bundles

## Local Storage

Use only for UI preferences or temporary draft state, never source-of-truth financial records.
