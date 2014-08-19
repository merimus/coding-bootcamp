import os
import sys
sys.path.append(os.path.abspath(os.path.relpath("../python")))
import euler

primes = euler.rwh_primes(10000)
double_squares = set(map(lambda x: 2 * x * x, range(1, 100)))

nums = set()
for p in primes:
    for ds in double_squares:
        nums.add(p + ds)
for n in range(2, 10000):
    if n % 2 == 0:
        continue
    if n in primes:
        continue
    if n not in nums:
        print n
        break

