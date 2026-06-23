# 实战范例 — 定格动画 / 黏土动画（风格驱动）

> jnMetaCode 原创实战范例（MIT）。把 5 段式结构用在**手作定格动画 /
> 黏土动画**上——一种「瑕疵本身就是美学」的风格。它教的是本库里最重要
> 的一课：**知道什么时候该打破规则。** 这里我们故意丢掉呼吸浮动
> （Rule 3）——定格动画是逐帧步进、固定机位的，手持晃动会毁掉这种质感。
>
> 概念：一只黏土小生物踮着脚走过一个手作布景。换掉角色和布景，保留
> 12fps 步进的纪律即可。
>
> *延伸阅读（取其灵感，并未照搬——全部用我们的结构重写）：黏土／定格
> 动画范式见
> [songguoxs/awesome-video-prompts](https://github.com/songguoxs/awesome-video-prompts)
> 和 [zhangchenchen/awesome_sora2_prompt](https://github.com/zhangchenchen/awesome_sora2_prompt)
> （MIT）。*
>
> **[English →](./claymation.md)**

---

## 先要定义的变量

| 变量 | 本例取值 | 可替换为… |
|---|---|---|
| `{{character}}` | 一只圆肚子的黏土小生物 | 一只毛毡狐狸 / 一个铁丝加黏土的机器人 |
| `{{set}}` | 一片微缩的长苔藓的林地 | 一个小厨房 / 一座纸板城市 |
| `{{action}}` | 踮脚走过，然后受惊僵住 | 烤一个歪歪的蛋糕 / 追一只虫子 |
| `{{material}}` | 哑光橡皮泥，能看见指纹 | 羊毛毡 / 铁丝外裹上色黏土 |
| `{{lighting}}` | 暖色实用台灯，柔和阴影 | 冷调窗光 / 小串灯 |

---

## 完整提示词（可直接复制）

### 1 · 核心主题
`手作黏土动画 | 12fps 步进定格 | 触感指纹质地 | 暖色实用照明 | 迷人的瑕疵感，无丝滑 CG 3D，无运动模糊`

### 2 · 人物与场景

**角色：** {{character}}，由 {{material}} 捏成。瑕疵就是风格，不是要藏
起来的缺点：{{material}} 上看得见的拇指印和工具痕、零件拼接处淡淡的接
缝、表面细小的疙瘩、帧与帧之间轻微的抖动与「boil」。表情简单、有表现
力、手作感十足。

**布景：** {{set}}——一个真实的微缩模型，纯手工搭建：看得出手工痕迹、
一点点胶水反光、稍微不平整的布景、表面的灰尘。一个桌面立体布景，而不
是渲染图。

### 3 · 氛围与画质
拍得像一个真实的定格动画片场：偏微距镜头俯拍桌面立体布景，浅景深，
{{lighting}}（实用灯具，柔和的光线衰减）。**12fps 步进动画**——动作以
细小、离散的步子推进，帧与帧之间带着淡淡的「boil」，和手工逐帧摆拍一
模一样。暖调、略带瑕疵的曝光。

### 4 · 运镜规则
**只用固定机位或步进式运镜——故意不要呼吸浮动。** 这就是那处打破规则
之处：定格动画的摄影机架在云台/导轨上，不是手持。用静止固定机位，或者
缓慢的逐帧步进式推轨/摇镜（运镜本身也是一帧一帧步进）。这里若用丝滑的
呼吸式手持浮动，会被读成 CG，毁掉手作的错觉。
- *声音：* No score（实在要配，可用一段简单的玩具感小旋律）。现场／拟
  音音效——布料/黏土轻轻摩挲声、细小脚步声、一点吱呀声、安静工坊里闷闷
  的室内底噪。

### 5 · 分镜（3 拍，约 8–10 秒）

```
0–3s · 登场（步进）
动作：{{character}} {{action}}——动作以细小的 12fps 步子推进，表面
      淡淡 boil。
镜头：固定机位俯拍 {{set}} 全景，{{lighting}} 从一侧打来。
质地：拇指印和接缝在灯光下显形。

3–6s · 节拍（那个小瞬间）
动作：一个停顿，一个简单而有表现力的反应——一次眨眼（眼皮分 2 步
      先合后睁）、一次歪头。
镜头：缓慢步进式推近（不要丝滑运镜）。
声音：细小拟音——一声摩挲、一声吱呀。

6–10s · 收住（克制）
动作：{{character}} 安定下来 / 完成那个小动作。
镜头：定住，固定机位。
收尾：没有盛大终幕，没有闪光，没有丝滑的横扫。就是小生物静止下来，
      布景安静下来，最后一记淡淡的帧 boil。
```

### 负面提示词（Seedance / Kling——粘进独立负面框）
```
blurry, low resolution, watermark, text overlay, subtitles, logo, smooth CG 3D render, Pixar-style smooth animation, motion blur, fluid 60fps motion, photorealistic skin, glossy plastic perfection, perfectly clean flawless surfaces, handheld camera shake, breathing camera float, melting/morphing geometry, oversaturated colors, video-game look, frame flicker, ghosting, jarring hard cuts
```

---

## 为什么这么搭

- **故意打破呼吸感规则（Rule 3 例外）。** 定格动画依赖固定云台和步进帧。
  那个支撑本库每一个其它模板的呼吸浮动，在这里会背叛手作质感——所以我
  们把它丢掉，并在负面里明确否定「handheld camera shake / breathing
  camera float」。*规则服务于题材，而不是反过来。*
- **瑕疵就是美学（Rule 5，更进一步）。** 拇指印、接缝、表面疙瘩、帧与
  帧之间的「boil」。在别的题材里瑕疵是用来增加真实感的；在这里它们就是
  媒介本身。丝滑 = 错。
- **「12fps 步进」是那个承重锚点（对应 Rule 2）。** 正如「ARRI +
  Panavision」把实拍锚定住，「12fps stepped stop-motion, frame boil」把
  模型锚定到真正的黏土动画上，而不是丝滑 CG。
- **克制收尾（Rule 6）。** 不要闪光终幕，不要横扫。小生物静止下来，让手
  作的趣味完整保留。

**用法**：先生成 *0–3s 登场* 这一拍，确认 12fps 步进运动和黏土质地都对
了——如果跑出来是丝滑/CG 感，就加强「12fps stepped, frame boil, no
motion blur」再重跑。运镜一律保持固定机位。

**模型**：Kling 和 Seedance 2.0 处理风格化步进运动很好；Veo 3 也能做，
但要当心它默认走丝滑插帧——这时狠压负面框（「smooth CG, motion blur,
60fps」）。Pika 在风格化短片动画上同样很强。
