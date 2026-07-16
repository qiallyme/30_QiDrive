---
layout: page
title: Workflows
slug: ""
summary: ""
status: publish
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

# Business Workflows

## Manual Transaction Entry

Actor: User

Trigger: User wants to record money movement.

Steps:

1. Choose date.
2. Choose account affected.
3. Enter amount and description.
4. Add split lines.
5. Validate balance.
6. Save transaction.

Output: Balanced transaction with split lines.

## Gig Income Deposit Split

Actor: User

Trigger: Platform deposit arrives.

Example:

```text
Dr Checking                     100.00
    Cr Lyft Ride Income          80.00
    Cr Tips Income               20.00
```

Output: Income correctly separated by source.

## Mixed Expense Split

Actor: User

Trigger: One purchase includes business and personal items.

Example:

```text
Dr Vehicle Fuel Expense          40.00
Dr Personal Food Expense         10.00
    Cr Checking                  50.00
```

Output: One real-world purchase separated into useful categories.
