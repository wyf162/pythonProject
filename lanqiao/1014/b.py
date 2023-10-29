# -*- coding : utf-8 -*-
# @Time: 2023/10/14 19:07
# @Author: yefei.wang
# @File: c.py

import os
import sys

# 请在此输入您的代码
from collections import Counter
sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, q = MI()
for _ in range(q):
    s = input()
    i = 1
    for c in s:
        if c=='L':
            i = i*2-1
        else:
            i = i*2
    print(i)




