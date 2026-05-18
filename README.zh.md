# ai-shortfilm-prompts · AI 短片提示词方法论

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/jnMetaCode/ai-shortfilm-prompts?style=social)](https://github.com/jnMetaCode/ai-shortfilm-prompts)
[![X Post](https://img.shields.io/badge/PJ_Ace_tweet-13.4M_views-1DA1F2?logo=x)](https://x.com/PJaccetturo/status/2053475534965965067)

> AI 短片提示词写作的开源方法库 + 案例集 + Claude Code Skill。
> 首发版本基于 Mx-Shell《丧尸清道夫》(Zombie Scavenger) 拆解 ——
> **让好莱坞导演 PJ Ace 评为"近年来最佳短片之一"** 的作品。
> 后续计划收录更多 AI 短片创作者的方法。

---

## 🎬 PJ Ace 那条引爆的推文

> *"这是我近年来看过最好的短片之一。"*
> *"很快，我们将不再称其为'AI 电影'，而直接称其为电影。"*
>
> *Film name: Zombie Scavenger by MX-Shell.*
>
> —— **PJ Ace** ([@PJaccetturo](https://x.com/PJaccetturo))
> [2026 年 5 月 10 日](https://x.com/PJaccetturo/status/2053475534965965067)

| 1340 万 浏览 | 82K 点赞 | 7.4K 转发 | 39K 收藏 | 2.3K 评论 |
|---|---|---|---|---|

本仓库是这部短片背后**完整的工作流** —— Mx-Shell 自己在粉丝群分享了提示词文档，又在抖音直播完整讲了他的方法论。我们做的是结构化整理。

---

## ⚡ 今晚就能抄的一句话

复制到 Sora / Seedance / 可灵 / 即梦 / Veo，替换 `{{...}}`：

```
变形宽荧幕电影质感。模拟 IMAX 胶片摄影机 + Panavision C 系列镜头
（焦段 35mm，光圈 f4）。手持拍摄，全程保持极其轻微的、如呼吸般的镜头浮动。
{{你的场景描述}}。
不需要配乐，仅保留同期声。
```

**为什么管用**：写具体摄影机型号 + "呼吸感"运镜，能把 AI 锚定到真电影美学；"电影感"这种空泛词没用。完整拆解见 [方法论](./methodology.zh.md)。

---

---

## 故事

2026 年 5 月，**Mx-Shell**（云南玉溪人，中专学历，29 岁，已成家，摄影副业）用 **10 天** 做出 3 分钟 AI 短片《丧尸清道夫》：原子朋克机器人在末日丧尸危机后的滨海别墅，与一只呆鸵鸟相遇，跳着 1980 年代标志性舞蹈风格的霹雳舞，踢飞丧尸头颅。

> 关于"3000 元成本"：网传的口径来自 Mx-Shell 本人，但他在直播里被追问时又改口为"几万 / 两万多块钱"。真实开销大概率比 3000 元高，但仍然远低于真人拍摄的同等时长短片。第一部 AI 作品是给姐姐家的云南玉溪新平希尔顿酒店做的（2026 年 1 月）。

短片被好莱坞导演 **PJ Ace** 评为"近年来最佳短片之一"并全网寻找原作者。
他事后开了两次直播，把自己写提示词的思路全部讲出来，还把当初的文档分享给了粉丝。

**这个仓库是把那些原始材料整理、归纳、结构化，让你能学到他写提示词的方法。**

不是教你复刻这部片子。是教你写出能做出**自己作品**的提示词。

---

## 这里有什么

```
ai-shortfilm-prompts/
├── README.md                  ← 你在看的这一份
├── LICENSE                    ← MIT
├── .claude-plugin/            ← plugin 元数据（plugin.json + marketplace.json）
├── 方法论.md                  ← Mx-Shell 的 5 段式提示词模板讲解 ⭐
├── 实战FAQ.md                 ← 整合的 17 条 + 直播 Q&A
├── 原始提示词/                ← Mx-Shell 公开过的 10+ 个完整作品
│   ├── 索引.md
│   ├── 丧尸清道夫.md          ← 标志作
│   ├── 假面骑士-变身系列.md   ← 5 个变体共享一套模板
│   ├── 卡莎-LOL变身.md        ← 15s / 20s / 5s 三个版本
│   ├── 环太平洋-高达.md       ← 重型机甲跳机 + FPV 运镜
│   ├── 赛博江湖.md            ← 邵氏 + 蒸汽朋克模板
│   └── 合金装备-武器充能与打斗.md ← 后期剪辑型动作戏
├── 模板/                       ← 去掉 IP 的通用骨架
│   ├── 15秒变身模板.md
│   ├── 多分镜叙事模板.md
│   └── 风格画质骨架.md         ← 7 种可复用的氛围段
├── 教程/                       ← 可以直接发布到各平台的二次创作内容
│   ├── README.md               ← 分发策略
│   ├── 公众号长文-丧尸清道夫拆解.md  ← ~5000 字深度版
│   └── 抖音小红书短文版.md          ← 短平快版（抖音/小红书/Twitter）
├── .claude/skills/shortfilm-prompt/  ← Claude Code Skill
│   └── SKILL.md                ← /shortfilm-prompt 调用后自动生成提示词
├── 来源与致谢.md
└── 资料/                       ← 原始 docx / 直播 mp4 / pandoc 转换的 md
    ├── 直播回放切片.mp4
    ├── mx-shell提示词+问题解决方案（2026.03.15).docx
    ├── mx-shell提示词合集+问题解决方案(2026.05.10).docx
    ├── 直播回放文字版1.doc
    ├── 直播回放文字版2.doc
    ├── 视频说明.md              ← 视频内容说明 + 处理建议
    ├── 视频截图/                ← 6 张直播关键帧（可作教程配图）
    └── markdown/              ← pandoc 转出来的 md 归档
```

---

## 怎么读

**如果你只有 10 分钟** → 读 [方法论.md](./方法论.md)。
那里讲了 Mx-Shell 反复使用的 5 段式结构，看完你大概就能开始自己写。

**如果你想自己做一部变身/丧尸/MV 短片**：
1. 先看 [方法论.md](./方法论.md) 理解结构
2. 翻 [原始提示词/](./原始提示词/) 找一个最接近你想做的作品
3. 翻 [模板/](./模板/) 找一份去 IP 的骨架，填上自己的设定
4. 翻 [实战FAQ.md](./实战FAQ.md) 看遇到具体问题怎么处理

**如果你用 Claude Code**：
把 `.claude/skills/shortfilm-prompt/` 拷到你的工作目录（或 `~/.claude/skills/` 全局可用），然后输入 `/shortfilm-prompt` —— Skill 会问你几个问题然后帮你写提示词。

---

## 这套方法论是为谁写的

- **写过提示词，但效果一直不稳定**的人 —— 这里有结构化的写法。
- **想做 AI 短片，但不知道从哪开始**的人 —— 直接套用模板就行。
- **被"AI 生成视频质量差"劝退**过的人 —— 90% 的问题不是模型不行，是提示词没写对。

---

## 这套方法论**不是**

- 一键复制粘贴的咒语 —— Mx-Shell 自己也说"用同样的提示词生成两次都会差很多"。AI 是抽卡。
- 通用万灵药 —— 这套方法主要为 **Seedance 2.0 / 小云雀 沉浸式短片**优化。其他模型（Sora / 可灵 / 即梦）思路通用，具体词汇可能要调。
- 完整教程 —— 没讲剪辑、调色、配乐、后期。建议自学剪映 + 找 Artlist 等版权音乐网站。

---

## 安装 Skill（Claude Code 用户）

三种方式任选：

**方式 1：项目内引用**（推荐用于试用）
```bash
git clone https://github.com/jnMetaCode/ai-shortfilm-prompts.git
cd ai-shortfilm-prompts
claude  # 进入 Claude Code 后输入 /shortfilm-prompt
```

**方式 2：全局可用**
```bash
mkdir -p ~/.claude/skills
cp -r ai-shortfilm-prompts/.claude/skills/shortfilm-prompt ~/.claude/skills/
# 在任意目录启动 Claude Code 都能用 /shortfilm-prompt
```

**方式 3：Git Submodule**（持续追更）
```bash
git submodule add https://github.com/jnMetaCode/ai-shortfilm-prompts.git .claude/skills/_shortfilm
# 更新：git submodule update --remote
```

---

## 姊妹项目（同作者的其他仓库）

本项目是 [@jnMetaCode](https://github.com/jnMetaCode) 系列的视频方向第一个项目。其他方向：

- [superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) —— 编程方法论 skill 中文增强版
- [agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) —— 211 个 AI 专家角色
- [agency-orchestrator](https://github.com/jnMetaCode/agency-orchestrator) —— 多角色协作编排
- [ai-coding-guide](https://github.com/jnMetaCode/ai-coding-guide) —— Claude Code 技巧速查
- [shellward](https://github.com/jnMetaCode/shellward) —— AI Agent 安全中间件
- [ai-coding-trilogy](https://github.com/jnMetaCode/ai-coding-trilogy) —— AI 编程实战三卷书

---

## 常用工具

Mx-Shell 自述他用的工具栈（数据来自直播 + 文档）：

| 用途 | 工具 |
|---|---|
| 视频生成 | 小云雀里的 **Seedance 2.0**（**不**用 Fast 版） |
| 图像生成 | **GPT Image**（占 80%）+ Midjourney + Krea |
| 材质优化 | **Flux Max**（金属、瓷砖、皮肤细节单独过一遍） |
| 三视图 | **Nanobanana** |
| 文案辅助 | **豆包** + ChatGPT（打斗戏让豆包写后自己改） |
| 剪辑 | **剪映** |
| 配乐 | **Artlist.io**（版权音乐） |

---

## 致谢

**Mx-Shell** —— 原始材料的作者。
他的话：
> 我把我的提示词分享给各位，按照我写的这些模版，
> 大家可以自己发挥自己的想象力去创作。
> 群里有好几个兄弟用我的模版自己编写出来的我看了真的非常不错，
> 大家也可以多交流，互相学习。

**PJ Ace（@PJaccetturo）** —— 好莱坞导演，最初点赞《丧尸清道夫》让它出圈。

详见 [来源与致谢.md](./来源与致谢.md)。

---

## License（双重许可）

- **jnMetaCode 原创工作**（方法论 / FAQ / 模板 / Skill / 元数据）—— **[MIT License](./LICENSE)**，免费使用包括商业用途，保留版权声明即可
- **Mx-Shell 原创内容**（原始提示词原文 / 直播 + 文档原文引用）—— **版权归 Mx-Shell 所有**，仅作学习参考归档，来源是他本人公开分享的粉丝群文档与抖音直播；商业使用须联系本人

完整许可见 [LICENSE](./LICENSE)（MIT 标准） + [NOTICE.zh](./NOTICE.zh)（双重许可细节）。归属说明见 [credits.zh.md](./credits.zh.md)。

---

## 一句话

> "我说白了，对于创作来说，设备不是重要的。想法才是最重要的。"
> —— Mx-Shell，2026 年 5 月直播
