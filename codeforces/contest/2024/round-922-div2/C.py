# -*- coding : utf-8 -*-
# @Time: 2024/1/30 22:47
# @Author: yefei.wang
# @File: C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
    a, b, r = MI()
    N = 60
    x = 0

    xa, xb = 0, 0
    for i in range(N, -1, -1):
        ai = (a >> i) & 1
        bi = (b >> i) & 1
        if ai == bi:
            continue
        else:
            if ai == 0 and bi == 1:
                if xa < xb:
                    if (1 << i) + x <= r:
                        xa += (1 << i)
                        x += (1 << i)
                    else:
                        xb += (1 << i)
                else:
                    xb += (1 << i)
            elif ai == 1 and bi == 0:
                if xa < xb:
                    xa += (1 << i)
                else:
                    if (1 << i) + x <= r:
                        xb += (1 << i)
                        x += (1 << i)
                    else:
                        xa += (1 << i)
    rst1 = abs(xa - xb)
    a, b = b, a
    N = 60
    x = 0

    xa, xb = 0, 0
    for i in range(N, -1, -1):
        ai = (a >> i) & 1
        bi = (b >> i) & 1
        if ai == bi:
            continue
        else:
            if ai == 0 and bi == 1:
                if xa < xb:
                    if (1 << i) + x <= r:
                        xa += (1 << i)
                        x += (1 << i)
                    else:
                        xb += (1 << i)
                else:
                    xb += (1 << i)
            elif ai == 1 and bi == 0:
                if xa < xb:
                    xa += (1 << i)
                else:
                    if (1 << i) + x <= r:
                        xb += (1 << i)
                        x += (1 << i)
                    else:
                        xa += (1 << i)
    rst2 = abs(xa - xb)
    rst = min(rst1, rst2)
    print(rst)
