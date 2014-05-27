import os
import sys
sys.path.append(os.path.abspath(os.path.relpath("../python")))
import euler

sum = 0
num = 0
primes = euler.Primes()
for p in primes.Primes():
    if p < 10:
        continue
    temp = p / 10
    m = 10
    a = p % m
    truncatable = True
    while temp > 0:
        if not primes.IsPrime(temp) or not primes.IsPrime(a):
            truncatable = False
            break
        m *= 10
        a = p % m
        temp /= 10
    if truncatable:
        print p
        sum += p
        num += 1
    if num == 11:
        break
print sum
