"""
Cutest Picture Generator - Baby Red Panda Hugging a Heart
Deterministic: same seed = same output every run
"""

from PIL import Image, ImageDraw, ImageFilter
import random
import os

def create_cutest_picture():
    """Generate the cutest picture: baby red panda hugging a heart"""
    
    # Fixed seed for determinism
    random.seed(42)
    
    # Image size
    width, height = 1024, 1024
    image = Image.new('RGB', (width, height), '#FFF8F0')
    draw = ImageDraw.Draw(image)
    
    # === BACKGROUND ===
    # Soft gradient background
    for y in range(height):
        r = int(255 - (y / height) * 30)
        g = int(248 - (y / height) * 20)
        b = int(240 - (y / height) * 15)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # === FLOWER FIELD BACKGROUND ===
    # Simple flowers
    for _ in range(50):
        x = random.randint(0, width)
        y = random.randint(height - 200, height)
        size = random.randint(15, 30)
        colors = ['#FF6B9D', '#FF85A2', '#FFB3C6', '#FF4D6D']
        color = random.choice(colors)
        
        # Flower petals
        for angle in range(0, 360, 60):
            rad = (angle - 90) * 3.14159 / 180
            px = x + int(size * 0.6 * (1 if angle % 120 == 0 else 0.7) * (1 if angle == 90 else 1))
            py = y + int(size * 0.6 * (1 if angle % 120 == 0 else 0.7) * (1 if angle == 270 else 1))
            draw.ellipse([px - size//3, py - size//3, px + size//3, py + size//3], fill=color)
        
        # Center
        draw.ellipse([x - size//4, y - size//4, x + size//4, y + size//4], fill='#FFD700')
    
    # === GROUND ===
    draw.ellipse([0, height - 100, width, height + 100], fill='#E8F5E9')
    draw.ellipse([0, height - 50, width, height + 50], fill='#C8E6C9')
    
    # === HEART ===
    heart_x, heart_y = width // 2, height // 2 + 50
    heart_size = 180
    
    # Heart shape using arcs
    heart_color = '#FF6B9D'
    heart_border = '#FF4D6D'
    
    # Draw heart
    draw.ellipse([heart_x - heart_size//2, heart_y - heart_size//3, 
                  heart_x + heart_size//2, heart_y + heart_size//6], 
                 fill=heart_color, outline=heart_border, width=3)
    draw.ellipse([heart_x - heart_size//2, heart_y - heart_size//6,
                  heart_x + heart_size//2, heart_y + heart_size//2],
                 fill=heart_color, outline=heart_border, width=3)
    draw.polygon([
        (heart_x - heart_size//2, heart_y + heart_size//6),
        (heart_x, heart_y + heart_size//3),
        (heart_x + heart_size//2, heart_y + heart_size//6)
    ], fill=heart_color, outline=heart_border, width=3)
    
    # Heart shine
    draw.ellipse([heart_x - heart_size//4, heart_y - heart_size//4,
                  heart_x - heart_size//6, heart_y - heart_size//8],
                 fill='#FFB3C6', outline=None)
    
    # === RED PANDA ===
    panda_x, panda_y = heart_x, heart_y - 80
    
    # Body
    body_color = '#D4A574'
    body_dark = '#B8865A'
    belly_color = '#FFF5E6'
    ear_color = '#B8865A'
    eye_color = '#1A1A1A'
    nose_color = '#FF6B6B'
    
    # Body (oval)
    draw.ellipse([panda_x - 100, panda_y - 30, panda_x + 100, panda_y + 120],
                 fill=body_color, outline=body_dark, width=2)
    
    # Belly
    draw.ellipse([panda_x - 60, panda_y + 10, panda_x + 60, panda_y + 90],
                 fill=belly_color)
    
    # Arms hugging heart
    # Left arm
    draw.ellipse([panda_x - 130, panda_y + 20, panda_x - 50, panda_y + 80],
                 fill=body_color, outline=body_dark, width=2)
    # Right arm  
    draw.ellipse([panda_x + 50, panda_y + 20, panda_x + 130, panda_y + 80],
                 fill=body_color, outline=body_dark, width=2)
    
    # Paws
    draw.ellipse([panda_x - 120, panda_y + 70, panda_x - 80, panda_y + 100],
                 fill='#C9A06C', outline=body_dark, width=2)
    draw.ellipse([panda_x + 80, panda_y + 70, panda_x + 120, panda_y + 100],
                 fill='#C9A06C', outline=body_dark, width=2)
    
    # Head
    head_size = 90
    draw.ellipse([panda_x - head_size, panda_y - head_size, 
                  panda_x + head_size, panda_y + head_size],
                 fill=body_color, outline=body_dark, width=2)
    
    # Ears
    draw.ellipse([panda_x - head_size - 20, panda_y - head_size + 10,
                  panda_x - head_size + 10, panda_y - head_size + 50],
                 fill=ear_color, outline=body_dark, width=2)
    draw.ellipse([panda_x + head_size - 10, panda_y - head_size + 10,
                  panda_x + head_size + 20, panda_y - head_size + 50],
                 fill=ear_color, outline=body_dark, width=2)
    
    # Inner ears
    draw.ellipse([panda_x - head_size - 15, panda_y - head_size + 20,
                  panda_x - head_size + 5, panda_y - head_size + 40],
                 fill='#FFB3B3')
    draw.ellipse([panda_x + head_size - 5, panda_y - head_size + 20,
                  panda_x + head_size + 15, panda_y - head_size + 40],
                 fill='#FFB3B3')
    
    # Eyes
    eye_y = panda_y - 15
    # Left eye
    draw.ellipse([panda_x - 40, eye_y - 15, panda_x - 15, eye_y + 10],
                 fill=eye_color)
    draw.ellipse([panda_x - 35, eye_y - 10, panda_x - 20, eye_y + 5],
                 fill='#FFFFFF')
    # Right eye
    draw.ellipse([panda_x + 15, eye_y - 15, panda_x + 40, eye_y + 10],
                 fill=eye_color)
    draw.ellipse([panda_x + 20, eye_y - 10, panda_x + 35, eye_y + 5],
                 fill='#FFFFFF')
    
    # Eye shine (cute big eyes)
    draw.ellipse([panda_x - 32, eye_y - 8, panda_x - 27, eye_y - 3],
                 fill='#FFFFFF')
    draw.ellipse([panda_x + 27, eye_y - 8, panda_x + 32, eye_y - 3],
                 fill='#FFFFFF')
    
    # Blush
    draw.ellipse([panda_x - 50, panda_y + 5, panda_x - 30, panda_y + 20],
                 fill='#FFB3B3', outline=None)
    draw.ellipse([panda_x + 30, panda_y + 5, panda_x + 50, panda_y + 20],
                 fill='#FFB3B3', outline=None)
    
    # Nose
    draw.ellipse([panda_x - 8, panda_y + 5, panda_x + 8, panda_y + 18],
                 fill=nose_color)
    
    # Mouth (cute smile)
    draw.arc([panda_x - 15, panda_y + 15, panda_x + 15, panda_y + 35],
             start=0, end=180, fill=eye_color, width=2)
    
    # === SPARKLES ===
    sparkle_positions = [
        (150, 150), (850, 100), (900, 400), (200, 500),
        (700, 200), (350, 80), (100, 300), (950, 250)
    ]
    
    for sx, sy in sparkle_positions:
        # 4-point star sparkle
        size = random.randint(8, 15)
        points = [
            (sx, sy - size),
            (sx + size//3, sy - size//3),
            (sx + size, sy),
            (sx + size//3, sy + size//3),
            (sx, sy + size),
            (sx - size//3, sy + size//3),
            (sx - size, sy),
            (sx - size//3, sy - size//3)
        ]
        draw.polygon(points, fill='#FFD700', outline='#FFA500')
        
        # Glow
        draw.ellipse([sx - size, sy - size, sx + size, sy + size],
                     fill='#FFFACD', outline=None)
    
    # === TEXT ===
    # Subtle text at bottom
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    draw.text((width//2 - 100, height - 60), "So Cute! 🦊💕", 
              fill='#FF6B9D', font=font)
    
    # === SAVE ===
    output_dir = '/output'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'entry.png')
    image.save(output_path, 'PNG', optimize=True)
    
    print(f"Saved cute picture to {output_path}")
    print(f"Image size: {image.size}")
    print(f"File size: {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    create_cutest_picture()
