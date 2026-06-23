# 实战范例 — 监控录像 / 伪纪录恐怖

> jnMetaCode 原创实战范例（MIT）。把 5 段式结构用在**伪纪录 / 监控录像
> 恐怖**上——这是一个**劣质相机本身就是全部美学**的题材，靠克制（而非
> 血腥）制造恐惧。还有一处刻意的破例：相机是固定机位，所以放弃了呼吸浮
> 动（监控不会动）。
>
> 概念：一台固定监控摄像头，对着夜里空无一人的走廊；有什么东西，微妙地、
> 不对劲地反常。换掉地点，留住这份克制。
>
> *延伸阅读（只作灵感，未照搬——全部用我们的结构重写）：
> [zhangchenchen/awesome_sora2_prompt](https://github.com/zhangchenchen/awesome_sora2_prompt)
> 里的 Horror / CCTV 风格分类（MIT）。*
>
> **[English →](./found-footage-horror.md)**

---

## 开始前需要先定义的变量

| 变量 | 本例取值 | 可替换为… |
|---|---|---|
| `{{place}}` | 凌晨 3 点空荡的办公室走廊 | 停车场 / 楼梯间 / 后院 |
| `{{wrong_thing}}` | 走廊尽头本来关着的门此刻开着 | 半截身子探出画面的人影 / 灯一盏接一盏熄灭 |
| `{{cam_type}}` | 天花板监控摄像头，广角 fisheye | 门铃摄像头 / 手持手机 / 婴儿监视器 |
| `{{timestamp}}` | 03:14:07 AM，右上角 | 烧录日期 / 频道标签 |
| `{{night_mode}}` | IR 夜视绿灰 | 低照度彩色，带重噪点 |

---

## 完整提示词（可直接复制）

### 1 · 核心主题
`found-footage horror | fixed security-cam angle | {{night_mode}} | 靠静止制造恐惧 | 不要 jumpscare 血腥，不要电影质感`

### 2 · 人物与场景

**主体（这个空间，以及它哪里不对劲）：** {{place}}，空旷、静止。恐怖之
处在于*几乎*什么都没发生——然后 {{wrong_thing}}。没有怪物现身，没有血。
那份不对劲安静而具体。

**作为"角色"的"相机"（这就是质感所在）：** {{cam_type}}——{{night_mode}}，
低分辨率，暗部能看见压缩块（compression blocking），细微的传感器噪点在
画面里爬行，广角/fisheye 边缘略带畸变，一个 {{timestamp}} 烧录字幕，以及
偶尔的掉帧/卡顿（dropped/stuttered frame）。这些瑕疵**就是**美学——不是
要清理掉的缺陷。

### 3 · 氛围与画质
拍得像真正的劣质监控录像：**不是**电影摄影机。低动态范围，压死的黑里带
噪点，绿灰 IR 或浑浊的低照度彩色，压缩伪影，跟不上黑暗的固定曝光。这份
"丑"才是真实感——任何看起来调过色或有电影感的东西都会破坏这个错觉。

### 4 · 运镜规则
**固定机位——锁死。刻意不要呼吸浮动（NO breath-float）。** 监控摄像头不
会呼吸、不会漂移、不会重新构图；它只是盯着。（这就是那处破例：这套模板
里大多锚定的手持浮动会立刻被读成"有个人在拍"，毁掉监控录像的错觉。）全
镜头就一个固定广角。
- *声音：* No score。只有环境底噪——空调嗡鸣、远处一记无法解释的敲击、
  快坏掉的灯发出的电流嗡声。沉默替你做事。

### 5 · 分镜（3 拍，约 10s）

```
0–4s · 正常（建立无聊感）
画面: {{place}}，空荡、静止。{{night_mode}}，噪点在爬，{{timestamp}} 在
      走。什么都没发生。把无聊撑住——这是在下套。
镜头: 固定广角。锁死。
声音: 环境底噪，一点轻微嗡鸣。

4–7s · 不对劲（那个微小而具体的变化）
画面: {{wrong_thing}}——微妙、容易错过、没有音效突刺。就在它发生的那一
      刻，画面卡顿/掉一帧。
镜头: 依旧固定。得让眼睛自己去找它。
声音: 嗡鸣，也许远处一记敲击。没有 stinger。

7–10s · 停住（克制收尾）
画面: 别的什么都没动。那个不对劲的东西就……留在那儿。录像继续在这片空
      荡、如今已经不对劲的空间上滚动。
收尾: 没有现身、没有怪物、没有尖叫、没有伴着一声巨响切黑。只是 timestamp
      在一条不再正常的走廊上继续走。
```

### 负面提示词（Seedance / Kling——粘进独立负面框）
```
cinematic color grade, filmic look, shallow depth of field, smooth handheld motion, breathing camera float, dramatic lighting, lens flare, high resolution clean image, watermark, logo, gore, blood splatter, jumpscare monster reveal, oversaturated colors, 3D cartoon render, video-game look, polished VFX, score music, melting/morphing geometry, warped unreadable timestamp text
```

---

## 为什么这么搭

- **劣质相机本身就是这个题材（刻意反用 Rule 2）。** 我们不锚定"ARRI +
  Panavision"，而是锚定"监控摄像头、IR 夜视、压缩噪点、时间戳"。这种劣
  质的观感，正是让人相信"这是某人捡到的真实录像"的关键。一张干净的电影
  级画面会毁掉它。
- **锁死机位，不要呼吸浮动（Rule 3 例外）。** 固定相机只会盯着。任何漂移
  都会被读成有人在操控，破坏设定——所以我们去掉浮动，并把"breathing
  camera float / smooth handheld"写进负面。
- **克制就是恐怖（Rule 6，武器化）。** 没有怪物、没有血腥、没有音效突刺。
  在一个无聊画面里出现一个微小而具体的*不对劲*，比任何现身都吓人——还能
  阻止模型默认套路化的廉价 jumpscare。
- **瑕疵当作不完美锚点（Rule 5）。** 噪点、压缩块、掉一帧、fisheye 边缘。
  在这里，这些"瑕疵"不是为加真实感而添加的——它们就是整个媒介本身。

**用法**：先跑*正常*那一拍，确保它读起来像货真价实的劣质录像（噪点、时间
戳、固定机位）；如果跑出来太干净/太电影感，就在负面框里使劲压。把
{{wrong_thing}} 留得小——克制才是吓人的地方。

**模型**：Sora 2 极擅长那种"诡异真实录像"的观感，也能稳住固定画面；Kling
和 Seedance 也行，但要盯着它们别把画面美化了——把负面框推满。屏幕上的
timestamp 尽量短，免得模型把文字扭曲掉。
