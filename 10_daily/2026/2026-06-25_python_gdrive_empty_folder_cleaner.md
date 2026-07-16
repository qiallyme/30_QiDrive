---
layout: page
title: "Python GDrive Empty Folder Cleaner"
slug: "python_gdrive_empty_folder_cleaner"
created_at: "2026-06-25 19:28:19"
updated_at: "2026-07-16T06:49:34-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-009.json"
template_key: master-template
date: 2026-06-25
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a3dc785-1490-83ea-981e-53d66dc4552a"
canonical_ref: ""
---

# Python GDrive Empty Folder Cleaner

## Overview
- **Date**: 2026-06-25 19:28:19
- **Conversation ID**: `6a3dc785-1490-83ea-981e-53d66dc4552a`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> gril i need a script preferribly python script to add to my tool box  that can walk the gdrive and remove empty folders, now you know the empty folders have some hidden desktop.ini file or somethign soemtimes, thats still empty to me, but its important that is doesnt accidently delete a folder that has a folder that has something in it, so it has to check the whole path before quartining the folders.

### Assistant
> I’ll give you a safe toolbox-grade script, not a reckless “delete empty dirs” toy. The key move is **bottom-up scanning + quarantine-first + dry-run default**, so a folder only gets moved after its entire subtree is proven empty except ignorable junk like `desktop.ini`.

### Assistant
> Girl yes. Use **quarantine-first**, not delete-first. This script:
> 
> - Walks the folder tree **bottom-up**
> - Treats junk files like `desktop.ini`, `.DS_Store`, `Thumbs.db` as “empty”
> - Does **not** remove a folder if any descendant contains a real file
> - Defaults to **dry run**
> - Moves empty folder branches into a quarantine folder only when you pass `--apply`
> 
> Save as:
> 
> `gdrive_empty_folder_quarantine.py`
> 
> ```python
> #!/usr/bin/env python3
> """
> Quarantine effectively-empty folders from a Google Drive-synced folder.
> 
> A folder is considered empty if it contains only:
> - ignored junk files like desktop.ini
> - other folders that are also effectively empty
> 
> Default mode is DRY RUN. Nothing is moved unless --apply is passed.
> 
> Example:
>     python gdrive_empty_folder_quarantine.py "G:\\My Drive"
>     python gdrive_empty_folder_quarantine.py "G:\\My Drive" --apply
> """
> 
> from __future__ import annotations
> 
> import argparse
> import csv
> import os
> import shutil
> from dataclasses import dataclass
> from datetime import datetime
> from pathlib import Path
> 
> 
> DEFAULT_IGNORED_FILES = {
>     "desktop.ini",
>     ".ds_store",
>     "thumbs.db",
>     "ehthumbs.db",
>     "icon\r",
>     ".localized",
> }
> 
> 
> @dataclass
> class ScanResult:
>     path: Path
>     effectively_empty: bool
>     ignored_files: list[Path]
>     real_items: list[Path]
> 
> 
> def normalize_name(name: str) -> str:
>     return name.strip().lower()
> 
> 
> def is_ignored_file(path: Path, ignored_files: set[str]) -> bool:
>     return normalize_name(path.name) in ignored_files
> 
> 
> def is_inside(child: Path, parent: Path) -> bool:
>     try:
>         child.resolve().relative_to(parent.resolve())
>         return True
>     except ValueError:
>         return False
> 
> 
> def scan_directory(
>     directory: Path,
>     ignored_files: set[str],
>     excluded_dirs: list[Path],
>     results: dict[Path, ScanResult],
> ) -> bool:
>     """
>     Returns True if directory is effectively empty.
>     Conservative rule:
>     - Symlinks are treated as real items.
>     - Unknown access errors make a directory non-empty.
>     """
> 
>     ignored_found: list[Path] = []
>     real_items: list[Path] = []
>     child_dirs_empty = True
> 
>     try:
>         entries = list(os.scandir(directory))
>     except PermissionError:
>         real_items.append(directory / "[PERMISSION_DENIED]")
>         results[directory] = ScanResult(directory, False, ignored_found, real_items)
>         return False
> 
>     for entry in entries:
>         path = Path(entry.path)
> 
>         if any(is_inside(path, excluded) or path.resolve() == excluded.resolve() for excluded in excluded_dirs):
>             continue
> 
>         try:
>             if entry.is_symlink():
>                 real_items.append(path)
>                 continue
> 
>             if entry.is_file(follow_symlinks=False):
>                 if is_ignored_file(path, ignored_files):
>                     ignored_found.append(path)
>                 else:
>                     real_items.append(path)
>                 continue
> 
>             if entry.is_dir(follow_symlinks=False):
>                 child_empty = scan_directory(path, ignored_files, excluded_dirs, results)
>                 if not child_empty:
>                     child_dirs_empty = False
>                 continue
> 
>             # Anything weird gets treated as real to avoid accidental removal.
>             real_items.append(path)
> 
>         except OSError:
>             real_items.append(path)
> 
>     effectively_empty = child_dirs_empty and not real_items
> 
>     results[directory] = ScanResult(
>         path=directory,
>         effectively_empty=effectively_empty,
>         ignored_files=ignored_found,
>         real_items=real_items,
>     )
> 
>     return effectively_empty
> 
> 
> def get_topmost_empty_dirs(
>     root: Path,
>     results: dict[Path, ScanResult],
>     include_root: bool = False,
> ) -> list[Path]:
>     """
>     If an entire branch is empty, quarantine the top folder only.
>     This avoids moving child folders separately and making a mess.
>     """
> 
>     empty_dirs = [
>         path for path, result in results.items()
>         if result.effectively_empty and (include_root or path != root)
>     ]
> 
>     empty_dirs.sort(key=lambda p: len(p.parts))
> 
>     selected: list[Path] = []
> 
>     for path in empty_dirs:
>         already_covered = any(is_inside(path, chosen) or path == chosen for chosen in selected)
>         if not already_covered:
>             selected.append(path)
> 
>     return selected
> 
> 
> def unique_destination(dest: Path) -> Path:
>     if not dest.exists():
>         return dest
> 
>     counter = 2
>     while True:
>         candidate = dest.with_name(f"{dest.name}__{counter}")
>         if not candidate.exists():
>             return candidate
>         counter += 1
> 
> 
> def write_manifest(manifest_path: Path, planned_moves: list[tuple[Path, Path]]) -> None:
>     manifest_path.parent.mkdir(parents=True, exist_ok=True)
> 
>     with manifest_path.open("w", newline="", encoding="utf-8") as f:
>         writer = csv.writer(f)
>         writer.writerow(["original_path", "quarantine_path"])
> 
>         for original, quarantine in planned_moves:
>             writer.writerow([str(original), str(quarantine)])
> 
> 
> def quarantine_dirs(
>     root: Path,
>     dirs_to_move: list[Path],
>     quarantine_root: Path,
>     apply: bool,
> ) -> list[tuple[Path, Path]]:
>     planned_moves: list[tuple[Path, Path]] = []
> 
>     for directory in dirs_to_move:
>         relative = directory.relative_to(root)
>         destination = unique_destination(quarantine_root / relative)
>         planned_moves.append((directory, destination))
> 
>     if not apply:
>         return planned_moves
> 
>     quarantine_root.mkdir(parents=True, exist_ok=True)
> 
>     for original, destination in planned_moves:
>         destination.parent.mkdir(parents=True, exist_ok=True)
>         shutil.move(str(original), str(destination))
> 
>     return planned_moves
> 
> 
> def main() -> None:
>     parser = argparse.ArgumentParser(
>         description="Safely quarantine effectively-empty folders from a Google Drive folder."
>     )
> 
>     parser.add_argument(
>         "root",
>         help="Root folder to scan, for example: G:\\My Drive or /Users/me/Google Drive/My Drive",
>     )
> 
>     parser.add_argument(
>         "--apply",
>         action="store_true",
>         help="Actually move folders into quarantine. Without this, script only prints a dry run.",
>     )
> 
>     parser.add_argument(
>         "--quarantine-dir",
>         default=None,
>         help="Optional quarantine directory. Defaults to ROOT/.empty_folder_quarantine/TIMESTAMP",
>     )
> 
>     parser.add_argument(
>         "--ignore-file",
>         action="append",
>         default=[],
>         help="Additional filename to treat as junk/empty. Can be used more than once.",
>     )
> 
>     parser.add_argument(
>         "--include-root",
>         action="store_true",
>         help="Allow quarantining the root itself if it is empty. Off by default.",
>     )
> 
>     args = parser.parse_args()
> 
>     root = Path(args.root).expanduser().resolve()
> 
>     if not root.exists():
>         raise SystemExit(f"Root does not exist: {root}")
> 
>     if not root.is_dir():
>         raise SystemExit(f"Root is not a directory: {root}")
> 
>     timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
> 
>     if args.quarantine_dir:
>         quarantine_root = Path(args.quarantine_dir).expanduser().resolve()
>     else:
>         quarantine_root = root / ".empty_folder_quarantine" / timestamp
> 
>     ignored_files = set(DEFAULT_IGNORED_FILES)
>     ignored_files.update(normalize_name(name) for name in args.ignore_file)
> 
>     excluded_dirs = [
>         root / ".empty_folder_quarantine",
>         quarantine_root,
>     ]
> 
>     print("")
>     print("Scanning:")
>     print(f"  Root:       {root}")
>     print(f"  Mode:       {'APPLY / MOVE TO QUARANTINE' if args.apply else 'DRY RUN / NO CHANGES'}")
>     print(f"  Quarantine: {quarantine_root}")
>     print("")
> 
>     results: dict[Path, ScanResult] = {}
> 
>     scan_directory(
>         directory=root,
>         ignored_files=ignored_files,
>         excluded_dirs=excluded_dirs,
>         results=results,
>     )
> 
>     dirs_to_move = get_topmost_empty_dirs(
>         root=root,
>         results=results,
>         include_root=args.include_root,
>     )
> 
>     planned_moves = quarantine_dirs(
>         root=root,
>         dirs_to_move=dirs_to_move,
>         quarantine_root=quarantine_root,
>         apply=args.apply,
>     )
> 
>     print(f"Effectively empty folder branches found: {len(planned_moves)}")
>     print("")
> 
>     for original, destination in planned_moves:
>         print(f"{'[MOVE]' if args.apply else '[DRY] '} {original}")
>         print(f"       -> {destination}")
> 
>     if args.apply and planned_moves:
>         manifest_path = quarantine_root / "_manifest.csv"
>         write_manifest(manifest_path, planned_moves)
>         print("")
>         print(f"Manifest written: {manifest_path}")
> 
>     print("")
>     if not args.apply:
>         print("No changes made. Run again with --apply to quarantine these folders.")
>     else:
>         print("Done. Folders were moved to quarantine, not permanently deleted.")
> 
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ## Run it safely first
> 
> Dry run:
> 
> ```bash
> python gdrive_empty_folder_quarantine.py "G:\My Drive"
> ```
> 
> Actually quarantine:
> 
> ```bash
> python gdrive_empty_folder_quarantine.py "G:\My Drive" --apply
> ```
> 
> For a smaller test folder first, better:
> 
> ```bash
> python gdrive_empty_folder_quarantine.py "G:\My Drive\QiDrive" 
> python gdrive_empty_folder_quarantine.py "G:\My Drive\QiDrive" --apply
> ```
> 
> ## Important note
> 
> Do **not** aim this at the entire Google Drive root the first time unless you enjoy chaos cosplay. Test it on one project folder first. This script is conservative, but Google Drive can have weird sync artifacts, shortcuts, and placeholder files. The script treats anything besides your explicit junk list as real content, which is exactly what we want.

### User
> can i run this on its own without the toolbox

### Assistant
> Yes. **The script I gave you can run completely on its own without the toolbox.**
> 
> That standalone version does **not** need:
> 
> - `BaseTool`
> - `main_ui.py`
> - the builder
> - PyInstaller
> - the toolbox folder structure
> 
> It only uses Python’s standard library.
> 
> Run it like this:
> 
> ```bash
> python gdrive_empty_folder_quarantine.py "G:\My Drive"
> ```
> 
> Then live mode:
> 
> ```bash
> python gdrive_empty_folder_quarantine.py "G:\My Drive" --apply
> ```
> 
> ## The distinction
> 
> There are **two possible forms** of this tool:
> 
> | Version | Runs alone? | Used by toolbox? |
> |---|---:|---:|
> | Standalone CLI script | ✅ Yes | ❌ Not automatically |
> | Toolbox plugin class | ❌ Not cleanly by itself | ✅ Yes |
> 
> Your toolbox tools are expected to inherit from `BaseTool` and implement `get_name`, `build_ui`, and `execute` for the shell. That’s the plugin contract. fileciteturn0file0
> 
> Your builder is what scans `tools/<bucket>/<tool>/<tool>.py`, finds classes inheriting from `BaseTool`, injects them into `main_ui.py`, and builds the app. fileciteturn0file1 The developer guide confirms that structure is for toolbox tools, not standalone scripts. fileciteturn0file5
> 
> ## My recommendation
> 
> For this one: **keep both.**
> 
> Use the standalone script when you just need to clean Google Drive fast.
> 
> Then later wrap the same logic into:
> 
> ```txt
> tools/organize/gdrive_empty_folder_quarantine/gdrive_empty_folder_quarantine.py
> ```
> 
> That way:
> 
> - CLI version = emergency/manual use
> - Toolbox version = polished button inside QiOne
> 
> And yes, your current `main_ui.py` already shows a registered `GDriveEmptyFolderQuarantineTool`, so the toolbox side is either already started or already injected. fileciteturn0file6

### User
> make it interactive pleae and ready to download for me i want to run it from anwhere and select the folder it do a dry run first maybe create a csv file for me to review then ask me if i wnt to execute or cancel. or soemthign.

### Assistant
> I’ll package this as a **standalone interactive GUI script**: choose folder, dry-run scan, CSV review file, then a confirmation prompt before anything moves. No toolbox dependency, no silent deletion nonsense.

### Assistant
> Done. I made you a **standalone interactive version** — no toolbox needed.
> 
> Download the full package here:
> 
> [Download the standalone ZIP](sandbox:/mnt/data/gdrive_empty_folder_cleaner_standalone.zip)
> 
> Or just the Python file:
> 
> [Download the Python script](sandbox:/mnt/data/gdrive_empty_folder_cleaner_interactive.py)
> 
> ## What it does
> 
> - Opens a GUI
> - Lets you **select any folder**
> - Runs a **dry run first**
> - Creates CSV review files:
>   - `empty_folder_quarantine_plan.csv`
>   - `empty_folder_details.csv`
> - Lets you open/review the CSV
> - Runs a **fresh safety scan again** before executing
> - Asks for final confirmation
> - Moves folders into:
> 
> ```txt
> _QI_EMPTY_FOLDER_QUARANTINE
> ```
> 
> It does **not permanently delete anything**.
> 
> ## How to run
> 
> On Windows, unzip the package and double-click:
> 
> ```txt
> run_gdrive_empty_folder_cleaner.bat
> ```
> 
> Or run the Python file directly:
> 
> ```bash
> python gdrive_empty_folder_cleaner_interactive.py
> ```
> 
> Tiny warning: test this on a smaller Google Drive folder first before aiming it at all of `My Drive`. Not because the script is reckless — because Google Drive is weird and loves chaos.

### User
> its really really slow or got hung up.

### Assistant
> Yeah, that means I probably made it too “safe but chatty” for a huge Drive tree. Google Drive folders can look frozen because every nested `os.scandir()` hits sync/placeholder weirdness. I’m going to tighten it: background thread, visible heartbeat, faster pruning, scan limits, and a stop button.

### User
> it can just be in cmd

### Assistant
> CMD is the right call. The GUI added friction and made “is it frozen?” harder to tell. I’m making you a command-line version that prints progress, writes the review CSV, then asks: **execute / rescan / cancel**.

### Assistant
> Yep — **CMD version is better for this job.** I made you a replacement that should feel less “hung” because it prints progress while scanning.
> 
> Download it here:
> 
> [Download CMD version ZIP](sandbox:/mnt/data/gdrive_empty_folder_cleaner_cmd.zip)
> 
> Individual files:
> 
> [Python CMD script](sandbox:/mnt/data/gdrive_empty_folder_cleaner_cmd.py)  
> [Windows runner BAT](sandbox:/mnt/data/run_gdrive_empty_folder_cleaner_cmd.bat)  
> [README](sandbox:/mnt/data/README_gdrive_empty_folder_cleaner_cmd.txt)
> 
> ## What changed
> 
> - No GUI.
> - Runs from CMD.
> - Prompts you to paste the folder path.
> - Prints scan progress every few hundred folders.
> - Writes a CSV review file first.
> - Then asks:
> 
> ```txt
> E = execute this plan now
> R = rescan first
> O = open CSV review file
> C = cancel / exit
> ```
> 
> - Requires you to type:
> 
> ```txt
> MOVE
> ```
> 
> before it actually quarantines anything.
> 
> ## How to use
> 
> Unzip it anywhere, then double-click:
> 
> ```txt
> run_gdrive_empty_folder_cleaner_cmd.bat
> ```
> 
> Or from CMD:
> 
> ```bash
> python gdrive_empty_folder_cleaner_cmd.py
> ```
> 
> Or pass the folder directly:
> 
> ```bash
> python gdrive_empty_folder_cleaner_cmd.py "G:\My Drive"
> ```
> 
> ## Important
> 
> It moves empty branches into:
> 
> ```txt
> _QI_EMPTY_FOLDER_QUARANTINE
> ```
> 
> It still does **not delete permanently**. It also treats `.git`, `node_modules`, `.venv`, `.obsidian`, and similar heavy/system folders as **real content** by default so it doesn’t waste forever crawling them or accidentally flatten project guts.

### User
> {'asset_pointer': 'sediment://file_00000000fd04720caaebce8f6f660ad9', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 739, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 107993, 'width': 1605}OK LOOK AT ALL THESE FILES, I BET 1/2 ARE JUNK, HOW CAN I SYSTEMATICALLY7 CLEAN UP MY DRIVE.

### Assistant
> Yes. And the hard truth: **do not start “cleaning” by clicking around.** That is how people delete evidence, legal docs, exports, and one random folder that turns out to be the source of truth.
> 
> From your screenshot, the cleanup priority is obvious:
> 
> | Folder | Size | Why it matters |
> |---|---:|---|
> | `00_inbox` | **427 GB** | This is the beast. 57% of the drive. Start here. |
> | `_Private` | **275 GB** | 36% of the drive. Huge, but probably higher-risk. |
> | Everything else | ~53 GB | Mostly noise compared to the first two. |
> 
> So no, we are not cleaning “the drive.” We are cleaning **two monsters** first.
> 
> ---
> 
> # The Systematic Drive Cleanup Plan
> 
> ## Phase 1 — Audit, don’t delete
> 
> First, generate CSV reports:
> 
> 1. **Top largest files**
> 2. **Files by extension**
> 3. **Old files by modified date**
> 4. **Duplicate candidates**
> 5. **Empty folders**
> 6. **Likely junk folders**
> 7. **Root bucket summary**
> 
> You want a spreadsheet where every row says:
> 
> ```txt
> path, size, extension, modified date, category, risk level, recommended action
> ```
> 
> The goal is to make decisions from a table, not vibes.
> 
> ---
> 
> # Phase 2 — Use risk zones
> 
> ## Safe to auto-quarantine
> 
> These are usually trash:
> 
> ```txt
> desktop.ini
> Thumbs.db
> .DS_Store
> __MACOSX
> .tmp
> .temp
> .crdownload
> .part
> .partial
> .cache
> .pyc
> __pycache__
> node_modules
> .venv
> venv
> dist
> build
> .cache
> .ipynb_checkpoints
> ```
> 
> But even here: **quarantine, don’t delete.**
> 
> ---
> 
> ## Review before moving
> 
> These are suspicious but not automatically trash:
> 
> ```txt
> .zip
> .rar
> .7z
> .iso
> .exe
> .msi
> .mov
> .mp4
> .psd
> .ai
> figma exports
> copy files
> duplicate downloads
> screenshots
> old phone backups
> export folders
> ```
> 
> These probably contain a lot of bloat.
> 
> ---
> 
> ## Never auto-delete
> 
> Protect these:
> 
> ```txt
> 07_legal
> 06_finance
> 05_business
> 03_life
> 01_Qs_Journey
> .obsidian
> ```
> 
> These can be organized, deduped, archived, and indexed — but not casually nuked. Your future self will curse you.
> 
> ---
> 
> # Phase 3 — Attack `00_inbox` first
> 
> `00_inbox` is the dumping ground. It has:
> 
> ```txt
> 427 GB
> 2,062 folders
> 13,671 files
> ```
> 
> That is the cleanup battlefield.
> 
> Suggested process:
> 
> ## Pass A — Biggest files first
> 
> Sort `00_inbox` by size.
> 
> Anything over:
> 
> ```txt
> 500 MB
> 1 GB
> 5 GB
> 10 GB
> ```
> 
> gets reviewed first.
> 
> Why? Because deleting or archiving 50 giant files beats sorting 5,000 tiny PDFs like a raccoon with a spreadsheet.
> 
> ---
> 
> ## Pass B — Extension groups
> 
> Group by file type:
> 
> ```txt
> videos
> archives
> images
> PDFs
> docs
> code
> app installers
> unknown files
> ```
> 
> Then decide by category.
> 
> Example:
> 
> | Category | Action |
> |---|---|
> | Old installers | Quarantine |
> | Duplicate ZIP exports | Quarantine |
> | Phone videos | Move to `09_assets/media_review` |
> | PDFs | Route to legal/business/finance/life |
> | Screenshots | Review by date, then archive |
> | Unknown extension | Leave until inspected |
> 
> ---
> 
> ## Pass C — Inbox routing
> 
> Create only a few review folders:
> 
> ```txt
> 00_inbox/_REVIEW_BIG_FILES
> 00_inbox/_REVIEW_DUPLICATES
> 00_inbox/_REVIEW_ARCHIVES
> 00_inbox/_REVIEW_MEDIA
> 00_inbox/_REVIEW_DOCS
> 00_inbox/_QUARANTINE_CANDIDATES
> ```
> 
> Do **not** create 47 hyper-specific folders. That becomes a second mess wearing a wig.
> 
> ---
> 
> # Phase 4 — Handle `_Private` second
> 
> `_Private` is huge:
> 
> ```txt
> 275 GB
> 188 folders
> 17,012 files
> ```
> 
> This probably means fewer folders but very large contents.
> 
> For `_Private`, do **size audit first**, not filename cleanup.
> 
> Likely bloat:
> 
> ```txt
> phone backups
> videos
> old exports
> duplicate photo libraries
> cloud sync copies
> zip archives
> download dumps
> ```
> 
> But because it is private, treat it as **high-risk**.
> 
> Rule:
> 
> > Nothing in `_Private` gets deleted automatically. Only quarantine candidates after CSV review.
> 
> ---
> 
> # Phase 5 — Then clean the smaller folders
> 
> After `00_inbox` and `_Private`, then hit:
> 
> ```txt
> 09_assets       28 GB
> 07_legal        11 GB
> 05_business      7 GB
> 03_life          3 GB
> 10_data          1 GB
> 01_Qs_Journey    1 GB
> ```
> 
> The smaller folders may have many files, but they are not where your storage problem lives.
> 
> ---
> 
> # The cleanup pipeline I’d build
> 
> Honestly, the right tool is not just “empty folder remover.”
> 
> You need a **QiDrive Auditor**.
> 
> It should do this:
> 
> ## Step 1 — Scan
> 
> Produces:
> 
> ```txt
> qidrive_audit_summary.csv
> qidrive_largest_files.csv
> qidrive_extension_summary.csv
> qidrive_duplicate_candidates.csv
> qidrive_junk_candidates.csv
> qidrive_empty_folders.csv
> qidrive_old_files.csv
> ```
> 
> ## Step 2 — Recommend action
> 
> Each row gets a recommendation:
> 
> ```txt
> KEEP
> REVIEW
> ROUTE
> QUARANTINE
> IGNORE
> ```
> 
> ## Step 3 — User reviews CSV
> 
> You mark rows:
> 
> ```txt
> approved_action = QUARANTINE
> approved_action = KEEP
> approved_action = ROUTE
> ```
> 
> ## Step 4 — Execute approved rows only
> 
> The tool only moves files you explicitly approved.
> 
> That is the clean, adult version. No chaos goblin deleting.
> 
> ---
> 
> # Your immediate next move
> 
> Do this order:
> 
> ```txt
> 1. Audit 00_inbox
> 2. Pull top 500 largest files
> 3. Pull extension summary
> 4. Quarantine obvious junk
> 5. Review duplicate candidates
> 6. Repeat for _Private
> 7. Only then touch legal/business/life
> ```
> 
> Do **not** start with empty folders. Empty folders are cosmetic. Your real problem is **mass and duplication**.
> 
> The next tool you need is:
> 
> ```txt
> QiDrive Audit + Cleanup Planner
> ```
> 
> Not a deleter. A planner that makes CSVs first, then executes only what you approve.
