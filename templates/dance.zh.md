# 实战范例 — 舞蹈 / 编舞影片

> jnMetaCode 原创实战范例（MIT）。把 5 段式结构用在**舞蹈影片**上——
> 它是 [music-video.md](./music-video.md) 的反面：MV 由*剪辑*堆出来，舞蹈
> 影片则停在*身体的连续运动*上。教你全身捕捉、身体卡拍，以及「别裁掉
> 动作」的克制。
>
> 概念：一名独舞的当代舞者，在一座空旷大厅里，一镜流畅到底。换风格、换
> 空间都行，但守住「身体连续」这条规矩。
>
> *延伸阅读（只作灵感，未照搬——全部用我们的结构重写）：表演/舞蹈类
> 范式见
> [jax-explorer/awesome-veo3-videos](https://github.com/jax-explorer/awesome-veo3-videos)
> （无授权协议——仅作灵感参考）。*
>
> **[English →](./dance.md)**

---

## 先定义这些变量

| 变量 | 本例取值 | 可替换为… |
|---|---|---|
| `{{dancer}}` | 一名独舞的当代舞者 | 街舞/嘻哈舞团 / 芭蕾双人 |
| `{{style_tempo}}` | 流畅当代舞，~90 BPM，渐强 | krump ~150 / 华尔兹 ~84 / breaking ~110 |
| `{{space}}` | 一座洒满阳光的空旷水泥大厅 | 黄昏的屋顶 / 黑色舞台 / 街头 |
| `{{move}}` | 一段由地面盘旋而起的舞句 | 定格-爆发组合 / 跳跃连段 |
| `{{grade}}` | 暖色硬窗光，长长的影子 | 单点光强明暗对比 / 冷调日光 |

---

## 完整提示词（可直接复制）

### 1 · 核心主题
`舞蹈影像 | 全身连续运动 | 身体卡节拍 | 锁一档大胆调色 | 真实身体运动,不要僵硬 mocap 感、不要碎切`

### 2 · 人物与场景

**舞者：** {{dancer}}。参考上传照片，五官 100% 保留，不做美颜。真实感
来自发力本身：汗水、急促的喘息、肌肉的紧绷与控制，头发和宽松衣物随惯
性甩动，赤脚在地面擦出声响。带重量的真实运动——而不是失重僵硬的 mocap
木偶。

**场景：** {{space}}，{{grade}}。光与地面也是编舞的一部分——影子随身体
而动。

### 3 · 氛围与画质
Shot on ARRI Alexa with anamorphic primes，浓烈的 {{grade}}。胶片颗粒、
真实实景光，快速摆动的四肢允许运动模糊。一种坚定的影调。取景要让**全身**
都看得清——舞蹈活在整个身形里，而不在紧裁切里。

### 4 · 运镜规则
**一镜流畅到底**，跟着身体走——环绕、跟移、或一记缓慢推进，始终让
{{dancer}} 完整留在画面内。和 MV 的快切相反：让动作演完。
- *呼吸感：* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence."——镜头是活的，随舞者
  移动，但绝不裁掉动作。
- *声音（这里要音乐，和 MV 一样）：* 这个题材靠一条音轨。指定
  {{style_tempo}}，让身体的运动锁死在拍子上。底下铺 Production audio——
  喘息、脚擦地、布料声。如果你有成品音轨，先用临时音生成，后期再把真歌
  铺进去。

### 5 · 分镜（一镜到底，约 12s）

```
0–3s · Entry（建立身体 + 空间）
Action: {{dancer}} 起势，先静后动，{{grade}} 的光在 {{space}} 里勾出身形。
Camera: 缓慢推进/环绕，全身入画。
Beat:   动作在重拍上启动。

3–9s · The phrase（{{move}} —— 身体的陈述）
Action: {{move}} 连续展开——惯性、重量、控制，汗水与喘息，影子随身体
        扫过。
Camera: 一记流畅跟随——环绕/跟移——绝不切走，绝不在关键时刻把四肢裁
        出画面。
Beat:   动作的重音落在节奏上。

9–12s · Resolve（克制收尾）
Action: 舞句收束；{{dancer}} 落定，胸口起伏。
Camera: 停住，呼吸浮动，全身入画。
Close:  不对镜定格 pose，无 logo，无炫技旋转。只有舞者在动作结束之处的
        光里喘着气。
```

### 负面提示词（Seedance / Kling——粘进独立负面框）
```
blurry, low resolution, watermark, text overlay, subtitles, logo, stiff mocap motion, weightless floaty movement, robotic interpolation, choppy cuts mid-move, cropped-out limbs, plastic CG skin, glossy idol render, video-game look, 3D cartoon, flat even studio lighting, distorted face, extra fingers, bent/broken joints, melting/morphing limbs, frame flicker, ghosting, lifeless locked-off camera
```

---

## 为什么这么搭

- **连续的身体，而非剪辑（舞蹈/MV 的分水岭）。** MV 跟着拍子切碎；舞蹈
  影片停在身体上，让动作读得出来。把它做成一镜流畅到底、全身始终在画面
  里——切走或在关键时刻裁掉四肢，就毁了。
- **重量与发力（Rule 5）。** 汗水、喘息、肌肉控制、擦地的脚、随惯性甩动
  的衣物。失重僵硬的运动一看就是 mocap；正是这份物理重量让舞蹈变真。
- **音乐就是节奏（Rule 4，和 MV 一样）。** 舞蹈建立在一条音轨上——指定
  tempo 让身体卡拍。真歌后期铺进去。
- **克制收尾（Rule 6）。** 舞者在动作结束之处喘着气，而不是对镜定格
  pose。那份精疲力竭，比一个眨眼更真。

**用法**：先跑*舞句*那一拍（3–9s）——如果身体动得有真实重量、并完整留在
画面里（不裁四肢、不僵硬如 mocap），首尾两段自然把它框住。保持一个连续
动作。

**模型**：Kling 拍全身人体运动极强；Veo 3 和 Sora 2 在写实 + 原生音乐处
理上很出色。快速动作时留意弯折/断裂的关节和四肢变形——把它们负面掉，并
让身体完整入画。
