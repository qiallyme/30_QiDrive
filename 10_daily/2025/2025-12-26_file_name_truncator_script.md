---
layout: page
title: "File Name Truncator Script"
slug: "file_name_truncator_script"
created_at: "2025-12-26 12:35:36"
updated_at: "2026-07-16T06:49:29-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-002.json"
template_key: master-template
date: 2025-12-26
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "694ed55e-98c4-8330-a510-6f947c260cfa"
canonical_ref: ""
---

# File Name Truncator Script

## Overview
- **Date**: 2025-12-26 12:35:36
- **Conversation ID**: `694ed55e-98c4-8330-a510-6f947c260cfa`
- **Source**: `Chat-Export-28513-2026/conversations-002.json`

## Chat History

### User
> give me a quick script i can run inside a folder that will truncate the file name down to 25 characters while preserving the extension.

### Assistant
> Here is a **clean, safe, no-nonsense solution**. Pick the one that matches your OS. Both **run inside the folder**, preserve extensions, and **hard-cap filenames at 25 characters total** (base name + extension).
> 
> ---
> 
> ## Windows (PowerShell) — recommended for you
> 
> **What it does**
> - Truncates filenames to **25 characters max**
> - Preserves the file extension
> - Skips files that are already compliant
> - Prevents extension loss
> - Safe for batch execution
> 
> ### Run this inside the target folder
> ```powershell
> Get-ChildItem -File | ForEach-Object {
>     $maxLength = 25
>     $ext = $_.Extension
>     $baseMax = $maxLength - $ext.Length
> 
>     if ($_.Name.Length -gt $maxLength -and $baseMax -gt 0) {
>         $newBase = $_.BaseName.Substring(0, [Math]::Min($baseMax, $_.BaseName.Length))
>         $newName = "$newBase$ext"
> 
>         if (-not (Test-Path $newName)) {
>             Rename-Item $_.FullName $newName
>         }
>     }
> }
> ```
> 
> ### Dry-run (preview only)
> If you want to **see changes before committing**:
> ```powershell
> Get-ChildItem -File | ForEach-Object {
>     $maxLength = 25
>     $ext = $_.Extension
>     $baseMax = $maxLength - $ext.Length
> 
>     if ($_.Name.Length -gt $maxLength -and $baseMax -gt 0) {
>         $newBase = $_.BaseName.Substring(0, [Math]::Min($baseMax, $_.BaseName.Length))
>         "$($_.Name)  ->  $newBase$ext"
>     }
> }
> ```
> 
> ---
> 
> ## macOS / Linux (Bash)
> 
> ```bash
> for f in *.*; do
>   ext="${f##*.}"
>   base="${f%.*}"
>   max=25
>   newbase="${base:0:$((max - ${#ext} - 1))}"
>   new="$newbase.$ext"
> 
>   [ "$f" != "$new" ] && mv -n "$f" "$new"
> done
> ```
> 
> ---
> 
> ## Important Notes (read this)
> - **25 characters is total filename length**, not just the base name.
> - This does **not** auto-dedupe collisions. If two files truncate to the same name, the second is skipped (by design).
> - If you want **hash suffixes**, **incrementing numbers**, or **QiDecimal IDs appended**, say so and I’ll give you the exact variant.
> 
> If you want this wrapped as:
> - a `.ps1` utility  
> - a reversible rename (log + undo)  
> - or QiNote / QiVault-safe (ID-aware)
> 
> say the word.

### User
> i need to clear my git cach since imade updates to the gitignore file so i can retry my commit.

### Assistant
> Here’s the **exact, correct sequence**. No fluff.
> 
> You updated `.gitignore`, but Git is still tracking files that were already committed. You need to **remove them from the index**, not from disk.
> 
> ---
> 
> ## Clear Git cache (respecting new `.gitignore`)
> 
> Run this **from the repo root**:
> 
> ```bash
> git rm -r --cached .
> git add .
> git commit -m "chore: reapply .gitignore and clear tracked cache"
> ```
> 
> That’s it. This:
> - Clears the index
> - Re-applies `.gitignore`
> - Keeps your local files intact
> - Lets you retry the commit cleanly
> 
> ---
> 
> ## If you haven’t committed yet (safer reset)
> 
> If your failed commit didn’t go through and you just want to retry:
> 
> ```bash
> git reset
> git rm -r --cached .
> git add .
> ```
> 
> Then review:
> 
> ```bash
> git status
> ```
> 
> Commit when satisfied.
> 
> ---
> 
> ## Verify what’s still tracked (sanity check)
> 
> ```bash
> git ls-files | grep -v -f .gitignore
> ```
> 
> If anything shows up that shouldn’t, your `.gitignore` rules are wrong — not Git.
> 
> ---
> 
> ## Common mistakes (don’t do these)
> - ❌ Deleting files manually
> - ❌ Re-cloning the repo (waste of time)
> - ❌ Expecting `.gitignore` to untrack existing files automatically
> 
> ---
> 
> ## If this is a **Quartz / Astro / Node repo**
> You *should* be ignoring at minimum:
> 
> ```gitignore
> node_modules/
> dist/
> .build/
> .cache/
> .quartz/
> .obsidian/
> .DS_Store
> .env
> ```
> 
> If you want, paste your `.gitignore` here and I’ll audit it fast and tell you exactly what’s wrong or missing.

### User
> ok so i go to push and its still talking about lfs, but when i look at the tree the folder with all the large files are ignored yet my git is like 6.4 gbs.

### Assistant
> What you’re seeing is normal: **.gitignore only stops new files from being added.** If those large files were *ever* committed (or added and then committed), they’re already in your repo history (or LFS pointers), and your local `.git/` directory stays huge.
> 
> Also: even if the folder is now ignored, Git can still be tracking:
> - the files (normal Git blobs), or
> - LFS pointers + local LFS objects (`.git/lfs/objects`), or
> - both (because of history).
> 
> Here’s the fastest way to diagnose and fix it.
> 
> ---
> 
> ## 1) Confirm what’s using space (Git objects vs LFS objects)
> 
> Run from repo root:
> 
> ```bash
> git rev-parse --is-inside-work-tree
> du -sh .git
> du -sh .git/lfs 2>/dev/null || echo "No .git/lfs folder"
> ```
> 
> If `.git/lfs` is huge, you’ve got local LFS objects stored.
> 
> ---
> 
> ## 2) See what Git thinks is LFS-tracked right now
> 
> ```bash
> git lfs version
> git lfs env
> git lfs ls-files
> git lfs track
> ```
> 
> - If `git lfs ls-files` shows files, Git will keep bringing up LFS.
> - If it shows nothing but you still see LFS warnings, your repo may still have LFS config/hooks set up or history contains LFS pointers.
> 
> Also check attributes (this is the real source of truth for LFS tracking rules):
> 
> ```bash
> cat .gitattributes
> ```
> 
> If you see lines like `*.psd filter=lfs diff=lfs merge=lfs -text`, you’re in LFS-land.
> 
> ---
> 
> ## 3) If the big files are already tracked (most likely): untrack them *now*
> 
> This removes them from the index for the current snapshot (does not remove history yet):
> 
> ```bash
> git rm -r --cached path/to/that/folder
> git add .gitignore .gitattributes
> git commit -m "stop tracking large files (ignored going forward)"
> ```
> 
> Then try pushing again.
> 
> But: **your repo can still be massive** because history still contains them.
> 
> ---
> 
> ## 4) If you want the repo to stop being 6.4GB: you must rewrite history
> 
> There are two main cases:
> 
> ### Case A — You want to keep LFS, but clean it up
> This is usually easiest.
> 
> ```bash
> git lfs prune
> ```
> 
> That clears *unreferenced* LFS objects locally. It won’t shrink history stored remotely if those objects are referenced.
> 
> ### Case B — You want to remove the big files from history entirely (shrink repo)
> You need a history rewrite. The modern tool is `git filter-repo`.
> 
> **Install:** (one-time; if you don’t have it)
> ```bash
> git filter-repo --help
> ```
> 
> If that errors, you don’t have it installed.
> 
> **Remove a folder from all history:**
> ```bash
> git filter-repo --path path/to/that/folder --invert-paths
> ```
> 
> Then you must force push (because history changed):
> ```bash
> git push --force --all
> git push --force --tags
> ```
> 
> If you’re using GitHub and others are collaborating, this will break their clones until they rebase/re-clone.
> 
> ---
> 
> ## 5) If you want to stop using LFS entirely (optional)
> 
> If you never intended to use LFS and just want Git to stop mentioning it:
> 
> ```bash
> git lfs uninstall
> ```
> 
> But note: if your history contains LFS pointers, that doesn’t magically convert them back.
> 
> Also remove LFS rules (only if you truly don’t want LFS):
> - delete the LFS lines in `.gitattributes`
> - commit the change
> 
> ---
> 
> ## 6) Quick “tell me exactly what is huge” command
> 
> This shows the largest objects in Git history (non-LFS blobs):
> 
> ```bash
> git rev-list --objects --all |
>   git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
>   sed -n 's/^blob //p' |
>   sort -nr -k2 |
>   head -20
> ```
> 
> If that list contains your “ignored” folder files, they’re in history, period.
> 
> ---
> 
> ## The blunt truth
> If your repo is **6.4GB**, one of these is true:
> 1) You committed large files at some point, and they’re in history, or  
> 2) LFS pulled large objects into `.git/lfs/objects`, or  
> 3) Both.
> 
> Ignoring the folder now doesn’t change any of that.
> 
> ---
> 
> ## If you paste 3 outputs, I’ll tell you the exact next command set
> Paste the output of:
> 
> 1) `du -sh .git .git/lfs 2>/dev/null`  
> 2) `git lfs ls-files`  
> 3) `cat .gitattributes`
> 
> …and I’ll tell you whether you should prune, untrack, or rewrite history (and which exact command is safest for your situation).

### User
> how do i make sure this path is ignored. "C:\QiOS_v1\projects\FCFCU_Case_Quartz\content\case_fcfcu_v_codyrv\20_evidence_vault\20_RAW"

### Assistant
> Short answer: **Git ignores paths relative to the repo root, not absolute Windows paths.**  
> So `"C:\QiOS_v1\projects\FCFCU_Case_Quartz\..."` will **never** match.
> 
> You must ignore it **relative to the repository root**.
> 
> ---
> 
> ## Step 1: Identify the repo root
> From inside the repo, run:
> ```bash
> git rev-parse --show-toplevel
> ```
> 
> Assuming it returns:
> ```
> C:/QiOS_v1/projects/FCFCU_Case_Quartz
> ```
> 
> That means your `.gitignore` paths start **from there**.
> 
> ---
> 
> ## Step 2: Add the correct ignore rule
> 
> In `.gitignore`, add **one of the following** (pick the level you want):
> 
> ### Ignore JUST the RAW folder
> ```gitignore
> /content/case_fcfcu_v_codyrv/20_evidence_vault/20_RAW/
> ```
> 
> ### Ignore EVERYTHING inside it (explicit, safer)
> ```gitignore
> /content/case_fcfcu_v_codyrv/20_evidence_vault/20_RAW/**
> ```
> 
> ### Ignore the entire evidence vault (recommended for sanity)
> ```gitignore
> /content/case_fcfcu_v_codyrv/20_evidence_vault/
> ```
> 
> Git uses **forward slashes only**, even on Windows.
> 
> ---
> 
> ## Step 3: Verify Git sees it as ignored
> 
> ```bash
> git check-ignore -v content/case_fcfcu_v_codyrv/20_evidence_vault/20_RAW/somefile.ext
> ```
> 
> If ignored correctly, Git will tell you **which line** in `.gitignore` is doing it.
> 
> If nothing prints → it is **not** ignored.
> 
> ---
> 
> ## Step 4 (critical): If it was EVER tracked, ignoring is not enough
> 
> If those files were already added before you updated `.gitignore`, you must untrack them:
> 
> ```bash
> git rm -r --cached content/case_fcfcu_v_codyrv/20_evidence_vault/20_RAW
> git commit -m "stop tracking RAW evidence vault"
> ```
> 
> This does **not delete local files**.
> 
> ---
> 
> ## Step 5: Confirm nothing under it is tracked
> 
> ```bash
> git ls-files | grep 20_evidence_vault
> ```
> 
> If anything shows up → Git is still tracking it.
> 
> ---
> 
> ## Hard truth (important)
> - `.gitignore` prevents **future tracking**
> - It does **nothing** to history
> - Your 6.4 GB repo means those files are **already in history or LFS**
> - Ignoring fixes *future commits*, not repo size
> 
> If you want, next we can:
> - audit your `.gitignore` fully
> - clean LFS properly
> - or surgically remove that folder from history (safe or aggressive options)
> 
> Tell me which direction you want to go.

### User
> heres my current index.md file i need to udpate it for quartz 4. ---

> title: Case Hub

> layout: basic

> ---

> 

> <header style="margin: 20px 0 30px; text-align: left;">

>   <h1 style="font-size: 1.8rem; font-weight: 800; margin: 0;">Case Hub</h1>

>   <p style="color: var(--gray); font-size: 0.9rem; margin: 5px 0 0;">FCFCU v. Cody • Legal Repository</p>

> </header>

> 

> <div class="case-grid" style="display: grid; grid-template-columns: 1fr; gap: 12px; width: 100%;">

> 

>   <a href="/00_admin/40_action_center/" style="text-decoration: none; color: inherit;">

>     <div style="background: var(--secondary); padding: 18px; border-radius: 16px; display: flex; align-items: center; gap: 16px; color: white;">

>       <div style="width: 44px; height: 44px; background: rgba(255,255,255,0.2); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 800;">⚡</div>

>       <div>

>         <h2 style="font-size: 1rem; margin: 0; color: white;">Action Center</h2>

>         <p style="font-size: 0.85rem; margin: 2px 0 0; color: rgba(255,255,255,0.8);">Pre-hearing checklists & strategy</p>

>       </div>

>     </div>

>   </a>

> 

>   <a href="/10_filings/" style="text-decoration: none; color: inherit;">

>     <div style="background: var(--light); border: 1px solid var(--lightgray); padding: 18px; border-radius: 16px; display: flex; align-items: center; gap: 16px;">

>       <div style="width: 44px; height: 44px; background: var(--highlight); color: var(--secondary); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 800;">10</div>

>       <div>

>         <h2 style="font-size: 1rem; margin: 0;">Filings</h2>

>         <p style="font-size: 0.85rem; margin: 2px 0 0; color: var(--gray);">Drafts, exhibits, and filed receipts</p>

>       </div>

>     </div>

>   </a>

> 

>   <a href="/20_evidence_vault/" style="text-decoration: none; color: inherit;">

>     <div style="background: var(--light); border: 1px solid var(--lightgray); padding: 18px; border-radius: 16px; display: flex; align-items: center; gap: 16px;">

>       <div style="width: 44px; height: 44px; background: var(--highlight); color: var(--secondary); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 800;">20</div>

>       <div>

>         <h2 style="font-size: 1rem; margin: 0;">Evidence Vault</h2>

>         <p style="font-size: 0.85rem; margin: 2px 0 0; color: var(--gray);">Raw photos, video, and exhibits A-P</p>

>       </div>

>     </div>

>   </a>

> 

>   <a href="/30_court_record/" style="text-decoration: none; color: inherit;">

>     <div style="background: var(--light); border: 1px solid var(--lightgray); padding: 18px; border-radius: 16px; display: flex; align-items: center; gap: 16px;">

>       <div style="width: 44px; height: 44px; background: var(--highlight); color: var(--secondary); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 800;">30</div>

>       <div>

>         <h2 style="font-size: 1rem; margin: 0;">Court Record</h2>

>         <p style="font-size: 0.85rem; margin: 2px 0 0; color: var(--gray);">Official docket and complete record</p>

>       </div>

>     </div>

>   </a>

> 

>   <a href="/00_admin/05_timeline/" style="text-decoration: none; color: inherit;">

>     <div style="background: var(--light); border: 1px solid var(--lightgray); padding: 18px; border-radius: 16px; display: flex; align-items: center; gap: 16px;">

>       <div style="width: 44px; height: 44px; background: var(--highlight); color: var(--secondary); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 800;">📅</div>

>       <div>

>         <h2 style="font-size: 1rem; margin: 0;">Timeline</h2>

>         <p style="font-size: 0.85rem; margin: 2px 0 0; color: var(--gray);">Chronological log of case events</p>

>       </div>

>     </div>

>   </a>

> 

> </div>

> 

> ---

> 

> ### Strategy & Overviews

> * [[00_admin/20_strategy/index|Case Strategy]]

> * [[00_admin/10_overviews/index|Failure Maps & PDFs]]

> * [[00_admin/00_trackers/index|Financial Tracker & Log]]

### Assistant
> Good news: **your content is solid**. The problem is *structure*, not intent.
> 
> Quartz 4:
> - **Does not like heavy inline HTML**
> - Prefers **pure Markdown + Quartz components**
> - Automatically handles layout, spacing, and theming
> 
> So the fix is to **strip the HTML** and rewrite this using **Quartz-native constructs** (headings, callouts, cards, wikilinks). This will also make it more future-proof and readable in Obsidian.
> 
> Below is a **Quartz 4–clean rewrite** you can drop in as a replacement.
> 
> ---
> 
> ## ✅ Quartz 4–Compatible `index.md` (Recommended)
> 
> ```md
> ---
> title: Case Hub
> ---
> 
> # Case Hub
> *FCFCU v. Cody • Legal Repository*
> 
> ---
> 
> ## Primary Sections
> 
> ### ⚡ [[00_admin/40_action_center/index|Action Center]]
> Pre-hearing checklists, deadlines, and strategic execution.
> 
> ### 📁 [[10_filings/index|Filings]]
> Drafts, exhibits, motions, and filed receipts.
> 
> ### 🧾 [[20_evidence_vault/index|Evidence Vault]]
> Raw photos, video, audio, and labeled exhibits (A–P).
> 
> ### 🏛️ [[30_court_record/index|Court Record]]
> Official docket, orders, notices, and procedural history.
> 
> ### 📅 [[00_admin/05_timeline/index|Timeline]]
> Chronological log of events, filings, and incidents.
> 
> ---
> 
> ## Strategy & Overviews
> 
> - [[00_admin/20_strategy/index|Case Strategy]]
> - [[00_admin/10_overviews/index|Failure Maps & PDFs]]
> - [[00_admin/00_trackers/index|Financial Tracker & Log]]
> ```
> 
> ---
> 
> ## Why this works (important)
> 
> - ✅ **No inline HTML** → Quartz won’t choke
> - ✅ Uses **Obsidian-style wikilinks** → Quartz resolves them correctly
> - ✅ Quartz handles spacing, typography, cards, and theme colors
> - ✅ Clean in Obsidian *and* Quartz
> - ✅ Easy to extend later (cards, callouts, diagrams)
> 
> ---
> 
> ## Optional Upgrade (Quartz “Card” feel without HTML)
> 
> If you want a more “dashboard” feel later, Quartz 4 supports **callouts**, which render nicely:
> 
> ```md
> > [!info] ⚡ Action Center
> > [[00_admin/40_action_center/index|Pre-hearing checklists & strategy]]
> 
> > [!note] 📁 Filings
> > [[10_filings/index|Drafts, exhibits, and receipts]]
> ```
> 
> No CSS. No HTML. No breakage.
> 
> ---
> 
> ## Blunt assessment (truth mode)
> - Your **HTML-heavy version is why Quartz feels weird**
> - Quartz is **not a static HTML site generator** — it’s a knowledge graph renderer
> - Treat it like **Obsidian-first Markdown**, not a webpage
> 
> If you want next:
> - a **Quartz 4 sidebar config**
> - an **index auto-generated from folder structure**
> - or a **Case Hub landing page + public/private split**
> 
> say the word and tell me which direction.

### User
> give me the cool call outs, and yes, sidebar please and index auto generated, yes, a case hub landing page fwith public private split.

### Assistant
> You want four things, and they *do* fit together cleanly in Quartz 4:
> 
> 1) “Cool” callouts on the Case Hub landing page  
> 2) A real sidebar (Explorer)  
> 3) Auto-generated folder index pages  
> 4) A public/private split that doesn’t leak your evidence vault
> 
> Below is the setup that actually works in Quartz 4.5.x. citeturn0search1turn1view1turn1view2turn3search0turn3search7
> 
> ---
> 
> ## 1) Case Hub landing page with “cool” callouts (Quartz 4 compatible)
> 
> Replace your `content/index.md` with this (or adapt paths). Quartz supports Obsidian callout syntax directly. citeturn0search1
> 
> ```md
> ---
> title: Case Hub
> ---
> 
> # Case Hub
> *FCFCU v. Cody • Legal Repository*
> 
> > [!warning] Safety + Exposure Boundary
> > This repo contains sensitive material. Keep **RAW** evidence out of public builds.
> > - Public: sanitized / redacted summaries
> > - Private: full vault (protected)
> 
> ---
> 
> ## Quick Actions
> 
> > [!tip] ⚡ Action Center
> > Pre-hearing checklists, deadlines, and execution.
> > **Go:** [[00_admin/40_action_center/index|Open Action Center]]
> 
> > [!note] 📅 Timeline
> > Chronological case log (events, filings, incidents).
> > **Go:** [[00_admin/05_timeline/index|Open Timeline]]
> 
> > [!info] 🏛️ Court Record
> > Official docket, notices, orders, procedural history.
> > **Go:** [[30_court_record/index|Open Court Record]]
> 
> ---
> 
> ## Core Libraries
> 
> > [!abstract] 📁 Filings
> > Drafts, exhibits, motions, and filed receipts.
> > **Go:** [[10_filings/index|Open Filings]]
> 
> > [!example] 🧾 Evidence Vault
> > Exhibits and supporting material (do **not** publish RAW).
> > **Go:** [[20_evidence_vault/index|Open Evidence Vault]]
> 
> ---
> 
> ## Strategy & Overviews
> 
> > [!success] 🧭 Strategy Pack
> > - [[00_admin/20_strategy/index|Case Strategy]]
> > - [[00_admin/10_overviews/index|Failure Maps & PDFs]]
> > - [[00_admin/00_trackers/index|Financial Tracker & Log]]
> 
> ---
> 
> ## Public vs Private
> 
> > [!question] Public Site (Shareable)
> > Redacted / sanitized pages only.
> > - Use `publish: true` or keep content under `/public`
> > - No RAW uploads, no unredacted PDFs
> 
> > [!danger] Private Site (Protected)
> > Full case vault, including evidence + internal notes.
> > Put behind Cloudflare Access / Zero Trust (recommended).
> ```
> 
> Optional “slick” move: make some callouts collapsible:
> 
> ```md
> > [!danger]- Private Vault Rules (click to expand)
> > - No RAW in public build
> > - Keep `20_RAW` excluded via Quartz `ignorePatterns`
> > - Keep it out of git history if possible
> ```
> 
> ---
> 
> ## 2) Sidebar (Explorer) in Quartz 4
> 
> Quartz’s “sidebar” is controlled in `quartz.layout.ts`, and the Explorer component is the standard navigation sidebar. citeturn1view1turn0search0
> 
> ### Minimal, clean sidebar layout (recommended)
> In `quartz.layout.ts`, ensure you have Explorer in the `left` column:
> 
> ```ts
> import * as Component from "./quartz/components"
> 
> export const defaultContentPageLayout: PageLayout = {
>   left: [
>     Component.Explorer({
>       title: "Case Files",
>       folderClickBehavior: "collapse",
>       folderDefaultState: "collapsed",
>       useSavedState: true,
>     }),
>   ],
>   right: [
>     Component.TableOfContents(),
>     Component.Backlinks(),
>     Component.Graph(),
>   ],
> }
> ```
> 
> If you want the explorer to *link to folder index pages* (instead of just collapsing), set:
> 
> ```ts
> folderClickBehavior: "link",
> ```
> 
> (That pairs perfectly with FolderPage index generation below.) citeturn1view1turn1view2
> 
> ---
> 
> ## 3) Auto-generated folder index pages (no more manual “index” work)
> 
> Enable the **FolderPage** emitter plugin. Quartz will generate listing pages for folders automatically. citeturn1view2turn0search5
> 
> In `quartz.config.ts`, add (or ensure it exists) in `emitters`:
> 
> ```ts
> import * as Plugin from "./quartz/plugins"
> 
> export default {
>   configuration: {
>     // ...
>   },
>   plugins: {
>     transformers: [
>       // ...
>     ],
>     filters: [
>       // ...
>     ],
>     emitters: [
>       // ...
>       Plugin.FolderPage(),
>       Plugin.TagPage(),
>       Plugin.ContentIndex(),
>       Plugin.Assets(),
>       Plugin.Static(),
>     ],
>   },
> }
> ```
> 
> Quartz docs note FolderPage uses the default list-page layout and the FolderContent component. citeturn1view2turn3search7turn3search9
> 
> ---
> 
> ## 4) Public / Private split that actually prevents leaks
> 
> ### The blunt truth
> If you build a public site from a vault that contains RAW assets, you must exclude them at the Quartz build level. Quartz specifically warns that non-markdown assets can get emitted unless excluded; the correct mechanism is `ignorePatterns`. citeturn3search0turn3search7
> 
> ### Option A (best): two builds, two deploys
> - **Public build:** only `/content/public`
> - **Private build:** `/content` (everything), protected behind Cloudflare Access
> 
> Quartz supports selecting a content directory with `-d`. citeturn4search1turn4search16
> 
> Example structure:
> ```
> content_public/   (safe, redacted)
> content_private/  (full vault)
> ```
> 
> Build commands:
> ```bash
> # public
> npx quartz build -d content_public -o public
> 
> # private
> npx quartz build -d content_private -o public-private
> ```
> 
> Deploy `public` to your public domain/subdomain, deploy `public-private` behind Zero Trust.
> 
> ### Option B (single content folder): ignorePatterns + private folder naming
> Keep:
> ```
> content/
>   public/
>   private/
> ```
> 
> Then in `quartz.config.ts` for the **public** site:
> ```ts
> configuration: {
>   ignorePatterns: [
>     "private/**",
>     "**/20_RAW/**",
>   ],
> }
> ```
> 
> Quartz documents `ignorePatterns` explicitly for private pages, with examples like excluding any folder named `private` at any depth. citeturn3search0turn2view0
> 
> ---
> 
> ## What I’d do in your FCFCU case repo
> - Public build: **only** redacted summaries + filings that are already public record
> - Private build: full vault (including evidence), **Cloudflare Access**
> - Explorer sidebar: `folderClickBehavior: "link"` so folders open their auto-generated index pages
> 
> If you paste your current `quartz.config.ts` and `quartz.layout.ts` (even just the relevant sections), I’ll give you the exact edits line-by-line so you don’t get stuck in “Quartz config hell.”

### User
> this is th etree. ```markdown
> . 📂 content
> └── 📂 case_fcfcu_v_codyrv/
> │  └── 📂 00_admin/
> │    └── 📂 00_trackers/
> │      ├── 📄 Case_Log.md
> │      ├── 📄 Expense_Tracking_Template_Reference.md
> │      ├── 📄 FINAL_STATUS_REPORT_2025-12-22.md
> │      ├── 📄 Financial_Tracker.md
> │      ├── 📄 Time_and_Capacity_Loss_Log.md
> │      ├── 📄 index.md
> │    └── 📂 05_timeline/
> │      └── 📂 10_2022/
> │        └── 📂 11/
> │      └── 📂 20_2023/
> │        └── 📂 09/
> │          └── 📂 20/
> │            ├── 📄 2023-09-20_FCFCU_Hardship_and_Health_Notice_Letter.md
> │          └── 📂 21/
> │            ├── 📄 2023-09-21_FCFCU_Letter_Pre_Shipment.md
> │          └── 📂 25/
> │            ├── 📄 2023-09-25_FCFCU_Letter_Delivered.md
> │          ├── 📄 index.md
> │        ├── 📄 index.md
> │      └── 📂 20_2024/
> │        └── 📂 03/
> │          └── 📂 20/
> │            ├── 📄 2024-03-20_FCFCU_Certified_Response_Tax_Records.md
> │        └── 📂 06/
> │          └── 📂 21/
> │            ├── 📄 2024-06-21_Property_Appraisal.md
> │        └── 📂 07/
> │          └── 📂 12/
> │            ├── 📄 2024-07-12_Mortgage_Payment_Record.md
> │          └── 📂 19/
> │            ├── 📄 2024-07-19_Invoice_003.md
> │        └── 📂 12/
> │          └── 📂 04/
> │            ├── 📄 2024-12-04_FCFCU_Statement.md
> │          └── 📂 09/
> │            ├── 📄 2024-12-09_FCFCU_Outgoing_Email_Bank_Access_Request.md
> │          └── 📂 11/
> │            ├── 📄 2024-12-11_FCFCU_Outgoing_Email_Bank_Access_Request.md
> │        ├── 📄 2024-06-21_document_Raw_Exhibit_Map.md
> │        ├── 📄 index.md
> │      └── 📂 30_2025/
> │        └── 📂 01/
> │          ├── 📄 2025-01-09_order_Court_Orders_And_Hearing_Scheduled.md
> │          ├── 📄 2025-01-09_order_Order_Court_Orders_And_Hearing_Scheduled.md
> │          ├── 📄 2025-01-16_Case_Filed.md
> │          ├── 📄 2025-01-16_court_filing_Case_Filed.md
> │        └── 📂 03/
> │          ├── 📄 2025-03-03_Service_Issued.md
> │          ├── 📄 2025-03-05_Service_Attempt_1.md
> │          ├── 📄 2025-03-05_motion_Motion_Motion_Motion_To_Vacate_Void_Judgement.md
> │          ├── 📄 2025-03-05_motion_Motion_Motion_To_Vacate_Void_Judgement.md
> │          ├── 📄 2025-03-05_motion_Motion_To_Vacate_Void_Judgement.md
> │          ├── 📄 index.md
> │        └── 📂 04/
> │          ├── 📄 2025-04-09_service_Service_Attempt_2.md
> │          ├── 📄 2025-04-15_Service_Attempt_2.md
> │        └── 📂 05/
> │          ├── 📄 2025-05-13_Motion_for_Default_Judgment.md
> │          ├── 📄 2025-05-13_motion_Motion_For_Default_Judgment.md
> │          ├── 📄 2025-05-21_Order_Denying_Default_Judgment.md
> │          ├── 📄 2025-05-21_court_filing_017_Order_Denying_Default_Judgment.md
> │          ├── 📄 2025-05-23_Amended_Motion_Default_Judgment.md
> │          ├── 📄 2025-05-23_document_Default_Judgment_Entered.md
> │          ├── 📄 2025-05-28_Default_Judgment_Entered.md
> │          ├── 📄 2025-05-29_document_Praecipe_Sheriff_Sale.md
> │          ├── 📄 2025-05-30_Praecipe_Sheriff_Sale.md
> │          ├── 📄 2025-05-30_document_Aes_Ada_Notice.md
> │        └── 📂 06/
> │          └── 📂 08/
> │            ├── 📄 2025-06-08_AES_ADA_Notice.md
> │          ├── 📄 2025-06-13_document_Sheriff_Sale_Notice_Posted.md
> │          ├── 📄 index.md
> │        └── 📂 07/
> │          ├── 📄 2025-07-09_Sheriff_Sale_Notice_Posted.md
> │          ├── 📄 2025-07-17_Plaintiff_Bid_Filed.md
> │          ├── 📄 index.md
> │        └── 📂 08/
> │          ├── 📄 2025-08-05_document_030_Report_Sheriff_Sale_No_Excess.md
> │          ├── 📄 2025-08-15_Sheriff_Sale.md
> │          ├── 📄 2025-08-15_enforcement_Writ_Of_Assistance_Issued.md
> │        └── 📂 09/
> │          ├── 📄 2025-09-09_Decree_Foreclosure_Returned.md
> │          ├── 📄 index.md
> │        └── 📂 10/
> │          ├── 📄 2025-10-29_Petition_for_Writ_of_Assistance.md
> │          ├── 📄 2025-10-29_enforcement_Petition_For_Writ_Of_Assistance.md
> │        └── 📂 11/
> │          └── 📂 06/
> │            ├── 📄 2025-11-06_Writ_of_Assistance_Issued.md
> │          └── 📂 26/
> │            ├── 📄 2025-11-26_Sheriff_Deputies_Arrive_Unrelated.md
> │        └── 📂 12/
> │          └── 📂 03/
> │            ├── 📄 2025-12-03_IMPD_Contact_Knocked_Then_Left.md
> │          └── 📂 09/
> │            ├── 📄 2025-12-09_0948_Sheriff_Arrival_Initial_Entry.md
> │            ├── 📄 2025-12-09_1000_Active_Removal_Process.md
> │            ├── 📄 2025-12-09_1016_Medical_Distress_Incident.md
> │            ├── 📄 2025-12-09_1018_Officer_Interference_Property_Retrieval.md
> │            ├── 📄 2025-12-09_1020_Room_Vacated.md
> │            ├── 📄 2025-12-09_1033_Post_Removal_Entry_Privacy_Violation.md
> │            ├── 📄 2025-12-09_1046_Camera_System_Manipulation.md
> │            ├── 📄 2025-12-09_1048_Refrigerator_Unplugged.md
> │            ├── 📄 2025-12-09_1209_Hallway_Activity.md
> │            ├── 📄 2025-12-09_Writ_Executed_Removal.md
> │          └── 📂 10/
> │            ├── 📄 2025-12-10_Motions_Filed.md
> │            ├── 📄 2025-12-10_document_Financial_Tracker.md
> │          └── 📂 11/
> │            ├── 📄 2025-12-11_Court_Orders_and_Hearing_Scheduled.md
> │          └── 📂 12/
> │            ├── 📄 2025-12-12_Supplemental_Emergency_Motion.md
> │            ├── 📄 2025-12-12_document_028_Report_Court_Defendant_Request.md
> │          └── 📂 13/
> │          └── 📂 14/
> │            ├── 📄 2025-12-14_Other_Camera_Porch_Activity.md
> │          └── 📂 15/
> │          └── 📂 16/
> │            ├── 📄 2025-12-16_AES_Emergency_Notice.md
> │            ├── 📄 2025-12-16_Emergency_Supplemental_Declaration_Filed.md
> │            ├── 📄 2025-12-16_Motion_Surplus_Funds.md
> │            ├── 📄 2025-12-16_motion_027_Supplemental_Motion_Access.md
> │          └── 📂 17/
> │            ├── 📄 2025-12-17_Notice_Surplus_Funds_Hearing.md
> │            ├── 📄 2025-12-17_Report_No_Excess_Proceeds.md
> │            ├── 📄 2025-12-17_document_Aes_Emergency_Notice.md
> │          └── 📂 18/
> │            ├── 📄 2025-12-18_Automated_Notices_Issued.md
> │          └── 📂 19/
> │            ├── 📄 2025-12-19_gigi_acute_anxiety_attack.md
> │          └── 📂 20/
> │          └── 📂 21/
> │            ├── 📄 2025-12-21_DOJ_Civil_Rights_Complaint_Submitted.md
> │            ├── 📄 2025-12-21_document_Case_Log.md
> │          └── 📂 22/
> │            ├── 📄 2025-12-22_Declaration_Filed_Envelope_37416037.md
> │            ├── 📄 2025-12-22_Supplemental_Snapshot_Displacement_Relocation_Damages.md
> │            ├── 📄 2025-12-22_Today_Snapshot_Current_State.md
> │          └── 📂 23/
> │          └── 📂 24/
> │          ├── 📄 index.md
> │        ├── 📄 index.md
> │      └── 📂 40_2026/
> │        └── 📂 01/
> │          ├── 📄 2026-01-09_motion_Supplemental_Emergency_Motion.md
> │    └── 📂 10_overviews/
> │      ├── 📄 Integrate_Disability_Separate_Appeals_Get_Stay.m4a
> │      ├── 📄 Procedural_failure_map_one_pager.md
> │      ├── 📄 Void_Judgment_Eviction_Crisis.pdf
> │      ├── 📄 Void_Judgment_Eviction_Crisis.pdf.bak
> │      └── 📂 case_maps/
> │        ├── 📄 action_Master_Strategy_Canvas.canvas
> │        ├── 📄 action_Master_Strategy_Canvas.md
> │        ├── 📄 root_Affidavit_Strategy.canvas
> │        ├── 📄 root_Affidavit_Strategy.md
> │        ├── 📄 root_Decisions.canvas
> │        ├── 📄 root_Decisions.md
> │        ├── 📄 root_Filed_Closed.canvas
> │        ├── 📄 root_Filed_Closed.md
> │        ├── 📄 root_Future_Leverage.canvas
> │        ├── 📄 root_Future_Leverage.md
> │        ├── 📄 root_Hearing_Jan_9th.canvas
> │        ├── 📄 root_Hearing_Jan_9th.md
> │        ├── 📄 root_Master_Strategy_Decision_Tree.canvas
> │        ├── 📄 root_Master_Strategy_Decision_Tree.md
> │        ├── 📄 root_Parallel_Pressure.canvas
> │        ├── 📄 root_Parallel_Pressure.md
> │        ├── 📄 root_Post_Removal_Record.canvas
> │        ├── 📄 root_Post_Removal_Record.md
> │        ├── 📄 strategy_Strategic_Plan.canvas
> │        ├── 📄 strategy_Strategic_Plan.md
> │        ├── 📄 timeline_Timeline_Canvas.canvas
> │        ├── 📄 timeline_Timeline_Canvas.md
> │      ├── 📄 index.md
> │    └── 📂 20_strategy/
> │      └── 📂 10_ada_title_ii/
> │        ├── 📄 2025-12-22_ADA_Accommodation_Letter_Displacement_Access.md
> │        ├── 📄 2025-12-22_Civil_Rights_Notice_Disability_Discrimination.md
> │      └── 📂 20_jurisdiction_service_tr_4_1_b/
> │      └── 📂 30_void_vs_voidable_tr_60b/
> │      ├── 📄 index.md
> │    └── 📂 30_drafts-templates/
> │      └── 📂 10_motions/
> │        ├── 📄 index.md
> │        ├── 📄 motion_emergency_stay_of_writ.docx
> │        ├── 📄 motion_emergency_stay_of_writ.md
> │        ├── 📄 motion_emergency_supplemental_motion_ongoing_harm.docx
> │        ├── 📄 motion_emergency_supplemental_motion_ongoing_harm.md
> │        ├── 📄 motion_to_vacate_void_judgement.docx
> │        ├── 📄 motion_to_vacate_void_judgment.md
> │        └── 📂 motions_templates/
> │          ├── 📄 _Motions.md
> │          ├── 📄 index.md
> │      └── 📂 20_declarations_affidavits/
> │        ├── 📄 029_Emergency_Supplemental_Declaration_Citation_Review.md
> │        ├── 📄 2025-12-21_Supplemental_Declaration_Ongoing_Displacement_Economic_Harm_Interference.md
> │        ├── 📄 affidavit_not_served.docx
> │        ├── 📄 affidavit_not_served.md
> │        └── 📂 affidavits_templates/
> │          ├── 📄 ADA_Disability_Affidavit.md
> │          ├── 📄 Affidavit_Blanca_Observations_Hygiene_Exhaustion_Sleeping_Car_Gigi.md
> │          ├── 📄 Affidavit_Father_Financial_Support_Displacement.md
> │          ├── 📄 Affidavit_Mother_Housing_Instability_Conditions.md
> │          ├── 📄 Affidavit_Zai_Displacement_Immigration_Harm_Living_Conditions.md
> │          ├── 📄 Character_Affidavit.md
> │          ├── 📄 Community_Service_Affidavit.md
> │          ├── 📄 Credibility_Affidavit.md
> │          ├── 📄 Observations_Affidavit.md
> │          ├── 📄 _Instructions_for_witnesses.md
> │          ├── 📄 index.md
> │        └── 📂 declarations_templates/
> │          ├── 📄 Gender_Identity_Clarification.md
> │          ├── 📄 _Declarations.md
> │          ├── 📄 index.md
> │        ├── 📄 index.md
> │        ├── 📄 updated_affidavit_language.md
> │        ├── 📄 verified_affidavit_of_defendant.md
> │      └── 📂 30_exhibits/
> │        ├── 📄 exhibit_list.docx
> │        ├── 📄 exhibit_list.md
> │        └── 📂 exhibits_templates/
> │          ├── 📄 _Exhibits_Lists.md
> │          ├── 📄 index.md
> │        ├── 📄 index.md
> │      └── 📂 40_others/
> │        ├── 📄 ada_packet.md
> │        ├── 📄 attorney_brief.md
> │        ├── 📄 index.md
> │        └── 📂 outreach_templates/
> │          ├── 📄 2025-01-02_case_brief_civil_rights_ada_consumer_protection.md
> │          ├── 📄 2025-01-02_linkedin_attorney_request_post.md
> │          ├── 📄 2025-12-19_family_message_zion_tesla_help.md
> │          ├── 📄 _Advocate_Outreach_Message.md
> │          ├── 📄 index.md
> │        ├── 📄 receipt_usps_tracking.md
> │        ├── 📄 script_call_lawyers.md
> │      └── 📂 50_proposed_orders/
> │        ├── 📄 index.md
> │        ├── 📄 proposed_order_emergency_stay.md
> │        ├── 📄 proposed_order_motion_to_vacate.md
> │        └── 📂 proposed_templates/
> │          ├── 📄 Proposed_Orders.md
> │          ├── 📄 index.md
> │      └── 📂 60_Complaints/
> │        └── 📂 10_DOJ_Civil_Rights_complaint/
> │          ├── 📄 2025-12-21_DOJ_Civil_Rights_Complaint_Submitted.md
> │          ├── 📄 2025-12-22_DOJ_Civil_Rights_Report_688619-FXN.pdf
> │          ├── 📄 DOJ CIVIL RIGHTS COMPLAINT.md
> │        └── 📂 20_INDIANA_CIVIL_RIGHTS_COMMISION/
> │          ├── 📄 2025-12-22_ICRC_Complaint_Displacement_Disability_Access_Justice.md
> │          ├── 📄 Indiana Civil Rights Commission (ICRC).md
> │        └── 📂 30_HUD_FHEO/
> │          ├── 📄 2025-12-22_HUD_Complaint_Displacement_Disability_Access_Justice.md
> │          ├── 📄 30_HUB_FHEO.md
> │        ├── 📄 index.md
> │      ├── 📄 Court_Document_Form.html
> │      ├── 📄 Court_Document_Form.md
> │      ├── 📄 Settlement_Strategy_and_Contingency_Plan.md
> │    ├── 📄 AES_data.xlsx
> │    ├── 📄 Case_Master_Index.md
> │    ├── 📄 Contacts.md
> │    ├── 📄 Damages_Time_Capacity_Log_Index.md
> │    ├── 📄 Evidence_Master_Index.md
> │    ├── 📄 Filings_Master_Index.md
> │    ├── 📄 Talking_Points.md
> │    ├── 📄 Timeline_Master.md
> │    ├── 📄 index.md
> │  └── 📂 10_filings/
> │    └── 📂 10_2025-12-10_motion_vacate/
> │      └── 📂 01_drafts/
> │        ├── 📄 Emergency Motions.docx
> │        ├── 📄 index.md
> │      └── 📂 02_exhibits/
> │        ├── 📄 01_motion_vacate.pdf
> │        ├── 📄 01_motion_vacate.pdf.bak
> │        ├── 📄 02_emergency_motion_quash_stay.pdf
> │        ├── 📄 02_emergency_motion_quash_stay.pdf.bak
> │        ├── 📄 03_order_vacate_proposed.pdf
> │        ├── 📄 03_order_vacate_proposed.pdf.bak
> │        ├── 📄 04_order_stay_writ_proposed.pdf
> │        ├── 📄 04_order_stay_writ_proposed.pdf.bak
> │        ├── 📄 05_Exhibit_List.pdf
> │        ├── 📄 05_Exhibit_List.pdf.bak
> │        ├── 📄 06_Exhibits_Combined.pdf
> │        ├── 📄 combinepdf.pdf
> │        ├── 📄 combinepdf.pdf.bak
> │        ├── 📄 index.md
> │      └── 📂 03_proposed_order/
> │        ├── 📄 Proposed_Order_Vacate.docx
> │        ├── 📄 index.md
> │      └── 📂 04_filed_receipts/
> │        ├── 📄 Odyssey_Envelope_Receipt.pdf
> │        ├── 📄 Odyssey_Envelope_Receipt.pdf.bak
> │        ├── 📄 index.md
> │    └── 📂 20_2025-12-11_Supplemental_Emergency_Motion_Access/
> │      └── 📂 01_drafts/
> │        ├── 📄 SUPPLEMENT_FORMATTING_CHECKLIST.md
> │        ├── 📄 Supplemental_Emergency_Motion.pdf
> │        ├── 📄 index.md
> │      └── 📂 02_exhibits/
> │        ├── 📄 20_exhibits_combined_source
> │        ├── 📄 Exhibit_H_Declaration.pdf
> │        ├── 📄 index.md
> │      └── 📂 04_filed_receipts/
> │        ├── 📄 Odyssey_Envelope_Receipt.pdf
> │        ├── 📄 Odyssey_Envelope_Receipt.pdf.bak
> │        ├── 📄 index.md
> │    └── 📂 30_2025-12-21_Post-Execution_Incident_Declaration/
> │      ├── 📄 EX-N-001_2025-12-22_Declaration_Ongoing_Displacement_and_Economic_Harm.pdf
> │    ├── 📄 Motions.md
> │    ├── 📄 index.md
> │  └── 📂 20_evidence_vault/
> │    └── 📂 10_EXHIBIT_SETS/
> │      ├── 📄 _checklist.md
> │      └── 📂 exhibits_A-H_initial/
> │        ├── 📄 2025-12-10_MTV_Exhibits_Combined.pdf
> │        ├── 📄 Exhibit_A_20250305_Sheriff_Return.pdf
> │        ├── 📄 Exhibit_B_20250415_Sheriff_Return.pdf
> │        ├── 📄 Exhibit_C_20250116_Incomplete_Summons.pdf
> │        ├── 📄 Exhibit_D_20250513_Default_Judgment_Motion.pdf
> │        ├── 📄 Exhibit_E_20251029_Petition_for_Writ.pdf
> │        ├── 📄 Exhibit_E_20251029_Petition_for_Writ.pdf.bak
> │        ├── 📄 Exhibit_F_Affidavit_Cody_RiceVelasquez.pdf
> │        ├── 📄 Exhibit_F_Affidavit_Cody_RiceVelasquez.pdf.bak
> │        ├── 📄 Exhibit_G1_ADA_Notice_Request.pdf
> │        ├── 📄 Exhibit_G1_ADA_Notice_Request.pdf.bak
> │        ├── 📄 Exhibit_G2_AES_ADA_Docs_Disconnect_Notices.pdf
> │        ├── 📄 Exhibit_H_Declaration.pdf
> │        ├── 📄 index.md
> │      └── 📂 exhibits_I_ada_communications/
> │      └── 📂 exhibits_J_eviction_removal/
> │      └── 📂 exhibits_K_financial/
> │      └── 📂 exhibits_L_statements/
> │      └── 📂 exhibits_M_court-service/
> │      └── 📂 exhibits_N_declarations/
> │        └── 📂 Envelope_37416037/
> │          ├── 📄 EX-N-001_2025-12-22_Declaration_Ongoing_Displacement_and_Economic_Harm.pdf
> │        └── 📂 drafts/
> │          ├── 📄 Exhibit_N_001_DECLARATION OF CODY RICE-VELASQUEZ.md
> │      └── 📂 exhibits_P_property/
> │      ├── 📄 index.md
> │    └── 📂 20_RAW/
> │      └── 📂 10_supporting/
> │        └── 📂 10_photos_video/
> │          └── 📂 2025-11-26_Sheriff_At_Home_Unrelated_No_Notice/
> │            ├── 📄 EX-V-26-02_2025-11-26_2200.mp4
> │            ├── 📄 index.md
> │          └── 📂 2025-12-03_Police_Knocked_Then_Left_Quickly/
> │            ├── 📄 EX-V-03-02_2025-12-03_1351.mp4
> │            ├── 📄 EX-V-03-03_2025-12-03_1351.jpg
> │            ├── 📄 index.md
> │          └── 📂 2025-12-09_Removal_Day_Camera_Bedroom/
> │            ├── 📄 EX-V-09-01_2025-12-09_0948.mp4
> │            ├── 📄 EX-V-09-02_2025-12-09_0949.mp4
> │            ├── 📄 EX-V-09-03_2025-12-09_0950.mp4
> │            ├── 📄 EX-V-09-04_2025-12-09_0951.mp4
> │            ├── 📄 EX-V-09-05_2025-12-09_0952.mp4
> │            ├── 📄 EX-V-09-06_2025-12-09_0953.mp4
> │            ├── 📄 EX-V-09-07_2025-12-09_0954.mp4
> │            ├── 📄 EX-V-09-08_2025-12-09_0955.mp4
> │            ├── 📄 EX-V-09-09_2025-12-09_0956.mp4
> │            ├── 📄 EX-V-09-10_2025-12-09_0957.mp4
> │            ├── 📄 EX-V-09-11_2025-12-09_0958.mp4
> │            ├── 📄 EX-V-09-12_2025-12-09_0959.mp4
> │            ├── 📄 EX-V-09-13_2025-12-09_1000.mp4
> │            ├── 📄 EX-V-09-14_2025-12-09_1001.mp4
> │            ├── 📄 EX-V-09-15_2025-12-09_1002.mp4
> │            ├── 📄 EX-V-09-16_2025-12-09_1003.mp4
> │            ├── 📄 EX-V-09-17_2025-12-09_1004.mp4
> │            ├── 📄 EX-V-09-18_2025-12-09_1005.mp4
> │            ├── 📄 EX-V-09-19_2025-12-09_1006.mp4
> │            ├── 📄 EX-V-09-20_2025-12-09_1007.mp4
> │            ├── 📄 EX-V-09-21_2025-12-09_1008.mp4
> │            ├── 📄 EX-V-09-22_2025-12-09_1009.mp4
> │            ├── 📄 EX-V-09-23_2025-12-09_1010.mp4
> │            ├── 📄 EX-V-09-24_2025-12-09_1011.mp4
> │            ├── 📄 EX-V-09-25_2025-12-09_1012.mp4
> │            ├── 📄 EX-V-09-26_2025-12-09_1013.mp4
> │            ├── 📄 EX-V-09-27_2025-12-09_1014.mp4
> │            ├── 📄 EX-V-09-28_2025-12-09_1015.mp4
> │            ├── 📄 EX-V-09-29_2025-12-09_1016.mp4
> │            ├── 📄 EX-V-09-30_2025-12-09_1017.mp4
> │            ├── 📄 EX-V-09-31_2025-12-09_1018.mp4
> │            ├── 📄 EX-V-09-32_2025-12-09_1019.mp4
> │            ├── 📄 EX-V-09-33_2025-12-09_1020.mp4
> │            ├── 📄 EX-V-09-34_2025-12-09_1021.mp4
> │            ├── 📄 EX-V-09-35_2025-12-09_1022.mp4
> │            ├── 📄 EX-V-09-36_2025-12-09_1023.mp4
> │            ├── 📄 EX-V-09-37_2025-12-09_1024.mp4
> │            ├── 📄 EX-V-09-38_2025-12-09_1025.mp4
> │            ├── 📄 EX-V-09-39_2025-12-09_1026.mp4
> │            ├── 📄 EX-V-09-40_2025-12-09_1027.mp4
> │            ├── 📄 EX-V-09-41_2025-12-09_1028.mp4
> │            ├── 📄 EX-V-09-42_2025-12-09_1029.mp4
> │            ├── 📄 EX-V-09-43_2025-12-09_1030.mp4
> │            ├── 📄 EX-V-09-44_2025-12-09_1031.mp4
> │            ├── 📄 EX-V-09-45_2025-12-09_1032.mp4
> │            ├── 📄 EX-V-09-46_2025-12-09_1033.mp4
> │            ├── 📄 EX-V-09-47_2025-12-09_1034.mp4
> │            ├── 📄 EX-V-09-48_2025-12-09_1035.mp4
> │            ├── 📄 EX-V-09-49_2025-12-09_1036.mp4
> │            ├── 📄 EX-V-09-50_2025-12-09_1037.mp4
> │            ├── 📄 EX-V-09-51_2025-12-09_1038.mp4
> │            ├── 📄 EX-V-09-52_2025-12-09_1039.mp4
> │            ├── 📄 EX-V-09-53_2025-12-09_1040.mp4
> │            ├── 📄 EX-V-09-54_2025-12-09_1041.mp4
> │            ├── 📄 EX-V-09-55_2025-12-09_1042.mp4
> │            ├── 📄 EX-V-09-56_2025-12-09_1043.mp4
> │            ├── 📄 EX-V-09-57_2025-12-09_1044.mp4
> │            ├── 📄 EX-V-09-58_2025-12-09_1045.mp4
> │            ├── 📄 EX-V-09-59_2025-12-09_1046.mp4
> │            ├── 📄 EX-V-09-60_2025-12-09_1047.mp4
> │            ├── 📄 EX-V-09-61_2025-12-09_1048.mp4
> │            ├── 📄 index.md
> │            ├── 📄 new_index_entries.txt
> │          └── 📂 2025-12-09_Removal_Day_Camera_Garage/
> │            ├── 📄 EX-V-09-62_2025-12-09_0000_00.mp4
> │            ├── 📄 EX-V-09-63_2025-12-09_0000_01.mp4
> │            ├── 📄 EX-V-09-64_2025-12-09_0000_02.mp4
> │            ├── 📄 EX-V-09-65_2025-12-09_0000_03.mp4
> │            ├── 📄 EX-V-09-66_2025-12-09_0000_04.mp4
> │            ├── 📄 EX-V-09-67_2025-12-09_0000_05.mp4
> │            ├── 📄 EX-V-09-68_2025-12-09_0000_06.mp4
> │            ├── 📄 EX-V-09-69_2025-12-09_0000_07.mp4
> │            ├── 📄 EX-V-09-70_2025-12-09_0000_08.mp4
> │            ├── 📄 EX-V-09-71_2025-12-09_0000_09.mp4
> │            ├── 📄 EX-V-09-72_2025-12-09_0000_10.mp4
> │            ├── 📄 EX-V-09-73_2025-12-09_0000_11.mp4
> │            ├── 📄 EX-V-09-74_2025-12-09_0000_12.mp4
> │            ├── 📄 EX-V-09-75_2025-12-09_0000_13.mp4
> │            ├── 📄 EX-V-09-76_2025-12-09_0000_14.mp4
> │            ├── 📄 EX-V-09-77_2025-12-09_0000_15.mp4
> │            ├── 📄 EX-V-09-78_2025-12-09_0000_16.mp4
> │            ├── 📄 EX-V-09-79_2025-12-09_0000_17.mp4
> │            ├── 📄 EX-V-09-80_2025-12-09_0000_18.mp4
> │            ├── 📄 EX-V-09-81_2025-12-09_0000_19.mp4
> │            ├── 📄 EX-V-09-82_2025-12-09_0000_20.mp4
> │            ├── 📄 EX-V-09-83_2025-12-09_0000_21.mp4
> │            ├── 📄 EX-V-09-84_2025-12-09_0000_22.mp4
> │            ├── 📄 EX-V-09-85_2025-12-09_0000_23.mp4
> │            ├── 📄 EX-V-09-86_2025-12-09_0000_24.mp4
> │            ├── 📄 EX-V-09-87_2025-12-09_0000_25.mp4
> │            ├── 📄 EX-V-09-88_2025-12-09_0000_26.mp4
> │            ├── 📄 EX-V-09-89_2025-12-09_0000_27.mp4
> │            ├── 📄 EX-V-09-90_2025-12-09_0000_28.mp4
> │            ├── 📄 EX-V-09-91_2025-12-09_0000_29.mp4
> │            ├── 📄 EX-V-09-92_2025-12-09_0000_30.mp4
> │            ├── 📄 EX-V-09-93_2025-12-09_0000_31.mp4
> │            ├── 📄 EX-V-09-94_2025-12-09_0000_32.mp4
> │            ├── 📄 EX-V-09-95_2025-12-09_0000_33.mp4
> │            ├── 📄 EX-V-09-96_2025-12-09_0000_34.mp4
> │            ├── 📄 EX-V-09-97_2025-12-09_0000_35.mp4
> │            ├── 📄 EX-V-09-98_2025-12-09_0000_36.mp4
> │            ├── 📄 EX-V-09-99_2025-12-09_0000_37.mp4
> │            ├── 📄 index.md
> │          └── 📂 2025-12-09_Removal_Day_Camera_Hallway/
> │            ├── 📄 EX-V-09-179_2025-12-09_1209.mp4
> │          └── 📂 2025-12-09_Removal_Day_Camera_Kitchen/
> │            ├── 📄 EX-V-09-185_2025-12-09_9103.mp4
> │          └── 📂 2025-12-09_Removal_Day_Camera_Porch/
> │            └── 📂 09/
> │              ├── 📄 EX-V-09-142_2025-12-09_0944.mp4
> │              ├── 📄 EX-V-09-143_2025-12-09_0945.mp4
> │              ├── 📄 EX-V-09-145_2025-12-09_0950.mp4
> │              ├── 📄 EX-V-09-148_2025-12-09_0957.mp4
> │              ├── 📄 index.md
> │            └── 📂 10/
> │              ├── 📄 EX-V-09-151_2025-12-09_1003.mp4
> │              ├── 📄 EX-V-09-153_2025-12-09_1009.mp4
> │              ├── 📄 EX-V-09-157_2025-12-09_1016.mp4
> │              ├── 📄 EX-V-09-160_2025-12-09_1022.mp4
> │              ├── 📄 EX-V-09-162_2025-12-09_1027.mp4
> │              ├── 📄 EX-V-09-164_2025-12-09_1028.mp4
> │              ├── 📄 EX-V-09-166_2025-12-09_1040.mp4
> │              ├── 📄 EX-V-09-168_2025-12-09_1041.mp4
> │              ├── 📄 EX-V-09-169_2025-12-09_1051.mp4
> │              ├── 📄 EX-V-09-171_2025-12-09_1057.mp4
> │              ├── 📄 index.md
> │            └── 📂 11/
> │              ├── 📄 EX-V-09-173_2025-12-09_1130.mp4
> │              ├── 📄 EX-V-09-175_2025-12-09_1131.mp4
> │              ├── 📄 index.md
> │            └── 📂 12/
> │              ├── 📄 EX-V-09-176_2025-12-09_1206.mp4
> │              ├── 📄 EX-V-09-177_2025-12-09_1207.mp4
> │              ├── 📄 index.md
> │            └── 📂 13/
> │              ├── 📄 EX-V-09-180_2025-12-09_1318.mp4
> │              ├── 📄 EX-V-09-182_2025-12-09_1327.mp4
> │              ├── 📄 index.md
> │            ├── 📄 EX-V-09-133_2025-12-09_0443.jpg
> │            ├── 📄 EX-V-09-134_2025-12-09_0448.jpg
> │            ├── 📄 EX-V-09-144_2025-12-09_0945.jpg
> │            ├── 📄 EX-V-09-146_2025-12-09_0950.jpg
> │            ├── 📄 EX-V-09-149_2025-12-09_0957.jpg
> │            ├── 📄 EX-V-09-152_2025-12-09_1003.jpg
> │            ├── 📄 EX-V-09-154_2025-12-09_1009.jpg
> │            ├── 📄 EX-V-09-158_2025-12-09_1016.jpg
> │            ├── 📄 EX-V-09-161_2025-12-09_1022.jpg
> │            ├── 📄 EX-V-09-163_2025-12-09_1027.jpg
> │            ├── 📄 EX-V-09-167_2025-12-09_1040.jpg
> │            ├── 📄 EX-V-09-170_2025-12-09_1051.jpg
> │            ├── 📄 EX-V-09-172_2025-12-09_1057.jpg
> │            ├── 📄 EX-V-09-174_2025-12-09_1130.jpg
> │            ├── 📄 EX-V-09-178_2025-12-09_1207.jpg
> │            ├── 📄 EX-V-09-181_2025-12-09_1318.jpg
> │            ├── 📄 EX-V-09-183_2025-12-09_1327.jpg
> │            ├── 📄 index.md
> │          └── 📂 2025-12-09_Removal_Day_Photos/
> │            ├── 📄 EX-V-09-100_2025-12-0.jpg
> │            ├── 📄 EX-V-09-101_2025-12-0.jpg
> │            ├── 📄 EX-V-09-102_2025-12-0.png
> │            ├── 📄 EX-V-09-103_2025-12-0.jpg
> │            ├── 📄 EX-V-09-104_2025-12-0.jpg
> │            ├── 📄 EX-V-09-105_2025-12-0.jpg
> │            ├── 📄 EX-V-09-106_2025-12-0.jpg
> │            ├── 📄 EX-V-09-107_2025-12-0.jpg
> │            ├── 📄 EX-V-09-108_2025-12-.heic
> │            ├── 📄 EX-V-09-108_2025-12-0.jpg
> │            ├── 📄 EX-V-09-109_2025-12-0.jpg
> │            ├── 📄 EX-V-09-110_2025-12-0.jpg
> │            ├── 📄 EX-V-09-111_2025-12-0.jpg
> │            ├── 📄 EX-V-09-112_2025-12-0.jpg
> │            ├── 📄 EX-V-09-113_2025-12-0.jpg
> │            ├── 📄 EX-V-09-114_2025-12-0.jpg
> │            ├── 📄 EX-V-09-115_2025-12-0.jpg
> │            ├── 📄 EX-V-09-116_2025-12-0.jpg
> │            ├── 📄 EX-V-09-117_2025-12-0.jpg
> │            ├── 📄 EX-V-09-118_2025-12-0.jpg
> │            ├── 📄 EX-V-09-119_2025-12-0.png
> │            ├── 📄 EX-V-09-120_2025-12-0.jpg
> │            ├── 📄 EX-V-09-121_2025-12-0.jpg
> │            ├── 📄 EX-V-09-122_2025-12-0.jpg
> │            ├── 📄 EX-V-09-123_2025-12-0.jpg
> │            ├── 📄 EX-V-09-124_2025-12-0.jpg
> │            ├── 📄 EX-V-09-125_2025-12-0.jpg
> │            ├── 📄 EX-V-09-126_2025-12-0.jpg
> │            ├── 📄 EX-V-09-127_2025-12-0.jpg
> │            ├── 📄 EX-V-09-128_2025-12-.heic
> │            ├── 📄 EX-V-09-128_2025-12-0.jpg
> │            ├── 📄 EX-V-09-129_2025-12-0.png
> │            ├── 📄 EX-V-09-130_2025-12-0.png
> │            ├── 📄 EX-V-09-131_2025-12-0.jpg
> │            ├── 📄 EX-V-09-132_2025-12-0.jpg
> │            ├── 📄 EX-V-09-135_2025-12-0.jpg
> │            ├── 📄 EX-V-09-136_2025-12-0.jpg
> │            ├── 📄 EX-V-09-137_2025-12-0.jpg
> │            ├── 📄 EX-V-09-138_2025-12-0.jpg
> │            ├── 📄 EX-V-09-139_2025-12-0.jpg
> │            ├── 📄 EX-V-09-140_2025-12-0.jpg
> │            ├── 📄 EX-V-09-141_2025-12-0.jpg
> │            ├── 📄 EX-V-09-147_2025-12-0.jpg
> │            ├── 📄 EX-V-09-150_2025-12-0.jpg
> │            ├── 📄 EX-V-09-155_2025-12-0.jpg
> │            ├── 📄 EX-V-09-156_2025-12-0.jpg
> │            ├── 📄 EX-V-09-159_2025-12-0.jpg
> │            ├── 📄 EX-V-09-165_2025-12-0.jpg
> │            ├── 📄 EX-V-09-184_2025-12-0.jpg
> │            ├── 📄 index.md
> │          └── 📂 2025-12-14_Other_Camera_Porch/
> │            └── 📂 1300/
> │              ├── 📄 EX-V-14-01_2025-12-14_1351.mp4
> │              ├── 📄 EX-V-14-02_2025-12-14_1352.mp4
> │              ├── 📄 index.md
> │            └── 📂 1500/
> │              ├── 📄 EX-V-14-03_2025-12-14_1500.mp4
> │              ├── 📄 EX-V-14-04_2025-12-14_1501.mp4
> │              ├── 📄 EX-V-14-05_2025-12-14_1502.mp4
> │              ├── 📄 EX-V-14-06_2025-12-14_1503.mp4
> │              ├── 📄 EX-V-14-07_2025-12-14_1504.mp4
> │              ├── 📄 EX-V-14-08_2025-12-14_1505.mp4
> │              ├── 📄 EX-V-14-09_2025-12-14_1506.mp4
> │              ├── 📄 EX-V-14-10_2025-12-14_1507.mp4
> │              ├── 📄 EX-V-14-11_2025-12-14_1508.mp4
> │              ├── 📄 EX-V-14-12_2025-12-14_1509.mp4
> │              ├── 📄 EX-V-14-13_2025-12-14_1510.mp4
> │              ├── 📄 EX-V-14-14_2025-12-14_1511.mp4
> │              ├── 📄 EX-V-14-15_2025-12-14_1512.mp4
> │              ├── 📄 EX-V-14-16_2025-12-14_1513.mp4
> │              ├── 📄 EX-V-14-17_2025-12-14_1514.mp4
> │              ├── 📄 EX-V-14-18_2025-12-14_1515.mp4
> │              ├── 📄 EX-V-14-19_2025-12-14_1516.mp4
> │              ├── 📄 EX-V-14-20_2025-12-14_1517.mp4
> │              ├── 📄 EX-V-14-21_2025-12-14_1518.mp4
> │              ├── 📄 EX-V-14-22_2025-12-14_1519.mp4
> │              ├── 📄 EX-V-14-23_2025-12-14_1520.mp4
> │              ├── 📄 EX-V-14-24_2025-12-14_1521.mp4
> │              ├── 📄 EX-V-14-25_2025-12-14_1522.mp4
> │              ├── 📄 EX-V-14-26_2025-12-14_1523.mp4
> │              ├── 📄 EX-V-14-27_2025-12-14_1524.mp4
> │              ├── 📄 EX-V-14-28_2025-12-14_1525.mp4
> │              ├── 📄 EX-V-14-29_2025-12-14_1526.mp4
> │              ├── 📄 EX-V-14-30_2025-12-14_1527.mp4
> │              ├── 📄 EX-V-14-31_2025-12-14_1528.mp4
> │              ├── 📄 EX-V-14-32_2025-12-14_1529.mp4
> │              ├── 📄 EX-V-14-33_2025-12-14_1530.mp4
> │              ├── 📄 EX-V-14-34_2025-12-14_1531.mp4
> │              ├── 📄 EX-V-14-35_2025-12-14_1532.mp4
> │              ├── 📄 EX-V-14-36_2025-12-14_1533.mp4
> │              ├── 📄 EX-V-14-37_2025-12-14_1534.mp4
> │              ├── 📄 EX-V-14-38_2025-12-14_1535.mp4
> │              ├── 📄 EX-V-14-39_2025-12-14_1536.mp4
> │              ├── 📄 EX-V-14-40_2025-12-14_1537.mp4
> │              ├── 📄 EX-V-14-41_2025-12-14_1538.mp4
> │              ├── 📄 EX-V-14-42_2025-12-14_1539.mp4
> │              ├── 📄 EX-V-14-43_2025-12-14_1540.mp4
> │              ├── 📄 EX-V-14-44_2025-12-14_1541.mp4
> │              ├── 📄 EX-V-14-45_2025-12-14_1542.mp4
> │              ├── 📄 EX-V-14-46_2025-12-14_1543.mp4
> │              ├── 📄 EX-V-14-47_2025-12-14_1544.mp4
> │              ├── 📄 EX-V-14-48_2025-12-14_1545.mp4
> │              ├── 📄 EX-V-14-49_2025-12-14_1546.mp4
> │              ├── 📄 EX-V-14-50_2025-12-14_1547.mp4
> │              ├── 📄 EX-V-14-51_2025-12-14_1548.mp4
> │              ├── 📄 EX-V-14-52_2025-12-14_1549.mp4
> │              ├── 📄 EX-V-14-53_2025-12-14_1550.mp4
> │              ├── 📄 EX-V-14-54_2025-12-14_1551.mp4
> │              ├── 📄 EX-V-14-55_2025-12-14_1552.mp4
> │              ├── 📄 EX-V-14-56_2025-12-14_1553.mp4
> │              ├── 📄 EX-V-14-57_2025-12-14_1554.mp4
> │              ├── 📄 EX-V-14-58_2025-12-14_1555.mp4
> │              ├── 📄 EX-V-14-59_2025-12-14_1556.mp4
> │              ├── 📄 EX-V-14-60_2025-12-14_1557.mp4
> │              ├── 📄 EX-V-14-61_2025-12-14_1558.mp4
> │              ├── 📄 EX-V-14-62_2025-12-14_1559.mp4
> │              ├── 📄 index.md
> │            └── 📂 1600/
> │              ├── 📄 EX-V-14-100_2025-12-14_1637.mp4
> │              ├── 📄 EX-V-14-101_2025-12-14_1638.mp4
> │              ├── 📄 EX-V-14-102_2025-12-14_1639.mp4
> │              ├── 📄 EX-V-14-103_2025-12-14_1640.mp4
> │              ├── 📄 EX-V-14-104_2025-12-14_1641.mp4
> │              ├── 📄 EX-V-14-105_2025-12-14_1642.mp4
> │              ├── 📄 EX-V-14-106_2025-12-14_1643.mp4
> │              ├── 📄 EX-V-14-107_2025-12-14_1644.mp4
> │              ├── 📄 EX-V-14-108_2025-12-14_1645.mp4
> │              ├── 📄 EX-V-14-109_2025-12-14_1646.mp4
> │              ├── 📄 EX-V-14-110_2025-12-14_1647.mp4
> │              ├── 📄 EX-V-14-111_2025-12-14_1648.mp4
> │              ├── 📄 EX-V-14-112_2025-12-14_1649.mp4
> │              ├── 📄 EX-V-14-113_2025-12-14_1650.mp4
> │              ├── 📄 EX-V-14-114_2025-12-14_1651.mp4
> │              ├── 📄 EX-V-14-115_2025-12-14_1652.mp4
> │              ├── 📄 EX-V-14-116_2025-12-14_1653.mp4
> │              ├── 📄 EX-V-14-117_2025-12-14_1654.mp4
> │              ├── 📄 EX-V-14-118_2025-12-14_1655.mp4
> │              ├── 📄 EX-V-14-119_2025-12-14_1656.mp4
> │              ├── 📄 EX-V-14-120_2025-12-14_1657.mp4
> │              ├── 📄 EX-V-14-121_2025-12-14_1658.mp4
> │              ├── 📄 EX-V-14-122_2025-12-14_1659.mp4
> │              ├── 📄 EX-V-14-63_2025-12-14_1600.mp4
> │              ├── 📄 EX-V-14-64_2025-12-14_1601.mp4
> │              ├── 📄 EX-V-14-65_2025-12-14_1602.mp4
> │              ├── 📄 EX-V-14-66_2025-12-14_1603.mp4
> │              ├── 📄 EX-V-14-67_2025-12-14_1604.mp4
> │              ├── 📄 EX-V-14-68_2025-12-14_1605.mp4
> │              ├── 📄 EX-V-14-69_2025-12-14_1606.mp4
> │              ├── 📄 EX-V-14-70_2025-12-14_1607.mp4
> │              ├── 📄 EX-V-14-71_2025-12-14_1608.mp4
> │              ├── 📄 EX-V-14-72_2025-12-14_1609.mp4
> │              ├── 📄 EX-V-14-73_2025-12-14_1610.mp4
> │              ├── 📄 EX-V-14-74_2025-12-14_1611.mp4
> │              ├── 📄 EX-V-14-75_2025-12-14_1612.mp4
> │              ├── 📄 EX-V-14-76_2025-12-14_1613.mp4
> │              ├── 📄 EX-V-14-77_2025-12-14_1614.mp4
> │              ├── 📄 EX-V-14-78_2025-12-14_1615.mp4
> │              ├── 📄 EX-V-14-79_2025-12-14_1616.mp4
> │              ├── 📄 EX-V-14-80_2025-12-14_1617.mp4
> │              ├── 📄 EX-V-14-81_2025-12-14_1618.mp4
> │              ├── 📄 EX-V-14-82_2025-12-14_1619.mp4
> │              ├── 📄 EX-V-14-83_2025-12-14_1620.mp4
> │              ├── 📄 EX-V-14-84_2025-12-14_1621.mp4
> │              ├── 📄 EX-V-14-85_2025-12-14_1622.mp4
> │              ├── 📄 EX-V-14-86_2025-12-14_1623.mp4
> │              ├── 📄 EX-V-14-87_2025-12-14_1624.mp4
> │              ├── 📄 EX-V-14-88_2025-12-14_1625.mp4
> │              ├── 📄 EX-V-14-89_2025-12-14_1626.mp4
> │              ├── 📄 EX-V-14-90_2025-12-14_1627.mp4
> │              ├── 📄 EX-V-14-91_2025-12-14_1628.mp4
> │              ├── 📄 EX-V-14-92_2025-12-14_1629.mp4
> │              ├── 📄 EX-V-14-93_2025-12-14_1630.mp4
> │              ├── 📄 EX-V-14-94_2025-12-14_1631.mp4
> │              ├── 📄 EX-V-14-95_2025-12-14_1632.mp4
> │              ├── 📄 EX-V-14-96_2025-12-14_1633.mp4
> │              ├── 📄 EX-V-14-97_2025-12-14_1634.mp4
> │              ├── 📄 EX-V-14-98_2025-12-14_1635.mp4
> │              ├── 📄 EX-V-14-99_2025-12-14_1636.mp4
> │              ├── 📄 index.md
> │          └── 📂 2025-12-17_Retrieval_Day_Camera_Bedroom/
> │            ├── 📄 EX-V-17-00_2025-12-17_1100.mp4
> │            ├── 📄 EX-V-17-01_2025-12-17_1101.mp4
> │            ├── 📄 EX-V-17-02_2025-12-17_1102.mp4
> │            ├── 📄 EX-V-17-03_2025-12-17_1103.mp4
> │            ├── 📄 EX-V-17-04_2025-12-17_1104.mp4
> │            ├── 📄 EX-V-17-05_2025-12-17_1105.mp4
> │            ├── 📄 EX-V-17-06_2025-12-17_1106.mp4
> │            ├── 📄 EX-V-17-07_2025-12-17_1107.mp4
> │            ├── 📄 EX-V-17-08_2025-12-17_1108.mp4
> │            ├── 📄 EX-V-17-09_2025-12-17_1109.mp4
> │            ├── 📄 EX-V-17-10_2025-12-17_1110.mp4
> │            ├── 📄 EX-V-17-11_2025-12-17_1111.mp4
> │            ├── 📄 EX-V-17-12_2025-12-17_1112.mp4
> │            ├── 📄 EX-V-17-13_2025-12-17_1113.mp4
> │            ├── 📄 EX-V-17-14_2025-12-17_1114.mp4
> │            ├── 📄 EX-V-17-15_2025-12-17_1115.mp4
> │            ├── 📄 EX-V-17-16_2025-12-17_1116.mp4
> │            ├── 📄 EX-V-17-17_2025-12-17_1117.mp4
> │            ├── 📄 EX-V-17-18_2025-12-17_1118.mp4
> │            ├── 📄 EX-V-17-19_2025-12-17_1119.mp4
> │            ├── 📄 EX-V-17-20_2025-12-17_1120.mp4
> │            ├── 📄 EX-V-17-21_2025-12-17_1121.mp4
> │            ├── 📄 EX-V-17-22_2025-12-17_1122.mp4
> │            ├── 📄 EX-V-17-23_2025-12-17_1123.mp4
> │            ├── 📄 EX-V-17-24_2025-12-17_1124.mp4
> │            ├── 📄 EX-V-17-25_2025-12-17_1125.mp4
> │            ├── 📄 EX-V-17-26_2025-12-17_1126.mp4
> │            ├── 📄 EX-V-17-27_2025-12-17_1127.mp4
> │            ├── 📄 EX-V-17-28_2025-12-17_1128.mp4
> │            ├── 📄 EX-V-17-29_2025-12-17_1129.mp4
> │            ├── 📄 EX-V-17-30_2025-12-17_1130.mp4
> │            ├── 📄 EX-V-17-31_2025-12-17_1131.mp4
> │            ├── 📄 EX-V-17-32_2025-12-17_1132.mp4
> │            ├── 📄 EX-V-17-33_2025-12-17_1133.mp4
> │            ├── 📄 EX-V-17-34_2025-12-17_1134.mp4
> │            ├── 📄 EX-V-17-35_2025-12-17_1135.mp4
> │            ├── 📄 EX-V-17-36_2025-12-17_1136.mp4
> │            ├── 📄 EX-V-17-37_2025-12-17_1137.mp4
> │            ├── 📄 EX-V-17-38_2025-12-17_1138.mp4
> │            ├── 📄 EX-V-17-39_2025-12-17_1139.mp4
> │            ├── 📄 EX-V-17-40_2025-12-17_1140.mp4
> │            ├── 📄 EX-V-17-41_2025-12-17_1141.mp4
> │            ├── 📄 EX-V-17-42_2025-12-17_1142.mp4
> │            ├── 📄 index.md
> │          └── 📂 2025-12-17_Retrieval_Day_Camera_Driveway/
> │            └── 📂 00/
> │              ├── 📄 EX-V-17-100_2025-12-17_0057.mp4
> │              ├── 📄 EX-V-17-101_2025-12-17_0058.mp4
> │              ├── 📄 EX-V-17-102_2025-12-17_0059.mp4
> │              ├── 📄 EX-V-17-43_2025-12-17_0000.mp4
> │              ├── 📄 EX-V-17-44_2025-12-17_0001.mp4
> │              ├── 📄 EX-V-17-45_2025-12-17_0002.mp4
> │              ├── 📄 EX-V-17-46_2025-12-17_0003.mp4
> │              ├── 📄 EX-V-17-47_2025-12-17_0004.mp4
> │              ├── 📄 EX-V-17-48_2025-12-17_0005.mp4
> │              ├── 📄 EX-V-17-49_2025-12-17_0006.mp4
> │              ├── 📄 EX-V-17-50_2025-12-17_0007.mp4
> │              ├── 📄 EX-V-17-51_2025-12-17_0008.mp4
> │              ├── 📄 EX-V-17-52_2025-12-17_0009.mp4
> │              ├── 📄 EX-V-17-53_2025-12-17_0010.mp4
> │              ├── 📄 EX-V-17-54_2025-12-17_0011.mp4
> │              ├── 📄 EX-V-17-55_2025-12-17_0012.mp4
> │              ├── 📄 EX-V-17-56_2025-12-17_0013.mp4
> │              ├── 📄 EX-V-17-57_2025-12-17_0014.mp4
> │              ├── 📄 EX-V-17-58_2025-12-17_0015.mp4
> │              ├── 📄 EX-V-17-59_2025-12-17_0016.mp4
> │              ├── 📄 EX-V-17-60_2025-12-17_0017.mp4
> │              ├── 📄 EX-V-17-61_2025-12-17_0018.mp4
> │              ├── 📄 EX-V-17-62_2025-12-17_0019.mp4
> │              ├── 📄 EX-V-17-63_2025-12-17_0020.mp4
> │              ├── 📄 EX-V-17-64_2025-12-17_0021.mp4
> │              ├── 📄 EX-V-17-65_2025-12-17_0022.mp4
> │              ├── 📄 EX-V-17-66_2025-12-17_0023.mp4
> │              ├── 📄 EX-V-17-67_2025-12-17_0024.mp4
> │              ├── 📄 EX-V-17-68_2025-12-17_0025.mp4
> │              ├── 📄 EX-V-17-69_2025-12-17_0026.mp4
> │              ├── 📄 EX-V-17-70_2025-12-17_0027.mp4
> │              ├── 📄 EX-V-17-71_2025-12-17_0028.mp4
> │              ├── 📄 EX-V-17-72_2025-12-17_0029.mp4
> │              ├── 📄 EX-V-17-73_2025-12-17_0030.mp4
> │              ├── 📄 EX-V-17-74_2025-12-17_0031.mp4
> │              ├── 📄 EX-V-17-75_2025-12-17_0032.mp4
> │              ├── 📄 EX-V-17-76_2025-12-17_0033.mp4
> │              ├── 📄 EX-V-17-77_2025-12-17_0034.mp4
> │              ├── 📄 EX-V-17-78_2025-12-17_0035.mp4
> │              ├── 📄 EX-V-17-79_2025-12-17_0036.mp4
> │              ├── 📄 EX-V-17-80_2025-12-17_0037.mp4
> │              ├── 📄 EX-V-17-81_2025-12-17_0038.mp4
> │              ├── 📄 EX-V-17-82_2025-12-17_0039.mp4
> │              ├── 📄 EX-V-17-83_2025-12-17_0040.mp4
> │              ├── 📄 EX-V-17-84_2025-12-17_0041.mp4
> │              ├── 📄 EX-V-17-85_2025-12-17_0042.mp4
> │              ├── 📄 EX-V-17-86_2025-12-17_0043.mp4
> │              ├── 📄 EX-V-17-87_2025-12-17_0044.mp4
> │              ├── 📄 EX-V-17-88_2025-12-17_0045.mp4
> │              ├── 📄 EX-V-17-89_2025-12-17_0046.mp4
> │              ├── 📄 EX-V-17-90_2025-12-17_0047.mp4
> │              ├── 📄 EX-V-17-91_2025-12-17_0048.mp4
> │              ├── 📄 EX-V-17-92_2025-12-17_0049.mp4
> │              ├── 📄 EX-V-17-93_2025-12-17_0050.mp4
> │              ├── 📄 EX-V-17-94_2025-12-17_0051.mp4
> │              ├── 📄 EX-V-17-95_2025-12-17_0052.mp4
> │              ├── 📄 EX-V-17-96_2025-12-17_0053.mp4
> │              ├── 📄 EX-V-17-97_2025-12-17_0054.mp4
> │              ├── 📄 EX-V-17-98_2025-12-17_0055.mp4
> │              ├── 📄 EX-V-17-99_2025-12-17_0056.mp4
> │              ├── 📄 index.md
> │            └── 📂 01/
> │              ├── 📄 EX-V-17-103_2025-12-17_0100.mp4
> │              ├── 📄 EX-V-17-104_2025-12-17_0101.mp4
> │              ├── 📄 EX-V-17-105_2025-12-17_0102.mp4
> │              ├── 📄 EX-V-17-106_2025-12-17_0103.mp4
> │              ├── 📄 EX-V-17-107_2025-12-17_0104.mp4
> │              ├── 📄 EX-V-17-108_2025-12-17_0105.mp4
> │              ├── 📄 EX-V-17-109_2025-12-17_0106.mp4
> │              ├── 📄 EX-V-17-110_2025-12-17_0107.mp4
> │              ├── 📄 EX-V-17-111_2025-12-17_0108.mp4
> │              ├── 📄 EX-V-17-112_2025-12-17_0109.mp4
> │              ├── 📄 EX-V-17-113_2025-12-17_0110.mp4
> │              ├── 📄 EX-V-17-114_2025-12-17_0111.mp4
> │              ├── 📄 EX-V-17-115_2025-12-17_0112.mp4
> │              ├── 📄 EX-V-17-116_2025-12-17_0113.mp4
> │              ├── 📄 EX-V-17-117_2025-12-17_0114.mp4
> │              ├── 📄 EX-V-17-118_2025-12-17_0115.mp4
> │              ├── 📄 EX-V-17-119_2025-12-17_0116.mp4
> │              ├── 📄 EX-V-17-120_2025-12-17_0117.mp4
> │              ├── 📄 EX-V-17-121_2025-12-17_0118.mp4
> │              ├── 📄 EX-V-17-122_2025-12-17_0119.mp4
> │              ├── 📄 EX-V-17-123_2025-12-17_0120.mp4
> │              ├── 📄 EX-V-17-124_2025-12-17_0121.mp4
> │              ├── 📄 EX-V-17-125_2025-12-17_0122.mp4
> │              ├── 📄 EX-V-17-126_2025-12-17_0123.mp4
> │              ├── 📄 EX-V-17-127_2025-12-17_0124.mp4
> │              ├── 📄 EX-V-17-128_2025-12-17_0125.mp4
> │              ├── 📄 EX-V-17-129_2025-12-17_0126.mp4
> │              ├── 📄 EX-V-17-130_2025-12-17_0127.mp4
> │              ├── 📄 EX-V-17-131_2025-12-17_0128.mp4
> │              ├── 📄 EX-V-17-132_2025-12-17_0129.mp4
> │              ├── 📄 EX-V-17-133_2025-12-17_0130.mp4
> │              ├── 📄 EX-V-17-134_2025-12-17_0131.mp4
> │              ├── 📄 EX-V-17-135_2025-12-17_0132.mp4
> │              ├── 📄 EX-V-17-136_2025-12-17_0133.mp4
> │              ├── 📄 EX-V-17-137_2025-12-17_0134.mp4
> │              ├── 📄 EX-V-17-138_2025-12-17_0135.mp4
> │              ├── 📄 EX-V-17-139_2025-12-17_0136.mp4
> │              ├── 📄 EX-V-17-140_2025-12-17_0137.mp4
> │              ├── 📄 EX-V-17-141_2025-12-17_0138.mp4
> │              ├── 📄 EX-V-17-142_2025-12-17_0139.mp4
> │              ├── 📄 EX-V-17-143_2025-12-17_0140.mp4
> │              ├── 📄 EX-V-17-144_2025-12-17_0141.mp4
> │              ├── 📄 EX-V-17-145_2025-12-17_0142.mp4
> │              ├── 📄 EX-V-17-146_2025-12-17_0143.mp4
> │              ├── 📄 EX-V-17-147_2025-12-17_0144.mp4
> │              ├── 📄 EX-V-17-148_2025-12-17_0145.mp4
> │              ├── 📄 EX-V-17-149_2025-12-17_0146.mp4
> │              ├── 📄 EX-V-17-150_2025-12-17_0147.mp4
> │              ├── 📄 EX-V-17-151_2025-12-17_0148.mp4
> │              ├── 📄 EX-V-17-152_2025-12-17_0149.mp4
> │              ├── 📄 EX-V-17-153_2025-12-17_0150.mp4
> │              ├── 📄 EX-V-17-154_2025-12-17_0151.mp4
> │              ├── 📄 EX-V-17-155_2025-12-17_0152.mp4
> │              ├── 📄 EX-V-17-156_2025-12-17_0153.mp4
> │              ├── 📄 EX-V-17-157_2025-12-17_0154.mp4
> │              ├── 📄 EX-V-17-158_2025-12-17_0155.mp4
> │              ├── 📄 EX-V-17-159_2025-12-17_0156.mp4
> │              ├── 📄 EX-V-17-160_2025-12-17_0157.mp4
> │              ├── 📄 EX-V-17-161_2025-12-17_0158.mp4
> │              ├── 📄 EX-V-17-162_2025-12-17_0159.mp4
> │              ├── 📄 index.md
> │            └── 📂 02/
> │              ├── 📄 EX-V-17-163_2025-12-17_0200.mp4
> │              ├── 📄 EX-V-17-164_2025-12-17_0201.mp4
> │              ├── 📄 EX-V-17-165_2025-12-17_0202.mp4
> │              ├── 📄 EX-V-17-166_2025-12-17_0203.mp4
> │              ├── 📄 EX-V-17-167_2025-12-17_0204.mp4
> │              ├── 📄 EX-V-17-168_2025-12-17_0205.mp4
> │              ├── 📄 EX-V-17-169_2025-12-17_0206.mp4
> │              ├── 📄 EX-V-17-170_2025-12-17_0207.mp4
> │              ├── 📄 EX-V-17-171_2025-12-17_0208.mp4
> │              ├── 📄 EX-V-17-172_2025-12-17_0209.mp4
> │              ├── 📄 EX-V-17-173_2025-12-17_0210.mp4
> │              ├── 📄 EX-V-17-174_2025-12-17_0211.mp4
> │              ├── 📄 EX-V-17-175_2025-12-17_0212.mp4
> │              ├── 📄 EX-V-17-176_2025-12-17_0213.mp4
> │              ├── 📄 EX-V-17-177_2025-12-17_0214.mp4
> │              ├── 📄 EX-V-17-178_2025-12-17_0215.mp4
> │              ├── 📄 EX-V-17-179_2025-12-17_0216.mp4
> │              ├── 📄 EX-V-17-180_2025-12-17_0217.mp4
> │              ├── 📄 EX-V-17-181_2025-12-17_0218.mp4
> │              ├── 📄 EX-V-17-182_2025-12-17_0219.mp4
> │              ├── 📄 EX-V-17-183_2025-12-17_0220.mp4
> │              ├── 📄 EX-V-17-184_2025-12-17_0221.mp4
> │              ├── 📄 EX-V-17-185_2025-12-17_0222.mp4
> │              ├── 📄 EX-V-17-186_2025-12-17_0223.mp4
> │              ├── 📄 EX-V-17-187_2025-12-17_0224.mp4
> │              ├── 📄 EX-V-17-188_2025-12-17_0225.mp4
> │              ├── 📄 EX-V-17-189_2025-12-17_0226.mp4
> │              ├── 📄 EX-V-17-190_2025-12-17_0227.mp4
> │              ├── 📄 EX-V-17-191_2025-12-17_0228.mp4
> │              ├── 📄 EX-V-17-192_2025-12-17_0229.mp4
> │              ├── 📄 EX-V-17-193_2025-12-17_0230.mp4
> │              ├── 📄 EX-V-17-194_2025-12-17_0231.mp4
> │              ├── 📄 EX-V-17-195_2025-12-17_0232.mp4
> │              ├── 📄 EX-V-17-196_2025-12-17_0233.mp4
> │              ├── 📄 EX-V-17-197_2025-12-17_0234.mp4
> │              ├── 📄 EX-V-17-198_2025-12-17_0235.mp4
> │              ├── 📄 EX-V-17-199_2025-12-17_0236.mp4
> │              ├── 📄 EX-V-17-200_2025-12-17_0237.mp4
> │              ├── 📄 EX-V-17-201_2025-12-17_0238.mp4
> │              ├── 📄 EX-V-17-202_2025-12-17_0239.mp4
> │              ├── 📄 EX-V-17-203_2025-12-17_0240.mp4
> │              ├── 📄 EX-V-17-204_2025-12-17_0241.mp4
> │              ├── 📄 EX-V-17-205_2025-12-17_0242.mp4
> │              ├── 📄 EX-V-17-206_2025-12-17_0243.mp4
> │              ├── 📄 EX-V-17-207_2025-12-17_0244.mp4
> │              ├── 📄 EX-V-17-208_2025-12-17_0245.mp4
> │              ├── 📄 EX-V-17-209_2025-12-17_0246.mp4
> │              ├── 📄 EX-V-17-210_2025-12-17_0247.mp4
> │              ├── 📄 EX-V-17-211_2025-12-17_0248.mp4
> │              ├── 📄 EX-V-17-212_2025-12-17_0249.mp4
> │              ├── 📄 EX-V-17-213_2025-12-17_0250.mp4
> │              ├── 📄 EX-V-17-214_2025-12-17_0251.mp4
> │              ├── 📄 EX-V-17-215_2025-12-17_0252.mp4
> │              ├── 📄 EX-V-17-216_2025-12-17_0253.mp4
> │              ├── 📄 EX-V-17-217_2025-12-17_0254.mp4
> │              ├── 📄 EX-V-17-218_2025-12-17_0255.mp4
> │              ├── 📄 EX-V-17-219_2025-12-17_0256.mp4
> │              ├── 📄 EX-V-17-220_2025-12-17_0257.mp4
> │              ├── 📄 EX-V-17-221_2025-12-17_0258.mp4
> │              ├── 📄 EX-V-17-222_2025-12-17_0259.mp4
> │              ├── 📄 index.md
> │            └── 📂 03/
> │              ├── 📄 EX-V-17-223_2025-12-17_0300.mp4
> │              ├── 📄 EX-V-17-224_2025-12-17_0301.mp4
> │              ├── 📄 EX-V-17-225_2025-12-17_0302.mp4
> │              ├── 📄 EX-V-17-226_2025-12-17_0303.mp4
> │              ├── 📄 EX-V-17-227_2025-12-17_0304.mp4
> │              ├── 📄 EX-V-17-228_2025-12-17_0305.mp4
> │              ├── 📄 EX-V-17-229_2025-12-17_0306.mp4
> │              ├── 📄 EX-V-17-230_2025-12-17_0307.mp4
> │              ├── 📄 EX-V-17-231_2025-12-17_0308.mp4
> │              ├── 📄 EX-V-17-232_2025-12-17_0309.mp4
> │              ├── 📄 EX-V-17-233_2025-12-17_0310.mp4
> │              ├── 📄 EX-V-17-234_2025-12-17_0311.mp4
> │              ├── 📄 EX-V-17-235_2025-12-17_0312.mp4
> │              ├── 📄 EX-V-17-236_2025-12-17_0313.mp4
> │              ├── 📄 EX-V-17-237_2025-12-17_0314.mp4
> │              ├── 📄 EX-V-17-238_2025-12-17_0315.mp4
> │              ├── 📄 EX-V-17-239_2025-12-17_0316.mp4
> │              ├── 📄 EX-V-17-240_2025-12-17_0317.mp4
> │              ├── 📄 EX-V-17-241_2025-12-17_0318.mp4
> │              ├── 📄 EX-V-17-242_2025-12-17_0319.mp4
> │              ├── 📄 EX-V-17-243_2025-12-17_0320.mp4
> │              ├── 📄 EX-V-17-244_2025-12-17_0321.mp4
> │              ├── 📄 EX-V-17-245_2025-12-17_0322.mp4
> │              ├── 📄 EX-V-17-246_2025-12-17_0323.mp4
> │              ├── 📄 EX-V-17-247_2025-12-17_0324.mp4
> │              ├── 📄 EX-V-17-248_2025-12-17_0325.mp4
> │              ├── 📄 EX-V-17-249_2025-12-17_0326.mp4
> │              ├── 📄 EX-V-17-250_2025-12-17_0327.mp4
> │              ├── 📄 EX-V-17-251_2025-12-17_0328.mp4
> │              ├── 📄 EX-V-17-252_2025-12-17_0329.mp4
> │              ├── 📄 EX-V-17-253_2025-12-17_0330.mp4
> │              ├── 📄 EX-V-17-254_2025-12-17_0331.mp4
> │              ├── 📄 EX-V-17-255_2025-12-17_0332.mp4
> │              ├── 📄 EX-V-17-256_2025-12-17_0333.mp4
> │              ├── 📄 EX-V-17-257_2025-12-17_0334.mp4
> │              ├── 📄 EX-V-17-258_2025-12-17_0335.mp4
> │              ├── 📄 EX-V-17-259_2025-12-17_0336.mp4
> │              ├── 📄 EX-V-17-260_2025-12-17_0337.mp4
> │              ├── 📄 EX-V-17-261_2025-12-17_0338.mp4
> │              ├── 📄 EX-V-17-262_2025-12-17_0339.mp4
> │              ├── 📄 EX-V-17-263_2025-12-17_0340.mp4
> │              ├── 📄 EX-V-17-264_2025-12-17_0341.mp4
> │              ├── 📄 EX-V-17-265_2025-12-17_0342.mp4
> │              ├── 📄 EX-V-17-266_2025-12-17_0343.mp4
> │              ├── 📄 EX-V-17-267_2025-12-17_0344.mp4
> │              ├── 📄 EX-V-17-268_2025-12-17_0345.mp4
> │              ├── 📄 EX-V-17-269_2025-12-17_0346.mp4
> │              ├── 📄 EX-V-17-270_2025-12-17_0347.mp4
> │              ├── 📄 EX-V-17-271_2025-12-17_0348.mp4
> │              ├── 📄 EX-V-17-272_2025-12-17_0349.mp4
> │              ├── 📄 EX-V-17-273_2025-12-17_0350.mp4
> │              ├── 📄 EX-V-17-274_2025-12-17_0351.mp4
> │              ├── 📄 EX-V-17-275_2025-12-17_0352.mp4
> │              ├── 📄 EX-V-17-276_2025-12-17_0353.mp4
> │              ├── 📄 EX-V-17-277_2025-12-17_0354.mp4
> │              ├── 📄 EX-V-17-278_2025-12-17_0355.mp4
> │              ├── 📄 EX-V-17-279_2025-12-17_0356.mp4
> │              ├── 📄 EX-V-17-280_2025-12-17_0357.mp4
> │              ├── 📄 EX-V-17-281_2025-12-17_0358.mp4
> │              ├── 📄 EX-V-17-282_2025-12-17_0359.mp4
> │              ├── 📄 index.md
> │            └── 📂 04/
> │              ├── 📄 EX-V-17-283_2025-12-17_0400.mp4
> │              ├── 📄 EX-V-17-284_2025-12-17_0401.mp4
> │              ├── 📄 EX-V-17-285_2025-12-17_0402.mp4
> │              ├── 📄 EX-V-17-286_2025-12-17_0403.mp4
> │              ├── 📄 EX-V-17-287_2025-12-17_0404.mp4
> │              ├── 📄 EX-V-17-288_2025-12-17_0405.mp4
> │              ├── 📄 EX-V-17-289_2025-12-17_0406.mp4
> │              ├── 📄 EX-V-17-290_2025-12-17_0407.mp4
> │              ├── 📄 EX-V-17-291_2025-12-17_0408.mp4
> │              ├── 📄 EX-V-17-292_2025-12-17_0409.mp4
> │              ├── 📄 EX-V-17-293_2025-12-17_0410.mp4
> │              ├── 📄 EX-V-17-294_2025-12-17_0411.mp4
> │              ├── 📄 EX-V-17-295_2025-12-17_0412.mp4
> │              ├── 📄 EX-V-17-296_2025-12-17_0413.mp4
> │              ├── 📄 EX-V-17-297_2025-12-17_0414.mp4
> │              ├── 📄 EX-V-17-298_2025-12-17_0415.mp4
> │              ├── 📄 EX-V-17-299_2025-12-17_0416.mp4
> │              ├── 📄 EX-V-17-300_2025-12-17_0417.mp4
> │              ├── 📄 EX-V-17-301_2025-12-17_0418.mp4
> │              ├── 📄 EX-V-17-302_2025-12-17_0419.mp4
> │              ├── 📄 EX-V-17-303_2025-12-17_0420.mp4
> │              ├── 📄 EX-V-17-304_2025-12-17_0421.mp4
> │              ├── 📄 EX-V-17-305_2025-12-17_0422.mp4
> │              ├── 📄 EX-V-17-306_2025-12-17_0423.mp4
> │              ├── 📄 EX-V-17-307_2025-12-17_0424.mp4
> │              ├── 📄 EX-V-17-308_2025-12-17_0425.mp4
> │              ├── 📄 EX-V-17-309_2025-12-17_0426.mp4
> │              ├── 📄 EX-V-17-310_2025-12-17_0427.mp4
> │              ├── 📄 EX-V-17-311_2025-12-17_0428.mp4
> │              ├── 📄 EX-V-17-312_2025-12-17_0429.mp4
> │              ├── 📄 EX-V-17-313_2025-12-17_0430.mp4
> │              ├── 📄 EX-V-17-314_2025-12-17_0431.mp4
> │              ├── 📄 EX-V-17-315_2025-12-17_0432.mp4
> │              ├── 📄 EX-V-17-316_2025-12-17_0433.mp4
> │              ├── 📄 EX-V-17-317_2025-12-17_0434.mp4
> │              ├── 📄 EX-V-17-318_2025-12-17_0435.mp4
> │              ├── 📄 EX-V-17-319_2025-12-17_0436.mp4
> │              ├── 📄 EX-V-17-320_2025-12-17_0437.mp4
> │              ├── 📄 EX-V-17-321_2025-12-17_0438.mp4
> │              ├── 📄 EX-V-17-322_2025-12-17_0439.mp4
> │              ├── 📄 EX-V-17-323_2025-12-17_0440.mp4
> │              ├── 📄 EX-V-17-324_2025-12-17_0441.mp4
> │              ├── 📄 EX-V-17-325_2025-12-17_0442.mp4
> │              ├── 📄 EX-V-17-326_2025-12-17_0443.mp4
> │              ├── 📄 EX-V-17-327_2025-12-17_0444.mp4
> │              ├── 📄 EX-V-17-328_2025-12-17_0445.mp4
> │              ├── 📄 EX-V-17-329_2025-12-17_0446.mp4
> │              ├── 📄 EX-V-17-330_2025-12-17_0447.mp4
> │              ├── 📄 EX-V-17-331_2025-12-17_0448.mp4
> │              ├── 📄 EX-V-17-332_2025-12-17_0449.mp4
> │              ├── 📄 EX-V-17-333_2025-12-17_0450.mp4
> │              ├── 📄 EX-V-17-334_2025-12-17_0451.mp4
> │              ├── 📄 EX-V-17-335_2025-12-17_0452.mp4
> │              ├── 📄 EX-V-17-336_2025-12-17_0453.mp4
> │              ├── 📄 EX-V-17-337_2025-12-17_0454.mp4
> │              ├── 📄 EX-V-17-338_2025-12-17_0455.mp4
> │              ├── 📄 EX-V-17-339_2025-12-17_0456.mp4
> │              ├── 📄 EX-V-17-340_2025-12-17_0457.mp4
> │              ├── 📄 EX-V-17-341_2025-12-17_0458.mp4
> │              ├── 📄 EX-V-17-342_2025-12-17_0459.mp4
> │              ├── 📄 index.md
> │            └── 📂 05/
> │              ├── 📄 EX-V-17-343_2025-12-17_0500.mp4
> │              ├── 📄 EX-V-17-344_2025-12-17_0501.mp4
> │              ├── 📄 EX-V-17-345_2025-12-17_0502.mp4
> │              ├── 📄 EX-V-17-346_2025-12-17_0503.mp4
> │              ├── 📄 EX-V-17-347_2025-12-17_0504.mp4
> │              ├── 📄 EX-V-17-348_2025-12-17_0505.mp4
> │              ├── 📄 EX-V-17-349_2025-12-17_0506.mp4
> │              ├── 📄 EX-V-17-350_2025-12-17_0507.mp4
> │              ├── 📄 EX-V-17-351_2025-12-17_0508.mp4
> │              ├── 📄 EX-V-17-352_2025-12-17_0509.mp4
> │              ├── 📄 EX-V-17-353_2025-12-17_0510.mp4
> │              ├── 📄 EX-V-17-354_2025-12-17_0511.mp4
> │              ├── 📄 EX-V-17-355_2025-12-17_0512.mp4
> │              ├── 📄 EX-V-17-356_2025-12-17_0513.mp4
> │              ├── 📄 EX-V-17-357_2025-12-17_0514.mp4
> │              ├── 📄 EX-V-17-358_2025-12-17_0515.mp4
> │              ├── 📄 EX-V-17-359_2025-12-17_0516.mp4
> │              ├── 📄 EX-V-17-360_2025-12-17_0517.mp4
> │              ├── 📄 EX-V-17-361_2025-12-17_0518.mp4
> │              ├── 📄 EX-V-17-362_2025-12-17_0519.mp4
> │              ├── 📄 EX-V-17-363_2025-12-17_0520.mp4
> │              ├── 📄 EX-V-17-364_2025-12-17_0521.mp4
> │              ├── 📄 EX-V-17-365_2025-12-17_0522.mp4
> │              ├── 📄 EX-V-17-366_2025-12-17_0523.mp4
> │              ├── 📄 EX-V-17-367_2025-12-17_0524.mp4
> │              ├── 📄 EX-V-17-368_2025-12-17_0525.mp4
> │              ├── 📄 EX-V-17-369_2025-12-17_0526.mp4
> │              ├── 📄 EX-V-17-370_2025-12-17_0527.mp4
> │              ├── 📄 EX-V-17-371_2025-12-17_0528.mp4
> │              ├── 📄 EX-V-17-372_2025-12-17_0529.mp4
> │              ├── 📄 EX-V-17-373_2025-12-17_0530.mp4
> │              ├── 📄 EX-V-17-374_2025-12-17_0531.mp4
> │              ├── 📄 EX-V-17-375_2025-12-17_0532.mp4
> │              ├── 📄 EX-V-17-376_2025-12-17_0533.mp4
> │              ├── 📄 EX-V-17-377_2025-12-17_0534.mp4
> │              ├── 📄 EX-V-17-378_2025-12-17_0535.mp4
> │              ├── 📄 EX-V-17-379_2025-12-17_0536.mp4
> │              ├── 📄 EX-V-17-380_2025-12-17_0537.mp4
> │              ├── 📄 EX-V-17-381_2025-12-17_0538.mp4
> │              ├── 📄 EX-V-17-382_2025-12-17_0539.mp4
> │              ├── 📄 EX-V-17-383_2025-12-17_0540.mp4
> │              ├── 📄 EX-V-17-384_2025-12-17_0541.mp4
> │              ├── 📄 EX-V-17-385_2025-12-17_0542.mp4
> │              ├── 📄 EX-V-17-386_2025-12-17_0543.mp4
> │              ├── 📄 EX-V-17-387_2025-12-17_0544.mp4
> │              ├── 📄 EX-V-17-388_2025-12-17_0545.mp4
> │              ├── 📄 EX-V-17-389_2025-12-17_0546.mp4
> │              ├── 📄 EX-V-17-390_2025-12-17_0547.mp4
> │              ├── 📄 EX-V-17-391_2025-12-17_0548.mp4
> │              ├── 📄 EX-V-17-392_2025-12-17_0549.mp4
> │              ├── 📄 EX-V-17-393_2025-12-17_0550.mp4
> │              ├── 📄 EX-V-17-394_2025-12-17_0551.mp4
> │              ├── 📄 EX-V-17-395_2025-12-17_0552.mp4
> │              ├── 📄 EX-V-17-396_2025-12-17_0553.mp4
> │              ├── 📄 EX-V-17-397_2025-12-17_0554.mp4
> │              ├── 📄 EX-V-17-398_2025-12-17_0555.mp4
> │              ├── 📄 EX-V-17-399_2025-12-17_0556.mp4
> │              ├── 📄 EX-V-17-400_2025-12-17_0557.mp4
> │              ├── 📄 EX-V-17-401_2025-12-17_0558.mp4
> │              ├── 📄 EX-V-17-402_2025-12-17_0559.mp4
> │              ├── 📄 index.md
> │            └── 📂 06/
> │              ├── 📄 EX-V-17-403_2025-12-17_0600.mp4
> │              ├── 📄 EX-V-17-404_2025-12-17_0601.mp4
> │              ├── 📄 EX-V-17-405_2025-12-17_0602.mp4
> │              ├── 📄 EX-V-17-406_2025-12-17_0603.mp4
> │              ├── 📄 EX-V-17-407_2025-12-17_0604.mp4
> │              ├── 📄 EX-V-17-408_2025-12-17_0605.mp4
> │              ├── 📄 EX-V-17-409_2025-12-17_0606.mp4
> │              ├── 📄 EX-V-17-410_2025-12-17_0607.mp4
> │              ├── 📄 EX-V-17-411_2025-12-17_0608.mp4
> │              ├── 📄 EX-V-17-412_2025-12-17_0609.mp4
> │              ├── 📄 EX-V-17-413_2025-12-17_0610.mp4
> │              ├── 📄 EX-V-17-414_2025-12-17_0611.mp4
> │              ├── 📄 EX-V-17-415_2025-12-17_0612.mp4
> │              ├── 📄 EX-V-17-416_2025-12-17_0613.mp4
> │              ├── 📄 EX-V-17-417_2025-12-17_0614.mp4
> │              ├── 📄 EX-V-17-418_2025-12-17_0615.mp4
> │              ├── 📄 EX-V-17-419_2025-12-17_0616.mp4
> │              ├── 📄 EX-V-17-420_2025-12-17_0617.mp4
> │              ├── 📄 EX-V-17-421_2025-12-17_0618.mp4
> │              ├── 📄 EX-V-17-422_2025-12-17_0619.mp4
> │              ├── 📄 EX-V-17-423_2025-12-17_0620.mp4
> │              ├── 📄 EX-V-17-424_2025-12-17_0621.mp4
> │              ├── 📄 EX-V-17-425_2025-12-17_0622.mp4
> │              ├── 📄 EX-V-17-426_2025-12-17_0623.mp4
> │              ├── 📄 EX-V-17-427_2025-12-17_0624.mp4
> │              ├── 📄 EX-V-17-428_2025-12-17_0625.mp4
> │              ├── 📄 EX-V-17-429_2025-12-17_0626.mp4
> │              ├── 📄 EX-V-17-430_2025-12-17_0627.mp4
> │              ├── 📄 EX-V-17-431_2025-12-17_0628.mp4
> │              ├── 📄 EX-V-17-432_2025-12-17_0629.mp4
> │              ├── 📄 EX-V-17-433_2025-12-17_0630.mp4
> │              ├── 📄 EX-V-17-434_2025-12-17_0631.mp4
> │              ├── 📄 EX-V-17-435_2025-12-17_0632.mp4
> │              ├── 📄 EX-V-17-436_2025-12-17_0633.mp4
> │              ├── 📄 EX-V-17-437_2025-12-17_0634.mp4
> │              ├── 📄 EX-V-17-438_2025-12-17_0635.mp4
> │              ├── 📄 EX-V-17-439_2025-12-17_0636.mp4
> │              ├── 📄 EX-V-17-440_2025-12-17_0637.mp4
> │              ├── 📄 EX-V-17-441_2025-12-17_0638.mp4
> │              ├── 📄 EX-V-17-442_2025-12-17_0639.mp4
> │              ├── 📄 EX-V-17-443_2025-12-17_0640.mp4
> │              ├── 📄 EX-V-17-444_2025-12-17_0641.mp4
> │              ├── 📄 EX-V-17-445_2025-12-17_0642.mp4
> │              ├── 📄 EX-V-17-446_2025-12-17_0643.mp4
> │              ├── 📄 EX-V-17-447_2025-12-17_0644.mp4
> │              ├── 📄 EX-V-17-448_2025-12-17_0645.mp4
> │              ├── 📄 EX-V-17-449_2025-12-17_0646.mp4
> │              ├── 📄 EX-V-17-450_2025-12-17_0647.mp4
> │              ├── 📄 EX-V-17-451_2025-12-17_0648.mp4
> │              ├── 📄 EX-V-17-452_2025-12-17_0649.mp4
> │              ├── 📄 EX-V-17-453_2025-12-17_0650.mp4
> │              ├── 📄 EX-V-17-454_2025-12-17_0651.mp4
> │              ├── 📄 EX-V-17-455_2025-12-17_0652.mp4
> │              ├── 📄 EX-V-17-456_2025-12-17_0653.mp4
> │              ├── 📄 EX-V-17-457_2025-12-17_0654.mp4
> │              ├── 📄 EX-V-17-458_2025-12-17_0655.mp4
> │              ├── 📄 EX-V-17-459_2025-12-17_0656.mp4
> │              ├── 📄 EX-V-17-460_2025-12-17_0657.mp4
> │              ├── 📄 EX-V-17-461_2025-12-17_0658.mp4
> │              ├── 📄 EX-V-17-462_2025-12-17_0659.mp4
> │              ├── 📄 index.md
> │            └── 📂 07/
> │              ├── 📄 EX-V-17-463_2025-12-17_0700.mp4
> │              ├── 📄 EX-V-17-464_2025-12-17_0701.mp4
> │              ├── 📄 EX-V-17-465_2025-12-17_0702.mp4
> │              ├── 📄 EX-V-17-466_2025-12-17_0703.mp4
> │              ├── 📄 EX-V-17-467_2025-12-17_0704.mp4
> │              ├── 📄 EX-V-17-468_2025-12-17_0705.mp4
> │              ├── 📄 EX-V-17-469_2025-12-17_0706.mp4
> │              ├── 📄 EX-V-17-470_2025-12-17_0707.mp4
> │              ├── 📄 EX-V-17-471_2025-12-17_0708.mp4
> │              ├── 📄 EX-V-17-472_2025-12-17_0709.mp4
> │              ├── 📄 EX-V-17-473_2025-12-17_0710.mp4
> │              ├── 📄 EX-V-17-474_2025-12-17_0711.mp4
> │              ├── 📄 EX-V-17-475_2025-12-17_0712.mp4
> │              ├── 📄 EX-V-17-476_2025-12-17_0713.mp4
> │              ├── 📄 EX-V-17-477_2025-12-17_0714.mp4
> │              ├── 📄 EX-V-17-478_2025-12-17_0715.mp4
> │              ├── 📄 EX-V-17-479_2025-12-17_0716.mp4
> │              ├── 📄 EX-V-17-480_2025-12-17_0717.mp4
> │              ├── 📄 EX-V-17-481_2025-12-17_0718.mp4
> │              ├── 📄 EX-V-17-482_2025-12-17_0719.mp4
> │              ├── 📄 EX-V-17-483_2025-12-17_0720.mp4
> │              ├── 📄 EX-V-17-484_2025-12-17_0721.mp4
> │              ├── 📄 EX-V-17-485_2025-12-17_0722.mp4
> │              ├── 📄 EX-V-17-486_2025-12-17_0723.mp4
> │              ├── 📄 EX-V-17-487_2025-12-17_0724.mp4
> │              ├── 📄 EX-V-17-488_2025-12-17_0725.mp4
> │              ├── 📄 EX-V-17-489_2025-12-17_0726.mp4
> │              ├── 📄 EX-V-17-490_2025-12-17_0727.mp4
> │              ├── 📄 EX-V-17-491_2025-12-17_0728.mp4
> │              ├── 📄 EX-V-17-492_2025-12-17_0729.mp4
> │              ├── 📄 EX-V-17-493_2025-12-17_0730.mp4
> │              ├── 📄 EX-V-17-494_2025-12-17_0731.mp4
> │              ├── 📄 EX-V-17-495_2025-12-17_0732.mp4
> │              ├── 📄 EX-V-17-496_2025-12-17_0733.mp4
> │              ├── 📄 EX-V-17-497_2025-12-17_0734.mp4
> │              ├── 📄 EX-V-17-498_2025-12-17_0735.mp4
> │              ├── 📄 EX-V-17-499_2025-12-17_0736.mp4
> │              ├── 📄 EX-V-17-500_2025-12-17_0737.mp4
> │              ├── 📄 EX-V-17-501_2025-12-17_0738.mp4
> │              ├── 📄 EX-V-17-502_2025-12-17_0739.mp4
> │              ├── 📄 EX-V-17-503_2025-12-17_0740.mp4
> │              ├── 📄 EX-V-17-504_2025-12-17_0741.mp4
> │              ├── 📄 EX-V-17-505_2025-12-17_0742.mp4
> │              ├── 📄 EX-V-17-506_2025-12-17_0743.mp4
> │              ├── 📄 EX-V-17-507_2025-12-17_0744.mp4
> │              ├── 📄 EX-V-17-508_2025-12-17_0745.mp4
> │              ├── 📄 EX-V-17-509_2025-12-17_0746.mp4
> │              ├── 📄 EX-V-17-510_2025-12-17_0747.mp4
> │              ├── 📄 EX-V-17-511_2025-12-17_0748.mp4
> │              ├── 📄 EX-V-17-512_2025-12-17_0749.mp4
> │              ├── 📄 EX-V-17-513_2025-12-17_0750.mp4
> │              ├── 📄 EX-V-17-514_2025-12-17_0751.mp4
> │              ├── 📄 EX-V-17-515_2025-12-17_0752.mp4
> │              ├── 📄 EX-V-17-516_2025-12-17_0753.mp4
> │              ├── 📄 EX-V-17-517_2025-12-17_0754.mp4
> │              ├── 📄 EX-V-17-518_2025-12-17_0755.mp4
> │              ├── 📄 EX-V-17-519_2025-12-17_0756.mp4
> │              ├── 📄 EX-V-17-520_2025-12-17_0757.mp4
> │              ├── 📄 EX-V-17-521_2025-12-17_0758.mp4
> │              ├── 📄 EX-V-17-522_2025-12-17_0759.mp4
> │              ├── 📄 index.md
> │            └── 📂 08/
> │              ├── 📄 EX-V-17-523_2025-12-17_0800.mp4
> │              ├── 📄 EX-V-17-524_2025-12-17_0801.mp4
> │              ├── 📄 EX-V-17-525_2025-12-17_0802.mp4
> │              ├── 📄 EX-V-17-526_2025-12-17_0803.mp4
> │              ├── 📄 EX-V-17-527_2025-12-17_0804.mp4
> │              ├── 📄 EX-V-17-528_2025-12-17_0805.mp4
> │              ├── 📄 EX-V-17-529_2025-12-17_0806.mp4
> │              ├── 📄 EX-V-17-530_2025-12-17_0807.mp4
> │              ├── 📄 EX-V-17-531_2025-12-17_0808.mp4
> │              ├── 📄 EX-V-17-532_2025-12-17_0809.mp4
> │              ├── 📄 EX-V-17-533_2025-12-17_0810.mp4
> │              ├── 📄 EX-V-17-534_2025-12-17_0811.mp4
> │              ├── 📄 EX-V-17-535_2025-12-17_0812.mp4
> │              ├── 📄 EX-V-17-536_2025-12-17_0813.mp4
> │              ├── 📄 EX-V-17-537_2025-12-17_0814.mp4
> │              ├── 📄 EX-V-17-538_2025-12-17_0815.mp4
> │              ├── 📄 EX-V-17-539_2025-12-17_0816.mp4
> │              ├── 📄 EX-V-17-540_2025-12-17_0817.mp4
> │              ├── 📄 EX-V-17-541_2025-12-17_0818.mp4
> │              ├── 📄 EX-V-17-542_2025-12-17_0819.mp4
> │              ├── 📄 EX-V-17-543_2025-12-17_0820.mp4
> │              ├── 📄 EX-V-17-544_2025-12-17_0821.mp4
> │              ├── 📄 EX-V-17-545_2025-12-17_0822.mp4
> │              ├── 📄 EX-V-17-546_2025-12-17_0823.mp4
> │              ├── 📄 EX-V-17-547_2025-12-17_0824.mp4
> │              ├── 📄 EX-V-17-548_2025-12-17_0825.mp4
> │              ├── 📄 EX-V-17-549_2025-12-17_0826.mp4
> │              ├── 📄 EX-V-17-550_2025-12-17_0827.mp4
> │              ├── 📄 EX-V-17-551_2025-12-17_0828.mp4
> │              ├── 📄 EX-V-17-552_2025-12-17_0829.mp4
> │              ├── 📄 EX-V-17-553_2025-12-17_0830.mp4
> │              ├── 📄 EX-V-17-554_2025-12-17_0831.mp4
> │              ├── 📄 EX-V-17-555_2025-12-17_0832.mp4
> │              ├── 📄 EX-V-17-556_2025-12-17_0833.mp4
> │              ├── 📄 EX-V-17-557_2025-12-17_0834.mp4
> │              ├── 📄 EX-V-17-558_2025-12-17_0835.mp4
> │              ├── 📄 EX-V-17-559_2025-12-17_0836.mp4
> │              ├── 📄 EX-V-17-560_2025-12-17_0837.mp4
> │              ├── 📄 EX-V-17-561_2025-12-17_0838.mp4
> │              ├── 📄 EX-V-17-562_2025-12-17_0839.mp4
> │              ├── 📄 EX-V-17-563_2025-12-17_0840.mp4
> │              ├── 📄 EX-V-17-564_2025-12-17_0841.mp4
> │              ├── 📄 EX-V-17-565_2025-12-17_0842.mp4
> │              ├── 📄 EX-V-17-566_2025-12-17_0843.mp4
> │              ├── 📄 EX-V-17-567_2025-12-17_0844.mp4
> │              ├── 📄 EX-V-17-568_2025-12-17_0845.mp4
> │              ├── 📄 EX-V-17-569_2025-12-17_0846.mp4
> │              ├── 📄 EX-V-17-570_2025-12-17_0847.mp4
> │              ├── 📄 EX-V-17-571_2025-12-17_0848.mp4
> │              ├── 📄 EX-V-17-572_2025-12-17_0849.mp4
> │              ├── 📄 EX-V-17-573_2025-12-17_0850.mp4
> │              ├── 📄 EX-V-17-574_2025-12-17_0851.mp4
> │              ├── 📄 EX-V-17-575_2025-12-17_0852.mp4
> │              ├── 📄 EX-V-17-576_2025-12-17_0853.mp4
> │              ├── 📄 EX-V-17-577_2025-12-17_0854.mp4
> │              ├── 📄 EX-V-17-578_2025-12-17_0855.mp4
> │              ├── 📄 EX-V-17-579_2025-12-17_0856.mp4
> │              ├── 📄 EX-V-17-580_2025-12-17_0857.mp4
> │              ├── 📄 EX-V-17-581_2025-12-17_0858.mp4
> │              ├── 📄 EX-V-17-582_2025-12-17_0859.mp4
> │              ├── 📄 index.md
> │            └── 📂 09/
> │              ├── 📄 EX-V-17-583_2025-12-17_0900.mp4
> │              ├── 📄 EX-V-17-584_2025-12-17_0901.mp4
> │              ├── 📄 EX-V-17-585_2025-12-17_0902.mp4
> │              ├── 📄 EX-V-17-586_2025-12-17_0903.mp4
> │              ├── 📄 EX-V-17-587_2025-12-17_0904.mp4
> │              ├── 📄 EX-V-17-588_2025-12-17_0905.mp4
> │              ├── 📄 EX-V-17-589_2025-12-17_0906.mp4
> │              ├── 📄 EX-V-17-590_2025-12-17_0907.mp4
> │              ├── 📄 EX-V-17-591_2025-12-17_0908.mp4
> │              ├── 📄 EX-V-17-592_2025-12-17_0909.mp4
> │              ├── 📄 EX-V-17-593_2025-12-17_0910.mp4
> │              ├── 📄 EX-V-17-594_2025-12-17_0911.mp4
> │              ├── 📄 EX-V-17-595_2025-12-17_0912.mp4
> │              ├── 📄 EX-V-17-596_2025-12-17_0913.mp4
> │              ├── 📄 EX-V-17-597_2025-12-17_0914.mp4
> │              ├── 📄 EX-V-17-598_2025-12-17_0915.mp4
> │              ├── 📄 EX-V-17-599_2025-12-17_0916.mp4
> │              ├── 📄 EX-V-17-600_2025-12-17_0917.mp4
> │              ├── 📄 EX-V-17-601_2025-12-17_0918.mp4
> │              ├── 📄 EX-V-17-602_2025-12-17_0919.mp4
> │              ├── 📄 EX-V-17-603_2025-12-17_0920.mp4
> │              ├── 📄 EX-V-17-604_2025-12-17_0921.mp4
> │              ├── 📄 EX-V-17-605_2025-12-17_0922.mp4
> │              ├── 📄 EX-V-17-606_2025-12-17_0923.mp4
> │              ├── 📄 EX-V-17-607_2025-12-17_0924.mp4
> │              ├── 📄 EX-V-17-608_2025-12-17_0925.mp4
> │              ├── 📄 EX-V-17-609_2025-12-17_0926.mp4
> │              ├── 📄 EX-V-17-610_2025-12-17_0927.mp4
> │              ├── 📄 EX-V-17-611_2025-12-17_0928.mp4
> │              ├── 📄 EX-V-17-612_2025-12-17_0929.mp4
> │              ├── 📄 EX-V-17-613_2025-12-17_0930.mp4
> │              ├── 📄 EX-V-17-614_2025-12-17_0931.mp4
> │              ├── 📄 EX-V-17-615_2025-12-17_0932.mp4
> │              ├── 📄 EX-V-17-616_2025-12-17_0933.mp4
> │              ├── 📄 EX-V-17-617_2025-12-17_0934.mp4
> │              ├── 📄 EX-V-17-618_2025-12-17_0935.mp4
> │              ├── 📄 EX-V-17-619_2025-12-17_0936.mp4
> │              ├── 📄 EX-V-17-620_2025-12-17_0937.mp4
> │              ├── 📄 EX-V-17-621_2025-12-17_0938.mp4
> │              ├── 📄 EX-V-17-622_2025-12-17_0939.mp4
> │              ├── 📄 EX-V-17-623_2025-12-17_0940.mp4
> │              ├── 📄 EX-V-17-624_2025-12-17_0941.mp4
> │              ├── 📄 EX-V-17-625_2025-12-17_0942.mp4
> │              ├── 📄 EX-V-17-626_2025-12-17_0943.mp4
> │              ├── 📄 EX-V-17-627_2025-12-17_0944.mp4
> │              ├── 📄 EX-V-17-628_2025-12-17_0945.mp4
> │              ├── 📄 EX-V-17-629_2025-12-17_0946.mp4
> │              ├── 📄 EX-V-17-630_2025-12-17_0947.mp4
> │              ├── 📄 EX-V-17-631_2025-12-17_0948.mp4
> │              ├── 📄 EX-V-17-632_2025-12-17_0949.mp4
> │              ├── 📄 EX-V-17-633_2025-12-17_0950.mp4
> │              ├── 📄 EX-V-17-634_2025-12-17_0951.mp4
> │              ├── 📄 EX-V-17-635_2025-12-17_0952.mp4
> │              ├── 📄 EX-V-17-636_2025-12-17_0953.mp4
> │              ├── 📄 EX-V-17-637_2025-12-17_0954.mp4
> │              ├── 📄 EX-V-17-638_2025-12-17_0955.mp4
> │              ├── 📄 EX-V-17-639_2025-12-17_0956.mp4
> │              ├── 📄 EX-V-17-640_2025-12-17_0957.mp4
> │              ├── 📄 EX-V-17-641_2025-12-17_0958.mp4
> │              ├── 📄 EX-V-17-642_2025-12-17_0959.mp4
> │              ├── 📄 index.md
> │            └── 📂 10/
> │              ├── 📄 EX-V-17-643_2025-12-17_1000.mp4
> │              ├── 📄 EX-V-17-644_2025-12-17_1001.mp4
> │              ├── 📄 EX-V-17-645_2025-12-17_1002.mp4
> │              ├── 📄 EX-V-17-646_2025-12-17_1003.mp4
> │              ├── 📄 EX-V-17-647_2025-12-17_1004.mp4
> │              ├── 📄 EX-V-17-648_2025-12-17_1005.mp4
> │              ├── 📄 EX-V-17-649_2025-12-17_1006.mp4
> │              ├── 📄 EX-V-17-650_2025-12-17_1007.mp4
> │              ├── 📄 EX-V-17-651_2025-12-17_1008.mp4
> │              ├── 📄 EX-V-17-652_2025-12-17_1009.mp4
> │              ├── 📄 EX-V-17-653_2025-12-17_1010.mp4
> │              ├── 📄 EX-V-17-654_2025-12-17_1011.mp4
> │              ├── 📄 EX-V-17-655_2025-12-17_1012.mp4
> │              ├── 📄 EX-V-17-656_2025-12-17_1013.mp4
> │              ├── 📄 EX-V-17-657_2025-12-17_1014.mp4
> │              ├── 📄 EX-V-17-658_2025-12-17_1015.mp4
> │              ├── 📄 EX-V-17-659_2025-12-17_1016.mp4
> │              ├── 📄 EX-V-17-660_2025-12-17_1017.mp4
> │              ├── 📄 EX-V-17-661_2025-12-17_1018.mp4
> │              ├── 📄 EX-V-17-662_2025-12-17_1019.mp4
> │              ├── 📄 EX-V-17-663_2025-12-17_1020.mp4
> │              ├── 📄 EX-V-17-664_2025-12-17_1021.mp4
> │              ├── 📄 EX-V-17-665_2025-12-17_1022.mp4
> │              ├── 📄 EX-V-17-666_2025-12-17_1023.mp4
> │              ├── 📄 EX-V-17-667_2025-12-17_1024.mp4
> │              ├── 📄 EX-V-17-668_2025-12-17_1025.mp4
> │              ├── 📄 EX-V-17-669_2025-12-17_1026.mp4
> │              ├── 📄 EX-V-17-670_2025-12-17_1027.mp4
> │              ├── 📄 EX-V-17-671_2025-12-17_1028.mp4
> │              ├── 📄 EX-V-17-672_2025-12-17_1029.mp4
> │              ├── 📄 EX-V-17-673_2025-12-17_1030.mp4
> │              ├── 📄 EX-V-17-674_2025-12-17_1031.mp4
> │              ├── 📄 EX-V-17-675_2025-12-17_1032.mp4
> │              ├── 📄 EX-V-17-676_2025-12-17_1033.mp4
> │              ├── 📄 EX-V-17-677_2025-12-17_1034.mp4
> │              ├── 📄 EX-V-17-678_2025-12-17_1035.mp4
> │              ├── 📄 EX-V-17-679_2025-12-17_1036.mp4
> │              ├── 📄 EX-V-17-680_2025-12-17_1037.mp4
> │              ├── 📄 EX-V-17-681_2025-12-17_1038.mp4
> │              ├── 📄 EX-V-17-682_2025-12-17_1038.mp4
> │              ├── 📄 EX-V-17-684_2025-12-17_1039.mp4
> │              ├── 📄 EX-V-17-685_2025-12-17_1039.mp4
> │              ├── 📄 EX-V-17-686_2025-12-17_1040.mp4
> │              ├── 📄 EX-V-17-687_2025-12-17_1041.mp4
> │              ├── 📄 EX-V-17-688_2025-12-17_1042.mp4
> │              ├── 📄 EX-V-17-689_2025-12-17_1043.mp4
> │              ├── 📄 EX-V-17-690_2025-12-17_1044.mp4
> │              ├── 📄 EX-V-17-691_2025-12-17_1045.mp4
> │              ├── 📄 EX-V-17-692_2025-12-17_1046.mp4
> │              ├── 📄 EX-V-17-693_2025-12-17_1047.mp4
> │              ├── 📄 EX-V-17-694_2025-12-17_1048.mp4
> │              ├── 📄 EX-V-17-695_2025-12-17_1049.mp4
> │              ├── 📄 EX-V-17-696_2025-12-17_1050.mp4
> │              ├── 📄 EX-V-17-697_2025-12-17_1051.mp4
> │              ├── 📄 EX-V-17-698_2025-12-17_1052.mp4
> │              ├── 📄 EX-V-17-699_2025-12-17_1053.mp4
> │              ├── 📄 EX-V-17-700_2025-12-17_1054.mp4
> │              ├── 📄 EX-V-17-701_2025-12-17_1055.mp4
> │              ├── 📄 EX-V-17-702_2025-12-17_1056.mp4
> │              ├── 📄 EX-V-17-703_2025-12-17_1057.mp4
> │              ├── 📄 EX-V-17-704_2025-12-17_1058.mp4
> │              ├── 📄 EX-V-17-705_2025-12-17_1058.mp4
> │              ├── 📄 EX-V-17-706_2025-12-17_1059.mp4
> │              ├── 📄 EX-V-17-707_2025-12-17_1059.mp4
> │              ├── 📄 index.md
> │            └── 📂 11/
> │              ├── 📄 EX-V-17-709_2025-12-17_1100.mp4
> │              ├── 📄 EX-V-17-710_2025-12-17_1101.mp4
> │              ├── 📄 EX-V-17-711_2025-12-17_1102.mp4
> │              ├── 📄 EX-V-17-712_2025-12-17_1103.mp4
> │              ├── 📄 EX-V-17-713_2025-12-17_1104.mp4
> │              ├── 📄 EX-V-17-714_2025-12-17_1105.mp4
> │              ├── 📄 EX-V-17-715_2025-12-17_1106.mp4
> │              ├── 📄 EX-V-17-716_2025-12-17_1107.mp4
> │              ├── 📄 EX-V-17-717_2025-12-17_1108.mp4
> │              ├── 📄 EX-V-17-718_2025-12-17_1109.mp4
> │              ├── 📄 EX-V-17-719_2025-12-17_1110.mp4
> │              ├── 📄 EX-V-17-720_2025-12-17_1111.mp4
> │              ├── 📄 EX-V-17-721_2025-12-17_1112.mp4
> │              ├── 📄 EX-V-17-722_2025-12-17_1113.mp4
> │              ├── 📄 EX-V-17-723_2025-12-17_1114.mp4
> │              ├── 📄 EX-V-17-724_2025-12-17_1115.mp4
> │              ├── 📄 EX-V-17-725_2025-12-17_1116.mp4
> │              ├── 📄 EX-V-17-726_2025-12-17_1117.mp4
> │              ├── 📄 EX-V-17-727_2025-12-17_1118.mp4
> │              ├── 📄 EX-V-17-728_2025-12-17_1119.mp4
> │              ├── 📄 EX-V-17-729_2025-12-17_1120.mp4
> │              ├── 📄 EX-V-17-730_2025-12-17_1121.mp4
> │              ├── 📄 EX-V-17-731_2025-12-17_1122.mp4
> │              ├── 📄 EX-V-17-732_2025-12-17_1123.mp4
> │              ├── 📄 EX-V-17-733_2025-12-17_1124.mp4
> │              ├── 📄 EX-V-17-734_2025-12-17_1125.mp4
> │              ├── 📄 EX-V-17-735_2025-12-17_1126.mp4
> │              ├── 📄 EX-V-17-736_2025-12-17_1127.mp4
> │              ├── 📄 EX-V-17-737_2025-12-17_1128.mp4
> │              ├── 📄 EX-V-17-738_2025-12-17_1129.mp4
> │              ├── 📄 EX-V-17-739_2025-12-17_1130.mp4
> │              ├── 📄 EX-V-17-740_2025-12-17_1131.mp4
> │              ├── 📄 EX-V-17-741_2025-12-17_1132.mp4
> │              ├── 📄 EX-V-17-742_2025-12-17_1133.mp4
> │              ├── 📄 EX-V-17-743_2025-12-17_1134.mp4
> │              ├── 📄 EX-V-17-744_2025-12-17_1134.mp4
> │              ├── 📄 EX-V-17-745_2025-12-17_1135.mp4
> │              ├── 📄 EX-V-17-746_2025-12-17_1135.mp4
> │              ├── 📄 EX-V-17-748_2025-12-17_1136.mp4
> │              ├── 📄 EX-V-17-749_2025-12-17_1137.mp4
> │              ├── 📄 EX-V-17-750_2025-12-17_1138.mp4
> │              ├── 📄 EX-V-17-751_2025-12-17_1139.mp4
> │              ├── 📄 EX-V-17-752_2025-12-17_1140.mp4
> │              ├── 📄 EX-V-17-753_2025-12-17_1141.mp4
> │              ├── 📄 EX-V-17-754_2025-12-17_1142.mp4
> │              ├── 📄 EX-V-17-755_2025-12-17_1143.mp4
> │              ├── 📄 EX-V-17-756_2025-12-17_1143.mp4
> │              ├── 📄 EX-V-17-758_2025-12-17_1144.mp4
> │              ├── 📄 EX-V-17-759_2025-12-17_1145.mp4
> │              ├── 📄 EX-V-17-760_2025-12-17_1146.mp4
> │              ├── 📄 EX-V-17-761_2025-12-17_1147.mp4
> │              ├── 📄 EX-V-17-762_2025-12-17_1148.mp4
> │              ├── 📄 EX-V-17-763_2025-12-17_1149.mp4
> │              ├── 📄 EX-V-17-764_2025-12-17_1149.mp4
> │              ├── 📄 EX-V-17-766_2025-12-17_1150.mp4
> │              ├── 📄 EX-V-17-767_2025-12-17_1151.mp4
> │              ├── 📄 EX-V-17-768_2025-12-17_1152.mp4
> │              ├── 📄 EX-V-17-769_2025-12-17_1153.mp4
> │              ├── 📄 EX-V-17-770_2025-12-17_1154.mp4
> │              ├── 📄 EX-V-17-771_2025-12-17_1155.mp4
> │              ├── 📄 EX-V-17-772_2025-12-17_1156.mp4
> │              ├── 📄 EX-V-17-773_2025-12-17_1157.mp4
> │              ├── 📄 EX-V-17-774_2025-12-17_1158.mp4
> │              ├── 📄 EX-V-17-775_2025-12-17_1159.mp4
> │              ├── 📄 index.md
> │            └── 📂 12/
> │              ├── 📄 EX-V-17-776_2025-12-17_1200.mp4
> │              ├── 📄 EX-V-17-777_2025-12-17_1201.mp4
> │              ├── 📄 EX-V-17-778_2025-12-17_1202.mp4
> │              ├── 📄 EX-V-17-779_2025-12-17_1203.mp4
> │              ├── 📄 EX-V-17-780_2025-12-17_1204.mp4
> │              ├── 📄 EX-V-17-781_2025-12-17_1205.mp4
> │              ├── 📄 EX-V-17-782_2025-12-17_1205.mp4
> │              ├── 📄 EX-V-17-784_2025-12-17_1206.mp4
> │              ├── 📄 EX-V-17-785_2025-12-17_1207.mp4
> │              ├── 📄 EX-V-17-786_2025-12-17_1208.mp4
> │              ├── 📄 EX-V-17-787_2025-12-17_1209.mp4
> │              ├── 📄 EX-V-17-788_2025-12-17_1210.mp4
> │              ├── 📄 EX-V-17-789_2025-12-17_1211.mp4
> │              ├── 📄 EX-V-17-790_2025-12-17_1211.mp4
> │              ├── 📄 EX-V-17-792_2025-12-17_1212.mp4
> │              ├── 📄 EX-V-17-793_2025-12-17_1218.mp4
> │              ├── 📄 EX-V-17-795_2025-12-17_1225.mp4
> │              ├── 📄 EX-V-17-797_2025-12-17_1233.mp4
> │              ├── 📄 EX-V-17-798_2025-12-17_1234.mp4
> │              ├── 📄 EX-V-17-800_2025-12-17_1239.mp4
> │              ├── 📄 EX-V-17-802_2025-12-17_1240.mp4
> │              ├── 📄 EX-V-17-803_2025-12-17_1245.mp4
> │              ├── 📄 EX-V-17-805_2025-12-17_1256.mp4
> │              ├── 📄 index.md
> │            └── 📂 15/
> │              ├── 📄 EX-V-17-814_2025-12-17_1500.mp4
> │              ├── 📄 EX-V-17-816_2025-12-17_1507.mp4
> │              ├── 📄 EX-V-17-818_2025-12-17_1508.mp4
> │              ├── 📄 EX-V-17-819_2025-12-17_1546.mp4
> │              ├── 📄 EX-V-17-820_2025-12-17_1547.mp4
> │              ├── 📄 EX-V-17-822_2025-12-17_1552.mp4
> │              ├── 📄 index.md
> │            └── 📂 16/
> │              ├── 📄 EX-V-17-824_2025-12-17_1611.mp4
> │              ├── 📄 EX-V-17-825_2025-12-17_1612.mp4
> │              ├── 📄 EX-V-17-827_2025-12-17_1618.mp4
> │              ├── 📄 EX-V-17-829_2025-12-17_1619.mp4
> │              ├── 📄 EX-V-17-830_2025-12-17_1626.mp4
> │              ├── 📄 EX-V-17-832_2025-12-17_1627.mp4
> │              ├── 📄 EX-V-17-833_2025-12-17_1634.mp4
> │              ├── 📄 EX-V-17-835_2025-12-17_1640.mp4
> │              ├── 📄 index.md
> │          └── 📂 2025-12-17_Retrieval_Day_Photos/
> │            ├── 📄 EX-V-17-683_2025-12-17_1038.jpg
> │            ├── 📄 EX-V-17-708_2025-12-17_1059.jpg
> │            ├── 📄 EX-V-17-747_2025-12-17_1135.jpg
> │            ├── 📄 EX-V-17-757_2025-12-17_1143.jpg
> │            ├── 📄 EX-V-17-765_2025-12-17_1149.jpg
> │            ├── 📄 EX-V-17-783_2025-12-17_1205.jpg
> │            ├── 📄 EX-V-17-791_2025-12-17_1211.jpg
> │            ├── 📄 EX-V-17-794_2025-12-17_1218.jpg
> │            ├── 📄 EX-V-17-796_2025-12-17_1225.jpg
> │            ├── 📄 EX-V-17-799_2025-12-17_1234.jpg
> │            ├── 📄 EX-V-17-801_2025-12-17_1239.jpg
> │            ├── 📄 EX-V-17-804_2025-12-17_1245.jpg
> │            ├── 📄 EX-V-17-806_2025-12-17_1256.jpg
> │            ├── 📄 EX-V-17-807_2025-12-17_1357.jpg
> │            ├── 📄 EX-V-17-808_2025-12-17_1425.jpg
> │            ├── 📄 EX-V-17-809_2025-12-17_1430.jpg
> │            ├── 📄 EX-V-17-810_2025-12-17_1436.jpg
> │            ├── 📄 EX-V-17-811_2025-12-17_1442.jpg
> │            ├── 📄 EX-V-17-812_2025-12-17_1447.jpg
> │            ├── 📄 EX-V-17-813_2025-12-17_1453.jpg
> │            ├── 📄 EX-V-17-815_2025-12-17_1500.jpg
> │            ├── 📄 EX-V-17-817_2025-12-17_1507.jpg
> │            ├── 📄 EX-V-17-821_2025-12-17_1547.jpg
> │            ├── 📄 EX-V-17-823_2025-12-17_1552.jpg
> │            ├── 📄 EX-V-17-826_2025-12-17_1612.jpg
> │            ├── 📄 EX-V-17-828_2025-12-17_1618.jpg
> │            ├── 📄 EX-V-17-831_2025-12-17_1626.jpg
> │            ├── 📄 EX-V-17-834_2025-12-17_1634.jpg
> │            ├── 📄 EX-V-17-836_2025-12-17_1640.jpg
> │            ├── 📄 index.md
> │          ├── 📄 RENAME_RESULTS.txt
> │          ├── 📄 execute_rename.py
> │          ├── 📄 index.md
> │          ├── 📄 review_timeline_frontmatter.py
> │        └── 📂 20_receipts/
> │          ├── 📄 2025-12-20_EXH-20_2025-12-20_07192024_INVOICE_003.jpg
> │          ├── 📄 Zoho One - Subscription Renewal - Final Reminder!.pdf
> │          ├── 📄 index.md
> │        └── 📂 30_declarations/
> │          ├── 📄 2025-12-21_Exhibit_V-03-02_Declaration_Ongoing_Displacement_and_Harm.pdf
> │        └── 📂 40_affidavits/
> │          └── 📂 ada-disability/
> │          └── 📂 character/
> │          └── 📂 community-service/
> │          └── 📂 credibility/
> │          └── 📂 observations/
> │      └── 📂 20_property/
> │        └── 📂 10_mortgage_history/
> │          └── 📂 20_payments/
> │            ├── 📄 2025-12-20_EXH-20_2024-07-12.png
> │            ├── 📄 index.md
> │        └── 📂 20_parcel/
> │          ├── 📄 Parcel_6016506_PRC.pdf
> │          ├── 📄 Parcel_6016506_PRC.pdf.bak
> │          ├── 📄 Parcel_6016506_ParcelDetailHistory.pdf
> │          ├── 📄 index.md
> │      └── 📂 30_fcfcu/
> │        ├── 📄 2023-09-20_FCFCU_Hardship_and_Health_Notice_Letter.pdf
> │        ├── 📄 2023-09-20_FCFCU_Hardship_and_Health_Notice_Letter.pdf.bak
> │        ├── 📄 2023-09-20_FCFCU_Hardship_and_Health_Notice_Letter_Delivery.md
> │        ├── 📄 2023-09-20_Notice_Disabilities_Hardship.pdf
> │        ├── 📄 2023-09-20_Notice_Disabilities_Hardship.pdf.bak
> │        ├── 📄 2024-03-20_FCFCU_Certified_Response_Tax_Records.pdf
> │        ├── 📄 2024-03-20_FCFCU_Certified_Response_Tax_Records.pdf.bak
> │        ├── 📄 2024-12-09_outgoing_email_bank_access_request.pdf
> │        ├── 📄 2024-12-09_outgoing_email_bank_access_request.pdf.bak
> │        ├── 📄 2024-12-11_outgoing_email_bank_access_request.pdf
> │        ├── 📄 2024-12-11_outgoing_email_bank_access_request.pdf.bak
> │        ├── 📄 2024-20-03_Response_to_tax_notice.pdf
> │        ├── 📄 2024-20-03_Response_to_tax_notice.pdf.bak
> │        ├── 📄 20241204_FCFCU_Statement (1).pdf
> │        ├── 📄 20241204_FCFCU_Statement (1).pdf.bak
> │        ├── 📄 20241204_FCFCU_Statement (2).pdf
> │        ├── 📄 20241204_FCFCU_Statement (2).pdf.bak
> │        ├── 📄 20241204_FCFCU_Statement.pdf
> │        ├── 📄 20241204_FCFCU_Statement.pdf.bak
> │        ├── 📄 2025-12-20_EXH-30_fcfcu_740eacdc_2025-12-20_EXH-fcfcu_740eacdc_06212024_ifinancial_ball_state_Vcenter_Vfinancia.jpg
> │        ├── 📄 2025-12-20_EXH-30_fcfcu_ac6eb2ea_2025-12-20_EXH-fcfcu_ac6eb2ea_06212024_ifinancial_ball_state_Vcenter_Vfinancia.jpg
> │        ├── 📄 21June-24-4817Shadow_Appraisal.pdf
> │        ├── 📄 FCFCU_v_CR-V_Report_to_Court.pdf
> │        ├── 📄 FCFCU_v_CR-V_Report_to_Court.pdf.bak
> │        ├── 📄 REPORT_TO_COURT_ON_DEFENDANTS_REQUEST.pdf
> │        ├── 📄 REPORT_TO_COURT_ON_DEFENDANTS_REQUEST.pdf.bak
> │        ├── 📄 index.md
> │      └── 📂 50_aes/
> │        ├── 📄 2025-06-08_AES_ADA_Notice.pdf
> │        ├── 📄 2025-06-08_AES_ADA_Notice.pdf.bak
> │        ├── 📄 2025-06-08_AES_ADA_Request_Financial_Hardship_Relief.pdf
> │        ├── 📄 2025-06-08_AES_ADA_Request_Financial_Hardship_Relief.pdf.bak
> │        ├── 📄 2025-12-16_AES_Emergency_Notice.md
> │        ├── 📄 AES_Data_Fields_Reference.md
> │        ├── 📄 index.md
> │      └── 📂 99__archive/
> │        ├── 📄 README_supporting.md
> │        ├── 📄 index.md
> │      ├── 📄 Raw_Exhibit_Map.md
> │      ├── 📄 index.md
> │    ├── 📄 Evidence_Log.md
> │    ├── 📄 index.md
> │  └── 📂 30_court_record/
> │    └── 📂 10_docket/
> │      ├── 📄 001_Complaint.pdf
> │      ├── 📄 002_Appearance.pdf
> │      ├── 📄 002_Appearance.pdf.bak
> │      ├── 📄 003_Request_for_Admissions.pdf
> │      ├── 📄 004_Notice_to_Homeowners.pdf
> │      ├── 📄 004_Notice_to_Homeowners.pdf.bak
> │      ├── 📄 005_Appearance_2.pdf
> │      ├── 📄 005_Appearance_2.pdf.bak
> │      ├── 📄 006_Summons_1.pdf
> │      ├── 📄 007_Summons_2.pdf
> │      ├── 📄 008_Summons_3.pdf
> │      ├── 📄 009_Summons_4.pdf
> │      ├── 📄 010_Summons_5.pdf
> │      ├── 📄 011_Service_Returned_03-05-2025.pdf
> │      ├── 📄 012_Service_Returned_04-15-2025.pdf
> │      ├── 📄 013_Motion_for_Default_Judgment.pdf
> │      ├── 📄 014_Affidavit.pdf
> │      ├── 📄 015_Affidavit_Attorney_Fees.pdf
> │      ├── 📄 016_Affidavit_Additional.pdf
> │      ├── 📄 017_Order_Denying_Default_Judgment.pdf
> │      ├── 📄 017_Order_Denying_Default_Judgment.pdf.bak
> │      ├── 📄 018_Omitted_Notice_of_Service.pdf
> │      ├── 📄 018_Omitted_Notice_of_Service.pdf.bak
> │      ├── 📄 019_Amended_Motion_Default_Judgment_1.pdf
> │      ├── 📄 019_Amended_Motion_Default_Judgment_1.pdf.bak
> │      ├── 📄 020_Amended_Motion_Default_Judgment_2.pdf
> │      ├── 📄 021_Praecipe_Sheriff_Sale_1.pdf
> │      ├── 📄 021_Praecipe_Sheriff_Sale_1.pdf.bak
> │      ├── 📄 022_Praecipe_Sheriff_Sale_2.pdf
> │      ├── 📄 023_Decree_Foreclosure_Returned.pdf
> │      ├── 📄 023_Decree_Foreclosure_Returned.pdf.bak
> │      ├── 📄 024_Petition_Writ_of_Assistance.pdf
> │      ├── 📄 024_Petition_Writ_of_Assistance.pdf.bak
> │      ├── 📄 025_Motion_Vacate_Stay_Writ.pdf
> │      ├── 📄 025_Motion_Vacate_Stay_Writ.pdf.bak
> │      ├── 📄 026_Exhibit_List_A-G.pdf
> │      ├── 📄 026_Exhibit_List_A-G.pdf.bak
> │      ├── 📄 027_Supplemental_Motion_Access.pdf
> │      ├── 📄 027_Supplemental_Motion_Access.pdf.bak
> │      ├── 📄 028_Report_Court_Defendant_Request.pdf
> │      ├── 📄 028_Report_Court_Defendant_Request.pdf.bak
> │      ├── 📄 029_Emergency_Supplemental_Declaration.pdf
> │      ├── 📄 029_Emergency_Supplemental_Declaration.pdf.bak
> │      ├── 📄 030_Report_Sheriff_Sale_No_Excess.pdf
> │      ├── 📄 031_Proposed_Order_Vacate.pdf
> │      ├── 📄 031_Proposed_Order_Vacate.pdf.bak
> │      ├── 📄 032_Proposed_Order_Stay.pdf
> │      ├── 📄 032_Proposed_Order_Stay.pdf.bak
> │      ├── 📄 _Case_Summary.md
> │      ├── 📄 index.md
> │  ├── 📄 README.md
> │  ├── 📄 _headers
> │  ├── 📄 _redirects
> │  └── 📂 assets/
> │    ├── 📄 README.md
> │  └── 📂 tools/
> │    ├── 📄 CANVAS_WORKFLOW_QUICKSTART.md
> │    ├── 📄 FORENSIC_AUDIT_EXECUTION_PLAN.md
> │    ├── 📄 FORENSIC_AUDIT_QUICKSTART.md
> │    ├── 📄 GIT_LFS_SETUP.md
> │    ├── 📄 MEDIA_OPTIMIZATION_SUMMARY.md
> │    ├── 📄 OBSIDIAN_CANVAS_SETUP.md
> │    ├── 📄 QUARTZ_MEDIA_CONFIG.md
> │    ├── 📄 TOOLS.md
> │    └── 📂 __pycache__/
> │      ├── 📄 canvas_updater.cpython-314.pyc
> │      ├── 📄 date_extractor.cpython-314.pyc
> │      ├── 📄 discovery.cpython-314.pyc
> │      ├── 📄 discrepancy_detector.cpython-314.pyc
> │      ├── 📄 forensic_audit_pipeline.cpython-314.pyc
> │      ├── 📄 index_updater.cpython-314.pyc
> │      ├── 📄 pdf_processor.cpython-314.pyc
> │      ├── 📄 timeline_builder.cpython-314.pyc
> │    ├── 📄 add_frontmatter.py
> │    ├── 📄 add_tags_to_markdown.py
> │    ├── 📄 canvas_to_markdown.py
> │    ├── 📄 canvas_updater.py
> │    ├── 📄 case_brain_full_pipeline.py
> │    ├── 📄 check_orphans_and_create_indexes.py
> │    ├── 📄 compress_pdfs.py
> │    ├── 📄 compress_pdfs_inplace.py
> │    ├── 📄 convert_all_txt_to_md.py
> │    ├── 📄 convert_heic_to_jpeg.py
> │    ├── 📄 date_extractor.py
> │    ├── 📄 discovery.py
> │    ├── 📄 discrepancy_detector.py
> │    ├── 📄 forensic_audit_pipeline.py
> │    ├── 📄 index.md
> │    ├── 📄 index_updater.py
> │    ├── 📄 link_timeline_events.py
> │    ├── 📄 move_opposing_filings.py
> │    ├── 📄 optimize_images.py
> │    ├── 📄 optimize_pdfs_pikepdf.py
> │    ├── 📄 pdf_processor.py
> │    ├── 📄 rename_evidence_files.ps1
> │    ├── 📄 requirements_forensic_audit.txt
> │    ├── 📄 timeline_builder.py
> │    ├── 📄 update_brain.ps1
> │    ├── 📄 viewer.html
> │  ├── 📄 wrangler.toml
> └── 📄 index.md
> ```

### Assistant
> Got it. This tree is *already* strong (clear separation: **timeline** vs **filings** vs **evidence vault**). The problems you’re going to hit are not “structure” problems—they’re **scale, duplication, naming drift, and index rot**. Here’s what I would fix, tighten, and standardize so it stays court-ready under stress.
> 
> ---
> 
> ## 1) Fix the biggest risk: duplicates + naming drift
> 
> ### What I see
> You have repeated files with slightly different names for the same event, e.g.:
> - `2025-01-09_order_Court_Orders_And_Hearing_Scheduled.md`
> - `2025-01-09_order_Order_Court_Orders_And_Hearing_Scheduled.md`
> - Multiple versions of “Motion to Vacate Void Judgment” on the same date.
> 
> ### Why it matters
> In litigation, duplicates become credibility landmines. Opposing counsel will exploit inconsistency (“which one is your real position?”). You want **one canonical file** plus a clean revision trail.
> 
> ### Standard
> - **One canonical document per event** in the timeline.
> - All alternates go into `/_archive/` or `/_versions/` with a suffix like `v2`, `v3`, etc.
> - Never keep two “final-ish” variants at the same level.
> 
> **Recommendation (naming rule):**
> `YYYY-MM-DD_{category}_{short_title}__vN.md` only when needed  
> Examples:
> - `2025-03-05_motion_to_vacate_void_judgment__v1.md`
> - `2025-03-05_motion_to_vacate_void_judgment__v2.md`
> 
> ---
> 
> ## 2) Separate “timeline narrative” from “court filing artifacts” harder
> 
> Right now, your timeline includes items like `motion_`, `court_filing_`, `document_`. That blurs the line.
> 
> ### Clean mental model
> - **Timeline** answers: *What happened? When? Who? What evidence exists?*
> - **Filings** answers: *What did we file? What exhibits were attached? Where’s the receipt?*
> 
> ### What to do
> In `00_admin/05_timeline/...`, keep timeline entries as “event logs” even if they link to filings.
> 
> In each timeline entry, include a small block like:
> 
> - **Related Filing(s):** `10_filings/10_2025-12-10_motion_vacate/...`
> - **Related Exhibits:** `20_evidence_vault/10_EXHIBIT_SETS/...`
> - **Related Video/Photo:** `20_evidence_vault/20_RAW/...`
> 
> That way timeline stays readable, and filings stay defensible.
> 
> ---
> 
> ## 3) Your evidence vault needs a “stable exhibit ID system”
> 
> You’re *close* with `EX-V-09-XX` etc. Keep going and make it ironclad.
> 
> ### Recommendation: two-layer naming
> 1) **Stable ID** (never changes): `EX-V-09-059`
> 2) **Human-readable metadata** (optional, can change): `__bedroom_cam_1046.mp4`
> 
> So files become:
> - `EX-V-09-059__bedroom_cam_2025-12-09_1046.mp4`
> - `EX-P-09-112__removal_day_photo_012.jpg`
> 
> Why: filenames should remain sortable and citeable in pleadings.
> 
> ---
> 
> ## 4) Create a single “Master Index” that drives everything
> 
> You already have:
> - `Case_Master_Index.md`
> - `Evidence_Master_Index.md`
> - `Filings_Master_Index.md`
> - `Timeline_Master.md`
> 
> Good. Now make them **authoritative** and automate/discipline around them.
> 
> ### Minimum required sections per Master Index
> 
> **Filings_Master_Index.md**
> - Filing date
> - Title
> - Odyssey envelope number (if applicable)
> - What relief requested
> - Status (pending/denied/granted/hearing set)
> - Links: PDF + source MD/DOCX + receipt
> 
> **Evidence_Master_Index.md**
> - Exhibit ID
> - Type (video/photo/pdf/screenshot)
> - Date/time captured
> - Source system (camera, phone, Odyssey, USPS, etc.)
> - Short description
> - Where referenced (which motion / declaration / paragraph)
> 
> **Timeline_Master.md**
> - One row per event (date/time)
> - Event title
> - Category (service, filing, execution, harm, ADA, utilities)
> - Links to the timeline entry + linked evidence
> 
> If you keep these three current, you can generate hearing packets fast.
> 
> ---
> 
> ## 5) Consolidate the “overviews” section into “Attorney-ready packets”
> 
> `10_overviews/` has mixed media (`.m4a`, `.pdf`, `.md`, `.canvas`). That’s fine internally, but for operational clarity:
> 
> ### Suggested sub-structure
> - `10_overviews/10_case_brief/`
> - `10_overviews/20_procedural_posture/`
> - `10_overviews/30_key_exhibits/`
> - `10_overviews/40_hearing_packets/`
> - `10_overviews/50_outreach/`
> 
> Each folder has an `index.md` that says:
> - purpose
> - last updated
> - what to send to an attorney/court vs what is internal
> 
> ---
> 
> ## 6) Clean up the filings folders: add “source” and “final” conventions
> 
> Your filing folders are good (`01_drafts`, `02_exhibits`, `03_proposed_order`, `04_filed_receipts`). Two tweaks:
> 
> ### Add:
> - `00_source/` → the editable originals (docx/md)
> - `99_final/` → the final PDFs exactly as filed (no `.bak` clutter)
> 
> Keep `.bak` out of the repo if possible (or shove into `_trash/` / `.gitignore`).
> 
> ---
> 
> ## 7) The *one* thing you’re missing: a “freeze” mechanism
> 
> When something is filed or used as an exhibit, it should become **immutable**.
> 
> ### Implement this rule
> - Anything in:
>   - `10_filings/**/99_final/`
>   - `20_evidence_vault/10_EXHIBIT_SETS/**`
>   becomes **read-only by policy** (even if not technically locked).
> 
> If you need a correction, you create a new version and reference it explicitly.
> 
> ---
> 
> ## 8) Quick triage: what I’d do next (highest ROI)
> 
> 1) **Deduplicate same-day duplicates** in `30_2025/` (keep 1 canonical file per event).
> 2) Enforce the naming convention on motions (`motion_...__vN`), move extras to `_versions/`.
> 3) Standardize evidence IDs for the massive camera dumps (`EX-V-09-###` already started—finish it).
> 4) Bring the three Master Indexes up to date and treat them as “truth.”
> 
> ---
> 
> If you tell me what your immediate goal is—**court hearing packet**, **attorney intake**, **public complaint package**, or **internal recordkeeping**—I’ll give you an exact “do this, then this” checklist and a rename/move map that won’t break links.

### User
> to get a documentation site published somehow but my connection is really slow and i cant push to github.

### Assistant
> You’ve got two separate problems:
> 
> 1) **You need a docs site “published”**  
> 2) **You currently can’t push to GitHub because your upload is too slow/unreliable**
> 
> So you need a publishing path that **doesn’t depend on big git pushes**.
> 
> Below are the practical options, ordered from “fastest path” to “most robust.”
> 
> ---
> 
> ## Option A (fastest): Publish with Cloudflare Pages via “Direct Upload” (no git push)
> If your goal is simply “get something live,” Cloudflare Pages can host a static site from an uploaded build output.
> 
> **How:**
> 1. On your local machine, build your docs site into a static folder:
>    - Quartz: typically outputs to something like `public/` (depends on your setup).
>    - Other static sites: often `dist/` or `build/`.
> 2. Zip that output folder (`public/` or `dist/`).
> 3. Upload it to Cloudflare Pages using direct upload (UI).
> 
> **Pros**
> - No GitHub push required.
> - Works even with a flaky connection (one upload vs many tiny git objects).
> - You get a public URL quickly.
> 
> **Cons**
> - Each update requires another upload (manual deploy).
> - If the output folder is big (images/videos), upload may still be painful.
> 
> **If your docs output is huge:** don’t upload the whole evidence vault. Host media separately (see Option D) and keep the docs site lightweight.
> 
> ---
> 
> ## Option B (low bandwidth, repeatable): “Sneakernet” the repo to a second connection, then push
> If you have **any** place with decent internet (friend’s Wi-Fi, library, hotspot at a better location):
> 
> **How:**
> 1. Copy your repo folder (or a bare clone) to a USB drive.
> 2. Go somewhere with good upload.
> 3. Push from there.
> 
> **Pros**
> - You keep the standard GitHub → Pages pipeline.
> - One-time pain, then normal flow.
> 
> **Cons**
> - Requires physically moving.
> 
> This is honestly the most reliable way if you’re blocked for days.
> 
> ---
> 
> ## Option C (surprisingly effective): Push “thin” updates only (stop committing heavy files)
> Right now your tree suggests you have **lots of heavy binary assets** (MP4, PDFs, etc.). If those are in the repo, GitHub pushes will be brutal on slow upload.
> 
> **Fix:**
> - Keep the docs site repo **text-first**:
>   - `.md` files and a few small images only.
> - Move heavy files (videos, large PDFs) out of the docs repo.
> 
> If you do this, your pushes become tiny and feasible even on slow connections.
> 
> **What to move out of Git:**
> - `content/.../20_evidence_vault/20_RAW/.../*.mp4`
> - large combined PDFs
> - anything > ~10–25 MB per file (on your connection, even that may be too big)
> 
> **How to keep links working:**
> - Replace those heavy files with **link stubs** in Markdown that point to where the file actually lives (see Option D).
> 
> ---
> 
> ## Option D (best structure for your case): Host evidence media separately, keep docs as an index
> Given your folder structure, your evidence vault is enormous. A docs site should not be trying to serve hundreds/thousands of MP4s from GitHub anyway.
> 
> **Split the system:**
> - **Docs site repo (GitHub/Pages/Cloudflare Pages):**  
>   Only Markdown + indexes + thumbnails + short supporting PDFs if needed.
> - **Evidence storage (one of these):**
>   - Cloudflare R2 (good if you’re already Cloudflare-first)
>   - Google Drive / Dropbox (quickest)
>   - Backblaze B2, etc.
> 
> Then in your docs pages, link to the evidence objects.
> 
> **Pros**
> - Your docs site becomes publishable on bad internet.
> - Your evidence remains accessible without destroying your repo history.
> 
> **Cons**
> - Takes a bit of setup.
> 
> ---
> 
> ## Option E (if you need a site TODAY and can’t upload big builds): Use a “single-file docs” landing page
> If even uploading a build zip is too much, publish a *minimal* site first:
> - One HTML page (or a tiny Markdown site) with:
>   - Case overview
>   - Timeline links
>   - Index links
>   - “Evidence request” instructions
> - Then expand later.
> 
> This is a tactical “get something live” move.
> 
> ---
> 
> # What I recommend for you (based on your tree)
> Your tree screams **“separate the evidence vault from the docs repo.”**  
> Trying to publish *that* whole structure as a docs site from GitHub is a time-waster on a normal connection, and basically impossible on a slow one.
> 
> **Do this:**
> 1) Publish the docs site with **only**:
> - `00_admin/00_trackers/`
> - `10_overviews/`
> - `20_strategy/`
> - `10_filings/` (lightweight PDFs okay, but not giant bundles)
> - timeline markdown
> - master indexes
> 
> 2) Move:
> - `20_evidence_vault/20_RAW/**` (especially MP4s)
> to R2 or Drive.
> 
> 3) Add link stubs inside your Markdown:
> - “Exhibit V-09-59 (video)” → link to the hosted object.
> 
> ---
> 
> # Immediate next step (no questions, just a clean action)
> Pick **one** of these “publish paths” right now:
> 
> - **If you can upload one zip:** do **Option A** (Cloudflare Pages direct upload) from your built `public/` or `dist/`.
> - **If uploads are failing everywhere:** do **Option B** (USB to better internet) and push once.
> - **If you want this to be sustainable:** start **Option D** split today, even if it’s basic.
> 
> If you tell me what you’re using to generate the docs site (**Quartz / Docusaurus / MkDocs / Astro / something else**) and what hosting target you want (**GitHub Pages vs Cloudflare Pages**), I’ll give you the exact commands and the leanest file list to ship first (so you’re not trying to push 2,000 MP4s through a straw).

### User
> 1/12/2025 zai

### Assistant
> I’m going to interpret **“1/12/2025 zai”** as a request to **turn that shorthand into a proper timeline entry**. If that’s wrong, say so and I’ll adjust—fast.
> 
> Here is a **Quartz / Obsidian–clean timeline entry** you can drop in immediately.
> 
> ---
> 
> ### `2025-01-12_event_zai.md`
> 
> ```md
> ---
> title: Zai — Case-Related Event
> date: 2025-01-12
> category: timeline
> tags:
>   - zai
>   - witness
>   - case-event
> ---
> 
> ## Event Summary
> Interaction involving **Zai** relevant to the FCFCU case.
> 
> ## Details
> - **Date:** January 12, 2025
> - **Person:** Zai
> - **Type:** Case-related interaction / occurrence
> - **Location:** _[add if applicable]_
> 
> ## What Happened
> Brief factual description of what occurred.  
> (Stick to observable facts. No interpretation here.)
> 
> ## Why It Matters
> Explain relevance to the case:
> - Credibility
> - Timeline continuity
> - Evidence linkage
> - Pattern establishment
> 
> ## Related Evidence
> - _[Link to evidence if any]_  
>   Example: `[[20_evidence_vault/EX-XX-XXX|Exhibit ID]]`
> 
> ## Related Filings
> - _[Link if referenced in a motion or declaration]_
> 
> ## Notes
> - Any follow-up needed
> - Any corroboration required
> ```
> 
> ---
> 
> ### Where this should live
> Based on your structure:
> 
> ```
> 00_admin/05_timeline/30_2025/
> └── 2025-01-12_event_zai.md
> ```
> 
> ---
> 
> ### Blunt guidance (important)
> - Keep this **event-focused**, not emotional.
> - If Zai is a **witness or participant**, consistency across timeline entries matters.
> - If this connects to **multiple dates**, reference them—don’t duplicate the story.
> 
> If you want, next I can:
> - Convert this into a **sworn-declaration-ready paragraph**
> - Link it properly into your **Timeline_Master.md**
> - Normalize all “Zai” references across the repo so nothing drifts
> 
> Just tell me which.
