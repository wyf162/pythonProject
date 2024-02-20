# -*- coding : utf-8 -*-
# @Time: 2024/2/20 20:03
# @Author: yefei.wang
# @File: 1921E.py
# https://codeforces.com/problemset/problem/1921/E

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
    h, w, xa, ya, xb, yb = MI()
    if xa < xb:
        dx = xb - xa
        if dx % 2 == 1:
            if abs(ya - yb) <= 1:
                print('Alice')
            elif ya < yb:
                if w - ya <= (dx + 1) // 2:
                    print('Alice')
                else:
                    print('Draw')
            else:
                if ya - 1 <= (dx + 1) // 2:
                    print('Alice')
                else:
                    print('Draw')
        else:
            if abs(ya - yb) < 1:
                print('Bob')
            elif ya < yb:
                if yb - 1 <= dx // 2:
                    print('Bob')
                else:
                    print('Draw')
            else:
                if w - yb <= dx // 2:
                    print('Bob')
                else:
                    print('Draw')

    else:
        print('Draw')
