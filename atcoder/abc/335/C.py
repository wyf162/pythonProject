# -*- coding : utf-8 -*-
# @Time: 2024/1/6 20:04
# @Author: yefei.wang
# @File: C.py

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
dq = [[i + 1, 0] for i in range(n)]
hi = 0
for _ in range(q):
    op, c = input().split()
    if op == '1':
        x, y = dq[hi]
        if c == 'U':
            y += 1
        elif c == 'D':
            y -= 1
        elif c == 'R':
            x += 1
        elif c == 'L':
            x -= 1
        ti = (hi - 1) % n
        dq[ti][0], dq[ti][1] = x, y
        hi = ti
    elif op == '2':
        i = (int(c) - 1 + hi) % n
        print(*dq[i])
