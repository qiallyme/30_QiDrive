---
layout: page
title: Transaction.contract
slug: transaction-contract
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
uid: b874c867d1404fb2844c915f2263d5b4
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Transaction Contract

## Create Transaction Payload

```json
{
  "date": "2026-06-30",
  "description": "Lyft deposit",
  "splits": [
    { "account": "Checking", "debit": 100, "credit": 0 },
    { "account": "Lyft Income", "debit": 0, "credit": 80 },
    { "account": "Tips Income", "debit": 0, "credit": 20 }
  ]
}
```

## Rule

Debits must equal credits before save.
