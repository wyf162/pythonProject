# -*- coding : utf-8 -*-
# @Time: 2023/10/21 19:27
# @Author: yefei.wang
# @File: b.py

import sys

sys.stdin = open('./../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
s = input()
t = input()

mx = n
ans = list(range(1, n+1))

for i in range(m-n+1):
    diff = []
    for j in range(n):
        if s[j] != t[i+j]:
            diff.append(j+1)
    if len(diff) < mx:
        ans = diff
        mx = len(ans)

print(mx)
if mx:
    print(' '.join(map(str, ans)))

