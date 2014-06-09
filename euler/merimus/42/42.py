
f = open('words.txt', 'r')
file = f.read()
f.close()

base = ord('A') - 1
def value(word):
    # 19 11 25
    sum = 0
    for char in list(word):
        sum += ord(char) - base
    return sum

triangles = set()
for i in range(1, 100):
    triangles.add((i * (i + 1)) / 2)

number = 0
words = file.replace('"', '').split(',')
for word in words:
    if value(word) in triangles:
        number += 1
        print word, value(word)
print "ANSWER:", number
