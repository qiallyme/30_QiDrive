from __future__ import annotations

import csv
import re
import shutil
from pathlib import Path


ROOT = Path.cwd()
QICODE = ROOT / "10_qispark" / "10_QiSpark" / "00_QiCode"
CLEANUP = ROOT / "_qiconfig" / "cleanup_2026-06-29_qicode_legal_labels"
BACKUP = CLEANUP / "backups_before_legal_labels"
REPORT = CLEANUP / "qicode_legal_labels_manifest.csv"
TODAY = "2026-06-29"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def backup(path: Path) -> None:
    if path.exists():
        target = BACKUP / path.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            shutil.copy2(path, target)


def write(path: Path, text: str, rows: list[dict[str, str]], reason: str) -> None:
    backup(path)
    path.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")
    rows.append({"action": "rewrite", "path": rel(path), "reason": reason})


def title_num_from_code(code: str) -> int:
    return int(code[1:])


def legal_section_ref(title: int, article: int, section: int) -> str:
    return f"Sec. {title}.{article:02d}.{section:03d}"


def rewrite_title_file(path: Path) -> tuple[str, bool]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    changed = False

    title_match = re.search(r"# QiCode Title (\d+) - (.+)", text)
    if not title_match:
        return text, False
    title_num = int(title_match.group(1))
    title_name = title_match.group(2).strip()
    code = f"T{title_num:02d}"

    text = text.replace(
        f"# QiCode Title {title_num:02d} - {title_name}",
        f"# Title {title_num}. {title_name}",
    )
    text = text.replace(
        f"title: QiCode Title {title_num:02d} - {title_name}",
        f"title: Title {title_num}. {title_name}",
    )

    text = re.sub(
        r"## Citation\n\n- Title citation: `QiCode T(\d{2})`\n- Section citation form: `QiCode T\d{2}\.A##\.S###`\n- Line citation form: `QiCode T\d{2}\.A##\.S###\.L###`",
        lambda m: (
            "## Citation\n\n"
            f"- Legal citation: `QiCode Title {int(m.group(1))}`\n"
            f"- Article citation: `QiCode Title {int(m.group(1))}, Article #`\n"
            f"- Section citation: `QiCode Sec. {int(m.group(1))}.##.###`\n"
            f"- Stable ID alias: `QiCode T{m.group(1)}.A##.S###.L###`"
        ),
        text,
    )

    text = re.sub(
        rf"## Article (\d+) - (.+Sec.) \(`{code}\.A(\d\d)`\)",
        lambda m: f"## Article {int(m.group(1))}. {m.group(2)}\n\nStable ID: `{code}.A{m.group(3)}`",
        text,
    )

    def section_repl(match: re.Match[str]) -> str:
        section_num = int(match.group(1))
        section_name = match.group(2)
        stable = match.group(3)
        stable_match = re.match(r"T(\d\d)\.A(\d\d)\.S(\d\d\d)", stable)
        if not stable_match:
            return match.group(0)
        title = int(stable_match.group(1))
        article = int(stable_match.group(2))
        section = int(stable_match.group(3))
        legal = legal_section_ref(title, article, section)
        return f"### {legal}. {section_name}\n\nStable ID: `{stable}`"

    text = re.sub(r"### Section (\d+) - (.+Sec.) \(`(T\d\d\.A\d\d\.S\d\d\d)`\)", section_repl, text)

    def line_repl(match: re.Match[str]) -> str:
        stable = match.group(1)
        line_num = int(match.group(2))
        body = match.group(3)
        stable_match = re.match(r"T(\d\d)\.A(\d\d)\.S(\d\d\d)", stable)
        if not stable_match:
            return match.group(0)
        title = int(stable_match.group(1))
        article = int(stable_match.group(2))
        section = int(stable_match.group(3))
        legal = legal_section_ref(title, article, section)
        return f"- `Line {line_num}` {body} (`{legal}.L{line_num:03d}`; stable ID `{stable}.L{line_num:03d}`)"

    text = re.sub(r"- `(T\d\d\.A\d\d\.S\d\d\d)\.L(\d\d\d)` (.+)", line_repl, text)

    def rule_repl(match: re.Match[str]) -> str:
        line_num = int(match.group(1))
        body = match.group(2)
        return f"- `Rule {title_num}.001.L{line_num:03d}` {body} (stable ID `{code}.R001.L{line_num:03d}`)"

    text = re.sub(rf"- `{code}\.R001\.L(\d\d\d)` (.+)", rule_repl, text)

    text = text.replace('updated_at: "2026-06-29"', f'updated_at: "{TODAY}"')
    changed = True
    return text, changed


def rewrite_index(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    text = text.replace("- Title: `QiCode T01`", "- Title: `QiCode Title 1`")
    text = text.replace("- Article: `QiCode T01.A01`", "- Article: `QiCode Title 1, Article 1`")
    text = text.replace("- Section: `QiCode T01.A01.S010`", "- Section: `QiCode Sec. 1.01.010`")
    text = text.replace("- Line: `QiCode T01.A01.S010.L001`", "- Line: `QiCode Sec. 1.01.010, Line 1`")
    text = re.sub(r"\[`QiCode T(\d\d)` - ([^\]]+)\]", lambda m: f"[Title {int(m.group(1))}. {m.group(2)}]", text)
    return text


def rewrite_guide(path: Path) -> str:
    return """---
layout: page
title: QiCode Citation Guide
slug: qicode-citation-guide
summary: Reference syntax for citing QiCode personal-doctrine provisions.
status: active
updated_at: "2026-06-29"
tags:
  - qicode
source_type: manual
---
# QiCode Citation Guide

## Legal Citation First

Use the plain legal-style citation first. Use the compact ID only when exact machine-stable reference is helpful.

## Hierarchy

- `Title #` means the major division of the doctrine.
- `Article #` means a subdivision inside a title.
- `Sec. #.##.###` means a section.
- `Line #` means a citeable rule line inside a section.

## Examples

- `QiCode Title 1` cites Title 1, My Truth and Source.
- `QiCode Title 1, Article 2` cites the Law of One article.
- `QiCode Sec. 3.03.010` cites Title 3, Article 3, Section 010: Boundary Validity.
- `QiCode Sec. 9.03.020, Line 1` cites the QiMemory bridge rule.

## Stable ID Aliases

- `QiCode T01` is the stable ID alias for `QiCode Title 1`.
- `QiCode T01.A02` is the stable ID alias for `QiCode Title 1, Article 2`.
- `QiCode T03.A03.S010` is the stable ID alias for `QiCode Sec. 3.03.010`.
- `QiCode T09.A03.S020.L001` is the stable ID alias for `QiCode Sec. 9.03.020, Line 1`.

## Style Rules

- Put legal-style citations before stable IDs.
- Keep section numbers stable once cited.
- Add new sections in increments of 10, such as `Sec. 1.01.010`, `Sec. 1.01.020`, and `Sec. 1.01.030`.
- Treat `Title 1` through `Title 8` as personal doctrine and `Title 9` as the bridge into QiSpark technical doctrine.
"""


def rewrite_overview(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    replacements = {
        "`T01`": "`Title 1`",
        "`T02` through `T04`": "`Title 2` through `Title 4`",
        "`T05` through `T07`": "`Title 5` through `Title 7`",
        "`T08`": "`Title 8`",
        "`T09`": "`Title 9`",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def main() -> int:
    rows: list[dict[str, str]] = []
    CLEANUP.mkdir(parents=True, exist_ok=True)
    for path in sorted(QICODE.glob("title_*/*.md")):
        new_text, changed = rewrite_title_file(path)
        if changed:
            write(path, new_text, rows, "Legal-style citations before stable IDs.")
    write(QICODE / "_index.md", rewrite_index(QICODE / "_index.md"), rows, "Updated index citation examples and title labels.")
    write(QICODE / "citation_guide.md", rewrite_guide(QICODE / "citation_guide.md"), rows, "Rewrote citation guide around legal citations first.")
    write(QICODE / "01_core_overview.md", rewrite_overview(QICODE / "01_core_overview.md"), rows, "Updated overview to use Title labels first.")

    with REPORT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["action", "path", "reason"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"actions={len(rows)}")
    print(f"report={REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
