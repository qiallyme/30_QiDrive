---
title: "QiCode Governance"
aliases:
  - "QiCode Document Governance"
system: "QiOS"
document_type: "governance-standard"
status: "working-canonical"
version: "1.0"
canonical: true
updated: "2026-07-18"
source:
  - "QiCode Documentation database"
  - "QiLife Data Model Spine"
tags:
  - "qicode"
  - "governance"
  - "standards"
---
> **Parent:** [[00 - QiCode Home|QiCode Home]]
> **Related:** [[QiCode Registry|Registry]] · [[QiCode Numbering Standard|Numbering Standard]]

# QiCode Governance

## § 00.02.004 — Status Labels

| Status | Meaning |
| --- | --- |
| `active-doctrine` | Current authoritative doctrine |
| `working-canonical` | Current organizing standard pending formal ratification |
| `outline-only` | Registered topic without approved body content |
| `reference` | Points to a canonical section elsewhere |
| `deferred` | Intentionally excluded from the current implementation scope |
| `experimental` | Under evaluation; not active doctrine |
| `quarantined` | Isolated because placement or authority is unresolved |
| `superseded` | Replaced by a named newer record |
| `archived` | Retained for history; no longer active |

## § 02.01.001 — Decision Records

A decision record is required when a change alters section identity, authority, scope, placement, or compatibility.

At minimum, record:

- the decision;
- the reason;
- the affected sections or documents;
- the migration impact; and
- the effective version or date.

## § 02.01.002 — Standards

Standards define repeatable operating rules. They must have a named scope, status, version, and canonical file.

Indexes and registries may summarize a standard but must not duplicate its full body.

## § 02.01.005 — Versioning

- Use versions to identify meaningful document states, not every minor wording edit.
- A superseding version must identify what it replaces.
- Preserve old versions when needed for migration, evidence, or historical reconstruction.

## § 02.02.001 — Change Requests

A structural change should identify:

1. the requested outcome;
2. the sections or files affected;
3. whether numbers or links change;
4. whether migration is required; and
5. the proposed canonical destination.

## § 02.02.002 — Migration Rules

When moving, splitting, merging, or renumbering content:

- update the canonical document;
- update the registry;
- update affected links;
- preserve prior identifiers when they may still be cited; and
- record the mapping in migration notes.

## § 02.02.003 — Deprecation Rules

Deprecation means the item remains identifiable but should no longer be used for new work.

A deprecated item must state its replacement or explain that no replacement exists.

## § 02.02.004 — Supersession

A superseded document or section is replaced by a named newer authority. The older item remains in archive and must link forward to its replacement when practical.

## § 02.02.005 — Review Cycle

Review the registry whenever a canonical document is split, renamed, promoted, superseded, or archived.

Validation should confirm that:

- each active section has one registry entry;
- each active section points to one existing canonical file;
- section IDs remain unique; and
- internal links resolve.

## § 02.02.006 — Versioning & Continuity

Raw exports and source compilations are preserved separately from cleaned or reconciled documents.

A rewritten document must never be represented as untouched source material. Archive instead of deleting material that may matter for continuity or proof.

## § 02.02.007 — Updates & Ratification

Working standards remain clearly labeled until ratified. Ratification changes status; it does not require copying the same body into another document.

Promotion from outline, experiment, archive, or quarantine requires deliberate review and placement in an active canonical document.
