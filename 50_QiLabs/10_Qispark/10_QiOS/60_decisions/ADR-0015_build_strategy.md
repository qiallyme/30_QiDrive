---
layout: adr
title: ADR-0015: Markdown to Single HTML Build
slug: adr-0015-markdown-to-single-html-build
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
uid: 5bb63b0d61894d4e92f1c9f78e5d20bf
canonical_ref: ""
template_key: master-template
---

# ADR-0015: Markdown to Single HTML Build

## Status

Accepted.

## Context

The repository has a small Node build that discovers Markdown and renders `site/index.html`. It also contains Mintlify navigation configuration and a Python chronicle generator. Multiple publication models can create conflicting navigation and authority.

## Decision

Canonical documentation remains Markdown or MDX in its owning folders. The supported reader build is one generated static HTML file at `site/index.html`, produced by `npm run build`.

The reader provides two coordinated navigation modes:

- a cascading left-side directory tree that mirrors repository folders
- an optional center-screen mind map that expands folders and opens document pages

HTML, chronicles, manifests, indexes, and external publications are derived outputs and do not become canonical by being generated or deployed.

## Rationale

The existing build is lightweight, searchable, portable, and introduces no additional documentation framework.

## Consequences

- Stale required paths are corrected when source documents move.
- Markdown and MDX coverage is required.
- The directory tree and mind map derive from the same repository paths and document-status rules.
- The directory tree remains the primary navigator; the mind map is a secondary visual view.
- Selecting a document from either navigation mode opens the same rendered document section.
- `docs.json` and wiki plans remain secondary until aligned with this decision.
