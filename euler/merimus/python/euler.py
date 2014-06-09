import math

class Primes(object):
    # Generate primes and perform primality testing.
    def __init__(self):
        self.primes = set([2, 3, 5, 7])
        self.lastprime = 7

    def Primes(self):
        # Generate infinite list of primes.
        for p in self.primes:
            yield p
        while True:
            yield self.NextPrime()

    def NextPrime(self):
        # Return next prime bigger then those in self.primes.
        primes = sorted(self.primes)
        n = self.lastprime + 2
        found = False
        while not found:
            cuttoff = math.sqrt(n)
            for p in primes:
                if p > cuttoff:
                    found = True
                    self.primes.add(n)
                    self.lastprime = n
                    return n
                if n % p == 0:
                    n += 2
                    break

    def IsPrime(self, p):
        lastprime = max(self.primes)
        while lastprime < p:
            lastprime = self.NextPrime()
        return p in self.primes

def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
