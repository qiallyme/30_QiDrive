import os
import json
import re
import sys
import unicodedata
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LOGS_DIR = r'C:\QiLabs\40_QiVault\01_inbox\logs'
DAILY_DIR = r'C:\QiLabs\40_QiVault\10_daily'

def slugify(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    value = re.sub(r'[-\s]+', '_', value)
    return value

def format_blockquote(text):
    if not text:
        return ""
    lines = text.split('\n')
    return "\n".join(f"> {line}" for line in lines)

def process_conversation(conv, source_file):
    conv_id = conv.get("id") or conv.get("conversation_id")
    title = conv.get("title") or "Untitled Conversation"
    create_time = conv.get("create_time")
    
    if not create_time:
        return
        
    dt = datetime.fromtimestamp(create_time)
    date_str = dt.strftime('%Y-%m-%d')
    time_str = dt.strftime('%H:%M:%S')
    year_str = dt.strftime('%Y')
    
    mapping = conv.get("mapping", {})
    current_node = conv.get("current_node")
    
    # Reconstruct active thread of user and assistant messages
    thread = []
    node_id = current_node
    while node_id:
        node = mapping.get(node_id)
        if not node:
            break
        msg = node.get("message")
        if msg:
            author = msg.get("author", {})
            role = author.get("role")
            content = msg.get("content", {})
            parts = content.get("parts", [])
            
            text_parts = []
            for part in parts:
                if isinstance(part, str):
                    text_parts.append(part)
                elif isinstance(part, dict):
                    text_parts.append(part.get("text", str(part)))
                else:
                    text_parts.append(str(part))
            
            text = "".join(text_parts).strip()
            if role in ("user", "assistant") and text:
                thread.append({
                    "role": role,
                    "text": text
                })
        node_id = node.get("parent")
        
    thread.reverse()
    
    if not thread:
        return  # skip empty conversations
        
    # Generate filename and target path
    slug = slugify(title)
    if not slug:
        slug = f"chat_{conv_id[:8]}"
        
    year_dir = os.path.join(DAILY_DIR, year_str)
    os.makedirs(year_dir, exist_ok=True)
    
    filename = f"{date_str}_{slug}.md"
    file_path = os.path.join(year_dir, filename)
    
    counter = 1
    while os.path.exists(file_path):
        filename = f"{date_str}_{slug}_{counter}.md"
        file_path = os.path.join(year_dir, filename)
        counter += 1
        
    # Build markdown content with frontmatter
    fm = f"""---
layout: page
title: "{title}"
slug: "{slug}"
created_at: "{date_str} {time_str}"
updated_at: "{date_str} {time_str}"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "{source_file}"
template_key: master-template
date: {date_str}
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "{conv_id}"
canonical_ref: ""
---

# {title}

## Overview
- **Date**: {date_str} {time_str}
- **Conversation ID**: `{conv_id}`
- **Source**: `{source_file}`

## Chat History
"""
    
    for msg in thread:
        role_label = "User" if msg["role"] == "user" else "Assistant"
        fm += f"\n### {role_label}\n{format_blockquote(msg['text'])}\n"
        
    with open(file_path, 'w', encoding='utf-8') as out_f:
        out_f.write(fm)
        
    return file_path

def main():
    processed_count = 0
    skipped_count = 0
    
    # 1. Process __CaptainsLogchatexports (1).json
    main_json = os.path.join(LOGS_DIR, "__CaptainsLogchatexports (1).json")
    if os.path.exists(main_json):
        print(f"Processing {main_json}...")
        with open(main_json, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                for conv in data:
                    res = process_conversation(conv, "__CaptainsLogchatexports (1).json")
                    if res:
                        processed_count += 1
                    else:
                        skipped_count += 1
            except Exception as e:
                print(f"Error reading {main_json}: {e}")
                
    # 2. Process Chat-Export-28513-2026/conversations-*.json
    chat_export_dir = os.path.join(LOGS_DIR, "Chat-Export-28513-2026")
    if os.path.exists(chat_export_dir):
        print(f"Processing {chat_export_dir}...")
        for f in sorted(os.listdir(chat_export_dir)):
            if f.startswith("conversations-") and f.endswith(".json"):
                full_path = os.path.join(chat_export_dir, f)
                with open(full_path, 'r', encoding='utf-8') as jf:
                    try:
                        data = json.load(jf)
                        for conv in data:
                            res = process_conversation(conv, f"Chat-Export-28513-2026/{f}")
                            if res:
                                processed_count += 1
                            else:
                                skipped_count += 1
                    except Exception as e:
                        print(f"Error reading {full_path}: {e}")
                        
    print(f"Done. Processed: {processed_count} chats, Skipped: {skipped_count} chats.")

if __name__ == "__main__":
    main()
