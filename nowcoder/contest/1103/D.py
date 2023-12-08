# -*- coding : utf-8 -*-
# @Time: 2023/11/5 23:08
# @Author: yefei.wang
# @File: D.py
import sys

sys.stdin = open('../../input.txt')
# sys.stdout = open('./../../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    N, K = MI()
