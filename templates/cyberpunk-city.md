# Worked Example — Cyberpunk City Roam (atmospheric, environment-led)

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to an **atmospheric environment piece** where the *city* is
> the subject, not a character. Completes the cyber set alongside
> [cyber-wuxia](../prompts/cyber-wuxia.md). Teaches the gritty-cyber
> camera combo (Sony Venice + Canon K-35) and "active environment =
> atmosphere."
>
> Concept: a slow night roam through a rain-soaked neon megacity, one
> lone figure dissolving into the crowd. Swap the city's flavour, keep
> the atmosphere discipline.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): cyberpunk/cinematic-city scenes surveyed in
> [hr98w/awesome-sora-prompts](https://github.com/hr98w/awesome-sora-prompts)
> (CC0) and [geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts)
> (MIT).*
>
> **[中文版 →](./cyberpunk-city.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{city_flavour}}` | dense East-Asian neon street market | brutalist corporate canyon / flooded back-alleys |
| `{{weather}}` | steady cold rain, volumetric haze | drifting acid fog / falling ash |
| `{{neon_palette}}` | magenta + cyan over teal base | sodium-orange + green / cold blue + red |
| `{{figure}}` | a lone hooded figure | a courier on a bike / no figure at all |
| `{{move}}` | slow forward dolly down the street | a descending drone / a static long hold |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`neon cyberpunk metropolis | rain-soaked night roam | volumetric haze | low-saturation teal base + neon accents | atmospheric realism, no game-CG city, no clean render`

### 2 · Character & scene

**Subject (the city itself):** {{city_flavour}} at night, {{weather}}.
The environment is *active*, which is what makes it atmosphere and not a
matte painting: rain falling and pooling, steam from vents, a {{neon_palette}}
sign flickering with one dead tube, reflections rippling in puddles,
people passing as soft silhouettes. Grime, wear, wet surfaces everywhere
— imperfection is the realism.

**Figure (optional, secondary):** {{figure}}, small in the frame, never
the focus — it gives the city scale, then disappears into it.

### 3 · Atmosphere & quality
Shot on Sony Venice + Canon K-35 series (the gritty hard-sci-fi combo),
anamorphic widescreen, horizontal lens flares from the neon. Low-saturation
teal base with {{neon_palette}} accents punching through the haze.
Volumetric light shafts, organic film grain, true reflective highlights
on wet ground (not blown-out CG bloom).

### 4 · Camera rules
{{move}} — slow and deliberate; the city should drift past, not race.
- *Breathing:* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence."
- *Sound:* No score. Production / ambient audio only — steady rain,
  distant traffic and sirens, the electric buzz of neon, fragments of
  crowd chatter, a low city hum. A synth drone is allowed only as faint
  ambient texture, not a music track.

### 5 · Storyboard (per-second, ~10s single roam)

```
0–3s · Enter
Action: The roam begins — {{move}} into the {{city_flavour}}, rain
        streaking the frame, neon smearing in the wet lens.
Camera: Slow, low. Reflections lead the eye down the street.
Sound:  Rain + distant traffic establish; neon buzz close.

3–7s · Through
Action: Pass the flickering {{neon_palette}} sign (one dead tube),
        steam crossing the frame, {{figure}} passing as a silhouette.
Camera: Hold the drift; a puddle reflection ripples as something passes.
Detail: Grime and wear catch the light — the lived-in texture.

7–10s · Dissolve
Action: {{figure}} merges into the moving crowd and is gone; the street
        continues without them.
Camera: Keep drifting, breath-float, do not stop on the figure.
Close:  No reveal, no hero turn, no title. Just the sign flickering once
        more and the rain continuing down the empty-feeling street.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, soft focus, watermark, text overlay, subtitles, logo, oversaturated colors, plastic skin, glossy CG render, video-game look, clean render, 3D cartoon render, flat even studio lighting, perfectly clean dry surfaces, dead static matte-painting city, blown-out neon bloom, melting/morphing geometry, warped signage text, frame flicker, ghosting, jarring hard cuts, lifeless locked-off camera, cheesy lens flare
```

---

## Why it's built this way

- **Active environment = atmosphere (Stage 2 discipline).** A static city
  reads as a matte painting. Rain pooling, steam, a flickering dead tube,
  rippling reflections, passing silhouettes — motion in the environment is
  what makes it feel real and inhabited.
- **The gritty-cyber camera combo (Rule 2).** "Sony Venice + Canon K-35"
  anchors the model to hard-sci-fi cinematography. "Cyberpunk city, neon,
  4K" gives you a game cutscene instead.
- **Imperfection as realism (Rule 5).** Grime, wear, wet surfaces, a dead
  neon tube. Clean = CG. The wear is the point.
- **The figure dissolves (Rule 6).** No hero reveal, no title card. Letting
  the figure vanish into the crowd keeps it atmospheric and stops the model
  turning it into a character beat.

**Usage:** generate the *3–7s "through"* beat first — if the wet
reflections, neon smear and haze read as real there, the rest holds.
Keep it one slow continuous move; this genre dies when the camera races.

**Model:** Kling and Seedance 2.0 handle wet-neon motion and reflections
well; Veo 3 gives the cleanest volumetric light and native ambient sound.
Watch for warped on-screen sign text — put "warped signage text" in the
negative field, or keep signs abstract/non-textual.
