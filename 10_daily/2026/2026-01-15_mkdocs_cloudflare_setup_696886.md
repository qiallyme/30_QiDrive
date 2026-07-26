---
title: "MkDocs Cloudflare Setup"
date: "2026-01-15"
created_at: "2026-01-15T06:16:52.154514+00:00"
conversation_id: "6968862b-798c-8325-811e-d5b03aab32c9"
tags:
  - ai_chat
  - export
---

# MkDocs Cloudflare Setup

> **Date:** 2026-01-15 | **Conversation ID:** `6968862b-798c-8325-811e-d5b03aab32c9`

---

### **User**
we were working on a mkdocs static build for the case site but whate ver gemini gavbe me just keeps failing, give me the cloudflare setting and other files needed for a successfule mkdocs build withi in broswer asset viewing like pdf. images, video, ect.

---

### **Assistant**
Below is a Cloudflare Pages + MkDocs setup that reliably builds and serves **PDF/image/video assets inline in the browser**, plus gives you clean “browse-the-folder” behavior (either via your own generated `index.html` files or a simple MkDocs “Assets” page).

You already have a solid “folder index” HTML pattern in your repo (example here: fileciteturn0file14). The configs below make Cloudflare serve those assets cleanly and stop CSP/MIME issues from breaking in-browser viewing.

---

## 1) Cloudflare Pages settings (the part Gemini often screws up)

### Build & Deploy
- **Framework preset:** `None`
- **Build command:**
```bash
pip install -r requirements.txt && mkdocs build --strict
```
- **Build output directory:**  
`site`

### Environment variables (set in Pages → Settings → Environment variables)
- `PYTHON_VERSION` = `3.11` (or `3.12` if your dependencies support it)
- `PIP_DISABLE_PIP_VERSION_CHECK` = `1`
- `PIP_NO_CACHE_DIR` = `1`
- Optional but helpful:
  - `MKDOCS_ENABLE_GIT_REVISION_DATE` = `1` (if you use git date plugins)
  - `CI` = `1`

**Most common failure:** people set output dir to `docs/site` or `public` or forget `site`. MkDocs outputs to `site/` by default.

---

## 2) Required repo files

### `requirements.txt` (minimum viable + asset-friendly plugins)
```txt
mkdocs==1.6.0
mkdocs-material==9.5.33

# Nice-to-haves for evidence-heavy sites
mkdocs-awesome-pages-plugin==2.10.1
mkdocs-glightbox==0.4.0
mkdocs-video==1.5.0
pymdown-extensions==10.9
```

If you want *zero plugins*, you can remove everything except `mkdocs` and `mkdocs-material`. The rest just makes evidence browsing nicer.

---

## 3) `mkdocs.yml` (battle-tested for assets, PDFs, and deep folders)

```yaml
site_name: CASE-VIEW FCFCU v. CODY
site_url: https://<your-cloudflare-pages-domain>/
use_directory_urls: true

theme:
  name: material
  features:
    - navigation.instant
    - navigation.tracking
    - navigation.tabs
    - navigation.top
    - content.code.copy
    - toc.follow
  palette:
    scheme: slate

markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true

plugins:
  - search
  - awesome-pages
  - glightbox
  - video

# Put ALL evidence inside docs/ so MkDocs copies it to /site unchanged
docs_dir: docs

# Optional: if you keep a lot of non-md content in docs/, do NOT exclude it.
# MkDocs will copy it through as "static" as long as it's under docs/.
```

### Key rule that prevents 80% of “why is my PDF missing” problems
**All PDFs/images/video must live under `docs/`** (or a folder referenced by `docs_dir`). MkDocs only publishes what’s inside `docs/`.

---

## 4) Asset layout that works with in-browser viewing

Example structure:

```txt
repo/
  mkdocs.yml
  requirements.txt
  docs/
    index.md
    assets/
      pdf/
        01_motion_vacate.pdf
      img/
        photo1.png
      video/
        clip1.mp4
    evidence/
      02_filings/
        20_.../
          02_exhibits/
            Exhibit_H_Declaration.pdf
            index.html
```

You can keep your hand-generated folder `index.html` pages (like the one you already have fileciteturn0file14). MkDocs will copy them through and Cloudflare will serve them normally.

---

## 5) Make PDFs open *in-browser* (not download-only)

In Markdown, link like this:

```md
### Motion to Vacate
- [Open PDF](/assets/pdf/01_motion_vacate.pdf)
- Inline preview:

<iframe
  src="/assets/pdf/01_motion_vacate.pdf"
  width="100%"
  height="900"
  style="border:1px solid rgba(255,255,255,0.15); border-radius: 12px;"
></iframe>
```

This works **if** your site headers don’t block iframes or PDF rendering.

---

## 6) Add Cloudflare Pages headers to avoid CSP/CORP “silent failures”

Create: `docs/_headers`

```txt
/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: interest-cohort=()
  Cross-Origin-Opener-Policy: same-origin
  Cross-Origin-Resource-Policy: same-origin

# Allow embedding your own PDFs/videos in iframes on your own site
  Content-Security-Policy: default-src 'self'; img-src 'self' data: blob:; media-src 'self' blob:; object-src 'self'; frame-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline';

/assets/pdf/*
  Content-Type: application/pdf

/assets/video/*
  Accept-Ranges: bytes
  Cache-Control: public, max-age=31536000, immutable

/assets/img/*
  Cache-Control: public, max-age=31536000, immutable
```

Notes:
- The CSP above is intentionally “tight but functional” for evidence sites.
- `Accept-Ranges: bytes` helps video seeking and large-file streaming behavior.
- You generally do **not** need to force `Content-Type` for PDFs, but it can help if you ever see weird MIME behavior.

---

## 7) Add redirects only if you need them

MkDocs is not an SPA. You usually don’t need redirects.

If you *do* want a couple stable entry points, create: `docs/_redirects`

```txt
/home    /index.html    302
```

That’s it. Don’t add the SPA wildcard redirect (`/* /index.html 200`) unless you enjoy breaking deep links to actual files.

---

## 8) The top 5 build failures and the fast fix

1) **Cloudflare output dir wrong** → must be `site`  
2) **Evidence files not under `docs/`** → MkDocs never publishes them  
3) **Using `mkdocs serve` in build** → wrong; must be `mkdocs build`  
4) **Python version mismatch** → set `PYTHON_VERSION=3.11`  
5) **CSP blocks iframe/object** → add `docs/_headers` as above

---

## 9) If you want “browse folders” like a file explorer (without writing HTML indexes)

You have two workable approaches:

### A) Keep your existing `index.html` per folder (works immediately)
You’re already doing this. MkDocs will publish it unchanged, and Cloudflare serves it fine. (Again, your example index is here: fileciteturn0file14.)

### B) Make a single `Assets.md` page with curated links
Create `docs/assets.md` and manually link “evidence packs” and key PDFs. This is usually better than dumping raw directories.

---

If you paste your current **Cloudflare build log error** (the exact failure lines) I’ll tell you which of the above items is the culprit in one pass—no guessing.

---

### **User**
and if we do vite instead, fyi the content folder to copy over is at root content/ and everything for the virte press buils is in a root folder called vitepress/

---

### **Assistant**
Yes—**VitePress on Cloudflare Pages** is often the cleaner move, especially if you want “static site + asset vault” behavior with fewer Python headaches.

Given your repo layout:

- `content/` at repo root (the stuff you want published as browseable assets: PDFs/images/video/etc.)
- `vitepress/` at repo root (the VitePress project)

The key is: **VitePress only publishes what’s inside its `docs/` folder**, plus anything inside **`docs/public/`** as raw static files.

So we’ll **copy `/<repo>/content` → `/<repo>/vitepress/docs/public/content` during build**.

That gives you:
- assets served at `/content/...`
- direct in-browser PDF viewing
- images/video served as static files
- no funky MkDocs constraints

---

## 1) Cloudflare Pages settings (VitePress)

### Build & Deploy
- **Framework preset:** `None` (or VitePress if it shows up—either works; None is predictable)
- **Build command:**
```bash
cd vitepress && npm ci && npm run build
```
- **Build output directory:**
```txt
vitepress/docs/.vitepress/dist
```

### Environment variables (Pages → Settings → Environment variables)
- `NODE_VERSION` = `20` (or `18`, but 20 is the safe default now)

---

## 2) VitePress project structure you should have

Inside `vitepress/`:

```txt
vitepress/
  package.json
  docs/
    index.md
    .vitepress/
      config.mts
```

And we will create:

```txt
vitepress/docs/public/
  content/               <-- build will populate this from /content
  _headers               <-- Cloudflare response headers for PDFs/video
  _redirects             <-- optional
```

---

## 3) The critical build step: copy `/content` into VitePress `public`

You have two good options:

### Option A (recommended): Node script, cross-platform, no bash assumptions
Create: `vitepress/scripts/sync-content.mjs`

```js
import fs from "node:fs";
import path from "node:path";

function copyDir(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const s = path.join(src, entry.name);
    const d = path.join(dest, entry.name);
    if (entry.isDirectory()) copyDir(s, d);
    else fs.copyFileSync(s, d);
  }
}

const repoRoot = path.resolve(process.cwd(), ".."); // since we run from /vitepress
const src = path.join(repoRoot, "content");
const dest = path.join(process.cwd(), "docs", "public", "content");

if (!fs.existsSync(src)) {
  console.log(`[sync-content] No /content found at ${src}. Skipping.`);
  process.exit(0);
}

fs.rmSync(dest, { recursive: true, force: true });
copyDir(src, dest);
console.log(`[sync-content] Copied ${src} -> ${dest}`);
```

Then in `vitepress/package.json`:

```json
{
  "name": "vitepress-site",
  "private": true,
  "type": "module",
  "scripts": {
    "prebuild": "node scripts/sync-content.mjs",
    "build": "vitepress build docs",
    "dev": "vitepress dev docs --host 0.0.0.0 --port 5173"
  },
  "devDependencies": {
    "vitepress": "^1.3.0"
  }
}
```

**Result:** every build automatically republishes the latest `content/` as `/content/...`

### Option B (bash): faster, but depends on unix tools
In Cloudflare’s build cmd:

```bash
rsync -a --delete content/ vitepress/docs/public/content/ && cd vitepress && npm ci && npm run build
```

I prefer Option A because it’s deterministic and portable.

---

## 4) VitePress config (set base path correctly)

Create/confirm: `vitepress/docs/.vitepress/config.mts`

```ts
import { defineConfig } from "vitepress";

export default defineConfig({
  title: "CASE-VIEW FCFCU v. CODY",
  description: "Case documentation and evidence vault",
  base: "/", // IMPORTANT for Cloudflare Pages at root domain/subdomain

  themeConfig: {
    nav: [
      { text: "Home", link: "/" },
      { text: "Assets", link: "/assets" }
    ],
    sidebar: [
      { text: "Start", items: [{ text: "Home", link: "/" }] },
      { text: "Evidence", items: [{ text: "Assets", link: "/assets" }] }
    ]
  }
});
```

If you deploy under a subpath (like `example.com/case/`), then `base` must be `"/case/"`. For a normal Pages domain or custom subdomain, keep `"/"`.

---

## 5) Assets page (quick “file explorer-lite” jump points)

Create `vitepress/docs/assets.md`:

```md
# Assets (static)

Everything in `/content` is published at:

- `/content/...`

## Key PDFs
- [Motion to Vacate](/content/pdf/01_motion_vacate.pdf)

## Inline PDF preview example

<iframe
  src="/content/pdf/01_motion_vacate.pdf"
  width="100%"
  height="900"
  style="border:1px solid rgba(0,0,0,0.15); border-radius: 12px;"
></iframe>
```

That gives you predictable in-browser viewing and a simple landing page.

---

## 6) Cloudflare headers for in-browser PDFs + video streaming

Create: `vitepress/docs/public/_headers`

```txt
/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Cross-Origin-Opener-Policy: same-origin
  Cross-Origin-Resource-Policy: same-origin

  Content-Security-Policy: default-src 'self'; img-src 'self' data: blob:; media-src 'self' blob:; frame-src 'self'; object-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline';

/content/video/*
  Accept-Ranges: bytes
  Cache-Control: public, max-age=31536000, immutable

/content/img/*
  Cache-Control: public, max-age=31536000, immutable

/content/pdf/*
  Cache-Control: public, max-age=31536000, immutable
```

This avoids the classic “PDF won’t embed” and helps large media behave well.

---

## 7) Cloudflare redirects (optional)

Only add this if you want a convenience alias:

Create: `vitepress/docs/public/_redirects`

```txt
/assets  /assets.html  302
```

Generally, you do not need redirects for VitePress.

---

## 8) What this gives you (no fluff, just outcomes)

- Drop a PDF at `content/pdf/foo.pdf`
- It auto-deploys to `https://yoursite.pages.dev/content/pdf/foo.pdf`
- It opens in browser, and you can embed it via iframe
- Same for images (`/content/img/...`) and videos (`/content/video/...`)
- Your “case site” content lives in VitePress pages, while the evidence vault stays as raw files

---

If you tell me your **exact** current `content/` structure (like `content/pdf`, `content/evidence`, etc.), I’ll give you:
- a clean `/assets.md` that mirrors it,
- and a nav/sidebar that makes it feel like a real evidence browser instead of a junk drawer.

---

### **User**
┣ 📂_ingest
┃ ┣ 📜01_MASTER_INDEX_Starter_2026-01-10.md
┃ ┣ 📜01092026_005.pdf.pdf
┃ ┣ 📜CASE_FCFCU_Violation_Index_Starter_2026-01-10.csv
┃ ┣ 📜f12dee70-15da-4041-97fd-1fba9554adaf.pdf
┃ ┗ 📜Summary - MyCase.html
┣ 📂00_ADMIN
┃ ┣ 📂00_trackers
┃ ┃ ┣ 📜2024-12-09_Eviction_Case_MasterFile.docx
┃ ┃ ┣ 📜2025-12-16_case_log_entry.md
┃ ┃ ┣ 📜2025-12-16_case_summary.md
┃ ┃ ┣ 📜case_conversation_log.txt
┃ ┃ ┣ 📜Case_Log.md
┃ ┃ ┣ 📜expenses.csv
┃ ┃ ┣ 📜Financial_Tracker.md
┃ ┃ ┣ 📜index.html
┃ ┃ ┣ 📜index.md
┃ ┃ ┣ 📜Master_Strategy_Canvas.canvas
┃ ┃ ┗ 📜QiCase-FCFCU_Financial_Tracker.xlsx
┃ ┣ 📂05_timeline
┃ ┃ ┣ 📂10_2023
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂20_2024
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂30_2025
┃ ┃ ┃ ┣ 📂30_2025
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-01-16_Case_Filed.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-03-05_Service_Attempt_1.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-04-15_Service_Attempt_2.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-05-13_Motion_for_Default_Judgm.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-05-21_Order_Denying_Default_Ju.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-05-23_Amended_Motion_Default_J.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-05-28_Default_Judgment_Entered.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-05-30_Praecipe_Sheriff_Sale.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-07-09_Sheriff_Sale_Notice_Post.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-08-15_Sheriff_Sale.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-10-29_Petition_for_Writ_of_Ass.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-11-06_Writ_of_Assistance_Issue.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-12-09_Writ_Executed_Removal.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-12-10_Motions_Filed.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-12-11_Court_Orders_and_Hearing.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__2025-12-12_Supplemental_Emergency_M.md
┃ ┃ ┃ ┃ ┣ 📜WA0.00.030__index.html
┃ ┃ ┃ ┃ ┗ 📜WA0.00.030__index.md
┃ ┃ ┃ ┣ 📜2025-01-16_Case_Filed.md
┃ ┃ ┃ ┣ 📜2025-03-05_Service_Attempt_1.md
┃ ┃ ┃ ┣ 📜2025-04-15_Service_Attempt_2.md
┃ ┃ ┃ ┣ 📜2025-05-13_Motion_for_Default_Judgment.md
┃ ┃ ┃ ┣ 📜2025-05-21_Order_Denying_Default_Judgment.md
┃ ┃ ┃ ┣ 📜2025-05-23_Amended_Motion_Default_Judgment.md
┃ ┃ ┃ ┣ 📜2025-05-28_Default_Judgment_Entered.md
┃ ┃ ┃ ┣ 📜2025-05-30_Praecipe_Sheriff_Sale.md
┃ ┃ ┃ ┣ 📜2025-07-09_Sheriff_Sale_Notice_Posted.md
┃ ┃ ┃ ┣ 📜2025-08-15_Sheriff_Sale.md
┃ ┃ ┃ ┣ 📜2025-10-29_Petition_for_Writ_of_Assistance.md
┃ ┃ ┃ ┣ 📜2025-11-06_Writ_of_Assistance_Issued.md
┃ ┃ ┃ ┣ 📜2025-12-09_Writ_Executed_Removal.md
┃ ┃ ┃ ┣ 📜2025-12-10_Motions_Filed.md
┃ ┃ ┃ ┣ 📜2025-12-11_Court_Orders_and_Hearing_Scheduled.md
┃ ┃ ┃ ┣ 📜2025-12-12_Supplemental_Emergency_Motion.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┗ 📜index.md
┃ ┃ ┣ 📂40_2026
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📜Timeline_Canvas.canvas
┃ ┃ ┣ 📜WA0.00.030__index.md
┃ ┃ ┣ 📜WA0.00.030__Timeline_Canvas.canvas
┃ ┃ ┗ 📜WA0.00.060__Master_Timeline.md
┃ ┣ 📂10_overviews
┃ ┃ ┣ 📂critiques
┃ ┃ ┣ 📂debates
┃ ┃ ┣ 📂deep_dives
┃ ┃ ┃ ┗ 📜Integrate_Disability_Separate_Appeals_Get_Stay.m4a
┃ ┃ ┣ 📂explainers
┃ ┃ ┣ 📂infographics
┃ ┃ ┃ ┗ 📜Void_Judgment_Eviction_Crisis.pdf
┃ ┃ ┣ 📂maps
┃ ┃ ┃ ┗ 📜Procedural_failure_map_one_pager.md
┃ ┃ ┣ 📂reports
┃ ┃ ┗ 📜index.html
┃ ┣ 📂20_strategy
┃ ┃ ┣ 📂10_ada_title_ii
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂20_jurisdiction_service_tr_4_1_b
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂30_void_vs_voidable_tr_60b
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📜index.html
┃ ┃ ┣ 📜Settlement_Strategy_and_Contingency_Plan.md
┃ ┃ ┣ 📜Strategic_Plan.canvas
┃ ┃ ┣ 📜WA0.00.01_COMMAND_MAP.canvas
┃ ┃ ┣ 📜WA0.00.010_ACTIVE_STRATEGIES.md
┃ ┃ ┗ 📜WA0.00.020_PROMOTION_CANDIDATES.md
┃ ┣ 📂30_hearing_planner
┃ ┃ ┣ 📜_README.md
┃ ┃ ┣ 📜index.html
┃ ┃ ┣ 📜WA0.01.001_HEARING_GOALS.md
┃ ┃ ┣ 📜WA0.01.002_TALKING_POINTS.md
┃ ┃ ┗ 📜WA0.01.003_JUDGE_QUESTIONS_PREDICTED.md
┃ ┣ 📂90_reference_only
┃ ┣ 📜QiCase-FCFCU_Financial_Tracker.xlsx
┃ ┗ 📜WA0.00.000_WAR_ROOM_OVERVIEW.md
┣ 📂10_PHASES
┃ ┣ 📂01_Foreclosure_Core_Court_Record
┃ ┃ ┣ 📂01_Docket
┃ ┃ ┃ ┣ 📂docket_files
┃ ┃ ┃ ┃ ┣ 📜001_Complaint.pdf
┃ ┃ ┃ ┃ ┣ 📜002_Appearance.pdf
┃ ┃ ┃ ┃ ┣ 📜003_Request_for_Admissions.pdf
┃ ┃ ┃ ┃ ┣ 📜004_Notice_to_Homeowners.pdf
┃ ┃ ┃ ┃ ┣ 📜005_Appearance_2.pdf
┃ ┃ ┃ ┃ ┣ 📜006_Summons_1.pdf
┃ ┃ ┃ ┃ ┣ 📜007_Summons_2.pdf
┃ ┃ ┃ ┃ ┣ 📜008_Summons_3.pdf
┃ ┃ ┃ ┃ ┣ 📜009_Summons_4.pdf
┃ ┃ ┃ ┃ ┣ 📜010_Summons_5.pdf
┃ ┃ ┃ ┃ ┣ 📜011_Service_Returned_03-05-2025.pdf
┃ ┃ ┃ ┃ ┣ 📜012_Service_Returned_04-15-2025.pdf
┃ ┃ ┃ ┃ ┣ 📜013_Motion_for_Default_Judgment.pdf
┃ ┃ ┃ ┃ ┣ 📜014_Affidavit.pdf
┃ ┃ ┃ ┃ ┣ 📜015_Affidavit_Attorney_Fees.pdf
┃ ┃ ┃ ┃ ┣ 📜016_Order_Denying_Motion_for_Default_Judgment.pdf
┃ ┃ ┃ ┃ ┣ 📜017_OMITTED NOTICE OF SERVICE TO DEFENDANT.pdf
┃ ┃ ┃ ┃ ┣ 📜018_Omitted_Notice_of_Service.pdf
┃ ┃ ┃ ┃ ┣ 📜019_Amended_Motion_Default_Judgment_1.pdf
┃ ┃ ┃ ┃ ┣ 📜020_Amended_Motion_Default_Judgment_2.pdf
┃ ┃ ┃ ┃ ┣ 📜021_Praecipe_Sheriff_Sale_1.pdf
┃ ┃ ┃ ┃ ┣ 📜022_Plaintif_bid_2025_07_17_10_14_40.pdf.pdf
┃ ┃ ┃ ┃ ┣ 📜022_Praecipe_Sheriff_Sale_2.pdf
┃ ┃ ┃ ┃ ┣ 📜023_Decree_Foreclosure_Returned.pdf
┃ ┃ ┃ ┃ ┣ 📜024_Petition_Writ_of_Assistance.pdf
┃ ┃ ┃ ┃ ┣ 📜024_Service Returned Served.pdf
┃ ┃ ┃ ┃ ┣ 📜025_Motion_Vacate_Stay_Writ.pdf
┃ ┃ ┃ ┃ ┣ 📜026_Exhibit_List_A-G.pdf
┃ ┃ ┃ ┃ ┣ 📜027_Supplemental_Motion_Access.pdf
┃ ┃ ┃ ┃ ┣ 📜028_Report_Court_Defendant_Request.pdf
┃ ┃ ┃ ┃ ┣ 📜029_Emergency_Supplemental_Declaration.pdf
┃ ┃ ┃ ┃ ┣ 📜030_Report_Sheriff_Sale_No_Excess.pdf
┃ ┃ ┃ ┃ ┣ 📜031_Proposed_Order_Vacate.pdf
┃ ┃ ┃ ┃ ┣ 📜032_Proposed_Order_Stay.pdf
┃ ┃ ┃ ┃ ┣ 📜033_ADA_Disability_Affidavit.pdf
┃ ┃ ┃ ┃ ┗ 📜2025_10_29_13_47_03.pdf.pdf
┃ ┃ ┃ ┣ 📂docket_snapshots
┃ ┃ ┃ ┣ 📜_Case_Summary.md
┃ ┃ ┃ ┗ 📜docket_index.md
┃ ┃ ┣ 📂02_Pleadings_FCFCU
┃ ┃ ┃ ┣ 📂complaint
┃ ┃ ┃ ┣ 📂fcfcu_affidavits_testimony
┃ ┃ ┃ ┣ 📂motions
┃ ┃ ┃ ┗ 📂writ_of_assistance
┃ ┃ ┣ 📂03_Service_Process
┃ ┃ ┃ ┣ 📂sheriff_returns
┃ ┃ ┃ ┣ 📜affidavits_service.md
┃ ┃ ┃ ┗ 📜service_defects_analysis.md
┃ ┃ ┣ 📂04_Orders_Judgements
┃ ┃ ┃ ┣ 📂default_judgement
┃ ┃ ┃ ┣ 📂final_orders
┃ ┃ ┃ ┗ 📂orders_vacate_stay
┃ ┃ ┣ 📂05_Sale_and_Possesion
┃ ┃ ┃ ┣ 📂deed_records
┃ ┃ ┃ ┣ 📂sheriff_sale
┃ ┃ ┃ ┗ 📜possession_admissions.md
┃ ┃ ┣ 📂06_Financial_Accounting
┃ ┃ ┃ ┣ 📂check_balances
┃ ┃ ┃ ┣ 📜interest_fee_irregularities.md
┃ ┃ ┃ ┗ 📜surplus_definciency_analysis.md
┃ ┃ ┣ 📂10_2025-12-10_motion_vacate
┃ ┃ ┃ ┣ 📂01_drafts
┃ ┃ ┃ ┃ ┣ 📜Emergency Motions.docx
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂02_exhibits
┃ ┃ ┃ ┃ ┣ 📜01_motion_vacate.pdf
┃ ┃ ┃ ┃ ┣ 📜02_emergency_motion_quash_stay.pdf
┃ ┃ ┃ ┃ ┣ 📜03_order_vacate_proposed.pdf
┃ ┃ ┃ ┃ ┣ 📜04_order_stay_writ_proposed.pdf
┃ ┃ ┃ ┃ ┣ 📜05_Exhibit_List.pdf
┃ ┃ ┃ ┃ ┣ 📜06_Exhibits_Combined.pdf
┃ ┃ ┃ ┃ ┣ 📜combinepdf.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂03_proposed_order
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜Proposed_Order_Vacate.docx
┃ ┃ ┃ ┣ 📂04_filed_receipts
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜Odyssey_Envelope_Receipt.pdf
┃ ┃ ┃ ┣ 📜.gitkeep
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂20_2025-12-11_Supplemental_Emergency_Motion_Access
┃ ┃ ┃ ┣ 📂01_drafts
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜Supplemental_Emergency_Motion.pdf
┃ ┃ ┃ ┣ 📂02_exhibits
┃ ┃ ┃ ┃ ┣ 📜20_exhibits_combined_source
┃ ┃ ┃ ┃ ┣ 📜Exhibit_H_Declaration.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂04_filed_receipts
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜Odyssey_Envelope_Receipt.pdf
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┗ 📂90_Filed_Record_Snapshot
┃ ┣ 📂02_credit_reporting_FCRA
┃ ┃ ┣ 📂00_Packet_Master
┃ ┃ ┣ 📂01_Bureaus
┃ ┃ ┃ ┣ 📂equifax
┃ ┃ ┃ ┣ 📂experian
┃ ┃ ┃ ┗ 📂transunion
┃ ┃ ┣ 📂02_Furnisher_FCFCU
┃ ┃ ┣ 📂03_CFPB
┃ ┃ ┣ 📂04_Damage_Proof
┃ ┃ ┗ 📂05_Reputational_Pressure
┃ ┃   ┗ 📂better_business_bureau
┃ ┃     ┣ 📂responses
┃ ┃     ┗ 📜complaint.md
┃ ┣ 📂03_ownership_obligations_purge
┃ ┃ ┣ 📂00_Common_Legal_Basis
┃ ┃ ┣ 📂01_AES_Indiana
┃ ┃ ┣ 📂02_Citizens_Energy
┃ ┃ ┣ 📂03_Shadow_Pointe_HOA
┃ ┃ ┗ 📂04_City_Indianapolis
┃ ┣ 📂04_regulations_civil_rights
┃ ┃ ┣ 📂01_State_Local
┃ ┃ ┃ ┣ 📂indiana_attorney_general
┃ ┃ ┃ ┣ 📂indiana_civil_rights_commission
┃ ┃ ┃ ┗ 📂local_housing_or_code
┃ ┃ ┣ 📂02_Federal
┃ ┃ ┃ ┣ 📂CFPB
┃ ┃ ┃ ┣ 📂DOJ_civil_rights_division
┃ ┃ ┃ ┃ ┣ 📂ADA_Title_ii
┃ ┃ ┃ ┃ ┗ 📂housing_disability
┃ ┃ ┃ ┗ 📂Other_Federal_Agencies
┃ ┃ ┗ 📂90_Response_Tracking
┃ ┣ 📂05_litigation_settlement
┃ ┃ ┣ 📂01_Global_Demand
┃ ┃ ┣ 📂02_Preservation_Letters
┃ ┃ ┣ 📂03_Draft_Complaints
┃ ┃ ┗ 📂04_Settement_Docs
┃ ┗ 📂06_Public_Accountability
┃   ┣ 📂01_Public_Timeline
┃   ┣ 📂02_Fact_Checked_Summary
┃   ┣ 📂03_Media_Briefs
┃   ┣ 📂04_Advocacy_Orgs
┃   ┣ 📂90_Published_Material
┃   ┗ 📜00_README_LOCK.md
┣ 📂20_EVIDENCE_VAULT_IMMUTABLE
┃ ┣ 📂00_Index
┃ ┃ ┣ 📜chain_of_custody.md
┃ ┃ ┣ 📜evidence_log.md
┃ ┃ ┗ 📜master_evidence_index.md
┃ ┣ 📂01_Court_Official
┃ ┃ ┣ 📂clerk_records
┃ ┃ ┣ 📂orders_judgements
┃ ┃ ┗ 📂sheriff_documents
┃ ┣ 📂02_credit_reporting
┃ ┃ ┣ 📂bureau_reports
┃ ┃ ┣ 📂furnisher_data
┃ ┃ ┗ 📂score_history
┃ ┣ 📂03_correspondence
┃ ┃ ┣ 📂agencies
┃ ┃ ┣ 📂certified_mail_proof
┃ ┃ ┗ 📂fcfcu
┃ ┣ 📂04_utilities_hoa_city
┃ ┃ ┣ 📂aes
┃ ┃ ┣ 📂citizens
┃ ┃ ┣ 📂city
┃ ┃ ┗ 📂hoa
┃ ┣ 📂05_photos_audio_video
┃ ┣ 📂06_medical_ada_support,
┃ ┣ 📂07_hardships_affidavits,
┃ ┣ 📂08_financial_other,
┃ ┣ 📂99_hashes_and_integrity
┃ ┣ 📜Evidence_Log.md
┃ ┗ 📜index.html
┣ 📂30_WORKING_DRAFTS
┃ ┣ 📂_raw_evidence
┃ ┃ ┣ 📂10_supporting
┃ ┃ ┃ ┣ 📂10_photos_video
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_00241326_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_012aa06e_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_01b3e905_2025-1.png
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_10f4975d_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_1a80b987_2025-1.mp4
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_1beefb11_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_1f3f8a81_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_25fb1992_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_2f0952db_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_49c74ec6_2025-.heic
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_4e01fa01_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_5be451ba_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_5d95cae5_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_61129253_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_63fb7b02_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_71c9e6a7_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_78ba1ccc_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_7a544ef7_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_8350e7be_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_8a163413_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_8d885a5c_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_942cfd7f_2025-1.png
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_9b611100_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_9fb3a08a_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_9ff5022d_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_a8832e17_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_ca02d006_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_db9b10b5_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_e4cb3622_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_ebaaa38d_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_ed6dc885_2025-1.mp4
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_f510498b_2025-.heic
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_f60d8098_2025-1.png
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_f98b089a_2025-1.png
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_fa1703bf_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_fdd8d4ef_2025-1.jpg
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂20_receipts
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-20_receipts_0860d3df_2025-12-20.jpg
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂30_declarations
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂40_affidavits
┃ ┃ ┃ ┃ ┣ 📂ada-disability
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂character
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂community-service
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂credibility
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂observations
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂20_property
┃ ┃ ┃ ┣ 📂10_mortgage_history
┃ ┃ ┃ ┃ ┣ 📂20_payments
┃ ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-20_payments_c5131deb_2025-12-20.png
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂20_parcel
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜Parcel_6016506_ParcelDetailHistory.pdf
┃ ┃ ┃ ┃ ┗ 📜Parcel_6016506_PRC.pdf
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂30_fcfcu
┃ ┃ ┃ ┣ 📜2023-09-20_FCFCU_Hardship_and_Health_Notice_Le.pdf
┃ ┃ ┃ ┣ 📜2023-09-20_FCFCU_Hardship_and_Health_Notice_Let.md
┃ ┃ ┃ ┣ 📜2023-09-20_Notice_Disabilities_Hardship.pdf
┃ ┃ ┃ ┣ 📜2024-03-20_FCFCU_Certified_Response_Tax_Record.pdf
┃ ┃ ┃ ┣ 📜2024-12-09_outgoing_email_bank_access_request.pdf
┃ ┃ ┃ ┣ 📜2024-12-11_outgoing_email_bank_access_request.pdf
┃ ┃ ┃ ┣ 📜2024-20-03_Response_to_tax_notice.pdf
┃ ┃ ┃ ┣ 📜20241204_FCFCU_Statement (1).pdf
┃ ┃ ┃ ┣ 📜20241204_FCFCU_Statement (2).pdf
┃ ┃ ┃ ┣ 📜20241204_FCFCU_Statement.pdf
┃ ┃ ┃ ┣ 📜2025-12-20_EXH-30_fcfcu_740eacdc_2025-12-20_EX.jpg
┃ ┃ ┃ ┣ 📜2025-12-20_EXH-30_fcfcu_ac6eb2ea_2025-12-20_EX.jpg
┃ ┃ ┃ ┣ 📜21June-24-4817Shadow_Appraisal.pdf
┃ ┃ ┃ ┣ 📜FCFCU_v_CR-V_Report_to_Court.pdf
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┗ 📜REPORT_TO_COURT_ON_DEFENDANTS_REQUEST.pdf
┃ ┃ ┣ 📂50_aes
┃ ┃ ┃ ┣ 📜2025-06-08_AES_ADA_Notice.pdf
┃ ┃ ┃ ┣ 📜2025-06-08_AES_ADA_Request_Financial_Hardship_.pdf
┃ ┃ ┃ ┣ 📜2025-12-16_AES_Emergency_Notice.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂99__archive
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┗ 📜README_supporting.md
┃ ┃ ┣ 📜index.html
┃ ┃ ┗ 📜Raw_Exhibit_Map.md
┃ ┣ 📂_templates
┃ ┃ ┣ 📂10_motions
┃ ┃ ┃ ┣ 📂motions_templates
┃ ┃ ┃ ┃ ┣ 📜_Motions.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜index.md
┃ ┃ ┃ ┣ 📜motion_emergency_stay_of_writ.docx
┃ ┃ ┃ ┣ 📜motion_emergency_stay_of_writ.md
┃ ┃ ┃ ┣ 📜motion_emergency_supplemental_motion_ongoing_.docx
┃ ┃ ┃ ┣ 📜motion_emergency_supplemental_motion_ongoing_ha.md
┃ ┃ ┃ ┣ 📜motion_to_vacate_void_judgement.docx
┃ ┃ ┃ ┗ 📜motion_to_vacate_void_judgment.md
┃ ┃ ┣ 📂20_declarations_affidavits
┃ ┃ ┃ ┣ 📂affidavits_templates
┃ ┃ ┃ ┃ ┣ 📜_Instructions_for_witnesses.md
┃ ┃ ┃ ┃ ┣ 📜ADA_Disability_Affidavit.md
┃ ┃ ┃ ┃ ┣ 📜Character_Affidavit.md
┃ ┃ ┃ ┃ ┣ 📜Community_Service_Affidavit.md
┃ ┃ ┃ ┃ ┣ 📜Credibility_Affidavit.md
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜index.md
┃ ┃ ┃ ┃ ┗ 📜Observations_Affidavit.md
┃ ┃ ┃ ┣ 📂declarations_templates
┃ ┃ ┃ ┃ ┣ 📜_Declarations.md
┃ ┃ ┃ ┃ ┣ 📜Gender_Identity_Clarification.md
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜index.md
┃ ┃ ┃ ┣ 📜affidavit_not_served.docx
┃ ┃ ┃ ┣ 📜affidavit_not_served.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜index.md
┃ ┃ ┃ ┣ 📜updated_affidavit_language.md
┃ ┃ ┃ ┗ 📜verified_affidavit_of_defendant.md
┃ ┃ ┣ 📂30_exhibits
┃ ┃ ┃ ┣ 📂exhibits_templates
┃ ┃ ┃ ┃ ┣ 📜_Exhibits_Lists.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜exhibit_list.docx
┃ ┃ ┃ ┣ 📜exhibit_list.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂40_others
┃ ┃ ┃ ┣ 📂outreach_templates
┃ ┃ ┃ ┃ ┣ 📜_Advocate_Outreach_Message.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜ada_packet.md
┃ ┃ ┃ ┣ 📜attorney_brief.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜index.md
┃ ┃ ┃ ┣ 📜receipt_usps_tracking.md
┃ ┃ ┃ ┗ 📜script_call_lawyers.md
┃ ┃ ┣ 📂50_proposed_orders
┃ ┃ ┃ ┣ 📂proposed_templates
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜Proposed_Orders.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜index.md
┃ ┃ ┃ ┣ 📜proposed_order_emergency_stay.md
┃ ┃ ┃ ┗ 📜proposed_order_motion_to_vacate.md
┃ ┃ ┗ 📜index.html
┃ ┣ 📂Case_FCFCU_Personal_Narrative
┃ ┃ ┣ 📂01_Public_Narrative
┃ ┃ ┃ ┣ 📜2025-12-15_they_threw_us_into_the_cold.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┗ 📜Public_Statement.md
┃ ┃ ┣ 📂02_Exposure_and_Harm
┃ ┃ ┃ ┣ 📂Photos_Conditions
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂Weather_Reports
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜Cold_Risk_Report.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂03_Internal_Analysis
┃ ┃ ┃ ┣ 📂Payout_Strategy
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜Long_Term_Payout_Strategy.md
┃ ┃ ┃ ┣ 📂Premonitions
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜Premonitions_I_Knew_Before_I_Knew.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┗ 📜Session_Summary_2025-12-15_i_knew_before_i_knew.md
┃ ┃ ┣ 📂04_Donations_and_Support
┃ ┃ ┃ ┣ 📂Donation_Page_HTML
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂Screenshots_Live_Page
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜Donations_Context.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂05_Timeline
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┗ 📜Master_Timeline.md
┃ ┃ ┗ 📜index.html
┃ ┣ 📂DC_CLAIMS_AND_MOTIONS
┃ ┃ ┣ 📂50_proposed_orders
┃ ┃ ┃ ┣ 📂proposed_templates
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜Proposed_Orders.md
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜index.md
┃ ┃ ┃ ┣ 📜proposed_order_emergency_stay.md
┃ ┃ ┃ ┗ 📜proposed_order_motion_to_vacate.md
┃ ┃ ┣ 📂motions_templates
┃ ┃ ┃ ┣ 📜_Motions.md
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📜_README.md
┃ ┃ ┣ 📜EMERGENCY_FILING_PACKET.md
┃ ┃ ┣ 📜index.html
┃ ┃ ┣ 📜index.md
┃ ┃ ┣ 📜motion_emergency_stay_of_writ.docx
┃ ┃ ┣ 📜motion_emergency_stay_of_writ.md
┃ ┃ ┣ 📜motion_emergency_supplemental_motion_ongoing_.docx
┃ ┃ ┣ 📜motion_emergency_supplemental_motion_ongoing_ha.md
┃ ┃ ┣ 📜motion_to_vacate_void_judgement.docx
┃ ┃ ┣ 📜motion_to_vacate_void_judgment.md
┃ ┃ ┗ 📜Proposed_Order_Vacate.docx
┃ ┣ 📂DF_FACTS_DECLARATIONS
┃ ┃ ┣ 📂affidavits_templates
┃ ┃ ┃ ┣ 📜_Instructions_for_witnesses.md
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜ADA_Disability_Affidavit.md
┃ ┃ ┃ ┣ 📜Character_Affidavit.md
┃ ┃ ┃ ┣ 📜Community_Service_Affidavit.md
┃ ┃ ┃ ┣ 📜Credibility_Affidavit.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜index.md
┃ ┃ ┃ ┗ 📜Observations_Affidavit.md
┃ ┃ ┣ 📂declarations_templates
┃ ┃ ┃ ┣ 📜_Declarations.md
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜Gender_Identity_Clarification.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┗ 📜index.md
┃ ┃ ┣ 📜_README.md
┃ ┃ ┣ 📜affidavit_not_served.docx
┃ ┃ ┣ 📜affidavit_not_served.md
┃ ┃ ┣ 📜index.html
┃ ┃ ┣ 📜index.md
┃ ┃ ┣ 📜updated_affidavit_language.md
┃ ┃ ┗ 📜verified_affidavit_of_defendant.md
┃ ┣ 📂Exhibit_Sets
┃ ┃ ┣ 📂_exhibit_A-H_initial
┃ ┃ ┃ ┣ 📜2025-12-10_MTV_Exhibits_Combined.pdf
┃ ┃ ┃ ┣ 📜Exhibit_A_20250305_Sheriff_Return.pdf
┃ ┃ ┃ ┣ 📜Exhibit_B_20250415_Sheriff_Return.pdf
┃ ┃ ┃ ┣ 📜Exhibit_C_20250116_Incomplete_Summons.pdf
┃ ┃ ┃ ┣ 📜Exhibit_D_20250513_Default_Judgment_Motion.pdf
┃ ┃ ┃ ┣ 📜Exhibit_E_20251029_Petition_for_Writ.pdf
┃ ┃ ┃ ┣ 📜Exhibit_F_Affidavit_Cody_RiceVelasquez.pdf
┃ ┃ ┃ ┣ 📜Exhibit_G1_ADA_Notice_Request.pdf
┃ ┃ ┃ ┣ 📜Exhibit_G2_AES_ADA_Docs_Disconnect_Notices.pdf
┃ ┃ ┃ ┣ 📜Exhibit_H_Declaration.pdf
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂DH_HARD_EXHIBITS
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜exhibit_list.docx
┃ ┃ ┃ ┣ 📜exhibit_list.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┗ 📜TEMPLATE_EXHIBIT_LABEL.md
┃ ┃ ┣ 📂exhibits_I_ada_communications
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂exhibits_J_eviction_removal
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂exhibits_K_financial
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂exhibits_L_statements
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂exhibits_M_court-service
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂exhibits_P_property
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂exhibits_templates
┃ ┃ ┃ ┣ 📜_Exhibits_Lists.md
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📜_checklist.md
┃ ┃ ┗ 📜index.html
┃ ┣ 📂INTERNAL_NOTES_NOT_FOR_COURT
┃ ┃ ┣ 📂DI_INTERNAL_REFERENCE
┃ ┃ ┃ ┣ 📂outreach_templates
┃ ┃ ┃ ┃ ┣ 📜_Advocate_Outreach_Message.md
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜ada_packet.md
┃ ┃ ┃ ┣ 📜attorney_brief.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜index.md
┃ ┃ ┃ ┣ 📜receipt_usps_tracking.md
┃ ┃ ┃ ┣ 📜script_call_lawyers.md
┃ ┃ ┃ ┣ 📜TEMPLATE_COURT_DOC.md
┃ ┃ ┃ ┣ 📜TEMPLATE_HANDUP_PACKET_NOTE.md
┃ ┃ ┃ ┣ 📜TEMPLATE_SECTION_COVER.md
┃ ┃ ┃ ┣ 📜TEMPLATE_SECTION_INDEX.md
┃ ┃ ┃ ┗ 📜TEMPLATE_WAR_NOTE.md
┃ ┃ ┣ 📂REFERENCE_ONLY
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📜index.html
┃ ┃ ┣ 📜move_legacy.py
┃ ┃ ┗ 📜organize_case.py
┃ ┣ 📂VIOLATION_INTELLIGENCE
┃ ┃ ┣ 📂10_VIOLATIONS
┃ ┃ ┃ ┣ 📂CREDIT_BUREAUS
┃ ┃ ┃ ┣ 📂FCFCU
┃ ┃ ┃ ┣ 📂OTHER_PARTIES
┃ ┃ ┃ ┣ 📂REGULATORS_PROCEDURAL
┃ ┃ ┃ ┗ 📂UTILITIES_HOA_CITY
┃ ┃ ┣ 📂90_DISCARDED_OR_MERGED
┃ ┃ ┃ ┗ 📜README.md
┃ ┃ ┣ 📂VIOLATIONS
┃ ┃ ┃ ┣ 📂CREDIT_BUREAUS
┃ ┃ ┃ ┃ ┣ 📜V-011_experian-reinvestigation-failure.md
┃ ┃ ┃ ┃ ┣ 📜V-012_equifax-reinvestigation-failure.md
┃ ┃ ┃ ┃ ┗ 📜V-013_transunion-reinvestigation-failure.md
┃ ┃ ┃ ┣ 📂FCFCU
┃ ┃ ┃ ┃ ┣ 📜V-001_fcfcu-continues-reporting-first-mortgage-post-judgment-sale.md
┃ ┃ ┃ ┃ ┣ 📜V-002_fcfcu-continues-reporting-second-mortgage-post-judgment-sale.md
┃ ┃ ┃ ┃ ┣ 📜V-003_monthly-delinquencies-after-foreclosure-judgment.md
┃ ┃ ┃ ┃ ┣ 📜V-004_past-due-amount-schedule-after-judgment.md
┃ ┃ ┃ ┃ ┣ 📜V-005_failure-to-correct-inaccurate-furnishings.md
┃ ┃ ┃ ┃ ┣ 📜V-006_dual-tradeline-double-counting.md
┃ ┃ ┃ ┃ ┣ 📜V-007_inconsistent-reporting-vs-court-position.md
┃ ┃ ┃ ┃ ┣ 📜V-008_credit-defamation-false-publication.md
┃ ┃ ┃ ┃ ┣ 📜V-009_fdCPA-misrepresentation-of-debt-status.md
┃ ┃ ┃ ┃ ┣ 📜V-010_failure-to-mark-account-foreclosure-closed.md
┃ ┃ ┃ ┃ ┣ 📜V-025_cost-shift-fcfcu-refused-winterize.md
┃ ┃ ┃ ┃ ┣ 📜V-030_service-completed-no-notice-before-writ.md
┃ ┃ ┃ ┃ ┣ 📜V-033_removal-6-7-days-after-deed-recorded.md
┃ ┃ ┃ ┃ ┣ 📜V-036_surplus-funds-declared-resolved.md
┃ ┃ ┃ ┃ ┣ 📜V-037_interest-fees-arbitrarily-inflated.md
┃ ┃ ┃ ┃ ┣ 📜V-038_fcfcu-testimony-winterize-then-leave.md
┃ ┃ ┃ ┃ ┣ 📜V-070_global-demand-letter.md
┃ ┃ ┃ ┃ ┣ 📜V-071_litigation-hold-preservation-letter.md
┃ ┃ ┃ ┃ ┣ 📜V-072_equitable-relief-tradeline-deletion.md
┃ ┃ ┃ ┃ ┣ 📜V-073_damages-credit-score-suppression.md
┃ ┃ ┃ ┃ ┣ 📜V-074_damages-out-of-pocket-costs.md
┃ ┃ ┃ ┃ ┣ 📜V-075_public-accountability-hold.md
┃ ┃ ┃ ┃ ┣ 📜V-080_conversion-negligence-post-removal-damage.md
┃ ┃ ┃ ┃ ┗ 📜V-081_evidence-spoliation-unplugged-cameras.md
┃ ┃ ┃ ┣ 📂OTHER_PARTIES
┃ ┃ ┃ ┃ ┣ 📜V-076_fha-reasonable-accommodation-failure.md
┃ ┃ ┃ ┃ ┣ 📜V-077_ada-title-iii-entertainment-access-failure.md
┃ ┃ ┃ ┃ ┣ 📜V-078_ada-effective-communication-failure.md
┃ ┃ ┃ ┃ ┣ 📜V-083_discriminatory-maintenance-redlining.md
┃ ┃ ┃ ┃ ┗ 📜V-084_predatory-land-contract-reverse-redlining.md
┃ ┃ ┃ ┣ 📂REGULATORS_PROCEDURAL
┃ ┃ ┃ ┃ ┣ 📜V-031_sheriff-return-inaccuracies.md
┃ ┃ ┃ ┃ ┣ 📜V-032_no-ada-compliant-notice.md
┃ ┃ ┃ ┃ ┣ 📜V-034_attorney-appeared-without-formal-appearance.md
┃ ┃ ┃ ┃ ┣ 📜V-035_court-relied-on-service-sufficiency.md
┃ ┃ ┃ ┃ ┣ 📜V-050_cfpb-complaint-track.md
┃ ┃ ┃ ┃ ┣ 📜V-051_indiana-ag-complaint-track.md
┃ ┃ ┃ ┃ ┣ 📜V-052_icrc-complaint-track.md
┃ ┃ ┃ ┃ ┣ 📜V-053_doj-civil-rights-complaint-track.md
┃ ┃ ┃ ┃ ┣ 📜V-060_bbb-complaint-reputational-pressure.md
┃ ┃ ┃ ┃ ┣ 📜V-079_void-judgment-procedural-error.md
┃ ┃ ┃ ┃ ┗ 📜V-082_fraud-on-the-court-material-misrepresentation.md
┃ ┃ ┃ ┗ 📂UTILITIES_HOA_CITY
┃ ┃ ┃   ┣ 📜V-020_post-0815-aes-electric-charges-billed.md
┃ ┃ ┃   ┣ 📜V-021_post-0815-citizens-energy-charges-billed.md
┃ ┃ ┃   ┣ 📜V-022_post-0815-hoa-assessments-billed.md
┃ ┃ ┃   ┣ 📜V-023_city-grass-cut-ticket-assessed-after-loss-of-access.md
┃ ┃ ┃   ┣ 📜V-024_municipal-code-enforcement-after-possession-transfer.md
┃ ┃ ┃   ┗ 📜V-026_credit-harm-compounded-utility-municipal.md
┃ ┃ ┣ 📜00_README_SYSTEM.md
┃ ┃ ┣ 📜01_MASTER_INDEX_APPEND.md
┃ ┃ ┣ 📜01_MASTER_INDEX_FULL.md
┃ ┃ ┣ 📜01_MASTER_INDEX.md
┃ ┃ ┣ 📜02_TAG_MAP.md
┃ ┃ ┣ 📜03_THEORY_CLUSTERS.md
┃ ┃ ┣ 📜04_RISK_REGISTER.md
┃ ┃ ┗ 📜V-000_TEMPLATE.md
┃ ┣ 📂WB_BASIS
┃ ┃ ┣ 📂WB1_00_LAW_RESEARCH
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WB1.00.001_CASE_LAW_RESEARCH.md
┃ ┃ ┃ ┣ 📜WB1.00.002_VOID_VS_VOIDABLE_ANALYSIS.md
┃ ┃ ┃ ┗ 📜WB1.00.003_JURISDICTION_THEORY.md
┃ ┃ ┣ 📂WB1_01_ALTERNATE_THEORIES
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WB1.01.001_BACKUP_ARGUMENTS.md
┃ ┃ ┃ ┗ 📜WB1.01.002_IF_JUDGE_PUSHBACK.md
┃ ┃ ┣ 📜_README.md
┃ ┃ ┗ 📜index.html
┃ ┣ 📂WC_CLAIMS_AND_MOTIONS
┃ ┃ ┣ 📂WC2_00_DRAFT_MOTIONS
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WC2.00.001_DRAFT_MOTION_VACATE.md
┃ ┃ ┃ ┣ 📜WC2.00.002_DRAFT_EMERGENCY_STAY.md
┃ ┃ ┃ ┣ 📜WC2.00.003_DRAFT_SUPPLEMENTAL.md
┃ ┃ ┃ ┣ 📜WC2.00.010___Motions.md
┃ ┃ ┃ ┣ 📜WC2.00.010__motion_emergency_stay_of_writ.docx
┃ ┃ ┃ ┣ 📜WC2.00.010__motion_emergency_stay_of_writ.md
┃ ┃ ┃ ┣ 📜WC2.00.010__motion_emergency_supplemental_mot.docx
┃ ┃ ┃ ┣ 📜WC2.00.010__motion_emergency_supplemental_motio.md
┃ ┃ ┃ ┣ 📜WC2.00.010__motion_to_vacate_void_judgement.docx
┃ ┃ ┃ ┗ 📜WC2.00.010__motion_to_vacate_void_judgment.md
┃ ┃ ┣ 📂WC2_01_PROPOSED_ORDERS
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WC2.01.001_DRAFT_ORDER_VACATE.md
┃ ┃ ┃ ┣ 📜WC2.01.002_DRAFT_ORDER_STAY.md
┃ ┃ ┃ ┣ 📜WC2.01.010__index.html
┃ ┃ ┃ ┣ 📜WC2.01.010__index.md
┃ ┃ ┃ ┣ 📜WC2.01.010__proposed_order_emergency_stay.md
┃ ┃ ┃ ┣ 📜WC2.01.010__proposed_order_motion_to_vacate.md
┃ ┃ ┃ ┗ 📜WC2.01.010__Proposed_Orders.md
┃ ┃ ┣ 📜_README.md
┃ ┃ ┗ 📜index.html
┃ ┣ 📂WD_SERVICE
┃ ┃ ┣ 📂WD3_00_SERVICE_TRACKING
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WD3.00.001_SERVICE_MATRIX.md
┃ ┃ ┃ ┗ 📜WD3.00.002_SERVICE_FAILURE_ANALYSIS.md
┃ ┃ ┣ 📂WD3_01_SERVICE_EVIDENCE
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WD3.01.001_SUMMONS_SOURCE.pdf
┃ ┃ ┃ ┗ 📜WD3.01.002_SHERIFF_METADATA.md
┃ ┃ ┣ 📜_README.md
┃ ┃ ┗ 📜index.html
┃ ┣ 📂WE_EFFECTS_PROCEDURAL
┃ ┃ ┣ 📂WE4_00_CHAIN_ANALYSIS
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WE4.00.001_PROCEDURAL_FAILURE_MAP.md
┃ ┃ ┃ ┣ 📜WE4.00.002_BUT_FOR_ANALYSIS.md
┃ ┃ ┃ ┣ 📜WE4.00.010__Integrate_Disability_Separate_Appe.m4a
┃ ┃ ┃ ┣ 📜WE4.00.010__Procedural_failure_map_one_pager.md
┃ ┃ ┃ ┗ 📜WE4.00.010__Void_Judgment_Eviction_Crisis.pdf
┃ ┃ ┣ 📂WE4_01_REMEDIES
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WE4.01.001_STAY_PATHS.md
┃ ┃ ┃ ┗ 📜WE4.01.002_REVERSAL_PATHS.md
┃ ┃ ┣ 📜_README.md
┃ ┃ ┗ 📜index.html
┃ ┣ 📂WF_DECLARATIONS
┃ ┃ ┣ 📂WF5_00_FACT_DEVELOPMENT
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WF5.00.001_FACT_TIMELINE.md
┃ ┃ ┃ ┗ 📜WF5.00.002_FACT_GAPS.md
┃ ┃ ┣ 📂WF5_01_DRAFT_DECLARATIONS
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WF5.01.001_DRAFT_AFFIDAVIT.md
┃ ┃ ┃ ┣ 📜WF5.01.002_DRAFT_DECLARATION.md
┃ ┃ ┃ ┣ 📜WF5.01.010___Declarations.md
┃ ┃ ┃ ┣ 📜WF5.01.010___Instructions_for_witnesses.md
┃ ┃ ┃ ┣ 📜WF5.01.010__ADA_Disability_Affidavit.md
┃ ┃ ┃ ┣ 📜WF5.01.010__affidavit_not_served.docx
┃ ┃ ┃ ┣ 📜WF5.01.010__affidavit_not_served.md
┃ ┃ ┃ ┣ 📜WF5.01.010__Character_Affidavit.md
┃ ┃ ┃ ┣ 📜WF5.01.010__Community_Service_Affidavit.md
┃ ┃ ┃ ┣ 📜WF5.01.010__Credibility_Affidavit.md
┃ ┃ ┃ ┣ 📜WF5.01.010__Gender_Identity_Clarification.md
┃ ┃ ┃ ┣ 📜WF5.01.010__index 1.md
┃ ┃ ┃ ┣ 📜WF5.01.010__index.html
┃ ┃ ┃ ┣ 📜WF5.01.010__index.md
┃ ┃ ┃ ┣ 📜WF5.01.010__Observations_Affidavit.md
┃ ┃ ┃ ┣ 📜WF5.01.010__updated_affidavit_language.md
┃ ┃ ┃ ┗ 📜WF5.01.010__verified_affidavit_of_defendant.md
┃ ┃ ┣ 📜_README.md
┃ ┃ ┗ 📜index.html
┃ ┣ 📂WG_GROUNDS_ADA
┃ ┃ ┣ 📂WG6_00_ADA_STRATEGY
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WG6.00.001_ADA_TITLE_II_ANALYSIS.md
┃ ┃ ┃ ┗ 📜WG6.00.002_REASONABLE_ACCOMMODATIONS.md
┃ ┃ ┣ 📂WG6_01_PARALLEL_ENFORCEMENT
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WG6.01.001_DOJ_COMPLAINT.md
┃ ┃ ┃ ┣ 📜WG6.01.002_ICRC_COMPLAINT.md
┃ ┃ ┃ ┗ 📜WG6.01.003_STATUS_TRACKER.md
┃ ┃ ┣ 📜_README.md
┃ ┃ ┗ 📜index.html
┃ ┣ 📂WH7_00_RAW_INTAKE
┃ ┃ ┣ 📂10_supporting
┃ ┃ ┃ ┣ 📂10_photos_video
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_00241326_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_012aa06e_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_01b3e905_2025-1.png
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_10f4975d_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_1a80b987_2025-1.mp4
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_1beefb11_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_1f3f8a81_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_25fb1992_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_2f0952db_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_49c74ec6_2025-.heic
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_4e01fa01_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_5be451ba_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_5d95cae5_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_61129253_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_63fb7b02_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_71c9e6a7_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_78ba1ccc_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_7a544ef7_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_8350e7be_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_8a163413_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_8d885a5c_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_942cfd7f_2025-1.png
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_9b611100_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_9fb3a08a_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_9ff5022d_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_a8832e17_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_ca02d006_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_db9b10b5_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_e4cb3622_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_ebaaa38d_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_ed6dc885_2025-1.mp4
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_f510498b_2025-.heic
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_f60d8098_2025-1.png
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_f98b089a_2025-1.png
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_fa1703bf_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-10_photos_video_fdd8d4ef_2025-1.jpg
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_002.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_012.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_01b.png
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_10f.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_1a8.mp4
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_1be.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_1f3.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_25f.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_2f0.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_49.heic
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_4e0.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_5be.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_5d9.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_611.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_63f.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_71c.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_78b.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_7a5.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_835.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_8a1.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_8d8.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_942.png
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_9b6.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_9fb.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_9ff.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_a88.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_ca0.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_db9.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_e4c.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_eba.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_ed6.mp4
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_f5.heic
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_f60.png
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_f98.png
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_fa1.jpg
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-10_photos_video_fdd.jpg
┃ ┃ ┃ ┃ ┗ 📜WH7.00.020__index.html
┃ ┃ ┃ ┣ 📂20_receipts
┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-20_receipts_0860d3df_2025-12-20.jpg
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-20_receipts_0860d3d.jpg
┃ ┃ ┃ ┃ ┗ 📜WH7.00.020__index.html
┃ ┃ ┃ ┣ 📂30_declarations
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜WH7.00.020__index.html
┃ ┃ ┃ ┣ 📂40_affidavits
┃ ┃ ┃ ┃ ┣ 📂ada-disability
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜WH7.00.020__index.html
┃ ┃ ┃ ┃ ┣ 📂character
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜WH7.00.020__index.html
┃ ┃ ┃ ┃ ┣ 📂community-service
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜WH7.00.020__index.html
┃ ┃ ┃ ┃ ┣ 📂credibility
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜WH7.00.020__index.html
┃ ┃ ┃ ┃ ┣ 📂observations
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜WH7.00.020__index.html
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜WH7.00.020__index.html
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┗ 📜WH7.00.020__index.html
┃ ┃ ┣ 📂20_property
┃ ┃ ┃ ┣ 📂10_mortgage_history
┃ ┃ ┃ ┃ ┣ 📂20_payments
┃ ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_EXH-20_payments_c5131deb_2025-12-20.png
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-20_payments_c5131de.png
┃ ┃ ┃ ┃ ┃ ┗ 📜WH7.00.020__index.html
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜WH7.00.020__index.html
┃ ┃ ┃ ┣ 📂20_parcel
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜Parcel_6016506_ParcelDetailHistory.pdf
┃ ┃ ┃ ┃ ┣ 📜Parcel_6016506_PRC.pdf
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__index.html
┃ ┃ ┃ ┃ ┣ 📜WH7.00.020__Parcel_6016506_ParcelDetailHistory.pdf
┃ ┃ ┃ ┃ ┗ 📜WH7.00.020__Parcel_6016506_PRC.pdf
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┗ 📜WH7.00.020__index.html
┃ ┃ ┣ 📂30_declarations
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂30_fcfcu
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜2023-09-20_FCFCU_Hardship_and_Health_Notice_Le.pdf
┃ ┃ ┃ ┣ 📜2023-09-20_FCFCU_Hardship_and_Health_Notice_Let.md
┃ ┃ ┃ ┣ 📜2023-09-20_Notice_Disabilities_Hardship.pdf
┃ ┃ ┃ ┣ 📜2024-03-20_FCFCU_Certified_Response_Tax_Record.pdf
┃ ┃ ┃ ┣ 📜2024-12-09_outgoing_email_bank_access_request.pdf
┃ ┃ ┃ ┣ 📜2024-12-11_outgoing_email_bank_access_request.pdf
┃ ┃ ┃ ┣ 📜2024-20-03_Response_to_tax_notice.pdf
┃ ┃ ┃ ┣ 📜20241204_FCFCU_Statement (1).pdf
┃ ┃ ┃ ┣ 📜20241204_FCFCU_Statement (2).pdf
┃ ┃ ┃ ┣ 📜20241204_FCFCU_Statement.pdf
┃ ┃ ┃ ┣ 📜2025-12-20_EXH-30_fcfcu_740eacdc_2025-12-20_EX.jpg
┃ ┃ ┃ ┣ 📜2025-12-20_EXH-30_fcfcu_ac6eb2ea_2025-12-20_EX.jpg
┃ ┃ ┃ ┣ 📜21June-24-4817Shadow_Appraisal.pdf
┃ ┃ ┃ ┣ 📜FCFCU_v_CR-V_Report_to_Court.pdf
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜REPORT_TO_COURT_ON_DEFENDANTS_REQUEST.pdf
┃ ┃ ┃ ┣ 📜WH7.00.020__2023-09-20_FCFCU_Hardship_and_Heal.pdf
┃ ┃ ┃ ┣ 📜WH7.00.020__2023-09-20_FCFCU_Hardship_and_Healt.md
┃ ┃ ┃ ┣ 📜WH7.00.020__2023-09-20_Notice_Disabilities_Har.pdf
┃ ┃ ┃ ┣ 📜WH7.00.020__2024-03-20_FCFCU_Certified_Respons.pdf
┃ ┃ ┃ ┣ 📜WH7.00.020__2024-12-09_outgoing_email_bank_acc.pdf
┃ ┃ ┃ ┣ 📜WH7.00.020__2024-12-11_outgoing_email_bank_acc.pdf
┃ ┃ ┃ ┣ 📜WH7.00.020__2024-20-03_Response_to_tax_notice.pdf
┃ ┃ ┃ ┣ 📜WH7.00.020__20241204_FCFCU_Statement (1).pdf
┃ ┃ ┃ ┣ 📜WH7.00.020__20241204_FCFCU_Statement (2).pdf
┃ ┃ ┃ ┣ 📜WH7.00.020__20241204_FCFCU_Statement.pdf
┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-30_fcfcu_740eacdc_2.jpg
┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-20_EXH-30_fcfcu_ac6eb2ea_2.jpg
┃ ┃ ┃ ┣ 📜WH7.00.020__21June-24-4817Shadow_Appraisal.pdf
┃ ┃ ┃ ┣ 📜WH7.00.020__FCFCU_v_CR-V_Report_to_Court.pdf
┃ ┃ ┃ ┣ 📜WH7.00.020__index.html
┃ ┃ ┃ ┗ 📜WH7.00.020__REPORT_TO_COURT_ON_DEFENDANTS_REQU.pdf
┃ ┃ ┣ 📂40_affidavits
┃ ┃ ┃ ┣ 📂ada-disability
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂character
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂community-service
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂credibility
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂observations
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂50_aes
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜2025-06-08_AES_ADA_Notice.pdf
┃ ┃ ┃ ┣ 📜2025-06-08_AES_ADA_Request_Financial_Hardship_.pdf
┃ ┃ ┃ ┣ 📜2025-12-16_AES_Emergency_Notice.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WH7.00.020__2025-06-08_AES_ADA_Notice.pdf
┃ ┃ ┃ ┣ 📜WH7.00.020__2025-06-08_AES_ADA_Request_Financi.pdf
┃ ┃ ┃ ┣ 📜WH7.00.020__2025-12-16_AES_Emergency_Notice.md
┃ ┃ ┃ ┗ 📜WH7.00.020__index.html
┃ ┃ ┣ 📂99__archive
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WH7.00.020__index.html
┃ ┃ ┃ ┗ 📜WH7.00.020__README_supporting.md
┃ ┃ ┣ 📜_README.md
┃ ┃ ┣ 📜index.html
┃ ┃ ┣ 📜Raw_Exhibit_Map.md
┃ ┃ ┣ 📜WH7.00.001_RAW_PHONE_DUMP.md
┃ ┃ ┣ 📜WH7.00.002_RAW_VIDEO_AUDIO.md
┃ ┃ ┣ 📜WH7.00.003_RAW_SCREENSHOTS.md
┃ ┃ ┗ 📜WH7.00.020__Raw_Exhibit_Map.md
┃ ┣ 📂WH7_01_POTENTIAL_EXHIBITS
┃ ┃ ┣ 📂10_EXHIBIT_SETS
┃ ┃ ┃ ┣ 📂_exhibit_A-H_initial
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜WH7.01.0100__2025-12-10_MTV_Exhibits_Combined.pdf
┃ ┃ ┃ ┃ ┣ 📜WH7.01.0100__Exhibit_A_20250305_Sheriff_Return.pdf
┃ ┃ ┃ ┃ ┣ 📜WH7.01.0100__Exhibit_B_20250415_Sheriff_Return.pdf
┃ ┃ ┃ ┃ ┣ 📜WH7.01.0100__Exhibit_C_20250116_Incomplete_Sum.pdf
┃ ┃ ┃ ┃ ┣ 📜WH7.01.0100__Exhibit_D_20250513_Default_Judgme.pdf
┃ ┃ ┃ ┃ ┣ 📜WH7.01.0100__Exhibit_E_20251029_Petition_for_W.pdf
┃ ┃ ┃ ┃ ┣ 📜WH7.01.0100__Exhibit_F_Affidavit_Cody_RiceVela.pdf
┃ ┃ ┃ ┃ ┣ 📜WH7.01.0100__Exhibit_G1_ADA_Notice_Request.pdf
┃ ┃ ┃ ┃ ┣ 📜WH7.01.0100__Exhibit_G2_AES_ADA_Docs_Disconnec.pdf
┃ ┃ ┃ ┃ ┣ 📜WH7.01.0100__Exhibit_H_Declaration.pdf
┃ ┃ ┃ ┃ ┗ 📜WH7.01.0100__index.html
┃ ┃ ┃ ┣ 📂exhibits_I_ada_communications
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜WH7.01.0100__index.html
┃ ┃ ┃ ┣ 📂exhibits_J_eviction_removal
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜WH7.01.0100__index.html
┃ ┃ ┃ ┣ 📂exhibits_K_financial
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜WH7.01.0100__index.html
┃ ┃ ┃ ┣ 📂exhibits_L_statements
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜WH7.01.0100__index.html
┃ ┃ ┃ ┣ 📂exhibits_M_court-service
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜WH7.01.0100__index.html
┃ ┃ ┃ ┣ 📂exhibits_P_property
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜WH7.01.0100__index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WH7.01.0100___checklist.md
┃ ┃ ┃ ┗ 📜WH7.01.0100__index.html
┃ ┃ ┣ 📂30_exhibits
┃ ┃ ┃ ┣ 📂exhibits_templates
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜WH7.01.0050___Exhibits_Lists.md
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WH7.01.0050__exhibit_list.docx
┃ ┃ ┃ ┗ 📜WH7.01.0050__exhibit_list.md
┃ ┃ ┣ 📜index.html
┃ ┃ ┣ 📜WH7.01.0001_POTENTIAL_EXHIBIT_0001.pdf
┃ ┃ ┗ 📜WH7.01.0002_POTENTIAL_EXHIBIT_0002.pdf
┃ ┣ 📂WI_INTERNAL
┃ ┃ ┣ 📂00_trackers
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜index.md
┃ ┃ ┃ ┗ 📜Session_Summary_2025-12-16_fcfcu_case_dna_strat.md
┃ ┃ ┣ 📂05_timeline
┃ ┃ ┃ ┣ 📂30_2025
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜2025-01-16_Case_Filed.md
┃ ┃ ┃ ┃ ┣ 📜2025-03-05_Service_Attempt_1.md
┃ ┃ ┃ ┃ ┣ 📜2025-04-15_Service_Attempt_2.md
┃ ┃ ┃ ┃ ┣ 📜2025-05-13_Motion_for_Default_Judgment.md
┃ ┃ ┃ ┃ ┣ 📜2025-05-21_Order_Denying_Default_Judgment.md
┃ ┃ ┃ ┃ ┣ 📜2025-05-23_Amended_Motion_Default_Judgment.md
┃ ┃ ┃ ┃ ┣ 📜2025-05-28_Default_Judgment_Entered.md
┃ ┃ ┃ ┃ ┣ 📜2025-05-30_Praecipe_Sheriff_Sale.md
┃ ┃ ┃ ┃ ┣ 📜2025-07-09_Sheriff_Sale_Notice_Posted.md
┃ ┃ ┃ ┃ ┣ 📜2025-08-15_Sheriff_Sale.md
┃ ┃ ┃ ┃ ┣ 📜2025-10-29_Petition_for_Writ_of_Assistance.md
┃ ┃ ┃ ┃ ┣ 📜2025-11-06_Writ_of_Assistance_Issued.md
┃ ┃ ┃ ┃ ┣ 📜2025-12-09_Writ_Executed_Removal.md
┃ ┃ ┃ ┃ ┣ 📜2025-12-10_Motions_Filed.md
┃ ┃ ┃ ┃ ┣ 📜2025-12-11_Court_Orders_and_Hearing_Scheduled.md
┃ ┃ ┃ ┃ ┣ 📜2025-12-12_Supplemental_Emergency_Motion.md
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜index.md
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜index.md
┃ ┃ ┃ ┗ 📜Timeline_Canvas.canvas
┃ ┃ ┣ 📂10_overviews
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜Integrate_Disability_Separate_Appeals_Get_Stay.m4a
┃ ┃ ┃ ┣ 📜Procedural_failure_map_one_pager.md
┃ ┃ ┃ ┗ 📜Void_Judgment_Eviction_Crisis.pdf
┃ ┃ ┣ 📂20_strategy
┃ ┃ ┃ ┣ 📂10_ada_title_ii
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂20_jurisdiction_service_tr_4_1_b
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂30_void_vs_voidable_tr_60b
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┗ 📜Strategic_Plan.canvas
┃ ┃ ┣ 📂personal_narrative
┃ ┃ ┃ ┣ 📂01_Public_Narrative
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜2025-12-15_they_threw_us_into_the_cold.md
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜Public_Statement.md
┃ ┃ ┃ ┣ 📂02_Exposure_and_Harm
┃ ┃ ┃ ┃ ┣ 📂Photos_Conditions
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂Weather_Reports
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜Cold_Risk_Report.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂03_Internal_Analysis
┃ ┃ ┃ ┃ ┣ 📂Payout_Strategy
┃ ┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜Long_Term_Payout_Strategy.md
┃ ┃ ┃ ┃ ┣ 📂Premonitions
┃ ┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜Premonitions_I_Knew_Before_I_Knew.md
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜Session_Summary_2025-12-15_i_knew_before_i_knew.md
┃ ┃ ┃ ┣ 📂04_Donations_and_Support
┃ ┃ ┃ ┃ ┣ 📂Donation_Page_HTML
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂Screenshots_Live_Page
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜Donations_Context.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂05_Timeline
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜Master_Timeline.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂WI8_00_DOCKET_RECORD
┃ ┃ ┃ ┣ 📂legacy
┃ ┃ ┃ ┃ ┣ 📂30_court_record
┃ ┃ ┃ ┃ ┃ ┣ 📂10_docket
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001___Case_Summary.md
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__001_Complaint.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__002_Appearance.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__003_Request_for_Admissions.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__004_Notice_to_Homeowners.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__005_Appearance_2.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__006_Summons_1.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__007_Summons_2.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__008_Summons_3.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__009_Summons_4.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__010_Summons_5.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__011_Service_Returned_03-05-2025.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__012_Service_Returned_04-15-2025.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__013_Motion_for_Default_Judgment.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__014_Affidavit.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__015_Affidavit_Attorney_Fees.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__016_Affidavit_Additional.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__017_Order_Denying_Default_Judgment.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__018_Omitted_Notice_of_Service.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__019_Amended_Motion_Default_Judgmen.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__020_Amended_Motion_Default_Judgmen.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__021_Praecipe_Sheriff_Sale_1.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__022_Praecipe_Sheriff_Sale_2.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__023_Decree_Foreclosure_Returned.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__024_Petition_Writ_of_Assistance.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__025_Motion_Vacate_Stay_Writ.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__026_Exhibit_List_A-G.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__027_Supplemental_Motion_Access.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__028_Report_Court_Defendant_Request.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__029_Emergency_Supplemental_Declara.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__030_Report_Sheriff_Sale_No_Excess.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__031_Proposed_Order_Vacate.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__032_Proposed_Order_Stay.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.00.001__033_ADA_Disability_Affidavit.pdf
┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜WI8.00.001__index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WI8.00.001_FULL_DOCKET.pdf
┃ ┃ ┃ ┗ 📜WI8.00.002_DOCKET_NOTES.md
┃ ┃ ┣ 📂WI8_01_PUBLIC_ADVOCACY
┃ ┃ ┃ ┣ 📂al_narrative
┃ ┃ ┃ ┃ ┣ 📂01_Public_Narrative
┃ ┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.01.010__2025-12-15_they_threw_us_into_the_c.md
┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.01.010__index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜WI8.01.010__Public_Statement.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂rrative
┃ ┃ ┃ ┃ ┣ 📂04_Donations_and_Support
┃ ┃ ┃ ┃ ┃ ┣ 📂Donation_Page_HTML
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜WI8.01.050__index.html
┃ ┃ ┃ ┃ ┃ ┣ 📂Screenshots_Live_Page
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜WI8.01.050__index.html
┃ ┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.01.050__Donations_Context.md
┃ ┃ ┃ ┃ ┃ ┗ 📜WI8.01.050__index.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WI8.01.001_PRESS_STRATEGY.md
┃ ┃ ┃ ┣ 📜WI8.01.002_SOCIAL_MEDIA_PLAN.md
┃ ┃ ┃ ┗ 📜WI8.01.003_TIMING_AND_RISK.md
┃ ┃ ┣ 📂WI8_02_DAMAGES_AND_SETTLEMENT
┃ ┃ ┃ ┣ 📂l_narrative
┃ ┃ ┃ ┃ ┣ 📂02_Exposure_and_Harm
┃ ┃ ┃ ┃ ┃ ┣ 📂Photos_Conditions
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜WI8.02.050__index.html
┃ ┃ ┃ ┃ ┃ ┣ 📂Weather_Reports
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜WI8.02.050__index.html
┃ ┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.02.050__Cold_Risk_Report.md
┃ ┃ ┃ ┃ ┃ ┗ 📜WI8.02.050__index.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂on
┃ ┃ ┃ ┃ ┣ 📂__legacy
┃ ┃ ┃ ┃ ┃ ┣ 📂00_admin
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂00_trackers
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.02.010__03_Case_Log_Entry_2025-12-15.md
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.02.010__2024-12-09_Eviction_Case_MasterFi.docx
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.02.010__2025-12-16_case_log_entry.md
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.02.010__2025-12-16_case_summary.md
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.02.010__case_conversation_log.txt
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.02.010__Case_Log.md
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.02.010__expenses.csv
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.02.010__Financial_Tracker.md
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.02.010__index.html
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.02.010__index.md
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.02.010__QiCase-FCFCU_Financial_Tracker.xlsx
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.02.010__Session_Summary_2025-12-16_fcfcu__1.md
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜WI8.02.010__Session_Summary_2025-12-16_fcfcu_ca.md
┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WI8.02.001_ECONOMIC_HARM.md
┃ ┃ ┃ ┣ 📜WI8.02.002_NON_ECONOMIC_HARM.md
┃ ┃ ┃ ┗ 📜WI8.02.003_SETTLEMENT_SCENARIOS.md
┃ ┃ ┣ 📂WI8_99_INTERNAL_ONLY
┃ ┃ ┃ ┣ 📂l_narrative
┃ ┃ ┃ ┃ ┣ 📂03_Internal_Analysis
┃ ┃ ┃ ┃ ┃ ┣ 📂Payout_Strategy
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.99.010__index.html
┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜WI8.99.010__Long_Term_Payout_Strategy.md
┃ ┃ ┃ ┃ ┃ ┣ 📂Premonitions
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.99.010__index.html
┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜WI8.99.010__Premonitions_I_Knew_Before_I_Knew.md
┃ ┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┣ 📜WI8.99.010__index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜WI8.99.010__Session_Summary_2025-12-15_i_knew_b.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📜_README.md
┃ ┃ ┣ 📜03_Case_Log_Entry_2025-12-15.md
┃ ┃ ┣ 📜2024-12-09_Eviction_Case_MasterFile.docx
┃ ┃ ┣ 📜2025-12-16_case_log_entry.md
┃ ┃ ┣ 📜2025-12-16_case_summary.md
┃ ┃ ┣ 📜Case Narrative - Wrongful Foreclosure and Displ.md
┃ ┃ ┣ 📜case_conversation_log.txt
┃ ┃ ┣ 📜Case_Log.md
┃ ┃ ┣ 📜combinepdf.pdf
┃ ┃ ┣ 📜Contacts.md
┃ ┃ ┣ 📜Crisis_The_Anatomy_of_Institutional_Failure.pdf
┃ ┃ ┣ 📜Debate.m4a
┃ ┃ ┣ 📜expenses.csv
┃ ┃ ┣ 📜Financial_Tracker.md
┃ ┃ ┣ 📜Foreclosure and Housing Litigation Case Record.csv
┃ ┃ ┣ 📜Foreclosure_Void_Judgment_Institutional_Failur.m4a
┃ ┃ ┣ 📜Foreclosure_Void_Versus_Damages_Due_Process.m4a
┃ ┃ ┣ 📜Forensic_Audit_of_a_Void_Foreclosure.m4a
┃ ┃ ┣ 📜Formal Inventory of Violations and Schedule of .md
┃ ┃ ┣ 📜index.html
┃ ┃ ┣ 📜Inventory of Civil and Fair Housing Rights Vio.csv
┃ ┃ ┣ 📜LEGAL MEMORANDUM.md
┃ ┃ ┣ 📜Odyssey_Envelope_Receipt.pdf
┃ ┃ ┣ 📜Proposal for Strategic Reports in the Matter of.md
┃ ┃ ┣ 📜Talking_Points.md
┃ ┃ ┗ 📜Wrongful_Foreclosure_A_Case_Study_in_Civil_Rig.pdf
┃ ┣ 📂WZ_PROMOTION
┃ ┃ ┣ 📂WZ9_00_050_FILINGS
┃ ┃ ┃ ┣ 📂motion_vacate
┃ ┃ ┃ ┃ ┣ 📂01_drafts
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__Emergency Motions.docx
┃ ┃ ┃ ┃ ┃ ┗ 📜WZ9.00.050__index.html
┃ ┃ ┃ ┃ ┣ 📂02_exhibits
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__01_motion_vacate.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__02_emergency_motion_quash_stay.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__03_order_vacate_proposed.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__04_order_stay_writ_proposed.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__05_Exhibit_List.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__06_Exhibits_Combined.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__combinepdf.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜WZ9.00.050__index.html
┃ ┃ ┃ ┃ ┣ 📂03_proposed_order
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜WZ9.00.050__Proposed_Order_Vacate.docx
┃ ┃ ┃ ┃ ┣ 📂04_filed_receipts
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜WZ9.00.050__Odyssey_Envelope_Receipt.pdf
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__.gitkeep
┃ ┃ ┃ ┃ ┗ 📜WZ9.00.050__index.html
┃ ┃ ┃ ┣ 📂Supplemental
┃ ┃ ┃ ┃ ┣ 📂01_drafts
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜WZ9.00.050__Supplemental_Emergency_Motion.pdf
┃ ┃ ┃ ┃ ┣ 📂02_exhibits
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__20_exhibits_combined_source
┃ ┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__Exhibit_H_Declaration.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜WZ9.00.050__index.html
┃ ┃ ┃ ┃ ┣ 📂04_filed_receipts
┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┃ ┣ 📜WZ9.00.050__index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜WZ9.00.050__Odyssey_Envelope_Receipt.pdf
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜WZ9.00.050__index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┣ 📜WZ9.00.050__index.html
┃ ┃ ┃ ┗ 📜WZ9.00.050__Motions.md
┃ ┃ ┣ 📜_README.md
┃ ┃ ┣ 📜index.html
┃ ┃ ┣ 📜WZ9.00.001_READY_FOR_BINDER.md
┃ ┃ ┣ 📜WZ9.00.002_REJECTED_FOR_COURT.md
┃ ┃ ┣ 📜WZ9.00.003_PROMOTION_LOG.md
┃ ┃ ┗ 📜WZ9.00.010_PROMOTION_CHECKLIST.md
┃ ┣ 📜_README.md
┃ ┣ 📜audit_fcfcu.py
┃ ┣ 📜Binder Covers.pdf
┃ ┣ 📜Contacts.md
┃ ┣ 📜create_masters.py
┃ ┣ 📜Exhibit X — Inventory of Jurisdictional, Execut.md
┃ ┣ 📜fix_court_binder.py
┃ ┣ 📜index.html
┃ ┣ 📜index.md
┃ ┣ 📜INTERNAL VALUATION MEMO.md
┃ ┣ 📜Master_Index.md
┃ ┣ 📜PROMOTION_CHECKLIST.md
┃ ┗ 📜Talking_Points.md
┣ 📂40_PRINT_READY_BINDERS
┃ ┣ 📂01_court_binder
┃ ┃ ┣ 📂fcfcu-49d03-2501-mf-002559
┃ ┃ ┃ ┣ 📂a_anchor_overview
┃ ┃ ┃ ┃ ┣ 📂a0_00_cover_index
┃ ┃ ┃ ┃ ┃ ┣ 📜a0.00.000_section_cover.html
┃ ┃ ┃ ┃ ┃ ┣ 📜a0.00.010_master_case_index.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂a0_01_overview
┃ ┃ ┃ ┃ ┃ ┣ 📜a0.01.001_one_page_case_summary.html
┃ ┃ ┃ ┃ ┃ ┣ 📜a0.01.002_hearing_scope_and_relief.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂b_basis_issue_and_law
┃ ┃ ┃ ┃ ┣ 📂b1_00_cover
┃ ┃ ┃ ┃ ┃ ┣ 📜b1.00.000_section_cover.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂b1_01_issue_law
┃ ┃ ┃ ┃ ┃ ┣ 📜b1.01.001_core_issue_statement.html
┃ ┃ ┃ ┃ ┃ ┣ 📜b1.01.002_trial_rule_4_1_b_standard.html
┃ ┃ ┃ ┃ ┃ ┣ 📜b1.01.003_void_vs_voidable_case_law.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂c_claims_and_motions
┃ ┃ ┃ ┃ ┣ 📂c2_01_motion_vacate
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.01.001_motion_to_vacate_void_judgment.html
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.01.002_motion_vacate.html
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.01.002_motion_vacate.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.01.003_exhibit_list.html
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.01.003_exhibit_list.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.01.004_exhibits_combined.html
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.01.004_exhibits_combined.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂c2_02_emergency_stay_quash
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.02.001_emergency_motion_stay_or_quash.html
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.02.002_emergency_motion_stay_or_quash.html
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.02.002_emergency_motion_stay_or_quash.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂c2_03_supplemental
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.03.001_supplemental_emergency_motion.html
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.03.002_supplemental_emergency_motion.html
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.03.002_supplemental_emergency_motion.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.03.003_exhibit_h_declaration.html
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.03.003_exhibit_h_declaration.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.03.004_odyssey_envelope_receipt.html
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.03.004_odyssey_envelope_receipt.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.03.005_combined_source.html
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.03.005_combined_source.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂c2_04_proposed_orders
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.04.001_order_vacate_proposed.html
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.04.001_order_vacate_proposed.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.04.001_proposed_order_vacate.html
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.04.002_order_stay_writ_proposed.html
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.04.002_order_stay_writ_proposed.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜c2.04.002_proposed_order_stay_writ.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂d_delivery_service
┃ ┃ ┃ ┃ ┣ 📂d3_00_cover
┃ ┃ ┃ ┃ ┃ ┣ 📜d3.00.000_section_cover.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂d3_01_summons
┃ ┃ ┃ ┃ ┃ ┣ 📜d3.01.001_summons_incomplete.html
┃ ┃ ┃ ┃ ┃ ┣ 📜d3.01.001_summons_incomplete.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂d3_02_sheriff_returns
┃ ┃ ┃ ┃ ┃ ┣ 📜d3.02.001_sheriff_return_2025-03-05.html
┃ ┃ ┃ ┃ ┃ ┣ 📜d3.02.001_sheriff_return_2025-03-05.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜d3.02.002_sheriff_return_2025-04-15.html
┃ ┃ ┃ ┃ ┃ ┣ 📜d3.02.002_sheriff_return_2025-04-15.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂d3_03_service_analysis
┃ ┃ ┃ ┃ ┃ ┣ 📜d3.03.001_service_defect_analysis.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂e_effects_procedural_chain
┃ ┃ ┃ ┃ ┣ 📂e4_00_cover
┃ ┃ ┃ ┃ ┃ ┣ 📜e4.00.000_section_cover.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂e4_01_default_judgment
┃ ┃ ┃ ┃ ┃ ┣ 📜e4.01.001_default_judgment_entry.html
┃ ┃ ┃ ┃ ┃ ┣ 📜e4.01.001_default_judgment_entry.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂e4_02_petition_for_writ
┃ ┃ ┃ ┃ ┃ ┣ 📜e4.02.001_petition_for_writ_of_assistance.html
┃ ┃ ┃ ┃ ┃ ┣ 📜e4.02.001_petition_for_writ_of_assistance.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂e4_03_writ_issued
┃ ┃ ┃ ┃ ┃ ┣ 📜e4.03.001_writ_of_assistance_issued.html
┃ ┃ ┃ ┃ ┃ ┣ 📜e4.03.001_writ_of_assistance_issued.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂e4_04_removal_enforcement
┃ ┃ ┃ ┃ ┃ ┣ 📜e4.04.001_removal_enforcement_record.html
┃ ┃ ┃ ┃ ┃ ┣ 📜e4.04.001_removal_enforcement_record.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂e4_05_chain_summary
┃ ┃ ┃ ┃ ┃ ┣ 📜e4.05.001_procedural_chain_summary.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂f_facts_declarations
┃ ┃ ┃ ┃ ┣ 📂f5_00_cover
┃ ┃ ┃ ┃ ┃ ┣ 📜f5.00.000_section_cover.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂f5_01_affidavit_not_served
┃ ┃ ┃ ┃ ┃ ┣ 📜f5.01.001_affidavit_not_served.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂f5_02_declaration_ongoing_harm
┃ ┃ ┃ ┃ ┃ ┣ 📜f5.02.001_declaration_ongoing_harm.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂f5_03_credibility_declaration
┃ ┃ ┃ ┃ ┃ ┣ 📜f5.03.001_credibility_declaration.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂g_grounds_ada
┃ ┃ ┃ ┃ ┣ 📂g6_00_cover
┃ ┃ ┃ ┃ ┃ ┣ 📜g6.00.000_section_cover.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂g6_01_ada_notice
┃ ┃ ┃ ┃ ┃ ┣ 📜g6.01.001_ada_notice.html
┃ ┃ ┃ ┃ ┃ ┣ 📜g6.01.001_ada_notice.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂g6_02_ada_supporting
┃ ┃ ┃ ┃ ┃ ┣ 📜g6.02.001_ada_supporting_documentation.html
┃ ┃ ┃ ┃ ┃ ┣ 📜g6.02.001_ada_supporting_documentation.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂g6_03_ada_impact_summary
┃ ┃ ┃ ┃ ┃ ┣ 📜g6.03.001_ada_impact_summary.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂h_hard_exhibits
┃ ┃ ┃ ┃ ┣ 📂h7_00_cover
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.00.000_section_cover.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂h7_01_exhibits_a-h
┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0001_exhibit_a_sheriff_return_2025-03-0.html
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0001_exhibit_a_sheriff_return_2025-03-05.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0001-0008_exhibits_combined.html
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0001-0008_exhibits_combined.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0002_exhibit_b_sheriff_return_2025-04-1.html
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0002_exhibit_b_sheriff_return_2025-04-15.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0003_exhibit_c_incomplete_summons.html
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0003_exhibit_c_incomplete_summons.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0004_exhibit_d_default_judgment_motion.html
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0004_exhibit_d_default_judgment_motion.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0005_exhibit_e_petition_for_writ.html
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0005_exhibit_e_petition_for_writ.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0006_exhibit_f_affidavit.html
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0006_exhibit_f_affidavit.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0007_exhibit_g1_ada_notice.html
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0007_exhibit_g1_ada_notice.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0008_exhibit_g2_aes_ada_documents.html
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0008_exhibit_g2_aes_ada_documents.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0009_exhibit_h_declaration_of_backgroun.html
┃ ┃ ┃ ┃ ┃ ┣ 📜h7.01.0009_exhibit_h_declaration_of_background.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂h7_02_exhibits_i_ada
┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂h7_03_exhibits_j_removal
┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂h7_04_exhibits_k_financial
┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂h7_05_exhibits_l_statements
┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂h7_06_exhibits_m_service
┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂h7_07_exhibits_p_property
┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂i_internal_reference
┃ ┃ ┃ ┃ ┣ 📂i8_00_cover
┃ ┃ ┃ ┃ ┃ ┣ 📜i8.00.000_section_cover.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂i8_01_full_docket
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_000_case_summary.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_000_full_docket.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_000_full_docket.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_001_complaint.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_001_complaint.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_002_appearance.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_002_appearance.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_003_request_for_admissions.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_003_request_for_admissions.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_004_notice_to_homeowners.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_004_notice_to_homeowners.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_005_appearance_2.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_005_appearance_2.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_006_summons_1.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_006_summons_1.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_007_summons_2.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_007_summons_2.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_008_summons_3.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_008_summons_3.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_009_summons_4.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_009_summons_4.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_010_summons_5.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_010_summons_5.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_011_service_returned_03-05-2025.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_011_service_returned_03-05-2025.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_012_service_returned_04-15-2025.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_012_service_returned_04-15-2025.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_013_motion_for_default_judgment.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_013_motion_for_default_judgment.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_014_affidavit.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_014_affidavit.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_015_affidavit_attorney_fees.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_015_affidavit_attorney_fees.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_016_affidavit_additional.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_016_affidavit_additional.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_017_order_denying_default_judgment.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_017_order_denying_default_judgment.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_018_omitted_notice_of_service.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_018_omitted_notice_of_service.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_019_amended_motion_default_judgment_1.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_019_amended_motion_default_judgment_1.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_020_amended_motion_default_judgment_2.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_020_amended_motion_default_judgment_2.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_021_praecipe_sheriff_sale_1.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_021_praecipe_sheriff_sale_1.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_022_praecipe_sheriff_sale_2.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_022_praecipe_sheriff_sale_2.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_023_decree_foreclosure_returned.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_023_decree_foreclosure_returned.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_024_petition_writ_of_assistance.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_024_petition_writ_of_assistance.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_025_motion_vacate_stay_writ.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_025_motion_vacate_stay_writ.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_026_exhibit_list_a-g.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_026_exhibit_list_a-g.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_027_supplemental_motion_access.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_027_supplemental_motion_access.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_028_report_court_defendant_request.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_028_report_court_defendant_request.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_029_emergency_supplemental_declaration.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_029_emergency_supplemental_declaration.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_030_report_sheriff_sale_no_excess.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_030_report_sheriff_sale_no_excess.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_031_proposed_order_vacate.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_031_proposed_order_vacate.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_032_proposed_order_stay.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_032_proposed_order_stay.pdf
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_033_ada_disability_affidavit.html
┃ ┃ ┃ ┃ ┃ ┣ 📜i8_01_033_ada_disability_affidavit.pdf
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂i8_02_research_notes
┃ ┃ ┃ ┃ ┃ ┣ 📜i8.02.001_research_and_notes.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📂i8_99_do_not_print
┃ ┃ ┃ ┃ ┃ ┣ 📜i8.99.999_internal_do_not_print.html
┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂j_exports
┃ ┃ ┃ ┃ ┣ 📜_readme.html
┃ ┃ ┃ ┃ ┣ 📜index.html
┃ ┃ ┃ ┃ ┗ 📜j9.00.00_section_cover.html
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┗ 📜index.html
┃ ┣ 📂01_COURT_BINDER
┃ ┃ ┣ 📂A_ANCHOR_OVERVIEW
┃ ┃ ┃ ┣ 📂A0_00_COVER_INDEX
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜A0.00.000_SECTION_COVER.md
┃ ┃ ┃ ┃ ┣ 📜A0.00.010_MASTER_CASE_INDEX.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂A0_01_OVERVIEW
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜A0.01.001_ONE_PAGE_CASE_SUMMARY.md
┃ ┃ ┃ ┃ ┣ 📜A0.01.002_HEARING_SCOPE_AND_RELIEF.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂B_BASIS_ISSUE_AND_LAW
┃ ┃ ┃ ┣ 📂B1_00_COVER
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜B1.00.000_SECTION_COVER.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂B1_01_ISSUE_LAW
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜B1.01.001_CORE_ISSUE_STATEMENT.md
┃ ┃ ┃ ┃ ┣ 📜B1.01.002_TRIAL_RULE_4_1_B_STANDARD.md
┃ ┃ ┃ ┃ ┣ 📜B1.01.003_VOID_VS_VOIDABLE_CASE_LAW.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂C_CLAIMS_AND_MOTIONS
┃ ┃ ┃ ┣ 📂C2_00_COVER
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜C2.00.000_SECTION_COVER.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂C2_01_MOTION_VACATE
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜C2.01.001_MOTION_TO_VACATE_VOID_JUDGMENT.md
┃ ┃ ┃ ┃ ┣ 📜C2.01.002_motion_vacate.pdf
┃ ┃ ┃ ┃ ┣ 📜C2.01.003_Exhibit_List.pdf
┃ ┃ ┃ ┃ ┣ 📜C2.01.004_Exhibits_Combined.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂C2_02_EMERGENCY_STAY_QUASH
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜C2.02.001_EMERGENCY_MOTION_STAY_OR_QUASH.md
┃ ┃ ┃ ┃ ┣ 📜C2.02.002_Emergency_Motion_Stay_OR_Quash.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂C2_03_SUPPLEMENTAL
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜C2.03.001_SUPPLEMENTAL_EMERGENCY_MOTION.md
┃ ┃ ┃ ┃ ┣ 📜C2.03.002_Supplemental_Emergency_Motion.pdf
┃ ┃ ┃ ┃ ┣ 📜C2.03.003_EXHIBIT_H_DECLARATION.pdf
┃ ┃ ┃ ┃ ┣ 📜C2.03.004_Odyssey_Envelope_Receipt.pdf
┃ ┃ ┃ ┃ ┣ 📜C2.03.005_COMBINED_SOURCE.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂C2_04_PROPOSED_ORDERS
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜C2.04.001_order_vacate_proposed.pdf
┃ ┃ ┃ ┃ ┣ 📜C2.04.001_PROPOSED_ORDER_VACATE.md
┃ ┃ ┃ ┃ ┣ 📜C2.04.002_order_stay_writ_proposed.pdf
┃ ┃ ┃ ┃ ┣ 📜C2.04.002_PROPOSED_ORDER_STAY_WRIT.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂D_DELIVERY_SERVICE
┃ ┃ ┃ ┣ 📂D3_00_COVER
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜D3.00.000_SECTION_COVER.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂D3_01_SUMMONS
┃ ┃ ┃ ┃ ┣ 📜D3.01.001_SUMMONS_INCOMPLETE.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂D3_02_SHERIFF_RETURNS
┃ ┃ ┃ ┃ ┣ 📜D3.02.001_SHERIFF_RETURN_2025-03-05.pdf
┃ ┃ ┃ ┃ ┣ 📜D3.02.002_SHERIFF_RETURN_2025-04-15.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂D3_03_SERVICE_ANALYSIS
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜D3.03.001_SERVICE_DEFECT_ANALYSIS.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂E_EFFECTS_PROCEDURAL_CHAIN
┃ ┃ ┃ ┣ 📂E4_00_COVER
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜E4.00.000_SECTION_COVER.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂E4_01_DEFAULT_JUDGMENT
┃ ┃ ┃ ┃ ┣ 📜E4.01.001_DEFAULT_JUDGMENT_ENTRY.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂E4_02_PETITION_FOR_WRIT
┃ ┃ ┃ ┃ ┣ 📜E4.02.001_PETITION_FOR_WRIT_OF_ASSISTANCE.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂E4_03_WRIT_ISSUED
┃ ┃ ┃ ┃ ┣ 📜E4.03.001_WRIT_OF_ASSISTANCE_ISSUED.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂E4_04_REMOVAL_ENFORCEMENT
┃ ┃ ┃ ┃ ┣ 📜E4.04.001_REMOVAL_ENFORCEMENT_RECORD.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂E4_05_CHAIN_SUMMARY
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜E4.05.001_PROCEDURAL_CHAIN_SUMMARY.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂F_FACTS_DECLARATIONS
┃ ┃ ┃ ┣ 📂F5_00_COVER
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜F5.00.000_SECTION_COVER.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂F5_01_AFFIDAVIT_NOT_SERVED
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜F5.01.001_AFFIDAVIT_NOT_SERVED.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂F5_02_DECLARATION_ONGOING_HARM
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜F5.02.001_DECLARATION_ONGOING_HARM.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂F5_03_CREDIBILITY_DECLARATION
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜F5.03.001_CREDIBILITY_DECLARATION.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂G_GROUNDS_ADA
┃ ┃ ┃ ┣ 📂G6_00_COVER
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜G6.00.000_SECTION_COVER.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂G6_01_ADA_NOTICE
┃ ┃ ┃ ┃ ┣ 📜G6.01.001_ADA_NOTICE.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂G6_02_ADA_SUPPORTING
┃ ┃ ┃ ┃ ┣ 📜G6.02.001_ADA_SUPPORTING_DOCUMENTATION.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂G6_03_ADA_IMPACT_SUMMARY
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜G6.03.001_ADA_IMPACT_SUMMARY.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂H_HARD_EXHIBITS
┃ ┃ ┃ ┣ 📂H7_00_COVER
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜H7.00.000_SECTION_COVER.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂H7_01_EXHIBITS_A-H
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜H7.01.0001_EXHIBIT_A_SHERIFF_RETURN_2025-03-05.pdf
┃ ┃ ┃ ┃ ┣ 📜H7.01.0001-0008_EXHIBITS_COMBINED.pdf
┃ ┃ ┃ ┃ ┣ 📜H7.01.0002_EXHIBIT_B_SHERIFF_RETURN_2025-04-15.pdf
┃ ┃ ┃ ┃ ┣ 📜H7.01.0003_EXHIBIT_C_INCOMPLETE_SUMMONS.pdf
┃ ┃ ┃ ┃ ┣ 📜H7.01.0004_EXHIBIT_D_DEFAULT_JUDGMENT_MOTION.pdf
┃ ┃ ┃ ┃ ┣ 📜H7.01.0005_EXHIBIT_E_PETITION_FOR_WRIT.pdf
┃ ┃ ┃ ┃ ┣ 📜H7.01.0006_EXHIBIT_F_AFFIDAVIT.pdf
┃ ┃ ┃ ┃ ┣ 📜H7.01.0007_EXHIBIT_G1_ADA_NOTICE.pdf
┃ ┃ ┃ ┃ ┣ 📜H7.01.0008_EXHIBIT_G2_AES_ADA_DOCUMENTS.pdf
┃ ┃ ┃ ┃ ┣ 📜H7.01.0009_EXHIBIT_H_DECLARATION_OF_BACKGROUND.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂H7_02_EXHIBITS_I_ADA
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂H7_03_EXHIBITS_J_REMOVAL
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂H7_04_EXHIBITS_K_FINANCIAL
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂H7_05_EXHIBITS_L_STATEMENTS
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂H7_06_EXHIBITS_M_SERVICE
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂H7_07_EXHIBITS_P_PROPERTY
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┣ 📂I_INTERNAL_REFERENCE
┃ ┃ ┃ ┣ 📂I8_00_COVER
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜I8.00.000_SECTION_COVER.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂I8_01_FULL_DOCKET
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜I8_01_000_CASE_SUMMARY.md
┃ ┃ ┃ ┃ ┣ 📜I8_01_000_FULL_DOCKET.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_001_Complaint.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_002_Appearance.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_003_Request_for_Admissions.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_004_Notice_to_Homeowners.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_005_Appearance_2.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_006_Summons_1.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_007_Summons_2.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_008_Summons_3.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_009_Summons_4.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_010_Summons_5.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_011_Service_Returned_03-05-2025.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_012_Service_Returned_04-15-2025.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_013_Motion_for_Default_Judgment.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_014_Affidavit.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_015_Affidavit_Attorney_Fees.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_016_Affidavit_Additional.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_017_Order_Denying_Default_Judgment.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_018_Omitted_Notice_of_Service.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_019_Amended_Motion_Default_Judgment_1.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_020_Amended_Motion_Default_Judgment_2.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_021_Praecipe_Sheriff_Sale_1.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_022_Praecipe_Sheriff_Sale_2.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_023_Decree_Foreclosure_Returned.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_024_Petition_Writ_of_Assistance.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_025_Motion_Vacate_Stay_Writ.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_026_Exhibit_List_A-G.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_027_Supplemental_Motion_Access.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_028_Report_Court_Defendant_Request.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_029_Emergency_Supplemental_Declaration.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_030_Report_Sheriff_Sale_No_Excess.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_031_Proposed_Order_Vacate.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_032_Proposed_Order_Stay.pdf
┃ ┃ ┃ ┃ ┣ 📜I8_01_033_ADA_Disability_Affidavit.pdf
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂I8_02_RESEARCH_NOTES
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜I8.02.001_RESEARCH_AND_NOTES.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📂I8_99_DO_NOT_PRINT
┃ ┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┃ ┣ 📜I8.99.999_INTERNAL_DO_NOT_PRINT.md
┃ ┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┃ ┣ 📜_README.md
┃ ┃ ┃ ┗ 📜index.html
┃ ┃ ┗ 📜index.html
┃ ┣ 📜_COURT_MODE_BUTTONS.md
┃ ┣ 📜_COURT_MODE_BUTTONS.md.md
┃ ┣ 📜_COURT_MODE_PLAYBOOK.md.md
┃ ┣ 📜00A_Cover_Court.html
┃ ┣ 📜00A_Cover_Opposing.html
┃ ┣ 📜00A_Cover.html
┃ ┣ 📜00B_Spine.html
┃ ┣ 📜00C_Table_of_Contents.md
┃ ┣ 📜01A_TAB_01_MOTION.md
┃ ┣ 📜01B_Motion_To_Vacate_Void_Judgment.pdf
┃ ┣ 📜02A_TAB_02_EXHIBITS.md
┃ ┣ 📜02B_Exhibits_Index.md
┃ ┣ 📜02C_Exhibits.pdf
┃ ┣ 📜BINDER_1_USER_COPY_PRINT_ME.pdf
┃ ┣ 📜BINDER_2_JUDGE_COPY_PRINT_ME.pdf
┃ ┣ 📜BINDER_3_OPPOSING_COPY_PRINT_ME.pdf
┃ ┣ 📜COMPLETE_COURT_BINDER_PRINT_ME.pdf
┃ ┗ 📜index.html
┗ 📂90_OUTPUTS_EXPORTS
  ┣ 📂02_war_room
  ┃ ┣ 📂wa_anchor_overview
  ┃ ┃ ┣ 📂wa0_00_command_map
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┗ 📜wa0.00.01_command_map.html
  ┃ ┃ ┣ 📂wa0_01_hearing_planning
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wa0.01.001_hearing_goals.html
  ┃ ┃ ┃ ┣ 📜wa0.01.002_talking_points.html
  ┃ ┃ ┃ ┗ 📜wa0.01.003_judge_questions_predicted.html
  ┃ ┃ ┣ 📂wa0.00.001_timeline
  ┃ ┃ ┃ ┣ 📂30_2025
  ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-01-16_case_filed.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-03-05_service_attempt_1.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-04-15_service_attempt_2.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-05-13_motion_for_default_jud.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-05-21_order_denying_default_.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-05-23_amended_motion_default.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-05-28_default_judgment_enter.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-05-30_praecipe_sheriff_sale.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-07-09_sheriff_sale_notice_po.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-08-15_sheriff_sale.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-10-29_petition_for_writ_of_a.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-11-06_writ_of_assistance_iss.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-12-09_writ_executed_removal.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-12-10_motions_filed.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-12-11_court_orders_and_heari.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__2025-12-12_supplemental_emergency.html
  ┃ ┃ ┃ ┃ ┣ 📜wa0.00.030__index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜wa0.00.030__index.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wa0.00.030__index.html
  ┃ ┃ ┃ ┣ 📜wa0.00.030__timeline_canvas.html
  ┃ ┃ ┃ ┗ 📜wa0.00.060__master_timeline.html
  ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┣ 📜wa0.00.000_war_room_overview.html
  ┃ ┃ ┣ 📜wa0.00.010_active_strategies.html
  ┃ ┃ ┗ 📜wa0.00.020_promotion_candidates.html
  ┃ ┣ 📂wb_basis_issue_and_law
  ┃ ┃ ┣ 📂wb1_00_law_research
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wb1.00.001_case_law_research.html
  ┃ ┃ ┃ ┣ 📜wb1.00.002_void_vs_voidable_analysis.html
  ┃ ┃ ┃ ┗ 📜wb1.00.003_jurisdiction_theory.html
  ┃ ┃ ┣ 📂wb1_01_alternate_theories
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wb1.01.001_backup_arguments.html
  ┃ ┃ ┃ ┗ 📜wb1.01.002_if_judge_pushback.html
  ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┗ 📜index.html
  ┃ ┣ 📂wc_claims_and_motions
  ┃ ┃ ┣ 📂wc2_00_draft_motions
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wc2.00.001_draft_motion_vacate.html
  ┃ ┃ ┃ ┣ 📜wc2.00.002_draft_emergency_stay.html
  ┃ ┃ ┃ ┣ 📜wc2.00.003_draft_supplemental.html
  ┃ ┃ ┃ ┣ 📜wc2.00.010___motions.html
  ┃ ┃ ┃ ┣ 📜wc2.00.010__motion_emergency_stay_of_writ.docx
  ┃ ┃ ┃ ┣ 📜wc2.00.010__motion_emergency_stay_of_writ.html
  ┃ ┃ ┃ ┣ 📜wc2.00.010__motion_emergency_supplemental_mot.docx
  ┃ ┃ ┃ ┣ 📜wc2.00.010__motion_emergency_supplemental_mot.html
  ┃ ┃ ┃ ┣ 📜wc2.00.010__motion_to_vacate_void_judgement.docx
  ┃ ┃ ┃ ┗ 📜wc2.00.010__motion_to_vacate_void_judgment.html
  ┃ ┃ ┣ 📂wc2_01_proposed_orders
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wc2.01.001_draft_order_vacate.html
  ┃ ┃ ┃ ┣ 📜wc2.01.002_draft_order_stay.html
  ┃ ┃ ┃ ┣ 📜wc2.01.010__index-content.html
  ┃ ┃ ┃ ┣ 📜wc2.01.010__index.html
  ┃ ┃ ┃ ┣ 📜wc2.01.010__proposed_order_emergency_stay.html
  ┃ ┃ ┃ ┣ 📜wc2.01.010__proposed_order_motion_to_vacate.html
  ┃ ┃ ┃ ┗ 📜wc2.01.010__proposed_orders.html
  ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┗ 📜index.html
  ┃ ┣ 📂wd_delivery_service
  ┃ ┃ ┣ 📂wd3_00_service_tracking
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wd3.00.001_service_matrix.html
  ┃ ┃ ┃ ┗ 📜wd3.00.002_service_failure_analysis.html
  ┃ ┃ ┣ 📂wd3_01_service_evidence
  ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wd3.01.001_summons_source.html
  ┃ ┃ ┃ ┣ 📜wd3.01.001_summons_source.pdf
  ┃ ┃ ┃ ┗ 📜wd3.01.002_sheriff_metadata.html
  ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┗ 📜index.html
  ┃ ┣ 📂we_effects_procedural_chain
  ┃ ┃ ┣ 📂we4_00_chain_analysis
  ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜we4.00.001_procedural_failure_map.html
  ┃ ┃ ┃ ┣ 📜we4.00.002_but_for_analysis.html
  ┃ ┃ ┃ ┣ 📜we4.00.010__integrate_disability_separate_appe.m4a
  ┃ ┃ ┃ ┣ 📜we4.00.010__void_judgment_eviction_crisis.html
  ┃ ┃ ┃ ┗ 📜we4.00.010__void_judgment_eviction_crisis.pdf
  ┃ ┃ ┣ 📂we4_01_remedies
  ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜we4.01.001_stay_paths.html
  ┃ ┃ ┃ ┗ 📜we4.01.002_reversal_paths.html
  ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┗ 📜index.html
  ┃ ┣ 📂wf_facts_declarations
  ┃ ┃ ┣ 📂wf5_00_fact_development
  ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wf5.00.001_fact_timeline.html
  ┃ ┃ ┃ ┗ 📜wf5.00.002_fact_gaps.html
  ┃ ┃ ┣ 📂wf5_01_draft_declarations
  ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wf5.01.001_draft_affidavit.html
  ┃ ┃ ┃ ┣ 📜wf5.01.002_draft_declaration.html
  ┃ ┃ ┃ ┣ 📜wf5.01.010___declarations.html
  ┃ ┃ ┃ ┣ 📜wf5.01.010___instructions_for_witnesses.html
  ┃ ┃ ┃ ┣ 📜wf5.01.010__ada_disability_affidavit.html
  ┃ ┃ ┃ ┣ 📜wf5.01.010__affidavit_not_served.docx
  ┃ ┃ ┃ ┣ 📜wf5.01.010__affidavit_not_served.html
  ┃ ┃ ┃ ┣ 📜wf5.01.010__character_affidavit.html
  ┃ ┃ ┃ ┣ 📜wf5.01.010__community_service_affidavit.html
  ┃ ┃ ┃ ┣ 📜wf5.01.010__credibility_affidavit.html
  ┃ ┃ ┃ ┣ 📜wf5.01.010__gender_identity_clarification.html
  ┃ ┃ ┃ ┣ 📜wf5.01.010__index-1.html
  ┃ ┃ ┃ ┣ 📜wf5.01.010__index-content.html
  ┃ ┃ ┃ ┣ 📜wf5.01.010__index.html
  ┃ ┃ ┃ ┣ 📜wf5.01.010__observations_affidavit.html
  ┃ ┃ ┃ ┗ 📜wf5.01.010__verified_affidavit_of_defendant.html
  ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┗ 📜index.html
  ┃ ┣ 📂wg_grounds_ada
  ┃ ┃ ┣ 📂wg6_00_ada_strategy
  ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wg6.00.001_ada_title_ii_analysis.html
  ┃ ┃ ┃ ┗ 📜wg6.00.002_reasonable_accommodations.html
  ┃ ┃ ┣ 📂wg6_01_parallel_enforcement
  ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wg6.01.001_doj_complaint.html
  ┃ ┃ ┃ ┣ 📜wg6.01.002_icrc_complaint.html
  ┃ ┃ ┃ ┗ 📜wg6.01.003_status_tracker.html
  ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┗ 📜index.html
  ┃ ┣ 📂wh_hard_evidence
  ┃ ┃ ┣ 📂wh7_00_raw_intake
  ┃ ┃ ┃ ┣ 📂10_photos_video
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_00241326_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_00241326_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_012aa06e_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_012aa06e_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_01b3e905_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_01b3e905_2025-1.png
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_10f4975d_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_10f4975d_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_1a80b987_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_1a80b987_2025-1.mp4
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_1beefb11_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_1beefb11_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_1f3f8a81_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_1f3f8a81_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_25fb1992_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_25fb1992_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_2f0952db_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_2f0952db_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_49c74ec6_2025-.heic
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_4e01fa01_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_4e01fa01_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_5be451ba_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_5be451ba_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_5d95cae5_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_5d95cae5_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_61129253_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_61129253_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_63fb7b02_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_63fb7b02_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_71c9e6a7_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_71c9e6a7_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_78ba1ccc_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_78ba1ccc_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_7a544ef7_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_7a544ef7_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_8350e7be_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_8350e7be_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_8a163413_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_8a163413_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_8d885a5c_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_8d885a5c_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_942cfd7f_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_942cfd7f_2025-1.png
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_9b611100_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_9b611100_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_9fb3a08a_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_9fb3a08a_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_9ff5022d_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_9ff5022d_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_a8832e17_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_a8832e17_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_ca02d006_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_ca02d006_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_db9b10b5_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_db9b10b5_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_e4cb3622_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_e4cb3622_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_ebaaa38d_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_ebaaa38d_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_ed6dc885_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_ed6dc885_2025-1.mp4
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_f510498b_2025-.heic
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_f60d8098_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_f60d8098_2025-1.png
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_f98b089a_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_f98b089a_2025-1.png
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_fa1703bf_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_fa1703bf_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_fdd8d4ef_2025-.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-10_photos_video_fdd8d4ef_2025-1.jpg
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📂10_supporting
  ┃ ┃ ┃ ┃ ┣ 📂10_photos_video
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video__1.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video__2.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_00.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_002.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_01.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_012.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_01b.png
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_10.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_10f.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_1a.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_1a8.mp4
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_1b.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_1be.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_1f.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_1f3.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_25.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_25f.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_2f.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_2f0.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_49.heic
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_4e.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_4e0.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_5b.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_5be.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_5d.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_5d9.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_61.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_611.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_63.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_63f.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_71.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_71c.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_78.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_78b.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_7a.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_7a5.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_83.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_835.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_8a.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_8a1.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_8d.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_8d8.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_94.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_942.png
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_9b.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_9b6.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_9f.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_9fb.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_9ff.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_a8.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_a88.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_ca.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_ca0.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_db.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_db9.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_e4.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_e4c.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_eb.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_eba.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_ed.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_ed6.mp4
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_f5.heic
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_f6.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_f60.png
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_f9.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_f98.png
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_fa.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_fa1.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_fd.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-10_photos_video_fdd.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┃ ┣ 📂20_receipts
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-20_receipts_0860d3.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-20_receipts_0860d3d.jpg
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┃ ┣ 📂30_declarations
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┃ ┣ 📂40_affidavits
  ┃ ┃ ┃ ┃ ┃ ┣ 📂ada-disability
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📂character
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📂community-service
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📂credibility
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📂observations
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┣ 📂20_property
  ┃ ┃ ┃ ┃ ┣ 📂10_mortgage_history
  ┃ ┃ ┃ ┃ ┃ ┣ 📂20_payments
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-20_payments_c5131d.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-20_payments_c5131de.png
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┃ ┣ 📂20_parcel
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__parcel_6016506_parceldetailhistor.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__parcel_6016506_parceldetailhistory.pdf
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__parcel_6016506_prc.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__parcel_6016506_prc.pdf
  ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┣ 📂20_property-1
  ┃ ┃ ┃ ┃ ┣ 📂10_mortgage_history
  ┃ ┃ ┃ ┃ ┃ ┣ 📂20_payments
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-20_payments_c5131deb_2025-12-2.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-20_payments_c5131deb_2025-12-20.png
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📂20_parcel
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜parcel_6016506_parceldetailhistory.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜parcel_6016506_parceldetailhistory.pdf
  ┃ ┃ ┃ ┃ ┃ ┣ 📜parcel_6016506_prc.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜parcel_6016506_prc.pdf
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📂20_receipts
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-20_receipts_0860d3df_2025-12-2.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-20_receipts_0860d3df_2025-12-20.jpg
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📂30_declarations
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📂30_fcfcu
  ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┣ 📜2023-09-20_fcfcu_hardship_and_health_notice_1.html
  ┃ ┃ ┃ ┃ ┣ 📜2023-09-20_fcfcu_hardship_and_health_notice_l.html
  ┃ ┃ ┃ ┃ ┣ 📜2023-09-20_fcfcu_hardship_and_health_notice_le.pdf
  ┃ ┃ ┃ ┃ ┣ 📜2023-09-20_notice_disabilities_hardship.html
  ┃ ┃ ┃ ┃ ┣ 📜2023-09-20_notice_disabilities_hardship.pdf
  ┃ ┃ ┃ ┃ ┣ 📜2024-03-20_fcfcu_certified_response_tax_recor.html
  ┃ ┃ ┃ ┃ ┣ 📜2024-03-20_fcfcu_certified_response_tax_record.pdf
  ┃ ┃ ┃ ┃ ┣ 📜2024-12-09_outgoing_email_bank_access_request.html
  ┃ ┃ ┃ ┃ ┣ 📜2024-12-09_outgoing_email_bank_access_request.pdf
  ┃ ┃ ┃ ┃ ┣ 📜2024-12-11_outgoing_email_bank_access_request.html
  ┃ ┃ ┃ ┃ ┣ 📜2024-12-11_outgoing_email_bank_access_request.pdf
  ┃ ┃ ┃ ┃ ┣ 📜2024-20-03_response_to_tax_notice.html
  ┃ ┃ ┃ ┃ ┣ 📜2024-20-03_response_to_tax_notice.pdf
  ┃ ┃ ┃ ┃ ┣ 📜20241204_fcfcu_statement-(1).html
  ┃ ┃ ┃ ┃ ┣ 📜20241204_fcfcu_statement-(1).pdf
  ┃ ┃ ┃ ┃ ┣ 📜20241204_fcfcu_statement-(2).html
  ┃ ┃ ┃ ┃ ┣ 📜20241204_fcfcu_statement-(2).pdf
  ┃ ┃ ┃ ┃ ┣ 📜20241204_fcfcu_statement.html
  ┃ ┃ ┃ ┃ ┣ 📜20241204_fcfcu_statement.pdf
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-30_fcfcu_740eacdc_2025-12-20_e.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-30_fcfcu_740eacdc_2025-12-20_ex.jpg
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-30_fcfcu_ac6eb2ea_2025-12-20_e.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-20_exh-30_fcfcu_ac6eb2ea_2025-12-20_ex.jpg
  ┃ ┃ ┃ ┃ ┣ 📜21june-24-4817shadow_appraisal.html
  ┃ ┃ ┃ ┃ ┣ 📜21june-24-4817shadow_appraisal.pdf
  ┃ ┃ ┃ ┃ ┣ 📜fcfcu_v_cr-v_report_to_court.html
  ┃ ┃ ┃ ┃ ┣ 📜fcfcu_v_cr-v_report_to_court.pdf
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📜report_to_court_on_defendants_request.html
  ┃ ┃ ┃ ┃ ┗ 📜report_to_court_on_defendants_request.pdf
  ┃ ┃ ┃ ┣ 📂30_fcfcu-1
  ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2023-09-20_fcfcu_hardship_and_h_1.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2023-09-20_fcfcu_hardship_and_hea.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2023-09-20_fcfcu_hardship_and_heal.pdf
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2023-09-20_notice_disabilities_ha.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2023-09-20_notice_disabilities_har.pdf
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2024-03-20_fcfcu_certified_respon.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2024-03-20_fcfcu_certified_respons.pdf
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2024-12-09_outgoing_email_bank_ac.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2024-12-09_outgoing_email_bank_acc.pdf
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2024-12-11_outgoing_email_bank_ac.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2024-12-11_outgoing_email_bank_acc.pdf
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2024-20-03_response_to_tax_notice.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2024-20-03_response_to_tax_notice.pdf
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__20241204_fcfcu_statement-(1).html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__20241204_fcfcu_statement-(1).pdf
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__20241204_fcfcu_statement-(2).html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__20241204_fcfcu_statement-(2).pdf
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__20241204_fcfcu_statement.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__20241204_fcfcu_statement.pdf
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-30_fcfcu_740eacdc_.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-30_fcfcu_740eacdc_2.jpg
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-30_fcfcu_ac6eb2ea_.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-20_exh-30_fcfcu_ac6eb2ea_2.jpg
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__21june-24-4817shadow_appraisal.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__21june-24-4817shadow_appraisal.pdf
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__fcfcu_v_cr-v_report_to_court.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__fcfcu_v_cr-v_report_to_court.pdf
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__report_to_court_on_defendants_req.html
  ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__report_to_court_on_defendants_requ.pdf
  ┃ ┃ ┃ ┣ 📂40_affidavits
  ┃ ┃ ┃ ┃ ┣ 📂ada-disability
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📂character
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📂community-service
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📂credibility
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📂observations
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📂50_aes
  ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-06-08_aes_ada_notice.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-06-08_aes_ada_notice.pdf
  ┃ ┃ ┃ ┃ ┣ 📜2025-06-08_aes_ada_request_financial_hardship_.pdf
  ┃ ┃ ┃ ┃ ┣ 📜2025-06-08_aes_ada_request_financial_hardship.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-16_aes_emergency_notice.html
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📂50_aes-1
  ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-06-08_aes_ada_notice.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-06-08_aes_ada_notice.pdf
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-06-08_aes_ada_request_financ.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-06-08_aes_ada_request_financi.pdf
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__2025-12-16_aes_emergency_notice.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┣ 📂99__archive
  ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index-content.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.00.020__index.html
  ┃ ┃ ┃ ┃ ┗ 📜wh7.00.020__readme_supporting.html
  ┃ ┃ ┃ ┣ 📜_readme-1.html
  ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wh7.00.001_raw_phone_dump.html
  ┃ ┃ ┃ ┣ 📜wh7.00.002_raw_video_audio.html
  ┃ ┃ ┃ ┗ 📜wh7.00.003_raw_screenshots.html
  ┃ ┃ ┣ 📂wh7_01_potential_exhibits
  ┃ ┃ ┃ ┣ 📂10_exhibit_sets
  ┃ ┃ ┃ ┃ ┣ 📂_exhibit_a-h_initial
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__2025-12-10_mtv_exhibits_combined.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__2025-12-10_mtv_exhibits_combined.pdf
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_a_20250305_sheriff_retur.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_a_20250305_sheriff_return.pdf
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_b_20250415_sheriff_retur.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_b_20250415_sheriff_return.pdf
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_c_20250116_incomplete_su.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_c_20250116_incomplete_sum.pdf
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_d_20250513_default_judgm.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_d_20250513_default_judgme.pdf
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_e_20251029_petition_for_.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_e_20251029_petition_for_w.pdf
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_f_affidavit_cody_ricevel.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_f_affidavit_cody_ricevela.pdf
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_g1_ada_notice_request.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_g1_ada_notice_request.pdf
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_g2_aes_ada_docs_disconne.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_g2_aes_ada_docs_disconnec.pdf
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_h_declaration.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__exhibit_h_declaration.pdf
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.01.0100__index.html
  ┃ ┃ ┃ ┃ ┣ 📂exhibits_i_ada_communications
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.01.0100__index.html
  ┃ ┃ ┃ ┃ ┣ 📂exhibits_j_eviction_removal
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.01.0100__index.html
  ┃ ┃ ┃ ┃ ┣ 📂exhibits_k_financial
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.01.0100__index.html
  ┃ ┃ ┃ ┃ ┣ 📂exhibits_l_statements
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.01.0100__index.html
  ┃ ┃ ┃ ┃ ┣ 📂exhibits_m_court-service
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.01.0100__index.html
  ┃ ┃ ┃ ┃ ┣ 📂exhibits_p_property
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.01.0100__index.html
  ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100___checklist.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0100__index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜wh7.01.0100__index.html
  ┃ ┃ ┃ ┣ 📂30_exhibits
  ┃ ┃ ┃ ┃ ┣ 📂exhibits_templates
  ┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wh7.01.0050___exhibits_lists.html
  ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📜wh7.01.0050__exhibit_list.docx
  ┃ ┃ ┃ ┃ ┗ 📜wh7.01.0050__exhibit_list.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wh7.01.0001_potential_exhibit_0001.html
  ┃ ┃ ┃ ┣ 📜wh7.01.0001_potential_exhibit_0001.pdf
  ┃ ┃ ┃ ┣ 📜wh7.01.0002_potential_exhibit_0002.html
  ┃ ┃ ┃ ┗ 📜wh7.01.0002_potential_exhibit_0002.pdf
  ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┣ 📜evidence_log.html
  ┃ ┃ ┗ 📜index.html
  ┃ ┣ 📂wi_internal_reference
  ┃ ┃ ┣ 📂00_trackers
  ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜qicase-fcfcu_financial_tracker.xlsx
  ┃ ┃ ┃ ┗ 📜session_summary_2025-12-16_fcfcu_case_dna_str.html
  ┃ ┃ ┣ 📂05_timeline
  ┃ ┃ ┃ ┣ 📂30_2025
  ┃ ┃ ┃ ┃ ┣ 📜2025-01-16_case_filed.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-03-05_service_attempt_1.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-04-15_service_attempt_2.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-05-13_motion_for_default_judgment.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-05-21_order_denying_default_judgment.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-05-23_amended_motion_default_judgment.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-05-28_default_judgment_entered.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-05-30_praecipe_sheriff_sale.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-07-09_sheriff_sale_notice_posted.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-08-15_sheriff_sale.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-10-29_petition_for_writ_of_assistance.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-11-06_writ_of_assistance_issued.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-09_writ_executed_removal.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-11_court_orders_and_hearing_scheduled.html
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-12_supplemental_emergency_motion.html
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┗ 📜timeline_canvas.html
  ┃ ┃ ┣ 📂10_overviews
  ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜integrate_disability_separate_appeals_get_stay.m4a
  ┃ ┃ ┃ ┣ 📜procedural_failure_map_one_pager.html
  ┃ ┃ ┃ ┣ 📜void_judgment_eviction_crisis.html
  ┃ ┃ ┃ ┗ 📜void_judgment_eviction_crisis.pdf
  ┃ ┃ ┣ 📂20_strategy
  ┃ ┃ ┃ ┣ 📂10_ada_title_ii
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📂20_jurisdiction_service_tr_4_1_b
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📂30_void_vs_voidable_tr_60b
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┗ 📜strategic_plan.html
  ┃ ┃ ┣ 📂personal_narrative
  ┃ ┃ ┃ ┣ 📂01_public_narrative
  ┃ ┃ ┃ ┃ ┣ 📜2025-12-15_they_threw_us_into_the_cold.html
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┗ 📜public_statement.html
  ┃ ┃ ┃ ┣ 📂02_exposure_and_harm
  ┃ ┃ ┃ ┃ ┣ 📂photos_conditions
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📂weather_reports
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📜cold_risk_report.html
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📂03_internal_analysis
  ┃ ┃ ┃ ┃ ┣ 📂payout_strategy
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜long_term_payout_strategy.html
  ┃ ┃ ┃ ┃ ┣ 📂premonitions
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜premonitions_i_knew_before_i_knew.html
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┗ 📜session_summary_2025-12-15_i_knew_before_i_kn.html
  ┃ ┃ ┃ ┣ 📂04_donations_and_support
  ┃ ┃ ┃ ┃ ┣ 📂donation_page_html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📂screenshots_live_page
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┃ ┣ 📜donations_context.html
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📂05_timeline
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┗ 📜master_timeline.html
  ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┣ 📂wi8_00_docket_record
  ┃ ┃ ┃ ┣ 📂legacy
  ┃ ┃ ┃ ┃ ┣ 📂30_court_record
  ┃ ┃ ┃ ┃ ┃ ┣ 📂10_docket
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001___case_summary.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__001_complaint.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__001_complaint.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__002_appearance.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__002_appearance.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__003_request_for_admissions.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__003_request_for_admissions.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__004_notice_to_homeowners.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__004_notice_to_homeowners.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__005_appearance_2.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__005_appearance_2.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__006_summons_1.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__006_summons_1.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__007_summons_2.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__007_summons_2.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__008_summons_3.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__008_summons_3.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__009_summons_4.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__009_summons_4.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__010_summons_5.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__010_summons_5.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__011_service_returned_03-05-2025.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__011_service_returned_03-05-2025.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__012_service_returned_04-15-2025.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__012_service_returned_04-15-2025.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__013_motion_for_default_judgment.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__013_motion_for_default_judgment.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__014_affidavit.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__014_affidavit.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__015_affidavit_attorney_fees.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__015_affidavit_attorney_fees.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__016_affidavit_additional.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__016_affidavit_additional.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__017_order_denying_default_judgmen.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__017_order_denying_default_judgment.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__018_omitted_notice_of_service.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__018_omitted_notice_of_service.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__019_amended_motion_default_judgme.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__019_amended_motion_default_judgmen.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__020_amended_motion_default_judgme.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__020_amended_motion_default_judgmen.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__021_praecipe_sheriff_sale_1.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__021_praecipe_sheriff_sale_1.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__022_praecipe_sheriff_sale_2.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__022_praecipe_sheriff_sale_2.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__023_decree_foreclosure_returned.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__023_decree_foreclosure_returned.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__024_petition_writ_of_assistance.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__024_petition_writ_of_assistance.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__025_motion_vacate_stay_writ.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__025_motion_vacate_stay_writ.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__026_exhibit_list_a-g.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__026_exhibit_list_a-g.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__027_supplemental_motion_access.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__027_supplemental_motion_access.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__028_report_court_defendant_reques.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__028_report_court_defendant_request.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__029_emergency_supplemental_declar.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__029_emergency_supplemental_declara.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__030_report_sheriff_sale_no_excess.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__030_report_sheriff_sale_no_excess.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__031_proposed_order_vacate.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__031_proposed_order_vacate.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__032_proposed_order_stay.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__032_proposed_order_stay.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__033_ada_disability_affidavit.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__033_ada_disability_affidavit.pdf
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.00.001__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wi8.00.001__index.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wi8.00.001_full_docket.html
  ┃ ┃ ┃ ┣ 📜wi8.00.001_full_docket.pdf
  ┃ ┃ ┃ ┗ 📜wi8.00.002_docket_notes.html
  ┃ ┃ ┣ 📂wi8_01_public_advocacy
  ┃ ┃ ┃ ┣ 📂al_narrative
  ┃ ┃ ┃ ┃ ┣ 📂01_public_narrative
  ┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.01.010__2025-12-15_they_threw_us_into_the.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.01.010__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.01.010__index.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wi8.01.010__public_statement.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📂rrative
  ┃ ┃ ┃ ┃ ┣ 📂04_donations_and_support
  ┃ ┃ ┃ ┃ ┃ ┣ 📂donation_page_html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.01.050__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wi8.01.050__index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📂screenshots_live_page
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.01.050__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wi8.01.050__index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.01.050__donations_context.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.01.050__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wi8.01.050__index.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wi8.01.001_press_strategy.html
  ┃ ┃ ┃ ┣ 📜wi8.01.002_social_media_plan.html
  ┃ ┃ ┃ ┗ 📜wi8.01.003_timing_and_risk.html
  ┃ ┃ ┣ 📂wi8_02_damages_and_settlement
  ┃ ┃ ┃ ┣ 📂l_narrative
  ┃ ┃ ┃ ┃ ┣ 📂02_exposure_and_harm
  ┃ ┃ ┃ ┃ ┃ ┣ 📂photos_conditions
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.050__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wi8.02.050__index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📂weather_reports
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.050__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wi8.02.050__index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.050__cold_risk_report.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.050__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wi8.02.050__index.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📂on
  ┃ ┃ ┃ ┃ ┣ 📂__legacy
  ┃ ┃ ┃ ┃ ┃ ┣ 📂00_admin
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂00_trackers
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.010__03_case_log_entry_2025-12-15.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.010__2024-12-09_eviction_case_masterfi.docx
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.010__2025-12-16_case_log_entry.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.010__2025-12-16_case_summary.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.010__case_conversation_log.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.010__case_conversation_log.txt
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.010__case_log.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.010__expenses.csv
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.010__financial_tracker.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.010__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.010__index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.010__qicase-fcfcu_financial_tracker.xlsx
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.02.010__session_summary_2025-12-16_fcfc_1.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wi8.02.010__session_summary_2025-12-16_fcfcu_.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜wi8.02.001_economic_harm.html
  ┃ ┃ ┃ ┣ 📜wi8.02.002_non_economic_harm.html
  ┃ ┃ ┃ ┗ 📜wi8.02.003_settlement_scenarios.html
  ┃ ┃ ┣ 📂wi8_99_internal_only
  ┃ ┃ ┃ ┣ 📂l_narrative
  ┃ ┃ ┃ ┃ ┣ 📂03_internal_analysis
  ┃ ┃ ┃ ┃ ┃ ┣ 📂payout_strategy
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.99.010__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.99.010__index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wi8.99.010__long_term_payout_strategy.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📂premonitions
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.99.010__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.99.010__index.html
  ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜wi8.99.010__premonitions_i_knew_before_i_knew.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.99.010__index-content.html
  ┃ ┃ ┃ ┃ ┃ ┣ 📜wi8.99.010__index.html
  ┃ ┃ ┃ ┃ ┃ ┗ 📜wi8.99.010__session_summary_2025-12-15_i_knew.html
  ┃ ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┣ 📜03_case_log_entry_2025-12-15.html
  ┃ ┃ ┣ 📜2024-12-09_eviction_case_masterfile.docx
  ┃ ┃ ┣ 📜2025-12-16_case_log_entry.html
  ┃ ┃ ┣ 📜2025-12-16_case_summary.html
  ┃ ┃ ┣ 📜case_conversation_log.html
  ┃ ┃ ┣ 📜case_conversation_log.txt
  ┃ ┃ ┣ 📜case-narrative-wrongful-foreclosure-and-displ.html
  ┃ ┃ ┣ 📜combinepdf.html
  ┃ ┃ ┣ 📜combinepdf.pdf
  ┃ ┃ ┣ 📜contacts.html
  ┃ ┃ ┣ 📜crisis_the_anatomy_of_institutional_failure.html
  ┃ ┃ ┣ 📜crisis_the_anatomy_of_institutional_failure.pdf
  ┃ ┃ ┣ 📜debate.m4a
  ┃ ┃ ┣ 📜expenses.csv
  ┃ ┃ ┣ 📜foreclosure_void_judgment_institutional_failur.m4a
  ┃ ┃ ┣ 📜foreclosure_void_versus_damages_due_process.m4a
  ┃ ┃ ┣ 📜foreclosure-and-housing-litigation-case-record.csv
  ┃ ┃ ┣ 📜forensic_audit_of_a_void_foreclosure.m4a
  ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┣ 📜inventory-of-civil-and-fair-housing-rights-vio.csv
  ┃ ┃ ┣ 📜legal-memorandum.html
  ┃ ┃ ┣ 📜odyssey_envelope_receipt.html
  ┃ ┃ ┣ 📜odyssey_envelope_receipt.pdf
  ┃ ┃ ┣ 📜proposal-for-strategic-reports-in-the-matter-.html
  ┃ ┃ ┣ 📜talking_points.html
  ┃ ┃ ┣ 📜wrongful_foreclosure_a_case_study_in_civil_ri.html
  ┃ ┃ ┗ 📜wrongful_foreclosure_a_case_study_in_civil_rig.pdf
  ┃ ┣ 📂wz_promotion_pipeline
  ┃ ┃ ┣ 📂wz9_00_050_filings_intake
  ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┣ 📜wz9.00.001_ready_for_binder.html
  ┃ ┃ ┣ 📜wz9.00.002_rejected_for_court.html
  ┃ ┃ ┣ 📜wz9.00.003_promotion_log.html
  ┃ ┃ ┗ 📜wz9.00.010_promotion_checklist.html
  ┃ ┗ 📜index.html
  ┣ 📂03_drafts_templates
  ┃ ┣ 📂dc_claims_and_motions
  ┃ ┃ ┣ 📂50_proposed_orders
  ┃ ┃ ┃ ┣ 📂proposed_templates
  ┃ ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┃ ┗ 📜proposed_orders.html
  ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┣ 📜proposed_order_emergency_stay.html
  ┃ ┃ ┃ ┗ 📜proposed_order_motion_to_vacate.html
  ┃ ┃ ┣ 📂motions_templates
  ┃ ┃ ┃ ┣ 📜_motions.html
  ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┣ 📜emergency_filing_packet.html
  ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┣ 📜motion_emergency_stay_of_writ.docx
  ┃ ┃ ┣ 📜motion_emergency_stay_of_writ.html
  ┃ ┃ ┣ 📜motion_emergency_supplemental_motion_ongoing_.docx
  ┃ ┃ ┣ 📜motion_emergency_supplemental_motion_ongoing_.html
  ┃ ┃ ┣ 📜motion_to_vacate_void_judgement.docx
  ┃ ┃ ┣ 📜motion_to_vacate_void_judgment.html
  ┃ ┃ ┗ 📜proposed_order_vacate.docx
  ┃ ┣ 📂df_facts_declarations
  ┃ ┃ ┣ 📂affidavits_templates
  ┃ ┃ ┃ ┣ 📜_instructions_for_witnesses.html
  ┃ ┃ ┃ ┣ 📜ada_disability_affidavit.html
  ┃ ┃ ┃ ┣ 📜character_affidavit.html
  ┃ ┃ ┃ ┣ 📜community_service_affidavit.html
  ┃ ┃ ┃ ┣ 📜credibility_affidavit.html
  ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┃ ┗ 📜observations_affidavit.html
  ┃ ┃ ┣ 📂declarations_templates
  ┃ ┃ ┃ ┣ 📜_declarations.html
  ┃ ┃ ┃ ┣ 📜gender_identity_clarification.html
  ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┣ 📜affidavit_not_served.docx
  ┃ ┃ ┣ 📜affidavit_not_served.html
  ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┣ 📜updated_affidavit_language.html
  ┃ ┃ ┗ 📜verified_affidavit_of_defendant.html
  ┃ ┣ 📂dh_hard_exhibits
  ┃ ┃ ┣ 📂exhibits_templates
  ┃ ┃ ┃ ┣ 📜_exhibits_lists.html
  ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┣ 📜exhibit_list.docx
  ┃ ┃ ┣ 📜exhibit_list.html
  ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┗ 📜template_exhibit_label.html
  ┃ ┣ 📂di_internal_reference
  ┃ ┃ ┣ 📂outreach_templates
  ┃ ┃ ┃ ┣ 📜_advocate_outreach_message.html
  ┃ ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┃ ┗ 📜index.html
  ┃ ┃ ┣ 📜ada_packet.html
  ┃ ┃ ┣ 📜attorney_brief.html
  ┃ ┃ ┣ 📜index-content.html
  ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┣ 📜receipt_usps_tracking.html
  ┃ ┃ ┣ 📜script_call_lawyers.html
  ┃ ┃ ┣ 📜template_court_doc.html
  ┃ ┃ ┣ 📜template_handup_packet_note.html
  ┃ ┃ ┣ 📜template_section_cover.html
  ┃ ┃ ┣ 📜template_section_index.html
  ┃ ┃ ┗ 📜template_war_note.html
  ┃ ┣ 📜_readme.html
  ┃ ┗ 📜index.html
  ┣ 📂99_archive
  ┃ ┣ 📂docs
  ┃ ┃ ┣ 📜_readme.html
  ┃ ┃ ┣ 📜index.html
  ┃ ┃ ┗ 📜migration_notes.html
  ┃ ┗ 📂tools
  ┃   ┣ 📜arch.010__add_frontmatter.py
  ┃   ┣ 📜arch.010__build_indexes.py
  ┃   ┣ 📜arch.010__case_brain_full_pipeline.py
  ┃   ┣ 📜arch.010__case_brain_pipeline.py
  ┃   ┣ 📜arch.010__check_orphans_and_create_indexes.py
  ┃   ┣ 📜arch.010__compress_pdfs_inplace.py
  ┃   ┣ 📜arch.010__compress_pdfs.py
  ┃   ┣ 📜arch.010__convert_all_txt_to_md.py
  ┃   ┣ 📜arch.010__convert_to_markdown.py
  ┃   ┣ 📜arch.010__fix_duplicate_frontmatter.py
  ┃   ┣ 📜arch.010__index-content.html
  ┃   ┣ 📜arch.010__index.html
  ┃   ┣ 📜arch.010__link_timeline_events.py
  ┃   ┣ 📜arch.010__move_opposing_filings.py
  ┃   ┣ 📜arch.010__optimize_pdfs_pikepdf.py
  ┃   ┣ 📜arch.010__rename_evidence_files.ps1
  ┃   ┗ 📜arch.010__update_brain.ps1
  ┣ 📜_README.md
  ┣ 📜AUDIT_REPORT.md
  ┣ 📜index_from_evidence_vault.html
  ┣ 📜index.html
  ┣ 📜J9.00.00_SECTION_COVER.md
  ┣ 📜J9.01.001_COURT_SET_MASTER.md
  ┣ 📜J9.01.002_PERSONAL_MASTER.md
  ┣ 📜J9.01.003_OPPOSITION_SET_MASTER.md
  ┣ 📜J9.01.004_INTERNAL_RED_MASTER.md
  ┗ 📜promotion_checklist.html

---

### **Assistant**
You didn’t ask a question, but the intent is obvious: you’re showing me the current repo tree because you want me to sanity-check it, call out structural problems, and tell you what to fix first so this doesn’t collapse under its own weight.

Here’s the blunt assessment and the clean path forward.

---

## What’s working (keep it)
- **Separation of concerns is mostly correct**: `00_ADMIN` vs `10_PHASES` vs `20_EVIDENCE_VAULT_IMMUTABLE` vs `40_PRINT_READY_BINDERS`.
- **You have a strong “promotion pipeline” concept** (`WZ_PROMOTION`, `READY_FOR_BINDER`, etc.)—that’s the right model for court work.
- **Your binder output structure is actually usable** (`40_PRINT_READY_BINDERS/.../a_anchor_overview`, `b_basis_issue_and_law`, etc.). That’s the end product. Everything else should feed that.

---

## The biggest problems (these will bite you)
### 1) You have multiple “truth sources” for the same content
Examples:
- Timeline exists in `00_ADMIN/05_timeline`, then again in `WI_INTERNAL/05_timeline`, then again scattered as dated MD files.
- Docket PDFs exist in `10_PHASES/.../docket_files` and again under `WI8_00_DOCKET_RECORD/...`

This creates “which one is canonical?” confusion and guarantees stale copies.

**Rule:** one canonical location per artifact type; everything else is either *derived output* or *shortcut index*.

---

### 2) The WH7 duplication explosion (it’s a mess)
You’ve got:
- `30_WORKING_DRAFTS/_raw_evidence/...` original filenames
- plus duplicated “WH7.00.020__” prefixed copies of basically everything

That’s not “organization.” That’s a storage multiplier.

**Fix:** decide whether WH7 prefixes are:
- (A) a *renaming standard* (canonical), or  
- (B) an *indexing/export standard* (derived)

Right now it’s both, so you’re duplicating.

---

### 3) Folder names with trailing commas (this will cause bugs)
You have:
- `06_medical_ada_support,`
- `07_hardships_affidavits,`
- `08_financial_other,`

Those commas will screw up scripts, links, and mental parsing.

**Fix immediately:** rename to remove commas.

---

### 4) `_ingest` is correct, but you’re letting it become a “junk drawer”
`_ingest` should be a **temporary staging area**. Things must move out and be indexed, or you’ll lose chain-of-custody clarity.

**Rule:** nothing stays in `_ingest` longer than 48 hours; it either gets promoted to:
- `30_WORKING_DRAFTS/_raw_evidence/...` (raw)
- or `20_EVIDENCE_VAULT_IMMUTABLE/...` (immutable)
- and then logged in `20_EVIDENCE_VAULT_IMMUTABLE/00_Index/evidence_log.md`

---

### 5) You have both “strategy” and “templates” duplicated across multiple places
Example: `DC_CLAIMS_AND_MOTIONS` and `WC_CLAIMS_AND_MOTIONS` and `_templates/.../motions`.

This is close to good (different roles), but right now it reads like copies rather than a pipeline.

**Rule:** templates are templates; drafts are drafts; filed is filed; print-ready is print-ready. Don’t clone between them—promote.

---

## What I would standardize (canonical map)
If you want this system to stay stable, define canonical sources like this:

### Canonical sources
- **Court record / docket PDFs:**  
  `10_PHASES/01_Foreclosure_Core_Court_Record/01_Docket/docket_files/`
- **Working analysis + drafts:**  
  `30_WORKING_DRAFTS/` (everything here is editable / in-progress)
- **Immutable evidence:**  
  `20_EVIDENCE_VAULT_IMMUTABLE/` (only finalized, hashed, logged)
- **Print-ready outputs:**  
  `40_PRINT_READY_BINDERS/` (derived outputs only—never edited manually)
- **Admin / trackers / indices:**  
  `00_ADMIN/` (governance + tracking only)

### Non-canonical (should only contain links/indexes/exports)
- `WI_INTERNAL/` looks like it’s acting as a “mirrored vault.” That’s fine **only if it is explicitly “indexes + exports,” not duplicates**.

---

## The “stop the bleeding” priority order (do these first)
1) **Remove commas from folder names** in `20_EVIDENCE_VAULT_IMMUTABLE` (fast fix, high impact).
2) **Pick canonical timeline location** (keep one; the rest become index pages that link to it).
3) **Pick canonical docket location** (one set of PDFs; elsewhere becomes references only).
4) **Decide what WH7 is**: canonical rename *or* export label—not both.
5) **Enforce promotion rules**: `_ingest → working → immutable → print-ready` with logging.

---

## A clean policy that will keep you sane
Use this as your operating doctrine:

- **Only ONE canonical file.**  
  If it exists twice, one is wrong.
- **Derived outputs must be reproducible.**  
  Print-ready HTML/PDF should be generated from source markdown/docs.
- **Immutable means immutable.**  
  Nothing gets edited in the vault—ever.
- **Every item must have:**
  - a home (canonical path),
  - an index entry,
  - and (if evidence) chain-of-custody metadata.

---

## Quick callouts from your tree (specific fixes)
- `01092026_005.pdf.pdf` → kill the double extension.
- `surplus_definciency_analysis.md` → typo (“deficiency”).
- Mixed naming: `void_judgement` vs `void_judgment` → pick one spelling and enforce it.
- `Settlement_Strategy_and_Contingency_Plan.md` is in `00_ADMIN/20_strategy` which is fine, but make sure it’s clearly **not evidence** and doesn’t get duplicated into “court binder” unless it’s meant for filing.

---

## If you tell me ONE thing, I can lock this down fast
If you answer nothing else, decide this:

**Is `WI_INTERNAL/` supposed to be:**
- (A) a *separate curated view/export layer* (indexes + read-only snapshots), **or**
- (B) a *second working copy*?

Because if it’s (B), you’re going to keep duplicating and drifting forever. The correct answer is almost always (A).

If you want, I’ll write you a short, strict “repo governance” README (rules + promotion checklist) tailored to *your* tree so you can follow it under stress without thinking.

---

### **User**
ok so the war room folder were originally like my work bench stuff that im going through and reviewing and such not quite the final product for court or future filings. so i need to clean it up and move the ready to go things int eh correct location.

---

### **Assistant**
Good — that clarification helps. What you described is **not a failure**, it’s just an unlabeled role problem. The WAR ROOM did its job; now it needs to be **demoted from “mystery blob” to a defined stage in the pipeline**.

I’m going to give you a **clean, enforceable model** and a **mechanical cleanup plan** you can execute without re-thinking every file.

No fluff. No vibes. Just order.

---

# 1. Re-define the WAR ROOM (lock this in)

**WAR ROOM = transient analysis + synthesis workspace.**

It is:
- Where you *think*, *compare*, *annotate*, *cross-reference*
- Where files are **allowed to be messy**
- Where duplicates are tolerated temporarily
- Where nothing is assumed “court-ready”

It is **NOT**:
- A canonical source
- An evidence vault
- A filing location
- A print-ready source

Write this sentence at the top of the WAR ROOM README and mean it.

---

# 2. Add a status taxonomy (this is the missing control)

Inside WAR ROOM, every item must declare **what it is**.

Create these folders **inside WAR_ROOM only**:

```
WAR_ROOM/
  00_INTAKE_UNSORTED/
  10_REVIEWING/
  20_ANALYZED_NOT_CLEAN/
  30_READY_FOR_PROMOTION/
  99_ARCHIVE_CONTEXT_ONLY/
```

### Meaning (non-negotiable)
- **00_INTAKE_UNSORTED**  
  Raw pulls, screenshots, downloads, copied PDFs, notes.
- **10_REVIEWING**  
  Actively being read, highlighted, compared.
- **20_ANALYZED_NOT_CLEAN**  
  You understand it, but it’s messy, duplicated, or not packaged.
- **30_READY_FOR_PROMOTION**  
  This is the key gate. These are *approved* to leave WAR ROOM.
- **99_ARCHIVE_CONTEXT_ONLY**  
  Kept only for background or reasoning trail; never promoted.

If it’s not in `30_READY_FOR_PROMOTION`, it **does not move**.

---

# 3. Promotion rules (this prevents future chaos)

When something is “ready,” it does **not** stay in WAR ROOM.

### Promotion destinations
| Item Type | Goes To |
|---------|--------|
| Raw factual evidence | `20_EVIDENCE_VAULT_IMMUTABLE/` |
| Editable analysis, draft motions | `30_WORKING_DRAFTS/` |
| Filed documents | `10_PHASES/.../Filed/` |
| Print-ready binder content | `40_PRINT_READY_BINDERS/` |
| Strategy / planning | `00_ADMIN/20_strategy/` |

**WAR ROOM never contains the final copy. Ever.**

After promotion:
- Leave **a stub README or shortcut note** in WAR ROOM:
  > “Promoted to: 20_EVIDENCE_VAULT_IMMUTABLE/… on YYYY-MM-DD”

This preserves your reasoning trail without duplication.

---

# 4. The actual cleanup plan (do this in order)

### Phase 1 — Freeze
Do **not** reorganize everything at once.

1. Create the five WAR ROOM folders above.
2. Move **everything currently in WAR ROOM** into:
   ```
   WAR_ROOM/00_INTAKE_UNSORTED/
   ```
   No thinking yet.

This resets cognitive load.

---

### Phase 2 — Triage (fast, not perfect)
Work one subfolder at a time:

For each file:
- If you’re **still reading / comparing** → `10_REVIEWING`
- If you **understand it but it’s messy** → `20_ANALYZED_NOT_CLEAN`
- If you’d **stake your name on it** → `30_READY_FOR_PROMOTION`
- If it’s just “why you thought what you thought” → `99_ARCHIVE_CONTEXT_ONLY`

Do not rename yet. Just sort.

---

### Phase 3 — Promotion pass (this is where order returns)
Only open `30_READY_FOR_PROMOTION`.

For each item:
1. Decide its **final home**
2. Move it there
3. If evidence:
   - Log it in `20_EVIDENCE_VAULT_IMMUTABLE/00_Index/evidence_log.md`
4. Leave a short note behind in WAR ROOM

WAR ROOM should start shrinking fast.

---

# 5. Rename WAR ROOM to something less dangerous

Once cleaned:

**Rename:**
```
WAR_ROOM → 15_ANALYSIS_WAR_ROOM
```

Why:
- It enforces stage order
- Prevents you (or a future you) from treating it as final
- Keeps it psychologically “mid-pipeline”

---

# 6. One rule that saves you from future burnout

> **If a file exists in WAR ROOM and elsewhere, WAR ROOM loses.**

WAR ROOM never wins a conflict.

---

# 7. Optional (but powerful): add a promotion checklist

Drop this file at:
```
WAR_ROOM/README_PROMOTION_RULES.md
```

Contents:
- Is this factual evidence?
- Is it complete?
- Is it edited?
- Is it logged?
- Is this the canonical copy?

If you answer “no” to any, it stays.

---

## Final grounding (because I know how your brain works)
You weren’t disorganized — you were **thinking under pressure**.

What broke was **role definition**, not capability.

Once WAR ROOM is explicitly a *thinking space* and not a *destination*, everything else snaps into place.

If you want, next I can:
- Draft the WAR ROOM README verbatim
- Create a **1-page promotion flowchart**
- Or help you do a **surgical pass on one specific subfolder** so you don’t spiral

Tell me which one.

---
