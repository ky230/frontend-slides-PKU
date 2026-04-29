---
name: PKU Color Skins
description: 9 curated + 1 DIY color skin for PKU Academic Classic. Override :root variables to change header/footer, background, text, and accent colors.
---

# PKU Color Skins Reference

> **Usage**: `python3 init-slides.py --skin <name>` injects the skin CSS into the template.
> Default `classic` = PKU Red-Yellow-White (no overrides).

---

## Quick Reference

| # | Skin | Category | `--theme-primary` | `--theme-bg` | `--theme-text` | Font |
|---|------|----------|-------------------|-------------|---------------|------|
| 00 | **classic** (default) | — | `#cc0000` | `#fefefc` | `#1a1a1a` | Times New Roman |
| 01 | **bold** | 🌑 | `#FF5722` | `#2d2d2d` | `#ffffff` | Space Grotesk |
| 02 | **cobalt** | ☀️ | `#4361ee` | `#f7f0f0` | `#0a0a0a` | Manrope |
| 03 | **voltage** | 🌑 | `#0066ff` | `#1a1a2e` | `#ffffff` | Manrope |
| 04 | **botanical** | 🌑 | `#d4a574` | `#0f0f0f` | `#e8e4df` | IBM Plex Sans |
| 06 | **jade** | ☀️ | `#2ca657` | `#fdfdfc` | `#1a1a1a` | Plus Jakarta Sans |
| 07 | **lavender** | ☀️ | `#9171a6` | `#eee1d8` | `#1a1a1a` | Outfit |
| 09 | **cyber** | ✨ | `#00ffcc` | `#0a0f1c` | `#e0e0e0` | Satoshi |
| 10 | **terminal** | ✨ | `#39d353` | `#0d1117` | `#c9d1d9` | JetBrains Mono |
| — | **diy** | 🎨 | User-defined | User-defined | User-defined | User-defined |




---

## How It Works

Each skin is a CSS file in `assets/skins/<name>.css` that overrides `:root` variables:

```css
:root {
    --theme-primary: #...;   /* Header, footer, bullets, accent borders */
    --theme-accent:  #...;   /* Title highlight, progress bar */
    --theme-bg:      #...;   /* Slide background */
    --theme-text:    #...;   /* Body text color */
    --font-body:     '...';  /* Body font family */
}
```

Skins may also override:
- `.slide` background (gradients, patterns)
- `.title-banner h1` / `.transition-text` font-family
- `table` colors for dark themes
- `a` link color
- `.global-header` / `.global-footer` effects

**HTML structure is never changed.** Skins are pure CSS overrides.

---

## Notes

- Dark skins (01, 03, 04, 09, 10) include table/link color adjustments for readability
- MathJax SVG inherits `color` — works on both light and dark backgrounds
- Logo images have `background-color: white` in base template — visible on dark backgrounds
- Each CSS file has a comment `/* Google Fonts: ... */` parsed by `init-slides.py` to auto-inject `<link>` tags
- For Fontshare fonts (cyber), a `/* Fontshare: ... */` comment is used instead
- **DIY skin**: `cp assets/skins/diy.css.example assets/skins/diy.css` — fully annotated template, not git-tracked
