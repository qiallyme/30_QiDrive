---
layout: section
title: Title 11. QiLabs Workspace
slug: qicode-title-11-qilabs-workspace
summary: QiLabs Workspace governs 00_QiLabs.workspace — templates, housekeeping, configs, manifests, and operational support tools.
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
  - qilabs
source_type: manual
---

# Title 11. QiLabs Workspace

## Citation

- Legal citation: `QiCode Title 11`
- Article citation: `QiCode Title 11, Article #`
- Section citation: `QiCode Sec. 11.##.###`
- Stable ID alias: `QiCode T11.A##.S###.L###`

## Rule of Construction

- `Rule 11.001.L001` This title governs `00_QiLabs.workspace` — the operational support layer for the entire QiLabs root. (stable ID `T11.R001.L001`)
- `Rule 11.001.L002` A section states a governing principle; a line states a citeable rule or application. (stable ID `T11.R001.L002`)
- `Rule 11.001.L003` Exceptions must be named, reviewed, and linked to the record that justifies them. (stable ID `T11.R001.L003`)

## Article 1. Workspace Purpose

Stable ID: `T11.A01`

### Sec. 11.01.010. Primary Function

Stable ID: `T11.A01.S010`

- `Line 1` The workspace holds operational support material: templates, housekeeping tools, manifests, reports, and run scripts. (`Sec. 11.01.010.L001`; stable ID `T11.A01.S010.L001`)
- `Line 2` The workspace is not the vault, app source, docs site, file archive, or server runtime. (`Sec. 11.01.010.L002`; stable ID `T11.A01.S010.L002`)
- `Line 3` If use is ambiguous, the material belongs in the governed domain it supports, not the workspace. (`Sec. 11.01.010.L003`; stable ID `T11.A01.S010.L003`)

### Sec. 11.01.020. Scope Boundary

Stable ID: `T11.A01.S020`

- `Line 1` Workspace material is tooling that operates on other domains, not domain content itself. (`Sec. 11.01.020.L001`; stable ID `T11.A01.S020.L001`)
- `Line 2` Source of truth for vault, apps, and sites does not live in the workspace. (`Sec. 11.01.020.L002`; stable ID `T11.A01.S020.L002`)
- `Line 3` Agent instructions, codex files, and shared configs belong here when they apply across the whole root. (`Sec. 11.01.020.L003`; stable ID `T11.A01.S020.L003`)

## Article 2. Templates

Stable ID: `T11.A02`

### Sec. 11.02.010. Template Authority

Stable ID: `T11.A02.S010`

- `Line 1` The canonical master template lives in `00_QiLabs.workspace/_qiconfig/master_template.md`. (`Sec. 11.02.010.L001`; stable ID `T11.A02.S010.L001`)
- `Line 2` Vault templates must conform to master template frontmatter requirements. (`Sec. 11.02.010.L002`; stable ID `T11.A02.S010.L002`)
- `Line 3` Templates must be reviewed before deployment to ensure required keys are present and type values are correct. (`Sec. 11.02.010.L003`; stable ID `T11.A02.S010.L003`)

## Article 3. Housekeeping

Stable ID: `T11.A03`

### Sec. 11.03.010. Housekeeping Scope

Stable ID: `T11.A03.S010`

- `Line 1` The housekeeping tool governs frontmatter normalization, tag validation, inventory, reports, and link rewriting. (`Sec. 11.03.010.L001`; stable ID `T11.A03.S010.L001`)
- `Line 2` Broad renames must not be executed without a separately approved rename plan. (`Sec. 11.03.010.L002`; stable ID `T11.A03.S010.L002`)
- `Line 3` Housekeeping must run dry-run first; apply only after review. (`Sec. 11.03.010.L003`; stable ID `T11.A03.S010.L003`)

## Article 4. Config and Manifests

Stable ID: `T11.A04`

### Sec. 11.04.010. Configuration Authority

Stable ID: `T11.A04.S010`

- `Line 1` Workspace `_qiconfig` holds canonical config for housekeeping, tags, and master templates. (`Sec. 11.04.010.L001`; stable ID `T11.A04.S010.L001`)
- `Line 2` Config changes must be reviewed before applying any housekeeping run that depends on them. (`Sec. 11.04.010.L002`; stable ID `T11.A04.S010.L002`)
- `Line 3` Manifests record point-in-time state and must not be used as live operational truth. (`Sec. 11.04.010.L003`; stable ID `T11.A04.S010.L003`)

## Article 5. Codex and Agent Instructions

Stable ID: `T11.A05`

### Sec. 11.05.010. Agent Governance

Stable ID: `T11.A05.S010`

- `Line 1` Agent instructions, AGENTS.md, and skill files that apply across the whole root are managed from the workspace. (`Sec. 11.05.010.L001`; stable ID `T11.A05.S010.L001`)
- `Line 2` Agent instructions must not contradict QiCode doctrine; when conflict exists, QiCode governs. (`Sec. 11.05.010.L002`; stable ID `T11.A05.S010.L002`)
- `Line 3` Skills and agents with domain-specific scope belong in `.agents` at the domain root, not the workspace. (`Sec. 11.05.010.L003`; stable ID `T11.A05.S010.L003`)

## Article 6. Logs, Reports, and Plans

Stable ID: `T11.A06`

### Sec. 11.06.010. Log Retention

Stable ID: `T11.A06.S010`

- `Line 1` Housekeeping run logs, reports, and plans are stored in the workspace toolbox; they are not vault knowledge. (`Sec. 11.06.010.L001`; stable ID `T11.A06.S010.L001`)
- `Line 2` Plans must be reviewed before applying; approved plans are the only basis for `apply` runs. (`Sec. 11.06.010.L002`; stable ID `T11.A06.S010.L002`)
- `Line 3` Summaries may be promoted to vault outputs when they contain institutional knowledge worth preserving. (`Sec. 11.06.010.L003`; stable ID `T11.A06.S010.L003`)

## Cross References

- [QiCode Index](../_index.md)
- [Title 10 — QiLabs](../title_10_qilabs/title_10_qilabs.md)
- [Migration Map](../reference/qilabs_title_migration_map.md)
