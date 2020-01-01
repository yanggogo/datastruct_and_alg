'''
欧几里得算法求最大公约数

思考问题：

1. 如何证明该算法时间复杂度为 O（logN）

定理：
如果 M > N， 则 M % N < M/2

'''


def gcd(a, b):

    while b > 0:
        rem = a % b
        a = b
        b = rem
    return a

test_data = [
    (3, 5, 1),
    (2, 4, 2),
    (10, 10, 10),
    (10, 100, 10),
    (100, 10, 10)
]

for a, b, r in test_data:
    assert gcd(a, b) == r
print("success!")