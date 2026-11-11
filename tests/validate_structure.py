"""Structure smoke test for agent-course-synthesizer v0.2 (no network)."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
expected = ["SKILL.md", "README.md", "references/01-source-extraction.md",
 "references/02-knowledge-synthesis.md", "references/03-deduplication-and-evidence.md",
 "references/04-curriculum-design.md", "references/05-notion-output-template.md",
 "references/06-quality-control.md", "references/07-reader-validation.md"]
for name in expected:
    path = root / name
    assert path.is_file() and path.stat().st_size > 200, name
skill = (root / "SKILL.md").read_text(encoding="utf-8")
assert skill.splitlines()[:2] == ["---", "name: agent-course-synthesizer"]
assert "v0.2.0" in skill
assert all(f"references/{i:02d}-" in skill for i in range(1, 8))
assert "Teaching Note" in skill and "Research Record" in skill
for path in root.rglob("*.md"):
    assert "\x00" not in path.read_text(encoding="utf-8")
print("PASS: v0.2 structure and seven reference links")
