---
layout: page
title: Import Staging Pipeline
slug: import-staging-pipeline
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
uid: 0bc77a961dfb444cbe3a420dfdd52241
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Import Staging Pipeline

## Purpose

QiFinance must import aggressively without corrupting the ledger.

The system should support CSV, OFX/QFX, PDF statements, screenshots, receipt photos, manual entries, and eventually bank feeds. But imported data must never write directly into confirmed transactions or ledger entries.

## Hard Rule

Imports enter staging first.

No imported row, receipt, statement line, OCR result, or bank-feed item becomes ledger truth until it has passed through normalization, duplicate review, and confirmation.

## Required Flow

```text
source
  -> raw_import_batch
  -> staged_import_item
  -> normalization
  -> duplicate_detection
  -> user/system review
  -> confirmed transaction
  -> transaction splits
  -> ledger entries
  -> evidence links
  -> reports/views
```

## Source Types

Supported or planned source types:

- manual entry
- bank CSV
- credit card CSV
- OFX/QFX
- PDF statement
- receipt photo
- screenshot
- email receipt
- live bank API later

## Staging Item Fields

A staged item should preserve raw source data and normalized suggestions.

Suggested fields:

- `id`
- `workspace_id`
- `source_batch_id`
- `source_type`
- `raw_description`
- `raw_amount`
- `raw_date`
- `raw_counterparty`
- `normalized_description`
- `normalized_counterparty_id`
- `suggested_account_id`
- `suggested_category_id`
- `suggested_tags`
- `possible_duplicate_transaction_ids`
- `confidence_score`
- `review_status`
- `created_at`
- `updated_at`

## Duplicate Detection

Duplicate detection should consider:

- date proximity
- amount match
- account match
- merchant/counterparty similarity
- source priority
- pending vs posted status
- receipt evidence already attached
- manual entry overlap

## User Experience Rule

The user should not be punished for importing the same financial fact from multiple sources.

Example:

- bank feed pending item
- later posted CSV row
- receipt photo

These may all describe the same event. The system should merge or link them rather than create duplicate confirmed transactions.

## Ledger Protection Rule

The ledger only accepts confirmed transactions.

The import pipeline may be messy. The ledger must stay clean.
