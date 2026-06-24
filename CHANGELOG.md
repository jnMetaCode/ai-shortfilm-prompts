# Changelog

All notable changes to this project. This repo is a bilingual methodology
+ prompt library + Claude Code Skill for cinematic AI-video prompts.

## v0.4.0 — 2026-06-24

Big content + web round: from a few genres to a broad, searchable library.

### Added
- **14 new cinematic video-prompt genres** (bilingual EN/中文, 5-stage worked
  examples) — bringing the library to **17 genres**:
  product commercial, food ASMR, talking-animal vlog, movie trailer,
  cyberpunk city, claymation / stop-motion, nature timelapse,
  found-footage / CCTV horror, anime → live-action, music video,
  sports slow-motion, fashion film, travel vlog, drone / FPV.
- **Web showcase upgrade** (`docs/`, live at prompts.aiolaola.com):
  - Left-sidebar category layout (replaces top tabs).
  - **English mirror site** at `/en/` with bilingual `hreflang`.
  - **Static per-prompt pages (SSG)** via `scripts/generate_pages.py` —
    each prompt now renders into crawlable HTML with its own
    title/description/canonical/JSON-LD + copy button (62 pages).
  - `sitemap.xml` (65 URLs), `robots.txt`, JSON-LD (WebSite + HowTo),
    Open Graph cover image (`docs/assets/og-cover.png`).
  - Ecosystem nav links (aiOlaOla / AO / SP) with UTM attribution.
- Each genre teaches one distinct camera/technique lesson; SKILL template
  table and README kept in sync (EN + 中文).

### Fixed
- Viral-tab crash in the gallery (`render()` now handles non-section cats).
- Canonical / sitemap URLs aligned to Cloudflare's extensionless serving.
- `travel-vlog` intro montage-structure typo (`food` → `move`).

### Quality
- Multi-agent quality audit across all 17 genres (34 files): 7 hard rules,
  5-stage structure, EN/中文 parity, internal links, and IP-safety all pass.

## v0.3.1

- Skill files moved to `skills/shortfilm-prompt/` (plugin root) with a
  `.claude/skills/` symlink, fixing an empty marketplace install.

## v0.3.0

- Research-grounded upgrade: model table, machine-readable index, cheat
  sheet, negative-prompt prefab, failure-case gallery, dead-link CI.

## v0.2.0 · v0.1.0

- Initial methodology + prompt library + Claude Code Skill, built from
  Mx-Shell's *Zombie Scavenger* method.
