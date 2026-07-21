# QiLife Deferred Finance Bridge

Notes: Merged deferred transactions and obligations doctrine for future QiFinance bridge.
QiCode: § 05.02.006
Sort Key: 05.02.006
Status: active
Tags: Core, Registry/Archive
Type: Reference
Version: Reconciled V1

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Deferred  

**Version:** Reconciled V1

## Deferred / Not Core V1

```
transactions
obligations
```

These are not deleted from the concept. They are demoted.

They belong to a later **QiFinance** module or bridge.

QiLife may still capture financial or obligation-related information as QiBits using:

- `transaction_seed`
- `obligation_seed`
- `receipt`
- `payment_note`
- `bill_note`
- `money_issue`

But the specialized finance tables should not be part of QiLife core V1.

## Deferred: `transactions`

Transactions are not QiLife core V1.

They belong to a later QiFinance module or bridge.

QiLife may capture transaction-related seeds as QiBits.

### Deferred Table Sketch

```
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

### Rule

Do not build this into QiLife core until there is a clear reason.

For now, use finance app exports, documents, QiBits, and links.

## Deferred: `obligations`

Obligations are not QiLife core V1.

They belong to a later QiFinance / legal / agreements module if needed.

QiLife may capture obligation-related seeds as QiBits or actions.

### Deferred Table Sketch

```
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

### Statuses

```
open
partial
waiting_on
resolved
disputed
archived
```

### Rule

If it is just “someone owes something,” capture it as a QiBit or Action first.

Create a full obligations table only when tracking becomes too frequent or too important to handle through QiBits, actions, threads, and links.