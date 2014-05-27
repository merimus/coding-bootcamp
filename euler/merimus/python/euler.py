import math

class Primes(object):
    # Generate primes and perform primality testing.
    def __init__(self):
        self.primes = set([2, 3, 5, 7])

    def Primes(self):
        # Generate infinite list of primes.
        for p in self.primes:
            yield p
        while True:
            yield self.NextPrime()

    def NextPrime(self):
        # Return next prime bigger then those in self.primes.
        primes = sorted(self.primes)
        n = max(self.primes) + 2
        found = False
        while not found:
            cuttoff = math.sqrt(n)
            for p in primes:
                if p > cuttoff:
                    found = True
                    self.primes.add(n)
                    return n
                if n % p == 0:
                    n += 2
                    break

    def IsPrime(self, p):
        lastprime = max(self.primes)
        while lastprime < p:
            lastprime = self.NextPrime()
        return p in self.primes

