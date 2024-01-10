# -*- coding : utf-8 -*-
# @Time: 2023/12/1 20:10
# @Author: yefei.wang
# @File: E.py

import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    gems = []
    magic_gems = []
