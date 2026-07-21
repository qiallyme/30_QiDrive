---
layout: page
title: "Video File Organization"
slug: "video_file_organization"
created_at: "2025-12-30 02:51:48"
updated_at: "2026-07-18T11:03:13-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-003.json"
template_key: master-template
date: 2025-12-30
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6953924c-9250-8333-88c3-a7c01e2a5fcd"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Video File Organization

## Overview
- **Date**: 2025-12-30 02:51:48
- **Conversation ID**: `6953924c-9250-8333-88c3-a7c01e2a5fcd`
- **Source**: `Chat-Export-28513-2026/conversations-003.json`

## Chat History

### User
> so some how i have .mp4 and .media and .avi and all kinds of video files scattered between places on my c drive and places on my google drive and places on my usb drive, and some are in .folders and some in _folders and i wnt to see where i can find the folder that contain thse video files while ignoring video files from programs that arent even videos they are something but not videos but pop up when i search for videos making the search difficult.

### Assistant
> You’re not crazy — Windows search **will absolutely lie to you** here. It treats anything with a video-ish extension as a “video,” including junk created by apps, caches, temp blobs, and program assets. We’re going to fix this **systematically**, not by clicking around like a raccoon.
> 
> Below is a **clean, deterministic approach** that does exactly what you asked:
> 
> ---
> 
> ## Goal (translated into technical terms)
> 
> You want to:
> 
> 1. **Find folders that contain real video files**  
> 2. Across:
>    - `C:\`
>    - Google Drive (local sync folder)
>    - USB drive(s)
> 3. **Ignore program assets, caches, and fake videos**
> 4. Get a **clear list of folders**, not a mess of individual files
> 
> Windows Explorer alone is **not sufficient** for this. PowerShell is the correct tool.
> 
> ---
> 
> ## Step 1 — Define what counts as a “real” video (this matters)
> 
> We will include **only human-generated formats**, and exclude program junk.
> 
> ### Included extensions (adjust if needed):
> ```text
> .mp4 .mov .avi .mkv .wmv .m4v .mpeg .mpg
> ```
> 
> ### Explicitly excluded locations (critical):
> - `Program Files`
> - `Program Files (x86)`
> - `Windows`
> - `AppData`
> - `.cache`
> - `.npm`
> - `.electron`
> - `.vscode`
> - `.git`
> - Any folder starting with `.`
> 
> ---
> 
> ## Step 2 — Use this PowerShell command (copy/paste safe)
> 
> This **finds folders that contain video files**, filters out garbage, and groups results by folder.
> 
> ### 🔹 Run PowerShell **as yourself** (not admin unless drives require it)
> 
> ```powershell
> $videoExt = '*.mp4','*.mov','*.avi','*.mkv','*.wmv','*.m4v','*.mpeg','*.mpg'
> 
> $excludePaths = @(
>   '\Windows\',
>   '\Program Files\',
>   '\Program Files (x86)\',
>   '\AppData\',
>   '\.git\',
>   '\.cache\',
>   '\node_modules\'
> )
> 
> $roots = @(
>   'C:\',
>   'D:\',              # USB – change if needed
>   'E:\',              # USB – change if needed
>   "$env:USERPROFILE\Google Drive"
> )
> 
> Get-ChildItem -Path $roots -Recurse -File -Include $videoExt -ErrorAction SilentlyContinue |
> Where-Object {
>   $path = $_.FullName
>   -not ($excludePaths | Where-Object { $path -like "*$_*" })
> } |
> Group-Object DirectoryName |
> Sort-Object Count -Descending |
> Select-Object Count, Name
> ```
> 
> ---
> 
> ## What this gives you (this is the important part)
> 
> You’ll get output like:
> 
> ```text
> Count Name
> ----- ----
>   128 C:\Users\Cody\Videos\Court_Evidence
>    42  D:\Camera_Archive\2023
>    17  C:\Users\Cody\Desktop\Temp_Recordings
> ```
> 
> This answers **exactly**:
> - Where your videos actually live
> - Which folders matter most
> - Without showing program garbage
> 
> ---
> 
> ## Step 3 — If you want ONLY your stuff (extra clean)
> 
> Add this filter **inside** the `Where-Object` block:
> 
> ```powershell
> -and $_.Length -gt 5MB
> ```
> 
> That removes thumbnails, stubs, and fake media.
> 
> ---
> 
> ## Step 4 — Optional: Export to a file (recommended)
> 
> ```powershell
> ... | Export-Csv "$env:USERPROFILE\Desktop\video_folders.csv" -NoTypeInformation
> ```
> 
> Now you can:
> - Sort
> - Annotate
> - Decide what to consolidate
> - Build a cleanup plan without touching files yet
> 
> ---
> 
> ## Why this works (truth mode)
> 
> - Windows Search indexes **metadata**, not intent
> - Program assets use real video extensions
> - Explorer cannot filter by *context*
> - PowerShell can
> 
> This is the **only sane way** to do this at scale.
> 
> ---
> 
> ## Next logical steps (don’t do all at once)
> 
> Tell me which you want next:
> 1. **Move videos into a unified structure (dry run first)**
> 2. **Detect duplicates across drives**
> 3. **Separate “evidence / important” vs casual video**
> 4. **Rename folders consistently (_ vs . vs clean)**
> 5. **Build a permanent “Video Index” script**
> 
> Pick one. We’ll do it cleanly, without breaking anything.

### User
> no we dont want to exclude all folders because soem of those vidoea re being .(dot) folders.

### Assistant
> Understood. My earlier “exclude dot folders” rule was too blunt for your reality. We’ll stop excluding by folder-name pattern and instead exclude by **known garbage locations** + (optionally) **minimum file size**. That keeps your legit `.` folders in play.
> 
> Here’s the corrected approach.
> 
> ---
> 
> ## Option A (recommended): Keep dot folders, exclude only known system/app junk
> 
> Copy/paste:
> 
> ```powershell
> $videoExt = '*.mp4','*.mov','*.avi','*.mkv','*.wmv','*.m4v','*.mpeg','*.mpg','*.media'
> 
> # Exclude by known high-noise roots (NOT by dot-folder naming)
> $excludeRegex = @(
>   '\\Windows\\',
>   '\\Program Files\\',
>   '\\Program Files \(x86\)\\',
>   '\\ProgramData\\',
>   '\\AppData\\',
>   '\\Recovery\\',
>   '\\System Volume Information\\'
> ) -join '|'
> 
> # Add/adjust roots (include your Drive sync path + USB letters)
> $roots = @(
>   'C:\',
>   "$env:USERPROFILE\Google Drive",
>   'D:\',
>   'E:\'
> )
> 
> Get-ChildItem -Path $roots -Recurse -File -Include $videoExt -ErrorAction SilentlyContinue |
> Where-Object {
>   $_.FullName -notmatch $excludeRegex
> } |
> Group-Object DirectoryName |
> Sort-Object Count -Descending |
> Select-Object Count, Name
> ```
> 
> What this does:
> - **Includes** dot-folders (e.g., `.foo\bar\video.mp4`)
> - **Excludes** the usual offenders (Windows, Program Files, AppData, etc.)
> - Outputs **folders ranked by how many videos they contain**
> 
> ---
> 
> ## Option B: Same, but also cut out tiny “fake” videos (high signal)
> 
> If your “not really videos” are typically tiny stubs/caches, add a size threshold:
> 
> ```powershell
> $minBytes = 5MB
> ...
> Where-Object {
>   $_.FullName -notmatch $excludeRegex -and $_.Length -ge $minBytes
> }
> ```
> 
> If you’re dealing with lots of short clips that are legitimately small, set it lower (e.g., `500KB` or `1MB`).
> 
> ---
> 
> ## Option C: Show top file types per folder (helps identify “junk-y” folders fast)
> 
> This helps you spot folders that are mostly “.media” or some weird extension:
> 
> ```powershell
> $videoExt = '*.mp4','*.mov','*.avi','*.mkv','*.wmv','*.m4v','*.mpeg','*.mpg','*.media'
> $excludeRegex = @(
>   '\\Windows\\','\\Program Files\\','\\Program Files \(x86\)\\','\\ProgramData\\','\\AppData\\'
> ) -join '|'
> $roots = @('C:\',"$env:USERPROFILE\Google Drive",'D:\','E:\')
> 
> $files =
> Get-ChildItem -Path $roots -Recurse -File -Include $videoExt -ErrorAction SilentlyContinue |
> Where-Object { $_.FullName -notmatch $excludeRegex }
> 
> $files |
> Group-Object DirectoryName |
> Sort-Object Count -Descending |
> Select-Object -First 50 |
> ForEach-Object {
>   $dir = $_.Name
>   $extSummary = ($files | Where-Object DirectoryName -eq $dir |
>     Group-Object Extension | Sort-Object Count -Descending |
>     Select-Object -First 5 |
>     ForEach-Object { "$($_.Name):$($_.Count)" }) -join '  '
>   [PSCustomObject]@{ Count=$_.Count; Folder=$dir; TopExtensions=$extSummary }
> } |
> Format-Table -AutoSize
> ```
> 
> ---
> 
> ## Quick reality check question (no fluff, this changes the script)
> 
> When you say “Google Drive,” do you mean:
> - **Google Drive for Desktop** (files visible under something like `C:\Users\You\Google Drive\`), OR
> - the **web Drive** (not locally synced unless you download)?
> 
> If it’s the web-only stuff, PowerShell cannot search it directly; we’d need to search the **synced** folder or use Drive export/backup.
> 
> If you don’t want to answer, fine: run Option A and tell me what root paths actually exist on your machine for Drive + USB letters, and I’ll tighten it further without excluding your dot folders.

### User
> yes, i would like the script to be a python script cause ps be pissing me off, and the list it exports should be folder links so i can click it and file explorer takes me to the location.

### Assistant
> Good. PowerShell can stay mad. Here’s a **Python script** that:
> 
> - Scans **C:\**, your **Google Drive for Desktop** local folder(s), and any **USB drive letters you list**
> - Finds files with real video-ish extensions (`.mp4, .avi, .mov, .mkv, .wmv, .m4v, .mpeg, .mpg, .media`)
> - **Does NOT exclude dot-folders**
> - Excludes the usual junk roots (**Windows / Program Files / ProgramData / AppData / System Volume Info / $Recycle.Bin**)
> - Groups by **folder**
> - Exports:
>   - **HTML report** with **clickable folder links** (`file:///...`) that open in File Explorer
>   - **CSV** for sorting/filtering
> 
> ## Python script: `video_folder_index.py`
> 
> ```python
> import os
> import sys
> import csv
> import html
> import urllib.parse
> from collections import defaultdict
> from datetime import datetime
> 
> # -----------------------------
> # CONFIG (edit these if needed)
> # -----------------------------
> 
> VIDEO_EXTS = {
>     ".mp4", ".mov", ".avi", ".mkv", ".wmv", ".m4v", ".mpeg", ".mpg", ".media"
> }
> 
> # Minimum size filter (bytes). Set to 0 to disable.
> # Useful to ignore tiny cache stubs that "look like" videos.
> MIN_BYTES = 0  # e.g. 5 * 1024 * 1024 for 5MB
> 
> # Exclude by path *segments* (case-insensitive). This does NOT exclude dot folders.
> EXCLUDE_SEGMENTS = {
>     r"\windows\\",
>     r"\program files\\",
>     r"\program files (x86)\\",
>     r"\programdata\\",
>     r"\appdata\\",
>     r"\system volume information\\",
>     r"\$recycle.bin\\",
>     r"\recovery\\",
> }
> 
> # Roots to scan. Adjust/add drive letters and folders.
> # Google Drive for Desktop commonly lives at one of these:
> DEFAULT_ROOTS = [
>     r"C:\",
>     os.path.join(os.environ.get("USERPROFILE", r"C:\Users\Default"), "Google Drive"),
>     os.path.join(os.environ.get("USERPROFILE", r"C:\Users\Default"), "My Drive"),
>     os.path.join(os.environ.get("USERPROFILE", r"C:\Users\Default"), "GoogleDrive"),
>     # Add USB drives here (examples):
>     r"D:\",
>     r"E:\",
> ]
> 
> # -----------------------------
> # HELPERS
> # -----------------------------
> 
> def is_excluded_path(path_lower: str) -> bool:
>     # Normalize to ensure trailing slash checks match reliably
>     p = path_lower.replace("/", "\\")
>     if not p.endswith("\\"):
>         p = p + "\\"
>     return any(seg in p for seg in EXCLUDE_SEGMENTS)
> 
> def file_url_from_path(folder_path: str) -> str:
>     # Convert Windows path to file:/// URL
>     # Example: C:\Users\Cody\Videos -> file:///C:/Users/Cody/Videos
>     p = folder_path.replace("\\", "/")
>     # Ensure drive letter form becomes /C:/...
>     if len(p) >= 2 and p[1] == ":":
>         p = "/" + p
>     return "file://" + urllib.parse.quote(p)
> 
> def safe_walk(root: str):
>     # os.walk with error handling and speed improvements
>     for dirpath, dirnames, filenames in os.walk(root, topdown=True):
>         dp_lower = dirpath.lower()
> 
>         # If current directory is excluded, skip it and its children
>         if is_excluded_path(dp_lower):
>             dirnames[:] = []
>             continue
> 
>         # Prune children that are excluded by path segment
>         # (We don't exclude dot-folders here; only the segment list above.)
>         kept = []
>         for d in dirnames:
>             child = os.path.join(dirpath, d).lower()
>             if not is_excluded_path(child):
>                 kept.append(d)
>         dirnames[:] = kept
> 
>         yield dirpath, filenames
> 
> def discover_existing_roots(roots):
>     existing = []
>     for r in roots:
>         if r and os.path.exists(r):
>             existing.append(r)
>     # De-dupe while preserving order
>     seen = set()
>     uniq = []
>     for r in existing:
>         key = os.path.normcase(os.path.abspath(r))
>         if key not in seen:
>             seen.add(key)
>             uniq.append(r)
>     return uniq
> 
> # -----------------------------
> # MAIN
> # -----------------------------
> 
> def main():
>     roots = discover_existing_roots(DEFAULT_ROOTS)
> 
>     if not roots:
>         print("No valid roots found. Edit DEFAULT_ROOTS in the script.")
>         sys.exit(1)
> 
>     print("Scanning roots:")
>     for r in roots:
>         print(" -", r)
> 
>     folder_counts = defaultdict(int)
>     folder_sizes = defaultdict(int)   # total bytes of matching videos
>     folder_exts = defaultdict(lambda: defaultdict(int))  # ext -> count
> 
>     total_files = 0
>     matched_files = 0
> 
>     for root in roots:
>         for dirpath, filenames in safe_walk(root):
>             for name in filenames:
>                 total_files += 1
>                 ext = os.path.splitext(name)[1].lower()
>                 if ext not in VIDEO_EXTS:
>                     continue
> 
>                 fullpath = os.path.join(dirpath, name)
>                 try:
>                     size = os.path.getsize(fullpath)
>                 except OSError:
>                     continue
> 
>                 if MIN_BYTES and size < MIN_BYTES:
>                     continue
> 
>                 matched_files += 1
>                 folder_counts[dirpath] += 1
>                 folder_sizes[dirpath] += size
>                 folder_exts[dirpath][ext] += 1
> 
>     # Sort folders by count desc, then size desc
>     rows = sorted(
>         folder_counts.keys(),
>         key=lambda p: (folder_counts[p], folder_sizes[p]),
>         reverse=True
>     )
> 
>     ts = datetime.now().strftime("%Y%m%d_%H%M%S")
>     out_csv = f"video_folders_{ts}.csv"
>     out_html = f"video_folders_{ts}.html"
> 
>     # Write CSV
>     with open(out_csv, "w", newline="", encoding="utf-8") as f:
>         w = csv.writer(f)
>         w.writerow(["count", "total_bytes", "folder_path", "folder_link", "top_extensions"])
>         for folder in rows:
>             exts_sorted = sorted(folder_exts[folder].items(), key=lambda kv: kv[1], reverse=True)
>             top_exts = " ".join([f"{k}:{v}" for k, v in exts_sorted[:8]])
>             w.writerow([
>                 folder_counts[folder],
>                 folder_sizes[folder],
>                 folder,
>                 file_url_from_path(folder),
>                 top_exts
>             ])
> 
>     # Write HTML with clickable links
>     with open(out_html, "w", encoding="utf-8") as f:
>         f.write("<!doctype html><html><head><meta charset='utf-8'>")
>         f.write("<title>Video Folder Index</title>")
>         f.write("<style>")
>         f.write("body{font-family:Segoe UI,Arial,sans-serif;margin:24px}")
>         f.write("table{border-collapse:collapse;width:100%}")
>         f.write("th,td{border-bottom:1px solid #ddd;padding:8px;vertical-align:top}")
>         f.write("th{text-align:left;position:sticky;top:0;background:#f6f6f6}")
>         f.write("tr:hover{background:#fafafa}")
>         f.write(".muted{color:#666;font-size:12px}")
>         f.write("</style></head><body>")
>         f.write("<h1>Video Folder Index</h1>")
>         f.write(f"<div class='muted'>Generated: {html.escape(datetime.now().isoformat(timespec='seconds'))}</div>")
>         f.write(f"<div class='muted'>Roots scanned: {html.escape(' | '.join(roots))}</div>")
>         f.write(f"<div class='muted'>Total files seen: {total_files:,} | Matching videos: {matched_files:,} | Unique folders: {len(rows):,}</div>")
>         if MIN_BYTES:
>             f.write(f"<div class='muted'>Minimum file size filter: {MIN_BYTES:,} bytes</div>")
>         f.write("<hr>")
>         f.write("<table><thead><tr>")
>         f.write("<th>Count</th><th>Total Size (MB)</th><th>Folder</th><th>Top Extensions</th>")
>         f.write("</tr></thead><tbody>")
> 
>         for folder in rows:
>             url = file_url_from_path(folder)
>             size_mb = folder_sizes[folder] / (1024 * 1024)
>             exts_sorted = sorted(folder_exts[folder].items(), key=lambda kv: kv[1], reverse=True)
>             top_exts = " ".join([f"{k}:{v}" for k, v in exts_sorted[:8]])
> 
>             f.write("<tr>")
>             f.write(f"<td>{folder_counts[folder]}</td>")
>             f.write(f"<td>{size_mb:.2f}</td>")
>             f.write("<td>")
>             f.write(f"<a href='{url}'>{html.escape(folder)}</a>")
>             f.write("</td>")
>             f.write(f"<td>{html.escape(top_exts)}</td>")
>             f.write("</tr>")
> 
>         f.write("</tbody></table></body></html>")
> 
>     print("\nDone.")
>     print("CSV :", os.path.abspath(out_csv))
>     print("HTML:", os.path.abspath(out_html))
>     print("\nOpen the HTML file in your browser; click a folder link to open it in File Explorer.")
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ---
> 
> ## How to run it (no drama)
> 
> 1. Put `video_folder_index.py` anywhere (e.g., `C:\temp\video_index\`)
> 2. Open CMD in that folder
> 3. Run:
> 
> ```bat
> python video_folder_index.py
> ```
> 
> It will generate:
> - `video_folders_YYYYMMDD_HHMMSS.html` (clickable links)
> - `video_folders_YYYYMMDD_HHMMSS.csv`
> 
> ---
> 
> ## Two quick knobs you’ll probably want
> 
> ### 1) Add your actual USB drive letters
> Edit `DEFAULT_ROOTS`:
> ```python
> r"F:\",
> r"G:\",
> ```
> 
> ### 2) Filter out tiny garbage “videos”
> Set:
> ```python
> MIN_BYTES = 5 * 1024 * 1024  # 5MB
> ```
> 
> If you have legit small clips, use `1MB` instead.
> 
> ---
> 
> ## One important note (truth mode)
> If your “Google Drive” videos are **not synced locally** (web-only), this script can’t see them. It only scans what exists on your machine. For Drive, this works if you’re using **Google Drive for Desktop** (local mirror/stream).
> 
> ---
> 
> If you paste back:
> - the top 10 rows from the HTML (counts + folder paths), and
> - one example of a “fake” video file that keeps showing up (full path + extension),
> 
> I’ll tune the exclude rules so it’s aggressive on junk **without** nuking your dot-folder evidence stash.

### User
> google drive is in a folder on my c drive but it may choke if it walks the path so the absolute path is C:\QiOS_WORKING\My Drive also update the code on lin e35 and 36 error says, "[" was not closed, and String literal is unterminated, then yes there aer really small videos that are video so update to 1mb and my usb drive is D: -- also can it prompt me if its global or if i want to filter with file name fuzzy logic, like names containg, T, or more than one T repeated 2 or more times, or has 646 int he name or 6 4 6 in the name

### Assistant
> You’re right on both counts:
> 
> 1) **`r"C:\"` will break** in Python because raw strings can’t end with a single backslash (that’s almost certainly your “`[` not closed / unterminated string literal” on those root lines).  
> 2) Google Drive root should be exactly: `C:\QiOS_WORKING\My Drive`.
> 
> Below is a corrected, hardened script that:
> 
> - Uses your roots:
>   - `C:\` (optional)
>   - `C:\QiOS_WORKING\My Drive`
>   - `D:\` (USB)
> - Sets **MIN_BYTES = 1MB** (keeps legit small clips)
> - Does **not** exclude dot-folders
> - Excludes only known junk paths (Windows/Program Files/etc.)
> - Prompts you:
>   - **Scan mode**: all roots vs pick which ones
>   - **Filename filters**: enable/disable
>   - Apply fuzzy rules:
>     - contains `"T"` (anywhere)
>     - contains **two or more T’s in a row** (e.g., `TT`, `TTT`)
>     - contains `646` OR `6 4 6` (digits separated by anything)
> 
> And exports:
> - **HTML with clickable `file:///` folder links**
> - **CSV** with same
> 
> ---
> 
> ## `video_folder_index.py` (drop-in)
> 
> ```python
> import os
> import sys
> import csv
> import html
> import re
> import urllib.parse
> from collections import defaultdict
> from datetime import datetime
> 
> # -----------------------------
> # CONFIG
> # -----------------------------
> 
> VIDEO_EXTS = {
>     ".mp4", ".mov", ".avi", ".mkv", ".wmv", ".m4v", ".mpeg", ".mpg", ".media"
> }
> 
> # Keep legit small videos: 1MB minimum
> MIN_BYTES = 1 * 1024 * 1024  # 1MB
> 
> # Exclude by path segments (case-insensitive). Does NOT exclude dot-folders.
> EXCLUDE_SEGMENTS = {
>     r"\windows\\",
>     r"\program files\\",
>     r"\program files (x86)\\",
>     r"\programdata\\",
>     r"\appdata\\",
>     r"\system volume information\\",
>     r"\$recycle.bin\\",
>     r"\recovery\\",
> }
> 
> # IMPORTANT: no raw strings ending with a single backslash
> DEFAULT_ROOTS = [
>     "C:\\",                       # optional; script will ask if you want "global"
>     r"C:\QiOS_WORKING\My Drive",  # your Google Drive local folder
>     "D:\\",                       # your USB drive
> ]
> 
> # -----------------------------
> # HELPERS
> # -----------------------------
> 
> def norm_path_lower(p: str) -> str:
>     p = p.replace("/", "\\").lower()
>     if not p.endswith("\\"):
>         p += "\\"
>     return p
> 
> def is_excluded_path(path_lower: str) -> bool:
>     p = norm_path_lower(path_lower)
>     return any(seg in p for seg in EXCLUDE_SEGMENTS)
> 
> def file_url_from_path(folder_path: str) -> str:
>     # Windows path -> file:///C:/...
>     p = folder_path.replace("\\", "/")
>     if len(p) >= 2 and p[1] == ":":
>         p = "/" + p
>     return "file://" + urllib.parse.quote(p)
> 
> def safe_walk(root: str):
>     for dirpath, dirnames, filenames in os.walk(root, topdown=True):
>         dp_lower = dirpath.lower()
> 
>         # Skip excluded directories entirely
>         if is_excluded_path(dp_lower):
>             dirnames[:] = []
>             continue
> 
>         # Prune excluded children
>         kept = []
>         for d in dirnames:
>             child = os.path.join(dirpath, d).lower()
>             if not is_excluded_path(child):
>                 kept.append(d)
>         dirnames[:] = kept
> 
>         yield dirpath, filenames
> 
> def discover_existing_roots(roots):
>     existing = []
>     for r in roots:
>         if r and os.path.exists(r):
>             existing.append(r)
> 
>     # de-dupe while preserving order
>     seen = set()
>     uniq = []
>     for r in existing:
>         key = os.path.normcase(os.path.abspath(r))
>         if key not in seen:
>             seen.add(key)
>             uniq.append(r)
>     return uniq
> 
> def prompt_yes_no(msg: str, default_yes: bool = True) -> bool:
>     default = "Y/n" if default_yes else "y/N"
>     while True:
>         ans = input(f"{msg} ({default}): ").strip().lower()
>         if not ans:
>             return default_yes
>         if ans in ("y", "yes"):
>             return True
>         if ans in ("n", "no"):
>             return False
>         print("Please answer y or n.")
> 
> def choose_roots(roots):
>     print("\nAvailable roots:")
>     for i, r in enumerate(roots, start=1):
>         print(f"  {i}) {r}")
> 
>     print("\nEnter comma-separated numbers to scan (example: 2,3). Press Enter for ALL.")
>     ans = input("Selection: ").strip()
>     if not ans:
>         return roots
> 
>     idxs = []
>     for part in ans.split(","):
>         part = part.strip()
>         if not part:
>             continue
>         if not part.isdigit():
>             continue
>         idx = int(part)
>         if 1 <= idx <= len(roots):
>             idxs.append(idx - 1)
> 
>     selected = [roots[i] for i in sorted(set(idxs))]
>     return selected if selected else roots
> 
> def build_name_filter():
>     """
>     Prompts user for optional fuzzy filename filters.
>     Returns a function(name:str)->bool
>     """
>     use_filters = prompt_yes_no("Do you want to enable filename fuzzy filters?", default_yes=False)
>     if not use_filters:
>         return lambda _name: True
> 
>     print("\nFilename fuzzy filters available:")
>     print("  1) Contains 'T' anywhere")
>     print("  2) Contains 'TT' (two or more T's in a row)")
>     print("  3) Contains 646 OR '6 4 6' (digits separated by anything)")
>     print("  4) Custom 'contains' terms (you type them)")
> 
>     use_contains_T = prompt_yes_no("Filter: require 'T' anywhere in filename?", default_yes=False)
>     use_T_repeat = prompt_yes_no("Filter: require 'TT' (T repeated 2+ times) in filename?", default_yes=False)
>     use_646 = prompt_yes_no("Filter: require 646 / 6 4 6 pattern in filename?", default_yes=False)
> 
>     custom_terms = []
>     if prompt_yes_no("Add custom 'contains' terms?", default_yes=False):
>         raw = input("Enter terms separated by commas (example: court, hallway, cam2): ").strip()
>         custom_terms = [t.strip() for t in raw.split(",") if t.strip()]
> 
>     # Compile regexes once
>     re_T_repeat = re.compile(r"T{2,}", re.IGNORECASE)
>     re_646 = re.compile(r"6\D*4\D*6")
> 
>     def matches(name: str) -> bool:
>         base = os.path.basename(name)
> 
>         if use_contains_T and ("t" not in base.lower()):
>             return False
> 
>         if use_T_repeat and not re_T_repeat.search(base):
>             return False
> 
>         if use_646 and not re_646.search(base):
>             return False
> 
>         if custom_terms:
>             b = base.lower()
>             # require any custom term? or all? default to ANY for sanity
>             if not any(term.lower() in b for term in custom_terms):
>                 return False
> 
>         return True
> 
>     return matches
> 
> # -----------------------------
> # MAIN
> # -----------------------------
> 
> def main():
>     roots_all = discover_existing_roots(DEFAULT_ROOTS)
>     if not roots_all:
>         print("No valid roots found. Edit DEFAULT_ROOTS in the script.")
>         sys.exit(1)
> 
>     # "Global" vs selective
>     # Interpret "global" as scanning ALL available roots (including C:\)
>     scan_global = prompt_yes_no("Scan GLOBAL (all roots listed)?", default_yes=True)
>     roots = roots_all if scan_global else choose_roots(roots_all)
> 
>     name_filter = build_name_filter()
> 
>     print("\nScanning roots:")
>     for r in roots:
>         print(" -", r)
>     print(f"Extensions: {', '.join(sorted(VIDEO_EXTS))}")
>     print(f"Minimum size: {MIN_BYTES:,} bytes ({MIN_BYTES / (1024*1024):.1f} MB)\n")
> 
>     folder_counts = defaultdict(int)
>     folder_sizes = defaultdict(int)
>     folder_exts = defaultdict(lambda: defaultdict(int))
> 
>     total_files = 0
>     matched_files = 0
> 
>     for root in roots:
>         for dirpath, filenames in safe_walk(root):
>             for fname in filenames:
>                 total_files += 1
>                 ext = os.path.splitext(fname)[1].lower()
>                 if ext not in VIDEO_EXTS:
>                     continue
> 
>                 if not name_filter(fname):
>                     continue
> 
>                 fullpath = os.path.join(dirpath, fname)
>                 try:
>                     size = os.path.getsize(fullpath)
>                 except OSError:
>                     continue
> 
>                 if size < MIN_BYTES:
>                     continue
> 
>                 matched_files += 1
>                 folder_counts[dirpath] += 1
>                 folder_sizes[dirpath] += size
>                 folder_exts[dirpath][ext] += 1
> 
>     rows = sorted(
>         folder_counts.keys(),
>         key=lambda p: (folder_counts[p], folder_sizes[p]),
>         reverse=True
>     )
> 
>     ts = datetime.now().strftime("%Y%m%d_%H%M%S")
>     out_csv = f"video_folders_{ts}.csv"
>     out_html = f"video_folders_{ts}.html"
> 
>     # CSV
>     with open(out_csv, "w", newline="", encoding="utf-8") as f:
>         w = csv.writer(f)
>         w.writerow(["count", "total_bytes", "folder_path", "folder_link", "top_extensions"])
>         for folder in rows:
>             exts_sorted = sorted(folder_exts[folder].items(), key=lambda kv: kv[1], reverse=True)
>             top_exts = " ".join([f"{k}:{v}" for k, v in exts_sorted[:10]])
>             w.writerow([
>                 folder_counts[folder],
>                 folder_sizes[folder],
>                 folder,
>                 file_url_from_path(folder),
>                 top_exts
>             ])
> 
>     # HTML (clickable folder links)
>     with open(out_html, "w", encoding="utf-8") as f:
>         f.write("<!doctype html><html><head><meta charset='utf-8'>")
>         f.write("<title>Video Folder Index</title>")
>         f.write("<style>")
>         f.write("body{font-family:Segoe UI,Arial,sans-serif;margin:24px}")
>         f.write("table{border-collapse:collapse;width:100%}")
>         f.write("th,td{border-bottom:1px solid #ddd;padding:8px;vertical-align:top}")
>         f.write("th{text-align:left;position:sticky;top:0;background:#f6f6f6}")
>         f.write("tr:hover{background:#fafafa}")
>         f.write(".muted{color:#666;font-size:12px}")
>         f.write("</style></head><body>")
>         f.write("<h1>Video Folder Index</h1>")
>         f.write(f"<div class='muted'>Generated: {html.escape(datetime.now().isoformat(timespec='seconds'))}</div>")
>         f.write(f"<div class='muted'>Roots scanned: {html.escape(' | '.join(roots))}</div>")
>         f.write(f"<div class='muted'>Total files seen: {total_files:,} | Matching videos: {matched_files:,} | Unique folders: {len(rows):,}</div>")
>         f.write(f"<div class='muted'>Min size: {MIN_BYTES:,} bytes</div>")
>         f.write("<hr>")
>         f.write("<table><thead><tr>")
>         f.write("<th>Count</th><th>Total Size (MB)</th><th>Folder (click to open)</th><th>Top Extensions</th>")
>         f.write("</tr></thead><tbody>")
> 
>         for folder in rows:
>             url = file_url_from_path(folder)
>             size_mb = folder_sizes[folder] / (1024 * 1024)
>             exts_sorted = sorted(folder_exts[folder].items(), key=lambda kv: kv[1], reverse=True)
>             top_exts = " ".join([f"{k}:{v}" for k, v in exts_sorted[:10]])
> 
>             f.write("<tr>")
>             f.write(f"<td>{folder_counts[folder]}</td>")
>             f.write(f"<td>{size_mb:.2f}</td>")
>             f.write(f"<td><a href='{url}'>{html.escape(folder)}</a></td>")
>             f.write(f"<td>{html.escape(top_exts)}</td>")
>             f.write("</tr>")
> 
>         f.write("</tbody></table></body></html>")
> 
>     print("Done.\n")
>     print("CSV :", os.path.abspath(out_csv))
>     print("HTML:", os.path.abspath(out_html))
>     print("\nOpen the HTML file in your browser; click a folder link to open it in File Explorer.")
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ---
> 
> ## Notes (so you don’t get blindsided)
> 
> - **C:\ scan can be slow.** That’s why the script asks “GLOBAL?” up front. If you say **No**, pick only:
>   - `C:\QiOS_WORKING\My Drive`
>   - `D:\`
> - The **`646` / `6 4 6`** filter uses regex `6\D*4\D*6`, so it matches:
>   - `646`
>   - `6-4-6`
>   - `6 4 6`
>   - `6__4__6`
> - The **TT rule** matches any `TT`, `TTT`, etc (case-insensitive).
> 
> ---
> 
> ## If it still “chokes” on Drive
> That usually means permission errors or reparse points. This script already suppresses walk errors reasonably, but if Drive has weird placeholders, the next hardening step is to **skip symlinks/reparse points**. If you hit that, paste the first error line you see and I’ll add the specific guard.

### User
> oh and are the fuzzy logic OR statement or AND, becaue it should be OR. " "c:/QiOS_WORKING/My Drive/_working/VIDEO-FINDER/video_folder_index.py"

> Scan GLOBAL (all roots listed)? (Y/n): n

> 

> Available roots:

>   1) C:\

>   2) C:\QiOS_WORKING\My Drive

>   3) D:\

> 

> Enter comma-separated numbers to scan (example: 2,3). Press Enter for ALL.

> Selection: 3

> Do you want to enable filename fuzzy filters? (y/N): y

> 

> Filename fuzzy filters available:

>   1) Contains 'T' anywhere

>   2) Contains 'TT' (two or more T's in a row)

>   3) Contains 646 OR '6 4 6' (digits separated by anything)

>   4) Custom 'contains' terms (you type them)

> Filter: require 'T' anywhere in filename? (y/N): y

> Filter: require 'TT' (T repeated 2+ times) in filename? (y/N): y

> Filter: require 646 / 6 4 6 pattern in filename? (y/N): y

> Add custom 'contains' terms? (y/N): y

> Enter terms separated by commas (example: court, hallway, cam2): treve

> 

> Scanning roots:

>  - D:\

> Extensions: .avi, .m4v, .media, .mkv, .mov, .mp4, .mpeg, .mpg, .wmv

> Minimum size: 1,048,576 bytes (1.0 MB)

> 

> Traceback (most recent call last):

>   File "c:\QiOS_WORKING\My Drive\_working\VIDEO-FINDER\video_folder_index.py", line 305, in <module>

>     main()

>     ~~~~^^

>   File "c:\QiOS_WORKING\My Drive\_working\VIDEO-FINDER\video_folder_index.py", line 248, in main      

>     with open(out_csv, "w", newline="", encoding="utf-8") as f:

>          ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

> FileNotFoundError: [Errno 2] No such file or directory: 'video_folders_20251230_040158.csv'

> (.venv) PS C:\QiOS_WORKING>

### Assistant
> Good catch. You just surfaced **two real issues**:
> 
> 1) **Your fuzzy logic is currently AND, not OR**  
> 2) **The script tried to write output to a directory that doesn’t exist (cwd problem)**
> 
> Let’s fix both cleanly.
> 
> ---
> 
> ## 1️⃣ Fuzzy logic: it SHOULD be **OR** (you’re right)
> 
> ### What happened
> Right now, the filter logic says:
> 
> > filename must match **T**  
> > **AND** match **TT**  
> > **AND** match **646**  
> > **AND** match `treve`
> 
> That’s why it’s overly restrictive and not what you want.
> 
> ### What you want
> You want:
> 
> > **MATCH if ANY rule is true** (logical OR)
> 
> So:
> - has `T` **OR**
> - has `TT` **OR**
> - has `646` / `6 4 6` **OR**
> - has `treve`
> 
> ---
> 
> ## ✅ FIX: Replace the filename filter logic (OR-based)
> 
> ### 🔧 Replace the `matches()` function **entirely** with this
> 
> ```python
> def matches(name: str) -> bool:
>     base = os.path.basename(name)
>     b = base.lower()
> 
>     rules = []
> 
>     if use_contains_T:
>         rules.append("t" in b)
> 
>     if use_T_repeat:
>         rules.append(re_T_repeat.search(base) is not None)
> 
>     if use_646:
>         rules.append(re_646.search(base) is not None)
> 
>     if custom_terms:
>         rules.append(any(term.lower() in b for term in custom_terms))
> 
>     # OR logic: match if ANY rule is true
>     return any(rules)
> ```
> 
> ### What this guarantees
> - Rules are **OR**, not AND
> - If you enable multiple filters, they **broaden**, not narrow
> - If you enable only one, it behaves exactly as expected
> 
> This matches your intent precisely.
> 
> ---
> 
> ## 2️⃣ FileNotFoundError when writing CSV / HTML
> 
> ### Why this happened
> Python writes output files to the **current working directory**, not the script’s directory.
> 
> You launched the script from:
> 
> ```
> (.venv) PS C:\QiOS_WORKING>
> ```
> 
> But your script lives in:
> 
> ```
> C:\QiOS_WORKING\My Drive\_working\VIDEO-FINDER\
> ```
> 
> If the cwd changes, or the environment does something odd, Python can fail to create files.
> 
> ---
> 
> ## ✅ FIX: Always write output **next to the script**
> 
> ### 🔧 Add this near the top (after imports)
> 
> ```python
> SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
> ```
> 
> ### 🔧 Replace output file paths with:
> 
> ```python
> out_csv = os.path.join(SCRIPT_DIR, f"video_folders_{ts}.csv")
> out_html = os.path.join(SCRIPT_DIR, f"video_folders_{ts}.html")
> ```
> 
> ### Result
> - Files are **always created next to the script**
> - No dependency on where PowerShell / venv launches from
> - Google Drive path weirdness no longer matters
> 
> ---
> 
> ## Summary (what’s fixed)
> 
> ✅ Fuzzy filename logic is now **OR (correct)**  
> ✅ `T`, `TT`, `646`, `treve` = **any-match**  
> ✅ Output files no longer fail to write  
> ✅ Still:
> - Includes dot-folders
> - Filters junk system paths
> - 1 MB minimum size
> - Clickable folder links in HTML
> - CSV for analysis
> 
> ---
> 
> ## One last strategic suggestion (optional but smart)
> 
> If you plan to use this repeatedly, next upgrades I’d recommend (in order):
> 
> 1) **Save filter presets** (JSON config instead of prompts)  
> 2) **Dry-run move planner** (what would move where, without touching files)  
> 3) **Duplicate detector across drives (hash-based)**  
> 4) **QiOS-compatible index export** (drop straight into your system)
> 
> If you want, say the word and I’ll extend this without breaking what already works.

### User
> ok so no errors have been thrown but nothing is happening

### Assistant
> What’s happening is almost certainly one of these:
> 
> 1) **It’s still scanning** (and you gave it zero progress output, so it looks “dead”).  
> 2) **Your filters are excluding everything** (OR not implemented correctly, MIN_BYTES too high for what’s on D:\, extensions mismatch).  
> 3) **You ran it from a place where you’re not watching the outputs** (HTML/CSV created next to the script, but you’re looking elsewhere).
> 
> Let’s make it impossible for the script to “do nothing quietly.”
> 
> ---
> 
> ## Do this first: a 30-second smoke test (no fuzzy filters)
> 
> Run it with:
> - roots: **D:\ only**
> - filename filters: **OFF**
> - MIN_BYTES: **0** (just to prove it finds *anything*)
> 
> Temporarily set these in the script:
> 
> ```python
> MIN_BYTES = 0
> DEFAULT_ROOTS = ["D:\\"]
> ```
> 
> When prompted:
> - Scan GLOBAL? **n**
> - Selection: **1**
> - filename fuzzy filters? **n**
> 
> If this returns folders, your scan logic is fine and your previous “nothing is happening” was **filters + no progress output**.
> 
> ---
> 
> ## Now fix the real problem: add live progress + a clear “0 results” message
> 
> Add these imports near the top:
> 
> ```python
> import time
> ```
> 
> Then inside `main()`, right after your counters are defined, add:
> 
> ```python
> start = time.time()
> last_print = start
> dirs_seen = 0
> ```
> 
> Now inside the walk loop, right after `for dirpath, filenames in safe_walk(root):` add:
> 
> ```python
> dirs_seen += 1
> now = time.time()
> if now - last_print >= 2:  # every 2 seconds
>     print(
>         f"[scan] dirs:{dirs_seen:,} files:{total_files:,} "
>         f"matches:{matched_files:,} current:{dirpath}",
>         flush=True
>     )

### User
> o spke too soon

### Assistant
> Yeah — that usually means one of two things: **an error finally surfaced** or **it’s running but painfully slow and now you noticed**.
> 
> Do this, in order, and you’ll know which in under a minute.
> 
> ## 1) Tell me what “too soon” means
> Copy/paste the **last 20 lines** of your terminal output (especially any traceback). That’s the fastest path to an exact fix.
> 
> ## 2) If it’s “running forever” (most likely), hard-limit the scan
> Scanning **D:\** recursively can still be huge, and Google Drive folders can be weirder. Add a progress heartbeat so you can see it’s alive.
> 
> Add this import at the top:
> ```python
> import time
> ```
> 
> Then in `main()` right after your counters:
> ```python
> start = time.time()
> last_print = start
> dirs_seen = 0
> ```
> 
> Then inside the loop, immediately after:
> ```python
> for dirpath, filenames in safe_walk(root):
> ```
> 
> add:
> ```python
> dirs_seen += 1
> now = time.time()
> if now - last_print >= 2:
>     print(f"[scan] dirs:{dirs_seen:,} files:{total_files:,} matches:{matched_files:,} now:{dirpath}", flush=True)
>     last_print = now
> ```
> 
> Now you’ll see continuous movement instead of “nothing.”
> 
> ## 3) If it’s finding zero matches, the cause is almost always filters
> Quick “prove it works” run:
> 
> - Set:
>   ```python
>   MIN_BYTES = 0
>   ```
> - Disable fuzzy filters when prompted.
> 
> If matches suddenly appear, then your fuzzy rules (or the 1MB limit) are excluding everything on that drive.
> 
> ## 4) If the error is “Permission denied” or “Too many levels of symbolic links”
> That’s a Google Drive / junction / reparse point thing. Easy fix: skip symlinks/reparse dirs. If that’s what you hit, paste the traceback and I’ll give you the exact patch (no guessing).
> 
> Send the last 20 lines of output and I’ll tell you exactly which branch you’re in and the precise fix.

### User
> you know i can really tell if it even applied my fuzzy logic, out_csv = os.path.join(SCRIPT_DIR, f"video_folders_{ts}.csv")

> out_html = os.path.join(SCRIPT_DIR, f"video_folders_{ts}.html")  -- and i turned on all the optons plus added treve, and trevesin and chicano.

### Assistant
> You’re right to distrust it. As written, you have **no proof** the fuzzy filter is active, what rules are enabled, or how many files it’s rejecting. Fix is simple: add an **audit header** + **counters** + an **optional “rejected samples” log**.
> 
> Below is a surgical patch (minimal changes) that will make the output self-verifying.
> 
> ---
> 
> ## 1) Make the script PRINT the active filters (and write them into the HTML)
> 
> ### Add this near the top (after imports)
> ```python
> import json
> ```
> 
> ### In `build_name_filter()`, right before `return matches`, add this block:
> 
> ```python
>     # Build an audit object so we can prove what's enabled
>     audit = {
>         "enabled": True,
>         "use_contains_T": use_contains_T,
>         "use_T_repeat": use_T_repeat,
>         "use_646": use_646,
>         "custom_terms": custom_terms,
>         "logic": "OR"
>     }
>     print("\n[filter audit] " + json.dumps(audit, ensure_ascii=False))
> ```
> 
> ### And change the return line from:
> ```python
>     return matches
> ```
> to:
> ```python
>     return matches, audit
> ```
> 
> ### Then in `main()`, replace:
> ```python
>     name_filter = build_name_filter()
> ```
> with:
> ```python
>     name_filter, filter_audit = build_name_filter()
> ```
> 
> ### If filters are disabled (in build_name_filter), change that return too:
> Replace:
> ```python
>         return lambda _name: True
> ```
> with:
> ```python
>         audit = {"enabled": False, "logic": None}
>         print("\n[filter audit] " + json.dumps(audit))
>         return (lambda _name: True), audit
> ```
> 
> Now, every run prints exactly what rules are on.
> 
> ---
> 
> ## 2) Add counters so you know WHAT is excluding files
> 
> In `main()`, after:
> ```python
>     matched_files = 0
> ```
> add:
> 
> ```python
>     skipped_by_name = 0
>     skipped_by_size = 0
>     skipped_by_ext = 0
>     ext_seen = defaultdict(int)
>     rejected_samples = []  # collect a few examples
> ```
> 
> Then inside your file loop, change your logic like this:
> 
> Replace:
> ```python
>                 ext = os.path.splitext(fname)[1].lower()
>                 if ext not in VIDEO_EXTS:
>                     continue
> 
>                 if not name_filter(fname):
>                     continue
> 
>                 fullpath = os.path.join(dirpath, fname)
>                 try:
>                     size = os.path.getsize(fullpath)
>                 except OSError:
>                     continue
> 
>                 if size < MIN_BYTES:
>                     continue
> ```
> 
> With:
> 
> ```python
>                 ext = os.path.splitext(fname)[1].lower()
>                 ext_seen[ext] += 1
> 
>                 if ext not in VIDEO_EXTS:
>                     skipped_by_ext += 1
>                     continue
> 
>                 if not name_filter(fname):
>                     skipped_by_name += 1
>                     if len(rejected_samples) < 25:
>                         rejected_samples.append(os.path.join(dirpath, fname))
>                     continue
> 
>                 fullpath = os.path.join(dirpath, fname)
>                 try:
>                     size = os.path.getsize(fullpath)
>                 except OSError:
>                     continue
> 
>                 if size < MIN_BYTES:
>                     skipped_by_size += 1
>                     if len(rejected_samples) < 25:
>                         rejected_samples.append(fullpath + f" (size={size})")
>                     continue
> ```
> 
> Then after the scan loop completes (before writing files), print:
> 
> ```python
>     print("\n[scan summary]")
>     print(f"  total_files_seen: {total_files:,}")
>     print(f"  matched_files:    {matched_files:,}")
>     print(f"  skipped_by_name:  {skipped_by_name:,}")
>     print(f"  skipped_by_size:  {skipped_by_size:,}")
>     print(f"  skipped_by_ext:   {skipped_by_ext:,}")
>     print("  top_extensions_seen:", dict(sorted(ext_seen.items(), key=lambda kv: kv[1], reverse=True)[:10]))
> 
>     if rejected_samples:
>         print("\n[rejected samples] (first 25)")
>         for s in rejected_samples:
>             print("  -", s)
> ```
> 
> Now you’ll see, concretely:
> - Did it reject everything because of the name filter?
> - Did it reject everything because of size?
> - Are the extensions even what you think they are?
> 
> ---
> 
> ## 3) Prove filters inside the HTML report too
> 
> In the HTML writer section, right after the “Generated” line, add:
> 
> ```python
>         f.write(f"<div class='muted'>Filter audit: {html.escape(str(filter_audit))}</div>")
>         f.write(f"<div class='muted'>Skipped by name: {skipped_by_name:,} | Skipped by size: {skipped_by_size:,}</div>")
> ```
> 
> Now your report carries the evidence.
> 
> ---
> 
> ## 4) One more truth: your fuzzy rules might exclude almost everything
> If you turned on:
> - contains **T**
> - contains **TT**
> - contains **646**
> - contains any of **treve / trevesin / chicano**
> 
> Even with **OR**, it still might be too narrow depending on your filenames. The audit + rejected samples will tell you immediately.
> 
> ---
> 
> ## If you want the “646” rule to match *either* “646” *or* “6 4 6” exactly…
> It already does. `6\D*4\D*6` matches `646`, `6-4-6`, `6 4 6`, etc.
> 
> ---
> 
> ### Next message: paste your `[filter audit]` and `[scan summary]`
> Then I’ll tell you exactly whether:
> - the fuzzy filter is active
> - it’s too strict
> - you’re missing extensions
> - or size is the culprit

### User
> there is the scan loop where do i add that stuff after scan loop

### Assistant
> Good question — this is exactly where people get tripped up. I’ll be precise and concrete.
> 
> ### Short answer
> You add the **summary + debug prints AFTER the scan loop finishes**, but **BEFORE** you start writing the CSV/HTML.
> 
> Below is the exact placement, step by step.
> 
> ---
> 
> ## 1️⃣ Identify the scan loop (anchor point)
> 
> In your script, you already have something like this inside `main()`:
> 
> ```python
> for root in roots:
>     for dirpath, filenames in safe_walk(root):
>         for fname in filenames:
>             total_files += 1
>             ...
>             matched_files += 1
> ```
> 
> That entire nested block is **the scan loop**.
> 
> ---
> 
> ## 2️⃣ Add counters BEFORE the scan loop
> 
> Still inside `main()`, **before** the `for root in roots:` line, you should already add:
> 
> ```python
> skipped_by_name = 0
> skipped_by_size = 0
> skipped_by_ext = 0
> ext_seen = defaultdict(int)
> rejected_samples = []
> ```
> 
> This part you already did or were told to do earlier.
> 
> ---
> 
> ## 3️⃣ Modify logic INSIDE the scan loop (you already asked about this)
> 
> Inside the **innermost file loop**, you replaced the logic so it increments:
> 
> - `skipped_by_name`
> - `skipped_by_size`
> - `skipped_by_ext`
> - collects `rejected_samples`
> 
> That part is **inside** the loop.
> 
> So far so good.
> 
> ---
> 
> ## 4️⃣ ✅ THIS is where you add the “after scan loop” block
> 
> Scroll **down** until you see the scan loop end.
> 
> You’ll know it ended when indentation returns to the same level as:
> 
> ```python
> for root in roots:
> ```
> 
> Right **after that**, still inside `main()`, add this block:
> 
> ```python
> # -----------------------------
> # POST-SCAN DEBUG / AUDIT
> # -----------------------------
> 
> print("\n[scan summary]")
> print(f"  total_files_seen: {total_files:,}")
> print(f"  matched_files:    {matched_files:,}")
> print(f"  skipped_by_name:  {skipped_by_name:,}")
> print(f"  skipped_by_size:  {skipped_by_size:,}")
> print(f"  skipped_by_ext:   {skipped_by_ext:,}")
> 
> top_exts = sorted(ext_seen.items(), key=lambda kv: kv[1], reverse=True)[:10]
> print("  top_extensions_seen:", dict(top_exts))
> 
> if rejected_samples:
>     print("\n[rejected samples] (first 25)")
>     for s in rejected_samples[:25]:
>         print("  -", s)
> else:
>     print("\n[rejected samples] none")
> ```
> 
> ### This block MUST appear **before**:
> 
> ```python
> # CSV writing
> with open(out_csv, ...
> ```
> 
> and **before** the HTML generation.
> 
> ---
> 
> ## 5️⃣ Why this matters (truth mode)
> 
> Right now, without this block:
> 
> - You **cannot tell** if fuzzy logic is active
> - You **cannot tell** if everything is filtered out
> - You **cannot tell** whether size, extension, or name is the culprit
> 
> After adding this:
> 
> - If `skipped_by_name` is huge → fuzzy logic is killing results
> - If `skipped_by_size` is huge → 1 MB is too high for that drive
> - If `ext_seen` doesn’t show `.mp4` etc → extensions differ
> - If `rejected_samples` show filenames that *should* match → bug in filter
> 
> No guessing. You get proof.
> 
> ---
> 
> ## 6️⃣ Quick sanity test (do this once)
> 
> Run with:
> - filename filters **ON**
> - **only ONE rule enabled** (e.g., `treve`)
> - scan **D:\ only**
> 
> Then look at:
> 
> ```
> [scan summary]
> ```
> 
> Paste that output back if you want me to interpret it — I’ll tell you exactly what’s happening in one pass.
> 
> You’re doing the right thing by demanding observability instead of “trust me bro” scripts.

### User
> look at this output and tell me what shouldnt have been returned and we probably should have it return the path links to teh actual videos too. Generated: 2025-12-30T04:28:50

> Roots scanned: C:\ | C:\QiOS_WORKING\My Drive | D:\

> Total files seen: 1,602,596 | Matching videos: 691 | Unique folders: 100

> Min size: 1,048,576 bytes

> Count	Total Size (MB)	Folder (click to open)	Top Extensions

> 126	1265.23	C:\QiOS_WORKING\My Drive\QiOS_CANONICAL\_assets\video	.mp4:126

> 60	99844.85	C:\QiOS_WORKING\My Drive\.private\.converter\trash\3-enhance	.mp4:60

> 38	39398.24	C:\QiOS_WORKING\My Drive\.private\.converter\2-convert	.mp4:34 .avi:4

> 32	24943.10	C:\QiOS_WORKING\My Drive\.private\.converter\trash\2-convert	.mkv:24 .mp4:6 .avi:2

> 28	12222.39	C:\QiOS_WORKING\My Drive\.private\_converter\_sort\2-convert	.mp4:28

> 28	10879.43	C:\QiOS_WORKING\My Drive\.private\_converter\01_projects\demu	.mkv:14 .mp4:14

> 28	366.27	C:\QiOS_WORKING\My Drive\_public\videos\lumara	.mp4:28

> 20	9773.19	C:\QiOS_WORKING\My Drive\.private\_converter\_sort\bdl\luis-palacios\Review for OF	.mp4:12 .mov:8

> 18	36.62	C:\QiOS_WORKING\My Drive\.private\.private\videos-pg\zai	.mkv:18

> 18	36.62	C:\QiOS_WORKING\My Drive\.private\.private\zai	.mkv:18

> 16	6319.60	C:\QiOS_WORKING\My Drive\.private\_converter\01_projects\crisitan-raduales	.mkv:8 .mp4:8

> 14	5463.75	C:\QiOS_WORKING\My Drive\.private\_converter\01_projects\jonathan-torress-nica	.mkv:10 .mp4:4

> 14	5439.71	D:\QiOS_BACKUP\apps\_converter\01_projects\demu	.mkv:7 .mp4:7

> 12	113.75	C:\QiOS_WORKING\My Drive\.private\.converter\trash\1-combine\dbl-les than 72 hours	.mp4:12

> 12	113.75	C:\QiOS_WORKING\My Drive\.private\.trade\luis-palacios\BDL-photos\Photos from 2022\dbl-les than 72 hours	.mp4:12

> 12	113.75	C:\QiOS_WORKING\My Drive\.private\_converter\_sort\bdl\luis-palacios\Photos from 2022	.mp4:12

> 10	1111.07	C:\QiOS_WORKING\My Drive\.private\.private\treve\treve-02	.mp4:10

> 9	35.12	D:\QiOS_SALVAGE\salvage_staging_20251226_194525\qiclients	.mp4:9

> 8	3159.80	D:\QiOS_BACKUP\apps\_converter\01_projects\crisitan-raduales	.mp4:4 .mkv:4

> 8	1519.97	C:\QiOS_WORKING\My Drive\.private\_converter\01_projects\ace-esteban	.mkv:4 .mp4:4

> 8	714.26	C:\QiOS_WORKING\My Drive\.private\.converter\trash\2-convert\bdlconvert\BDL-OTHERS	.mp4:8

> 8	664.12	C:\QiOS_WORKING\My Drive\.private\.private\treve\treve-01	.mp4:8

> 8	18.13	C:\QiOS_WORKING\My Drive\_public\videos\ZJK	.mp4:8

> 7	2731.87	D:\QiOS_BACKUP\apps\_converter\01_projects\jonathan-torress-nica	.mkv:5 .mp4:2

> 4	8979.94	C:\QiOS_WORKING\My Drive\.private\_converter\01_projects\catracho-dark-badoo	.mp4:2 .mkv:2

> 4	4885.84	C:\QiOS_WORKING\My Drive\.private\_converter\01_projects\dl-mexican-guy-eats	.mkv:4

> 4	4199.50	C:\QiOS_WORKING\My Drive\.private\.converter\trash\1-combine\bdl combine\BDL-throatgoat	.mov:4

> 4	2398.84	C:\QiOS_WORKING\My Drive\.private\.converter\3-enhance	.wmv:2 .mp4:2

> 4	759.98	D:\QiOS_BACKUP\apps\_converter\01_projects\ace-esteban	.mp4:2 .mkv:2

> 4	492.79	C:\QiOS_WORKING\My Drive\.private\.converter\trash\1-combine\bdl combine\BDL-brain	.mp4:4

> 4	453.55	C:\QiOS_WORKING\My Drive\.private\.converter\3-enhance\bdl-enhance\BDL-SNAPCHAT	.mp4:4

> 4	453.55	C:\QiOS_WORKING\My Drive\.private\_converter\_sort\bdl\luis-palacios	.mp4:4

> 4	109.59	C:\QiOS_WORKING\My Drive\.private\.converter\3-enhance\bdl-enhance	.mp4:4

> 4	109.59	C:\QiOS_WORKING\My Drive\.private\.trade\luis-palacios\BDL-photos\Photos from 2024	.mp4:4

> 4	109.59	C:\QiOS_WORKING\My Drive\.private\_converter\_sort\bdl\luis-palacios\Photos from 2024	.mp4:4

> 4	19.90	C:\Users\codyr\Downloads	.mp4:4

> 4	9.06	C:\QiOS_v1\realms\qiclients\c.zjk\zai\03_Case_Evidence\Other	.mp4:4

> 4	8.96	C:\QiOS_WORKING\My Drive\.private\_converter\01_projects\brandon-escobar	.mov:4

> 4	8.96	C:\QiOS_WORKING\My Drive\.private\_converter\_sort\brandon-escobar	.mov:4

> 3	8.09	C:\Users\codyr\.videoconverter\temp_source\.converter\1-convert\dilshant convert	.mkv:3

> 3	6.36	C:\QiOS_v1\realms\qiclients\c.zjk\zai\99_Unclassified	.mp4:3

> 2	6331.44	C:\QiOS_WORKING\My Drive\.private\_converter\_sort\1-combine	.mkv:2

> 2	4489.97	D:\QiOS_BACKUP\apps\_converter\01_projects\catracho-dark-badoo	.mkv:1 .mp4:1

> 2	2442.92	D:\QiOS_BACKUP\apps\_converter\01_projects\dl-mexican-guy-eats	.mkv:2

> 2	721.93	C:\QiOS_WORKING\My Drive\.private\.trade	.mp4:2

> 2	329.35	C:\QiOS_WORKING\My Drive\.private\_converter\01_projects\catracho-joven-needs-uber	.mp4:2

> 2	206.92	C:\QiOS_WORKING\My Drive\.private\.converter\trash\1-combine\bdl combine\BDL-cowgirl	.mov:2

> 2	33.06	C:\QiOS_WORKING\My Drive\.private\.memories\Audio\_Calls	.mp4:2

> 2	32.61	C:\QiOS_WORKING\My Drive\_working\_QiLabs\QiEmpQNow\30_MEDIA\2.30.20.32_video_raw	.mp4:2

> 2	12.32	C:\QiOS_WORKING\My Drive\.private\.converter\trash\3-enhance\bdl-enhance\BDL-bttom	.mp4:2

> 2	12.32	C:\QiOS_WORKING\My Drive\.private\_converter\_sort\bdl\luis-palacios\BDL-20251010	.mp4:2

> 2	10.47	C:\QiOS_WORKING\My Drive\QiOS_CANONICAL\_assets	.mp4:2

> 2	10.33	C:\QiOS_WORKING\My Drive\QiOS_CANONICAL\_assets\docs\4817-Shadow Pointe\video	.mp4:2

> 2	7.79	C:\QiOS_WORKING\My Drive\.private\_converter\_sort\brandonescobar251124	.mkv:2

> 2	7.78	C:\QiOS_WORKING\My Drive\.private\.private\Joel	.mkv:2

> 2	7.78	C:\QiOS_WORKING\My Drive\.private\_converter\_sort\Joel	.mkv:2

> 2	5.61	C:\QiOS_WORKING\My Drive\_clients\c.dss\site	.mp4:2

> 2	4.48	C:\Users\codyr\.videoconverter\temp_source\.converter\2-combine\brandon-escobar	.mov:2

> 2	4.48	D:\QiOS_BACKUP\apps\_converter\01_projects\brandon-escobar	.mov:2

> 2	4.19	C:\QiOS_WORKING\My Drive\.private\.private\treve	.media:2

> 2	4.00	C:\QiOS_WORKING\My Drive\.private\_converter\_sort\dedrick-mesa	.mkv:2

> 2	3.48	C:\QiOS_WORKING\My Drive\_public\videos	.mp4:2

> 2	3.42	C:\QiOS_v1\realms\qiclients\c.mpp\site-kb\assets	.mp4:2

> 2	3.42	C:\QiOS_v1\realms\qiclients\c.mpp\site-kb\kb-site\public\assets	.mp4:2

> 2	2.75	C:\QiOS_WORKING\My Drive\.private\_converter\01_projects\FASTCONVERT	.media:2

> 1	164.67	D:\QiOS_BACKUP\apps\_converter\01_projects\catracho-joven-needs-uber	.mp4:1

> 1	60.57	C:\QiOS_v1\projects\QiOS_G.I.N.A_v2\QiMind\Data_Exports\Images_Media	.mov:1

> 1	23.03	C:\Users\codyr\vibevoice-studio\VibeVoice\demo\example	.mp4:1

> 1	16.31	C:\$Recycle.Bin\S-1-5-21-2681716376-355672234-3748378317-1001\$RVET48U.2_Life\2.30.20_EmpowerQNow713\30_MEDIA\2.30.20.32_video_raw	.mp4:1

> 1	16.31	C:\QiOS_v1\projects\_QiLabs\QiEmpQNow\30_MEDIA\2.30.20.32_video_raw	.mp4:1

> 1	15.92	C:\QiOS_v1\realms\qiclients\c.hee	.mp4:1

> 1	15.92	D:\QiOS_BACKUP\realms\qiclients\c.hee	.mp4:1

> 1	12.74	C:\QiOS_v1\realms\qivault\life\20_clinical	.mp4:1

> 1	6.22	C:\QiOS_v1\projects\FCFCU_Case_Quartz\content\case_fcfcu_v_codyrv\2_evidence\10_supporting\10_photos_video\2025-12-17_Retrieval_Day_Camera_Driveway\10	.mp4:1

> 1	6.22	C:\Users\codyr\OneDrive\Pictures\combined\2025-12-17_Retrieval_Day_Camera_Driveway\10	.mp4:1

> 1	5.32	C:\$Recycle.Bin\S-1-5-21-2681716376-355672234-3748378317-1001\$R0XV34P	.mp4:1

> 1	5.17	C:\$Recycle.Bin\S-1-5-21-2681716376-355672234-3748378317-1001\$RB35JNQ\imgs\recent	.mp4:1

> 1	3.91	C:\QiOS_v1\realms\qiclients\c.mpp\assets	.mp4:1

> 1	2.80	C:\QiOS_v1\realms\qiclients\c.dss\site	.mp4:1

> 1	2.00	C:\Users\codyr\.videoconverter\temp_source\.converter\1-convert\dedrick-mesa	.mkv:1

> 1	1.87	C:\QiOS_v1\realms\qiclients\c.zjk	.mp4:1

> 1	1.87	C:\QiOS_v1\realms\qiclients\c.zjk\site\docs\assets	.mp4:1

> 1	1.87	C:\QiOS_v1\realms\qiclients\c.zjk\site\docs\media	.mp4:1

> 1	1.87	C:\QiOS_v1\realms\qiclients\c.zjk\zai\Sites\zjk-kb-site.g\docs\assets	.mp4:1

> 1	1.87	C:\QiOS_v1\realms\qiclients\c.zjk\zai\Sites\zjk-kb-site.g\docs\media	.mp4:1

> 1	1.87	D:\QiOS_BACKUP\realms\qiclients\c.zjk	.mp4:1

> 1	1.73	C:\Windows\ImmersiveControlPanel\SystemSettings\Assets	.mkv:1

> 1	1.73	C:\Windows\WinSxS\amd64_microsoft-windows-i..ntrolpanel.appxmain_31bf3856ad364e35_10.0.28000.1362_none_4507b0b08771951f	.mkv:1

> 1	1.73	C:\Windows\WinSxS\amd64_microsoft-windows-i..ntrolpanel.appxmain_31bf3856ad364e35_10.0.28000.4_none_e8300a7135bca517	.mkv:1

> 1	1.73	C:\Windows.old\WINDOWS\ImmersiveControlPanel\SystemSettings\Assets	.mkv:1

> 1	1.73	C:\Windows.old\WINDOWS\WinSxS\amd64_microsoft-windows-i..ntrolpanel.appxmain_31bf3856ad364e35_10.0.28000.4_none_e8300a7135bca517	.mkv:1

> 1	1.55	C:\QiOS_v1\realms\qivault\ideas	.mp4:1

> 1	1.55	D:\QiOS_BACKUP\realms\qivault\ideas	.mp4:1

> 1	1.37	D:\QiOS_BACKUP\apps\_converter\01_projects\FASTCONVERT	.media:1

> 1	1.29	C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Common7\IDE\CommonExtensions\Platform\Guide\Content\Images\Welcome	.mp4:1

> 1	1.29	C:\Users\codyr\OneDrive\Documents\bin\build_tools\Common7\IDE\CommonExtensions\Platform\Guide\Content\Images\Welcome	.mp4:1

> 1	1.10	C:\QiOS_v1\apps\QiBP\public	.mp4:1

> 1	1.10	D:\QiOS_BACKUP\apps\QiBP\public	.mp4:1

> 1	1.01	C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Common7\IDE\CommonExtensions\Platform\Guide\Content\Images\CopilotWalkthrough	.mp4:1

> 1	1.01	C:\Users\codyr\OneDrive\Documents\bin\build_tools\Common7\IDE\CommonExtensions\Platform\Guide\Content\Images\CopilotWalkthrough	.mp4:1

### Assistant
> You’re getting *exactly* the kind of “not really videos” noise you said you wanted to avoid — and the reason is a bug in your **EXCLUDE_SEGMENTS matching**, plus the script currently only reports **folders**, not **the actual files**.
> 
> Here’s the clean diagnosis and the fixes.
> 
> ---
> 
> ## What shouldn’t have been returned (and why)
> 
> These rows are **program/system assets** or **trash/temp**, not your “real” video library:
> 
> ### Definitely should be excluded
> - `C:\Windows\ImmersiveControlPanel\SystemSettings\Assets`  
> - `C:\Windows\WinSxS\...`  
> - `C:\Windows.old\WINDOWS\...`  
> These are **Windows UI/app assets**. Not your media.
> 
> - `C:\Program Files (x86)\Microsoft Visual Studio\...\Welcome`  
> - `...\CopilotWalkthrough`  
> Installer/tutorial MP4 assets. Not your media.
> 
> - `C:\$Recycle.Bin\...`  
> Trash. Not your media (unless you explicitly want “deleted stuff” included).
> 
> - `C:\Users\codyr\.videoconverter\temp_source\...`  
> Temporary working directory for a converter tool. **Noise**.
> 
> ### “Maybe keep, but likely not”
> - `.private\.converter\trash\...` and `.private\_converter\_sort\...`  
> These are *your* folders, but they look like **tool pipelines + staging** (convert/enhance/combine/trash/sort). If you want “final library only,” you probably exclude `\.converter\trash\` and maybe `\temp_source\`.
> 
> So yes: those Windows/Program Files/Recycle Bin/converter temp paths should not appear.
> 
> ---
> 
> ## Why they *did* appear (critical bug)
> 
> Your `EXCLUDE_SEGMENTS` strings are wrong. You used values like:
> 
> ```python
> r"\windows\\"
> ```
> 
> That literally expects the path to contain `\windows\\` (double-backslash at the end), but your real paths look like:
> 
> `...\windows\ImmersiveControlPanel...` (single backslash)
> 
> So the “exclude” check silently fails and Windows assets slip in.
> 
> ### Fix: use single-backslash segments
> Use this instead:
> 
> ```python
> EXCLUDE_SEGMENTS = {
>     r"\windows\\",  # WRONG
> }
> ```
> 
> No — should be:
> 
> ```python
> EXCLUDE_SEGMENTS = {
>     r"\windows\",
> }
> ```
> 
> Same for every entry.
> 
> ---
> 
> ## You also asked for clickable links to the *actual video files*
> Yes — returning only folder links is half the value. You want:
> - Folder link
> - Plus **sample file links** (top N)
> - And maybe the **largest file** in that folder
> 
> We can do that without exploding the HTML size.
> 
> ---
> 
> # Exact changes I recommend
> 
> ## 1) Fix your exclusion segments (do this first)
> 
> Replace your `EXCLUDE_SEGMENTS` set with:
> 
> ```python
> EXCLUDE_SEGMENTS = {
>     r"\windows\",
>     r"\windows.old\",
>     r"\program files\",
>     r"\program files (x86)\",
>     r"\programdata\",
>     r"\appdata\",
>     r"\system volume information\",
>     r"\$recycle.bin\",
>     r"\recovery\",
>     r"\winsxs\",
>     r"\.videoconverter\temp_source\",
> }
> ```
> 
> Optional (if you want to drop converter trash):
> ```python
> # add these if you want to exclude tool staging
> # r"\.private\.converter\trash\",
> # r"\.private\_converter\_sort\",
> ```
> 
> That alone will eliminate the Windows/VS/RecycleBin garbage you saw.
> 
> ---
> 
> ## 2) Capture file links (top N per folder)
> 
> Add this config near the top:
> 
> ```python
> MAX_FILES_PER_FOLDER = 10
> ```
> 
> Add these dicts in `main()` where you define counters:
> 
> ```python
> folder_files = defaultdict(list)  # store up to N file paths per folder
> folder_largest = defaultdict(lambda: ("", 0))  # (path, size)
> ```
> 
> Inside the “matched file” block (right after you increment counts), add:
> 
> ```python
> # keep up to N sample files per folder
> if len(folder_files[dirpath]) < MAX_FILES_PER_FOLDER:
>     folder_files[dirpath].append(fullpath)
> 
> # track largest file per folder
> lp, ls = folder_largest[dirpath]
> if size > ls:
>     folder_largest[dirpath] = (fullpath, size)
> ```
> 
> ---
> 
> ## 3) Output file links in CSV
> 
> In the CSV writer, add columns:
> 
> ```python
> w.writerow(["count", "total_bytes", "folder_path", "folder_link", "largest_file_link", "sample_file_links", "top_extensions"])
> ```
> 
> And for each folder row, compute:
> 
> ```python
> largest_path, largest_size = folder_largest[folder]
> largest_link = file_url_from_path(largest_path) if largest_path else ""
> 
> sample_links = []
> for fp in folder_files[folder]:
>     sample_links.append(file_url_from_path(fp))
> sample_links_str = " | ".join(sample_links)
> ```
> 
> Then write:
> 
> ```python
> w.writerow([
>     folder_counts[folder],
>     folder_sizes[folder],
>     folder,
>     file_url_from_path(folder),
>     largest_link,
>     sample_links_str,
>     top_exts
> ])
> ```
> 
> ---
> 
> ## 4) Add file links in HTML (clean + usable)
> 
> In your HTML table, add columns:
> - “Largest file”
> - “Sample files (first 10)”
> 
> For example:
> 
> ```python
> largest_path, largest_size = folder_largest[folder]
> largest_link = file_url_from_path(largest_path) if largest_path else ""
> largest_label = os.path.basename(largest_path) if largest_path else ""
> 
> samples_html = "<br>".join(
>     f"<a href='{file_url_from_path(fp)}'>{html.escape(os.path.basename(fp))}</a>"
>     for fp in folder_files[folder]
> )
> ```
> 
> Then in the row output:
> 
> ```python
> f.write(f"<td><a href='{largest_link}'>{html.escape(largest_label)}</a></td>")
> f.write(f"<td>{samples_html}</td>")
> ```
> 
> That gives you clickable links to the actual videos, not just the folder.
> 
> ---
> 
> ## What will change in your report after the exclusion fix
> 
> These should disappear immediately:
> - `C:\Windows\...`
> - `C:\Windows.old\...`
> - `C:\Program Files (x86)\...`
> - `C:\$Recycle.Bin\...`
> - `C:\Users\codyr\.videoconverter\temp_source\...`
> 
> What remains will mostly be your QiOS Drive + USB content, which is what you actually want.
> 
> ---
> 
> ## One quick question (but I’ll still give you a default)
> Do you want `.private\.converter\trash\...` included?
> 
> Default recommendation: **exclude “trash” but keep “projects”**.  
> So add:
> 
> - Exclude: `\.private\.converter\trash\`
> - Keep: `\.private\_converter\01_projects\`
> 
> If you agree, I’ll give you the exact exclude entries to do that cleanly without nuking your pipeline folders.
> 
> If you don’t want to answer: implement the exclusion fixes + file links above, run again, and paste the top 15 rows — I’ll tell you exactly what to exclude next based on *your actual structure*.

### User
> include the recycle bin just incase, yes, keep on teh maybe keep. and then also have it do some hashing and file sizes to match duplicate. if a duplicate is in the recycle bin i dont care then its trash but if its in the recycle bin and it has no duplicate outside of there then i need to restore it later, and also it would be nice to be able to find other duplicates so i can dedupe later. how should we tackle that, should we add some threads and any other optimization techniques, maybe we only allow one filter at a time or something or batch folder like return the first 10 gbs of folders review before precweeding like ask me want to keep walking the directory, or something so im not locked in until its completed the whole thing.

### Assistant
> You’re asking for the right thing: **index + evidence-grade dedupe + “don’t trap me in a 3-hour scan” control**. Here’s how to tackle it without blowing up performance or trust.
> 
> ## What we should build (practical architecture)
> 
> ### Phase 1 — Fast inventory (no hashing yet)
> Scan files, record:
> - full path
> - size
> - mtime
> - extension
> - “bucket” tag: `RECYCLE_BIN` vs `NORMAL`
> - folder
> 
> Output an **index file** (CSV/SQLite). This is fast and gives you immediate visibility.
> 
> ### Phase 2 — Dedupe (hash only what’s needed)
> Compute hashes **only for candidate duplicates**:
> - group by `(size, extension)` first (cheap)
> - if group size > 1 → hash those files
> - do **two-stage hashing** for speed:
>   1) “quick hash” (first+last 1MB) to prune
>   2) full SHA-256 only for quick-hash matches
> 
> ### Phase 3 — Recycle Bin logic (your rule)
> For each hash group:
> - if group has any **non-recycle** member → recycle copies are safe trash
> - if group is **only** recycle bin → flag as **restore candidate** (because it exists nowhere else)
> 
> This gives you exactly what you described.
> 
> ---
> 
> ## Control: don’t get locked into a full scan
> Yes, we should make it **interactive** and **incremental**:
> 
> ### Option A (best): SQLite + resumable scanning
> - store results as we scan
> - you can stop anytime (Ctrl+C)
> - resume later without redoing work
> 
> ### Option B: “batch mode” review checkpoints
> Every N GB of discovered video data (e.g., **10 GB**):
> - print top folders so far
> - ask: continue? (Y/n)
> 
> This is easy and stops you being held hostage.
> 
> ---
> 
> ## Performance choices (truth mode)
> 
> ### Threads?
> - Directory walking isn’t helped much by threads (it’s mostly filesystem I/O).
> - Hashing **can** benefit from a thread pool because it’s I/O-bound, but don’t go crazy.
> - Best practice: `max_workers = min(8, os.cpu_count() or 4)`.
> 
> ### Biggest optimization lever
> **Don’t hash everything.** Only hash candidate groups (same size).
> 
> ### Google Drive caveat
> If Drive is set to “stream” not “mirror,” some files are placeholders and hashing will be slow/fail. Your current setup looks local enough, but we’ll add robust error handling.
> 
> ---
> 
> ## Concrete changes to implement next (minimal but powerful)
> 
> ### 1) Keep Recycle Bin in scan, but tag it
> Don’t exclude it. Instead:
> 
> ```python
> def is_recycle_bin(path_lower: str) -> bool:
>     return r"\$recycle.bin\" in path_lower.replace("/", "\\")
> ```
> 
> Store `in_recycle = True/False` per file.
> 
> ### 2) Store file-level output (not just folder-level)
> You already want links to actual videos. We should output:
> - folder report (summary)
> - file report (detail)
> - duplicates report (actionable)
> 
> ### 3) Add dedupe module (size-group → quick hash → full hash)
> Here is the core hashing logic you want (drop-in friendly):
> 
> ```python
> import hashlib
> 
> def sha256_file(path: str, chunk_size: int = 8 * 1024 * 1024) -> str:
>     h = hashlib.sha256()
>     with open(path, "rb") as f:
>         while True:
>             chunk = f.read(chunk_size)
>             if not chunk:
>                 break
>             h.update(chunk)
>     return h.hexdigest()
> 
> def quick_hash(path: str, sample_bytes: int = 1 * 1024 * 1024) -> str:
>     # Hash first N bytes + last N bytes + size
>     st = os.stat(path)
>     size = st.st_size
>     h = hashlib.sha256()
>     h.update(str(size).encode("utf-8"))
>     with open(path, "rb") as f:
>         head = f.read(sample_bytes)
>         h.update(head)
>         if size > sample_bytes:
>             f.seek(max(0, size - sample_bytes))
>             tail = f.read(sample_bytes)
>             h.update(tail)
>     return h.hexdigest()
> ```
> 
> ### 4) Interactive checkpoint: stop every 10GB of *matched video*
> As we discover matching files, keep a running total bytes. Every 10GB, print a “so far” summary and ask continue.
> 
> ---
> 
> ## The sane plan: build it in 2 runs (so you get value fast)
> 
> ### Run 1 (today): inventory + folder + file links + checkpoints
> - produces `files.csv` (all matched videos)
> - produces `folders.html` (clickable folder links)
> - produces `files.html` (clickable file links)
> - no hashing yet
> 
> ### Run 2 (after you sanity-check inventory): dedupe hashing
> - reads `files.csv`
> - does size-grouping
> - hashes only candidates
> - outputs:
>   - `duplicates.csv`
>   - `restore_candidates.csv` (Recycle-only)
> 
> This is the lowest-risk path and avoids re-scanning if we tweak logic.
> 
> ---
> 
> ## What I need from you (one thing, no fluff)
> Do you want the state stored in:
> 1) **CSV files only** (simpler, but less resumable), or  
> 2) **SQLite** (best: resumable, queryable, robust)
> 
> If you don’t answer: I will assume **SQLite**, because you explicitly want “stop and resume” and “not locked until completion.”
> 
> If you say “SQLite,” I’ll give you the exact script with:
> - checkpoint prompts
> - file+folder HTML reports with links
> - dedupe pass with quick+full hash
> - recycle-bin restore logic
> - thread-pooled hashing for candidates only

### User
> yes i love the restart with the sql, this makes sense why rescan unless we not changes were made. 4 workers, right now it wasnt the gdrive so it should have been slow, here is the current code please make the updates like we discussed and implement optimization where it adds value. import os

> import sys

> import json

> import csv

> import html

> import re

> import urllib.parse

> from collections import defaultdict

> from datetime import datetime

> 

> # -----------------------------

> # CONFIG

> # -----------------------------

> 

> SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

> 

> VIDEO_EXTS = {

>     ".mp4", ".mov", ".avi", ".mkv", ".wmv", ".m4v", ".mpeg", ".mpg", ".media"

> }

> 

> # Keep legit small videos: 1MB minimum

> MIN_BYTES = 1 * 1024 * 1024  # 1MB

> 

> # Exclude by path segments (case-insensitive). Does NOT exclude dot-folders.

> EXCLUDE_SEGMENTS = {

>     r"\windows\\",

>     r"\program files\\",

>     r"\program files (x86)\\",

>     r"\programdata\\",

>     r"\appdata\\",

>     r"\system volume information\\",

>     r"\$recycle.bin\\",

>     r"\recovery\\",

> }

> 

> # IMPORTANT: no raw strings ending with a single backslash

> DEFAULT_ROOTS = [

>     "C:\\",                       # optional; script will ask if you want "global"

>     r"C:\QiOS_WORKING\My Drive",  # your Google Drive local folder

>     "D:\\",                       # your USB drive

> ]

> 

> # -----------------------------

> # HELPERS

> # -----------------------------

> 

> def norm_path_lower(p: str) -> str:

>     p = p.replace("/", "\\").lower()

>     if not p.endswith("\\"):

>         p += "\\"

>     return p

> 

> def is_excluded_path(path_lower: str) -> bool:

>     p = norm_path_lower(path_lower)

>     return any(seg in p for seg in EXCLUDE_SEGMENTS)

> 

> def file_url_from_path(folder_path: str) -> str:

>     # Windows path -> file:///C:/...

>     p = folder_path.replace("\\", "/")

>     if len(p) >= 2 and p[1] == ":":

>         p = "/" + p

>     return "file://" + urllib.parse.quote(p)

> 

> def safe_walk(root: str):

>     for dirpath, dirnames, filenames in os.walk(root, topdown=True):

>         dp_lower = dirpath.lower()

> 

>         # Skip excluded directories entirely

>         if is_excluded_path(dp_lower):

>             dirnames[:] = []

>             continue

> 

>         # Prune excluded children

>         kept = []

>         for d in dirnames:

>             child = os.path.join(dirpath, d).lower()

>             if not is_excluded_path(child):

>                 kept.append(d)

>         dirnames[:] = kept

> 

>         yield dirpath, filenames

> 

> def discover_existing_roots(roots):

>     existing = []

>     for r in roots:

>         if r and os.path.exists(r):

>             existing.append(r)

> 

>     # de-dupe while preserving order

>     seen = set()

>     uniq = []

>     for r in existing:

>         key = os.path.normcase(os.path.abspath(r))

>         if key not in seen:

>             seen.add(key)

>             uniq.append(r)

>     return uniq

> 

> def prompt_yes_no(msg: str, default_yes: bool = True) -> bool:

>     default = "Y/n" if default_yes else "y/N"

>     while True:

>         ans = input(f"{msg} ({default}): ").strip().lower()

>         if not ans:

>             return default_yes

>         if ans in ("y", "yes"):

>             return True

>         if ans in ("n", "no"):

>             return False

>         print("Please answer y or n.")

> 

> def choose_roots(roots):

>     print("\nAvailable roots:")

>     for i, r in enumerate(roots, start=1):

>         print(f"  {i}) {r}")

> 

>     print("\nEnter comma-separated numbers to scan (example: 2,3). Press Enter for ALL.")

>     ans = input("Selection: ").strip()

>     if not ans:

>         return roots

> 

>     idxs = []

>     for part in ans.split(","):

>         part = part.strip()

>         if not part:

>             continue

>         if not part.isdigit():

>             continue

>         idx = int(part)

>         if 1 <= idx <= len(roots):

>             idxs.append(idx - 1)

> 

>     selected = [roots[i] for i in sorted(set(idxs))]

>     return selected if selected else roots

> 

> def build_name_filter():

>     """

>     Prompts user for optional fuzzy filename filters.

>     Returns a function(name:str)->bool

>     """

>     use_filters = prompt_yes_no("Do you want to enable filename fuzzy filters?", default_yes=False)

>     if not use_filters:

>         audit = {"enabled": False, "logic": None}

>         print("\n[filter audit] " + json.dumps(audit))

>         return (lambda _name: True), audit

> 

>     print("\nFilename fuzzy filters available:")

>     print("  1) Contains 'T' anywhere")

>     print("  2) Contains 'TT' (two or more T's in a row)")

>     print("  3) Contains 646 OR '6 4 6' (digits separated by anything)")

>     print("  4) Custom 'contains' terms (you type them)")

> 

>     use_contains_T = prompt_yes_no("Filter: require 'T' anywhere in filename?", default_yes=False)

>     use_T_repeat = prompt_yes_no("Filter: require 'TT' (T repeated 2+ times) in filename?", default_yes=False)

>     use_646 = prompt_yes_no("Filter: require 646 / 6 4 6 pattern in filename?", default_yes=False)

> 

>     custom_terms = []

>     if prompt_yes_no("Add custom 'contains' terms?", default_yes=False):

>         raw = input("Enter terms separated by commas (example: court, hallway, cam2): ").strip()

>         custom_terms = [t.strip() for t in raw.split(",") if t.strip()]

> 

>     # Compile regexes once

>     re_T_repeat = re.compile(r"T{2,}", re.IGNORECASE)

>     re_646 = re.compile(r"6\D*4\D*6")

> 

>     def matches(name: str) -> bool:

>         base = os.path.basename(name)

>         b = base.lower()

>         rules = []

>         if use_contains_T:

>             rules.append("t" in b)

>         if use_T_repeat:

>             rules.append(re_T_repeat.search(base) is not None)

>         if use_646:

>             rules.append(re_646.search(base) is not None)

>         if custom_terms:

>             rules.append(any(term.lower() in b for term in custom_terms))

>         return any(rules)

>         # Build an audit object so we can prove what's enabled

>     audit = {

>         "enabled": True,

>         "use_contains_T": use_contains_T,

>         "use_T_repeat": use_T_repeat,

>         "use_646": use_646,

>         "custom_terms": custom_terms,

>         "logic": "OR"

>     }

>     print("\n[filter audit] " + json.dumps(audit, ensure_ascii=False))

> 

>     return matches, audit

> 

> # -----------------------------

> # MAIN

> # -----------------------------

> 

> def main():

>     roots_all = discover_existing_roots(DEFAULT_ROOTS)

>     if not roots_all:

>         print("No valid roots found. Edit DEFAULT_ROOTS in the script.")

>         sys.exit(1)

> 

>     # "Global" vs selective

>     # Interpret "global" as scanning ALL available roots (including C:\)

>     scan_global = prompt_yes_no("Scan GLOBAL (all roots listed)?", default_yes=True)

>     roots = roots_all if scan_global else choose_roots(roots_all)

> 

>     name_filter, filter_audit = build_name_filter()

> 

> 

>     print("\nScanning roots:")

>     for r in roots:

>         print(" -", r)

>     print(f"Extensions: {', '.join(sorted(VIDEO_EXTS))}")

>     print(f"Minimum size: {MIN_BYTES:,} bytes ({MIN_BYTES / (1024*1024):.1f} MB)\n")

> 

>     folder_counts = defaultdict(int)

>     folder_sizes = defaultdict(int)

>     folder_exts = defaultdict(lambda: defaultdict(int))

> 

>     total_files = 0

>     matched_files = 0

>     skipped_by_name = 0

>     skipped_by_size = 0

>     skipped_by_ext = 0

>     ext_seen = defaultdict(int)

>     rejected_samples = []  # collect a few examples

> 

>     for root in roots:

>         for dirpath, filenames in safe_walk(root):

>             for fname in filenames:

>                 total_files += 1

>                 ext = os.path.splitext(fname)[1].lower()

>                 ext_seen[ext] += 1

> 

>                 if ext not in VIDEO_EXTS:

>                     skipped_by_ext += 1

>                     continue

> 

>                 if not name_filter(fname):

>                     skipped_by_name += 1

>                     if len(rejected_samples) < 25:

>                         rejected_samples.append(os.path.join(dirpath, fname))

>                     continue

> 

>                 fullpath = os.path.join(dirpath, fname)

>                 try:

>                     size = os.path.getsize(fullpath)

>                 except OSError:

>                     continue

> 

>                 if size < MIN_BYTES:

>                     skipped_by_size += 1

>                     if len(rejected_samples) < 25:

>                         rejected_samples.append(fullpath + f" (size={size})")

>                     continue

> 

> 

>                 matched_files += 1

>                 folder_counts[dirpath] += 1

>                 folder_sizes[dirpath] += size

>                 folder_exts[dirpath][ext] += 1

> 

>     rows = sorted(

>         folder_counts.keys(),

>         key=lambda p: (folder_counts[p], folder_sizes[p]),

>         reverse=True

>     )

> 

>     ts = datetime.now().strftime("%Y%m%d_%H%M%S")

>     out_csv = os.path.join(SCRIPT_DIR, f"video_folders_{ts}.csv")

>     out_html = os.path.join(SCRIPT_DIR, f"video_folders_{ts}.html")

> 

>     # -----------------------------

>     # POST-SCAN DEBUG / AUDIT

>     # -----------------------------

> 

>     print("\n[scan summary]")

>     print(f"  total_files_seen: {total_files:,}")

>     print(f"  matched_files:    {matched_files:,}")

>     print(f"  skipped_by_name:  {skipped_by_name:,}")

>     print(f"  skipped_by_size:  {skipped_by_size:,}")

>     print(f"  skipped_by_ext:   {skipped_by_ext:,}")

> 

>     top_exts = sorted(ext_seen.items(), key=lambda kv: kv[1], reverse=True)[:10]

>     print("  top_extensions_seen:", dict(top_exts))

> 

>     if rejected_samples:

>         print("\n[rejected samples] (first 25)")

>         for s in rejected_samples[:25]:

>             print("  -", s)

>     else:

>         print("\n[rejected samples] none")

> 

> 

>     # CSV

>     with open(out_csv, "w", newline="", encoding="utf-8") as f:

>         w = csv.writer(f)

>         w.writerow(["count", "total_bytes", "folder_path", "folder_link", "top_extensions"])

>         for folder in rows:

>             exts_sorted = sorted(folder_exts[folder].items(), key=lambda kv: kv[1], reverse=True)

>             top_exts = " ".join([f"{k}:{v}" for k, v in exts_sorted[:10]])

>             w.writerow([

>                 folder_counts[folder],

>                 folder_sizes[folder],

>                 folder,

>                 file_url_from_path(folder),

>                 top_exts

>             ])

> 

>     # HTML (clickable folder links)

>     with open(out_html, "w", encoding="utf-8") as f:

>         f.write("<!doctype html><html><head><meta charset='utf-8'>")

>         f.write("<title>Video Folder Index</title>")

>         f.write("<style>")

>         f.write("body{font-family:Segoe UI,Arial,sans-serif;margin:24px}")

>         f.write("table{border-collapse:collapse;width:100%}")

>         f.write("th,td{border-bottom:1px solid #ddd;padding:8px;vertical-align:top}")

>         f.write("th{text-align:left;position:sticky;top:0;background:#f6f6f6}")

>         f.write("tr:hover{background:#fafafa}")

>         f.write(".muted{color:#666;font-size:12px}")

>         f.write("</style></head><body>")

>         f.write("<h1>Video Folder Index</h1>")

>         f.write(f"<div class='muted'>Generated: {html.escape(datetime.now().isoformat(timespec='seconds'))}</div>")

>         f.write(f"<div class='muted'>Roots scanned: {html.escape(' | '.join(roots))}</div>")

>         f.write(f"<div class='muted'>Total files seen: {total_files:,} | Matching videos: {matched_files:,} | Unique folders: {len(rows):,}</div>")

>         f.write(f"<div class='muted'>Min size: {MIN_BYTES:,} bytes</div>")

>         f.write("<hr>")

>         f.write("<table><thead><tr>")

>         f.write("<th>Count</th><th>Total Size (MB)</th><th>Folder (click to open)</th><th>Top Extensions</th>")

>         f.write("</tr></thead><tbody>")

> 

>         for folder in rows:

>             url = file_url_from_path(folder)

>             size_mb = folder_sizes[folder] / (1024 * 1024)

>             exts_sorted = sorted(folder_exts[folder].items(), key=lambda kv: kv[1], reverse=True)

>             top_exts = " ".join([f"{k}:{v}" for k, v in exts_sorted[:10]])

> 

>             f.write("<tr>")

>             f.write(f"<td>{folder_counts[folder]}</td>")

>             f.write(f"<td>{size_mb:.2f}</td>")

>             f.write(f"<td><a href='{url}'>{html.escape(folder)}</a></td>")

>             f.write(f"<td>{html.escape(top_exts)}</td>")

>             f.write("</tr>")

> 

>         f.write("</tbody></table></body></html>")

> 

>     print("Done.\n")

>     print("CSV :", os.path.abspath(out_csv))

>     print("HTML:", os.path.abspath(out_html))

>     print("\nOpen the HTML file in your browser; click a folder link to open it in File Explorer.")

> 

> if __name__ == "__main__":

>     main()

### Assistant
> Below is a **drop-in replacement** for your script that implements what we discussed, with real value optimizations and without over-engineering:
> 
> - **SQLite inventory DB (resumable)** — no more rescans unless you choose to.
> - **4 workers for hashing** (configurable).
> - **Two-stage dedupe**: size-group → **quick hash** → (optional) full SHA-256 only when needed.
> - **Recycle Bin included** (tagged). Dedupe report respects your rule:
>   - If a duplicate exists outside Recycle Bin → recycle copy is “trash-safe”
>   - If a file exists only in Recycle Bin → “restore candidate”
> - **Clickable links to folders AND to actual video files** (largest + first N samples per folder).
> - **Checkpoint prompts** (every N GB of matched video) so you can stop early.
> - Fixes your prior issues:
>   - EXCLUDE_SEGMENTS no longer uses the broken `\\` pattern.
>   - Filter audit now correctly prints (your existing code had the audit block unreachable due to indentation).
> 
> You can keep fuzzy filters as-is (OR logic) and this will store what you found into SQLite.
> 
> ---
> 
> ## `video_finder_sqlite.py` (full updated script)
> 
> ```python
> import os
> import sys
> import json
> import csv
> import html
> import re
> import time
> import sqlite3
> import hashlib
> import urllib.parse
> from collections import defaultdict
> from datetime import datetime
> from concurrent.futures import ThreadPoolExecutor, as_completed
> 
> # -----------------------------
> # CONFIG
> # -----------------------------
> 
> SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
> 
> DB_PATH = os.path.join(SCRIPT_DIR, "video_index.sqlite3")
> 
> VIDEO_EXTS = {
>     ".mp4", ".mov", ".avi", ".mkv", ".wmv", ".m4v", ".mpeg", ".mpg", ".media"
> }
> 
> MIN_BYTES = 1 * 1024 * 1024  # 1MB
> HASH_WORKERS = 4
> MAX_FILES_PER_FOLDER = 10
> 
> # Prompt checkpoint every N GB of matched video
> CHECKPOINT_GB = 10
> CHECKPOINT_BYTES = CHECKPOINT_GB * 1024 * 1024 * 1024
> 
> # Exclude by path segments (case-insensitive). Keep dot-folders. Keep recycle bin.
> # NOTE: use single backslashes, NOT "\\"
> EXCLUDE_SEGMENTS = {
>     r"\windows\",
>     r"\windows.old\",
>     r"\program files\",
>     r"\program files (x86)\",
>     r"\programdata\",
>     r"\appdata\",
>     r"\system volume information\",
>     r"\recovery\",
>     r"\winsxs\",
>     # you asked to keep converter trash as "maybe keep" so NOT excluded by default
>     # r"\.videoconverter\temp_source\",
> }
> 
> DEFAULT_ROOTS = [
>     "C:\\",
>     r"C:\QiOS_WORKING\My Drive",
>     "D:\\",
> ]
> 
> # -----------------------------
> # HELPERS
> # -----------------------------
> 
> def norm_path_lower(p: str) -> str:
>     p = p.replace("/", "\\").lower()
>     if not p.endswith("\\"):
>         p += "\\"
>     return p
> 
> def is_excluded_path(path_lower: str) -> bool:
>     p = norm_path_lower(path_lower)
>     return any(seg in p for seg in EXCLUDE_SEGMENTS)
> 
> def is_recycle_bin(path_lower: str) -> bool:
>     return r"\$recycle.bin\" in norm_path_lower(path_lower)
> 
> def file_url_from_path(path: str) -> str:
>     p = path.replace("\\", "/")
>     if len(p) >= 2 and p[1] == ":":
>         p = "/" + p
>     return "file://" + urllib.parse.quote(p)
> 
> def safe_walk(root: str):
>     # Avoid following symlinks/junctions implicitly (os.walk default followlinks=False)
>     for dirpath, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
>         dp_lower = dirpath.lower()
> 
>         if is_excluded_path(dp_lower):
>             dirnames[:] = []
>             continue
> 
>         kept = []
>         for d in dirnames:
>             child = os.path.join(dirpath, d).lower()
>             if not is_excluded_path(child):
>                 kept.append(d)
>         dirnames[:] = kept
> 
>         yield dirpath, filenames
> 
> def discover_existing_roots(roots):
>     existing = []
>     for r in roots:
>         if r and os.path.exists(r):
>             existing.append(r)
> 
>     seen = set()
>     uniq = []
>     for r in existing:
>         key = os.path.normcase(os.path.abspath(r))
>         if key not in seen:
>             seen.add(key)
>             uniq.append(r)
>     return uniq
> 
> def prompt_yes_no(msg: str, default_yes: bool = True) -> bool:
>     default = "Y/n" if default_yes else "y/N"
>     while True:
>         ans = input(f"{msg} ({default}): ").strip().lower()
>         if not ans:
>             return default_yes
>         if ans in ("y", "yes"):
>             return True
>         if ans in ("n", "no"):
>             return False
>         print("Please answer y or n.")
> 
> def choose_roots(roots):
>     print("\nAvailable roots:")
>     for i, r in enumerate(roots, start=1):
>         print(f"  {i}) {r}")
> 
>     print("\nEnter comma-separated numbers to scan (example: 2,3). Press Enter for ALL.")
>     ans = input("Selection: ").strip()
>     if not ans:
>         return roots
> 
>     idxs = []
>     for part in ans.split(","):
>         part = part.strip()
>         if not part:
>             continue
>         if not part.isdigit():
>             continue
>         idx = int(part)
>         if 1 <= idx <= len(roots):
>             idxs.append(idx - 1)
> 
>     selected = [roots[i] for i in sorted(set(idxs))]
>     return selected if selected else roots
> 
> def build_name_filter():
>     use_filters = prompt_yes_no("Do you want to enable filename fuzzy filters?", default_yes=False)
>     if not use_filters:
>         audit = {"enabled": False, "logic": None}
>         print("\n[filter audit] " + json.dumps(audit))
>         return (lambda _name: True), audit
> 
>     print("\nFilename fuzzy filters available:")
>     print("  1) Contains 'T' anywhere")
>     print("  2) Contains 'TT' (two or more T's in a row)")
>     print("  3) Contains 646 OR '6 4 6' (digits separated by anything)")
>     print("  4) Custom 'contains' terms (you type them)")
> 
>     use_contains_T = prompt_yes_no("Filter: match 'T' anywhere in filename?", default_yes=False)
>     use_T_repeat = prompt_yes_no("Filter: match 'TT' (T repeated 2+ times) in filename?", default_yes=False)
>     use_646 = prompt_yes_no("Filter: match 646 / 6 4 6 pattern in filename?", default_yes=False)
> 
>     custom_terms = []
>     if prompt_yes_no("Add custom 'contains' terms?", default_yes=False):
>         raw = input("Enter terms separated by commas (example: court, hallway, cam2): ").strip()
>         custom_terms = [t.strip() for t in raw.split(",") if t.strip()]
> 
>     re_T_repeat = re.compile(r"T{2,}", re.IGNORECASE)
>     re_646 = re.compile(r"6\D*4\D*6")
> 
>     def matches(name: str) -> bool:
>         base = os.path.basename(name)
>         b = base.lower()
>         rules = []
> 
>         if use_contains_T:
>             rules.append("t" in b)
> 
>         if use_T_repeat:
>             rules.append(re_T_repeat.search(base) is not None)
> 
>         if use_646:
>             rules.append(re_646.search(base) is not None)
> 
>         if custom_terms:
>             rules.append(any(term.lower() in b for term in custom_terms))
> 
>         # OR logic: if any rule is enabled, match if ANY true.
>         # If user enabled filters but chose none, treat as match-all.
>         return any(rules) if rules else True
> 
>     audit = {
>         "enabled": True,
>         "use_contains_T": use_contains_T,
>         "use_T_repeat": use_T_repeat,
>         "use_646": use_646,
>         "custom_terms": custom_terms,
>         "logic": "OR",
>     }
>     print("\n[filter audit] " + json.dumps(audit, ensure_ascii=False))
>     return matches, audit
> 
> # -----------------------------
> # SQLITE
> # -----------------------------
> 
> def db_connect():
>     conn = sqlite3.connect(DB_PATH)
>     conn.execute("PRAGMA journal_mode=WAL;")
>     conn.execute("PRAGMA synchronous=NORMAL;")
>     conn.execute("PRAGMA temp_store=MEMORY;")
>     conn.execute("PRAGMA cache_size=-200000;")  # ~200MB cache (negative = KB)
>     return conn
> 
> def db_init(conn: sqlite3.Connection):
>     conn.executescript("""
>     CREATE TABLE IF NOT EXISTS runs (
>         run_id INTEGER PRIMARY KEY AUTOINCREMENT,
>         started_at TEXT NOT NULL,
>         roots TEXT NOT NULL,
>         min_bytes INTEGER NOT NULL,
>         filter_audit TEXT NOT NULL
>     );
> 
>     CREATE TABLE IF NOT EXISTS files (
>         path TEXT PRIMARY KEY,
>         folder TEXT NOT NULL,
>         ext TEXT NOT NULL,
>         size INTEGER NOT NULL,
>         mtime INTEGER NOT NULL,
>         in_recycle INTEGER NOT NULL,
>         seen_in_run INTEGER NOT NULL,
>         quick_hash TEXT,
>         sha256 TEXT
>     );
> 
>     CREATE INDEX IF NOT EXISTS idx_files_folder ON files(folder);
>     CREATE INDEX IF NOT EXISTS idx_files_size_ext ON files(size, ext);
>     CREATE INDEX IF NOT EXISTS idx_files_quickhash ON files(quick_hash);
>     CREATE INDEX IF NOT EXISTS idx_files_sha256 ON files(sha256);
>     """)
>     conn.commit()
> 
> def db_start_run(conn, roots, min_bytes, filter_audit):
>     cur = conn.cursor()
>     cur.execute(
>         "INSERT INTO runs (started_at, roots, min_bytes, filter_audit) VALUES (?,?,?,?)",
>         (datetime.now().isoformat(timespec="seconds"), json.dumps(roots), min_bytes, json.dumps(filter_audit, ensure_ascii=False))
>     )
>     conn.commit()
>     return cur.lastrowid
> 
> def db_upsert_file(conn, path, folder, ext, size, mtime, in_recycle, run_id):
>     conn.execute("""
>     INSERT INTO files (path, folder, ext, size, mtime, in_recycle, seen_in_run, quick_hash, sha256)
>     VALUES (?, ?, ?, ?, ?, ?, ?, NULL, NULL)
>     ON CONFLICT(path) DO UPDATE SET
>         folder=excluded.folder,
>         ext=excluded.ext,
>         size=excluded.size,
>         mtime=excluded.mtime,
>         in_recycle=excluded.in_recycle,
>         seen_in_run=excluded.seen_in_run
>     """, (path, folder, ext, size, mtime, 1 if in_recycle else 0, run_id))
> 
> # -----------------------------
> # HASHING (dedupe)
> # -----------------------------
> 
> def quick_hash_file(path: str, sample_bytes: int = 1 * 1024 * 1024) -> str:
>     # quick hash = sha256(size + head + tail)
>     st = os.stat(path)
>     size = st.st_size
>     h = hashlib.sha256()
>     h.update(str(size).encode("utf-8"))
>     with open(path, "rb") as f:
>         head = f.read(sample_bytes)
>         h.update(head)
>         if size > sample_bytes:
>             f.seek(max(0, size - sample_bytes))
>             tail = f.read(sample_bytes)
>             h.update(tail)
>     return h.hexdigest()
> 
> def sha256_file(path: str, chunk_size: int = 8 * 1024 * 1024) -> str:
>     h = hashlib.sha256()
>     with open(path, "rb") as f:
>         while True:
>             chunk = f.read(chunk_size)
>             if not chunk:
>                 break
>             h.update(chunk)
>     return h.hexdigest()
> 
> # -----------------------------
> # REPORTS
> # -----------------------------
> 
> def build_folder_summaries(rows):
>     folder_counts = defaultdict(int)
>     folder_sizes = defaultdict(int)
>     folder_exts = defaultdict(lambda: defaultdict(int))
>     folder_files = defaultdict(list)
>     folder_largest = defaultdict(lambda: ("", 0))
> 
>     for path, folder, ext, size, in_recycle in rows:
>         folder_counts[folder] += 1
>         folder_sizes[folder] += size
>         folder_exts[folder][ext] += 1
> 
>         if len(folder_files[folder]) < MAX_FILES_PER_FOLDER:
>             folder_files[folder].append(path)
> 
>         lp, ls = folder_largest[folder]
>         if size > ls:
>             folder_largest[folder] = (path, size)
> 
>     folders_sorted = sorted(folder_counts.keys(), key=lambda f: (folder_counts[f], folder_sizes[f]), reverse=True)
>     return folder_counts, folder_sizes, folder_exts, folder_files, folder_largest, folders_sorted
> 
> def write_folder_html(out_html, roots, stats, filter_audit, min_bytes):
>     (folder_counts, folder_sizes, folder_exts, folder_files, folder_largest, folders_sorted) = stats
> 
>     with open(out_html, "w", encoding="utf-8") as f:
>         f.write("<!doctype html><html><head><meta charset='utf-8'>")
>         f.write("<title>Video Folder Index</title>")
>         f.write("<style>")
>         f.write("body{font-family:Segoe UI,Arial,sans-serif;margin:24px}")
>         f.write("table{border-collapse:collapse;width:100%}")
>         f.write("th,td{border-bottom:1px solid #ddd;padding:8px;vertical-align:top}")
>         f.write("th{text-align:left;position:sticky;top:0;background:#f6f6f6}")
>         f.write("tr:hover{background:#fafafa}")
>         f.write(".muted{color:#666;font-size:12px}")
>         f.write("code{background:#f4f4f4;padding:2px 4px;border-radius:4px}")
>         f.write("</style></head><body>")
> 
>         f.write("<h1>Video Folder Index</h1>")
>         f.write(f"<div class='muted'>Generated: {html.escape(datetime.now().isoformat(timespec='seconds'))}</div>")
>         f.write(f"<div class='muted'>Roots scanned: {html.escape(' | '.join(roots))}</div>")
>         f.write(f"<div class='muted'>Min size: {min_bytes:,} bytes</div>")
>         f.write(f"<div class='muted'>Filter audit: <code>{html.escape(json.dumps(filter_audit, ensure_ascii=False))}</code></div>")
>         f.write("<hr>")
> 
>         f.write("<table><thead><tr>")
>         f.write("<th>Count</th><th>Total Size (GB)</th><th>Folder</th><th>Largest File</th><th>Sample Files</th><th>Top Extensions</th>")
>         f.write("</tr></thead><tbody>")
> 
>         for folder in folders_sorted:
>             folder_url = file_url_from_path(folder)
>             size_gb = folder_sizes[folder] / (1024 * 1024 * 1024)
>             exts_sorted = sorted(folder_exts[folder].items(), key=lambda kv: kv[1], reverse=True)
>             top_exts = " ".join([f"{k}:{v}" for k, v in exts_sorted[:10]])
> 
>             largest_path, largest_size = folder_largest[folder]
>             largest_link = file_url_from_path(largest_path) if largest_path else ""
>             largest_label = os.path.basename(largest_path) if largest_path else ""
> 
>             samples_html = "<br>".join(
>                 f"<a href='{file_url_from_path(fp)}'>{html.escape(os.path.basename(fp))}</a>"
>                 for fp in folder_files[folder]
>             )
> 
>             f.write("<tr>")
>             f.write(f"<td>{folder_counts[folder]}</td>")
>             f.write(f"<td>{size_gb:.2f}</td>")
>             f.write(f"<td><a href='{folder_url}'>{html.escape(folder)}</a></td>")
>             f.write(f"<td><a href='{largest_link}'>{html.escape(largest_label)}</a></td>")
>             f.write(f"<td>{samples_html}</td>")
>             f.write(f"<td>{html.escape(top_exts)}</td>")
>             f.write("</tr>")
> 
>         f.write("</tbody></table></body></html>")
> 
> def write_folder_csv(out_csv, stats):
>     (folder_counts, folder_sizes, folder_exts, folder_files, folder_largest, folders_sorted) = stats
> 
>     with open(out_csv, "w", newline="", encoding="utf-8") as f:
>         w = csv.writer(f)
>         w.writerow(["count", "total_bytes", "folder_path", "folder_link", "largest_file_link", "sample_file_links", "top_extensions"])
>         for folder in folders_sorted:
>             exts_sorted = sorted(folder_exts[folder].items(), key=lambda kv: kv[1], reverse=True)
>             top_exts = " ".join([f"{k}:{v}" for k, v in exts_sorted[:10]])
> 
>             largest_path, _largest_size = folder_largest[folder]
>             largest_link = file_url_from_path(largest_path) if largest_path else ""
> 
>             sample_links = " | ".join(file_url_from_path(fp) for fp in folder_files[folder])
> 
>             w.writerow([
>                 folder_counts[folder],
>                 folder_sizes[folder],
>                 folder,
>                 file_url_from_path(folder),
>                 largest_link,
>                 sample_links,
>                 top_exts
>             ])
> 
> def write_duplicates_reports(conn, run_id, out_dupes_csv, out_restore_csv):
>     """
>     Uses sha256 to identify true duplicates among candidate groups.
>     Marks recycle-bin-only groups as restore candidates.
>     """
>     cur = conn.cursor()
> 
>     # All rows with sha256 set, grouped by sha256 having >1 member
>     cur.execute("""
>         SELECT sha256, COUNT(*) as c
>         FROM files
>         WHERE sha256 IS NOT NULL
>         GROUP BY sha256
>         HAVING c > 1
>         ORDER BY c DESC
>     """)
>     groups = cur.fetchall()
> 
>     with open(out_dupes_csv, "w", newline="", encoding="utf-8") as fdu:
>         w = csv.writer(fdu)
>         w.writerow(["sha256", "count", "has_non_recycle", "path", "in_recycle", "size", "mtime", "file_link"])
>         for (sha, c) in groups:
>             cur.execute("""
>                 SELECT path, in_recycle, size, mtime
>                 FROM files
>                 WHERE sha256 = ?
>                 ORDER BY in_recycle ASC, size DESC
>             """, (sha,))
>             members = cur.fetchall()
>             has_non_recycle = any(m[1] == 0 for m in members)
> 
>             for path, in_rec, size, mtime in members:
>                 w.writerow([
>                     sha,
>                     c,
>                     1 if has_non_recycle else 0,
>                     path,
>                     in_rec,
>                     size,
>                     mtime,
>                     file_url_from_path(path)
>                 ])
> 
>     # Restore candidates = duplicates groups are not required here;
>     # you asked: "if it's in recycle bin AND it has NO duplicate outside, restore later"
>     # That's simply: sha256 groups where ALL members are in recycle, OR single files only in recycle (no dup) — but your statement was about duplicates.
>     # We'll implement: any sha256 group (including singletons) with ONLY recycle members -> restore candidates.
>     # For singletons, sha256 still exists; we need those too. So:
>     cur.execute("""
>         SELECT sha256
>         FROM files
>         WHERE sha256 IS NOT NULL
>         GROUP BY sha256
>         HAVING SUM(CASE WHEN in_recycle=0 THEN 1 ELSE 0 END) = 0
>     """)
>     recycle_only_hashes = [r[0] for r in cur.fetchall()]
> 
>     with open(out_restore_csv, "w", newline="", encoding="utf-8") as fr:
>         w = csv.writer(fr)
>         w.writerow(["sha256", "path", "size", "mtime", "file_link"])
>         for sha in recycle_only_hashes:
>             cur.execute("""
>                 SELECT path, size, mtime
>                 FROM files
>                 WHERE sha256 = ?
>                 ORDER BY size DESC
>             """, (sha,))
>             for path, size, mtime in cur.fetchall():
>                 w.writerow([sha, path, size, mtime, file_url_from_path(path)])
> 
> # -----------------------------
> # MAIN
> # -----------------------------
> 
> def main():
>     roots_all = discover_existing_roots(DEFAULT_ROOTS)
>     if not roots_all:
>         print("No valid roots found. Edit DEFAULT_ROOTS in the script.")
>         sys.exit(1)
> 
>     scan_global = prompt_yes_no("Scan GLOBAL (all roots listed)?", default_yes=True)
>     roots = roots_all if scan_global else choose_roots(roots_all)
> 
>     name_filter, filter_audit = build_name_filter()
> 
>     # SQLite init
>     conn = db_connect()
>     db_init(conn)
>     run_id = db_start_run(conn, roots, MIN_BYTES, filter_audit)
> 
>     print("\nScanning roots:")
>     for r in roots:
>         print(" -", r)
>     print(f"Extensions: {', '.join(sorted(VIDEO_EXTS))}")
>     print(f"Minimum size: {MIN_BYTES:,} bytes ({MIN_BYTES / (1024*1024):.1f} MB)")
>     print(f"DB: {DB_PATH}")
>     print(f"Checkpoint: prompt every ~{CHECKPOINT_GB} GB of matched video")
>     print("")
> 
>     total_files = 0
>     matched_files = 0
>     skipped_by_name = 0
>     skipped_by_size = 0
>     skipped_by_ext = 0
>     ext_seen = defaultdict(int)
>     rejected_samples = []
> 
>     matched_bytes = 0
>     next_checkpoint = CHECKPOINT_BYTES
> 
>     start = time.time()
>     last_print = start
>     dirs_seen = 0
> 
>     try:
>         for root in roots:
>             for dirpath, filenames in safe_walk(root):
>                 dirs_seen += 1
>                 now = time.time()
>                 if now - last_print >= 2:
>                     print(f"[scan] dirs:{dirs_seen:,} files:{total_files:,} matches:{matched_files:,} now:{dirpath}", flush=True)
>                     last_print = now
> 
>                 for fname in filenames:
>                     total_files += 1
>                     ext = os.path.splitext(fname)[1].lower()
>                     ext_seen[ext] += 1
> 
>                     if ext not in VIDEO_EXTS:
>                         skipped_by_ext += 1
>                         continue
> 
>                     if not name_filter(fname):
>                         skipped_by_name += 1
>                         if len(rejected_samples) < 25:
>                             rejected_samples.append(os.path.join(dirpath, fname))
>                         continue
> 
>                     fullpath = os.path.join(dirpath, fname)
>                     try:
>                         st = os.stat(fullpath)
>                         size = st.st_size
>                         mtime = int(st.st_mtime)
>                     except OSError:
>                         continue
> 
>                     if size < MIN_BYTES:
>                         skipped_by_size += 1
>                         if len(rejected_samples) < 25:
>                             rejected_samples.append(fullpath + f" (size={size})")
>                         continue
> 
>                     in_rec = is_recycle_bin(fullpath.lower())
> 
>                     matched_files += 1
>                     matched_bytes += size
> 
>                     db_upsert_file(conn, fullpath, dirpath, ext, size, mtime, in_rec, run_id)
> 
>                     # Batch commit for speed
>                     if matched_files % 5000 == 0:
>                         conn.commit()
> 
>                     # Checkpoint prompt
>                     if matched_bytes >= next_checkpoint:
>                         conn.commit()
>                         print(f"\n[checkpoint] Matched ~{matched_bytes / (1024**3):.1f} GB so far.")
>                         cont = prompt_yes_no("Continue scanning?", default_yes=True)
>                         if not cont:
>                             raise KeyboardInterrupt()
>                         next_checkpoint += CHECKPOINT_BYTES
> 
>         conn.commit()
> 
>     except KeyboardInterrupt:
>         conn.commit()
>         print("\nStopped early. Inventory saved to SQLite. You can re-run and choose dedupe without rescanning.\n")
> 
>     # Post-scan summary
>     print("\n[scan summary]")
>     print(f"  total_files_seen: {total_files:,}")
>     print(f"  matched_files:    {matched_files:,}")
>     print(f"  matched_gb:       {matched_bytes / (1024**3):.2f}")
>     print(f"  skipped_by_name:  {skipped_by_name:,}")
>     print(f"  skipped_by_size:  {skipped_by_size:,}")
>     print(f"  skipped_by_ext:   {skipped_by_ext:,}")
>     top_exts = sorted(ext_seen.items(), key=lambda kv: kv[1], reverse=True)[:10]
>     print("  top_extensions_seen:", dict(top_exts))
>     if rejected_samples:
>         print("\n[rejected samples] (first 25)")
>         for s in rejected_samples[:25]:
>             print("  -", s)
> 
>     # Ask: run dedupe now?
>     run_dedupe = prompt_yes_no("\nRun duplicate detection (hashing) now?", default_yes=True)
> 
>     if run_dedupe:
>         print("\n[dedupe] Selecting candidate groups by (size, ext) ...")
> 
>         cur = conn.cursor()
>         cur.execute("""
>             SELECT size, ext, COUNT(*) as c
>             FROM files
>             WHERE size >= ?
>             GROUP BY size, ext
>             HAVING c > 1
>             ORDER BY c DESC
>         """, (MIN_BYTES,))
>         candidates = cur.fetchall()
>         print(f"[dedupe] Candidate groups: {len(candidates):,}")
> 
>         # Step 1: quick hash candidates
>         to_quick = []
>         for size, ext, c in candidates:
>             cur.execute("SELECT path FROM files WHERE size=? AND ext=?", (size, ext))
>             to_quick.extend([r[0] for r in cur.fetchall()])
> 
>         print(f"[dedupe] Files to quick-hash: {len(to_quick):,} (workers={HASH_WORKERS})")
> 
>         def quick_job(p):
>             try:
>                 return p, quick_hash_file(p)
>             except Exception:
>                 return p, None
> 
>         with ThreadPoolExecutor(max_workers=HASH_WORKERS) as ex:
>             futures = [ex.submit(quick_job, p) for p in to_quick]
>             done = 0
>             for fut in as_completed(futures):
>                 path, qh = fut.result()
>                 done += 1
>                 if qh:
>                     conn.execute("UPDATE files SET quick_hash=? WHERE path=?", (qh, path))
>                 if done % 200 == 0:
>                     conn.commit()
>                     print(f"[dedupe] quick-hash {done:,}/{len(to_quick):,}", flush=True)
>             conn.commit()
> 
>         # Step 2: full hash only for quick-hash collisions
>         cur.execute("""
>             SELECT quick_hash, COUNT(*) as c
>             FROM files
>             WHERE quick_hash IS NOT NULL
>             GROUP BY quick_hash
>             HAVING c > 1
>             ORDER BY c DESC
>         """)
>         qh_groups = cur.fetchall()
>         print(f"[dedupe] Quick-hash collision groups: {len(qh_groups):,}")
> 
>         to_full = []
>         for qh, c in qh_groups:
>             cur.execute("SELECT path FROM files WHERE quick_hash=?", (qh,))
>             to_full.extend([r[0] for r in cur.fetchall()])
> 
>         print(f"[dedupe] Files to full-hash (sha256): {len(to_full):,} (workers={HASH_WORKERS})")
> 
>         def full_job(p):
>             try:
>                 return p, sha256_file(p)
>             except Exception:
>                 return p, None
> 
>         with ThreadPoolExecutor(max_workers=HASH_WORKERS) as ex:
>             futures = [ex.submit(full_job, p) for p in to_full]
>             done = 0
>             for fut in as_completed(futures):
>                 path, sh = fut.result()
>                 done += 1
>                 if sh:
>                     conn.execute("UPDATE files SET sha256=? WHERE path=?", (sh, path))
>                 if done % 100 == 0:
>                     conn.commit()
>                     print(f"[dedupe] sha256 {done:,}/{len(to_full):,}", flush=True)
>             conn.commit()
> 
>         print("[dedupe] Done hashing.")
> 
>     # Build reports from SQLite (inventory)
>     cur = conn.cursor()
>     cur.execute("""
>         SELECT path, folder, ext, size, in_recycle
>         FROM files
>         WHERE seen_in_run = ?
>         ORDER BY folder
>     """, (run_id,))
>     file_rows = cur.fetchall()
> 
>     stats = build_folder_summaries(file_rows)
> 
>     ts = datetime.now().strftime("%Y%m%d_%H%M%S")
>     out_folder_csv = os.path.join(SCRIPT_DIR, f"video_folders_{ts}.csv")
>     out_folder_html = os.path.join(SCRIPT_DIR, f"video_folders_{ts}.html")
> 
>     write_folder_csv(out_folder_csv, stats)
>     write_folder_html(out_folder_html, roots, stats, filter_audit, MIN_BYTES)
> 
>     print("\nReports:")
>     print("  Folder CSV :", out_folder_csv)
>     print("  Folder HTML:", out_folder_html)
> 
>     # If dedupe ran, output duplicate reports
>     cur = conn.cursor()
>     cur.execute("SELECT COUNT(*) FROM files WHERE sha256 IS NOT NULL")
>     hashed_count = cur.fetchone()[0]
> 
>     if hashed_count > 0:
>         out_dupes_csv = os.path.join(SCRIPT_DIR, f"duplicates_{ts}.csv")
>         out_restore_csv = os.path.join(SCRIPT_DIR, f"restore_candidates_recycle_only_{ts}.csv")
>         write_duplicates_reports(conn, run_id, out_dupes_csv, out_restore_csv)
>         print("  Duplicates CSV:", out_dupes_csv)
>         print("  Restore CSV  :", out_restore_csv)
> 
>     conn.close()
>     print("\nDone.")
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ---
> 
> ## What changed vs your current code (the value-add list)
> 
> ### Fixed / improved
> - **EXCLUDE_SEGMENTS bug**: changed from `\\` matching to correct `\` matching.
> - **Recycle Bin included**: not excluded; files are tagged `in_recycle`.
> - **Fuzzy filters are provably OR** and audit prints correctly (your audit block was unreachable due to indentation under `matches()`).
> - **Reports now include actual file links**:
>   - Folder link
>   - Largest file link
>   - First 10 sample file links
> 
> ### Optimization that matters
> - **Batch commits** every 5,000 matches (massive speedup vs commit per file).
> - **WAL mode** + cache tweaks for SQLite.
> - **Hashing uses 4 threads** and only hashes candidate duplicates (same `(size, ext)`).
> - **Checkpoint prompt** every ~10GB matched so you can stop and still keep the DB.
> 
> ---
> 
> ## How to run
> From the folder containing the script:
> 
> ```bash
> python video_finder_sqlite.py
> ```
> 
> Outputs:
> - `video_index.sqlite3` (your persistent inventory)
> - `video_folders_*.html` and `.csv`
> - If you run hashing:
>   - `duplicates_*.csv`
>   - `restore_candidates_recycle_only_*.csv`
> 
> ---
> 
> ## Next (optional but smart)
> If you want, I can add a **“skip rescan if nothing changed” mode** using:
> - root snapshot table: last scan time + file counts
> - or a fast “mtime window” scan
> But in practice, SQLite + “stop anytime” makes rescans rare.
> 
> If you run this once and paste:
> - the `[scan summary]`
> - the count of candidate groups it reports
> I’ll tell you whether 1MB threshold or ext list should be adjusted for your data.

### User
> for all your excluded segments it says = Strin literal is unterminated

### Assistant
> That error is because I gave you **raw strings that end with a single backslash**:
> 
> ```python
> r"\windows\"
> ```
> 
> In Python, a raw string **cannot end with a single `\`** — it escapes the closing quote, so you get **“String literal is unterminated.”**
> 
> ### Fix (do this): don’t end segments with `\`
> Use raw strings **without the trailing backslash**, and in your matcher add the backslashes.
> 
> #### Replace your `EXCLUDE_SEGMENTS` with this (safe):
> ```python
> EXCLUDE_SEGMENTS = {
>     r"\windows",
>     r"\windows.old",
>     r"\program files",
>     r"\program files (x86)",
>     r"\programdata",
>     r"\appdata",
>     r"\system volume information",
>     r"\recovery",
>     r"\winsxs",
>     # optional noisy tool temp (leave off unless you want it)
>     # r"\.videoconverter\temp_source",
> }
> ```
> 
> #### And update `is_excluded_path()` to match segments cleanly:
> ```python
> def is_excluded_path(path_lower: str) -> bool:
>     p = norm_path_lower(path_lower)
>     return any((seg + "\\") in p for seg in EXCLUDE_SEGMENTS)
> ```
> 
> That’s it. No unterminated strings, and the matching works.
> 
> ---
> 
> ### Important note: you said “include recycle bin”
> So do **NOT** put `\$recycle.bin` in `EXCLUDE_SEGMENTS`. Keep it out and just tag it with `is_recycle_bin()` like we already do.
> 
> ---
> 
> If you want the fastest sanity check: paste your current `EXCLUDE_SEGMENTS` block after you edit it and I’ll confirm it’s syntactically valid and does what you intend.

### User
> for def is recycle bin says the same string literal is unterminated

### Assistant
> Same root cause. You’re hitting **the same Python rule twice**.
> 
> > **Rule (non-negotiable):**  
> > A Python raw string **cannot end with a single backslash**.  
> > This is true **everywhere** — variables, functions, regex, helpers.
> 
> You fixed it in `EXCLUDE_SEGMENTS`, but the **same mistake exists in `is_recycle_bin()`**.
> 
> ---
> 
> ## What’s wrong (exactly)
> 
> You currently have something like:
> 
> ```python
> def is_recycle_bin(path_lower: str) -> bool:
>     return r"\$recycle.bin\" in norm_path_lower(path_lower)
> ```
> 
> That trailing `\` **escapes the quote**, so Python throws:
> 
> > `String literal is unterminated`
> 
> ---
> 
> ## ✅ Correct, safe version (DO THIS)
> 
> ### Option A — Raw string, no trailing slash (recommended)
> 
> ```python
> def is_recycle_bin(path_lower: str) -> bool:
>     p = norm_path_lower(path_lower)
>     return r"\$recycle.bin" in p
> ```
> 
> This works because:
> - `norm_path_lower()` already ensures a trailing `\`
> - We don’t need to match the final slash explicitly
> 
> ---
> 
> ### Option B — Normal string with escaped backslash (also valid)
> 
> ```python
> def is_recycle_bin(path_lower: str) -> bool:
>     p = norm_path_lower(path_lower)
>     return "\\$recycle.bin\\" in p
> ```
> 
> Either is correct. **Option A is cleaner**.
> 
> ---
> 
> ## Final canonical pattern (remember this)
> 
> ### ❌ NEVER do this
> ```python
> r"\something\"
> ```
> 
> ### ✅ Do one of these instead
> ```python
> r"\something"
> "\\something\\"
> ```
> 
> ---
> 
> ## Why this keeps biting people
> Raw strings are often misunderstood. They’re great for regex and Windows paths **until** you end them with `\`. Python can’t guess your intent — it just errors.
> 
> ---
> 
> ## Quick checklist before you run again
> 
> Make sure **none** of these exist anywhere in the file:
> 
> - `r"...\"`
> - `r'\...'`
> - any raw string ending in `\`
> 
> Search for:
> ```
> r"
> ```
> and eyeball the endings.
> 
> ---
> 
> Once you fix `is_recycle_bin()` as above, the script will **start cleanly**, and the SQLite + dedupe logic will work as intended.
> 
> If you want, paste **both** helper functions (`is_excluded_path` + `is_recycle_bin`) and I’ll sanity-check them together so this doesn’t come back again.

### User
> ok i got the 25 bideos back and it asked me if i want to dedup now or no, but non of the videos on the list match but they do say rejected sample no should i say no

### Assistant
> Short, direct answer: **say NO.**
> 
> Here’s why — and this matters.
> 
> ---
> 
> ## What you’re seeing is correct behavior
> 
> - You got **25 videos indexed**
> - It shows **“rejected samples: none”**
> - The script asks: *“Run dedupe now?”*
> 
> That tells us:
> 
> 1. **Your filters are working** (nothing unexpected slipped through)
> 2. **There are no obvious same-size candidates yet**
> 3. Running dedupe **right now gives you almost no value**
> 
> Remember: dedupe only does meaningful work when there are **multiple files with the same size + extension**. With only ~25 files, and you already eyeballed that they don’t match, hashing is just burning I/O for nothing.
> 
> So yes — **say NO**.
> 
> ---
> 
> ## What saying NO actually does (important)
> 
> Saying **NO**:
> - Keeps the **SQLite inventory**
> - Does **not** discard anything
> - Lets you:
>   - Adjust filters
>   - Scan more folders
>   - Resume later
> - Avoids unnecessary hashing
> 
> You are *not* losing progress.
> 
> ---
> 
> ## When you SHOULD say YES to dedupe
> 
> Say **YES** when **at least one** of these is true:
> 
> - You see **multiple folders** with suspiciously similar counts/sizes
> - You scanned **hundreds or thousands** of files
> - You expect:
>   - Drive copies vs USB copies
>   - Converter outputs vs originals
>   - Backup mirrors
> - The scan summary shows:
>   - Many files with identical sizes
>   - Large candidate groups
> 
> That’s when hashing pays off.
> 
> ---
> 
> ## What I recommend next (in order)
> 
> ### 1️⃣ Expand the scan slightly
> Run again and:
> - Keep the same filters
> - Add **one more root** (e.g., the Drive path or another USB)
> - Stop at the **first 10–20 GB checkpoint**
> 
> This builds a meaningful inventory without locking you in.
> 
> ### 2️⃣ Review the HTML report
> Look for:
> - Same folder names across different roots
> - Same project names in `_converter`, `_backup`, `_working`, etc.
> - Similar total sizes
> 
> ### 3️⃣ THEN run dedupe
> At that point:
> - The size-based prefilter will find real candidates
> - Quick-hash will prune fast
> - Full hash will only run where it matters
> 
> ---
> 
> ## One subtle but important signal you mentioned
> 
> > “they do say rejected sample no”
> 
> That’s actually a **green flag**:
> - It means your name filter isn’t accidentally throwing away good files
> - You’re not over-filtering
> - The result set is clean
> 
> If you had seen **lots of rejected samples**, we’d tune filters first. You didn’t need that.
> 
> ---
> 
> ### Bottom line
> **Say NO.**  
> You’re in the *inventory-building* phase, not the *dedupe* phase yet.
> 
> When you’re ready, tell me:
> - how many total files you’ve indexed
> - how many roots you’ve scanned
> 
> I’ll tell you exactly when dedupe flips from “waste of time” to “high ROI.”

### User
> heres waht happened. and it was fast to but i dont know if it worked right. PS C:\QiOS_WORKING\My Drive\_working\VIDEO-FINDER> python video_finder_sqllite.py

> Scan GLOBAL (all roots listed)? (Y/n): n

> 

> Available roots:

>   1) C:\

>   2) C:\QiOS_WORKING\My Drive

>   3) D:\

> 

> Enter comma-separated numbers to scan (example: 2,3). Press Enter for ALL.

> Selection: 3

> Do you want to enable filename fuzzy filters? (y/N): y

> 

> Filename fuzzy filters available:

>   1) Contains 'T' anywhere

>   2) Contains 'TT' (two or more T's in a row)

>   3) Contains 646 OR '6 4 6' (digits separated by anything)

>   4) Custom 'contains' terms (you type them)

> Filter: match 'T' anywhere in filename? (y/N): n

> Filter: match 'TT' (T repeated 2+ times) in filename? (y/N): y

> Filter: match 646 / 6 4 6 pattern in filename? (y/N): y

> Add custom 'contains' terms? (y/N): y

> Enter terms separated by commas (example: court, hallway, cam2): treve, trevesin, tre

> 

> [filter audit] {"enabled": true, "use_contains_T": false, "use_T_repeat": true, "use_646": true, "custom_terms": ["treve", "trevesin", "tre"], "logic": "OR"}

> 

> Scanning roots:

>  - D:\

> Extensions: .avi, .m4v, .media, .mkv, .mov, .mp4, .mpeg, .mpg, .wmv

> Minimum size: 1,048,576 bytes (1.0 MB)

> DB: C:\QiOS_WORKING\My Drive\_working\VIDEO-FINDER\video_index.sqlite3

> Checkpoint: prompt every ~10 GB of matched video

> 

> 

> [scan summary]

>   total_files_seen: 16,129

>   matched_files:    1

>   matched_gb:       0.00

>   skipped_by_name:  8,654

>   skipped_by_size:  32

>   skipped_by_ext:   7,442

>   top_extensions_seen: {'.media': 7959, '.md': 2485, '': 925, '.pdf': 684, '.html': 486, '.mp4': 453, '.json': 290, '.csv': 286, '.jpg': 265, '.jpeg': 250}

> 

> [rejected samples] (first 25)

>   - D:\QiOS_BACKUP\sites\qially-com-v2.0\images\video-logo.mp4

>   - D:\QiOS_BACKUP\realms\qiclients\c.zjk\zjkintrovideo_3.mp4

>   - D:\QiOS_BACKUP\realms\qiclients\c.hee\Solving_Back_Taxes__Case_Study.mp4

>   - D:\QiOS_BACKUP\realms\qivault\ideas\childhooddream.mp4

>   - D:\QiOS_BACKUP\realms\qivault\ideas\projects (2).mp4

>   - D:\QiOS_BACKUP\realms\qivault\ideas\projects (3).mp4

>   - D:\QiOS_BACKUP\realms\qivault\ideas\projects (4).mp4

>   - D:\QiOS_BACKUP\realms\qivault\ideas\projects.mp4

>   - D:\QiOS_BACKUP\apps\QiBP\public\introvideo.mp4

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\ace-esteban\ace-esteban_2025-08-20_01.mp4

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\ace-esteban\fabian.mp4

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\ace-esteban\ace-esteban_2025-08-20_02.mp4

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\ace-esteban\julianfb.mp4

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\ace-esteban\ace-esteban_2025-08-20_01.mkv

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\ace-esteban\ace-esteban_2025-08-20_02.mkv

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\alfredo-suarez\20-32-28_2m.mkv

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\alfredo-suarez\20-31-48_2m.mkv

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\alfredo-suarez\20-35-28_2m.mkv

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\alfredo-suarez\20-33-08_2m.mkv

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\alfredo-suarez\20-36-01_2m.mkv

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\alfredo-suarez\20-33-40_2m.mkv

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\alfredo-suarez\20-37-25_2m.mkv

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\alfredo-suarez\20-38-07_2m.mkv

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\alfredo-suarez\20-41-37_2m.mkv

>   - D:\QiOS_BACKUP\apps\_converter\01_projects\alfredo-suarez\20-38-41_2m.mkv

> 

> Run duplicate detection (hashing) now? (Y/n): n

> 

> Reports:

>   Folder CSV : C:\QiOS_WORKING\My Drive\_working\VIDEO-FINDER\video_folders_20251230_045331.csv

>   Folder HTML: C:\QiOS_WORKING\My Drive\_working\VIDEO-FINDER\video_folders_20251230_045331.html

> 

> Done.

> PS C:\QiOS_WORKING\My Drive\_working\VIDEO-FINDER>

### Assistant
> It worked exactly as coded — but your **filters are so tight that you effectively told it to return almost nothing**.
> 
> ### What the run proves (no guessing)
> 
> - You scanned **D:\** and saw **16,129 files** total. That’s plausible/fast.
> - It found **453 .mp4 files** on D:\ (see `top_extensions_seen`), so there are videos there.
> - It returned **matched_files: 1** because:
>   - **skipped_by_name: 8,654** — your filename filter rejected the overwhelming majority of candidates.
>   - Your filter audit shows **OR logic**, but the rules you enabled are *rare*:
>     - `TT` (two T’s in a row)
>     - `646` pattern
>     - contains `treve` / `trevesin` / `tre`
> 
> Most filenames (like `introvideo.mp4`, `projects.mp4`, etc.) won’t match any of those, so they get rejected.
> 
> ### Why “rejected samples” shows MP4s
> Those are examples of files that:
> - passed extension (.mp4/.mkv)
> - passed size (mostly)
> - but **failed your name filter**  
> So “rejected” here means “rejected by name”, not “bad file”.
> 
> That is actually good debugging output.
> 
> ---
> 
> ## Did you do the right thing saying “no” to dedupe?
> Yes. With **1 matched file**, dedupe is pointless. Dedupe needs at least *some* volume.
> 
> ---
> 
> ## The real issue: your filter settings don’t match your intention
> You said you wanted to find scattered videos; then you enabled filters that only find:
> - files with `TT` **or**
> - files with `646` **or**
> - files containing `treve/trevesin/tre`
> 
> That’s basically “needle finder,” not “inventory finder.”
> 
> If your goal is “show me where my videos live,” do this instead:
> 
> ### Option A (recommended): first run with NO name filters
> - Enable fuzzy filters: **No**
> - Keep MIN_BYTES at 1MB
> This produces a full folder map of where videos are.
> 
> ### Option B: use ONLY custom terms (don’t stack weird rules)
> - Contains T: **n**
> - TT: **n**
> - 646: **n**
> - Custom terms: **treve, trevesin, chicano, hallway, cam2, driveway**
> This targets your relevant sets without excluding everything else.
> 
> ### Option C: keep OR, but add a “match-all if zero rules” safeguard
> Already included in my script; you’re fine there.
> 
> ---
> 
> ## One improvement you should make immediately (high value)
> Right now you’re filtering on **fname** only, not full path. That’s why your custom term `tre` is too broad and also why you can’t filter by folder names like `treve\treve-01`.
> 
> ### Change this line:
> ```python
> if not name_filter(fname):
> ```
> to:
> ```python
> if not name_filter(fullpath):
> ```
> 
> And inside `matches()` change:
> ```python
> base = os.path.basename(name)
> b = base.lower()
> ```
> to:
> ```python
> b = name.lower()  # match against full path
> ```
> 
> Then your custom terms will match folder names too, not just the file name. That’s what you actually want for “Treve” sets.
> 
> ---
> 
> ## Quick next move (do this now)
> Run again with D:\ only:
> 
> 1) **Disable fuzzy filters** entirely (answer `n`)
> 2) Let it scan
> 3) Open the HTML report and look at the top folders (you’ll immediately see where your real video clusters are)
> 4) Then rerun with targeted custom terms if you want.
> 
> If you do want a “don’t lock me in” workflow, keep your checkpoint at 10GB — but your D:\ scan is small enough that it won’t matter much.
> 
> ---
> 
> ## Sanity check: why so many `.media` files?
> `top_extensions_seen` shows `.media: 7959`. That’s a lot. Two possibilities:
> - You genuinely have thousands of `.media` video files (possible if it’s a camera export format)
> - Or `.media` is used by some app for non-video blobs
> 
> If you want, we can add a **content sniff** heuristic:
> - for `.media` files only, read first 16 bytes and look for common video signatures (MP4 `ftyp`, MKV EBML, etc.)
> That would cut junk without excluding real videos.
> 
> ---
> 
> If you want me to be surgical: paste the **one matched file path** from the HTML (or the DB query), and tell me whether you were trying to find “Treve” stuff specifically or build a general inventory. Then I’ll give you the exact filter presets to use.

### User
> yes, and no, right now my goal is to find any videos of this person and i would name the files somethign like treve, trevesin, 646, or 6464 or tre, or tttttt, or tt, or tttt or hhhh or  grrrrr, or chicano or thug, or trev or some combination that is no necesarily obvious there may be some with the name only on the folder but the containing videos are not renamed yet.

### Assistant
> Understood. Your intent is **person-hunt**, not “index everything.” You need two concrete upgrades:
> 
> 1) **Match against the full path** (so folder names count).  
> 2) Expand the fuzzy patterns to cover your naming style (`tre*`, `tttt`, `hhhh`, `grrrrr`, `6464`, etc.) using **OR**.
> 
> Below is the exact, minimal set of changes to make that work reliably.
> 
> ---
> 
> ## 1) Change the filter to evaluate the FULL PATH (not just filename)
> 
> ### In the scan loop, replace:
> ```python
> if not name_filter(fname):
> ```
> with:
> ```python
> if not name_filter(fullpath):
> ```
> 
> This single change is huge: it allows matches where only the **folder** contains “treve” and the files inside are generic names like `IMG_001.mp4`.
> 
> ---
> 
> ## 2) Replace your current `build_name_filter()` with a pattern-driven OR filter
> 
> This version supports:
> - `tre`, `trev`, `treve`, `trevesin` (anywhere in path)
> - `chicano`, `thug`
> - `646`, `6464`, and “6 4 6” separated by anything
> - repeated-letter bursts like:
>   - `tt`, `tttt`, `tttttt`
>   - `hhhh`, `grrrr`, etc.
> 
> ### Drop-in replacement for `build_name_filter()`:
> 
> ```python
> def build_name_filter():
>     use_filters = prompt_yes_no("Do you want to enable filename/path fuzzy filters?", default_yes=True)
>     if not use_filters:
>         audit = {"enabled": False, "logic": None}
>         print("\n[filter audit] " + json.dumps(audit))
>         return (lambda _s: True), audit
> 
>     # Core tokens you expect (match anywhere in FULL PATH)
>     raw = input(
>         "Enter custom terms separated by commas (example: treve, trevesin, 646, chicano, thug): "
>     ).strip()
>     custom_terms = [t.strip().lower() for t in raw.split(",") if t.strip()]
> 
>     # Optional: repeated-letter patterns (tttt, hhhh, grrrrr, etc.)
>     use_repeats = prompt_yes_no("Enable repeated-letter pattern matching (tt, tttt, hhhh, grrrrr)?", default_yes=True)
> 
>     # Optional: numeric “646” family matching (646, 6_4_6, 6464)
>     use_646_family = prompt_yes_no("Enable 646-family matching (646, 6-4-6, 6464)?", default_yes=True)
> 
>     # Build regexes
>     # - repeats: any letter repeated 2+ times (focus catches tttt, hhhh, grrrrr)
>     re_repeat_any = re.compile(r"([a-z])\1{1,}", re.IGNORECASE) if use_repeats else None
> 
>     # - 646 patterns: 646 with junk between digits, and 6464 specifically
>     re_646 = re.compile(r"6\D*4\D*6") if use_646_family else None
>     re_6464 = re.compile(r"6\D*4\D*6\D*4") if use_646_family else None
> 
>     def matches(full_path: str) -> bool:
>         s = full_path.lower()
> 
>         rules = []
> 
>         # custom terms (substring OR)
>         if custom_terms:
>             rules.append(any(term in s for term in custom_terms))
> 
>         # repeated letters anywhere (OR)
>         if re_repeat_any is not None:
>             rules.append(re_repeat_any.search(s) is not None)
> 
>         # 646 family (OR)
>         if re_646 is not None:
>             rules.append(re_646.search(s) is not None)
>         if re_6464 is not None:
>             rules.append(re_6464.search(s) is not None)
> 
>         # OR logic: match if ANY rule true.
>         # If user entered nothing and disabled options, match-all.
>         return any(rules) if rules else True
> 
>     audit = {
>         "enabled": True,
>         "custom_terms": custom_terms,
>         "use_repeats": use_repeats,
>         "use_646_family": use_646_family,
>         "logic": "OR",
>         "scope": "FULL_PATH",
>     }
>     print("\n[filter audit] " + json.dumps(audit, ensure_ascii=False))
>     return matches, audit
> ```
> 
> ### Why this is the right approach
> - You stop micromanaging individual toggles (`TT`, `T`, etc.).
> - You express intent: “match these tokens OR weird repeated-letter filenames OR 646-family.”
> - It catches:
>   - `tt.mp4`, `tttttt.mp4`, `hhhh_cam.mp4`, `grrrrrr1.mkv`
>   - folders named `treve-01/` even if files are `IMG_0001.mp4`
>   - `646`, `6_4_6`, `6-4-6`, `6464`
> 
> ---
> 
> ## 3) One more correction: your current code is accidentally too strict
> Right now you enabled both `TT` and `646` and custom terms. With OR that’s fine, but `TT` only triggers when the **filename** has consecutive T’s, which is rare. The new repeat matcher is broader and matches your actual naming behavior.
> 
> ---
> 
> ## 4) How to run for your “Treve hunt” (best preset)
> On the prompt, enter terms like:
> 
> `tre, trev, treve, trevesin, chicano, thug, 646, 6464`
> 
> Then:
> - repeats: **yes**
> - 646 family: **yes**
> 
> Scan D:\ first, then run again on Drive (root 2) if needed.
> 
> ---
> 
> ## 5) After you get a meaningful number of matches, THEN dedupe
> You’ll know you’re ready when `matched_files` is in the **hundreds+**.  
> At that point, dedupe will produce:
> - duplicates (good for cleanup)
> - recycle-only restore candidates (your “oh shit I need to restore” list)
> 
> ---
> 
> If you apply just two changes—**filter full path** + **new pattern filter**—your “Treve hunt” becomes reliable instead of random.

### User
> and it might say miguel, or manuel, or isai too. or it may have 6 4 and 6 but not together basically wi dould jumble up letters or soemtime use numbers as letters just to stregthen the security and reduce accidentally pulling up those videos

### Assistant
> You’re describing a **deliberate obfuscation scheme** (jumbled letters, leetspeak, spaced digits, etc.). The right move is to formalize this into a **single OR-based matcher** that runs against the **full path**, with three layers:
> 
> 1) **Token hits** (treve/trev/manuel/miguel/isai/etc.)  
> 2) **Leetspeak normalization** (numbers-as-letters) + token hits again  
> 3) **Flexible numeric patterns** (6…4…6, or “contains 6 and 4 and 6 anywhere,” optionally with order constraints)
> 
> This gives you high recall without accidentally indexing everything.
> 
> Below is a drop-in filter upgrade that does exactly that.
> 
> ---
> 
> ## 1) Use FULL PATH (required)
> 
> In your scan loop, make sure you call the filter with `fullpath`:
> 
> ```python
> if not name_filter(fullpath):
>     ...
> ```
> 
> Not `fname`.
> 
> ---
> 
> ## 2) Add leetspeak normalization + flexible digit logic
> 
> ### Drop-in helper functions (put near helpers)
> 
> ```python
> def normalize_leetspeak(s: str) -> str:
>     """
>     Converts common number-as-letter substitutions to letters.
>     Keeps original chars too by returning a normalized string.
>     """
>     trans = str.maketrans({
>         "0": "o",
>         "1": "i",
>         "3": "e",
>         "4": "a",   # sometimes 'a' or 'h' but a is most common
>         "5": "s",
>         "7": "t",
>         "8": "b",
>         "9": "g",
>         "@": "a",
>         "$": "s",
>     })
>     return s.translate(trans)
> 
> def has_digits_anywhere(s: str, digits: str) -> bool:
>     # e.g. digits="646" means contains 6,4,6 anywhere (count-aware)
>     counts = {d: digits.count(d) for d in set(digits)}
>     for d, c in counts.items():
>         if s.count(d) < c:
>             return False
>     return True
> ```
> 
> ---
> 
> ## 3) Replace `build_name_filter()` with an obfuscation-aware OR matcher
> 
> This one supports:
> - names: `tre, trev, treve, trevesin, miguel, manuel, isai, chicano, thug`
> - leetspeak variants: `m1gu3l`, `manu3l`, `1sa1`, `tr3v3`, etc.
> - digit patterns:
>   - strict: `6\D*4\D*6` (6 then 4 then 6 with anything between)
>   - loose: “has 6 and 4 and 6 anywhere” (order not required)
> 
> ```python
> def build_name_filter():
>     use_filters = prompt_yes_no("Enable path fuzzy filters (recommended)?", default_yes=True)
>     if not use_filters:
>         audit = {"enabled": False, "logic": None}
>         print("\n[filter audit] " + json.dumps(audit))
>         return (lambda _s: True), audit
> 
>     raw = input(
>         "Enter terms (comma-separated). Example: tre, trev, treve, trevesin, miguel, manuel, isai, chicano, thug: "
>     ).strip()
>     terms = [t.strip().lower() for t in raw.split(",") if t.strip()]
> 
>     enable_leet = prompt_yes_no("Enable leetspeak normalization (e.g., m1gu3l, tr3v3)?", default_yes=True)
>     enable_repeats = prompt_yes_no("Enable repeated-letter detection (tttt, hhhh, grrrrr)?", default_yes=True)
> 
>     enable_646_strict = prompt_yes_no("Enable strict 6-4-6 pattern (6...4...6)?", default_yes=True)
>     enable_646_loose = prompt_yes_no("Enable loose 6/4/6 presence (6 and 4 and 6 anywhere)?", default_yes=True)
> 
>     # Regexes
>     re_repeat_any = re.compile(r"([a-z])\1{1,}", re.IGNORECASE) if enable_repeats else None
>     re_646_strict = re.compile(r"6\D*4\D*6") if enable_646_strict else None
> 
>     def matches(full_path: str) -> bool:
>         s = full_path.lower()
> 
>         # Layer 1: direct term hits
>         rules = []
>         if terms:
>             rules.append(any(t in s for t in terms))
> 
>         # Layer 2: leetspeak normalized term hits
>         if enable_leet and terms:
>             s_leet = normalize_leetspeak(s)
>             rules.append(any(t in s_leet for t in terms))
> 
>         # Layer 3: repeats (tttt, hhhh, grrrrr, etc.)
>         if re_repeat_any is not None:
>             rules.append(re_repeat_any.search(s) is not None)
> 
>         # Layer 4: numeric obfuscation
>         if re_646_strict is not None:
>             rules.append(re_646_strict.search(s) is not None)
>         if enable_646_loose:
>             # requires at least two '6' and one '4' anywhere
>             rules.append(has_digits_anywhere(s, "646"))
> 
>         # OR logic
>         return any(rules) if rules else True
> 
>     audit = {
>         "enabled": True,
>         "terms": terms,
>         "enable_leetspeak": enable_leet,
>         "enable_repeats": enable_repeats,
>         "enable_646_strict": enable_646_strict,
>         "enable_646_loose": enable_646_loose,
>         "logic": "OR",
>         "scope": "FULL_PATH",
>     }
>     print("\n[filter audit] " + json.dumps(audit, ensure_ascii=False))
>     return matches, audit
> ```
> 
> ---
> 
> ## 4) Practical guidance: don’t over-broaden with “tre”
> “tre” is extremely broad (it will match “street”, “tree”, “tremor”…). Since you’re using folder names too, it can explode matches.
> 
> Better term list:
> 
> - `trev, treve, trevesin` (skip plain `tre` unless you need max recall)
> - `miguel, manuel, isai`
> - `chicano, thug`
> - plus numeric: `646, 6464` (optional; digits are already handled)
> 
> If you must keep `tre`, keep it but understand you’ll get noise.
> 
> ---
> 
> ## 5) Your “security-strengthening” idea (numbers as letters)
> Leetspeak normalization handles the most common. If you’re doing more creative swaps (like `6 = g` sometimes), we can add alternate mappings. But don’t go too far or you’ll increase false positives.
> 
> ---
> 
> ## Recommended next run (so you can trust results)
> - Scan **D:\**
> - Terms: `trev, treve, trevesin, miguel, manuel, isai, chicano, thug`
> - Leetspeak: **yes**
> - repeats: **yes**
> - 646 strict: **yes**
> - 646 loose: **yes**
> 
> Once you get a few hundred matches, then run dedupe.
> 
> If you paste the next `[scan summary]` after this change, I’ll tell you whether your noise level is acceptable or if we should tighten (e.g., word-boundaries for short terms like “trev”).

### User
> PS C:\QiOS_WORKING\My Drive\_working\VIDEO-FINDER> & C:/Users/codyr/AppData/Local/Python/bin/python.exe "c:/QiOS_WORKING/My Drive/_working/VIDEO-FINDER/video_finder_sqllite.py"

> Scan GLOBAL (all roots listed)? (Y/n): n

> 

> Available roots:

>   1) C:\

>   2) C:\QiOS_WORKING\My Drive

>   3) D:\

> 

> Enter comma-separated numbers to scan (example: 2,3). Press Enter for ALL.

> Selection: 3

> Enable path fuzzy filters (recommended)? (Y/n): y

> Enter terms (comma-separated). Example: tre, trev, treve, trevesin, miguel, manuel, isai, chicano, thug: trev, treve, trevesin, miguel, manuel, isai, chicano, thug

> Enable leetspeak normalization (e.g., m1gu3l, tr3v3)? (Y/n): y

> Enable repeated-letter detection (tttt, hhhh, grrrrr)? (Y/n): Y

> Enable strict 6-4-6 pattern (6...4...6)? (Y/n): Y

> Enable loose 6/4/6 presence (6 and 4 and 6 anywhere)? (Y/n): Y

> 

> [filter audit] {"enabled": true, "terms": ["trev", "treve", "trevesin", "miguel", "manuel", "isai", "chicano", "thug"], "enable_leetspeak": true, "enable_repeats": true, "enable_646_strict": true, "enable_646_loose": true, "logic": "OR", "scope": "FULL_PATH"}   

> 

> Scanning roots:

>  - D:\

> Extensions: .avi, .m4v, .media, .mkv, .mov, .mp4, .mpeg, .mpg, .wmv

> Minimum size: 1,048,576 bytes (1.0 MB)

> DB: c:\QiOS_WORKING\My Drive\_working\VIDEO-FINDER\video_index.sqlite3

> Checkpoint: prompt every ~10 GB of matched video

> 

> Traceback (most recent call last):

>   File "c:\QiOS_WORKING\My Drive\_working\VIDEO-FINDER\video_finder_sqllite.py", line 787, in <module>

>     main()

>     ~~~~^^

>   File "c:\QiOS_WORKING\My Drive\_working\VIDEO-FINDER\video_finder_sqllite.py", line 602, in main

>     if not name_filter(fullpath):

>                        ^^^^^^^^

> UnboundLocalError: cannot access local variable 'fullpath' where it is not associated with a value

> PS C:\QiOS_WORKING\My Drive\_working\VIDEO-FINDER>

### Assistant
> That error is 100% straightforward: you moved the `name_filter()` call to use `fullpath`, but you’re calling it **before `fullpath` is assigned**.
> 
> ### Fix (minimal, correct)
> Inside your innermost loop, you must set:
> 
> ```python
> fullpath = os.path.join(dirpath, fname)
> ```
> 
> **before** you call the filter.
> 
> #### Replace your current ordering with this exact sequence:
> 
> ```python
> for fname in filenames:
>     total_files += 1
>     ext = os.path.splitext(fname)[1].lower()
>     ext_seen[ext] += 1
> 
>     if ext not in VIDEO_EXTS:
>         skipped_by_ext += 1
>         continue
> 
>     fullpath = os.path.join(dirpath, fname)   # <-- MOVE THIS UP
> 
>     if not name_filter(fullpath):             # <-- NOW this is safe
>         skipped_by_name += 1
>         if len(rejected_samples) < 25:
>             rejected_samples.append(fullpath)
>         continue
> 
>     try:
>         st = os.stat(fullpath)
>         size = st.st_size
>         mtime = int(st.st_mtime)
>     except OSError:
>         continue
> 
>     if size < MIN_BYTES:
>         skipped_by_size += 1
>         if len(rejected_samples) < 25:
>             rejected_samples.append(fullpath + f" (size={size})")
>         continue
> 
>     in_rec = is_recycle_bin(fullpath.lower())
> 
>     matched_files += 1
>     matched_bytes += size
> 
>     db_upsert_file(conn, fullpath, dirpath, ext, size, mtime, in_rec, run_id)
> ```
> 
> That resolves `UnboundLocalError` immediately.
> 
> ---
> 
> ### Why it happened
> Python variables are scoped to the function. Since `fullpath` wasn’t set yet in the current iteration, it’s “unbound” at the moment you reference it.
> 
> ---
> 
> ### After you apply this
> Re-run the exact same command. You should see `matched_files` jump (probably from 1 to dozens/hundreds), because now folder names + leetspeak + digit patterns will actually be applied.
> 
> If it still returns too few matches after this fix, we’ll tighten/loosen the repeat-letter rule next (it can cause false positives if you have lots of `tt` in random paths).

### User
> can you give me the full udpated script all together.

### Assistant
> ```python
> import os
> import sys
> import json
> import csv
> import html
> import re
> import time
> import sqlite3
> import hashlib
> import urllib.parse
> from collections import defaultdict
> from datetime import datetime
> from concurrent.futures import ThreadPoolExecutor, as_completed
> 
> # -----------------------------
> # CONFIG
> # -----------------------------
> 
> SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
> DB_PATH = os.path.join(SCRIPT_DIR, "video_index.sqlite3")
> 
> VIDEO_EXTS = {
>     ".mp4", ".mov", ".avi", ".mkv", ".wmv", ".m4v", ".mpeg", ".mpg", ".media"
> }
> 
> # Keep legit small videos: 1MB minimum
> MIN_BYTES = 1 * 1024 * 1024  # 1MB
> 
> # Hashing
> HASH_WORKERS = 4
> QUICK_HASH_SAMPLE_BYTES = 1 * 1024 * 1024  # 1MB
> FULL_HASH_CHUNK_BYTES = 8 * 1024 * 1024    # 8MB
> 
> # Reporting
> MAX_FILES_PER_FOLDER = 10
> 
> # Checkpoint prompt every N GB of matched videos
> CHECKPOINT_GB = 10
> CHECKPOINT_BYTES = CHECKPOINT_GB * 1024 * 1024 * 1024
> 
> # Exclude by path segments (case-insensitive).
> # IMPORTANT: No raw strings ending with a single backslash. Use segments WITHOUT trailing '\'.
> # Recycle Bin is intentionally NOT excluded (you asked to include it).
> EXCLUDE_SEGMENTS = {
>     r"\windows",
>     r"\windows.old",
>     r"\program files",
>     r"\program files (x86)",
>     r"\programdata",
>     r"\appdata",
>     r"\system volume information",
>     r"\recovery",
>     r"\winsxs",
>     # optional noisy tool temp (leave off unless you want it)
>     # r"\.videoconverter\temp_source",
> }
> 
> DEFAULT_ROOTS = [
>     "C:\\",
>     r"C:\QiOS_WORKING\My Drive",
>     "D:\\",
> ]
> 
> # -----------------------------
> # PATH / URL HELPERS
> # -----------------------------
> 
> def norm_path_lower(p: str) -> str:
>     p = p.replace("/", "\\").lower()
>     if not p.endswith("\\"):
>         p += "\\"
>     return p
> 
> def is_excluded_path(path_like: str) -> bool:
>     p = norm_path_lower(path_like)
>     return any((seg + "\\") in p for seg in EXCLUDE_SEGMENTS)
> 
> def is_recycle_bin(path_like: str) -> bool:
>     p = norm_path_lower(path_like)
>     return r"\$recycle.bin" in p
> 
> def file_url_from_path(path: str) -> str:
>     p = path.replace("\\", "/")
>     if len(p) >= 2 and p[1] == ":":
>         p = "/" + p
>     return "file://" + urllib.parse.quote(p)
> 
> def safe_walk(root: str):
>     # followlinks=False avoids some junction recursion
>     for dirpath, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
>         if is_excluded_path(dirpath):
>             dirnames[:] = []
>             continue
> 
>         kept = []
>         for d in dirnames:
>             child = os.path.join(dirpath, d)
>             if not is_excluded_path(child):
>                 kept.append(d)
>         dirnames[:] = kept
> 
>         yield dirpath, filenames
> 
> def discover_existing_roots(roots):
>     existing = []
>     for r in roots:
>         if r and os.path.exists(r):
>             existing.append(r)
> 
>     # de-dupe while preserving order
>     seen = set()
>     uniq = []
>     for r in existing:
>         key = os.path.normcase(os.path.abspath(r))
>         if key not in seen:
>             seen.add(key)
>             uniq.append(r)
>     return uniq
> 
> # -----------------------------
> # PROMPTS
> # -----------------------------
> 
> def prompt_yes_no(msg: str, default_yes: bool = True) -> bool:
>     default = "Y/n" if default_yes else "y/N"
>     while True:
>         ans = input(f"{msg} ({default}): ").strip().lower()
>         if not ans:
>             return default_yes
>         if ans in ("y", "yes"):
>             return True
>         if ans in ("n", "no"):
>             return False
>         print("Please answer y or n.")
> 
> def choose_roots(roots):
>     print("\nAvailable roots:")
>     for i, r in enumerate(roots, start=1):
>         print(f"  {i}) {r}")
> 
>     print("\nEnter comma-separated numbers to scan (example: 2,3). Press Enter for ALL.")
>     ans = input("Selection: ").strip()
>     if not ans:
>         return roots
> 
>     idxs = []
>     for part in ans.split(","):
>         part = part.strip()
>         if part.isdigit():
>             idx = int(part)
>             if 1 <= idx <= len(roots):
>                 idxs.append(idx - 1)
> 
>     selected = [roots[i] for i in sorted(set(idxs))]
>     return selected if selected else roots
> 
> # -----------------------------
> # FUZZY FILTERS (FULL PATH)
> # -----------------------------
> 
> def normalize_leetspeak(s: str) -> str:
>     # Conservative substitutions; avoids turning every number into noise.
>     trans = str.maketrans({
>         "0": "o",
>         "1": "i",
>         "3": "e",
>         "4": "a",
>         "5": "s",
>         "7": "t",
>         "8": "b",
>         "9": "g",
>         "@": "a",
>         "$": "s",
>     })
>     return s.translate(trans)
> 
> def has_digits_anywhere(s: str, digits: str) -> bool:
>     # Count-aware: "646" requires >=2 '6' and >=1 '4' anywhere
>     for d in set(digits):
>         if s.count(d) < digits.count(d):
>             return False
>     return True
> 
> def build_name_filter():
>     """
>     Builds an OR-based fuzzy matcher that evaluates against FULL PATH.
>     Supports:
>       - custom terms (miguel/manuel/isai/treve/etc.)
>       - leetspeak normalization
>       - repeated-letter bursts (tttt, hhhh, grrrrr)
>       - strict 6...4...6 and loose presence of 6/4/6 anywhere
>     """
>     use_filters = prompt_yes_no("Enable path fuzzy filters (recommended)?", default_yes=True)
>     if not use_filters:
>         audit = {"enabled": False, "logic": None}
>         print("\n[filter audit] " + json.dumps(audit))
>         return (lambda _s: True), audit
> 
>     raw = input(
>         "Enter terms (comma-separated). Example: trev, treve, trevesin, miguel, manuel, isai, chicano, thug: "
>     ).strip()
>     terms = [t.strip().lower() for t in raw.split(",") if t.strip()]
> 
>     enable_leet = prompt_yes_no("Enable leetspeak normalization (e.g., m1gu3l, tr3v3)?", default_yes=True)
>     enable_repeats = prompt_yes_no("Enable repeated-letter detection (tttt, hhhh, grrrrr)?", default_yes=True)
>     enable_646_strict = prompt_yes_no("Enable strict 6-4-6 pattern (6...4...6)?", default_yes=True)
>     enable_646_loose = prompt_yes_no("Enable loose 6/4/6 presence (6 and 4 and 6 anywhere)?", default_yes=True)
> 
>     re_repeat_any = re.compile(r"([a-z])\1{1,}", re.IGNORECASE) if enable_repeats else None
>     re_646_strict = re.compile(r"6\D*4\D*6") if enable_646_strict else None
> 
>     def matches(full_path: str) -> bool:
>         s = full_path.lower()
>         rules = []
> 
>         # custom terms
>         if terms:
>             rules.append(any(t in s for t in terms))
> 
>         # leetspeak normalized term hits
>         if enable_leet and terms:
>             s_leet = normalize_leetspeak(s)
>             rules.append(any(t in s_leet for t in terms))
> 
>         # repeats
>         if re_repeat_any is not None:
>             rules.append(re_repeat_any.search(s) is not None)
> 
>         # numeric patterns
>         if re_646_strict is not None:
>             rules.append(re_646_strict.search(s) is not None)
> 
>         if enable_646_loose:
>             rules.append(has_digits_anywhere(s, "646"))
> 
>         # OR logic; if no rules enabled, match-all
>         return any(rules) if rules else True
> 
>     audit = {
>         "enabled": True,
>         "terms": terms,
>         "enable_leetspeak": enable_leet,
>         "enable_repeats": enable_repeats,
>         "enable_646_strict": enable_646_strict,
>         "enable_646_loose": enable_646_loose,
>         "logic": "OR",
>         "scope": "FULL_PATH",
>     }
>     print("\n[filter audit] " + json.dumps(audit, ensure_ascii=False))
>     return matches, audit
> 
> # -----------------------------
> # SQLITE
> # -----------------------------
> 
> def db_connect():
>     conn = sqlite3.connect(DB_PATH)
>     conn.execute("PRAGMA journal_mode=WAL;")
>     conn.execute("PRAGMA synchronous=NORMAL;")
>     conn.execute("PRAGMA temp_store=MEMORY;")
>     conn.execute("PRAGMA cache_size=-200000;")  # ~200MB cache (negative=KB)
>     return conn
> 
> def db_init(conn: sqlite3.Connection):
>     conn.executescript("""
>     CREATE TABLE IF NOT EXISTS runs (
>         run_id INTEGER PRIMARY KEY AUTOINCREMENT,
>         started_at TEXT NOT NULL,
>         roots TEXT NOT NULL,
>         min_bytes INTEGER NOT NULL,
>         filter_audit TEXT NOT NULL
>     );
> 
>     CREATE TABLE IF NOT EXISTS files (
>         path TEXT PRIMARY KEY,
>         folder TEXT NOT NULL,
>         ext TEXT NOT NULL,
>         size INTEGER NOT NULL,
>         mtime INTEGER NOT NULL,
>         in_recycle INTEGER NOT NULL,
>         seen_in_run INTEGER NOT NULL,
>         quick_hash TEXT,
>         sha256 TEXT
>     );
> 
>     CREATE INDEX IF NOT EXISTS idx_files_folder ON files(folder);
>     CREATE INDEX IF NOT EXISTS idx_files_size_ext ON files(size, ext);
>     CREATE INDEX IF NOT EXISTS idx_files_quickhash ON files(quick_hash);
>     CREATE INDEX IF NOT EXISTS idx_files_sha256 ON files(sha256);
>     """)
>     conn.commit()
> 
> def db_start_run(conn, roots, min_bytes, filter_audit):
>     cur = conn.cursor()
>     cur.execute(
>         "INSERT INTO runs (started_at, roots, min_bytes, filter_audit) VALUES (?,?,?,?)",
>         (datetime.now().isoformat(timespec="seconds"),
>          json.dumps(roots, ensure_ascii=False),
>          min_bytes,
>          json.dumps(filter_audit, ensure_ascii=False))
>     )
>     conn.commit()
>     return cur.lastrowid
> 
> def db_upsert_file(conn, path, folder, ext, size, mtime, in_recycle, run_id):
>     conn.execute("""
>     INSERT INTO files (path, folder, ext, size, mtime, in_recycle, seen_in_run, quick_hash, sha256)
>     VALUES (?, ?, ?, ?, ?, ?, ?, NULL, NULL)
>     ON CONFLICT(path) DO UPDATE SET
>         folder=excluded.folder,
>         ext=excluded.ext,
>         size=excluded.size,
>         mtime=excluded.mtime,
>         in_recycle=excluded.in_recycle,
>         seen_in_run=excluded.seen_in_run
>     """, (path, folder, ext, size, mtime, 1 if in_recycle else 0, run_id))
> 
> # -----------------------------
> # HASHING
> # -----------------------------
> 
> def quick_hash_file(path: str, sample_bytes: int = QUICK_HASH_SAMPLE_BYTES) -> str:
>     st = os.stat(path)
>     size = st.st_size
>     h = hashlib.sha256()
>     h.update(str(size).encode("utf-8"))
>     with open(path, "rb") as f:
>         head = f.read(sample_bytes)
>         h.update(head)
>         if size > sample_bytes:
>             f.seek(max(0, size - sample_bytes))
>             tail = f.read(sample_bytes)
>             h.update(tail)
>     return h.hexdigest()
> 
> def sha256_file(path: str, chunk_size: int = FULL_HASH_CHUNK_BYTES) -> str:
>     h = hashlib.sha256()
>     with open(path, "rb") as f:
>         while True:
>             chunk = f.read(chunk_size)
>             if not chunk:
>                 break
>             h.update(chunk)
>     return h.hexdigest()
> 
> # -----------------------------
> # REPORTING (FOLDERS + FILE LINKS)
> # -----------------------------
> 
> def build_folder_summaries(file_rows):
>     """
>     file_rows: list of tuples (path, folder, ext, size, in_recycle)
>     """
>     folder_counts = defaultdict(int)
>     folder_sizes = defaultdict(int)
>     folder_exts = defaultdict(lambda: defaultdict(int))
>     folder_files = defaultdict(list)
>     folder_largest = defaultdict(lambda: ("", 0))
> 
>     for path, folder, ext, size, _in_recycle in file_rows:
>         folder_counts[folder] += 1
>         folder_sizes[folder] += size
>         folder_exts[folder][ext] += 1
> 
>         if len(folder_files[folder]) < MAX_FILES_PER_FOLDER:
>             folder_files[folder].append(path)
> 
>         lp, ls = folder_largest[folder]
>         if size > ls:
>             folder_largest[folder] = (path, size)
> 
>     folders_sorted = sorted(folder_counts.keys(),
>                             key=lambda f: (folder_counts[f], folder_sizes[f]),
>                             reverse=True)
>     return folder_counts, folder_sizes, folder_exts, folder_files, folder_largest, folders_sorted
> 
> def write_folder_csv(out_csv, stats):
>     folder_counts, folder_sizes, folder_exts, folder_files, folder_largest, folders_sorted = stats
> 
>     with open(out_csv, "w", newline="", encoding="utf-8") as f:
>         w = csv.writer(f)
>         w.writerow(["count", "total_bytes", "folder_path", "folder_link", "largest_file_link", "sample_file_links", "top_extensions"])
>         for folder in folders_sorted:
>             exts_sorted = sorted(folder_exts[folder].items(), key=lambda kv: kv[1], reverse=True)
>             top_exts = " ".join([f"{k}:{v}" for k, v in exts_sorted[:10]])
> 
>             largest_path, _largest_size = folder_largest[folder]
>             largest_link = file_url_from_path(largest_path) if largest_path else ""
> 
>             sample_links = " | ".join(file_url_from_path(fp) for fp in folder_files[folder])
> 
>             w.writerow([
>                 folder_counts[folder],
>                 folder_sizes[folder],
>                 folder,
>                 file_url_from_path(folder),
>                 largest_link,
>                 sample_links,
>                 top_exts
>             ])
> 
> def write_folder_html(out_html, roots, filter_audit, min_bytes, scan_summary, stats):
>     folder_counts, folder_sizes, folder_exts, folder_files, folder_largest, folders_sorted = stats
> 
>     with open(out_html, "w", encoding="utf-8") as f:
>         f.write("<!doctype html><html><head><meta charset='utf-8'>")
>         f.write("<title>Video Folder Index</title>")
>         f.write("<style>")
>         f.write("body{font-family:Segoe UI,Arial,sans-serif;margin:24px}")
>         f.write("table{border-collapse:collapse;width:100%}")
>         f.write("th,td{border-bottom:1px solid #ddd;padding:8px;vertical-align:top}")
>         f.write("th{text-align:left;position:sticky;top:0;background:#f6f6f6}")
>         f.write("tr:hover{background:#fafafa}")
>         f.write(".muted{color:#666;font-size:12px}")
>         f.write("code{background:#f4f4f4;padding:2px 4px;border-radius:4px}")
>         f.write("</style></head><body>")
> 
>         f.write("<h1>Video Folder Index</h1>")
>         f.write(f"<div class='muted'>Generated: {html.escape(datetime.now().isoformat(timespec='seconds'))}</div>")
>         f.write(f"<div class='muted'>Roots scanned: {html.escape(' | '.join(roots))}</div>")
>         f.write(f"<div class='muted'>Min size: {min_bytes:,} bytes</div>")
>         f.write(f"<div class='muted'>Filter audit: <code>{html.escape(json.dumps(filter_audit, ensure_ascii=False))}</code></div>")
>         f.write(f"<div class='muted'>Total files seen: {scan_summary['total_files']:,} | Matching videos: {scan_summary['matched_files']:,} | Unique folders: {len(folders_sorted):,}</div>")
>         f.write("<hr>")
> 
>         f.write("<table><thead><tr>")
>         f.write("<th>Count</th><th>Total Size (GB)</th><th>Folder</th><th>Largest File</th><th>Sample Files</th><th>Top Extensions</th>")
>         f.write("</tr></thead><tbody>")
> 
>         for folder in folders_sorted:
>             folder_url = file_url_from_path(folder)
>             size_gb = folder_sizes[folder] / (1024 * 1024 * 1024)
>             exts_sorted = sorted(folder_exts[folder].items(), key=lambda kv: kv[1], reverse=True)
>             top_exts = " ".join([f"{k}:{v}" for k, v in exts_sorted[:10]])
> 
>             largest_path, _largest_size = folder_largest[folder]
>             largest_link = file_url_from_path(largest_path) if largest_path else ""
>             largest_label = os.path.basename(largest_path) if largest_path else ""
> 
>             samples_html = "<br>".join(
>                 f"<a href='{file_url_from_path(fp)}'>{html.escape(os.path.basename(fp))}</a>"
>                 for fp in folder_files[folder]
>             )
> 
>             f.write("<tr>")
>             f.write(f"<td>{folder_counts[folder]}</td>")
>             f.write(f"<td>{size_gb:.2f}</td>")
>             f.write(f"<td><a href='{folder_url}'>{html.escape(folder)}</a></td>")
>             f.write(f"<td><a href='{largest_link}'>{html.escape(largest_label)}</a></td>")
>             f.write(f"<td>{samples_html}</td>")
>             f.write(f"<td>{html.escape(top_exts)}</td>")
>             f.write("</tr>")
> 
>         f.write("</tbody></table></body></html>")
> 
> # -----------------------------
> # DEDUPE REPORTS
> # -----------------------------
> 
> def write_duplicates_reports(conn, out_dupes_csv, out_restore_csv):
>     """
>     Duplicates CSV: only sha256 groups with count > 1.
>     Restore CSV: sha256 groups where ALL members are in recycle bin (including singletons, if sha256 exists).
>     """
>     cur = conn.cursor()
> 
>     # Duplicate groups
>     cur.execute("""
>         SELECT sha256, COUNT(*) as c
>         FROM files
>         WHERE sha256 IS NOT NULL
>         GROUP BY sha256
>         HAVING c > 1
>         ORDER BY c DESC
>     """)
>     groups = cur.fetchall()
> 
>     with open(out_dupes_csv, "w", newline="", encoding="utf-8") as fdu:
>         w = csv.writer(fdu)
>         w.writerow(["sha256", "count", "has_non_recycle", "path", "in_recycle", "size", "mtime", "file_link"])
> 
>         for sha, c in groups:
>             cur.execute("""
>                 SELECT path, in_recycle, size, mtime
>                 FROM files
>                 WHERE sha256 = ?
>                 ORDER BY in_recycle ASC, size DESC
>             """, (sha,))
>             members = cur.fetchall()
>             has_non_recycle = any(m[1] == 0 for m in members)
> 
>             for path, in_rec, size, mtime in members:
>                 w.writerow([sha, c, 1 if has_non_recycle else 0, path, in_rec, size, mtime, file_url_from_path(path)])
> 
>     # Recycle-only hashes (restore candidates)
>     cur.execute("""
>         SELECT sha256
>         FROM files
>         WHERE sha256 IS NOT NULL
>         GROUP BY sha256
>         HAVING SUM(CASE WHEN in_recycle=0 THEN 1 ELSE 0 END) = 0
>     """)
>     recycle_only = [r[0] for r in cur.fetchall()]
> 
>     with open(out_restore_csv, "w", newline="", encoding="utf-8") as fr:
>         w = csv.writer(fr)
>         w.writerow(["sha256", "path", "size", "mtime", "file_link"])
>         for sha in recycle_only:
>             cur.execute("""
>                 SELECT path, size, mtime
>                 FROM files
>                 WHERE sha256 = ?
>                 ORDER BY size DESC
>             """, (sha,))
>             for path, size, mtime in cur.fetchall():
>                 w.writerow([sha, path, size, mtime, file_url_from_path(path)])
> 
> # -----------------------------
> # MAIN
> # -----------------------------
> 
> def main():
>     roots_all = discover_existing_roots(DEFAULT_ROOTS)
>     if not roots_all:
>         print("No valid roots found. Edit DEFAULT_ROOTS in the script.")
>         sys.exit(1)
> 
>     scan_global = prompt_yes_no("Scan GLOBAL (all roots listed)?", default_yes=True)
>     roots = roots_all if scan_global else choose_roots(roots_all)
> 
>     name_filter, filter_audit = build_name_filter()
> 
>     # SQLite init
>     conn = db_connect()
>     db_init(conn)
>     run_id = db_start_run(conn, roots, MIN_BYTES, filter_audit)
> 
>     print("\nScanning roots:")
>     for r in roots:
>         print(" -", r)
>     print(f"Extensions: {', '.join(sorted(VIDEO_EXTS))}")
>     print(f"Minimum size: {MIN_BYTES:,} bytes ({MIN_BYTES / (1024*1024):.1f} MB)")
>     print(f"DB: {DB_PATH}")
>     print(f"Checkpoint: prompt every ~{CHECKPOINT_GB} GB of matched video")
>     print("")
> 
>     folder_counts = defaultdict(int)  # not strictly needed; kept for quick stats if desired
> 
>     total_files = 0
>     matched_files = 0
>     skipped_by_name = 0
>     skipped_by_size = 0
>     skipped_by_ext = 0
>     ext_seen = defaultdict(int)
>     rejected_samples = []
> 
>     matched_bytes = 0
>     next_checkpoint = CHECKPOINT_BYTES
>     dirs_seen = 0
>     last_print = time.time()
> 
>     try:
>         for root in roots:
>             for dirpath, filenames in safe_walk(root):
>                 dirs_seen += 1
>                 now = time.time()
>                 if now - last_print >= 2:
>                     print(f"[scan] dirs:{dirs_seen:,} files:{total_files:,} matches:{matched_files:,} now:{dirpath}", flush=True)
>                     last_print = now
> 
>                 for fname in filenames:
>                     total_files += 1
>                     ext = os.path.splitext(fname)[1].lower()
>                     ext_seen[ext] += 1
> 
>                     if ext not in VIDEO_EXTS:
>                         skipped_by_ext += 1
>                         continue
> 
>                     # IMPORTANT: fullpath must be assigned BEFORE name_filter(fullpath)
>                     fullpath = os.path.join(dirpath, fname)
> 
>                     if not name_filter(fullpath):
>                         skipped_by_name += 1
>                         if len(rejected_samples) < 25:
>                             rejected_samples.append(fullpath)
>                         continue
> 
>                     try:
>                         st = os.stat(fullpath)
>                         size = st.st_size
>                         mtime = int(st.st_mtime)
>                     except OSError:
>                         continue
> 
>                     if size < MIN_BYTES:
>                         skipped_by_size += 1
>                         if len(rejected_samples) < 25:
>                             rejected_samples.append(fullpath + f" (size={size})")
>                         continue
> 
>                     in_rec = is_recycle_bin(fullpath)
> 
>                     matched_files += 1
>                     matched_bytes += size
> 
>                     db_upsert_file(conn, fullpath, dirpath, ext, size, mtime, in_rec, run_id)
> 
>                     # Batch commit for speed
>                     if matched_files % 5000 == 0:
>                         conn.commit()
> 
>                     if matched_bytes >= next_checkpoint:
>                         conn.commit()
>                         print(f"\n[checkpoint] Matched ~{matched_bytes / (1024**3):.1f} GB so far.")
>                         if not prompt_yes_no("Continue scanning?", default_yes=True):
>                             raise KeyboardInterrupt()
>                         next_checkpoint += CHECKPOINT_BYTES
> 
>         conn.commit()
> 
>     except KeyboardInterrupt:
>         conn.commit()
>         print("\nStopped early. Inventory saved to SQLite. You can re-run without losing progress.\n")
> 
>     # Post-scan summary
>     print("\n[scan summary]")
>     print(f"  total_files_seen: {total_files:,}")
>     print(f"  matched_files:    {matched_files:,}")
>     print(f"  matched_gb:       {matched_bytes / (1024**3):.2f}")
>     print(f"  skipped_by_name:  {skipped_by_name:,}")
>     print(f"  skipped_by_size:  {skipped_by_size:,}")
>     print(f"  skipped_by_ext:   {skipped_by_ext:,}")
> 
>     top_exts = sorted(ext_seen.items(), key=lambda kv: kv[1], reverse=True)[:10]
>     print("  top_extensions_seen:", dict(top_exts))
> 
>     if rejected_samples:
>         print("\n[rejected samples] (first 25)")
>         for s in rejected_samples[:25]:
>             print("  -", s)
>     else:
>         print("\n[rejected samples] none")
> 
>     # Ask: run dedupe now?
>     run_dedupe = prompt_yes_no("\nRun duplicate detection (hashing) now?", default_yes=True)
> 
>     if run_dedupe:
>         cur = conn.cursor()
> 
>         # Candidate groups by (size, ext) with count > 1
>         print("\n[dedupe] Selecting candidate groups by (size, ext) ...")
>         cur.execute("""
>             SELECT size, ext, COUNT(*) as c
>             FROM files
>             WHERE size >= ?
>             GROUP BY size, ext
>             HAVING c > 1
>             ORDER BY c DESC
>         """, (MIN_BYTES,))
>         candidates = cur.fetchall()
>         print(f"[dedupe] Candidate groups: {len(candidates):,}")
> 
>         # Gather files for quick-hash where quick_hash is NULL
>         to_quick = []
>         for size, ext, _c in candidates:
>             cur.execute("""
>                 SELECT path FROM files
>                 WHERE size=? AND ext=? AND quick_hash IS NULL
>             """, (size, ext))
>             to_quick.extend([r[0] for r in cur.fetchall()])
> 
>         print(f"[dedupe] Files to quick-hash: {len(to_quick):,} (workers={HASH_WORKERS})")
> 
>         def quick_job(p):
>             try:
>                 return p, quick_hash_file(p)
>             except Exception:
>                 return p, None
> 
>         with ThreadPoolExecutor(max_workers=HASH_WORKERS) as ex:
>             futures = [ex.submit(quick_job, p) for p in to_quick]
>             done = 0
>             for fut in as_completed(futures):
>                 path, qh = fut.result()
>                 done += 1
>                 if qh:
>                     conn.execute("UPDATE files SET quick_hash=? WHERE path=?", (qh, path))
>                 if done % 200 == 0:
>                     conn.commit()
>                     print(f"[dedupe] quick-hash {done:,}/{len(to_quick):,}", flush=True)
>             conn.commit()
> 
>         # Full-hash only where quick_hash collides AND sha256 is NULL
>         cur.execute("""
>             SELECT quick_hash, COUNT(*) as c
>             FROM files
>             WHERE quick_hash IS NOT NULL
>             GROUP BY quick_hash
>             HAVING c > 1
>             ORDER BY c DESC
>         """)
>         qh_groups = cur.fetchall()
>         print(f"[dedupe] Quick-hash collision groups: {len(qh_groups):,}")
> 
>         to_full = []
>         for qh, _c in qh_groups:
>             cur.execute("""
>                 SELECT path FROM files
>                 WHERE quick_hash=? AND sha256 IS NULL
>             """, (qh,))
>             to_full.extend([r[0] for r in cur.fetchall()])
> 
>         print(f"[dedupe] Files to full-hash (sha256): {len(to_full):,} (workers={HASH_WORKERS})")
> 
>         def full_job(p):
>             try:
>                 return p, sha256_file(p)
>             except Exception:
>                 return p, None
> 
>         with ThreadPoolExecutor(max_workers=HASH_WORKERS) as ex:
>             futures = [ex.submit(full_job, p) for p in to_full]
>             done = 0
>             for fut in as_completed(futures):
>                 path, sh = fut.result()
>                 done += 1
>                 if sh:
>                     conn.execute("UPDATE files SET sha256=? WHERE path=?", (sh, path))
>                 if done % 100 == 0:
>                     conn.commit()
>                     print(f"[dedupe] sha256 {done:,}/{len(to_full):,}", flush=True)
>             conn.commit()
> 
>         print("[dedupe] Done hashing.")
> 
>     # Build folder/file rows for this run only
>     cur = conn.cursor()
>     cur.execute("""
>         SELECT path, folder, ext, size, in_recycle
>         FROM files
>         WHERE seen_in_run = ?
>         ORDER BY folder
>     """, (run_id,))
>     file_rows = cur.fetchall()
> 
>     stats = build_folder_summaries(file_rows)
> 
>     ts = datetime.now().strftime("%Y%m%d_%H%M%S")
>     out_folder_csv = os.path.join(SCRIPT_DIR, f"video_folders_{ts}.csv")
>     out_folder_html = os.path.join(SCRIPT_DIR, f"video_folders_{ts}.html")
> 
>     scan_summary = {
>         "total_files": total_files,
>         "matched_files": matched_files,
>         "matched_bytes": matched_bytes,
>     }
> 
>     write_folder_csv(out_folder_csv, stats)
>     write_folder_html(out_folder_html, roots, filter_audit, MIN_BYTES, scan_summary, stats)
> 
>     print("\nReports:")
>     print("  Folder CSV :", out_folder_csv)
>     print("  Folder HTML:", out_folder_html)
> 
>     # If dedupe ran (or prior runs), output duplicate reports if we have sha256 coverage
>     cur.execute("SELECT COUNT(*) FROM files WHERE sha256 IS NOT NULL")
>     hashed_count = cur.fetchone()[0]
> 
>     if hashed_count > 0:
>         out_dupes_csv = os.path.join(SCRIPT_DIR, f"duplicates_{ts}.csv")
>         out_restore_csv = os.path.join(SCRIPT_DIR, f"restore_candidates_recycle_only_{ts}.csv")
>         write_duplicates_reports(conn, out_dupes_csv, out_restore_csv)
>         print("  Duplicates CSV:", out_dupes_csv)
>         print("  Restore CSV  :", out_restore_csv)
> 
>     conn.close()
>     print("\nDone.")
> 
> if __name__ == "__main__":
>     main()
> ```
