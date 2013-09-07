import argparse
import colorsys
from PIL import Image

import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("file_in", type=str, help="NumPy array file", default="pointmap.npy")
parser.add_argument("file_out", type=str, help="Output file name", default="fractal.png")
parser.add_argument("size", type=int, help="Image size")
args = parser.parse_args()

size = args.size
roots = np.load(args.file_in)
hits = np.zeros((size, size), dtype=np.int)
image = Image.new("RGB", (size, size))

x_max = 1.5
x_min = -1.5
y_max = 1.5
y_min = -1.5

# Generate Hit map
for root in roots:
    point_x = (size - 1) * (root[0] - x_min) / (x_max - x_min)
    point_y = (size - 1) * (root[1] - y_min) / (y_max - y_min)
    if all([point_x >= 0,
            point_x <= size - 1,
            point_y >= 0,
            point_y <= size - 1]):
                hits[int(point_x)][int(point_y)] += 1

# Plot hits on image
max_hits = np.log(np.amax(hits))
for xi, xd in enumerate(hits):
    for yi, yd in enumerate(xd):
        if yd > 0:
            c_val = np.log(yd) / max_hits
            r, g, b = colorsys.hsv_to_rgb(c_val / 2, 1 - c_val, 0.5 + c_val / 2)[:]
            image.putpixel((xi, yi), (int(255 * r), int(255 * g), int(255 * b)))

image.save(args.file_out, "PNG")
