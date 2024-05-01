# -*- coding : utf-8 -*-
# @Time: 2024/5/1 23:55
# @Author: yefei.wang
# @File: E.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    freq = LI() + [0]
    ans = [-1] * (n + 1)
    ans[0] = freq[0]
    cost = 0
    for i in range(1, n + 1):
        if freq[i - 1] == 0:
            x = i - 1
            x = x // 2
            cost += 1
            find = False
            while x > 0:
                if freq[x] > 1:
                    freq[x] -= 1
                    find = True
                    break
                else:
                    x = x // 2
                    cost += 1
            if not find:
                if freq[x] > 1:
                    freq[x] -= 1
                else:
                    break
            freq[i - 1] = 1
            ans[i] = cost + freq[i]
        else:
            ans[i] = cost + freq[i]
    print(*ans)
