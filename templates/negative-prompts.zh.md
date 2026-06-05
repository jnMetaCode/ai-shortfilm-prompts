# 负面提示词（反穿帮骨架）

> **[English →](./negative-prompts.md)**
>
> 作者 jnMetaCode（MIT 协议）。这是[风格画质骨架](./atmosphere-prefabs.zh.md)
> 的反面搭档：那边描述你**想要**什么，这里收集你想**排除**什么 ——
> AI 视频反复翻车的那些点（手指融化、塑料皮肤、画面闪烁、"游戏 CG 感"），
> 以及不同模型该怎么压制它们。
>
> **用法**：如果你的模型有负面字段，直接把下面的标准段塞进去；
> 没有字段的话先看兼容表 —— 有几个工具需要改成"只写正向"的写法，
> 还有两个一旦你写"no ___"反而会把那个东西召唤出来。

---

## 标准负面骨架

复制粘贴，当默认值用。它针对分辨率/锐度缺陷、叠加垃圾、解剖崩坏、
过度风格化的 CG/动漫感，以及死板的运镜 —— 这些就是一眼看上去
"很 AI"的穿帮点。

```
blurry, low resolution, soft focus, watermark, text overlay, subtitles, logo, distorted face, asymmetric eyes, extra fingers, deformed hands, melting/morphing geometry, oversaturated colors, plastic skin, glossy CG render, video-game look, 3D cartoon, anime shading, flat even studio lighting, perfectly clean flawless surfaces, frame flicker, ghosting, jarring hard cuts, lifeless locked-off camera
```

它**故意**写成一串逗号分隔的"不想要的名词/短语"—— 这正是各家专用
负面字段（Veo、Kling、Wan、Hailuo）期望的格式。粘进专用字段时
**不要**在每项前加 "no" 或 "don't"。没有字段的工具，见下方的
"句内否定"说明。

---

## 哪些模型有负面字段 —— 以及怎么喂

各家机制的差异比想象中大。有的工具有专门的输入框，有的要把负面
折进正向提示词当"护栏短语"，还有**两个（Runway Gen-4，以及一定程度上
Seedance 的消费端 App）根本不可靠地支持否定**—— Runway 上写 "no X"
甚至会把 X 召唤出来。

| 模型 | 有专用负面字段？ | 怎么否定 | 单镜头上限 | IP 过滤 | 语言 |
|---|---|---|---|---|---|
| **Seedance 2.0**（豆包 / 即梦-小云雀，字节） | 部分 —— 消费端 App 里没有可靠字段 | 描述你**想要**的；把规避措辞折进提示词 | ~10–15s（豆包 App 锁死 5s/10s 按钮；即梦网页与火山引擎控制台开放 4–15s） | 严（字节国内端比多数西方工具更狠） | 都行（中文最稳） |
| **Veo 3 / 3.1**（Google） | **有** | 字段里写名词/短语列表 —— **别写 "no/don't" 命令** | 8s（4/6/8s）；Extend 叠 7s 段最长 ~148s，4–5 次后画质明显下降 | 严 | EN |
| **Kling 2.x / 3.0**（快手） | **有** | 最适合稳定性穿帮（滑步、多指、变形），不适合泛泛的"画质"词 | 2.5：5–10s（Pro ~12s）；3.0：单提示 ~15s | 严（违禁词过滤命中一个就**整条**提示词被拒） | 都行 |
| **Hailuo / MiniMax**（Hailuo 02 / 2.3） | **有** | 少用 —— 针对具体穿帮做边界限定，别当主控杠杆 | ~6–10s（1080p ~6s；768p ~10s） | 中等 | 都行 |
| **Wan 2.x**（阿里，开源） | **有**（健壮） | 文档默认值：morphing、warping、face deformation、flickering、jittering、inconsistent lighting | 2.2：~3–8s；2.5/2.6：~10–15s | 自部署时宽松 | 中文为母语（纯英文可能拉胯） |
| **Runway Gen-4 / 4.5** | **没有** | 只写正向 —— 只描述**应该**出现的；"no X" 可能产出相反结果 | 5s 或 10s | 严 | EN |
| **Pika（2.2 / 2.5）** | 部分 —— 2.5 有，2.2 不确定 | 2.5 接受 "no morphing, no extra limbs…"；2.2 请先在 App 里验证 | 5s/10s；Pikaframes 关键帧最长 ~25s | 中等 | EN |
| **Sora 2 / 2 Pro**（OpenAI） | **没有**专用框 | 句内用护栏短语否定（"original characters only, no logos or text"） | Pro 最长 ~25s（标准档更短） | 严（三层审核；连"形似"都拦，不止名字） | EN |

**三条最容易翻车的规则：**

1. **Runway Gen-4 只吃正向。** 把 `no distorted hands` 搬进 Runway 提示词
   是跨工具最常见的错 —— 它可能**召唤**畸形手。请把整个意图改成正向写法
   （"clean five-fingered hands, anatomically correct"）。
2. **专用字段吃描述，不吃命令。** Veo/Kling/Wan 里写
   `extra limbs, glitch morphs, text overlays` —— 别写 `no extra limbs`。
   那个 "no" 浪费 token，还可能把解析器搞糊涂。
3. **Seedance 消费端豆包 App 没有暴露负面字段，且锁死 5s/10s 按钮。**
   别在那承诺 15s 或负面框；完整的 4–15s 区间和更细的控制在
   即梦网页 / 火山引擎那边。

> 置信度：时长与负面提示机制对 Veo 3.1、Runway Gen-4、Kling、Wan、Sora
> 为中高（2026 年厂商/帮助文档一致）；对 Seedance 2.0 与 Hailuo 为中
> （多来自第三方教程）。Veo 的 ~148s 与 Sora/Pika 的 ~25s 来自
> 扩展/关键帧功能，**不是**普通单镜头生成。IP 过滤"严/中/宽"是定性判断，
> 非厂商正式分级。

---

## 分场景定制版

按你要拍的题材，把对应一行追加到标准骨架后面。它们针对各场景特有的
翻车点，而不是泛泛的画质。

### 变身镜头

```
premature full transformation, symmetrical clean armor, instant costume swap, no in-between morph stages, untextured smooth plating, transformation happening off a single cut
```

为什么：变身镜头的失败在于**跳过中间**—— 模型直接蹦到成品战衣，或者
渲染得跟出厂一样干净。你要的是分阶段、不对称、带战损的生长过程。
搭配**暗黑特摄**风格骨架。

### 打斗 / 打击感

```
weightless floaty motion, no impact, soft contact, characters phasing through each other, missing follow-through, slow-motion drift on every hit, no debris or dust on impact
```

为什么：AI 打斗看起来**没重量**—— 拳头没落点、身体不被击退。
把飘忽感否掉，要求冲击与重量。搭配**好莱坞青橙**或**重型机甲**骨架。

### 对话 / 特写口型

```
lip-sync drift, mouth out of sync with audio, frozen dead eyes, mannequin stillness, uncanny face warp on speech, teeth merging, plastic lip texture
```

为什么：近景对话会暴露口型漂移和"死鱼眼"的恐怖谷感。搭配
**商业人像**参考流程，先把脸锁死再上动作。

### 环境 / 大远景

```
warping background geometry, flickering distant detail, melting architecture, repeating tiled textures, impossible perspective, crowd faces smearing, signage gibberish text
```

为什么：远景崩在**背景**—— 糊成一团的人群、乱码招牌、逐帧"沸腾"的建筑。
把几何稳住。

---

## 另见

- [`../skills/shortfilm-prompt/SKILL.md`](../skills/shortfilm-prompt/SKILL.md)
  —— 组装完整提示词的 Skill；当目标模型有负面字段时它会取用这个骨架。
- [`../methodology.zh.md`](../methodology.zh.md) —— 这些负面词嵌入的
  5 段式结构（反穿帮清单属于画质/氛围那一段）。
- [`./atmosphere-prefabs.zh.md`](./atmosphere-prefabs.zh.md) —— 正面搭档：
  你**想要**镜头长成什么样。
