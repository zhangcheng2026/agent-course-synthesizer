"""Structural smoke test. No network/Notion/GitHub access required."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
expected = [
    "SKILL.md",
    "references/01-source-extraction.md",
    "references/02-knowledge-synthesis.md",
    "references/03-deduplication-and-evidence.md",
    "references/04-curriculum-design.md",
    "references/05-notion-output-template.md",
    "references/06-quality-control.md",
    "examples/rag-validation.md",
    "README.md",
]
for path in expected:
    p = root / path
    assert p.is_file() and p.stat().st_size > 200, f"Missing or empty: {path}"
skill = (root / "SKILL.md").read_text(encoding="utf-8")
assert skill.startswith("---\nname: agent-course-synthesizer\n")
assert "description:" in skill
assert all(f"references/{i:02d}-" in skill for i in range(1, 7))
for p in root.rglob("*.md"):
    assert "\x00" not in p.read_text(encoding="utf-8")
print("PASS: 9 required files, valid frontmatter prefix, six reference links, UTF-8 text")
