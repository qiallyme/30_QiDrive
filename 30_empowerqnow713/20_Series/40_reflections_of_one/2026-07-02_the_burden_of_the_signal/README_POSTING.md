---
layout: page
title: Readme Posting
slug: readme-posting
summary: ""
status: publish
created_at: "2026-07-16T06:19:39-04:00"
updated_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 7d0137c5300f4e79a8a5c945029cbc16
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Posting Instructions — The Burden of the Signal

## What This Package Contains

```text
the-burden-of-the-signal_site-dropin/
├── index.md
└── media/
    ├── hero.jpg
    └── video.mp4
```

## Fixes Applied

- Renamed `index.md.md` to `index.md`.
- Replaced Obsidian image syntax `![[hero.jpg]]` with standard Markdown: `![...](./media/hero.jpg)`.
- Added `hero_image`, `image`, `hero_alt`, and `featured_video` front matter.
- Added a standard HTML video embed for `video.mp4`.
- Updated the hero prompt to match the corrected QSaysIt aesthetic: electric blue, plasma purple, low-light, divine everyday grunge.

## Where To Put It

Preferred post-bundle location:

```text
30_empowerqnow713/20_Posts/EmpowerQNow/the-burden-of-the-signal/
```

Inside that folder, you should have:

```text
index.md
media/hero.jpg
media/video.mp4
```

## After Dropping It In

1. Run the housekeeping/front matter checker.
2. Rebuild the site.
3. Confirm the post appears under EmpowerQNow.
4. Confirm the hero image renders.
5. Confirm the video plays.
6. Confirm the final URL resolves to something like:

```text
/empowerqnow/the-burden-of-the-signal/
```

## Watch For

If the post does not appear, check:

- `visibility: public`
- `status: active`
- `nav_hidden: false`
- `series: EmpowerQNow`
- `slug: the-burden-of-the-signal`
- whether the builder supports page bundles with `index.md`

If the builder does **not** support page bundles, use the fallback pattern:

```text
20_Posts/EmpowerQNow/the-burden-of-the-signal.md
assets/posts/the-burden-of-the-signal/hero.jpg
assets/posts/the-burden-of-the-signal/video.mp4
```

Then update asset paths in front matter and body accordingly.
