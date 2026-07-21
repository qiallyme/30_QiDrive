---
layout: article
title: Article 1. QiApps Purpose
slug: qicode-title-17-article-01-qiapps-purpose
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 17
qicode_article: 1
parent_title: Title 17. QiApps
canonical_ref: QiCode T17.A01
source_type: manual
---

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


