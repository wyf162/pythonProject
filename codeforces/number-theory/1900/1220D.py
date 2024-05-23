# -*- coding: utf-8 -*-
# @Time: 2024/4/1 10:29
# @Author: yfwang
# @File: 1220D.py

import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
nums = LI()
cnt = Counter()
for v in nums:
    cnt[v & -v] += 1

msk = cnt.most_common()[0][0]
chosen = []
for v in nums:
    if v & -v != msk:
        chosen.append(v)

print(len(chosen))
print(' '.join(map(str, chosen)))
