
import itertools

def test(digits, divisor):
    return int(''.join(digits)) % divisor == 0

n = 0
sum = 0
for p in itertools.permutations(list("0123456789")):
    n += 1
    if n % 10000 == 0:
        print n
    if test(p[1:4], 2) and test(p[2:5], 3) and test(p[3:6], 5) and test(p[4:7], 7) and test(p[5:8], 11) and test(p[6:9], 13) and test(p[7:10], 17):
        print p
        sum += int(''.join(p))
print "ANSWER:", sum
