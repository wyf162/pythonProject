# -*- coding : utf-8 -*-
# @Time: 2024/5/1 14:43
# @Author: yefei.wang
# @File: 386C.py
# https://codeforces.com/problemset/problem/386/C

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')

s = input()
n = len(s)

d = len(set(s))
ans = [0] * (d + 1)
ans[0] = d
last_idx = [-1] * 27

for end in range(n):
    last_idx[ord(s[end]) - ord('a')] = end
    tmp = last_idx.copy()
    tmp.sort(reverse=True)
    d = 0
    for i in range(26):
        if tmp[i] == -1:
            break
        d += 1
        ans[d] += tmp[i] - tmp[i + 1]
print(*ans, sep='\n')
