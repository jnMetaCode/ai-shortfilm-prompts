# 实战范例 — 音乐 MV / 表演（卡点剪辑）

> jnMetaCode 原创实战范例（MIT）。把 5 段式结构用在**音乐 MV** 上——
> 它是 [movie-trailer.md](./movie-trailer.md) 的刻意反面:预告片禁用音乐
> 铺底、专门设计音效;而 MV 是唯一**「歌本身才是重点」**的题材。本模板
> 教你什么时候*该*要音乐,以及怎么卡着节拍剪。
>
> 概念:一位表演者置身风格化空间,跟着一首曲子的节奏剪辑。换掉艺人、
> 视觉风格、节奏即可;保留卡点剪辑的纪律。
>
> *延伸阅读(灵感来源,非照搬——全部用我们的结构重写):
> [jax-explorer/awesome-veo3-videos](https://github.com/jax-explorer/awesome-veo3-videos)
> 里的表演 / 音乐分类(无许可证,仅作灵感)与
> [geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts)
> 里的音画同步笔记(MIT)。*
>
> **[English →](./music-video.md)**

---

## 先定义这些变量

| 变量 | 本例取值 | 可替换为… |
|---|---|---|
| `{{artist}}` | 一位独唱歌手 | 一支乐队 / 一名舞者 / 一位器乐演奏者 |
| `{{genre_tempo}}` | 梦幻 synth-pop,~100 BPM,中等能量 | trap ~140 / 抒情慢歌 ~70 / hyperpop ~160 |
| `{{look}}` | 夜晚屋顶,霓虹照亮的雨 | 纯白无缝背景墙 / 黄昏时分的沙漠 |
| `{{grade}}` | 品红 + 青在深蓝之上的霓虹色 | 高调粉彩 / 暖调胶片 |
| `{{hook_moment}}` | 约第 4 秒副歌爆发那一刻 | 整段剪辑层层推向的那个重拍 |

---

## 完整提示词（可直接复制）

### 1 · 核心主题
`音乐 MV | 卡点多镜剪辑 | 一种鲜明色调 | 表演能量 | 不做对口型字面化、不做无动机乱剪`

### 2 · 人物与场景

**表演者:** {{artist}}。参考上传照片,五官 100% 保留,不做美颜。真实
的表演能量——汗水、呼吸、快动作的运动模糊、一缕散落贴在脸上的头发。
带瑕疵才像真表演,而不是打磨过头的 CG 偶像。

**场景:** {{look}},围绕 {{grade}} 搭建。空间随音乐起反应——灯光脉动、
雨水卡上节拍、倒影流动。

### 3 · 氛围与画质
Shot on Sony Venice with anamorphic primes;在 {{grade}} 里做大胆的风格
化调色(MV 的色彩可以比叙事片推得更狠)。胶片颗粒、真实霓虹/实景光,
快动作允许运动模糊。全片只认定一种视觉风格。

### 4 · 运镜规则
**卡点剪辑**的多镜剪辑——verse 段保持长镜头,进 {{hook_moment}} 切得更
快,运镜落在重拍上。
- *呼吸感:* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence." ——这里它可以骑着节奏走,
  比叙事镜头再活一点。
- *声音(唯一的例外——这里就是要音乐):* 和这里其它每一个模板都不同,
  这个题材本就建立在一首曲子上。指定**节奏、曲风和能量**
  ({{genre_tempo}}),让模型的运动和剪辑卡到节拍上。如果你有自己的歌,
  就生成到静音/临时音轨,后期再把真歌铺进去。除非你要,否则别让模型
  自己编歌词/人声。

### 5 · 分镜（卡点剪辑，约 12s）

**FORMAT 头——先把节拍数算死：**
`16:9 | 12s | ~100 BPM | 6 shots | beat-synced` —— 把 tempo + 镜头数写在最前，
模型才会把每个 cut 落在重拍上、而不是乱飘。收尾踩高潮：BGM 戛然而止、画面定格。

```
0–4s · Intro / verse（让它呼吸）
Action: {{artist}} 置身 {{look}},表演进行中,{{grade}} 立住基调。
        更慢、更长的停留,贴合 verse 段。
Camera: 缓慢推进或单次缓慢弧线运动。呼吸浮动。
Beat:   切镜落在重拍上,稀疏。

4–8s · Hook / drop（{{hook_moment}} —— 兑现的高潮）
Action: 能量拉升——表演者唱到副歌,空间起反应(灯光脉动、雨势骤起),
        动作变利落。
Camera: 切得更快,一次运镜狠狠落在 drop 上。
Beat:   切镜节奏进 hook 时翻倍。

8–12s · Outro（克制收尾）
Action: 能量回落;最后一个停住的表演画面。
Camera: 停住,呼吸浮动。
Close:  画面上无歌词字幕、无 logo 卡片、无定格俏皮眨眼。只是表演者和
        空间随乐句结束而归于平静。
```

### 负面提示词（即梦/可灵——粘进独立负面框）
```
blurry, low resolution, watermark, text overlay, lyric subtitles, logo, karaoke text, distorted face, asymmetric eyes, extra fingers, deformed hands, lip-sync mismatch, plastic CG skin, glossy idol render, video-game look, 3D cartoon, flat even studio lighting, grade shifting randomly between shots, unmotivated epileptic cuts, frame flicker, ghosting, lifeless locked-off camera
```

---

## 为什么这么搭

- **唯一「该用音乐」的题材(Rule 4 反转)。** 其它每个模板都说「无配乐,
  只用现场声」。MV 是例外——它本就建立在一首曲子上。所以我们指定
  节奏/曲风/能量让运动和剪辑同步,而且(和预告片正相反)我们*想要*这段
  音乐,而不是禁掉它。
- **卡点剪,别乱剪。** MV 和随便堆的混剪的区别,就在于切镜和运镜落在
  重拍上、剪辑进 hook 时加速。把分镜映射到歌的结构(verse → hook →
  outro)上,而不是只对着钟表秒数。
- **一种鲜明色调(Rule 1 的 MV 方言)。** MV 的色彩可以比叙事片推得更
  狠——但仍然是*一种*认定的视觉风格,而不是每个镜头换一个滤镜。
- **表演的瑕疵(Rule 5)+ 克制收尾(Rule 6)。** 汗水、呼吸、运动模糊让它
  像真表演;收在一个归于平静的画面(而非歌词卡或 logo),才保持电影感。

**用法**:先定下歌的结构,再把切镜映射上去——先生成 *hook* 这个 beat,
因为它是兑现的高潮。如果你有真歌,就生成到临时音轨/静音,后期再同步
真曲子。让表演者的脸在各镜头间保持一致(先生成 hook 帧来锁住长相)。

**模型**:Veo 3 和 Sora 2 处理表演动作、以及(若你需要的)原生音频最
好;Kling 3.0 在节奏性动作和多语言对白上很强。要对自己的歌做真正的对
口型,后期铺进去,别指望生成的人声。
