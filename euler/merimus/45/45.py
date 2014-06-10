import os
import sys
sys.path.append(os.path.abspath(os.path.relpath("../python")))
import euler

n = 286
while True:
    t = euler.nthTriangular(n)
    if euler.isPentagonal(t) and euler.isHexagonal(t):
        print n, t
        break
    n += 1
