# -*- coding: utf-8 -*-
# @Time: 2024/5/7 16:26
# @Author: yfwang
# @File: 1644E.py


import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
sys.stdout = open('../../output.txt', 'w')
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
    s = input()
    if len(set(s)) == 1:
        print(n)
        continue

    x, y = 1, 1
    cnt = 1
    for c in s:
        if c == 'R':
            y += 1
        elif c == 'D':
            x += 1
        cnt += 1

    ans = n * n - (x * y - cnt)
    if s[0] == 'R':
        ans -= (n - x)
        for i in range(1, len(s)):
            if s[i] == 'R':
                ans -= (n - x)
            else:
                break
    elif s[0] == 'D':
        ans -= (n - y)
        for i in range(1, len(s)):
            if s[i] == 'D':
                ans -= (n - y)
            else:
                break
    print(ans)
