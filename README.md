# paper-reading-guide

**版本** v0.1.0 · **许可** MIT · 跨 Codex / Claude Code / Gemini

> An interactive **paper-reading companion** as an Agent Skill (Codex / Claude Code / Gemini).
> It walks you through one paper at a time using the three-pass method — orient, read
> section-by-section, answer your questions — and grounds explanations with pluggable
> per-domain cheatsheets. Built for **control + deep learning** and **audio-visual learning**,
> with a general-DL fallback for any ML paper. Output language follows you (Chinese by default).

交互式**论文陪读**技能。用三遍法带你逐节精读单篇论文,边读边讲、随时答问,
按论文方向自动加载领域速查表,讲解不跑偏。面向**控制+深度学习**与**声视觉/音频-视觉**
两大方向,并对任意深度学习论文有通用兜底。小结只写本地 Markdown。

## 特性
- **三遍法陪读**:60 秒定位 → 逐节精读 → 按需深读;一节一停,不一次倒全文。
- **可插拔领域速查表**:读法主干领域无关,行话基准拆成独立文件,自动选表、可扩展。
- **领域无关提问清单 + 方向专属追问项**,帮你逼出每篇的创新点与局限。
- **跨 agent**:Agent Skills 开放标准,Codex / Claude Code / Gemini 通用。
- **看图能力**:`render_page.py` 把承载结论的关键页(学习曲线/热力图/波束图)渲成 PNG。
- **PDF 骨架脚本**:`extract_outline.py` 快速抽章节与图表标题,加速定位。
- **自带示例会话**,降低上手门槛、提升隐式触发准确度。

## 目录
```
paper-reading-guide/
├── SKILL.md                       # 入口:角色、选表、三遍法流程、纪律
├── README.md
├── LICENSE                        # MIT,作者:拂晓 / fu xiao
├── CONTRIBUTING.md                # 如何贡献(尤其加领域速查表)
├── CHANGELOG.md                   # 版本更新日志
├── REPO_META.md                   # GitHub 仓库描述/topics(建仓用,非运行依赖)
├── requirements.txt               # 脚本依赖(PyMuPDF)
├── .gitignore
├── agents/openai.yaml             # Codex 元数据(可选)
├── references/
│   ├── three-pass-reading.md      # 三遍法详解
│   ├── question-checklist.md      # 通用提问骨架(领域无关)
│   ├── summary-template.md        # 精读小结模板
│   └── domains/                   # 可插拔领域速查表
│       ├── _index.md              # 运行时选表规则
│       ├── general-dl.md          # 通用 DL 兜底
│       ├── control-dl.md          # 控制 + 深度学习
│       ├── audio-visual.md        # 声视觉 / 音频-视觉
│       └── acoustic-imaging.md    # 声学成像 / 阵列定位
├── examples/                      # 示例会话(用法演示 + 隐式触发锚点)
│   ├── control-dl-session.md
│   ├── audio-visual-session.md
│   └── boundary-decline.md        # 触发边界:批量需求转交给专门技能
└── scripts/
    ├── extract_outline.py         # 抽 PDF 章节/图表标题(需 PyMuPDF)
    └── render_page.py             # 把关键页渲成 PNG 来看图(需 PyMuPDF)
```

## 安装
**Codex**(全局):
```bash
cp -R paper-reading-guide ~/.codex/skills/
pip install -r requirements.txt   # 可选,给 scripts/ 用(PyMuPDF)
```
**Claude Code**(全局):
```bash
cp -R paper-reading-guide ~/.claude/skills/   # 给 Claude Code 用时可删掉 agents/openai.yaml
```
项目内安装则放进仓库的 `.codex/skills/` 或 `.claude/skills/`。装完重启 agent,
`/skills` 里能看到即成功。

> 本仓库根目录是省 token 主版本。`full-version/` 是完整版归档,用于对照或手动安装;
> 两者的 skill 名同为 `paper-reading-guide`,不要同时安装到同一个 skills 目录。

## 用法
进到放 PDF 的文件夹启动 agent:
```
$paper-reading-guide 带我读 papers/Haarnoja2018_SAC.pdf
```
它会先判定方向并加载对应速查表 → 给 60 秒速览卡 → 问你走全程还是只看某部分 →
一节一节讲、讲完就停。随时可问"这公式啥意思""它最大的创新在哪""和 XX 篇区别"。
读完按模板输出精读小结,建议存到 `notes/作者年份_短标题.md`。

## 扩展一个新方向(欢迎 PR)
1. 在 `references/domains/` 新建 `your-domain.md`,套用 `CONTRIBUTING.md` 里的统一结构
   (基础链路 / 核心概念 / 常见方法 / 数据集与指标 / 该方向追问项)。
2. 在 `_index.md` 的"选表规则"表里加一行信号词。
3. 提 PR。**SKILL.md 不用改**——它只认 `domains/` 下的文件 + 索引。

## 看图与扫描件
文本层读不到曲线细节,但 `scripts/render_page.py <pdf> <页码>` 能把关键页渲成 PNG,
打开看(或交给带视觉的模型读)。遇到扫描件(图片型 PDF),脚本会提示"该页几乎无
文字层",此时纯文本抽取无效,需走渲染看图 / OCR。

## 配套与边界
本技能只做"单篇交互陪读"。**批量**需求(把一堆论文整理成创新点对比表)请交给
专门的批量文献整理技能——那是独立技能,**不随本包发布**;没有也不影响本技能运行,
遇到批量需求时本技能会礼貌转交而非硬扛。

> 说明:真正被 agent 加载执行的是 `SKILL.md + references/ + scripts/`。
> `README.md`、`examples/`、`LICENSE` 是给人看的,不是运行依赖。

## License
MIT License © 拂晓 / fu xiao

## 安全提示
Agent Skills 会在你的环境中运行代码(本技能含两个 Python 脚本)。安装第三方技能前
请先阅读其 `SKILL.md` 与 `scripts/`。本技能脚本只读取你指定的本地 PDF、输出文本与
PNG,不联网、不上传。
