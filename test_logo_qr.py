#!/usr/bin/env python3
"""
Test script for logo QR code functionality
"""

import os
from PIL import Image, ImageDraw
from src.qr_code_maker import create_qr_code, create_full_page_image

def create_test_logo():
    """Create a simple test logo"""
    # Create a simple circular logo
    logo_size = 200
    logo = Image.new('RGBA', (logo_size, logo_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(logo)
    
    # Draw a circle
    margin = 20
    draw.ellipse([margin, margin, logo_size-margin, logo_size-margin], 
                 fill=(255, 0, 0, 255), outline=(0, 0, 0, 255), width=3)
    
    # Add some text
    try:
        from PIL import ImageFont
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    text = "LOGO"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (logo_size - text_width) // 2
    text_y = (logo_size - text_height) // 2
    draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
    
    return logo

def test_logo_qr():
    """Test QR code generation with logo"""
    print("Creating test logo...")
    logo = create_test_logo()
    logo_path = "test_logo.png"
    logo.save(logo_path)
    print(f"Test logo saved as: {logo_path}")
    
    print("Testing QR code with logo...")
    test_url = "https://example.com"
    
    # Test basic QR code with logo
    qr_with_logo = create_qr_code(test_url, qr_size=1000, logo_path=logo_path, logo_size_ratio=0.2)
    qr_with_logo.save("test_qr_with_logo.png")
    print("QR code with logo saved as: test_qr_with_logo.png")
    
    # Test full page image with logo
    print("Testing full page image with logo...")
    full_page = create_full_page_image(
        title="Test QR Code with Logo",
        url=test_url,
        font_path="",
        save_to_dir=".",
        logo_path=logo_path,
        logo_size_ratio=0.15
    )
    full_page.save("test_full_page_with_logo.png")
    print("Full page image with logo saved as: test_full_page_with_logo.png")
    
    # Test QR code without logo for comparison
    print("Testing QR code without logo...")
    qr_without_logo = create_qr_code(test_url, qr_size=1000)
    qr_without_logo.save("test_qr_without_logo.png")
    print("QR code without logo saved as: test_qr_without_logo.png")
    
    print("\nTest completed! Check the generated PNG files.")
    print("Files created:")
    print("- test_logo.png (test logo)")
    print("- test_qr_with_logo.png (QR code with logo)")
    print("- test_qr_without_logo.png (QR code without logo)")
    print("- test_full_page_with_logo.png (full page with logo)")

if __name__ == "__main__":
    test_logo_qr()
