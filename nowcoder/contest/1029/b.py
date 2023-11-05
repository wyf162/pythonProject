# -*- coding : utf-8 -*-
# @Time: 2023/10/29 21:56
# @Author: yefei.wang
# @File: b.py

import sys

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, q = MI()
s = input()

for _ in range(q):
    l, r = MI()
    t = ''
    for i in range(len(s)):
        if l - 1 <= i <= r - 1:
            t += s[i] * 2
        else:
            t += s[i]
    s = t
print(s)
