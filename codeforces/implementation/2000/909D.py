# -*- coding: utf-8 -*-
# @Time: 2024/5/17 14:10
# @Author: yfwang
# @File: 909D.py
# https://codeforces.com/problemset/problem/909/D
# simulate

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

tcn = 1
for _tcn_ in range(tcn):
    s = input()
    groups = [[]]
    for c in s:
        if not groups[-1]:
            groups[-1].append(c)
        else:
            if groups[-1][-1] == c:
                groups[-1].append(c)
            else:
                groups.append([c])
    # print(groups)

    ans = 0
    while True:
        if len(groups) <= 1:
            break
        ans += 1
        minus = [0] * len(groups)
        if groups[0][0] != groups[1][0]:
            minus[0] += 1
        for i in range(1, len(groups)-1):
            if groups[i][0] != groups[i-1][0]:
                minus[i] += 1
            if groups[i][0] != groups[i+1][0]:
                minus[i] += 1
        if groups[-1][0] != groups[-2][0]:
            minus[-1] += 1
        new_groups = []
        for i in range(len(groups)):
            for _ in range(minus[i]):
                if groups[i]:
                    groups[i].pop()
            if groups[i]:
                if not new_groups:
                    new_groups.append(groups[i])
                else:
                    if new_groups[-1][0] == groups[i][0]:
                        new_groups[-1] += groups[i]
                    else:
                        new_groups.append(groups[i])
        groups = new_groups
    print(ans)
