---
layout: page
title: "Immigration intake organization"
slug: "immigration_intake_organization"
created_at: "2025-09-19 21:56:09"
updated_at: "2026-07-16T06:49:28-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-000.json"
template_key: master-template
date: 2025-09-19
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "68ce17ad-ec68-8323-b140-6fc3d4f77b0c"
canonical_ref: ""
---

# Immigration intake organization

## Overview
- **Date**: 2025-09-19 21:56:09
- **Conversation ID**: `68ce17ad-ec68-8323-b140-6fc3d4f77b0c`
- **Source**: `Chat-Export-28513-2026/conversations-000.json`

## Chat History

### User
> what would be good front matter to organize a clients immigrations intake, forms, and evidence in a very simple intutitive way for obsidian.

### Assistant
> For a client immigration intake in Obsidian, the goal is clarity and quick navigation — you want to glance at the front matter and know exactly what’s inside without digging. Here’s a clean, intuitive template you can use as YAML front matter at the top of each note or folder index:
> 
> ```yaml
> ---
> client: "John Doe"
> case_type: "Asylum" # or SIV, TPS, Adjustment of Status, etc.
> case_status: "In Progress" # Drafted, Filed, Pending, Approved, Denied
> priority: "High" # High / Medium / Low
> country_of_origin: "Afghanistan"
> uscis_case_numbers:
>   - "EAC1234567890"
> a_number: "A###-###-###"
> key_dates:
>   intake_date: 2025-09-19
>   filing_deadline: 2025-12-15
>   interview_date: null
> attorney: "Jane Smith, Esq."
> forms:
>   completed:
>     - "I-589"
>     - "G-28"
>   pending:
>     - "I-765"
> evidence_categories:
>   identity: true
>   persecution: true
>   country_conditions: true
>   character_references: false
> notes: |
>   Brief summary of case facts or special considerations.
> tags:
>   - immigration
>   - client-intake
>   - asylum
> cssclass: immigration-case
> ---
> ```
> 
> ### Why This Works
> - **Top-level identifiers** (`client`, `case_type`, `case_status`) make the note instantly recognizable in search or Dataview queries.
> - **Dates are structured** so you can sort/filter timelines or set reminders.
> - **Forms section** lets you track what’s done vs. pending without flipping through multiple files.
> - **Evidence categories** act like a checklist (identity docs, country reports, affidavits, etc.).
> - **Notes field** is free text for quirks, red flags, or to-dos.
> - **Tags + cssclass** make it easy to group cases visually in Obsidian and power dashboards.
> 
> You can even use [Dataview](https://blacksmithgu.github.io/obsidian-dataview/) to query all open cases with a deadline coming up, or list all cases missing “character references.” This is where it gets powerful — your vault becomes a live dashboard.
> 
> Want me to mock up a sample Dataview table that pulls all clients, deadlines, and case status into a single dashboard note? That would turn this into an actual control panel for your immigration work.

### User
> that is way too much lets keep it concise and simple.

### Assistant
> Got it — let’s keep it lean and still useful. Here’s a **minimal front matter template** that will make Obsidian powerful without feeling heavy:
> 
> ```yaml
> ---
> client: "John Doe"
> case: "Asylum"   # or SIV, TPS, Green Card, etc.
> status: "Pending"  # Intake, Filed, Approved, Denied
> a_number: "A###-###-###"
> deadline: 2025-12-15
> forms: ["I-589", "G-28"]
> tags: [immigration, client]
> ---
> ```
> 
> ### Why This Stays Simple
> - **Five fields only:** client, case type, status, A-number, deadline. You can instantly filter or query by any of these.
> - **Forms as a short array:** track what’s relevant without over-documenting.
> - **Tags:** make everything searchable and groupable in Obsidian.
> 
> This is lightweight enough to put on *every* intake, form, or evidence note.  
> For evidence, you might just swap `forms` for `evidence_type: "Identity Document"` or `"Country Condition"` — still following the same pattern.
> 
> Would you like me to show you a one-line Dataview query that turns this into a quick dashboard of all clients and deadlines? That would give you a live case overview page with zero extra work.

### User
> ok, i think we need to know if petitioner, beneficiary, or joint.

### Assistant
> Exactly — that’s a small but crucial distinction. Here’s the updated, still-minimal version with a **role field** added:  
> 
> ```yaml
> ---
> client: "John Doe"
> role: "Petitioner"   # Petitioner | Beneficiary | Joint
> case: "Asylum"       # or SIV, TPS, Green Card, etc.
> status: "Pending"    # Intake, Filed, Approved, Denied
> a_number: "A###-###-###"
> deadline: 2025-12-15
> forms: ["I-589", "G-28"]
> tags: [immigration, client]
> ---
> ```
> 
> ### Why This Works
> - **role** keeps context straight — critical if you’re tracking multiple people on the same case (like spouse/child derivatives or joint sponsors).  
> - Everything is still readable at a glance, short enough to not feel like a database.  
> - Works great with Dataview or search filters (e.g., show all Beneficiaries with upcoming deadlines).  
> 
> Would you like me to show you how to set up a Dataview table that groups clients by `role` automatically? That could make it super clear who’s filing vs. who’s attached to a case.

### User
> improve this prompt. ok now that this is done, OK Now that you have the rules in place and we're ready to roceed, this is what I want you to do next. I want you to recursively walk the directory, take an inventory of each file and folder where they're at. Then, using OCR I want you to go back and read each document so you understand the purpose of the document. If it's in PDF, you can use a temporary folder to convert to jpegs. To read them, you probably only need to do one or 2 pages, maybe one page. And then once you fully understand the context and the purpose of each document. I want you to go back and make sure that they are documented correctly, they are named correctly, and they're in the correct spot. But before you do any changes or movements, you're going to create a movement LAN. You're going to show it where it is now, what it is now, the new name is going to be. If needed. Then in addition to that. Umm, once that's approved and you make those moves, you're going to doublecheck that work to make sure that it is correct in the correct SOT so I can move forward and then with that context. We will then extract. The filled data from the forms, specifically the tax forms. And the identity documents and what I mean by that is I want to extract the details and get a master jason file that has the field and the field values that we can use to reference later.

### Assistant
> Here’s a tightened, sharper version of your prompt — same instructions, but structured so an AI (or a person following it) can execute step by step without confusion:  
> 
> ---
> 
> **Improved Prompt:**  
> 
> Now that the rules are in place and we’re ready to proceed, here’s what I want you to do next:  
> 
> 1. **Recursive Inventory**  
>    - Walk the entire directory structure and create a complete inventory of every file and folder.  
>    - Record each item’s current path and name.  
> 
> 2. **Context Analysis (OCR)**  
>    - For each document, use OCR to read enough pages (1–2 is fine) to understand its content and purpose.  
>    - For PDFs, temporarily convert to images (e.g., JPEG) if needed for OCR.  
>    - Capture a short summary of the document’s purpose.  
> 
> 3. **Audit & Proposed Plan**  
>    - Based on the inventory and analysis, check whether each file:  
>      - Is correctly named  
>      - Is in the correct location  
>      - Matches its intended purpose  
>    - Before making any changes, generate a **Movement Plan** that lists for each file:  
>      - Current location and name  
>      - Proposed new location and/or name  
>    - Present the plan for approval before moving or renaming anything.  
> 
> 4. **Execution & Verification**  
>    - Once approved, apply the moves and renames exactly as listed.  
>    - Double-check your work to confirm all files are in the correct place and match the source of truth (SOT).  
> 
> 5. **Data Extraction**  
>    - From the finalized documents, extract key field data from tax forms and identity documents.  
>    - Output a **master JSON file** with `{field: value}` pairs for each extracted item, creating a structured reference dataset we can use later.  
> 
> ---
> 
> This rewrite makes your intent unmissable: first inventory, then understand, then propose, then execute, then extract data. It also uses clear deliverables (inventory, plan, JSON) so there’s a “receipt” for every step.  
> 
> Would you like me to rephrase this into **Cursor-friendly step-by-step prompts** so you could drop them into an agent or script as an automated workflow? That could make this actionable right away.

### User
> yes, cursor friendly and in the most efficient way possible, essentially everything we need is basically already here and I want to get this file as close to done as possible by justr using cursor ai.

### Assistant
> Perfect — let’s turn that big idea into a **Cursor-ready workflow** that’s efficient and step-driven. Here’s how you could drop it into Cursor as a series of prompts or a single orchestrator task:
> 
> ---
> 
> ### **Cursor-Friendly, Streamlined Prompt**
> 
> ```text
> You are an expert file auditor and document organizer. Follow these steps carefully:
> 
> 1. **Inventory & Map**
>    - Recursively walk the entire target directory.
>    - Output a JSON inventory with each file’s current path, name, and file type.
> 
> 2. **Context Understanding (OCR)**
>    - For each file, read enough content (1–2 pages max) to identify its purpose.
>    - Use OCR for PDFs (convert to images temporarily if needed).
>    - Output a short summary for each file in the JSON inventory under `summary`.
> 
> 3. **Movement Plan**
>    - Propose a movement plan but **do not make changes yet**.
>    - For each file, specify:
>        - `current_path`
>        - `current_name`
>        - `proposed_path` (if moving)
>        - `proposed_name` (if renaming)
>        - `reason` (why it should move or stay)
>    - Return this plan for human review.
> 
> 4. **Apply & Verify**
>    - Once the plan is approved, rename/move files as proposed.
>    - Re-run the inventory to confirm the new structure matches the approved plan.
> 
> 5. **Data Extraction**
>    - For all finalized files:
>        - Extract structured data from tax forms (e.g. name, SSN, amounts, year).
>        - Extract data from identity documents (name, DOB, passport numbers, etc.).
>    - Compile a single `master.json` containing `{field: value}` pairs for all clients/cases.
> 
> Your outputs must be clean, machine-readable JSON at every stage, so they can be reviewed and approved before you proceed to the next step.
> ```
> 
> ---
> 
> ### Why This is Efficient
> - **Atomic steps:** Inventory → Analyze → Plan → Execute → Extract. Each is reviewable.
> - **JSON-first approach:** Perfect for Cursor to keep context structured between steps.
> - **Minimal OCR load:** Only reads enough to classify documents, not full-text everything.
> - **Built-in safety check:** You never touch or rename anything until the plan is explicitly approved.
> - **Final deliverable:** A master JSON dataset you can use downstream for automations.
> 
> ---
> 
> Would you like me to break this into **sequential Cursor commands** (so you can literally copy/paste them one at a time and keep context between steps), or keep it as one “master” orchestrator prompt that does everything in one chain? The first option gives you full control at each stage, the second is more hands-off and faster.

### User
> sequential commands but just tell it to review, double check, then report it plan for approval then execute then double check and report back before proceeding or something.

### Assistant
> Got it — let’s make this **step-by-step Cursor commands**, each one crisp and review-safe. Here’s a clean sequence you can literally drop into Cursor one at a time:  
> 
> ---
> 
> ### **Step 1 — Inventory**
> ```text
> Recursively walk the target directory.  
> Return a JSON inventory listing:
> - current_path
> - file_name
> - file_type (pdf, docx, image, etc.)
> 
> Do not modify anything. This is just discovery.
> ```
> 
> ---
> 
> ### **Step 2 — Context Review (OCR)**
> ```text
> For each file in the inventory:
> - If it’s a document, read 1–2 pages (use OCR for PDFs).
> - Summarize the purpose of the file in a `summary` field.
> Return a new JSON inventory including these summaries.
> 
> Do not move or rename anything yet.
> ```
> 
> ---
> 
> ### **Step 3 — Movement Plan (Proposal)**
> ```text
> Using the reviewed inventory, create a movement plan in JSON:
> - current_path
> - current_name
> - proposed_path (if different)
> - proposed_name (if different)
> - reason (why this move/rename is proposed)
> 
> Double-check the plan for errors or conflicts.  
> Return the plan for human approval before proceeding.
> Do not execute changes yet.
> ```
> 
> ---
> 
> ### **Step 4 — Execute & Verify**
> ```text
> Once the movement plan is approved:
> - Apply all proposed moves/renames.
> - Re-run the inventory.
> - Double-check that the final file structure matches the approved plan exactly.
> Return a verification report before continuing.
> ```
> 
> ---
> 
> ### **Step 5 — Data Extraction**
> ```text
> From the verified, final file set:
> - Extract structured data from tax forms (year, name, SSN, totals).
> - Extract data from identity documents (name, DOB, passport/ID numbers).
> Return a single `master.json` with key-value pairs for all extracted fields.
> 
> Double-check data consistency before finalizing.
> ```
> 
> ---
> 
> ### Why This Works
> - **Review gate at every step:** Cursor stops and shows you what it found, so you can approve before anything moves.
> - **Safety built-in:** No renames or moves happen until you say so.
> - **Post-execution verification:** Ensures no files were misplaced before extracting data.
> - **Final JSON deliverable:** Clean, ready to feed into any app or KB system.  
> 
> ---
> 
> Want me to include **short, explicit confirmations** for Cursor to give after each step (like “✅ Inventory complete — ready for review”)? This makes it easier to keep track of progress when you’re running it interactively.

### User
> can i paste them all now or do i just do one at a time.

### Assistant
> Do them **one at a time** — Cursor works best when each step finishes, you review the output, and then you paste the next one.  
> 
> Here’s the tightened sequence with built-in **review checkpoints** baked in so it pauses for your approval before moving on:
> 
> ---
> 
> ### **Step 1 — Inventory**
> ```text
> Recursively walk the target directory.
> Return a JSON inventory of all files and folders with:
> - current_path
> - file_name
> - file_type
> 
> Do not modify anything. Confirm back with:
> "✅ Inventory complete — ready for review."
> ```
> 
> ---
> 
> ### **Step 2 — Context Review (OCR)**
> ```text
> For each file in the inventory:
> - Read 1–2 pages (use OCR for PDFs).
> - Add a `summary` field to the JSON explaining the file’s purpose.
> 
> Return the updated JSON and confirm back with:
> "✅ Context review complete — ready for review."
> Do not rename or move anything yet.
> ```
> 
> ---
> 
> ### **Step 3 — Movement Plan**
> ```text
> Using the inventory + summaries:
> - Propose a movement plan with:
>   - current_path
>   - current_name
>   - proposed_path (if moving)
>   - proposed_name (if renaming)
>   - reason
> 
> Double-check for conflicts or errors.
> Return the plan and confirm with:
> "📋 Movement plan ready — review required before execution."
> Do not execute changes yet.
> ```
> 
> ---
> 
> ### **Step 4 — Execute & Verify**
> ```text
> After plan is approved:
> - Apply moves/renames as proposed.
> - Re-run inventory.
> - Verify final structure matches the approved plan.
> 
> Return a verification report and confirm back with:
> "✅ Execution complete — structure verified."
> ```
> 
> ---
> 
> ### **Step 5 — Data Extraction**
> ```text
> From the finalized set:
> - Extract structured data from tax forms and ID documents.
> - Output a single `master.json` with `{field: value}` pairs.
> 
> Double-check for consistency and confirm back with:
> "📦 Master JSON file ready — review data before using."
> ```
> 
> ---
> 
> This gives you **natural pause points** to eyeball the output, approve, and keep control — perfect for Cursor’s conversational flow.  
> 
> Would you like me to also give you a **single “orchestrator” version** you can run later once you trust it, so it just does all five steps back-to-back but still reports after each one? That can be your speed-run mode once you’ve debugged the workflow.

### User
> for pdf they will need to convert 1 page to jpeg then ocr the jpg because pdf takes too long and doesnt work mostly.

### Assistant
> Exactly — that’s the most reliable approach for speed and accuracy. Let’s bake that directly into the step so Cursor does it automatically and efficiently.
> 
> Here’s the **final refined sequence** with explicit PDF→JPEG→OCR built in:
> 
> ---
> 
> ### **Step 1 — Inventory**
> ```text
> Recursively walk the target directory.
> Return a JSON inventory with:
> - current_path
> - file_name
> - file_type
> 
> Do not change anything yet.
> Confirm back with:
> "✅ Inventory complete — ready for review."
> ```
> 
> ---
> 
> ### **Step 2 — Context Review (PDF→JPEG→OCR)**
> ```text
> For each file in the inventory:
> - If PDF: extract the first page only, convert it to JPEG, then OCR that JPEG.
> - If image or docx: OCR or read text directly.
> - Add a `summary` field describing the document’s purpose.
> 
> Return the updated JSON and confirm with:
> "✅ Context review complete — ready for review."
> Do not rename or move anything yet.
> ```
> 
> ---
> 
> ### **Step 3 — Movement Plan**
> ```text
> Using the updated inventory:
> - Create a proposed movement plan:
>   - current_path
>   - current_name
>   - proposed_path (if moving)
>   - proposed_name (if renaming)
>   - reason
> 
> Double-check for mistakes or conflicts.
> Return the plan and confirm with:
> "📋 Movement plan ready — review required before execution."
> Stop and wait for approval before proceeding.
> ```
> 
> ---
> 
> ### **Step 4 — Execute & Verify**
> ```text
> After approval:
> - Apply all moves/renames.
> - Re-run the inventory.
> - Verify final structure matches the approved plan exactly.
> 
> Return a verification report and confirm:
> "✅ Execution complete — structure verified."
> ```
> 
> ---
> 
> ### **Step 5 — Data Extraction**
> ```text
> From the finalized set:
> - Extract structured field data from tax forms (year, name, SSN, totals).
> - Extract data from identity documents (name, DOB, passport/ID numbers).
> - Output a single `master.json` with `{field: value}` pairs.
> 
> Double-check data consistency and confirm:
> "📦 Master JSON file ready — review data before using."
> ```
> 
> ---
> 
> This keeps it **fast** by only touching the first page of PDFs, and avoids full PDF parsing which is usually slow and error-prone. You’ll still get context (titles, names, form type) without wasting time on irrelevant pages.  
> 
> Want me to add a **failsafe** here — for example, if OCR fails on the first page, try the second page automatically before skipping? That can catch blank cover pages without manual intervention.

### User
> I'll recursively walk the directory and create a JSON inventory of all files and folders. Let me start by exploring the directory structure.
> 
> 
> [1 tool called]
> 
> Now I need to explore the subdirectories to get a complete inventory. Let me check the nested folders systematically:
> 
> 
> [9 tools called]
> 
> Now let me continue exploring the Joint Documents and other major directories:
> 
> 
> [14 tools called]
> 
> Now let me continue with the USCIS Documents and other directories:
> 
> 
> [10 tools called]
> 
> Now let me check the .cursor directory and any other hidden files:
> 
> 
> [2 tools called]
> 
> Now I have a complete inventory. Let me create the JSON structure with all the files and folders I've discovered:
> 
> ```json
> {
>   "inventory": [
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa",
>       "file_name": "_headers",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa",
>       "file_name": "_README.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa",
>       "file_name": "_redirects",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa",
>       "file_name": "00_Individual_Documents",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents",
>       "file_name": "_README.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents",
>       "file_name": "Beneficiary_Ciriaco_Castaneda",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda",
>       "file_name": "01_Identity_Financial",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "file_name": "attachment-photo-passport-c_castaneda-rodriguez.jpeg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "file_name": "BEN_Birth_Cert_001_Original.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "file_name": "BEN_Birth_Cert_002_Translation.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "file_name": "BEN_Birth_Cert_003_Supplemental.pdf",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "file_name": "BEN_Birth_Certificate-001.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "file_name": "BEN_Foregin_Voters_Registration_Stub-001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "file_name": "Castaneda-Rodriguez_Ciri-(Beneficiary)-SS-Card.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "file_name": "Castaneda-Rodriguez_Ciri-(Beneficiary)-SSA-89.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "file_name": "Castaneda-Rodriguez_Ciri-(Beneficiary)-SSA-Docusign-001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "file_name": "Castaneda-Rodriguez_Ciri-(Beneficiary)-SSA-Docusign-002.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "file_name": "Castaneda-Rodriguez_Ciri-(Beneficiary)-SSN_Receipt.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda",
>       "file_name": "02_Employment_Personal",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "_README.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "document_2025_01.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "document_2025_02.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "document_2025_03.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "document_2025_04.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "document_2025_38.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "document_2025_61.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "document_2025_62.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "document_2025_63.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "document_2025_67.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "document_2025_69.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "document_2025_71.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "document_2025_73.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "document_2025_75.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "document_2025_76.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "Entry_Records",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal\\Entry_Records",
>       "file_name": "_README.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "OR_10_CP_10_Plane_Tickets",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "OR_11_CP_11_Bus_Tickets",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "Travel_Documents",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal\\Travel_Documents",
>       "file_name": "_README.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "Travel_Photos",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal\\Travel_Photos",
>       "file_name": "_README.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal",
>       "file_name": "Visa_History",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\02_Employment_Personal\\Visa_History",
>       "file_name": "_README.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents",
>       "file_name": "Beneficiary_Passport_Photos.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents",
>       "file_name": "Petitioner_Passport_Photos.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents",
>       "file_name": "Petitioner_Rosa_Lucas",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas",
>       "file_name": "01_Identity_Financial",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "file_name": "_README.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "file_name": "attachment-photo-passport-r_lucas-esteban.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "file_name": "Indiana_Drivers_License-001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "file_name": "Indiana_Drivers_License-002.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "file_name": "Joint_Accounts",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial\\Joint_Accounts",
>       "file_name": "1320_Joint bank account statements.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial\\Joint_Accounts",
>       "file_name": "1350_Joint Loan Statements.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial\\Joint_Accounts",
>       "file_name": "BANK_00000000_1321_Chase-Deposit-Balance-Summary_P001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "file_name": "Lucas-Esteban_Rosa (Petitioner)-I551 .png",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "file_name": "PET_Birth_Cert_001_Original.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "file_name": "PET_Birth_Cert_002_Digital.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "file_name": "PET_Birth_Cert_003_Translation.pdf",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "file_name": "PET_Birth_Cert_004_Translation.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "file_name": "PET_Birth_Cert_005_Supplemental.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "file_name": "PET_Birth_Certificate-001.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas",
>       "file_name": "02_Employment_Personal",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents",
>       "file_name": "README.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa",
>       "file_name": "01_Joint_Documents",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents",
>       "file_name": "01_Marriage_Financial",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial",
>       "file_name": "_README.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial",
>       "file_name": "Certificates",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Certificates",
>       "file_name": "_README.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Certificates",
>       "file_name": "1301_Marriage Certificate.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Certificates",
>       "file_name": "1302_Marriage Certificate.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Certificates",
>       "file_name": "document_0909_11.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial",
>       "file_name": "Divorces",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Divorces",
>       "file_name": "126_Divorce Decrees.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial",
>       "file_name": "Family_Photos",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Family_Photos",
>       "file_name": "README.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial",
>       "file_name": "Joint_Accounts",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Accounts",
>       "file_name": "BANK_20220902_09022022_Operating_Bank_P001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Accounts",
>       "file_name": "BANK_20220923_09232022_Operating_Bank_P001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Accounts",
>       "file_name": "BANK_20221216_12162022_Operating_Bank_P001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Accounts",
>       "file_name": "BANK_20230630_06302023_Operating_Bank_P001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Accounts",
>       "file_name": "BANK_20240223_02232024_Operating_Bank_P001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Accounts",
>       "file_name": "BANK_20240924_09242024_Operating_Bank_P001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Accounts",
>       "file_name": "BANK_20241202_12022024_Operating_Bank_P001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Accounts",
>       "file_name": "BANK_20250721_07212025_Operating_Bank_P001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial",
>       "file_name": "Joint_Insurance",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Insurance",
>       "file_name": "1370_Joint Auto Insurance Policy.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Insurance",
>       "file_name": "core-plugins.json",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Insurance",
>       "file_name": "INS_00000000_1371_Founders_Insurance_Company_P001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Insurance",
>       "file_name": "INS_00000000_1371_Founders_Insurance_Company_P002.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Insurance",
>       "file_name": "Insurance_Doc_09092025_001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Insurance",
>       "file_name": "Insurance_Doc_09092025_002.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Insurance",
>       "file_name": "Insurance_Doc_09092025_003.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Insurance",
>       "file_name": "Insurance_Doc_09092025_004.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Insurance",
>       "file_name": "Insurance_Doc_09092025.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Insurance",
>       "file_name": "PAY_20170715_07152017_Instructions_for_Payer_Borrower_Aporcor_including_afin_P001.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Insurance",
>       "file_name": "PAY_20170715_07152017_Instructions_for_Payer_Borrower_Borrower_Aporcor_including_afin_P002.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial",
>       "file_name": "Joint_Lease or Mortgage",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Lease or Mortgage",
>       "file_name": "1340_Lease Agreement-Mortgage w. both.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial",
>       "file_name": "Joint_Utilities",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Utilities",
>       "file_name": "1360_Joint Utility Bills.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Utilities",
>       "file_name": "1361_Electric.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Utilities",
>       "file_name": "1362_Internet.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Utilities",
>       "file_name": "1363_Water.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial",
>       "file_name": "Letters",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Letters",
>       "file_name": "1401_C.Santos.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial",
>       "file_name": "Other Joint Records",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Other Joint Records",
>       "file_name": "1380_Other Joint Record - Copy.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Other Joint Records",
>       "file_name": "1381_Medical.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Other Joint Records",
>       "file_name": "1382_School.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial",
>       "file_name": "Photos",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Photos",
>       "file_name": "_README.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Photos",
>       "file_name": "131_Family Photos",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Photos\\131_Family Photos",
>       "file_name": "1310_Family photos.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial",
>       "file_name": "Relationship_Timeline",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Relationship_Timeline",
>       "file_name": "_README.md",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial",
>       "file_name": "Tax_Documents",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents",
>       "file_name": "2022_Tax_Year",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year",
>       "file_name": "2022",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022",
>       "file_name": "Deductions",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Deductions",
>       "file_name": "1098_SLB_ASSETS-MORT-INT.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022",
>       "file_name": "Expense_Receipts",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Expense_Receipts",
>       "file_name": "1099_misc_2022_v2.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Expense_Receipts",
>       "file_name": "1099_misc_2022_v3.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Expense_Receipts",
>       "file_name": "1099_misc_2022_v4.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022",
>       "file_name": "Income",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022",
>       "file_name": "Tax_Filings",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Tax_Filings",
>       "file_name": "TaxReturn.20250919T810315Z.pdf",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022",
>       "file_name": "Wages-n-Income",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Wages-n-Income",
>       "file_name": "1099-MISC_PRINCESS HOUSE - ROSA.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Wages-n-Income",
>       "file_name": "1099-MISC_PRINCESS HOUSE 2 - ROSA.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Wages-n-Income",
>       "file_name": "1099-NEC_RAMON SANCHEZ - ROSA.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Wages-n-Income",
>       "file_name": "1099-NEC_SERGIO_SANCHEZ-CIRIACO.pdf",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Wages-n-Income",
>       "file_name": "CHECKSTUB-CAPITALCITY-20220101.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Wages-n-Income",
>       "file_name": "CHECKSTUB-CAPITALCITY-20220506.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Wages-n-Income",
>       "file_name": "W2_GEODIS_ROSA.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents",
>       "file_name": "2023_Tax_Year",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2023_Tax_Year",
>       "file_name": "2023",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2023_Tax_Year\\2023",
>       "file_name": "Deductions",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2023_Tax_Year\\2023\\Deductions",
>       "file_name": "1098_2017.jpg",
>       "file_type": "file"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2023_Tax_Year\\2023",
>       "file_name": "Expenses",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2023_Tax_Year\\2023",
>       "file_name": "Tax_Filings",
>       "file_type": "folder"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2023_Tax_Year\\2023",
>       "file_name": "Wages-n-Income"

### Assistant
> Queen of Receipts, you did Step 1. Nice pull. Now drop these **one-at-a-time** into Cursor. They assume you already have the JSON inventory from your last step.
> 
> ---
> 
> ### Step 2 — Context review with PDF→JPEG→OCR (+ auto fallback)
> ```text
> You have an `inventory` JSON from the prior step. Review each item to understand purpose WITHOUT moving/renaming files.
> 
> Rules:
> - If file_type == "pdf": extract page 1 → JPEG (150–200 DPI). If OCR returns low confidence, try page 2 automatically. Store temp JPEGs under `.tmp/ocr/` mirroring the source path. Delete temps after processing.
> - If image (jpg/jpeg/png/webp/tif): OCR directly.
> - If md/txt: read first 2000 chars.
> - If docx: extract text (no conversion if a docx reader is available); else skip with reason.
> 
> Heuristics (assign any that match):
> - form_type: detect common USCIS/IRS codes (I-130, I-485, I-864, I-765, I-693, I-589, G-28, SSA-89, W-2, 1099-NEC, 1099-MISC, 1095-A, 1098).
> - evidence_type: Identity | Marriage | Financial | Tax | Employment | Travel | Photos | Letters | Medical | School | Utilities | Insurance | Court.
> - person_role: Petitioner | Beneficiary | Joint | Unknown (infer from filenames like `PET_`, `BEN_`, “Joint”, or folder path).
> - year: 4-digit year if obvious (in filename or form).
> - summary: 1-2 sentences, human-readable.
> - confidence: 0–1 float for detection confidence.
> 
> Return JSON `review` with one object per file:
> {
>   "current_path": "...",
>   "file_name": "...",
>   "file_type": "...",
>   "summary": "...",
>   "form_type": "I-130|I-864|W-2|…|Unknown",
>   "evidence_type": "Identity|Marriage|…|Unknown",
>   "person_role": "Petitioner|Beneficiary|Joint|Unknown",
>   "year": 2023|null,
>   "confidence": 0.0–1.0,
>   "notes": "any anomalies"
> }
> 
> Confirm back ONLY with:
> "✅ Context review complete — ready for review."
> ```
> 
> ---
> 
> ### Step 3 — Movement plan (proposal only; double-check before output)
> ```text
> Using the `review` JSON:
> - Propose moves/renames, DO NOT execute.
> - Keep your proposal simple and legible.
> 
> Naming rules (apply when renaming is helpful):
> - Prefer: <ROLE>__<EVIDENCE or FORM>__<FORM/TYPE/DETAIL>__<YEAR or DATE>__v01.<ext>
>   Examples:
>   - PET__Identity__Birth-Cert__1990__v01.jpg
>   - JOINT__Tax__W-2__2022__Rosa__v01.jpg
>   - BEN__Form__I-130A__v01.pdf
> - Preserve original if already clear; otherwise propose rename.
> 
> Placement rules (examples; adapt to your vault):
> - Individual docs → `00_Individual_Documents/<Petitioner_* or Beneficiary_*>/<01_Identity_Financial or 02_Employment_Personal/...>`
> - Joint docs → `01_Joint_Documents/01_Marriage_Financial/<Joint_Accounts | Joint_Insurance | Joint_Utilities | Photos | Certificates | Tax_Documents/...>`
> - Tax by year → `.../Tax_Documents/<YYYY_Tax_Year>/<YYYY>/<Wages-n-Income|Tax_Filings|Deductions|Expenses>`
> 
> Output `movement_plan` as JSON array:
> {
>   "current_path": "...",
>   "current_name": "...",
>   "proposed_path": "...",        // null if unchanged
>   "proposed_name": "...",        // null if unchanged
>   "reason": "short justification",
>   "risk": "low|medium|high"      // high = ambiguous detection
> }
> 
> Double-check for path conflicts, filename collisions, missing parents, or circular moves. If any risk != low, flag in `reason`.
> 
> Confirm back ONLY with:
> "📋 Movement plan ready — review required before execution."
> ```
> 
> ---
> 
> ### Step 4 — Execute & verify (after you approve the plan)
> ```text
> Apply the approved `movement_plan`. Steps:
> 1) Dry-run: simulate moves/renames and report any conflicts.
> 2) Execute: perform filesystem changes exactly as approved.
> 3) Re-inventory: produce `post_inventory` JSON (same schema as initial).
> 4) Diff: report adds/moves/renames vs. the plan. Fail if mismatched.
> 5) Integrity: confirm all target directories exist; no orphaned files; no duplicates.
> 
> Return:
> {
>   "applied": [ ...items moved/renamed... ],
>   "skipped": [ ...items + reasons... ],
>   "post_inventory": { ... },
>   "diff_summary": { "moved": n, "renamed": n, "unchanged": n, "issues": n }
> }
> 
> Confirm back ONLY with:
> "✅ Execution complete — structure verified."
> ```
> 
> ---
> 
> ### Step 5 — Data extraction → `master.json` (tax + ID docs)
> ```text
> From the verified structure, extract fields from:
> - IRS forms (W-2, 1099-NEC/MISC, 1095-A, 1098, 1040 summary pages if present)
> - Identity docs (passport, I-551, SSN card, DL/State ID, birth/marriage certs, SSA-89)
> 
> Field targets (populate when present):
> {
>   "person_role": "Petitioner|Beneficiary|Joint",
>   "person_name": "...",
>   "dob": "YYYY-MM-DD",
>   "ssn_last4": "...",
>   "a_number": "A###-###-###",
>   "passport_number": "...",
>   "dl_number": "...",
>   "i551_alien_number": "...",
>   "form": "W-2|1099-NEC|1095-A|1098|SSA-89|BirthCert|MarriageCert|I-551|I-130|I-864|...",
>   "tax_year": 2022|2023|null,
>   "employer_payer": "...",
>   "wages_or_amount": "...",
>   "address": "...",
>   "document_issue_date": "YYYY-MM-DD|null",
>   "document_expiry_date": "YYYY-MM-DD|null",
>   "source_path": "full path to file"
> }
> 
> Output a single `master.json` (array of records). Include `"confidence"` per record and `"notes"` for uncertain OCR fields. Deduplicate by (form + tax_year + person_name + employer_payer) keeping highest confidence.
> 
> Confirm back ONLY with:
> "📦 Master JSON file ready — review data before using."
> ```
> 
> ---
> 
> ### Optional failsafes to add (recommended)
> - If first PDF page is blank/cover, auto-try page 2.
> - If OCR confidence < 0.55, mark `risk: high` and do **not** propose renames/moves for that item in Step 3.
> - For very large images, downscale to max 2500px on the long side before OCR to speed up.
> 
> ---
> 
> When you’re ready, paste **Step 2** first. After it confirms, eyeball the JSON, then go Step 3 → Step 4 → Step 5. Momentum on, nonsense off.

### User
> {

>   "review": [

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial\\PET_Birth_Cert_001_Original.jpg",

>       "file_name": "PET_Birth_Cert_001_Original.jpg",

>       "file_type": "jpg",

>       "summary": "Original birth certificate for petitioner Rosa Lucas-Esteban from San Juan Bautista Tuxtepec, Oaxaca, Mexico.",

>       "form_type": "Unknown",

>       "evidence_type": "Identity",

>       "person_role": "Petitioner",

>       "year": 1971,

>       "confidence": 0.95,

>       "notes": "Primary identity document for petitioner"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial\\PET_Birth_Cert_002_Digital.jpg",

>       "file_name": "PET_Birth_Cert_002_Digital.jpg",

>       "file_type": "jpg",

>       "summary": "Digital copy of petitioner's birth certificate for Rosa Lucas-Esteban.",

>       "form_type": "Unknown",

>       "evidence_type": "Identity",

>       "person_role": "Petitioner",

>       "year": 1971,

>       "confidence": 0.95,

>       "notes": "Digital backup of original birth certificate"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial\\PET_Birth_Cert_003_Translation.pdf",

>       "file_name": "PET_Birth_Cert_003_Translation.pdf",

>       "file_type": "pdf",

>       "summary": "Official English translation of petitioner's birth certificate from Spanish to English.",

>       "form_type": "Unknown",

>       "evidence_type": "Identity",

>       "person_role": "Petitioner",

>       "year": 1971,

>       "confidence": 0.95,

>       "notes": "Certified translation required for USCIS"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial\\PET_Birth_Cert_004_Translation.md",

>       "file_name": "PET_Birth_Cert_004_Translation.md",

>       "file_type": "md",

>       "summary": "Markdown transcription of petitioner's birth certificate translation showing Rosa Lucas-Esteban born March 30, 1971 in San Juan Bautista Tuxtepec, Oaxaca.",

>       "form_type": "Unknown",

>       "evidence_type": "Identity",

>       "person_role": "Petitioner",

>       "year": 1971,

>       "confidence": 0.98,

>       "notes": "Text version of birth certificate translation"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial\\PET_Birth_Cert_005_Supplemental.md",

>       "file_name": "PET_Birth_Cert_005_Supplemental.md",

>       "file_type": "md",

>       "summary": "Supplemental documentation for petitioner's birth certificate with additional verification details.",

>       "form_type": "Unknown",

>       "evidence_type": "Identity",

>       "person_role": "Petitioner",

>       "year": 1971,

>       "confidence": 0.90,

>       "notes": "Additional supporting documentation"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial\\BEN_Birth_Cert_001_Original.jpg",

>       "file_name": "BEN_Birth_Cert_001_Original.jpg",

>       "file_type": "jpg",

>       "summary": "Original birth certificate for beneficiary Ciriaco Castañeda Rodríguez from Ayahualulco, Chilapa de Álvarez, Guerrero, Mexico.",

>       "form_type": "Unknown",

>       "evidence_type": "Identity",

>       "person_role": "Beneficiary",

>       "year": 1987,

>       "confidence": 0.95,

>       "notes": "Primary identity document for beneficiary"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial\\BEN_Birth_Cert_002_Translation.md",

>       "file_name": "BEN_Birth_Cert_002_Translation.md",

>       "file_type": "md",

>       "summary": "Certificate of Origin for beneficiary Ciriaco Castañeda Rodríguez born June 27, 1987 in Ayahualulco, Chilapa de Álvarez, Guerrero, Mexico.",

>       "form_type": "Unknown",

>       "evidence_type": "Identity",

>       "person_role": "Beneficiary",

>       "year": 1987,

>       "confidence": 0.98,

>       "notes": "Official certificate with family verification"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial\\BEN_Birth_Cert_003_Supplemental.pdf",

>       "file_name": "BEN_Birth_Cert_003_Supplemental.pdf",

>       "file_type": "pdf",

>       "summary": "Supplemental documentation for beneficiary's birth certificate with additional verification details.",

>       "form_type": "Unknown",

>       "evidence_type": "Identity",

>       "person_role": "Beneficiary",

>       "year": 1987,

>       "confidence": 0.90,

>       "notes": "Additional supporting documentation"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial\\Indiana_Drivers_License-001.jpg",

>       "file_name": "Indiana_Drivers_License-001.jpg",

>       "file_type": "jpg",

>       "summary": "Indiana driver's license for petitioner Rosa Lucas-Esteban showing current address and identification.",

>       "form_type": "Unknown",

>       "evidence_type": "Identity",

>       "person_role": "Petitioner",

>       "year": null,

>       "confidence": 0.95,

>       "notes": "Government-issued photo ID"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial\\Indiana_Drivers_License-002.jpg",

>       "file_name": "Indiana_Drivers_License-002.jpg",

>       "file_type": "jpg",

>       "summary": "Second copy of Indiana driver's license for petitioner Rosa Lucas-Esteban.",

>       "form_type": "Unknown",

>       "evidence_type": "Identity",

>       "person_role": "Petitioner",

>       "year": null,

>       "confidence": 0.95,

>       "notes": "Backup copy of driver's license"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial\\Lucas-Esteban_Rosa (Petitioner)-I551 .png",

>       "file_name": "Lucas-Esteban_Rosa (Petitioner)-I551 .png",

>       "file_type": "png",

>       "summary": "I-551 Permanent Resident Card (Green Card) for petitioner Rosa Lucas-Esteban showing lawful permanent resident status.",

>       "form_type": "I-551",

>       "evidence_type": "Identity",

>       "person_role": "Petitioner",

>       "year": null,

>       "confidence": 0.98,

>       "notes": "Permanent resident card - key immigration status document"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial\\Castaneda-Rodriguez_Ciri-(Beneficiary)-SS-Card.jpg",

>       "file_name": "Castaneda-Rodriguez_Ciri-(Beneficiary)-SS-Card.jpg",

>       "file_type": "jpg",

>       "summary": "Social Security card for beneficiary Ciriaco Castañeda Rodríguez showing authorized work status.",

>       "form_type": "Unknown",

>       "evidence_type": "Identity",

>       "person_role": "Beneficiary",

>       "year": null,

>       "confidence": 0.95,

>       "notes": "Social Security card with work authorization"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial\\Castaneda-Rodriguez_Ciri-(Beneficiary)-SSA-89.jpg",

>       "file_name": "Castaneda-Rodriguez_Ciri-(Beneficiary)-SSA-89.jpg",

>       "file_type": "jpg",

>       "summary": "SSA-89 form for beneficiary Ciriaco Castañeda Rodríguez related to Social Security application or update.",

>       "form_type": "SSA-89",

>       "evidence_type": "Identity",

>       "person_role": "Beneficiary",

>       "year": null,

>       "confidence": 0.90,

>       "notes": "Social Security Administration form"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Certificates\\1301_Marriage Certificate.jpg",

>       "file_name": "1301_Marriage Certificate.jpg",

>       "file_type": "jpg",

>       "summary": "Marriage certificate for Rosa Lucas-Esteban and Ciriaco Castañeda Rodríguez showing legal marriage status.",

>       "form_type": "Unknown",

>       "evidence_type": "Marriage",

>       "person_role": "Joint",

>       "year": null,

>       "confidence": 0.95,

>       "notes": "Primary marriage evidence document"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Certificates\\1302_Marriage Certificate.jpg",

>       "file_name": "1302_Marriage Certificate.jpg",

>       "file_type": "jpg",

>       "summary": "Second copy of marriage certificate for Rosa Lucas-Esteban and Ciriaco Castañeda Rodríguez.",

>       "form_type": "Unknown",

>       "evidence_type": "Marriage",

>       "person_role": "Joint",

>       "year": null,

>       "confidence": 0.95,

>       "notes": "Backup copy of marriage certificate"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Tax_Filings\\TaxReturn.20250919T810315Z.pdf",

>       "file_name": "TaxReturn.20250919T810315Z.pdf",

>       "file_type": "pdf",

>       "summary": "2022 joint tax return for Rosa Lucas-Esteban and Ciriaco Castañeda Rodríguez filed as married filing jointly.",

>       "form_type": "Unknown",

>       "evidence_type": "Tax",

>       "person_role": "Joint",

>       "year": 2022,

>       "confidence": 0.95,

>       "notes": "Complete 2022 tax return filing"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Wages-n-Income\\W2_GEODIS_ROSA.jpg",

>       "file_name": "W2_GEODIS_ROSA.jpg",

>       "file_type": "jpg",

>       "summary": "2022 W-2 form for Rosa Lucas-Esteban from GEODIS showing employment income and tax withholding.",

>       "form_type": "W-2",

>       "evidence_type": "Employment",

>       "person_role": "Petitioner",

>       "year": 2022,

>       "confidence": 0.98,

>       "notes": "Employment income documentation"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Wages-n-Income\\1099-NEC_SERGIO_SANCHEZ-CIRIACO.pdf",

>       "file_name": "1099-NEC_SERGIO_SANCHEZ-CIRIACO.pdf",

>       "file_type": "pdf",

>       "summary": "2022 1099-NEC form for Ciriaco Castañeda Rodríguez from Sergio Sanchez showing non-employee compensation income.",

>       "form_type": "1099-NEC",

>       "evidence_type": "Employment",

>       "person_role": "Beneficiary",

>       "year": 2022,

>       "confidence": 0.98,

>       "notes": "Self-employment income documentation"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Wages-n-Income\\1099-MISC_PRINCESS HOUSE - ROSA.jpg",

>       "file_name": "1099-MISC_PRINCESS HOUSE - ROSA.jpg",

>       "file_type": "jpg",

>       "summary": "2022 1099-MISC form for Rosa Lucas-Esteban from Princess House showing miscellaneous income.",

>       "form_type": "1099-MISC",

>       "evidence_type": "Employment",

>       "person_role": "Petitioner",

>       "year": 2022,

>       "confidence": 0.98,

>       "notes": "Additional income documentation"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2023_Tax_Year\\2023\\Wages-n-Income\\1099-NEC ROSA.jpg",

>       "file_name": "1099-NEC ROSA.jpg",

>       "file_type": "jpg",

>       "summary": "2023 1099-NEC form for Rosa Lucas-Esteban showing non-employee compensation income.",

>       "form_type": "1099-NEC",

>       "evidence_type": "Employment",

>       "person_role": "Petitioner",

>       "year": 2023,

>       "confidence": 0.98,

>       "notes": "Self-employment income for 2023"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2023_Tax_Year\\2023\\Wages-n-Income\\1099-NEC CIRACO.jpg",

>       "file_name": "1099-NEC CIRACO.jpg",

>       "file_type": "jpg",

>       "summary": "2023 1099-NEC form for Ciriaco Castañeda Rodríguez showing non-employee compensation income.",

>       "form_type": "1099-NEC",

>       "evidence_type": "Employment",

>       "person_role": "Beneficiary",

>       "year": 2023,

>       "confidence": 0.98,

>       "notes": "Self-employment income for 2023"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2024_Tax_Year\\2024\\1099_misc_2024.jpg",

>       "file_name": "1099_misc_2024.jpg",

>       "file_type": "jpg",

>       "summary": "2024 1099-MISC form showing miscellaneous income for current tax year.",

>       "form_type": "1099-MISC",

>       "evidence_type": "Employment",

>       "person_role": "Unknown",

>       "year": 2024,

>       "confidence": 0.95,

>       "notes": "Current year income documentation"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2024_Tax_Year\\2024\\bank_stmt_chase_2024.jpg",

>       "file_name": "bank_stmt_chase_2024.jpg",

>       "file_type": "jpg",

>       "summary": "2024 Chase bank statement showing joint account activity and financial stability.",

>       "form_type": "Unknown",

>       "evidence_type": "Financial",

>       "person_role": "Joint",

>       "year": 2024,

>       "confidence": 0.95,

>       "notes": "Joint bank account statement"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Accounts\\BANK_20220902_09022022_Operating_Bank_P001.jpg",

>       "file_name": "BANK_20220902_09022022_Operating_Bank_P001.jpg",

>       "file_type": "jpg",

>       "summary": "September 2022 joint bank account statement showing shared financial responsibility.",

>       "form_type": "Unknown",

>       "evidence_type": "Financial",

>       "person_role": "Joint",

>       "year": 2022,

>       "confidence": 0.95,

>       "notes": "Joint account evidence for marriage bona fides"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Insurance\\1370_Joint Auto Insurance Policy.md",

>       "file_name": "1370_Joint Auto Insurance Policy.md",

>       "file_type": "md",

>       "summary": "Joint auto insurance policy documentation showing shared insurance coverage for both spouses.",

>       "form_type": "Unknown",

>       "evidence_type": "Insurance",

>       "person_role": "Joint",

>       "year": null,

>       "confidence": 0.90,

>       "notes": "Joint insurance evidence"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Utilities\\1360_Joint Utility Bills.md",

>       "file_name": "1360_Joint Utility Bills.md",

>       "file_type": "md",

>       "summary": "Joint utility bills documentation showing shared household expenses and joint responsibility.",

>       "form_type": "Unknown",

>       "evidence_type": "Utilities",

>       "person_role": "Joint",

>       "year": null,

>       "confidence": 0.90,

>       "notes": "Joint utility evidence for marriage bona fides"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\02_USCIS_Documents\\01_Forms_Notices\\Receipt_Notices\\NOT_20250729_07292025_Form_i-797C_Notice_of_Action_P001.jpg",

>       "file_name": "NOT_20250729_07292025_Form_i-797C_Notice_of_Action_P001.jpg",

>       "file_type": "jpg",

>       "summary": "I-797C Notice of Action receipt from USCIS dated July 29, 2025 showing case acceptance and processing.",

>       "form_type": "I-797C",

>       "evidence_type": "Unknown",

>       "person_role": "Unknown",

>       "year": 2025,

>       "confidence": 0.95,

>       "notes": "USCIS receipt notice"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\02_USCIS_Documents\\01_Forms_Notices\\NOT-ACT-i797-FORM-I765_APPROVAL_20250419-20300418.jpg",

>       "file_name": "NOT-ACT-i797-FORM-I765_APPROVAL_20250419-20300418.jpg",

>       "file_type": "jpg",

>       "summary": "I-797 approval notice for Form I-765 (Employment Authorization Document) approved April 19, 2025.",

>       "form_type": "I-765",

>       "evidence_type": "Unknown",

>       "person_role": "Beneficiary",

>       "year": 2025,

>       "confidence": 0.98,

>       "notes": "Work authorization approval"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\02_USCIS_Documents\\01_Forms_Notices\\EAD.jpeg.png",

>       "file_name": "EAD.jpeg.png",

>       "file_type": "png",

>       "summary": "Employment Authorization Document (EAD) card showing work authorization for beneficiary.",

>       "form_type": "I-765",

>       "evidence_type": "Identity",

>       "person_role": "Beneficiary",

>       "year": null,

>       "confidence": 0.95,

>       "notes": "Physical EAD card"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\Intake_Forms\\01-Immigration Intake Form.md",

>       "file_name": "01-Immigration Intake Form.md",

>       "file_type": "md",

>       "summary": "Comprehensive immigration intake form with petitioner and beneficiary information including personal details, addresses, and family information.",

>       "form_type": "Unknown",

>       "evidence_type": "Unknown",

>       "person_role": "Joint",

>       "year": null,

>       "confidence": 0.95,

>       "notes": "Case intake documentation"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\02_Legal_Agreements\\Legal_Documents\\Accountant_Verification_Letter_Draft.md",

>       "file_name": "Accountant_Verification_Letter_Draft.md",

>       "file_type": "md",

>       "summary": "Draft accountant verification letter template for employment and financial verification for immigration case.",

>       "form_type": "Unknown",

>       "evidence_type": "Employment",

>       "person_role": "Joint",

>       "year": null,

>       "confidence": 0.90,

>       "notes": "Employment verification template"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\02_Legal_Agreements\\Legal_Documents\\Living_Will_Draft.md",

>       "file_name": "Living_Will_Draft.md",

>       "file_type": "md",

>       "summary": "Draft living will and testament naming spouse as beneficiary, demonstrating financial interdependence and family relationship.",

>       "form_type": "Unknown",

>       "evidence_type": "Unknown",

>       "person_role": "Joint",

>       "year": null,

>       "confidence": 0.90,

>       "notes": "Estate planning document for marriage evidence"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Family_Photos\\README.md",

>       "file_name": "README.md",

>       "file_type": "md",

>       "summary": "Family photos collection requirements and guidelines for immigration case showing marriage bona fides.",

>       "form_type": "Unknown",

>       "evidence_type": "Photos",

>       "person_role": "Joint",

>       "year": null,

>       "confidence": 0.85,

>       "notes": "Photo collection guidelines"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Passport_Photos.md",

>       "file_name": "Petitioner_Passport_Photos.md",

>       "file_type": "md",

>       "summary": "Passport photo status tracking for petitioner Rosa Lucas-Esteban showing completion status.",

>       "form_type": "Unknown",

>       "evidence_type": "Photos",

>       "person_role": "Petitioner",

>       "year": null,

>       "confidence": 0.90,

>       "notes": "Photo requirements tracking"

>     },

>     {

>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Passport_Photos.md",

>       "file_name": "Beneficiary_Passport_Photos.md",

>       "file_type": "md",

>       "summary": "Passport photo status tracking for beneficiary Ciriaco Castañeda Rodríguez showing completion status.",

>       "form_type": "Unknown",

>       "evidence_type": "Photos",

>       "person_role": "Beneficiary",

>       "year": null,

>       "confidence": 0.90,

>       "notes": "Photo requirements tracking"

>     }

>   ]

> }

### Assistant
> 📋 Movement plan ready — review required before execution.
> 
> Here’s the proposed plan (no changes applied yet). I kept moves minimal and only suggested renames where it clearly improves clarity. Items with uncertainty are flagged with `risk`.
> 
> ```json
> {
>   "movement_plan": [
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "current_name": "PET_Birth_Cert_001_Original.jpg",
>       "proposed_path": null,
>       "proposed_name": "PET__Identity__Birth-Cert__1971__Original__v01.jpg",
>       "reason": "Standardize naming (role, type, year, version).",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "current_name": "PET_Birth_Cert_002_Digital.jpg",
>       "proposed_path": null,
>       "proposed_name": "PET__Identity__Birth-Cert__1971__Digital__v01.jpg",
>       "reason": "Standardize naming and clarify digital copy.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "current_name": "PET_Birth_Cert_003_Translation.pdf",
>       "proposed_path": null,
>       "proposed_name": "PET__Identity__Birth-Cert__1971__Translation__v01.pdf",
>       "reason": "Align translation with birth cert set.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "current_name": "PET_Birth_Cert_004_Translation.md",
>       "proposed_path": null,
>       "proposed_name": "PET__Identity__Birth-Cert__1971__Translation__Text__v01.md",
>       "reason": "Clarify text transcription vs certified PDF.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "current_name": "PET_Birth_Cert_005_Supplemental.md",
>       "proposed_path": null,
>       "proposed_name": "PET__Identity__Birth-Cert__1971__Supplemental__v01.md",
>       "reason": "Consistent set naming.",
>       "risk": "low"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "current_name": "BEN_Birth_Cert_001_Original.jpg",
>       "proposed_path": null,
>       "proposed_name": "BEN__Identity__Birth-Cert__1987__Original__v01.jpg",
>       "reason": "Standardize beneficiary birth certificate.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "current_name": "BEN_Birth_Cert_002_Translation.md",
>       "proposed_path": null,
>       "proposed_name": "BEN__Identity__Birth-Cert__1987__Translation__Text__v01.md",
>       "reason": "Clarify translation text.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "current_name": "BEN_Birth_Cert_003_Supplemental.pdf",
>       "proposed_path": null,
>       "proposed_name": "BEN__Identity__Birth-Cert__1987__Supplemental__v01.pdf",
>       "reason": "Consistent set naming.",
>       "risk": "low"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "current_name": "Indiana_Drivers_License-001.jpg",
>       "proposed_path": null,
>       "proposed_name": "PET__Identity__DL-IN__Front__v01.jpg",
>       "reason": "Clarify ID type and page/side.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "current_name": "Indiana_Drivers_License-002.jpg",
>       "proposed_path": null,
>       "proposed_name": "PET__Identity__DL-IN__Back__v01.jpg",
>       "reason": "Clarify ID type and page/side.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Petitioner_Rosa_Lucas\\01_Identity_Financial",
>       "current_name": "Lucas-Esteban_Rosa (Petitioner)-I551 .png",
>       "proposed_path": null,
>       "proposed_name": "PET__Identity__I-551__Card__v01.png",
>       "reason": "Normalize name; remove space before extension; standard format.",
>       "risk": "low"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "current_name": "Castaneda-Rodriguez_Ciri-(Beneficiary)-SS-Card.jpg",
>       "proposed_path": null,
>       "proposed_name": "BEN__Identity__SSN-Card__v01.jpg",
>       "reason": "Standardize SSN card naming.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents\\Beneficiary_Ciriaco_Castaneda\\01_Identity_Financial",
>       "current_name": "Castaneda-Rodriguez_Ciri-(Beneficiary)-SSA-89.jpg",
>       "proposed_path": null,
>       "proposed_name": "BEN__Identity__SSA-89__v01.jpg",
>       "reason": "Standardize SSA-89 naming.",
>       "risk": "low"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Certificates",
>       "current_name": "1301_Marriage Certificate.jpg",
>       "proposed_path": null,
>       "proposed_name": "JOINT__Marriage__Certificate__v01.jpg",
>       "reason": "Normalize marriage certificate naming.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Certificates",
>       "current_name": "1302_Marriage Certificate.jpg",
>       "proposed_path": null,
>       "proposed_name": "JOINT__Marriage__Certificate__v02.jpg",
>       "reason": "Second copy; versioned.",
>       "risk": "low"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Tax_Filings",
>       "current_name": "TaxReturn.20250919T810315Z.pdf",
>       "proposed_path": null,
>       "proposed_name": "JOINT__Tax__Return__2022__v01.pdf",
>       "reason": "Make tax year explicit; remove timestamp noise.",
>       "risk": "low"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Wages-n-Income",
>       "current_name": "W2_GEODIS_ROSA.jpg",
>       "proposed_path": null,
>       "proposed_name": "PET__Tax__W-2__2022__GEODIS__v01.jpg",
>       "reason": "Standardize W-2 naming (role, year, payer).",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Wages-n-Income",
>       "current_name": "1099-NEC_SERGIO_SANCHEZ-CIRIACO.pdf",
>       "proposed_path": null,
>       "proposed_name": "BEN__Tax__1099-NEC__2022__Sergio-Sanchez__v01.pdf",
>       "reason": "Standardize 1099 naming.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2022_Tax_Year\\2022\\Wages-n-Income",
>       "current_name": "1099-MISC_PRINCESS HOUSE - ROSA.jpg",
>       "proposed_path": null,
>       "proposed_name": "PET__Tax__1099-MISC__2022__Princess-House__v01.jpg",
>       "reason": "Normalize payer name; standard structure.",
>       "risk": "low"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2023_Tax_Year\\2023\\Wages-n-Income",
>       "current_name": "1099-NEC ROSA.jpg",
>       "proposed_path": null,
>       "proposed_name": "PET__Tax__1099-NEC__2023__Unknown-Payer__v01.jpg",
>       "reason": "Add role and year; payer not in filename.",
>       "risk": "medium"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2023_Tax_Year\\2023\\Wages-n-Income",
>       "current_name": "1099-NEC CIRACO.jpg",
>       "proposed_path": null,
>       "proposed_name": "BEN__Tax__1099-NEC__2023__Unknown-Payer__v01.jpg",
>       "reason": "Add role and year; payer not in filename.",
>       "risk": "medium"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2024_Tax_Year\\2024",
>       "current_name": "1099_misc_2024.jpg",
>       "proposed_path": null,
>       "proposed_name": "UNKNOWN__Tax__1099-MISC__2024__v01.jpg",
>       "reason": "Year known; role unknown from OCR. Keep generic.",
>       "risk": "medium"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Tax_Documents\\2024_Tax_Year\\2024",
>       "current_name": "bank_stmt_chase_2024.jpg",
>       "proposed_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Accounts",
>       "proposed_name": "JOINT__Financial__Bank-Statement__Chase__2024__v01.jpg",
>       "reason": "Bank statements belong under Joint_Accounts, not Tax_Year root.",
>       "risk": "low"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Accounts",
>       "current_name": "BANK_20220902_09022022_Operating_Bank_P001.jpg",
>       "proposed_path": null,
>       "proposed_name": "JOINT__Financial__Bank-Statement__Operating__2022-09-02__v01.jpg",
>       "reason": "Normalize date format and context.",
>       "risk": "low"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Insurance",
>       "current_name": "1370_Joint Auto Insurance Policy.md",
>       "proposed_path": null,
>       "proposed_name": "JOINT__Insurance__Auto-Policy__v01.md",
>       "reason": "Standardize joint insurance naming.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Joint_Utilities",
>       "current_name": "1360_Joint Utility Bills.md",
>       "proposed_path": null,
>       "proposed_name": "JOINT__Utilities__Bills__v01.md",
>       "reason": "Standardize utilities naming.",
>       "risk": "low"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\02_USCIS_Documents\\01_Forms_Notices\\Receipt_Notices",
>       "current_name": "NOT_20250729_07292025_Form_i-797C_Notice_of_Action_P001.jpg",
>       "proposed_path": null,
>       "proposed_name": "USCIS__Notice__I-797C__Receipt__2025-07-29__v01.jpg",
>       "reason": "Normalize notice naming, explicit date.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\02_USCIS_Documents\\01_Forms_Notices",
>       "current_name": "NOT-ACT-i797-FORM-I765_APPROVAL_20250419-20300418.jpg",
>       "proposed_path": null,
>       "proposed_name": "USCIS__Notice__I-765__Approval__2025-04-19__v01.jpg",
>       "reason": "Clarify approval type and date; drop expiry window from name.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\02_USCIS_Documents\\01_Forms_Notices",
>       "current_name": "EAD.jpeg.png",
>       "proposed_path": null,
>       "proposed_name": "USCIS__ID__EAD__Card__Front__v01.png",
>       "reason": "Fix double extension; standardize EAD card name.",
>       "risk": "low"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\Intake_Forms",
>       "current_name": "01-Immigration Intake Form.md",
>       "proposed_path": null,
>       "proposed_name": "CASE__Intake__Rosa-Ciriaco__v01.md",
>       "reason": "Standardize case intake naming; pair both parties.",
>       "risk": "low"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\02_Legal_Agreements\\Legal_Documents",
>       "current_name": "Accountant_Verification_Letter_Draft.md",
>       "proposed_path": null,
>       "proposed_name": "JOINT__Legal__Accountant-Verification-Letter__Draft__v01.md",
>       "reason": "Clarify doc purpose and status.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\02_Legal_Agreements\\Legal_Documents",
>       "current_name": "Living_Will_Draft.md",
>       "proposed_path": null,
>       "proposed_name": "JOINT__Legal__Living-Will__Draft__v01.md",
>       "reason": "Clarify legal doc type and status.",
>       "risk": "low"
>     },
> 
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\01_Joint_Documents\\01_Marriage_Financial\\Family_Photos",
>       "current_name": "README.md",
>       "proposed_path": null,
>       "proposed_name": null,
>       "reason": "Leave as-is (folder guidance).",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents",
>       "current_name": "Petitioner_Passport_Photos.md",
>       "proposed_path": null,
>       "proposed_name": null,
>       "reason": "Leave as-is; status tracker.",
>       "risk": "low"
>     },
>     {
>       "current_path": "k:\\vaults\\client\\rosalucas\\Vault_Rosa\\00_Individual_Documents",
>       "current_name": "Beneficiary_Passport_Photos.md",
>       "proposed_path": null,
>       "proposed_name": null,
>       "reason": "Leave as-is; status tracker.",
>       "risk": "low"
>     }
>   ]
> }
> ```
> 
> If this looks right, say “Approve Step 4” and I’ll run the execute & verify instructions exactly against this plan. If you want tweaks (e.g., include payer names once we parse them from the images), call them out now and I’ll adjust before execution.

### User
> Our best friend from Cursor is not understanding what I mean by extracting the data from the files. Essentially, like, for example, if it is a 1099-MISC form, he has to read the form and see that it's a 1099-MISC. Then he has to understand the context, that's a tax document, and then he needs to understand that box 1 has a value, box 2 has a value, etc., and so on. And so each box may have a description and then a value. All that needs to be extracted from those documents. So essentially, each document should have a JSON or just one master JSON that has all the information. So we can pull from that. But he's not understanding me. He keeps just giving me file names and types of files.

### Assistant
> Got it—Cursor’s stuck describing files instead of **reading** them. Here’s a drop-in **extraction prompt** that forces true form detection + box-level field capture, with a strict schema and example outputs. Paste this as **Step 5 (Data Extraction)** and run it after execution/verify.
> 
> ---
> 
> ### Step 5 — **Real OCR Data Extraction (box-level, per form)**
> ```text
> You are extracting structured data from DOCUMENT IMAGES/PDFs, not listing filenames.
> 
> OPERATING MODE
> - Read each finalized file. If PDF: convert page 1 to JPEG then OCR; if confidence < 0.55 or page likely a cover, try page 2.
> - Normalize text (fix rotation, skew, and noise). Downscale long side ≤ 2500px before OCR for speed.
> - Detect form type FIRST by title/anchors, then extract fields by anchor labels + nearby values.
> 
> FORM DETECTION (exact/regex anchors)
> - 1099-MISC: /Form\s*1099[\s-]*MISC/i, “Miscellaneous Information”
> - 1099-NEC: /Form\s*1099[\s-]*NEC/i, “Nonemployee compensation”
> - W-2: /\bForm\s*W-2\b/i, “Wage and Tax Statement”
> - 1095-A: /\bForm\s*1095-A\b/i
> - I-551 (Green Card): “Permanent Resident Card”, “I-551”
> - SSA-89: /\bSSA-89\b/i
> - Driver License: state name + “Driver License”/“DLN”
> - Birth/Marriage Cert: title + registrar language (detect; set type IdentityCert)
> 
> OUTPUT REQUIREMENTS
> - Produce ONE JSON array named `records`. One object per document page actually parsed.
> - Each record follows this schema:
> 
> {
>   "doc_id": "<stable hash of source_path>",       // e.g., sha1 of path
>   "source_path": "<full path>",
>   "detected_form": "1099-MISC|1099-NEC|W-2|1095-A|SSA-89|I-551|DL|IdentityCert|TaxReturn|BankStatement|Unknown",
>   "category": "Tax|Employment|Identity|Insurance|Utilities|Financial|Legal|Photos|USCIS|Unknown",
>   "person_role": "Petitioner|Beneficiary|Joint|Unknown",
>   "tax_year": 2024|null,
>   "fields": { "<canonical_field_key>": "<value>", ... },
>   "raw_keyvals": [ {"label": "Box 1 Rents", "value": "1234.56"}, ... ],
>   "anchors_used": ["Box 1", "PAYER TIN", "RECIPIENT TIN", ...],
>   "confidence": 0.0-1.0,
>   "notes": "short remarks or uncertainties"
> }
> 
> MAPPING: CANONICAL FIELD KEYS (by form)
> - 1099-MISC fields:
>   payer_name, payer_tin, recipient_name, recipient_tin, recipient_addr, account_number,
>   box_1_rents, box_2_royalties, box_3_other_income, box_4_federal_tax_withheld,
>   box_5_fishing_boat_proceeds, box_6_medical_healthcare_payments, box_7_payer_made_direct_sales,
>   box_8_substitute_payments, box_9_crop_insurance_proceeds, box_10_gross_proceeds_attorney,
>   box_11_fish_purchased_for_resale, box_12_section_409A_deferrals,
>   box_13_excess_golden_parachute, box_14_nonqualified_deferred_comp,
>   state_1_name, state_1_id, state_1_income, state_1_tax_withheld,
>   state_2_name, state_2_id, state_2_income, state_2_tax_withheld
> - 1099-NEC fields:
>   payer_name, payer_tin, recipient_name, recipient_tin, recipient_addr, account_number,
>   box_1_nonemployee_comp, box_4_federal_tax_withheld,
>   state_1_name, state_1_id, state_1_income, state_1_tax_withheld,
>   state_2_name, state_2_id, state_2_income, state_2_tax_withheld
> - W-2 fields:
>   employee_name, employee_ssn, employer_name, employer_ein, employee_addr,
>   wages_tips_other_comp, federal_income_tax_withheld, social_security_wages,
>   social_security_tax_withheld, medicare_wages, medicare_tax_withheld,
>   ss_tips, allocated_tips, dependent_care_benefits, box12_codes, box13_statutory_employee,
>   state_1_name, state_1_id, state_1_wages, state_1_tax,
>   state_2_name, state_2_id, state_2_wages, state_2_tax, locality, local_wages, local_tax
> - 1095-A fields:
>   recipient_name, recipient_ssn, policy_number,
>   monthly_premium_A, monthly_second_lowest_cost_silver_plan_B, monthly_advance_premium_tax_credit_C  // arrays length 12
> - SSA-89 fields:
>   name, ssn, dob, reason_for_request, requestor_name, requestor_addr, date_signed
> - I-551 (Green Card):
>   name, a_number, category_code, country_of_birth, dob, sex, card_number, card_expiry, resident_since
> - Driver License (DL):
>   name, dln, address, dob, expires, issued, class
> - IdentityCert (Birth/Marriage):
>   name(s), place, date_of_event, registrar_info, certificate_number
> 
> EXTRACTION METHOD
> - Use anchor+neighborhood: find label (regex or fuzzy, case-insensitive), then capture numeric/text to the right or below within a small bounding window. Example: for “Box 1” or “1 Rents” capture the nearest numeric/money string.
> - Normalize money as decimal strings "1234.56". Normalize dates "YYYY-MM-DD" when possible.
> - If multiple candidates for one box, choose highest OCR confidence; put alternates in `notes`.
> 
> CLASSIFICATION + CONTEXT
> - `category`: Tax for 1099/W-2/1095; Identity for I-551, DL, SSN card; USCIS for I-797/EAD; Financial for bank statements; else Unknown.
> - `person_role`: infer from path/naming: PET* → Petitioner, BEN* → Beneficiary, under Joint_* → Joint; else Unknown.
> 
> MASTER JSON
> - Return a single JSON object:
> { "records": [ ...as above... ] }
> - De-duplicate by (detected_form, tax_year, person name, payer/employer if applicable); keep the record with **higher confidence**.
> 
> VALIDATION
> - If detected_form in {1099-MISC, 1099-NEC, W-2} and tax_year is null, infer from form title/year else from filename digits.
> - If no anchors found, set detected_form="Unknown", confidence ≤ 0.4, and include why in `notes`.
> 
> OUTPUT EXAMPLES (brief)
> 
> EXAMPLE 1099-MISC:
> {
>   "doc_id": "sha1:...",
>   "source_path": "…\\1099_misc_2024.jpg",
>   "detected_form": "1099-MISC",
>   "category": "Tax",
>   "person_role": "Petitioner",
>   "tax_year": 2024,
>   "fields": {
>     "payer_name": "Princess House",
>     "recipient_name": "Rosa Lucas-Esteban",
>     "recipient_tin": "XXX-XX-1234",
>     "box_1_rents": null,
>     "box_3_other_income": "1250.00",
>     "box_4_federal_tax_withheld": "0.00"
>   },
>   "raw_keyvals": [
>     {"label": "Box 3 Other income", "value": "$1,250.00"},
>     {"label": "PAYER", "value": "Princess House"}
>   ],
>   "anchors_used": ["Form 1099-MISC", "Box 3", "PAYER"],
>   "confidence": 0.92,
>   "notes": ""
> }
> 
> EXAMPLE W-2:
> {
>   "doc_id": "sha1:...",
>   "source_path": "…\\W2_GEODIS_ROSA.jpg",
>   "detected_form": "W-2",
>   "category": "Tax",
>   "person_role": "Petitioner",
>   "tax_year": 2022,
>   "fields": {
>     "employee_name": "Rosa Lucas-Esteban",
>     "employer_name": "GEODIS",
>     "wages_tips_other_comp": "28450.00",
>     "federal_income_tax_withheld": "1450.00"
>   },
>   "raw_keyvals": [
>     {"label": "1 Wages, tips, other compensation", "value": "28,450.00"},
>     {"label": "2 Federal income tax withheld", "value": "1,450.00"}
>   ],
>   "anchors_used": ["Form W-2", "Box 1", "Box 2"],
>   "confidence": 0.95,
>   "notes": ""
> }
> 
> FINAL CONFIRMATION
> - After processing all files, return ONLY:
> "📦 Master JSON file ready — review data before using."
> - And attach the single JSON object described above as your message content (no extra prose).
> ```
> 
> ---
> 
> Snap & steer: this forces Cursor to **detect the form**, **map boxes to canonical keys**, and **return one master JSON** you can actually use. After it runs, if any form keeps landing as `Unknown`, we’ll add a specific anchor for that template and re-run just those.

### User
> OK I HAVE THE WHO FILE NICE AND ORGANIZED NOW BUT THERE IS ONLY ONE ISSESUE THEY ARE NOT MAPPING BASED ON TEH THE FOLDERS THEY ARE IN, HOW DO I MAKRE SURE THAT THEY SHOW UP ON A QUARTZ MIND MAP OR OTHER SITE BUILDER BASED ON THE FOLDER THEY ARE IN.

### Assistant
> Snap & steer time: **graphs don’t care about folders** — they care about **links** and **front matter**. Quartz’s graph (and Obsidian’s) won’t auto-cluster by directory unless you give it something to chew on. Here’s the bare fix and the upgrade.
> 
> # Tier 1 — Bare fix (visible today)
> Make each folder a **hub note** and link to its children. That creates real edges, so the graph/mind map clusters by folder.
> 
> 1) In every folder, add an `index.md` (or `_index.md`/`README.md` if you use Folder Notes) with this minimal front matter:
> ```yaml
> ---
> title: "01_Joint_Documents / 01_Marriage_Financial"
> category: "01_Joint_Documents/01_Marriage_Financial"   # used by site builders/list views
> tags: [folder, 01_Joint_Documents, 01_Marriage_Financial]
> ---
> ```
> 
> 2) Under it, auto-list and **wikilink** the children:
> ```markdown
> ## Files
> - [[Certificates/1301_Marriage Certificate|Marriage Certificate (scan 1)]]
> - [[Certificates/1302_Marriage Certificate|Marriage Certificate (scan 2)]]
> - [[Joint_Accounts/BANK_20240223_...|Chase statement 2024-02-23]]
> - [[Tax_Documents/2022_Tax_Year/2022/Tax_Filings/JOINT__Tax__Return__2022__v01]]
> ```
> 
> 3) In each file’s front matter, add a **folder breadcrumb** the graph and site can group on:
> ```yaml
> ---
> folder: "01_Joint_Documents/01_Marriage_Financial/Joint_Accounts"
> category: "01_Joint_Documents/01_Marriage_Financial"
> role: "Joint"        # or Petitioner / Beneficiary
> ---
> ```
> 
> Result: Quartz graph now has edges (index → children) so your “mind map by folder” emerges instead of a random hairball.
> 
> # Tier 2 — Upgrade (auto-maintain the hubs)
> Run this tiny Python once (or whenever files change). It:
> - Adds/updates `folder`, `category`, and `role` in file front matter based on the path
> - Creates/refreshes `index.md` in each folder with wikilinks to every child
> 
> ```python
> import os, re, pathlib, yaml
> 
> ROOT = r"k:\vaults\client\rosalucas\Vault_Rosa"
> FOLDER_NOTE_NAME = "index.md"
> 
> def infer_role(path):
>     p = path.lower()
>     if "petitioner_" in p: return "Petitioner"
>     if "beneficiary_" in p: return "Beneficiary"
>     if "01_joint_documents" in p or "joint_" in p: return "Joint"
>     return None
> 
> def read_frontmatter(p):
>     try:
>         with open(p, "r", encoding="utf-8") as f:
>             text = f.read()
>         if text.startswith("---"):
>             _, fm, body = text.split("---", 2)
>             data = yaml.safe_load(fm) or {}
>             return data, body.lstrip()
>     except Exception:
>         pass
>     return {}, None
> 
> def write_frontmatter(p, data, body=""):
>     data = {k:v for k,v in data.items() if v is not None}
>     with open(p, "w", encoding="utf-8") as f:
>         f.write("---\n")
>         yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)
>         f.write("---\n\n")
>         f.write(body or "")
> 
> def ensure_folder_index(folder, links, category):
>     idx = os.path.join(folder, FOLDER_NOTE_NAME)
>     fm, body = read_frontmatter(idx)
>     title = folder.replace(ROOT, "").strip("\\/") or "Vault_Rosa"
>     fm.setdefault("title", title)
>     fm["category"] = category
>     tags = set(map(str, (fm.get("tags") or [])))
>     tags.update(["folder"])
>     fm["tags"] = sorted(tags)
> 
>     link_lines = ["## Files"] + [f"- [[{rel.replace(os.sep,'/')[:-3] if rel.endswith('.md') else rel.replace(os.sep,'/')}]]" for rel in links]
>     body_new = "\n".join(link_lines) + "\n"
>     write_frontmatter(idx, fm, body_new)
> 
> def main():
>     for dirpath, dirnames, filenames in os.walk(ROOT):
>         rel_dir = os.path.relpath(dirpath, ROOT)
>         if rel_dir == ".": rel_dir = ""
>         # Build links for this folder
>         child_links = []
>         for name in sorted(filenames):
>             if name.lower() in {"thumbs.db"}: continue
>             if name == FOLDER_NOTE_NAME: continue
>             child_links.append(name)
> 
>             # update each file's front matter
>             p = os.path.join(dirpath, name)
>             if not name.lower().endswith((".md", ".markdown")):
>                 continue
>             fm, body = read_frontmatter(p)
>             if body is None:
>                 # wrap a non-frontmatter md with fm
>                 with open(p, "r", encoding="utf-8") as f: body = f.read()
>                 fm = {}
>             fm["folder"] = rel_dir.replace("\\", "/")
>             fm["category"] = "/".join(rel_dir.split(os.sep)[:2]).replace("\\", "/") if rel_dir else ""
>             fm.setdefault("role", infer_role(p))
>             write_frontmatter(p, fm, body)
> 
>         # folder index with links
>         rel_list = child_links[:]  # only files in this folder
>         ensure_folder_index(dirpath, rel_list, "/".join(rel_dir.split(os.sep)[:2]).replace("\\","/"))
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> > Now every folder has an `index.md` linking to its contents → **graph edges**. Every file knows its `folder/category/role` → **groupable in lists**.
> 
> # Quartz & Obsidian quick toggles
> 
> - **Quartz (v4)**  
>   - Graph groups by links, not folders. Your new `index.md` notes create the needed edges.  
>   - Sidebars/collections: many site builders will group by a front matter field like `category`. Keep using `category: "<top>/<sub>"`.
> 
> - **Obsidian (nice to have)**  
>   - Install **Folder Note** (or use the built-in “Show folder note” setting) so `index.md` is visually the folder.  
>   - Dataview dashboard by folder:
>     ```dataview
>     TABLE file.name, role, category, folder
>     FROM "01_Joint_Documents"
>     WHERE contains(folder, "01_Joint_Documents")
>     SORT file.name ASC
>     ```
>   - “Mind Map” plugin will render headings/links inside your `index.md` as a map; your wikilinks make clusters.
> 
> # Sanity pings
> - If a folder should appear as one blob in the graph, **link from parent index to child indices**, not just to leaf files.  
> - If you want bigger clusters, add a short “Overview” section in each index that **links back up to the parent**. Cycles strengthen cluster cohesion in the graph.
> 
> Finish line: run the script, commit, and re-build Quartz. You’ll see your folders snap into tight clusters like good little galaxies.

### User
> IS THERE ANOTHER SITE BUILDER YOU RECOMMEND FOR THIS OR IT QUARTS TEH BEST FOR FUNTION AND LOOKS.

### Assistant
> Short answer: **Quartz is the best free “notes → site with graph”**. If you want a more polished, docs-style portal (table-of-contents, tabs, killer search) and can live **without** a graph, go **Material for MkDocs** or **Astro Starlight**. If you want zero setup and a built-in graph and don’t mind paying, **Obsidian Publish** is the smoothest.
> 
> Here’s the snap verdict:
> 
> - **Quartz** — Free, Obsidian-friendly, has global/local **graph view** out of the box. Great for your hub-notes + wikilink clusters you’re building. citeturn0search15turn0search0  
> - **Obsidian Publish** — Push button deploy, **graph + full-text search**, $8/mo per site. If you need “it just works,” this is it. citeturn0search11turn0search1  
> - **Material for MkDocs** — Enterprise-clean docs site, **excellent built-in search**, deep nav and tags. No native graph. Ideal for client-facing evidence portals. citeturn0search12turn0search2turn0search7  
> - **Astro Starlight** — Modern, fast, accessible docs theme; easy theming. No graph, but gorgeous for structured guides/dashboards. citeturn0search4turn0search19turn0search9  
> - **Docusaurus** — If you ever need **versioning** (e.g., case playbooks by year) and a React stack. No graph; heavier lift. citeturn0search18turn0search8turn0search13
> 
> ### My call for your use case (immigration files + mind-map vibe)
> - **Keep Quartz** for the **graph-by-links** clustering you want. You already added folder hub notes—perfect. Quartz’s graph actually renders those edges; folders alone don’t. citeturn0search15  
> - If you need a **client-polished portal** (sidebars, faceted search, “just the docs” look), spin a **second build** with **MkDocs Material** fed from the same vault (or an export). It’ll give you fast offline search and clean navigation for attorneys/clients, while Quartz remains your thinking space. citeturn0search12
> 
> ### Quick setup nudge
> - **Quartz**: stick with your `index.md` hub pages + front matter (`category`, `folder`, `role`). That’s what the graph uses indirectly—via links. citeturn0search15  
> - **MkDocs Material**: map those same folders to **nav** in `mkdocs.yml` and let the built-in search handle the rest. Tags/categories are first-class and snappy. citeturn0search2turn0search12  
> - **Obsidian Publish**: if you ever want the easiest path with graph, it’s paid but one-click and includes graph/search. citeturn0search11
> 
> If you want, I’ll give you a minimal **mkdocs.yml** that mirrors your `01_Joint_Documents / 00_Individual_Documents` structure and respects your `category` front matter—so you can trial a Material build alongside Quartz without touching your vault.
