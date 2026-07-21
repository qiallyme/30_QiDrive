---
layout: page
title: "Unzipping Files One by One"
slug: "unzipping_files_one_by_one"
created_at: "2026-06-14 19:44:32"
updated_at: "2026-07-18T11:03:16-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-009.json"
template_key: master-template
date: 2026-06-14
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a2f4ace-8d70-83ea-aed1-80a84abed3c2"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Unzipping Files One by One

## Overview
- **Date**: 2026-06-14 19:44:32
- **Conversation ID**: `6a2f4ace-8d70-83ea-aed1-80a84abed3c2`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> ok so in htis folder i have take out from google but not enough space on my drive to actually unzip it all, i need to unzip one at a time, delete the old zip folder, empty recycle bin, then repeat until all are unzipped "C:\QiLabs\50_QiNexus\My Drive\00_inbox\10_ingestion\20_drive_imports\Takeout"

### Assistant
> You’re right: this needs a controlled one-at-a-time extraction, not “select all unzip” chaos. The key correction: **don’t send the zip to Recycle Bin** if space is tight — permanently delete it only after the extraction succeeds.

### Assistant
> Yes. Use this **PowerShell script**. It will:
> 
> 1. Empty Recycle Bin first.
> 2. Find all `.zip` files in that Takeout folder.
> 3. Unzip **one at a time** into `_extracted`.
> 4. Delete the zip **only after successful extraction**.
> 5. Empty Recycle Bin again after each zip.
> 6. Stop if one fails, so you don’t lose anything.
> 
> Paste this into PowerShell:
> 
> ```powershell
> $Root = "C:\QiLabs\50_QiNexus\My Drive\00_inbox\10_ingestion\20_drive_imports\Takeout"
> $ExtractTo = Join-Path $Root "_extracted"
> $Log = Join-Path $Root "_takeout_unzip_log.txt"
> 
> New-Item -ItemType Directory -Path $ExtractTo -Force | Out-Null
> 
> "=== Google Takeout unzip started: $(Get-Date) ===" | Out-File $Log -Append
> 
> Write-Host "Emptying Recycle Bin first..."
> Clear-RecycleBin -Force -ErrorAction SilentlyContinue
> 
> $SevenZipCandidates = @(
>   "$env:ProgramFiles\7-Zip\7z.exe",
>   "${env:ProgramFiles(x86)}\7-Zip\7z.exe"
> )
> 
> $SevenZip = $SevenZipCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
> 
> $Zips = Get-ChildItem -Path $Root -Filter "*.zip" -File | Sort-Object Name
> 
> if ($Zips.Count -eq 0) {
>   Write-Host "No zip files found in $Root"
>   exit
> }
> 
> Write-Host "Found $($Zips.Count) zip files."
> Write-Host "Extracting to: $ExtractTo"
> 
> foreach ($Zip in $Zips) {
>   Write-Host ""
>   Write-Host "========================================"
>   Write-Host "Extracting: $($Zip.Name)"
>   Write-Host "Size: $([math]::Round($Zip.Length / 1GB, 2)) GB"
>   Write-Host "========================================"
> 
>   "Extracting $($Zip.FullName) at $(Get-Date)" | Out-File $Log -Append
> 
>   try {
>     if ($SevenZip) {
>       & $SevenZip x "$($Zip.FullName)" "-o$ExtractTo" -aos
> 
>       if ($LASTEXITCODE -ne 0) {
>         throw "7-Zip failed with exit code $LASTEXITCODE"
>       }
>     }
>     else {
>       Expand-Archive -LiteralPath $Zip.FullName -DestinationPath $ExtractTo -ErrorAction Stop
>     }
> 
>     Write-Host "Extraction succeeded. Deleting zip permanently..."
>     Remove-Item -LiteralPath $Zip.FullName -Force
> 
>     "Deleted $($Zip.FullName) at $(Get-Date)" | Out-File $Log -Append
> 
>     Write-Host "Emptying Recycle Bin..."
>     Clear-RecycleBin -Force -ErrorAction SilentlyContinue
> 
>     Write-Host "Done with $($Zip.Name)"
>   }
>   catch {
>     Write-Host ""
>     Write-Host "FAILED on: $($Zip.Name)" -ForegroundColor Red
>     Write-Host "Zip was NOT deleted." -ForegroundColor Yellow
>     Write-Host $_.Exception.Message -ForegroundColor Red
> 
>     "FAILED $($Zip.FullName) at $(Get-Date): $($_.Exception.Message)" | Out-File $Log -Append
>     break
>   }
> }
> 
> "=== Google Takeout unzip ended: $(Get-Date) ===" | Out-File $Log -Append
> 
> Write-Host ""
> Write-Host "Process complete or stopped safely."
> Write-Host "Log file: $Log"
> ```
> 
> **Important correction, girl:** deleting to Recycle Bin does **not** free usable disk space until it’s emptied. This script does a **permanent delete after successful unzip**, which is what you actually need.
> 
> Your extracted files will land here:
> 
> ```text
> C:\QiLabs\50_QiNexus\My Drive\00_inbox\10_ingestion\20_drive_imports\Takeout\_extracted
> ```
> 
> If one zip expands larger than your available free space, this will still fail. But it will fail safely and keep that zip intact.
