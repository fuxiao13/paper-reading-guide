# 领域速查表索引(选表 + 扩展规则)

陪读开场时,按论文方向选**一张或多张**速查表作为讲解基准。判不准就问用户一句,
或直接用 `general-dl.md` 兜底——它对任何深度学习论文都成立。

## 选表规则(看标题/摘要里的信号词)
| 信号词 | 选这张表 |
|---|---|
| 强化学习 / RL / policy / reward / MPC / 控制 / 系统辨识 / 模仿学习 / sim-to-real / 机器人控制 / Koopman / 稳定性 | `control-dl.md` |
| 视听 / audio-visual / 声源(视觉)定位 / 视听分离 / 跨模态 / sounding object / lip / AV fusion | `audio-visual.md` |
| 麦克风阵列 / 波束形成 / beamforming / DAMAS / CLEAN-SC / 声成像 / 声源定位(纯音频阵列) | `acoustic-imaging.md` |
| 以上都不沾,但是深度学习论文 | `general-dl.md` |

可同时选两张:比如"用视听信息做机器人控制"→ `control-dl.md` + `audio-visual.md`。

## 每张表的统一结构
1. **基础链路 / 问题设定**:这个方向在解决什么、典型 pipeline。
2. **核心概念**:讲解时必须用对的术语与直觉。
3. **常见方法/范式**:把论文归到哪一类,便于谈"相对前人新在哪"。
4. **常用数据集与指标**:评价口径。
5. **该方向追问项**:配合通用 `question-checklist.md` 用的方向专属问题。

## 怎么加一个新方向(给贡献者)
1. 在本目录新建 `your-domain.md`,套用上面的"统一结构"。
2. 在本文件的"选表规则"表里加一行信号词。
3. 提个 PR。SKILL.md 不用改——它只认 `references/domains/` 下的文件 + 本索引。
