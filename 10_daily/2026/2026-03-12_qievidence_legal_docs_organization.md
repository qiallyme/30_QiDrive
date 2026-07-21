---
layout: page
title: "QiEvidence - Legal Docs Organization"
slug: "qievidence_legal_docs_organization"
created_at: "2026-03-12 02:20:17"
updated_at: "2026-07-18T11:03:14-04:00"
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
date: 2026-03-12
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69b2690a-7af0-8327-8ba6-62f9c46628b7"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# QiEvidence - Legal Docs Organization

## Overview
- **Date**: 2026-03-12 02:20:17
- **Conversation ID**: `69b2690a-7af0-8327-8ba6-62f9c46628b7`
- **Source**: `Chat-Export-28513-2026/conversations-004.json`

## Chat History

### User
> how should i document e notices for case filings, docket entriesa with docket pdfs, and overall my case stratagies, evidence an such inside capacities.

### Assistant
> Alright — let’s design this so **Capacities works like your case brain**, not just a dumping ground. You want three things simultaneously:
> 
> 1. **Chronology (what happened when)**  
> 2. **Evidence vault (documents + exhibits)**  
> 3. **Strategy layer (your thinking, arguments, risks)**  
> 
> If you don’t separate those, everything turns into chaos fast.
> 
> ---
> 
> # Capacities Structure for Your Legal Case
> 
> Create **four object types**.
> 
> ```
> Case
> Filing / Docket Entry
> Evidence / Exhibit
> Strategy / Argument
> ```
> 
> Everything links to the **Case** object.
> 
> ---
> 
> # 1. Case Object (Top Level)
> 
> Example:
> 
> ```
> Case: FCFCU Foreclosure Dispute
> Case Number: 49D03-2501-MF-002559
> Court: Marion Superior Court 3
> Judge: Gary Miller
> Status: Active
> ```
> 
> Properties:
> 
> ```
> case_number
> court
> judge
> opposing_party
> phase
> status
> key_deadlines
> ```
> 
> Sections inside the page:
> 
> ```
> Overview
> Timeline
> Active Motions
> Evidence Index
> Strategy Notes
> Regulatory Complaints
> ```
> 
> This becomes the **command center page**.
> 
> ---
> 
> # 2. Docket / Filing Entries
> 
> Every filing or notice gets its **own object**.
> 
> Example:
> 
> ```
> Object Type: Filing
> Title: Order Setting Hearing
> Date: 2026-03-11
> Filed By: Court
> Docket Entry #: optional
> ```
> 
> Properties:
> 
> ```
> date
> filed_by
> document_type
> status
> related_motion
> impact_level
> ```
> 
> Attach the **PDF of the filing**.
> 
> Then summarize like this:
> 
> ```
> Summary
> Court scheduled hearing for March 27.
> 
> Implication
> Court moving forward despite pending objection.
> 
> My Response
> Filed objection and exhibits.
> 
> Risk
> Court may proceed unless objection acknowledged.
> ```
> 
> Why this matters:  
> Later you can filter:
> 
> ```
> All filings by court
> All filings by plaintiff
> All orders
> All motions
> ```
> 
> ---
> 
> # 3. Evidence / Exhibits
> 
> Evidence should **not** be inside filings.
> 
> Make a separate object type.
> 
> Example:
> 
> ```
> Object Type: Evidence
> Title: Sheriff's Deed Recording Delay
> Category: Property Transfer
> Date: 2025-12-02
> Source: County Recorder
> Exhibit #: E-12
> ```
> 
> Properties:
> 
> ```
> exhibit_number
> source
> date
> evidence_type
> credibility
> used_in_motion
> ```
> 
> Then summarize:
> 
> ```
> What it shows
> Sheriff deed recorded Dec 2.
> 
> Why it matters
> Confirms ownership change shortly before eviction.
> 
> Legal relevance
> Supports lack of notice argument.
> ```
> 
> Attach:
> 
> ```
> PDF
> Screenshot
> Transcript
> Photos
> ```
> 
> ---
> 
> # 4. Strategy / Arguments
> 
> This is where you put your thinking.
> 
> Example:
> 
> ```
> Object Type: Strategy
> Title: Lack of Service Defense
> Type: Legal Theory
> Strength: High
> ```
> 
> Structure:
> 
> ```
> Argument
> Court lacked jurisdiction due to improper service.
> 
> Evidence Supporting
> E-04 sheriff return defects
> E-12 sheriff deed timeline
> E-15 lack of posting photos
> 
> Weakness
> Court already ruled service sufficient.
> 
> Next Move
> Raise again on appeal or due process violation.
> ```
> 
> ---
> 
> # 5. Timeline Object (Optional but powerful)
> 
> Capacities works really well if you make **timeline entries**.
> 
> Example:
> 
> ```
> Object: Event
> 
> Title: Writ of Assistance Executed
> Date: 2025-12-09
> Type: Enforcement Action
> ```
> 
> Links:
> 
> ```
> Related Filing
> Related Evidence
> Related Strategy
> ```
> 
> Then your case timeline becomes automatic.
> 
> ---
> 
> # What This Looks Like
> 
> Inside the **Case page** you’ll see:
> 
> ```
> CASE: FCFCU FORECLOSURE
> 
> Timeline
> 2025-12-02 sheriff deed recorded
> 2025-12-09 writ executed
> 2026-01-09 hearing
> 
> Filings
> Order Setting Hearing
> Motion to Vacate
> Objection to Hearing
> 
> Evidence
> Sheriff deed
> Notice defects
> Transcript
> 
> Strategy
> Jurisdiction challenge
> Accounting discrepancy
> Surplus funds claim
> ```
> 
> Everything is linked.
> 
> No chaos.
> 
> ---
> 
> # Naming Standard (important)
> 
> Name things consistently.
> 
> ```
> FILING_2026-03-11_Order_Setting_Hearing
> FILING_2026-03-10_Objection_to_Hearing
> 
> EVID_E12_Sheriff_Deed_Record
> EVID_E15_No_Notice_Posting
> 
> STRAT_Jurisdiction_Service_Defect
> STRAT_Surplus_Funds_Claim
> ```
> 
> This matters when exporting later.
> 
> ---
> 
> # Where to Put Docket PDFs
> 
> Attach them to the **Filing object**.
> 
> Inside the page:
> 
> ```
> PDF
> Summary
> Impact
> Links to evidence
> Links to strategy
> ```
> 
> ---
> 
> # Why Capacities Works Well For This
> 
> Because it behaves like a **knowledge graph**.
> 
> You can click:
> 
> ```
> Evidence → which motions used it
> Strategy → which evidence supports it
> Filing → what it affects
> ```
> 
> You start seeing patterns instantly.
> 
> ---
> 
> # One More Tip (critical)
> 
> Create a **“Judge Reaction” field** for filings.
> 
> ```
> judge_response
> accepted
> denied
> ignored
> pending
> ```
> 
> Courts often **ignore filings without formally denying them**.
> 
> Tracking that pattern is extremely useful later.
> 
> ---
> 
> # If you want, I can also show you a **much more powerful structure** most pro litigators use:
> 
> **The Litigation Pyramid**
> 
> ```
> FACTS
> ↓
> EVIDENCE
> ↓
> LEGAL THEORY
> ↓
> MOTIONS
> ↓
> COURT RESPONSE
> ```
> 
> If you build Capacities around that model, your case becomes **ridiculously easy to navigate and explain**.

### User
> a case would just be a project no or is a good to have it as a seperate objwect, then strategy is like a notice, evidence if like a file, filing is like a document, are you sure its better to seperate?

### Assistant
> Short answer: **yes — separate them.**  
> Using only *project / note / document / file* will work at first, but once you have **50+ filings, exhibits, transcripts, and strategy notes**, it becomes impossible to filter or analyze.
> 
> You’re essentially building a **litigation knowledge graph**, not a notebook.
> 
> Let me break it down in practical terms.
> 
> ---
> 
> # The Two Ways You Could Do It
> 
> ## Option A — Simple (Projects + Notes)
> 
> Structure:
> 
> ```
> Project
>    ├─ Notes (strategy)
>    ├─ Documents (filings)
>    └─ Files (evidence)
> ```
> 
> Example:
> 
> ```
> Project: FCFCU Foreclosure
> 
> Notes
>    Service Defect Argument
>    Surplus Funds Strategy
> 
> Documents
>    Motion to Vacate
>    Order Setting Hearing
> 
> Files
>    Sheriff's Deed
>    Transcript
> ```
> 
> ### Pros
> • quick to set up  
> • fewer object types
> 
> ### Cons
> • cannot easily filter  
> • timeline becomes messy  
> • filings, strategy, and evidence get mixed  
> • hard to see relationships later
> 
> For **serious cases**, this becomes a problem fast.
> 
> ---
> 
> # Option B — Structured Case Model (recommended)
> 
> Objects:
> 
> ```
> Case
> Filing
> Evidence
> Strategy
> Event
> ```
> 
> Then everything links together.
> 
> Example:
> 
> ```
> Case
>    FCFCU Foreclosure
> ```
> 
> Connected objects:
> 
> ```
> Filing
>    Motion to Vacate
> 
> Evidence
>    Sheriff's Deed
>    Transcript
> 
> Strategy
>    Lack of Service Argument
> 
> Event
>    Writ of Assistance Executed
> ```
> 
> Now you can answer questions instantly:
> 
> ```
> Show all filings
> Show all evidence used in Motion to Vacate
> Show all events between Dec 1 and Dec 9
> Show all strategy tied to surplus funds
> ```
> 
> That becomes **powerful fast**.
> 
> ---
> 
> # The Key Concept
> 
> You're separating **WHAT something is**.
> 
> | Thing | Purpose |
> |---|---|
> | Case | container / command center |
> | Filing | what was filed with court |
> | Evidence | proof |
> | Strategy | your thinking |
> | Event | what happened |
> 
> They are fundamentally different things.
> 
> ---
> 
> # Think of it like a criminal investigation board
> 
> Not everything is the same type of item.
> 
> ```
> Case
> │
> ├ Evidence (photos, documents)
> ├ Events (timeline)
> ├ Motions (filings)
> └ Theories (strategy)
> ```
> 
> That’s why separating them works better.
> 
> ---
> 
> # Why this matters for YOU specifically
> 
> Your case already has:
> 
> • filings  
> • court orders  
> • transcripts  
> • sheriff documents  
> • financial evidence  
> • strategy notes  
> • regulatory complaints  
> 
> That’s **six different types of information**.
> 
> If you dump them all into notes, you'll lose structure.
> 
> ---
> 
> # What I Actually Recommend for Capacities
> 
> Keep it lean:
> 
> ### Objects
> 
> ```
> Case
> Filing
> Evidence
> Strategy
> Event
> ```
> 
> That’s it.
> 
> Five types only.
> 
> ---
> 
> # How they connect
> 
> ```
> Case
>    ↳ Filing
>         ↳ Evidence
>         ↳ Strategy
>    ↳ Event
> ```
> 
> Example:
> 
> ```
> Motion to Vacate
>    uses evidence → Sheriff Deed
>    supports strategy → Service Defect
> ```
> 
> ---
> 
> # This also prepares you for something important later
> 
> If you export the case into:
> 
> • court filings  
> • legal binders  
> • AI analysis  
> • appeals  
> 
> having **structured evidence + arguments** saves massive time.
> 
> ---
> 
> # My honest advice for your situation
> 
> You’re doing **serious litigation documentation**.
> 
> Use the structured model.
> 
> It takes **10 minutes more upfront** and saves **hundreds of hours later**.
> 
> ---
> 
> # If you want, I can also show you something extremely powerful:
> 
> How to structure the case so Capacities automatically generates:
> 
> • **timeline of the case**  
> • **evidence index**  
> • **motion binder**  
> • **exhibit list**
> 
> Basically turning Capacities into a **litigation command center**.
> 
> It’s only about **8 properties and 3 templates**, but it makes the whole system run itself.

### User
> you dont think we need orders, docket, violations, legal theories, or lanes as objects?

### Assistant
> You’re asking the **right question**, because this is where people either build a clean legal system… or create a 20-object monster that becomes unusable.
> 
> Short answer:
> 
> **You do NOT want too many object types.**  
> Most things you listed should be **types or properties**, not separate objects.
> 
> Think **database normalization vs usability**.
> 
> ---
> 
> # The Rule for Object Types
> 
> Create an object only when:
> 
> 1. It has **its own lifecycle**
> 2. It needs **relationships to many things**
> 3. You will **query/filter it frequently**
> 
> If it doesn’t meet those criteria → **property, tag, or subtype**.
> 
> ---
> 
> # What I Would Actually Use
> 
> ### Objects (the core system)
> 
> ```
> Case
> Filing
> Evidence
> Event
> Strategy
> ```
> 
> That’s it.
> 
> Everything else fits inside those.
> 
> ---
> 
> # Where Your Suggestions Fit
> 
> ## Orders
> 
> Not a separate object.
> 
> Orders are just a **type of filing**.
> 
> Example:
> 
> ```
> Object: Filing
> type: Order
> title: Order Setting Hearing
> date: 2026-03-11
> ```
> 
> Filings include:
> 
> ```
> Motion
> Order
> Notice
> Brief
> Transcript
> Judgment
> ```
> 
> So you filter:
> 
> ```
> type = Order
> ```
> 
> ---
> 
> ## Docket
> 
> The docket is not a thing.
> 
> It is just:
> 
> ```
> All filings sorted by date
> ```
> 
> So Capacities automatically becomes the docket.
> 
> You just create a query view:
> 
> ```
> All filings
> sort by date
> ```
> 
> Boom — docket.
> 
> ---
> 
> ## Violations
> 
> These **should be an object** if you’re tracking misconduct.
> 
> Example:
> 
> ```
> Violation
> ```
> 
> Properties:
> 
> ```
> actor
> rule
> date
> severity
> related evidence
> related filing
> ```
> 
> Example entry:
> 
> ```
> Violation: Failure to Serve Notice
> Actor: Plaintiff
> Rule: Indiana Trial Rule 4
> Evidence: E12 Sheriff Return
> ```
> 
> This becomes powerful if you later file:
> 
> ```
> sanctions
> appeal
> civil rights complaint
> ```
> 
> ---
> 
> ## Legal Theories
> 
> These are just **Strategy objects**.
> 
> Example:
> 
> ```
> Strategy: Lack of Jurisdiction
> Strategy: Service Defect
> Strategy: Surplus Funds Entitlement
> Strategy: Accounting Manipulation
> ```
> 
> They link to:
> 
> ```
> Evidence
> Filings
> Violations
> ```
> 
> So no separate object needed.
> 
> ---
> 
> ## Lanes
> 
> You’re thinking like a litigator here.
> 
> Lanes are **case dimensions**.
> 
> But they should be a **property**, not objects.
> 
> Example property on filings or evidence:
> 
> ```
> lane
> ```
> 
> Possible values:
> 
> ```
> Foreclosure
> Service Defect
> Surplus Funds
> Accounting
> Due Process
> Eviction Conduct
> ```
> 
> Then you can filter:
> 
> ```
> show all filings in lane: surplus funds
> ```
> 
> ---
> 
> # The Final Model (clean and powerful)
> 
> Objects:
> 
> ```
> Case
> Filing
> Evidence
> Event
> Strategy
> Violation
> ```
> 
> Six objects total.
> 
> That’s the sweet spot.
> 
> ---
> 
> # How They Relate
> 
> ```
> Case
>  │
>  ├ Filing
>  │   ├ Evidence
>  │   ├ Strategy
>  │   └ Violations
>  │
>  ├ Event
>  │
>  ├ Evidence
>  │
>  └ Strategy
> ```
> 
> ---
> 
> # Real Example
> 
> ```
> Case
>    FCFCU Foreclosure
> ```
> 
> Connected objects:
> 
> ```
> Filing
>    Motion to Vacate
> 
> Evidence
>    Sheriff's Deed Recording
> 
> Strategy
>    Lack of Service
> 
> Violation
>    Failure to Provide Notice
> 
> Event
>    Writ of Assistance Executed
> ```
> 
> Everything links.
> 
> ---
> 
> # Why This Works
> 
> You get automatic views like:
> 
> **Docket**
> 
> ```
> All filings sorted by date
> ```
> 
> **Evidence Index**
> 
> ```
> All evidence grouped by lane
> ```
> 
> **Violation Log**
> 
> ```
> All violations grouped by actor
> ```
> 
> **Strategy Map**
> 
> ```
> All strategies linked to evidence
> ```
> 
> ---
> 
> # One thing most people miss (this matters)
> 
> Create a property called:
> 
> ```
> impact
> ```
> 
> Values:
> 
> ```
> critical
> high
> medium
> low
> ```
> 
> Courts bury important facts inside huge filings.
> 
> This lets you surface **the 5 things that actually matter**.
> 
> ---
> 
> # My honest recommendation
> 
> Don’t overbuild.
> 
> Start with:
> 
> ```
> Case
> Filing
> Evidence
> Strategy
> Event
> Violation
> ```
> 
> Then add properties:
> 
> ```
> lane
> impact
> actor
> status
> ```
> 
> That structure will handle **thousands of records** without breaking.
> 
> ---
> 
> If you want, I can also show you something that would help your case massively:
> 
> **How to structure the system so Capacities automatically builds your**
> 
> - **litigation timeline**
> - **exhibit list**
> - **motion binder**
> - **sanctions log**
> 
> Basically turning it into a **litigation command center** instead of just notes.

### User
> im at violations right now im callign them case_issues, i need to know property types, like object select, text, blocks, description ect, too. and how do i link the other bojectes to the case object, do i do properties or enter objected in the body of the case?

### Assistant
> You’re right at the point where **schema matters**. If you get this wrong now, the whole system becomes messy later. So let’s set it up clean.
> 
> Also: **yes — calling them `case_issues` is better than violations.**  
> That lets you track:
> 
> - procedural errors  
> - misconduct  
> - legal defects  
> - accounting discrepancies  
> - jurisdiction issues  
> 
> without sounding accusatory everywhere.
> 
> ---
> 
> # 1. Case_Issues Object Schema
> 
> Create object type:
> 
> ```
> case_issue
> ```
> 
> Use these properties.
> 
> ### Core Properties
> 
> | Property | Type | Purpose |
> |---|---|---|
> | title | title | name of issue |
> | case | object | link to case |
> | status | select | open / investigating / proven / dismissed |
> | severity | select | critical / high / medium / low |
> | lane | select | legal category |
> | actor | select | who caused issue |
> | rule_or_law | text | rule violated |
> | discovered_date | date | when you noticed |
> | filing_related | object | filing connected |
> | evidence | object | supporting evidence |
> | strategy | object | argument tied to it |
> 
> ---
> 
> ### Example Entry
> 
> ```
> Case Issue: Lack of Service Notice
> 
> case: FCFCU Foreclosure
> status: open
> severity: critical
> lane: service_defect
> actor: plaintiff
> rule_or_law: Indiana Trial Rule 4
> discovered_date: 2026-01-09
> ```
> 
> Body section:
> 
> ```
> Summary
> Plaintiff claims service completed but no notice was posted or mailed.
> 
> Evidence
> E12 Sheriff return discrepancy
> Photos showing no posting
> 
> Legal Impact
> Jurisdiction challenge.
> ```
> 
> ---
> 
> # 2. Property Types Explained
> 
> Use these types inside Capacities.
> 
> | Type | Use |
> |---|---|
> | text | short values |
> | select | dropdown |
> | multi-select | multiple values |
> | object | link to another object |
> | date | timeline |
> | number | optional scoring |
> | url | external references |
> | blocks | long notes |
> 
> ---
> 
> # Recommended property types for case_issue
> 
> ```
> case → object
> status → select
> severity → select
> lane → select
> actor → select
> rule_or_law → text
> discovered_date → date
> filing_related → object
> evidence → object (multi)
> strategy → object
> ```
> 
> ---
> 
> # 3. How Objects Should Link
> 
> You asked the **most important architecture question**:
> 
> > Do I link objects with properties or inside the body?
> 
> Answer:
> 
> **Use BOTH, but for different purposes.**
> 
> ---
> 
> ## Use Properties for STRUCTURE
> 
> Example:
> 
> ```
> case_issue
> case → FCFCU Foreclosure
> evidence → Sheriff Deed
> filing_related → Motion to Vacate
> ```
> 
> This lets Capacities:
> 
> - filter
> - build tables
> - generate lists
> - build timelines
> 
> ---
> 
> ## Use Body Links for CONTEXT
> 
> Inside the page:
> 
> ```
> This issue became clear after reviewing [[Motion to Vacate]]
> 
> Supporting evidence includes [[Sheriff Deed Recording]]
> ```
> 
> Body links help reading.
> 
> Properties power the system.
> 
> ---
> 
> # 4. Case Object Structure
> 
> Your **case page becomes the command center**.
> 
> Properties:
> 
> ```
> case_number → text
> court → text
> judge → text
> status → select
> phase → select
> ```
> 
> ---
> 
> Inside the case body create sections:
> 
> ```
> Overview
> 
> Key Filings
> 
> Evidence Index
> 
> Case Issues
> 
> Strategy
> 
> Timeline
> ```
> 
> Then embed objects.
> 
> Example:
> 
> ```
> /embed case_issue where case = this case
> /embed filing where case = this case
> /embed evidence where case = this case
> ```
> 
> Now the page auto-populates.
> 
> ---
> 
> # 5. Example Relationship
> 
> ```
> Case
>    FCFCU Foreclosure
> ```
> 
> Linked objects:
> 
> ```
> Case Issue
>    Lack of Service
> 
> Filing
>    Motion to Vacate
> 
> Evidence
>    Sheriff Deed
> 
> Strategy
>    Jurisdiction Challenge
> ```
> 
> Each object contains:
> 
> ```
> case → FCFCU Foreclosure
> ```
> 
> So everything connects automatically.
> 
> ---
> 
> # 6. Lane Categories I Recommend
> 
> Create select list:
> 
> ```
> service_defect
> foreclosure_process
> surplus_funds
> accounting_discrepancy
> eviction_execution
> due_process
> civil_rights
> regulatory
> ```
> 
> ---
> 
> # 7. Severity Scale
> 
> ```
> critical
> high
> moderate
> low
> note
> ```
> 
> Critical = affects jurisdiction or damages.
> 
> ---
> 
> # 8. Status Values
> 
> ```
> open
> investigating
> supported
> resolved
> dismissed
> ```
> 
> ---
> 
> # 9. One Advanced Property (very useful)
> 
> Add:
> 
> ```
> impact_score → number
> ```
> 
> Example:
> 
> ```
> 10 = case altering
> 7 = major argument
> 5 = supporting argument
> 3 = contextual
> 1 = minor
> ```
> 
> Later you can sort by importance.
> 
> ---
> 
> # 10. Final Architecture
> 
> Objects you should have:
> 
> ```
> case
> filing
> evidence
> event
> strategy
> case_issue
> ```
> 
> Relationships:
> 
> ```
> case_issue
>    ↳ evidence
>    ↳ filing
>    ↳ strategy
>    ↳ case
> ```
> 
> ---
> 
> # One last tip (this will help you a LOT)
> 
> Create a **property on filings**:
> 
> ```
> court_response → select
> ```
> 
> Values:
> 
> ```
> granted
> denied
> ignored
> pending
> ```
> 
> Courts ignore filings constantly.
> 
> Tracking this pattern helps later.
> 
> ---
> 
> If you want, I can also show you a **much more powerful setup** most pro litigators use:
> 
> A **litigation intelligence board** where Capacities automatically generates:
> 
> - case timeline  
> - issue tracker  
> - evidence binder  
> - motion index  
> 
> from the same objects you’re creating right now.

### User
> how would you recommend i enter the docket, as event, and the documents in teh event listed as related object filings, Case Summary

> Financial Center First Credit Union v. Cody Rice-Velasquez, American Express National Bank, N.A., JP Morgan Chase Bank, N.A.

> Case Number	49D03-2501-MF-002559

> Court	Marion Superior Court 3

> Type	MF - Mortgage Foreclosure

> Filed	01/16/2025

> Status	05/28/2025 , Decided

> Parties to the Case

> Hide all party details

> Defendant	Rice-Velasquez, Cody

> Address3137 Melbourne Road Drive S,

> Indianapolis, IN 46228

> AttorneyPro Se

> Defendant	American Express National Bank, N.A.

> Address115 W. Towne Ridge Parkway

> Sandy, UT 84070

> Defendant	JP Morgan Chase Bank, N.A.

> Address1111 Polaris Parkway

> Columbus, OH 43240

> Plaintiff	Financial Center First Credit Union

> Address7101 E. 56th Street

> Indianapolis, IN 46226

> AttorneyMichael E. Farrer

> #678449, Lead, Retained

> Attorney address 1601 South Anderson Street

> P.O. Box 494

> Elwood, IN 46036

> Attorney phone 765-552-9878(W)

> AttorneyScott Andrew Kainrath

> #2606949, Retained

> Attorney address 1601 S. Anderson Street

> P.O. Box 494

> Elwood, IN 46036

> Attorney phone 765-687-1000(W)

> AttorneyFelix O'Neill Rippy

> #1751918, Retained

> Attorney address Welch & Company LLC

> 117 E Charles St, Ste 201

> PO Box 428

> Muncie, IN 47308

> Attorney phone 765-282-9501(W)

> Chronological Case Summary

> 01/16/2025	

> Case Opened as a New Filing

> 01/16/2025	

> Complaint/Equivalent Pleading Filed

> Complaint on Notes and to Foreclose Mortgages

> Filed By:Financial Center First Credit Union

> File Stamp:01/16/2025

> 01/16/2025	

> Appearance Filed

> Appearance

> For Party:Financial Center First Credit Union

> File Stamp:01/16/2025

> 01/16/2025	

> Request for Admissions

> Request for Admissions

> Filed By:Financial Center First Credit Union

> File Stamp:01/16/2025

> 01/16/2025	

> Notice Filed

> Notice to Homeowners, Contract Buyers, and Renters

> Filed By:Financial Center First Credit Union

> File Stamp:01/16/2025

> 01/16/2025	

> Appearance Filed

> Appearance

> For Party:Financial Center First Credit Union

> File Stamp:01/16/2025

> 01/16/2025	

> Subpoena/Summons Filed

> Summons

> Filed By:Financial Center First Credit Union

> File Stamp:01/16/2025

> 01/16/2025	

> Subpoena/Summons Filed

> Summons

> Filed By:Financial Center First Credit Union

> File Stamp:01/16/2025

> 01/16/2025	

> Subpoena/Summons Filed

> Summons

> Filed By:Financial Center First Credit Union

> File Stamp:01/16/2025

> 01/16/2025	

> Subpoena/Summons Filed

> Summons

> Filed By:Financial Center First Credit Union

> File Stamp:01/16/2025

> 01/16/2025	

> Subpoena/Summons Filed

> Summons

> Filed By:Financial Center First Credit Union

> File Stamp:01/16/2025

> 03/03/2025	

> Service Issued

> SUMM

> Serve To:Rice-Velasquez, Cody

> 03/05/2025	

> Service Returned Served

> C1 COPY LEFT AND MAILED @ 4817 SHADOW PT. DR.46254 -20354

> Party Served:Rice-Velasquez, Cody

> 04/09/2025	

> Service Issued

> SUMM

> Serve To:Rice-Velasquez, Cody

> 04/15/2025	

> Service Returned Served

> C1- COPY LEFT AND MAILED TO ADDRESS PROVIDED- 32939

> Party Served:Rice-Velasquez, Cody

> 05/13/2025	

> Motion for Default Judgment Filed

> Motion for Default Judgment Entry and Decree of Foreclosure

> Filed By:Financial Center First Credit Union

> File Stamp:05/13/2025

> 05/13/2025	

> Affidavit Filed

> Affidavit

> Filed By:Financial Center First Credit Union

> File Date:05/13/2025

> 05/13/2025	

> Affidavit in Support of Attorney fees

> Affidavit in Support of Attorney Fees

> Filed By:Financial Center First Credit Union

> File Date:05/13/2025

> 05/21/2025	

> Order Denying Motion for Default Judgment

> Default Judgment Entry and Decree of Foreclosure is denied. No return of service on American Express or JP Morgan Chase.

> Judicial Officer:Hannah, Therese A - MAG

> Order Signed:05/21/2025

> 05/21/2025	

> Notice Filed

> Omitted Notice of Service

> Filed By:Financial Center First Credit Union

> File Stamp:05/21/2025

> 05/22/2025	

> Automated Paper Notice Issued to Parties

> Order Denying Motion for Default Judgment ---- 5/21/2025 : Cody Rice-Velasquez;American Express National Bank, N.A.;JP Morgan Chase Bank, N.A.

> 05/22/2025	

> Automated ENotice Issued to Parties

> Order Denying Motion for Default Judgment ---- 5/21/2025 : Felix O'Neill Rippy;Michael E. Farrer

> 05/23/2025	

> Motion Filed

> Request to Enter Amended Default Judgment and Decree of Foreclosure

> Filed By:Financial Center First Credit Union

> File Stamp:05/23/2025

> 05/28/2025	

> Order Granting Motion for Default Judgment

> Amended Default Judgment Entry and Decree of Foreclosure.

> Judicial Officer:Hannah, Therese A - MAG

> Order Signed:05/28/2025

> 05/28/2025	

> Default Judgment entered

> Judicial Officer:Hannah, Therese A - MAG

> Comment: 

> (Default Judgment and Decree of Foreclosure; address commonly known as 4817 Shadow Pointe Drive, Indianapolis, Indiana 46254; total amount of $220,863.09)

> 05/29/2025	

> Automated ENotice Issued to Parties

> Order Granting Motion for Default Judgment ---- 5/28/2025 : Felix O'Neill Rippy;Michael E. Farrer

> 05/29/2025	

> Automated Paper Notice Issued to Parties

> Order Granting Motion for Default Judgment ---- 5/28/2025 : Cody Rice-Velasquez;American Express National Bank, N.A.;JP Morgan Chase Bank, N.A.

> 05/30/2025	

> Praecipe for Order of Sale

> Praecipe for Sheriff's Sale

> Filed By:Financial Center First Credit Union

> File Stamp:05/29/2025

> 06/13/2025	

> Decree of Foreclosure Sent to Sheriff for Sale

> Issued to Sheriff for the 8/15/25 Sheriff Sale

> 07/09/2025	

> Service Returned Served

> NOTICE OF SHERIFF SALE POSTED AT 4817 SHADOW POINTE DR 46254 - 32939

> Party Served:Rice-Velasquez, Cody

> 07/17/2025	

> Notice Filed

> Plaintiff's Bid

> Filed By:Financial Center First Credit Union

> File Stamp:07/17/2025

> 09/09/2025	

> Decree of Foreclosure Returned

> Fully Satisfied on 08/15/25 Sheriff Sale, Total Paid $240,464.20, Sale #032

> File Stamp:09/09/2025

> 09/09/2025	

> Clerk Releases Judgment

> By Sheriff Sale

> 10/29/2025	

> Petition Filed

> Petition for Entry of Writ of Assistance

> Filed By:Financial Center First Credit Union

> File Stamp:10/29/2025

> 10/29/2025	

> Document Filed

> Writ of Assistance

> Filed By:Financial Center First Credit Union

> File Stamp:10/29/2025

> 11/06/2025	

> Order for Writ

> Order for writ of assistance.

> Judicial Officer:Hannah, Therese A - MAG

> Order Signed:11/06/2025

> 11/07/2025	

> Automated Paper Notice Issued to Parties

> Order for Writ ---- 11/6/2025 : Cody Rice-Velasquez;American Express National Bank, N.A.;JP Morgan Chase Bank, N.A.

> 11/07/2025	

> Automated ENotice Issued to Parties

> Order for Writ ---- 11/6/2025 : Felix O'Neill Rippy;Michael E. Farrer

> 12/11/2025	

> Motion to Set Aside/Vacate Judgment Filed

> Motion to Vacate Void Judgment under TR 60(B)(6) and 60(B)(1)

> Filed By:Rice-Velasquez, Cody

> File Stamp:12/10/2025

> 12/11/2025	

> Motion to Quash Filed

> Emergency Motion to Stay Writ of Assistance and Protect Property

> Filed By:Rice-Velasquez, Cody

> File Stamp:12/10/2025

> 12/11/2025	

> Witness and/or Exhibit List Filed

> Exhibit List Exhibits AG

> Filed By:Rice-Velasquez, Cody

> File Stamp:12/10/2025

> 12/11/2025	

> Hearing Scheduling Activity

> Hearing on Motion to Set Aside/Vacate Judgment scheduled for 01/09/2026 at 9:30 AM.

> 12/11/2025	

> Order Denying

> Order Denying Motion Staying Writ of Assistance

> Judicial Officer:Hannah, Therese A - MAG

> Order Signed:12/11/2025

> 12/11/2025	

> Order for Hearing

> Order Setting Defendant's Motion to Set Aside Judgment for Hearing

> Judicial Officer:Hannah, Therese A - MAG

> Order Signed:12/11/2025

> 12/12/2025	

> Automated Paper Notice Issued to Parties

> Hearing Scheduling Activity ---- 12/11/2025 : American Express National Bank, N.A.;JP Morgan Chase Bank, N.A. Order Denying ---- 12/11/2025 : American Express National Bank, N.A.;JP Morgan Chase Bank, N.A. Order for Hearing ---- 12/11/2025 : American Express National Bank, N.A.;JP Morgan Chase Bank, N.A.

> 12/12/2025	

> Automated ENotice Issued to Parties

> Hearing Scheduling Activity ---- 12/11/2025 : Cody Rice-Velasquez;Felix O'Neill Rippy;Michael E. Farrer Order Denying ---- 12/11/2025 : Cody Rice-Velasquez;Felix O'Neill Rippy;Michael E. Farrer Order for Hearing ---- 12/11/2025 : Cody Rice-Velasquez;Felix O'Neill Rippy;Michael E. Farrer

> 12/12/2025	

> Motion Filed

> Supplemental Emergency Motion for Temporary Access or Temporary Limited Re-Entry Pending January 9 Hearing

> Filed By:Rice-Velasquez, Cody

> File Stamp:12/11/2025

> 12/12/2025	

> Notice Filed

> Report to Court on Defendant's Request to Obtain Personal Item

> Filed By:Financial Center First Credit Union

> File Stamp:12/12/2025

> 12/16/2025	

> Declaration Filed

> Emergency Supplemental Declaration of Cody Rice-Velasquez (Continuing Irreparable Harm, ADA Necessity, Non-Waiver)

> Filed by:Rice-Velasquez, Cody

> File Stamp:12/16/2025

> 12/16/2025	

> Motion Filed

> Emergency Motion to Preserve and Account for Foreclosure Sale Surplus Funds

> Filed By:Rice-Velasquez, Cody

> File Stamp:12/16/2025

> 12/17/2025	

> Notice Issued

> Motion for Surplus Funds will be heard at the 1/9/26 Hearing

> 12/17/2025	

> Notice Filed

> Report to Sheriff's Sale and Report of No Excess Proceeds

> Filed By:Financial Center First Credit Union

> File Stamp:12/17/2025

> 12/18/2025	

> Automated ENotice Issued to Parties

> Notice Issued ---- 12/17/2025 : Cody Rice-Velasquez;Felix O'Neill Rippy;Michael E. Farrer

> 12/18/2025	

> Automated Paper Notice Issued to Parties

> Notice Issued ---- 12/17/2025 : American Express National Bank, N.A.;JP Morgan Chase Bank, N.A.

> 12/22/2025	

> Notice Filed

> Declaration of Defendant regarding ongoing displacement, economic harm, removal and retrieval conduct, and interference with access to the courts.

> Filed By:Rice-Velasquez, Cody

> File Stamp:12/22/2025

> 01/09/2026	

> Hearing on Motion to Set Aside/Vacate Judgment

> Session:01/09/2026 9:30 AM, Judicial Officer: Hannah, Therese A - MAG

> Comment:in person

> Result:Commenced and concluded

> 01/09/2026	

> Hearing Journal Entry

> Hearing on Motion to Set Aside and Motion to Release Funds conducted in room C0934; Plaintiff appears via counsel Scott Kainrath; Defendant Cody Rice- Velasquez appears without counsel; Argument heard; The Court to issue an Order

> Judicial Officer:Hannah, Therese A - MAG

> 01/09/2026	

> Appearance Filed

> APPEARANCE FORM CIVIL LITIGATION

> For Party:Financial Center First Credit Union

> File Stamp:01/09/2026

> 01/21/2026	

> Order Issued

> Order from January 9, 2026 Hearing on Motion to Set Aside Judgment

> Judicial Officer:Hannah, Therese A - MAG

> Order Signed:01/20/2026

> 01/22/2026	

> Automated Paper Notice Issued to Parties

> Order Issued ---- 1/21/2026 : American Express National Bank, N.A.;JP Morgan Chase Bank, N.A.

> 01/22/2026	

> Automated ENotice Issued to Parties

> Order Issued ---- 1/21/2026 : Cody Rice-Velasquez;Felix O'Neill Rippy;Michael E. Farrer;Scott Andrew Kainrath

> 02/09/2026	

> Notice Filed

> Notice of Appeal

> Filed By:Rice-Velasquez, Cody

> File Stamp:02/09/2026

> 02/20/2026	

> Petition Filed

> Petition to Pay Surplus Funds to the Clerk of the Court

> Filed By:Financial Center First Credit Union

> File Stamp:02/20/2026

> 02/24/2026	

> Petition Filed

> Petition for Disposition of Surplus and Motion for Nunc Pro Tunc

> Filed By:Financial Center First Credit Union

> File Stamp:02/24/2026

> 02/26/2026	

> Order Denying

> Order Denying Petition for Nunc Pro Tunc

> Judicial Officer:Hannah, Therese A - MAG

> Order Signed:02/26/2026

> 02/27/2026	

> Automated Paper Notice Issued to Parties

> Order Denying ---- 2/26/2026 : American Express National Bank, N.A.;JP Morgan Chase Bank, N.A.

> 02/27/2026	

> Automated ENotice Issued to Parties

> Order Denying ---- 2/26/2026 : Cody Rice-Velasquez;Felix O'Neill Rippy;Michael E. Farrer;Scott Andrew Kainrath

> 02/27/2026	

> Objection Filed

> Motion ??? Defendant???s Consolidated Objection to Plaintiff???s Requested Modification of Credit Bid and Request for Evidentiary Hearing

> Filed By:Rice-Velasquez, Cody

> File Stamp:02/26/2026

> 02/27/2026	

> Motion Filed

> Defendants Motion to Enforce Plaintiff???s Petition to Pay Surplus Funds

> Filed By:Rice-Velasquez, Cody

> File Stamp:02/26/2026

> 03/02/2026	

> Order Granting

> Order to Pay Surplus Funds to the Clerk of the Court

> Judicial Officer:Hannah, Therese A - MAG

> Order Signed:03/02/2026

> 03/03/2026	

> Automated Paper Notice Issued to Parties

> Order Granting ---- 3/2/2026 : American Express National Bank, N.A.;JP Morgan Chase Bank, N.A.

> 03/03/2026	

> Automated ENotice Issued to Parties

> Order Granting ---- 3/2/2026 : Cody Rice-Velasquez;Felix O'Neill Rippy;Michael E. Farrer;Scott Andrew Kainrath

> 03/04/2026	

> Order Denying

> Order Moot

> Judicial Officer:Hannah, Therese A - MAG

> Order Signed:03/03/2026

> 03/05/2026	

> Automated Paper Notice Issued to Parties

> Order Denying ---- 3/4/2026 : American Express National Bank, N.A.;JP Morgan Chase Bank, N.A.

> 03/05/2026	

> Automated ENotice Issued to Parties

> Order Denying ---- 3/4/2026 : Cody Rice-Velasquez;Felix O'Neill Rippy;Michael E. Farrer;Scott Andrew Kainrath

> 03/06/2026	

> Motion for Hearing Filed

> Request for Hearing

> Filed By:Financial Center First Credit Union

> File Stamp:03/06/2026

> 03/06/2026	

> Notice Filed

> Notice of Disposition of Property

> Filed By:Financial Center First Credit Union

> File Stamp:03/06/2026

> 03/11/2026	

> Hearing Scheduling Activity

> Hearing scheduled for 03/27/2026 at 11:00 AM.

> 03/11/2026	

> Order for Hearing

> Notice of Hearing on Motion to Clarify Judgment

> Judicial Officer:Hannah, Therese A - MAG

> Order Signed:03/11/2026

> 03/11/2026	

> Motion to Impose Sanctions Filed

> Defendant???s Motion for Sanctions Pursuant to Indiana Trial Rule 11

> Filed By:Rice-Velasquez, Cody

> File Stamp:03/09/2026

> 03/11/2026	

> Objection Filed

> Defendant Motion to Deny Hearing and Enforce Deposit of Surplus

> Filed By:Rice-Velasquez, Cody

> File Stamp:03/11/2026

> 03/12/2026	

> Automated Paper Notice Issued to Parties

> Hearing Scheduling Activity ---- 3/11/2026 : American Express National Bank, N.A.;JP Morgan Chase Bank, N.A. Order for Hearing ---- 3/11/2026 : American Express National Bank, N.A.;JP Morgan Chase Bank, N.A.

> 03/12/2026	

> Automated ENotice Issued to Parties

> Hearing Scheduling Activity ---- 3/11/2026 : Cody Rice-Velasquez;Felix O'Neill Rippy;Michael E. Farrer;Scott Andrew Kainrath Order for Hearing ---- 3/11/2026 : Cody Rice-Velasquez;Felix O'Neill Rippy;Michael E. Farrer;Scott Andrew Kainrath

> 03/27/2026	

> Hearing

> Session:03/27/2026 11:00 AM, Judicial Officer: Hannah, Therese A - MAG

> Comment:in person; on Motion to Clarify Record

> Financial Information

> Financial Balances reflected are current representations of transactions processed by the Clerk’s Office. Please note that any balance due does not reflect interest that has accrued – if applicable – since the last payment. For questions/concerns regarding balances shown, please contact the Clerk’s Office.

> Financial Center First Credit Union

> Plaintiff

> Balance Due (as of 03/12/2026)

> 0.00

> Charge Summary

> Description	Amount	Credit	Payment

> Court Costs and Filing Fees	185.00	0.00	185.00

> Transaction Summary

> Date	Description	Amount

> 01/16/2025	Transaction Assessment	185.00

> 01/16/2025	Electronic Payment	(185.00)

> This is not the official court record. Official records of court proceedings may only be obtained directly from the court maintaining a particular record.

>  

> Subscribe to content by RSS or Email

> Follow us on Twitter

> Indiana Courts YouTube Channel

> Get our shared photos on Flickr

> Terms of Use

### Assistant
> Yes — but **not every docket line should become an Event**. That’s the trap.
> 
> The clean model is:
> 
> - **Docket entry = Filing OR Event**, depending on what it actually is
> - **PDF/document = attached to the Filing object**
> - **Event = something that happened**
> - **Filing = something submitted / issued / entered**
> - **ENotice / paper notice = usually metadata on the filing/event, not its own full object unless strategically important**
> 
> ## The rule
> 
> Ask this for each docket line:
> 
> ### Make it a **Filing** if:
> - something was filed
> - an order was issued/signed
> - a notice document was filed
> - a petition/motion/objection/appearance was filed
> - there is a docket PDF or actual court document behind it
> 
> Examples from your case:
> - Complaint filed
> - Motion for Default Judgment filed
> - Order Granting Motion for Default Judgment
> - Motion to Vacate
> - Notice of Appeal
> - Motion for Sanctions
> - Objection Filed
> - Order to Pay Surplus Funds
> 
> ### Make it an **Event** if:
> - it reflects process activity, not a standalone legal document
> - it marks something that occurred in the case timeline
> - it is scheduling, hearing occurrence, service attempt/return, sale sent to sheriff, judgment released, etc.
> 
> Examples:
> - Case Opened
> - Service Issued
> - Service Returned Served
> - Hearing Scheduling Activity
> - Hearing held
> - Hearing journal entry
> - Decree sent to sheriff for sale
> - Clerk releases judgment
> - Automated ENotice issued
> - Automated Paper Notice issued
> 
> ---
> 
> # Best practice for your docket
> 
> ## 1. Do **not** make the whole docket one Event
> That kills detail.
> 
> ## 2. Do **not** make every single line a giant Filing
> That mixes process activity with documents.
> 
> ## 3. Use this split:
> 
> ### Object types
> - `case`
> - `filing`
> - `event`
> - `evidence`
> - `strategy`
> - `case_issue`
> 
> That’s enough.
> 
> ---
> 
> # How I’d enter the docket
> 
> ## A. Create one Case object
> Example:
> 
> ```text
> FCFCU_v_Cody_Rice-Velasquez_49D03-2501-MF-002559
> ```
> 
> Properties:
> - case_number → text
> - court → text
> - case_type → select/text
> - filed_date → date
> - status → select
> - plaintiff → text or object later
> - defendants → text or multi-text for now
> 
> Body:
> - summary
> - party snapshot
> - current posture
> - embedded views of filings/events/issues/strategy
> 
> ---
> 
> ## B. Create a Filing object for every meaningful docket document
> Not every line. Every **meaningful document entry**.
> 
> Examples from your text:
> 
> - Complaint on Notes and to Foreclose Mortgages
> - Request for Admissions
> - Notice to Homeowners, Contract Buyers, and Renters
> - Motion for Default Judgment Entry and Decree of Foreclosure
> - Affidavit
> - Affidavit in Support of Attorney Fees
> - Order Denying Motion for Default Judgment
> - Request to Enter Amended Default Judgment and Decree of Foreclosure
> - Order Granting Motion for Default Judgment
> - Praecipe for Sheriff’s Sale
> - Petition for Entry of Writ of Assistance
> - Writ of Assistance
> - Order for Writ of Assistance
> - Motion to Vacate Void Judgment
> - Emergency Motion to Stay Writ
> - Exhibit List Exhibits AG
> - Supplemental Emergency Motion for Temporary Access
> - Emergency Supplemental Declaration
> - Emergency Motion to Preserve and Account for Surplus Funds
> - Report of No Excess Proceeds
> - Declaration re displacement/economic harm
> - Notice of Appeal
> - Petition to Pay Surplus Funds to Clerk
> - Petition for Disposition of Surplus and Motion for Nunc Pro Tunc
> - Order Denying Petition for Nunc Pro Tunc
> - Consolidated Objection to Requested Modification of Credit Bid
> - Motion to Enforce Petition to Pay Surplus Funds
> - Order to Pay Surplus Funds to Clerk
> - Order Moot
> - Request for Hearing
> - Notice of Disposition of Property
> - Notice of Hearing on Motion to Clarify Judgment
> - Motion for Sanctions
> - Motion to Deny Hearing and Enforce Deposit of Surplus
> 
> That’s your real legal document layer.
> 
> ---
> 
> ## C. Create Event objects for procedural happenings
> Examples:
> 
> - Case Opened
> - Service Issued to Cody on 03/03/2025
> - Service Returned Served on 03/05/2025
> - Service Issued to Cody on 04/09/2025
> - Service Returned Served on 04/15/2025
> - Automated notice issued for 05/21/2025 order
> - Decree sent to sheriff for sale
> - Notice of sheriff sale posted
> - Decree returned satisfied on 09/09/2025
> - Clerk releases judgment
> - Hearing scheduled for 01/09/2026
> - Hearing held on 01/09/2026
> - Hearing journal entry on 01/09/2026
> - Notice issued that surplus motion will be heard on 01/09/2026
> - Hearing scheduled for 03/27/2026
> - Hearing on 03/27/2026
> 
> These are timeline anchors.
> 
> ---
> 
> # Your specific question:
> ## “Do I enter the docket as event, and documents in the event as related object filings?”
> 
> **Mostly no.**  
> That makes Event the parent of everything, which is backwards.
> 
> Better:
> 
> - **Filing** stands on its own
> - **Event** stands on its own
> - They can link to each other when related
> 
> Example:
> 
> ### Filing
> `Order_for_Hearing_2026-03-11`
> 
> Properties:
> - case → FCFCU case
> - filing_date → 2026-03-11
> - filing_type → order
> - filed_by → court
> - lane → surplus_funds / procedure
> - related_event → Hearing_scheduled_for_2026-03-27
> - docket_text → “Notice of Hearing on Motion to Clarify Judgment”
> - pdf → attached if you have it
> 
> ### Event
> `Hearing_Scheduled_2026-03-27_11AM`
> 
> Properties:
> - case → FCFCU case
> - event_date → 2026-03-27
> - event_type → hearing
> - status → scheduled
> - related_filings → Order_for_Hearing_2026-03-11, Request_for_Hearing_2026-03-06
> - lane → surplus_funds / clarify_record
> 
> That is cleaner.
> 
> ---
> 
> # Recommended property schema
> 
> ## Filing object
> Use these:
> 
> - `case` → object
> - `filing_date` → date
> - `file_stamp_date` → date
> - `filing_type` → select
> - `document_title` → text
> - `docket_label` → text
> - `filed_by` → select
> - `judicial_officer` → text
> - `order_signed_date` → date
> - `lane` → multi-select
> - `status` → select
> - `related_event` → object
> - `related_issues` → object
> - `related_strategy` → object
> - `related_evidence` → object
> - `pdf_status` → select
> - `docket_pdf` → media/file if Capacities supports, otherwise link block/body
> - `source` → select (`mycase`, `efile`, `court_order`, `manual`)
> - `sequence_no` → number if you want manual chronology
> 
> ### Filing type select values
> ```text
> complaint
> motion
> order
> notice
> petition
> objection
> declaration
> affidavit
> appearance
> writ
> praecipe
> exhibit_list
> journal_entry
> other
> ```
> 
> ### Filed by select values
> ```text
> plaintiff
> defendant
> court
> clerk
> sheriff
> other
> ```
> 
> ### Status select values
> ```text
> filed
> issued
> granted
> denied
> moot
> pending
> scheduled
> entered
> ```
> 
> ### PDF status
> ```text
> have_pdf
> need_pdf
> no_pdf_exists
> screenshot_only
> ```
> 
> ---
> 
> ## Event object
> Properties:
> 
> - `case` → object
> - `event_date` → date
> - `event_type` → select
> - `title` → title
> - `actor` → select
> - `related_filings` → object
> - `related_issues` → object
> - `lane` → multi-select
> - `outcome` → text
> - `status` → select
> - `source` → select
> 
> ### Event type values
> ```text
> case_opened
> service_issued
> service_returned
> hearing_scheduled
> hearing_held
> journal_entry
> notice_sent
> sale_activity
> judgment_activity
> clerk_activity
> property_posting
> other
> ```
> 
> ### Actor values
> ```text
> court
> clerk
> plaintiff
> defendant
> sheriff
> system
> ```
> 
> ---
> 
> ## Case_Issue object
> You already have this — good.
> 
> Properties:
> - `case` → object
> - `issue_type` → select
> - `status` → select
> - `severity` → select
> - `lane` → multi-select
> - `related_filings` → object
> - `related_events` → object
> - `related_evidence` → object
> - `related_strategy` → object
> - `rule_or_basis` → text
> - `discovered_date` → date
> 
> ---
> 
> # How to link to the Case object
> 
> ## Use a **property**
> Every filing, event, issue, evidence, and strategy should have:
> 
> ```text
> case → [FCFCU case object]
> ```
> 
> That is the main link.
> 
> ## Then use the Case body as the dashboard
> Inside the case page, embed or manually reference:
> 
> - recent filings
> - timeline events
> - active case issues
> - strategies
> - evidence index
> 
> So:
> 
> - **property link = structural database link**
> - **body links/embeds = human-readable command center**
> 
> That’s the right split.
> 
> ---
> 
> # What the Case page should look like
> 
> ## Properties
> - case_number
> - court
> - type
> - filed_date
> - status
> - phase
> 
> ## Body
> ```markdown
> ## Overview
> Short plain-English summary of posture.
> 
> ## Current Pressure Points
> - service defect
> - surplus funds
> - sanctions
> - hearing on March 27
> 
> ## Filings
> [embedded list of filings where case = this case]
> 
> ## Timeline
> [embedded list of events where case = this case, sorted by event_date]
> 
> ## Case Issues
> [embedded list of case_issues where case = this case]
> 
> ## Strategy
> [embedded list of strategy where case = this case]
> 
> ## Evidence
> [embedded list of evidence where case = this case]
> ```
> 
> ---
> 
> # For docket PDFs specifically
> 
> Treat the **docket line** and **document PDF** as part of the Filing object.
> 
> Example:
> 
> ## Filing object
> `Order_Granting_Default_Judgment_2025-05-28`
> 
> Properties:
> - filing_type → order
> - docket_label → Order Granting Motion for Default Judgment
> - document_title → Amended Default Judgment Entry and Decree of Foreclosure
> - filed_by → court
> - order_signed_date → 2025-05-28
> - case → FCFCU case
> - pdf_status → have_pdf
> 
> Body:
> ```markdown
> ## Docket Text
> Order Granting Motion for Default Judgment
> 
> ## Summary
> Court entered amended default judgment and decree of foreclosure.
> 
> ## Why It Matters
> This is the pivotal judgment entry that later drives sale, writ, and surplus issues.
> 
> ## Attached PDF
> [attach PDF or image/screenshot]
> 
> ## Related
> [[Default_Judgment_Entered_2025-05-28]]
> [[Case_Issue_Service_Defect]]
> [[Strategy_TR60B_Void_Judgment]]
> ```
> 
> That’s better than burying the document under an Event.
> 
> ---
> 
> # What to do with ENotices and paper notices
> 
> Do **not** create a full object for every automated ENotice. That’s overkill.
> 
> Use one of these approaches:
> 
> ## Option 1 — as Event only when important
> Only create an Event if the notice timing matters strategically.
> 
> Example:
> - `ENotice_Issued_for_01-21-2026_Order_on_01-22-2026`
> 
> Useful if you are tracking who got notice and when.
> 
> ## Option 2 — as properties / body notes on the related filing
> For most cases, better.
> 
> On the Filing object add:
> - `notice_date` → date
> - `notice_method` → multi-select (`enotice`, `paper_notice`)
> - `notice_recipients` → text
> - `notice_issue_flag` → checkbox/select if something looks wrong
> 
> This is usually enough.
> 
> For your case, some notices matter because of service and due process. So only elevate the important ones.
> 
> ---
> 
> # My recommendation for your exact case
> 
> Use this rule:
> 
> ## Create Filing objects for:
> - all motions
> - all orders
> - all petitions
> - all objections
> - all declarations/affidavits
> - complaint
> - writ
> - major notices with legal substance
> - appeal notice
> - exhibit lists
> 
> ## Create Event objects for:
> - service attempts/returns
> - hearing scheduling
> - hearing occurrence
> - journal entries
> - sheriff sale process milestones
> - notice issuance when timing matters
> - clerk actions
> - case opened / judgment released / decree returned
> 
> ## Don’t create standalone objects for:
> - every routine automated paper/enotice line
> - every duplicate summons unless they matter to a service defect argument
> 
> For duplicate summons/service entries, you can sometimes roll them into one service-focused Event plus linked Case_Issue.
> 
> ---
> 
> # Concrete example from your docket
> 
> ## Filing
> `Motion_to_Vacate_Void_Judgment_2025-12-10`
> 
> Properties:
> - case → FCFCU case
> - filing_date → 2025-12-11
> - file_stamp_date → 2025-12-10
> - filing_type → motion
> - filed_by → defendant
> - lane → service_defect, due_process
> - related_event → Hearing_2026-01-09
> - related_issues → Lack_of_Service, Void_Judgment
> - pdf_status → have_pdf
> 
> ## Event
> `Hearing_on_Motion_to_Set_Aside_2026-01-09`
> 
> Properties:
> - case → FCFCU case
> - event_date → 2026-01-09
> - event_type → hearing_held
> - actor → court
> - related_filings → Motion_to_Vacate_Void_Judgment_2025-12-10, Motion_to_Preserve_Surplus_2025-12-16
> - lane → service_defect, surplus_funds
> - outcome → Argument heard; court to issue order
> 
> ## Filing
> `Order_from_January_9_Hearing_2026-01-21`
> 
> Properties:
> - case → FCFCU case
> - filing_type → order
> - filed_by → court
> - order_signed_date → 2026-01-20
> - filing_date → 2026-01-21
> - related_event → Hearing_on_Motion_to_Set_Aside_2026-01-09
> 
> That’s the pattern.
> 
> ---
> 
> # Final answer
> 
> So no, I would **not** enter “the docket” as one Event with filings under it.
> 
> I would do this instead:
> 
> - the **docket is a view**
> - **Filing objects** hold the actual docket documents
> - **Event objects** hold procedural milestones
> - both link back to the **Case** with a property
> - the **Case page** displays them together in chronological order or by category
> 
> That gives you:
> - a real docket view
> - a timeline view
> - a motion binder
> - an issues map
> 
> without duplicating yourself into madness.
> 
> If you want, next move is I can give you a **copy-ready Capacities schema pack** for:
> `case`, `filing`, `event`, and `case_issue`
> with exact property names, types, and suggested select values in a format you can build from directly.

### User
> filing object, like a propery in filing object for create all those as objects?

### Assistant
> Yes — **inside the `filing` object, many of those should be properties, not separate objects**.
> 
> That’s the clean answer.
> 
> ## What should be a property on `filing`
> These are just attributes of the filing:
> 
> - filing_type
> - filed_by
> - filing_date
> - file_stamp_date
> - order_signed_date
> - docket_label
> - document_title
> - status
> - lane
> - judicial_officer
> - pdf_status
> - source
> - notice_method
> - notice_date
> - recipients_summary
> - sequence_no
> 
> Those are **not** their own objects.
> 
> ---
> 
> # What should be linked as objects from `filing`
> These are things with their own life and relationships:
> 
> - `case`
> - `related_event`
> - `related_case_issue`
> - `related_strategy`
> - `related_evidence`
> 
> So the filing object is basically:
> 
> ## Filing object
> ### Properties
> - `case` → **object**
> - `filing_type` → **select**
> - `filed_by` → **select**
> - `filing_date` → **date**
> - `file_stamp_date` → **date**
> - `order_signed_date` → **date**
> - `docket_label` → **text**
> - `document_title` → **text**
> - `status` → **select**
> - `lane` → **multi-select**
> - `judicial_officer` → **text**
> - `pdf_status` → **select**
> - `source` → **select**
> - `related_event` → **object**
> - `related_case_issue` → **object**
> - `related_strategy` → **object**
> - `related_evidence` → **object**
> 
> ### Body
> - short summary
> - why it matters
> - pasted docket text
> - attached PDF / screenshot
> - manual notes
> 
> ---
> 
> # Example
> 
> ## Filing object:
> `Order_to_Pay_Surplus_Funds_2026-03-02`
> 
> ### Properties
> - `case` → FCFCU case
> - `filing_type` → order
> - `filed_by` → court
> - `filing_date` → 2026-03-02
> - `order_signed_date` → 2026-03-02
> - `docket_label` → Order Granting
> - `document_title` → Order to Pay Surplus Funds to the Clerk of the Court
> - `status` → granted
> - `lane` → surplus_funds
> - `judicial_officer` → Hannah, Therese A - MAG
> - `pdf_status` → have_pdf
> - `related_case_issue` → surplus_funds_withholding
> - `related_strategy` → enforce_surplus_deposit
> - `related_event` → surplus_order_notice_issued_2026-03-03
> 
> ---
> 
> # Simple rule
> 
> ## Make it a property if:
> it only describes the filing.
> 
> ## Make it an object if:
> it needs its own page, its own notes, and links to multiple other things.
> 
> ---
> 
> # For your setup, this means:
> 
> ## Do **not** create separate objects for:
> - filing_type
> - order type
> - status
> - judge
> - source
> - notice method
> - lane
> 
> Those are properties.
> 
> ## Do create separate objects for:
> - case
> - event
> - case_issue
> - strategy
> - evidence
> 
> Those are real linked records.
> 
> ---
> 
> # Best way to think about it
> 
> A `filing` is like a row with a brain.
> 
> It has:
> - **properties** = structured metadata
> - **body** = human explanation
> - **linked objects** = relationships
> 
> That’s the sweet spot.
> 
> ## Not this:
> - every field becomes an object  
> that gets stupid fast.
> 
> ## Not this either:
> - everything is just text  
> then you can’t filter anything.
> 
> ---
> 
> # Clean minimum schema for `filing`
> 
> Use this and don’t overcomplicate it:
> 
> - `case` → object
> - `filing_type` → select
> - `filed_by` → select
> - `filing_date` → date
> - `document_title` → text
> - `docket_label` → text
> - `status` → select
> - `lane` → multi-select
> - `related_event` → object
> - `related_case_issue` → object
> - `related_strategy` → object
> - `related_evidence` → object
> - `pdf_status` → select
> 
> That’s enough to start.
> 
> If you want, next I’ll lay out the exact same thing for `event` and `case_issue` so the three objects fit together cleanly.
