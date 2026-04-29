# Fine-Tuning Cheat Sheet

> **核心：调 slide 就是调这 12 个参数**

---

## 1. Bullet Text

| Adjustment | Property | Where | Range | Default | Example |
|------------|----------|-------|-------|---------|---------|
| **Vertical position** | `top` | Container `<div>` | 50–200px | 100px | `top: 150px` |
| **Horizontal position** | `left` | Container `<div>` | -20–40px | 0px | `left: 5px` |
| **Region width** | `width` | Container `<div>` | 40–100% | 48% | `width: 55%` |
| **Font size** | `font-size` | `<ul>` element | 1.4–2.0em | 1.85em | `font-size: 1.6em` |
| **Left margin** (fine) | `margin-left` | `<ul>` element | -80–40px | 0 | `margin-left: -30px` |
| **Line density** | `margin-bottom` | `<li>` element | 4–30px | 30px (8px dense) | `margin-bottom: 8px` |

> **-80px margin-left** = flush with red title bar left edge.
> **margin-bottom: 8px** = "dense mode" for content-heavy slides.

---

## 2. Images

| Adjustment | Property | Where | Range | Default | Example |
|------------|----------|-------|-------|---------|---------|
| **Vertical position** | `top` | Container `<div>` | 50–200px | 70px | `top: 100px` |
| **Horizontal position** | `right` or `left` | Container `<div>` | 0–50px | 0px | `right: 20px` |
| **Region width** | `width` | Container `<div>` | 40–100% | 55% | `width: 50%` |
| **Grid gap** | `gap` | Grid `<div>` | 2–15px | 10px | `gap: 6px` |
| **Individual image width** | `width` | `<img>` | 80–100% | 100% | `width: 90%` |

---

## 3. Tables

| Adjustment | Property | Where | Range | Default | Example |
|------------|----------|-------|-------|---------|---------|
| **Font size** | `font-size` | `<table>` | 0.5–0.85em | 0.6em | `font-size: 0.75em` |
| **Horizontal offset** | `margin-left` | `<table>` | -40–40px | 0 | `margin-left: -20px` |
| **Table width** | `width` | `<table>` | 80–120% | 100% | `width: 110%` |
| **Cell padding** | `padding` | `<th>/<td>` | 2–12px | 10px 15px | `padding: 3px 8px` |
| **Header background** | `background` | `<tr>` | — | `var(--theme-primary)` | `rgba(139,0,0,0.08)` (light) |

> **Nested tables** (inside `<li>`): Use `font-size: 0.75em` on `<table>` for proportional sizing relative to bullet text.

---

## 4. Footnotes / Annotations

| Adjustment | Property | Where | Range | Default | Example |
|------------|----------|-------|-------|---------|---------|
| **Font size** | `font-size` | Footer `<div>` | 0.7–0.9em | 0.85em | `font-size: 0.85em` |
| **Top spacing** | `margin-top` | Footer `<div>` | 2–20px | 6px | `margin-top: 10px` |
| **Left offset** | `margin-left` | Footer `<div>` | -30–0px | -20px | `margin-left: -20px` |

---

## 5. Layout Systems

### dual-layout (Left-Right Grid)

| Adjustment | Property | Where | Range | Default | Example |
|------------|----------|-------|-------|---------|---------|
| **Column ratio** | `--split` | `.dual-layout` | `3fr 7fr` to `7fr 3fr` | `4fr 6fr` | `--split: 1fr 1fr` |
| **Top offset** | `margin-top` | `.dual-layout` | 0–80px | 0.5rem | `margin-top: 40px` |
| **Column gap** | `gap` | `.dual-layout` | 10–60px | 40px | `gap: 1rem` |

### Absolute-Position (Independent Elements)

```html
<div class="slide-content" style="position: relative; overflow: visible;">
    <!-- Element 1: position: absolute; top: ___; left: ___; width: ___; -->
    <!-- Element 2: position: absolute; top: ___; right: ___; width: ___; -->
</div>
```

> **Key rule:** Parent = `position: relative`. Children = `position: absolute`.
> **Position knobs:** `top`, `left` (or `right`), `width`.

---

## 6. Figure Grid System (`.fig`)

| Adjustment | CSS Variable | Range | Default | Example |
|------------|-------------|-------|---------|---------|
| **Image width** | `--w` | 60–100% | 100% | `--w: 80%` |
| **Image height** | `--h` | 20–70vh | Per preset | `--h: 35vh` |
| **Horizontal shift** | `--x` | -50–50px | 0px | `--x: -20px` |
| **Vertical shift** | `--y` | -50–50px | 0px | `--y: -10px` |
| **Grid gap** | `--gap` | 2–15px | 15px | `--gap: 8px` |
| **Caption font** | `--cap-size` | 14–24px | auto | `--cap-size: 18px` |
| **Caption offset** | `--cap-y` | -10–10px | 0px | `--cap-y: -5px` |

> **Best for:** Image-only regions (backup slides, full-page plots).
> **Not for:** Mixed bullet+image slides → use Absolute-Position instead.

---

## 7. Highlight Boxes

| Box Type | Class | Border Color | Use Case |
|----------|-------|-------------|----------|
| Red conclusion | `.highlight-box` | `var(--theme-highlight)` | Key results, status summary |
| Blue note | `.important-box` | `#3b82f6` | Technical details, methodology |
| Orange warning | `.warning-box` | `#f59e0b` | Caveats, limitations |
| Green tip | `.tip-box` | `#22c55e` | Recommendations, next steps |

---

## 7.5. Inline Text Highlight

Use `.highlight-accent` to highlight key terms inside bullet text. Color follows `--theme-highlight` (default: PKU-Red `#cc0000` on light backgrounds).

```html
<!-- Basic highlight -->
<li>The observed <span class="highlight-accent">excess at 95 GeV</span> is 2.8σ local.</li>

<!-- Bold + highlight -->
<li>Result: <strong><span class="highlight-accent">μ = 1.03 ± 0.12</span></strong></li>

<!-- Highlight inside sub-bullet -->
<li>Systematic uncertainties:
    <ul>
        <li><span class="highlight-accent">JES</span> dominates the btag category</li>
    </ul>
</li>
```

> **颜色由框架自动管理**: 正文页使用 `--theme-highlight`，扉页由框架自动适配，用户无需额外处理。

---

## 8. Quick Recipes

### Dense bullet page (many points)
```html
<li style="margin-bottom: 8px;">Point here</li>  <!-- vs default 30px -->
```

### Push bullets left for more space
```html
<ul class="bullet-list" style="margin-left: -40px; font-size: 1.6em;">
```

### Full-width image page (no bullets)
```html
<div class="slide-content" style="position: relative;">
    <!-- [IMAGES]: desc | KNOBS: top(3%), left(-3.5%), width(110%) -->
    <div style="position: absolute; top: 3%; left: -3.5%; width: 110%;">
        <div class="fig fig-2x4" style="--gap: 10px;">
            <img src="..."> <!-- repeat for each image -->
        </div>
    </div>
</div>
```

### Nested table inside bullet
```html
<li>Description:
    <table style="font-size: 0.75em; margin-top: 6px; margin-left: -20px; width: 110%;">
        <tr><th>Col A</th><th>Col B</th></tr>
        <tr><td>val</td><td>val</td></tr>
    </table>
</li>
```

---

## 9. Terminal & Code Blocks (`.mac-terminal`)

### 9.1 Container-Level Layout

| Adjustment | Property | Where | Range | Default | Example |
|------------|----------|-------|-------|---------|---------|
| **Overall top offset** | `margin-top` | `.slide-content` | -40–60px | 0 | `margin-top: 20px` |
| **Overall left offset** | `padding-left` | `.slide-content` | 0–60px | 0 | `padding-left: 30px` |
| **Two-col gap** | `gap` | `.two-col` | 10–60px | 30px | `gap: 20px` |
| **Two-col top** | `margin-top` | `.two-col` | -40–60px | 0 | `margin-top: 10px` |
| **Column vertical** | `padding-top` | `.left-col` / `.right-col` | 0–40px | 0 | `padding-top: 10px` |

### 9.2 Per-Terminal Knobs

| Adjustment | Property | Where | Range | Default | Example |
|------------|----------|-------|-------|---------|---------|
| **Terminal accent** | `--term-accent` | `.mac-terminal` | any color | `#39d353` | `--term-accent: #89b4fa` |
| **Terminal top** | `margin-top` | `.mac-terminal` | -20–40px | 0 | `margin-top: 10px` |
| **Terminal left** | `margin-left` | `.mac-terminal` | -20–40px | 0 | `margin-left: -10px` |
| **Terminal width** | `width` | `.mac-terminal` | 80–110% | 100% | `width: 105%` |
| **Code font size** | `font-size` | `.mac-terminal-code` | 11–16px | clamp(11px,1.3vw,14px) | `font-size: 13px` |
| **Code line-height** | `line-height` | `.mac-terminal-code` | 1.4–2.0 | 1.65 | `line-height: 1.5` |
| **Stacked gap** | `gap` | Column wrapper | 10–40px | 20px | `gap: 15px` |
| **Line reveal delay** | `data-delay` | `.term-line` | 0–5000ms | per-line | `data-delay="800"` |
| **Viewport trigger** | `threshold` | JS observer | 0–1.0 | 0.5 | (code change only) |

### 9.3 Element Labels (Required)

When a slide contains **2+ terminals**, each terminal **must** have a `<!-- [ELEMENT] -->` comment above it:

```html
<!-- [LEFT: Terminal Command Output] -->
<div class="mac-terminal" style="margin-top: 0; margin-left: 0; width: 100%;">
    ...
</div>

<!-- [RIGHT: Python Code Display] -->
<div class="mac-terminal" style="--term-accent: #61afef; margin-top: 0; margin-left: 0; width: 100%;">
    ...
</div>
```

> **Rule:** Every `.mac-terminal` must expose `margin-top`, `margin-left`, `width` in `style=""`. Every `.mac-terminal-code` inside it must expose `font-size` if overriding the default.
