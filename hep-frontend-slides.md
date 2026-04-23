---
name: hep-frontend-slides
description: 🎨 HTML Slides 制作专家 — 使用 frontend-slides 技能创建零依赖、动画丰富的 HTML 演示文稿。支持从零创建、PPT 转换、风格探索。适用于组会汇报、conference talk、pitch deck 等场景。
---

# Frontend Slides — HTML Presentation Maker

Create zero-dependency, animation-rich HTML presentations that run entirely in the browser.

**Activate:** `/hep-frontend-slides` or describe "make slides / create presentation / convert PPT".

---

## HARD-STOP (violating any = restart immediately)

> **DO NOT write temporary Python scripts.** Creating `/tmp/build_slides.py` or ANY `.py` to generate/assemble HTML is FORBIDDEN. The ONLY scripts you may run are the repo's own `init-slides.py` and `bundle-html.py`.

> **DO NOT auto-bundle.** `bundle-html.py` may ONLY run when the **user explicitly says `bundle` / `deliver` / `pack`**. After content injection, ask "Ready to bundle?" and WAIT. NEVER bundle on your own.

> **DO NOT hand-write HTML skeletons.** In PKU mode, all CSS/JS/Logo/Header/Footer come from `init-slides.py` + the empty template. You ONLY inject content into placeholder pages.

---

## Skill Files

**Read first:** `{{FRONTEND_SLIDES_REPO_PATH}}/SKILL.md` (full 6-phase workflow for Free mode).

### Support Files (load on demand)

| File | Purpose | When |
|------|---------|------|
| `reference/STYLE_PRESETS.md` | 12 curated visual presets | Phase 2: style selection |
| `reference/viewport-base.css` | Mandatory responsive CSS for Free mode | Phase 3: generation |
| `reference/html-template.md` | HTML structure, JS features, quality standards | Phase 3: generation |
| `reference/animation-patterns.md` | CSS/JS animation snippets | Phase 3: generation |
| `reference/PKU_ACADEMIC_CLASSIC.md` | PKU template full spec (CSS/JS/Logo) | PKU mode activation |
| `reference/FIGURE_LAYOUTS.md` | Figure Layout System: 16 presets + 5 knobs | PKU mode: image-heavy slides |
| `scripts/bundle-html.py` | Embed local images as base64 | **User says `bundle` only** |
| `scripts/extract-pptx.py` | PPT content extraction | **User provides `.pptx`** |
| `scripts/deploy.sh` | Deploy to Vercel | **User says `deploy`** |
| `scripts/export-pdf.sh` | Export to PDF | **User says `export PDF`** |

All paths relative to: `{{FRONTEND_SLIDES_REPO_PATH}}/`

---

## Mode Selection

When the user says "make slides" without specifying a template, **ask**:

> 1. 🏛️ **PKU Academic Classic** — group meeting / academic report (red-yellow, dual Logo, fixed layout)
> 2. ⚡️ **Free** — free style (12 presets, responsive, for pitch / tech talk / creative)

**PKU triggers:** "PKU template" / "academic slides" / "group meeting slides" / "CMS slides" / "CEPC slides"
**Free triggers:** "free style" / "pitch deck" / "tech talk" / "creative slides" / explicit refusal of PKU

---

## 🏛️ PKU Academic Classic Mode

### Pre-requisite

Read the full style spec: `{{FRONTEND_SLIDES_REPO_PATH}}/reference/PKU_ACADEMIC_CLASSIC.md`

> **Token Explosion Prevention:** Logos are stored as real images in `{{FRONTEND_SLIDES_REPO_PATH}}/assets/`. NEVER output Base64 logo data in specs, memory, or AI-generated content.
> `init-slides.py` auto-converts `src="assets/..."` to **repo absolute paths** so logos render from any output directory via `file://`.
> User content images (plots/figures) must use **relative paths only** (e.g., `<img src="attachments/plot.png">`).
> `bundle-html.py` converts ALL images (logos + user images) to base64 at delivery time.

> **Step numbers below are PKU-mode specific and unrelated to SKILL.md Phase numbers.**

### Step 1: Brand Selection + Mandatory Pre-flight Q&A

Pre-flight questions are defined in `reference/PKU_ACADEMIC_CLASSIC.md` §0 (Q0–Q9). Complete ALL before generating any HTML.

### Step 2: Generate (strictly per PKU_ACADEMIC_CLASSIC.md spec)

> PKU mode uses fixed 1920×1080 canvas + JS `applyScale()`. Ignore SKILL.md's `viewport-base.css` / `clamp()` / `100vh` rules entirely.

Strictly follow the spec for: CSS (copy verbatim), JS (copy verbatim), title slide format, outline page, transition pages (must match outline order), content pages (`data-title` = nearest transition title), bullet hierarchy (L1 red disc / L2 red dash / L3 numbered), MathJax LaTeX, highlight boxes (`.highlight-box` / `.important-box` / `.warning-box` / `.tip-box`), footer-center = Q4 speaker name.

### Step 3: Fine Tuning

> Fine Tuning MUST happen BEFORE `bundle-html.py`. Bundle is the delivery seal; editing after bundle means fighting base64 data.

**Triggers:** "fine tuning" / "adjust" / "fix slide X"

**Protocol:**
1. **Receive feedback** — User specifies changes per slide (e.g., "Slide 4: title too small, make 1.1em")
2. **Locate** — `grep_search` for `<!-- [Slide N] -->`, then `view_file` that range. Do NOT modify slide comment markers.
3. **Execute** — Use `replace_file_content` for surgical edits. All changes must comply with `PKU_ACADEMIC_CLASSIC.md`.
4. **Structural changes** (insert/delete slides) — After the operation, **re-number ALL subsequent `<!-- [Slide N] -->` markers** to maintain strict sequential order. Report new total.

| Category | Example | Re-bundle? |
|----------|---------|:---:|
| Typography / spacing | Font size, bold, color, alignment, gap | ❌ |
| Content edits | Wording, bullets, data corrections | ❌ |
| Box class swap | `highlight-box` ↔ `important-box` | ❌ |
| Insert / delete slide | Add slide between 5 and 6 | ❌ |
| **New local image** | Add a new plot reference | ✅ |

**Exit Fine Tuning:** When user says `bundle` / `deliver`, run `bundle-html.py` and report completion.

---

## ⚡️ Free Mode

Fully delegated to `{{FRONTEND_SLIDES_REPO_PATH}}/SKILL.md` (6-phase workflow: detect → content → style → generate → deliver → share).

> Free mode uses `reference/viewport-base.css` + `clamp()` responsive system. Do NOT mix with PKU's fixed 1920×1080 canvas.

| Dimension | PKU Academic | Free |
|-----------|-------------|------|
| Layout | Fixed 1920×1080 + JS scaling | `100vh` + `clamp()` responsive |
| Font | Times New Roman | Per-preset font pairs |
| Skeleton | `init-slides.py` scaffold | AI generates full HTML directly |
| Style | Single (red-yellow classic) | 12 presets |
| Logo | PKU + CMS/CEPC | None built-in |

`bundle-html.py` and Fine Tuning are **shared capabilities** across both modes.

---

## 🔧 PKU Batch Generation Rules (NON-NEGOTIABLE)

> These rules apply to PKU Academic Classic mode ONLY. Free mode generates HTML directly without `init-slides.py`.

### Rule 1: Batch 0 — Scaffold via init-slides.py

**DO NOT hand-write the HTML skeleton.** Run the scaffold script:

```bash
python3 {{FRONTEND_SLIDES_REPO_PATH}}/scripts/init-slides.py \
  --template CMS \
  --title "Report Title" \
  --subtitle "Optional Subtitle" \
  --author "Author1:1, Author2:2" \
  --speaker "Author1" \
  --affiliations "Peking University (CN)" "Sapienza (IT)" \
  --date "Mar 20th 2026" \
  --event "TB meeting" \
  --highlight "keyword1" "keyword2" \
  --outline "Section 1:2" "Section 2:4" "Back Up:1" \
  --out /path/to/output.html
```

The script auto-generates: template copy, footer substitution, title slide (with `--highlight` keywords wrapped in `.highlight-yellow`), outline, transition + content placeholder pages, `<!-- [Slide N] -->` markers.

**After scaffold, AI tasks are LIMITED to:**
1. Replace placeholder content via `replace_file_content`
2. Insert additional pages before `<!-- END slides-scroller -->`
3. **Ask the user:** "Content injection complete. Fine Tune or bundle?" **WAIT for user response. DO NOT auto-bundle.**

### Rule 2: No Temporary Scripts (see HARD-STOP)

❌ No `/tmp/*.py` scripts to build HTML. ❌ No regex extraction from `.md` specs.
✅ Write slide content directly via `write_to_file` / `replace_file_content`.
✅ Only allowed scripts: `init-slides.py` (scaffold) and `bundle-html.py` (embed).

### Rule 3: Slide Comment Markers

Every `<section>` MUST be preceded by `<!-- [Slide N] Type: Title -->`. The scroller container MUST end with `<!-- END slides-scroller -->`. New slides are inserted before this marker.

---

## 📦 Asset Bundling (NON-NEGOTIABLE)

All delivered HTML files must be fully self-contained — zero path dependencies, all images base64-embedded.

**When user says `bundle` / `deliver`:**

```bash
python3 {{FRONTEND_SLIDES_REPO_PATH}}/scripts/bundle-html.py <input.html> <output.html>
# For in-place: use same path for both arguments
```

The script scans all `<img src>`, skips base64/http, converts local paths to `data:image/...;base64,...`, and overwrites in place.

**Skip only if:** no new local image references were added since last bundle.
**First PKU delivery:** NEVER skip.

---

## Core Principles (from SKILL.md)

1. **Zero Dependencies** — Single HTML, inline CSS/JS, no npm
2. **Show, Don't Tell** — Generate visual previews, not abstract descriptions
3. **Viewport Fitting** — Free: `100vh` per slide, no scrolling. PKU: fixed 1080px + JS scaling
4. **Distinctive Design** — Avoid generic AI aesthetics
5. **Asset Bundling** — All local images must be base64-embedded before delivery
