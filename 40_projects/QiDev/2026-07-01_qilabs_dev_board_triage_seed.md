---
layout: page
title: Qilabs Dev Board Triage Seed
slug: qilabs-dev-board-triage-seed
summary: ""
status: active
created_at: "2026-07-01T23:17:15-05:00"
updated_at: "2026-07-18T11:03:20-04:00"
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ba75aae0bb414633aeee4a3464d334ef
canonical_ref: ""
source_type: manual
template_key: master-template
type: note
---

# QiLabs Dev Board — Cross-Project Triage Seed

**Date:** 2026-07-01  
**Knowledge base target:** QiOS / QiLabs development workflow  
**Purpose:** Seed the GitHub Project with known open development items across QiLabs, without over-scoping them.

---

## Core Rule

These are **Triage** items.

Do **not** write full specs yet. Add the issue title and fields only.

An item leaves Triage only when it has:

- a clear problem
- a desired outcome
- a rough scope
- acceptance criteria
- an estimate

---

## GitHub Project Field Defaults

For every item below:

| Field | Default |
|---|---|
| Status | Inbox |
| Iteration | blank |

Backlog is not a dumping ground. Backlog means:

```txt
status:Ready no:iteration
```

Triage means:

```txt
status:Inbox
```

Current means:

```txt
iteration:@current -status:Done
```

---

# Seed Triage Items

## QiOS / Toolbox

| Issue | Priority | Type | App / Area | Estimate |
|---|---:|---|---|---:|
| `[QiOS] Bug: Restore broken tool actions` | P1 | Bug | QiOS | 5 |
| `[QiOS] Refactor: Convert toolbox into plugin-based shell` | P1 | Refactor | QiOS | 8 |
| `[QiOS] Chore: Kill old background processes before build/run` | P1 | Chore | QiOS | 3 |
| `[QiOS] Chore: Audit existing tools for plugin conversion` | P1 | Chore | QiOS | 5 |
| `[QiOS] Feature: Add plugin manifest and dynamic tool buttons` | P1 | Feature | QiOS | 5 |
| `[QiOS] Chore: Add plugin smoke test checklist` | P1 | Chore | QiOS | 3 |

## QiFi / Finance App

| Issue | Priority | Type | App / Area | Estimate |
|---|---:|---|---|---:|
| `[QiFi] Design: Define double-entry accounting model` | P1 | Design | QiFi | 8 |
| `[QiFi] Feature: Build transaction importer pipeline` | P1 | Feature | QiFi | 8 |
| `[QiFi] Bug: Handle duplicate imported transactions` | P1 | Bug | QiFi | 5 |
| `[QiFi] Feature: Add chart-of-accounts templates` | P2 | Feature | QiFi | 5 |
| `[QiFi] Feature: Add bills, debts, assets, and liabilities model` | P2 | Feature | QiFi | 8 |
| `[QiFi] Chore: Stabilize qifinance worker runtime config` | P1 | Chore | QiFi | 3 |
| `[QiFi] Docs: Add finance schema purpose and critique context` | P2 | Docs | QiFi | 2 |

## QiServer / Supabase / Cloudflare

| Issue | Priority | Type | App / Area | Estimate |
|---|---:|---|---|---:|
| `[QiServer] Bug: Fix Supabase records API 403/CORS/RLS issue` | P1 | Bug | QiServer | 5 |
| `[QiServer] Feature: Add GPT action endpoint for Supabase memory access` | P1 | Feature | QiServer | 5 |
| `[QiServer] Docs: Document Supabase secrets and env names` | P1 | Docs | QiServer | 2 |
| `[QiServer] Chore: Add Cloudflare Pages/Workers deployment checklist` | P2 | Chore | QiServer | 3 |
| `[QiServer] Design: Define Zero Trust and auth boundary` | P2 | Design | QiServer | 5 |
| `[QiServer] Chore: Move runtime scripts out of workspace root` | P2 | Chore | QiServer | 3 |

## QiMemory

| Issue | Priority | Type | App / Area | Estimate |
|---|---:|---|---|---:|
| `[QiMemory] Design: Define memory/config/rules storage model` | P1 | Design | QiMemo | 5 |
| `[QiMemory] Feature: Add retrieve memory action` | P1 | Feature | QiMemo | 5 |
| `[QiMemory] Feature: Add edit/update memory action` | P1 | Feature | QiMemo | 5 |
| `[QiMemory] Docs: Write custom GPT action setup guide` | P1 | Docs | QiMemo | 3 |

> Naming note: if the project field still says `QiMemo`, use that field value for now. Rename to `QiMemory` later if you decide to standardize it.

## QiLife / Cadence / Planner

| Issue | Priority | Type | App / Area | Estimate |
|---|---:|---|---|---:|
| `[QiLife] Bug: Stop Cadence-style auto-project creation loop` | P1 | Bug | QiLife | 5 |
| `[QiLife] Design: Define Planner / ERM / Workbench navigation` | P1 | Design | QiLife | 5 |
| `[QiLife] Feature: Add daily plan and activity workflow` | P2 | Feature | QiLife | 5 |
| `[QiLife] Feature: Add journal ledger and timeline model` | P1 | Feature | QiLife | 8 |
| `[QiLife] Docs: Standardize Obsidian note naming and templates` | P2 | Docs | QiLife | 3 |

## QiCare

| Issue | Priority | Type | App / Area | Estimate |
|---|---:|---|---|---:|
| `[QiCare] Design: Define caregiver event timeline model` | P2 | Design | QiCare | 5 |
| `[QiCare] Feature: Add incident reporting workflow` | P2 | Feature | QiCare | 5 |
| `[QiCare] Feature: Link care events to evidence records` | P2 | Feature | QiCare | 5 |
| `[QiCare] Docs: Draft caregiver documentation standards` | P2 | Docs | QiCare | 3 |

## QiSpark / Docs / Public Site

| Issue | Priority | Type | App / Area | Estimate |
|---|---:|---|---|---:|
| `[QiSpark] Bug: Stop AI-generated book summaries replacing landing pages` | P1 | Bug | QiSpark | 3 |
| `[QiSpark] Feature: Build QiSpark docs and landing homepage` | P1 | Feature | QiSpark | 5 |
| `[QiSpark] Chore: Retire QiAccess references` | P1 | Chore | QiSpark | 3 |
| `[QiSpark] Chore: Rename QiNexus references to QiDrive` | P1 | Chore | QiSpark | 3 |
| `[QiSpark] Docs: Move QiDNA doctrine inside QiSpark` | P2 | Docs | QiSpark | 3 |
| `[QiSpark] Docs: Add .why files and root navigation docs` | P2 | Docs | QiSpark | 3 |
| `[QiSpark] Feature: Build local post export/drop-in zip flow` | P2 | Feature | QiSpark | 5 |

## QiDrive / Records / Evidence

| Issue | Priority | Type | App / Area | Estimate |
|---|---:|---|---|---:|
| `[QiDrive] Design: Define evidence storage model` | P1 | Design | QiDrive | 5 |
| `[QiDrive] Feature: Link records, events, tags, and attachments` | P1 | Feature | QiDrive | 5 |
| `[QiDrive] Chore: Create import, log, and reject folders for ingestion` | P2 | Chore | QiDrive | 3 |
| `[QiDrive] Feature: Build standalone recursive ingestor` | P2 | Feature | QiDrive | 8 |
| `[QiDrive] Docs: Add transcript/audio storage rules` | P2 | Docs | QiDrive | 3 |

## Workspace / GitHub / Repo Operations

| Issue | Priority | Type | App / Area | Estimate |
|---|---:|---|---|---:|
| `[QiLabs] Docs: Add lean GitHub Project workflow` | P1 | Docs | QiLabs | 1 |
| `[QiLabs] Chore: Create standard GitHub issue templates` | P1 | Chore | QiLabs | 2 |
| `[QiLabs] Chore: Clean approved root folder structure` | P1 | Chore | QiLabs | 5 |
| `[QiLabs] Docs: Add repo README and short description standards` | P2 | Docs | QiLabs | 2 |
| `[QiLabs] Chore: Add validation scripts for project health checks` | P2 | Chore | QiLabs | 5 |
| `[QiLabs] Chore: Align GitHub labels with project fields` | P3 | Chore | QiLabs | 2 |

---

# Suggested First Pass

Add the issues in batches. Do not add bodies yet.

Recommended batch order:

1. QiOS / Toolbox
2. QiServer / Supabase / Cloudflare
3. QiFi / Finance App
4. QiSpark / Docs / Public Site
5. QiDrive / Records / Evidence
6. QiLife / Cadence / Planner
7. QiMemory
8. QiCare
9. Workspace / GitHub / Repo Operations

---

# Promotion Rule

When an item is ready to leave Triage:

1. Set `Status = Ready`
2. Leave `Iteration` blank if it is not this week
3. Add acceptance criteria
4. Add sub-issues only if estimate is `8`

If it is going into Current:

1. Set `Iteration = current`
2. Keep active Current items tight
3. Do not put more than 3 major items in progress

---

# Do Not Overbuild Yet

Skip these for now:

- Roadmap view
- Releases view
- Agent Queue view
- Agent Sessions field
- Impact field
- Confidence field
- Release Target field

Those can come later when the board has real activity.
