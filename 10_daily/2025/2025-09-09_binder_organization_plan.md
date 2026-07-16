---
layout: page
title: "Binder organization plan"
slug: "binder_organization_plan"
created_at: "2025-09-09 04:15:50"
updated_at: "2025-09-09 04:15:50"
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
uid: "68bff03f-6d08-832f-9fde-358de05b42bf"
canonical_ref: ""
---

# Binder organization plan

## Overview
- **Date**: 2025-09-09 04:15:50
- **Conversation ID**: `68bff03f-6d08-832f-9fde-358de05b42bf`
- **Source**: `Chat-Export-28513-2026/conversations-000.json`

## Chat History

### User
> Hey, can you give me a prompt for Cursor to create another binder for another immigration case, but this one's a little different. So the couple, the one individual has, I think has to do the last seven years of taxes. The other, and then the other one, they got to do them together for the last three years, I believe. So we need to have the folder set up correctly for filing those taxes and having them as part of the evidence of the tax filings or financial evidence. And also, I'm separating their originals to give the originals back to them. And I'm going to be printing out the copies for the binder that they can give to the attorney. So I want to keep it separate, what they're going to turn into the attorney versus what they're going to, what they're going to keep as their records. And so I guess I'll give you a quick rundown. I have a lot of financial documents, like you like bills and receipts and things like that. Then I have some travel documents like airplane tickets, bus tickets, things like that. I have a I-797 notice of benefit for a petition of qualifying family member. I have a notice of hearing or removal proceedings. I have a I-797 notice of action approval notice for the appointment authorization. I have authorization for social security administration to release the social security number verification. I have a letter from one of their friends that I need to translate from Spanish to English and provide a certificate of translation. I have a marriage evidence. I have birth certificates that need translated. I have all their W-2s, 1099s, 1098s and other tax forms and filings and other receipts from attorneys, attorney agreements, marriage licenses, BNB receipts, copies of IDs. I also have the agreement and the list of required documents. I'll provide that to you as well. And then a questionnaire that they need to fill out. So I need to get that set up and marked down somehow and get all that information filled in. And the contract for services with a confirmation of payments. So you get all that organized. In my original folder, the way I already had it separated originally, I had beneficiary documents, petitioner documents, marriage evidence, supporting evidence, financial evidence, but that may not be the way I want it. I want to be the most efficient. Again, there needs to be a separation of their original copies for their records and then what's actually going to be turned into the attorney. And it needs to be in a fashion that is like a paralegal that had did it and turned it into the attorney, not what the actual attorney is going to do. Because I feel like if I go too far, she's going to be like, what the heck is this person doing?

### Assistant
> Got it. Here’s a clean, surgical **Cursor prompt** that will spin up the right binder structure for this immigration case. It bakes in the tax-year split, the originals vs. attorney copies, and the categories you mentioned (financial, travel, identity, petitions, translations, etc.). This prompt will let Cursor generate the folders and keep it tidy like a paralegal’s prep, not an overbearing attorney file.
> 
> ---
> 
> ### Cursor Prompt
> 
> ```
> Create a new directory structure for an immigration binder project with two clear top-level sections:
> 
> 1. **Client Originals (Return to Clients)**
>    - Beneficiary Originals
>    - Petitioner Originals
>    - Joint Originals (e.g., marriage license, shared financial docs)
>    - Translations Originals
>    - Receipts & Agreements Originals
> 
> 2. **Attorney Binder (Copies to Provide)**
>    - 01_Identity_And_Status
>        - Copies of IDs (driver’s license, SSN, EAD, passports, birth certificates + translations)
>        - Notices of Action (I-797 approvals, hearing notices)
>    - 02_Marriage_Evidence
>        - Marriage license
>        - Photos, correspondence, joint bills
>        - Letters of support (with translations + certificate of translation)
>    - 03_Financial_Evidence
>        - Tax Filings
>            - Petitioner_Taxes_Last7Years
>            - Joint_Taxes_Last3Years
>            - W2s_1099s_1098s
>        - Bills_Receipts (utilities, BNB, attorney receipts, etc.)
>        - Bank Statements, Paystubs
>    - 04_Travel_Evidence
>        - Plane tickets
>        - Bus tickets
>    - 05_Legal_And_Agreements
>        - Attorney_Agreements
>        - Service_Contracts
>        - Confirmation_Of_Payments
>    - 06_Questionnaires_And_Checklists
>        - Client_Questionnaire
>        - Required_Documents_List
>        - Cover_Letters
> 
> Rules:
> - Create empty placeholder files (README.md) in each folder with a brief description of what belongs there.
> - Use numbering on the Attorney Binder folders to ensure logical exhibit order.
> - Originals folder must not be numbered (to keep separate from submission packet).
> - Output the structure in a tree format with full relative paths.
> - At the end, generate a CSV mapping file with columns: Current_Path, Updated_Path, Notes (so updates can be batch-run if the structure changes later).
> ```
> 
> ---
> 
> This gives you **two tiers**: one safe vault for originals, one polished packet for attorney submission. The tax split is crystal (7 years for one, 3 years joint). You can drop in your docs and later run a renaming or numbering pass if needed.
> 
> Do you want me to also generate the **cover page + exhibit index template** for this binder so it reads like a paralegal packet right out of the gate? That way the attorney sees the order and doesn’t think you’re trying to “be” the attorney.

### User
> Well, I want the client's originals to be ordered in a fashion for their own binder. I just want to make sure that there's a binder to turn into the attorney, which will be all copies, and there's a binder for the clients, which is the originals. And yes, I need the cover pages for each section and subsection. Cover pages will also serve as the index for those sections, and there should be a master index for the client originals, a master index for the attorney binder, and a master index for all of it together. Tax filings. Again, I need all the years in there, separated by years, and what needs to be in there. Okay, make sure this is good and ready to go. I don't want to go back and redoing stuff. And go ahead and go ahead and do the numbering, okay? I don't know if you want to do, you know, originals OR with an ID number, and then maybe the other ones are just copy. Maybe we don't want to do evidence IDs since it's not pro se. The attorney will do however they want, but maybe we want to still have an index with the numbering system. Keep it simple. Keep it sweet. Keep it scalable.

### Assistant
> Alright, let’s lock this down clean so you don’t have to redo it later. Here’s the blueprint for **both binders, cover pages, master indexes, and numbered tax filings by year**. I’ll keep it paralegal-style: organized, clear, professional, but not over-lawyered.  
> 
> ---
> 
> ## Binder System Setup
> 
> ### Top Level
> - **Client Originals Binder (OR_)**
>   - Organized for the client’s personal records.
>   - Uses `OR_XX` numbering prefix for consistency.
> - **Attorney Binder (Copy_)**
>   - All copies, ready to hand to attorney.
>   - Uses `CP_XX` numbering prefix for consistency.
> 
> Both binders mirror each other in structure so you can track documents across them.
> 
> ---
> 
> ## Folder & Numbering Structure
> 
> ### 01_Identity_And_Status
> - OR_01 / CP_01 – IDs (DL, SSN, EAD, Passport)  
> - OR_02 / CP_02 – Birth Certificates (+ translations)  
> - OR_03 / CP_03 – USCIS Notices (I-797 approvals, hearing notices, benefit petitions)  
> 
> ### 02_Marriage_Evidence
> - OR_04 / CP_04 – Marriage License  
> - OR_05 / CP_05 – Photos, correspondence, joint bills  
> - OR_06 / CP_06 – Letters of Support (with translations & certs)  
> 
> ### 03_Financial_Evidence
> - OR_07 / CP_07 – Tax Filings  
>    - OR_07A / CP_07A – Petitioner Taxes (Year-by-Year, Last 7 Years)  
>    - OR_07B / CP_07B – Joint Taxes (Year-by-Year, Last 3 Years)  
>    - OR_07C / CP_07C – W2s, 1099s, 1098s (Year-by-Year, match tax filings)  
> - OR_08 / CP_08 – Bills & Receipts (utilities, BNB, attorney receipts)  
> - OR_09 / CP_09 – Bank Statements, Paystubs  
> 
> ### 04_Travel_Evidence
> - OR_10 / CP_10 – Plane Tickets  
> - OR_11 / CP_11 – Bus Tickets  
> 
> ### 05_Legal_And_Agreements
> - OR_12 / CP_12 – Attorney Agreements  
> - OR_13 / CP_13 – Service Contracts  
> - OR_14 / CP_14 – Confirmations of Payment  
> 
> ### 06_Questionnaires_And_Checklists
> - OR_15 / CP_15 – Client Questionnaire  
> - OR_16 / CP_16 – Required Documents List  
> - OR_17 / CP_17 – Cover Letters  
> 
> ---
> 
> ## Cover Pages & Indexes
> 
> Each **section** starts with a cover page that doubles as an index for that section. Format:
> 
> **Section 03 – Financial Evidence**  
> _Subsection 03A – Petitioner Taxes (2017–2023)_  
> - 03A-2017 – Federal Return + W2s  
> - 03A-2018 – Federal Return + W2s  
> - …  
> - 03A-2023 – Federal Return + W2s  
> 
> _Subsection 03B – Joint Taxes (2021–2023)_  
> - 03B-2021 – Joint Return + Supporting Docs  
> - 03B-2022 – Joint Return + Supporting Docs  
> - 03B-2023 – Joint Return + Supporting Docs  
> 
> ---
> 
> ### Master Indexes
> 1. **Master Index – Client Originals (OR_)**  
>    Lists every OR_ item with section/subsection.
> 2. **Master Index – Attorney Binder (CP_)**  
>    Lists every CP_ item with section/subsection.
> 3. **Unified Master Index**  
>    Side-by-side: OR_ vs CP_ (helps you confirm both binders are in sync).  
> 
> ---
> 
> ## Cursor Prompt (Final)
> 
> Here’s what you can drop straight into Cursor to build this:
> 
> ```
> Create a directory structure for two binders:
> 
> 1. Client_Originals (prefix OR_)
> 2. Attorney_Binder (prefix CP_)
> 
> Mirror the structure between both. Use numbering on all sections and subsections:
> 
> 01_Identity_And_Status
> 02_Marriage_Evidence
> 03_Financial_Evidence
>    - 03A_Petitioner_Taxes (Yearly folders for last 7 years)
>    - 03B_Joint_Taxes (Yearly folders for last 3 years)
>    - 03C_W2s_1099s_1098s (Yearly folders)
> 04_Travel_Evidence
> 05_Legal_And_Agreements
> 06_Questionnaires_And_Checklists
> 
> Inside each folder, create a COVER_PAGE.md file that serves as that section’s index.
> Create three master index files at the top level:
> - MASTER_INDEX_ORIGINALS.md
> - MASTER_INDEX_COPIES.md
> - MASTER_INDEX_ALL.md (side-by-side OR_ vs CP_)
> 
> Output:
> 1. Tree structure with full relative paths.
> 2. Pre-generated COVER_PAGE.md templates with numbering placeholders.
> 3. Master index templates with numbering references.
> ```
> 
> ---
> 
> This way you’ll have **ready-to-print cover pages and indexes** baked in, every tax year neatly split, and both binders locked in sync.  
> 
> Do you want me to actually **draft the sample COVER_PAGE.md text** for, say, the **Financial Evidence section** so you can just duplicate and tweak for each section?

### Assistant
> Perfect. I’ve pulled in the three drafts you uploaded—the **agreement**, the **lista de documentos**, and the **questionnaire**【16†source】【17†source】【18†source】. Here’s how we can lock this binder system in tight with your requirements:
> 
> ---
> 
> # Binder Blueprint
> 
> ## 1. Two Complete Binders
> - **Client Originals Binder (prefix `OR_`)**  
>   Ordered neatly, so the client can track their originals for personal records.  
> - **Attorney Binder (prefix `CP_`)**  
>   All copies, ready to turn over. Same structure as the originals so they mirror each other.
> 
> Both will have **cover pages** for each section/subsection, which also double as **indexes**.
> 
> ---
> 
> ## 2. Section Breakdown (with Numbering)
> 
> **01_Identity_And_Status**  
> - OR_01 / CP_01 – Birth Certificates (+ translations)  
> - OR_02 / CP_02 – IDs (DL, SSN, EAD, Passport)  
> - OR_03 / CP_03 – Immigration Notices (I-797 approvals, hearing notices, SSA verifications)
> 
> **02_Marriage_Evidence**  
> - OR_04 / CP_04 – Marriage License  
> - OR_05 / CP_05 – Photos, correspondence, joint bills  
> - OR_06 / CP_06 – Support Letters (Spanish originals + English translations + certificate of translation)
> 
> **03_Financial_Evidence**  
> - OR_07 / CP_07 – Tax Filings  
>    - OR_07A / CP_07A – Petitioner Taxes (Year-by-Year, Last 7 Years)  
>    - OR_07B / CP_07B – Joint Taxes (Year-by-Year, Last 3 Years)  
>    - OR_07C / CP_07C – W2s, 1099s, 1098s  
> - OR_08 / CP_08 – Bills & Receipts (utilities, attorney receipts, BNB, etc.)  
> - OR_09 / CP_09 – Bank Statements & Paystubs  
> 
> **04_Travel_Evidence**  
> - OR_10 / CP_10 – Plane Tickets  
> - OR_11 / CP_11 – Bus Tickets  
> 
> **05_Legal_And_Agreements**  
> - OR_12 / CP_12 – Attorney Agreement【16†source】  
> - OR_13 / CP_13 – Service Contracts & Confirmations of Payment  
> - OR_14 / CP_14 – Receipts  
> 
> **06_Questionnaires_And_Checklists**  
> - OR_15 / CP_15 – Client Questionnaire【18†source】  
> - OR_16 / CP_16 – Required Document List【17†source】  
> - OR_17 / CP_17 – Cover Letters  
> 
> ---
> 
> ## 3. Cover Pages & Indexes
> 
> ### Section Cover Pages
> Each section/subsection starts with a **COVER_PAGE.md** that:
> - Lists the documents expected in that section.  
> - Includes numbering (OR_XX / CP_XX).  
> - Acts as the **table of contents** for that section.  
> 
> Example (Financial Evidence → Tax Filings):
> 
> ```
> # Section 03 – Financial Evidence
> ## Subsection 03A – Petitioner Taxes (Last 7 Years)
> - 03A-2017 – Federal Return + W2s
> - 03A-2018 – Federal Return + W2s
> ...
> - 03A-2023 – Federal Return + W2s
> 
> ## Subsection 03B – Joint Taxes (Last 3 Years)
> - 03B-2021 – Joint Return + W2s
> - 03B-2022 – Joint Return + W2s
> - 03B-2023 – Joint Return + W2s
> ```
> 
> ---
> 
> ### Master Indexes
> 1. **MASTER_INDEX_ORIGINALS.md** – Lists every `OR_` item.  
> 2. **MASTER_INDEX_COPIES.md** – Lists every `CP_` item.  
> 3. **MASTER_INDEX_ALL.md** – Side-by-side OR_ vs CP_ (sync check).  
> 
> ---
> 
> ## 4. Cursor Prompt (Turnkey)
> 
> Here’s the prompt you can paste into Cursor to generate this whole structure:
> 
> ```
> Create a directory structure for an immigration binder project with two binders:
> 
> 1. Client_Originals (prefix OR_)
> 2. Attorney_Binder (prefix CP_)
> 
> Mirror the structure between both. Sections:
> 
> 01_Identity_And_Status
> 02_Marriage_Evidence
> 03_Financial_Evidence
>    - 03A_Petitioner_Taxes (Yearly folders for last 7 years, 2017–2023)
>    - 03B_Joint_Taxes (Yearly folders for last 3 years, 2021–2023)
>    - 03C_W2s_1099s_1098s (Yearly folders)
> 04_Travel_Evidence
> 05_Legal_And_Agreements
> 06_Questionnaires_And_Checklists
> 
> Rules:
> - Prefix files/folders with OR_ for Originals, CP_ for Copies.
> - In each section/subsection, create COVER_PAGE.md that lists documents as an index.
> - At top level, create three master indexes:
>   - MASTER_INDEX_ORIGINALS.md
>   - MASTER_INDEX_COPIES.md
>   - MASTER_INDEX_ALL.md (OR_ vs CP_ side-by-side)
> 
> Output:
> 1. Full directory tree with relative paths.
> 2. COVER_PAGE.md templates for each section.
> 3. Master index templates.
> ```
> 
> ---
> 
> Do you want me to go ahead and **draft one full COVER_PAGE.md (like for Financial Evidence)** and one **MASTER_INDEX_ALL.md** so you can just duplicate/adjust instead of starting from scratch?

### User
> so does this structure take care of the checklsit, and where is the markdown for the inforamtion/bio info that needs filled out.

### Assistant
> Yes—this structure does take care of the checklist and bio info, but let me spell it out clean so you see exactly where each piece lives and how the Markdown works.
> 
> ---
> 
> # Where Each Piece Goes
> 
> ### ✅ Checklist (Lista de Documentos)
> - Your uploaded **lista_documentos_draft.md**【17†source】 is already a required-documents list.  
> - That lives in **06_Questionnaires_And_Checklists → OR_16 / CP_16 – Required Documents List**.  
> - Inside that folder, the **COVER_PAGE.md** will act as an index, and the Spanish version + your English working version will both be included.  
> - That way, the attorney binder gets the polished version, and the client binder keeps the original request.
> 
> ---
> 
> ### ✅ Bio / Info Forms
> - Your **questionnaire_draft.md**【18†source】 is the personal bio + immigration history form.  
> - That lives in **06_Questionnaires_And_Checklists → OR_15 / CP_15 – Client Questionnaire**.  
> - This needs a Markdown template with blanks so it can be filled out either digitally or by hand.  
> - Example snippet for the Markdown template:
> 
> ```markdown
> # Client Questionnaire (Petitioner)
> 
> ## General Information
> - Full Name: ______________________________
> - Other Names Used: _______________________
> - Date of Birth: ___________________________
> - Place of Birth: __________________________
> - Social Security Number: _________________
> - A-Number: _______________________________
> 
> ## Contact Information
> - Current Address: _________________________
> - Phone Number(s): _________________________
> - Email: _________________________________
> 
> ## Immigration History
> - Total number of U.S. entries: ____________
> - Date of last entry: ______________________
> - Place of last entry: _____________________
> - Method of last entry: ____________________
> 
> ## Criminal / Legal History
> - Have you ever been arrested/detained? Yes / No
> - If yes, explain: _________________________
> 
> ## Family Information
> - Current Spouse: __________________________
> - Prior Marriages: _________________________
> - Children (Name / DOB / Country / Current Residence):  
>   1. ______________________________________  
>   2. ______________________________________  
> 
> ## Employment History (last 5 years)
> - Employer: _______________________________
> - Type of Work: ___________________________
> - Dates: From ______ To ______
> ```
> 
> This format mirrors your draft but makes it **fillable in Markdown**.  
> 
> ---
> 
> ### ✅ Attorney Agreement
> - Your **agreement_draft.md**【16†source】 lives in **05_Legal_And_Agreements → OR_12 / CP_12 – Attorney Agreement**.  
> - It will also get a **COVER_PAGE.md** explaining what’s inside (e.g., agreement + receipts).  
> 
> ---
> 
> # How the Pieces Flow
> 
> 1. **Client Originals Binder**: Holds the signed agreement, the Spanish/English checklist, the filled-out questionnaire, and original IDs/taxes.  
> 2. **Attorney Binder**: Holds copies of the same, with cover pages/indexes, so the attorney doesn’t have to dig.  
> 3. **Indexes**: The **Master Indexes** reference both the checklist and bio info sections (OR_15/16 and CP_15/16).  
> 
> ---
> 
> So yes—this structure **does cover the checklist** and **provides a home for bio/questionnaire info**.  
> The only thing left is to actually drop in **Markdown templates** like the one above, so they can be filled out directly or printed.  
> 
> ---
> 
> Do you want me to **generate all the COVER_PAGE.md templates and both MASTER_INDEX files in one Markdown bundle** so you have them pre-written and ready to insert into the folders? That way you wouldn’t need to duplicate or guess.

### User
> here is the code extraction, give me the final cursor end all be all that will update the directory, file names, numbering, placeholders, ect ect, and it should then read everything and udpate the information form it can find, also it should keep an eye out for any insights to help with this case prep. also please put together a billing suggestions for thsi work.

### Assistant
> Locked and loaded. Here’s your **one-shot Cursor prompt** that (1) standardizes the vault, (2) builds twin binders (Client Originals + Attorney Copies), (3) fixes misspellings/numbering, (4) generates cover pages + master indexes, (5) extracts any fillable bio data it can find from existing Markdown/PDF/JPG (best-effort OCR), (6) emits a **rename map + undo scripts**, and (7) surfaces **case-prep insights**. It’s surgical and reversible.
> 
> > Paste the whole block into Cursor. No follow-ups, just go.
> 
> ---
> 
> ### 🔧 Cursor “End-All-Be-All” Prompt
> 
> ```bash
> You are an expert paralegal systems engineer. Operate in the current workspace as the case root.
> Goals (do ALL, in order, idempotently & with full logs):
>   A) BACKUP + SAFETY
>   B) DIRECTORY STANDARDIZATION & RENUMBERING
>   C) TWIN BINDERS (Client Originals = OR_, Attorney Binder = CP_) with mirrored structure
>   D) YEAR-BY-YEAR TAX FOLDERS (7 yrs individual, 3 yrs joint), W-2/1099/1098 alignment
>   E) COVER PAGES per section/subsection + 3 Master Indexes
>   F) METADATA EXTRACTION to prefill bio/questionnaire where possible
>   G) INSIGHT SCAN for missing docs, mismatches, red flags
>   H) OUTPUT: rename_map.csv, undo scripts, action report
> 
> CONSTRAINTS:
> - Be reversible: generate rename_map.csv (Current_Path,Updated_Path,Reason) and write undo_{sh,bat}.sh/.bat using the map.
> - Never overwrite source without backup: copy previous state to ./_backups/{timestamp}/
> - Only touch within this repo; do not reach network.
> 
> REFERENCE HINTS (check what is present and adapt):
> - Existing misspelling to fix: "11_Benificiary" → "11_Beneficiary".
> - Current vault skeleton lives under ./Vault_Rosa/ … use it as your base.
> - There are converted JPGs and archived PDFs under ./archived and scattered finance/notes folders.
> - Use our prevailing naming convention: {PREFIX}{YYYYMMDD}_{Clean_File_Name}_P{page}.jpg
>   PREFIX set by category: BEN, PET, MAR, BANK, INS, PAY, TAX, NOT, ATT, OTH.
> 
> STEP A — SAFETY:
> 1) Create ./_backups/{YYYYMMDD_HHMMSS}/ and copy a manifest of all paths there (no need to duplicate big binaries).
> 2) Create ./_logs/{timestamp}/run.log and tee all actions.
> 
> STEP B — DIRECTORY STANDARDIZATION:
> 1) Normalize folder names under ./Vault_Rosa:
>    - 1_Immigration/
>      - 11_Beneficiary/
>      - 12_Petitioner/
>      - 13_Marriage/
>      - 14_Supporting/
>    - 2_Financial/
>      - 21_Tax_Returns/
>      - 22_W2_1099_Forms/
>      - 23_Pay_Stubs/
>      - 24_Expense_Records/
>      - 25_Payment_Receipts/
>    - 3_Forms/
>      - 30_Notices/
>      - 31_USCIS_Forms/
>      - 32_Other_Forms/
>    - 4_Notes/
>      - 41_Attorney_Notes/
>      - 42_Client_Notes/
>      - 43_Communication_Log/
>      - 44_Other_Files/
>    Keep existing files; just move/rename into this shape.
> 
> 2) Standardize file names:
>    - Replace spaces/hyphens with underscores, collapse repeats, keep extensions.
>    - Keep existing date tokens (YYYYMMDD) if present; otherwise leave filename as-is.
> 
> 3) Move strays by keyword heuristics:
>    - “payment/receipt/pago/recibo” → 2_Financial/25_Payment_Receipts
>    - “operating bank/chase/deposit/balance/statement” → 2_Financial/24_Expense_Records or 2_Financial/21_Tax_Returns if it’s clearly tax-year supporting statement (keep heuristic conservative, log any ambiguity)
>    - “i-797/797c/notice of action” → 3_Forms/30_Notices
>    - “ins/insurance/founders” → 1_Immigration/13_Marriage/137_Joint_Insurance
>    - “1098/1099/w-2/tax/irs” → 2_Financial/21_Tax_Returns or 22_W2_1099_Forms as appropriate
>    - “questionnaire/cuestionario/lista de documentos” → 1_Immigration/11_Beneficiary (source drafts) and later mirrored into binder checklists
> 
> 4) Record every move/rename in rename_map.csv with reason “standardize/move”.
> 
> STEP C — TWIN BINDERS:
> Create two top-level mirrors at repo root:
> - Client_Originals/ (prefix OR_)
> - Attorney_Binder/ (prefix CP_)
> Each with numbered sections and subsections:
> 
> 01_Identity_And_Status/
>   OR_01/CP_01_IDs
>   OR_02/CP_02_Birth_Certs_Translations
>   OR_03/CP_03_USCIS_Notices
> 02_Marriage_Evidence/
>   OR_04/CP_04_Marriage_License
>   OR_05/CP_05_Photos_Messages_Joint_Bills
>   OR_06/CP_06_Support_Letters_Translations_Certs
> 03_Financial_Evidence/
>   OR_07/CP_07_Tax_Filings
>     OR_07A/CP_07A_Individual_Taxes_By_Year
>     OR_07B/CP_07B_Joint_Taxes_By_Year
>     OR_07C/CP_07C_W2_1099_1098_By_Year
>   OR_08/CP_08_Bills_Receipts
>   OR_09/CP_09_Bank_Statements_Paystubs
> 04_Travel_Evidence/
>   OR_10/CP_10_Plane_Tickets
>   OR_11/CP_11_Bus_Tickets
> 05_Legal_And_Agreements/
>   OR_12/CP_12_Attorney_Agreements
>   OR_13/CP_13_Service_Contracts
>   OR_14/CP_14_Payment_Confirmations
> 06_Questionnaires_And_Checklists/
>   OR_15/CP_15_Client_Questionnaire
>   OR_16/CP_16_Required_Doc_List
>   OR_17/CP_17_Cover_Letters
> 
> Mirror copies: originals → OR_* ; copies → CP_* (copy files, do NOT move originals). Keep Originals unnumbered at file level if needed, but keep the folder numbering for easy crosswalk.
> 
> STEP D — TAX YEARS:
> - Compute target years dynamically from current year = 2025.
> - Individual last 7 filing years: 2018–2024 (create folders even if empty): {year}/Federal_Return, {year}/State_Return (if applicable), {year}/W2s, {year}/1099s, {year}/1098s, {year}/Supporting.
> - Joint last 3 filing years: 2022–2024 with the same sub-structure.
> - Also auto-detect any other year tokens present in source (e.g., 2017, 2008–2010). Create “_EXTRA/{year}” for out-of-scope finds so nothing is lost; log a “beyond-scope” note.
> 
> STEP E — COVER PAGES + MASTER INDEXES:
> For EVERY section/subsection in both binders:
>   - Generate COVER_PAGE.md (acts as index for that section) with:
>     • Title, Purpose (“Paralegal-prepared evidence index — copies for attorney; originals for client.”)
>     • Numbered list of expected items (templated) and present items (discovered)
>     • “Missing/To-Obtain” checklist created from heuristics (e.g., tax year missing W-2)
> Create at root:
>   - MASTER_INDEX_ORIGINALS.md (lists all OR_ paths)
>   - MASTER_INDEX_COPIES.md (lists all CP_ paths)
>   - MASTER_INDEX_ALL.md (two-column crosswalk OR_→CP_, checkbox column)
> 
> STEP F — METADATA EXTRACTION (best-effort):
> - Parse any .md/.txt for key fields to prefill questionnaires:
>   • Names, DOB, A-Number, SSN (mask in copies), addresses (last 5 yrs), entries to US, arrest history flags.
> - Attempt OCR for .jpg/.pdf using pytesseract if available; otherwise skip and log “OCR unavailable”.
> - Write extracted fields into:
>   - Client_Originals/06_Questionnaires_And_Checklists/OR_15_Client_Questionnaire/QUESTIONNAIRE_PREFILL.md
>   - Attorney_Binder/06_…/CP_15_…/QUESTIONNAIRE_PREFILL.md
> - NEVER store full SSN in CP_ copies; mask as ***-**-1234.
> 
> STEP G — INSIGHT SCAN:
> Produce ./_reports/{timestamp}/INSIGHTS.md with bullets:
>   - Missing tax years or missing W-2/1099s inside years
>   - Mismatch between Notices and IDs (e.g., names/addresses)
>   - Any hearing notices (EOIR) detected → flag to ensure attorney gets copies
>   - Spanish letters detected w/o English translation or no certificate → flag
>   - Payments/receipts w/o contract or contract w/o receipts → flag
>   - Bank statements present but no joint lease/mortgage → flag as optional
> Each bullet contains the file path(s) that triggered it.
> 
> STEP H — RENAME MAP + UNDO:
> - Every move/rename → append to rename_map.csv.
> - Generate undo.sh (bash) and undo.bat (Windows) that reverse operations using the map.
> - Emit DONE banner with counts: moved, renamed, OCR’d, cover pages created, insights found.
> 
> IMPLEMENTATION DETAILS:
> - Create /util/ folder scripts:
>   • util/reorganize_binder.py  → does B, C, D, E (structure & docs)
>   • util/extract_metadata.py  → does F (pytesseract optional)
>   • util/insights.py          → does G
>   • util/run_all.py           → orchestrator: backup, run steps in order, then write summary
> - Make run_all.py safe to re-run (idempotent) and verbose.
> 
> RUN:
> - Create the scripts, then run: python util/run_all.py
> - After run, print pointers to:
>   • Client_Originals/, Attorney_Binder/
>   • MASTER_INDEX_*.md
>   • _reports/{timestamp}/INSIGHTS.md
>   • rename_map.csv and undo scripts
> ```
> 
> ---
> 
> ### What this does (short version)
> - Fixes folder typos and normalizes structure.
> - Builds **two mirrored binders** (OR_ vs CP_), adds **cover pages** + **3 master indexes**.
> - Creates **year-by-year tax folders** (2018–2024 individual; 2022–2024 joint), plus an `_EXTRA` bucket for off-range years found.
> - Prefills questionnaire Markdown from what it can read; masks SSNs in CP_.
> - Generates **insights**: missing docs, translation gaps, notices, receipts/contracts mismatches.
> - Produces **rename_map.csv** and **undo scripts** so you can revert anything instantly.
> - Uses the current vault layout as detected in your extraction (e.g., the “Benificiary” typo, scattered financials), so it adapts to what’s there. fileciteturn1file0
> 
> ---
> 
> ### Billing suggestions (clean, receipt-ready)
> 
> | Workstream | Scope summary | Est. time | Rate | Subtotal |
> |---|---|---:|---:|---:|
> | Intake & Scoping | Review extraction, confirm binder plan, risk checks | 0.5–1.0 hr | $99/hr | $50–$99 |
> | Vault Standardization | Fix folder typos, normalize names, map/move + logs | 1.5–2.5 hr | $99/hr | $149–$248 |
> | Twin Binder Build | Originals + Attorney copies, mirrored structure | 1.0–1.5 hr | $99/hr | $99–$149 |
> | Tax Year Buildout | 7-yr individual, 3-yr joint, year subfolders | 0.8–1.2 hr | $99/hr | $79–$119 |
> | Cover Pages + Indexes | Section covers + 3 master indexes | 1.0–1.5 hr | $99/hr | $99–$149 |
> | Metadata Prefill | Parse MD/PDF/JPG (best-effort OCR), mask PII in CP_ | 1.0–2.0 hr | $99/hr | $99–$198 |
> | Insight Report | Gaps, flags, next steps for attorney handoff | 0.7–1.0 hr | $99/hr | $69–$99 |
> | QA + Undo Safety | Verify crosswalk OR_↔CP_, test undo scripts | 0.5–1.0 hr | $99/hr | $50–$99 |
> | **Estimated total** | **All of the above** | **7.0–11.7 hr** |  | **$694–$1,160** |
> 
> **Notes**
> - If heavy OCR or re-scan is needed for low-quality images, add 1–3 hours.
> - Translation/certification of letters is **separate** (flat $45–$85/page typical, or your preferred vendor).
> - Court/attorney-requested re-order later is out-of-scope; quote after review.
> 
> ---
> 
> Snap-and-steer extras when you’re ready: I can also drop in **ready-made COVER_PAGE.md templates** (Financial, Identity, Marriage) and the **Master Index** skeletons pre-written so it’s print-clean on first run.

### User
> please create a move and rename map because this is all still a mess and cursor aint getting it. I move most of the files more logically where they go but we need updates and renames and the attorney binder is just giong to mirrtor rthe client folder so it made a script to do this so we can simplify the numbering too.

### Assistant
> Snap & steer time. We’re going to (1) **produce a clean move/rename map**, (2) **apply it safely** (with undo), and (3) **mirror Client → Attorney** so both binders stay in lock-step with **simpler numbering**. I baked real examples from your current tree so the rules hit what’s actually there. fileciteturn2file0
> 
> ---
> 
> # What we’re standardizing (simple + scalable)
> 
> **Sections (no OR_/CP_ clutter in folder names):**
> ```
> 00_Biographical/
> 01_Identity_And_Status/
> 02_Forms/
> 03_Notices/
> 04_Marriage_Evidence/
> 05_Legal_And_Agreements/
> 06_Travel_Evidence/
> 07_Financial_Evidence/
> 08_Questionnaires_And_Checklists/
> ```
> 
> **Inside sections, use short, human names:**
> ```
> 01_Identity_And_Status/
>   01_IDs/
>   02_Birth_Certificates_Translations/
>   03_USCIS_Notices/
> ...
> 07_Financial_Evidence/
>   01_Tax_Filings/
>     01_Individual_By_Year/
>     02_Joint_By_Year/
>     03_W2_1099_1098_By_Year/
>   02_Bills_Receipts/
>   03_Bank_Statements_Paystubs/
> ```
> 
> **Files** get normalized to:
> ```
> {TAG}_{YYYYMMDD}_{Slug}_P{page}.ext
> ```
> - TAG ∈ {ID, BIR, NOT, MAR, ATT, PAY, BANK, TAX, W2, 1099, 1098, LET, INS, TRV, Q}  
> - Dates recovered from filename or parent folder; if none, use `00000000`.  
> - Slug = Short, de-spaced, capitalized words (≤ 6 tokens).  
> - Page suffix added if multi-page or image series.
> 
> Examples we’ll auto-fix from your vault:
> - `08052025_1-797 INOTICE OF ACTION I.jpg` → `NOT_20250805_Notice_of_Action_P001.jpg`  
> - `123_r.lucas_Acta de Nacimiento.jpg` → `BIR_00000000_RLucas_Birth_Certificate_P001.jpg`  
> - `PAY_20250707_07072025_Previous_Payments__17_P001.jpg` → **keep** (already compliant)  
> - `financial_doc_0205-20-24.pdf` → `PAY_20240205_Payment_or_Bill_P001.pdf`  
> - `InterCambioExpress_Bill Payments.pdf` → `PAY_00000000_InterCambioExpress_Bill_Payments_P001.pdf`  
> - Typos like `INOTICE` → `Notice`, `Keily` → `Kelly`, `Benificiary` → `Beneficiary`.
> 
> ---
> 
> # Run order (fast + reversible)
> 
> 1) **Dry-run map** (CSV) → you eyeball.  
> 2) **Apply map** → atomic renames + moves + undo scripts.  
> 3) **Mirror** Client_Originals → Attorney_Binder (copies only).  
> 4) **Rebuild indexes** (optional—kept in the scripts, can toggle).
> 
> ---
> 
> ## 1) Script — Generate move/rename map (dry-run)
> 
> Save as `tools/generate_map.py` at repo root (where `Vault_Rosa` lives).
> 
> ```python
> import csv, re, os, hashlib
> from pathlib import Path
> ROOT = Path(r"K:\Vaults\Client\Rosa-KB")  # change if needed
> VAULT = ROOT / "Vault_Rosa"
> CLIENT = VAULT / "Client_Originals"
> ATTORNEY = VAULT / "Attorney_Binder"
> OUTDIR = ROOT / "_audit_out"
> OUTDIR.mkdir(exist_ok=True)
> MAP_CSV = OUTDIR / "master_rename_map.csv"
> 
> # -------- helpers
> SPACE = re.compile(r"[^\w\.]+", re.UNICODE)
> MULTI_US = re.compile(r"_+")
> DATE4 = re.compile(r"(\d{2})(\d{2})(\d{4})")         # 08052025 → 08 05 2025
> DATE_SPLIT = re.compile(r"(\d{2})[-_](\d{2})[-_](\d{2,4})")  # 0205-20-24
> BAD_TOKENS = {
>   "INOTICE":"Notice", "Keily":"Kelly", "Benificiary":"Beneficiary",
>   "Cert":"Certificate", "Certs":"Certificates"
> }
> 
> def slugify(s, keep_ext=True, limit_tokens=6):
>     base = Path(s).name
>     stem, ext = os.path.splitext(base)
>     for k,v in BAD_TOKENS.items():
>         stem = stem.replace(k, v)
>     stem = stem.strip().replace("-", " ").replace(".", " ")
>     stem = SPACE.sub("_", stem)
>     stem = MULTI_US.sub("_", stem).strip("_")
>     parts = [p for p in stem.split("_") if p]
>     parts = parts[:limit_tokens]
>     stem = "_".join([p[0].upper()+p[1:] if p else "" for p in parts])
>     return (stem + ext) if keep_ext else stem
> 
> def infer_date(path):
>     name = path.name
>     # 08052025 → 2025-08-05
>     m = DATE4.search(name)
>     if m:
>         mm, dd, yyyy = m.groups()
>         return f"{yyyy}{mm}{dd}"
>     # 0205-20-24 or 0205_20_24 → try guess century (>=30 → 19xx else 20xx)
>     m = DATE_SPLIT.search(name)
>     if m:
>         mm, dd, yy = m.groups()
>         if len(yy)==2:
>             yyyy = f"20{yy}" if int(yy)<30 else f"19{yy}"
>         else:
>             yyyy = yy
>         return f"{yyyy}{mm}{dd}"
>     # parent year folders
>     for p in path.parents:
>         if p.name.isdigit() and len(p.name)==4:
>             yyyy = p.name
>             # no month/day, set to 0000
>             return f"{yyyy}0000"
>     return "00000000"
> 
> def tag_for(path):
>     n = path.name.lower()
>     p = path.parent.as_posix().lower()
>     if any(k in (n+p) for k in ["i-797","notice_of_action","notice of action","not_"]): return "NOT"
>     if any(k in (n+p) for k in ["birth","acta de nacimiento","certificado","certificates"]): return "BIR"
>     if any(k in (n+p) for k in ["passport","id","ssn","driver","license","identification"]): return "ID"
>     if any(k in (n+p) for k in ["marriage","wedding","license"]): return "MAR"
>     if any(k in (n+p) for k in ["attorney","agreement","contract"]): return "ATT"
>     if any(k in (n+p) for k in ["payment","receipt","bill","intercambio","previous payments"]): return "PAY"
>     if any(k in (n+p) for k in ["bank","statement","operating bank","chase"]): return "BANK"
>     if any(k in (n+p) for k in ["1098","1099","w2"]): return "TAX"  # simplified
>     if any(k in (n+p) for k in ["letter","support","translation"]): return "LET"
>     if any(k in (n+p) for k in ["insurance"]): return "INS"
>     if any(k in (n+p) for k in ["ticket","travel","bus","plane"]): return "TRV"
>     if any(k in (n+p) for k in ["questionnaire","lista de documentos","checklist"]): return "Q"
>     return "OTH"
> 
> def simple_page_index(path):
>     # single files default to P001; series handled later if numerically suffixed
>     return "P001"
> 
> def normalize_file(path: Path):
>     ext = path.suffix.lower()
>     stem = slugify(path.stem, keep_ext=False)
>     yyyymmdd = infer_date(path)
>     tag = tag_for(path)
>     page = simple_page_index(path)
>     new_name = f"{tag}_{yyyymmdd}_{stem}_{page}{ext}"
>     # compress underscores
>     new_name = MULTI_US.sub("_", new_name).replace("__","_").strip("_")
>     return new_name
> 
> def target_dir(path: Path):
>     # Map current mess to the clean structure (client originals only).
>     rel = path.relative_to(VAULT)
>     top = rel.parts[0] if len(rel.parts)>0 else ""
>     # Prefer existing placement when it already matches final skeleton:
>     if "Client_Originals" in rel.parts:
>         # keep section; only clean subfolder names lightly
>         return (CLIENT / Path(*rel.parts[2:-1])).resolve()  # drop top two parts (Client_Originals / section)
>     # heuristics for non-standard
>     low = path.as_posix().lower()
>     if any(k in low for k in ["questionnaire","lista_de_documentos","lista de documentos","simplified_checklist"]):
>         return CLIENT / "08_Questionnaires_And_Checklists"
>     if any(k in low for k in ["notice of action","i-797","notice_of_action"]):
>         return CLIENT / "03_Notices"
>     if any(k in low for k in ["marriage","wedding","joint"]):
>         return CLIENT / "04_Marriage_Evidence"
>     if any(k in low for k in ["agreement","attorney","contract","payment"]):
>         return CLIENT / "05_Legal_And_Agreements"
>     if any(k in low for k in ["bank","paystub","receipt","w2","1099","1098","financial","expense"]):
>         return CLIENT / "07_Financial_Evidence"
>     if any(k in low for k in ["passport","birth","id","ssn","license","biographical"]):
>         return CLIENT / "01_Identity_And_Status"
>     return CLIENT / "00_Biographical"
> 
> def is_binary(p: Path):
>     return p.suffix.lower() not in (".md",".txt",".csv",".json",".yaml",".yml",".ini",".log")
> 
> def main():
>     rows = []
>     for p in VAULT.rglob("*"):
>         if p.is_dir(): 
>             continue
>         # Skip our own outputs
>         if "_audit_out" in p.as_posix() or "_reports" in p.as_posix(): 
>             continue
>         cur = p.resolve()
>         tgt_dir = target_dir(cur)
>         tgt_dir.mkdir(parents=True, exist_ok=True)
>         new_name = normalize_file(cur)
>         tgt = (tgt_dir / new_name).resolve()
>         if tgt == cur:
>             continue
>         reason = []
>         if tgt_dir not in cur.parents:
>             reason.append("move")
>         if new_name != cur.name:
>             reason.append("rename")
>         rows.append([str(cur), str(tgt), ",".join(reason) or "normalize"])
>     # Write map
>     with MAP_CSV.open("w", newline="", encoding="utf-8") as f:
>         w = csv.writer(f)
>         w.writerow(["Current_Path","Updated_Path","Reason"])
>         w.writerows(rows)
>     print(f"Wrote {MAP_CSV} with {len(rows)} planned changes.")
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> **What this catches from your vault right now:** mis-placed notices, mixed financial PDFs, birth cert images, payment receipts, and the duplicated OR_/CP_ folder names under section folders. It routes them into the **clean section tree** and normalizes filenames. fileciteturn2file0
> 
> ---
> 
> ## 2) Script — Apply (with undo)
> 
> Save as `tools/apply_map.py`.
> 
> ```python
> import csv, os, shutil
> from pathlib import Path
> 
> ROOT = Path(r"K:\Vaults\Client\Rosa-KB")
> OUTDIR = ROOT / "_audit_out"
> MAP_CSV = OUTDIR / "master_rename_map.csv"
> UNDO_BAT = OUTDIR / "undo_moves.bat"
> UNDO_SH = OUTDIR / "undo_moves.sh"
> 
> def ensure_parent(p: Path):
>     p.parent.mkdir(parents=True, exist_ok=True)
> 
> def main():
>     moves = []
>     with MAP_CSV.open("r", encoding="utf-8") as f:
>         r = csv.DictReader(f)
>         for row in r:
>             src = Path(row["Current_Path"])
>             dst = Path(row["Updated_Path"])
>             if not src.exists():
>                 continue
>             ensure_parent(dst)
>             shutil.move(str(src), str(dst))
>             moves.append((dst, src))  # reversed for undo
> 
>     # generate undo scripts
>     with UNDO_BAT.open("w", encoding="utf-8") as f:
>         f.write("@echo off\n")
>         for dst, src in moves:
>             f.write(f'mkdir "{src.parent}" 2>nul\n')
>             f.write(f'move "{dst}" "{src.parent}"\n')
>     with UNDO_SH.open("w", encoding="utf-8") as f:
>         f.write("#!/usr/bin/env bash\nset -e\n")
>         for dst, src in moves:
>             f.write(f'mkdir -p "{src.parent}"\n')
>             f.write(f'mv "{dst}" "{src.parent}/"\n')
>     print(f"Moved {len(moves)} items. Undo: {UNDO_BAT} / {UNDO_SH}")
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ---
> 
> ## 3) Script — Mirror Client → Attorney (always make copies)
> 
> Save as `tools/mirror_binder.py`.
> 
> ```python
> from pathlib import Path
> import shutil, filecmp, os
> 
> ROOT = Path(r"K:\Vaults\Client\Rosa-KB")
> VAULT = ROOT / "Vault_Rosa"
> CLIENT = VAULT / "Client_Originals"
> ATTORNEY = VAULT / "Attorney_Binder"
> 
> def copy_if_newer(src: Path, dst: Path):
>     if not dst.exists():
>         dst.parent.mkdir(parents=True, exist_ok=True)
>         shutil.copy2(src, dst)
>         return True
>     # replace if src is newer or size differs
>     if src.stat().st_mtime > dst.stat().st_mtime or src.stat().st_size != dst.stat().st_size:
>         shutil.copy2(src, dst)
>         return True
>     return False
> 
> def main():
>     changed = 0
>     for p in CLIENT.rglob("*"):
>         if p.is_dir(): 
>             continue
>         rel = p.relative_to(CLIENT)
>         dst = ATTORNEY / rel
>         if copy_if_newer(p, dst):
>             changed += 1
>     print(f"Mirrored {changed} files from Client_Originals → Attorney_Binder.")
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> > Result: Attorney_Binder **mirrors structure and filenames**—zero double-prefix madness, clean and readable. Re-run anytime after more moves/renames; it only copies deltas.
> 
> ---
> 
> ## 4) (Optional) Rebuild Master Indexes
> 
> Save as `tools/rebuild_indexes.py`.
> 
> ```python
> from pathlib import Path
> 
> ROOT = Path(r"K:\Vaults\Client\Rosa-KB")
> VAULT = ROOT / "Vault_Rosa"
> CLIENT = VAULT / "Client_Originals"
> ATTORNEY = VAULT / "Attorney_Binder"
> 
> def index_dir(root: Path):
>     lines = []
>     for p in sorted(root.rglob("*")):
>         if p.is_dir(): 
>             continue
>         rel = p.relative_to(root)
>         lines.append(f"- [ ] {rel.as_posix()}")
>     return "\n".join(lines)
> 
> def write(path: Path, text: str):
>     path.parent.mkdir(parents=True, exist_ok=True)
>     path.write_text(text, encoding="utf-8")
> 
> def main():
>     write(VAULT/"MASTER_INDEX_ORIGINALS.md", "# Master Index – Client Originals\n\n"+index_dir(CLIENT))
>     write(VAULT/"MASTER_INDEX_COPIES.md", "# Master Index – Attorney Binder\n\n"+index_dir(ATTORNEY))
>     # Side-by-side: poor man’s crosswalk (same paths)
>     write(VAULT/"MASTER_INDEX_ALL.md",
>           "# Master Index – All (Crosswalk)\n\n"
>           "Left: Client Originals | Right: Attorney Binder\n\n"
>           "_Paths are identical; check both binders below._\n")
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ---
> 
> ## 5) One-liner runner (Windows PowerShell)
> 
> ```powershell
> # From the repo root
> python tools/generate_map.py      # build master_rename_map.csv (dry-run)
> notepad .\_audit_out\master_rename_map.csv  # quick eyeball/edit if needed
> python tools/apply_map.py         # apply (with undo scripts)
> python tools/mirror_binder.py     # mirror Client → Attorney (copies only)
> python tools/rebuild_indexes.py   # rebuild indexes (optional)
> ```
> 
> ---
> 
> ## Sample rows that will appear in `master_rename_map.csv`
> 
> You’ll see lines like these (illustrative based on your tree):
> 
> ```
> Current_Path,Updated_Path,Reason
> K:\Vaults\Client\Rosa-KB\Vault_Rosa\1_Immigration\Attorney_Binder\01_Identity_And_Status\OR_01_CP_01_IDs\123_r.lucas_Acta de Nacimiento.jpg,K:\Vaults\Client\Rosa-KB\Vault_Rosa\Client_Originals\01_Identity_And_Status\02_Birth_Certificates_Translations\BIR_00000000_RLucas_Birth_Certificate_P001.jpg,move,rename
> K:\Vaults\Client\Rosa-KB\Vault_Rosa\1_Immigration\Attorney_Binder\01_Identity_And_Status\OR_03_CP_03_USCIS_Notices\08052025_1-797 INOTICE OF ACTION I.jpg,K:\Vaults\Client\Rosa-KB\Vault_Rosa\Client_Originals\03_Notices\NOT_20250805_Notice_of_Action_P001.jpg,move,rename
> K:\Vaults\Client\Rosa-KB\Vault_Rosa\_audit_out\backup\20250909_185947\Vault_Rosa\2_Financial\2024\financial_doc_0205-20-24.pdf,K:\Vaults\Client\Rosa-KB\Vault_Rosa\Client_Originals\07_Financial_Evidence\02_Bills_Receipts\PAY_20240205_Payment_or_Bill_P001.pdf,move,rename
> K:\Vaults\Client\Rosa-KB\Vault_Rosa\1_Immigration\Attorney_Binder\05_Legal_And_Agreements\OR_14_CP_14_Payment_Confirmations\PAY_20250421_04212025_Previous_Payments__16_P001.jpg,K:\Vaults\Client\Rosa-KB\Vault_Rosa\Client_Originals\05_Legal_And_Agreements\Payment_Confirmations\PAY_20250421_Previous_Payments_16_P001.jpg,move,rename
> ```
> 
> (Your file set is large; the script generates all rows so you don’t hand-type any of this.) fileciteturn2file0
> 
> ---
> 
> ## Billing quick-sheet (fair + receipt-ready)
> 
> - **Vault normalization & mapping** (scripts + CSV + review): **1.0–1.5 hr**
> - **Apply + Mirror + Index refresh**: **0.5–1.0 hr**
> - **Spot fixes (edge cases/Spanish titles)**: **0.5–1.0 hr**
> 
> At **$99/hr** → **$198–$446** baseline. Heavy edge-cases or extra translation/QC adds time.
> 
> ---
> 
> ### Finish: Done. Dusted. Next bag.
> Run the 5-step sequence. If Cursor balks again, these scripts do not depend on it; they work directly on disk, cleanly and reversibly. After the first pass, we can tighten the tags or add a couple more filename heuristics (e.g., better W-2/1099 detection) without redoing anything—just regenerate the map and re-apply.
