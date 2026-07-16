---
layout: page
title: "Code Review and Feedback"
slug: "code_review_and_feedback"
created_at: "2026-05-18 13:22:27"
updated_at: "2026-07-16T06:49:32-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-007.json"
template_key: master-template
date: 2026-05-18
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a0b58d8-9d28-83ea-ad0d-8866c55f8b17"
canonical_ref: ""
---

# Code Review and Feedback

## Overview
- **Date**: 2026-05-18 13:22:27
- **Conversation ID**: `6a0b58d8-9d28-83ea-ad0d-8866c55f8b17`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> what do you think about this code

### Assistant
> It’s **useful**, but it’s not ready as a trusted QiNexus/QiAccess sync tool yet. It’s a decent first-pass validator, not a safe production mover.
> 
> The good:
> 
> - It is interactive-first, which matches your rule: menu → scan → edit CSV → apply.
> - It avoids immediate destructive action. The CSV approval step is smart.
> - It creates `_index.md` when accepting folders into docs, which is aligned with your wiki/docs structure.
> - It skips common junk folders like `.hidden`, `node_modules`, and `__pycache__`.
> - It handles parent quarantine moves so it doesn’t repeatedly move child folders after the parent is gone.
> 
> The problem:
> 
> This script compares **QiNexus live storage** against **QiAccess repo docs** as if the folder trees should mirror each other. That is conceptually dangerous.
> 
> QiNexus is your storage backbone. QiAccess docs are your engineering/readable doctrine layer. They are related, but they should **not** be 1:1 mirrors. Your blueprint even separates Google Drive/QiNexus as storage from repo docs/Wiki.js as knowledge/app documentation. fileciteturn0file1
> 
> So the biggest flaw is not Python. It’s the premise.
> 
> ## My verdict
> 
> Use this as a **folder gap reporter**, not a sync authority.
> 
> Do **not** let it quarantine from `G:\My Drive\QiNexus` based only on “missing in docs.” That could move valid life/legal/finance/archive folders just because they do not belong in repo docs. That’s how we accidentally create chaos while trying to fight chaos. Rude but true.
> 
> ## Specific code issues
> 
> 1. **Quarantine is too aggressive**
> 
> `QUARANTINE` moves the actual source folder out of QiNexus. That’s a big destructive action. There is no dry-run preview after CSV edit except the count summary. It should print every planned move before confirmation.
> 
> 2. **No path safety validation**
> 
> The CSV can be edited manually, which means `rel_path` and `quarantine_target` are untrusted. The script should verify that:
> 
> - source is inside `DEFAULT_PATH1`
> - target is inside `DEFAULT_QUARANTINE`
> - no `..` path traversal exists
> - no absolute paths sneak into `rel_path`
> 
> Right now, a bad CSV row could move something unintended.
> 
> 3. **Folder mirroring is the wrong action**
> 
> For `ACCEPT`, it creates the same relative folder path inside docs and adds `_index.md`. But QiAccess docs should not mirror every QiNexus bucket/subfolder. Docs should explain structure, not duplicate storage.
> 
> Better action names:
> 
> - `DOCUMENT` — create a docs page describing this QiNexus folder
> - `IGNORE` — leave alone
> - `REVIEW` — needs human classification
> - `MOVE_WITHIN_QINEXUS` — future manifest action, but not this script
> - `QUARANTINE_DUPLICATE_OR_JUNK` — only after stronger checks
> 
> 4. **No sync pause**
> 
> You said this needs to pause for Drive syncing. This version does not really do that. It only pauses at menu points. Before and after moves, it should explicitly say: “Pause for Google Drive sync,” then wait for Enter.
> 
> 5. **No manifest/history log**
> 
> After apply, it should write an apply log like:
> 
> `sync_apply_log_YYYYMMDD_HHMMSS.csv`
> 
> with source, destination, action, status, timestamp, and error. Right now the terminal output is the only record.
> 
> 6. **Defaults are hardcoded**
> 
> That’s okay for *your* machine, but the script should display the defaults and allow override interactively. Especially because you use multiple roots and machines.
> 
> 7. **CSV only captures missing in path2**
> 
> It does not report:
> 
> - folders in docs missing from QiNexus
> - matching folders
> - ignored folders
> - possible renamed/moved folders
> - depth risk
> - empty folders
> - folders with only system junk
> 
> That’s fine for v0, but don’t call it “sync validator” yet. It’s a one-direction diff tool.
> 
> ## What I’d rename it
> 
> Current name vibe: **QiNexus Sync Validator**
> 
> Better name: **QiNexus Docs Gap Reviewer**
> 
> Because that is what it safely does.
> 
> ## What I would tell Codex to do
> 
> Have Codex refactor it into a safer workflow:
> 
> 1. Keep interactive menu.
> 2. Make `scan` generate a review manifest.
> 3. Replace `ACCEPT` with `DOCUMENT`.
> 4. Make quarantine disabled unless user turns on “danger mode.”
> 5. Add strict path safety checks.
> 6. Add dry-run preview.
> 7. Add before/after Google Drive sync pauses.
> 8. Add apply log.
> 9. Add config section at top with editable roots.
> 10. Never assume QiNexus and QiAccess docs should mirror 1:1.
> 
> The script is a good skeleton. The dangerous part is that it currently treats “not documented” like “maybe removable.” For your system, that’s backwards. Undocumented means **needs classification**, not **deserves quarantine**.

### User
> give me the updated code you would use for this if you built it.

### Assistant
> I’m going to keep this aligned with your actual rule: interactive prompts, CSV review manifest, no silent destructive moves, and quarantine locked behind an explicit danger switch.

### Assistant
> Yep. I would replace the current script with this safer version.
> 
> Key shift: this is now a **review + documentation gap tool**, not a fake “sync” tool that might bully QiNexus into matching repo docs. The old code was useful, but this version respects the source-of-truth split from your blueprint: QiNexus is storage; QiAccess docs explain the system. fileciteturn0file1
> 
> Save as:
> 
> `qinexus_docs_gap_reviewer.py`
> 
> ```python
> #!/usr/bin/env python3
> """
> qinexus_docs_gap_reviewer.py
> 
> Purpose:
>     Interactive QiNexus → QiAccess Docs gap reviewer.
> 
> Context:
>     This tool scans a live QiNexus storage tree and compares it against a
>     QiAccess documentation tree. It generates a CSV review manifest so Cody
>     can decide which QiNexus folders should receive documentation stubs.
> 
> Important Doctrine:
>     QiNexus and QiAccess docs are NOT expected to mirror 1:1.
> 
>     QiNexus = storage backbone / live file system.
>     QiAccess docs = source-of-truth documentation / explanation layer.
> 
>     Missing documentation does NOT mean a folder is junk.
>     Missing documentation means: review, classify, document, or ignore.
> 
> Safety Model:
>     - Interactive only.
>     - No command arguments required.
>     - Generates CSV manifest first.
>     - Applies only explicit actions from CSV.
>     - Quarantine is disabled unless danger mode is explicitly enabled.
>     - All apply runs create a log.
>     - Path traversal and unsafe CSV edits are blocked.
> """
> 
> import csv
> import os
> import shutil
> from dataclasses import dataclass
> from datetime import datetime
> from pathlib import Path
> 
> 
> # =============================================================================
> # CONFIG
> # =============================================================================
> 
> DEFAULT_QINEXUS_ROOT = Path(r"G:\My Drive\QiNexus")
> DEFAULT_DOCS_ROOT = Path(r"C:\QiLabs\_QiAccess_Start\docs")
> DEFAULT_QUARANTINE_ROOT = Path(r"G:\My Drive\_Quarantined\QiNexus_Docs_Gap_Review")
> 
> MANIFEST_PREFIX = "qinexus_docs_gap_manifest"
> APPLY_LOG_PREFIX = "qinexus_docs_gap_apply_log"
> 
> INDEX_FILENAME = "_index.md"
> 
> EXCLUDED_DIR_NAMES = {
>     ".git",
>     ".obsidian",
>     ".obsidian-qidocs",
>     ".vscode",
>     "__pycache__",
>     "node_modules",
>     "dist",
>     "build",
>     ".next",
>     ".turbo",
>     ".cache",
>     ".pytest_cache",
>     ".mypy_cache",
>     ".ruff_cache",
>     "venv",
>     ".venv",
>     "env",
>     ".env",
> }
> 
> VALID_ACTIONS = {
>     "",
>     "REVIEW",
>     "DOCUMENT",
>     "IGNORE",
>     "QUARANTINE",
> }
> 
> DANGER_MODE_ALLOW_QUARANTINE = False
> 
> 
> # =============================================================================
> # DATA STRUCTURES
> # =============================================================================
> 
> @dataclass
> class GapRow:
>     rel_path: str
>     status: str
>     action: str
>     docs_target: str
>     quarantine_target: str
>     note: str = ""
> 
> 
> @dataclass
> class ApplyResult:
>     rel_path: str
>     action: str
>     source: str
>     target: str
>     status: str
>     message: str
> 
> 
> # =============================================================================
> # UI HELPERS
> # =============================================================================
> 
> def print_header(title: str) -> None:
>     print()
>     print("=" * 72)
>     print(f" {title}")
>     print("=" * 72)
> 
> 
> def print_subheader(title: str) -> None:
>     print()
>     print("-" * 72)
>     print(title)
>     print("-" * 72)
> 
> 
> def pause(message: str = "Press Enter to continue...") -> None:
>     input(f"\n{message}")
> 
> 
> def sync_pause(stage: str) -> None:
>     print_header(f"Google Drive Sync Pause — {stage}")
>     print("Pause here so Google Drive has time to settle.")
>     print("Check Drive status if needed before continuing.")
>     pause("Press Enter when Drive sync looks calm...")
> 
> 
> def choose(prompt: str, options: list[tuple[str, str]], default_index: int = 0) -> str:
>     print()
>     print(prompt)
> 
>     for i, (_, label) in enumerate(options, start=1):
>         mark = "  [default]" if i - 1 == default_index else ""
>         print(f"  {i}. {label}{mark}")
> 
>     while True:
>         raw = input("Choose number: ").strip()
> 
>         if not raw:
>             return options[default_index][0]
> 
>         if raw.isdigit():
>             index = int(raw) - 1
>             if 0 <= index < len(options):
>                 return options[index][0]
> 
>         print("Invalid choice.")
> 
> 
> def yes_no(prompt: str, default: bool = False) -> bool:
>     suffix = "Y/n" if default else "y/N"
> 
>     while True:
>         answer = input(f"{prompt} [{suffix}]: ").strip().lower()
> 
>         if not answer:
>             return default
> 
>         if answer in {"y", "yes"}:
>             return True
> 
>         if answer in {"n", "no"}:
>             return False
> 
>         print("Please answer yes or no.")
> 
> 
> def get_path_interactive(label: str, default: Path) -> Path:
>     print()
>     raw = input(f"{label}\nDefault: {default}\nPath: ").strip().strip('"')
> 
>     if not raw:
>         return default
> 
>     return Path(raw)
> 
> 
> # =============================================================================
> # PATH SAFETY
> # =============================================================================
> 
> def normalize_rel_path(path_text: str) -> str:
>     clean = path_text.strip().replace("\\", "/")
> 
>     while clean.startswith("./"):
>         clean = clean[2:]
> 
>     return clean.strip("/")
> 
> 
> def is_bad_rel_path(rel_path: str) -> bool:
>     if not rel_path:
>         return True
> 
>     p = Path(rel_path)
> 
>     if p.is_absolute():
>         return True
> 
>     parts = p.parts
> 
>     if ".." in parts:
>         return True
> 
>     if any(part.strip() == "" for part in parts):
>         return True
> 
>     return False
> 
> 
> def safe_join(root: Path, rel_path: str) -> Path:
>     rel_path = normalize_rel_path(rel_path)
> 
>     if is_bad_rel_path(rel_path):
>         raise ValueError(f"Unsafe relative path blocked: {rel_path}")
> 
>     root_resolved = root.resolve()
>     candidate = (root_resolved / rel_path).resolve()
> 
>     try:
>         candidate.relative_to(root_resolved)
>     except ValueError as exc:
>         raise ValueError(f"Path escaped root and was blocked: {candidate}") from exc
> 
>     return candidate
> 
> 
> def ensure_target_inside_root(target: Path, root: Path) -> Path:
>     root_resolved = root.resolve()
>     target_resolved = target.resolve()
> 
>     try:
>         target_resolved.relative_to(root_resolved)
>     except ValueError as exc:
>         raise ValueError(f"Target escaped allowed root and was blocked: {target_resolved}") from exc
> 
>     return target_resolved
> 
> 
> # =============================================================================
> # SCANNING
> # =============================================================================
> 
> def should_skip_dir(dirname: str) -> bool:
>     if dirname in EXCLUDED_DIR_NAMES:
>         return True
> 
>     if dirname.startswith("."):
>         return True
> 
>     return False
> 
> 
> def collect_directories(root: Path) -> set[str]:
>     results: set[str] = set()
> 
>     for current_root, dirs, _files in os.walk(root):
>         dirs[:] = [d for d in dirs if not should_skip_dir(d)]
> 
>         rel = Path(current_root).relative_to(root)
> 
>         if str(rel) == ".":
>             continue
> 
>         rel_text = str(rel).replace("\\", "/")
>         results.add(rel_text)
> 
>     return results
> 
> 
> def scan_gaps(qinexus_root: Path, docs_root: Path, quarantine_root: Path) -> list[GapRow]:
>     print_header("Scanning QiNexus vs QiAccess Docs")
>     print(f"QiNexus root: {qinexus_root}")
>     print(f"Docs root:    {docs_root}")
>     print()
>     print("Reminder: this is a docs gap review.")
>     print("It does not assume the two trees should mirror each other.")
> 
>     qinexus_dirs = collect_directories(qinexus_root)
>     docs_dirs = collect_directories(docs_root)
> 
>     missing_docs = sorted(qinexus_dirs - docs_dirs)
> 
>     rows: list[GapRow] = []
> 
>     for rel in missing_docs:
>         docs_target = docs_root / rel / INDEX_FILENAME
>         quarantine_target = quarantine_root / rel
> 
>         rows.append(
>             GapRow(
>                 rel_path=rel,
>                 status="missing_in_docs",
>                 action="REVIEW",
>                 docs_target=str(docs_target).replace("\\", "/"),
>                 quarantine_target=str(quarantine_target).replace("\\", "/"),
>                 note="",
>             )
>         )
> 
>     return rows
> 
> 
> # =============================================================================
> # CSV
> # =============================================================================
> 
> def timestamp() -> str:
>     return datetime.now().strftime("%Y%m%d_%H%M%S")
> 
> 
> def write_manifest(rows: list[GapRow]) -> Path:
>     out_path = Path(f"{MANIFEST_PREFIX}_{timestamp()}.csv")
> 
>     with out_path.open("w", newline="", encoding="utf-8") as f:
>         writer = csv.DictWriter(
>             f,
>             fieldnames=[
>                 "rel_path",
>                 "status",
>                 "action",
>                 "docs_target",
>                 "quarantine_target",
>                 "note",
>             ],
>         )
>         writer.writeheader()
> 
>         for row in rows:
>             writer.writerow(
>                 {
>                     "rel_path": row.rel_path,
>                     "status": row.status,
>                     "action": row.action,
>                     "docs_target": row.docs_target,
>                     "quarantine_target": row.quarantine_target,
>                     "note": row.note,
>                 }
>             )
> 
>     return out_path
> 
> 
> def find_manifests() -> list[Path]:
>     return sorted(
>         Path(".").glob(f"{MANIFEST_PREFIX}_*.csv"),
>         key=lambda p: p.stat().st_mtime,
>         reverse=True,
>     )
> 
> 
> def choose_manifest() -> Path | None:
>     manifests = find_manifests()
> 
>     if not manifests:
>         print("No manifest CSV files found.")
>         return None
> 
>     print()
>     print("Available manifests:")
> 
>     visible = manifests[:10]
> 
>     for i, path in enumerate(visible, start=1):
>         print(f"  {i}. {path.name}")
> 
>     while True:
>         raw = input("Choose manifest number, or Enter to cancel: ").strip()
> 
>         if not raw:
>             return None
> 
>         if raw.isdigit():
>             index = int(raw) - 1
> 
>             if 0 <= index < len(visible):
>                 return visible[index]
> 
>         print("Invalid choice.")
> 
> 
> def read_manifest(path: Path) -> list[GapRow]:
>     rows: list[GapRow] = []
> 
>     with path.open("r", encoding="utf-8-sig", newline="") as f:
>         reader = csv.DictReader(f)
> 
>         required = {
>             "rel_path",
>             "status",
>             "action",
>             "docs_target",
>             "quarantine_target",
>             "note",
>         }
> 
>         missing = required - set(reader.fieldnames or [])
> 
>         if missing:
>             raise ValueError(f"Manifest is missing required columns: {sorted(missing)}")
> 
>         for row in reader:
>             rel_path = normalize_rel_path(row.get("rel_path", ""))
>             action = row.get("action", "").strip().upper()
> 
>             if action not in VALID_ACTIONS:
>                 raise ValueError(
>                     f"Invalid action '{action}' for path '{rel_path}'. "
>                     f"Valid actions: {sorted(VALID_ACTIONS)}"
>                 )
> 
>             if is_bad_rel_path(rel_path):
>                 raise ValueError(f"Unsafe rel_path in manifest: {rel_path}")
> 
>             rows.append(
>                 GapRow(
>                     rel_path=rel_path,
>                     status=row.get("status", "").strip(),
>                     action=action,
>                     docs_target=row.get("docs_target", "").strip(),
>                     quarantine_target=row.get("quarantine_target", "").strip(),
>                     note=row.get("note", "").strip(),
>                 )
>             )
> 
>     return rows
> 
> 
> def write_apply_log(results: list[ApplyResult]) -> Path:
>     out_path = Path(f"{APPLY_LOG_PREFIX}_{timestamp()}.csv")
> 
>     with out_path.open("w", newline="", encoding="utf-8") as f:
>         writer = csv.DictWriter(
>             f,
>             fieldnames=[
>                 "rel_path",
>                 "action",
>                 "source",
>                 "target",
>                 "status",
>                 "message",
>             ],
>         )
>         writer.writeheader()
> 
>         for result in results:
>             writer.writerow(
>                 {
>                     "rel_path": result.rel_path,
>                     "action": result.action,
>                     "source": result.source,
>                     "target": result.target,
>                     "status": result.status,
>                     "message": result.message,
>                 }
>             )
> 
>     return out_path
> 
> 
> # =============================================================================
> # DOCUMENTATION STUBS
> # =============================================================================
> 
> def title_from_rel_path(rel_path: str) -> str:
>     name = Path(rel_path).name
>     name = name.replace("_", " ").replace("-", " ")
>     return " ".join(part.capitalize() for part in name.split())
> 
> 
> def build_index_content(rel_path: str, source_root_name: str = "QiNexus") -> str:
>     title = title_from_rel_path(rel_path)
> 
>     return f"""---
> title: {title}
> source_system: {source_root_name}
> source_path: {rel_path}
> doc_type: qinexus_folder_stub
> status: draft
> created: {datetime.now().strftime("%Y-%m-%d")}
> ---
> 
> # {title}
> 
> ## Purpose
> 
> Describe what this QiNexus folder is for.
> 
> ## Source Folder
> 
> `{rel_path}`
> 
> ## Placement Rule
> 
> Explain what belongs here and what does not belong here.
> 
> ## Related Systems
> 
> - QiNexus
> - QiAccess Start
> - Wiki.js
> 
> ## Notes
> 
> This page was generated by `qinexus_docs_gap_reviewer.py` and needs human review.
> """
> 
> 
> def document_folder(row: GapRow, docs_root: Path) -> ApplyResult:
>     rel = row.rel_path
> 
>     try:
>         target_dir = safe_join(docs_root, rel)
>         index_file = target_dir / INDEX_FILENAME
> 
>         target_dir.mkdir(parents=True, exist_ok=True)
> 
>         if index_file.exists():
>             return ApplyResult(
>                 rel_path=rel,
>                 action="DOCUMENT",
>                 source="",
>                 target=str(index_file),
>                 status="SKIPPED",
>                 message="_index.md already exists.",
>             )
> 
>         index_file.write_text(build_index_content(rel), encoding="utf-8")
> 
>         return ApplyResult(
>             rel_path=rel,
>             action="DOCUMENT",
>             source="",
>             target=str(index_file),
>             status="OK",
>             message="Created documentation stub.",
>         )
> 
>     except Exception as exc:
>         return ApplyResult(
>             rel_path=rel,
>             action="DOCUMENT",
>             source="",
>             target="",
>             status="ERROR",
>             message=str(exc),
>         )
> 
> 
> # =============================================================================
> # QUARANTINE
> # =============================================================================
> 
> def quarantine_folder(
>     row: GapRow,
>     qinexus_root: Path,
>     quarantine_root: Path,
> ) -> ApplyResult:
>     rel = row.rel_path
> 
>     try:
>         source = safe_join(qinexus_root, rel)
>         target = safe_join(quarantine_root, rel)
>         target = ensure_target_inside_root(target, quarantine_root)
> 
>         if not source.exists():
>             return ApplyResult(
>                 rel_path=rel,
>                 action="QUARANTINE",
>                 source=str(source),
>                 target=str(target),
>                 status="SKIPPED",
>                 message="Source does not exist.",
>             )
> 
>         if target.exists():
>             suffix = datetime.now().strftime("%Y%m%d_%H%M%S")
>             target = target.with_name(f"{target.name}__{suffix}")
> 
>         target.parent.mkdir(parents=True, exist_ok=True)
>         shutil.move(str(source), str(target))
> 
>         return ApplyResult(
>             rel_path=rel,
>             action="QUARANTINE",
>             source=str(source),
>             target=str(target),
>             status="OK",
>             message="Moved folder to quarantine.",
>         )
> 
>     except Exception as exc:
>         return ApplyResult(
>             rel_path=rel,
>             action="QUARANTINE",
>             source="",
>             target="",
>             status="ERROR",
>             message=str(exc),
>         )
> 
> 
> def collapse_child_quarantine_rows(rows: list[GapRow]) -> list[GapRow]:
>     quarantine_rows = [r for r in rows if r.action == "QUARANTINE"]
>     quarantine_rows.sort(key=lambda r: len(r.rel_path.split("/")))
> 
>     kept: list[GapRow] = []
>     moved_parents: set[str] = set()
> 
>     for row in quarantine_rows:
>         rel = row.rel_path
> 
>         if any(rel.startswith(parent + "/") for parent in moved_parents):
>             continue
> 
>         kept.append(row)
>         moved_parents.add(rel)
> 
>     non_quarantine = [r for r in rows if r.action != "QUARANTINE"]
> 
>     return non_quarantine + kept
> 
> 
> # =============================================================================
> # COMMANDS
> # =============================================================================
> 
> def run_scan() -> None:
>     print_header("Create Review Manifest")
> 
>     qinexus_root = get_path_interactive("QiNexus root", DEFAULT_QINEXUS_ROOT)
>     docs_root = get_path_interactive("QiAccess docs root", DEFAULT_DOCS_ROOT)
>     quarantine_root = get_path_interactive("Quarantine root", DEFAULT_QUARANTINE_ROOT)
> 
>     if not qinexus_root.exists():
>         print(f"QiNexus root does not exist: {qinexus_root}")
>         pause()
>         return
> 
>     if not docs_root.exists():
>         print(f"Docs root does not exist: {docs_root}")
>         pause()
>         return
> 
>     rows = scan_gaps(qinexus_root, docs_root, quarantine_root)
> 
>     print()
>     print(f"Found {len(rows)} QiNexus folders missing matching docs folders.")
> 
>     if not rows:
>         print("No docs gaps found.")
>         pause()
>         return
> 
>     manifest = write_manifest(rows)
> 
>     print()
>     print(f"Manifest created: {manifest.resolve()}")
>     print()
>     print("Open the CSV and set action to one of:")
>     print("  REVIEW      keep for later review")
>     print("  DOCUMENT    create docs folder + _index.md stub")
>     print("  IGNORE      intentionally do nothing")
>     print("  QUARANTINE  move folder out of QiNexus — danger mode required")
>     print()
>     print("Default action is REVIEW.")
>     print("Nothing moves until Apply is run.")
> 
>     pause()
> 
> 
> def summarize_actions(rows: list[GapRow]) -> None:
>     counts = {
>         "REVIEW": 0,
>         "DOCUMENT": 0,
>         "IGNORE": 0,
>         "QUARANTINE": 0,
>         "": 0,
>     }
> 
>     for row in rows:
>         counts[row.action] = counts.get(row.action, 0) + 1
> 
>     print()
>     print("Plan Summary:")
>     print(f"  DOCUMENT:    {counts.get('DOCUMENT', 0)}")
>     print(f"  QUARANTINE:  {counts.get('QUARANTINE', 0)}")
>     print(f"  IGNORE:      {counts.get('IGNORE', 0)}")
>     print(f"  REVIEW:      {counts.get('REVIEW', 0)}")
>     print(f"  blank:       {counts.get('', 0)}")
> 
> 
> def preview_rows(rows: list[GapRow], action: str, limit: int = 30) -> None:
>     selected = [row for row in rows if row.action == action]
> 
>     if not selected:
>         return
> 
>     print_subheader(f"Preview: {action}")
> 
>     for row in selected[:limit]:
>         print(f"  - {row.rel_path}")
> 
>     if len(selected) > limit:
>         print(f"  ... and {len(selected) - limit} more")
> 
> 
> def run_apply() -> None:
>     print_header("Apply Manifest Actions")
> 
>     manifest = choose_manifest()
> 
>     if manifest is None:
>         return
> 
>     try:
>         rows = read_manifest(manifest)
>     except Exception as exc:
>         print(f"Manifest error: {exc}")
>         pause()
>         return
> 
>     rows = collapse_child_quarantine_rows(rows)
> 
>     actionable = [r for r in rows if r.action in {"DOCUMENT", "QUARANTINE"}]
> 
>     summarize_actions(rows)
>     preview_rows(rows, "DOCUMENT")
>     preview_rows(rows, "QUARANTINE")
> 
>     if not actionable:
>         print()
>         print("No actionable rows found. Use DOCUMENT or QUARANTINE in the action column.")
>         pause()
>         return
> 
>     qinexus_root = get_path_interactive("QiNexus root", DEFAULT_QINEXUS_ROOT)
>     docs_root = get_path_interactive("QiAccess docs root", DEFAULT_DOCS_ROOT)
>     quarantine_root = get_path_interactive("Quarantine root", DEFAULT_QUARANTINE_ROOT)
> 
>     if not qinexus_root.exists():
>         print(f"QiNexus root does not exist: {qinexus_root}")
>         pause()
>         return
> 
>     if not docs_root.exists():
>         print(f"Docs root does not exist: {docs_root}")
>         pause()
>         return
> 
>     has_quarantine = any(r.action == "QUARANTINE" for r in actionable)
> 
>     if has_quarantine and not DANGER_MODE_ALLOW_QUARANTINE:
>         print_header("Quarantine Blocked")
>         print("This script contains QUARANTINE rows, but danger mode is OFF.")
>         print()
>         print("That is intentional.")
>         print("Missing docs does not prove a QiNexus folder is junk.")
>         print()
>         print("To enable quarantine, edit the script:")
>         print("  DANGER_MODE_ALLOW_QUARANTINE = True")
>         print()
>         print("Then rerun Apply.")
>         pause()
>         return
> 
>     if has_quarantine:
>         print_header("Danger Zone")
>         print("QUARANTINE will MOVE folders out of QiNexus.")
>         print("This is not a documentation action.")
>         print("Only continue if you already verified these are junk, duplicates, or unsafe clutter.")
> 
>         if not yes_no("Do you understand this will move live folders?", default=False):
>             print("Aborted.")
>             pause()
>             return
> 
>     if not yes_no("Apply these actions now?", default=False):
>         print("Aborted.")
>         pause()
>         return
> 
>     sync_pause("Before Apply")
> 
>     results: list[ApplyResult] = []
> 
>     for row in actionable:
>         if row.action == "DOCUMENT":
>             result = document_folder(row, docs_root)
>             results.append(result)
>             print(f"[{result.status}] DOCUMENT {row.rel_path} — {result.message}")
> 
>         elif row.action == "QUARANTINE":
>             result = quarantine_folder(row, qinexus_root, quarantine_root)
>             results.append(result)
>             print(f"[{result.status}] QUARANTINE {row.rel_path} — {result.message}")
> 
>     log_path = write_apply_log(results)
> 
>     sync_pause("After Apply")
> 
>     print_header("Apply Complete")
>     print(f"Apply log written: {log_path.resolve()}")
> 
>     ok_count = sum(1 for r in results if r.status == "OK")
>     skipped_count = sum(1 for r in results if r.status == "SKIPPED")
>     error_count = sum(1 for r in results if r.status == "ERROR")
> 
>     print()
>     print(f"OK:      {ok_count}")
>     print(f"Skipped: {skipped_count}")
>     print(f"Errors:  {error_count}")
> 
>     pause()
> 
> 
> def run_show_doctrine() -> None:
>     print_header("Tool Doctrine")
>     print("This tool reviews documentation gaps.")
>     print()
>     print("It does NOT assume:")
>     print("  - QiNexus folders should all exist in repo docs")
>     print("  - missing docs means a folder is junk")
>     print("  - repo docs should mirror storage")
>     print()
>     print("Safe default flow:")
>     print("  1. Scan")
>     print("  2. Review CSV")
>     print("  3. DOCUMENT only the folders that need explanation")
>     print("  4. IGNORE normal storage folders that do not need docs")
>     print("  5. Use QUARANTINE only for verified junk or duplicates")
>     pause()
> 
> 
> # =============================================================================
> # MAIN MENU
> # =============================================================================
> 
> def main() -> None:
>     while True:
>         print_header("QiNexus Docs Gap Reviewer")
> 
>         action = choose(
>             "Choose an action",
>             [
>                 ("scan", "Scan QiNexus and create review manifest"),
>                 ("apply", "Apply DOCUMENT / QUARANTINE actions from manifest"),
>                 ("doctrine", "Show tool doctrine"),
>                 ("exit", "Exit"),
>             ],
>             default_index=0,
>         )
> 
>         if action == "scan":
>             run_scan()
> 
>         elif action == "apply":
>             run_apply()
> 
>         elif action == "doctrine":
>             run_show_doctrine()
> 
>         elif action == "exit":
>             print("Done.")
>             break
> 
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> What changed from the original version you uploaded: it no longer treats missing docs as a reason to move folders, it defaults everything to `REVIEW`, it adds path safety checks, it writes an apply log, it pauses for Drive sync, and quarantine is blocked unless you intentionally flip the danger switch. That’s the sane version. Your original had the right skeleton, but this one has guardrails. fileciteturn0file0
