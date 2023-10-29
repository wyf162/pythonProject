# -*- coding : utf-8 -*-
# @Time: 2023/9/30 20:04
# @Author: yefei.wang
# @File: c.py

import math
import os
import sys
from collections import Counter, deque
from io import BytesIO, IOBase

BUFSIZE = 8192
MOD = 10 ** 9 + 7
MODD = 998244353
inf = float('inf')
sys.setrecursionlimit(10 ** 6)

sys.stdin = open('../../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
s = input()
t = input()

prefix = t[:n] == s
suffix = t[-n:] == s

if prefix and suffix:
    print(0)
elif prefix and not suffix:
    print(1)
elif not prefix and suffix:
    print(2)
else:
    print(3)
