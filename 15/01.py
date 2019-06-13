# counter 
from collections import Counter

l = [11,1,2,2,1,21,2,1,1,2,1,1,1,15,4,5,5,54,4,5,4,45]

print(Counter(l))

s = 'asssssvvaavavavassbbbbba'

print(Counter(s))

s = 'How many times does each word shop up in this sentence word word shoe up up'

words = s.split()

print(Counter(words))

c = Counter(words)

print(c.most_common(2))

print(sum(c.values()))
