# -*- coding : utf-8 -*-
# @Time: 2023/9/23 20:21
# @Author: yefei.wang
# @File: c.py
# import sys
# sys.stdin = open('../input.txt', 'r')

x = input()
s = list(map(int, list(x)))
ans = True
for i in range(1, len(s)):
    if s[i - 1] > s[i]:
        continue
    else:
        ans = False
        break
if ans:
    print('Yes')
else:
    print('No')
