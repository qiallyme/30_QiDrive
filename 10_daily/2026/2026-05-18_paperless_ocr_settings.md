---
layout: page
title: "Paperless OCR Settings"
slug: "paperless_ocr_settings"
created_at: "2026-05-18 22:05:22"
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
uid: "6a0bd36d-3408-83ea-a37c-c048503e55ce"
canonical_ref: ""
---

# Paperless OCR Settings

## Overview
- **Date**: 2026-05-18 22:05:22
- **Conversation ID**: `6a0bd36d-3408-83ea-a37c-c048503e55ce`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> anything i should update here in paperless. Output Type

> Language

> Pages

> Mode

> Skip Archive File

> Image DPI

> Clean

> Deskew

> Enable  

> Rotate Pages

> Enable  

> Rotate Pages Threshold

> Max Image Pixels

> Color Conversion Strategy

> OCR Arguments

### Assistant
> I’ll give you the “don’t overthink it” Paperless defaults, then the few settings worth changing for your QiArchive/OCR pipeline.

### Assistant
> Yes. For **QiArchive/Paperless**, I’d keep this boring and stable. You want **searchable originals + clean archive PDFs**, not a fragile OCR science project.
> 
> ### Recommended Paperless OCR settings
> 
> | Setting | Recommendation | Why |
> |---|---:|---|
> | **Output Type** | `pdfa` / archive PDF | Best for long-term archive/search. Paperless keeps originals separately, and archive PDFs are for searchable preservation. Paperless is designed around storing documents as searchable archives. citeturn899348search10turn899348search19 |
> | **Language** | `eng` | Use English unless you regularly scan other languages. If you add Spanish later, use `eng+spa`, but only after installing the OCR language package. Paperless uses OCR language configuration to infer related behavior. citeturn899348search0 |
> | **Pages** | blank / default | Do **not** limit pages unless OCR is too slow. For legal/finance, full-document OCR matters. |
> | **Mode** | `skip` or default | Use `skip` if many PDFs already contain text. Use `redo` only when existing OCR is garbage. Don’t blindly redo everything. |
> | **Skip Archive File** | **Off** | You want the archive/search PDF. Only turn this on for temporary bulk import speed. |
> | **Image DPI** | `300` | Solid OCR quality without bloating everything. |
> | **Clean** | `clean` or default | Fine for scans. Avoid aggressive cleaning unless documents look messy. |
> | **Deskew** | **Enable** | Good for scanner/photo documents. It corrects slight page skew from scanning. citeturn899348search7 |
> | **Rotate Pages** | **Enable**, but watch it | Useful for sideways pages, but if Paperless starts rotating things wrong, disable it. Rotation issues are a known pain point. citeturn899348search7turn899348search15 |
> | **Rotate Pages Threshold** | default first | Don’t touch unless rotation misbehaves. Then raise/lower based on results. Paperless docs specifically say to adjust threshold if auto-rotation is wrong. citeturn899348search0turn899348search7 |
> | **Max Image Pixels** | default | Leave it unless huge images fail processing. |
> | **Color Conversion Strategy** | default / `RGB` | Default is fine. Don’t get cute here unless archive creation errors. |
> | **OCR Arguments** | leave blank | No custom args yet. Custom OCR arguments are where chaos enters the building. |
> 
> ### My actual “set it and move on” version
> 
> For your system, I’d use:
> 
> ```text
> Output Type: pdfa
> Language: eng
> Pages: blank/default
> Mode: skip
> Skip Archive File: off
> Image DPI: 300
> Clean: clean/default
> Deskew: enabled
> Rotate Pages: enabled
> Rotate Pages Threshold: default
> Max Image Pixels: default
> Color Conversion Strategy: default/RGB
> OCR Arguments: blank
> ```
> 
> ### One important warning
> 
> If you are importing **already-searchable PDFs**, `Mode: skip` is the right move. If you use `redo`, Paperless may reprocess OCR unnecessarily, slow the server down, and sometimes make good PDFs worse. Save `redo` for specific bad documents only.
> 
> For your current pipeline: **don’t optimize OCR yet**. Get intake, tags, correspondents, storage paths, and export/sync behavior working first. OCR tuning is phase two.

### User
> Enable Barcodes

> Enable  

> Enable TIFF Support

> Enable  

> Barcode String

> Retain Split Pages

> Enable  

> Enable ASN

> Enable  

> ASN Prefix

> Upscale

> DPI

> Max Pages

> Enable Tag Detection

> Enable  

> Tag Mapping

### Assistant
> Yep — this batch is more “workflow behavior” than OCR quality. For QiArchive, most of these should stay conservative unless you’re intentionally scanning separator sheets/barcodes.

### Assistant
> Yes — but **do not turn all of this on yet** unless you’re batch-scanning physical papers with barcode separator sheets. Otherwise you’ll create accidental splits and mystery behavior. Classic “we automated the mess” trap.
> 
> ## Recommended settings for QiArchive right now
> 
> | Setting | Recommendation | Why |
> |---|---:|---|
> | **Enable Barcodes** | **Off for now** | Only needed if you scan one big PDF and want Paperless to split it by barcode separator pages. Paperless uses barcodes for page separation when enabled. citeturn439739search8turn439739search11 |
> | **Enable TIFF Support** | **Off unless needed** | Turn on only if your scanner/app outputs `.tif` / `.tiff`. Most phone/scanner workflows use PDF/JPG/PNG. |
> | **Barcode String** | Default / blank | Only set this if you use a custom separator barcode. Don’t customize yet. |
> | **Retain Split Pages** | **Off** | Separator pages should usually be removed from final docs. If using ASN barcodes, ASN pages may be retained differently because they identify the document. citeturn439739search8 |
> | **Enable ASN** | **Optional, but I’d turn ON if you keep physical files** | ASN = Archive Serial Number. This is useful when you want the digital document to point back to a physical folder/binder/file. Paperless supports ASN lookup as part of physical archive workflows. citeturn439739search18 |
> | **ASN Prefix** | `ASN` | Clean and standard. Example: `ASN000123`. |
> | **Upscale** | **Off** | Only use if barcode detection fails on low-quality scans. It can slow processing. |
> | **DPI** | `300` | Matches the OCR setting. Good balance. |
> | **Max Pages** | blank/default | Don’t limit unless giant scans are choking the server. |
> | **Enable Tag Detection** | **On** | This is useful. Let Paperless detect tags from document text. Low-risk, high-value. |
> | **Tag Mapping** | Leave blank for now | Don’t build a mapping until your tag taxonomy is stable. Otherwise you’ll be cleaning up garbage tags later. |
> 
> ## My actual recommendation
> 
> Use this:
> 
> ```text id="mmyrbx"
> Enable Barcodes: Off
> Enable TIFF Support: Off
> Barcode String: blank/default
> Retain Split Pages: Off
> Enable ASN: On, if keeping physical documents
> ASN Prefix: ASN
> Upscale: Off
> DPI: 300
> Max Pages: blank/default
> Enable Tag Detection: On
> Tag Mapping: blank
> ```
> 
> ## The split-brain rule
> 
> Use **ASN** for physical paper tracking.
> 
> Use **barcodes** only when doing bulk scans where one upload contains multiple separate documents.
> 
> So for now:
> 
> **Digital-first imports:** barcode off, ASN optional.  
> **Physical archive workflow:** ASN on.  
> **Bulk scanner workflow:** barcode on later, after testing with 5–10 documents.
> 
> Do **not** enable barcode splitting casually. That setting is powerful, but it’s also how Paperless starts slicing documents like it’s had too much coffee.

### User
> in order what to udpate here. Paperless-ngx

> Welcome, qiadmin. View site / Change password / Log out Toggle theme (current theme: auto)

> Paperless-ngx administration

> Accounts

> Model name	Add link	Change or view list link

> Email addresses	

> Add

> Change

> Audit log

> Model name	Add link	Change or view list link

> Log entries		

> View

> Auth Token

> Model name	Add link	Change or view list link

> Tokens	

> Add

> Change

> Authentication and Authorization

> Model name	Add link	Change or view list link

> Groups	

> Add

> Change

> Users	

> Add

> Change

> Celery Results

> Model name	Add link	Change or view list link

> Group results	

> Add

> Change

> Task results	

> Add

> Change

> Documents

> Model name	Add link	Change or view list link

> Correspondents	

> Add

> Change

> Custom field instances	

> Add

> Change

> Custom fields	

> Add

> Change

> Document types	

> Add

> Change

> Documents		

> Change

> Notes	

> Add

> Change

> Paperless tasks	

> Add

> Change

> Saved views	

> Add

> Change

> Share links	

> Add

> Change

> Storage paths	

> Add

> Change

> Tags	

> Add

> Change

> MFA

> Model name	Add link	Change or view list link

> Authenticators	

> Add

> Change

> Paperless mail

> Model name	Add link	Change or view list link

> Mail accounts	

> Add

> Change

> Mail rules	

> Add

> Change

> Processed mails	

> Add

> Change

> Social Accounts

> Model name	Add link	Change or view list link

> Social accounts	

> Add

> Change

> Social application tokens	

> Add

> Change

> Social applications	

> Add

> Change

### Assistant
> Yes. Update **only the operational objects first**. Ignore the admin/system tables unless there is a reason.
> 
> Here’s the order I’d do it in for QiArchive:
> 
> ## 1. Storage paths
> 
> Do this first because documents need a destination logic.
> 
> Go to:
> 
> **Documents → Storage paths → Add**
> 
> Create the main paths you already started, for example:
> 
> | Name | Path pattern |
> |---|---|
> | `00 Inbox` | `00_inbox/{{ created_year }}/{{ title }}` |
> | `10 Workbench` | `10_workbench/{{ created_year }}/{{ title }}` |
> | `20 Timeline` | `20_timeline/{{ created_year }}/{{ title }}` |
> | `30 Life` | `30_life/{{ created_year }}/{{ title }}` |
> | `40 People` | `40_people/{{ correspondent }}/{{ created_year }}/{{ title }}` |
> | `50 Business` | `50_business/{{ created_year }}/{{ title }}` |
> | `60 Finance` | `60_finance/{{ created_year }}/{{ correspondent }}/{{ title }}` |
> | `70 Legal` | `70_legal/{{ created_year }}/{{ document_type }}/{{ title }}` |
> | `80 Tech` | `80_tech/{{ created_year }}/{{ title }}` |
> | `90 Assets` | `90_assets/{{ created_year }}/{{ title }}` |
> | `100 Data` | `100_data/{{ created_year }}/{{ title }}` |
> | `110 Reference` | `110_reference/{{ created_year }}/{{ title }}` |
> | `900 Archive` | `900_archive/{{ created_year }}/{{ title }}` |
> 
> Don’t get too fancy yet. Storage paths should be stable, not clever.
> 
> ---
> 
> ## 2. Document types
> 
> Go to:
> 
> **Documents → Document types → Add**
> 
> Start with a lean set:
> 
> | Document Type |
> |---|
> | `Statement` |
> | `Receipt` |
> | `Invoice` |
> | `Bill` |
> | `Contract` |
> | `Notice` |
> | `Letter` |
> | `Court Filing` |
> | `Evidence` |
> | `Medical` |
> | `Insurance` |
> | `Tax` |
> | `ID / Credential` |
> | `Manual / Reference` |
> | `Screenshot` |
> | `Export` |
> | `Other` |
> 
> This is where we prevent the monster taxonomy. Keep it practical.
> 
> ---
> 
> ## 3. Tags
> 
> Go to:
> 
> **Documents → Tags → Add**
> 
> Use tags for status, domain, priority, and action. Not for everything.
> 
> Suggested starter tags:
> 
> ### Status tags
> 
> | Tag |
> |---|
> | `inbox` |
> | `review_needed` |
> | `processed` |
> | `archived` |
> | `duplicate_check` |
> | `needs_ocr_review` |
> 
> ### Action tags
> 
> | Tag |
> |---|
> | `to_pay` |
> | `to_file` |
> | `to_upload` |
> | `to_print` |
> | `to_dispute` |
> | `to_reconcile` |
> | `waiting_response` |
> 
> ### Domain tags
> 
> | Tag |
> |---|
> | `finance` |
> | `legal` |
> | `business` |
> | `household` |
> | `tech` |
> | `tax` |
> | `medical_admin` |
> | `vehicle` |
> | `property` |
> 
> ### Priority tags
> 
> | Tag |
> |---|
> | `urgent` |
> | `deadline` |
> | `high_value` |
> | `sensitive` |
> 
> Don’t create 200 tags. That is how Paperless becomes a junk drawer with a search bar.
> 
> ---
> 
> ## 4. Correspondents
> 
> Go to:
> 
> **Documents → Correspondents → Add**
> 
> This is the “who is this from/to/about” field.
> 
> Start with only recurring entities:
> 
> | Correspondent examples |
> |---|
> | Banks |
> | Credit unions |
> | Courts |
> | Attorneys |
> | Insurance companies |
> | Utilities |
> | Phone/internet providers |
> | Healthcare admin entities |
> | Government agencies |
> | Employers/clients |
> | Vendors |
> | Family/household entities if useful |
> 
> Do **not** create one for every random receipt. Only recurring or important sources.
> 
> ---
> 
> ## 5. Custom fields
> 
> Go to:
> 
> **Documents → Custom fields → Add**
> 
> This is where Paperless becomes actually useful for QiArchive.
> 
> Create these first:
> 
> | Field Name | Type | Use |
> |---|---|---|
> | `QiID` | Text | Your system/global ID |
> | `Case ID` | Text | Legal/court/claim grouping |
> | `Account Last 4` | Text | Finance/accounts |
> | `Statement Period Start` | Date | Statements |
> | `Statement Period End` | Date | Statements |
> | `Due Date` | Date | Bills/notices |
> | `Amount` | Monetary / Text | Bills, receipts, invoices |
> | `Tax Year` | Number / Text | Tax sorting |
> | `Physical Location` | Text | Binder/box/folder reference |
> | `Source System` | Text | Drive, Gmail, scanner, portal, upload |
> | `Review Status` | Text | Optional if tags are not enough |
> 
> If Paperless supports select fields in your version, make `Review Status` a select-like field conceptually:
> 
> `New / Reviewed / Needs Action / Filed / Archived`
> 
> But if that’s annoying, skip it and use tags.
> 
> ---
> 
> ## 6. Saved views
> 
> Go to:
> 
> **Documents → Saved views → Add**
> 
> Create views that match how your brain works:
> 
> | View Name | Filter idea |
> |---|---|
> | `Inbox - Needs Review` | tag = `review_needed` or `inbox` |
> | `Finance - To Reconcile` | tag = `to_reconcile` |
> | `Bills - To Pay` | tag = `to_pay` |
> | `Legal - Active` | document type = `Court Filing`, `Evidence`, `Notice` |
> | `Tax - Current Year` | tag = `tax` |
> | `Deadlines` | tag = `deadline` or custom due date exists |
> | `Needs OCR Review` | tag = `needs_ocr_review` |
> | `Duplicates / Cleanup` | tag = `duplicate_check` |
> | `Sensitive Docs` | tag = `sensitive` |
> 
> This is the payoff layer. Saved views are your dashboards.
> 
> ---
> 
> ## 7. Mail accounts / Mail rules
> 
> Do this later unless email ingestion is today’s goal.
> 
> Go to:
> 
> **Paperless mail → Mail accounts**  
> Then:
> 
> **Paperless mail → Mail rules**
> 
> Use this only after the base taxonomy is stable. Otherwise mail auto-ingestion will spray chaos into your archive.
> 
> Good future rules:
> 
> | Rule | Action |
> |---|---|
> | Bank statements | type `Statement`, tag `finance`, storage `60 Finance` |
> | Utility bills | type `Bill`, tag `to_pay`, storage `60 Finance` |
> | Legal/court emails | type `Notice` or `Court Filing`, tag `legal`, storage `70 Legal` |
> | Receipts | type `Receipt`, tag `to_reconcile`, storage `60 Finance` |
> 
> ---
> 
> ## 8. Notes
> 
> Skip for setup.
> 
> Use notes only after documents are imported, for human context like:
> 
> `This relates to the foreclosure timeline.`  
> `Needs dispute letter.`  
> `Matched to bank transaction on 2026-05-18.`
> 
> ---
> 
> ## 9. Users / Groups / Auth / MFA
> 
> Only update this if someone else will access Paperless.
> 
> For now:
> 
> | Area | Recommendation |
> |---|---|
> | Users | Leave as `qiadmin` unless adding another person |
> | Groups | Skip |
> | Tokens | Skip unless API integration needs it |
> | MFA | Enable later after setup is stable |
> | Share links | Avoid unless intentionally sharing documents |
> 
> ---
> 
> ## 10. Ignore these unless troubleshooting
> 
> Do not mess with these right now:
> 
> | Section | Why |
> |---|---|
> | Audit log | Read-only/system trail |
> | Celery Results | Background task history |
> | Paperless tasks | Processing/task status |
> | Processed mails | Mail history |
> | Social accounts | Not needed |
> | Social applications | Not needed |
> | Social application tokens | Not needed |
> | Custom field instances | Automatically created when fields are used |
> | Documents → Documents | Don’t mass-edit until taxonomy is ready |
> 
> ## Actual order, no fluff
> 
> Do it exactly like this:
> 
> 1. **Storage paths**
> 2. **Document types**
> 3. **Tags**
> 4. **Correspondents**
> 5. **Custom fields**
> 6. **Saved views**
> 7. **Mail accounts**
> 8. **Mail rules**
> 9. **MFA**
> 10. **API tokens only when needed**
> 
> That’s the clean path.
> 
> Right now, your next screen should be:
> 
> **Documents → Storage paths → Add**
> 
> Start there.

### User
> WHATS THE IMAP SERVER, PORT FOR GMAIL

### Assistant
> For **Gmail IMAP**:
> 
> ```text
> IMAP server: imap.gmail.com
> Port: 993
> Security: SSL/TLS
> Username: your full Gmail address
> Password: App Password, not your normal Gmail password
> ```
> 
> For sending mail, if needed:
> 
> ```text
> SMTP server: smtp.gmail.com
> Port: 465 with SSL/TLS
> or
> Port: 587 with STARTTLS
> Username: your full Gmail address
> Password: App Password
> ```
> 
> Important: Gmail usually requires **2-Step Verification enabled** before you can create an **App Password**. Use that app password in Paperless, not your regular Gmail login.

### User
> ok back to paperless how do we autoingest into paperless, from any device, or first do i just need it uploaded to the google drive then somethign watches the drive or how can we make this work best.

### Assistant
> This is the right question. The clean answer is: don’t make every device “talk to Paperless” directly; make every device drop documents into one intake lane, then Paperless consumes that lane.

### Assistant
> Best setup: **one universal intake folder** that Paperless watches. Every device sends files there. Paperless consumes them, OCRs them, tags/routes them, and removes them from the intake folder after ingest. Paperless officially uses a **consumption directory** for this; files placed there are imported into Paperless and are not retained in that consume folder afterward. citeturn635801search0turn635801search3
> 
> ## The clean QiArchive ingestion model
> 
> ### Best path
> 
> ```text
> Any Device
>    ↓
> Google Drive / QiArchive Intake folder
>    ↓
> Sync tool on QiServer
>    ↓
> Paperless consume folder
>    ↓
> Paperless OCR + classify + archive
> ```
> 
> But here’s the important part: **Paperless itself should watch a local server folder**, not Google Drive directly.
> 
> So the real architecture should be:
> 
> ```text
> Google Drive:
> QiArchive/_inbox/paperless_consume/
> 
> QiServer local:
>  /srv/qios/data/paperless/consume/
> 
> Sync bridge:
>  Google Drive intake → local consume folder
> 
> Paperless:
>  Watches /usr/src/paperless/consume inside container
> ```
> 
> ## Why this is the best setup
> 
> Paperless wants a normal local filesystem consume directory. In Docker, the docs specifically say not to change the internal `PAPERLESS_CONSUMPTION_DIR`; instead, change the local folder mounted into the container through `docker-compose.yml`. citeturn635801search3
> 
> So don’t make Paperless depend directly on Drive weirdness. Let Drive be the human-friendly dropbox, and let the server sync/copy files into Paperless.
> 
> ## Intake options, ranked
> 
> ### 1. Best overall: Google Drive intake folder + rclone/sync script
> 
> This is what I’d do for you.
> 
> Every device already understands Google Drive:
> 
> - iPhone: scan/upload to Drive
> - Windows PC: save/export to Drive folder
> - Android/tablet: upload to Drive
> - Gmail attachments: save to Drive
> - Scanner app: export to Drive
> 
> Then QiServer runs a small scheduled sync that copies/moves new files from:
> 
> ```text
> Google Drive/QiArchive/_inbox/paperless_consume
> ```
> 
> to:
> 
> ```text
> /srv/qios/data/paperless/consume
> ```
> 
> Paperless handles the rest.
> 
> This keeps Paperless stable and lets your intake work from anywhere.
> 
> ### 2. Also good: email-to-Paperless
> 
> Paperless supports mail accounts and mail rules, so you can create a Gmail label or mailbox that Paperless checks. This is great for bills, statements, receipts, and attachments. citeturn635801search0
> 
> Example:
> 
> ```text
> Gmail label: To Paperless
> Paperless mail rule:
> - consume attachments
> - apply tag: inbox
> - maybe document type: Receipt / Statement / Bill
> ```
> 
> Use this for email-native docs. Don’t make it the only intake path.
> 
> ### 3. Good later: scanner/network share directly to consume folder
> 
> If you have a scanner or multifunction printer, it can scan directly to a network folder/share mapped to Paperless consume. This is common Paperless usage: scanner drops files into a hot folder, Paperless consumes them. citeturn635801search8
> 
> But for you, this is phase two. Drive intake is simpler and device-agnostic.
> 
> ### 4. Direct upload through Paperless UI
> 
> Fine for one-offs. Not the main system.
> 
> Use this when you’re already in Paperless and need to upload something manually.
> 
> ## My recommendation for your exact setup
> 
> Use **three intake lanes**:
> 
> ```text
> 01_drive_drop
> For anything from phone, PC, scanner app, downloaded PDFs.
> 
> 02_email_drop
> For Gmail bills, receipts, statements, notices.
> 
> 03_manual_upload
> For emergency one-offs directly inside Paperless.
> ```
> 
> But all should land with the same first tag:
> 
> ```text
> inbox
> ```
> 
> Then your Paperless rules/classification can sort later.
> 
> ## Folder design in Google Drive
> 
> Create this:
> 
> ```text
> QiArchive
>   _inbox
>     paperless_consume
>     paperless_holding
>     paperless_failed
> ```
> 
> ### What each folder does
> 
> | Folder | Purpose |
> |---|---|
> | `paperless_consume` | Drop files here from any device |
> | `paperless_holding` | Stuff you are not ready to ingest yet |
> | `paperless_failed` | Bad files, duplicates, or things that need manual review |
> 
> Do **not** let Paperless consume your entire Drive. That would be a crime scene with Wi-Fi.
> 
> ## Server-side target folder
> 
> On QiServer, use:
> 
> ```text
> /srv/qios/data/paperless/consume
> ```
> 
> Your Docker compose should mount that into the container as the Paperless consume folder.
> 
> Something like:
> 
> ```yaml
> volumes:
>   - /srv/qios/data/paperless/consume:/usr/src/paperless/consume
> ```
> 
> That matches the Paperless model: local host folder mounted into the container’s consume directory. citeturn635801search3
> 
> ## Important behavior
> 
> When Paperless consumes files from the consume directory, it imports them into its own storage and removes them from that consume directory. It still preserves the original document internally, and archive versions are stored alongside originals. citeturn635801search0
> 
> Translation: the consume folder is **not storage**. It is a conveyor belt.
> 
> ## The system I’d build first
> 
> ### Phase 1 — simple and stable
> 
> 1. Create Google Drive folder:  
>    `QiArchive/_inbox/paperless_consume`
> 
> 2. Mount or sync that folder on QiServer using `rclone`.
> 
> 3. Have a small script copy new files into:  
>    `/srv/qios/data/paperless/consume`
> 
> 4. Paperless consumes from there.
> 
> 5. Every ingested document starts with:
>    - tag: `inbox`
>    - maybe tag: `review_needed`
>    - storage path: `00 Inbox`
> 
> ### Phase 2 — rules
> 
> Add Paperless rules/classification:
> 
> - bank statements → `60 Finance`
> - court/legal docs → `70 Legal`
> - receipts → `60 Finance`
> - tech docs → `80 Tech`
> - manuals/reference → `110 Reference`
> 
> Paperless has automatic matching that can assign tags, correspondents, document types, and storage paths based on prior assignments. citeturn635801search19
> 
> ### Phase 3 — email ingestion
> 
> Set up Gmail IMAP and mail rules after your folders/tags/types are stable.
> 
> ## Decision
> 
> Do **Google Drive intake → QiServer consume folder → Paperless**.
> 
> That gives you:
> 
> - intake from any device
> - no exposing Paperless publicly
> - clean central workflow
> - easy backup
> - easy failure handling
> - no direct dependency on mobile upload hacks
> 
> The key rule: **Drive is the dropbox. Paperless is the archive. The consume folder is the conveyor belt.**

### User
> the first folder in qiarchive is 10_ingestion is that not good enough.

### Assistant
> Yes — **`10_ingestion` is good enough**. Better than `_inbox`, actually, because it matches your numbered QiArchive doctrine.
> 
> I’d use it like this:
> 
> ```text
> QiArchive/
>   10_ingestion/
>     10_paperless_consume/
>     20_holding/
>     30_failed/
>     40_processed_log/
> ```
> 
> Or slightly cleaner:
> 
> ```text
> QiArchive/
>   10_ingestion/
>     10_consume/
>     20_holding/
>     30_failed/
>     40_review/
> ```
> 
> My vote:
> 
> ```text
> QiArchive/
>   10_ingestion/
>     10_consume/
>     20_holding/
>     30_failed/
>     40_review/
> ```
> 
> ### What each one means
> 
> | Folder | Use |
> |---|---|
> | `10_consume` | Drop files here from any device. This syncs/copies into Paperless consume. |
> | `20_holding` | Stuff you are not ready to ingest yet. |
> | `30_failed` | Files that failed import or need fixing. |
> | `40_review` | Optional staging for docs that ingested but need human cleanup. |
> 
> ### The server mapping
> 
> Your Google Drive folder:
> 
> ```text
> QiArchive/10_ingestion/10_consume
> ```
> 
> syncs to QiServer:
> 
> ```text
> /srv/qios/data/paperless/consume
> ```
> 
> Paperless watches/uses that local server folder.
> 
> ### One correction
> 
> Don’t call the Drive folder `paperless_consume` unless you want the folder name tied forever to Paperless.
> 
> Better:
> 
> ```text
> 10_consume
> ```
> 
> Because later the same ingestion layer can feed:
> 
> - Paperless
> - OCR
> - QiBrain
> - Qdrant
> - Neo4j
> - dedupe tools
> - archive logs
> 
> So yes, **`10_ingestion` is the right first folder**. Keep it. The only update is to make the subfolders intentional and numbered.
