# Credits & Sources

> Where the content in this repo comes from, who owns what, and how
> it should be used.
>
> **[中文版 →](./credits.zh.md)**

---

## Original author

**Mx-Shell**

- Yunnan, China; 29 years old (his own quote: *"I'm 28… wait, I'm 29 this
  year. Turning 30 next year."*)
- Vocational school graduate, photography as a paid side gig
- Married, with a kid
- Started touching AI video in **January 2026**. His first AI work was a
  promotional video for his sister's hotel — Xinping Hilton in Yuxi,
  Yunnan (*"My first AI video was for our family's hotel — my sister's
  hotel — Xinping Hilton in Xinping, Yuxi, Yunnan"*)
- *Zombie Scavenger* went viral in May 2026

---

## Source material

This repo was distilled from materials Mx-Shell **voluntarily and
publicly distributed** via two channels:

| File | Content | Date |
|---|---|---|
| `mx-shell prompt + Q&A (2026.03.15).docx` | 17 troubleshooting items + 10+ complete prompt artifacts | March 15, 2026 |
| `mx-shell prompt collection + Q&A (2026.05.10).docx` | Kamen Rider variants + two key shots from Zombie Scavenger | May 10, 2026 |
| `Livestream transcript part 1.doc` | First half of his Douyin Q&A | May 12, 2026 |
| `Livestream transcript part 2.doc` | Second half of his Douyin Q&A | May 12, 2026 |
| `Livestream clip.mp4` | A 7-minute slice of the original stream | May 12, 2026 |

The docx files were shared in his fan group. The livestream was public
on Douyin. All sources are voluntary public distribution — not leaked,
scraped, or extracted privately.

---

## What this repo does

What this repo **does not** do:
- Does not rewrite, expand, or "re-create" Mx-Shell's original prompts
- Does not strip his name or impersonate him

What this repo **does** do:
- Distills [methodology.md](./methodology.md) — the systematic 5-stage
  structure from his livestream + documents
- Consolidates [faq.md](./faq.md) — his 17 troubleshooting items plus
  scattered Q&A
- Converts the docx/doc files into structured markdown
  (`prompts/`)
- Extracts the [model templates](./templates/) — IP-stripped reusable bones
- Provides a [Claude Code Skill](./skills/shortfilm-prompt/) so
  Claude can produce prompts following his methodology

Every `prompts/` file marks its source document and date.

---

## Mx-Shell's stance on sharing

From the March 15 document (item 17):

> *"This Kamen Rider thing was just a whim. I didn't expect this much
> attention. Thanks everyone for liking it. If you joined the fan group
> just to grab the prompts and then leave — fine, I don't mind.*
>
> *I'm sharing my prompts with you. Use my templates as a starting
> point. Let your imagination run.*
>
> *Several people in my group have already written excellent prompts
> from these templates. Feel free to swap learnings."*

From the May 12 livestream:

> *"You can learn this, you can take it and do whatever — I don't care.*
>
> *I source from atom-punk. The image I used is the one you see. Anyone
> claiming I scraped from a game — go check, I never wrote any IP names
> in my prompts."*

> *"I hope this lets the Chinese AI scene draw some inspiration from
> what I shared today. Not saying I'm a benchmark — just hoping it
> helps someone."*

---

## Repo maintainer commitments

- ✅ Mx-Shell's name + source links preserved everywhere
- ✅ Commercial usage of his content must be cleared with him directly
  (see LICENSE)
- ✅ Any modification / takedown request from him will be honored
  **immediately**
- ✅ No author impersonation
- ✅ No use of this content for training commercial AI models

---

## Third-party citations

- **Jesse Vincent (@obra)** — creator of the [superpowers](https://github.com/obra/superpowers)
  SKILL system. The `SKILL.md` frontmatter format + TDD-driven skill-
  writing methodology used in this repo derives from his work.
- **PJ Ace (@PJaccetturo)** — Hollywood director. First retweeted
  *Zombie Scavenger* calling it *"one of the best short films in recent
  years,"* introducing it to English-speaking audiences.

---

## Tools mentioned in this repo

(Mx-Shell's self-reported stack — no endorsement)

| Purpose | Tool |
|---|---|
| Video generation | **Xiaoyunque / Seedance 2.0** (avoid Fast variant) |
| Image generation | **GPT Image** (80%) + Midjourney + Krea |
| Texture refinement | **Flux Max** |
| 3-view design | **Nanobanana** |
| Prompt drafting helper | **Doubao** (combat scenes) |
| Editing | **CapCut** (剪映) |
| Music | **Artlist.io** (licensed, not AI-generated) |

---

## On IP names in original prompts

Mx-Shell's original prompts contain some IP names:

- 仮面ライダー BLACK SUN (Kamen Rider BLACK SUN)
- Gundam
- Pacific Rim
- Ready Player One
- Metal Gear Solid
- Kai'Sa (League of Legends)
- Iron Man
- Michael Jackson (referenced for dance style)

These IP rights belong to their respective owners. This repo retains
the original prompts as **faithful records of the source material**.
When using them:

1. Seedance 2.0 is known to filter IP names — direct use often gets
   **blocked**
2. Commercial use requires clearing rights with each IP holder
3. Personal learning / non-commercial use is lower risk but still
   advisable to substitute with style descriptions

The [templates/](./templates/) directory contains IP-stripped generalized versions.

---

## How to cite this repo

Suggested format:

> Methodology derived from Mx-Shell's publicly-shared *Zombie Scavenger*
> materials, organized at:
> https://github.com/jnMetaCode/ai-shortfilm-prompts
>
> Original prompts © Mx-Shell, 2026 · Organized analysis © jnMetaCode, 2026

---

## Contact

- **Repo maintainer**: [@jnMetaCode](https://github.com/jnMetaCode)
  · WeChat public account "AI 不止语"
- **Issues / feedback**: [GitHub Issues](https://github.com/jnMetaCode/ai-shortfilm-prompts/issues)
- **Mx-Shell**: Douyin handle "Mx-Shell"
