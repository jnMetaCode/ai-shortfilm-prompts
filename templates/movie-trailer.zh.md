# 实战范例 — 电影感预告片(层层升级的多镜剪辑)

> jnMetaCode 原创实战范例(MIT)。把 5 段式结构用在**预告片**上——
> 一段层层升级的多镜蒙太奇,要在约 15 秒内暗示出一整个世界。建立在
> [multi-shot-narrative.zh.md](./multi-shot-narrative.zh.md) 与
> [genre-camera-sop.zh.md](./genre-camera-sop.zh.md) 的「史诗」运镜块之上。
> 教会你预告片赖以为生的那一件事:**刻意设计的声音 + 层层升级的节奏**。
>
> 概念:一支科幻惊悚预告片——安静的建场、一个引爆点、层层升级的快切、
> 一记硬切黑场、一拍标题。换掉世界,保住节奏。
>
> *延伸阅读(只取灵感,未照搬——全部用我们的结构重写):
> [snubroot/Veo-3-Prompting-Guide](https://github.com/snubroot/Veo-3-Prompting-Guide)
> 里的电影感/营销预告片分类(只取结构)以及
> [zhangchenchen/awesome_sora2_prompt](https://github.com/zhangchenchen/awesome_sora2_prompt)
> (MIT)。*
>
> **[English →](./movie-trailer.md)**

---

## 开拍前要先定义的变量

| 变量 | 本例取值 | 可替换为… |
|---|---|---|
| `{{world}}` | 一座被海水淹没的近未来沿海城市 | 一处冰封的边境殖民地 / 一座饱受战火的首都 |
| `{{protagonist}}` | 一名孤身的潜水工程师 | 一个疲惫的侦探 / 一个拿着奇怪装置的孩子 |
| `{{threat}}` | 水下某个庞然之物正在移动 | 不断蔓延的大停电 / 逼近的风暴墙 |
| `{{title_word}}` | 一个自造的单词标题,例如 "TIDEBREAK" | 你项目的标题 |
| `{{grade}}` | 去饱和的钢蓝调 | 琥珀尘黄 / 病态绿 |

---

## 完整提示词(可直接复制)

### 1 · 核心主题
`电影感预告片 | 层层升级的多镜蒙太奇 | 全片锁定一种胶片色 | 由声音设计驱动 | 克制的揭示,无俗套旁白,无快速频闪硬切`

### 2 · 人物与场景

**人物(主角):** {{protagonist}}。参考上传照片,五官 100% 保留,
不做美颜。带瑕疵:脸上的雨/汗、一道疤或疲惫的眼神、磨旧的实用装备
(不是干净的戏服)。只出现在 2–3 个镜头里——预告片是暗示,不是解释。

**世界({{world}}):** 真正的主角。靠质感堆出来,而不是靠交代说明——
湿混凝土、明灭的招牌、残骸、天气。{{threat}} 只能被感觉到,绝不完全
现身。

### 3 · 氛围与画质
宽景世界镜头用模拟 IMAX 胶片摄影机 + Panavision C-series(35mm,f/4);
人物近景用 Sony Venice + Canon K-35。**全片每个镜头锁定同一种胶片色:
{{grade}},低对比,有机胶片颗粒。** 一支每切一刀就换个观感的预告片会
散架——色调就是把它黏成一体的胶水。

### 4 · 运镜规则
多镜头剪辑,**层层升级的节奏**:开头长镜久持,随着张力上升切点越来越
短,然后在结尾前留一拍静止。
- *呼吸感:* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence."
- *声音(刻意设计的,不是套一首歌):* 不要硬塞一段流行配乐。用现场同期
  声 + 刻意设计的预告片声音——在升级段下方铺一层低频次声逐渐抬升,在
  某个关键切点上来一记硬冲击("braam"),然后在标题前留一拍近乎静默。
  逐拍把声音写清楚;不要让模型自己脑补一段通用的配乐垫底。

### 5 · 分镜(6 镜,约 15 秒)

```
Shot 1 — 建场(长镜久持,安静)
  {{world}} 的宽景,{{grade}} 色调,缓慢推进。几近静止。只有微弱环境
  音。暴风雨前的平静。

Shot 2 — 主角(近景)
  紧贴 {{protagonist}} 的脸,一闪而过的不安。画面下方一个遥远的低沉
  声音开始响起。

Shot 3 — 引爆点(第一个 {{threat}} 的迹象)
  中景——有什么不对劲:水面晃动、一盏灯熄灭、一个传感器读数飙升。次
  声抬升从这里开始。

Shot 4–5 — 升级(切点变短)
  一对急促的快拍:运动、反应、{{threat}} 的惊鸿一瞥(绝不完整揭示)。
  镜头更躁动。抬升继续爬升。

Shot 6 — 硬切黑场 + 标题
  在最后一个动作上来一记硬冲击,切到黑场。一拍静默。单个单词
  {{title_word}} 淡入,再淡出。
  收尾:没有主角金句,没有旁白,没有爆炸蒙太奇。只有切黑、最后一记声
  音、还有标题。
```

### 负面提示词(Seedance / Kling——粘进独立负面框)
```
blurry, low resolution, soft focus, watermark, text overlay, subtitles, logo, distorted face, asymmetric eyes, extra fingers, deformed hands, melting/morphing geometry, oversaturated colors, plastic skin, glossy CG render, video-game look, 3D cartoon render, flat even studio lighting, grade shifting between shots, rapid epileptic strobe cuts, cheesy lens flare, frame flicker, ghosting, lifeless locked-off camera, generic stock music feel
```

---

## 为什么这么搭

- **一种色调就是把它黏成一体的胶水(把 Rule 1 用在剪辑上)。** 多镜预告
  片翻车的头号原因,就是每切一刀换一个观感。全片 6 镜锁死 {{grade}};
  让节奏和声音去扛升级,而不是靠换色调。
- **声音设计逐拍写清楚(Rule 4 的预告片变体)。** 预告片有一半是声音。
  我们不会只说一句「只用同期声」就完事——而是把抬升、冲击、标题前的静
  默都写成脚本,这样模型才不会贴一段通用配乐垫底。
- **暗示,别解释(Rule 6)。** {{threat}} 只给惊鸿一瞥,绝不完整揭示;
  主角只出现在 2–3 镜。结尾落在切黑 + 一个单词上,而不是一句主角台词。
  正是这份克制,才让预告片有「悬」的味道。
- **层层升级的切点节奏。** 长镜久持 → 切点收短 → 一拍静止。读起来像
  「预告片」的,是这套节奏,而不是花哨的特效。

**用法**:先跑 Shot 1(建场)和 Shot 6(标题拍),把色调和结尾定死,再
在两者之间搭升级段。整支控制在 ≤6 镜以内——预告片一旦解释过多就废了。
后期拼接,在时间线上做声音设计。

**模型**:宽景拍用 Veo 3 和 Sora 2,世界一致性和原生声音最强;Kling
对动作升级的快切非常出色。每镜控制在 ≤8s。在豆包 app 上,按每镜
5s/10s 的预设锁来规划。
