
def divisors(n):
    # return list (numbers less than n which divide evenly into n)
    return [i for i in range(1, (n+1)/2+1) if n % i == 0]

d_mem = dict()
def d(n):
    if n in d_mem:
        return d_mem[n]
    d_mem[n] = sum(divisors(n))
    return d_mem[n]

def isAmicable(n):
    a = d(n)
    if a == n:
        return False;
    b = d(a)
    return b == n

print sum([n for n in range(1, 10000-1) if isAmicable(n)])
