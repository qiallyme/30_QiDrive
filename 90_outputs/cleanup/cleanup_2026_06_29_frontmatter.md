---
layout: artifact
title: Front Matter and Formatting Cleanup - 2026-06-29
slug: cleanup-2026-06-29-frontmatter
summary: Scripted and manual cleanup report for front matter normalization and key document formatting.
status: active
created_at: "2026-06-29"
updated_at: "2026-07-18T11:03:20-04:00"
tags:
  - cleanup
  - vault-maintenance
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
uid: c75d12890fe648aebb8ab6baa68752f8
canonical_ref: ""
template_key: master-template
type: note
---

# Front Matter and Formatting Cleanup - 2026-06-29

## Scripted Pass

- Added or normalized front matter across the vault.
- Preserved non-standard imported front matter fields instead of dropping them.
- Added missing H1 headings where the note had no visible title.
- Removed duplicate first H1 headings caused by earlier import cleanup.
- Normalized line endings and excess blank lines.
- Repaired common mojibake/encoding artifacts in imported and generated markdown.
- Moved generated Python cache and script placeholder notes into cleanup review storage.

## Manual Review Pass

- Rebuilt [QiNotesSync Home](00_home/00_home.md).
- Rebuilt [Lisa Care Record 2026](40_projects/Lisa_Care_Record_2026/Lisa_Care_Record_2026.md).
- Rebuilt [Lisa Care Record start page](../40_projects/Lisa_Care_Record_2026/00_START_HERE/index.md).
- Rebuilt [Lisa Care Record Dashboard](dashboard.care_record.md).
- Rebuilt [How to Use This Vault](how_to_use_this_vault.md).
- Rebuilt [Record Scope and Boundaries](record_scope_and_boundaries.md).
- Rebuilt [Obsidian Plugin Setup Instructions](obsidian_plugin_setup_instructions.md).
- Rebuilt the active [Daily Notes](../10_daily/02_daily.md) index.

## Records

- [Front matter report](../_qiconfig/cleanup_2026-06-29_frontmatter/frontmatter_formatting_report.csv)
- [Encoding repair report](../_qiconfig/cleanup_2026-06-29_frontmatter/encoding_repair_report.csv)
- [Encoding repair pass 2 report](../_qiconfig/cleanup_2026-06-29_frontmatter/encoding_repair_pass2_report.csv)
- Backups are stored under `_qiconfig/cleanup_2026-06-29_frontmatter`.

## Validation

- Markdown files checked outside cleanup archives: 864.
- Missing front matter: 0.
- Missing required front matter fields (`layout`, `title`, `status`): 0.
- Scalar `tags:` fields remaining: 0.
- Notes without an H1 heading: 0.
- Detected mojibake/encoding artifact files: 0.
- Broken local links in manually reviewed entry pages: 0.
- Remaining Notion-artifact files: 25.
- Remaining long-line files: 111.

## Remaining Manual Work

- Review long imported Notion notes with `<aside>` blocks.
- Review sensitive Lisa evidence summaries for audience-specific wording before sending.
- Decide whether `10_daily` should remain the active daily folder name or be migrated back to `02_daily` in a separate, link-aware move.
