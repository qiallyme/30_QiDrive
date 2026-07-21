---
layout: page
title: "Java Functions for Calculations"
slug: "java_functions_for_calculations"
created_at: "2023-07-31 23:02:40"
updated_at: "2026-07-18T11:03:11-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "__CaptainsLogchatexports (1).json"
template_key: master-template
date: 2023-07-31
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "a9218dcc-9409-411e-b968-9550235772de"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Java Functions for Calculations

## Overview
- **Date**: 2023-07-31 23:02:40
- **Conversation ID**: `a9218dcc-9409-411e-b968-9550235772de`
- **Source**: `__CaptainsLogchatexports (1).json`

## Chat History

### User
> need java script with the following functions. Functio 1. On edit of srvp_grosssalesforthemonth, divide srvp_grosssalesforthemonth by 1.07 to get srvp_calculatedpretax. Funtion 2. srvp_calculatedpretax * .07 = srvp_calculatedtaxesdue, Function 3. srvp_srvfilingfee = 40.00, Function 4. srvp_calculatedtotal = srvp_calculatedtaxesdue + srvp_srvfilingfee. Function 5. srvp_totalduecash = srvp_calculatedtotal Function 6. srvp_totalduecard = srvp_totalduecash * 1.035

### Assistant
> Sure, here's the JavaScript code with the functions you requested:
> 
> ```javascript
> // Function 1: On edit of srvp_grosssalesforthemonth, divide by 1.07 to get srvp_calculatedpretax.
> function calculatePretax(srvp_grosssalesforthemonth) {
>   return srvp_grosssalesforthemonth / 1.07;
> }
> 
> // Function 2: Calculate srvp_calculatedtaxesdue = srvp_calculatedpretax * 0.07.
> function calculateTaxesDue(srvp_calculatedpretax) {
>   return srvp_calculatedpretax * 0.07;
> }
> 
> // Function 3: Set srvp_srvfilingfee to 40.00.
> function setFilingFee() {
>   return 40.00;
> }
> 
> // Function 4: Calculate srvp_calculatedtotal = srvp_calculatedtaxesdue + srvp_srvfilingfee.
> function calculateTotalDue(srvp_calculatedtaxesdue, srvp_srvfilingfee) {
>   return srvp_calculatedtaxesdue + srvp_srvfilingfee;
> }
> 
> // Function 5: Set srvp_totalduecash to srvp_calculatedtotal.
> function setTotalDueCash(srvp_calculatedtotal) {
>   return srvp_calculatedtotal;
> }
> 
> // Function 6: Calculate srvp_totalduecard = srvp_totalduecash * 1.035.
> function calculateTotalDueCard(srvp_totalduecash) {
>   return srvp_totalduecash * 1.035;
> }
> ```
> 
> You can use these functions in your code by passing the required parameters and storing the results accordingly. If you have any questions or need further assistance, feel free to ask!

### User
> i need this as a library to add it to dynamics 365

### Assistant
> Sure, I can provide the JavaScript code as a library that you can add to Dynamics 365. Here's the library version of the functions:
> 
> ```javascript
> // Define a namespace for the library
> var SRVPLibrary = SRVPLibrary || {};
> 
> // Function 1: On edit of srvp_grosssalesforthemonth, divide by 1.07 to get srvp_calculatedpretax.
> SRVPLibrary.calculatePretax = function (srvp_grosssalesforthemonth) {
>   return srvp_grosssalesforthemonth / 1.07;
> };
> 
> // Function 2: Calculate srvp_calculatedtaxesdue = srvp_calculatedpretax * 0.07.
> SRVPLibrary.calculateTaxesDue = function (srvp_calculatedpretax) {
>   return srvp_calculatedpretax * 0.07;
> };
> 
> // Function 3: Set srvp_srvfilingfee to 40.00.
> SRVPLibrary.setFilingFee = function () {
>   return 40.00;
> };
> 
> // Function 4: Calculate srvp_calculatedtotal = srvp_calculatedtaxesdue + srvp_srvfilingfee.
> SRVPLibrary.calculateTotalDue = function (srvp_calculatedtaxesdue, srvp_srvfilingfee) {
>   return srvp_calculatedtaxesdue + srvp_srvfilingfee;
> };
> 
> // Function 5: Set srvp_totalduecash to srvp_calculatedtotal.
> SRVPLibrary.setTotalDueCash = function (srvp_calculatedtotal) {
>   return srvp_calculatedtotal;
> };
> 
> // Function 6: Calculate srvp_totalduecard = srvp_totalduecash * 1.035.
> SRVPLibrary.calculateTotalDueCard = function (srvp_totalduecash) {
>   return srvp_totalduecash * 1.035;
> };
> ```
> 
> To add this library to Dynamics 365, you can follow these steps:
> 
> 1. Log in to your Dynamics 365 environment.
> 
> 2. Navigate to the appropriate area where you want to use the library, such as a custom entity form.
> 
> 3. Open the form in the form designer.
> 
> 4. Go to the "Form Properties" section.
> 
> 5. Click on "Form Libraries" and then click "Add."
> 
> 6. In the "Library Name" field, enter a name for the library, for example, "SRVPLibrary."
> 
> 7. In the "Library" field, paste the entire code block of the library provided above.
> 
> 8. Save and publish the form.
> 
> Now you can use the functions from the library in your Dynamics 365 form scripts. For example, you can call the functions like this:
> 
> ```javascript
> // Assuming srvp_grosssalesforthemonth is the field you want to use for calculation
> var grossSales = Xrm.Page.getAttribute("srvp_grosssalesforthemonth").getValue();
> var calculatedPretax = SRVPLibrary.calculatePretax(grossSales);
> var taxesDue = SRVPLibrary.calculateTaxesDue(calculatedPretax);
> var filingFee = SRVPLibrary.setFilingFee();
> var calculatedTotal = SRVPLibrary.calculateTotalDue(taxesDue, filingFee);
> var totalDueCash = SRVPLibrary.setTotalDueCash(calculatedTotal);
> var totalDueCard = SRVPLibrary.calculateTotalDueCard(totalDueCash);
> 
> // Now you can use totalDueCard for further processing or display it on the form.
> ```
> 
> Please note that the actual implementation and usage may vary based on your specific Dynamics 365 setup and requirements. Always thoroughly test the code before deploying it to your production environment. If you need any further assistance or have any questions, feel free to ask!

### User
> sorry I mean I need to add it as a web resource js file

### Assistant
> No problem! If you want to add the JavaScript code as a web resource in Dynamics 365, follow these steps:
> 
> 1. Prepare the JavaScript code:
>    - Copy the entire library code provided earlier (Function 1 to Function 6) and save it as a new .js file. For example, you can name it "SRVPLibrary.js".
>    - Make sure there are no syntax errors or issues in the code before proceeding.
> 
> 2. Upload the JavaScript file as a web resource:
>    - Log in to your Dynamics 365 environment.
>    - Go to "Settings" > "Customizations" > "Customize the System."
>    - In the left navigation pane, expand "Web Resources."
>    - Click on "New" to create a new web resource.
>    - Provide the following information:
>      - Name: Enter a unique name for the web resource, like "SRVPLibrary".
>      - Display Name: You can give it a user-friendly display name, like "SRVP Library".
>      - Type: Choose "Script (JScript)" for JavaScript files.
>      - Text Editor: Paste the JavaScript code you prepared in step 1 into the text editor.
>      - Check the "Publish" box to publish the web resource immediately.
>    - Click "Save" and then "Publish" to make the web resource available.
> 
> 3. Use the web resource in forms or scripts:
>    - Once the web resource is created and published, you can use it in different forms or scripts within Dynamics 365.
>    - Navigate to the form where you want to use the functions from the library.
>    - Open the form in the form designer.
>    - Go to the "Form Properties" section.
>    - Click on "Form Libraries" and then click "Add."
>    - In the "Library Name" field, enter a name for the library, like "SRVPLibrary".
>    - In the "Library" field, click on the magnifying glass icon and select the web resource you created earlier (e.g., "SRVPLibrary.js").
>    - Click "Add" and then "OK" to close the form library window.
>    - Save and publish the form.
> 
> 4. Use the functions in form scripts:
>    - Now you can use the functions from the web resource library in your form scripts as demonstrated in the previous response.
> 
> For example, assuming the form has a field named "srvp_grosssalesforthemonth," you can use the library functions like this:
> 
> ```javascript
> var grossSales = Xrm.Page.getAttribute("srvp_grosssalesforthemonth").getValue();
> var calculatedPretax = SRVPLibrary.calculatePretax(grossSales);
> var taxesDue = SRVPLibrary.calculateTaxesDue(calculatedPretax);
> var filingFee = SRVPLibrary.setFilingFee();
> var calculatedTotal = SRVPLibrary.calculateTotalDue(taxesDue, filingFee);
> var totalDueCash = SRVPLibrary.setTotalDueCash(calculatedTotal);
> var totalDueCard = SRVPLibrary.calculateTotalDueCard(totalDueCash);
> 
> // Now you can use totalDueCard for further processing or display it on the form.
> ```
> 
> Remember to test thoroughly before deploying changes to your production environment. If you have any questions or need further assistance, feel free to ask!

### User
> give me the code all together I got confused. sorry

### Assistant
> No problem! Here's the entire code for the JavaScript library as a web resource in Dynamics 365:
> 
> 1. Save the following code as a new .js file (e.g., "SRVPLibrary.js"):
> 
> ```javascript
> // Define a namespace for the library
> var SRVPLibrary = SRVPLibrary || {};
> 
> // Function 1: On edit of srvp_grosssalesforthemonth, divide by 1.07 to get srvp_calculatedpretax.
> SRVPLibrary.calculatePretax = function (srvp_grosssalesforthemonth) {
>   return srvp_grosssalesforthemonth / 1.07;
> };
> 
> // Function 2: Calculate srvp_calculatedtaxesdue = srvp_calculatedpretax * 0.07.
> SRVPLibrary.calculateTaxesDue = function (srvp_calculatedpretax) {
>   return srvp_calculatedpretax * 0.07;
> };
> 
> // Function 3: Set srvp_srvfilingfee to 40.00.
> SRVPLibrary.setFilingFee = function () {
>   return 40.00;
> };
> 
> // Function 4: Calculate srvp_calculatedtotal = srvp_calculatedtaxesdue + srvp_srvfilingfee.
> SRVPLibrary.calculateTotalDue = function (srvp_calculatedtaxesdue, srvp_srvfilingfee) {
>   return srvp_calculatedtaxesdue + srvp_srvfilingfee;
> };
> 
> // Function 5: Set srvp_totalduecash to srvp_calculatedtotal.
> SRVPLibrary.setTotalDueCash = function (srvp_calculatedtotal) {
>   return srvp_calculatedtotal;
> };
> 
> // Function 6: Calculate srvp_totalduecard = srvp_totalduecash * 1.035.
> SRVPLibrary.calculateTotalDueCard = function (srvp_totalduecash) {
>   return srvp_totalduecash * 1.035;
> };
> ```
> 
> 2. Upload the "SRVPLibrary.js" file as a web resource:
>    - Log in to your Dynamics 365 environment.
>    - Go to "Settings" > "Customizations" > "Customize the System."
>    - In the left navigation pane, expand "Web Resources."
>    - Click on "New" to create a new web resource.
>    - Provide the following information:
>      - Name: "SRVPLibrary"
>      - Display Name: "SRVP Library"
>      - Type: "Script (JScript)"
>      - Text Editor: Paste the entire code from the "SRVPLibrary.js" file into the text editor.
>      - Check the "Publish" box to publish the web resource immediately.
>    - Click "Save" and then "Publish" to make the web resource available.
> 
> 3. Use the library in form scripts:
>    - Navigate to the form where you want to use the functions from the library.
>    - Open the form in the form designer.
>    - Go to the "Form Properties" section.
>    - Click on "Form Libraries" and then click "Add."
>    - In the "Library Name" field, enter "SRVPLibrary".
>    - In the "Library" field, click on the magnifying glass icon and select the web resource you created earlier (e.g., "SRVPLibrary.js").
>    - Click "Add" and then "OK" to close the form library window.
>    - Save and publish the form.
> 
> 4. Use the functions in form scripts:
>    - Now you can use the functions from the web resource library in your form scripts as demonstrated in the previous responses.
> 
> For example, assuming the form has a field named "srvp_grosssalesforthemonth," you can use the library functions like this:
> 
> ```javascript
> var grossSales = Xrm.Page.getAttribute("srvp_grosssalesforthemonth").getValue();
> var calculatedPretax = SRVPLibrary.calculatePretax(grossSales);
> var taxesDue = SRVPLibrary.calculateTaxesDue(calculatedPretax);
> var filingFee = SRVPLibrary.setFilingFee();
> var calculatedTotal = SRVPLibrary.calculateTotalDue(taxesDue, filingFee);
> var totalDueCash = SRVPLibrary.setTotalDueCash(calculatedTotal);
> var totalDueCard = SRVPLibrary.calculateTotalDueCard(totalDueCash);
> 
> // Now you can use totalDueCard for further processing or display it on the form.
> ```
> 
> Remember to test thoroughly before deploying changes to your production environment. If you have any questions or need further assistance, feel free to ask!
