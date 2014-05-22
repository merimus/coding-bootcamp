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

def digits(n):
    tmp = n
    result = []
    while tmp > 0:
        result.append(tmp % 10)
        tmp /= 10
    result.reverse()
    return result

def number(d):
    tmp = map(lambda x:str(x), d)
    return int(''.join(tmp))

def test(p, n):
    d = digits(n)
    for i in range(len(d)):
        if not p.IsPrime(number(d)):
            return False
        tmp = d[0]
        d = d[1:]
        d.append(tmp)
    return True

num = 0
p = Primes()
for i in range(2, 1000000):
    if test(p, i):
        print i
        num += 1
print "ANSWER:", num
        
