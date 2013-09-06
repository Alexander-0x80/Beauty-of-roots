import argparse
import colorsys
from PIL import Image

import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("file_in", type=str, help="NumPy array file", default="pointmap.npy")
parser.add_argument("file_out", type=str, help="Output file name", default="fractal.png")
args = parser.parse_args()

points = np.load(args.file_in)
size = len(points)
image = Image.new("RGB", (size, size))

max_hits = np.log(np.amax(points))
for xi, xd in enumerate(points):
    for yi, yd in enumerate(xd):
        if yd > 0:
            c_val = np.log(yd) / max_hits
            r, g, b = colorsys.hsv_to_rgb(c_val / 2, 1 - c_val, 0.5 + c_val / 2)[:]
            image.putpixel((xi, yi), (int(255 * r), int(255 * g), int(255 * b)))

image.save(args.file_out, "PNG")
