# -*- coding: utf-8 -*-
# @Time: 2024/7/18 9:19
# @Author: yfwang
# @File: 1167E.py

import sys
from pyrival.data_structures.SegmentTree import SegmentTree
from pyrival.data_structures.SortedList import SortedList

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 10 ** 6

tcn = 1
for _tcn_ in range(tcn):
    n, x = MI()
    A = LI()

