---
title: "qiAlly.com Blog & Exposure System — Technical Spec"
date: 2025-12-04
owner: "Cody Rice-Velasquez"
project: "qiAlly.com Public Blog"
status: "v1 - skeleton spec"
layout: page
slug: qially-com-blog-exposure-system-technical-spec
summary: ""
created_at: "2026-07-16T06:19:39-04:00"
updated_at: "2026-07-16T06:19:39-04:00"
author: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ae9eb032ec1c4b3f988add45d6206d3e
canonical_ref: ""
source_type: manual
template_key: master-template
---

## 1. Goals & Constraints

### 1.1 Goals

- Host a **public-facing blog** at `https://qially.com/blog` for:
  - Personal essays
  - “Chats With Consciousness” (AI conversation reflections)
  - INFJ/ADHD/spirituality/business/strategy content
- Keep **all sensitive/internal** content on `qiAlly.me` (strict separation).
- Keep stack **simple, static, and Cloudflare-friendly**.
- Use **Markdown + front matter** as the primary authoring format.
- Allow future expansion (RSS feed, SEO, tagging, pagination) without repainting the whole thing.

### 1.2 Constraints

- Deployment target: **Cloudflare Pages** (via GitHub).
- No heavy frameworks required (Next.js, Astro, etc.) unless absolutely necessary later.
- Prefer **vanilla HTML/CSS/JS** plus a small build script over a big SSG.
- Authoring should be compatible with **Obsidian-style Markdown**.

---

## 2. Stack Overview

### 2.1 High-Level

- **Type:** Static site
- **Deploy:** Cloudflare Pages, build output in `/dist`
- **Authoring:** Markdown with YAML front matter
- **Build Tool:** Lightweight Node.js build script (ESM) using:
  - `gray-matter` (parse front matter)
  - `marked` or `markdown-it` (Markdown → HTML)
- **Styling:** Plain CSS (or a single global stylesheet) with responsive layout
  - No Tailwind or big CSS frameworks in v1 (can add later)
- **JS:** Minimal; only for niceties (e.g. mobile nav, scroll-to-top, etc.)

---

## 3. Directory Structure

Create a repo with this structure:

```plaintext
/
├─ package.json
├─ build.mjs                 # Node build script (Markdown → HTML → dist)
├─ cloudflare-pages.yml      # (optional) CF build config if needed
├─ /src
│  ├─ index.html             # qiAlly.com homepage (skeleton)
│  ├─ blog
│  │  ├─ index.html          # /blog landing page (built from template)
│  │  ├─ templates
│  │  │  ├─ layout.html      # base HTML shell (head, header, footer)
│  │  │  ├─ blog-index.html  # template for blog list
│  │  │  └─ blog-post.html   # template for individual post content
│  │  └─ static
│  │     └─ blog.css         # blog styles
│  ├─ assets
│  │  ├─ logo.svg
│  │  ├─ favicon.ico
│  │  └─ og-image-default.png
│  └─ static                 # other static assets (shared)
│     └─ robots.txt
├─ /content
│  └─ posts
│     ├─ 2025-12-04-high-voltage-moment.md
│     ├─ 2025-12-xx-post-02.md
│     └─ ...
└─ /dist                     # build output (what Cloudflare deploys)
   ├─ index.html
   ├─ blog
   │  ├─ index.html
   │  ├─ high-voltage-moment/index.html
   │  └─ ...
   ├─ assets
   └─ robots.txt
````

---

## 4. Content Model

### 4.1 Blog Post Front Matter

Each post in `/content/posts` should use:

```markdown
---
slug: "high-voltage-moment"
title: "High Voltage: A Moment of Truth"
subtitle: "On feeling fragile with a powerful mind"
date: 2025-12-04
tags:
  - personal
  - mental-health
  - growth
  - chats-with-consciousness
series: "Chats With Consciousness"
status: "published"  # or "draft"
canonical_url: ""    # optional override
description: "A reflection on why a powerful brain can still feel fragile and overloaded."
---

Post body in Markdown here...
```

**Build rules:**

* `slug` becomes the URL segment:

  * `/blog/high-voltage-moment/`
* `status: draft` → do **not** include in blog index or build in v1.
* `date` used for sorting (newest first) and for `<time>` tags + metadata.
* `tags`, `series` may be used later for filtered views; for now: show on post page.

---

## 5. Routing & URL Design

### 5.1 Public Routes

* `/`

  * Main qiAlly.com home (simple intro + CTA → `/blog`)
* `/blog`

  * Blog index, listing posts (title, date, subtitle/excerpt, tags, read-more link)
* `/blog/:slug/`

  * Individual blog post page

### 5.2 Future (Optional) Routes

* `/blog/tag/:tag/` — filtered by tag
* `/blog/series/chats-with-consciousness/` — all posts in the series
* `/feed.xml` — RSS feed

---

## 6. Templates

### 6.1 Base Layout (`/src/blog/templates/layout.html`)

This is the base shell. Use simple placeholders for build script to replace:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>{{PAGE_TITLE}}</title>
  <meta name="description" content="{{PAGE_DESCRIPTION}}" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />

  <link rel="icon" href="/assets/favicon.ico" />
  <link rel="stylesheet" href="/blog/static/blog.css" />

  <!-- Open Graph -->
  <meta property="og:title" content="{{PAGE_TITLE}}">
  <meta property="og:description" content="{{PAGE_DESCRIPTION}}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{{PAGE_URL}}">
  <meta property="og:image" content="{{PAGE_OG_IMAGE}}">
</head>
<body>
  <header class="site-header">
    <a href="/" class="logo">
      <img src="/assets/logo.svg" alt="QiAlly logo">
    </a>
    <nav class="main-nav">
      <a href="/blog">Blog</a>
      <!-- Add other public nav links later -->
    </nav>
  </header>

  <main class="site-main">
    {{PAGE_CONTENT}}
  </main>

  <footer class="site-footer">
    <p>&copy; {{CURRENT_YEAR}} QiAlly. All rights reserved.</p>
  </footer>
</body>
</html>
```

### 6.2 Blog Index Template (`/src/blog/templates/blog-index.html`)

`{{POST_LIST}}` will be filled by build script:

```html
<section class="blog-hero">
  <h1>QiAlly Blog</h1>
  <p>Essays, reflections, and conversations at the edge of growth and consciousness.</p>
</section>

<section class="blog-list">
  {{POST_LIST}}
</section>
```

Each post item structure (built by script):

```html
<article class="blog-card">
  <a href="/blog/{{slug}}/">
    <h2>{{title}}</h2>
  </a>
  <p class="meta">
    <time datetime="{{date_iso}}">{{date_human}}</time>
    <span class="tags">{{tags_joined}}</span>
  </p>
  <p class="excerpt">{{excerpt}}</p>
  <a class="read-more" href="/blog/{{slug}}/">Read more →</a>
</article>
```

### 6.3 Blog Post Template (`/src/blog/templates/blog-post.html`)

`{{POST_CONTENT_HTML}}` is full HTML converted from Markdown:

```html
<article class="blog-post">
  <header class="post-header">
    <p class="post-series">{{series}}</p>
    <h1>{{title}}</h1>
    <p class="post-subtitle">{{subtitle}}</p>
    <p class="post-meta">
      <time datetime="{{date_iso}}">{{date_human}}</time>
      <span class="tags">{{tags_joined}}</span>
    </p>
  </header>

  <section class="post-body">
    {{POST_CONTENT_HTML}}
  </section>

  <footer class="post-footer">
    <p class="post-cta">
      This entry is part of the <strong>{{series}}</strong> series.
    </p>
    <!-- Future: links to next/previous, email signup, etc. -->
  </footer>
</article>
```

---

## 7. Build Script Requirements (`build.mjs`)

Implement a Node script with these responsibilities:

1. **Clean `/dist`** on each run.
2. **Copy static assets** from `/src` → `/dist`:

   * `/src/index.html` → `/dist/index.html`
   * `/src/assets` → `/dist/assets`
   * `/src/static` → `/dist`
3. **Read all Markdown posts** from `/content/posts`.
4. For each post:

   * Parse YAML front matter (`gray-matter`).
   * Convert Markdown body → HTML (`marked` or `markdown-it`).
   * Generate:

     * `slug` from front matter (fallback: file name without date).
     * `date_iso` and `date_human` (e.g. `2025-12-04` → `December 4, 2025`).
     * `excerpt` (first 160–200 characters, stripped of HTML).
   * Inject data into `blog-post.html` template.
   * Wrap with `layout.html`.
   * Write output to `/dist/blog/<slug>/index.html`.
5. **Build blog index page**:

   * Sort posts by `date` (descending).
   * For each `status: published` post, create a card (see above).
   * Inject cards into `blog-index.html`.
   * Wrap with `layout.html`.
   * Write `/dist/blog/index.html`.

**CLI usage:**

```bash
node build.mjs
```

Cloudflare Pages build command: `node build.mjs`, output dir: `/dist`.

---

## 8. Security & Separation Notes

* This repo is for **qiAlly.com only**.
  **Do NOT** include:

  * Any internal `.me` links
  * Raw chat logs
  * Client names, immigration case details, etc.
* Only use **sanitized, curated content**.
* If reusing text originally written for `.me`, it must be:

  * De-identified
  * Emotionally grounded
  * Safe to show to strangers

---

## 9. Integration Points for Exposure Strategy (Non-Code Hooks)

Cursor doesn’t need to implement these now, but code should **leave room** for them:

1. **Email capture section** (future)

   * Space in post footer for a Substack/Zoho/Attio embed or simple form.

2. **Social sharing**

   * Ensure each post page:

     * Has correct `og:title`, `og:description`, `og:url`.
     * Uses a default `og:image` (replaceable later per-post).

3. **RSS feed**

   * Optional second pass: `feed.xml` generation in `build.mjs` using the same post metadata.

4. **Canonical URLs**

   * Use `<link rel="canonical">` in `<head>`:

     * If `canonical_url` in front matter: use that.
     * Else: use the blog URL built from domain + slug.

---

## 10. First Seed Post to Implement

Create `content/posts/2025-12-04-high-voltage-moment.md` with front matter matching this spec.
Body can be a placeholder; content will be filled later.

```markdown
---
slug: "high-voltage-moment"
title: "High Voltage: A Moment of Truth"
subtitle: "On feeling fragile with a powerful mind"
date: 2025-12-04
tags:
  - personal
  - mental-health
  - growth
  - chats-with-consciousness
series: "Chats With Consciousness"
status: "published"
canonical_url: ""
description: "A reflection on why a powerful brain can still feel fragile and overloaded – and why that’s not weakness but overload."
---

[Body content will be added after skeleton is verified.]
```

---

```

---

Next steps after you hand this to Cursor:

1. Have Cursor:
   - Initialize `package.json`
   - Add `gray-matter` + `marked` (or `markdown-it`)
   - Implement `build.mjs`
   - Scaffold the `/src` + `/content` structure from the spec
2. Once that’s built and deploying cleanly to Cloudflare Pages, come back to me and we’ll:
   - Write the real **“High Voltage”** post body
   - Draft 2–3 more posts
   - Set up your exposure workflows (Substack, Medium, cross-posting templates)
   - If you want, I can ALSO write a “Cursor prompt” version of this spec so it can auto-generate everything with minimal back-and-forth.
```
---
