---
layout: page
title: Adr 0013 Folder Documentation Model
slug: adr-0013-folder-documentation-model
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
uid: 2ab7465fba4e4e93948d9d4a3ad9cd23
canonical_ref: ""
source_type: manual
template_key: master-template
---

# ADR-0013: Folder Documentation Model

## Status

Accepted.

## Context

Active domains use files such as `_10_QiAccess.md`, while legacy trees use `_index.md`, `index.mdx`, or no folder descriptor.

## Decision

Every governed folder has one underscore-prefixed Markdown descriptor named for the folder. Numbered folders retain their number, for example `_10_QiAccess.md`.

The descriptor contains Overview, Responsibilities, Flows, and Structure as needed. Topic documents and ADRs may coexist, but multiple competing folder descriptors may not.

## Rationale

A predictable descriptor makes each folder self-explaining and gives build and audit tools a stable discovery rule.

## Consequences

- New governed folders require a descriptor when activated.
- Existing `_index.md` and `index.mdx` files require review before merge or replacement.
- Generated, imported-media, dependency, and Git-internal folders are outside this rule unless promoted into governed QiDNA.
