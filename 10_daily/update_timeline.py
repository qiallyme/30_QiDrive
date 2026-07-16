#!/usr/bin/env python3
"""
QiLabs Daily Timeline Generator
Parses daily log markdown files and builds an interactive visual HTML timeline.
"""

import os
import re
import json
import html
from pathlib import Path

# Setup paths relative to the script location
SCRIPT_DIR = Path(__file__).parent.resolve()
OUTPUT_HTML = SCRIPT_DIR / "daily_timeline.html"

print("Scanning daily log directories...")

# Scan all folders matching a 4-digit year format
year_dirs = sorted([d for d in SCRIPT_DIR.iterdir() if d.is_dir() and re.match(r'^\d{4}$', d.name)])

events = []
all_tags = set()

# Regex to parse frontmatter safely without external dependencies
FM_PATTERN = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL | re.MULTILINE)

for y_dir in year_dirs:
    for md_file in y_dir.glob("*.md"):
        if md_file.name.startswith("_"):
            continue
            
        content = md_file.read_text(encoding="utf-8", errors="replace")
        
        # Parse event date from filename (YYYY-MM-DD) or fallback to file creation
        date_match = re.match(r'^(\d{4}-\d{2}-\d{2})', md_file.stem)
        event_date = date_match.group(1) if date_match else f"{y_dir.name}-01-01"
        
        # Parse frontmatter
        title = md_file.stem
        summary = ""
        tags = []
        
        fm_match = FM_PATTERN.match(content)
        body = content
        if fm_match:
            fm_text = fm_match.group(1)
            body = content[fm_match.end():]
            
            # Simple line parsing for YAML keys
            for line in fm_text.splitlines():
                if line.startswith("title:"):
                    title = line.split(":", 1)[1].strip().strip('"').strip("'")
                elif line.startswith("summary:"):
                    summary = line.split(":", 1)[1].strip().strip('"').strip("'")
                elif line.startswith("tags:"):
                    # Handle YAML inline array [tag1, tag2] or bullet tags (simple parsing)
                    tags_raw = line.split(":", 1)[1].strip()
                    if tags_raw.startswith("[") and tags_raw.endswith("]"):
                        tags = [t.strip().strip('"').strip("'") for t in tags_raw[1:-1].split(",") if t.strip()]
                    else:
                        tags = [tags_raw] if tags_raw else []
                        
            # If tags is empty, check if tags is defined on separate lines
            if not tags:
                # Look for bullet points inside tags block in YAML if multiline
                tags_block_match = re.search(r'tags:\s*\n((?:\s+-\s+\S+\n)+)', fm_text)
                if tags_block_match:
                    tags = [line.strip().replace("-", "").strip() for line in tags_block_match.group(1).splitlines() if line.strip()]
        
        # fallback summary from first lines of body if empty
        if not summary:
            # Strip markdown headers, checkboxes, and HTML comments/tags
            clean_body = re.sub(r'#+\s+.*?\n', '', body)
            clean_body = re.sub(r'Category:.*?\n|Created time:.*?\n|Date:.*?\n|Event Description:.*?\n|Slug:.*?\n|Status:.*?\n|Realm:.*?\n|sensitivity:.*?\n|classification:.*?\n|aliases:.*?\n|node:.*?\n|system:.*?\n|graph_weight:.*?\n|tags:.*?\n|orbit:.*?\n|Blocked by:.*?\n|Blocking:.*?\n', '', clean_body, flags=re.IGNORECASE)
            clean_body = re.sub(r'<!--.*?-->|<[^>]+>', '', clean_body, flags=re.DOTALL)
            clean_body = re.sub(r'-\s+\[\s*\]\s*', '', clean_body)
            clean_body = clean_body.strip()
            
            # Get first 160 characters
            first_lines = [line.strip() for line in clean_body.splitlines() if line.strip() and not line.strip().startswith("-")]
            if first_lines:
                summary = " ".join(first_lines)[:160] + "..." if len(" ".join(first_lines)) > 160 else " ".join(first_lines)
                
        # Fallback tags from body if empty
        if not tags:
            body_tags_match = re.findall(r'•\s*([a-zA-Z0-9\s-]+)', body)
            if body_tags_match:
                tags = [t.strip() for t in body_tags_match if t.strip()]
            else:
                inline_tags = re.findall(r'#([a-zA-Z0-9_-]+)', body)
                if inline_tags:
                    tags = inline_tags

        # Resolve human category/type for color tagging
        category = "General"
        category_match = re.search(r'Category:\s*([a-zA-Z\s]+)', body, re.IGNORECASE)
        if category_match:
            category = category_match.group(1).strip()
            
        tags = sorted(list(set([t.lower().replace("#", "").strip() for t in tags if t.strip()])))
        for t in tags:
            all_tags.add(t)
            
        # File URL relative to timeline HTML
        rel_path = md_file.relative_to(SCRIPT_DIR).as_posix()
        file_url = f"file:///{md_file.as_posix().replace(' ', '%20')}"
        
        events.append({
            "date": event_date,
            "year": y_dir.name,
            "title": title,
            "summary": summary,
            "tags": tags,
            "category": category,
            "path": rel_path,
            "file_url": file_url
        })

# Sort events chronologically
events.sort(key=lambda e: e["date"])
unique_years = sorted(list(set(e["year"] for e in events)))

print(f"Parsed {len(events)} daily log events. Compiling dashboard...")

# Generate the timeline HTML string
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QiVault Interactive Life Timeline</title>
    <!-- Premium Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        :root {{
            --bg-color: #0b111e;
            --panel-color: rgba(21, 31, 50, 0.7);
            --card-color: rgba(27, 41, 66, 0.65);
            --text-color: #f1f5f9;
            --muted-color: #94a3b8;
            --primary: #818cf8;
            --accent: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --border: rgba(255, 255, 255, 0.08);
            --timeline-line: rgba(129, 140, 248, 0.25);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            overflow-x: hidden;
            background-image: 
                radial-gradient(at 10% 20%, rgba(129, 140, 248, 0.08) 0px, transparent 50%),
                radial-gradient(at 90% 80%, rgba(16, 185, 129, 0.06) 0px, transparent 50%);
            background-attachment: fixed;
        }}

        header {{
            background: linear-gradient(180deg, rgba(11, 17, 30, 0.95) 0%, rgba(11, 17, 30, 0) 100%);
            padding: 2.5rem 2rem 1.5rem;
            position: sticky;
            top: 0;
            z-index: 100;
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border);
        }}

        .header-content {{
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }}

        .title-block {{
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }}

        .title-block i {{
            color: var(--primary);
            width: 32px;
            height: 32px;
        }}

        h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 2.2rem;
            font-weight: 700;
            letter-spacing: -0.03em;
            background: linear-gradient(135deg, #fff 30%, var(--primary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .search-filter-row {{
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            align-items: center;
        }}

        .search-wrapper {{
            position: relative;
            flex: 1;
            min-width: 280px;
        }}

        .search-wrapper i {{
            position: absolute;
            left: 1rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--muted-color);
            pointer-events: none;
            width: 18px;
            height: 18px;
        }}

        .search-input {{
            width: 100%;
            padding: 0.8rem 1rem 0.8rem 2.8rem;
            background-color: rgba(15, 23, 42, 0.6);
            border: 1px solid var(--border);
            border-radius: 50px;
            color: var(--text-color);
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            transition: all 0.3s ease;
        }}

        .search-input:focus {{
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 15px rgba(129, 140, 248, 0.2);
            background-color: rgba(15, 23, 42, 0.8);
        }}

        .filter-group {{
            display: flex;
            gap: 0.5rem;
            overflow-x: auto;
            padding-bottom: 0.3rem;
            scrollbar-width: none;
        }}

        .filter-group::-webkit-scrollbar {{
            display: none;
        }}

        .btn {{
            padding: 0.6rem 1.1rem;
            border: 1px solid var(--border);
            background-color: var(--panel-color);
            color: var(--text-color);
            font-family: 'Outfit', sans-serif;
            font-size: 0.9rem;
            font-weight: 600;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .btn:hover {{
            border-color: var(--primary);
            background-color: rgba(129, 140, 248, 0.1);
        }}

        .btn.active {{
            background-color: var(--primary);
            color: #0b111e;
            border-color: var(--primary);
            box-shadow: 0 0 15px rgba(129, 140, 248, 0.45);
        }}

        main {{
            max-width: 1000px;
            margin: 0 auto;
            padding: 2.5rem 1.5rem 5rem;
            position: relative;
        }}

        .timeline-line {{
            position: absolute;
            left: 50%;
            top: 2rem;
            bottom: 2rem;
            width: 2px;
            background-color: var(--timeline-line);
            transform: translateX(-50%);
            z-index: 1;
        }}

        .timeline-container {{
            position: relative;
            z-index: 10;
            display: flex;
            flex-direction: column;
            gap: 2.5rem;
        }}

        .event-node {{
            display: grid;
            grid-template-columns: 1fr 60px 1fr;
            align-items: center;
            opacity: 1;
            transition: transform 0.5s ease, opacity 0.5s ease;
        }}

        .event-node.hidden {{
            display: none;
        }}

        .left-content {{
            grid-column: 1;
            text-align: right;
            display: flex;
            justify-content: flex-end;
        }}

        .right-content {{
            grid-column: 3;
            text-align: left;
            display: flex;
            justify-content: flex-start;
        }}

        .timeline-dot-wrapper {{
            grid-column: 2;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }}

        .timeline-dot {{
            width: 16px;
            height: 16px;
            background-color: var(--bg-color);
            border: 3px solid var(--primary);
            border-radius: 50%;
            z-index: 15;
            transition: all 0.3s ease;
            box-shadow: 0 0 10px rgba(129, 140, 248, 0.4);
        }}

        .event-node:hover .timeline-dot {{
            transform: scale(1.35);
            background-color: var(--primary);
            box-shadow: 0 0 18px var(--primary);
        }}

        .glass-card {{
            background: var(--panel-color);
            backdrop-filter: blur(16px);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 1.5rem;
            width: 92%;
            max-width: 440px;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            position: relative;
        }}

        .glass-card:hover {{
            transform: translateY(-5px);
            border-color: rgba(129, 140, 248, 0.35);
            box-shadow: 0 15px 40px rgba(129, 140, 248, 0.15);
            background: rgba(21, 31, 50, 0.85);
        }}

        .event-date {{
            font-family: 'Outfit', sans-serif;
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--primary);
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.3rem;
        }}

        .left-content .event-date {{
            justify-content: flex-end;
        }}

        .event-title-link {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--text-color);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.4rem;
            margin-bottom: 0.8rem;
            transition: color 0.2s ease;
        }}

        .left-content .event-title-link {{
            justify-content: flex-end;
        }}

        .event-title-link:hover {{
            color: var(--primary);
        }}

        .event-title-link i {{
            width: 14px;
            height: 14px;
            opacity: 0.5;
            transition: opacity 0.2s ease;
        }}

        .event-title-link:hover i {{
            opacity: 1;
        }}

        .event-summary {{
            font-size: 0.9rem;
            color: var(--muted-color);
            margin-bottom: 1rem;
        }}

        .event-footer {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            align-items: center;
        }}

        .left-content .event-footer {{
            justify-content: flex-end;
        }}

        .badge {{
            padding: 0.3rem 0.7rem;
            font-size: 0.75rem;
            font-weight: 600;
            border-radius: 4px;
            background-color: rgba(255, 255, 255, 0.05);
            color: var(--muted-color);
            border: 1px solid var(--border);
        }}

        .badge-category {{
            background-color: rgba(16, 185, 129, 0.12);
            color: var(--accent);
            border-color: rgba(16, 185, 129, 0.25);
        }}

        .tag-badge {{
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .tag-badge:hover {{
            background-color: var(--primary);
            color: #0b111e;
            border-color: var(--primary);
        }}

        .no-results {{
            text-align: center;
            padding: 4rem 2rem;
            background: var(--panel-color);
            border: 1px solid var(--border);
            border-radius: 16px;
            color: var(--muted-color);
            display: none;
        }}

        .no-results i {{
            width: 48px;
            height: 48px;
            margin-bottom: 1rem;
            color: var(--primary);
            opacity: 0.6;
        }}

        /* Responsive Layout adjustment */
        @media (max-width: 768px) {{
            .timeline-line {{
                left: 20px;
            }}

            .event-node {{
                grid-template-columns: 40px 1fr;
                gap: 0;
            }}

            .timeline-dot-wrapper {{
                grid-column: 1;
                justify-content: center;
            }}

            .left-content, .right-content {{
                grid-column: 2;
                text-align: left;
                justify-content: flex-start;
                padding-left: 1.5rem;
            }}

            .left-content .event-date, .left-content .event-title-link, .left-content .event-footer {{
                justify-content: flex-start;
            }}

            .glass-card {{
                width: 100%;
                max-width: 100%;
            }}
        }}
    </style>
</head>
<body>

    <header>
        <div class="header-content">
            <div class="title-block">
                <i data-lucide="milestone"></i>
                <h1>QiVault Interactive Life Timeline</h1>
            </div>
            
            <div class="search-filter-row">
                <div class="search-wrapper">
                    <i data-lucide="search"></i>
                    <input type="text" id="searchInput" class="search-input" placeholder="Search events, tags, categories, or text...">
                </div>
                
                <div class="filter-group">
                    <button class="btn active" onclick="filterYear('all', this)">All Years</button>
                    {"".join(f'<button class="btn" onclick="filterYear(\'{yr}\', this)">{yr}</button>' for yr in unique_years)}
                </div>
            </div>
        </div>
    </header>

    <main>
        <div class="timeline-line"></div>
        
        <div class="timeline-container" id="timelineContainer">
            {"".join(f"""
            <div class="event-node" data-year="{e['year']}" data-tags="{",".join(e['tags'])}" data-category="{e['category'].lower()}" data-search="{html.escape(e['title'].lower() + ' ' + e['summary'].lower() + ' ' + e['category'].lower())}">
                <div class="{"left-content" if i % 2 == 0 else "right-content"}">
                    <div class="glass-card">
                        <div class="event-date">
                            <i data-lucide="calendar"></i> {e['date']}
                        </div>
                        <a href="{e['file_url']}" target="_blank" class="event-title-link">
                            {html.escape(e['title'])} <i data-lucide="external-link"></i>
                        </a>
                        <div class="event-summary">{html.escape(e['summary'])}</div>
                        <div class="event-footer">
                            <span class="badge badge-category">{html.escape(e['category'])}</span>
                            {"".join(f'<span class="badge tag-badge" onclick="filterTag(\'{t}\')">#{html.escape(t)}</span>' for t in e['tags'])}
                        </div>
                    </div>
                </div>
                <div class="timeline-dot-wrapper">
                    <div class="timeline-dot"></div>
                </div>
            </div>
            """ for i, e in enumerate(events))}
        </div>
        
        <div class="no-results" id="noResults">
            <i data-lucide="frown"></i>
            <h2>No timeline events match your filter</h2>
            <p>Try resetting the year filter or clearing the search text.</p>
        </div>
    </main>

    <script>
        // Init Lucide Icons
        lucide.createIcons();

        let currentYear = 'all';
        let currentTag = '';
        
        const searchInput = document.getElementById('searchInput');
        const eventNodes = document.querySelectorAll('.event-node');
        const noResults = document.getElementById('noResults');

        searchInput.addEventListener('input', filterEvents);

        function filterYear(year, button) {{
            currentYear = year;
            currentTag = ''; // Reset tag selection on year change
            
            // Toggle active class in buttons
            document.querySelectorAll('.filter-group .btn').forEach(btn => {{
                btn.classList.remove('active');
            }});
            button.classList.add('active');
            
            filterEvents();
        }}

        function filterTag(tag) {{
            currentTag = tag;
            searchInput.value = ''; // Clear search when clicking a tag for specific viewing
            
            // Reset active year button to all
            document.querySelectorAll('.filter-group .btn').forEach(btn => {{
                btn.classList.remove('active');
            }});
            document.querySelector('.filter-group .btn').classList.add('active');
            currentYear = 'all';
            
            filterEvents();
        }}

        function filterEvents() {{
            const searchVal = searchInput.value.toLowerCase().strip();
            let visibleCount = 0;
            
            eventNodes.forEach(node => {{
                const nodeYear = node.getAttribute('data-year');
                const nodeTags = node.getAttribute('data-tags').split(',');
                const searchContent = node.getAttribute('data-search');
                
                let matchesYear = (currentYear === 'all' || nodeYear === currentYear);
                let matchesTag = (currentTag === '' || nodeTags.includes(currentTag));
                let matchesSearch = (searchVal === '' || searchContent.includes(searchVal) || nodeTags.some(t => t.includes(searchVal)));
                
                if (matchesYear && matchesTag && matchesSearch) {{
                    node.classList.remove('hidden');
                    visibleCount++;
                }} else {{
                    node.classList.add('hidden');
                }}
            }});
            
            if (visibleCount === 0) {{
                noResults.style.display = 'block';
                document.querySelector('.timeline-line').style.display = 'none';
            }} else {{
                noResults.style.display = 'none';
                document.querySelector('.timeline-line').style.display = 'block';
            }}
        }}

        // Helper string strip method
        String.prototype.strip = function() {{
            return this.replace(/^\\s+|\\s+$/g, '');
        }};
    </script>
</body>
</html>
"""

# Save visual HTML file
with OUTPUT_HTML.open("w", encoding="utf-8", newline="") as f:
    f.write(html_template)

print(f"Timeline HTML successfully created at: {OUTPUT_HTML}")
print("Run this script whenever you add or edit daily logs to refresh the dashboard.")
