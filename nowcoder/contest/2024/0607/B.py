# -*- coding : utf-8 -*-
# @Time: 2024/6/7 19:11
# @Author: yefei.wang
# @File: B.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()

if n % 2:
    ans1 = (3 + n) * ((n - 3) // 2 + 1) // 2
    ans2 = (2 + n - 1) * ((n - 1 - 2) // 2 + 1) // 2 // 2
    ans = ans1 + ans2
    print(ans % mod)
else:
    ans1 = (3 + n - 1) * ((n - 1 - 3) // 2 + 1) // 2
    ans2 = (2 + n) * ((n - 2) // 2 + 1) // 2 // 2
    ans = ans1 + ans2
    print(ans % mod)
