import sys

def cycle(n):
    seen = set()
    d = 1 / n
    r = 1 % n
    seen.add(r)
    count = 0
    watchfor = 0
    inCycle = False
    while True:
        d = (r * 10) / n
        sys.stdout.write(str(d))
        r = (r * 10) % n

        if r == watchfor:
            return count
        if r in seen:
            if not inCycle:
                watchfor = r
            inCycle = True
            count += 1
        seen.add(r)

index = 0
current = 0
for i in range(2, 1000):
    n = cycle(i)
    print " ", i, n
    if n > current:
        index = i
        current = n
print index, current
