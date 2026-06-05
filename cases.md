# Failure → Fix Gallery

> The 14 most common ways AI-video prompts go wrong — and the exact fix
> for each. Every case is grounded in [faq.md](./faq.md) (full Q&A) and
> [methodology.md](./methodology.md) (the 5-stage structure).
>
> Each card: **❌ Symptom / 🔍 Cause / ✅ Fix** — with a concrete
> before→after prompt snippet wherever one helps.
>
> **[中文版 →](./cases.zh.md)**

---

## How to use this page

Skim the symptoms, jump to the one that matches your output, apply the
fix. For the *why* behind each fix, follow the link at the bottom of the
card to the relevant FAQ entry or methodology stage.

Sections:
1. [Faces & IP](#1-faces--ip)
2. [Realism & CG-look](#2-realism--cg-look)
3. [Motion & timing](#3-motion--timing)
4. [Audio](#4-audio)
5. [Endings](#5-endings)

---

## 1. Faces & IP

### Uploaded face photo gets blocked by moderation

**❌ Symptom:** Your reference photo is rejected or flagged before
generation even starts.

**🔍 Cause:** Face moderation on AI-video platforms keeps tightening.
Direct full-face uploads have the highest rejection rate.

**✅ Fix:** In order of escalation —
1. Try several different photos.
2. Feed the photo to Doubao with the **commercial-portrait describer
   template** to generate a *"photorealistic colored sketch"* version,
   then upload that instead.
3. Design the character to **avoid full-face exposure entirely**: helmet,
   mask, robot, back-of-head shots, mannequins with big sunglasses. (This
   is the real reason *Zombie Scavenger*'s lead is a robot.)

→ [faq.md — Faces / IP / blocked content](./faq.md#faces--ip--blocked-content)

---

### Prompt gets flagged for IP / copyright

**❌ Symptom:** A prompt naming Kamen Rider, Gundam, Pacific Rim, Iron
Man, or Kai'Sa gets blocked by Seedance 2.0.

**🔍 Cause:** Seedance's IP-rights filtering is aggressive and blocks
real film / character names.

**✅ Fix:** Strip the names; keep the *design language* as description.

```diff
- Iron Man red-and-gold armor, repulsor blast
+ atom-punk retro-futurist red-and-gold suit, palm energy burst
- Black Sun aesthetic, gritty tokusatsu
+ gritty dark battle-damaged aesthetic, gritty tokusatsu
```

Also works: delete a few characters or punctuation marks without
changing meaning, or swap in synonyms for the same look.

→ [faq.md — Faces / IP / blocked content](./faq.md#faces--ip--blocked-content) ·
[prompts/README.md](./prompts/README.md)

---

### Face / identity drifts between shots

**❌ Symptom:** The character's face shape or expression changes from clip
to clip; the same person doesn't read across cuts.

**🔍 Cause:** Weak Stage 2 lock-down. If you don't explicitly pin facial
features, the AI drifts.

**✅ Fix:** Lock the face hard in **Stage 2 (Character & scene)**:

```text
Face: Reference uploaded photo. Features, face shape, hairstyle 100%
      preserved. No beautification. Maintain [wound / scar / blemish].
```

For transformations, go even harder — keep bone structure identical
across the change:

```text
Preserve the same bone structure, jaw geometry, and facial features
100% identical before and after transformation.
```

Give each key visual element (face, expression, key prop) **its own
dedicated reference photo** so the AI doesn't blend them.

→ [methodology.md — Stage 2](./methodology.md#stage-2--character--scene)

---

## 2. Realism & CG-look

### Output looks like cheap plastic CG, not live-action

**❌ Symptom:** Faces and surfaces read as glossy, fake, game-render CG
instead of film.

**🔍 Cause:** Two usual culprits — (1) over-beautified / filtered
reference photos that already look fake, (2) low-quality reference images
with no real photoreal or 3D-render texture.

**✅ Fix:** Use clear, large, **un-filtered** headshots — ideally bare-face
(no movie puts beauty filters on its actors). Only feed reference images
when the source is genuinely high-detail photoreal or a 3D render. For
dynamic shots (transformations, combat), drop references entirely and let
the AI free-form from **pure text**.

→ [faq.md — Picture quality / texture / realism](./faq.md#picture-quality--texture--realism)

---

### Reference image leaks its art style into the output

**❌ Symptom:** Your output picks up the *style* of the reference (anime,
drawn, CG render) instead of just its design.

**🔍 Cause:** AI binds a reference image's texture and style information
together — poor reference quality leaks unwanted aesthetics into the
result.

**✅ Fix:** Don't attach a reference unless it is genuinely photoreal or a
high-quality 3D render. For motion shots, **omit references entirely** —
Mx-Shell's Kamen Rider armor came entirely from text, which also made
every output uniquely different. Reserve references for character/scene
*continuity* only.

→ [methodology.md — Principle #1](./methodology.md#1-dont-give-the-ai-reference-images-unless-the-image-quality-is-high) ·
[faq.md — References vs. pure text](./faq.md#picture-quality--texture--realism)

---

### Video feels stiff and game-CG — no "presence"

**❌ Symptom:** The shot is technically fine but feels artificial and
locked-off, like game cinematics rather than a handheld film moment.

**🔍 Cause:** Missing the "breathing" handheld float, and no explicit
realism anchors.

**✅ Fix:** Add realism anchors in **Stage 1** (`cinematic | hyperreal |
no game-CG feel`), and in **Stage 4** always include the breathing line:

```text
Breathing: Handheld shot. Throughout, maintain an extremely subtle,
           breath-like camera float to enhance presence.
```

Name a real camera + lens so the AI has a concrete visual anchor — e.g.
IMAX film camera + Panavision C-series (35mm, f/4) for epic shots, or
Sony Venice + Canon K-35 for gritty sci-fi.

→ [methodology.md — Stage 3 & 4](./methodology.md#stage-3--atmosphere--look)

---

### A specific camera move won't execute

**❌ Symptom:** Wrong focal length, wrong angle, or the orbit goes the
wrong direction.

**🔍 Cause:** Vague descriptions like "cinematic" or "dramatic" carry no
precision. The AI needs explicit camera models, focal lengths, and
movement vocabulary.

**✅ Fix:** Be precise in **Stage 4** — camera + lens, shot size, angle,
motion type, and rhythm:

```diff
- Cinematic dramatic camera move around the hero
+ IMAX + Panavision C 35mm. Medium close-up, low-angle 30° from left.
+ Orbit clockwise, very slow, with a 0.1s reactive micro-shake.
```

Vocabulary to pull from — shot sizes (wide / medium / close-up), angles
(low / high / level / over-shoulder), motions (push-in / orbit / follow /
FPV), rhythms (very slow / steady / sudden / reactive).

→ [methodology.md — Stage 4](./methodology.md#stage-4--camera-rules) ·
[faq.md — Camera & composition](./faq.md#camera--composition)

---

### Color grade falls apart in post (banding, noise)

**❌ Symptom:** Pushing color correction even a little causes banding and
noise.

**🔍 Cause:** AI-generated video has a **low color bitrate** — far less
grading headroom than real-camera footage.

**✅ Fix:** Lock your color tone **upstream**, at the image/prompt stage
(**Stage 3, Color & tone**), and keep that section consistent across every
shot. Make the big aesthetic choice in the prompt (Hollywood teal-orange,
grey-blue, retro warm-orange + sea-salt blue…). Do only minor transitions
in CapCut — don't try to *fix* color in post; fix it in the prompt.

→ [faq.md — Duration / long videos / editing](./faq.md#duration--long-videos--editing)

---

## 3. Motion & timing

### One-take video collapses past ~15 seconds

**❌ Symptom:** A transformation or single-shot runs long and quality
breaks down mid-sequence.

**🔍 Cause:** Seedance struggles with one-shot generations much longer
than 15s. The sweet spot is 5–15s by scene type.

**✅ Fix:** Keep transformations **≤ 15s per shot**. For longer sequences
(>15s combat), generate the first 15s, then use Xiaoyunque web client's
**"Continue this video"** to extend. This segmented approach beats one
30s+ shot. Mx-Shell built Kai'Sa as a 15s version plus a separate 5s
extension.

→ [faq.md — Duration / long videos / editing](./faq.md#duration--long-videos--editing) ·
[prompts/kaisa-transformation.md](./prompts/kaisa-transformation.md)

---

### Prompt exceeds the character limit; won't submit

**❌ Symptom:** A long, detailed multi-shot prompt hits the character
ceiling and can't be sent to Seedance 2.0.

**🔍 Cause:** Detailed segmentation and multi-shot scripts run past the
mobile client's limit.

**✅ Fix:** Switch from the mobile app to the **Xiaoyunque web client** —
it has a higher character ceiling. Still too long? Trim ruthlessly: drop
redundant descriptors, merge related clauses, abbreviate Scene lines.
(Mx-Shell's Pacific Rim prompt explicitly notes it needs the web client.)

→ [faq.md — Word limits / rerolls](./faq.md#word-limits--rerolls--non-reproducibility) ·
[prompts/pacific-rim-gundam.md](./prompts/pacific-rim-gundam.md)

---

### Two clips don't connect — feels like two videos

**❌ Symptom:** Cut two clips together and it reads as two separate shots,
not one continuous action.

**🔍 Cause:** No motion-direction continuity. The audience can't read one
action flowing into the next.

**✅ Fix:** Connect by **motion-direction continuity**, not by matching
static frames. *Zombie Scavenger* example: the robot throws a bomb that
blasts the horde and pushes him out one side of frame; the next shot, he
**enters from that same side**. Design shots with deliberate exit/enter
edges to build logical spatial flow.

→ [faq.md — Duration / long videos / editing](./faq.md#duration--long-videos--editing)

---

### A great shot generated once, then won't reproduce

**❌ Symptom:** A combat or weapon-charge shot lands beautifully once,
then every reroll fails to reproduce the camera work.

**🔍 Cause:** AI generation is non-deterministic. Mx-Shell's *Flame
Demon* camera move was an accident — the AI didn't actually follow the
instruction, and he can't reproduce it either.

**✅ Fix:** Accept randomness as part of the process. Treat one prompt as
a **ticket to draw**, not a deterministic recipe — invest in reroll
*selection*, not prompt polish. Mx-Shell's typical counts: high-difficulty
shots 20+ tries, simple shots 2–3. *Zombie Scavenger* burned ~400 images
+ 200+ video shots to land ~40 final clips. **Curate the output; don't
chase prompt perfection.**

→ [faq.md — Word limits / rerolls / non-reproducibility](./faq.md#word-limits--rerolls--non-reproducibility)

---

## 4. Audio

### AI adds background music you didn't ask for

**❌ Symptom:** The model scores your clip with non-diegetic music when
you only wanted production audio.

**🔍 Cause:** Default AI-video models add music unless told otherwise.

**✅ Fix:** Always specify it in **Stage 3 (Atmosphere & look)**:

```text
Sound: No score. Production audio only.
```

Mx-Shell used this formula across every prompt (Zombie Scavenger, Kamen
Rider, Kai'Sa, Metal Gear charge-combat, Pacific Rim, Cyber-Wuxia).

→ [methodology.md — Stage 3](./methodology.md#stage-3--atmosphere--look)

---

## 5. Endings

### The ending is an FX pile-up and reads cheap

**❌ Symptom:** Stacked explosions, light bursts, and particle effects at
the end overwhelm the frame and read as amateur.

**🔍 Cause:** Excess FX at the climax overstages the moment. Mx-Shell
deliberately avoids it.

**✅ Fix:** Practice restraint — **end quietly**. No dialogue, no
explosion, no blinding light. Just the character in the moment: standing,
breathing, in smoke, with one distant element (a meteor crossing the
sky). A restrained ending reads as more elevated than an FX-heavy one.

> *"No dialogue. No explosion. No blinding light. Just a figure standing
> in the smoke, a meteor crossing the distant sky."*
> — Mx-Shell, *Methodology* Principle #3

→ [methodology.md — Principle #3](./methodology.md#3-rerolls-are-normal-leave-the-ending-empty)

---

## See also

- [faq.md](./faq.md) — the full Q&A this gallery distills.
- [methodology.md](./methodology.md) — the 5-stage structure every fix
  refers to.
- [prompts/](./prompts/) — Mx-Shell's complete original prompts.
