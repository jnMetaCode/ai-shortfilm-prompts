# Worked Example — Travel Vlog / Sense of Place

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to a **travel vlog** — an authentic handheld montage that has
> to make the viewer *feel a place* in a few shots. Teaches the
> montage-of-place structure (wide → detail → people → move), authentic
> mirrorless-handheld energy, and marking a location through specific
> sensory details rather than a stock drone cliché.
>
> Concept: a morning in a coastal old town. Swap the destination, keep
> the montage discipline.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): VLog / travel montage patterns surveyed in
> [jax-explorer/awesome-veo3-videos](https://github.com/jax-explorer/awesome-veo3-videos)
> (no license — inspiration only).*
>
> **[中文版 →](./travel-vlog.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{place}}` | a coastal old town at morning | a night market / an alpine village / a desert road |
| `{{wide}}` | sun rising over tiled rooftops and the sea | a temple gate / a neon street / dunes |
| `{{detail}}` | steam off a street-food griddle, a cat on a wall | hands making tea / a lantern / footprints in sand |
| `{{people}}` | a vendor laughing, kids running an alley | a monk sweeping / a busker / a fisherman |
| `{{traveler}}` | the vlogger, seen briefly from behind | a couple / a solo backpacker / hands only |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`travel vlog | authentic handheld montage | golden-hour natural light | sense of place | real-not-staged, no glossy drone-stock cliché`

### 2 · Character & scene

**Traveler (secondary):** {{traveler}} — rarely the focus, mostly a
presence that gives the place scale and a POV. Reference uploaded photo if
shown; otherwise hands / over-the-shoulder.

**Place (the real subject):** {{place}}. The location is told through
*specific sensory details*, not a postcard: {{detail}}, {{people}},
real textures, real light, candid life. Imperfections that read as real
travel footage: imperfect framing, a lens flare, wind, a passerby crossing.

### 3 · Atmosphere & quality
Shot mirrorless-handheld (a real travel-creator look — not a cinema rig,
not a phone): warm golden-hour natural light, light film grain, true
colour, slightly imperfect handheld exposure. Authentic and immediate,
not a glossy tourism-board spot.

### 4 · Camera rules
Handheld montage energy — a few short shots that build a place: a wide to
establish, close details, a human moment, a motion shot walking in.
- *Breathing:* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence." — here it can be a touch
  more alive; real travel footage has energy and small reframes.
- *Sound:* No score. Production / ambient audio only — enumerate the place:
  waves and gulls, a sizzling griddle, market chatter in the local
  language, footsteps on stone, wind. (Add trending music in post if
  posting to social.)

### 5 · Storyboard (4 shots, ~12s)

```
Shot 1 — Arrive (wide, establish)
  {{wide}}, golden morning light. Handheld, a slow drift in.

Shot 2 — Detail (get specific)
  Close on {{detail}} — the texture that says exactly where this is.
  Quick, intimate, shallow focus.

Shot 3 — People (the place is alive)
  {{people}} — a candid human moment, not posed. The traveler may pass
  through frame.

Shot 4 — Move (put us there)
  A walking POV / over-the-shoulder of {{traveler}} heading into the
  scene, the place opening up ahead.
  Close: No spinning drone hero shot, no title card, no "subscribe."
  Just the traveler walking on into the place, ambient sound carrying.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, watermark, text overlay, subtitles, logo, oversaturated colors, glossy tourism-board look, fake HDR, plastic CG render, video-game look, 3D cartoon, flat even studio lighting, staged posed tourists, empty lifeless streets, distorted faces, extra fingers, melting/morphing geometry, frame flicker, ghosting, lifeless locked-off camera, generic drone stock shot, subscribe button overlay
```

---

## Why it's built this way

- **Sense of place through specific details, not postcards.** A travel
  vlog lands when it shows *this exact place* — steam off a real griddle,
  a cat on a wall, the local language in the chatter — not a generic drone
  sweep. Concrete sensory detail beats scenery.
- **Mirrorless-handheld, not cinema or drone (Rule 2, matched to genre).**
  The authentic travel-creator look is handheld mirrorless with golden
  light. A glossy drone/tripod look reads as a tourism ad and kills the
  "I was there" feel.
- **Montage structure: wide → detail → people → move.** This four-beat
  shape builds a place fast. It's the travel-vlog grammar, not a narrative.
- **Restrained close (Rule 6).** Walking on into the place, not a drone
  hero spin or a subscribe card. Keeps it authentic.

**Usage:** generate the *detail* and *people* shots first — they carry the
"sense of place"; if those feel specific and alive, the wide and the move
frame them. Mark the location through what's unique to it.

**Model:** Kling and Seedance handle handheld energy and crowds well;
Veo 3 gives the best golden-hour realism and native ambient audio. For
social, lay a trending track over it in post.
