from __future__ import annotations

import csv
import shutil
from pathlib import Path


ROOT = Path.cwd()
QICODE = ROOT / "10_qispark" / "10_QiSpark" / "00_QiCode"
CLEANUP = ROOT / "_qiconfig" / "cleanup_2026-06-29_qicode_personal"
BACKUP = CLEANUP / "backups_before_personal_qicode"
REVIEW = CLEANUP / "moved_review"
REPORT = CLEANUP / "qicode_personal_doctrine_manifest.csv"
TODAY = "2026-06-29"


TITLES = [
    {
        "folder": "title_01_truth",
        "file": "title_01_truth.md",
        "code": "T01",
        "name": "My Truth and Source",
        "summary": "The source doctrine of QiCode: truth, unity, EmpowerQNow, and the personal law that everything else must serve.",
        "articles": [
            ("A01", "My Truth", [
                ("S010", "Truth Before Performance", "My truth is not a performance, brand posture, or argument strategy; it is the record of what I know, live, observe, and choose to stand inside."),
                ("S020", "Witness", "I may witness my life directly before translating it for another person's comfort, system, or category."),
                ("S030", "Non-Erasure", "No institution, relationship, crisis, or diagnosis may erase the continuity of my lived truth."),
            ]),
            ("A02", "Law of One", [
                ("S010", "Unity", "The Law of One is held here as a unity principle: separation is useful for navigation, but not ultimate truth."),
                ("S020", "Service", "Service must not require self-abandonment; true service preserves dignity, consent, and source alignment."),
                ("S030", "Discernment", "Unity does not mean collapse of boundaries; discernment is how unity becomes safe in daily life."),
            ]),
            ("A03", "EmpowerQNow", [
                ("S010", "Empowerment", "EmpowerQNow is the public-facing current of this doctrine: truth turned toward empowerment, language, repair, and liberation."),
                ("S020", "Voice", "The voice of EmpowerQNow should be clear, grounded, and unwilling to confuse survival with failure."),
                ("S030", "Transmission", "Any teaching, post, guide, or creative work from this source should return power to the reader rather than creating dependence."),
            ]),
        ],
    },
    {
        "folder": "title_02_self",
        "file": "title_02_self.md",
        "code": "T02",
        "name": "Inner World and Self",
        "summary": "The inner-life doctrine for selfhood, care, nervous-system truth, and spiritual/emotional steadiness.",
        "articles": [
            ("A01", "Self-Recognition", [
                ("S010", "Self-Contact", "I must be able to locate myself before I can responsibly respond to others."),
                ("S020", "Need", "A need is information, not evidence of weakness."),
                ("S030", "Capacity", "Capacity is a fact of the moment and must be designed around rather than denied."),
            ]),
            ("A02", "Inner Care", [
                ("S010", "Regulation", "Regulation is not repression; it is the practice of returning enough agency to choose the next honest step."),
                ("S020", "Rest", "Rest is a lawful maintenance act within QiCode and does not require moral defense."),
                ("S030", "Repair", "Repair begins with truthful naming, then moves toward the smallest viable restoration."),
            ]),
            ("A03", "Sacred Interior", [
                ("S010", "Privacy", "Not every inner truth is public material, even when it is real."),
                ("S020", "Discernment", "Inner guidance should be recorded with humility and checked against care, reality, and consequence."),
                ("S030", "Integration", "Inner work becomes useful when it changes action, language, boundaries, or peace."),
            ]),
        ],
    },
    {
        "folder": "title_03_identity",
        "file": "title_03_identity.md",
        "code": "T03",
        "name": "Identity and Integrity",
        "summary": "The doctrine of identity, naming, self-definition, boundaries, and non-contradiction.",
        "articles": [
            ("A01", "Identity", [
                ("S010", "Self-Definition", "I retain the right to define myself in language that is precise, alive, and not reduced to someone else's fear."),
                ("S020", "Multiplicity", "Different roles, moods, capacities, and histories may coexist without becoming fraud or contradiction."),
                ("S030", "Naming", "Names, labels, and aliases should clarify relationship and context without replacing the living person."),
            ]),
            ("A02", "Integrity", [
                ("S010", "Alignment", "Integrity means the visible life and the known inner truth are brought into closer alignment over time."),
                ("S020", "Record", "When identity is challenged or mischaracterized, records should preserve context rather than retaliatory distortion."),
                ("S030", "Correction", "Correction is lawful when it restores truth without unnecessary exposure."),
            ]),
            ("A03", "Boundaries", [
                ("S010", "Boundary Validity", "A boundary is valid when it protects safety, truth, capacity, dignity, or consent."),
                ("S020", "Access", "Access to me, my labor, my attention, or my records is not automatically granted by proximity or urgency."),
                ("S030", "Enforcement", "A boundary without enforcement becomes a request; enforcement may be calm, documented, and proportionate."),
            ]),
        ],
    },
    {
        "folder": "title_04_mind",
        "file": "title_04_mind.md",
        "code": "T04",
        "name": "Mind and Will",
        "summary": "The doctrine of attention, cognition, will, decisions, overload, and executive reality.",
        "articles": [
            ("A01", "Attention", [
                ("S010", "Capture Before Sort", "When attention is overloaded, capture first and sort later."),
                ("S020", "Focus", "Focus requires a named object, a realistic scope, and permission to stop."),
                ("S030", "Noise", "Noise should be reduced at the system level rather than treated only as personal discipline failure."),
            ]),
            ("A02", "Decision", [
                ("S010", "Decision Record", "Important decisions should preserve context, options, choice, and consequence."),
                ("S020", "Delay", "Delay may be lawful when information, safety, or capacity is missing."),
                ("S030", "Reversibility", "A decision should name whether it is reversible, difficult to reverse, or final."),
            ]),
            ("A03", "Will", [
                ("S010", "Agency", "Will is not brute force; will is aligned choice with enough structure to survive friction."),
                ("S020", "Commitment", "A commitment must be sized to actual capacity, not fantasy capacity."),
                ("S030", "Renegotiation", "Renegotiating a commitment is more truthful than silently collapsing under it."),
            ]),
        ],
    },
    {
        "folder": "title_05_work",
        "file": "title_05_work.md",
        "code": "T05",
        "name": "Work, Creation, and Stewardship",
        "summary": "The outer-work doctrine for projects, creation, service, craft, money, and stewardship.",
        "articles": [
            ("A01", "Work", [
                ("S010", "Project Home", "Every serious project should have one clear home, one purpose, and one visible next-action surface."),
                ("S020", "Labor Record", "Labor that costs time, income, health, or opportunity may be recorded without shame."),
                ("S030", "Completion", "Completion means the intended user can find and use the result without reconstructing hidden context."),
            ]),
            ("A02", "Creation", [
                ("S010", "Useful First", "A created artifact should be useful before it is ornamental."),
                ("S020", "Voice", "Creative work may carry personal truth while still being edited for audience, safety, and form."),
                ("S030", "Output", "Outputs should name their audience, status, and intended next use."),
            ]),
            ("A03", "Stewardship", [
                ("S010", "Resources", "Money, tools, records, systems, and energy are stewardship objects and should be treated with care."),
                ("S020", "Sustainability", "Work that destroys the worker is not a stable operating model."),
                ("S030", "Value", "Value includes money, care, time, skill, meaning, continuity, and repair."),
            ]),
        ],
    },
    {
        "folder": "title_06_people",
        "file": "title_06_people.md",
        "code": "T06",
        "name": "People, Relations, and Exchange",
        "summary": "The relational doctrine for people, roles, communication, care, exchange, and obligation.",
        "articles": [
            ("A01", "People", [
                ("S010", "Whole Person", "A person is never only a role, conflict, debt, diagnosis, or request."),
                ("S020", "Role Clarity", "Roles should clarify responsibility without swallowing identity."),
                ("S030", "Contact Boundary", "Contact information, relational context, and interpretation should be separated when possible."),
            ]),
            ("A02", "Communication", [
                ("S010", "Context", "Important communication should preserve sender, receiver, date, medium, and surrounding context."),
                ("S020", "Tone and Fact", "Tone may be described, but fact and interpretation should remain distinguishable."),
                ("S030", "Draft Status", "Draft replies remain drafts until deliberately sent."),
            ]),
            ("A03", "Exchange", [
                ("S010", "Reciprocity", "Exchange should be grounded in clarity, consent, and reality rather than guilt or panic."),
                ("S020", "Care Labor", "Care labor is real labor even when performed inside family systems."),
                ("S030", "Obligation", "Obligation should not be inferred from crisis pressure without review."),
            ]),
        ],
    },
    {
        "folder": "title_07_ethics",
        "file": "title_07_ethics.md",
        "code": "T07",
        "name": "Ethics, Responsibility, and Disclosure",
        "summary": "The doctrine of care, harm reduction, privacy, fairness, responsibility, and selective disclosure.",
        "articles": [
            ("A01", "Ethics", [
                ("S010", "Dignity", "Records should preserve dignity even when documenting conflict, harm, or contradiction."),
                ("S020", "Minimum Necessary Disclosure", "Share only what is needed for the purpose, audience, and safety context."),
                ("S030", "Consent", "Consent and access boundaries should be explicit when material involves other people."),
            ]),
            ("A02", "Responsibility", [
                ("S010", "Owned Action", "Responsibility begins with what I can truthfully own, repair, change, or refuse."),
                ("S020", "False Burden", "I am not responsible for carrying another person's entire system when consent, capacity, or safety is absent."),
                ("S030", "Evidence", "Responsibility claims should be grounded in evidence and context, not projection alone."),
            ]),
            ("A03", "Disclosure", [
                ("S010", "Sensitive Material", "Medical, legal, financial, and family-conflict material requires higher review before disclosure."),
                ("S020", "Audience", "A record may be true and still not appropriate for every audience."),
                ("S030", "Misuse Risk", "If a record can be easily misused, label it and route it carefully."),
            ]),
        ],
    },
    {
        "folder": "title_08_cycles_legacy",
        "file": "title_08_cycles_legacy.md",
        "code": "T08",
        "name": "Cycles, Closure, and Legacy",
        "summary": "The doctrine of seasons, endings, repair cycles, archive, inheritance, and legacy design.",
        "articles": [
            ("A01", "Cycles", [
                ("S010", "Seasonality", "Life moves in seasons; a system should allow return, renewal, rest, and revision."),
                ("S020", "Review", "Active commitments, systems, and records need review before they become hidden burden."),
                ("S030", "Reset", "A reset is lawful when the current structure no longer serves truth, care, or action."),
            ]),
            ("A02", "Closure", [
                ("S010", "Completion Record", "Closed work should say what was done, where it lives, and what remains open."),
                ("S020", "Grief", "Closure may include grief without treating grief as failure."),
                ("S030", "Archive", "Archive material should remain findable without crowding the active field."),
            ]),
            ("A03", "Legacy", [
                ("S010", "Inheritance", "Legacy is what can be carried forward without needing the whole crisis to be relived."),
                ("S020", "Design", "Design should help the future self understand why the structure exists."),
                ("S030", "Transmission", "What is transmitted should preserve meaning, dignity, and usefulness."),
            ]),
        ],
    },
    {
        "folder": "title_09_qispark_bridge",
        "file": "title_09_qispark_bridge.md",
        "code": "T09",
        "name": "QiSpark Technical Doctrine Bridge",
        "summary": "The bridge from personal doctrine into QiSpark technical/dev doctrine, QiServer, QiMemory, and QiConnect.",
        "articles": [
            ("A01", "Bridge Rule", [
                ("S010", "Personal First", "QiSpark technical doctrine serves QiCode; it does not replace the personal life doctrine."),
                ("S020", "Translation", "Technical systems translate doctrine into infrastructure, data, workflows, and tools."),
                ("S030", "Subordination", "When technical elegance conflicts with humane use, humane use governs unless safety requires otherwise."),
            ]),
            ("A02", "QiSpark", [
                ("S010", "Dev Doctrine", "QiSpark holds the technical development doctrine: standards, structure, registries, schemas, decisions, and templates."),
                ("S020", "System Layers", "QiSpark feeds QiServer, QiVault, QiApps, and related implementation layers."),
                ("S030", "Engineering Record", "Technical decisions belong in ADRs, standards, registries, and system documentation."),
            ]),
            ("A03", "QiServer and Connected Systems", [
                ("S010", "QiServer", "QiServer is the runtime and service layer for infrastructure, integrations, workers, and system operations."),
                ("S020", "QiMemory", "QiMemory handles ingestion, extraction, embeddings, retrieval, graphs, memory, and sync/backup concerns."),
                ("S030", "QiConnect", "QiConnect handles APIs, workflows, external integrations, and connection surfaces between systems."),
            ]),
        ],
    },
]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def backup(path: Path) -> None:
    if path.exists():
        target = BACKUP / path.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            shutil.copy2(path, target)


def frontmatter(title: str, slug: str, summary: str, layout: str = "section") -> str:
    return f"""---
layout: {layout}
title: {title}
slug: {slug}
summary: {summary}
status: active
updated_at: "{TODAY}"
tags:
  - qicode
source_type: manual
---"""


def title_doc(item: dict[str, object]) -> str:
    code = item["code"]
    name = item["name"]
    lines = [
        frontmatter(f"QiCode Title {code[1:]} - {name}", f"qicode-title-{code[1:].lower()}-{str(name).lower().replace(' ', '-').replace(',', '')}", item["summary"]),
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
        f"- `{code}.R001.L001` This title is part of QiCode and should be read as personal life doctrine first.",
        f"- `{code}.R001.L002` A section states a governing principle; a line states a citeable rule or application.",
        f"- `{code}.R001.L003` Exceptions should be named, reviewed, and linked to the record that justifies them.",
        "",
    ]
    for article_code, article_name, sections in item["articles"]:
        lines += [f"## Article {article_code[1:]} - {article_name} (`{code}.{article_code}`)", ""]
        for section_code, section_name, rule in sections:
            ref = f"{code}.{article_code}.{section_code}"
            lines += [
                f"### Section {section_code[1:]} - {section_name} (`{ref}`)",
                "",
                f"- `{ref}.L001` {rule}",
                f"- `{ref}.L002` Apply this provision with truth, care, consent, and proportion.",
                f"- `{ref}.L003` If the provision is used in a project, link back to the record, output, or decision that applies it.",
                "",
            ]
    lines += ["## Cross References", "", "- [QiCode Index](../_index.md)", "- [Citation Guide](../citation_guide.md)"]
    return "\n".join(lines)


def index_doc() -> str:
    lines = [
        frontmatter("QiCode", "qicode", "Personal life doctrine in legal-code style, with a bridge into QiSpark technical doctrine."),
        "# QiCode",
        "",
        "QiCode is the citeable personal life doctrine for truth, identity, inner work, outer work, relationships, ethics, closure, and legacy. QiSpark begins after QiCode as the technical/dev doctrine that implements and supports the life doctrine.",
        "",
        "## Citation Pattern",
        "",
        "- Title: `QiCode T01`",
        "- Article: `QiCode T01.A01`",
        "- Section: `QiCode T01.A01.S010`",
        "- Line: `QiCode T01.A01.S010.L001`",
        "",
        "## Personal Doctrine",
        "",
    ]
    for item in TITLES[:8]:
        lines.append(f"- [`QiCode {item['code']}` - {item['name']}]({item['folder']}/{item['file']})")
    lines += [
        "",
        "## Technical Doctrine Bridge",
        "",
        f"- [`QiCode {TITLES[8]['code']}` - {TITLES[8]['name']}]({TITLES[8]['folder']}/{TITLES[8]['file']})",
        "",
        "## QiSpark Technical Doctrine",
        "",
        "- [QiSpark System](../_index.md)",
        "- [QiServer](../../20_QiServer/_index.md)",
        "- [QiMemory](../../20_QiServer/30_QiMemory/_index.md)",
        "- [QiConnect](../../20_QiServer/50_QiConnect/_index.md)",
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
    return "\n".join(lines)


def citation_doc() -> str:
    return f"""{frontmatter("QiCode Citation Guide", "qicode-citation-guide", "Reference syntax for citing QiCode personal-doctrine provisions.", "page")}
# QiCode Citation Guide

## Hierarchy

- `T##` means Title.
- `A##` means Article.
- `S###` means Section.
- `L###` means Line.

## Examples

- `QiCode T01` cites Title 01, My Truth and Source.
- `QiCode T01.A02` cites Title 01, Article 02, Law of One.
- `QiCode T03.A03.S010` cites the Boundary Validity section.
- `QiCode T09.A03.S020.L001` cites the QiMemory bridge rule.

## Style Rules

- Use backticks around citations in prose.
- Keep section numbers stable once cited.
- Add new sections in increments of 10, such as `S010`, `S020`, and `S030`, so later inserts can fit between them.
- Use line numbers when a provision may need exact reference in prompts, decisions, review comments, or formal notes.
- Treat `T01` through `T08` as personal doctrine and `T09` as the bridge into QiSpark technical doctrine.
"""


def overview_doc() -> str:
    return f"""{frontmatter("QiCode Core Overview", "qicode-core-overview", "Overview of QiCode as personal life doctrine with a technical bridge into QiSpark.", "page")}
# QiCode Core Overview

QiCode is the personal life doctrine. It is written in a legal-code style so it can be cited, extended, and applied without losing its center.

## Doctrine Layers

1. `T01` establishes My Truth and Source: Law of One, EmpowerQNow, voice, and source alignment.
2. `T02` through `T04` govern the inner world: self, identity, mind, will, boundaries, and agency.
3. `T05` through `T07` govern the outer world: work, creation, people, exchange, ethics, responsibility, and disclosure.
4. `T08` governs cycles, closure, archive, and legacy.
5. `T09` bridges into QiSpark technical doctrine.

## Technical Handoff

QiSpark is the technical/dev doctrine that implements and supports QiCode. QiSpark feeds QiServer, QiMemory, QiConnect, QiVault, and QiApps.

## Active Surfaces

- [QiCode Index](_index.md)
- [Citation Guide](citation_guide.md)
- [QiSpark System](../_index.md)
- [QiServer](../../20_QiServer/_index.md)
- [QiMemory](../../20_QiServer/30_QiMemory/_index.md)
- [QiConnect](../../20_QiServer/50_QiConnect/_index.md)
"""


def write(path: Path, text: str, rows: list[dict[str, str]], action: str, reason: str) -> None:
    backup(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")
    rows.append({"action": action, "path": rel(path), "reason": reason})


def move_old_title_dirs(rows: list[dict[str, str]]) -> None:
    wanted = {item["folder"] for item in TITLES}
    for directory in sorted(QICODE.glob("title_*")):
        if not directory.is_dir() or directory.name in wanted:
            continue
        target = REVIEW / "previous_generated_titles" / directory.name
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            shutil.rmtree(target)
        shutil.move(str(directory), str(target))
        rows.append({"action": "archive_previous_title", "path": f"{rel(directory)} -> {rel(target)}", "reason": "Archived generated title folder from previous QiCode model."})


def main() -> int:
    rows: list[dict[str, str]] = []
    CLEANUP.mkdir(parents=True, exist_ok=True)
    move_old_title_dirs(rows)
    for item in TITLES:
        path = QICODE / item["folder"] / item["file"]
        write(path, title_doc(item), rows, "write_title", f"Wrote personal-doctrine title {item['code']}.")
    write(QICODE / "_index.md", index_doc(), rows, "write_index", "Rebuilt QiCode index around personal doctrine and QiSpark bridge.")
    write(QICODE / "citation_guide.md", citation_doc(), rows, "write_guide", "Updated citation guide examples for personal doctrine.")
    write(QICODE / "01_core_overview.md", overview_doc(), rows, "write_overview", "Updated overview to explain personal doctrine and technical handoff.")
    with REPORT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["action", "path", "reason"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"actions={len(rows)}")
    print(f"report={REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
