# 更新日志

遵循 [Keep a Changelog](https://keepachangelog.com/) 与语义化版本(SemVer)。

## [0.1.0] - 2026-06-23
首个发布版本。

### 新增
- 论文陪读核心技能(`SKILL.md`):三遍法、逐节推进、随时答问、收尾出精读小结。
- 可插拔领域速查表(`references/domains/`):控制+深度学习、声视觉/音频-视觉、
  声学成像,以及通用 DL 兜底;经 `_index.md` 选表。
- 通用提问清单(`references/question-checklist.md`)+ 通用精读小结模板
  (`references/summary-template.md`,含方向附加字段)。
- 脚本:`extract_outline.py`(抽章节/图表标题,**输出含页码**)、
  `render_page.py`(把关键页渲成 PNG 看图,检测扫描件)。
- 示例会话(`examples/`)、`CONTRIBUTING.md`、`REPO_META.md`、
  `requirements.txt`、`.gitignore`。

### 说明
- 跨 agent:遵循开放 Agent Skills 标准,Codex / Claude Code / Gemini 通用。
- 边界:只做单篇交互陪读;批量整理需求转交专门技能(不随本包发布)。
