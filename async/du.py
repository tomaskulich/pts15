from eventloop import EventLoop, my_print, printer
from functools import partial

class Promise():

    def __init__(self, resolver):
        pass


    def then(self, then_fn):
        pass
    
    def delayed(time, val = None):
        """
        creates promise which resolves after time `time` with value `val`
        """

        def resolver(resolve, reject):
            e.wait(time, lambda: resolve(val))

        return Promise(resolver)

    def all(list_of_promises):
        """
        Promise.all(list_of_promises) returns a new promise which resolves when all the promises from
        the given argument resolve. Result is a list cotaining values of individual promises in
        list_of_promises. Similar to bluebirdPromise.all
        """
        pass
    
    def foreach(iterable, get_promise):
        """
        executes `get_promise` on each element from `iterable`. Results from `get_promise` are
        waited for within the iteration.

        foreach pseudocode:
        
        for elem in iterable:
            p = get_promise(elem)
            wait for p to fulfill, then continue

        """
        pass


def print_inc_wait(res):
    print(res)
    res += 1
    return Promise.delayed(1, res)

def test1():
    """
    basic promise functionality.

    should print begin, 0, 1, 2, 3 in one second intervals
    moreover, `then` should return Promise object
    """
    p = Promise.delayed(1,0) \
    .then(print_inc_wait) \
    .then(print_inc_wait) \
    .then(print_inc_wait) \
    .then(my_print)
    print('begin')
    assert(isinstance(p, Promise))

def test2():
    """
    Test if promises are flattening returning values correctly.

    Two snippets in this test should behave indistinguishibly from the outside world;
    both should print '1' after 1 second delay
    """
    Promise.delayed(1,0) \
    .then(lambda x: x+1) \
    .then(my_print)

    Promise.delayed(1,0) \
    .then(lambda x: Promise.delayed(0, x+1)) \
    .then(my_print)

def test3():
    """
    Two "Promise chains" may be run at once
     
    should print 1 1 [delay] 2 2 [delay] 3 3
    """
    def get_promise():
        return Promise.delayed(1,0) \
            .then(print_inc_wait) \
            .then(print_inc_wait) \
            .then(print_inc_wait) 

    get_promise()
    get_promise()

def test4():
    """
    creating new Promise works as it should
    """
    def resolver(resolve, reject):
        e.wait(2, lambda: resolve(10))

    # ugly long line, what should I do about it?
    Promise(resolver).then(lambda res: my_print("should print this after 2 seconds, moreover, this should be 10: %d"%res))

def test5():
    """
    Tests await.

    Should print [0, 2, 4, 8, 10] after 5 seconds (because the last Promise from the given list
    resolves after 5 seconds)
    """

    list_of_promises = [Promise.delayed(5-i, 2*i) for i in range(5)]
    Promise.await(list_of_promises).then(my_print)

def test6():
    """
    Tests foreach.

    Should print 1, [delay 1s], 2, [delay 2s], 3, [delay 3s], 4
    """

    def f(x):
        print('%d'%x)
        return Promise.delayed(x, x)

    Promise.foreach([1, 2, 3, 4], f)

e = EventLoop()
e.start()


#test1()
#test2()
#test3()
#test4()
#test5()
#test6()









