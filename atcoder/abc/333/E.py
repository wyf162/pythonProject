# -*- coding : utf-8 -*-
# @Time: 2023/12/16 20:39
# @Author: yefei.wang
# @File: E.py

import sys
from collections import Counter

sys.stdin = open('./../../input.txt')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n = I()
a = [LI() for _ in range(n)]
b = []
c = Counter()
for i in range(n - 1, -1, -1):
    t, x = a[i]
    if t == 1:
        if c[x] > 0:
            c[x] -= 1
            b.append(1)
        else:
            b.append(0)
    elif t == 2:
        c[x] += 1

if any(v > 0 for k, v in c.items()):
    print(-1)
else:
    b = b[::-1]
    k = 0
    j = 0
    rst = 0
    for i in range(n):
        t, x = a[i]
        if t == 1:
            if b[j]:
                k += 1
                rst = max(rst, k)
            j += 1
        elif t == 2:
            k -= 1
    print(rst)
    print(*b)
