---
layout: page
title: Obsidian Plugin Setup Instructions
slug: obsidian-plugin-setup-instructions
summary: Suggested Obsidian plugins and settings for maintaining the Lisa Care Record.
status: publish
updated_at: "2026-07-16T06:49:36-04:00"
tags: []
  - projects
  - lisa-care-record
source_type: manual
created_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 326196eb70b1439db160f59b4f67395f
canonical_ref: ""
template_key: master-template
---

# Obsidian Plugin Setup Instructions

These plugins are optional, but they make the record easier to maintain consistently.

## 1. Templater

- Configure folder templates so new files receive the correct starter structure.
- Suggested mappings:
  - `01_FORMAL_RECORD/` -> `_templates/01_template.formal_record.md`
  - `02_TIMELINE/` -> `_templates/02_template.timeline.md`
  - `03_EXHIBITS/` -> `_templates/03_template.exhibit.md`
  - `04_FINANCIAL_LEDGER/` -> `_templates/04_template.ledger.md`
  - `06_COMMUNICATIONS/` -> `_templates/06_template.communication.md`

## 2. QuickAdd

- Create fast-capture commands for timeline events, worklog entries, exhibit notes, and communication summaries.
- Keep commands tied to the correct folder and template.

## 3. Linter

- Configure the Linter to update `updated_at` when a file is saved.
- Do not let Linter overwrite manually entered `created_at` values.
- Preserve YAML list formatting for fields like `tags`, `aliases`, and `references`.

## 4. Dataview

- Use Dataview on `00_START_HERE/index.md` or `01_dashboard.care_record.md` to list files by status, sensitivity, or tags.
- Prefer Dataview for review dashboards, not for canonical record truth.

## 5. Metadata Menu

- Define allowed values for fields like `status`, `sensitivity`, and `share_level`.
- Use it to prevent typos and keep records consistent across sections.
