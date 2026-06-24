# Worked Example — Automotive / Car Commercial

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to a **car commercial** — where reflective surfaces, a moving
> light sweep, and automotive rig camerawork are the craft. Distinct from
> [product-commercial.md](./product-commercial.md) (tabletop macro): here
> the hero is a vehicle in motion.
>
> Concept: a coupe carving a coastal road at dusk, light streaking across
> the bodywork. Swap the car and road, keep the surface/light discipline.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): commercial/product patterns in
> [LichAmnesia/awesome-ad-video-prompts](https://github.com/LichAmnesia/awesome-ad-video-prompts)
> (CC BY 4.0).*
>
> **[中文版 →](./car-commercial.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{car}}` | a low matte-grey coupe | an SUV / a classic roadster / an EV |
| `{{road}}` | a cliff coastal road at dusk | a wet city street / a salt flat / a tunnel |
| `{{surface}}` | matte paint with a soft sheen | glossy black / brushed metal / pearl white |
| `{{light_sweep}}` | a band of warm sun raking along the body | neon reflections / a studio light arc |
| `{{grade}}` | warm dusk gold + cool shadow | high-contrast night / desaturated steel |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`automotive commercial | reflective surfaces in motion | speed and form beauty | a moving light sweep reveal | photoreal, no plastic CG car, no floating-in-void render`

### 2 · Character & scene

**Hero (the car):** {{car}}, {{surface}}. The bodywork is the subject —
its form revealed by how light moves across it. Imperfections that read as
real, not CG: faint road grime and dust on the lower panels, a bead of
water, heat haze off the hood, real tire sidewall flex and tread, true
reflections of {{road}} sliding across the paint.

**Scene:** {{road}}, {{grade}}. A real environment reflected in the
surfaces — never a seamless studio void.

### 3 · Atmosphere & quality
Shot on ARRI Alexa with anamorphic primes, from a camera car / Russian-arm
rig (the real automotive-ad tool). {{grade}}, film grain, true specular
highlights and reflections — the "wet"/metallic look comes from real
environment reflection, not CG bloom.

### 4 · Camera rules
Low tracking shots skimming the bodywork, a rig move that lets
{{light_sweep}} travel along the form, a pass alongside the moving car.
- *Breathing:* keep it minimal — automotive rigs are stabilised; a smooth
  glide, not a handheld float.
- *Sound:* No score. Production audio only — the engine note, tires on
  {{road}}, wind, a turbo or EV whir. (If the brand needs a music bed, add
  it deliberately in the edit — don't let the model invent one.)

### 5 · Storyboard (3 beats, ~10s)

```
0–3s · Surface (the reveal in reflection)
Action: Macro-ish on {{surface}} as {{light_sweep}} travels across it —
        the form reads through moving light and reflection, not a flat lit
        side.
Camera: Slow rig glide along the bodywork.

3–7s · Motion (the car alive on the road)
Action: {{car}} carves through {{road}}, tires gripping, the environment
        streaking in the paint, heat haze off the hood.
Camera: Low tracking pass alongside, the world reflected and rushing.
Sound:  Engine + tires + wind in sync.

7–10s · Hero rest (restrained close)
Action: The car settles to a stop; the last of {{light_sweep}} slides off
        the body.
Camera: Hold, a slow glide to a stop.
Close:  No logo slam, no spinning turntable, no lens-flare burst. Just the
        car at rest and the light leaving the surface.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, watermark, text overlay, subtitles, logo, oversaturated colors, plastic CG car, glossy unreal render, video-game look, 3D cartoon, floating car in white void, seamless studio infinity backdrop, blown-out highlights, flat even lighting, perfectly clean showroom surfaces, warped reflections, melting/morphing bodywork, wrong wheel rotation, frame flicker, ghosting, spinning turntable, cheesy lens flare
```

---

## Why it's built this way

- **Light reveals form (the automotive move).** A car ad isn't a flat-lit
  product shot — the body is revealed by a light sweep travelling across
  reflective surfaces. Build the storyboard around moving light and
  reflection, not a static beauty pose.
- **Real reflections = realism (Rule 5).** Road grime, a water bead, heat
  haze, the environment streaking in the paint. A perfectly clean car in a
  white void is the CG default; the reflections and grime sell it as real.
- **Automotive rig, not "cinematic" (Rule 2).** "ARRI + anamorphic, camera
  car / Russian-arm rig, low tracking" anchors the model to real car
  cinematography. "Car driving, cinematic 4K" gives a game render.
- **Restrained close (Rule 6).** Car at rest, light leaving the body — not
  a logo slam or turntable spin. Premium is quiet.

**Usage:** generate the *motion* beat (3–7s) first — if the reflections,
tire grip and environment streaking read as real there, the surface and
hero beats frame it. Watch for warped reflections and wrong wheel rotation;
negate them.

**Model:** Veo 3 and Sora 2 give the best reflective-surface and motion
realism; Kling is strong on the tracking pass. Watch wheels rotating the
wrong way at speed — keep passes short or add the wheel-direction negative.
