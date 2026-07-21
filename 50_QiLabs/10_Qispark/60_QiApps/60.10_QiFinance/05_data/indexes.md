---
layout: page
title: Indexes
slug: indexes
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
uid: c1b682c868f8481aa4af5f5052d703a7
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Indexes

## Expected Indexes

- transactions.workspace_id
- transactions.date
- transaction_splits.transaction_id
- transaction_splits.account_id
- accounts.workspace_id
- payees.workspace_id

## Later

Indexes for import deduplication and search.
