# Worked Example — CCTV / Found-Footage Horror

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to **found-footage / security-cam horror** — a genre where a
> *degraded, cheap camera* is the entire aesthetic, and restraint (not
> gore) creates the dread. Another deliberate rule break: the camera is a
> fixed mount, so the breath-float is dropped (a CCTV does not move).
>
> Concept: a fixed security camera on an empty night corridor; something
> is subtly, wrongly off. Swap the location, keep the discipline.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): the Horror / CCTV-style category in
> [zhangchenchen/awesome_sora2_prompt](https://github.com/zhangchenchen/awesome_sora2_prompt)
> (MIT).*
>
> **[中文版 →](./found-footage-horror.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{place}}` | an empty office corridor at 3 AM | a parking garage / a stairwell / a back yard |
| `{{wrong_thing}}` | a door at the end stands open that was shut | a figure half-out of frame / lights cutting out one by one |
| `{{cam_type}}` | ceiling security camera, wide fisheye | a doorbell cam / a handheld phone / a baby monitor |
| `{{timestamp}}` | 03:14:07 AM, top-right | a date burn-in / a channel label |
| `{{night_mode}}` | IR night-vision green-grey | low-lux colour with heavy noise |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`found-footage horror | fixed security-cam angle | {{night_mode}} | dread through stillness | no jumpscare gore, no cinematic polish`

### 2 · Character & scene

**Subject (the space, and what's wrong with it):** {{place}}, empty and
still. The horror is that *almost* nothing happens — then {{wrong_thing}}.
No monster reveal, no blood. The wrongness is quiet and specific.

**The "camera" as a character (this is the look):** {{cam_type}} —
{{night_mode}}, low resolution, visible compression blocking in the
shadows, faint sensor noise crawling, a slightly warped wide/fisheye
edge, a {{timestamp}} burn-in, and an occasional dropped/stuttered frame.
These artefacts ARE the aesthetic — not flaws to clean up.

### 3 · Atmosphere & quality
Shot to look like real cheap surveillance footage: NOT a cinema camera.
Low dynamic range, crushed blacks with noise, green-grey IR or murky
low-lux colour, compression artefacts, fixed exposure that can't keep up
with the dark. The "ugliness" is the realism — anything that looks graded
or filmic breaks the illusion.

### 4 · Camera rules
**Fixed mount — locked off. Deliberately NO breath-float.** A security
camera does not breathe, drift, or reframe; it stares. (This is the rule
break: the handheld float that anchors most templates here would instantly
read as "a person filming," killing the CCTV illusion.) One fixed wide
angle for the whole shot.
- *Sound:* No score. Just room tone — an HVAC hum, a distant unexplained
  knock, the electrical buzz of a failing light. Silence does the work.

### 5 · Storyboard (3 beats, ~10s)

```
0–4s · Normal (establish the boredom)
Action: {{place}}, empty, still. {{night_mode}}, noise crawling, the
        {{timestamp}} ticking. Nothing happens. Hold the boredom — it
        sets the trap.
Camera: Fixed wide. Locked.
Sound:  Room tone, a faint hum.

4–7s · Wrong (the small specific change)
Action: {{wrong_thing}} — subtle, easy to miss, no music sting. A frame
        stutters/drops right as it happens.
Camera: Still fixed. The eye has to find it.
Sound:  The hum, maybe one distant knock. No stinger.

7–10s · Hold (restrained close)
Action: Nothing else moves. The wrong thing just… stays. The footage
        keeps rolling on the empty, now-wrong space.
Close:  No reveal, no creature, no scream, no cut to black with a bang.
        Just the timestamp ticking on a corridor that is no longer right.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
cinematic color grade, filmic look, shallow depth of field, smooth handheld motion, breathing camera float, dramatic lighting, lens flare, high resolution clean image, watermark, logo, gore, blood splatter, jumpscare monster reveal, oversaturated colors, 3D cartoon render, video-game look, polished VFX, score music, melting/morphing geometry, warped unreadable timestamp text
```

---

## Why it's built this way

- **The cheap camera IS the genre (deliberate Rule 2 inversion).** Instead
  of "ARRI + Panavision," we anchor to "security cam, IR night mode,
  compression noise, timestamp." The degraded look is exactly what sells
  "this is real footage someone found." A clean cinematic image destroys it.
- **Locked-off, no breath-float (Rule 3 exception).** A mounted camera
  stares. Any drift reads as a human operator and breaks the conceit — so
  we drop the float and negate "breathing camera float / smooth handheld."
- **Restraint is the horror (Rule 6, weaponised).** No monster, no gore,
  no music sting. One small, specific *wrong* thing in a boring frame is
  scarier than any reveal — and it stops the model defaulting to cheap
  jumpscares.
- **Artefacts as imperfection anchors (Rule 5).** Noise, blocking, a
  dropped frame, a fisheye edge. Here the "flaws" aren't added realism —
  they're the whole medium.

**Usage:** generate the *normal* beat first and make sure it reads as
genuine cheap footage (noise, timestamp, fixed angle); if it comes out
clean/cinematic, lean hard on the negative field. Keep {{wrong_thing}}
small — the restraint is the scare.

**Model:** Sora 2 is excellent at the "uncanny real footage" look and
holds the fixed frame; Kling and Seedance work but watch that they don't
prettify it — push the negative field. Keep any on-screen timestamp short
so the model doesn't warp the text.
