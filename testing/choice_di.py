import random
from collections import Counter

def choice(options, random_gen = random.random):
    options = list(options)
    rnd = random_gen()
    for option, p in options:
        rnd -= p
        if rnd <= 0: return option

options = [('a', 0.1), ('b', 0.2), ('c', 0.3), ('d', 0.4)]

random_orig = random

def random_gen_factory(dx):
    val = 0
    def res():
        nonlocal val
        old_val = val
        val += dx
        return old_val
    return res

generator = random_gen_factory(0.001)
#for i in range(100):
#    print(generator())


counter = Counter(choice(options, random_gen = generator) for i in range(1000))

print(counter.most_common())



