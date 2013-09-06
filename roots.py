import itertools
import argparse
from time import time

import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("degree", type=int, help="Polynomial degree")
parser.add_argument("size", type=int, help="Array size")
parser.add_argument("filename", type=str, default="pointmap.npy")
args = parser.parse_args()

degree = args.degree
size = args.size
points = np.zeros((size, size), dtype=np.int)

x_max = 1.5
x_min = -1.5
y_max = 1.5
y_min = -1.5

start_t = time()
for poly in itertools.product(*([[-1, 1]] * degree)):
    for root in np.roots((1,) + poly):
        point_x = (size - 1) * (root.real - x_min) / (x_max - x_min)
        point_y = (size - 1) * (root.imag - y_min) / (y_max - y_min)
        if all([point_x >= 0,
                point_x <= size - 1,
                point_y >= 0,
                point_y <= size - 1]):
                    points[int(point_x)][int(point_y)] += 1

print "Complete in {} seconds.".format(str(int(time() - start_t)))
with open(args.filename, "w") as out_file:
    np.save(out_file, points)
