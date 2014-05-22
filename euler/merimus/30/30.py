
def sumfifthpowers(num):
    tmp = num
    sum = 0
    while tmp > 0:
        digit = tmp % 10
        tmp /= 10
        sum += digit**5
    return sum

sum = 0
for i in range(2, 1000000):
    if i == sumfifthpowers(i):
        print i
        sum += i
print sum
