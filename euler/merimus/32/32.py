
def digits(a):
    d = []
    tmp = a
    while tmp > 0:
        d.append(tmp % 10)
        tmp /= 10
    return d

def pandigital(a, b, c):
    la = digits(a)
    lb = digits(b)
    lc = digits(c)
    if len(la + lb + lc) != 9:
        return False
    s = set(la + lb + lc)
    if 0 in s:
        return False
    return len(set(la + lb + lc)) == 9

import math
products = set()
for a in range(1, 10000):
    for b in range(a, 10000):
        if math.ceil(math.log10(a)) + math.ceil(math.log10(b)) > 5:
            break
        if pandigital(a, b, a * b):
            products.add(a * b)
            print a, b, a * b
sum = 0
for p in products:
    sum += p
print sum
