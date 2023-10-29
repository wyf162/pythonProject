# -*- coding : utf-8 -*-
# @Time: 2023/10/7 20:11
# @Author: yefei.wang
# @File: c.py

import sys
from collections import Counter

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
a = LI()
ss = [input() for _ in range(n)]

s2i = [[s, i] for i, s in enumerate(a)]
s2i.sort(key=lambda x: (-x[0], x[1]))


def calc(i, s):
    score = 0
    for j in range(m):
        if s[j] == 'o':
            score += a[j]
    return score + i + 1


scores = [calc(i, s) for i, s in enumerate(ss)]
hst = Counter(scores)
mx = max(scores)
if hst[mx] == 1:
    only_one = True
else:
    only_one = False

if only_one:
    for i, s in enumerate(ss):
        if scores[i] >= mx:
            print(0)
        else:
            ans = 0
            cur = scores[i]
            i = 0
            while cur <= mx:
                j = s2i[i][1]
                if s[j] == 'x':
                    cur += a[j]
                    ans += 1

                i += 1
            print(ans)
else:
    for i, s in enumerate(ss):
        if scores[i] > mx:
            print(0)
        else:
            ans = 0
            cur = scores[i]
            i = 0
            while cur <= mx:
                j = s2i[i][1]
                if s[j] == 'x':
                    cur += a[j]
                    ans += 1
                i += 1
            print(ans)
