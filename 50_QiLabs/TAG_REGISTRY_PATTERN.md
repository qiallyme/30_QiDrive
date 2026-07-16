---
layout: page
title: Tag Registry Pattern
slug: tag-registry-pattern
summary: ""
status: active
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
uid: 079c150c978d4eeba2ddba159d6e9990
canonical_ref: ""
source_type: manual
template_key: master-template
---

# QiLabs Tag Registry Pattern

## Correct model

Use a lean global registry plus folder-level overlays.

```txt
C:\QiLabs\_qiconfig\tags.json                  # global base registry
C:\QiLabs\40_QiVault\Some_Project\tags.json   # optional overlay
C:\QiLabs\40_QiVault\Some_Project\Sub\tags.json # narrower overlay
```

## Merge behavior

For each Markdown file:

1. Load the global registry.
2. Walk from the repo/vault root to the file folder.
3. Merge every discovered overlay `tags.json`.
4. Validate the note tags against the effective registry.
5. Apply folder defaults only for the folder where they match.
6. Never delete unknown tags automatically. Flag them in the report.

## Minimum and maximum tags

Global policy:

- minimum: 3
- default maximum: 8
- absolute maximum: 12

Overlay policy:

- can raise the effective maximum using `max_bonus`
- cannot exceed the global absolute maximum
- can define project defaults without changing the global registry

## Why this is better

The global file stays clean. Projects like Lisa Care Record, QiCode legal doctrine, client files, finance, and evidence binders can each carry their own specialized tags without turning the entire vault into a tag swamp.
