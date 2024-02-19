# -*- coding : utf-8 -*-
# @Time: 2024/2/19 22:51
# @Author: yefei.wang
# @File: D.py

import sys
from collections import Counter

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
z = 2 ** 31 - 1
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    cnt = Counter()
    ans = 0
    for x in nums:
        if cnt[x]:
            cnt[x] -= 1
            continue
        y = x ^ z
        cnt[y] += 1
        ans += 1
    print(ans)
