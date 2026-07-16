---
layout: page
title: "Cursor file renaming prompt"
slug: "cursor_file_renaming_prompt"
created_at: "2025-09-09 17:06:55"
updated_at: "2025-09-09 17:06:55"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-000.json"
template_key: master-template
date: 2025-09-09
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "68c0a4de-df38-8332-bd67-0a91f83a7c43"
canonical_ref: ""
---

# Cursor file renaming prompt

## Overview
- **Date**: 2025-09-09 17:06:55
- **Conversation ID**: `68c0a4de-df38-8332-bd67-0a91f83a7c43`
- **Source**: `Chat-Export-28513-2026/conversations-000.json`

## Chat History

### User
> give me a promopt for cursor to go thorugh and read every file inside the financial , forms, and notes folders and rename the files to something short and descriptive.

### Assistant
> Here’s a clean Cursor prompt you can drop in. It’ll walk through the **financial**, **forms**, and **notes** folders, read each file, and then rename them into something short and descriptive based on the content:
> 
> ```bash
> # Cursor Prompt:
> Go into the project root and recursively scan the following folders:
> - ./financial
> - ./forms
> - ./notes
> 
> For every file inside these folders:
> 1. Open and read the file contents.
> 2. Infer the main subject or purpose of the file (e.g., "bank_statement_Jan2025.pdf", "I-589_asylum_draft.docx", "client_meeting_notes.txt").
> 3. Generate a new, short, descriptive filename in lowercase with underscores.  
>    - Keep it under ~30 characters.  
>    - Use keywords that describe the file content.  
>    - Preserve the original file extension.  
>    - Example: "bank_statement.pdf" instead of "document_1.pdf".
> 4. Rename the file with the new descriptive name.  
> 5. Output a CSV rename map with two columns: `old_path,new_path`.
> 
> At the end, confirm all changes and ensure no duplicate names exist.
> ```
> 
> Would you like me to also make it **undo-friendly** (so Cursor creates a backup or keeps the rename map ready to reverse everything if needed)?

### User
> now i want it to review everything we have make sure the document file names are correct and make corrections where needed update the checklist accordingly and next steps of what needs to be done like for one preping the taxes.

### Assistant
> Got you, Q. Here’s a single drop-in **Cursor prompt** that audits the whole repo, fixes file names, updates the checklist, and spits out concrete next steps (incl. tax prep). It’s undo-safe and receipt-ready.
> 
> ```bash
> # CURSOR PROMPT — Repo Audit + Rename + Checklist + Next Steps (UNDO-SAFE)
> 
> You are an engineering ops auditor. Work from the project root.
> 
> SCOPE
> - Include: ./financial, ./forms, ./notes, plus any ./checklists or ./docs
> - Process files recursively. Skip node_modules, .git, build/dist, .DS_Store, tmp.
> 
> OBJECTIVES (in order)
> 1) AUDIT: Read every file; extract topic, date(s), parties, doc type.
> 2) VALIDATE/RENAME: Ensure filenames are short, descriptive, and consistent. Fix where needed.
> 3) CHECKLIST: Update project checklist with completed items + new tasks from findings.
> 4) NEXT STEPS: Generate prioritized action plan (incl. “prep taxes” track).
> 5) SAFETY: Produce undo map and make a timestamped backup before renames.
> 
> NAMING STANDARD
> - Format: <topic>_<qualifier>[_yyyy-mm-dd][_vN].<ext>
> - Lowercase, words separated by underscores, max ~32 chars base name.
> - Preserve extension. Remove spaces, emojis, random numbers.
> - Examples:
>   - bank_chase_stmt_2025-01.pdf
>   - uscis_i-589_draft_v2.docx
>   - client_meeting_notes_2025-09-01.md
>   - w2_2024_employername.pdf
> - If exact date not clear:
>   - Prefer document date inside file; else filename; else parent folder; else omit date.
> - Topic lexicon (use if detected):
>   - financial/: bank_stmt, credit_stmt, invoice, receipt, budget, w2, 1099, 1040, schedule_c, ledger, qbo_export
>   - forms/: uscis_i-589, uscis_i-765, g-28, affidavit, declaration, cover_letter, index
>   - notes/: meeting_notes, call_notes, research, todo
> - Parties: normalize common orgs: irs, uscis, ssa, dmv, chase, boa, capitalone, starbucks, etc.
> - Avoid duplicates: if collision, append _v2, _v3… keeping date stable.
> 
> RENAMING RULES
> - Keep semantic meaning; don’t hallucinate. Prefer conservative terms when unsure.
> - Strip leading numbering unless it encodes order that matters. If order matters in a sequence, convert to suffix _01, _02…
> - Normalize months to yyyy-mm-dd (ISO).
> - Redact PII from filenames (e.g., full SSN). Keep last4 if essential: _xxx1234.
> 
> OUTPUT ARTIFACTS (write to ./_audit_out/)
> - rename_map.csv         # old_path,new_path
> - rename_collisions.csv  # collisions resolved with chosen name
> - audit_findings.md      # issues, warnings, rationale for renames
> - checklist.md           # updated checklist with [ ] / [x]
> - next_steps.md          # prioritized action plan with owners/durations
> - index_of_docs.csv      # path, title, date, parties, doc_type, summary
> - backup/                # timestamped copy of files BEFORE renames
> 
> CHECKLIST LOGIC
> - Create/merge ./_audit_out/checklist.md with sections:
>   - [x] File audit completed (date)
>   - [x] Naming normalized to standard (date)
>   - [ ] Tax Prep – Gather year docs (W-2/1099/1098, receipts, bank stmts)
>   - [ ] Tax Prep – Reconcile accounts (bank/credit vs ledger)
>   - [ ] Tax Prep – Draft Schedule C (if applicable)
>   - [ ] USCIS Packet – Verify form versions/current editions
>   - [ ] USCIS Packet – Cross-check declaration vs exhibits
>   - [ ] Financial – Budget snapshot & cashflow 90d
>   - [ ] Notes – Convert action items to tasks
> - Auto-tick items you complete. Add new items you infer from the audit.
> - For each task add: `- Est: <minutes>  Owner: <role>  Blockers: <if any>`
> 
> NEXT STEPS TEMPLATE (populate in ./_audit_out/next_steps.md)
> - Tier 1 (Bare fix; next 24–48h):
>   1) **Prep Taxes – Gather Source Docs**  
>      - Pull W-2/1099/1098, bank/credit statements, big receipts  
>      - Est: 120m  Owner: Finance  Output: /financial/taxes/<year>/source_docs/
>   2) **Reconcile Accounts (Last 3 Months)**  
>      - Compare statements vs ledger; flag mismatches  
>      - Est: 180m  Owner: Finance  Output: reconciliation_YYYY-Q#.xlsx
>   3) **USCIS Forms Version Check**  
>      - Confirm editions on I-589, I-765, G-28; update if outdated  
>      - Est: 60m  Owner: Forms
>   4) **Notes → Tasks Migration**  
>      - Parse notes for actionables; append to checklist.md  
>      - Est: 45m  Owner: Ops
> 
> - Tier 2 (Upgrade/future-proof; 1–2 weeks):
>   1) Document dates auto-parser + validator
>   2) Entity normalization dictionary (irs/uscis/banks/vendors)
>   3) Monthly “closing kit” generator (zip + index)
>   4) Dedupe & near-duplicate detector (hash + fuzzy)
> 
> AUDIT & CORRECTION WORKFLOW
> 1) DRY RUN
>    - Simulate renames; generate all reports without touching files.
>    - Show a diff summary and example mappings in audit_findings.md.
> 2) BACKUP
>    - Create ./_audit_out/backup/<timestamp>/ with original tree.
> 3) RENAME
>    - Apply renames safely using rename_map.csv. Prevent overwrites.
> 4) VALIDATE
>    - Re-scan for any out-of-policy filenames; fix & append to rename_map.csv.
> 5) CHECKLIST & PLANS
>    - Update checklist.md and next_steps.md based on actual findings.
> 
> TECHNICAL DETAILS
> - CSVs should be UTF-8, headers present.
> - Keep paths relative to repo root.
> - If a file is binary and unreadable, infer from context (parent folder, extension, exif for images/pdfs if available).
> - For PDFs: attempt first-page text extraction (title/date).
> - For DOCX: read core properties + first ~2 pages of text.
> - For images: detect if it’s receipt/invoice/photo via OCR keywords when possible.
> 
> UNDO / ROLLBACK
> - Use rename_map.csv to reverse changes: swap columns and reapply.
> - Provide a one-liner rollback command in audit_findings.md.
> 
> DELIVERABLES & ACCEPTANCE
> - All artifacts written under ./_audit_out/ with a timestamp in the first line.
> - No filename policy violations remain in target folders.
> - No collisions or, if unavoidable, documented in rename_collisions.csv.
> - Checklist and next_steps clearly actionable today.
> 
> EXECUTION FLAGS
> - Default: DRY_RUN=true. After presenting summary, proceed to BACKUP+RENAME automatically unless fatal errors present.
> - Flags you may expose at top of audit_findings.md:
>   - DRY_RUN: true/false
>   - MAX_NAME_LEN: 32
>   - DATE_FALLBACK: omit|folder|mtime
>   - COLLISION_STRATEGY: increment_version|append_suffix
> 
> BEGIN.
> ```
> 
> Want me to generate a **starter checklist.md** and **next_steps.md** skeletons right now so you can drop them in and go?

### User
> can you make a simple binder cover for my clients binder book, this we will house her immigration case. financials, taxes, ect.

### Assistant
> Here’s a clean, simple binder cover for your client’s binder book:  
> 
> 📂 [Download client_binder_cover.pdf](sandbox:/mnt/data/client_binder_cover.pdf)  
> 
> It has a centered title, a subtitle noting “Immigration Case • Financials • Taxes • Notes,” and today’s date. Do you want me to also design matching **section dividers** (Immigration, Financials, Taxes, Notes) so the whole binder has a consistent look?

### User
> what is the height and width of a binder spine

### Assistant
> Binder spines are sneaky little rectangles—shorter than the cover height and with widths that depend on how many trees’ worth of paper you’re cramming in.  
> 
> **Standard U.S. binder dimensions (based on letter-size, 11" paper height):**  
> - **Height:** The spine is the same as the cover height, about **11.5 inches** (to cover 11" paper + margin).  
> - **Width (the variable part):**  
>   - 0.5" spine → holds ~100 sheets  
>   - 1" spine → ~200 sheets  
>   - 1.5" spine → ~300 sheets  
>   - 2" spine → ~400 sheets  
>   - 3" spine → ~600 sheets  
>   - 4" spine → ~800 sheets  
> 
> So when you make spine labels, the safe print area is **11" tall by [spine width] wide**, where the width is 0.5"–4" depending on the binder. Most label templates (like Avery) are slightly shorter, about **10.75" tall**, so they slide into the plastic sleeve without wrinkling.  
> 
> Do you want me to spin you up a **template PDF for spine labels** in a few common widths so you can just print, cut, and slide them in?

### User
> in pixels

### Assistant
> Alright, let’s switch from inches to pixels. The trick is that it depends on the **DPI (dots per inch)** setting you’re printing at. Most office printers default to **300 DPI** (high quality) or **150 DPI** (draft).  
> 
> Here’s the math:  
> - **Height:** 11" × 300 DPI = **3300 px** tall  
> - **Width:** spine size in inches × 300 DPI  
> 
> So for common spines at **300 DPI**:  
> - 0.5" spine → 150 px wide × 3300 px tall  
> - 1" spine → 300 px wide × 3300 px tall  
> - 1.5" spine → 450 px wide × 3300 px tall  
> - 2" spine → 600 px wide × 3300 px tall  
> - 3" spine → 900 px wide × 3300 px tall  
> - 4" spine → 1200 px wide × 3300 px tall  
> 
> If you go **150 DPI** (still okay for labels): just cut those numbers in half.  
> 
> 👉 So the safe design area for most binders is somewhere between **150–1200 px wide** and **3300 px tall**, depending on spine thickness.  
> 
> Do you want me to generate you a **ready-to-print PDF spine label template** (say 1", 2", and 3" widths) with guides so you can just drop in text/graphics?
