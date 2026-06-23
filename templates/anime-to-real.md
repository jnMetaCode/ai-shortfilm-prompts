# Worked Example — Anime / 2D → Live-Action Real

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to the **"anime character as live-action"** translation — a
> hugely searched genre that fails in two opposite ways: cheap cosplay, or
> plastic CG. The trick is translating the *medium* (cel shading → real
> materials + physics) while preserving the *silhouette* that makes the
> character readable. This template leans hardest on Rule 7 — the
> recognisable trait-bundle is exactly what IP filters catch.
>
> Concept: a stylised "wind swordsman" concept rendered as a real person
> in a real world. Describe traits, never an IP name.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): style-transfer / anime categories in
> [zhangchenchen/awesome_sora2_prompt](https://github.com/zhangchenchen/awesome_sora2_prompt)
> (MIT).*
>
> **[中文版 →](./anime-to-real.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{silhouette}}` | tall, lean, long coat, single shoulder guard | the readable shape that IDs the character |
| `{{signature}}` | a streak of pale-blue hair, a chipped jade pendant | the 2–3 traits that say "it's them" — no IP name |
| `{{palette}}` | indigo + worn steel + pale blue | the character's colour identity |
| `{{world}}` | a rain-wet stone bridge at dusk | the scene translated to a real location |
| `{{prop}}` | a worn, real-steel curved blade | the iconic item, made physical |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`anime character reimagined as live-action | photoreal materials and physics | preserved silhouette + signature traits | cinematic grade | no cosplay cheapness, no CG plastic, no cel shading`

### 2 · Character & scene

**Character (translate the medium, keep the silhouette):** a real human
with the readable {{silhouette}} and {{signature}} that identify the
character — but rendered fully real: **real skin with pores and faint
texture, real hair (individual strands, not a helmet), real woven fabric
with weight and wrinkles, {{prop}} as actual worn metal.** Drop every 2D
cue — no cel shading, no flat anime eyes, no impossible hair gravity.
Eyes and proportions human, not enlarged.

**Imperfections (this is what separates "real" from "cosplay"):** skin
sheen and stray flyaway hairs, fabric creased and a little worn, a real
scuff on the {{prop}}, faint sweat. Cosplay looks new and posed; real
looks lived-in.

**Scene:** {{world}}, {{palette}} carried into the real lighting.

### 3 · Atmosphere & quality
Shot on ARRI Alexa with vintage primes, cinematic grade in {{palette}}.
Real-world physics on everything — cloth swings and settles with weight,
hair moves with air, light wraps real skin. Filmic grain. The goal is
"a still from a live-action film adaptation," not a render or a con photo.

### 4 · Camera rules
A slow, deliberate reveal — push or arc that lets the real materials read.
- *Breathing:* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence."
- *Sound:* No score. Production audio only — rain on stone, fabric shift,
  the scrape of {{prop}}, ambient world tone.

### 5 · Storyboard (3 beats, ~10s)

```
0–3s · Detail (sell the realism in close-up)
Action: Macro on real skin / a flyaway hair / the woven fabric / the
        scuffed {{prop}} — the textures that say "this is real."
Camera: Slow push on the detail, shallow focus.

3–7s · The silhouette (now we recognise them)
Action: Pull to reveal the full {{silhouette}} in {{world}} — the shape
        and {{signature}} make the character readable, but every surface
        is real.
Camera: Slow arc, breath-float, rain and air moving cloth and hair.

7–10s · A held look (restrained close)
Action: A small, human expression — a breath, a glance, no anime pose.
Close:  No power-up glow, no logo, no flashy hero stance. Just a real
        person who happens to be that character, standing in real rain.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
cel shading, anime shading, flat 2D look, cartoon, enlarged anime eyes, impossible hair gravity, plastic CG skin, doll-like face, cosplay wig look, cheap costume, brand-new unworn fabric, oversaturated colors, glossy render, video-game look, watermark, text overlay, logo, distorted face, extra fingers, melting/morphing geometry, frame flicker, jarring hard cuts, lifeless locked-off camera
```

---

## Why it's built this way

- **Translate the medium, keep the silhouette.** The character reads
  because of *shape + 2–3 signature traits*, not because of cel shading.
  Swap every 2D cue for a real-material equivalent (cel → skin pores,
  flat hair → strands, anime eyes → human eyes) and keep the silhouette —
  that's the whole craft of "2D → real."
- **Imperfection is the cosplay/real divide (Rule 5).** New, clean,
  posed = cosplay. Worn fabric, scuffed prop, flyaway hair, real skin =
  live-action film. The wear is what sells it.
- **Heavy on Rule 7 — describe traits, never the IP.** A recognisable
  trait-bundle (the name, the exact iconic outfit) is exactly what Sora's
  lookalike filter and Seedance's IP filter catch. Use {{silhouette}} +
  {{signature}} as *descriptions*, not the character's name.
- **Restrained close (Rule 6).** A human breath, not a power-up pose.
  Keeps it grounded as "film adaptation," not fan-art animation.

**Usage:** generate the *detail* beat (0–3s) first — if the skin, hair and
fabric read as genuinely real there, the full reveal will hold. If it comes
out plasticky or cel-shaded, push the negative field hard. **Sanitise any
IP-recognisable wording** before running on Seedance/Sora.

**Model:** Veo 3 and Sora 2 give the best photoreal skin/material
translation; both have strict lookalike filters, so keep it trait-described,
not named. Kling and Seedance also work — Seedance especially will reject a
named IP outright, so describe only.
