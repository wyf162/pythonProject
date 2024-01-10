# -*- coding : utf-8 -*-
# @Time: 2023/11/12 19:39
# @Author: yefei.wang
# @File: C.py

import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, k = MI()
s = input()
rst = s[:k].upper() + s[k:].lower()
print(rst)