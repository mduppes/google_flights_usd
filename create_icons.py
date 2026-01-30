from PIL import Image, ImageDraw

def create_plane_icon(size, filename):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    s = size / 128.0
    plane_color = (26, 115, 232, 255)  # Google blue
    
    # Clean airplane pointing to top-right (like taking off)
    points = [
        (95*s, 15*s),    # Nose
        (100*s, 25*s),   # Right of nose
        (75*s, 50*s),    # Right wing junction
        (110*s, 75*s),   # Right wing tip
        (95*s, 85*s),    # Right wing back
        (60*s, 60*s),    # Body center right
        (45*s, 75*s),    # Tail right
        (20*s, 105*s),   # Tail tip
        (25*s, 95*s),    # Tail left
        (15*s, 85*s),    # Tail fin tip
        (30*s, 80*s),    # Tail fin back
        (50*s, 55*s),    # Body center left
        (35*s, 25*s),    # Left wing back
        (55*s, 5*s),     # Left wing tip
        (65*s, 30*s),    # Left wing junction
        (85*s, 10*s),    # Left of nose
    ]
    
    draw.polygon(points, fill=plane_color)
    img.save(filename, 'PNG')
    print(f"Created {filename}")

create_plane_icon(16, 'icons/icon16.png')
create_plane_icon(48, 'icons/icon48.png')
create_plane_icon(128, 'icons/icon128.png')
print("All icons created!")
