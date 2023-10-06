# -*- coding : utf-8 -*-
# @Time: 2023/10/2 14:01
# @Author: yefei.wang
# @File: a.py

import sys
# sys.stdin = open('./input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
ss = [input() for _ in range(n)]
ans = []
for i in range(n):
    if ss[i] == 'AC':
        continue
    else:
        ans.append(i+1)
print(' '.join(map(str, ans)))
