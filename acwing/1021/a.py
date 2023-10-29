# -*- coding : utf-8 -*-
# @Time: 2023/10/21 19:26
# @Author: yefei.wang
# @File: a.py

import sys

# sys.stdin = open('./../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
if n < 5:
    print(1)
else:
    print(n - 5 + 1)
