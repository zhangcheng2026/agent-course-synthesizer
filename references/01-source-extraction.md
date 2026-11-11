# 01｜来源发现、覆盖状态与原子 Claim

## 两类覆盖必须分开

单页 Notion fetch 完整、没有截断，只能证明**该次页面文本读取完成**。要宣称课程主题覆盖完整，还需要确认相关子页、图片、代码、笔记与附件。采用 read_complete / read_partial / not_found / not_in_scope，注明选取范围、未读章节和限制。八门课程读取 15 个选定页面不等于读完八门课程。

每条来源记录：课程根页、标题、精确 URL、章节小节锚点、读取日期、文本截断与附件情况、source_voice（original/translation/learner_notes/synthesizer/external_check）、independence_group、技术版本。

## 原子 Claim 格式

~~~yaml
claim_id: STEP2-001
concept: Agent Loop
type: mechanism
claim: 工具结果反馈影响下一轮动态决策
qualifiers: 典型动态 Agent Loop，不代表所有固定 Workflow
source:
  course: 实际课程
  page_title: 完整章节名
  page_url: Notion 页面 URL
  anchor: 相关小节标题
source_voice: original
independence_group: original-course-branch
framework_version: null
confidence: supported
~~~

一条 Claim 不能混合定义、优势、例子和性能判断。将输入/处理/输出、代码版本、真实执行情况单独记录。完整原子证据表放 Research Record；正文只引用重要小节，读者不必理解 Claim 编号才看懂课程。

## 出口验收

能解释读了哪些页面、具体读取边界、每条主张的来源、哪些未读取或未运行。资料不足时必须标 partial，不得宣称全量。