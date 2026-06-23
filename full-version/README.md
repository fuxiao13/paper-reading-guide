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

## 安装
**Codex**(全局):
```bash
cp -R paper-reading-guide ~/.codex/skills/
pip install -r requirements.txt   # 可选,给 scripts/ 用(PyMuPDF)
```

## 用法
进到放 PDF 的文件夹启动 agent:
```
$paper-reading-guide 带我读 papers/Haarnoja2018_SAC.pdf
```
它会先判定方向并加载对应速查表 → 给 60 秒速览卡 → 问你走全程还是只看某部分 →
一节一节讲、讲完就停。随时可问"这公式啥意思""它最大的创新在哪""和 XX 篇区别"。

## 说明
这是完整版归档。它与根目录省 token 版的 skill 名同为 `paper-reading-guide`,不要同时安装。
