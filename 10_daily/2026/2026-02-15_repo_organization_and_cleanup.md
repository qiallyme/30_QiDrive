---
layout: page
title: "Repo Organization and Cleanup"
slug: "repo_organization_and_cleanup"
created_at: "2026-02-15 22:59:22"
updated_at: "2026-02-15 22:59:22"
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
date: 2026-02-15
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6992a410-3d58-8326-83ec-554bc66220ac"
canonical_ref: ""
---

# Repo Organization and Cleanup

## Overview
- **Date**: 2026-02-15 22:59:22
- **Conversation ID**: `6992a410-3d58-8326-83ec-554bc66220ac`
- **Source**: `Chat-Export-28513-2026/conversations-004.json`

## Chat History

### User
> give me a cursor prompt to finish oraganizing and cleaning up this repo to finish our next step and solidify where we are . ```markdown
> . 📂 content
> └── 📂 00_CASE_MASTER/
> │  ├── 📄 FCFCU_CASE_MASTER - 0_master.csv
> │  ├── 📄 Strategic_Plan.canvas
> │  ├── 📄 _Case_Summary.md
> └── 📂 01_PHASES/
> │  └── 📂 C-00_Foreclosure_Record/
> │    └── 📂 00.01_Record_Integrity/
> │      ├── 📄 Filing timestamp audit (service vs default timing).md
> │      ├── 📄 Master docket verification (all entries accounted for).md
> │      ├── 📄 Order sequence alignment (complaint → default → sale → writ).md
> │    └── 📂 00.02_Jurisdictional_Defects/
> │      ├── 📄 Service_Deficiency_Analysis.md
> │    └── 📂 00.03_Appellate_Preservation/
> │      ├── 📄 Appellate_Issue_Preservation.md
> │    ├── 📄 FCFCU_CASE_MASTER - 0_docket.csv
> │    ├── 📄 _PHASE_OVERVIEW.md
> │  └── 📂 C-01_Service_Notice_Defects/
> │    └── 📂 01.01_Service_Compliance_Audit/
> │    └── 📂 01.02_Notice_Failures/
> │    └── 📂 01.03_Legal_Impact_Assessment/
> │    ├── 📄 _PHASE_OVERVIEW.md
> │  └── 📂 C-02_Evidence_Preservation/
> │    └── 📂 02.01_Litigation_Hold_Control/
> │    └── 📂 02.02_Spoliation_Risk_Register/
> │      ├── 📄 20_Spoliation_Risk_Ledger.md
> │    └── 📂 02.03_Evidence_Intake_Log/
> │    ├── 📄 _PHASE_OVERVIEW.md
> │  └── 📂 C-03_Financial_Misconduct/
> │    └── 📂 03.01_Surplus_Forensics/
> │      ├── 📄 1️⃣ SURPLUS ACCOUNTING DEMAND LETTER.md
> │    └── 📂 03.02_Fee_Inflation_Audit/
> │      ├── 📄 FCFCU_Audit_Forensic_Discrepancies.canvas
> │    └── 📂 03.03_FCRA_Exposure_Link/
> │      ├── 📄 2️⃣ FCRA STATUTORY DAMAGES MODEL.md
> │      ├── 📄 30_Full_TriMerge_2025_12_tradelines.csv
> │      ├── 📄 Core_Credit_Tables.md
> │    └── 📂 03.04_Regulatory_Pressure/
> │      ├── 📄 3️⃣ REGULATOR-READY COMPLAINT PACKET.md
> │      └── 📂 CFPB/
> │        ├── 📄 01_Combined_Narrative_and_Excerpt.md
> │        ├── 📄 CFPB_Complaint_Draft.md
> │        ├── 📄 CFPB_Violation_Excerpt_Master.md
> │        ├── 📄 Cover_Letter.md
> │        ├── 📄 _CFPB.md
> │      └── 📂 CRAs/
> │        └── 📂 Equifax/
> │          ├── 📄 Equifax_Violation_Excerpt.md
> │          ├── 📄 _Equifax.md
> │        └── 📂 Experian/
> │          ├── 📄 Experian_Access_your_credit_report_2_tradelines.csv
> │          ├── 📄 Experian_Access_your_credit_report_CH13_tradelines.csv
> │          ├── 📄 Experian_Violation_Excerpt.md
> │          ├── 📄 _Experian.md
> │        └── 📂 Transunion/
> │          ├── 📄 TransUnion_Violation_Excerpt.md
> │          ├── 📄 _Transunion.md
> │        ├── 📄 _CRAs.md
> │      ├── 📄 City_of_Indy_Violation_Excerpt.md
> │      ├── 📄 Execution_Checklist.md
> │      ├── 📄 FORMAL NOTICE OF CONTINUING FCRA VIOLATIONS.md
> │      └── 📂 NCUA/
> │      ├── 📄 NCUA CONSUMER COMPLAINT – DRAFT.md
> │        ├── 📄 01_Combined_Narrative_and_Excerpt_2.md
> │        ├── 📄 Cover_Letter_6.md
> │        ├── 📄 Exhibit_Manifest_1.md
> │        ├── 📄 MANIFEST_NCUA_Complaint_Packet.md
> │        ├── 📄 _NCUA.md
> │      ├── 📄 NOTICE OF FAILURE TO REFLECT DISPUTED STATUS.md
> │      ├── 📄 PHASE_CREDIT_EXECUTION_MAP.md
> │      ├── 📄 Sanctions_Readiness_Memo.md
> │    ├── 📄 _20_CFPB.md
> │    ├── 📄 _20_furnisher_disputes.md
> │    ├── 📄 _30_NCUA.md
> │    ├── 📄 _30_bureau_disputes.md
> │    ├── 📄 _30_demand_letters.md
> │    ├── 📄 _BBB.md
> │    ├── 📄 _CREDIT_FCRA_MASTER.md
> │    ├── 📄 _PHASE_OVERVIEW.md
> │  └── 📂 C-04_Writ_Removal_Conduct/
> │    └── 📂 04.01_Writ_Execution_Validity/
> │    └── 📂 04.02_Property_Interference/
> │    └── 📂 04.03_State_Action_Analysis/
> │      ├── 📄 MANIFEST_Sheriff_Oversight_Packet.md
> │      ├── 📄 Marion_County_Sheriff_Oversight_Violation_Excerpt.md
> │      ├── 📄 Sheriff_Internal_Affairs_Complaint.md
> │      ├── 📄 Sheriff_Violation_Excerpt.md
> │    └── 📂 04.04_Post_Removal_Damages/
> │    ├── 📄 _20_AG_Indiana.md
> │    ├── 📄 _20_Habitability.md
> │    ├── 📄 _35_Sheriff_Oversight.md
> │    ├── 📄 _45_FCC_Telecom.md
> │    └── 📂 _LEGACY/
> │    ├── 📄 _PHASE_OVERVIEW.md
> │  └── 📂 C-05_Civil_Rights/
> │    └── 📂 05.01_ADA_Accommodation_Record/
> │      ├── 📄 99_Legacy_Excerpt_3.md
> │      ├── 📄 _C06_ADA.md
> │    └── 📂 05.02_Access_to_Court_Impact/
> │    └── 📂 05.03_Discriminatory_Impact_Assessment/
> │      ├── 📄 Cover_Letter_1.md
> │      ├── 📄 Cover_Letter_3.md
> │      ├── 📄 Cover_Letter_4.md
> │      ├── 📄 Cover_Letter_5.md
> │      ├── 📄 Cover_Letter_7.md
> │      ├── 📄 Cover_Letter_DOJ_Supplemental.md
> │      ├── 📄 DOJ_Civil_Rights_Violation_Excerpt.md
> │      ├── 📄 DOJ_Civil_Rights_Violation_Excerpt_Master.md
> │      ├── 📄 DOJ_Supplemental_Continuing_Harm.md
> │      ├── 📄 Exhibit_Manifest.md
> │      ├── 📄 HUD_FHEO_Complaint_Narrative.md
> │      ├── 📄 HUD_FHEO_Violation_Excerpt.md
> │      ├── 📄 IN_AG_Violation_Excerpt.md
> │      ├── 📄 IN_DFI_Violation_Excerpt.md
> │      ├── 📄 Indiana_AG_Complaint_Narrative.md
> │      ├── 📄 Indiana_Civil_Rights_Commission_Violation_Excerpt.md
> │      ├── 📄 Indiana_Civil_Rights_Complaint_Narrative.md
> │      ├── 📄 Indiana_DFI_Complaint_Narrative.md
> │      ├── 📄 Indiana_Department_of_Financial_Institutions_DFI_Violation_Excerpt.md
> │      ├── 📄 MANIFEST_HUD_FHEO_Complaint_Packet.md
> │      ├── 📄 MANIFEST_ICRC_Complaint_Packet.md
> │      ├── 📄 MANIFEST_IN_AG_Complaint_Packet.md
> │      ├── 📄 MANIFEST_Indiana_DFI_Packet.md
> │      ├── 📄 Violation_to_Regulator_Mapping.md
> │    ├── 📄 _25_IN_DFI.md
> │    ├── 📄 _40_DOJ_Civil_Rights.md
> │    ├── 📄 _50_HUD_FHEO.md
> │    ├── 📄 _55_IN_Civil_Rights.md
> │    └── 📂 _LEGACY/
> │      ├── 📄 99_Legacy_Excerpt_1.md
> │      └── 📂 C06_ADA/
> │      └── 📂 C08_Regulators/
> │      ├── 📄 Cover_Letter_2.md
> │    ├── 📄 _PHASE_OVERVIEW.md
> │  └── 📂 C-06_Settlement_Narrative_Control/
> │    └── 📂 06.01_Settlement_Framework/
> │    └── 📂 06.02_Negotiation_Tracking/
> │    └── 📂 06.03_Narrative_Discipline/
> │      ├── 📄 01_Combined_Narrative_and_Excerpt_1.md
> │      ├── 📄 20251215_displacement_cold_exposure.md
> │      ├── 📄 BBB_Violation_Excerpt.md
> │      ├── 📄 _C10_Narrative_Control.md
> │    ├── 📄 NT_Attorney_Intake_Summary.md
> │    └── 📂 _LEGACY/
> │      └── 📂 C10_Narrative_Control/
> │    ├── 📄 _PHASE_OVERVIEW.md
> │  ├── 📄 FCFCU_CASE_MASTER - 1_phases.csv
> │  ├── 📄 _PHASES_MASTER.md
> └── 📂 02_VIOLATIONS/
> │  ├── 📄 03_CASE_VIOLATIONS.md
> │  ├── 📄 FCFCU_CASE_MASTER - 2_violations.csv
> └── 📂 03_EVENTS/
> │  ├── 📄 02_TIMELINE.mw
> │  └── 📂 2021/
> │    ├── 📄 20210624_FCFCU_Signed_First_Mortgage_Note.md
> │  └── 📂 2022/
> │    ├── 📄 20220628_FCFCU_Signed_Second_Mortgage_Note.md
> │  └── 📂 2023/
> │    ├── 📄 2023-09-20_FCFCU_Hardship_and_Health_Notice_Let.md
> │    ├── 📄 20230920_FCFCU_Hardship_and_Health_Notice_Letter.md
> │    ├── 📄 20230921_FCFCU_Letter_Pre_Shipment.md
> │    ├── 📄 20230925_FCFCU_Letter_Delivered.md
> │  └── 📂 2024/
> │    ├── 📄 2024-12-09_Eviction_Case_MasterFile.md
> │    ├── 📄 20240320_FCFCU_Certified_Response_Tax_Records.md
> │    ├── 📄 20240621_FCFCU_Property_Appraisal.md
> │    ├── 📄 20240712_FCFCU_Mortgage_Payment_Record.md
> │    ├── 📄 20240913_FCFCU_Plaintiff_Claims_Default_Letter_Sent.md
> │    ├── 📄 20241119_FCFCU_Plaintiff_Claims_Amount_Due.md
> │    ├── 📄 20241204_FCFCU_Notice_of_Default_Right_to_Cure_Sent.md
> │    ├── 📄 20241204_FCFCU_Statement.md
> │    ├── 📄 20241209_FCFCU_Outgoing_Email_Bank_Access_Reques.md
> │    ├── 📄 20241211_FCFCU_Outgoing_Email_Bank_Access_Reques.md
> │  └── 📂 2025/
> │    ├── 📄 2025-01-16_Case_Filed.md
> │    ├── 📄 2025-03-05_Service_Attempt_1.md
> │    ├── 📄 2025-04-15_Service_Attempt_2.md
> │    ├── 📄 2025-05-13_Motion_for_Default_Judgment.md
> │    ├── 📄 2025-05-21_Order_Denying_Default_Judgment.md
> │    ├── 📄 2025-05-23_Amended_Motion_Default_Judgment.md
> │    ├── 📄 2025-05-28_Default_Judgment_Entered.md
> │    ├── 📄 2025-05-30_Praecipe_Sheriff_Sale.md
> │    ├── 📄 2025-07-09_Sheriff_Sale_Notice_Posted.md
> │    ├── 📄 2025-08-15_Sheriff_Sale.md
> │    ├── 📄 2025-10-29_Petition_for_Writ_of_Assistance.md
> │    ├── 📄 2025-11-06_Writ_of_Assistance_Issued.md
> │    ├── 📄 2025-12-09_Writ_Executed_Removal.md
> │    ├── 📄 2025-12-09_case_log.md
> │    ├── 📄 2025-12-10_Motions_Filed.md
> │    ├── 📄 2025-12-11_Court_Orders_and_Hearing_Scheduled.md
> │    ├── 📄 2025-12-12_Supplemental_Emergency_Motion.md
> │    ├── 📄 2025-12-15_displacement_cold_exposure.md
> │    ├── 📄 2025-12-16_AES_Emergency_Notice.md
> │    ├── 📄 2025-12-16_case_dna.md
> │    ├── 📄 2025-12-16_case_log.md
> │    ├── 📄 20250104_DEADLINE_Cure_Period_Expires.md
> │    ├── 📄 20250109_COURT_Orders_And_Hearing_Scheduled.md
> │    ├── 📄 20250109_COURT_Orders_Hearing_Scheduled.md
> │    ├── 📄 20250114_FCFCU_Plaintiff_Conducts_SCRA_Searches.md
> │    ├── 📄 20250115_COUNSEL_Felix_Rippy_Files_Appearance.md
> │    ├── 📄 20250115_FCFCU_Notice_of_Default_Sent.md
> │    ├── 📄 20250116_COURT_Summons_Issued.md
> │    ├── 📄 20250116_FCFCU_Case_Filed.md
> │    ├── 📄 20250116_FCFCU_Complaint_Filed.md
> │    ├── 📄 20250116_SHERIFF_SERVICE_Simultaneous_Delivery_Claim.md
> │    ├── 📄 20250305_SHERIFF_SERVICE_Return_Claimed.md
> │    ├── 📄 20250409_SERVICE_Attempt_2.md
> │    ├── 📄 20250409_SHERIFF_SERVICE_Attempt_Two.md
> │    ├── 📄 20250415_SHERIFF_Service_Return_Claimed.md
> │    ├── 📄 20250429_FCFCU_VP_Affidavit_Debt_Signed.md
> │    ├── 📄 20250501_CRA_CREDIT_EVENT_FCFCU_BALANCE_CHANGED.md
> │    ├── 📄 20250507_FCFCU_Flowers_Affidavit_Notarized.md
> │    ├── 📄 20250513_ATTORNEY_Files_Fee_Affidavit.md
> │    ├── 📄 20250513_COURT_Motion_Default_Judgment.md
> │    ├── 📄 20250513_COURT_Motion_For_Default_Judgment.md
> │    ├── 📄 20250521_COURT_Order_Denying_Default.md
> │    ├── 📄 20250521_COURT_Order_Denying_Default_Judgment.md
> │    ├── 📄 20250521_FCFCU_Plaintiff_Files_for_Default_Judgment.md
> │    ├── 📄 20250521_ORDER_Denying_Default.md
> │    ├── 📄 20250521_ORDER_Denying_Default_Judgment.md
> │    ├── 📄 20250523_COURT_Default_Judgment_Entered.md
> │    ├── 📄 20250523_COURT_document_Default_Judgment_Entered.md
> │    ├── 📄 20250523_FCFCU_Amended_Default_Judgment_Requested.md
> │    ├── 📄 20250523_FCFCU_Amended_Motion_Default_Judgment.md
> │    ├── 📄 20250528_COURT_Default_Judgment_Entered.md
> │    ├── 📄 20250528_COURT_Judgment_Entered.md
> │    ├── 📄 20250528_FCFCU_May28_FORECLOSURE.md
> │    ├── 📄 20250529_Praecipe_Sheriff_Sale_Filed.md
> │    ├── 📄 20250529_SHERIFF_Praecipe_Sale.md
> │    ├── 📄 20250529_SHERIFF_Praecipe_Sale_02.md
> │    ├── 📄 20250530_AES_ADA_Notice.md
> │    ├── 📄 20250530_AES_Ada_Notice_02.md
> │    ├── 📄 20250530_SHERIFF_Praecipe_Sale.md
> │    ├── 📄 20250601_CRA_REPORTING_EVENT_FCFCU_DUPLICATE_TRADELINE.md
> │    ├── 📄 20250601_CRA_REPORTING_EVENT_FCFCU_STATUS_CHANGED.md
> │    ├── 📄 20250601_CRA_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │    ├── 📄 20250601_CRA_REPORTING_VIOLATION_EVENT_FCFCU_INITIAL_FALSE_REPORTING.md
> │    ├── 📄 20250608_AES_ADA_Notice.md
> │    ├── 📄 20250613_Sheriff_Sale_Notice.md
> │    ├── 📄 20250613_Sheriff_Sale_Notice_Posted.md
> │    ├── 📄 20250701_CRA_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │    ├── 📄 20250706_FCFCU_Plaintiff_Claims_Notice_of_Sale.md
> │    ├── 📄 20250709_Sheriff_Sale_Notice_Claimed.md
> │    ├── 📄 20250717_FCFCU_Plaintiff_Places_Bid.md
> │    ├── 📄 20250801_CRA_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │    ├── 📄 20250805_FCFCU_Report_Sheriff_Sale_No_Excess.md
> │    ├── 📄 20250805_Sheriff_Sale_No_Excess.md
> │    ├── 📄 20250815_FCFCU_BILLING_Utility_Bill_AES_during_dispute.md
> │    ├── 📄 20250815_Sheriff_Sale.md
> │    ├── 📄 20250815_Sheriff_Sale_Occurs.md
> │    ├── 📄 20250815_Writ_Assistance_Issued.md
> │    ├── 📄 20250815_Writ_Of_Assistance_Issued.md
> │    ├── 📄 20250819_Sheriff_Deed_Signed.md
> │    ├── 📄 20250901_EVENT_CREDIT_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │    ├── 📄 20250909_Decree_Foreclosure_Returned.md
> │    ├── 📄 20250909_Judgment_Satisfied_Return_Filed.md
> │    ├── 📄 20251001_EVENT_CREDIT_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │    ├── 📄 20251029_Petition_For_Writ_Of_Assistance_log_ext_1.md
> │    ├── 📄 20251029_Petition_Writ_Assistance.md
> │    ├── 📄 20251029_Petition_for_Writ_of_Assistance.md
> │    ├── 📄 20251029_enforcement_Petition_For_Writ_Of_Assist.md
> │    ├── 📄 20251101_EVENT_CREDIT_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │    ├── 📄 20251106_Writ_of_Assistance_Granted.md
> │    ├── 📄 20251106_Writ_of_Assistance_Issued.md
> │    ├── 📄 20251126_Sheriff_Deputies_Arrive_Unrelated.md
> │    ├── 📄 20251201_December_ADA_.md
> │    ├── 📄 20251201_December_CONVERSION___NEGLIGENCE_.md
> │    ├── 📄 20251201_December_CONVERSION___PROPERTY_INTERFERENCE_.md
> │    ├── 📄 20251201_December_EVIDENCE_SPOLIATION_.md
> │    ├── 📄 20251201_December_PROCEDURAL_.md
> │    ├── 📄 20251201_December_SPOLIATION_OF_EVIDENCE_.md
> │    ├── 📄 20251201_EVENT_CREDIT_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │    ├── 📄 20251203_IMPD_Contact_Knocked_Then_Left.md
> │    ├── 📄 20251207_Retrieval_Day.md
> │    ├── 📄 20251209_0948_Sheriff_Arrival_Initial_Entry.md
> │    ├── 📄 20251209_1000_Active_Removal_Process.md
> │    ├── 📄 20251209_1016_Medical_Distress_Incident.md
> │    ├── 📄 20251209_1018_Officer_Interference_Property_Retr.md
> │    ├── 📄 20251209_1020_Room_Vacated.md
> │    ├── 📄 20251209_1209_Hallway_Activity.md
> │    ├── 📄 20251209_DISPLACEMENT_Emergency_Housing_Roaches_.md
> │    ├── 📄 20251209_ENFORCEMENT_Armed_removal_from_property.md
> │    ├── 📄 20251209_ENFORCEMENT_Writ_Executed__Forced_Removal.md
> │    ├── 📄 20251209_Removal_Day_Camera_Garage.md
> │    ├── 📄 20251209_Writ_Executed_Forced_Removal.md
> │    ├── 📄 20251209_Writ_Executed_Removal.md
> │    ├── 📄 20251209_Writ_Executed_Removal_migrated_1.md
> │    ├── 📄 20251210_EXPENSE_Essential_items_purchase.md
> │    ├── 📄 20251210_Financial_Tracker.md
> │    ├── 📄 20251210_Financial_Tracker_Update.md
> │    ├── 📄 20251210_Motions_Filed.md
> │    ├── 📄 20251210_PROCEDURAL_.md
> │    ├── 📄 20251210_document_Financial_Tracker.md
> │    ├── 📄 20251211_Court_Orders_and_Hearing_Scheduled.md
> │    ├── 📄 20251212_028_Report_Court_Defendant_Request.md
> │    ├── 📄 20251212_Attorney_Certifies_Document_Sent.md
> │    ├── 📄 20251212_Report_Defendant_Request.md
> │    ├── 📄 20251212_Supplemental_Emergency_Motion.md
> │    ├── 📄 20251212_document_028_Report_Court_Defendant_Req.md
> │    ├── 📄 20251215_Case_DNA_Strategy_Checkpoint.md
> │    ├── 📄 20251215_Case_DNA_Strategy_Checkpoint_log_ext_1.md
> │    ├── 📄 20251215_Case_DNA_Strategy_Checkpoint_log_ext_2.md
> │    ├── 📄 20251215_LOG_Consolidated_Forensic_Case_Log.md
> │    ├── 📄 20251215_Strategic_Planning_Session.md
> │    ├── 📄 20251215_TRAUMA_Sexual_coercion_incident.md
> │    ├── 📄 20251216_027_Supplemental_Motion_Access.md
> │    ├── 📄 20251216_ENFORCEMENT_Access_Denial_by_Susan_Abbett.md
> │    ├── 📄 20251216_ENFORCEMENT_Post_Removal_Access_Denial.md
> │    ├── 📄 20251216_Filing_Execution_Audit.md
> │    ├── 📄 20251216_Motion_Surplus_Funds.md
> │    ├── 📄 20251216_Procedural_Action_Filing_Execution_Documentation_Audit.md
> │    ├── 📄 20251216_Supplemental_Motion_Access.md
> │    ├── 📄 20251216_motion_027_Supplemental_Motion_Access.md
> │    ├── 📄 20251217_AES_Emergency_Notice.md
> │    ├── 📄 20251217_Notice_Surplus_Funds_Hearing.md
> │    ├── 📄 20251217_Report_No_Excess_Proceeds.md
> │    ├── 📄 20251217_document_Aes_Emergency_Notice.md
> │    ├── 📄 20251218_Automated_Notices_Issued.md
> │    ├── 📄 20251219_gigi_acute_anxiety_attack.md
> │    ├── 📄 20251221_ADA_Accommodation_Coordination.md
> │    ├── 📄 20251221_Afternoon_Evening_-_Post-Removal_Harms_Documentation.md
> │    ├── 📄 20251221_Camera_Unplugging_Discovery.md
> │    ├── 📄 20251221_Case_Consolidation.md
> │    ├── 📄 20251221_Case_Log.md
> │    ├── 📄 20251221_DISCOVERY_Discovery_of_Camera_and_Fridge_Disconnection.md
> │    ├── 📄 20251221_DISCOVERY_Property_Damage_Discovery.md
> │    ├── 📄 20251221_DISTRESS_Physical_and_Financial_Distress_during_Retrieval.md
> │    ├── 📄 20251221_DOJ_Civil_Rights_Complaint_Submitted.md
> │    ├── 📄 20251221_DOJ_Complaint_Submitted.md
> │    ├── 📄 20251221_Early_Morning_-_Gigi_Escape_Incident.md
> │    ├── 📄 20251221_Evening_-_Procedural_Coordination_ADA_Accommodation.md
> │    ├── 📄 20251221_Evening_-_Surveillance_Cameras_Guidance.md
> │    ├── 📄 20251221_Gigi_Escape_Incident.md
> │    ├── 📄 20251221_HOTEL_Hotel_Crisis_Deposit_Hold_Refusal.md
> │    ├── 📄 20251221_INCIDENT_Gigi_Service_Animal_Escape_Crisis.md
> │    ├── 📄 20251221_INCIDENT_Service_Animal_Escape.md
> │    ├── 📄 20251221_Morning_-_CameraRefrigerator_Unplugging_Discovery.md
> │    ├── 📄 20251221_Morning_-_Physical_Exhaustion_During_Access_Window.md
> │    ├── 📄 20251221_PROTOCOL_Property_Retrieval_Surveillance_Guidance.md
> │    ├── 📄 20251221_Physical_Exhaustion_Access.md
> │    ├── 📄 20251221_Post_Removal_Harms_Documentation.md
> │    ├── 📄 20251221_Surveillance_Cameras_Guidance.md
> │    ├── 📄 20251221_document_Case_Log.md
> │    ├── 📄 20251222_Court_Filing_History_Confirmed_and_Cross-Referenced.md
> │    ├── 📄 20251222_Court_Filing_History_Cross_Reference.md
> │    ├── 📄 20251222_Current_State_Snapshot.md
> │    ├── 📄 20251222_Declaration_Filed_Envelope_37416037.md
> │    ├── 📄 20251222_FINAL_STATUS_REPORT.md
> │    ├── 📄 20251222_Supplemental_Snapshot_Displacement_Relo.md
> │    ├── 📄 20251222_Today_Snapshot_Current_State.md
> │    ├── 📄 20251222_Vault_State_Sync.md
> │    ├── 📄 20251222_Vault_State_Sync_Documentation_Consolidation.md
> │  └── 📂 2026/
> │    ├── 📄 20260101_EVENT_CREDIT_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │    ├── 📄 20260102_GENERAL_.md
> │    ├── 📄 20260109_Felix_Rippy_Files_Late_Appearance.md
> │    ├── 📄 20260109_Supplemental_Emergency_Motion.md
> │    ├── 📄 20260109_motion_Supplemental_Emergency_Motion.md
> │    ├── 📄 20260118_COLLATERAL_DAMAGE_Zai_Asylum_Impact.md
> │    ├── 📄 20260118_DISPUTE_EasyTax_Crystal_Rodriguez_Dispute.md
> │    ├── 📄 20260118_FINANCIAL_LOSS_Lost_Tax_Season_Income.md
> │    ├── 📄 20260118_HOUSING_Otis_Emergency_Housing_Collapse.md
> │    ├── 📄 20260118_RELOCATION_Forced_Relocation_to_Evansville.md
> │    ├── 📄 20260118_RELOCATION_Relocation_to_Evansville.md
> │    ├── 📄 20260118_STRATEGY_Strategic_Context_Clarification_Session.md
> │    ├── 📄 20260127_FILING_CFPB_Complaint_Filing.md
> │    ├── 📄 20260127_FILING_Regulator_Filings_HUD_NCUA_DOJ_.md
> │    ├── 📄 20260201_EVENT_CREDIT_REPORTING_EVENT_FCFCU_BALANCE_CHANGED.md
> │    ├── 📄 20260201_EVENT_CREDIT_REPORTING_EVENT_FCFCU_DUPLICATE_TRADELINE.md
> │    ├── 📄 20260201_EVENT_CREDIT_REPORTING_EVENT_FCFCU_STATUS_CHANGED.md
> │    ├── 📄 20260201_cold_exposure.md
> │    ├── 📄 20260203_COMMUNICATION_Credit_Dispute_Package_Sent.md
> │    ├── 📄 20260203_COMMUNICATION_Evidence_Preservation_Packet_Sent.md
> │    ├── 📄 20260204_EVENT_CREDIT_REPORTING_EVENT_FCFCU_FALSE_REPORTING_AFTER_NOTICE.md
> │    ├── 📄 20260209_Case_Log_Entry
> │    ├── 📄 20260209_EVENT_CREDIT_REPORTING_EVENT_FCFCU_FALSE_REPORTING_AFTER_NOTICE.md
> │    ├── 📄 20260212_Session_Summary_2026-02-12_Tax_FCRA_Strategy_Update.md
> │  ├── 📄 FCFCU_CASE_MASTER - 3_events.csv
> │  ├── 📄 Timeline_Inventory.csv
> └── 📂 04_DOCUMENTS/
> │  ├── 📄 2026-02-02_Equifax_Dispute_Letter.html
> │  ├── 📄 2026-02-02_Experian_Dispute_Letter.html
> │  ├── 📄 2026-02-02_TransUnion_Dispute_Letter.html
> │  ├── 📄 2026-02-03_FCFCU_Furnisher_Deletion_Demand_FINAL.html
> │  ├── 📄 ADA_Disability_Affidavit.md
> │  ├── 📄 Credit_Dispute_Master_Packet_Index.html
> │  ├── 📄 Equifax_dispute_letter.html
> │  ├── 📄 FCFCU_CASE_MASTER - 4_docs.csv
> │  ├── 📄 Landlord_Explanation_Letter.html
> │  ├── 📄 Landlord_Statement.html
> │  ├── 📄 Ouput.txt
> │  ├── 📄 _05_OUTPUT.md
> │  ├── 📄 _10_Service_Animal_Notice.md
> │  ├── 📄 _50_output.md
> │  ├── 📄 _60_CMS_Caretaker_Impact.md
> │  ├── 📄 _65_SSA_OIG.md
> │  ├── 📄 _70_VA_Informational.md
> │  ├── 📄 _Advocate_Outreach_Message.md
> │  └── 📂 _drafts/
> │    ├── 📄 20260202_draft_housing_affidavit.html
> │    ├── 📄 20260203_draft_Equifax_Dispute_Letter.html
> │    └── 📂 Consumer_Statements/
> │      ├── 📄 Consumer_Statement_Landlords.md
> │      ├── 📄 Emergency_Credit_Harm_Addendum.md
> │      ├── 📄 _Consumer_Statements.md
> │    ├── 📄 Exhibit_N_001_DECLARATION_OF_CODY_RICE_VELASQUEZ.md
> │    ├── 📄 Formal_Retrieval_Protocol_ADA.md
> │    ├── 📄 NOTICE OF INTENT TO PURSUE FURTHER ACTION.md
> │    ├── 📄 __drafts.md
> │  ├── 📄 _settlement_letter_draft.md
> │  ├── 📄 a0.01.001_one_page_case_summary.html
> │  ├── 📄 a0.01.002_hearing_scope_and_relief.html
> │  ├── 📄 ada_disability_affidavit.html
> │  ├── 📄 ada_packet.html
> │  ├── 📄 affidavit_not_served.html
> │  └── 📂 analysis/
> │    └── 📂 00_Strategy/
> │      ├── 📄 20260201_STRATEGY_Auto_Save_D0015.canvas
> │      ├── 📄 20260201_STRATEGY_Auto_Save_D0016.canvas
> │      ├── 📄 20260207_STRATEGY_Auto_Save_D0009.canvas
> │      ├── 📄 20260207_STRATEGY_Auto_Save_D0010.canvas
> │      ├── 📄 20260207_STRATEGY_Auto_Save_D0012.canvas
> │      ├── 📄 20260207_STRATEGY_Auto_Save_D0013.canvas
> │      ├── 📄 20260207_STRATEGY_Auto_Save_D0134.canvas
> │      ├── 📄 20260207_STRATEGY_Auto_Save_D0152.canvas
> │      ├── 📄 20260207_STRATEGY_Auto_Save_D0153.canvas
> │      ├── 📄 _00_Strategy.md
> │    ├── 📄 20260210_DATA_FCFCU_Case_Master_GS1.csv
> │    ├── 📄 20260210_REPORT_AI_Analysis_Grok_2.pdf
> │    ├── 📄 20260212_NOTES_Dictated_Case_Review.txt
> │    ├── 📄 _analysis.md
> │  ├── 📄 attorney_brief.html
> │  ├── 📄 b1.01.001_core_issue_statement.html
> │  ├── 📄 b1.01.002_trial_rule_4_1_b_standard.html
> │  ├── 📄 b1.01.003_void_vs_voidable_case_law.html
> │  ├── 📄 c2.03.004_odyssey_envelope_receipt.html
> │  ├── 📄 case-narrative-wrongful-foreclosure-and-displ.html
> │  ├── 📄 case_conversation_log.html
> │  ├── 📄 character_affidavit.html
> │  ├── 📄 cms_ssa_caretaker.html
> │  ├── 📄 cold_risk_report.html
> │  ├── 📄 credibility_affidavit.html
> │  ├── 📄 crisis_the_anatomy_of_institutional_failure.html
> │  ├── 📄 dfi_servicing_complaint.html
> │  ├── 📄 docs.md
> │  ├── 📄 doj_supplemental.html
> │  ├── 📄 donations_context.html
> │  ├── 📄 dump_tree_with_ocr.py
> │  ├── 📄 emergency_filing_packet.html
> │  ├── 📄 equifax.html
> │  └── 📂 exhibits/
> │    ├── 📄 _exhibits.md
> │  ├── 📄 fcc_harassment.html
> │  ├── 📄 fcfcu_v_cr-v_report_to_court.html
> │  ├── 📄 file-tree-content.html
> │  └── 📂 filings/
> │    ├── 📄 _filings.md
> │  ├── 📄 gender_identity_clarification.html
> │  ├── 📄 hud_fheo_narrative.html
> │  ├── 📄 i8.02.001_research_and_notes.html
> │  ├── 📄 i8.99.999_internal_do_not_print.html
> │  ├── 📄 icrc_civil_rights.html
> │  ├── 📄 legal-memorandum.html
> │  └── 📂 letters/
> │    ├── 📄 _letters.md
> │  ├── 📄 long_term_payout_strategy.html
> │  ├── 📄 master_strategic_timeline.html
> │  ├── 📄 master_timeline.html
> │  ├── 📄 master_violation_inventory.html
> │  ├── 📄 migration_notes.html
> │  ├── 📄 ncua_complaint.html
> │  ├── 📄 observations_affidavit.html
> │  ├── 📄 odyssey_envelope_receipt.html
> │  └── 📂 orders/
> │    ├── 📄 _orders.md
> │  └── 📂 packets/
> │    ├── 📄 HEARING_Cheat_Sheet.md
> │    ├── 📄 _packets.md
> │  ├── 📄 procedural_failure_map_one_pager.html
> │  ├── 📄 proposal-for-strategic-reports-in-the-matter-.html
> │  ├── 📄 public_statement.html
> │  ├── 📄 receipt_usps_tracking.html
> │  ├── 📄 report_to_court_on_defendants_request.html
> │  ├── 📄 sheriff_internal_affairs.html
> │  ├── 📄 strategic_plan.html
> │  ├── 📄 talking_points.html
> │  ├── 📄 timeline_canvas.html
> │  ├── 📄 transunion.html
> │  ├── 📄 updated_affidavit_language.html
> │  ├── 📄 va_informational.html
> │  ├── 📄 verified_affidavit_of_defendant.html
> │  ├── 📄 void_judgment_eviction_crisis.html
> └── 📂 05_DISPUTES/
> │  ├── 📄 00_COMPLAINT_PACKET_CHECKLIST.md
> │  ├── 📄 FCFCU_CASE_MASTER - 5_disputes.csv
> │  ├── 📄 Ledger.txt
> │  ├── 📄 _04_LEDGER.md
> │  └── 📂 audits/
> │    └── 📂 20260212_FCFCU_Accounting_Audit_Report/
> │      └── 📂 02_Source_Documents/
> │        ├── 📄 _02_Source_Documents.md
> │      ├── 📄 20260212_FCFCU_Accounting_Audit_Report.md
> │      ├── 📄 NT_Forensic_Accounting_Audit_Summary.md
> │      ├── 📄 _20260212_FCFCU_Accounting_Audit_Report.md
> │    ├── 📄 _audits.md
> │    └── 📂 fcfcu_gsheets/
> │      ├── 📄 FCFCU_CASE_MASTER.gsheet
> │      ├── 📄 _fcfcu_gsheets.md
> │  ├── 📄 dump_tree_with_ocr.py
> │  └── 📂 harm_damages/
> │    ├── 📄 99_Legacy_Excerpt.md
> │    ├── 📄 _harm_damages.md
> │  └── 📂 service/
> │    ├── 📄 _service.md
> │  └── 📂 task_spine/
> │    ├── 📄 _task_spine.md
> │    ├── 📄 task_export.csv
> │    ├── 📄 task_export_backup.csv
> │  └── 📂 violations/
> │    ├── 📄 _violations.md
> │    ├── 📄 violations_UPDATED.csv
> └── 📂 06_DAMAGES/
> │  ├── 📄 04_CASE_VALUATION.md
> │  ├── 📄 FCFCU_CASE_MASTER - 6_damages.csv
> │  ├── 📄 _20_ledgers.md
> │  ├── 📄 _30_Trackers.md
> └── 📂 07_ACTORS/
> │  ├── 📄 FCFCU_CASE_MASTER - 7_actors.csv
> └── 📂 08_ENTITIES/
> └── 📂 90_ADMIN/
> │  ├── 📄 _00_ADMIN.md
> │  └── 📂 _intake/
> │    ├── 📄 AES_Utility_Violation_Excerpt.md
> │    ├── 📄 B1.00.000_SECTION_COVER.md
> │    ├── 📄 B1.01.001_CORE_ISSUE_STATEMENT.md
> │    ├── 📄 B1.01.002_TRIAL_RULE_4_1_B_STANDARD.md
> │    ├── 📄 B1.01.003_VOID_VS_VOIDABLE_CASE_LAW.md
> │    ├── 📄 BBB_Complaint_Narrative.md
> │    ├── 📄 BBB_Violation_Excerpt.md
> │    ├── 📄 C2.00.000_SECTION_COVER.md
> │    ├── 📄 C2.01.001_MOTION_TO_VACATE_VOID_JUDGMENT.md
> │    ├── 📄 C2.02.001_EMERGENCY_MOTION_STAY_OR_QUASH.md
> │    ├── 📄 C2.03.001_SUPPLEMENTAL_EMERGENCY_MOTION.md
> │    ├── 📄 C2.04.001_PROPOSED_ORDER_VACATE.md
> │    ├── 📄 C2.04.002_PROPOSED_ORDER_STAY_WRIT.md
> │    ├── 📄 CFPB_Complaint_Draft.md
> │    ├── 📄 CFPB_Complaint_Narrative.md
> │    ├── 📄 CFPB_Escalation_Packet_DRAFT.md
> │    ├── 📄 CFPB_Violation_Excerpt.md
> │    ├── 📄 CFPB_Violation_Excerpt_Master.md
> │    ├── 📄 CMS_Informational_Complaint.md
> │    ├── 📄 Case Narrative - Wrongful Foreclosure and Displ.md
> │    ├── 📄 Case update.md
> │    ├── 📄 Case_Log.md
> │    ├── 📄 Character_Affidavit.md
> │    ├── 📄 Citizens_Utility_Violation_Excerpt.md
> │    ├── 📄 City_of_Indy_Violation_Excerpt.md
> │    ├── 📄 Cold_Risk_Report.md
> │    ├── 📄 Community_Service_Affidavit.md
> │    ├── 📄 Consumer_Statement_Landlords.md
> │    ├── 📄 Contacts.md
> │    ├── 📄 Cover_Letter.md
> │    ├── 📄 Cover_Letter_DOJ_Supplemental.md
> │    ├── 📄 Credibility_Affidavit.md
> │    ├── 📄 D3.00.000_SECTION_COVER.md
> │    ├── 📄 D3.03.001_SERVICE_DEFECT_ANALYSIS.md
> │    ├── 📄 DOJ_Civil_Rights_Violation_Excerpt.md
> │    ├── 📄 DOJ_Civil_Rights_Violation_Excerpt_Master.md
> │    ├── 📄 DOJ_Supplemental_Continuing_Harm.md
> │    ├── 📄 DOJ_Violation_Excerpt.md
> │    ├── 📄 Declaration_Secondary_Displacement_Otis.md
> │    ├── 📄 Demand_Notice_and_Ledger.md
> │    ├── 📄 Donations_Context.md
> │    ├── 📄 E4.05.001_PROCEDURAL_CHAIN_SUMMARY.md
> │    ├── 📄 EMERGENCY_FILING_PACKET.md
> │    ├── 📄 EXPOSURE_CONSEQUENTIAL_CONSOLIDATED.md
> │    ├── 📄 EXPOSURE_ECONOMIC_CONSOLIDATED.md
> │    ├── 📄 EXPOSURE_MISC_STRATEGY_CONSOLIDATED.md
> │    ├── 📄 EXPOSURE_NON_ECONOMIC_CONSOLIDATED.md
> │    ├── 📄 Emergency_Supplemental_Declaration_Consolidated.md
> │    ├── 📄 Equifax_Dispute_Letter.md
> │    ├── 📄 Equifax_Violation_Excerpt.md
> │    ├── 📄 Evidence_Log.md
> │    ├── 📄 Exhibit X — Inventory of Jurisdictional, Execut.md
> │    ├── 📄 Exhibit_Manifest.md
> │    ├── 📄 Experian_Dispute_Letter.md
> │    ├── 📄 Experian_Violation_Excerpt.md
> │    ├── 📄 F5.00.000_SECTION_COVER.md
> │    ├── 📄 F5.01.001_AFFIDAVIT_NOT_SERVED.md
> │    ├── 📄 F5.02.001_DECLARATION_ONGOING_HARM.md
> │    ├── 📄 F5.03.001_CREDIBILITY_DECLARATION.md
> │    ├── 📄 FCC_Harassment_Complaint.md
> │    ├── 📄 FCC_Violation_Excerpt.md
> │    ├── 📄 FCFCU_Late_Reporting_Evidence_2026.txt
> │    ├── 📄 FINANCIAL CENTER 01012017-02122026.txt
> │    ├── 📄 Financial_Tracker.md
> │    ├── 📄 Foreclosure Irregularities and Forensic Accounting.md
> │    ├── 📄 G6.03.001_ADA_IMPACT_SUMMARY.md
> │    ├── 📄 Gender_Identity_Clarification.md
> │    ├── 📄 Gigi_Documentation_Pack.md
> │    ├── 📄 Gigi_Service_Dog_Training_Manual.md
> │    ├── 📄 HUD_FHEO_Complaint_Narrative.md
> │    ├── 📄 HUD_FHEO_Violation_Excerpt.md
> │    ├── 📄 HUD_Violation_Excerpt_OLD.md
> │    ├── 📄 I8.02.001_RESEARCH_AND_NOTES.md
> │    ├── 📄 I8.99.999_INTERNAL_DO_NOT_PRINT.md
> │    ├── 📄 I8_01_000_CASE_SUMMARY.md
> │    ├── 📄 ICRC_Violation_Excerpt.md
> │    ├── 📄 INTERNAL VALUATION MEMO.md
> │    ├── 📄 IN_AG_Violation_Excerpt.md
> │    ├── 📄 IN_DFI_Violation_Excerpt.md
> │    ├── 📄 Indiana_AG_Complaint_Narrative.md
> │    ├── 📄 Indiana_Civil_Rights_Commission_Violation_Excerpt.md
> │    ├── 📄 Indiana_Civil_Rights_Complaint_Narrative.md
> │    ├── 📄 Indiana_DFI_Complaint_Narrative.md
> │    ├── 📄 Indiana_Department_of_Financial_Institutions_DFI_Violation_Excerpt.md
> │    ├── 📄 J9.01.001_COURT_SET_MASTER.md
> │    ├── 📄 J9.01.002_PERSONAL_MASTER.md
> │    ├── 📄 J9.01.003_OPPOSITION_SET_MASTER.md
> │    ├── 📄 J9.01.004_INTERNAL_RED_MASTER.md
> │    ├── 📄 LEGAL MEMORANDUM.md
> │    ├── 📄 Litigation_Decision_Tree.md
> │    ├── 📄 Long_Term_Payout_Strategy.md
> │    ├── 📄 MANIFEST_Credit_Bureau_Dispute_Packet.md
> │    ├── 📄 MANIFEST_HUD_FHEO_Complaint_Packet.md
> │    ├── 📄 MANIFEST_ICRC_Complaint_Packet.md
> │    ├── 📄 MANIFEST_IN_AG_Complaint_Packet.md
> │    ├── 📄 MANIFEST_Indiana_DFI_Packet.md
> │    ├── 📄 MANIFEST_NCUA_Complaint_Packet.md
> │    ├── 📄 MANIFEST_PHASE_03_SENDS.md
> │    ├── 📄 MANIFEST_Reserve_Informational_Filings.md
> │    ├── 📄 MANIFEST_Sheriff_Oversight_Packet.md
> │    ├── 📄 MITIGATION_LOG_Temporary_Housing.md
> │    ├── 📄 Marion_County_Sheriff_Oversight_Violation_Excerpt.md
> │    ├── 📄 Master_Timeline.md
> │    ├── 📄 Master_Timeline_Strategy_Summary.md
> │    ├── 📄 Motions.md
> │    ├── 📄 NCUA_Complaint_Narrative.md
> │    ├── 📄 NCUA_Complaint_Narrative_draft_old.md
> │    ├── 📄 NCUA_Violation_Excerpt.md
> │    ├── 📄 NT_2025-12-21_Gigi_Escape_Displacement_Safety_Event.md
> │    ├── 📄 NT_Attorney_Intake_Packet_Executive.md
> │    ├── 📄 NT_Attorney_Intake_Summary.md
> │    ├── 📄 NT_Damages_Matrix_Ab_Initio.md
> │    ├── 📄 NT_Demand_Ready_Exposure_Summary.md
> │    ├── 📄 NT_Financial_Tracker.md
> │    ├── 📄 NT_Forced_Relocation_Market_Loss_Memo.md
> │    ├── 📄 NT_Forensic_Accounting_Audit_Summary.md
> │    ├── 📄 NT_INTERNAL VALUATION MEMO.md
> │    ├── 📄 NT_Monetary_Exposure_Estimate.md
> │    ├── 📄 NT_Payment_Portal_and_Check_History.md
> │    ├── 📄 NT_Post_Removal_Artifact_Checklist.md
> │    ├── 📄 NT_Procedural_failure_map_one_pager.md
> │    ├── 📄 NT_Quarantined_Claims_Hold.md
> │    ├── 📄 NT_Violation_Remedy_Inventory.md
> │    ├── 📄 Notice_of_Evidence_Preservation.md
> │    ├── 📄 Observations_Affidavit.md
> │    ├── 📄 PHASE_04_Regulators.md
> │    ├── 📄 PHASE_05_Litigation.md
> │    ├── 📄 Phase_01_5_Preservation_Packet_Cover_Sheet.md
> │    ├── 📄 Premonitions_I_Knew_Before_I_Knew.md
> │    ├── 📄 Procedural_failure_map_one_pager.md
> │    ├── 📄 Proposal for Strategic Reports in the Matter of.md
> │    ├── 📄 Proposed_Order_Vacate.docx
> │    ├── 📄 Proposed_Orders.md
> │    ├── 📄 QiCase-FCFCU_Financial_Tracker.xlsx
> │    ├── 📄 README.md
> │    ├── 📄 README_supporting.md
> │    ├── 📄 Raw_Exhibit_Map.md
> │    ├── 📄 Room_Conditions_Factual_Log.md
> │    ├── 📄 SSA_OIG_Informational_Filing.md
> │    ├── 📄 Sanctions_Readiness_Memo.md
> │    ├── 📄 Session_Summary_2025-12-15_i_knew_before_i_knew.md
> │    ├── 📄 Settlement_Strategy_and_Contingency_Plan.md
> │    ├── 📄 Sheriff_Internal_Affairs_Complaint.md
> │    ├── 📄 Sheriff_Violation_Excerpt.md
> │    ├── 📄 Supplemental_Declaration_Accounting_Surplus.md
> │    ├── 📄 Supplemental_Declaration_Cody_DRAFT.md
> │    ├── 📄 TEMPLATE_COURT_DOC.md
> │    ├── 📄 TEMPLATE_EXHIBIT_LABEL.md
> │    ├── 📄 TEMPLATE_HANDUP_PACKET_NOTE.md
> │    ├── 📄 TEMPLATE_SECTION_COVER.md
> │    ├── 📄 TEMPLATE_SECTION_INDEX.md
> │    ├── 📄 TEMPLATE_WAR_NOTE.md
> │    ├── 📄 Talking_Points.md
> │    ├── 📄 TransUnion_Violation_Excerpt.md
> │    ├── 📄 VA_Informational_Filing.md
> │    ├── 📄 Violation_to_Regulator_Mapping.md
> │    ├── 📄 ada_packet.md
> │    ├── 📄 affidavit_not_served.docx
> │    ├── 📄 affidavit_not_served.md
> │    ├── 📄 arch.010__add_frontmatter.py
> │    ├── 📄 arch.010__build_indexes.py
> │    ├── 📄 arch.010__case_brain_full_pipeline.py
> │    ├── 📄 arch.010__case_brain_pipeline.py
> │    ├── 📄 arch.010__check_orphans_and_create_indexes.py
> │    ├── 📄 arch.010__compress_pdfs.py
> │    ├── 📄 arch.010__compress_pdfs_inplace.py
> │    ├── 📄 arch.010__convert_all_txt_to_md.py
> │    ├── 📄 arch.010__convert_to_markdown.py
> │    ├── 📄 arch.010__fix_duplicate_frontmatter.py
> │    ├── 📄 arch.010__link_timeline_events.py
> │    ├── 📄 arch.010__move_opposing_filings.py
> │    ├── 📄 arch.010__optimize_pdfs_pikepdf.py
> │    ├── 📄 arch.010__rename_evidence_files.ps1
> │    ├── 📄 arch.010__update_brain.ps1
> │    ├── 📄 attorney_brief.md
> │    ├── 📄 audit_fcfcu.py
> │    ├── 📄 audit_report.txt
> │    ├── 📄 authority.csv
> │    ├── 📄 b5f0f109bc88052d4000.woff2
> │    ├── 📄 c8ba52b05a9ef10f4758.woff2
> │    ├── 📄 cb10ffd7684cd9836a05.woff2
> │    ├── 📄 cbe0ae49c52c920fd563.woff2
> │    ├── 📄 create_masters.py
> │    └── 📂 docs/
> │      ├── 📄 009_Summons_4.pdf
> │      ├── 📄 010_Summons_5.pdf
> │      ├── 📄 014_Affidavit.pdf
> │      ├── 📄 018_Omitted_Notice_of_Service.pdf
> │      ├── 📄 023_Decree_Foreclosure_Returned.pdf
> │      ├── 📄 024_Petition_Writ_of_Assistance.pdf
> │      ├── 📄 025_Motion_Vacate_Stay_Writ.pdf
> │      ├── 📄 026_Exhibit_List_A-G.pdf
> │      ├── 📄 027_Supplemental_Motion_Access.pdf
> │      ├── 📄 028_Report_Court_Defendant_Request.pdf
> │      ├── 📄 029_Emergency_Supplemental_Declaration.pdf
> │      ├── 📄 030_Report_Sheriff_Sale_No_Excess.pdf
> │      ├── 📄 031_Proposed_Order_Vacate.pdf
> │      ├── 📄 032_Proposed_Order_Stay.pdf
> │      ├── 📄 033_ADA_Disability_Affidavit.pdf
> │      ├── 📄 0809b8fd-4b31-4ac4-a5f5-561da006d165.pdf
> │      ├── 📄 13312381_invoice.pdf
> │      ├── 📄 13312381_tmp.pdf
> │      ├── 📄 13312462_invoice.pdf
> │      ├── 📄 13312462_tmp.pdf
> │      ├── 📄 13312465_invoice.pdf
> │      ├── 📄 13312465_tmp.pdf
> │      ├── 📄 13348806_tmp.pdf
> │      ├── 📄 13383977_invoice.pdf
> │      ├── 📄 13383977_tmp.pdf
> │      ├── 📄 15c873fa-5cfd-4980-be43-dd077effeb2b.pdf
> │      ├── 📄 1990-05-18_FORMAL DISPUTE OF INACCURATE REPORTING Copy.pdf
> │      ├── 📄 2023-09-20_Notice_Disabilities_Hardship.pdf
> │      ├── 📄 2024-12-09_outgoing_email_bank_access_request.pdf
> │      ├── 📄 2024-12-11_outgoing_email_bank_access_request.pdf
> │      ├── 📄 2024-20-03_Response_to_tax_notice.pdf
> │      ├── 📄 20241204_FCFCU_Statement.pdf
> │      ├── 📄 2025-06-08_AES_ADA_Notice.pdf
> │      ├── 📄 2025-12-21_Exhibit_V-03-02_DECLARATION RE PRIOR LAW ENFORCEMENT CONTACTS, AUDIBILITY LIMITATIONS, AND SAFETY CONTEXT_crice4485@gmail.com.pdf
> │      ├── 📄 2025-12-21_ForensicAudit_FCFCU.pdf
> │      ├── 📄 2025-12-22_DOJ_Civil_Rights_Report_688619-FXN.pdf
> │      ├── 📄 2025_01_16_09_16_24.pdf.pdf
> │      ├── 📄 2025_05_13_14_52_56.pdf.pdf
> │      ├── 📄 2025_05_13_14_54_31.pdf.pdf
> │      ├── 📄 2025_05_13_14_55_22.pdf.pdf
> │      ├── 📄 2025_05_21_14_25_43.pdf.pdf
> │      ├── 📄 2025_05_23_11_06_25.pdf.pdf
> │      ├── 📄 2025_05_23_11_07_23.pdf.pdf
> │      ├── 📄 2025_05_29_14_15_32.pdf.pdf
> │      ├── 📄 2025_05_29_14_15_54.pdf.pdf
> │      ├── 📄 2026-02-03_BASIS OF DISPUTE (NON-CURABLE DEFECTS).pdf
> │      ├── 📄 21June-24-4817Shadow_Appraisal.pdf
> │      ├── 📄 50100846854.pdf
> │      ├── 📄 50100879809.pdf
> │      ├── 📄 50100883027.pdf
> │      ├── 📄 50100916138.pdf
> │      ├── 📄 5bf7e045-828d-4cac-8a3f-fc3b31439649.pdf
> │      ├── 📄 67e9f7c4-a021-441d-b1ce-ba3e7a034b8e.pdf
> │      ├── 📄 7dba97cb-da59-4f70-9e9e-6a7f9b300c07.pdf
> │      ├── 📄 8b2ae2d6-b47c-4086-bb36-675c455c1c72.pdf
> │      ├── 📄 9214890142980444614178.pdf
> │      ├── 📄 9214890142980444614581.pdf
> │      ├── 📄 9214890142980444614741.pdf
> │      ├── 📄 C2.01.002_motion_vacate.pdf
> │      ├── 📄 C2.01.003_Exhibit_List.pdf
> │      ├── 📄 C2.01.004_Exhibits_Combined.pdf
> │      ├── 📄 C2.02.002_Emergency_Motion_Stay_OR_Quash.pdf
> │      ├── 📄 C2.03.004_Odyssey_Envelope_Receipt.pdf
> │      ├── 📄 C2.03.005_COMBINED_SOURCE.pdf
> │      ├── 📄 C2.04.001_order_vacate_proposed.pdf
> │      ├── 📄 C2.04.002_order_stay_writ_proposed.pdf
> │      ├── 📄 CPR certification (1).pdf
> │      ├── 📄 Call Customer Care.pdf
> │      ├── 📄 Chase Credit Journey - Credit report.pdf
> │      ├── 📄 Chase Credit Journey.pdf
> │      ├── 📄 Credit Report.pdf
> │      ├── 📄 Crisis_The_Anatomy_of_Institutional_Failure.pdf
> │      ├── 📄 DLGF_ Tax Bill Search.pdf
> │      ├── 📄 Emergency Motions.gdoc
> │      ├── 📄 Exhibit X — Inventory of Jurisdictional, Execution, and Civil Rights Violations.pdf
> │      ├── 📄 Exhibit_G1_ADA_Notice_Request.pdf
> │      ├── 📄 Exhibit_H_Declaration.pdf
> │      ├── 📄 Experian - Access your credit report-CH13.pdf
> │      ├── 📄 Experian - Access your credit report.pdf
> │      ├── 📄 Experian - Dispute Cart.pdf
> │      ├── 📄 Experian - Dispute Cart2.pdf
> │      ├── 📄 FCFCU_v_CR-V_Report_to_Court.pdf
> │      ├── 📄 FORMAL_SURPLUS_DEMAND_CAUSE_NO_49D03-2501-MF-002559_Sheriff_Sale_Date_08-15-2025.pdf
> │      ├── 📄 G6.01.001_ADA_NOTICE.pdf
> │      ├── 📄 Gmail - Dispute Received, Investigation in Process.pdf
> │      ├── 📄 Gmail - Follow-Up Courtesy Notice – Demand for Deletion of FCFCU Tradelines (Acct. 661563L____).pdf
> │      ├── 📄 Gmail - Surplus Demand – Sheriff Sale August 15, 2025.pdf
> │      ├── 📄 H7.01.0006_EXHIBIT_F_AFFIDAVIT.pdf
> │      ├── 📄 H7.01.0008_EXHIBIT_G2_AES_ADA_DOCUMENTS.pdf
> │      ├── 📄 I8_01_001_Complaint.pdf
> │      ├── 📄 I8_01_002_Appearance.pdf
> │      ├── 📄 I8_01_004_Notice_to_Homeowners.pdf
> │      ├── 📄 I8_01_005_Appearance_2.pdf
> │      ├── 📄 I8_01_006_Summons_1.pdf
> │      ├── 📄 I8_01_007_Summons_2.pdf
> │      ├── 📄 I8_01_008_Summons_3.pdf
> │      ├── 📄 Indy.gov_ Pay Your Property Taxes.pdf
> │      ├── 📄 Invoice.pdf
> │      ├── 📄 Invoice2.pdf
> │      ├── 📄 Invoice3.pdf
> │      ├── 📄 Invoice4.pdf
> │      ├── 📄 Marion County, IN, Estimated 2025 Taxes 6016506.pdf
> │      ├── 📄 Missing Evidence and Vanishing Foreclosure Surplus.pdf
> │      ├── 📄 My Account - Credit Card Receipt - LetterStream.pdf
> │      ├── 📄 MyTitle.pdf
> │      ├── 📄 Odyssey_Envelope_Receipt.pdf
> │      ├── 📄 Orientation_and_Onboardin_signed_pages_Copy.pdf
> │      ├── 📄 PART 2 — EMERGENCY MOTION TO STAY WRIT.gdoc
> │      ├── 📄 PART 3 — UPDATED AFFIDAVIT.gdoc
> │      ├── 📄 PROOF_OF_ADDRESS.pdf
> │      ├── 📄 Parcel_6016506_PRC.pdf
> │      ├── 📄 Parcel_6016506_ParcelDetailHistory.pdf
> │      ├── 📄 RAYS CONSTRUCTION.pdf
> │      ├── 📄 REPORT_TO_COURT_ON_DEFENDANTS_REQUEST.pdf
> │      ├── 📄 Search Results.pdf
> │      ├── 📄 Service_Returned_Served.pdf
> │      ├── 📄 Service_Returned_Served_(1).pdf
> │      ├── 📄 Summary_-_MyCase.pdf
> │      ├── 📄 Supplemental_Emergency_Motion.pdf
> │      ├── 📄 Wrongful_Foreclosure_A_Case_Study_in_Civil_Rig.pdf
> │      ├── 📄 Your accounts _ Credit Karma.pdf
> │      ├── 📄 Zoho One - Subscription Renewal - Final Reminder!.pdf
> │      ├── 📄 b16d8fad-1b70-4865-8403-71c7a3117b53.pdf
> │      ├── 📄 cody_rice_velasquez-fullstack (1).pdf
> │      ├── 📄 combinepdf.pdf
> │      ├── 📄 dfadadf.pdf
> │      ├── 📄 dfafa.pdf
> │      ├── 📄 dfafdsasdf.pdf
> │      ├── 📄 dfasdfadsffafaf.pdf
> │      ├── 📄 direct-deposit-form-CASHAPP.PDF
> │      ├── 📄 e-filing-efsp-comparison.pdf
> │      ├── 📄 efiling-user-guide.pdf
> │      ├── 📄 f588fab6-f89f-41c3-bfce-05ad0d108a06.pdf
> │      ├── 📄 formal_surplus_demand_certified.pdf
> │      ├── 📄 formal_surplus_demand_certified_counsel.pdf
> │      ├── 📄 id-card (3).pdf
> │      ├── 📄 identity_verification_letter_mission-lane-cc.pdf
> │      ├── 📄 indy_pvdnet_document.pdf
> │      ├── 📄 parcel_6016506_parceldetailhistory_3.pdf
> │      ├── 📄 parcel_6016506_prc_3.pdf
> │      ├── 📄 rttet.pdf
> │      ├── 📄 vehicle-insurance-id-card.pdf
> │      ├── 📄 void_judgment_eviction_crisis.pdf
> │      ├── 📄 wertwewtwtwt.pdf
> │    ├── 📄 exhibit_list.docx
> │    ├── 📄 exhibit_list.md
> │    ├── 📄 fix_court_binder.py
> │    ├── 📄 graph-wasm.wasm
> │    └── 📂 imgs/
> │      ├── 📄 05b618077343fbbd92b7.ttf
> │      ├── 📄 07192024_INVOICE_003.jpg
> │      ├── 📄 085cb93e613ba3d40d2b.woff2
> │      ├── 📄 2024-12-14_outgoing_text_bank_access_request.png
> │      ├── 📄 2025-12-20_EXH-10_photos_video_00241326_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_10f4975d_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_1beefb11_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_1f3f8a81_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_25fb1992_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_2f0952db_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_4e01fa01_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_5be451ba_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_5d95cae5_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_63fb7b02_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_71c9e6a7_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_7a544ef7_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_8350e7be_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_8a163413_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_8d885a5c_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_9b611100_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_9fb3a08a_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_9ff5022d_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_a8832e17_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_ca02d006_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_db9b10b5_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_e4cb3622_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_ebaaa38d_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_f510498b_2025-.heic
> │      ├── 📄 2025-12-20_EXH-10_photos_video_f60d8098_2025-1.png
> │      ├── 📄 2025-12-20_EXH-10_photos_video_f98b089a_2025-1.png
> │      ├── 📄 2025-12-20_EXH-10_photos_video_fa1703bf_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-10_photos_video_fdd8d4ef_2025-1.jpg
> │      ├── 📄 2025-12-20_EXH-30_fcfcu_740eacdc_2025-12-20_EX.jpg
> │      ├── 📄 2025-12-20_EXH-30_fcfcu_ac6eb2ea_2025-12-20_EX.jpg
> │      ├── 📄 2308ab1944a6bfa5c5b8.svg
> │      ├── 📄 293fd13dbca5a3e450ef.woff2
> │      ├── 📄 2CAA8E246CB3_1765294197.jpg
> │      ├── 📄 454577c22304619db035.ttf
> │      ├── 📄 52ac8f3034507f1d9e53.ttf
> │      ├── 📄 535a6cf662596b3bd6a6.woff2
> │      ├── 📄 70cc7ff27245e82ad414.ttf
> │      ├── 📄 72505e6a122c6acd5471.woff2
> │      ├── 📄 844d385a31ebae5141198646b19f5dcc3be5831afc2a2a6ecc737d880c2a07dd.jpg
> │      ├── 📄 94f2f163d4b698242fef.otf
> │      ├── 📄 DL_REDACTED.jpg
> │      ├── 📄 FrontImage-2024-07-12.png
> │      ├── 📄 IMG_1833.PNG
> │      ├── 📄 IMG_1837.JPG
> │      ├── 📄 IMG_1864.HEIC
> │      ├── 📄 favicon.png
> │      ├── 📄 identity_verification_bank_statement_old-national.jpg
> │    ├── 📄 index.md
> │    ├── 📄 motion_emergency_stay_of_writ.docx
> │    ├── 📄 motion_emergency_stay_of_writ.md
> │    ├── 📄 motion_emergency_supplemental_motion_ongoing_.docx
> │    ├── 📄 motion_emergency_supplemental_motion_ongoing_ha.md
> │    ├── 📄 motion_to_vacate_void_judgement.docx
> │    ├── 📄 motion_to_vacate_void_judgment.md
> │    ├── 📄 proposed_order_emergency_stay.md
> │    ├── 📄 proposed_order_motion_to_vacate.md
> │    ├── 📄 receipt_usps_tracking.md
> │    ├── 📄 rss.xml
> │    ├── 📄 script_call_lawyers.md
> │    ├── 📄 spoliation_risk_ledger.md
> │    ├── 📄 strategy.csv
> │    └── 📂 txt/
> │      ├── 📄 01092026_C_DOC_D0465.txt
> │      ├── 📄 13312381_C_DOC_D0001.txt
> │      ├── 📄 13312381_C_DOC_D0461.txt
> │      ├── 📄 13312381_C_DOC_D0533.txt
> │      ├── 📄 13312462_C_DOC_D0002.txt
> │      ├── 📄 13312462_C_DOC_D0003.txt
> │      ├── 📄 13312462_C_DOC_D0004.txt
> │      ├── 📄 13312462_C_DOC_D0462.txt
> │      ├── 📄 13312465_C_DOC_D0005.txt
> │      ├── 📄 13312465_C_DOC_D0006.txt
> │      ├── 📄 17695436_C_DOC_D0103.txt
> │      ├── 📄 17701079_C_DOC_D0491.txt
> │      ├── 📄 20230920_C_DOC_D0074.txt
> │      ├── 📄 20240320_C_DOC_D0075.txt
> │      ├── 📄 20241209_C_DOC_D0071.txt
> │      ├── 📄 20241211_C_DOC_D0072.txt
> │      ├── 📄 20250116_C_DOC_D0018.txt
> │      ├── 📄 20250116_C_DOC_D0019.txt
> │      ├── 📄 20250116_C_DOC_D0020.txt
> │      ├── 📄 20250116_C_DOC_D0021.txt
> │      ├── 📄 20250116_C_DOC_D0022.txt
> │      ├── 📄 20250116_C_DOC_D0023.txt
> │      ├── 📄 20250116_C_DOC_D0024.txt
> │      ├── 📄 20250116_C_DOC_D0025.txt
> │      ├── 📄 20250305_C_DOC_D0028.txt
> │      ├── 📄 20250415_C_DOC_D0029.txt
> │      ├── 📄 20250513_C_DOC_D0030.txt
> │      ├── 📄 20250513_C_DOC_D0031.txt
> │      ├── 📄 20250513_C_DOC_D0032.txt
> │      ├── 📄 20250521_C_DOC_D0033.txt
> │      ├── 📄 20250521_C_DOC_D0034.txt
> │      ├── 📄 20250521_C_DOC_D0035.txt
> │      ├── 📄 20250523_C_DOC_D0036.txt
> │      ├── 📄 20250523_C_DOC_D0037.txt
> │      ├── 📄 20250530_C_DOC_D0039.txt
> │      ├── 📄 20250530_C_DOC_D0040.txt
> │      ├── 📄 20250608_C_DOC_D0102.txt
> │      ├── 📄 20250709_C_DOC_D0041.txt
> │      ├── 📄 20250717_C_DOC_D0042.txt
> │      ├── 📄 20250909_C_DOC_D0043.txt
> │      ├── 📄 20251029_C_DOC_D0017.txt
> │      ├── 📄 20251029_C_DOC_D0045.txt
> │      ├── 📄 20251210_C_DOC_D0047.txt
> │      ├── 📄 20251210_C_DOC_D0048.txt
> │      ├── 📄 20251210_C_DOC_D0049.txt
> │      ├── 📄 20251210_C_DOC_D0051.txt
> │      ├── 📄 20251210_C_DOC_D0052.txt
> │      ├── 📄 20251211_C_DOC_D0053.txt
> │      ├── 📄 20251211_C_DOC_D0054.txt
> │      ├── 📄 20251211_C_DOC_D0055.txt
> │      ├── 📄 20251211_C_DOC_D0056.txt
> │      ├── 📄 20251211_C_DOC_D0058.txt
> │      ├── 📄 20251212_C_DOC_D0059.txt
> │      ├── 📄 20251212_C_DOC_D0060.txt
> │      ├── 📄 20251216_C_DOC_D0061.txt
> │      ├── 📄 20251217_C_DOC_D0062.txt
> │      ├── 📄 20251221_C_DOC_D0068.txt
> │      ├── 📄 20251222_C_DOC_D0063.txt
> │      ├── 📄 20251222_C_DOC_D0064.txt
> │      ├── 📄 20251222_C_DOC_D0451.txt
> │      ├── 📄 20260101_C_DOC_D0070.txt
> │      ├── 📄 20260101_C_DOC_D0073.txt
> │      ├── 📄 20260101_C_DOC_D0448.txt
> │      ├── 📄 20260101_C_DOC_D0450.txt
> │      ├── 📄 20260108_C_DOC_D0474.txt
> │      ├── 📄 20260115_C_DOC_D0505.txt
> │      ├── 📄 20260115_C_DOC_D0506.txt
> │      ├── 📄 20260115_C_DOC_D0507.txt
> │      ├── 📄 20260115_C_DOC_D0508.txt
> │      ├── 📄 20260115_C_DOC_D0511.txt
> │      ├── 📄 20260115_C_DOC_D0512.txt
> │      ├── 📄 20260115_C_DOC_D0513.txt
> │      ├── 📄 20260118_C_DOC_D0475.txt
> │      ├── 📄 20260118_C_DOC_D0478.txt
> │      ├── 📄 20260118_C_DOC_D0482.txt
> │      ├── 📄 20260120_C_DOC_D0066.txt
> │      ├── 📄 20260124_C_DOC_D0488.txt
> │      ├── 📄 20260131_C_DOC_D0517.txt
> │      ├── 📄 20260131_C_DOC_D0518.txt
> │      ├── 📄 20260201_C_DOC_D0514.txt
> │      ├── 📄 20260201_C_DOC_D0524.txt
> │      ├── 📄 20260203_C_DOC_D0081.txt
> │      ├── 📄 20260203_C_DOC_D0092.txt
> │      ├── 📄 20260203_C_DOC_D0093.txt
> │      ├── 📄 20260203_C_DOC_D0096.txt
> │      ├── 📄 20260203_C_DOC_D0097.txt
> │      ├── 📄 20260203_C_DOC_D0099.txt
> │      ├── 📄 20260203_C_DOC_D0100.txt
> │      ├── 📄 20260203_C_DOC_D0441.txt
> │      ├── 📄 20260203_C_DOC_D0442.txt
> │      ├── 📄 20260203_C_DOC_D0443.txt
> │      ├── 📄 20260203_C_DOC_D0444.txt
> │      ├── 📄 20260203_C_DOC_D0445.txt
> │      ├── 📄 20260203_C_DOC_D0446.txt
> │      ├── 📄 20260203_C_DOC_D0447.txt
> │      ├── 📄 20260203_C_DOC_D0449.txt
> │      ├── 📄 20260203_C_DOC_D0455.txt
> │      ├── 📄 20260203_C_DOC_D0456.txt
> │      ├── 📄 20260203_C_DOC_D0457.txt
> │      ├── 📄 20260203_C_DOC_D0458.txt
> │      ├── 📄 20260203_C_DOC_D0459.txt
> │      ├── 📄 20260203_C_DOC_D0460.txt
> │      ├── 📄 20260203_C_DOC_D0476.txt
> │      ├── 📄 20260203_C_DOC_D0483.txt
> │      ├── 📄 20260203_C_DOC_D0486.txt
> │      ├── 📄 20260203_C_DOC_D0492.txt
> │      ├── 📄 20260203_C_DOC_D0493.txt
> │      ├── 📄 20260203_C_DOC_D0498.txt
> │      ├── 📄 20260203_C_DOC_D0499.txt
> │      ├── 📄 20260203_C_DOC_D0500.txt
> │      ├── 📄 20260203_C_DOC_D0501.txt
> │      ├── 📄 20260203_C_DOC_D0519.txt
> │      ├── 📄 20260203_C_DOC_D0520.txt
> │      ├── 📄 20260203_C_DOC_D0521.txt
> │      ├── 📄 20260203_C_DOC_D0522.txt
> │      ├── 📄 20260203_C_DOC_D0523.txt
> │      ├── 📄 20260203_C_DOC_D0531.txt
> │      ├── 📄 20260203_C_DOC_D0535.txt
> │      ├── 📄 20260203_C_DOC_D0537.txt
> │      ├── 📄 20260203_C_DOC_D0538.txt
> │      ├── 📄 20260203_C_DOC_D0539.txt
> │      ├── 📄 20260203_C_DOC_D0543.txt
> │      ├── 📄 20260203_C_DOC_D0544.txt
> │      ├── 📄 20260203_C_DOC_D0545.txt
> │      ├── 📄 20260203_C_DOC_D0549.txt
> │      ├── 📄 20260203_C_DOC_D0550.txt
> │      ├── 📄 20260203_C_DOC_D0551.txt
> │      ├── 📄 20260203_C_DOC_D0552.txt
> │      ├── 📄 20260203_C_DOC_D0556.txt
> │      ├── 📄 20260203_C_DOC_D0557.txt
> │      ├── 📄 20260207_C_DOC_D0464.txt
> │      ├── 📄 20260207_C_DOC_D0467.txt
> │      ├── 📄 20260207_C_DOC_D0468.txt
> │      ├── 📄 20260207_C_DOC_D0470.txt
> │      ├── 📄 20260207_C_DOC_D0471.txt
> │      ├── 📄 20260207_C_DOC_D0472.txt
> │      ├── 📄 20260207_C_DOC_D0479.txt
> │      ├── 📄 20260207_C_DOC_D0485.txt
> │      ├── 📄 20260207_C_DOC_D0495.txt
> │      ├── 📄 37288599_C_DOC_D0510.txt
> │      ├── 📄 60185613_C_DOC_D0480.txt
> │    ├── 📄 updated_affidavit_language.md
> │    ├── 📄 verified_affidavit_of_defendant.md
> │    └── 📂 video/
> │      ├── 📄 00-06-23_2a.mkv
> │      ├── 📄 00-16-23_2a.mkv
> │      ├── 📄 00-26-23_2a.mkv
> │      ├── 📄 00-36-23_2a.mkv
> │      ├── 📄 00-46-23_2a.mkv
> │      ├── 📄 00-56-23_2a.mkv
> │      ├── 📄 01-06-23_2a.mkv
> │      ├── 📄 01-16-23_2a.mkv
> │      ├── 📄 01-26-22_2a.mkv
> │      ├── 📄 01-36-22_2a.mkv
> │      ├── 📄 01-46-22_2a.mkv
> │      ├── 📄 01-56-22_2a.mkv
> │      ├── 📄 02-06-22_2a.mkv
> │      ├── 📄 02-16-22_2a.mkv
> │      ├── 📄 02-26-22_2a.mkv
> │      ├── 📄 02-36-22_2a.mkv
> │      ├── 📄 02-46-22_2a.mkv
> │      ├── 📄 02-56-21_2a.mkv
> │      ├── 📄 03-06-21_2a.mkv
> │      ├── 📄 03-16-21_2a.mkv
> │      ├── 📄 03-26-21_2a.mkv
> │      ├── 📄 03-36-21_2a.mkv
> │      ├── 📄 03-46-21_2a.mkv
> │      ├── 📄 03-56-21_2a.mkv
> │      ├── 📄 04-06-21_2a.mkv
> │      ├── 📄 04-16-21_2a.mkv
> │      ├── 📄 04-26-21_2a.mkv
> │      ├── 📄 04-36-21_2a.mkv
> │      ├── 📄 04-46-20_2a.mkv
> │      ├── 📄 04-56-20_2a.mkv
> │      ├── 📄 05-06-20_2a.mkv
> │      ├── 📄 05-16-20_2a.mkv
> │      ├── 📄 05-26-20_2a.mkv
> │      ├── 📄 05-36-20_2a.mkv
> │      ├── 📄 05-46-20_2a.mkv
> │      ├── 📄 05-56-20_2a.mkv
> │      ├── 📄 06-06-20_2a.mkv
> │      ├── 📄 06-16-20_2a.mkv
> │      ├── 📄 06-26-20_2a.mkv
> │      ├── 📄 06-36-19_2a.mkv
> │      ├── 📄 06-46-19_2a.mkv
> │      ├── 📄 06-56-19_2a.mkv
> │      ├── 📄 07-06-19_2a.mkv
> │      ├── 📄 07-16-19_2a.mkv
> │      ├── 📄 07-26-19_2a.mkv
> │      ├── 📄 07-36-19_2a.mkv
> │      ├── 📄 07-46-19_2a.mkv
> │      ├── 📄 07-56-19_2a.mkv
> │      ├── 📄 08-06-19_2a.mkv
> │      ├── 📄 08-16-18_2a.mkv
> │      ├── 📄 08-26-18_2a.mkv
> │      ├── 📄 08-36-18_2a.mkv
> │      ├── 📄 08-46-18_2a.mkv
> │      ├── 📄 08-56-18_2a.mkv
> │      ├── 📄 09-06-18_2a.mkv
> │      ├── 📄 09-16-18_2a.mkv
> │      ├── 📄 09-26-18_2a.mkv
> │      ├── 📄 09-36-18_2a.mkv
> │      ├── 📄 09-46-18_2a.mkv
> │      ├── 📄 09-56-18_2a.mkv
> │      ├── 📄 10-06-17_2a.mkv
> │      ├── 📄 10-16-17_2a.mkv
> │      ├── 📄 10-26-17_2a.mkv
> │      ├── 📄 10-36-17_2a.mkv
> │      ├── 📄 10-46-17_2a.mkv
> │      ├── 📄 10-56-17_2a.mkv
> │      ├── 📄 2CAA8E1B675120251209103140_album_local_cache.mp4
> │      ├── 📄 2CAA8E246CB320251209103011_album_local_cache.mp4
> │      ├── 📄 2d5198822ab091ce4305.woff2
> │      ├── 📄 4bb6ac751d1c5478ff3a.woff2
> │      ├── 📄 Missing_Evidence_and_Vanishing_Foreclosure_Surplus.m4a
> │      ├── 📄 Recording.m4a
> │      ├── 📄 integrate_disability_separate_appeals_get_stay.m4a
> │      ├── 📄 voicemail-14956B1E-5384-4F00-9AB1-C87D98D7C6E1.m4a
> │  └── 📂 references/
> │    ├── 📄 1975_CIVIL_RIGHTS_.md
> │    ├── 📄 1977_19_PROCEDURAL_.md
> │    ├── 📄 1980s_FAIR_HOUSING_ACT_BREACH__EXCLUSIONARY_ZONING__.md
> │    ├── 📄 1985_PROCEDURAL_.md
> │    ├── 📄 2000_PROCEDURAL_.md
> │    ├── 📄 2009_Ca_PROCEDURAL_.md
> │    ├── 📄 2009_FAIR_HOUSING_ACT_BREACH__PATTERN_OR_PRACTICE_OF_REDLINING__.md
> │    ├── 📄 2010_20_ADA_.md
> │    ├── 📄 2020_FAIR_HOUSING_ACT_BREACH__REASONABLE_ACCOMMODATION_FAILURE__.md
> │    ├── 📄 2026_REF_FCRA_Remedies.pdf
> │    ├── 📄 99_CASE_SCHEMA.md
> │    ├── 📄 April 20_FAIR_HOUSING_ACT_BREACH__RACE__NATIONAL_ORIGIN___HOSTILE_HOUSING_ENVIRONMENT_.md
> │    ├── 📄 April 20_FAIR_HOUSING_ACT_BREACH__SEXUAL_HARASSMENT__.md
> │    ├── 📄 August 1_FAIR_HOUSING_ACT_BREACH__ACCESSIBILITY_REQUIREMENTS__.md
> │    ├── 📄 August 2_FAILURE_TO_PROVIDE_EQUAL_MAINTENANCE_SERVICES__REO_DWELLINGS__.md
> │    ├── 📄 August 2_FAIR_HOUSING_ACT_BREACH__GENDER___SEXUAL_HARASSMENT_.md
> │    ├── 📄 August 2_POTENTIAL_IC___32_30_10_14_VIOLATION__SURPLUS_MISMANAGEMENT__.md
> │    ├── 📄 Early 20_ADA_.md
> │    ├── 📄 February_FAIR_HOUSING_ACT_BREACH__DISABILITY__FAMILIAL_STATUS__.md
> │    ├── 📄 Google Sheets Validation Guide.md
> │    ├── 📄 January _DUE_PROCESS_FAILURE___NOTICE_DEFICIENCY_.md
> │    ├── 📄 January _FAIR_HOUSING_ACT_BREACH__FAMILIAL_STATUS___OCCUPANCY_POLICIES_.md
> │    ├── 📄 July 201_FAIR_HOUSING_ACT_BREACH__INTENTIONAL_DISCRIMINATION___DISPARATE_IMPACT__.md
> │    ├── 📄 June 8, _ADA_.md
> │    ├── 📄 June 9, _PROCEDURAL_.md
> │    ├── 📄 March 20_FAIR_HOUSING_ACT_BREACH__FAMILIAL_STATUS__.md
> │    ├── 📄 March 20_FAIR_HOUSING_ACT_BREACH__RACE__COLOR___APPRAISAL_BIAS_.md
> │    ├── 📄 March 5,_DUE_PROCESS_FAILURE___DEFECTIVE_SERVICE_.md
> │    ├── 📄 March 5,_PROCEDURAL_.md
> │    ├── 📄 May 28, _FORECLOSURE_.md
> │    ├── 📄 May 28, _PROCEDURAL_.md
> │    ├── 📄 Not in s_ADA_.md
> │    ├── 📄 Not in s_DISCRIMINATORY_ADVERTISING_.md
> │    ├── 📄 Not in s_DUE_PROCESS_VIOLATION__STANDARD_OF_PROOF__.md
> │    ├── 📄 Not in s_FAIR_HOUSING_ACT_BREACH__REASONABLE_ACCOMMODATION_FAILURE__.md
> │    ├── 📄 Not in s_PROCEDURAL_.md
> │    ├── 📄 Not in s_SECTION_504_BREACH___FAILURE_TO_PROVIDE_INTERPRETER_.md
> │    ├── 📄 Not in s_UNCONSTITUTIONAL_PRESUMPTION__VESTING_OF_TITLE__.md
> │    ├── 📄 November_FAIR_HOUSING_ACT_BREACH__REASONABLE_ACCOMMODATION_DENIAL__.md
> │    ├── 📄 November_FRAUD_ON_THE_COURT___MATERIAL_MISREPRESENTATION_.md
> │    ├── 📄 October _FAIR_HOUSING_ACT_BREACH__RACE__NATIONAL_ORIGIN___DISCRIMINATORY_MAINTENANCE_.md
> │    ├── 📄 October _FAIR_HOUSING_ACT_BREACH__RACE___REDLINING_.md
> │    ├── 📄 Preforec_ADA_.md
> │    ├── 📄 Septembe_FAIR_HOUSING_ACT_BREACH__RACE___ARBITRARY_CRIMINAL_HISTORY_POLICIES_.md
> │    ├── 📄 _references.md
> │    ├── 📄 rules.md
> │    ├── 📄 schema.json
> │  └── 📂 templates/
> │    ├── 📄 Notebooklm-prompts.md
> │    ├── 📄 _templates.md
> │    └── 📂 affidavits/
> │      ├── 📄 EMERGENCY SUPPLEMENTAL DECLARATION.gdoc
> │      ├── 📄 TPL_Affidavit_ADA_Disability.md
> │      ├── 📄 TPL_Affidavit_Character.md
> │      ├── 📄 TPL_Affidavit_Community_Service.md
> │      ├── 📄 TPL_Affidavit_Credibility.md
> │      ├── 📄 TPL_Affidavit_Language_Updates.md
> │      ├── 📄 TPL_Affidavit_Observations.md
> │      ├── 📄 TPL_Affidavit_Verified_Defendant.md
> │      ├── 📄 TPL_Declaration_Gender_Identity_Clarification.md
> │      ├── 📄 TPL_housing_affidavit.md
> │      ├── 📄 WF5.01.010__Credibility_Affidavit.md
> │      ├── 📄 WF5.01.010__Gender_Identity_Clarification.md
> │      ├── 📄 WF5.01.010__updated_affidavit_language.md
> │      ├── 📄 WF5.01.010__verified_affidavit_of_defendant.md
> │      ├── 📄 _affidavits.md
> │    └── 📂 binders/
> │      ├── 📄 TPL_Binder_Section_Cover.md
> │      ├── 📄 TPL_Binder_Section_Index.md
> │      ├── 📄 _binders.md
> │    └── 📂 exhibits/
> │      ├── 📄 TPL_Exhibits_Lists.md
> │      ├── 📄 _exhibits.md
> │    └── 📂 front_matter/
> │      ├── 📄 FRONT_MATTER_MIGRATION_INSTRUCTION.md
> │      ├── 📄 _front_matter.md
> │    └── 📂 internal/
> │      ├── 📄 TPL_settlement_letter_draft.md
> │      ├── 📄 _internal.md
> │    └── 📂 motions/
> │      ├── 📄 Copy of  EMERGENCY MOTION TO PRESERVE AND ACCOUNT FOR SURPLUS FUNDS.gdoc
> │      ├── 📄 EMERGENCY MOTION TO PRESERVE AND ACCOUNT FOR SURPLUS FUNDS.gdoc
> │      ├── 📄 TPL_emergency_stay_of_writ.md
> │      ├── 📄 TPL_vacate_void_judgment.md
> │      ├── 📄 _10_motions.md
> │      ├── 📄 _motions.md
> │    └── 📂 orders/
> │      ├── 📄 TPL_Proposed_Order.md
> │      ├── 📄 TPL_proposed_order_emergency_stay.md
> │      ├── 📄 TPL_proposed_order_motion_to_vacate.md
> │      ├── 📄 _orders.md
> │    └── 📂 outreach/
> │      ├── 📄 TPL_Advocate_Outreach.md
> │      ├── 📄 TPL_Attorney_Brief.md
> │      ├── 📄 _outreach.md
> │    └── 📂 packets/
> │      ├── 📄 TPL_ADA_Packet.md
> │      ├── 📄 TPL_Handup_Packet_Note.md
> │      ├── 📄 TPL_attorney_intake_packet_executive.md
> │      ├── 📄 _packets.md
> │  └── 📂 tools/
> │    ├── 📄 Efileincourts.gov.md
> │    ├── 📄 GenerateTimelineInventory.py
> │    ├── 📄 _tools.md
> │    ├── 📄 analyze_tasks.py
> │    ├── 📄 analyze_tasks_v2.py
> │    ├── 📄 compiled_task_spine.csv
> │    ├── 📄 dedupe_content_recursive.py
> │    ├── 📄 dedupe_intake.py
> │    ├── 📄 dedupe_intake_v2.py
> │    ├── 📄 dedupe_intake_v3.py
> │    ├── 📄 dedupe_suffixes.py
> │    ├── 📄 dedupe_suffixes_recursive.py
> │    ├── 📄 dedupe_suffixes_v2.py
> │    ├── 📄 dump_tree_with_ocr.py
> │    ├── 📄 index.py
> │    ├── 📄 merge_intake.py
> │    ├── 📄 merge_intake_v2.py
> │    ├── 📄 schema_task_spine.md
> │    └── 📂 scripts/
> │      ├── 📄 AddManualTasks.ps1
> │      ├── 📄 CleanCaseMaster.py
> │      ├── 📄 ExtractCaseMasterLogs.py
> │      ├── 📄 ExtractViolationsTimeline.py
> │      ├── 📄 GenerateTimelineEntries.ps1
> │      ├── 📄 MigrateTasks.ps1
> │      ├── 📄 StandardizeFM.ps1
> │      ├── 📄 SweepCaseMaster.py
> │      ├── 📄 UpdateCaseChecklist.ps1
> │      ├── 📄 _scripts.md
> │      ├── 📄 migrate_task_spine.py
> │    ├── 📄 sync_violations.py
> └── 📂 99_VAULT/
> │  └── 📂 10_Authority/
> │    └── 📂 Agency_Guidance/
> │      ├── 📄 _Agency_Guidance.md
> │    └── 📂 Case_Law/
> │      ├── 📄 _Case_Law.md
> │    └── 📂 Court_Rules/
> │      ├── 📄 _Court_Rules.md
> │    └── 📂 Policies/
> │      ├── 📄 _Policies.md
> │    └── 📂 Regulations/
> │      ├── 📄 _Regulations.md
> │    └── 📂 Statutes/
> │      ├── 📄 _Statutes.md
> │    ├── 📄 _10_Authority.md
> │  └── 📂 C-00_Foreclosure_Record/
> │    └── 📂 C00_DOCKET/
> │      ├── 📄 20250116_DKT_09_15_15_APPEARANCE.PDF
> │      ├── 📄 20250116_DKT_09_16_24_REQUEST_FOR_ADMISSIONS.PDF
> │      ├── 📄 20250116_DKT_09_17_12_NOTICE_TO_HOMEOWNERS.PDF
> │      ├── 📄 20250116_DKT_09_17_59_APPEARANCE.PDF
> │      ├── 📄 20250116_DKT_09_19_01_SUMMONS.PDF
> │      ├── 📄 20250116_DKT_09_19_33_SUMMONS.PDF
> │      ├── 📄 20250116_DKT_09_20_42_SUMMONS.PDF
> │      ├── 📄 20250116_DKT_09_21_26_SUMMONS.PDF
> │      ├── 📄 20250116_DKT_09_22_07_SUMMONS.PDF
> │      ├── 📄 20250116_DKT_COMPLAINT_AND_SUMMONS.PDF
> │      ├── 📄 20250305_DKT_SERVICE_RETURNED_SERVED_1.PDF
> │      ├── 📄 20250415_DKT_SERVICE_RETURNED_SERVED_2.PDF
> │      ├── 📄 20250513_DKT_14_52_56_MOTION_DEFAULT.PDF
> │      ├── 📄 20250513_DKT_14_53_36_AFFIDAVIT.PDF
> │      ├── 📄 20250513_DKT_14_54_31_AFFIDAVIT_ATTORNEY.PDF
> │      ├── 📄 20250513_DKT_MOTION_DEFAULT_JUDGMENT.PDF
> │      ├── 📄 20250521_DKT_14_25_43_OMITTED_NOTICE.PDF
> │      ├── 📄 20250521_DKT_USPS_CERTIFIED_RECEIPT.PDF
> │      ├── 📄 20250523_DKT_11_06_25_REQUEST_DEFAULT.PDF
> │      ├── 📄 20250523_DKT_MOTION_AMENDED_DEFAULT.PDF
> │      ├── 📄 20250528_DKT_PRAECIPE_FOR_SHERIFFS_SALES.PDF
> │      ├── 📄 20250529_DKT_AMENDED_DEFAULT_JUDGEMENT.PDF
> │      ├── 📄 20250709_DKT_NOTICE_SHERIFF_SALE_POSTED.PDF
> │      ├── 📄 20250717_DKT_PLAINTIFF_BID.PDF
> │      ├── 📄 20250909_DKT_DECREE_RETURNED.PDF
> │      ├── 📄 20251029_DKT_13_47_03_ORDER_FOR_WRIT.PDF
> │      ├── 📄 20251029_DKT_13_47_52_WRIT.PDF
> │      ├── 📄 20251029_DKT_PETITION_WRIT_ASSISTANCE.PDF
> │      ├── 📄 20251211_DKT_EMERGENCY_MOTION_STAY_WRIT.PDF
> │      ├── 📄 20251211_DKT_EXHIBIT_LIST.PDF
> │      ├── 📄 20251211_DKT_MOTION_TO_VACATE_JUDGMENT.PDF
> │      ├── 📄 20251211_DKT_PROPOSED_ORDER_STAY.PDF
> │      ├── 📄 20251211_DKT_PROPOSED_ORDER_VACATE.PDF
> │      ├── 📄 20251211_DKT_SUPPLEMENTAL_EMERGENCY_MOTION.PDF
> │      ├── 📄 20251212_DKT_NOTICE_OBTAIN_ITEM_REPORT.PDF
> │      ├── 📄 20251216_DKT_EMERGENCY_SUPPLEMENTAL_DECLARATION.PDF
> │      ├── 📄 20251216_DKT_MOTION_PRESERVE_SURPLUS.PDF
> │      ├── 📄 20251217_DKT_REPORT_SHERIFF_SALE.PDF
> │      ├── 📄 20251222_DKT_DECLARATION_ONGOING_DISPLACEMENT.PDF
> │      ├── 📄 20260109_DKT_HEARING_JOURNAL_ENTRY.PDF
> │      ├── 📄 20260121_DKT_ORDER_DENYING_VACATE.PDF
> │      ├── 📄 20260209_DKT_CASE_DOC_TEMPLATE.PDF
> │      ├── 📄 _C00_DOCKET.md
> │      ├── 📄 _MYCASE_DOCKET_SUMMARY.MD
> │    ├── 📄 C00_Hearing_Transcript_Recording_20260209_174803.mp4
> │    ├── 📄 _C00_Record_Defects.md
> │  └── 📂 C-01_Service_Notice_Defects/
> │    └── 📂 00_RECEIVED/
> │      ├── 📄 _00_RECEIVED.md
> │    └── 📂 01_FILED/
> │      ├── 📄 20260115_C01_FORECL_FCFCU_MOTION_D0511.pdf
> │      ├── 📄 _01_FILED.md
> │    └── 📂 02_ORDERS/
> │      ├── 📄 20260118_C01_FORECL_FCFCU_MOTION_D0482.pdf
> │      ├── 📄 _02_ORDERS.md
> │    └── 📂 03_EVIDENCE/
> │      └── 📂 01_PHOTOS/
> │        ├── 📄 _01_PHOTOS.md
> │      └── 📂 02_VIDEO/
> │        ├── 📄 _02_VIDEO.md
> │      └── 📂 03_DOCUMENTS/
> │        ├── 📄 _03_DOCUMENTS.md
> │      └── 📂 04_FINANCIAL/
> │        ├── 📄 _04_FINANCIAL.md
> │      └── 📂 05_EXPORTS/
> │        ├── 📄 _05_EXPORTS.md
> │      ├── 📄 _03_EVIDENCE.md
> │    └── 📂 04_CORRESPONDENCE/
> │      ├── 📄 20260101_C01_FORECL_FCFCU_DOC_D0073.pdf
> │      ├── 📄 20260207_C01_FORECL_FCFCU_MOTION_D0510.pdf
> │      ├── 📄 _04_CORRESPONDENCE.md
> │    └── 📂 05_LOGS/
> │      ├── 📄 20260203_C01_FORECL_FCFCU_DOC_D0551.pdf
> │      ├── 📄 20260203_C01_FORECL_FCFCU_ORDER_D0549.pdf
> │      ├── 📄 20260203_C01_FORECL_ORDER_D0550.pdf
> │      ├── 📄 20260210_REPORT_AI_Analysis_Grok.pdf
> │      ├── 📄 Service_Log.md
> │      ├── 📄 _05_LOGS.md
> │    ├── 📄 20251126_C02_VIDEO_D0440.mp4
> │    ├── 📄 20251203_C02_PHOTO_D0247.jpg
> │    ├── 📄 20251203_C02_VIDEO_D0439.mp4
> │    ├── 📄 20251209_C02_PHOTO_D0108.jpg
> │    ├── 📄 20261125_220020_C02_PHOTO_D0248.png
> │    └── 📂 99_ARCHIVE/
> │      ├── 📄 _99_ARCHIVE.md
> │    ├── 📄 Comparable_Market_Analysis_4817_Shadow_Pointe_Dr.html
> │    ├── 📄 _C01_Service_Notice_Defects.md
> │    ├── 📄 _TOC.md
> │  └── 📂 C-02_Evidence_Preservation/
> │    └── 📂 00_drafts/
> │      ├── 📄 20260202_CAPTURE_Auto_Save_D0516.html
> │      ├── 📄 _C02_drafts.md
> │    └── 📂 01_PHOTOS/
> │      ├── 📄 20251209_PHOTO_Auto_Save_D0107.heic
> │      ├── 📄 20251209_PHOTO_Auto_Save_D0112.heic
> │      ├── 📄 20251220_PHOTO_Auto_Save_D0132.heic
> │      ├── 📄 20251220_PHOTO_Auto_Save_D0133.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0144.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0145.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0146.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0147.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0148.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0149.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0150.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0151.heic
> │      ├── 📄 20260208_PHOTO_Evidence_IMG_2905.PNG
> │      ├── 📄 20260208_PHOTO_Evidence_IMG_2906.PNG
> │      ├── 📄 20260208_PHOTO_Evidence_IMG_2908.PNG
> │      ├── 📄 20260208_PHOTO_Evidence_IMG_2911.PNG
> │      ├── 📄 20260208_PHOTO_Evidence_IMG_2913.PNG
> │      ├── 📄 20260208_PHOTO_Evidence_IMG_2914.PNG
> │      ├── 📄 _01_PHOTOS.md
> │    └── 📂 02_VIDEO/
> │      ├── 📄 20260209_C02_Screen_Recording_hearing_jan_09_2026.mp4
> │      ├── 📄 _02_VIDEO.md
> │    └── 📂 03_DOCUMENTS/
> │      ├── 📄 20260121_FILE_Auto_Save_D0477.pptx
> │      ├── 📄 20260131_C06_ADA_FCFCU_INV_D0517.pdf
> │      ├── 📄 20260201_C00_ORDER_D0524.pdf
> │      ├── 📄 20260201_C06_ADA_VIDEO_D0514.pdf
> │      ├── 📄 20260203_C00_ORDER_D0552.pdf
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0469.mhtml
> │      ├── 📄 20260203_EMAIL_Auto_Save_D0497.eml
> │      ├── 📄 20260207_FILE_Auto_Save_D0014.mw
> │      ├── 📄 20260209_LEGAL_Appellate_Document.docx
> │      ├── 📄 20260209_LEGAL_Appellate_Document.pdf
> │      ├── 📄 20260209_NOTICE_Direct_Dispute_Deletion_Demand.pdf
> │      ├── 📄 20260209_TEMPLATE_Case_Document.pdf
> │      ├── 📄 20260209_TEMPLATE_Case_Document_Backup.pdf
> │      ├── 📄 20260210_NOTICE_Notice_of_Appeal_FILED.pdf
> │      ├── 📄 20260210_NOTICE_Notice_of_Appeal_FILED.png
> │      ├── 📄 20260210_REPORT_ShadowPointe_Client.pdf
> │      ├── 📄 _03_DOCUMENTS.md
> │    └── 📂 04_FINANCIAL/
> │      ├── 📄 20250719_INV_Zoho_Corp_50100846854.pdf
> │      ├── 📄 20250729_INV_Zoho_Corp_50100879809.pdf
> │      ├── 📄 20250729_INV_Zoho_Corp_50100883027.pdf
> │      ├── 📄 20250807_INV_Zoho_Corp_50100916138.pdf
> │      ├── 📄 20251126_NOTICE_AES_Disconnect.pdf
> │      ├── 📄 20260115_INV_Tello_Mobile_82016155.pdf
> │      ├── 📄 20260115_INV_Tello_Mobile_82016231.pdf
> │      ├── 📄 20260115_INV_Tello_Mobile_82016359.pdf
> │      ├── 📄 20260115_INV_Tello_Mobile_82016391.pdf
> │      ├── 📄 20260115_INV_Zoho_Corp_50101514115.pdf
> │      ├── 📄 20260202_INV_Invoice_Generic_1.pdf
> │      ├── 📄 20260202_INV_Invoice_Generic_2.pdf
> │      ├── 📄 20260202_INV_Invoice_Generic_3.pdf
> │      ├── 📄 20260202_INV_Invoice_Generic_4.pdf
> │      ├── 📄 20260202_INV_Zoho_Corp_50100846854.pdf
> │      ├── 📄 20260202_INV_Zoho_Corp_50100879809.pdf
> │      ├── 📄 20260202_INV_Zoho_Corp_50100883027.pdf
> │      ├── 📄 20260202_INV_Zoho_Corp_50100916138.pdf
> │      ├── 📄 20260203_INV_Invoice_Generic_1.pdf
> │      ├── 📄 20260205_INV_RecordXchange_4_018222.pdf
> │      ├── 📄 _04_FINANCIAL.md
> │    └── 📂 05_EXPORTS/
> │      └── 📂 20260109_Hearing_Transcript_Exports/
> │        ├── 📄 20260209_C02_Site_Download_hearing_jan_09_2026.html
> │        ├── 📄 20260209_C02_hearing_jan_09_2026_transcript_regular.txt
> │        ├── 📄 _20260109_Hearing_Transcript_Exports.md
> │      ├── 📄 _05_EXPORTS.md
> │    ├── 📄 20260131_C03_FCRA_FCFCU_DISP_D0518.pdf
> │    ├── 📄 _C02_EVIDENCE.md
> │    ├── 📄 _C02_Evidence_Preservation.md
> │  └── 📂 C-03_Financial_Misconduct/
> │    └── 📂 01_PHOTOS/
> │      ├── 📄 20251220_C02_PHOTO_D0077.jpg
> │      ├── 📄 20260118_C02_PHOTO_D0246.jpeg
> │      ├── 📄 20260118_C02_PHOTO_D0473.jpeg
> │      ├── 📄 _01_PHOTOS.md
> │    └── 📂 03_DOCUMENTS/
> │      ├── 📄 20260118_C03_FCRA_COMPLAINT_D0478.pdf
> │      ├── 📄 20260118_C03_FCRA_EXPRN_ORDER_D0475.pdf
> │      ├── 📄 20260203_C03_EQFX_DOC_D0535.pdf
> │      ├── 📄 20260203_C03_FCRA_DISP_D0457.pdf
> │      ├── 📄 20260203_C03_FCRA_EQFX_DISP_D0483.pdf
> │      ├── 📄 20260203_C03_FCRA_EQFX_DISP_D0493.pdf
> │      ├── 📄 20260203_C03_FCRA_EQFX_JUDGM_D0531.pdf
> │      ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0455.pdf
> │      ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0456.pdf
> │      ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0459.pdf
> │      ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0537.pdf
> │      ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0538.pdf
> │      ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0539.pdf
> │      ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0519.pdf
> │      ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0520.pdf
> │      ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0543.pdf
> │      ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0544.pdf
> │      ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0545.pdf
> │      ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0486.pdf
> │      ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0498.pdf
> │      ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0500.pdf
> │      ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0501.pdf
> │      ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0541.pdf
> │      ├── 📄 20260203_C03_FCRA_TRNUN_ORDER_D0499.pdf
> │      ├── 📄 20260207_C03_FCRA_EQFX_DISP_D0480.pdf
> │      ├── 📄 20260207_C03_FCRA_EQFX_DISP_D0533.pdf
> │      ├── 📄 20260207_C03_FCRA_EQFX_JUDGM_D0003.pdf
> │      ├── 📄 20260207_C03_FCRA_EQFX_JUDGM_D0004.pdf
> │      ├── 📄 20260207_C03_FCRA_EQFX_JUDGM_D0529.pdf
> │      ├── 📄 20260207_C03_FCRA_FCFCU_JUDGM_D0006.pdf
> │      ├── 📄 20260207_C03_FCRA_FCFCU_JUDGM_D0530.pdf
> │      ├── 📄 20260207_C03_FCRA_TRNUN_DISP_D0467.pdf
> │      ├── 📄 20260207_C03_FCRA_TRNUN_DISP_D0485.pdf
> │      ├── 📄 20260207_C03_FCRA_TRNUN_DOC_D0468.pdf
> │      ├── 📄 20260207_C03_FCRA_TRNUN_DOC_D0470.pdf
> │      ├── 📄 20260207_C03_FCRA_TRNUN_DOC_D0471.pdf
> │      ├── 📄 20260207_C03_FCRA_TRNUN_VIDEO_D0472.pdf
> │      ├── 📄 20260207_C03_TRNUN_COMPLAINT_D0479.pdf
> │      ├── 📄 20260209_REPORT_CapOne_Credit_Ricevelasquez_A.pdf
> │      ├── 📄 20260209_REPORT_CapOne_Credit_Ricevelasquez_B.pdf
> │      ├── 📄 20260209_REPORT_CapOne_Credit_Ricevelasquez_James.pdf
> │      ├── 📄 _03_DOCUMENTS.md
> │    └── 📂 03_EVIDENCE/
> │      └── 📂 01_PHOTOS/
> │        ├── 📄 20240624_C02_PHOTO_D0076.jpg
> │        ├── 📄 20251220_C02_PHOTO_D0078.png
> │        ├── 📄 20251220_C02_PHOTO_D0454.jpg
> │        ├── 📄 20260207_C02_PHOTO_D0245.jpg
> │        ├── 📄 _01_PHOTOS.md
> │      └── 📂 02_VIDEO/
> │        ├── 📄 _02_VIDEO.md
> │      └── 📂 03_DOCUMENTS/
> │        ├── 📄 20260101_C00_FCFCU_DOC_D0448.pdf
> │        ├── 📄 20260101_C00_FCFCU_DOC_D0450.pdf
> │        ├── 📄 20260108_C00_AES_DOC_D0474.pdf
> │        ├── 📄 20260203_C00_AES_DOC_D0460.pdf
> │        ├── 📄 20260203_C00_DOC_D0441.pdf
> │        ├── 📄 20260203_C00_DOC_D0458.pdf
> │        ├── 📄 20260203_C00_FCFCU_DOC_D0442.pdf
> │        ├── 📄 20260203_C00_FCFCU_DOC_D0443.pdf
> │        ├── 📄 20260203_C00_FCFCU_DOC_D0444.pdf
> │        ├── 📄 20260203_C00_FCFCU_DOC_D0446.pdf
> │        ├── 📄 20260203_C00_FCFCU_DOC_D0447.pdf
> │        ├── 📄 20260203_C00_FCFCU_DOC_D0449.pdf
> │        ├── 📄 20260203_C00_INV_D0445.pdf
> │        ├── 📄 20260208_REPORT_Credit_Analysis_WalletHub.pdf
> │        ├── 📄 20260208_REPORT_WalletHub_Credit_Analysis.pdf
> │        ├── 📄 20260209_REPORT_Credit_Report.pdf
> │        ├── 📄 FCFCU_NOTICE_Direct_Dispute_Deletion_Demand.pdf
> │        ├── 📄 _03_DOCUMENTS.md
> │      └── 📂 04_FINANCIAL/
> │        ├── 📄 _04_FINANCIAL.md
> │      └── 📂 05_EXPORTS/
> │        ├── 📄 _05_EXPORTS.md
> │      ├── 📄 _03_EVIDENCE.md
> │    └── 📂 04_FINANCIAL/
> │      ├── 📄 20260207_C02_PHOTO_D0466.jpg
> │      ├── 📄 20260207_C03_FCRA_EQFX_INV_D0001.pdf
> │      ├── 📄 20260207_C03_FCRA_EQFX_INV_D0461.pdf
> │      ├── 📄 20260207_C03_FCRA_LSTRM_INV_D0002.pdf
> │      ├── 📄 20260207_C03_FCRA_LSTRM_INV_D0005.pdf
> │      ├── 📄 20260207_C03_FCRA_LSTRM_INV_D0462.pdf
> │      ├── 📄 20260207_C03_FCRA_LSTRM_INV_D0463.pdf
> │      ├── 📄 _04_FINANCIAL.md
> │    ├── 📄 20260202_CAPTURE_Auto_Save_D0525.html
> │    ├── 📄 20260202_CAPTURE_Auto_Save_D0526.html
> │    ├── 📄 20260202_CAPTURE_Auto_Save_D0528.html
> │    ├── 📄 20260202_CAPTURE_Auto_Save_D0534.html
> │    ├── 📄 20260202_CAPTURE_Auto_Save_D0536.html
> │    ├── 📄 20260202_CAPTURE_Auto_Save_D0540.html
> │    ├── 📄 20260202_CAPTURE_Auto_Save_D0559.html
> │    ├── 📄 20260202_CAPTURE_Auto_Save_D0560.html
> │    ├── 📄 20260202_CAPTURE_Auto_Save_D0563.html
> │    ├── 📄 20260202_CAPTURE_Auto_Save_D0564.html
> │    ├── 📄 20260203_CAPTURE_Auto_Save_D0515.html
> │    ├── 📄 20260203_CAPTURE_Auto_Save_D0527.html
> │    ├── 📄 20260203_CAPTURE_Auto_Save_D0532.html
> │    ├── 📄 20260203_CAPTURE_Auto_Save_D0542.html
> │    ├── 📄 20260203_CAPTURE_Auto_Save_D0546.html
> │    ├── 📄 20260203_CAPTURE_Auto_Save_D0547.html
> │    ├── 📄 _03_EVIDENCE.md
> │    ├── 📄 _C03_Credit_Reporting_FCRA.md
> │    ├── 📄 _C07_Financial_Misconduct.md
> │  └── 📂 C-04_Writ_Removal_Conduct/
> │    └── 📂 01_PHOTOS/
> │      ├── 📄 20251209_C02_PHOTO_D0109.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0110.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0111.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0113.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0114.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0155.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0156.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0157.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0158.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0159.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0160.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0161.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0162.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0163.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0164.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0165.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0166.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0167.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0168.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0169.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0170.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0171.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0172.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0173.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0174.png
> │      ├── 📄 20251209_C02_PHOTO_D0175.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0176.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0177.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0178.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0179.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0180.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0181.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0182.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0183.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0184.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0185.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0186.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0188.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0189.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0190.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0191.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0192.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0193.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0194.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0195.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0196.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0197.png
> │      ├── 📄 20251209_C02_PHOTO_D0198.png
> │      ├── 📄 20251209_C02_PHOTO_D0199.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0200.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0201.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0202.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0203.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0204.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0205.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0206.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0207.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0208.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0209.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0210.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0211.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0212.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0214.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0215.png
> │      ├── 📄 20251220_C02_PHOTO_D0216.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0217.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0218.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0219.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0220.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0221.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0222.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0223.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0225.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0226.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0227.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0228.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0229.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0230.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0231.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0233.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0234.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0235.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0236.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0237.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0238.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0239.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0240.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0241.png
> │      ├── 📄 20251220_C02_PHOTO_D0242.png
> │      ├── 📄 20251220_C02_PHOTO_D0243.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0244.jpg
> │      ├── 📄 20260207_C02_PHOTO_D0213.jpg
> │      ├── 📄 20260207_C02_PHOTO_D0224.jpg
> │      ├── 📄 _01_PHOTOS.md
> │    └── 📂 02_VIDEO/
> │      ├── 📄 20251209_C02_VIDEO_D0104.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0105.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0106.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0249.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0250.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0251.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0252.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0253.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0254.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0255.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0256.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0257.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0258.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0259.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0260.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0261.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0262.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0263.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0264.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0265.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0266.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0267.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0268.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0269.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0270.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0271.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0272.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0273.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0274.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0275.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0276.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0277.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0278.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0279.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0280.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0281.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0282.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0283.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0284.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0285.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0286.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0115.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0116.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0117.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0118.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0119.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0120.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0121.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0122.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0123.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0124.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0125.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0126.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0127.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0128.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0129.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0130.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0131.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0287.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0288.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0289.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0290.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0291.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0292.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0293.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0294.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0295.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0296.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0297.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0298.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0299.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0300.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0301.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0302.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0303.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0304.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0305.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0306.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0307.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0308.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0309.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0310.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0311.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0312.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0313.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0314.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0315.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0316.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0317.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0318.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0319.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0320.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0321.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0322.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0323.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0324.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0325.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0326.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0327.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0328.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0329.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0330.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0331.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0332.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0333.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0334.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0335.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0336.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0337.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0338.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0339.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0340.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0341.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0342.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0343.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0344.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0345.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0346.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0347.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0348.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0349.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0350.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0351.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0352.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0353.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0354.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0355.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0356.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0357.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0358.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0359.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0360.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0361.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0362.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0363.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0364.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0365.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0366.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0367.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0368.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0369.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0370.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0371.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0372.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0373.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0374.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0375.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0376.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0377.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0378.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0379.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0380.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0381.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0382.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0383.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0384.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0385.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0386.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0387.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0388.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0389.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0390.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0391.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0392.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0393.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0394.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0395.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0396.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0397.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0398.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0399.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0400.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0401.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0402.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0403.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0404.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0405.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0406.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0407.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0408.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0409.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0410.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0411.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0412.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0413.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0414.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0415.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0416.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0417.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0418.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0419.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0420.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0421.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0422.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0423.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0424.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0425.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0426.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0427.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0428.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0429.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0430.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0431.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0432.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0433.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0434.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0435.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0436.mp4
> │      ├── 📄 20251220_C02_VIDEO_D0437.mp4
> │      ├── 📄 20251220_C02_VIDEO_D0438.mp4
> │      ├── 📄 Photo_Video_DB.csv
> │      ├── 📄 Photo_Video_DB_2ddf84a04402819ea365d894c16a3fdf_all.csv
> │      ├── 📄 _02_VIDEO.md
> │    └── 📂 03_DOCUMENTS/
> │      └── 📂 04_CORRESPONDENCE/
> │        ├── 📄 _04_CORRESPONDENCE.md
> │      ├── 📄 20241209_C02_FCFCU_VIDEO_D0071.pdf
> │      ├── 📄 20241211_C02_FCFCU_VIDEO_D0072.pdf
> │      ├── 📄 20260203_C00_DOC_D0476.pdf
> │      ├── 📄 20260207_C00_DOC_D0464.pdf
> │      ├── 📄 POST_INCIDENT_CONDITION_SUMMARY.md
> │      ├── 📄 _03_DOCUMENTS.md
> │    └── 📂 04_FINANCIAL/
> │      ├── 📄 20260203_C00_LSTRM_INV_D0492.pdf
> │      ├── 📄 20260203_C00_LSTRM_INV_D0521.pdf
> │      ├── 📄 20260203_C00_LSTRM_INV_D0522.pdf
> │      ├── 📄 20260203_C00_LSTRM_INV_D0523.pdf
> │      ├── 📄 Financial.csv
> │      ├── 📄 Financial_2cef84a044028021905ff6d8938abe93_all.csv
> │      ├── 📄 Financial_Tracker.md
> │      ├── 📄 Food_Purchase.md
> │      ├── 📄 Food_Purchase_(1).md
> │      ├── 📄 Food_Purchase_1.md
> │      ├── 📄 Food_Purchase_2.md
> │      ├── 📄 Food_Purchase_3.md
> │      ├── 📄 Food_Purchase_4.md
> │      ├── 📄 Gas_For_Lyft.md
> │      ├── 📄 Gas_Purchase_For_Lyft.md
> │      ├── 📄 Pet_Needs.md
> │      ├── 📄 _04_FINANCIAL.md
> │    └── 📂 05_EXPORTS/
> │      ├── 📄 EX_V_09_31_20251209_1018_mp4_—_OFFICER_POSITIONE.md
> │      ├── 📄 EX_V_09_46_20251209_1033_mp4_—_POST_REMOVAL_ENTR.md
> │      ├── 📄 _05_EXPORTS.md
> │      └── 📂 events/
> │        ├── 📄 025_12_09_Removal_Day_Camera_Bedroom.md
> │        ├── 📄 20250109_order_Court_Orders_And_Hearing_Schedule.md
> │        ├── 📄 20250109_order_Order_Court_Orders_And_Hearing_Sc.md
> │        ├── 📄 20250116_Case_Filed.md
> │        ├── 📄 20250116_court_filing_Case_Filed.md
> │        ├── 📄 20250303_Service_Issued.md
> │        ├── 📄 20250305_Service_Attempt_1.md
> │        ├── 📄 20250305_motion_Motion_Motion_Motion_To_Vacate_V.md
> │        ├── 📄 20250305_motion_Motion_Motion_To_Vacate_Void_Jud.md
> │        ├── 📄 20250305_motion_Motion_To_Vacate_Void_Judgement.md
> │        ├── 📄 20250409_service_Service_Attempt_2.md
> │        ├── 📄 20250415_Service_Attempt_2.md
> │        ├── 📄 20250513_Motion_for_Default_Judgment.md
> │        ├── 📄 20250513_motion_Motion_For_Default_Judgment.md
> │        ├── 📄 20250613_document_Sheriff_Sale_Notice_Posted.md
> │        ├── 📄 20250709_Sheriff_Sale_Notice_Posted.md
> │        ├── 📄 20250717_Plaintiff_Bid_Filed.md
> │        ├── 📄 20250805_document_030_Report_Sheriff_Sale_No_Exc.md
> │        ├── 📄 20250815_enforcement_Writ_Of_Assistance_Issued.md
> │        ├── 📄 20251126_Sheriff_At_Home_Unrelated_No_Notice.md
> │        ├── 📄 20251203_Police_Knocked_Then_Left_Quickly.md
> │        ├── 📄 20251207_Retrieval_Day.md
> │        ├── 📄 20251209_1033_Post_Removal_Entry_Privacy_Violati.md
> │        ├── 📄 20251209_1046_Camera_System_Manipulation.md
> │        ├── 📄 20251209_1048_Refrigerator_Unplugged.md
> │        ├── 📄 20251209_Removal_Day_Photos.md
> │        ├── 📄 20251214_Other_Camera_Porch_Activity.md
> │        ├── 📄 20251216_AES_Emergency_Notice.md
> │        ├── 📄 20251216_Emergency_Supplemental_Declaration_File.md
> │        ├── 📄 20251221_DOJ_Civil_Rights_Complaint_Submitted.md
> │        ├── 📄 EX_V_09_29_20251209_1016_mp4_—_SHERIFF_INSIDE_BE.md
> │        ├── 📄 EX_V_09_32_20251209_1019_mp4_—_CONTINUED_INTERFE.md
> │        ├── 📄 EX_V_09_33_20251209_1020_mp4_—_ROOM_VACANT_(BASE.md
> │        ├── 📄 EX_V_09_47_20251209_1034_mp4_—_ABSENCE_FROM_ROOM.md
> │        ├── 📄 EX_V_09_59_20251209_1046_mp4_—_RE_ENTRY_AND_CAME.md
> │        ├── 📄 EX_V_09_60_20251209_1047_mp4_—_ELECTRONICS_AND_C.md
> │        ├── 📄 EX_V_09_61_20251209_1048_mp4_—_REFRIGERATOR_UNPL.md
> │        ├── 📄 NT_Video_Narration_Log_Removal_Day.md
> │        ├── 📄 _checklist.md
> │        ├── 📄 _events.md
> │    ├── 📄 20260202_CAPTURE_Auto_Save_D0558.html
> │    ├── 📄 _03_EVIDENCE.md
> │    ├── 📄 _C04_Writ_Removal.md
> │  └── 📂 C-05_Civil_Rights/
> │    └── 📂 01_FILED/
> │      ├── 📄 _01_FILED (2).md
> │      ├── 📄 _01_FILED.md
> │    └── 📂 01_PHOTOS/
> │      ├── 📄 _01_PHOTOS.md
> │    └── 📂 02_VIDEO/
> │      ├── 📄 _02_VIDEO.md
> │    └── 📂 03_DOCUMENTS/
> │      ├── 📄 _03_DOCUMENTS.md
> │    └── 📂 03_EVIDENCE/
> │      └── 📂 01_PHOTOS/
> │        ├── 📄 _01_PHOTOS.md
> │      └── 📂 02_VIDEO/
> │        ├── 📄 _02_VIDEO.md
> │      └── 📂 03_DOCUMENTS/
> │        └── 📂 04_CORRESPONDENCE/
> │          ├── 📄 20230920_C00_DOC_D0074.pdf
> │          ├── 📄 20240320_C00_FCFCU_DOC_D0075.pdf
> │          ├── 📄 20251210_C00_DOC_D0050.pdf
> │          ├── 📄 20260101_C00_FCFCU_DOC_D0070.pdf
> │          ├── 📄 20260118_C02_PHOTO_D0481.jpeg
> │          ├── 📄 20260207_C00_DOC_D0142.pdf
> │          ├── 📄 _04_CORRESPONDENCE.md
> │        ├── 📄 20230920_FCFCU_Hardship_Health_Notice_Delivery.md
> │        ├── 📄 20251216_AES_Emergency_Notice.md
> │        ├── 📄 _03_DOCUMENTS.md
> │      └── 📂 04_FINANCIAL/
> │        ├── 📄 _04_FINANCIAL.md
> │      └── 📂 05_EXPORTS/
> │        ├── 📄 _05_EXPORTS.md
> │      ├── 📄 _03_EVIDENCE.md
> │    └── 📂 04_FINANCIAL/
> │      ├── 📄 _04_FINANCIAL.md
> │    └── 📂 05_EXPORTS/
> │      ├── 📄 _05_EXPORTS.md
> │    └── 📂 05_LOGS/
> │      ├── 📄 20260210_REPORT_AI_Analysis_Grok_1.pdf
> │      ├── 📄 _05_LOGS.md
> │      ├── 📄 grok_report.pdf
> │    ├── 📄 20260202_CAPTURE_Auto_Save_D0565.html
> │    ├── 📄 20260202_CAPTURE_Auto_Save_D0566.html
> │    ├── 📄 _03_EVIDENCE.md
> │    ├── 📄 _C05_State_Action_Liability.md
> │    ├── 📄 _C06_ADA_Disability_Access.md
> │    ├── 📄 _C08_Regulatory.md
> │    ├── 📄 cfpb_consumer_reporting_companies_list_2025.csv
> │  └── 📂 C-06_Settlement_Narrative_Control/
> │    └── 📂 FCFCU_Guides_Website/
> │      ├── 📄 20260203_C00_FCFCU_DOC_D0092.pdf
> │      ├── 📄 20260203_C00_FCFCU_DOC_D0093.pdf
> │      ├── 📄 _FCFCU_Guides_Website.md
> │    └── 📂 FCFCU_Website_Exports/
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0080.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0081.pdf
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0082.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0083.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0084.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0085.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0086.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0087.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0088.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0089.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0090.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0091.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0094.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0095.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0096.pdf
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0097.pdf
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0098.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0099.pdf
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0100.pdf
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0101.mhtml
> │      ├── 📄 _FCFCU_Website_Exports.md
> │    ├── 📄 _C09_Settlement_Resolution.md
> │    ├── 📄 _C10_Narrative_Control.md
> │  ├── 📄 _99_VAULT.md
> │  ├── 📄 dump_tree_with_ocr.py
> └── 📄 _content.md
> ```

### Assistant
> ```text
> You are working inside the repo under /content. Your job is to FINISH organizing + cleaning this repo so the next step is easy: (1) publish/binder output, (2) reliable “source of truth” tables, and (3) consistent cross-links between master tables ⇄ events ⇄ phases ⇄ evidence.
> 
> NON-NEGOTIABLE GOALS
> - Single spine of truth: the FCFCU_CASE_MASTER CSV set (0_master, 0_docket, 1_phases, 2_violations, 3_events, 4_docs, 5_disputes, 6_damages, 7_actors) is canonical. Everything else is supporting material.
> - No duplicate “same thing” files living in multiple places without a pointer + reason.
> - Naming is strict: YYYY-MM-DD_* for dated narrative/event docs. No spaces in filenames where avoidable; use underscores. (Keep existing names if already referenced heavily; add redirects instead.)
> - Every Phase folder must have: _PHASE_OVERVIEW.md + links to its key artifacts + its evidence vault pointer.
> - Every Event doc must have frontmatter with at least: id, date, type, phase, actors, entities, related_docs, related_violations.
> - Evidence lives in 99_VAULT, content holds “clean narratives + indices + outputs.” Do not mix.
> 
> WHAT YOU MUST PRODUCE (deliverables)
> 1) A clear repo “north star” README at /content/README.md:
>    - What this repo is
>    - Where the source-of-truth tables are
>    - How to add a new event
>    - How to add a new doc/evidence item
>    - How to generate/publish outputs
> 2) A cleanup plan executed as commits:
>    - move/rename files
>    - remove obvious duplicates (or replace with pointer stubs)
>    - create missing index files
> 3) A deterministic index layer:
>    - /content/index.md (top-level clickable map)
>    - /content/01_PHASES/_PHASES_MASTER.md updated with links
>    - /content/03_EVENTS/index.md updated + consistent year sub-indexes
>    - /content/99_VAULT/_TOC.md updated (or created)
> 4) A “NEXT STEP READY” state:
>    - /content/04_DOCUMENTS should be only finalized outward-facing documents + a _drafts/ area
>    - /content/04_DOCUMENTS/analysis and “auto_save canvas” files should be moved to /content/90_ADMIN/analysis (or /content/90_ADMIN/_intake) unless explicitly final
> 5) A scripts/tools sanity pass:
>    - One tools folder only (prefer /content/90_ADMIN/tools OR /content/tools — choose ONE and consolidate)
>    - Deduplicate script versions (v1/v2/v3) by selecting the best and archiving the rest under /content/90_ADMIN/_archive/tools/
>    - Add a single entry script: /content/tools/run_pipeline.md (or .py) that documents how to run: dedupe → indexes → exports.
> 
> REPO CLEANUP RULES (how to decide moves)
> - If it’s evidence (pdf, photo, video, raw exports): it belongs in /content/99_VAULT/… (phase-specific)
> - If it’s a narrative, analysis memo, or a clean writeup: it belongs in /content/01_PHASES or /content/04_DOCUMENTS (final only)
> - If it’s “auto_save”, scratch, canvas dumps, transcript exports: it belongs in /content/90_ADMIN/analysis or /content/90_ADMIN/_intake, NOT in final trees
> - If you find duplicates like:
>   - “20230920_FCFCU_Hardship_and_Health_Notice_Let.md” vs “2023-09-20_FCFCU_Hardship_and_Health_Notice_Letter.md”
>   Keep ONE canonical name, and replace the other with a stub file that points to canonical (do not break inbound links without leaving breadcrumbs).
> 
> FOCUS AREAS (based on the tree shown)
> A) Consolidate /content/04_DOCUMENTS
> - Create: /content/04_DOCUMENTS/_drafts (already exists) and /content/04_DOCUMENTS/_final
> - Move clearly-final html letters into _final
> - Move “analysis/00_Strategy/*.canvas” into /content/90_ADMIN/analysis/00_Strategy
> - Move “Ouput.txt” (typo) to /content/90_ADMIN/_intake/output.txt (or delete if redundant)
> - Ensure /content/04_DOCUMENTS/docs.md becomes an index, not a junk drawer
> 
> B) Normalize /content/03_EVENTS
> - Enforce one filename convention:
>   - YYYY-MM-DD_<short_title>.md (dash date, underscores title)
> - For duplicates: pick the best-named canonical, create stub pointer for the other.
> - Update /content/03_EVENTS/Timeline_Inventory.csv if it’s meant to mirror 3_events.csv; otherwise move it to /content/90_ADMIN/analysis
> 
> C) Align /content/01_PHASES with evidence vault
> - For each C-0X phase:
>   - ensure _PHASE_OVERVIEW.md exists + links to:
>     - canonical phase row in 1_phases.csv (by id)
>     - key memos
>     - key evidence vault location (/content/99_VAULT/C-0X_…)
> - Ensure C-05 and C-06 legacy folders don’t contain active files. Move active to main, keep legacy as archive with a clear note.
> 
> D) Fix “empty” tables/folders
> - /content/08_ENTITIES appears empty: create FCFCU_CASE_MASTER - 8_entities.csv OR a stub _README explaining entities are in 0_master/7_actors until created.
> - Ensure 07_ACTORS has a readable index markdown.
> 
> OUTPUTS YOU SHOULD ADD
> - /content/90_ADMIN/CHANGELOG.md (human readable)
> - /content/90_ADMIN/_archive/ (for old versions, deprecated drafts, and duplicate scripts)
> - /content/90_ADMIN/QA_CHECKLIST.md (quick verification steps)
> 
> QUALITY GATES (must pass before finishing)
> - `rg -n "Auto_Save|Ouput.txt|dump_tree_with_ocr.py"` shows they live only under /90_ADMIN or /tools, not scattered
> - No phase folder missing _PHASE_OVERVIEW.md
> - /content/index.md links to: Case Master, Phases, Events, Violations, Disputes, Damages, Actors, Vault, Admin
> - Every stub pointer file clearly says “Moved to …” and includes the new relative path.
> - Git diff is cleanly separated into 2–5 commits: (1) structure/indexes, (2) moves/renames, (3) script consolidation, (4) docs/readme, (5) final QA fixes.
> 
> EXECUTION INSTRUCTIONS
> 1) Create a new branch: `chore/repo-cleanup-nextstep`
> 2) Inventory:
>    - Find duplicates by title/date
>    - Find “auto_save/canvas” clusters
>    - Find scripts with versions
> 3) Apply moves + create stub pointers
> 4) Create/refresh indexes + README
> 5) Run quick QA searches (ripgrep) and fix stragglers
> 6) Commit with clear messages
> 7) Output a short summary of what changed + where “next step” begins.
> 
> Start now. Don’t ask me questions unless you hit a hard ambiguity that blocks a move. Prefer making a reasonable decision and documenting it in CHANGELOG.md.
> ```

### User
> i also have this app folder and we have a case rag and mk material docs and paperless that we need to get all hooked up first of course is the docs so i can view on my phone online and then the case rag and paperless for ingestion into teh rag. ---
> uid: b675a161-3ec4-4a9a-884a-5ba448e6ec80
> ---
> ```markdown
> . 📂 app
> └── 📂 case_rag/
> │  ├── 📄 _90_PIPELINE.md
> │  └── 📂 config/
> │    ├── 📄 ingest_rules.yaml
> │    ├── 📄 sources.yaml
> │  └── 📂 data/
> │    └── 📂 extracted_text/
> │      ├── 📄 00_CASE_MANAGEMENT_10_Case_Master_01_CASE_MASTER.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_10_Case_Master_03_CASE_TASKS.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_10_Case_Master_04_CASE_VIOLATIONS.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_10_Case_Master_05_CASE_VALUATION_INTERNAL.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_20_Trackers_10_Harm_Tracker.csv.txt
> │      ├── 📄 00_CASE_MANAGEMENT_20_Trackers_NT_Forensic_Accounting_Audit_Summary.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_20_Trackers_authority.csv.txt
> │      ├── 📄 00_CASE_MANAGEMENT_20_Trackers_docket.csv.txt
> │      ├── 📄 00_CASE_MANAGEMENT_20_Trackers_financial.csv.txt
> │      ├── 📄 00_CASE_MANAGEMENT_20_Trackers_strategy.csv.txt
> │      ├── 📄 00_CASE_MANAGEMENT_20_Trackers_tasks.csv.txt
> │      ├── 📄 00_CASE_MANAGEMENT_20_Trackers_violations.csv.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_10_motions__10_motions.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_10_motions__emergency_stay_of_writ.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_10_motions__vacate_void_judgment.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_20_affidavits_TPL_Affidavit_ADA_Disability.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_20_affidavits_TPL_Affidavit_Character.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_20_affidavits_TPL_Affidavit_Community_Service.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_20_affidavits_TPL_Affidavit_Credibility.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_20_affidavits_TPL_Affidavit_Language_Updates.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_20_affidavits_TPL_Affidavit_Observations.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_20_affidavits_TPL_Affidavit_Verified_Defendant.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_20_affidavits_TPL_Declaration_Gender_Identity_Clarification.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_20_affidavits__20_affidavits.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_20_affidavits__GUIDE_Witness_Instructions.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_40_exhibits__40_exhibits.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_40_exhibits__Exhibits_Lists.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_50_orders__50_orders.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_50_orders__Proposed_Order.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_50_orders__proposed_order_emergency_stay.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_50_orders__proposed_order_motion_to_vacate.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_60_packets_2026-01-19_attorney_intake_packet_executive.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_60_packets_TPL_ADA_Packet.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_60_packets_TPL_Handup_Packet_Note.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_60_packets__60_packets.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_70_outreach_TPL_Advocate_Outreach.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_70_outreach_TPL_Attorney_Brief.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_70_outreach__70_outreach.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_80_binders_TPL_Binder_Section_Cover.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_80_binders_TPL_Binder_Section_Index.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_80_binders__80_binders.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_90_internal__Court_Doc.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_99_Templates_90_internal__settlement_letter_draft.md.txt
> │      ├── 📄 00_CASE_MANAGEMENT_PHASE_00_Case_Management.md.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_001_2025-01-16_Appearance.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_002_2025-01-16_Appearance_2.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_003_2025-01-16_Complaint.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_004_2025-01-16_Notice_to_Homeowners.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_005_2025-01-16_Request_for_Admissions.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_006_2025-01-16_Summons_1.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_007_2025-01-16_Summons_2.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_008_2025-01-16_Summons_3.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_009_2025-01-16_Summons_4.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_010_2025-01-16_Summons_5.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_011_2025-03-05_Service_Returned_Served.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_012_2025-04-15_Service_Returned_Served.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_013_2025-05-13_Affidavit.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_014_2025-05-13_Affidavit_Attorney_Fees.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_015_2025-05-13_Motion_for_Default_Judgment.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_016_2025-05-21_Notice_Omitted_Service.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_017_2025-05-21_Omitted_Notice_of_Service_Report.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_018_2025-05-21_Order_Denying_Default.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_019_2025-05-23_Motion_Amended_Default_1.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_020_2025-05-23_Motion_Amended_Default_2.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_021_2025-05-23_Order_Default_Judgment.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_022_2025-05-30_Praecipe_Sheriff_Sale_1.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_023_2025-05-30_Praecipe_Sheriff_Sale_2.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_024_2025-07-09_Service_Returned_Served_Sheriff.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_025_2025-07-17_Notice_Plaintiffs_Bid.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_026_2025-09-09_Decree_Foreclosure_Returned.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_027_2025-10-29_Petition_Writ_of_Assistance.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_028_2025-10-29_Writ_of_Assistance_Document.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_029_2025-11-06_Order_Writ_of_Assistance.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_030_2025-12-10_Combined_Exhibits_A-H.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_031_2025-12-10_Exhibit_F_Affidavit.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_032_2025-12-10_Exhibit_G1_ADA_Notice.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_034_2025-12-10_Exhibit_H_Declaration.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_035_2025-12-10_motion_vacate.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_036_2025-12-11_Denial_stay_writ.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_037_2025-12-11_Exhibit_List_A-G.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_038_2025-12-11_Hearing_Set_Proposed_Order_Vacate.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_039_2025-12-11_Motion_Vacate_Judgment.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_040_2025-12-11_Proposed_Order_Stay.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_041_2025-12-11_Supplemental_Emergency_Motion.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_042_2025-12-12_Report_to_Court.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_043_2025-12-12_Supplemental_Emergency_Motion.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_044_2025-12-16_Emergency_Supplemental_Declaration.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_045_2025-12-17_Report_Sheriff_Sale_No_Excess.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_046_2025-12-22_ADA_Disability_Affidavit.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_047_2025-12-22_Declaration_Ongoing_D.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_048_2026-01-09_Appearance_Plaintiff.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD_049_2026-01-20_Order_from_1_9_26_hearing.pdf.txt
> │      ├── 📄 01_RECORDS_10_COURT_RECORD__10_Docket.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Appraisal_21June-24-4817Shadow_Appraisal.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Appraisal__Appraisal.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Emails_2024-12-09_outgoing_email_bank_access_request.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Emails_2024-12-11_outgoing_email_bank_access_request.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Emails_FCFCU_v_CR-V_Report_to_Court.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Emails__Emails.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Letters_2023-09-20_FCFCU_Hardship_Health_Notice_Delivery.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Letters_2023-09-20_FCFCU_Hardship_and_Health_Notice_Le.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Letters_2024-03-20_FCFCU_Certified_Response_Tax_Record.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Letters_Formal_Retrieval_Protocol_ADA.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Letters__Letters.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Payments__Payments.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Reports__Reports.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_About Financial Center - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Careers & Culture - Financial Center.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Credit Union vs. Bank - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Financial Center Announces CEO Retirement and Appointment of Interim Leadership - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Financial Center Celebrates Laura Mirabal’s Selection to the 2025 Indiana Latino Leadership Circle - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Financial Center Completes Merger with Indianapolis Post Office Credit Union - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Financial Center Expands to Hancock County with $1.5M McCordsville Branch - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Financial Center First Credit Union Selects Ning Duong as New CEO - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Financial Center First Credit Union and Indianapolis Post Office Credit Union Announce Plans to Merge - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Financial Center Leads the Way in AI-Powered Translations with New Traduality Partnership - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Financial Center Recognized with 2025 MeridianLink Arc Award for Impactful Use of Technology in Financial Services - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Financial Center and Indianapolis Post Office Credit Union to Merge May 1 - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Financial_Center_-_Home_Equity_Line_of_Credit.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Financial_Center_-_Home_Equity_Loan.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Home Equity Loans & Lines of Credit - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Mortgage_-_Common_Mistakes.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Mortgage_-_Refinancing.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Mortgages - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_News Releases - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_News Releases - Financial Center.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Open Positions - Financial Center.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu_Site_Content_Privacy Policy - Financial Center.mhtml.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_10_fcfcu__10_fcfcu.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_20_aes_2025-06-08_AES_ADA_Notice.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_20_aes_2025-12-16_AES_Emergency_Notice.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_20_aes__20_aes.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors_40_Others_Manager_Response_Acknowledge_Form-1769543600128.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_10_actors__20_actors.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_10_photos_video_NT_Video_Narration_Log_Removal_Day.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_10_photos_video__10_photos_video.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_20_parcel_DLGF_ Tax Bill Search.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_20_parcel_Marion County, IN, Estimated 2025 Taxes 6016506.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_20_parcel_MyTitle.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_20_parcel_Parcel_6016506_PRC 1.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_20_parcel_Parcel_6016506_PRC.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_20_parcel_Parcel_6016506_ParcelDetailHistory 1.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_20_parcel_Parcel_6016506_ParcelDetailHistory.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_20_parcel__20_parcel.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_20_parcel_f588fab6-f89f-41c3-bfce-05ad0d108a06.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_20_parcel_indy_pvdnet_document (1).pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_20_parcel_indy_pvdnet_document.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_30_declarations__30_declarations.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_40_affidavits__40_affidavits.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_40_affidavits_ada-disability__ada-disability.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_40_affidavits_character__character.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_40_affidavits_community-service__community-service.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_40_affidavits_credibility__credibility.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_40_affidavits_observations__observations.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_60_credit_10_Chase_Report_2025-07.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_60_credit_20_Chase_Inquiry_Summary.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_60_credit_30_Full_TriMerge_2025-12.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_60_credit_Experian - Access your credit report--2.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_60_credit_Experian - Access your credit report-CH13.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_70_Financial_10_AES_Statement_2025-08.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_70_Financial_13312381_invoice.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_70_Financial_13312462_invoice.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting_70_Financial_13312465_invoice.pdf.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_20_supporting__30_supporting.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW_Service_Log.md.txt
> │      ├── 📄 01_RECORDS_20_EVIDENCE_RAW__20_evidence.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_10_Motions_MO_motion_emergency_stay_of_writ.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_10_Motions_MO_motion_emergency_supplemental_motion_ongoing_ha.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_10_Motions_MO_motion_to_vacate_void_judgment.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_10_Motions_MO_proposed_order_motion_to_vacate.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_10_Motions__30_motions.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_20_Orders_OR_03_order_vacate_proposed.pdf.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_20_Orders_OR_04_order_stay_writ_proposed.pdf.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_20_Orders__40_orders.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_30_Hearings_10_Void_Judgment_Hearing_2026-01-09_10_Binder_User_Copy.pdf.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_30_Hearings_10_Void_Judgment_Hearing_2026-01-09_10_Hearing_Assets_COURT_MODE_BUTTONS.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_30_Hearings_10_Void_Judgment_Hearing_2026-01-09_10_Hearing_Assets_HEARING_Cheat_Sheet.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_30_Hearings_10_Void_Judgment_Hearing_2026-01-09_10_Hearing_Assets__COURT_MODE_PLAYBOOK.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_30_Hearings_10_Void_Judgment_Hearing_2026-01-09_20_Binder_Judge_Copy.pdf.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_30_Hearings_10_Void_Judgment_Hearing_2026-01-09_30_Binder_Opposing_Copy.pdf.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_30_Hearings_10_Void_Judgment_Hearing_2026-01-09_40_Binder_Complete.pdf.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_30_Hearings_10_Void_Judgment_Hearing_2026-01-09__Hearing_Void_Judgment_2026-01-09.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_40_Envelopes_and_Receipts_10_2025-12-10_motion_vacate_10_ENV_Receipt_37288599.pdf.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_40_Envelopes_and_Receipts_10_2025-12-10_motion_vacate_20_ENV_Receipt_Odyssey.pdf.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_40_Envelopes_and_Receipts_10_2025-12-10_motion_vacate_99_Combined_Submission_Full.pdf.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_40_Envelopes_and_Receipts_10_2025-12-10_motion_vacate__10_2025-12-10_motion_vacate.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_40_Envelopes_and_Receipts_20_2025-12-11_Supplemental_Emergency_Motion_Access_10_Supplemental_Emergency_Motion_Draft.pdf.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_40_Envelopes_and_Receipts_20_2025-12-11_Supplemental_Emergency_Motion_Access__20_2025-12-11_Supplemental_Emergency_Motion_Access.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT_40_Envelopes_and_Receipts__90_Filed_Envelopes.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT__01_PHASE_FORECLOSURE_COURT.md.txt
> │      ├── 📄 02_PHASE_WORK_01_PHASE_FORECLOSURE_COURT__TOC_.md.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_01_PHASE_PRESERVATION_MASTER.md.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_10_Ledgers_20_Spoliation_Risk_Ledger.md.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_10_Ledgers__10_Ledgers_Index.md.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_20_Notices_and_Sends_10_letters_01_2026-02-01_Signed_Preservation_Notice.pdf.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_20_Notices_and_Sends_10_letters_02_2026-02-03_Second_Notice_Cover.html.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_20_Notices_and_Sends_10_letters_03_Litigation_Hold_FollowUp_Draft.html.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_20_Notices_and_Sends_10_letters__10_letters.md.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_20_Notices_and_Sends_20_Emails_01_2026-01-31_Email_Service_Record_1.pdf.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_20_Notices_and_Sends_20_Emails_02_2026-01-31_Email_Service_Record_2.pdf.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_20_Notices_and_Sends_20_Emails__20_Emails.md.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_20_Notices_and_Sends_30_Packet_01_2026-02-03_Preservation_Packet_Final_Certified.pdf.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_20_Notices_and_Sends_30_Packet_02_2026-02-03_Preservation_Packet_Final_FirstClass.pdf.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_20_Notices_and_Sends_30_Packet_11_2026-02-03_Invoice_Certified_Mail.pdf.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_20_Notices_and_Sends_30_Packet_12_2026-02-03_Invoice_First_Class_Mail.pdf.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_20_Notices_and_Sends_30_Packet_13_2026-02-03_Payment_Receipt_LetterStream.pdf.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_20_Notices_and_Sends_30_Packet__30_Packet.md.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_20_Notices_and_Sends__20_Notices_Index.md.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_30_Responses_and_Receipts_01_2026-02-01_MCSO_Email_Receipt.pdf.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION_30_Responses_and_Receipts__30_Responses_Index.md.txt
> │      ├── 📄 02_PHASE_WORK_02_PHASE_PRESERVATION__TOC_.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_01_PHASE_CREDIT_FCRA_MASTER.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_10_Send_Queue_Consumer_Statement_Landlords.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_10_Send_Queue_Core_Credit_Tables.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_10_Send_Queue_Execution_Checklist.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_10_Send_Queue_Housing_Emergency_Affidavit.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_10_Send_Queue_Landlord_Clarification_Statement.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_10_Send_Queue_Landlord_Explanation_Letter.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_10_Send_Queue_Landlord_Statement.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_10_Send_Queue_PHASE_CREDIT_EXECUTION_MAP.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_10_Send_Queue_Sanctions_Readiness_Memo.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_20_furnisher_disputes_13312462_tmp.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_20_furnisher_disputes_13312465_tmp.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_20_furnisher_disputes_2026-02-03_BASIS OF DISPUTE (NON-CURABLE DEFECTS).pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_20_furnisher_disputes_2026-02-03_FCFCU_Furnisher_Deletion_Demand_FINAL.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_20_furnisher_disputes_CFPB_Complaint_Draft.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_20_furnisher_disputes__20_furnisher_disputes.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_Equifax_13312381_tmp.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_Equifax_2026-02-02_Equifax_Dispute_Letter.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_Equifax_Call Customer Care.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_Equifax_Equifax_Violation_Excerpt.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_Equifax__Equifax.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_Experian_2026-02-02_Experian_Dispute_Letter.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_Experian_Experian - Access your credit report.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_Experian_Experian - Dispute Cart.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_Experian_Experian - Dispute Cart2.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_Experian_Experian_Violation_Excerpt.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_Experian__Experian.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_TransUnion_2026-02-02_TransUnion_Dispute_Letter.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_TransUnion_Gmail - Dispute Received, Investigation in Process.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_TransUnion_TransUnion_Violation_Excerpt.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes_TransUnion__TransUnion.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_30_bureau_disputes__30_bureau_disputes.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_40_Utility_Disputes_AES_2026-02-03_AES_Utility_Dispute.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_40_Utility_Disputes_AES_Utility Dispute (AES Indiana) - Cody Rice-Velasquez.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_40_Utility_Disputes_AES_Utility Dispute (Citizens Water) - Cody Rice-Velasquez.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_40_Utility_Disputes_AES_Utility Dispute (Code Enforcement) - Cody Rice-Velasquez.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_40_Utility_Disputes_Citizens_2026-02-03_Citizens_Utility_Dispute.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_40_Utility_Disputes_Local_Code_2026-02-03_Code_Enforcement_Dispute.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_40_Utility_Disputes__40_utilities.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_50_CFPB_01_Combined_Narrative_and_Excerpt.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_50_CFPB_99_Legacy_Excerpt.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_50_CFPB_CFPB_Violation_Excerpt_Master.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_50_CFPB_Cover_Letter.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_50_CFPB__20_CFPB.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_65_Court_Transcripts_Requests_4-018222 - Circuit and Superior Courts of Marion County, Indiana.mhtml.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_65_Court_Transcripts_Requests_Estimate_4-018222.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_65_Court_Transcripts_Requests_MarionCountyAudioRequestAuthorization_20260203_49D03-2501-MF-002559.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_65_Court_Transcripts_Requests_Your order has been submitted successfully.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_65_Court_Transcripts_Requests_request for recording.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_70_Credit_Data_Extraction_10_Chase_Report_2025-07_tradelines.csv.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_70_Credit_Data_Extraction_20_Chase_Inquiry_Summary_tradelines.csv.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_70_Credit_Data_Extraction_30_Full_TriMerge_2025-12_tradelines.csv.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_70_Credit_Data_Extraction_Experian - Access your credit report--2_tradelines.csv.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_70_Credit_Data_Extraction_Experian - Access your credit report-CH13_tradelines.csv.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_80_Credit_Damages_Emergency_Credit_Harm_Addendum.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_80_Credit_Damages__70_damages.md.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_95_Supporting_Docs_Affidavits_exhibit_b_harm_addendum.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_95_Supporting_Docs_Affidavits_exhibit_c_affidavit_emergency 1.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_95_Supporting_Docs_Affidavits_exhibit_c_affidavit_emergency.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_95_Supporting_Docs_Affidavits_index.html.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_95_Supporting_Docs_PROOF_OF_ADDRESS.pdf.txt
> │      ├── 📄 02_PHASE_WORK_03_PHASE_CREDIT_FCRA_95_Supporting_Docs_identity_verification_letter_mission-lane-cc.pdf.txt
> │      ├── 📄 02_PHASE_WORK_05_PHASE_LITIGATION_00_Intake_NT_Attorney_Intake_Summary.md.txt
> │      ├── 📄 02_PHASE_WORK_05_PHASE_LITIGATION_00_Intake__00_Intake.md.txt
> │      ├── 📄 02_PHASE_WORK_05_PHASE_LITIGATION_30_demand_letters__30_demand_letters.md.txt
> │      ├── 📄 02_PHASE_WORK_05_PHASE_LITIGATION_40_opposing_counsel__40_opposing_counsel.md.txt
> │      ├── 📄 02_PHASE_WORK_05_PHASE_LITIGATION_50_draft_pleadings__50_draft_pleadings.md.txt
> │      ├── 📄 02_PHASE_WORK_05_PHASE_LITIGATION_60_output_10_filings__10_filings.md.txt
> │      ├── 📄 02_PHASE_WORK_05_PHASE_LITIGATION_60_output_20_orders__20_orders.md.txt
> │      ├── 📄 02_PHASE_WORK_05_PHASE_LITIGATION_60_output_30_packets__30_packets.md.txt
> │      ├── 📄 02_PHASE_WORK_05_PHASE_LITIGATION_60_output_40_motions__40_motions.md.txt
> │      ├── 📄 02_PHASE_WORK_05_PHASE_LITIGATION_60_output_50_letters__50_letters.md.txt
> │      ├── 📄 02_PHASE_WORK_05_PHASE_LITIGATION_60_output__60_output.md.txt
> │      ├── 📄 02_PHASE_WORK_05_PHASE_LITIGATION_70_hearings__70_hearings.md.txt
> │      ├── 📄 02_PHASE_WORK_05_PHASE_LITIGATION_PHASE_05_Litigation.md.txt
> │      ├── 📄 02_PHASE_WORK_06_PHASE_MEDIA_INQUIRIES_2025-12-15_displacement_cold_exposure.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_01_COMPLAINT_PACKET_CHECKLIST.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_01_PHASE_REGULATORS_MASTER.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_10_Industry_10_BBB_01_Combined_Narrative_and_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_10_Industry_10_BBB_BBB_Violation_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_10_Industry_10_BBB_Cover_Letter.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_10_Industry_10_BBB_Exhibit_Manifest.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_10_Industry_10_BBB__BBB.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_10_Industry__10_Industry.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_20_Local_35_Sheriff_Oversight_Cover_Letter.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_20_Local_35_Sheriff_Oversight_MANIFEST_Sheriff_Oversight_Packet.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_20_Local_35_Sheriff_Oversight_Marion_County_Sheriff_Oversight_Violation_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_20_Local_35_Sheriff_Oversight_Sheriff_Internal_Affairs_Complaint.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_20_Local_35_Sheriff_Oversight_Sheriff_Violation_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_20_Local_35_Sheriff_Oversight__35_Sheriff_Oversight.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_20_Local_City_of_Indy_Violation_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_20_Local__20_Local.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_10_IN_AG_Cover_Letter.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_10_IN_AG_IN_AG_Violation_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_10_IN_AG_Indiana_AG_Complaint_Narrative.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_10_IN_AG_MANIFEST_IN_AG_Complaint_Packet.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_10_IN_AG__20_AG_Indiana.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_20_IN_DFI_Cover_Letter.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_20_IN_DFI_IN_DFI_Violation_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_20_IN_DFI_Indiana_DFI_Complaint_Narrative.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_20_IN_DFI_Indiana_Department_of_Financial_Institutions_DFI_Violation_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_20_IN_DFI_MANIFEST_Indiana_DFI_Packet.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_20_IN_DFI__25_IN_DFI.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_30_IN_Civil_Rights_99_Legacy_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_30_IN_Civil_Rights_Cover_Letter.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_30_IN_Civil_Rights_Indiana_Civil_Rights_Commission_Violation_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_30_IN_Civil_Rights_Indiana_Civil_Rights_Complaint_Narrative.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_30_IN_Civil_Rights_MANIFEST_ICRC_Complaint_Packet.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_30_IN_Civil_Rights__55_IN_Civil_Rights.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State__30_State.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_30_State_icrc_civil_rights.html.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_10_NCUA_01_Combined_Narrative_and_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_10_NCUA_99_Legacy_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_10_NCUA_Cover_Letter.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_10_NCUA_Exhibit_Manifest.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_10_NCUA_MANIFEST_NCUA_Complaint_Packet.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_10_NCUA__30_NCUA.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_10_NCUA_ncua_complaint.html.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_20_DOJ_99_Legacy_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_20_DOJ_Cover_Letter_DOJ_Supplemental.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_20_DOJ_DOJ_Civil_Rights_Violation_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_20_DOJ_DOJ_Civil_Rights_Violation_Excerpt_Master.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_20_DOJ_DOJ_Supplemental_Continuing_Harm.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_20_DOJ__40_DOJ_Civil_Rights.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_20_DOJ_doj_supplemental.html.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_30_HUD_Cover_Letter.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_30_HUD_HUD_FHEO_Complaint_Narrative.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_30_HUD_HUD_FHEO_Violation_Excerpt.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_30_HUD_MANIFEST_HUD_FHEO_Complaint_Packet.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_30_HUD__50_HUD_FHEO.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_40_Federal_30_HUD_hud_fheo_narrative.html.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_Violation_to_Regulator_Mapping.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS__TOC_.md.txt
> │      ├── 📄 03_PHASE_WORK_04_PHASE_REGULATORS_index.html.txt
> │      ├── 📄 repo_dump_tree_with_contents_and_ocr.txt.txt
> │    └── 📂 manifests/
> │      ├── 📄 repo_index.json
> │  └── 📂 prompts/
> │    ├── 📄 rag_answer.txt
> │  └── 📂 scripts/
> │    └── 📂 rag/
> │      ├── 📄 01_scan_repo.py
> │      ├── 📄 02_extract_text.py
> │      ├── 📄 03_embed_index.py
> │      ├── 📄 04_query_chat.py
> │    ├── 📄 setup_rag_env.ps1
> │  └── 📂 ui/
> └── 📂 mkdocs-material-boilerplate/
> │  ├── 📄 Dockerfile
> │  ├── 📄 LICENSE
> │  ├── 📄 Pipfile
> │  ├── 📄 Pipfile.lock
> │  ├── 📄 README.md
> │  ├── 📄 amplify.yml
> │  ├── 📄 docker-compose.yml
> │  └── 📂 docs_sample/
> │    ├── 📄 CNAME
> │    └── 📂 assets/
> │      └── 📂 css/
> │        ├── 📄 custom.css
> │    └── 📂 extensions/
> │      ├── 📄 code-hilite.md
> │      ├── 📄 footnote.md
> │      ├── 📄 mathjax.md
> │    └── 📂 getting-started/
> │      ├── 📄 docker.md
> │      ├── 📄 download-boilerplate.md
> │      ├── 📄 invoke.md
> │      ├── 📄 pip.md
> │      ├── 📄 pipenv.md
> │    └── 📂 hosting-and-deployment/
> │      ├── 📄 aws-amplify-console.md
> │      ├── 📄 combinations.md
> │      ├── 📄 github-pages.md
> │      ├── 📄 gitlab-pages.md
> │      ├── 📄 netlify.md
> │    └── 📂 images/
> │      ├── 📄 graduate-cap.192x192.png
> │      ├── 📄 graduate-cap.48x48.png
> │      ├── 📄 graduate-cap.96x96.png
> │      ├── 📄 graduate-cap.png
> │      ├── 📄 material.png
> │    ├── 📄 index.md
> │    ├── 📄 license.md
> │    ├── 📄 manifest.json
> │    ├── 📄 material-for-mkdocs.md
> │  ├── 📄 mkdocs-sample.yml
> │  ├── 📄 netlify.toml
> │  ├── 📄 renovate.json
> │  ├── 📄 requirements-dev.txt
> │  ├── 📄 requirements.txt
> │  ├── 📄 runtime.txt
> │  ├── 📄 tasks.py
> └── 📂 paperless_fcfcu/
> │  ├── 📄 backup_case_evidence.cmd
> │  └── 📂 backups/
> │    ├── 📄 index.html
> │  └── 📂 consume/
> │    ├── 📄 _B_EVIDENCE.md
> │    ├── 📄 court_record__20_court_record.md
> │    ├── 📄 court_record___20_court_record.md
> │    ├── 📄 court_record_docket_files__EXH__026_Exhibit_List_A-G.pdf
> │    ├── 📄 court_record_docket_files__MO__013_Motion_for_Default_Judgment.pdf
> │    ├── 📄 court_record_docket_files__MO__019_Amended_Motion_Default_Judgmen.pdf
> │    ├── 📄 court_record_docket_files__MO__020_Amended_Motion_Default_Judgmen.pdf
> │    ├── 📄 court_record_docket_files__MO__025_Motion_Vacate_Stay_Writ.pdf
> │    ├── 📄 court_record_docket_files__MO__027_Supplemental_Motion_Access.pdf
> │    ├── 📄 court_record_docket_files__OR__023_Decree_Foreclosure_Returned.pdf
> │    ├── 📄 court_record_docket_files__OR__031_Proposed_Order_Vacate.pdf
> │    ├── 📄 court_record_docket_files__OR__032_Proposed_Order_Stay.pdf
> │    ├── 📄 court_record_docket_files__PL_017_OMITTED NOTICE OF SERVICE TO DEFENDANT.pdf
> │    ├── 📄 court_record_docket_files__PL_029_Emergency_Supplemental_Declaration.pdf
> │    ├── 📄 court_record_docket_files__PL__001_Complaint.pdf
> │    ├── 📄 court_record_docket_files__PL__002_Appearance.pdf
> │    ├── 📄 court_record_docket_files__PL__003_Request_for_Admissions.pdf
> │    ├── 📄 court_record_docket_files__PL__004_Notice_to_Homeowners.pdf
> │    ├── 📄 court_record_docket_files__PL__005_Appearance_2.pdf
> │    ├── 📄 court_record_docket_files__PL__006_Summons_1.pdf
> │    ├── 📄 court_record_docket_files__PL__007_Summons_2.pdf
> │    ├── 📄 court_record_docket_files__PL__008_Summons_3.pdf
> │    ├── 📄 court_record_docket_files__PL__009_Summons_4.pdf
> │    ├── 📄 court_record_docket_files__PL__010_Summons_5.pdf
> │    ├── 📄 court_record_docket_files__PL__011_Service_Returned_03-05-2025.pdf
> │    ├── 📄 court_record_docket_files__PL__012_Service_Returned_04-15-2025.pdf
> │    ├── 📄 court_record_docket_files__PL__014_Affidavit.pdf
> │    ├── 📄 court_record_docket_files__PL__015_Affidavit_Attorney_Fees.pdf
> │    ├── 📄 court_record_docket_files__PL__016_Affidavit_Additional.pdf
> │    ├── 📄 court_record_docket_files__PL__018_Omitted_Notice_of_Service.pdf
> │    ├── 📄 court_record_docket_files__PL__021_Praecipe_Sheriff_Sale_1.pdf
> │    ├── 📄 court_record_docket_files__PL__022_Praecipe_Sheriff_Sale_2.pdf
> │    ├── 📄 court_record_docket_files__PL__024_Petition_Writ_of_Assistance.pdf
> │    ├── 📄 court_record_docket_files__PL__028_Report_Court_Defendant_Request.pdf
> │    ├── 📄 court_record_docket_files__PL__030_Report_Sheriff_Sale_No_Excess.pdf
> │    ├── 📄 court_record_docket_files__PL__033_ADA_Disability_Affidavit.pdf
> │    ├── 📄 court_record_docket_files___10_docket_files.md
> │    ├── 📄 evidence_admin__00_evidence_admin.md
> │    ├── 📄 evidence_admin__10_chain_of_custody.md
> │    ├── 📄 evidence_admin__20_Evidence_Log.md
> │    ├── 📄 evidence_admin__EXH_Raw_Exhibit_Map.md
> │    ├── 📄 evidence_admin___10_evidence_admin.md
> │    ├── 📄 index.html
> │    ├── 📄 primary___30_primary.md
> │    ├── 📄 primary_aes__PL_2025-06-08_aes_ada_notice.pdf
> │    ├── 📄 primary_aes__PL_2025-12-16_AES_Emergency_Notice.md
> │    ├── 📄 primary_aes___20_aes.md
> │    ├── 📄 primary_aes___README.md
> │    ├── 📄 primary_fcfcu__2023-09-20_FCFCU_Hardship_and_Healt.md
> │    ├── 📄 primary_fcfcu__20241204_FCFCU_Statement (1).pdf
> │    ├── 📄 primary_fcfcu__20241204_FCFCU_Statement (2).pdf
> │    ├── 📄 primary_fcfcu__20241204_fcfcu_statement-(1).pdf
> │    ├── 📄 primary_fcfcu__20241204_fcfcu_statement-(2).pdf
> │    ├── 📄 primary_fcfcu__20241204_fcfcu_statement.pdf
> │    ├── 📄 primary_fcfcu__PL_2023-09-20_FCFCU_Hardship_and_Health_Notice_Let.md
> │    ├── 📄 primary_fcfcu__PL_2023-09-20_notice_disabilities_hardship.pdf
> │    ├── 📄 primary_fcfcu__PL_2024-20-03_response_to_tax_notice.pdf
> │    ├── 📄 primary_fcfcu___10_fcfcu.md
> │    ├── 📄 primary_fcfcu___README.md
> │    ├── 📄 quarantine_candidates__50_quarantine_candidates.md
> │    ├── 📄 quarantine_candidates___50_quarantine_candidates.md
> │    ├── 📄 supporting__40_supporting.md
> │    ├── 📄 supporting___40_supporting.md
> │    ├── 📄 supporting_docs___docs.md
> │    ├── 📄 supporting_docs_affidavits__PL_affidavits.md
> │    ├── 📄 supporting_docs_affidavits___affidavits.md
> │    ├── 📄 supporting_docs_affidavits_ada-disability___ada-disability.md
> │    ├── 📄 supporting_docs_affidavits_character___character.md
> │    ├── 📄 supporting_docs_affidavits_community-service___community-service.md
> │    ├── 📄 supporting_docs_affidavits_credibility___credibility.md
> │    ├── 📄 supporting_docs_affidavits_observations___observations.md
> │    ├── 📄 supporting_docs_declarations__PL_declarations.md
> │    ├── 📄 supporting_docs_declarations___declarations.md
> │    ├── 📄 supporting_docs_receipts___receipts.md
> │    ├── 📄 supporting_docs_records___records.md
> │    ├── 📄 supporting_multi-media___multi-media.md
> │    ├── 📄 supporting_property___property.md
> │    ├── 📄 supporting_property_mortgage_history___10_mortgage_history.md
> │    ├── 📄 supporting_property_mortgage_history_payments__2025-12-20_EXH-20_payments_c5131deb_2025-12-20.png
> │    ├── 📄 supporting_property_mortgage_history_payments__20_payments.md
> │    ├── 📄 supporting_property_mortgage_history_payments___10_payments.md
> │    ├── 📄 supporting_property_parcel__Parcel_6016506_PRC.pdf
> │    ├── 📄 supporting_property_parcel__Parcel_6016506_ParcelDetailHistory.pdf
> │    ├── 📄 supporting_property_parcel___20_parcel.md
> │  └── 📂 data/
> │    ├── 📄 PG_VERSION
> │    └── 📂 base/
> │      └── 📂 1/
> │        ├── 📄 index.html
> │      ├── 📄 index.html
> │    ├── 📄 celerybeat-schedule.db
> │    └── 📂 global/
> │      ├── 📄 index.html
> │      ├── 📄 pg_control
> │    └── 📂 index/
> │    ├── 📄 index.html
> │      ├── 📄 MAIN_WRITELOCK
> │      ├── 📄 MAIN_df60pz781b1vkrg5.seg
> │      ├── 📄 _MAIN_110.toc
> │      ├── 📄 index.html
> │    └── 📂 log/
> │      ├── 📄 celery.log
> │      ├── 📄 celery.log.2
> │      ├── 📄 celery.log.rotate.13123699319956527895
> │      ├── 📄 celery.log.rotate.14527157462966423769
> │      ├── 📄 celery.log.rotate.16014095090721714709
> │      ├── 📄 celery.log.rotate.16551543857574243639
> │      ├── 📄 celery.log.rotate.4002149963526754070
> │      ├── 📄 celery.log.rotate.5851441854598125821
> │      ├── 📄 celery.log.rotate.9282371777522306113
> │      ├── 📄 index.html
> │      ├── 📄 paperless.log
> │      ├── 📄 paperless.log.rotate.1272259500908817030
> │      ├── 📄 paperless.log.rotate.2124330999174016128
> │    ├── 📄 migration_lock
> │    └── 📂 pg_commit_ts/
> │      ├── 📄 index.html
> │    └── 📂 pg_dynshmem/
> │      ├── 📄 index.html
> │    ├── 📄 pg_hba.conf
> │    ├── 📄 pg_ident.conf
> │    └── 📂 pg_logical/
> │      ├── 📄 index.html
> │      └── 📂 mappings/
> │        ├── 📄 index.html
> │      ├── 📄 replorigin_checkpoint
> │      └── 📂 snapshots/
> │        ├── 📄 index.html
> │    └── 📂 pg_multixact/
> │      ├── 📄 index.html
> │      └── 📂 members/
> │        ├── 📄 0000
> │        ├── 📄 index.html
> │      └── 📂 offsets/
> │        ├── 📄 0000
> │        ├── 📄 index.html
> │    └── 📂 pg_notify/
> │      ├── 📄 index.html
> │    └── 📂 pg_replslot/
> │      ├── 📄 index.html
> │    └── 📂 pg_serial/
> │      ├── 📄 index.html
> │    └── 📂 pg_snapshots/
> │      ├── 📄 index.html
> │    └── 📂 pg_stat/
> │      ├── 📄 index.html
> │      ├── 📄 pgstat.stat
> │    └── 📂 pg_stat_tmp/
> │      ├── 📄 index.html
> │    └── 📂 pg_subtrans/
> │      ├── 📄 0000
> │      ├── 📄 index.html
> │    └── 📂 pg_tblspc/
> │      ├── 📄 index.html
> │    └── 📂 pg_twophase/
> │      ├── 📄 index.html
> │    └── 📂 pg_wal/
> │      ├── 📄 000000010000000000000001
> │      └── 📂 archive_status/
> │        ├── 📄 index.html
> │      ├── 📄 index.html
> │    └── 📂 pg_xact/
> │      ├── 📄 0000
> │      ├── 📄 index.html
> │    ├── 📄 postgresql.auto.conf
> │    ├── 📄 postgresql.conf
> │    ├── 📄 postmaster.opts
> │  ├── 📄 docker-compose.yml
> │  └── 📂 export/
> │    ├── 📄 index.html
> │  ├── 📄 index.html
> │  └── 📂 media/
> │    └── 📂 documents/
> │      └── 📂 archive/
> │        ├── 📄 0000001.pdf
> │        ├── 📄 0000002.pdf
> │        ├── 📄 0000003.pdf
> │        ├── 📄 0000004.pdf
> │        ├── 📄 0000005.pdf
> │        ├── 📄 0000006.pdf
> │        ├── 📄 0000007.pdf
> │        ├── 📄 0000008.pdf
> │        ├── 📄 0000009.pdf
> │        ├── 📄 0000010.pdf
> │        ├── 📄 0000011.pdf
> │        ├── 📄 0000012.pdf
> │        ├── 📄 0000013.pdf
> │        ├── 📄 0000014.pdf
> │        ├── 📄 0000015.pdf
> │        ├── 📄 0000016.pdf
> │        ├── 📄 0000017.pdf
> │        ├── 📄 0000018.pdf
> │        ├── 📄 0000019.pdf
> │        ├── 📄 0000020.pdf
> │        ├── 📄 0000021.pdf
> │        ├── 📄 0000022.pdf
> │        ├── 📄 0000023.pdf
> │        ├── 📄 0000024.pdf
> │        ├── 📄 0000025.pdf
> │        ├── 📄 0000026.pdf
> │        ├── 📄 0000027.pdf
> │        ├── 📄 0000028.pdf
> │        ├── 📄 0000029.pdf
> │        ├── 📄 0000030.pdf
> │        ├── 📄 0000031.pdf
> │        ├── 📄 0000032.pdf
> │        ├── 📄 0000033.pdf
> │        ├── 📄 0000034.pdf
> │        ├── 📄 0000035.pdf
> │        ├── 📄 0000036.pdf
> │        ├── 📄 0000037.pdf
> │        ├── 📄 0000038.pdf
> │        ├── 📄 0000039.pdf
> │        ├── 📄 0000040.pdf
> │        ├── 📄 0000041.pdf
> │        ├── 📄 0000042.pdf
> │        ├── 📄 0000043.pdf
> │        ├── 📄 0000044.pdf
> │        ├── 📄 0000045.pdf
> │        ├── 📄 0000046.pdf
> │        ├── 📄 0000047.pdf
> │        ├── 📄 0000048.pdf
> │        ├── 📄 0000049.pdf
> │        ├── 📄 0000050.pdf
> │        ├── 📄 0000051.pdf
> │        ├── 📄 0000052.pdf
> │        ├── 📄 0000053.pdf
> │        ├── 📄 0000054.pdf
> │        ├── 📄 0000055.pdf
> │        ├── 📄 0000056.pdf
> │        ├── 📄 0000057.pdf
> │        ├── 📄 0000058.pdf
> │        ├── 📄 0000059.pdf
> │        ├── 📄 0000060.pdf
> │        ├── 📄 0000061.pdf
> │        ├── 📄 0000062.pdf
> │        ├── 📄 0000063.pdf
> │        ├── 📄 0000064.pdf
> │        ├── 📄 0000065.pdf
> │        ├── 📄 0000066.pdf
> │        ├── 📄 0000067.pdf
> │        ├── 📄 0000068.pdf
> │        ├── 📄 0000069.pdf
> │        ├── 📄 0000070.pdf
> │        ├── 📄 0000071.pdf
> │        ├── 📄 0000072.pdf
> │        ├── 📄 0000073.pdf
> │        ├── 📄 0000074.pdf
> │        ├── 📄 0000075.pdf
> │        ├── 📄 0000076.pdf
> │        ├── 📄 0000077.pdf
> │        ├── 📄 0000078.pdf
> │        ├── 📄 0000079.pdf
> │        ├── 📄 0000080.pdf
> │        ├── 📄 0000081.pdf
> │        ├── 📄 0000082.pdf
> │        ├── 📄 0000083.pdf
> │        ├── 📄 0000084.pdf
> │        ├── 📄 0000085.pdf
> │        ├── 📄 index.html
> │      ├── 📄 index.html
> │      └── 📂 originals/
> │        ├── 📄 0000001.pdf
> │        ├── 📄 0000002.pdf
> │        ├── 📄 0000003.pdf
> │        ├── 📄 0000004.pdf
> │        ├── 📄 0000005.pdf
> │        ├── 📄 0000006.pdf
> │        ├── 📄 0000007.pdf
> │        ├── 📄 0000008.pdf
> │        ├── 📄 0000009.pdf
> │        ├── 📄 0000010.pdf
> │        ├── 📄 0000011.pdf
> │        ├── 📄 0000012.pdf
> │        ├── 📄 0000013.pdf
> │        ├── 📄 0000014.pdf
> │        ├── 📄 0000015.pdf
> │        ├── 📄 0000016.pdf
> │        ├── 📄 0000017.pdf
> │        ├── 📄 0000018.pdf
> │        ├── 📄 0000019.pdf
> │        ├── 📄 0000020.pdf
> │        ├── 📄 0000021.pdf
> │        ├── 📄 0000022.pdf
> │        ├── 📄 0000023.pdf
> │        ├── 📄 0000024.pdf
> │        ├── 📄 0000025.pdf
> │        ├── 📄 0000026.pdf
> │        ├── 📄 0000027.pdf
> │        ├── 📄 0000028.pdf
> │        ├── 📄 0000029.pdf
> │        ├── 📄 0000030.pdf
> │        ├── 📄 0000031.pdf
> │        ├── 📄 0000032.pdf
> │        ├── 📄 0000033.pdf
> │        ├── 📄 0000034.pdf
> │        ├── 📄 0000035.pdf
> │        ├── 📄 0000036.pdf
> │        ├── 📄 0000037.pdf
> │        ├── 📄 0000038.pdf
> │        ├── 📄 0000039.pdf
> │        ├── 📄 0000040.pdf
> │        ├── 📄 0000041.pdf
> │        ├── 📄 0000042.pdf
> │        ├── 📄 0000043.jpg
> │        ├── 📄 0000044.jpg
> │        ├── 📄 0000045.pdf
> │        ├── 📄 0000046.pdf
> │        ├── 📄 0000047.pdf
> │        ├── 📄 0000048.pdf
> │        ├── 📄 0000049.jpg
> │        ├── 📄 0000050.pdf
> │        ├── 📄 0000051.jpg
> │        ├── 📄 0000052.jpg
> │        ├── 📄 0000053.png
> │        ├── 📄 0000054.jpg
> │        ├── 📄 0000055.jpg
> │        ├── 📄 0000056.jpg
> │        ├── 📄 0000057.jpg
> │        ├── 📄 0000058.jpg
> │        ├── 📄 0000059.jpg
> │        ├── 📄 0000060.jpg
> │        ├── 📄 0000061.jpg
> │        ├── 📄 0000062.jpg
> │        ├── 📄 0000063.jpg
> │        ├── 📄 0000064.jpg
> │        ├── 📄 0000065.jpg
> │        ├── 📄 0000066.jpg
> │        ├── 📄 0000067.jpg
> │        ├── 📄 0000068.jpg
> │        ├── 📄 0000069.jpg
> │        ├── 📄 0000070.png
> │        ├── 📄 0000071.jpg
> │        ├── 📄 0000072.jpg
> │        ├── 📄 0000073.jpg
> │        ├── 📄 0000074.jpg
> │        ├── 📄 0000075.jpg
> │        ├── 📄 0000076.jpg
> │        ├── 📄 0000077.jpg
> │        ├── 📄 0000078.jpg
> │        ├── 📄 0000079.jpg
> │        ├── 📄 0000080.jpg
> │        ├── 📄 0000081.jpg
> │        ├── 📄 0000082.jpg
> │        ├── 📄 0000083.png
> │        ├── 📄 0000084.pdf
> │        ├── 📄 0000085.pdf
> │        ├── 📄 index.html
> │      └── 📂 thumbnails/
> │        ├── 📄 0000001.webp
> │        ├── 📄 0000002.webp
> │        ├── 📄 0000003.webp
> │        ├── 📄 0000004.webp
> │        ├── 📄 0000005.webp
> │        ├── 📄 0000006.webp
> │        ├── 📄 0000007.webp
> │        ├── 📄 0000008.webp
> │        ├── 📄 0000009.webp
> │        ├── 📄 0000010.webp
> │        ├── 📄 0000011.webp
> │        ├── 📄 0000012.webp
> │        ├── 📄 0000013.webp
> │        ├── 📄 0000014.webp
> │        ├── 📄 0000015.webp
> │        ├── 📄 0000016.webp
> │        ├── 📄 0000017.webp
> │        ├── 📄 0000018.webp
> │        ├── 📄 0000019.webp
> │        ├── 📄 0000020.webp
> │        ├── 📄 0000021.webp
> │        ├── 📄 0000022.webp
> │        ├── 📄 0000023.webp
> │        ├── 📄 0000024.webp
> │        ├── 📄 0000025.webp
> │        ├── 📄 0000026.webp
> │        ├── 📄 0000027.webp
> │        ├── 📄 0000028.webp
> │        ├── 📄 0000029.webp
> │        ├── 📄 0000030.webp
> │        ├── 📄 0000031.webp
> │        ├── 📄 0000032.webp
> │        ├── 📄 0000033.webp
> │        ├── 📄 0000034.webp
> │        ├── 📄 0000035.webp
> │        ├── 📄 0000036.webp
> │        ├── 📄 0000037.webp
> │        ├── 📄 0000038.webp
> │        ├── 📄 0000039.webp
> │        ├── 📄 0000040.webp
> │        ├── 📄 0000041.webp
> │        ├── 📄 0000042.webp
> │        ├── 📄 0000043.webp
> │        ├── 📄 0000044.webp
> │        ├── 📄 0000045.webp
> │        ├── 📄 0000046.webp
> │        ├── 📄 0000047.webp
> │        ├── 📄 0000048.webp
> │        ├── 📄 0000049.webp
> │        ├── 📄 0000050.webp
> │        ├── 📄 0000051.webp
> │        ├── 📄 0000052.webp
> │        ├── 📄 0000053.webp
> │        ├── 📄 0000054.webp
> │        ├── 📄 0000055.webp
> │        ├── 📄 0000056.webp
> │        ├── 📄 0000057.webp
> │        ├── 📄 0000058.webp
> │        ├── 📄 0000059.webp
> │        ├── 📄 0000060.webp
> │        ├── 📄 0000061.webp
> │        ├── 📄 0000062.webp
> │        ├── 📄 0000063.webp
> │        ├── 📄 0000064.webp
> │        ├── 📄 0000065.webp
> │        ├── 📄 0000066.webp
> │        ├── 📄 0000067.webp
> │        ├── 📄 0000068.webp
> │        ├── 📄 0000069.webp
> │        ├── 📄 0000070.webp
> │        ├── 📄 0000071.webp
> │        ├── 📄 0000072.webp
> │        ├── 📄 0000073.webp
> │        ├── 📄 0000074.webp
> │        ├── 📄 0000075.webp
> │        ├── 📄 0000076.webp
> │        ├── 📄 0000077.webp
> │        ├── 📄 0000078.webp
> │        ├── 📄 0000079.webp
> │        ├── 📄 0000080.webp
> │        ├── 📄 0000081.webp
> │        ├── 📄 0000082.webp
> │        ├── 📄 0000083.webp
> │        ├── 📄 0000084.webp
> │        ├── 📄 0000085.webp
> │        ├── 📄 index.html
> │    ├── 📄 index.html
> │    ├── 📄 media.lock
> └── 📄 scenario_simulation_agent.py
> ```

### Assistant
> Yep. You’ve already got the three legs you need — you just haven’t wired them into a single “truth pipeline” yet:
> 
> - **Docs Site (MkDocs Material)** = *human browsing on phone*
> - **Paperless** = *document intake + OCR + tagging*
> - **Case RAG** = *AI search/answers across the corpus*
> 
> Below is the cleanest way to hook them up without turning your repo into spaghetti.
> 
> ---
> 
> ## The right build order (don’t freestyle this)
> 
> ### 1) Docs site first (phone access)
> Goal: you can open a URL on your phone and navigate your case materials like a site.
> 
> **What should be in MkDocs:**
> - Only **curated, human-readable** content:
>   - Phase masters
>   - Docket index / trackers
>   - Exhibit lists
>   - “What happened” timeline narrative
>   - Playbooks / checklists / templates
> - Not raw PDFs (you can link PDFs, but don’t try to “MkDocs your entire evidence vault”)
> 
> **Pattern**
> - `mkdocs-material-boilerplate/` becomes your docs app
> - Your content lives in a single source folder in the repo (recommended):
>   - `docs_src/` (source-of-truth markdown)
>   - MkDocs builds to `site/` (generated)
> 
> **Deployment options**
> - **Fastest/lowest pain:** Cloudflare Pages (build command + output dir)
> - If you insist on local-first and just want it online: push to GitHub → Pages is fine too, but CF Pages is your ecosystem.
> 
> ✅ Output: `https://<your-docs-domain>/` works on mobile.
> 
> ---
> 
> ### 2) Paperless second (ingestion + OCR)
> Goal: everything you add (email, scan, phone upload) becomes OCR’d and normalized.
> 
> You already have `paperless_fcfcu/` with docker-compose and a ton of archived documents. Good.
> 
> **Do this next:**
> - Make Paperless the **single intake mouth**
> - Feed it:
>   - scans
>   - email-to-paperless
>   - phone uploads
>   - exported court PDFs
> - Ensure OCR is on and good enough (English is fine; if you need multilingual later, that’s a separate fight)
> 
> ✅ Output: Paperless becomes your “document registry” with tags + metadata.
> 
> ---
> 
> ### 3) Case RAG third (index + embed + query)
> Goal: RAG indexes:
> - MkDocs curated markdown (high signal)
> - Paperless documents (OCR text + metadata)
> - Optional: your trackers CSVs
> 
> You already have scripts:
> - `01_scan_repo.py`
> - `02_extract_text.py`
> - `03_embed_index.py`
> - `04_query_chat.py`
> 
> That’s the right shape. Now you need to make it **pull from Paperless automatically** instead of you dragging files around.
> 
> ✅ Output: You can ask “what did they claim on May 28 vs July 17” and it cites the right artifacts.
> 
> ---
> 
> ## The wiring: one pipeline, two outputs
> 
> ### Source of truth flows like this
> 
> **Paperless (raw truth)**  
> → export/metadata snapshot  
> → RAG extraction + embeddings  
> → (A) AI answers (RAG UI)  
> → (B) curated markdown updates (MkDocs)
> 
> So:
> - Paperless is the **truth vault**
> - RAG is the **search brain**
> - MkDocs is the **presentation layer**
> 
> MkDocs should *not* be the ingestion source. That’s backwards.
> 
> ---
> 
> ## Minimal folder structure that won’t rot
> 
> Add these (top-level):
> 
> ```
> docs_src/                  # curated markdown only (what humans read)
> rag_store/
>   corpus/                  # text chunks RAG reads (generated)
>   index/                   # embeddings + metadata (generated)
>   snapshots/
>     paperless_export/      # latest exported OCR + metadata (generated)
> ```
> 
> And keep:
> - `paperless_fcfcu/` = the running system + data volumes (ideally NOT fully committed if it’s huge)
> - `app/case_rag/` = code + configs
> 
> ---
> 
> ## Paperless → RAG: how to connect (the practical way)
> 
> ### Option A (recommended): export from Paperless via API
> You run a script that:
> 1) pulls document list + metadata (tags, correspondents, created date, title)
> 2) downloads OCR’d text (or the file and extracts text)
> 3) stores into `rag_store/snapshots/paperless_export/`
> 4) triggers embed refresh
> 
> That gives you:
> - stable ingestion
> - metadata available for filtering (by tag, date, doc type)
> - reproducible builds
> 
> ### Option B (simple but janky): point RAG at Paperless “media/documents/archive”
> You *can* point your extractor at:
> `paperless_fcfcu/media/documents/archive/`
> …but you’ll lose a lot of metadata context unless you also capture Paperless DB/API data.
> 
> If you care about **chain-of-custody and traceability**, use Option A.
> 
> ---
> 
> ## MkDocs ↔ evidence linking (don’t break links)
> 
> In MkDocs, link to evidence like this:
> 
> - “View PDF” links should point to either:
>   - Paperless document URL (best, includes metadata page)
>   - or a public/static mirror bucket (only if you need public)
> 
> If your docs site is private (which it should be), linking to Paperless directly is fine.
> 
> ---
> 
> ## What to do *today* (no theory)
> 
> ### Phase 1: Get docs online (1 sitting)
> 1. Create `docs_src/` and move only curated markdown there.
> 2. In `mkdocs-material-boilerplate/`, set:
>    - `docs_dir: ../docs_src`
>    - `site_dir: ../site` (or keep default inside boilerplate)
> 3. Make a dead-simple nav:
>    - Home
>    - Phases
>    - Docket / Timeline
>    - Trackers
>    - Templates
> 4. Deploy to Cloudflare Pages.
> 
> ### Phase 2: Make Paperless the only intake (same day)
> 1. Confirm Paperless is reachable from your phone (Tailscale/Zero Trust/Cloudflare Tunnel).
> 2. Make “consume” the only drop zone.
> 3. Stop manually sprinkling PDFs into random folders.
> 
> ### Phase 3: Hook Paperless export into case_rag (next)
> 1. Add a new script: `scripts/rag/00_sync_paperless.py`
> 2. Update `config/sources.yaml` to include:
>    - `docs_src/` (curated)
>    - `rag_store/snapshots/paperless_export/` (raw OCR exports)
> 3. Run pipeline end-to-end:
>    - sync → extract → embed → query
> 
> ---
> 
> ## Your biggest current risk (I’m calling it out)
> You’ve got:
> - `app/case_rag/data/extracted_text/` full of `.txt` artifacts (good),
> - **AND** a full Paperless archive dumped in repo-ish structure (heavy),
> - **AND** MkDocs boilerplate sitting separate.
> 
> If you don’t formalize the flow, you’ll end up with:
> - duplicate truth
> - broken references
> - “which version is real?” fights
> - embeddings that drift
> 
> So: **declare the system of record**:
> - Raw docs = Paperless
> - Curated narrative = docs_src (MkDocs)
> - Search index = rag_store (generated)
> 
> Everything else is derived.
> 
> ---
> 
> ## If you want, next message I’ll give you:
> - a ready-to-paste `mkdocs.yml` wired to `docs_src/`
> - a sane `sources.yaml` + `ingest_rules.yaml` layout for:
>   - curated vs raw
>   - per-phase tag filters
>   - “court record” priority boosting
> - a concrete `00_sync_paperless.py` spec (API-based) that outputs:
>   - `document.json` metadata
>   - `document.txt` OCR text
>   - stable filenames using your Qi-style IDs
> 
> But the move right now is simple: **stand up the docs site first** so you stop feeling blind on mobile. Then ingestion. Then RAG.

### User
> why did gemini just make 10 phases again we had settled on 7

### Assistant
> Because Gemini is doing the default “project manager brain” thing: it sees complexity, so it invents more buckets to feel organized. Unless you *hard-constrained* it (“exactly 7 phases, no more, no less”), it will happily re-split your lanes.
> 
> Also: a lot of templates (legal playbooks, litigation checklists, even “case management” frameworks) naturally come in 9–12 sections. Models regurgitate that structure when they’re unsure what your spine is.
> 
> ### The real fix
> Your system has **one spine** (7 phases). Everything else is:
> - **subphases**
> - **lanes**
> - **views/filters**
> - **tables**
> - **workstreams**
> —not new phases.
> 
> If Gemini made 10 again, it likely did one of these:
> 1) Split your **Phase 0 / Case Management** into multiple “phases” (case mgmt, evidence, comms, etc.).
> 2) Broke **Credit/FCRA**, **Regulators**, **Litigation** into separate “phases” instead of keeping them as lanes under one phase.
> 3) Added “Media/PR” and “Damages/Valuation” as phases (they’re lanes/views, not spine nodes).
> 
> ### Your rule (non-negotiable)
> **Phases never increase.**  
> New work goes under existing phases as:
> - `00.xx` subphase folders
> - a new tracker/table
> - a new tag in Paperless
> - a new MkDocs section
> - a new RAG “collection”
> 
> ### Paste this into Gemini next time (hard constraint)
> ```text
> You are reorganizing my case project. The case has EXACTLY 7 phases. 
> DO NOT create any additional phases. 
> If something does not fit, it must become (a) a subphase folder, (b) a lane/view, or (c) a tracker/table under one of the 7 phases.
> 
> Output:
> 1) List the 7 phases unchanged (same IDs and names).
> 2) Under each phase, propose subphases as 00.01, 00.02, etc.
> 3) Map every existing folder/file into one of the 7 phases.
> Any attempt to output more than 7 phases is incorrect.
> ```
> 
> ### Quick sanity check
> If you paste your **actual 7 phase names** (just the headers), I’ll:
> - pin the “phase spine” as a canonical block you can reuse everywhere
> - show where Gemini’s extra 3 “phases” should live (which parent phase + subphase)
> - give you a one-screen “phase mapping rule” you can slap on every agent prompt so this stops happening.

### User
> also he was dipping in my evidence vault for some reason. how should i get this back organized. ```markdown
> . 📂 99_VAULT
> └── 📂 C-01_Jurisdictional_Defects/
> │  └── 📂 00_RECEIVED/
> │    ├── 📄 _00_RECEIVED.md
> │  └── 📂 00_drafts/
> │    ├── 📄 20260202_CAPTURE_Auto_Save_D0516.html
> │    ├── 📄 _C02_drafts.md
> │  └── 📂 01_FILED/
> │    ├── 📄 20260115_C01_FORECL_FCFCU_MOTION_D0511.pdf
> │    ├── 📄 _01_FILED.md
> │  └── 📂 01_PHOTOS/
> │    ├── 📄 20251209_PHOTO_Auto_Save_D0107.heic
> │    ├── 📄 20251209_PHOTO_Auto_Save_D0112.heic
> │    ├── 📄 20251220_PHOTO_Auto_Save_D0132.heic
> │    ├── 📄 20251220_PHOTO_Auto_Save_D0133.heic
> │    ├── 📄 20260207_PHOTO_Auto_Save_D0144.heic
> │    ├── 📄 20260207_PHOTO_Auto_Save_D0145.heic
> │    ├── 📄 20260207_PHOTO_Auto_Save_D0146.heic
> │    ├── 📄 20260207_PHOTO_Auto_Save_D0147.heic
> │    ├── 📄 20260207_PHOTO_Auto_Save_D0148.heic
> │    ├── 📄 20260207_PHOTO_Auto_Save_D0149.heic
> │    ├── 📄 20260207_PHOTO_Auto_Save_D0150.heic
> │    ├── 📄 20260207_PHOTO_Auto_Save_D0151.heic
> │    ├── 📄 20260208_PHOTO_Evidence_IMG_2905.PNG
> │    ├── 📄 20260208_PHOTO_Evidence_IMG_2906.PNG
> │    ├── 📄 20260208_PHOTO_Evidence_IMG_2908.PNG
> │    ├── 📄 20260208_PHOTO_Evidence_IMG_2911.PNG
> │    ├── 📄 20260208_PHOTO_Evidence_IMG_2913.PNG
> │    ├── 📄 20260208_PHOTO_Evidence_IMG_2914.PNG
> │    ├── 📄 _01_PHOTOS.md
> │  └── 📂 02_ORDERS/
> │    ├── 📄 20260118_C01_FORECL_FCFCU_MOTION_D0482.pdf
> │    ├── 📄 _02_ORDERS.md
> │  └── 📂 02_VIDEO/
> │    ├── 📄 20260209_C02_Screen_Recording_hearing_jan_09_2026.mp4
> │    ├── 📄 _02_VIDEO.md
> │  └── 📂 03_DOCUMENTS/
> │    ├── 📄 20260121_FILE_Auto_Save_D0477.pptx
> │    ├── 📄 20260131_C06_ADA_FCFCU_INV_D0517.pdf
> │    ├── 📄 20260201_C00_ORDER_D0524.pdf
> │    ├── 📄 20260201_C06_ADA_VIDEO_D0514.pdf
> │    ├── 📄 20260203_C00_ORDER_D0552.pdf
> │    ├── 📄 20260203_CAPTURE_Auto_Save_D0469.mhtml
> │    ├── 📄 20260203_EMAIL_Auto_Save_D0497.eml
> │    ├── 📄 20260207_FILE_Auto_Save_D0014.mw
> │    ├── 📄 20260209_LEGAL_Appellate_Document.docx
> │    ├── 📄 20260209_LEGAL_Appellate_Document.pdf
> │    ├── 📄 20260209_NOTICE_Direct_Dispute_Deletion_Demand.pdf
> │    ├── 📄 20260209_TEMPLATE_Case_Document.pdf
> │    ├── 📄 20260209_TEMPLATE_Case_Document_Backup.pdf
> │    ├── 📄 20260210_NOTICE_Notice_of_Appeal_FILED.pdf
> │    ├── 📄 20260210_NOTICE_Notice_of_Appeal_FILED.png
> │    ├── 📄 20260210_REPORT_ShadowPointe_Client.pdf
> │    ├── 📄 _03_DOCUMENTS.md
> │  └── 📂 03_EVIDENCE/
> │    └── 📂 01_PHOTOS/
> │      ├── 📄 _01_PHOTOS.md
> │    └── 📂 02_VIDEO/
> │      ├── 📄 _02_VIDEO.md
> │    └── 📂 03_DOCUMENTS/
> │      ├── 📄 _03_DOCUMENTS.md
> │    └── 📂 04_FINANCIAL/
> │      ├── 📄 _04_FINANCIAL.md
> │    └── 📂 05_EXPORTS/
> │      ├── 📄 _05_EXPORTS.md
> │    ├── 📄 _03_EVIDENCE.md
> │  └── 📂 04_CORRESPONDENCE/
> │    ├── 📄 20260101_C01_FORECL_FCFCU_DOC_D0073.pdf
> │    ├── 📄 20260207_C01_FORECL_FCFCU_MOTION_D0510.pdf
> │    ├── 📄 _04_CORRESPONDENCE.md
> │  └── 📂 04_FINANCIAL/
> │    ├── 📄 20250719_INV_Zoho_Corp_50100846854.pdf
> │    ├── 📄 20250729_INV_Zoho_Corp_50100879809.pdf
> │    ├── 📄 20250729_INV_Zoho_Corp_50100883027.pdf
> │    ├── 📄 20250807_INV_Zoho_Corp_50100916138.pdf
> │    ├── 📄 20251126_NOTICE_AES_Disconnect.pdf
> │    ├── 📄 20260115_INV_Tello_Mobile_82016155.pdf
> │    ├── 📄 20260115_INV_Tello_Mobile_82016231.pdf
> │    ├── 📄 20260115_INV_Tello_Mobile_82016359.pdf
> │    ├── 📄 20260115_INV_Tello_Mobile_82016391.pdf
> │    ├── 📄 20260115_INV_Zoho_Corp_50101514115.pdf
> │    ├── 📄 20260202_INV_Invoice_Generic_1.pdf
> │    ├── 📄 20260202_INV_Invoice_Generic_2.pdf
> │    ├── 📄 20260202_INV_Invoice_Generic_3.pdf
> │    ├── 📄 20260202_INV_Invoice_Generic_4.pdf
> │    ├── 📄 20260202_INV_Zoho_Corp_50100846854.pdf
> │    ├── 📄 20260202_INV_Zoho_Corp_50100879809.pdf
> │    ├── 📄 20260202_INV_Zoho_Corp_50100883027.pdf
> │    ├── 📄 20260202_INV_Zoho_Corp_50100916138.pdf
> │    ├── 📄 20260203_INV_Invoice_Generic_1.pdf
> │    ├── 📄 20260205_INV_RecordXchange_4_018222.pdf
> │    ├── 📄 _04_FINANCIAL.md
> │  └── 📂 05_EXPORTS/
> │    └── 📂 20260109_Hearing_Transcript_Exports/
> │      ├── 📄 20260209_C02_Site_Download_hearing_jan_09_2026.html
> │      ├── 📄 20260209_C02_hearing_jan_09_2026_transcript_regular.txt
> │      ├── 📄 _20260109_Hearing_Transcript_Exports.md
> │    ├── 📄 _05_EXPORTS.md
> │  └── 📂 05_LOGS/
> │    ├── 📄 20260203_C01_FORECL_FCFCU_DOC_D0551.pdf
> │    ├── 📄 20260203_C01_FORECL_FCFCU_ORDER_D0549.pdf
> │    ├── 📄 20260203_C01_FORECL_ORDER_D0550.pdf
> │    ├── 📄 20260210_REPORT_AI_Analysis_Grok.pdf
> │    ├── 📄 Service_Log.md
> │    ├── 📄 _05_LOGS.md
> │  ├── 📄 20251126_C02_VIDEO_D0440.mp4
> │  ├── 📄 20251203_C02_PHOTO_D0247.jpg
> │  ├── 📄 20251203_C02_VIDEO_D0439.mp4
> │  ├── 📄 20251209_C02_PHOTO_D0108.jpg
> │  ├── 📄 20260131_C03_FCRA_FCFCU_DISP_D0518.pdf
> │  ├── 📄 20261125_220020_C02_PHOTO_D0248.png
> │  └── 📂 99_ARCHIVE/
> │    ├── 📄 _99_ARCHIVE.md
> │  └── 📂 C00_DOCKET/
> │    ├── 📄 20250116_DKT_09_15_15_APPEARANCE.PDF
> │    ├── 📄 20250116_DKT_09_16_24_REQUEST_FOR_ADMISSIONS.PDF
> │    ├── 📄 20250116_DKT_09_17_12_NOTICE_TO_HOMEOWNERS.PDF
> │    ├── 📄 20250116_DKT_09_17_59_APPEARANCE.PDF
> │    ├── 📄 20250116_DKT_09_19_01_SUMMONS.PDF
> │    ├── 📄 20250116_DKT_09_19_33_SUMMONS.PDF
> │    ├── 📄 20250116_DKT_09_20_42_SUMMONS.PDF
> │    ├── 📄 20250116_DKT_09_21_26_SUMMONS.PDF
> │    ├── 📄 20250116_DKT_09_22_07_SUMMONS.PDF
> │    ├── 📄 20250116_DKT_COMPLAINT_AND_SUMMONS.PDF
> │    ├── 📄 20250305_DKT_SERVICE_RETURNED_SERVED_1.PDF
> │    ├── 📄 20250415_DKT_SERVICE_RETURNED_SERVED_2.PDF
> │    ├── 📄 20250513_DKT_14_52_56_MOTION_DEFAULT.PDF
> │    ├── 📄 20250513_DKT_14_53_36_AFFIDAVIT.PDF
> │    ├── 📄 20250513_DKT_14_54_31_AFFIDAVIT_ATTORNEY.PDF
> │    ├── 📄 20250513_DKT_MOTION_DEFAULT_JUDGMENT.PDF
> │    ├── 📄 20250521_DKT_14_25_43_OMITTED_NOTICE.PDF
> │    ├── 📄 20250521_DKT_USPS_CERTIFIED_RECEIPT.PDF
> │    ├── 📄 20250523_DKT_11_06_25_REQUEST_DEFAULT.PDF
> │    ├── 📄 20250523_DKT_MOTION_AMENDED_DEFAULT.PDF
> │    ├── 📄 20250528_DKT_PRAECIPE_FOR_SHERIFFS_SALES.PDF
> │    ├── 📄 20250529_DKT_AMENDED_DEFAULT_JUDGEMENT.PDF
> │    ├── 📄 20250709_DKT_NOTICE_SHERIFF_SALE_POSTED.PDF
> │    ├── 📄 20250717_DKT_PLAINTIFF_BID.PDF
> │    ├── 📄 20250909_DKT_DECREE_RETURNED.PDF
> │    ├── 📄 20251029_DKT_13_47_03_ORDER_FOR_WRIT.PDF
> │    ├── 📄 20251029_DKT_13_47_52_WRIT.PDF
> │    ├── 📄 20251029_DKT_PETITION_WRIT_ASSISTANCE.PDF
> │    ├── 📄 20251211_DKT_EMERGENCY_MOTION_STAY_WRIT.PDF
> │    ├── 📄 20251211_DKT_EXHIBIT_LIST.PDF
> │    ├── 📄 20251211_DKT_MOTION_TO_VACATE_JUDGMENT.PDF
> │    ├── 📄 20251211_DKT_PROPOSED_ORDER_STAY.PDF
> │    ├── 📄 20251211_DKT_PROPOSED_ORDER_VACATE.PDF
> │    ├── 📄 20251211_DKT_SUPPLEMENTAL_EMERGENCY_MOTION.PDF
> │    ├── 📄 20251212_DKT_NOTICE_OBTAIN_ITEM_REPORT.PDF
> │    ├── 📄 20251216_DKT_EMERGENCY_SUPPLEMENTAL_DECLARATION.PDF
> │    ├── 📄 20251216_DKT_MOTION_PRESERVE_SURPLUS.PDF
> │    ├── 📄 20251217_DKT_REPORT_SHERIFF_SALE.PDF
> │    ├── 📄 20251222_DKT_DECLARATION_ONGOING_DISPLACEMENT.PDF
> │    ├── 📄 20260109_DKT_HEARING_JOURNAL_ENTRY.PDF
> │    ├── 📄 20260121_DKT_ORDER_DENYING_VACATE.PDF
> │    ├── 📄 20260209_DKT_CASE_DOC_TEMPLATE.PDF
> │    ├── 📄 _C00_DOCKET.md
> │    ├── 📄 _MYCASE_DOCKET_SUMMARY.MD
> │  ├── 📄 C00_Hearing_Transcript_Recording_20260209_174803.mp4
> │  ├── 📄 Comparable_Market_Analysis_4817_Shadow_Pointe_Dr.html
> │  ├── 📄 _C00_Record_Defects.md
> │  ├── 📄 _C01_Service_Notice_Defects.md
> │  ├── 📄 _C02_EVIDENCE.md
> │  ├── 📄 _C02_Evidence_Preservation.md
> │  ├── 📄 _TOC.md
> └── 📂 C-02_Writ_Eviction_Irregularities/
> └── 📂 C-03_Post_Removal_Liability/
> │  └── 📂 01_PHOTOS/
> │    ├── 📄 20251209_C02_PHOTO_D0109.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0110.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0111.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0113.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0114.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0155.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0156.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0157.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0158.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0159.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0160.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0161.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0162.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0163.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0164.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0165.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0166.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0167.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0168.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0169.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0170.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0171.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0172.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0173.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0174.png
> │    ├── 📄 20251209_C02_PHOTO_D0175.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0176.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0177.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0178.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0179.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0180.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0181.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0182.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0183.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0184.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0185.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0186.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0188.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0189.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0190.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0191.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0192.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0193.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0194.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0195.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0196.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0197.png
> │    ├── 📄 20251209_C02_PHOTO_D0198.png
> │    ├── 📄 20251209_C02_PHOTO_D0199.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0200.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0201.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0202.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0203.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0204.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0205.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0206.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0207.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0208.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0209.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0210.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0211.jpg
> │    ├── 📄 20251209_C02_PHOTO_D0212.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0214.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0215.png
> │    ├── 📄 20251220_C02_PHOTO_D0216.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0217.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0218.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0219.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0220.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0221.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0222.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0223.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0225.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0226.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0227.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0228.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0229.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0230.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0231.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0233.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0234.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0235.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0236.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0237.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0238.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0239.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0240.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0241.png
> │    ├── 📄 20251220_C02_PHOTO_D0242.png
> │    ├── 📄 20251220_C02_PHOTO_D0243.jpg
> │    ├── 📄 20251220_C02_PHOTO_D0244.jpg
> │    ├── 📄 20260207_C02_PHOTO_D0213.jpg
> │    ├── 📄 20260207_C02_PHOTO_D0224.jpg
> │    ├── 📄 _01_PHOTOS.md
> │  └── 📂 02_VIDEO/
> │    ├── 📄 20251209_C02_VIDEO_D0104.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0105.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0106.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0249.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0250.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0251.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0252.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0253.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0254.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0255.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0256.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0257.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0258.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0259.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0260.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0261.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0262.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0263.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0264.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0265.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0266.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0267.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0268.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0269.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0270.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0271.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0272.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0273.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0274.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0275.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0276.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0277.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0278.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0279.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0280.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0281.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0282.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0283.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0284.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0285.mp4
> │    ├── 📄 20251209_C02_VIDEO_D0286.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0115.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0116.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0117.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0118.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0119.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0120.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0121.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0122.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0123.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0124.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0125.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0126.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0127.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0128.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0129.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0130.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0131.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0287.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0288.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0289.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0290.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0291.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0292.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0293.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0294.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0295.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0296.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0297.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0298.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0299.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0300.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0301.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0302.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0303.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0304.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0305.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0306.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0307.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0308.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0309.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0310.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0311.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0312.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0313.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0314.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0315.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0316.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0317.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0318.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0319.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0320.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0321.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0322.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0323.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0324.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0325.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0326.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0327.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0328.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0329.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0330.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0331.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0332.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0333.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0334.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0335.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0336.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0337.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0338.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0339.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0340.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0341.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0342.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0343.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0344.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0345.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0346.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0347.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0348.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0349.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0350.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0351.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0352.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0353.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0354.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0355.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0356.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0357.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0358.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0359.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0360.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0361.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0362.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0363.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0364.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0365.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0366.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0367.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0368.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0369.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0370.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0371.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0372.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0373.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0374.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0375.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0376.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0377.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0378.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0379.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0380.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0381.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0382.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0383.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0384.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0385.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0386.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0387.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0388.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0389.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0390.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0391.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0392.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0393.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0394.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0395.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0396.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0397.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0398.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0399.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0400.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0401.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0402.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0403.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0404.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0405.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0406.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0407.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0408.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0409.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0410.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0411.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0412.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0413.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0414.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0415.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0416.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0417.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0418.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0419.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0420.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0421.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0422.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0423.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0424.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0425.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0426.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0427.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0428.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0429.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0430.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0431.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0432.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0433.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0434.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0435.mp4
> │    ├── 📄 20251217_C02_VIDEO_D0436.mp4
> │    ├── 📄 20251220_C02_VIDEO_D0437.mp4
> │    ├── 📄 20251220_C02_VIDEO_D0438.mp4
> │    ├── 📄 Photo_Video_DB.csv
> │    ├── 📄 Photo_Video_DB_2ddf84a04402819ea365d894c16a3fdf_all.csv
> │    ├── 📄 _02_VIDEO.md
> │  └── 📂 03_DOCUMENTS/
> │    └── 📂 04_CORRESPONDENCE/
> │      ├── 📄 _04_CORRESPONDENCE.md
> │    ├── 📄 20241209_C02_FCFCU_VIDEO_D0071.pdf
> │    ├── 📄 20241211_C02_FCFCU_VIDEO_D0072.pdf
> │    ├── 📄 20260203_C00_DOC_D0476.pdf
> │    ├── 📄 20260207_C00_DOC_D0464.pdf
> │    ├── 📄 POST_INCIDENT_CONDITION_SUMMARY.md
> │    ├── 📄 _03_DOCUMENTS.md
> │  └── 📂 04_FINANCIAL/
> │    ├── 📄 20260203_C00_LSTRM_INV_D0492.pdf
> │    ├── 📄 20260203_C00_LSTRM_INV_D0521.pdf
> │    ├── 📄 20260203_C00_LSTRM_INV_D0522.pdf
> │    ├── 📄 20260203_C00_LSTRM_INV_D0523.pdf
> │    ├── 📄 Financial.csv
> │    ├── 📄 Financial_2cef84a044028021905ff6d8938abe93_all.csv
> │    ├── 📄 Financial_Tracker.md
> │    ├── 📄 Food_Purchase.md
> │    ├── 📄 Food_Purchase_(1).md
> │    ├── 📄 Food_Purchase_1.md
> │    ├── 📄 Food_Purchase_2.md
> │    ├── 📄 Food_Purchase_3.md
> │    ├── 📄 Food_Purchase_4.md
> │    ├── 📄 Gas_For_Lyft.md
> │    ├── 📄 Gas_Purchase_For_Lyft.md
> │    ├── 📄 Pet_Needs.md
> │    ├── 📄 _04_FINANCIAL.md
> │  └── 📂 05_EXPORTS/
> │    ├── 📄 EX_V_09_31_20251209_1018_mp4_—_OFFICER_POSITIONE.md
> │    ├── 📄 EX_V_09_46_20251209_1033_mp4_—_POST_REMOVAL_ENTR.md
> │    ├── 📄 _05_EXPORTS.md
> │    └── 📂 events/
> │      ├── 📄 025_12_09_Removal_Day_Camera_Bedroom.md
> │      ├── 📄 20250109_order_Court_Orders_And_Hearing_Schedule.md
> │      ├── 📄 20250109_order_Order_Court_Orders_And_Hearing_Sc.md
> │      ├── 📄 20250116_Case_Filed.md
> │      ├── 📄 20250116_court_filing_Case_Filed.md
> │      ├── 📄 20250303_Service_Issued.md
> │      ├── 📄 20250305_Service_Attempt_1.md
> │      ├── 📄 20250305_motion_Motion_Motion_Motion_To_Vacate_V.md
> │      ├── 📄 20250305_motion_Motion_Motion_To_Vacate_Void_Jud.md
> │      ├── 📄 20250305_motion_Motion_To_Vacate_Void_Judgement.md
> │      ├── 📄 20250409_service_Service_Attempt_2.md
> │      ├── 📄 20250415_Service_Attempt_2.md
> │      ├── 📄 20250513_Motion_for_Default_Judgment.md
> │      ├── 📄 20250513_motion_Motion_For_Default_Judgment.md
> │      ├── 📄 20250613_document_Sheriff_Sale_Notice_Posted.md
> │      ├── 📄 20250709_Sheriff_Sale_Notice_Posted.md
> │      ├── 📄 20250717_Plaintiff_Bid_Filed.md
> │      ├── 📄 20250805_document_030_Report_Sheriff_Sale_No_Exc.md
> │      ├── 📄 20250815_enforcement_Writ_Of_Assistance_Issued.md
> │      ├── 📄 20251126_Sheriff_At_Home_Unrelated_No_Notice.md
> │      ├── 📄 20251203_Police_Knocked_Then_Left_Quickly.md
> │      ├── 📄 20251207_Retrieval_Day.md
> │      ├── 📄 20251209_1033_Post_Removal_Entry_Privacy_Violati.md
> │      ├── 📄 20251209_1046_Camera_System_Manipulation.md
> │      ├── 📄 20251209_1048_Refrigerator_Unplugged.md
> │      ├── 📄 20251209_Removal_Day_Photos.md
> │      ├── 📄 20251214_Other_Camera_Porch_Activity.md
> │      ├── 📄 20251216_AES_Emergency_Notice.md
> │      ├── 📄 20251216_Emergency_Supplemental_Declaration_File.md
> │      ├── 📄 20251221_DOJ_Civil_Rights_Complaint_Submitted.md
> │      ├── 📄 EX_V_09_29_20251209_1016_mp4_—_SHERIFF_INSIDE_BE.md
> │      ├── 📄 EX_V_09_32_20251209_1019_mp4_—_CONTINUED_INTERFE.md
> │      ├── 📄 EX_V_09_33_20251209_1020_mp4_—_ROOM_VACANT_(BASE.md
> │      ├── 📄 EX_V_09_47_20251209_1034_mp4_—_ABSENCE_FROM_ROOM.md
> │      ├── 📄 EX_V_09_59_20251209_1046_mp4_—_RE_ENTRY_AND_CAME.md
> │      ├── 📄 EX_V_09_60_20251209_1047_mp4_—_ELECTRONICS_AND_C.md
> │      ├── 📄 EX_V_09_61_20251209_1048_mp4_—_REFRIGERATOR_UNPL.md
> │      ├── 📄 NT_Video_Narration_Log_Removal_Day.md
> │      ├── 📄 _checklist.md
> │      ├── 📄 _events.md
> │  ├── 📄 20260202_CAPTURE_Auto_Save_D0558.html
> │  ├── 📄 _03_EVIDENCE.md
> │  ├── 📄 _C04_Writ_Removal.md
> └── 📂 C-04_FCRA_Financial_Misconduct/
> │  └── 📂 01_PHOTOS/
> │    ├── 📄 20251220_C02_PHOTO_D0077.jpg
> │    ├── 📄 20260118_C02_PHOTO_D0246.jpeg
> │    ├── 📄 20260118_C02_PHOTO_D0473.jpeg
> │    ├── 📄 _01_PHOTOS.md
> │  └── 📂 03_DOCUMENTS/
> │    ├── 📄 20260118_C03_FCRA_COMPLAINT_D0478.pdf
> │    ├── 📄 20260118_C03_FCRA_EXPRN_ORDER_D0475.pdf
> │    ├── 📄 20260203_C03_EQFX_DOC_D0535.pdf
> │    ├── 📄 20260203_C03_FCRA_DISP_D0457.pdf
> │    ├── 📄 20260203_C03_FCRA_EQFX_DISP_D0483.pdf
> │    ├── 📄 20260203_C03_FCRA_EQFX_DISP_D0493.pdf
> │    ├── 📄 20260203_C03_FCRA_EQFX_JUDGM_D0531.pdf
> │    ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0455.pdf
> │    ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0456.pdf
> │    ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0459.pdf
> │    ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0537.pdf
> │    ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0538.pdf
> │    ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0539.pdf
> │    ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0519.pdf
> │    ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0520.pdf
> │    ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0543.pdf
> │    ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0544.pdf
> │    ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0545.pdf
> │    ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0486.pdf
> │    ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0498.pdf
> │    ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0500.pdf
> │    ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0501.pdf
> │    ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0541.pdf
> │    ├── 📄 20260203_C03_FCRA_TRNUN_ORDER_D0499.pdf
> │    ├── 📄 20260207_C03_FCRA_EQFX_DISP_D0480.pdf
> │    ├── 📄 20260207_C03_FCRA_EQFX_DISP_D0533.pdf
> │    ├── 📄 20260207_C03_FCRA_EQFX_JUDGM_D0003.pdf
> │    ├── 📄 20260207_C03_FCRA_EQFX_JUDGM_D0004.pdf
> │    ├── 📄 20260207_C03_FCRA_EQFX_JUDGM_D0529.pdf
> │    ├── 📄 20260207_C03_FCRA_FCFCU_JUDGM_D0006.pdf
> │    ├── 📄 20260207_C03_FCRA_FCFCU_JUDGM_D0530.pdf
> │    ├── 📄 20260207_C03_FCRA_TRNUN_DISP_D0467.pdf
> │    ├── 📄 20260207_C03_FCRA_TRNUN_DISP_D0485.pdf
> │    ├── 📄 20260207_C03_FCRA_TRNUN_DOC_D0468.pdf
> │    ├── 📄 20260207_C03_FCRA_TRNUN_DOC_D0470.pdf
> │    ├── 📄 20260207_C03_FCRA_TRNUN_DOC_D0471.pdf
> │    ├── 📄 20260207_C03_FCRA_TRNUN_VIDEO_D0472.pdf
> │    ├── 📄 20260207_C03_TRNUN_COMPLAINT_D0479.pdf
> │    ├── 📄 20260209_REPORT_CapOne_Credit_Ricevelasquez_A.pdf
> │    ├── 📄 20260209_REPORT_CapOne_Credit_Ricevelasquez_B.pdf
> │    ├── 📄 20260209_REPORT_CapOne_Credit_Ricevelasquez_James.pdf
> │    ├── 📄 _03_DOCUMENTS.md
> │  └── 📂 03_EVIDENCE/
> │    └── 📂 01_PHOTOS/
> │      ├── 📄 20240624_C02_PHOTO_D0076.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0078.png
> │      ├── 📄 20251220_C02_PHOTO_D0454.jpg
> │      ├── 📄 20260207_C02_PHOTO_D0245.jpg
> │      ├── 📄 _01_PHOTOS.md
> │    └── 📂 02_VIDEO/
> │      ├── 📄 _02_VIDEO.md
> │    └── 📂 03_DOCUMENTS/
> │      ├── 📄 20260101_C00_FCFCU_DOC_D0448.pdf
> │      ├── 📄 20260101_C00_FCFCU_DOC_D0450.pdf
> │      ├── 📄 20260108_C00_AES_DOC_D0474.pdf
> │      ├── 📄 20260203_C00_AES_DOC_D0460.pdf
> │      ├── 📄 20260203_C00_DOC_D0441.pdf
> │      ├── 📄 20260203_C00_DOC_D0458.pdf
> │      ├── 📄 20260203_C00_FCFCU_DOC_D0442.pdf
> │      ├── 📄 20260203_C00_FCFCU_DOC_D0443.pdf
> │      ├── 📄 20260203_C00_FCFCU_DOC_D0444.pdf
> │      ├── 📄 20260203_C00_FCFCU_DOC_D0446.pdf
> │      ├── 📄 20260203_C00_FCFCU_DOC_D0447.pdf
> │      ├── 📄 20260203_C00_FCFCU_DOC_D0449.pdf
> │      ├── 📄 20260203_C00_INV_D0445.pdf
> │      ├── 📄 20260208_REPORT_Credit_Analysis_WalletHub.pdf
> │      ├── 📄 20260208_REPORT_WalletHub_Credit_Analysis.pdf
> │      ├── 📄 20260209_REPORT_Credit_Report.pdf
> │      ├── 📄 FCFCU_NOTICE_Direct_Dispute_Deletion_Demand.pdf
> │      ├── 📄 _03_DOCUMENTS.md
> │    └── 📂 04_FINANCIAL/
> │      ├── 📄 _04_FINANCIAL.md
> │    └── 📂 05_EXPORTS/
> │      ├── 📄 _05_EXPORTS.md
> │    ├── 📄 _03_EVIDENCE.md
> │  └── 📂 04_FINANCIAL/
> │    ├── 📄 20260207_C02_PHOTO_D0466.jpg
> │    ├── 📄 20260207_C03_FCRA_EQFX_INV_D0001.pdf
> │    ├── 📄 20260207_C03_FCRA_EQFX_INV_D0461.pdf
> │    ├── 📄 20260207_C03_FCRA_LSTRM_INV_D0002.pdf
> │    ├── 📄 20260207_C03_FCRA_LSTRM_INV_D0005.pdf
> │    ├── 📄 20260207_C03_FCRA_LSTRM_INV_D0462.pdf
> │    ├── 📄 20260207_C03_FCRA_LSTRM_INV_D0463.pdf
> │    ├── 📄 _04_FINANCIAL.md
> │  ├── 📄 20260202_CAPTURE_Auto_Save_D0525.html
> │  ├── 📄 20260202_CAPTURE_Auto_Save_D0526.html
> │  ├── 📄 20260202_CAPTURE_Auto_Save_D0528.html
> │  ├── 📄 20260202_CAPTURE_Auto_Save_D0534.html
> │  ├── 📄 20260202_CAPTURE_Auto_Save_D0536.html
> │  ├── 📄 20260202_CAPTURE_Auto_Save_D0540.html
> │  ├── 📄 20260202_CAPTURE_Auto_Save_D0559.html
> │  ├── 📄 20260202_CAPTURE_Auto_Save_D0560.html
> │  ├── 📄 20260202_CAPTURE_Auto_Save_D0563.html
> │  ├── 📄 20260202_CAPTURE_Auto_Save_D0564.html
> │  ├── 📄 20260203_CAPTURE_Auto_Save_D0515.html
> │  ├── 📄 20260203_CAPTURE_Auto_Save_D0527.html
> │  ├── 📄 20260203_CAPTURE_Auto_Save_D0532.html
> │  ├── 📄 20260203_CAPTURE_Auto_Save_D0542.html
> │  ├── 📄 20260203_CAPTURE_Auto_Save_D0546.html
> │  ├── 📄 20260203_CAPTURE_Auto_Save_D0547.html
> │  ├── 📄 _03_EVIDENCE.md
> │  ├── 📄 _C03_Credit_Reporting_FCRA.md
> │  ├── 📄 _C07_Financial_Misconduct.md
> └── 📂 C-05_Accounting_Surplus/
> ├── 📄 _99_VAULT.md
> └── 📄 _TOC.md
> ```

### Assistant
> Gemini “dipping” into `99_VAULT` is exactly what happens when the agent can’t tell **Work Product** vs **Evidence-of-record** vs **Scratch**. Your vault is trying to be all three, so the model wanders.
> 
> You don’t need a full redesign. You need **hard boundaries + one intake chute + one publish lane**.
> 
> ## What’s wrong (fast diagnosis)
> 1) **Duplicates of the same concept** inside a case folder:
> - You have `01_PHOTOS`, `02_VIDEO`, `03_DOCUMENTS` **and also** `03_EVIDENCE/01_PHOTOS/02_VIDEO/03_DOCUMENTS/...`
> - That’s “two vaults” inside one case → guaranteed drift.
> 
> 2) **Loose files at the phase root** (the orphan stuff at `C-01/...` root) → the agent uses those as a dumping ground.
> 
> 3) **Mixed intent folders**:
> - `00_RECEIVED` (intake), `00_drafts` (scratch), `01_FILED` (court record), `05_LOGS` (metadata), `04_FINANCIAL` (damages), plus photos/videos scattered.
> That’s fine, but only if *each item has a single home*.
> 
> ## The rule that fixes this
> ### `99_VAULT` = immutable evidence only.
> No drafts. No working docs. No “auto save”. No exports generated by tools unless they’re final exhibits or logs.
> 
> Work product belongs in **phase work** (your `02_PHASE_WORK/...` folders) and gets *copied* into vault only when it becomes an exhibit or filed item.
> 
> ---
> 
> # Your target structure (minimal surgery)
> 
> Inside each `C-xx_*` folder, keep ONLY these top-level buckets:
> 
> ```text
> 00_INTAKE/        (everything new lands here first)
> 10_EVIDENCE/      (immutable originals + normalized media)
> 20_COURT_RECORD/  (filed, orders, notices, docket PDFs)
> 30_CORRESP/       (emails, letters, mail proofs)
> 40_FINANCIAL/     (invoices, receipts, damage proofs)
> 90_EXPORTS/       (generated transcripts, renderings, tool outputs)
> 99_ADMIN/         (indexes, manifests, log, mapping tables)
> 99_QUARANTINE/    (duplicates, unknowns, needs review)
> ```
> 
> And under `10_EVIDENCE/` you standardize:
> 
> ```text
> 10_EVIDENCE/
>   01_PHOTOS/
>   02_VIDEO/
>   03_DOCS/
>   04_AUDIO/ (optional)
> ```
> 
> ### Delete (or deprecate) the duplicate tree
> Pick ONE:
> - either keep `01_PHOTOS/02_VIDEO/03_DOCUMENTS` **OR**
> - keep `03_EVIDENCE/01_PHOTOS/02_VIDEO/03_DOCUMENTS`
> 
> **Best move:** keep the clearer one: `10_EVIDENCE/*` and kill the confusing “03_EVIDENCE” naming (because you already have “03_DOCUMENTS” which collides).
> 
> ---
> 
> # Concrete moves for what you showed
> 
> ## 1) Collapse the duplicates in `C-01_Jurisdictional_Defects`
> - Move everything from:
>   - `C-01/.../01_PHOTOS` → `C-01/.../10_EVIDENCE/01_PHOTOS`
>   - `C-01/.../02_VIDEO` → `C-01/.../10_EVIDENCE/02_VIDEO`
>   - `C-01/.../03_DOCUMENTS` → split:
>     - filed things → `20_COURT_RECORD/`
>     - correspondence → `30_CORRESP/`
>     - drafts/templates → **NOT IN VAULT** (send to phase work repo)
>     - reports (appraisal, shadowpointe) → `40_FINANCIAL/` or `10_EVIDENCE/03_DOCS/` depending if it’s valuation evidence
> 
> - Then **remove or freeze**:
>   - `C-01/.../03_EVIDENCE/` (or make it a symlink/redirect note and stop using it)
> 
> ## 2) Stop letting “drafts” live in the vault
> Anything like:
> - `*_Auto_Save_*.html`
> - `.mw` markwhen working file
> - `.pptx` working deck
> - `.docx` working appellate doc
> 
> Those go to:
> `02_PHASE_WORK/<phase>/.../drafts/` (or your docs repo), not `99_VAULT`.
> 
> In the vault you keep only:
> - the final PDF you filed
> - the final exhibit you attached
> - the final exported transcript you are relying on (and even that can be in `90_EXPORTS`)
> 
> ## 3) Quarantine the orphans at the phase root
> These:
> - `20251126_C02_VIDEO_D0440.mp4`, etc.
> Move them into `99_QUARANTINE/` **immediately**, then later re-home them into the correct `C-xx/.../10_EVIDENCE/...` folder when you confirm phase.
> 
> This one move prevents “random stuff at root” forever.
> 
> ---
> 
> # “Agent-proofing” so it can’t wander again
> 
> ## A) Put a red-line README at `99_VAULT/_99_VAULT.md`
> Add a rule block like:
> 
> - `99_VAULT is immutable evidence only.`
> - `No drafts, no working documents, no auto-save captures.`
> - `All new items go to 00_INTAKE then get processed.`
> - `Work product lives in 02_PHASE_WORK and is copied in only when final.`
> 
> Agents respect boundary text if it’s blunt and repeated.
> 
> ## B) Add one universal “INBOX” folder
> At the top of `99_VAULT` add:
> 
> `00_INBOX_DROP/`
> 
> Everything from phone, email, downloads goes there first. Then you run your organizer script/triage.
> 
> ---
> 
> # Short execution checklist (do this in order)
> 
> 1) **Create** the standardized buckets in each `C-xx` you care about (start with C-01, C-03, C-04).
> 2) **Move** `00_drafts` out of the vault (to phase work). Leave behind an `_MOVED.md` stub so you can find it later.
> 3) **Collapse** duplicate evidence trees (choose one canonical `10_EVIDENCE/*`).
> 4) **Sweep** root-level orphan files into `99_QUARANTINE/`.
> 5) **Write** `99_VAULT/_99_VAULT.md` with rules + “INBOX only” policy.
> 
> ---
> 
> # If you want the cleanest “single source of truth”
> - Vault stores **originals** and **final artifacts only**.
> - MkDocs site reads from:
>   - `02_PHASE_WORK` (narratives, trackers, writing)
>   - and links to vault PDFs via stable paths (or a doc server).
> - Case RAG ingests:
>   - `02_PHASE_WORK` markdown + selected vault PDFs (not drafts, not duplicates).
> - Paperless is your ingestion front door:
>   - Paperless tags → determine which `C-xx` + bucket it belongs to.
> 
> ---
> 
> If you paste the **exact 7 phases** (just names/IDs) I’ll map:
> - which `C-xx` folders belong to which phase,
> - and give you a deterministic rule: `phase_id + doc_type -> path`
> so this can be automated in your RAG ingestion rules + Paperless tags without human sorting.

### User
> what were the 7 phases we landed on?

### Assistant
> I don’t have the exact “final 7” captured in this chat history snippet, so I can’t truthfully quote them back like a receipt.
> 
> But based on what **you** have repeatedly treated as the case spine (and what you listed as the “main things”), the 7-phase set we were effectively operating under is this:
> 
> 1) **Record Integrity & Docket Control**  
>    (master docket verification, order sequence, timestamp audit, missing filings)
> 
> 2) **Jurisdiction / Service / Notice Defects**  
>    (mailing/publication/posting defects, 48-hour notice issues, due process)
> 
> 3) **Writ / Eviction Irregularities**  
>    (unknown occupants narrative, procedural skips, enforcement defects)
> 
> 4) **Conduct / ADA / Civil Rights**  
>    (accommodations, unnecessary force, disability impacts, Title II-type framing)
> 
> 5) **Evidence Preservation & Spoliation**  
>    (litigation holds, chain of custody, missing/altered media, preservation demands)
> 
> 6) **Credit Reporting / FCRA & Secondary Harm**  
>    (furnisher/bureau disputes, reinsertion, inaccuracies, denial letters, damages)
> 
> 7) **Accounting / Surplus / Valuation & Damages**  
>    (math reconciliation, fees/interest inflation, surplus impossibility, valuation proof)
> 
> If you want, paste the “phase master” header file you’re using (the one with the spine list), and I’ll lock the names/IDs exactly and generate the canonical folder map + Zoho lanes so Gemini stops inventing extra phases.

### User
> confirm please. ```json
> {
>   "$schema": "https://json-schema.org/draft/2020-12/schema",
>   "$id": "https://qially.me/schemas/fcfcu_case_master.schema.json",
>   "title": "FCFCU Case Master Tables (Source-of-Truth) Schema",
>   "type": "object",
>   "additionalProperties": false,
>   "properties": {
>     "PHASE_MASTER": { "$ref": "#/$defs/PHASE_MASTER" },
>     "ACTOR_MASTER": { "$ref": "#/$defs/ACTOR_MASTER" },
>     "ENTITY_MASTER": { "$ref": "#/$defs/ENTITY_MASTER" },
>     "VIOLATION_MASTER": { "$ref": "#/$defs/VIOLATION_MASTER" },
>     "EVENT_LOG": { "$ref": "#/$defs/EVENT_LOG" },
>     "DOCUMENT_REGISTRY": { "$ref": "#/$defs/DOCUMENT_REGISTRY" },
>     "DISPUTE_LOG": { "$ref": "#/$defs/DISPUTE_LOG" },
>     "DAMAGES_LEDGER": { "$ref": "#/$defs/DAMAGES_LEDGER" }
>   },
>   "required": [
>     "PHASE_MASTER",
>     "ACTOR_MASTER",
>     "ENTITY_MASTER",
>     "VIOLATION_MASTER",
>     "EVENT_LOG",
>     "DOCUMENT_REGISTRY",
>     "DISPUTE_LOG",
>     "DAMAGES_LEDGER"
>   ],
>   "$defs": {
>     "id_string": {
>       "type": "string",
>       "minLength": 3,
>       "pattern": "^[A-Z0-9_\\-\\.]+$",
>       "description": "Uppercase, prefix-based, no spaces."
>     },
> 
>     "PHASE_MASTER": {
>       "type": "array",
>       "items": {
>         "type": "object",
>         "additionalProperties": false,
>         "properties": {
>           "phase_id": { "allOf": [{ "$ref": "#/$defs/id_string" }, { "pattern": "^P_[A-Z0-9_\\-\\.]+$" }] },
>           "phase_code": { "type": "string", "pattern": "^C\\d{2}$" },
>           "phase_name": { "type": "string", "minLength": 2 },
>           "strategy_thesis": { "type": "string", "minLength": 2 },
>           "elements_to_prove": { "type": "string", "minLength": 2 },
>           "primary_remedies": { "type": "string", "minLength": 2 },
>           "success_criteria": { "type": "string", "minLength": 2 },
>           "status": { "type": "string", "enum": ["ACTIVE", "SUPPORTING", "CLOSED"] },
>           "priority": { "type": "integer", "minimum": 1, "maximum": 5 }
>         },
>         "required": [
>           "phase_id",
>           "phase_code",
>           "phase_name",
>           "strategy_thesis",
>           "elements_to_prove",
>           "primary_remedies",
>           "success_criteria",
>           "status",
>           "priority"
>         ]
>       }
>     },
> 
>     "ACTOR_MASTER": {
>       "type": "array",
>       "items": {
>         "type": "object",
>         "additionalProperties": false,
>         "properties": {
>           "actor_id": { "allOf": [{ "$ref": "#/$defs/id_string" }, { "pattern": "^A_[A-Z0-9_\\-\\.]+$" }] },
>           "actor_type": { "type": "string", "enum": ["PERSON", "ORG", "GOV", "COURT", "AGENCY", "VENDOR"] },
>           "display_name": { "type": "string", "minLength": 2 },
>           "role_tags": { "type": "string", "minLength": 1, "description": "Comma-separated tags." },
>           "alt_names": { "type": "string" },
>           "contact_info": { "type": "string" },
>           "notes": { "type": "string" }
>         },
>         "required": ["actor_id", "actor_type", "display_name", "role_tags"]
>       }
>     },
> 
>     "ENTITY_MASTER": {
>       "type": "array",
>       "items": {
>         "type": "object",
>         "additionalProperties": false,
>         "properties": {
>           "entity_id": { "allOf": [{ "$ref": "#/$defs/id_string" }, { "pattern": "^E_[A-Z0-9_\\-\\.]+$" }] },
>           "entity_type": {
>             "type": "string",
>             "enum": ["PROPERTY", "LOAN", "ACCOUNT", "TRADELINE", "UTILITY", "DEVICE", "CASE", "ADDRESS", "EVIDENCE_SET"]
>           },
>           "display_name": { "type": "string", "minLength": 2 },
>           "owner_actor_id": { "type": "string", "pattern": "^A_[A-Z0-9_\\-\\.]+$" },
>           "identifiers": { "type": "string" },
>           "notes": { "type": "string" }
>         },
>         "required": ["entity_id", "entity_type", "display_name"]
>       }
>     },
> 
>     "VIOLATION_MASTER": {
>       "type": "array",
>       "items": {
>         "type": "object",
>         "additionalProperties": false,
>         "properties": {
>           "violation_id": { "allOf": [{ "$ref": "#/$defs/id_string" }, { "pattern": "^V_[A-Z0-9_\\-\\.]+$" }] },
>           "phase_id": { "type": "string", "pattern": "^P_[A-Z0-9_\\-\\.]+$" },
>           "actor_id": { "type": "string", "pattern": "^A_[A-Z0-9_\\-\\.]+$" },
>           "entity_id": { "type": "string", "pattern": "^E_[A-Z0-9_\\-\\.]+$" },
>           "violation_group": { "type": "string", "minLength": 2 },
>           "statute_or_theory": { "type": "string", "minLength": 2 },
>           "description": { "type": "string", "minLength": 2 },
>           "start_date": { "type": "string", "format": "date" },
>           "end_date": { "type": "string", "format": "date" },
>           "ongoing": { "type": "boolean" },
>           "severity": { "type": "string", "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"] },
>           "status": { "type": "string", "enum": ["SUSPECTED", "SUPPORTED", "PROVEN", "CURED", "DISPUTED"] }
>         },
>         "required": [
>           "violation_id",
>           "phase_id",
>           "actor_id",
>           "violation_group",
>           "statute_or_theory",
>           "description",
>           "start_date",
>           "ongoing",
>           "severity",
>           "status"
>         ]
>       }
>     },
> 
>     "EVENT_LOG": {
>       "type": "array",
>       "items": {
>         "type": "object",
>         "additionalProperties": false,
>         "properties": {
>           "event_id": { "allOf": [{ "$ref": "#/$defs/id_string" }, { "pattern": "^EV_[A-Z0-9_\\-\\.]+$" }] },
>           "event_datetime": { "type": "string", "format": "date-time" },
>           "phase_id": { "type": "string", "pattern": "^P_[A-Z0-9_\\-\\.]+$" },
>           "event_type": { "type": "string", "minLength": 2 },
>           "primary_actor_id": { "type": "string", "pattern": "^A_[A-Z0-9_\\-\\.]+$" },
>           "entity_id": { "type": "string", "pattern": "^E_[A-Z0-9_\\-\\.]+$" },
>           "violation_id": { "type": "string", "pattern": "^V_[A-Z0-9_\\-\\.]+$" },
>           "summary": { "type": "string", "minLength": 2 },
>           "doc_ids": { "type": "string", "description": "Comma-separated doc_id(s)." },
>           "confidence": { "type": "string", "enum": ["LOW", "MEDIUM", "HIGH"] }
>         },
>         "required": ["event_id", "event_datetime", "phase_id", "event_type", "primary_actor_id", "summary", "confidence"]
>       }
>     },
> 
>     "DOCUMENT_REGISTRY": {
>       "type": "array",
>       "items": {
>         "type": "object",
>         "additionalProperties": false,
>         "properties": {
>           "doc_id": { "allOf": [{ "$ref": "#/$defs/id_string" }, { "pattern": "^D_[A-Z0-9_\\-\\.]+$" }] },
>           "date": { "type": "string", "format": "date" },
>           "doc_type": {
>             "type": "string",
>             "enum": [
>               "COURT_FILING",
>               "COURT_ORDER",
>               "SHERIFF_RETURN",
>               "CREDIT_REPORT",
>               "DISPUTE_LETTER",
>               "EMAIL",
>               "VIDEO",
>               "PHOTO",
>               "INVOICE",
>               "UTILITY_NOTICE",
>               "TRANSCRIPT",
>               "EXPORT",
>               "OTHER"
>             ]
>           },
>           "phase_id": { "type": "string", "pattern": "^P_[A-Z0-9_\\-\\.]+$" },
>           "source_actor_id": { "type": "string", "pattern": "^A_[A-Z0-9_\\-\\.]+$" },
>           "entity_id": { "type": "string", "pattern": "^E_[A-Z0-9_\\-\\.]+$" },
>           "event_id": { "type": "string", "pattern": "^EV_[A-Z0-9_\\-\\.]+$" },
>           "file_path": { "type": "string", "minLength": 3 },
>           "hash": { "type": "string" },
>           "notes": { "type": "string" }
>         },
>         "required": ["doc_id", "date", "doc_type", "phase_id", "file_path"]
>       }
>     },
> 
>     "DISPUTE_LOG": {
>       "type": "array",
>       "items": {
>         "type": "object",
>         "additionalProperties": false,
>         "properties": {
>           "dispute_id": { "allOf": [{ "$ref": "#/$defs/id_string" }, { "pattern": "^DS_[A-Z0-9_\\-\\.]+$" }] },
>           "date_sent": { "type": "string", "format": "date" },
>           "phase_id": { "type": "string", "pattern": "^P_[A-Z0-9_\\-\\.]+$" },
>           "actor_id": { "type": "string", "pattern": "^A_[A-Z0-9_\\-\\.]+$" },
>           "entity_id": { "type": "string", "pattern": "^E_[A-Z0-9_\\-\\.]+$" },
>           "violation_id": { "type": "string", "pattern": "^V_[A-Z0-9_\\-\\.]+$" },
>           "tracking_number": { "type": "string" },
>           "method": { "type": "string", "enum": ["CERTIFIED_MAIL", "EMAIL", "CFPB_PORTAL", "CRA_PORTAL", "FAX", "OTHER"] },
>           "deadline": { "type": "string", "format": "date" },
>           "response_received": { "type": "boolean" },
>           "outcome": { "type": "string", "enum": ["PENDING", "VERIFIED", "DELETED", "UPDATED", "NO_RESPONSE", "REINSERTED", "PARTIAL"] },
>           "doc_id": { "type": "string", "pattern": "^D_[A-Z0-9_\\-\\.]+$" }
>         },
>         "required": ["dispute_id", "date_sent", "phase_id", "actor_id", "entity_id", "method", "response_received", "outcome", "doc_id"]
>       }
>     },
> 
>     "DAMAGES_LEDGER": {
>       "type": "array",
>       "items": {
>         "type": "object",
>         "additionalProperties": false,
>         "properties": {
>           "damage_id": { "allOf": [{ "$ref": "#/$defs/id_string" }, { "pattern": "^DM_[A-Z0-9_\\-\\.]+$" }] },
>           "date_incurred": { "type": "string", "format": "date" },
>           "phase_id": { "type": "string", "pattern": "^P_[A-Z0-9_\\-\\.]+$" },
>           "actor_id": { "type": "string", "pattern": "^A_[A-Z0-9_\\-\\.]+$" },
>           "entity_id": { "type": "string", "pattern": "^E_[A-Z0-9_\\-\\.]+$" },
>           "event_id": { "type": "string", "pattern": "^EV_[A-Z0-9_\\-\\.]+$" },
>           "violation_id": { "type": "string", "pattern": "^V_[A-Z0-9_\\-\\.]+$" },
>           "category": { "type": "string", "enum": ["OUT_OF_POCKET", "PROPERTY", "CREDIT", "OPPORTUNITY", "STATUTORY", "OTHER"] },
>           "subtype": { "type": "string", "minLength": 2 },
>           "amount": { "type": "number", "minimum": 0 },
>           "calc_method": { "type": "string", "enum": ["ACTUAL", "ESTIMATE", "RANGE", "STATUTORY"] },
>           "doc_id": { "type": "string", "pattern": "^D_[A-Z0-9_\\-\\.]+$" },
>           "reimbursed": { "type": "boolean" },
>           "notes": { "type": "string" }
>         },
>         "required": ["damage_id", "date_incurred", "phase_id", "category", "subtype", "amount", "calc_method", "reimbursed"]
>       }
>     }
>   }
> }
> ```
> 
> ---
> 
> # Google Sheets Validation Guide (practical + strict)
> 
> ## 0) Sheet Setup (do this once)
> 
> Create these tabs (exact names):
> 
> * `PHASE_MASTER`
> * `ACTOR_MASTER`
> * `ENTITY_MASTER`
> * `VIOLATION_MASTER`
> * `EVENT_LOG`
> * `DOCUMENT_REGISTRY`
> * `DISPUTE_LOG`
> * `DAMAGES_LEDGER`
> * `VALIDATION` (helper tab)
> 
> In `VALIDATION`, build **named ranges** (Data → Named ranges):
> 
> | Named Range     | Range (example)          | Purpose             |
> | --------------- | ------------------------ | ------------------- |
> | `PHASE_IDS`     | `PHASE_MASTER!A2:A`      | `phase_id` list     |
> | `ACTOR_IDS`     | `ACTOR_MASTER!A2:A`      | `actor_id` list     |
> | `ENTITY_IDS`    | `ENTITY_MASTER!A2:A`     | `entity_id` list    |
> | `VIOLATION_IDS` | `VIOLATION_MASTER!A2:A`  | `violation_id` list |
> | `EVENT_IDS`     | `EVENT_LOG!A2:A`         | `event_id` list     |
> | `DOC_IDS`       | `DOCUMENT_REGISTRY!A2:A` | `doc_id` list       |
> 
> Assumption: Column A is each table’s primary key.
> 
> ---
> 
> ## 1) Data Validation Dropdowns (ENUMs)
> 
> ### PHASE_MASTER
> 
> * `status`: allow list → `ACTIVE,SUPPORTING,CLOSED`
> * `priority`: number between `1` and `5`
> 
> ### ACTOR_MASTER
> 
> * `actor_type`: `PERSON,ORG,GOV,COURT,AGENCY,VENDOR`
> 
> ### ENTITY_MASTER
> 
> * `entity_type`: `PROPERTY,LOAN,ACCOUNT,TRADELINE,UTILITY,DEVICE,CASE,ADDRESS,EVIDENCE_SET`
> 
> ### VIOLATION_MASTER
> 
> * `severity`: `LOW,MEDIUM,HIGH,CRITICAL`
> * `status`: `SUSPECTED,SUPPORTED,PROVEN,CURED,DISPUTED`
> * `ongoing`: checkbox
> 
> ### EVENT_LOG
> 
> * `confidence`: `LOW,MEDIUM,HIGH`
> 
> ### DOCUMENT_REGISTRY
> 
> * `doc_type`: `COURT_FILING,COURT_ORDER,SHERIFF_RETURN,CREDIT_REPORT,DISPUTE_LETTER,EMAIL,VIDEO,PHOTO,INVOICE,UTILITY_NOTICE,TRANSCRIPT,EXPORT,OTHER`
> 
> ### DISPUTE_LOG
> 
> * `method`: `CERTIFIED_MAIL,EMAIL,CFPB_PORTAL,CRA_PORTAL,FAX,OTHER`
> * `response_received`: checkbox
> * `outcome`: `PENDING,VERIFIED,DELETED,UPDATED,NO_RESPONSE,REINSERTED,PARTIAL`
> 
> ### DAMAGES_LEDGER
> 
> * `category`: `OUT_OF_POCKET,PROPERTY,CREDIT,OPPORTUNITY,STATUTORY,OTHER`
> * `calc_method`: `ACTUAL,ESTIMATE,RANGE,STATUTORY`
> * `reimbursed`: checkbox
> 
> ---
> 
> ## 2) Foreign Key Validation (no linking tables, just FK cells)
> 
> ### Option A (Recommended): Dropdown from named range
> 
> For FK columns like `phase_id`, `actor_id`, etc:
> 
> * Data validation → “Dropdown (from a range)”
> * Use the named range (ex: `=PHASE_IDS`)
> 
> This prevents bad IDs outright.
> 
> ### Option B: Formula-based validation (catches blanks vs invalid)
> 
> Use Data validation → “Custom formula is”:
> 
> **phase_id valid**
> 
> ```gs
> =OR($B2="",COUNTIF(PHASE_IDS,$B2)>0)
> ```
> 
> **actor_id valid**
> 
> ```gs
> =OR($C2="",COUNTIF(ACTOR_IDS,$C2)>0)
> ```
> 
> **entity_id valid**
> 
> ```gs
> =OR($D2="",COUNTIF(ENTITY_IDS,$D2)>0)
> ```
> 
> **doc_id valid**
> 
> ```gs
> =OR($H2="",COUNTIF(DOC_IDS,$H2)>0)
> ```
> 
> Adjust column letters to your sheet.
> 
> ---
> 
> ## 3) Primary Key Uniqueness (hard fail)
> 
> Add conditional formatting to Column A in every table:
> 
> Custom formula:
> 
> ```gs
> =COUNTIF($A$2:$A,$A2)>1
> ```
> 
> Format: red fill.
> 
> Also add “Text is not empty” rule if you want strictness:
> 
> * Data validation: “Text is not empty” for required columns.
> 
> ---
> 
> ## 4) ID Prefix Enforcement (cheap but effective)
> 
> Conditional formatting rules on Column A:
> 
> ### PHASE_MASTER (P_)
> 
> ```gs
> =AND($A2<>"",NOT(REGEXMATCH($A2,"^P_[A-Z0-9_\-\.]+$")))
> ```
> 
> ### ACTOR_MASTER (A_)
> 
> ```gs
> =AND($A2<>"",NOT(REGEXMATCH($A2,"^A_[A-Z0-9_\-\.]+$")))
> ```
> 
> ### ENTITY_MASTER (E_)
> 
> ```gs
> =AND($A2<>"",NOT(REGEXMATCH($A2,"^E_[A-Z0-9_\-\.]+$")))
> ```
> 
> …and so on for `V_`, `EV_`, `D_`, `DS_`, `DM_`.
> 
> ---
> 
> ## 5) Date / DateTime Enforcement
> 
> ### Dates (YYYY-MM-DD)
> 
> Data validation → “Custom formula is”:
> 
> ```gs
> =OR($E2="",REGEXMATCH(TEXT($E2,"yyyy-mm-dd"),"^\d{4}-\d{2}-\d{2}$"))
> ```
> 
> ### Datetime (ISO-ish)
> 
> If you store datetime as Google datetime, validate it’s not blank + is a number:
> 
> ```gs
> =OR($B2="",ISNUMBER($B2))
> ```
> 
> (Then format the column as Date time.)
> 
> ---
> 
> ## 6) Attachment / File Path sanity (Obsidian-friendly)
> 
> In `DOCUMENT_REGISTRY!file_path` add validation to discourage junk:
> 
> Custom formula:
> 
> ```gs
> =AND($H2<>"",NOT(REGEXMATCH($H2,"[<>:\"|?*]")))
> ```
> 
> Optional (encourage relative paths):
> 
> ```gs
> =AND($H2<>"",NOT(REGEXMATCH($H2,"^[A-Za-z]:\\\\")))
> ```
> 
> ---
> 
> ## 7) “Required Fields Missing” Spotlight (fast triage)
> 
> Add a helper column at the end of each table called `row_errors`.
> 
> Example for `VIOLATION_MASTER` (adjust columns to your layout):
> 
> ```gs
> =TEXTJOIN(" | ",TRUE,
> IF($A2="","missing violation_id",""),
> IF($B2="","missing phase_id",""),
> IF($C2="","missing actor_id",""),
> IF($F2="","missing statute_or_theory",""),
> IF($G2="","missing description",""),
> IF($H2="","missing start_date","")
> )
> ```
> 
> Then conditional format the row when `row_errors` not blank:
> 
> ```gs
> =$Z2<>""
> ```
> 
> ---
> 
> If you tell me the **exact column order** you’re using in each tab (or paste one header row), I’ll generate the **exact validation formulas** per sheet with correct column letters so you can copy/paste without thinking.```markdown
> . 📂 30.05.01_FCFCU
> ├── 📄 CASE_FCFCU.code-workspace
> └── 📂 app/
> │  └── 📂 case_rag/
> │  └── 📂 mkdocs/
> │    ├── 📄 Dockerfile
> │    ├── 📄 LICENSE
> │    ├── 📄 Pipfile
> │    ├── 📄 Pipfile.lock
> │    ├── 📄 README.md
> │    ├── 📄 amplify.yml
> │    ├── 📄 docker-compose.yml
> │    └── 📂 docs_sample/
> │      ├── 📄 CNAME
> │      └── 📂 assets/
> │        └── 📂 css/
> │          ├── 📄 custom.css
> │      └── 📂 extensions/
> │        ├── 📄 code-hilite.md
> │        ├── 📄 footnote.md
> │        ├── 📄 mathjax.md
> │      └── 📂 getting-started/
> │        ├── 📄 docker.md
> │        ├── 📄 download-boilerplate.md
> │        ├── 📄 invoke.md
> │        ├── 📄 pip.md
> │        ├── 📄 pipenv.md
> │      └── 📂 hosting-and-deployment/
> │        ├── 📄 aws-amplify-console.md
> │        ├── 📄 combinations.md
> │        ├── 📄 github-pages.md
> │        ├── 📄 gitlab-pages.md
> │        ├── 📄 netlify.md
> │      └── 📂 images/
> │        ├── 📄 graduate-cap.192x192.png
> │        ├── 📄 graduate-cap.48x48.png
> │        ├── 📄 graduate-cap.96x96.png
> │        ├── 📄 graduate-cap.png
> │        ├── 📄 material.png
> │      ├── 📄 index.md
> │      ├── 📄 license.md
> │      ├── 📄 manifest.json
> │      ├── 📄 material-for-mkdocs.md
> │    ├── 📄 mkdocs-sample.yml
> │    ├── 📄 netlify.toml
> │    ├── 📄 renovate.json
> │    ├── 📄 requirements-dev.txt
> │    ├── 📄 requirements.txt
> │    ├── 📄 runtime.txt
> │  └── 📂 paperless_fcfcu/
> │    ├── 📄 backup_case_evidence.cmd
> │    └── 📂 backups/
> │      ├── 📄 index.html
> │    └── 📂 consume/
> │      ├── 📄 _B_EVIDENCE.md
> │      ├── 📄 court_record__20_court_record.md
> │      ├── 📄 court_record___20_court_record.md
> │      ├── 📄 court_record_docket_files__EXH__026_Exhibit_List_A-G.pdf
> │      ├── 📄 court_record_docket_files__MO__013_Motion_for_Default_Judgment.pdf
> │      ├── 📄 court_record_docket_files__MO__019_Amended_Motion_Default_Judgmen.pdf
> │      ├── 📄 court_record_docket_files__MO__020_Amended_Motion_Default_Judgmen.pdf
> │      ├── 📄 court_record_docket_files__MO__025_Motion_Vacate_Stay_Writ.pdf
> │      ├── 📄 court_record_docket_files__MO__027_Supplemental_Motion_Access.pdf
> │      ├── 📄 court_record_docket_files__OR__023_Decree_Foreclosure_Returned.pdf
> │      ├── 📄 court_record_docket_files__OR__031_Proposed_Order_Vacate.pdf
> │      ├── 📄 court_record_docket_files__OR__032_Proposed_Order_Stay.pdf
> │      ├── 📄 court_record_docket_files__PL_017_OMITTED NOTICE OF SERVICE TO DEFENDANT.pdf
> │      ├── 📄 court_record_docket_files__PL_029_Emergency_Supplemental_Declaration.pdf
> │      ├── 📄 court_record_docket_files__PL__001_Complaint.pdf
> │      ├── 📄 court_record_docket_files__PL__002_Appearance.pdf
> │      ├── 📄 court_record_docket_files__PL__003_Request_for_Admissions.pdf
> │      ├── 📄 court_record_docket_files__PL__004_Notice_to_Homeowners.pdf
> │      ├── 📄 court_record_docket_files__PL__005_Appearance_2.pdf
> │      ├── 📄 court_record_docket_files__PL__006_Summons_1.pdf
> │      ├── 📄 court_record_docket_files__PL__007_Summons_2.pdf
> │      ├── 📄 court_record_docket_files__PL__008_Summons_3.pdf
> │      ├── 📄 court_record_docket_files__PL__009_Summons_4.pdf
> │      ├── 📄 court_record_docket_files__PL__010_Summons_5.pdf
> │      ├── 📄 court_record_docket_files__PL__011_Service_Returned_03-05-2025.pdf
> │      ├── 📄 court_record_docket_files__PL__012_Service_Returned_04-15-2025.pdf
> │      ├── 📄 court_record_docket_files__PL__014_Affidavit.pdf
> │      ├── 📄 court_record_docket_files__PL__015_Affidavit_Attorney_Fees.pdf
> │      ├── 📄 court_record_docket_files__PL__016_Affidavit_Additional.pdf
> │      ├── 📄 court_record_docket_files__PL__018_Omitted_Notice_of_Service.pdf
> │      ├── 📄 court_record_docket_files__PL__021_Praecipe_Sheriff_Sale_1.pdf
> │      ├── 📄 court_record_docket_files__PL__022_Praecipe_Sheriff_Sale_2.pdf
> │      ├── 📄 court_record_docket_files__PL__024_Petition_Writ_of_Assistance.pdf
> │      ├── 📄 court_record_docket_files__PL__028_Report_Court_Defendant_Request.pdf
> │      ├── 📄 court_record_docket_files__PL__030_Report_Sheriff_Sale_No_Excess.pdf
> │      ├── 📄 court_record_docket_files__PL__033_ADA_Disability_Affidavit.pdf
> │      ├── 📄 court_record_docket_files___10_docket_files.md
> │      ├── 📄 evidence_admin__00_evidence_admin.md
> │      ├── 📄 evidence_admin__10_chain_of_custody.md
> │      ├── 📄 evidence_admin__20_Evidence_Log.md
> │      ├── 📄 evidence_admin__EXH_Raw_Exhibit_Map.md
> │      ├── 📄 evidence_admin___10_evidence_admin.md
> │      ├── 📄 index.html
> │      ├── 📄 primary___30_primary.md
> │      ├── 📄 primary_aes__PL_2025-06-08_aes_ada_notice.pdf
> │      ├── 📄 primary_aes__PL_2025-12-16_AES_Emergency_Notice.md
> │      ├── 📄 primary_aes___20_aes.md
> │      ├── 📄 primary_aes___README.md
> │      ├── 📄 primary_fcfcu__2023-09-20_FCFCU_Hardship_and_Healt.md
> │      ├── 📄 primary_fcfcu__20241204_FCFCU_Statement (1).pdf
> │      ├── 📄 primary_fcfcu__20241204_FCFCU_Statement (2).pdf
> │      ├── 📄 primary_fcfcu__20241204_fcfcu_statement-(1).pdf
> │      ├── 📄 primary_fcfcu__20241204_fcfcu_statement-(2).pdf
> │      ├── 📄 primary_fcfcu__20241204_fcfcu_statement.pdf
> │      ├── 📄 primary_fcfcu__PL_2023-09-20_FCFCU_Hardship_and_Health_Notice_Let.md
> │      ├── 📄 primary_fcfcu__PL_2023-09-20_notice_disabilities_hardship.pdf
> │      ├── 📄 primary_fcfcu__PL_2024-20-03_response_to_tax_notice.pdf
> │      ├── 📄 primary_fcfcu___10_fcfcu.md
> │      ├── 📄 primary_fcfcu___README.md
> │      ├── 📄 quarantine_candidates__50_quarantine_candidates.md
> │      ├── 📄 quarantine_candidates___50_quarantine_candidates.md
> │      ├── 📄 supporting__40_supporting.md
> │      ├── 📄 supporting___40_supporting.md
> │      ├── 📄 supporting_docs___docs.md
> │      ├── 📄 supporting_docs_affidavits__PL_affidavits.md
> │      ├── 📄 supporting_docs_affidavits___affidavits.md
> │      ├── 📄 supporting_docs_affidavits_ada-disability___ada-disability.md
> │      ├── 📄 supporting_docs_affidavits_character___character.md
> │      ├── 📄 supporting_docs_affidavits_community-service___community-service.md
> │      ├── 📄 supporting_docs_affidavits_credibility___credibility.md
> │      ├── 📄 supporting_docs_affidavits_observations___observations.md
> │      ├── 📄 supporting_docs_declarations__PL_declarations.md
> │      ├── 📄 supporting_docs_declarations___declarations.md
> │      ├── 📄 supporting_docs_receipts___receipts.md
> │      ├── 📄 supporting_docs_records___records.md
> │      ├── 📄 supporting_multi-media___multi-media.md
> │      ├── 📄 supporting_property___property.md
> │      ├── 📄 supporting_property_mortgage_history___10_mortgage_history.md
> │      ├── 📄 supporting_property_mortgage_history_payments__2025-12-20_EXH-20_payments_c5131deb_2025-12-20.png
> │      ├── 📄 supporting_property_mortgage_history_payments__20_payments.md
> │      ├── 📄 supporting_property_mortgage_history_payments___10_payments.md
> │      ├── 📄 supporting_property_parcel__Parcel_6016506_PRC.pdf
> │      ├── 📄 supporting_property_parcel__Parcel_6016506_ParcelDetailHistory.pdf
> │      ├── 📄 supporting_property_parcel___20_parcel.md
> │    └── 📂 data/
> │      ├── 📄 PG_VERSION
> │      └── 📂 base/
> │        └── 📂 1/
> │          ├── 📄 index.html
> │        ├── 📄 index.html
> │      ├── 📄 celerybeat-schedule.db
> │      └── 📂 global/
> │        ├── 📄 index.html
> │        ├── 📄 pg_control
> │      └── 📂 index/
> │      ├── 📄 index.html
> │        ├── 📄 MAIN_WRITELOCK
> │        ├── 📄 MAIN_df60pz781b1vkrg5.seg
> │        ├── 📄 _MAIN_110.toc
> │        ├── 📄 index.html
> │      └── 📂 log/
> │        ├── 📄 celery.log
> │        ├── 📄 celery.log.2
> │        ├── 📄 celery.log.rotate.13123699319956527895
> │        ├── 📄 celery.log.rotate.14527157462966423769
> │        ├── 📄 celery.log.rotate.16014095090721714709
> │        ├── 📄 celery.log.rotate.16551543857574243639
> │        ├── 📄 celery.log.rotate.4002149963526754070
> │        ├── 📄 celery.log.rotate.5851441854598125821
> │        ├── 📄 celery.log.rotate.9282371777522306113
> │        ├── 📄 index.html
> │        ├── 📄 paperless.log
> │        ├── 📄 paperless.log.rotate.1272259500908817030
> │        ├── 📄 paperless.log.rotate.2124330999174016128
> │      ├── 📄 migration_lock
> │      └── 📂 pg_commit_ts/
> │        ├── 📄 index.html
> │      └── 📂 pg_dynshmem/
> │        ├── 📄 index.html
> │      ├── 📄 pg_hba.conf
> │      ├── 📄 pg_ident.conf
> │      └── 📂 pg_logical/
> │        ├── 📄 index.html
> │        └── 📂 mappings/
> │          ├── 📄 index.html
> │        ├── 📄 replorigin_checkpoint
> │        └── 📂 snapshots/
> │          ├── 📄 index.html
> │      └── 📂 pg_multixact/
> │        ├── 📄 index.html
> │        └── 📂 members/
> │          ├── 📄 0000
> │          ├── 📄 index.html
> │        └── 📂 offsets/
> │          ├── 📄 0000
> │          ├── 📄 index.html
> │      └── 📂 pg_notify/
> │        ├── 📄 index.html
> │      └── 📂 pg_replslot/
> │        ├── 📄 index.html
> │      └── 📂 pg_serial/
> │        ├── 📄 index.html
> │      └── 📂 pg_snapshots/
> │        ├── 📄 index.html
> │      └── 📂 pg_stat/
> │        ├── 📄 index.html
> │        ├── 📄 pgstat.stat
> │      └── 📂 pg_stat_tmp/
> │        ├── 📄 index.html
> │      └── 📂 pg_subtrans/
> │        ├── 📄 0000
> │        ├── 📄 index.html
> │      └── 📂 pg_tblspc/
> │        ├── 📄 index.html
> │      └── 📂 pg_twophase/
> │        ├── 📄 index.html
> │      └── 📂 pg_wal/
> │        ├── 📄 000000010000000000000001
> │        └── 📂 archive_status/
> │          ├── 📄 index.html
> │        ├── 📄 index.html
> │      └── 📂 pg_xact/
> │        ├── 📄 0000
> │        ├── 📄 index.html
> │      ├── 📄 postgresql.auto.conf
> │      ├── 📄 postgresql.conf
> │      ├── 📄 postmaster.opts
> │    ├── 📄 docker-compose.yml
> │    └── 📂 export/
> │      ├── 📄 index.html
> │    ├── 📄 index.html
> │    └── 📂 media/
> │      └── 📂 documents/
> │        └── 📂 archive/
> │          ├── 📄 0000001.pdf
> │          ├── 📄 0000002.pdf
> │          ├── 📄 0000003.pdf
> │          ├── 📄 0000004.pdf
> │          ├── 📄 0000005.pdf
> │          ├── 📄 0000006.pdf
> │          ├── 📄 0000007.pdf
> │          ├── 📄 0000008.pdf
> │          ├── 📄 0000009.pdf
> │          ├── 📄 0000010.pdf
> │          ├── 📄 0000011.pdf
> │          ├── 📄 0000012.pdf
> │          ├── 📄 0000013.pdf
> │          ├── 📄 0000014.pdf
> │          ├── 📄 0000015.pdf
> │          ├── 📄 0000016.pdf
> │          ├── 📄 0000017.pdf
> │          ├── 📄 0000018.pdf
> │          ├── 📄 0000019.pdf
> │          ├── 📄 0000020.pdf
> │          ├── 📄 0000021.pdf
> │          ├── 📄 0000022.pdf
> │          ├── 📄 0000023.pdf
> │          ├── 📄 0000024.pdf
> │          ├── 📄 0000025.pdf
> │          ├── 📄 0000026.pdf
> │          ├── 📄 0000027.pdf
> │          ├── 📄 0000028.pdf
> │          ├── 📄 0000029.pdf
> │          ├── 📄 0000030.pdf
> │          ├── 📄 0000031.pdf
> │          ├── 📄 0000032.pdf
> │          ├── 📄 0000033.pdf
> │          ├── 📄 0000034.pdf
> │          ├── 📄 0000035.pdf
> │          ├── 📄 0000036.pdf
> │          ├── 📄 0000037.pdf
> │          ├── 📄 0000038.pdf
> │          ├── 📄 0000039.pdf
> │          ├── 📄 0000040.pdf
> │          ├── 📄 0000041.pdf
> │          ├── 📄 0000042.pdf
> │          ├── 📄 0000043.pdf
> │          ├── 📄 0000044.pdf
> │          ├── 📄 0000045.pdf
> │          ├── 📄 0000046.pdf
> │          ├── 📄 0000047.pdf
> │          ├── 📄 0000048.pdf
> │          ├── 📄 0000049.pdf
> │          ├── 📄 0000050.pdf
> │          ├── 📄 0000051.pdf
> │          ├── 📄 0000052.pdf
> │          ├── 📄 0000053.pdf
> │          ├── 📄 0000054.pdf
> │          ├── 📄 0000055.pdf
> │          ├── 📄 0000056.pdf
> │          ├── 📄 0000057.pdf
> │          ├── 📄 0000058.pdf
> │          ├── 📄 0000059.pdf
> │          ├── 📄 0000060.pdf
> │          ├── 📄 0000061.pdf
> │          ├── 📄 0000062.pdf
> │          ├── 📄 0000063.pdf
> │          ├── 📄 0000064.pdf
> │          ├── 📄 0000065.pdf
> │          ├── 📄 0000066.pdf
> │          ├── 📄 0000067.pdf
> │          ├── 📄 0000068.pdf
> │          ├── 📄 0000069.pdf
> │          ├── 📄 0000070.pdf
> │          ├── 📄 0000071.pdf
> │          ├── 📄 0000072.pdf
> │          ├── 📄 0000073.pdf
> │          ├── 📄 0000074.pdf
> │          ├── 📄 0000075.pdf
> │          ├── 📄 0000076.pdf
> │          ├── 📄 0000077.pdf
> │          ├── 📄 0000078.pdf
> │          ├── 📄 0000079.pdf
> │          ├── 📄 0000080.pdf
> │          ├── 📄 0000081.pdf
> │          ├── 📄 0000082.pdf
> │          ├── 📄 0000083.pdf
> │          ├── 📄 0000084.pdf
> │          ├── 📄 0000085.pdf
> │          ├── 📄 index.html
> │        ├── 📄 index.html
> │        └── 📂 originals/
> │          ├── 📄 0000001.pdf
> │          ├── 📄 0000002.pdf
> │          ├── 📄 0000003.pdf
> │          ├── 📄 0000004.pdf
> │          ├── 📄 0000005.pdf
> │          ├── 📄 0000006.pdf
> │          ├── 📄 0000007.pdf
> │          ├── 📄 0000008.pdf
> │          ├── 📄 0000009.pdf
> │          ├── 📄 0000010.pdf
> │          ├── 📄 0000011.pdf
> │          ├── 📄 0000012.pdf
> │          ├── 📄 0000013.pdf
> │          ├── 📄 0000014.pdf
> │          ├── 📄 0000015.pdf
> │          ├── 📄 0000016.pdf
> │          ├── 📄 0000017.pdf
> │          ├── 📄 0000018.pdf
> │          ├── 📄 0000019.pdf
> │          ├── 📄 0000020.pdf
> │          ├── 📄 0000021.pdf
> │          ├── 📄 0000022.pdf
> │          ├── 📄 0000023.pdf
> │          ├── 📄 0000024.pdf
> │          ├── 📄 0000025.pdf
> │          ├── 📄 0000026.pdf
> │          ├── 📄 0000027.pdf
> │          ├── 📄 0000028.pdf
> │          ├── 📄 0000029.pdf
> │          ├── 📄 0000030.pdf
> │          ├── 📄 0000031.pdf
> │          ├── 📄 0000032.pdf
> │          ├── 📄 0000033.pdf
> │          ├── 📄 0000034.pdf
> │          ├── 📄 0000035.pdf
> │          ├── 📄 0000036.pdf
> │          ├── 📄 0000037.pdf
> │          ├── 📄 0000038.pdf
> │          ├── 📄 0000039.pdf
> │          ├── 📄 0000040.pdf
> │          ├── 📄 0000041.pdf
> │          ├── 📄 0000042.pdf
> │          ├── 📄 0000043.jpg
> │          ├── 📄 0000044.jpg
> │          ├── 📄 0000045.pdf
> │          ├── 📄 0000046.pdf
> │          ├── 📄 0000047.pdf
> │          ├── 📄 0000048.pdf
> │          ├── 📄 0000049.jpg
> │          ├── 📄 0000050.pdf
> │          ├── 📄 0000051.jpg
> │          ├── 📄 0000052.jpg
> │          ├── 📄 0000053.png
> │          ├── 📄 0000054.jpg
> │          ├── 📄 0000055.jpg
> │          ├── 📄 0000056.jpg
> │          ├── 📄 0000057.jpg
> │          ├── 📄 0000058.jpg
> │          ├── 📄 0000059.jpg
> │          ├── 📄 0000060.jpg
> │          ├── 📄 0000061.jpg
> │          ├── 📄 0000062.jpg
> │          ├── 📄 0000063.jpg
> │          ├── 📄 0000064.jpg
> │          ├── 📄 0000065.jpg
> │          ├── 📄 0000066.jpg
> │          ├── 📄 0000067.jpg
> │          ├── 📄 0000068.jpg
> │          ├── 📄 0000069.jpg
> │          ├── 📄 0000070.png
> │          ├── 📄 0000071.jpg
> │          ├── 📄 0000072.jpg
> │          ├── 📄 0000073.jpg
> │          ├── 📄 0000074.jpg
> │          ├── 📄 0000075.jpg
> │          ├── 📄 0000076.jpg
> │          ├── 📄 0000077.jpg
> │          ├── 📄 0000078.jpg
> │          ├── 📄 0000079.jpg
> │          ├── 📄 0000080.jpg
> │          ├── 📄 0000081.jpg
> │          ├── 📄 0000082.jpg
> │          ├── 📄 0000083.png
> │          ├── 📄 0000084.pdf
> │          ├── 📄 0000085.pdf
> │          ├── 📄 index.html
> │        └── 📂 thumbnails/
> │          ├── 📄 0000001.webp
> │          ├── 📄 0000002.webp
> │          ├── 📄 0000003.webp
> │          ├── 📄 0000004.webp
> │          ├── 📄 0000005.webp
> │          ├── 📄 0000006.webp
> │          ├── 📄 0000007.webp
> │          ├── 📄 0000008.webp
> │          ├── 📄 0000009.webp
> │          ├── 📄 0000010.webp
> │          ├── 📄 0000011.webp
> │          ├── 📄 0000012.webp
> │          ├── 📄 0000013.webp
> │          ├── 📄 0000014.webp
> │          ├── 📄 0000015.webp
> │          ├── 📄 0000016.webp
> │          ├── 📄 0000017.webp
> │          ├── 📄 0000018.webp
> │          ├── 📄 0000019.webp
> │          ├── 📄 0000020.webp
> │          ├── 📄 0000021.webp
> │          ├── 📄 0000022.webp
> │          ├── 📄 0000023.webp
> │          ├── 📄 0000024.webp
> │          ├── 📄 0000025.webp
> │          ├── 📄 0000026.webp
> │          ├── 📄 0000027.webp
> │          ├── 📄 0000028.webp
> │          ├── 📄 0000029.webp
> │          ├── 📄 0000030.webp
> │          ├── 📄 0000031.webp
> │          ├── 📄 0000032.webp
> │          ├── 📄 0000033.webp
> │          ├── 📄 0000034.webp
> │          ├── 📄 0000035.webp
> │          ├── 📄 0000036.webp
> │          ├── 📄 0000037.webp
> │          ├── 📄 0000038.webp
> │          ├── 📄 0000039.webp
> │          ├── 📄 0000040.webp
> │          ├── 📄 0000041.webp
> │          ├── 📄 0000042.webp
> │          ├── 📄 0000043.webp
> │          ├── 📄 0000044.webp
> │          ├── 📄 0000045.webp
> │          ├── 📄 0000046.webp
> │          ├── 📄 0000047.webp
> │          ├── 📄 0000048.webp
> │          ├── 📄 0000049.webp
> │          ├── 📄 0000050.webp
> │          ├── 📄 0000051.webp
> │          ├── 📄 0000052.webp
> │          ├── 📄 0000053.webp
> │          ├── 📄 0000054.webp
> │          ├── 📄 0000055.webp
> │          ├── 📄 0000056.webp
> │          ├── 📄 0000057.webp
> │          ├── 📄 0000058.webp
> │          ├── 📄 0000059.webp
> │          ├── 📄 0000060.webp
> │          ├── 📄 0000061.webp
> │          ├── 📄 0000062.webp
> │          ├── 📄 0000063.webp
> │          ├── 📄 0000064.webp
> │          ├── 📄 0000065.webp
> │          ├── 📄 0000066.webp
> │          ├── 📄 0000067.webp
> │          ├── 📄 0000068.webp
> │          ├── 📄 0000069.webp
> │          ├── 📄 0000070.webp
> │          ├── 📄 0000071.webp
> │          ├── 📄 0000072.webp
> │          ├── 📄 0000073.webp
> │          ├── 📄 0000074.webp
> │          ├── 📄 0000075.webp
> │          ├── 📄 0000076.webp
> │          ├── 📄 0000077.webp
> │          ├── 📄 0000078.webp
> │          ├── 📄 0000079.webp
> │          ├── 📄 0000080.webp
> │          ├── 📄 0000081.webp
> │          ├── 📄 0000082.webp
> │          ├── 📄 0000083.webp
> │          ├── 📄 0000084.webp
> │          ├── 📄 0000085.webp
> │          ├── 📄 index.html
> │      ├── 📄 index.html
> │      ├── 📄 media.lock
> └── 📂 content/
> │  └── 📂 00_CASE_MASTER/
> │    ├── 📄 FCFCU_CASE_MASTER - 0_master.csv
> │    ├── 📄 Strategic_Plan.canvas
> │    ├── 📄 _Case_Summary.md
> │  └── 📂 01_PHASES/
> │    ├── 📄 1_phases-v2.csv
> │    ├── 📄 1_phases.csv
> │    └── 📂 C-00_Foreclosure_Record/
> │      └── 📂 00.01_Record_Integrity/
> │        ├── 📄 Filing timestamp audit (service vs default timing).md
> │        ├── 📄 Filing timestamp audit.md
> │        ├── 📄 Master docket verification (all entries accounted for).md
> │        ├── 📄 Master docket verification.md
> │        ├── 📄 Order sequence alignment (complaint → default → sale → writ).md
> │        ├── 📄 Order sequence alignment.md
> │      └── 📂 00.02_Jurisdictional_Defects/
> │        ├── 📄 Service deficiency analysis.md
> │        ├── 📄 Service_Deficiency_Analysis.md
> │      └── 📂 00.03_Appellate_Preservation/
> │        ├── 📄 Appellate issue preservation memo.md
> │        ├── 📄 Appellate_Issue_Preservation.md
> │      ├── 📄 _PHASE_OVERVIEW.md
> │    └── 📂 C-01_Service_Notice_Defects/
> │      └── 📂 01.01_Service_Compliance_Audit/
> │        ├── 📄 Secondary mailing failure analysis.md
> │        ├── 📄 Sheriff return review.md
> │      └── 📂 01.02_Notice_Failures/
> │        ├── 📄 48-hour notice absence documentation.md
> │        ├── 📄 Publication proof gap.md
> │      └── 📂 01.03_Legal_Impact_Assessment/
> │      ├── 📄 _PHASE_OVERVIEW.md
> │    └── 📂 C-02_Evidence_Preservation/
> │      └── 📂 02.01_Litigation_Hold_Control/
> │        ├── 📄 Dispatch preservation notices.md
> │      └── 📂 02.02_Spoliation_Risk_Register/
> │        ├── 📄 20_Spoliation_Risk_Ledger.md
> │      └── 📂 02.03_Evidence_Intake_Log/
> │      ├── 📄 _PHASE_OVERVIEW.md
> │    └── 📂 C-03_Financial_Misconduct/
> │      └── 📂 03.01_Surplus_Forensics/
> │        ├── 📄 1️⃣ SURPLUS ACCOUNTING DEMAND LETTER.md
> │        └── 📂 C-05_Accounting_Surplus/
> │          ├── 📄 NT_Attorney_Intake_Summary.md
> │          ├── 📄 _25_IN_DFI.md
> │          ├── 📄 _50_HUD_FHEO.md
> │          ├── 📄 _PHASE_OVERVIEW.md
> │        ├── 📄 Surplus reconciliation table.md
> │      └── 📂 03.02_Fee_Inflation_Audit/
> │        ├── 📄 FCFCU_Audit_Forensic_Discrepancies.canvas
> │      └── 📂 03.03_FCRA_Exposure_Link/
> │        ├── 📄 2️⃣ FCRA STATUTORY DAMAGES MODEL.md
> │        ├── 📄 30_Full_TriMerge_2025_12_tradelines.csv
> │        ├── 📄 Core_Credit_Tables.md
> │        ├── 📄 _20_furnisher_disputes.md
> │        ├── 📄 _CREDIT_FCRA_MASTER.md
> │      └── 📂 03.04_Regulatory_Pressure/
> │        ├── 📄 3️⃣ REGULATOR-READY COMPLAINT PACKET.md
> │        └── 📂 CFPB/
> │          ├── 📄 01_Combined_Narrative_and_Excerpt.md
> │          ├── 📄 CFPB_Complaint_Draft.md
> │          ├── 📄 CFPB_Violation_Excerpt_Master.md
> │          ├── 📄 Cover_Letter.md
> │          ├── 📄 _CFPB.md
> │        └── 📂 CRAs/
> │          └── 📂 Equifax/
> │            ├── 📄 Equifax_Violation_Excerpt.md
> │            ├── 📄 _Equifax.md
> │          └── 📂 Experian/
> │            ├── 📄 Experian_Access_your_credit_report_2_tradelines.csv
> │            ├── 📄 Experian_Access_your_credit_report_CH13_tradelines.csv
> │            ├── 📄 Experian_Violation_Excerpt.md
> │            ├── 📄 _Experian.md
> │          └── 📂 Transunion/
> │            ├── 📄 TransUnion_Violation_Excerpt.md
> │            ├── 📄 _Transunion.md
> │          ├── 📄 _CRAs.md
> │        ├── 📄 City_of_Indy_Violation_Excerpt.md
> │        ├── 📄 Execution_Checklist.md
> │        ├── 📄 FORMAL NOTICE OF CONTINUING FCRA VIOLATIONS.md
> │        └── 📂 NCUA/
> │        ├── 📄 NCUA CONSUMER COMPLAINT – DRAFT.md
> │          ├── 📄 01_Combined_Narrative_and_Excerpt_2.md
> │          ├── 📄 Cover_Letter_6.md
> │          ├── 📄 Exhibit_Manifest_1.md
> │          ├── 📄 MANIFEST_NCUA_Complaint_Packet.md
> │          ├── 📄 _NCUA.md
> │        ├── 📄 NOTICE OF FAILURE TO REFLECT DISPUTED STATUS.md
> │        ├── 📄 PHASE_CREDIT_EXECUTION_MAP.md
> │        ├── 📄 Sanctions_Readiness_Memo.md
> │        ├── 📄 _20_CFPB.md
> │        ├── 📄 _30_NCUA.md
> │        ├── 📄 _30_bureau_disputes.md
> │        ├── 📄 _30_demand_letters.md
> │        ├── 📄 _BBB.md
> │      ├── 📄 _PHASE_OVERVIEW.md
> │    └── 📂 C-04_Writ_Removal_Conduct/
> │      └── 📂 04.01_Writ_Execution_Validity/
> │        ├── 📄 Writ predicate checklist.md
> │      └── 📂 04.02_Property_Interference/
> │        ├── 📄 Property interference log.md
> │      └── 📂 04.03_State_Action_Analysis/
> │        ├── 📄 1983 element mapping.md
> │        ├── 📄 MANIFEST_Sheriff_Oversight_Packet.md
> │        ├── 📄 Marion_County_Sheriff_Oversight_Violation_Excerpt.md
> │        ├── 📄 Sheriff_Internal_Affairs_Complaint.md
> │        ├── 📄 Sheriff_Violation_Excerpt.md
> │      └── 📂 04.04_Post_Removal_Damages/
> │      ├── 📄 _20_AG_Indiana.md
> │      ├── 📄 _20_Habitability.md
> │      ├── 📄 _35_Sheriff_Oversight.md
> │      ├── 📄 _45_FCC_Telecom.md
> │      ├── 📄 _PHASE_OVERVIEW.md
> │    └── 📂 C-05_Civil_Rights/
> │      └── 📂 05.01_ADA_Accommodation_Record/
> │        ├── 📄 99_Legacy_Excerpt_3.md
> │        ├── 📄 Accommodation request log.md
> │        ├── 📄 _C06_ADA.md
> │      └── 📂 05.02_Access_to_Court_Impact/
> │        ├── 📄 DOJ_Civil_Rights_Violation_Excerpt.md
> │      └── 📂 05.03_Discriminatory_Impact_Assessment/
> │        ├── 📄 Cover_Letter_1.md
> │        ├── 📄 Cover_Letter_3.md
> │        ├── 📄 Cover_Letter_4.md
> │        ├── 📄 Cover_Letter_5.md
> │        ├── 📄 Cover_Letter_7.md
> │        ├── 📄 Cover_Letter_DOJ_Supplemental.md
> │        ├── 📄 DOJ_Civil_Rights_Violation_Excerpt.md
> │        ├── 📄 DOJ_Civil_Rights_Violation_Excerpt_Master.md
> │        ├── 📄 DOJ_Supplemental_Continuing_Harm.md
> │        ├── 📄 Exhibit_Manifest.md
> │        ├── 📄 HUD_FHEO_Complaint_Narrative.md
> │        ├── 📄 HUD_FHEO_Violation_Excerpt.md
> │        ├── 📄 IN_AG_Violation_Excerpt.md
> │        ├── 📄 IN_DFI_Violation_Excerpt.md
> │        ├── 📄 Indiana_AG_Complaint_Narrative.md
> │        ├── 📄 Indiana_Civil_Rights_Commission_Violation_Excerpt.md
> │        ├── 📄 Indiana_Civil_Rights_Complaint_Narrative.md
> │        ├── 📄 Indiana_DFI_Complaint_Narrative.md
> │        ├── 📄 Indiana_Department_of_Financial_Institutions_DFI_Violation_Excerpt.md
> │        ├── 📄 MANIFEST_HUD_FHEO_Complaint_Packet.md
> │        ├── 📄 MANIFEST_ICRC_Complaint_Packet.md
> │        ├── 📄 MANIFEST_IN_AG_Complaint_Packet.md
> │        ├── 📄 MANIFEST_Indiana_DFI_Packet.md
> │        ├── 📄 Violation_to_Regulator_Mapping.md
> │      ├── 📄 _40_DOJ_Civil_Rights.md
> │      ├── 📄 _55_IN_Civil_Rights.md
> │      ├── 📄 _PHASE_OVERVIEW.md
> │    └── 📂 C-06_Settlement_Narrative_Control/
> │      └── 📂 06.01_Settlement_Framework/
> │        ├── 📄 Settlement demand model.md
> │      └── 📂 06.02_Negotiation_Tracking/
> │      └── 📂 06.03_Narrative_Discipline/
> │        ├── 📄 01_Combined_Narrative_and_Excerpt_1.md
> │        ├── 📄 20251215_displacement_cold_exposure.md
> │        ├── 📄 BBB_Violation_Excerpt.md
> │        ├── 📄 _C10_Narrative_Control.md
> │      ├── 📄 _PHASE_OVERVIEW.md
> │    ├── 📄 Phase Kanban.md
> │    ├── 📄 _PHASES_MASTER.md
> │    ├── 📄 _STRUCTURE_LOCK.md
> │  └── 📂 02_VIOLATIONS/
> │    ├── 📄 03_CASE_VIOLATIONS.md
> │    ├── 📄 FCFCU_CASE_MASTER - 2_violations.csv
> │    ├── 📄 FCFCU_CASE_MASTER - 2_violations.csv.md
> │    └── 📂 violations/
> │      ├── 📄 _violations.md
> │      ├── 📄 violations_UPDATED.csv
> │  └── 📂 03_EVENTS/
> │    ├── 📄 02_TIMELINE.mw
> │    └── 📂 2021/
> │      ├── 📄 2021-06-24_FCFCU_Signed_First_Mortgage_Note.md
> │    └── 📂 2022/
> │      ├── 📄 2022-06-28_FCFCU_Signed_Second_Mortgage_Note.md
> │    └── 📂 2023/
> │      ├── 📄 2023-09-20_FCFCU_Hardship_and_Health_Notice_Let.md
> │      ├── 📄 2023-09-20_FCFCU_Hardship_and_Health_Notice_Letter.md
> │      ├── 📄 2023-09-21_FCFCU_Letter_Pre_Shipment.md
> │      ├── 📄 2023-09-25_FCFCU_Letter_Delivered.md
> │    └── 📂 2024/
> │      ├── 📄 2024-03-20_FCFCU_Certified_Response_Tax_Records.md
> │      ├── 📄 2024-06-21_FCFCU_Property_Appraisal.md
> │      ├── 📄 2024-07-12_FCFCU_Mortgage_Payment_Record.md
> │      ├── 📄 2024-09-13_FCFCU_Plaintiff_Claims_Default_Letter_Sent.md
> │      ├── 📄 2024-11-19_FCFCU_Plaintiff_Claims_Amount_Due.md
> │      ├── 📄 2024-12-04_FCFCU_Notice_of_Default_Right_to_Cure_Sent.md
> │      ├── 📄 2024-12-04_FCFCU_Statement.md
> │      ├── 📄 2024-12-09_Eviction_Case_MasterFile.md
> │      ├── 📄 2024-12-09_FCFCU_Outgoing_Email_Bank_Access_Reques.md
> │      ├── 📄 2024-12-11_FCFCU_Outgoing_Email_Bank_Access_Reques.md
> │    └── 📂 2025/
> │      ├── 📄 2025-01-04_DEADLINE_Cure_Period_Expires.md
> │      ├── 📄 2025-01-09_COURT_Orders_And_Hearing_Scheduled.md
> │      ├── 📄 2025-01-09_COURT_Orders_Hearing_Scheduled.md
> │      ├── 📄 2025-01-14_FCFCU_Plaintiff_Conducts_SCRA_Searches.md
> │      ├── 📄 2025-01-15_COUNSEL_Felix_Rippy_Files_Appearance.md
> │      ├── 📄 2025-01-15_FCFCU_Notice_of_Default_Sent.md
> │      ├── 📄 2025-01-16_COURT_Summons_Issued.md
> │      ├── 📄 2025-01-16_Case_Filed.md
> │      ├── 📄 2025-01-16_FCFCU_Case_Filed.md
> │      ├── 📄 2025-01-16_FCFCU_Complaint_Filed.md
> │      ├── 📄 2025-01-16_SHERIFF_SERVICE_Simultaneous_Delivery_Claim.md
> │      ├── 📄 2025-03-05_SHERIFF_SERVICE_Return_Claimed.md
> │      ├── 📄 2025-03-05_Service_Attempt_1.md
> │      ├── 📄 2025-04-09_SERVICE_Attempt_2.md
> │      ├── 📄 2025-04-09_SHERIFF_SERVICE_Attempt_Two.md
> │      ├── 📄 2025-04-15_SHERIFF_Service_Return_Claimed.md
> │      ├── 📄 2025-04-15_Service_Attempt_2.md
> │      ├── 📄 2025-04-29_FCFCU_VP_Affidavit_Debt_Signed.md
> │      ├── 📄 2025-05-01_CRA_CREDIT_EVENT_FCFCU_BALANCE_CHANGED.md
> │      ├── 📄 2025-05-07_FCFCU_Flowers_Affidavit_Notarized.md
> │      ├── 📄 2025-05-13_ATTORNEY_Files_Fee_Affidavit.md
> │      ├── 📄 2025-05-13_COURT_Motion_Default_Judgment.md
> │      ├── 📄 2025-05-13_COURT_Motion_For_Default_Judgment.md
> │      ├── 📄 2025-05-13_Motion_for_Default_Judgment.md
> │      ├── 📄 2025-05-21_COURT_Order_Denying_Default.md
> │      ├── 📄 2025-05-21_COURT_Order_Denying_Default_Judgment.md
> │      ├── 📄 2025-05-21_FCFCU_Plaintiff_Files_for_Default_Judgment.md
> │      ├── 📄 2025-05-21_ORDER_Denying_Default.md
> │      ├── 📄 2025-05-21_Order_Denying_Default_Judgment.md
> │      ├── 📄 2025-05-23_Amended_Motion_Default_Judgment.md
> │      ├── 📄 2025-05-23_COURT_Default_Judgment_Entered.md
> │      ├── 📄 2025-05-23_COURT_document_Default_Judgment_Entered.md
> │      ├── 📄 2025-05-23_FCFCU_Amended_Default_Judgment_Requested.md
> │      ├── 📄 2025-05-23_FCFCU_Amended_Motion_Default_Judgment.md
> │      ├── 📄 2025-05-28_COURT_Default_Judgment_Entered.md
> │      ├── 📄 2025-05-28_COURT_Judgment_Entered.md
> │      ├── 📄 2025-05-28_Default_Judgment_Entered.md
> │      ├── 📄 2025-05-28_FCFCU_May28_FORECLOSURE.md
> │      ├── 📄 2025-05-29_Praecipe_Sheriff_Sale_Filed.md
> │      ├── 📄 2025-05-29_SHERIFF_Praecipe_Sale.md
> │      ├── 📄 2025-05-29_SHERIFF_Praecipe_Sale_02.md
> │      ├── 📄 2025-05-30_AES_ADA_Notice.md
> │      ├── 📄 2025-05-30_AES_Ada_Notice_02.md
> │      ├── 📄 2025-05-30_Praecipe_Sheriff_Sale.md
> │      ├── 📄 2025-05-30_SHERIFF_Praecipe_Sale.md
> │      ├── 📄 2025-06-01_CRA_REPORTING_EVENT_FCFCU_DUPLICATE_TRADELINE.md
> │      ├── 📄 2025-06-01_CRA_REPORTING_EVENT_FCFCU_STATUS_CHANGED.md
> │      ├── 📄 2025-06-01_CRA_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │      ├── 📄 2025-06-01_CRA_REPORTING_VIOLATION_EVENT_FCFCU_INITIAL_FALSE_REPORTING.md
> │      ├── 📄 2025-06-08_AES_ADA_Notice.md
> │      ├── 📄 2025-06-13_Sheriff_Sale_Notice.md
> │      ├── 📄 2025-06-13_Sheriff_Sale_Notice_Posted.md
> │      ├── 📄 2025-07-01_CRA_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │      ├── 📄 2025-07-06_FCFCU_Plaintiff_Claims_Notice_of_Sale.md
> │      ├── 📄 2025-07-09_Sheriff_Sale_Notice_Claimed.md
> │      ├── 📄 2025-07-09_Sheriff_Sale_Notice_Posted.md
> │      ├── 📄 2025-07-17_FCFCU_Plaintiff_Places_Bid.md
> │      ├── 📄 2025-08-01_CRA_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │      ├── 📄 2025-08-05_FCFCU_Report_Sheriff_Sale_No_Excess.md
> │      ├── 📄 2025-08-05_Sheriff_Sale_No_Excess.md
> │      ├── 📄 2025-08-15_FCFCU_BILLING_Utility_Bill_AES_during_dispute.md
> │      ├── 📄 2025-08-15_Sheriff_Sale.md
> │      ├── 📄 2025-08-15_Sheriff_Sale_Occurs.md
> │      ├── 📄 2025-08-15_Writ_Assistance_Issued.md
> │      ├── 📄 2025-08-15_Writ_Of_Assistance_Issued.md
> │      ├── 📄 2025-08-19_Sheriff_Deed_Signed.md
> │      ├── 📄 2025-09-01_EVENT_CREDIT_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │      ├── 📄 2025-09-09_Decree_Foreclosure_Returned.md
> │      ├── 📄 2025-09-09_Judgment_Satisfied_Return_Filed.md
> │      ├── 📄 2025-10-01_EVENT_CREDIT_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │      ├── 📄 2025-10-29_Petition_For_Writ_Of_Assistance_log_ext_1.md
> │      ├── 📄 2025-10-29_Petition_Writ_Assistance.md
> │      ├── 📄 2025-10-29_Petition_for_Writ_of_Assistance.md
> │      ├── 📄 2025-10-29_enforcement_Petition_For_Writ_Of_Assist.md
> │      ├── 📄 2025-11-01_EVENT_CREDIT_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │      ├── 📄 2025-11-06_Writ_of_Assistance_Granted.md
> │      ├── 📄 2025-11-06_Writ_of_Assistance_Issued.md
> │      ├── 📄 2025-11-26_Sheriff_Deputies_Arrive_Unrelated.md
> │      ├── 📄 2025-12-01_December_ADA_.md
> │      ├── 📄 2025-12-01_December_CONVERSION___NEGLIGENCE_.md
> │      ├── 📄 2025-12-01_December_CONVERSION___PROPERTY_INTERFERENCE_.md
> │      ├── 📄 2025-12-01_December_EVIDENCE_SPOLIATION_.md
> │      ├── 📄 2025-12-01_December_PROCEDURAL_.md
> │      ├── 📄 2025-12-01_December_SPOLIATION_OF_EVIDENCE_.md
> │      ├── 📄 2025-12-01_EVENT_CREDIT_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │      ├── 📄 2025-12-03_IMPD_Contact_Knocked_Then_Left.md
> │      ├── 📄 2025-12-07_Retrieval_Day.md
> │      ├── 📄 2025-12-09_0948_Sheriff_Arrival_Initial_Entry.md
> │      ├── 📄 2025-12-09_1000_Active_Removal_Process.md
> │      ├── 📄 2025-12-09_1016_Medical_Distress_Incident.md
> │      ├── 📄 2025-12-09_1018_Officer_Interference_Property_Retr.md
> │      ├── 📄 2025-12-09_1020_Room_Vacated.md
> │      ├── 📄 2025-12-09_1209_Hallway_Activity.md
> │      ├── 📄 2025-12-09_DISPLACEMENT_Emergency_Housing_Roaches_.md
> │      ├── 📄 2025-12-09_ENFORCEMENT_Armed_removal_from_property.md
> │      ├── 📄 2025-12-09_ENFORCEMENT_Writ_Executed__Forced_Removal.md
> │      ├── 📄 2025-12-09_Removal_Day_Camera_Garage.md
> │      ├── 📄 2025-12-09_Writ_Executed_Forced_Removal.md
> │      ├── 📄 2025-12-09_Writ_Executed_Removal.md
> │      ├── 📄 2025-12-09_Writ_Executed_Removal_migrated_1.md
> │      ├── 📄 2025-12-09_case_log.md
> │      ├── 📄 2025-12-10_EXPENSE_Essential_items_purchase.md
> │      ├── 📄 2025-12-10_Financial_Tracker.md
> │      ├── 📄 2025-12-10_Financial_Tracker_Update.md
> │      ├── 📄 2025-12-10_Motions_Filed.md
> │      ├── 📄 2025-12-10_PROCEDURAL_.md
> │      ├── 📄 2025-12-10_document_Financial_Tracker.md
> │      ├── 📄 2025-12-11_Court_Orders_and_Hearing_Scheduled.md
> │      ├── 📄 2025-12-12_028_Report_Court_Defendant_Request.md
> │      ├── 📄 2025-12-12_Attorney_Certifies_Document_Sent.md
> │      ├── 📄 2025-12-12_Report_Defendant_Request.md
> │      ├── 📄 2025-12-12_Supplemental_Emergency_Motion.md
> │      ├── 📄 2025-12-12_document_028_Report_Court_Defendant_Req.md
> │      ├── 📄 2025-12-15_Case_DNA_Strategy_Checkpoint.md
> │      ├── 📄 2025-12-15_Case_DNA_Strategy_Checkpoint_log_ext_1.md
> │      ├── 📄 2025-12-15_Case_DNA_Strategy_Checkpoint_log_ext_2.md
> │      ├── 📄 2025-12-15_LOG_Consolidated_Forensic_Case_Log.md
> │      ├── 📄 2025-12-15_Strategic_Planning_Session.md
> │      ├── 📄 2025-12-15_TRAUMA_Sexual_coercion_incident.md
> │      ├── 📄 2025-12-15_displacement_cold_exposure.md
> │      ├── 📄 2025-12-16_027_Supplemental_Motion_Access.md
> │      ├── 📄 2025-12-16_AES_Emergency_Notice.md
> │      ├── 📄 2025-12-16_ENFORCEMENT_Access_Denial_by_Susan_Abbett.md
> │      ├── 📄 2025-12-16_ENFORCEMENT_Post_Removal_Access_Denial.md
> │      ├── 📄 2025-12-16_Filing_Execution_Audit.md
> │      ├── 📄 2025-12-16_Motion_Surplus_Funds.md
> │      ├── 📄 2025-12-16_Procedural_Action_Filing_Execution_Documentation_Audit.md
> │      ├── 📄 2025-12-16_Supplemental_Motion_Access.md
> │      ├── 📄 2025-12-16_case_dna.md
> │      ├── 📄 2025-12-16_case_log.md
> │      ├── 📄 2025-12-16_motion_027_Supplemental_Motion_Access.md
> │      ├── 📄 2025-12-17_AES_Emergency_Notice.md
> │      ├── 📄 2025-12-17_Notice_Surplus_Funds_Hearing.md
> │      ├── 📄 2025-12-17_Report_No_Excess_Proceeds.md
> │      ├── 📄 2025-12-17_document_Aes_Emergency_Notice.md
> │      ├── 📄 2025-12-18_Automated_Notices_Issued.md
> │      ├── 📄 2025-12-19_gigi_acute_anxiety_attack.md
> │      ├── 📄 2025-12-21_ADA_Accommodation_Coordination.md
> │      ├── 📄 2025-12-21_Afternoon_Evening_-_Post-Removal_Harms_Documentation.md
> │      ├── 📄 2025-12-21_Camera_Unplugging_Discovery.md
> │      ├── 📄 2025-12-21_Case_Consolidation.md
> │      ├── 📄 2025-12-21_Case_Log.md
> │      ├── 📄 2025-12-21_DISCOVERY_Discovery_of_Camera_and_Fridge_Disconnection.md
> │      ├── 📄 2025-12-21_DISCOVERY_Property_Damage_Discovery.md
> │      ├── 📄 2025-12-21_DISTRESS_Physical_and_Financial_Distress_during_Retrieval.md
> │      ├── 📄 2025-12-21_DOJ_Civil_Rights_Complaint_Submitted.md
> │      ├── 📄 2025-12-21_DOJ_Complaint_Submitted.md
> │      ├── 📄 2025-12-21_Early_Morning_-_Gigi_Escape_Incident.md
> │      ├── 📄 2025-12-21_Evening_-_Procedural_Coordination_ADA_Accommodation.md
> │      ├── 📄 2025-12-21_Evening_-_Surveillance_Cameras_Guidance.md
> │      ├── 📄 2025-12-21_Gigi_Escape_Incident.md
> │      ├── 📄 2025-12-21_HOTEL_Hotel_Crisis_Deposit_Hold_Refusal.md
> │      ├── 📄 2025-12-21_INCIDENT_Gigi_Service_Animal_Escape_Crisis.md
> │      ├── 📄 2025-12-21_INCIDENT_Service_Animal_Escape.md
> │      ├── 📄 2025-12-21_Morning_-_CameraRefrigerator_Unplugging_Discovery.md
> │      ├── 📄 2025-12-21_Morning_-_Physical_Exhaustion_During_Access_Window.md
> │      ├── 📄 2025-12-21_PROTOCOL_Property_Retrieval_Surveillance_Guidance.md
> │      ├── 📄 2025-12-21_Physical_Exhaustion_Access.md
> │      ├── 📄 2025-12-21_Post_Removal_Harms_Documentation.md
> │      ├── 📄 2025-12-21_Surveillance_Cameras_Guidance.md
> │      ├── 📄 2025-12-21_document_Case_Log.md
> │      ├── 📄 2025-12-22_Court_Filing_History_Confirmed_and_Cross-Referenced.md
> │      ├── 📄 2025-12-22_Court_Filing_History_Cross_Reference.md
> │      ├── 📄 2025-12-22_Current_State_Snapshot.md
> │      ├── 📄 2025-12-22_Declaration_Filed_Envelope_37416037.md
> │      ├── 📄 2025-12-22_FINAL_STATUS_REPORT.md
> │      ├── 📄 2025-12-22_Supplemental_Snapshot_Displacement_Relo.md
> │      ├── 📄 2025-12-22_Today_Snapshot_Current_State.md
> │      ├── 📄 2025-12-22_Vault_State_Sync.md
> │      ├── 📄 2025-12-22_Vault_State_Sync_Documentation_Consolidation.md
> │      ├── 📄 20250521_ORDER_Denying_Default_Judgment.md
> │      ├── 📄 20250815_Sheriff_Sale.md
> │      ├── 📄 20251029_Petition_for_Writ_of_Assistance.md
> │      ├── 📄 20251106_Writ_of_Assistance_Issued.md
> │      ├── 📄 20251209_Writ_Executed_Removal.md
> │      ├── 📄 20251210_Motions_Filed.md
> │      ├── 📄 20251211_Court_Orders_and_Hearing_Scheduled.md
> │      ├── 📄 20251212_Supplemental_Emergency_Motion.md
> │    └── 📂 2026/
> │      ├── 📄 2026-01-01_EVENT_CREDIT_REPORTING_EVENT_FCFCU_WILLFUL_FALSE_REPORTING.md
> │      ├── 📄 2026-01-02_GENERAL_.md
> │      ├── 📄 2026-01-09_Felix_Rippy_Files_Late_Appearance.md
> │      ├── 📄 2026-01-09_Supplemental_Emergency_Motion.md
> │      ├── 📄 2026-01-09_motion_Supplemental_Emergency_Motion.md
> │      ├── 📄 2026-01-18_COLLATERAL_DAMAGE_Zai_Asylum_Impact.md
> │      ├── 📄 2026-01-18_DISPUTE_EasyTax_Crystal_Rodriguez_Dispute.md
> │      ├── 📄 2026-01-18_FINANCIAL_LOSS_Lost_Tax_Season_Income.md
> │      ├── 📄 2026-01-18_HOUSING_Otis_Emergency_Housing_Collapse.md
> │      ├── 📄 2026-01-18_RELOCATION_Forced_Relocation_to_Evansville.md
> │      ├── 📄 2026-01-18_RELOCATION_Relocation_to_Evansville.md
> │      ├── 📄 2026-01-18_STRATEGY_Strategic_Context_Clarification_Session.md
> │      ├── 📄 2026-01-27_FILING_CFPB_Complaint_Filing.md
> │      ├── 📄 2026-01-27_FILING_Regulator_Filings_HUD_NCUA_DOJ_.md
> │      ├── 📄 2026-02-01_EVENT_CREDIT_REPORTING_EVENT_FCFCU_BALANCE_CHANGED.md
> │      ├── 📄 2026-02-01_EVENT_CREDIT_REPORTING_EVENT_FCFCU_DUPLICATE_TRADELINE.md
> │      ├── 📄 2026-02-01_EVENT_CREDIT_REPORTING_EVENT_FCFCU_STATUS_CHANGED.md
> │      ├── 📄 2026-02-01_cold_exposure.md
> │      ├── 📄 2026-02-03_COMMUNICATION_Credit_Dispute_Package_Sent.md
> │      ├── 📄 2026-02-03_COMMUNICATION_Evidence_Preservation_Packet_Sent.md
> │      ├── 📄 2026-02-04_EVENT_CREDIT_REPORTING_EVENT_FCFCU_FALSE_REPORTING_AFTER_NOTICE.md
> │      ├── 📄 2026-02-09_EVENT_CREDIT_REPORTING_EVENT_FCFCU_FALSE_REPORTING_AFTER_NOTICE.md
> │      ├── 📄 2026-02-12_Session_Summary_2026-02-12_Tax_FCRA_Strategy_Update.md
> │      ├── 📄 20260209_Case_Log_Entry
> │    ├── 📄 FCFCU_CASE_MASTER - 3_events.csv
> │    ├── 📄 FCFCU_CASE_MASTER - 3_events.csv.md
> │    ├── 📄 index.md
> │  └── 📂 04_DOCUMENTS/
> │    └── 📂 00_drafts/
> │      ├── 📄 20260202_CAPTURE_Auto_Save_D0516.html
> │      ├── 📄 _C02_drafts.md
> │    └── 📂 05_EXPORTS/
> │      └── 📂 20260109_Hearing_Transcript_Exports/
> │        ├── 📄 20260209_C02_Site_Download_hearing_jan_09_2026.html
> │        ├── 📄 20260209_C02_hearing_jan_09_2026_transcript_regular.txt
> │        ├── 📄 _20260109_Hearing_Transcript_Exports.md
> │      ├── 📄 EX_V_09_31_20251209_1018_mp4_—_OFFICER_POSITIONE.md
> │      ├── 📄 EX_V_09_46_20251209_1033_mp4_—_POST_REMOVAL_ENTR.md
> │      ├── 📄 _05_EXPORTS (2).md
> │      ├── 📄 _05_EXPORTS (3).md
> │      ├── 📄 _05_EXPORTS.md
> │      └── 📂 events/
> │        ├── 📄 025_12_09_Removal_Day_Camera_Bedroom.md
> │        ├── 📄 20250109_order_Court_Orders_And_Hearing_Schedule.md
> │        ├── 📄 20250109_order_Order_Court_Orders_And_Hearing_Sc.md
> │        ├── 📄 20250116_Case_Filed.md
> │        ├── 📄 20250116_court_filing_Case_Filed.md
> │        ├── 📄 20250303_Service_Issued.md
> │        ├── 📄 20250305_Service_Attempt_1.md
> │        ├── 📄 20250305_motion_Motion_Motion_Motion_To_Vacate_V.md
> │        ├── 📄 20250305_motion_Motion_Motion_To_Vacate_Void_Jud.md
> │        ├── 📄 20250305_motion_Motion_To_Vacate_Void_Judgement.md
> │        ├── 📄 20250409_service_Service_Attempt_2.md
> │        ├── 📄 20250415_Service_Attempt_2.md
> │        ├── 📄 20250513_Motion_for_Default_Judgment.md
> │        ├── 📄 20250513_motion_Motion_For_Default_Judgment.md
> │        ├── 📄 20250613_document_Sheriff_Sale_Notice_Posted.md
> │        ├── 📄 20250709_Sheriff_Sale_Notice_Posted.md
> │        ├── 📄 20250717_Plaintiff_Bid_Filed.md
> │        ├── 📄 20250805_document_030_Report_Sheriff_Sale_No_Exc.md
> │        ├── 📄 20250815_enforcement_Writ_Of_Assistance_Issued.md
> │        ├── 📄 20251126_Sheriff_At_Home_Unrelated_No_Notice.md
> │        ├── 📄 20251203_Police_Knocked_Then_Left_Quickly.md
> │        ├── 📄 20251207_Retrieval_Day.md
> │        ├── 📄 20251209_1033_Post_Removal_Entry_Privacy_Violati.md
> │        ├── 📄 20251209_1046_Camera_System_Manipulation.md
> │        ├── 📄 20251209_1048_Refrigerator_Unplugged.md
> │        ├── 📄 20251209_Removal_Day_Photos.md
> │        ├── 📄 20251214_Other_Camera_Porch_Activity.md
> │        ├── 📄 20251216_AES_Emergency_Notice.md
> │        ├── 📄 20251216_Emergency_Supplemental_Declaration_File.md
> │        ├── 📄 20251221_DOJ_Civil_Rights_Complaint_Submitted.md
> │        ├── 📄 EX_V_09_29_20251209_1016_mp4_—_SHERIFF_INSIDE_BE.md
> │        ├── 📄 EX_V_09_32_20251209_1019_mp4_—_CONTINUED_INTERFE.md
> │        ├── 📄 EX_V_09_33_20251209_1020_mp4_—_ROOM_VACANT_(BASE.md
> │        ├── 📄 EX_V_09_47_20251209_1034_mp4_—_ABSENCE_FROM_ROOM.md
> │        ├── 📄 EX_V_09_59_20251209_1046_mp4_—_RE_ENTRY_AND_CAME.md
> │        ├── 📄 EX_V_09_60_20251209_1047_mp4_—_ELECTRONICS_AND_C.md
> │        ├── 📄 EX_V_09_61_20251209_1048_mp4_—_REFRIGERATOR_UNPL.md
> │        ├── 📄 NT_Video_Narration_Log_Removal_Day.md
> │        ├── 📄 _checklist.md
> │        ├── 📄 _events.md
> │    ├── 📄 ADA_Disability_Affidavit.md
> │    ├── 📄 FCFCU_CASE_MASTER - 4_docs.csv
> │    ├── 📄 FCFCU_CASE_MASTER - 4_docs.csv.md
> │    ├── 📄 _05_OUTPUT.md
> │    ├── 📄 _10_Service_Animal_Notice.md
> │    ├── 📄 _50_output.md
> │    ├── 📄 _60_CMS_Caretaker_Impact.md
> │    ├── 📄 _65_SSA_OIG.md
> │    ├── 📄 _70_VA_Informational.md
> │    ├── 📄 _Advocate_Outreach_Message.md
> │    └── 📂 _drafts/
> │      ├── 📄 2026-02-15_Draft_Letters.md
> │      ├── 📄 20260202_draft_housing_affidavit.html
> │      ├── 📄 20260203_draft_Equifax_Dispute_Letter.html
> │      └── 📂 Consumer_Statements/
> │        ├── 📄 Consumer_Statement_Landlords.md
> │        ├── 📄 Emergency_Credit_Harm_Addendum.md
> │        ├── 📄 _Consumer_Statements.md
> │      ├── 📄 Exhibit_N_001_DECLARATION_OF_CODY_RICE_VELASQUEZ.md
> │      ├── 📄 Formal_Retrieval_Protocol_ADA.md
> │      ├── 📄 NOTICE OF INTENT TO PURSUE FURTHER ACTION.md
> │      ├── 📄 __drafts.md
> │    └── 📂 _final/
> │      ├── 📄 2026-02-02_Equifax_Dispute_Letter.html
> │      ├── 📄 2026-02-02_Experian_Dispute_Letter.html
> │      ├── 📄 2026-02-02_TransUnion_Dispute_Letter.html
> │      ├── 📄 2026-02-03_FCFCU_Furnisher_Deletion_Demand_FINAL.html
> │      ├── 📄 Credit_Dispute_Master_Packet_Index.html
> │      ├── 📄 Equifax_dispute_letter.html
> │      ├── 📄 Landlord_Explanation_Letter.html
> │      ├── 📄 Landlord_Statement.html
> │      ├── 📄 a0.01.001_one_page_case_summary.html
> │      ├── 📄 a0.01.002_hearing_scope_and_relief.html
> │      ├── 📄 ada_disability_affidavit.html
> │      ├── 📄 ada_packet.html
> │      ├── 📄 affidavit_not_served.html
> │      ├── 📄 attorney_brief.html
> │      ├── 📄 b1.01.001_core_issue_statement.html
> │      ├── 📄 b1.01.002_trial_rule_4_1_b_standard.html
> │      ├── 📄 b1.01.003_void_vs_voidable_case_law.html
> │      ├── 📄 c2.03.004_odyssey_envelope_receipt.html
> │      ├── 📄 case-narrative-wrongful-foreclosure-and-displ.html
> │      ├── 📄 case_conversation_log.html
> │      ├── 📄 character_affidavit.html
> │      ├── 📄 cms_ssa_caretaker.html
> │      ├── 📄 cold_risk_report.html
> │      ├── 📄 credibility_affidavit.html
> │      ├── 📄 crisis_the_anatomy_of_institutional_failure.html
> │      ├── 📄 dfi_servicing_complaint.html
> │      ├── 📄 doj_supplemental.html
> │      ├── 📄 donations_context.html
> │      ├── 📄 emergency_filing_packet.html
> │      ├── 📄 equifax.html
> │      └── 📂 exhibits/
> │        ├── 📄 _exhibits.md
> │      ├── 📄 fcc_harassment.html
> │      ├── 📄 fcfcu_v_cr-v_report_to_court.html
> │      ├── 📄 file-tree-content.html
> │      └── 📂 filings/
> │        ├── 📄 _filings.md
> │      ├── 📄 gender_identity_clarification.html
> │      ├── 📄 hud_fheo_narrative.html
> │      ├── 📄 i8.02.001_research_and_notes.html
> │      ├── 📄 i8.99.999_internal_do_not_print.html
> │      ├── 📄 icrc_civil_rights.html
> │      ├── 📄 legal-memorandum.html
> │      └── 📂 letters/
> │        ├── 📄 _letters.md
> │      ├── 📄 long_term_payout_strategy.html
> │      ├── 📄 master_strategic_timeline.html
> │      ├── 📄 master_timeline.html
> │      ├── 📄 master_violation_inventory.html
> │      ├── 📄 migration_notes.html
> │      ├── 📄 ncua_complaint.html
> │      ├── 📄 observations_affidavit.html
> │      ├── 📄 odyssey_envelope_receipt.html
> │      └── 📂 orders/
> │        ├── 📄 _orders.md
> │      └── 📂 packets/
> │        ├── 📄 HEARING_Cheat_Sheet.md
> │        ├── 📄 _packets.md
> │      ├── 📄 procedural_failure_map_one_pager.html
> │      ├── 📄 proposal-for-strategic-reports-in-the-matter-.html
> │      ├── 📄 public_statement.html
> │      ├── 📄 receipt_usps_tracking.html
> │      ├── 📄 report_to_court_on_defendants_request.html
> │      ├── 📄 sheriff_internal_affairs.html
> │      ├── 📄 strategic_plan.html
> │      ├── 📄 talking_points.html
> │      ├── 📄 timeline_canvas.html
> │      ├── 📄 transunion.html
> │      ├── 📄 updated_affidavit_language.html
> │      ├── 📄 va_informational.html
> │      ├── 📄 verified_affidavit_of_defendant.html
> │      ├── 📄 void_judgment_eviction_crisis.html
> │    ├── 📄 _settlement_letter_draft.md
> │    └── 📂 analysis/
> │      └── 📂 00_Strategy/
> │        ├── 📄 _00_Strategy.md
> │    ├── 📄 docs.md
> │  └── 📂 05_DISPUTES/
> │    ├── 📄 00_COMPLAINT_PACKET_CHECKLIST.md
> │    ├── 📄 FCFCU_CASE_MASTER - 5_disputes.csv
> │    ├── 📄 FCFCU_CASE_MASTER - 5_disputes.csv.md
> │    ├── 📄 Ledger.txt
> │    ├── 📄 _04_LEDGER.md
> │  └── 📂 06_DAMAGES/
> │    ├── 📄 04_CASE_VALUATION.md
> │    ├── 📄 FCFCU_CASE_MASTER - 6_damages.csv
> │    ├── 📄 FCFCU_CASE_MASTER - 6_damages.csv.md
> │    ├── 📄 _20_ledgers.md
> │    ├── 📄 _30_Trackers.md
> │    └── 📂 harm_damages/
> │      ├── 📄 99_Legacy_Excerpt.md
> │      ├── 📄 _harm_damages.md
> │  └── 📂 07_ACTORS/
> │    ├── 📄 FCFCU_CASE_MASTER - 7_actors.csv
> │  └── 📂 08_ENTITIES/
> │    ├── 📄 _README.md
> │  └── 📂 90_ADMIN/
> │    ├── 📄 _00_ADMIN.md
> │    └── 📂 analysis/
> │      └── 📂 00_Strategy/
> │        ├── 📄 20260201_STRATEGY_Auto_Save_D0015.canvas
> │        ├── 📄 20260201_STRATEGY_Auto_Save_D0016.canvas
> │        ├── 📄 20260207_STRATEGY_Auto_Save_D0009.canvas
> │        ├── 📄 20260207_STRATEGY_Auto_Save_D0010.canvas
> │        ├── 📄 20260207_STRATEGY_Auto_Save_D0012.canvas
> │        ├── 📄 20260207_STRATEGY_Auto_Save_D0013.canvas
> │        ├── 📄 20260207_STRATEGY_Auto_Save_D0134.canvas
> │        ├── 📄 20260207_STRATEGY_Auto_Save_D0152.canvas
> │        ├── 📄 20260207_STRATEGY_Auto_Save_D0153.canvas
> │      ├── 📄 20260210_DATA_FCFCU_Case_Master_GS1.csv
> │      ├── 📄 20260210_REPORT_AI_Analysis_Grok_2.pdf
> │      ├── 📄 20260212_NOTES_Dictated_Case_Review.txt
> │      ├── 📄 Timeline_Inventory.csv
> │      ├── 📄 _analysis.md
> │    └── 📂 logs/
> │      ├── 📄 20260203_C01_FORECL_FCFCU_DOC_D0551.pdf
> │      ├── 📄 20260203_C01_FORECL_FCFCU_ORDER_D0549.pdf
> │      ├── 📄 20260203_C01_FORECL_ORDER_D0550.pdf
> │      ├── 📄 20260210_REPORT_AI_Analysis_Grok.pdf
> │      ├── 📄 Service_Log.md
> │      ├── 📄 _05_LOGS.md
> │    └── 📂 references/
> │      ├── 📄 1975_CIVIL_RIGHTS_.md
> │      ├── 📄 1977_19_PROCEDURAL_.md
> │      ├── 📄 1980s_FAIR_HOUSING_ACT_BREACH__EXCLUSIONARY_ZONING__.md
> │      ├── 📄 1985_PROCEDURAL_.md
> │      ├── 📄 2000_PROCEDURAL_.md
> │      ├── 📄 2009_Ca_PROCEDURAL_.md
> │      ├── 📄 2009_FAIR_HOUSING_ACT_BREACH__PATTERN_OR_PRACTICE_OF_REDLINING__.md
> │      ├── 📄 2010_20_ADA_.md
> │      ├── 📄 2020_FAIR_HOUSING_ACT_BREACH__REASONABLE_ACCOMMODATION_FAILURE__.md
> │      ├── 📄 2026_REF_FCRA_Remedies.pdf
> │      ├── 📄 99_CASE_SCHEMA.md
> │      ├── 📄 April 20_FAIR_HOUSING_ACT_BREACH__RACE__NATIONAL_ORIGIN___HOSTILE_HOUSING_ENVIRONMENT_.md
> │      ├── 📄 April 20_FAIR_HOUSING_ACT_BREACH__SEXUAL_HARASSMENT__.md
> │      ├── 📄 August 1_FAIR_HOUSING_ACT_BREACH__ACCESSIBILITY_REQUIREMENTS__.md
> │      ├── 📄 August 2_FAILURE_TO_PROVIDE_EQUAL_MAINTENANCE_SERVICES__REO_DWELLINGS__.md
> │      ├── 📄 August 2_FAIR_HOUSING_ACT_BREACH__GENDER___SEXUAL_HARASSMENT_.md
> │      ├── 📄 August 2_POTENTIAL_IC___32_30_10_14_VIOLATION__SURPLUS_MISMANAGEMENT__.md
> │      ├── 📄 Early 20_ADA_.md
> │      ├── 📄 February_FAIR_HOUSING_ACT_BREACH__DISABILITY__FAMILIAL_STATUS__.md
> │      ├── 📄 Google Sheets Validation Guide.md
> │      ├── 📄 January _DUE_PROCESS_FAILURE___NOTICE_DEFICIENCY_.md
> │      ├── 📄 January _FAIR_HOUSING_ACT_BREACH__FAMILIAL_STATUS___OCCUPANCY_POLICIES_.md
> │      ├── 📄 July 201_FAIR_HOUSING_ACT_BREACH__INTENTIONAL_DISCRIMINATION___DISPARATE_IMPACT__.md
> │      ├── 📄 June 8, _ADA_.md
> │      ├── 📄 June 9, _PROCEDURAL_.md
> │      ├── 📄 March 20_FAIR_HOUSING_ACT_BREACH__FAMILIAL_STATUS__.md
> │      ├── 📄 March 20_FAIR_HOUSING_ACT_BREACH__RACE__COLOR___APPRAISAL_BIAS_.md
> │      ├── 📄 March 5,_DUE_PROCESS_FAILURE___DEFECTIVE_SERVICE_.md
> │      ├── 📄 March 5,_PROCEDURAL_.md
> │      ├── 📄 May 28, _FORECLOSURE_.md
> │      ├── 📄 May 28, _PROCEDURAL_.md
> │      ├── 📄 Not in s_ADA_.md
> │      ├── 📄 Not in s_DISCRIMINATORY_ADVERTISING_.md
> │      ├── 📄 Not in s_DUE_PROCESS_VIOLATION__STANDARD_OF_PROOF__.md
> │      ├── 📄 Not in s_FAIR_HOUSING_ACT_BREACH__REASONABLE_ACCOMMODATION_FAILURE__.md
> │      ├── 📄 Not in s_PROCEDURAL_.md
> │      ├── 📄 Not in s_SECTION_504_BREACH___FAILURE_TO_PROVIDE_INTERPRETER_.md
> │      ├── 📄 Not in s_UNCONSTITUTIONAL_PRESUMPTION__VESTING_OF_TITLE__.md
> │      ├── 📄 November_FAIR_HOUSING_ACT_BREACH__REASONABLE_ACCOMMODATION_DENIAL__.md
> │      ├── 📄 November_FRAUD_ON_THE_COURT___MATERIAL_MISREPRESENTATION_.md
> │      ├── 📄 October _FAIR_HOUSING_ACT_BREACH__RACE__NATIONAL_ORIGIN___DISCRIMINATORY_MAINTENANCE_.md
> │      ├── 📄 October _FAIR_HOUSING_ACT_BREACH__RACE___REDLINING_.md
> │      ├── 📄 Preforec_ADA_.md
> │      ├── 📄 Septembe_FAIR_HOUSING_ACT_BREACH__RACE___ARBITRARY_CRIMINAL_HISTORY_POLICIES_.md
> │      ├── 📄 _references.md
> │      ├── 📄 rules.md
> │      ├── 📄 schema.json
> │    └── 📂 templates/
> │      ├── 📄 Notebooklm-prompts.md
> │      ├── 📄 _templates.md
> │      └── 📂 affidavits/
> │        ├── 📄 EMERGENCY SUPPLEMENTAL DECLARATION.gdoc
> │        ├── 📄 TPL_Affidavit_ADA_Disability.md
> │        ├── 📄 TPL_Affidavit_Character.md
> │        ├── 📄 TPL_Affidavit_Community_Service.md
> │        ├── 📄 TPL_Affidavit_Credibility.md
> │        ├── 📄 TPL_Affidavit_Language_Updates.md
> │        ├── 📄 TPL_Affidavit_Observations.md
> │        ├── 📄 TPL_Affidavit_Verified_Defendant.md
> │        ├── 📄 TPL_Declaration_Gender_Identity_Clarification.md
> │        ├── 📄 TPL_housing_affidavit.md
> │        ├── 📄 WF5.01.010__Credibility_Affidavit.md
> │        ├── 📄 WF5.01.010__Gender_Identity_Clarification.md
> │        ├── 📄 WF5.01.010__updated_affidavit_language.md
> │        ├── 📄 WF5.01.010__verified_affidavit_of_defendant.md
> │        ├── 📄 _affidavits.md
> │      └── 📂 binders/
> │        ├── 📄 TPL_Binder_Section_Cover.md
> │        ├── 📄 TPL_Binder_Section_Index.md
> │        ├── 📄 _binders.md
> │      └── 📂 exhibits/
> │        ├── 📄 TPL_Exhibits_Lists.md
> │        ├── 📄 _exhibits.md
> │      └── 📂 front_matter/
> │        ├── 📄 FRONT_MATTER_MIGRATION_INSTRUCTION.md
> │        ├── 📄 _front_matter.md
> │      └── 📂 internal/
> │        ├── 📄 TPL_settlement_letter_draft.md
> │        ├── 📄 _internal.md
> │      └── 📂 motions/
> │        ├── 📄 Copy of  EMERGENCY MOTION TO PRESERVE AND ACCOUNT FOR SURPLUS FUNDS.gdoc
> │        ├── 📄 EMERGENCY MOTION TO PRESERVE AND ACCOUNT FOR SURPLUS FUNDS.gdoc
> │        ├── 📄 TPL_emergency_stay_of_writ.md
> │        ├── 📄 TPL_vacate_void_judgment.md
> │        ├── 📄 _10_motions.md
> │        ├── 📄 _motions.md
> │      └── 📂 orders/
> │        ├── 📄 TPL_Proposed_Order.md
> │        ├── 📄 TPL_proposed_order_emergency_stay.md
> │        ├── 📄 TPL_proposed_order_motion_to_vacate.md
> │        ├── 📄 _orders.md
> │      └── 📂 outreach/
> │        ├── 📄 TPL_Advocate_Outreach.md
> │        ├── 📄 TPL_Attorney_Brief.md
> │        ├── 📄 _outreach.md
> │      └── 📂 packets/
> │        ├── 📄 TPL_ADA_Packet.md
> │        ├── 📄 TPL_Handup_Packet_Note.md
> │        ├── 📄 TPL_attorney_intake_packet_executive.md
> │        ├── 📄 _packets.md
> │  └── 📂 99_VAULT/
> │    └── 📂 C-00_DOCKET/
> │      ├── 📄 20250116_DKT_09_15_15_APPEARANCE.PDF
> │      ├── 📄 20250116_DKT_09_16_24_REQUEST_FOR_ADMISSIONS.PDF
> │      ├── 📄 20250116_DKT_09_17_12_NOTICE_TO_HOMEOWNERS.PDF
> │      ├── 📄 20250116_DKT_09_17_59_APPEARANCE.PDF
> │      ├── 📄 20250116_DKT_09_19_01_SUMMONS.PDF
> │      ├── 📄 20250116_DKT_09_19_33_SUMMONS.PDF
> │      ├── 📄 20250116_DKT_09_20_42_SUMMONS.PDF
> │      ├── 📄 20250116_DKT_09_21_26_SUMMONS.PDF
> │      ├── 📄 20250116_DKT_09_22_07_SUMMONS.PDF
> │      ├── 📄 20250116_DKT_COMPLAINT_AND_SUMMONS.PDF
> │      ├── 📄 20250305_DKT_SERVICE_RETURNED_SERVED_1.PDF
> │      ├── 📄 20250415_DKT_SERVICE_RETURNED_SERVED_2.PDF
> │      ├── 📄 20250513_DKT_14_52_56_MOTION_DEFAULT.PDF
> │      ├── 📄 20250513_DKT_14_53_36_AFFIDAVIT.PDF
> │      ├── 📄 20250513_DKT_14_54_31_AFFIDAVIT_ATTORNEY.PDF
> │      ├── 📄 20250513_DKT_MOTION_DEFAULT_JUDGMENT.PDF
> │      ├── 📄 20250521_DKT_14_25_43_OMITTED_NOTICE.PDF
> │      ├── 📄 20250521_DKT_USPS_CERTIFIED_RECEIPT.PDF
> │      ├── 📄 20250523_DKT_11_06_25_REQUEST_DEFAULT.PDF
> │      ├── 📄 20250523_DKT_MOTION_AMENDED_DEFAULT.PDF
> │      ├── 📄 20250528_DKT_PRAECIPE_FOR_SHERIFFS_SALES.PDF
> │      ├── 📄 20250529_DKT_AMENDED_DEFAULT_JUDGEMENT.PDF
> │      ├── 📄 20250709_DKT_NOTICE_SHERIFF_SALE_POSTED.PDF
> │      ├── 📄 20250717_DKT_PLAINTIFF_BID.PDF
> │      ├── 📄 20250909_DKT_DECREE_RETURNED.PDF
> │      ├── 📄 20251029_DKT_13_47_03_ORDER_FOR_WRIT.PDF
> │      ├── 📄 20251029_DKT_13_47_52_WRIT.PDF
> │      ├── 📄 20251029_DKT_PETITION_WRIT_ASSISTANCE.PDF
> │      ├── 📄 20251211_DKT_EMERGENCY_MOTION_STAY_WRIT.PDF
> │      ├── 📄 20251211_DKT_EXHIBIT_LIST.PDF
> │      ├── 📄 20251211_DKT_MOTION_TO_VACATE_JUDGMENT.PDF
> │      ├── 📄 20251211_DKT_PROPOSED_ORDER_STAY.PDF
> │      ├── 📄 20251211_DKT_PROPOSED_ORDER_VACATE.PDF
> │      ├── 📄 20251211_DKT_SUPPLEMENTAL_EMERGENCY_MOTION.PDF
> │      ├── 📄 20251212_DKT_NOTICE_OBTAIN_ITEM_REPORT.PDF
> │      ├── 📄 20251216_DKT_EMERGENCY_SUPPLEMENTAL_DECLARATION.PDF
> │      ├── 📄 20251216_DKT_MOTION_PRESERVE_SURPLUS.PDF
> │      ├── 📄 20251217_DKT_REPORT_SHERIFF_SALE.PDF
> │      ├── 📄 20251222_DKT_DECLARATION_ONGOING_DISPLACEMENT.PDF
> │      ├── 📄 20260109_DKT_HEARING_JOURNAL_ENTRY.PDF
> │      ├── 📄 20260121_DKT_ORDER_DENYING_VACATE.PDF
> │      ├── 📄 20260209_DKT_CASE_DOC_TEMPLATE.PDF
> │      ├── 📄 FCFCU_CASE_MASTER - 0_docket.csv.md
> │      ├── 📄 _C00_DOCKET.md
> │      ├── 📄 _MYCASE_DOCKET_SUMMARY.MD
> │    └── 📂 E-00_Raw_Intake/
> │      └── 📂 MD/
> │        ├── 📄 AES_Utility_Violation_Excerpt.md
> │        ├── 📄 B1.00.000_SECTION_COVER.md
> │        ├── 📄 B1.01.001_CORE_ISSUE_STATEMENT.md
> │        ├── 📄 B1.01.002_TRIAL_RULE_4_1_B_STANDARD.md
> │        ├── 📄 B1.01.003_VOID_VS_VOIDABLE_CASE_LAW.md
> │        ├── 📄 BBB_Complaint_Narrative.md
> │        ├── 📄 BBB_Violation_Excerpt.md
> │        ├── 📄 C2.00.000_SECTION_COVER.md
> │        ├── 📄 C2.01.001_MOTION_TO_VACATE_VOID_JUDGMENT.md
> │        ├── 📄 C2.02.001_EMERGENCY_MOTION_STAY_OR_QUASH.md
> │        ├── 📄 C2.03.001_SUPPLEMENTAL_EMERGENCY_MOTION.md
> │        ├── 📄 C2.04.001_PROPOSED_ORDER_VACATE.md
> │        ├── 📄 C2.04.002_PROPOSED_ORDER_STAY_WRIT.md
> │        ├── 📄 CFPB_Complaint_Draft.md
> │        ├── 📄 CFPB_Complaint_Narrative.md
> │        ├── 📄 CFPB_Escalation_Packet_DRAFT.md
> │        ├── 📄 CFPB_Violation_Excerpt.md
> │        ├── 📄 CFPB_Violation_Excerpt_Master.md
> │        ├── 📄 CMS_Informational_Complaint.md
> │        ├── 📄 Case Narrative - Wrongful Foreclosure and Displ.md
> │        ├── 📄 Case update.md
> │        ├── 📄 Case_Log.md
> │        ├── 📄 Character_Affidavit.md
> │        ├── 📄 Citizens_Utility_Violation_Excerpt.md
> │        ├── 📄 City_of_Indy_Violation_Excerpt.md
> │        ├── 📄 Cold_Risk_Report.md
> │        ├── 📄 Community_Service_Affidavit.md
> │        ├── 📄 Consumer_Statement_Landlords.md
> │        ├── 📄 Contacts.md
> │        ├── 📄 Cover_Letter.md
> │        ├── 📄 Cover_Letter_DOJ_Supplemental.md
> │        ├── 📄 Credibility_Affidavit.md
> │        ├── 📄 D3.00.000_SECTION_COVER.md
> │        ├── 📄 D3.03.001_SERVICE_DEFECT_ANALYSIS.md
> │        ├── 📄 DOJ_Civil_Rights_Violation_Excerpt.md
> │        ├── 📄 DOJ_Civil_Rights_Violation_Excerpt_Master.md
> │        ├── 📄 DOJ_Supplemental_Continuing_Harm.md
> │        ├── 📄 DOJ_Violation_Excerpt.md
> │        ├── 📄 Declaration_Secondary_Displacement_Otis.md
> │        ├── 📄 Demand_Notice_and_Ledger.md
> │        ├── 📄 Donations_Context.md
> │        ├── 📄 E4.05.001_PROCEDURAL_CHAIN_SUMMARY.md
> │        ├── 📄 EMERGENCY_FILING_PACKET.md
> │        ├── 📄 EXPOSURE_CONSEQUENTIAL_CONSOLIDATED.md
> │        ├── 📄 EXPOSURE_ECONOMIC_CONSOLIDATED.md
> │        ├── 📄 EXPOSURE_MISC_STRATEGY_CONSOLIDATED.md
> │        ├── 📄 EXPOSURE_NON_ECONOMIC_CONSOLIDATED.md
> │        ├── 📄 Emergency_Supplemental_Declaration_Consolidated.md
> │        ├── 📄 Equifax_Dispute_Letter.md
> │        ├── 📄 Equifax_Violation_Excerpt.md
> │        ├── 📄 Evidence_Log.md
> │        ├── 📄 Exhibit X — Inventory of Jurisdictional, Execut.md
> │        ├── 📄 Exhibit_Manifest.md
> │        ├── 📄 Experian_Dispute_Letter.md
> │        ├── 📄 Experian_Violation_Excerpt.md
> │        ├── 📄 F5.00.000_SECTION_COVER.md
> │        ├── 📄 F5.01.001_AFFIDAVIT_NOT_SERVED.md
> │        ├── 📄 F5.02.001_DECLARATION_ONGOING_HARM.md
> │        ├── 📄 F5.03.001_CREDIBILITY_DECLARATION.md
> │        ├── 📄 FCC_Harassment_Complaint.md
> │        ├── 📄 FCC_Violation_Excerpt.md
> │        ├── 📄 Financial_Tracker.md
> │        ├── 📄 Foreclosure Irregularities and Forensic Accounting.md
> │        ├── 📄 G6.03.001_ADA_IMPACT_SUMMARY.md
> │        ├── 📄 Gender_Identity_Clarification.md
> │        ├── 📄 Gigi_Documentation_Pack.md
> │        ├── 📄 Gigi_Service_Dog_Training_Manual.md
> │        ├── 📄 HUD_FHEO_Complaint_Narrative.md
> │        ├── 📄 HUD_FHEO_Violation_Excerpt.md
> │        ├── 📄 HUD_Violation_Excerpt_OLD.md
> │        ├── 📄 I8.02.001_RESEARCH_AND_NOTES.md
> │        ├── 📄 I8.99.999_INTERNAL_DO_NOT_PRINT.md
> │        ├── 📄 I8_01_000_CASE_SUMMARY.md
> │        ├── 📄 ICRC_Violation_Excerpt.md
> │        ├── 📄 INTERNAL VALUATION MEMO.md
> │        ├── 📄 IN_AG_Violation_Excerpt.md
> │        ├── 📄 IN_DFI_Violation_Excerpt.md
> │        ├── 📄 Indiana_AG_Complaint_Narrative.md
> │        ├── 📄 Indiana_Civil_Rights_Commission_Violation_Excerpt.md
> │        ├── 📄 Indiana_Civil_Rights_Complaint_Narrative.md
> │        ├── 📄 Indiana_DFI_Complaint_Narrative.md
> │        ├── 📄 Indiana_Department_of_Financial_Institutions_DFI_Violation_Excerpt.md
> │        ├── 📄 J9.01.001_COURT_SET_MASTER.md
> │        ├── 📄 J9.01.002_PERSONAL_MASTER.md
> │        ├── 📄 J9.01.003_OPPOSITION_SET_MASTER.md
> │        ├── 📄 J9.01.004_INTERNAL_RED_MASTER.md
> │        ├── 📄 LEGAL MEMORANDUM.md
> │        ├── 📄 Litigation_Decision_Tree.md
> │        ├── 📄 Long_Term_Payout_Strategy.md
> │        ├── 📄 MANIFEST_Credit_Bureau_Dispute_Packet.md
> │        ├── 📄 MANIFEST_HUD_FHEO_Complaint_Packet.md
> │        ├── 📄 MANIFEST_ICRC_Complaint_Packet.md
> │        ├── 📄 MANIFEST_IN_AG_Complaint_Packet.md
> │        ├── 📄 MANIFEST_Indiana_DFI_Packet.md
> │        ├── 📄 MANIFEST_NCUA_Complaint_Packet.md
> │        ├── 📄 MANIFEST_PHASE_03_SENDS.md
> │        ├── 📄 MANIFEST_Reserve_Informational_Filings.md
> │        ├── 📄 MANIFEST_Sheriff_Oversight_Packet.md
> │        ├── 📄 MITIGATION_LOG_Temporary_Housing.md
> │        ├── 📄 Marion_County_Sheriff_Oversight_Violation_Excerpt.md
> │        ├── 📄 Master_Timeline.md
> │        ├── 📄 Master_Timeline_Strategy_Summary.md
> │        ├── 📄 Motions.md
> │        ├── 📄 NCUA_Complaint_Narrative.md
> │        ├── 📄 NCUA_Complaint_Narrative_draft_old.md
> │        ├── 📄 NCUA_Violation_Excerpt.md
> │        ├── 📄 NT_2025-12-21_Gigi_Escape_Displacement_Safety_Event.md
> │        ├── 📄 NT_Attorney_Intake_Packet_Executive.md
> │        ├── 📄 NT_Attorney_Intake_Summary.md
> │        ├── 📄 NT_Damages_Matrix_Ab_Initio.md
> │        ├── 📄 NT_Demand_Ready_Exposure_Summary.md
> │        ├── 📄 NT_Financial_Tracker.md
> │        ├── 📄 NT_Forced_Relocation_Market_Loss_Memo.md
> │        ├── 📄 NT_Forensic_Accounting_Audit_Summary.md
> │        ├── 📄 NT_INTERNAL VALUATION MEMO.md
> │        ├── 📄 NT_Monetary_Exposure_Estimate.md
> │        ├── 📄 NT_Payment_Portal_and_Check_History.md
> │        ├── 📄 NT_Post_Removal_Artifact_Checklist.md
> │        ├── 📄 NT_Procedural_failure_map_one_pager.md
> │        ├── 📄 NT_Quarantined_Claims_Hold.md
> │        ├── 📄 NT_Violation_Remedy_Inventory.md
> │        ├── 📄 Notice_of_Evidence_Preservation.md
> │        ├── 📄 Observations_Affidavit.md
> │        ├── 📄 PHASE_04_Regulators.md
> │        ├── 📄 PHASE_05_Litigation.md
> │        ├── 📄 Phase_01_5_Preservation_Packet_Cover_Sheet.md
> │        ├── 📄 Premonitions_I_Knew_Before_I_Knew.md
> │        ├── 📄 Procedural_failure_map_one_pager.md
> │        ├── 📄 Proposal for Strategic Reports in the Matter of.md
> │        ├── 📄 Proposed_Orders.md
> │        ├── 📄 README.md
> │        ├── 📄 README_supporting.md
> │        ├── 📄 Raw_Exhibit_Map.md
> │        ├── 📄 Room_Conditions_Factual_Log.md
> │        ├── 📄 SSA_OIG_Informational_Filing.md
> │        ├── 📄 Sanctions_Readiness_Memo.md
> │        ├── 📄 Session_Summary_2025-12-15_i_knew_before_i_knew.md
> │        ├── 📄 Settlement_Strategy_and_Contingency_Plan.md
> │        ├── 📄 Sheriff_Internal_Affairs_Complaint.md
> │        ├── 📄 Sheriff_Violation_Excerpt.md
> │        ├── 📄 Supplemental_Declaration_Accounting_Surplus.md
> │        ├── 📄 Supplemental_Declaration_Cody_DRAFT.md
> │        ├── 📄 TEMPLATE_COURT_DOC.md
> │        ├── 📄 TEMPLATE_EXHIBIT_LABEL.md
> │        ├── 📄 TEMPLATE_HANDUP_PACKET_NOTE.md
> │        ├── 📄 TEMPLATE_SECTION_COVER.md
> │        ├── 📄 TEMPLATE_SECTION_INDEX.md
> │        ├── 📄 TEMPLATE_WAR_NOTE.md
> │        ├── 📄 Talking_Points.md
> │        ├── 📄 TransUnion_Violation_Excerpt.md
> │        ├── 📄 VA_Informational_Filing.md
> │        ├── 📄 Violation_to_Regulator_Mapping.md
> │        ├── 📄 _00_RECEIVED.md
> │        ├── 📄 ada_packet.md
> │        ├── 📄 affidavit_not_served.md
> │        ├── 📄 attorney_brief.md
> │        ├── 📄 exhibit_list.md
> │        ├── 📄 index.md
> │        ├── 📄 motion_emergency_stay_of_writ.md
> │        ├── 📄 motion_emergency_supplemental_motion_ongoing_ha.md
> │        ├── 📄 motion_to_vacate_void_judgment.md
> │        ├── 📄 proposed_order_emergency_stay.md
> │        ├── 📄 proposed_order_motion_to_vacate.md
> │        ├── 📄 receipt_usps_tracking.md
> │        ├── 📄 script_call_lawyers.md
> │        ├── 📄 spoliation_risk_ledger.md
> │        ├── 📄 updated_affidavit_language.md
> │        ├── 📄 verified_affidavit_of_defendant.md
> │      └── 📂 docs/
> │        ├── 📄 009_Summons_4.pdf
> │        ├── 📄 010_Summons_5.pdf
> │        ├── 📄 014_Affidavit.pdf
> │        ├── 📄 018_Omitted_Notice_of_Service.pdf
> │        ├── 📄 023_Decree_Foreclosure_Returned.pdf
> │        ├── 📄 024_Petition_Writ_of_Assistance.pdf
> │        ├── 📄 025_Motion_Vacate_Stay_Writ.pdf
> │        ├── 📄 026_Exhibit_List_A-G.pdf
> │        ├── 📄 027_Supplemental_Motion_Access.pdf
> │        ├── 📄 028_Report_Court_Defendant_Request.pdf
> │        ├── 📄 029_Emergency_Supplemental_Declaration.pdf
> │        ├── 📄 030_Report_Sheriff_Sale_No_Excess.pdf
> │        ├── 📄 031_Proposed_Order_Vacate.pdf
> │        ├── 📄 032_Proposed_Order_Stay.pdf
> │        ├── 📄 033_ADA_Disability_Affidavit.pdf
> │        ├── 📄 0809b8fd-4b31-4ac4-a5f5-561da006d165.pdf
> │        ├── 📄 13312381_invoice.pdf
> │        ├── 📄 13312381_tmp.pdf
> │        ├── 📄 13312462_invoice.pdf
> │        ├── 📄 13312462_tmp.pdf
> │        ├── 📄 13312465_invoice.pdf
> │        ├── 📄 13312465_tmp.pdf
> │        ├── 📄 13348806_tmp.pdf
> │        ├── 📄 13383977_invoice.pdf
> │        ├── 📄 13383977_tmp.pdf
> │        ├── 📄 15c873fa-5cfd-4980-be43-dd077effeb2b.pdf
> │        ├── 📄 1990-05-18_FORMAL DISPUTE OF INACCURATE REPORTING Copy.pdf
> │        ├── 📄 2023-09-20_Notice_Disabilities_Hardship.pdf
> │        ├── 📄 2024-12-09_outgoing_email_bank_access_request.pdf
> │        ├── 📄 2024-12-11_outgoing_email_bank_access_request.pdf
> │        ├── 📄 2024-20-03_Response_to_tax_notice.pdf
> │        ├── 📄 20241204_FCFCU_Statement.pdf
> │        ├── 📄 2025-06-08_AES_ADA_Notice.pdf
> │        ├── 📄 2025-12-21_Exhibit_V-03-02_DECLARATION RE PRIOR LAW ENFORCEMENT CONTACTS, AUDIBILITY LIMITATIONS, AND SAFETY CONTEXT_crice4485@gmail.com.pdf
> │        ├── 📄 2025-12-21_ForensicAudit_FCFCU.pdf
> │        ├── 📄 2025-12-22_DOJ_Civil_Rights_Report_688619-FXN.pdf
> │        ├── 📄 2025_01_16_09_16_24.pdf.pdf
> │        ├── 📄 2025_05_13_14_52_56.pdf.pdf
> │        ├── 📄 2025_05_13_14_54_31.pdf.pdf
> │        ├── 📄 2025_05_13_14_55_22.pdf.pdf
> │        ├── 📄 2025_05_21_14_25_43.pdf.pdf
> │        ├── 📄 2025_05_23_11_06_25.pdf.pdf
> │        ├── 📄 2025_05_23_11_07_23.pdf.pdf
> │        ├── 📄 2025_05_29_14_15_32.pdf.pdf
> │        ├── 📄 2025_05_29_14_15_54.pdf.pdf
> │        ├── 📄 2026-02-03_BASIS OF DISPUTE (NON-CURABLE DEFECTS).pdf
> │        ├── 📄 21June-24-4817Shadow_Appraisal.pdf
> │        ├── 📄 50100846854.pdf
> │        ├── 📄 50100879809.pdf
> │        ├── 📄 50100883027.pdf
> │        ├── 📄 50100916138.pdf
> │        ├── 📄 5bf7e045-828d-4cac-8a3f-fc3b31439649.pdf
> │        ├── 📄 67e9f7c4-a021-441d-b1ce-ba3e7a034b8e.pdf
> │        ├── 📄 7dba97cb-da59-4f70-9e9e-6a7f9b300c07.pdf
> │        ├── 📄 8b2ae2d6-b47c-4086-bb36-675c455c1c72.pdf
> │        ├── 📄 9214890142980444614178.pdf
> │        ├── 📄 9214890142980444614581.pdf
> │        ├── 📄 9214890142980444614741.pdf
> │        ├── 📄 C2.01.002_motion_vacate.pdf
> │        ├── 📄 C2.01.003_Exhibit_List.pdf
> │        ├── 📄 C2.01.004_Exhibits_Combined.pdf
> │        ├── 📄 C2.02.002_Emergency_Motion_Stay_OR_Quash.pdf
> │        ├── 📄 C2.03.004_Odyssey_Envelope_Receipt.pdf
> │        ├── 📄 C2.03.005_COMBINED_SOURCE.pdf
> │        ├── 📄 C2.04.001_order_vacate_proposed.pdf
> │        ├── 📄 C2.04.002_order_stay_writ_proposed.pdf
> │        ├── 📄 CPR certification (1).pdf
> │        ├── 📄 Call Customer Care.pdf
> │        ├── 📄 Chase Credit Journey - Credit report.pdf
> │        ├── 📄 Chase Credit Journey.pdf
> │        ├── 📄 Credit Report.pdf
> │        ├── 📄 Crisis_The_Anatomy_of_Institutional_Failure.pdf
> │        ├── 📄 DLGF_ Tax Bill Search.pdf
> │        ├── 📄 Emergency Motions.gdoc
> │        ├── 📄 Exhibit X — Inventory of Jurisdictional, Execution, and Civil Rights Violations.pdf
> │        ├── 📄 Exhibit_G1_ADA_Notice_Request.pdf
> │        ├── 📄 Exhibit_H_Declaration.pdf
> │        ├── 📄 Experian - Access your credit report-CH13.pdf
> │        ├── 📄 Experian - Access your credit report.pdf
> │        ├── 📄 Experian - Dispute Cart.pdf
> │        ├── 📄 Experian - Dispute Cart2.pdf
> │        ├── 📄 FCFCU_v_CR-V_Report_to_Court.pdf
> │        ├── 📄 FORMAL_SURPLUS_DEMAND_CAUSE_NO_49D03-2501-MF-002559_Sheriff_Sale_Date_08-15-2025.pdf
> │        ├── 📄 G6.01.001_ADA_NOTICE.pdf
> │        ├── 📄 Gmail - Dispute Received, Investigation in Process.pdf
> │        ├── 📄 Gmail - Follow-Up Courtesy Notice – Demand for Deletion of FCFCU Tradelines (Acct. 661563L____).pdf
> │        ├── 📄 Gmail - Surplus Demand – Sheriff Sale August 15, 2025.pdf
> │        ├── 📄 H7.01.0006_EXHIBIT_F_AFFIDAVIT.pdf
> │        ├── 📄 H7.01.0008_EXHIBIT_G2_AES_ADA_DOCUMENTS.pdf
> │        ├── 📄 I8_01_001_Complaint.pdf
> │        ├── 📄 I8_01_002_Appearance.pdf
> │        ├── 📄 I8_01_004_Notice_to_Homeowners.pdf
> │        ├── 📄 I8_01_005_Appearance_2.pdf
> │        ├── 📄 I8_01_006_Summons_1.pdf
> │        ├── 📄 I8_01_007_Summons_2.pdf
> │        ├── 📄 I8_01_008_Summons_3.pdf
> │        ├── 📄 Indy.gov_ Pay Your Property Taxes.pdf
> │        ├── 📄 Invoice.pdf
> │        ├── 📄 Invoice2.pdf
> │        ├── 📄 Invoice3.pdf
> │        ├── 📄 Invoice4.pdf
> │        ├── 📄 Marion County, IN, Estimated 2025 Taxes 6016506.pdf
> │        ├── 📄 Missing Evidence and Vanishing Foreclosure Surplus.pdf
> │        ├── 📄 My Account - Credit Card Receipt - LetterStream.pdf
> │        ├── 📄 MyTitle.pdf
> │        ├── 📄 Odyssey_Envelope_Receipt.pdf
> │        ├── 📄 Orientation_and_Onboardin_signed_pages_Copy.pdf
> │        ├── 📄 PART 2 — EMERGENCY MOTION TO STAY WRIT.gdoc
> │        ├── 📄 PART 3 — UPDATED AFFIDAVIT.gdoc
> │        ├── 📄 PROOF_OF_ADDRESS.pdf
> │        ├── 📄 Parcel_6016506_PRC.pdf
> │        ├── 📄 Parcel_6016506_ParcelDetailHistory.pdf
> │        ├── 📄 Proposed_Order_Vacate.docx
> │        ├── 📄 RAYS CONSTRUCTION.pdf
> │        ├── 📄 REPORT_TO_COURT_ON_DEFENDANTS_REQUEST.pdf
> │        ├── 📄 Search Results.pdf
> │        ├── 📄 Service_Returned_Served.pdf
> │        ├── 📄 Service_Returned_Served_(1).pdf
> │        ├── 📄 Summary_-_MyCase.pdf
> │        ├── 📄 Supplemental_Emergency_Motion.pdf
> │        ├── 📄 Wrongful_Foreclosure_A_Case_Study_in_Civil_Rig.pdf
> │        ├── 📄 Your accounts _ Credit Karma.pdf
> │        ├── 📄 Zoho One - Subscription Renewal - Final Reminder!.pdf
> │        ├── 📄 affidavit_not_served.docx
> │        ├── 📄 b16d8fad-1b70-4865-8403-71c7a3117b53.pdf
> │        ├── 📄 cody_rice_velasquez-fullstack (1).pdf
> │        ├── 📄 combinepdf.pdf
> │        ├── 📄 dfadadf.pdf
> │        ├── 📄 dfafa.pdf
> │        ├── 📄 dfafdsasdf.pdf
> │        ├── 📄 dfasdfadsffafaf.pdf
> │        ├── 📄 direct-deposit-form-CASHAPP.PDF
> │        ├── 📄 e-filing-efsp-comparison.pdf
> │        ├── 📄 efiling-user-guide.pdf
> │        ├── 📄 exhibit_list.docx
> │        ├── 📄 f588fab6-f89f-41c3-bfce-05ad0d108a06.pdf
> │        ├── 📄 formal_surplus_demand_certified.pdf
> │        ├── 📄 formal_surplus_demand_certified_counsel.pdf
> │        ├── 📄 id-card (3).pdf
> │        ├── 📄 identity_verification_letter_mission-lane-cc.pdf
> │        ├── 📄 indy_pvdnet_document.pdf
> │        ├── 📄 motion_emergency_stay_of_writ.docx
> │        ├── 📄 motion_emergency_supplemental_motion_ongoing_.docx
> │        ├── 📄 motion_to_vacate_void_judgement.docx
> │        ├── 📄 parcel_6016506_parceldetailhistory_3.pdf
> │        ├── 📄 parcel_6016506_prc_3.pdf
> │        ├── 📄 rss.xml
> │        ├── 📄 rttet.pdf
> │        ├── 📄 vehicle-insurance-id-card.pdf
> │        ├── 📄 void_judgment_eviction_crisis.pdf
> │        ├── 📄 wertwewtwtwt.pdf
> │      └── 📂 imgs/
> │        ├── 📄 05b618077343fbbd92b7.ttf
> │        ├── 📄 07192024_INVOICE_003.jpg
> │        ├── 📄 085cb93e613ba3d40d2b.woff2
> │        ├── 📄 2024-12-14_outgoing_text_bank_access_request.png
> │        ├── 📄 2025-12-20_EXH-10_photos_video_00241326_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_10f4975d_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_1beefb11_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_1f3f8a81_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_25fb1992_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_2f0952db_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_4e01fa01_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_5be451ba_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_5d95cae5_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_63fb7b02_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_71c9e6a7_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_7a544ef7_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_8350e7be_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_8a163413_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_8d885a5c_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_9b611100_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_9fb3a08a_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_9ff5022d_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_a8832e17_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_ca02d006_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_db9b10b5_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_e4cb3622_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_ebaaa38d_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_f510498b_2025-.heic
> │        ├── 📄 2025-12-20_EXH-10_photos_video_f60d8098_2025-1.png
> │        ├── 📄 2025-12-20_EXH-10_photos_video_f98b089a_2025-1.png
> │        ├── 📄 2025-12-20_EXH-10_photos_video_fa1703bf_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-10_photos_video_fdd8d4ef_2025-1.jpg
> │        ├── 📄 2025-12-20_EXH-30_fcfcu_740eacdc_2025-12-20_EX.jpg
> │        ├── 📄 2025-12-20_EXH-30_fcfcu_ac6eb2ea_2025-12-20_EX.jpg
> │        ├── 📄 2308ab1944a6bfa5c5b8.svg
> │        ├── 📄 293fd13dbca5a3e450ef.woff2
> │        ├── 📄 2CAA8E246CB3_1765294197.jpg
> │        ├── 📄 454577c22304619db035.ttf
> │        ├── 📄 52ac8f3034507f1d9e53.ttf
> │        ├── 📄 535a6cf662596b3bd6a6.woff2
> │        ├── 📄 70cc7ff27245e82ad414.ttf
> │        ├── 📄 72505e6a122c6acd5471.woff2
> │        ├── 📄 844d385a31ebae5141198646b19f5dcc3be5831afc2a2a6ecc737d880c2a07dd.jpg
> │        ├── 📄 94f2f163d4b698242fef.otf
> │        ├── 📄 DL_REDACTED.jpg
> │        ├── 📄 FrontImage-2024-07-12.png
> │        ├── 📄 IMG_1833.PNG
> │        ├── 📄 IMG_1837.JPG
> │        ├── 📄 IMG_1864.HEIC
> │        ├── 📄 favicon.png
> │        ├── 📄 identity_verification_bank_statement_old-national.jpg
> │      └── 📂 sheets/
> │        ├── 📄 QiCase-FCFCU_Financial_Tracker.xlsx
> │        ├── 📄 authority.csv
> │        ├── 📄 strategy.csv
> │      └── 📂 txt/
> │        ├── 📄 01092026_C_DOC_D0465.txt
> │        ├── 📄 13312381_C_DOC_D0001.txt
> │        ├── 📄 13312381_C_DOC_D0461.txt
> │        ├── 📄 13312381_C_DOC_D0533.txt
> │        ├── 📄 13312462_C_DOC_D0002.txt
> │        ├── 📄 13312462_C_DOC_D0003.txt
> │        ├── 📄 13312462_C_DOC_D0004.txt
> │        ├── 📄 13312462_C_DOC_D0462.txt
> │        ├── 📄 13312465_C_DOC_D0005.txt
> │        ├── 📄 13312465_C_DOC_D0006.txt
> │        ├── 📄 17695436_C_DOC_D0103.txt
> │        ├── 📄 17701079_C_DOC_D0491.txt
> │        ├── 📄 20230920_C_DOC_D0074.txt
> │        ├── 📄 20240320_C_DOC_D0075.txt
> │        ├── 📄 20241209_C_DOC_D0071.txt
> │        ├── 📄 20241211_C_DOC_D0072.txt
> │        ├── 📄 20250116_C_DOC_D0018.txt
> │        ├── 📄 20250116_C_DOC_D0019.txt
> │        ├── 📄 20250116_C_DOC_D0020.txt
> │        ├── 📄 20250116_C_DOC_D0021.txt
> │        ├── 📄 20250116_C_DOC_D0022.txt
> │        ├── 📄 20250116_C_DOC_D0023.txt
> │        ├── 📄 20250116_C_DOC_D0024.txt
> │        ├── 📄 20250116_C_DOC_D0025.txt
> │        ├── 📄 20250305_C_DOC_D0028.txt
> │        ├── 📄 20250415_C_DOC_D0029.txt
> │        ├── 📄 20250513_C_DOC_D0030.txt
> │        ├── 📄 20250513_C_DOC_D0031.txt
> │        ├── 📄 20250513_C_DOC_D0032.txt
> │        ├── 📄 20250521_C_DOC_D0033.txt
> │        ├── 📄 20250521_C_DOC_D0034.txt
> │        ├── 📄 20250521_C_DOC_D0035.txt
> │        ├── 📄 20250523_C_DOC_D0036.txt
> │        ├── 📄 20250523_C_DOC_D0037.txt
> │        ├── 📄 20250530_C_DOC_D0039.txt
> │        ├── 📄 20250530_C_DOC_D0040.txt
> │        ├── 📄 20250608_C_DOC_D0102.txt
> │        ├── 📄 20250709_C_DOC_D0041.txt
> │        ├── 📄 20250717_C_DOC_D0042.txt
> │        ├── 📄 20250909_C_DOC_D0043.txt
> │        ├── 📄 20251029_C_DOC_D0017.txt
> │        ├── 📄 20251029_C_DOC_D0045.txt
> │        ├── 📄 20251210_C_DOC_D0047.txt
> │        ├── 📄 20251210_C_DOC_D0048.txt
> │        ├── 📄 20251210_C_DOC_D0049.txt
> │        ├── 📄 20251210_C_DOC_D0051.txt
> │        ├── 📄 20251210_C_DOC_D0052.txt
> │        ├── 📄 20251211_C_DOC_D0053.txt
> │        ├── 📄 20251211_C_DOC_D0054.txt
> │        ├── 📄 20251211_C_DOC_D0055.txt
> │        ├── 📄 20251211_C_DOC_D0056.txt
> │        ├── 📄 20251211_C_DOC_D0058.txt
> │        ├── 📄 20251212_C_DOC_D0059.txt
> │        ├── 📄 20251212_C_DOC_D0060.txt
> │        ├── 📄 20251216_C_DOC_D0061.txt
> │        ├── 📄 20251217_C_DOC_D0062.txt
> │        ├── 📄 20251221_C_DOC_D0068.txt
> │        ├── 📄 20251222_C_DOC_D0063.txt
> │        ├── 📄 20251222_C_DOC_D0064.txt
> │        ├── 📄 20251222_C_DOC_D0451.txt
> │        ├── 📄 20260101_C_DOC_D0070.txt
> │        ├── 📄 20260101_C_DOC_D0073.txt
> │        ├── 📄 20260101_C_DOC_D0448.txt
> │        ├── 📄 20260101_C_DOC_D0450.txt
> │        ├── 📄 20260108_C_DOC_D0474.txt
> │        ├── 📄 20260115_C_DOC_D0505.txt
> │        ├── 📄 20260115_C_DOC_D0506.txt
> │        ├── 📄 20260115_C_DOC_D0507.txt
> │        ├── 📄 20260115_C_DOC_D0508.txt
> │        ├── 📄 20260115_C_DOC_D0511.txt
> │        ├── 📄 20260115_C_DOC_D0512.txt
> │        ├── 📄 20260115_C_DOC_D0513.txt
> │        ├── 📄 20260118_C_DOC_D0475.txt
> │        ├── 📄 20260118_C_DOC_D0478.txt
> │        ├── 📄 20260118_C_DOC_D0482.txt
> │        ├── 📄 20260120_C_DOC_D0066.txt
> │        ├── 📄 20260124_C_DOC_D0488.txt
> │        ├── 📄 20260131_C_DOC_D0517.txt
> │        ├── 📄 20260131_C_DOC_D0518.txt
> │        ├── 📄 20260201_C_DOC_D0514.txt
> │        ├── 📄 20260201_C_DOC_D0524.txt
> │        ├── 📄 20260203_C_DOC_D0081.txt
> │        ├── 📄 20260203_C_DOC_D0092.txt
> │        ├── 📄 20260203_C_DOC_D0093.txt
> │        ├── 📄 20260203_C_DOC_D0096.txt
> │        ├── 📄 20260203_C_DOC_D0097.txt
> │        ├── 📄 20260203_C_DOC_D0099.txt
> │        ├── 📄 20260203_C_DOC_D0100.txt
> │        ├── 📄 20260203_C_DOC_D0441.txt
> │        ├── 📄 20260203_C_DOC_D0442.txt
> │        ├── 📄 20260203_C_DOC_D0443.txt
> │        ├── 📄 20260203_C_DOC_D0444.txt
> │        ├── 📄 20260203_C_DOC_D0445.txt
> │        ├── 📄 20260203_C_DOC_D0446.txt
> │        ├── 📄 20260203_C_DOC_D0447.txt
> │        ├── 📄 20260203_C_DOC_D0449.txt
> │        ├── 📄 20260203_C_DOC_D0455.txt
> │        ├── 📄 20260203_C_DOC_D0456.txt
> │        ├── 📄 20260203_C_DOC_D0457.txt
> │        ├── 📄 20260203_C_DOC_D0458.txt
> │        ├── 📄 20260203_C_DOC_D0459.txt
> │        ├── 📄 20260203_C_DOC_D0460.txt
> │        ├── 📄 20260203_C_DOC_D0476.txt
> │        ├── 📄 20260203_C_DOC_D0483.txt
> │        ├── 📄 20260203_C_DOC_D0486.txt
> │        ├── 📄 20260203_C_DOC_D0492.txt
> │        ├── 📄 20260203_C_DOC_D0493.txt
> │        ├── 📄 20260203_C_DOC_D0498.txt
> │        ├── 📄 20260203_C_DOC_D0499.txt
> │        ├── 📄 20260203_C_DOC_D0500.txt
> │        ├── 📄 20260203_C_DOC_D0501.txt
> │        ├── 📄 20260203_C_DOC_D0519.txt
> │        ├── 📄 20260203_C_DOC_D0520.txt
> │        ├── 📄 20260203_C_DOC_D0521.txt
> │        ├── 📄 20260203_C_DOC_D0522.txt
> │        ├── 📄 20260203_C_DOC_D0523.txt
> │        ├── 📄 20260203_C_DOC_D0531.txt
> │        ├── 📄 20260203_C_DOC_D0535.txt
> │        ├── 📄 20260203_C_DOC_D0537.txt
> │        ├── 📄 20260203_C_DOC_D0538.txt
> │        ├── 📄 20260203_C_DOC_D0539.txt
> │        ├── 📄 20260203_C_DOC_D0543.txt
> │        ├── 📄 20260203_C_DOC_D0544.txt
> │        ├── 📄 20260203_C_DOC_D0545.txt
> │        ├── 📄 20260203_C_DOC_D0549.txt
> │        ├── 📄 20260203_C_DOC_D0550.txt
> │        ├── 📄 20260203_C_DOC_D0551.txt
> │        ├── 📄 20260203_C_DOC_D0552.txt
> │        ├── 📄 20260203_C_DOC_D0556.txt
> │        ├── 📄 20260203_C_DOC_D0557.txt
> │        ├── 📄 20260207_C_DOC_D0464.txt
> │        ├── 📄 20260207_C_DOC_D0467.txt
> │        ├── 📄 20260207_C_DOC_D0468.txt
> │        ├── 📄 20260207_C_DOC_D0470.txt
> │        ├── 📄 20260207_C_DOC_D0471.txt
> │        ├── 📄 20260207_C_DOC_D0472.txt
> │        ├── 📄 20260207_C_DOC_D0479.txt
> │        ├── 📄 20260207_C_DOC_D0485.txt
> │        ├── 📄 20260207_C_DOC_D0495.txt
> │        ├── 📄 37288599_C_DOC_D0510.txt
> │        ├── 📄 60185613_C_DOC_D0480.txt
> │        ├── 📄 FCFCU_Late_Reporting_Evidence_2026.txt
> │        ├── 📄 FINANCIAL CENTER 01012017-02122026.txt
> │        ├── 📄 audit_report.txt
> │        ├── 📄 output.txt
> │      └── 📂 video/
> │        ├── 📄 00-06-23_2a.mkv
> │        ├── 📄 00-16-23_2a.mkv
> │        ├── 📄 00-26-23_2a.mkv
> │        ├── 📄 00-36-23_2a.mkv
> │        ├── 📄 00-46-23_2a.mkv
> │        ├── 📄 00-56-23_2a.mkv
> │        ├── 📄 01-06-23_2a.mkv
> │        ├── 📄 01-16-23_2a.mkv
> │        ├── 📄 01-26-22_2a.mkv
> │        ├── 📄 01-36-22_2a.mkv
> │        ├── 📄 01-46-22_2a.mkv
> │        ├── 📄 01-56-22_2a.mkv
> │        ├── 📄 02-06-22_2a.mkv
> │        ├── 📄 02-16-22_2a.mkv
> │        ├── 📄 02-26-22_2a.mkv
> │        ├── 📄 02-36-22_2a.mkv
> │        ├── 📄 02-46-22_2a.mkv
> │        ├── 📄 02-56-21_2a.mkv
> │        ├── 📄 03-06-21_2a.mkv
> │        ├── 📄 03-16-21_2a.mkv
> │        ├── 📄 03-26-21_2a.mkv
> │        ├── 📄 03-36-21_2a.mkv
> │        ├── 📄 03-46-21_2a.mkv
> │        ├── 📄 03-56-21_2a.mkv
> │        ├── 📄 04-06-21_2a.mkv
> │        ├── 📄 04-16-21_2a.mkv
> │        ├── 📄 04-26-21_2a.mkv
> │        ├── 📄 04-36-21_2a.mkv
> │        ├── 📄 04-46-20_2a.mkv
> │        ├── 📄 04-56-20_2a.mkv
> │        ├── 📄 05-06-20_2a.mkv
> │        ├── 📄 05-16-20_2a.mkv
> │        ├── 📄 05-26-20_2a.mkv
> │        ├── 📄 05-36-20_2a.mkv
> │        ├── 📄 05-46-20_2a.mkv
> │        ├── 📄 05-56-20_2a.mkv
> │        ├── 📄 06-06-20_2a.mkv
> │        ├── 📄 06-16-20_2a.mkv
> │        ├── 📄 06-26-20_2a.mkv
> │        ├── 📄 06-36-19_2a.mkv
> │        ├── 📄 06-46-19_2a.mkv
> │        ├── 📄 06-56-19_2a.mkv
> │        ├── 📄 07-06-19_2a.mkv
> │        ├── 📄 07-16-19_2a.mkv
> │        ├── 📄 07-26-19_2a.mkv
> │        ├── 📄 07-36-19_2a.mkv
> │        ├── 📄 07-46-19_2a.mkv
> │        ├── 📄 07-56-19_2a.mkv
> │        ├── 📄 08-06-19_2a.mkv
> │        ├── 📄 08-16-18_2a.mkv
> │        ├── 📄 08-26-18_2a.mkv
> │        ├── 📄 08-36-18_2a.mkv
> │        ├── 📄 08-46-18_2a.mkv
> │        ├── 📄 08-56-18_2a.mkv
> │        ├── 📄 09-06-18_2a.mkv
> │        ├── 📄 09-16-18_2a.mkv
> │        ├── 📄 09-26-18_2a.mkv
> │        ├── 📄 09-36-18_2a.mkv
> │        ├── 📄 09-46-18_2a.mkv
> │        ├── 📄 09-56-18_2a.mkv
> │        ├── 📄 10-06-17_2a.mkv
> │        ├── 📄 10-16-17_2a.mkv
> │        ├── 📄 10-26-17_2a.mkv
> │        ├── 📄 10-36-17_2a.mkv
> │        ├── 📄 10-46-17_2a.mkv
> │        ├── 📄 10-56-17_2a.mkv
> │        ├── 📄 2CAA8E1B675120251209103140_album_local_cache.mp4
> │        ├── 📄 2CAA8E246CB320251209103011_album_local_cache.mp4
> │        ├── 📄 2d5198822ab091ce4305.woff2
> │        ├── 📄 4bb6ac751d1c5478ff3a.woff2
> │        ├── 📄 Missing_Evidence_and_Vanishing_Foreclosure_Surplus.m4a
> │        ├── 📄 Recording.m4a
> │        ├── 📄 integrate_disability_separate_appeals_get_stay.m4a
> │        ├── 📄 voicemail-14956B1E-5384-4F00-9AB1-C87D98D7C6E1.m4a
> │    └── 📂 E-01_PHOTOS/
> │      ├── 📄 20240624_C02_PHOTO_D0076.jpg
> │      ├── 📄 20251203_C02_PHOTO_D0247.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0108.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0109.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0110.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0111.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0113.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0114.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0155.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0156.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0157.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0158.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0159.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0160.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0161.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0162.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0163.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0164.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0165.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0166.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0167.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0168.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0169.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0170.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0171.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0172.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0173.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0174.png
> │      ├── 📄 20251209_C02_PHOTO_D0175.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0176.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0177.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0178.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0179.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0180.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0181.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0182.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0183.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0184.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0185.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0186.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0188.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0189.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0190.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0191.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0192.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0193.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0194.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0195.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0196.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0197.png
> │      ├── 📄 20251209_C02_PHOTO_D0198.png
> │      ├── 📄 20251209_C02_PHOTO_D0199.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0200.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0201.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0202.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0203.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0204.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0205.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0206.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0207.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0208.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0209.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0210.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0211.jpg
> │      ├── 📄 20251209_C02_PHOTO_D0212.jpg
> │      ├── 📄 20251209_PHOTO_Auto_Save_D0107.heic
> │      ├── 📄 20251209_PHOTO_Auto_Save_D0112.heic
> │      ├── 📄 20251220_C02_PHOTO_D0077.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0078.png
> │      ├── 📄 20251220_C02_PHOTO_D0214.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0215.png
> │      ├── 📄 20251220_C02_PHOTO_D0216.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0217.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0218.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0219.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0220.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0221.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0222.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0223.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0225.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0226.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0227.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0228.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0229.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0230.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0231.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0233.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0234.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0235.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0236.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0237.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0238.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0239.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0240.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0241.png
> │      ├── 📄 20251220_C02_PHOTO_D0242.png
> │      ├── 📄 20251220_C02_PHOTO_D0243.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0244.jpg
> │      ├── 📄 20251220_C02_PHOTO_D0454.jpg
> │      ├── 📄 20251220_PHOTO_Auto_Save_D0132.heic
> │      ├── 📄 20251220_PHOTO_Auto_Save_D0133.heic
> │      ├── 📄 20260118_C02_PHOTO_D0246.jpeg
> │      ├── 📄 20260118_C02_PHOTO_D0473.jpeg
> │      ├── 📄 20260207_C02_PHOTO_D0213.jpg
> │      ├── 📄 20260207_C02_PHOTO_D0224.jpg
> │      ├── 📄 20260207_C02_PHOTO_D0245.jpg
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0144.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0145.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0146.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0147.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0148.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0149.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0150.heic
> │      ├── 📄 20260207_PHOTO_Auto_Save_D0151.heic
> │      ├── 📄 20260208_PHOTO_Evidence_IMG_2905.PNG
> │      ├── 📄 20260208_PHOTO_Evidence_IMG_2906.PNG
> │      ├── 📄 20260208_PHOTO_Evidence_IMG_2908.PNG
> │      ├── 📄 20260208_PHOTO_Evidence_IMG_2911.PNG
> │      ├── 📄 20260208_PHOTO_Evidence_IMG_2913.PNG
> │      ├── 📄 20260208_PHOTO_Evidence_IMG_2914.PNG
> │      ├── 📄 20261125_220020_C02_PHOTO_D0248.png
> │      ├── 📄 _01_PHOTOS.md
> │    └── 📂 E-02_VIDEO/
> │      ├── 📄 20251126_C02_VIDEO_D0440.mp4
> │      ├── 📄 20251203_C02_VIDEO_D0439.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0104.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0105.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0106.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0249.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0250.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0251.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0252.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0253.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0254.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0255.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0256.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0257.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0258.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0259.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0260.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0261.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0262.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0263.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0264.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0265.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0266.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0267.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0268.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0269.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0270.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0271.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0272.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0273.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0274.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0275.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0276.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0277.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0278.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0279.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0280.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0281.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0282.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0283.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0284.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0285.mp4
> │      ├── 📄 20251209_C02_VIDEO_D0286.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0115.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0116.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0117.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0118.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0119.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0120.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0121.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0122.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0123.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0124.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0125.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0126.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0127.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0128.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0129.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0130.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0131.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0287.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0288.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0289.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0290.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0291.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0292.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0293.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0294.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0295.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0296.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0297.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0298.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0299.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0300.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0301.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0302.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0303.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0304.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0305.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0306.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0307.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0308.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0309.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0310.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0311.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0312.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0313.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0314.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0315.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0316.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0317.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0318.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0319.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0320.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0321.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0322.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0323.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0324.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0325.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0326.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0327.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0328.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0329.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0330.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0331.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0332.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0333.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0334.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0335.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0336.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0337.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0338.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0339.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0340.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0341.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0342.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0343.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0344.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0345.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0346.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0347.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0348.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0349.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0350.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0351.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0352.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0353.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0354.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0355.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0356.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0357.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0358.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0359.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0360.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0361.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0362.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0363.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0364.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0365.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0366.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0367.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0368.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0369.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0370.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0371.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0372.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0373.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0374.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0375.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0376.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0377.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0378.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0379.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0380.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0381.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0382.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0383.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0384.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0385.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0386.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0387.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0388.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0389.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0390.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0391.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0392.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0393.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0394.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0395.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0396.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0397.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0398.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0399.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0400.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0401.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0402.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0403.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0404.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0405.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0406.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0407.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0408.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0409.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0410.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0411.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0412.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0413.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0414.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0415.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0416.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0417.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0418.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0419.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0420.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0421.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0422.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0423.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0424.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0425.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0426.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0427.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0428.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0429.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0430.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0431.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0432.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0433.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0434.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0435.mp4
> │      ├── 📄 20251217_C02_VIDEO_D0436.mp4
> │      ├── 📄 20251220_C02_VIDEO_D0437.mp4
> │      ├── 📄 20251220_C02_VIDEO_D0438.mp4
> │      ├── 📄 20260209_C02_Screen_Recording_hearing_jan_09_2026.mp4
> │      ├── 📄 C00_Hearing_Transcript_Recording_20260209_174803.mp4
> │      ├── 📄 Photo_Video_DB.csv
> │      ├── 📄 Photo_Video_DB_2ddf84a04402819ea365d894c16a3fdf_all.csv
> │      ├── 📄 _02_VIDEO (2).md
> │      ├── 📄 _02_VIDEO (3).md
> │      ├── 📄 _02_VIDEO.md
> │    └── 📂 E-03_DOCUMENTS/
> │      └── 📂 01_FILED/
> │        ├── 📄 20260115_C01_FORECL_FCFCU_MOTION_D0511.pdf
> │        ├── 📄 _01_FILED.md
> │      └── 📂 02_ORDERS/
> │        ├── 📄 20260118_C01_FORECL_FCFCU_MOTION_D0482.pdf
> │        ├── 📄 _02_ORDERS.md
> │      └── 📂 04_CORRESPONDENCE/
> │        ├── 📄 20260101_C01_FORECL_FCFCU_DOC_D0073.pdf
> │        ├── 📄 20260207_C01_FORECL_FCFCU_MOTION_D0510.pdf
> │        ├── 📄 _04_CORRESPONDENCE.md
> │      ├── 📄 20241209_C02_FCFCU_VIDEO_D0071.pdf
> │      ├── 📄 20241211_C02_FCFCU_VIDEO_D0072.pdf
> │      ├── 📄 20260101_C00_FCFCU_DOC_D0448.pdf
> │      ├── 📄 20260101_C00_FCFCU_DOC_D0450.pdf
> │      ├── 📄 20260108_C00_AES_DOC_D0474.pdf
> │      ├── 📄 20260118_C03_FCRA_COMPLAINT_D0478.pdf
> │      ├── 📄 20260118_C03_FCRA_EXPRN_ORDER_D0475.pdf
> │      ├── 📄 20260121_FILE_Auto_Save_D0477.pptx
> │      ├── 📄 20260131_C03_FCRA_FCFCU_DISP_D0518.pdf
> │      ├── 📄 20260131_C06_ADA_FCFCU_INV_D0517.pdf
> │      ├── 📄 20260201_C00_ORDER_D0524.pdf
> │      ├── 📄 20260201_C06_ADA_VIDEO_D0514.pdf
> │      ├── 📄 20260202_CAPTURE_Auto_Save_D0525.html
> │      ├── 📄 20260202_CAPTURE_Auto_Save_D0526.html
> │      ├── 📄 20260202_CAPTURE_Auto_Save_D0528.html
> │      ├── 📄 20260202_CAPTURE_Auto_Save_D0534.html
> │      ├── 📄 20260202_CAPTURE_Auto_Save_D0536.html
> │      ├── 📄 20260202_CAPTURE_Auto_Save_D0540.html
> │      ├── 📄 20260202_CAPTURE_Auto_Save_D0558.html
> │      ├── 📄 20260202_CAPTURE_Auto_Save_D0559.html
> │      ├── 📄 20260202_CAPTURE_Auto_Save_D0560.html
> │      ├── 📄 20260202_CAPTURE_Auto_Save_D0563.html
> │      ├── 📄 20260202_CAPTURE_Auto_Save_D0564.html
> │      ├── 📄 20260203_C00_AES_DOC_D0460.pdf
> │      ├── 📄 20260203_C00_DOC_D0441.pdf
> │      ├── 📄 20260203_C00_DOC_D0458.pdf
> │      ├── 📄 20260203_C00_DOC_D0476.pdf
> │      ├── 📄 20260203_C00_FCFCU_DOC_D0442.pdf
> │      ├── 📄 20260203_C00_FCFCU_DOC_D0443.pdf
> │      ├── 📄 20260203_C00_FCFCU_DOC_D0444.pdf
> │      ├── 📄 20260203_C00_FCFCU_DOC_D0446.pdf
> │      ├── 📄 20260203_C00_FCFCU_DOC_D0447.pdf
> │      ├── 📄 20260203_C00_FCFCU_DOC_D0449.pdf
> │      ├── 📄 20260203_C00_INV_D0445.pdf
> │      ├── 📄 20260203_C00_ORDER_D0552.pdf
> │      ├── 📄 20260203_C03_EQFX_DOC_D0535.pdf
> │      ├── 📄 20260203_C03_FCRA_DISP_D0457.pdf
> │      ├── 📄 20260203_C03_FCRA_EQFX_DISP_D0483.pdf
> │      ├── 📄 20260203_C03_FCRA_EQFX_DISP_D0493.pdf
> │      ├── 📄 20260203_C03_FCRA_EQFX_JUDGM_D0531.pdf
> │      ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0455.pdf
> │      ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0456.pdf
> │      ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0459.pdf
> │      ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0537.pdf
> │      ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0538.pdf
> │      ├── 📄 20260203_C03_FCRA_EXPRN_DISP_D0539.pdf
> │      ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0519.pdf
> │      ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0520.pdf
> │      ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0543.pdf
> │      ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0544.pdf
> │      ├── 📄 20260203_C03_FCRA_FCFCU_DISP_D0545.pdf
> │      ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0486.pdf
> │      ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0498.pdf
> │      ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0500.pdf
> │      ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0501.pdf
> │      ├── 📄 20260203_C03_FCRA_TRNUN_DISP_D0541.pdf
> │      ├── 📄 20260203_C03_FCRA_TRNUN_ORDER_D0499.pdf
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0469.mhtml
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0515.html
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0527.html
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0532.html
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0542.html
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0546.html
> │      ├── 📄 20260203_CAPTURE_Auto_Save_D0547.html
> │      ├── 📄 20260203_EMAIL_Auto_Save_D0497.eml
> │      ├── 📄 20260207_C00_DOC_D0464.pdf
> │      ├── 📄 20260207_C03_FCRA_EQFX_DISP_D0480.pdf
> │      ├── 📄 20260207_C03_FCRA_EQFX_DISP_D0533.pdf
> │      ├── 📄 20260207_C03_FCRA_EQFX_JUDGM_D0003.pdf
> │      ├── 📄 20260207_C03_FCRA_EQFX_JUDGM_D0004.pdf
> │      ├── 📄 20260207_C03_FCRA_EQFX_JUDGM_D0529.pdf
> │      ├── 📄 20260207_C03_FCRA_FCFCU_JUDGM_D0006.pdf
> │      ├── 📄 20260207_C03_FCRA_FCFCU_JUDGM_D0530.pdf
> │      ├── 📄 20260207_C03_FCRA_TRNUN_DISP_D0467.pdf
> │      ├── 📄 20260207_C03_FCRA_TRNUN_DISP_D0485.pdf
> │      ├── 📄 20260207_C03_FCRA_TRNUN_DOC_D0468.pdf
> │      ├── 📄 20260207_C03_FCRA_TRNUN_DOC_D0470.pdf
> │      ├── 📄 20260207_C03_FCRA_TRNUN_DOC_D0471.pdf
> │      ├── 📄 20260207_C03_FCRA_TRNUN_VIDEO_D0472.pdf
> │      ├── 📄 20260207_C03_TRNUN_COMPLAINT_D0479.pdf
> │      ├── 📄 20260207_FILE_Auto_Save_D0014.mw
> │      ├── 📄 20260208_REPORT_Credit_Analysis_WalletHub.pdf
> │      ├── 📄 20260208_REPORT_WalletHub_Credit_Analysis.pdf
> │      ├── 📄 20260209_LEGAL_Appellate_Document.docx
> │      ├── 📄 20260209_LEGAL_Appellate_Document.pdf
> │      ├── 📄 20260209_NOTICE_Direct_Dispute_Deletion_Demand.pdf
> │      ├── 📄 20260209_REPORT_CapOne_Credit_Ricevelasquez_A.pdf
> │      ├── 📄 20260209_REPORT_CapOne_Credit_Ricevelasquez_B.pdf
> │      ├── 📄 20260209_REPORT_CapOne_Credit_Ricevelasquez_James.pdf
> │      ├── 📄 20260209_REPORT_Credit_Report.pdf
> │      ├── 📄 20260209_TEMPLATE_Case_Document.pdf
> │      ├── 📄 20260209_TEMPLATE_Case_Document_Backup.pdf
> │      ├── 📄 20260210_NOTICE_Notice_of_Appeal_FILED.pdf
> │      ├── 📄 20260210_NOTICE_Notice_of_Appeal_FILED.png
> │      ├── 📄 20260210_REPORT_ShadowPointe_Client.pdf
> │      ├── 📄 Comparable_Market_Analysis_4817_Shadow_Pointe_Dr.html
> │      ├── 📄 FCFCU_NOTICE_Direct_Dispute_Deletion_Demand.pdf
> │      ├── 📄 POST_INCIDENT_CONDITION_SUMMARY.md
> │    └── 📂 E-04_FINANCIAL/
> │      ├── 📄 20250719_INV_Zoho_Corp_50100846854.pdf
> │      ├── 📄 20250729_INV_Zoho_Corp_50100879809.pdf
> │      ├── 📄 20250729_INV_Zoho_Corp_50100883027.pdf
> │      ├── 📄 20250807_INV_Zoho_Corp_50100916138.pdf
> │      ├── 📄 20251126_NOTICE_AES_Disconnect.pdf
> │      ├── 📄 20260115_INV_Tello_Mobile_82016155.pdf
> │      ├── 📄 20260115_INV_Tello_Mobile_82016231.pdf
> │      ├── 📄 20260115_INV_Tello_Mobile_82016359.pdf
> │      ├── 📄 20260115_INV_Tello_Mobile_82016391.pdf
> │      ├── 📄 20260115_INV_Zoho_Corp_50101514115.pdf
> │      ├── 📄 20260202_INV_Invoice_Generic_1.pdf
> │      ├── 📄 20260202_INV_Invoice_Generic_2.pdf
> │      ├── 📄 20260202_INV_Invoice_Generic_3.pdf
> │      ├── 📄 20260202_INV_Invoice_Generic_4.pdf
> │      ├── 📄 20260202_INV_Zoho_Corp_50100846854.pdf
> │      ├── 📄 20260202_INV_Zoho_Corp_50100879809.pdf
> │      ├── 📄 20260202_INV_Zoho_Corp_50100883027.pdf
> │      ├── 📄 20260202_INV_Zoho_Corp_50100916138.pdf
> │      ├── 📄 20260203_C00_LSTRM_INV_D0492.pdf
> │      ├── 📄 20260203_C00_LSTRM_INV_D0521.pdf
> │      ├── 📄 20260203_C00_LSTRM_INV_D0522.pdf
> │      ├── 📄 20260203_C00_LSTRM_INV_D0523.pdf
> │      ├── 📄 20260203_INV_Invoice_Generic_1.pdf
> │      ├── 📄 20260205_INV_RecordXchange_4_018222.pdf
> │      ├── 📄 20260207_C02_PHOTO_D0466.jpg
> │      ├── 📄 20260207_C03_FCRA_EQFX_INV_D0001.pdf
> │      ├── 📄 20260207_C03_FCRA_EQFX_INV_D0461.pdf
> │      ├── 📄 20260207_C03_FCRA_LSTRM_INV_D0002.pdf
> │      ├── 📄 20260207_C03_FCRA_LSTRM_INV_D0005.pdf
> │      ├── 📄 20260207_C03_FCRA_LSTRM_INV_D0462.pdf
> │      ├── 📄 20260207_C03_FCRA_LSTRM_INV_D0463.pdf
> │      ├── 📄 Financial.csv
> │      ├── 📄 Financial_2cef84a044028021905ff6d8938abe93_all.csv
> │      ├── 📄 Financial_Tracker.md
> │      ├── 📄 Food_Purchase.md
> │      ├── 📄 Gas_For_Lyft.md
> │      ├── 📄 Gas_Purchase_For_Lyft.md
> │      ├── 📄 Pet_Needs.md
> │    ├── 📄 FCFCU_CASE_MASTER - 0_docket.csv
> │  ├── 📄 README.md
> │  └── 📂 audits/
> │    └── 📂 20260212_FCFCU_Accounting_Audit_Report/
> │      └── 📂 02_Source_Documents/
> │        ├── 📄 _02_Source_Documents.md
> │      ├── 📄 NT_Forensic_Accounting_Audit_Summary.md
> │    ├── 📄 _audits.md
> │    └── 📂 fcfcu_gsheets/
> │      ├── 📄 FCFCU_CASE_MASTER.gsheet
> │      ├── 📄 _fcfcu_gsheets.md
> │  ├── 📄 index.md
> │  └── 📂 tools/
> │    ├── 📄 Efileincourts.gov.md
> │    ├── 📄 _tools.md
> │    ├── 📄 compiled_task_spine.csv
> │    ├── 📄 run_pipeline.md
> │    ├── 📄 schema_task_spine.md
> │    └── 📂 scripts/
> └── 📄 package-lock.json
> ```

### Assistant
> Yes. Confirmed.
> 
> Based on your current repo structure under `content/01_PHASES/`, the **7 active strategic phases** we landed on are:
> 
> ---
> 
> ### **C-00 — Foreclosure Record (Foundation / Audit Layer)**
> Purpose: Master record integrity, sequencing, appellate preservation.  
> This is your structural base — not a claim, but the forensic control layer.
> 
> ---
> 
> ### **C-01 — Service & Notice Defects**
> Core thesis: Lack of proper service → void judgment.  
> This is your jurisdictional kill shot (Trial Rule 4.1(B), notice failures, publication gaps, 48-hour issues).
> 
> ---
> 
> ### **C-02 — Evidence Preservation**
> Litigation hold, spoliation risk, chain of custody, intake log.  
> Protects your leverage and sanctions posture.
> 
> ---
> 
> ### **C-03 — Financial Misconduct**
> Surplus accounting, fee inflation, FCRA exposure, regulator escalation.  
> This is the money + credibility destruction phase.
> 
> ---
> 
> ### **C-04 — Writ / Removal Conduct**
> Execution irregularities, armed removal, property interference, §1983 mapping.  
> This is the wrongful dispossession layer.
> 
> ---
> 
> ### **C-05 — Civil Rights**
> ADA accommodation record, access to court impact, DOJ/HUD/ICRC filings.  
> This reframes the case from foreclosure → civil rights deprivation.
> 
> ---
> 
> ### **C-06 — Settlement & Narrative Control**
> Demand modeling, regulator pressure synchronization, messaging discipline.  
> This controls leverage and endgame positioning.
> 
> ---
> 
> ## Structural Confirmation
> 
> You do **not** have 8.  
> You do **not** have 5.  
> You have:
> 
> > 1 audit base + 6 strategic enforcement phases = 7 total.
> 
> C-00 is foundational.  
> C-01 through C-06 are execution phases.
> 
> That matches:
> - Your folder tree  
> - Your CSV master structure  
> - Your regulator packet builds  
> - Your damages ledger architecture  
> 
> If you want, I can now:
> 
> - Map each phase to a `P_XXXX` schema ID block for `PHASE_MASTER`
> - Or confirm which ones are `ACTIVE` vs `SUPPORTING` based on current posture.
> 
> Where do you want to tighten next?

### User
> map the schema please so we can make sure we are aligned moving forward adn we can lock this and then implement logging moving forward.

### Assistant
> Here’s the **locked schema map** I recommend for your case system so we stop “re-inventing the spreadsheet” every week and can start **logging forward cleanly**.
> 
> This is designed to support: **Phases → Lanes → Tasks → Docs/Artifacts → Events → Assertions/Violations → Filings/Exhibits**, with traceability in both directions.
> 
> ---
> 
> ## 0) Core design rules (lock these)
> 
> 1. **Everything is an object with an ID** (phase, lane, task, doc, event, filing, exhibit, claim).
> 2. **Events are facts** (date/time, what happened, who, where).  
>    **Docs are artifacts** (pdf, screenshot, letter, filing).  
>    **Tasks are actions** (do something, produce something).
> 3. **Traceability is mandatory**:
>    - Task ↔ supports/creates Docs
>    - Doc ↔ references Events
>    - Event ↔ supports Claims/Violations
>    - Filing ↔ bundles Docs as Exhibits
> 4. **No orphan docs**: every doc must link to at least one Event *or* one Task (ideally both).
> 
> ---
> 
> ## 1) Entity map (tables) + relationships
> 
> ### A) `phase`
> Top-level strategy buckets (your C-01, C-02, etc.)
> 
> **Fields**
> - `phase_id` (PK) — e.g., `C-01`
> - `phase_name`
> - `status` — Active / Planned / Parked / Closed
> - `core_theory`
> - `primary_objective`
> - `notes`
> 
> **Relationships**
> - phase 1 → many lanes
> - phase 1 → many tasks (optionally direct if you skip lanes)
> 
> ---
> 
> ### B) `lane` (aka sub-phase / phase lane)
> A **structured slice** inside a phase: “Service Defects → Mailing”, “Writ → Unknown Occupants”, etc.
> 
> **Fields**
> - `lane_id` (PK) — e.g., `C-01.L02`
> - `phase_id` (FK)
> - `lane_name`
> - `status`
> - `lane_objective`
> - `notes`
> - `sort_order`
> 
> **Relationships**
> - lane 1 → many tasks
> - lane 1 → many claims/violations (optional but useful)
> 
> ---
> 
> ### C) `task`
> Actionable work items. This is what you actually *do*.
> 
> **Fields**
> - `task_id` (PK) — e.g., `T-0123`
> - `phase_id` (FK)
> - `lane_id` (FK, nullable but preferred)
> - `task_name`
> - `task_type` — Research / Draft / File / Request / Analyze / Outreach / Evidence-Hold
> - `status` — Not Started / In Progress / Blocked / Done
> - `priority` — P0/P1/P2
> - `owner` — Cody / Attorney / TBD
> - `due_date` (optional)
> - `next_action` (1 sentence)
> - `blocker` (optional)
> - `created_at`, `updated_at`
> 
> **Relationships**
> - task many ↔ many docs (via join table)
> - task many ↔ many events (via join table)
> - task may produce a filing
> 
> ---
> 
> ### D) `doc` (artifact registry)
> Every file, screenshot, email, letter, transcript, court PDF.
> 
> **Fields**
> - `doc_id` (PK) — e.g., `D-0456`
> - `doc_title` (human name)
> - `doc_type` — Court Filing / Order / Return of Service / Letter / Photo / Video / Transcript / Spreadsheet / Invoice
> - `source` — MyCase / Clerk / Plaintiff Counsel / Sheriff / USPS / CRA / CFPB / NCUA / Personal
> - `doc_date` — date on the document (not upload date)
> - `received_date` — when you got it
> - `file_name` — exact stored filename
> - `storage_path` — Drive path or repo path
> - `hash_sha256` (optional but ideal)
> - `confidentiality` — Public / Private / Sealed / PII
> - `summary` (2–5 lines)
> - `reliability` — Primary / Secondary / Hearsay / Unknown
> - `notes`
> 
> **Relationships**
> - doc many ↔ many events
> - doc many ↔ many tasks
> - doc may be an exhibit in a filing
> 
> ---
> 
> ### E) `event` (timeline facts)
> This is the backbone of your Markwhen timeline and “table of events”.
> 
> **Fields**
> - `event_id` (PK) — e.g., `E-2025-12-09-01`
> - `event_date_start`
> - `event_date_end` (nullable)
> - `event_title`
> - `event_category` — Service / Filing / Order / Writ / Eviction / Credit Reporting / Regulatory / Property Damage
> - `location` (optional)
> - `actors` — structured list or text
> - `narrative` — what happened, clean & factual
> - `impact_tags` — ADA / Due Process / Housing Harm / Property Harm / Credit Harm
> - `confidence` — High/Med/Low
> - `status` — Confirmed / Disputed / Alleged
> - `notes`
> 
> **Relationships**
> - event many ↔ many docs
> - event many ↔ many claims/violations
> - event many ↔ many tasks (things triggered by the event)
> 
> ---
> 
> ### F) `claim` (aka assertion / violation)
> This is where you encode the legal/strategic “why it matters”.
> 
> **Fields**
> - `claim_id` (PK) — e.g., `CL-0088`
> - `phase_id` (FK)
> - `lane_id` (FK, optional)
> - `claim_type` — Jurisdictional Defect / Service Defect / Abuse of Process / ADA / Tort / FCRA / Accounting
> - `legal_basis` — statute/rule/case cite (text)
> - `theory_statement` — one paragraph
> - `elements_checklist` — bullet-able text
> - `status` — Draft / Supported / Needs Evidence / Filed / Resolved
> - `notes`
> 
> **Relationships**
> - claim many ↔ many events
> - claim many ↔ many docs
> - claim may be argued in a filing
> 
> ---
> 
> ### G) `filing` (court + regulatory)
> A single submission (Notice of Appeal, Motion, CFPB complaint, NCUA complaint, CRA dispute).
> 
> **Fields**
> - `filing_id` (PK) — e.g., `F-2026-02-10-01`
> - `filing_channel` — Court / CFPB / NCUA / CRA / FCFCU Direct / AG / Other
> - `filing_title`
> - `filed_date`
> - `case_number` (nullable for regulators)
> - `status` — Draft / Filed / Served / Acknowledged / Responded / Closed
> - `method` — eFile / Mail / Portal / Email / Fax
> - `tracking` — certified mail / portal confirmation id
> - `notes`
> 
> **Relationships**
> - filing 1 → many exhibits (docs) via `exhibit`
> 
> ---
> 
> ### H) `exhibit` (filing bundle index)
> This is your “binder-ready” list.
> 
> **Fields**
> - `exhibit_id` (PK) — e.g., `EX-F-2026-02-10-01-07`
> - `filing_id` (FK)
> - `doc_id` (FK)
> - `exhibit_label` — Exhibit A / B / C…
> - `exhibit_title`
> - `page_range` (optional)
> - `notes`
> 
> ---
> 
> ## 2) Join tables (this is what makes it powerful)
> 
> ### `task_doc`
> - `task_id` (FK)
> - `doc_id` (FK)
> - `relation` — reads / produces / requests / references
> 
> ### `event_doc`
> - `event_id` (FK)
> - `doc_id` (FK)
> - `relation` — proves / mentions / contradicts / contextualizes
> 
> ### `event_claim`
> - `event_id` (FK)
> - `claim_id` (FK)
> - `support_level` — strong / medium / weak
> 
> ### `doc_claim`
> - `doc_id` (FK)
> - `claim_id` (FK)
> - `support_level`
> 
> ### `task_event`
> - `task_id` (FK)
> - `event_id` (FK)
> - `relation` — triggered_by / clarifies / responds_to
> 
> ---
> 
> ## 3) Minimal “logging forward” workflow (do this every time)
> 
> When anything happens (new email, new court entry, new CRA update):
> 
> 1. **Create/Update Event** (one row)
> 2. **Register Doc** (one row per file)
> 3. **Link Doc ↔ Event** (`event_doc`)
> 4. If it changes strategy: **link Event ↔ Claim** (`event_claim`)
> 5. If it requires action: **create Task** and link to Event/Doc
> 
> That’s it. No chaos.
> 
> ---
> 
> ## 4) Required ID conventions (lock)
> 
> - `phase_id`: `C-01` etc.
> - `lane_id`: `C-01.L01` (2-digit lane)
> - `task_id`: `T-0001` sequential
> - `doc_id`: `D-0001` sequential
> - `event_id`: `E-YYYY-MM-DD-##` (date + sequence)
> - `filing_id`: `F-YYYY-MM-DD-##`
> - `claim_id`: `CL-0001`
> - `exhibit_id`: derived from filing + sequence
> 
> If you stick to these, everything merges cleanly across Zoho, CSV, repo manifests, and binder outputs.
> 
> ---
> 
> ## 5) What “locked” means in practice
> 
> If you agree to this schema, then:
> - Every CSV export follows these exact column names.
> - Every import tool / script uses these keys.
> - Your Markwhen timeline can be generated from `event` (+ tags).
> - Your binder exhibit list can be generated from `filing/exhibit`.
> - Your “what’s left to do” dashboard comes from `task`.
> 
> ---
> 
> If you want, I’ll take your existing phase list (C-01..C-04 + whatever else you’ve been using) and output the **blank-but-structured** CSV headers for all tables above (plus the join tables) so Gemini can ingest without guessing column names.

### User
> also we are missing task for 01.03, 02.03, heres the full tree, we have some missing tasks and some rando stuff, tell me what to delete and what to add ```markdown
> . 📂 01_PHASES
> ├── 📄 1_phases-v2.csv
> ├── 📄 1_phases.csv
> └── 📂 C-00_Foreclosure_Record/
> │  └── 📂 00.01_Record_Integrity/
> │    ├── 📄 Filing timestamp audit.md
> │    ├── 📄 Master docket verification.md
> │    ├── 📄 Order sequence alignment.md
> │  └── 📂 00.02_Jurisdictional_Defects/
> │    ├── 📄 Service_Deficiency_Analysis.md
> │  └── 📂 00.03_Appellate_Preservation/
> │    ├── 📄 Appellate_Issue_Preservation.md
> │  ├── 📄 _PHASE_OVERVIEW.md
> └── 📂 C-01_Jurisdictional_Defects/
> │  └── 📂 01.01_Service_Compliance_Audit/
> │    ├── 📄 Secondary mailing failure analysis.md
> │    ├── 📄 Sheriff return review.md
> │  └── 📂 01.02_Notice_Failures/
> │    ├── 📄 48-hour notice absence documentation.md
> │    ├── 📄 Publication proof gap.md
> │  └── 📂 01.03_Legal_Impact_Assessment/
> │  ├── 📄 _PHASE_OVERVIEW.md
> └── 📂 C-02_Evidence_Preservation/
> │  └── 📂 02.01_Litigation_Hold_Control/
> │    ├── 📄 Dispatch preservation notices.md
> │  └── 📂 02.02_Spoliation_Risk_Register/
> │    ├── 📄 20_Spoliation_Risk_Ledger.md
> │  └── 📂 02.03_Evidence_Intake_Log/
> │  ├── 📄 _PHASE_OVERVIEW.md
> └── 📂 C-03_Post_Removal_Liability/
> │  └── 📂 03.01_Writ_Execution_Validity/
> │    ├── 📄 Writ predicate checklist.md
> │  └── 📂 03.02_Property_Interference/
> │    ├── 📄 Property interference log.md
> │  └── 📂 03.03_State_Action_Analysis/
> │    ├── 📄 1983 element mapping.md
> │    ├── 📄 MANIFEST_Sheriff_Oversight_Packet.md
> │    ├── 📄 Marion_County_Sheriff_Oversight_Violation_Excerpt.md
> │    ├── 📄 Sheriff_Internal_Affairs_Complaint.md
> │    ├── 📄 Sheriff_Violation_Excerpt.md
> │    ├── 📄 _35_Sheriff_Oversight.md
> │  ├── 📄 _20_AG_Indiana.md
> │  ├── 📄 _20_Habitability.md
> │  ├── 📄 _45_FCC_Telecom.md
> │  ├── 📄 _PHASE_OVERVIEW.md
> └── 📂 C-04_FCRA_Financial_Misconduct/
> │  └── 📂 04.01_Furnisher_Liability_Mapping/
> │    ├── 📄 2️⃣ FCRA STATUTORY DAMAGES MODEL.md
> │    ├── 📄 30_Full_TriMerge_2025_12_tradelines.csv
> │    ├── 📄 Core_Credit_Tables.md
> │    ├── 📄 Duplicate tradeline documentation.md
> │    ├── 📄 _20_furnisher_disputes.md
> │    ├── 📄 _CREDIT_FCRA_MASTER.md
> │  └── 📂 04.02_Bureau_Dispute_Tracking/
> │    ├── 📄 30_Full_TriMerge_2025_12_tradelines.csv
> │    ├── 📄 3️⃣ REGULATOR-READY COMPLAINT PACKET.md
> │    └── 📂 CFPB/
> │      ├── 📄 01_Combined_Narrative_and_Excerpt.md
> │      ├── 📄 CFPB_Complaint_Draft.md
> │      ├── 📄 CFPB_Violation_Excerpt_Master.md
> │      ├── 📄 Cover_Letter.md
> │      ├── 📄 _CFPB.md
> │    └── 📂 CRAs/
> │      └── 📂 Equifax/
> │        ├── 📄 Equifax_Violation_Excerpt.md
> │        ├── 📄 _Equifax.md
> │      └── 📂 Experian/
> │        ├── 📄 Experian_Access_your_credit_report_2_tradelines.csv
> │        ├── 📄 Experian_Access_your_credit_report_CH13_tradelines.csv
> │        ├── 📄 Experian_Violation_Excerpt.md
> │        ├── 📄 _Experian.md
> │      └── 📂 Transunion/
> │        ├── 📄 TransUnion_Violation_Excerpt.md
> │        ├── 📄 _Transunion.md
> │      ├── 📄 _CRAs.md
> │    ├── 📄 City_of_Indy_Violation_Excerpt.md
> │    ├── 📄 Execution_Checklist.md
> │    ├── 📄 FORMAL NOTICE OF CONTINUING FCRA VIOLATIONS.md
> │    └── 📂 NCUA/
> │    ├── 📄 NCUA CONSUMER COMPLAINT – DRAFT.md
> │      ├── 📄 01_Combined_Narrative_and_Excerpt_2.md
> │      ├── 📄 Cover_Letter_6.md
> │      ├── 📄 Exhibit_Manifest_1.md
> │      ├── 📄 MANIFEST_NCUA_Complaint_Packet.md
> │      ├── 📄 _NCUA.md
> │    ├── 📄 NOTICE OF FAILURE TO REFLECT DISPUTED STATUS.md
> │    ├── 📄 PHASE_CREDIT_EXECUTION_MAP.md
> │    ├── 📄 Sanctions_Readiness_Memo.md
> │    ├── 📄 _20_CFPB.md
> │    ├── 📄 _30_NCUA.md
> │    ├── 📄 _30_bureau_disputes.md
> │    ├── 📄 _30_demand_letters.md
> │    ├── 📄 _BBB.md
> └── 📂 C-05_Accounting_Surplus/
> │  └── 📂 05.01_Surplus_Forensics/
> │    ├── 📄 1️⃣ SURPLUS ACCOUNTING DEMAND LETTER.md
> │    └── 📂 C-05_Accounting_Surplus/
> │      ├── 📄 NT_Attorney_Intake_Summary.md
> │      ├── 📄 _25_IN_DFI.md
> │      ├── 📄 _50_HUD_FHEO.md
> │      ├── 📄 _PHASE_OVERVIEW.md
> │    ├── 📄 Surplus reconciliation table.md
> │  └── 📂 05.02_Fee_Inflation_Audit/
> │    ├── 📄 FCFCU_Audit_Forensic_Discrepancies.canvas
> │  ├── 📄 _PHASE_OVERVIEW.md
> └── 📂 C-06_Civil_Rights_Exposure/
> │  └── 📂 05.01_ADA_Accommodation_Record/
> │    ├── 📄 99_Legacy_Excerpt_3.md
> │    ├── 📄 Accommodation request log.md
> │    ├── 📄 _C06_ADA.md
> │  └── 📂 05.02_Access_to_Court_Impact/
> │    ├── 📄 DOJ_Civil_Rights_Violation_Excerpt.md
> │  └── 📂 05.03_Discriminatory_Impact_Assessment/
> │    ├── 📄 Cover_Letter_1.md
> │    ├── 📄 Cover_Letter_3.md
> │    ├── 📄 Cover_Letter_4.md
> │    ├── 📄 Cover_Letter_5.md
> │    ├── 📄 Cover_Letter_7.md
> │    ├── 📄 Cover_Letter_DOJ_Supplemental.md
> │    ├── 📄 DOJ_Civil_Rights_Violation_Excerpt.md
> │    ├── 📄 DOJ_Civil_Rights_Violation_Excerpt_Master.md
> │    ├── 📄 DOJ_Supplemental_Continuing_Harm.md
> │    ├── 📄 Exhibit_Manifest.md
> │    ├── 📄 HUD_FHEO_Complaint_Narrative.md
> │    ├── 📄 HUD_FHEO_Violation_Excerpt.md
> │    ├── 📄 IN_AG_Violation_Excerpt.md
> │    ├── 📄 IN_DFI_Violation_Excerpt.md
> │    ├── 📄 Indiana_AG_Complaint_Narrative.md
> │    ├── 📄 Indiana_Civil_Rights_Commission_Violation_Excerpt.md
> │    ├── 📄 Indiana_Civil_Rights_Complaint_Narrative.md
> │    ├── 📄 Indiana_DFI_Complaint_Narrative.md
> │    ├── 📄 Indiana_Department_of_Financial_Institutions_DFI_Violation_Excerpt.md
> │    ├── 📄 MANIFEST_HUD_FHEO_Complaint_Packet.md
> │    ├── 📄 MANIFEST_ICRC_Complaint_Packet.md
> │    ├── 📄 MANIFEST_IN_AG_Complaint_Packet.md
> │    ├── 📄 MANIFEST_Indiana_DFI_Packet.md
> │    ├── 📄 Violation_to_Regulator_Mapping.md
> │  └── 📂 06.01_ADA_Accommodation_Record/
> │    ├── 📄 Accommodation request log.md
> │  └── 📂 06.02_Discriminatory_Impact_Assessment/
> │    ├── 📄 DOJ_Civil_Rights_Violation_Excerpt.md
> │  ├── 📄 _40_DOJ_Civil_Rights.md
> │  ├── 📄 _55_IN_Civil_Rights.md
> │  ├── 📄 _PHASE_OVERVIEW.md
> └── 📂 C-07_Settlement_Narrative_Control/
> │  └── 📂 06.01_Settlement_Framework/
> │    ├── 📄 Settlement demand model.md
> │  └── 📂 06.02_Negotiation_Tracking/
> │  └── 📂 06.03_Narrative_Discipline/
> │    ├── 📄 01_Combined_Narrative_and_Excerpt_1.md
> │    ├── 📄 20251215_displacement_cold_exposure.md
> │    ├── 📄 BBB_Violation_Excerpt.md
> │    ├── 📄 _C10_Narrative_Control.md
> │  └── 📂 07.01_Settlement_Framework/
> │    ├── 📄 Settlement demand model.md
> │  └── 📂 07.02_Narrative_Discipline/
> │    ├── 📄 _C10_Narrative_Control.md
> │  ├── 📄 _PHASE_OVERVIEW.md
> ├── 📄 Phase Kanban.md
> ├── 📄 _PHASES_MASTER.md
> └── 📄 _STRUCTURE_LOCK.md
> ```

### Assistant
> Yep — you’ve got **real duplication + mis-numbering + mixed “phase vs regulator packets”** in places. Here’s what I’d delete/move/add so **01.03 and 02.03 have real tasks**, and the tree stops drifting.
> 
> ## What to delete (or move out) — concrete calls
> 
> ### 1) Kill duplicate phase CSVs
> - **DELETE** `01_PHASES/1_phases.csv`
> - **KEEP** `01_PHASES/1_phases-v2.csv` (rename to `1_phases.csv` if you want one canonical)
> 
> Reason: two sources of truth = guaranteed drift.
> 
> ---
> 
> ### 2) C-04 has duplicated tradeline CSV stored twice
> You have `30_Full_TriMerge_2025_12_tradelines.csv` in:
> - `04.01_Furnisher_Liability_Mapping/`
> - `04.02_Bureau_Dispute_Tracking/`
> 
> **KEEP only one** (I recommend keep in `04.02_Bureau_Dispute_Tracking/`), and:
> - **DELETE** the duplicate in `04.01_...`  
>   OR move it to a shared `C-04/_DATA/` folder and reference it.
> 
> ---
> 
> ### 3) C-05 has a nested folder that shouldn’t exist
> Inside:
> `C-05_Accounting_Surplus/05.01_Surplus_Forensics/` you have:
> `📂 C-05_Accounting_Surplus/` again.
> 
> That’s a recursion / copy-paste artifact.
> 
> - **MOVE OUT** anything valuable from `05.01_Surplus_Forensics/C-05_Accounting_Surplus/` to the proper level:
>   `C-05_Accounting_Surplus/`  
> - Then **DELETE** the nested folder.
> 
> ---
> 
> ### 4) C-06 has duplicate lane sets with wrong numbering
> You have both:
> - `05.01_ADA_Accommodation_Record/`, `05.02_Access_to_Court_Impact/`, `05.03_Discriminatory_Impact_Assessment/`
> and
> - `06.01_ADA_Accommodation_Record/`, `06.02_Discriminatory_Impact_Assessment/`
> 
> This is confusion fuel.
> 
> **KEEP ONLY the `06.xx` set** (because it matches phase C-06), and:
> - **MOVE** any unique docs from `05.xx` into the matching `06.xx`
> - **DELETE** the `05.xx` folders after merge
> 
> Also: you have the same “Accommodation request log.md” twice — dedupe.
> 
> ---
> 
> ### 5) C-07 has duplicate lane sets with wrong numbering
> You have both:
> - `06.01_Settlement_Framework/`, `06.02_Negotiation_Tracking/`, `06.03_Narrative_Discipline/`
> and
> - `07.01_Settlement_Framework/`, `07.02_Narrative_Discipline/`
> 
> **KEEP ONLY the `07.xx` set** (matches phase C-07).  
> - **MOVE** unique docs from `06.xx` into `07.xx`
> - **DELETE** `06.xx` folders after merge
> 
> ---
> 
> ### 6) C-03 has “rando stuff” at phase root — decide the rule
> In `C-03_Post_Removal_Liability/` you’ve got:
> - `_20_AG_Indiana.md`
> - `_20_Habitability.md`
> - `_45_FCC_Telecom.md`
> 
> These are not lane-specific and look like **regulator/agency packets**.
> 
> Pick one rule and enforce it:
> 
> **My recommendation:** create `C-03/_REGULATORS/` and move those there.
> 
> So:
> - **MOVE** `_20_AG_Indiana.md` → `C-03/_REGULATORS/`
> - **MOVE** `_20_Habitability.md` → `C-03/_REGULATORS/`
> - **MOVE** `_45_FCC_Telecom.md` → `C-03/_REGULATORS/`
> 
> (If they actually belong to C-06 civil rights instead, then move them there. But don’t leave them floating.)
> 
> ---
> 
> ## What to add (missing tasks) — 01.03 and 02.03
> 
> You’re right: those lanes exist but have no actual working docs/tasks. Here’s what should be there (non-generic, aligned to your strategy).
> 
> ### C-01 / 01.03_Legal_Impact_Assessment (ADD)
> Create these files:
> 
> 1) `Jurisdictional defect → remedy matrix.md`  
>    - Map each defect (mailing, posting, publication, 48-hr, unknown occupants, etc.) to: relief sought, standard of proof, best cite bucket, and what doc/event proves it.
> 
> 2) `TR 60(B)(6) void/voidable framing memo.md`  
>    - Your “void ab initio” positioning + what you’re actually asking the court to do.
> 
> 3) `Record-based reversal arguments (appeal-ready).md`  
>    - Clean bullets of reversible errors based strictly on the record you can cite.
> 
> 4) `Service/Notice defect severity scoring.md`  
>    - A table that ranks defects by: jurisdiction-kill strength, corroboration, and how easy it is for them to “explain away.”
> 
> 5) `Requested relief package definition.md`  
>    - Vacate judgment, stay writ, sanctions, fee shifting, correction orders, etc., with which phase supports each.
> 
> That lane should answer: **“So what? What is the legal effect and the requested remedy?”**
> 
> ---
> 
> ### C-02 / 02.03_Evidence_Intake_Log (ADD)
> Right now it’s empty. It needs to become your intake control center.
> 
> Create these:
> 
> 1) `10_Evidence_Intake_Log.csv` (or `.md` if you insist, but CSV is better)  
>    Columns should match your schema: `doc_id, received_date, doc_date, source, type, title, path, hash, linked_event_ids, linked_task_ids, confidentiality, notes`
> 
> 2) `Intake SOP.md`  
>    - Step-by-step: rename → hash → register → link to event → link to claim → store immutable.
> 
> 3) `Naming Convention Enforcement.md`  
>    - The exact filename format and what gets rejected.
> 
> 4) `Evidence Chain-of-Custody Register.md`  
>    - Especially important for photos/videos and anything from sheriff/court portals.
> 
> 5) `Open Requests Tracker.md`  
>    - USPS proof, publication receipts, sheriff invoices, body cam, dispatch logs, clerk certified records, etc.
> 
> That lane should answer: **“Do we know what we have, where it is, and what it proves?”**
> 
> ---
> 
> ## What to rename (because numbering is lying)
> 
> ### C-02 is misnamed
> Your earlier phase list had **C-02 = Writ & Eviction Irregularities**.
> This tree has **C-02_Evidence_Preservation**.
> 
> Pick one. Right now this will break your CSV alignment.
> 
> **Recommendation:**
> - Rename this folder to: `C-02_Evidence_Preservation/` only if you are committing that C-02 is evidence.
> - Otherwise, move Evidence Preservation into its own phase (ex: `C-08_Evidence_Preservation`) and restore `C-02_Writ_Eviction_Irregularities/`.
> 
> Blunt truth: **you can’t keep reusing phase numbers for different theories**. That’s how your system collapses.
> 
> ---
> 
> ## Quick “keep as-is” (nothing wrong, just messy)
> 
> - C-00 looks fine (record integrity, appellate preservation) — that’s a real foundation.
> - C-01 01.01 and 01.02 have appropriate lane docs.
> - C-04 structure is mostly fine; it just needs dedupe and a consistent data folder rule.
> 
> ---
> 
> ## The minimal “cleanup commit plan” (do this in order)
> 
> 1) Delete old phases CSV, keep v2.
> 2) Fix C-05 recursion folder.
> 3) Deduplicate C-06 (keep 06.xx only).
> 4) Deduplicate C-07 (keep 07.xx only).
> 5) Add the missing 01.03 and 02.03 task docs listed above.
> 6) Decide whether C-02 is “Writ/Eviction” or “Evidence Preservation” and rename/migrate accordingly.
> 
> If you want, paste your **current C-01 and C-02 lane IDs from the CSV** (or just the top rows), and I’ll give you the exact **task rows to add** (task_id/task_name/task_type/status/next_action) so you can import cleanly without hand-editing.

### User
> give me a migrations scripts and finish this im tired and have to move one, ```markdown
> . 📂 01_PHASES
> ├── 📄 1_phases-v3-LOCKED.csv
> ├── 📄 1_phases.csv
> └── 📂 C-00_Foreclosure_Record/
> │  └── 📂 C-00.L01_Record_Integrity/
> │    ├── 📄 T-0001_Master docket verification.md
> │    ├── 📄 T-0002_Filing timestamp audit.md
> │    ├── 📄 T-0003_Order sequence alignment.md
> │  └── 📂 C-00.L02_Jurisdictional_Predicate_Review/
> │    ├── 📄 D-0001_Service_Deficiency_Analysis.md
> │  └── 📂 C-00.L03_Appellate_Preservation/
> │    ├── 📄 D-0002_Appellate_Issue_Preservation.md
> │  ├── 📄 _PHASE_OVERVIEW.md
> └── 📂 C-01_Jurisdictional_Defects/
> │  └── 📂 C-01.L01_Service_Compliance_Audit/
> │    ├── 📄 T-0006_Sheriff return review.md
> │    ├── 📄 T-0007_Secondary mailing failure analysis.md
> │  └── 📂 C-01.L02_Notice_Failures/
> │    ├── 📄 T-0008_48-hour notice absence documentation.md
> │    ├── 📄 T-0009_Publication proof gap.md
> │  ├── 📄 _PHASE_OVERVIEW.md
> └── 📂 C-02_Evidence_Preservation/
> │  └── 📂 C-02.L01_Litigation_Hold_Control/
> │    ├── 📄 T-0010_Dispatch preservation notices.md
> │  └── 📂 C-02.L02_Spoliation_Risk_Register/
> │    ├── 📄 D-0004_20_Spoliation_Risk_Ledger.md
> │  ├── 📄 _PHASE_OVERVIEW.md
> └── 📂 C-03_Post_Removal_Liability/
> │  └── 📂 C-03.L01_Writ_Execution_Validity/
> │    ├── 📄 T-0011_Writ predicate checklist.md
> │  └── 📂 C-03.L02_Property_Interference/
> │    ├── 📄 T-0012_Property interference log.md
> │  └── 📂 C-03.L03_State_Action_Analysis/
> │    ├── 📄 D-0005_Sheriff_Internal_Affairs_Complaint.md
> │    ├── 📄 MANIFEST_Sheriff_Oversight_Packet.md
> │    ├── 📄 Marion_County_Sheriff_Oversight_Violation_Excerpt.md
> │    ├── 📄 Sheriff_Violation_Excerpt.md
> │    ├── 📄 T-0013_1983 element mapping.md
> │    ├── 📄 _35_Sheriff_Oversight.md
> │  ├── 📄 _20_AG_Indiana.md
> │  ├── 📄 _20_Habitability.md
> │  ├── 📄 _45_FCC_Telecom.md
> │  ├── 📄 _PHASE_OVERVIEW.md
> └── 📂 C-04_FCRA_Financial_Misconduct/
> │  └── 📂 C-04.L01_Furnisher_Liability_Mapping/
> │    ├── 📄 Core_Credit_Tables.md
> │    ├── 📄 D-0006_2️⃣ FCRA STATUTORY DAMAGES MODEL.md
> │    ├── 📄 D-0007_30_Full_TriMerge_2025_12_tradelines.csv
> │    ├── 📄 T-0014_Duplicate tradeline documentation.md
> │    ├── 📄 _20_furnisher_disputes.md
> │    ├── 📄 _CREDIT_FCRA_MASTER.md
> │  └── 📂 C-04.L02_Bureau_Dispute_Tracking/
> │    ├── 📄 30_Full_TriMerge_2025_12_tradelines.csv
> │    ├── 📄 3️⃣ REGULATOR-READY COMPLAINT PACKET.md
> │    └── 📂 CFPB/
> │      ├── 📄 01_Combined_Narrative_and_Excerpt.md
> │      ├── 📄 CFPB_Complaint_Draft.md
> │      ├── 📄 CFPB_Violation_Excerpt_Master.md
> │      ├── 📄 Cover_Letter.md
> │      ├── 📄 _CFPB.md
> │    └── 📂 CRAs/
> │      └── 📂 Equifax/
> │        ├── 📄 Equifax_Violation_Excerpt.md
> │        ├── 📄 _Equifax.md
> │      └── 📂 Experian/
> │        ├── 📄 Experian_Access_your_credit_report_2_tradelines.csv
> │        ├── 📄 Experian_Access_your_credit_report_CH13_tradelines.csv
> │        ├── 📄 Experian_Violation_Excerpt.md
> │        ├── 📄 _Experian.md
> │      └── 📂 Transunion/
> │        ├── 📄 TransUnion_Violation_Excerpt.md
> │        ├── 📄 _Transunion.md
> │      ├── 📄 _30_bureau_disputes.md
> │      ├── 📄 _CRAs.md
> │    ├── 📄 City_of_Indy_Violation_Excerpt.md
> │    ├── 📄 Execution_Checklist.md
> │    ├── 📄 FORMAL NOTICE OF CONTINUING FCRA VIOLATIONS.md
> │    └── 📂 NCUA/
> │    ├── 📄 NCUA CONSUMER COMPLAINT – DRAFT.md
> │      ├── 📄 01_Combined_Narrative_and_Excerpt_2.md
> │      ├── 📄 Cover_Letter_6.md
> │      ├── 📄 Exhibit_Manifest_1.md
> │      ├── 📄 MANIFEST_NCUA_Complaint_Packet.md
> │      ├── 📄 _NCUA.md
> │    ├── 📄 NOTICE OF FAILURE TO REFLECT DISPUTED STATUS.md
> │    ├── 📄 PHASE_CREDIT_EXECUTION_MAP.md
> │    ├── 📄 Sanctions_Readiness_Memo.md
> │    ├── 📄 _30_demand_letters.md
> │    ├── 📄 _BBB.md
> └── 📂 C-05_Accounting_Surplus/
> │  └── 📂 C-05.L01_Surplus_Forensics/
> │    ├── 📄 D-0008_1️⃣ SURPLUS ACCOUNTING DEMAND LETTER.md
> │    ├── 📄 NT_Attorney_Intake_Summary.md
> │    ├── 📄 T-0015_Surplus reconciliation table.md
> │    ├── 📄 _25_IN_DFI.md
> │    ├── 📄 _50_HUD_FHEO.md
> │    ├── 📄 _PHASE_OVERVIEW.md
> │  └── 📂 C-05.L02_Fee_Inflation_Audit/
> │    ├── 📄 D-0009_FCFCU_Audit_Forensic_Discrepancies.canvas
> │  ├── 📄 _PHASE_OVERVIEW.md
> └── 📂 C-06_Civil_Rights_Exposure/
> │  └── 📂 C-06.L01_ADA_Accommodation_Record/
> │    ├── 📄 99_Legacy_Excerpt_3.md
> │    ├── 📄 Accommodation request log.md
> │    ├── 📄 D-0010__C06_ADA.md
> │    ├── 📄 D-0011_DOJ_Civil_Rights_Violation_Excerpt.md
> │    ├── 📄 T-0016_Accommodation request log.md
> │  └── 📂 C-06.L02_Discriminatory_Impact_Assessment/
> │    ├── 📄 Cover_Letter_1.md
> │    ├── 📄 Cover_Letter_3.md
> │    ├── 📄 Cover_Letter_4.md
> │    ├── 📄 Cover_Letter_5.md
> │    ├── 📄 Cover_Letter_7.md
> │    ├── 📄 Cover_Letter_DOJ_Supplemental.md
> │    ├── 📄 DOJ_Civil_Rights_Violation_Excerpt.md
> │    ├── 📄 DOJ_Civil_Rights_Violation_Excerpt_Master.md
> │    ├── 📄 DOJ_Supplemental_Continuing_Harm.md
> │    ├── 📄 Exhibit_Manifest.md
> │    ├── 📄 HUD_FHEO_Complaint_Narrative.md
> │    ├── 📄 HUD_FHEO_Violation_Excerpt.md
> │    ├── 📄 IN_AG_Violation_Excerpt.md
> │    ├── 📄 IN_DFI_Violation_Excerpt.md
> │    ├── 📄 Indiana_AG_Complaint_Narrative.md
> │    ├── 📄 Indiana_Civil_Rights_Commission_Violation_Excerpt.md
> │    ├── 📄 Indiana_Civil_Rights_Complaint_Narrative.md
> │    ├── 📄 Indiana_DFI_Complaint_Narrative.md
> │    ├── 📄 Indiana_Department_of_Financial_Institutions_DFI_Violation_Excerpt.md
> │    ├── 📄 MANIFEST_HUD_FHEO_Complaint_Packet.md
> │    ├── 📄 MANIFEST_ICRC_Complaint_Packet.md
> │    ├── 📄 MANIFEST_IN_AG_Complaint_Packet.md
> │    ├── 📄 MANIFEST_Indiana_DFI_Packet.md
> │    ├── 📄 Violation_to_Regulator_Mapping.md
> │  ├── 📄 _40_DOJ_Civil_Rights.md
> │  ├── 📄 _55_IN_Civil_Rights.md
> │  ├── 📄 _PHASE_OVERVIEW.md
> └── 📂 C-07_Settlement_Narrative_Control/
> │  └── 📂 06.01_Settlement_Framework/
> │  └── 📂 C-07.L01_Settlement_Framework/
> │    ├── 📄 Settlement demand model.md
> │    ├── 📄 T-0017_Settlement demand model.md
> │  └── 📂 C-07.L02_Narrative_Discipline/
> │    ├── 📄 01_Combined_Narrative_and_Excerpt_1.md
> │    ├── 📄 20251215_displacement_cold_exposure.md
> │    ├── 📄 BBB_Violation_Excerpt.md
> │    ├── 📄 D-0012__C10_Narrative_Control.md
> │    ├── 📄 _C10_Narrative_Control.md
> │  ├── 📄 _PHASE_OVERVIEW.md
> ├── 📄 Phase Kanban.md
> ├── 📄 _PHASES_MASTER.md
> └── 📄 _STRUCTURE_LOCK.md
> ```, also happy go lucky may a phaes v3.

### Assistant
> Here’s the **locked, forward-safe migration kit**: one **SQL migration (v3)** to finish the DB schema cleanly + one **repo migration script (Python)** that will **(a)** create the missing lane/task/doc structure for **C-01.L03** and **C-02.L03**, **(b)** clean the obvious “rando/duplicate” folder issue in **C-07**, and **(c)** standardize filenames to your **ID-first** convention without nuking content.
> 
> ---
> 
> ## 1) SQL Migration — finish V2 properly (add missing join tables + indexes + updated_at trigger)
> 
> Save as: `DATABASE_SCHEMA_MIGRATION_V3.sql` (run after your current V2)
> 
> ```sql
> -- DATABASE_SCHEMA_MIGRATION_V3.sql
> -- Completes schema v2: remaining join tables, indexes, and updated_at triggers
> 
> BEGIN;
> 
> -- 0) Safety: create extension if needed
> CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
> 
> -- 1) Finish join tables (V2 only created task_doc then stopped)
> CREATE TABLE IF NOT EXISTS public.event_doc (
>     event_id TEXT REFERENCES public.events(event_id) ON DELETE CASCADE,
>     doc_id   TEXT REFERENCES public.docs(doc_id) ON DELETE CASCADE,
>     relation TEXT NOT NULL CHECK (relation IN ('proves','mentions','contradicts','context')),
>     PRIMARY KEY (event_id, doc_id)
> );
> 
> CREATE TABLE IF NOT EXISTS public.event_claim (
>     event_id TEXT REFERENCES public.events(event_id) ON DELETE CASCADE,
>     claim_id TEXT REFERENCES public.claims(claim_id) ON DELETE CASCADE,
>     strength TEXT NOT NULL CHECK (strength IN ('strong','medium','weak')),
>     PRIMARY KEY (event_id, claim_id)
> );
> 
> CREATE TABLE IF NOT EXISTS public.doc_claim (
>     doc_id   TEXT REFERENCES public.docs(doc_id) ON DELETE CASCADE,
>     claim_id TEXT REFERENCES public.claims(claim_id) ON DELETE CASCADE,
>     strength TEXT NOT NULL CHECK (strength IN ('strong','medium','weak')),
>     PRIMARY KEY (doc_id, claim_id)
> );
> 
> CREATE TABLE IF NOT EXISTS public.task_event (
>     task_id  TEXT REFERENCES public.tasks(task_id) ON DELETE CASCADE,
>     event_id TEXT REFERENCES public.events(event_id) ON DELETE CASCADE,
>     relation TEXT NOT NULL CHECK (relation IN ('triggered_by','clarifies','responds_to')),
>     PRIMARY KEY (task_id, event_id)
> );
> 
> -- 2) Indexes for fast filtering (phase/lane timelines, doc lookups)
> CREATE INDEX IF NOT EXISTS idx_lanes_phase_id      ON public.lanes(phase_id);
> CREATE INDEX IF NOT EXISTS idx_tasks_phase_id      ON public.tasks(phase_id);
> CREATE INDEX IF NOT EXISTS idx_tasks_lane_id       ON public.tasks(lane_id);
> CREATE INDEX IF NOT EXISTS idx_claims_phase_id     ON public.claims(phase_id);
> CREATE INDEX IF NOT EXISTS idx_claims_lane_id      ON public.claims(lane_id);
> CREATE INDEX IF NOT EXISTS idx_exhibits_filing_id  ON public.exhibits(filing_id);
> CREATE INDEX IF NOT EXISTS idx_exhibits_doc_id     ON public.exhibits(doc_id);
> CREATE INDEX IF NOT EXISTS idx_task_doc_doc_id     ON public.task_doc(doc_id);
> CREATE INDEX IF NOT EXISTS idx_event_doc_doc_id    ON public.event_doc(doc_id);
> 
> -- Optional: JSONB / tag search helpers
> CREATE INDEX IF NOT EXISTS idx_events_actors_gin   ON public.events USING GIN (actors);
> CREATE INDEX IF NOT EXISTS idx_events_tags_gin     ON public.events USING GIN (impact_tags);
> 
> -- 3) updated_at trigger helper
> CREATE OR REPLACE FUNCTION public.set_updated_at()
> RETURNS TRIGGER AS $$
> BEGIN
>   NEW.updated_at = NOW();
>   RETURN NEW;
> END;
> $$ LANGUAGE plpgsql;
> 
> -- Add updated_at columns where missing + triggers where relevant
> DO $$
> BEGIN
>   IF NOT EXISTS (
>     SELECT 1 FROM information_schema.columns
>     WHERE table_schema='public' AND table_name='docs' AND column_name='updated_at'
>   ) THEN
>     ALTER TABLE public.docs ADD COLUMN updated_at TIMESTAMPTZ DEFAULT NOW();
>   END IF;
> 
>   IF NOT EXISTS (
>     SELECT 1 FROM information_schema.columns
>     WHERE table_schema='public' AND table_name='lanes' AND column_name='updated_at'
>   ) THEN
>     ALTER TABLE public.lanes ADD COLUMN updated_at TIMESTAMPTZ DEFAULT NOW();
>   END IF;
> 
>   IF NOT EXISTS (
>     SELECT 1 FROM information_schema.columns
>     WHERE table_schema='public' AND table_name='phases' AND column_name='updated_at'
>   ) THEN
>     ALTER TABLE public.phases ADD COLUMN updated_at TIMESTAMPTZ DEFAULT NOW();
>   END IF;
> 
>   IF NOT EXISTS (
>     SELECT 1 FROM information_schema.columns
>     WHERE table_schema='public' AND table_name='events' AND column_name='updated_at'
>   ) THEN
>     ALTER TABLE public.events ADD COLUMN updated_at TIMESTAMPTZ DEFAULT NOW();
>   END IF;
> 
>   IF NOT EXISTS (
>     SELECT 1 FROM information_schema.columns
>     WHERE table_schema='public' AND table_name='claims' AND column_name='updated_at'
>   ) THEN
>     ALTER TABLE public.claims ADD COLUMN updated_at TIMESTAMPTZ DEFAULT NOW();
>   END IF;
> 
>   IF NOT EXISTS (
>     SELECT 1 FROM information_schema.columns
>     WHERE table_schema='public' AND table_name='filings' AND column_name='updated_at'
>   ) THEN
>     ALTER TABLE public.filings ADD COLUMN updated_at TIMESTAMPTZ DEFAULT NOW();
>   END IF;
> END$$;
> 
> DROP TRIGGER IF EXISTS trg_phases_updated_at ON public.phases;
> CREATE TRIGGER trg_phases_updated_at
> BEFORE UPDATE ON public.phases
> FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
> 
> DROP TRIGGER IF EXISTS trg_lanes_updated_at ON public.lanes;
> CREATE TRIGGER trg_lanes_updated_at
> BEFORE UPDATE ON public.lanes
> FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
> 
> DROP TRIGGER IF EXISTS trg_tasks_updated_at ON public.tasks;
> CREATE TRIGGER trg_tasks_updated_at
> BEFORE UPDATE ON public.tasks
> FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
> 
> DROP TRIGGER IF EXISTS trg_docs_updated_at ON public.docs;
> CREATE TRIGGER trg_docs_updated_at
> BEFORE UPDATE ON public.docs
> FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
> 
> DROP TRIGGER IF EXISTS trg_events_updated_at ON public.events;
> CREATE TRIGGER trg_events_updated_at
> BEFORE UPDATE ON public.events
> FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
> 
> DROP TRIGGER IF EXISTS trg_claims_updated_at ON public.claims;
> CREATE TRIGGER trg_claims_updated_at
> BEFORE UPDATE ON public.claims
> FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
> 
> DROP TRIGGER IF EXISTS trg_filings_updated_at ON public.filings;
> CREATE TRIGGER trg_filings_updated_at
> BEFORE UPDATE ON public.filings
> FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();
> 
> COMMIT;
> ```
> 
> ---
> 
> ## 2) Repo Migration Script — creates missing C-01.L03 + C-02.L03 tasks, fixes C-07 “rando folder”, normalizes naming
> 
> ### What this script will do (opinionated + safe)
> **Adds (missing):**
> - `C-01.L03_Legal_Impact_Assessment/`
>   - `T-0018_TR60B6_void_ab_initio_impact_memo.md`
>   - `T-0019_Prejudice_and_due_process_harm_analysis.md`
>   - `D-0013_Jurisdictional_Impact_Assessment_Memo.md` (doc produced by T-0018)
> - `C-02.L03_Evidence_Intake_Log/`
>   - `T-0020_Evidence_intake_log_setup_and_rules.md`
>   - `D-0014_Evidence_Intake_Log_Template.md`
>   - `D-0015_Evidence_Intake_Log_2026_Q1.csv`
> 
> **Fixes (delete/move):**
> - `C-07_Settlement_Narrative_Control/06.01_Settlement_Framework/` (the stray lane folder)
>   - If it’s empty: **delete**
>   - If it has files: **move them into** `C-07.L01_Settlement_Framework/`
> 
> **Normalizes:**
> - Any `Settlement demand model.md` that duplicates `T-0017_Settlement demand model.md`:
>   - keeps the **ID version**, renames the non-ID one to `_LEGACY_Settlement demand model.md` (does **not** delete content)
> 
> ### Save as: `migrate_phases_repo_v3.py`
> 
> ```python
> import argparse
> import shutil
> from pathlib import Path
> from datetime import datetime
> 
> # ----------------------------
> # Helpers
> # ----------------------------
> def ts():
>     return datetime.now().strftime("%Y%m%d_%H%M%S")
> 
> def ensure_dir(p: Path, dry_run: bool):
>     if p.exists():
>         return
>     print(f"[MKDIR] {p}")
>     if not dry_run:
>         p.mkdir(parents=True, exist_ok=True)
> 
> def write_file(p: Path, content: str, dry_run: bool):
>     if p.exists():
>         print(f"[SKIP] exists: {p.name}")
>         return
>     print(f"[WRITE] {p}")
>     if not dry_run:
>         p.write_text(content, encoding="utf-8")
> 
> def move_all(src: Path, dst: Path, dry_run: bool):
>     if not src.exists():
>         return
>     ensure_dir(dst, dry_run)
>     for item in src.iterdir():
>         target = dst / item.name
>         print(f"[MOVE] {item} -> {target}")
>         if not dry_run:
>             shutil.move(str(item), str(target))
> 
> def safe_delete_dir(p: Path, dry_run: bool):
>     if not p.exists():
>         return
>     # Only delete if empty
>     if any(p.iterdir()):
>         print(f"[SKIP] not empty, won't delete: {p}")
>         return
>     print(f"[RMDIR] {p}")
>     if not dry_run:
>         p.rmdir()
> 
> def backup_tree(root: Path, dry_run: bool):
>     backup = root.parent / f"{root.name}__BACKUP__{ts()}"
>     print(f"[BACKUP] {root} -> {backup}")
>     if not dry_run:
>         shutil.copytree(root, backup)
>     return backup
> 
> # ----------------------------
> # Content templates (minimal, not fluff)
> # ----------------------------
> TASK_TMPL = """---
> task_id: {task_id}
> phase_id: {phase_id}
> lane_id: {lane_id}
> task_type: {task_type}
> status: Not Started
> priority: {priority}
> owner: Cody
> next_action: {next_action}
> ---
> 
> # {title}
> 
> ## Objective
> {objective}
> 
> ## Inputs
> {inputs}
> 
> ## Output
> {output}
> 
> ## Notes
> {notes}
> """
> 
> DOC_TMPL = """---
> doc_id: {doc_id}
> phase_id: {phase_id}
> lane_id: {lane_id}
> doc_type: {doc_type}
> status: Active
> source: Self
> reliability: Primary
> ---
> 
> # {title}
> 
> ## Summary
> {summary}
> 
> ## Links
> - Producing Task: [[{task_id}]]
> 
> ## Notes
> {notes}
> """
> 
> CSV_TMPL = """doc_id,phase_id,lane_id,item_type,item_id,title,date,source,storage_path,hash_sha256,notes
> """
> 
> # ----------------------------
> # Migration actions
> # ----------------------------
> def migrate(root: Path, dry_run: bool):
>     if not root.exists():
>         raise SystemExit(f"Root not found: {root}")
> 
>     backup_tree(root, dry_run)
> 
>     # 1) Create missing lanes
>     c01 = root / "C-01_Jurisdictional_Defects"
>     c02 = root / "C-02_Evidence_Preservation"
>     c07 = root / "C-07_Settlement_Narrative_Control"
> 
>     c01_l03 = c01 / "C-01.L03_Legal_Impact_Assessment"
>     c02_l03 = c02 / "C-02.L03_Evidence_Intake_Log"
> 
>     ensure_dir(c01_l03, dry_run)
>     ensure_dir(c02_l03, dry_run)
> 
>     # 2) Add missing tasks/docs for C-01.L03
>     write_file(
>         c01_l03 / "T-0018_TR60B6_void_ab_initio_impact_memo.md",
>         TASK_TMPL.format(
>             task_id="T-0018",
>             phase_id="C-01",
>             lane_id="C-01.L03",
>             task_type="Draft",
>             priority="P0",
>             next_action="Draft memo: why defects make judgment void (not voidable); cite TR 60(B)(6), TR 4.1, due process.",
>             title="TR 60(B)(6) void ab initio impact memo",
>             objective="Convert the service/notice defects into a clean legal-impact memo that ties directly to vacatur and nullification of downstream orders.",
>             inputs="- Service/Notice defect findings (C-01.L01, C-01.L02)\n- Docket timeline (C-00)\n- Any court statements about service",
>             output="D-0013 Jurisdictional Impact Assessment Memo (court-ready narrative + citations map)",
>             notes="Keep it surgical: jurisdiction first, downstream collapse second (default → sale → writ).",
>         ),
>         dry_run,
>     )
> 
>     write_file(
>         c01_l03 / "T-0019_Prejudice_and_due_process_harm_analysis.md",
>         TASK_TMPL.format(
>             task_id="T-0019",
>             phase_id="C-01",
>             lane_id="C-01.L03",
>             task_type="Analyze",
>             priority="P1",
>             next_action="Map specific prejudice: no chance to respond, no participation at default, lost hearing opportunities, ADA notice impacts.",
>             title="Prejudice and due process harm analysis",
>             objective="Document how defective notice caused concrete prejudice (procedural + practical), strengthening vacatur and civil-rights posture.",
>             inputs="- Court dates + default timeline\n- ADA accommodation attempts (C-06)\n- Eviction/removal facts (C-03)",
>             output="Prejudice section usable in motions, appeal briefs, and regulator narratives",
>             notes="This is where you connect 'missing notice' to real-world harm without sounding emotional.",
>         ),
>         dry_run,
>     )
> 
>     write_file(
>         c01_l03 / "D-0013_Jurisdictional_Impact_Assessment_Memo.md",
>         DOC_TMPL.format(
>             doc_id="D-0013",
>             phase_id="C-01",
>             lane_id="C-01.L03",
>             doc_type="Memo",
>             title="Jurisdictional Impact Assessment Memo (Void ab initio chain)",
>             summary="Court-ready memo: service/notice defects → lack of personal jurisdiction → void default/judgment → downstream orders and writ collapse.",
>             task_id="T-0018",
>             notes="Add pinpoint citations once you paste in the exact docket entries/returns/publication lines.",
>         ),
>         dry_run,
>     )
> 
>     # 3) Add missing tasks/docs for C-02.L03
>     write_file(
>         c02_l03 / "T-0020_Evidence_intake_log_setup_and_rules.md",
>         TASK_TMPL.format(
>             task_id="T-0020",
>             phase_id="C-02",
>             lane_id="C-02.L03",
>             task_type="Draft",
>             priority="P0",
>             next_action="Stand up intake rules: naming, hashing, source, event/task links, no-orphan enforcement.",
>             title="Evidence intake log setup and rules",
>             objective="Create the operational rules and log templates so every new artifact gets an ID, a hash, and trace links on day one.",
>             inputs="- Your folder conventions\n- LITIGATION_SCHEMA_LOCK.md rules\n- Existing doc patterns in C-04/C-06",
>             output="D-0014 Intake template + D-0015 CSV log seeded for 2026 Q1",
>             notes="This is what stops the repo from drifting again.",
>         ),
>         dry_run,
>     )
> 
>     write_file(
>         c02_l03 / "D-0014_Evidence_Intake_Log_Template.md",
>         DOC_TMPL.format(
>             doc_id="D-0014",
>             phase_id="C-02",
>             lane_id="C-02.L03",
>             doc_type="Template",
>             title="Evidence Intake Log Template (Rules + Required Fields)",
>             summary="Template + rules for logging every artifact with ID, hash, source, and required linking (task/event).",
>             task_id="T-0020",
>             notes="If you want: enforce with a pre-commit hook later.",
>         ),
>         dry_run,
>     )
> 
>     write_file(
>         c02_l03 / "D-0015_Evidence_Intake_Log_2026_Q1.csv",
>         CSV_TMPL,
>         dry_run,
>     )
> 
>     # 4) Fix C-07 stray folder: "06.01_Settlement_Framework"
>     stray = c07 / "06.01_Settlement_Framework"
>     target = c07 / "C-07.L01_Settlement_Framework"
>     if stray.exists():
>         if any(stray.iterdir()):
>             print("[FIX] Moving stray C-07/06.01_Settlement_Framework contents into C-07.L01_Settlement_Framework")
>             move_all(stray, target, dry_run)
>         safe_delete_dir(stray, dry_run)
> 
>     # 5) Prefer ID file, preserve legacy duplicate (no deletion)
>     id_file = target / "T-0017_Settlement demand model.md"
>     legacy_file = target / "Settlement demand model.md"
>     if legacy_file.exists() and id_file.exists():
>         legacy_new = target / "_LEGACY_Settlement demand model.md"
>         print(f"[RENAME] {legacy_file.name} -> {legacy_new.name}")
>         if not dry_run:
>             legacy_file.rename(legacy_new)
> 
>     print("\n[DONE] Migration steps completed. Run your audit script next.")
> 
> def main():
>     ap = argparse.ArgumentParser()
>     ap.add_argument("--root", required=True, help="Path to 01_PHASES directory")
>     ap.add_argument("--dry-run", action="store_true", help="Print actions without changing files")
>     args = ap.parse_args()
>     migrate(Path(args.root), args.dry_run)
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ### Run it
> ```bash
> python migrate_phases_repo_v3.py --root "C:\g-drive\My Drive\qivault\30_projects\30.05_CASES\30.05.01_FCFCU\content\01_PHASES" --dry-run
> python migrate_phases_repo_v3.py --root "C:\g-drive\My Drive\qivault\30_projects\30.05_CASES\30.05.01_FCFCU\content\01_PHASES"
> ```
> 
> Then run your existing audit:
> ```bash
> python schema_integrity_audit.py
> ```
> 
> ---
> 
> ## 3) Quick call: what to delete vs keep (based on your tree)
> 
> **Delete (only if empty after move):**
> - `C-07_Settlement_Narrative_Control/06.01_Settlement_Framework/` ✅ (it’s a drift artifact)
> 
> **Do NOT delete (rename to preserve history):**
> - Any non-ID duplicate of an ID-file (example: `Settlement demand model.md`) → rename to `_LEGACY_...` like the script does.
> 
> **Keep as-is for now (but later you should ID-prefix):**
> - The many cover letters and narratives in `C-06.L02...` (they’re content-heavy; don’t churn when you’re exhausted—just lock intake rules so new stuff is clean).
> 
> ---
> 
> If you want the migration script to also **auto-prefix** the non-ID files in C-06.L02 with `D-####_...` safely (without collisions), say the word and I’ll extend it—but right now this gets you **unstuck** and aligned **without blowing up your repo**.

### User
> when did we do a database? ok fine, make it postgress local or something im not dealing with supabase right now.

### Assistant
> You *didn’t* “do a database” in the sense of running one. We drafted artifacts **as if** you’d want one (you just uploaded files named like `DATABASE_SCHEMA_MIGRATION_V2.sql`, `LITIGATION_SCHEMA_LOCK.md`, etc.). Those uploads have **expired on my side**, so I can’t read them right now. If you want me to merge/extend *those exact files*, re-upload them.  
> 
> That said: you’re tired and need to move on, so here’s a clean **local Postgres** setup + **migrations + import + folder-index logging**, aligned to your phase/lane/task/doc system.
> 
> ---
> 
> ## 0) What to delete / what to add (based on your tree)
> 
> ### Delete / consolidate (rando + duplicates)
> 1. **Duplicate folder in C-07**
>    - ❌ `C-07_Settlement_Narrative_Control/06.01_Settlement_Framework/`  
>    - ✅ Keep `C-07_Settlement_Narrative_Control/C-07.L01_Settlement_Framework/`
> 
> 2. **Duplicate “Settlement demand model” file**
>    - In `C-07.L01...` you have:
>      - `Settlement demand model.md`
>      - `T-0017_Settlement demand model.md`
>    - ❌ Delete the unprefixed one; ✅ keep `T-0017_...`
> 
> 3. **Duplicate “Accommodation request log”**
>    - In `C-06.L01...` you have:
>      - `Accommodation request log.md`
>      - `T-0016_Accommodation request log.md`
>    - ❌ Delete the unprefixed one; ✅ keep `T-0016_...` (this is a living log = Task/Tracker)
> 
> 4. **Duplicate DOJ excerpt in C-06**
>    - You have both:
>      - `D-0011_DOJ_Civil_Rights_Violation_Excerpt.md`
>      - `DOJ_Civil_Rights_Violation_Excerpt.md` (and maybe master too)
>    - ✅ Pick ONE canonical:
>      - Keep `D-0011_DOJ_Civil_Rights_Violation_Excerpt.md`
>      - If you need “Master”, rename to `D-00XX_DOJ_Civil_Rights_Violation_Excerpt_Master.md`
>      - ❌ Delete any unprefixed duplicates.
> 
> ### Add (missing lanes + missing tasks you called out)
> You’re missing lane folders for **01.03** and **02.03** in the “locked” tree naming style.
> 
> 1. Add lane folder:
> - ✅ `C-01_Jurisdictional_Defects/C-01.L03_Legal_Impact_Assessment/`
> 
> Add tasks/docs inside (suggested, non-generic, matches your strategy):
> - `T-0018_TR60B6_void_ab_initio_argument_map.md`
> - `D-0013_Jurisdictional_defect_consequence_matrix.md` (service/notice → void vs voidable, remedy, preservation)
> - `T-0019_Appellate_posture_and_standard_of_review_notes.md`
> - `D-0014_Relief_requested_remedy_menu_vacate_stay_sanctions.md`
> 
> 2. Add lane folder:
> - ✅ `C-02_Evidence_Preservation/C-02.L03_Evidence_Intake_Log/`
> 
> Add tasks/docs inside:
> - `T-0020_Evidence_intake_register.md` (living intake log)
> - `D-0015_Chain_of_custody_template.md`
> - `T-0021_File_hashing_and_immutability_ledger.md`
> - `D-0016_Evidence_intake_SOP_and_naming_rules.md`
> 
> ---
> 
> ## 1) Locked schema (what we’re implementing)
> 
> This is the *minimum* that won’t break later:
> 
> ### Core entities
> - **phase**: `C-01`, `C-02`…
> - **lane**: `C-01.L01`, `C-01.L02`, `C-01.L03`…
> - **artifact**: any file tracked (task/doc/manifest/etc.)
>   - `artifact_type`: `TASK`, `DOC`, `MANIFEST`, `EXCERPT`, `CSV`, `CANVAS`, `OTHER`
>   - `artifact_code`: `T-0017`, `D-0011` (nullable for legacy until normalized)
>   - `title`: human name
>   - `path`: relative repo path
>   - `sha256`, `bytes`, timestamps (so “immutability” becomes real)
> 
> ### Logging (so you can “implement logging moving forward”)
> - **artifact_log**: append-only event stream:
>   - `CREATED`, `MOVED`, `RENAMED`, `HASHED`, `UPDATED`, `DELETED`, `TAGGED`, `STATUS_CHANGED`
>   - includes old/new values where relevant
> 
> ### Optional but useful
> - tags, links (artifact↔artifact references), status, priority.
> 
> ---
> 
> ## 2) Local Postgres: docker-compose + migrations + importer
> 
> ### A) `docker-compose.yml`
> ```yaml
> services:
>   db:
>     image: postgres:16
>     container_name: qiphases_db
>     environment:
>       POSTGRES_DB: qiphases
>       POSTGRES_USER: qiphases
>       POSTGRES_PASSWORD: qiphases
>     ports:
>       - "54329:5432"
>     volumes:
>       - qiphases_data:/var/lib/postgresql/data
> volumes:
>   qiphases_data:
> ```
> 
> ### B) Migration 001 — schema (`migrations/001_init.sql`)
> ```sql
> BEGIN;
> 
> CREATE SCHEMA IF NOT EXISTS qiphase;
> 
> -- ---------- enums ----------
> DO $$ BEGIN
>   CREATE TYPE qiphase.artifact_type AS ENUM ('TASK','DOC','MANIFEST','EXCERPT','CSV','CANVAS','OTHER');
> EXCEPTION WHEN duplicate_object THEN NULL; END $$;
> 
> DO $$ BEGIN
>   CREATE TYPE qiphase.log_action AS ENUM (
>     'CREATED','MOVED','RENAMED','HASHED','UPDATED','DELETED','TAGGED','STATUS_CHANGED','IMPORTED'
>   );
> EXCEPTION WHEN duplicate_object THEN NULL; END $$;
> 
> -- ---------- phases ----------
> CREATE TABLE IF NOT EXISTS qiphase.phase (
>   phase_id        text PRIMARY KEY,          -- e.g., C-01
>   phase_name      text NOT NULL,
>   status          text NOT NULL DEFAULT 'Active',
>   core_theory     text,
>   primary_objective text,
>   notes           text,
>   created_at      timestamptz NOT NULL DEFAULT now(),
>   updated_at      timestamptz NOT NULL DEFAULT now()
> );
> 
> -- ---------- lanes ----------
> CREATE TABLE IF NOT EXISTS qiphase.lane (
>   lane_id         text PRIMARY KEY,          -- e.g., C-01.L03
>   phase_id        text NOT NULL REFERENCES qiphase.phase(phase_id) ON DELETE CASCADE,
>   lane_name       text NOT NULL,
>   sort_order      int NOT NULL DEFAULT 0,
>   status          text NOT NULL DEFAULT 'Active',
>   notes           text,
>   created_at      timestamptz NOT NULL DEFAULT now(),
>   updated_at      timestamptz NOT NULL DEFAULT now()
> );
> 
> CREATE INDEX IF NOT EXISTS idx_lane_phase ON qiphase.lane(phase_id);
> 
> -- ---------- artifacts (files) ----------
> CREATE TABLE IF NOT EXISTS qiphase.artifact (
>   artifact_id     bigserial PRIMARY KEY,
>   lane_id         text REFERENCES qiphase.lane(lane_id) ON DELETE SET NULL,
>   phase_id        text REFERENCES qiphase.phase(phase_id) ON DELETE SET NULL,
> 
>   artifact_type   qiphase.artifact_type NOT NULL DEFAULT 'OTHER',
>   artifact_code   text,                  -- e.g., T-0017 / D-0011 (nullable for legacy)
>   title           text NOT NULL,
>   path            text NOT NULL UNIQUE,   -- relative path
>   ext             text,
>   sha256          text,
>   bytes           bigint,
>   is_active       boolean NOT NULL DEFAULT true,
> 
>   created_at      timestamptz NOT NULL DEFAULT now(),
>   updated_at      timestamptz NOT NULL DEFAULT now()
> );
> 
> CREATE INDEX IF NOT EXISTS idx_artifact_phase ON qiphase.artifact(phase_id);
> CREATE INDEX IF NOT EXISTS idx_artifact_lane  ON qiphase.artifact(lane_id);
> CREATE INDEX IF NOT EXISTS idx_artifact_code  ON qiphase.artifact(artifact_code);
> 
> -- ---------- tags ----------
> CREATE TABLE IF NOT EXISTS qiphase.tag (
>   tag_id          bigserial PRIMARY KEY,
>   tag             text NOT NULL UNIQUE
> );
> 
> CREATE TABLE IF NOT EXISTS qiphase.artifact_tag (
>   artifact_id     bigint NOT NULL REFERENCES qiphase.artifact(artifact_id) ON DELETE CASCADE,
>   tag_id          bigint NOT NULL REFERENCES qiphase.tag(tag_id) ON DELETE CASCADE,
>   PRIMARY KEY (artifact_id, tag_id)
> );
> 
> -- ---------- links between artifacts ----------
> CREATE TABLE IF NOT EXISTS qiphase.artifact_link (
>   link_id         bigserial PRIMARY KEY,
>   from_artifact_id bigint NOT NULL REFERENCES qiphase.artifact(artifact_id) ON DELETE CASCADE,
>   to_artifact_id   bigint NOT NULL REFERENCES qiphase.artifact(artifact_id) ON DELETE CASCADE,
>   link_type       text NOT NULL DEFAULT 'references', -- flexible
>   notes           text,
>   created_at      timestamptz NOT NULL DEFAULT now()
> );
> 
> -- ---------- append-only logs ----------
> CREATE TABLE IF NOT EXISTS qiphase.artifact_log (
>   log_id          bigserial PRIMARY KEY,
>   artifact_id     bigint REFERENCES qiphase.artifact(artifact_id) ON DELETE SET NULL,
>   action          qiphase.log_action NOT NULL,
>   actor           text NOT NULL DEFAULT 'system',
>   details         jsonb NOT NULL DEFAULT '{}'::jsonb,
>   occurred_at     timestamptz NOT NULL DEFAULT now()
> );
> 
> COMMIT;
> ```
> 
> ### C) Migration 002 — seed phases/lanes (`migrations/002_seed_phases_lanes.sql`)
> This seeds what you already have *structurally* (you can expand later).
> ```sql
> BEGIN;
> 
> -- phases (edit names if you want them different)
> INSERT INTO qiphase.phase (phase_id, phase_name, core_theory, primary_objective)
> VALUES
> ('C-00','Foreclosure Record',NULL,'Build clean record + predicate'),
> ('C-01','Jurisdictional Defects','Void ab initio via TR 60(B)(6)','Vacate judgment / strike jurisdiction'),
> ('C-02','Evidence Preservation','Spoliation + preservation control','Lock evidence + chain of custody'),
> ('C-03','Post-Removal Liability','Tort + civil rights exposure','Liability + damages'),
> ('C-04','FCRA / Financial Misconduct','Federal statutory exposure','Deletion + statutory damages'),
> ('C-05','Accounting / Surplus','Mathematical impossibility + fee inflation','Forensics + recovery'),
> ('C-06','Civil Rights Exposure','ADA + access-to-court + discriminatory impact','Regulatory + civil rights track'),
> ('C-07','Settlement / Narrative Control','Narrative discipline + demand posture','Settlement leverage')
> ON CONFLICT (phase_id) DO NOTHING;
> 
> -- lanes
> INSERT INTO qiphase.lane (lane_id, phase_id, lane_name, sort_order)
> VALUES
> ('C-00.L01','C-00','Record Integrity',1),
> ('C-00.L02','C-00','Jurisdictional Predicate Review',2),
> ('C-00.L03','C-00','Appellate Preservation',3),
> 
> ('C-01.L01','C-01','Service Compliance Audit',1),
> ('C-01.L02','C-01','Notice Failures',2),
> ('C-01.L03','C-01','Legal Impact Assessment',3),
> 
> ('C-02.L01','C-02','Litigation Hold Control',1),
> ('C-02.L02','C-02','Spoliation Risk Register',2),
> ('C-02.L03','C-02','Evidence Intake Log',3),
> 
> ('C-03.L01','C-03','Writ Execution Validity',1),
> ('C-03.L02','C-03','Property Interference',2),
> ('C-03.L03','C-03','State Action Analysis',3),
> 
> ('C-04.L01','C-04','Furnisher Liability Mapping',1),
> ('C-04.L02','C-04','Bureau Dispute Tracking',2),
> 
> ('C-05.L01','C-05','Surplus Forensics',1),
> ('C-05.L02','C-05','Fee Inflation Audit',2),
> 
> ('C-06.L01','C-06','ADA Accommodation Record',1),
> ('C-06.L02','C-06','Discriminatory Impact Assessment',2),
> 
> ('C-07.L01','C-07','Settlement Framework',1),
> ('C-07.L02','C-07','Narrative Discipline',2)
> ON CONFLICT (lane_id) DO NOTHING;
> 
> COMMIT;
> ```
> 
> ### D) Migration runner (`scripts/migrate.sh`)
> ```bash
> #!/usr/bin/env bash
> set -euo pipefail
> 
> DB_URL="${DB_URL:-postgresql://qiphases:qiphases@localhost:54329/qiphases}"
> 
> psql "$DB_URL" -v ON_ERROR_STOP=1 -f migrations/001_init.sql
> psql "$DB_URL" -v ON_ERROR_STOP=1 -f migrations/002_seed_phases_lanes.sql
> 
> echo "Migrations applied ✅"
> ```
> 
> ---
> 
> ## 3) Folder index + logging script (what you actually need)
> 
> This walks `01_PHASES/`, infers phase/lane from folder names, infers code/type from filename prefixes, hashes files, upserts artifacts, and logs changes.
> 
> ### `scripts/index_repo.py`
> ```python
> import os, re, json, hashlib
> from pathlib import Path
> import psycopg2
> from psycopg2.extras import RealDictCursor
> 
> DB_URL = os.getenv("DB_URL", "postgresql://qiphases:qiphases@localhost:54329/qiphases")
> ROOT = Path(os.getenv("PHASES_ROOT", "01_PHASES")).resolve()
> 
> LANE_RE = re.compile(r"^(C-\d{2})\.(L\d{2})_")  # folder: C-01.L03_Name
> PHASE_RE = re.compile(r"^(C-\d{2})_")          # folder: C-01_Name
> 
> FILE_CODE_RE = re.compile(r"^(T-\d{4}|D-\d{4})_(.+)$")
> 
> def sha256_file(p: Path) -> str:
>     h = hashlib.sha256()
>     with p.open("rb") as f:
>         for chunk in iter(lambda: f.read(1024 * 1024), b""):
>             h.update(chunk)
>     return h.hexdigest()
> 
> def infer_artifact_type(code: str | None, ext: str) -> str:
>     if code and code.startswith("T-"): return "TASK"
>     if code and code.startswith("D-"): return "DOC"
>     if ext.lower() == ".csv": return "CSV"
>     if ext.lower() == ".canvas": return "CANVAS"
>     return "OTHER"
> 
> def infer_phase_lane(rel_parts):
>     phase_id = None
>     lane_id = None
>     for part in rel_parts:
>         m1 = PHASE_RE.match(part)
>         if m1:
>             phase_id = m1.group(1)
>         m2 = LANE_RE.match(part)
>         if m2:
>             phase_id = m2.group(1)
>             lane_id = f"{m2.group(1)}.{m2.group(2)}"
>     return phase_id, lane_id
> 
> def log(cur, artifact_id, action, details):
>     cur.execute(
>         """
>         INSERT INTO qiphase.artifact_log (artifact_id, action, actor, details)
>         VALUES (%s, %s, 'indexer', %s::jsonb)
>         """,
>         (artifact_id, action, json.dumps(details)),
>     )
> 
> def upsert_artifact(cur, phase_id, lane_id, path, title, code, a_type, ext, sha, size):
>     cur.execute("SELECT artifact_id, sha256, path, title FROM qiphase.artifact WHERE path=%s", (path,))
>     row = cur.fetchone()
> 
>     if row is None:
>         cur.execute(
>             """
>             INSERT INTO qiphase.artifact
>               (phase_id, lane_id, path, title, artifact_code, artifact_type, ext, sha256, bytes)
>             VALUES
>               (%s,%s,%s,%s,%s,%s,%s,%s,%s)
>             RETURNING artifact_id
>             """,
>             (phase_id, lane_id, path, title, code, a_type, ext, sha, size),
>         )
>         artifact_id = cur.fetchone()["artifact_id"]
>         log(cur, artifact_id, "CREATED", {"path": path, "sha256": sha})
>         log(cur, artifact_id, "IMPORTED", {"phase_id": phase_id, "lane_id": lane_id})
>         return
> 
>     artifact_id = row["artifact_id"]
>     changes = {}
>     if row["sha256"] != sha:
>         changes["sha256"] = {"old": row["sha256"], "new": sha}
>     if row["title"] != title:
>         changes["title"] = {"old": row["title"], "new": title}
> 
>     if changes:
>         cur.execute(
>             """
>             UPDATE qiphase.artifact
>             SET phase_id=%s, lane_id=%s, title=%s, artifact_code=%s, artifact_type=%s,
>                 ext=%s, sha256=%s, bytes=%s, updated_at=now()
>             WHERE artifact_id=%s
>             """,
>             (phase_id, lane_id, title, code, a_type, ext, sha, size, artifact_id),
>         )
>         log(cur, artifact_id, "UPDATED", changes)
>     else:
>         # keep phase/lane fresh
>         cur.execute(
>             """
>             UPDATE qiphase.artifact
>             SET phase_id=%s, lane_id=%s, updated_at=now()
>             WHERE artifact_id=%s
>             """,
>             (phase_id, lane_id, artifact_id),
>         )
> 
> def main():
>     if not ROOT.exists():
>         raise SystemExit(f"PHASES_ROOT not found: {ROOT}")
> 
>     conn = psycopg2.connect(DB_URL)
>     conn.autocommit = False
> 
>     with conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
>         for p in ROOT.rglob("*"):
>             if p.is_dir():
>                 continue
>             if p.name.startswith("."):
>                 continue
> 
>             rel = p.relative_to(ROOT).as_posix()
>             phase_id, lane_id = infer_phase_lane(p.relative_to(ROOT).parts)
> 
>             # infer code/title
>             stem = p.stem
>             ext = p.suffix
>             code = None
>             title = stem
> 
>             m = FILE_CODE_RE.match(stem)
>             if m:
>                 code = m.group(1)
>                 title = m.group(2)
> 
>             a_type = infer_artifact_type(code, ext)
>             sha = sha256_file(p)
>             size = p.stat().st_size
> 
>             upsert_artifact(cur, phase_id, lane_id, rel, title, code, a_type, ext, sha, size)
> 
>         conn.commit()
>     print("Index complete ✅")
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ### `scripts/index.sh`
> ```bash
> #!/usr/bin/env bash
> set -euo pipefail
> 
> export DB_URL="${DB_URL:-postgresql://qiphases:qiphases@localhost:54329/qiphases}"
> export PHASES_ROOT="${PHASES_ROOT:-01_PHASES}"
> 
> python3 scripts/index_repo.py
> ```
> 
> ---
> 
> ## 4) One-time “fix the tree” patch list (fast)
> 
> Apply these changes manually or via a rename script:
> 
> ### Create the missing lanes + files
> - Create:
>   - `01_PHASES/C-01_Jurisdictional_Defects/C-01.L03_Legal_Impact_Assessment/`
>   - `01_PHASES/C-02_Evidence_Preservation/C-02.L03_Evidence_Intake_Log/`
> 
> - Add files:
>   - `.../C-01.L03.../T-0018_TR60B6_void_ab_initio_argument_map.md`
>   - `.../C-01.L03.../D-0013_Jurisdictional_defect_consequence_matrix.md`
>   - `.../C-01.L03.../T-0019_Appellate_posture_and_standard_of_review_notes.md`
>   - `.../C-01.L03.../D-0014_Relief_requested_remedy_menu_vacate_stay_sanctions.md`
>   - `.../C-02.L03.../T-0020_Evidence_intake_register.md`
>   - `.../C-02.L03.../D-0015_Chain_of_custody_template.md`
>   - `.../C-02.L03.../T-0021_File_hashing_and_immutability_ledger.md`
>   - `.../C-02.L03.../D-0016_Evidence_intake_SOP_and_naming_rules.md`
> 
> ### Delete duplicates
> - Delete folder: `01_PHASES/C-07_Settlement_Narrative_Control/06.01_Settlement_Framework/`
> - Delete files:
>   - `.../C-07.L01.../Settlement demand model.md`
>   - `.../C-06.L01.../Accommodation request log.md`
>   - any unprefixed duplicate DOJ excerpt if `D-0011_...` exists
> 
> ---
> 
> ## 5) “Happy go lucky may a phase v3” ✅
> If you mean: **treat `1_phases-v3-LOCKED.csv` as authoritative and stop touching it**, do this:
> - Keep `1_phases-v3-LOCKED.csv` as read-only.
> - Only ever write new deltas to:
>   - `phase_changes_log.csv` (or into Postgres via `artifact_log`)
> - If you need a working copy, create:
>   - `1_phases-working.csv` (never overwrite locked)
> 
> ---
> 
> ## If you re-upload the expired files…
> …I’ll merge my schema/scripts **into your existing `DATABASE_SCHEMA_MIGRATION_V2.sql` + lock doc** instead of replacing them, and I’ll align IDs exactly to your `1_phases-v3-LOCKED.csv`.
> 
> For now, you can run this locally in under 5 minutes:
> 1) `docker compose up -d`  
> 2) `bash scripts/migrate.sh`  
> 3) `bash scripts/index.sh`
> 
> That gets you: **local Postgres + migrations + folder indexing + change logs**.

### User
> ```markdown
> . 📂 90_ADMIN
> ├── 📄 DATABASE_SCHEMA_MIGRATION_V2.sql
> ├── 📄 DATABASE_SCHEMA_MIGRATION_V3.sql
> ├── 📄 LITIGATION_SCHEMA_LOCK.md
> ├── 📄 _00_ADMIN.md
> └── 📂 analysis/
> │  └── 📂 00_Strategy/
> │    ├── 📄 20260201_STRATEGY_Auto_Save_D0015.canvas
> │    ├── 📄 20260201_STRATEGY_Auto_Save_D0016.canvas
> │    ├── 📄 20260207_STRATEGY_Auto_Save_D0009.canvas
> │    ├── 📄 20260207_STRATEGY_Auto_Save_D0010.canvas
> │    ├── 📄 20260207_STRATEGY_Auto_Save_D0012.canvas
> │    ├── 📄 20260207_STRATEGY_Auto_Save_D0013.canvas
> │    ├── 📄 20260207_STRATEGY_Auto_Save_D0134.canvas
> │    ├── 📄 20260207_STRATEGY_Auto_Save_D0152.canvas
> │    ├── 📄 20260207_STRATEGY_Auto_Save_D0153.canvas
> │  ├── 📄 20260210_DATA_FCFCU_Case_Master_GS1.csv
> │  ├── 📄 20260210_REPORT_AI_Analysis_Grok_2.pdf
> │  ├── 📄 20260212_NOTES_Dictated_Case_Review.txt
> │  ├── 📄 Timeline_Inventory.csv
> │  ├── 📄 _analysis.md
> └── 📂 logs/
> │  ├── 📄 20260203_C01_FORECL_FCFCU_DOC_D0551.pdf
> │  ├── 📄 20260203_C01_FORECL_FCFCU_ORDER_D0549.pdf
> │  ├── 📄 20260203_C01_FORECL_ORDER_D0550.pdf
> │  ├── 📄 20260210_REPORT_AI_Analysis_Grok.pdf
> │  ├── 📄 Service_Log.md
> │  ├── 📄 _05_LOGS.md
> ├── 📄 migrate_phases_repo_v3.py
> └── 📂 references/
> │  ├── 📄 1975_CIVIL_RIGHTS_.md
> │  ├── 📄 1977_19_PROCEDURAL_.md
> │  ├── 📄 1980s_FAIR_HOUSING_ACT_BREACH__EXCLUSIONARY_ZONING__.md
> │  ├── 📄 1985_PROCEDURAL_.md
> │  ├── 📄 2000_PROCEDURAL_.md
> │  ├── 📄 2009_Ca_PROCEDURAL_.md
> │  ├── 📄 2009_FAIR_HOUSING_ACT_BREACH__PATTERN_OR_PRACTICE_OF_REDLINING__.md
> │  ├── 📄 2010_20_ADA_.md
> │  ├── 📄 2020_FAIR_HOUSING_ACT_BREACH__REASONABLE_ACCOMMODATION_FAILURE__.md
> │  ├── 📄 2026_REF_FCRA_Remedies.pdf
> │  ├── 📄 99_CASE_SCHEMA.md
> │  ├── 📄 April 20_FAIR_HOUSING_ACT_BREACH__RACE__NATIONAL_ORIGIN___HOSTILE_HOUSING_ENVIRONMENT_.md
> │  ├── 📄 April 20_FAIR_HOUSING_ACT_BREACH__SEXUAL_HARASSMENT__.md
> │  ├── 📄 August 1_FAIR_HOUSING_ACT_BREACH__ACCESSIBILITY_REQUIREMENTS__.md
> │  ├── 📄 August 2_FAILURE_TO_PROVIDE_EQUAL_MAINTENANCE_SERVICES__REO_DWELLINGS__.md
> │  ├── 📄 August 2_FAIR_HOUSING_ACT_BREACH__GENDER___SEXUAL_HARASSMENT_.md
> │  ├── 📄 August 2_POTENTIAL_IC___32_30_10_14_VIOLATION__SURPLUS_MISMANAGEMENT__.md
> │  ├── 📄 Early 20_ADA_.md
> │  ├── 📄 February_FAIR_HOUSING_ACT_BREACH__DISABILITY__FAMILIAL_STATUS__.md
> │  ├── 📄 Google Sheets Validation Guide.md
> │  ├── 📄 January _DUE_PROCESS_FAILURE___NOTICE_DEFICIENCY_.md
> │  ├── 📄 January _FAIR_HOUSING_ACT_BREACH__FAMILIAL_STATUS___OCCUPANCY_POLICIES_.md
> │  ├── 📄 July 201_FAIR_HOUSING_ACT_BREACH__INTENTIONAL_DISCRIMINATION___DISPARATE_IMPACT__.md
> │  ├── 📄 June 8, _ADA_.md
> │  ├── 📄 June 9, _PROCEDURAL_.md
> │  ├── 📄 March 20_FAIR_HOUSING_ACT_BREACH__FAMILIAL_STATUS__.md
> │  ├── 📄 March 20_FAIR_HOUSING_ACT_BREACH__RACE__COLOR___APPRAISAL_BIAS_.md
> │  ├── 📄 March 5,_DUE_PROCESS_FAILURE___DEFECTIVE_SERVICE_.md
> │  ├── 📄 March 5,_PROCEDURAL_.md
> │  ├── 📄 May 28, _FORECLOSURE_.md
> │  ├── 📄 May 28, _PROCEDURAL_.md
> │  ├── 📄 Not in s_ADA_.md
> │  ├── 📄 Not in s_DISCRIMINATORY_ADVERTISING_.md
> │  ├── 📄 Not in s_DUE_PROCESS_VIOLATION__STANDARD_OF_PROOF__.md
> │  ├── 📄 Not in s_FAIR_HOUSING_ACT_BREACH__REASONABLE_ACCOMMODATION_FAILURE__.md
> │  ├── 📄 Not in s_PROCEDURAL_.md
> │  ├── 📄 Not in s_SECTION_504_BREACH___FAILURE_TO_PROVIDE_INTERPRETER_.md
> │  ├── 📄 Not in s_UNCONSTITUTIONAL_PRESUMPTION__VESTING_OF_TITLE__.md
> │  ├── 📄 November_FAIR_HOUSING_ACT_BREACH__REASONABLE_ACCOMMODATION_DENIAL__.md
> │  ├── 📄 November_FRAUD_ON_THE_COURT___MATERIAL_MISREPRESENTATION_.md
> │  ├── 📄 October _FAIR_HOUSING_ACT_BREACH__RACE__NATIONAL_ORIGIN___DISCRIMINATORY_MAINTENANCE_.md
> │  ├── 📄 October _FAIR_HOUSING_ACT_BREACH__RACE___REDLINING_.md
> │  ├── 📄 Preforec_ADA_.md
> │  ├── 📄 Septembe_FAIR_HOUSING_ACT_BREACH__RACE___ARBITRARY_CRIMINAL_HISTORY_POLICIES_.md
> │  ├── 📄 _references.md
> │  ├── 📄 rules.md
> │  ├── 📄 schema.json
> └── 📂 schema_headers/
> │  ├── 📄 TEMPLATE_claim.csv
> │  ├── 📄 TEMPLATE_doc.csv
> │  ├── 📄 TEMPLATE_doc_claim.csv
> │  ├── 📄 TEMPLATE_event.csv
> │  ├── 📄 TEMPLATE_event_claim.csv
> │  ├── 📄 TEMPLATE_event_doc.csv
> │  ├── 📄 TEMPLATE_exhibit.csv
> │  ├── 📄 TEMPLATE_filing.csv
> │  ├── 📄 TEMPLATE_lane.csv
> │  ├── 📄 TEMPLATE_phase.csv
> │  ├── 📄 TEMPLATE_task.csv
> │  ├── 📄 TEMPLATE_task_doc.csv
> │  ├── 📄 TEMPLATE_task_event.csv
> ├── 📄 schema_integrity_audit.py
> └── 📂 templates/
> │  ├── 📄 Notebooklm-prompts.md
> │  ├── 📄 _templates.md
> │  └── 📂 affidavits/
> │    ├── 📄 EMERGENCY SUPPLEMENTAL DECLARATION.gdoc
> │    ├── 📄 TPL_Affidavit_ADA_Disability.md
> │    ├── 📄 TPL_Affidavit_Character.md
> │    ├── 📄 TPL_Affidavit_Community_Service.md
> │    ├── 📄 TPL_Affidavit_Credibility.md
> │    ├── 📄 TPL_Affidavit_Language_Updates.md
> │    ├── 📄 TPL_Affidavit_Observations.md
> │    ├── 📄 TPL_Affidavit_Verified_Defendant.md
> │    ├── 📄 TPL_Declaration_Gender_Identity_Clarification.md
> │    ├── 📄 TPL_housing_affidavit.md
> │    ├── 📄 WF5.01.010__Credibility_Affidavit.md
> │    ├── 📄 WF5.01.010__Gender_Identity_Clarification.md
> │    ├── 📄 WF5.01.010__updated_affidavit_language.md
> │    ├── 📄 WF5.01.010__verified_affidavit_of_defendant.md
> │    ├── 📄 _affidavits.md
> │  └── 📂 binders/
> │    ├── 📄 TPL_Binder_Section_Cover.md
> │    ├── 📄 TPL_Binder_Section_Index.md
> │    ├── 📄 _binders.md
> │  └── 📂 exhibits/
> │    ├── 📄 TPL_Exhibits_Lists.md
> │    ├── 📄 _exhibits.md
> │  └── 📂 front_matter/
> │    ├── 📄 FRONT_MATTER_MIGRATION_INSTRUCTION.md
> │    ├── 📄 _front_matter.md
> │  └── 📂 internal/
> │    ├── 📄 TPL_settlement_letter_draft.md
> │    ├── 📄 _internal.md
> │  └── 📂 motions/
> │    ├── 📄 Copy of  EMERGENCY MOTION TO PRESERVE AND ACCOUNT FOR SURPLUS FUNDS.gdoc
> │    ├── 📄 EMERGENCY MOTION TO PRESERVE AND ACCOUNT FOR SURPLUS FUNDS.gdoc
> │    ├── 📄 TPL_emergency_stay_of_writ.md
> │    ├── 📄 TPL_vacate_void_judgment.md
> │    ├── 📄 _10_motions.md
> │    ├── 📄 _motions.md
> │  └── 📂 orders/
> │    ├── 📄 TPL_Proposed_Order.md
> │    ├── 📄 TPL_proposed_order_emergency_stay.md
> │    ├── 📄 TPL_proposed_order_motion_to_vacate.md
> │    ├── 📄 _orders.md
> │  └── 📂 outreach/
> │    ├── 📄 TPL_Advocate_Outreach.md
> │    ├── 📄 TPL_Attorney_Brief.md
> │    ├── 📄 _outreach.md
> │  └── 📂 packets/
> │    ├── 📄 TPL_ADA_Packet.md
> │    ├── 📄 TPL_Handup_Packet_Note.md
> │    ├── 📄 TPL_attorney_intake_packet_executive.md
> │    └── 📄 _packets.md
> ```, doe this help or what? can we run a sql server local and extension or soemthign in the ide ot edit or should i go ahead and add a database but im not using supa im at max.

### Assistant
> You *didn’t* “do a database” in the sense of running one — you drafted **schema + migrations** (`DATABASE_SCHEMA_MIGRATION_V2/V3.sql`) as the foundation for **logging + queryability**. That’s why it feels like “wait when did we do this?” — it was design work, not deployment.
> 
> You said “Postgres local” and “I’m not dealing with Supabase.” Good. Local Postgres in Docker is the least-friction option.
> 
> Below is a **clean, locked path forward**:
> 
> ---
> 
> ## 1) What’s missing in your repo right now (and what to add)
> 
> ### Missing lane folders + tasks
> 
> #### **C-01.L03_Legal_Impact_Assessment** (missing tasks)
> Add these files (next task IDs after T-0017):
> 
> - `T-0018_Defect_to_Rule_Mapping_Matrix.md`
> - `T-0019_TR60B6_Void_Judgment_Argument_Outline.md`
> - `T-0020_Remedies_and_Relief_Request_Map.md`
> 
> #### **C-02.L03_Evidence_Intake_Log** (lane exists in schema intent, missing in tree)
> Create the lane folder and add:
> 
> - `T-0021_Evidence_Intake_Log_Template.md`
> - `T-0022_Chain_of_Custody_and_Source_Metadata.md`
> - `T-0023_Hash_Baseline_and_Immutability_Procedure.md`
> 
> > These aren’t “generic placeholders” — they map directly to what you keep needing: rule mapping, void impact, remedy framing, and a real evidence intake + custody + hash discipline so nobody can play games with authenticity later.
> 
> ---
> 
> ## 2) What to delete / consolidate (rando stuff)
> 
> You’ve got **duplicates-by-content** and **duplicates-by-role**:
> 
> ### In `C-06` (Civil Rights Exposure)
> You have **both**:
> - `Accommodation request log.md` and `T-0016_Accommodation request log.md`
> 
> Pick one pattern. Since you’re standardizing, keep the **T- prefixed** one and delete/merge the unprefixed duplicate:
> - ✅ keep: `T-0016_Accommodation request log.md`
> - ❌ delete after merge: `Accommodation request log.md`
> 
> ### In `C-07` (Settlement Narrative Control)
> You have both:
> - `Settlement demand model.md` and `T-0017_Settlement demand model.md`
> 
> Same rule:
> - ✅ keep: `T-0017_Settlement demand model.md`
> - ❌ delete after merge: `Settlement demand model.md`
> 
> ### In `C-04`
> You have duplicate copy of `30_Full_TriMerge_2025_12_tradelines.csv` in two places.
> That’s fine **only if** one is “raw immutable” and one is “working copy.” Right now it’s ambiguous.
> 
> Do this:
> - Keep the one in `C-04.L01_Furnisher_Liability_Mapping/` as **immutable source** (rename it to include `_RAW_IMMUTABLE`)
> - Keep the one in `C-04.L02_Bureau_Dispute_Tracking/` as **working copy** (rename include `_WORKING`)
> 
> If you won’t enforce that rule, delete one — duplicated evidence without a rule turns into future contradictions.
> 
> ---
> 
> ## 3) Local Postgres: minimal setup (Docker) + IDE editing
> 
> ### `docker-compose.yml` (drop this in repo root or `90_ADMIN/db/`)
> ```yaml
> services:
>   postgres:
>     image: postgres:16
>     container_name: litigation_pg
>     environment:
>       POSTGRES_USER: litigation
>       POSTGRES_PASSWORD: litigation
>       POSTGRES_DB: litigation_db
>     ports:
>       - "54329:5432"
>     volumes:
>       - litigation_pg_data:/var/lib/postgresql/data
> volumes:
>   litigation_pg_data:
> ```
> 
> ### Start it
> ```bash
> docker compose up -d
> ```
> 
> ### Recommended VS Code extensions
> - **SQLTools** + **SQLTools PostgreSQL/Redshift Driver**
> - or “PostgreSQL” extension (any that lets you browse schemas + run queries)
> 
> Connection details:
> - Host: `localhost`
> - Port: `54329`
> - DB: `litigation_db`
> - User: `litigation`
> - Password: `litigation`
> 
> ---
> 
> ## 4) Migration scripts (Postgres local)
> 
> You already have:
> - `/mnt/data/DATABASE_SCHEMA_MIGRATION_V3.sql` (use this as the **current canonical**)
> 
> Put it in repo as:
> - `90_ADMIN/DATABASE_SCHEMA_MIGRATION_V3.sql`
> 
> ### `90_ADMIN/db/01_apply_schema.sh`
> ```bash
> #!/usr/bin/env bash
> set -euo pipefail
> 
> PGHOST="${PGHOST:-localhost}"
> PGPORT="${PGPORT:-54329}"
> PGDATABASE="${PGDATABASE:-litigation_db}"
> PGUSER="${PGUSER:-litigation}"
> PGPASSWORD="${PGPASSWORD:-litigation}"
> 
> export PGHOST PGPORT PGDATABASE PGUSER PGPASSWORD
> 
> psql -v ON_ERROR_STOP=1 -f "90_ADMIN/DATABASE_SCHEMA_MIGRATION_V3.sql"
> 
> echo "✅ Schema applied to ${PGDATABASE} on ${PGHOST}:${PGPORT}"
> ```
> 
> Run:
> ```bash
> bash 90_ADMIN/db/01_apply_schema.sh
> ```
> 
> ---
> 
> ## 5) Seed the DB from your locked CSV (phases/lanes/tasks)
> 
> Your locked file is:
> - `/mnt/data/1_phases-v3-LOCKED.csv`
> You should keep it in repo at:
> - `01_PHASES/1_phases-v3-LOCKED.csv`
> 
> ### `90_ADMIN/db/02_seed_from_locked_csv.py`
> This seeds **phase/lane/task/doc** rows based on the CSV hierarchy and your ID conventions.
> 
> ```python
> #!/usr/bin/env python3
> import os
> import pandas as pd
> import psycopg2
> from psycopg2.extras import execute_values
> 
> CSV_PATH = os.environ.get("CSV_PATH", "01_PHASES/1_phases-v3-LOCKED.csv")
> 
> DB = {
>     "host": os.environ.get("PGHOST", "localhost"),
>     "port": int(os.environ.get("PGPORT", "54329")),
>     "dbname": os.environ.get("PGDATABASE", "litigation_db"),
>     "user": os.environ.get("PGUSER", "litigation"),
>     "password": os.environ.get("PGPASSWORD", "litigation"),
> }
> 
> def main():
>     df = pd.read_csv(CSV_PATH).fillna("")
>     # expected columns: id,name,parent_id,level,type,status,core_theory,primary_objective,notes,locked_id
> 
>     phases = []
>     lanes = []
>     tasks = []
>     docs = []
> 
>     for _, r in df.iterrows():
>         rid = str(r["id"]).strip()
>         name = str(r["name"]).strip()
>         parent_id = str(r["parent_id"]).strip() or None
>         level = str(r["level"]).strip()
>         rtype = str(r["type"]).strip()
>         status = str(r["status"]).strip() or "Active"
>         core_theory = str(r["core_theory"]).strip()
>         primary_objective = str(r["primary_objective"]).strip()
>         notes = str(r["notes"]).strip()
>         locked_id = str(r.get("locked_id", "")).strip()
> 
>         # We map by "level" primarily.
>         if level == "phase":
>             phases.append((rid, name, status, core_theory, primary_objective, notes))
>         elif level == "lane":
>             # parent_id must be phase id
>             lanes.append((locked_id or rid, parent_id, name, status, core_theory, primary_objective, notes))
>         elif level == "task":
>             # parent_id must be lane id (like C-00.01)
>             # store task_id as locked_id (T-0001) where available; else derive
>             task_id = locked_id or rid
>             tasks.append((task_id, parent_id, name, status, core_theory, primary_objective, notes))
>         elif level == "doc":
>             doc_id = locked_id or rid
>             docs.append((doc_id, parent_id, name, status, notes))
>         else:
>             # ignore unknown levels
>             pass
> 
>     conn = psycopg2.connect(**DB)
>     conn.autocommit = False
>     try:
>         with conn.cursor() as cur:
>             # phases
>             execute_values(cur, """
>                 INSERT INTO phase (phase_id, name, status, core_theory, primary_objective, notes)
>                 VALUES %s
>                 ON CONFLICT (phase_id) DO UPDATE SET
>                   name=EXCLUDED.name,
>                   status=EXCLUDED.status,
>                   core_theory=EXCLUDED.core_theory,
>                   primary_objective=EXCLUDED.primary_objective,
>                   notes=EXCLUDED.notes;
>             """, phases)
> 
>             # lanes (lane_id is your locked_id like C-00.L01)
>             execute_values(cur, """
>                 INSERT INTO lane (lane_id, phase_id, name, status, core_theory, primary_objective, notes)
>                 VALUES %s
>                 ON CONFLICT (lane_id) DO UPDATE SET
>                   name=EXCLUDED.name,
>                   status=EXCLUDED.status,
>                   core_theory=EXCLUDED.core_theory,
>                   primary_objective=EXCLUDED.primary_objective,
>                   notes=EXCLUDED.notes;
>             """, lanes)
> 
>             # tasks
>             execute_values(cur, """
>                 INSERT INTO task (task_id, lane_id, name, status, core_theory, primary_objective, notes)
>                 VALUES %s
>                 ON CONFLICT (task_id) DO UPDATE SET
>                   name=EXCLUDED.name,
>                   status=EXCLUDED.status,
>                   core_theory=EXCLUDED.core_theory,
>                   primary_objective=EXCLUDED.primary_objective,
>                   notes=EXCLUDED.notes;
>             """, tasks)
> 
>             # docs (optional; may be sparse in CSV)
>             if docs:
>                 execute_values(cur, """
>                     INSERT INTO doc (doc_id, lane_id, title, status, notes)
>                     VALUES %s
>                     ON CONFLICT (doc_id) DO UPDATE SET
>                       title=EXCLUDED.title,
>                       status=EXCLUDED.status,
>                       notes=EXCLUDED.notes;
>                 """, docs)
> 
>         conn.commit()
>         print(f"✅ Seeded phases={len(phases)}, lanes={len(lanes)}, tasks={len(tasks)}, docs={len(docs)} from {CSV_PATH}")
>     except Exception:
>         conn.rollback()
>         raise
>     finally:
>         conn.close()
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> Run it:
> ```bash
> python 90_ADMIN/db/02_seed_from_locked_csv.py
> ```
> 
> ---
> 
> ## 6) Repo “finish it” script: create missing lanes + files + remove duplicates
> 
> This script does three things:
> 1) creates missing lane folders
> 2) creates missing task files
> 3) flags duplicates you should merge/delete (and can auto-delete if you flip a switch)
> 
> ### `90_ADMIN/migrate_repo_finish_v3.py`
> ```python
> #!/usr/bin/env python3
> from pathlib import Path
> 
> ROOT = Path("01_PHASES")
> 
> # What we are adding (the concrete missing items you called out)
> ADD = {
>     "C-01_Jurisdictional_Defects/C-01.L03_Legal_Impact_Assessment": [
>         "T-0018_Defect_to_Rule_Mapping_Matrix.md",
>         "T-0019_TR60B6_Void_Judgment_Argument_Outline.md",
>         "T-0020_Remedies_and_Relief_Request_Map.md",
>     ],
>     "C-02_Evidence_Preservation/C-02.L03_Evidence_Intake_Log": [
>         "T-0021_Evidence_Intake_Log_Template.md",
>         "T-0022_Chain_of_Custody_and_Source_Metadata.md",
>         "T-0023_Hash_Baseline_and_Immutability_Procedure.md",
>     ],
> }
> 
> # Duplicates to resolve (manual merge -> then delete the loser)
> DUPES = [
>     ("01_PHASES/C-06_Civil_Rights_Exposure/C-06.L01_ADA_Accommodation_Record/Accommodation request log.md",
>      "01_PHASES/C-06_Civil_Rights_Exposure/C-06.L01_ADA_Accommodation_Record/T-0016_Accommodation request log.md"),
>     ("01_PHASES/C-07_Settlement_Narrative_Control/C-07.L01_Settlement_Framework/Settlement demand model.md",
>      "01_PHASES/C-07_Settlement_Narrative_Control/C-07.L01_Settlement_Framework/T-0017_Settlement demand model.md"),
> ]
> 
> def ensure_file(path: Path, title: str):
>     if path.exists():
>         return
>     path.write_text(f"# {title}\n\n## Purpose\n\n## Inputs\n\n## Steps\n\n## Output / Artifact\n\n## Notes\n", encoding="utf-8")
> 
> def main():
>     # 1) Create missing lanes + tasks
>     for rel_lane, files in ADD.items():
>         lane_path = ROOT / rel_lane
>         lane_path.mkdir(parents=True, exist_ok=True)
>         for fn in files:
>             ensure_file(lane_path / fn, fn.replace("_", " ").replace(".md", ""))
> 
>     # 2) Print duplicate pairs to resolve
>     print("\n=== DUPLICATES TO MERGE THEN DELETE (keep the T- version) ===")
>     for a, b in DUPES:
>         pa, pb = Path(a), Path(b)
>         print(f"- Loser (merge/delete): {pa} {'[MISSING]' if not pa.exists() else ''}")
>         print(f"  Winner (keep):        {pb} {'[MISSING]' if not pb.exists() else ''}")
> 
>     print("\n✅ v3 finish pass complete (missing lanes/tasks created).")
>     print("Next: merge duplicate content into the T- file, then delete the loser file.")
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> Run:
> ```bash
> python 90_ADMIN/migrate_repo_finish_v3.py
> ```
> 
> ---
> 
> ## 7) Answering your “SQL server local?” question
> 
> Don’t use Microsoft SQL Server here. It adds friction and gives you nothing you need.
> 
> Use **Postgres local in Docker** + VS Code extension. That gets you:
> - a real DB for logging events/tasks/docs
> - easy schema edits
> - no Supabase quotas
> - portable (works on any machine)
> 
> If later you want “file-based and ultra-light,” then SQLite is the alternative — but you explicitly want **Postgres**, and your schema/migrations are already in that direction.
> 
> ---
> 
> ## The only “next actions” you need tonight
> 
> 1) `docker compose up -d`  
> 2) `bash 90_ADMIN/db/01_apply_schema.sh`  
> 3) `python 90_ADMIN/db/02_seed_from_locked_csv.py`  
> 4) `python 90_ADMIN/migrate_repo_finish_v3.py`  
> 
> That gets you: **local DB running + schema applied + seeded + missing tasks created**.
> 
> If you want, next step after sleep is the **sync logger** (watch folder changes → insert doc rows with hash + timestamp). But you don’t need that to “move on” tonight.

### User
> yes, sync logger please. one click commit and push,

### Assistant
> Yep. We can do this **local-first** with **Postgres** (or SQLite if you want ultra-simple), and a **one-click “sync logger”** that:
> 
> 1) validates repo structure  
> 2) writes an append-only log entry (CSV + Markdown)  
> 3) stages changes  
> 4) commits with a clean message  
> 5) pushes to origin
> 
> Also: your earlier uploaded SQL/PY files are **expired on my side**, so I can’t read them right now. If you want me to *wire this exactly* to `DATABASE_SCHEMA_MIGRATION_V3.sql` + your existing `schema_integrity_audit.py`, re-upload them. **But you don’t need that to start**—the scripts below work today.
> 
> ---
> 
> ## Decision: Postgres local (recommended) vs SQLite (fastest)
> 
> ### If you want “real DB” but local-only:
> **Postgres in Docker**. Zero Supabase. Clean.
> 
> ### If you want “I’m tired, don’t make me babysit services”:
> **SQLite**. No daemon, one file, works everywhere.
> 
> Given your current state: **SQLite now, Postgres later** is the lowest-friction path. But I’ll give you Postgres anyway since you asked.
> 
> ---
> 
> ## A. Local Postgres in Docker (copy/paste)
> 
> Create `90_ADMIN/db/docker-compose.yml`:
> ```yaml
> services:
>   postgres:
>     image: postgres:16
>     container_name: qicase_pg
>     environment:
>       POSTGRES_USER: qicase
>       POSTGRES_PASSWORD: qicase
>       POSTGRES_DB: qicase
>     ports:
>       - "54329:5432"
>     volumes:
>       - qicase_pgdata:/var/lib/postgresql/data
> volumes:
>   qicase_pgdata:
> ```
> 
> Run:
> ```bash
> docker compose -f 90_ADMIN/db/docker-compose.yml up -d
> ```
> 
> Connect:
> ```bash
> psql "postgres://qicase:qicase@localhost:54329/qicase"
> ```
> 
> ---
> 
> ## B. Migration runner (Postgres) — “apply all migrations in order”
> 
> Folder convention:
> ```
> 90_ADMIN/db/migrations/
>   001_init.sql
>   002_schema_v2.sql
>   003_schema_v3.sql
> ```
> 
> Create `90_ADMIN/db/apply_migrations.sh`:
> ```bash
> #!/usr/bin/env bash
> set -euo pipefail
> 
> DB_URL="${DB_URL:-postgres://qicase:qicase@localhost:54329/qicase}"
> MIG_DIR="${MIG_DIR:-90_ADMIN/db/migrations}"
> 
> echo "DB_URL=$DB_URL"
> echo "MIG_DIR=$MIG_DIR"
> 
> # ensure migrations table exists
> psql "$DB_URL" -v ON_ERROR_STOP=1 <<'SQL'
> CREATE TABLE IF NOT EXISTS schema_migrations (
>   id SERIAL PRIMARY KEY,
>   filename TEXT UNIQUE NOT NULL,
>   applied_at TIMESTAMPTZ NOT NULL DEFAULT now()
> );
> SQL
> 
> for f in $(ls -1 "$MIG_DIR"/*.sql 2>/dev/null | sort); do
>   base="$(basename "$f")"
>   applied="$(psql "$DB_URL" -tAc "SELECT 1 FROM schema_migrations WHERE filename='$base' LIMIT 1;")"
>   if [[ "$applied" == "1" ]]; then
>     echo "SKIP  $base"
>   else
>     echo "APPLY $base"
>     psql "$DB_URL" -v ON_ERROR_STOP=1 -f "$f"
>     psql "$DB_URL" -v ON_ERROR_STOP=1 -c "INSERT INTO schema_migrations(filename) VALUES('$base');"
>   fi
> done
> 
> echo "Done."
> ```
> 
> Make executable:
> ```bash
> chmod +x 90_ADMIN/db/apply_migrations.sh
> ```
> 
> Run:
> ```bash
> DB_URL="postgres://qicase:qicase@localhost:54329/qicase" 90_ADMIN/db/apply_migrations.sh
> ```
> 
> ---
> 
> ## C. “Sync Logger” — one click commit + push
> 
> ### What it does (tight + practical)
> - Creates/updates:
>   - `90_ADMIN/logs/sync_log.csv` (append-only)
>   - `90_ADMIN/logs/sync_log.md` (append-only)
> - Auto-commit message like:
>   - `sync: 2026-02-16 22:14 CT | 7 files | C-01.L01`
> - Pushes to `origin main` (or your current branch)
> 
> Create `90_ADMIN/qi_sync.py`:
> ```python
> #!/usr/bin/env python3
> from __future__ import annotations
> 
> import csv
> import os
> import re
> import subprocess
> from dataclasses import dataclass
> from datetime import datetime, timezone
> from pathlib import Path
> from typing import List, Optional
> 
> REPO_ROOT = Path(__file__).resolve().parents[1]  # 90_ADMIN/ -> repo root
> LOG_DIR = REPO_ROOT / "90_ADMIN" / "logs"
> LOG_CSV = LOG_DIR / "sync_log.csv"
> LOG_MD = LOG_DIR / "sync_log.md"
> 
> DEFAULT_BRANCH = os.environ.get("QI_BRANCH", "").strip()  # optional override
> REMOTE = os.environ.get("QI_REMOTE", "origin").strip()
> 
> LANE_HINT_RE = re.compile(r"(?P<phase>C-\d{2})\.(?P<lane>L\d{2})", re.IGNORECASE)
> 
> 
> @dataclass
> class GitStatus:
>     changed_paths: List[str]
>     branch: str
> 
> 
> def run(cmd: List[str], cwd: Path = REPO_ROOT, check: bool = True) -> str:
>     p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
>     if check and p.returncode != 0:
>         raise RuntimeError(
>             f"Command failed: {' '.join(cmd)}\n"
>             f"exit={p.returncode}\nSTDOUT:\n{p.stdout}\nSTDERR:\n{p.stderr}"
>         )
>     return (p.stdout or "").strip()
> 
> 
> def get_branch() -> str:
>     b = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
>     if DEFAULT_BRANCH:
>         return DEFAULT_BRANCH
>     return b
> 
> 
> def get_status() -> GitStatus:
>     # Porcelain: " M file", "A  file", "?? file"
>     out = run(["git", "status", "--porcelain"])
>     changed = []
>     for line in out.splitlines():
>         if not line.strip():
>             continue
>         path = line[3:].strip()
>         changed.append(path)
>     return GitStatus(changed_paths=changed, branch=get_branch())
> 
> 
> def infer_lane_hint(paths: List[str]) -> str:
>     """
>     Find the first C-XX.LYY pattern in any changed path to help with commit msg.
>     """
>     for p in paths:
>         m = LANE_HINT_RE.search(p.replace("\\", "/"))
>         if m:
>             return f"{m.group('phase').upper()}.{m.group('lane').upper()}"
>     # fallback: if phases tree touched, just say PHASES
>     if any(p.startswith("01_PHASES/") or p.startswith("01_PHASES\\") for p in paths):
>         return "PHASES"
>     return "MISC"
> 
> 
> def ensure_logs() -> None:
>     LOG_DIR.mkdir(parents=True, exist_ok=True)
>     if not LOG_CSV.exists():
>         with LOG_CSV.open("w", newline="", encoding="utf-8") as f:
>             w = csv.writer(f)
>             w.writerow(["ts_local", "ts_utc", "branch", "lane_hint", "files_changed", "commit_msg"])
>     if not LOG_MD.exists():
>         LOG_MD.write_text("# Sync Log\n\n(append-only)\n\n", encoding="utf-8")
> 
> 
> def now_local_str() -> str:
>     # Don’t guess timezone libraries. Keep it simple.
>     # User timezone is America/Chicago; store local timestamp label.
>     return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
> 
> 
> def now_utc_str() -> str:
>     return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
> 
> 
> def maybe_run_integrity_audit() -> Optional[str]:
>     """
>     If 90_ADMIN/schema_integrity_audit.py exists, run it.
>     Return a short status string to include in the log.
>     """
>     audit = REPO_ROOT / "90_ADMIN" / "schema_integrity_audit.py"
>     if not audit.exists():
>         return None
>     try:
>         out = run(["python", str(audit)], check=True)
>         return "audit:OK"
>     except Exception as e:
>         return f"audit:FAIL ({e})"
> 
> 
> def write_log_entry(branch: str, lane_hint: str, files_changed: int, commit_msg: str, audit_status: Optional[str]) -> None:
>     ensure_logs()
>     ts_local = now_local_str()
>     ts_utc = now_utc_str()
> 
>     # CSV append
>     with LOG_CSV.open("a", newline="", encoding="utf-8") as f:
>         w = csv.writer(f)
>         w.writerow([ts_local, ts_utc, branch, lane_hint, files_changed, commit_msg])
> 
>     # MD append
>     extra = f" | {audit_status}" if audit_status else ""
>     with LOG_MD.open("a", encoding="utf-8") as f:
>         f.write(f"- **{ts_local}** (`{branch}`) — {files_changed} files — `{lane_hint}` — `{commit_msg}`{extra}\n")
> 
> 
> def main() -> None:
>     status = get_status()
> 
>     if not status.changed_paths:
>         print("No changes to commit. Exiting.")
>         return
> 
>     lane_hint = infer_lane_hint(status.changed_paths)
>     ts = datetime.now().strftime("%Y-%m-%d %H:%M")
>     files_changed = len(status.changed_paths)
> 
>     commit_msg = f"sync: {ts} CT | {files_changed} files | {lane_hint}"
> 
>     # optional: run audit before committing
>     audit_status = maybe_run_integrity_audit()
>     if audit_status and audit_status.startswith("audit:FAIL"):
>         # hard stop: don’t commit bad structure silently
>         raise SystemExit(f"Integrity audit failed. Fix first.\n{audit_status}")
> 
>     # stage all changes
>     run(["git", "add", "-A"])
> 
>     # commit
>     run(["git", "commit", "-m", commit_msg])
> 
>     # push
>     branch = status.branch
>     run(["git", "push", REMOTE, branch])
> 
>     # log AFTER successful push
>     write_log_entry(branch=branch, lane_hint=lane_hint, files_changed=files_changed, commit_msg=commit_msg, audit_status=audit_status)
> 
>     print(f"Done: {commit_msg}")
> 
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> Make executable:
> ```bash
> chmod +x 90_ADMIN/qi_sync.py
> ```
> 
> Run:
> ```bash
> python 90_ADMIN/qi_sync.py
> ```
> 
> ---
> 
> ## D. One-click launchers (Windows + Mac/Linux)
> 
> ### Windows PowerShell: `90_ADMIN/qi_sync.ps1`
> ```powershell
> $ErrorActionPreference = "Stop"
> python "$PSScriptRoot\qi_sync.py"
> ```
> 
> Run:
> ```powershell
> powershell -ExecutionPolicy Bypass -File 90_ADMIN\qi_sync.ps1
> ```
> 
> ### Mac/Linux: `90_ADMIN/qi_sync.sh`
> ```bash
> #!/usr/bin/env bash
> set -euo pipefail
> python3 90_ADMIN/qi_sync.py
> ```
> 
> Run:
> ```bash
> chmod +x 90_ADMIN/qi_sync.sh
> ./90_ADMIN/qi_sync.sh
> ```
> 
> ---
> 
> ## E. IDE setup (so you’re not “dealing with a database”)
> 
> If you go Postgres:
> - Use a DB extension in your IDE (Cursor/VS Code):
>   - “PostgreSQL” extension (connect to `localhost:54329`, user/pass/db = `qicase`)
> - Keep migrations as files in git. That’s the point: **DB state is reproducible**.
> 
> If you go SQLite:
> - Use “SQLite Viewer” extension
> - DB file lives at `90_ADMIN/db/qicase.sqlite`
> - You can still have migrations; it’s just easier.
> 
> ---
> 
> ## What I need from you (only if you want this wired to YOUR exact schema)
> Re-upload these (they expired for me):
> - `DATABASE_SCHEMA_MIGRATION_V2.sql`
> - `DATABASE_SCHEMA_MIGRATION_V3.sql`
> - `schema_integrity_audit.py`
> 
> Then I’ll:
> - merge V2/V3 into ordered migrations (`001_...`, `002_...`, etc.)
> - adjust `qi_sync.py` to:
>   - run the migration apply script automatically (optional flag)
>   - also append to your **Evidence Intake Log** lane (`C-02.L03`) if you want it to log file ingests
> 
> For now, you can start moving immediately with what’s above.

### User
> back to the app build. Yep. You’ve already got the three legs you need — you just haven’t wired them into a single “truth pipeline” yet:
> 
> * **Docs Site (MkDocs Material)** = *human browsing on phone*
> * **Paperless** = *document intake + OCR + tagging*
> * **Case RAG** = *AI search/answers across the corpus*
> 
> Below is the cleanest way to hook them up without turning your repo into spaghetti.
> 
> ---
> 
> ## The right build order (don’t freestyle this)
> 
> ### 1) Docs site first (phone access)
> 
> Goal: you can open a URL on your phone and navigate your case materials like a site.
> 
> **What should be in MkDocs:**
> 
> * Only **curated, human-readable** content:
> 
>   * Phase masters
>   * Docket index / trackers
>   * Exhibit lists
>   * “What happened” timeline narrative
>   * Playbooks / checklists / templates
> * Not raw PDFs (you can link PDFs, but don’t try to “MkDocs your entire evidence vault”)
> 
> **Pattern**
> 
> * `mkdocs-material-boilerplate/` becomes your docs app
> * Your content lives in a single source folder in the repo (recommended):
> 
>   * `docs_src/` (source-of-truth markdown)
>   * MkDocs builds to `site/` (generated)
> 
> **Deployment options**
> 
> * **Fastest/lowest pain:** Cloudflare Pages (build command + output dir)
> * If you insist on local-first and just want it online: push to GitHub → Pages is fine too, but CF Pages is your ecosystem.
> 
> ✅ Output: `https://<your-docs-domain>/` works on mobile.
> 
> ---
> 
> ### 2) Paperless second (ingestion + OCR)
> 
> Goal: everything you add (email, scan, phone upload) becomes OCR’d and normalized.
> 
> You already have `paperless_fcfcu/` with docker-compose and a ton of archived documents. Good.
> 
> **Do this next:**
> 
> * Make Paperless the **single intake mouth**
> * Feed it:
> 
>   * scans
>   * email-to-paperless
>   * phone uploads
>   * exported court PDFs
> * Ensure OCR is on and good enough (English is fine; if you need multilingual later, that’s a separate fight)
> 
> ✅ Output: Paperless becomes your “document registry” with tags + metadata.
> 
> ---
> 
> ### 3) Case RAG third (index + embed + query)
> 
> Goal: RAG indexes:
> 
> * MkDocs curated markdown (high signal)
> * Paperless documents (OCR text + metadata)
> * Optional: your trackers CSVs
> 
> You already have scripts:
> 
> * `01_scan_repo.py`
> * `02_extract_text.py`
> * `03_embed_index.py`
> * `04_query_chat.py`
> 
> That’s the right shape. Now you need to make it **pull from Paperless automatically** instead of you dragging files around.
> 
> ✅ Output: You can ask “what did they claim on May 28 vs July 17” and it cites the right artifacts.
> 
> ---
> 
> ## The wiring: one pipeline, two outputs
> 
> ### Source of truth flows like this
> 
> **Paperless (raw truth)**
> → export/metadata snapshot
> → RAG extraction + embeddings
> → (A) AI answers (RAG UI)
> → (B) curated markdown updates (MkDocs)
> 
> So:
> 
> * Paperless is the **truth vault**
> * RAG is the **search brain**
> * MkDocs is the **presentation layer**
> 
> MkDocs should *not* be the ingestion source. That’s backwards.
> 
> ---
> 
> ## Minimal folder structure that won’t rot
> 
> Add these (top-level):
> 
> ```
> docs_src/                  # curated markdown only (what humans read)
> rag_store/
>   corpus/                  # text chunks RAG reads (generated)
>   index/                   # embeddings + metadata (generated)
>   snapshots/
>     paperless_export/      # latest exported OCR + metadata (generated)
> ```
> 
> And keep:
> 
> * `paperless_fcfcu/` = the running system + data volumes (ideally NOT fully committed if it’s huge)
> * `app/case_rag/` = code + configs
> 
> ---
> 
> ## Paperless → RAG: how to connect (the practical way)
> 
> ### Option A (recommended): export from Paperless via API
> 
> You run a script that:
> 
> 1. pulls document list + metadata (tags, correspondents, created date, title)
> 2. downloads OCR’d text (or the file and extracts text)
> 3. stores into `rag_store/snapshots/paperless_export/`
> 4. triggers embed refresh
> 
> That gives you:
> 
> * stable ingestion
> * metadata available for filtering (by tag, date, doc type)
> * reproducible builds
> 
> ### Option B (simple but janky): point RAG at Paperless “media/documents/archive”
> 
> You *can* point your extractor at:
> `paperless_fcfcu/media/documents/archive/`
> …but you’ll lose a lot of metadata context unless you also capture Paperless DB/API data.
> 
> If you care about **chain-of-custody and traceability**, use Option A.
> 
> ---
> 
> ## MkDocs ↔ evidence linking (don’t break links)
> 
> In MkDocs, link to evidence like this:
> 
> * “View PDF” links should point to either:
> 
>   * Paperless document URL (best, includes metadata page)
>   * or a public/static mirror bucket (only if you need public)
> 
> If your docs site is private (which it should be), linking to Paperless directly is fine.
> 
> ---
> 
> ## What to do *today* (no theory)
> 
> ### Phase 1: Get docs online (1 sitting)
> 
> 1. Create `docs_src/` and move only curated markdown there.
> 2. In `mkdocs-material-boilerplate/`, set:
> 
>    * `docs_dir: ../docs_src`
>    * `site_dir: ../site` (or keep default inside boilerplate)
> 3. Make a dead-simple nav:
> 
>    * Home
>    * Phases
>    * Docket / Timeline
>    * Trackers
>    * Templates
> 4. Deploy to Cloudflare Pages.
> 
> ### Phase 2: Make Paperless the only intake (same day)
> 
> 1. Confirm Paperless is reachable from your phone (Tailscale/Zero Trust/Cloudflare Tunnel).
> 2. Make “consume” the only drop zone.
> 3. Stop manually sprinkling PDFs into random folders.
> 
> ### Phase 3: Hook Paperless export into case_rag (next)
> 
> 1. Add a new script: `scripts/rag/00_sync_paperless.py`
> 2. Update `config/sources.yaml` to include:
> 
>    * `docs_src/` (curated)
>    * `rag_store/snapshots/paperless_export/` (raw OCR exports)
> 3. Run pipeline end-to-end:
> 
>    * sync → extract → embed → query
> 
> ---
> 
> ## Your biggest current risk (I’m calling it out)
> 
> You’ve got:
> 
> * `app/case_rag/data/extracted_text/` full of `.txt` artifacts (good),
> * **AND** a full Paperless archive dumped in repo-ish structure (heavy),
> * **AND** MkDocs boilerplate sitting separate.
> 
> If you don’t formalize the flow, you’ll end up with:
> 
> * duplicate truth
> * broken references
> * “which version is real?” fights
> * embeddings that drift
> 
> So: **declare the system of record**:
> 
> * Raw docs = Paperless
> * Curated narrative = docs_src (MkDocs)
> * Search index = rag_store (generated)
> 
> Everything else is derived.
> 
> ---
> 
> ## If you want, next message I’ll give you:
> 
> * a ready-to-paste `mkdocs.yml` wired to `docs_src/`
> * a sane `sources.yaml` + `ingest_rules.yaml` layout for:
> 
>   * curated vs raw
>   * per-phase tag filters
>   * “court record” priority boosting
> * a concrete `00_sync_paperless.py` spec (API-based) that outputs:
> 
>   * `document.json` metadata
>   * `document.txt` OCR text
>   * stable filenames using your Qi-style IDs
> 
> But the move right now is simple: **stand up the docs site first** so you stop feeling blind on mobile. Then ingestion. Then RAG.

### Assistant
> Yeah, we “did a database” in the only way that matters: you already have **migration SQL files + a schema lock doc** sitting in `90_ADMIN/`. That’s the database plan. You just never wired it to an actual local Postgres instance.
> 
> You said: **local Postgres, no Supabase** + **sync logger** + **one-click commit/push**. Here’s the full wiring.
> 
> ---
> 
> # 1) Local Postgres (Docker) — dead simple
> 
> ## `docker-compose.yml` (put at repo root or in `90_ADMIN/db/`)
> ```yaml
> services:
>   qicase_postgres:
>     image: postgres:16
>     container_name: qicase_postgres
>     restart: unless-stopped
>     environment:
>       POSTGRES_DB: qicase
>       POSTGRES_USER: qicase
>       POSTGRES_PASSWORD: qicase_pw_change_me
>     ports:
>       - "54329:5432"
>     volumes:
>       - qicase_pgdata:/var/lib/postgresql/data
> 
> volumes:
>   qicase_pgdata:
> ```
> 
> ### Start it
> ```bash
> docker compose up -d
> ```
> 
> ### Connect string (for scripts + IDE)
> - Host: `localhost`
> - Port: `54329`
> - DB: `qicase`
> - User: `qicase`
> - Pass: `qicase_pw_change_me`
> 
> > VS Code: use **SQLTools** + Postgres driver, or the **PostgreSQL** extension. Either works.
> 
> ---
> 
> # 2) Migration runner (applies V2, V3, then V4)
> 
> Create `90_ADMIN/db/migrate.sh`
> ```bash
> #!/usr/bin/env bash
> set -euo pipefail
> 
> DB_HOST="${DB_HOST:-localhost}"
> DB_PORT="${DB_PORT:-54329}"
> DB_NAME="${DB_NAME:-qicase}"
> DB_USER="${DB_USER:-qicase}"
> DB_PASS="${DB_PASS:-qicase_pw_change_me}"
> 
> export PGPASSWORD="$DB_PASS"
> 
> psql_cmd() {
>   psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$DB_NAME" -v ON_ERROR_STOP=1 "$@"
> }
> 
> echo "==> Applying migrations to $DB_NAME@$DB_HOST:$DB_PORT as $DB_USER"
> 
> psql_cmd -f "90_ADMIN/DATABASE_SCHEMA_MIGRATION_V2.sql"
> psql_cmd -f "90_ADMIN/DATABASE_SCHEMA_MIGRATION_V3.sql"
> psql_cmd -f "90_ADMIN/DATABASE_SCHEMA_MIGRATION_V4.sql"
> 
> echo "✅ Migrations applied."
> ```
> 
> Make executable:
> ```bash
> chmod +x 90_ADMIN/db/migrate.sh
> ```
> 
> ---
> 
> # 3) Add the missing “sync logger” tables (Migration V4)
> 
> Create `90_ADMIN/DATABASE_SCHEMA_MIGRATION_V4.sql`
> ```sql
> BEGIN;
> 
> -- Useful extensions (safe if already present)
> CREATE EXTENSION IF NOT EXISTS pgcrypto;
> 
> -- Track each sync/log run
> CREATE TABLE IF NOT EXISTS sync_run (
>   run_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   started_at TIMESTAMPTZ NOT NULL DEFAULT now(),
>   ended_at TIMESTAMPTZ,
>   status TEXT NOT NULL DEFAULT 'started', -- started|ok|error
>   repo_root TEXT NOT NULL,
>   git_branch TEXT,
>   head_before TEXT,
>   head_after TEXT,
>   host TEXT,
>   os_user TEXT,
>   notes TEXT
> );
> 
> -- Track changed files observed during the run
> CREATE TABLE IF NOT EXISTS file_change_log (
>   change_id BIGSERIAL PRIMARY KEY,
>   run_id UUID NOT NULL REFERENCES sync_run(run_id) ON DELETE CASCADE,
>   detected_at TIMESTAMPTZ NOT NULL DEFAULT now(),
>   change_type TEXT NOT NULL, -- A|M|D|R|?? (git porcelain)
>   path TEXT NOT NULL,
>   old_path TEXT,
>   sha256 TEXT,
>   size_bytes BIGINT,
>   mtime_epoch BIGINT,
> 
>   -- Optional schema linkage if you want to attach changes to entities later
>   phase_id TEXT,
>   lane_id TEXT,
>   task_id TEXT,
>   doc_id TEXT
> );
> 
> CREATE INDEX IF NOT EXISTS idx_file_change_log_run_id ON file_change_log(run_id);
> CREATE INDEX IF NOT EXISTS idx_file_change_log_path ON file_change_log(path);
> CREATE INDEX IF NOT EXISTS idx_file_change_log_task_id ON file_change_log(task_id);
> 
> -- Quick view: what changed, grouped by phase-ish folder
> CREATE OR REPLACE VIEW v_changes_by_phase AS
> SELECT
>   run_id,
>   split_part(path, '/', 2) AS top_folder,
>   count(*) AS changes
> FROM file_change_log
> GROUP BY run_id, split_part(path, '/', 2);
> 
> COMMIT;
> ```
> 
> ---
> 
> # 4) Sync logger (logs git changes → DB) + One-click commit & push
> 
> ## A) Python logger: `90_ADMIN/sync_logger.py`
> ```python
> #!/usr/bin/env python3
> import os
> import re
> import json
> import time
> import hashlib
> import getpass
> import platform
> import subprocess
> from dataclasses import dataclass
> from pathlib import Path
> from typing import List, Optional, Tuple
> 
> import psycopg2
> 
> 
> @dataclass
> class GitChange:
>     change_type: str   # A/M/D/R/?? etc
>     path: str
>     old_path: Optional[str] = None
> 
> 
> def run(cmd: List[str], cwd: Path) -> Tuple[int, str, str]:
>     p = subprocess.run(cmd, cwd=str(cwd), text=True, capture_output=True)
>     return p.returncode, p.stdout.strip(), p.stderr.strip()
> 
> 
> def git_branch(repo: Path) -> str:
>     _, out, _ = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], repo)
>     return out
> 
> 
> def git_head(repo: Path) -> str:
>     _, out, _ = run(["git", "rev-parse", "HEAD"], repo)
>     return out
> 
> 
> def parse_git_status_porcelain(repo: Path) -> List[GitChange]:
>     """
>     Uses `git status --porcelain=v1 -z` for reliable parsing.
>     Handles renames in the form: 'R  old -> new' in v1, but -z gives pairs.
>     """
>     code, out, err = run(["git", "status", "--porcelain=v1", "-z"], repo)
>     if code != 0:
>         raise RuntimeError(f"git status failed: {err}")
> 
>     items = out.split("\x00")
>     items = [i for i in items if i]
>     changes: List[GitChange] = []
> 
>     i = 0
>     while i < len(items):
>         entry = items[i]
>         # entry looks like: 'XY path' or 'XY path\0oldpath\0newpath' (for rename/copy in -z)
>         status = entry[:2]
>         rest = entry[3:] if len(entry) > 3 else ""
> 
>         x, y = status[0], status[1]
>         ct = y if y != " " else x
>         ct = ct.strip() or "?"
> 
>         if ct in ("R", "C"):
>             # Rename/copy: next token is the new path in some outputs,
>             # but safer: parse "old -> new" if present, otherwise read next token.
>             if " -> " in rest:
>                 oldp, newp = rest.split(" -> ", 1)
>                 changes.append(GitChange(change_type=ct, path=newp, old_path=oldp))
>                 i += 1
>             else:
>                 # Fallback: treat rest as old, next token as new
>                 oldp = rest
>                 newp = items[i + 1] if i + 1 < len(items) else rest
>                 changes.append(GitChange(change_type=ct, path=newp, old_path=oldp))
>                 i += 2
>         else:
>             changes.append(GitChange(change_type=ct, path=rest))
>             i += 1
> 
>     return changes
> 
> 
> def sha256_file(p: Path) -> str:
>     h = hashlib.sha256()
>     with p.open("rb") as f:
>         for chunk in iter(lambda: f.read(1024 * 1024), b""):
>             h.update(chunk)
>     return h.hexdigest()
> 
> 
> def infer_ids_from_path(path: str) -> dict:
>     """
>     Optional: tries to extract schema IDs from filenames/folders:
>     - task: T-0001
>     - doc:  D-0001
>     - phase: C-01
>     - lane:  C-01.L02
>     """
>     ids = {"phase_id": None, "lane_id": None, "task_id": None, "doc_id": None}
> 
>     m = re.search(r"(C-\d{2})", path)
>     if m:
>         ids["phase_id"] = m.group(1)
> 
>     m = re.search(r"(C-\d{2}\.L\d{2})", path)
>     if m:
>         ids["lane_id"] = m.group(1)
> 
>     m = re.search(r"(T-\d{4})", path)
>     if m:
>         ids["task_id"] = m.group(1)
> 
>     m = re.search(r"(D-\d{4})", path)
>     if m:
>         ids["doc_id"] = m.group(1)
> 
>     return ids
> 
> 
> def connect_db():
>     host = os.getenv("DB_HOST", "localhost")
>     port = int(os.getenv("DB_PORT", "54329"))
>     db = os.getenv("DB_NAME", "qicase")
>     user = os.getenv("DB_USER", "qicase")
>     pw = os.getenv("DB_PASS", "qicase_pw_change_me")
>     return psycopg2.connect(host=host, port=port, dbname=db, user=user, password=pw)
> 
> 
> def main():
>     repo_root = Path(os.getenv("REPO_ROOT", Path.cwd())).resolve()
> 
>     # sanity check it's a repo
>     code, _, _ = run(["git", "rev-parse", "--is-inside-work-tree"], repo_root)
>     if code != 0:
>         raise SystemExit(f"Not a git repo: {repo_root}")
> 
>     branch = git_branch(repo_root)
>     head_before = git_head(repo_root)
>     changes = parse_git_status_porcelain(repo_root)
> 
>     conn = connect_db()
>     conn.autocommit = False
> 
>     try:
>         with conn.cursor() as cur:
>             cur.execute(
>                 """
>                 INSERT INTO sync_run (repo_root, git_branch, head_before, host, os_user, notes)
>                 VALUES (%s, %s, %s, %s, %s, %s)
>                 RETURNING run_id
>                 """,
>                 (
>                     str(repo_root),
>                     branch,
>                     head_before,
>                     platform.node(),
>                     getpass.getuser(),
>                     f"detected {len(changes)} working-tree changes",
>                 ),
>             )
>             run_id = cur.fetchone()[0]
> 
>             for ch in changes:
>                 file_path = (repo_root / ch.path).resolve()
>                 ids = infer_ids_from_path(ch.path)
> 
>                 sha = None
>                 size = None
>                 mtime = None
> 
>                 # Only hash if file exists and is not a directory
>                 if file_path.exists() and file_path.is_file() and ch.change_type != "D":
>                     try:
>                         sha = sha256_file(file_path)
>                         st = file_path.stat()
>                         size = int(st.st_size)
>                         mtime = int(st.st_mtime)
>                     except Exception:
>                         pass
> 
>                 cur.execute(
>                     """
>                     INSERT INTO file_change_log
>                       (run_id, change_type, path, old_path, sha256, size_bytes, mtime_epoch,
>                        phase_id, lane_id, task_id, doc_id)
>                     VALUES
>                       (%s, %s, %s, %s, %s, %s, %s,
>                        %s, %s, %s, %s)
>                     """,
>                     (
>                         str(run_id),
>                         ch.change_type,
>                         ch.path,
>                         ch.old_path,
>                         sha,
>                         size,
>                         mtime,
>                         ids["phase_id"],
>                         ids["lane_id"],
>                         ids["task_id"],
>                         ids["doc_id"],
>                     ),
>                 )
> 
>             cur.execute(
>                 "UPDATE sync_run SET status='ok', ended_at=now() WHERE run_id=%s",
>                 (str(run_id),),
>             )
> 
>         conn.commit()
>         print(json.dumps({"status": "ok", "run_id": str(run_id), "changes": len(changes)}, indent=2))
>     except Exception as e:
>         conn.rollback()
>         with conn.cursor() as cur:
>             cur.execute(
>                 "INSERT INTO sync_run (repo_root, git_branch, head_before, status, notes) VALUES (%s,%s,%s,'error',%s)",
>                 (str(repo_root), branch, head_before, str(e)),
>             )
>         conn.commit()
>         raise
>     finally:
>         conn.close()
> 
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> Install dependency:
> ```bash
> pip install psycopg2-binary
> ```
> 
> ---
> 
> ## B) One-click script: `90_ADMIN/one_click_sync.sh`
> This does: **migrate → log → commit → push**.
> 
> ```bash
> #!/usr/bin/env bash
> set -euo pipefail
> 
> REPO_ROOT="$(git rev-parse --show-toplevel)"
> cd "$REPO_ROOT"
> 
> # 1) Ensure DB schema exists
> bash 90_ADMIN/db/migrate.sh
> 
> # 2) Log current changes into DB (before commit)
> python 90_ADMIN/sync_logger.py
> 
> # 3) Commit + push if anything changed
> if [[ -n "$(git status --porcelain)" ]]; then
>   TS="$(date +"%Y-%m-%d %H:%M:%S")"
>   git add -A
>   git commit -m "SYNC: repo snapshot ${TS}"
>   git push origin "$(git rev-parse --abbrev-ref HEAD)"
>   echo "✅ Commit + push complete."
> else
>   echo "ℹ️ No changes to commit."
> fi
> ```
> 
> Make executable:
> ```bash
> chmod +x 90_ADMIN/one_click_sync.sh
> ```
> 
> Run it:
> ```bash
> bash 90_ADMIN/one_click_sync.sh
> ```
> 
> That’s your “one click”.
> 
> ---
> 
> # 5) About your missing tasks (01.03, 02.03)
> 
> You’re not imagining it: your `1_phases-v3-LOCKED.csv` currently does **not** include `C-01.L03` or `C-02.L03`, and your repo tree also lacks those lanes.
> 
> The **fast fix** is: you already have `migrate_phases_repo_v3.py`. Use it as the “structure enforcer,” but you need to add two lanes + tasks into the CSV first or the script will never generate them.
> 
> ### What to add (non-generic, aligned to your case)
> Add these to the CSV and create corresponding lane folders:
> 
> **C-01.L03_Legal_Impact_Assessment**
> - `T-0004_TR60B_voidness_argument_map.md` (void vs voidable, jurisdiction predicate)
> - `T-0005_Remedies_matrix_vacate_stay_sanctions.md` (what relief maps to what defect)
> - `D-0003_Jurisdictional_defects_impact_memo.md` (the “so what” memo you file/attach)
> 
> **C-02.L03_Evidence_Intake_Log**
> - `T-0018_Evidence_intake_protocol.md` (naming, hashing, metadata minimums)
> - `T-0019_Intake_backlog_processing_log.md` (your “catch up” pass)
> - `D-0013_Evidence_intake_log_master.md` (the master intake ledger spec)
> 
> If you want me to **write the exact CSV rows** for those (matching your schema columns), paste the header row from `1_phases-v3-LOCKED.csv` and I’ll output the rows perfectly formatted. I’m not guessing your column names.
> 
> ---
> 
> # 6) “Do I need SQL Server locally?”
> No. That’s you overcomplicating it.
> 
> - Your migrations are already written in **Postgres-flavored SQL**.
> - Postgres runs clean in Docker.
> - Your IDE can edit/query it via extensions.
> - You avoid Microsoft-driver nonsense.
> 
> Postgres local wins here.
> 
> ---
> 
> ## What to do right now (in order)
> 1) Add `docker-compose.yml`
> 2) Add `DATABASE_SCHEMA_MIGRATION_V4.sql`
> 3) Add `90_ADMIN/db/migrate.sh`
> 4) Add `90_ADMIN/sync_logger.py`
> 5) Add `90_ADMIN/one_click_sync.sh`
> 6) Run:
> ```bash
> docker compose up -d
> bash 90_ADMIN/one_click_sync.sh
> ```
> 
> If anything errors, paste the console output and I’ll correct it fast.
