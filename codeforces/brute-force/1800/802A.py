# -*- coding : utf-8 -*-
# @Time: 2024/6/1 21:49
# @Author: yefei.wang
# @File: 802A.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, c = MI()
reqs = LI()

libs = set()
cost = 0
for i, req in enumerate(reqs):
    if req in libs:
        continue
    else:
        if len(libs) == c:
            k = 0
            for book in libs:
                if book not in reqs[i + 1:]:
                    libs.remove(book)
                    break
                j = reqs.index(book, i + 1)
                if j > k:
                    k = j
            else:
                # print(i+k)
                libs.remove(reqs[k])
        cost += 1
        libs.add(req)
    # print(libs)
print(cost)
