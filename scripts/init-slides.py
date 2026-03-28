#!/usr/bin/env python3
"""
init-slides.py — PKU Academic Classic Slide Harness Scaffold

从空白模板初始化 HTML 幻灯片骨架。
自动生成：Title Slide, Outline, 各 Section 的过渡页 + 内容占位页。

Usage:
    python3 init-slides.py \\
        --template CMS \\
        --title "BTL time resolution..." \\
        --author "Leyan Li" \\
        --event "TB meeting" \\
        --outline "Motivation" "Analysis" "Back Up" \\
        --out /path/to/output.html
"""

import argparse
import os
import re
import sys


def main():
    parser = argparse.ArgumentParser(
        description="PKU Academic Classic Slide Harness — 初始化幻灯片骨架"
    )
    parser.add_argument(
        "--template", required=True, choices=["CMS", "CEPC"],
        help="品牌模板: CMS 或 CEPC"
    )
    parser.add_argument("--title", required=True, help="报告主标题")
    parser.add_argument("--subtitle", default="", help="副标题 (可选)")
    parser.add_argument("--author", required=True, help="作者列表 (逗号分隔, 用 :N 标注单位编号, 如 'Alice:1, Bob:2')")
    parser.add_argument("--speaker", default="Leyan Li", help="演讲者 (自动加下划线，默认为 Leyan Li)")
    parser.add_argument("--affiliations", nargs="+", default=["Peking University (CN)"], help="单位列表 (按序自动编号, 如 'PKU (CN)' 'INFN (IT)')")
    parser.add_argument("--date", default="", help="报告日期")
    parser.add_argument("--reference", default="", help="Reference 引用 (格式: 'nickname|url' 或纯 url)")
    parser.add_argument("--event", required=True, help="会议/报告类型 (显示在 footer-right)")
    parser.add_argument(
        "--outline", nargs="*", default=[],
        help='Outline sections 列表, 如: "Motivation:2" "Analysis:4" "Back Up:1" (:后代表预期内容页数，默认为1)'
    )
    parser.add_argument("--out", required=True, help="输出 HTML 文件路径")
    parser.add_argument(
        "--highlight", nargs="*", default=[],
        help='标题关键词高亮列表 (黄色), 如: "time resolution" "preliminary"'
    )
    args = parser.parse_args()

    # 1. 读取空白模板
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(
        script_dir, "..", "assets", f"PKU_{args.template}_Classic_Empty.html"
    )

    if not os.path.exists(template_path):
        print(f"❌ Template not found: {template_path}", file=sys.stderr)
        sys.exit(1)

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 2. Logo 路径：相对 → 仓库绝对路径（确保任意输出目录都能预览）
    repo_root = os.path.normpath(os.path.join(script_dir, ".."))
    assets_abs = os.path.join(repo_root, "assets")
    html = html.replace('src="assets/', f'src="{assets_abs}/')

    # 3. 标题高亮处理：将关键词包裹为 <span class="highlight-yellow">
    highlighted_title = args.title
    for kw in args.highlight:
        highlighted_title = re.sub(
            re.escape(kw),
            f'<span class="highlight-yellow">{kw}</span>',
            highlighted_title,
            flags=re.IGNORECASE
        )

    # 4. 替换占位符 (footer 也用高亮版标题)
    html = html.replace("{{TITLE_PLACEHOLDER}}", highlighted_title)
    html = html.replace("{{AUTHOR_PLACEHOLDER}}", args.speaker)
    html = html.replace("{{EVENT_PLACEHOLDER}}", args.event)

    # 5. 生成 Slide 注入内容
    injections = []
    slide_idx = 1

    # --- Title Slide ---
    subtitle_html = ""
    if args.subtitle:
        subtitle_html = f'\n            <h2>{args.subtitle}</h2>'

    # 演讲者下划线 + 单位上标处理
    authors = [a.strip() for a in args.author.split(",")]
    author_parts = []
    for a in authors:
        # 解析 Name:N 格式
        if ":" in a:
            name, affil_num = a.rsplit(":", 1)
            name = name.strip()
            affil_num = affil_num.strip()
            sup = f'<sup>{affil_num}</sup>'
        else:
            name = a.strip()
            sup = ''
        if name == args.speaker:
            author_parts.append(
                f'<u style="text-decoration: underline; text-underline-offset: 0.15em; '
                f'text-decoration-skip-ink: none;">{name}</u>{sup}'
            )
        else:
            author_parts.append(f'{name}{sup}')
    author_line = ", ".join(author_parts)

    # 单位列表自动编号 + 换行
    affil_parts = []
    for i, aff in enumerate(args.affiliations, 1):
        affil_parts.append(f'<sup>{i}</sup> {aff}')
    affil_line = "<br>".join(affil_parts)

    date_html = ""
    if args.date:
        date_sup = re.sub(r'(\d+)(st|nd|rd|th)\b', r'\1<sup>\2</sup>', args.date)
        date_html = f'\n            <p style="margin-top: 2rem; font-size: 0.8em;">{date_sup}</p>'

    ref_html = ""
    if args.reference:
        if "|" in args.reference:
            nickname, url = args.reference.split("|", 1)
            ref_html = f'\n            <p style="font-size: 0.8em;">Reference: <a href="{url.strip()}" target="_blank" style="color: #0000EE; text-decoration: underline; text-underline-offset: 0.15em; text-decoration-skip-ink: none;">{nickname.strip()}</a></p>'
        else:
            ref_html = f'\n            <p style="font-size: 0.8em;">Reference: <a href="{args.reference}" target="_blank" style="color: #0000EE; text-decoration: underline; text-underline-offset: 0.15em; text-decoration-skip-ink: none;">{args.reference}</a></p>'

    injections.append(f"""
    <!-- [Slide {slide_idx}] Title Slide -->
    <section class="slide title-slide visible" data-header="hidden" data-title="">
        <div class="title-banner reveal d1">
            <h1>{highlighted_title}</h1>{subtitle_html}
        </div>
        <div class="author-info reveal d2">
            <p>{author_line}</p>
            <p style="margin-top: 1rem;">{affil_line}</p>{date_html}{ref_html}
        </div>
    </section>""")
    slide_idx += 1

    # --- Outline Page ---
    if args.outline:
        lis = "\n                ".join(
            [f"<li><strong>{sec.rsplit(':', 1)[0].strip()}</strong></li>" for sec in args.outline]
        )
        injections.append(f"""
    <!-- [Slide {slide_idx}] Outline -->
    <section class="slide normal-slide" data-header="visible" data-title="Outline">
        <div class="slide-content">
            <ul class="bullet-list reveal d1" style="margin-top: 6rem;">
                {lis}
            </ul>
        </div>
    </section>""")
        slide_idx += 1

        # --- 每个 Section 生成: 过渡页 + 内容占位页 ---
        for sec in args.outline:
            parts = sec.rsplit(":", 1)
            title = parts[0].strip()
            count = 1
            if len(parts) > 1 and parts[1].isdigit():
                count = int(parts[1])

            # 过渡页
            injections.append(f"""
    <!-- [Slide {slide_idx}] Transition: {title} -->
    <section class="slide transition-slide" data-header="hidden" data-title="">
        <div class="transition-text reveal d1">{title}</div>
    </section>""")
            slide_idx += 1

            # 内容占位页
            for c in range(count):
                placeholder_suffix = f" {c+1}" if count > 1 else ""
                injections.append(f"""
    <!-- [Slide {slide_idx}] Content: {title} -->
    <section class="slide normal-slide" data-header="visible" data-title="{title}">
        <div class="slide-content reveal d1">
            <ul class="bullet-list">
                <li>{title} content placeholder{placeholder_suffix}</li>
            </ul>
        </div>
    </section>""")
                slide_idx += 1

    # 6. 注入到模板
    injection_html = "\n".join(injections) + "\n    <!-- END slides-scroller -->"
    html = html.replace("<!-- END slides-scroller -->", injection_html)

    # 7. 写入输出
    out_path = os.path.abspath(args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    total = slide_idx - 1
    print(f"✅ Slide harness created successfully at {out_path}")
    print(f"   Total slides: {total}")
    if args.outline:
        print(f"   Outline sections: {len(args.outline)}")
        for i, sec in enumerate(args.outline, 1):
            parts = sec.rsplit(":", 1)
            title = parts[0].strip()
            count = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1
            print(f"     {i}. {title} (Allocated {count} pages)")


if __name__ == "__main__":
    main()
