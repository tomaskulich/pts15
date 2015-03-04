
from collections import namedtuple
User = namedtuple('User', ['first', 'last'])

u1 = User('Jozo', 'Jedna')
u2 = User(first='Jozo', last='Jedna')

print(u1)
print(u1.first)
print(u1 == u2)
