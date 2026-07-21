---
layout: section
title: Title 17. QiApps
slug: qicode-title-17-qiapps
summary: QiApps governs 60_QiApps — all app projects, UI layers, and product tools within the QiLabs ecosystem.
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
  - qilabs
source_type: manual
---

# Title 17. QiApps

## Citation

- Legal citation: `QiCode Title 17`
- Article citation: `QiCode Title 17, Article #`
- Section citation: `QiCode Sec. 17.##.###`
- Stable ID alias: `QiCode T17.A##.S###.L###`

## Rule of Construction

- `Rule 17.001.L001` This title governs `60_QiApps` — app projects, UI layers, and product tools. (stable ID `T17.R001.L001`)
- `Rule 17.001.L002` A section states a governing principle; a line states a citeable rule or application. (stable ID `T17.R001.L002`)
- `Rule 17.001.L003` Exceptions must be named, reviewed, and linked to the record that justifies them. (stable ID `T17.R001.L003`)

## Article 1. QiApps Purpose

Stable ID: `T17.A01`

### Sec. 17.01.010. Primary Function

Stable ID: `T17.A01.S010`

- `Line 1` QiApps contains app projects and UI/tooling layers: products that users or operators directly interact with. (`Sec. 17.01.010.L001`; stable ID `T17.A01.S010.L001`)
- `Line 2` QiApps does not become the source of truth unless explicitly defined in the app's governing doctrine. (`Sec. 17.01.010.L002`; stable ID `T17.A01.S010.L002`)
- `Line 3` If use is ambiguous, the placement rule for the nearest parent title controls. (`Sec. 17.01.010.L003`; stable ID `T17.A01.S010.L003`)

### Sec. 17.01.020. Data Flow Rule

Stable ID: `T17.A01.S020`

- `Line 1` Apps read from and write to approved source layers (Supabase, QiDrive, QiVault) through documented APIs. (`Sec. 17.01.020.L001`; stable ID `T17.A01.S020.L001`)
- `Line 2` Apps must not hold canonical data directly; they surface, transform, and display it. (`Sec. 17.01.020.L002`; stable ID `T17.A01.S020.L002`)
- `Line 3` Any app that holds canonical data must declare it as a source in its title doctrine. (`Sec. 17.01.020.L003`; stable ID `T17.A01.S020.L003`)

## Article 2. App Project Rules

Stable ID: `T17.A02`

### Sec. 17.02.010. Project Structure

Stable ID: `T17.A02.S010`

- `Line 1` Each app project under `60_QiApps` must have a numbered subfolder and a product doctrine document. (`Sec. 17.02.010.L001`; stable ID `T17.A02.S010.L001`)
- `Line 2` Governed apps include QiLife (`40_QiLife`), QiJourney (`30_QiJourney`), GINA (`10_GINA`), CareLite (`10_CareLite`), and Firefly (`firefly.md`). QiAccess (`20_QiAccess`) is retired as a standalone app and merged into Homepage. (`Sec. 17.02.010.L002`; stable ID `T17.A02.S010.L002`)
- `Line 3` Experiments and abandoned apps must be moved to an archive subfolder, not deleted. (`Sec. 17.02.010.L003`; stable ID `T17.A02.S010.L003`)

## Article 3. QiLife

Stable ID: `T17.A03`

### Sec. 17.03.010. QiLife Scope

Stable ID: `T17.A03.S010`

- `Line 1` QiLife is the primary personal life operating system app; it lives in `60_QiApps/40_QiLife`. (`Sec. 17.03.010.L001`; stable ID `T17.A03.S010.L001`)
- `Line 2` QiLife's data spine is Supabase; schema changes follow the migration policy in QiLife's title. (`Sec. 17.03.010.L002`; stable ID `T17.A03.S010.L002`)
- `Line 3` QiLife UI/tools live in QiApps; QiLife source of truth for personal data is QiDrive/Supabase. (`Sec. 17.03.010.L003`; stable ID `T17.A03.S010.L003`)

## Article 4. QiFinance (Firefly)

Stable ID: `T17.A04`

### Sec. 17.04.010. QiFinance Scope

Stable ID: `T17.A04.S010`

- `Line 1` QiFinance (Firefly) is the financial tracking and analysis app; it is documented in `60_QiApps/60_QiApps/firefly.md`. (`Sec. 17.04.010.L001`; stable ID `T17.A04.S010.L001`)
- `Line 2` QiFinance operates on a single financial universe principle: one data model, no duplicate transaction sources. (`Sec. 17.04.010.L002`; stable ID `T17.A04.S010.L002`)
- `Line 3` Financial data authority decisions must be documented in QiFinance ADRs. (`Sec. 17.04.010.L003`; stable ID `T17.A04.S010.L003`)

## Article 5. CareLite

Stable ID: `T17.A05`

### Sec. 17.05.010. CareLite Scope

Stable ID: `T17.A05.S010`

- `Line 1` CareLite and related caregiving tools live in `60_QiApps/60_QiApps/10_CareLite`. (`Sec. 17.05.010.L001`; stable ID `T17.A05.S010.L001`)
- `Line 2` Caregiving records and evidence are protected; the app may surface them but must not modify canonical records. (`Sec. 17.05.010.L002`; stable ID `T17.A05.S010.L002`)
- `Line 3` Care record documentation lives in the vault under protected folders; it does not merge into app source. (`Sec. 17.05.010.L003`; stable ID `T17.A05.S010.L003`)

## Article 6. Experiments

Stable ID: `T17.A06`

### Sec. 17.06.010. Experiment Policy

Stable ID: `T17.A06.S010`

- `Line 1` Experimental apps and tooling live in `60_QiApps/69_QiTrials` or equivalent. (`Sec. 17.06.010.L001`; stable ID `T17.A06.S010.L001`)
- `Line 2` Experiments must be clearly labeled with status, start date, and exit criteria. (`Sec. 17.06.010.L002`; stable ID `T17.A06.S010.L002`)
- `Line 3` An experiment that moves to production must graduate to its own numbered subfolder with a product doctrine doc. (`Sec. 17.06.010.L003`; stable ID `T17.A06.S010.L003`)

## Article 7. App Lifecycle

Stable ID: `T17.A07`

### Sec. 17.07.010. Lifecycle States

Stable ID: `T17.A07.S010`

- `Line 1` App lifecycle states are: `experimental`, `active`, `maintenance`, `deprecated`, `archived`. (`Sec. 17.07.010.L001`; stable ID `T17.A07.S010.L001`)
- `Line 2` Status must be reflected in the app's `status` frontmatter field and its doctrine document. (`Sec. 17.07.010.L002`; stable ID `T17.A07.S010.L002`)
- `Line 3` A deprecated app must document its successor and migration path before being archived. (`Sec. 17.07.010.L003`; stable ID `T17.A07.S010.L003`)

## Cross References

- [QiCode Index](../_index.md)
- [Title 10 — QiLabs](../title_10_qilabs/title_10_qilabs.md)
- [Migration Map](../reference/qilabs_title_migration_map.md)
