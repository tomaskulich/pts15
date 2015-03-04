
class Username:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return "%s %s"%(self.first, self.last)

    def __len__(self):
        return 2

def str(obj):
    if not hasattr(obj, '__str__'):
        raise Exception('hey dude, you cannot put this to str')
    return obj.__str__()
