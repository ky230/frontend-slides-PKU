---
name: PKU Academic Classic
description: PKU Academic Classic presentation template — red-yellow palette, fixed 1920x1080 canvas, dual Logo, amber-gold progress bar. Supports CMS and CEPC brand variants.
---

# PKU Academic Classic — Full Style Specification

> **Reference spec for PKU Academic Classic.** CSS/JS source of truth is the template file (`assets/PKU_{CMS,CEPC}_Classic_Empty.html`). This doc covers: class index, HTML patterns, layout systems, generation rules, and the Element Annotation Convention (EAC).

---

## 0. Pre-flight Q&A (Mandatory, DO NOT skip)

Before generating any HTML, you **must** confirm the following with the user:

| # | Question | Target Location | Default |
|---|----------|----------------|---------|
| Q0 | Brand selection: CMS or CEPC? | Logo + footer | None (required) |
| Q1 | Main title? Which keywords to highlight yellow? | `<h1>` title-banner + footer-left | None (required) |
| Q2 | Report type / meeting name? | `<h2>` title-banner + footer-right | None (required) |
| Q3 | Author list? | author-info | None (required) |
| Q4 | Who is the speaker? (underlined on title, centered in footer) | author-info + footer-center | None (required) |
| Q5 | Affiliation list? | author-info | None (required) |
| Q6 | Report date? | author-info | Today's date (rendered as Mar 28<sup>th</sup>) |
| Q7 | Reference citation? | author-info | Optional |
| Q8 | Outline list? | Outline + transition slides | None (required) |
| Q9 | HTML output path? | `init-slides.py --out` | None (required, user-specified) |

**Additional user requirements** (images, special layouts, etc.) are handled after the Q&A.

---

## 1. Logo Assets (Image Files)

> **⚠️ Logos are stored as real image files. NEVER place Base64 long strings in this file!**
> Before delivery, `bundle-html.py` embeds all images (including logos) as Base64.

All logos are stored in:
```
{{FRONTEND_SLIDES_REPO_PATH}}/assets/
```

### 1.1 PKU Logo (shared by both brands)
- File: `assets/PKU_logo.jpeg`

HTML usage:
```html
<img src="assets/PKU_logo.jpeg" class="logo-img pku-logo" alt="PKU Logo">
```

### 1.2 CEPC Logo
- File: `assets/CEPC_logo.png`

HTML usage:
```html
<img src="assets/CEPC_logo.png" class="logo-img cepc-logo" alt="CEPC Logo">
```

### 1.3 CMS Logo
- File: `assets/CMS_logo.png`

HTML usage:
```html
<img src="assets/CMS_logo.png" class="logo-img cms-logo" alt="CMS Logo">
```

---

## 2. CMS vs CEPC Differences

| Element | CEPC Version | CMS Version |
|---------|-------------|-------------|
| Logo 2 | CEPC logo, `.cepc-logo`, `border-radius: 50%` | CMS logo, `.cms-logo`, `border-radius: 4px` |
| Extra CSS | None | `.cms-logo { border-radius: 4px; }` |

**Apart from the Logo, all CSS/JS/HTML structure is identical.**

---

## 3. CSS Reference (Minimal)

> 📌 **Source of truth:** `assets/PKU_{CMS,CEPC}_Classic_Empty.html` template file.
> **Read the template directly.** This section only lists key variables and class names.

### 3.1 CSS Custom Properties (`:root`)

```css
:root {
    --bg-white: #fefefc;
    --pku-red: #cc0000;
    --pku-yellow: #ffff00;
    --text-dark: #1a1a1a;
    --font-body: 'Times New Roman', Times, serif;
    --font-comic: 'Comic Sans MS', 'Comic Sans', cursive;
    --title-size: 64px;
    --h1-size: 56px;
    --body-size: 34px;
    --footer-height: 48px;
    --header-height: 60px;
    --duration-normal: 0.5s;
}
```

### 3.2 Class Name Index

| Class | Purpose | Key Properties |
|-------|---------|----------------|
| `.slide` | Base slide (1920×1080) | `scroll-snap-align: start` |
| `.slide.normal-slide` | Content slide | `padding-top: var(--header-height)` |
| `.title-slide` | Title page | No header, centered |
| `.transition-slide` | Section divider | Red vertical line, Comic Sans |
| `.slide-content` | Content wrapper | `width: 1760px; margin: 0 auto` |
| `.bullet-list` | L1 bullets | Red disc, `var(--body-size)` |
| `.bullet-list li ul li` | L2 bullets | Red dash `—`, 0.9em |
| `.dual-layout` | Left-right grid | `--split: 4fr 6fr` (adjustable) |
| `.left-col` / `.right-col` | Grid children | Flex column |
| `.highlight-box` | Red conclusion box | Left border red |
| `.important-box` | Blue note box | Left border blue |
| `.warning-box` | Orange warning box | Left border orange |
| `.tip-box` | Green tip box | Left border green |
| `.fig` | Figure grid system | `--w --h --x --y --gap` knobs |
| `.fig-RxC` | Grid presets | `fig-1` through `fig-4x4` |
| `.tab` | Table wrapper | `--w --x --y --tab-size` knobs |
| `.reveal .d1/.d2/.d3` | Animations | Fade-up on scroll, staggered delay |
| `.highlight-yellow` | Yellow keyword | Title highlight |
| `.image-grid` | Legacy image grid | `auto-fit, minmax(30%, 1fr)` |


---

## 4. MathJax Configuration

Insert after `</style>` and before `</head>`:

```html
<script>
    MathJax = {
        tex: {
            inlineMath: [['$', '$'], ['\\(', '\\)']],
            displayMath: [['$$', '$$'], ['\\[', '\\]']]
        },
        svg: { fontCache: 'global' }
    };
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
```

---

## 5. HTML Structure Template

### 5.1 Overall Skeleton

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{Q1_Main_Title}}</title>
    <style>
        /* Paste full CSS from Section 3 */
    </style>
    <!-- Paste MathJax config from Section 4 -->
</head>
<body>
    <div id="scale-wrapper">

    <!-- Global Logo -->
    <div class="global-logos" id="globalLogos">
        <img src="{{PKU_LOGO_BASE64}}" class="logo-img pku-logo" alt="PKU Logo">
        <!-- For CEPC brand: -->
        <img src="{{CEPC_LOGO_BASE64}}" class="logo-img cepc-logo" alt="CEPC Logo">
        <!-- For CMS brand: -->
        <!-- <img src="{{CMS_LOGO_BASE64}}" class="logo-img cms-logo" alt="CMS Logo"> -->
    </div>

    <!-- Top Red Bar -->
    <div class="global-header hidden" id="globalHeader">
        <div class="header-text" id="headerText">Title Placeholder</div>
    </div>

    <!-- Segmented Progress Bar -->
    <div class="progress-container" id="progressContainer"></div>

    <!-- Bottom Red Bar -->
    <div class="global-footer">
        <div class="footer-left">
            {{Q1_Main_Title_with_highlight-yellow_spans}}
        </div>
        <div class="footer-center">
            {{Q4_Speaker}}
        </div>
        <div class="footer-right">
            {{Q2_Report_Type}} <span id="pageNumber" style="margin-left: 0.5rem;">1</span>
        </div>
    </div>

    <div class="slides-scroller" id="slidesScroller">
        <!-- Slide content goes here -->
    </div>
    </div>

    <script>
        // Paste full JS from Section 6
    </script>
</body>
</html>
```

### 5.2 Title Slide

```html
<section class="slide title-slide visible" data-header="hidden" data-title="">
    <div class="title-banner reveal d1">
        <h1>{{Q1_Main_Title, keywords wrapped in <span class="highlight-yellow">}}</h1>
        <h2>{{Q2_Report_Type}}</h2>
    </div>
    <div class="author-info reveal d2">
        <p><u style="text-decoration: underline; text-underline-offset: 0.25em; text-decoration-skip-ink: none;">{{Q4_Speaker}}</u><sup>1</sup>, {{Other_Authors}}<sup>N</sup></p>
        <p style="margin-top: 1rem;"><sup>1</sup> {{Q5_Affiliations}}</p>
        <!-- Additional affiliations numbered sequentially -->
        <p style="margin-top: 2rem; font-size: 0.8em;">{{Q6_Date}}</p>
        <p style="font-size: 0.8em;">Reference: {{Q7_Reference_Link}}</p>
    </div>
</section>
```

### 5.3 Outline Page

```html
<section class="slide normal-slide" data-header="visible" data-title="Outline">
    <div class="slide-content">
        <ul class="bullet-list reveal d1" style="margin-top: 6rem; margin-left: 0;">
            <li><strong>{{Outline_Item_1}}</strong></li>
            <li><strong>{{Outline_Item_2}}</strong></li>
            <!-- ... -->
        </ul>
    </div>
</section>
```

### 5.4 Transition Slide

**Titles must strictly correspond to the Outline bullet order.**

```html
<section class="slide transition-slide" data-header="hidden" data-title="">
    <div class="transition-text reveal d1">
        {{Outline_Item_N}}
    </div>
</section>
```

### 5.5 Content Slide

The top red bar title `data-title` defaults to the nearest transition page title.

```html
<section class="slide normal-slide" data-header="visible" data-title="{{Nearest_Transition_Title}}">
    <div class="slide-content reveal d1">
        <ul class="bullet-list" style="margin-left: 0;">
            <li>Level 1 content (red disc bullet)
                <ul>
                    <li>Level 2 content (red dash —)</li>
                </ul>
            </li>
        </ul>
    </div>
</section>
```

> **⚠️ DO NOT use `<h3>` / `<h4>` / `<h5>` or any inline heading tags in content slides!**
> 
> - The **only source** for the page title is the top red bar `data-title` (38px yellow text)
> - `data-title` defaults to the nearest transition title, but can be customized (e.g., "Landau MPV Comparison")
> - Content area only allows: `bullet-list`, `table`, `image-grid`, `highlight-box` / `important-box`, etc.
> - When sub-section headings are needed, use **bold L1 bullet** instead of heading tags

> **💡 Per-slide bullet margin fine-tuning:**
>
> `.slide-content` defaults to `overflow: visible`, so you can freely adjust `margin-left` on `<ul>` to any value:
> - `margin-left: 0` — standard position (flush with content boundary)
> - `margin-left: -40px` — push left beyond content boundary
> - `margin-left: -80px` — maximum, aligns with red title bar left edge
>
> **⚠️ Do NOT use `list-style-position: inside`** — it changes the bullet-text spacing. Keep default `outside` and adjust `margin-left` instead.

### 5.6 Highlight Box Usage

```html
<!-- Red conclusion box -->
<div class="highlight-box">
    <strong>Key conclusion:</strong> Conclusion content here
</div>

<!-- Blue important box -->
<div class="important-box">
    <strong>Important:</strong> Important note here
</div>

<!-- Orange warning box -->
<div class="warning-box">
    <strong>Warning:</strong> Warning content here
</div>

<!-- Green tip box -->
<div class="tip-box">
    <strong>Tip:</strong> Tip content here
</div>
```

### 5.7 Figure Layout System

> **Scope:** Best for **image-only regions** — backup slides, full-page plots, pure figure grids. For mixed bullet+image slides, use **§5.9 Absolute-Position** pattern instead.

Use `.fig` + preset class for image grids. Available presets: `fig-1`, `fig-1x2` through `fig-4x4` (rows×cols, max 4).

**7 knobs** (override via `style="--knob:value"`):
- Layout: `--w` width, `--h` height, `--x` horizontal shift, `--y` vertical shift, `--gap` spacing
- Caption: `--cap-size` font size (default auto), `--cap-y` vertical offset

**Dual-layout** uses `--split` for ratio: `style="--split: 1fr 1fr;"` (default `4fr 6fr`)

```html
<!-- fig-2x3: 2行×3列 | --w --h --x --y --gap --cap-size --cap-y -->
<div class="fig fig-2x3 reveal d2" style="--gap:8px;">
    <div class="figure-frame"><img src="th5_nocut.png"><div class="caption">th=5 (no cut)</div></div>
    <div class="figure-frame"><img src="th10_nocut.png"><div class="caption">th=10</div></div>
    <div class="figure-frame"><img src="th20_nocut.png"><div class="caption">th=20</div></div>
    <div class="figure-frame"><img src="th5_cut.png"><div class="caption">th=5 (cut)</div></div>
    <div class="figure-frame"><img src="th10_cut.png"><div class="caption">th=10</div></div>
    <div class="figure-frame"><img src="th20_cut.png"><div class="caption">th=20</div></div>
</div>
```

> **⚠️ AI Generation Rule: Inline Comment is MANDATORY**
>
> When generating HTML with `.fig` containers, you **MUST** place an HTML comment on the same line or directly above, listing the layout and available knobs:
> ```html
> <!-- fig-2x3: 2行×3列 | --w --h --x --y --gap --cap-size --cap-y -->
> ```
> This lets the user adjust parameters without consulting documentation.

> For full reference with ASCII diagrams and all presets, see `reference/FIGURE_LAYOUTS.md`.

### 5.8 Table Layout System

> **Scope:** Best for **standalone tables** filling a content region. For tables nested inside bullet lists, use inline `font-size`/`margin` on `<table>` directly — see `FINE_TUNING.md` §3.

Wrap any `<table>` in a `<div class="tab">` to gain free positioning, font control, and caption support.

**7 knobs** (override via `style="--knob:value"`):
- Position: `--w` width, `--x` horizontal shift, `--y` vertical shift
- Typography: `--tab-size` table font size (default `0.6 × body-size`)
- Cell padding: `--pad-h` horizontal, `--pad-v` vertical
- Caption: `--cap-size` font size, `--cap-y` vertical offset

**Caption** is optional. When present, use `<div class="caption">` — it automatically renders centered, grey `#666`, matching figure captions.

```html
<!-- tab | --w --x --y --tab-size --pad-h --pad-v --cap-size --cap-y -->
<div class="tab" style="--w:80%; --x:40px; --y:-10px; --tab-size:18px;">
    <table>
        <tr><th>Column A</th><th>Column B</th><th>Column C</th></tr>
        <tr><td>1.23</td><td>4.56</td><td>7.89</td></tr>
        <tr><td>0.12</td><td>3.45</td><td>6.78</td></tr>
    </table>
    <div class="caption">Tab. Description of the table content.</div>
</div>
```

> **⚠️ AI Generation Rule: Inline Comment is MANDATORY**
>
> When generating HTML with `.tab` containers, you **MUST** place an HTML comment on the same line or directly above, listing the available knobs:
> ```html
> <!-- tab | --w --x --y --tab-size --pad-h --pad-v --cap-size --cap-y -->
> ```
> This lets the user adjust parameters without consulting documentation.

> **💡 Caption is OFF by default.** Only add `<div class="caption">` when the user explicitly requests a table caption. When present, it inherits the same style as figure captions (centered, grey).

### 5.9 Absolute-Position Mixed Layout (Complex Slides)

For slides where bullets, images, tables, and footnotes each need **independent** position/size control:

```html
<div class="slide-content" style="position: relative; overflow: visible;">

    <!-- [BULLETS]: Main analysis bullets | KNOBS: top(100px), left(0), width(48%), font-size(1.85em) -->
    <div style="position: absolute; top: 100px; left: 0px; width: 48%;">
        <ul class="bullet-list reveal d2" style="font-size: 1.85em;">
            <li>First point</li>
        </ul>
    </div>

    <!-- [IMAGES]: 2x2 analysis plots | KNOBS: top(70px), right(0), width(55%), gap(6px) -->
    <div class="reveal d3"
        style="position: absolute; top: 70px; right: 0px; width: 55%; display: grid; grid-template-columns: 1fr 1fr; gap: 6px;">
        <img src="attachment/plot1.png" style="width: 100%;">
        <img src="attachment/plot2.png" style="width: 100%;">
    </div>

    <!-- [FOOTNOTE]: Variable definitions | KNOBS: font-size(0.85em), margin-top(6px), margin-left(-20px) -->
    <div style="font-size: 0.85em; color: #888; margin-top: 6px; margin-left: -20px;">
        <sup>†</sup> Footnote text
    </div>

</div>
```

**When to use:** Any slide where bullets and images need *independent* tuning. This is the **most common pattern** for CMS analysis slides.

**When NOT to use:** Simple full-width bullet content → default `.slide-content` flow. Simple left-right split → `.dual-layout`.

> ⚠️ **Parent must have `position: relative`**. Children use `position: absolute` with `top/left/right/width` for placement.

### 5.10 Comment-Out Convention (Hiding Content)

To hide content without deleting (e.g., removing a plot row pending reviewer feedback):

```html
<!-- [HIDDEN]: QCD DR row — removed per reviewer request, keeping for restoration
<div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 6px;">
    <img src="attachment/qcd_met.png">
    ...
</div>
-->
```

Always include a `[HIDDEN]:` tag with a brief reason.

---

## 6. JavaScript Reference (Minimal)

> 📌 **Source of truth:** `assets/PKU_{CMS,CEPC}_Classic_Empty.html` template file.
> **Read the template directly.** JS is copied verbatim by `init-slides.py`.

### Key Components

| Component | Function | Notes |
|-----------|----------|-------|
| `applyScale()` | 1920×1080 → viewport scaling | `Math.min(w/1920, h/1080)` |
| `SlidePresentation` | Keyboard/wheel/scroll nav | Arrow keys, Space, G (go-to), F (fullscreen) |
| `IntersectionObserver` | Scroll-triggered `.visible` class | Triggers `.reveal` animations |
| `sessionStorage` | Persists slide position | Survives Live Server hot-reload |
| Progress bar | Segmented amber `#d4a800` | Stops at "Back Up" transition |
| Go-to overlay | `G` key → input slide number | Enter confirms, Esc cancels |


---

    constructor() {
        this.slides = document.querySelectorAll('.slide');
        if (this.slides.length === 0) return;

        this.header = document.getElementById('globalHeader');
        this.headerText = document.getElementById('headerText');
        this.pageNum = document.getElementById('pageNumber');
        this.scroller = document.getElementById('slidesScroller');

        this.setupIntersectionObserver();
        this.setupKeyboardNav();
        this.setupWheelNav();

        applyScale();

        // Restore saved slide position (survives Live Server hot-reload)
        const savedSlide = sessionStorage.getItem('savedSlideIndex');
        if (savedSlide !== null) {
            setTimeout(() => {
                this.scroller.scrollTo({ top: parseInt(savedSlide) * 1080, behavior: 'instant' });
            }, 50);
        }
    }

    setupWheelNav() {
        let isWheeling = false;
        window.addEventListener('wheel', (e) => {
            if (isWheeling) return;
            const currentIndex = Math.round(this.scroller.scrollTop / 1080);
            if (e.deltaY > 2) {
                if (currentIndex < this.slides.length - 1) {
                    isWheeling = true;
                    this.scroller.scrollTo({ top: (currentIndex + 1) * 1080, behavior: 'smooth' });
                    setTimeout(() => { isWheeling = false; }, 600);
                }
            } else if (e.deltaY < -2) {
                if (currentIndex > 0) {
                    isWheeling = true;
                    this.scroller.scrollTo({ top: (currentIndex - 1) * 1080, behavior: 'smooth' });
                    setTimeout(() => { isWheeling = false; }, 600);
                }
            }
        }, { passive: false });
    }

    setupIntersectionObserver() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');

                    const index = Array.from(this.slides).indexOf(entry.target) + 1;

                    // Persist current slide for Live Server
                    sessionStorage.setItem('savedSlideIndex', index - 1);

                    if (this.pageNum) this.pageNum.innerText = index;

                    const segments = document.querySelectorAll('.progress-segment');
                    segments.forEach((seg, i) => {
                        if (i < index) {
                            seg.classList.add('active');
                        } else {
                            seg.classList.remove('active');
                        }
                    });

                    const headerState = entry.target.getAttribute('data-header');
                    const title = entry.target.getAttribute('data-title');

                    if (headerState === 'visible') {
                        this.header.classList.remove('hidden');
                        this.headerText.innerHTML = title || '';
                        // data-title supports LaTeX: triggers MathJax re-render when $ is detected
                        if (window.MathJax && title && title.includes('$')) {
                            MathJax.typesetPromise([this.headerText]).catch(() => {});
                        }
                    } else {
                        this.header.classList.add('hidden');
                    }
                }
            });
        }, { root: this.scroller, threshold: 0.5 });

        this.slides.forEach(slide => observer.observe(slide));
    }

    setupKeyboardNav() {
        // --- Go-to-slide overlay ---
        const overlay = document.createElement('div');
        overlay.id = 'goto-overlay';
        overlay.innerHTML = `
            <div style="position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.4);
                display:flex;align-items:center;justify-content:center;z-index:9999;">
                <div style="background:#fff;border-radius:12px;padding:30px 40px;box-shadow:0 8px 32px rgba(0,0,0,0.3);
                    text-align:center;font-family:'Times New Roman',serif;">
                    <div style="font-size:20px;color:#888;margin-bottom:12px;">Go to Slide</div>
                    <input id="goto-input" type="number" min="1" style="font-size:36px;width:100px;text-align:center;
                        border:2px solid #cc0000;border-radius:8px;padding:8px;outline:none;" />
                    <div style="font-size:14px;color:#aaa;margin-top:8px;">Enter ↵ confirm &nbsp; Esc cancel</div>
                </div>
            </div>`;
        overlay.style.display = 'none';
        document.body.appendChild(overlay);

        const gotoInput = document.getElementById('goto-input');
        let gotoActive = false;

        const showGoto = () => {
            gotoActive = true;
            overlay.style.display = 'block';
            gotoInput.value = '';
            gotoInput.focus();
        };
        const hideGoto = () => {
            gotoActive = false;
            overlay.style.display = 'none';
        };

        gotoInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                const n = parseInt(gotoInput.value);
                if (n >= 1 && n <= this.slides.length) {
                    this.scroller.scrollTo({ top: (n - 1) * 1080, behavior: 'smooth' });
                }
                hideGoto();
                e.stopPropagation();
            } else if (e.key === 'Escape') {
                hideGoto();
                e.stopPropagation();
            }
        });
        overlay.addEventListener('click', (e) => { if (e.target === overlay.firstElementChild) hideGoto(); });

        document.addEventListener('keydown', (e) => {
            if (gotoActive) return;

            if (e.key === 'g' || e.key === 'G') {
                showGoto();
                return;
            }

            if (e.key === 'f' || e.key === 'F') {
                if (!document.fullscreenElement) {
                    document.documentElement.requestFullscreen().catch(() => {});
                } else {
                    if (document.exitFullscreen) {
                        document.exitFullscreen();
                    }
                }
                return;
            }

            const currentIndex = Math.round(this.scroller.scrollTop / 1080);

            if (e.key === 'ArrowDown' || e.key === 'PageDown' || e.key === ' ') {
                e.preventDefault();
                if (currentIndex < this.slides.length - 1) {
                    this.scroller.scrollTo({
                        top: (currentIndex + 1) * 1080,
                        behavior: 'smooth'
                    });
                }
            } else if (e.key === 'ArrowUp' || e.key === 'PageUp') {
                e.preventDefault();
                if (currentIndex > 0) {
                    this.scroller.scrollTo({
                        top: (currentIndex - 1) * 1080,
                        behavior: 'smooth'
                    });
                }
            }
        });
    }
}
document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('progressContainer');
    const slidesArr = Array.from(document.querySelectorAll('.slide'));
    let totalSlides = slidesArr.length;
    // Find transition slide containing "Back Up"; progress bar renders only up to that point
    const backUpIndex = slidesArr.findIndex(s => s.classList.contains('transition-slide') && s.textContent.trim().includes('Back Up'));
    if (backUpIndex !== -1) {
        totalSlides = backUpIndex;
    }
    for (let i = 0; i < totalSlides; i++) {
        const seg = document.createElement('div');
        seg.className = 'progress-segment';
        container.appendChild(seg);
    }
    new SlidePresentation();
});
```

---

## 7. Generation Rules Summary

| Rule | Requirement |
|------|-------------|
| Font | `'Times New Roman', Times, serif` (global); transition title uses `'Comic Sans MS', cursive` |
| Title h1 | 64px, white on red, keywords use `.highlight-yellow` |
| Subtitle h2 | 32px (`calc(var(--title-size) * 0.5)`) |
| Body text | 34px |
| Header title | 38px, yellow `var(--pku-yellow)`, bold |
| Footer font | 24px, white |
| L1 Bullet | Red `disc` marker, `var(--body-size)` |
| L2 Bullet | Red `—` dash, `calc(var(--body-size) * 0.9)` |
| L3 Bullet | Numbered `1. 2. 3.` (disabled by default, enabled on user request) |
| Formulas | MathJax 3, inline `$...$`, display `$$...$$` |
| Progress bar | Amber-gold `#d4a800` segmented |
| Transition decoration | Left-side red gradient vertical line |
| Speaker underline | `text-underline-offset: 0.25em; text-decoration-skip-ink: none;` |
| Affiliation labels | Superscript numbering `<sup>N</sup>` |
| Footer center | Uses Q4-specified speaker name |
| Transition titles | Must strictly correspond to Outline bullet order |
| Content data-title | Defaults to nearest transition page title |
| Table font | `calc(var(--body-size) * 0.6)` ≈ 20px, follows global |
| Caption font | `calc(var(--body-size) * 0.6)` ≈ 20px, follows global, no hardcoding |
| slide-content padding | `20px 0` (not 60px), maximizes content area |
| Dense bullet mode | `li style="margin-bottom: 10px;"` overrides default 30px, for content-heavy pages |
| 6-image comparison grid | Use `.fig fig-2x3` with `--gap: 8px` |
| Figure inline comment | **MANDATORY**: `<!-- fig-RxC: R行×C列 \| --w --h --x --y --gap --cap-size --cap-y -->` above every `.fig` div |
| `--split` (dual-layout) | `--split: 4fr 6fr` default; override with e.g. `--split: 1fr 1fr` |
| data-title LaTeX | `innerHTML` + `MathJax.typesetPromise()` renders formulas in the red bar title |
| Element Annotation | **MANDATORY**: `<!-- [TYPE]: desc \| KNOBS: param(value), ... -->` above every positioned element |
| Comment-out hidden | `<!-- [HIDDEN]: reason ... -->` wrapping hidden content |

---

## 8. Element Annotation Convention (EAC)

> **NON-NEGOTIABLE**: Every independently positioned element MUST have an annotation comment.

### Format

```
<!-- [TYPE]: description | KNOBS: param1(current_value), param2(current_value), ... -->
```

### Type Tags

| Tag | Used For |
|-----|----------|
| `[BULLETS]` | Bullet list containers |
| `[IMAGES]` | Image grids, single images, figure regions |
| `[TABLE]` | Tables (standalone or nested) |
| `[HIGHLIGHT-BOX]` | `.highlight-box`, `.important-box`, etc. |
| `[FOOTNOTE]` | Footer annotations, definitions |
| `[CAPTION]` | Standalone captions below image regions |
| `[HIDDEN]` | Commented-out content |
| `[CUSTOM]` | Anything else (e.g., decorative elements) |

### Rules

1. **KNOBS list** — Only list parameters the user is likely to adjust. Focus on position (`top`, `left`, `right`, `width`) and size (`font-size`, `gap`). Skip `color`, `display`, etc.
2. **Current values** — Always show current value in parens: `top(100px)`, not just `top`.
3. **One line** — Keep the comment to a single line. Abbreviate descriptions if needed.
4. **Update on edit** — When modifying an element's style, update the KNOBS values in the comment.
5. **Skip for trivial elements** — Simple `<li>` items, inline `<strong>`, etc. don't need annotations. Only annotate *container-level* elements with position/size properties.

### Examples

```html
<!-- [BULLETS]: Systematic uncertainties list | KNOBS: top(100px), left(0), width(48%), font-size(1.85em) -->
<div style="position: absolute; top: 100px; left: 0px; width: 48%;">
    <ul class="bullet-list reveal d2" style="font-size: 1.85em;"> ... </ul>
</div>

<!-- [IMAGES]: Prefit control plots 2x4 | KNOBS: top(3%), left(-3.5%), width(110%) -->
<div class="reveal d1" style="position: absolute; top: 3%; left: -3.5%; width: 110%;">
    <div class="fig fig-2x4" style="--gap: 10px;"> ... </div>
</div>

<!-- [TABLE]: Signal yields summary | KNOBS: font-size(0.75em), margin-left(-20px), width(110%) -->
<table style="font-size: 0.75em; margin-left: -20px; width: 110%;"> ... </table>

<!-- [FOOTNOTE]: Jet matching definitions | KNOBS: font-size(0.85em), margin-top(6px) -->
<div style="font-size: 0.85em; color: #888; margin-top: 6px;"> ... </div>
```
