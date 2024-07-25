# -*- coding : utf-8 -*-
# @Time: 2024/7/25 23:36
# @Author: yefei.wang
# @File: 1023D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 1
for _tcn_ in range(tcn):
    n, q = MI()
    A = LI()
    if max(A) < q and 0 not in A:
        print('NO')
        continue
    elif max(A) < q:
        A[A.index(0)] = q

    for i in range(n - 2, -1, -1):
        if A[i] == 0:
            A[i] = A[i + 1]
    for i in range(1, n, 1):
        if A[i] == 0:
            A[i] = A[i - 1]
    # print(A)

    hst = dict()
    for i, a in enumerate(A):
        hst[a] = i

    for i in range(n-1):
        if A[i+1] < A[i] and hst[A[i]] > i:
            print('NO')
            break
    else:
        print('YES')
        print(*A)
