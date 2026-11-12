"""Offline package integrity checks for agent-course-synthesizer v0.4.0.
No model, live Notion, source-reading or pedagogical-effectiveness validation.
Run from any directory with Python 3.10+; standard library only.
"""
from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
REFS = [
    "01-source-extraction.md", "02-knowledge-synthesis.md",
    "03-deduplication-and-evidence.md", "04-curriculum-design.md",
    "05-notion-output-template.md", "06-quality-control.md",
    "07-reader-validation.md", "08-teaching-depth-and-scenario.md",
    "09-practice-and-model-bridge.md",
]
PREFIXES = ["SRC", "SYN", "DED", "CUR", "NOT", "QA", "READ", "CASE", "PRA"]
REQUIRED = ["SKILL.md", "README.md", "tests/validate_structure.py",
            "examples/rag-validation.md"] + ["references/" + name for name in REFS]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate():
    for name in REQUIRED:
        require((ROOT / name).is_file(), "Missing file: " + name)
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    require(skill.startswith("---\nname: agent-course-synthesizer\n"),
            "Incorrect name/frontmatter")
    front = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
    require(front is not None, "Invalid frontmatter")
    require("description: " in front.group(1), "Missing description")
    for name in ("SKILL.md", "README.md"):
        content = (ROOT / name).read_text(encoding="utf-8")
        require("# Agent Course Synthesizer v0.4.0" in content,
                "Incorrect active version: " + name)
    for name in REFS:
        require("references/" + name in skill, "Unlinked reference: " + name)

    ids = []
    for name, prefix in zip(REFS, PREFIXES):
        content = (ROOT / "references" / name).read_text(encoding="utf-8")
        found = re.findall(r"^## (" + prefix + r"-\d{2})｜", content, re.M)
        require(bool(found), "Missing requirement IDs: " + name)
        require([int(i.rsplit("-", 1)[1]) for i in found] ==
                list(range(1, len(found) + 1)), "Nonsequential IDs: " + name)
        ids.extend(found)
    require(len(ids) == len(set(ids)), "Duplicate requirement ID")

    links = 0
    for path in sorted(ROOT.rglob("*.md")):
        content = path.read_text(encoding="utf-8")
        require("\x00" not in content, "NUL byte: " + str(path))
        # Check only literal relative Markdown links, not external URLs/anchors.
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            if target:
                require((path.parent / target).is_file(),
                        "Broken link: " + str(path.relative_to(ROOT)) + " -> " + target)
                links += 1
        fence = None
        for line in content.splitlines():
            match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
            if not match:
                continue
            mark, tail = match.groups()
            if fence is None:
                fence = (mark[0], len(mark))
            elif mark[0] == fence[0] and len(mark) >= fence[1] and not tail.strip():
                fence = None
        require(fence is None, "Unclosed code fence: " + str(path))

    raw = (ROOT / "examples/rag-validation.md").read_bytes()
    blob = b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw
    require(hashlib.sha1(blob).hexdigest() ==
            "1c9bdd85056bfa56b3918796c9fbccc368dd82b1",
            "Historical example changed; preserve it or explicitly review a new baseline")
    print(f"PASS: {len(REQUIRED)} required files; {len(REFS)} linked references; "
          f"{len(ids)} unique requirement IDs; {links} local links; "
          "code fences and historical example integrity")
    print("SCOPE: static integrity only; teaching quality and live execution not tested")


if __name__ == "__main__":
    validate()
