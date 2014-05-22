
def divisors(n):
    # return list (numbers less than n which divide evenly into n)
    return [i for i in range(1, (n+1)/2+1) if n % i == 0]

d_mem = dict()
def d(n):
    if n in d_mem:
        return d_mem[n]
    d_mem[n] = sum(divisors(n))
    return d_mem[n]

def isAbundant(n):
    a = d(n)
    return a > n

print "compute abundant"
abundant = [n for n in range(1, 28123+1) if isAbundant(n)]
sum_of_abundant = set()
print "compute sum of two abundant"
for x in abundant:
    for y in abundant:
        sum_of_abundant.add(x + y)
print "generate result"
print sum([x for x in range(28123+1) if x not in sum_of_abundant])
