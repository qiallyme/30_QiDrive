---
layout: page
title: Core Principles
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

# Core Principles

## 1. Double-Entry Under the Hood

Users should not need to understand debits and credits, but the system must.

Every transaction should be structurally capable of balanced split lines.

## 2. Mixed Money Is Normal

The app must assume that personal and business finances overlap.

A single transaction may include:

- Business expense
- Personal expense
- Transfer
- Tip income
- Platform income
- Reimbursement
- Debt payment
- Tax-related amount

## 3. Splits Are First-Class

Splits are not an advanced feature. They are the core transaction model.

Example:

```text
Dr Cash - Checking              100.00
    Cr Income - Lyft Rides       80.00
    Cr Income - Tips             20.00
```

## 4. Infrastructure Before Schema

Do not design isolated Cody-only tables.

Design for:

- Single user now
- Friend testing soon
- Auth later
- Workspace ownership always

## 5. Explain the Why

Every major folder and decision needs a `.why` note.

The future maintainer is probably Cody, tired, annoyed, and asking why something exists.

## 6. Source of Truth Matters

The app must distinguish:

- User-entered data
- Imported data
- System-generated data
- AI-suggested data
- Confirmed data
- Disputed data

## 7. No Financial Gaslighting

The app should help users understand that money passing through their account is not the same as available money.

## 8. Build for Survival First

The MVP should prioritize cash reality, runway, debts, bills, and work-related expense clarity before fancy reports.
