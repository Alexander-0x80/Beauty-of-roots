import itertools
import argparse
from time import time

import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("degree", type=int, help="Polynomial degree")
parser.add_argument("filename", type=str, default="pointmap.npy")
args = parser.parse_args()

degree = args.degree
points = list()

start_t = time()
for poly in itertools.product(*([[-1, 1]] * degree)):
    for root in np.roots((1,) + poly):
        points.append((root.real, root.imag))

roots_data = np.array(points, dtype=np.float64)
print "Complete in {} seconds.".format(str(int(time() - start_t)))
with open(args.filename, "w") as out_file:
    np.save(out_file, roots_data)
