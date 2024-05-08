# -*- coding : utf-8 -*-
# @Time: 2024/5/8 22:44
# @Author: yefei.wang
# @File: C.py

import sys
from itertools import accumulate

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
    N = I()
    S = input()
    ss = S.split('b')
    A = []
    C = []
    for s in ss:
        if s:
            A.append(s.count('a'))
            C.append(s.count('c'))
    if len(A) <= 1:
        print(0)
        continue
    A.pop()
    C.pop(0)
    # print(A)
    # print(C)
    ans = min(sum(A), sum(C))
    PA = list(accumulate(A, initial=0))
    PC = list(accumulate(C, initial=0))
    for i in range(len(A) + 1):
        ans = min(ans, PA[i] + PC[-1] - PC[i])
    print(ans)
