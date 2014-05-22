

n1 = 1
n2 = 1
index = 2

done = False
while not done:
    index += 1
    # the IndexTh fib number is.
    fib = n1 + n2
    n2 = n1
    n1 = fib
    if len(str(fib)) >= 1000:
        print index
        done = True


