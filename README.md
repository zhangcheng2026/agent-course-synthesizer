# Agent Course Synthesizer

面向个人 Notion AI Agent 课程体系的**多课程知识综合 Skill**。将类似课程按主题进行交叉提取、去重、对比、课程重构和证据审查，输出简体中文 Step 复习笔记。

## 当前状态

- v0.1.0：主 `SKILL.md` + 6 个核心 references 文件。
- `examples/rag-validation.md`：已根据 Notion 的 **5 个课程来源**完成第一轮 RAG 主题抽样整合；**未覆盖全部 02–09**，未执行代码/性能基准。
- 默认不修改任何 Notion 页面；需要用户指定 `create-new` 或 `update-existing` 后，才执行对应写入。
- 仓库内容是独立编写的工作流规则，仅参考外部 Skills 的方法，并非它们的衍生镜像。

## 目录

```
SKILL.md
references/
  01-source-extraction.md
  02-knowledge-synthesis.md
  03-deduplication-and-evidence.md
  04-curriculum-design.md
  05-notion-output-template.md
  06-quality-control.md
examples/
  rag-validation.md
tests/
  validate_structure.py
```

## 在 Agent Skills 客户端中使用

把整个仓库目录置于支持 Agent Skills 的客户端可访问的 skills 目录中，使客户端识别仓库根目录的 `SKILL.md`。也可把目录重命名成 `agent-course-synthesizer`。**放到 GitHub 不代表 ChatGPT 自动安装该 Skill**；只有在使用环境能读取它时，才会按其规则运行。Notion 读取/写入必须依赖已有连接工具权限。

示例指令：

```
使用 agent-course-synthesizer：
主题：RAG；源：Notion 02–09 中含 RAG 的章节；
目标：01 | AI Agent｜学习体系与项目实践 / Step 10。
模式：draft；深度：balanced。
先提交来源清单和缺口，随后给原子观点矩阵与紧凑课程草稿。
未明确要求写入前，不修改原来的 Step 10。
```

## 上游方法参考

- [Research Synthesis — SkillMedev](https://github.com/SkillMedev/skills/tree/main/skills/research-synthesis)
- [Knowledge Synthesis — Anthropic](https://github.com/anthropics/knowledge-work-plugins/tree/main/enterprise-search/skills/knowledge-synthesis)
- [Education Agent Skills — Gareth Manning](https://github.com/GarethManning/education-agent-skills)

仅借鉴“原子知识、聚类、分歧、去重、来源、知识依赖、学习目标”等方法，不直接复制上游 `SKILL.md` 原文。上游项目的许可证与适用约束应分别遵守。

## 维护路线

1. 补完 02–09 的 RAG 主题来源清单并做章节级覆盖核查。
2. 针对 RAG 补充可运行的 `retrieval / generation / evaluation` 最小案例，并记录依赖版本。
3. 完成 Notion 新稿页的人工审阅，再由用户明确授权更新 Step 10。
4. 复用同一流程验证 Memory、MCP、Context Engineering。
