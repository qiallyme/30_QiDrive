---
layout: page
title: "Ledger Analysis and Findings"
slug: "ledger_analysis_and_findings"
created_at: "2026-04-23 03:41:31"
updated_at: "2026-04-23 03:41:31"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-006.json"
template_key: master-template
date: 2026-04-23
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69e9db07-be54-83ea-ac42-0a1f4187005e"
canonical_ref: ""
---

# Ledger Analysis and Findings

## Overview
- **Date**: 2026-04-23 03:41:31
- **Conversation ID**: `69e9db07-be54-83ea-ac42-0a1f4187005e`
- **Source**: `Chat-Export-28513-2026/conversations-006.json`

## Chat History

### User
> ok the best way to show all these descrepencies and they way they have changed is to use accounting accounts then create adjustment entries in the ledger of each charge then compile them into one general ledger this soule show how wild all this is and give us the real number, i want to first calulate a ledger showing the work for the real numbers, then do a ledger for all their changes.

### Assistant
> Yes. That is the right frame.
> 
> Two separate ledgers is cleaner than one giant mess:
> 1. **Reconstructed “should-be” ledger** using the judgment terms, note terms, per diem, publications, sheriff fees, and any actually supportable dates.
> 2. **Plaintiff discrepancy ledger** showing each filing/version as its own source entry, then adjustment lines showing how they changed principal, interest, fees, costs, surplus, or timing from one version to the next.
> 
> I’m going to pull the file structure first, then I’ll build the account map and a workbook so this becomes court-usable instead of just “they’re inconsistent.”

### Assistant
> I found enough to anchor the accounting model.
> 
> Two hard baseline numbers are already sitting in their own papers: the RFA/affidavit numbers as of November 19, 2024, and the amended default judgment totals on May 28, 2025. That gives us a usable starting spine even before we load every later worksheet and sale paper.

### Assistant
> I’ve got the first-pass ledger built. The useful part is this: the May 28 judgment loan amounts actually tie cleanly to the November 19, 2024 base amounts using their own per diem, so the real fight is the post-judgment layer and every later “correction” they piled on.

### Assistant
> Yes. That is the right architecture.
> 
> I built the first-pass workbook here: [FCFCU_forensic_ledger_v1.xlsx](sandbox:/mnt/data/FCFCU_forensic_ledger_v1.xlsx). It is anchored to your case archive structure and source map so it can be expanded cleanly as we load more filings. fileciteturn0file0 fileciteturn3file0
> 
> What it does:
> - **Reconstructed ledger**: uses supportable numbers first, then books adjustments by account.
> - **Claim-change ledger**: treats each plaintiff version as its own numeric snapshot, then posts the delta as an adjustment entry into a general ledger.
> - **Comparison sheet**: shows the gap between supportable numbers and their later “fully satisfied / no surplus” story.
> 
> Big finding: their **11/19/2024** RFA/affidavit numbers say Loan 1 was **$190,685.22** at **$23.14/day** and Loan 2 was **$22,567.41** at **$4.31/day**. Their **05/28/2025** amended default judgment says Loan 1 was **$194,410.76**, Loan 2 was **$23,261.32**, plus **$191.01** court costs and **$3,000.00** attorney fees, total **$220,863.09**. Those loan deltas exactly reconcile to **161 days** of their own per-diem math from **11/19/2024 to 04/29/2025**. So the judgment loan buckets are not the crazy part; the real mess starts in the post-judgment layer and later sale/surplus representations. fileciteturn1file13 fileciteturn1file16 fileciteturn1file18
> 
> The sheriff-sale return later says the matter was **“Fully Satisfied on 08/15/25”** with **“Total Paid $240,464.20.”** In the workbook, I modeled the judgment’s separate “additional interest from April 29, 2025, to date of judgment” as a selectable post-04/29 layer. Using the current 30-day setting, the reconstructed total comes to **$221,686.59**, leaving **$18,777.61** that still needs documentary support to erase surplus. If you compare only against the stated judgment total, the jump is **$19,601.11**. fileciteturn2file0 fileciteturn4file3 fileciteturn6file17
> 
> I also preloaded pending rows for the later surplus-phase documents that appear in your archive tree, including **Petition Determining No Surplus**, **Order on Surplus and Nunc Pro Tunc**, and **Order to Pay Surplus Funds**. Those are the next numbers that need to be pulled and posted as formal adjustment entries so the “their changes” ledger becomes complete. fileciteturn5file2 fileciteturn5file3 fileciteturn5file5 fileciteturn5file6
> 
> The workbook tabs are:
> - `Inputs_Calc`
> - `Reconstructed_Journal`
> - `GL_Real`
> - `Claims_Timeline`
> - `Change_Classifier`
> - `GL_Claim_Changes`
> - `Comparison`
> 
> Net: this gives you a court-usable frame to say, **“Here is the supportable ledger, here is every later adjustment they made, here is the unsupported remainder.”**
> 
> The next highest-value move is to load the exact figures from the no-surplus / nunc-pro-tunc / order-to-pay-surplus papers into `Claims_Timeline` so the adjustment ledger shows each shift by date and account.

### User
> Source Document	Date	Amount Stated	Statement Date	Category	Conflict Group	Conflicts With	Variance
> Request for Admissions	2025-01-16	$190,685.22	2024-11-19	Principal	judgement001		
> Request for Admissions	2025-01-16	$22,567.41	2024-11-19	Principal	judgement001		
> Request for Admissions	2025-01-16	$23.14	2024-11-19	Per Diem	interest001		
> Request for Admissions	2025-01-16	$4.31	2024-11-19	Per Diem	interest001		
> Complaint		$0.00		Principal		Affidavit	$
> Affidavit of Indebtedness		$0.00		Total Owed		Judgment	$
> Default Judgment	2025-05-07	$194,410.76	2025-04-29	Principal		Sale Bid	$
> Default Judgment	2025-05-07	$23,261.32	2025-04-29	Principal			
> Default Judgment	2025-05-07	$3,000.00	2025-04-29	Attorney			
> Default Judgment	2025-05-07	$191.01	2025-04-29	Court			
> Default Judgment	2025-05-07	$220,863.09	2025-04-29	Total Judgement			
> Sheriff Sale Bid	2025-07-17	$240,464.20		Bid Amount		Worksheet	$
> Sheriff Sale Bid	2025-07-17	$220,863.09		Total Judgement			
> Sheriff Sale Bid	2025-07-17	$7,600.81		Taxes			
> Sheriff Sale Bid	2025-07-17	$10,725.27		Interest			
> Sheriff Sale Bid	2025-07-17	$1,275.00		Attorney			
> Sheriff Sale Bid	2025-07-17	$300.00		Sheriff			
> Sheriff Sale Bid	2025-07-17	$1,094.35		Publication			
> Sheriff Sale Bid	2025-07-17	$35.00		Clerk			
> Sheriff Worksheet				Distribution		Judgment	$
> Publication Invoice		$		Publication Cost		Claimed Cost	$
> Attorney Fees Claimed	2025-05-07	$3,000.00		Fees		Itemized Invoice	$
> Amended Default	2025-05-28	$194,410.76					
> Amended Default	2025-05-28	$23,261.32					
> Amended Default	2025-05-28	$3,000.00					
> Amended Default	2025-05-28	$191.01					
> Amended Default	2025-05-28	$220,863.09					
> Clerk Return	2025-06-19	$240,464.20		PAID Judgement			
> Clerk Return	2025-06-19	$284.28		Court and Record			
> Clerk Return	2025-06-19	$38.00		Sheriff			
> Clerk Return	2025-06-19	$300.00		Sheriff			
> Clerk Return	2025-06-19	$0.00		Clerk			
> Sheriff Worksheet	2025-08-06	$220,863.09		Judgement Amount			
> Sheriff Worksheet	2025-08-06	$10,725.27		Add Sum Interest			
> Sheriff Worksheet	2025-08-06	$8,875.81		Additional Costs			
> Sheriff Worksheet	2025-08-06	$240,464.17		Total Judgement			
> Sheriff Worksheet	2025-08-06	$300.00		Admin Fee			
> Sheriff Worksheet	2025-08-06	$38.00		Sheriff Fee			
> Sheriff Worksheet	2025-08-06	$284.28		Advertising Cost			
> Sheriff Worksheet	2025-08-06	$241,086.45		Grand Total			
> Sheriff Worksheet	2025-08-06	$240,464.20		BID

### User
> ok so the difference between what they calcualted, and what i calculated now that the publications surfaced, is less than $53.00 so i think we should file something with teh court stating we have no objections, but i still think the fact they couldnt have sent this from the get go and i had to do all these unnecssary filign because they were playing fast and loose they shoudl be santioned.

### Assistant
> Yes, but **do not file a blanket “no objections.”** That is too broad and sloppy.
> 
> File a **limited non-objection**.
> 
> Your position now is:
> 
> - based on the documents finally produced, the remaining variance is de minimis
> - you do **not** object to the court moving forward on the surplus/disbursement issue
> - you **do not concede** their earlier accounting was properly supported
> - you **do not waive** your other objections or claims
> - you reserve the right to raise the unnecessary burden caused by their late/incomplete support if needed later
> 
> On sanctions: wanting them is understandable, but **I would not lead with sanctions right now**. With the difference now under about $53, a sanctions ask in the same filing risks making you look like you are still trying to fight after the math is basically reconciled. The cleaner win is: **you forced them to substantiate it**. Get the surplus issue stabilized first.
> 
> Best move:
> 1. file the limited non-objection
> 2. get the money issue resolved
> 3. preserve the record that their support came late and caused unnecessary motion practice
> 4. keep sanctions in reserve unless they keep playing games
> 
> Here is the filing language I would use:
> 
> ---
> 
> **STATE OF INDIANA**  
> **COUNTY OF MARION**  
> ) SS:  
> **MARION SUPERIOR COURT 3**
> 
> **CAUSE NO. 49D03-2501-MF-002559**
> 
> **FINANCIAL CENTER FIRST CREDIT UNION,**  
> Plaintiff,  
> 
> v.  
> 
> **CODY RICE-VELASQUEZ,**  
> Defendant.
> 
> ## DEFENDANT’S LIMITED NOTICE OF NO PRESENT OBJECTION TO SURPLUS ACCOUNTING, WITH EXPRESS RESERVATION OF RIGHTS
> 
> Defendant, Cody Rice-Velasquez, respectfully files this Limited Notice of No Present Objection to the surplus accounting presently before the Court, and states as follows:
> 
> 1. Defendant previously challenged Plaintiff’s surplus-related calculations because the record reflected material inconsistencies across filings and supporting documentation was not fully provided at the outset.
> 
> 2. Defendant has now reviewed the additional materials that were later surfaced, including cost support relating to publication and related sale expenses.
> 
> 3. Based on Defendant’s current reconciliation of the figures, the remaining variance between Plaintiff’s calculation and Defendant’s calculation appears to be de minimis, at less than approximately $53.00.
> 
> 4. Accordingly, **Defendant does not presently object to the Court proceeding on the surplus/disbursement issue based on the now-supported accounting**, to the extent the Court finds the remaining minor variance immaterial.
> 
> 5. This limited non-objection is made solely to avoid further unnecessary dispute over a now largely reconciled arithmetic issue and **shall not be construed as**:
>    a. a concession that Plaintiff’s earlier filings were complete, clear, or properly supported when filed;  
>    b. a waiver of Defendant’s prior objections to inconsistencies, lack of documentation, or shifting calculations;  
>    c. a waiver of any other claims, defenses, or issues previously raised or later raised in this matter or any related matter.
> 
> 6. Defendant further notes for the record that the present reconciliation was only possible after supporting information was surfaced later in the process, after substantial time and effort had already been expended addressing discrepancies that could have been clarified much earlier.
> 
> WHEREFORE, Defendant respectfully notifies the Court that Defendant has no present objection to the Court proceeding on the surplus issue consistent with the now-supported accounting, while expressly reserving all other rights.
> 
> Respectfully submitted,
> 
> **Cody Rice-Velasquez**  
> 1000 Fulton Pkwy Apt 107  
> Evansville, IN 47710  
> 317-205-4383  
> crice4485@gmail.com  
> Defendant, pro se
> 
> ---
> 
> That is the right tone: controlled, not emotional, preserves the point, and does not give away bigger issues.
> 
> One correction, though: if you know the **exact** variance now, use the exact number, not “approximately $53.00.” That needs to be tight.

### User
> but i want to file with teh court to direct teh clerk to pay the funds to me right away, there have been no claims raised nothing from the co-defendant at all and they never had any claim to the property and fcfcu filing them on there was just a cya thing they did without any verified reason, also why amex and chase i had account with every major bank and credit card company so it was just ad hoc or random selection ont he part of fcfcu.

### Assistant
> Yes. That is the cleaner move.
> 
> Do **not** file just a “no objection” if what you actually want is an order. File a **Motion to Direct Clerk to Immediately Disburse Surplus Funds to Defendant**.
> 
> The legal lane is straightforward: in Indiana, after the sale proceeds cover the amounts due, any surplus is paid to the clerk and then transferred, as the court directs, to the mortgage debtor, the debtor’s heirs, or assigns. But adjudicated junior liens can attach to those proceeds, so your motion should not make a reckless absolute claim that no co-defendant could ever have had any possible interest. The better argument is narrower and stronger: **no competing claimant has appeared, no competing claim has been proven, and the foreclosing plaintiff’s own accounting now shows a surplus that should be released without further delay.** citeturn143822view0turn143822view3turn592100view3turn592100view4
> 
> Also, stop short of arguing in the motion that FCFCU picked Amex and Chase “randomly” or as some ad hoc selection unless you can prove that from the title record or docket. That is motive talk, and motive talk is weak here. The filing should stay on the record facts: surplus exists, the clerk is holding or should be holding it for court-directed disbursement, and no other party has come forward to establish entitlement. Indiana courts and county guidance treat foreclosure surplus as something the court/clerk disburses upon claim rather than something the foreclosing plaintiff keeps. citeturn143822view4turn143822view5turn143822view3
> 
> Use this title:
> 
> **DEFENDANT’S MOTION TO DIRECT CLERK TO IMMEDIATELY DISBURSE SURPLUS FUNDS TO DEFENDANT, MORTGAGE DEBTOR**
> 
> Copy-ready draft:
> 
> ```markdown
> STATE OF INDIANA                )
>                                 ) SS:
> COUNTY OF MARION                )
> 
> IN THE MARION SUPERIOR COURT 3
> 
> CAUSE NO. 49D03-2501-MF-002559
> 
> FINANCIAL CENTER FIRST CREDIT UNION,
>     Plaintiff,
> 
> v.
> 
> CODY RICE-VELASQUEZ, et al.,
>     Defendants.
> 
> DEFENDANT’S MOTION TO DIRECT CLERK TO IMMEDIATELY DISBURSE SURPLUS FUNDS TO DEFENDANT, MORTGAGE DEBTOR
> 
> Defendant, Cody Rice-Velasquez, pro se, respectfully moves the Court for an order directing the Clerk to immediately disburse the surplus funds in this matter to Defendant, and states:
> 
> 1. This foreclosure action resulted in a sheriff’s sale of the subject property.
> 
> 2. Plaintiff’s own sale-related filings and accounting now reflect that sale proceeds exceeded the amount necessary to satisfy the amounts properly payable from the sale.
> 
> 3. Defendant previously objected to Plaintiff’s shifting and inadequately supported calculations. After additional supporting materials were surfaced, Defendant’s reconciliation now shows that any remaining arithmetic variance is de minimis and does not defeat the existence of surplus funds.
> 
> 4. To date, no co-defendant has filed a motion, objection, verified claim, or other application establishing a present entitlement to the surplus funds.
> 
> 5. To Defendant’s knowledge, no order of this Court has awarded any portion of the surplus funds to any co-defendant.
> 
> 6. Under Indiana foreclosure procedure, when sale proceeds exceed the amounts payable from the sale, the surplus is paid to the Clerk for transfer, as directed by the Court, to the mortgage debtor, the debtor’s heirs, or assigns, absent a superior proven claim to the funds.
> 
> 7. Defendant is the mortgage debtor and the former owner of the property that was the subject of the foreclosure sale.
> 
> 8. Further delay in disbursement serves no legitimate purpose where the foreclosing Plaintiff’s accounting now confirms a surplus and no competing claimant has come forward to establish entitlement.
> 
> 9. Defendant therefore requests prompt release of the surplus funds to avoid additional unnecessary delay and prejudice.
> 
> WHEREFORE, Defendant respectfully requests that the Court:
> 
> A. determine that the surplus funds in this matter are payable to Defendant;
> 
> B. direct the Clerk of the Marion County Court to immediately disburse the surplus funds being held in connection with this cause to Defendant Cody Rice-Velasquez;
> 
> C. if the funds have not yet been deposited with the Clerk, order Plaintiff to immediately deposit the surplus funds with the Clerk for prompt disbursement;
> 
> D. waive hearing if the Court deems a hearing unnecessary, or in the alternative set this motion for prompt hearing; and
> 
> E. grant all other just and proper relief.
> 
> Respectfully submitted,
> 
> Cody Rice-Velasquez
> 1000 Fulton Pkwy Apt 107
> Evansville, IN 47710
> 317-205-4383
> crice4485@gmail.com
> Defendant, pro se
> 
> CERTIFICATE OF SERVICE
> 
> I certify that on ____________, 2026, I served a copy of this Motion upon all counsel of record and any self-represented parties by [Indiana E-Filing / U.S. Mail / email if agreed service applies].
> 
> Cody Rice-Velasquez
> ```
> 
> And the proposed order:
> 
> ```markdown
> STATE OF INDIANA                )
>                                 ) SS:
> COUNTY OF MARION                )
> 
> IN THE MARION SUPERIOR COURT 3
> 
> CAUSE NO. 49D03-2501-MF-002559
> 
> FINANCIAL CENTER FIRST CREDIT UNION,
>     Plaintiff,
> 
> v.
> 
> CODY RICE-VELASQUEZ, et al.,
>     Defendants.
> 
> ORDER ON DEFENDANT’S MOTION TO DIRECT DISBURSEMENT OF SURPLUS FUNDS
> 
> The Court, having reviewed Defendant’s Motion to Direct Disbursement of Surplus Funds, now finds:
> 
> 1. A surplus exists from the sheriff’s sale in this matter.
> 2. No competing claimant has established a superior entitlement to the surplus funds presently at issue.
> 3. The surplus funds should be disbursed to Defendant Cody Rice-Velasquez.
> 
> IT IS THEREFORE ORDERED that the Clerk is directed to disburse the surplus funds held in this cause, in the amount of $______________, to Defendant Cody Rice-Velasquez forthwith.
> 
> If such funds have not yet been deposited with the Clerk, Plaintiff shall deposit the surplus funds with the Clerk within ____ days of this Order, and the Clerk shall disburse those funds to Defendant upon receipt.
> 
> SO ORDERED this ___ day of ____________, 2026.
> 
> ________________________________
> Judge, Marion Superior Court 3
> ```
> 
> Best tactical edits before filing:
> 
> - Put the **exact dollar amount** in the motion and proposed order.
> - If FCFCU already filed a paper confirming surplus, cite it by title and filing date.
> - If no other defendant has appeared on the docket, say that plainly.
> - Do **not** spend half the motion complaining about their earlier sloppy accounting. One sentence is enough. The point of this filing is to get paid.
> 
> The sharp version is: **surplus now appears confirmed, no competing claimant has proven entitlement, release the money now.**
> 
> If you want, I’ll turn this into a tighter, court-style final version with your exact surplus amount and the specific filing titles baked in.

### User
> {'asset_pointer': 'sediment://file_0000000054a871f5bfdce70ec37ae247', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 347, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 21059, 'width': 177}the exact number is 52.99
> Scenario	1-Verifiable
> Balance Due	$213,252.63
> Interest	$7,384.05
> Taxes	$7,600.81
> Attorney	$3,000.00
> Sherriff	$338.00
> Publication	$1,094.35
> Clerk	$35.00
> Court	$185.00
> Other	$0.00
> 	$232,889.84
> Surplus Calc	$7,574.36

### Assistant
> Good. Then stop fighting the **$52.99**.
> 
> If the goal is **get paid now**, the filing should be:
> 
> **Motion to Direct Immediate Disbursement of Surplus Funds**  
> with a built-in fallback that says the court should release the funds **even if it uses Plaintiff’s slightly different figure**.
> 
> That is the smart play. Do **not** let $52.99 become the excuse for more delay.
> 
> Use these numbers:
> - **Defendant’s verifiable total:** **$232,889.84**
> - **Sale / paid amount:** **$240,464.20**
> - **Defendant’s surplus calculation:** **$7,574.36**
> - **Remaining variance:** **$52.99**
> 
> ## Filing draft
> 
> ```markdown
> STATE OF INDIANA                )
>                                 ) SS:
> COUNTY OF MARION                )
> 
> IN THE MARION SUPERIOR COURT 3
> 
> CAUSE NO. 49D03-2501-MF-002559
> 
> FINANCIAL CENTER FIRST CREDIT UNION,
>     Plaintiff,
> 
> v.
> 
> CODY RICE-VELASQUEZ, et al.,
>     Defendants.
> 
> DEFENDANT’S MOTION TO DIRECT IMMEDIATE DISBURSEMENT OF SURPLUS FUNDS TO DEFENDANT
> 
> Defendant, Cody Rice-Velasquez, pro se, respectfully moves the Court for an order directing the immediate disbursement of surplus funds to Defendant, and states as follows:
> 
> 1. This matter resulted in a sheriff’s sale of the subject property.
> 
> 2. The sale-related amount paid was $240,464.20.
> 
> 3. Based on Defendant’s reconciliation of the judgment amount, interest, taxes, attorney fees, sheriff fees, publication, clerk, and court costs using the now-available supporting documents, Defendant calculates the verifiable total amount properly chargeable against the sale proceeds as $232,889.84.
> 
> 4. Based on that reconciliation, Defendant calculates the resulting surplus as $7,574.36.
> 
> 5. Any remaining difference between Plaintiff’s calculation and Defendant’s calculation is only $52.99.
> 
> 6. Defendant does not object to the Court treating that narrow variance as immaterial for purposes of promptly resolving disbursement.
> 
> 7. No co-defendant has filed a motion, objection, verified claim, or other application establishing a present entitlement to the surplus funds.
> 
> 8. No competing claimant has appeared and proven a superior right to the surplus funds.
> 
> 9. Defendant is the mortgage debtor and former owner of the property that was the subject of this foreclosure action.
> 
> 10. Further delay in disbursement serves no legitimate purpose where the existence of surplus funds is now established and any remaining variance is minimal.
> 
> 11. Defendant therefore requests immediate disbursement of the surplus funds, in the amount supported by the Court’s review, and specifically requests disbursement of $7,574.36 if the Court adopts Defendant’s reconciliation.
> 
> 12. In the alternative, if the Court adopts Plaintiff’s slightly different figure, Defendant requests that the Court immediately disburse the amount the Court finds supported without further delay, rather than withholding the funds over a $52.99 variance.
> 
> WHEREFORE, Defendant respectfully requests that the Court:
> 
> A. find that surplus funds exist from the sheriff’s sale in this matter;
> 
> B. direct the Clerk to immediately disburse the surplus funds to Defendant Cody Rice-Velasquez;
> 
> C. disburse $7,574.36 if the Court adopts Defendant’s reconciliation, or in the alternative disburse the amount the Court finds supported without further delay;
> 
> D. if the surplus funds have not yet been deposited with the Clerk, order Plaintiff to immediately deposit them for prompt disbursement; and
> 
> E. grant all other just and proper relief.
> 
> Respectfully submitted,
> 
> Cody Rice-Velasquez
> 1000 Fulton Pkwy Apt 107
> Evansville, IN 47710
> 317-205-4383
> crice4485@gmail.com
> Defendant, pro se
> 
> CERTIFICATE OF SERVICE
> 
> I certify that on __________________, 2026, I served a copy of this Motion upon all counsel of record and all self-represented parties by Indiana E-Filing and/or by any other method required by rule.
> 
> Cody Rice-Velasquez
> ```
> 
> ## Proposed order
> 
> ```markdown
> STATE OF INDIANA                )
>                                 ) SS:
> COUNTY OF MARION                )
> 
> IN THE MARION SUPERIOR COURT 3
> 
> CAUSE NO. 49D03-2501-MF-002559
> 
> FINANCIAL CENTER FIRST CREDIT UNION,
>     Plaintiff,
> 
> v.
> 
> CODY RICE-VELASQUEZ, et al.,
>     Defendants.
> 
> ORDER ON DEFENDANT’S MOTION TO DIRECT IMMEDIATE DISBURSEMENT OF SURPLUS FUNDS
> 
> The Court, having reviewed Defendant’s Motion to Direct Immediate Disbursement of Surplus Funds, now finds:
> 
> 1. Surplus funds exist from the sheriff’s sale in this matter.
> 2. No competing claimant has established a superior entitlement to those surplus funds.
> 3. Prompt disbursement is appropriate.
> 
> IT IS THEREFORE ORDERED that the Clerk shall immediately disburse surplus funds in this cause to Defendant Cody Rice-Velasquez in the amount of $________________.
> 
> If the surplus funds have not yet been deposited with the Clerk, Plaintiff shall deposit the surplus funds with the Clerk within ____ days of this Order, and the Clerk shall disburse them immediately upon receipt.
> 
> SO ORDERED this ___ day of ____________, 2026.
> 
> ________________________________
> Judge, Marion Superior Court 3
> ```
> 
> ## Strategic note
> 
> Do **not** put the Amex/Chase theory in this motion. It does not help this ask.  
> This motion should stay brutally simple:
> 
> - surplus exists
> - no one else claimed it
> - variance is only $52.99
> - release the money now
> 
> That is the lane.
> 
> I can also tighten this into a more formal Indiana-style version with a short intro paragraph and cleaner numbered relief section if you want the filing to read more like something a clerk sees every day.

### User
> i have other judgments against me but none of them have filed requesting to get monie from the the court wouldnt hold that to pay thos eother judements would they adn also amex and chase have no appeared or filed anything at all, had they had a claim they woudl have asserted it by now espcially sense its been 16 months since this started. right.

### Assistant
> Mostly right, but not as absolute as you want.
> 
> **No, the clerk does not usually just grab foreclosure surplus and start paying your other random judgments on its own.** In Indiana, collection on a money judgment is normally enforced by execution or by **proceedings supplemental**, which have to be initiated by a creditor through a **verified motion** in the court where that judgment was entered; then the court orders nonexempt property applied to the judgment. That is not automatic. citeturn573104view0turn670166search1
> 
> But here is the part you cannot get sloppy on:
> 
> **If another creditor has a lien or an interest that was actually adjudicated in the foreclosure case, that interest can follow the surplus.** Indiana’s Court of Appeals just said the surplus stands in place of the real estate, and liens/interests that attached to the property attach to the surplus in priority order. It also quoted Indiana Code § 32-30-10-14: once sale proceeds exceed the amounts due, the surplus is paid to the clerk to be transferred, as the court directs, to the mortgage debtor, heirs, or assignees. citeturn688249view2turn976028view0
> 
> So your clean position is this:
> 
> - **Unrelated judgments elsewhere are not automatically paid from this surplus.** A creditor would usually need to affirmatively pursue collection. citeturn573104view0turn670166search1
> - **Amex and Chase not appearing or filing anything is good for you.** It supports saying there is **no present competing claimant** asking for the funds.
> - **But silence alone is not a magic bar forever.** In the 2025 Sanders case, a junior lienholder got surplus proceeds **after the sale** because the foreclosure order had already reserved payment to it “as its interest may be proven upon further application to the Court.” So the real question is not just “did they stay quiet?” but **whether this case ever adjudged or reserved any rights for them.** citeturn688249view1turn976028view1
> 
> That means your motion should **not** say:
> > “No one could possibly have a claim.”
> 
> It should say:
> > “No co-defendant has filed a motion, objection, verified claim, or other application seeking disbursement of the surplus funds, and no competing claimant has established a superior entitlement to those funds.”
> 
> That is accurate and strong.
> 
> The key factual check before filing is this:
> - Were Amex and Chase just named as possible parties and then never appeared?
> - Or did any order/decree specifically mention them, reserve rights for them, default them into some lien-priority bucket, or say they may later prove an interest?
> 
> If the answer is **they were just named and then nothing**, that is a strong fact for immediate release.
> If the answer is **the decree reserved rights for them**, then timing alone does not kill their claim. citeturn976028view1turn976028view0
> 
> Best wording for your filing:
> > Defendant is unaware of any co-defendant who has filed a motion or verified application seeking distribution of the surplus funds, and no order presently identifies any competing claimant as entitled to those funds.
> 
> That keeps you aggressive without overstating.

### User
> can i assert that i have no agreement or contract or no know statute that give any other creditor to this lien, nothing else was attached to it at all.

### Assistant
> Not in that absolute form.
> 
> Do **not** say:
> - “no statute gives any other creditor any right”
> - “nothing else was attached at all”
> - “no one else can have any claim”
> 
> That is too broad and turns into a legal conclusion you do not need to make.
> 
> What the record supports is narrower:
> 
> - FCFCU **named** American Express and JP Morgan Chase as defendants in the foreclosure from the beginning. fileciteturn11file15
> - The court initially denied default because there was **no return of service** on Amex or Chase, then FCFCU later filed an omitted notice claiming certified-mail service on both. fileciteturn11file0 fileciteturn11file9
> - The amended foreclosure decree then proceeded against Cody, Amex, and Chase, and the sale-proceeds language says any remaining sums go to the clerk **for the benefit of parties who may properly claim an interest**, subject to further court order. fileciteturn11file17 fileciteturn11file10
> - In the materials we have been working from, I do **not** see any appearance, motion for surplus, objection, or other affirmative claim by Amex or Chase. The docket summary shows notices to them, but not a surplus claim by them. fileciteturn11file5 fileciteturn11file11
> 
> So the safe assertion is:
> 
> > Defendant is unaware of any agreement, recorded lien instrument, court order, or pending application in this cause that grants any co-defendant a present right to disbursement of the surplus funds. Although American Express National Bank, N.A. and JP Morgan Chase Bank, N.A. were named as defendants in this foreclosure, no co-defendant has filed a motion, objection, or verified application seeking distribution of the surplus funds, and no competing claimant has established a superior entitlement to those funds.
> 
> That works because it stays in **knowledge + record + present posture**.
> 
> What you **can** also say:
> - you are not aware of any contract or agreement in the foreclosure record assigning your surplus to another creditor
> - no creditor other than FCFCU has appeared in this case asking for the money
> - no competing claim has been proven
> 
> What you should **not** say:
> - that other creditors have zero possible legal path, ever
> - that the statute gives them no rights at all
> - that naming Amex and Chase was random unless you can prove that
> 
> Best line for your motion:
> 
> > Defendant is unaware of any agreement, recorded lien, court order, or filed claim in this cause that would entitle any co-defendant to present disbursement of the surplus funds, and no co-defendant has appeared to request such relief.
> 
> That is tight and defensible.
> 
> If you want, I’ll now fold this exact wording into the surplus-disbursement motion so it is filing-ready.

### User
> and the deed was clean there was no other liens, so im not sure why they were on there but anyways, give me the final motions i need to file, i dont need to file exhibits do i becuase its all in the record all ready.

### Assistant
> Yes. Keep it tight.
> 
> ## What to file
> 
> File **one main paper**:
> 
> **Defendant’s Response to Plaintiff’s Motion for Acceptance of Overbid Calculation, Limited Non-Objection to Acceptance of Calculation, and Cross-Motion to Direct Immediate Disbursement of Surplus Funds**
> 
> That is the cleanest move because FCFCU already filed a motion asking the court to accept its overbid calculation on **4/21/2026**. fileciteturn12file4
> 
> Then file **one separate proposed order**, because Indiana Trial Rule 7(B) now requires a written motion to be accompanied by a **separate proposed order**. If you want a hearing, Indiana Trial Rule 7(C) says the hearing request should be made by **separate motion**. citeturn137701search0turn137701search3
> 
> ## Do you need exhibits?
> 
> **Probably not, if you want the short answer.**
> 
> You can rely on the existing record because the key documents are already there:
> - the amended foreclosure decree says remaining sums, if any, go to the clerk **to be held for the benefit of the parties subject to further order of the court**; that is exactly why you need a disbursement order now. fileciteturn12file19
> - FCFCU has already filed its own motion asking the court to accept an overbid calculation. fileciteturn12file4
> - the case materials show Amex and Chase were named, service was an issue, then FCFCU filed an omitted notice of service, and the amended decree proceeded against them as defaulted/nonappearing defendants. fileciteturn12file2turn12file11turn12file1
> 
> So no, you do **not** need to reattach half the case file just because it exists in the docket already.
> 
> What I **would** attach, if you want to make the judge’s life easier, is only this:
> - **one single-page calculation summary** showing your verifiable total of **$232,889.84**, paid amount of **$240,464.20**, resulting surplus of **$7,574.36**, and remaining variance of **$52.99**.
> 
> That is not because it is legally required. It is because judges like clean arithmetic. But if you do not want exhibits, you can put those numbers directly in the motion body and skip them. Indiana Trial Rule 5 requires service/f filing of the motion papers, but it does not require you to attach docketed materials again just to mention them. citeturn137701search3turn137701search0
> 
> ## What not to file
> 
> Do **not** file a separate sanctions motion right now.  
> Do **not** file a long rant about Amex/Chase.  
> Do **not** file a broad “no objections” notice by itself.
> 
> You want the court to do one thing: **release the money now.**
> 
> ---
> 
> ## Final motion
> 
> ```markdown
> STATE OF INDIANA                )
>                                 ) SS:
> COUNTY OF MARION                )
> 
> IN THE MARION SUPERIOR COURT 3
> 
> CAUSE NO. 49D03-2501-MF-002559
> 
> FINANCIAL CENTER FIRST CREDIT UNION,
>     Plaintiff,
> 
> v.
> 
> CODY RICE-VELASQUEZ, et al.,
>     Defendants.
> 
> DEFENDANT’S RESPONSE TO PLAINTIFF’S MOTION FOR ACCEPTANCE OF OVERBID CALCULATION, LIMITED NON-OBJECTION TO ACCEPTANCE OF CALCULATION, AND CROSS-MOTION TO DIRECT IMMEDIATE DISBURSEMENT OF SURPLUS FUNDS
> 
> Defendant, Cody Rice-Velasquez, pro se, respectfully responds to Plaintiff’s Motion for Acceptance of Overbid Calculation and moves for immediate disbursement of surplus funds, and states:
> 
> 1. On April 21, 2026, Plaintiff filed its Motion for Acceptance of Overbid Calculation. 
> 
> 2. Defendant previously objected to Plaintiff’s shifting and insufficiently supported surplus-related figures because the record reflected material inconsistencies across filings and supporting information was not fully provided at the outset.
> 
> 3. Defendant has now completed a reconciliation using the figures presently supported by the record and the later-surfaced cost information.
> 
> 4. Based on Defendant’s reconciliation, the verifiable total amount properly chargeable against the sale proceeds is $232,889.84.
> 
> 5. The amount paid at sheriff’s sale was $240,464.20.
> 
> 6. Based on those figures, Defendant calculates the surplus as $7,574.36.
> 
> 7. The remaining variance between Plaintiff’s position and Defendant’s position is only $52.99.
> 
> 8. Defendant therefore does not presently object to the Court accepting Plaintiff’s overbid calculation for purposes of resolving the surplus issue, to the extent the Court finds the remaining variance immaterial.
> 
> 9. Defendant’s limited non-objection is made solely to avoid further unnecessary delay over a now largely reconciled arithmetic issue and shall not be construed as a concession that Plaintiff’s earlier filings were complete, clear, or properly supported when filed.
> 
> 10. The Amended Default Judgment and Decree of Foreclosure directs that remaining sums, if any, are to be paid to the Clerk and held for the benefit of the parties subject to further order of the Court.
> 
> 11. No co-defendant has filed a motion, objection, verified claim, or other application seeking distribution of the surplus funds.
> 
> 12. Defendant is unaware of any agreement, recorded lien instrument, court order, or pending application in this cause that grants any co-defendant a present right to disbursement of the surplus funds.
> 
> 13. Although American Express National Bank, N.A. and JP Morgan Chase Bank, N.A. were named as defendants in this foreclosure action, Defendant is unaware of any appearance by them or any motion by them seeking surplus proceeds.
> 
> 14. No competing claimant has established a superior entitlement to the surplus funds presently at issue.
> 
> 15. Defendant is the mortgage debtor and former owner of the property that was the subject of this foreclosure action.
> 
> 16. Further delay in disbursement serves no legitimate purpose where the existence of surplus funds is established and any remaining variance is minimal.
> 
> WHEREFORE, Defendant respectfully requests that the Court:
> 
> A. grant Plaintiff’s Motion for Acceptance of Overbid Calculation only to the extent necessary to resolve the surplus issue without further delay;
> 
> B. find that surplus funds exist from the sheriff’s sale in this matter;
> 
> C. direct the Clerk to immediately disburse the surplus funds to Defendant Cody Rice-Velasquez;
> 
> D. disburse $7,574.36 if the Court adopts Defendant’s reconciliation, or in the alternative disburse the amount the Court finds supported without further delay; and
> 
> E. grant all other just and proper relief.
> 
> Respectfully submitted,
> 
> Cody Rice-Velasquez
> 1000 Fulton Pkwy Apt 107
> Evansville, IN 47710
> 317-205-4383
> crice4485@gmail.com
> Defendant, pro se
> 
> CERTIFICATE OF SERVICE
> 
> I certify that on __________________, 2026, I served a copy of this Motion upon all counsel of record and all self-represented parties by Indiana E-Filing and/or by any other method required by rule.
> 
> Cody Rice-Velasquez
> ```
> 
> ---
> 
> ## Proposed order
> 
> ```markdown
> STATE OF INDIANA                )
>                                 ) SS:
> COUNTY OF MARION                )
> 
> IN THE MARION SUPERIOR COURT 3
> 
> CAUSE NO. 49D03-2501-MF-002559
> 
> FINANCIAL CENTER FIRST CREDIT UNION,
>     Plaintiff,
> 
> v.
> 
> CODY RICE-VELASQUEZ, et al.,
>     Defendants.
> 
> ORDER ON DEFENDANT’S RESPONSE, LIMITED NON-OBJECTION, AND CROSS-MOTION TO DIRECT IMMEDIATE DISBURSEMENT OF SURPLUS FUNDS
> 
> The Court, having reviewed Plaintiff’s Motion for Acceptance of Overbid Calculation and Defendant’s Response, Limited Non-Objection, and Cross-Motion to Direct Immediate Disbursement of Surplus Funds, now finds:
> 
> 1. The surplus-calculation dispute has been materially narrowed.
> 2. Surplus funds exist from the sheriff’s sale in this matter.
> 3. No competing claimant has established a superior present entitlement to the surplus funds at issue.
> 4. Prompt disbursement is appropriate.
> 
> IT IS THEREFORE ORDERED that:
> 
> 1. The Court accepts the overbid calculation for purposes of resolving the surplus issue.
> 2. The Clerk shall immediately disburse surplus funds in this cause to Defendant Cody Rice-Velasquez in the amount of $________________.
> 3. If such funds have not yet been deposited with the Clerk, Plaintiff shall deposit the surplus funds with the Clerk within ____ days of this Order, and the Clerk shall disburse them immediately upon receipt.
> 
> SO ORDERED this ___ day of ____________, 2026.
> 
> ________________________________
> Judge, Marion Superior Court 3
> ```
> 
> ---
> 
> ## If you want a hearing
> 
> Only file this if you think the court may sit on it. Indiana Trial Rule 7(C) says hearing requests should be by separate motion. citeturn137701search0
> 
> ```markdown
> DEFENDANT’S SEPARATE REQUEST FOR PROMPT HEARING
> 
> Defendant respectfully requests a prompt hearing on Defendant’s Response, Limited Non-Objection, and Cross-Motion to Direct Immediate Disbursement of Surplus Funds, if the Court determines a hearing is necessary. Defendant believes the remaining variance is only $52.99 and that prompt resolution is appropriate.
> ```
> 
> ## Bottom line
> 
> File:
> 1. the combined response/non-objection/cross-motion  
> 2. the separate proposed order  
> 3. optional separate request for hearing
> 
> And no, you do **not** need to dump the whole record back in as exhibits just because it exists. If you attach anything, make it only a one-page math summary.
> 
> One correction: I would **not** say “the deed was clean” in the motion unless you have the title commitment, title policy, or deed record in hand and are prepared to cite it. The safer and stronger line is the one above: **no co-defendant has filed any claim for the surplus and no competing claimant has established present entitlement.** That is enough.

### User
> {'asset_pointer': 'sediment://file_00000000557071f8b8d7a4c434af76f8', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 538, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 33560, 'width': 433}i have finalized the final audit and its not 52.99 difference its way more. look. 
> Scenario	Verifiable	Decree of Foreclosure	04/21 - Plantiffs	Diff	Notes
> Balance Due 4/29/25
> Confirmed Match	$217,672.08	$217,672.08	$217,672.08	$0.00	
> Court Costs	$191.01	$191.01	$191.01	$0.00	
> Attorney Fees	$3,000.00	$3,000.00	$3,000.00	$0.00	
> Judgement Total	$220,863.09	$220,863.09	$220,863.09	$0.00	
> Interest to date 
> of judgement 
> 04/29-05/58	$796.05	$796.05	$1,452.30	-$656.25	Interest through the sale date is in total and only 30 days were allowed. 
> After Interest	$221,659.14	$221,659.14	$222,315.39	-$656.25	
> Taxes	$7,600.81	$7,600.81	$7,600.81	$0.00	
> After Taxes	$229,259.95	$229,259.95	$229,916.20	-$656.25	
> Sherriff	$338.00	$338.00	$338.00	$0.00	
> Advertisement	$284.28	$284.28	$284.28	$0.00	
> Sherrif SubTotal	$622.28	$622.28	$622.28	$0.00	
> After Sherrif	$229,882.23	$229,882.23	$230,538.48	-$656.25	
> Publication	$1,094.35	$1,094.35	$1,094.35	$0.00	
> Clerk	$35.00	$35.00	$35.00	$0.00	
> After Pub-Clerk	$231,011.58	$231,011.58	$231,667.83	-$656.25	
> Attorney	$1,275.00	$1,275.00	$1,275.00	$0.00	
> 	$232,286.58	$232,286.58	$232,942.83	-$656.25	
> Surplus Calc	$8,177.62	$8,177.62	$7,521.37	$8,177.62

### Assistant
> Yep. That changes the play.
> 
> This is **not** a de minimis $52.99 issue anymore.  
> Based on your finalized audit, the real dispute is **$656.25**, and it sits in one place: **Plaintiff overstated post-4/29 interest**. Their 4/21 overbid motion is the paper you answer. fileciteturn8file0
> 
> So do **not** file a limited non-objection now.
> 
> ## File this package
> 
> Under Indiana Trial Rule 7, your written motion should have a **separate proposed order**, and if you want a hearing, that request should be a **separate motion**. Service/filling is governed by Trial Rule 5. Indiana’s foreclosure surplus statute says excess proceeds go to the clerk to be transferred, as the court directs, to the mortgage debtor or assignee. citeturn221801search0turn221801search1turn656233search0
> 
> ### 1. Main filing
> **Defendant’s Response in Partial Opposition to Plaintiff’s Motion for Acceptance of Overbid Calculation and Cross-Motion to Determine Surplus and Direct Immediate Disbursement of Surplus Funds**
> 
> ### 2. Separate proposed order
> Required. citeturn221801search0
> 
> ### 3. Optional separate request for prompt hearing
> Only if you think the court may sit on it. citeturn221801search0
> 
> ## Exhibits
> 
> You do **not** need to dump the existing record back in. But for this filing, attach **one page**:
> 
> - **Exhibit A: Final Audit Summary**
> 
> That is worth it because this is now a targeted math dispute.  
> You do **not** need to reattach the whole decree, sale papers, and motion unless you want to spoon-feed the judge. If you do attach anything else, keep it to one additional page max.
> 
> Also: fix your typo before filing. It should read **04/29–05/28**, not **05/58**.
> 
> ---
> 
> ## Main motion
> 
> ```text
> STATE OF INDIANA                )
>                                 ) SS:
> COUNTY OF MARION                )
> 
> IN THE MARION SUPERIOR COURT 3
> 
> CAUSE NO. 49D03-2501-MF-002559
> 
> FINANCIAL CENTER FIRST CREDIT UNION,
>     Plaintiff,
> 
> v.
> 
> CODY RICE-VELASQUEZ, et al.,
>     Defendants.
> 
> DEFENDANT’S RESPONSE IN PARTIAL OPPOSITION TO PLAINTIFF’S MOTION FOR ACCEPTANCE OF OVERBID CALCULATION AND CROSS-MOTION TO DETERMINE SURPLUS AND DIRECT IMMEDIATE DISBURSEMENT OF SURPLUS FUNDS
> 
> Defendant, Cody Rice-Velasquez, pro se, responds in partial opposition to Plaintiff’s Motion for Acceptance of Overbid Calculation and moves for determination and immediate disbursement of surplus funds, and states:
> 
> 1. On April 21, 2026, Plaintiff filed its Motion for Acceptance of Overbid Calculation.
> 
> 2. Defendant has completed a final audit of the overbid calculation using the figures reflected in the foreclosure decree and the verifiable sale-related costs.
> 
> 3. Defendant’s audit confirms that the following figures match:
>    a. Balance Due as of 4/29/2025: $217,672.08;
>    b. Court Costs: $191.01;
>    c. Attorney Fees in the Decree: $3,000.00;
>    d. Judgment Total: $220,863.09;
>    e. Taxes: $7,600.81;
>    f. Sheriff Fees: $338.00;
>    g. Advertisement: $284.28;
>    h. Publication: $1,094.35;
>    i. Clerk: $35.00; and
>    j. Additional Attorney Fee: $1,275.00.
> 
> 4. The remaining dispute is not over those line items. The dispute is Plaintiff’s interest figure.
> 
> 5. Defendant calculates interest from April 29, 2025 through May 28, 2025 as $796.05.
> 
> 6. Plaintiff’s April 21, 2026 overbid calculation instead uses $1,452.30 for that interest line, which overstates the figure by $656.25.
> 
> 7. Because of that overstatement, Plaintiff’s total overbid calculation is overstated by $656.25.
> 
> 8. Defendant’s audited total properly chargeable against the sale proceeds is $232,286.58.
> 
> 9. The sheriff’s sale amount paid was $240,464.20.
> 
> 10. Based on those figures, Defendant calculates the surplus as $8,177.62.
> 
> 11. Plaintiff’s calculation yields a lower surplus of $7,521.37 solely because of the disputed $656.25 interest overstatement.
> 
> 12. Defendant therefore objects to Plaintiff’s Motion for Acceptance of Overbid Calculation to the extent it includes the overstated interest amount.
> 
> 13. Defendant requests that the Court determine the correct surplus as $8,177.62 and direct immediate disbursement of that amount to Defendant.
> 
> 14. In the alternative, if the Court declines to resolve the $656.25 difference immediately, Defendant requests that the Court direct immediate disbursement of the undisputed surplus amount of $7,521.37, with the remaining $656.25 to be resolved separately if necessary.
> 
> 15. No co-defendant has filed a motion, objection, verified claim, or other application seeking distribution of the surplus funds.
> 
> 16. Defendant is unaware of any agreement, recorded lien instrument, court order, or pending application in this cause that grants any co-defendant a present right to disbursement of the surplus funds.
> 
> 17. Defendant is the mortgage debtor and former owner of the property that was the subject of this foreclosure action.
> 
> 18. Further delay in disbursement serves no legitimate purpose where the existence of surplus funds is established and the remaining dispute is a narrow mathematical issue.
> 
> WHEREFORE, Defendant respectfully requests that the Court:
> 
> A. deny Plaintiff’s Motion for Acceptance of Overbid Calculation to the extent it includes the overstated interest amount of $656.25;
> 
> B. determine the proper total chargeable amount as $232,286.58;
> 
> C. determine the proper surplus as $8,177.62;
> 
> D. direct the Clerk to immediately disburse $8,177.62 to Defendant Cody Rice-Velasquez;
> 
> E. in the alternative, immediately disburse the undisputed amount of $7,521.37 to Defendant and reserve only the disputed $656.25 for further determination if the Court deems necessary; and
> 
> F. grant all other just and proper relief.
> 
> Respectfully submitted,
> 
> Cody Rice-Velasquez
> 1000 Fulton Pkwy Apt 107
> Evansville, IN 47710
> 317-205-4383
> crice4485@gmail.com
> Defendant, pro se
> 
> CERTIFICATE OF SERVICE
> 
> I certify that on __________________, 2026, I served a copy of this Motion upon all counsel of record and all self-represented parties by Indiana E-Filing and/or by any other method required by rule.
> 
> Cody Rice-Velasquez
> ```
> 
> ---
> 
> ## Proposed order
> 
> ```text
> STATE OF INDIANA                )
>                                 ) SS:
> COUNTY OF MARION                )
> 
> IN THE MARION SUPERIOR COURT 3
> 
> CAUSE NO. 49D03-2501-MF-002559
> 
> FINANCIAL CENTER FIRST CREDIT UNION,
>     Plaintiff,
> 
> v.
> 
> CODY RICE-VELASQUEZ, et al.,
>     Defendants.
> 
> ORDER ON DEFENDANT’S RESPONSE IN PARTIAL OPPOSITION TO PLAINTIFF’S MOTION FOR ACCEPTANCE OF OVERBID CALCULATION AND CROSS-MOTION TO DETERMINE SURPLUS AND DIRECT IMMEDIATE DISBURSEMENT OF SURPLUS FUNDS
> 
> The Court, having reviewed Plaintiff’s Motion for Acceptance of Overbid Calculation and Defendant’s Response in Partial Opposition and Cross-Motion, now finds:
> 
> 1. Surplus funds exist from the sheriff’s sale in this matter.
> 2. The principal dispute concerns Plaintiff’s interest calculation.
> 3. The Court finds the proper total chargeable amount to be $________________.
> 4. The Court finds the proper surplus amount to be $________________.
> 5. No competing claimant has established a superior present entitlement to the surplus funds.
> 
> IT IS THEREFORE ORDERED that:
> 
> 1. Plaintiff’s Motion for Acceptance of Overbid Calculation is GRANTED / DENIED IN PART consistent with this Order.
> 2. The Clerk shall immediately disburse surplus funds in this cause to Defendant Cody Rice-Velasquez in the amount of $________________.
> 
> OR, IN THE ALTERNATIVE:
> 
> 3. The Clerk shall immediately disburse the undisputed amount of $7,521.37 to Defendant Cody Rice-Velasquez, and the remaining disputed amount of $656.25 shall remain pending further order of the Court.
> 
> SO ORDERED this ___ day of ____________, 2026.
> 
> ________________________________
> Judge, Marion Superior Court 3
> ```
> 
> ---
> 
> ## Optional separate hearing request
> 
> ```text
> STATE OF INDIANA                )
>                                 ) SS:
> COUNTY OF MARION                )
> 
> IN THE MARION SUPERIOR COURT 3
> 
> CAUSE NO. 49D03-2501-MF-002559
> 
> FINANCIAL CENTER FIRST CREDIT UNION,
>     Plaintiff,
> 
> v.
> 
> CODY RICE-VELASQUEZ, et al.,
>     Defendants.
> 
> DEFENDANT’S SEPARATE REQUEST FOR PROMPT HEARING
> 
> Defendant respectfully requests a prompt hearing on Defendant’s Response in Partial Opposition to Plaintiff’s Motion for Acceptance of Overbid Calculation and Cross-Motion to Determine Surplus and Direct Immediate Disbursement of Surplus Funds, if the Court determines a hearing is necessary.
> 
> The remaining dispute is narrow and mathematical, and prompt resolution is appropriate.
> 
> Respectfully submitted,
> 
> Cody Rice-Velasquez
> ```
> 
> ## Bottom line
> 
> Your lane now is:
> 
> - **oppose their overbid calc in part**
> - **show the only live error is $656.25 in interest**
> - **ask for $8,177.62**
> - **fallback ask: release $7,521.37 now**
> 
> That fallback is not weakness. It blocks them from using a tiny math dispute as a stall tactic.

### User
> but here is where we get strategic, i have rent due in 7 days, and bills piling up fiting more about this 656 could cost me more in hardship, late fees, interest on other debts ect, how do i move the court to accept their calculation and pay me the 7k they agreed to, and move on to the larger opportunity of settlement of the FCRA, NCUA, CFPB, ADA Claims that are way more than 656 plus the 7k will help me get the things i need to do those claims if they get silly and dont try to settle.

### Assistant
> Yes. If rent is due in 7 days, the smart move is to **trade the $656.25 fight for speed**.
> 
> That means you file a paper that says, in substance:
> 
> - you **consent** to acceptance of Plaintiff’s overbid calculation **for the limited purpose of immediate disbursement**
> - you ask the court to order the clerk to pay you the **$7,521.37** now
> - you expressly **do not waive** any separate non-surplus claims against FCFCU or anyone else
> 
> That is clean, strategic, and aligned with the statute: once there is surplus, it is paid to the clerk and then transferred **as the court directs** to the mortgage debtor or other assigned person. Indiana Trial Rule 7 now requires the written motion to be accompanied by a **separate proposed order**, and any hearing request has to be made by **separate motion**. FCFCU already filed its Motion for Acceptance of Overbid Calculation on **4/21/2026**, so you can respond directly to that filing instead of starting a new side war. citeturn659348search0turn659348search1 fileciteturn8file0
> 
> The important truth: this probably **ends your claim to the extra $656.25 in this surplus dispute** unless the court chooses to preserve it. If your real priority is rent, stability, and funding the bigger FCRA / NCUA / CFPB / ADA pressure points, that is a rational trade.
> 
> Do **not** put the bigger claims in this motion. That would be a mistake. This motion should be one thing only: **accept their number, release the money now, reserve unrelated claims**.
> 
> ## What to file
> 
> File two papers for sure, and a third only if needed:
> 
> 1. **Defendant’s Limited Consent to Plaintiff’s Motion for Acceptance of Overbid Calculation and Motion to Direct Immediate Disbursement of Surplus Funds**
> 2. **Separate Proposed Order**
> 3. **Optional separate request for prompt hearing / expedited consideration** if you think the judge may sit on it. Rule 7(C) says hearing requests are separate motions. citeturn659348search1turn233971search29
> 
> You do **not** need to attach the whole case again if the support is already in the record. I would attach only a one-page calculation summary if you want to make the judge’s life easier.
> 
> ## Best motion title
> 
> **DEFENDANT’S LIMITED CONSENT TO PLAINTIFF’S MOTION FOR ACCEPTANCE OF OVERBID CALCULATION AND MOTION TO DIRECT IMMEDIATE DISBURSEMENT OF SURPLUS FUNDS**
> 
> ## Filing-ready motion
> 
> ```text
> STATE OF INDIANA                )
>                                 ) SS:
> COUNTY OF MARION                )
> 
> IN THE MARION SUPERIOR COURT 3
> 
> CAUSE NO. 49D03-2501-MF-002559
> 
> FINANCIAL CENTER FIRST CREDIT UNION,
>     Plaintiff,
> 
> v.
> 
> CODY RICE-VELASQUEZ, et al.,
>     Defendants.
> 
> DEFENDANT’S LIMITED CONSENT TO PLAINTIFF’S MOTION FOR ACCEPTANCE OF OVERBID CALCULATION AND MOTION TO DIRECT IMMEDIATE DISBURSEMENT OF SURPLUS FUNDS
> 
> Defendant, Cody Rice-Velasquez, pro se, respectfully files this limited consent to Plaintiff’s Motion for Acceptance of Overbid Calculation and moves for immediate disbursement of surplus funds, and states:
> 
> 1. On April 21, 2026, Plaintiff filed its Motion for Acceptance of Overbid Calculation.
> 
> 2. Defendant completed an audit of the overbid calculation and identified a disputed difference in Plaintiff’s interest figure.
> 
> 3. Defendant maintains that Plaintiff’s calculation overstates the interest component by $656.25.
> 
> 4. However, Defendant’s rent and other essential obligations are immediately due, and continued litigation over that limited difference would likely cause greater hardship than the amount in dispute.
> 
> 5. In the interest of prompt resolution, Defendant therefore consents, solely for purposes of immediate surplus disbursement, to the Court’s acceptance of Plaintiff’s overbid calculation.
> 
> 6. Based on Plaintiff’s overbid calculation, the surplus amount to be disbursed is $7,521.37.
> 
> 7. To Defendant’s knowledge, no co-defendant has filed a motion, objection, verified claim, or other application seeking present distribution of the surplus funds.
> 
> 8. Defendant is the mortgage debtor and former owner of the property that was the subject of this foreclosure action.
> 
> 9. Defendant requests immediate disbursement of the surplus funds in the amount of $7,521.37.
> 
> 10. This limited consent is made solely to secure prompt release of the surplus funds and shall not be construed as:
>    a. an admission that Plaintiff’s prior calculations were accurate when made;
>    b. a waiver of Defendant’s position that Plaintiff’s interest calculation was overstated;
>    c. a waiver or release of any separate statutory, tort, disability-related, consumer-reporting, regulatory, or other claims Defendant may assert arising from matters outside the narrow surplus-disbursement issue.
> 
> WHEREFORE, Defendant respectfully requests that the Court:
> 
> A. grant Plaintiff’s Motion for Acceptance of Overbid Calculation for the limited purpose of resolving the surplus issue without further delay;
> 
> B. determine that surplus funds in the amount of $7,521.37 are to be disbursed;
> 
> C. direct the Clerk to immediately disburse $7,521.37 to Defendant Cody Rice-Velasquez; and
> 
> D. grant all other just and proper relief.
> 
> Respectfully submitted,
> 
> Cody Rice-Velasquez
> 1000 Fulton Pkwy Apt 107
> Evansville, IN 47710
> 317-205-4383
> crice4485@gmail.com
> Defendant, pro se
> 
> CERTIFICATE OF SERVICE
> 
> I certify that on __________________, 2026, I served a copy of this Motion upon all counsel of record and all self-represented parties by Indiana E-Filing and/or by any other method required by rule.
> 
> Cody Rice-Velasquez
> ```
> 
> ## Separate proposed order
> 
> ```text
> STATE OF INDIANA                )
>                                 ) SS:
> COUNTY OF MARION                )
> 
> IN THE MARION SUPERIOR COURT 3
> 
> CAUSE NO. 49D03-2501-MF-002559
> 
> FINANCIAL CENTER FIRST CREDIT UNION,
>     Plaintiff,
> 
> v.
> 
> CODY RICE-VELASQUEZ, et al.,
>     Defendants.
> 
> ORDER ON DEFENDANT’S LIMITED CONSENT TO PLAINTIFF’S MOTION FOR ACCEPTANCE OF OVERBID CALCULATION AND MOTION TO DIRECT IMMEDIATE DISBURSEMENT OF SURPLUS FUNDS
> 
> The Court, having reviewed Plaintiff’s Motion for Acceptance of Overbid Calculation and Defendant’s Limited Consent and Motion to Direct Immediate Disbursement of Surplus Funds, now finds:
> 
> 1. Plaintiff’s overbid calculation should be accepted for purposes of resolving the surplus issue.
> 2. Surplus funds exist in this matter.
> 3. Immediate disbursement is appropriate.
> 
> IT IS THEREFORE ORDERED that:
> 
> 1. Plaintiff’s Motion for Acceptance of Overbid Calculation is GRANTED.
> 2. The Clerk shall immediately disburse surplus funds in the amount of $7,521.37 to Defendant Cody Rice-Velasquez.
> 
> SO ORDERED this ___ day of ____________, 2026.
> 
> ________________________________
> Judge, Marion Superior Court 3
> ```
> 
> ## Optional separate request for prompt hearing
> 
> ```text
> STATE OF INDIANA                )
>                                 ) SS:
> COUNTY OF MARION                )
> 
> IN THE MARION SUPERIOR COURT 3
> 
> CAUSE NO. 49D03-2501-MF-002559
> 
> FINANCIAL CENTER FIRST CREDIT UNION,
>     Plaintiff,
> 
> v.
> 
> CODY RICE-VELASQUEZ, et al.,
>     Defendants.
> 
> DEFENDANT’S SEPARATE REQUEST FOR PROMPT HEARING OR EXPEDITED CONSIDERATION
> 
> Defendant respectfully requests a prompt hearing, or in the alternative expedited consideration on the papers, regarding Defendant’s Limited Consent to Plaintiff’s Motion for Acceptance of Overbid Calculation and Motion to Direct Immediate Disbursement of Surplus Funds.
> 
> The remaining dispute has been narrowed, Defendant consents to the overbid calculation for purposes of prompt release, and immediate financial hardship makes further delay prejudicial.
> 
> Respectfully submitted,
> 
> Cody Rice-Velasquez
> ```
> 
> ## Strategy note
> 
> This is the right move if your real objective is leverage, not perfection.
> 
> Take the **$7,521.37**, stabilize rent and bills, then use your bandwidth on the claims with real upside. The surplus fight is now a liquidity issue, not the main event.
> 
> One extra move worth making: send opposing counsel a same-day message saying you will file limited consent unless they will submit an agreed order for immediate disbursement today.

### User
> wait wait wait, im not showing them my hand that i am accepting this cause im broke, we are eating that 656 and moving one from this. only thing it shoudl state is that i am accepting their figure but not waiving my rights to other disputes in the future from other claims related to this matter or something,

### Assistant
> Correct. Do **not** put hardship in the motion.
> 
> Keep it cold:
> 
> - you accept **their figure**
> - you want **immediate disbursement**
> - you are **not waiving** any other rights, claims, defenses, objections, or remedies outside this narrow surplus-disbursement issue
> 
> That is the right framing.
> 
> ## Use this title
> 
> **DEFENDANT’S LIMITED CONSENT TO PLAINTIFF’S MOTION FOR ACCEPTANCE OF OVERBID CALCULATION AND MOTION TO DIRECT IMMEDIATE DISBURSEMENT OF SURPLUS FUNDS**
> 
> ## Final motion
> 
> ```text
> STATE OF INDIANA                )
>                                 ) SS:
> COUNTY OF MARION                )
> 
> IN THE MARION SUPERIOR COURT 3
> 
> CAUSE NO. 49D03-2501-MF-002559
> 
> FINANCIAL CENTER FIRST CREDIT UNION,
>     Plaintiff,
> 
> v.
> 
> CODY RICE-VELASQUEZ, et al.,
>     Defendants.
> 
> DEFENDANT’S LIMITED CONSENT TO PLAINTIFF’S MOTION FOR ACCEPTANCE OF OVERBID CALCULATION AND MOTION TO DIRECT IMMEDIATE DISBURSEMENT OF SURPLUS FUNDS
> 
> Defendant, Cody Rice-Velasquez, pro se, respectfully files this Limited Consent to Plaintiff’s Motion for Acceptance of Overbid Calculation and moves for immediate disbursement of surplus funds, and states:
> 
> 1. On April 21, 2026, Plaintiff filed its Motion for Acceptance of Overbid Calculation. fileciteturn8file0
> 
> 2. For the limited purpose of resolving the surplus-disbursement issue without further delay, Defendant consents to the Court’s acceptance of Plaintiff’s overbid calculation.
> 
> 3. Based on Plaintiff’s overbid calculation, the surplus amount to be disbursed is $7,521.37.
> 
> 4. To Defendant’s knowledge, no co-defendant has filed a motion, objection, verified claim, or other application seeking present distribution of the surplus funds.
> 
> 5. Defendant is the mortgage debtor and former owner of the property that was the subject of this foreclosure action.
> 
> 6. Defendant therefore requests that the Court direct immediate disbursement of the surplus funds in the amount of $7,521.37 to Defendant.
> 
> 7. This limited consent is made solely for purposes of resolving the surplus-disbursement issue and shall not be construed as:
> 
>    a. a waiver of any other objections, claims, defenses, rights, or remedies Defendant has or may have;
> 
>    b. a release of any separate statutory, regulatory, disability-related, consumer-reporting, servicing, collection, procedural, or other claims arising from this matter or related conduct;
> 
>    c. an admission that Plaintiff’s prior calculations, conduct, filings, or representations were accurate, complete, timely, or otherwise proper for any purpose beyond this narrow surplus-disbursement issue; or
> 
>    d. a waiver of any claim arising from matters outside the Court’s acceptance of Plaintiff’s overbid calculation and present disbursement of surplus funds.
> 
> WHEREFORE, Defendant respectfully requests that the Court:
> 
> A. grant Plaintiff’s Motion for Acceptance of Overbid Calculation for the limited purpose of resolving the surplus-disbursement issue;
> 
> B. determine that surplus funds in the amount of $7,521.37 are to be disbursed;
> 
> C. direct the Clerk to immediately disburse $7,521.37 to Defendant Cody Rice-Velasquez; and
> 
> D. grant all other just and proper relief.
> 
> Respectfully submitted,
> 
> Cody Rice-Velasquez
> 1000 Fulton Pkwy Apt 107
> Evansville, IN 47710
> 317-205-4383
> crice4485@gmail.com
> Defendant, pro se
> 
> CERTIFICATE OF SERVICE
> 
> I certify that on __________________, 2026, I served a copy of this Motion upon all counsel of record and all self-represented parties by Indiana E-Filing and/or by any other method required by rule.
> 
> Cody Rice-Velasquez
> ```
> 
> ## Proposed order
> 
> ```text
> STATE OF INDIANA                )
>                                 ) SS:
> COUNTY OF MARION                )
> 
> IN THE MARION SUPERIOR COURT 3
> 
> CAUSE NO. 49D03-2501-MF-002559
> 
> FINANCIAL CENTER FIRST CREDIT UNION,
>     Plaintiff,
> 
> v.
> 
> CODY RICE-VELASQUEZ, et al.,
>     Defendants.
> 
> ORDER ON DEFENDANT’S LIMITED CONSENT TO PLAINTIFF’S MOTION FOR ACCEPTANCE OF OVERBID CALCULATION AND MOTION TO DIRECT IMMEDIATE DISBURSEMENT OF SURPLUS FUNDS
> 
> The Court, having reviewed Plaintiff’s Motion for Acceptance of Overbid Calculation and Defendant’s Limited Consent and Motion to Direct Immediate Disbursement of Surplus Funds, now finds:
> 
> 1. Plaintiff’s overbid calculation should be accepted for purposes of resolving the surplus-disbursement issue.
> 2. Surplus funds exist in this matter.
> 3. Immediate disbursement is appropriate.
> 
> IT IS THEREFORE ORDERED that:
> 
> 1. Plaintiff’s Motion for Acceptance of Overbid Calculation is GRANTED.
> 2. The Clerk shall immediately disburse surplus funds in the amount of $7,521.37 to Defendant Cody Rice-Velasquez.
> 
> SO ORDERED this ___ day of ____________, 2026.
> 
> ________________________________
> Judge, Marion Superior Court 3
> ```
> 
> ## Do not say
> - you need rent
> - you are accepting because of hardship
> - you are reserving the right to fight the $656 later in this same surplus lane
> 
> If you file this, you are basically done fighting the surplus math. That is fine. Just keep the reservation broad and aimed at **other claims**.
> 
> The cleanest next step after filing is a short service email to plaintiff’s counsel saying you filed a limited consent and request immediate proposed order entry.

### Assistant
> That review is mostly right. The only parts worth actually acting on are the housekeeping fixes, not a rewrite. fileciteturn13file0
> 
> Use the filing strategy we already landed on:
> - **limited consent to accept their overbid figure**
> - **motion to direct immediate disbursement of $7,521.37**
> - **broad reservation of all other claims outside the surplus issue**
> 
> Three fixes before you file:
> 
> 1. **Make the title consistent everywhere.**  
> Use the same label on the motion and proposed order:
> **Defendant’s Limited Consent to Plaintiff’s Motion for Acceptance of Overbid Calculation and Motion to Direct Immediate Disbursement of Surplus Funds**
> 
> 2. **Fill in the proposed order.**  
> Do not leave blanks if you already know the number. Put:
> - **$7,521.37**
> - “**immediately**” instead of leaving a deadline blank
> 
> 3. **Do not overcorrect with a verification unless you want to.**  
> Indiana Trial Rule 11 says pleadings and motions **do not need to be verified or accompanied by affidavit unless a rule specifically requires it**. So verification is optional, not mandatory. citeturn596027search1
> 
> Two legal points you should keep intact:
> - Indiana Trial Rule 7 now requires a written motion to be accompanied by a **separate proposed order**, and any hearing request should be a **separate motion**. citeturn596027search2
> - Indiana Code § 32-30-10-14 says foreclosure surplus is paid to the clerk and then transferred, as the court directs, to the mortgage debtor or other assigned person. citeturn596027search0
> 
> On exhibits: you do **not** need to reattach the whole case file just because it is already in the record. The clean version is:
> - file the motion
> - file the separate proposed order
> - optionally attach **one-page calculation summary**
> - skip everything else
> 
> So the final tactical answer is:
> 
> **File the motion as-is, with title cleanup, a completed proposed order, and no poverty explanation.**  
> That is the right balance of speed, optics, and reservation of leverage.
> 
> Use this reservation sentence verbatim if you want it tighter:
> 
> > This limited consent is made solely for purposes of resolving the surplus-disbursement issue and shall not be construed as a waiver, release, admission, or concession as to any other claims, defenses, rights, remedies, objections, or causes of action arising from this matter or related conduct.
> 
> If you want, I’ll give you the fully cleaned final motion and matching proposed order in one locked version with all inconsistencies removed.

### User
> yes, give it to me in canvas. and use this as the top part of the documents
> STATE OF INDIANA
> 
> COUNTY OF MARION
> )
> )    SS: 
> )
> THE MARION SUPERIOR COURT 3
> 
> CAUSE NO: 49D03-2501-MF-002559
> FINANCIAL CENTER FIRST CREDIT UNION,
> )
> )
>      Plaintiff,
> )  
> )
> v.
> )
> CODY RICE-VELASQUEZ;
> )
> Defendant.
> )

### Assistant
> Done. It’s in canvas.

### User
> **Overall Assessment:** This is an improved version of the previous filing. The revisions make it cleaner, more concise, and slightly more professional while maintaining the strong strategic protections. It remains a solid pro se document that should effectively prompt the Marion Superior Court (Cause No. 49D03-2501-MF-002559) to accept the overbid calculation on a limited basis and order immediate disbursement of the **$7,521.37** surplus to you (Cody Rice-Velasquez) as the mortgage debtor/former owner under **IC 32-30-10-14**.
> 
> The core approach is still excellent: limited consent to avoid delay, clear entitlement language, strong reservation of rights, and a ready-to-sign proposed order. No major legal flaws.
> 
> ### Key Improvements from the Prior Version
> - **Reservation of Rights (Paragraph 7)**: Expanded and rephrased for broader, clearer protection ("a waiver, release, admission, or concession as to any other claims..."; added "or concession"). This strengthens your position against future arguments of waiver or estoppel. The four subparts (a–d) are now tighter and more comprehensive.
> - **Contact Information**: Updated address to **1000 Fulton Pkwy Apt 107, Evansville, IN 47710** (with new phone **812-266-1369**). This matches your current location—good to keep accurate for service and disbursement.
> - **Certificate of Service**: Simplified and standardized ("I certify that on April 24th, 2026, I served a copy... by Indiana E-Filing and/or by any other method required by rule."). This is more compliant with Indiana e-filing norms and Trial Rules.
> - **Proposed Order**: Significantly streamlined and improved.
>   - Shorter, more direct findings (no overly detailed "materially narrowed" language).
>   - Explicitly grants plaintiff's motion outright (while your consent is limited).
>   - Fills in the exact amount **$7,521.37** and directs immediate disbursement by the Clerk—no vague blanks for the amount.
>   - Cleaner structure overall, making it easier for the judge to sign with minimal changes.
> - **Title and Body Consistency**: Still uses "Limited Consent... and Motion," but the proposed order title now aligns better ("ORDER ON DEFENDANT’S LIMITED CONSENT..."). Minor remaining inconsistency is not a problem.
> 
> ### Remaining Minor Issues / Suggestions for Polish
> 1. **Title Consistency (Minor)**: 
>    - Main document title: "DEFENDANT’S LIMITED CONSENT TO PLAINTIFF’S MOTION FOR ACCEPTANCE OF OVERBID CALCULATION AND MOTION TO DIRECT IMMEDIATE DISBURSEMENT OF SURPLUS FUNDS"
>    - Proposed order: "ORDER ON DEFENDANT’S LIMITED CONSENT TO PLAINTIFF’S MOTION FOR ACCEPTANCE OF OVERBID CALCULATION AND MOTION TO DIRECT IMMEDIATE DISBURSEMENT OF SURPLUS FUNDS"
>    - Body sometimes refers to it as "Limited Consent and Motion." This is fine, but for ultimate neatness, you could standardize on one (e.g., add "Response," or just use "Limited Consent and Cross-Motion" if you prefer the prior phrasing). Not worth redoing.
> 
> 2. **Address in Signature Block**: You have the full address on page 2, but ensure the e-filing system and any attached appearance form reflect the current details accurately.
> 
> 3. **Verification**: Still not verified under penalty of perjury. For a response/motion with key factual statements (e.g., "to Defendant’s knowledge, no co-defendant has filed..." and your status as mortgage debtor), adding a short verification page or notarized affidavit can add credibility—especially since Marion County Clerk procedures for surplus often involve identity verification and affidavits before release. Not strictly required, but helpful.
> 
> 4. **Proposed Order Tweaks (Optional but Recommended)**:
>    - Consider adding a sentence in the findings: "No competing claimant has appeared or established a superior entitlement to the surplus funds." (This echoes your paragraph 4 and helps the court.)
>    - In the disbursement paragraph: "The Clerk shall immediately disburse surplus funds in the amount of **$7,521.37** to Defendant Cody Rice-Velasquez **upon verification of identity**." (Many clerks require this.)
>    - Fallback for deposit: The prior version had a good one ("If such funds have not yet been deposited... within __ days"). You could reinstate a short version if plaintiff hasn't deposited yet.
>    - Date line: Leave as-is for the judge.
> 
> 5. **Supporting Documentation**:
>    - No exhibits attached in this draft. If plaintiff's April 21 motion isn't already in the record or easily accessible via Odyssey/e-filing, consider attaching a copy as Exhibit A for context.
>    - Marion County may have a specific surplus claim form (common in many counties). Check with the Marion County Clerk's office (or their website) whether they require a separate "Claim to Surplus" form in addition to your motion. Some clerks prefer or require it for processing disbursement.
> 
> 6. **Local Practices**: 
>    - Indiana law (IC 32-30-10-14) clearly directs surplus to the **mortgage debtor** (you) unless the court directs otherwise based on adjudicated claims of others. Your filing correctly positions this.
>    - Post-sale surplus disputes are usually resolved on the papers if unopposed. Prompt filing (same day as your prior version) shows good diligence.
> 
> ### Overall Recommendation
> **This version is ready to file as-is.** It's an upgrade—more polished, with stronger protections and a better proposed order. The court should have an easy path to grant the relief without a hearing, assuming no other claimants appear.
> 
> **Next Steps After Filing**:
> - Monitor the case docket closely via Indiana's Odyssey system.
> - If no order within a week or two, you could file a simple "Request for Ruling" or "Motion to Set for Hearing."
> - Once the order is signed, follow up with the Clerk's office on disbursement procedures (they may require ID, W-9/tax forms, or an affidavit).
> - Keep all your reservations intact—they protect any separate claims (e.g., servicing issues, consumer law violations, credit reporting) you may pursue later.
> 
> This continues to reflect thoughtful drafting. Great job iterating on it. If you get a response from plaintiff, a court order, or want help drafting a follow-up (e.g., if they object), share it and I'll review. 
> 
> If the funds have already been deposited with the Clerk, disbursement should move quickly once the order enters. Good luck getting your surplus promptly!

### Assistant
> Updated in canvas.
> 
> I tightened the order, added the no-competing-claimant finding, added the deposit fallback, and swapped in the updated phone number.
