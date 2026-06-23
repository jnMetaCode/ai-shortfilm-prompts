# Worked Example — Nature / Landscape Timelapse

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to a **landscape timelapse** — where the subject is *light and
> time*, not a character. Reinforces the "lock one grade, mark time by
> light" discipline (shared with the emotional templates) and the rare
> case where the breath-float is deliberately minimal (a timelapse rides a
> locked tripod / motion-control rig, not a handheld).
>
> Concept: a mountain valley from pre-dawn to night, clouds streaming,
> shadows sweeping. Swap the location, keep the time-compression rules.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): nature/landscape scenes in
> [hr98w/awesome-sora-prompts](https://github.com/hr98w/awesome-sora-prompts)
> (CC0) and the camera/grade notes in
> [khanof89/awesome-video-prompts](https://github.com/khanof89/awesome-video-prompts)
> (MIT).*
>
> **[中文版 →](./nature-timelapse.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{place}}` | a high alpine valley | a coastal cliff / a desert mesa / a city skyline |
| `{{time_arc}}` | pre-dawn → midday → dusk → night | blue hour → sunrise / storm rolling in |
| `{{motion}}` | clouds streaming, shadows sweeping | tide rising / fog pouring over a ridge |
| `{{grade}}` | cool dawn blue warming to gold | desaturated steel / warm amber |
| `{{foreground}}` | a lone wind-bent pine | a still lake / a winding road |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`landscape timelapse | natural light cycle | one locked grade across time | grand stillness | photoreal, no HDR oversharpening, no oversaturated postcard look`

### 2 · Character & scene

**Subject (light + time over {{place}}):** the landscape is the frame;
*time* is the subject. {{motion}} compressed — clouds and shadows move
fast while the land stays solid. A {{foreground}} anchors scale and gives
the eye a fixed point as the light changes around it.

**Imperfections (keep it real, not a stock postcard):** a faint lens
flare and dust as the sun crests, one bird crossing the frame, haze in
the far valley, uneven cloud — nature is never perfectly clean.

### 3 · Atmosphere & quality
Shot on a RED / ARRI with a wide anamorphic lens on a motion-control
timelapse rig. **Lock ONE grade across the whole arc: {{grade}}** — mark
the passage of time *only* through the changing sun angle, shadow length,
and sky colour, never by switching filters. Photoreal, fine natural grain,
true dynamic range (no crunchy HDR halos).

### 4 · Camera rules
Locked-off, or an extremely slow motion-control push/parallax — a
timelapse rides a rig, not a hand.
- *Breathing:* keep it **minimal here** — a tripod-locked timelapse should
  be rock-steady; at most an imperceptible drift. (This is the rare
  template where the full breath-float line is dialled almost to zero.)
- *Sound:* No score. Production / ambient audio only — wind over the
  ridge, distant water, birdsong at dawn, the deep quiet of night.

### 5 · Storyboard (4 beats = one day, ~12s)

```
0–3s · Pre-dawn ({{grade}} at its coolest)
Action: {{place}} under blue pre-dawn light, {{foreground}} a silhouette.
        {{motion}} just beginning, slow.
Camera: Locked wide. The sky lightens at the edge.

3–6s · Sunrise → midday
Action: Sun crests — a flare and dust catch the lens; shadows shorten and
        sweep across the land as {{motion}} accelerates.
Camera: Imperceptible slow push.

6–9s · Afternoon → dusk
Action: Light warms through the locked grade, shadows lengthen the other
        way, clouds streaming gold. A bird crosses once.

9–12s · Dusk → night (restrained close)
Action: Colour drains to deep blue, first stars. {{motion}} slows and
        settles.
Close:  No dramatic sun-ray finale, no music swell. Just the valley going
        quiet under the first stars, {{foreground}} still where it began.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, watermark, text overlay, subtitles, logo, oversaturated colors, HDR halos, crunchy oversharpening, postcard look, fake painted sky, plastic CG terrain, video-game look, 3D render, grade shifting between shots, flickering exposure (timelapse flicker), warping geometry, melting clouds, jarring hard cuts, shaky handheld camera
```

---

## Why it's built this way

- **Lock one grade, mark time by light (shared core discipline).** Same
  rule that holds emotional multi-shot edits together: don't switch
  filters to show time passing — let the sun angle, shadow length and sky
  colour do it. The grade is the constant the eye trusts.
- **Tripod, not handheld (deliberate breath-float exception).** A
  timelapse is shot locked-off on a rig. The breath-float that anchors
  most templates here is dialled almost to zero — match the camera anchor
  to how the genre is *actually* shot.
- **Imperfections keep it real (Rule 5).** Lens flare, dust, a crossing
  bird, haze. The postcard-perfect version reads as a stock render; the
  small flaws read as a real lens pointed at a real place.
- **Restrained close (Rule 6).** Quiet under the first stars, not a
  god-ray finale. Stops the model piling on a fake dramatic sunburst.

**Usage:** generate the *sunrise → midday* beat first — if the light
transition stays on one grade and doesn't flicker, the full arc will hold.
Watch for "timelapse flicker" (exposure jumping frame to frame) — negate it
explicitly. Keep the camera locked.

**Model:** Veo 3 and Sora 2 give the best photoreal skies and light
transitions; Kling and Seedance handle the motion well but watch for
flicker on long light changes. This genre wants real dynamic range — avoid
the HDR/oversaturation default.
