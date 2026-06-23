# Worked Example — Drone / FPV Aerial

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to an **FPV / aerial drone shot** — where the *camera move
> itself* is the content: scale, speed, and one continuous flight.
> Teaches the FPV/aerial vocabulary (dive, fly-through, orbit, reveal)
> and the continuous one-take discipline.
>
> Concept: an FPV drone launches low, dives through a canyon, and pulls
> up to reveal a vista. Swap the location, keep the continuous move.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): aerial/landscape scenes in
> [hr98w/awesome-sora-prompts](https://github.com/hr98w/awesome-sora-prompts)
> (CC0).*
>
> **[中文版 →](./drone-fpv.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{subject}}` | a deep red-rock canyon with a river | a coastal cliff town / a skyscraper canyon / a forest waterfall |
| `{{move}}` | low dive → fly-through the gorge → pull-up reveal | proximity orbit / power-loop / dolly-zoom reveal |
| `{{gap}}` | a narrow slot between rock walls | an arch / a bridge span / a tree line |
| `{{reveal}}` | a vast valley opening at sunrise | a city skyline / the open sea / a mountain range |
| `{{light}}` | low golden sunrise, long shadows, haze | blue hour / harsh midday / storm light |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`FPV drone flight | aerial scale and speed | natural light | one continuous take | photoreal, no game-engine flythrough look`

### 2 · Character & scene

**Subject (the place, traversed):** {{subject}}, under {{light}}. The
scale is the point — the drone's speed and proximity make the size of the
place felt. Real atmosphere makes it photoreal: haze in the distance,
dust or spray kicked up near surfaces, birds, moving water, wind in
vegetation.

**Imperfections (keep it real footage, not a render):** real atmospheric
haze and light scatter, tiny motion judder on the fastest moves, true
surface texture (rock grain, water, foliage) — not a clean CG flythrough.

### 3 · Atmosphere & quality
Shot on an FPV cinewhoop drone with an ultrawide lens (the real FPV look —
fast, immersive, slight wide distortion), or a cinematic aerial drone for
smoother moves. Anamorphic widescreen, {{light}}, fine film grain, true
depth haze for scale.

### 4 · Camera rules
**The move is the whole shot — one continuous take.** FPV vocabulary:
{{move}} — committed, flowing, no cuts. Speed and proximity to surfaces
(through {{gap}}) create the visceral scale.
- *Breathing:* not the usual handheld float here — the drone has its own
  motion. Keep any added float minimal; let the flight path carry it.
- *Sound:* No score. Production / ambient audio only — wind rush, the
  faint rotor hum (or near-silence at altitude), water or wind at the
  surfaces, the air opening up on the reveal.

### 5 · Storyboard (one continuous move, ~10s)

```
0–3s · Launch / low (establish scale low to the ground)
Action: The drone starts low and fast over {{subject}}, close to the
        surface so speed reads.
Camera: FPV, ultrawide, committed forward motion.

3–7s · Through (the visceral middle — proximity)
Action: {{move}} — dive and fly-through {{gap}}, walls/edges rushing past
        close to the lens. This proximity is the thrill.
Camera: Continuous, no cut; slight wide distortion, micro-judder on the
        fastest bit.
Sound:  Wind rush builds.

7–10s · Pull-up reveal (the payoff)
Action: The drone pulls up and out to reveal {{reveal}} — the scale lands
        all at once.
Camera: Smooth climbing reveal, the world opening.
Close:  No title, no logo, no spin-around hero orbit. Just the vista
        holding as the drone settles and the wind opens out.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, watermark, text overlay, subtitles, logo, oversaturated colors, game-engine flythrough, video-game look, plastic CG terrain, 3D render, fake HDR, flat lifeless lighting, warping/melting geometry, rubber-sheet landscape, jarring hard cuts, stutter, frame flicker, ghosting, cheesy lens flare, obvious CG water
```

---

## Why it's built this way

- **The move is the content.** FPV/aerial isn't about a subject doing
  something — it's about the flight: scale, speed, proximity. Build the
  storyboard as one continuous move (launch → through → reveal), not as
  events.
- **FPV tool + vocabulary (Rule 2).** "FPV cinewhoop, ultrawide, dive,
  fly-through" anchors the model to real drone footage. "Aerial shot,
  cinematic" gives a generic stock flyover or a game flythrough.
- **Atmosphere sells the scale and the realism (Rule 5).** Depth haze,
  dust/spray near surfaces, micro-judder on fast moves. A perfectly clean
  flythrough reads as a game engine; the haze and judder read as real
  capture.
- **Restrained close (Rule 6).** Let the reveal hold, no spin-around hero
  orbit or title. The vista is the payoff; don't pile on.

**Usage:** generate the *through* beat (3–7s) first — proximity and speed
are the thrill; if the fly-through reads as real FPV (not a CG flythrough),
the launch and reveal frame it. Keep it one continuous move; cuts kill the
FPV feel.

**Model:** Kling and Seedance handle fast continuous motion well; Veo 3
and Sora 2 give the best photoreal terrain, depth haze and native wind
audio. Watch for "rubber-sheet" warping on fast low passes — negate it and
keep surfaces textured.
