# -*- coding : utf-8 -*-
# @Time: 2023/12/3 15:05
# @Author: yefei.wang
# @File: G.py

import copy
import math
import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 998244353

n, m, k = MI()
mtx = [['' for j in range(m)] for i in range(n)]
for _k_ in range(k):
    i, j, c = input().split()
    i = int(i) - 1
    j = int(j) - 1
    mtx[i][j] = c
    for nj in range(max(j - 5, 0), j + 1, 1):
        if ''.join(mtx[i][nj:nj + 5]) == 'HNIST':
            exit(print(_k_ + 1))

print('Oh no!')
