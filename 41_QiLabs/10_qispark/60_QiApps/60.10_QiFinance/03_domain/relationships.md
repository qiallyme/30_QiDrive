---
layout: page
title: Relationships
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
