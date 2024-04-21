# -*- coding : utf-8 -*-
# @Time: 2024/4/20 20:08
# @Author: yefei.wang
# @File: B.py

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, q = MI()
nums = LI()

tot = n
hst = [0] * (n+1)
for x in nums:
    if hst[x] == 0:
        tot -= 1
        hst[x] = 1
    else:
        tot += 1
        hst[x] = 0
print(tot)

