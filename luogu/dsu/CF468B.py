# -*- coding : utf-8 -*-
# @Time: 2023/10/26 22:52
# @Author: yefei.wang
# @File: CF468B.py

import sys
from heapq import heappop, heappush

sys.stdin = open('./../../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))