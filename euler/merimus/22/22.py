




all_words = []
for line in open("names.txt"):
    words = line.split(',')
    stripped = [w.strip('"') for w in words]
    all_words.extend(stripped)
all_words.sort()

def value(word):
    return sum([ord(w) - 64 for w in word])

position = 1
total = 0
for word in all_words:
    total += value(word) * position
    position += 1
print total
