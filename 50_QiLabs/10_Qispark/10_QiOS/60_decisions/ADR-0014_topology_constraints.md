---
layout: adr
title: ADR-0014: Topology Constraints
slug: adr-0014-topology-constraints
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
uid: 37b388ee94694eb2a6f69b7b103f91f8
canonical_ref: ""
template_key: master-template
---

# ADR-0014: Topology Constraints

## Status

Accepted.

## Context

QiOS documentation is intended to remain flat, but legacy and imported trees include deeper nesting, including tracked personal media beyond four directory levels.

## Decision

- Governed QiDNA paths may be at most four directories below the repository root.
- Deeper paths require documented operational necessity; categorization alone is insufficient.
- Prefer links, metadata, and indexes over repeated nesting.
- Report existing violations before changing them. Flattening, moving, or deleting requires a reviewed change.

## Rationale

The limit keeps locations memorable, reduces duplicate taxonomies, and supports one generated documentation view.

## Consequences

- Audits flag depth violations.
- New documentation does not deepen legacy trees.
- Imported evidence may remain unchanged until classified, but it is not a canonical topology model.
