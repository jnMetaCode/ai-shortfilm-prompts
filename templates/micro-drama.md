# Worked Example — Vertical Micro-Drama (竖屏短剧)

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to the **vertical micro-drama** — the short-form dramatic
> scene format built for phones (抖音/Reels 短剧). Teaches vertical-first
> framing, shot-reverse-shot dialogue grammar, and the hook + cliffhanger
> structure that drives binge-watching.
>
> Concept: a tense two-person confrontation with a cold-open hook and a
> cliffhanger cut. Swap the conflict, keep the structure. IP-free.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): viral/short-form patterns in
> [zhangchenchen/awesome_sora2_prompt](https://github.com/zhangchenchen/awesome_sora2_prompt)
> (MIT).*
>
> **[中文版 →](./micro-drama.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{a}}` | a tired young woman, office wear | the protagonist — describe, no IP |
| `{{b}}` | an older man, expensive suit | the antagonist / the twist character |
| `{{hook}}` | she slaps a resignation letter on the desk | the shocking first-2s beat |
| `{{conflict}}` | "You knew. The whole time." | the line that escalates it |
| `{{cliff}}` | he slides her a photo — she freezes | the unanswered turn that ends the clip |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`vertical micro-drama | dialogue confrontation | hook-heavy cold open | shot-reverse-shot | grounded performance, no soap-opera overacting`

### 2 · Character & scene

**Characters:** {{a}} and {{b}}. Reference uploaded photos, features 100%
preserved, no beautification. Real, restrained emotion — a tight jaw, a
flicker in the eyes, a held breath — not theatrical overacting.
Imperfections: tired eyes, a stray hair, real skin, a slightly creased
collar. The realism makes the drama land.

**Scene:** a lived-in office at night (or your setting) — practical desk
lamp, papers, a cold city window. Vertical 9:16 framing built around faces.

### 3 · Atmosphere & quality
Shot on ARRI Alexa with vintage primes, restrained cinematic grade,
shallow focus that isolates faces. **Composed for vertical (9:16):** faces
sit in the upper-middle, eye-lines respected for shot-reverse-shot. Film
grain, motivated practical light, real shadow.

### 4 · Camera rules
**Shot-reverse-shot dialogue grammar:** a clean single on {{a}}, a reverse
single on {{b}}, a tighter push as the tension rises. Vertical framing
keeps each face large.
- *Breathing:* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence." — subtle, keeps the scene
  alive and immediate.
- *Sound:* No score, or a single low tension drone under the turn — not a
  swelling soap-opera string. Production audio: dialogue, room tone, a
  desk-lamp hum, a chair shift. Let silence sharpen the beats.

### 5 · Storyboard (3 beats, ~12s — built to hook + cliffhang)

```
0–2s · Cold open (the hook — survive the swipe)
Action: Straight in, no setup: {{hook}}. The shocking beat lands in the
        first two seconds, before anyone can scroll away.
Camera: A punch-in single on {{a}}, vertical, face large.
Sound:  The sharp diegetic sound of the hook; then dead quiet.

2–8s · Confrontation (shot-reverse-shot)
Action: {{a}}: "{{conflict}}" — cut to {{b}}'s reaction, then back. The
        tension escalates line by line, faces tightening.
Camera: Clean single / reverse single, a slow push on each as it heats up.
Sound:  Dialogue and room tone; maybe one low drone entering.

8–12s · Cliffhanger (the unanswered turn)
Action: {{cliff}} — a reveal or reversal that flips the scene, left
        unresolved.
Camera: Hold on the frozen reaction, push in slightly.
Close:  No resolution, no music sting, no "to be continued" card needed —
        cut on the frozen face mid-reaction. The unanswered question is
        what makes them tap the next episode.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, watermark, text overlay, subtitles, logo, theatrical overacting, exaggerated soap-opera expressions, plastic CG skin, glossy idol render, video-game look, 3D cartoon, flat even studio lighting, horizontal letterboxing, faces too small in frame, distorted face, asymmetric eyes, extra fingers, lip-sync mismatch, melting/morphing geometry, swelling melodramatic score, frame flicker, jarring hard cuts, lifeless locked-off camera
```

---

## Why it's built this way

- **Hook in the first 2 seconds (vertical-first law).** Phone audiences
  decide instantly. Open *on* the shocking beat ({{hook}}) — no setup, no
  slow build — or they swipe. The cold open is the whole game.
- **Vertical framing changes the grammar.** Faces sit large in the
  upper-middle, eye-lines respected so shot-reverse-shot reads in 9:16.
  Horizontal letterboxing or tiny faces kill a micro-drama; negate them.
- **Shot-reverse-shot is the dialogue engine.** Single / reverse single /
  tightening push is how a confrontation reads. Keep it clean and let the
  faces carry it.
- **Restraint + cliffhanger (Rule 6, drama variant).** Grounded acting (a
  tight jaw, not theatrics) makes it land; ending on a frozen, unanswered
  reaction — not a resolution or a music sting — is what drives the binge.

**Usage:** generate the *cold open* (0–2s) first — if the hook lands and the
acting is restrained (not soap-opera), build the confrontation and
cliffhanger around it. Keep faces large; shoot/think 9:16 throughout.
Sanitise any IP-recognisable wording before running.

**Model:** Veo 3 and Sora 2 are strongest for synced dialogue and grounded
faces; Kling 3.0 supports multilingual dialogue. Keep dialogue lines short
so lip-sync holds; cut away on the reverse if a take's sync drifts.
