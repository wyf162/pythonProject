# -*- coding : utf-8 -*-
# @Time: 2024/5/11 21:41
# @Author: yefei.wang
# @File: 1620C.py
# tree
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
mod = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, k, x = MI()
    s = input()
    groups = [0]
    for c in s:
        if c == 'a':
            if groups[-1] <= 0:
                groups[-1] -= 1
            else:
                groups.append(-1)
        elif c == '*':
            if groups[-1] >= 0:
                groups[-1] += 1
            else:
                groups.append(1)
    # print(groups)

    nums = [x * k + 1 for x in groups if x > 0]
    m = len(nums)
    prod = [1] * (m + 1)
    for i in range(m - 1, -1, -1):
        prod[i] = nums[i] * prod[i + 1]
    # print(prod)

    ans = [0] * m
    for i in range(m):
        for j in range(nums[i]):
            if (j + 1) * prod[i + 1] < x:
                continue
            else:
                ans[i] = j
                x -= j * prod[i + 1]
                break

    i1 = 0
    for i, x in enumerate(groups):
        if x > 0:
            groups[i] = ans[i1]
            i1 += 1
    # print(groups)
    rets = ''
    for i, x in enumerate(groups):
        if x > 0:
            rets += 'b' * x
        else:
            rets += 'a' * abs(x)
    print(rets)
