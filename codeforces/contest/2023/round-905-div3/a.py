# -*- coding : utf-8 -*-
# @Time: 2023/10/22 19:08
# @Author: yefei.wang
# @File: a.py
import sys

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    s = input()
    pre = 1
    ans = 4
    for i in range(4):
        x = int(s[i])
        if x == 0:
            x = 10
        if x > pre:
            ans += x - pre
            pre = x
        elif x < pre:
            ans += pre - x
            pre = x
    print(ans)
