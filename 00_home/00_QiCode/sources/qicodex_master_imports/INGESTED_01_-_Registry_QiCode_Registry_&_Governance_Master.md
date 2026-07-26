# QiCode Registry & Governance Master

> **Master Registry, Numbering Standards & Package Manifest for QiOS**

## QiCode Governance

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

---

## QiCode Numbering Standard

---
title: "QiCode Numbering Standard"
aliases:
  - "QiDecimal Numbering Standard"
  - "QiCode Section Standard"
system: "QiOS"
document_type: "standard"
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
  - "numbering"
---
> **Parent:** [[00 - QiCode Home|QiCode Home]]
> **Related:** [[QiCode Registry|Registry]] · [[QiCode Governance|Governance]]

# QiCode Numbering Standard

## § 00.01.001 — Purpose

This standard gives every QiCode doctrine, standard, and registered topic a stable identifier and a single canonical location.

## § 00.01.002 — Scope

It governs titles, chapters, sections, registry entries, citations, renumbering, and file references within QiCode.

It does not define the substantive doctrine of every registered section.

## § 00.01.003 — Definitions

| Term | Meaning |
| --- | --- |
| **Title** | A two-digit top-level domain |
| **Chapter** | A two-digit subdivision within a title |
| **Section** | A three-digit registered unit within a chapter |
| **Registry** | The numbered map of sections, statuses, and canonical destinations |
| **Canonical document** | The one file containing the active body of a section |
| **Reference** | A link to a canonical section without duplicated body text |

## § 00.01.004 — Realm Structure

```text
Title TT
└── Chapter TT.CC
    └── Section TT.CC.SSS
```

Titles define domains. Chapters group related rules. Sections carry the registered doctrine, standard, reference, or placeholder.

## § 00.01.005 — Hierarchy & Authority

Authority descends in this order:

1. [[QiCode Registry|QiCode Registry]] for identity and placement;
2. the active canonical document named by the registry;
3. approved supporting standards and decision records;
4. implementation notes; and
5. archive, quarantine, and raw source material.

A section may be referenced from many places, but its active body must exist in one canonical document only.

## § 00.01.006 — QiDecimal System

QiCode sections use:

```text
TT.CC.SSS
```

| Element | Meaning | Format |
| --- | --- | --- |
| `TT` | Title | Two digits |
| `CC` | Chapter | Two digits |
| `SSS` | Section | Three digits |

Example: `06.03.002` means Title 06, Chapter 03, Section 002.

## § 00.01.007 — QiCodex Unified Decimal Registry

The registry records each section's:

- identifier;
- title;
- status; and
- canonical document or disposition.

The registry summarizes and links. It must not become a second copy of the doctrine.

## § 00.01.008 — Numbering Rules

- A chapter number such as `05.01` is a container and must not also be used as a section ID.
- Every active section ID must be unique.
- Add sections at the end of the correct chapter unless insertion is structurally necessary.
- Do not recycle identifiers from archived, deleted, or superseded sections.
- Status and file location are metadata; they are not encoded in the number.
- Titles `90` and `99` remain reserved for archive/quarantine and experimental work.
- Record renumbering in [[QiCode Migration Notes|QiCode Migration Notes]].

## § 00.01.009 — Citation Format

Use the section symbol and full identifier:

```text
§ 06.03.002 — QiBits
```

In Obsidian, cite the canonical document with a wikilink rather than copying its body.

## § 00.02.001 — Naming Rules

- Use readable names instead of database slugs.
- Use stable document names based on responsibility, not temporary implementation details.
- Use one term consistently after it is declared canonical.
- Mark renamed or replaced terms rather than silently reusing them with a different meaning.

## § 00.02.005 — File Conventions

- A document filename describes the document; it does not replace its QiCode section IDs.
- One focused document may contain several sections from the same responsibility area.
- Use full-path wikilinks inside this package to avoid ambiguity in larger vaults.
- Archive historical source files without editorial frontmatter when exact preservation matters.

---

## QiCode Package Manifest

---
title: "QiCode Package Manifest"
aliases:
  - "QiCode Manifest"
system: "QiOS"
document_type: "manifest"
status: "active-record"
version: "1.0"
canonical: false
updated: "2026-07-18"
source:
  - "Generated Obsidian package"
tags:
  - "qicode"
  - "manifest"
---
> **Parent:** [[00 - QiCode Home|QiCode Home]]

# QiCode Package Manifest

This package contains the following active and archival files:

- `00 - QiCode Home.md`
- `01 - Registry/QiCode Governance.md`
- `01 - Registry/QiCode Numbering Standard.md`
- `01 - Registry/QiCode Registry.md`
- `02 - QiLife/QiLife Architecture.md`
- `02 - QiLife/QiLife Data Model.md`
- `02 - QiLife/QiLife Deferred Finance Bridge.md`
- `02 - QiLife/QiLife Doctrine.md`
- `02 - QiLife/QiLife Product Surfaces.md`
- `02 - QiLife/QiLife Workflows.md`
- `90 - Archive/QiCode Migration Notes.md`
- `90 - Archive/QiLife App Spec - Legacy.md`
- `90 - Archive/Sources/QiCode Combined Cleaned Draft.md`
- `90 - Archive/Sources/QiCode Compiled Doctrine - Original.md`
- `README - Install.md`

---

## QiCode Registry

---
title: "QiCode Registry"
aliases:
  - "QiCode Master Index"
  - "QiDecimal Registry"
system: "QiOS"
document_type: "registry"
status: "working-canonical"
version: "1.0"
canonical: true
updated: "2026-07-18"
source:
  - "QiCode Documentation database"
  - "QiLife Data Model Spine"
tags:
  - "qicode"
  - "registry"
  - "qios"
---
> **Parent:** [[00 - QiCode Home|QiCode Home]]
> **Related:** [[QiCode Numbering Standard|Numbering Standard]] · [[QiCode Governance|Governance]]

# QiCode Registry

> [!info] Registry rule
> This document identifies sections and their status. It does not duplicate the full body of active doctrine.

## Status Key

- **Active doctrine** — authoritative body exists in the linked canonical document.
- **Working standard** — current organizing rule pending formal ratification.
- **Outline only** — registered heading with no approved body supplied.
- **Reference** — points to active doctrine located elsewhere.
- **Deferred** — preserved but excluded from current core scope.
- **Quarantined / Archived / Experimental** — not active doctrine.

## Title 00 — General Provisions

### Chapter 00.01 — QiEOS Protocol v2.0

- **§ 00.01.001 — Purpose** — `working-standard` — [[QiCode Numbering Standard|Numbering Standard]]
- **§ 00.01.002 — Scope** — `working-standard` — [[QiCode Numbering Standard|Numbering Standard]]
- **§ 00.01.003 — Definitions** — `working-standard` — [[QiCode Numbering Standard|Numbering Standard]]
- **§ 00.01.004 — Realm Structure** — `working-standard` — [[QiCode Numbering Standard|Numbering Standard]]
- **§ 00.01.005 — Hierarchy & Authority** — `working-standard` — [[QiCode Numbering Standard|Numbering Standard]]
- **§ 00.01.006 — QiDecimal System** — `working-standard` — [[QiCode Numbering Standard|Numbering Standard]]
- **§ 00.01.007 — QiCodex Unified Decimal Registry** — `working-standard` — [[QiCode Numbering Standard|Numbering Standard]]
- **§ 00.01.008 — Numbering Rules** — `working-standard` — [[QiCode Numbering Standard|Numbering Standard]]
- **§ 00.01.009 — Citation Format** — `working-standard` — [[QiCode Numbering Standard|Numbering Standard]]
- **§ 00.01.010 — Privacy & Sovereignty** — `outline-only` — —
### Chapter 00.02 — Naming, Status & File Conventions

- **§ 00.02.001 — Naming Rules** — `working-standard` — [[QiCode Numbering Standard|Numbering Standard]]
- **§ 00.02.002 — Canonical Terms** — `outline-only` — —
- **§ 00.02.003 — Retired Terms** — `outline-only` — —
- **§ 00.02.004 — Status Labels** — `working-standard` — [[QiCode Governance|QiCode Governance]]
- **§ 00.02.005 — File Conventions** — `working-standard` — [[QiCode Numbering Standard|Numbering Standard]]
## Title 01 — Doctrine & Principles

### Chapter 01.01 — Qi Doctrine & Principles

- **§ 01.01.001 — Core Doctrine** — `outline-only` — —
- **§ 01.01.002 — System Purpose** — `outline-only` — —
- **§ 01.01.003 — Founding Principles** — `outline-only` — —
- **§ 01.01.004 — Principle of Awareness** — `outline-only` — —
- **§ 01.01.005 — Principle of Presence** — `outline-only` — —
- **§ 01.01.006 — Modularity** — `outline-only` — —
- **§ 01.01.007 — Minimum Viable Structure** — `outline-only` — —
- **§ 01.01.008 — Human-First Operations** — `outline-only` — —
### Chapter 01.02 — Decision Rules

- **§ 01.02.001 — Merge Before Splitting** — `outline-only` — —
- **§ 01.02.002 — Properties Before New Tables** — `outline-only` — —
- **§ 01.02.003 — Folders Must Earn Existence** — `outline-only` — —
- **§ 01.02.004 — No Placeholder Architecture** — `outline-only` — —
- **§ 01.02.005 — Archive Instead of Deleting** — `outline-only` — —
## Title 02 — Governance & Standards

### Chapter 02.01 — Decisions, Standards & Templates

- **§ 02.01.001 — Decision Records** — `working-standard` — [[QiCode Governance|QiCode Governance]]
- **§ 02.01.002 — Standards** — `working-standard` — [[QiCode Governance|QiCode Governance]]
- **§ 02.01.003 — Templates** — `outline-only` — —
- **§ 02.01.004 — Forms** — `outline-only` — —
- **§ 02.01.005 — Versioning** — `working-standard` — [[QiCode Governance|QiCode Governance]]
### Chapter 02.02 — Change Control & Deprecation

- **§ 02.02.001 — Change Requests** — `working-standard` — [[QiCode Governance|QiCode Governance]]
- **§ 02.02.002 — Migration Rules** — `working-standard` — [[QiCode Governance|QiCode Governance]]
- **§ 02.02.003 — Deprecation Rules** — `working-standard` — [[QiCode Governance|QiCode Governance]]
- **§ 02.02.004 — Supersession** — `working-standard` — [[QiCode Governance|QiCode Governance]]
- **§ 02.02.005 — Review Cycle** — `working-standard` — [[QiCode Governance|QiCode Governance]]
- **§ 02.02.006 — Versioning & Continuity** — `working-standard` — [[QiCode Governance|QiCode Governance]]
- **§ 02.02.007 — Updates & Ratification** — `working-standard` — [[QiCode Governance|QiCode Governance]]
## Title 03 — System Architecture

### Chapter 03.01 — QiLabs Root Model

- **§ 03.01.001 — Canonical Root Structure** — `outline-only` — —
- **§ 03.01.002 — Workspace Layer** — `outline-only` — —
- **§ 03.01.003 — Docs Layer** — `outline-only` — —
- **§ 03.01.004 — Runtime Layer** — `outline-only` — —
- **§ 03.01.005 — Records Layer** — `outline-only` — —
- **§ 03.01.006 — Apps Layer** — `outline-only` — —
### Chapter 03.02 — QiSpark Documentation & Landing

- **§ 03.02.001 — QiSpark Scope** — `outline-only` — —
- **§ 03.02.002 — Docs Site Role** — `outline-only` — —
- **§ 03.02.003 — Landing Page Role** — `outline-only` — —
- **§ 03.02.004 — QiDNA Placement** — `outline-only` — —
- **§ 03.02.005 — Navigation Model** — `outline-only` — —
### Chapter 03.03 — QiServer Runtime & Cloudflare

- **§ 03.03.001 — QiServer Scope** — `outline-only` — —
- **§ 03.03.002 — Cockpit** — `outline-only` — —
- **§ 03.03.003 — Runtime Services** — `outline-only` — —
- **§ 03.03.004 — Cloudflare & Zero Trust** — `outline-only` — —
- **§ 03.03.005 — Backups, Secrets & Recovery** — `outline-only` — —
### Chapter 03.04 — QiDrive Records & Evidence

- **§ 03.04.001 — QiDrive Scope** — `outline-only` — —
- **§ 03.04.002 — Drive Mirror** — `outline-only` — —
- **§ 03.04.003 — Evidence Libraries** — `outline-only` — —
- **§ 03.04.004 — Retention** — `outline-only` — —
- **§ 03.04.005 — Export Bundles** — `outline-only` — —
### Chapter 03.05 — QiApps, Projects & Integrations

- **§ 03.05.001 — QiApps Scope** — `outline-only` — —
- **§ 03.05.002 — App Registry** — `outline-only` — —
- **§ 03.05.003 — Project Standards** — `outline-only` — —
- **§ 03.05.004 — Shared Components** — `outline-only` — —
- **§ 03.05.005 — External Integrations** — `outline-only` — —
- **§ 03.05.006 — QiLife Placement Reference** — `reference` — [[QiLife Architecture|QiLife Architecture]]
## Title 04 — Chronicle & Records

### Chapter 04.01 — Timeline, Journal & Chronicle

- **§ 04.01.001 — Chronicle Purpose** — `outline-only` — —
- **§ 04.01.002 — Timeline Events** — `outline-only` — —
- **§ 04.01.003 — Journal Entries** — `outline-only` — —
- **§ 04.01.004 — Daily Logs** — `outline-only` — —
- **§ 04.01.005 — Incident Logs** — `outline-only` — —
- **§ 04.01.006 — Relationship Notes** — `outline-only` — —
- **§ 04.01.007 — Decision Notes** — `outline-only` — —
- **§ 04.01.008 — Evidence Links** — `outline-only` — —
- **§ 04.01.009 — Review & Reconstruction** — `outline-only` — —
- **§ 04.01.010 — QiLife Chronicle Reference** — `reference` — [[QiLife Workflows|QiLife Workflows]]
### Chapter 04.02 — Records, Metadata & Links

- **§ 04.02.001 — Record Definition** — `outline-only` — —
- **§ 04.02.002 — Record Types** — `outline-only` — —
- **§ 04.02.003 — Metadata** — `outline-only` — —
- **§ 04.02.004 — Tags** — `outline-only` — —
- **§ 04.02.005 — Links & Relationships** — `outline-only` — —
- **§ 04.02.006 — QiLife Records Reference** — `reference` — [[QiLife Data Model|QiLife Data Model]]
### Chapter 04.03 — Evidence, Audit, Import & Export

- **§ 04.03.001 — Evidence Definition** — `outline-only` — —
- **§ 04.03.002 — Audit Trail** — `outline-only` — —
- **§ 04.03.003 — Retention Rules** — `outline-only` — —
- **§ 04.03.004 — Import Standard** — `outline-only` — —
- **§ 04.03.005 — Export Standard** — `outline-only` — —
- **§ 04.03.006 — QiLife Audit Reference** — `reference` — [[QiLife Data Model|QiLife Data Model]]
## Title 05 — Operations & Workflows

### Chapter 05.01 — QiAlly Delivery OS

- **§ 05.01.001 — Workflow Standard** — `outline-only` — —
- **§ 05.01.002 — SOP Standard** — `outline-only` — —
- **§ 05.01.003 — Routine Standard** — `outline-only` — —
- **§ 05.01.004 — Checklist Standard** — `outline-only` — —
- **§ 05.01.005 — Runbook Standard** — `outline-only` — —
- **§ 05.01.006 — QiLife Workflow Reference** — `reference` — [[QiLife Workflows|QiLife Workflows]]
### Chapter 05.02 — Maintenance, Incidents & Deployment

- **§ 05.02.001 — Maintenance** — `outline-only` — —
- **§ 05.02.002 — Incident Levels** — `outline-only` — —
- **§ 05.02.003 — Recovery Process** — `outline-only` — —
- **§ 05.02.004 — Deployment Process** — `outline-only` — —
- **§ 05.02.005 — Rollback Process** — `outline-only` — —
## Title 06 — QiLife

### Chapter 06.01 — Purpose, Boundaries & Scope

- **§ 06.01.001 — Purpose & Operating Doctrine** — `active-doctrine` — [[QiLife Doctrine|QiLife Doctrine]]
- **§ 06.01.002 — Core V1 Scope** — `active-doctrine` — [[QiLife Doctrine|QiLife Doctrine]]

### Chapter 06.02 — Architecture & Placement

- **§ 06.02.001 — Position in QiOS** — `active-doctrine` — [[QiLife Architecture|QiLife Architecture]]
- **§ 06.02.002 — Canonical Placement** — `active-doctrine` — [[QiLife Architecture|QiLife Architecture]]
- **§ 06.02.003 — Database Portability** — `active-doctrine` — [[QiLife Architecture|QiLife Architecture]]

### Chapter 06.03 — Core V1 Data Model

- **§ 06.03.001 — Core Tables** — `active-doctrine` — [[QiLife Data Model|QiLife Data Model]]
- **§ 06.03.002 — QiBits** — `active-doctrine` — [[QiLife Data Model|QiLife Data Model]]
- **§ 06.03.003 — Buckets** — `active-doctrine` — [[QiLife Data Model|QiLife Data Model]]
- **§ 06.03.004 — Threads** — `active-doctrine` — [[QiLife Data Model|QiLife Data Model]]
- **§ 06.03.005 — Actions & Action Steps** — `active-doctrine` — [[QiLife Data Model|QiLife Data Model]]
- **§ 06.03.006 — People** — `active-doctrine` — [[QiLife Data Model|QiLife Data Model]]
- **§ 06.03.007 — Events** — `active-doctrine` — [[QiLife Data Model|QiLife Data Model]]
- **§ 06.03.008 — Documents** — `active-doctrine` — [[QiLife Data Model|QiLife Data Model]]
- **§ 06.03.009 — Knowledge Items** — `active-doctrine` — [[QiLife Data Model|QiLife Data Model]]
- **§ 06.03.010 — Links** — `active-doctrine` — [[QiLife Data Model|QiLife Data Model]]
- **§ 06.03.011 — Activity Log** — `active-doctrine` — [[QiLife Data Model|QiLife Data Model]]
- **§ 06.03.012 — AI Outputs** — `active-doctrine` — [[QiLife Data Model|QiLife Data Model]]
- **§ 06.03.013 — Daily Summaries** — `active-doctrine` — [[QiLife Data Model|QiLife Data Model]]

### Chapter 06.04 — Views, Review & Build Order

- **§ 06.04.001 — Timeline Projection** — `active-doctrine` — [[QiLife Workflows|QiLife Workflows]]
- **§ 06.04.002 — Human-in-the-Loop Truth Layers** — `active-doctrine` — [[QiLife Workflows|QiLife Workflows]]
- **§ 06.04.003 — AI Review Queue** — `active-doctrine` — [[QiLife Workflows|QiLife Workflows]]
- **§ 06.04.004 — Build Order** — `active-doctrine` — [[QiLife Workflows|QiLife Workflows]]

### Chapter 06.05 — Product Surfaces

- **§ 06.05.001 — Inbox** — `outline-only` — [[QiLife Product Surfaces|QiLife Product Surfaces]]
- **§ 06.05.002 — Today** — `outline-only` — [[QiLife Product Surfaces|QiLife Product Surfaces]]
- **§ 06.05.003 — Calendar** — `outline-only` — [[QiLife Product Surfaces|QiLife Product Surfaces]]
- **§ 06.05.004 — Tasks** — `outline-only` — [[QiLife Product Surfaces|QiLife Product Surfaces]]
- **§ 06.05.005 — Activities** — `outline-only` — [[QiLife Product Surfaces|QiLife Product Surfaces]]
- **§ 06.05.006 — Routines** — `outline-only` — [[QiLife Product Surfaces|QiLife Product Surfaces]]
- **§ 06.05.007 — People & Relationships** — `outline-only` — [[QiLife Product Surfaces|QiLife Product Surfaces]]
- **§ 06.05.008 — Communication History** — `outline-only` — [[QiLife Product Surfaces|QiLife Product Surfaces]]
- **§ 06.05.009 — Projects & Workbench** — `outline-only` — [[QiLife Product Surfaces|QiLife Product Surfaces]]
- **§ 06.05.010 — Notes & Creative Work** — `outline-only` — [[QiLife Product Surfaces|QiLife Product Surfaces]]
- **§ 06.05.011 — Research** — `outline-only` — [[QiLife Product Surfaces|QiLife Product Surfaces]]
- **§ 06.05.012 — Outputs** — `outline-only` — [[QiLife Product Surfaces|QiLife Product Surfaces]]

### Chapter 06.06 — Deferred Finance Bridge

- **§ 06.06.001 — Boundary** — `deferred` — [[QiLife Deferred Finance Bridge|Deferred Finance Bridge]]
- **§ 06.06.002 — Deferred Transactions** — `deferred` — [[QiLife Deferred Finance Bridge|Deferred Finance Bridge]]
- **§ 06.06.003 — Deferred Obligations** — `deferred` — [[QiLife Deferred Finance Bridge|Deferred Finance Bridge]]

## Title 07 — Security & Access

### Chapter 07.01 — Accounts, Permissions & Devices

- **§ 07.01.001 — Account Registry** — `outline-only` — —
- **§ 07.01.002 — Roles** — `outline-only` — —
- **§ 07.01.003 — Permissions** — `outline-only` — —
- **§ 07.01.004 — Devices** — `outline-only` — —
- **§ 07.01.005 — Access Review** — `outline-only` — —
### Chapter 07.02 — Secrets, Incidents & Recovery

- **§ 07.02.001 — Passwords** — `outline-only` — —
- **§ 07.02.002 — API Keys** — `outline-only` — —
- **§ 07.02.003 — Recovery Codes** — `outline-only` — —
- **§ 07.02.004 — Security Incidents** — `outline-only` — —
- **§ 07.02.005 — Credential Rotation** — `outline-only` — —
## Title 08 — Finance & Assets

### Chapter 08.01 — Finance, Inventory & Reimbursements

- **§ 08.01.001 — Accounts** — `outline-only` — —
- **§ 08.01.002 — Transactions** — `outline-only` — —
- **§ 08.01.003 — Receipts** — `outline-only` — —
- **§ 08.01.004 — Inventory** — `outline-only` — —
- **§ 08.01.005 — Reimbursements** — `outline-only` — —
### Chapter 08.02 — Assets, Debts & Reports

- **§ 08.02.001 — Assets** — `outline-only` — —
- **§ 08.02.002 — Property** — `outline-only` — —
- **§ 08.02.003 — Debts** — `outline-only` — —
- **§ 08.02.004 — Claims** — `outline-only` — —
- **§ 08.02.005 — Reports** — `outline-only` — —
## Title 09 — Legal Matters

### Chapter 09.01 — Contracts, Notices & Housing

- **§ 09.01.001 — Contracts** — `outline-only` — —
- **§ 09.01.002 — Agreements** — `outline-only` — —
- **§ 09.01.003 — Notices** — `outline-only` — —
- **§ 09.01.004 — Housing Records** — `outline-only` — —
- **§ 09.01.005 — Deadlines** — `outline-only` — —
### Chapter 09.02 — Disputes, Claims & Client Matters

- **§ 09.02.001 — Disputes** — `outline-only` — —
- **§ 09.02.002 — Claims** — `outline-only` — —
- **§ 09.02.003 — Evidence Packets** — `outline-only` — —
- **§ 09.02.004 — Client Matters** — `outline-only` — —
- **§ 09.02.005 — Case Timelines** — `outline-only` — —
## Title 10 — Publication & Works

### Chapter 10.01 — Publication Registry

- **§ 10.01.001 — Work Types** — `outline-only` — —
- **§ 10.01.002 — Draft Status** — `outline-only` — —
- **§ 10.01.003 — Publication Status** — `outline-only` — —
- **§ 10.01.004 — Platforms** — `outline-only` — —
- **§ 10.01.005 — Canonical Versions** — `outline-only` — —
### Chapter 10.02 — Series, Books, Posts & Pages

- **§ 10.02.001 — Series** — `outline-only` — —
- **§ 10.02.002 — Books** — `outline-only` — —
- **§ 10.02.003 — Chapters** — `outline-only` — —
- **§ 10.02.004 — Essays & Posts** — `outline-only` — —
- **§ 10.02.005 — Public Pages** — `outline-only` — —
## Title 90 — Archive & Quarantine

### Chapter 90.01 — Archive, Deprecation & Cleanup

- **§ 90.01.001 — Archive Rules** — `archived-outline` — [[QiCode Migration Notes|Migration Notes]]
- **§ 90.01.002 — Superseded Items** — `archived-outline` — [[QiCode Migration Notes|Migration Notes]]
- **§ 90.01.003 — Deprecated Items** — `archived-outline` — [[QiCode Migration Notes|Migration Notes]]
- **§ 90.01.004 — Quarantine** — `archived-outline` — [[QiCode Migration Notes|Migration Notes]]
- **§ 90.01.005 — Cleanup Rules** — `archived-outline` — [[QiCode Migration Notes|Migration Notes]]
### Chapter 90.02 — Quarantined Legacy Specifications

- **§ 90.02.001 — Legacy QiLife App Spec** — `quarantined` — [[QiLife App Spec - Legacy|Legacy QiLife Spec]]
## Title 99 — Experimental

### Chapter 99.01 — Prototypes, Research & Parking Lot

- **§ 99.01.001 — Prototypes** — `experimental` — —
- **§ 99.01.002 — Research** — `experimental` — —
- **§ 99.01.003 — Future Concepts** — `experimental` — —
- **§ 99.01.004 — Evaluation** — `experimental` — —
- **§ 99.01.005 — Promote or Kill Rules** — `experimental` — —

## Registry Maintenance

When a section gains an approved body, replace `outline-only` with its status and link the single canonical document. Do not paste the full body into this registry.

---

## 📘 QiCodex — Unified Decimal Registry

# 📘 QiCodex — Unified Decimal Registry

Notes: Merged into existing draft chapter without changing chapter name.
QiCode: § 00.01.005
Parent: Title 00 — General Provisions (Title%2000%20%E2%80%94%20General%20Provisions%20fca8e718a53d46afad20fe1b13fb4caf.md)
Status: draft
Type: Reference

*All folders, files, and modules in QiOne share a single QiDecimal namespace.*

| ID | Name | Description | Owner | Status |
| --- | --- | --- | --- | --- |
| 0 | Inbox | Temporary workspace for uncategorized input | CRV | active |
| 1 | QiEOS | Governance Realm (Constitution + Law) | CRV | active |
| 1.10 | Protocol | QiEOS governance & update process | QiEOS | active |
| 1.20 | QiCode | Life Code (Statutes of System & Self) | QiEOS | active |
| 1.21 | Title I — Foundations | Core principles & structure | QiCode | active |
| 1.21.1 | §1 Principle of Awareness | Law of observation & reflection | QiCode | active |
| 1.21.2 | §2 Principle of Presence | Law of now & embodiment | QiCode | active |
| 1.22 | Title II — Self & Inner Work | Awareness, habits, emotional systems | QiCode | active |
| 1.23 | Title III — Work & Creation | Productivity, flow, and manifestation | QiCode | active |
| 1.24 | Title IV — Relations & Exchange | Boundaries, reciprocity, and connection | QiCode | active |
| 1.25 | Title V — Action & Automation | Execution, energy management, movement | QiCode | active |
| 1.26 | Title VI — Identity & Integrity | Authenticity, naming, and alignment | QiCode | active |
| 1.27 | Title VII — Mind & Will | Decision-making, thought hygiene | QiCode | active |
| 1.28 | Title VIII — Cycles & Closure | Endings, transitions, forgiveness | QiCode | active |
| 1.29 | Title IX — Ethics & Evolution | Moral systems, feedback, growth | QiCode | active |
| 1.30 | Title X — Legacy & Design | Purpose, continuity, vision | QiCode | active |
| 1.30_Templates | Templates | Master templates (App/KB/Client) | QiEOS | active |
| 1.40 | RAG | AI bots, embeddings, and automation layer | QiEOS | active |
| 1.50 | Meta | Indexes, QiCodex, and registry data | QiEOS | active |
| 1.90 | ARCH | Archive of retired QiEOS components | QiEOS | active |
| 2 | QiSelf KB | Personal Knowledge Base | CRV | active |
| 2.10 | START | Overview, system map | CRV | active |
| 2.20 | ABOUT | Story, identity | CRV | active |
| 2.30 | LIFE | Habits, goals, and reflections | CRV | active |
| 2.40 | OPS | Personal workflows and routines | CRV | active |
| 2.50 | DOCS | Personal writings, letters, thoughts | CRV | active |
| 2.60 | MEDIA | Visuals, recordings, transcripts | CRV | active |
| 2.70 | TECH | Automations, scripts, prompts | CRV | active |
| 2.90 | ARCH | Archived personal data | CRV | active |
| 3 | QiAlly KB | Business Knowledge Base | QiAlly | active |
| 3.10 | START | Mission, purpose, branding | QiAlly | active |
| 3.20 | ABOUT | Structure, team, org identity | QiAlly | active |
| 3.30 | OFFER | Services, pricing, strategy | QiAlly | active |
| 3.40 | OPS | SOPs, process docs | QiAlly | active |
| 3.50 | DOCS | Contracts, reports, deliverables | QiAlly | active |
| 3.60 | MEDIA | Design, marketing, assets | QiAlly | active |
| 3.70 | TECH | APIs, automations, integrations | QiAlly | active |
| 3.90 | ARCH | Archived business content | QiAlly | active |
| 4 | Clients | Client Ecosystems | QiAlly | active |
| 4.10 | <slug> | Individual client container | QiAlly | active |
| 4.11 | EOS | Agreements & scope | QiAlly | active |
| 4.12 | KB | Client-specific knowledge base | QiAlly | active |
| 4.13 | SITE | Client site or PWA | QiAlly | active |
| 4.90 | ARCH | Archived client data | QiAlly | active |
| 5 | Apps | Application Layer | QiSuite | active |
| 5.10 | dev | Development environment | QiSuite | active |
| 5.20 | staging | Testing environment | QiSuite | active |
| 5.30 | live | Production environment | QiSuite | active |
| 5.90 | ARCH | Archived deployments | QiSuite | active |
| 6 | Data | Datasets & Indexes | QiSuite | active |
| 6.10 | qi_index | Core knowledge index | QiSuite | active |
| 6.20 | vector | Embeddings & RAG data | QiSuite | active |
| 6.30 | datasets | External datasets | QiSuite | active |
| 6.90 | ARCH | Archived data | QiSuite | active |
| 7 | Tools | Scripts & Utilities | QiSuite | active |
| 7.10 | python | Python utilities | QiSuite | active |
| 7.20 | node | Node.js utilities | QiSuite | active |
| 7.30 | shell | Shell scripts | QiSuite | active |
| 7.90 | ARCH | Archived tools | QiSuite | active |
| 8 | Docs | Manuals & Publications | QiAlly | active |
| 8.10 | Manuals | Guides, handbooks | QiAlly | active |
| 8.20 | Brand | Logos, templates, style | QiAlly | active |
| 8.30 | Publications | External reports | QiAlly | active |
| 8.90 | ARCH | Archived documents | QiAlly | active |
| 9 | ARCH | Global Archive | QiOne | active |

```
---
✅ **What This Achieves**
- Unified numbering from root to law section.
- No padding above 9 — visually minimal and calm.
- All sub-realms and laws predictable (`x.10`, `x.20`, `x.21.1`, etc.).
- One codex to rule all numbering — no improvising IDs ever again.
---
The **QiCodex.csv** file serves as the machine-readable registry for all QiDecimal IDs, ready for `/1.50_Meta/` index automation and future AI lookups.
```

---
