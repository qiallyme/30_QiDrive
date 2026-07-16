---
layout: page
title: Post Transactions
slug: post-transactions
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
uid: d1223a98b1984de6a0a6c92cc2d5ba9f
canonical_ref: ""
source_type: manual
template_key: master-template
---

# POST /transactions

## Purpose

Create a balanced transaction with split lines.

## Validation

- Workspace required
- Date required
- At least two split lines
- Total debits equal total credits

## Failure Cases

- Unbalanced transaction
- Missing account
- Unauthorized workspace
