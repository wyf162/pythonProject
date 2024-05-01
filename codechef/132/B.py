# -*- coding : utf-8 -*-
# @Time: 2024/5/1 22:36
# @Author: yefei.wang
# @File: B.py

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
    n, k = MI()
    ss = [input() for _ in range(n)]
    cnt = [0] * 101
    for s in ss:
        if s.count('1') == 1:
            cnt[k - 1 - s.index('1')] = 1
    ans = 0
    for i in range(101):
        if cnt[i] == 1:
            ans |= (1 << i)
        else:
            break
    YN(2 ** k - 1 <= ans)
