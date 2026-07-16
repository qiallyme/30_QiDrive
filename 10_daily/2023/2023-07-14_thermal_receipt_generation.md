---
layout: page
title: "Thermal Receipt Generation"
slug: "thermal_receipt_generation"
created_at: "2023-07-14 12:25:59"
updated_at: "2026-07-16T06:49:27-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "__CaptainsLogchatexports (1).json"
template_key: master-template
date: 2023-07-14
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "31c0c5f5-f6ed-4965-99bc-c2975a7e45af"
canonical_ref: ""
---

# Thermal Receipt Generation

## Overview
- **Date**: 2023-07-14 12:25:59
- **Conversation ID**: `31c0c5f5-f6ed-4965-99bc-c2975a7e45af`
- **Source**: `__CaptainsLogchatexports (1).json`

## Chat History

### User
> make me a recedipt ot print in thermal. 
> InvoiceRecent #12886 
>  Help
> Client 
> Ellington Montenegro Padilla (NO NOT SERVICE)
> This customer is not tax exempt
>  
> Client email Cc/Bcc
> ellingtonalbertom@gmail.com
>  Send later  
> Payment methods
> Cards
> Bank transfer
> Tips
> Gracias por ser nuestro client. Aceptamos tarjetas de crédito, pagos ACH y Zelle. Puede enviar su pago de Zelle a Contact@cjr-co.com
> Edit payment methods
> BALANCE DUE
> $100.00
>  
> Last Delivery: Sent by email to ellingtonalbertom@gmail.com at Jul 14, 1:23 pm Eastern Daylight Time
> Billing address
> Ellington Montenegro Padilla
> 2223 Sumter St. Apt B
> Indianapolis, IN  46224 US
> + Shipping information
> Terms 
> Due on receipt
> Invoice date
> 07/14/2023
> Create recurring invoice
> Due date
> 07/15/2023
> Late fees apply
> Location
> SRV-Indy
> Location of sale
> 3585 Commercial Dr730, Indianapolis, IN, 46222, USA
> #
> SERVICE DATE
> PRODUCT/SERVICE 
> DESCRIPTION
> QTY
> RATE
> AMOUNT
> TAX
>    
> Message on invoice
> This will show up on the invoice.
> Message on statement
> If you send statements to clients, this will show up as the description for this invoice.
> Subtotal	$100.00
>   
> Taxable subtotal $0.00
> Select tax rate
> Based on location
> Need help with sales tax? Learn more
> 
>  
> $0.00
> See the math
> $0.00
> Total	
> $100.00
> Balance due	
> $100.00
>  Attachments Maximum size: 20MB
> Drag/Drop files here or click the icon
> Show existing
> Activities
> 07/14/2023
> TODAY
> Ellington Montenegro Padilla (NO NOT SERVICE) Viewed this invoice.
> 07/14, 1:24 pm Eastern Daylight Time
> You Sent this invoice.
> 07/14, 1:23 pm Eastern Daylight Time

### Assistant
> I can help you generate a receipt to print in thermal format based on the information you provided. Here's an example of a receipt:
> 
> ```
> ----------------------------------
>          INVOICE RECEIPT
> ----------------------------------
> 
> Invoice Recent #12886
> 
> Client:
> Ellington Montenegro Padilla (NO NOT SERVICE)
> This customer is not tax exempt
> 
> Client email Cc/Bcc:
> ellingtonalbertom@gmail.com
> 
> Payment methods:
> - Cards
> - Bank transfer
> 
> Tips:
> Gracias por ser nuestro cliente. Aceptamos tarjetas de crédito, pagos ACH y Zelle. Puede enviar su pago de Zelle a Contact@cjr-co.com
> 
> BALANCE DUE
> $100.00
> 
> Last Delivery:
> Sent by email to ellingtonalbertom@gmail.com at Jul 14, 1:23 pm Eastern Daylight Time
> 
> Billing address:
> Ellington Montenegro Padilla
> 2223 Sumter St. Apt B
> Indianapolis, IN 46224 US
> 
> Shipping information:
> 
> Terms: Due on receipt
> Invoice date: 07/14/2023
> Due date: 07/15/2023
> Late fees apply
> 
> Location: SRV-Indy
> Location of sale:
> 3585 Commercial Dr730, Indianapolis, IN, 46222, USA
> 
> ----------------------------------
>        PRODUCT/SERVICE DETAILS
> ----------------------------------
> 
> SERVICE DATE        PRODUCT/SERVICE          QTY    RATE    AMOUNT   TAX
> ------------------------------------------------------------------------
>                                        Subtotal:  $100.00
>                                  Taxable subtotal:  $0.00
>                              Total (including tax):  $100.00
> 
> ----------------------------------
>         ACTIVITIES & MESSAGES
> ----------------------------------
> 
> Activities:
> - TODAY: Ellington Montenegro Padilla (NO NOT SERVICE) viewed this invoice.
> - 07/14, 1:24 pm Eastern Daylight Time: You sent this invoice.
> - 07/14, 1:23 pm Eastern Daylight Time: Last delivery sent to ellingtonalbertom@gmail.com
> 
> Message on invoice:
> This will show up on the invoice.
> 
> Message on statement:
> If you send statements to clients, this will show up as the description for this invoice.
> 
> ----------------------------------
>            THANK YOU FOR YOUR BUSINESS!
> ----------------------------------
> ```
> 
> Please note that this is just a sample receipt based on the information provided. You can customize it further according to your specific needs and branding.

### User
> is ther a way to creat a button on an app that will invoke facetime

### Assistant
> Yes, it is possible to create a button in an app that can invoke FaceTime. Here's an example of how you can achieve this in iOS using Swift:
> 
> 1. Open your Xcode project and go to the view controller where you want to add the button.
> 
> 2. Add a button to your view controller's interface. You can either do this programmatically in your code or by using Interface Builder.
> 
> 3. In the action method of the button, you can use the `UIApplication.shared.open` method to invoke FaceTime with a specific phone number. Here's an example of how you can do this:
> 
> ```swift
> import UIKit
> 
> class ViewController: UIViewController {
>     @IBAction func facetimeButtonTapped(_ sender: UIButton) {
>         let phoneNumber = "1234567890" // Replace with the desired phone number
>         let url = URL(string: "facetime://\(phoneNumber)")!
>         
>         if UIApplication.shared.canOpenURL(url) {
>             UIApplication.shared.open(url, options: [:], completionHandler: nil)
>         } else {
>             // FaceTime is not available on this device
>             // Handle the error or display an alert to the user
>         }
>     }
>     
>     // Rest of your view controller code...
> }
> ```
> 
> 4. Customize the `phoneNumber` variable with the desired phone number you want to call via FaceTime.
> 
> 5. Run your app, and when the button is tapped, it will invoke FaceTime with the specified phone number.
> 
> Remember to handle cases where FaceTime may not be available on the user's device and provide appropriate error handling or user feedback.

### User
> let say I want to add a button to my page sites that will invoke facetime on the ipad

### Assistant
> If you want to add a button to a webpage that can invoke FaceTime on an iPad, you can use HTML and JavaScript to achieve this functionality. However, please note that invoking FaceTime directly from a webpage may not be possible due to security restrictions imposed by web browsers. Instead, you can create a link that opens the FaceTime app on the iPad with a specific phone number.
> 
> Here's an example of how you can create a button that opens FaceTime on an iPad:
> 
> ```html
> <button onclick="openFaceTime()">Call via FaceTime</button>
> 
> <script>
> function openFaceTime() {
>   var phoneNumber = "1234567890"; // Replace with the desired phone number
>   var url = "facetime://" + phoneNumber;
>   
>   window.location.href = url;
> }
> </script>
> ```
> 
> In the above code, the `openFaceTime()` function is triggered when the button is clicked. It constructs the FaceTime URL with the desired phone number and sets `window.location.href` to that URL. When the user clicks the button, it will attempt to open the FaceTime app on their iPad with the specified phone number.
> 
> Please note that this code will work on an iPad if the user has FaceTime installed and their browser allows the opening of FaceTime URLs. However, the exact behavior may vary depending on the user's device and browser settings.
