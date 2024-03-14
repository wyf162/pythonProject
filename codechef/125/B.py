# -*- coding : utf-8 -*-
# @Time: 2024/3/13 22:35
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
    s = input()
    cnt1 = s.count('1')
    if k >= n:
        print('')
    elif k >= cnt1:
        print('0' * (n - k))
    else:
        ss = list(s)
        for i in range(n):
            if ss[i] == '1' and k > 0:
                ss[i] = '0'
                k -= 1
        print(''.join(ss))
