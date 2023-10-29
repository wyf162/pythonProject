# -*- coding : utf-8 -*-
# @Time: 2023/10/21 12:14
# @Author: yefei.wang
# @File: a.py
import sys

sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
n = I()
a1, a2 = 0, 0
while n > 0:
    a1 += 1
    if a2 == 0 and n % 3 == 1:
        a2 = a1
    n -= (n + 2) // 3

print(a1, a2)
