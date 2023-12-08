# -*- coding : utf-8 -*-
# @Time: 2023/11/19 22:35
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
    s = input()
    b = s.count('B')
    if b == k:
        print('0')
    elif b < k:
        for i in range(n):
            if s[i] == 'A':
                b += 1
            if b == k:
                print(1)
                print(i+1, 'B')
                break
    else:
        for i in range(n):
            if s[i] == 'B':
                b -= 1
            if b == k:
                print(1)
                print(i+1, 'A')
                break
