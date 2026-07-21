---
layout: page
title: Readme
slug: readme
summary: ""
status: active
created_at: "2026-07-16T06:19:39-04:00"
updated_at: "2026-07-18T11:03:16-04:00"
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 83c838c4a9a2411db087f7997d03303e
canonical_ref: ""
source_type: manual
template_key: master-template
type: note
---

# Story Bible Template Pack

This pack gives you two ways to create a story bible.

## Option 1 — Run the PowerShell script

1. Copy `Create-StoryBible.ps1` into the series or book folder.
2. Open PowerShell in that folder.
3. Run:

```powershell
powershell -ExecutionPolicy Bypass -File .\Create-StoryBible.ps1
```

The script creates `00_bible` in the current folder and adds only files that do not already exist.

It will not overwrite:
- an existing `00_bible` folder
- an existing bible file
- any other content in the project folder

## Option 2 — Copy the template folder

Copy the included `00_bible` folder into a series or book folder.

Windows will prompt you if files already exist. Choose the option that preserves existing files.

## Option 3 — Use the single-file template

Open `Story_Bible_Master_Template.md`, copy it, rename it, and use it as a compact bible when a full folder is unnecessary.
