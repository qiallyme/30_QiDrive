---
layout: page
title: Ai Policy Ingestion Vs Intelligence
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

# AI Policy: Ingestion Assistance vs Intelligence Layer

## Purpose

QiFinance should use AI carefully without allowing AI to corrupt the ledger.

The system distinguishes between two different AI roles:

1. AI-assisted ingestion
2. User-facing financial intelligence

These are not the same thing.

## Core Rule

AI may suggest, classify, normalize, summarize, and explain.

AI may not become the source of ledger truth.

## Role 1: AI-Assisted Ingestion

AI may be used early in the import pipeline to reduce manual cleanup.

Allowed uses:

- normalize messy merchant names
- suggest counterparties
- suggest categories
- suggest tags
- identify likely duplicates
- parse receipt text
- extract statement lines
- summarize source documents
- propose explanations

Example:

Raw bank text:

```text
TST* SQ TARGET 0093847 INDIANAPOLIS IN
```

AI suggestion:

```text
Counterparty: Target
Likely type: retail purchase
Possible tags: household, groceries, personal, tax_review if user indicates business use
```

This is a suggestion. It is not ledger truth.

## Role 2: User-Facing Intelligence Layer

User-facing AI comes later, after the structured data model works.

Allowed future questions:

- "Where did my money go last month?"
- "How much did I spend on vehicle repairs for Lyft?"
- "Who owes me money?"
- "Which expenses need receipts before tax time?"
- "What changed compared to last month?"

## Non-Negotiable Ledger Rule

The app must remain useful if AI is unavailable.

Core capabilities must work without AI:

- accounts
- transactions
- splits
- ledger math
- evidence attachment
- reports
- views
- export

## Safety Rule

AI must not:

- invent transactions
- modify confirmed ledger entries without user action
- silently change amounts
- silently delete records
- mark disputed facts as proven
- replace deterministic accounting math

## Practical Build Guidance

Use AI as an internal accelerator during ingestion, but keep AI outside the core ledger engine.

The ledger is math. AI is assistance.
