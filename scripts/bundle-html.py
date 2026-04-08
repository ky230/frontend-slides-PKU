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

    # 正则表达式寻找 <img ... src="路径">
    pattern = r'<img\s+[^>]*src=["\']([^"\']+)["\']'
    matches = re.finditer(pattern, html_content)
    
    bundled_count = 0
    for match in matches:
        img_src = match.group(1)
        # 跳过已经是 base64 或外部网络链接的图片
        if img_src.startswith("data:") or img_src.startswith("http"):
            continue 
            
        if os.path.isabs(img_src):
            full_img_path = img_src
        else:
            full_img_path = os.path.join(base_dir, img_src)
            
        if os.path.exists(full_img_path):
            try:
                b64_data = get_base64_encoded_image(full_img_path)
                # 字符串精准替换 src
                html_content = html_content.replace(f'src="{img_src}"', f'src="{b64_data}"')
                html_content = html_content.replace(f"src='{img_src}'", f"src='{b64_data}'")
                print(f"🖼️ 成功嵌入图片: {img_src}")
                bundled_count += 1
            except Exception as e:
                print(f"❌ 嵌入失败 {img_src}: {e}")
        else:
            print(f"⚠️ 找不到图片文件，已跳过: {full_img_path}")
            
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("\n" + "="*50)
    print(f"✨ 单文件打包完成！")
    print(f"总计嵌入图片: {bundled_count} 张")
    print(f"生成路径: {output_html_path}")
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
