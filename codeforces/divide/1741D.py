# -*- coding : utf-8 -*-
# @Time: 2024/2/4 16:13
# @Author: yefei.wang
# @File: 1741D.py
import copy
import math
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    perm = LI()
    perm1 = copy.deepcopy(perm)
    B = int(math.log2(n))
    # print(B)
    ops = 0
    for b in range(B):
        perm2 = []
        step = 1 << b
        for x in range(0, n, step * 2):
            x1, x2 = x, x + step
            if perm1[x1] > perm1[x2]:
                ops += 1
                for i in range(x2, x2 + step):
                    perm2.append(perm1[i])
                for i in range(x1, x1 + step):
                    perm2.append(perm1[i])
            else:
                for i in range(x1, x1 + step):
                    perm2.append(perm1[i])
                for i in range(x2, x2 + step):
                    perm2.append(perm1[i])
        perm1 = perm2
    for i in range(n):
        if perm1[i] != i + 1:
            print(-1)
            break
    else:
        print(ops)
