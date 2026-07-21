---
layout: page
title: "Mail Collection Inquiry"
slug: "mail_collection_inquiry"
created_at: "2026-06-05 21:21:17"
updated_at: "2026-07-18T11:03:15-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-008.json"
template_key: master-template
date: 2026-06-05
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a238419-9ab4-83ea-8073-83e79866f593"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Mail Collection Inquiry

## Overview
- **Date**: 2026-06-05 21:21:17
- **Conversation ID**: `6a238419-9ab4-83ea-8073-83e79866f593`
- **Source**: `Chat-Export-28513-2026/conversations-008.json`

## Chat History

### User
> {'asset_pointer': 'sediment://file_00000000125071f59d3ccd55b87ba6c2', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 1536, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 990004, 'width': 710}

### Assistant
> Yep — that looks like **collection / billing / toll-type mail**, not random junk.
> 
> What I can read:
> 
> **Sender block**
> CSPROF47  
> P.O. Box 1280  
> Oaks, PA 19456-1280  
> **Address Service Requested**
> 
> That **P.O. Box 1280 in Oaks, PA** shows up in debt-collection/legal-letter examples, including CBCS collection mail and other billing/collection-style notices. It also appears in a Pennsylvania Turnpike toll invoice sample with a similar **CSPROF48** code, so **CSPROF47 is probably a mail-processing/client code**, not the real company name. citeturn684676search6turn684676search8
> 
> “**Address Service Requested**” means the sender asked USPS to forward/correct/return address info if the mail is undeliverable. Basically: “track this person’s current mailing address.” USPS describes it as forwarding/address-correction handling. citeturn705756search0
> 
> **Do not ignore it.** Open it and send me the inside pages. If it’s a debt collector, you likely have a **30-day dispute/validation window** after receiving the debt validation info. CFPB and FTC both say you can dispute in writing within 30 days; if disputed properly, the collector has to verify before continuing collection. citeturn752638search5turn752638search1turn752638search3
> 
> Immediate move:
> 
> ```text
> Open it.
> Photograph every page front/back.
> Do not call them yet.
> Do not admit the debt.
> Do not pay anything until we identify the creditor, amount, account, dates, and whether it is valid/time-barred/disputable.
> ```
> 
> This is exactly the kind of envelope where we go boring, procedural, and annoying. Paper trail > panic.

### User
> Is there a way to find a Older like like for example, like if I wanna see informed deliveries records from like last year is there something that the USPS all even offered to look at old records cause they’ve been doing a form delivery for a while and I don’t think that they they’re not picking out the mail of the people who signed up obviously so all of us getting scanned so it’s gotta be saved somewhere and I probably for a certain amount of time so I wonder if they would have records from last year we put it this way United States government we know damn well they got the record whether or not USPS as a normal entity can actually like provide it to me somehow is another question and that’s the question I’m asking, but we know that they got everything they don’t throw away nothing you know they don’t

### Assistant
> Yeah — your instinct is right **conceptually**, but the annoying practical answer is: **USPS probably cannot give you last year’s actual Informed Delivery envelope images through normal consumer access.**
> 
> Here’s the clean breakdown.
> 
> ## What USPS lets you see normally
> 
> The **Informed Delivery dashboard only keeps mailpiece images for 7 days**. USPS also says if you got the Daily Digest emails, you can access those images **as long as you kept the emails**. So your best archive is probably your Gmail, not USPS’s dashboard. USPS says the scanned images come from mail processed through automation equipment, mainly letter-size mail, not every flat/large envelope. citeturn836262view0
> 
> ## What USPS says it retains internally
> 
> USPS’s official Informed Delivery system records say:
> 
> - normal mailpiece images: **up to 7 days**
> - cloud-based mailpiece images: **14 days**
> - user data: **2 years, 11 months**
> - cloud audit logs: **13 months** citeturn399523view1
> 
> So, brutal truth: **last year’s envelope image is probably gone unless it’s preserved in your own email.** The government does keep a lot, yes, but agencies also have formal retention/disposal rules. For this specific system, USPS publicly says the image retention window is short.
> 
> ## What may still exist
> 
> Not necessarily the picture, but maybe metadata:
> 
> - Informed Delivery subscription/account records
> - Daily Digest email records
> - email delivery/open/click data
> - audit logs, if still within retention
> - possibly mailpiece data like destination address, Intelligent Mail barcode, delivery point ZIP, and processing equipment ID, depending what system retained it citeturn399523view0
> 
> That may help prove **something was scanned/sent in Informed Delivery**, but it may not recover the actual envelope image.
> 
> ## Best move: search your email first
> 
> Search Gmail for:
> 
> ```text
> from:(USPSInformeddelivery@email.informeddelivery.usps.com)
> ```
> 
> Then narrow by date:
> 
> ```text
> from:(USPSInformeddelivery@email.informeddelivery.usps.com) after:2025/01/01 before:2025/12/31
> ```
> 
> For this specific envelope, try:
> 
> ```text
> "CSPROF47" OR "Oaks PA" OR "P.O. Box 1280" OR "Fulton Pkwy"
> ```
> 
> If Gmail kept those Daily Digest emails, that’s your best evidence source. Boring but effective.
> 
> ## Official request route
> 
> You can file a **USPS Privacy Act / FOIA request** through the USPS FOIA portal. USPS says the portal lets users submit requests, track status, and receive responsive documents. citeturn399523view3 USPS also says people requesting records about themselves should use identity certification, and records about another person need a privacy waiver. citeturn848523view0
> 
> Use wording like this:
> 
> ```text
> I am requesting, under the Privacy Act and FOIA, all records associated with my USPS Informed Delivery account and my address for the date range [DATE RANGE], including Daily Digest email records, mailpiece image metadata, mailpiece data, Intelligent Mail Barcode data if available, delivery point ZIP data, email delivery logs, audit logs, and any records showing scanned mailpieces sent to my Informed Delivery notifications.
> 
> I understand actual mailpiece images may be subject to retention limits, but I request any retained metadata or related records from USPS 820.300 Informed Delivery and related systems.
> ```
> 
> Translation: don’t ask only for “images,” because they’ll likely say “not retained.” Ask for **records and metadata** too. That’s where the little gremlins hide the receipts.
