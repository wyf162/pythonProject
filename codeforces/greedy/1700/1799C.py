# -*- coding : utf-8 -*-
# @Time: 2024/3/24 21:35
# @Author: yefei.wang
# @File: 1799C.py

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

tcn = I()
for _tnc_ in range(tcn):
    s = list(input())
    n = len(s)
    ans = [''] * n
    c = sorted(s, reverse=True)
    for i in range(n // 2):
        if c[-1] == c[-2]:
            ans[i] = c[-2]
            ans[n - 1 - i] = c[-1]
            c.pop()
            c.pop()
        else:
            if c[0] == c[-2]:
                r = c.pop()
                j = i
                while len(c) >= 2:
                    ans[j] = c.pop()
                    ans[n - 1 - j] = c.pop()
                    j += 1
                if len(c) == 0:
                    ans[j] = r
                else:
                    ans[j] = c.pop()
                    ans[j + 1] = r
                break
            else:
                ans[i] = c[-2]
                ans[n - 1 - i] = c[-1]
                c.pop()
                c.pop()
                break
    ind = 0
    for i in range(n):
        if not ans[i]:
            ans[i] = c.pop()
    print("".join(ans))
