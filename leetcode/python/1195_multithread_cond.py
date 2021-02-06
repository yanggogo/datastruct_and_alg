import threading


class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.atom_n = 1
        self.cond = threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for i in range(int(self.n/3)-int(self.n/15)):
            self.cond.acquire()
            while not (self.atom_n % 3 == 0 and self.atom_n % 5 != 0):
                self.cond.wait()
            printFizz()
            self.atom_n += 1
            self.cond.notify_all()
            self.cond.release()


    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        for i in range(int(self.n/5)-int(self.n/15)):
            self.cond.acquire()
            while not (self.atom_n % 5 == 0 and self.atom_n % 3 != 0):
                self.cond.wait()
            printBuzz()
            self.atom_n += 1
            self.cond.notify_all()
            self.cond.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for i in range(int(self.n/15)):
            self.cond.acquire()
            while not (self.atom_n % 3 == 0 and self.atom_n % 5 == 0):
                self.cond.wait()
            printFizzBuzz()
            self.atom_n += 1
            self.cond.notify_all()
            self.cond.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n - int(self.n/3) - int(self.n/5) + int(self.n/15)):
            self.cond.acquire()
            while not (self.atom_n % 3 != 0 and self.atom_n % 5 != 0):
                self.cond.wait()
            printNumber(self.atom_n)
            self.atom_n += 1
            self.cond.notify_all()
            self.cond.release()

def printNumber(x):
    print(x)

def printFizz():
    print("fizz")

def printFizzBuzz():
    print("fizzbuzz")

def printBuzz():
    print("buzz")

if __name__ == "__main__":
    obj = FizzBuzz(16)
    fiz = threading.Thread(target=obj.fizz, name="fizz", args=(printFizz,))
    buz = threading.Thread(target=obj.buzz, name="buzz", args=(printBuzz,))
    fizbuz = threading.Thread(target=obj.fizzbuzz, name="fizzbuzz", args=(printFizzBuzz,))
    number = threading.Thread(target=obj.number, name="number", args=(printNumber,))

    threads = [fiz, buz, fizbuz, number]
    for t in threads:
        t.start()
