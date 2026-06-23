# 实战范例 — 会说话的动物 VLog（自拍 POV）

> jnMetaCode 原创实战范例（MIT）。把 5 段式结构用在**会说话的动物
> VLog**——这种第一人称形态随原生音频引擎爆火（一只宠物对着手持自拍
> 镜头讲述自己的一天）。它和情感萌宠线
> （[pet-lifetime-narrative.zh.md](./pet-lifetime-narrative.zh.md)）天然成对，
> 但走的是俏皮搞笑路线，而不是催泪。
>
> 概念：一只腿短的柯基为自己的早晨做 VLog，对着镜头讲个不停。
> 换掉动物和段子，保留结构即可。
>
> *延伸阅读（仅作灵感，并非照搬——全部用我们的结构重写过）：会说话
> 的动物 / VLog 套路调研自
> [jax-explorer/awesome-veo3-videos](https://github.com/jax-explorer/awesome-veo3-videos)
> （无 license，仅供创作灵感），分类结构参考自
> [zhangchenchen/awesome_sora2_prompt](https://github.com/zhangchenchen/awesome_sora2_prompt)
> （MIT）。*
>
> **[English →](./animal-vlog.md)**

---

## 开拍前要先定义的变量

| 变量 | 本范例取值 | 可替换为… |
|---|---|---|
| `{{animal}}` | 一只橙白相间、腿短的柯基 | 一只臭脸虎斑猫 / 一只金毛幼犬 |
| `{{voice}}` | 温暖、略带憨气、语速快 | 干巴巴一本正经 / 尖细又兴奋 |
| `{{setting}}` | 洒满阳光的厨房，随后是后院 | 一间公寓 / 一辆车里 / 一条登山小径 |
| `{{bit}}` | 像美食评论家一样点评早餐 | 讲述「忙得不可开交」的慵懒一天 |
| `{{punchline}}` | 说到一半被掉落的零食岔了神 | 一头栽倒，「直播结束」 |

---

## 完整提示词（可直接复制）

### 1 · 核心主题
`第一人称动物 VLog | 手持自拍 POV | 自然日光 | 同步说话+环境音 | 迷人的写实感，无诡异 CG 毛发`

### 2 · 人物与场景

**主体（动物）：** {{animal}}，直接对着镜头说话（嘴唇和下巴随语音
自然同步张合——自然，不像僵硬木偶）。保留这些瑕疵，让它真实、且在每
次切镜后还是*同一只*动物：嘴角一点口水、左耳毛微微打结、鼻头上一粒
碎屑、一只眼睛略微发懒。表情丰富、面部灵活。声音：{{voice}}。

**场景：** {{setting}}。真实有生活痕迹的空间——水槽里有碗、地上有
咬坏的玩具——不是干净的摄影棚。日光从窗户照进来。

### 3 · 氛围与画质
按**手机风格**拍摄——超广角自拍取景、手臂伸直举着、画面边缘有轻微
镜头畸变，动物的脸又近又略带鱼眼，自动对焦微微来回拉风箱。这是刻意
的题材打破：VLog 要的是*手机相机*的看法，**而不是**电影镜头。自然
日光、真实色彩、极少颗粒，以及真实手持手机视频那种随性、不完美的
曝光。

### 4 · 运镜规则
自拍 POV——动物（或一个看不见的主人）把镜头举在手臂长度处；画面像真
实手持 VLog 那样上下晃动、再重新居中。一两个快速的切出，去拍它正在
「讲」的东西（B-roll 空镜）。
- *呼吸感：* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence." ——这里可以比平时活泼
  一点；真实自拍视频本就会飘、会重新构图。
- *声音：* No score. 只用制作 / 同步音频——动物的声音（{{voice}}）锁定
  在它的嘴部动作上，项圈叮当、爪子刮地、{{setting}} 的环境音、偶尔画
  外人类的一声「嗯哼」。台词必须和嘴型同步。

### 5 · 分镜（3 拍，约 10s）

```
0–3s · 开场 / 打招呼
动作：{{animal}} 占满自拍画面，直视镜头，张口就开始 {{bit}}——语速快、
      表情丰富。
镜头：手臂长度自拍，轻微晃动，脸又近、边缘畸变。
声音：第一帧起声音就同步，背后是 {{setting}} 的环境音。

3–7s · 段子 / B-roll
动作：切出去拍它正在讲的东西（那只食盆 / 那份「繁忙」日程），再切回
      正在反应的说话的脸。
镜头：快速手持切出空镜，随后重新居中回到脸上。
声音：声音在切出画面上继续，项圈叮当、爪子刮地。

7–10s · 包袱 / 收尾
动作：{{punchline}}——段子崩了；动物丢了思路。
镜头：相机随「主播」放弃这一条而倾斜 / 下垂。
收尾：没有挥爪大告别，没有屏幕上的爱心，没有订阅图标。就是动物一头
      趴下、画面倾向天花板，声音说到一半渐渐消失。
```

### 负面提示词（Seedance / Kling——粘进独立负面框）
```
blurry, low resolution, watermark, text overlay, subtitles, logo, distorted face, asymmetric eyes, extra limbs, deformed paws, the animal changing breed or color between shots, uncanny rubbery CG fur, dead glassy eyes, stiff puppet jaw, lip-sync mismatch, oversaturated colors, plastic skin, glossy CG render, video-game look, 3D cartoon render, polished cinematic lighting, frame flicker, ghosting, jarring hard cuts, on-screen emojis, subscribe button overlay
```

---

## 为什么这么搭

- **手机相机的看法，而非电影感（刻意打破 Rule 2）。** VLog 的全部魅力
  就在于它看起来像手机拍的。所以这里不写「ARRI + Panavision」，而是把
  相机锚点定在「超广角自拍取景、边缘轻微畸变、自动对焦拉风箱」。在这
  里用电影镜头的锚点，会让画面看起来像精修广告，毁掉真实感。相机锚点
  要匹配*题材*，不要凭条件反射乱套。
- **瑕疵锚点同时兼任一致性锁（Rule 5）。** 口水、打结的耳朵、鼻头碎屑
  ——这些让它在切出空镜再切回来后仍是*同一只*动物，就像情感萌宠片始终
  是同一只狗。
- **嘴型同步要写明。** 会说话的动物视频最常死在僵硬的木偶下巴或对不上
  的口型——在主体描述块里点明「嘴唇和下巴自然同步、不像木偶」，并把这
  些翻车点写进负面。
- **克制收尾（Rule 6）。** 不挥爪、不爱心、不订阅图标。主播只是丢了思
  路一头趴下，反而更好笑，也能拦住模型自己加社交媒体 UI 浮层。

**用法**：先跑*打招呼*那一拍（0–3s），把会说话的脸和声音定住；如果那
里口型和品种都对了，切出空镜和包袱就能接得住。段子要短——一个梗、一
次崩。

**模型**：Veo 3 和 Sora 2 对同步口语对白最强——说话镜头用它俩之一。
Kling 3.0 支持多语种对白。Seedance 2.0 有原生同步音频，但说话拍记得
校验口型；某条同步飘了就切去 B-roll 空镜。
