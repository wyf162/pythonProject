# -*- coding : utf-8 -*-
# @Time: 2024/1/17 20:07
# @Author: yefei.wang
# @File: 1542C.py
import bisect
import sys
import math


def lcm_of_array(a):
    lcm = a[0]
    for i in range(1, len(a)):
        lcm = lcm * a[i] // math.gcd(lcm, a[i])
    return lcm


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    ans = 0
    l = 1
    for i in range(2, 45):
        c = n//l - n // math.lcm(l, i)
        # print(i, c)
        ans += i * (n//l - n // math.lcm(l, i))
        ans %= mod
        l = math.lcm(l, i)
    print(ans)
