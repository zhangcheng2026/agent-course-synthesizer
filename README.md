# Agent Course Synthesizer v0.2.0

面向 Notion 中多门 AI Agent 课程的主题融合与教学重构 Skill。

## v0.2 的关键改变

旧版擅长来源核查、Claim 记录和去重，但容易把长矩阵和审计附在 Step 正文后面。新版**分别生成教学正文和研究记录**，二者通过 Notion 链接和 Claim ID 连接；新增案例驱动、渐进式术语、知识边界、减少重复讲解和首次读者模拟审查。

## 目录

- SKILL.md：入口与七阶段方法
- references/01–06：来源、综合、去重、课程设计、Notion 模板、发布/质量
- references/07-reader-validation.md：新增读者模拟与 Step 回归标准
- examples/rag-validation.md：v0.1 抽样 RAG 样本（原文件保持不变）
- tests/validate_structure.py：结构测试

## 使用示例

> 请读取 GitHub 仓库 agent-course-synthesizer 的 v0.2 SKILL.md 与 references。整合 Notion 02–09 对应 Step 2 的相关章节，目标是 01｜AI Agent 学习体系与项目实践 / Step 2。mode=update-existing，depth=balanced，delivery=dual。先保存旧版快照，在关联研究页保留完整 Claim/来源/审计，再把 Step 2 正文改成以订单查询贯穿的案例驱动课程。读者审核与证据审核通过后发布并回读。

仓库托管不等于客户端已安装 Skill；Notion/GitHub 访问与写入取决于账号连接权限。v0.1 留在 Git 历史，旧 RAG 示例仍是历史研究样本，不能被冒认为完整八门来源或新版正文模板。