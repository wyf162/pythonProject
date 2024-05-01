# -*- coding : utf-8 -*-
# @Time: 2024/5/1 0:13
# @Author: yefei.wang
# @File: D1.py

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

# N = 2 * 10 ** 6 + 5
# f = [i for i in range(N)]
# for i in range(2, N + 1):
#     f[i] = f[i - 1] + (a // i + 1) // i

hst = dict()

tcn = I()
for _tcn_ in range(tcn):
    a, b = MI()
    if (a, b) in hst:
        print(hst[(a, b)])
        continue
    ans = a
    for i in range(2, b + 1):
        ans += (a // i + 1) // i
    hst[(a, b)] = ans
    print(ans)
