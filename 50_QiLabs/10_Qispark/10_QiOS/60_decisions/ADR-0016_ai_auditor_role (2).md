---
layout: page
title: Adr 0016 Ai Auditor Role
slug: adr-0016-ai-auditor-role
summary: ""
status: publish
created_at: "2026-07-16T06:19:39-04:00"
updated_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 7a48e21fca6644fbb475edc778abfea2
canonical_ref: ""
source_type: manual
template_key: master-template
---

# ADR-0016: AI as Auditor, Not Authority

## Status

Accepted.

## Context

QiOS uses Codex and other AI services to inspect repositories, interpret captures, draft structures, and propose changes. QiCapture and QiLife already require human review before AI output becomes official.

## Decision

AI acts as auditor, analyst, and draft author. It may collect evidence, identify conflicts, generate reports, and prepare proposed changes. It may not declare runtime facts, promote drafts to doctrine, delete canonical material, or approve high-impact records without human review or an explicit trusted automation rule.

## Rationale

AI improves consistency and scale but can be incomplete or wrong. QiDNA must remain traceable to repository evidence, runtime verification, accepted decisions, and accountable approval.

## Consequences

- AI reports identify unknowns and unavailable evidence.
- Accepted ADRs and merged source documents, not chat output, carry authority.
- Destructive or topology-changing recommendations require explicit review.
- Runtime facts override AI inference and stale planning notes.
