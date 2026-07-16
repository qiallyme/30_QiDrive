![][image1]

![][image2]

![][image3]

The analysis of the spreadsheet data reveals a complex legal and financial case involving Financial Center First Credit Union (FCFCU), characterized by significant credit reporting errors, audit discrepancies, and substantial claims for damages.

### **Key Takeaways**

* **Systemic FCRA Reporting Errors:**  
  * The 2.5.1\_fcra\_ISSUE table identifies 14 distinct reporting errors, all currently attributed to the Experian (EXP) bureau.  
  * The most common issues involve reporting a balance or a delinquent status (e.g., "180 days late") for periods after the account should have been marked as satisfied or closed (post-satisfaction).  
  * Specific examples include records \[FCRA-0001\] and \[FCRA-0002\], where the reported status "F" differs from the correct status "OK" following a sale/satisfaction anchor on 08/15/2025.  
* **Significant Financial Audit Variance:**  
  * An audit comparison between the Plaintiff's claims and the Defendant's audit reveals a total overcharge variance of approximately **\-$17,080.34**.  
  * The largest discrepancies are found in "Interest (Per Diem)" (-$10,725.30) and "Attorney Fees" (-$4,750.00), where the defendant's audit suggests these charges should be zero.  
  * Other variances include "Publication/Misc" (-$1,094.35) and "Sheriff Costs" (-$284.28).  
* **Substantial Damages and Broad Violation Scope:**  
  * The Damages table records over **$210,000** in total financial impact. The "Damages" category itself accounts for $208,000, which includes high-value claims such as a $75,000 entry for trauma related to sexual coercion under duress \[DMG-2026-004\].  
  * The case involves 269 recorded violations across multiple categories: Procedural (89), Tort (78), Statutory (69), ADA (22), and Constitutional (11).  
  * The Case\_Event\_Log shows the timeline began with a "Past Due Account Notification" in June 2024, escalating to an "Exparte Order for Protection" in November 2024 and a formal case filing in January 2025\.

The user wants an analysis of the data in the spreadsheet.

There are many tables (CSVs) provided.

The active sheet is 2.5.1\_fcra\_ISSUE.

The user's selection is a single cell Z9 in that sheet.

I should start by inspecting the tables to understand the overall structure and content.

Given the large number of tables, I'll focus on the ones that seem most central or summarized first.

FCFCU\_CASE\_MASTER-0\_master-Index seems like a good place to start for an overview.

FCFCU\_CASE\_MASTER-Audit\_Summary also sounds like a summary.

FCFCU\_CASE\_MASTER-3\_events-Case\_Event\_Log might give a chronological view.

FCFCU\_CASE\_MASTER-2\_violations-Table2 and FCFCU\_CASE\_MASTER-6\_damages-Table10 seem like core data tables.

I will start by listing and inspecting a few key tables.

1. FCFCU\_CASE\_MASTER-0\_master-Index-A1:G9-20260322201844.csv  
2. FCFCU\_CASE\_MASTER-Audit\_Summary-B1:B5-20260322201845.csv (and other Audit\_Summary parts)  
3. FCFCU\_CASE\_MASTER-2\_violations-Table2-A1:AE271-20260322201846.csv  
4. FCFCU\_CASE\_MASTER-6\_damages-Table10-A1:R592-20260322201846.csv  
5. FCFCU\_CASE\_MASTER-3\_events-Case\_Event\_Log-A1:H143-20260322201846.csv

Wait, the prompt says "analyze the data in the spreadsheet".

I'll begin by inspecting the first few rows of these key tables to understand the context of "FCFCU CASE MASTER". It looks like a legal or compliance case tracking system (FCRA \- Fair Credit Reporting Act).

Plan:

1. Load and inspect the index and summary tables.  
2. Identify key themes (violations, damages, events, actors).  
3. Provide a high-level summary and then drill down into specific areas like violations or damages if they contain quantitative data.  
4. Create visualizations if appropriate (e.g., violations by type, damages over time).

Let's start with inspection.  
Show code  
Python  
`import pandas as pd`

`# List of key files to inspect`  
`files_to_inspect = [`  
    `"FCFCU_CASE_MASTER-0_master-Index-A1:G9-20260322201844.csv",`  
    `"FCFCU_CASE_MASTER-Audit_Summary-B7:E16-20260322201845.csv",`  
    `"FCFCU_CASE_MASTER-2_violations-Table2-A1:AE271-20260322201846.csv",`  
    `"FCFCU_CASE_MASTER-6_damages-Table10-A1:R592-20260322201846.csv",`  
    `"FCFCU_CASE_MASTER-3_events-Case_Event_Log-A1:H143-20260322201846.csv"`  
`]`

`for file in files_to_inspect:`  
    `print(f"--- {file} ---")`  
    `df = pd.read_csv(file)`  
    `print(df.head())`  
    `print(df.info())`  
    `print("\n")`

Code output  
`--- FCFCU_CASE_MASTER-0_master-Index-A1:G9-20260322201844.csv ---`  
   `case_name  case_id  court  plaintiff  defendant  status  exposure_anchor`  
`0        NaN      NaN    NaN        NaN        NaN     NaN              NaN`  
`1        NaN      NaN    NaN        NaN        NaN     NaN              NaN`  
`2        NaN      NaN    NaN        NaN        NaN     NaN              NaN`  
`3        NaN      NaN    NaN        NaN        NaN     NaN              NaN`  
`4        NaN      NaN    NaN        NaN        NaN     NaN              NaN`  
`<class 'pandas.core.frame.DataFrame'>`  
`RangeIndex: 8 entries, 0 to 7`  
`Data columns (total 7 columns):`  
 `#   Column           Non-Null Count  Dtype`    
`---  ------           --------------  -----`    
 `0   case_name        0 non-null      float64`  
 `1   case_id          0 non-null      float64`  
 `2   court            0 non-null      float64`  
 `3   plaintiff        0 non-null      float64`  
 `4   defendant        0 non-null      float64`  
 `5   status           0 non-null      float64`  
 `6   exposure_anchor  0 non-null      float64`  
`dtypes: float64(7)`  
`memory usage: 576.0 bytes`  
`None`

`--- FCFCU_CASE_MASTER-Audit_Summary-B7:E16-20260322201845.csv ---`  
              `Category  Plaintiff Claim (8/15)  Defendant Audit  Variance (Overcharge)`  
`0   Judgment Principal               220863.00        220637.00                -226.41`  
`1  Interest (Per Diem)                10725.30             0.00              -10725.30`  
`2    Taxes (Premature)                 7600.81          7600.81                   0.00`  
`3        Attorney Fees                 4750.00             0.00               -4750.00`  
`4     Publication/Misc                 1094.35             0.00               -1094.35`  
`<class 'pandas.core.frame.DataFrame'>`  
`RangeIndex: 7 entries, 0 to 6`  
`Data columns (total 4 columns):`  
 `#   Column                  Non-Null Count  Dtype`    
`---  ------                  --------------  -----`    
 `0   Category                7 non-null      object`   
 `1   Plaintiff Claim (8/15)  7 non-null      float64`  
 `2   Defendant Audit         7 non-null      float64`  
 `3   Variance (Overcharge)   7 non-null      float64`  
`dtypes: float64(3), object(1)`  
`memory usage: 352.0+ bytes`  
`None`

`--- FCFCU_CASE_MASTER-2_violations-Table2-A1:AE271-20260322201846.csv ---`  
  `violation_id violation_date     actor                          violation_type description status                                                         notes Actor / institution Date / timeframe Harm caused Rights implicated  Source Supporting text excerpt Violation type  actor_role category confidence_level evidence_ids  harm_category impact_summary                      issue_title ledger_status legal_authority  objective_issue  phase_id procedural_context  source_document  summary violation_category  violation_date_end  why_it_matters`  
`0        V-020            NaN       AES             THEORY_POST_SALE_COST_SHIFT         NaN  Draft         Imported from trash: VIO_AES_UTILITY_2026-01-15-20.md                 NaN              NaN         NaN               NaN     NaN                     NaN            NaN         NaN      NaN              NaN          NaN            NaN            NaN             Post Sale Cost Shift           NaN             NaN              NaN       NaN                NaN              NaN      NaN          Statutory                 NaN             NaN`  
`1        V-021            NaN  CITIZENS             THEORY_POST_SALE_COST_SHIFT         NaN  Draft    Imported from trash: VIO_CITIZENS_UTILITY_2026-01-15-21.md                 NaN              NaN         NaN               NaN     NaN                     NaN            NaN         NaN      NaN              NaN          NaN            NaN            NaN             Post Sale Cost Shift           NaN             NaN              NaN       NaN                NaN              NaN      NaN          Statutory                 NaN             NaN`  
`2        V-022            NaN       HOA             THEORY_POST_SALE_COST_SHIFT         NaN  Draft            Imported from trash: VIO_HOA_TORT_2026-01-15-22.md                 NaN              NaN         NaN               NaN     NaN                     NaN            NaN         NaN      NaN              NaN          NaN            NaN            NaN             Post Sale Cost Shift           NaN             NaN              NaN       NaN                NaN              NaN      NaN          Statutory                 NaN             NaN`  
`3        V-023            NaN  CITYOFIN  THEORY_WRONGFUL_ENFORCEMENT_NO_CONTROL         NaN  Draft  Imported from trash: VIO_CITYOFIN_MUNICIPAL_2026-01-15-23.md                 NaN              NaN         NaN               NaN     NaN                     NaN            NaN         NaN      NaN              NaN          NaN            NaN            NaN  Wrongful Enforcement No Control           NaN             NaN              NaN       NaN                NaN              NaN      NaN          Statutory                 NaN             NaN`  
`4        V-024            NaN  CITYOFIN  THEORY_WRONGFUL_ENFORCEMENT_NO_CONTROL         NaN  Draft  Imported from trash: VIO_CITYOFIN_MUNICIPAL_2026-01-15-24.md                 NaN              NaN         NaN               NaN     NaN                     NaN            NaN         NaN      NaN              NaN          NaN            NaN            NaN  Wrongful Enforcement No Control           NaN             NaN              NaN       NaN                NaN              NaN      NaN          Statutory                 NaN             NaN`  
`<class 'pandas.core.frame.DataFrame'>`  
`RangeIndex: 270 entries, 0 to 269`  
`Data columns (total 31 columns):`  
 `#   Column                   Non-Null Count  Dtype`    
`---  ------                   --------------  -----`    
 `0   violation_id             269 non-null    object`   
 `1   violation_date           59 non-null     object`   
 `2   actor                    268 non-null    object`   
 `3   violation_type           267 non-null    object`   
 `4   description              258 non-null    object`   
 `5   status                   269 non-null    object`   
 `6   notes                    269 non-null    object`   
 `7   Actor / institution      1 non-null      object`   
 `8   Date / timeframe         1 non-null      object`   
 `9   Harm caused              1 non-null      object`   
 `10  Rights implicated        1 non-null      object`   
 `11  Source                   1 non-null      float64`  
 `12  Supporting text excerpt  1 non-null      object`   
 `13  Violation type           1 non-null      object`   
 `14  actor_role               0 non-null      float64`  
 `15  category                 2 non-null      object`   
 `16  confidence_level         258 non-null    object`   
 `17  evidence_ids             58 non-null     object`   
 `18  harm_category            0 non-null      float64`  
 `19  impact_summary           95 non-null     object`   
 `20  issue_title              13 non-null     object`   
 `21  ledger_status            258 non-null    object`   
 `22  legal_authority          95 non-null     object`   
 `23  objective_issue          0 non-null      float64`  
 `24  phase_id                 0 non-null      float64`  
 `25  procedural_context       160 non-null    object`   
 `26  source_document          0 non-null      float64`  
 `27  summary                  0 non-null      float64`  
 `28  violation_category       269 non-null    object`   
 `29  violation_date_end       0 non-null      float64`  
 `30  why_it_matters           0 non-null      float64`  
`dtypes: float64(9), object(22)`  
`memory usage: 65.5+ KB`  
`None`

`--- FCFCU_CASE_MASTER-6_damages-Table10-A1:R592-20260322201846.csv ---`  
  `transaction_id transaction_date   amount currency transaction_category        transaction_type                                                     description                                                    related_violation_ids                payee                                                                       notes entry_type  event_time time_certainty date_logged source attachments_present attachment_description external_reference`  
`0   EXP-2026-001       2025-08-15    150.0      USD              Utility            Utility Bill               AES Indiana - Electric Service (Post-Sale Period)                                                        V-FCFCU-2025-0080          AES Indiana  Utility charges during disputed ownership period - unjust enrichment claim        NaN         NaN            NaN         NaN    NaN                 NaN                    NaN                NaN`  
`1  COST-2025-004       2025-12-09   1200.0      USD              Expense       Emergency Housing                 Hotel costs (roach-infested, unsafe conditions)                                                        V-FCFCU-2025-0051       Various Hotels           Emergency housing following forced removal in freezing conditions        NaN         NaN            NaN         NaN    NaN                 NaN                    NaN                NaN`  
`2  COST-2025-005       2025-12-10    300.0      USD              Expense  Replacement Essentials  Toiletries, clothing, dog supplies (unable to access property)                                                        V-FCFCU-2025-0051              Various                    Emergency purchases - forced to leave without essentials        NaN         NaN            NaN         NaN    NaN                 NaN                    NaN                NaN`  
`3   DMG-2026-004       2025-12-15  75000.0      USD              Damages         Sexual Coercion    Sexual coercion under duress (homeless, freezing conditions)  V-FCFCU-2025-0202,V-FCFCU-2025-0203,V-FCFCU-2025-0204,V-FCFCU-2025-0205  Cody Rice-Velasquez  Foreseeable vulnerability created by unlawful displacement - severe trauma        NaN         NaN            NaN         NaN    NaN                 NaN                    NaN                NaN`  
`4  COST-2025-003       2025-12-21    500.0      USD              Expense       Veterinary/Search   Service animal (Gigi) escape - veterinary check, search costs                                                        V-FCFCU-2025-0207              Various   Service animal escaped during hotel transition due to displacement stress        NaN         NaN            NaN         NaN    NaN                 NaN                    NaN                NaN`  
`<class 'pandas.core.frame.DataFrame'>`  
`RangeIndex: 591 entries, 0 to 590`  
`Data columns (total 18 columns):`  
 `#   Column                  Non-Null Count  Dtype`    
`---  ------                  --------------  -----`    
 `0   transaction_id          590 non-null    object`   
 `1   transaction_date        133 non-null    object`   
 `2   amount                  20 non-null     float64`  
 `3   currency                22 non-null     object`   
 `4   transaction_category    22 non-null     object`   
 `5   transaction_type        22 non-null     object`   
 `6   description             590 non-null    object`   
 `7   related_violation_ids   276 non-null    object`   
 `8   payee                   19 non-null     object`   
 `9   notes                   22 non-null     object`   
 `10  entry_type              568 non-null    object`   
 `11  event_time              0 non-null      float64`  
 `12  time_certainty          568 non-null    object`   
 `13  date_logged             568 non-null    object`   
 `14  source                  568 non-null    object`   
 `15  attachments_present     568 non-null    object`   
 `16  attachment_description  231 non-null    object`   
 `17  external_reference      557 non-null    object`   
`dtypes: float64(2), object(16)`  
`memory usage: 83.2+ KB`  
`None`

`--- FCFCU_CASE_MASTER-3_events-Case_Event_Log-A1:H143-20260322201846.csv ---`  
  `event_id Event_Date_Time                   Event_Title                                    Event_Narrative  Event_Type                                                            Event_Actors                                      Event_Location  notes`  
`0     E001      2024-06-24               Notice Received                      Past Due Account Notification      NOTICE                                                                   FCFCU  4817 Shadow Pointe Dr, Indianapolis, IN 46254-3744    NaN`  
`1     E002      2024-06-26              Payment Returned  Returned Online Loan Payment (Insufficient Funds)     PAYMENT                                                                   FCFCU  4817 Shadow Pointe Dr, Indianapolis, IN 46254-3744    NaN`  
`2     E003      2024-07-03                 Payment Check                                      Check Payment     PAYMENT  Marion County Treasurer; Taxpayer: Financial Center First Credit Union  4817 Shadow Pointe Dr, Indianapolis, IN 46254-3744    NaN`  
`3     E004      2024-11-18  Exparte Order for Protection   Ex Parte Order for Protection / Notice to Appear  PROTECTION                                                               Defendant  4817 Shadow Pointe Dr, Indianapolis, IN 46254-3744    NaN`  
`4     E005      2025-01-16                    Case Filed                                                NaN      FILING                                                       Plaintiff Counsel  4817 Shadow Pointe Dr, Indianapolis, IN 46254-3744    NaN`  
`<class 'pandas.core.frame.DataFrame'>`  
`RangeIndex: 142 entries, 0 to 141`  
`Data columns (total 8 columns):`  
 `#   Column           Non-Null Count  Dtype`    
`---  ------           --------------  -----`    
 `0   event_id         142 non-null    object`   
 `1   Event_Date_Time  57 non-null     object`   
 `2   Event_Title      57 non-null     object`   
 `3   Event_Narrative  56 non-null     object`   
 `4   Event_Type       57 non-null     object`   
 `5   Event_Actors     57 non-null     object`   
 `6   Event_Location   56 non-null     object`   
 `7   notes            0 non-null      float64`  
`dtypes: float64(1), object(7)`  
`memory usage: 9.0+ KB`  
`None`

The data is related to a legal case involving "Financial Center First Credit Union" (FCFCU).

Key findings from the inspection:

1. **Audit Summary**: Shows categories like Judgment Principal, Interest, Taxes, Attorney Fees, etc. There's a variance (overcharge) calculation between Plaintiff Claim and Defendant Audit.  
2. **Violations**: A table with 270 entries. Many are in "Draft" status. Categories include "Statutory". Violation types include "THEORY\_POST\_SALE\_COST\_SHIFT", "Wrongful Enforcement No Control", etc.  
3. **Damages**: Contains transactions like Utility Bills, Emergency Housing, Sexual Coercion (severe trauma), Veterinary/Search. Amounts range from small ($150) to large ($75,000).  
4. **Event Log**: Chronological events starting from June 2024 (Notice Received) to 2025 (Case Filed, Exparte Order).

The user wants an analysis. I can analyze:

* The distribution of violation types.  
* The breakdown of damages by category.  
* The timeline of events.  
* The audit variance.

Let's look at the Audit Summary more closely to get the total variance.

Let's also look at the Damages table to sum up the amounts by category.

And the Violations table to see the count of violations per actor.

I'll also check FCFCU\_CASE\_MASTER-2.5.1\_fcra\_ISSUE-FCRA\_2-A1:AA90-20260322201844.csv because it's the active sheet (though the user selected Z9, which might be a specific cell).

Wait, the active sheet is 2.5.1\_fcra\_ISSUE. Let's inspect that too.  
Show code  
Python  
`# Inspect the active sheet data`  
`active_sheet_file = "FCFCU_CASE_MASTER-2.5.1_fcra_ISSUE-FCRA_2-A1:AA90-20260322201844.csv"`  
`df_active = pd.read_csv(active_sheet_file)`  
`print(f"--- {active_sheet_file} ---")`  
`print(df_active.head())`  
`print(df_active.info())`

`# Also check the Audit Summary more thoroughly`  
`audit_summary_file = "FCFCU_CASE_MASTER-Audit_Summary-B7:E16-20260322201845.csv"`  
`df_audit = pd.read_csv(audit_summary_file)`  
`print(f"--- {audit_summary_file} ---")`  
`print(df_audit)`

Code output  
`--- FCFCU_CASE_MASTER-2.5.1_fcra_ISSUE-FCRA_2-A1:AA90-20260322201844.csv ---`  
          `id snapshot _date        tradeline bureau    yr  mon status correct status  bal reported  correct balance  post-notice                              Issues                                        anchor  doc-ref                                                                                                                                                          Notes Date Reported Date of Status Last Payment Received  Scheduled Amount  Actual Amount  - Period_Date                         Issues_Auto                                   Anchor_Auto                                                                                                                                                     notes_auto  Issue_Count  Weighted_Issue_Count`  
`0  FCRA-0001     2026-03-22  661563L2 ($23k)    EXP  2026  Feb      F             OK           0.0              0.0         True           STATUS; POST-SATISFACTION  08/15/2025 Sale / 09/09/2025 Decree Returned      NaN                                                  Reported status differs from correct status | Reporting period is after 08/15/2025 sale / satisfaction anchor    2026-03-19     2026-01-01            2024-08-12               0.0            0.0  -  2026-02-01           STATUS; POST-SATISFACTION  08/15/2025 Sale / 09/09/2025 Decree Returned                                                  Reported status differs from correct status | Reporting period is after 08/15/2025 sale / satisfaction anchor            2                     4`  
`1  FCRA-0002     2026-03-22  661563L2 ($23k)    EXP  2026  Jan      F             OK           0.0              0.0         True           STATUS; POST-SATISFACTION  08/15/2025 Sale / 09/09/2025 Decree Returned      NaN                                                  Reported status differs from correct status | Reporting period is after 08/15/2025 sale / satisfaction anchor    2026-03-19     2026-01-01                   NaN               NaN            NaN  -  2026-01-01           STATUS; POST-SATISFACTION  08/15/2025 Sale / 09/09/2025 Decree Returned                                                  Reported status differs from correct status | Reporting period is after 08/15/2025 sale / satisfaction anchor            2                     4`  
`2  FCRA-0003     2026-03-22  661563L2 ($23k)    EXP  2025  Dec    180             OK       24676.0              0.0         True  STATUS; BALANCE; POST-SATISFACTION  08/15/2025 Sale / 09/09/2025 Decree Returned      NaN  Reported status differs from correct status | Reported balance differs from correct balance | Reporting period is after 08/15/2025 sale / satisfaction anchor    2026-03-19     2026-01-01            2024-08-13             209.0            0.0  -  2025-12-01  STATUS; BALANCE; POST-SATISFACTION  08/15/2025 Sale / 09/09/2025 Decree Returned  Reported status differs from correct status | Reported balance differs from correct balance | Reporting period is after 08/15/2025 sale / satisfaction anchor            3                     6`  
`3  FCRA-0004     2026-03-22  661563L2 ($23k)    EXP  2025  Nov    180             OK       24517.0              0.0         True  STATUS; BALANCE; POST-SATISFACTION  08/15/2025 Sale / 09/09/2025 Decree Returned      NaN  Reported status differs from correct status | Reported balance differs from correct balance | Reporting period is after 08/15/2025 sale / satisfaction anchor    2026-03-19     2026-01-01            2024-08-13             209.0            0.0  -  2025-11-01  STATUS; BALANCE; POST-SATISFACTION  08/15/2025 Sale / 09/09/2025 Decree Returned  Reported status differs from correct status | Reported balance differs from correct balance | Reporting period is after 08/15/2025 sale / satisfaction anchor            3                     6`  
`4  FCRA-0005     2026-03-22  661563L2 ($23k)    EXP  2025  Oct    180             OK       24363.0              0.0         True  STATUS; BALANCE; POST-SATISFACTION  08/15/2025 Sale / 09/09/2025 Decree Returned      NaN  Reported status differs from correct status | Reported balance differs from correct balance | Reporting period is after 08/15/2025 sale / satisfaction anchor    2026-03-19     2026-01-01            2024-08-13             209.0            0.0  -  2025-10-01  STATUS; BALANCE; POST-SATISFACTION  08/15/2025 Sale / 09/09/2025 Decree Returned  Reported status differs from correct status | Reported balance differs from correct balance | Reporting period is after 08/15/2025 sale / satisfaction anchor            3                     6`  
`<class 'pandas.core.frame.DataFrame'>`  
`RangeIndex: 89 entries, 0 to 88`  
`Data columns (total 27 columns):`  
 `#   Column                 Non-Null Count  Dtype`    
`---  ------                 --------------  -----`    
 `0   id                     89 non-null     object`   
 `1   snapshot _date         89 non-null     object`   
 `2   tradeline              89 non-null     object`   
 `3   bureau                 89 non-null     object`   
 `4   yr                     89 non-null     int64`    
 `5   mon                    89 non-null     object`   
 `6   status                 89 non-null     object`   
 `7   correct status         89 non-null     object`   
 `8   bal reported           45 non-null     float64`  
 `9   correct balance        48 non-null     float64`  
 `10  post-notice            89 non-null     bool`     
 `11  Issues                 14 non-null     object`   
 `12  anchor                 12 non-null     object`   
 `13  doc-ref                0 non-null      float64`  
 `14  Notes                  14 non-null     object`   
 `15  Date Reported          89 non-null     object`   
 `16  Date of Status         89 non-null     object`   
 `17  Last Payment Received  44 non-null     object`   
 `18  Scheduled Amount       44 non-null     float64`  
 `19  Actual Amount          44 non-null     float64`  
 `20  -                      89 non-null     object`   
 `21  Period_Date            89 non-null     object`   
 `22  Issues_Auto            14 non-null     object`   
 `23  Anchor_Auto            12 non-null     object`   
 `24  notes_auto             14 non-null     object`   
 `25  Issue_Count            89 non-null     int64`    
 `26  Weighted_Issue_Count   89 non-null     int64`    
`dtypes: bool(1), float64(5), int64(3), object(18)`  
`memory usage: 18.3+ KB`  
`None`  
`--- FCFCU_CASE_MASTER-Audit_Summary-B7:E16-20260322201845.csv ---`  
              `Category  Plaintiff Claim (8/15)  Defendant Audit  Variance (Overcharge)`  
`0   Judgment Principal               220863.00        220637.00                -226.41`  
`1  Interest (Per Diem)                10725.30             0.00              -10725.30`  
`2    Taxes (Premature)                 7600.81          7600.81                   0.00`  
`3        Attorney Fees                 4750.00             0.00               -4750.00`  
`4     Publication/Misc                 1094.35             0.00               -1094.35`  
`5        Sheriff Costs                  622.28           338.00                -284.28`  
`6                Clerk                   35.00            35.00                   0.00`

The active sheet 2.5.1\_fcra\_ISSUE contains Fair Credit Reporting Act (FCRA) reporting data. It tracks reported status and balance versus "correct" status and balance across different bureaus (EXP, etc.) and months.

Key columns in 2.5.1\_fcra\_ISSUE:

* bureau: Credit bureau (e.g., EXP).  
* status: Reported status.  
* correct status: What the status should have been.  
* bal reported: Reported balance.  
* correct balance: What the balance should have been.  
* Issues: Description of the reporting error (e.g., "STATUS; POST-SATISFACTION").  
* Issue\_Count: Number of issues in that record.

I can analyze:

1. **FCRA Reporting Errors**: Frequency of issues by bureau and type.  
2. **Audit Discrepancies**: The variance between plaintiff claims and defendant audits.  
3. **Damages Breakdown**: Categorizing the financial impact.  
4. **Violations Overview**: Types of violations identified.

Let's refine the analysis:

* **Takeaway 1: FCRA Reporting Accuracy.** Analyze the 2.5.1\_fcra\_ISSUE table to show the number of reporting errors per bureau and the nature of these errors (status vs balance).  
* **Takeaway 2: Financial Audit Variance.** Summarize the Audit\_Summary table to show the total overcharge/variance.  
* **Takeaway 3: Damages and Violations.** Summarize the Damages and Violations tables to show the scale and scope of the case.

I will start by calculating the counts and sums for these areas.  
Show code  
Python  
`import altair as alt`

`# 1. FCRA Reporting Analysis`  
`df_fcra = pd.read_csv("FCFCU_CASE_MASTER-2.5.1_fcra_ISSUE-FCRA_2-A1:AA90-20260322201844.csv")`  
`# Filter rows where Issue_Count > 0`  
`fcra_issues = df_fcra[df_fcra['Issue_Count'] > 0].copy()`

`# 2. Audit Summary Analysis`  
`df_audit = pd.read_csv("FCFCU_CASE_MASTER-Audit_Summary-B7:E16-20260322201845.csv")`  
`total_variance = df_audit['Variance (Overcharge)'].sum()`

`# 3. Damages Analysis`  
`df_damages = pd.read_csv("FCFCU_CASE_MASTER-6_damages-Table10-A1:R592-20260322201846.csv")`  
`# Clean amount column`  
`df_damages['amount'] = pd.to_numeric(df_damages['amount'], errors='coerce')`  
`damages_by_cat = df_damages.groupby('transaction_category')['amount'].sum().reset_index()`

`# 4. Violations Analysis`  
`df_violations = pd.read_csv("FCFCU_CASE_MASTER-2_violations-Table2-A1:AE271-20260322201846.csv")`  
`violation_counts = df_violations['violation_category'].value_counts().reset_index()`  
`violation_counts.columns = ['violation_category', 'count']`

`# Create Visualizations`

`# Chart 1: FCRA Issues by Bureau`  
`fcra_bureau_chart = alt.Chart(fcra_issues).mark_bar().encode(`  
    `x=alt.X('bureau:N', title='Credit Bureau'),`  
    `y=alt.Y('count():Q', title='Number of Reporting Issues'),`  
    `color='bureau:N'`  
`).properties(title='FCRA Reporting Issues by Bureau')`  
`fcra_bureau_chart.save('fcra_bureau_issues.json')`

`# Chart 2: Audit Variance by Category`  
`audit_chart = alt.Chart(df_audit).mark_bar().encode(`  
    `x=alt.X('Category:N', sort='-y', title='Audit Category'),`  
    `y=alt.Y('Variance (Overcharge):Q', title='Variance (Overcharge Amount)'),`  
    `color=alt.condition(`  
        `alt.datum['Variance (Overcharge)'] < 0,`  
        `alt.value('red'),`  
        `alt.value('green')`  
    `)`  
`).properties(title='Audit Variance by Category (Plaintiff vs Defendant)')`  
`audit_chart.save('audit_variance.json')`

`# Chart 3: Damages by Category`  
`damages_chart = alt.Chart(damages_by_cat).mark_arc().encode(`  
    `theta=alt.Theta('amount:Q', title='Total Amount'),`  
    `color=alt.Color('transaction_category:N', title='Damage Category'),`  
    `tooltip=['transaction_category', 'amount']`  
`).properties(title='Distribution of Damages by Category')`  
`damages_chart.save('damages_distribution.json')`

`# Print summaries for text response`  
`print("FCRA Issues Summary:")`  
`print(fcra_issues['bureau'].value_counts())`  
`print("\nAudit Total Variance:", total_variance)`  
`print("\nDamages Summary:")`  
`print(damages_by_cat)`  
`print("\nViolation Counts:")`  
`print(violation_counts)`

Code output  
`FCRA Issues Summary:`  
`bureau`  
`EXP    14`  
`Name: count, dtype: int64`

`Audit Total Variance: -17080.339999999997`

`Damages Summary:`  
  `transaction_category     amount`  
`0              Damages  208000.00`  
`1              Expense    2800.00`  
`2        Legal Expense      30.95`  
`3              Utility     150.00`

`Violation Counts:`  
  `violation_category  count`  
`0         Procedural     89`  
`1               Tort     78`  
`2          Statutory     69`  
`3                ADA     22`  
`4     Constitutional     11`

I have analyzed the data across several key tables.

Summary of findings:

1. **FCRA Reporting Issues**: There are 14 identified reporting errors in the 2.5.1\_fcra\_ISSUE table, all associated with the 'EXP' (Experian) bureau. These include status and balance discrepancies, particularly post-satisfaction.  
2. **Audit Variance**: The Audit\_Summary shows a total variance (overcharge) of approximately \-$17,080.34. The largest discrepancies are in "Interest (Per Diem)" (-$10,725.30) and "Attorney Fees" (-$4,750.00).  
3. **Damages**: Total damages recorded in the Damages table exceed $210,000, with the vast majority ($208,000) categorized as "Damages" (likely non-economic or specific harm like the $75k sexual coercion entry).  
4. **Violations**: There are 269 violation entries, with "Procedural" (89), "Tort" (78), and "Statutory" (69) being the most frequent categories.

I will now structure the final response with these takeaways and the generated charts.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQ8AAAHCCAYAAADxWUxUAAAXRklEQVR4Xu3d+XuU9bnH8f5VbX845/QSrWzWirZWrUXqroggi2ERlcrSCEYqtrRaWj24VD1q3bWoeKmtrYqK+8pm2Akgi3J++h6/j+dJJ58ntxO/Q3vfJO8fXlcm80xmEvjMm5mQ5Vv7D/1vAoBv6lt6BgAMBfEAUIR4AChCPAAUIR4AihAPAEWIB4AixANAEeIBoAjxAFCEeAAoQjwAFCEeAIoUx+PMs89OJ4w+sd/23fvTvoNH0qVTplSvL1zSXV0un19f5idnnZW27do74Hp+87tbG9fdev0njh2TVt99T+P40TJm/LjGeUNx8oQJjfP+Va69bmHjPMvvb/vv/j/vmV2zG8eBo6WjeOQwtJ43ety49On2PdXpl155LX26bXd1mXzZfN7eA19Uo64v/8xzL375NmMb111ff316wcJFjeOdaH0fSkWOx1NPr61OP/L4U2nBosWNywBHw1GNx/U9NzYu93Xx+P6Y0VVA8uD17QaLx6Tzz0sffLK5cvHkydV5U6dPr15+uGFLmvCj09Km3h3p9DPPqM5b9Mvu9NBjT1anr1vyy/7ra30f6tP55a69B9ODDz+WbvrNyuq83/7+D9XLx556uvGx1vGor3frzr3p1B//OK1Z+3xafvOvB1z3ZdOmNW4vhza/3LP/cPr7K6+n19a/k7rmzhtwrJbjkS+XT5/0w5Or9/Osn33156N/dvn1aTNmVh97/vPN71fr7dZ/HzkwP5s0qTrvrnv/J936x9ur0/lt8ssZXV3pjbffr24rf1z1+1HfzquvvzXgdjHydBSP+uFxfefQIWetT1vyo4w8xnx+vsPUsdE7i17//X9+pDovn37syTWV+s7QepvjT/5B9fraF/72/7e9L/104sTqdOvYB4tHHYN8uXwn2bBlW38wWk/X6suvff5vaXH30v6PK8crP9XKEaovO1g8Jl8+tf9jybeX3z7fcXMYW28na73T3rLqj1Wg8u3np4n1HbvW+shjydJladXtqwfcbms86j+7/Hp+f/P7kgNcPwXNT3vqvwN9P4gHOoqH3qHyv1atr+ehtz7yyI8W8r9m+fTEn/+8f5jZ+x9valx/fpnPz5fNpweLjHc8svyooPuGnv73M/tk89Y09qTx1enB4jHYo7Ts0S/vwPW//rXB4nHH3fdWj4jqRyC11njkANTv59fF44yfntUfv9qk885LGz/dPuBtiQdaHdV49Ny0Ip1y2mnVQ+b8r28+rzUeWQ5ADkhraPo+O1w9HNfrr0/nO0q+Izz+l2e+DMTJ1cP7+ulKvr78NONHPzm9/1/ZfIfJjwby6OuH+61jz29z3eIl1WkrHvl0vhPnjyVHQD/W+vL5Dryo+/oqEPnpQn76lD/221bfWf0rni+TH53k6zz7nHP6by8/BZsy7Yq0tGd5ennd+urpRb69/HodnVp+23z5OfPn919n/f7Vd/Ba69OW/H7UIZk1e07/x6LxyLed368777mv/7ZvXvm76s80/1nV73N+ma/jBxNOIR4oj0cUgz1VOto+3rQ17ez7rHG+N40M8O9EPL5GfhSVH0Ho04gI8qOY1s+rAP9ux3w8APggHgCKEA8ARYgHgCLEA0AR4gGgCPEAUIR4AChCPAAUIR4AirjFI3+j28LFX/20sZ7lKxrHAcTmFo+sjscLL73S+DkWm3t3Vt/WDuBfT++bQxEiHgCOPa7xAHDsIh4AihAPAEWIB4AixANAEeIBoAjxAFCEeAAoQjwAFCEeAIoQDwBFiAeAIsQDQBHiAaAI8QBQhHgAKEI8ABQhHgCKEA8ARYgHgCLEA0AR4gGgCPEAUIR4OHrmrSPp5BsOITD9O8M/EQ9HoxYdQnAXrTrc+HvDV4iHIx0q4pl7z+eNvzd8hXg40qEiHuJhIx6OdKiIh3jYiIcjHSriIR424uFIh4p4iIeNeDjSoSIe4mEjHo50qIiHeNiIhyMdKuIhHjbi4UiHiniIh414ONKhIh7iYSMejnSoiId42IiHIx0q4iEeNuLhSIeKeIiHjXg40qEiHuJhIx6OdKiIh3jYiIcjHSriIR424uFIh4p4iIeNeDjSoSIe4mEjHo50qIiHeNiIhyMdKuIhHjbi4UiHiniIh414ONKhIh7iYSMejnSoiId42IiHIx0q4iEeNuLhSIeKeIiHjXg40qEiHuJhIx6OdKiIh3jYiIcjHSriIR424uFIh4p4iIeNeDjSoSIe4mEjHo50qIiHeNiIhyMdKuIhHjbi4UiHiniIh414ONKhIh7iYSMejnSoiId42IiHIx0q4iEeNuLhSIeKeIiHjXg40qEiHuJhIx6OdKiIh3jYiIcjHSriIR424uFIh4p4iIeNeDjSoSIe4mEjHo50qIiHeNiIhyMdKuIhHjbi4UiHiniIh414ONKhIh7iYSMejnSoiId42IiHIx0q4iEeNuLhSIeKeIiHjXg40qEiHuJhIx6OdKiIh3jYiIcjHSriIR424uFIh4p4iIeNeDjSoSIe4mEjHo50qIiHeNiIhyMdKuIhHjbi4UiHiniIh414ONKhIh7iYSMejnSoiId42IiHIx0q4iEeNuLhSIeKeIiHjXg40qEiHuJhIx6OdKiIh3jYiIcjHSriIR424uFIh4p4iIeNeDjSoSIe4mEjHo50qIiHeNiIhyMdKuIhHjbi4UiHiniIh414ONKhIh7iYSMejnSoiId42IiHIx0q4iEeNuLhSIeKeIiHjXg40qEiHuJhIx6OdKiIh3jYiIcjHSriIR424uFIh4p4iIeNeDjSoSIe4mEjHo50qIiHeNiIhyMdKuIhHjbi4UiHiniIh414ONKhIh7iYSMejnSoiId42IiHIx0q4iEeNuLhSIeKeIiHjXg40qEiHuJhIx6OdKiIh3jYiIcjHSriIR424uFIh4p4iIeNeDjSoSIe4mEjHo50qIiHeNiIhyMdKuIhHjbi4UiHiniIh414ONKhIh7iYXOLx4xZXWnh4u607+CRdPe996d1699pXGa406EiHuJhc4tHluOxqXdHev2t9xrHRgIdKuIhHjb3eGzd2Zdee/PdtHvfwcbx4U6HiniIh809Hvnl4u5l1dMYPT7c6VARD/GwucZjpNOhIh7iYSMejnSoiId42IiHIx0q4iEeNuLhSIeKeIiHjXg40qEiHuJhIx6OdKiIh3jYiIcjHSriIR424uFIh4p4iIeNeDjSoSIe4mEjHo50qIiHeNiIhyMdKuIhHjbi4UiHiniIh414ONKhIh7iYSMejnSoiId42IiHIx0q4iEeNuLhSIeKeIiHjXg40qEiHuJhIx6OdKiIh3jYiIcjHSriIR424uFIh4p4iIeNeDjSoSIe4mEjHo50qIiHeNiIhyMdKuIhHjbi4UiHiniIh414ONKhIh7iYSMejnSoiId42IiHIx0q4iEeNuLhSIeKeIiHjXg40qEiHuJhIx6OdKiIh3jYiuOxdefe9OgTa9KDDz+eJk+Z2jiO9nSoiId42IrjsbPvQFp95z1p38Ej6YoZsxrH0Z4OFfEQD1txPGp7D3zROA9Do0NFPMTDVhyPDZu3VU9d8suZV85uHEd7OlTEQzxsxfHIzj3/wvQf//lf6d0PNjSOoT0dKuIhHrbieOSnK/lRR7apd0fjONrToSIe4mErjkerq65e0DgP7elQEQ/xsBXHIz/a+OEpp1befv/jxnG0p0NFPMTDVhyPbFnPr9Ilk6cQj0I6VMRDPGzF8cif6+jdvidt/HRHmjPv6sZxtKdDRTzEw1Ycjxpf51FOh4p4iIetOB59n32eps+8Mk2ZOj3Nnju/cRzt6VARD/GwFcdj89Zd1dd37Np7ME2bPrNxHO3pUBEP8bAVxwOd06EiHuJhK4pH6xeI8UVi5XSoiId42IrigaNDh4p4iIetOB75Ece3v/PdyveOG5U2btneuAy+ng4V8RAPW3E88td3bNm2uzqdv6uW76z95nSoiId42IrjkY06/oQ0cdK51U8UW3Xb6sZxfD0dKuIhHraO4nHi6LHV05ZTJpzaOIb2dKiIh3jYiuORv86jftqCMjpUxEM8bMXxaP2EKY88yuhQEQ/xsBXFY8/+w9WXp/N1Hp3RoSIe4mErikfWu6Ov+tL0fJofBlRGh4p4iIetOB6Lu5em+dcsSNdetyi9vO7NxnG0p0NFPMTDVhyP/FSFpyud0aEiHuJhK44HPwC5czpUxEM8bMXxyE4/48w0eszY9Oa7HzaOoT0dKuIhHrbieNS/9Cmf7pozr3Ec7elQEQ/xsBXHI9u+e3965rkXG+djaHSoiId42DqKx3Gjjk/jxp9UfW+LHkN7OlTEQzxsxfFo/a7aefOvbRxHezpUxEM8bMXxQOd0qIiHeNiK47Hv4JF09sRzqk+czr2K39tSQoeKeIiHrTge9U9Pz/GYesWMxnG0p0NFPMTDVhyP/H0t+Rvk8unnXnipcRzt6VARD/GwFcUj/xdtDsZDjz5RPXXht8aV0aEiHuJhK4pH669d0GMYOh0q4iEetqJ45G/Hz99NW+tZvqJxGbSnQ0U8xMNWFA8cHTpUxEM8bEXxyE9X/vHqG9XnPvQYhk6HiniIh60oHtlDjz6Z7v/zI+mRx59Ka559vnEc7elQEQ/xsBXHIxszbnyaNn1Weurp5xrH0J4OFfEQD1txPPJTl97te6rT/La4MjpUxEM8bMXxyM49/8Lq99R+vLG3cQzt6VARD/GwdRQPdEaHiniIh604HnyRWOd0qIiHeNg6ige/Ma4zOlTEQzxsxfHgW/I7p0NFPMTDVhwPviW/czpUxEM8bMXxyN5+76O0rOdX1aMQPYb2dKiIh3jYiuORf+3Cn+57oPp2/AsvvrRxHO3pUBEP8bAVx6Pvs8/Ti39/tTq99IbljeNoT4eKeIiHrSgerb9qkl83WU6HiniIh60oHln+PEf+6lL+q7acDhXxEA9bR/FYecsqHnl0QIeKeIiHrTge+Zc+8QuuO6NDRTzEw1Ycj/x5j+5lPfw8jw7oUBEP8bAVx6P155jyM0zL6FARD/GwFcej1ayuuY3z0J4OFfEQD1txPOpHHlfOnpeuW7SkcRzt6VARD/GwFcWDX71wdOhQEQ/xsBXFo1X+OaY7+w40zkd7OlTEQzxsxfH4aOOn6cTRYxvnY+h0qIiHeNiK44HO6VARD/GwEQ9HOlTEQzxsxMORDhXxEA8b8XCkQ0U8xMNGPBzpUBEP8bARD0c6VMRDPGzEw5EOFfEQDxvxcKRDRTzEw0Y8HOlQEQ/xsBEPRzpUxEM8bMTDkQ4V8RAPG/FwpENFPMTDRjwc6VARD/GwEQ9HOlTEQzxsxMORDhXxEA8b8XCkQ0U8xMNGPBzpUBEP8bARD0c6VMRDPGzEw5EOFfEQDxvxcKRDRTzEw0Y8HOlQEQ/xsBEPRzpUxEM8bMTDkQ4V8RAPG/FwpENFPMTDRjwc6VARD/GwhYjH0huWN84bCXSoiId42ELE44WXXkkffLK5cf5wp0NFPMTDFiIeg9m971Da1XdgWNOhIp7Zdx1s/L0NR3r/G4oQ8ehZviJNnT6zcf5wp0NFPDzysIWIx0ilQ0U8xMNGPBzpUBEP8bARD0c6VMRDPGzEw5EOFfEQDxvxcKRDRTzEw0Y8HOlQEQ/xsBEPRzpUxEM8bMTDkQ4V8RAPG/FwpENFPMTDRjwc6VARD/GwEQ9HOlTEQzxsxMORDhXxEA8b8XCkQ0U8xMNGPBzpUBEP8bARD0c6VMRDPGzEw5EOFfEQDxvxcKRDRTzEw0Y8HOlQEQ/xsBEPRzpUxEM8bMTDkQ4V8RAPG/FwpENFPMTDRjwc6VARD/GwEQ9HOlTEQzxsxMORDhXxEA8b8XCkQ0U8xMNGPBzpUBEP8bARD0c6VMRDPGzEw5EOFfEQDxvxcKRDRTzEw0Y8HOlQEQ/xsBEPRzpUxEM8bMTDkQ4V8RAPG/FwpENFPMTDRjwc6VARD/GwEQ9HOlTEQzxsxMORDhXxEA8b8XCkQ0U8xMNGPBzpUBEP8bARD0c6VMRDPGzEw5EOFfEQDxvxcKRDRTzEw0Y8HOlQEQ/xsBEPRzpUxEM8bMTDkQ4V8RAPG/FwpENFPMTDRjwc6VARD/GwEQ9HOlTEQzxsxMORDhXxEA8b8XCkQ0U8xMNGPBzpUBEP8bARD0c6VMRDPGzEw5EOFfEQDxvxcKRDRTzEw0Y8HOlQEQ/xsBEPRzpUxEM8bMTDkQ4V8RAPG/FwpENFPMTDRjwc6VARD/GwEQ9HOlTEQzxsxMORDhXxEA8b8XCkQ0U8xMNGPBzpUBEP8bARD0c6VMRDPGzEw5EOFfEQDxvxcKRDRTzEw0Y8HOlQEQ/xsBEPRzpUxEM8bMTDkQ4V8RAPG/FwpENFPMTDRjwc6VARD/GwEQ9HOlTEQzxsxMORDhXxEA8b8XCkQ0U8xMNGPBzpUBEP8bARD0c6VMRDPGzEw5EOFfEQDxvxcKRDRTzEw0Y8HOlQEQ/xsBEPRzpUxEM8bMTDkQ4V8RAPG/FwpENFPMTDRjwc6VARD/GwEQ9HOlTEQzxsxMORDhXxEA8b8XCkQ0U8xMNGPBzpUBEP8bARD0c6VMRDPGzEw5EOFfEQDxvxcKRDRTzEw0Y8HOlQEQ/xsBEPRzpUxEM8bMTDkQ4V8RAPG/FwpENFPMTDRjwc6VARD/GwEQ9HOlTEQzxsxMORDhXxEA8b8XCkQ0U8xMNGPBzpUBEP8bARD0c6VMRDPGzEw5EOFfEQDxvxcKRDRTzEw0Y8HOlQEQ/xsBEPRzpUxEM8bMTDkQ4V8RAPG/FwpENFPMTDRjwc6VARD/GwEQ9HOlTEQzxsxMORDhXxEA8b8XCkQ0U8xMNGPBzpUBEP8bARD0c6VMRDPGzEw5EOFfEQDxvxcKRDRTzEw0Y8HOlQEQ/xsBEPRzpUxEM8bMTDkQ4V8RAPG/FwpENFPMTDRjwc6VARD/Gwucdj38Ej6e5770/r1r/TODbc6VARD/GwucdjU++O9Ppb7zXOHwl0qIiHeNjCxuP6ZTemK2bMGtYmzb0DxwD9exuO9P43FO7xyBZ3L0szZnU1zgcQV4h4ADj2EA8Uy083L770snT5FTPSQ48+kbbt2pdW3rIq9X32eXV+lj8hrm+H4YF4oFiOR/6cVf16DkcOSD79p/seqF7+9R/rGm+H4YF4oJjGo2f5irRl667qdB0PDF/EA8Va49G7Y0964i/Ppq65V1WvE4/hj3gAKEI8ABQhHgCKEA8ARYgHgCLEA0AR4gGgCPEAUIR4AChCPFBs++79jfMwchAPDLC4e2n/6Tnzrk6zuuakV157M82ee1V69Y23q++S/d5xo9K8+demW1bdlu64+9507vkXDriODzdsSRs2b6t+yMyTa9ZWkcnXtbPvQBp1/AlpzbPPp3vuezCNOuH7aeOW7f2XyS/1/UFcxAMDXHjxpQNez+H4eGNveu+jjemSyVOqYOTz63jk062PQL79ne+mMePGV6db45FfTr5sanX+zCtn918+Xw/xODYRDwzQ+shj/jULqnjkcGT5vHbxqF/PIdB4XHDRJf2XOe+Ci/qvh3gcm4gHgCLEA0AR4gGgCPEAUIR4AChCPAAUIR4AihAPAEWIB4AixANAEeIxgoxadKhh4srDAy6z9IbljbcDBkM8RhANRzZ+6aEBl/nFoiXp0ssuT+vf+SCtfeGl6rybfv3bSn79D7ffkabPvDLt2X84zZjVlW5eeUt1LF9u4eLuxm1i+CIeI4iGY7B41I88rlmwsBGP/M1rL69bX/0i6/ry9bF8mniMLMRjBNFwDBaPWbPnVj+z4/plN1ah2LX34IBArPjy5d4DX6T7HnioOnbtLxal21bfVb1N/asmMTIQjxFEwzFYPIChIh4jyAW3Hk4Tbjw0QPfD/3wKAnwTxANAEeIBoAjxAFCEeAAoQjwAFCEeAIoQDwBFiAeAIsQDQBHiAaAI8QBQhHgAKEI8ABT5P52082yiS/zrAAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>