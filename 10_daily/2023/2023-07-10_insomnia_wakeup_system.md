---
layout: page
title: "Insomnia Wakeup System"
slug: "insomnia_wakeup_system"
created_at: "2023-07-10 06:02:39"
updated_at: "2023-07-10 06:02:39"
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
date: 2023-07-10
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "dceb5433-913d-44bf-901c-dc2f5c532306"
canonical_ref: ""
---

# Insomnia Wakeup System

## Overview
- **Date**: 2023-07-10 06:02:39
- **Conversation ID**: `dceb5433-913d-44bf-901c-dc2f5c532306`
- **Source**: `__CaptainsLogchatexports (1).json`

## Chat History

### User
> I want to make either an app or a flow, or something that will make sure I am out of bed. I have insomnia and currently I have a script setup on alexa, that at a certain time, she starts talking, turns volumn all the way up, turns on my tv and my lights in the room, and turns on a vibrator in my bed. but even when I am unconscious I am able to say "Alex Cancel", and its stops, I have it set to do it like 3 times and somehow I can still turn it off.

### Assistant
> It sounds like you've built a very sophisticated wakeup system already. However, you're right in identifying that it still has a flaw, which is the fact that you can cancel the alarms while still half-asleep. Here's an idea for a system that will force you to fully wake up and engage with something before it stops.
> 
> 1. **Use a different smart speaker**: Instead of using Alexa, consider using a Google Home device. This is because you can set up Google Routines to require you to say a specific phrase before it stops the routine. You could set up a long and complex phrase that you'd have to fully wake up and think about before you could say it correctly.
> 
> 2. **Use a smart light**: You've already incorporated this into your setup, but make sure the light is set to gradually get brighter over a period of 30 minutes or so. This simulates a sunrise and is a gentler way to wake up than sudden, bright light.
> 
> 3. **Incorporate physical movement**: You can use a smart outlet to control a loud device in a different room (like a radio or a buzzer), so you have to physically get out of bed and walk to another room to turn it off. 
> 
> 4. **Integrate a task**: If you have a smart lock or a smart coffee maker, you could set up a routine where you have to unlock the front door or start the coffee maker within a certain amount of time after the alarm starts, or else it will keep going. This would force you to do a more complex task that will fully wake you up.
> 
> 5. **App solutions**: There are several apps on the market that require you to complete tasks in order to turn off the alarm. For example, 'Alarmy' has features that require you to solve math problems, shake the phone a certain number of times, or even scan a barcode or QR code in your home to turn off the alarm. 
> 
> 6. **Consider sleep hygiene**: Finally, while technology can definitely help you wake up, it's also important to consider your sleep hygiene. If you're having trouble staying awake during the day and falling asleep at night, you might want to look into your caffeine intake, screen time before bed, bedtime routine, and sleep environment to make sure they're all conducive to a good night's sleep. You may also want to speak to a healthcare provider about your insomnia, as there may be underlying issues that need to be addressed.
>    
> Remember, while technology can help, it's not a substitute for good sleep habits or medical advice if you're experiencing insomnia or other sleep issues.

### User
> ok so lets break thsi down into its components, Google Home, Alexa, Bedroom Light 1, 2, and Hue, Bed Vibrator, Roku TV. Here is what you can work with. I have to be up and awake no later than 12pm on Monday Tuesday, wednesday thursday, friday, saturday and sunday, would it make sense to have the "Codys Alarm" do something short small at 10 like a quick vibrations of the bed, then at 1030 turn on the hue light at 10%, then from there get lauder and heaver and more and more until by 12pm its like a circus in my room and I cannot shut it off unless I say, I would like to have some super califradulistcsespialidous on the side, drivers license number 17 20 65 96 56

### Assistant
> Absolutely, creating a gradual alarm system sounds like a great idea. It would help your body gradually adjust to being awake rather than jolting you awake with a loud noise or bright light.
> 
> Here's a rough sketch of a system you could implement:
> 
> **10:00 AM**:
> The bed vibrator initiates a gentle wake-up process by vibrating lightly for a few minutes. You could use a smart plug to trigger this device.
> 
> **10:30 AM**:
> The Philips Hue light in your room turns on at 10% brightness, mimicking the early sunrise. You can configure this in the Philips Hue app or through a smart home system like Google Home.
> 
> **11:00 AM**:
> The Hue light gradually increases to 50% brightness. At the same time, your Bedroom Lights 1 and 2 switch on at low brightness. Alexa or Google Home could start playing some gentle, relaxing music, slowly increasing the volume.
> 
> **11:30 AM**:
> The Hue light increases to 100% brightness, and Bedroom Lights 1 and 2 increase to their full brightness. The bed vibrator starts shaking more heavily, and the music volume increases further.
> 
> **11:50 AM**:
> Your Roku TV turns on and starts playing a high-energy show, movie, or music channel. The music from the smart speaker and the bed vibrator continue their routine.
> 
> **12:00 PM**:
> The music volume reaches its maximum level, and the bed vibrator shakes as strongly as it can. The smart speaker asks you for the passphrase. 
> 
> Only when you say "I would like to have some super califragilisticexpialidocious on the side, drivers license number 17 20 65 96 56", will everything be turned off.
> 
> Remember, all these actions can be set up with routines or flows in Google Home or Alexa (or another smart home controller). However, you may need to use third-party apps or integrations to control certain devices. For example, the Roku TV might need to be controlled using a service like Harmony, or the vibrator might need to be controlled using its own app or a smart plug.
> 
> The exact setup will depend on the specific devices you have and the integrations they support. If you can't set up everything using one system, you might need to use a more complex setup with several different apps and services. 
> 
> In addition, for the voice passphrase, you can set up a routine with Google Home to recognize the specific phrase and then stop the alarm, but I'm not aware of a similar functionality with Alexa as of my knowledge cutoff in September 2021. Please check the most current capabilities of your devices.

### User
> all these devices work through the alexa thankfully, can you provide me with draft of the schema for alexa for me to set up now?

### Assistant
> Certainly, here's a draft schema for you. Note that your device compatibility and the exact wording may vary, and you might have to adjust things a bit depending on your specific devices and their Alexa Skills.
> 
> 1. **10:00 AM - Bed Vibrator**:
> Create a routine named "Bed Vibrator Start" that starts at 10:00 AM every day of the week. The action should be "Device Settings" -> "Power" -> "On" for your bed vibrator device.
> 
> 2. **10:30 AM - Philips Hue Light**:
> Create a routine named "Light Start" that starts at 10:30 AM every day of the week. The action should be "Device Settings" -> "Brightness" -> "10%" for your Philips Hue light.
> 
> 3. **11:00 AM - Increase Light Intensity and Start Music**:
> Create a routine named "Music Start" that starts at 11:00 AM every day of the week. This routine should include two actions. The first action should be "Device Settings" -> "Brightness" -> "50%" for your Philips Hue light. The second action should be "Music" -> (select your music provider) -> (select a gentle playlist or song).
> 
> 4. **11:30 AM - Increase Light Intensity, More Music, and Bed Vibrator**:
> Create a routine named "Wake Up More" that starts at 11:30 AM every day of the week. The first action should be "Device Settings" -> "Brightness" -> "100%" for your Philips Hue light. The second action should be "Device Settings" -> "Power" -> "On" for your Bedroom Lights 1 and 2. The third action should be "Device Settings" -> "Increase Sound" for your bed vibrator (if available). The fourth action should be "Music" -> (select your music provider) -> (select a more energetic playlist or song).
> 
> 5. **11:50 AM - Roku TV On**:
> Create a routine named "TV On" that starts at 11:50 AM every day of the week. The action should be "Device Settings" -> "Power" -> "On" for your Roku TV. Depending on the Skill you're using to control the Roku, you may also be able to start a specific channel or show.
> 
> 6. **12:00 PM - Maximum Volume and Lights**:
> Create a routine named "Final Wake Up" that starts at 12:00 PM every day of the week. The action should be "Device Settings" -> "Brightness" -> "100%" for your Bedroom Lights 1 and 2, and "Device Settings" -> "Volume" -> "10" for your Alexa device. 
> 
> After setting up these routines, you need to create a "Custom Routine" that will stop all the actions when you say the passphrase. Here are the steps:
> 
> 1. In the Alexa app, tap on 'More' and select 'Routines'.
> 2. Tap on the '+' icon to create a new routine.
> 3. Under 'When this happens', choose 'Voice' and type in your passphrase: "I would like to have some super califragilisticexpialidocious on the side, drivers license number 17 20 65 96 56".
> 4. Tap 'Next' and then under 'Add action' select 'Device Settings'.
> 5. Here you should add all the devices that need to be turned off, set the bedroom lights to the normal brightness level, stop the music, turn off the Roku TV, etc. 
> 
> Remember, Alexa's routines capabilities could have changed after my last update in September 2021, so be sure to refer to the most current documentation or help resources if you encounter any difficulties. Also, be patient with the setup – it may take a little time and adjustment to get everything working just the way you want.

### User
> I want to make a door bell shortcut on my iphone using scripting in shortcuts app. Basically, if I receive a text message that says "

### Assistant
> If you'd like to create a shortcut on your iPhone that triggers when you receive a specific text message, here's an example of how you could do it. However, as of my knowledge cutoff in September 2021, there's no direct way to trigger a shortcut based on the content of a received text message due to privacy restrictions. But we can use a workaround, using automation based on an incoming message from a specific person and then using an 'If' statement to check for the specific message content. 
> 
> 1. Open the Shortcuts app on your iPhone.
> 2. Tap "Automation" at the bottom.
> 3. Tap the "+" button to create a new automation.
> 4. Tap "Create Personal Automation".
> 5. Scroll down and tap "Message".
> 6. Select "is Received" and choose the sender from whom you'll receive the specific text message.
> 7. Tap "Next".
> 8. Now, you'll set up the actions that will happen when you receive a message from the selected contact. Tap "Add Action".
> 9. Tap "Scripting".
> 10. Tap "If".
> 11. In the condition, tap "Choose" and select "Text". Then tap the second "Choose" and select "Input". Now you should see "If Text Input". Tap on "Input" and type the specific message you're expecting, e.g., "Ding Dong".
> 12. After setting up the condition, tap "Add Action" below the "Then" statement.
> 13. You can now select what you want to happen if the condition is met. For example, if you want to play a sound, you could select "Play Sound". If you want to send a reply, you could select "Send Message", etc.
> 14. Once you've set up your action, tap "Next".
> 15. Review the automation. Make sure "Ask Before Running" is turned off to ensure the automation runs automatically. Then tap "Done".
> 
> This automation should now run whenever you receive a message from the selected contact. If the message matches the specific text you set, it will perform the action(s) you specified.
> 
> Please note that due to privacy and security reasons, Apple might not allow direct triggering of automations based on message content. The options available to you might also depend on the updates and changes Apple has made to the Shortcuts app and iOS since my knowledge cutoff in September 2021. Please refer to the most recent user manuals or help resources for the best results.

### User
> Ding dong it will open the alexa app and start the ding dong sound

### Assistant
> Unfortunately, Apple's Shortcuts app does not allow direct interaction with the Alexa app as of my knowledge cutoff in September 2021. However, you can create a workaround using a smart home device like an Amazon Echo to play the sound.
> 
> Here's how you could set it up:
> 
> 1. First, create a routine in the Alexa app to play the sound when a specific phrase is spoken. 
>     - Open the Alexa app.
>     - Go to "More" > "Routines".
>     - Tap "+" to create a new routine.
>     - For "When this happens", select "Voice" and enter a phrase like "Play doorbell sound".
>     - For "Add action", select "Sounds" > "Doorbells" and choose the "Ding Dong" sound.
>     - Save the routine.
> 
> 2. Next, create an automation in the Shortcuts app that will make Siri say the phrase to trigger the Alexa routine when you receive a specific text message. The Alexa device should be able to pick up the command from Siri if it's close to your iPhone. 
>     - Open the Shortcuts app and go to "Automation".
>     - Tap "+" to create a new automation.
>     - Select "Create Personal Automation".
>     - Scroll down and tap "Message".
>     - Select "is Received" from a specific sender.
>     - Add an action and select "Speak Text".
>     - For the text, enter the phrase you used in the Alexa routine ("Play doorbell sound").
>     - Turn off "Ask Before Running" and save the automation.
> 
> Now, when you receive a specific text message, Siri will say the phrase to trigger the Alexa routine and play the doorbell sound.
> 
> Remember that this setup has limitations, and it may not always work as expected. For example, the Alexa device may not always pick up the command from Siri, especially if there's background noise or if the devices are not close enough to each other.
> 
> As always, the options available to you might depend on updates and changes made to the Shortcuts app, the Alexa app, and iOS after my knowledge cutoff in September 2021. Please refer to the most recent user manuals or help resources for the best results.
