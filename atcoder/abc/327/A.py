# -*- coding : utf-8 -*-
# @Time: 2023/11/4 19:59
# @Author: yefei.wang
# @File: A.py
import sys

# sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))


n = I()
s = input()
if 'ab' in s or 'ba' in s:
    print('Yes')
else:
    print('No')