# Worked Example — Fashion Film / Editorial Look Book

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to a **fashion film** — where there's no plot: the *garment
> in motion* and editorial light are the subject. Teaches movement-as-
> content, editorial lighting, and texture over narrative.
>
> Concept: a model in a flowing coat, fabric moving in a controlled wind,
> shot like a high-fashion editorial. Swap the look, keep the rhythm.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): commercial/editorial patterns in
> [LichAmnesia/awesome-ad-video-prompts](https://github.com/LichAmnesia/awesome-ad-video-prompts)
> (CC BY 4.0) and [geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts)
> (MIT).*
>
> **[中文版 →](./fashion-film.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{model}}` | a model in a long structured coat | streetwear / couture gown / tailored suit |
| `{{fabric_motion}}` | the coat sweeping in a slow wind | a dress rippling / a scarf trailing |
| `{{set}}` | a bare concrete studio with one hard window | a sand dune / a marble hall / a neon alley |
| `{{light}}` | one hard key from a high window, deep shadow | high-key white / chiaroscuro / coloured gels |
| `{{grade}}` | desaturated with warm skin | rich editorial B&W / muted earth tones |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`fashion film | editorial movement | controlled hard light + texture | confident stillness and motion | high-fashion realism, no catalog stiffness`

### 2 · Character & scene

**Model:** {{model}}. Reference uploaded photo, features 100% preserved,
no beautification, no plastic retouching — real skin with texture and
pores, a stray hair, natural poise. Movement is editorial: deliberate,
confident, a little aloof; not a smiling catalog pose.

**Garment (co-subject):** the clothing is half the shot. {{fabric_motion}}
— real fabric weight, weave visible, wrinkles and drape that move with
air and the body.

**Scene:** {{set}}, {{light}}.

### 3 · Atmosphere & quality
Shot on ARRI Alexa with vintage primes, editorial {{grade}}. One
controlled hard key with deep falloff, soft negative fill — fashion
lighting sculpts, it doesn't flatten. Fine film grain, true fabric and
skin texture, rich shadow.

### 4 · Camera rules
Slow, deliberate moves built around the garment — a slow push, a lateral
track past the model, a turn that lets {{fabric_motion}} read.
- *Breathing:* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence."
- *Sound:* No score (or a single rhythmic music bed if it's a runway
  cut — an editorial film can carry music like an MV). Production audio:
  fabric movement, footsteps on the floor, a fan's air, room tone.

### 5 · Storyboard (3 beats, ~10s)

```
0–3s · Texture (the detail sells the fabric)
Action: Macro on the {{model}}'s garment — the weave, a seam, the drape,
        light raking across the {{fabric_motion}}.
Camera: Slow push on the texture, shallow focus.

3–7s · Movement (the garment in motion)
Action: Pull to the full figure in {{set}}; the model moves, {{fabric_motion}}
        catches the air and the hard {{light}}.
Camera: Slow lateral track or a turn, breath-float, letting the fabric
        lead the eye.

7–10s · The editorial hold (restrained close)
Action: The model settles into a confident, still editorial pose; the
        fabric comes to rest.
Camera: Hold, breath-float.
Close:  No smile-to-camera, no logo card, no spin. Just a held editorial
        frame and the fabric settling in the hard light.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, watermark, text overlay, subtitles, logo, plastic retouched skin, doll-like face, oversaturated colors, glossy CG render, video-game look, 3D cartoon, flat even catalog lighting, smiling stock-photo pose, stiff mannequin, brand-new fabric with no movement, distorted face, extra fingers, deformed hands, melting/morphing cloth, frame flicker, ghosting, lifeless locked-off camera, cheesy lens flare
```

---

## Why it's built this way

- **Movement is the content, not a plot.** A fashion film has no story —
  the garment moving in light is the subject. Build the storyboard around
  fabric motion and an editorial hold, not around events.
- **Editorial light sculpts (Rule 2/atmosphere).** One hard key with deep
  falloff, not flat catalog light. "ARRI + vintage primes, one hard key"
  anchors high-fashion cinematography; "studio fashion shoot, bright" gives
  a stiff catalog look.
- **Real texture beats retouching (Rule 5).** Real skin pores, fabric
  weave and drape, a stray hair. Plastic-retouched skin and brand-new
  motionless fabric read as CG; the texture and movement are the luxury.
- **Restrained editorial close (Rule 6).** A confident held pose, not a
  smile-to-camera or a spin. Keeps it editorial, not catalog.

**Usage:** generate the *movement* beat (3–7s) first — fashion lives on how
the fabric moves; if the drape and the hard light read as real there, the
rest holds. Keep the model's look consistent across cuts (generate the hold
frame first to lock it).

**Model:** Veo 3 and Sora 2 give the best fabric physics and editorial
skin/light; Kling is strong on the movement. If you want a runway music
bed, lay it in post (see [music-video.md](./music-video.md) for beat-sync).
