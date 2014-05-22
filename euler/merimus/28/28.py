
size = 1001
sum = 1
n = 1
for i in range(2, size/2+2):
    for c in range(4):
        n += 2*(i-1)
        sum += n
print sum
