---
title: "QiLife Deferred Finance Bridge"
aliases:
  - "QiLife Finance Bridge"
system: "QiOS"
document_type: "deferred-specification"
status: "deferred"
version: "1.0"
canonical: true
updated: "2026-07-18"
source:
  - "QiCode Documentation database"
  - "QiLife Data Model Spine"
tags:
  - "qicode"
  - "qios"
  - "qilife"
---
> **Parent:** [[00 - QiCode Home|QiCode Home]]
> **Related:** [[QiLife Doctrine|Doctrine]] · [[QiLife Data Model|Data Model]] · [[QiLife Workflows|Workflows]]

# QiLife Deferred Finance Bridge

> **Title:** 06 — QiLife  
> **Chapter:** 06.06 — Deferred Finance Bridge

This document preserves deferred finance concepts without making them part of QiLife core V1.

## § 06.06.001 — Boundary

Specialized finance tables are not part of QiLife core V1. They belong to a later **QiFinance** module or bridge.

QiLife may still capture financial or obligation-related information as QiBits, including:

- `transaction_seed`;
- `obligation_seed`;
- `receipt`;
- `payment_note`;
- `bill_note`; and
- `money_issue`.

The last three values are descriptive capture patterns unless later added to the canonical `qibit_type` registry.

## § 06.06.002 — Deferred Transactions

Transactions are not part of QiLife core V1. QiLife may capture transaction-related seeds as QiBits and connect them to documents, actions, or threads.

##### Deferred Table Sketch

```text
transactions
├── id
├── date
├── amount_cents
├── currency
├── direction
├── from_label
├── to_label
├── category
├── bucket_key
├── thread_id
├── status
├── notes
├── evidence_document_id
├── source_qibit_id
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

Do not build this table into QiLife core until a clear operational need exists. Until then, use QiFinance exports, documents, QiBits, and links.

## § 06.06.003 — Deferred Obligations

Obligations are not part of QiLife core V1. They may later belong to QiFinance, legal, or agreement-specific modules.

##### Deferred Table Sketch

```text
obligations
├── id
├── owed_by_label
├── owed_to_label
├── obligation_type
├── amount_cents
├── currency
├── reason
├── status
├── due_date
├── related_transaction_id
├── source_qibit_id
├── created_at
├── updated_at
├── resolved_at
├── archived_at
└── deleted_at
```

##### Deferred Obligation Statuses

```text
open
partial
waiting_on
resolved
disputed
archived
```

If the requirement is only “someone owes something,” capture it first as a QiBit or action. Create a dedicated obligations table only when the volume or importance cannot be handled through QiBits, actions, threads, and links.

---
