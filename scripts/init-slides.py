#!/usr/bin/env python3
"""
init-slides.py — PKU Academic Classic Slide Harness Scaffold

Initialize HTML slide skeleton from empty template.
Auto-generates: Title Slide, Outline, Transition + Content placeholder pages per Section.

Usage:
    python3 init-slides.py \\
        --logos PKU_logo.jpeg CMS_logo.png \\
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


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))

SKIN_CHOICES = sorted(
    os.path.splitext(f)[0]
    for f in os.listdir(os.path.join(REPO_ROOT, "assets", "skins"))
    if f.endswith(".css") and not f.endswith(".example")
)


def main():
    parser = argparse.ArgumentParser(
        description="PKU Academic Classic Slide Harness — scaffold initialization"
    )
    parser.add_argument(
        "--logos", nargs="*", default=["PKU_logo.jpeg", "CMS_logo.png"],
        help="Logo filenames (in assets/logos/), left-to-right order, default: PKU + CMS"
    )
    parser.add_argument("--title", required=True, help="Report main title")
    parser.add_argument("--subtitle", default="", help="Subtitle (optional)")
    parser.add_argument("--author", required=True, help="Author list (comma-separated, use :N for affiliation number, e.g. 'Alice:1, Bob:2')")
    parser.add_argument("--speaker", default="Leyan Li", help="Speaker (auto-underlined on title, default: Leyan Li)")
    parser.add_argument("--affiliations", nargs="+", default=["Peking University (CN)"], help="Affiliation list (auto-numbered in order, e.g. 'PKU (CN)' 'INFN (IT)')")
    parser.add_argument("--date", default="", help="Report date")
    parser.add_argument("--reference", default="", help="Reference citation (format: 'nickname|url' or plain url)")
    parser.add_argument("--event", required=True, help="Meeting/report type (shown in footer-right)")
    parser.add_argument(
        "--outline", nargs="*", default=[],
        help='Outline sections, e.g. "Motivation:2" "Analysis:4" "Back Up:1" (:N = expected content pages, default 1)'
    )
    parser.add_argument("--out", required=True, help="Output HTML file path")
    parser.add_argument(
        "--highlight", nargs="*", default=[],
        help='Title keyword highlight list (yellow), e.g. "time resolution" "preliminary"'
    )
    parser.add_argument(
        "--skin", default="classic", choices=SKIN_CHOICES,
        help="Color skin (default: classic = PKU Red-Yellow-White)"
    )
    args = parser.parse_args()

    # 1. Read empty template
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(
        script_dir, "..", "assets", "templates", "Empty_template.html"
    )

    if not os.path.exists(template_path):
        print(f"❌ Template not found: {template_path}", file=sys.stderr)
        sys.exit(1)

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 2. Logo injection: scan assets/logos/ and replace placeholder
    repo_root = os.path.normpath(os.path.join(script_dir, ".."))
    logos_dir = os.path.join(repo_root, "assets", "logos")
    logo_imgs = []
    for logo_name in args.logos:
        logo_path = os.path.join(logos_dir, logo_name)
        if not os.path.exists(logo_path):
            print(f"⚠️  Logo not found: {logo_path}, skipping", file=sys.stderr)
            continue
        logo_abs = os.path.abspath(logo_path)
        alt = logo_name.rsplit('.', 1)[0].replace('_', ' ')
        logo_imgs.append(f'            <img src="{logo_abs}" class="logo-img" alt="{alt}">')
    logo_html = "\n".join(logo_imgs) if logo_imgs else "            <!-- no logos -->"
    html = html.replace("<!-- LOGO_PLACEHOLDER -->", logo_html)

    assets_abs = os.path.join(repo_root, "assets")
    skin_css = ""
    skin_font_link = ""
    if args.skin:
        skin_path = os.path.join(assets_abs, "skins", f"{args.skin}.css")
        if not os.path.exists(skin_path):
            if args.skin == "diy":
                print("❌ diy.css not found! Create it first:", file=sys.stderr)
                print(f"   cp {os.path.join(assets_abs, 'skins', 'diy.css.example')} {skin_path}", file=sys.stderr)
                sys.exit(1)
            print(f"⚠️  Skin file not found: {skin_path}, using classic", file=sys.stderr)
        else:
            with open(skin_path, "r", encoding="utf-8") as sf:
                skin_content = sf.read()
            # Extract Google Fonts URL from comment
            font_match = re.search(r'/\* Google Fonts: (.+?) \*/', skin_content)
            if font_match:
                font_families = font_match.group(1).strip()
                if font_families != "none":
                    skin_font_link = (
                        f'    <link rel="stylesheet" '
                        f'href="https://fonts.googleapis.com/css2?family={font_families}&display=swap">'
                    )
            # Extract Fontshare URL from comment
            fs_match = re.search(r'/\* Fontshare: (.+?) \*/', skin_content)
            if fs_match:
                skin_font_link = f'    <link rel="stylesheet" href="{fs_match.group(1).strip()}">'
            skin_css = skin_content

    if skin_css:
        html = html.replace('</style>', f'\n        /* === SKIN: {args.skin} === */\n{skin_css}\n    </style>')
    if skin_font_link:
        html = html.replace('</head>', f'{skin_font_link}\n</head>')

    # 3. Title highlight: wrap keywords in <span class="highlight-accent">
    highlighted_title = args.title
    for kw in args.highlight:
        highlighted_title = re.sub(
            re.escape(kw),
            f'<span class="highlight-accent">{kw}</span>',
            highlighted_title,
            flags=re.IGNORECASE
        )

    # 4. Replace placeholders (footer also uses highlighted title)
    html = html.replace("{{TITLE_PLACEHOLDER}}", highlighted_title)
    html = html.replace("{{AUTHOR_PLACEHOLDER}}", args.speaker)
    html = html.replace("{{EVENT_PLACEHOLDER}}", args.event)

    # 5. Generate slide injection content
    injections = []
    slide_idx = 1

    # --- Title Slide ---
    subtitle_html = ""
    if args.subtitle:
        subtitle_html = f'\n            <h2>{args.subtitle}</h2>'

    # Speaker underline + affiliation superscript processing
    authors = [a.strip() for a in args.author.split(",")]
    author_parts = []
    for a in authors:
        # Parse Name:N format
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
                f'<u style="text-decoration: underline; text-underline-offset: 0.25em; '
                f'text-decoration-skip-ink: none;">{name}</u>{sup}'
            )
        else:
            author_parts.append(f'{name}{sup}')
    author_line = ", ".join(author_parts)

    # Affiliation list auto-numbering + line breaks
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
            ref_html = f'\n            <p style="font-size: 0.8em;">Reference: <a href="{url.strip()}" target="_blank" style="color: #0000EE; text-decoration: underline; text-underline-offset: 0.25em; text-decoration-skip-ink: none;">{nickname.strip()}</a></p>'
        else:
            ref_html = f'\n            <p style="font-size: 0.8em;">Reference: <a href="{args.reference}" target="_blank" style="color: #0000EE; text-decoration: underline; text-underline-offset: 0.25em; text-decoration-skip-ink: none;">{args.reference}</a></p>'

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

        # --- Generate per Section: transition + content placeholder pages ---
        for sec in args.outline:
            parts = sec.rsplit(":", 1)
            title = parts[0].strip()
            count = 1
            if len(parts) > 1 and parts[1].isdigit():
                count = int(parts[1])

            # Transition page
            injections.append(f"""
    <!-- [Slide {slide_idx}] Transition: {title} -->
    <section class="slide transition-slide" data-header="hidden" data-title="">
        <div class="transition-text reveal d1">{title}</div>
    </section>""")
            slide_idx += 1

            # Content placeholder page
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

    # 6. Inject into template
    injection_html = "\n".join(injections) + "\n    <!-- END slides-scroller -->"
    html = html.replace("<!-- END slides-scroller -->", injection_html)

    # 7. Write output
    out_path = os.path.abspath(args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    total = slide_idx - 1
    print(f"✅ Slide harness created successfully at {out_path}")
    print(f"   Total slides: {total}")
    print(f"   Skin: {args.skin}")
    print(f"   Logos: {', '.join(args.logos)}")
    if args.outline:
        print(f"   Outline sections: {len(args.outline)}")
        for i, sec in enumerate(args.outline, 1):
            parts = sec.rsplit(":", 1)
            title = parts[0].strip()
            count = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1
            print(f"     {i}. {title} (Allocated {count} pages)")


if __name__ == "__main__":
    main()
