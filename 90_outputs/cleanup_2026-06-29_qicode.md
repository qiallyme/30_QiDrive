---
layout: artifact
title: QiCode Personal Doctrine Refactor - 2026-06-29
slug: cleanup-2026-06-29-qicode
summary: Report for reshaping QiCode into personal life doctrine with a legal-code citation style and a bridge into QiSpark technical doctrine.
status: active
created_at: "2026-06-29"
updated_at: "2026-06-29"
tags:
  - cleanup
  - qicode
  - qispark
artifact_kind: report
source_type: generated
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
template_key: master-template
---

# QiCode Personal Doctrine Refactor - 2026-06-29

## What Changed

- Recentered QiCode as personal life doctrine, not general technical doctrine.
- Rebuilt the active [QiCode index](10_qispark/00_QiCode/_index.md).
- Updated the [QiCode citation guide](10_qispark/00_QiCode/citation_guide.md).
- Updated [QiCode Core Overview](10_qispark/00_QiCode/01_core_overview.md).
- Replaced the prior generated title model with 9 corrected titles.
- Archived previous generated title folders under `_qiconfig/cleanup_2026-06-29_qicode_personal/moved_review/previous_generated_titles`.
- Preserved the legal-code reference style: Title, Article, Section, Line.

## Active Doctrine Shape

- [T01 - My Truth and Source](10_qispark/00_QiCode/title_01_truth/title_01_truth.md)
- [T02 - Inner World and Self](10_qispark/00_QiCode/title_02_self/title_02_self.md)
- [T03 - Identity and Integrity](10_qispark/00_QiCode/title_03_identity/title_03_identity.md)
- [T04 - Mind and Will](10_qispark/00_QiCode/title_04_mind/title_04_mind.md)
- [T05 - Work, Creation, and Stewardship](10_qispark/00_QiCode/title_05_work/title_05_work.md)
- [T06 - People, Relations, and Exchange](10_qispark/00_QiCode/title_06_people/title_06_people.md)
- [T07 - Ethics, Responsibility, and Disclosure](10_qispark/00_QiCode/title_07_ethics/title_07_ethics.md)
- [T08 - Cycles, Closure, and Legacy](10_qispark/00_QiCode/title_08_cycles_legacy/title_08_cycles_legacy.md)
- [T09 - QiSpark Technical Doctrine Bridge](10_qispark/00_QiCode/title_09_qispark_bridge/title_09_qispark_bridge.md)

## Citation Pattern

- Title: `QiCode Title 1`
- Article: `QiCode Title 1, Article 1`
- Section: `QiCode Sec. 1.01.010`
- Line: `QiCode Sec. 1.01.010, Line 1`

Compact IDs remain as stable aliases, for example `QiCode T01.A01.S010.L001`.

## Technical Handoff

QiCode `T01` through `T08` are personal doctrine. `T09` is the bridge into technical/dev doctrine:

- [QiSpark System](../10_qispark/10_QiSpark/_index.md)
- [QiServer](10_qispark/01_QiInfra-Global/20_QiServer/_index.md)
- [QiMemory](10_qispark/01_QiInfra-Global/20_QiServer/30_QiMemory/_index.md)
- [QiConnect](10_qispark/01_QiInfra-Global/20_QiServer/50_QiConnect/_index.md)

## Validation

- Active QiCode files checked: 12.
- Missing front matter in active QiCode files: 0.
- Missing H1 headings in active QiCode files: 0.
- Broken links in active QiCode index, guide, overview, and title files: 0.
- Legal-style labels now appear before compact stable IDs.

## Records

- [Personal doctrine manifest](../_qiconfig/cleanup_2026-06-29_qicode_personal/qicode_personal_doctrine_manifest.csv)
- [Legal-label manifest](../_qiconfig/cleanup_2026-06-29_qicode_legal_labels/qicode_legal_labels_manifest.csv)
- Generator script: [reshape_qicode_personal.py](../_qiconfig/scripts/reshape_qicode_personal.py)
- Label-first script: [qicode_legal_labels_first.py](../_qiconfig/scripts/qicode_legal_labels_first.py)
- Earlier generator script retained for reference: [legalize_qicode.py](../_qiconfig/scripts/legalize_qicode.py)
