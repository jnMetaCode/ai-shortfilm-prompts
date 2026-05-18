# FAQ — Tools, Failures, Costs, Edge Cases

> Consolidated from the 17 troubleshooting items in Mx-Shell's
> shared document + scattered tips across his two-part livestream Q&A.
>
> Direct quotes from Mx-Shell are in `>` blocks (his original Chinese
> with English translation).
>
> **[中文版 →](./faq.zh.md)**

---

## Tools & models

### Q: Which platform for video generation?

**Xiaoyunque (小云雀)** — specifically its **Seedance 2.0** "Immersive
Shortfilm" mode.

> *"Use the Seedance 2.0 model, not Seedance 2.0 Fast. Fast is quicker
> but skimps on detail. Don't bother with the other random models."*

### Q: Which model for image generation?

About 80% of *Zombie Scavenger* images were made with **GPT Image**.
Next most-used: **Midjourney**, then **Krea**, then **Flux Max** for
material refinement.

Standard workflow:
```
MJ or Seedream  →  Flux (texture / realism polish)  →  Nanobanana (3-views)
```

Skip later steps if an earlier one already produced what you need.

### Q: Hardware requirements?

None. Seedance runs on cloud GPUs. Any office-grade machine works.

---

## Faces / IP / blocked content

### Q: My uploaded face photo gets blocked. What now?

(Note: face moderation is tightening. The methods below may not always
work.)

1. Try several different photos.
2. Ignore the warning and let it generate anyway (likeness may drop).
3. Accept distortion: feed the photo to Doubao and ask for a
   *"photorealistic colored sketch"* — then use that.
4. Use the commercial-portrait describer (see next item).

### Q: Commercial portrait describer template

Feed your photo + this prompt to Doubao:

```
Generate an image: style = "portrait photography". Reference uploaded
photo. Generate a hyperreal commercial portrait of a 22-25 year-old
East Asian male, close shot. Features and face shape 100% match the
reference. Preserve minor facial blemishes. Light scattered loose
strands of hair for a relaxed feel. No accessories. Wearing a deep
black T-shirt. Background: light white blurred gradient. Soft side
lighting to bring out the dimensionality of the face. Warm healthy
skin tone with natural fine luster. Detail enhancement at 100%, disable
over-smoothing. Color: refined warm tones. Edges sharp and clean —
no blur, jaggies, or ghosting. Final output: commercial retouched
portrait quality. Canon EF85mm f/1.2. Aspect 3:4.
```

### Q: A different approach: don't use a face at all

> *"Not every story needs a face. My recent two pieces both work this
> way."*

Helmets, masks, robots, back-of-head shots, mannequins with big
sunglasses — all bypass face moderation while still letting you act.
That's the *real* reason *Zombie Scavenger*'s protagonist is a robot.

### Q: My prompt gets flagged for IP / copyright. What now?

> *"Seedance's IP-rights filtering is aggressive lately. Strip the
> film/character names from your prompt."*

- Replace film/character names (Iron Man → "atom-punk retro-futurist
  red-and-gold suit"; *Black Sun* aesthetic → "gritty dark battle-damaged
  aesthetic").
- Delete a few characters or punctuation marks without changing the
  meaning.
- Use synonyms for the same design language.

### Q: Generation just failed. Now what?

Regenerate. Failure is normal.

---

## Picture quality / texture / realism

### Q: Why does my AI video look like cheap CG?

Two main reasons:

1. **Over-beautified reference photos.**
   > *"Use clear large headshots, not over-filtered ones. If you have
   > the confidence, shoot bare-face (which movie has filters on its
   > actors?). Too perfect = fake."*

2. **Bad reference image source.**
   > *"Don't feed the AI reference images unless your reference itself
   > is high-detail photoreal — or a 3D render."*

### Q: References vs. pure text — which is better?

> *"All my Kamen Rider armor designs came from text descriptions —
> the AI gets to free-form."*
> *"Now everyone gets a different armor design. Yours is uniquely yours.
> Isn't that better?"*

For dynamic-motion shots (transformation, combat), **don't** use
start/end keyframe locking — let the AI generate freely. Save keyframe
locking for character/scene continuity needs only.

### Q: How do I make metal / tile / light feel more real?

Ask the AI itself to write the material description for you:

> *"Like — describe the tile's smoothness, polished or matte finish,
> the cold feeling of stone..."*

Or run the image through **Flux Max** to specifically enhance metal
reflectivity, scratches, and light scattering.

### Q: What resolution should I output?

> *"My videos are all 720p."*

720p is fine for domestic platforms (they recompress anyway). Save
the compute budget for more rerolls.

---

## Camera & composition

### Q: How do I describe camera motion?

> *"For me, camera control is all in the text."*

Picture the move in your head first, then translate to:
- Shot size (medium / close-up / wide)
- Angle (low / high / level)
- Motion (push-in / orbit / follow / locked / FPV)
- Rhythm (very slow / steady / 0.1s reactive shake)

Full vocabulary list in [methodology.md - Stage 4](./methodology.md).

### Q: How do I describe composition?

> *"Just describe it. Know what 'center line' or '3×3 rule of thirds'
> means."*

Example:
```
Model's back centered along the left-of-center-line, right elbow akimbo
forms a framing element, framing the visual subject (the robot).
Robot faces camera, model has back to camera. Robot = near layer,
model = front layer, bar counter = middle layer, background environment
= back layer.
```

Describe **layers** (foreground / middle / background) — far more useful
than positional hints like *"X is next to Y."*

### Q: Should I draw storyboard sketches?

Optional. Mx-Shell only used a hand-drawn storyboard for **one** shot
(the closing long take on the spaceship). Drawing helps save AI compute
but can introduce a "hand-drawn line art" leak into the generated output.

If you want to try: feed any photo to Doubao/GPT and ask it to convert
to *"black-and-white sketch for storyboard reference."* One sentence.

---

## Duration / long videos / editing

### Q: Optimal generation duration?

Depends on the scene. Mx-Shell's habits:
- Opening / transformation: 15s
- General shot: 5–10s
- Brief action (a blink, a glance): 4–5s

### Q: How do I make a video longer than 15s?

Use Xiaoyunque web client's **"Continue this video"** feature. That's how
combat sequences extend transformations.

Don't know how to write a combat prompt?
> *"Write it yourself. I don't enjoy doing combat — get Doubao to
> draft it and refine."*

### Q: How do I connect two video clips?

By **motion direction continuity**.

> *"My robot throws a bomb that blasts the zombie horde — and he gets
> pushed out of frame one side. Next shot, he enters from the same side."*

Visually, the audience reads the motion as one continuous action.

### Q: What editor?

**CapCut** (剪映). No fancy software.

### Q: Color grading?

Some. But AI-generated video has **low color bitrate** — grading
flexibility is limited:

> *"Push it too far and you get color banding and noise. Not like a
> real-camera output where you can really push the dial."*

Best strategy: lock your color tone at the image-generation stage,
keep all video prompts' "Color & tone" section consistent, and do
only minor transitions in post.

---

## Word limits / rerolls / non-reproducibility

### Q: Prompt too long?

- On mobile → switch to the web client.
- Still too long → trim.

### Q: I used your exact prompt — why doesn't my output look like yours?

> *"Even I get different outputs running the same prompt twice."*

AI generation is gacha. Treat one prompt as a **ticket to draw**, not
a deterministic recipe.

**Mx-Shell's per-shot reroll counts:**
- High: 20+ tries
- Low: 2–3 tries
- *Zombie Scavenger* total: ~400 generated images + 200+ video shots
  to produce the final ~40 clips

### Q: How do I reproduce *Flame Demon*'s camera move?

> *"That was an accidental beauty. The AI didn't follow my instruction.
> Blind cat, dead mouse. I can't reproduce it either."*

Accept randomness. Reroll selection matters more than prompt polish.

---

## Music / sound

### Q: Did you make the music?

No. Licensed music from **Artlist.io**.

### Q: Sound effects?

Seedance generates production audio automatically. Specify any unusual
ones in the prompt:

```
Expression-switch sound: a sci-fi tonal sweep
```

### Q: Voice / dialogue?

> *"My whole film has exactly one voice line."*

If you only need one or two lines, don't bother with voice consistency
— pick the best Seedance generates. Newer Xiaoyunque versions have a
**voice reference** feature for consistency needs.

---

## Inspiration / learning

### Q: Where did the story come from?

> *"The inspiration came from Wall-E."*

Anywhere — films, your own life, novels, TV.
> *"You need to have a life before you can have creativity."*

### Q: I'm stuck mid-project. What do?

> *"I didn't have a complete script either. I chatted with a friend,
> shot two test scenes, saw the texture was OK, then started thinking
> about the opening. I made it up as I went."*

**Shoot two test scenes first, then plan as you go.** Better than
finishing a full script in isolation before any AI iteration.

### Q: How do I learn AI shortfilm production?

Mx-Shell himself started in **January 2026**, self-taught.
> *"What I'm saying may be rough — I'm self-taught too, no systematic
> training."*

### Q: Should I learn video editing?

**Yes.**
> *"AI-generated clips aren't always perfect. Trim a piece here, add
> a transition there, splice. Saves money on rerolls."*

---

## Cost / time

### Stated numbers (Mx-Shell self-reported)

| Item | Number |
|---|---|
| Total project duration | 10 days |
| Total cost | Initially stated **~3000 RMB**; later clarified **"actually tens of thousands, maybe 20,000+ RMB"** |
| Images generated | ~400 |
| Video shots generated | 200+ (for ~40 final clips) |
| Hand-written prompt ratio | 95% (only combat scenes were AI-assisted via Doubao) |
| Complete script existed | No — made up as he went |

> *"3000 USD?? It's RMB!"*
> *"Hmm — actually tens of thousands by G2, maybe 20k+ RMB."*
> *"3000 RMB, yes."*

⚠️ **Reality check:** the viral "10 days / 3000 RMB" number is the
marketing line. The actual outlay was likely **20,000 RMB or more**
once you include all the rerolls. Still far below the cost of
shooting a real 3-minute short.

---

## Miscellaneous

### Q: What about base costume for the character?

> *"Match the combat style. No one fights in stilettos. The base outfit
> should match the genre, otherwise immersion breaks."*

### Q: Your prompts have typos.

Yes.
> *"My prompts have some typos. Feel free to fix them before using."*

### Q: What's your background?

Vocational school. Photography is a side hobby.

### Q: Will you keep posting new prompts?

Depends.
> *"I have a day job and other hobbies. The Kamen Rider thing was just
> a whim — I didn't expect this much attention."*
