---
layout: page
title: Post Transactions
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
