# -*- coding : utf-8 -*-
# @Time: 2024/5/3 0:34
# @Author: yefei.wang
# @File: G1.py

import sys
from collections import defaultdict
import bisect

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
    n, l, r = MI()
    s = input()
    groups = [[] for _ in range(26)]
    for i, c in enumerate(s):
        idx = ord(c) - ord('a')
        groups[idx].append(i)
    for i in range(26):
        if len(groups[i]) >= l:
            next_groups = [[] for _ in range(26)]
            for i1 in groups[i]:
                if i1 + 1 >= n:
                    continue
                idx1 = ord(s[i1+1]) - ord('a')
                next_groups[idx1].append(i1+1)
