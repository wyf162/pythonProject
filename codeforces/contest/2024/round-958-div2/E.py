# -*- coding : utf-8 -*-
# @Time: 2024/7/15 23:12
# @Author: yefei.wang
# @File: E.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    arr = LI()

    # prev smaller
    left_bound = [-1] * n
    stk = []
    for i in range(n):
        while stk and arr[stk[-1]] >= arr[i]:
            stk.pop()
        if stk:
            left_bound[i] = stk[-1]
        stk.append(i)
    print(left_bound)

    # next smaller
    right_bound = [n] * n
    stk = []
    for i in range(n - 1, -1, -1):
        while stk and arr[stk[-1]] > arr[i]:
            stk.pop()
        if stk:
            right_bound[i] = stk[-1]
        stk.append(i)
    print(right_bound)
    ans = 0
    for i in range(1, n):
        a, b = max(0, left_bound[i]), right_bound[i]
        ans += (i - a) * (b - i) * arr[i]

    print(ans)
