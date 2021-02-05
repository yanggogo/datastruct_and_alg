# FNV hash算法

参考： https://www.cnblogs.com/davygeek/p/10705721.html
https://zhuanlan.zhihu.com/p/299237346


```c
FNV_prime = (1 << 24) + (1 << 8) + 0x193;
BASIS = 0x811c9dc5
hash = BASIS;
for each octet_of_data to be hashed
     hash = hash * FNV_prime
     hash = hash ^ (octet_of_data & 0xFF)
return hash;
```

```python

def get_fnv_hash(key, len):
    FNV_prime = pow(2, 24) + pow(2, 8) + 0x193
    BASIS = 0x811c9dc5
    hash = BASIS
    for i in range(len):
        hash = hash ^ (key[i] & 0xFF)
        hash = hash * FNV_prime
    return hash
```

DHThash过程

1. 根据FNV hash算法计算关键字的hash值
2. 根据集群总pt_num数，得到数据存放对应的pt_id = hash%pt_num

为什么上述过程可以实现扩减容时的一致性hash呢？

