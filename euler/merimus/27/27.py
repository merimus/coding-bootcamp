import math

class GenPrime(object):
    def __init__(self):
        self.primes = [2, 3, 5, 7]
    def Primes(self):
        for p in self.primes:
            yield p
        while True:
            yield self.GenPrime()
    def IsPrime(self, n):
        cuttoff = math.sqrt(n)
        for p in self.primes:
            if p > cuttoff:
                return True
            if n % p == 0:
                return False
    def GenPrime(self, n):
        c = n + 1
        while not self.IsPrime(c):
            c += 1
        self.primes.append(c)
        return c

class Primes(object):
    def __init__(self):
        self.primes = set([2, 3, 5, 7])
        self.lastprime = 7
        self.gp = GenPrime()
    def IsPrime(self, p):
        while self.lastprime < p:
            self.lastprime = self.gp.GenPrime(self.lastprime)
            self.primes.add(self.lastprime)
        return p in self.primes

#n^2 + an + b, where |a|  1000 and |b|  1000
p = Primes()
biggest = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while p.IsPrime(n**2 + a*n + b):
            n += 1
        if n > biggest:
            biggest = n
            print a, b, n, a*b

        
