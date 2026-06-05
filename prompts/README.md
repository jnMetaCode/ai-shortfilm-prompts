# Mx-Shell's Original Prompts — Archive

> **All files in this directory are Mx-Shell's original Chinese
> prompts**, kept untranslated to preserve his authorial voice and
> rights of attribution. Each file has an English header at the top
> explaining what the work is.
>
> **Sources**: All content was sourced from Mx-Shell's voluntary
> public distribution via two channels:
> 1. Prompt documents he shared in his fan group
>    (`mx-shell prompts + Q&A *.docx`)
> 2. His public Douyin livestream on May 12, 2026
>
> See [../credits.md](../credits.md) for full source attribution and
> his stated consent.

---

## Index

At-a-glance table of every prompt in this archive. Machine-readable
version: [index.json](./index.json).

| Prompt | Type | Duration | Variants | IP-safe | Rerolls |
|---|---|---|---|---|---|
| [Zombie Scavenger](./zombie-scavenger.md) ⭐ | multi-shot-narrative | two complete shot sequences | 1 | contains IP names | ~400 images + 200+ shots → ~40 clips (project-wide) |
| [Kamen Rider / Tokusatsu](./kamen-rider-transformations.md) ⭐ | transformation | 15s per shot (one-take) | 6 | contains IP names | highly variable (2-3 low, 20+ high) |
| [Kai'Sa (LoL)](./kaisa-transformation.md) | transformation | 15s + 20s + 5s extension | 3 | contains IP names | n/a |
| [Metal Gear charge + combat](./metal-gear-charge-combat.md) | charge-combat | charge 10-15s + combat 15s | 1 | contains IP names | extremely low one-shot success; assembled in post |
| [Pacific Rim + Gundam](./pacific-rim-gundam.md) | mech-drop | 15s (one-shot) | 1 | contains IP names | high breakdown rate; instruction non-compliance common |
| [Cyber Wuxia skeleton](./cyber-wuxia.md) | atmospheric | variable (template only) | 1 | safe | n/a |

> **IP-safe?** "contains IP names" means the original prompt names real
> franchises/characters that **Seedance 2.0 will block** — see
> [A note on IP names](#a-note-on-ip-names) below for how to strip them.
> "safe" means the prompt is already a generalized style skeleton.

---

## 1. Narrative (multi-shot edited)

- **[zombie-scavenger.md](./zombie-scavenger.md)** ⭐
  *Zombie Scavenger* — the work PJ Ace called "one of the best short
  films in recent years." Atompunk robot in a post-apocalyptic
  beachfront villa meets a confused ostrich, dances Michael Jackson
  moves. Two complete shot sequences.

## 2. Transformations (single-shot, one-take)

- **[kamen-rider-transformations.md](./kamen-rider-transformations.md)** ⭐
  Six Kamen Rider variants (five riders + a flight version) sharing one 5-stage template:
  - Cockroach Rider (HENSHIN, dark red crystal)
  - Fire Demon (flame crown horns)
  - Thunder Dragon (AMAZONS, dark blue crystal)
  - Rainbow Elk (male elk antlers)
  - Violet Hawk Valkyrie (Korean 변신, dark purple crystal)
  - Violet Hawk Valkyrie — flight version

- **[kaisa-transformation.md](./kaisa-transformation.md)**
  League of Legends Kai'Sa, three versions:
  - 15-second per-shot version (5 shots)
  - 20-second per-shot version (4 phases, with fear-buildup)
  - 5-second extension (flight + 8-missile barrage)

## 3. Heavy mecha

- **[pacific-rim-gundam.md](./pacific-rim-gundam.md)**
  Airship dive → virtual gauntlet → digital-cube mech assembly →
  ocean slam → kaiju reveal. 8 shots, FPV camera work.

## 4. Style templates (character + scene skeleton)

- **[cyber-wuxia.md](./cyber-wuxia.md)**
  Shaw Brothers + steampunk + wuxia look skeleton. Ming-dynasty
  eunuch / cybernetic prosthetics / candlelit courtyard. **Story
  content left blank — fill in your own.**

## 5. Combat composites (weapon-charge + combat)

- **[metal-gear-charge-combat.md](./metal-gear-charge-combat.md)**
  Weapon-charge segment + combat segment. Plus 4 reference-image
  prompts for scene / monster / weapon / power armor. Post-edited
  composite.

---

## How to use this archive

1. **Beginner**: Start with [zombie-scavenger.md](./zombie-scavenger.md)
   alongside [../methodology.md](../methodology.md). See how the
   5-stage template maps to a concrete piece.
2. **Want to make a transformation**:
   [kamen-rider-transformations.md](./kamen-rider-transformations.md)
   shows all six variants at once — it's more illustrative of
   "what's a variable vs. what's a constant" than reading the
   template alone.
3. **Want to make combat / longer pieces**:
   [kaisa-transformation.md](./kaisa-transformation.md) +
   [metal-gear-charge-combat.md](./metal-gear-charge-combat.md)
   demonstrate the standard "segmented generation + post-editing"
   workflow.
4. **Want a static-atmosphere / poster**:
   [cyber-wuxia.md](./cyber-wuxia.md) is a clean look skeleton.

---

## A note on IP names

The original prompts contain some IP names:

- 仮面ライダー BLACK SUN (Kamen Rider BLACK SUN)
- Gundam
- Pacific Rim
- Ready Player One
- Metal Gear Solid
- Kai'Sa (LoL)
- Iron Man
- Michael Jackson (referenced for dance style)

**Seedance 2.0 will block these.** From the original author:
> "Replace film/character names in the prompt, or delete some
> characters / punctuation without changing meaning."

The [../templates/](../templates/) directory provides IP-stripped
generalized versions ready to use.
