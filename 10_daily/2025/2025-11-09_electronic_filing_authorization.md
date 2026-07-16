---
layout: page
title: "Electronic filing authorization"
slug: "electronic_filing_authorization"
created_at: "2025-11-09 06:40:50"
updated_at: "2025-11-09 06:40:50"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-001.json"
template_key: master-template
date: 2025-11-09
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69108b9f-5480-832b-84af-2a5202be435f"
canonical_ref: ""
---

# Electronic filing authorization

## Overview
- **Date**: 2025-11-09 06:40:50
- **Conversation ID**: `69108b9f-5480-832b-84af-2a5202be435f`
- **Source**: `Chat-Export-28513-2026/conversations-001.json`

## Chat History

### User
> my client is not getting my email to sign his tax return can you give me the language required for him to sign off on all three of his returns electgronically so i can just put the combined pdf into the file in honeybooks an dhvae him sign in his portal.

### Assistant
> Here’s professional, IRS-compliant language you can paste directly above or below the signature line in HoneyBook (or any PDF you upload) so your client can electronically sign and authorize all three returns at once:  
> 
> ---
> 
> ### **Electronic Filing Authorization for Tax Year 20XX (Combined Return Authorization)**
> 
> I, **[Client Name]**, hereby authorize **[Your Firm or Name]** to prepare and electronically file my federal and state income tax returns for the following tax years:
> 
> - **20XX Federal Income Tax Return (Form 1040 and attachments)**  
> - **20XX State Income Tax Return**  
> - **20XX Local/City/Other Return (if applicable)**  
> 
> By signing below, I acknowledge that:  
> 1. I have reviewed each of the above tax returns and confirm that, to the best of my knowledge, all information provided is true, correct, and complete.  
> 2. I authorize **[Your Firm or Name]** to electronically file these returns on my behalf using the IRS e-file system and any applicable state or local filing system.  
> 3. I understand that my signature below serves as my official authorization and consent in lieu of physically signing IRS Form 8879 and any equivalent state authorization forms.  
> 4. I agree that my electronic signature below shall have the same legal effect as a handwritten signature for purposes of verifying and authorizing my tax filings.  
> 
> **Client Name:** ___________________________  
> **Date:** ___________________________  
> **Signature (Electronic):** ___________________________
> 
> ---
> 
> If you’d like, I can also generate a polished **HoneyBook-ready PDF cover page** (with your logo, headings, and embedded signature box) to drop into the file for signing — would you like me to do that?

### User
> i need to make this into a iframe url. https://drive.google.com/drive/folders/1uyYWwxEVaFreiBGZpEpjJwJ4NoIq7QtP?usp=drive_link

### Assistant
> To embed that **Google Drive folder** in an `<iframe>`, you can’t use the regular sharing link — Google requires a modified “preview” URL format.  
> 
> Here’s the version you can safely embed:  
> 
> ```html
> <iframe 
>   src="https://drive.google.com/embeddedfolderview?id=1uyYWwxEVaFreiBGZpEpjJwJ4NoIq7QtP#grid" 
>   style="width:100%; height:600px; border:0;">
> </iframe>
> ```
> 
> ✅ **Notes:**
> - Replace `#grid` with `#list` if you want a list view instead of grid view.  
> - The folder must have **“Anyone with the link” → Viewer** access for it to display.  
> - You can adjust `height` or `width` as needed.  
> 
> Would you like me to give you a responsive version that scales automatically with the container (so it looks good on phones too)?

### User
> that i frame is not working what options do i have to cover these pdfs into embedible something.

### Assistant
> Yeah, that folder embed is probably getting blocked — either by Google’s frame rules *or* by whatever app you’re pasting it into (a lot of portals strip iframes completely).
> 
> You’ve basically got 3 realistic paths here, depending on what you’re trying to do with those PDFs:
> 
> ---
> 
> ## 1️⃣ Easiest (for signing): Skip embed → upload PDF directly into HoneyBook
> 
> Since your end goal is **getting the returns signed**, honestly the cleanest solution is:
> 
> 1. Download the combined PDF from Google Drive.  
> 2. Go into HoneyBook → that client’s project → upload the PDF directly.  
> 3. Use HoneyBook’s **Smart File / Contract / Signature** tools to place a signature box + date.  
> 
> No iframe, no embed drama. The client just sees “Sign here” in their portal and it’s legally clean.
> 
> ---
> 
> ## 2️⃣ If you *really* want an embeddable viewer (website / custom portal)
> 
> ### Option A – Embed a *single* PDF from Google Drive
> 
> For each PDF, grab its **file ID** and use the `.../preview` URL:
> 
> 1. Open the PDF in Drive.  
> 2. In the address bar you’ll see something like:  
>    `https://drive.google.com/file/d/FILE_ID/view?usp=sharing`  
> 3. Use that `FILE_ID` in this iframe:
> 
> ```html
> <iframe
>   src="https://drive.google.com/file/d/FILE_ID/preview"
>   style="width: 100%; height: 600px; border: 0;"
>   allow="autoplay">
> </iframe>
> ```
> 
> Make sure:
> - The file is set to **“Anyone with the link – Viewer”**.
> - The platform you’re pasting this in actually allows iframes (many CRMs/portals don’t).
> 
> ---
> 
> ### Option B – Use a generic PDF viewer as an iframe
> 
> If your PDFs are hosted somewhere public (your own site, S3, etc.), you can use Google’s viewer wrapper:
> 
> ```html
> <iframe
>   src="https://drive.google.com/viewerng/viewer?embedded=true&url=ENCODED_PDF_URL"
>   style="width:100%; height:600px; border:0;">
> </iframe>
> ```
> 
> Replace `ENCODED_PDF_URL` with the URL-encoded link to your PDF.
> 
> ---
> 
> ### Option C – Basic browser PDF embed (if you control hosting)
> 
> If the PDF is sitting on your own domain (or somewhere that allows framing), you can just do:
> 
> ```html
> <embed
>   src="https://yourdomain.com/path/to/return-package.pdf"
>   type="application/pdf"
>   width="100%"
>   height="600px">
> ```
> 
> or
> 
> ```html
> <iframe
>   src="https://yourdomain.com/path/to/return-package.pdf"
>   style="width:100%; height:600px; border:0;">
> </iframe>
> ```
> 
> ---
> 
> ## 3️⃣ If iframes are blocked where you’re embedding
> 
> If the app you’re using (very possibly HoneyBook) **does not allow iframes at all**, then:
> 
> - You **won’t** be able to embed Google Drive or any external viewer.
> - Your realistic options are:
>   - Upload the PDFs directly into that system (best for signing).
>   - Or give the client a normal download link to the PDFs (view in a new tab) and just use the portal for the **signature page only**.
> 
> ---
> 
> If you tell me *where* you’re trying to embed this (HoneyBook smart file, your website, some portal), I can give you a copy-paste snippet tailored exactly to that setup.
