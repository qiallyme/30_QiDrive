---
layout: page
title: Relationships
slug: relationships
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
uid: ec2454195a8e4513ab9f7a1431e63576
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Relationships

```text
Workspace
  └── Users
  └── Accounts
  └── Transactions
        └── Splits
              └── Account
        └── Payee
        └── Attachments
  └── Rules
```

## Notes

- Transactions belong to a workspace.
- Splits belong to a transaction.
- Splits point to accounts.
- Reports are derived from transactions and splits.
