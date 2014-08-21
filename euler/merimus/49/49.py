import os
import sys
sys.path.append(os.path.abspath(os.path.relpath("../python")))
import euler

primes = euler.rwh_primes(10000)
primes = set([p for p in primes if p > 999 and p < 10000 and p >= 1487])

ordered_primes = sorted(primes)
for p in ordered_primes:
    ordered_primes.remove(p)
    for n in ordered_primes:
        m = n + (n - p)
        # 1487 4817 8147
        if p == 1487 and n == 4817:
            print "break"
        if m in primes:
            ps = set(list(str(p)))
            ns = set(list(str(n)))
            ms = set(list(str(m)))
            if ps == ns and ns == ms:
                print p, n, m

        
