# -*- coding : utf-8 -*-
# @Time: 2024/1/19 19:21
# @Author: yefei.wang
# @File: C.py

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

n, m = MI()
A = LI()

pre_sum = [0] * (n+1)
pre_sum[1] = 1
for i in range(1, n):
    pre_sum[i+1] += pre_sum[i] + int(A[i] != A[i-1])

for _ in range(m):
    i1, i2 = GMI()
    ret = pre_sum[i2+1] - pre_sum[i1]
    if i1 > 0 and A[i1] == A[i1-1]:
        ret += 1
    print(ret)
