import os
import sys
sys.path.append(os.path.abspath(os.path.relpath("../python")))
import euler

def pandigital(n):
    digits = list(str(n))
    digits = sorted(digits)
    for i in range(1, len(digits) + 1):
        if digits[i - 1] != str(i):
            return False
    return True

for p in euler.rwh_primes(7654321):
    if pandigital(p):
        print p
