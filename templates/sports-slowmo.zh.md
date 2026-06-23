# 实战范例 — 高速摄影慢动作运动

> jnMetaCode 原创实战范例（MIT）。把 5 段式结构用在**高速摄影慢动作
> 运动**上——这一题材的全部功夫都在一台真正的高速摄影机（Phantom 级）
> 和那个*决定性瞬间*上。教你掌握高帧率锚点与发力细节（汗水、肌肉紧绷、
> 冲击），正是这些把有血有肉的慢动作和游戏引擎重放区分开来。
>
> 概念：一名短跑选手从起跑器上爆发，把那个决定性的蹬地瞬间冻结成极慢
> 动作。换个项目，保留这套方法纪律。
>
> *延伸阅读（取自灵感，并非照搬——全部用我们的结构重写）：电影感／运
> 动动态笔记见
> [geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts)
> （MIT）。*
>
> **[English →](./sports-slowmo.md)**

---

## 先要定义的变量

| 变量 | 本例 | 可替换为… |
|---|---|---|
| `{{athlete}}` | 起跑器上的短跑选手 | 一名拳击手／一名游泳运动员／一名滑板手 |
| `{{moment}}` | 起跑器上爆发的第一蹬 | 拳头命中／入水瞬间／翻板动作 |
| `{{detail}}` | 汗珠从眉梢甩出、肌肉紧绷 | 水如帘幕泼洒／镁粉爆开 |
| `{{venue}}` | 黄昏泛光灯下的体育场跑道 | 一间健身房／一座泳池／一处街头场地 |
| `{{palette}}` | 冷白泛光灯 + 暖肤色 | 高对比黑白／高饱和赛场 |

---

## 完整提示词（可直接复制）

### 1 · 核心主题
`高速摄影慢动作运动 | 决定性瞬间细节 | 自然场地光 | 有血有肉的发力 | 写实，无游戏引擎重放感`

### 2 · 人物与场景

**运动员：** {{athlete}}。参考上传照片，五官 100% 保留，不做美颜。真实
感全在发力上：脸部用力、咬紧牙关、肌肉紧绷颤抖、血管凸起、{{detail}}、
磨损陈旧的装备、尘土或镁粉。不是干净的英雄站姿——而是逼到生理极限的
身体。

**场景：** {{venue}}，{{palette}}。空气里有质感——尘埃、呼出的白气、
飞溅的水雾——都被慢动作显形。

### 3 · 氛围与画质
Shot on a Phantom high-speed cinema camera at ~1000fps（真正的慢动作工
具），以极慢动作回放。电影感 {{palette}} 调色，浅景深，细腻胶片颗粒。
每一处微观细节都看得清：一颗汗珠、布料波动、地面在力下的形变。

### 4 · 运镜规则
锁定或平滑跟拍，跟住 {{moment}}——高速摄影机架是稳定的，不是手持。
- *呼吸感：* keep it minimal here — a high-speed shot rides a rig;
  at most an imperceptible drift, not the usual handheld float.
- *声音：* No score. Production audio only——冲击声、爆发式的喘息、
  {{moment}} 的刮擦/水花声、低沉的人群嗡鸣，然后是慢段被拉长、扭曲了
  时间的音轨。

### 5 · 分镜（3 拍，约 10s）

```
0–2s · 蓄势（实时，张力）
动作：{{athlete}} 就位、静止、急促喘息，每块肌肉都已上满弦。
镜头：朝发力点缓慢推近。
声音：呼吸声、逐渐收紧的人群嗡鸣。

2–7s · 决定性瞬间（极慢动作——回报所在）
动作：{{moment}} 炸开——但以极慢动作呈现：{{detail}} 悬停在空中，
      布料波动，身体的全部力量逐帧读出。
镜头：跟住动作，焦点锁定在细节上。
声音：被时间拉长的冲击声 + 喘息；一切都被拉伸、变得沉重。

7–10s · 释放（缓出）
动作：动作完成；最后一滴汗落下。
镜头：定住，向实时缓缓回落。
收尾：无胜利怒吼，无炫耀英雄站姿，无光晕。只有耗尽的身体，和最后
      那滴汗落地。
```

### 负面提示词（Seedance / Kling——粘进独立负面框）
```
blurry, low resolution, watermark, text overlay, subtitles, logo, oversaturated colors, plastic CG skin, video-game replay look, game-engine render, 3D cartoon, motion interpolation artifacts, stutter, smooth-but-fake slow motion, flat even studio lighting, perfectly clean flawless gear, distorted face, extra fingers, melting/morphing geometry, frame flicker, ghosting, lifeless locked-off camera, cheesy lens flare
```

---

## 为什么这么搭

- **写「高帧率工具」，而不是「慢动作」（Rule 2）。** "Phantom high-speed
  camera at 1000fps" 把模型锚定到真实的高速摄影上。写「slow-mo,
  cinematic」只会得到一段抖动的插帧假货。
- **发力细节 = 真实感（Rule 5）。** 用力的脸、紧绷的肌肉、汗水、磨损
  的装备。干净的英雄站姿读起来像 CG；正是这份用力和飞溅的汗水让画面
  有血有肉。
- **决定性瞬间就是整条镜头。** 蓄势（实时）→ 唯一那个瞬间用极慢动作
  → 缓出。别什么都慢动作；正是这份对比给了回报应有的分量。
- **克制收尾（Rule 6）。** 耗尽的身体 + 一滴落下的汗，而不是胜利怒
  吼。让画面保持真实，也避免模型加上凯旋特效。

**用法**：先生成*决定性瞬间*这一拍（2–7s）——如果慢动作读起来像真实
的高速素材（而非插帧糊成一团）、汗水/发力细节立得住，就围着它搭建。
盯紧假插帧的痕迹，把它们负掉。

**模型**：Kling 和 Seedance 对动态真实感处理得不错；Veo 3 给出最干净
的高细节慢动作和原生冲击音效。避开模型默认的「平滑插帧」——靠负面框
把画面维持成真正的高速捕捉感。
