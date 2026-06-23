# Worked Example — Stop-Motion / Claymation (style-driven)

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to **handmade stop-motion / claymation** — a style where the
> imperfections *are* the aesthetic. Teaches the most important lesson in
> this library: **know when to BREAK a rule.** Here we deliberately drop
> the breath-float (Rule 3) — stop-motion is stepped and locked-off, a
> handheld sway would destroy the look.
>
> Concept: a small clay creature tiptoes across a handmade set. Swap the
> character and set, keep the 12fps stepped discipline.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): claymation / stop-motion patterns in
> [songguoxs/awesome-video-prompts](https://github.com/songguoxs/awesome-video-prompts)
> and [zhangchenchen/awesome_sora2_prompt](https://github.com/zhangchenchen/awesome_sora2_prompt)
> (MIT).*
>
> **[中文版 →](./claymation.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{character}}` | a round-bellied clay creature | a felt fox / a wire-and-clay robot |
| `{{set}}` | a miniature mossy forest floor | a tiny kitchen / a cardboard city |
| `{{action}}` | tiptoes across, then freezes, startled | bakes a lopsided cake / chases a bug |
| `{{material}}` | matte plasticine with visible fingerprints | wool felt / painted clay over wire |
| `{{lighting}}` | warm practical desk lamp, soft shadow | cool window light / tiny string lights |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`handmade claymation | 12fps stepped stop-motion | tactile fingerprint texture | warm practical lighting | charming imperfection, no smooth CG 3D, no motion blur`

### 2 · Character & scene

**Character:** {{character}}, made of {{material}}. The imperfections are
the style, not flaws to hide: visible thumbprints and tool marks in the
{{material}}, faint seams where parts join, tiny surface lumps, a subtle
wobble and "boil" between frames. Expressive, simple, handmade.

**Set:** {{set}} — a real miniature, built by hand: visible craft, a bit
of glue sheen, slightly uneven scenery, dust on the surfaces. A tabletop
diorama, not a render.

### 3 · Atmosphere & quality
Shot like a real stop-motion set: macro-leaning lens over a tabletop
diorama, shallow depth of field, {{lighting}} (practical lamps, soft
falloff). **12fps stepped animation** — movement advances in small
discrete steps with a faint frame-to-frame "boil," exactly like hand-posed
animation. Warm, slightly imperfect exposure.

### 4 · Camera rules
**Locked-off or stepped moves only — deliberately NO breath-float.** This
is the rule break: stop-motion cameras are on rigs, not handheld. Use a
static lock-off, or a slow incremental dolly/pan that itself steps frame
by frame. A smooth breathing handheld float here reads as CG and kills the
handmade illusion.
- *Sound:* No score (or a simple toy-like motif if you must). Production /
  foley audio — soft fabric/clay shuffles, tiny footsteps, a little
  squeak, the muffled room tone of a quiet workshop.

### 5 · Storyboard (3 beats, ~8–10s)

```
0–3s · Enter (stepped)
Action: {{character}} {{action}} — movement advances in small 12fps
        steps, surface boiling faintly.
Camera: Locked-off wide of the {{set}}, {{lighting}} from one side.
Texture: Thumbprints and seams catch the lamp light.

3–6s · Beat (the little moment)
Action: A pause, a simple expressive reaction — a blink (eyelids posed
        shut then open over 2 steps), a head tilt.
Camera: Slow stepped push-in (no smooth move).
Sound:  Tiny foley — a shuffle, a squeak.

6–10s · Settle (restrained)
Action: {{character}} settles / completes the small action.
Camera: Hold, locked-off.
Close:  No big finale, no sparkle, no smooth swoop. Just the creature
        still, the set quiet, one last faint frame-boil.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, watermark, text overlay, subtitles, logo, smooth CG 3D render, Pixar-style smooth animation, motion blur, fluid 60fps motion, photorealistic skin, glossy plastic perfection, perfectly clean flawless surfaces, handheld camera shake, breathing camera float, melting/morphing geometry, oversaturated colors, video-game look, frame flicker, ghosting, jarring hard cuts
```

---

## Why it's built this way

- **Break the breathing rule on purpose (Rule 3 exception).** Stop-motion
  lives on a locked rig and stepped frames. The breath-float that anchors
  every other template here would betray the handmade look — so we drop it
  and negate "handheld camera shake / breathing camera float" explicitly.
  *The rules serve the genre, not the reverse.*
- **Imperfection IS the aesthetic (Rule 5, taken further).** Thumbprints,
  seams, surface lumps, the frame-to-frame "boil." In other genres flaws
  add realism; here they ARE the medium. Smooth = wrong.
- **"12fps stepped" is the load-bearing anchor (Rule 2 analogue).** Just as
  "ARRI + Panavision" anchors live-action, "12fps stepped stop-motion,
  frame boil" anchors the model to real claymation, not smooth CG.
- **Restrained close (Rule 6).** No sparkle finale, no swoop. The creature
  going still keeps the handmade charm intact.

**Usage:** generate the *0–3s enter* beat first to confirm the 12fps
stepped motion and the clay texture read correctly — if it comes out
smooth/CG, strengthen "12fps stepped, frame boil, no motion blur" and
re-roll. Keep moves locked-off.

**Model:** Kling and Seedance 2.0 handle stylized stepped motion well;
Veo 3 can do it but watch for it defaulting to smooth interpolation —
lean hard on the negative field ("smooth CG, motion blur, 60fps").
Pika is also strong for stylized short-form animation.
