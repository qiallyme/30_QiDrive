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
