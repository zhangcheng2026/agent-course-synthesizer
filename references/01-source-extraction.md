# 01｜来源发现、覆盖状态、原子 Claim 与教学素材

## 一、先确认主题和覆盖范围

按用户指定的 Notion 课程及其课程地图进行**主题定位**：哪些课程是主力、哪些只补机制或实践、哪些不应在本 Step 重复。必须阅读相关小节正文，不能只看标题和片段。Notion 页面 API 未截断只说明该次页面文本完整，不代表课程的所有章节、图示、附件、代码或视频已经审核。

状态使用 `read_complete` / `read_partial` / `not_found` / `not_in_scope`，注明被选页面、未读章节、图像与代码的可读性；将同一作者原文、译文、迁移版、用户课堂笔记归到一个独立来源组，不能伪装为不同作者的交叉证据。

每条来源记录：课程根页、标题、URL、**精确小节**、读取日期、页面完整/截断状态、附件范围、`source_voice`（original / translation / learner_notes / synthesizer / external_check）、`independence_group`、技术版本。

## 二、Atomic Claim：原子知识判断

每条原子主张只表述一个定义、机制、取舍或限制，不混合未经证实的性能数据。示意：

~~~yaml
claim_id: STEP4-001
concept: Few-shot Prompting
type: mechanism
claim: 本次 Prompt 附带代表性输入-输出示例，可引导模型依照示例执行任务
qualifiers: 不更新模型权重，效果依赖任务、模型与示例质量
source:
  course: 实际课程
  page_title: 完整小节标题
  page_url: Notion 页面 URL
  anchor: 具体小节
source_voice: learner_notes
independence_group: original-course-branch
framework_version: null
confidence: supported
~~~

## 三、v0.3 新增：提取“可用于教学的完整解释链”

**不能只记录原子 Claim。** 对每个核心概念额外记下：

- `problem_context`：原课程从什么现实问题出发？解决了什么困难？
- `naive_attempt`：普通人/简单实现通常会怎么做？为何不足或在哪些条件失效？如果原文没有讨论，标 `synthesizer_example`，不伪称作者讲过。
- `mechanism_steps`：核心流程的输入、中间变化/判断、输出、停止或反馈；保留关键“为什么”。
- `teaching_examples`：作者的具体例子、关键比喻、对照案例；区分原作者示例与教学者新编示例。
- `counterexamples_and_limits`：使概念边界变清楚的反例、适用条件、失败模式与不同方案取舍。
- `implementation_and_tests`：源代码实际使用的框架/版本，是否本次运行，如何验证；不要把 mock 当成大模型测试。
- `readability_observation`：初学者可能卡在哪里，需要怎样更通俗地解释。

例：Few-shot 的价值不仅是“给几个例子”，还需要说清“分类边界为什么混淆、三条例子分别纠正什么、它怎样利用当前上下文而不是训练权重、示例是否真的让独立测试集变好”。一个多来源主题可以分别取定义、机制、案例、反例，不能为了去重抹掉过程。

## 出口验收

可精确回答：读了什么、没读什么、主张来自哪一节、哪些机制解释和反例值得保留、哪些是自己构造的例子。不能把选定页面的完整读取宣称为全课程覆盖。
