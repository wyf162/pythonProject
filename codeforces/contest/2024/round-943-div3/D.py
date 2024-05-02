# -*- coding : utf-8 -*-
# @Time: 2024/5/2 23:03
# @Author: yefei.wang
# @File: D.py


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
    n, k, pb, ps = MI()
    P = [0] + LI()
    A = [0] + LI()

    B = []
    cur = pb
    for _ in range(k):
        B.append(A[cur])
        cur = P[cur]
        if cur == pb:
            break
    mxb = max(B)
    mxi = B.index(mxb)
    score_bodya = 0
    pre_sum = 0
    for i in range(len(B)):
        pre_sum += B[i]
        score_bodya = max(score_bodya, pre_sum + B[i] * (k - i - 1))
    # print(score_bodya)
    # print(B)

    B = []
    cur = ps
    for _ in range(k):
        B.append(A[cur])
        cur = P[cur]
        if cur == ps:
            break
    mxb = max(B)
    mxi = B.index(mxb)
    score_sasha = 0
    pre_sum = 0
    for i in range(len(B)):
        pre_sum += B[i]
        score_sasha = max(score_sasha, pre_sum + B[i] * (k - i - 1))
    # print(score_sasha)
    # print(B)

    if score_bodya == score_sasha:
        print('Draw')
    elif score_bodya > score_sasha:
        print('Bodya')
    else:
        print('Sasha')
