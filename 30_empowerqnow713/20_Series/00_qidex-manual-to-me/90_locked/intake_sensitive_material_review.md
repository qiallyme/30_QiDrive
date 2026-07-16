---
title: Intake Sensitive Material Review
section: 01_Q/90_locked/00_my_eyes_only
category: sensitive_review
access_level: L4
visibility: locked
ai_ingest: false
shareable: never
status: migrated
created: 2026-05-24
last_updated: 2026-05-24
related:
  - 20_personal/30_identity_notes/identity_context.md
  - 30_clinical/00_clinical_summary/clinical_summary_starter.md
  - 99_system/40_exports/intake_migration_report.md
tags:
  - locked
  - sensitive
  - intake
  - review
source:
  - _intake/PART XI - Manual to Me Cody’s Guide to Understandi 203f84a044028013b57ecce49990408d.md
  - _intake/10 1 Transgender 219f84a04402810cb8f6e70c5a540224.md
  - _intake/10 4 Person of Color 219f84a04402811eb893f617ab821fe0.md
  - _intake/10 5 Phonophobia 219f84a044028179b85bcdef2fa17d96.md
  - _intake/10 6 Depression 219f84a04402813d9db1deaebc48293a.md
  - _intake/10 7 PTSD 219f84a044028133b42bd62ad343dca2.md
  - _intake/10 8 Anxiety 219f84a0440281bb9e13c5b9d4a1af18.md
  - _intake/10 9 ADHD 219f84a04402818281e6cecb0ef7384a.md
  - _intake/10 10 Correspondence Anxiety 219f84a0440281dd8158c32fb4331416.md
  - _intake/Codys_Guide_to_Understanding_and_Connection.wav
  - _intake/Codys_Guide_to_Understanding_and_Connection_(1).wav
---

# Intake Sensitive Material Review

## Audio Version

![[manual_final_review_audio.mp3]]

## Purpose

This file tracks which imported source items contain sensitive material, unresolved artifacts, or handling concerns that should not be casually promoted into more accessible layers.

## Sensitive Content Categories Found in `_intake`

- non-public identity disclosures
- self-reported clinical and mental health labels
- trauma- and PTSD-related language
- raw audio artifacts, some of which now have compressed derivative copies in layer folders
- duplicated or AI-expanded explanatory content that is not reliable as standalone evidence

## Recommended Handling

### Summarize, do not quote widely

The condition-specific files under `10.*` are useful for extracting themes, but many read like generalized AI explainers. They should support cautious summaries, not become canonical truth on their own.

### Keep identity disclosures restricted

Transgender and person-of-color material is not surface-safe by default and should remain restricted or case-by-case.

### Keep source audio separate from canonical notes

Compressed `.mp3` derivatives were created for the available section recordings and placed beside the matching canonical notes. The original `.wav` files still remain raw source artifacts in `_intake/`, and their spoken content has not been transcript-verified in this pass.

## Human Review Flags

- non-English or encoding-damaged text appears in several overview files
- one referenced personality note is missing from the export
- some audio-linked markdown sections do not have matching clean transcript text
- some intake markdown files reference section audio files that are missing from the export, especially for sections 06 and 08
- no source in `_intake` grounds a full life-history chronology

## Promotion Rule

Nothing in this review file should be treated as public-safe or AI-safe for general ingestion. Promote only by creating or revising a separate canonical file at a lower sensitivity level.
