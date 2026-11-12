# Agent Course Synthesizer v0.4.0

将八门AI Agent课程按已有课程地图整合为适合首次系统学习的中文教材，同时保存独立研究依据。v0.4.0保留v0.3.0的深度解释、来源核查、快照与安全发布，进一步要求检查读者能否顺着学会。

## 本版变化
1. **先完整体验，再拆解概念**：在密集术语前先走一次输入→关键变化→结果。
2. **知识分层**：区分必须掌握、只需认识、后续再学；深度内容有去向，不机械限制篇幅。
3. **按主题选择课程原例**：优先考察八门课程中实际读过的合适例子，允许转述、必要短引、改编或综合；标明来源及关键改动。不固定会议场景，不要求每个Step强制换例，不因用户职业默认套行业案例。
4. **代码难度匹配读者**：核心骨架与完整工程实现分层，陌生语法先解释。
5. **补全mock到真实组件的桥梁**：具体展示模型/组件收到什么、返回什么、应用如何衔接；不能只说“替换MockLLM即可”。
6. **检验业务语义**：成功声明、实际数据变化、回执和断言一致；仅保存回执不能说已改变外部环境。
7. **主动学习与视觉辅助**：关键转折先预测、再解释；图/表/状态对照按理解需要使用，不机械配额。
8. **独立评价学习体验**：合规通过不自动等于读者通过；按顺序、负担、衔接、实践、主动理解、阅读节奏逐项审查。
9. **更清晰的发布验证**：检查转义粗体、文件名误链接等细节，区分API回读与浏览器视觉验收；未验证项不计完成。

## 文件
- [SKILL.md](SKILL.md)：执行入口，完整整理时加载全部九份references。
- [01](references/01-source-extraction.md)：来源、Atomic Claims、解释素材与原例出处。
- [02](references/02-knowledge-synthesis.md)：跨课综合、claim_matrix与知识依赖。
- [03](references/03-deduplication-and-evidence.md)：证据去重和阅读节奏。
- [04](references/04-curriculum-design.md)：早期体验、知识分层、主动推演。
- [05](references/05-notion-output-template.md)：双层产物、快照及结构/显示验证。
- [06](references/06-quality-control.md)：合规与学习双轨评估、稳定条款ID及逐项审计。
- [07](references/07-reader-validation.md)：首次读者的六维评估与主题化回归。
- [08](references/08-teaching-depth-and-scenario.md)：原课案例选择、改编归属和先评分。
- [09](references/09-practice-and-model-bridge.md)：新增，实践难度、mock桥梁与业务语义。
- [tests/validate_structure.py](tests/validate_structure.py)：离线结构检查，不证明模型执行效果或教学效果。
- [examples/rag-validation.md](examples/rag-validation.md)：原仓库v0.1历史抽样记录，保持原样，不升级其历史结论。

## 手动更新GitHub
下载并解压ZIP，进入其中的 `agent-course-synthesizer` 文件夹，将**文件夹里面的内容**放入现有仓库根目录，同路径文件替换，新增 `references/09-practice-and-model-bridge.md`。不要在原仓库里再嵌套同名文件夹，不清空仓库其他内容。包不含Git历史、凭证或本轮私有Notion课程资料；历史example是你公开仓库已有文件，保持不变。

本包基于2026-11-12读取的GitHub main文件；其树SHA为 `8e91961c0bc69893f3af067fc106dcadbb0afa7a`，原SKILL文件SHA为 `0c1ba1981d121f3866698ebf5467e11c1ae4e392`。树SHA不是提交SHA。若你下载后又改过仓库，请先比较差异。此交付不代表GitHub已更新，也不代表客户端已安装；本次仅制作可下载的更新包。

更新前可在仓库根目录运行：
~~~bash
python tests/validate_structure.py
~~~
没有第三方依赖。结果只验证版本、文件、链接、条款ID和历史样例完整性。完整教学行为需要在后续真实任务中验证；不得将静态检查称为教学评分。

本次打包验证（2026-11-12）：结构检查通过，覆盖13个必需文件、9份references、47个唯一条款ID及24个本地链接；frontmatter校验通过。一次独立的专项读者审阅试用识别了样稿中的反馈缺失、成功语义与状态不一致、mock桥梁缺失及无依据的满分评价。另一项新课设计试用未完成，完整课程生成、Notion发布和真人学习效果尚未验证；不能将此包称为全面行为测试通过。

## 调用示例
> 请读取我GitHub仓库当前agent-course-synthesizer v0.4.0及全部references，按课程地图完整整理Step X。先读取来源并保留阅读范围，保存原稿快照，建立独立研究记录；按主题优先采用合适的原课程案例，不固定会议场景。采用deep/dual，明确要求覆盖时使用update-existing。写成知识分层、先体验后解释、实践难度匹配的教学正文。最后分别评估执行合规与首次学习体验，列出每项要求的证据、修复和未验证范围。

如仅请评估一篇现有课，可明确“仅评审，不改写/发布”；这时不伪称完成整套研究发布流程。不强制所有Step用版本迭代格式，也不规定统一代码行数、术语数量或正文字符上限。
