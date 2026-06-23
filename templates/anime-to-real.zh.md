# 实战范例 — 动漫 / 2D → 真人实拍

> jnMetaCode 原创实战范例（MIT）。把 5 段式结构用在**「动漫角色变真人」**
> 这一题材上——这是搜索量极大、却往往从两个相反方向翻车的类型：要么
> 廉价 cosplay，要么塑料感 CG。诀窍在于**翻译媒介**（赛璐珞渲染 → 真实
> 材质 + 物理）的同时，**保留让角色一眼可辨的剪影**。本模板最吃 Rule 7
> ——那一组可辨识的特征，正是 IP 过滤会拦的东西。
>
> 概念：一个风格化的「驭风剑客」概念，渲染成真实世界里的真人。只描述
> 特征，绝不写 IP 名字。
>
> *延伸阅读（取其灵感，非照搬——全部按我们的结构重写）：
> [zhangchenchen/awesome_sora2_prompt](https://github.com/zhangchenchen/awesome_sora2_prompt)
> 里的风格迁移 / 动漫类目（MIT）。*
>
> **[English →](./anime-to-real.md)**

---

## 先定义这些变量

| 变量 | 本例取值 | 你可替换为… |
|---|---|---|
| `{{silhouette}}` | 高挑、清瘦、长外套、单侧护肩 | 能让人认出这个角色的可辨形状 |
| `{{signature}}` | 一缕淡蓝挑染、一块缺角的玉坠 | 那 2–3 个「就是 ta」的标志特征——不写 IP 名 |
| `{{palette}}` | 靛蓝 + 旧钢色 + 浅蓝 | 角色的色彩身份 |
| `{{world}}` | 黄昏时分一座被雨打湿的石桥 | 翻译成真实地点的场景 |
| `{{prop}}` | 一把磨旧的真钢曲刃刀 | 那件标志性道具，做成实体 |

---

## 完整提示词（可直接复制）

### 1 · 核心主题
`anime character reimagined as live-action | 真实材质与物理 | 保留剪影 + 标志特征 | 电影级调色 | 不要廉价 cosplay 感、不要塑料 CG、不要赛璐珞渲染`

### 2 · 人物与场景

**人物（翻译媒介，保留剪影）：** 一个真人，带着能识别角色的可辨
{{silhouette}} 与 {{signature}}——但完全渲染成真实的：**真实皮肤，有
毛孔和细微纹理；真实头发（一根根发丝，不是一顶头盔）；真实编织布料，
有重量、有褶皱；{{prop}} 是真正磨旧的金属。** 去掉每一个 2D 线索——
没有赛璐珞渲染、没有扁平的动漫眼、没有违反重力的头发。眼睛和身体比例
都按真人来，不放大。

**瑕疵（这正是「真」与「cosplay」的分界）：** 皮肤的油光和几缕飞起的
碎发，布料起皱、略带磨旧，{{prop}} 上一道真实的刮痕，淡淡的汗。
cosplay 看起来崭新而摆拍；真人看起来有生活痕迹。

**场景：** {{world}}，把 {{palette}} 带进真实的光照里。

### 3 · 氛围与画质
Shot on ARRI Alexa with vintage primes，按 {{palette}} 做电影级调色。
所有东西都遵守真实世界物理——布料带着重量摆动、落定，头发随空气
而动，光裹着真实的皮肤。胶片颗粒。目标是「一部真人改编电影的定格」，
不是渲染图，也不是漫展照片。

### 4 · 运镜规则
缓慢、克制的揭示——推或弧线运镜，让真实材质看得清楚。
- *呼吸感：* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence."
- *声音：* No score. Production audio only——雨打石面、布料摩挲、
  {{prop}} 的刮擦声、环境氛围声。

### 5 · 分镜（3 拍，约 10s）

```
0–3s · 细节（用特写卖出真实感）
Action: 微距对准真实皮肤 / 一缕飞起的碎发 / 编织布料 / 刮花的
        {{prop}}——那些说「这是真的」的质感。
Camera: 缓慢推近细节，浅景深。

3–7s · 剪影（这下认出 ta 了）
Action: 拉开揭示 {{world}} 里完整的 {{silhouette}}——这个形状和
        {{signature}} 让角色可辨，但每一个表面都是真实的。
Camera: 缓慢弧线运镜，呼吸浮动，雨和空气拂动布料与头发。

7–10s · 一个停住的眼神（克制特写）
Action: 一个微小的、属于人的表情——一次呼吸、一个眼神，没有动漫姿势。
Close:  没有蓄力光效、没有 logo、没有炫技的英雄站姿。就是一个恰好
        是那个角色的真人，站在真实的雨里。
```

### 负面提示词（即梦 / 可灵——粘进独立负面框）
```
cel shading, anime shading, flat 2D look, cartoon, enlarged anime eyes, impossible hair gravity, plastic CG skin, doll-like face, cosplay wig look, cheap costume, brand-new unworn fabric, oversaturated colors, glossy render, video-game look, watermark, text overlay, logo, distorted face, extra fingers, melting/morphing geometry, frame flicker, jarring hard cuts, lifeless locked-off camera
```

---

## 为什么这么搭

- **翻译媒介，保留剪影。** 角色之所以认得出，靠的是*形状 + 2–3 个标志
  特征*，而不是赛璐珞渲染。把每个 2D 线索换成真实材质的对应物（赛璐
  珞 → 皮肤毛孔，扁平头发 → 一根根发丝，动漫眼 → 真人眼），再保留剪影
  ——这就是「2D → 真人」的全部手艺。
- **瑕疵是 cosplay / 真人的分界（Rule 5）。** 崭新、干净、摆拍 =
  cosplay。磨旧的布料、刮花的道具、飞起的碎发、真实的皮肤 = 真人电影。
  正是这些磨损卖出了真实。
- **最吃 Rule 7——描述特征，绝不写 IP 名字。** 一组可辨识的特征
  （名字、那身一模一样的标志性服装）正是 Sora 的相似度过滤和即梦的 IP
  过滤会拦的东西。把 {{silhouette}} + {{signature}} 当作*描述*来用，
  不要写角色的名字。
- **克制特写（Rule 6）。** 一次属于人的呼吸，而不是蓄力姿势。让它稳稳
  落在「电影改编」上，而不是同人动画。

**用法**：先跑细节那一拍（0–3s）——如果皮肤、头发、布料在那里看起来
是真正真实的，完整揭示就稳得住。如果跑出来塑料感或赛璐珞感，把负面框
往狠里加。在即梦 / Sora 上跑之前，**清掉任何能认出 IP 的措辞**。

**模型**：Veo 3 和 Sora 2 的真实皮肤 / 材质翻译最好；两者都有严格的相似
度过滤，所以保持用特征描述、不点名。可灵和即梦也能用——即梦尤其会直接
拒绝点名的 IP，所以只做描述。
