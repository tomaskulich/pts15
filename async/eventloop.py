from queue import Queue
from threading import Thread, Condition
from time import sleep
from math import sqrt


class EventLoop():

    def __init__(self):
        self.queue = Queue()
        self.lock = Condition()

    def start(self):
        def _start():
            with(self.lock):
                while True:
                    while not self.queue.empty():
                        fn = self.queue.get()
                        fn()
                    self.lock.wait()
        Thread(target=_start).start()
        
    def run(self, action):
        with(self.lock):
            self.queue.put(action)
            self.lock.notify_all()

    def wait(self, time, callback):
        def to_run():
            sleep(time)
            #TODO: why not just use
            # callback()
            self.run(callback)
        Thread(target = to_run).start()

    def read_file(self, filename, callback):
        def to_run():
            f = open(filename, 'r')
            res = f.read()
            # TODO: why not just use
            # callback(res)
            self.run(lambda: callback(res))
        Thread(target = to_run).start()

def my_print(message):
    print(message)

def printer(message):
    def res():
        print(message)
    return res

if __name__ == 'main':
    e = EventLoop()
    e.start()

    def ex1():
        e.run(printer('ahoj'))
        e.run(printer('svet'))
        e.run(printer(':)'))
    ex1()


    def ex2():
        e.wait(1, printer('Ich'))
        e.wait(2, printer('bin'))
        e.wait(3, printer('scheduled'))
        print('ejchuchu!')
    ex2()

    def ex3():
        e.read_file('dummy.txt', my_print)
        print('ejchuchu!')
    ex3()

    def ex4():

        def cb1():
            print('Ich')
            e.wait(1, cb2)

        def cb2():
            print('bin')
            e.wait(1, cb3)

        def cb3():
            print('in der')
            e.wait(1, cb4)

        def cb4():
            print('Callback-Hölle :(')

        e.wait(1, cb1)

    ex4()

    def freeze():
        def cb():
            print('tututu')
            e.run(cb)
        e.run(cb)
        def cb2():
            print('aaaaaa')
            e.run(cb2)
        e.run(cb2)
    #freeze()

    def is_prime(n, cb):
        chunk_size = 100
        def trynk(n, k):
            if k > sqrt(n):
                e.run(lambda: cb(True))
                return
            for i in range(k, k + chunk_size):
                if n%i == 0:
                    e.run(lambda: cb(False))
                    return 
            e.run(lambda: trynk(n, k + chunk_size))
        e.run(lambda: trynk(n, 2))

