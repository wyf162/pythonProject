# -*- coding : utf-8 -*-
# @Time: 2023/10/11 19:34
# @Author: yefei.wang
# @File: 486C.py

import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, p = MI()
p -= 1
s = input()
i, j = 0, n - 1
idxs = []
ans = 0
while i < j:
    if s[i] != s[j]:
        dis = abs(ord(s[i]) - ord(s[j]))
        ans += min(dis, 26 - dis)
        idxs.append(i)
    i += 1
    j -= 1

if not idxs:
    print(ans)
    exit(0)

t = n - 1

if p >= n // 2:
    p = n - p - 1

if len(idxs) == 1:
    t = min(t, abs(p - idxs[0]))
else:
    if p <= idxs[0]:
        t = min(t, idxs[-1] - p)
    elif p >= idxs[-1]:
        t = min(t, p - idxs[0])
    else:
        t = min(t, (p - idxs[0]) + idxs[-1] - idxs[0], (idxs[-1] - p) + idxs[-1] - idxs[0])

ans += t
print(ans)
