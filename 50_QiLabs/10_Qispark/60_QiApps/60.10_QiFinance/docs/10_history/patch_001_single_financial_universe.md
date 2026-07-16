---
layout: page
title: Patch 001 Single Financial Universe
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

# Patch 001: Single Financial Universe Critique Integration

## Date

2026-06-30

## Reason

A critique of the QiFinance doctrine confirmed the direction and surfaced several concepts that should be made explicit before scaffolding the app.

## Added Concepts

### 1. Single Financial Universe

QiFinance should treat personal, gig, business, family, and obligation-related money as one economic life.

Personal/business separation happens through views, accounts, tags, classifications, and reports — not separate databases.

### 2. Event vs Consequence

The user records the real-world event. The system generates accounting consequences.

This keeps the UX simple while preserving double-entry rigor.

### 3. Import Staging Pipeline

Imports must never write directly to the confirmed ledger.

All imported data moves through staging, normalization, deduplication, and confirmation.

### 4. AI Policy Clarification

AI may assist with ingestion early but should not control ledger truth.

User-facing financial intelligence comes later after the structured data is reliable.

### 5. Counterparty and Accountability Views

QiFinance should treat counterparties and obligations as first-class views.

The app must answer not only "where did money go?" but also "who was involved?" and "who owes whom?"

## Implementation Effect

Gemini/Codex scaffolding should include stubs for:

- import staging
- normalization suggestions
- duplicate review
- counterparty routes
- accountability routes
- event/consequence transaction model
- AI suggestion boundaries

## Non-Change

The ledger remains the source of truth.

AI does not own accounting math.
