# -*- coding: utf-8 -*-
# @Time: 2024/5/7 13:07
# @Author: yfwang
# @File: 1129A2.py

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

tcn = 3
for _tcn_ in range(tcn):
    n, m = MI()
    to_move = [n] * n
    cnt = [0] * n

    for _ in range(m):
        u, v = GMI()
        to_move[u] = min(to_move[u], (v - u) % n)
        cnt[u] += 1

    ans = [0] * n
    cur = max((cnt[i] - 1) * n + i + to_move[i] for i in range(n) if cnt[i])
    for i in range(n):
        ans[i] = cur - i
        if cnt[i]:
            cur = max(cur, cnt[i] * n + i + to_move[i])
    print(*ans)
