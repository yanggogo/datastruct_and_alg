'''
关于取模的几个公式

概念：
如果（A-B）% C == 0，则认为 A%C == B%C，表示A，B同模与C。

1. 如果 A%C == B%C，则  （A+D）% C == （B+D）% C

2. 如果 A%C == B%C，则  （A*D）% C == （B*D）% C 

3. A%C == (A%C) % C

证明方法： 令 A = M*C + A%C， 其中M = A/C

请求出：

思考问题一：

2^100 % 5 == ?

            ((a^(b/2))%c * (a^(b/2))%c) % c        if b % 2 == 0
          /
a^b % c = 
          \
            ((a^(b/2))%c * (a^(b/2))%c * a) % c    if b % 2 == 1


思考问题二：

求a 和 b 的最大公约数

greateast common divisor

'''

def gcd(a, b):
    pass