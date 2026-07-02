from __future__ import annotations

import csv
import shutil
from datetime import date
from pathlib import Path


ROOT = Path.cwd()
QICODE = ROOT / "10_qispark" / "10_QiSpark" / "00_QiCode"
STAMP = f"cleanup_{date.today().isoformat()}_qicode"
CLEANUP = ROOT / "_qiconfig" / STAMP
BACKUP = CLEANUP / "backups_before_qicode_legal_style"
REVIEW = CLEANUP / "moved_review"
REPORT = CLEANUP / "qicode_legal_style_manifest.csv"


TITLES = [
    {
        "old": "1.21_Title_Foundations",
        "folder": "title_01_foundations",
        "file": "title_01_foundations.md",
        "code": "T01",
        "name": "Foundations",
        "summary": "The basic authority, purpose, scope, and interpretive rules of the QiCode.",
        "articles": [
            (
                "A01",
                "Authority and Scope",
                [
                    ("S010", "Purpose", "The QiCode gives durable language to the operating principles of the Qi system and the person using it."),
                    ("S020", "Scope", "The QiCode governs personal operations, system design, records, automation, review, and disclosure boundaries."),
                    ("S030", "Interpretation", "When a rule is unclear, interpret it toward clarity, preservation, humane pacing, and source-grounded action."),
                ],
            ),
            (
                "A02",
                "Source of Truth",
                [
                    ("S010", "Canonical Records", "Truth is held by the most direct and maintained record, not by summaries, dashboards, or generated views."),
                    ("S020", "Derived Material", "AI outputs, dashboards, and indexes may assist navigation but do not override source records."),
                    ("S030", "Conflict Rule", "When two records conflict, preserve both, identify the conflict, and resolve through evidence rather than deletion."),
                ],
            ),
            (
                "A03",
                "Operating Presumptions",
                [
                    ("S010", "Plain Language", "Rules should be readable by a tired human before they are optimized for machines."),
                    ("S020", "Stable References", "Important provisions should be citeable by title, article, section, and line."),
                    ("S030", "Minimum Necessary Structure", "Add structure only when it improves retrieval, safety, or action."),
                ],
            ),
        ],
    },
    {
        "old": "1.22_Title_Self_and_Inner_Work",
        "folder": "title_02_self",
        "file": "title_02_self.md",
        "code": "T02",
        "name": "Self and Inner Work",
        "summary": "Rules for self-trust, nervous-system care, reflection, repair, and sustainable self-governance.",
        "articles": [
            (
                "A01",
                "Self-Knowledge",
                [
                    ("S010", "Self-Observation", "Observation is allowed before judgment; the system should help notice patterns without turning them into verdicts."),
                    ("S020", "Needs and Limits", "A need, limit, or capacity constraint is recordable as operational context, not as failure."),
                    ("S030", "Identity Boundary", "No temporary state may be treated as the whole identity of the person."),
                ],
            ),
            (
                "A02",
                "Regulation and Care",
                [
                    ("S010", "Pacing", "Work should be broken into survivable units when overload is present."),
                    ("S020", "Repair", "Repair actions should be concrete, kind, and smaller than the shame response wants them to be."),
                    ("S030", "Rest", "Rest is a maintenance operation and may be scheduled, protected, and logged as such."),
                ],
            ),
            (
                "A03",
                "Reflection Records",
                [
                    ("S010", "Private Reflection", "Private reflection may be preserved without being promoted into public record."),
                    ("S020", "Reframing", "A reframe should keep the facts while reducing distortion, collapse, or self-erasure."),
                    ("S030", "Continuity", "Notes about self-understanding should remain linkable across time without forcing premature conclusions."),
                ],
            ),
        ],
    },
    {
        "old": "1.23_Title_Work_and_Creation",
        "folder": "title_03_work",
        "file": "title_03_work.md",
        "code": "T03",
        "name": "Work and Creation",
        "summary": "Rules for projects, creative work, value production, documentation, and delivery.",
        "articles": [
            (
                "A01",
                "Project Formation",
                [
                    ("S010", "Project Home", "Every active project should have one clear home, one purpose statement, and one next-action surface."),
                    ("S020", "Scope", "A project should distinguish active work, reference material, outputs, and archive material."),
                    ("S030", "Completion", "Completion means the intended user can find and use the result without reconstructing hidden context."),
                ],
            ),
            (
                "A02",
                "Creation Standards",
                [
                    ("S010", "Useful First", "A created artifact should be useful before it is ornamental."),
                    ("S020", "Evidence of Work", "Important work should leave a record of decisions, assumptions, and handoff state."),
                    ("S030", "Iteration", "A draft may exist as a draft, but its status must be visible."),
                ],
            ),
            (
                "A03",
                "Outputs",
                [
                    ("S010", "Output Home", "Generated reports, packets, exports, and deliverables belong in an output or project-specific export area."),
                    ("S020", "Audience", "An output should name or imply its intended audience before it is sent."),
                    ("S030", "Reuse", "Reusable artifacts should be turned into templates only after repeated need is observed."),
                ],
            ),
        ],
    },
    {
        "old": "1.24_Title_Relations_and_Exchange",
        "folder": "title_04_relations",
        "file": "title_04_relations.md",
        "code": "T04",
        "name": "Relations and Exchange",
        "summary": "Rules for people, roles, communication, obligations, exchange, and boundaries.",
        "articles": [
            (
                "A01",
                "People and Roles",
                [
                    ("S010", "Person Record", "A person may be referenced by role, relationship, or contact record, but the distinction should remain clear."),
                    ("S020", "Role Limits", "A role describes a context of interaction and must not flatten the whole person."),
                    ("S030", "Directory Hygiene", "Contact information should be separated from narrative interpretation where possible."),
                ],
            ),
            (
                "A02",
                "Communication",
                [
                    ("S010", "Message Context", "Important messages should preserve date, sender, receiver, medium, and surrounding context."),
                    ("S020", "Tone and Fact", "Tone may be described, but factual claims and emotional interpretation should be distinguishable."),
                    ("S030", "Response Readiness", "Draft replies should be marked as drafts until deliberately sent."),
                ],
            ),
            (
                "A03",
                "Exchange and Obligation",
                [
                    ("S010", "Ledger Principle", "Money, labor, care, and time can be recorded without reducing relationship to transaction."),
                    ("S020", "Consent", "Obligations should not be inferred from pressure, panic, or role confusion without review."),
                    ("S030", "Boundary", "A boundary is valid when it protects safety, capacity, truth, or dignity."),
                ],
            ),
        ],
    },
    {
        "old": "1.25_Title_Action_and_Automation",
        "folder": "title_05_action",
        "file": "title_05_action.md",
        "code": "T05",
        "name": "Action and Automation",
        "summary": "Rules for tasks, workflows, automation, agents, triggers, and review loops.",
        "articles": [
            (
                "A01",
                "Action Units",
                [
                    ("S010", "Next Action", "A next action should be concrete enough to do without solving the whole project again."),
                    ("S020", "Task State", "Tasks should expose status, owner, due context, and blocking condition when those are known."),
                    ("S030", "Review", "A stale task should be reviewed before it is silently carried forward."),
                ],
            ),
            (
                "A02",
                "Automation Authority",
                [
                    ("S010", "Human Override", "Automation may assist but must leave room for human correction and pause."),
                    ("S020", "Traceability", "Automated moves, edits, or summaries should leave a manifest or log when they affect records."),
                    ("S030", "Safety", "Automation must not delete, disclose, or overwrite sensitive material without an explicit rule."),
                ],
            ),
            (
                "A03",
                "Agents and Tools",
                [
                    ("S010", "Tool Fit", "Use the simplest reliable tool that preserves the record and completes the job."),
                    ("S020", "Agent Scope", "Agents should operate inside a named scope with visible assumptions."),
                    ("S030", "Verification", "Agent output should be verified before it becomes source material."),
                ],
            ),
        ],
    },
    {
        "old": "1.26_Title_Identity_and_Integrity",
        "folder": "title_06_identity",
        "file": "title_06_identity.md",
        "code": "T06",
        "name": "Identity and Integrity",
        "summary": "Rules for identity, canonical references, provenance, integrity, and non-contradiction.",
        "articles": [
            (
                "A01",
                "Identity",
                [
                    ("S010", "Canonical Identity", "Each important object should have one canonical identity and may have many aliases."),
                    ("S020", "Aliases", "Aliases help retrieval but must not create competing truth sources."),
                    ("S030", "Local Identity", "A local note ID may support navigation without pretending to be database truth."),
                ],
            ),
            (
                "A02",
                "Integrity",
                [
                    ("S010", "Preservation", "Original records should be preserved when transformed, summarized, or exported."),
                    ("S020", "Lineage", "A transformed record should be traceable back to its source when practical."),
                    ("S030", "Correction", "Corrections should be explicit rather than silently rewriting history."),
                ],
            ),
            (
                "A03",
                "Contradiction Handling",
                [
                    ("S010", "Conflict Capture", "Contradictions should be captured as conflicts, not erased."),
                    ("S020", "Resolution", "Resolution requires evidence, decision, or status change."),
                    ("S030", "Unresolved State", "Unresolved is an allowed state when the evidence is incomplete."),
                ],
            ),
        ],
    },
    {
        "old": "1.27_Title_Mind_and_Will",
        "folder": "title_07_mind",
        "file": "title_07_mind.md",
        "code": "T07",
        "name": "Mind and Will",
        "summary": "Rules for attention, intention, decisions, planning, and cognitive load.",
        "articles": [
            (
                "A01",
                "Attention",
                [
                    ("S010", "Capture Before Sort", "When attention is overloaded, capture first and sort later."),
                    ("S020", "Context Limits", "A workspace should reduce open loops rather than multiplying them."),
                    ("S030", "Focus", "Focus work should name the object, the outcome, and the stop condition."),
                ],
            ),
            (
                "A02",
                "Decision",
                [
                    ("S010", "Decision Record", "Important decisions should preserve context, options, choice, and consequence."),
                    ("S020", "Reversibility", "A decision should note whether it is reversible, hard to reverse, or final."),
                    ("S030", "Delay", "Delay may be a valid decision when information, capacity, or safety is missing."),
                ],
            ),
            (
                "A03",
                "Will and Commitment",
                [
                    ("S010", "Commitment Fit", "A commitment should match actual capacity and known constraints."),
                    ("S020", "Renegotiation", "Renegotiating a commitment is better than silently failing it."),
                    ("S030", "Agency", "The system should increase agency, not punish the person for needing structure."),
                ],
            ),
        ],
    },
    {
        "old": "1.28_Title_Cycles_and_Closure",
        "folder": "title_08_cycles",
        "file": "title_08_cycles.md",
        "code": "T08",
        "name": "Cycles and Closure",
        "summary": "Rules for review cycles, completion, archiving, closure, and renewal.",
        "articles": [
            (
                "A01",
                "Cycles",
                [
                    ("S010", "Review Cycle", "Active systems need periodic review to prevent quiet drift."),
                    ("S020", "Cadence", "A cadence should be light enough to survive real life."),
                    ("S030", "Reset", "A reset is a legitimate maintenance action when the system becomes too heavy."),
                ],
            ),
            (
                "A02",
                "Closure",
                [
                    ("S010", "Completion Record", "Closed work should say what was done, where the result lives, and what remains open."),
                    ("S020", "Archive Rule", "Archive material should stay findable without crowding active space."),
                    ("S030", "Loose Ends", "Loose ends should be listed rather than hidden inside memory."),
                ],
            ),
            (
                "A03",
                "Renewal",
                [
                    ("S010", "Retrospective", "A retrospective should extract learning without reopening every wound."),
                    ("S020", "Supersession", "Superseded material should point to the active replacement."),
                    ("S030", "Continuity", "Closure should preserve continuity for the future self returning later."),
                ],
            ),
        ],
    },
    {
        "old": "1.29_Title_Ethics_and_Evolution",
        "folder": "title_09_ethics",
        "file": "title_09_ethics.md",
        "code": "T09",
        "name": "Ethics and Evolution",
        "summary": "Rules for harm reduction, privacy, fairness, consent, and responsible system evolution.",
        "articles": [
            (
                "A01",
                "Ethical Use",
                [
                    ("S010", "Minimum Necessary Disclosure", "Share only what is needed for the purpose, audience, and safety context."),
                    ("S020", "Dignity", "Records should preserve dignity even when documenting conflict or harm."),
                    ("S030", "Consent", "Consent and access boundaries should be explicit when material involves other people."),
                ],
            ),
            (
                "A02",
                "Safety",
                [
                    ("S010", "Sensitive Material", "Medical, legal, financial, and family-conflict material requires higher review before disclosure."),
                    ("S020", "Misuse Risk", "If a record can be easily misused, label it and route it carefully."),
                    ("S030", "Careful Automation", "Automation should not amplify harm, exposure, or mistaken certainty."),
                ],
            ),
            (
                "A03",
                "Evolution",
                [
                    ("S010", "Change Record", "System changes should be documented when they affect meaning, routing, or trust."),
                    ("S020", "Experiment", "Experiments should be named as experiments until accepted."),
                    ("S030", "Upgrade Rule", "Upgrades should reduce friction without erasing proven working patterns."),
                ],
            ),
        ],
    },
    {
        "old": "1.30_Title_Legacy_and_Design",
        "folder": "title_10_legacy",
        "file": "title_10_legacy.md",
        "code": "T10",
        "name": "Legacy and Design",
        "summary": "Rules for design continuity, inheritance, legacy material, and durable meaning.",
        "articles": [
            (
                "A01",
                "Design",
                [
                    ("S010", "Design Purpose", "Design should make the right action easier to see, choose, and complete."),
                    ("S020", "Coherence", "Names, folders, metadata, and interfaces should tell the same story."),
                    ("S030", "Simplicity", "A simpler structure is preferred when it preserves meaning and retrieval."),
                ],
            ),
            (
                "A02",
                "Legacy",
                [
                    ("S010", "Legacy Preservation", "Legacy material should be preserved when it contains context, lineage, or reusable thought."),
                    ("S020", "Legacy Quarantine", "Legacy material should not govern the active system unless promoted deliberately."),
                    ("S030", "Inheritance", "Useful legacy concepts may be inherited with attribution and updated placement."),
                ],
            ),
            (
                "A03",
                "Durability",
                [
                    ("S010", "Future Reader", "A future reader should be able to understand why the structure exists."),
                    ("S020", "Reference Stability", "Citations should survive file movement through indexes and stable code labels."),
                    ("S030", "Living Code", "The QiCode may evolve, but each change should make the code more useful, not merely more elaborate."),
                ],
            ),
        ],
    },
]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def backup_path(path: Path) -> None:
    if path.exists():
        target = BACKUP / path.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            shutil.copy2(path, target)


def write_file(path: Path, text: str, rows: list[dict[str, str]], action: str, reason: str) -> None:
    backup_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")
    rows.append({"action": action, "path": rel(path), "reason": reason})


def move_path(src: Path, dst: Path, rows: list[dict[str, str]], reason: str) -> None:
    if not src.exists():
        return
    if dst.exists():
        return
    backup_path(src) if src.is_file() else None
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    rows.append({"action": "move", "path": f"{rel(src)} -> {rel(dst)}", "reason": reason})


def frontmatter(title: str, slug: str, summary: str, layout: str = "section") -> str:
    return f"""---
layout: {layout}
title: {title}
slug: {slug}
summary: {summary}
status: active
updated_at: "{date.today().isoformat()}"
tags:
  - qispark
  - qicode
source_type: manual
---"""


def title_document(item: dict[str, object]) -> str:
    code = item["code"]
    name = item["name"]
    lines = [
        frontmatter(
            f"QiCode Title {code[1:]} - {name}",
            f"qicode-title-{code[1:].lower()}-{str(name).lower().replace(' ', '-')}",
            item["summary"],
        ),
        f"# QiCode Title {code[1:]} - {name}",
        "",
        "## Citation",
        "",
        f"- Title citation: `QiCode {code}`",
        f"- Section citation form: `QiCode {code}.A##.S###`",
        f"- Line citation form: `QiCode {code}.A##.S###.L###`",
        "",
        "## Rule of Construction",
        "",
        f"- `{code}.R001.L001` This title is part of the QiCode and should be read with the whole code.",
        f"- `{code}.R001.L002` A section states a governing principle; a line states a citeable rule or application.",
        f"- `{code}.R001.L003` If a provision conflicts with a more specific active project rule, preserve both and resolve by source, audience, and purpose.",
        "",
    ]
    for article_code, article_name, sections in item["articles"]:
        lines += [f"## Article {article_code[1:]} - {article_name} (`{code}.{article_code}`)", ""]
        for section_code, section_name, section_rule in sections:
            section_ref = f"{code}.{article_code}.{section_code}"
            lines += [
                f"### Section {section_code[1:]} - {section_name} (`{section_ref}`)",
                "",
                f"- `{section_ref}.L001` {section_rule}",
                f"- `{section_ref}.L002` Apply this section in a way that preserves clear ownership, durable records, and humane operational load.",
                f"- `{section_ref}.L003` Any exception should be named, reviewed, and linked to the record that justifies it.",
                "",
            ]
    lines += [
        "## Cross References",
        "",
        "- [QiCode Index](../_index.md)",
        "- [Citation Guide](../citation_guide.md)",
    ]
    return "\n".join(lines)


def index_document() -> str:
    rows = [
        frontmatter("QiCode", "qicode", "Legal-code style operating code for QiSpark/QiOS doctrine."),
        "# QiCode",
        "",
        "QiCode is the citeable operating code for the Qi system. It uses a legal-code style so ideas can be referenced by title, article, section, and line.",
        "",
        "## Citation Pattern",
        "",
        "- Title: `QiCode T01`",
        "- Article: `QiCode T01.A01`",
        "- Section: `QiCode T01.A01.S010`",
        "- Line: `QiCode T01.A01.S010.L001`",
        "",
        "## Titles",
        "",
    ]
    for item in TITLES:
        rows.append(f"- [`QiCode {item['code']}` - {item['name']}]({item['folder']}/{item['file']})")
    rows += [
        "",
        "## Reference Documents",
        "",
        "- [Citation Guide](citation_guide.md)",
        "- [Core Overview](01_core_overview.md)",
        "- [Founding Principles](00_principles.md)",
        "- [QiCode Life Protocol](1.0_QiCode_Life_Protocol.md)",
        "- [Core Principles Legacy](1.01_Core_Principles.md)",
        "- [QiEOS Protocol](QiEOS_Protocol_v3.0.md)",
        "- [QiSuite Dev Bible](QiSuite_Dev_Bible.md)",
    ]
    return "\n".join(rows)


def citation_guide() -> str:
    return f"""{frontmatter("QiCode Citation Guide", "qicode-citation-guide", "Reference syntax for citing QiCode provisions.", "page")}
# QiCode Citation Guide

## Hierarchy

- `T##` means Title.
- `A##` means Article.
- `S###` means Section.
- `L###` means Line.

## Examples

- `QiCode T01` cites Title 01, Foundations.
- `QiCode T01.A02` cites Title 01, Article 02, Source of Truth.
- `QiCode T01.A02.S020` cites the Derived Material section.
- `QiCode T01.A02.S020.L001` cites the first line of that section.

## Style Rules

- Use backticks around citations in prose.
- Keep section numbers stable once cited.
- Add new sections in increments of 10, such as `S010`, `S020`, and `S030`, so later inserts can fit between them.
- Use line numbers for provisions that may need exact reference in prompts, decisions, or review comments.
"""


def overview_document() -> str:
    return f"""{frontmatter("QiCode Core Overview", "qicode-core-overview", "Overview of the legal-code style QiCode structure.", "page")}
# QiCode Core Overview

QiCode is the legal-code style doctrine layer for QiSpark. It converts personal operating principles, system rules, and design doctrine into citeable provisions.

## What QiCode Does

- Gives major principles a stable home.
- Makes rules citeable by title, article, section, and line.
- Separates source doctrine from generated summaries.
- Gives agents and humans the same reference language.

## Active Code

- [QiCode Index](_index.md)
- [Citation Guide](citation_guide.md)

## Legacy Sources

The older protocol files remain as source and historical material. They may be incorporated into titles over time, but the active citation surface is the title structure listed in the index.
"""


def main() -> int:
    rows: list[dict[str, str]] = []
    CLEANUP.mkdir(parents=True, exist_ok=True)
    QICODE.mkdir(parents=True, exist_ok=True)

    empty_title = QICODE / "Title 1"
    if empty_title.exists():
        target = REVIEW / "empty_Title_1"
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.move(str(empty_title), str(target))
                rows.append({"action": "move", "path": f"{rel(empty_title)} -> {rel(target)}", "reason": "Moved empty placeholder title folder."})
            except OSError as exc:
                rows.append({"action": "skip_move", "path": rel(empty_title), "reason": f"Could not move empty placeholder title folder: {exc}"})

    for item in TITLES:
        old_dir = QICODE / item["old"]
        new_dir = QICODE / item["folder"]
        if old_dir.exists() and old_dir != new_dir:
            move_path(old_dir, new_dir, rows, "Renamed old title folder to simplified legal-code title folder.")
        new_dir.mkdir(parents=True, exist_ok=True)
        old_note = new_dir / f"_{item['old']}.md"
        if old_note.exists():
            target = REVIEW / "old_title_notes" / old_note.relative_to(QICODE)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(old_note), str(target))
            rows.append({"action": "move", "path": f"{rel(old_note)} -> {rel(target)}", "reason": "Moved placeholder title note before replacing with citeable title text."})
        write_file(new_dir / item["file"], title_document(item), rows, "write_title", f"Wrote citeable legal-code title {item['code']}.")

    write_file(QICODE / "_index.md", index_document(), rows, "write_index", "Created QiCode legal-code index.")
    write_file(QICODE / "citation_guide.md", citation_guide(), rows, "write_guide", "Created QiCode citation guide.")
    write_file(QICODE / "01_core_overview.md", overview_document(), rows, "write_overview", "Updated QiCode overview to point at active legal-code structure.")

    # Update nearby navigation surfaces.
    for rel_path in [
        Path("10_qispark/10_QiSpark/_index.md"),
        Path("10_qispark/10_QiSpark/10_QiSpark.md"),
    ]:
        path = ROOT / rel_path
        if path.exists():
            backup_path(path)
            text = path.read_text(encoding="utf-8", errors="ignore")
            text = text.replace("00_QiCode/01_core_overview.md", "00_QiCode/_index.md")
            path.write_text(text, encoding="utf-8", newline="\n")
            rows.append({"action": "update_link", "path": rel(path), "reason": "Pointed QiSpark navigation to QiCode index."})

    with REPORT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["action", "path", "reason"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"actions={len(rows)}")
    print(f"report={REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
