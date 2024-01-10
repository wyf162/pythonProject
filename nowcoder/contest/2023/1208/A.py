# -*- coding : utf-8 -*-
# @Time: 2023/12/8 19:00
# @Author: yefei.wang
# @File: A.py
import math
import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n = I()
a = LI()
s = sum(a)

for k in range(1, n + 1):
    p, q = s * k, n
    c = math.gcd(p, q)
    p, q = p // c, q // c
    # inve = pow(q, -1, mod2)
    inve = pow(q, mod2 - 2, mod2)
    ans = p * inve % mod2
    print(ans, end=' ')
print()
