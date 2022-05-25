def rgb_to_yuv(rgb):
    r, g, b = rgb
    y = (r + g + b) >> 2
    u = 128 + ((r - b) >> 2)
    v = 128 + ((-r + g * 2 - b) >> 3)
    return y, u, v


print(rgb_to_yuv((0, 0, 0)))
print(rgb_to_yuv((255, 255, 255)))