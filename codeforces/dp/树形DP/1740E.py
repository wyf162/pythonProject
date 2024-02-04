# -*- coding : utf-8 -*-
# @Time: 2024/2/4 19:47
# @Author: yefei.wang
# @File: 1740E.py

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

n = I()
tree = [[] for _ in range(n)]
fa = LGMI()
for i, x in enumerate(fa, start=1):
    tree[x].append(i)
fa = [-1] + fa

dfs = []
stk = [0]
while len(stk):
    x = stk.pop()
    dfs.append(x)
    for y in tree[x]:
        stk.append(y)

# print(dfs)
dp = [0] * n
dep = [1] * n
for x in dfs[::-1]:
    for y in tree[x]:
        dep[x] = max(dep[x], dep[y] + 1)
    dp[x] = max(dep[x], sum(dp[y] for y in tree[x]))
print(dp[0])
