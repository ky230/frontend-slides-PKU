#!/usr/bin/env python3
import base64
import os
import re
import sys
import mimetypes

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode('utf-8')
    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type:
        mime_type = "image/png"
    return f"data:{mime_type};base64,{b64_string}"

def bundle_html(input_html_path, output_html_path):
    base_dir = os.path.dirname(os.path.abspath(input_html_path))
    
    with open(input_html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Regex to find <img ... src="path">
    pattern = r'<img\s+[^>]*src=["\']([^"\']+)["\']'
    matches = re.finditer(pattern, html_content)
    
    bundled_count = 0
    for match in matches:
        img_src = match.group(1)
        # Skip images already base64-encoded or external URLs
        if img_src.startswith("data:") or img_src.startswith("http"):
            continue 
            
        if os.path.isabs(img_src):
            full_img_path = img_src
        else:
            full_img_path = os.path.join(base_dir, img_src)
            
        if os.path.exists(full_img_path):
            try:
                b64_data = get_base64_encoded_image(full_img_path)
                # Exact string replacement of src
                html_content = html_content.replace(f'src="{img_src}"', f'src="{b64_data}"')
                html_content = html_content.replace(f"src='{img_src}'", f"src='{b64_data}'")
                print(f"🖼️ Embedded image: {img_src}")
                bundled_count += 1
            except Exception as e:
                print(f"❌ Failed to embed {img_src}: {e}")
        else:
            print(f"⚠️ Image not found, skipped: {full_img_path}")
            
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("\n" + "="*50)
    print(f"✨ Bundle complete!")
    print(f"Total images embedded: {bundled_count}")
    print(f"Output: {output_html_path}")
    print("="*50)

if __name__ == "__main__":
    if len(sys.argv) not in [2, 3]:
        print("Usage: python bundle-html.py <input.html> [output.html]")
        sys.exit(1)
        
    input_file = sys.argv[1]
    if len(sys.argv) == 3:
        output_file = sys.argv[2]
    else:
        # Automatically generate _bundle suffixed output file if none provided
        base, ext = os.path.splitext(input_file)
        if ext.lower() == "":
            ext = ".html"
        output_file = f"{base}_bundle{ext}"
        
    bundle_html(input_file, output_file)
