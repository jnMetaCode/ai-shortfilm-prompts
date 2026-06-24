# CLAUDE.md

Conventions for working in this repo. Read before editing.

## What this repo is

A bilingual (EN/中文) methodology + prompt library + Claude Code Skill for
writing cinematic AI-video prompts, built from Mx-Shell's *Zombie Scavenger*
method. Pure docs + one Skill, no build step. Two CI checks: a dead-link
scan (`.github/workflows/links.yml`) and LLM-judge skill evals
(`.github/workflows/evals.yml` + `evals/`, needs the `ANTHROPIC_API_KEY` secret).

## Hard conventions

1. **File paths must be ASCII.** No Chinese filenames. Chinese content goes
   in `*.zh.md` files. (Internal links broke twice before because docs linked
   to Chinese paths like `方法论.md` that don't exist — the real file is
   `methodology.zh.md`.)

2. **Keep EN/中文 pairs in sync.** `methodology`, `faq`, `credits`, `NOTICE`,
   and `templates/*` each have an English file and a `.zh.md` (or `.zh`)
   sibling. Edit both, or note the divergence.

3. **The Skill: `SKILL.md` (English) is what Claude Code loads and executes.**
   `SKILL.zh.md` is a human reference translation — keep it at parity when you
   change the rules, but the English file is canonical.
   **Real skill files live at `skills/shortfilm-prompt/` (plugin root), NOT
   `.claude/skills/`.** A plugin only discovers skills under
   `<plugin-root>/skills/`; the old `.claude/skills/` path made the marketplace
   install ship an empty plugin (fixed in v0.3.1). `.claude/skills/shortfilm-prompt`
   is a **symlink → `../../skills/shortfilm-prompt`** so a bare in-repo `claude`
   still auto-discovers it as a project skill — single source of truth, two entry
   points. Don't move the real files back, don't delete the symlink, don't
   duplicate. (links.yml does NOT glob `.claude/**` so it won't double-scan the
   symlink with a wrong relative base.)

4. **After editing any internal link, run a dead-link check** across all
   `*.md` before committing. This has bitten us repeatedly.

5. **X/tweet `status` links point to the maintainer's own tweet**
   (`x.com/aibuzhiyu/status/2056426660577288645`), NOT PJ Ace's original —
   this is deliberate (don't drive traffic away). The `@PJaccetturo` *handle*
   still links to his profile as attribution. The `13.4M views` stats table
   has a footnote crediting PJ Ace's tweet. Don't "fix" these back.

## Licensing boundary (don't blur it)

- **jnMetaCode's work** — methodology, FAQ, templates, the Skill, metadata,
  `assets/demo-prompt.md` — is **MIT**.
- **Mx-Shell's original material** in `prompts/` (his actual prompts, doc
  excerpts) is **© Mx-Shell, all rights reserved**, archived for educational
  reference. See `NOTICE`. Don't relicense it as MIT.

## Do not commit

`资料/` (Mx-Shell's raw docx + livestream video + screenshots) and `教程/`
(channel-exclusive distribution articles) are **gitignored on purpose** —
copyright-sensitive + channel exclusivity. Don't add them to git. The repo
ships only structured, original documentation.

## Releasing

Bump `version` in both `.claude-plugin/plugin.json` and
`.claude-plugin/marketplace.json`, then tag + `gh release create`. Current: v0.4.0.
Log notable changes in `CHANGELOG.md`. When adding/removing a web prompt,
re-run `python3 scripts/generate_pages.py` (regenerates `docs/p/` + sitemap).
