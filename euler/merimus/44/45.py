
def nth_pentagonal(n):
    return n * (3 * n - 1) / 2

n = 10000
pentagonals = map(nth_pentagonal, range(1, n))
set_pentagonals = set(pentagonals)

smallest = None
for i in range(0, n-1):
    for j in range(i, n-1):
        pi = pentagonals[i]
        pj = pentagonals[j]
        if (pi + pj) in set_pentagonals and (pj - pi) in set_pentagonals:
            if not smallest:
                smallest = pj - pi
            smallest = min(smallest, pj - pi)
            print i, j, pi, pj, pj - pi
print "ANSWER:", smallest

