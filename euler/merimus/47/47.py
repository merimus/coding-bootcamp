import os
import sys
sys.path.append(os.path.abspath(os.path.relpath("../python")))
import euler

primes = euler.rwh_primes(1000000)

def UniqueFactors(n):
    factors = set()
    for p in primes:
        if p > n:
            break
        while n % p == 0:
            factors.add(p)
            n /= p
    return len(factors)

consecutive = 0
for i in xrange(1000000):
    if UniqueFactors(i) == 4:
        consecutive += 1
    else:
        consecutive = 0
    if consecutive == 4:
        print i - 3
        break
