# Worked Example — Cinematic Teaser Trailer (escalating multi-shot)

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to a **teaser trailer** — an escalating multi-shot montage
> that has to imply a whole world in ~15s. Builds on
> [multi-shot-narrative.md](./multi-shot-narrative.md) and the Epic block
> of [genre-camera-sop.md](./genre-camera-sop.md). Teaches the one thing
> trailers live on: **designed sound + escalating rhythm**.
>
> Concept: a sci-fi thriller teaser — quiet establishing, an inciting
> beat, escalation cuts, a smash to black, one title beat. Swap the world,
> keep the rhythm.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): cinematic/marketing trailer categories in
> [snubroot/Veo-3-Prompting-Guide](https://github.com/snubroot/Veo-3-Prompting-Guide)
> (structure only) and [zhangchenchen/awesome_sora2_prompt](https://github.com/zhangchenchen/awesome_sora2_prompt)
> (MIT).*
>
> **[中文版 →](./movie-trailer.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{world}}` | a drowned near-future coastal city | a frozen frontier colony / a war-torn capital |
| `{{protagonist}}` | a lone diver-engineer | a tired detective / a child with a strange device |
| `{{threat}}` | something vast moving under the water | a spreading blackout / an approaching storm wall |
| `{{title_word}}` | one-word made-up title, e.g. "TIDEBREAK" | your project's title |
| `{{grade}}` | desaturated steel-blue | amber dust / sickly green |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`cinematic teaser trailer | escalating multi-shot montage | one locked filmic grade | sound-design driven | restrained reveal, no cheesy voiceover, no rapid strobe cuts`

### 2 · Character & scene

**Protagonist:** {{protagonist}}. Reference uploaded photo, features
100% preserved, no beautification. Imperfections: rain/sweat on the face,
a scar or tired eyes, worn practical gear (not a clean costume). Appears
in only 2–3 shots — a teaser implies, it doesn't explain.

**World ({{world}}):** the real subject. Built from texture, not
exposition — wet concrete, flickering signage, debris, weather. {{threat}}
is felt, never fully shown.

### 3 · Atmosphere & quality
Shot on simulated IMAX film camera + Panavision C-series (35mm, f/4) for
the wide world beats; Sony Venice + Canon K-35 for the close character
beats. **Lock ONE grade across every shot: {{grade}}, low contrast,
organic film grain.** A trailer that changes look per cut falls apart —
the grade is the glue.

### 4 · Camera rules
Edited multi-shot, **escalating rhythm**: long holds early, cuts get
shorter as tension rises, then one held beat of stillness before the end.
- *Breathing:* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence."
- *Sound (designed, not a song):* No fabricated pop track. Production
  audio + deliberate trailer sound design — low sub-bass rises under the
  escalation, one hard impact ("braam") on a key cut, then a beat of near
  silence before the title. Enumerate the sound per beat; do NOT let the
  model invent a generic music bed.

### 5 · Storyboard (6 shots, ~15s)

```
Shot 1 — Establish (long hold, quiet)
  Wide of {{world}}, {{grade}} grade, slow push. Almost still. Faint
  ambient only. The calm before.

Shot 2 — The protagonist (close)
  Tight on {{protagonist}}'s face, a flicker of unease. A distant low
  sound begins under the frame.

Shot 3 — The inciting beat (the first sign of {{threat}})
  Medium shot — something is wrong: water shifts, a light dies, a sensor
  spikes. The sub-bass rise starts.

Shot 4–5 — Escalation (cuts shorten)
  A rapid pair of beats: motion, reaction, a glimpse (never the full
  reveal) of {{threat}}. Camera more active. Rise climbs.

Shot 6 — Smash to black + title
  One hard impact on the final motion, cut to black. A beat of silence.
  The single word {{title_word}} fades up, then out.
  Close: No hero one-liner, no voiceover, no explosion montage. Just the
  cut to black, one last sound, the title.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, soft focus, watermark, text overlay, subtitles, logo, distorted face, asymmetric eyes, extra fingers, deformed hands, melting/morphing geometry, oversaturated colors, plastic skin, glossy CG render, video-game look, 3D cartoon render, flat even studio lighting, grade shifting between shots, rapid epileptic strobe cuts, cheesy lens flare, frame flicker, ghosting, lifeless locked-off camera, generic stock music feel
```

---

## Why it's built this way

- **One grade is the glue (Rule 1 applied to editing).** The #1 way a
  multi-shot trailer breaks is a different look per cut. Lock {{grade}}
  across all 6 shots; let rhythm and sound carry the escalation instead.
- **Sound design is described per beat (Rule 4, trailer variant).** A
  trailer is half sound. We don't say "production audio only" and stop —
  we script the rise, the impact, and the silence-before-title, so the
  model doesn't paste a generic music bed.
- **Imply, don't explain (Rule 6).** Show {{threat}} in glimpses, never
  the full reveal; protagonist in 2–3 shots. End on a cut to black + one
  word, not a hero line. Restraint is what makes a teaser tease.
- **Escalating cut rhythm.** Long holds → shortening cuts → one still
  beat. This rhythm, not flashy VFX, is what reads as "trailer."

**Usage:** generate Shot 1 (establish) and Shot 6 (title beat) first to
lock the grade and the ending; build the escalation between them. Keep
the whole thing ≤6 shots — teasers fail when they over-explain. Stitch in
post and do the sound design on the timeline.

**Model:** Veo 3 and Sora 2 give the strongest world-coherence and native
sound for the wide beats; Kling is excellent for the action escalation
cuts. Keep each shot ≤8s. On the Doubao app, plan around the 5s/10s
preset lock per shot.
