---
layout: page
title: "Photo authenticity check"
slug: "photo_authenticity_check"
created_at: "2025-09-10 06:45:57"
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
date: 2025-09-10
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "68c164dd-83ec-8322-9479-9b64f500e103"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Photo authenticity check

## Overview
- **Date**: 2025-09-10 06:45:57
- **Conversation ID**: `68c164dd-83ec-8322-9479-9b64f500e103`
- **Source**: `Chat-Export-28513-2026/conversations-000.json`

## Chat History

### User
> how can i use photos taken during the war in khost and see meta deta that can help confirm the authenticity of these photos

### Assistant
> If you’ve got photos from Khost during the war and you want to check their authenticity, metadata can definitely help—but it’s a slippery game because metadata can be stripped, faked, or degraded over time. Here’s how you can tackle it:  
> 
> ---
> 
> ### Step 1: Extract the metadata
> Digital photos usually carry **EXIF data** (Exchangeable Image File Format). This can include:
> - Timestamp of when the picture was taken
> - Camera model and serial number
> - GPS coordinates (if the device had location enabled)
> - Editing history in some cases
> 
> **Tools you can use:**
> - On Windows: right-click photo → *Properties* → *Details*  
> - On macOS: Preview → *Tools* → *Show Inspector* → *Info* tab  
> - Cross-platform: `exiftool` (command-line, very thorough)  
>   ```
>   exiftool yourphoto.jpg
>   ```
> - Online: websites like *metapicz.com* or *exif.regex.info* (but be careful uploading sensitive war photos to random sites).  
> 
> ---
> 
> ### Step 2: Look for consistency
> - **Date & time:** Do they line up with the known timeline of events in Khost? Cross-check with news reports or known attacks on specific days.  
> - **GPS data:** Some smartphones embed latitude/longitude. Plug into Google Maps or OpenStreetMap—does it drop you in Khost?  
> - **Device info:** Was the camera model something common in Afghanistan at the time? An iPhone 15 in 2010 is a dead giveaway of tampering.  
> - **Edits:** If EXIF shows repeated “Adobe Photoshop” saves, authenticity drops.  
> 
> ---
> 
> ### Step 3: Cross-reference beyond metadata
> - **Shadows & light:** Compare sun/shadow angles with actual time of day in Khost on that date (websites like SunCalc let you check).  
> - **Landmarks:** Mountains, mosques, and streets don’t lie. Match with satellite imagery (Google Earth historical view can rewind to that year).  
> - **Clothing & vehicles:** Do uniforms, license plates, or car models match the year and location?  
> 
> ---
> 
> ### Step 4: Watch for red flags
> - Missing metadata isn’t unusual (many platforms strip it), but oddly perfect metadata that looks too neat may be fabricated.  
> - Inconsistencies—like a timestamp in U.S. timezone or GPS from a different country—don’t automatically prove fakes, but they deserve digging.  
> 
> ---
> 
> Want me to show you a ready-to-use script (say in Python with `exifread` or `pillow`) that can pull out and display metadata cleanly so you don’t have to dig through each photo manually? That way you could run it on a folder of Khost photos and get a structured report.

### User
> give me workflow/presentation suggestions

### Assistant
> Got it—let’s turn this into a tight workflow you can present (like a case-building or authenticity-check walkthrough). Think of it like a layered sieve: every stage either strengthens or weakens the photo’s credibility.  
> 
> ---
> 
> ## **Workflow: Authenticating War Photos (Khost Example)**
> 
> ### **1. Collection & Preservation**
> - Gather photos in original format (avoid screenshots or re-uploads).  
> - Make working copies; keep originals untouched.  
> - Note source (who gave it, when, in what context).
> 
> ---
> 
> ### **2. Metadata Extraction**
> - Run **EXIF/metadata scan** with `exiftool` or Python script.  
> - Log: date/time, device model, GPS, software used.  
> - Store results in a structured table (CSV or spreadsheet).
> 
> ---
> 
> ### **3. Metadata Analysis**
> - **Timeline check**: Does timestamp match known events in Khost?  
> - **Geolocation check**: Plot GPS on map.  
> - **Device check**: Was this device plausible for that place and year?  
> - **Editing footprint**: Look for “Photoshop” or multiple software tags.
> 
> ---
> 
> ### **4. Visual Cross-Reference**
> - **Environmental cues**: Compare background terrain, buildings, or signage with satellite imagery (Google Earth historical).  
> - **Sun & shadow analysis**: Use SunCalc to check if shadows align with date/time metadata.  
> - **Clothing/vehicles**: Cross-check with known military uniforms, license plates, or regional vehicle models.
> 
> ---
> 
> ### **5. Consistency & Corroboration**
> - Compare multiple photos from the set—do they share the same camera, timestamps in sequence, and consistent GPS?  
> - Cross-validate with external sources (news reports, NGO docs, eyewitness accounts).  
> - Look for anomalies (e.g., sudden camera change mid-event, timestamps jumping around).
> 
> ---
> 
> ### **6. Documentation & Presentation**
> - Create a **report deck** (slides or PDF) with:  
>   - Photo + key metadata (side-by-side)  
>   - Maps with plotted GPS  
>   - Shadow/sunlight diagrams  
>   - Annotated visuals highlighting matching landmarks  
> - Use a **traffic-light authenticity score**:  
>   - ✅ Strongly consistent  
>   - ⚠️ Mixed/needs caution  
>   - ❌ Likely altered/inconsistent  
> 
> ---
> 
> ### **7. Preservation for Review**
> - Keep a digital chain of custody log: who accessed photos, when, and what tools were used.  
> - Save all raw analysis outputs for transparency (metadata dumps, maps, etc.).
> 
> ---
> 
> ## **Presentation Suggestions**
> - **Narrative framing**: “We’re not proving truth absolutely, we’re weighing likelihood through multiple independent checks.”  
> - **Visuals over text**: Show maps, timelines, and side-by-sides—don’t drown people in raw EXIF dumps.  
> - **Progressive reveal**: Start with photo, then layer metadata, then external checks, then final assessment.  
> - **Comparative example**: Show one *authentic-looking* vs one *tampered* example so audience understands the difference.
> 
> ---
> 
> Do you want me to sketch out a **sample slide deck outline** (like slide titles + what goes on each) so you could plug in your Khost photos and findings? That way the workflow becomes a ready-to-present package.
