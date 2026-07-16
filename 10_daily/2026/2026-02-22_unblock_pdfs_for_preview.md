---
layout: page
title: "Unblock PDFs for Preview"
slug: "unblock_pdfs_for_preview"
created_at: "2026-02-22 04:52:25"
updated_at: "2026-07-16T06:49:30-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-004.json"
template_key: master-template
date: 2026-02-22
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "699adfe1-ba9c-832d-b6c5-429ea27c61ef"
canonical_ref: ""
---

# Unblock PDFs for Preview

## Overview
- **Date**: 2026-02-22 04:52:25
- **Conversation ID**: `699adfe1-ba9c-832d-b6c5-429ea27c61ef`
- **Source**: `Chat-Export-28513-2026/conversations-004.json`

## Chat History

### User
> WHATS THE COMMAND TO UNBLOCK ALL PDF TO THE SHOW UP IN THE PREVIEW

### Assistant
> If you’re on **Windows** and PDFs aren’t previewing because they’re “blocked” (downloaded from the internet), here are the exact commands.
> 
> ## Unblock a Single PDF (PowerShell)
> 
> ```powershell
> Unblock-File "C:\Path\To\Your\File.pdf"
> ```
> 
> ## Unblock All PDFs in a Folder
> 
> ```powershell
> Get-ChildItem "C:\Path\To\Folder" -Filter *.pdf | Unblock-File
> ```
> 
> ## Unblock All PDFs Recursively (including subfolders)
> 
> ```powershell
> Get-ChildItem "C:\Path\To\Folder" -Filter *.pdf -Recurse | Unblock-File
> ```
> 
> ---
> 
> If the issue is **Explorer Preview Pane not showing PDFs**, also check:
> 
> 1. Open File Explorer  
> 2. View → Preview Pane  
> 3. Make sure **Adobe Acrobat** (or your PDF viewer) is set as default  
> 4. In Adobe: Edit → Preferences → General → enable **“Enable PDF thumbnail previews in Windows Explorer”**
> 
> If that’s not the scenario, tell me:
> - Windows or Mac?
> - Is it a browser preview issue or File Explorer preview issue?
> - Any error message?
