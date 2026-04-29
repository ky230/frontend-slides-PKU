#!/usr/bin/env python3
"""
renumber-slides.py — Renumber slide markers & figure directories.

After inserting or deleting slides, this script:
  1. Renumbers all <!-- [Slide N] ... --> comments sequentially (1, 2, 3, ...)
  2. Updates all src="Figures/SN/..." image paths to match new numbering
  3. Renames Figures/SN/ directories on disk to match

Usage:
    python3 renumber-slides.py <input.html> [--dry-run]

Options:
    --dry-run    Show what would change without modifying anything.

Example:
    # After inserting a new slide between Slide 5 and Slide 6:
    python3 renumber-slides.py ./my_talk.html
    # Result: old Slide 6→7, Slide 7→8, ..., Figures/S6/→S7/, etc.
"""

import re
import os
import sys
import shutil
from pathlib import Path


def find_figures_dir(html_path: Path) -> Path | None:
    """Find the Figures/ directory relative to the HTML file.
    
    Convention: for {path}/{name}.html, look for:
      1. {path}/attachment_{name}_html/Figures/
      2. {path}/attachment/slides/   (legacy format)
    """
    parent = html_path.parent
    stem = html_path.stem
    
    # Convention 1: attachment_{name}_html/Figures/
    new_style = parent / f"attachment_{stem}_html" / "Figures"
    if new_style.is_dir():
        return new_style
    
    # Convention 2: attachment/slides/ (legacy, e.g. Pre-slides project)
    legacy_style = parent / "attachment" / "slides"
    if legacy_style.is_dir():
        return legacy_style
    
    return None


def detect_img_prefix(html_content: str) -> str | None:
    """Auto-detect the image path prefix from existing src attributes.
    
    Returns the prefix string like 'attachment/slides/' or 
    'attachment_xxx_html/Figures/' so we know what to renumber.
    """
    # Match src="<prefix>S<number>/..."
    match = re.search(r'src="([^"]*?/S)\d+/', html_content)
    if match:
        # Return everything up to and excluding the 'S'
        full = match.group(1)
        return full[:-1] + "/"  # e.g. "attachment/slides/"
    return None


def renumber(html_path: str, dry_run: bool = False):
    html_path = Path(html_path).resolve()
    
    if not html_path.is_file():
        print(f"❌ File not found: {html_path}")
        sys.exit(1)
    
    content = html_path.read_text(encoding="utf-8")
    
    # --- Step 1: Collect current slide markers ---
    # Pattern: <!-- [Slide N] ... -->
    marker_pattern = re.compile(r'(<!--\s*\[Slide\s+)(\d+)(\].*?-->)')
    markers = list(marker_pattern.finditer(content))
    
    if not markers:
        print("❌ No <!-- [Slide N] --> markers found.")
        sys.exit(1)
    
    print(f"📋 Found {len(markers)} slide markers")
    
    # Build old→new mapping
    old_numbers = [int(m.group(2)) for m in markers]
    renumber_map = {}  # old_number → new_number
    changes = []
    
    for new_num, (marker, old_num) in enumerate(zip(markers, old_numbers), start=1):
        renumber_map[old_num] = new_num
        if old_num != new_num:
            # Extract title for display
            title = marker.group(3).strip().rstrip("-->").strip("] ").strip()
            changes.append(f"  Slide {old_num} → {new_num}  ({title})")
    
    if not changes:
        print("✅ All slide numbers are already sequential. Nothing to do.")
        return
    
    print(f"\n🔄 Renumbering {len(changes)} slides:")
    for c in changes:
        print(c)
    
    # --- Step 2: Renumber markers in HTML ---
    new_content = content
    # Process in reverse order to preserve positions
    for marker in reversed(markers):
        old_num = int(marker.group(2))
        new_num = renumber_map[old_num]
        if old_num != new_num:
            old_text = marker.group(0)
            new_text = f"{marker.group(1)}{new_num}{marker.group(3)}"
            # Replace at exact position
            start, end = marker.span()
            new_content = new_content[:start] + new_text + new_content[end:]
    
    # --- Step 3: Renumber image src paths ---
    img_prefix = detect_img_prefix(content)
    fig_dir = find_figures_dir(html_path)
    
    src_changes = []
    if img_prefix:
        print(f"\n🖼️  Image prefix detected: {img_prefix}")
        
        # Replace src="prefix/SN/..." with new numbers
        # Process highest numbers first to avoid S1→S2 then S2→S3 chains
        for old_num in sorted(renumber_map.keys(), reverse=True):
            new_num = renumber_map[old_num]
            if old_num != new_num:
                old_src = f'{img_prefix}S{old_num}/'
                new_src = f'{img_prefix}S{new_num}/'
                count = new_content.count(old_src)
                if count > 0:
                    # Use temporary placeholder to avoid collision
                    placeholder = f'{img_prefix}__TEMP_S{new_num}__/'
                    new_content = new_content.replace(old_src, placeholder)
                    src_changes.append((old_src, new_src, count))
        
        # Resolve placeholders
        for old_src, new_src, count in src_changes:
            placeholder = f'{img_prefix}__TEMP_S{renumber_map[int(re.search(r"S(\d+)", old_src).group(1))]}__/'
            new_content = new_content.replace(placeholder, new_src)
            print(f"  {old_src} → {new_src}  ({count} refs)")
    
    # --- Step 4: Rename figure directories ---
    dir_renames = []
    if fig_dir and fig_dir.is_dir():
        print(f"\n📁 Figures directory: {fig_dir}")
        
        # Collect existing S* directories
        existing_dirs = {}
        for d in fig_dir.iterdir():
            if d.is_dir() and re.match(r'^S(\d+)$', d.name):
                num = int(d.name[1:])
                existing_dirs[num] = d
        
        # Plan renames (use temp names to avoid collision)
        for old_num in sorted(renumber_map.keys()):
            new_num = renumber_map[old_num]
            if old_num != new_num and old_num in existing_dirs:
                old_dir = existing_dirs[old_num]
                tmp_dir = fig_dir / f"__tmp_S{new_num}"
                new_dir = fig_dir / f"S{new_num}"
                dir_renames.append((old_dir, tmp_dir, new_dir))
                print(f"  S{old_num}/ → S{new_num}/")
        
        if not dir_renames:
            print("  (no directories need renaming)")
    
    # --- Execute or dry-run ---
    if dry_run:
        print(f"\n🏁 DRY RUN complete. No files modified.")
        print(f"   {len(changes)} markers + {len(src_changes)} src paths + {len(dir_renames)} directories would change.")
        return
    
    # Write HTML
    html_path.write_text(new_content, encoding="utf-8")
    print(f"\n✏️  Updated {html_path.name}")
    
    # Rename directories (two-phase: all→tmp, then tmp→final)
    if dir_renames:
        for old_dir, tmp_dir, _ in dir_renames:
            shutil.move(str(old_dir), str(tmp_dir))
        for _, tmp_dir, new_dir in dir_renames:
            shutil.move(str(tmp_dir), str(new_dir))
        print(f"📁 Renamed {len(dir_renames)} figure directories")
    
    print(f"\n✅ Done! {len(changes)} slides renumbered.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    html_file = sys.argv[1]
    dry = "--dry-run" in sys.argv
    renumber(html_file, dry_run=dry)
