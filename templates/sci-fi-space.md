# Worked Example — Hard Sci-Fi Space / Zero-G

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to **hard sci-fi space** — where weightless physics, vast
> scale, and the *silence of vacuum* are the craft. Teaches zero-G motion,
> the vacuum-sound choice (no external sound in space, only diegetic
> helmet audio), and epic restraint.
>
> Concept: an astronaut on a tether drifting outside a station, Earth
> below. Swap the scenario, keep the physics and the silence.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): space/cinematic scenes in
> [hr98w/awesome-sora-prompts](https://github.com/hr98w/awesome-sora-prompts)
> (CC0).*
>
> **[中文版 →](./sci-fi-space.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{subject}}` | an astronaut on a tether | a docking spacecraft / a derelict station |
| `{{action}}` | drifting, reaching for a handrail | an undock / a slow spin / a spacewalk repair |
| `{{vista}}` | Earth's curve and the terminator line below | a gas giant / an asteroid field / deep starfield |
| `{{wear}}` | scuffed suit, scratched visor reflections | worn hull panels, ice venting, micro-meteor pits |
| `{{light}}` | hard low sun, deep black shadow | planet-reflected glow / cold blue starlight |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`hard sci-fi space | zero-gravity physics | vast scale | controlled vacuum silence | photoreal NASA-footage realism, no game-cutscene look`

### 2 · Character & scene

**Subject:** {{subject}}, {{action}} — in true weightlessness: slow,
floaty, momentum-driven motion, a tether and cables drifting, no "up."
Imperfections that read as real footage: {{wear}}, dust motes, fingerprint
smears on the visor, the suit fabric creased and used. Not a clean render.

**Scene:** {{vista}}, {{light}}. True deep black space, a sharp un-twinkling
starfield, hard sunlight with no atmospheric scatter.

### 3 · Atmosphere & quality
Shot on a simulated IMAX film camera + Panavision lens, anamorphic
widescreen. Photoreal, the look of real orbital footage: extreme contrast
(blinding lit side, pure black shadow), fine grain, true reflections of
{{vista}} curving across the visor.

### 4 · Camera rules
A slow, weightless drift or orbit around {{subject}} — space camera moves
are smooth and momentum-driven, not handheld.
- *Breathing:* not the usual handheld float here — motion is a slow
  weightless drift. Keep any float minimal and floaty, never a jitter.
- *Sound (the vacuum choice):* No score. **No external sound in vacuum** —
  outside the suit it is silent. Diegetic audio only: the muffled breathing
  inside the helmet, a suit-radio crackle, the dull thud of a glove on
  metal *felt* through the suit. Silence is the realism.

### 5 · Storyboard (3 beats, ~10s)

```
0–3s · Drift (establish scale + weightlessness)
Action: {{subject}} drifts slowly against {{vista}}; tether and cables
        float. Tiny, fragile against the scale.
Camera: Slow orbital drift.
Sound:  Only helmet breathing; the vast silence outside.

3–7s · The moment ({{action}})
Action: {{action}} plays out in real weightless physics — slow reach,
        momentum carrying the body, a controlled correction.
Camera: Continue the drift, holding {{subject}} small in frame.
Sound:  Breathing quickens; a radio crackle; a muffled metal thud.

7–10s · Stillness (restrained close)
Action: {{subject}} steadies; {{vista}} turns slowly below.
Camera: Hold, weightless float.
Close:  No explosion, no dramatic music swell, no hero turn-to-camera.
        Just a small figure, the silence, and a planet turning below.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, watermark, text overlay, subtitles, logo, oversaturated colors, twinkling stars, atmospheric haze in space, plastic CG render, video-game cutscene look, 3D cartoon, gravity-bound motion, fast jerky movement, handheld jitter, flat even lighting, melting/morphing geometry, distorted face, frame flicker, ghosting, cheesy lens flare, loud explosions in vacuum
```

---

## Why it's built this way

- **Vacuum is silent (Rule 4, space variant).** The single biggest "tell"
  of real space footage is that there's no sound outside the suit. We give
  only diegetic helmet audio (breathing, radio) and let silence carry the
  scale — instead of the Hollywood "loud explosions in space" default.
- **Weightless physics, not gravity motion.** Slow, floaty, momentum-driven
  movement and drifting tethers. Fast or gravity-bound motion instantly
  reads as a game cutscene; negate it.
- **Scale through smallness + true black (atmosphere).** Keep the figure
  small against the vista, true deep-black space, un-twinkling stars, hard
  unscattered light. "IMAX + Panavision, NASA-footage realism" anchors it;
  "epic space scene, 4K" gives a game render.
- **Restrained close (Rule 6).** A small figure and a turning planet, not
  an explosion or a hero shot. The quiet IS the awe.

**Usage:** generate the *drift* beat first — if the weightlessness and the
true-black/starfield read as real orbital footage, the rest holds. Keep
motion slow; this genre dies on fast or jittery movement.

**Model:** Veo 3 and Sora 2 give the best photoreal space, reflections and
diegetic audio; Kling and Seedance handle the slow motion well. Lean on the
negative field to kill twinkling stars, space-haze and gravity-bound motion.
