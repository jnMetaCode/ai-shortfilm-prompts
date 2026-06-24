# 实战范例 — 汽车广告

> jnMetaCode 原创实战范例（MIT）。把 5 段式结构用在**汽车广告**——
> 这里的功夫全在反光车身、移动的光带扫过，以及汽车广告专用的运镜器
> 材。区别于 [product-commercial.zh.md](./product-commercial.md)
> （台面微距）：这里的主角是一辆运动中的车。
>
> 概念：一辆轿跑在黄昏的海岸公路上飞驰，光带掠过车身。换掉车和路，
> 把「车身/光线」的纪律保留下来。
>
> *延伸阅读（只取灵感、未照搬——全部用我们的结构重写）：商业/产品类
> 模式见
> [LichAmnesia/awesome-ad-video-prompts](https://github.com/LichAmnesia/awesome-ad-video-prompts)
> （CC BY 4.0）。*
>
> **[English →](./car-commercial.md)**

---

## 先定义这些变量

| 变量 | 本例 | 可替换为… |
|---|---|---|
| `{{car}}` | 一辆低趴的哑光灰轿跑 | SUV / 经典敞篷跑车 / 电动车 |
| `{{road}}` | 黄昏的悬崖海岸公路 | 湿漉漉的城市街道 / 盐碱滩 / 隧道 |
| `{{surface}}` | 带柔和光泽的哑光漆面 | 亮黑 / 拉丝金属 / 珠光白 |
| `{{light_sweep}}` | 一道暖阳光带掠过车身 | 霓虹反射 / 影棚弧形光 |
| `{{grade}}` | 暖黄昏金 + 冷调阴影 | 高对比夜景 / 去饱和钢灰 |

---

## 完整提示词（可直接复制）

### 1 · 核心主题
`汽车广告 | 运动中的反光车身 | 速度与造型之美 | 移动光带揭示车形 | 写实，不要塑料感 CG 车，不要悬浮在虚空里的渲染图`

### 2 · 人物与场景

**主角（这辆车）：** {{car}}，{{surface}}。车身就是主体——它的造型靠
光线如何在表面上游走来揭示。要那种看着「真实」、而非 CG 的瑕疵：下护
板上淡淡的路尘与灰、一颗水珠、引擎盖上的热浪、真实的轮胎胎侧形变与
胎纹、{{road}} 在漆面上滑过的真实倒影。

**场景：** {{road}}，{{grade}}。一个真实环境倒映在车身表面——绝不是
天衣无缝的白棚虚空。

### 3 · 氛围与画质
Shot on ARRI Alexa with anamorphic primes，from a camera car /
Russian-arm rig（真正的汽车广告器材）。{{grade}}，film grain，真实的
镜面高光与倒影——那种「湿润」/金属质感来自真实环境的反射，而非 CG
辉光。

### 4 · 运镜规则
贴地跟拍镜头擦着车身滑过，用一个摇臂运动让 {{light_sweep}} 沿着车形
游走，再来一段与行驶中的车并行的跟拍。
- *呼吸感：* keep it minimal——汽车广告器材都是稳定的；要 a smooth
  glide，not a handheld float。
- *声音：* No score。Production audio only——引擎声、轮胎在 {{road}}
  上的声音、风声、涡轮或电机的呼啸。（若品牌需要音乐垫底，在剪辑里
  有意识地加进去——别让模型自己编一段。）

### 5 · 分镜（3 拍，约 10s）

```
0–3s · 车身（在倒影中揭示）
Action：近乎微距地拍 {{surface}}，{{light_sweep}} 掠过它——车形靠移
        动的光与倒影读出来，而不是一面平光摆拍。
Camera：缓慢摇臂沿车身滑行。

3–7s · 运动（车在路上活起来）
Action：{{car}} 切过 {{road}}，轮胎抓地，环境在漆面上拉成光带，引擎
        盖上热浪升腾。
Camera：贴地并行跟拍，世界倒映其上、飞速掠过。
Sound：引擎 + 轮胎 + 风，同步。

7–10s · 主角定格（克制收尾）
Action：车缓缓停稳；{{light_sweep}} 的最后一缕滑离车身。
Camera：定住，缓慢滑行至停。
Close：No logo slam，no spinning turntable，no lens-flare burst。
       只是静止的车，和离开表面的光。
```

### 负面提示词（即梦/可灵——粘进独立负面框）
```
blurry, low resolution, watermark, text overlay, subtitles, logo, oversaturated colors, plastic CG car, glossy unreal render, video-game look, 3D cartoon, floating car in white void, seamless studio infinity backdrop, blown-out highlights, flat even lighting, perfectly clean showroom surfaces, warped reflections, melting/morphing bodywork, wrong wheel rotation, frame flicker, ghosting, spinning turntable, cheesy lens flare
```

---

## 为什么这么搭

- **光揭示车形（汽车广告的核心动作）。** 汽车广告不是一面平光的产品
  摆拍——车身靠一道光带扫过反光表面来揭示。整个分镜要围绕移动的光与
  倒影来搭，而不是一个静止的美姿。
- **真实倒影 = 真实感（Rule 5）。** 路尘、一颗水珠、热浪、环境在漆面
  上拉成光带。一辆一尘不染、悬浮在白棚虚空里的车就是 CG 的默认长相；
  靠倒影和路尘才把它卖成真的。
- **汽车广告器材，而非「电影感」（Rule 2）。**「ARRI + anamorphic，
  camera car / Russian-arm rig，贴地跟拍」把模型锚定到真实的汽车摄影。
  「Car driving, cinematic 4K」只会给你一张游戏渲染图。
- **克制收尾（Rule 6）。** 车停稳、光离开车身——而不是 logo 砸场或转
  盘旋转。高级感是安静的。

**用法**：先生成*运动*那一拍（3–7s）——如果那里的倒影、轮胎抓地和环
境光带读着真实，车身拍和主角拍就能把它框起来。盯紧扭曲的倒影和反转
的车轮；用负面压掉它们。

**模型**：Veo 3 和 Sora 2 在反光表面和运动真实感上最好；可灵在并行跟
拍上很强。注意高速时车轮反向旋转——把跟拍段做短，或加上车轮方向的负
面词。
