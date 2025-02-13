import colorgram


IMAGE = "images.jpeg"
NUM_OF_COLORS = 50
rgb_colors = []
colors = colorgram.extract(IMAGE, NUM_OF_COLORS)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)