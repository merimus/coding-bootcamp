
def twobasepalindrome(n):
    # palindrome in base 10?
    a = list(str(n))
    b = list(a)
    b.reverse()
    if cmp(a, b) != 0:
        return False

    # palindrome in base 2
    a = list(bin(n)[2:])
    b = list(a)
    b.reverse()
    if cmp(a, b) != 0:
        return False
    return True

sum = 0
for n in range(1000000):
    if twobasepalindrome(n):
        print n
        sum += n
print "ANSWER:", sum
