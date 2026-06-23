# Worked Example — Talking Animal VLog (selfie POV)

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to the **talking-animal vlog** — the viral first-person form
> that exploded with native-audio engines (a pet narrating its day to a
> handheld selfie camera). Pairs naturally with the emotional pet line
> ([pet-lifetime-narrative.md](./pet-lifetime-narrative.md)) but plays it
> for charm and comedy instead of tears.
>
> Concept: a stubby corgi vlogs its morning, talking to the camera.
> Swap the animal and the bit, keep the structure.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): talking-animal / VLog patterns surveyed in
> [jax-explorer/awesome-veo3-videos](https://github.com/jax-explorer/awesome-veo3-videos)
> (no license — creative inspiration only) and category structure from
> [zhangchenchen/awesome_sora2_prompt](https://github.com/zhangchenchen/awesome_sora2_prompt)
> (MIT).*
>
> **[中文版 →](./animal-vlog.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{animal}}` | a stubby orange-and-white corgi | a grumpy tabby cat / a golden retriever puppy |
| `{{voice}}` | warm, slightly goofy, fast | dry and deadpan / squeaky and excitable |
| `{{setting}}` | a sunny kitchen, then the back yard | an apartment / a car / a hiking trail |
| `{{bit}}` | reviewing breakfast like a food critic | narrating a "very busy" lazy day |
| `{{punchline}}` | gets distracted mid-sentence by a dropped treat | flops over and "ends the stream" |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`first-person animal vlog | handheld selfie POV | natural daylight | synced talking + ambient | charming realism, no uncanny CG fur`

### 2 · Character & scene

**Hero subject (the animal):** {{animal}}, talking directly to the camera
(lip and jaw move in sync with the speech — natural, not a stiff puppet).
Imperfections that keep it real and the *same* animal across cuts: a bit
of drool at one corner, fur slightly matted on the left ear, a crumb on
the snout, one slightly lazy eye. Expressive, mobile face. Voice:
{{voice}}.

**Scene:** {{setting}}. Real lived-in space — dishes in the sink, a chewed
toy on the floor — not a clean studio. Daylight from a window.

### 3 · Atmosphere & quality
Shot **smartphone-style** — wide ultrawide selfie framing held at
arm's length, slight lens distortion at the edges, the animal's face
close and a little fish-eyed, autofocus hunting just slightly. This is
the deliberate genre break: a vlog wants a *phone camera* look, **not**
a cinema lens. Natural daylight, true colour, minimal grain, the casual
imperfect exposure of real handheld phone video.

### 4 · Camera rules
Selfie POV — the animal (or an unseen owner) holds the camera at arm's
length; framing bobs and re-centres like real handheld vlog footage.
One or two quick cutaways to what it's "talking about" (B-roll).
- *Breathing:* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence." — here it can be a touch
  more active than usual; real selfie video drifts and re-frames.
- *Sound:* No score. Production / synced audio only — the animal's voice
  ({{voice}}) locked to its mouth movements, collar jingle, claws on the
  floor, ambient {{setting}} sounds, the occasional off-camera human
  "mm-hm". Dialogue must sync to the lip movement.

### 5 · Storyboard (3 beats, ~10s)

```
0–3s · Cold open / greeting
Action: {{animal}} fills the selfie frame, looks straight into lens, and
        launches into {{bit}} — talking fast, expressive.
Camera: Arm's-length selfie, slight bob, face close and edge-distorted.
Sound:  Voice in sync from frame one, ambient {{setting}} behind.

3–7s · The bit / B-roll
Action: Cutaway to what it's narrating (the food bowl / the "busy"
        schedule), then back to the talking face reacting.
Camera: Quick handheld cutaway, then re-centre on the face.
Sound:  Voice continues over the cutaway, collar jingle, claws on floor.

7–10s · Punchline / sign-off
Action: {{punchline}} — the bit collapses; the animal loses the thread.
Camera: Camera tilts / drops as the "host" gives up on the take.
Close:  No big paw-wave goodbye, no on-screen hearts, no subscribe
        graphic. Just the animal flopping down and the frame tilting to
        the ceiling, voice trailing off mid-word.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, watermark, text overlay, subtitles, logo, distorted face, asymmetric eyes, extra limbs, deformed paws, the animal changing breed or color between shots, uncanny rubbery CG fur, dead glassy eyes, stiff puppet jaw, lip-sync mismatch, oversaturated colors, plastic skin, glossy CG render, video-game look, 3D cartoon render, polished cinematic lighting, frame flicker, ghosting, jarring hard cuts, on-screen emojis, subscribe button overlay
```

---

## Why it's built this way

- **Phone-camera look, not cinema (deliberate Rule 2 break).** The whole
  charm of a vlog is that it looks shot on a phone. So instead of "ARRI +
  Panavision" we anchor to "ultrawide selfie framing, slight edge
  distortion, autofocus hunting." Using a cinema-lens anchor here would
  read as a polished ad and kill the authenticity. Match the camera
  anchor to the *genre*, not to a reflex.
- **Imperfection anchors double as the consistency lock (Rule 5).** Drool,
  matted ear, crumb on the snout — these keep it the *same* animal across
  the cutaway and back, the way emotional pet pieces stay one dog.
- **Lip-sync is explicit.** Talking-animal video fails most on a stiff
  puppet jaw or mismatched sync — call out "lip and jaw move in sync,
  natural not puppet" in the subject block and negate the failure modes.
- **Restrained close (Rule 6).** No paw-wave, no hearts, no subscribe
  graphic. The host simply losing the thread and flopping over is funnier
  and stops the model adding social-media UI overlays.

**Usage:** generate the *greeting* beat (0–3s) first to lock the talking
face and the voice; if the lip-sync and the breed read right there, the
cutaway and punchline will hold. Keep the bit short — one joke, one
collapse.

**Model:** Veo 3 and Sora 2 are strongest for synced spoken dialogue —
use one of them for the talking shots. Kling 3.0 supports multilingual
dialogue. Seedance 2.0 has native synced audio but verify the lip-sync
on the talking beats; cut away to B-roll if a take's sync drifts.
