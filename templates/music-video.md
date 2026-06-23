# Worked Example — Music Video / Performance (beat-synced)

> Original worked example by jnMetaCode (MIT). Applies the 5-stage
> structure to a **music video** — and it's the deliberate counterpoint to
> [movie-trailer.md](./movie-trailer.md): the trailer bans a music bed and
> designs sound; the MV is the one genre where **the track IS the point**.
> This template teaches when to *want* music and how to cut to a beat.
>
> Concept: a single performer in a stylised space, cut to a track's
> rhythm. Swap the artist, look, and tempo; keep the beat-sync discipline.
>
> *Further reading (inspiration, not copied — all rewritten in our
> structure): performance / music categories in
> [jax-explorer/awesome-veo3-videos](https://github.com/jax-explorer/awesome-veo3-videos)
> (no license — inspiration only) and audio-sync notes in
> [geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts)
> (MIT).*
>
> **[中文版 →](./music-video.zh.md)**

---

## Variables you need to define first

| Variable | This example | Swap for… |
|---|---|---|
| `{{artist}}` | a solo singer | a band / a dancer / an instrumentalist |
| `{{genre_tempo}}` | dreamy synth-pop, ~100 BPM, mid-energy | trap ~140 / ballad ~70 / hyperpop ~160 |
| `{{look}}` | neon-lit rain on a rooftop at night | a white cyclorama / a desert at golden hour |
| `{{grade}}` | magenta + cyan neon over deep blue | high-key pastel / warm film |
| `{{hook_moment}}` | the chorus drop at ~4s | the beat the whole edit builds to |

---

## The complete prompt (copy-paste ready)

### 1 · Core theme
`music video | beat-synced multi-shot | one bold grade | performance energy | no karaoke literalism, no random unmotivated cuts`

### 2 · Character & scene

**Performer:** {{artist}}. Reference uploaded photo, features 100%
preserved, no beautification. Real performance energy — sweat, breath,
motion blur on fast moves, a stray hair stuck to the face. Imperfections
keep it a real performance, not a polished CG idol.

**Scene:** {{look}}, built around {{grade}}. The space reacts to the music
— lights pulse, rain catches the beat, reflections move.

### 3 · Atmosphere & quality
Shot on Sony Venice with anamorphic primes; bold stylised grade in
{{grade}} (an MV can push colour harder than a narrative film). Film grain,
real neon/practical light, motion blur allowed on fast moves. One
committed look across the whole piece.

### 4 · Camera rules
Edited multi-shot **cut to the beat** — holds on the verse, faster cuts
into {{hook_moment}}, a camera move that lands on the downbeat.
- *Breathing:* "Handheld shot. Throughout, maintain an extremely subtle,
  breath-like camera float to enhance presence." — here it can ride the
  rhythm, a touch more alive than a narrative shot.
- *Sound (the exception — music IS wanted):* unlike every other template
  here, this genre is built ON a track. Specify **tempo, genre and energy**
  ({{genre_tempo}}) so the model's motion and cuts lock to the beat. If you
  have your own track, generate to silence/temp and lay the real song in
  post. Avoid letting the model fabricate lyrics/vocals unless you want
  them.

### 5 · Storyboard (beat-synced, ~12s)

```
0–4s · Intro / verse (let it breathe)
Action: {{artist}} in {{look}}, mid-performance, {{grade}} establishing.
        Slower, longer holds matching the verse.
Camera: Slow push or a single slow arc. Breath-float.
Beat:   Cuts land on the downbeats, sparse.

4–8s · Hook / drop ({{hook_moment}} — the payoff)
Action: Energy lifts — the performer hits the chorus, the space reacts
        (lights pulse, rain bursts), motion sharpens.
Camera: Faster cuts, a move that lands hard on the drop.
Beat:   Cut rhythm doubles into the hook.

8–12s · Outro (restrained close)
Action: Energy settles back; one last held performance frame.
Camera: Hold, breath-float.
Close:  No lyric text on screen, no logo card, no freeze-frame wink. Just
        the performer and the space coming to rest as the phrase ends.
```

### Negative prompt (Seedance / Kling — paste into the dedicated field)
```
blurry, low resolution, watermark, text overlay, lyric subtitles, logo, karaoke text, distorted face, asymmetric eyes, extra fingers, deformed hands, lip-sync mismatch, plastic CG skin, glossy idol render, video-game look, 3D cartoon, flat even studio lighting, grade shifting randomly between shots, unmotivated epileptic cuts, frame flicker, ghosting, lifeless locked-off camera
```

---

## Why it's built this way

- **The one place music IS the point (Rule 4 inverted).** Every other
  template says "No score. Production audio only." An MV is the exception —
  it's built on a track. So we specify tempo/genre/energy so motion and
  cuts sync, and (the counterpoint to the trailer) we *want* the music
  rather than banning it.
- **Cut to the beat, not at random.** The difference between an MV and a
  random montage is that cuts and camera moves land on the downbeat and
  the edit accelerates into the hook. Map the storyboard to the song's
  structure (verse → hook → outro), not to clock seconds alone.
- **One bold grade (Rule 1, MV dialect).** An MV can push colour harder
  than a narrative film — but still *one* committed look, not a different
  filter per cut.
- **Performance imperfections (Rule 5) + restrained close (Rule 6).**
  Sweat, breath, motion blur keep it a real performance; ending on a
  settling frame (not a lyric card or logo) keeps it cinematic.

**Usage:** decide the track's structure first, then map cuts to it —
generate the *hook* beat first since it's the payoff. If you have a real
song, generate to temp/silence and sync the real track in post. Keep
performers' faces consistent across cuts (generate the hook frame first to
lock the look).

**Model:** Veo 3 and Sora 2 handle performance motion and (if you want it)
native audio best; Kling 3.0 is strong on rhythmic action and multilingual
dialogue. For real lip-sync to your own track, lay it in post rather than
trusting generated vocals.
