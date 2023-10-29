# -*- coding : utf-8 -*-
# @Time: 2023/10/7 20:01
# @Author: yefei.wang
# @File: c.py
import sys
sys.stdin = open('../../input.txt', 'r')
s = input()

ans = True
for i in range(1, 16, 2):
    if s[i] == '0':
        continue
    else:
        ans = False
if ans:
    print('Yes')
else:
    print('No')