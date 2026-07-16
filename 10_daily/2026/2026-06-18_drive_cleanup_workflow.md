---
layout: page
title: "Drive Cleanup Workflow"
slug: "drive_cleanup_workflow"
created_at: "2026-06-18 10:36:01"
updated_at: "2026-07-16T06:49:33-04:00"
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
date: 2026-06-18
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a341023-c454-83ea-a8b7-8bd827f5914e"
canonical_ref: ""
---

# Drive Cleanup Workflow

## Overview
- **Date**: 2026-06-18 10:36:01
- **Conversation ID**: `6a341023-c454-83ea-a8b7-8bd827f5914e`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> switching hears for a second i really really need help from the ai to organize my drive once and for all, but to do it in stages with pauses and human in the middle so i can approve as we go, becaue it is just a mess, and the file names are atroshish. i can use codex but i rather use codex for the documetnation site and use the ide for the organizing.

### Assistant
> Yes. This is exactly the kind of thing that needs **AI-assisted staging**, not “let the robot loose in Drive and pray.” We build a conveyor belt: inventory → classify → propose → approve → execute → verify.

### Assistant
> Yes. **Do not use Codex for this.** Codex should stay on the docs/site/dev thread. Drive cleanup needs a slower, approval-gated “ops agent” workflow in the IDE.
> 
> Your blueprint already gives us the anchor: **Google Drive / QiNexus is the storage backbone**, with canonical buckets like `00_inbox`, `01_workbench`, `06_finance`, `07_legal`, `10_data`, `12_archive`, and `13_system`. That means we are not inventing a new filing religion mid-chaos. We are enforcing the one you already picked. fileciteturn0file0
> 
> ## The correct model
> 
> **AI does not organize the Drive directly.**
> 
> AI creates:
> 
> 1. an inventory  
> 2. a classification proposal  
> 3. a rename proposal  
> 4. a move proposal  
> 5. a human approval sheet  
> 6. then a small batch execution  
> 7. then verification  
> 
> No deletes. No mass rename. No YOLO. We are not giving Skynet write access to your evidence folder. Absolutely not.
> 
> ---
> 
> # Drive Cleanup System
> 
> ## Stage 0 — Lock the Rules
> 
> Create a control folder:
> 
> `50_QiNexus/My Drive/13_system/drive_cleanup/2026-06_drive_reorg/`
> 
> Inside it:
> 
> ```text
> 00_rules/
> 01_inventory/
> 02_ai_proposals/
> 03_human_review/
> 04_approved_batches/
> 05_execution_logs/
> 06_error_logs/
> 07_final_indexes/
> ```
> 
> This folder becomes the audit trail.
> 
> ---
> 
> ## Stage 1 — Inventory Only
> 
> The IDE agent should first scan Drive and produce:
> 
> ```text
> drive_inventory_raw.csv
> drive_inventory_summary.md
> duplicate_candidates.csv
> bad_filename_candidates.csv
> orphaned_files.csv
> oversized_files.csv
> shared_files_audit.csv
> folder_tree_snapshot.md
> ```
> 
> Each row should include:
> 
> ```text
> file_id
> current_name
> mime_type
> current_path
> parent_folder_id
> created_time
> modified_time
> owner
> size
> shared_status
> web_view_link
> extension
> detected_date
> detected_person
> detected_domain
> suggested_bucket
> confidence
> notes
> ```
> 
> The **file ID matters more than the path** because Drive paths can lie when folders move.
> 
> ---
> 
> ## Stage 2 — Classification Proposal
> 
> AI sorts files into your QiNexus buckets:
> 
> ```text
> 00_inbox
> 01_workbench
> 02_timeline
> 03_life
> 04_people
> 05_business
> 06_finance
> 07_legal
> 08_tech
> 09_assets
> 10_data
> 11_reference
> 12_archive
> 13_system
> ```
> 
> Output:
> 
> ```text
> classification_proposal.csv
> classification_summary.md
> needs_human_decision.csv
> ```
> 
> Every row gets a status:
> 
> ```text
> AUTO_SAFE
> REVIEW_REQUIRED
> DO_NOT_TOUCH
> ARCHIVE_CANDIDATE
> DUPLICATE_CANDIDATE
> LEGAL_SENSITIVE
> FINANCE_SENSITIVE
> CARE_SENSITIVE
> ```
> 
> Important rule:
> 
> **Legal, finance, medical/care, identity, court, immigration, tax, and signed documents are never auto-moved without approval.**
> 
> ---
> 
> ## Stage 3 — Rename Proposal
> 
> For atrocious filenames, use a stable pattern:
> 
> ```text
> YYYY-MM-DD_entity_topic_doc-type_status.ext
> ```
> 
> Examples:
> 
> ```text
> 2026-06-17_mom_care_hospital-discharge-summary_source.pdf
> 2026-06-14_firefly_transactions_export_raw.csv
> 2025-09-05_zaitullah_asylum_i589_final-for-signature.pdf
> 2026-06-12_hertz_lyft-rental_billing-dispute_notes.md
> ```
> 
> For unknown dates:
> 
> ```text
> undated_entity_topic_doc-type.ext
> ```
> 
> For messy screenshots:
> 
> ```text
> 2026-06-17_mom_care_text-message-screenshot_001.png
> ```
> 
> For duplicates:
> 
> ```text
> DO NOT rename yet.
> ```
> 
> Duplicates should be grouped first.
> 
> ---
> 
> ## Stage 4 — Human Review Sheet
> 
> This is the key.
> 
> The IDE should create:
> 
> ```text
> human_review_batch_001.csv
> ```
> 
> Columns:
> 
> ```text
> file_id
> current_name
> current_path
> proposed_name
> proposed_path
> reason
> confidence
> risk_level
> approve_move
> approve_rename
> human_note
> final_decision
> ```
> 
> You approve by editing:
> 
> ```text
> approve_move = YES/NO
> approve_rename = YES/NO
> final_decision = APPROVE / SKIP / HOLD / DELETE_LATER
> ```
> 
> Not sexy. But it works.
> 
> ---
> 
> ## Stage 5 — Execute Small Batches
> 
> Batch size:
> 
> ```text
> 25 files max
> ```
> 
> Why? Because if something gets weird, you only have a small mess, not a digital house fire.
> 
> Execution output:
> 
> ```text
> batch_001_execution_log.csv
> batch_001_before_snapshot.csv
> batch_001_after_snapshot.csv
> batch_001_errors.csv
> ```
> 
> Every move/rename must be reversible.
> 
> ---
> 
> ## Stage 6 — Verify
> 
> After each batch:
> 
> ```text
> Verify file IDs still exist.
> Verify new parent folder.
> Verify new name.
> Verify no file lost permissions accidentally.
> Verify log matches approved sheet.
> ```
> 
> Then pause.
> 
> You review.
> 
> Then next batch.
> 
> ---
> 
> # IDE Prompt To Paste
> 
> Use this:
> 
> ```text
> You are helping me build a safe, human-approved Google Drive organization system for my QiNexus Drive.
> 
> Do not move, rename, delete, archive, or modify any Google Drive file yet.
> 
> First, create a staged Drive cleanup workflow with inventory-only mode.
> 
> Use this canonical QiNexus bucket model:
> 
> 00_inbox
> 01_workbench
> 02_timeline
> 03_life
> 04_people
> 05_business
> 06_finance
> 07_legal
> 08_tech
> 09_assets
> 10_data
> 11_reference
> 12_archive
> 13_system
> 
> Create a local project/workflow for Drive cleanup that produces CSV and Markdown audit files before any changes happen.
> 
> Required control folder structure:
> 
> 50_QiNexus/My Drive/13_system/drive_cleanup/2026-06_drive_reorg/
>   00_rules/
>   01_inventory/
>   02_ai_proposals/
>   03_human_review/
>   04_approved_batches/
>   05_execution_logs/
>   06_error_logs/
>   07_final_indexes/
> 
> Stage 1 goal:
> Build an inventory-only scanner for Google Drive.
> 
> The scanner should export:
> 
> drive_inventory_raw.csv
> drive_inventory_summary.md
> duplicate_candidates.csv
> bad_filename_candidates.csv
> orphaned_files.csv
> oversized_files.csv
> shared_files_audit.csv
> folder_tree_snapshot.md
> 
> Each inventory row should include:
> 
> file_id
> current_name
> mime_type
> current_path
> parent_folder_id
> created_time
> modified_time
> owner
> size
> shared_status
> web_view_link
> extension
> detected_date
> detected_person
> detected_domain
> suggested_bucket
> confidence
> notes
> 
> Rules:
> - Use Google Drive file IDs as the stable source of truth.
> - Do not rely only on paths.
> - Do not modify Drive during inventory.
> - Do not delete anything.
> - Do not rename anything.
> - Do not move anything.
> - Mark legal, finance, care, medical, identity, tax, court, immigration, signed, or evidence-like files as sensitive.
> - Sensitive files must always be REVIEW_REQUIRED.
> - Produce a clear README explaining how to run inventory-only mode.
> - Produce a dry-run architecture before writing code.
> - Ask me for approval before implementing any function that modifies Drive.
> 
> After inventory works, prepare Stage 2 classification proposal only. Still no Drive modifications.
> ```
> 
> ---
> 
> # Better Prompt After Inventory Exists
> 
> Once the inventory CSV is created, use this:
> 
> ```text
> Using the existing drive_inventory_raw.csv, create a classification proposal only.
> 
> Do not modify Drive.
> 
> For each file, propose:
> 
> suggested_bucket
> suggested_subfolder
> proposed_name
> proposed_path
> classification_reason
> confidence
> risk_level
> human_review_required
> sensitivity_flags
> 
> Use these statuses:
> 
> AUTO_SAFE
> REVIEW_REQUIRED
> DO_NOT_TOUCH
> ARCHIVE_CANDIDATE
> DUPLICATE_CANDIDATE
> LEGAL_SENSITIVE
> FINANCE_SENSITIVE
> CARE_SENSITIVE
> 
> Output:
> 
> classification_proposal.csv
> classification_summary.md
> needs_human_decision.csv
> 
> Rules:
> - Legal, finance, identity, medical, care, court, tax, immigration, signed, or evidence files must be REVIEW_REQUIRED.
> - Unknown files go to REVIEW_REQUIRED, not AUTO_SAFE.
> - Screenshots should be grouped by likely topic/date.
> - CSV exports should usually go under 10_data unless they clearly belong to finance/legal/care.
> - Reusable images, media, templates, and branding go under 09_assets.
> - Active work goes under 01_workbench.
> - Historical inactive material goes under 12_archive.
> - System rules, indexes, schemas, and manifests go under 13_system.
> ```
> 
> ---
> 
> # The Real Strategy
> 
> ## Use AI for judgment, not authority
> 
> AI can say:
> 
> > “This looks like finance.”
> 
> It should not decide:
> 
> > “I moved your tax file into archive because vibes.”
> 
> No. Jail.
> 
> ## Start with ugly wins
> 
> First cleanup targets:
> 
> 1. obvious duplicate exports  
> 2. screenshots  
> 3. random PDFs in root  
> 4. CSV/data dumps  
> 5. old downloads  
> 6. unnamed scans  
> 7. app-generated garbage  
> 
> Do **not** start with legal, mom care, taxes, immigration, or identity records. Those are high-risk. We touch those after the system proves itself.
> 
> ---
> 
> # My Recommended First Pass
> 
> Start with only these folders/categories:
> 
> ```text
> Screenshots
> Downloads
> CSV exports
> Random images
> Unsorted PDFs
> Old app exports
> Duplicate obvious copies
> ```
> 
> Avoid for now:
> 
> ```text
> Legal
> Finance
> Medical
> Mom care
> Immigration
> Signed forms
> Court evidence
> Tax records
> Identity documents
> ```
> 
> That is the difference between a cleanup and a self-inflicted discovery nightmare.
> 
> ---
> 
> # The Naming Rule
> 
> Use this:
> 
> ```text
> YYYY-MM-DD_entity_topic_doc-type_status.ext
> ```
> 
> Where:
> 
> ```text
> entity = mom, cody, qiserver, hertz, lyft, zaitullah, qiaccess, qinexus
> topic = care, billing-dispute, hospital, transactions, blueprint, rental
> doc-type = receipt, screenshot, export, statement, letter, form, notes
> status = raw, final, signed, submitted, draft, source, reviewed
> ```
> 
> Examples:
> 
> ```text
> 2026-06-17_mom_care_medication-list_source.pdf
> 2026-06-14_firefly_transactions_export_raw.csv
> 2026-06-12_hertz_lyft-rental_dispute-screenshot_001.png
> 2026-06-16_qiaccess_start_blueprint_final.md
> ```
> 
> ---
> 
> # Decision
> 
> Use the IDE to build:
> 
> ## `qidrivemaid`
> 
> Working name. Slightly sassy. Useful.
> 
> Purpose:
> 
> ```text
> Inventory, classify, propose, review, and safely organize Google Drive / QiNexus with human approval gates.
> ```
> 
> Not a one-time cleanup script. A reusable Drive governance tool.
> 
> Final architecture:
> 
> ```text
> qidrivemaid/
>   README.md
>   config/
>     buckets.yml
>     naming_rules.yml
>     sensitive_patterns.yml
>   scripts/
>     01_inventory_drive.py
>     02_classify_inventory.py
>     03_generate_review_batches.py
>     04_execute_approved_batch.py
>     05_verify_batch.py
>   output/
>     inventory/
>     proposals/
>     review/
>     approved/
>     logs/
> ```
> 
> And the first command should only ever be:
> 
> ```text
> inventory-only
> ```
> 
> That’s the move. We organize the chaos without letting the AI become the chaos.

### User
> ok girl you want to give me a python script to add these folders and files for this.

### Assistant
> Yep. I’d scaffold **the tool** and **the Drive audit/control folders** separately. The script below creates the structure, starter config files, README, and safe stub scripts — no Drive modifications.

### Assistant
> Absolutely. Save this as:
> 
> ```text
> bootstrap_qidrivemaid.py
> ```
> 
> Then run it from the IDE terminal:
> 
> ```bash
> python bootstrap_qidrivemaid.py
> ```
> 
> It creates the **QiDriveMaid tool scaffold** plus the **Drive cleanup control folders**. It does **not** move, rename, delete, or touch Drive files beyond creating empty folders/files. This follows the QiNexus storage model from your blueprint. fileciteturn0file0
> 
> ```python
> from pathlib import Path
> from textwrap import dedent
> import argparse
> 
> 
> DEFAULT_PROJECT_ROOT = Path.cwd() / "qidrivemaid"
> 
> DEFAULT_CONTROL_ROOT = Path(
>     r"C:\QiLabs\50_QiNexus\My Drive\13_system\drive_cleanup\2026-06_drive_reorg"
> )
> 
> 
> QI_BUCKETS = [
>     "00_inbox",
>     "01_workbench",
>     "02_timeline",
>     "03_life",
>     "04_people",
>     "05_business",
>     "06_finance",
>     "07_legal",
>     "08_tech",
>     "09_assets",
>     "10_data",
>     "11_reference",
>     "12_archive",
>     "13_system",
> ]
> 
> 
> CONTROL_FOLDERS = [
>     "00_rules",
>     "01_inventory",
>     "02_ai_proposals",
>     "03_human_review",
>     "04_approved_batches",
>     "05_execution_logs",
>     "06_error_logs",
>     "07_final_indexes",
> ]
> 
> 
> PROJECT_FOLDERS = [
>     "config",
>     "scripts",
>     "output/inventory",
>     "output/proposals",
>     "output/review",
>     "output/approved",
>     "output/logs",
>     "output/errors",
>     "docs",
> ]
> 
> 
> def write_file(path: Path, content: str, overwrite: bool = False) -> None:
>     path.parent.mkdir(parents=True, exist_ok=True)
> 
>     if path.exists() and not overwrite:
>         print(f"SKIP existing file: {path}")
>         return
> 
>     path.write_text(dedent(content).strip() + "\n", encoding="utf-8")
>     print(f"WROTE: {path}")
> 
> 
> def touch_keep_files(root: Path) -> None:
>     for folder in root.rglob("*"):
>         if folder.is_dir():
>             keep = folder / ".gitkeep"
>             if not keep.exists():
>                 keep.write_text("", encoding="utf-8")
> 
> 
> def create_project_scaffold(project_root: Path, overwrite: bool = False) -> None:
>     print(f"\nCreating QiDriveMaid project scaffold at:\n{project_root}\n")
> 
>     for folder in PROJECT_FOLDERS:
>         path = project_root / folder
>         path.mkdir(parents=True, exist_ok=True)
>         print(f"DIR: {path}")
> 
>     write_file(
>         project_root / "README.md",
>         """
>         # QiDriveMaid
> 
>         QiDriveMaid is a safe, human-approved Google Drive organization helper for QiNexus.
> 
>         It follows this workflow:
> 
>         1. Inventory
>         2. Classify
>         3. Propose
>         4. Human review
>         5. Approved batch execution
>         6. Verification
>         7. Final index
> 
>         ## Safety Rules
> 
>         - Do not delete files.
>         - Do not rename files without approval.
>         - Do not move files without approval.
>         - Use Google Drive file IDs as the stable source of truth.
>         - Legal, finance, medical, care, tax, court, immigration, identity, and signed documents require human review.
>         - Unknown files go to REVIEW_REQUIRED.
>         - Batch execution should be limited to 25 files at a time.
> 
>         ## First Command
> 
>         The first real command should only be inventory-only mode.
> 
>         ```bash
>         python scripts/01_inventory_drive.py
>         ```
> 
>         ## QiNexus Buckets
> 
>         - 00_inbox
>         - 01_workbench
>         - 02_timeline
>         - 03_life
>         - 04_people
>         - 05_business
>         - 06_finance
>         - 07_legal
>         - 08_tech
>         - 09_assets
>         - 10_data
>         - 11_reference
>         - 12_archive
>         - 13_system
>         """,
>         overwrite,
>     )
> 
>     write_file(
>         project_root / ".gitignore",
>         """
>         __pycache__/
>         *.pyc
>         .env
>         .venv/
>         venv/
>         credentials.json
>         token.json
>         *.log
> 
>         output/inventory/*.csv
>         output/proposals/*.csv
>         output/review/*.csv
>         output/approved/*.csv
>         output/logs/*.csv
>         output/errors/*.csv
> 
>         !output/**/.gitkeep
>         """,
>         overwrite,
>     )
> 
>     write_file(
>         project_root / "requirements.txt",
>         """
>         google-api-python-client
>         google-auth
>         google-auth-oauthlib
>         google-auth-httplib2
>         pandas
>         pyyaml
>         tqdm
>         python-dateutil
>         """,
>         overwrite,
>     )
> 
>     write_file(
>         project_root / "config" / "buckets.yml",
>         """
>         buckets:
>           00_inbox:
>             description: "Temporary landing zone. Nothing lives here permanently."
>           01_workbench:
>             description: "Active work, projects, tasks, builds, drafts, and current documents."
>           02_timeline:
>             description: "Journals, logs, event trails, daily notes, weekly notes, chronology."
>           03_life:
>             description: "Routines, home needs, planning, wellness structures, personal operations."
>           04_people:
>             description: "Family, support network, caregiving coordination, relationship/context notes."
>           05_business:
>             description: "Brand, revenue, client, and business materials."
>           06_finance:
>             description: "Budgets, bills, reports, reconciliations, account notes, and planning."
>             sensitive: true
>           07_legal:
>             description: "Matters, filings, court records, evidence, timelines, and legal research."
>             sensitive: true
>           08_tech:
>             description: "Servers, apps, code notes, scripts, architecture, deployments."
>           09_assets:
>             description: "Reusable images, videos, audio, templates, branding, design, and media."
>           10_data:
>             description: "CSVs, sheets, exports, datasets, logs, structured source material."
>           11_reference:
>             description: "Articles, laws, examples, guides, research, citations, external docs."
>           12_archive:
>             description: "Inactive, historical, deprecated, completed, or frozen material."
>           13_system:
>             description: "Rules, manifests, indexes, schemas, automation records, and structure docs."
>         """,
>         overwrite,
>     )
> 
>     write_file(
>         project_root / "config" / "naming_rules.yml",
>         """
>         naming_pattern: "YYYY-MM-DD_entity_topic_doc-type_status.ext"
> 
>         examples:
>           - "2026-06-17_mom_care_hospital-discharge-summary_source.pdf"
>           - "2026-06-14_firefly_transactions_export_raw.csv"
>           - "2026-06-12_hertz_lyft-rental_billing-dispute_notes.md"
>           - "undated_cody_identity_document_source.pdf"
> 
>         statuses:
>           - raw
>           - source
>           - draft
>           - reviewed
>           - final
>           - signed
>           - submitted
>           - archived
> 
>         rules:
>           - "Use lowercase."
>           - "Use hyphens inside phrases."
>           - "Use underscores between major fields."
>           - "Do not rename duplicates until duplicate grouping is complete."
>           - "Use undated_ when the document date is unknown."
>         """,
>         overwrite,
>     )
> 
>     write_file(
>         project_root / "config" / "sensitive_patterns.yml",
>         """
>         sensitive_keywords:
>           legal:
>             - court
>             - lawsuit
>             - evidence
>             - affidavit
>             - attorney
>             - filing
>             - motion
>             - order
>             - notice
>             - police
>             - eviction
>             - contract
>             - agreement
>           finance:
>             - tax
>             - irs
>             - bank
>             - statement
>             - invoice
>             - receipt
>             - payment
>             - payroll
>             - budget
>             - transaction
>             - firefly
>             - quickbooks
>           medical_care:
>             - hospital
>             - discharge
>             - medication
>             - morphine
>             - nurse
>             - caregiver
>             - oxygen
>             - diagnosis
>             - care
>             - mychart
>           identity:
>             - passport
>             - license
>             - ssn
>             - birth
>             - immigration
>             - i-94
>             - ead
>             - visa
>             - asylum
>             - siv
>           signed:
>             - signed
>             - signature
>             - notarized
>             - executed
> 
>         default_sensitive_status: "REVIEW_REQUIRED"
>         """,
>         overwrite,
>     )
> 
>     write_file(
>         project_root / "scripts" / "01_inventory_drive.py",
>         """
>         \"\"\"
>         Stage 1: Inventory Google Drive.
> 
>         This script is intentionally a safe placeholder.
> 
>         It should eventually:
>         - authenticate with Google Drive
>         - list files and folders
>         - export drive_inventory_raw.csv
>         - export duplicate_candidates.csv
>         - export bad_filename_candidates.csv
>         - export orphaned_files.csv
>         - export oversized_files.csv
>         - export shared_files_audit.csv
>         - export folder_tree_snapshot.md
> 
>         It must not move, rename, delete, archive, or modify Drive files.
>         \"\"\"
> 
>         from pathlib import Path
>         import pandas as pd
> 
> 
>         OUTPUT_DIR = Path(__file__).resolve().parents[1] / "output" / "inventory"
>         OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
> 
> 
>         COLUMNS = [
>             "file_id",
>             "current_name",
>             "mime_type",
>             "current_path",
>             "parent_folder_id",
>             "created_time",
>             "modified_time",
>             "owner",
>             "size",
>             "shared_status",
>             "web_view_link",
>             "extension",
>             "detected_date",
>             "detected_person",
>             "detected_domain",
>             "suggested_bucket",
>             "confidence",
>             "notes",
>         ]
> 
> 
>         def main():
>             print("Inventory-only mode placeholder.")
>             print("No Drive files will be modified.")
> 
>             sample_path = OUTPUT_DIR / "drive_inventory_raw.csv"
> 
>             if not sample_path.exists():
>                 pd.DataFrame(columns=COLUMNS).to_csv(sample_path, index=False)
>                 print(f"Created empty inventory template: {sample_path}")
>             else:
>                 print(f"Inventory template already exists: {sample_path}")
> 
> 
>         if __name__ == "__main__":
>             main()
>         """,
>         overwrite,
>     )
> 
>     write_file(
>         project_root / "scripts" / "02_classify_inventory.py",
>         """
>         \"\"\"
>         Stage 2: Classify inventory.
> 
>         Reads:
>         - output/inventory/drive_inventory_raw.csv
> 
>         Writes:
>         - output/proposals/classification_proposal.csv
>         - output/proposals/classification_summary.md
>         - output/proposals/needs_human_decision.csv
> 
>         This script must not modify Google Drive.
>         \"\"\"
> 
>         from pathlib import Path
>         import pandas as pd
> 
> 
>         ROOT = Path(__file__).resolve().parents[1]
>         INVENTORY = ROOT / "output" / "inventory" / "drive_inventory_raw.csv"
>         OUT_DIR = ROOT / "output" / "proposals"
>         OUT_DIR.mkdir(parents=True, exist_ok=True)
> 
> 
>         PROPOSAL_COLUMNS = [
>             "file_id",
>             "current_name",
>             "current_path",
>             "suggested_bucket",
>             "suggested_subfolder",
>             "proposed_name",
>             "proposed_path",
>             "classification_reason",
>             "confidence",
>             "risk_level",
>             "human_review_required",
>             "sensitivity_flags",
>             "status",
>         ]
> 
> 
>         def main():
>             if not INVENTORY.exists():
>                 raise FileNotFoundError(f"Missing inventory file: {INVENTORY}")
> 
>             df = pd.read_csv(INVENTORY)
> 
>             proposal = pd.DataFrame(columns=PROPOSAL_COLUMNS)
> 
>             proposal_path = OUT_DIR / "classification_proposal.csv"
>             review_path = OUT_DIR / "needs_human_decision.csv"
>             summary_path = OUT_DIR / "classification_summary.md"
> 
>             proposal.to_csv(proposal_path, index=False)
>             proposal.to_csv(review_path, index=False)
> 
>             summary_path.write_text(
>                 "# Classification Summary\\n\\n"
>                 "Classification placeholder created. No Drive files were modified.\\n",
>                 encoding="utf-8",
>             )
> 
>             print(f"Wrote: {proposal_path}")
>             print(f"Wrote: {review_path}")
>             print(f"Wrote: {summary_path}")
> 
> 
>         if __name__ == "__main__":
>             main()
>         """,
>         overwrite,
>     )
> 
>     write_file(
>         project_root / "scripts" / "03_generate_review_batches.py",
>         """
>         \"\"\"
>         Stage 3: Generate human review batches.
> 
>         Reads:
>         - output/proposals/classification_proposal.csv
> 
>         Writes:
>         - output/review/human_review_batch_001.csv
> 
>         This script must not modify Google Drive.
>         \"\"\"
> 
>         from pathlib import Path
>         import pandas as pd
> 
> 
>         ROOT = Path(__file__).resolve().parents[1]
>         PROPOSAL = ROOT / "output" / "proposals" / "classification_proposal.csv"
>         OUT_DIR = ROOT / "output" / "review"
>         OUT_DIR.mkdir(parents=True, exist_ok=True)
> 
> 
>         REVIEW_COLUMNS = [
>             "file_id",
>             "current_name",
>             "current_path",
>             "proposed_name",
>             "proposed_path",
>             "reason",
>             "confidence",
>             "risk_level",
>             "approve_move",
>             "approve_rename",
>             "human_note",
>             "final_decision",
>         ]
> 
> 
>         def main():
>             if not PROPOSAL.exists():
>                 raise FileNotFoundError(f"Missing classification proposal: {PROPOSAL}")
> 
>             df = pd.read_csv(PROPOSAL)
> 
>             review = pd.DataFrame(columns=REVIEW_COLUMNS)
> 
>             for col in REVIEW_COLUMNS:
>                 if col not in review.columns:
>                     review[col] = ""
> 
>             out_path = OUT_DIR / "human_review_batch_001.csv"
>             review.to_csv(out_path, index=False)
> 
>             print(f"Wrote human review batch: {out_path}")
>             print("Edit approve_move, approve_rename, and final_decision before execution.")
> 
> 
>         if __name__ == "__main__":
>             main()
>         """,
>         overwrite,
>     )
> 
>     write_file(
>         project_root / "scripts" / "04_execute_approved_batch.py",
>         """
>         \"\"\"
>         Stage 4: Execute approved batch.
> 
>         DANGER ZONE.
> 
>         This is intentionally locked by default.
> 
>         Future behavior:
>         - read an approved human review CSV
>         - move/rename only rows explicitly approved
>         - log before/after file IDs, names, paths, and parent IDs
>         - limit batch size to 25 files
>         - produce rollback notes
> 
>         This script should not be implemented until inventory, classification,
>         review, and verification are stable.
>         \"\"\"
> 
> 
>         def main():
>             raise SystemExit(
>                 "Execution is intentionally disabled. "
>                 "Implement only after human approval workflow is proven."
>             )
> 
> 
>         if __name__ == "__main__":
>             main()
>         """,
>         overwrite,
>     )
> 
>     write_file(
>         project_root / "scripts" / "05_verify_batch.py",
>         """
>         \"\"\"
>         Stage 5: Verify approved batch execution.
> 
>         Future behavior:
>         - confirm file IDs still exist
>         - confirm new parent folder
>         - confirm new name
>         - confirm permissions did not unexpectedly change
>         - compare approved CSV to execution log
> 
>         This script must be read-only.
>         \"\"\"
> 
> 
>         def main():
>             print("Verification placeholder. No Drive files modified.")
> 
> 
>         if __name__ == "__main__":
>             main()
>         """,
>         overwrite,
>     )
> 
>     write_file(
>         project_root / "docs" / "workflow.md",
>         """
>         # QiDriveMaid Workflow
> 
>         ## Stage 1 — Inventory
> 
>         Create a complete Drive inventory.
> 
>         No changes allowed.
> 
>         ## Stage 2 — Classification
> 
>         Propose bucket, subfolder, name, risk, and status.
> 
>         No changes allowed.
> 
>         ## Stage 3 — Human Review
> 
>         Create review batches.
> 
>         Human must approve move and rename decisions.
> 
>         ## Stage 4 — Execute Approved Batch
> 
>         Only approved rows may be changed.
> 
>         Batch size: 25 files max.
> 
>         ## Stage 5 — Verify
> 
>         Confirm every changed file still exists and landed where expected.
> 
>         ## Forbidden Until Later
> 
>         - delete
>         - permanent archive
>         - duplicate removal
>         - legal/finance/care auto-processing
>         """,
>         overwrite,
>     )
> 
>     touch_keep_files(project_root / "output")
> 
> 
> def create_control_folders(control_root: Path, overwrite: bool = False) -> None:
>     print(f"\nCreating Drive cleanup control folders at:\n{control_root}\n")
> 
>     control_root.mkdir(parents=True, exist_ok=True)
> 
>     for folder in CONTROL_FOLDERS:
>         path = control_root / folder
>         path.mkdir(parents=True, exist_ok=True)
>         print(f"DIR: {path}")
> 
>     write_file(
>         control_root / "00_rules" / "README.md",
>         """
>         # Drive Cleanup Rules
> 
>         This folder controls the staged Google Drive / QiNexus cleanup.
> 
>         ## Hard Rules
> 
>         - Inventory first.
>         - Classify second.
>         - Human review third.
>         - Approved batch execution fourth.
>         - Verify after every batch.
>         - No deletes during early cleanup.
>         - No auto-moving sensitive files.
>         - No mass rename without review.
>         - Legal, finance, medical/care, identity, court, immigration, tax, and signed documents require human approval.
> 
>         ## Batch Limit
> 
>         25 files max per execution batch.
>         """,
>         overwrite,
>     )
> 
>     write_file(
>         control_root / "00_rules" / "bucket_model.md",
>         "\n".join(["# QiNexus Bucket Model", ""] + [f"- `{bucket}`" for bucket in QI_BUCKETS]),
>         overwrite,
>     )
> 
>     write_file(
>         control_root / "03_human_review" / "human_review_columns.md",
>         """
>         # Human Review Sheet Columns
> 
>         Required columns:
> 
>         - file_id
>         - current_name
>         - current_path
>         - proposed_name
>         - proposed_path
>         - reason
>         - confidence
>         - risk_level
>         - approve_move
>         - approve_rename
>         - human_note
>         - final_decision
> 
>         Allowed final_decision values:
> 
>         - APPROVE
>         - SKIP
>         - HOLD
>         - DELETE_LATER
> 
>         Do not use DELETE_LATER for execution yet. It is only a marker.
>         """,
>         overwrite,
>     )
> 
> 
> def main():
>     parser = argparse.ArgumentParser(
>         description="Bootstrap QiDriveMaid folder and file scaffold."
>     )
> 
>     parser.add_argument(
>         "--project-root",
>         default=str(DEFAULT_PROJECT_ROOT),
>         help="Where to create the qidrivemaid project scaffold.",
>     )
> 
>     parser.add_argument(
>         "--control-root",
>         default=str(DEFAULT_CONTROL_ROOT),
>         help="Where to create the Drive cleanup control folders.",
>     )
> 
>     parser.add_argument(
>         "--skip-control-folders",
>         action="store_true",
>         help="Only create the qidrivemaid project scaffold, not Drive control folders.",
>     )
> 
>     parser.add_argument(
>         "--overwrite",
>         action="store_true",
>         help="Overwrite existing starter files.",
>     )
> 
>     args = parser.parse_args()
> 
>     project_root = Path(args.project_root)
>     control_root = Path(args.control_root)
> 
>     create_project_scaffold(project_root, overwrite=args.overwrite)
> 
>     if not args.skip_control_folders:
>         create_control_folders(control_root, overwrite=args.overwrite)
> 
>     print("\nDone.")
>     print("\nNext safe command:")
>     print(f'cd "{project_root}"')
>     print("pip install -r requirements.txt")
>     print("python scripts/01_inventory_drive.py")
> 
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ## Safer custom run command
> 
> If you want to explicitly place the tool somewhere instead of wherever your IDE terminal is sitting:
> 
> ```bash
> python bootstrap_qidrivemaid.py --project-root "C:\QiLabs\20_QiSystem\50_data\qidrivemaid"
> ```
> 
> Or if you only want the local tool scaffold and **not** the Drive control folders yet:
> 
> ```bash
> python bootstrap_qidrivemaid.py --skip-control-folders
> ```
> 
> My recommendation: run it once normally. Then commit the `qidrivemaid` scaffold, but **do not commit Drive inventory outputs** once real data starts generating.

### User
> heres the path fyi. incase that changes anything. C:\QiLabs\40_QiVault\My Drive\13_system\bootstrap_qidrivemaid.py

### Assistant
> Yep, that **does change the default path**.
> 
> Your active Drive mount is currently:
> 
> ```text
> C:\QiLabs\40_QiVault\My Drive
> ```
> 
> So the control folder should be:
> 
> ```text
> C:\QiLabs\40_QiVault\My Drive\13_system\drive_cleanup\2026-06_drive_reorg
> ```
> 
> Not the old path I used:
> 
> ```text
> C:\QiLabs\50_QiNexus\My Drive\...
> ```
> 
> Naming drift alert: your blueprint says Google Drive / QiNexus is the storage backbone, but your actual filesystem is using `40_QiVault`. Don’t fight that right now. Use the real path. Reconcile the name later. fileciteturn0file0
> 
> ## Best command to run
> 
> From wherever you are, run:
> 
> ```bash
> python "C:\QiLabs\40_QiVault\My Drive\13_system\bootstrap_qidrivemaid.py" --project-root "C:\QiLabs\20_QiSystem\50_data\qidrivemaid" --control-root "C:\QiLabs\40_QiVault\My Drive\13_system\drive_cleanup\2026-06_drive_reorg"
> ```
> 
> That puts:
> 
> ## Tool/code here
> 
> ```text
> C:\QiLabs\20_QiSystem\50_data\qidrivemaid
> ```
> 
> ## Drive audit/control files here
> 
> ```text
> C:\QiLabs\40_QiVault\My Drive\13_system\drive_cleanup\2026-06_drive_reorg
> ```
> 
> That split is cleaner:
> 
> | Thing | Best home | Why |
> |---|---|---|
> | `qidrivemaid` code | `20_QiSystem\50_data\qidrivemaid` | system/tooling layer |
> | Drive cleanup logs/rules/review CSVs | `40_QiVault\My Drive\13_system\drive_cleanup` | Drive governance layer |
> | Actual Drive files | stay wherever they are until approved | no chaos goblin behavior |
> 
> ## Optional: update the script default
> 
> Inside `bootstrap_qidrivemaid.py`, change this:
> 
> ```python
> DEFAULT_CONTROL_ROOT = Path(
>     r"C:\QiLabs\50_QiNexus\My Drive\13_system\drive_cleanup\2026-06_drive_reorg"
> )
> ```
> 
> To this:
> 
> ```python
> DEFAULT_CONTROL_ROOT = Path(
>     r"C:\QiLabs\40_QiVault\My Drive\13_system\drive_cleanup\2026-06_drive_reorg"
> )
> ```
> 
> Then future runs can just be:
> 
> ```bash
> python "C:\QiLabs\40_QiVault\My Drive\13_system\bootstrap_qidrivemaid.py" --project-root "C:\QiLabs\20_QiSystem\50_data\qidrivemaid"
> ```
> 
> My call: **use the explicit full command this first time** so nothing lands in the wrong folder.

### User
> give me the full updated script and make sure it is interactive im not doing run commands.

### Assistant
> Got it. I’m making this “click/run in IDE and answer prompts,” not argument-flag nonsense. Defaults will use your actual `40_QiVault\My Drive` path so it stops trying to birth folders in the wrong universe.

### Assistant
> Yes. Replace the contents of:
> 
> ```text
> C:\QiLabs\40_QiVault\My Drive\13_system\bootstrap_qidrivemaid.py
> ```
> 
> with this full script.
> 
> Then just **open it in the IDE and click Run Python File** or double-click it. It will ask you what to create. No flags, no command-line gymnastics.
> 
> It uses your real Drive path:
> 
> ```text
> C:\QiLabs\40_QiVault\My Drive
> ```
> 
> And keeps the QiNexus bucket model from your blueprint as the organizing doctrine. fileciteturn0file0
> 
> ```python
> from pathlib import Path
> from textwrap import dedent
> from datetime import datetime
> import sys
> 
> 
> # ============================================================
> # QiDriveMaid Interactive Bootstrapper
> # ============================================================
> #
> # Purpose:
> # Create a safe, staged Google Drive / QiVault / QiNexus cleanup scaffold.
> #
> # This script DOES NOT:
> # - move Drive files
> # - rename Drive files
> # - delete Drive files
> # - archive Drive files
> # - modify existing Drive content except creating folders/starter files
> #
> # It only creates:
> # - qidrivemaid project scaffold
> # - Drive cleanup control folder structure
> # - starter config files
> # - starter placeholder scripts
> # - audit/log folders
> #
> # ============================================================
> 
> 
> DEFAULT_STORAGE_ROOT = Path(r"C:\QiLabs\40_QiVault\My Drive")
> 
> DEFAULT_PROJECT_ROOT = Path(r"C:\QiLabs\20_QiSystem\50_data\qidrivemaid")
> 
> DEFAULT_CONTROL_ROOT = (
>     DEFAULT_STORAGE_ROOT
>     / "13_system"
>     / "drive_cleanup"
>     / "2026-06_drive_reorg"
> )
> 
> 
> QI_BUCKETS = [
>     "00_inbox",
>     "01_workbench",
>     "02_timeline",
>     "03_life",
>     "04_people",
>     "05_business",
>     "06_finance",
>     "07_legal",
>     "08_tech",
>     "09_assets",
>     "10_data",
>     "11_reference",
>     "12_archive",
>     "13_system",
> ]
> 
> 
> CONTROL_FOLDERS = [
>     "00_rules",
>     "01_inventory",
>     "02_ai_proposals",
>     "03_human_review",
>     "04_approved_batches",
>     "05_execution_logs",
>     "06_error_logs",
>     "07_final_indexes",
> ]
> 
> 
> PROJECT_FOLDERS = [
>     "config",
>     "scripts",
>     "output",
>     "output/inventory",
>     "output/proposals",
>     "output/review",
>     "output/approved",
>     "output/logs",
>     "output/errors",
>     "docs",
> ]
> 
> 
> INVENTORY_COLUMNS = [
>     "file_id",
>     "current_name",
>     "mime_type",
>     "current_path",
>     "parent_folder_id",
>     "created_time",
>     "modified_time",
>     "owner",
>     "size",
>     "shared_status",
>     "web_view_link",
>     "extension",
>     "detected_date",
>     "detected_person",
>     "detected_domain",
>     "suggested_bucket",
>     "confidence",
>     "notes",
> ]
> 
> 
> REVIEW_COLUMNS = [
>     "file_id",
>     "current_name",
>     "current_path",
>     "proposed_name",
>     "proposed_path",
>     "reason",
>     "confidence",
>     "risk_level",
>     "approve_move",
>     "approve_rename",
>     "human_note",
>     "final_decision",
> ]
> 
> 
> # ============================================================
> # Terminal / prompt helpers
> # ============================================================
> 
> 
> def line() -> None:
>     print("-" * 72)
> 
> 
> def title(text: str) -> None:
>     print()
>     line()
>     print(text)
>     line()
> 
> 
> def normalize_answer(value: str) -> str:
>     return value.strip().lower()
> 
> 
> def ask_yes_no(prompt: str, default: bool = True) -> bool:
>     default_text = "Y/n" if default else "y/N"
> 
>     while True:
>         answer = input(f"{prompt} [{default_text}]: ").strip()
> 
>         if not answer:
>             return default
> 
>         answer = normalize_answer(answer)
> 
>         if answer in {"y", "yes"}:
>             return True
> 
>         if answer in {"n", "no"}:
>             return False
> 
>         print("Please type y or n.")
> 
> 
> def ask_choice(prompt: str, choices: dict, default: str) -> str:
>     print(prompt)
> 
>     for key, label in choices.items():
>         marker = " ← default" if key == default else ""
>         print(f"  {key}) {label}{marker}")
> 
>     while True:
>         answer = input("Choose: ").strip()
> 
>         if not answer:
>             return default
> 
>         if answer in choices:
>             return answer
> 
>         print(f"Please choose one of: {', '.join(choices.keys())}")
> 
> 
> def ask_path(prompt: str, default: Path) -> Path:
>     print()
>     print(prompt)
>     print(f"Default:")
>     print(f"  {default}")
> 
>     answer = input("Press Enter to use default, or paste a different path: ").strip()
> 
>     if not answer:
>         return default
> 
>     # Remove accidental wrapping quotes.
>     answer = answer.strip('"').strip("'")
>     return Path(answer)
> 
> 
> def pause_before_exit() -> None:
>     print()
>     input("Done. Press Enter to close this window...")
> 
> 
> # ============================================================
> # File / folder helpers
> # ============================================================
> 
> 
> def make_dir(path: Path, dry_run: bool = False) -> None:
>     if dry_run:
>         print(f"DRY RUN DIR: {path}")
>         return
> 
>     path.mkdir(parents=True, exist_ok=True)
>     print(f"DIR: {path}")
> 
> 
> def write_file(path: Path, content: str, overwrite: bool = False, dry_run: bool = False) -> None:
>     clean_content = dedent(content).strip() + "\n"
> 
>     if dry_run:
>         action = "WOULD OVERWRITE" if path.exists() and overwrite else "WOULD WRITE"
>         if path.exists() and not overwrite:
>             action = "WOULD SKIP EXISTING"
>         print(f"{action}: {path}")
>         return
> 
>     path.parent.mkdir(parents=True, exist_ok=True)
> 
>     if path.exists() and not overwrite:
>         print(f"SKIP existing file: {path}")
>         return
> 
>     path.write_text(clean_content, encoding="utf-8")
>     print(f"WROTE: {path}")
> 
> 
> def write_csv_template(path: Path, columns: list[str], overwrite: bool = False, dry_run: bool = False) -> None:
>     header = ",".join(columns) + "\n"
> 
>     if dry_run:
>         action = "WOULD OVERWRITE CSV" if path.exists() and overwrite else "WOULD WRITE CSV"
>         if path.exists() and not overwrite:
>             action = "WOULD SKIP EXISTING CSV"
>         print(f"{action}: {path}")
>         return
> 
>     path.parent.mkdir(parents=True, exist_ok=True)
> 
>     if path.exists() and not overwrite:
>         print(f"SKIP existing CSV: {path}")
>         return
> 
>     path.write_text(header, encoding="utf-8")
>     print(f"WROTE CSV TEMPLATE: {path}")
> 
> 
> def touch_gitkeep_files(root: Path, dry_run: bool = False) -> None:
>     if not root.exists() and not dry_run:
>         return
> 
>     folders = []
> 
>     if dry_run:
>         # In dry run, we only print known output folders instead of walking.
>         return
> 
>     for folder in root.rglob("*"):
>         if folder.is_dir():
>             folders.append(folder)
> 
>     for folder in folders:
>         keep = folder / ".gitkeep"
> 
>         if not keep.exists():
>             keep.write_text("", encoding="utf-8")
> 
> 
> # ============================================================
> # Content generators
> # ============================================================
> 
> 
> def readme_content(project_root: Path, control_root: Path) -> str:
>     return f"""
>     # QiDriveMaid
> 
>     QiDriveMaid is a safe, human-approved Google Drive organization helper for QiVault / QiNexus.
> 
>     It exists to clean up Drive without letting automation cause a digital house fire.
> 
>     ## Current Paths
> 
>     Project/tool scaffold:
> 
>     `{project_root}`
> 
>     Drive cleanup control folder:
> 
>     `{control_root}`
> 
>     ## Workflow
> 
>     1. Inventory
>     2. Classification proposal
>     3. Rename/move proposal
>     4. Human review
>     5. Approved batch execution
>     6. Verification
>     7. Final index
> 
>     ## Safety Rules
> 
>     - Do not delete files.
>     - Do not rename files without approval.
>     - Do not move files without approval.
>     - Use Google Drive file IDs as the stable source of truth.
>     - Legal, finance, medical, care, tax, court, immigration, identity, and signed documents require human review.
>     - Unknown files go to REVIEW_REQUIRED.
>     - Batch execution should be limited to 25 files at a time.
> 
>     ## Current Stage
> 
>     Bootstrap only.
> 
>     The scripts created here are placeholders and safe templates.
> 
>     The execution script is intentionally locked.
>     """
> 
> 
> def gitignore_content() -> str:
>     return """
>     __pycache__/
>     *.pyc
>     .env
>     .venv/
>     venv/
>     credentials.json
>     token.json
>     *.log
> 
>     output/inventory/*.csv
>     output/proposals/*.csv
>     output/review/*.csv
>     output/approved/*.csv
>     output/logs/*.csv
>     output/errors/*.csv
> 
>     !output/**/.gitkeep
>     """
> 
> 
> def requirements_content() -> str:
>     return """
>     google-api-python-client
>     google-auth
>     google-auth-oauthlib
>     google-auth-httplib2
>     pandas
>     pyyaml
>     tqdm
>     python-dateutil
>     """
> 
> 
> def buckets_yml_content() -> str:
>     return """
>     buckets:
>       00_inbox:
>         description: "Temporary landing zone. Nothing lives here permanently."
>         sensitive: false
> 
>       01_workbench:
>         description: "Active work, projects, tasks, builds, drafts, and current documents."
>         sensitive: false
> 
>       02_timeline:
>         description: "Journals, logs, event trails, daily notes, weekly notes, chronology."
>         sensitive: false
> 
>       03_life:
>         description: "Routines, home needs, planning, wellness structures, personal operations."
>         sensitive: false
> 
>       04_people:
>         description: "Family, support network, caregiving coordination, relationship/context notes."
>         sensitive: true
> 
>       05_business:
>         description: "Brand, revenue, client, and business materials."
>         sensitive: false
> 
>       06_finance:
>         description: "Budgets, bills, reports, reconciliations, account notes, and planning."
>         sensitive: true
> 
>       07_legal:
>         description: "Matters, filings, court records, evidence, timelines, and legal research."
>         sensitive: true
> 
>       08_tech:
>         description: "Servers, apps, code notes, scripts, architecture, deployments."
>         sensitive: false
> 
>       09_assets:
>         description: "Reusable images, videos, audio, templates, branding, design, and media."
>         sensitive: false
> 
>       10_data:
>         description: "CSVs, sheets, exports, datasets, logs, structured source material."
>         sensitive: false
> 
>       11_reference:
>         description: "Articles, laws, examples, guides, research, citations, and external docs."
>         sensitive: false
> 
>       12_archive:
>         description: "Inactive, historical, deprecated, completed, or frozen material."
>         sensitive: false
> 
>       13_system:
>         description: "Rules, manifests, indexes, schemas, automation records, and structure docs."
>         sensitive: false
>     """
> 
> 
> def naming_rules_content() -> str:
>     return """
>     naming_pattern: "YYYY-MM-DD_entity_topic_doc-type_status.ext"
> 
>     examples:
>       - "2026-06-17_mom_care_hospital-discharge-summary_source.pdf"
>       - "2026-06-14_firefly_transactions_export_raw.csv"
>       - "2026-06-12_hertz_lyft-rental_billing-dispute_notes.md"
>       - "undated_cody_identity_document_source.pdf"
> 
>     statuses:
>       - raw
>       - source
>       - draft
>       - reviewed
>       - final
>       - signed
>       - submitted
>       - archived
> 
>     entity_examples:
>       - cody
>       - mom
>       - qiserver
>       - qiaccess
>       - qivault
>       - qinexus
>       - hertz
>       - lyft
>       - firefly
>       - zaitullah
> 
>     rules:
>       - "Use lowercase."
>       - "Use hyphens inside phrases."
>       - "Use underscores between major fields."
>       - "Do not rename duplicates until duplicate grouping is complete."
>       - "Use undated_ when the document date is unknown."
>       - "Never auto-rename legal, finance, medical/care, identity, signed, tax, court, or immigration files."
>     """
> 
> 
> def sensitive_patterns_content() -> str:
>     return """
>     sensitive_keywords:
>       legal:
>         - court
>         - lawsuit
>         - evidence
>         - affidavit
>         - attorney
>         - filing
>         - motion
>         - order
>         - notice
>         - police
>         - eviction
>         - contract
>         - agreement
>         - claim
>         - complaint
>         - dispute
>         - discovery
> 
>       finance:
>         - tax
>         - irs
>         - bank
>         - statement
>         - invoice
>         - receipt
>         - payment
>         - payroll
>         - budget
>         - transaction
>         - firefly
>         - quickbooks
>         - bill
>         - refund
>         - charge
>         - hertz
>         - lyft
> 
>       medical_care:
>         - hospital
>         - discharge
>         - medication
>         - morphine
>         - nurse
>         - caregiver
>         - oxygen
>         - diagnosis
>         - care
>         - mychart
>         - comfort
>         - keepers
>         - humana
>         - hospice
>         - appointment
> 
>       identity:
>         - passport
>         - license
>         - ssn
>         - social security
>         - birth
>         - immigration
>         - i-94
>         - ead
>         - visa
>         - asylum
>         - siv
>         - uscis
>         - nvc
>         - ds-260
> 
>       signed:
>         - signed
>         - signature
>         - notarized
>         - executed
> 
>     default_sensitive_status: "REVIEW_REQUIRED"
>     unknown_file_status: "REVIEW_REQUIRED"
>     """
> 
> 
> def status_model_content() -> str:
>     return """
>     statuses:
>       AUTO_SAFE:
>         meaning: "Low-risk file can be proposed for move/rename, but still should not be modified without batch approval."
> 
>       REVIEW_REQUIRED:
>         meaning: "Human must review before any change."
> 
>       DO_NOT_TOUCH:
>         meaning: "Do not move, rename, archive, or delete."
> 
>       ARCHIVE_CANDIDATE:
>         meaning: "Looks inactive or historical, but still requires approval."
> 
>       DUPLICATE_CANDIDATE:
>         meaning: "Possible duplicate. Do not delete. Group first."
> 
>       LEGAL_SENSITIVE:
>         meaning: "Legal/evidence/court/contract matter. Human approval required."
> 
>       FINANCE_SENSITIVE:
>         meaning: "Finance/tax/billing/accounting matter. Human approval required."
> 
>       CARE_SENSITIVE:
>         meaning: "Medical/care/family support matter. Human approval required."
>     """
> 
> 
> def inventory_script_content() -> str:
>     return '''
>     """
>     Stage 1: Inventory Google Drive.
> 
>     This is currently a SAFE placeholder.
> 
>     Future purpose:
>     - authenticate with Google Drive
>     - list files and folders
>     - export drive_inventory_raw.csv
>     - export duplicate_candidates.csv
>     - export bad_filename_candidates.csv
>     - export orphaned_files.csv
>     - export oversized_files.csv
>     - export shared_files_audit.csv
>     - export folder_tree_snapshot.md
> 
>     This script must not move, rename, delete, archive, or modify Drive files.
>     """
> 
>     from pathlib import Path
>     import csv
> 
> 
>     ROOT = Path(__file__).resolve().parents[1]
>     OUTPUT_DIR = ROOT / "output" / "inventory"
> 
>     INVENTORY_COLUMNS = [
>         "file_id",
>         "current_name",
>         "mime_type",
>         "current_path",
>         "parent_folder_id",
>         "created_time",
>         "modified_time",
>         "owner",
>         "size",
>         "shared_status",
>         "web_view_link",
>         "extension",
>         "detected_date",
>         "detected_person",
>         "detected_domain",
>         "suggested_bucket",
>         "confidence",
>         "notes",
>     ]
> 
> 
>     def write_empty_csv(path: Path, columns: list[str]) -> None:
>         path.parent.mkdir(parents=True, exist_ok=True)
> 
>         if path.exists():
>             print(f"Exists, leaving alone: {path}")
>             return
> 
>         with path.open("w", newline="", encoding="utf-8") as f:
>             writer = csv.writer(f)
>             writer.writerow(columns)
> 
>         print(f"Created template: {path}")
> 
> 
>     def main() -> None:
>         print("QiDriveMaid — inventory-only placeholder")
>         print("No Drive files will be modified.")
> 
>         OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
> 
>         write_empty_csv(OUTPUT_DIR / "drive_inventory_raw.csv", INVENTORY_COLUMNS)
>         write_empty_csv(OUTPUT_DIR / "duplicate_candidates.csv", INVENTORY_COLUMNS)
>         write_empty_csv(OUTPUT_DIR / "bad_filename_candidates.csv", INVENTORY_COLUMNS)
>         write_empty_csv(OUTPUT_DIR / "orphaned_files.csv", INVENTORY_COLUMNS)
>         write_empty_csv(OUTPUT_DIR / "oversized_files.csv", INVENTORY_COLUMNS)
>         write_empty_csv(OUTPUT_DIR / "shared_files_audit.csv", INVENTORY_COLUMNS)
> 
>         tree_snapshot = OUTPUT_DIR / "folder_tree_snapshot.md"
>         if not tree_snapshot.exists():
>             tree_snapshot.write_text(
>                 "# Folder Tree Snapshot\\n\\nInventory has not been connected yet.\\n",
>                 encoding="utf-8",
>             )
>             print(f"Created template: {tree_snapshot}")
> 
>         summary = OUTPUT_DIR / "drive_inventory_summary.md"
>         if not summary.exists():
>             summary.write_text(
>                 "# Drive Inventory Summary\\n\\nInventory has not been connected yet.\\n",
>                 encoding="utf-8",
>             )
>             print(f"Created template: {summary}")
> 
>         print("Inventory placeholder complete.")
> 
> 
>     if __name__ == "__main__":
>         main()
>     '''
> 
> 
> def classify_script_content() -> str:
>     return '''
>     """
>     Stage 2: Classify inventory.
> 
>     Reads:
>     - output/inventory/drive_inventory_raw.csv
> 
>     Writes:
>     - output/proposals/classification_proposal.csv
>     - output/proposals/classification_summary.md
>     - output/proposals/needs_human_decision.csv
> 
>     This script must not modify Google Drive.
>     """
> 
>     from pathlib import Path
>     import csv
> 
> 
>     ROOT = Path(__file__).resolve().parents[1]
>     INVENTORY = ROOT / "output" / "inventory" / "drive_inventory_raw.csv"
>     OUT_DIR = ROOT / "output" / "proposals"
> 
>     PROPOSAL_COLUMNS = [
>         "file_id",
>         "current_name",
>         "current_path",
>         "suggested_bucket",
>         "suggested_subfolder",
>         "proposed_name",
>         "proposed_path",
>         "classification_reason",
>         "confidence",
>         "risk_level",
>         "human_review_required",
>         "sensitivity_flags",
>         "status",
>     ]
> 
> 
>     def write_empty_csv(path: Path, columns: list[str]) -> None:
>         path.parent.mkdir(parents=True, exist_ok=True)
> 
>         with path.open("w", newline="", encoding="utf-8") as f:
>             writer = csv.writer(f)
>             writer.writerow(columns)
> 
>         print(f"Wrote: {path}")
> 
> 
>     def main() -> None:
>         print("QiDriveMaid — classification placeholder")
>         print("No Drive files will be modified.")
> 
>         if not INVENTORY.exists():
>             raise FileNotFoundError(f"Missing inventory file: {INVENTORY}")
> 
>         OUT_DIR.mkdir(parents=True, exist_ok=True)
> 
>         write_empty_csv(OUT_DIR / "classification_proposal.csv", PROPOSAL_COLUMNS)
>         write_empty_csv(OUT_DIR / "needs_human_decision.csv", PROPOSAL_COLUMNS)
> 
>         summary_path = OUT_DIR / "classification_summary.md"
>         summary_path.write_text(
>             "# Classification Summary\\n\\n"
>             "Classification placeholder created. No Drive files were modified.\\n",
>             encoding="utf-8",
>         )
>         print(f"Wrote: {summary_path}")
> 
> 
>     if __name__ == "__main__":
>         main()
>     '''
> 
> 
> def review_batches_script_content() -> str:
>     return '''
>     """
>     Stage 3: Generate human review batches.
> 
>     Reads:
>     - output/proposals/classification_proposal.csv
> 
>     Writes:
>     - output/review/human_review_batch_001.csv
> 
>     This script must not modify Google Drive.
>     """
> 
>     from pathlib import Path
>     import csv
> 
> 
>     ROOT = Path(__file__).resolve().parents[1]
>     PROPOSAL = ROOT / "output" / "proposals" / "classification_proposal.csv"
>     OUT_DIR = ROOT / "output" / "review"
> 
>     REVIEW_COLUMNS = [
>         "file_id",
>         "current_name",
>         "current_path",
>         "proposed_name",
>         "proposed_path",
>         "reason",
>         "confidence",
>         "risk_level",
>         "approve_move",
>         "approve_rename",
>         "human_note",
>         "final_decision",
>     ]
> 
> 
>     def main() -> None:
>         print("QiDriveMaid — human review batch placeholder")
>         print("No Drive files will be modified.")
> 
>         if not PROPOSAL.exists():
>             raise FileNotFoundError(f"Missing classification proposal: {PROPOSAL}")
> 
>         OUT_DIR.mkdir(parents=True, exist_ok=True)
> 
>         out_path = OUT_DIR / "human_review_batch_001.csv"
> 
>         with out_path.open("w", newline="", encoding="utf-8") as f:
>             writer = csv.writer(f)
>             writer.writerow(REVIEW_COLUMNS)
> 
>         print(f"Wrote human review batch: {out_path}")
>         print("Edit approve_move, approve_rename, and final_decision before execution.")
> 
> 
>     if __name__ == "__main__":
>         main()
>     '''
> 
> 
> def execute_script_content() -> str:
>     return '''
>     """
>     Stage 4: Execute approved batch.
> 
>     DANGER ZONE.
> 
>     This is intentionally locked by default.
> 
>     Future behavior:
>     - read an approved human review CSV
>     - move/rename only rows explicitly approved
>     - log before/after file IDs, names, paths, and parent IDs
>     - limit batch size to 25 files
>     - produce rollback notes
> 
>     This script should not be implemented until inventory, classification,
>     review, and verification are stable.
>     """
> 
> 
>     def main() -> None:
>         raise SystemExit(
>             "Execution is intentionally disabled. "
>             "Implement only after the human approval workflow is proven."
>         )
> 
> 
>     if __name__ == "__main__":
>         main()
>     '''
> 
> 
> def verify_script_content() -> str:
>     return '''
>     """
>     Stage 5: Verify approved batch execution.
> 
>     Future behavior:
>     - confirm file IDs still exist
>     - confirm new parent folder
>     - confirm new name
>     - confirm permissions did not unexpectedly change
>     - compare approved CSV to execution log
> 
>     This script must be read-only.
>     """
> 
> 
>     def main() -> None:
>         print("QiDriveMaid — verification placeholder")
>         print("No Drive files modified.")
> 
> 
>     if __name__ == "__main__":
>         main()
>     '''
> 
> 
> def workflow_doc_content() -> str:
>     return """
>     # QiDriveMaid Workflow
> 
>     ## Stage 1 — Inventory
> 
>     Create a complete Drive inventory.
> 
>     No changes allowed.
> 
>     ## Stage 2 — Classification
> 
>     Propose bucket, subfolder, name, risk, and status.
> 
>     No changes allowed.
> 
>     ## Stage 3 — Human Review
> 
>     Create review batches.
> 
>     Human must approve move and rename decisions.
> 
>     ## Stage 4 — Execute Approved Batch
> 
>     Only approved rows may be changed.
> 
>     Batch size: 25 files max.
> 
>     ## Stage 5 — Verify
> 
>     Confirm every changed file still exists and landed where expected.
> 
>     ## Forbidden Until Later
> 
>     - delete
>     - permanent archive
>     - duplicate removal
>     - legal auto-processing
>     - finance auto-processing
>     - care/medical auto-processing
>     - identity document auto-processing
>     """
> 
> 
> def launcher_bat_content(project_root: Path) -> str:
>     return f"""
>     @echo off
>     title QiDriveMaid Menu
>     cd /d "{project_root}"
>     echo QiDriveMaid placeholder menu
>     echo.
>     echo This project has been scaffolded.
>     echo The current scripts are safe placeholders.
>     echo.
>     echo 1. Inventory placeholder
>     echo 2. Classification placeholder
>     echo 3. Human review placeholder
>     echo.
>     set /p choice=Choose 1, 2, or 3:
>     if "%choice%"=="1" python scripts\\01_inventory_drive.py
>     if "%choice%"=="2" python scripts\\02_classify_inventory.py
>     if "%choice%"=="3" python scripts\\03_generate_review_batches.py
>     echo.
>     pause
>     """
> 
> 
> # ============================================================
> # Create project scaffold
> # ============================================================
> 
> 
> def create_project_scaffold(
>     project_root: Path,
>     control_root: Path,
>     overwrite: bool = False,
>     dry_run: bool = False,
> ) -> None:
>     title("Creating QiDriveMaid Project Scaffold")
> 
>     print(f"Project root:")
>     print(f"  {project_root}")
>     print()
> 
>     for folder in PROJECT_FOLDERS:
>         make_dir(project_root / folder, dry_run=dry_run)
> 
>     write_file(
>         project_root / "README.md",
>         readme_content(project_root, control_root),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         project_root / ".gitignore",
>         gitignore_content(),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         project_root / "requirements.txt",
>         requirements_content(),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         project_root / "config" / "buckets.yml",
>         buckets_yml_content(),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         project_root / "config" / "naming_rules.yml",
>         naming_rules_content(),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         project_root / "config" / "sensitive_patterns.yml",
>         sensitive_patterns_content(),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         project_root / "config" / "status_model.yml",
>         status_model_content(),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         project_root / "scripts" / "01_inventory_drive.py",
>         inventory_script_content(),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         project_root / "scripts" / "02_classify_inventory.py",
>         classify_script_content(),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         project_root / "scripts" / "03_generate_review_batches.py",
>         review_batches_script_content(),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         project_root / "scripts" / "04_execute_approved_batch.py",
>         execute_script_content(),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         project_root / "scripts" / "05_verify_batch.py",
>         verify_script_content(),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         project_root / "docs" / "workflow.md",
>         workflow_doc_content(),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         project_root / "START_QiDriveMaid_Menu.bat",
>         launcher_bat_content(project_root),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     if not dry_run:
>         touch_gitkeep_files(project_root / "output", dry_run=dry_run)
> 
> 
> # ============================================================
> # Create Drive control folders
> # ============================================================
> 
> 
> def create_control_folders(
>     control_root: Path,
>     overwrite: bool = False,
>     dry_run: bool = False,
> ) -> None:
>     title("Creating Drive Cleanup Control Folders")
> 
>     print(f"Control root:")
>     print(f"  {control_root}")
>     print()
> 
>     make_dir(control_root, dry_run=dry_run)
> 
>     for folder in CONTROL_FOLDERS:
>         make_dir(control_root / folder, dry_run=dry_run)
> 
>     write_file(
>         control_root / "00_rules" / "README.md",
>         """
>         # Drive Cleanup Rules
> 
>         This folder controls the staged Google Drive / QiVault / QiNexus cleanup.
> 
>         ## Hard Rules
> 
>         - Inventory first.
>         - Classify second.
>         - Human review third.
>         - Approved batch execution fourth.
>         - Verify after every batch.
>         - No deletes during early cleanup.
>         - No auto-moving sensitive files.
>         - No mass rename without review.
>         - Legal, finance, medical/care, identity, court, immigration, tax, and signed documents require human approval.
> 
>         ## Batch Limit
> 
>         25 files max per execution batch.
>         """,
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         control_root / "00_rules" / "bucket_model.md",
>         "\n".join(["# QiNexus Bucket Model", ""] + [f"- `{bucket}`" for bucket in QI_BUCKETS]),
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         control_root / "00_rules" / "naming_pattern.md",
>         """
>         # Naming Pattern
> 
>         Use:
> 
>         `YYYY-MM-DD_entity_topic_doc-type_status.ext`
> 
>         Examples:
> 
>         - `2026-06-17_mom_care_hospital-discharge-summary_source.pdf`
>         - `2026-06-14_firefly_transactions_export_raw.csv`
>         - `2026-06-12_hertz_lyft-rental_billing-dispute_notes.md`
>         - `undated_cody_identity_document_source.pdf`
> 
>         Rules:
> 
>         - lowercase
>         - hyphens inside phrases
>         - underscores between major fields
>         - never auto-rename sensitive files
>         - unknown dates use `undated_`
>         """,
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         control_root / "03_human_review" / "human_review_columns.md",
>         """
>         # Human Review Sheet Columns
> 
>         Required columns:
> 
>         - file_id
>         - current_name
>         - current_path
>         - proposed_name
>         - proposed_path
>         - reason
>         - confidence
>         - risk_level
>         - approve_move
>         - approve_rename
>         - human_note
>         - final_decision
> 
>         Allowed final_decision values:
> 
>         - APPROVE
>         - SKIP
>         - HOLD
>         - DELETE_LATER
> 
>         Do not use DELETE_LATER for execution yet. It is only a marker.
>         """,
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_csv_template(
>         control_root / "03_human_review" / "human_review_batch_template.csv",
>         REVIEW_COLUMNS,
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         control_root / "05_execution_logs" / "execution_log_readme.md",
>         """
>         # Execution Logs
> 
>         Every future approved batch must create:
> 
>         - before snapshot
>         - after snapshot
>         - execution log
>         - error log
>         - rollback notes
> 
>         No execution script should run unless a human-approved CSV exists.
>         """,
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     write_file(
>         control_root / "07_final_indexes" / "final_indexes_readme.md",
>         """
>         # Final Indexes
> 
>         This folder will eventually contain cleaned Drive indexes and final reports.
> 
>         Nothing here is canonical until batch verification is complete.
>         """,
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
> 
> # ============================================================
> # Main interactive flow
> # ============================================================
> 
> 
> def print_intro() -> None:
>     title("QiDriveMaid Interactive Bootstrapper")
> 
>     print("This will create the scaffold for your Drive cleanup system.")
>     print()
>     print("It will NOT move, rename, delete, archive, or modify existing Drive files.")
>     print("It only creates folders and starter files.")
>     print()
>     print("Default Drive root:")
>     print(f"  {DEFAULT_STORAGE_ROOT}")
>     print()
>     print("Default project/tool root:")
>     print(f"  {DEFAULT_PROJECT_ROOT}")
>     print()
>     print("Default Drive cleanup control root:")
>     print(f"  {DEFAULT_CONTROL_ROOT}")
> 
> 
> def print_plan(
>     mode: str,
>     project_root: Path,
>     control_root: Path,
>     overwrite: bool,
>     dry_run: bool,
> ) -> None:
>     title("Review Plan")
> 
>     print(f"Mode:")
>     print(f"  {mode}")
>     print()
>     print(f"Project root:")
>     print(f"  {project_root}")
>     print()
>     print(f"Control root:")
>     print(f"  {control_root}")
>     print()
>     print(f"Overwrite existing starter files:")
>     print(f"  {'YES' if overwrite else 'NO'}")
>     print()
>     print(f"Dry run only:")
>     print(f"  {'YES' if dry_run else 'NO'}")
>     print()
>     print("Safety:")
>     print("  No existing Drive files will be moved, renamed, deleted, or archived.")
> 
> 
> def interactive_main() -> None:
>     print_intro()
> 
>     mode = ask_choice(
>         "\nWhat do you want to create?",
>         {
>             "1": "Create BOTH project scaffold and Drive cleanup control folders — recommended",
>             "2": "Create project scaffold only",
>             "3": "Create Drive cleanup control folders only",
>             "4": "Preview only / dry run",
>             "5": "Exit",
>         },
>         default="1",
>     )
> 
>     if mode == "5":
>         print("Exiting. Nothing changed.")
>         return
> 
>     dry_run = mode == "4"
> 
>     if mode in {"1", "2", "4"}:
>         project_root = ask_path(
>             "Where should the QiDriveMaid tool/project scaffold go?",
>             DEFAULT_PROJECT_ROOT,
>         )
>     else:
>         project_root = DEFAULT_PROJECT_ROOT
> 
>     if mode in {"1", "3", "4"}:
>         control_root = ask_path(
>             "Where should the Drive cleanup control/audit folder go?",
>             DEFAULT_CONTROL_ROOT,
>         )
>     else:
>         control_root = DEFAULT_CONTROL_ROOT
> 
>     overwrite = ask_yes_no(
>         "Overwrite existing starter files if they already exist?",
>         default=False,
>     )
> 
>     print_plan(
>         mode=mode,
>         project_root=project_root,
>         control_root=control_root,
>         overwrite=overwrite,
>         dry_run=dry_run,
>     )
> 
>     proceed = ask_yes_no("Proceed?", default=True)
> 
>     if not proceed:
>         print("Cancelled. Nothing changed.")
>         return
> 
>     started = datetime.now()
> 
>     if mode in {"1", "2", "4"}:
>         create_project_scaffold(
>             project_root=project_root,
>             control_root=control_root,
>             overwrite=overwrite,
>             dry_run=dry_run,
>         )
> 
>     if mode in {"1", "3", "4"}:
>         create_control_folders(
>             control_root=control_root,
>             overwrite=overwrite,
>             dry_run=dry_run,
>         )
> 
>     finished = datetime.now()
> 
>     title("Complete")
> 
>     print(f"Started:  {started}")
>     print(f"Finished: {finished}")
>     print()
>     print("Created/checked:")
>     print(f"  Project: {project_root}")
>     print(f"  Control: {control_root}")
>     print()
>     print("Next useful thing:")
>     print("  Open the qidrivemaid folder in your IDE.")
>     print("  Use START_QiDriveMaid_Menu.bat if you want a clickable placeholder menu.")
>     print()
>     print("Reminder:")
>     print("  The real Drive inventory connector is not implemented yet.")
>     print("  This scaffold is the safe foundation, not the chaos goblin.")
> 
> 
> def main() -> None:
>     try:
>         interactive_main()
>     except KeyboardInterrupt:
>         print("\nCancelled by user.")
>     except Exception as exc:
>         print()
>         print("ERROR:")
>         print(exc)
>         print()
>         print("Nothing should have touched existing Drive files.")
>     finally:
>         # Keep the terminal open when double-clicked on Windows.
>         if sys.platform.startswith("win"):
>             pause_before_exit()
> 
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ## What to choose when it opens
> 
> Pick:
> 
> ```text
> 1) Create BOTH project scaffold and Drive cleanup control folders — recommended
> ```
> 
> Then press **Enter** for both default paths.
> 
> For overwrite:
> 
> ```text
> NO
> ```
> 
> Unless you already ran the old version and want these starter files refreshed.
> 
> The important correction is baked in now: **Drive control/audit lives under `40_QiVault\My Drive\13_system`, not the old `50_QiNexus` path.**

### User
> how do we build this into a smart file organizer local fs ai system that we can set rules fuzzy rules and it can adapt as we make approvals or correct it .

### Assistant
> This becomes a **local decision engine**, not just a cleanup script. The trick is separating “what it thinks” from “what it’s allowed to do,” then turning every approval/correction into training data.

### Assistant
> We build it as a **local filesystem AI organizer with a memory spine**.
> 
> Not “AI sorts my files.” That’s too vague and dangerous.
> 
> The real system is:
> 
> > **Scan files → extract signals → score rules → propose action → human approves/corrects → system learns → next proposal gets smarter.**
> 
> Think of it like a junior filing clerk who must show their work before touching anything.
> 
> ---
> 
> # The Core Architecture
> 
> ```text
> QiDriveMaid
> │
> ├── 01 Scanner
> │   Reads local filesystem / Drive-mounted folder
> │
> ├── 02 Metadata Extractor
> │   Gets name, path, extension, size, dates, text preview, OCR later
> │
> ├── 03 Rule Engine
> │   Applies exact + fuzzy folder rules
> │
> ├── 04 AI Classifier
> │   Uses embeddings / local LLM to infer meaning
> │
> ├── 05 Decision Engine
> │   Combines rules + AI + prior approvals
> │
> ├── 06 Human Review
> │   CSV / local web UI / approval queue
> │
> ├── 07 Learning Ledger
> │   Stores every approval/correction
> │
> ├── 08 Executor
> │   Moves/renames only approved files
> │
> └── 09 Verifier
>     Confirms file landed correctly
> ```
> 
> Your QiNexus bucket model is already the target taxonomy: `00_inbox`, `01_workbench`, `06_finance`, `07_legal`, `10_data`, `12_archive`, `13_system`, etc. That’s the spine. We do **not** let the AI invent new top-level buckets every five minutes like it drank a Red Bull. fileciteturn0file0
> 
> ---
> 
> # The Big Rule
> 
> ## AI can propose.
> 
> ## Rules can score.
> 
> ## Only approval can execute.
> 
> That keeps the system useful without turning it into a haunted Roomba for your Drive.
> 
> ---
> 
> # Data Model
> 
> Use SQLite locally.
> 
> Not Supabase yet. Not Postgres yet. Not a whole cathedral. SQLite is perfect for this stage.
> 
> ## Core tables
> 
> ```text
> files
> file_signals
> classification_runs
> proposals
> human_decisions
> rules
> rule_matches
> learned_examples
> execution_batches
> execution_logs
> ```
> 
> ---
> 
> ## `files`
> 
> Tracks every discovered file.
> 
> ```text
> id
> file_hash
> current_path
> current_name
> extension
> mime_type
> size_bytes
> created_at
> modified_at
> first_seen_at
> last_seen_at
> is_missing
> ```
> 
> For local filesystem, the file path is unstable. So we also store:
> 
> ```text
> file_hash
> size_bytes
> modified_at
> ```
> 
> That helps detect renamed/moved files.
> 
> ---
> 
> ## `file_signals`
> 
> Stores extracted meaning.
> 
> ```text
> file_id
> filename_tokens
> path_tokens
> detected_date
> detected_entity
> detected_domain
> text_preview
> ocr_text
> source_app
> language
> sensitivity_flags
> ```
> 
> Examples:
> 
> ```text
> detected_entity = mom
> detected_domain = care
> sensitivity_flags = medical_care, legal_sensitive
> ```
> 
> ---
> 
> ## `rules`
> 
> Stores your fuzzy rules.
> 
> ```text
> id
> rule_name
> rule_type
> pattern
> target_bucket
> target_subfolder
> weight
> risk_level
> enabled
> created_at
> updated_at
> ```
> 
> Rule types:
> 
> ```text
> filename_contains
> path_contains
> extension_is
> mime_type_is
> regex_match
> date_detected
> entity_detected
> semantic_similarity
> sensitive_keyword
> ```
> 
> ---
> 
> ## `proposals`
> 
> Every AI/rule recommendation goes here.
> 
> ```text
> id
> file_id
> proposed_bucket
> proposed_subfolder
> proposed_name
> proposed_path
> confidence
> risk_level
> reason
> status
> created_at
> ```
> 
> Statuses:
> 
> ```text
> PENDING_REVIEW
> APPROVED
> CORRECTED
> REJECTED
> EXECUTED
> FAILED
> ```
> 
> ---
> 
> ## `human_decisions`
> 
> This is the learning gold.
> 
> ```text
> id
> proposal_id
> file_id
> decision
> approved_bucket
> approved_subfolder
> approved_name
> human_note
> correction_reason
> created_at
> ```
> 
> Decision values:
> 
> ```text
> APPROVE
> CORRECT
> SKIP
> HOLD
> DO_NOT_TOUCH
> ```
> 
> Every correction becomes training data.
> 
> ---
> 
> ## `learned_examples`
> 
> The system stores examples like:
> 
> ```text
> filename: Screenshot_20260617_103944.png
> old_guess: 09_assets/screenshots
> human_corrected_to: 07_legal/mom_care/evidence/messages
> reason: text message screenshot related to care dispute
> ```
> 
> Next time it sees a similar screenshot, it gets smarter.
> 
> ---
> 
> # How the “Fuzzy Rules” Work
> 
> Rules should not be binary unless they are truly exact.
> 
> They should score.
> 
> Example:
> 
> ```yaml
> rule_name: mom_care_medical_docs
> rule_type: weighted_fuzzy
> target_bucket: 04_people
> target_subfolder: mom/care/medical
> risk_level: CARE_SENSITIVE
> auto_execute: false
> weight: 80
> 
> signals:
>   filename_contains:
>     - hospital
>     - discharge
>     - mychart
>     - oxygen
>     - medication
>     - morphine
> 
>   path_contains:
>     - mom
>     - care
>     - medical
> 
>   extension:
>     - pdf
>     - jpg
>     - png
> 
> required_review: true
> ```
> 
> Another:
> 
> ```yaml
> rule_name: csv_exports_to_data
> rule_type: weighted_fuzzy
> target_bucket: 10_data
> target_subfolder: exports/raw
> risk_level: LOW
> auto_execute: false
> weight: 60
> 
> signals:
>   extension:
>     - csv
>     - json
>     - xlsx
> 
>   filename_contains:
>     - export
>     - transactions
>     - inventory
>     - backup
> ```
> 
> But then finance sensitivity overrides it:
> 
> ```yaml
> rule_name: finance_sensitive_override
> rule_type: sensitive_override
> target_bucket: 06_finance
> risk_level: FINANCE_SENSITIVE
> required_review: true
> weight: 100
> 
> signals:
>   filename_contains:
>     - bank
>     - tax
>     - irs
>     - payment
>     - payroll
>     - transaction
>     - invoice
>     - hertz
>     - lyft
> ```
> 
> So a file like:
> 
> ```text
> 2026_06_14_transaction_export.csv
> ```
> 
> might first score as:
> 
> ```text
> 10_data/exports/raw = 60
> ```
> 
> but then finance override says:
> 
> ```text
> 06_finance/transactions/firefly = 100
> ```
> 
> Final proposal:
> 
> ```text
> 06_finance/transactions/firefly
> REVIEW_REQUIRED
> ```
> 
> That’s the behavior we want.
> 
> ---
> 
> # Decision Engine Logic
> 
> Each file gets scored by multiple systems.
> 
> ```text
> Final Confidence =
>   exact rules score
> + fuzzy filename score
> + path context score
> + extension score
> + semantic similarity score
> + learned example score
> - sensitivity penalty
> - ambiguity penalty
> ```
> 
> Example output:
> 
> ```text
> File:
> IMG_4021.png
> 
> Detected:
> screenshot, text message, mom, medication, hospital
> 
> Scores:
> 04_people/mom/care/messages: 84
> 07_legal/evidence/messages: 76
> 09_assets/screenshots: 30
> 
> Proposal:
> 04_people/mom/care/messages
> 
> Risk:
> CARE_SENSITIVE
> 
> Action:
> REVIEW_REQUIRED
> 
> Reason:
> Screenshot appears to involve mom care communication and medication/hospital context.
> ```
> 
> That is useful.
> 
> Not just:
> 
> > “Moved to screenshots.”
> 
> Because no. Screenshot is file format context, not life context. The AI has to learn that.
> 
> ---
> 
> # Learning Loop
> 
> This is the part that makes it adaptive.
> 
> ## When you approve
> 
> The system learns:
> 
> ```text
> This pattern was correct.
> Increase weight for matching signals.
> ```
> 
> ## When you correct
> 
> The system learns:
> 
> ```text
> This looked like X, but Cody said it belongs in Y.
> Store this as an example.
> Reduce confidence next time similar ambiguity appears.
> ```
> 
> ## When you mark DO_NOT_TOUCH
> 
> The system learns:
> 
> ```text
> This category requires lockdown.
> Never auto-propose aggressive actions here.
> ```
> 
> ---
> 
> # The Memory Model
> 
> Use two types of memory.
> 
> ## 1. Rule memory
> 
> Human-readable YAML.
> 
> Good for durable doctrine.
> 
> ```text
> config/rules/
>   00_global_safety.yml
>   01_bucket_rules.yml
>   02_sensitive_rules.yml
>   03_filename_rules.yml
>   04_entity_rules.yml
>   05_learned_rules.yml
> ```
> 
> ## 2. Example memory
> 
> SQLite rows.
> 
> Good for pattern matching.
> 
> ```text
> learned_examples
> ```
> 
> Example:
> 
> ```text
> “Screenshots with mom + medication + accusation language usually belong in care/legal evidence review, not assets.”
> ```
> 
> ---
> 
> # Local AI Layer
> 
> There are three levels.
> 
> ## Level 1 — No AI
> 
> Use rules only.
> 
> Good for:
> 
> ```text
> .csv → data review
> .pdf with tax → finance review
> passport/license/ssn → identity review
> ```
> 
> ## Level 2 — Embeddings
> 
> The system compares files to prior approved examples.
> 
> Example:
> 
> ```text
> This file is semantically similar to 23 files Cody approved into:
> 07_legal/mom_care/evidence/messages
> ```
> 
> That is the best first “smart” layer.
> 
> ## Level 3 — Local LLM
> 
> Use local LLM only to explain and propose:
> 
> ```text
> Given filename, folder path, extracted text, and prior examples, suggest bucket/subfolder/name.
> ```
> 
> Do **not** use LLM as the source of truth.
> 
> LLM gives reasoning. The decision engine decides confidence. Human approves.
> 
> ---
> 
> # Folder Structure
> 
> Inside the tool:
> 
> ```text
> qidrivemaid/
> │
> ├── config/
> │   ├── buckets.yml
> │   ├── naming_rules.yml
> │   ├── sensitive_patterns.yml
> │   ├── rules/
> │   │   ├── 00_global_safety.yml
> │   │   ├── 01_bucket_rules.yml
> │   │   ├── 02_sensitive_rules.yml
> │   │   ├── 03_filename_rules.yml
> │   │   ├── 04_entity_rules.yml
> │   │   └── 05_learned_rules.yml
> │
> ├── data/
> │   ├── qidrivemaid.sqlite
> │   └── embeddings/
> │
> ├── scripts/
> │   ├── 01_scan_local_fs.py
> │   ├── 02_extract_signals.py
> │   ├── 03_score_rules.py
> │   ├── 04_generate_proposals.py
> │   ├── 05_review_queue.py
> │   ├── 06_apply_human_decisions.py
> │   ├── 07_execute_approved_batch.py
> │   ├── 08_verify_batch.py
> │   └── 09_learn_from_decisions.py
> │
> ├── app/
> │   ├── local_review_ui.py
> │   └── templates/
> │
> ├── output/
> │   ├── inventory/
> │   ├── proposals/
> │   ├── review/
> │   ├── approved/
> │   ├── logs/
> │   └── reports/
> │
> └── README.md
> ```
> 
> ---
> 
> # The Review UI
> 
> Start ugly. CSV first.
> 
> Then make it nicer.
> 
> ## Phase 1 Review
> 
> CSV:
> 
> ```text
> human_review_batch_001.csv
> ```
> 
> You edit:
> 
> ```text
> approve_move
> approve_rename
> final_decision
> human_note
> ```
> 
> ## Phase 2 Review
> 
> Local web app:
> 
> ```text
> http://localhost:8501
> ```
> 
> Each card shows:
> 
> ```text
> current file
> current path
> preview
> proposed path
> proposed name
> reason
> confidence
> risk
> buttons:
>   Approve
>   Correct
>   Hold
>   Do Not Touch
> ```
> 
> For ADHD sanity, the UI should show **one file at a time** or **small batches of 10–25**.
> 
> No giant spreadsheet doom wall.
> 
> ---
> 
> # Approval Actions
> 
> Each proposal should have these buttons:
> 
> ```text
> Approve as proposed
> Correct folder
> Correct name
> Hold
> Mark sensitive
> Mark duplicate
> Do not touch
> ```
> 
> Each correction asks:
> 
> ```text
> Where should similar files go next time?
> ```
> 
> Options:
> 
> ```text
> Just this file
> Similar filenames
> Similar folder context
> Similar extracted text
> Always when these keywords appear
> ```
> 
> That’s how we turn corrections into fuzzy rules without making you write YAML manually every time.
> 
> ---
> 
> # Safety Modes
> 
> You need four modes.
> 
> ## 1. Observe Mode
> 
> ```text
> Scan only.
> No proposals.
> No changes.
> ```
> 
> ## 2. Propose Mode
> 
> ```text
> Generate classifications and rename/move suggestions.
> No changes.
> ```
> 
> ## 3. Review Mode
> 
> ```text
> Human approves/corrects.
> No changes yet.
> ```
> 
> ## 4. Execute Mode
> 
> ```text
> Apply only approved changes.
> Batch limited.
> Log everything.
> ```
> 
> Default must always be:
> 
> ```text
> Observe Mode
> ```
> 
> Because chaos goblin gets no default power.
> 
> ---
> 
> # Confidence Thresholds
> 
> Use hard thresholds.
> 
> ```text
> 0–49  = weak guess, review required
> 50–74 = decent guess, review required
> 75–89 = strong guess, review required
> 90–100 = strong safe guess, eligible for auto-safe proposal only
> ```
> 
> But sensitive files override everything:
> 
> ```text
> legal
> finance
> medical/care
> identity
> tax
> court
> immigration
> signed
> ```
> 
> Always:
> 
> ```text
> REVIEW_REQUIRED
> ```
> 
> Even at 100 confidence.
> 
> ---
> 
> # Auto-Execution Rules
> 
> Early version:
> 
> ```text
> auto_execute = false
> ```
> 
> Later version can allow very narrow actions:
> 
> ```text
> Move obvious .tmp files to 12_archive/system_temp_review
> Move duplicate empty folders to review list
> Move obvious app cache files to 12_archive/app_exports_review
> ```
> 
> But honestly? For your Drive, I’d keep auto-execution off for a while.
> 
> Your files are not just clutter. A lot of them are evidence, care records, finance disputes, legal history, business context, and system DNA. Too much risk.
> 
> ---
> 
> # The “Adaptive” Part
> 
> Here’s the actual adaptive loop:
> 
> ```text
> 1. System proposes:
>    File A → 09_assets/screenshots
> 
> 2. You correct:
>    File A → 07_legal/mom_care/evidence/messages
> 
> 3. System records:
>    - filename was screenshot
>    - OCR contained “police”, “neglect”, “medication”
>    - path was Downloads/Screenshots
>    - correction target was legal/care/evidence
>    - human note: "care dispute evidence"
> 
> 4. Next similar file:
>    System boosts legal/care/evidence score.
> 
> 5. After repeated approvals:
>    System creates suggested learned rule:
>    “Screenshots containing mom + police/neglect/medication should go to legal/care evidence review.”
> 
> 6. You approve the learned rule.
> 
> 7. Future proposals improve.
> ```
> 
> That is the sweet spot.
> 
> It learns, but it does not silently mutate doctrine.
> 
> ---
> 
> # Rule Promotion
> 
> The system should not automatically create permanent rules.
> 
> It should propose them.
> 
> Example:
> 
> ```text
> Suggested Learned Rule
> 
> Pattern:
> Screenshots containing:
> - mom
> - police
> - medication
> - neglect
> - hospital
> 
> Usually approved to:
> 07_legal/mom_care/evidence/messages
> 
> Seen:
> 14 times
> 
> Accuracy:
> 92%
> 
> Approve this as a fuzzy rule?
> YES / NO / EDIT
> ```
> 
> That’s clean.
> 
> ---
> 
> # Local Filesystem vs Google Drive API
> 
> You have two possible scan modes.
> 
> ## Local filesystem mode
> 
> Scans:
> 
> ```text
> C:\QiLabs\40_QiVault\My Drive
> ```
> 
> Pros:
> 
> ```text
> simple
> fast
> works with normal Python
> easy to test
> no OAuth first
> ```
> 
> Cons:
> 
> ```text
> does not know true Google Drive file IDs
> Google Docs/Sheets may appear weird
> shared file metadata may be limited
> ```
> 
> ## Google Drive API mode
> 
> Pros:
> 
> ```text
> real file IDs
> sharing metadata
> owner metadata
> web links
> Google Docs support
> safer long-term tracking
> ```
> 
> Cons:
> 
> ```text
> OAuth setup
> more moving parts
> more ways to annoy you
> ```
> 
> ## My recommendation
> 
> Build in this order:
> 
> ```text
> Phase 1: Local filesystem mode
> Phase 2: SQLite memory + review loop
> Phase 3: fuzzy rules
> Phase 4: embeddings
> Phase 5: Google Drive API metadata
> Phase 6: execution with verification
> ```
> 
> Do **not** start with the Drive API. That’s how we lose a weekend and gain nothing.
> 
> ---
> 
> # MVP Build Plan
> 
> ## Phase 1 — Local Inventory
> 
> Build:
> 
> ```text
> 01_scan_local_fs.py
> ```
> 
> Outputs:
> 
> ```text
> files table
> drive_inventory_raw.csv
> folder_tree_snapshot.md
> ```
> 
> It scans:
> 
> ```text
> C:\QiLabs\40_QiVault\My Drive
> ```
> 
> No AI yet.
> 
> ---
> 
> ## Phase 2 — Signals
> 
> Build:
> 
> ```text
> 02_extract_signals.py
> ```
> 
> Extract:
> 
> ```text
> extension
> filename words
> date from filename
> known people/entities
> known app/source
> sensitive keywords
> basic text preview for txt/md/csv/pdf later
> ```
> 
> ---
> 
> ## Phase 3 — Fuzzy Rules
> 
> Build:
> 
> ```text
> 03_score_rules.py
> ```
> 
> Reads YAML rules.
> 
> Outputs scores:
> 
> ```text
> file_id
> rule_id
> score
> reason
> ```
> 
> ---
> 
> ## Phase 4 — Proposals
> 
> Build:
> 
> ```text
> 04_generate_proposals.py
> ```
> 
> Creates:
> 
> ```text
> classification_proposal.csv
> needs_human_decision.csv
> ```
> 
> No execution.
> 
> ---
> 
> ## Phase 5 — Human Learning
> 
> Build:
> 
> ```text
> 06_apply_human_decisions.py
> 09_learn_from_decisions.py
> ```
> 
> Reads approved/corrected CSV.
> 
> Stores:
> 
> ```text
> human_decisions
> learned_examples
> suggested_learned_rules
> ```
> 
> ---
> 
> ## Phase 6 — UI
> 
> Only after the data loop works.
> 
> Use simple local UI:
> 
> ```text
> Streamlit or Textual
> ```
> 
> I’d start with Streamlit because visual review matters.
> 
> ---
> 
> # The Smart File Organizer Should Have “Brains,” Not Just Scripts
> 
> ## Brain 1 — Taxonomy
> 
> Your bucket model.
> 
> ```text
> Where can things go?
> ```
> 
> ## Brain 2 — Rules
> 
> Your fuzzy logic.
> 
> ```text
> What patterns mean what?
> ```
> 
> ## Brain 3 — Memory
> 
> Your approvals/corrections.
> 
> ```text
> What did Cody decide before?
> ```
> 
> ## Brain 4 — Similarity
> 
> Embeddings.
> 
> ```text
> What past approved files does this resemble?
> ```
> 
> ## Brain 5 — Safety
> 
> Hard overrides.
> 
> ```text
> What should never be auto-touched?
> ```
> 
> ---
> 
> # The Confidence Explanation Should Be Human-Readable
> 
> Every proposal should say:
> 
> ```text
> Suggested:
> 04_people/mom/care/messages
> 
> Why:
> - filename looks like a screenshot
> - OCR mentions medication and hospital
> - similar to 8 prior files approved into mom/care/messages
> - contains care-sensitive terms, so review is required
> 
> Confidence:
> 82
> 
> Risk:
> CARE_SENSITIVE
> 
> Allowed action:
> review only
> ```
> 
> That is much better than mystery AI vibes.
> 
> ---
> 
> # The Rule Format I’d Use
> 
> ```yaml
> id: mom_care_messages
> name: Mom Care Messages
> enabled: true
> target_bucket: 04_people
> target_subfolder: mom/care/messages
> risk_level: CARE_SENSITIVE
> requires_review: true
> 
> match:
>   any_filename_contains:
>     - screenshot
>     - messages
>     - sms
>     - messenger
>     - text
> 
>   any_text_contains:
>     - medication
>     - hospital
>     - nurse
>     - oxygen
>     - police
>     - neglect
> 
>   any_path_contains:
>     - screenshots
>     - downloads
>     - mom
> 
> weights:
>   filename_match: 25
>   text_match: 40
>   path_match: 15
>   learned_similarity: 30
> 
> thresholds:
>   propose_at: 50
>   strong_at: 80
> ```
> 
> ---
> 
> # What Not To Do
> 
> Do **not** build this as:
> 
> ```text
> One giant prompt that asks AI where everything goes.
> ```
> 
> Bad. Fragile. Expensive. Unverifiable.
> 
> Do **not** build this as:
> 
> ```text
> A script that recursively moves files based on filename.
> ```
> 
> Also bad. That is how `IMG_4021.png` becomes “assets” when it’s actually legal evidence.
> 
> Do **not** start with:
> 
> ```text
> auto-delete duplicates
> ```
> 
> Absolutely not. Duplicates get grouped, reviewed, and only later removed.
> 
> ---
> 
> # The Correct First Upgrade To Your Script
> 
> Your current bootstrap is Stage 0.
> 
> The next version should add:
> 
> ```text
> qidrivemaid.sqlite
> local filesystem scanner
> rules table
> human_decisions table
> basic fuzzy rule scoring
> review CSV generator
> learning ledger
> ```
> 
> Not Drive API. Not OCR. Not local LLM.
> 
> Build the boring spine first.
> 
> ---
> 
> # Version Roadmap
> 
> ## v0.1 — Scaffold
> 
> Already started.
> 
> ```text
> folders
> configs
> placeholder scripts
> control folders
> ```
> 
> ## v0.2 — Local inventory
> 
> ```text
> scan local Drive mount
> store SQLite records
> export inventory CSV
> ```
> 
> ## v0.3 — Rule scoring
> 
> ```text
> YAML fuzzy rules
> sensitivity detection
> confidence scores
> proposal generation
> ```
> 
> ## v0.4 — Human review loop
> 
> ```text
> review CSV
> approval import
> correction storage
> learned examples
> ```
> 
> ## v0.5 — Suggested rules
> 
> ```text
> detect repeated corrections
> suggest new fuzzy rules
> ```
> 
> ## v0.6 — Local UI
> 
> ```text
> one-file-at-a-time review cards
> approve/correct/hold buttons
> ```
> 
> ## v0.7 — Embeddings
> 
> ```text
> similarity to prior approved examples
> semantic grouping
> ```
> 
> ## v0.8 — Execution
> 
> ```text
> approved batch only
> 25 files max
> before/after logs
> verification
> ```
> 
> ## v0.9 — Google Drive API
> 
> ```text
> file IDs
> sharing metadata
> owner metadata
> web links
> Google Docs handling
> ```
> 
> ---
> 
> # My Opinionated Call
> 
> Build it as:
> 
> ```text
> QiDriveMaid = local-first adaptive file governance system
> ```
> 
> Not:
> 
> ```text
> Drive cleanup script
> ```
> 
> The cleanup script solves today.
> 
> The governance system prevents the mess from coming back.
> 
> The immediate next build should be:
> 
> ```text
> 1. SQLite schema
> 2. local folder scanner
> 3. basic fuzzy rules
> 4. review CSV
> 5. approval/correction importer
> 6. learned examples table
> ```
> 
> Once that loop works, adding local AI becomes easy instead of magical nonsense.
> 
> The first real intelligent behavior is not “LLM classifies files.”
> 
> It is:
> 
> > “Cody corrected this kind of file three times, so the system proposes a new rule.”
> 
> That is the money.

### User
> are we goind a local database or supabase, i want everything logged correctly and queriable.

### Assistant
> We go **hybrid**, but with a clear authority split.
> 
> ## Decision
> 
> ### **Local SQLite first**
> For the organizer itself.
> 
> ### **Supabase second**
> For centralized querying, dashboards, cross-device review, and long-term system reporting.
> 
> Not either/or. The correct answer is:
> 
> ```text
> SQLite = operational black box / local event recorder
> Supabase = central query layer / system memory / dashboard source
> ```
> 
> Your Drive system needs to be safe before it needs to be fancy.
> 
> ---
> 
> # Why not Supabase-only?
> 
> Because file organization touches the local filesystem:
> 
> ```text
> C:\QiLabs\40_QiVault\My Drive
> ```
> 
> That means the organizer needs to know:
> 
> - what exists locally
> - what disappeared
> - what changed
> - what failed
> - what path moved
> - what batch touched it
> - what the system thought before touching it
> 
> A local SQLite database is perfect for that. It is fast, inspectable, portable, and hard to accidentally break with network/auth nonsense.
> 
> Supabase-only would add friction too early.
> 
> ---
> 
> # Why not SQLite-only?
> 
> Because you specifically said:
> 
> > “I want everything logged correctly and queriable.”
> 
> Correct. That means eventually you want:
> 
> - dashboards
> - review queues
> - searchable history
> - “show me every file related to Mom care”
> - “show me all rejected proposals”
> - “show me every file moved by batch 004”
> - “show me files tagged legal-sensitive”
> - “show me everything touched last week”
> - “show me all corrections Cody made”
> - “show me repeated patterns that should become rules”
> 
> That belongs in Supabase/Postgres once the local loop works.
> 
> ---
> 
> # The Proper Architecture
> 
> ```text
> Local Filesystem
>       ↓
> QiDriveMaid Scanner
>       ↓
> SQLite Local DB
>       ↓
> CSV / Review UI / Approval
>       ↓
> Execution Logs
>       ↓
> Supabase Sync
>       ↓
> QiAccess / dashboards / reporting
> ```
> 
> ## Authority split
> 
> | Layer | Role | Canonical for |
> |---|---|---|
> | Local filesystem | actual files | what physically exists |
> | SQLite | local scan + operation ledger | what happened during organization |
> | Supabase | central queryable system record | reporting, dashboarding, long-term analysis |
> | Markdown/CSV exports | human-readable audit | review, backup, evidence trail |
> 
> ---
> 
> # My call
> 
> ## Build v1 with SQLite.
> 
> But design the schema so it can mirror into Supabase later with almost no pain.
> 
> Use names that work in both:
> 
> ```text
> snake_case
> uuid/id columns
> created_at
> updated_at
> batch_id
> status
> json metadata fields where useful
> ```
> 
> Do **not** make a goofy SQLite-only schema that has to be rewritten later.
> 
> ---
> 
> # Canonical logging model
> 
> Every important action should create an event.
> 
> This is the spine:
> 
> ```text
> file_events
> ```
> 
> Not just “current file state.”
> 
> You need an append-only history.
> 
> ## Example event types
> 
> ```text
> DISCOVERED
> SCANNED
> SIGNALS_EXTRACTED
> RULE_MATCHED
> PROPOSAL_CREATED
> PROPOSAL_APPROVED
> PROPOSAL_CORRECTED
> PROPOSAL_REJECTED
> BATCH_CREATED
> MOVE_STARTED
> MOVE_COMPLETED
> RENAME_STARTED
> RENAME_COMPLETED
> VERIFY_PASSED
> VERIFY_FAILED
> ERROR
> HOLD
> DO_NOT_TOUCH
> ```
> 
> That gives us receipts.
> 
> ---
> 
> # Local SQLite tables
> 
> Start with these:
> 
> ```text
> files
> file_snapshots
> file_events
> file_signals
> rules
> rule_matches
> proposals
> human_decisions
> learned_examples
> batches
> batch_items
> execution_logs
> sync_log
> ```
> 
> That is enough. Not bloated, not weak.
> 
> ---
> 
> ## `files`
> 
> Current known identity of a file.
> 
> ```sql
> id
> stable_key
> current_path
> current_name
> extension
> mime_type
> size_bytes
> content_hash
> created_at_fs
> modified_at_fs
> first_seen_at
> last_seen_at
> status
> ```
> 
> `stable_key` can be:
> 
> ```text
> hash + size + modified time
> ```
> 
> Until we later add Google Drive file IDs.
> 
> ---
> 
> ## `file_snapshots`
> 
> Point-in-time state.
> 
> ```sql
> id
> file_id
> scan_id
> path
> name
> size_bytes
> modified_at_fs
> content_hash
> exists_at_scan
> created_at
> ```
> 
> This lets us say:
> 
> > “Here is what the file looked like before batch 003.”
> 
> ---
> 
> ## `file_events`
> 
> Append-only audit trail.
> 
> ```sql
> id
> file_id
> batch_id
> event_type
> event_message
> actor
> source
> metadata_json
> created_at
> ```
> 
> Examples:
> 
> ```text
> actor = system
> actor = cody
> source = local_scan
> source = human_review
> source = executor
> ```
> 
> ---
> 
> ## `proposals`
> 
> What the system thinks should happen.
> 
> ```sql
> id
> file_id
> proposed_bucket
> proposed_subfolder
> proposed_name
> proposed_path
> confidence
> risk_level
> reason
> status
> created_at
> ```
> 
> ---
> 
> ## `human_decisions`
> 
> What you approved or corrected.
> 
> ```sql
> id
> proposal_id
> file_id
> decision
> approved_bucket
> approved_subfolder
> approved_name
> human_note
> correction_reason
> created_at
> ```
> 
> This is the learning layer.
> 
> ---
> 
> ## `batches`
> 
> Execution grouping.
> 
> ```sql
> id
> batch_name
> batch_status
> created_at
> approved_at
> executed_at
> verified_at
> notes
> ```
> 
> ---
> 
> ## `batch_items`
> 
> Every file in a batch.
> 
> ```sql
> id
> batch_id
> file_id
> proposal_id
> approved_action
> before_path
> after_path
> before_name
> after_name
> status
> error_message
> ```
> 
> ---
> 
> # Supabase later gets the same tables
> 
> When we sync to Supabase, we mirror the local SQLite tables into Postgres.
> 
> The only adjustment:
> 
> ```text
> SQLite id → UUID or text id
> metadata_json → jsonb
> timestamps → timestamptz
> ```
> 
> That is easy if we plan now.
> 
> ---
> 
> # What is canonical?
> 
> Here’s the non-confusing answer:
> 
> ## For real-time file operations
> 
> ```text
> SQLite is canonical.
> ```
> 
> Because it records what happened locally during a scan or batch.
> 
> ## For system-wide reporting
> 
> ```text
> Supabase is canonical.
> ```
> 
> Because it becomes the queryable long-term memory.
> 
> ## For file contents
> 
> ```text
> Drive / QiVault is canonical.
> ```
> 
> Because the file itself is the source.
> 
> ## For folder doctrine
> 
> ```text
> QiNexus rules are canonical.
> ```
> 
> Your blueprint already defines the bucket model and says Google Drive / QiNexus is the storage backbone. fileciteturn0file0
> 
> ---
> 
> # Practical build order
> 
> ## Phase 1 — SQLite local ledger
> 
> Build this now:
> 
> ```text
> qidrivemaid.sqlite
> scan local filesystem
> store files
> store snapshots
> store events
> export inventory CSV
> ```
> 
> ## Phase 2 — proposals + decisions
> 
> ```text
> rules
> rule_matches
> proposals
> human_decisions
> learned_examples
> review CSV
> ```
> 
> ## Phase 3 — execution audit
> 
> ```text
> batches
> batch_items
> execution_logs
> verification events
> ```
> 
> ## Phase 4 — Supabase sync
> 
> ```text
> push SQLite rows to Supabase
> sync_log tracks what uploaded
> QiAccess can query dashboards
> ```
> 
> ## Phase 5 — Supabase review UI
> 
> Later, if useful:
> 
> ```text
> Review queue inside QiAccess
> approve/correct from phone
> dashboard by bucket/risk/status
> ```
> 
> ---
> 
> # Important: use append-only logs
> 
> Do not only update rows.
> 
> Every meaningful change should be logged as an event.
> 
> Bad:
> 
> ```text
> file.status = moved
> ```
> 
> Better:
> 
> ```text
> file_events:
> - DISCOVERED
> - PROPOSAL_CREATED
> - PROPOSAL_APPROVED
> - MOVE_STARTED
> - MOVE_COMPLETED
> - VERIFY_PASSED
> ```
> 
> That gives you a real audit trail.
> 
> ---
> 
> # Final answer
> 
> Use:
> 
> ```text
> Local SQLite now.
> Supabase mirror later.
> ```
> 
> But design the SQLite schema like it already wants to become Supabase.
> 
> That gives you:
> 
> - safe local execution
> - complete audit trail
> - human approval history
> - adaptive learning
> - future dashboards
> - queryability
> - no premature cloud headache
> 
> This is the sane path. Supabase gets involved once the local organizer proves it can scan, propose, log, and learn without making a mess.

### User
> so are we using electron or tikinter

### Assistant
> Use **Tkinter first**, not Electron.
> 
> Electron is prettier. Tkinter is faster to build, easier to debug, local-native, and perfect for the first approval workflow. We do **not** need a whole mini Slack app just to approve file moves. That is overbuilding.
> 
> ## Decision
> 
> ```text
> v0.1–v0.4: CLI + CSV + Tkinter
> v0.5+: Streamlit or lightweight web UI
> v1.0+: Electron only if we truly need polished desktop packaging
> ```
> 
> ## Why Tkinter wins right now
> 
> | Option | Verdict | Why |
> |---|---:|---|
> | **Tkinter** | **Use now** | Built into Python, simple local GUI, works with SQLite, easy buttons, no frontend stack |
> | Electron | Not yet | Adds Node, bundling, IPC, build headaches, more surface area |
> | Streamlit | Later maybe | Great for review dashboards, but browser-based and less “desktop tool” |
> | Textual/TUI | Maybe | Good keyboard workflow, less visual for file previews |
> | PySide/PyQt | Later maybe | Better than Tkinter visually, but heavier |
> 
> ## The right stack
> 
> ```text
> Python
> SQLite
> YAML rules
> Tkinter review UI
> CSV/Markdown exports
> Local filesystem scanner
> Later: Supabase sync
> ```
> 
> Your QiNexus model already defines the organizing buckets and says Drive/QiNexus is the storage backbone, so the UI’s job is not to invent a new system — it just lets you review proposals against that structure. fileciteturn0file0
> 
> ---
> 
> # What the Tkinter app should do
> 
> ## Main screen
> 
> ```text
> QiDriveMaid
> 
> [Scan Local Drive]
> [Extract Signals]
> [Generate Proposals]
> [Open Review Queue]
> [Import Decisions]
> [View Logs]
> [Exit]
> ```
> 
> ## Review screen
> 
> One file at a time, ADHD-friendly:
> 
> ```text
> Current file:
> Screenshot_20260617_103944.png
> 
> Current path:
> Downloads/Screenshots
> 
> Suggested:
> 04_people/mom/care/messages
> 
> Suggested name:
> 2026-06-17_mom_care_text-message-screenshot_001.png
> 
> Confidence:
> 82
> 
> Risk:
> CARE_SENSITIVE
> 
> Reason:
> Filename/path suggests screenshot. Detected mom/care/legal-sensitive terms.
> 
> Buttons:
> [Approve]
> [Correct Folder]
> [Correct Name]
> [Hold]
> [Do Not Touch]
> [Next]
> ```
> 
> ## Correction modal
> 
> ```text
> Choose bucket:
> 04_people
> 
> Choose subfolder:
> mom/care/messages
> 
> Should similar files follow this correction?
> [Just this file]
> [Similar filenames]
> [Similar folder context]
> [Similar text/signals]
> ```
> 
> That last part is where the learning loop starts.
> 
> ---
> 
> # Why not Electron yet?
> 
> Electron makes sense when you need:
> 
> - polished desktop installer
> - drag/drop file preview
> - advanced search UI
> - full dashboard
> - synced Supabase login
> - cross-platform app distribution
> - embedded browser-like components
> 
> You do **not** need that for the first useful version.
> 
> Right now we need:
> 
> ```text
> scan → propose → approve/correct → learn → log
> ```
> 
> Tkinter can handle that without dragging in a whole JavaScript circus.
> 
> ---
> 
> # My recommended build path
> 
> ## Phase 1 — No GUI yet
> 
> Finish the backend:
> 
> ```text
> qidrivemaid.sqlite
> local scan
> file_events
> proposals
> human_decisions
> review CSV
> ```
> 
> ## Phase 2 — Tkinter approval app
> 
> Build only:
> 
> ```text
> review queue
> approve
> correct
> hold
> do not touch
> write decisions to SQLite
> export review log
> ```
> 
> ## Phase 3 — Better previews
> 
> Add:
> 
> ```text
> image preview
> text preview
> PDF metadata only
> open file button
> open containing folder button
> ```
> 
> ## Phase 4 — Supabase sync
> 
> Add:
> 
> ```text
> sync logs
> sync file records
> sync decisions
> sync proposals
> ```
> 
> ## Phase 5 — Decide if Electron is worth it
> 
> Only after the workflow proves itself.
> 
> ---
> 
> # Final answer
> 
> Use **Tkinter** for the first local app.
> 
> Do **not** use Electron yet.
> 
> Electron is for polish. Tkinter is for control. Right now we need control, logs, approvals, and learning — not a shiny wrapper on an unfinished brain.

### User
> ok theide is almost done we also have open code we can use, but i need  really smart ai to review the code

### Assistant
> Yes — and for this one, the review needs to be **safety + architecture**, not just “does the Python run.” File organizer code can quietly destroy trust if it moves one wrong thing.

### Assistant
> Yes. We need a **serious review gate** before this thing gets permission to touch files.
> 
> Right now, the review should focus on:
> 
> 1. **Can it accidentally modify files?**
> 2. **Is every action logged?**
> 3. **Is the SQLite schema sane and queryable?**
> 4. **Can it recover from interruption?**
> 5. **Are approvals actually required before execution?**
> 6. **Does it follow the QiVault/QiNexus bucket doctrine instead of inventing chaos?** Your blueprint already says Drive/QiNexus is the storage backbone and defines the bucket model, so the code needs to obey that. fileciteturn0file0
> 
> ---
> 
> # What to send me
> 
> Best option: upload a zip of the project folder.
> 
> Second best: paste:
> 
> ```text
> qidrivemaid/
>   tree output
>   README.md
>   config/*.yml
>   scripts/*.py
>   app/*.py
>   schema.sql or db setup file
> ```
> 
> Most important files to review first:
> 
> ```text
> database/schema file
> scanner script
> proposal generator
> review/approval importer
> executor script
> verifier script
> Tkinter app
> rules config
> ```
> 
> The executor is the danger zone. That gets reviewed like it’s handling court evidence, because for you, some of it basically is.
> 
> ---
> 
> # Use This Review Prompt in the IDE / OpenCode
> 
> Paste this into the code agent:
> 
> ```text
> You are reviewing QiDriveMaid, a local-first adaptive file organizer for a Google Drive-mounted Windows filesystem.
> 
> Context:
> - The local Drive path is C:\QiLabs\40_QiVault\My Drive
> - The system must organize files according to the QiVault/QiNexus bucket model:
>   00_inbox
>   01_workbench
>   02_timeline
>   03_life
>   04_people
>   05_business
>   06_finance
>   07_legal
>   08_tech
>   09_assets
>   10_data
>   11_reference
>   12_archive
>   13_system
> 
> Primary requirement:
> This system must be safe, auditable, reversible, and human-approved.
> 
> Review the code for the following:
> 
> 1. Safety
> - Confirm no script can move, rename, delete, archive, or overwrite files unless explicitly approved.
> - Confirm execution is disabled or gated by approved review records.
> - Confirm sensitive files are never auto-executed.
> - Confirm batch size limits exist or are planned.
> - Confirm there is no dangerous recursive move logic.
> - Confirm dry-run behavior exists before execution.
> 
> 2. Database / Logging
> - Review the SQLite schema.
> - Confirm the schema supports files, snapshots, events, proposals, decisions, batches, batch items, rule matches, and execution logs.
> - Confirm important actions write append-only file_events.
> - Confirm the design is queryable and later mirrorable to Supabase/Postgres.
> - Confirm timestamps are consistent.
> - Confirm IDs are stable enough for local filesystem tracking.
> 
> 3. Rule Engine
> - Confirm rules are separated from execution.
> - Confirm fuzzy rules produce proposals, not actions.
> - Confirm sensitive overrides win over normal classification.
> - Confirm unknown/ambiguous files go to REVIEW_REQUIRED.
> - Confirm legal, finance, medical/care, identity, court, immigration, tax, signed, and evidence-like files are review-gated.
> 
> 4. Human Review Loop
> - Confirm approvals/corrections are stored.
> - Confirm corrections can become learned examples.
> - Confirm proposed learned rules require approval before becoming durable rules.
> - Confirm there is a path for APPROVE, CORRECT, HOLD, SKIP, and DO_NOT_TOUCH.
> 
> 5. Local Filesystem Correctness
> - Review Windows path handling.
> - Confirm paths are normalized safely.
> - Confirm the scanner avoids following dangerous recursive loops.
> - Confirm hidden/system folders are handled intentionally.
> - Confirm files inside the control/system folder are not accidentally classified for movement.
> - Confirm the app does not organize its own database, logs, scripts, or review files.
> 
> 6. Recovery / Idempotency
> - Confirm interrupted scans can resume or rerun safely.
> - Confirm repeated scans do not create duplicate garbage.
> - Confirm execution logs can reconstruct what happened.
> - Confirm verifier can compare before/after state.
> - Confirm failed moves are logged without corrupting approval state.
> 
> 7. UX / Tkinter
> - Confirm the UI does not allow accidental approval of huge batches.
> - Confirm risky files are visually marked.
> - Confirm one-file-at-a-time or small-batch review is supported.
> - Confirm approval buttons write decisions, not direct file actions.
> - Confirm executor remains separate from review UI.
> 
> 8. Code Quality
> - Identify brittle functions.
> - Identify duplicated logic.
> - Identify unclear names.
> - Identify missing tests.
> - Identify places where config should replace hardcoded logic.
> - Identify any high-risk assumptions.
> 
> Output format:
> A. Executive summary
> B. Critical blockers
> C. High-risk issues
> D. Medium-risk issues
> E. Low-risk cleanup
> F. Missing tests
> G. Recommended next patch order
> H. Files/functions that should not be trusted yet
> I. Exact suggested changes, with filenames
> 
> Do not patch anything yet. Review only.
> ```
> 
> ---
> 
> # My Review Rubric
> 
> When you send me the code, I’ll grade it like this:
> 
> | Area | Pass Condition |
> |---|---|
> | **Safety** | Nothing mutates files without explicit approved record |
> | **Logging** | Every meaningful action creates an append-only event |
> | **Database** | Queryable, normalized enough, Supabase-ready later |
> | **Rules** | Rules score/propose only; they do not execute |
> | **Sensitive files** | Legal/finance/care/identity always review-gated |
> | **Recovery** | Interrupted runs don’t leave mystery state |
> | **UI** | Approval is clear, deliberate, and not batch-chaotic |
> | **Executor** | Locked down, small batches, before/after snapshots |
> | **Verifier** | Confirms actual filesystem result after execution |
> 
> ---
> 
> # The hard line
> 
> Until review passes, the executor should stay functionally locked.
> 
> Acceptable:
> 
> ```text
> scan
> index
> extract signals
> score rules
> generate proposals
> show review queue
> store decisions
> ```
> 
> Not acceptable yet:
> 
> ```text
> move files
> rename files
> delete duplicates
> archive automatically
> clean empty folders
> bulk approve everything
> ```
> 
> That’s how Drive becomes a crime scene.
> 
> ---
> 
> # What I want first
> 
> Send me either:
> 
> ```text
> project zip
> ```
> 
> or paste the project tree plus these files:
> 
> ```text
> schema.sql
> database.py
> scanner.py
> rules.py
> proposals.py
> review.py
> executor.py
> verify.py
> app.py
> ```
> 
> I’ll give you a proper code review with blockers, not fluffy AI applause.

### Assistant
> I’ve got the context map. I’m going to review it as a **pre-execution safety audit**, not a cute code skim. The danger file is the executor/UI path, so that’s where I’m starting.

### Assistant
> First pass finding: the prototype is **not garbage** — the spine is there: scanner, SQLite, rule scoring, proposals, human decisions, batches, executor, verifier, and Tkinter. But the executor/UI path is too permissive for real Drive. We need one safety patch before it touches anything real.

### Assistant
> ## Verdict
> 
> **Do not run this on the real Drive yet.**
> 
> The architecture is pointed in the right direction: local SQLite, scanner, signal extraction, rule scoring, proposals, human review, batches, executor, verifier, and Tkinter UI are all present. That is the correct spine. The uploaded context map shows the full `61_QiFileMaid` project with `local_review_ui.py`, config rules, SQLite DB, inventory/review outputs, scratch test files, and pipeline scripts. fileciteturn2file4
> 
> But the current version is still **prototype-safe**, not **real-file-safe**.
> 
> The main problem: **the executor can perform real moves too easily**, and the UI exposes that executor like a normal button. That is too spicy for your actual Drive.
> 
> ---
> 
> # A. Executive Summary
> 
> ## What’s good
> 
> You have the right major pieces:
> 
> | Piece | Status |
> |---|---:|
> | SQLite local database | Good start |
> | File inventory | Working |
> | Signals extraction | Working basic version |
> | Rule scoring | Working basic version |
> | Proposal generation | Working |
> | Human review CSV/UI | Working prototype |
> | Learned examples | Started |
> | Batch execution | Exists but unsafe |
> | Verification | Exists but shallow |
> 
> The database design includes files, snapshots, events, signals, rules, rule matches, proposals, human decisions, learned examples, batches, batch items, and sync logging. That is the right shape for local-first now and Supabase mirror later. fileciteturn2file1
> 
> The bucket model is also aligned with your QiNexus doctrine: Drive/QiNexus is the storage backbone, and the canonical roots include `00_inbox`, `04_people`, `06_finance`, `07_legal`, `10_data`, `13_system`, etc. fileciteturn2file5
> 
> ## What’s not safe yet
> 
> The executor uses real filesystem movement. It creates destination folders and calls `shutil.move`. That is fine eventually, but not before path guards, dry-run mode, destination collision checks, typed confirmation, and batch-specific execution exist.
> 
> The Tkinter UI also has a visible **“Execute Approved Batch”** button that runs the executor and verifier directly. fileciteturn2file3
> 
> That button is the danger goblin. Remove or disable it until safety gates exist.
> 
> ---
> 
> # B. Critical Blockers
> 
> ## 1. Disable real execution from the UI
> 
> Right now the UI has:
> 
> ```text
> 6. Execute Approved Batch
> ```
> 
> and `run_executor()` calls:
> 
> ```text
> 07_execute_approved_batch.py
> 08_verify_batch.py
> ```
> 
> That is too easy to click by accident. fileciteturn2file3
> 
> ### Fix
> 
> For now, replace that button with:
> 
> ```text
> Execution Locked — Export Approved Batch Only
> ```
> 
> The executor should only be runnable from a deliberately separate flow after a review report.
> 
> ---
> 
> ## 2. Add dry-run mode to the executor
> 
> The executor needs:
> 
> ```text
> --dry-run
> ```
> 
> Default should be dry-run.
> 
> Real execution should require something obnoxious like:
> 
> ```text
> --execute --confirm-token MOVE_FILES_I_UNDERSTAND
> ```
> 
> No token, no move.
> 
> ---
> 
> ## 3. Add path traversal protection
> 
> Approved paths must not be able to escape the target directory.
> 
> Block anything containing:
> 
> ```text
> ..
> absolute paths
> drive letters like C:\
> UNC paths like \\server
> leading slash
> ```
> 
> Every destination must resolve inside the selected target root.
> 
> Required guard:
> 
> ```python
> target_root = target_dir.resolve()
> dest = (target_root / after_path_str).resolve()
> 
> if not str(dest).startswith(str(target_root)):
>     raise RuntimeError("Blocked unsafe destination outside target root")
> ```
> 
> Same idea for source paths.
> 
> ---
> 
> ## 4. Add destination collision protection
> 
> Before moving:
> 
> ```python
> if dest_file.exists():
>     fail safely
> ```
> 
> Do **not** overwrite. Do **not** auto-suffix yet. Just fail and log.
> 
> Later we can add:
> 
> ```text
> _conflict001
> ```
> 
> But not now.
> 
> ---
> 
> ## 5. Batch execution must require explicit batch ID
> 
> Current executor grabs the latest approved batch:
> 
> ```text
> latest approved batch
> ```
> 
> Bad. Too magical.
> 
> It should require:
> 
> ```text
> --batch-id 12
> ```
> 
> No batch ID, no execution.
> 
> Otherwise you can accidentally execute an old batch you forgot existed.
> 
> ---
> 
> ## 6. Approval flags are not respected strongly enough
> 
> The CSV has:
> 
> ```text
> approve_move
> approve_rename
> final_decision
> ```
> 
> But the current logic mostly treats:
> 
> ```text
> APPROVE = MOVE_RENAME
> CORRECT = MOVE_RENAME
> ```
> 
> That is too blunt.
> 
> Correct behavior:
> 
> | final_decision | approve_move | approve_rename | Action |
> |---|---:|---:|---|
> | APPROVE | Y | Y | MOVE_RENAME |
> | APPROVE | Y | N | MOVE_ONLY |
> | APPROVE | N | Y | RENAME_ONLY |
> | APPROVE | N | N | NOOP / invalid |
> | HOLD | any | any | no execution |
> | SKIP | any | any | no execution |
> | DO_NOT_TOUCH | any | any | no execution, locked |
> 
> Right now you need separate approved actions, not just `MOVE_RENAME`.
> 
> ---
> 
> # C. High-Risk Issues
> 
> ## 1. Scanner will organize its own organs if pointed at the wrong root
> 
> The project tree includes:
> 
> ```text
> data/qifilemaid.sqlite
> output/inventory
> output/review
> scratch_test_files
> scripts
> __pycache__
> ```
> 
> Those should not be scanned as normal files when this eventually points at real Drive or app folders. fileciteturn2file4
> 
> ### Add exclusions
> 
> Hard-exclude:
> 
> ```text
> .git
> __pycache__
> .venv
> node_modules
> data/qifilemaid.sqlite
> output
> scratch_test_files
> 13_system/drive_cleanup
> 60_QiApps/61_QiFileMaid
> ```
> 
> Eventually make this configurable:
> 
> ```text
> config/exclude_paths.yml
> ```
> 
> ---
> 
> ## 2. Stable file identity is not strong enough yet
> 
> Current scanner identifies existing files primarily by `current_path`.
> 
> That means if a file is manually moved outside the app, the next scan may treat it as:
> 
> ```text
> old file = MISSING
> new file = DISCOVERED
> ```
> 
> Instead, scanner should attempt identity resolution by:
> 
> ```text
> content_hash + size_bytes
> ```
> 
> Then update `current_path`.
> 
> Use path as location, not identity.
> 
> ---
> 
> ## 3. Proposal generation deletes pending proposals
> 
> The proposal script deletes pending proposals before regenerating.
> 
> That can wipe an active review queue.
> 
> Better:
> 
> ```text
> proposal_runs table
> proposal_run_id on proposals
> superseded_at column
> ```
> 
> Do not delete pending proposals silently. Mark them as:
> 
> ```text
> SUPERSEDED
> ```
> 
> ---
> 
> ## 4. Already-organized files are being renamed badly
> 
> Your review CSV shows this kind of name:
> 
> ```text
> 2026-06-17_mom_care_mom_general_mom_discharge_summary_raw_raw.txt
> ```
> 
> That means the naming logic is stacking metadata onto already-normalized names.
> 
> Bad. It will create monster filenames.
> 
> ### Add guard
> 
> If the file is already inside the proposed bucket/subfolder and already has date/entity/topic/status shape, propose:
> 
> ```text
> NO_RENAME
> ```
> 
> or keep the existing filename.
> 
> ---
> 
> ## 5. Sensitive files are detected but not execution-gated
> 
> The rules do identify sensitive categories like finance and medical/care. The sample proposals show `FINANCE_SENSITIVE` and `MEDICAL_CARE_SENSITIVE`. That is good.
> 
> But sensitive files should require a stronger approval state before execution:
> 
> ```text
> SENSITIVE_APPROVED
> ```
> 
> Not just regular `APPROVED`.
> 
> For legal, care, finance, identity, tax, court, immigration, signed, evidence:
> 
> ```text
> requires_sensitive_confirm = true
> ```
> 
> ---
> 
> # D. Medium-Risk Issues
> 
> ## 1. Rule thresholds are defined but not enforced correctly
> 
> Your YAML rules include:
> 
> ```text
> propose_at
> strong_at
> ```
> 
> But scoring inserts any match with score above zero.
> 
> Fix:
> 
> ```python
> if score >= propose_at:
>     insert rule match
> ```
> 
> Anything below threshold should be ignored or logged as weak only.
> 
> ---
> 
> ## 2. Finance override is too broad
> 
> This rule sends all transaction/bank/invoice-ish files to:
> 
> ```text
> 06_finance/transactions/firefly
> ```
> 
> But not all finance files are Firefly.
> 
> Better targets:
> 
> ```text
> 06_finance/review
> 06_finance/transactions/review
> 06_finance/statements/review
> ```
> 
> Only use Firefly if `firefly` is detected in filename/path/text.
> 
> ---
> 
> ## 3. Human review batch status is misleading
> 
> The UI creates a batch when opening the review queue, then marks it `APPROVED` when you reach the end.
> 
> But using **Next / Skip** does not record a decision.
> 
> So the batch can become `APPROVED` even if very little was approved.
> 
> Fix:
> 
> ```text
> PENDING_REVIEW
> PARTIALLY_REVIEWED
> READY_FOR_EXECUTION
> EXECUTED
> VERIFIED
> ```
> 
> Only mark `READY_FOR_EXECUTION` if at least one executable item exists and all items have explicit decisions.
> 
> ---
> 
> ## 4. Verifier is too shallow
> 
> Verifier checks destination exists and file size matches.
> 
> That is not enough.
> 
> Add:
> 
> ```text
> content_hash check
> source no longer exists when move expected
> destination inside target root
> batch item status only becomes VERIFIED after check
> ```
> 
> ---
> 
> ## 5. SQLite needs foreign key enforcement
> 
> SQLite does not enforce foreign keys unless enabled per connection.
> 
> Add this in `get_db_connection()`:
> 
> ```python
> conn.execute("PRAGMA foreign_keys = ON")
> conn.execute("PRAGMA journal_mode = WAL")
> ```
> 
> ---
> 
> # E. Low-Risk Cleanup
> 
> ## 1. README is basically empty
> 
> Current README is just:
> 
> ```text
> # 61_QiFileMaid
> ```
> 
> It needs real operating instructions.
> 
> Minimum sections:
> 
> ```text
> Purpose
> Safety model
> Pipeline
> Modes
> Database schema
> How to test on scratch files
> Forbidden real-drive execution rules
> ```
> 
> ---
> 
> ## 2. Remove generated junk from repo
> 
> Do not commit:
> 
> ```text
> data/qifilemaid.sqlite
> output/*.csv
> __pycache__
> scratch_test_files after testing
> ```
> 
> Keep:
> 
> ```text
> data/.gitkeep
> output/.gitkeep
> scratch_test_files/README.md maybe
> ```
> 
> Add `.gitignore`.
> 
> ---
> 
> ## 3. Use `sys.executable` instead of `"python"`
> 
> In the Tkinter UI, replace:
> 
> ```python
> cmd = ["python", str(script_path)] + args
> ```
> 
> with:
> 
> ```python
> cmd = [sys.executable, str(script_path)] + args
> ```
> 
> This avoids the “wrong Python environment” nonsense.
> 
> ---
> 
> # F. Missing Tests
> 
> You need these before real Drive execution:
> 
> ```text
> test_dry_run_does_not_move_files
> test_execute_requires_batch_id
> test_execute_requires_confirmation_token
> test_path_traversal_is_blocked
> test_absolute_destination_is_blocked
> test_destination_collision_fails_safely
> test_hold_skip_do_not_touch_do_not_execute
> test_sensitive_file_requires_sensitive_approval
> test_scan_excludes_app_and_system_folders
> test_rescan_does_not_duplicate_same_file
> test_manual_move_updates_existing_file_identity
> test_verify_detects_hash_mismatch
> ```
> 
> No tests, no real Drive. Period.
> 
> ---
> 
> # G. Recommended Next Patch Order
> 
> ## Patch 1 — Lock execution
> 
> Do this first.
> 
> ```text
> Disable UI execution button.
> Executor defaults to dry-run.
> Executor requires explicit batch ID.
> Executor requires confirmation token for real move.
> ```
> 
> ## Patch 2 — Path safety
> 
> ```text
> safe_resolve_under_root()
> block path traversal
> block absolute paths
> block destination collisions
> ```
> 
> ## Patch 3 — Batch correctness
> 
> ```text
> APPROVE + approve_move/approve_rename determine action.
> Batch status becomes READY_FOR_EXECUTION only after explicit finalization.
> ```
> 
> ## Patch 4 — Scanner exclusions
> 
> ```text
> exclude app folders, output, DB, pycache, git, drive cleanup system folders.
> ```
> 
> ## Patch 5 — Improve naming
> 
> ```text
> Avoid renaming already-normalized files.
> Avoid duplicated entity/topic/status tokens.
> ```
> 
> ## Patch 6 — Better identity
> 
> ```text
> Resolve files by content_hash + size before current_path.
> ```
> 
> ## Patch 7 — Tests
> 
> Then test against `scratch_test_files`.
> 
> ---
> 
> # H. Files Not Trusted Yet
> 
> These are useful but **not real-drive trusted yet**:
> 
> ```text
> app/local_review_ui.py
> scripts/06_apply_human_decisions.py
> scripts/07_execute_approved_batch.py
> scripts/08_verify_batch.py
> scripts/04_generate_proposals.py
> scripts/01_scan_local_fs.py
> ```
> 
> Most dangerous:
> 
> ```text
> scripts/07_execute_approved_batch.py
> ```
> 
> Second most dangerous:
> 
> ```text
> app/local_review_ui.py
> ```
> 
> Because it exposes execution.
> 
> ---
> 
> # I. Copy/Paste Patch Prompt For The IDE
> 
> Use this:
> 
> ```text
> Review and patch QiFileMaid for pre-real-drive safety.
> 
> This is a local-first adaptive file organizer. It must not touch real Drive files until execution safety gates are implemented.
> 
> Context:
> - Project path: 60_QiApps/61_QiFileMaid
> - Local test target: scratch_test_files
> - Real Drive target later: C:\QiLabs\40_QiVault\My Drive
> - Canonical buckets:
>   00_inbox
>   01_workbench
>   02_timeline
>   03_life
>   04_people
>   05_business
>   06_finance
>   07_legal
>   08_tech
>   09_assets
>   10_data
>   11_reference
>   12_archive
>   13_system
> 
> Patch in this order:
> 
> 1. Disable real execution from app/local_review_ui.py
> - Remove or disable the "Execute Approved Batch" button.
> - Replace it with "Execution Locked — Export Approved Batch Only".
> - Do not allow the GUI to run 07_execute_approved_batch.py yet.
> - The UI may show a warning explaining that execution requires CLI safety gates.
> 
> 2. Harden scripts/07_execute_approved_batch.py
> - Default to dry-run mode.
> - Add required --batch-id.
> - Add --execute flag.
> - Add --confirm-token MOVE_FILES_I_UNDERSTAND for actual moves.
> - If --execute is not provided, print planned actions only and log DRY_RUN_PLANNED events.
> - If --execute is provided without the exact confirm token, abort.
> - Add batch size cap of 25 executable items.
> - Add safe path resolution:
>   - block absolute paths
>   - block drive-letter paths
>   - block UNC paths
>   - block any path containing ..
>   - ensure source and destination resolve inside target_dir
> - Add destination collision protection:
>   - if destination exists, mark item FAILURE and log error
>   - never overwrite
> - Require batch_status = READY_FOR_EXECUTION, not merely APPROVED.
> - Do not grab the latest approved batch automatically.
> 
> 3. Fix scripts/06_apply_human_decisions.py
> - Respect approve_move and approve_rename flags.
> - Map decisions to approved_action:
>   APPROVE + move Y + rename Y = MOVE_RENAME
>   APPROVE + move Y + rename N = MOVE_ONLY
>   APPROVE + move N + rename Y = RENAME_ONLY
>   APPROVE + move N + rename N = NOOP_INVALID
>   CORRECT uses the same flags
>   HOLD/SKIP/DO_NOT_TOUCH must never create executable actions
> - Only create executable batch_items for explicit executable actions.
> - Add batch_status = READY_FOR_EXECUTION only if at least one executable item exists.
> - Otherwise keep batch_status = REVIEW_COMPLETE_NO_EXECUTION.
> - Store approved_path/full target in human_decisions or metadata_json.
> 
> 4. Harden scanner in scripts/01_scan_local_fs.py
> - Add config/exclude_paths.yml.
> - Exclude:
>   .git
>   __pycache__
>   .venv
>   venv
>   node_modules
>   data/qifilemaid.sqlite
>   output
>   scratch_test_files unless target_dir is exactly scratch_test_files
>   13_system/drive_cleanup
>   60_QiApps/61_QiFileMaid
> - Do not scan the app's own database, outputs, logs, or review files.
> - Resolve target_dir and reject scanning system roots accidentally.
> 
> 5. Improve file identity
> - Use content_hash + size_bytes as secondary identity when current_path is not found.
> - If a matching file hash/size exists at a new path, update the existing record instead of creating a duplicate.
> - Keep path snapshots append-only.
> 
> 6. Fix proposal/naming logic in scripts/04_generate_proposals.py
> - Do not rename already-normalized files.
> - Avoid duplicate tokens like mom_care_mom...raw_raw.
> - If file is already in proposed bucket/subfolder and name is acceptable, set proposed action to NOOP_REVIEW.
> - Do not delete pending proposals. Mark old pending proposals SUPERSEDED instead.
> 
> 7. Enforce thresholds in scripts/03_score_rules.py
> - Use rule thresholds.propose_at.
> - Do not insert rule_matches below propose_at.
> - Keep weak matches only in debug output if needed.
> 
> 8. Add SQLite safety in scripts/db.py
> - Enable PRAGMA foreign_keys = ON on every connection.
> - Enable WAL mode.
> - Add indexes for file_events.file_id, proposals.file_id, batch_items.batch_id, batch_items.file_id.
> - Add constraints/checks where practical for statuses.
> 
> 9. Add tests
> Create tests for:
> - dry-run does not move files
> - execution requires batch id
> - execution requires confirmation token
> - path traversal blocked
> - absolute destination blocked
> - destination collision blocked
> - SKIP/HOLD/DO_NOT_TOUCH do not execute
> - sensitive files require explicit approval state
> - scanner excludes app/system folders
> - verifier catches hash mismatch
> 
> Do not add AI/LLM features yet.
> Do not add Supabase sync yet.
> Do not touch real Drive.
> Patch only for safety, auditability, idempotency, and review correctness.
> ```
> 
> ---
> 
> # Bottom Line
> 
> This is a **good v0.2 prototype**.
> 
> But it is **not allowed near the real Drive yet**.
> 
> One safety patch away from being respectable. Two patches away from being useful. Three patches away from “okay, now we can start letting it clean a tiny approved batch.”

### User
> if this is a real ai file helper doesnt it need a vector storage or symtatic graph

### Assistant
> Yes — **eventually**. But not before the safety spine is locked.
> 
> A real AI file helper needs **three brains**, in this order:
> 
> ```text
> 1. Relational ledger = what exists, what happened, what was approved
> 2. Vector memory = what this file is similar to
> 3. Semantic graph = how people/projects/matters/docs/entities relate
> ```
> 
> Right now QiFileMaid has #1 started: SQLite tables for files, snapshots, events, rule matches, proposals, human decisions, learned examples, batches, batch items, and sync logging. That is the correct first layer. fileciteturn4file0
> 
> But yes: to become a **smart AI file helper**, it should add vector storage and later a semantic graph.
> 
> ---
> 
> # The correct architecture
> 
> ```text
> SQLite / Supabase
>   = factual ledger
>   = audit trail
>   = approvals
>   = current state
>   = batches
>   = events
> 
> Vector store
>   = semantic similarity
>   = "this looks like those 14 prior files"
>   = fuzzy search
>   = clustering
>   = examples-based learning
> 
> Semantic graph
>   = relationships
>   = Mom ↔ care ↔ hospital ↔ medication ↔ evidence
>   = Hertz ↔ Lyft ↔ rental dispute ↔ receipts ↔ screenshots
>   = Zai ↔ immigration ↔ SIV ↔ asylum ↔ USCIS docs
> ```
> 
> Plain English:
> 
> | Layer | Question it answers |
> |---|---|
> | **SQLite/Postgres** | What happened? |
> | **Vector store** | What is this similar to? |
> | **Graph** | What is this connected to? |
> 
> They are not interchangeable.
> 
> ---
> 
> # Do we need vector storage now?
> 
> ## Not yet for execution.
> 
> But yes for **smart classification**.
> 
> Right now your system can say:
> 
> > filename contains `bank`, so finance.
> 
> That’s useful but basic.
> 
> Vector memory lets it say:
> 
> > This file looks semantically similar to prior files Cody approved into `07_legal/mom_care/evidence/messages`, even though the filename is just `Screenshot_4021.png`.
> 
> That is the real upgrade.
> 
> ---
> 
> # What vector storage should store
> 
> Do **not** embed whole files blindly. That’s expensive and messy.
> 
> Embed **file intelligence records**:
> 
> ```text
> file_id
> content_hash
> current_name
> current_path
> filename_tokens
> path_tokens
> text_preview
> detected_date
> detected_entity
> detected_domain
> sensitivity_flags
> approved_bucket
> approved_subfolder
> human_decision
> human_note
> ```
> 
> That becomes a semantic memory card for each file.
> 
> Example:
> 
> ```text
> Screenshot_20260617_103944.png
> text mentions: medication, police, neglect, hospital
> entity: mom
> domain: care/legal
> human approved to: 07_legal/mom_care/evidence/messages
> ```
> 
> Next similar screenshot gets boosted toward that same path.
> 
> ---
> 
> # What vector DB should we use?
> 
> For your setup:
> 
> ## Best first choice: **ChromaDB**
> 
> Why:
> 
> ```text
> local
> simple
> Python-native
> good enough
> easy metadata filters
> works without Supabase
> ```
> 
> Path:
> 
> ```text
> 60_QiApps/61_QiFileMaid/data/vector/chroma/
> ```
> 
> Use it for v0.5-ish.
> 
> ## Later option: Supabase `pgvector`
> 
> Once Supabase sync exists, mirror embeddings there.
> 
> ```text
> local Chroma = working memory
> Supabase pgvector = central memory
> ```
> 
> Do not start with pgvector. That adds cloud complexity too early.
> 
> ---
> 
> # Do we need a semantic graph?
> 
> Yes, but later.
> 
> The graph is not for “which folder should this file go in?” at first.
> 
> The graph is for:
> 
> ```text
> show me every document connected to Mom's June 2026 hospitalization
> show me every file tied to Hertz/Lyft rental dispute
> show me care records that also became legal evidence
> show me people connected to a matter
> show me timeline of events across files/messages/receipts
> ```
> 
> That is **QiLife/QiNexus intelligence**, not just cleanup.
> 
> Your blueprint already says vector search, graphs, exports, dashboards, and reports are useful but **derived systems**, not canonical truth. Canonical truth stays in source files, database records, repo docs, and designated operating pages. fileciteturn4file5
> 
> That means graph/vector are **advisors**, not kings.
> 
> ---
> 
> # What graph storage should we use?
> 
> ## Do not add Neo4j inside QiFileMaid yet.
> 
> You already have the idea of Neo4j/qiserver in the broader system, but for this app we should start lighter. The blueprint lists Neo4j as a possible qiserver service layer component, not something every app needs immediately. fileciteturn4file6
> 
> Use SQLite edge tables first:
> 
> ```text
> entities
> file_entities
> relationships
> ```
> 
> That gives you graph logic without spinning up another dependency.
> 
> Later, if the relationships become valuable:
> 
> ```text
> SQLite edge tables → Supabase relational graph → Neo4j projection
> ```
> 
> Not:
> 
> ```text
> install Neo4j because “AI graph” sounds sexy
> ```
> 
> That’s how we build a cathedral before we have a front door. And we are not doing cathedral nonsense.
> 
> ---
> 
> # Add these tables before adding Chroma
> 
> ## `entities`
> 
> ```sql
> CREATE TABLE entities (
>     id INTEGER PRIMARY KEY AUTOINCREMENT,
>     entity_type TEXT NOT NULL,
>     canonical_name TEXT NOT NULL,
>     aliases_json TEXT,
>     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
>     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
>     UNIQUE(entity_type, canonical_name)
> );
> ```
> 
> Entity types:
> 
> ```text
> person
> organization
> matter
> project
> account
> vehicle
> location
> system
> document_type
> topic
> ```
> 
> Examples:
> 
> ```text
> person: mom
> organization: Hertz
> organization: Lyft
> matter: hertz_lyft_rental_dispute
> matter: mom_care_june_2026
> system: QiFileMaid
> document_type: bank_statement
> ```
> 
> ---
> 
> ## `file_entities`
> 
> ```sql
> CREATE TABLE file_entities (
>     id INTEGER PRIMARY KEY AUTOINCREMENT,
>     file_id INTEGER NOT NULL,
>     entity_id INTEGER NOT NULL,
>     role TEXT,
>     confidence INTEGER,
>     source TEXT,
>     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
>     FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
>     FOREIGN KEY(entity_id) REFERENCES entities(id) ON DELETE CASCADE
> );
> ```
> 
> Roles:
> 
> ```text
> subject
> sender
> recipient
> payer
> payee
> provider
> care_subject
> legal_party
> source_system
> ```
> 
> ---
> 
> ## `relationships`
> 
> ```sql
> CREATE TABLE relationships (
>     id INTEGER PRIMARY KEY AUTOINCREMENT,
>     from_entity_id INTEGER NOT NULL,
>     to_entity_id INTEGER NOT NULL,
>     relationship_type TEXT NOT NULL,
>     confidence INTEGER,
>     source TEXT,
>     evidence_file_id INTEGER,
>     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
>     FOREIGN KEY(from_entity_id) REFERENCES entities(id),
>     FOREIGN KEY(to_entity_id) REFERENCES entities(id),
>     FOREIGN KEY(evidence_file_id) REFERENCES files(id)
> );
> ```
> 
> Examples:
> 
> ```text
> mom --has_care_matter--> mom_care_june_2026
> Hertz --involved_in--> hertz_lyft_rental_dispute
> Lyft --involved_in--> hertz_lyft_rental_dispute
> bank_statement_june.txt --mentions--> IRS
> ```
> 
> ---
> 
> # Add vector tables too
> 
> Even if Chroma stores the vectors, SQLite should track them.
> 
> ## `embedding_index`
> 
> ```sql
> CREATE TABLE embedding_index (
>     id INTEGER PRIMARY KEY AUTOINCREMENT,
>     file_id INTEGER NOT NULL,
>     embedding_provider TEXT NOT NULL,
>     embedding_model TEXT NOT NULL,
>     vector_store TEXT NOT NULL,
>     vector_collection TEXT NOT NULL,
>     vector_id TEXT NOT NULL,
>     embedded_text_hash TEXT,
>     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
>     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
>     FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE
> );
> ```
> 
> Example:
> 
> ```text
> embedding_provider = local
> embedding_model = nomic-embed-text
> vector_store = chroma
> vector_collection = qifilemaid_files
> vector_id = file_123_signal_v1
> ```
> 
> ---
> 
> ## `similarity_matches`
> 
> ```sql
> CREATE TABLE similarity_matches (
>     id INTEGER PRIMARY KEY AUTOINCREMENT,
>     file_id INTEGER NOT NULL,
>     similar_file_id INTEGER NOT NULL,
>     similarity_score REAL NOT NULL,
>     reason TEXT,
>     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
>     FOREIGN KEY(file_id) REFERENCES files(id),
>     FOREIGN KEY(similar_file_id) REFERENCES files(id)
> );
> ```
> 
> This lets the proposal engine say:
> 
> ```text
> Similar to 8 files Cody already approved into mom/care/legal evidence.
> ```
> 
> That’s the AI juice.
> 
> ---
> 
> # Add this pipeline phase
> 
> Current pipeline:
> 
> ```text
> scan
> extract signals
> score rules
> generate proposals
> review
> learn
> execute
> verify
> ```
> 
> Upgrade pipeline:
> 
> ```text
> 01 scan local fs
> 02 extract signals
> 03 extract entities
> 04 score rules
> 05 embed file memory cards
> 06 find similar approved examples
> 07 generate proposals
> 08 review
> 09 learn from decisions
> 10 suggest new rules
> 11 execute approved batch
> 12 verify
> ```
> 
> Important: vector/graph should feed proposals, not execute actions.
> 
> ---
> 
> # What gets stored where?
> 
> | Data | SQLite | Vector store | Graph |
> |---|---:|---:|---:|
> | File path | Yes | Metadata only | Maybe |
> | File hash | Yes | Metadata | No |
> | Events | Yes | No | Maybe important ones |
> | Human decisions | Yes | Metadata | Yes, as evidence |
> | Text preview | Yes | Embedded | Maybe |
> | Entities | Yes | Metadata | Yes |
> | Relationships | Yes | No | Yes |
> | Similarity | Yes | Yes | No |
> | Approvals | Yes | Metadata | Yes |
> 
> ---
> 
> # The smart behavior we actually want
> 
> ## Without vector
> 
> ```text
> bank_statement_june.txt
> → finance because filename says bank
> ```
> 
> Fine.
> 
> ## With vector
> 
> ```text
> IMG_9912.png
> → likely mom care legal evidence
> because OCR/text resembles 12 prior approved screenshots about care dispute
> ```
> 
> Now it’s useful.
> 
> ## With graph
> 
> ```text
> IMG_9912.png
> → connected to:
> - Mom
> - June 2026 hospitalization
> - Comfort Keepers dispute
> - medication issue
> - possible legal evidence timeline
> ```
> 
> Now it’s powerful.
> 
> ---
> 
> # My recommended order
> 
> Do this:
> 
> ## v0.3 — Safety patch first
> 
> No vector. No graph.
> 
> ```text
> lock execution
> dry-run
> path guards
> batch IDs
> collision protection
> scanner exclusions
> ```
> 
> ## v0.4 — Entity tables
> 
> Add:
> 
> ```text
> entities
> file_entities
> relationships
> ```
> 
> Still no vector DB.
> 
> Why? Because entities improve both graph and vector later.
> 
> ## v0.5 — Chroma vector memory
> 
> Add:
> 
> ```text
> embedding_index
> similarity_matches
> ChromaDB local store
> ```
> 
> Use embeddings only on:
> 
> ```text
> filename
> path
> text_preview
> detected entities
> human-approved destination
> human note
> ```
> 
> ## v0.6 — learned rule suggestions
> 
> Use repeated human corrections + vector similarity to suggest new fuzzy rules.
> 
> ## v0.7 — graph view/query
> 
> SQLite graph tables first.
> 
> Example queries:
> 
> ```text
> show all files connected to mom_care_june_2026
> show files tied to both finance and legal
> show all Hertz/Lyft dispute evidence
> ```
> 
> ## v1.0 — Supabase mirror
> 
> Mirror:
> 
> ```text
> files
> events
> entities
> relationships
> proposals
> decisions
> embedding_index
> ```
> 
> Then decide if pgvector or Neo4j earns a seat.
> 
> ---
> 
> # Final answer
> 
> Yes, a real AI file helper should have **vector memory** and eventually a **semantic graph**.
> 
> But the order is:
> 
> ```text
> 1. SQLite safety/audit spine
> 2. Entity extraction + relationship tables
> 3. Local vector store
> 4. Similarity-based proposal boosts
> 5. Learned rule suggestions
> 6. Supabase mirror
> 7. Optional Neo4j / pgvector when useful
> ```
> 
> Do **not** bolt Chroma or Neo4j onto an unsafe executor. That’s putting a rocket engine on a shopping cart.
> 
> First we make it safe.
> 
> Then we make it smart.

### User
> ok, well we need to go ahead and set that up im not waiting until later to have a half done app. and lets go ahead and use whatever databaselocally for speed but still able to migrate to supabase later.

### Assistant
> Agreed. We should not leave the “smart” layer as imaginary futureware. The move is: **SQLite stays the source ledger**, then we add **local Chroma vector memory** and **SQLite graph tables** now, with schema names that mirror cleanly into Supabase later.

### Assistant
> Yes. We set it up **now**, but we do it cleanly:
> 
> ```text id="mekoxw"
> Local relational DB: SQLite
> Local vector store: ChromaDB
> Local semantic graph: SQLite graph tables
> Future cloud mirror: Supabase Postgres + pgvector
> ```
> 
> That gives you speed locally, actual AI memory, and a clean migration path later. No half-done app. No “we’ll add intelligence someday” lie.
> 
> Your current `61_QiFileMaid` project already has the right basic skeleton: `app/local_review_ui.py`, configs, `data/qifilemaid.sqlite`, inventory/review outputs, scratch test files, and scripts for scan/signals/rules/proposals/decisions/execution/verification/learning. fileciteturn6file0 The current DB already includes proposals, human decisions, learned examples, batches, batch items, and sync logging, so we are extending the spine instead of ripping it out. fileciteturn5file3
> 
> One doctrine note: your blueprint is right that vector search and graphs are **derived systems**, not canonical truth. Canonical truth remains files, database records, repo docs, and designated operating pages. fileciteturn6file1 So vector/graph can advise; they do not get to boss the executor around.
> 
> ---
> 
> # Decision
> 
> ## Use this local stack
> 
> | Layer | Tool | Why |
> |---|---|---|
> | Ledger / audit / approvals | **SQLite** | Fast, local, reliable, easy to inspect |
> | Vector memory | **ChromaDB persistent local store** | Chroma supports persistent local storage with `PersistentClient`, so it fits this phase. citeturn267221search0 |
> | Embeddings | **Ollama `/api/embed`** | Local embeddings, private, no cloud dependency. Ollama’s current embedding endpoint is `/api/embed`. citeturn267221search19 |
> | Future vector cloud | **Supabase pgvector** | Supabase uses pgvector for storing/querying embeddings in Postgres. citeturn267221search1 |
> | Semantic graph | **SQLite edge tables now** | Migrates cleanly to Supabase relational tables later |
> | Future graph | **Supabase views first, Neo4j projection later** | Do not drag Neo4j into the app yet |
> 
> ---
> 
> # What we are adding now
> 
> ## New folders
> 
> ```text id="4aj3vi"
> 60_QiApps/61_QiFileMaid/
> ├── migrations
> │   ├── sqlite
> │   └── supabase
> ├── data
> │   ├── qifilemaid.sqlite
> │   └── vector
> │       └── chroma
> ├── scripts
> │   ├── 05_extract_entities.py
> │   ├── 05_embed_file_memory.py
> │   ├── 05_find_similar_files.py
> │   ├── 10_suggest_learned_rules.py
> │   └── 90_export_supabase_seed_sql.py
> └── config
>     ├── entities.yml
>     ├── vector.yml
>     └── graph_relationships.yml
> ```
> 
> ## New SQLite tables
> 
> ```text id="8a5rry"
> schema_migrations
> entities
> file_entities
> relationships
> embedding_index
> similarity_matches
> proposal_evidence
> suggested_learned_rules
> supabase_sync_queue
> ```
> 
> ## New Chroma collection
> 
> ```text id="9vrag9"
> qifilemaid_file_memory_v1
> ```
> 
> ---
> 
> # The important design choice
> 
> Keep local integer IDs, but add migration-safe public IDs.
> 
> SQLite can keep:
> 
> ```text id="bx3gy8"
> id INTEGER PRIMARY KEY AUTOINCREMENT
> ```
> 
> But every important table also needs:
> 
> ```text id="c4kdnf"
> uid TEXT UNIQUE NOT NULL
> ```
> 
> Why? Because Supabase/Postgres prefers UUID-style IDs, and integer local IDs will collide later.
> 
> So:
> 
> ```text id="j5bp31"
> SQLite local id = fast local joins
> uid = stable sync/migration identity
> ```
> 
> That is the bridge. Clean. Boring. Correct.
> 
> ---
> 
> # Copy/Paste Prompt For IDE / OpenCode
> 
> Use this as the next patch prompt:
> 
> ```text id="l6cj8k"
> Patch QiFileMaid to add the smart AI memory layer now, while keeping local-first speed and future Supabase migration compatibility.
> 
> Project path:
> 60_QiApps/61_QiFileMaid
> 
> Current app state:
> - Existing local DB: data/qifilemaid.sqlite
> - Existing scripts:
>   scripts/01_scan_local_fs.py
>   scripts/02_extract_signals.py
>   scripts/03_score_rules.py
>   scripts/04_generate_proposals.py
>   scripts/06_apply_human_decisions.py
>   scripts/07_execute_approved_batch.py
>   scripts/08_verify_batch.py
>   scripts/09_learn_from_decisions.py
>   scripts/db.py
> - Existing GUI:
>   app/local_review_ui.py
> - Existing config:
>   config/buckets.yml
>   config/naming_rules.yml
>   config/sensitive_patterns.yml
>   config/rules/01_bucket_rules.yml
> 
> Important:
> Do not touch real Drive.
> Do not add auto-execution.
> Do not let vector or graph logic execute file operations.
> Vector and graph layers may only improve proposals, explanations, similarity evidence, learned rule suggestions, and review context.
> 
> Architecture decision:
> - Keep SQLite as the local authoritative ledger.
> - Add ChromaDB as the local persistent vector store.
> - Add semantic graph tables inside SQLite.
> - Design all new tables so they can migrate cleanly to Supabase/Postgres later.
> - Add stable uid TEXT fields to new major tables.
> - Do not replace local integer IDs yet.
> - Do not add Supabase runtime sync yet.
> - Create Supabase-compatible SQL migration drafts only.
> 
> Required folders:
> - migrations/sqlite
> - migrations/supabase
> - data/vector/chroma
> - docs
> 
> Update requirements.txt:
> - chromadb
> - requests
> - pyyaml
> - python-dateutil
> 
> Use local Ollama embeddings through:
> POST http://localhost:11434/api/embed
> 
> Default embedding model in config/vector.yml:
> embeddinggemma
> 
> Also allow model override in config/vector.yml.
> 
> Create config/vector.yml:
> vector_store: chroma
> persist_dir: data/vector/chroma
> collection_name: qifilemaid_file_memory_v1
> embedding_provider: ollama
> embedding_model: embeddinggemma
> ollama_url: http://localhost:11434/api/embed
> embedding_text_version: file_memory_card_v1
> top_k_similar: 8
> minimum_similarity: 0.72
> 
> Create config/entities.yml:
> entity_types:
>   - person
>   - organization
>   - matter
>   - project
>   - account
>   - vehicle
>   - location
>   - system
>   - document_type
>   - topic
> 
> seed_entities:
>   - entity_type: person
>     canonical_name: mom
>     aliases: ["mother", "mom care"]
>   - entity_type: organization
>     canonical_name: hertz
>     aliases: ["hertz rental", "hertz lyft"]
>   - entity_type: organization
>     canonical_name: lyft
>     aliases: ["lyft express drive"]
>   - entity_type: organization
>     canonical_name: firefly
>     aliases: ["firefly iii", "firefly transactions"]
>   - entity_type: matter
>     canonical_name: mom_care_june_2026
>     aliases: ["mom care", "june 2026 hospitalization", "care dispute"]
>   - entity_type: matter
>     canonical_name: hertz_lyft_rental_dispute
>     aliases: ["rental dispute", "lyft rental", "hertz billing"]
> 
> Create config/graph_relationships.yml:
> relationship_types:
>   - mentions
>   - about
>   - evidence_for
>   - connected_to
>   - involved_in
>   - source_system_for
>   - belongs_to_matter
>   - care_subject
>   - finance_subject
>   - legal_subject
> 
> Patch scripts/db.py:
> 1. Enable PRAGMA foreign_keys = ON on every connection.
> 2. Enable WAL mode.
> 3. Add a schema_migrations table.
> 4. Add uid TEXT UNIQUE columns to new tables.
> 5. Do not drop existing data by default.
> 6. Keep drop_tables=True behavior only for scratch/test use.
> 7. Add indexes for:
>    - file_events(file_id)
>    - file_events(event_type)
>    - proposals(file_id)
>    - proposals(status)
>    - rule_matches(file_id)
>    - batch_items(batch_id)
>    - batch_items(file_id)
>    - file_entities(file_id)
>    - file_entities(entity_id)
>    - relationships(from_entity_id)
>    - relationships(to_entity_id)
>    - embedding_index(file_id)
>    - embedding_index(vector_id)
>    - similarity_matches(file_id)
> 
> Add SQLite migration:
> migrations/sqlite/002_ai_memory_graph_vector.sql
> 
> It must create:
> 
> schema_migrations:
> - version TEXT PRIMARY KEY
> - applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
> 
> entities:
> - id INTEGER PRIMARY KEY AUTOINCREMENT
> - uid TEXT UNIQUE NOT NULL
> - entity_type TEXT NOT NULL
> - canonical_name TEXT NOT NULL
> - aliases_json TEXT
> - description TEXT
> - created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
> - updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
> - UNIQUE(entity_type, canonical_name)
> 
> file_entities:
> - id INTEGER PRIMARY KEY AUTOINCREMENT
> - uid TEXT UNIQUE NOT NULL
> - file_id INTEGER NOT NULL
> - entity_id INTEGER NOT NULL
> - role TEXT
> - confidence INTEGER
> - source TEXT
> - evidence_text TEXT
> - created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
> - FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE
> - FOREIGN KEY(entity_id) REFERENCES entities(id) ON DELETE CASCADE
> - UNIQUE(file_id, entity_id, role)
> 
> relationships:
> - id INTEGER PRIMARY KEY AUTOINCREMENT
> - uid TEXT UNIQUE NOT NULL
> - from_entity_id INTEGER NOT NULL
> - to_entity_id INTEGER NOT NULL
> - relationship_type TEXT NOT NULL
> - confidence INTEGER
> - source TEXT
> - evidence_file_id INTEGER
> - evidence_text TEXT
> - metadata_json TEXT
> - created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
> - FOREIGN KEY(from_entity_id) REFERENCES entities(id)
> - FOREIGN KEY(to_entity_id) REFERENCES entities(id)
> - FOREIGN KEY(evidence_file_id) REFERENCES files(id)
> 
> embedding_index:
> - id INTEGER PRIMARY KEY AUTOINCREMENT
> - uid TEXT UNIQUE NOT NULL
> - file_id INTEGER NOT NULL
> - embedding_provider TEXT NOT NULL
> - embedding_model TEXT NOT NULL
> - vector_store TEXT NOT NULL
> - vector_collection TEXT NOT NULL
> - vector_id TEXT NOT NULL
> - embedded_text_hash TEXT
> - embedding_text_version TEXT
> - metadata_json TEXT
> - created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
> - updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
> - FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE
> - UNIQUE(file_id, embedding_model, embedding_text_version)
> 
> similarity_matches:
> - id INTEGER PRIMARY KEY AUTOINCREMENT
> - uid TEXT UNIQUE NOT NULL
> - file_id INTEGER NOT NULL
> - similar_file_id INTEGER NOT NULL
> - similarity_score REAL NOT NULL
> - reason TEXT
> - source TEXT
> - created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
> - FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE
> - FOREIGN KEY(similar_file_id) REFERENCES files(id) ON DELETE CASCADE
> - UNIQUE(file_id, similar_file_id, source)
> 
> proposal_evidence:
> - id INTEGER PRIMARY KEY AUTOINCREMENT
> - uid TEXT UNIQUE NOT NULL
> - proposal_id INTEGER NOT NULL
> - evidence_type TEXT NOT NULL
> - evidence_label TEXT
> - evidence_value TEXT
> - score REAL
> - metadata_json TEXT
> - created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
> - FOREIGN KEY(proposal_id) REFERENCES proposals(id) ON DELETE CASCADE
> 
> suggested_learned_rules:
> - id INTEGER PRIMARY KEY AUTOINCREMENT
> - uid TEXT UNIQUE NOT NULL
> - rule_name TEXT NOT NULL
> - suggested_rule_json TEXT NOT NULL
> - support_count INTEGER DEFAULT 0
> - estimated_accuracy REAL
> - status TEXT DEFAULT 'PENDING_REVIEW'
> - created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
> - reviewed_at TIMESTAMP
> - human_note TEXT
> 
> supabase_sync_queue:
> - id INTEGER PRIMARY KEY AUTOINCREMENT
> - uid TEXT UNIQUE NOT NULL
> - table_name TEXT NOT NULL
> - record_uid TEXT NOT NULL
> - operation TEXT NOT NULL
> - payload_json TEXT
> - status TEXT DEFAULT 'PENDING'
> - created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
> - synced_at TIMESTAMP
> - error_message TEXT
> 
> Create Supabase migration draft:
> migrations/supabase/002_ai_memory_graph_vector.sql
> 
> It should be Postgres-compatible:
> - use uuid primary keys where appropriate
> - use gen_random_uuid()
> - use jsonb instead of TEXT for JSON fields
> - include create extension if not exists vector;
> - include vector-compatible placeholders but do not require actual embedding dimension yet unless config provides one
> - mirror entities, file_entities, relationships, embedding_index, similarity_matches, proposal_evidence, suggested_learned_rules, supabase_sync_queue
> 
> Add script:
> scripts/05_extract_entities.py
> 
> Behavior:
> - Read files and file_signals.
> - Load config/entities.yml and config/sensitive_patterns.yml.
> - Match canonical names and aliases against:
>   current_name
>   current_path
>   filename_tokens
>   path_tokens
>   text_preview
>   sensitivity_flags
> - Upsert entities from seed config.
> - Insert file_entities rows with role and confidence.
> - Suggested role mapping:
>   mom + care/medical terms = care_subject
>   hertz/lyft + finance/dispute terms = finance_subject or legal_subject
>   firefly + transaction/export terms = source_system
>   legal sensitive terms = legal_subject
> - Insert file_events:
>   ENTITY_EXTRACTED
> - No file modifications.
> 
> Add script:
> scripts/05_embed_file_memory.py
> 
> Behavior:
> - Build a file memory card for each file with signals.
> - Include:
>   file_id
>   current_name
>   current_path
>   extension
>   detected_date
>   detected_entity
>   detected_domain
>   sensitivity_flags
>   text_preview
>   top rule matches
>   current proposal if any
>   human decision if any
>   file_entities if any
> - Hash the memory card text.
> - Skip if embedding_index already has same file_id + model + embedding_text_version + hash.
> - Call Ollama /api/embed.
> - Upsert into ChromaDB PersistentClient at data/vector/chroma.
> - Collection: qifilemaid_file_memory_v1.
> - Store metadata:
>   file_id
>   file_uid if available
>   current_name
>   current_path
>   sensitivity_flags
>   detected_domain
>   proposed_bucket
>   approved_bucket
>   status
> - Insert/update embedding_index.
> - Insert file_events:
>   EMBEDDING_CREATED
>   EMBEDDING_SKIPPED_UNCHANGED
> - No file modifications.
> 
> Add script:
> scripts/05_find_similar_files.py
> 
> Behavior:
> - For each embedded file, query Chroma for top_k similar.
> - Exclude self.
> - Prefer prior human-approved/corrected files as stronger examples.
> - Write similarity_matches rows.
> - Write proposal_evidence rows for pending proposals:
>   evidence_type = vector_similarity
>   evidence_label = similar approved files
>   evidence_value = concise summary
>   score = max similarity
> - Insert file_events:
>   SIMILARITY_MATCHED
> - No file modifications.
> 
> Patch scripts/04_generate_proposals.py:
> - Use rule scores as before.
> - Add boost from similarity_matches when similar files have approved/corrected human decisions.
> - Add graph/entity context from file_entities.
> - Insert proposal_evidence rows explaining:
>   rule_match
>   sensitivity_flag
>   entity_match
>   vector_similarity
> - Do not allow vector similarity to override sensitive review gates.
> - Do not auto-execute anything.
> 
> Patch scripts/09_learn_from_decisions.py:
> - Use human_decisions + similarity_matches + file_entities.
> - Generate suggested_learned_rules when at least 3 similar corrections point to the same target bucket/subfolder.
> - Insert into suggested_learned_rules with status PENDING_REVIEW.
> - Do not write permanent YAML rules automatically.
> - Insert file_events:
>   LEARNED_RULE_SUGGESTED
> 
> Patch app/local_review_ui.py:
> - Add display sections to review card:
>   Entities detected
>   Similar prior files
>   Proposal evidence
> - Do not add execution power.
> - Keep execution locked unless previous safety patch is fully implemented.
> - The UI can show "Smart Context Available" if vector/entity evidence exists.
> - Use sys.executable instead of hardcoded python in subprocess calls.
> 
> Update README.md:
> - Explain the local-first AI memory architecture:
>   SQLite = ledger
>   Chroma = vector similarity memory
>   SQLite graph tables = semantic relationships
>   Supabase later = cloud mirror / pgvector
> - Explain that vector and graph are advisors, not truth.
> - Explain the pipeline:
>   01 scan
>   02 extract signals
>   05 extract entities
>   03 score rules
>   04 generate proposals
>   05 embed file memory
>   05 find similar files
>   06 review/decisions
>   09 learn from decisions
>   10 suggest learned rules
>   07 execute only after safety gates
>   08 verify
> 
> Add tests:
> - test_entity_seed_insert
> - test_file_entity_detection_mom_care
> - test_file_entity_detection_hertz_lyft
> - test_memory_card_hash_stable
> - test_embedding_skips_unchanged_file
> - test_similarity_excludes_self
> - test_similarity_boost_does_not_auto_execute
> - test_suggested_rule_requires_review
> - test_supabase_migration_sql_exists
> - test_vector_store_files_are_not_scanned
> 
> Do not implement cloud Supabase sync yet.
> Do not implement Neo4j yet.
> Do not implement real file execution.
> Do not move, rename, delete, or archive any files.
> ```
> 
> ---
> 
> # Pipeline after this patch
> 
> Your new working order becomes:
> 
> ```text id="odxr1e"
> 1. Scan filesystem
> 2. Extract signals
> 3. Extract entities
> 4. Score rules
> 5. Generate first proposals
> 6. Embed file memory cards
> 7. Find similar files
> 8. Regenerate enhanced proposals
> 9. Human review
> 10. Learn from decisions
> 11. Suggest learned rules
> 12. Execute only after safety gates
> ```
> 
> Yes, proposal generation happens twice in early versions. That is normal: first pass creates structure, second pass uses similarity evidence.
> 
> ---
> 
> # Why Chroma + SQLite instead of only one DB?
> 
> Because each has a job.
> 
> ## SQLite
> 
> ```text id="lm8p76"
> facts
> events
> approvals
> batches
> entities
> relationships
> audit trail
> Supabase migration path
> ```
> 
> ## Chroma
> 
> ```text id="shn9ja"
> semantic similarity
> nearest approved examples
> fuzzy memory
> "this looks like that"
> ```
> 
> ## Supabase later
> 
> ```text id="j9hxou"
> shared dashboard
> phone review
> central reporting
> pgvector
> QiAccess integration
> ```
> 
> Supabase can store vectors using pgvector later, but locally Chroma gets you smart search without waiting on cloud setup. Supabase’s vector docs explicitly support pgvector for embeddings, so the migration path is real, not imaginary. citeturn267221search1
> 
> ---
> 
> # Important safety rule
> 
> Even after this patch:
> 
> ```text id="8sm2la"
> Vector confidence cannot execute.
> Graph confidence cannot execute.
> Rule confidence cannot execute.
> Only approved batch items can execute.
> ```
> 
> AI can say:
> 
> > “This looks like Mom care legal evidence.”
> 
> It cannot say:
> 
> > “I moved it for you.”
> 
> No ma’am. Not until the executor safety patch is done.
> 
> ---
> 
> # My exact recommendation
> 
> Tell the IDE to do **two patches**, in this order:
> 
> ## Patch A — Safety lock
> 
> Executor hardening, dry-run, batch ID, path guards.
> 
> ## Patch B — Smart memory
> 
> SQLite graph + Chroma vectors + entity extraction + similarity evidence.
> 
> But since you don’t want a half-done app, it is fine to tell it to prepare both now. Just require:
> 
> ```text id="qteg06"
> Execution remains locked until safety tests pass.
> ```
> 
> That gives you a complete brain without handing it a loaded chainsaw.
