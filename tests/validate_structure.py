"""Offline structure and content-contract checks for agent-course-synthesizer v0.3.0.

Can run in the v0.3 patch folder or an existing repository after extraction.
Does not test a real model, Notion connector, or teaching effectiveness.
"""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
required = {
    "SKILL.md", "README.md",
    "references/01-source-extraction.md",
    "references/02-knowledge-synthesis.md",
    "references/03-deduplication-and-evidence.md",
    "references/04-curriculum-design.md",
    "references/05-notion-output-template.md",
    "references/06-quality-control.md",
    "references/07-reader-validation.md",
    "references/08-teaching-depth-and-scenario.md",
    "tests/validate_structure.py",
}
for filename in sorted(required):
    path = root / filename
    assert path.is_file(), f"Missing required file: {filename}"
    assert path.stat().st_size > 250, f"File appears too short: {filename}"

skill = (root / "SKILL.md").read_text(encoding="utf-8")
readme = (root / "README.md").read_text(encoding="utf-8")
assert skill.splitlines()[:2] == ["---", "name: agent-course-synthesizer"]
assert re.search(r"# Agent Course Synthesizer v0\.3\.0\b", skill)
assert re.search(r"# Agent Course Synthesizer v0\.3\.0\b", readme)
for i in range(1, 9):
    assert f"references/{i:02d}-" in skill, f"Missing reference {i:02d} in SKILL.md"

# All literal Markdown links to repository references must resolve.
for source in [root / "SKILL.md", *sorted((root / "references").glob("*.md"))]:
    for link in re.findall(r"\]\(([^)#]+\.md)\)", source.read_text(encoding="utf-8")):
        assert (source.parent / link).is_file(), f"Broken link: {source.name} -> {link}"

full_text = "\n".join((root / name).read_text(encoding="utf-8") for name in sorted(required) if name.endswith(".md"))
checks = {
    "dual-layer research provenance": "Teaching Note" in skill and "Research Record" in skill and "source_manifest" in skill,
    "universal scenario preference": "跨行业" in skill and "不默认套用用户个人职业" in skill,
    "narrative depth": "朴素方案" in skill and "为什么需要" in skill and "逐步" in skill,
    "plain-language pedagogy": "通俗" in skill and "首次出现" in skill,
    "review separated from teaching": "Review Recap" in skill and "复习" in skill,
    "flexible length": "不设置正文默认字数/字符上限" in skill and "不设置 5000–8000 字符目标" in full_text,
    "scenario rubric": "普遍性" in full_text and "可验证" in full_text,
    "not forced V0-V3": "不强制所有 Step 用版本迭代格式" in readme,
    "example provenance and experiments": "教学模拟" in skill and "真实 LLM" in full_text,
    "safe Notion update": "快照" in skill and "子页" in skill,
}
assert all(checks.values()), "Unmet v0.3 contract(s): " + ", ".join(k for k, ok in checks.items() if not ok)

for path in root.rglob("*.md"):
    assert "\x00" not in path.read_text(encoding="utf-8"), f"NUL byte in {path}"

legacy_example = root / "examples/rag-validation.md"
if not legacy_example.exists():
    print("NOTE: historical examples/rag-validation.md is not part of the patch; retain it in your GitHub repository")
print("PASS: v0.3.0 structure, eight reference links and depth/scenario contracts")
