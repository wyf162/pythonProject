# -*- coding : utf-8 -*-
# @Time: 2023/12/3 14:20
# @Author: yefei.wang
# @File: C.py


import sys

sys.stdin = open('../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
i = 1
while True:
    s = 1
    k = 1
    for _ in range(4):
        k *= i
        s += k
    if s == n:
        exit(print('Yes'))
    elif s > n:
        exit(print('No'))
        break
    else:
        i += 1
