
order = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def permute(a):
    # Find the largest index k such that a[k] < a[k + 1].
    found = False
    for k in reversed(range(0, len(a) - 1)):
        if a[k] < a[k+1]:
            found = True
            break
    if not found:
        return False

    # Find the largest index l such that a[k] < a[l].
    for l in reversed(range(0, len(a))):
        if a[k] < a[l]:
            break

    # Swap the value of a[k] with that of a[l].
    t = a[k]
    a[k] = a[l]
    a[l] = t

    # Reverse the sequence from a[k + 1] up to and including the final element a[n]
    t = a[k+1:]
    t.reverse()
    a[k+1:] = t
    return True

cnt = 1
while cnt != 1000000:
    permute(order)
    cnt += 1
print "".join(order)

