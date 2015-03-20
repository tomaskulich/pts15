
...
class A:
    def __init__(self, x, y, z):
        d = D(z)
        self.c = C(y, d)
        self.b = B(x, self.c)


