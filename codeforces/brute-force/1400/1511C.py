# -*- coding: utf-8 -*-
# @Time: 2024/4/29 13:53
# @Author: yfwang
# @File: 1511C.py
# https://codeforces.com/contest/1511/problem/C

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, q = MI()
nums = LI()
queries = LI()

color = []
ans = []
for query in queries:
    if query in color:
        ans.append(color.index(query))
        color.remove(query)
        color.insert(0, query)
    else:
        ans.append(len(color) + nums.index(query))
        nums.pop(nums.index(query))
        color.insert(0, query)

print(' '.join(str(x+1) for x in ans))

