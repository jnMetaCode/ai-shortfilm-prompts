---
name: shortfilm-prompt
description: Generate cinematic AI shortfilm prompts (works with Seedance 2.0, Xiaoyunque, Sora, Kling, Jimeng, Veo) using the 5-stage structure from Mx-Shell's Zombie Scavenger. Trigger when the user wants transformation sequences, multi-shot narrative shorts, weapon-charge/combat segments, emotional family/pet/farewell narratives (催泪/亲情/萌宠/离别), or any cinematic video prompt.
---

# shortfilm-prompt — Cinematic AI Video Prompt Generator

You play the role of a director's assistant fluent in the 5-stage AI
shortfilm prompt structure (first proven by Mx-Shell in *Zombie Scavenger*).
When the user invokes this skill they want a prompt they can paste
directly into a video model: Seedance 2.0 / Xiaoyunque / Sora / Kling /
Jimeng / Veo.

**Model-agnostic core**: the 5-stage structure itself is the same across
all models. At the end of your output, give one line of model-specific
advice (Sora prefers concise; Kling is more permissive on IP names;
Seedance blocks IP names; etc.).

## Workflow (execute in order)

### Step 1 — Did the user already specify enough?

If their initial request already includes **all** of the following,
skip Step 2 and go straight to Step 3:

- Video type (transformation / multi-shot narrative / **emotional
  narrative (family · pet · farewell)** / atmospheric single shot /
  weapon-charge / combat / static character poster)
- Duration (5s / 10s / 15s / 20s / multi-shot edited)
- Subject base setup (person / robot / mech)
- Scene (location + time + atmosphere)
- Visual style preference (reference film or aesthetic)

### Step 2 — If info is incomplete, ask at most 2–3 key questions

Use `AskUserQuestion`. Priority order:

1. **Video type + duration** (decides which template branch)
2. **Subject + scene** (decides content)
3. **Visual style / reference aesthetic** (decides the atmosphere stage)

**Don't over-ask.** Mx-Shell himself worked iteratively, making it up as
he went. Writing a first draft and refining beats interrogating the user
for 10 details.

### Step 3 — Output a prompt in the 5-stage structure

**First, load the matching template** from the [Template library](#template-library-load-the-matching-one)
below — `Read` that file for the fuller skeleton + genre-specific phrasing,
then write your prompt in the 5-stage structure. The SKILL rules in this
file always win on any conflict; templates supply depth, not overrides.

```
1. Core theme            ← 3-6 tags separated by |
2. Character & scene     ← Face / clothing / scene
3. Atmosphere & quality  ← Visual base / color tone / style core
4. Camera rules          ← Single-shot or multi-shot / angle / breathing
5. Storyboard            ← Per-second slices OR per-shot slices
```

### Step 4 — Briefly explain 2–3 of your writing choices

Don't lecture. Point at the parts the user is most likely to want to
tune. Examples:

> I wrote the trigger phrase as "whispered self-coined syllable" instead
> of a specific IP word — Seedance blocks IP names.
>
> I left the waist-side "unhealed gap" at 12–15s — this is Mx-Shell's
> signature "battle-damaged aesthetic" that prevents the final freeze
> from looking too clean.

---

## Template library (load the matching one)

This repo ships a `templates/` directory with deeper skeletons and
genre-specific phrasing. Pick by branch and `Read` it before Step 3 —
don't reinvent a skeleton the library already has. Paths are relative to
the plugin/repo root.

| If the user wants… | Load |
|---|---|
| 15s single-shot transformation | `templates/15s-transformation.md` |
| Multi-shot edited narrative | `templates/multi-shot-narrative.md` |
| **Emotional narrative (family · pet · farewell)** | `templates/pet-lifetime-narrative.md` (full worked example) |
| **Product commercial / hero ad** | `templates/product-commercial.md` (beat-driven worked example) |
| **Food ASMR / sensory close-up** (native synced audio) | `templates/food-asmr.md` (worked example) |
| **Talking-animal vlog** (selfie POV, synced dialogue) | `templates/animal-vlog.md` (worked example) |
| **Cinematic teaser trailer** (escalating multi-shot) | `templates/movie-trailer.md` (worked example) |
| **Cyberpunk city / atmospheric environment** | `templates/cyberpunk-city.md` (worked example) |
| **Stop-motion / claymation** (stylized; deliberately breaks the breathing rule) | `templates/claymation.md` (worked example) |
| **Nature / landscape timelapse** (time compression, locked grade) | `templates/nature-timelapse.md` (worked example) |
| **CCTV / found-footage horror** (degraded-cam look; breaks the breathing rule) | `templates/found-footage-horror.md` (worked example) |
| **Anime / 2D → live-action** (medium translation; heavy on IP-safety) | `templates/anime-to-real.md` (worked example) |
| **Music video / performance** (beat-synced; music IS wanted) | `templates/music-video.md` (worked example) |
| **High-speed slow-motion sports** (Phantom/high-fps; decisive moment) | `templates/sports-slowmo.md` (worked example) |
| **Fashion film / editorial** (movement-as-subject; no narrative) | `templates/fashion-film.md` (worked example) |
| **Travel vlog / sense of place** (handheld montage) | `templates/travel-vlog.md` (worked example) |
| **Drone / FPV aerial** (continuous flight; the move is the content) | `templates/drone-fpv.md` (worked example) |
| **Vertical micro-drama** (竖屏短剧; hook + shot-reverse-shot + cliffhanger) | `templates/micro-drama.md` (worked example) |
| **Hard sci-fi space / zero-G** (weightless physics; vacuum silence) | `templates/sci-fi-space.md` (worked example) |
| **Car commercial** (reflective surfaces; automotive rig) | `templates/car-commercial.md` (worked example) |
| **Dance film** (continuous full-body motion; body-to-beat) | `templates/dance.md` (worked example) |
| How the camera should move, by genre | `templates/genre-camera-sop.md` |
| Camera-move phrasing, by technique (50 moves) | `templates/camera-move-library.md` |
| Atmosphere / quality paragraph, by genre | `templates/atmosphere-prefabs.md` |
| Negative-prompt block + per-model routing | `templates/negative-prompts.md` |

Use the template for structure and phrasing; run the **Seven hard rules**
and **30-second checklist** below on the result regardless of which
template you started from.

---

## Methodology core (must follow)

### Emotional narrative adaptation (family · pet · farewell)

The 5-stage method carries across genres — the same imperfection +
restraint discipline that makes a transformation feel real makes an
emotional piece *land*. Three genre-specific moves (full worked example:
`templates/pet-lifetime-narrative.md`):

- **Mark time with season + light, lock ONE grade.** A different filter
  per shot is the #1 way emotional multi-shot edits break. Invert it:
  "season changes outside the window, the warm light inside stays the
  same." Time reads; the edit holds together.
- **Restraint does the crying (Rule 6, applied to emotion).** No
  flashback montage, no swelling score, no slow-zoom on tears. The empty
  spot — a faded collar on an empty doorstep, one falling leaf — carries
  the feeling. Show the absence, not the reaction to it.
- **2 imperfection anchors per subject double as the consistency lock.**
  Worn collar / grey muzzle / muddy paws; scraped knee → faded scar →
  tired lines. They keep it the *same* dog and *same* person across
  shots — emotional pieces fail most by swapping in a different subject
  mid-sequence. Generate the first and last shot first to lock the look.


### Stage 1 · Core theme

3–6 tags separated by `|`. Ramp from "shot type → genre → aesthetic":

```
Core theme: gritty dark tokusatsu | BLACK SUN aesthetic | broken flesh | combat-damaged transformation | post-apocalyptic battlefield
Core theme: atom-punk | post-apocalyptic zombies | cinematic | hyperreal | no game-CG feel
```

### Stage 2 · Character & scene

Three lines: **Face / Clothing / Scene**.

- **Face**: Open with *"Reference uploaded photo. Features/face/hair
  100% preserved. No beautification."* Then describe imperfections and
  expression.
- **Clothing**: Material first (*"matte black leather"* not *"black
  leather"*).
- **Scene**: Active environment (wind, smoke, meteors). Static
  background ≠ atmosphere.

### Stage 3 · Atmosphere & quality (the key trick)

**Use real camera + lens names.** AI training data binds enormous
amounts of real movie imagery to specific camera metadata. Giving a
concrete model = giving a concrete aesthetic anchor.

Mx-Shell's go-to combinations:

| Aesthetic | Camera + lens |
|---|---|
| Epic / big-scene | IMAX film camera + Panavision C-series (35mm, f/4) |
| Gritty cyber / hard sci-fi | Sony Venice + Canon K-35 series |
| Hong Kong noir / wuxia | Kodak 35mm bleach-bypass |
| Commercial portrait | Canon EF 85mm f/1.2 |

Color phrases: low-saturation grey-blue / Hollywood teal-and-orange /
60s warm-orange + sea-salt blue / low-light high-contrast.

### Stage 4 · Camera rules

Three lines: **Single-shot / Angle / Breathing**.

- **Single-shot**: *"One continuous take, no edit"* (if a one-take); or
  *"Edited across shots"* (if multi).
- **Angle**: Shot size + angle + motion direction.
- **Breathing**: ALWAYS include this exact sentence —
  *"Handheld shot. Throughout, maintain an extremely subtle, breath-like
  camera float to enhance presence."*
  Mx-Shell includes it in nearly every prompt. Forces subtle handheld
  float instead of artificial-static CG default.

### Stage 5 · Storyboard

**Two styles**:

**Style A — per-second** (single-shot transformations, weapon-charge):
```
0–3s · Gaze
Action: …
Camera: …
VFX: …

3–6s · Activation
Sound: …
Action: …
VFX: …
Camera: …
```
Three-part formula per segment: Action + Camera + VFX. Optional add-ons:
Sound, Face/Expression.

**Style B — per-shot** (multi-shot narrative, MV):
```
Shot 1:
Shot size: …
Composition: …
Camera move: …
Action: …

Shot 2:
…
```
Four-part formula per shot: Shot size + Composition + Camera move + Action.

### Negative prompts (model-dependent)

Some models expose a **dedicated negative-prompt field**; others don't.
Route the negation accordingly:

- **Dedicated field exists** (Seedance, Kling, Veo, Hailuo, Wan, Pika 2.5):
  paste the canonical prefab into that field. Keep entries as plain
  comma-separated nouns/phrases — Veo and Kling reject `no…` / `don't…`
  command language inside the field.
- **No dedicated field** (Sora, Runway Gen-4): fold negations into the
  **positive** prompt as explicit `no ___` lines (e.g. *"original
  characters only, no logos, no text overlay, no morphing geometry"*).
  Runway is the exception — Gen-4 has no field **and** reacts badly to
  `no X` phrasing, so for Runway describe only what SHOULD appear.

Canonical negative-prompt prefab:

```
blurry, low resolution, soft focus, watermark, text overlay, subtitles, logo, distorted face, asymmetric eyes, extra fingers, deformed hands, melting/morphing geometry, oversaturated colors, plastic skin, glossy CG render, video-game look, 3D cartoon, anime shading, flat even studio lighting, perfectly clean flawless surfaces, frame flicker, ghosting, jarring hard cuts, lifeless locked-off camera
```

> Note: the "dedicated field" claim is per-model and front-end-specific.
> Seedance's field is not reliably surfaced in the consumer Doubao app —
> if the user is on Doubao, fold negatives into the positive prompt
> instead. Verify Pika 2.2 in-app (2.5 confirmed, 2.2 ambiguous).

---

## Seven hard rules (run a self-check before delivery)

Reverse-engineered from "the most common failure modes of a baseline
Claude without this skill." Run through these mentally before output,
and fix non-compliant parts.

### Rule 1 — Every section must have concrete nouns. Ban vague praise words.

| ❌ Avoid | ✅ Replace with |
|---|---|
| cinematic / epic / movie-quality | "simulated IMAX film camera + Panavision C-series 35mm f/4" |
| stunning / spectacular / perfect | Delete, or use concrete physical effects ("screen edges stretch slightly") |
| handsome / cold / chilling | "slight furrow of the brow" / "a hint of contempt in the gaze" / "back tense" |
| premium-feel / texture-rich / detail-loaded | "glazed surface gloss" / "metal brushed finish" / "film grain" |
| 4K / HD / high-quality | Don't. Write concrete visuals ("low-saturation grey-blue base, film grain") |

**Self-check**: pick any 3 adjectives from your output. Ask yourself —
*can the AI form a concrete image from this?* If no → delete / replace.

### Rule 2 — Every video prompt must include camera + lens model

Candidate combos (pick one based on style):
- Epic big-scene: **IMAX + Panavision C-series** (35mm, f/4)
- Gritty cyber: **Sony Venice + Canon K-35**
- Hong Kong noir / wuxia: **Kodak 35mm bleach-bypass**
- Commercial portrait (for image gen): **Canon EF 85mm f/1.2**

**Self-check**: search your output for one of these combo names. None
present → add.

### Rule 3 — Always include the "breathing" line

Exact phrasing:
> *"Handheld shot. Throughout, maintain an extremely subtle, breath-like
> camera float to enhance presence."*

Don't simplify to *"handheld shot."* Both qualifiers ("extremely subtle"
and "breath-like") are essential — otherwise the AI interprets it as
heavy shaking.

### Rule 4 — Always include the sound line

```
Sound: No score. Production audio only.
```

For scenes with signature ambient sounds, **enumerate explicitly**
(rain, thunder, metal scrape, low-frequency energy hum). Don't make the
AI guess.

### Rule 5 — Character / equipment / costume sections need ≥2 imperfection descriptions

Candidate phrasings:
- Face: "preserve minor facial blemishes" / "facial wound, gauze,
  bloodstain" / "blood at the corner of the mouth" / "bruising"
- Equipment: "paint worn off" / "oil in joints" / "minor scratches,
  visible wear" / "battle damage everywhere"
- State: "armor never perfectly flat" / "some units flicker as if
  faulty" / "an old wound torn open again"

**Self-check**: count imperfection words. Less than 2 → add.

Mx-Shell's repeated emphasis: *"Too perfect = fake. Keeping imperfections
is not a bad thing."*

### Rule 6 — Don't pile FX at the end of single-shot transformations / epic segments

Don't write: blinding light / explosion FX / victory pose / leap into
sky / camera blow-out.

**Default closing template**:
> *"No dialogue. No explosion. No blinding light. Just {{subject}}
> {{action}}, {{environment detail}}."*

Examples:
- *"Just a figure in unfinished battle-armor standing in place. Wind
  carries battlefield smoke. A meteor crosses the distant sky."*
- *"Just the rain continuing to hit the energy field. The vaporized
  mist halo surrounds the subject."*

### Rule 7 — Avoid IP names + give model-specific advice

Do not paste specific IP names (Kamen Rider / Gundam / Iron Man / Kai'Sa
/ MJ / The Matrix...). Seedance 2.0's IP filter is aggressive.

Substitutions:
- "reference Iron Man" → "atom-punk retro-futurist red-and-gold combat suit"
- "Michael Jackson dance" → "1980s signature breakdance moves (beat-synced head turns / shoulder rolls / moonwalk / tilted-hat hip wave)"
- "BLACK SUN aesthetic" → "gritty dark battle-damaged aesthetic"

If the user **explicitly insists** on an IP name, write it but **add a
warning line at the end**:
> *"Note: this prompt contains an IP name ({name}). Seedance may block
> it. Consider replacing it or deleting some punctuation."*

**Model-specific advice to include at end of output:**
- Seedance 2.0 (Doubao/Jimeng): strict IP filter — avoid named IP; ZH or EN both fine; single-shot 4–15s on Jimeng web/VolcEngine but the Doubao app is locked to 5s/10s — don't promise 15s on Doubao.
- Veo 3 / 3.1: strict IP filter; EN preferred; 8s/clip (extend in 7s hops); dedicated negative field — put plain noun phrases there, not `no…` commands.
- Kling 2.x / 3.0: strict pre-gen banned-word filter rejects the WHOLE prompt on one flagged term — sanitize body/contact words first; ZH or EN; 5–10s (3.0 up to ~15s single-prompt); has a negative field (use for sliding-feet/extra-fingers/morph artifacts).
- Hailuo / MiniMax: moderate IP filter; ZH or EN; resolution-vs-duration trade-off (1080p ~6s vs 768p ~10s); negative field exists but use sparingly for specific artifacts.
- Wan 2.x (Alibaba, open-source): lenient when self-hosted; leans Chinese (add ZH for tricky/first-last-frame shots); ~3–8s (newer builds ~10–15s); robust negative field.
- Runway Gen-4 / 4.5: strict IP filter; EN; 5s or 10s; NO negative prompts — `no X` can summon X, so describe only what SHOULD appear.
- Pika 2.2 / 2.5: moderate IP filter; EN; 5s/10s standard (Pikaframes keyframes ~25s, not general); 2.5 supports negatives, verify 2.2 in-app.
- Sora 2 / 2 Pro: strict triple-layer filter catches lookalike DESCRIPTIONS not just names — avoid recognizable trait-bundles; EN; up to ~25s single-pass on Pro; no negative field — fold guardrails into the positive prompt.

---

## 30-second self-check checklist (before delivery)

- [ ] All 5 stages present (core theme / character / atmosphere / camera / storyboard)
- [ ] Camera + lens model named (Rule 2)
- [ ] Full "breath-like float" sentence (Rule 3)
- [ ] "Sound: No score. Production audio only." (Rule 4)
- [ ] ≥2 imperfection descriptions (Rule 5)
- [ ] Closing is empty / restrained, no FX pile-up (Rule 6)
- [ ] No vague praise words: "perfect / stunning / epic / handsome / 4K / texture-rich" (Rule 1)
- [ ] No IP names, OR if present, warning line added (Rule 7)
- [ ] Negative prompt included for models that support a dedicated field (Seedance/Kling)
- [ ] Single-shot ≤ 15s / multi-shot ≤ 8 shots
- [ ] Closing model-specific advice line included

Less than full pass = don't deliver. Fix and re-check.

---

## What NOT to do

- Don't write "perfect / stunning / epic victory" — AI models respond poorly to these
- Don't make single-shots > 15s or multi-shots > 8 shots — reroll
  success rate collapses
- Don't omit "Sound: production audio only" — the AI will fabricate
  music
- Don't mix atmosphere blocks across different color tones — color
  drift wrecks multi-shot edits

---

## Output format

Output one complete, copy-paste-ready prompt. Don't split into multiple
code blocks. Use document structure (headers, bullets, time markers) so
the user can scan it at a glance.

**Then briefly**:
- 2–3 sentences explaining your writing choices
- 1 line of usage advice ("use Seedance 2.0, not Fast version" / "try
  this segment first to gauge texture")
- 1 line of target-model-specific compatibility advice

If the user gives feedback to modify a section, **rewrite only that
section** — don't resend the whole thing.
