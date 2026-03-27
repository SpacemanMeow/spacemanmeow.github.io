#!/usr/bin/env python3
"""
Markdown to HTML Converter - Universal Tool with Incremental Build
Converts Markdown files in _posts to rich text HTML files in assets/html
Only processes files that have been modified since last conversion

Usage:
    python3 tools/md_to_html.py              # Convert updated files only
    python3 tools/md_to_html.py --all        # Convert all files
    python3 tools/md_to_html.py --verbose    # Verbose output
    python3 tools/md_to_html.py --file post.md  # Convert specific file
"""

import os
import re
import sys
import glob
import argparse
import hashlib
from pathlib import Path
from datetime import datetime

# Configuration
POSTS_DIR = '/Users/gaolitao/Documents/code/spacemanmeow.github.io/_posts'
OUTPUT_DIR = '/Users/gaolitao/Documents/code/spacemanmeow.github.io/assets/html'
CACHE_FILE = '/Users/gaolitao/Documents/code/spacemanmeow.github.io/tools/.md_to_html_cache'

# HTML Template with rich styling
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.8;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
            background-color: #fafafa;
        }}
        article {{
            background-color: #fff;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        }}
        h1 {{
            font-size: 28px;
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 16px;
            line-height: 1.4;
        }}
        h2 {{
            font-size: 22px;
            font-weight: 600;
            color: #2c3e50;
            margin: 32px 0 16px 0;
            padding-bottom: 8px;
            border-bottom: 2px solid #eee;
        }}
        h3 {{
            font-size: 18px;
            font-weight: 600;
            color: #34495e;
            margin: 24px 0 12px 0;
        }}
        p {{
            margin-bottom: 16px;
            text-align: justify;
        }}
        ol {{
            margin: 20px 0;
            padding-left: 24px;
        }}
        ol li {{
            margin-bottom: 16px;
            padding-left: 8px;
        }}
        ol li strong {{
            color: #2c3e50;
        }}
        ul {{
            margin: 16px 0;
            padding-left: 24px;
        }}
        ul li {{
            margin-bottom: 12px;
            padding-left: 8px;
        }}
        ul li strong {{
            color: #e74c3c;
        }}
        .image-gallery {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin: 24px 0;
            justify-content: center;
        }}
        .gallery-img {{
            width: 160px;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }}
        .gallery-img:hover {{
            transform: scale(1.05);
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .highlight-box {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 24px;
            border-radius: 12px;
            margin: 24px 0;
        }}
        .highlight-box a {{
            color: #ffd700;
            font-weight: 600;
        }}
        .tag {{
            display: inline-block;
            background-color: #f0f0f0;
            color: #666;
            padding: 4px 12px;
            border-radius: 16px;
            font-size: 12px;
            margin-right: 8px;
            margin-bottom: 8px;
        }}
        .tags-container {{
            margin-bottom: 24px;
        }}
    </style>
</head>
<body>
    <article>
        <h1>{title}</h1>

        <div class="tags-container">
            {tags_html}
        </div>

        {body_html}
    </article>
</body>
</html>'''


def load_cache():
    """Load conversion cache from file"""
    cache = {}
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and '|' in line:
                        parts = line.split('|')
                        if len(parts) >= 2:
                            filepath = parts[0]
                            mtime = parts[1]
                            cache[filepath] = float(mtime)
        except Exception as e:
            print(f"Warning: Could not load cache: {e}")
    return cache


def save_cache(cache):
    """Save conversion cache to file"""
    try:
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            for filepath, mtime in cache.items():
                f.write(f"{filepath}|{mtime}\n")
    except Exception as e:
        print(f"Warning: Could not save cache: {e}")


def get_file_mtime(filepath):
    """Get file modification time"""
    try:
        return os.path.getmtime(filepath)
    except Exception:
        return 0


def needs_conversion(md_path, cache, output_dir):
    """Check if file needs conversion based on modification time"""
    # Always convert if not in cache
    if md_path not in cache:
        return True
    
    # Check if markdown file has been modified
    current_mtime = get_file_mtime(md_path)
    cached_mtime = cache.get(md_path, 0)
    
    if current_mtime > cached_mtime:
        return True
    
    # Check if output file exists
    filename = os.path.basename(md_path)
    output_filename = filename.replace('.md', '.html')
    output_path = os.path.join(output_dir, output_filename)
    
    if not os.path.exists(output_path):
        return True
    
    return False


def parse_front_matter(content):
    """Parse YAML front matter from markdown content"""
    if not content.startswith('---'):
        return {}, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    
    front_matter = parts[1].strip()
    body = parts[2].strip()
    
    metadata = {}
    for line in front_matter.split('\n'):
        line = line.strip()
        if not line or ':' not in line:
            continue
        
        # Handle array syntax carefully
        if line.startswith('tags:') or line.startswith('categories:'):
            key = line.split(':')[0].strip()
            value_str = line[len(key)+1:].strip()
            # Parse array [item1, item2, ...]
            if value_str.startswith('[') and value_str.endswith(']'):
                items = []
                for item in value_str[1:-1].split(','):
                    item = item.strip().strip('"\'')
                    if item:
                        items.append(item)
                metadata[key] = items
            else:
                metadata[key] = value_str.strip('"\'')
        else:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            # Remove quotes if present
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            metadata[key] = value
    
    return metadata, body


def convert_images_to_gallery(html_content):
    """Convert consecutive images to gallery format"""
    lines = html_content.split('\n')
    new_lines = []
    gallery_imgs = []
    
    for line in lines:
        if '<img' in line and 'class="gallery-img"' in line:
            gallery_imgs.append(line.strip())
        else:
            if gallery_imgs:
                # Close gallery
                new_lines.append('<div class="image-gallery">')
                new_lines.extend(gallery_imgs)
                new_lines.append('</div>')
                gallery_imgs = []
            new_lines.append(line)
    
    # Handle remaining images
    if gallery_imgs:
        new_lines.append('<div class="image-gallery">')
        new_lines.extend(gallery_imgs)
        new_lines.append('</div>')
    
    return '\n'.join(new_lines)


def markdown_to_html(body, metadata):
    """Convert markdown body to HTML"""
    html = body
    
    # Store original lines for list type detection
    original_lines = body.split('\n')
    
    # Convert headers (h3, h2, h1 order matters)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # Convert images - handle Jekyll image syntax
    def replace_image(match):
        alt = match.group(1) or 'image'
        src = match.group(2)
        return f'<img src="{src}" alt="{alt}" class="gallery-img">'
    
    html = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)(?:\{[^}]*\})?', replace_image, html)
    
    # Convert links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', html)
    
    # Convert bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    
    # Convert unordered lists (must be before ordered lists)
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    
    # Convert ordered lists
    html = re.sub(r'^\d+\. (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    
    # Wrap lists
    lines = html.split('\n')
    result = []
    in_ul = False
    in_ol = False
    
    for i, line in enumerate(lines):
        if line.startswith('<li>'):
            # Determine list type from original content
            orig_line = original_lines[i] if i < len(original_lines) else ''
            is_ordered = re.match(r'^\d+\. ', orig_line)
            
            if not in_ul and not in_ol:
                if is_ordered:
                    result.append('<ol>')
                    in_ol = True
                else:
                    result.append('<ul>')
                    in_ul = True
            elif in_ul and is_ordered:
                # Switch from ul to ol
                result.append('</ul>')
                result.append('<ol>')
                in_ul = False
                in_ol = True
            elif in_ol and not is_ordered:
                # Switch from ol to ul
                result.append('</ol>')
                result.append('<ul>')
                in_ol = False
                in_ul = True
            result.append(line)
        else:
            if in_ul:
                result.append('</ul>')
                in_ul = False
            if in_ol:
                result.append('</ol>')
                in_ol = False
            result.append(line)
    
    if in_ul:
        result.append('</ul>')
    if in_ol:
        result.append('</ol>')
    
    html = '\n'.join(result)
    
    # Convert paragraphs (simple approach)
    paragraphs = html.split('\n\n')
    new_paragraphs = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<') and not p.startswith('!['):
            p = f'<p>{p}</p>'
        new_paragraphs.append(p)
    html = '\n\n'.join(new_paragraphs)
    
    # Wrap image groups in galleries
    html = convert_images_to_gallery(html)
    
    return html


def generate_html(metadata, body_html, lang):
    """Generate complete HTML document"""
    
    title = metadata.get('title', 'Untitled')
    tags = metadata.get('tags', [])
    
    # Ensure list
    if isinstance(tags, str):
        tags = [tags]
    
    # Format tags
    tags_html = ''.join([f'<span class="tag">{tag}</span>' for tag in tags])
    
    # Determine language
    lang_code = metadata.get('lang', lang)
    
    return HTML_TEMPLATE.format(
        title=title,
        tags_html=tags_html,
        body_html=body_html,
        lang=lang_code
    )


def get_language_from_filename(filename):
    """Extract language code from filename (e.g., file.zh-CN.md -> zh-CN)"""
    parts = filename.split('.')
    if len(parts) >= 3:
        return parts[-2]
    return 'en'


def process_markdown_file(md_path, output_dir, cache, verbose=True):
    """Process a single markdown file"""
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        metadata, body = parse_front_matter(content)
        
        # Get language from filename
        filename = os.path.basename(md_path)
        lang = get_language_from_filename(filename)
        
        # Convert to HTML
        body_html = markdown_to_html(body, metadata)
        html = generate_html(metadata, body_html, lang)
        
        # Write output
        output_filename = filename.replace('.md', '.html')
        output_path = os.path.join(output_dir, output_filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        # Update cache with current modification time
        cache[md_path] = get_file_mtime(md_path)
        
        if verbose:
            print(f"✓ {filename} -> {output_filename}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error processing {md_path}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Convert Markdown files to rich HTML (Incremental Build)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
    python3 tools/md_to_html.py              # Convert updated files only
    python3 tools/md_to_html.py --all        # Convert all files
    python3 tools/md_to_html.py --verbose    # Verbose output
    python3 tools/md_to_html.py --file post.md  # Convert specific file
    python3 tools/md_to_html.py --clean      # Clear cache and convert all
        '''
    )
    parser.add_argument('--all', '-a', action='store_true', help='Convert all files (ignore cache)')
    parser.add_argument('--clean', '-c', action='store_true', help='Clear cache and convert all')
    parser.add_argument('--file', '-f', help='Convert specific file only')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--posts-dir', default=POSTS_DIR, help='Posts directory')
    parser.add_argument('--output-dir', default=OUTPUT_DIR, help='Output directory')
    
    args = parser.parse_args()
    
    # Handle clean option
    if args.clean:
        if os.path.exists(CACHE_FILE):
            os.remove(CACHE_FILE)
            print("Cache cleared.")
        args.all = True
    
    # Load cache
    cache = {} if args.all else load_cache()
    
    # Ensure output directory exists
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Get files to process
    if args.file:
        md_files = [os.path.join(args.posts_dir, args.file)]
        # Force conversion for specific file
        args.all = True
    else:
        md_files = glob.glob(os.path.join(args.posts_dir, '*.md'))
        # Exclude placeholder
        md_files = [f for f in md_files if '.placeholder' not in f]
    
    if not md_files:
        print("No markdown files found.")
        return
    
    # Filter files that need conversion
    if args.all:
        files_to_process = md_files
    else:
        files_to_process = [f for f in md_files if needs_conversion(f, cache, args.output_dir)]
    
    print(f"Found {len(md_files)} markdown file(s)")
    if not args.all:
        print(f"Files needing conversion: {len(files_to_process)}")
    print(f"Output directory: {args.output_dir}")
    print("Converting...\n")
    
    if not files_to_process:
        print("✅ All files are up to date!")
        return
    
    success_count = 0
    fail_count = 0
    
    for md_file in sorted(files_to_process):
        if process_markdown_file(md_file, args.output_dir, cache, verbose=args.verbose):
            success_count += 1
        else:
            fail_count += 1
    
    # Save updated cache
    save_cache(cache)
    
    print(f"\n{'='*50}")
    print(f"✅ Success: {success_count}")
    if fail_count > 0:
        print(f"❌ Failed: {fail_count}")
    print(f"{'='*50}")


if __name__ == '__main__':
    main()
