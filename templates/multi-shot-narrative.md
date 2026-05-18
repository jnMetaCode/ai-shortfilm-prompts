# Multi-Shot Narrative Template

> Source: organized from Mx-Shell's publicly shared prompt materials
> and Douyin livestream content (March/May 2026). This is the
> generalized skeleton extracted from *Zombie Scavenger*.
>
> Best for: edit-style shorts where an event is broken into N shots,
> each 5–8 seconds, then assembled into a coherent narrative.
>
> **[中文版 →](./multi-shot-narrative.zh.md)**

---

## Skeleton

```
[Character & scene setup]
  Subject 1 (Portrait1 reference): …
  Subject 2 (Portrait2 reference): …
  Scene (Portrait3 reference): …
  Sound: …

[Atmosphere & quality]
  Style core: …
  Visual base: …
  Color & tone: …

[Story content]
  Shot 1: shot size + composition + camera move + content
  Shot 2: …
  Shot 3: …
  …
```

Each shot has four required fields: **Shot size / Composition /
Camera move / Story content**.

---

## Vocabulary cheat sheet

### Shot sizes
- Extreme wide — establishes environment
- Wide — full body + significant context
- Medium — waist-up
- Close — chest-up
- Close-up — face, hands, props
- Long-lens close — compresses depth, distant intimate shot

### Composition
- Centered / symmetric
- Rule-of-thirds
- Diagonal
- Framing (using doorways, windows, body parts as frames)
- Foreground / midground / background layers (state what each layer is)
- Empty shot (no human subject in frame)
- Over-the-shoulder (foreground is one character's shoulder/back-of-head)

### Camera moves
- Locked-off
- Slow push-in / pull-out
- Follow tracking
- Orbit (clockwise / counter-clockwise)
- Handheld (with subtle floating)
- Lateral pan / tilt
- FPV (free-tilting frame)

### Story actions (use verbs, not adjectives)
- Enter / turn / step back / stand straight / squat
- Lower head / raise head / tilt head / stare
- Switch expression / defensive stance / combat ready

---

## Application example (robot + small animal + villa scenario)

```
[Character & scene setup]
Robot protagonist (Portrait1): {{Subject 1 description: build, style,
                                clothing, expression display method}}
Small animal (Portrait2): {{Subject 2 description: species, expression}}
Scene (Portrait3): {{Time of day, location, style, environment state,
                     atmosphere}}
Sound: No score. Production audio only.

[Atmosphere & quality]
Style core: {{3–5 tags: atom-punk / post-apocalyptic / cinematic /
             hyperreal / no game-CG feel}}
Visual base: Anamorphic widescreen cinematic. Simulated IMAX film camera
             paired with {{lens combo}} (motion blur added).
Color & tone: {{era / aesthetic}}, {{primary color scheme}}, film grain,
              retro wide-angle lens, low-saturation retro film LUT.
              {{Lighting description: natural side-light / hard light /
              volumetric fog ...}}
Visual base: Reference {{benchmark work}} aesthetic, {{specific style}}
             for character motion control.

[Story content]

Shot 1:
  Shot size: {{Medium / Close-up / ...}}
  Composition: {{Centered / Symmetric / Foreground-midground-background...}}
  Camera move: {{Locked / Tracking / Push-in / ...}}
  Story content: {{What subject does → what happens → subject's reaction}}

Shot 2:
  Shot size: …
  Composition: …
  Camera move: …
  Story content: …

(Add 3–8 shots as needed)
```

---

## Five high-yield multi-shot techniques

### 1. Empty shot + off-screen sound
```
Shot: Wide, level pan of the entire bar counter. Empty shot, bar
      occupies the lower third of frame.
Story content: A rustling noise comes from behind the counter, as if
               something is rummaging beneath it.
```
**Use it for**: a shot with no protagonist + off-screen sound establishes
"unseen threat" tension faster than any visible monster.

### 2. Over-the-shoulder close-up (establishes mutual gaze between two subjects)
```
Shot: Long-lens, over-the-shoulder.
Composition: Robot in mid-ground left, foreground is ostrich's
             back-of-head on the right. Focus on robot, producing
             shallow depth of field.
Camera move: Locked-off.
Story content: Ostrich rises rapidly with back to camera, head pops up
               from below frame, surveys the robot. Robot startles
               again, covers face with both hands, daring not look.
```
**Use it for**: when two characters confront each other, an OTS captures
both subjects in one shot — tension reads higher than cutting back and
forth between two close-ups.

### 3. Expression switch as a shot's endpoint
```
Shot: Long-lens close-up, robot side-45° face.
Story content: Robot's LED face switches from yellow-frightened to
               white-thinking expression.
```
**Use it for**: a whole shot can be just an emotional shift. The
expression switch = the thought process, the inner monologue when
there's no dialogue.

### 4. Cuts + tracking + scene changes (great for MV-style segments)
```
Story content: Robot dances all over the location (poolside, second-
               floor corridor, on a lounger, on the roof). Tracking
               camera, auto-composition, jump-cut between shots,
               location changes, with foot close-ups (back-slide
               moonwalk) interspersed.
```
**Use it for**: MV/montage doesn't need every shot meticulously
designed. Give the AI permission to jump-cut, but lock the motion
style strictly (*"1980s-style breakdance moves"*).

### 5. Production audio enumerated
Always include:
```
Sound: No score. Production audio only.
```
For scenes with signature ambient sounds, enumerate them explicitly:
glass breaking, footsteps on debris, distant zombie growls, ocean
waves, wind through broken windows. Don't make the AI guess.

---

## Debugging tips

1. **Test 2–3 shots first to check texture**, don't lay out all 7 shots
   upfront.
2. **Motion direction between shots must rhyme** — if previous shot
   has subject moving right, next shot subject should enter from left.
3. **Generate each shot independently for 5–10s**. Stitch with
   transitions in post. One-shot 30s+ generation has terrible
   reroll-success rate.
4. **Portrait numbering must be stable**: Portrait1 always the
   protagonist, Portrait2 always the animal — don't swap mid-project.
