
class A:
    def __init__(self, b, c):
        print('new A')
        self.b = b
        self.c = c
    def __str__(self):
        return 'A(%s, %s)'%(str(self.b), str(self.c))

class B:
    def __init__(self, x, c):
        print('new B')
        self.x = x
        self.c = c
    def __str__(self):
        return 'B(%s, %s)'%(str(self.x), str(self.c))

class C:
    def __init__(self, y, d):
        print('new C')
        self.y = y
        self.d = d
    def __str__(self):
        return 'C(%s, %s)'%(str(self.y), str(self.d))

class D:
    def __init__(self, z):
        print('new D')
        self.z = z
    def __str__(self):
        return 'D(%s)'%str(self.z)

class app_provider():

    def __init__(self, config):
        self.scope = {}
        self.config = config

    def get_property(self, name, factory):
        if name in self.scope:
            return self.scope[name]
        res = factory()
        self.scope[name] = res
        return res
    
    # TODO: wouldn't it be better if A, B, C accept 'provider' (and not instances of B, C, D)?
    def get_d(self):
        return self.get_property('d', lambda: D(self.config['z']))

    def get_c(self):
        return self.get_property('c', lambda: C(self.config['y'], self.get_d()))

    def get_b(self):
        return self.get_property('b', lambda: B(self.config['x'], self.get_c()))

    def get_a(self):
        return self.get_property('a', lambda: A(self.get_b(), self.get_c()))

config = {'x': 'x', 'y': 'y', 'z': 'z'}
p = app_provider(config)
a = p.get_a()
a = p.get_a()
print(a)



class request_provider():
    def __init__(self, request, app_provider):
        self.request = request
        self.app_provider = app_provider
