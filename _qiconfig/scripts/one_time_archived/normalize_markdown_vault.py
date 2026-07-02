from __future__ import annotations

import csv
import hashlib
import os
import re
import shutil
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


FIELD_ORDER = [
    "layout",
    "title",
    "slug",
    "summary",
    "status",
    "created_at",
    "updated_at",
    "author",
    "owner",
    "sensitivity",
    "classification",
    "realm_label",
    "context",
    "aliases",
    "tags",
    "keywords",
    "references",
    "target_system",
    "target_scope",
    "canonical_ref",
    "uid",
    "template_key",
    "source_type",
    "adr_id",
    "supersedes",
    "artifact_kind",
    "registry_key",
    "standard_key",
]

KNOWN_FIELDS = set(FIELD_ORDER)
TODAY = os.environ.get("QINOTES_UPDATED_AT", str(date.today()))


@dataclass
class Change:
    path: str
    actions: list[str]
    old_hash: str
    new_hash: str


def read_text(path: Path) -> str:
    data = path.read_bytes()
    if b"\x00" in data:
        # Common import artifact: sparse NULs before numeric path segments.
        data = data.replace(b"\x00", b"")
    text = data.decode("utf-8-sig", errors="replace")
    return text.replace("\r\n", "\n").replace("\r", "\n")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"['\"`]", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "untitled"


def title_from_name(path: Path) -> str:
    stem = path.stem
    if stem.lower() in {"readme", "_index", "index"}:
        stem = path.parent.name
    stem = re.sub(r"^[0-9]+[_ .-]*", "", stem)
    stem = stem.strip("_-. ")
    stem = stem.replace("_", " ").replace("-", " ")
    stem = re.sub(r"\s+", " ", stem).strip()
    if not stem:
        stem = path.parent.name.replace("_", " ")
    keep = {"QiOS", "QiSpark", "QiServer", "QiVault", "QiApps", "QiLife", "QiGina"}
    words = []
    for word in stem.split():
        words.append(word if word in keep else word[:1].upper() + word[1:])
    return " ".join(words)


def extract_h1(body: str) -> str | None:
    match = re.search(r"^#\s+(.+?)\s*$", body, re.M)
    if not match:
        return None
    title = match.group(1).strip()
    title = re.sub(r"\s+#*$", "", title)
    return title or None


def infer_layout(path: Path) -> str:
    name = path.name.lower()
    stem = path.stem.lower()
    parts = [p.lower() for p in path.parts]
    if path.as_posix() == "00_home/00_home.md":
        return "home"
    if "template" in stem or "_templates" in parts or "templates" in parts:
        return "template"
    if stem.startswith("adr-") or re.match(r"^\d{4}_", stem):
        if "decision" in path.as_posix().lower() or "adr" in stem:
            return "adr"
    if name in {"readme.md", "_index.md", "index.md"}:
        return "section"
    if stem == path.parent.name.lower():
        return "section"
    if "cleanup" in stem or "report" in stem or "export" in parts:
        return "artifact"
    return "page"


def infer_source_type(path: Path) -> str:
    parts = [p.lower() for p in path.parts]
    if any(p in parts for p in ["01_inbox", "02_daily", "cadence", "copilot", "tasknotes"]):
        return "imported"
    if "outputs" in parts or "50_outputs" in parts:
        return "generated"
    return "manual"


def infer_tags(path: Path, layout: str) -> list[str]:
    tags: list[str] = []
    if layout in {"home", "section"}:
        tags.append("moc")
    top = path.parts[0].lower() if path.parts else ""
    mapping = {
        "00_home": "home",
        "01_inbox": "inbox",
        "10_daily": "daily",
        "20_life": "life",
        "30_empowerqnow713": "EmpowerQNow713",
        "40_projects": "projects",
        "50_QiLabs": "QiLabs",
        "90_outputs": "outputs",
        "_qiconfig": "config",
        "Cadence": "cadence",
        "Copilot": "copilot",
        "TaskNotes": "tasknotes",
        "Templates": "Templates"
    }
    if top in mapping:
        tags.append(mapping[top])
    text = path.as_posix().lower()
    if "lisa_care_record_2026" in text:
        tags.append("lisa-care-record")
    if "dashboard" in path.stem.lower():
        tags.append("dashboard")
    if "decision" in text or "adr" in path.stem.lower():
        tags.append("decisions")
    return dedupe(tags)


def dedupe(values: list[str]) -> list[str]:
    seen = set()
    out = []
    for value in values:
        value = value.strip()
        if not value:
            continue
        key = value.lower()
        if key not in seen:
            seen.add(key)
            out.append(value)
    return out


def split_frontmatter(text: str) -> tuple[dict[str, object], list[str], str, bool]:
    if not text.startswith("---\n"):
        return {}, [], text, False
    match = re.search(r"\n---\s*\n", text)
    if not match:
        return {}, [], text, False
    raw = text[4 : match.start()]
    body = text[match.end() :]
    data: dict[str, object] = {}
    extra_order: list[str] = []
    current_key: str | None = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        list_item = re.match(r"^\s*-\s+(.+?)\s*$", line)
        if list_item and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(clean_scalar(list_item.group(1)))
            continue
        key_match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", line)
        if not key_match:
            continue
        key, value = key_match.group(1), key_match.group(2)
        current_key = key
        if key not in KNOWN_FIELDS:
            extra_order.append(key)
        if value == "":
            data[key] = [] if key in {"tags", "aliases", "keywords", "references"} else ""
        elif value == "[]":
            data[key] = []
        elif value.startswith("[") and value.endswith("]"):
            items = [clean_scalar(v) for v in value.strip("[]").split(",")]
            data[key] = [v for v in items if v]
        else:
            if key in {"tags", "aliases", "keywords", "references"}:
                data[key] = [clean_tag(clean_scalar(value))]
            else:
                data[key] = clean_scalar(value)
    return data, extra_order, body, True


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value.strip()


def clean_tag(value: str) -> str:
    value = clean_scalar(value)
    value = value.lstrip("#")
    if value == "MOCs":
        value = "moc"
    value = value.replace(" ", "-")
    return value


def quote_yaml(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def render_frontmatter(data: dict[str, object], extra_order: list[str] | None = None) -> str:
    lines = ["---"]
    rendered = set()
    ordered_keys = FIELD_ORDER + [key for key in (extra_order or []) if key not in FIELD_ORDER]
    ordered_keys += sorted(key for key in data if key not in ordered_keys)
    for key in ordered_keys:
        if key not in data:
            continue
        rendered.add(key)
        value = data[key]
        if value in (None, ""):
            continue
        if isinstance(value, list):
            value = dedupe([clean_tag(str(v)) if key == "tags" else str(v).strip() for v in value])
            if not value:
                continue
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            value = str(value).strip()
            if key in {"created_at", "updated_at"} and re.match(r"^\d{4}-\d{2}-\d{2}$", value):
                lines.append(f'{key}: "{value}"')
            elif re.search(r"[:#\\[\\]{}&,*!|>'\"%@`]", value) or value.lower() in {"yes", "no", "true", "false", "null"}:
                lines.append(f"{key}: {quote_yaml(value)}")
            else:
                lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def normalize_body(body: str, title: str) -> tuple[str, list[str]]:
    actions: list[str] = []
    body = body.replace("\ufeff", "")
    body = re.sub(r"[ \t]+$", "", body, flags=re.M)
    body = re.sub(r"\n{4,}", "\n\n\n", body)

    lines = body.lstrip("\n").splitlines()
    while lines and lines[0].strip() == "---":
        lines.pop(0)
        actions.append("removed_body_hr_after_frontmatter")
    body = "\n".join(lines).strip("\n")

    h1 = extract_h1(body)
    if not h1:
        body = f"# {title}\n\n{body}".rstrip()
        actions.append("added_h1")
    else:
        # Collapse duplicate first two H1s caused by earlier import cleanup passes.
        split = body.splitlines()
        h1_indexes = [i for i, line in enumerate(split[:30]) if line.startswith("# ")]
        if len(h1_indexes) >= 2:
            first = re.sub(r"^#\s+", "", split[h1_indexes[0]]).strip()
            second = re.sub(r"^#\s+", "", split[h1_indexes[1]]).strip()
            if first.lower() == second.lower():
                del split[h1_indexes[1]]
                body = "\n".join(split)
                actions.append("removed_duplicate_h1")

    body = re.sub(r"\n(#{1,6}\s+[^\n]+)\n(?!\n)", r"\n\1\n\n", body)
    body = re.sub(r"(?<!\n)\n(#{1,6}\s+)", r"\n\n\1", body)
    body = re.sub(r"\n{4,}", "\n\n\n", body)
    return body.strip() + "\n", actions


def normalize_file(path: Path, root: Path) -> tuple[str, list[str]] | None:
    original = read_text(path)
    data, extra_order, body, had_fm = split_frontmatter(original.lstrip("\ufeff"))
    actions: list[str] = []
    if not had_fm:
        actions.append("added_frontmatter")
    elif extra_order:
        actions.append("preserved_extra_frontmatter")

    title = str(data.get("title") or extract_h1(body) or title_from_name(path))
    layout = str(data.get("layout") or infer_layout(path))
    tags = []
    if isinstance(data.get("tags"), list):
        tags.extend([clean_tag(str(v)) for v in data["tags"]])
    tags.extend(infer_tags(path.relative_to(root), layout))

    data.update(
        {
            "layout": layout,
            "title": title,
            "slug": str(data.get("slug") or slugify(title)),
            "status": str(data.get("status") or "active"),
            "updated_at": str(data.get("updated_at") or TODAY),
            "tags": dedupe(tags),
            "source_type": str(data.get("source_type") or infer_source_type(path.relative_to(root))),
        }
    )
    if layout == "artifact" and not data.get("artifact_kind"):
        data["artifact_kind"] = "report" if "report" in path.stem.lower() or "cleanup" in path.stem.lower() else "document"

    frontmatter = render_frontmatter(data, extra_order)
    new_body, body_actions = normalize_body(body, title)
    actions.extend(body_actions)
    normalized = f"{frontmatter}\n{new_body}"
    if normalized != original:
        if had_fm:
            actions.append("normalized_frontmatter")
        return normalized, dedupe(actions)
    return None


def iter_markdown(root: Path) -> list[Path]:
    skip_parts = {".obsidian"}
    files: list[Path] = []
    for path in root.rglob("*.md"):
        rel_parts = path.relative_to(root).parts
        if any(part in skip_parts for part in rel_parts):
            continue
        if len(rel_parts) >= 2 and rel_parts[0] == "_qiconfig" and rel_parts[1].startswith("cleanup_"):
            continue
        if rel_parts[:2] == ("_qiconfig", "scripts"):
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    root = Path.cwd()
    stamp = os.environ.get("QINOTES_CLEANUP_STAMP", f"frontmatter_{TODAY}")
    cleanup = root / "_qiconfig" / stamp
    backup_dir = cleanup / "backups_before_frontmatter"
    cleanup.mkdir(parents=True, exist_ok=True)
    report_path = cleanup / "frontmatter_formatting_report.csv"

    dry_run = "--dry-run" in sys.argv
    changes: list[Change] = []
    for path in iter_markdown(root):
        result = normalize_file(path, root)
        if not result:
            continue
        normalized, actions = result
        original = read_text(path)
        if not dry_run:
            backup_path = backup_dir / path.relative_to(root)
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            if not backup_path.exists():
                shutil.copy2(path, backup_path)
            write_text(path, normalized)
        changes.append(Change(str(path.relative_to(root)), actions, sha(original), sha(normalized)))

    with report_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["path", "actions", "old_hash", "new_hash"])
        writer.writeheader()
        for change in changes:
            writer.writerow(
                {
                    "path": change.path,
                    "actions": ";".join(change.actions),
                    "old_hash": change.old_hash,
                    "new_hash": change.new_hash,
                }
            )

    print(f"dry_run={dry_run}")
    print(f"changed_files={len(changes)}")
    print(f"report={report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
