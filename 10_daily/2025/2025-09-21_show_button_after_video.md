---
layout: page
title: "Show button after video"
slug: "show_button_after_video"
created_at: "2025-09-21 17:41:04"
updated_at: "2026-07-18T11:03:12-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-000.json"
template_key: master-template
date: 2025-09-21
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "68d07ef4-88b4-8320-8ac9-7b737d822990"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Show button after video

## Overview
- **Date**: 2025-09-21 17:41:04
- **Conversation ID**: `68d07ef4-88b4-8320-8ac9-7b737d822990`
- **Source**: `Chat-Export-28513-2026/conversations-000.json`

## Chat History

### User
> how do i get a button on a site to show the video is over ot continue in dev.

### Assistant
> Add a `video` event listener and toggle the button visibility/state when it ends. Example:  
> 
> ```html
> <video id="myVideo" controls>
>   <source src="your-video.mp4" type="video/mp4">
> </video>
> 
> <button id="continueBtn" style="display:none;">Continue</button>
> 
> <script>
> const video = document.getElementById('myVideo');
> const btn = document.getElementById('continueBtn');
> 
> video.addEventListener('ended', () => {
>   btn.style.display = 'inline-block'; // show button
> });
> 
> btn.addEventListener('click', () => {
>   // do whatever "continue" means in dev
>   console.log('Continuing...');
> });
> </script>
> ```
> 
> Key point: `video.addEventListener('ended', ...)` fires once playback finishes.  
> Would you like me to make the button disabled instead of hidden until the video ends?
