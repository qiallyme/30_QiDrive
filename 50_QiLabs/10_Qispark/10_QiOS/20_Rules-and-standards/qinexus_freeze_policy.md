---
layout: page
title: Qinexus Freeze Policy
slug: ""
summary: ""
status: publish
created_at: ""
updated_at: ""
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Phase 0 — Freeze and Protect (QiNexus)

Goal: prevent accidental loss during reorganization.

**Mandatory Rules:**
- Do not delete anything.
- Do not let an AI move files directly.
- Create and use the `13_system/qinexus_cleanup/` folder.
- Generate manifests and reports before any moves.

### Cleanup System Structure
Located at `50_QiNexus/My Drive/13_system/qinexus_cleanup/`:
- `rules/`: Governance and movement criteria.
- `reports/`: Audit results and analysis.
- `manifests/`: Snapshots of directory state.
- `quarantine/`: Staging for disputed or risky items.
- `scripts/`: Automation for audit and verification.
- `approved_moves/`: Verified move instructions for human execution.
