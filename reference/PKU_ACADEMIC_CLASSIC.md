---
name: PKU Academic Classic
description: PKU Academic Classic presentation template — red-yellow palette, fixed 1920x1080 canvas, dual Logo, amber-gold progress bar. Supports CMS and CEPC brand variants.
---

# PKU Academic Classic — Full Style Specification

> **Fully self-contained**: This file contains everything needed to generate PKU academic slides (CSS/JS/HTML structure/Logo base64). No external file dependencies.

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

## 3. Full CSS

The following CSS must be embedded **verbatim** inside `<style>` tags:

> 📌 **Single Source of Truth is the `assets/PKU_{CMS,CEPC}_Classic_Empty.html` template file.**
> This section is only a reference copy for manual AI generation. If inconsistent with the template, the template takes precedence.

```css
/* ===========================================
   CSS CUSTOM PROPERTIES (Theme: PKU Red-Yellow Classic)
   PKU Academic Presentation Style - Fixed Absolute Ratio (1920x1080)
   =========================================== */
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

/* Base Environment Reset */
html, body {
    height: 100%; width: 100%; margin: 0; padding: 0;
    overflow: hidden; background: #1a1a1a;
    color: var(--text-dark); font-family: var(--font-body);
}
* { box-sizing: border-box; }

/* Smart Proportional Scaling Canvas */
#scale-wrapper {
    position: absolute;
    width: 1920px; height: 1080px;
    left: 50%; top: 50%;
    transform-origin: center center;
    background: var(--bg-white);
    overflow: hidden;
    box-shadow: 0 0 20px rgba(0,0,0,0.4);
}

/* Scroll Container */
.slides-scroller {
    position: absolute; left: 0; top: 0;
    width: 100%; height: 100%;
    overflow-y: auto;
    scroll-snap-type: y mandatory;
    scroll-behavior: smooth;
}
.slides-scroller::-webkit-scrollbar { display: none; }
.slides-scroller { scrollbar-width: none; }

/* -------------------------------------------
   GLOBAL WIDGETS
   ------------------------------------------- */
.global-logos {
    position: absolute; top: 12px; right: 0;
    height: calc(var(--header-height) - 4px);
    display: flex; align-items: center; justify-content: flex-end;
    padding-right: 10px; z-index: 1001;
    background: transparent;
}
.logo-img {
    height: 130%;
    object-fit: contain; margin-left: 5px;
    border-radius: 50%;
    box-shadow: 0 2px 4px rgba(0,0,0,0.3);
    background-color: white;
}
/* CMS Logo Override (CMS brand only) */
.cms-logo {
    border-radius: 4px;
}

.global-header {
    position: absolute; top: 0; left: 0;
    width: 1920px; height: var(--header-height);
    background: var(--pku-red); z-index: 1000;
    display: flex; align-items: center; padding-left: 30px;
    transition: transform 0.3s ease;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.global-header.hidden { transform: translateY(-100%); }
.header-text {
    color: var(--pku-yellow); font-size: 38px; font-weight: bold;
    font-family: var(--font-body);
}

.progress-container {
    position: absolute; bottom: var(--footer-height); left: 0;
    width: 1920px; height: 4px; z-index: 1001;
    display: flex; gap: 2px;
}
.progress-segment {
    flex: 1; height: 100%;
    background: rgba(255,255,255,0.15);
    transition: background 0.4s ease, box-shadow 0.4s ease;
}
.progress-segment.active {
    background: #d4a800;
    box-shadow: 0 0 4px rgba(212,168,0,0.5);
}

.global-footer {
    position: absolute; bottom: 0; left: 0;
    width: 1920px; height: var(--footer-height);
    background: var(--pku-red); z-index: 1000;
    display: flex; justify-content: space-between; align-items: center;
    padding: 0 20px; color: white; font-weight: bold;
    font-family: var(--font-body); font-size: 24px;
    box-shadow: 0 -4px 6px rgba(0,0,0,0.1);
}
.footer-left { text-align: left; flex: 2; }
.footer-center { text-align: center; flex: 1; }
.footer-right { text-align: right; flex: 2; display: flex; justify-content: flex-end; gap: 10px; }

/* -------------------------------------------
   SLIDE BASE STYLES
   ------------------------------------------- */
.slide {
    width: 1920px; height: 1080px;
    overflow: hidden; scroll-snap-align: start;
    display: flex; flex-direction: column; position: relative;
    padding-bottom: var(--footer-height);
    background-color: var(--bg-white);
    background-image: 
        linear-gradient(rgba(139, 69, 19, 0.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(139, 69, 19, 0.035) 1px, transparent 1px);
    background-size: 50px 50px;
}
.slide.normal-slide {
    padding-top: var(--header-height);
}

/* -------------------------------------------
   TITLE SLIDE
   ------------------------------------------- */
.title-slide { justify-content: center; }
.title-banner {
    width: 1920px; background: var(--pku-red); color: white;
    text-align: center; padding: 60px 20px; margin-bottom: 40px;
    margin-top: 80px;
}
.title-banner h1 {
    font-family: var(--font-body); font-size: var(--title-size);
    margin: 0 0 20px 0; font-weight: bold;
}
.title-banner h2 {
    font-family: var(--font-body); font-size: calc(var(--title-size) * 0.5);
    margin: 0; font-weight: bold;
}
.highlight-yellow { color: var(--pku-yellow); }
.author-info {
    margin-top: 60px; text-align: center;
    font-size: var(--body-size); line-height: 1.8;
    color: var(--text-dark);
}
.author-info p { margin: 10px 0; }

/* -------------------------------------------
   TRANSITION SLIDE
   ------------------------------------------- */
.transition-slide {
    justify-content: center; align-items: center; text-align: center;
    position: relative;
}
.transition-slide::before {
    content: '';
    position: absolute;
    left: 120px; top: 80px; bottom: 80px;
    width: 6px;
    background: linear-gradient(180deg, transparent 0%, var(--pku-red) 15%, var(--pku-red) 85%, transparent 100%);
    border-radius: 3px;
}
.transition-text {
    font-family: var(--font-comic); font-size: 64px;
    font-weight: bold; color: var(--text-dark);
    padding-left: 60px;
}

/* -------------------------------------------
   CONTENT SLIDES
   ------------------------------------------- */
.slide-content {
    flex: 1; width: 1760px; margin: 0 auto;
    padding: 20px 0; overflow: hidden;
    display: flex; flex-direction: column;
}

/* Bullet Hierarchy */
.bullet-list { margin-left: 40px; }
.bullet-list li {
    list-style-type: disc;
    font-size: var(--body-size); margin-bottom: 30px; line-height: 1.5;
}
/* Dense mode: use li style="margin-bottom: 10px;" to override default 30px for content-heavy pages */
.bullet-list li::marker { color: var(--pku-red); font-size: 1.1em; }
/* L2: Red Dash */
.bullet-list li ul li {
    list-style-type: '— ';
    font-size: calc(var(--body-size) * 0.9);
    margin-bottom: 20px;
}
.bullet-list li ul li::marker { color: var(--pku-red); font-size: 1em; }

/* Text-Image Mixed Layout */
.dual-layout {
    display: grid; grid-template-columns: 4fr 6fr; gap: 40px; height: 100%;
}
.left-col {
    display: flex; flex-direction: column;
    justify-content: flex-start; padding-top: 20px; padding-right: 40px;
}
.right-col {
    display: flex; flex-direction: column;
    justify-content: center; gap: 20px;
    min-height: 0; overflow: hidden;
}
.image-box {
    flex: 1; min-height: 0;
    display: flex; justify-content: center; align-items: center;
}
.image-box img { max-width: 100%; max-height: 100%; object-fit: contain; }

a { color: #0000ee; text-decoration: underline; text-decoration-skip-ink: none; }

/* Equal Two-Column */
.two-col {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 60px; height: 100%; align-items: start;
}

/* Table Styles */
table {
    width: 100%; border-collapse: collapse;
    font-size: calc(var(--body-size) * 0.6); margin: 25px 0;
    background: var(--bg-white); box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
th { 
    background: var(--pku-red); color: white; padding: 12px 15px; 
    font-weight: bold; text-align: center; border: 1px solid var(--pku-red);
}
td { 
    padding: 10px 15px; border: 1px solid #ddd; text-align: center; 
}
tr:nth-child(even) { background: #f5f0e3; }

/* Image Grid */
.image-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(30%, 1fr));
    gap: 15px; width: 100%; align-items: center; justify-items: center;
}
.image-grid img { max-width: 100%; max-height: 100%; object-fit: contain; border-radius: 4px; }
.image-grid .grid-label { grid-column: 1 / -1; font-weight: bold; text-align: center; color: var(--pku-red); padding-bottom: 5px; }

/* Highlight Conclusion Box */
.highlight-box {
    background: rgba(204, 0, 0, 0.06);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(204, 0, 0, 0.20);
    border-left: 6px solid var(--pku-red);
    padding: 25px 30px; margin: 30px 0;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    font-size: calc(var(--body-size) * 0.95); line-height: 1.6;
}
.highlight-box strong { color: var(--pku-red); }

/* Important Box */
.important-box {
    background: rgba(59, 130, 246, 0.06);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(59, 130, 246, 0.20);
    border-left: 6px solid #3b82f6;
    padding: 25px 30px; margin: 30px 0;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    font-size: calc(var(--body-size) * 0.95); line-height: 1.6;
}
.important-box strong { color: #3b82f6; }

/* Warning Box */
.warning-box {
    background: rgba(245, 158, 11, 0.06);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(245, 158, 11, 0.20);
    border-left: 6px solid #f59e0b;
    padding: 25px 30px; margin: 30px 0;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    font-size: calc(var(--body-size) * 0.95); line-height: 1.6;
}
.warning-box strong { color: #f59e0b; }

/* Tip Box */
.tip-box {
    background: rgba(34, 197, 94, 0.06);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(34, 197, 94, 0.20);
    border-left: 6px solid #22c55e;
    padding: 25px 30px; margin: 30px 0;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    font-size: calc(var(--body-size) * 0.95); line-height: 1.6;
}
.tip-box strong { color: #22c55e; }

/* Image + Caption */
.figure-frame { text-align: center; overflow: hidden; }
.figure-frame img {
    max-width: 100%; max-height: 28vh; object-fit: contain;
    border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.figure-frame .caption {
    font-size: calc(var(--body-size) * 0.6); color: #666; margin-top: 4px;
}

/* -------------------------------------------
   ANIMATIONS
   ------------------------------------------- */
.reveal {
    opacity: 0; transform: translateY(20px);
    transition: opacity var(--duration-normal), transform var(--duration-normal);
}
.slide.visible .reveal { opacity: 1; transform: translateY(0); }
.d1 { transition-delay: 0.1s; }
.d2 { transition-delay: 0.2s; }
.d3 { transition-delay: 0.3s; }
```

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
        <p><u style="text-decoration: underline; text-underline-offset: 0.15em; text-decoration-skip-ink: none;">{{Q4_Speaker}}</u><sup>1</sup>, {{Other_Authors}}<sup>N</sup></p>
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
        <ul class="bullet-list reveal d1" style="margin-top: 6rem;">
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
        <ul class="bullet-list">
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

### 5.7 6-Image Comparison Grid

Used in TB slides to display multi-threshold / multi-VOV comparison plots (3 columns × 2 rows):

```html
<ul class="bullet-list" style="margin-bottom: 2px;"><li><strong>Run Title</strong></li></ul>
<ul class="bullet-list" style="margin-bottom: 5px; font-size: 0.8em;">
    <li>Top row: <strong>>120 ADC cut</strong> | Bottom row: <strong>>0 ADC cut</strong></li>
</ul>
<div class="image-grid"
    style="grid-template-columns: repeat(3, 1fr); grid-template-rows: 1fr 1fr; gap: 8px; flex: 1; min-height: 0;">
    <div class="figure-frame"><img src="..."><div class="caption">th=3 (>120)</div></div>
    <!-- 6 figure-frames total -->
</div>
```

> **⚠️ Key constraints:**
> - `grid-template-rows: 1fr 1fr` splits two equal rows; combined with `flex: 1; min-height: 0` to prevent overflow
> - Bullets use `margin-bottom: 2px / 5px` compact mode, maximizing space for images
> - `.figure-frame img` is capped at `max-height: 28vh`, ensuring two rows fit within the page

---

## 6. Full JavaScript

The following JS must be embedded **verbatim** inside `<script>` tags (before `</body>`):

> 📌 **Single Source of Truth is the `assets/PKU_{CMS,CEPC}_Classic_Empty.html` template file.**
> This section is only a reference copy for manual AI generation. If inconsistent with the template, the template takes precedence.

```javascript
// 1. Smart Proportional Scaling Engine
function applyScale() {
    const wrapper = document.getElementById('scale-wrapper');
    if (!wrapper) return;
    const targetWidth = 1920;
    const targetHeight = 1080;
    const scale = Math.min(window.innerWidth / targetWidth, window.innerHeight / targetHeight);
    wrapper.style.transform = `translate(-50%, -50%) scale(${scale})`;
}
window.addEventListener('resize', applyScale);

// 2. Interaction Manager
class SlidePresentation {
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
| Speaker underline | `text-underline-offset: 0.15em; text-decoration-skip-ink: none;` |
| Affiliation labels | Superscript numbering `<sup>N</sup>` |
| Footer center | Uses Q4-specified speaker name |
| Transition titles | Must strictly correspond to Outline bullet order |
| Content data-title | Defaults to nearest transition page title |
| Table font | `calc(var(--body-size) * 0.6)` ≈ 20px, follows global |
| Caption font | `calc(var(--body-size) * 0.6)` ≈ 20px, follows global, no hardcoding |
| slide-content padding | `20px 0` (not 60px), maximizes content area |
| Dense bullet mode | `li style="margin-bottom: 10px;"` overrides default 30px, for content-heavy pages |
| 6-image comparison grid | `grid-template-rows: 1fr 1fr; gap: 8px; flex: 1; min-height: 0` |
| data-title LaTeX | `innerHTML` + `MathJax.typesetPromise()` renders formulas in the red bar title |
