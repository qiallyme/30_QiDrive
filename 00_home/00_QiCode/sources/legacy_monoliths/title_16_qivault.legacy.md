---
layout: section
title: Title 16. QiVault
slug: qicode-title-16-qivault
summary: QiVault governs 40_QiVault — the markdown vault, local knowledge workspace, and frontmatter-governed note system.
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
  - qilabs
source_type: manual
---

# Title 16. QiVault

## Citation

- Legal citation: `QiCode Title 16`
- Article citation: `QiCode Title 16, Article #`
- Section citation: `QiCode Sec. 16.##.###`
- Stable ID alias: `QiCode T16.A##.S###.L###`

## Rule of Construction

- `Rule 16.001.L001` This title governs `40_QiVault` — the markdown vault and local knowledge workspace. (stable ID `T16.R001.L001`)
- `Rule 16.001.L002` A section states a governing principle; a line states a citeable rule or application. (stable ID `T16.R001.L002`)
- `Rule 16.001.L003` Exceptions must be named, reviewed, and linked to the record that justifies them. (stable ID `T16.R001.L003`)

## Article 1. Vault Purpose

Stable ID: `T16.A01`

### Sec. 16.01.010. Primary Function

Stable ID: `T16.A01.S010`

- `Line 1` QiVault is the markdown vault and local knowledge workspace: notes, journals, indexes, and local doctrine. (`Sec. 16.01.010.L001`; stable ID `T16.A01.S010.L001`)
- `Line 2` QiVault may mirror or stage markdown knowledge that originates in QiDrive or other sources. (`Sec. 16.01.010.L002`; stable ID `T16.A01.S010.L002`)
- `Line 3` If use is ambiguous, the placement rule for the nearest parent title controls. (`Sec. 16.01.010.L003`; stable ID `T16.A01.S010.L003`)

### Sec. 16.01.020. Vault vs. Drive

Stable ID: `T16.A01.S020`

- `Line 1` QiVault is not the same as QiDrive when QiDrive is acting as the source of truth for files. (`Sec. 16.01.020.L001`; stable ID `T16.A01.S020.L001`)
- `Line 2` Do not duplicate canonical docs between vault and drive without a clear source mapping in frontmatter. (`Sec. 16.01.020.L002`; stable ID `T16.A01.S020.L002`)
- `Line 3` When a markdown file exists in both places, the one with `source_type: manual` and a `canonical_ref` wins. (`Sec. 16.01.020.L003`; stable ID `T16.A01.S020.L003`)

## Article 2. Markdown Rules

Stable ID: `T16.A02`

### Sec. 16.02.010. Frontmatter Requirement

Stable ID: `T16.A02.S010`

- `Line 1` All markdown files in QiVault must carry valid frontmatter as defined by the master template. (`Sec. 16.02.010.L001`; stable ID `T16.A02.S010.L001`)
- `Line 2` Frontmatter keys defined as required in the housekeeping config must not be absent or empty. (`Sec. 16.02.010.L002`; stable ID `T16.A02.S010.L002`)
- `Line 3` List-type fields (`tags`, `keywords`, `aliases`) must use YAML block scalar format, not inline `[]` followed by dangling list items. (`Sec. 16.02.010.L003`; stable ID `T16.A02.S010.L003`)

## Article 3. Indexes

Stable ID: `T16.A03`

### Sec. 16.03.010. Index Policy

Stable ID: `T16.A03.S010`

- `Line 1` Each significant folder in QiVault must have an `_index.md` that describes the folder's purpose. (`Sec. 16.03.010.L001`; stable ID `T16.A03.S010.L001`)
- `Line 2` Index files must not be deleted by housekeeping tools; they are protected files. (`Sec. 16.03.010.L002`; stable ID `T16.A03.S010.L002`)
- `Line 3` Generated index blocks must be clearly marked with housekeeping managed block comments. (`Sec. 16.03.010.L003`; stable ID `T16.A03.S010.L003`)

## Article 4. Links and Backlinks

Stable ID: `T16.A04`

### Sec. 16.04.010. Link Integrity

Stable ID: `T16.A04.S010`

- `Line 1` Obsidian wiki-links within the vault must use stable file slugs or paths, not display names. (`Sec. 16.04.010.L001`; stable ID `T16.A04.S010.L001`)
- `Line 2` Link rewrites must not be run globally without a separately approved rewrite plan. (`Sec. 16.04.010.L002`; stable ID `T16.A04.S010.L002`)
- `Line 3` Broken links are surfaced in housekeeping reports; they must be resolved, not silently patched. (`Sec. 16.04.010.L003`; stable ID `T16.A04.S010.L003`)

## Article 5. Frontmatter

Stable ID: `T16.A05`

### Sec. 16.05.010. Frontmatter Governance

Stable ID: `T16.A05.S010`

- `Line 1` The canonical frontmatter standard is defined in the master template at `00_QiLabs.workspace/_qiconfig/master_template.md`. (`Sec. 16.05.010.L001`; stable ID `T16.A05.S010.L001`)
- `Line 2` Housekeeping may add missing required keys but must not overwrite non-empty values without explicit approval. (`Sec. 16.05.010.L002`; stable ID `T16.A05.S010.L002`)
- `Line 3` Tags must be registered in the global tag registry before use; unknown tags are surfaced as warnings. (`Sec. 16.05.010.L003`; stable ID `T16.A05.S010.L003`)

## Article 6. Knowledge Boundaries

Stable ID: `T16.A06`

### Sec. 16.06.010. Knowledge Placement

Stable ID: `T16.A06.S010`

- `Line 1` Personal knowledge, journals, notes, and life records belong in QiVault. (`Sec. 16.06.010.L001`; stable ID `T16.A06.S010.L001`)
- `Line 2` Developer system docs belong in QiSpark or the relevant domain title, not the personal vault. (`Sec. 16.06.010.L002`; stable ID `T16.A06.S010.L002`)
- `Line 3` Vault content must not be published without a `publish_target` declaration and sensitivity review. (`Sec. 16.06.010.L003`; stable ID `T16.A06.S010.L003`)

## Article 7. Sync and Archive

Stable ID: `T16.A07`

### Sec. 16.07.010. Vault Sync Policy

Stable ID: `T16.A07.S010`

- `Line 1` QiVault is version-controlled in its own git repository; commits are the canonical record of vault state. (`Sec. 16.07.010.L001`; stable ID `T16.A07.S010.L001`)
- `Line 2` Obsidian and Smart Env plugin files (`.obsidian/`, `.smart-env/`) are tracked but not treated as canonical knowledge. (`Sec. 16.07.010.L002`; stable ID `T16.A07.S010.L002`)
- `Line 3` Archived vault material is moved to `99_archive` with a clear archive date and reason. (`Sec. 16.07.010.L003`; stable ID `T16.A07.S010.L003`)

## Cross References

- [QiCode Index](../_index.md)
- [Title 10 — QiLabs](../title_10_qilabs/title_10_qilabs.md)
- [Migration Map](../reference/qilabs_title_migration_map.md)
