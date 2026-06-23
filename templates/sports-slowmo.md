# Worked Example — High-Speed Slow-Motion Sports

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to **high-speed slow-motion sports** — where a real
> high-speed camera (Phantom-class) and the *decisive moment* are the
> whole craft. Teaches the high-frame-rate anchor and physical-effort
> detail (sweat, strain, impact) that separate visceral slow-mo from a
> game-engine replay.
>
> Concept: a sprinter exploding off the blocks, the decisive push frozen
> in extreme slow motion. Swap the sport, keep the discipline.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): cinematic/sports motion notes in
> [geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts)
> (MIT).*
>
> **[中文版 →](./sports-slowmo.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{athlete}}` | a sprinter at the blocks | a boxer / a swimmer / a skateboarder |
| `{{moment}}` | the explosive first push off the blocks | the punch landing / the dive entry / the board flip |
| `{{detail}}` | sweat flicking off the brow, muscles taut | water sheeting off / chalk dust bursting |
| `{{venue}}` | a stadium track at dusk under floodlights | a gym / a pool / a street spot |
| `{{palette}}` | cool floodlight white + warm skin | high-contrast B&W / saturated arena |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`high-speed slow-motion sports | decisive-moment detail | natural venue light | visceral physical effort | photoreal, no game-engine replay look`

### 2 · Character & scene

**Athlete:** {{athlete}}. Reference uploaded photo, features 100%
preserved, no beautification. The realism is in the effort: strained
face, gritted teeth, muscles taut and trembling, veins raised, {{detail}},
scuffed and worn gear, dirt or chalk. Not a clean hero pose — a body at
its physical limit.

**Scene:** {{venue}}, {{palette}}. Atmosphere in the air — dust, breath
vapour, spray — made visible by the slow motion.

### 3 · Atmosphere & quality
Shot on a Phantom high-speed cinema camera at ~1000fps (the real slow-mo
tool), played back in extreme slow motion. Cinematic {{palette}} grade,
shallow focus, fine film grain. Every micro-detail readable: a single
sweat droplet, fabric rippling, the ground flexing under force.

### 4 · Camera rules
A locked or smoothly tracking shot that follows {{moment}} — high-speed
rigs are stabilised, not handheld.
- *Breathing:* keep it minimal here — a high-speed shot rides a rig;
  at most an imperceptible drift, not the usual handheld float.
- *Sound:* No score. Production audio only — the impact, the explosive
  breath, the scrape/splash of {{moment}}, a low crowd hum, then the
  stretched, time-warped audio of the slow section.

### 5 · Storyboard (3 beats, ~10s)

```
0–2s · Coiled (real-time, tension)
Action: {{athlete}} set, still, breathing hard, every muscle loaded.
Camera: Slow push toward the point of action.
Sound:  Breath, a tightening crowd hum.

2–7s · The decisive moment (extreme slow motion — the payoff)
Action: {{moment}} detonates — but in extreme slow-mo: {{detail}} hangs
        in the air, fabric ripples, the body's full force reads frame by
        frame.
Camera: Track the motion, locked focus on the detail.
Sound:  Time-stretched impact + breath; everything stretched and heavy.

7–10s · Release (ease out)
Action: The motion completes; a last sweat droplet falls.
Camera: Hold, settle toward real-time.
Close:  No victory roar, no flexing hero pose, no flare. Just the body
        spent and the last droplet hitting the ground.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, watermark, text overlay, subtitles, logo, oversaturated colors, plastic CG skin, video-game replay look, game-engine render, 3D cartoon, motion interpolation artifacts, stutter, smooth-but-fake slow motion, flat even studio lighting, perfectly clean flawless gear, distorted face, extra fingers, melting/morphing geometry, frame flicker, ghosting, lifeless locked-off camera, cheesy lens flare
```

---

## Why it's built this way

- **High-fps tool, not "slow motion" (Rule 2).** "Phantom high-speed
  camera at 1000fps" anchors the model to real high-speed cinematography.
  "Slow-mo, cinematic" gives you a stuttery interpolated fake.
- **Effort detail = realism (Rule 5).** Strained face, taut muscles,
  sweat, worn gear. A clean hero pose reads as CG; the strain and the
  flying sweat are what make it visceral.
- **The decisive moment is the whole shot.** Build (real-time) → the one
  moment in extreme slow-mo → ease out. Don't slow-mo everything; the
  contrast is what gives the payoff its weight.
- **Restrained close (Rule 6).** Spent body + a falling droplet, not a
  victory roar. Keeps it real and stops the model adding triumph VFX.

**Usage:** generate the *decisive moment* beat (2–7s) first — if the
slow-motion reads as real high-speed footage (not interpolated mush) and
the sweat/effort detail lands, build around it. Watch for fake
interpolation artifacts; negate them.

**Model:** Kling and Seedance handle motion realism well; Veo 3 gives the
cleanest high-detail slow-mo and native impact audio. Avoid models'
default "smooth interpolation" — lean on the negative field to keep it
looking like true high-speed capture.
