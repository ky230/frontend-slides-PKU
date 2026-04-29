# Terminal Box Reference

> Mac-style terminal component for code display and command animation in PKU slides.

---

## 1. Architecture

Two modes:

| Mode | Class | Purpose |
|------|-------|---------|
| **Static Code Display** | `.mac-terminal-lined` | Line-numbered code with syntax highlighting |
| **Dynamic Terminal** | `id="typewriter-terminal"` | Command output with timed line-by-line reveal |

---

## 2. HTML Structure

### 2.1 Static Code Display

```html
<!-- FINE TUNING:
     - .mac-terminal: adjust 'margin-top', 'margin-left', 'width'
     - .mac-terminal-code: adjust 'font-size' if overriding default
     - see FINE_TUNING.md §9
-->
<!-- [ELEMENT: Python Code Display] -->
<div class="mac-terminal" style="--term-accent: #61afef; margin-top: 0; margin-left: 0; width: 100%;">
    <div class="mac-terminal-bar">
        <span class="mac-dot mac-dot-red"></span>
        <span class="mac-dot mac-dot-yellow"></span>
        <span class="mac-dot mac-dot-green"></span>
        <span class="mac-terminal-title">python3 — analysis.py</span>
    </div>
    <div class="mac-terminal-body mac-terminal-lined">
<pre class="mac-terminal-code"><span class="code-line"><span class="term-keyword">import</span> ROOT</span>
<span class="code-line"><span class="term-keyword">def</span> <span class="term-func">analyze</span>(filename):</span>
<span class="code-line">    f = ROOT.TFile(<span class="term-string">"output.root"</span>)</span>
<span class="code-line">    h = f.Get(<span class="term-string">"h_mass"</span>)</span>
<span class="code-line">    <span class="term-keyword">return</span> h.GetMean()  <span class="term-comment"># expected value</span></span></pre>
    </div>
</div>
```

> **Key:** Add `.mac-terminal-lined` to `.mac-terminal-body` → enables VSCode-style line numbers.

### 2.2 Dynamic Terminal (Typewriter)

```html
<!-- [ELEMENT: Terminal Command Output — typewriter animation] -->
<div class="mac-terminal" style="margin-top: 0; margin-left: 0; width: 100%;">
    <div class="mac-terminal-bar">
        <span class="mac-dot mac-dot-red"></span>
        <span class="mac-dot mac-dot-yellow"></span>
        <span class="mac-dot mac-dot-green"></span>
        <span class="mac-terminal-title">leyan@lxplus — ~/analysis</span>
    </div>
    <div class="mac-terminal-body">
<pre class="mac-terminal-code" id="typewriter-terminal"><span class="term-line" data-delay="0"><span class="term-prompt">$</span> <span class="term-cmd">python3</span> run.py</span>
<span class="term-line" data-delay="600"><span class="term-green">Processing events...</span> ✅</span>
<span class="term-line" data-delay="1200"><span class="term-highlight">Done: 1000 events</span></span>
<span class="term-line" data-delay="1800"><span class="term-prompt">$</span> <span class="term-cursor">█</span></span></pre>
    </div>
</div>
```

**Animation mechanism:**
- JS in master template auto-detects `id="typewriter-terminal"`
- Each `.term-line` has `data-delay="N"` (milliseconds) controlling when it appears
- `threshold: 0.5` — animation triggers when 50% of the slide is visible
- Scrolling away resets all lines; scrolling back replays

> **Fine tuning:** Adjust `data-delay` values to control rhythm. See `FINE_TUNING.md §9`.

---

## 3. Syntax Tokens — Dark Theme (Default)

Base palette: [Catppuccin Mocha](https://catppuccin.com/palette)

| Token | Class | Color | Hex | Usage |
|-------|-------|-------|-----|-------|
| Keyword | `.term-keyword` | Purple | `#cba6f7` | `import/def/for/return/if/class/#include` |
| Function | `.term-func` | Blue | `#89b4fa` | function names |
| String | `.term-string` | Green | `#a6e3a1` | string literals |
| Comment | `.term-comment` | Gray | `#6c7086` | comments (italic) |
| Number | `.term-num` | Orange | `#fab387` | numeric literals |
| Highlight | `.term-highlight` | Yellow bg | `#f9e2af` | key values for audience attention |
| Prompt | `.term-prompt` | Green | `#a6e3a1` | terminal `$` |
| Command | `.term-cmd` | Blue | `#89b4fa` | terminal command name |
| Dim | `.term-dim` | Dark gray | `#585b70` | secondary log info |
| Success | `.term-green` | Green | `#a6e3a1` | success messages |
| Type | `.term-type` | Cyan | `#94e2d5` | C++ types: `TH1F`, `vector`, `auto` |
| Tag | `.term-tag` | Red | `#f38ba8` | HTML tags: `<div>`, `<section>` |
| Attribute | `.term-attr` | Yellow | `#f9e2af` | HTML attrs: `class=`, `style=` |

---

## 4. Syntax Tokens — Light Theme

Base palette: [Atom One Light](https://github.com/atom/one-light-syntax)

Overridden in light skin CSS files (`classic.css`, `cobalt.css`, `jade.css`, `lavender.css`):

| Token | Class | Color | Hex |
|-------|-------|-------|-----|
| Keyword | `.term-keyword` | Purple | `#a626a4` |
| Function | `.term-func` | Blue | `#4078f2` |
| String | `.term-string` | Green | `#50a14f` |
| Comment | `.term-comment` | Gray | `#a0a1a7` |
| Number | `.term-num` | Amber | `#986801` |
| Highlight | `.term-highlight` | Red bg | `#e45649` |
| Prompt | `.term-prompt` | Green | `#50a14f` |
| Command | `.term-cmd` | Blue | `#4078f2` |
| Dim | `.term-dim` | Light gray | `#a0a1a7` |
| Success | `.term-green` | Green | `#50a14f` |
| Type | `.term-type` | Teal | `#0184bc` |
| Tag | `.term-tag` | Red | `#e45649` |
| Attribute | `.term-attr` | Amber | `#986801` |

---

## 5. Language Tagging Examples

### Python
```html
<span class="term-keyword">import</span> ROOT
<span class="term-keyword">def</span> <span class="term-func">analyze</span>(f):
    h = f.Get(<span class="term-string">"h_mass"</span>)
    <span class="term-keyword">return</span> h.Integral()  <span class="term-comment"># total yield</span>
```

### C / C++
```html
<span class="term-keyword">#include</span> <span class="term-string">&lt;TH1F.h&gt;</span>
<span class="term-keyword">class</span> <span class="term-type">Analyzer</span> {
  <span class="term-keyword">void</span> <span class="term-func">produce</span>(<span class="term-type">edm::Event</span>&amp; e) {
    <span class="term-keyword">auto</span> score = model_.<span class="term-func">forward</span>({input});
  }
};
```

### JavaScript
```html
<span class="term-keyword">const</span> observer = <span class="term-keyword">new</span> <span class="term-type">IntersectionObserver</span>(
  (<span class="term-func">entries</span>) =&gt; {
    <span class="term-keyword">if</span> (entry.isIntersecting) { <span class="term-func">play</span>(); }
  }, { <span class="term-attr">threshold</span>: <span class="term-num">0.5</span> }
);
```

### HTML
```html
<span class="term-tag">&lt;section</span> <span class="term-attr">class</span>=<span class="term-string">"slide"</span><span class="term-tag">&gt;</span>
  <span class="term-tag">&lt;div</span> <span class="term-attr">class</span>=<span class="term-string">"highlight-box"</span><span class="term-tag">&gt;</span>
    <span class="term-highlight">&lt;strong&gt;Result&lt;/strong&gt;</span>
  <span class="term-tag">&lt;/div&gt;</span>
<span class="term-tag">&lt;/section&gt;</span>
```

### Rust
```html
<span class="term-keyword">fn</span> <span class="term-func">compute</span>(masses: &amp;[<span class="term-type">f64</span>]) -&gt; <span class="term-type">HashMap</span>&lt;<span class="term-type">u32</span>, <span class="term-type">f64</span>&gt; {
    <span class="term-keyword">let mut</span> r = <span class="term-type">HashMap</span>::<span class="term-func">new</span>();
    <span class="term-keyword">for</span> &amp;m <span class="term-keyword">in</span> masses {
        r.<span class="term-func">insert</span>(m <span class="term-keyword">as</span> <span class="term-type">u32</span>, <span class="term-highlight">limit.expected</span>);
    }
    r
}
```

---

## 6. Typewriter Animation

| Parameter | Location | Range | Default | Description |
|-----------|----------|-------|---------|-------------|
| `data-delay` | `.term-line` attr | 0–5000 ms | per-line | Delay before this line appears |
| `threshold` | JS observer | 0–1.0 | 0.5 | Viewport fraction to trigger animation |
| `id` | `<pre>` element | — | `typewriter-terminal` | Must be this exact ID for auto-detection |

**Behavior:**
1. Slide scrolls into view (50%+ visible) → animation starts
2. Each `.term-line` appears after its `data-delay` milliseconds
3. Slide scrolls out → all lines reset (hidden)
4. Scroll back → animation replays from start

---

## 7. CSS Custom Properties (Skin Overrides)

| Variable | Default (Dark) | Light Override | Usage |
|----------|---------------|----------------|-------|
| `--term-accent` | `#39d353` | `#39d353` | Dot/accent color |
| Terminal bar bg | `#3a3a3c → #2c2c2e` | `#e8e8ea → #d4d4d8` | Title bar gradient |
| `.mac-terminal-body` bg | `#1e1e2e` | `#fafafa` | Code body background |
| `.mac-terminal-code` color | `#cdd6f4` | `#383a42` | Default text color |
| `.mac-terminal` border | `rgba(255,255,255,0.08)` | `rgba(0,0,0,0.1)` | Outer border |

---

## 8. Fine Tuning Knobs

→ See `FINE_TUNING.md §9` for complete parameter table (container layout, per-terminal knobs, `data-delay`).
