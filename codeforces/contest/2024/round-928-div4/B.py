# -*- coding : utf-8 -*-
# @Time: 2024/2/19 22:39
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
    n = I()
    st = []
    for _ in range(n):
        x = input().count('1')
        if x:
            st.append(x)
    if st[0] == st[-1]:
        print('SQUARE')
    else:
        print('TRIANGLE')
