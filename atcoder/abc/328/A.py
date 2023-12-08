# -*- coding : utf-8 -*-
# @Time: 2023/11/11 20:01
# @Author: yefei.wang
# @File: C.py

import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))


n, x = MI()
a = LI()
rst = 0
for i in range(n):
    if a[i]<=x:
        rst += a[i]
print(rst)