---
layout: page
title: Indexes
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
