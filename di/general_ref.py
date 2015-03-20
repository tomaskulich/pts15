
....

b = B(x)
c = C(y)
da = lambda x: D(x).action() 
a = A(b,c,da)

class A:

    @staticmethod
    def getDefault():
        b = B()
        c = C()
        return A(b,c)


    def __init__(self, b, c, da):
        self.b = b
        self.c = c
        self.da = da


    def do_something(self, x)
        result = self.da()
        ...


    def do_another(self):
        ...
        ... <- highly cohesive piece of code
        ...
        
        ...
        ...
        ...

        ...
        ... <- other highly cohesive piece of code
        ...
