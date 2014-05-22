
def test(a, b, p1, p2):
    n = a / float(b)
    sa = str(a)
    sb = str(b)
    if sa[p1] == sb[p2]:
        if sa[p1] == '0' and sb[p2] == '0':
            # trivial
            return False
        x = int(sa[(p1 + 1) % 2])
        y = int(sb[(p2 + 1) % 2])
        if x == y:
            # trivial
            return False
        if y == 0:
            return False
        if n == (x / float(y)):
            print "%i/%i = %d, %i/%i = %d" % (a, b, n, x, y, x / float(y))
            return True
    return False

n = 1
d = 1
for a in range(10, 100):
    for b in range(a, 100):
        for x in range(2):
            for y in range(2):
                if test(a, b, x, y):
                    n *= a
                    d *= b
print n, d
