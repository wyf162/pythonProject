# -*- coding: utf-8 -*-
# @Time: 2024/3/22 14:46
# @Author: yfwang
# @File: 1930C.py
# https://codeforces.com/problemset/problem/1930/C

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
sys.stdout = open('../../jury.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    ans = []
    for i, x in enumerate(nums):
        ans.append(x + i + 1)
    ans.sort(reverse=True)
    for i in range(1, n):
        if ans[i] >= ans[i - 1]:
            ans[i] = ans[i - 1] - 1
    print(*ans)
