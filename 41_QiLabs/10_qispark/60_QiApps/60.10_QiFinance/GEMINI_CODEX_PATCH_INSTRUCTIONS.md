---
layout: page
title: Gemini Codex Patch Instructions
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

# QiFinance Docs Patch Instructions for Gemini / Codex

## Purpose

This patch updates the QiFinance documentation with concepts from the latest critique.

When scaffolding or reviewing the app, treat these files as source-of-truth additions.

## New Source Files

- `docs/00_doctrine/single_financial_universe.md`
- `docs/03_domain/event_vs_consequence.md`
- `docs/05_data/import_staging_pipeline.md`
- `docs/08_ai/ai_policy_ingestion_vs_intelligence.md`
- `docs/07_ui/views_counterparty_accountability.md`
- `docs/10_history/patch_001_single_financial_universe.md`

## Required App Skeleton Impact

Add or reserve stubs for:

### Domain / Types

- Event-facing transaction model
- Consequence-facing ledger entry model
- Transaction split model
- Counterparty model
- Accountability / obligation model
- Import batch model
- Staged import item model
- Evidence link model
- AI suggestion metadata

### Routes

- `/dashboard`
- `/accounts`
- `/transactions`
- `/transactions/new`
- `/imports`
- `/imports/review`
- `/counterparties`
- `/counterparties/:id`
- `/accountability`
- `/reports`
- `/settings`

### Services

- `transactionsService`
- `ledgerService`
- `splitsService`
- `importsService`
- `normalizationService`
- `dedupeService`
- `counterpartiesService`
- `accountabilityService`
- `evidenceService`
- `aiSuggestionsService`

## Hard Rules

1. Imports do not write directly to confirmed ledger.
2. AI suggestions do not become ledger truth automatically.
3. Personal and business records stay in one financial universe.
4. Separation happens through metadata, tags, accounts, views, and reports.
5. User-facing UI should avoid debit/credit language unless in advanced/accounting views.
6. Every transaction must be traceable to source/evidence/explanation when available.
7. Build single-user first, but keep workspace/user ownership fields in core models.

## Do Not Build Yet

- full auth
- bank-feed integrations
- Stripe/payment processing
- full tax preparation
- payroll
- inventory
- ERP features
- user-facing AI chat

Keep these as future architecture considerations only.
