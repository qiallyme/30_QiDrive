#!/usr/bin/env python3
"""
Build Timeline JSON from Markdown Files

This script reads all .md files from the events/ directory,
parses their YAML front matter, and generates a timeline.json file.
"""

import json
import os
import re
import shutil
from pathlib import Path
from datetime import datetime

# Paths
SCRIPT_DIR = Path(__file__).parent
EVENTS_DIR = SCRIPT_DIR / "events"
DIST_DIR = SCRIPT_DIR / "dist"
OUTPUT_FILE = DIST_DIR / "timeline.json"

# Files to copy to dist
FILES_TO_COPY = [
    "index.html",
    "styles.css",
    "script.js",
    "timeline-loader-json.js"
]

def parse_front_matter(content):
    """Parse YAML front matter from markdown content"""
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)
    
    if not match:
        return None
    
    front_matter_text = match.group(1)
    body = match.group(2).strip()
    
    # Parse YAML (simple parser)
    data = {}
    lines = front_matter_text.split('\n')
    current_key = None
    current_array = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check for array items
        if line.startswith('- '):
            if current_key:
                current_array.append(line[2:].strip())
            continue
        
        # Check for key-value pairs
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            if value == '':
                # Save previous array if exists
                if current_key and current_array:
                    data[current_key] = current_array
                # This is an array key
                current_key = key
                current_array = []
            else:
                # Save previous array if exists
                if current_key and current_array:
                    data[current_key] = current_array
                current_key = None
                current_array = []
                
                # Parse value
                if value == 'true':
                    data[key] = True
                elif value == 'false':
                    data[key] = False
                else:
                    data[key] = value
    
    # Save last array if exists
    if current_key and current_array:
        data[current_key] = current_array
    
    return {
        'frontMatter': data,
        'content': body
    }

def build_timeline():
    """Main build function"""
    print('\nBuilding timeline from markdown files...\n')
    
    # Create dist directory
    DIST_DIR.mkdir(exist_ok=True)
    if not DIST_DIR.exists():
        print('Created dist/ directory\n')
    
    # Copy files to dist
    print('Copying files to dist/...')
    for file_name in FILES_TO_COPY:
        src_path = SCRIPT_DIR / file_name
        dest_path = DIST_DIR / file_name
        if src_path.exists():
            shutil.copy2(src_path, dest_path)
            print(f'  [OK] {file_name}')
        else:
            print(f'  [SKIP] {file_name} not found')
    print()
    
    # Check if events directory exists
    if not EVENTS_DIR.exists():
        print('[ERROR] events/ directory not found!')
        return
    
    # Read all markdown files
    md_files = [f for f in EVENTS_DIR.glob('*.md') if not f.name.startswith('_')]
    print(f'Found {len(md_files)} markdown file(s)\n')
    
    # Parse each file
    events = []
    success_count = 0
    error_count = 0
    
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            parsed = parse_front_matter(content)
            
            if parsed:
                event = {
                    'id': md_file.stem,
                    'date': parsed['frontMatter'].get('date', ''),
                    'title': parsed['frontMatter'].get('title', ''),
                    'category': parsed['frontMatter'].get('category', ''),
                    'life_stage': parsed['frontMatter'].get('life_stage', ''),
                    'critical': parsed['frontMatter'].get('critical', False),
                    'tags': parsed['frontMatter'].get('tags', []),
                    'description': parsed['content']
                }
                
                events.append(event)
                print(f'  [OK] {md_file.name}')
                success_count += 1
            else:
                print(f'  [FAIL] {md_file.name} - Invalid front matter')
                error_count += 1
        except Exception as e:
            print(f'  [FAIL] {md_file.name} - {str(e)}')
            error_count += 1
    
    # Sort events by date (newest first)
    events.sort(key=lambda x: x['date'], reverse=True)
    
    # Write JSON file
    OUTPUT_FILE.write_text(json.dumps(events, indent=2), encoding='utf-8')
    
    print('\n' + '=' * 50)
    print(f'[SUCCESS] Built timeline.json')
    print(f'   Total events: {len(events)}')
    print(f'   Success: {success_count}')
    if error_count > 0:
        print(f'   Errors: {error_count}')
    print(f'   Output: {OUTPUT_FILE}')
    print('=' * 50 + '\n')
    
    # Print statistics
    categories = {}
    critical_count = sum(1 for e in events if e['critical'])
    
    for event in events:
        cat = event['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    print('Statistics:')
    print(f'   Critical events: {critical_count}')
    print('   By category:')
    for cat in sorted(categories.keys()):
        print(f'     - {cat}: {categories[cat]}')
    print()

if __name__ == '__main__':
    try:
        build_timeline()
    except Exception as e:
        print(f'[ERROR] Build failed: {str(e)}')
        exit(1)

