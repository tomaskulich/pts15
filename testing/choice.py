import random
from collections import Counter

def choice(options):
    options = list(options)
    rnd = random.random()
    for option, p in options:
        rnd -= p
        if rnd <= 0: return option

options = [('a', 0.1), ('b', 0.2), ('c', 0.3), ('d', 0.4)]
#print(choice(options))

random_orig = random
counter = Counter(choice(options) for i in range(1000))

print(counter.most_common())



