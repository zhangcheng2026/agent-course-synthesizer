# 01｜来源阅读、原子主张与原例提取

## SRC-01｜先定位主题与来源
读取课程地图、目标Step及关联子页，查看用户认可的已有Step作为风格参照；明确哪些参照只选读、哪些全文读。按地图选主力、补充、独有来源，不要求八门课等量贡献。阅读相关小节正文；不能用标题、目录、搜索摘要或以前的总结代替原文。若原文不可得，标缺口并限缩主张或寻找可靠补证，不能把笔记改称原文。

## SRC-02｜登记准确阅读范围
source_manifest每条记录：source_id、课程根页、选页标题与URL、精确小节、读取日期、读取/截断状态、未读范围、图像/代码/附件/视频可读性、技术版本或文件SHA。状态为read_complete/read_partial/not_found/not_in_scope，必须说明状态的分母是单文件文字、选节还是整门课程。取到图片URL不等于看过图片，页面API未截断不等于所有附件都读过。

## SRC-03｜标来源身份与独立性
标source_voice=original/translation/learner_notes/synthesizer/external_check及independence_group。同一原课的译文、迁移、课堂笔记不加独立票数；另一作者明确转述同一原始主张时，按该主张归回原来源。版本未知填未知，不伪造。Notion页面标题写“原文/字幕”仍须检查内容实际身份。

## SRC-04｜提取Atomic Claims
每条只表达一项判断，记录claim_id、concept、type、claim、qualifiers、source_id和准确小节、source_voice、独立组、版本、confidence。来源公共字段可继承manifest，必须能够反查。定义、机制、限制、性能结果和教学设计分别标识；新推论标inference，新例标synthesizer，不冒充作者结论。指标保留分母、实验条件与不确定性。

## SRC-05｜提取完整解释材料
对核心概念另记problem_context、naive_attempt、mechanism_steps、teaching_examples、counterexamples_and_limits、implementation_and_tests、readability_observation。保留作者如何从问题走到机制，而不是只摘最后一句；原文没有朴素失败时，可以设计反例，但要注明新编。输入、重要中间判断、输出、成本和检验方式要能支撑教学。

## SRC-06｜为课程原例建立可追溯记录
先从已读八门课程选节中找合适例子，再按08选择。每个被采用的例子记录：
- example_id、source_id、精确小节/锚点、original_task、原输入/规则/关键变化/结果及原文的模拟或实测性质。
- usage=original_paraphrase/short_quote/adapted/composite/synthesizer；对adapted/composite列出改动、混合来源及为何改。
- preserved_mechanism、omitted_details、omission_effect、prerequisites、版权/私密材料使用边界。
原课未给运行证据就保留“作者演示/教学示意”，不能升级为本次实测。直接引用仅取必要短句并标来源，优先准确转述；不把私有全文复制到公开示例包。

## SRC-07｜提取先备知识缺口
读例子和代码时标注读者尚未具备的领域知识、Python语法、数学或框架依赖，交给04/09分层处理。来源完整性与教学必要性分别判断：读过的内容不必全进正文，删掉的独有关键机制要说明去向。出口须回答“读了什么、没读什么、主张在哪、哪些例子值得教、哪些是自己的设计”。
