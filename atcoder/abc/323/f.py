# -*- coding : utf-8 -*-
# @Time: 2023/10/7 20:53
# @Author: yefei.wang
# @File: f.py

import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

xa, ya, xb, yb, xc, yc = MI()
move = 0
if xa <= xb <= xc or xc <= xb <= xa:
    move += abs(xc - xa)
else:
    move += abs(xa - xb) + abs(xc - xb)

if ya <= yb <= yc or yc <= yb <= ya:
    move += abs(yc - ya)
else:
    move += abs(ya - yb) + abs(yc - yb) + 2

print(move)
