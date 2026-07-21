---
layout: page
title: Streamlining the vendor management and contract signing process in a travel industry | Use Cases - Zoho CRM
slug: streamlining-the-vendor-management-and-contract-signing-process-in-a-travel-industry-use-cases-zoho-crm
status: publish
updated_at: "2026-07-18T11:03:20-04:00"
tags:
  - projects
source_type: manual
summary: ""
created_at: "2026-07-01T23:17:15-05:00"
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: fc1c5035f66e42a7bba08b6675434100
canonical_ref: ""
template_key: master-template
type: note
---

# Streamlining the vendor management and contract signing process in a travel industry | Use Cases - Zoho CRM

Done: No
Status: Not started
Priority: ✨ Medium
AI summary: The document outlines a streamlined vendor management and contract signing process for a California-based travel company using Zoho CRM. It details the need for structured onboarding and contract signing blueprints to enhance agent efficiency, ensure proper documentation, and improve conversion rates. Key features include mandatory task completion, email reminders, and SLA alerts to prevent delays in vendor onboarding and contract signing, ultimately aiming to facilitate smoother operations and better communication between agents and property owners.
Akiflow: No
Email: No
Favorite: No
Frequency 1: Once
Is Active: Yes
Is Archived: No
Note: No
Owner: Cody
URL: https://help.zoho.com/portal/en/kb/crm/use-cases/articles/streamlining-the-vendor-management-and-contract-signing-process-in-a-travel-industry

**Edition:** Enterprise and above | **Industry:** Travel and Tourism, Hospitality | **Features:** Blueprint

## Scenario

A California-based company provides an online platform for listing and renting local homes to travelers. It connects the property owners and the travelers to facilitate booking affordable living spaces all over the world.

Owners interested in listing their properties register on the company's portal. The agents contact them and sign a contract based on the company's terms and conditions. The interested owners are qualified and moved to the next stage of the sales cycle. The qualifying process is simple and doesn't involve rigid rules, the agents are encouraged to work at their own pace. They often prefer to discuss the terms, make negotiations, or sign contracts offline or on calls rather than via email. For this reason, there is no official way to warrant signing a contract.

Over time, the inconsistencies in the qualification process began to impact the conversions negatively. The sales managers noticed a sharp decline and increased delays in the overall conversions. The vendor onboarding process failed to provide clues as to the root cause. Now, the pressing demand from property owners and the travelers to add more listings has increased their challenges.

## Requirements

They require a process that can guide the agents through the process, helping them understand the activities that must be done at each stage. Most importantly, it should restrict them from proceeding to the next stage if the activities in the current stage are not completed.

The processes they require are:

1. An onboarding process for the vendors (property owners) to ensure the sales team knows the upcoming stages and the activities involved. It will also ensure communications are made through the proper channels.
2. Contract signing process that regulates document collection and verification at the right stages to speed up the contract signing process.

## Solution

The senior sales manager and the CRM administrator create two blueprints: one to manage the vendor onboarding process and the other one to manage the contract signing process.

### I. Blueprint for vendor onboarding

The onboarding process is simple and contains just a few stages. The blueprint is expected to:

1. Specify activities at each stage so that the agent has a clear idea about their tasks. For example, when the agent is unable to contact the vendor and clicks on the Failed to Contact transition, the next action would be to recontact them within 2 business days. To ensure they stay on track, you can create an After Transition task for them in the blueprint which will be visible under *Next Action*.

    [](https://desk.zoho.com/DocsDisplay-zgId=4241905&mode=inline&blockId=n3z4f7035718885a0490fb5a17c9267acf074)

2. Send email reminders to the agents for upcoming tasks and calls. The due date for completion will be displayed on the record detail page.

    [](https://desk.zoho.com/DocsDisplay-zgId=4241905&mode=inline&blockId=n3z4fb38a8a63070b4eb2accaf343c0281910)

    Restrict the agents from saving activities with inappropriate values by validating them.

3. For example, the task status should be Completed and the due date of a call must be 2 days from the date of trigger. The agents will only be able to save the transition if the values match.
4. Make attachments and notes mandatory and specify the documents they must attach in the checklist.For example, the NDA Needed transition can be completed only if the notes have been added, the email has been sent for NDA approval, and the call is completed. All these requirements are clearly mentioned in the checklist.
5. Prevent others from editing onboarding stages. Once a blueprint is created using the onboarding stages picklist field, the field will be locked after a record is created in the particular module. The stages will change as each transition is completed.

**Blueprint configuration**

1. Go to **Setup** > **Process Management** > **Blueprint**.
2. Click **Create Blueprint** and input the following:
3. Blueprint name: Vendor Onboarding
4. Module: Vendors
5. Layout: Standard
6. Field: Onboarding process

Create a picklist field called Vendor Onboarding stage with these values: Contact, In Discussion, Recontact, Contact in Future, NDA Approval, Interested, Lost.

3. In the blueprint editor, drag and drop the states and create the transitions in the table below:

| **Transition**  | **Before Transition**  | **During Transition**  | **After Transition**  |
| --- | --- | --- | --- |
| New vendor created  | Record owner  | N/A | Send email notification to the record owner and record owner's manager.        **Email template:** New vendor created.  |
| Contacted  | Record owner  | 1. Make notes and attachments mandatory.       2. Add a checklist and name it "Required attachments". Mention the following in the checklist:       a) Email sent or acknowledgement from the vendor.       b) Call script.  | N/A  |
| Failed to contact  | Record owner  | 1. Make notes mandatory.       2. **Insert message:** give reason for contact failure in notes.  | Click  **+Add** > **Create task**:
1. **Subject:** Recontact vendor.
2. **Due date:** Transition trigger date + 2 business days.
3. **Status:** In progress
4. **Priority:** High
5. **Assigned to:** select an agent
6. Check notify and remind assignee.
7. Remind one day before the due date at 10:00 am
8. **Alert:** Email and pop-up.  |
| Recontact failed  | Record owner  | N/A  | Field update    - Name: Call status    - Field: Contact status = failed  |
| NDA needed  | Record owner  | **1. + Add** > **Associated item** > **Call** > select **outgoing call status** and validate it as completed.    - **Insert error message:** Call status must be completed to move to the next state.        2. Add checklist.    **Name:** NDA-related attachment       a) Attach acknowledgement email from the vendor.       b) Mention call details in notes.  | Send email notification to the record owner and record owner's manager.       **Email template:** NDA required.  |
| Sign NDA  | Record owner  | **+ Add** > **Associated item** > **Task** > select    **status is completed**.  | Send email notification to the record owner and record owner's manager.       **Email template:** NDA signed.  |
| NDA not needed  | Record owner  | 1. Make attachment mandatory.       2. Add checklist    - **Name:** Documents needed    Attach the email that confirms NDA is not required.  | N/A  |
| Lost  | Record owner  | 1.  **Insert message:**    Enter reason for rejection     2. Select  **Make Notes Mandatory**  | Automate email notification to record owner and record owner's manager.     **Template name:**  Vendor rejected |

**Configuring common transition and SLA alert**

**Common transition:** A vendor can be marked uninterested from "Contact", "NDA approval", and "In Discussion" states if required. Make "Not interested" a common transition so that it is accessible from multiple states in the blueprint.

**To create a common transition, do the following**

1. Create a transition named **"Not interested".**
2. Check the **Common Transition** option.
3. Check the states: **In Discussion, Contact, NDA Approval**.

**SLA alert:** Set the maximum number of days a record can stay in a state and set it to escalate automatically when the period is extended. For example, the record can be in the NDA approval state for 3 business days, on the 4th day, an escalation alert will be sent to the manager.

**To create an SLA alert, do the following**

1. Go to **NDA approval state**.
2. Set the maximum days the record can stay in the NDA approval state: **enter 3 business days**.
3. In the *When exceeding the time limit*, choose who and when to be notified section, select escalate **After > 1 business day**.
4. Click **+Actions** > **Default SLA Alert** > **Roles and add Sales Manager and Record Owner**.
5. Click **Save**.

### II. Blueprint for the contract signing process

The interested vendors are moved to another process for signing the contract. The vendor is now converted into a deal and is contacted by a different team to discuss the commission fee and sponsorship charges for the contract period. The manager for this team wants to use a blueprint to standardize the collection of documents and prevent delays in signing contracts and receiving sponsorship payments from the vendor.

1. Make it mandatory to attach the email and the proposal that is sent to the vendor during the Proposal Sent transition.
2. Assign a task to send an email to the vendor if the documents are not received.
3. Make it mandatory to attach documents and list the received documents in the notes. Specify the documents and list in the checklist for reference. For example, the Document Received transition can only be completed if the notes and documents are attached.
4. Set SLA alert if the contract is not signed within 7 business days. On the 8th day an alert will be sent to the record owner and their manager.

**Blueprint configuration**

1. Go to **Setup** > **Process Management** > **Blueprint**.
2. Click **Create Blueprint** and input the following:
3. Blueprint name: Contract signing process
4. Module: Deals
5. Layout: Standard
6. Field: Contract stages

Add the following values to the Contract Stage picklist field: Interested Vendor, Proposal and Document, Commercial Discussion, ID Creation, Contract Sent, Contract Signed.

3. In the blueprint editor, drag and drop the states and create the transitions in the table below:

| **Transition** | **Before Transition** | **During Transition** | **After Transition** |
| --- | --- | --- | --- |
| Contract created | Record owner | N/A | Send email notification to the record owner and record owner's manager.      **Email template:** New contract created.  |
| Proposal sent | Record owner | Make attachments mandatory.       **Insert message:** Attach a copy of the email and proposal that was sent to the vendor. | N/A |
| Document received | Record owner | 1. Make notes and attachment mandatory.       2. Add checklist   Name: Documents to attach    - Attach documents received from the client.    - List the documents that were received. | N/A |
| Not received | Record owner | N/A | Click **+Add** > **Create task**:
1. Subject: Recontact vendor
2. Due date: Transition trigger date + 2 business days
3. Status: In progress
4. Priority: High
5. Assigned to: select an agent
6. Check notify and remind assignee
7. Remind one day before the due date at 10:00 am
8. Alert: Email and pop-up  |
| Received | Record owner | 1. Make notes and attachment mandatory.       2. Add checklist    Name: Documents to attach    - Attach documents received from the client.    - List the documents that were received. | N/A |
| ID created | Record owner | N/A | Send email notification to the record owner and record owner's manager.       **Email template:** Contract ID created. |
| Signed | Sales manager | Make attachment mandatory.       **Insert message:** Attach a copy of the contract. | Send email notification to the record owner, record owner's manager, and regional manager.         **Email template:** Contract signed   |

**Configuring SLA alert**

Set the maximum number of days a record can stay in a state and set it to escalate automatically when the period is extended.

For example, the record can be in the Contract Sent state for 7 business days, on the 8th day an escalation alert will be sent to the manager.

**To create an SLA alert, do the following**

1. Go to the **Contract Sent state**.
2. Set the maximum days the record can stay in the Contract Sent state: **enter 7 business days**.
3. In the When exceeding the time limit, choose who and when to be notified section, select escalate **After > 1 business day**.
4. Click **+Actions** > **Default SLA Alert** > **Roles and add Sales Manager and Record Owner**.
5. Click **Save**.

Tags :

[blueprint](https://help.zoho.com/portal/en/kb/tags/blueprint)

- Anumita Gupta
- Updated: 3 years ago

Helpful-10

Share :

- Zoho CRM Training Programs[REGISTER NOW](https://www.zoho.com/crm/customer-success/)

    Learn how to use the best tools for sales force automation and better customer engagement from Zoho's implementation specialists.
