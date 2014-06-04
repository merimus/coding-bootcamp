import math

def pandigital(n, m):
    digits = []
    # take n and multiply it by 1..m, return true
    # if the results are pandigital.
    for i in range(1, m+1):
        digits += list(str(n * i))
    if len(digits) != 9:
        return False
    s = set(digits)
    if len(s) != 9:
        return False
    if '0' in s:
        return False
    print n, m, int("".join(digits))
    return int("".join(digits))

m = 0
for x in range(1, 99999):
    l = (9 / len(str(x))) + 2
    for y in range(2, l):
        p = pandigital(x, y)
        if p:
            m = max(m, p)
print "ANSWER:", m
    
