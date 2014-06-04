import math

data = dict()

for a in range(1, 1000):
    for b in range(1, 1000):
        if a + b > 1000:
            continue
        # would the last side be integral?
        c = math.sqrt(a * a + b * b)
        if c == int(c):
            p = a + b + int(c)
            if p > 1000:
                continue
            data[p] = data.get(p, 0) + 1

num = 0
perimeter = 0
for p, n in data.iteritems():
    if n > num:
        perimeter = p
        num = n
print perimeter, num
        
