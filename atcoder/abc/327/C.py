# -*- coding : utf-8 -*-
# @Time: 2023/11/4 20:07
# @Author: yefei.wang
# @File: C.py

import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

N = 9
mtx = [LI() for _ in range(N)]

for i in range(N):
    if len(set(mtx[i])) == N:
        continue
    else:
        exit(print('No'))

for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append(mtx[j][i])
    if len(set(tmp)) == N:
        continue
    else:
        exit(print('No'))

for i in range(0, N, 3):
    for j in range(0, N, 3):
        tmp = []
        for a in range(i, i+3):
            for b in range(j,j+3):
                tmp.append(mtx[a][b])
        if len(set(tmp)) == N:
            continue
        else:
            exit(print('No'))
exit(print('Yes'))