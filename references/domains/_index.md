# 领域速查表索引(运行时:选表)

按论文方向选**一张或多张**速查表作为讲解基准;判不准就用 `general-dl.md` 兜底。
(新增方向 / 速查表的统一结构与贡献流程见仓库根目录 `CONTRIBUTING.md`。)

## 选表规则(看标题/摘要里的信号词)
| 信号词 | 选这张表 |
|---|---|
| 强化学习 / RL / policy / reward / MPC / 控制 / 系统辨识 / 模仿学习 / sim-to-real / 机器人控制 / Koopman / 稳定性 | `control-dl.md` |
| 视听 / audio-visual / 声源(视觉)定位 / 视听分离 / 跨模态 / sounding object / lip / AV fusion | `audio-visual.md` |
| 麦克风阵列 / 波束形成 / beamforming / DAMAS / CLEAN-SC / 声成像 / 声源定位(纯音频阵列) | `acoustic-imaging.md` |
| 以上都不沾,但是深度学习论文 | `general-dl.md` |

可同时选两张:如"用视听信息做机器人控制" → `control-dl.md` + `audio-visual.md`。
