# 实战范例 — 美食 ASMR / 感官特写

> jnMetaCode 原创实战范例（MIT）。把 5 段式结构用在**美食 ASMR**——
> 这个题材里*原生同步音频*本身就是全部重点，而不是事后补的点缀。这是
> 最能压榨现代引擎原生音画同步能力的模板（Seedance 2.0、Veo 3、
> Sora 2）。
>
> 概念：切开一块刚煎好的牛排，极限微距，清脆的同步拟音。换掉这道菜，
> 你就得到一副可复用的美食 ASMR 骨架。
>
> *延伸阅读（仅作灵感参考，未照搬——全部按我们的结构重写）：
> [songguoxs/awesome-video-prompts](https://github.com/songguoxs/awesome-video-prompts)
> 里的 ASMR / 美食提示词范式，以及
> [geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts)
> 的音画同步章节（MIT）。*
>
> **[English →](./food-asmr.md)**

---

## 先要定义的变量

| 变量 | 本例取值 | 可替换为… |
|---|---|---|
| `{{dish}}` | 一块厚切、刚煎好的牛排 | 一颗熟透的奇异果 / 一只刷了糖浆的可颂 / 一碗拉面 |
| `{{tool}}` | 一把沉手的主厨刀 | 手指 / 勺子 / 筷子 |
| `{{key_sound}}` | 脆皮爆裂声 + 刀切声 | 果汁迸溅 / 酥皮碎裂 / 啜汤声 |
| `{{texture}}` | 焦脆外壳、粉嫩中心、流出的肉汁 | 毛茸果皮 → 湿润的青绿果肉 / 金黄分层 |
| `{{ambient}}` | 安静的厨房，微弱的滋滋声 | 鸟鸣 / 雨打窗 / 咖啡馆的低语 |

---

## 完整提示词（可直接复制）

### 1 · 核心主题
`美食 ASMR | 极限微距感官特写 | 自然窗光 | 清脆同步拟音 | 诱人写实，不要过饱和的「美食色情」`

### 2 · 人物与场景

**主角主体（食物）：** {{dish}}。质感要具体描述：{{texture}}。带上
那些读起来*真实、而非摆拍造型*的瑕疵：煎色不均、一边被撕开、案板上
已经渗出一小摊肉汁、一粒碎屑没归位、蒸汽不规则地升腾。不是光鲜的杂
志摆盘——是真的刚做出来的食物。

**场景：** 一块磨旧的木质砧板，背后是 {{ambient}}，一道低角度的侧向
窗光打在蒸汽上。浅景深，背景是柔和的暖色虚化。

### 3 · 氛围与画质
ARRI Alexa 摄影机 + 100mm macro 微距镜头（极限特写部分可用 Laowa
probe macro 探针微距）。侧向暖色自然窗光，湿润／多汁表面上有轻柔的高
光泽，色彩忠于实物——*不要*那种过饱和的橘色「美食色情」调色。有机
胶片颗粒，浅焦把背景化开。

### 4 · 运镜规则
以若干段短促的微距镜头剪辑（或一镜到底的探针运动）。缓慢推近到接触
点；一次缓慢的变焦移焦。
- *呼吸感：* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence."
- *声音（这才是主角——把每一个声音都列全）：* No score. 只用现场／
  同步音频——{{key_sound}}、{{tool}} 接触 {{dish}} 那一下精确的声响、
  切开时湿润分离的声音、背景里微弱的 {{ambient}}、室内底噪。每一个声
  音都必须锁定到对应的画面帧；这是一支音频主导的片子，所以要把声音
  环境描述得和画面一样详尽。

### 5 · 分镜（4–5 拍，约 10s）

```
0–2s · 期待
动作：{{dish}} 静置在砧板上，蒸汽穿过侧光卷起。一切尚未动。
运镜：探针镜头缓慢推向表面。
声音：微弱的滋滋声 / {{ambient}}，室内底噪。接触前的安静。

2–4s · 接触
动作：{{tool}} 触到表面——第一下按压，还未切开。
运镜：定在接触点，焦平面薄如刀锋。
声音：{{key_sound}} 清脆的第一声——孤立、响亮、干净。

4–7s · 切开 / 让开
动作：{{tool}} 切开 {{dish}}——{{texture}} 显露，肉汁／内里暴露，
      切面分开。
运镜：微距跟随分开的切线；缓慢移焦到湿润的内里。
声音：{{key_sound}} 完整地同步而来——这是整段片子最爽的核心。

7–10s · 收
动作：一块被提起；最后一滴肉汁落下，停在砧板上。
运镜：定住，呼吸浮动。
收尾：不要戏剧化的摆盘花活，不要厨师之手的呈现，不要闪光。只有
      最后那滴落定、蒸汽渐渐稀薄。
```

### 负面提示词（Seedance / 可灵——粘进独立负面框）
```
blurry, low resolution, soft focus, watermark, text overlay, subtitles, logo, oversaturated colors, neon food coloring, plastic food, glossy CG render, video-game look, 3D cartoon render, flat even studio lighting, perfectly clean styled magazine plate, melting/morphing geometry, extra fingers, deformed hands, frame flicker, ghosting, jarring hard cuts, lifeless locked-off camera, silent footage, audio out of sync
```

---

## 为什么这么搭

- **声音和画面被同样精心地描述（Rule 4，加强版）。** ASMR 的成败全
  系于同步拟音。我们不会只写一句「只用现场音频」就过——我们把每一个
  声音都列出来，逐帧锁定。这是唯一一个音频块比画面块还长的题材。
- **真实食物的瑕疵（Rule 5）。** 不均的煎色、被撕开的一边、一粒散落
  的碎屑、渗出的肉汁。造型完美的食物读起来像塑料 CG；正是这些瑕疵让
  它显得诱人而真实。
- **真实色彩，不要美食色情调（Rule 1）。** 「过饱和的橘色、光鲜油亮」
  正是美食视频里那种含糊夸赞的陷阱。具体的质感词（「焦脆外壳、粉嫩中
  心、湿润光泽」）胜过一味拉饱和度。
- **克制的收尾（Rule 6）。** 是最后一滴落定，而不是摆盘揭晓。这能阻
  止模型给你硬加一段光鲜的主菜呈现花活。

**用法**：先跑「切开 / 让开」那一拍（4–7s）——那是高潮回报；如果质
感揭示和同步声音在那里立住了，再围着它把其余部分搭起来。这个题材偏
爱原生音频能力强的引擎。

**模型**：Seedance 2.0 的原生同步音频是它最突出的强项——这正是该用它
的题材。Veo 3 的原生音频也极出色（在提示词里描述声音环境；用负面框
处理伪影）。可灵 3.0 处理运动很好，但要验证音画同步。在豆包 App 上，
按 5s/10s 预设锁定来规划。
