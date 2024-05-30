# -*- coding : utf-8 -*-
# @Time: 2024/5/31 6:42
# @Author: yefei.wang
# @File: 1194D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
sys.stdout = open('../output.txt', 'w')

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
    n, k = MI()
    if k % 3:
        print('Alice' if n % 3 else 'Bob')
    else:
        v = n % (k + 1)
        print('Alice' if v % 3 or v == k else 'Bob')

    # def dfs(n):
    #     if n in (1, 2, k):
    #         return True
    #     ret = False
    #     if n - 1 >= 0:
    #         ret |= not dfs(n - 1)
    #     if n - 2 >= 0:
    #         ret |= not dfs(n - 2)
    #     if n - k >= 0:
    #         ret |= not dfs(n - k)
    #     return ret
    #
    #
    # ans = dfs(n)
    # print(ans)
