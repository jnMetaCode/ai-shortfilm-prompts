# Worked Example — Food ASMR / Sensory Close-up

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to **food ASMR** — the genre where *native synced audio*
> is the entire point, not an afterthought. This is the template that
> best exercises the modern engines' native audio-video sync (Seedance
> 2.0, Veo 3, Sora 2).
>
> Concept: cutting into a just-seared steak, extreme macro, crisp synced
> foley. Swap the dish and you have a reusable food-ASMR skeleton.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): ASMR / food prompt patterns in
> [songguoxs/awesome-video-prompts](https://github.com/songguoxs/awesome-video-prompts)
> and the audio-sync chapter of
> [geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts)
> (MIT).*
>
> **[中文版 →](./food-asmr.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{dish}}` | a thick just-seared steak | a ripe kiwi / a glazed croissant / a bowl of ramen |
| `{{tool}}` | a heavy chef's knife | fingers / a spoon / chopsticks |
| `{{key_sound}}` | crust crackle + knife slice | juice burst / flaky shatter / broth slurp |
| `{{texture}}` | charred crust, pink centre, juice | fuzzy skin → wet green / golden layers |
| `{{ambient}}` | a quiet kitchen, faint sizzle | birdsong / rain on a window / café murmur |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`food ASMR | extreme macro sensory close-up | natural window light | crisp synced foley | appetising realism, no oversaturated food-porn`

### 2 · Character & scene

**Hero subject (the food):** {{dish}}. Texture described concretely:
{{texture}}. Imperfections that read as *real, not food-styled*: the
sear is uneven, one edge torn, a little juice already pooling on the
board, a stray crumb out of place, steam rising unevenly. Not a
glossy magazine plate — food that was actually just cooked.

**Scene:** a worn wooden cutting board, a {{ambient}} behind it, a low
side shaft of window light catching the steam. Shallow depth, the
background a soft warm blur.

### 3 · Atmosphere & quality
Shot on ARRI Alexa with a 100mm macro lens (or a Laowa probe macro for
the extreme close work). Warm natural window light from the side, gentle
specular sheen on the wet/juicy surfaces, true-to-life colour — *not*
the oversaturated orange "food-porn" grade. Organic film grain, shallow
focus that melts the background.

### 4 · Camera rules
Edited across short macro beats (or one continuous probe move).
Slow push-ins onto the point of contact; one slow rack focus.
- *Breathing:* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence."
- *Sound (this is the star — enumerate everything):* No score.
  Production / synced audio only — {{key_sound}}, the precise contact of
  {{tool}} on {{dish}}, the wet separation as it parts, faint background
  {{ambient}}, room tone. Every sound must lock to the matching frame;
  this is an audio-led piece, so describe the soundscape in as much
  detail as the visuals.

### 5 · Storyboard (4–5 beats, ~10s)

```
0–2s · Anticipation
Action: {{dish}} rests on the board, steam curling up through the side
        light. Nothing moves yet.
Camera: Slow probe push-in toward the surface.
Sound:  Faint sizzle / {{ambient}}, room tone. Quiet before contact.

2–4s · Contact
Action: {{tool}} touches the surface — the first press, before it gives.
Camera: Hold on the contact point, focus razor-thin.
Sound:  The crisp first sound of {{key_sound}} — isolated, loud, clean.

4–7s · The cut / the give
Action: {{tool}} parts {{dish}} — {{texture}} revealed, juice/interior
        exposed, surfaces separating.
Camera: Macro follows the parting line; slow rack to the wet interior.
Sound:  The full {{key_sound}} in sync — the satisfying core of the clip.

7–10s · Settle
Action: A piece lifts away; a last drop of juice falls and settles on
        the board.
Camera: Hold, breath-float.
Close:  No dramatic plating flourish, no chef-hands presentation, no
        sparkle. Just the last drop settling and the steam thinning out.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, soft focus, watermark, text overlay, subtitles, logo, oversaturated colors, neon food coloring, plastic food, glossy CG render, video-game look, 3D cartoon render, flat even studio lighting, perfectly clean styled magazine plate, melting/morphing geometry, extra fingers, deformed hands, frame flicker, ghosting, jarring hard cuts, lifeless locked-off camera, silent footage, audio out of sync
```

---

## Why it's built this way

- **Sound is described as carefully as the image (Rule 4, amplified).**
  ASMR lives or dies on synced foley. We don't write "production audio
  only" and move on — we enumerate every sound and lock it to its frame.
  This is the one genre where the audio block is longer than the visual.
- **Real-food imperfections (Rule 5).** Uneven sear, a torn edge, a stray
  crumb, pooling juice. Styled-perfect food reads as plastic CG; the
  flaws are what make it appetising and real.
- **True colour, not food-porn grade (Rule 1).** "Oversaturated orange,
  glossy" is the vague-praise trap of food video. Concrete texture words
  ("charred crust, pink centre, wet sheen") beat saturation cranking.
- **Restrained close (Rule 6).** The last drop settling, not a plating
  reveal. Stops the model from tacking on a glossy hero-plate flourish.

**Usage:** generate the *cut / give* beat (4–7s) first — that is the
payoff; if the texture-reveal and the synced sound land there, build the
rest around it. This genre rewards engines with strong native audio.

**Model:** Seedance 2.0's native synced audio is its standout strength —
this is the genre to use it on. Veo 3 also does excellent native audio
(describe the soundscape in the prompt; use the negative field for
artifacts). Kling 3.0 handles the motion well but verify audio sync. On
the Doubao app, plan for the 5s/10s preset lock.
