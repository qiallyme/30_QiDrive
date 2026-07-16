# QiAlly.com Blog

Static blog generator for QiAlly.com public-facing content.

## Quick Start

1. Install dependencies:
```bash
npm install
```

2. Build the site:
```bash
npm run build
```

3. The output will be in `/dist` - ready to deploy to Cloudflare Pages.

## Structure

- `/src` - Source templates and static assets
- `/content/posts` - Markdown blog posts
- `/dist` - Build output (deployed to Cloudflare Pages)

## Adding a New Post

1. Create a new Markdown file in `/content/posts/` with the format:
   - `YYYY-MM-DD-slug.md`

2. Include front matter:
```markdown
---
slug: "your-slug"
title: "Your Title"
subtitle: "Optional subtitle"
date: YYYY-MM-DD
tags:
  - tag1
  - tag2
series: "Optional Series Name"
status: "published"
description: "SEO description"
---
```

3. Run `npm run build` to generate the HTML.

## Deployment

Configure Cloudflare Pages:
- Build command: `npm run build`
- Output directory: `dist`
- Node version: 18 or higher

