# -*- coding : utf-8 -*-
# @Time: 2023/9/30 20:18
# @Author: yefei.wang
# @File: d.py

import sys
sys.stdin = open('../../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
a = LI()