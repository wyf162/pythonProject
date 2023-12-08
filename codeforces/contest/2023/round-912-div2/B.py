# -*- coding : utf-8 -*-
# @Time: 2023/12/1 1:02
# @Author: yefei.wang
# @File: B.py

import sys

sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    mtx = [LI() for _ in range(n)]
    B = 30
    a = [0] * n
    for b in range(B):
        for i in range(n):
            x = 1
            for j in range(n):
                if i == j:
                    continue
                x &= mtx[i][j] >> b
            if x:
                a[i] |= (1 << b)
    ans = True
    for i in range(n):
        for j in range(i + 1, n):
            if i != j and mtx[i][j] != a[i] | a[j]:
                ans = False
                break
        if not ans:
            break
    if ans:
        print('Yes')
        print(*a)
    else:
        print('No')
