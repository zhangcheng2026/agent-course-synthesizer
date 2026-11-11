# Agent Course Synthesizer v0.3.0

将多门 AI Agent 课程整理为**适合首次系统学习的中文教材**，并保存独立的可追溯研究记录。v0.3 在 v0.2.0 的双层产物上升级教学深度，**不是改成一套新的无来源写作模板**。

## v0.3.0 的关键改变

1. **案例选得更通用**：默认使用多数职场读者熟悉的场景（如项目周会、客服工单、文档查问、任务跟进等），根据知识主题选择；仅当用户明确要求时使用其职业背景。所有模拟例子须明确标识。
2. **过程解释完整**：由“是什么”升级为“为什么出现 → 旧办法哪里不够 → 原理怎样工作 → 如何逐步改进 → 失败与边界 → 怎样验证”。保留作者有教学价值的机制推导、例子和反例，而不是只抽取原子结论。
3. **通俗、渐进、可复述**：先现实问题与朴素语言，再引出专业术语和实现细节；关键概念需要能解释中间过程。比喻是辅助，不可代替准确机制。
4. **深度正文与精炼复习分开**：系统学习默认 `depth=deep`，正文不受 5000–8000 字符示意范围限制；简短总结放在末尾，完整研究矩阵放独立页。
5. **可核验的实操与迭代**：技术点适合时展示 V0→V1→V2→V3 的失败与改进，但**不强制所有 Step 用版本迭代格式**。标明演示结果、mock 测试与真实 LLM 测试的区别；JSON 格式校验不等于事实验证。
6. **延续 v0.2 保障**：八门课程地图与来源标注、Claim 矩阵、原稿备份、Notion 子页保护、双轨审查仍然有效。

## 文件目录

- `SKILL.md`：v0.3.0 的执行入口、输入参数、验收及七阶段流程。
- `references/01-source-extraction.md`：阅读范围、来源证据与教学过程素材提取。
- `references/02-knowledge-synthesis.md`：概念聚类、课程地图与独立来源综合。
- `references/03-deduplication-and-evidence.md`：证据/教学去重，不删重要解释链。
- `references/04-curriculum-design.md`：深度教学的叙事与知识设计。
- `references/05-notion-output-template.md`：Notion 教学正文、独立研究记录及复习规范。
- `references/06-quality-control.md`：事实、解释、案例、代码与安全发布审核。
- `references/07-reader-validation.md`：首次学习者模拟检查与主题特定回归。
- `references/08-teaching-depth-and-scenario.md`：**v0.3 新增**的案例选择和讲透原理的量规。
- `tests/validate_structure.py`：离线结构与 v0.3 合约测试。
- `examples/rag-validation.md`：v0.1 的历史抽样验证，**保持不变**；不可误称完整八门课程结论。

## 用法示例

> 加载我仓库 `agent-course-synthesizer` 的 `SKILL.md` 与全部 `references/01–08`，参考我在 Notion 中的八门课程知识地图。以 Step 5「上下文工程」为目标，`depth=deep`、`delivery=dual`、`mode=draft`。不要仅列知识结论；要用多数职场读者熟悉的案例，从原始问题、朴素方案的问题、核心机制、逐步方案、失败条件、最小实践与真实可检验的验收完整讲解。保留来源重要推导和反例，正文末做精炼复习，详细研究证据另存关联页。先让我审阅，不要覆盖原 Step 5。

## v0.3.0 更新包使用说明

此 ZIP 是供仓库所有者**解压覆盖到现有仓库根目录**的更新包，不是完整的 Git 工作树，也没有代替你上传 GitHub。文件夹结构保持根目录 `SKILL.md`、`references/`、`tests/`。旧 `examples/` 需保留在原仓库，不要清空其他文件。

Windows PowerShell 在仓库根目录运行：

```powershell
git add SKILL.md README.md references tests
git commit -m "release: agent-course-synthesizer v0.3.0"
git push origin main
```

可选先运行 `python tests/validate_structure.py`，若提示缺少 `examples/rag-validation.md`，说明你不是在原来完整的仓库根目录执行。GitHub 权限与代理可能影响 push，但不影响本地更新包本身。

GitHub 仓库存放 Skill 不代表 ChatGPT 自动安装或自动读取，执行时仍需有访问权限并真正加载各文件。私有 Notion 课程不得直接复制进公开 Skill 仓库。
