
def nth_digit(n):
    i = 1
    while n > len(str(i)):
        n -= len(str(i))
        i += 1
    return int(str(i)[n-1])

product = 1
for i in range(7):
    product *= nth_digit(10**i)
    print nth_digit(10**i)
print "ANSWER:", product
