# 实战范例 — 时尚片 / 编辑大片 Look Book

> jnMetaCode 原创实战范例（MIT）。把 5 段式结构用在**时尚片**上——
> 这里没有剧情：**运动中的服装**与时装光才是主角。教的是「运动即内容」、
> 时装布光、以及质感胜过叙事。
>
> 概念：一位模特穿着飘逸长外套，布料在受控的风中运动，按高端时尚大片
> 的方式拍。换个造型，节奏照旧。
>
> *延伸阅读（取灵感，非照搬——全部用我们的结构重写）：商业／编辑大片
> 的范式参见
> [LichAmnesia/awesome-ad-video-prompts](https://github.com/LichAmnesia/awesome-ad-video-prompts)
> （CC BY 4.0）与 [geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts)
> （MIT）。*
>
> **[English →](./fashion-film.md)**

---

## 先要定义的变量

| 变量 | 本例取值 | 可替换为… |
|---|---|---|
| `{{model}}` | 一位穿着廓形长外套的模特 | 街头潮装 / 高定礼服 / 剪裁西装 |
| `{{fabric_motion}}` | 外套在缓风中扫动 | 裙摆涟漪 / 围巾拖曳 |
| `{{set}}` | 只有一扇硬光窗户的空旷水泥摄影棚 | 沙丘 / 大理石厅 / 霓虹小巷 |
| `{{light}}` | 高窗一道硬主光，深重阴影 | 高调全白 / 明暗对照 / 彩色色片 |
| `{{grade}}` | 低饱和、肤色偏暖 | 浓郁编辑黑白 / 哑光大地色 |

---

## 完整提示词（可直接复制）

### 1 · 核心主题
`时尚片 | 编辑式运动 | 受控硬光 + 质感 | 自信的静与动 | 高端时尚写实，无目录册僵硬感`

### 2 · 人物与场景

**模特：** {{model}}。参考上传照片，五官 100% 保留，不美颜、不做塑料
感精修——真实带质感与毛孔的皮肤、一缕乱发、自然的从容。动作是编辑式的：
克制、自信、略带疏离；不是带笑的目录册摆拍。

**服装（共同主角）：** 服装占了画面的一半。{{fabric_motion}}——真实的
布料重量、看得见织纹、随空气与身体运动的褶皱与垂坠。

**场景：** {{set}}，{{light}}。

### 3 · 氛围与画质
Shot on ARRI Alexa with vintage primes，编辑式{{grade}}。一道受控硬主
光，深重衰减，柔和负补光——时装布光是塑形，不是打平。细腻胶片颗粒，
真实的织物与皮肤质感，浓郁阴影。

### 4 · 运镜规则
围绕服装设计的缓慢、克制的运动——一个缓推、一次掠过模特的横移、一个
让 {{fabric_motion}} 读得出来的转身。
- *呼吸感：* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence."
- *声音：* No score（或者，如果是走秀剪辑，配一条有节奏的音乐铺底——
  编辑式时尚片可以像 MV 那样带音乐）。Production audio：布料运动、地面
  脚步、风扇的气流、环境底噪。

### 5 · 分镜（3 拍，约 10s）

```
0–3s · 质感（细节卖布料）
动作：微距拍 {{model}} 的服装——织纹、一道缝线、垂坠、光斜掠过
      {{fabric_motion}}。
运镜：对着质感缓推，浅景深。

3–7s · 运动（运动中的服装）
动作：拉到 {{set}} 中的全身；模特移动，{{fabric_motion}} 兜住空气和
      硬{{light}}。
运镜：缓慢横移或一个转身，呼吸浮动，让布料引导视线。

7–10s · 编辑式定格（克制收尾近景）
动作：模特落定成一个自信、静止的编辑式姿态；布料归于静止。
运镜：停住，呼吸浮动。
收尾：不对镜笑、不打 logo 卡、不转圈。只是一个停住的编辑式画面，布料
      在硬光里沉落。
```

### 负面提示词（Seedance / 可灵——粘进独立负面框）
```
blurry, low resolution, watermark, text overlay, subtitles, logo, plastic retouched skin, doll-like face, oversaturated colors, glossy CG render, video-game look, 3D cartoon, flat even catalog lighting, smiling stock-photo pose, stiff mannequin, brand-new fabric with no movement, distorted face, extra fingers, deformed hands, melting/morphing cloth, frame flicker, ghosting, lifeless locked-off camera, cheesy lens flare
```

---

## 为什么这么搭

- **运动是内容，不是剧情。** 时尚片没有故事——光里运动的服装才是主角。
  把分镜围着布料运动和一个编辑式定格搭，别围着事件搭。
- **编辑式光塑形（Rule 2／氛围）。** 一道深衰减的硬主光，不是平板的目
  录册光。「ARRI + vintage primes，一道硬主光」锚定高端时尚摄影；
  「studio fashion shoot, bright」给的是僵硬的目录册感。
- **真实质感胜过磨皮（Rule 5）。** 真实的皮肤毛孔、织物纹理与垂坠、一
  缕乱发。塑料感精修的皮肤和崭新不动的布料看起来就是 CG；质感和运动才
  是奢侈所在。
- **克制的编辑式收尾（Rule 6）。** 一个自信的停住姿态，不对镜笑、不转
  圈。这样才是编辑大片，不是目录册。

**用法**：先跑「运动」那拍（3–7s）——时尚片活在布料怎么动；只要那里的
垂坠和硬光读着真实，其余的就稳了。让模特造型在各镜间保持一致（先生成
定格那一拍把它锁住）。

**模型**：Veo 3 和 Sora 2 在布料物理与编辑式肤质／光上最佳；可灵在运动
上很强。要走秀音乐铺底就在后期铺（节拍对齐见 [music-video.md](./music-video.md)）。
