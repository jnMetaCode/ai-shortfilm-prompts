# 实战范例 — 产品广告 / 主打硬广（节拍驱动）

> jnMetaCode 原创实战范例（MIT）。把 5 段式结构用在**产品广告**——
> 这类题材最容易塌成塑料感 CG 高光和「悬浮在虚空里」的渲染图。
> 采用节拍同步的逐秒分镜（Stage 5，A 方案）。
>
> 概念：一支机械腕表的主打硬广，在洒满阳光的桌面上做触感十足的微距
> 揭示。把产品换掉，你就得到一副通用的广告骨架。
>
> *延伸阅读（只是灵感，未照搬——全部用我们的结构重写）：节拍驱动的
> 广告提示词套路见
> [LichAmnesia/awesome-ad-video-prompts](https://github.com/LichAmnesia/awesome-ad-video-prompts)
> （CC BY 4.0）。*
>
> **[English →](./product-commercial.md)**

---

## 动手前先定义这些变量

| 变量 | 本例取值 | 可换成… |
|---|---|---|
| `{{product}}` | 一支机械腕表 | 一只球鞋 / 一瓶香水 / 一台手机 |
| `{{material}}` | 拉丝钢表壳、蓝宝石镜面 | 针织网面 / 磨砂玻璃 / 阳极氧化铝 |
| `{{hero_action}}` | 上紧表冠，秒针扫过 | 鞋带拉紧 / 瓶盖揭开、雾气升腾 |
| `{{surface}}` | 深胡桃木桌面 | 湿石板 / 原色亚麻 / 拉丝混凝土 |
| `{{accent_color}}` | 暖琥珀色 | 冰蓝 / 牛血红 / 哑光黑 |

---

## 完整提示词（可直接复制）

### 1 · 核心主题
`高端产品广告 | 微距触感写实 | 受控硬主光 + 柔补光 | 节拍同步揭示 | 无塑料感 CG 高光、无虚空悬浮渲染`

### 2 · 人物与场景

**主体（产品）：** {{product}}——{{material}}。
先说材质、后说工艺：钢面读作*拉丝、而非镜面抛光*；镜面带一层极淡的
增透蓝色反光。瑕疵（正是它们撑起写实）：左侧表耳上一道极细微划痕，
恰好被主光勾出；表冠附近一枚半擦掉的指纹；表带皮革上最淡的一点浮尘。
一件被*触摸过*的真实物件，而不是展厅渲染图。

**场景：** 临窗的 {{surface}}，一束低斜侧光，细小尘埃在其中浮游。浅
景深——背景虚化成柔和的 {{accent_color}} 散景，绝不是平板无缝的纯色
背幕。

### 3 · 氛围与画质
ARRI Alexa 摄影机 + Laowa 24mm probe macro 探针微距镜头（真正的商业
微距工具——极近对焦、纵深感强的桌面透视）。窗左一束硬主光，机位右侧
柔和反射补光，向暗部受控衰减。克制的青暖调，有机胶片颗粒，金属上真
实的镜面高光（而非过曝的 CG bloom）。

### 4 · 运镜规则
剪成 4 个短节拍（或单镜时一段连续的探针运动）。缓慢、有意图的探针推
近，加一次横向掠过桌面的平移。
- *呼吸感：* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence."——保持微量；产品微距
  要的是稳定，不是晃动。
- *声音：* No score. Production audio only——设计过的拟音：表冠轻柔的
  咔哒、机芯细密的金属滴答、指尖擦过钢面的声音、室内底噪。（若品牌需
  要音乐垫底，在剪辑里有意加进去——别让模型自己编一段。）

### 5 · 分镜（4 节拍，约 10s）

```
0–2s · 建立（静置的物件）
动作：{{product}} 静静放在 {{surface}} 上，侧光低低掠过，一粒尘埃
      横穿画面。
运镜：从 20° 低角缓慢探针推近，朝表冠推去。
细节：表耳上的微划痕在光打到的一帧里闪了一下。

2–5s · 触碰（人手接触，不完整露脸）
动作：一只手入画；{{hero_action}}。
运镜：探针横向跟随这个动作，焦点锁在接触点上。
声音：那一个动作精准的拟音，孤立而清脆。

5–8s · 细节（微距收益）
动作：对工作部件的极致微距——秒针扫过、{{material}} 的纹理、一道真
      实的镜面亮点沿边缘滑过。
运镜：从前景纹理缓慢变焦到背后的 {{accent_color}} 散景。

8–10s · 安定（克制收尾）
动作：手撤出。{{product}} 回到静置。
运镜：定住，呼吸浮动，一片云飘过、光略微暗下来。
收尾：不砸 logo。不来旋转炫技的英雄环绕。不爆镜头光晕。只是物件归于
      静止，最后一粒尘埃穿过光线落定。
```

### 负面提示词（即梦/可灵——粘进独立负面框）
```
blurry, low resolution, soft focus, watermark, text overlay, subtitles, logo, oversaturated colors, plastic skin, glossy CG render, video-game look, 3D cartoon render, flat even studio lighting, perfectly clean flawless surfaces, blown-out highlights, floating product in empty white void, seamless infinity backdrop, frame flicker, ghosting, jarring hard cuts, lifeless locked-off camera, spinning hero rotation, cheesy lens flare
```

---

## 为什么这么搭

- **瑕疵才卖得动产品（Rule 5）。** 一道微划痕、一枚半擦掉的指纹，读
  作「真实物件、真实光线」——正是广告提示词默认那种死板 CG 渲染的反
  面。完美表面看着假；瑕疵才是写实。
- **用真实微距工具，而不是「电影感」（Rule 2）。** "ARRI + Laowa
  probe macro" 把模型锚定到真实的桌面商业素材上。「影棚产品图，4K」
  给你的是一张库存渲染图。
- **克制收尾（Rule 6）。** 不砸 logo、不英雄环绕、不光晕。物件只是归
  于静止，比揭示式的炫技更显高端——也阻止模型在结尾堆廉价广告特效。
- **节拍同步分镜。** 每个 2–3s 节拍 = 一个动作 + 一次运镜 + 一种声音。
  正是这种逐拍纪律，让 10s 广告不至于沦为含糊的漂移。

**用法**：先生成*细节*节拍（5–8s）——如果那里的微距纹理和镜面高光读
作真实，其余的就稳得住。人手接触只保留手部（露全脸会触发更严的肖像
过滤，且并不需要）。后期拼接 4 个节拍。

**模型**：Seedance 2.0 和可灵在触感微距运动上很强；Veo 3 给出最干净
的镜面/光照写实（用它的负面框，填朴素名词短语即可）。在豆包 App 上，
记住 5s/10s 预设锁——按 10s 总时长来规划节拍。
