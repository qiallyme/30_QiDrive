---
layout: page
title: Git LFS Setup Guide
slug: git-lfs-setup-guide
status: publish
updated_at: "2026-06-29"
tags:
  - projects
source_type: manual
summary: ""
created_at: ""
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
template_key: master-template
---

# Git LFS Setup Guide

## One-Time Initialization

```bash
git lfs install
```

This sets up Git LFS for your user account.

## What's Configured

### 1. `.gitattributes` - Baseline LFS Tracking

Common binary file types are configured to use LFS:
- PDF, images (PNG, JPG, GIF)
- Videos (MP4, MOV)
- Audio (WAV)
- Archives (ZIP)
- Office docs (PPTX, DOCX)
- Design files (PSD)

### 2. Pre-Commit Hook (`.git/hooks/pre-commit.ps1`)

- **Auto-tracks** files ≥80MB with Git LFS by extension
- **Hard blocks** files ≥100MB (GitHub's limit)
- **Warnings** for files 80-99MB
- Preserves existing Obsidian attachment mirror functionality

### 3. Pre-Push Hook (`.git/hooks/pre-push.ps1`)

- **Size check**: Scans for blobs ≥100MB in the push
- **QiCodex validation**: Ensures codex compliance
- Blocks push if either check fails

### 4. Large File Audit (`large_file_audit.py`)

- Scans repository for files ≥50MB
- Writes report to `.housekeeping/large_files.json`
- Integrated into housekeeper workflow
- Shown in `STATUS_DASHBOARD.md`

## How It Works

### Automatic LFS Tracking

When you commit a file ≥80MB:
1. Hook detects the large file
2. Automatically adds `*.ext` to `.gitattributes` (or exact path if no extension)
3. Re-stages the file so it's stored as an LFS pointer
4. Commit proceeds normally

### Size Limits

- **< 80MB**: Commits normally
- **80-99MB**: Auto-tracked with LFS, warning shown
- **≥ 100MB**: **Blocked** - must split or use LFS manually before committing

### Pre-Push Guard

Before pushing, checks:
1. No blobs ≥100MB in the push range
2. QiCodex validation passes

If either fails, push is blocked.

## Usage

### Normal Workflow

Just commit as usual. Large files are automatically handled:

```bash
git add large-file.pdf  # If ≥80MB, auto-tracked
git commit -m "Add large file"
git push origin main
```

### Manual LFS Tracking

If you want to track a file type before it's large:

```bash
git lfs track "*.myext"
git add .gitattributes
```

### View LFS Files

```bash
git lfs ls-files
```

### Check LFS Status

```bash
git lfs status
```

## Large File Audit

The audit runs automatically during housekeeping. To run manually:

```bash
python 7_Tools/7.10_python/large_file_audit.py
```

Results are in `.housekeeping/large_files.json` and shown in `STATUS_DASHBOARD.md`.

## Troubleshooting

### "git-lfs not found"

Install Git LFS:
```bash

# Windows (Chocolatey)

choco install git-lfs

# Or download from: https://git-lfs.github.com/

```

Then run:
```bash
git lfs install
```

### "Large file blocked"

If you need to commit a file ≥100MB:
1. Split it into smaller chunks, OR
2. Use Git LFS manually: `git lfs track "path/to/file"`

### "Pre-commit hook failed"

Check the error message. Common issues:
- File ≥100MB (must split or use LFS)
- Git LFS not installed
- PowerShell execution policy (should be handled by `-ExecutionPolicy Bypass`)

## FAQ

**Q: Will large files still be on GitHub-**
A: Yes—Git LFS stores them in GitHub's LFS storage (still "on GitHub"). Regular Git history stays fast.

**Q: What about quotas-**
A: GitHub LFS has storage/bandwidth quotas tied to your plan. Monitor usage in repository settings.

**Q: Do I have to manually run `git lfs track`-**
A: No—the pre-commit hook auto-tracks by extension (or exact path) when a staged file ≥80MB.

**Q: Can I disable LFS for specific files-**
A: Yes, add to `.gitattributes`:
```
path/to/file -filter -diff -merge
```
