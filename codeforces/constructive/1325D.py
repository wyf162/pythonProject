# -*- coding : utf-8 -*-
# @Time: 2023/10/12 0:20
# @Author: yefei.wang
# @File: 1325D.py

import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

xor, tot = MI()
if (tot - xor) % 2:
    print(-1)
elif xor > tot:
    print(-1)
elif xor == tot:
    if xor:
        print(1)
        print(xor)
    else:
        print(0)
else:
    v = (tot - xor) // 2
    if v & xor == 0:
        print(2)
        print(v + xor, v)
    else:
        print(3)
        print(xor, v, v)
