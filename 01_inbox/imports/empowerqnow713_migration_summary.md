---
layout: page
type: note
title: Empowerqnow713 Migration Summary
slug: empowerqnow713-migration-summary
summary: ""
status: active
created_at: "2026-07-07T23:45:07-04:00"
updated_at: "2026-07-18T11:03:11-04:00"
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 83005025a64a4267b0951742eaea5cb7
canonical_ref: ""
source_type: manual
template_key: master-template
---

# EmpowerQNow713 Migration Summary

Generated: 2026-07-08 02:28:08

## Uploaded tree scan

- Target subtree: `40_QiVault/30_empowerqnow713`
- Files classified: **274**
- Planned actions: {'move': 268, 'keep': 5, 'review': 1}

## Safety defaults

- Script defaults to dry-run.
- Script defaults to copy mode, not move mode.
- No existing destination file is overwritten.
- Collisions receive a `__migrated_YYYYMMDD_HHMMSS_###` suffix.
- Hidden vault/system folders are skipped.
- Existing content is not edited; missing index files can be created from the master template.

## Recommended first run

```powershell
python .\safe_qivault_empower_migrator.py --root "C:\QiLabs\40_QiVault\30_empowerqnow713" --dry-run
```

## Recommended first actual copy pass

```powershell
python .\safe_qivault_empower_migrator.py --root "C:\QiLabs\40_QiVault\30_empowerqnow713" --apply --mode copy
```
