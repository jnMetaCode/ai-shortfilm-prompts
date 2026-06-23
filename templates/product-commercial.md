# Worked Example — Product Commercial / Hero Ad (beat-driven)

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to a **product commercial** — the genre that most often
> collapses into plastic CG gloss and "floating-in-a-void" render.
> Uses the beat-synced per-second storyboard (Stage 5, Style A).
>
> Concept: a mechanical wristwatch hero ad, macro tactile reveal on a
> sunlit tabletop. Swap the product and you have a generic ad skeleton.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): beat-driven ad-prompt patterns in
> [LichAmnesia/awesome-ad-video-prompts](https://github.com/LichAmnesia/awesome-ad-video-prompts)
> (CC BY 4.0).*
>
> **[中文版 →](./product-commercial.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{product}}` | a mechanical wristwatch | a sneaker / a perfume bottle / a phone |
| `{{material}}` | brushed steel case, sapphire crystal | knit mesh / frosted glass / anodized aluminium |
| `{{hero_action}}` | the crown is wound, the second hand sweeps | laces pull taut / cap lifts and mist curls |
| `{{surface}}` | dark walnut tabletop | wet slate / raw linen / brushed concrete |
| `{{accent_color}}` | warm amber | ice blue / oxblood red / matte black |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`premium product commercial | macro tactile realism | controlled hard key + soft fill | beat-synced reveal | no plastic CG gloss, no floating-in-void render`

### 2 · Character & scene

**Hero subject (the product):** {{product}} — {{material}}.
Material described first, finish second: the steel reads *brushed, not
mirror-polished*; the crystal carries one faint anti-reflective blue
cast. Imperfections (these sell the realism): a hairline micro-scratch
on the left lug catching the key light, a single half-wiped fingerprint
smudge near the crown, the faintest dust on the strap leather. A real
object that has been *touched*, not a showroom render.

**Scene:** a {{surface}} near a window, a low side shaft of light, fine
dust motes drifting through it. Shallow depth — the background falls to
a soft {{accent_color}} bokeh, never a flat seamless sweep.

### 3 · Atmosphere & quality
Shot on ARRI Alexa with a Laowa 24mm probe macro lens (the real
commercial-macro tool — extreme close focus, deep tabletop perspective).
One hard key from window-left, soft bounce fill from camera-right,
controlled falloff into shadow. Restrained teal-and-warm grade, organic
film grain, true specular highlights on metal (not blown-out CG bloom).

### 4 · Camera rules
Edited across 4 short beats (or one continuous probe move if single-shot).
Slow, deliberate probe push-ins and one lateral track across the surface.
- *Breathing:* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence." — keep it micro; a
  product macro wants stability, not sway.
- *Sound:* No score. Production audio only — designed foley: the soft
  click of the crown, a fine metallic tick of the movement, the brush of
  a fingertip on steel, room tone. (If the brand needs a music bed, add
  it deliberately in the edit — don't let the model invent one.)

### 5 · Storyboard (4 beats, ~10s)

```
0–2s · Establish (the object at rest)
Action: {{product}} sits still on the {{surface}}, side light raking low,
        one dust mote crossing the frame.
Camera: Slow probe push-in from a low 20° angle toward the crown.
Detail: The micro-scratch on the lug flares for a frame as the light
        catches it.

2–5s · The touch (human contact, no full reveal of a face)
Action: A hand enters frame; {{hero_action}}.
Camera: Probe tracks the motion laterally, holding focus on the contact
        point.
Sound:  The precise foley of that single action, isolated and crisp.

5–8s · The detail (macro payoff)
Action: Extreme macro on the working part — the sweep of the second hand,
        the grain of the {{material}}, a true specular glint travelling
        across the edge.
Camera: Slow rack focus from foreground texture to the {{accent_color}}
        bokeh behind.

8–10s · Settle (restrained close)
Action: The hand withdraws. {{product}} returns to rest.
Camera: Hold, breath-float, light dimming a touch as a cloud passes.
Close:  No logo slam. No spinning glamour hero-spin. No lens-flare burst.
        Just the object at rest and one last dust mote settling through
        the light.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, soft focus, watermark, text overlay, subtitles, logo, oversaturated colors, plastic skin, glossy CG render, video-game look, 3D cartoon render, flat even studio lighting, perfectly clean flawless surfaces, blown-out highlights, floating product in empty white void, seamless infinity backdrop, frame flicker, ghosting, jarring hard cuts, lifeless locked-off camera, spinning hero rotation, cheesy lens flare
```

---

## Why it's built this way

- **Imperfections sell the product (Rule 5).** A micro-scratch and a
  half-wiped fingerprint read as "real object, real light" — the opposite
  of the lifeless CG render that ad prompts default to. Perfect surfaces
  look fake; the flaw is the realism.
- **Real macro tool, not "cinematic" (Rule 2).** "ARRI + Laowa probe
  macro" anchors the model to actual tabletop commercial footage. "Studio
  product shot, 4K" gives you a stock render.
- **Restrained close (Rule 6).** No logo slam, no hero-spin, no flare.
  The object simply returning to rest is more premium than a reveal
  flourish — and it stops the model piling on cheap ad VFX at the end.
- **Beat-synced storyboard.** Each 2–3s beat = one action + one camera
  move + one sound. This per-beat discipline is what keeps a 10s ad from
  becoming a vague drift.

**Usage:** generate the *Detail* beat (5–8s) first — if the macro texture
and specular highlight read as real there, the rest will hold. Keep the
human contact to hands only (a full face triggers stricter likeness
filters and isn't needed). Stitch the 4 beats in post.

**Model:** Seedance 2.0 and Kling are strong on tactile macro motion;
Veo 3 gives the cleanest specular/lighting realism (use its negative
field with plain noun phrases). On the Doubao app, remember the 5s/10s
preset lock — plan beats around 10s total.
