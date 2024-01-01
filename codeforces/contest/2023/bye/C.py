# -*- coding : utf-8 -*-
# @Time: 2023/12/30 23:22
# @Author: yefei.wang
# @File: C.py

import math
import sys

sys.stdin = open('./../../../input.txt')
input = lambda: sys.stdin.readline().rstrip('\r\n')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

N = 10 ** 5 + 5
f = [0] * N
f[1] = 1
f[2] = 0
f[3] = 1
for i in range(4, N):
    f[i] = f[i-3] + 1
# print(f[:11])

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    odd = 0
    pre_sum = 0
    ans = []
    for i in range(n):
        pre_sum += a[i]
        if a[i] % 2 == 1:
            odd += 1
        if i == 0:
            ans.append(pre_sum)
        else:
            ans.append(pre_sum - f[odd])
    print(*ans)
