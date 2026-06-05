# Negative Prompts — Reusable Anti-Artifact Block

> Authored by jnMetaCode (MIT). A companion to the
> [atmosphere prefabs](./atmosphere-prefabs.md): where those describe what
> you *want*, this file collects what you want to *exclude* — the recurring
> failure modes of AI video (melting hands, plastic skin, frame flicker,
> the "video-game look") and how to suppress them per model.
>
> **How to use**: drop the canonical block below into your model's negative
> field if it has one; otherwise read the compatibility table — several
> tools need positive-only phrasing instead, and a couple will summon the
> very thing you list if you write "no ___".
>
> **[中文版 →](./negative-prompts.zh.md)**

---

## The canonical negative prefab

Copy-paste this as your default. It targets resolution/sharpness defects,
overlay junk, anatomy breakage, the over-stylized CG/anime look, and dead
camera work — the artifacts that read as "AI" at a glance.

```
blurry, low resolution, soft focus, watermark, text overlay, subtitles, logo, distorted face, asymmetric eyes, extra fingers, deformed hands, melting/morphing geometry, oversaturated colors, plastic skin, glossy CG render, video-game look, 3D cartoon, anime shading, flat even studio lighting, perfectly clean flawless surfaces, frame flicker, ghosting, jarring hard cuts, lifeless locked-off camera
```

It is written as a **plain comma list of unwanted nouns/phrases** on
purpose — that is the format the dedicated negative fields (Veo, Kling,
Wan, Hailuo) expect. Do **not** prefix items with "no" or "don't" when
you paste into a dedicated field. For tools without a field, see the
in-prompt negation guidance below.

---

## Which models take a negative field — and how to feed it

Mechanics differ more than people expect. Some tools have a dedicated box,
some need the negatives folded into the positive prompt as guardrail
phrases, and **two (Runway Gen-4, and to a degree Seedance's consumer app)
do not reliably support negation at all** — on Runway, "no X" can actively
summon X.

| Model | Dedicated negative field? | How to negate | Single-shot max | IP filter | Lang |
|---|---|---|---|---|---|
| **Seedance 2.0** (Doubao / Jimeng-Xiaoyunque, ByteDance) | Partial — no reliable field in the consumer app | Describe what you DO want; fold avoidance phrasing in-prompt | ~10–15s (Doubao app locked to 5s/10s buttons; Jimeng web & VolcEngine console expose 4–15s) | Strict (domestic ByteDance is harsher than most Western tools) | Either (native ZH safest) |
| **Veo 3 / 3.1** (Google) | **Yes** | Plain noun/phrase list in the field — **no "no/don't" commands** | 8s (4/6/8s); Extend stacks 7s hops up to ~148s, quality drops after 4–5 | Strict | EN |
| **Kling 2.x / 3.0** (Kuaishou) | **Yes** | Best for stability artifacts (sliding feet, extra fingers, morphing), not generic "quality" words | 2.5: 5–10s (Pro ~12s); 3.0: ~15s single-prompt | Strict (banned-word filter rejects the WHOLE prompt on one match) | Either |
| **Hailuo / MiniMax** (Hailuo 02 / 2.3) | **Yes** | Use sparingly — boundary-setting for specific artifacts, not a primary lever | ~6–10s (1080p ~6s; 768p ~10s) | Moderate | Either |
| **Wan 2.x** (Alibaba, open-source) | **Yes** (robust) | Documented defaults: morphing, warping, face deformation, flickering, jittering, inconsistent lighting | 2.2: ~3–8s; 2.5/2.6: ~10–15s | Lenient when self-hosted | Native ZH (EN-only can underperform) |
| **Runway Gen-4 / 4.5** | **No** | Positive-only — describe only what SHOULD appear; "no X" can produce the opposite | 5s or 10s | Strict | EN |
| **Pika (2.2 / 2.5)** | Partial — yes on 2.5, unclear on 2.2 | 2.5 accepts "no morphing, no extra limbs…"; verify in-app on 2.2 | 5s/10s; Pikaframes keyframes up to ~25s | Moderate | EN |
| **Sora 2 / 2 Pro** (OpenAI) | **No** dedicated box | Negate in-prompt with guardrail phrases ("original characters only, no logos or text") | Up to ~25s on Pro (standard tier shorter) | Strict (triple-layer; catches lookalikes, not just names) | EN |

**Three rules that trip people up:**

1. **Runway Gen-4 is positive-only.** Porting `no distorted hands` into a
   Runway prompt is the single most common cross-tool mistake — it can
   *summon* distorted hands. Rephrase the whole intent positively
   ("clean five-fingered hands, anatomically correct").
2. **Dedicated fields take descriptions, not commands.** In Veo/Kling/Wan,
   put `extra limbs, glitch morphs, text overlays` — never
   `no extra limbs`. The "no" wastes a token and can confuse the parser.
3. **Seedance's consumer Doubao app has no surfaced negative field and is
   locked to 5s/10s buttons.** Don't promise 15s or a negative box there;
   the full 4–15s range and finer control live on Jimeng web / VolcEngine.

> Confidence: durations and negative-prompt mechanics are medium-high for
> Veo 3.1, Runway Gen-4, Kling, Wan, and Sora (consistent across 2026
> vendor/help docs); medium for Seedance 2.0 and Hailuo (mostly third-party
> guides). Veo's ~148s and Sora/Pika's ~25s come from extension/keyframe
> features, **not** plain single-shot generation. IP-filter "strictness"
> labels are qualitative judgments, not formal vendor classifications.

---

## Scenario-tuned variants

Append the relevant line to the canonical block for the genre you're
shooting. These target failure modes specific to each scenario rather than
generic quality.

### Transformation sequences

```
premature full transformation, symmetrical clean armor, instant costume swap, no in-between morph stages, untextured smooth plating, transformation happening off a single cut
```

Why: transformation shots fail by *skipping the middle* — the model jumps
straight to the finished suit, or renders it factory-clean. You want
staged, asymmetric, battle-worn growth. Pair with the **Dark Tokusatsu**
atmosphere prefab.

### Combat / impact

```
weightless floaty motion, no impact, soft contact, characters phasing through each other, missing follow-through, slow-motion drift on every hit, no debris or dust on impact
```

Why: AI combat reads as *weightless* — punches that don't land, bodies
that don't recoil. Negate the floatiness and demand impact/weight. Pair
with the **Hollywood Teal-and-Orange** or **Heavy Mech** prefab.

### Dialogue / talking head

```
lip-sync drift, mouth out of sync with audio, frozen dead eyes, mannequin stillness, uncanny face warp on speech, teeth merging, plastic lip texture
```

Why: close-up dialogue exposes lip-sync drift and the "frozen eyes"
uncanny look. Pair with the **Commercial Portrait** reference workflow so
the face is locked before motion.

### Environment / wide establishing

```
warping background geometry, flickering distant detail, melting architecture, repeating tiled textures, impossible perspective, crowd faces smearing, signage gibberish text
```

Why: wide shots break in the *background* — smearing crowds, gibberish
signage, architecture that boils between frames. Hold the geometry stable.

---

## See also

- [`../skills/shortfilm-prompt/SKILL.md`](../skills/shortfilm-prompt/SKILL.md)
  — the Skill that assembles full prompts; it pulls from this block when a
  target model has a negative field.
- [`../methodology.md`](../methodology.md) — the 5-stage structure these
  negatives plug into (the anti-artifact list belongs in the quality/
  atmosphere stage).
- [`./atmosphere-prefabs.md`](./atmosphere-prefabs.md) — the positive
  counterpart: what you *want* the shot to look like.
