# 实战范例 — 竖屏短剧

> jnMetaCode 原创实战范例（MIT）。把 5 段式结构用在**竖屏短剧**上——
> 专为手机打造的短篇戏剧场景格式（抖音/Reels 短剧）。教你竖屏优先的
> 构图、shot-reverse-shot（正反打）对话语法，以及驱动「一集接一集刷
> 下去」的「冷开钩子 + 悬念结尾」结构。
>
> 概念：一场两人之间剑拔弩张的对峙，冷开钩子开场，悬念剪断收尾。换掉
> 冲突，留住结构。无 IP。
>
> *Further reading（取其灵感，非照搬——全部用我们的结构重写）：
> viral/短视频套路见
> [zhangchenchen/awesome_sora2_prompt](https://github.com/zhangchenchen/awesome_sora2_prompt)
> （MIT）。*
>
> **[English →](./micro-drama.md)**

---

## 先定好这些变量

| 变量 | 本例取值 | 可替换为… |
|---|---|---|
| `{{a}}` | 一个疲惫的年轻女子，职业装 | 主角——描述外形，别用 IP |
| `{{b}}` | 一个上了年纪的男人，名贵西装 | 反派／反转角色 |
| `{{hook}}` | 她把一封辞职信拍在桌上 | 开场前 2 秒最炸的那一下 |
| `{{conflict}}` | 「你早就知道。从头到尾。」 | 把冲突推上去的那句台词 |
| `{{cliff}}` | 他把一张照片推到她面前——她僵住 | 收尾那个没解答的反转 |

---

## 完整提示词（可直接复制）

### 1 · 核心主题
`竖屏短剧 | 对话对峙 | 钩子前置的冷开场 | shot-reverse-shot（正反打）| 写实克制表演，不要狗血浮夸`

### 2 · 人物与场景

**人物：** {{a}} 和 {{b}}。参考上传照片，五官 100% 保留，不做美颜。
真实、克制的情绪——绷紧的下颌、眼里一闪、一口憋住的气——而非戏剧化的
浮夸表演。带瑕疵：疲惫的眼、一缕乱发、真实皮肤、微皱的衣领。正是这份
写实让戏剧落地。

**场景：** 夜里一间住惯了的办公室（或你的设定）——实景台灯、文件、一
扇透着城市寒意的窗。竖屏 9:16 构图，围绕脸来搭。

### 3 · 氛围与画质
ARRI Alexa + vintage primes 拍摄，克制的电影感调色，浅景深把脸从背景
里剥离出来。**为竖屏（9:16）构图：** 脸放在画面上中部，尊重眼神线以
便走 shot-reverse-shot。胶片颗粒、有动机的实景光、真实阴影。

### 4 · 运镜规则
**shot-reverse-shot（正反打）对话语法：** 一个干净的 {{a}} 单人镜，
一个反打的 {{b}} 单人镜，张力升高时再收得更紧。竖屏构图让每张脸都很大。
- *呼吸感：* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence." ——极轻微，让场面活着、
  贴脸、当下感强。
- *声音：* No score，或在反转底下铺一条单一的低频紧张嗡鸣——不是那种渐
  强的狗血煽情弦乐。Production audio：对白、室内底噪、台灯的电流声、椅
  子挪动声。让静默把节拍切得更利。

### 5 · 分镜（3 拍，约 12s——为钩子 + 悬念而搭）

```
0–2s · 冷开场（钩子——熬过那一划）
动作：直接进，不铺垫：{{hook}}。最炸的那一下落在头两秒里，趁还没人
      划走。
镜头：对 {{a}} 猛地推进的单人镜，竖屏，脸放大。
声音：钩子那一下尖锐的现场音；然后死寂。

2–8s · 对峙（shot-reverse-shot）
动作：{{a}}：「{{conflict}}」——切到 {{b}} 的反应，再切回来。张力一句
      一句往上顶，脸越绷越紧。
镜头：干净单人镜／反打单人镜，随着升温对每张脸缓慢推近。
声音：对白和室内底噪；也许有一条低频嗡鸣进来。

8–12s · 悬念（没解答的反转）
动作：{{cliff}}——一个掀翻整场戏的揭示或反转，悬着不解。
镜头：定在僵住的反应上，微微推近。
收尾：不解答、不给配乐重音、不需要「未完待续」字卡——切在那张僵住的、
      表情正到一半的脸上。正是这个没解答的问题，让人去点下一集。
```

### 负面提示词（Seedance / Kling——粘进独立负面框）
```
blurry, low resolution, watermark, text overlay, subtitles, logo, theatrical overacting, exaggerated soap-opera expressions, plastic CG skin, glossy idol render, video-game look, 3D cartoon, flat even studio lighting, horizontal letterboxing, faces too small in frame, distorted face, asymmetric eyes, extra fingers, lip-sync mismatch, melting/morphing geometry, swelling melodramatic score, frame flicker, jarring hard cuts, lifeless locked-off camera
```

---

## 为什么这么搭

- **钩子放在头 2 秒（竖屏第一铁律）。** 手机观众瞬间就做决定。直接
  开*在*最炸的那一下（{{hook}}）——不铺垫、不慢热——否则就被划走。冷
  开场就是全部胜负手。
- **竖屏改变了镜头语法。** 脸要大、放在画面上中部，尊重眼神线，正反
  打才能在 9:16 里读得通。横向黑边、或脸太小，都会害死一部短剧；把它
  们写进负面。
- **shot-reverse-shot（正反打）是对话引擎。** 单人镜／反打单人镜／逐
  渐收紧的推近，对峙就是靠这个读出来的。保持干净，让脸来扛。
- **克制 + 悬念（Rule 6，戏剧变体）。** 写实表演（绷紧的下颌，而非做
  作）才让戏落地；收在一张僵住的、没解答的反应上——而非一个解决或一记
  配乐重音——才是驱动追剧的东西。

**用法**：先把*冷开场*（0–2s）跑出来——如果钩子立住了、表演又是克制的
（不狗血），再围着它搭对峙和悬念。脸要大；全程按 9:16 拍／想。跑之前
先洗掉任何能认出 IP 的措辞。

**模型**：Veo 3 和 Sora 2 在对口型对白和写实脸上最强；Kling 3.0 支持
多语种对白。台词写短一点好让口型对得住；某一条 take 口型飘了，就在反
打上切走。
