# -*- coding : utf-8 -*-
# @Time: 2024/5/2 22:54
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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    A = [0] * n
    A[0] = 1000
    for i in range(n-1):
        A[i+1] = A[i] + nums[i]
    print(*A)
    # check = []
    # for i in range(1, n):
    #     check.append(A[i] % A[i-1])
    # print(*check)
    # print()
