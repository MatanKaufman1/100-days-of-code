import colorgram

IMAGE = "image.jpeg"
NUM_OF_COLORS = 100
rgb_colors = []

def color_extract():
    colors = colorgram.extract(IMAGE, NUM_OF_COLORS)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    return rgb_colors