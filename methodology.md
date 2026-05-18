# The Mx-Shell Prompt Methodology

> This document decomposes the 5-stage prompt structure Mx-Shell used
> repeatedly across *Zombie Scavenger*, the *Kamen Rider* transformation
> series, and others.
>
> Not a copy-paste cookbook — a system you can adapt to your own ideas.
>
> **[中文版 →](./methodology.zh.md)**

---

## One-sentence summary

**Write prompts the way a director writes a shot list, not the way a
copywriter writes a description.** Slice the scene by time, and for
each slice specify exactly four things: action / camera / VFX / sound.

---

## The 5-stage structure

All of Mx-Shell's video prompts follow this order. Don't shuffle it:

```
1. Core theme          ← Tone-setter (one line of tags)
2. Character & scene   ← Who is in it, wearing what
3. Atmosphere & look   ← How it looks
4. Camera rules        ← How the camera moves
5. Storyboard          ← Per-second OR per-shot breakdown
```

### Stage 1 · Core theme

A single line of style tags separated by `|` or `丨`. Gives the AI an
overall aesthetic anchor.

**How to write it:** 3–6 tags, ramping from "what kind of shot" to
"genre" to "aesthetic reference."

```
Core theme: gritty dark tokusatsu | broken flesh | combat-damaged transformation | post-apocalyptic battlefield
Core theme: atom-punk | post-apocalyptic zombies | cinematic | hyperreal | no game-CG feel
Core theme: realistic sci-fi | heavy mecha | epic | heavy-industry mechanical aesthetic | live-action performance
```

**Useful tag vocabulary** (mix and match):

| Type | Examples |
|---|---|
| Realism anchors | cinematic, hyperreal, live-action, no game-CG feel, anamorphic widescreen cinematic |
| Aesthetic schools | gritty dark, atom-punk, steampunk, cyberpunk, wasteland industrial, retro Hong Kong noir |
| Genres | tokusatsu, post-apocalyptic survival, lone-hero, mecha wuxia, heavy mecha |
| Emotional tone | broken flesh, combat-damaged transformation, somber, epic, oppressive |

---

### Stage 2 · Character & scene

Answers *"who is in the frame, what are they wearing, where do they
stand."* Three lines: **Face / Clothing / Scene**.

```
[Character setup]
Face:    Reference uploaded photo. Features, face shape, hairstyle 100% preserved.
         No beautification. Maintain facial wound, gauze, bloodstain.
         Hair covers forehead, expression somber throughout. At the moment
         of transformation, only a slight furrow of the brow — no heroic
         spark, no eye-light, keep the oppressive feel.
Clothing: Matte black leather trench coat, matte metal belt, dark red
          crystal at the buckle core.
Scene:    Post-apocalyptic battlefield, light breeze, smoke drifting,
          overcast wasteland, grey-blue sky. A meteor trailing fire
          and smoke crosses the sky.
```

**Counter-intuitive but Mx-Shell-emphasized points:**

- **"No beautification."** Realism comes from imperfections. Writing
  *"preserve minor facial blemishes"* explicitly is more effective than
  vaguely asking for "high quality."
- **"Reference uploaded photo, 100% preserve features"** — if you used a
  reference image, lock it down. Otherwise the AI will drift.
- **Clothing has texture.** *"Matte black leather"* has 3x the
  information of *"black leather jacket."*
- **Scene has motion.** Wind, smoke, meteor. A static background can't
  carry atmosphere.

---

### Stage 3 · Atmosphere & look

The **camera-emulation trick** Mx-Shell uses everywhere.

```
[Atmosphere & quality]
Visual base: Anamorphic widescreen cinematic. Simulated IMAX film
             camera, paired with Panavision C-series lens (35mm focal,
             f/4 aperture).
Color & tone: Low-saturation grey-blue dominant. Shadow info compressed
              but detail preserved. Subtle edge bloom, moderate film
              grain.
Style core:  Reference [aesthetic]. Emphasis on the fusion of biological
             texture and alien tech. Build an oppressive, heavy, live-
             action sensation of physical pain.
Sound: No score. Production audio only.
```

**Why it works:** AI training data binds huge amounts of real movie
imagery to specific camera-and-lens metadata. Giving the AI a real
camera model = giving it a concrete visual anchor — orders of magnitude
more effective than "cinematic feel."

**Mx-Shell's go-to combinations:**

| Aesthetic | Camera + lens |
|---|---|
| Epic / big scenes | **IMAX film camera + Panavision C-series** (35mm, f/4) |
| Gritty cyber / hard sci-fi | **Sony Venice + Canon K-35 series** |
| Hong Kong noir / wuxia | **Kodak 35mm vintage film, bleach-bypass** |
| Commercial portrait | **Canon EF 85mm f/1.2** |

**Common color phrases:** low-saturation grey-blue / Hollywood teal-and-orange / 60s retro warm-orange + sea-salt blue / dark-low-light high-contrast.

---

### Stage 4 · Camera rules

How the camera moves. Three lines: **single-shot / angle / breathing**.

```
[Camera rules]
Single-shot: One continuous take, no editing.
Angle: Open on a low-angle shot, character at 30° from the left, framed
       waist-up. As the transformation begins the camera orbits very
       slowly to a level head-on at the upper body. After transformation
       completes, orbit to the right side and shift to a high angle.
Breathing: Handheld shot. Throughout, maintain an *extremely subtle,
           breath-like camera float* to enhance presence.
```

**Vocabulary to pull from:**

- **Shot size**: extreme close-up / close-up / medium close-up / medium / wide / extreme wide
- **Angle**: low-angle / high-angle / eye-level / over-the-shoulder / vertical bird's-eye
- **Motion**: very slow push-in / orbit / handheld follow / locked-off / FPV / pull-out + drop + tilt-up
- **Rhythm**: very slow / steady / sudden / 0.1-second reactive micro-shake / extreme slow motion

**The "breathing" line** — Mx-Shell adds it to almost every prompt.
Reason: it forces the AI to add subtle handheld float, avoiding the
artificially-static CG-look default.

---

### Stage 5 · Storyboard (per-second OR per-shot)

The most critical — and most often missed — part of the whole system.

**Two writing styles, pick one based on the scene:**

#### Style A: per-second slices (single-shot, one-take)

Best for transformations, weapon-charge sequences, anything one-take.

```
0–3s · Gaze
Action: Subject slightly bows head, eyes locked on the belt. Back tense.
        Right hand slowly rises, grips the belt body.
Camera: Extremely slow push-in. Capture the subtle rise/fall of breath.
VFX:    Both eyes suddenly ignite with a platinum glow. Eye sockets
        crack around the rim. The glare creates lens flares.

3–6s · Activation
Sound:  Whispered "HENSHIN"
Action: As the word fades, the palm presses hard against the belt core.
        The crystal core is compressed and cracks; red light follows
        the fractures. The hand slowly releases after activation.
VFX:    The metal mechanism is violently awakened. The core splits down
        the centerline. Air collapses inward, creating distortion;
        screen edges stretch slightly. A horizontal pulse wave radiates
        outward in a spiral, dissipating after 0.3s.
Camera: Low-frequency hum approaches from a distance. The camera produces
        a reactive 0.1s micro-tremor.

6–9s · Tearing
[Then subcategorize: core / body / coat / shell / face / camera]
```

**Three-part formula per segment**: Action + Camera + VFX. Optional add-ons: Sound, Face/Expression.

#### Style B: per-shot slices (multi-shot edited)

Best for narrative shorts like *Zombie Scavenger*.

```
Shot 1:
Shot size:   Medium. Frame the robot from the waist up.
Composition: Robot's back centered as foreground.
             Background-left: floor-to-ceiling window.
             Background-right: bar counter.
Camera move: Follow-tracking shot.
Action:      Robot dances his way into the lounge area with his back
             to the camera. He spins to face camera as the dance's
             END pose. The LED face holds the green smiley pixel
             expression. Off-screen, a glass bottle shatters. The
             robot startles, takes a half-step back-and-left, hunches
             slightly. LED face switches instantly to the yellow
             frightened expression, gaze flicks to the right.

Shot 2:
Shot size:   Wide. Level pan of the entire bar counter.
Composition: Empty shot. Bar counter occupies the lower third; back
             wall of liquor shelves above.
Camera move: Slow push-in to build atmosphere.
Action:      A rustling noise comes from behind the counter — something
             is rummaging beneath it.
```

**Four-part formula per shot**: Shot size + Composition + Camera move + Action.

---

## Three counter-intuitive principles

### 1. Don't give the AI reference images unless the image quality is high

> "All my Kamen Rider armor designs came from text descriptions —
> letting the AI free-form."

The worst side effect of reference images: AI mimics the *art style*
of the reference (including CG look, anime look), not the *design*.
Exceptions: photoreal 3D renders or true high-detail live-action photos.

### 2. Describing flaws = describing reality

> "Too perfect = fake. Keeping imperfections is not a bad thing."

`Battle damage everywhere` / `paint worn off` / `oil in the joints`
/ `preserve minor facial blemishes` / `armor never perfectly flat` —
these "flaws" are the core source of Mx-Shell's signature texture.

### 3. Rerolls are normal. Leave the ending empty.

Across the film, 200+ video generations produced ~40 final clips.
Each shot averaged 5–10 rerolls; some 20+. **Don't aim for first-try
perfection.**

And don't pile on FX at the end:

> "No dialogue. No explosion. No blinding light. Just a figure
> standing in the smoke, a meteor crossing the distant sky."

Restraint reads more elevated than excess.

---

## After you finish writing

- Use **Seedance 2.0** (not the Fast variant).
- If the prompt exceeds the character limit, switch to the web client.
- IP names (real brands, real character names) get blocked — substitute
  with style descriptions.
- Full FAQ: [faq.md](./faq.md).

---

## Want real examples?

- [prompts/](./prompts/) — Mx-Shell's complete original prompts
  (Chinese body untouched, English header on each file).
  Includes *Zombie Scavenger*, *Kamen Rider* (5 variants), *Kai'Sa*
  (15s/20s/5s), *Pacific Rim + Gundam*, *Cyber-Wuxia*, *Metal Gear*.
- [templates/](./templates/) — IP-stripped reusable skeletons in
  English (organized from Mx-Shell's structure).
