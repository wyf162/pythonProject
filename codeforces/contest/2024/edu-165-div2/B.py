# -*- coding : utf-8 -*-
# @Time: 2024/4/29 22:48
# @Author: yefei.wang
# @File: B.py

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
    s = input()
    n = len(s)
    ans = 0
    one = 0
    for i in range(0, n, 1):
        if s[i] == '1':
            one += 1
        else:
            if one:
                ans += one + 1
    print(ans)
