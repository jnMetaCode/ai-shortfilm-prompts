# ai-shortfilm-prompts

> 🌐 **Browse the prompt library online → [prompts.aiolaola.com](https://prompts.aiolaola.com)** — view any template/case and copy it with one click, no install.

> 📖 **免费配套学习** → [从零学会 AI 编程](https://aiolaola.com/)：180 节免费实操课 + 《AI 编程实战三卷书》在线阅读 + 实战社区 · 永久免费

<!-- ═══ HERO DEMO SLOT — publish your rendered 15s clip in 2 steps:
     1. Drag your demo.mp4 into any GitHub issue/PR comment box; copy the
        https://user-images.githubusercontent.com/... URL it generates.
     2. In the block right below, remove the surrounding comment markers and
        put that URL in place of PASTE_VIDEO_URL_HERE.
     Prompt that generates this clip: ./assets/demo-prompt.md
     (gif instead of mp4? swap the video line for: <img src="./assets/demo.gif" width="720">) ═══ -->
<!--
<p align="center">
  <video src="PASTE_VIDEO_URL_HERE" width="720" autoplay loop muted playsinline></video>
  <br><sub>▶ 15s demo — generated from a prompt this repo's Skill wrote (<a href="./assets/demo-prompt.md">prompt</a>)</sub>
</p>
-->

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/jnMetaCode/ai-shortfilm-prompts?style=social)](https://github.com/jnMetaCode/ai-shortfilm-prompts)
[![X Post](https://img.shields.io/badge/read_the_thread-@aibuzhiyu-1DA1F2?logo=x)](https://x.com/aibuzhiyu/status/2056426660577288645)
[![Plugin](https://img.shields.io/badge/Claude_Code-plugin_install-blueviolet)](#install-claude-code)

> The complete methodology + prompt library + Claude Code Skill behind
> **[*Zombie Scavenger*](https://x.com/aibuzhiyu/status/2056426660577288645)**
> by Mx-Shell — the AI short that Hollywood director PJ Ace called
> *"one of the best short films I've seen in years."*

**[中文版 →](./README.zh.md)**

> ⚡ **Quick start:** [one-page cheat sheet](./cheatsheet.md) ·
> [failure→fix gallery](./cases.md)

---

## 🎬 The tweet that started it all

> *"This is one of the best short films I've seen in years.*
> *Very soon, we'll stop calling it 'AI film' and just call it film."*
>
> *Film name: Zombie Scavenger by MX-Shell.*
>
> — **PJ Ace** ([@PJaccetturo](https://x.com/PJaccetturo)),
> [May 10, 2026](https://x.com/aibuzhiyu/status/2056426660577288645)

| 13.4M views | 82K likes | 7.4K reposts | 39K bookmarks | 2.3K replies |
|---|---|---|---|---|

<sub>Stats are from PJ Ace's original tweet ([@PJaccetturo](https://x.com/PJaccetturo), May 10, 2026), as of mid-May 2026.</sub>

This repository is **the complete workflow behind that film**, made
available because Mx-Shell himself published his prompt collection
documents and walked through his entire method on a public Douyin
livestream.

---

## ⚡ The single-line magic prompt (try it tonight)

Copy this into Sora / Seedance / Kling / Veo. Replace `{{...}}`:

```
Anamorphic widescreen cinematic. Simulated IMAX film camera +
Panavision C-series lens (35mm focal, f/4 aperture). Handheld
shot — extremely subtle, breath-like camera float throughout.
{{your scene description}}.
No score. Production audio only.
```

**Why this works**: real camera bodies + "breath-like float" anchor
the AI to actual film aesthetics — not the vague "cinematic feel"
keyword everyone else uses. Full breakdown in
[methodology.md](./methodology.md).

---

## ❌ vs ✅ — what the method actually changes

Same idea: *a female mech warrior raises an energy shield in a thunderstorm.*

**❌ The naive prompt** (what most people write):

```
Epic cinematic shot of a beautiful female mech warrior activating a
stunning energy shield in the rain. Highly detailed, 4K, photorealistic,
movie-quality, dramatic lighting.
```

Vague praise — *epic / stunning / 4K / movie-quality* — gives the model
nothing concrete to anchor to. You get generic game-CG output.

**✅ With the 5-stage method** (excerpt):

```
Core theme: gritty hard sci-fi mech | rainy dock | battle-damage aesthetic | energy shield | post-apocalyptic live-action
Atmosphere: simulated IMAX film camera + Panavision C-series (35mm, f/4). Low-saturation teal base, film grain.
Camera: handheld — extremely subtle, breath-like float throughout.
9–12s: hexagonal energy cells light up unevenly, some flicker as if faulty; rain bends around a 2m dome.
Ending: no dialogue, no light burst — just rain vaporizing on the shield, a lightning flash across the dock.
```

Real camera/lens names + physical reactions + battle damage + an empty
ending = visceral realism. Full sample with the 10-item self-check:
[examples/02-skill-output-sample.md](./skills/shortfilm-prompt/examples/02-skill-output-sample.md).

---

## The story

May 2026. A 29-year-old vocational-school graduate from rural Yunnan,
China — handle **Mx-Shell** — used **10 days** and ~20,000 RMB of
cloud credits to make a 3-minute AI short called *Zombie Scavenger*:
an atomic-punk robot wanders into a beachfront villa after a zombie
apocalypse, meets a confused ostrich, and starts dancing
1980s-style breakdance moves while kicking a zombie's head across
the floor.

> On the cost: the widely-quoted "3,000 RMB" figure came from Mx-Shell
> himself, but on livestream he later revised it to "tens of thousands /
> 20k+." The real spend was likely well above 3,000 — still far below a
> comparable live-action shoot.

Hollywood director **PJ Ace (@PJaccetturo)** retweeted the film,
calling it *"one of the best short films I've seen in years"* and started a
search for the author.

A few weeks later Mx-Shell went on a Douyin livestream and **gave
away his entire workflow** — the prompts, the camera language, the
failure modes, the reroll counts.

This repo is the result of digesting 130,000 characters of his
materials into a structured, reusable system.

---

## What's in here

```
ai-shortfilm-prompts/
├── README.md              You're here. English entry point.
├── README.zh.md           Chinese version.
├── cheatsheet.md          One-page cheat sheet (the whole method at a glance).
├── cheatsheet.zh.md       Chinese version.
├── cases.md               Failure→fix gallery: common bad output and the fix.
├── cases.zh.md            Chinese version.
├── methodology.md         The 5-stage prompt structure, explained.
├── methodology.zh.md      Chinese version.
├── faq.md                 Q&A: tools, failures, costs, edge cases.
├── faq.zh.md              Chinese version.
├── credits.md             Sources & attribution.
├── credits.zh.md          Chinese version.
├── showcase.md            Things people made with the method.
├── CONTRIBUTING.md        Submission template & rules for new prompts.
├── LICENSE                MIT (this work)
├── NOTICE                 Attribution + Mx-Shell ARR details (dual-licensing)
│
├── prompts/                Mx-Shell's complete original prompts.
│                           Body kept in Chinese (his authorial
│                           voice), with English header on each file.
│   ├── README.md           Index of all prompt archives
│   ├── index.json          Machine-readable index of every prompt
│   ├── zombie-scavenger.md             *Zombie Scavenger*
│   ├── kamen-rider-transformations.md   Kamen Rider transformation × 6 (5 riders + flight)
│   ├── kaisa-transformation.md       LoL Kai'Sa transformation × 3 versions
│   ├── pacific-rim-gundam.md         Pacific Rim + Gundam mech-drop
│   ├── cyber-wuxia.md                Shaw Brothers + steampunk wuxia template
│   └── metal-gear-charge-combat.md   Weapon-charge + combat composite
│
├── templates/              IP-stripped generalized templates (EN + .zh.md siblings).
│                           Authored by jnMetaCode based on Mx-Shell's structure.
│   ├── 15s-transformation.md         15-second transformation
│   ├── multi-shot-narrative.md       Multi-shot edited narrative
│   ├── atmosphere-prefabs.md         8 reusable atmosphere/look prefabs
│   ├── negative-prompts.md           Reusable negative-prompt prefab (per-model)
│   ├── genre-camera-sop.md           Camera-movement SOP for 5 film genres
│   ├── camera-move-library.md        50 camera moves in 5 technique modules
│   ├── pet-lifetime-narrative.md     Worked example: pet × family emotional narrative
│   ├── family-recipe-farewell.md     Worked example: a mother's recipe handed down
│   └── elderly-cat-companion.md      Worked example: grandmother & cat, empty-nest
│
├── assets/                 Diagrams + the README hero-demo prompt.
│   ├── demo-prompt.md       Copy-paste 15s prompt the Skill wrote (hero slot)
│   └── 5-stage-structure.svg  The structure diagram
│
├── skills/shortfilm-prompt/   Claude Code Skill
│   ├── SKILL.md            How Claude should generate prompts (7 hard rules + 10-item checklist)
│   ├── TESTING.md          How to run rigorous skill tests in another Claude window
│   └── examples/           4 test cases (5 files) with expected outputs
│
└── .claude-plugin/         Plugin metadata (plugin.json + marketplace.json)
```

---

## TL;DR — The 5-stage prompt structure

<p align="center">
  <img src="./assets/5-stage-structure.svg" alt="The 5-stage prompt structure" width="660">
</p>

Every Mx-Shell video prompt follows the same skeleton. The order matters:

```
1. Core theme            ← 3-6 style tags separated by |
2. Character & scene     ← Face / clothing / environment
3. Atmosphere & quality  ← Visual base / color tone / style core
4. Camera rules          ← Single-shot or multi-shot / angle / breathing
5. Storyboard            ← Per-second OR per-shot breakdown
```

### Three counter-intuitive rules

1. **Specify real camera + lens models.**
   Don't write *"cinematic feel"*. Write
   *"simulated IMAX film camera, Panavision C-series lens, 35mm focal,
   f/4 aperture."* AI training data binds those exact strings to real
   movie aesthetics.

2. **Describe imperfections.**
   *"Battle-damaged armor, paint worn off, oil in the joints, minor
   facial blemishes preserved."* Perfection looks fake. The visceral
   realism comes from the flaws.

3. **Leave the ending empty.**
   *"No dialogue. No explosion. No blinding light.
   Just a figure standing in the smoke, a meteor crossing the sky."*

Full methodology in [methodology.md](./methodology.md).

---

## Install (Claude Code)

### Option 1 — Plugin Marketplace ⭐ (one-line install)

```
/plugin marketplace add jnMetaCode/ai-shortfilm-prompts
/plugin install ai-shortfilm-prompts@ai-shortfilm-prompts
```

Then in Claude Code:

```
/ai-shortfilm-prompts:shortfilm-prompt  Help me write a 15-second prompt for a
                                        robot transformation, green color palette,
                                        energy core in the belt buckle,
                                        post-apocalyptic jungle background
```

### Option 2 — Try it inside this repo

```bash
git clone https://github.com/jnMetaCode/ai-shortfilm-prompts.git
cd ai-shortfilm-prompts
claude --plugin-dir .   # then: /ai-shortfilm-prompts:shortfilm-prompt
```

### Option 3 — Make it available globally (manual copy)

```bash
mkdir -p ~/.claude/skills
cp -r ai-shortfilm-prompts/skills/shortfilm-prompt \
      ~/.claude/skills/
```

### Option 4 — As a submodule in your own project

```bash
git submodule add https://github.com/jnMetaCode/ai-shortfilm-prompts.git \
                  vendor/ai-shortfilm-prompts
claude --plugin-dir vendor/ai-shortfilm-prompts   # loads the plugin + skill
```

The Skill walks through the 5-stage structure, runs a 10-item self-check,
and warns you about IP names that may be blocked by Seedance 2.0.

---

## Compatible video models

The 5-stage structure is **model-agnostic**. Here's how the major 2026
engines compare — single-shot ceiling, negative-prompt support, IP filter,
preferred prompt language, and the one gotcha that trips people up:

| Model | Max single shot | Negative prompt | IP filter | Lang | Notes / gotcha |
|---|---|---|---|---|---|
| **[Seedance 2.0](https://dreamina.onelink.me/yKT4/dw7oxbdd)** (Doubao / Jimeng / [Xiaoyunque](https://xiaoyunque.jianying.com/s/ufhQBHB9CHg/), ByteDance) — *Mx-Shell's primary engine* | ~10–15s — but the **Doubao app is locked to 5s/10s preset buttons**; the full 4–15s range only on Jimeng/Dreamina web + VolcEngine console | Partial — no reliable dedicated field in the consumer app; negate by describing what you *do* want | Strict — domestic platforms aggressively reject named celebrities + branded IP | Either (ZH native, EN works) | Duration depends entirely on the front-end. Don't promise 15s if the user is on the Doubao app. Native synced audio-video is its standout strength. |
| **[Veo 3 / 3.1](https://deepmind.google/models/veo/)** (Google) | 8s per clip (4/6/8s); Extend adds 7s hops up to ~148s, but quality degrades after 4–5 extensions | Yes — dedicated field. List unwanted elements as plain nouns (`extra limbs, glitch morphs`); **no `no`/`don't` command phrasing** | Strict — rejects public figures, brands, voice/likeness; scans prompt *and* frames | EN | The negative field wants descriptive phrases, not commands — `no rain` style instructions can backfire. Best-in-class native audio + realism. |
| **[Kling 2.x / 3.0](https://klingai-share.kuaishou.com/h5-app/invitation?code=6BCGZXWZRMA9)** (Kuaishou) | 2.5: 5–10s (Pro ~12s); **3.0: up to ~15s single-prompt** multi-shot | Yes — dedicated field. Use for stability artifacts (sliding feet, extra fingers, morphing), not generic "quality" words | Strict — a pre-gen banned-word filter rejects the **whole prompt** on one match; hypersensitive | Either (ZH native, EN strong; 3.0 multilingual dialogue) | The banned-word filter is notoriously over-sensitive — a benign body/contact word can block a clean prompt. Sanitize wording first. Excellent action/motion realism. |
| **[Hailuo / MiniMax](https://hailuoai.video/)** (02 / 2.3) | ~6–10s — 1080p caps ~6s, 768p extends ~10s | Yes — but vendor guidance says use sparingly, for specific artifacts not as a primary lever | Moderate — more permissive than Sora/Veo, still blocks named celebs + overt IP | Either (ZH native, EN solid) | Resolution and duration trade off — you can't get max of both. Pick the axis that matters per shot. Strong motion at low cost. |
| **[Wan 2.x](https://tongyi.aliyun.com/)** (Alibaba, open-source) | 2.2: ~3–8s @ 24–30fps; 2.5/2.6 extend ~10–15s by mode | Yes — robust field; defaults like `morphing, warping, face deformation, flickering` | Lenient — open-weights/self-hostable, so **no enforced filter when run locally** (hosted APIs may add their own) | Native ZH (both, but ZH-trained) | Leans Chinese — first/last-frame mode especially; EN-only prompts can underperform, add ZH for tricky shots. Self-hostable, full ComfyUI control, renders legible ZH/EN on-screen text. |
| **[Runway Gen-4 / 4.5](https://runwayml.com/)** | 5s or 10s per generation | **No — does NOT support negatives.** `avoid X / no X` can produce the opposite. Describe only what *should* appear | Strict — blocks celebs, real people, copyrighted characters/brands | EN | Negative prompts are actively harmful here — `no distorted hands` can summon distorted hands. The single biggest mistake when porting prompts. Director-grade camera control + mature pro pipeline. |
| **[Pika](https://pika.art/)** (2.2 / 2.5) | Standard + Pikascenes: 5s or 10s; **Pikaframes (keyframe) up to ~25s** | Partial — 2.5 supports negatives (`no morphing, no extra limbs`); 2.2 unclear, verify in-app | Moderate — blocks overt celebs/IP, generally more relaxed than Sora/Veo | EN | Only the Pikaframes keyframe path reaches ~25s — ordinary text/image-to-video is still 5s/10s. Fast, effects/transition-driven, great for stylized short-form. |
| **[Sora 2 / 2 Pro](https://sora.com/)** (OpenAI) | Up to ~25s continuous single-pass on Sora 2 Pro (standard tier shorter) | No dedicated field — negate in-prompt with guardrails like `original characters only, no logos or text` | Strict — triple-layer moderation; blocks named IP **and visual lookalikes** even without the name | EN | The filter catches *descriptions*, not just names — `a spiky-haired ninja in an orange jumpsuit` still trips it (matches Naruto). Avoid recognizable trait-bundles, not only proper nouns. Leading prompt comprehension + world coherence. |

<sub>Durations and negative-prompt mechanics for Veo 3.1, Runway Gen-4, Kling,
Wan, and Sora are consistent across multiple 2026 vendor/help-doc sources;
Seedance 2.0 and Hailuo figures lean on third-party guides (treat `~` as
approximate). "Veo ~148s", "Sora/Pika ~25s" come from extension/keyframe
features, **not** plain single-shot generation. IP-filter "strictness" labels
are qualitative.</sub>

<sub>Tool names link to their sign-up pages; Xiaoyunque / Jimeng / Kling are invite links (both sides get free credits).</sub>

---

## Sister projects (by the same author)

This is the video-prompt sibling of the AI-coding ecosystem maintained
by [@jnMetaCode](https://github.com/jnMetaCode):

- [superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) — Chinese-enhanced edition of `obra/superpowers` (TDD / debug / git workflow skills)
- [agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) — 211 plug-and-play AI expert personas
- [agency-orchestrator](https://github.com/jnMetaCode/agency-orchestrator) — Multi-agent collaboration orchestrator
- [ai-coding-guide](https://github.com/jnMetaCode/ai-coding-guide) — 66 Claude Code tips
- [shellward](https://github.com/jnMetaCode/shellward) — AI Agent security middleware
- [ai-coding-trilogy](https://github.com/jnMetaCode/ai-coding-trilogy) — AI coding three-volume book

All projects share the same `SKILL.md` format. The video skill stacks
freely with any of them.

---

## Contributing

The roadmap is to collect more AI-shortfilm creators' methods, structured the
same way. New prompts, templates, fixes, and translations are welcome — see
[CONTRIBUTING.md](./CONTRIBUTING.md) for the submission template and rules
(public source required, credit the original creator).

Made something with the method? It goes on the [showcase](./showcase.md).

---

## Follow · 关注作者

<p>
  <img src="docs/assets/qr-wechat.jpg" width="168" alt="WeChat 公众号 AI 不止语">
  &nbsp;&nbsp;
  <img src="docs/assets/qr-douyin.jpg" width="168" alt="抖音 AI 不止语">
</p>

微信公众号「**AI 不止语**」 · 抖音 **@AI不止语**（AIBZY） · [X @jnMetaCode](https://x.com/jnMetaCode) · [aiOlaOla — 免费学 AI 编程](https://aiolaola.com/)

🌐 Live prompt library → **[prompts.aiolaola.com](https://prompts.aiolaola.com)**

---

## License

**[MIT License](./LICENSE)** for everything authored by jnMetaCode
(methodology, FAQ, templates, Skill, metadata). Free for any use
including commercial — just keep the copyright notice.

Mx-Shell's original prompts and document excerpts — sourced from his
fan-group documents and public Douyin livestream that he himself
distributed — remain **© Mx-Shell, all rights reserved**. Archived here
for educational reference; commercial use requires contacting Mx-Shell
directly. Full dual-licensing details: [NOTICE](./NOTICE) ·
attribution: [credits.md](./credits.md).

---

## A line worth remembering

> *"For creation, the equipment is not what matters.
> The idea is what matters."*
> — Mx-Shell, May 12, 2026 livestream
