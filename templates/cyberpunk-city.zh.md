# 实战范例 — 赛博朋克城市漫游（氛围向，以环境为主角)

> jnMetaCode 原创实战范例（MIT）。把 5 段式结构用在**氛围环境片**上——
> 主角是*城市本身*，而非某个人物。与
> [cyber-wuxia](../prompts/cyber-wuxia.md) 一起补齐整套赛博系列。教你那套
> 粗粝赛博的相机组合（Sony Venice + Canon K-35）以及「活的环境 = 氛围」。
>
> 概念：在一座被雨水浸透的霓虹巨城里，缓慢夜游，一个孤身人影最终消融进
> 人群。换掉城市的味道，保留氛围的纪律。
>
> *延伸阅读（灵感来源，非照搬——全部用我们的结构重写）：赛博朋克／电影
> 感城市场景，梳理自
> [hr98w/awesome-sora-prompts](https://github.com/hr98w/awesome-sora-prompts)
> （CC0）与 [geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts)
> （MIT）。*
>
> **[English →](./cyberpunk-city.md)**

---

## 先要定义的变量

| 变量 | 本例取值 | 可替换为… |
|---|---|---|
| `{{city_flavour}}` | 密集的东亚霓虹街边市集 | 野兽派企业峡谷 / 被水淹的后巷 |
| `{{weather}}` | 持续的冷雨、体积感薄雾 | 飘散的酸雾 / 落灰 |
| `{{neon_palette}}` | 品红 + 青，压在墨绿底色上 | 钠光橙 + 绿 / 冷蓝 + 红 |
| `{{figure}}` | 一个孤身戴兜帽的人影 | 一个骑车的快递员 / 完全没有人影 |
| `{{move}}` | 沿街缓慢前推的轨道镜头 | 一架下降的无人机 / 一个静止长镜 |

---

## 完整提示词（可直接复制）

### 1 · 核心主题
`霓虹赛博朋克大都会 | 雨夜漫游 | 体积感薄雾 | 低饱和墨绿底色 + 霓虹点缀 | 氛围写实，不要游戏 CG 城市，不要干净渲染`

### 2 · 人物与场景

**主体（城市本身）：** 夜里的 {{city_flavour}}，{{weather}}。环境是*活
的*——这正是它成为氛围、而非一张接景绘画的原因：雨在落、在积水，通风口
冒出蒸汽，一块 {{neon_palette}} 招牌闪烁着、有一根坏掉的灯管，倒影在水
洼里荡漾，行人化作柔和的剪影经过。污渍、磨损、湿漉漉的表面无处不在——
不完美才是写实。

**人影（可选，次要）：** {{figure}}，在画面里很小，永远不是焦点——它给
城市一个尺度感，然后消融进去。

### 3 · 氛围与画质
用 Sony Venice + Canon K-35 系列拍摄（那套粗粝硬科幻组合），变形宽银幕，
霓虹打出的水平镜头光晕。低饱和墨绿底色，{{neon_palette}} 的点缀穿透薄
雾。体积感光束，有机的胶片颗粒，湿地面上真实的反光高光（而不是过曝的
CG bloom）。

### 4 · 运镜规则
{{move}}——缓慢而克制；城市应当是漂过去，而不是飞驰。
- *呼吸感：* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence."
- *声音：* No score。只用现场／环境音——稳定的雨声、远处的车流与警笛、
  霓虹的电流嗡鸣、人群闲谈的碎片、低沉的城市底噪。合成器长音只允许作为
  极淡的环境质感，绝不当成一条配乐。

### 5 · 分镜（逐秒，约 10s 单镜漫游）

```
0–3s · 进入
动作：漫游开始——{{move}} 推进 {{city_flavour}}，雨水划过画面，霓虹在
      湿镜头上拖出晕染。
镜头：缓慢、压低。倒影引着视线往街道深处走。
声音：雨声 + 远处车流先立住；霓虹的嗡鸣在近处。

3–7s · 穿行
动作：经过那块闪烁的 {{neon_palette}} 招牌（一根灯管已坏），蒸汽横穿画
      面，{{figure}} 作为剪影经过。
镜头：保持漂移；水洼倒影随着某物经过而荡起涟漪。
细节：污渍与磨损接住光——那种住人留下的质感。

7–10s · 消融
动作：{{figure}} 融进流动的人群，消失了；街道不为谁停下，继续。
镜头：继续漂移，呼吸浮动，不要停在那个人影上。
收尾：没有揭示，没有主角回头，没有标题。只有招牌再闪一次，雨继续落在
      这条显得空荡的街上。
```

### 负面提示词（Seedance / 可灵——粘进独立负面框）
```
blurry, low resolution, soft focus, watermark, text overlay, subtitles, logo, oversaturated colors, plastic skin, glossy CG render, video-game look, clean render, 3D cartoon render, flat even studio lighting, perfectly clean dry surfaces, dead static matte-painting city, blown-out neon bloom, melting/morphing geometry, warped signage text, frame flicker, ghosting, jarring hard cuts, lifeless locked-off camera, cheesy lens flare
```

---

## 为什么这么搭

- **活的环境 = 氛围（第 2 段的纪律）。** 静止的城市读起来就是一张接景绘
  画，像背景板。雨在积水、蒸汽、一根闪烁的坏灯管、荡漾的倒影、经过的剪
  影——环境里的运动，才让它显得真实、有人住过。
- **粗粝赛博的相机组合（Rule 2）。** 「Sony Venice + Canon K-35」把模型
  锚到硬科幻摄影上。「赛博朋克城市，霓虹，4K」给你的则是一段游戏过场
  动画。
- **不完美即写实（Rule 5）。** 污渍、磨损、湿表面、一根坏掉的霓虹灯管。
  干净 = CG。磨损本身就是重点。
- **人影消融（Rule 6）。** 不给主角揭示，不给标题卡。让人影消失进人群，
  才能守住氛围感，避免模型把它转成一段人物戏。

**用法**：先生成 *3–7s「穿行」* 那一拍——如果湿倒影、霓虹晕染和薄雾在那
里读起来是真的，其余就稳了。保持一个缓慢连续的运动；这个类型一旦相机飞
驰起来就死了。

**模型**：可灵和 Seedance 2.0 对湿霓虹的运动和反光处理得不错；Veo 3 给出
最干净的体积光和原生环境声。留意屏幕上招牌文字会被扭曲——把 "warped
signage text" 放进负面框，或者让招牌保持抽象／不带文字。
