# -*- coding: utf-8 -*-
# @Time: 2024/7/2 11:06
# @Author: yfwang
# @File: 1442B_op.py
# ListNode

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
mod = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    A = LGMI()
    B = LGMI()

    ind = [-1] * n
    for i, a in enumerate(A):
        ind[a] = i
    for i in range(k):
        B[i] = ind[B[i]]

    C = [0] * n
    for i in range(k):
        C[B[i]] = 1

    pre = list(range(-1, n - 1))
    nex = list(range(1, n + 1))

    ans = 1
    for i in range(k):
        cnt = 0
        if pre[B[i]] >=0 and not C[pre[B[i]]]:
            cnt += 1
        if nex[B[i]] <n and not C[nex[B[i]]]:
            cnt += 1
        if cnt == 0:
            ans = 0
            break
        ans *= cnt
        ans %= mod
        if pre[B[i]] >= 0:
            nex[pre[B[i]]] = nex[B[i]]
        if nex[B[i]] < n:
            pre[nex[B[i]]] = pre[B[i]]

    print(ans)
