---
layout: adr
title: ADR-0008: QiLabs as Canonical Local Workstation Root
slug: adr-0008-qilabs-as-canonical-local-workstation-root
status: publish
updated_at: "2026-07-16T06:49:38-04:00"
tags: []
  - qispark
  - decisions
source_type: manual
summary: ""
created_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: f5060c8c9b7a46ff8234a079ceb686d5
canonical_ref: ""
template_key: master-template
---

# ADR-0008: QiLabs as Canonical Local Workstation Root

## Context

The architecture historically defined the developer/operator machine with a local state rooted at `C:/QiData/`. However, the ecosystem has evolved to encompass `QiArchive` (the system/spine concept) as well as the monorepo platform (`QiOne`). These are not simply sibling root folders but need to be part of a structured canonical machine-local ecosystem.

## Decision

* `QiLabs` will serve as the canonical machine root for local workstations.
* `QiData` (the state directory) will live directly under `QiLabs` (`C:/QiLabs/QiData`).
* `_QiOne_MonoRepo` will live under `QiLabs` (`C:/QiLabs/_QiOne_MonoRepo`).
* `QiArchive` represents a system/spine concept, not a literal sibling root directory.

## Rationale

This aligns the workstation filesystem with the system architecture model. By encapsulating everything within `QiLabs`, `QiOne` functions fully as the monorepo platform and `QiData` functions as local state, while preventing fragmentation across the machine.
