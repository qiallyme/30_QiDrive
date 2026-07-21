---
layout: page
title: "Unlock PDF Folder Files"
slug: "unlock_pdf_folder_files"
created_at: "2026-03-22 08:33:26"
updated_at: "2026-07-18T11:03:14-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-005.json"
template_key: master-template
date: 2026-03-22
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69bfef9a-fea0-8333-bdaa-2973323d0dbe"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Unlock PDF Folder Files

## Overview
- **Date**: 2026-03-22 08:33:26
- **Conversation ID**: `69bfef9a-fea0-8333-bdaa-2973323d0dbe`
- **Source**: `Chat-Export-28513-2026/conversations-005.json`

## Chat History

### User
> i need the command to unlock the pdf being blocked for a whole folder.

### Assistant
> Got you — quick, clean, no fluff.
> 
> ### ✅ If you're on **Windows (PowerShell)**  
> This removes the “blocked” flag (Mark of the Web) from ALL PDFs in a folder:
> 
> ```powershell
> Get-ChildItem "C:\path\to\your\folder" -Filter *.pdf -Recurse | Unblock-File
> ```
> 
> ---
> 
> ### 🔥 If you want to nuke ALL blocked files (not just PDFs):
> ```powershell
> Get-ChildItem "C:\path\to\your\folder" -Recurse | Unblock-File
> ```
> 
> ---
> 
> ### ⚡ Faster / more explicit (uses streams directly):
> ```powershell
> Get-ChildItem "C:\path\to\your\folder" -Recurse -Filter *.pdf | ForEach-Object {
>     Remove-Item -Path $_.FullName -Stream Zone.Identifier -ErrorAction SilentlyContinue
> }
> ```
> 
> ---
> 
> ### 🧠 What this is doing (quick context)
> Windows tags downloaded files with a `Zone.Identifier` stream → that’s what causes the “This file came from another computer” block.  
> These commands strip that tag.
> 
> ---
> 
> ### 🚨 Pro tip (you’ll care about this)
> If you’re prepping **court PDFs**:
> - This step is **mandatory** before merging or e-filing  
> - Hidden streams can cause **silent rejection or corruption flags**
> 
> ---
> 
> If you want, I can roll this into your **QiVault ingestion script** so every file gets auto-cleaned on import — no manual step ever again.

### User
> just have it to the bath the terminal is open in, how can i fix that for my whole machine casue this is all the time.

### Assistant
> Alright — two levels here: **quick fix for current folder** and **permanent fix so this stops happening.**
> 
> ---
> 
> ## ✅ 1. Current folder (what your terminal is already in)
> 
> Just run this — no path needed:
> 
> ```powershell
> Get-ChildItem -Recurse -Filter *.pdf | Unblock-File
> ```
> 
> Or everything (not just PDFs):
> 
> ```powershell
> Get-ChildItem -Recurse | Unblock-File
> ```
> 
> ---
> 
> ## 🔥 2. Fix it system-wide (stop the problem at the source)
> 
> Windows is adding the “Mark of the Web” (Zone.Identifier) every time you download files.
> 
> ### Option A — Disable it via Group Policy (best)
> 
> Run:
> 
> ```powershell
> gpedit.msc
> ```
> 
> Then go to:
> 
> ```
> User Configuration
> → Administrative Templates
> → Windows Components
> → Attachment Manager
> ```
> 
> Set:
> 
> > **Do not preserve zone information in file attachments = ENABLED**
> 
> ✔ This tells Windows: *stop tagging files as blocked*
> 
> ---
> 
> ### Option B — Registry (if no gpedit)
> 
> Run this:
> 
> ```powershell
> New-Item -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\Attachments" -Force
> Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\Attachments" -Name "SaveZoneInformation" -Value 1
> ```
> 
> ---
> 
> ## ⚠️ Reality check (important)
> Disabling this:
> - ✅ Removes constant unblock headaches
> - ❌ Removes a layer of Windows security warnings
> 
> For you → worth it  
> You’re handling controlled docs, not random shady downloads.
> 
> ---
> 
> ## 🧠 Best-practice (your setup specifically)
> 
> Don’t rely on memory. Automate it:
> 
> Create a tiny script:
> 
> ```powershell
> # unblock-all.ps1
> Get-ChildItem -Recurse | Unblock-File
> ```
> 
> Then:
> - Drop it into your working folders
> - Or wire it into your ingestion pipeline (QiVault step)
> 
> ---
> 
> ## 💡 My recommendation (clean + scalable)
> 
> Do BOTH:
> 1. Disable zone tagging (so future files are clean)
> 2. Keep an unblock step in your ingestion pipeline (for safety)
> 
> ---
> 
> If you want next step:
> I’ll wire this into your **QiVault ingestion + hashing pipeline** so:
> - File drops in
> - Gets renamed
> - Hash generated
> - Zone stripped
> - Indexed
> 
> Zero friction, fully automated.

### User
> can you create a python script that will do this for download when i run it

### Assistant
> Yep. I made it.
> 
> **Download:** [unblock_downloads.py](sandbox:/mnt/data/unblock_downloads.py)
> 
> ### Use it
> Default behavior: scans your **Downloads** folder and unblocks **PDFs** recursively.
> 
> ```bash
> python unblock_downloads.py
> ```
> 
> ### Useful variants
> 
> Unblock **everything** in Downloads:
> 
> ```bash
> python unblock_downloads.py --all
> ```
> 
> Unblock PDFs in the folder you’re currently in:
> 
> ```bash
> python unblock_downloads.py --folder .
> ```
> 
> Unblock everything in the current folder:
> 
> ```bash
> python unblock_downloads.py --folder . --all
> ```
> 
> Top-level only, no subfolders:
> 
> ```bash
> python unblock_downloads.py --no-recursive
> ```
> 
> ### What it does
> It removes the Windows `Zone.Identifier` stream, which is the stupid little “this file came from another computer” block.
> 
> ### Real talk
> This is a **manual cleanup script** when you run it. It does **not** automatically fire the second a file downloads.
> 
> If you want the next version, I can give you one that:
> - watches your Downloads folder continuously, or
> - makes a `.bat` launcher so you can double-click it like a normal person instead of typing commands.

### User
> heres an example of a tools script i have inside a python tools utility, can you update this code to follow the same structure so i can add it to my tool kit. import os

> import re

> import tkinter as tk

> from tkinter import ttk

> from core.base_tool import BaseTool

> import traceback

> 

> class ArchiveRouterTool(BaseTool):

>     def __init__(self):

>         self.target_extensions = {

>             '.pdf', '.md', '.csv', '.xls', '.xlsx', '.doc', '.docx', '.ppt', '.pptx', '.txt', '.rtf',

>             '.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm',

>             '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff'

>         }

>         self.ignore_folders = {

>             '.git', '.vscode', '.idea', 'node_modules', 'dist', 'build', 

>             '.next', '.turbo', '.cache', '__pycache__', 'public', 'vendor'

>         }

>         

>         # New State Variables

>         self.cancel_requested = False

>         self.memory_cache = []

>         self.memory_params = None

> 

>     def get_name(self):

>         return "📂 Archive Router"

> 

>     def build_ui(self, parent):

>         tk.Label(parent, text="Target ID Prefix (e.g. BBR4821):", bg="#0f0f11", fg="white").pack(anchor='w')

>         self.id_var = tk.StringVar()

>         tk.Entry(parent, textvariable=self.id_var, bg="#1c1c1e", fg="white", insertbackground="white").pack(fill='x', pady=(0, 10), ipady=5)

> 

>         tk.Label(parent, text="Keyword Hunter (Comma separated, leave blank for all):", bg="#0f0f11", fg="white").pack(anchor='w')

>         self.kw_var = tk.StringVar()

>         tk.Entry(parent, textvariable=self.kw_var, bg="#1c1c1e", fg="white", insertbackground="white").pack(fill='x', pady=(0, 5), ipady=5)

>         

>         # The Exact Match Toggle

>         self.exact_match_var = tk.BooleanVar(value=False)

>         ttk.Checkbutton(parent, text="Exact Keyword Match (e.g. '1' won't trigger '10' or '11')", variable=self.exact_match_var).pack(anchor='w', pady=(0, 10))

> 

>     def extract_and_format_date(self, name):

>         date_pattern = re.compile(r'\b(\d{1,4})[-/](\d{1,2})[-/](\d{1,4})\b')

>         match = date_pattern.search(name)

>         formatted_date = ""

>         if match:

>             full_match = match.group(0)

>             parts = re.split(r'[-/]', full_match)

>             y, m, d = (parts[0], parts[1], parts[2]) if len(parts[0]) == 4 else (parts[2], parts[0], parts[1])

>             formatted_date = f"{y}-{int(m):02d}-{int(d):02d}_"

>             name = name.replace(full_match, '')

>         return name, formatted_date

> 

>     def normalize_name(self, name, is_folder):

>         name = re.sub(r'[()]', '', name)

>         name = re.sub(r'\s*-\s*', '-', name)

>         name = re.sub(r'\s+', '_', name)

>         name = name.strip('_')

>         name = re.sub(r'_+', '_', name)

>         return name.capitalize() if is_folder else name.lower()

> 

>     def clean_base_name(self, name, target_id):

>         clean_name = name

>         if target_id:

>             base_id = target_id.strip('_')

>             clean_name = re.sub(re.escape(base_id), '', clean_name, flags=re.IGNORECASE)

>         clean_name = re.sub(r'bbr_', '', clean_name, flags=re.IGNORECASE)

>         return clean_name

> 

>     def execute(self, target_path, is_live, log, prog):

>         try:

>             self.cancel_requested = False 

>             target_id = self.id_var.get().strip().rstrip('_').upper() + '_' if self.id_var.get() else ""

>             raw_kws = self.kw_var.get()

>             keywords = [k.strip().lower() for k in raw_kws.split(',')] if raw_kws else []

>             exact_match = self.exact_match_var.get()

>             

>             current_params = (target_path, target_id, raw_kws, exact_match)

> 

>             if is_live and self.memory_cache and self.memory_params == current_params:

>                 log(f"🚀 [ROUTER] EXECUTING DIRECTLY FROM DRY RUN MEMORY...\n" + "-"*40)

>                 total = len(self.memory_cache)

>                 for i, (old_path, new_path, type_lbl) in enumerate(self.memory_cache):

>                     if self.cancel_requested:

>                         log("🛑 OPERATION ABORTED BY USER.")

>                         break

>                     

>                     try:

>                         os.rename(old_path, new_path)

>                         log(f"✅ {type_lbl} RENAMED: {os.path.basename(new_path)}")

>                     except Exception as e:

>                         log(f"❌ ERROR: {os.path.basename(old_path)} -> {e}")

>                     

>                     prog(((i+1) / max(1, total)) * 100)

> 

>                 self.memory_cache = [] 

>                 log("-" * 40 + "\n✅ ROUTER COMPLETE.\n")

>                 return

> 

>             self.memory_cache = [] 

>             self.memory_params = current_params

>         

>             log(f"🚀 [ROUTER] STARTING {'LIVE' if is_live else 'DRY RUN'} IN: {target_path}\n" + "-"*40)

>         

>             log("⏳ Calculating total items for progress bar (this might take a second)...")

>             total_items = sum([len(dirs) + len(files) for _, dirs, files in os.walk(target_path)])

>             log(f"📊 Found {total_items} items to scan. Beginning processing...")

>             

>             processed = 0

>             current_root = ""

> 

>             for root, dirs, files in os.walk(target_path, topdown=False):

>                 if self.cancel_requested:

>                     log("\n🛑 SCAN ABORTED BY USER.")

>                     break

> 

>                 if set(root.lower().replace('\\', '/').split('/')).intersection(self.ignore_folders):

>                     continue

> 

>                 # Breadcrumb Logging: Tell the user where we are currently looking

>                 if current_root != root:

>                     log(f"\n📂 Scanning Directory: {root}")

>                     current_root = root

> 

>                 # --- Process Files ---

>                 for file in files:

>                     processed += 1

>                     prog((processed / max(1, total_items)) * 100)

>                     

>                     name, ext = os.path.splitext(file)

>                     if ext.lower() not in self.target_extensions: continue

>                     

>                     if keywords:

>                         match_found = False

>                         for kw in keywords:

>                             if exact_match and re.search(rf'\b{re.escape(kw)}\b', name.lower()): match_found = True; break

>                             elif not exact_match and kw in name.lower(): match_found = True; break

>                         if not match_found: continue

> 

>                     clean_name = self.clean_base_name(name, target_id)

>                     clean_name, ext_date = self.extract_and_format_date(clean_name)

>                     clean_name = self.normalize_name(clean_name, False)

>                     new_name = f"{target_id}{ext_date}{clean_name}{ext.lower()}"

> 

>                     if file != new_name:

>                         old_path = os.path.join(root, file)

>                         new_path = os.path.join(root, new_name)

>                         

>                         if is_live:

>                             try:

>                                 os.rename(old_path, new_path)

>                                 log(f"✅ FILE: {new_name}")

>                             except Exception as e: log(f"❌ ERROR: {file} -> {e}")

>                         else:

>                             log(f"🔎 PREVIEW: {file} -> {new_name}")

>                             self.memory_cache.append((old_path, new_path, "FILE")) # Store in memory

> 

>                 # --- Process Folders ---

>                 for folder in dirs:

>                     processed += 1

>                     prog((processed / max(1, total_items)) * 100)

>                     

>                     if keywords:

>                         match_found = False

>                         for kw in keywords:

>                             if exact_match and re.search(rf'\b{re.escape(kw)}\b', folder.lower()): match_found = True; break

>                             elif not exact_match and kw in folder.lower(): match_found = True; break

>                     if not match_found: continue

> 

>                     clean_folder = self.clean_base_name(folder, target_id)

>                     clean_folder, ext_date = self.extract_and_format_date(clean_folder)

>                     clean_folder = self.normalize_name(clean_folder, True)

>                     new_name = f"{target_id}{ext_date}{clean_folder}"

> 

>                     if folder != new_name:

>                         old_path = os.path.join(root, folder)

>                         new_path = os.path.join(root, new_name)

> 

>                         if is_live:

>                             try:

>                                 os.rename(old_path, new_path)

>                                 log(f"📁 FOLDER: {new_name}/")

>                             except Exception as e: log(f"❌ ERROR: {folder} -> {e}")

>                         else:

>                             log(f"🔎 PREVIEW: {folder}/ -> {new_name}/")

>                             self.memory_cache.append((old_path, new_path, "FOLDER")) # Store in memory

> 

>             if not self.cancel_requested:

>                 log("-" * 40 + "\n✅ ROUTER COMPLETE.\n")

>         except Exception as e:

>             log(f"\n❌ CRITICAL THREAD ERROR ❌\n{traceback.format_exc()}")

### Assistant
> Yes. Your current script is a plain CLI utility. For your toolkit, it needs to behave like your `BaseTool` pattern:
> 
> - `get_name()`
> - `build_ui(parent)`
> - `execute(target_path, is_live, log, prog)`
> - optional dry-run memory cache
> - cancel support
> - clean logging
> 
> Below is a **drop-in tool version** that follows the same structure as your `ArchiveRouterTool`.
> 
> ```python
> import os
> import tkinter as tk
> from tkinter import ttk
> from core.base_tool import BaseTool
> import traceback
> 
> 
> class UnblockDownloadsTool(BaseTool):
>     def __init__(self):
>         # State
>         self.cancel_requested = False
>         self.memory_cache = []
>         self.memory_params = None
> 
>         # Common document/media extensions you may want to unblock selectively
>         self.common_extensions = {
>             ".pdf", ".md", ".csv", ".xls", ".xlsx", ".doc", ".docx",
>             ".ppt", ".pptx", ".txt", ".rtf",
>             ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff",
>             ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm",
>             ".zip", ".7z", ".rar", ".json", ".xml"
>         }
> 
>         self.ignore_folders = {
>             ".git", ".vscode", ".idea", "node_modules", "dist", "build",
>             ".next", ".turbo", ".cache", "__pycache__", "vendor"
>         }
> 
>     def get_name(self):
>         return "🔓 Unblock Files"
> 
>     def build_ui(self, parent):
>         tk.Label(
>             parent,
>             text="Extension Filter (comma separated, blank = use defaults):",
>             bg="#0f0f11",
>             fg="white"
>         ).pack(anchor="w")
> 
>         self.ext_var = tk.StringVar(value=".pdf")
>         tk.Entry(
>             parent,
>             textvariable=self.ext_var,
>             bg="#1c1c1e",
>             fg="white",
>             insertbackground="white"
>         ).pack(fill="x", pady=(0, 5), ipady=5)
> 
>         self.all_files_var = tk.BooleanVar(value=False)
>         ttk.Checkbutton(
>             parent,
>             text="Process ALL file types",
>             variable=self.all_files_var
>         ).pack(anchor="w", pady=(0, 5))
> 
>         self.recursive_var = tk.BooleanVar(value=True)
>         ttk.Checkbutton(
>             parent,
>             text="Scan subfolders recursively",
>             variable=self.recursive_var
>         ).pack(anchor="w", pady=(0, 5))
> 
>         self.skip_ignored_var = tk.BooleanVar(value=True)
>         ttk.Checkbutton(
>             parent,
>             text="Skip common junk/dev folders",
>             variable=self.skip_ignored_var
>         ).pack(anchor="w", pady=(0, 10))
> 
>     def _parse_extensions(self, raw_exts):
>         """
>         Normalize comma-separated extensions into a set like {'.pdf', '.docx'}.
>         Blank input falls back to {'.pdf'} unless ALL is checked.
>         """
>         if not raw_exts.strip():
>             return {".pdf"}
> 
>         parsed = set()
>         for ext in raw_exts.split(","):
>             ext = ext.strip().lower()
>             if not ext:
>                 continue
>             if not ext.startswith("."):
>                 ext = "." + ext
>             parsed.add(ext)
>         return parsed or {".pdf"}
> 
>     def _has_zone_identifier(self, file_path):
>         """
>         Check whether the file has the Zone.Identifier ADS.
>         """
>         ads_path = file_path + ":Zone.Identifier"
>         return os.path.exists(ads_path)
> 
>     def _remove_zone_identifier(self, file_path):
>         """
>         Remove the Zone.Identifier ADS from the file.
>         Returns True if removed, False if there was nothing to remove.
>         """
>         ads_path = file_path + ":Zone.Identifier"
>         if os.path.exists(ads_path):
>             os.remove(ads_path)
>             return True
>         return False
> 
>     def _should_skip_root(self, root):
>         root_parts = set(root.lower().replace("\\", "/").split("/"))
>         return bool(root_parts.intersection(self.ignore_folders))
> 
>     def _collect_candidates(self, target_path, recursive, process_all, extensions, skip_ignored):
>         """
>         Build a list of files eligible for inspection/unblocking.
>         """
>         candidates = []
> 
>         if recursive:
>             walker = os.walk(target_path)
>         else:
>             # Simulate os.walk top-level only
>             try:
>                 entries = os.listdir(target_path)
>             except Exception:
>                 return candidates
> 
>             files = []
>             dirs = []
>             for name in entries:
>                 full = os.path.join(target_path, name)
>                 if os.path.isdir(full):
>                     dirs.append(name)
>                 elif os.path.isfile(full):
>                     files.append(name)
>             walker = [(target_path, dirs, files)]
> 
>         for root, dirs, files in walker:
>             if skip_ignored and self._should_skip_root(root):
>                 continue
> 
>             for file in files:
>                 full_path = os.path.join(root, file)
> 
>                 if process_all:
>                     candidates.append(full_path)
>                     continue
> 
>                 _, ext = os.path.splitext(file)
>                 if ext.lower() in extensions:
>                     candidates.append(full_path)
> 
>         return candidates
> 
>     def execute(self, target_path, is_live, log, prog):
>         try:
>             self.cancel_requested = False
> 
>             raw_exts = self.ext_var.get().strip()
>             process_all = self.all_files_var.get()
>             recursive = self.recursive_var.get()
>             skip_ignored = self.skip_ignored_var.get()
>             extensions = self._parse_extensions(raw_exts)
> 
>             current_params = (
>                 target_path,
>                 raw_exts,
>                 process_all,
>                 recursive,
>                 skip_ignored
>             )
> 
>             # Live mode can reuse dry-run memory if params match
>             if is_live and self.memory_cache and self.memory_params == current_params:
>                 log("🚀 [UNBLOCKER] EXECUTING DIRECTLY FROM DRY RUN MEMORY...\n" + "-" * 40)
>                 total = len(self.memory_cache)
> 
>                 unblocked = 0
>                 failed = 0
> 
>                 for i, file_path in enumerate(self.memory_cache):
>                     if self.cancel_requested:
>                         log("🛑 OPERATION ABORTED BY USER.")
>                         break
> 
>                     try:
>                         changed = self._remove_zone_identifier(file_path)
>                         if changed:
>                             unblocked += 1
>                             log(f"✅ UNBLOCKED: {file_path}")
>                         else:
>                             log(f"⏭️ ALREADY CLEAN: {file_path}")
>                     except Exception as e:
>                         failed += 1
>                         log(f"❌ ERROR: {file_path} -> {e}")
> 
>                     prog(((i + 1) / max(1, total)) * 100)
> 
>                 self.memory_cache = []
> 
>                 log("-" * 40)
>                 log(f"✅ UNBLOCK COMPLETE | Unblocked: {unblocked} | Failed: {failed}\n")
>                 return
> 
>             # Fresh scan
>             self.memory_cache = []
>             self.memory_params = current_params
> 
>             mode_label = "ALL FILE TYPES" if process_all else f"EXTENSIONS: {', '.join(sorted(extensions))}"
>             recurse_label = "RECURSIVE" if recursive else "TOP-LEVEL ONLY"
> 
>             log(f"🚀 [UNBLOCKER] STARTING {'LIVE' if is_live else 'DRY RUN'} IN: {target_path}")
>             log(f"📌 Mode: {mode_label}")
>             log(f"📌 Scope: {recurse_label}")
>             log("-" * 40)
> 
>             log("⏳ Scanning for candidate files...")
>             candidates = self._collect_candidates(
>                 target_path=target_path,
>                 recursive=recursive,
>                 process_all=process_all,
>                 extensions=extensions,
>                 skip_ignored=skip_ignored
>             )
> 
>             total = len(candidates)
>             log(f"📊 Found {total} candidate files to inspect.")
> 
>             inspected = 0
>             blocked_found = 0
>             unblocked = 0
>             skipped = 0
>             failed = 0
> 
>             for file_path in candidates:
>                 if self.cancel_requested:
>                     log("\n🛑 SCAN ABORTED BY USER.")
>                     break
> 
>                 inspected += 1
>                 prog((inspected / max(1, total)) * 100)
> 
>                 try:
>                     has_block = self._has_zone_identifier(file_path)
> 
>                     if not has_block:
>                         skipped += 1
>                         continue
> 
>                     blocked_found += 1
> 
>                     if is_live:
>                         changed = self._remove_zone_identifier(file_path)
>                         if changed:
>                             unblocked += 1
>                             log(f"✅ UNBLOCKED: {file_path}")
>                         else:
>                             skipped += 1
>                             log(f"⏭️ ALREADY CLEAN: {file_path}")
>                     else:
>                         log(f"🔎 PREVIEW: BLOCKED -> {file_path}")
>                         self.memory_cache.append(file_path)
> 
>                 except Exception as e:
>                     failed += 1
>                     log(f"❌ ERROR: {file_path} -> {e}")
> 
>             if not self.cancel_requested:
>                 if not is_live:
>                     log("-" * 40)
>                     log(
>                         f"✅ DRY RUN COMPLETE | "
>                         f"Candidates: {total} | "
>                         f"Blocked Found: {blocked_found} | "
>                         f"Ready to Unblock: {len(self.memory_cache)} | "
>                         f"Failed: {failed}\n"
>                     )
>                 else:
>                     log("-" * 40)
>                     log(
>                         f"✅ UNBLOCK COMPLETE | "
>                         f"Candidates: {total} | "
>                         f"Blocked Found: {blocked_found} | "
>                         f"Unblocked: {unblocked} | "
>                         f"Skipped: {skipped} | "
>                         f"Failed: {failed}\n"
>                     )
> 
>         except Exception:
>             log(f"\n❌ CRITICAL THREAD ERROR ❌\n{traceback.format_exc()}")
> ```
> 
> ## What changed from your standalone script
> 
> ### 1. Converted it into your toolkit class model
> It now matches your app structure:
> - inherits `BaseTool`
> - has `build_ui()`
> - uses `execute(target_path, is_live, log, prog)`
> 
> ### 2. Added dry-run memory behavior
> Same pattern as your router:
> - first run in preview mode shows what would be unblocked
> - live run can reuse cached results if params match
> 
> ### 3. Added UI controls
> You can now choose:
> - specific extensions
> - all files
> - recursive or top-level only
> - skip junk folders
> 
> ### 4. Uses Windows ADS removal directly
> This is the real thing:
> ```python
> file_path + ":Zone.Identifier"
> ```
> That’s what removes the “blocked” status.
> 
> ---
> 
> ## Important reality check
> 
> Your original example tool is a **rename/router**.  
> This unblocker is **state-based cleanup**, so the memory cache stores file paths instead of `(old_path, new_path, type_lbl)` tuples. That’s correct for this use case.
> 
> ---
> 
> ## One bug in your example code you should fix
> Your folder loop has a logic issue:
> 
> ```python
> if keywords:
>     match_found = False
>     for kw in keywords:
>         if exact_match and re.search(...): match_found = True; break
>         elif not exact_match and kw in folder.lower(): match_found = True; break
> if not match_found: continue
> ```
> 
> If `keywords` is blank, `match_found` never exists and that can blow up depending on flow.  
> You got lucky because of the surrounding structure, but it’s sloppy. Initialize it cleanly before the condition or wrap the `continue` inside the keyword block.
> 
> Cleaner:
> 
> ```python
> match_found = True if not keywords else False
> for kw in keywords:
>     if exact_match and re.search(rf'\b{re.escape(kw)}\b', folder.lower()):
>         match_found = True
>         break
>     elif not exact_match and kw in folder.lower():
>         match_found = True
>         break
> 
> if not match_found:
>     continue
> ```
> 
> That applies to both file and folder matching.
> 
> ---
> 
> ## My recommendation
> Add one more checkbox later:
> 
> - **“Auto-unblock on scan before other tools run”**
> 
> Because honestly, this should probably become a shared utility your other file tools call first when touching downloaded docs.
> 
> If you want, I can also refactor this one into the exact same visual/logging style as your broader toolkit, including a **summary card**, **count badges**, and a **Stop button hook** pattern.
