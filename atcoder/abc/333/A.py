# -*- coding : utf-8 -*-
# @Time: 2023/12/16 19:59
# @Author: yefei.wang
# @File: A.py

import sys

sys.stdin = open('./../../input.txt')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = input()
print(n*int(n))