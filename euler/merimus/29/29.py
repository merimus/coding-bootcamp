
values = set()
for a in range(2, 101):
    for b in range(2, 101):
        values.add(a**b)
print len(values)
