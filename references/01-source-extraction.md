# 01｜资料发现与原子知识提取

## 范围与读取

1. 先定位用户指定的 01–09 课程根页面，确认实际页面隶属关系。不得把同名搜索结果直接当作目标教材；必要时从课程根页沿子页定位。
2. 对每个命中的章节获取完整正文、嵌套子页面和代码/图表的文字说明。记录读取时间、页面 URL、标题、章节路径、是否截断、是否有不可读附件。
3. 限定主题的选取标准：明确相关的定义、机制、条件、实验、指标、架构、反例；外围提及不等于系统覆盖。
4. 不盲目外扩全部课程。标记每个来源：`read_complete` / `read_partial` / `not_found` / `not_in_scope`。未读章节不能参与“已覆盖”统计。

## 原子 claim 的最小字段

```yaml
claim_id: RAG-001
concept: RAG/检索与生成
type: definition  # definition | mechanism | method | tradeoff | example | metric | caution
claim: "先检索外部相关片段，再作为上下文供生成器使用。"
qualifiers: "典型检索增强生成路径；工具型 Agentic RAG 可反复检索"
source:
  course: "具体课程名"
  page_title: "具体章节名"
  page_url: "Notion 页面 URL"
  anchor: "章节标题或短的原文定位"
independence_group: "original-course-branch"
confidence: supported # supported | tentative | conflicted | unverified
```

## 提取规范

- 一条 claim 不得同时混合“是什么、为什么、怎么做、是否最好”。
- 同一段可拆多个原子知识单元；主张和例子关联，例子不能冒充普遍规律。
- 标记 `source_voice`：原课程作者 / 译者或用户笔记 / 汇编者额外补充 / 外部核验。不同声音不得互相假冒。
- 将代码片段摘要为输入、处理、输出、框架/版本、复现条件，必要时附原文链接；不从未经执行的示例推导运行成功。
- `extraction_log` 标记未覆盖页、异常、潜在过时 API 和需要人工确认的问题。

## 出口验收

至少能回答：“读了哪些页面？每页抽取了什么？哪个结论来自哪个具体位置？哪些页没有读全？”如任一无法回答，不能声明全覆盖。
