#!/usr/bin/env python3
"""
Image Compressor Tool using macOS sips
Compresses images in assets directory while maintaining quality
Uses built-in sips command for better compatibility
Supports incremental compression - only compresses new or updated images
"""

import os
import subprocess
from pathlib import Path

# Configuration
ASSETS_DIR = '/Users/gaolitao/Documents/code/spacemanmeow.github.io/assets'
JPEG_QUALITY = 85  # Quality level (0-100, higher = better quality but larger file)
CACHE_FILE = '/Users/gaolitao/Documents/code/spacemanmeow.github.io/tools/.compress_cache'

def get_file_size(filepath):
    """Get file size in KB"""
    return os.path.getsize(filepath) / 1024

def get_file_mtime(filepath):
    """Get file modification time"""
    return os.path.getmtime(filepath)

def load_cache():
    """Load compression cache from file"""
    cache = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if line and '|' in line:
                    parts = line.split('|')
                    cache[parts[0]] = float(parts[1])
    return cache

def save_cache(cache):
    """Save compression cache to file"""
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        for filepath, mtime in cache.items():
            f.write(f"{filepath}|{mtime}\n")

def needs_compression(img_path, cache):
    """Check if an image needs compression"""
    img_path_str = str(img_path)
    
    # Not in cache - needs compression
    if img_path_str not in cache:
        return True
    
    # File has been modified since last compression
    current_mtime = get_file_mtime(img_path)
    cached_mtime = cache.get(img_path_str, 0)
    
    if current_mtime > cached_mtime:
        return True
    
    return False

def get_file_size(filepath):
    """Get file size in KB"""
    return os.path.getsize(filepath) / 1024

def compress_image_sips(image_path, quality=85):
    """
    Compress a single image using macOS sips
    
    Args:
        image_path: Path to the image file
        quality: JPEG quality (0-100), recommended 75-90 for good balance
    
    Returns:
        tuple: (original_size_kb, compressed_size_kb, success)
    """
    try:
        original_size = get_file_size(image_path)
        img_path_str = str(image_path)
        
        # Skip PNG files - they don't benefit from JPEG compression
        if image_path.suffix.lower() == '.png':
            # Just update cache for PNG files
            return original_size, original_size, True
        
        # Use sips to compress JPEG
        cmd = [
            'sips',
            '-s', 'formatOptions', str(quality),
            img_path_str,
            '--out', img_path_str  # Overwrite original
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            compressed_size = get_file_size(image_path)
            return original_size, compressed_size, True
        else:
            print(f"  Error: {result.stderr}")
            return original_size, original_size, False
        
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return 0, 0, False

def find_all_images(assets_dir):
    """Find all images in assets directory recursively"""
    supported_formats = {'.jpg', '.jpeg', '.png'}
    image_files = []
    
    assets_path = Path(assets_dir)
    for ext in supported_formats:
        # Search recursively in all subdirectories
        image_files.extend(assets_path.rglob(f'*{ext}'))
        image_files.extend(assets_path.rglob(f'*{ext.upper()}'))
    
    return sorted(image_files)

def main():
    """Main function to compress all images in assets directory"""
    print("="*60)
    print("Image Compression Tool (using macOS sips)")
    print("Incremental Mode - Only new/updated images")
    print("="*60)
    print(f"Directory: {ASSETS_DIR}")
    print(f"Quality: {JPEG_QUALITY}/100")
    print("="*60)
    
    # Load cache
    cache = load_cache()
    print(f"Cache loaded: {len(cache)} images\n")
    
    # Find all images
    image_files = find_all_images(ASSETS_DIR)
    
    if not image_files:
        print("No images found!")
        return
    
    print(f"Found {len(image_files)} total images")
    
    # Filter images that need compression
    images_to_compress = [img for img in image_files if needs_compression(img, cache)]
    
    print(f"Images needing compression: {len(images_to_compress)}")
    print(f"Output directory: {ASSETS_DIR}")
    print("\nConverting...\n")
    
    if not images_to_compress:
        print("✓ All images are up to date, no compression needed.")
        print("\n" + "="*60)
        print("Summary")
        print("="*60)
        print(f"Total Images: {len(image_files)}")
        print(f"Skipped: {len(image_files)}")
        print("="*60)
        return
    
    total_original = 0
    total_compressed = 0
    success_count = 0
    fail_count = 0
    
    for i, img_path in enumerate(images_to_compress, 1):
        print(f"[{i}/{len(images_to_compress)}] Processing: {img_path.relative_to(ASSETS_DIR)}")
        
        original_size, compressed_size, success = compress_image_sips(
            img_path, 
            quality=JPEG_QUALITY
        )
        
        if success:
            success_count += 1
            total_original += original_size
            total_compressed += compressed_size
            
            # Update cache with current modification time
            cache[str(img_path)] = get_file_mtime(img_path)
            
            reduction = ((original_size - compressed_size) / original_size * 100) if original_size > 0 else 0
            
            status = "✓" if compressed_size < original_size else "~"
            print(f"  {status} {original_size:.1f} KB → {compressed_size:.1f} KB ({reduction:+.1f}%)")
        else:
            fail_count += 1
            print(f"  ✗ Failed")
    
    # Save cache
    save_cache(cache)
    print(f"\nCache saved: {len(cache)} images")
    
    # Summary
    print("\n" + "="*60)
    print("Compression Summary")
    print("="*60)
    print(f"Total Images: {len(image_files)}")
    print(f"Successful: {success_count}")
    if fail_count > 0:
        print(f"Failed: {fail_count}")
    print(f"Skipped: {len(image_files) - len(images_to_compress)}")
    print(f"Original Size: {total_original:.1f} KB ({total_original/1024:.2f} MB)")
    print(f"Compressed Size: {total_compressed:.1f} KB ({total_compressed/1024:.2f} MB)")
    
    if total_original > 0:
        total_reduction = (total_original - total_compressed) / total_original * 100
        print(f"Total Reduction: {total_reduction:.1f}% ({total_original - total_compressed:.1f} KB saved)")
    
    print("="*60)

if __name__ == '__main__':
    main()
