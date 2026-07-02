---
layout: page
title: Business Rules
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

# Business Rules

## Ledger Rules

1. Every transaction must balance.
2. Every transaction must have at least two split lines.
3. Debits must equal credits.
4. Transfers are not income.
5. Credit card payments are not expenses by themselves.
6. Loan payments may split into principal and interest.
7. Mixed transactions must support multiple categories/accounts.

## User Rules

1. The user may mark a classification as confirmed.
2. AI suggestions are not final until accepted.
3. Imported data should retain source metadata.
4. Deleted records should prefer soft-delete where practical.
