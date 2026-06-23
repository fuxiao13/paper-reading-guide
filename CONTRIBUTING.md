# 贡献指南

欢迎贡献,尤其是**新增领域速查表**——这是本技能最容易、也最有价值的扩展点。

## 这个项目怎么组织
真正被 agent 加载执行的只有三块:`SKILL.md` + `references/` + `scripts/`。
`README.md`、`examples/`、`CONTRIBUTING.md`、`LICENSE` 是给人看的,不是运行依赖。
架构是"**通用读法主干 + 可插拔领域速查表**":读法领域无关,各方向的行话基准
拆在 `references/domains/` 下,SKILL.md 通过 `references/domains/_index.md` 选表。

## 加一个新领域速查表(最常见的贡献)
1. 在 `references/domains/` 新建 `your-domain.md`,按下列统一结构编写:
   - 基础链路 / 问题设定
   - 核心概念(讲解时必须用对的术语与直觉)
   - 常见方法 / 范式
   - 常用数据集与指标
   - 该方向追问项
   - 小结附加字段(供 `references/summary-template.md` 取用)
2. 在 `references/domains/_index.md` 的"选表规则"表里加一行信号词。
3. (可选)在 `examples/` 加一段该方向的示例会话。
4. **SKILL.md 通常不用改**——它只认 `domains/` 下的文件 + 索引。

## 内容准则
- 速查表是"够用的直觉版",不是教科书;与具体论文冲突时以论文为准。
- 术语、数据集、指标要准确;拿不准就标注存疑,别编。
- 保持中文为主(跟随项目风格),欢迎补充英文对照。

## 改脚本
- `scripts/` 只依赖 PyMuPDF(见 `requirements.txt`)。新增依赖请在 PR 里说明必要性。
- 改完跑一下 `python -m py_compile scripts/*.py`,并对真实 PDF 实测一次。
- 脚本须保持:只读本地文件、不联网、不上传。

## 提 PR
- 一个 PR 聚焦一件事(一张速查表 / 一处修复)。
- 描述清楚动机与改动范围;涉及速查表请说明覆盖的子方向。
