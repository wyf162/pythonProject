# -*- coding : utf-8 -*-
# @Time: 2023/12/1 0:56
# @Author: yefei.wang
# @File: B.py

import sys

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    a = LI()
    if k == 1:
        for i in range(1, n):
            if a[i - 1] > a[i]:
                print('NO')
                break
        else:
            print('YES')
    else:
        print('YES')
