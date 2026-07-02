---
layout: page
title: Event Vs Consequence
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

# Event vs Consequence Model

## Purpose

QiFinance separates what happened in the real world from how that event affects the books.

This protects the user from accounting complexity while preserving double-entry rigor under the hood.

## Definitions

### Event

An event is the real-world thing the user understands.

Examples:

- "I spent $100 at Target."
- "Lyft deposited $420."
- "I sent Mom $50 on Venmo."
- "I paid the Jeep loan."
- "I bought gas and snacks in one purchase."

Events are human-facing.

### Consequence

A consequence is the accounting effect generated from the event.

Examples:

- debit vehicle fuel expense
- debit personal snacks expense
- credit checking account
- debit cash
- credit Lyft income
- credit tips income
- reduce loan liability
- record interest expense

Consequences are system-facing.

## Example: Split Income Deposit

Event:

> Lyft deposited $100 into checking.

Consequences:

| Account | Debit | Credit |
|---|---:|---:|
| Checking | $100 | |
| Lyft Ride Income | | $80 |
| Tips Income | | $20 |

The user sees one deposit with a split. The ledger stores balanced consequences.

## Example: Mixed Target Purchase

Event:

> User spent $100 at Target.

User split:

- $60 groceries
- $40 clothing for business photo shoot

Consequences:

| Account | Debit | Credit |
|---|---:|---:|
| Personal Groceries Expense | $60 | |
| Business Wardrobe / Marketing Expense | $40 | |
| Checking | | $100 |

Tags may include:

- `tax_review`
- `business_use`
- `photo_shoot`

## Design Rule

The user should never be forced to manually think in debits and credits for ordinary workflows.

The app captures the event. The engine creates the consequences.

## Implementation Rule

Every confirmed transaction must be able to trace:

`event -> split lines -> ledger entries -> evidence -> explanation`
