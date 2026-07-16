---
layout: page
title: "Interactive personal documentation"
slug: "interactive_personal_documentation"
created_at: "2025-12-13 08:52:38"
updated_at: "2025-12-13 08:52:38"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-002.json"
template_key: master-template
date: 2025-12-13
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "693d7db5-9f60-8331-80b9-737fbbb4b7bc"
canonical_ref: ""
---

# Interactive personal documentation

## Overview
- **Date**: 2025-12-13 08:52:38
- **Conversation ID**: `693d7db5-9f60-8331-80b9-737fbbb4b7bc`
- **Source**: `Chat-Export-28513-2026/conversations-002.json`

## Chat History

### User
> For my website my personal one honestly what I want if I really think about it is like a documentation site but slightly interactive to help guide someone to learning about me if they wish while still working like a dev docs site they can go to the sections they want ect. Kinda how Microsoft has theirs where you can take the courses and be guided or just go to the sections you want to see. But the navigation or directory tree is in the sidebar with everything kinda like a Zoho wiki and I don’t want to build just a static HTML site so I can easily edit online without building or nothing

### Assistant
> You’re describing a **docs-first “Manual to Me” portal**:
> 
> - Left sidebar = the full tree (browse-anywhere).
> - “Guided paths” = optional sequences (like Microsoft Learn modules).
> - Light interactivity (checklists, sliders, self-assessments), but still fundamentally readable docs.
> - **Browser editing** with no local builds.
> 
> You already have the right UX instincts in your existing HTML: sticky top nav plus an aside that can serve as the “docs sidebar / quick links” pattern. fileciteturn1file6L22-L58
> 
> ## The honest constraint
> If you want **(A) docs UX** + **(B) custom domain** + **(C) private/Zero Trust** + **(D) edit in browser** + **(E) no builds**, you’re almost certainly looking at a **hosted docs/wiki platform** (or a self-hosted wiki with a built-in editor). A “pure static site” can do A/C, but it typically fails D/E unless you accept Git-based editing (which is still a “build,” just done by CI behind the scenes).
> 
> ## Best-fit options (ranked)
> ### 1) GitBook (hosted docs)
> **Why it matches:** Docs UX out of the box (sidebar tree, search, nav), **in-browser editing**, collections/spaces, good for “guided paths” via ordered pages.  
> **Privacy:** Can be private; can also be protected further behind Cloudflare Access if you want.
> 
> ### 2) Outline (wiki/docs hybrid)
> **Why it matches:** Clean docs feel, strong sidebar tree, great writing experience, permissions, collections. It’s more “Zoho wiki vibe” than “blog.”  
> **Tradeoff:** Usually self-hosted (or managed via a host), meaning a little more ops than GitBook, but still *no build workflow* for you.
> 
> ### 3) Wiki.js (self-hosted wiki)
> **Why it matches:** Tree nav, good editor, flexible auth options.  
> **Tradeoff:** More admin overhead than Outline for your use case.
> 
> ## What I would do for you (cleanest path)
> **GitBook for the content + Cloudflare Access for privacy.**
> 
> That gives you:
> - Microsoft-docs style navigation immediately (tree + search + sections).
> - “Guided” learning tracks by simply curating page order.
> - You edit everything in the browser.
> - Cloudflare Access puts it behind a login wall without you engineering auth.
> 
> ## Structure that will feel like “Microsoft Learn for Cody”
> Create **two parallel ways to navigate**:
> 
> ### A) Browse tree (left sidebar)
> Top-level buckets (example):
> - **Start Here**
>   - What this is
>   - How to use it
> - **Operating Manual**
>   - How I communicate
>   - How I work
>   - Boundaries & triggers
>   - Support playbook
> - **Story & Context**
>   - Timeline (high level)
>   - Patterns (deep dive)
> - **Work With Me**
>   - Services / strengths
>   - Working agreements
>   - FAQs
> 
> Your existing writing already leans naturally into “documentation as self-advocacy” (which is the perfect anchor theme for this site). fileciteturn1file16L68-L76
> 
> ### B) Guided paths (like courses)
> Make “Paths” that are just curated reading sequences:
> - **Path: Friend/Family (10 minutes)**
> - **Path: New Partner (30 minutes)**
> - **Path: Client/Employer (20 minutes)**
> - **Path: Conflict Repair / When I’m Overwhelmed (5 minutes)**
> 
> Each path is: Overview → 3–7 pages → quick checklist at the end.
> 
> ## Interactivity (without turning it into an app)
> Keep it lightweight:
> - Checklists (“Do / Don’t”)
> - “If this, then that” decision trees
> - A couple embedded tools (like sliders or a short self-assessment) *only where it adds value*
> 
> You’ve already prototyped interactive UI patterns (e.g., slider-based assessments) in your existing HTML assets, which can be repurposed as embedded pages if you want. fileciteturn1file12L1-L14
> 
> ## Fast next steps (no overengineering)
> 1) Pick platform: **GitBook** (recommended) or **Outline**.  
> 2) Create the **sidebar tree** first (empty pages are fine).  
> 3) Add **four “Start Here” pages**:
>    - “What this is”
>    - “If you only read one thing”
>    - “How to communicate with me”
>    - “How to support me when I’m overloaded”
> 4) Add 2–3 guided Paths as collections/playlists.
> 5) Put it behind Cloudflare Access when you’re ready to share selectively.
> 
> If you tell me which direction you prefer (GitBook vs Outline), I’ll give you the exact sidebar tree + the first 10 page titles + the “Path” layouts in a format you can paste straight in.

### User
> I don’t mind fit editing like I did yesterday we just need to organize it correctly and habe a side bar essential lock on the componente and only have to update folder paths and html files for the articles in those folder like a Zoho wiki I would use Zoho wiki if it didn’t require me to pay and handle additional users to view it .

### Assistant
> Understood. If you’re fine with Git-based editing, then the clean solution is:
> 
> - **Static docs site**
> - **Sidebar is “locked” as a component**
> - Each article is just an HTML file in a folder
> - The only “plumbing” you ever touch is:
>   1) the article HTML file itself, and  
>   2) *optionally* a sidebar manifest (ideally auto-generated so you don’t even touch that)
> 
> You can get a Zoho-wiki feel without Zoho-wiki pricing.
> 
> ## The architecture that won’t make you hate your life
> 
> ### 1) Folder structure = your wiki structure
> Example:
> 
> ```
> /site
>   /assets
>   /components
>     sidebar.html
>     header.html
>   /docs
>     /start-here
>       index.html
>       how-to-use.html
>     /operating-manual
>       communication.html
>       routines.html
>       overwhelm.html
>     /story-context
>       timeline.html
>       patterns.html
>   index.html
>   app.js
>   nav.json
> ```
> 
> ### 2) “Locked” layout: one shell, many content pages
> Every page uses the same layout and includes the same sidebar component. You don’t rewrite navigation per-page.
> 
> You can do this two ways:
> 
> **Option A (simplest):** each article is a full HTML page that loads the same sidebar via JS include.  
> **Option B (cleanest long-term):** a single `index.html` shell that loads article content into a `<main>` area (SPA-ish) based on URL hash or query param.
> 
> If you want *“only update folder paths and html files”*, Option A is easiest.
> 
> ---
> 
> ## Sidebar that you don’t manually maintain (recommended)
> You have two viable patterns:
> 
> ### Pattern 1: `nav.json` manifest (manual or generated)
> - Sidebar is rendered from `nav.json`
> - Each node points to `/docs/.../page.html`
> 
> **Best practice:** generate `nav.json` from the `/docs` folder with a tiny Python script. Then your “update” is literally: add/edit HTML file → run script → commit.
> 
> ### Pattern 2: Build sidebar from folder scan (not recommended on static hosting)
> Browser JS cannot reliably list server directories on static hosting without an API. So don’t chase that.
> 
> Manifest is the correct compromise.
> 
> ---
> 
> ## Minimal implementation plan (what you do next)
> 
> ### Step 1 — Create the locked layout
> Create:
> 
> - `/components/sidebar.html`
> - `/components/header.html`
> - `/assets/styles.css`
> - `app.js` (loads components + highlights active link)
> 
> Your sidebar never changes per page. Only the manifest does.
> 
> ### Step 2 — Standardize article template
> Every doc page follows the same skeleton and loads sidebar/header:
> 
> - `<div id="sidebar"></div>`
> - `<div id="header"></div>`
> - `<main> ... article content ... </main>`
> 
> ### Step 3 — Adopt a naming rule that keeps nav clean
> Use **slug file names**, and control display names in `nav.json`.
> 
> Example:
> - `how_i_operate.html` displayed as “How I Operate”
> - `when_i_struggle.html` displayed as “When I Struggle”
> 
> ### Step 4 — Automate `nav.json` generation (so you never “organize” twice)
> A script that:
> - scans `/docs/**.html`
> - infers section from folder
> - title from `<title>` tag (or first `<h1>`)
> - outputs `nav.json` grouped by folder
> 
> That gets you “Zoho wiki tree” with no manual maintenance.
> 
> ---
> 
> ## The blunt truth
> If you don’t generate the manifest, you will eventually let the sidebar drift out of sync with the docs. That’s the exact chaos tax you’re trying to avoid.
> 
> So: **HTML pages + locked sidebar + auto-generated nav.json** is the sweet spot.
> 
> ---
> 
> ## What I need from you (but I won’t stall you)
> If you answer these two things, I’ll give you the exact ready-to-paste file set (all code):
> 
> 1) Hosting target: **Cloudflare Pages** (I’m assuming yes)  
> 2) Routing preference:
>    - **Option A:** normal pages (`/docs/x/y.html`)  
>    - **Option B:** single shell with hash routes (`/#/docs/x/y`)
> 
> If you don’t answer, I’ll assume **Cloudflare Pages + Option A**, because it’s the least fragile and easiest to edit.

### User
> How is order handled or subfolders like sub topics. I’m thinking 7 major topics, 3 subtopics max each. FAQ style each article is the faq quick answer then deep dive materials, audios, videos, reports, infographics. Then maybe a section where I put the excerpts from the book pieces I’m going to publish like previews only they want the full book they buy it lol

### Assistant
> Order is not something the filesystem “magically” guarantees in a way you can trust across hosting/CDNs. You need to **define order explicitly**. There are three clean ways to do it; pick one and never revisit.
> 
> ## How order and subtopics should work
> 
> ### Option 1 (recommended): `nav.json` controls everything
> You keep your folder structure for sanity, but **order is dictated by a manifest**:
> 
> - 7 major topics (top-level nodes)
> - each has up to 3 subtopics (children)
> - each subtopic has pages (articles) in an ordered list
> 
> Example shape:
> 
> ```json
> {
>   "sections": [
>     {
>       "id": "start",
>       "title": "Start Here",
>       "order": 10,
>       "children": [
>         {
>           "id": "how-to-use",
>           "title": "How to Use This",
>           "order": 10,
>           "pages": [
>             { "title": "Read This First", "path": "/docs/start/read-this-first.html", "order": 10 },
>             { "title": "Quick Profile", "path": "/docs/start/quick-profile.html", "order": 20 }
>           ]
>         }
>       ]
>     }
>   ]
> }
> ```
> 
> **Pros:** precise, stable, sidebar tree is exactly what you want.  
> **Cons:** you either maintain this file (manageable) or generate it (better).
> 
> ### Option 2: Numeric prefixes in folder/file names (simple, zero-JS logic)
> You encode order into names:
> 
> ```
> /docs
>   /10_start-here
>     /10_overview
>       10_read-this-first.html
>       20_quick-profile.html
> ```
> 
> Then your sidebar builder sorts lexicographically and strips the prefixes for display.
> 
> **Pros:** no separate manifest required.  
> **Cons:** filenames look “ugly,” but it’s brutally reliable.
> 
> ### Option 3: Hybrid (best for ADHD-proofing)
> - Use **numeric prefixes** for major + subtopic folders (so the tree is always stable)
> - Use `nav.json` only to curate page-level order where needed
> 
> This keeps the number of things you can mess up very small.
> 
> ---
> 
> ## Subfolders and “subtopics”
> If you want **7 major topics, max 3 subtopics each**, enforce it structurally:
> 
> ```
> /docs
>   /10_start-here
>     /10_overview
>     /20_how-to-use
>     /30_navigation
>   /20_operating-manual
>     /10_communication
>     /20_work-style
>     /30_overwhelm-recovery
>   /30_relationships
>     /10_boundaries
>     /20_conflict-repair
>     /30_attachment-trust
>   ...
> ```
> 
> That gives you the Zoho-wiki feel: big categories → subtopic buckets → articles.
> 
> ---
> 
> ## Your “FAQ + deep dive” article pattern
> This is solid. Make it a **standard page template** so every article reads the same way:
> 
> ### Page layout (recommended)
> 1) **One-paragraph Quick Answer** (the FAQ answer)
> 2) **When this matters** (context / triggers)
> 3) **What helps** (do/don’t, scripts, checklists)
> 4) **Deep dive** (longform)
> 5) **Artifacts** (links/cards)
>    - audio
>    - video
>    - reports
>    - infographics
> 6) **Related pages** (auto or manual)
> 
> ### Files for one article (clean and scalable)
> Keep the article as the hub, and store artifacts in a sibling folder:
> 
> ```
> /docs/20_operating-manual/10_communication/
>   10_how-i-communicate.html
>   10_how-i-communicate.assets/
>     overview.png
>     conflict-script.pdf
>     audio-clip-1.mp3
>     video-embed-links.md
> ```
> 
> That keeps your site fast and your brain calm: article + a single assets folder.
> 
> ---
> 
> ## “Book previews” section (yes, do it)
> Give it its own major topic so it doesn’t pollute the “manual” content:
> 
> ```
> /docs/70_book-previews
>   /10_713-series
>   /20_silence-isnt-distance
>   /30_the-mirror
> ```
> 
> Each preview page should be:
> - short excerpt
> - “why this chapter exists”
> - link to buy / waitlist / mailing list
> - optionally an audio reading (powerful)
> 
> ---
> 
> ## The single decision that makes or breaks this
> Pick one ordering strategy now:
> 
> - If you want **maximum control with clean names**: `nav.json` ordering.
> - If you want **minimum moving parts**: numeric prefixes.
> - If you want **stable structure + flexible curation**: hybrid.
> 
> If you don’t choose, I would default you to **Hybrid**, because it prevents sidebar drift *and* keeps you from babysitting a manifest every time you add a page.

### User
> Numeric works go decimal for insertions restart the counting each level. Like how you are showing. Each article is a folder with index and assets to prevent folder bloating we can just make each article a folder and inside it index.html, infographic.png, audio.m4a, video.mp4, doc.pdf, and a article index or manifest to handle any necessary logic or linking you think? Or better way?

### Assistant
> Your plan is fundamentally sound. Numeric (decimal) ordering + “one article = one folder” is the cleanest way to keep the tree stable and prevent `/assets` from turning into a landfill.
> 
> That said, there are two design choices you should make up front so you don’t rebuild this later:
> 
> 1) **How navigation is built** (manual vs generated)  
> 2) **Where media lives** (in-repo vs external storage)
> 
> ## Recommended structure
> 
> ### Levels and ordering
> - Restart numbering at each level (major topic, subtopic, article).
> - Use decimal gaps (10, 20, 30…) so insertions are painless (e.g., 25).
> 
> ### Directory pattern
> Use this pattern:
> 
> ```
> /docs
>   /10_start-here
>     /10_overview
>       /10_read-this-first
>         index.html
>         meta.json
>         infographic.png
>         audio.m4a
>         doc.pdf
>   /20_operating-manual
>     /10_communication
>       /10_how-i-communicate
>         index.html
>         meta.json
>         audio.m4a
>         video.mp4
>         infographic.png
>         doc.pdf
> ```
> 
> This is exactly “Zoho wiki tree” with deterministic ordering.
> 
> ## Do you need an article manifest inside each folder?
> 
> ### Yes — but keep it minimal and standardized (`meta.json`)
> A tiny per-article manifest is worth it because it lets you:
> - auto-generate the sidebar (and breadcrumbs)
> - show “Assets” consistently without hardcoding links
> - support “Related articles” later
> - keep titles/descriptions out of HTML if you want
> 
> Example `meta.json`:
> 
> ```json
> {
>   "title": "How I Communicate",
>   "summary": "Quick answer: If you want me to respond fast, write the ask in one sentence and add context as bullets.",
>   "keywords": ["communication", "tone", "texting", "conflict"],
>   "assets": [
>     { "type": "infographic", "label": "Cheat Sheet", "file": "infographic.png" },
>     { "type": "audio", "label": "2-min audio", "file": "audio.m4a" },
>     { "type": "pdf", "label": "Printable script", "file": "doc.pdf" },
>     { "type": "video", "label": "Short video", "file": "video.mp4" }
>   ],
>   "related": [
>     "/docs/20_operating-manual/30_overwhelm-recovery/10_when-im-overloaded/"
>   ]
> }
> ```
> 
> Then your `index.html` can render the “Artifacts” section dynamically from `meta.json` (or you can leave it static and use `meta.json` only for nav generation).
> 
> ## Better way than putting video/audio files directly in the repo
> This is where I’m going to be blunt:
> 
> - Putting **.mp4 and .m4a** files in the same repo as your site will bloat your Git history fast, slow down deploys, and become a maintenance problem.
> - For Cloudflare Pages, large media can also make builds/deploys annoying.
> 
> ### Better pattern
> Keep “article folder” clean, but store heavy media externally:
> 
> - **Cloudflare R2** for files (pdf, audio, images, zips)
> - **Cloudflare Stream** for video (best UX)
> 
> Then in `meta.json`, assets can be either local files *or* URLs:
> 
> ```json
> { "type": "video", "label": "Short video", "url": "https://…cloudflarestream…" }
> ```
> 
> If you absolutely want “everything in the folder,” do it for:
> - `infographic.png`, small `doc.pdf`
> But I strongly recommend external for:
> - `video.mp4`, longer `audio.m4a`
> 
> ## Navigation logic without pain
> With your numeric folders, the simplest robust approach is:
> 
> - One script generates a global `nav.json` by scanning `/docs/**/meta.json`.
> - The sidebar component renders from `nav.json`.
> 
> That means your workflow is:
> 1) create article folder  
> 2) drop `index.html` + `meta.json` + assets  
> 3) run `build_nav.py`  
> 4) commit/push
> 
> No hand-editing sidebar, ever.
> 
> ## Small tweak that will save you headaches: trailing-slash URLs
> If each article is a folder with `index.html`, you can link like:
> 
> `/docs/20_operating-manual/10_communication/10_how-i-communicate/`
> 
> That is cleaner than linking to `index.html`, and it plays nicely with static hosting.
> 
> ## Bottom line
> Your “article = folder” approach is the right move.
> 
> - **Do include `meta.json`** per article (minimal, consistent).
> - **Do use numeric ordering** at each level (10/20/30 with decimals for inserts).
> - **Do generate a global `nav.json`** automatically.
> - **Don’t store big video/audio in the repo** unless you enjoy self-inflicted suffering; use R2/Stream and reference URLs.
> 
> If you want, I’ll give you the exact starter set:
> - `components/sidebar.html`
> - `app.js` that loads and renders `nav.json`
> - `build_nav.py` that scans your folder tree and builds the nav automatically
> - a starter `index.html` template for articles that reads `meta.json` and renders the “Artifacts” block consistently

### User
> Yes Zoho wiki tree and asset live in repo since they will be short and small anyways keeps everything in one place.  Ok for the video we can do YouTube link. Google link don’t work so YouTube it is

### Assistant
> Good. Then the “Zoho wiki tree + everything in repo (except video via YouTube)” pattern is clean and durable.
> 
> ## Canonical structure
> 
> Restart numbering at each level; use 10/20/30 with optional inserts (25).
> 
> ```
> /docs
>   /10_start-here
>     /10_overview
>       /10_read-this-first
>         index.html
>         meta.json
>         infographic.png
>         audio.m4a
>         doc.pdf
> 
>   /20_operating-manual
>     /10_communication
>       /10_how-i-communicate
>         index.html
>         meta.json
>         infographic.png
>         audio.m4a
>         doc.pdf
> ```
> 
> URLs use trailing slashes:
> 
> `/docs/20_operating-manual/10_communication/10_how-i-communicate/`
> 
> ## What goes in `meta.json` (minimal, practical)
> 
> This is the only “logic” file you need per article. Keep it tiny and consistent.
> 
> ```json
> {
>   "title": "How I Communicate",
>   "quick_answer": "If you want a fast response, put the ask in one sentence, then add context as bullets.",
>   "keywords": ["communication", "tone", "requests"],
>   "assets": [
>     { "type": "infographic", "label": "Cheat Sheet", "file": "infographic.png" },
>     { "type": "audio", "label": "2-min audio", "file": "audio.m4a" },
>     { "type": "pdf", "label": "Printable script", "file": "doc.pdf" }
>   ],
>   "video": {
>     "label": "Short video",
>     "youtube_id": "dQw4w9WgXcQ"
>   },
>   "related": [
>     "/docs/20_operating-manual/30_overwhelm-recovery/10_when-im-overloaded/"
>   ]
> }
> ```
> 
> Notes:
> - Use `youtube_id` (not a full link). It keeps embeds consistent.
> - If an article has no video, omit the `video` field.
> 
> ## Standard article `index.html` template
> 
> This gives you: **FAQ quick answer → deep dive → assets → embedded YouTube**.
> 
> ```html
> <!doctype html>
> <html lang="en">
> <head>
>   <meta charset="utf-8" />
>   <meta name="viewport" content="width=device-width,initial-scale=1" />
>   <title>Loading…</title>
>   <link rel="stylesheet" href="/assets/styles.css" />
>   <script defer src="/assets/app.js"></script>
> </head>
> <body>
>   <div class="layout">
>     <aside id="sidebar" class="sidebar"></aside>
> 
>     <main class="content">
>       <div class="breadcrumbs" id="breadcrumbs"></div>
> 
>       <h1 id="title">Loading…</h1>
> 
>       <section class="card">
>         <h2>Quick Answer</h2>
>         <p id="quickAnswer"></p>
>       </section>
> 
>       <section class="card">
>         <h2>Deep Dive</h2>
>         <div class="prose">
>           <!-- Write your deep dive here (static, authored content) -->
>           <p>...</p>
>         </div>
>       </section>
> 
>       <section class="card" id="assetsCard" style="display:none;">
>         <h2>Artifacts</h2>
>         <ul id="assetsList" class="asset-list"></ul>
>       </section>
> 
>       <section class="card" id="videoCard" style="display:none;">
>         <h2 id="videoLabel">Video</h2>
>         <div class="video-embed">
>           <iframe id="ytFrame"
>             title="YouTube video"
>             loading="lazy"
>             referrerpolicy="strict-origin-when-cross-origin"
>             allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
>             allowfullscreen></iframe>
>         </div>
>       </section>
> 
>       <section class="card" id="relatedCard" style="display:none;">
>         <h2>Related</h2>
>         <ul id="relatedList"></ul>
>       </section>
>     </main>
>   </div>
> </body>
> </html>
> ```
> 
> ## “Locked sidebar” + ordered tree
> 
> You have two files:
> 
> 1) `nav.json` (global, generated or hand-maintained)
> 2) `sidebar.html` (component that renders nav)
> 
> ### `nav.json` format (ordered by numeric names automatically)
> ```json
> {
>   "title": "Cody Docs",
>   "sections": [
>     {
>       "title": "Start Here",
>       "path": "/docs/10_start-here/",
>       "children": [
>         {
>           "title": "Overview",
>           "path": "/docs/10_start-here/10_overview/",
>           "children": [
>             { "title": "Read This First", "path": "/docs/10_start-here/10_overview/10_read-this-first/" }
>           ]
>         }
>       ]
>     }
>   ]
> }
> ```
> 
> You can maintain this manually at first. But the correct long-term move is to generate it.
> 
> ## The “best way” to avoid drift: generate `nav.json`
> If you’re willing to run one command before committing, you’ll never touch the sidebar again.
> 
> - Script scans `/docs/**/meta.json`
> - Uses numeric folder names for ordering
> - Uses `meta.json.title` for display names
> - Writes `/assets/nav.json`
> 
> If you want, I’ll paste a single-file `build_nav.py` that does this and works on Windows/Mac/Linux with plain Python.
> 
> ## YouTube policy (so embeds don’t break)
> - Put the **YouTube ID** in `meta.json`.
> - Embed via:
>   `https://www.youtube-nocookie.com/embed/<id>`
> - Avoid Google Drive links for video; you already learned why.
> 
> ## Decision checklist (locked in)
> - Numeric folder ordering at each level: yes
> - Article = folder + `index.html` + `meta.json` + small assets: yes
> - Video: YouTube embed only: yes
> - Sidebar: rendered from `nav.json`: yes
> - `nav.json`: start manual, then automate: recommended
> 
> If you tell me your 7 major topics + the 3 subtopics under each (just titles), I’ll output the exact folder tree with numeric prefixes and a starter `nav.json` that matches it.
