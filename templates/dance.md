# Worked Example — Dance / Choreography Film

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to a **dance film** — the counterpoint to
> [music-video.md](./music-video.md): an MV is built from *cuts*, a dance
> film holds on the *body in continuous motion*. Teaches full-body capture,
> body-to-beat sync, and the discipline of not cropping the movement.
>
> Concept: a solo contemporary dancer in an empty hall, one flowing take.
> Swap the style and space, keep the continuous-body rule.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): performance/dance patterns in
> [jax-explorer/awesome-veo3-videos](https://github.com/jax-explorer/awesome-veo3-videos)
> (no license — inspiration only).*
>
> **[中文版 →](./dance.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{dancer}}` | a solo contemporary dancer | a street/hip-hop crew / a ballet duo |
| `{{style_tempo}}` | fluid contemporary, ~90 BPM, building | krump ~150 / waltz ~84 / breaking ~110 |
| `{{space}}` | an empty sunlit concrete hall | a rooftop at dusk / a black stage / a street |
| `{{move}}` | a spiralling floor-to-rise phrase | a freeze-and-pop combo / a leap sequence |
| `{{grade}}` | warm hard window light, long shadows | single-spot chiaroscuro / cool daylight |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`dance film | full-body continuous motion | body synced to rhythm | one bold grade | real physical motion, no stiff mocap look, no choppy cuts`

### 2 · Character & scene

**Dancer:** {{dancer}}. Reference uploaded photo, features 100% preserved,
no beautification. The realism is in the effort: sweat, hard breathing,
muscle strain and control, hair and loose clothing moving with momentum,
a bare foot scuffing the floor. Real physical motion with weight — not a
weightless stiff mocap puppet.

**Scene:** {{space}}, {{grade}}. The light and floor are part of the
choreography — shadows move with the body.

### 3 · Atmosphere & quality
Shot on ARRI Alexa with anamorphic primes, bold {{grade}}. Film grain,
real practical light, motion blur allowed on fast limbs. One committed
look. Frame to keep the **whole body** readable — dance lives in the full
figure, not in tight crops.

### 4 · Camera rules
**One continuous flowing take** that follows the body — an orbit, a track,
a slow push that keeps {{dancer}} whole in frame. The opposite of an MV's
fast cuts: let the movement play.
- *Breathing:* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence." — alive, moving with the
  dancer, but never cropping the motion.
- *Sound (music IS wanted, like an MV):* this genre rides a track. Specify
  {{style_tempo}} so the body's motion locks to the beat. Production audio
  underneath — breath, foot scuffs, fabric. If you have the track, generate
  to temp and lay the real song in post.

### 5 · Storyboard (one continuous take, ~12s)

```
0–3s · Entry (establish body + space)
Action: {{dancer}} begins, still then moving, the {{grade}} light defining
        the figure in {{space}}.
Camera: Slow push/orbit, full body in frame.
Beat:   Movement initiates on the downbeat.

3–9s · The phrase ({{move}} — the body's argument)
Action: {{move}} plays out continuously — momentum, weight, control,
        sweat and breath, shadows sweeping with the body.
Camera: One flowing follow — orbit/track — never cutting away, never
        cropping out the limbs at the key moment.
Beat:   The motion accents land with the rhythm.

9–12s · Resolve (restrained close)
Action: The phrase resolves; {{dancer}} settles, chest heaving.
Camera: Hold, breath-float, full figure.
Close:  No freeze-frame pose-to-camera, no logo, no flashy spin. Just the
        dancer breathing in the light where the movement ended.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, watermark, text overlay, subtitles, logo, stiff mocap motion, weightless floaty movement, robotic interpolation, choppy cuts mid-move, cropped-out limbs, plastic CG skin, glossy idol render, video-game look, 3D cartoon, flat even studio lighting, distorted face, extra fingers, bent/broken joints, melting/morphing limbs, frame flicker, ghosting, lifeless locked-off camera
```

---

## Why it's built this way

- **Continuous body, not cuts (the dance/MV split).** An MV chops to the
  beat; a dance film holds on the body so the movement reads. Build it as
  one flowing take that keeps the whole figure in frame — cutting away or
  cropping the limbs at the key moment kills it.
- **Weight and effort (Rule 5).** Sweat, breath, muscle control, a
  scuffing foot, clothing carrying momentum. Weightless stiff motion reads
  as mocap; the physical weight is what makes dance real.
- **Music is the rhythm (Rule 4, like the MV).** Dance is built on a track —
  specify tempo so the body syncs. Lay your real song in post.
- **Restrained close (Rule 6).** Dancer breathing where the move ended, not
  a pose-to-camera freeze. The exhaustion is more real than a wink.

**Usage:** generate the *phrase* beat (3–9s) first — if the body moves with
real weight and stays whole in frame (no cropped limbs, no mocap stiffness),
the entry and resolve frame it. Keep it one continuous move.

**Model:** Kling is excellent at full-body human motion; Veo 3 and Sora 2
give strong realism + native music handling. Watch for bent/broken joints
and limb morphing on fast moves — negate them and keep the body framed whole.
