---
layout: page
title: "FCFCU Front Matter Config"
slug: "fcfcu_front_matter_config"
created_at: "2026-03-08 20:07:57"
updated_at: "2026-03-08 20:07:57"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-004.json"
template_key: master-template
date: 2026-03-08
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69ae1d59-6d3c-8332-a97d-8f4cff1961b4"
canonical_ref: ""
---

# FCFCU Front Matter Config

## Overview
- **Date**: 2026-03-08 20:07:57
- **Conversation ID**: `69ae1d59-6d3c-8332-a97d-8f4cff1961b4`
- **Source**: `Chat-Export-28513-2026/conversations-004.json`

## Chat History

### User
> ok for my fcfcu case, i have a ton of items with inconsistent missing from matter, first i need to make sure there is some sort of config, then we can address retifying missing front matter and normalizing front matter entries.

### Assistant
> Yes. Do it in that order or you’ll create a bigger mess.
> 
> ## The right sequence
> 
> 1. **Define one canonical front matter schema**
> 2. **Create a config that enforces it**
> 3. **Audit all files against that config**
> 4. **Backfill missing front matter**
> 5. **Normalize values and aliases**
> 6. **Lock it down so it stops drifting again**
> 
> If you start “fixing files” before the schema is locked, you’ll just be cleaning the same kitchen twice.
> 
> ---
> 
> ## Phase 1: create the config first
> 
> You need a single source of truth. Not vibes. Not “I usually use this field.” A real schema.
> 
> I’d use one root file like:
> 
> `config/frontmatter.schema.yaml`
> 
> Example starter shape:
> 
> ```yaml
> version: 1
> applies_to:
>   - "**/*.md"
> 
> required_fields:
>   - title
>   - document_id
>   - status
>   - created
>   - updated
>   - category
> 
> optional_fields:
>   - matter
>   - matter_id
>   - client
>   - project
>   - tags
>   - source
>   - author
>   - related_entities
>   - confidentiality
>   - aliases
>   - summary
> 
> field_types:
>   title: string
>   document_id: string
>   status: string
>   created: date
>   updated: date
>   category: string
>   matter: string
>   matter_id: string
>   client: string
>   project: string
>   tags: list
>   source: string
>   author: string
>   related_entities: list
>   confidentiality: string
>   aliases: list
>   summary: string
> 
> allowed_values:
>   status:
>     - draft
>     - active
>     - review
>     - final
>     - archived
>   confidentiality:
>     - public
>     - internal
>     - confidential
>     - privileged
> 
> canonical_fields:
>   doc_id: document_id
>   id: document_id
>   matter_name: matter
>   case: matter
>   case_name: matter
>   date_created: created
>   date_updated: updated
>   type: category
> 
> defaults:
>   status: draft
>   confidentiality: internal
>   tags: []
>   aliases: []
> 
> empty_as_missing:
>   - ""
>   - null
>   - "N/A"
>   - "na"
>   - "none"
>   - "unknown"
> 
> normalizers:
>   trim_strings: true
>   lowercase_fields:
>     - status
>     - confidentiality
>   title_case_fields:
>     - matter
>     - client
>     - project
>   dedupe_lists:
>     - tags
>     - aliases
>     - related_entities
> 
> rules:
>   require_one_of:
>     - ["matter", "project", "client"]
>   forbid_extra_fields: false
> ```
> 
> ---
> 
> ## What this config needs to do
> 
> It should answer these questions, explicitly:
> 
> - What fields are **required**
> - What fields are **optional**
> - Which old field names map to new ones
> - What values are allowed
> - What defaults should be injected
> - What counts as “missing”
> - What formatting rules apply
> - Whether extra fields are allowed or flagged
> 
> That gives you a machine-checkable contract.
> 
> ---
> 
> ## Phase 2: audit before touching anything
> 
> You need a report first.
> 
> Generate something like:
> 
> `reports/frontmatter_audit.csv`
> 
> Columns:
> 
> ```csv
> file_path,has_frontmatter,missing_required_fields,unknown_fields,empty_fields,alias_fields_found,invalid_values,needs_normalization
> ```
> 
> And maybe a summary report:
> 
> ```md
> # Front Matter Audit Summary
> 
> - Total files scanned:
> - Files with no front matter:
> - Files missing required fields:
> - Files with alias fields:
> - Files with invalid enum values:
> - Files with inconsistent matter values:
> ```
> 
> This tells you the actual shape of the problem instead of guessing.
> 
> ---
> 
> ## Phase 3: rectify missing front matter
> 
> There are 3 buckets:
> 
> ### 1. No front matter at all
> Inject a full block with placeholders/defaults.
> 
> Example:
> 
> ```yaml
> ---
> title: "PLACEHOLDER_TITLE"
> document_id: "PLACEHOLDER_DOC_ID"
> status: draft
> created: 2026-03-08
> updated: 2026-03-08
> category: "uncategorized"
> matter: "PLACEHOLDER_MATTER"
> tags: []
> confidentiality: internal
> summary: ""
> ---
> ```
> 
> ### 2. Partial front matter
> Backfill only missing required fields.
> 
> ### 3. Wrong field names
> Map aliases to canonical names, then remove the alias fields.
> 
> ---
> 
> ## Phase 4: normalize entries
> 
> This is where the real rot is.
> 
> Typical garbage you’ll want to normalize:
> 
> - `case`, `matter`, `matter_name`, `Case Name` → `matter`
> - `id`, `doc_id`, `documentId` → `document_id`
> - `Draft`, `draft`, `DRAFT` → `draft`
> - `FCFCU`, `Financial Center`, `Financial Center First CU`, `Financial Center First Credit Union` → one canonical label
> - date formats like `3/8/26`, `2026/03/08`, `March 8 2026` → `2026-03-08`
> 
> For your case specifically, I’d define a canonical matter dictionary too.
> 
> Example:
> 
> `config/matter_map.yaml`
> 
> ```yaml
> canonical_matters:
>   FCFCU_Foreclosure:
>     aliases:
>       - FCFCU
>       - Financial Center
>       - Financial Center First
>       - Financial Center First Credit Union
>       - FCFCU Case
>       - foreclosure case
> ```
> 
> That way every file touching this case gets normalized to the same matter value instead of fifty variations.
> 
> ---
> 
> ## Phase 5: lock it down
> 
> Once normalized, you need enforcement or this all slides back into chaos.
> 
> Minimum controls:
> 
> - pre-commit or script check for markdown files
> - reject missing required fields
> - reject alias fields
> - reject invalid enum values
> - auto-fix formatting where safe
> - emit a report instead of silently mutating when confidence is low
> 
> ---
> 
> ## Best file layout for this
> 
> I’d structure it like this:
> 
> ```text
> config/
>   frontmatter.schema.yaml
>   matter_map.yaml
>   field_aliases.yaml
>   enum_values.yaml
> 
> scripts/
>   frontmatter/
>     audit_frontmatter.py
>     fix_missing_frontmatter.py
>     normalize_frontmatter.py
>     validate_frontmatter.py
> 
> reports/
>   frontmatter_audit.csv
>   frontmatter_summary.md
> ```
> 
> That keeps schema, transforms, and outputs separate. Cleaner and easier to maintain.
> 
> ---
> 
> ## Practical normalization order
> 
> Do it in this exact order:
> 
> 1. **Audit**
> 2. **Inject missing front matter**
> 3. **Rename alias fields**
> 4. **Fill defaults**
> 5. **Normalize enums and case names**
> 6. **Normalize dates**
> 7. **Deduplicate list fields**
> 8. **Re-audit**
> 9. **Validate hard**
> 
> That sequence matters.
> 
> ---
> 
> ## My recommendation for your FCFU/FCFCU matter field
> 
> Pick one canonical value and stop letting variations exist.
> 
> I’d use:
> 
> ```yaml
> matter: FCFCU_Foreclosure
> ```
> 
> or if you want it more human-readable:
> 
> ```yaml
> matter: Financial Center First Credit Union Foreclosure
> ```
> 
> But choose one. One. Not both.
> 
> If you want both machine-readable and pretty, do:
> 
> ```yaml
> matter_id: FCFCU_Foreclosure
> matter: Financial Center First Credit Union Foreclosure
> ```
> 
> That’s better.
> 
> ---
> 
> ## What not to do
> 
> Do **not** start by manually editing files one by one. That is ADHD bait and a time sink.
> 
> Do **not** normalize values before alias mapping. You’ll miss half the field drift.
> 
> Do **not** make `matter` free-text forever if this repo is becoming a system. That guarantees entropy.
> 
> ---
> 
> ## Clean next move
> 
> Your next concrete artifact should be:
> 
> 1. `frontmatter.schema.yaml`
> 2. `matter_map.yaml`
> 3. `frontmatter_audit.py`
> 
> After that, the fixer scripts.
> 
> I can draft the actual canonical schema plus the alias map for your case repo right now in copy-paste form.

### User
> hun you going to give me a script to pull a front matter manifest, better yet why not a full manifest with all front matter and event body for that matter into csv then we map it to update field in csv them systematically do ea dry run then apply.

### Assistant
> Yes. That is the smarter way.
> 
> Do **not** mutate the files first.  
> Pull a **manifest CSV** first, review and map changes in tabular form, run a **dry run**, then apply. That gives you traceability, rollback logic, and less chaos.
> 
> ## Recommended flow
> 
> **Pass 1**
> - scan all markdown files
> - extract:
>   - file path
>   - existing front matter
>   - body preview
>   - body hash
>   - full body text
> - flatten front matter into CSV columns
> - output a manifest
> 
> **Pass 2**
> - you edit the CSV
> - add normalized target values in `new_*` columns
> 
> **Pass 3**
> - script reads CSV
> - dry run shows exact per-file changes
> - apply mode writes only approved changes
> - optional backup per file
> 
> ---
> 
> ## Suggested files
> 
> ```text
> scripts/frontmatter/
>   export_manifest.py
>   apply_manifest.py
> 
> data/manifests/
>   frontmatter_manifest.csv
>   frontmatter_manifest_reviewed.csv
> 
> reports/
>   manifest_dry_run.csv
>   manifest_apply_log.csv
> ```
> 
> ---
> 
> ## CSV structure I recommend
> 
> Core identity columns:
> 
> - `file_path`
> - `file_name`
> - `document_id`
> - `body_sha256`
> - `has_frontmatter`
> - `parse_error`
> 
> Body columns:
> 
> - `body_excerpt`
> - `body_full`
> 
> Existing FM columns:
> 
> - `fm_title`
> - `fm_status`
> - `fm_created`
> - `fm_updated`
> - `fm_category`
> - `fm_matter`
> - `fm_matter_id`
> - `fm_tags`
> - `fm_summary`
> 
> Catch-all columns:
> 
> - `fm_raw_yaml`
> - `fm_extra_json`
> 
> Target columns you edit:
> 
> - `new_title`
> - `new_status`
> - `new_created`
> - `new_updated`
> - `new_category`
> - `new_matter`
> - `new_matter_id`
> - `new_tags`
> - `new_summary`
> - `new_document_id`
> 
> Control columns:
> 
> - `action`
> - `notes`
> 
> Where `action` can be:
> - `skip`
> - `update_frontmatter`
> - `replace_frontmatter`
> - `inject_frontmatter`
> 
> ---
> 
> ## Script 1: export full manifest to CSV
> 
> This script:
> - walks a repo
> - parses YAML front matter if present
> - exports known FM fields
> - stores unknown FM in JSON
> - includes body excerpt and full body
> - includes body hash for safety
> 
> ```python
> #!/usr/bin/env python3
> """
> export_manifest.py
> 
> Scan markdown files, extract front matter + body, and export a CSV manifest
> for review and bulk normalization.
> 
> Usage:
>   python export_manifest.py --root "C:/path/to/repo" --out "data/manifests/frontmatter_manifest.csv"
> """
> 
> from __future__ import annotations
> 
> import argparse
> import csv
> import hashlib
> import json
> import re
> from pathlib import Path
> from typing import Any, Dict, Tuple
> 
> try:
>     import yaml
> except ImportError:
>     raise SystemExit("Missing dependency: pyyaml\nInstall with: pip install pyyaml")
> 
> KNOWN_FIELDS = [
>     "title",
>     "document_id",
>     "status",
>     "created",
>     "updated",
>     "category",
>     "matter",
>     "matter_id",
>     "client",
>     "project",
>     "tags",
>     "source",
>     "author",
>     "related_entities",
>     "confidentiality",
>     "aliases",
>     "summary",
> ]
> 
> CSV_COLUMNS = [
>     "file_path",
>     "file_name",
>     "has_frontmatter",
>     "parse_error",
>     "body_sha256",
>     "body_excerpt",
>     "body_full",
>     "fm_raw_yaml",
>     "fm_extra_json",
> ]
> 
> CSV_COLUMNS += [f"fm_{field}" for field in KNOWN_FIELDS]
> 
> CSV_COLUMNS += [
>     "new_title",
>     "new_document_id",
>     "new_status",
>     "new_created",
>     "new_updated",
>     "new_category",
>     "new_matter",
>     "new_matter_id",
>     "new_client",
>     "new_project",
>     "new_tags",
>     "new_source",
>     "new_author",
>     "new_related_entities",
>     "new_confidentiality",
>     "new_aliases",
>     "new_summary",
>     "action",
>     "notes",
> ]
> 
> 
> FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
> 
> 
> def sha256_text(text: str) -> str:
>     return hashlib.sha256(text.encode("utf-8")).hexdigest()
> 
> 
> def normalize_value_for_csv(value: Any) -> str:
>     if value is None:
>         return ""
>     if isinstance(value, (list, dict)):
>         return json.dumps(value, ensure_ascii=False)
>     return str(value)
> 
> 
> def parse_markdown_file(path: Path) -> Tuple[bool, str, Dict[str, Any], str, str]:
>     """
>     Returns:
>       has_frontmatter, parse_error, frontmatter_dict, raw_yaml, body
>     """
>     text = path.read_text(encoding="utf-8", errors="replace")
>     match = FRONTMATTER_RE.match(text)
> 
>     if not match:
>         return False, "", {}, "", text
> 
>     raw_yaml = match.group(1)
>     body = text[match.end():]
> 
>     try:
>         data = yaml.safe_load(raw_yaml) or {}
>         if not isinstance(data, dict):
>             return True, "frontmatter_not_mapping", {}, raw_yaml, body
>         return True, "", data, raw_yaml, body
>     except Exception as exc:
>         return True, f"yaml_parse_error: {exc}", {}, raw_yaml, body
> 
> 
> def build_row(path: Path, root: Path) -> Dict[str, str]:
>     has_frontmatter, parse_error, fm, raw_yaml, body = parse_markdown_file(path)
> 
>     row: Dict[str, str] = {
>         "file_path": str(path.relative_to(root)).replace("\\", "/"),
>         "file_name": path.name,
>         "has_frontmatter": "true" if has_frontmatter else "false",
>         "parse_error": parse_error,
>         "body_sha256": sha256_text(body),
>         "body_excerpt": body[:500].replace("\r\n", "\n").replace("\r", "\n"),
>         "body_full": body,
>         "fm_raw_yaml": raw_yaml,
>         "fm_extra_json": "",
>         "action": "skip",
>         "notes": "",
>     }
> 
>     extra: Dict[str, Any] = {}
> 
>     for key, value in fm.items():
>         if key in KNOWN_FIELDS:
>             row[f"fm_{key}"] = normalize_value_for_csv(value)
>         else:
>             extra[key] = value
> 
>     for field in KNOWN_FIELDS:
>         row.setdefault(f"fm_{field}", "")
> 
>     row["fm_extra_json"] = json.dumps(extra, ensure_ascii=False)
> 
>     for target_col in [c for c in CSV_COLUMNS if c.startswith("new_")]:
>         row.setdefault(target_col, "")
> 
>     return row
> 
> 
> def main() -> None:
>     parser = argparse.ArgumentParser()
>     parser.add_argument("--root", required=True, help="Root folder to scan")
>     parser.add_argument("--out", required=True, help="Output CSV path")
>     args = parser.parse_args()
> 
>     root = Path(args.root).resolve()
>     out_path = Path(args.out).resolve()
>     out_path.parent.mkdir(parents=True, exist_ok=True)
> 
>     files = sorted(root.rglob("*.md"))
> 
>     with out_path.open("w", encoding="utf-8-sig", newline="") as f:
>         writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore", quoting=csv.QUOTE_ALL)
>         writer.writeheader()
> 
>         for path in files:
>             row = build_row(path, root)
>             writer.writerow(row)
> 
>     print(f"Exported {len(files)} markdown files to: {out_path}")
> 
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ---
> 
> ## Script 2: apply reviewed CSV back to files
> 
> This script:
> - reads your reviewed CSV
> - compares `new_*` values against current front matter
> - supports `--dry-run`
> - supports `--apply`
> - supports `--backup-dir`
> - refuses to apply if body hash changed since export, unless forced
> 
> ```python
> #!/usr/bin/env python3
> """
> apply_manifest.py
> 
> Apply reviewed front matter updates from a manifest CSV back to markdown files.
> 
> Usage:
>   python apply_manifest.py --root "C:/path/to/repo" --csv "data/manifests/frontmatter_manifest_reviewed.csv" --dry-run --report "reports/manifest_dry_run.csv"
> 
>   python apply_manifest.py --root "C:/path/to/repo" --csv "data/manifests/frontmatter_manifest_reviewed.csv" --apply --backup-dir "backups/frontmatter" --report "reports/manifest_apply_log.csv"
> """
> 
> from __future__ import annotations
> 
> import argparse
> import csv
> import hashlib
> import json
> import shutil
> import re
> from pathlib import Path
> from typing import Any, Dict, Tuple, List
> 
> try:
>     import yaml
> except ImportError:
>     raise SystemExit("Missing dependency: pyyaml\nInstall with: pip install pyyaml")
> 
> KNOWN_FIELDS = [
>     "title",
>     "document_id",
>     "status",
>     "created",
>     "updated",
>     "category",
>     "matter",
>     "matter_id",
>     "client",
>     "project",
>     "tags",
>     "source",
>     "author",
>     "related_entities",
>     "confidentiality",
>     "aliases",
>     "summary",
> ]
> 
> FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
> 
> 
> def sha256_text(text: str) -> str:
>     return hashlib.sha256(text.encode("utf-8")).hexdigest()
> 
> 
> def parse_markdown_file(path: Path) -> Tuple[bool, Dict[str, Any], str, str]:
>     text = path.read_text(encoding="utf-8", errors="replace")
>     match = FRONTMATTER_RE.match(text)
> 
>     if not match:
>         return False, {}, "", text
> 
>     raw_yaml = match.group(1)
>     body = text[match.end():]
>     try:
>         fm = yaml.safe_load(raw_yaml) or {}
>         if not isinstance(fm, dict):
>             fm = {}
>     except Exception:
>         fm = {}
> 
>     return True, fm, raw_yaml, body
> 
> 
> def decode_csv_value(value: str) -> Any:
>     value = (value or "").strip()
>     if value == "":
>         return ""
> 
>     # Try JSON first for lists/dicts
>     if (value.startswith("[") and value.endswith("]")) or (value.startswith("{") and value.endswith("}")):
>         try:
>             return json.loads(value)
>         except Exception:
>             pass
> 
>     return value
> 
> 
> def build_new_frontmatter(existing_fm: Dict[str, Any], row: Dict[str, str]) -> Dict[str, Any]:
>     new_fm = dict(existing_fm)
> 
>     for field in KNOWN_FIELDS:
>         new_key = f"new_{field}"
>         if new_key not in row:
>             continue
> 
>         raw_value = row.get(new_key, "")
>         if raw_value == "":
>             continue
> 
>         value = decode_csv_value(raw_value)
>         new_fm[field] = value
> 
>     # Clean blank strings for known fields if action is replace_frontmatter
>     return new_fm
> 
> 
> def render_markdown(frontmatter: Dict[str, Any], body: str) -> str:
>     yaml_text = yaml.safe_dump(
>         frontmatter,
>         sort_keys=False,
>         allow_unicode=True,
>         default_flow_style=False,
>         width=1000,
>     ).strip()
> 
>     return f"---\n{yaml_text}\n---\n\n{body.lstrip()}"
> 
> 
> def diff_fields(old: Dict[str, Any], new: Dict[str, Any]) -> List[str]:
>     keys = sorted(set(old.keys()) | set(new.keys()))
>     changes: List[str] = []
> 
>     for key in keys:
>         if old.get(key) != new.get(key):
>             changes.append(key)
> 
>     return changes
> 
> 
> def main() -> None:
>     parser = argparse.ArgumentParser()
>     parser.add_argument("--root", required=True, help="Root folder of repo")
>     parser.add_argument("--csv", required=True, help="Reviewed manifest CSV")
>     parser.add_argument("--report", required=True, help="Output log CSV")
>     parser.add_argument("--dry-run", action="store_true")
>     parser.add_argument("--apply", action="store_true")
>     parser.add_argument("--backup-dir", help="Optional backup directory")
>     parser.add_argument("--force-body-hash", action="store_true", help="Apply even if body hash changed")
>     args = parser.parse_args()
> 
>     if not args.dry_run and not args.apply:
>         raise SystemExit("Choose either --dry-run or --apply")
> 
>     root = Path(args.root).resolve()
>     csv_path = Path(args.csv).resolve()
>     report_path = Path(args.report).resolve()
>     report_path.parent.mkdir(parents=True, exist_ok=True)
> 
>     backup_dir = Path(args.backup_dir).resolve() if args.backup_dir else None
>     if backup_dir:
>         backup_dir.mkdir(parents=True, exist_ok=True)
> 
>     results = []
> 
>     with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
>         reader = csv.DictReader(f)
> 
>         for row in reader:
>             action = (row.get("action") or "").strip().lower()
>             if action not in {"inject_frontmatter", "update_frontmatter", "replace_frontmatter"}:
>                 continue
> 
>             rel_path = row["file_path"]
>             file_path = (root / rel_path).resolve()
> 
>             result = {
>                 "file_path": rel_path,
>                 "action": action,
>                 "status": "",
>                 "changed_fields": "",
>                 "message": "",
>             }
> 
>             if not file_path.exists():
>                 result["status"] = "error"
>                 result["message"] = "file_not_found"
>                 results.append(result)
>                 continue
> 
>             has_fm, current_fm, _, body = parse_markdown_file(file_path)
>             current_hash = sha256_text(body)
>             manifest_hash = (row.get("body_sha256") or "").strip()
> 
>             if manifest_hash and current_hash != manifest_hash and not args.force_body_hash:
>                 result["status"] = "skipped"
>                 result["message"] = "body_hash_mismatch"
>                 results.append(result)
>                 continue
> 
>             if action == "replace_frontmatter":
>                 new_fm = {}
>             else:
>                 new_fm = dict(current_fm)
> 
>             new_fm = build_new_frontmatter(new_fm, row)
> 
>             # Optional: preserve unknown fields unless replace_frontmatter
>             changed = diff_fields(current_fm, new_fm)
>             result["changed_fields"] = json.dumps(changed, ensure_ascii=False)
> 
>             if not changed and has_fm:
>                 result["status"] = "skipped"
>                 result["message"] = "no_changes"
>                 results.append(result)
>                 continue
> 
>             new_text = render_markdown(new_fm, body)
> 
>             if args.dry_run:
>                 result["status"] = "dry_run"
>                 result["message"] = "would_update"
>                 results.append(result)
>                 continue
> 
>             if backup_dir:
>                 backup_target = backup_dir / rel_path
>                 backup_target.parent.mkdir(parents=True, exist_ok=True)
>                 shutil.copy2(file_path, backup_target)
> 
>             file_path.write_text(new_text, encoding="utf-8", newline="\n")
> 
>             result["status"] = "applied"
>             result["message"] = "updated"
>             results.append(result)
> 
>     with report_path.open("w", encoding="utf-8-sig", newline="") as f:
>         writer = csv.DictWriter(
>             f,
>             fieldnames=["file_path", "action", "status", "changed_fields", "message"],
>             quoting=csv.QUOTE_ALL,
>         )
>         writer.writeheader()
>         writer.writerows(results)
> 
>     print(f"Wrote report: {report_path}")
>     print(f"Processed rows: {len(results)}")
> 
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ---
> 
> ## How to use it
> 
> ### 1. Export the manifest
> 
> ```bash
> python scripts/frontmatter/export_manifest.py --root "C:/FCFCU_CASE" --out "data/manifests/frontmatter_manifest.csv"
> ```
> 
> ### 2. Open the CSV
> Filter and edit these columns:
> 
> - `action`
> - `new_*`
> 
> Example:
> 
> | file_path | fm_matter | new_matter | action |
> |---|---:|---:|---:|
> | `C-01/foo.md` | `FCFCU` | `Financial Center First Credit Union Foreclosure` | `update_frontmatter` |
> 
> ### 3. Dry run
> 
> ```bash
> python scripts/frontmatter/apply_manifest.py --root "C:/FCFCU_CASE" --csv "data/manifests/frontmatter_manifest_reviewed.csv" --dry-run --report "reports/manifest_dry_run.csv"
> ```
> 
> ### 4. Apply for real
> 
> ```bash
> python scripts/frontmatter/apply_manifest.py --root "C:/FCFCU_CASE" --csv "data/manifests/frontmatter_manifest_reviewed.csv" --apply --backup-dir "backups/frontmatter_2026-03-08" --report "reports/manifest_apply_log.csv"
> ```
> 
> ---
> 
> ## My blunt recommendation
> 
> Do **one extra pass** before applying:
> - normalize aliases in CSV first
> - do not hand-edit raw YAML in the file system
> - do not trust free-text `matter` values
> - keep `matter_id` separate from display `matter`
> 
> For your case, I’d likely standardize around:
> 
> ```text
> matter_id = FCFCU_FORECLOSURE
> matter = Financial Center First Credit Union Foreclosure
> ```
> 
> That gives you a stable machine key and a readable label.
> 
> ---
> 
> ## One upgrade you probably want next
> 
> Add a third script:
> 
> `build_mapping_template.py`
> 
> That would:
> - scan all distinct existing values
> - output a mapping CSV like:
> 
> ```csv
> field,old_value,new_value
> matter,FCFCU,Financial Center First Credit Union Foreclosure
> matter,Financial Center,Financial Center First Credit Union Foreclosure
> status,Draft,draft
> status,FINAL,final
> ```
> 
> That makes normalization way faster than editing file rows one by one.
> 
> That’s the real power move here.
> 
> If you want, I’ll give you **version 2** next: a tighter set of scripts that also generates a **distinct values mapping CSV** for `matter`, `status`, `category`, and `tags`, so you can normalize this repo without losing your mind.

### User
> the path to the content is here, G:\My Drive\QiVault\30_projects\CASES\30.05.01_CASE_FCFCU\content,  where do i updat that in the python script, also how can i also set which plugins for obsidian shoudl be on and what their settign shoudl be?

### Assistant
> Update it in the **command you run**, not hardcoded in the script unless you want that as the default.
> 
> ## For your path
> 
> Use this when running the export script:
> 
> ```bash
> python scripts/frontmatter/export_manifest.py --root "G:\My Drive\QiVault\30_projects\CASES\30.05.01_CASE_FCFCU\content" --out "data\manifests\frontmatter_manifest.csv"
> ```
> 
> And for apply:
> 
> ```bash
> python scripts/frontmatter/apply_manifest.py --root "G:\My Drive\QiVault\30_projects\CASES\30.05.01_CASE_FCFCU\content" --csv "data\manifests\frontmatter_manifest_reviewed.csv" --dry-run --report "reports\manifest_dry_run.csv"
> ```
> 
> Then real apply:
> 
> ```bash
> python scripts/frontmatter/apply_manifest.py --root "G:\My Drive\QiVault\30_projects\CASES\30.05.01_CASE_FCFCU\content" --csv "data\manifests\frontmatter_manifest_reviewed.csv" --apply --backup-dir "backups\frontmatter_2026-03-08" --report "reports\manifest_apply_log.csv"
> ```
> 
> ## Where to change it inside the script
> 
> If you want a built-in default path, change this part:
> 
> ```python
> parser.add_argument("--root", required=True, help="Root folder to scan")
> ```
> 
> to this:
> 
> ```python
> parser.add_argument(
>     "--root",
>     default=r"G:\My Drive\QiVault\30_projects\CASES\30.05.01_CASE_FCFCU\content",
>     help="Root folder to scan",
> )
> ```
> 
> Then it no longer needs `required=True`.
> 
> Same idea in `apply_manifest.py`:
> 
> ```python
> parser.add_argument(
>     "--root",
>     default=r"G:\My Drive\QiVault\30_projects\CASES\30.05.01_CASE_FCFCU\content",
>     help="Root folder of repo",
> )
> ```
> 
> But honestly, passing it in the command is cleaner. Hardcoding paths gets ugly fast.
> 
> ---
> 
> # Obsidian plugins and settings
> 
> Yes, you can control that too. Obsidian stores most of that in the vault’s `.obsidian` folder.
> 
> ## Main files that matter
> 
> Inside your vault:
> 
> ```text
> .obsidian/
>   app.json
>   appearance.json
>   community-plugins.json
>   core-plugins.json
>   hotkeys.json
>   workspace.json
>   graph.json
>   templates.json
>   daily-notes.json
>   backlinks.json
>   page-preview.json
>   command-palette.json
>   ...
>   plugins/
>     plugin-id-1/
>       data.json
>     plugin-id-2/
>       data.json
> ```
> 
> ## What controls what
> 
> ### Core plugins enabled
> This file controls Obsidian’s built-in plugins:
> 
> ```text
> .obsidian/core-plugins.json
> ```
> 
> Example:
> 
> ```json
> [
>   "file-explorer",
>   "search",
>   "starred",
>   "backlink",
>   "outgoing-link",
>   "tag-pane",
>   "properties",
>   "templates",
>   "daily-notes",
>   "command-palette"
> ]
> ```
> 
> ### Community plugins enabled
> This file controls which community plugins are turned on:
> 
> ```text
> .obsidian/community-plugins.json
> ```
> 
> Example:
> 
> ```json
> [
>   "dataview",
>   "templater-obsidian",
>   "obsidian-linter",
>   "metadata-menu",
>   "buttons"
> ]
> ```
> 
> ### Community plugin settings
> Each plugin usually stores settings here:
> 
> ```text
> .obsidian/plugins/<plugin-id>/data.json
> ```
> 
> Example:
> 
> ```text
> .obsidian/plugins/obsidian-linter/data.json
> .obsidian/plugins/templater-obsidian/data.json
> .obsidian/plugins/dataview/data.json
> ```
> 
> That means yes, you can absolutely define:
> - which plugins should be enabled
> - which core plugins should be enabled
> - each plugin’s settings
> 
> ---
> 
> # Best way to manage this cleanly
> 
> Do **not** manually click around forever in the UI if you want consistency.
> 
> Create a vault config package like this:
> 
> ```text
> config/obsidian/
>   core-plugins.json
>   community-plugins.json
>   app.json
>   hotkeys.json
>   plugins/
>     obsidian-linter/data.json
>     templater-obsidian/data.json
>     metadata-menu/data.json
> ```
> 
> Then use a sync script to push those files into:
> 
> ```text
> <your vault>\.obsidian\
> ```
> 
> ---
> 
> # Simple Python sync script
> 
> This will copy your standard config into the vault.
> 
> ```python
> #!/usr/bin/env python3
> from pathlib import Path
> import shutil
> 
> SOURCE = Path(r"G:\My Drive\QiVault\30_projects\CASES\30.05.01_CASE_FCFCU\config\obsidian")
> VAULT = Path(r"G:\My Drive\QiVault\30_projects\CASES\30.05.01_CASE_FCFCU\content\.obsidian")
> 
> def copy_tree(src: Path, dst: Path) -> None:
>     for item in src.rglob("*"):
>         rel = item.relative_to(src)
>         target = dst / rel
> 
>         if item.is_dir():
>             target.mkdir(parents=True, exist_ok=True)
>         else:
>             target.parent.mkdir(parents=True, exist_ok=True)
>             shutil.copy2(item, target)
>             print(f"Copied: {item} -> {target}")
> 
> if __name__ == "__main__":
>     if not SOURCE.exists():
>         raise SystemExit(f"Source config folder not found: {SOURCE}")
> 
>     VAULT.mkdir(parents=True, exist_ok=True)
>     copy_tree(SOURCE, VAULT)
>     print("Obsidian config sync complete.")
> ```
> 
> ---
> 
> # Recommended approach for your case vault
> 
> For a legal/evidence-heavy vault, I’d define:
> 
> ## Core plugins on
> - File explorer
> - Search
> - Backlinks
> - Outgoing links
> - Properties
> - Templates
> - Daily notes
> - Command palette
> - Page preview
> - Bookmarks
> 
> ## Community plugins worth considering
> - **Dataview** — query notes by frontmatter
> - **Templater** — repeatable note scaffolds
> - **Linter** — normalize YAML/frontmatter formatting
> - **Metadata Menu** — easier metadata editing
> - **Buttons** or **Commander** — optional convenience
> - **Kanban** only if you actually use it
> - **Excalidraw** only if visual mapping matters here
> - **Omnisearch** if built-in search feels too weak
> 
> Do **not** turn on thirty plugins just because they’re shiny. That’s how the vault turns into soup.
> 
> ---
> 
> # Practical answer to “how do I set their settings?”
> 
> Three ways:
> 
> ## 1. Manual once, then capture files
> Best option.
> 
> - set the plugins how you want inside Obsidian
> - close Obsidian
> - copy the resulting `.obsidian/*.json` files
> - save them as your standard config template
> 
> That’s the least stupid route because plugin settings vary wildly.
> 
> ## 2. Hand-edit JSON
> Works fine if you know the plugin IDs and setting schema.
> 
> ## 3. Scripted sync
> Best once you already have a known-good config.
> 
> ---
> 
> # What I would do in your shoes
> 
> For this FCFCU vault:
> 
> 1. get the manifest script working first using your `content` path
> 2. open the vault in Obsidian
> 3. configure the plugins manually one time
> 4. capture the `.obsidian` folder as your baseline
> 5. create a `config/obsidian/` template
> 6. sync it with script when needed
> 
> That way your content rules and your Obsidian behavior both become reproducible.
> 
> ## Cleanest command for you right now
> 
> ```bash
> python scripts/frontmatter/export_manifest.py --root "G:\My Drive\QiVault\30_projects\CASES\30.05.01_CASE_FCFCU\content" --out "G:\My Drive\QiVault\30_projects\CASES\30.05.01_CASE_FCFCU\data\manifests\frontmatter_manifest.csv"
> ```
> 
> One warning: if your script folder is **not** inside that case folder, keep the `--out` path absolute too, or the CSV will end up somewhere random and annoy you.
> 
> I can give you a **ready-to-use FCFCU Obsidian baseline config pack** next: core plugins list, community plugin list, and suggested settings for Dataview, Templater, Linter, and Metadata Menu.

### User
> right but i want it in the yaml incase the obisidan folder gets delted during clean up of the repo.

### Assistant
> Good instinct. Treat the **Obsidian config as declarative infrastructure**, not UI state.  
> Store the desired state in **YAML**, then generate `.obsidian` files from it. If the `.obsidian` folder gets nuked, you just regenerate it.
> 
> Think of it like **IaC but for your vault**.
> 
> ---
> 
> # 1. Create a YAML config
> 
> Create:
> 
> ```
> config/obsidian_config.yaml
> ```
> 
> Example:
> 
> ```yaml
> vault:
>   name: FCFCU_CASE
>   content_path: "G:/My Drive/QiVault/30_projects/CASES/30.05.01_CASE_FCFCU/content"
> 
> core_plugins:
>   - file-explorer
>   - search
>   - starred
>   - backlinks
>   - outgoing-link
>   - tag-pane
>   - properties
>   - templates
>   - daily-notes
>   - command-palette
>   - page-preview
>   - bookmarks
> 
> community_plugins:
>   - dataview
>   - templater-obsidian
>   - obsidian-linter
>   - metadata-menu
> 
> plugin_settings:
> 
>   templater-obsidian:
>     templates_folder: "_templates"
>     trigger_on_file_creation: true
> 
>   obsidian-linter:
>     format_on_save: true
>     yaml_sort_keys: false
>     yaml_array_style: "block"
> 
>   dataview:
>     enable_js: true
>     enable_inline_fields: true
> 
>   metadata-menu:
>     auto_sync: true
>     show_icons: true
> ```
> 
> ---
> 
> # 2. Python generator script
> 
> Create:
> 
> ```
> scripts/obsidian/generate_obsidian_config.py
> ```
> 
> This reads YAML and builds the `.obsidian` folder.
> 
> ```python
> #!/usr/bin/env python3
> 
> import json
> import yaml
> from pathlib import Path
> 
> CONFIG_PATH = Path("config/obsidian_config.yaml")
> 
> def load_config():
>     with open(CONFIG_PATH, "r", encoding="utf-8") as f:
>         return yaml.safe_load(f)
> 
> def write_json(path, data):
>     path.parent.mkdir(parents=True, exist_ok=True)
>     with open(path, "w", encoding="utf-8") as f:
>         json.dump(data, f, indent=2)
> 
> def main():
> 
>     config = load_config()
> 
>     vault_path = Path(config["vault"]["content_path"])
>     obsidian_path = vault_path / ".obsidian"
> 
>     obsidian_path.mkdir(exist_ok=True)
> 
>     # Core plugins
>     write_json(
>         obsidian_path / "core-plugins.json",
>         config.get("core_plugins", [])
>     )
> 
>     # Community plugins
>     write_json(
>         obsidian_path / "community-plugins.json",
>         config.get("community_plugins", [])
>     )
> 
>     # Plugin settings
>     plugin_settings = config.get("plugin_settings", {})
> 
>     for plugin, settings in plugin_settings.items():
> 
>         plugin_folder = obsidian_path / "plugins" / plugin
>         plugin_folder.mkdir(parents=True, exist_ok=True)
> 
>         write_json(plugin_folder / "data.json", settings)
> 
>     print("Obsidian config generated successfully.")
>     print(f"Vault path: {vault_path}")
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ---
> 
> # 3. Run it
> 
> ```
> python scripts/obsidian/generate_obsidian_config.py
> ```
> 
> It recreates:
> 
> ```
> content/.obsidian/
> ```
> 
> with:
> 
> ```
> .obsidian
>   core-plugins.json
>   community-plugins.json
>   plugins/
>      dataview/data.json
>      templater-obsidian/data.json
>      obsidian-linter/data.json
>      metadata-menu/data.json
> ```
> 
> ---
> 
> # 4. Add a repo rule (important)
> 
> Your repo should **ignore the generated folder**, but keep the YAML.
> 
> `.gitignore`
> 
> ```
> .obsidian/*
> !.obsidian/README.md
> ```
> 
> Then your repo structure becomes:
> 
> ```
> config/
>   obsidian_config.yaml
> 
> scripts/
>   obsidian/
>     generate_obsidian_config.py
> 
> content/
>   (notes here)
> 
> .obsidian/   ← generated, disposable
> ```
> 
> ---
> 
> # 5. Even better (for your workflow)
> 
> Add a **bootstrap script** that runs everything.
> 
> ```
> scripts/bootstrap_vault.py
> ```
> 
> Example:
> 
> ```python
> import subprocess
> 
> print("Generating Obsidian config...")
> subprocess.run(["python", "scripts/obsidian/generate_obsidian_config.py"])
> 
> print("Vault ready.")
> ```
> 
> Then one command restores everything.
> 
> ```
> python scripts/bootstrap_vault.py
> ```
> 
> ---
> 
> # 6. Why this is the right architecture
> 
> You now have:
> 
> | Layer | Source |
> |-----|------|
> Vault content | markdown |
> Vault structure | repo folders |
> Obsidian config | YAML |
> Runtime UI state | `.obsidian` |
> 
> If `.obsidian` is deleted:
> 
> ```
> run generator → vault restored
> ```
> 
> Exactly what you want.
> 
> ---
> 
> # 7. One improvement I strongly recommend
> 
> Add **frontmatter schema to the same YAML** so your vault rules live together.
> 
> Example:
> 
> ```yaml
> frontmatter_schema:
> 
>   required:
>     - title
>     - document_id
>     - status
>     - created
>     - category
>     - matter_id
> 
>   defaults:
>     status: draft
>     confidentiality: internal
> 
>   enums:
> 
>     status:
>       - draft
>       - active
>       - review
>       - final
>       - archived
> ```
> 
> Now one config file governs:
> 
> * Obsidian behavior
> * metadata rules
> * vault structure
> 
> ---
> 
> If you want, I can also give you a **much stronger version** of this system Cody would actually benefit from:
> 
> **QiVault Control System**
> 
> It would include:
> 
> • Obsidian YAML config  
> • frontmatter schema enforcement  
> • plugin auto install  
> • manifest generator  
> • CSV mapping engine  
> • vault health audit  
> 
> All driven from **one master YAML**.
> 
> It would make your FCFCU case vault **self-healing instead of fragile**.

### User
> really i need to get everything turned on and set up then copy the folder into a template on my mono repo to apply later, help me get all the plugins that we need and setup right theni can copy teh folder and we can then crate a script to create what we need from teh source later right.

### Assistant
> Yes. That is the right move.
> 
> **Do it live once inside the FCFCU vault, get it exactly how you want, then copy the `.obsidian` folder into your monorepo as the baseline template.** Obsidian stores vault configuration in the vault’s `.obsidian` folder, and core/community plugin activation plus plugin settings live there. Community plugins must be installed and enabled, and Restricted Mode has to be off to use them. citeturn0search0turn0search12
> 
> ## The clean plan
> 
> 1. Open the FCFCU vault.
> 2. Turn on the core plugins you actually need.
> 3. Install and configure the community plugins.
> 4. Close Obsidian fully.
> 5. Copy the finished `.obsidian` folder into your monorepo template area.
> 6. Later, script from that known-good source.
> 
> That beats trying to invent the config blind.
> 
> ---
> 
> ## What to turn on
> 
> ### Core plugins: turn these on
> These are built-in Obsidian features and are managed as core plugins. citeturn0search4turn0search8
> 
> Use this set for your legal/case vault:
> 
> - File explorer
> - Search
> - Backlinks
> - Outgoing links
> - Properties
> - Templates
> - Daily notes
> - Command palette
> - Page preview
> - Bookmarks
> 
> ### Core plugins: leave these off unless you actually use them
> - Canvas
> - Slides
> - Audio recorder
> - Workspaces
> - Random note
> - Publish
> 
> That keeps clutter down.
> 
> ---
> 
> ## Community plugins: install these first
> 
> ### 1. Dataview
> Dataview turns the vault into a queryable metadata/index layer, which is exactly what you want once front matter gets normalized. citeturn0search1turn0search5
> 
> Use it for:
> - case note indexes
> - exhibit lists
> - notes missing fields
> - status dashboards
> - timeline slices by date / phase / actor
> 
> ### 2. Templater
> Templater gives you reusable templates plus dynamic variables and scripting. citeturn0search2
> 
> Use it for:
> - note creation templates
> - case memo templates
> - exhibit note stubs
> - event/timeline entry templates
> - consistent file naming
> 
> ### 3. Linter
> Linter is specifically for keeping notes uniform, including YAML/frontmatter and markdown formatting. citeturn0search3turn0search7
> 
> Use it for:
> - front matter consistency
> - spacing cleanup
> - heading cleanup
> - preserving a standard file format
> 
> ### 4. Metadata Menu
> Use this if you want easier front matter editing in the UI. It is not mandatory, but it’s useful when you’re manually refining metadata after the bulk pass. Community plugins are installed through Obsidian’s Community plugins flow. citeturn0search0
> 
> ---
> 
> ## My actual recommendation: plugin stack
> 
> ### Required
> - Dataview
> - Templater
> - Linter
> 
> ### Strongly useful
> - Metadata Menu
> 
> ### Optional, only if you truly use them
> - Excalidraw
> - Omnisearch
> - Kanban
> 
> Do **not** install ten more “maybe useful” plugins right now. That is how you end up debugging the tool instead of the case.
> 
> ---
> 
> ## How to set them up
> 
> ### Dataview
> Turn it on and keep it pretty conservative at first.
> 
> Suggested settings:
> - enable inline fields: on
> - enable JavaScript queries: off at first, on later only if needed
> - refresh on changes: on
> 
> Reason: standard Dataview queries are enough for 90% of what you need. JS queries are powerful, but they also make things easier to break. Dataview’s core value is querying metadata and markdown pages as a live index. citeturn0search5turn0search1
> 
> ### Templater
> Suggested settings:
> - Templates folder location: `_templates`
> - Trigger Templater on new file creation: on
> - Folder templates: set later if you need folder-specific note types
> - Script folder: `_templates/scripts` only if you actually use JS scripts
> 
> This gives you clean structure without overcomplicating it. Templater is built around template variables/functions and optional JavaScript. citeturn0search2
> 
> ### Linter
> Suggested settings:
> - lint on save: on
> - yaml/frontmatter rules: on
> - keep key sorting off unless you want forced order
> - normalize spacing: on
> - heading cleanup: on
> - trailing spaces cleanup: on
> - blank lines consistency: on
> 
> Important: **do not** aggressively enable every YAML mutation rule until after your manifest pass. Linter is great for uniformity, but if you turn on too much before your metadata schema is stable, it can become a chaos multiplier. Linter explicitly supports YAML/frontmatter and markdown formatting rules. citeturn0search7turn0search3
> 
> ### Metadata Menu
> Suggested use:
> - only after front matter schema is decided
> - use it for manual corrections, not as your primary migration engine
> 
> ---
> 
> ## Folder structure I’d use inside the vault
> 
> ```text
> content/
>   _templates/
>     note_case_event.md
>     note_exhibit.md
>     note_motion.md
>     note_person.md
>     note_issue.md
>   _views/
>     missing_frontmatter.md
>     exhibit_index.md
>     event_timeline.md
>     witness_index.md
> ```
> 
> That gives Dataview and Templater somewhere sane to live.
> 
> ---
> 
> ## What to capture after setup
> 
> After you finish configuring the vault, copy these into your monorepo template source:
> 
> ```text
> .obsidian/
>   app.json
>   appearance.json
>   core-plugins.json
>   community-plugins.json
>   hotkeys.json
>   templates.json
>   daily-notes.json
>   page-preview.json
>   backlinks.json
>   command-palette.json
>   plugins/
>     dataview/data.json
>     templater-obsidian/data.json
>     obsidian-linter/data.json
>     metadata-menu/data.json
> ```
> 
> Obsidian Sync also treats core plugin lists, core plugin settings, and community plugin lists as configuration categories, which lines up with this folder-capture approach. citeturn0search12
> 
> ---
> 
> ## Best way to do this without wasting time
> 
> ### Session 1: baseline
> - install those 4 plugins
> - set the folders
> - turn on the core plugins
> - test one template
> - test one Dataview query
> - test Linter on one sacrificial note
> 
> ### Session 2: capture
> - close Obsidian
> - copy `.obsidian` into monorepo template folder
> - label it something like:
> 
> ```text
> templates/obsidian/fcfcu_case_v1/.obsidian/
> ```
> 
> ### Session 3: automate later
> Then we write the script that:
> - copies the baseline `.obsidian`
> - creates `_templates`
> - creates `_views`
> - optionally drops starter templates and starter Dataview dashboards
> 
> That is the sane order.
> 
> ---
> 
> ## My blunt opinion on your sequence
> 
> You do **not** need a YAML-driven config system first.
> 
> You need a **working vault first**.
> 
> Then you freeze it into a template.
> Then you abstract it.
> Then you automate it.
> 
> Trying to declaratively model plugin settings before you have the actual known-good files is backwards and annoying.
> 
> ---
> 
> ## Minimal starter Dataview notes you should make right away
> 
> ### Missing front matter tracker
> ```md
> ```dataview
> TABLE file.name AS File, file.folder AS Folder
> FROM ""
> WHERE !document_id OR !matter_id OR !status
> SORT file.name ASC
> ```
> ```
> 
> ### Event timeline
> ```md
> ```dataview
> TABLE event_date, title, status, actor
> FROM ""
> WHERE type = "event"
> SORT event_date ASC
> ```
> ```
> 
> ### Exhibit list
> ```md
> ```dataview
> TABLE exhibit_id, title, source, status
> FROM ""
> WHERE type = "exhibit"
> SORT exhibit_id ASC
> ```
> ```
> 
> Dataview is specifically meant for querying metadata and content across markdown pages. citeturn0search5turn0search1
> 
> ---
> 
> ## Your next move
> 
> Open the FCFCU vault and configure exactly these first:
> - core plugins listed above
> - Dataview
> - Templater
> - Linter
> - Metadata Menu
> 
> Then close Obsidian and copy the `.obsidian` folder into your monorepo template source.
> 
> After that, we turn it into a reproducible template/script without guessing.

### User
> we can also override the config file in obsidian that might be a good option for us, wait also i just realized something didnt i say i wanted to start using a differnt note taker that im runnin on railway?

### Assistant
> Yes — and you just caught an important architectural fork. Let's slow this down for a second because there are **two different layers** in what you're building:
> 
> 1. **Authoring / thinking environment**
> 2. **Knowledge storage / system of record**
> 
> Right now you’re mixing them.
> 
> ---
> 
> # The thing you remembered
> 
> Yes. You said you wanted to start using **Trilium** (hosted on Railway) as your note system.
> 
> Earlier you mentioned:
> 
> > if i host trilium on railway and connect it to the same postgres qiarchive uses
> 
> That means your **long-term system of record** would be Trilium + Postgres.
> 
> So Obsidian would become **optional**, not core.
> 
> ---
> 
> # Important difference
> 
> ### Obsidian
> - local markdown editor
> - vault based
> - metadata in YAML
> - plugin ecosystem
> - great thinking tool
> - terrible system of record
> 
> ### Trilium
> - database backed
> - hierarchical notes
> - built-in attributes
> - scripting
> - API
> - web access anywhere
> - real knowledge system
> 
> So if you run it on Railway, you already solved:
> 
> • mobile access  
> • hosting  
> • search  
> • structured attributes  
> 
> ---
> 
> # My honest recommendation for your stack
> 
> Use **both**, but with clear roles.
> 
> | Tool | Purpose |
> |-----|-----|
> Obsidian | drafting, thinking, writing |
> Trilium | canonical knowledge system |
> QiArchive | documents / evidence store |
> 
> Your stack becomes:
> 
> ```
> QiArchive
>    ↓
> Trilium (knowledge graph)
>    ↓
> Obsidian (authoring environment)
> ```
> 
> Obsidian becomes basically a **markdown IDE**.
> 
> ---
> 
> # What that means for your vault
> 
> You actually don't need to obsess over the perfect Obsidian setup anymore.
> 
> The vault only needs:
> 
> - minimal plugins
> - templating
> - frontmatter structure
> 
> Because the **real structure lives in Trilium**.
> 
> ---
> 
> # Minimal Obsidian stack if Trilium is the real system
> 
> You only need:
> 
> ### Keep
> 
> Dataview  
> Templater  
> Linter  
> 
> ### Optional
> 
> Metadata Menu
> 
> ### Remove entirely
> 
> Kanban  
> Excalidraw  
> Omnisearch  
> 30 other plugins
> 
> Let Obsidian stay **lightweight**.
> 
> ---
> 
> # How the workflow should look
> 
> ### Step 1 — capture
> 
> Write notes in Obsidian.
> 
> Example:
> 
> ```
> 2026-03-08_motion_interest_calculation.md
> ```
> 
> Frontmatter:
> 
> ```
> ---
> document_id: FCFCU_DOC_118
> type: motion
> matter_id: FCFCU_FORECLOSURE
> status: draft
> created: 2026-03-08
> ---
> ```
> 
> ---
> 
> ### Step 2 — ingest
> 
> Script pushes note → Trilium
> 
> Trilium becomes the structured system.
> 
> ---
> 
> ### Step 3 — query
> 
> Use Trilium:
> 
> - for dashboards
> - for relationships
> - for metadata
> - for linking evidence
> 
> ---
> 
> # Why this is actually perfect for you
> 
> Because Trilium supports:
> 
> • hierarchical notes  
> • attributes (like frontmatter)  
> • scripts  
> • REST API  
> • DB backend  
> 
> Which aligns with **QiArchive architecture**.
> 
> ---
> 
> # Where Obsidian still wins
> 
> Two things:
> 
> ### writing speed
> 
> Nothing beats Obsidian for:
> 
> - rapid writing
> - linking
> - markdown editing
> 
> ### offline
> 
> You can write anywhere.
> 
> Then sync.
> 
> ---
> 
> # Now about overriding Obsidian config
> 
> You are right.
> 
> You can override:
> 
> ```
> .obsidian/app.json
> .obsidian/core-plugins.json
> .obsidian/community-plugins.json
> .obsidian/plugins/*/data.json
> ```
> 
> But since you’re templating the vault anyway, the easiest thing is:
> 
> ```
> monorepo/
>    templates/
>        obsidian_vault/
>             .obsidian/
>             _templates/
>             _views/
> ```
> 
> Then a bootstrap script just copies it.
> 
> ---
> 
> # Here's the bigger architectural question
> 
> Before we go further:
> 
> ### Are you planning for Trilium to be
> 
> **A — your primary knowledge base**
> 
> or
> 
> **B — just a note tool running on Railway**
> 
> Because those are **two very different architectures**.
> 
> If it's **A**, we should design:
> 
> ```
> QiArchive
> Trilium
> Obsidian
> Paperless
> QiPortal
> ```
> 
> as one integrated system.
> 
> If it's **B**, then we keep focusing on the Obsidian vault as primary.
> 
> ---
> 
> # My gut feeling
> 
> Given everything you've built with:
> 
> • QiArchive  
> • entity-first thinking  
> • manifests  
> • automation  
> • Postgres  
> 
> Trilium fits your brain **much better than Obsidian**.
> 
> Obsidian is great for thinkers.
> 
> Trilium is great for **system builders**.
> 
> You're the second type.
> 
> ---
> 
> # If you want, I can show you something interesting next
> 
> How to turn your system into:
> 
> ```
> QiArchive = evidence layer
> Trilium = intelligence layer
> Postgres = structured layer
> Obsidian = drafting layer
> ```
> 
> Which would basically give you a **personal knowledge OS**.
> 
> And honestly?
> 
> You're about **one architectural decision away** from that already.

### User
> it was trillium that im using on railway but the ide wont be ablet o see an help me with it since it sits own server huh?

### Assistant
> Mostly yes.
> 
> If **Trilium is running on Railway as its own server**, your IDE is **not automatically going to see the live note content** the way it would see a local Obsidian vault folder. Trilium is designed around a database-backed knowledge base rather than flat markdown files, and it can run as a self-hosted server you sync to from clients. citeturn0search4turn0search10
> 
> So the split is:
> 
> - **Your IDE can see**
>   - the Trilium repo/code if you cloned it locally
>   - your deployment config
>   - scripts you write against Trilium
>   - exported files you keep locally
> 
> - **Your IDE cannot natively see**
>   - the live notes sitting inside the running Railway instance
>   - internal server-side note data unless you pull it out somehow
> 
> That is the important distinction.
> 
> ## What this means in practice
> 
> If your notes only exist **inside Trilium on the server**, then Cursor/VS Code/other IDE tools cannot just “look into” that knowledge base and help you structure or refactor it directly. They need one of these bridges:
> 
> ### Option 1: local export or mirror
> Export or sync Trilium content to local markdown/JSON files and let the IDE work on those.
> 
> This is the cleanest path if you want AI help with note content.
> 
> ### Option 2: API bridge
> Trilium exposes API-oriented capabilities and scripting/extensibility, so you can write tooling that reads notes out and pushes updates back. That means your IDE can help you by working on the **integration scripts**, not by magically seeing the server database directly. citeturn0search2turn0search16
> 
> ### Option 3: use Trilium as the app, not the editable source
> Treat Trilium as the runtime knowledge system and keep your “authoritative editable artifacts” in local files, then ingest them into Trilium.
> 
> That is usually the least painful architecture.
> 
> ## The blunt truth
> 
> If your goal is:
> 
> > “I want my IDE and AI assistant to help me heavily with my notes and structure”
> 
> then **server-only Trilium is a worse fit than local markdown**.
> 
> If your goal is:
> 
> > “I want a web-accessible, structured note system I can reach anywhere”
> 
> then Trilium is fine — but you need a sync/export workflow so the IDE has something local to chew on.
> 
> ## Best architecture for you
> 
> Given how you work, I would **not** make Railway Trilium the only home of your thinking.
> 
> Do this instead:
> 
> - **Local markdown repo/vault** = editable source
> - **Trilium on Railway** = web knowledge interface
> - **scripts** = sync/export/import layer
> 
> So the IDE helps with:
> - front matter cleanup
> - templates
> - manifests
> - bulk refactors
> - scripts
> - dashboards
> 
> And Trilium gives you:
> - mobile/web access
> - hierarchical browsing
> - centralized note access
> 
> ## Simple rule
> 
> **If it matters to AI-assisted editing, keep a local representation.**  
> Otherwise you’re asking your tools to operate through a wall.
> 
> ## Decision narrowing
> 
> You’ve got two sane paths:
> 
> ### Path A — keep Obsidian/local markdown as source of truth
> Best for:
> - AI help
> - bulk editing
> - repo governance
> - front matter workflows
> 
> Then sync selected content into Trilium.
> 
> ### Path B — make Trilium the source of truth
> Best for:
> - web-first usage
> - centralized notes
> - less file management
> 
> But then you need custom scripts/API tooling for serious automation, because your IDE won’t have native visibility into the live content. Trilium’s docs and ecosystem emphasize server/self-hosted use and API/extensions, which is exactly why this extra layer is needed. citeturn0search4turn0search16
> 
> My recommendation: **Path A**.  
> Use Trilium as a **consumer-facing or access-facing layer**, not the only editing layer.
> 
> The short version is: **your IDE can help with the code around Trilium and with any local mirror/export, but not with the live Railway-held note database unless you build a bridge.**
> 
> Next move: decide whether you want me to map a **local-markdown ↔ Trilium sync architecture** for QiVault/FCFCU.

### User
> same issue if i use atomic server huh? so either i get the looka nd feel with no ide help or keep obsidian and sue the ide.

### Assistant
> Short answer: **yes, same issue with almost any server-hosted note system**.
> 
> If the notes **live inside the server/database**, your IDE cannot “see” them directly. The IDE works best when content is **files in a folder**.
> 
> So the tradeoff you’re noticing is real:
> 
> | Approach | Pros | Cons |
> |---|---|---|
> | **Server note system** (Trilium, Atomic Server, etc.) | web UI, structured DB, remote access | IDE can't directly edit content |
> | **Local markdown vault** (Obsidian, plain repo) | IDE + AI tooling works great | weaker built-in database features |
> 
> But the conclusion **is not actually “pick one.”**  
> The real architecture most power users end up with is:
> 
> ```
> Local Markdown (IDE editable)
>         ↓
> Sync / Ingest
>         ↓
> Server Knowledge System
> ```
> 
> Think of it like **Git → GitHub**.
> 
> You don’t edit code directly in GitHub’s database.  
> You edit **files locally**, then push.
> 
> ---
> 
> # What this would look like for you
> 
> ### Authoring layer
> Local folder (QiVault / case folder)
> 
> Your IDE can fully see it:
> 
> ```
> QiVault/
>    cases/
>       FCFCU/
>          content/
>             notes.md
>             motion_interest_calc.md
> ```
> 
> This is where:
> 
> • AI helps  
> • scripts run  
> • manifests run  
> • front matter normalization happens  
> 
> ---
> 
> ### Knowledge layer
> Trilium or Atomic Server
> 
> Used for:
> 
> • browsing  
> • mobile access  
> • linking  
> • dashboards  
> 
> The notes get **pushed there**.
> 
> ---
> 
> # Why this actually fits your brain perfectly
> 
> Your system already has these layers:
> 
> ```
> QiArchive  → documents
> Markdown   → structured notes
> Postgres   → structured data
> ```
> 
> A knowledge server just becomes:
> 
> ```
> viewer + index
> ```
> 
> Not the authoring environment.
> 
> ---
> 
> # What happens if you make the server the only source
> 
> Then every time you want to:
> 
> • bulk rename fields  
> • normalize front matter  
> • run scripts  
> • export manifests  
> 
> …you fight the system.
> 
> That’s why developers rarely use server-native editors for serious work.
> 
> ---
> 
> # So your real choice is this
> 
> ### Option 1 (recommended)
> 
> ```
> Obsidian / markdown vault
>         ↓
> IDE + AI editing
>         ↓
> sync to Trilium / Atomic
> ```
> 
> You get:
> 
> ✔ IDE help  
> ✔ automation  
> ✔ server UI  
> 
> ---
> 
> ### Option 2
> 
> ```
> Trilium / Atomic only
> ```
> 
> You get:
> 
> ✔ nice UI  
> ✖ weak automation  
> ✖ poor AI tooling  
> ✖ no bulk file operations
> 
> ---
> 
> # One more option you might not have considered
> 
> You can actually **use Obsidian without using Obsidian plugins or UI features**.
> 
> Just treat it as a **markdown viewer/editor for your repo**.
> 
> Your IDE remains the main tool.
> 
> ---
> 
> # My honest recommendation for your stack
> 
> Given everything you're building:
> 
> ```
> QiArchive
> QiVault (markdown repo)
> IDE + AI
> Trilium (optional viewer)
> ```
> 
> Trilium becomes **read-optimized**.
> 
> Markdown repo becomes **write-optimized**.
> 
> ---
> 
> # The mental model
> 
> ```
> GitHub ≠ where you write code
> Database ≠ where you write queries
> CMS ≠ where you write articles
> ```
> 
> Same here.
> 
> **Server knowledge systems are great browsers.  
> They are rarely great authoring systems.**
> 
> ---
> 
> # One question before we lock this architecture
> 
> You mentioned **Atomic Server**.
> 
> Atomic is **very different** from Trilium.
> 
> It’s more like a **structured knowledge graph server**.
> 
> So the real question is:
> 
> **Were you planning to use Atomic as:**
> 
> A. a **semantic graph backend**  
> or  
> B. a **note-taking UI replacement**
> 
> Because if it's **A**, then IDE + markdown + Atomic actually becomes a **very powerful architecture**.
> 
> If it's **B**, then you run into the same IDE visibility issue you just noticed.

### User
> and what about flotes ?

### Assistant
> Short answer: **same problem class as Trilium / Atomic.**
> 
> But Flotes is a bit different, so let’s break it down clearly.
> 
> ---
> 
> # What Flotes actually is
> 
> entity["software","Flotes","note taking web app"] is a **web-based note system** that stores notes in a **database**, not a folder of markdown files.
> 
> That means:
> 
> | Feature | Flotes |
> |---|---|
> IDE can directly read notes | ❌ |
> Files exist on disk | ❌ |
> Database backend | ✔ |
> Web UI | ✔ |
> Server deployable | ✔ |
> 
> So if you run Flotes on Railway, the notes live **inside its database**, not in files your IDE can inspect.
> 
> Result: **same limitation you just noticed with Trilium.**
> 
> ---
> 
> # The real difference vs Trilium
> 
> | Tool | Storage model | Structure |
> |---|---|---|
> Flotes | DB | simple notes |
> Trilium | DB | hierarchical + attributes |
> Atomic | graph DB | semantic knowledge graph |
> Obsidian | files | markdown |
> 
> So Flotes is actually the **least structured** of the bunch.
> 
> It’s basically a **nice web notebook**, not a knowledge system.
> 
> ---
> 
> # The core issue you’re running into
> 
> Your workflow relies heavily on:
> 
> - scripts
> - manifests
> - automation
> - metadata normalization
> - AI refactoring
> - repo structure
> 
> All of those want **files**.
> 
> When the content lives inside a **database**, the IDE can’t manipulate it easily.
> 
> ---
> 
> # This is the architecture conflict
> 
> ### File-based systems
> 
> ```text
> markdown files
>    ↓
> IDE
>    ↓
> scripts / automation
> ```
> 
> ### Database systems
> 
> ```text
> database
>    ↓
> web interface
>    ↓
> API if you build tooling
> ```
> 
> You are **very much a file-system person**.
> 
> Everything you've built (QiVault, manifests, frontmatter) confirms that.
> 
> ---
> 
> # So what are your real options?
> 
> ### Option A (most compatible with your workflow)
> 
> Primary system:
> 
> ```text
> markdown repo
> ```
> 
> Editors:
> 
> - IDE
> - Obsidian
> 
> Optional viewer:
> 
> - Trilium
> - Flotes
> - Atomic
> 
> ---
> 
> ### Option B
> 
> Primary system:
> 
> ```text
> Trilium / Flotes / Atomic
> ```
> 
> Editors:
> 
> - web UI
> - custom scripts
> 
> You lose:
> 
> - IDE AI editing
> - simple git workflows
> - easy bulk operations
> 
> ---
> 
> # My blunt assessment for *you specifically*
> 
> Given:
> 
> - QiVault
> - manifests
> - automation scripts
> - repo governance
> - front matter normalization
> 
> You will **fight database note apps constantly**.
> 
> They’re great for casual note taking.
> 
> They are **not great for automation heavy workflows**.
> 
> ---
> 
> # The system that actually fits what you're building
> 
> ```text
> QiVault (markdown repo)
>       ↓
> IDE + AI
>       ↓
> scripts / manifests
>       ↓
> optional viewer
>    (Obsidian / Trilium)
> ```
> 
> Your notes remain **files**.
> 
> Everything else becomes a **tool around those files**.
> 
> ---
> 
> # If you want my honest recommendation
> 
> For your setup:
> 
> **Primary**
> 
> • markdown repo  
> • IDE  
> • scripts
> 
> **Viewer**
> 
> • Obsidian
> 
> **Optional knowledge UI**
> 
> • Trilium
> 
> Skip Flotes entirely.
> 
> It doesn't give you anything you don't already get from Obsidian.
> 
> ---
> 
> # The key realization you just had
> 
> You said:
> 
> > either i get the look and feel or keep obsidian and use the ide
> 
> That’s **almost right**, but the better framing is:
> 
> ```text
> write in files
> view anywhere
> ```
> 
> Not:
> 
> ```text
> write inside the viewer
> ```
> 
> ---
> 
> # One more thing (important)
> 
> You are **very close to building your own knowledge OS already** with:
> 
> - QiArchive
> - QiVault
> - manifests
> - frontmatter schema
> - scripts
> - Postgres
> 
> Most note apps are **simpler than what you’re building**.
> 
> Trying to replace your system with them will actually **downgrade your capabilities**.
> 
> ---
> 
> If you want, I can also show you something that will probably click instantly for you:
> 
> **A 4-layer architecture that turns QiVault into a real “personal knowledge OS”** while still letting you use Obsidian, IDEs, and optionally Trilium without conflict.

### User
> ok so we dont keep circuling this shit every other day give me a csv with toola nd decisions i can referenc elater

### Assistant
> Good call. Lock the decision so you stop burning cycles on it.  
> Here’s a **reference CSV you can drop in your repo** and treat as the canonical tool decisions for now.
> 
> :::writing{variant="standard" id="27481"}
> tool_name,category,decision,role_in_system,source_of_truth,ide_visibility,automation_level,reasoning,notes
> QiVault (Markdown Repo),Knowledge Storage,ADOPT,Primary knowledge source,Files (Markdown),Full,High,"File-based system enables IDE editing, AI assistance, git versioning, and bulk scripting.",All notes and structured metadata live here.
> IDE (Cursor / VSCode),Authoring Environment,ADOPT,Primary writing and refactoring environment,N/A,Full,High,"Needed for AI-assisted editing, scripting, schema enforcement, and large-scale refactors.",Primary daily tool.
> Obsidian,Viewer + Lightweight Editor,ADOPT (LIMITED),Visualization and quick navigation of markdown vault,Files (Markdown),Full,Medium,"Provides graph view, backlinks, and quick browsing but not required for automation.",Plugins kept minimal.
> Dataview (Obsidian plugin),Query Layer,ADOPT,Local query dashboards inside Obsidian,Files (Frontmatter),Full,Medium,"Useful for dashboards like exhibits, timelines, missing metadata.",Do not rely on it for core logic.
> Templater (Obsidian plugin),Template System,ADOPT,Reusable note templates,Files (Markdown),Full,Medium,"Ensures consistent note creation.",Templates stored in repo.
> Linter (Obsidian plugin),Formatting Enforcement,ADOPT,Normalize markdown and YAML,Files (Markdown),Full,High,"Prevents formatting drift and keeps files clean.",Avoid aggressive YAML mutation rules initially.
> Metadata Menu (Obsidian plugin),Metadata Editing,OPTIONAL,UI editing of frontmatter,Files (Markdown),Full,Medium,"Useful for manual corrections but not required.",Disable if unnecessary.
> Trilium (Railway),Knowledge Viewer,OPTIONAL,Web-accessible knowledge browsing,Database,Low,Medium,"Server interface for remote viewing; not used as editing source.",Sync from markdown if used.
> Atomic Server,Semantic Graph Backend,FUTURE OPTION,Structured knowledge graph layer,Database,Low,High,"Potential future semantic graph system.",Not primary note tool.
> Flotes,Web Notebook,REJECT,Simple web note system,Database,None,Low,"Does not add capability beyond existing tools and reduces automation ability.",Do not deploy.
> QiArchive,Document Repository,ADOPT,Evidence and document storage,Files + metadata,Full,High,"Canonical storage for documents and case artifacts.",Linked to markdown notes.
> Paperless-NGX,Document Intake,ADOPT,OCR and document ingestion,Database + files,Low,Medium,"Handles scanning, OCR, and tagging of incoming documents.",Feeds QiArchive.
> Postgres (Railway),Structured Data Layer,ADOPT,Structured records and automation backend,Database,Medium,High,"Used for structured entities, logs, and automation tasks.",Not used for note editing.
> Automation Scripts (Python),Automation Engine,ADOPT,Bulk refactoring, manifests, ingestion scripts,Files + DB,Full,High,"Critical for metadata normalization and system automation.",Stored in repo.
> Manifest CSV System,Audit Layer,ADOPT,Frontmatter extraction and bulk updates,Files (CSV),Full,High,"Allows controlled batch editing and dry runs.",Used before any mass mutation.
> :::
> 
> ### How to use this
> Save it somewhere like:
> 
> ```
> docs/system_tool_decisions.csv
> ```
> 
> or
> 
> ```
> config/architecture/tool_decisions.csv
> ```
> 
> Then when you start second-guessing the stack later, you just check this file instead of reopening the debate.
> 
> ### The **one-line rule this table encodes**
> **Files are the source of truth. Everything else is an interface.**
> 
> That single rule prevents 90% of the architecture churn you’ve been running into.
> 
> ---
> 
> If you want, I can also give you a **second CSV that’s even more useful long-term**:
> 
> `knowledge_stack_layers.csv`
> 
> It maps the **4 layers of your system (QiVault, QiArchive, Postgres, Viewer layer)** so every new tool you consider has to fit one of those layers instead of derailing the architecture.

### User
> gir that is way too many cateogries keep category decsiion, role, source, ide automation reasoning to a few options keep si very simple stupid for me.

### Assistant
> Got you. KISS mode. Fewer columns, fewer choices, no fluff.
> 
> Use **only these columns**:
> 
> ```
> category,tool,decision,role,source,ide,automation,reason
> ```
> 
> And keep the allowed values tight so you don’t overthink it later.
> 
> **Category options**
> ```
> notes
> docs
> viewer
> database
> automation
> editor
> ```
> 
> **Decision options**
> ```
> use
> optional
> future
> reject
> ```
> 
> **Source options**
> ```
> files
> database
> mixed
> ```
> 
> **IDE options**
> ```
> full
> limited
> none
> ```
> 
> **Automation options**
> ```
> high
> medium
> low
> ```
> 
> ---
> 
> ### Simple CSV
> 
> :::writing{variant="standard" id="14862"}
> category,tool,decision,role,source,ide,automation,reason
> notes,QiVault markdown repo,use,primary notes system,files,full,high,"files allow AI editing, scripts, and version control"
> editor,IDE (Cursor/VSCode),use,primary writing and scripting tool,files,full,high,"AI editing and bulk refactoring"
> viewer,Obsidian,optional,note browsing and graph view,files,full,medium,"nice UI but not required for system"
> docs,QiArchive,use,document evidence storage,files,full,high,"canonical storage for documents"
> docs,Paperless-NGX,use,document intake and OCR,database,limited,medium,"scan and ingest documents"
> database,Postgres (Railway),use,structured data backend,database,limited,high,"stores structured entities and automation data"
> viewer,Trilium (Railway),optional,web viewer for notes,database,none,medium,"remote browsing but not source of truth"
> viewer,Atomic Server,future,semantic knowledge graph,database,none,high,"possible future knowledge layer"
> viewer,Flotes,reject,web notebook,database,none,low,"adds no capability beyond markdown system"
> automation,Python scripts,use,automation and migrations,files,full,high,"manifests, normalization, ingestion"
> automation,CSV manifest system,use,bulk metadata editing,files,full,high,"controlled updates and dry runs"
> :::
> 
> ---
> 
> ### Where to store it
> 
> Put it somewhere obvious so future-you actually finds it:
> 
> ```
> config/tool_decisions.csv
> ```
> 
> or
> 
> ```
> docs/architecture/tools.csv
> ```
> 
> ---
> 
> ### The one rule encoded in this file
> 
> If you forget everything else, remember this:
> 
> ```
> files = source of truth
> ```
> 
> Everything else is **just an interface or automation layer**.
> 
> ---
> 
> If you want, I can also give you a **second tiny CSV (even simpler)** that will save you more time later:
> 
> ```
> decision_rules.csv
> ```
> 
> It’s basically **3 rules that prevent you from tool-hopping again.**

### User
> also you already know everythign we ahve discussed so go ahead and give the full current updated list as it stand now.

### Assistant
> Here’s the **clean, KISS reference CSV** with the current decisions based on everything we’ve talked through.  
> Same simple columns you asked for:
> 
> ```
> category,tool,decision,role,source,ide,automation,reason
> ```
> 
> And only the small option sets.
> 
> :::writing{variant="standard" id="53824"}
> category,tool,decision,role,source,ide,automation,reason
> notes,QiVault markdown repo,use,primary notes system,files,full,high,"files enable AI editing, scripts, git, and bulk refactoring"
> editor,Cursor IDE,use,primary development and writing environment,files,full,high,"AI-assisted coding and markdown editing"
> viewer,Obsidian,optional,note viewer and navigation UI,files,full,medium,"graph view, backlinks, quick browsing"
> viewer,Obsidian Dataview plugin,optional,query dashboards inside vault,files,full,medium,"metadata queries for exhibits timelines and missing fields"
> viewer,Obsidian Templater plugin,optional,note template generation,files,full,medium,"consistent note creation"
> automation,Obsidian Linter plugin,optional,markdown and yaml normalization,files,full,medium,"keeps formatting consistent"
> viewer,Metadata Menu plugin,optional,ui editing of frontmatter,files,full,low,"convenient but not required"
> docs,QiArchive,use,document evidence storage,files,full,high,"central storage for evidence and artifacts"
> docs,Paperless-NGX,use,document ingestion and OCR,mixed,limited,medium,"scanning tagging and OCR intake"
> database,Postgres (Railway),use,structured data backend,database,limited,high,"structured entities logs automation data"
> automation,Python scripts,use,automation engine,files,full,high,"bulk metadata updates ingestion scripts system tooling"
> automation,CSV manifest system,use,bulk metadata mapping and review,files,full,high,"safe dry-run editing of frontmatter"
> viewer,Trilium (Railway),optional,web knowledge viewer,database,none,medium,"remote browsing but not source of truth"
> viewer,Atomic Server,future,semantic knowledge graph,database,none,high,"possible future graph layer"
> viewer,Flotes,reject,web notebook,database,none,low,"adds no capability beyond markdown repo"
> docs,Google Drive,use,blob storage and sync,mixed,limited,low,"cheap large storage for files and archives"
> code,GitHub,use,code repository and version control,files,full,high,"versioning collaboration automation"
> automation,n8n (Railway),optional,workflow automation,mixed,limited,high,"event pipelines integrations"
> portal,Cloudflare Pages,use,client portals and static apps,files,full,high,"frontend hosting for QiPortals"
> automation,Cloudflare Workers,use,serverless automation layer,mixed,limited,high,"api endpoints ingestion tasks"
> database,Supabase,optional,secondary structured backend,database,limited,high,"used for portal apps if needed"
> database,Railway,use,hosting environment,mixed,limited,medium,"runs postgres n8n and services"
> :::
> 
> ---
> 
> ## Save it here
> I recommend:
> 
> ```
> QiVault/config/tool_decisions.csv
> ```
> 
> or
> 
> ```
> QiOne/docs/architecture/tools_current.csv
> ```
> 
> So when you start questioning tools again later you just open this file instead of re-architecting.
> 
> ---
> 
> ## The distilled architecture this CSV represents
> 
> Your stack right now:
> 
> ```
> FILES LAYER
> QiVault (markdown)
> QiArchive (documents)
> 
> AUTOMATION LAYER
> Python scripts
> CSV manifests
> n8n
> Cloudflare Workers
> 
> STRUCTURED DATA
> Postgres
> 
> VIEWERS
> Obsidian
> Trilium
> 
> HOSTING
> Railway
> Cloudflare
> 
> STORAGE
> Google Drive
> GitHub
> ```
> 
> And the **one governing rule** we locked in:
> 
> ```
> files = source of truth
> ```
> 
> Everything else is **interface, automation, or hosting**.
> 
> ---
> 
> If you want, next I can also give you a **second CSV that will help you way more long term**:
> 
> `system_layers.csv`
> 
> It defines the **5 layers of QiOS/QiVault** so every new tool you consider must fit one layer instead of derailing the architecture again.

### User
> back to obsidain for now what are my plugins and settings

### Assistant
> Alright — **locking this down so you stop tweaking it every week.**  
> This is the **minimal, stable Obsidian setup for your QiVault / case workflow**.
> 
> Goal:
> 
> - works with **markdown files**
> - works with **IDE + scripts**
> - avoids plugin chaos
> - supports **frontmatter + manifests**
> 
> ---
> 
> # Core Plugins (turn ON)
> 
> These come with Obsidian.
> 
> ```
> File explorer
> Search
> Backlinks
> Outgoing links
> Properties
> Templates
> Daily notes
> Command palette
> Page preview
> Bookmarks
> ```
> 
> ### Leave OFF
> 
> ```
> Canvas
> Slides
> Audio recorder
> Random note
> Publish
> Workspaces
> ```
> 
> Those add clutter for your use case.
> 
> ---
> 
> # Community Plugins (install)
> 
> These are the only ones you need.
> 
> ```
> dataview
> templater-obsidian
> obsidian-linter
> metadata-menu
> ```
> 
> Optional later:
> 
> ```
> omnisearch
> ```
> 
> Do **NOT** install a bunch of random plugins.
> 
> ---
> 
> # Plugin Settings
> 
> ## Dataview
> 
> Settings:
> 
> ```
> Enable Inline Fields: ON
> Enable JavaScript Queries: OFF (turn on later if needed)
> Refresh Index On Startup: ON
> Refresh Index On File Change: ON
> ```
> 
> Why:
> 
> - lets you build dashboards
> - query frontmatter
> - track missing metadata
> 
> ---
> 
> ## Templater
> 
> Settings:
> 
> ```
> Templates folder location: _templates
> Trigger templater on new file creation: ON
> Enable folder templates: OFF for now
> User scripts folder: _templates/scripts
> ```
> 
> Create folder:
> 
> ```
> content/_templates/
> ```
> 
> Example templates later:
> 
> ```
> case_event.md
> case_motion.md
> exhibit_note.md
> person_note.md
> issue_note.md
> ```
> 
> ---
> 
> ## Obsidian Linter
> 
> Turn on:
> 
> ```
> Lint on save
> Normalize headings
> Remove trailing spaces
> Ensure newline at end
> Normalize bullet lists
> ```
> 
> Frontmatter rules:
> 
> ```
> Keep YAML formatting clean
> Do NOT auto-sort keys yet
> Do NOT auto-add fields
> ```
> 
> Reason:
> 
> Your **manifest system** controls metadata, not the linter.
> 
> ---
> 
> ## Metadata Menu
> 
> Settings:
> 
> ```
> Auto update fields: ON
> Show metadata in sidebar: ON
> Show icons: optional
> ```
> 
> Use it only for **manual corrections**.
> 
> ---
> 
> # Folder Structure inside Vault
> 
> Create this:
> 
> ```
> content/
> 
> _templates/
> _views/
> _people/
> _events/
> _exhibits/
> _issues/
> _notes/
> ```
> 
> Special folders:
> 
> ```
> _templates  → templater files
> _views      → dataview dashboards
> ```
> 
> ---
> 
> # Example Dataview Dashboards
> 
> ## Missing Metadata
> 
> ````markdown
> ```dataview
> TABLE file.name
> FROM ""
> WHERE !document_id OR !matter_id OR !status
> SORT file.name ASC
> ```
> ````
> 
> ---
> 
> ## Exhibit Index
> 
> ````markdown
> ```dataview
> TABLE exhibit_id, title, source, status
> FROM ""
> WHERE type = "exhibit"
> SORT exhibit_id ASC
> ```
> ````
> 
> ---
> 
> ## Timeline
> 
> ````markdown
> ```dataview
> TABLE event_date, title, actor
> FROM ""
> WHERE type = "event"
> SORT event_date ASC
> ```
> ````
> 
> ---
> 
> # Capture the Vault Template
> 
> After configuring everything:
> 
> 1. **Close Obsidian**
> 2. Copy this folder:
> 
> ```
> content/.obsidian/
> ```
> 
> Into your repo:
> 
> ```
> QiOne/templates/obsidian_vault/.obsidian/
> ```
> 
> Now you have a **baseline template**.
> 
> Later we script:
> 
> ```
> bootstrap_vault.py
> ```
> 
> to recreate it automatically.
> 
> ---
> 
> # Important rule for you
> 
> Obsidian is **NOT the system**.
> 
> It is only:
> 
> ```
> viewer + editor
> ```
> 
> The real system is:
> 
> ```
> markdown files
> scripts
> manifests
> QiArchive
> ```
> 
> So keep Obsidian **lightweight**.
> 
> ---
> 
> # Your final plugin list (locked)
> 
> ```
> dataview
> templater
> linter
> metadata-menu
> ```
> 
> That's it.
> 
> ---
> 
> If you want, next I can also give you something **very useful for your case vault**:
> 
> A **ready-to-drop `_views/` folder** containing about **10 Dataview dashboards** like:
> 
> - missing metadata
> - exhibits
> - filings
> - timeline
> - witnesses
> - issues
> - evidence chain
> 
> It turns Obsidian into a **case command center** in about 2 minutes.

### User
> maybe if i try a them or somethign to trick my adhd to treat obsidain more better

### Assistant
> That’s actually a **very real ADHD strategy** — changing the visual environment can make your brain treat the tool as “new” and more engaging. A theme can absolutely help Obsidian feel less like “just another text editor” and more like a workspace your brain wants to open. Let’s keep it **simple and purposeful** so it helps focus instead of becoming another rabbit hole. 🧠✨
> 
> ---
> 
> # Good Obsidian Themes for ADHD / Focus
> 
> ## 1. **Minimal**
> entity["software","Minimal (Obsidian Theme)","Obsidian community theme"]
> 
> **Best balance of clean + customizable.**
> 
> Why it works:
> - reduces visual noise
> - adjustable accent colors
> - adjustable font sizes
> - clean sidebars
> 
> Good ADHD trick:
> - set **one strong accent color** so headings and links pop.
> 
> Suggested setup:
> - accent color: teal or purple  
> - sidebar width: slightly wider  
> - line width: ~700–800px  
> 
> ---
> 
> ## 2. **Things**
> entity["software","Things (Obsidian Theme)","Obsidian community theme"]
> 
> Very calm, very readable.
> 
> Why it helps:
> - looks like a structured notebook
> - great typography
> - feels organized without trying
> 
> Good if you want Obsidian to feel like **a thinking journal** instead of software.
> 
> ---
> 
> ## 3. **AnuPpuccin**
> entity["software","AnuPpuccin (Obsidian Theme)","Obsidian community theme"]
> 
> Great for dopamine. 🎨
> 
> Why it helps ADHD users:
> - vibrant but balanced colors
> - nice contrast
> - visually stimulating without being messy
> 
> Good if plain themes feel **too boring**.
> 
> ---
> 
> # My recommendation for you
> 
> Start with **Minimal**.
> 
> Then install this plugin:
> 
> ```
> Style Settings
> ```
> 
> It lets you adjust the theme without editing CSS.
> 
> ---
> 
> # Minimal Theme Settings I’d Use for You
> 
> Inside **Style Settings → Minimal**:
> 
> ### Layout
> 
> ```
> Readable line length: ON
> Line width: 750px
> Focus mode: ON
> ```
> 
> ### Sidebar
> 
> ```
> Sidebar width: ~280px
> ```
> 
> ### Colors
> 
> Pick one accent color and stick with it.
> 
> Examples that work well:
> 
> ```
> teal
> purple
> indigo
> ```
> 
> Avoid red/orange (too stressful long-term).
> 
> ---
> 
> # Fonts (very important for ADHD)
> 
> Good fonts reduce cognitive friction.
> 
> ### Body text
> 
> Use one of these:
> 
> ```
> Inter
> Source Sans Pro
> IBM Plex Sans
> ```
> 
> ### Code / frontmatter
> 
> ```
> JetBrains Mono
> ```
> 
> You can set fonts under:
> 
> ```
> Settings → Appearance → Fonts
> ```
> 
> ---
> 
> # Layout trick that helps ADHD focus
> 
> Set up a **3-pane workspace**.
> 
> Left sidebar:
> 
> ```
> File explorer
> ```
> 
> Center:
> 
> ```
> Current note
> ```
> 
> Right sidebar:
> 
> ```
> Backlinks
> Dataview dashboards
> Metadata
> ```
> 
> That way your brain always sees:
> 
> ```
> structure | content | context
> ```
> 
> ---
> 
> # Another trick: make a “Command Center” note
> 
> Create:
> 
> ```
> _views/dashboard.md
> ```
> 
> Put your dataview blocks there so opening Obsidian always shows useful info.
> 
> Example:
> 
> ````markdown
> # Case Dashboard
> 
> ## Missing Metadata
> ```dataview
> TABLE file.name
> FROM ""
> WHERE !document_id
> ```
> 
> ## Timeline
> ```dataview
> TABLE event_date, title
> FROM ""
> WHERE type = "event"
> SORT event_date
> ```
> ````
> 
> When Obsidian opens, it feels like a **mission control panel**, not a blank editor.
> 
> ---
> 
> # One more ADHD trick
> 
> Enable:
> 
> ```
> Settings → Editor → Focus mode
> ```
> 
> This dims everything except the paragraph you're working on.
> 
> Very good for concentration.
> 
> ---
> 
> # Final setup (keep it simple)
> 
> Theme:
> 
> ```
> Minimal
> ```
> 
> Plugins:
> 
> ```
> Dataview
> Templater
> Linter
> Metadata Menu
> Style Settings
> ```
> 
> That’s **5 plugins total**.
> 
> No more.
> 
> ---
> 
> 💡 If you want, I can also show you something **very ADHD-friendly**:
> 
> How to turn Obsidian into a **visual case command center** with:
> 
> - timeline panel  
> - evidence index  
> - issue tracker  
> - missing metadata alerts  
> 
> All in one dashboard note. It makes the vault feel **alive instead of static**, which helps a lot with motivation.

### User
> prism?

### Assistant
> If you mean the **Prism theme** for Obsidian, yeah — that’s actually a **pretty good ADHD-friendly choice**. It’s more colorful and energetic than Minimal, which can help if plain themes feel boring or “dead” to your brain.
> 
> entity["software","Prism (Obsidian Theme)","Obsidian community theme"]
> 
> ## Why Prism can work well for ADHD
> - **High contrast colors** → headings and structure stand out immediately  
> - **Color-coded elements** → easier visual scanning  
> - **Less “flat” feeling** than Minimal  
> - Makes notes feel a bit more like a **workspace** than a text document
> 
> For some ADHD brains, that **extra visual stimulation = better engagement**.
> 
> ---
> 
> # Recommended Prism setup (keep it controlled)
> 
> If you install Prism, tweak it so it doesn’t become visual chaos.
> 
> ### Appearance
> Set:
> 
> - **Readable line length** → ON  
> - **Line width** → ~750px  
> - **Interface font** → Inter  
> - **Text font** → Inter / Source Sans  
> 
> This keeps reading smooth.
> 
> ---
> 
> ### Editor settings
> 
> Turn on:
> 
> ```
> Focus mode
> Readable line length
> Show indentation guides
> ```
> 
> Those three help structure pop visually.
> 
> ---
> 
> ### Sidebar layout
> 
> Left sidebar:
> ```
> File Explorer
> ```
> 
> Right sidebar:
> ```
> Backlinks
> Metadata
> Outline
> ```
> 
> This gives you a **3-zone layout**:
> 
> ```
> navigation | writing | context
> ```
> 
> Which helps ADHD brains stay oriented.
> 
> ---
> 
> # Plugin combo that pairs well with Prism
> 
> Keep it small:
> 
> ```
> Dataview
> Templater
> Linter
> Metadata Menu
> Style Settings
> ```
> 
> That's it.
> 
> Avoid the temptation to install 20 plugins.
> 
> ---
> 
> # A trick that works surprisingly well
> 
> Pick **one accent color system for note types**.
> 
> Example:
> 
> ```
> motions → purple
> events → blue
> evidence → green
> issues → orange
> people → teal
> ```
> 
> With Prism, headings will visually separate those categories.
> 
> Your brain will start recognizing note types **without reading**.
> 
> ---
> 
> # My honest opinion for you
> 
> Between the themes:
> 
> | Theme | Best for |
> |------|------|
> Minimal | calm focus |
> Things | writing/journaling |
> Prism | ADHD stimulation |
> 
> For **your brain**, Prism might actually be the most motivating.
> 
> Minimal is cleaner but can feel **too sterile**.
> 
> ---
> 
> # One important rule
> 
> Don’t keep switching themes.
> 
> Give it **one week** before judging it.
> 
> ADHD brains need time for the interface to become familiar.
> 
> ---
> 
> If you want, I can also show you a **really powerful Obsidian trick** that works amazingly with Prism:
> 
> A **home dashboard note** that turns the vault into a **case command center** (timeline, exhibits, missing metadata, tasks) so opening Obsidian always shows something useful instead of a blank page.

### User
> border has cards and maybe typomagical, or ono sendaai encore or obsidian notion or laoster

### Assistant
> You’re basically picking between **three styles of themes**. I’ll translate the ones you mentioned so you can pick **fast and move on** instead of testing ten themes.
> 
> ---
> 
> # The themes you mentioned (what they actually feel like)
> 
> ## Border
> entity["software","Border (Obsidian Theme)","Obsidian community theme"]
> 
> **Best “cards UI” theme.**
> 
> Feels like:
> - Notion
> - dashboards
> - modular blocks
> 
> Pros
> - cards everywhere
> - strong visual separation
> - good for dashboards and Dataview
> - modern UI
> 
> Cons
> - slightly heavier
> - not as minimal for writing
> 
> Good for you if you want Obsidian to feel like a **control panel**.
> 
> ---
> 
> ## Typomagical
> entity["software","Typomagical (Obsidian Theme)","Obsidian community theme"]
> 
> **Typography-first theme.**
> 
> Feels like:
> - editorial writing
> - reading mode
> - very polished text
> 
> Pros
> - beautiful writing experience
> - amazing headings
> - great readability
> 
> Cons
> - not great for dashboards
> - less structural UI
> 
> Best if Obsidian is mostly **writing**.
> 
> ---
> 
> ## Ono Sendai Encore
> entity["software","Ono Sendai Encore (Obsidian Theme)","Obsidian community theme"]
> 
> Cyberpunk / neon aesthetic.
> 
> Pros
> - very stimulating
> - cool look
> - unique
> 
> Cons
> - can be visually noisy
> - not great for long writing sessions
> 
> Good for **dopamine**, not always for productivity.
> 
> ---
> 
> ## Obsidian Notion
> entity["software","Obsidian Notion Theme","Obsidian community theme"]
> 
> Makes Obsidian look like Notion.
> 
> Pros
> - familiar layout
> - card feel
> - comfortable navigation
> 
> Cons
> - Notion clones can feel clunky
> - sometimes slow
> 
> ---
> 
> ## Laoster
> entity["software","Laoster (Obsidian Theme)","Obsidian community theme"]
> 
> Very clean and modern.
> 
> Pros
> - minimal but stylish
> - good spacing
> - easy to read
> 
> Cons
> - less visually exciting
> - less dashboard feel
> 
> ---
> 
> # My recommendation for YOU
> 
> Given your ADHD + dashboards + system thinking:
> 
> ### #1 choice
> **Border**
> 
> Why:
> - card layout
> - structure pops
> - good with Dataview dashboards
> - feels like a workspace
> 
> ---
> 
> ### #2 choice
> **Typomagical**
> 
> If you want writing to feel amazing.
> 
> ---
> 
> ### Skip for now
> 
> ```
> Ono Sendai Encore
> Obsidian Notion
> Laoster
> ```
> 
> Not bad — just less aligned with your workflow.
> 
> ---
> 
> # Best combo for your vault
> 
> Theme:
> 
> ```
> Border
> ```
> 
> Plugins:
> 
> ```
> Dataview
> Templater
> Linter
> Metadata Menu
> Style Settings
> ```
> 
> Fonts:
> 
> ```
> Inter
> JetBrains Mono
> ```
> 
> ---
> 
> # One ADHD trick with Border
> 
> Turn your vault homepage into a **card dashboard**.
> 
> Example:
> 
> ```
> Dashboard
>  ├ Timeline
>  ├ Exhibits
>  ├ Issues
>  ├ People
>  └ Missing Metadata
> ```
> 
> Border makes those sections look like **cards**, which helps visual navigation.
> 
> ---
> 
> # My honest call
> 
> If you want Obsidian to feel like:
> 
> | Feel | Theme |
> |-----|-----|
> writing studio | Typomagical |
> knowledge dashboard | Border |
> dopamine aesthetic | Ono Sendai |
> 
> For **your system**?
> 
> 👉 **Border**.
> 
> ---
> 
> If you want, I can also show you **3 Obsidian plugins that massively improve ADHD usability** (one of them is a game-changer for navigation).

### User
> ya the card sare what i think help any other thems to take a peak at or sotp ehre.

### Assistant
> You’re on the **right track with cards**. For ADHD brains, **visual containers** (cards/panels) help because they break the page into chunks instead of one giant wall of text.
> 
> But don’t fall into the **theme rabbit hole** again. Look at **3 more max**, then pick one and lock it.
> 
> ---
> 
> # Themes worth a quick peek (card / modular feel)
> 
> ## Border  *(still the best card theme)*
> entity["software","Border (Obsidian Theme)","Obsidian community theme"]
> 
> Why it’s good:
> - dashboard feel
> - clear panels
> - great with Dataview
> - modern UI
> 
> This is still **my top pick for you**.
> 
> ---
> 
> ## ITS Theme
> entity["software","ITS Theme","Obsidian community theme"]
> 
> Very powerful theme.
> 
> Pros
> - modular UI blocks
> - tons of customization
> - works great with **Style Settings plugin**
> 
> Cons
> - lots of options (can become a rabbit hole)
> 
> Good middle ground between **cards + control**.
> 
> ---
> 
> ## AnuPpuccin
> entity["software","AnuPpuccin (Obsidian Theme)","Obsidian community theme"]
> 
> Why ADHD users like it:
> - very readable
> - colorful but balanced
> - strong visual hierarchy
> 
> Not a card theme but **very comfortable to use long-term**.
> 
> ---
> 
> ## Minimal (with cards)
> entity["software","Minimal (Obsidian Theme)","Obsidian community theme"]
> 
> Minimal itself is plain, but with **Minimal Cards CSS snippets** it becomes very card-like.
> 
> Pros
> - extremely stable
> - lots of community support
> - customizable
> 
> Cons
> - needs small tweaks.
> 
> ---
> 
> # My honest advice
> 
> You’ve already done enough exploration.
> 
> Look at only these **3 themes total**:
> 
> ```
> Border
> ITS Theme
> AnuPpuccin
> ```
> 
> Pick the one that makes your brain go:
> 
> > “yeah I want to open this again”
> 
> Then **stop theme hunting**.
> 
> ---
> 
> # My guess for you
> 
> Based on everything you've said:
> 
> **Border will probably stick.**
> 
> Because your brain likes:
> 
> - dashboards
> - structure
> - panels
> - control centers
> 
> Border makes Obsidian feel like a **system console**, not a notebook.
> 
> ---
> 
> # One more ADHD trick
> 
> Instead of worrying about the theme, create a **home dashboard note**.
> 
> Example layout:
> 
> ```
> HOME
>  ├ Timeline
>  ├ Exhibits
>  ├ Issues
>  ├ People
>  ├ Missing Metadata
>  └ Quick Capture
> ```
> 
> When Obsidian opens, you land on that page.
> 
> This reduces the **“what do I do now?” paralysis**.
> 
> ---
> 
> If you want, I can also show you **one plugin that pairs insanely well with card themes** and makes Obsidian feel much more like a modern workspace (it changes navigation and reduces ADHD friction a lot).

### User
> is there a quarts theme or a material them

### Assistant
> Yes — **both exist**, but they’re a bit different in Obsidian.
> 
> ---
> 
> # Material theme for Obsidian
> 
> Yes, there **is a Material-style theme** inspired by Google’s Material design.
> 
> entity["software","Obsidian Material Theme","community theme inspired by Material Design"]
> 
> Key points:
> 
> - Inspired by **Google Material + Atom editor style**  
> - Mainly **dark theme**  
> - Clean, modern UI  
> - Good code highlighting  
> 
> This theme is basically a **developer-style interface** rather than a dashboard/cards style. citeturn0search1
> 
> **Good if you like:**
> 
> - VS Code aesthetic  
> - developer UI  
> - dark minimal interfaces  
> 
> **Not great if you want:**
> 
> - cards
> - dashboards
> - visual panels
> 
> ---
> 
> # Quartz theme
> 
> There isn’t really a **mainstream “Quartz theme”** inside the official Obsidian theme store.
> 
> But **Quartz** usually refers to something different:
> 
> entity["software","Quartz","open-source static site generator for Obsidian vaults"]
> 
> Quartz is:
> 
> - a **static site generator**
> - turns your vault into a **website**
> - used for publishing notes online
> 
> So it’s **not a UI theme**, it’s more like a **publishing engine**.
> 
> ---
> 
> # Quick comparison
> 
> | Thing | What it actually is |
> |------|------|
> Material Theme | Obsidian UI theme |
> Quartz | publishing system |
> Border | dashboard theme |
> Minimal | clean writing theme |
> 
> ---
> 
> # For what you said earlier (ADHD + cards)
> 
> Material theme probably **won’t help much**.
> 
> You want themes that give **visual blocks**.
> 
> Best ones for that:
> 
> ```
> Border
> ITS Theme
> Minimal (with card snippets)
> ```
> 
> ---
> 
> # My recommendation (stop exploring after this)
> 
> Look at **only these 3 themes**:
> 
> ```
> Border
> ITS Theme
> Minimal
> ```
> 
> Pick one and lock it.
> 
> ---
> 
> # My guess for you
> 
> Based on everything you've said:
> 
> 👉 **Border**
> 
> Because:
> 
> - cards
> - structure
> - dashboards
> - visual navigation
> 
> Those help ADHD brains more than typography themes.
> 
> ---
> 
> If you want, I can also show you **one Obsidian trick that makes ANY theme look like a card dashboard** (and it takes about 30 seconds). It’s actually better than switching themes endlessly.

### User
> ok back to plugins

### Assistant
> Good — plugins matter more than themes anyway. Let’s **lock the plugin list** so you stop drifting.
> 
> Your goal with Obsidian is:
> 
> - work with **markdown files**
> - keep **IDE compatibility**
> - support **frontmatter + manifests**
> - provide **visual navigation for ADHD**
> - avoid plugin chaos
> 
> So we keep **~7–9 plugins max**.
> 
> ---
> 
> # Core Plugins (turn ON)
> 
> These are built into Obsidian.
> 
> ```
> File explorer
> Search
> Backlinks
> Outgoing links
> Properties
> Templates
> Daily notes
> Command palette
> Page preview
> Bookmarks
> ```
> 
> Leave OFF:
> 
> ```
> Canvas
> Slides
> Audio recorder
> Random note
> Publish
> Workspaces
> ```
> 
> ---
> 
> # Community Plugins (your locked list)
> 
> ### 1. Dataview
> entity["software","Dataview","Obsidian community plugin"]
> 
> Purpose  
> Query frontmatter and build dashboards.
> 
> Use it for:
> 
> - exhibit lists  
> - timeline  
> - missing metadata  
> - case indexes  
> 
> Settings:
> 
> ```
> Enable Inline Fields: ON
> Enable JavaScript Queries: OFF (for now)
> Refresh Index On Startup: ON
> Refresh On File Change: ON
> ```
> 
> ---
> 
> ### 2. Templater
> entity["software","Templater","Obsidian community plugin"]
> 
> Purpose  
> Consistent note creation.
> 
> Settings:
> 
> ```
> Templates folder: _templates
> Trigger on new file: ON
> User scripts: _templates/scripts
> ```
> 
> Example templates later:
> 
> ```
> case_event.md
> motion_note.md
> exhibit_note.md
> person_note.md
> issue_note.md
> ```
> 
> ---
> 
> ### 3. Linter
> entity["software","Obsidian Linter","Obsidian community plugin"]
> 
> Purpose  
> Normalize markdown and YAML.
> 
> Enable:
> 
> ```
> Lint on save
> Normalize headings
> Remove trailing spaces
> Ensure newline at end
> Normalize bullet lists
> ```
> 
> Disable for now:
> 
> ```
> Auto-sort YAML keys
> Auto-add fields
> ```
> 
> Your **manifest system controls metadata**, not the linter.
> 
> ---
> 
> ### 4. Metadata Menu
> entity["software","Metadata Menu","Obsidian community plugin"]
> 
> Purpose  
> Edit frontmatter visually.
> 
> Settings:
> 
> ```
> Show metadata sidebar: ON
> Auto sync fields: ON
> ```
> 
> Useful when manually correcting notes.
> 
> ---
> 
> ### 5. Style Settings
> entity["software","Style Settings","Obsidian community plugin"]
> 
> Purpose  
> Control theme options without editing CSS.
> 
> Needed for themes like:
> 
> - Border
> - ITS Theme
> - Minimal
> 
> ---
> 
> ### 6. Commander (ADHD navigation boost)
> entity["software","Commander","Obsidian community plugin"]
> 
> Purpose  
> Add buttons to the UI.
> 
> Example:
> 
> ```
> New Event
> New Exhibit
> New Note
> ```
> 
> Very helpful for quick capture.
> 
> ---
> 
> ### 7. Omnisearch (optional but nice)
> entity["software","Omnisearch","Obsidian community plugin"]
> 
> Purpose  
> Much better search than default.
> 
> Features:
> 
> - fuzzy search
> - fast indexing
> - better results
> 
> Optional but recommended.
> 
> ---
> 
> # Final Plugin List (locked)
> 
> ```
> Dataview
> Templater
> Linter
> Metadata Menu
> Style Settings
> Commander
> Omnisearch
> ```
> 
> 7 plugins total.
> 
> That’s a **stable setup**.
> 
> ---
> 
> # Plugin Folder Structure
> 
> Create these folders in your vault:
> 
> ```
> _templates/
> _views/
> _scripts/
> ```
> 
> Meaning:
> 
> ```
> _templates → templater templates
> _views → dataview dashboards
> _scripts → helper scripts
> ```
> 
> ---
> 
> # Example Dashboard Note
> 
> Create:
> 
> ```
> _views/dashboard.md
> ```
> 
> Example:
> 
> ````markdown
> # Case Dashboard
> 
> ## Missing Metadata
> ```dataview
> TABLE file.name
> FROM ""
> WHERE !document_id
> ```
> 
> ## Timeline
> ```dataview
> TABLE event_date, title
> FROM ""
> WHERE type = "event"
> SORT event_date
> ```
> ````
> 
> When Obsidian opens, it becomes a **control center**.
> 
> ---
> 
> # One plugin I deliberately did NOT recommend
> 
> ```
> Kanban
> Excalidraw
> Tasks
> Calendar
> ```
> 
> Those are good plugins, but they **pull you toward using Obsidian as a system**.
> 
> Your real system is:
> 
> ```
> markdown files
> scripts
> QiArchive
> Postgres
> ```
> 
> Obsidian is just a **viewer/editor**.
> 
> ---
> 
> # If you want one ADHD game-changer
> 
> There is **one plugin that massively improves navigation** and makes vaults feel like apps instead of documents.
> 
> Most people with big vaults eventually install it.
> 
> If you want, I can show you that one next — it pairs extremely well with **card themes like Border**.

### User
> here is the obsidian folder whtich file do you want to see to update. {
>   "name": ".obsidian",
>   "path": "g:\\My Drive\\QiVault\\30_projects\\CASES\\30.05.01_CASE_FCFCU\\content\\.obsidian",
>   "type": "directory",
>   "children": [
>     {
>       "name": "plugins",
>       "type": "folder",
>       "children": [
>         {
>           "name": "better_export_pdf",
>           "type": "folder",
>           "children": [
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "cmdr",
>           "type": "folder",
>           "children": [
>             {
>               "name": "data.json",
>               "type": "file"
>             },
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "dataview",
>           "type": "folder",
>           "children": [
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "export-to-html",
>           "type": "folder",
>           "children": [
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "folder_notes",
>           "type": "folder",
>           "children": [
>             {
>               "name": "data.json",
>               "type": "file"
>             },
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "markwhen",
>           "type": "folder",
>           "children": [
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "metadata-menu",
>           "type": "folder",
>           "children": [
>             {
>               "name": "data.json",
>               "type": "file"
>             },
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "note_uid_generator",
>           "type": "folder",
>           "children": [
>             {
>               "name": "data.json",
>               "type": "file"
>             },
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "notebook_navigator",
>           "type": "folder",
>           "children": [
>             {
>               "name": "data.json",
>               "type": "file"
>             },
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "obsidian-excalidraw-plugin",
>           "type": "folder",
>           "children": [
>             {
>               "name": "data.json",
>               "type": "file"
>             },
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "obsidian-linter",
>           "type": "folder",
>           "children": [
>             {
>               "name": "data.json",
>               "type": "file"
>             },
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "obsidian-mind-map",
>           "type": "folder",
>           "children": [
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "obsidian-style-settings",
>           "type": "folder",
>           "children": [
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "obsidian_enhancing_export",
>           "type": "folder",
>           "children": [
>             {
>               "name": "lua",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "citefilter.lua",
>                   "type": "file"
>                 },
>                 {
>                   "name": "markdown+hugo.lua",
>                   "type": "file"
>                 },
>                 {
>                   "name": "markdown.lua",
>                   "type": "file"
>                 },
>                 {
>                   "name": "math_block.lua",
>                   "type": "file"
>                 },
>                 {
>                   "name": "newline_to_para.lua",
>                   "type": "file"
>                 },
>                 {
>                   "name": "pdf.lua",
>                   "type": "file"
>                 },
>                 {
>                   "name": "polyfill.lua",
>                   "type": "file"
>                 },
>                 {
>                   "name": "shift_headings.lua",
>                   "type": "file"
>                 },
>                 {
>                   "name": "url.lua",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "textemplate",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "dissertation.tex",
>                   "type": "file"
>                 },
>                 {
>                   "name": "neurips.sty",
>                   "type": "file"
>                 },
>                 {
>                   "name": "neurips.tex",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "obsidian_html_plugin",
>           "type": "folder",
>           "children": [
>             {
>               "name": "data.json",
>               "type": "file"
>             },
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "obsidian_markmind",
>           "type": "folder",
>           "children": [
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "obsidian_ocr",
>           "type": "folder",
>           "children": [
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "obsidian_pandoc",
>           "type": "folder",
>           "children": [
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "omnisearch",
>           "type": "folder",
>           "children": [
>             {
>               "name": "data.json",
>               "type": "file"
>             },
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "templater-obsidian",
>           "type": "folder",
>           "children": [
>             {
>               "name": "main.js",
>               "type": "file"
>             },
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "styles.css",
>               "type": "file"
>             }
>           ]
>         }
>       ]
>     },
>     {
>       "name": "themes",
>       "type": "folder",
>       "children": [
>         {
>           "name": "Border",
>           "type": "folder",
>           "children": [
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "theme.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "Obsidianotion",
>           "type": "folder",
>           "children": [
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "theme.css",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "Oxygen",
>           "type": "folder",
>           "children": [
>             {
>               "name": "manifest.json",
>               "type": "file"
>             },
>             {
>               "name": "theme.css",
>               "type": "file"
>             }
>           ]
>         }
>       ]
>     },
>     {
>       "name": "app.json",
>       "type": "file"
>     },
>     {
>       "name": "appearance.json",
>       "type": "file"
>     },
>     {
>       "name": "backlink.json",
>       "type": "file"
>     },
>     {
>       "name": "community-plugins.json",
>       "type": "file"
>     },
>     {
>       "name": "community_plugins.json",
>       "type": "file"
>     },
>     {
>       "name": "core-plugins.json",
>       "type": "file"
>     },
>     {
>       "name": "core_plugins.json",
>       "type": "file"
>     },
>     {
>       "name": "graph.json",
>       "type": "file"
>     },
>     {
>       "name": "types.json",
>       "type": "file"
>     },
>     {
>       "name": "workspace.json",
>       "type": "file"
>     }
>   ],
>   "metadata": {
>     "generated": "2026-03-09T02:00:42.462Z",
>     "generator": "FileTree Pro Extension",
>     "version": "0.2.0",
>     "showIcons": false,
>     "maxDepth": 10
>   }
> }

### Assistant
> Perfect. This is enough to see the shape of the mess.
> 
> ## First thing: you have too much junk in here
> 
> You already have plugin drift. Not fatal, but yes, it’s drift.
> 
> You’ve got:
> - duplicate config filenames:
>   - `community-plugins.json` and `community_plugins.json`
>   - `core-plugins.json` and `core_plugins.json`
> - overlapping export plugins
> - multiple visual/mindmap-ish plugins
> - plugins installed that we probably do not need for this vault
> 
> So before we “update settings,” we need to identify:
> 1. what is **enabled**
> 2. what is just **installed but unused**
> 3. what settings are actually active
> 
> ---
> 
> ## The files I want first
> 
> Send these **exact files** first, in this order:
> 
> ### 1. enabled community plugins
> ```text
> .obsidian/community-plugins.json
> ```
> 
> ### 2. enabled core plugins
> ```text
> .obsidian/core-plugins.json
> ```
> 
> ### 3. theme + appearance settings
> ```text
> .obsidian/appearance.json
> ```
> 
> ### 4. app behavior
> ```text
> .obsidian/app.json
> ```
> 
> ### 5. workspace layout
> ```text
> .obsidian/workspace.json
> ```
> 
> That gives me:
> - what’s on
> - what theme is active
> - how the UI is behaving
> - whether the layout is helping or hurting you
> 
> ---
> 
> ## Then send these plugin settings files
> 
> These are the ones I care about most for your setup:
> 
> ```text
> .obsidian/plugins/cmdr/data.json
> .obsidian/plugins/folder_notes/data.json
> .obsidian/plugins/metadata-menu/data.json
> .obsidian/plugins/note_uid_generator/data.json
> .obsidian/plugins/notebook_navigator/data.json
> .obsidian/plugins/obsidian-linter/data.json
> .obsidian/plugins/omnisearch/data.json
> ```
> 
> If it exists, also send:
> 
> ```text
> .obsidian/plugins/templater-obsidian/data.json
> ```
> 
> I noticed that folder does **not** show a `data.json`, which is interesting. That usually means either:
> - it has not been configured yet, or
> - the plugin stores defaults only until changed
> 
> ---
> 
> ## What I already suspect we’ll do
> 
> ### Keep likely
> - `dataview`
> - `templater-obsidian`
> - `obsidian-linter`
> - `metadata-menu`
> - `omnisearch`
> - `cmdr`
> - maybe `folder_notes`
> 
> ### Likely cut or disable for now
> - `better_export_pdf`
> - `export-to-html`
> - `obsidian_enhancing_export`
> - `obsidian_html_plugin`
> - `obsidian_pandoc`
> - `obsidian_ocr`
> - `obsidian-excalidraw-plugin`
> - `obsidian-mind-map`
> - `obsidian_markmind`
> - `markwhen`
> - `note_uid_generator` maybe
> - `notebook_navigator` maybe
> 
> Not because they’re bad. Because this vault is supposed to be functional, not a plugin petting zoo.
> 
> ---
> 
> ## One important thing I want you to check right now
> 
> Open these and compare them:
> 
> ```text
> .obsidian/community-plugins.json
> .obsidian/community_plugins.json
> .obsidian/core-plugins.json
> .obsidian/core_plugins.json
> ```
> 
> If both versions exist, one may be stale. Obsidian usually uses the hyphenated versions:
> - `community-plugins.json`
> - `core-plugins.json`
> 
> The underscore versions smell like leftovers or plugin-created junk.
> 
> Do **not** delete them yet. Just show me contents first.
> 
> ---
> 
> ## Clean next batch to paste
> 
> Paste these first:
> 
> ```text
> community-plugins.json
> core-plugins.json
> appearance.json
> app.json
> workspace.json
> ```
> 
> Then I’ll tell you:
> - what to keep
> - what to disable
> - what settings to change
> - what files to ignore
> - what your final baseline `.obsidian` should be

### Assistant
> Alright Cody — I looked through the configs you uploaded. Your vault is **actually pretty solid already**, but there are a few things I’d tweak to make it cleaner and more “QiVault / case-work machine” instead of just a normal Obsidian setup.
> 
> I’ll break this into **three quick layers** so it’s easy to act on.
> 
> ---
> 
> # 1. Your current core plugin stack (good)
> Your core plugins are mostly correct. Nothing scary here.
> 
> Enabled core plugins include things like:
> 
> - File explorer  
> - Graph  
> - Canvas  
> - Backlinks  
> - Templates  
> - Daily notes  
> - Slides  
> - Workspaces  
> 
> All of those are confirmed in your config. fileciteturn0file1  
> 
> That’s a **good baseline vault**.
> 
> I would **leave core plugins alone**.
> 
> ---
> 
> # 2. Community plugins you installed (this is the real system)
> 
> You basically built a **knowledge operating system** stack already.
> 
> Your major components:
> 
> ### Knowledge structure
> - Dataview
> - Metadata Menu
> - Folder Notes
> - UID Generator
> 
> This is your **database layer**.
> 
> Example:  
> Your UID generator is configured to auto-assign a UID across the vault. fileciteturn0file7  
> 
> That’s **perfect for QiDecimal style identity**.
> 
> ---
> 
> ### Navigation layer
> - Notebook Navigator
> - OmniSearch
> 
> This replaces Obsidian’s weak navigation.
> 
> OmniSearch is configured with fuzzy search and weighting. fileciteturn0file10  
> 
> That’s good for **large vaults like QiVault**.
> 
> ---
> 
> ### Visual / mapping layer
> - Excalidraw
> - Mind Map
> - Markmind
> - Markwhen
> 
> This is actually **overkill**.
> 
> You don’t need **three mindmap systems**.
> 
> Keep only:
> 
> ✔ Excalidraw  
> ✔ Markwhen  
> 
> Delete:
> 
> ❌ obsidian-mind-map  
> ❌ markmind
> 
> They overlap.
> 
> ---
> 
> ### Export / publishing
> You installed **four export systems**:
> 
> - better_export_pdf
> - enhancing_export
> - pandoc
> - export-to-html
> 
> You only need **two**.
> 
> Best combo:
> 
> ✔ Pandoc  
> ✔ Export to HTML
> 
> Delete:
> 
> ❌ better_export_pdf  
> ❌ enhancing_export
> 
> They create conflicts.
> 
> ---
> 
> ### System automation
> - templater
> - cmdr
> - linter
> 
> This is good but **linter is basically unused**.
> 
> All rules are disabled in your config. fileciteturn0file9  
> 
> So either:
> 
> • enable rules  
> or  
> • remove it
> 
> Right now it does nothing.
> 
> ---
> 
> # 3. Appearance (themes)
> 
> Your current theme:
> 
> **Border** fileciteturn0file2  
> 
> That’s actually a good theme for **clean professional docs**.
> 
> But if you want something closer to:
> 
> - Quartz websites
> - Material UI
> - glassy dashboards
> 
> Then install one of these.
> 
> ### Best themes for you
> 
> **ITS Theme**
> (best power user theme)
> 
> **Minimal**
> (best customization)
> 
> **AnuPpuccin**
> (best beautiful UI)
> 
> ---
> 
> # 4. The one plugin you are missing (huge)
> 
> You need:
> 
> ### **Advanced Tables**
> 
> For legal case work this is essential.
> 
> Also install:
> 
> ### **QuickAdd**
> 
> This lets you create:
> 
> - case note templates
> - evidence logs
> - exhibit generators
> - UID files
> 
> in seconds.
> 
> ---
> 
> # 5. The one setting you should change immediately
> 
> Your attachments are currently saved **in the same folder as notes**:
> 
> ```
> "attachmentFolderPath": "./"
> ```
> 
> fileciteturn0file3  
> 
> For a legal vault this is messy.
> 
> Change to:
> 
> ```
> _assets
> ```
> 
> or
> 
> ```
> /attachments
> ```
> 
> Trust me.
> 
> ---
> 
> # 6. The final plugin stack I recommend
> 
> For **QiVault + case work**:
> 
> ### Core knowledge
> - Dataview
> - Metadata Menu
> - UID Generator
> 
> ### Navigation
> - OmniSearch
> - Notebook Navigator
> 
> ### Visual thinking
> - Excalidraw
> - Markwhen
> 
> ### Automation
> - Templater
> - QuickAdd
> 
> ### Export
> - Pandoc
> - Export to HTML
> 
> ### Utility
> - Advanced Tables
> 
> ---
> 
> # 7. What I want to see next
> 
> If we’re going to **fully tune this vault**, I need two things:
> 
> **1️⃣ Dataview settings**
> ```
> plugins/dataview/data.json
> ```
> 
> **2️⃣ Templater settings**
> ```
> plugins/templater-obsidian/data.json
> ```
> 
> Those control **the real power of your system**.
> 
> ---
> 
> 💡 Also Cody — real talk:
> 
> Your Obsidian vault is **already halfway to being QiNote**.
> 
> You basically built:
> 
> ```
> QiVault (storage)
> +
> Dataview (database)
> +
> UID generator (identity)
> +
> Templater (automation)
> ```
> 
> That’s **literally a knowledge OS**.
> 
> We can take this **one step further** and make it a **case-management engine** if you want.
> 
> If you want, next I can show you:
> 
> **“The 7 plugins that turn Obsidian into a legal case intelligence system.”**
> 
> You’d probably love that setup.

### User
> there is no tdata json for datab view yet, and can you help me update the linter setting and create the tempaltes. {
>   "ruleConfigs": {
>     "add-blank-line-after-yaml": {
>       "enabled": false
>     },
>     "dedupe-yaml-array-values": {
>       "enabled": false,
>       "dedupe-alias-key": true,
>       "dedupe-tag-key": true,
>       "dedupe-array-keys": true,
>       "ignore-keys": ""
>     },
>     "escape-yaml-special-characters": {
>       "enabled": false,
>       "try-to-escape-single-line-arrays": false
>     },
>     "force-yaml-escape": {
>       "enabled": false,
>       "force-yaml-escape-keys": ""
>     },
>     "format-tags-in-yaml": {
>       "enabled": false
>     },
>     "format-yaml-array": {
>       "enabled": false,
>       "alias-key": true,
>       "tag-key": true,
>       "default-array-style": "single-line",
>       "default-array-keys": true,
>       "force-single-line-array-style": "",
>       "force-multi-line-array-style": ""
>     },
>     "insert-yaml-attributes": {
>       "enabled": false,
>       "text-to-insert": "aliases: \ntags: "
>     },
>     "move-tags-to-yaml": {
>       "enabled": false,
>       "how-to-handle-existing-tags": "Nothing",
>       "tags-to-ignore": ""
>     },
>     "remove-yaml-keys": {
>       "enabled": false,
>       "yaml-keys-to-remove": ""
>     },
>     "sort-yaml-array-values": {
>       "enabled": false,
>       "sort-alias-key": true,
>       "sort-tag-key": true,
>       "sort-array-keys": true,
>       "ignore-keys": "",
>       "sort-order": "Ascending Alphabetical"
>     },
>     "yaml-key-sort": {
>       "enabled": false,
>       "yaml-key-priority-sort-order": "",
>       "priority-keys-at-start-of-yaml": true,
>       "yaml-sort-order-for-other-keys": "None"
>     },
>     "yaml-timestamp": {
>       "enabled": false,
>       "date-created": true,
>       "date-created-key": "date created",
>       "date-created-source-of-truth": "file system",
>       "date-modified": true,
>       "date-modified-key": "date modified",
>       "date-modified-source-of-truth": "file system",
>       "format": "dddd, MMMM Do YYYY, h:mm:ss a",
>       "convert-to-utc": false,
>       "update-on-file-contents-updated": "never"
>     },
>     "yaml-title": {
>       "enabled": false,
>       "title-key": "title",
>       "mode": "first-h1-or-filename-if-h1-missing"
>     },
>     "yaml-title-alias": {
>       "enabled": false,
>       "preserve-existing-alias-section-style": true,
>       "keep-alias-that-matches-the-filename": false,
>       "use-yaml-key-to-keep-track-of-old-filename-or-heading": true,
>       "alias-helper-key": "linter-yaml-title-alias"
>     },
>     "capitalize-headings": {
>       "enabled": false,
>       "style": "Title Case",
>       "ignore-case-words": true,
>       "ignore-words": "macOS, iOS, iPhone, iPad, JavaScript, TypeScript, AppleScript, I",
>       "lowercase-words": "a, an, the, aboard, about, abt., above, abreast, absent, across, after, against, along, aloft, alongside, amid, amidst, mid, midst, among, amongst, anti, apropos, around, round, as, aslant, astride, at, atop, ontop, bar, barring, before, B4, behind, below, beneath, neath, beside, besides, between, 'tween, beyond, but, by, chez, circa, c., ca., come, concerning, contra, counting, cum, despite, spite, down, during, effective, ere, except, excepting, excluding, failing, following, for, from, in, including, inside, into, less, like, minus, modulo, mod, near, nearer, nearest, next, notwithstanding, of, o', off, offshore, on, onto, opposite, out, outside, over, o'er, pace, past, pending, per, plus, post, pre, pro, qua, re, regarding, respecting, sans, save, saving, short, since, sub, than, through, thru, throughout, thruout, till, times, to, t', touching, toward, towards, under, underneath, unlike, until, unto, up, upon, versus, vs., v., via, vice, vis-à-vis, wanting, with, w/, w., c̄, within, w/i, without, 'thout, w/o, abroad, adrift, aft, afterward, afterwards, ahead, apart, ashore, aside, away, back, backward, backwards, beforehand, downhill, downstage, downstairs, downstream, downward, downwards, downwind, east, eastward, eastwards, forth, forward, forwards, heavenward, heavenwards, hence, henceforth, here, hereby, herein, hereof, hereto, herewith, home, homeward, homewards, indoors, inward, inwards, leftward, leftwards, north, northeast, northward, northwards, northwest, now, onward, onwards, outdoors, outward, outwards, overboard, overhead, overland, overseas, rightward, rightwards, seaward, seawards, skywards, skyward, south, southeast, southwards, southward, southwest, then, thence, thenceforth, there, thereby, therein, thereof, thereto, therewith, together, underfoot, underground, uphill, upstage, upstairs, upstream, upward, upwards, upwind, west, westward, westwards, when, whence, where, whereby, wherein, whereto, wherewith, although, because, considering, given, granted, if, lest, once, provided, providing, seeing, so, supposing, though, unless, whenever, whereas, wherever, while, whilst, ago, inasmuch, even, whether, whose, whoever, why, how, whatever, what, both, and, or, either, neither, nor, just, rather, such, that, yet, is, it"
>     },
>     "file-name-heading": {
>       "enabled": false
>     },
>     "header-increment": {
>       "enabled": false,
>       "start-at-h2": false
>     },
>     "headings-start-line": {
>       "enabled": false
>     },
>     "remove-trailing-punctuation-in-heading": {
>       "enabled": false,
>       "punctuation-to-remove": ".,;:!。，；：！"
>     },
>     "footnote-after-punctuation": {
>       "enabled": false
>     },
>     "move-footnotes-to-the-bottom": {
>       "enabled": false,
>       "include-blank-line-between-footnotes": false
>     },
>     "re-index-footnotes": {
>       "enabled": false
>     },
>     "auto-correct-common-misspellings": {
>       "enabled": false,
>       "ignore-words": "",
>       "skip-words-with-multiple-capitals": false,
>       "extra-auto-correct-files": []
>     },
>     "blockquote-style": {
>       "enabled": false,
>       "style": "space"
>     },
>     "convert-bullet-list-markers": {
>       "enabled": false
>     },
>     "default-language-for-code-fences": {
>       "enabled": false,
>       "default-language": ""
>     },
>     "emphasis-style": {
>       "enabled": false,
>       "style": "consistent"
>     },
>     "no-bare-urls": {
>       "enabled": false,
>       "no-bare-uris": false
>     },
>     "ordered-list-style": {
>       "enabled": false,
>       "number-style": "ascending",
>       "list-end-style": "."
>     },
>     "proper-ellipsis": {
>       "enabled": false
>     },
>     "quote-style": {
>       "enabled": false,
>       "single-quote-enabled": true,
>       "single-quote-style": "''",
>       "double-quote-enabled": true,
>       "double-quote-style": "\"\""
>     },
>     "remove-consecutive-list-markers": {
>       "enabled": false
>     },
>     "remove-empty-list-markers": {
>       "enabled": false
>     },
>     "remove-hyphenated-line-breaks": {
>       "enabled": false
>     },
>     "remove-multiple-spaces": {
>       "enabled": false
>     },
>     "strong-style": {
>       "enabled": false,
>       "style": "consistent"
>     },
>     "two-spaces-between-lines-with-content": {
>       "enabled": false,
>       "line-break-indicator": "  "
>     },
>     "unordered-list-style": {
>       "enabled": false,
>       "list-style": "consistent"
>     },
>     "compact-yaml": {
>       "enabled": false,
>       "inner-new-lines": false
>     },
>     "consecutive-blank-lines": {
>       "enabled": false
>     },
>     "convert-spaces-to-tabs": {
>       "enabled": false,
>       "tabsize": 4
>     },
>     "empty-line-around-blockquotes": {
>       "enabled": false
>     },
>     "empty-line-around-code-fences": {
>       "enabled": false
>     },
>     "empty-line-around-horizontal-rules": {
>       "enabled": false
>     },
>     "empty-line-around-math-blocks": {
>       "enabled": false
>     },
>     "empty-line-around-tables": {
>       "enabled": false
>     },
>     "heading-blank-lines": {
>       "enabled": false,
>       "bottom": true,
>       "empty-line-after-yaml": true
>     },
>     "line-break-at-document-end": {
>       "enabled": false
>     },
>     "move-math-block-indicators-to-their-own-line": {
>       "enabled": false
>     },
>     "paragraph-blank-lines": {
>       "enabled": false
>     },
>     "remove-empty-lines-between-list-markers-and-checklists": {
>       "enabled": false
>     },
>     "remove-link-spacing": {
>       "enabled": false
>     },
>     "remove-space-around-characters": {
>       "enabled": false,
>       "include-fullwidth-forms": true,
>       "include-cjk-symbols-and-punctuation": true,
>       "include-dashes": true,
>       "other-symbols": ""
>     },
>     "remove-space-before-or-after-characters": {
>       "enabled": false,
>       "characters-to-remove-space-before": ",!?;:).’”]",
>       "characters-to-remove-space-after": "¿¡‘“(["
>     },
>     "space-after-list-markers": {
>       "enabled": false
>     },
>     "space-between-chinese-japanese-or-korean-and-english-or-numbers": {
>       "enabled": false,
>       "english-symbols-punctuation-before": "-+;:'\"°%$)]",
>       "english-symbols-punctuation-after": "-+'\"([¥$"
>     },
>     "trailing-spaces": {
>       "enabled": false,
>       "two-space-line-break": false
>     },
>     "add-blockquote-indentation-on-paste": {
>       "enabled": false
>     },
>     "prevent-double-checklist-indicator-on-paste": {
>       "enabled": false
>     },
>     "prevent-double-list-item-indicator-on-paste": {
>       "enabled": false
>     },
>     "proper-ellipsis-on-paste": {
>       "enabled": false
>     },
>     "remove-hyphens-on-paste": {
>       "enabled": false
>     },
>     "remove-leading-or-trailing-whitespace-on-paste": {
>       "enabled": false
>     },
>     "remove-leftover-footnotes-from-quote-on-paste": {
>       "enabled": false
>     },
>     "remove-multiple-blank-lines-on-paste": {
>       "enabled": false
>     }
>   },
>   "lintOnSave": false,
>   "recordLintOnSaveLogs": false,
>   "displayChanged": true,
>   "suppressMessageWhenNoChange": false,
>   "lintOnFileChange": false,
>   "displayLintOnFileChangeNotice": false,
>   "settingsConvertedToConfigKeyValues": true,
>   "additionalFileExtensions": [],
>   "foldersToIgnore": [],
>   "filesToIgnore": [],
>   "linterLocale": "system-default",
>   "logLevel": "ERROR",
>   "lintCommands": [],
>   "customRegexes": [],
>   "commonStyles": {
>     "aliasArrayStyle": "single-line",
>     "tagArrayStyle": "single-line",
>     "minimumNumberOfDollarSignsToBeAMathBlock": 2,
>     "escapeCharacter": "\"",
>     "removeUnnecessaryEscapeCharsForMultiLineArrays": false
>   }
> }

### Assistant
> Yep. And first: **it’s fine that Dataview has no `data.json` yet.** That usually just means you haven’t changed any plugin settings worth writing yet. Not a problem.
> 
> Your Linter config right now is basically **all bark, no bite** — almost everything is off, and `lintOnSave` is false. So let’s fix it **without letting Linter wreck your frontmatter schema**.
> 
> # What to do with Linter
> 
> ## Goal
> Use Linter for:
> - spacing
> - blank lines
> - endings
> - basic cleanup
> 
> Do **not** use it yet for:
> - YAML field insertion
> - YAML key sorting
> - timestamps
> - title generation
> - tag movement
> 
> That stuff should stay under your **manifest / schema control**, not Obsidian freestyle chaos.
> 
> ---
> 
> # Recommended Linter config
> 
> Replace your current `obsidian-linter/data.json` with this:
> 
> ```json
> {
>   "ruleConfigs": {
>     "add-blank-line-after-yaml": {
>       "enabled": true
>     },
>     "dedupe-yaml-array-values": {
>       "enabled": false,
>       "dedupe-alias-key": true,
>       "dedupe-tag-key": true,
>       "dedupe-array-keys": true,
>       "ignore-keys": ""
>     },
>     "escape-yaml-special-characters": {
>       "enabled": false,
>       "try-to-escape-single-line-arrays": false
>     },
>     "force-yaml-escape": {
>       "enabled": false,
>       "force-yaml-escape-keys": ""
>     },
>     "format-tags-in-yaml": {
>       "enabled": false
>     },
>     "format-yaml-array": {
>       "enabled": false,
>       "alias-key": true,
>       "tag-key": true,
>       "default-array-style": "single-line",
>       "default-array-keys": true,
>       "force-single-line-array-style": "",
>       "force-multi-line-array-style": ""
>     },
>     "insert-yaml-attributes": {
>       "enabled": false,
>       "text-to-insert": "aliases: \ntags: "
>     },
>     "move-tags-to-yaml": {
>       "enabled": false,
>       "how-to-handle-existing-tags": "Nothing",
>       "tags-to-ignore": ""
>     },
>     "remove-yaml-keys": {
>       "enabled": false,
>       "yaml-keys-to-remove": ""
>     },
>     "sort-yaml-array-values": {
>       "enabled": false,
>       "sort-alias-key": true,
>       "sort-tag-key": true,
>       "sort-array-keys": true,
>       "ignore-keys": "",
>       "sort-order": "Ascending Alphabetical"
>     },
>     "yaml-key-sort": {
>       "enabled": false,
>       "yaml-key-priority-sort-order": "",
>       "priority-keys-at-start-of-yaml": true,
>       "yaml-sort-order-for-other-keys": "None"
>     },
>     "yaml-timestamp": {
>       "enabled": false,
>       "date-created": true,
>       "date-created-key": "date created",
>       "date-created-source-of-truth": "file system",
>       "date-modified": true,
>       "date-modified-key": "date modified",
>       "date-modified-source-of-truth": "file system",
>       "format": "dddd, MMMM Do YYYY, h:mm:ss a",
>       "convert-to-utc": false,
>       "update-on-file-contents-updated": "never"
>     },
>     "yaml-title": {
>       "enabled": false,
>       "title-key": "title",
>       "mode": "first-h1-or-filename-if-h1-missing"
>     },
>     "yaml-title-alias": {
>       "enabled": false,
>       "preserve-existing-alias-section-style": true,
>       "keep-alias-that-matches-the-filename": false,
>       "use-yaml-key-to-keep-track-of-old-filename-or-heading": true,
>       "alias-helper-key": "linter-yaml-title-alias"
>     },
>     "capitalize-headings": {
>       "enabled": false,
>       "style": "Title Case",
>       "ignore-case-words": true,
>       "ignore-words": "macOS, iOS, iPhone, iPad, JavaScript, TypeScript, AppleScript, I",
>       "lowercase-words": "a, an, the"
>     },
>     "file-name-heading": {
>       "enabled": false
>     },
>     "header-increment": {
>       "enabled": false,
>       "start-at-h2": false
>     },
>     "headings-start-line": {
>       "enabled": false
>     },
>     "remove-trailing-punctuation-in-heading": {
>       "enabled": false,
>       "punctuation-to-remove": ".,;:!。，；：！"
>     },
>     "footnote-after-punctuation": {
>       "enabled": false
>     },
>     "move-footnotes-to-the-bottom": {
>       "enabled": false,
>       "include-blank-line-between-footnotes": false
>     },
>     "re-index-footnotes": {
>       "enabled": false
>     },
>     "auto-correct-common-misspellings": {
>       "enabled": false,
>       "ignore-words": "",
>       "skip-words-with-multiple-capitals": false,
>       "extra-auto-correct-files": []
>     },
>     "blockquote-style": {
>       "enabled": true,
>       "style": "space"
>     },
>     "convert-bullet-list-markers": {
>       "enabled": false
>     },
>     "default-language-for-code-fences": {
>       "enabled": false,
>       "default-language": ""
>     },
>     "emphasis-style": {
>       "enabled": false,
>       "style": "consistent"
>     },
>     "no-bare-urls": {
>       "enabled": false,
>       "no-bare-uris": false
>     },
>     "ordered-list-style": {
>       "enabled": false,
>       "number-style": "ascending",
>       "list-end-style": "."
>     },
>     "proper-ellipsis": {
>       "enabled": false
>     },
>     "quote-style": {
>       "enabled": false,
>       "single-quote-enabled": true,
>       "single-quote-style": "''",
>       "double-quote-enabled": true,
>       "double-quote-style": "\"\""
>     },
>     "remove-consecutive-list-markers": {
>       "enabled": true
>     },
>     "remove-empty-list-markers": {
>       "enabled": true
>     },
>     "remove-hyphenated-line-breaks": {
>       "enabled": false
>     },
>     "remove-multiple-spaces": {
>       "enabled": false
>     },
>     "strong-style": {
>       "enabled": false,
>       "style": "consistent"
>     },
>     "two-spaces-between-lines-with-content": {
>       "enabled": false,
>       "line-break-indicator": "  "
>     },
>     "unordered-list-style": {
>       "enabled": false,
>       "list-style": "consistent"
>     },
>     "compact-yaml": {
>       "enabled": false,
>       "inner-new-lines": false
>     },
>     "consecutive-blank-lines": {
>       "enabled": true
>     },
>     "convert-spaces-to-tabs": {
>       "enabled": false,
>       "tabsize": 4
>     },
>     "empty-line-around-blockquotes": {
>       "enabled": true
>     },
>     "empty-line-around-code-fences": {
>       "enabled": true
>     },
>     "empty-line-around-horizontal-rules": {
>       "enabled": true
>     },
>     "empty-line-around-math-blocks": {
>       "enabled": true
>     },
>     "empty-line-around-tables": {
>       "enabled": true
>     },
>     "heading-blank-lines": {
>       "enabled": true,
>       "bottom": true,
>       "empty-line-after-yaml": true
>     },
>     "line-break-at-document-end": {
>       "enabled": true
>     },
>     "move-math-block-indicators-to-their-own-line": {
>       "enabled": true
>     },
>     "paragraph-blank-lines": {
>       "enabled": false
>     },
>     "remove-empty-lines-between-list-markers-and-checklists": {
>       "enabled": true
>     },
>     "remove-link-spacing": {
>       "enabled": true
>     },
>     "remove-space-around-characters": {
>       "enabled": false,
>       "include-fullwidth-forms": true,
>       "include-cjk-symbols-and-punctuation": true,
>       "include-dashes": true,
>       "other-symbols": ""
>     },
>     "remove-space-before-or-after-characters": {
>       "enabled": false,
>       "characters-to-remove-space-before": ",!?;:).’”]",
>       "characters-to-remove-space-after": "¿¡‘“(["
>     },
>     "space-after-list-markers": {
>       "enabled": true
>     },
>     "space-between-chinese-japanese-or-korean-and-english-or-numbers": {
>       "enabled": false,
>       "english-symbols-punctuation-before": "-+;:'\"°%$)]",
>       "english-symbols-punctuation-after": "-+'\"([¥$"
>     },
>     "trailing-spaces": {
>       "enabled": true,
>       "two-space-line-break": false
>     },
>     "add-blockquote-indentation-on-paste": {
>       "enabled": false
>     },
>     "prevent-double-checklist-indicator-on-paste": {
>       "enabled": true
>     },
>     "prevent-double-list-item-indicator-on-paste": {
>       "enabled": true
>     },
>     "proper-ellipsis-on-paste": {
>       "enabled": false
>     },
>     "remove-hyphens-on-paste": {
>       "enabled": false
>     },
>     "remove-leading-or-trailing-whitespace-on-paste": {
>       "enabled": true
>     },
>     "remove-leftover-footnotes-from-quote-on-paste": {
>       "enabled": false
>     },
>     "remove-multiple-blank-lines-on-paste": {
>       "enabled": true
>     }
>   },
>   "lintOnSave": true,
>   "recordLintOnSaveLogs": false,
>   "displayChanged": true,
>   "suppressMessageWhenNoChange": true,
>   "lintOnFileChange": false,
>   "displayLintOnFileChangeNotice": false,
>   "settingsConvertedToConfigKeyValues": true,
>   "additionalFileExtensions": [],
>   "foldersToIgnore": [
>     ".obsidian",
>     "_attachments",
>     "_exports",
>     "_archive"
>   ],
>   "filesToIgnore": [],
>   "linterLocale": "system-default",
>   "logLevel": "ERROR",
>   "lintCommands": [],
>   "customRegexes": [],
>   "commonStyles": {
>     "aliasArrayStyle": "single-line",
>     "tagArrayStyle": "single-line",
>     "minimumNumberOfDollarSignsToBeAMathBlock": 2,
>     "escapeCharacter": "\"",
>     "removeUnnecessaryEscapeCharsForMultiLineArrays": false
>   }
> }
> ```
> 
> ## Why this version
> This setup gives you:
> - **safe formatting cleanup**
> - **clean blank lines**
> - **consistent code/table/list spacing**
> - **no YAML meddling**
> 
> So Linter becomes a janitor, not a rogue records clerk.
> 
> ---
> 
> # Templates you should create now
> 
> Make this folder:
> 
> ```text
> content/_templates/
> ```
> 
> And if you want script helpers later:
> 
> ```text
> content/_templates/scripts/
> ```
> 
> ## 1. case_event.md
> 
> ```md
> ---
> title: "<% tp.file.title %>"
> document_id: ""
> type: event
> status: draft
> matter_id: FCFCU_FORECLOSURE
> matter: Financial Center First Credit Union Foreclosure
> event_date: <% tp.date.now("YYYY-MM-DD") %>
> created: <% tp.date.now("YYYY-MM-DD") %>
> updated: <% tp.date.now("YYYY-MM-DD") %>
> tags: [case, event, fcfcu]
> aliases: []
> summary: ""
> source: ""
> actors: []
> related_documents: []
> ---
> 
> # <% tp.file.title %>
> 
> ## Summary
> 
> ## Facts
> 
> ## Evidence
> 
> ## Notes
> 
> ## Follow Up
> ```
> 
> ---
> 
> ## 2. exhibit_note.md
> 
> ```md
> ---
> title: "<% tp.file.title %>"
> document_id: ""
> type: exhibit
> status: draft
> matter_id: FCFCU_FORECLOSURE
> matter: Financial Center First Credit Union Foreclosure
> exhibit_id: ""
> created: <% tp.date.now("YYYY-MM-DD") %>
> updated: <% tp.date.now("YYYY-MM-DD") %>
> tags: [case, exhibit, evidence, fcfcu]
> aliases: []
> summary: ""
> source: ""
> source_file: ""
> date_of_document: ""
> related_events: []
> related_people: []
> ---
> 
> # <% tp.file.title %>
> 
> ## Description
> 
> ## Relevance
> 
> ## Source Details
> 
> ## Notes
> ```
> 
> ---
> 
> ## 3. motion_note.md
> 
> ```md
> ---
> title: "<% tp.file.title %>"
> document_id: ""
> type: motion
> status: draft
> matter_id: FCFCU_FORECLOSURE
> matter: Financial Center First Credit Union Foreclosure
> filing_date: <% tp.date.now("YYYY-MM-DD") %>
> created: <% tp.date.now("YYYY-MM-DD") %>
> updated: <% tp.date.now("YYYY-MM-DD") %>
> tags: [case, motion, filing, fcfcu]
> aliases: []
> summary: ""
> court: ""
> cause_number: ""
> related_exhibits: []
> related_issues: []
> ---
> 
> # <% tp.file.title %>
> 
> ## Purpose
> 
> ## Key Argument
> 
> ## Support
> 
> ## Requested Relief
> 
> ## Notes
> ```
> 
> ---
> 
> ## 4. issue_note.md
> 
> ```md
> ---
> title: "<% tp.file.title %>"
> document_id: ""
> type: issue
> status: active
> matter_id: FCFCU_FORECLOSURE
> matter: Financial Center First Credit Union Foreclosure
> created: <% tp.date.now("YYYY-MM-DD") %>
> updated: <% tp.date.now("YYYY-MM-DD") %>
> tags: [case, issue, fcfcu]
> aliases: []
> summary: ""
> issue_type: ""
> priority: medium
> related_events: []
> related_documents: []
> related_people: []
> ---
> 
> # <% tp.file.title %>
> 
> ## Issue
> 
> ## Why It Matters
> 
> ## Supporting Facts
> 
> ## Evidence
> 
> ## Open Questions
> 
> ## Next Step
> ```
> 
> ---
> 
> ## 5. person_note.md
> 
> ```md
> ---
> title: "<% tp.file.title %>"
> document_id: ""
> type: person
> status: active
> matter_id: FCFCU_FORECLOSURE
> matter: Financial Center First Credit Union Foreclosure
> created: <% tp.date.now("YYYY-MM-DD") %>
> updated: <% tp.date.now("YYYY-MM-DD") %>
> tags: [case, person, fcfcu]
> aliases: []
> summary: ""
> role: ""
> organization: ""
> contact_info: ""
> related_events: []
> related_documents: []
> ---
> 
> # <% tp.file.title %>
> 
> ## Role
> 
> ## Relevance
> 
> ## Contact / Reference
> 
> ## Notes
> ```
> 
> ---
> 
> ## 6. filing_note.md
> 
> ```md
> ---
> title: "<% tp.file.title %>"
> document_id: ""
> type: filing
> status: draft
> matter_id: FCFCU_FORECLOSURE
> matter: Financial Center First Credit Union Foreclosure
> filed_date: <% tp.date.now("YYYY-MM-DD") %>
> created: <% tp.date.now("YYYY-MM-DD") %>
> updated: <% tp.date.now("YYYY-MM-DD") %>
> tags: [case, filing, court, fcfcu]
> aliases: []
> summary: ""
> court: ""
> cause_number: ""
> filing_party: ""
> related_exhibits: []
> related_issues: []
> ---
> 
> # <% tp.file.title %>
> 
> ## Filing Summary
> 
> ## Main Points
> 
> ## Supporting Exhibits
> 
> ## Notes
> ```
> 
> ---
> 
> # Templater settings you should use
> 
> Once the plugin writes a `data.json`, these are the settings you want:
> 
> - Templates folder: `_templates`
> - Trigger Templater on new file creation: **ON**
> - User scripts folder: `_templates/scripts`
> - Folder templates: leave off for this second unless you want me to map note types by folder
> 
> ---
> 
> # Folder setup I’d use right now
> 
> Inside `content/`:
> 
> ```text
> _templates/
> _views/
> _events/
> _exhibits/
> _filings/
> _issues/
> _people/
> _notes/
> ```
> 
> That gives you structure without overengineering it.
> 
> ---
> 
> # One thing you should not do yet
> 
> Do **not** let templates get too clever yet with auto-generated IDs, court names, or dynamic logic.
> 
> Why? Because your frontmatter normalization project is still in flight.
> 
> First:
> - stabilize fields
> - stabilize template structure
> - stabilize naming
> 
> Then we get fancy.
> 
> ---
> 
> # Best next move
> 
> Do these in order:
> 
> 1. replace `obsidian-linter/data.json` with the version above
> 2. create `_templates/`
> 3. add the 6 templates above
> 4. point Templater to `_templates`
> 5. test on one sacrificial note, not your real case file
> 
> After that, we can build your `_views/` dashboard notes so Obsidian actually becomes useful instead of decorative.
> 
> If you want, next I’ll give you the **4 best dashboard notes**:
> - missing metadata
> - exhibit index
> - event timeline
> - issue tracker

### Assistant
> Perfect — this helps. I can see what you're doing and you're **very close to a stable system**, but a few things need tightening so it doesn't become chaos later.
> 
> I'll break this into **3 concrete fixes**:
> 
> 1️⃣ Fix **Linter so it doesn't wreck metadata**  
> 2️⃣ Create **Dataview config + views**  
> 3️⃣ Build **proper templates for your case vault**
> 
> No theory — just the exact files to drop in.
> 
> ---
> 
> # 1. Fix Linter (so it behaves)
> 
> Your current config is basically **disabled everything**, which defeats the purpose.
> 
> But we **do NOT let Linter control YAML fields**. Your Python manifest script should control those.
> 
> ### Replace this file
> 
> ```
> .obsidian/plugins/obsidian-linter/data.json
> ```
> 
> with:
> 
> ```json
> {
>   "lintOnSave": true,
>   "displayChanged": true,
>   "suppressMessageWhenNoChange": true,
>   "logLevel": "ERROR",
> 
>   "foldersToIgnore": [
>     ".obsidian",
>     "_templates",
>     "_exports"
>   ],
> 
>   "ruleConfigs": {
> 
>     "add-blank-line-after-yaml": { "enabled": true },
> 
>     "heading-blank-lines": {
>       "enabled": true,
>       "bottom": true,
>       "empty-line-after-yaml": true
>     },
> 
>     "consecutive-blank-lines": { "enabled": true },
> 
>     "empty-line-around-code-fences": { "enabled": true },
> 
>     "empty-line-around-tables": { "enabled": true },
> 
>     "empty-line-around-blockquotes": { "enabled": true },
> 
>     "remove-consecutive-list-markers": { "enabled": true },
> 
>     "remove-empty-list-markers": { "enabled": true },
> 
>     "space-after-list-markers": { "enabled": true },
> 
>     "remove-link-spacing": { "enabled": true },
> 
>     "line-break-at-document-end": { "enabled": true },
> 
>     "trailing-spaces": {
>       "enabled": true,
>       "two-space-line-break": false
>     }
> 
>   }
> }
> ```
> 
> ### What this does
> 
> Linter now only:
> 
> ✔ cleans formatting  
> ✔ removes spacing junk  
> ✔ normalizes markdown  
> 
> It **does not touch your YAML schema.**
> 
> Critical for legal documentation.
> 
> ---
> 
> # 2. Dataview Setup (you need this)
> 
> You currently have **Dataview installed but not configured.**
> 
> Create this file:
> 
> ```
> .obsidian/plugins/dataview/data.json
> ```
> 
> Put this in it:
> 
> ```json
> {
>   "renderNullAs": "-",
>   "taskCompletionTracking": true,
>   "taskCompletionUseEmojiShorthand": false,
>   "taskCompletionText": "done",
>   "taskCompletionDateFormat": "yyyy-MM-dd",
>   "recursiveSubTaskCompletion": false,
>   "warnOnEmptyResult": false,
>   "refreshEnabled": true,
>   "refreshInterval": 10000
> }
> ```
> 
> ---
> 
> # 3. Create Views (this is the real power)
> 
> Create a folder:
> 
> ```
> content/_views
> ```
> 
> ---
> 
> ## Case Event Timeline
> 
> `_views/timeline.md`
> 
> ```md
> # FCFCU Timeline
> 
> ```dataview
> TABLE event_date, summary, source
> FROM ""
> WHERE type = "event"
> SORT event_date ASC
> ```
> ```
> 
> ---
> 
> ## Exhibit Index
> 
> `_views/exhibits.md`
> 
> ```md
> # Exhibit Index
> 
> ```dataview
> TABLE exhibit_id, summary, source_file
> FROM ""
> WHERE type = "exhibit"
> SORT exhibit_id ASC
> ```
> ```
> 
> ---
> 
> ## Missing Metadata
> 
> This is the **one you'll use constantly**.
> 
> `_views/missing_metadata.md`
> 
> ```md
> # Missing Metadata
> 
> ```dataview
> TABLE file.name
> FROM ""
> WHERE !document_id OR !type OR !matter_id
> ```
> ```
> 
> This instantly shows:
> 
> - notes missing document IDs
> - notes missing type
> - notes missing matter
> 
> ---
> 
> ## Issues Tracker
> 
> `_views/issues.md`
> 
> ```md
> # Case Issues
> 
> ```dataview
> TABLE priority, status, summary
> FROM ""
> WHERE type = "issue"
> SORT priority DESC
> ```
> ```
> 
> ---
> 
> # 4. Templates Folder
> 
> Create this:
> 
> ```
> content/_templates
> ```
> 
> Add these files.
> 
> ---
> 
> ## event_template.md
> 
> ```md
> ---
> document_id:
> type: event
> matter_id: FCFCU_FORECLOSURE
> event_date:
> created:
> updated:
> tags: [case,event,fcfcu]
> summary:
> source:
> actors:
> related_documents:
> ---
> 
> # Event
> 
> ## Summary
> 
> ## Details
> 
> ## Evidence
> 
> ## Notes
> ```
> 
> ---
> 
> ## exhibit_template.md
> 
> ```md
> ---
> document_id:
> type: exhibit
> matter_id: FCFCU_FORECLOSURE
> exhibit_id:
> date_of_document:
> source_file:
> created:
> updated:
> tags: [case,exhibit,evidence,fcfcu]
> summary:
> ---
> 
> # Exhibit
> 
> ## Description
> 
> ## Relevance
> 
> ## Notes
> ```
> 
> ---
> 
> ## issue_template.md
> 
> ```md
> ---
> document_id:
> type: issue
> matter_id: FCFCU_FORECLOSURE
> priority: medium
> status: open
> created:
> updated:
> tags: [case,issue,fcfcu]
> summary:
> ---
> 
> # Issue
> 
> ## Description
> 
> ## Why It Matters
> 
> ## Evidence
> 
> ## Next Step
> ```
> 
> ---
> 
> # 5. Small but important vault structure change
> 
> Your case vault should look like this:
> 
> ```
> content
> │
> ├── _templates
> ├── _views
> │
> ├── events
> ├── exhibits
> ├── issues
> ├── filings
> ├── notes
> ```
> 
> This keeps Dataview queries **predictable**.
> 
> ---
> 
> # Important observation
> 
> Your plugin stack is actually **excellent already**:
> 
> You have:
> 
> ✔ Dataview  
> ✔ Metadata Menu  
> ✔ Linter  
> ✔ Omnisearch  
> ✔ Markwhen  
> ✔ UID Generator  
> 
> That combo is **seriously powerful** for a legal knowledge vault.
> 
> You're basically building a **case intelligence system**, not just notes.
> 
> ---
> 
> # If you want next level (seriously useful)
> 
> Next I can give you:
> 
> ### 1️⃣ a **Python script that auto-generates `document_id`**
> 
> Example:
> 
> ```
> FCF-EXH-001
> FCF-EVT-014
> FCF-MTN-003
> ```
> 
> ---
> 
> ### 2️⃣ a **manifest builder**
> 
> Exports the entire case vault into:
> 
> ```
> case_manifest.csv
> ```
> 
> With:
> 
> ```
> document_id
> type
> title
> date
> summary
> file_path
> ```
> 
> Perfect for court prep.
> 
> ---
> 
> ### 3️⃣ a **Dataview dashboard**
> 
> One page that shows:
> 
> - timeline
> - missing metadata
> - issues
> - exhibits
> 
> All together.
> 
> ---
> 
> If you want, I can also show you a **very slick trick to turn Obsidian into a case command center** (basically a dashboard page you open every time). It fits perfectly with how you're structuring this.

### User
> this is what you gave me. {
>   "ruleConfigs": {
>     "add-blank-line-after-yaml": {
>       "enabled": true
>     },
>     "dedupe-yaml-array-values": {
>       "enabled": false,
>       "dedupe-alias-key": true,
>       "dedupe-tag-key": true,
>       "dedupe-array-keys": true,
>       "ignore-keys": ""
>     },
>     "escape-yaml-special-characters": {
>       "enabled": false,
>       "try-to-escape-single-line-arrays": false
>     },
>     "force-yaml-escape": {
>       "enabled": false,
>       "force-yaml-escape-keys": ""
>     },
>     "format-tags-in-yaml": {
>       "enabled": false
>     },
>     "format-yaml-array": {
>       "enabled": false,
>       "alias-key": true,
>       "tag-key": true,
>       "default-array-style": "single-line",
>       "default-array-keys": true,
>       "force-single-line-array-style": "",
>       "force-multi-line-array-style": ""
>     },
>     "insert-yaml-attributes": {
>       "enabled": false,
>       "text-to-insert": "aliases: \ntags: "
>     },
>     "move-tags-to-yaml": {
>       "enabled": false,
>       "how-to-handle-existing-tags": "Nothing",
>       "tags-to-ignore": ""
>     },
>     "remove-yaml-keys": {
>       "enabled": false,
>       "yaml-keys-to-remove": ""
>     },
>     "sort-yaml-array-values": {
>       "enabled": false,
>       "sort-alias-key": true,
>       "sort-tag-key": true,
>       "sort-array-keys": true,
>       "ignore-keys": "",
>       "sort-order": "Ascending Alphabetical"
>     },
>     "yaml-key-sort": {
>       "enabled": false,
>       "yaml-key-priority-sort-order": "",
>       "priority-keys-at-start-of-yaml": true,
>       "yaml-sort-order-for-other-keys": "None"
>     },
>     "yaml-timestamp": {
>       "enabled": false,
>       "date-created": true,
>       "date-created-key": "date created",
>       "date-created-source-of-truth": "file system",
>       "date-modified": true,
>       "date-modified-key": "date modified",
>       "date-modified-source-of-truth": "file system",
>       "format": "dddd, MMMM Do YYYY, h:mm:ss a",
>       "convert-to-utc": false,
>       "update-on-file-contents-updated": "never"
>     },
>     "yaml-title": {
>       "enabled": false,
>       "title-key": "title",
>       "mode": "first-h1-or-filename-if-h1-missing"
>     },
>     "yaml-title-alias": {
>       "enabled": false,
>       "preserve-existing-alias-section-style": true,
>       "keep-alias-that-matches-the-filename": false,
>       "use-yaml-key-to-keep-track-of-old-filename-or-heading": true,
>       "alias-helper-key": "linter-yaml-title-alias"
>     },
>     "capitalize-headings": {
>       "enabled": false,
>       "style": "Title Case",
>       "ignore-case-words": true,
>       "ignore-words": "macOS, iOS, iPhone, iPad, JavaScript, TypeScript, AppleScript, I",
>       "lowercase-words": "a, an, the, aboard, about, abt., above, abreast, absent, across, after, against, along, aloft, alongside, amid, amidst, mid, midst, among, amongst, anti, apropos, around, round, as, aslant, astride, at, atop, ontop, bar, barring, before, B4, behind, below, beneath, neath, beside, besides, between, 'tween, beyond, but, by, chez, circa, c., ca., come, concerning, contra, counting, cum, despite, spite, down, during, effective, ere, except, excepting, excluding, failing, following, for, from, in, including, inside, into, less, like, minus, modulo, mod, near, nearer, nearest, next, notwithstanding, of, o', off, offshore, on, onto, opposite, out, outside, over, o'er, pace, past, pending, per, plus, post, pre, pro, qua, re, regarding, respecting, sans, save, saving, short, since, sub, than, through, thru, throughout, thruout, till, times, to, t', touching, toward, towards, under, underneath, unlike, until, unto, up, upon, versus, vs., v., via, vice, vis-à-vis, wanting, with, w/, w., c̄, within, w/i, without, 'thout, w/o, abroad, adrift, aft, afterward, afterwards, ahead, apart, ashore, aside, away, back, backward, backwards, beforehand, downhill, downstage, downstairs, downstream, downward, downwards, downwind, east, eastward, eastwards, forth, forward, forwards, heavenward, heavenwards, hence, henceforth, here, hereby, herein, hereof, hereto, herewith, home, homeward, homewards, indoors, inward, inwards, leftward, leftwards, north, northeast, northward, northwards, northwest, now, onward, onwards, outdoors, outward, outwards, overboard, overhead, overland, overseas, rightward, rightwards, seaward, seawards, skywards, skyward, south, southeast, southwards, southward, southwest, then, thence, thenceforth, there, thereby, therein, thereof, thereto, therewith, together, underfoot, underground, uphill, upstage, upstairs, upstream, upward, upwards, upwind, west, westward, westwards, when, whence, where, whereby, wherein, whereto, wherewith, although, because, considering, given, granted, if, lest, once, provided, providing, seeing, so, supposing, though, unless, whenever, whereas, wherever, while, whilst, ago, inasmuch, even, whether, whose, whoever, why, how, whatever, what, both, and, or, either, neither, nor, just, rather, such, that, yet, is, it"
>     },
>     "file-name-heading": {
>       "enabled": false
>     },
>     "header-increment": {
>       "enabled": false,
>       "start-at-h2": false
>     },
>     "headings-start-line": {
>       "enabled": false
>     },
>     "remove-trailing-punctuation-in-heading": {
>       "enabled": false,
>       "punctuation-to-remove": ".,;:!。，；：！"
>     },
>     "footnote-after-punctuation": {
>       "enabled": false
>     },
>     "move-footnotes-to-the-bottom": {
>       "enabled": false,
>       "include-blank-line-between-footnotes": false
>     },
>     "re-index-footnotes": {
>       "enabled": false
>     },
>     "auto-correct-common-misspellings": {
>       "enabled": false,
>       "ignore-words": "",
>       "skip-words-with-multiple-capitals": false,
>       "extra-auto-correct-files": []
>     },
>     "blockquote-style": {
>       "enabled": false,
>       "style": "space"
>     },
>     "convert-bullet-list-markers": {
>       "enabled": false
>     },
>     "default-language-for-code-fences": {
>       "enabled": false,
>       "default-language": ""
>     },
>     "emphasis-style": {
>       "enabled": false,
>       "style": "consistent"
>     },
>     "no-bare-urls": {
>       "enabled": false,
>       "no-bare-uris": false
>     },
>     "ordered-list-style": {
>       "enabled": false,
>       "number-style": "ascending",
>       "list-end-style": "."
>     },
>     "proper-ellipsis": {
>       "enabled": false
>     },
>     "quote-style": {
>       "enabled": false,
>       "single-quote-enabled": true,
>       "single-quote-style": "''",
>       "double-quote-enabled": true,
>       "double-quote-style": "\"\""
>     },
>     "remove-consecutive-list-markers": {
>       "enabled": false
>     },
>     "remove-empty-list-markers": {
>       "enabled": false
>     },
>     "remove-hyphenated-line-breaks": {
>       "enabled": false
>     },
>     "remove-multiple-spaces": {
>       "enabled": false
>     },
>     "strong-style": {
>       "enabled": false,
>       "style": "consistent"
>     },
>     "two-spaces-between-lines-with-content": {
>       "enabled": false,
>       "line-break-indicator": "  "
>     },
>     "unordered-list-style": {
>       "enabled": false,
>       "list-style": "consistent"
>     },
>     "compact-yaml": {
>       "enabled": false,
>       "inner-new-lines": false
>     },
>     "consecutive-blank-lines": {
>       "enabled": false
>     },
>     "convert-spaces-to-tabs": {
>       "enabled": false,
>       "tabsize": 4
>     },
>     "empty-line-around-blockquotes": {
>       "enabled": false
>     },
>     "empty-line-around-code-fences": {
>       "enabled": false
>     },
>     "empty-line-around-horizontal-rules": {
>       "enabled": false
>     },
>     "empty-line-around-math-blocks": {
>       "enabled": false
>     },
>     "empty-line-around-tables": {
>       "enabled": false
>     },
>     "heading-blank-lines": {
>       "enabled": false,
>       "bottom": true,
>       "empty-line-after-yaml": true
>     },
>     "line-break-at-document-end": {
>       "enabled": false
>     },
>     "move-math-block-indicators-to-their-own-line": {
>       "enabled": false
>     },
>     "paragraph-blank-lines": {
>       "enabled": false
>     },
>     "remove-empty-lines-between-list-markers-and-checklists": {
>       "enabled": false
>     },
>     "remove-link-spacing": {
>       "enabled": false
>     },
>     "remove-space-around-characters": {
>       "enabled": false,
>       "include-fullwidth-forms": true,
>       "include-cjk-symbols-and-punctuation": true,
>       "include-dashes": true,
>       "other-symbols": ""
>     },
>     "remove-space-before-or-after-characters": {
>       "enabled": false,
>       "characters-to-remove-space-before": ",!?;:).’”]",
>       "characters-to-remove-space-after": "¿¡‘“(["
>     },
>     "space-after-list-markers": {
>       "enabled": false
>     },
>     "space-between-chinese-japanese-or-korean-and-english-or-numbers": {
>       "enabled": false,
>       "english-symbols-punctuation-before": "-+;:'\"°%$)]",
>       "english-symbols-punctuation-after": "-+'\"([¥$"
>     },
>     "trailing-spaces": {
>       "enabled": false,
>       "two-space-line-break": false
>     },
>     "add-blockquote-indentation-on-paste": {
>       "enabled": false
>     },
>     "prevent-double-checklist-indicator-on-paste": {
>       "enabled": false
>     },
>     "prevent-double-list-item-indicator-on-paste": {
>       "enabled": false
>     },
>     "proper-ellipsis-on-paste": {
>       "enabled": false
>     },
>     "remove-hyphens-on-paste": {
>       "enabled": false
>     },
>     "remove-leading-or-trailing-whitespace-on-paste": {
>       "enabled": false
>     },
>     "remove-leftover-footnotes-from-quote-on-paste": {
>       "enabled": false
>     },
>     "remove-multiple-blank-lines-on-paste": {
>       "enabled": false
>     }
>   },
>   "lintOnSave": true,
>   "recordLintOnSaveLogs": false,
>   "displayChanged": true,
>   "suppressMessageWhenNoChange": false,
>   "lintOnFileChange": false,
>   "displayLintOnFileChangeNotice": false,
>   "settingsConvertedToConfigKeyValues": true,
>   "additionalFileExtensions": [],
>   "foldersToIgnore": [],
>   "filesToIgnore": [],
>   "linterLocale": "system-default",
>   "logLevel": "ERROR",
>   "lintCommands": [],
>   "customRegexes": [],
>   "commonStyles": {
>     "aliasArrayStyle": "single-line",
>     "tagArrayStyle": "single-line",
>     "minimumNumberOfDollarSignsToBeAMathBlock": 2,
>     "escapeCharacter": "\"",
>     "removeUnnecessaryEscapeCharsForMultiLineArrays": false
>   }
> }

### Assistant
> Yep. That version was the **safe baseline**, not the **actually useful tuned version**. It won’t break your YAML, but it’s still too timid.
> 
> Here’s the corrected call:
> 
> ## Keep OFF
> Do **not** turn these on:
> - all YAML mutation rules
> - yaml key sort
> - yaml timestamp
> - yaml title
> - move tags to yaml
> - insert yaml attributes
> 
> That part stays the same.
> 
> ## Turn ON
> These are the ones you should flip to `true` in the file you pasted:
> 
> ```json
> {
>   "add-blank-line-after-yaml": { "enabled": true },
>   "blockquote-style": { "enabled": true, "style": "space" },
>   "remove-consecutive-list-markers": { "enabled": true },
>   "remove-empty-list-markers": { "enabled": true },
>   "consecutive-blank-lines": { "enabled": true },
>   "empty-line-around-blockquotes": { "enabled": true },
>   "empty-line-around-code-fences": { "enabled": true },
>   "empty-line-around-horizontal-rules": { "enabled": true },
>   "empty-line-around-math-blocks": { "enabled": true },
>   "empty-line-around-tables": { "enabled": true },
>   "heading-blank-lines": {
>     "enabled": true,
>     "bottom": true,
>     "empty-line-after-yaml": true
>   },
>   "line-break-at-document-end": { "enabled": true },
>   "move-math-block-indicators-to-their-own-line": { "enabled": true },
>   "remove-empty-lines-between-list-markers-and-checklists": { "enabled": true },
>   "remove-link-spacing": { "enabled": true },
>   "space-after-list-markers": { "enabled": true },
>   "trailing-spaces": {
>     "enabled": true,
>     "two-space-line-break": false
>   },
>   "prevent-double-checklist-indicator-on-paste": { "enabled": true },
>   "prevent-double-list-item-indicator-on-paste": { "enabled": true },
>   "remove-leading-or-trailing-whitespace-on-paste": { "enabled": true },
>   "remove-multiple-blank-lines-on-paste": { "enabled": true }
> }
> ```
> 
> ## Also change these top-level settings
> 
> Change:
> 
> ```json
> "suppressMessageWhenNoChange": false,
> "foldersToIgnore": [],
> ```
> 
> to:
> 
> ```json
> "suppressMessageWhenNoChange": true,
> "foldersToIgnore": [
>   ".obsidian",
>   "_templates",
>   "_views",
>   "_exports"
> ],
> ```
> 
> That’s the real cleanup.
> 
> ---
> 
> ## So your file was not “wrong”
> It was just still too passive in four places:
> 
> 1. formatting rules mostly still off  
> 2. no ignored folders  
> 3. notifications too noisy  
> 4. still acting like a placeholder config  
> 
> ---
> 
> ## Clean final version
> 
> Use this whole file instead of hand-editing line by line:
> 
> ```json
> {
>   "ruleConfigs": {
>     "add-blank-line-after-yaml": {
>       "enabled": true
>     },
>     "dedupe-yaml-array-values": {
>       "enabled": false,
>       "dedupe-alias-key": true,
>       "dedupe-tag-key": true,
>       "dedupe-array-keys": true,
>       "ignore-keys": ""
>     },
>     "escape-yaml-special-characters": {
>       "enabled": false,
>       "try-to-escape-single-line-arrays": false
>     },
>     "force-yaml-escape": {
>       "enabled": false,
>       "force-yaml-escape-keys": ""
>     },
>     "format-tags-in-yaml": {
>       "enabled": false
>     },
>     "format-yaml-array": {
>       "enabled": false,
>       "alias-key": true,
>       "tag-key": true,
>       "default-array-style": "single-line",
>       "default-array-keys": true,
>       "force-single-line-array-style": "",
>       "force-multi-line-array-style": ""
>     },
>     "insert-yaml-attributes": {
>       "enabled": false,
>       "text-to-insert": "aliases: \ntags: "
>     },
>     "move-tags-to-yaml": {
>       "enabled": false,
>       "how-to-handle-existing-tags": "Nothing",
>       "tags-to-ignore": ""
>     },
>     "remove-yaml-keys": {
>       "enabled": false,
>       "yaml-keys-to-remove": ""
>     },
>     "sort-yaml-array-values": {
>       "enabled": false,
>       "sort-alias-key": true,
>       "sort-tag-key": true,
>       "sort-array-keys": true,
>       "ignore-keys": "",
>       "sort-order": "Ascending Alphabetical"
>     },
>     "yaml-key-sort": {
>       "enabled": false,
>       "yaml-key-priority-sort-order": "",
>       "priority-keys-at-start-of-yaml": true,
>       "yaml-sort-order-for-other-keys": "None"
>     },
>     "yaml-timestamp": {
>       "enabled": false,
>       "date-created": true,
>       "date-created-key": "date created",
>       "date-created-source-of-truth": "file system",
>       "date-modified": true,
>       "date-modified-key": "date modified",
>       "date-modified-source-of-truth": "file system",
>       "format": "dddd, MMMM Do YYYY, h:mm:ss a",
>       "convert-to-utc": false,
>       "update-on-file-contents-updated": "never"
>     },
>     "yaml-title": {
>       "enabled": false,
>       "title-key": "title",
>       "mode": "first-h1-or-filename-if-h1-missing"
>     },
>     "yaml-title-alias": {
>       "enabled": false,
>       "preserve-existing-alias-section-style": true,
>       "keep-alias-that-matches-the-filename": false,
>       "use-yaml-key-to-keep-track-of-old-filename-or-heading": true,
>       "alias-helper-key": "linter-yaml-title-alias"
>     },
>     "capitalize-headings": {
>       "enabled": false,
>       "style": "Title Case",
>       "ignore-case-words": true,
>       "ignore-words": "macOS, iOS, iPhone, iPad, JavaScript, TypeScript, AppleScript, I",
>       "lowercase-words": "a, an, the"
>     },
>     "file-name-heading": {
>       "enabled": false
>     },
>     "header-increment": {
>       "enabled": false,
>       "start-at-h2": false
>     },
>     "headings-start-line": {
>       "enabled": false
>     },
>     "remove-trailing-punctuation-in-heading": {
>       "enabled": false,
>       "punctuation-to-remove": ".,;:!。，；：！"
>     },
>     "footnote-after-punctuation": {
>       "enabled": false
>     },
>     "move-footnotes-to-the-bottom": {
>       "enabled": false,
>       "include-blank-line-between-footnotes": false
>     },
>     "re-index-footnotes": {
>       "enabled": false
>     },
>     "auto-correct-common-misspellings": {
>       "enabled": false,
>       "ignore-words": "",
>       "skip-words-with-multiple-capitals": false,
>       "extra-auto-correct-files": []
>     },
>     "blockquote-style": {
>       "enabled": true,
>       "style": "space"
>     },
>     "convert-bullet-list-markers": {
>       "enabled": false
>     },
>     "default-language-for-code-fences": {
>       "enabled": false,
>       "default-language": ""
>     },
>     "emphasis-style": {
>       "enabled": false,
>       "style": "consistent"
>     },
>     "no-bare-urls": {
>       "enabled": false,
>       "no-bare-uris": false
>     },
>     "ordered-list-style": {
>       "enabled": false,
>       "number-style": "ascending",
>       "list-end-style": "."
>     },
>     "proper-ellipsis": {
>       "enabled": false
>     },
>     "quote-style": {
>       "enabled": false,
>       "single-quote-enabled": true,
>       "single-quote-style": "''",
>       "double-quote-enabled": true,
>       "double-quote-style": "\"\""
>     },
>     "remove-consecutive-list-markers": {
>       "enabled": true
>     },
>     "remove-empty-list-markers": {
>       "enabled": true
>     },
>     "remove-hyphenated-line-breaks": {
>       "enabled": false
>     },
>     "remove-multiple-spaces": {
>       "enabled": false
>     },
>     "strong-style": {
>       "enabled": false,
>       "style": "consistent"
>     },
>     "two-spaces-between-lines-with-content": {
>       "enabled": false,
>       "line-break-indicator": "  "
>     },
>     "unordered-list-style": {
>       "enabled": false,
>       "list-style": "consistent"
>     },
>     "compact-yaml": {
>       "enabled": false,
>       "inner-new-lines": false
>     },
>     "consecutive-blank-lines": {
>       "enabled": true
>     },
>     "convert-spaces-to-tabs": {
>       "enabled": false,
>       "tabsize": 4
>     },
>     "empty-line-around-blockquotes": {
>       "enabled": true
>     },
>     "empty-line-around-code-fences": {
>       "enabled": true
>     },
>     "empty-line-around-horizontal-rules": {
>       "enabled": true
>     },
>     "empty-line-around-math-blocks": {
>       "enabled": true
>     },
>     "empty-line-around-tables": {
>       "enabled": true
>     },
>     "heading-blank-lines": {
>       "enabled": true,
>       "bottom": true,
>       "empty-line-after-yaml": true
>     },
>     "line-break-at-document-end": {
>       "enabled": true
>     },
>     "move-math-block-indicators-to-their-own-line": {
>       "enabled": true
>     },
>     "paragraph-blank-lines": {
>       "enabled": false
>     },
>     "remove-empty-lines-between-list-markers-and-checklists": {
>       "enabled": true
>     },
>     "remove-link-spacing": {
>       "enabled": true
>     },
>     "remove-space-around-characters": {
>       "enabled": false,
>       "include-fullwidth-forms": true,
>       "include-cjk-symbols-and-punctuation": true,
>       "include-dashes": true,
>       "other-symbols": ""
>     },
>     "remove-space-before-or-after-characters": {
>       "enabled": false,
>       "characters-to-remove-space-before": ",!?;:).’”]",
>       "characters-to-remove-space-after": "¿¡‘“(["
>     },
>     "space-after-list-markers": {
>       "enabled": true
>     },
>     "space-between-chinese-japanese-or-korean-and-english-or-numbers": {
>       "enabled": false,
>       "english-symbols-punctuation-before": "-+;:'\"°%$)]",
>       "english-symbols-punctuation-after": "-+'\"([¥$"
>     },
>     "trailing-spaces": {
>       "enabled": true,
>       "two-space-line-break": false
>     },
>     "add-blockquote-indentation-on-paste": {
>       "enabled": false
>     },
>     "prevent-double-checklist-indicator-on-paste": {
>       "enabled": true
>     },
>     "prevent-double-list-item-indicator-on-paste": {
>       "enabled": true
>     },
>     "proper-ellipsis-on-paste": {
>       "enabled": false
>     },
>     "remove-hyphens-on-paste": {
>       "enabled": false
>     },
>     "remove-leading-or-trailing-whitespace-on-paste": {
>       "enabled": true
>     },
>     "remove-leftover-footnotes-from-quote-on-paste": {
>       "enabled": false
>     },
>     "remove-multiple-blank-lines-on-paste": {
>       "enabled": true
>     }
>   },
>   "lintOnSave": true,
>   "recordLintOnSaveLogs": false,
>   "displayChanged": true,
>   "suppressMessageWhenNoChange": true,
>   "lintOnFileChange": false,
>   "displayLintOnFileChangeNotice": false,
>   "settingsConvertedToConfigKeyValues": true,
>   "additionalFileExtensions": [],
>   "foldersToIgnore": [
>     ".obsidian",
>     "_templates",
>     "_views",
>     "_exports"
>   ],
>   "filesToIgnore": [],
>   "linterLocale": "system-default",
>   "logLevel": "ERROR",
>   "lintCommands": [],
>   "customRegexes": [],
>   "commonStyles": {
>     "aliasArrayStyle": "single-line",
>     "tagArrayStyle": "single-line",
>     "minimumNumberOfDollarSignsToBeAMathBlock": 2,
>     "escapeCharacter": "\"",
>     "removeUnnecessaryEscapeCharsForMultiLineArrays": false
>   }
> }
> ```
> 
> ## Template note
> Given your current vault tree, don’t create generic `events/`, `issues/`, etc. folders right now. You already have a real structure in place with `03_EVENTS`, `02_VIOLATIONS`, phase folders, and task/doc subtrees. fileciteturn1file0
> 
> So the smarter move is:
> - create `_templates`
> - create `_views`
> - leave your existing substantive folder tree alone
> 
> ## Next best move
> Create these only:
> - `_templates/event_template.md`
> - `_templates/exhibit_template.md`
> - `_templates/issue_template.md`
> - `_templates/filing_template.md`
> - `_views/missing_metadata.md`
> - `_views/timeline.md`
> 
> That gets you traction without starting another reorg spiral.

### User
> also you said somethign about a landing page for wheni get int ehre.

### Assistant
> Yep — this is actually one of the **best things you can do for ADHD and large vaults**: make a **Home / Command Center page** that opens every time the vault loads. It becomes your **mission control**.
> 
> You already uploaded a draft file (`Untitled-2.md`). That’s perfect — we’ll convert that idea into a proper **vault landing page**.
> 
> ---
> 
> # 1. Create the Home Page
> 
> Create this file:
> 
> ```
> content/_views/home.md
> ```
> 
> Paste this:
> 
> ```markdown
> ---
> title: FCFCU Case Command Center
> type: dashboard
> matter_id: FCFCU_FORECLOSURE
> ---
> 
> # ⚖️ FCFCU Case Command Center
> 
> ## Quick Navigation
> 
> - [[_views/timeline|📅 Case Timeline]]
> - [[_views/exhibits|📂 Exhibit Index]]
> - [[_views/issues|⚠️ Case Issues]]
> - [[_views/missing_metadata|🔎 Missing Metadata]]
> 
> ---
> 
> ## ⚠️ Open Issues
> 
> ```dataview
> TABLE priority, summary
> FROM ""
> WHERE type = "issue" AND status != "resolved"
> SORT priority DESC
> ```
> 
> ---
> 
> ## 📅 Recent Events
> 
> ```dataview
> TABLE event_date, summary
> FROM ""
> WHERE type = "event"
> SORT event_date DESC
> LIMIT 10
> ```
> 
> ---
> 
> ## 📂 Recent Documents
> 
> ```dataview
> TABLE file.mtime as Modified
> FROM ""
> SORT file.mtime DESC
> LIMIT 10
> ```
> 
> ---
> 
> ## 🔎 Metadata Problems
> 
> ```dataview
> TABLE file.name
> FROM ""
> WHERE !document_id OR !type OR !matter_id
> LIMIT 20
> ```
> 
> ---
> 
> ## 📝 Quick Create
> 
> Templates:
> 
> - Create Event → `_templates/event_template`
> - Create Exhibit → `_templates/exhibit_template`
> - Create Issue → `_templates/issue_template`
> - Create Filing → `_templates/filing_template`
> ```
> 
> ---
> 
> # 2. Make Obsidian Open This Page Automatically
> 
> Open:
> 
> ```
> Settings → Core Plugins → Workspaces
> ```
> 
> Turn **Workspaces ON**.
> 
> Then:
> 
> 1. Open the page  
>    ```
>    _views/home.md
>    ```
> 
> 2. Set layout how you want (sidebars etc).
> 
> 3. Go to:
> 
> ```
> Command Palette → Save workspace
> ```
> 
> Name it:
> 
> ```
> Case Command Center
> ```
> 
> 4. Enable:
> 
> ```
> Load last workspace on startup
> ```
> 
> Now whenever you open the vault, **this page loads first**.
> 
> ---
> 
> # 3. Optional (but very helpful)
> 
> Pin the page so it never disappears.
> 
> Right-click the tab → **Pin**.
> 
> ---
> 
> # 4. Add Quick Buttons (Commander plugin)
> 
> Since you installed **Commander**, you can add buttons for quick note creation.
> 
> Add commands:
> 
> ```
> Templater: Create new note from template
> ```
> 
> Buttons:
> 
> ```
> ➕ Event
> ➕ Exhibit
> ➕ Issue
> ➕ Filing
> ```
> 
> Then your vault behaves more like a **case management app**.
> 
> ---
> 
> # 5. Why this matters for your case
> 
> Instead of hunting through folders, you open Obsidian and immediately see:
> 
> - new documents
> - unresolved issues
> - event timeline
> - missing metadata
> - quick creation tools
> 
> It becomes a **case cockpit**, not a note pile.
> 
> ---
> 
> # 6. Small improvement I’d add
> 
> Add this to the very top of the page:
> 
> ```markdown
> > ⚖️ **Matter:** Financial Center First Credit Union Foreclosure  
> > **Cause Number:** 49D03-2501-MF-002559  
> > **Court:** Marion Superior Court 3
> ```
> 
> That keeps the legal context front-and-center.
> 
> ---
> 
> 💡 If you want, the **next upgrade** I’d suggest (this is powerful) is a **single page that shows your entire litigation posture**:
> 
> - Timeline  
> - Violations  
> - Exhibits  
> - Claims  
> - Financial damages  
> 
> All on one dashboard.
> 
> It’s the kind of view lawyers normally build in **$10k litigation software** — but you can do it in Obsidian with about **20 lines of Dataview.**

### User
> {'asset_pointer': 'sediment://file_00000000b01871fd887a382b1caeadf0', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 1068, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 275095, 'width': 1897}this is much better for me,

### Assistant
> Yes — **this is exactly the right direction.** 👏  
> What you built here is basically a **case command dashboard**, and it’s already doing three things correctly:
> 
> - one **entry point** (`_home`)
> - one **navigation spine** (your numbered folders)
> - one **status layer** (Dataview tables)
> 
> That’s the right mental model for ADHD + complex cases.
> 
> Now let me tighten a few things so it becomes **rock-solid and frictionless**.
> 
> ---
> 
> # 1. Fix the Event Date Showing as Code
> Right now your dashboard shows:
> 
> ```
> <% tp.date.now("YYYY-MM-DD") %>
> ```
> 
> That means the **Templater variable never executed**.
> 
> Templater only runs when creating a note **via the template command**, not when the file already exists.
> 
> So change your template field to this:
> 
> ```yaml
> event_date: {{date}}
> ```
> 
> or better:
> 
> ```yaml
> event_date: <% tp.date.now("YYYY-MM-DD") %>
> ```
> 
> BUT make sure the note is created using:
> 
> ```
> Templater: Create new note from template
> ```
> 
> Then it will populate correctly.
> 
> ---
> 
> # 2. Improve the Home Dashboard Layout
> 
> Your page is good, but we can make it **scan faster**.
> 
> Replace the top section with this:
> 
> ```markdown
> # ⚖️ FCFCU Case Command Center
> 
> > **Cause Number:** 49D03-2501-MF-002559  
> > **Court:** Marion Superior Court 3  
> > **Matter:** Financial Center First Credit Union Foreclosure
> 
> ---
> 
> ## 📍 Quick Navigation
> 
> | Section | Link |
> |------|------|
> | 📅 Timeline | [[Case Timeline]] |
> | 📂 Exhibits | [[Exhibit Index]] |
> | ⚠️ Issues | [[Case Issues]] |
> | 🔎 Missing Metadata | [[Missing Metadata]] |
> 
> ---
> ```
> 
> Tables scan faster than bullet lists.
> 
> ---
> 
> # 3. Make the Issues Table Better
> 
> Replace your issues block with this:
> 
> ```dataview
> TABLE priority, summary, file.mtime AS updated
> FROM ""
> WHERE type = "issue" AND status != "resolved"
> SORT priority DESC
> ```
> 
> Now you'll see:
> 
> - priority
> - summary
> - last update
> 
> This helps when issues evolve.
> 
> ---
> 
> # 4. Add an Evidence Table (you’ll want this soon)
> 
> Add this below issues:
> 
> ```markdown
> ## 📂 Exhibits
> 
> ```dataview
> TABLE exhibit_id, summary
> FROM ""
> WHERE type = "exhibit"
> SORT exhibit_id ASC
> LIMIT 10
> ```
> ```
> 
> That gives you a **quick evidence index**.
> 
> ---
> 
> # 5. Your Folder Structure is Excellent
> 
> Your sidebar shows:
> 
> ```
> 00_CASE_MASTER
> 01_PHASES
> 02_VIOLATIONS
> 03_EVENTS
> 04_DOCUMENTS
> 05_DISPUTES
> 06_DAMAGES
> 07_ACTORS
> 99_VAULT
> ```
> 
> That is **exactly the right hierarchy for a legal knowledge vault.**
> 
> You already separated:
> 
> - evidence
> - violations
> - damages
> - actors
> 
> That’s **litigation-grade organization**.
> 
> ---
> 
> # 6. One Small Navigation Trick
> 
> Pin `_home`.
> 
> Right-click tab → **Pin**
> 
> Then you always have your dashboard.
> 
> ---
> 
> # 7. One Plugin Feature That Will Help A LOT
> 
> Since you have **Commander**, add buttons:
> 
> ```
> ➕ Event
> ➕ Exhibit
> ➕ Issue
> ➕ Filing
> ```
> 
> They call:
> 
> ```
> Templater: Create new note from template
> ```
> 
> Then your vault behaves like a **case management system**.
> 
> ---
> 
> # 8. Your Graph is Actually Useful
> 
> That graph on the right is interesting.
> 
> Because if you maintain:
> 
> ```
> related_documents
> related_events
> actors
> issues
> ```
> 
> the graph becomes a **relationship map of the litigation**.
> 
> This is something lawyers normally pay for in tools like:
> 
> - Relativity
> - CaseMap
> - Everlaw
> 
> But Obsidian can do it free.
> 
> ---
> 
> # 9. One Last Improvement (small but huge)
> 
> Add this to the very bottom of the home page:
> 
> ```markdown
> ## 🕒 Recently Modified
> 
> ```dataview
> TABLE file.mtime AS Modified
> FROM ""
> SORT file.mtime DESC
> LIMIT 10
> ```
> ```
> 
> Now you always see the **last things you touched**.
> 
> That’s extremely helpful in big vaults.
> 
> ---
> 
> # What you built here is actually the correct pattern
> 
> You are essentially creating:
> 
> ```
> Case Vault
>     ↓
> Structured Notes
>     ↓
> Metadata
>     ↓
> Dataview Dashboard
> ```
> 
> That’s **exactly how knowledge systems should work.**
> 
> ---
> 
> If you want, the **next thing I can show you** will make this vault *really powerful*:
> 
> ### A "Case Intelligence Dashboard"
> 
> One page that automatically shows:
> 
> - violations timeline
> - damages tracker
> - evidence list
> - dispute status
> - actors map
> 
> Basically turning Obsidian into a **litigation command center**.

### User
> ok so now we got some views how do i get those table to populate from what we have is it fornt matter.

### Assistant
> Yes. **Mostly frontmatter.** That’s the engine.
> 
> Dataview can populate from three places:
> 
> 1. **Frontmatter** at the top of notes  
> 2. **Inline fields** inside note bodies  
> 3. **Built-in file metadata** like file name, path, created/modified time
> 
> Right now your tables are working because Dataview can already see some notes with fields like `type`, `priority`, and `summary`, and it can always see `file.name` and `file.mtime`. Your vault already has a structured folder system and a `_home` dashboard pattern, which is a good base for this. fileciteturn1file0
> 
> # The simple rule
> 
> If a Dataview table says:
> 
> ```dataview
> TABLE event_date, summary
> FROM ""
> WHERE type = "event"
> ```
> 
> then each matching note needs those fields somewhere Dataview can read them.
> 
> Usually that means this at the top:
> 
> ```yaml
> ---
> type: event
> event_date: 2025-12-09
> summary: Sheriff executed writ and forced removal
> ---
> ```
> 
> Without that, Dataview has nothing to grab except file metadata.
> 
> # What Dataview can read
> 
> ## 1. Frontmatter
> Best option for your case vault.
> 
> Example:
> 
> ```yaml
> ---
> document_id: EVT-FCFCU-2025-0001
> type: event
> matter_id: FCFCU_FORECLOSURE
> event_date: 2025-12-09
> summary: Sheriff executed writ and forced removal
> status: active
> ---
> ```
> 
> Then this works:
> 
> ```dataview
> TABLE event_date, summary, status
> FROM ""
> WHERE type = "event"
> ```
> 
> ## 2. Inline fields
> These go inside the body:
> 
> ```md
> event_date:: 2025-12-09
> summary:: Sheriff executed writ and forced removal
> type:: event
> ```
> 
> Dataview can read those too.
> 
> Good for quick notes, but for your system I’d use **frontmatter first**. It’s cleaner, more consistent, and easier for your Python manifest scripts.
> 
> ## 3. Built-in file metadata
> Dataview always knows things like:
> 
> - `file.name`
> - `file.path`
> - `file.folder`
> - `file.link`
> - `file.ctime`
> - `file.mtime`
> - `file.tags`
> 
> So this works even with no frontmatter:
> 
> ```dataview
> TABLE file.name, file.mtime
> FROM ""
> SORT file.mtime DESC
> ```
> 
> That’s why your recent documents block can populate even when metadata is incomplete.
> 
> # Why some of your tables are half-working
> 
> Because your vault already has a lot of notes, but most of the older notes probably do **not** yet have normalized frontmatter. Your file tree shows tons of markdown across `02_VIOLATIONS`, `03_EVENTS`, phase folders, and more, but the structure of those note files is likely inconsistent right now. fileciteturn1file0
> 
> So:
> - tables using `file.name` or `file.mtime` work easily
> - tables using `event_date`, `summary`, `priority`, `type`, `exhibit_id` only populate if those fields exist
> 
> # Best way to populate from what you already have
> 
> Do this in order.
> 
> ## Option A — easiest and smartest
> Use your **frontmatter manifest workflow**.
> 
> That means:
> 1. export all notes to CSV
> 2. see which notes are missing fields
> 3. map values in CSV
> 4. dry run
> 5. apply back to notes
> 
> That is the clean bulk approach.
> 
> ## Option B — for a few notes only
> Open a note and manually add frontmatter.
> 
> Example for an event note:
> 
> ```yaml
> ---
> document_id: EVT-FCFCU-2025-0001
> type: event
> matter_id: FCFCU_FORECLOSURE
> event_date: 2025-12-09
> summary: Forced removal executed under writ
> status: active
> ---
> ```
> 
> Then it instantly appears in the timeline table.
> 
> # What fields you should standardize first
> 
> For your dashboard to become useful fast, focus on just these:
> 
> ```yaml
> document_id:
> type:
> matter_id:
> summary:
> status:
> ```
> 
> Then add one type-specific field depending on note type:
> 
> ## Event notes
> ```yaml
> event_date:
> ```
> 
> ## Exhibit notes
> ```yaml
> exhibit_id:
> source_file:
> date_of_document:
> ```
> 
> ## Issue notes
> ```yaml
> priority:
> ```
> 
> ## Filing notes
> ```yaml
> filed_date:
> court:
> ```
> 
> That’s enough to make most dashboards useful.
> 
> # Best Dataview pattern for your existing vault
> 
> Since your files are still being normalized, use **fallback-friendly queries**.
> 
> Instead of this:
> 
> ```dataview
> TABLE event_date, summary
> FROM ""
> WHERE type = "event"
> ```
> 
> use this:
> 
> ```dataview
> TABLE event_date, summary, file.link
> FROM ""
> WHERE type = "event" OR contains(file.folder, "03_EVENTS")
> SORT event_date ASC
> ```
> 
> That way:
> - frontmatter-tagged event notes show up
> - notes in the `03_EVENTS` folder can still be caught while you normalize them
> 
> Your vault clearly has a dedicated `03_EVENTS` section already, so folder-based fallback is useful during transition. fileciteturn1file0
> 
> # Even better: transition queries
> 
> ## Timeline
> ```dataview
> TABLE event_date, summary, file.link
> FROM ""
> WHERE type = "event" OR contains(file.path, "03_EVENTS")
> SORT event_date ASC
> ```
> 
> ## Issues
> ```dataview
> TABLE priority, summary, file.link
> FROM ""
> WHERE type = "issue" OR contains(file.name, "issue")
> SORT priority DESC
> ```
> 
> ## Recent docs
> ```dataview
> TABLE file.mtime AS Modified, file.link
> FROM ""
> SORT file.mtime DESC
> LIMIT 15
> ```
> 
> These are imperfect, but good while the metadata is still messy.
> 
> # What I recommend for you
> 
> ## Right now
> Use Dataview with:
> - frontmatter where it exists
> - file metadata everywhere
> - folder-based fallback while normalizing
> 
> ## Over the next cleanup pass
> Use your manifest process to backfill:
> - `type`
> - `document_id`
> - `matter_id`
> - `summary`
> - `event_date` / `priority` / `exhibit_id` / `filed_date`
> 
> Then your dashboards stop being “best effort” and become reliable.
> 
> # Fast test
> 
> Pick one note in `03_EVENTS`, one in `02_VIOLATIONS`, and one exhibit/doc note.
> 
> Add frontmatter like this:
> 
> ```yaml
> ---
> document_id: TEST-001
> type: event
> matter_id: FCFCU_FORECLOSURE
> event_date: 2025-12-09
> summary: Test event for dashboard
> status: active
> ---
> ```
> 
> Save it.
> 
> If it appears in your Dataview table, then yes — frontmatter is the missing fuel.
> 
> # Bottom line
> 
> **Dataview tables populate from metadata, and frontmatter is the cleanest source of truth.**  
> For your vault:
> 
> - use `file.*` fields immediately
> - use folder fallback during transition
> - use frontmatter as the long-term system
> - use the manifest CSV to backfill the old notes in bulk
> 
> Next move should be building a **field map by note type** so you know exactly what each class of note needs.

### User
> ok so nowe we are at the get the front matter/properties correct so these views work, we can clean up folders and front matter now. her eis the most recent tree

### Assistant
> Yes. Now we’re at the **real work**:
> 
> 1. lock the folder rules  
> 2. lock the frontmatter schema  
> 3. use that schema to make the views reliable  
> 4. only then do bulk cleanup
> 
> And your latest tree is actually good enough to stop guessing. It shows the vault already has a strong top-level spine:
> `00_CASE_MASTER`, `01_PHASES`, `02_VIOLATIONS`, `03_EVENTS`, plus admin/references/reports areas under case master. fileciteturn2file0
> 
> ## My blunt read
> 
> Your problem is **not** that the structure is bad.
> 
> Your problem is:
> - some folders are **content folders**
> - some are **admin/system folders**
> - some notes are probably missing consistent `type`, `matter_id`, `summary`, dates, and IDs
> - your views are trying to query a vault that still behaves partly like a file archive and partly like a knowledge base
> 
> So don’t do a giant reorg yet. Do a **targeted normalization pass**.
> 
> # Step 1: lock what each top-level folder means
> 
> Use this as the current rule set:
> 
> ```text
> 00_CASE_MASTER = dashboard, master summaries, admin, reports, references
> 01_PHASES      = strategy/workstreams/phases/tasks/docs tied to phase structure
> 02_VIOLATIONS  = violation/theory/claim notes
> 03_EVENTS      = dated event notes / timeline items
> 04_DOCUMENTS   = document/exhibit/record notes
> 05_DISPUTES    = dispute workflows and regulator dispute notes
> 06_DAMAGES     = harm, damages, financial impact, valuation
> 07_ACTORS      = people, orgs, agencies, counterparties
> 99_VAULT       = utility, sandbox, temp, internal helper notes only
> ```
> 
> That top-level logic is already emerging from your tree. Keep it. fileciteturn2file0
> 
> # Step 2: separate “content” from “system”
> 
> You already have `_admin`, `captures`, `docs`, `references`, and `reports` under `00_CASE_MASTER`. That’s fine, but treat them as **system/support**, not normal content queried with the same logic as events/issues/violations. fileciteturn2file0
> 
> So:
> 
> ## Queryable content folders
> - `01_PHASES`
> - `02_VIOLATIONS`
> - `03_EVENTS`
> - `04_DOCUMENTS`
> - `05_DISPUTES`
> - `06_DAMAGES`
> - `07_ACTORS`
> 
> ## Mostly excluded from dashboard logic
> - `00_CASE_MASTER/_admin/captures`
> - `00_CASE_MASTER/_admin/docs`
> - `00_CASE_MASTER/_admin/references`
> - `00_CASE_MASTER/_admin/reports`
> - `99_VAULT`
> 
> That matters because Dataview should not treat a raw HTML capture or extracted text dump like a first-class case note.
> 
> # Step 3: lock the minimum frontmatter schema
> 
> Do not overbuild this. Use the minimum set that powers views.
> 
> ## Required on all queryable markdown notes
> 
> ```yaml
> ---
> title:
> document_id:
> type:
> matter_id:
> status:
> summary:
> created:
> updated:
> ---
> ```
> 
> ## Recommended common optional fields
> 
> ```yaml
> tags: []
> aliases: []
> source: ""
> source_file: ""
> related_documents: []
> related_events: []
> related_people: []
> related_issues: []
> ```
> 
> ## Type-specific fields
> 
> ### `type: event`
> ```yaml
> event_date:
> actors: []
> ```
> 
> ### `type: violation`
> ```yaml
> violation_code:
> violation_category:
> priority:
> ```
> 
> ### `type: document`
> ```yaml
> document_date:
> document_kind:
> exhibit_id:
> ```
> 
> ### `type: dispute`
> ```yaml
> agency:
> sent_date:
> deadline_date:
> ```
> 
> ### `type: damage`
> ```yaml
> damage_category:
> amount:
> date_range:
> ```
> 
> ### `type: actor`
> ```yaml
> actor_type:
> organization:
> role:
> ```
> 
> ### `type: phase`
> ```yaml
> phase_id:
> phase_status:
> ```
> 
> # Step 4: use folder-to-type defaults
> 
> This is how you move fast without hand-thinking every file.
> 
> ## Folder default mapping
> 
> ```text
> 01_PHASES      -> type: phase   (or task/document if clearly specialized)
> 02_VIOLATIONS  -> type: violation
> 03_EVENTS      -> type: event
> 04_DOCUMENTS   -> type: document
> 05_DISPUTES    -> type: dispute
> 06_DAMAGES     -> type: damage
> 07_ACTORS      -> type: actor
> ```
> 
> Important: this should be your **bulk backfill default**, not a forever rule. There will be exceptions. But it’s the right first pass.
> 
> # Step 5: lock your core matter fields
> 
> For this vault, stop letting this drift.
> 
> Use:
> 
> ```yaml
> matter_id: FCFCU_FORECLOSURE
> matter: Financial Center First Credit Union Foreclosure
> ```
> 
> Every queryable note in this vault should carry that unless it is clearly just admin/support material.
> 
> # Step 6: what folders I would clean now
> 
> Only a few.
> 
> ## Keep as-is
> - `00_CASE_MASTER`
> - `01_PHASES`
> - `02_VIOLATIONS`
> - `03_EVENTS`
> 
> These are already doing real work. fileciteturn2file0
> 
> ## Clean / standardize next
> - `04_DOCUMENTS`
> - `05_DISPUTES`
> - `06_DAMAGES`
> - `07_ACTORS`
> - `99_VAULT`
> 
> Why? Because those are usually where ambiguity creeps in fastest.
> 
> ## Create if not already present
> Inside root `content/`:
> 
> ```text
> _templates/
> _views/
> ```
> 
> These are system folders for authoring and dashboards, not substantive case folders.
> 
> # Step 7: the exact view logic you should use during transition
> 
> Because your metadata is not fully normalized yet, use **hybrid queries** right now.
> 
> ## Events
> ```dataview
> TABLE event_date, summary, file.link
> FROM ""
> WHERE type = "event" OR contains(file.path, "03_EVENTS")
> SORT event_date ASC
> ```
> 
> ## Violations
> ```dataview
> TABLE violation_code, summary, priority, file.link
> FROM ""
> WHERE type = "violation" OR contains(file.path, "02_VIOLATIONS")
> SORT file.name ASC
> ```
> 
> ## Documents
> ```dataview
> TABLE document_date, exhibit_id, summary, file.link
> FROM ""
> WHERE type = "document" OR contains(file.path, "04_DOCUMENTS")
> SORT document_date ASC
> ```
> 
> That lets your views work now while you backfill frontmatter.
> 
> # Step 8: the cleanup order
> 
> Do this in this order and don’t improvise:
> 
> ## Pass 1 — inventory
> Export a manifest of all markdown notes with:
> - file path
> - current frontmatter
> - likely folder-based type
> - parse status
> 
> ## Pass 2 — backfill minimum fields
> Backfill:
> - `type`
> - `matter_id`
> - `status`
> - `summary`
> - `created`
> - `updated`
> 
> ## Pass 3 — add type-specific fields
> Backfill:
> - `event_date`
> - `violation_code`
> - `document_date`
> - `agency`
> - `amount`
> - `actor_type`
> 
> ## Pass 4 — folder cleanup
> Only move files once metadata is good enough to identify what they are.
> 
> ## Pass 5 — tighten views
> Once metadata coverage is good, remove folder fallbacks from Dataview.
> 
> # Step 9: practical defaults for missing values
> 
> Use these defaults during the bulk pass:
> 
> ```yaml
> status: draft
> matter_id: FCFCU_FORECLOSURE
> matter: Financial Center First Credit Union Foreclosure
> summary: ""
> tags: []
> aliases: []
> created: 2026-03-09
> updated: 2026-03-09
> ```
> 
> Then replace blanks later where needed.
> 
> # Step 10: what I’d do next, specifically
> 
> Your next concrete move is not “clean folders” manually.
> 
> It is this:
> 
> ## Build a frontmatter manifest with these columns
> ```csv
> file_path,file_name,top_folder,current_type,new_type,document_id,matter_id,status,summary,created,updated,action,notes
> ```
> 
> And derive `top_folder` from:
> - `01_PHASES`
> - `02_VIOLATIONS`
> - `03_EVENTS`
> - etc.
> 
> Then set:
> - `new_type` from folder default
> - `matter_id` = `FCFCU_FORECLOSURE`
> - `action` = `update_frontmatter`
> 
> That gives you controlled bulk cleanup instead of folder roulette.
> 
> # My recommendation in one sentence
> 
> **Do not reorganize the vault first. Normalize frontmatter first, then let the metadata tell you what actually belongs where.**
> 
> If you want, next I’ll give you the exact **canonical frontmatter schema YAML** plus a **folder-to-type mapping CSV** for this FCFCU vault so you can start the manifest pass immediately.

### User
> mam the vault is the evidence vault, not notes, anything that just like notes and stuff goes in the case master.

### Assistant
> Yes — that changes the model, and it’s cleaner.
> 
> I was treating the vault like a notes vault.  
> You’re saying it is an **evidence vault first**, and that means:
> 
> - **the root vault = case evidence system**
> - **Case Master = working notes / dashboards / summaries / control layer**
> - everything else should be treated primarily as **evidence records, event records, violations, documents, damages, actors**, not casual notes
> 
> That fits your tree a lot better anyway. `00_CASE_MASTER` already looks like the control/admin layer, with summaries, admin, references, and reports living there. fileciteturn2file0
> 
> ## So here is the corrected model
> 
> ### Vault purpose
> **Evidence vault**
> 
> ### Case Master purpose
> **Notes, dashboards, summaries, work product, control center**
> 
> ---
> 
> # Correct top-level meaning now
> 
> ## `00_CASE_MASTER`
> This is where the “note-like” stuff goes:
> - dashboards
> - master summaries
> - strategy notes
> - admin
> - references
> - reports
> - quick working docs
> - case command center
> 
> ## Everything else
> This is **substantive case content**, not general notes:
> 
> - `01_PHASES` = workstreams / litigation structure / operational scaffolding
> - `02_VIOLATIONS` = violation records / theories / claims
> - `03_EVENTS` = factual timeline records
> - `04_DOCUMENTS` = document and exhibit records
> - `05_DISPUTES` = dispute and regulator matter records
> - `06_DAMAGES` = damage/harm records
> - `07_ACTORS` = person/org/entity records
> - `99_VAULT` = utility/sandbox/system leftovers only
> 
> That is a much better frame.
> 
> ---
> 
> # What this means for frontmatter
> 
> Frontmatter should describe the **record**, not whether it is a “note.”
> 
> So stop thinking in terms of:
> - note
> - issue note
> - exhibit note
> - event note
> 
> And switch to:
> - event record
> - violation record
> - document record
> - dispute record
> - damage record
> - actor record
> - case master note
> 
> That distinction matters.
> 
> ---
> 
> # New type model
> 
> Use these primary `type` values:
> 
> ```yaml
> type: case_master
> type: phase
> type: violation
> type: event
> type: document
> type: dispute
> type: damage
> type: actor
> ```
> 
> That’s it. Keep it tight.
> 
> ---
> 
> # Folder-to-type map
> 
> This should now be your default mapping:
> 
> ```text
> 00_CASE_MASTER -> case_master
> 01_PHASES      -> phase
> 02_VIOLATIONS  -> violation
> 03_EVENTS      -> event
> 04_DOCUMENTS   -> document
> 05_DISPUTES    -> dispute
> 06_DAMAGES     -> damage
> 07_ACTORS      -> actor
> ```
> 
> That becomes the default assumption for bulk frontmatter cleanup.
> 
> ---
> 
> # Correct schema approach
> 
> ## Common fields for all substantive records
> 
> ```yaml
> ---
> title:
> document_id:
> type:
> matter_id:
> matter:
> status:
> summary:
> created:
> updated:
> tags: []
> aliases: []
> source:
> source_file:
> ---
> ```
> 
> ## Type-specific fields
> 
> ### `type: event`
> ```yaml
> event_date:
> actors: []
> related_documents: []
> related_violations: []
> ```
> 
> ### `type: violation`
> ```yaml
> violation_code:
> violation_category:
> priority:
> related_events: []
> related_documents: []
> ```
> 
> ### `type: document`
> ```yaml
> document_date:
> document_kind:
> exhibit_id:
> hash:
> related_events: []
> related_violations: []
> ```
> 
> ### `type: dispute`
> ```yaml
> agency:
> sent_date:
> deadline_date:
> related_documents: []
> ```
> 
> ### `type: damage`
> ```yaml
> damage_category:
> amount:
> date_range:
> related_events: []
> related_documents: []
> ```
> 
> ### `type: actor`
> ```yaml
> actor_type:
> organization:
> role:
> related_events: []
> related_documents: []
> ```
> 
> ### `type: case_master`
> This is where the more note-like/control content lives:
> 
> ```yaml
> section:
> owner:
> review_status:
> related_records: []
> ```
> 
> ---
> 
> # Important correction to templates
> 
> The templates I gave before were too note-oriented for the whole vault.
> 
> That was wrong for your architecture.
> 
> You actually need **two classes of templates**:
> 
> ## 1. Case Master templates
> For:
> - dashboard
> - memo
> - strategy note
> - summary
> - action log
> 
> These live under:
> 
> ```text
> 00_CASE_MASTER
> ```
> 
> ## 2. Evidence record templates
> For:
> - event
> - violation
> - document
> - dispute
> - damage
> - actor
> 
> These live in the substantive folders.
> 
> ---
> 
> # What to do now
> 
> ## First
> Lock this rule:
> 
> > If it is analysis, planning, commentary, dashboarding, or “notes-like,” it goes in `00_CASE_MASTER`.
> 
> ## Second
> Treat the rest of the vault as **record objects**, not notes.
> 
> ## Third
> Update the home dashboard logic so it queries substantive folders as records and `00_CASE_MASTER` separately.
> 
> ---
> 
> # Better dashboard logic now
> 
> ## Case Master dashboard
> Lives in `00_CASE_MASTER`
> 
> It can query:
> - recent events
> - recent violations
> - missing metadata
> - recent documents
> - disputes due soon
> - damages records
> 
> ## Example event query
> ```dataview
> TABLE event_date, summary, file.link
> FROM "03_EVENTS"
> SORT event_date ASC
> ```
> 
> ## Example violation query
> ```dataview
> TABLE violation_code, priority, summary, file.link
> FROM "02_VIOLATIONS"
> SORT file.name ASC
> ```
> 
> ## Example documents query
> ```dataview
> TABLE document_date, exhibit_id, summary, file.link
> FROM "04_DOCUMENTS"
> SORT document_date ASC
> ```
> 
> That’s much cleaner than querying the whole vault blindly.
> 
> ---
> 
> # Folder cleanup rule
> 
> Now the cleanup question gets simpler:
> 
> ## Ask of each file:
> Is this:
> - a **record**
> - or **case master work product**
> 
> If it is:
> - a summary
> - a memo
> - a draft
> - a dashboard
> - a working analysis
> - a planning document
> - a tracker
> 
> Then it belongs in:
> 
> ```text
> 00_CASE_MASTER
> ```
> 
> If it is:
> - a timeline fact
> - a violation entry
> - a document record
> - a dispute item
> - a damages record
> - an actor/entity record
> 
> Then it belongs in the substantive folder.
> 
> That is the actual dividing line.
> 
> ---
> 
> # The next cleanup sequence is now
> 
> 1. classify files as either `case_master` or substantive record
> 2. assign `type` from folder default
> 3. normalize frontmatter
> 4. move only the files that are clearly in the wrong class
> 5. tighten views
> 
> ---
> 
> # Clean restatement of the system
> 
> ## `00_CASE_MASTER`
> Brain / control room
> 
> ## rest of vault
> Evidence / record system
> 
> That’s the right architecture.
> 
> If you want, next I’ll give you the **revised template pack** split correctly into:
> - `case_master` templates
> - evidence record templates

### Assistant
> Good — this CSV is exactly what we needed. You’ve basically **successfully extracted the vault’s metadata surface**. Now the goal is **not to keep all 108 columns**. That’s where systems explode.
> 
> Right now your manifest has **108 possible front-matter fields**. That’s way too many for stable views. Most of those should become either:
> 
> - deprecated
> - mapped to a canonical field
> - ignored
> 
> So the task now is **schema normalization**, not folder moving.
> 
> ---
> 
> # Step 1 — Identify the core schema
> 
> For your **evidence vault**, you only need about **14 universal fields**.
> 
> These power dashboards, manifests, exports, and search.
> 
> ### Canonical core fields
> 
> ```
> document_id
> type
> matter_id
> title
> summary
> status
> created
> updated
> event_date
> document_date
> actor
> exhibit_id
> violation_id
> source_file
> ```
> 
> Everything else becomes **secondary metadata**.
> 
> ---
> 
> # Step 2 — Map existing columns to canonical fields
> 
> From your CSV I can already see duplicates and variants like:
> 
> ```
> uuid
> uid
> id
> document_id
> ```
> 
> Those should all normalize to:
> 
> ```
> document_id
> ```
> 
> Another example:
> 
> ```
> actor
> actors
> related_people
> ```
> 
> Normalize to:
> 
> ```
> actors
> ```
> 
> Example mapping:
> 
> | Current column | Canonical |
> |---|---|
> uuid | document_id
> uid | document_id
> id | document_id
> actors | actors
> actor | actors
> violation_code | violation_id
> violation_category | violation_category
> document_kind | document_type
> document_date | document_date
> event_date | event_date
> created | created
> updated | updated
> summary | summary
> 
> ---
> 
> # Step 3 — Drop system noise
> 
> These should **not live in frontmatter** unless you have a specific reason:
> 
> Examples I saw:
> 
> ```
> binder
> Purpose
> Use
> toc
> trigger
> version
> ```
> 
> Those belong either in:
> 
> - Case master notes
> - body text
> - YAML under a nested field
> 
> Example:
> 
> ```
> meta:
>   binder: ADA
>   purpose: ADA packet
> ```
> 
> But not top-level.
> 
> ---
> 
> # Step 4 — Reduce the schema
> 
> After normalization, your vault frontmatter should look like this:
> 
> ### Example event record
> 
> ```yaml
> ---
> document_id: EVT-2025-12-09-WRIT
> type: event
> matter_id: FCFCU_FORECLOSURE
> title: Sheriff executes writ of assistance
> event_date: 2025-12-09
> actors:
>   - Marion County Sheriff
> summary: Sheriff removed occupants under writ of assistance
> status: confirmed
> created: 2026-03-09
> updated: 2026-03-09
> ---
> ```
> 
> ---
> 
> ### Example document record
> 
> ```yaml
> ---
> document_id: DOC-FCFCU-ORDER-001
> type: document
> matter_id: FCFCU_FORECLOSURE
> title: Court Order Denying Motion to Vacate
> document_date: 2026-01-09
> exhibit_id: K
> source_file: order_motion_vacate.pdf
> summary: Court denies motion citing sufficient service
> status: filed
> created: 2026-03-09
> updated: 2026-03-09
> ---
> ```
> 
> ---
> 
> ### Example violation record
> 
> ```yaml
> ---
> document_id: VIO-FCFCU-SERVICE-001
> type: violation
> matter_id: FCFCU_FORECLOSURE
> title: Improper service of foreclosure complaint
> violation_id: SERVICE_DEFECT
> violation_category: Due Process
> summary: No notice posted or mailed despite sheriff return
> status: active
> created: 2026-03-09
> updated: 2026-03-09
> ---
> ```
> 
> ---
> 
> # Step 5 — Update the manifest automatically
> 
> Instead of editing notes manually, the workflow should be:
> 
> ```
> Vault
>  ↓
> Extract metadata → CSV
>  ↓
> Normalize fields in CSV
>  ↓
> Dry run
>  ↓
> Write corrected frontmatter back to notes
> ```
> 
> That’s exactly the pipeline you described earlier.
> 
> ---
> 
> # Step 6 — Why your CSV is gold
> 
> Your CSV already has the hardest part done:
> 
> ```
> file_path
> file_name
> 108 potential metadata fields
> ```
> 
> That means we can automatically generate:
> 
> - field usage frequency
> - missing field report
> - schema mapping
> 
> ---
> 
> # Step 7 — Next script I would run
> 
> From that CSV we calculate:
> 
> ### field frequency
> 
> Example output:
> 
> ```
> summary → 312 notes
> event_date → 58 notes
> violation_id → 41 notes
> binder → 3 notes
> toc → 1 note
> ```
> 
> Then we decide:
> 
> ```
> keep
> merge
> delete
> ```
> 
> ---
> 
> # Step 8 — Example schema decision table
> 
> | field | action |
> |---|---|
> document_id | keep
> uid | merge → document_id
> uuid | merge → document_id
> actor | merge → actors
> actors | keep
> binder | move → meta.binder
> toc | drop
> trigger | drop
> version | drop
> 
> ---
> 
> # Step 9 — Once schema is stable
> 
> Then your Dataview queries become **very simple**:
> 
> ### events
> 
> ```
> FROM "03_EVENTS"
> WHERE type = "event"
> ```
> 
> ### violations
> 
> ```
> FROM "02_VIOLATIONS"
> WHERE type = "violation"
> ```
> 
> ### documents
> 
> ```
> FROM "04_DOCUMENTS"
> WHERE type = "document"
> ```
> 
> ---
> 
> # My honest recommendation right now
> 
> Do **not move folders yet**.
> 
> You’re already **90% correct structurally**.
> 
> The real work now is:
> 
> ```
> Frontmatter normalization
> ```
> 
> Because that controls:
> 
> - dashboards
> - exports
> - search
> - timeline
> - evidence indexing
> 
> ---
> 
> # If you want, I can also do something extremely helpful next
> 
> Using the CSV you uploaded, I can generate:
> 
> 1️⃣ **field frequency report**  
> 2️⃣ **canonical schema proposal**  
> 3️⃣ **automatic field mapping table**  
> 4️⃣ **cleanup script for the vault**
> 
> That will reduce your **108 fields → about 18 stable ones** without losing information.
> 
> And it will make your vault behave like **a real case database instead of a pile of markdown files**.

### User
> ok do that and tell me what to give the ide to get this done so i can move on to the next thing.

### Assistant
> Done. I made the three files you need:
> 
> [frontmatter_field_frequency.csv](sandbox:/mnt/data/frontmatter_field_frequency.csv)  
> [frontmatter_field_mapping_template.csv](sandbox:/mnt/data/frontmatter_field_mapping_template.csv)  
> [frontmatter_canonical_schema.csv](sandbox:/mnt/data/frontmatter_canonical_schema.csv)
> 
> ## What they are
> 
> **frontmatter_field_frequency.csv**  
> Shows which fields are actually used, how often, and sample values. This tells you what is real vs junk.
> 
> **frontmatter_field_mapping_template.csv**  
> A practical mapping table from current fields to canonical fields.
> 
> **frontmatter_canonical_schema.csv**  
> The reduced schema to target going forward.
> 
> ---
> 
> ## What I found fast
> 
> You have **1028 rows** and **108 columns** in the manifest.  
> That is too many frontmatter fields to keep sane.
> 
> The big fields actually in use are roughly:
> 
> - `uid`
> - `title`
> - `date`
> - `uuid`
> - `review`
> - `type`
> - `status`
> - `actor`
> - `tags`
> - `lane`
> - `description`
> - `kind`
> - `reviewed`
> 
> And the fields you actually want long-term are closer to:
> 
> - `document_id`
> - `type`
> - `matter_id`
> - `title`
> - `summary`
> - `status`
> - `created`
> - `updated`
> - `event_date`
> - `document_date`
> - `actors`
> - `source_file`
> - `exhibit_id`
> - `violation_id`
> - `priority`
> - `amount`
> - `currency`
> 
> That’s the real reduction.
> 
> ---
> 
> ## Important call
> 
> Your current metadata is mixing:
> 
> - identity
> - note workflow
> - binder/packet support
> - evidence properties
> - dashboard junk
> - one-off imports
> 
> So the right move is **not** “fix every field.”  
> The right move is:
> 
> 1. **keep** core fields  
> 2. **merge** duplicates  
> 3. **demote** weird fields to auxiliary  
> 4. **ignore** noise
> 
> ---
> 
> ## What to give the IDE
> 
> Give it this exact job:
> 
> ---
> 
> ### IDE task
> 
> Use `frontmatter_manifest.csv` plus these three support CSVs:
> 
> - `frontmatter_field_frequency.csv`
> - `frontmatter_field_mapping_template.csv`
> - `frontmatter_canonical_schema.csv`
> 
> Build a Python cleanup workflow for the FCFCU evidence vault.
> 
> ### Goal
> Normalize frontmatter across the vault so Dataview views work reliably, without moving folders yet.
> 
> ### Required outputs
> Create these scripts:
> 
> 1. `analyze_frontmatter.py`
> 2. `normalize_frontmatter_manifest.py`
> 3. `apply_frontmatter_updates.py`
> 
> ### Script responsibilities
> 
> **1. analyze_frontmatter.py**
> - load `frontmatter_manifest.csv`
> - report field usage frequency
> - report duplicate/overlapping identity fields
> - report missing canonical fields by row
> - infer likely `type` from top-level folder:
>   - `00_CASE_MASTER -> case_master`
>   - `01_PHASES -> phase`
>   - `02_VIOLATIONS -> violation`
>   - `03_EVENTS -> event`
>   - `04_DOCUMENTS -> document`
>   - `05_DISPUTES -> dispute`
>   - `06_DAMAGES -> damage`
>   - `07_ACTORS -> actor`
> 
> **2. normalize_frontmatter_manifest.py**
> - read `frontmatter_manifest.csv`
> - create a new CSV: `frontmatter_manifest_normalized.csv`
> - map fields using `frontmatter_field_mapping_template.csv`
> - produce canonical columns:
>   - `document_id`
>   - `type`
>   - `matter_id`
>   - `title`
>   - `summary`
>   - `status`
>   - `created`
>   - `updated`
>   - `record_date`
>   - `event_date`
>   - `document_date`
>   - `deadline_date`
>   - `actors`
>   - `source_file`
>   - `exhibit_id`
>   - `violation_id`
>   - `document_kind`
>   - `priority`
>   - `amount`
>   - `currency`
>   - `role`
>   - `binder`
>   - `lane`
>   - `legacy`
> - normalize values:
>   - `uid|uuid|id -> document_id`
>   - `description -> summary` when summary missing
>   - `actor -> actors`
>   - `date created -> created`
>   - `date modified -> updated`
>   - `doc_type -> document_kind`
>   - `due_date -> deadline_date`
> - normalize `status` to one of:
>   - `draft`
>   - `active`
>   - `filed`
>   - `confirmed`
>   - `resolved`
>   - `archived`
> - set `matter_id = FCFCU_FORECLOSURE` if blank
> - preserve noncanonical source columns in `legacy_fields_json`
> 
> **3. apply_frontmatter_updates.py**
> - read `frontmatter_manifest_normalized.csv`
> - dry-run first
> - update markdown files in place
> - write canonical frontmatter only
> - optionally preserve unknown legacy metadata under:
>   - `legacy_meta: {}`
> - do not move files
> - do not rewrite body text
> - create backups before writing
> - produce:
>   - `frontmatter_apply_report.csv`
> 
> ### Rules
> - vault is an **evidence vault first**
> - `00_CASE_MASTER` is for notes, dashboards, summaries, working docs
> - everything else is substantive record content
> - do not reorganize folders yet
> - prioritize frontmatter consistency over folder cleanup
> - output ISO dates where possible
> - prefer deterministic mappings over guesses
> - anything uncertain should be flagged in the normalized CSV, not silently rewritten
> 
> ### Deliverables
> - Python scripts
> - a dry-run report
> - a normalized manifest CSV
> - clear instructions for running export → normalize → dry run → apply
> 
> ---
> 
> ## What you do next
> 
> 1. hand the IDE that block  
> 2. have it generate the scripts  
> 3. run **normalize only** first  
> 4. inspect the normalized CSV  
> 5. run dry-run apply  
> 6. only then write to files
> 
> That gets you out of architecture limbo and into execution.
> 
> After that, the next thing is easy: tighten the Dataview views against the canonical fields.

### User
> code session expired i cant download the files

### Assistant
> Rebuilt them.
> 
> [frontmatter_field_frequency.csv](sandbox:/mnt/data/frontmatter_field_frequency.csv)  
> [frontmatter_field_mapping_template.csv](sandbox:/mnt/data/frontmatter_field_mapping_template.csv)  
> [frontmatter_canonical_schema.csv](sandbox:/mnt/data/frontmatter_canonical_schema.csv)
> 
> Use those plus your `frontmatter_manifest.csv` and hand the IDE the job block I gave you. That’s the shortest path out of this loop.

### User
> can you give me a todo list in csv

### Assistant
> I made it for you.
> 
> Download:  
> [obsidian_frontmatter_cleanup_todo.csv](sandbox:/mnt/data/obsidian_frontmatter_cleanup_todo.csv)
> 
> This is a **clean step-by-step execution list** so you stop context-switching and just move forward.
> 
> Columns are simple:
> 
> - **order** – execution order  
> - **task** – short name  
> - **description** – what to actually do  
> - **inputs** – files/tools needed  
> - **output** – what success produces
> 
> You can drop it into:
> 
> - **Obsidian table**
> - **Notion**
> - **Google Sheets**
> - **Dataview**
> - **your Qi system**
> 
> If you want, next I can also generate a **Dataview dashboard page** that shows:
> 
> - TODO
> - In Progress
> - Done
> 
> so your **case master becomes the command center** for this cleanup.
