# -*- coding: utf-8 -*-
# @Time: 2024/3/13 10:50
# @Author: yfwang
# @File: 1845C.py
# https://codeforces.com/contest/1845/problem/C

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
    s = input()
    m = I()
    a = input()
    b = input()
    z = 0
    ans = 'NO'
    for i in range(m):
        s1 = set()
        while z < len(s) and len(s1) < (int(b[i])) - int(a[i]) + 1:
            if a[i] <= s[z] <= b[i]:
                s1.add(s[z])
            z += 1
        if z == len(s) and len(s1) < int(b[i]) - int(a[i]) + 1:
            ans = 'YES'
    print(ans)
