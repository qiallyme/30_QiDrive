---
layout: report
title: QiCode Root Doctrine Cleanup
slug: cleanup-2026-06-30-qicode-root
summary: Moved QiCode root doctrine and overview files into their correct homes, leaving only the QiCode index at root.
status: complete
updated_at: "2026-07-18T11:03:20-04:00"
tags:
  - cleanup
  - qicode
  - qispark
source_type: manual
created_at: "2026-07-01T23:17:15-05:00"
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 05f6b1d190854da8b0a175220cea27f4
canonical_ref: ""
template_key: master-template
type: note
---

# QiCode Root Doctrine Cleanup

## Result

The root of `10_qispark/00_QiCode` now contains only `_index.md` as a Markdown file. Active doctrine remains organized by legal-code title folders.

## Moved QiCode Reference Files

- `citation_guide.md` -> `10_qispark/00_QiCode/reference/citation_guide.md`
- `01_core_overview.md` -> `10_qispark/00_QiCode/reference/core_overview.md`

## Moved Personal Source Doctrine

- `1.0_QiCode_Life_Protocol.md` -> `10_qispark/00_QiCode/sources/qicode_life_protocol.md`

This source is marked as personal doctrine source material and should continue to influence the active QiCode title files.

## Moved Legacy Dev Doctrine

- `00_principles.md` -> `10_qispark/10_QiSpark/90_legacy_doctrine/founding_principles_legacy.md`
- `1.01_Core_Principles.md` -> `10_qispark/10_QiSpark/90_legacy_doctrine/core_principles_legacy.md`
- `QiEOS_Protocol_v3.0.md` -> `10_qispark/10_QiSpark/90_legacy_doctrine/qieos_protocol_v3_legacy.md`
- `QiSuite_Dev_Bible.md` -> `10_qispark/10_QiSpark/90_legacy_doctrine/qisuite_dev_bible_legacy.md`

These files are marked as legacy reference material for QiSpark, not as active QiCode personal doctrine.

## Index Updates

- `10_qispark/00_QiCode/_index.md` now links to the legal-code titles, the reference folder, the personal source, QiSpark, QiServer, QiMemory, and QiConnect.
- `10_qispark/10_QiSpark/_index.md` now links to the actual `10_QiOS` subfolders and the legacy doctrine source index.
- `10_qispark/10_QiSpark/90_legacy_doctrine/_index.md` was added.

## Validation

- Checked QiCode and QiSpark legacy doctrine files: 19 files.
- Broken Markdown links found: 0.
- Encoding artifact files found: 0.
- QiCode root Markdown files remaining: `_index.md` only.

## Script And Manifest

- Script: `_qiconfig/scripts/finalize_qicode_root.py`
- Manifest: `_qiconfig/cleanup_2026-06-30_qicode_root/qicode_root_manifest.csv`
- Backups: `_qiconfig/cleanup_2026-06-30_qicode_root/backups`
