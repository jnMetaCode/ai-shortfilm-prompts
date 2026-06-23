# 实战范例 — 旅行 Vlog / 在地感

> jnMetaCode 原创实战范例（MIT）。把 5 段式结构用在**旅行 Vlog**——
> 一段真实手持的蒙太奇，要在寥寥几个镜头里让观众*真切感受到一个地方*。
> 教的是「在地蒙太奇」结构（wide → detail → people → food）、真实微单
> 手持的质感，以及用具体的感官细节(而非千篇一律的无人机套路)去标记一
> 个地方。
>
> 概念：海边老城的一个清晨。把目的地换掉，蒙太奇的纪律保留。
>
> *延伸阅读（仅作灵感，未照搬——全部用我们的结构重写）：VLog / 旅行
> 蒙太奇的套路梳理自
> [jax-explorer/awesome-veo3-videos](https://github.com/jax-explorer/awesome-veo3-videos)
> （无许可证——仅供灵感参考）。*
>
> **[English →](./travel-vlog.md)**

---

## 先把变量定下来

| 变量 | 本例取值 | 可替换为… |
|---|---|---|
| `{{place}}` | 清晨的海边老城 | 夜市 / 高山村落 / 沙漠公路 |
| `{{wide}}` | 太阳升过瓦顶屋脊与海面 | 一座庙门 / 一条霓虹街 / 沙丘 |
| `{{detail}}` | 街边煎锅冒起的热气、墙头一只猫 | 沏茶的手 / 一盏灯笼 / 沙上的脚印 |
| `{{people}}` | 摊主在笑、孩子追跑过巷子 | 扫地的僧人 / 街头艺人 / 渔夫 |
| `{{traveler}}` | Vlogger，只从背后一闪而过 | 一对情侣 / 独行背包客 / 只拍手 |

---

## 完整提示词（可直接复制）

### 1 · 核心主题
`旅行 Vlog | 真实手持蒙太奇 | golden-hour 自然光 | 在地感 | 真实不摆拍、无浮夸无人机素材套路`

### 2 · 人物与场景

**旅行者（次要）：** {{traveler}}——很少成为焦点，多数时候只是一个存
在，给这个地方一个尺度感和一个 POV。若上传了照片就参考；否则只拍手 /
越肩。

**地方（真正的主角）：** {{place}}。这个地点要靠*具体的感官细节*来讲，
而不是一张明信片：{{detail}}、{{people}}、真实的肌理、真实的光、未经摆
布的生活。要有那些一看就是真实旅拍的瑕疵：构图不完美、一道镜头眩光、
风、一个路人横穿画面。

### 3 · 氛围与画质
用 mirrorless 微单手持拍摄（真实旅拍创作者的看法——既不是电影机，也不
是无人机）：暖调 golden-hour 自然光、轻微胶片颗粒、真实色彩、略带瑕疵
的手持曝光。真实、当下，不是光鲜的旅游局宣传片。

### 4 · 运镜规则
手持蒙太奇的能量——几个短镜头堆出一个地方：一个 wide 起势、贴近的细节、
一个人的瞬间、一个走进去的运动镜头。
- *呼吸感：* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence."——这里可以稍微更鲜活
  一点；真实旅拍本就有能量和细小的重新构图。
- *声音：* No score. 只用现场 / 环境声——把这个地方一样样列出来：浪声
  与海鸥、煎锅的滋滋声、当地语言的市集喧闹、石板上的脚步、风。（要发
  社媒的话，后期叠一首当下流行的音乐。）

### 5 · 分镜（4 镜，约 12 秒）

```
Shot 1 — Arrive（wide，起势）
  {{wide}}，金色晨光。手持，缓缓漂移推入。

Shot 2 — Detail（具体起来）
  贴近拍 {{detail}}——那个一看就知道这是哪里的肌理。快、亲密、浅景深。

Shot 3 — People（这个地方是活的）
  {{people}}——一个未经摆布的人的瞬间，不是摆拍。旅行者可以从画面里
  穿过。

Shot 4 — Move（把我们带进去）
  跟着 {{traveler}} 走进场景的步行 POV / 越肩镜头，地方在前方一点点
  铺开。
  收尾：不要无人机转圈的炫技镜头，不要标题卡，不要「订阅」。就是旅行
  者继续往这个地方里走，环境声延续着。
```

### 负面提示词（Seedance / 可灵——粘进独立负面框）
```
blurry, low resolution, watermark, text overlay, subtitles, logo, oversaturated colors, glossy tourism-board look, fake HDR, plastic CG render, video-game look, 3D cartoon, flat even studio lighting, staged posed tourists, empty lifeless streets, distorted faces, extra fingers, melting/morphing geometry, frame flicker, ghosting, lifeless locked-off camera, generic drone stock shot, subscribe button overlay
```

---

## 为什么这么搭

- **在地感靠具体细节,不靠明信片。** 旅行 Vlog 打中人,是因为它拍出了
  *这个确切的地方*——真实煎锅冒的热气、墙头一只猫、喧闹里的当地语言
  ——而不是一段套路化的无人机扫摇。具体的感官细节胜过风景。
- **微单手持,不用电影机也不用无人机（Rule 2，按题材匹配）。** 真实旅
  拍创作者的看法就是微单手持配暖光。光鲜的无人机 / 三脚架看法会让画面
  像旅游广告,毁掉那种「我当时在场」的感觉。
- **蒙太奇结构:wide → detail → people → move。** 这四拍的形状能快速
  堆出一个地方。它是旅行 Vlog 的语法,不是叙事。
- **克制收尾（Rule 6）。** 继续往地方里走,而不是无人机炫技转圈或订阅
  卡。保住真实感。

**用法**:先跑 *detail* 和 *people* 两镜——它们扛着「在地感」;如果这俩
够具体、够鲜活,wide 和 move 就替它们做框。用这个地方独有的东西去标记
它在哪。

**模型**:可灵和 Seedance 对手持能量和人群处理得都不错;Veo 3 给出最好
的 golden-hour 写实和原生环境声。要发社媒,后期叠一首流行曲。
