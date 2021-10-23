# coding=utf-8
import threading

def printNumber(x):
    print(x)

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.atom_n = 0
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)
        # self.cond_z = threading.Condition(self.lock)
        # self.cond_e = threading.Condition(self.lock)
        # self.cond_o = threading.Condition(self.lock)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n):
            self.cond.acquire()
            while self.atom_n % 2 != 0:
                self.cond.wait()
            self.atom_n += 1
            printNumber(0)
            self.cond.notify_all()
            # if self.atom_n % 4 == 1:
            #     self.cond_o.notify()
            # elif self.atom_n % 4 == 3:
            #     self.cond_e.notify()
            self.cond.release()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(int(self.n/2)):
            self.cond.acquire()
            while self.atom_n % 4 != 3:
                self.cond.wait()
            self.atom_n += 1
            printNumber(int(self.atom_n / 2))
            self.cond.notify_all()
            self.cond.release()

    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(int((self.n+1)/2)):
            self.cond.acquire()
            while self.atom_n % 4 != 1:
                self.cond.wait()
            printNumber(1 + int(self.atom_n / 2))
            self.atom_n += 1
            self.cond.notify_all()
            self.cond.release()


if __name__ == "__main__":
    obj = ZeroEvenOdd(5)
    even_t = threading.Thread(target=obj.even, name="even", args=(printNumber,))
    odd_t = threading.Thread(target=obj.odd, name="odd", args=(printNumber,))
    zero_t = threading.Thread(target=obj.zero, name="zero", args=(printNumber,))
    zero_t.start()
    even_t.start()
    odd_t.start()


'''
test-host-001:~/xd # top -H -p 11412 
top - 07:30:52 up  4:34,  2 users,  load average: 3.21, 2.90, 2.59
Tasks:   2 total,   0 running,   2 sleeping,   0 stopped,   0 zombie
Cpu(s): 16.2%us, 33.1%sy,  0.0%ni, 50.5%id,  0.3%wa,  0.0%hi,  0.0%si,  0.0%st
Mem:     32113M total,    16736M used,    15376M free,      154M buffers
Swap:     4091M total,        0M used,     4091M free,      609M cached

  PID USER      PR  NI  VIRT  RES  SHR S   %CPU %MEM    TIME+  COMMAND                                                                                                                     
11412 root      20   0  118m 4196 1780 S      0  0.0   0:00.00 python                                                                                                                       
11414 root      20   0  118m 4196 1780 S      0  0.0   0:00.00 python       


如果for循环终止条件不对，线程会阻塞在获取条件变量的锁上，
也就是语句 self.cond.acquire()这里
test-host-001:~/xd # cat /proc/11412/stack 
[<ffffffff81095175>] futex_wait_queue_me+0xc5/0x110
[<ffffffff81095337>] futex_wait+0x117/0x250
[<ffffffff81097bc8>] do_futex+0xb8/0x1c0
[<ffffffff81097d52>] sys_futex+0x82/0x170
[<ffffffff81464592>] system_call_fastpath+0x16/0x1b
[<00007fe2f23c9a00>] 0x7fe2f23c9a00
[<ffffffffffffffff>] 0xffffffffffffffff
'''
