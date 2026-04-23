# Figure Layout System — Quick Reference

> **核心原则：改几个数字 = 控制图的位置和大小**

---

## 1. 旋钮 (CSS Custom Properties)

在任何 `.fig` 容器上，通过 `style="--变量名:值"` 微调：

| 旋钮 | 作用 | 写法示例 | 默认值 |
|------|------|---------|-------|
| `--w` | 图片宽度 | `--w:80%` | `100%` |
| `--h` | 图片高度 | `--h:35vh` | 按预设自动 |
| `--x` | 左右移动 | `--x:30px`（右移） / `--x:-30px`（左移） | `0px` |
| `--y` | 上下移动 | `--y:-20px`（上移） / `--y:20px`（下移） | `0px` |
| `--gap` | 图间距 | `--gap:8px` | `15px` |
| `--split` | 双栏比例 | `--split: 1fr 1fr` | `4fr 6fr` |
| `--cap-size` | 图例字号 | `--cap-size:20px` | 自动 (~17px) |
| `--cap-y` | 图例上下偏移 | `--cap-y:-5px`（上移） | `0px` |

```html
<!-- fig-1: 单图 | --w --h --x --y --gap --cap-size --cap-y -->
<div class="fig fig-1" style="--w:80%; --y:-20px;">
    <div class="figure-frame">
        <img src="plot.png">
        <div class="caption">Run 4482, VoV=3V</div>
    </div>
</div>
```

> **图例默认不显示**。只有在 `<div class="figure-frame">` 中写了 `<div class="caption">` 才会出现。
> 图例自动居于图片底部中央，字号自适配。要调就改 `--cap-size` 或 `--cap-y`。

---

## 2. 预设布局 (支持 1×1 到 4×4)

### `.fig-1` — 单张大图
```
┌───────────────────┐
│                   │
│     ┌───────┐     │
│     │  IMG  │     │
│     └───────┘     │
│                   │
└───────────────────┘
```
**HEP 用途：** 单张拟合图、Landau fit、时间分辨率对比图

```html
<div class="fig fig-1">
    <img src="fit_result.png">
</div>
```

---

### `.fig-1x2` — 1行×2列
```
┌─────────┬─────────┐
│         │         │
│  IMG 1  │  IMG 2  │
│         │         │
└─────────┴─────────┘
```
**HEP 用途：** Before/After 对比（有/无 cut）、L/R channel 对比

```html
<div class="fig fig-1x2" style="--h:60vh;">
    <div class="figure-frame"><img src="no_cut.png"><div class="caption">Without cut</div></div>
    <div class="figure-frame"><img src="with_cut.png"><div class="caption">With 78 ADC cut</div></div>
</div>
```

---

### `.fig-1x3` — 1行×3列
```
┌──────┬──────┬──────┐
│      │      │      │
│ IMG1 │ IMG2 │ IMG3 │
│      │      │      │
└──────┴──────┴──────┘
```
**HEP 用途：** 三个阈值 / 三个 VoV 对比

```html
<div class="fig fig-1x3" style="--gap:10px;">
    <div class="figure-frame"><img src="th5.png"><div class="caption">th=5</div></div>
    <div class="figure-frame"><img src="th10.png"><div class="caption">th=10</div></div>
    <div class="figure-frame"><img src="th20.png"><div class="caption">th=20</div></div>
</div>
```

---

### `.fig-2x1` — 2行×1列
```
┌───────────────────┐
│     ┌───────┐     │
│     │ IMG 1 │     │
│     └───────┘     │
│     ┌───────┐     │
│     │ IMG 2 │     │
│     └───────┘     │
└───────────────────┘
```
**HEP 用途：** 上下堆叠（如 singleHit + doubleHit 同一 bar）

```html
<div class="fig fig-2x1">
    <img src="single_hit.png">
    <img src="double_hit.png">
</div>
```

---

### `.fig-2x2` — 2行×2列
```
┌─────────┬─────────┐
│  IMG 1  │  IMG 2  │
├─────────┼─────────┤
│  IMG 3  │  IMG 4  │
└─────────┴─────────┘
```
**HEP 用途：** singleHit/doubleHit × 有/无 cut 四图对比

```html
<div class="fig fig-2x2" style="--gap:8px; --h:38vh;">
    <div class="figure-frame"><img src="sh_nocut.png"><div class="caption">SingleHit, no cut</div></div>
    <div class="figure-frame"><img src="sh_cut.png"><div class="caption">SingleHit, with cut</div></div>
    <div class="figure-frame"><img src="dh_nocut.png"><div class="caption">DoubleHit, no cut</div></div>
    <div class="figure-frame"><img src="dh_cut.png"><div class="caption">DoubleHit, with cut</div></div>
</div>
```

---

### `.fig-2x3` — 2行×3列 (TB 经典)
```
┌──────┬──────┬──────┐
│ IMG1 │ IMG2 │ IMG3 │
├──────┼──────┼──────┤
│ IMG4 │ IMG5 │ IMG6 │
└──────┴──────┴──────┘
```
**HEP 用途：** 3 threshold × ±cut 六图网格（TB meeting 最常见）

```html
<div class="fig fig-2x3" style="--gap:8px;">
    <div class="figure-frame"><img src="th5_nocut.png"><div class="caption">th=5 (no cut)</div></div>
    <div class="figure-frame"><img src="th10_nocut.png"><div class="caption">th=10 (no cut)</div></div>
    <div class="figure-frame"><img src="th20_nocut.png"><div class="caption">th=20 (no cut)</div></div>
    <div class="figure-frame"><img src="th5_cut.png"><div class="caption">th=5 (with cut)</div></div>
    <div class="figure-frame"><img src="th10_cut.png"><div class="caption">th=10 (with cut)</div></div>
    <div class="figure-frame"><img src="th20_cut.png"><div class="caption">th=20 (with cut)</div></div>
</div>
```

---

### `.fig-3x2` — 3行×2列
```
┌─────────┬─────────┐
│  IMG 1  │  IMG 2  │
├─────────┼─────────┤
│  IMG 3  │  IMG 4  │
├─────────┼─────────┤
│  IMG 5  │  IMG 6  │
└─────────┴─────────┘
```
**HEP 用途：** 六图竖排（如 6 个 bar pair 各一张）

```html
<div class="fig fig-3x2" style="--gap:6px;">
    <img src="bar2.png"><img src="bar3.png">
    <img src="bar4.png"><img src="bar5.png">
    <img src="bar6.png"><img src="bar7.png">
</div>
```

---

### `.fig-3x3` — 3行×3列 (九宫格)
```
┌──────┬──────┬──────┐
│ IMG1 │ IMG2 │ IMG3 │
├──────┼──────┼──────┤
│ IMG4 │ IMG5 │ IMG6 │
├──────┼──────┼──────┤
│ IMG7 │ IMG8 │ IMG9 │
└──────┴──────┴──────┘
```
**HEP 用途：** 3 VoV × 3 threshold 九宫格

```html
<div class="fig fig-3x3" style="--gap:5px;">
    <img src="v1_t1.png"><img src="v1_t2.png"><img src="v1_t3.png">
    <img src="v2_t1.png"><img src="v2_t2.png"><img src="v2_t3.png">
    <img src="v3_t1.png"><img src="v3_t2.png"><img src="v3_t3.png">
</div>
```

---

### `.fig-3x1` — 3行×1列

```html
<!-- fig-3x1: 3行×1列 | --w --h --x --y --gap -->
<div class="fig fig-3x1">
    <img src="a.png"><img src="b.png"><img src="c.png">
</div>
```

---

### `.fig-4x1` — 4行×1列

```html
<!-- fig-4x1: 4行×1列 | --w --h --x --y --gap -->
<div class="fig fig-4x1">
    <img src="a.png"><img src="b.png"><img src="c.png"><img src="d.png">
</div>
```

---

### `.fig-4x2` — 4行×2列

```html
<!-- fig-4x2: 4行×2列 | --w --h --x --y --gap -->
<div class="fig fig-4x2" style="--gap:6px;">
    <img src="1.png"><img src="2.png">
    <img src="3.png"><img src="4.png">
    <img src="5.png"><img src="6.png">
    <img src="7.png"><img src="8.png">
</div>
```

---

### `.fig-4x3` — 4行×3列

```html
<!-- fig-4x3: 4行×3列 | --w --h --x --y --gap -->
<div class="fig fig-4x3" style="--gap:5px;">
    <!-- 12 images -->
</div>
```

---

### `.fig-1x4` — 1行×4列

**HEP 用途：** 四个阈值 / 四个 VoV 横排对比

```html
<!-- fig-1x4: 1行×4列 | --w --h --x --y --gap -->
<div class="fig fig-1x4" style="--gap:10px;">
    <img src="a.png"><img src="b.png"><img src="c.png"><img src="d.png">
</div>
```

---

### `.fig-2x4` — 2行×4列

```html
<!-- fig-2x4: 2行×4列 | --w --h --x --y --gap -->
<div class="fig fig-2x4" style="--gap:8px;">
    <!-- 8 images -->
</div>
```

---

### `.fig-3x4` — 3行×4列

```html
<!-- fig-3x4: 3行×4列 | --w --h --x --y --gap -->
<div class="fig fig-3x4" style="--gap:6px;">
    <!-- 12 images -->
</div>
```

---

### `.fig-4x4` — 4行×4列 (十六宫格)

```html
<!-- fig-4x4: 4行×4列 | --w --h --x --y --gap -->
<div class="fig fig-4x4" style="--gap:5px;">
    <!-- 16 images -->
</div>
```

---

## 3. 与 `.dual-layout` 组合

### `--split` 变量控制左右比例

```html
<!-- 默认 4:6 (左文右图) -->
<div class="dual-layout">
    <div class="left-col">bullets...</div>
    <div class="right-col">
        <div class="fig fig-1"><img src="plot.png"></div>
    </div>
</div>

<!-- 等分 -->
<div class="dual-layout" style="--split: 1fr 1fr;">...</div>

<!-- 左宽右窄 -->
<div class="dual-layout" style="--split: 6fr 4fr;">...</div>
```

---

## 4. Caption 样式

每个 `.figure-frame` 可选加 `.caption`：

```html
<div class="figure-frame">
    <img src="plot.png">
    <div class="caption">Run 4482, VoV=3V, th=10</div>
</div>
```

Caption 自动继承 `calc(var(--body-size) * 0.5)` 字号，居中灰色文字。

---

## 5. AI 生成规则：Inline Comment 必须

> **⚠️ MANDATORY**：AI 在生成任何包含 `.fig` 的 HTML 时，**必须**在 `<div class="fig ...">` 上方加一行注释，格式为：
> ```html
> <!-- fig-RxC: R行×C列 | --w --h --x --y --gap --cap-size --cap-y -->
> ```
> 这样用户看源码时一目了然，知道可以改什么数字。

---

## 6. 常用组合速查

| 场景 | 写法 |
|------|------|
| 单图满宽 | `<div class="fig fig-1"><img src="..."></div>` |
| 单图 80% 宽 | `<div class="fig fig-1" style="--w:80%;"><img src="..."></div>` |
| 单图上移 20px | `<div class="fig fig-1" style="--y:-20px;"><img src="..."></div>` |
| 左右对比 | `<div class="fig fig-1x2">` |
| 六图 TB 网格 | `<div class="fig fig-2x3" style="--gap:8px;">` |
| 4列横排 | `<div class="fig fig-1x4">` |
| 左文右图 (等分) | `<div class="dual-layout" style="--split: 1fr 1fr;">` |
| 图高限制 35vh | 加 `style="--h:35vh;"` |
| 图例放大字号 | 加 `style="--cap-size:24px;"` |
| 图例上移 | 加 `style="--cap-y:-5px;"` |

---

## 7. 向后兼容

旧的 `.image-grid` 和手写 inline style 仍然完全正常工作。`.fig` 系统是**新增**的，不修改任何已有 CSS。

