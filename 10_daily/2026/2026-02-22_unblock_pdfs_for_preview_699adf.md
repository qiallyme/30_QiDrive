---
title: "Unblock PDFs for Preview"
date: "2026-02-22"
created_at: "2026-02-22T10:52:25.940196+00:00"
conversation_id: "699adfe1-ba9c-832d-b6c5-429ea27c61ef"
tags:
  - ai_chat
  - export
---

# Unblock PDFs for Preview

> **Date:** 2026-02-22 | **Conversation ID:** `699adfe1-ba9c-832d-b6c5-429ea27c61ef`

---

### **User**
WHATS THE COMMAND TO UNBLOCK ALL PDF TO THE SHOW UP IN THE PREVIEW

---

### **Assistant**
If you’re on **Windows** and PDFs aren’t previewing because they’re “blocked” (downloaded from the internet), here are the exact commands.

## Unblock a Single PDF (PowerShell)

```powershell
Unblock-File "C:\Path\To\Your\File.pdf"
```

## Unblock All PDFs in a Folder

```powershell
Get-ChildItem "C:\Path\To\Folder" -Filter *.pdf | Unblock-File
```

## Unblock All PDFs Recursively (including subfolders)

```powershell
Get-ChildItem "C:\Path\To\Folder" -Filter *.pdf -Recurse | Unblock-File
```

---

If the issue is **Explorer Preview Pane not showing PDFs**, also check:

1. Open File Explorer  
2. View → Preview Pane  
3. Make sure **Adobe Acrobat** (or your PDF viewer) is set as default  
4. In Adobe: Edit → Preferences → General → enable **“Enable PDF thumbnail previews in Windows Explorer”**

If that’s not the scenario, tell me:
- Windows or Mac?
- Is it a browser preview issue or File Explorer preview issue?
- Any error message?

---
