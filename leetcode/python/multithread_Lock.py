import threading

class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.locks = {"foo": threading.Lock(), "bar": threading.Lock()}
        self.locks["bar"].acquire()

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in range(self.n):
            self.locks["foo"].acquire()            
            # printFoo() outputs "foo". Do not change or remove this line.        	    
            printFoo()
            self.locks["bar"].release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            self.locks["bar"].acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.locks["foo"].release()

def printFoo():
    print("foo")

def printBar():
    print("bar")

if __name__ == "__main__":
    size = 10
    foobar = FooBar(size)
    threads = []
    for i in range(size):            
        threads.append(threading.Thread(target=foobar.foo, args=(printFoo,)))
        threads.append(threading.Thread(target=foobar.bar, args=(printBar,)))

    for i in range(size):
        threads[i].start()
