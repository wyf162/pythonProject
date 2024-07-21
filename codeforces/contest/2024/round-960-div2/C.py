# -*- coding : utf-8 -*-
# @Time: 2024/7/20 23:25
# @Author: yefei.wang
# @File: C.py

import copy
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    B = copy.deepcopy(A)

    tot = 0
    for _ in range(3):
        st = set()
        mx = 0
        for i in range(n):
            tot += A[i]
            if A[i] in st:
                mx = max(mx, A[i])
            st.add(A[i])
            A[i] = mx

    for i in range(n - 1, -1, -1):
        tot += (n - i) * A[i]
    print(tot)

    # jury = 0
    # while True:
    #     st = set()
    #     mx = 0
    #     for i in range(n):
    #         jury += B[i]
    #         if B[i] in st:
    #             mx = max(mx, B[i])
    #         st.add(B[i])
    #         B[i] = mx
    #
    #     if sum(B) == 0:
    #         break
    # print(_tcn_, tot, jury, tot == jury)
