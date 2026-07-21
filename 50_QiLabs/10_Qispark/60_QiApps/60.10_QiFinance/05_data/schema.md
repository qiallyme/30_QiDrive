---
layout: page
title: Schema
slug: schema
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
uid: 4088c81456e944489bad030c0b764c8b
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Schema Draft

## Guiding Rule

Every transaction is composed of split lines. Splits are the source of truth for reporting.

## Draft: transactions

```text
id
workspace_id
date
description
payee_id
status
source
memo
created_at
updated_at
created_by
```

## Draft: transaction_splits

```text
id
workspace_id
transaction_id
account_id
debit_amount
credit_amount
memo
line_order
created_at
updated_at
```

## Draft: accounts

```text
id
workspace_id
name
account_type
normal_balance
parent_account_id
is_active
created_at
updated_at
```

## Account Types

- asset
- liability
- equity
- income
- expense
