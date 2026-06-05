# Cheatsheet — One-Page Quick Reference

> Keep this open while you write. Full version: [methodology.md](./methodology.md)
> · Skill: [SKILL.md](./skills/shortfilm-prompt/SKILL.md)
>
> **[中文版 →](./cheatsheet.zh.md)**

---

## The 5-stage skeleton

```
1. Core theme           3-6 style tags, | -separated. Shot type → genre → aesthetic.
2. Character & scene     Face / Clothing / Scene. "No beautification." Material first. Moving background.
3. Atmosphere & look     Real camera + lens model. Color tone. Style core. Sound line.
4. Camera rules          Single-shot / Angle (size+angle+motion) / Breathing line.
5. Storyboard            Per-second slices (one-take) OR per-shot slices (multi-shot edit).
```

- **Style A · per-second** (transformation, weapon-charge, one-take): `Action + Camera + VFX` per slice. Add-ons: Sound, Face.
- **Style B · per-shot** (narrative, MV): `Shot size + Composition + Camera move + Action` per shot.

---

## 3 counter-intuitive rules

1. **No reference image unless it's high-quality.** AI mimics the reference's *art style* (CG/anime look), not its *design*. Free-form from text descriptions. Exception: photoreal 3D renders / true live-action photos.
2. **Describe flaws = describe reality.** Too perfect = fake. `battle damage` / `paint worn off` / `oil in joints` / `preserve minor facial blemishes`. Need **≥2** imperfections per character/equipment block.
3. **Rerolls are normal — leave the ending empty.** 2-3 to 20+ rerolls per shot is expected. Don't aim for first-try perfection. Don't pile FX on the close.

---

## Camera + lens lookup

| Aesthetic | Camera + lens |
|---|---|
| Epic / big-scene | IMAX film camera + Panavision C-series (35mm, f/4) |
| Gritty cyber / hard sci-fi | Sony Venice + Canon K-35 series |
| Hong Kong noir / wuxia | Kodak 35mm vintage film, bleach-bypass |
| Commercial portrait | Canon EF 85mm f/1.2 |

**Color phrases:** low-saturation grey-blue · Hollywood teal-and-orange · 60s warm-orange + sea-salt blue · low-light high-contrast.

---

## Two lines to paste verbatim

**Breathing** (almost every prompt — both qualifiers are essential, or the AI reads it as heavy shake):

> Handheld shot. Throughout, maintain an extremely subtle, breath-like camera float to enhance presence.

**Sound** (or the AI fabricates music):

```
Sound: No score. Production audio only.
```

For scenes with signature ambient sound, enumerate it (rain, thunder, metal scrape, low-frequency hum). Don't make the AI guess.

---

## Empty-ending template

Don't write: blinding light / explosion / victory pose / leap into sky / camera blow-out. Restraint reads more elevated than excess.

> No dialogue. No explosion. No blinding light. Just {{subject}} {{action}}, {{environment detail}}.

Example: *"Just a figure in unfinished battle-armor standing in place. Wind carries battlefield smoke. A meteor crosses the distant sky."*

---

## Pre-delivery checklist

- [ ] All 5 stages present
- [ ] Camera + lens model named
- [ ] Full "breath-like float" sentence verbatim
- [ ] `Sound: No score. Production audio only.`
- [ ] ≥2 imperfection descriptions
- [ ] Closing is empty / restrained — no FX pile-up
- [ ] No vague praise words (perfect / stunning / epic / handsome / 4K / texture-rich)
- [ ] No IP names (or warning line added)
- [ ] Single-shot ≤ 15s · multi-shot ≤ 8 shots
- [ ] Model advice line included (Seedance/Xiaoyunque: no IP names + strict filter; Sora: concise prompts; Kling: strict banned-word filter — sanitize IP terms first, needs explicit motion; Veo: English preferred)
