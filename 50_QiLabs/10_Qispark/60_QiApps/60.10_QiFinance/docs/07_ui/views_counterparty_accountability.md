---
layout: page
title: Views Counterparty Accountability
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

# Counterparty and Accountability Views

## Purpose

QiFinance should let users view money through relationships and obligations, not only accounts and categories.

Most financial apps answer:

- What account changed?
- What category was used?

QiFinance must also answer:

- Who was involved?
- Who owes whom?
- What is still unresolved?
- What can be proven?

## Counterparty View

A counterparty is the person, company, institution, platform, or entity on the other side of a financial event.

Examples:

- Lyft
- Uber
- DoorDash
- Chase
- Mom
- Zion
- landlord
- client
- mechanic
- Apple
- Target

### Counterparty View Should Show

For a selected counterparty:

- all related transactions
- total money in
- total money out
- open obligations
- attached evidence
- notes/explanations
- disputed items
- related tags
- related accounts

### Example

Selecting `Mom` should show:

- Venmo transfers sent
- checks received
- reimbursements owed
- loans or IOUs
- caregiving-related expenses
- disputed claims
- evidence screenshots or notes

## Accountability View

The accountability view tracks obligations and unresolved financial responsibility.

It answers:

- Who owes me?
- Who do I owe?
- What money is pending reimbursement?
- What expenses need proof?
- What transactions are disputed?
- What obligations are recurring or upcoming?

## Accountability Categories

Suggested statuses:

- `owed_to_me`
- `i_owe`
- `reimbursable`
- `pending_reimbursement`
- `disputed`
- `needs_evidence`
- `needs_explanation`
- `resolved`
- `written_off`

## UI Rule

These views should be first-class navigation items, not hidden advanced filters.

Suggested routes:

```text
/counterparties
/counterparties/:id
/accountability
/accountability/disputed
/accountability/reimbursements
/accountability/evidence-needed
```

## Why This Matters

Many users do not only need budgeting. They need memory, proof, and relationship-level accountability.

This is especially important for:

- gig workers
- family caregivers
- freelancers
- roommates
- shared vehicles
- informal loans
- reimbursement-heavy work
- mixed personal/business lives
