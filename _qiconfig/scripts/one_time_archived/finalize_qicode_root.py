from __future__ import annotations

import csv
import re
import shutil
from pathlib import Path


ROOT = Path.cwd()
QICODE = ROOT / "10_qispark" / "00_QiCode"
QISPARK = ROOT / "10_qispark" / "10_QiSpark"
CLEANUP = ROOT / "_qiconfig" / "cleanup_2026-06-30_qicode_root"
BACKUP = CLEANUP / "backups"
REPORT = CLEANUP / "qicode_root_manifest.csv"
TODAY = "2026-06-30"


MOVE_MAP = {
    QICODE / "citation_guide.md": QICODE / "reference" / "citation_guide.md",
    QICODE / "01_core_overview.md": QICODE / "reference" / "core_overview.md",
    QICODE / "1.0_QiCode_Life_Protocol.md": QICODE / "sources" / "qicode_life_protocol.md",
    QICODE / "00_principles.md": QISPARK / "90_legacy_doctrine" / "founding_principles_legacy.md",
    QICODE / "1.01_Core_Principles.md": QISPARK / "90_legacy_doctrine" / "core_principles_legacy.md",
    QICODE / "QiEOS_Protocol_v3.0.md": QISPARK / "90_legacy_doctrine" / "qieos_protocol_v3_legacy.md",
    QICODE / "QiSuite_Dev_Bible.md": QISPARK / "90_legacy_doctrine" / "qisuite_dev_bible_legacy.md",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def backup(path: Path) -> None:
    if not path.exists():
        return
    target = BACKUP / path.relative_to(ROOT)
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        shutil.copy2(path, target)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write(path: Path, text: str, rows: list[dict[str, str]], reason: str) -> None:
    backup(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")
    rows.append({"action": "rewrite", "path": rel(path), "reason": reason})


def fix_mojibake(text: str) -> str:
    try:
        repaired = text.encode("latin1").decode("utf-8")
        if repaired.count("�") <= text.count("�"):
            text = repaired
    except UnicodeEncodeError:
        pass

    replacements = {
        "â€“": "-",
        "â€”": "-",
        "â†’": "->",
        "â€™": "'",
        "â€˜": "'",
        "â€œ": '"',
        "â€": '"',
        "â€": '"',
        "Ã—": "x",
        "Ï€": "pi",
        "Â·": "-",
        "Â": "",
        "ðŸ“Œ": "",
        "ðŸ”§": "",
        "âš™ï¸": "",
        "âœ…": "",
        "ðŸ”": "",
        "ðŸ§±": "",
        "ðŸŒ": "",
        "ðŸ”®": "",
        "ðŸ§ ": "",
        "âœï¸": "",
        "â„¢": "(TM)",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def normalize_front_matter(text: str, status: str, tags: list[str], summary: str | None = None) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---", 4)
    if end == -1:
        return text
    front = text[4:end].strip()
    body = text[end + 4 :].lstrip()

    def set_scalar(block: str, key: str, value: str) -> str:
        line = f'{key}: "{value}"' if key == "updated_at" else f"{key}: {value}"
        if re.search(rf"^{re.escape(key)}:", block, flags=re.MULTILINE):
            return re.sub(rf"^{re.escape(key)}:.*$", line, block, flags=re.MULTILINE)
        return block.rstrip() + "\n" + line

    front = set_scalar(front, "status", status)
    front = set_scalar(front, "updated_at", TODAY)
    if summary is not None:
        front = set_scalar(front, "summary", summary)

    front = re.sub(
        r"^tags:\n(?:  - .+\n?)+",
        "tags:\n" + "".join(f"  - {tag}\n" for tag in tags),
        front,
        flags=re.MULTILINE,
    )
    return f"---\n{front.strip()}\n---\n{body}"


def rewrite_index() -> str:
    return f"""---
layout: section
title: QiCode
slug: qicode
summary: Personal life doctrine in legal-code style, with a bridge into QiSpark technical doctrine.
status: active
updated_at: "{TODAY}"
tags:
  - qicode
source_type: manual
---
# QiCode

QiCode is the citeable personal life doctrine for truth, identity, inner work, outer work, relationships, ethics, closure, and legacy. QiSpark begins after QiCode as the technical/dev doctrine that implements and supports the life doctrine.

## Citation Pattern

- Title: `QiCode Title 1`
- Article: `QiCode Title 1, Article 1`
- Section: `QiCode Sec. 1.01.010`
- Line: `QiCode Sec. 1.01.010, Line 1`

## Personal Doctrine

- [Title 1. My Truth and Source](title_01_truth/title_01_truth.md)
- [Title 2. Inner World and Self](title_02_self/title_02_self.md)
- [Title 3. Identity and Integrity](title_03_identity/title_03_identity.md)
- [Title 4. Mind and Will](title_04_mind/title_04_mind.md)
- [Title 5. Work, Creation, and Stewardship](title_05_work/title_05_work.md)
- [Title 6. People, Relations, and Exchange](title_06_people/title_06_people.md)
- [Title 7. Ethics, Responsibility, and Disclosure](title_07_ethics/title_07_ethics.md)
- [Title 8. Cycles, Closure, and Legacy](title_08_cycles_legacy/title_08_cycles_legacy.md)

## Technical Doctrine Bridge

- [Title 9. QiSpark Technical Doctrine Bridge](title_09_qispark_bridge/title_09_qispark_bridge.md)

## Reference

- [Core Overview](reference/core_overview.md)
- [Citation Guide](reference/citation_guide.md)
- [Personal Source: QiCode Life Protocol](sources/qicode_life_protocol.md)
- [QiSpark Legacy Doctrine Sources](../10_QiSpark/90_legacy_doctrine/_index.md)

## QiSpark Technical Doctrine

- [QiSpark System](../10_QiSpark/_index.md)
- [QiServer](../10_QiSpark/20_QiServer/_index.md)
- [QiMemory](../10_QiSpark/30_QiMemory/_index.md)
- [QiConnect](../10_QiSpark/50_QiConnect/_index.md)
"""


def rewrite_core_overview(text: str) -> str:
    text = fix_mojibake(text)
    text = normalize_front_matter(
        text,
        "active",
        ["qicode"],
        "Overview of QiCode as personal life doctrine with a technical bridge into QiSpark.",
    )
    text = text.replace("[QiCode Index](10_qispark/00_QiCode/_index.md)", "[QiCode Index](../_index.md)")
    text = text.replace("[Citation Guide](10_qispark/00_QiCode/citation_guide.md)", "[Citation Guide](citation_guide.md)")
    text = text.replace("[QiSpark System](10_qispark/10_QiSpark/_index.md)", "[QiSpark System](../../10_QiSpark/_index.md)")
    text = text.replace("[QiServer](10_qispark/01_QiInfra-Global/20_QiServer/_index.md)", "[QiServer](../../10_QiSpark/20_QiServer/_index.md)")
    text = text.replace("[QiMemory](10_qispark/01_QiInfra-Global/20_QiServer/30_QiMemory/_index.md)", "[QiMemory](../../10_QiSpark/30_QiMemory/_index.md)")
    text = text.replace("[QiConnect](10_qispark/01_QiInfra-Global/20_QiServer/50_QiConnect/_index.md)", "[QiConnect](../../10_QiSpark/50_QiConnect/_index.md)")
    return text


def rewrite_citation_guide(text: str) -> str:
    text = fix_mojibake(text)
    return normalize_front_matter(
        text,
        "active",
        ["qicode"],
        "Reference syntax for citing QiCode personal-doctrine provisions.",
    )


def rewrite_personal_source(text: str) -> str:
    text = fix_mojibake(text)
    text = normalize_front_matter(
        text,
        "source",
        ["qicode", "personal-doctrine", "source-material"],
        "Personal source doctrine that most strongly influences the active QiCode titles.",
    )
    text = text.replace("title: QiCode Life Protocol - Realm 1", "title: QiCode Life Protocol")
    text = text.replace("# QiCode Life Protocol - Realm 1", "# QiCode Life Protocol")
    return text


def rewrite_legacy_dev_source(text: str) -> str:
    text = fix_mojibake(text)
    text = normalize_front_matter(
        text,
        "legacy-reference",
        ["qispark", "legacy-doctrine", "source-material"],
        "Legacy technical doctrine retained as source material for QiSpark updates.",
    )
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (`legacy path: \2`)", text)
    return text


def rewrite_title_cross_refs(path: Path) -> str:
    text = read(path)
    text = text.replace("[QiCode Index](10_qispark/00_QiCode/_index.md)", "[QiCode Index](../_index.md)")
    text = text.replace("[Citation Guide](10_qispark/00_QiCode/citation_guide.md)", "[Citation Guide](../reference/citation_guide.md)")
    return text


def write_legacy_index() -> str:
    return f"""---
layout: section
title: QiSpark Legacy Doctrine Sources
slug: qispark-legacy-doctrine-sources
summary: Older technical doctrine retained as reference material for future QiSpark updates.
status: legacy-reference
updated_at: "{TODAY}"
tags:
  - qispark
  - legacy-doctrine
source_type: manual
---
# QiSpark Legacy Doctrine Sources

These files are retained as source material for the current QiSpark technical doctrine. They are not the active QiCode personal doctrine.

## Source Files

- [Founding Principles Legacy](founding_principles_legacy.md)
- [Core Principles Legacy](core_principles_legacy.md)
- [QiEOS Protocol v3 Legacy](qieos_protocol_v3_legacy.md)
- [QiSuite Dev Bible Legacy](qisuite_dev_bible_legacy.md)
"""


def rewrite_qispark_index(text: str) -> str:
    text = text.replace("[QiCode](10_qispark/00_QiCode/_index.md)", "[QiCode](../00_QiCode/_index.md)")
    text = text.replace("[Policies](10_Policies/_index.md)", "[Policies](10_QiOS/10_Policies/_index.md)")
    text = text.replace("[Rules](20_Rules/_index.md)", "[Rules](10_QiOS/20_Rules/_index.md)")
    text = text.replace("[Standards](30_Standards/110_front_matter.md)", "[Standards](10_QiOS/30_Standards/110_front_matter.md)")
    text = text.replace("[Structure](40_Structure/_index.md)", "[Structure](10_QiOS/40_Structure/_index.md)")
    text = text.replace("[Metadata](50_metadata/_metadata.md)", "[Metadata](10_QiOS/50_metadata/_metadata.md)")
    text = text.replace("[Decisions](60_decisions/_Decisions.md)", "[Decisions](10_QiOS/60_decisions/_Decisions.md)")
    text = text.replace("[Registries](70_registries/_index.md)", "[Registries](10_QiOS/70_registries/_index.md)")
    text = text.replace("[Schemas](80_schemas/90_schema.md)", "[Schemas](10_QiOS/80_schemas/90_schema.md)")
    text = text.replace("[Templates](90_Templates/_1.30_Templates.md)", "[Templates](10_QiOS/90_Templates/_1.30_Templates.md)")
    if "90_legacy_doctrine/_index.md" not in text:
        text = text.rstrip() + "\n- [Legacy Doctrine Sources](90_legacy_doctrine/_index.md)\n"
    text = re.sub(r'updated_at: "[^"]+"', f'updated_at: "{TODAY}"', text)
    return text


def main() -> int:
    rows: list[dict[str, str]] = []
    CLEANUP.mkdir(parents=True, exist_ok=True)

    for source, target in MOVE_MAP.items():
        if source.exists():
            backup(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                backup(target)
                target.unlink()
            shutil.move(str(source), str(target))
            rows.append({"action": "move", "path": f"{rel(source)} -> {rel(target)}", "reason": "QiCode root should only expose the index."})

    write(QICODE / "_index.md", rewrite_index(), rows, "Root index is the single active root file and points to moved sources.")
    write(QICODE / "reference" / "core_overview.md", rewrite_core_overview(read(QICODE / "reference" / "core_overview.md")), rows, "Moved overview into reference and fixed technical links.")
    write(QICODE / "reference" / "citation_guide.md", rewrite_citation_guide(read(QICODE / "reference" / "citation_guide.md")), rows, "Moved citation guide into reference.")
    write(QICODE / "sources" / "qicode_life_protocol.md", rewrite_personal_source(read(QICODE / "sources" / "qicode_life_protocol.md")), rows, "Moved personal doctrine source under QiCode sources.")

    for path in sorted((QISPARK / "90_legacy_doctrine").glob("*.md")):
        if path.name != "_index.md":
            write(path, rewrite_legacy_dev_source(read(path)), rows, "Marked outdated dev doctrine as QiSpark legacy source material.")

    write(QISPARK / "90_legacy_doctrine" / "_index.md", write_legacy_index(), rows, "Added index for moved QiSpark legacy doctrine sources.")
    write(QISPARK / "_index.md", rewrite_qispark_index(read(QISPARK / "_index.md")), rows, "Linked QiSpark to legacy doctrine source material.")

    for path in sorted(QICODE.glob("title_*/*.md")):
        write(path, rewrite_title_cross_refs(path), rows, "Updated title cross references after moving citation guide.")

    with REPORT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["action", "path", "reason"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"actions={len(rows)}")
    print(f"report={REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
