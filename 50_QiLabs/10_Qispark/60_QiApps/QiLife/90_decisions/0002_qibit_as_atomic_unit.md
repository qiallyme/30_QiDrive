---
layout: adr
title: ADR 0002: QiBit as the Atomic Unit
slug: adr-0002-qibit-as-the-atomic-unit
status: publish
updated_at: "2026-07-16T06:49:40-04:00"
tags: []
  - qispark
  - decisions
source_type: manual
summary: ""
created_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 6cb35e9465f54ecfbc782f49ee42298b
canonical_ref: ""
template_key: master-template
---

# ADR 0002: QiBit as the Atomic Unit

## Status

Accepted

---

## Context

User inputs vary drastically in format (a text message, a scan of a legal notice, a voice memo, a transaction log). Attempting to immediately force these into rigid schemas (like forcing a vague text "Zai gas $40" directly into a double-entry accounting ledger or a calendar deadline) leads to capture friction. People stop capturing items if the entry form is too demanding.

---

## Decision

We will establish the **QiBit** as the atomic unit of all data within **QiLife**.
*   Every capture action creates a QiBit first.
*   A QiBit contains a `raw_capture` field to preserve the exact raw input text, and metadata tracking when and how it was captured.
*   All structured operational records (Actions, Obligations, Transactions, Documents) must link back to a parent QiBit to preserve historical provenance.

---

## Consequences

*   **Zero-Friction Ingestion**: Cody can capture thoughts or logs in a single input field.
*   **Staged Structure**: Separation of capture from organization. AI or manual triage processes run asynchronously or semi-synchronously to unpack the QiBit into structured tables without blocking ingestion.
*   **Provenance Retention**: Clicking on any Action or Transaction allows Cody to trace it back to the exact raw text or situation that triggered it.
