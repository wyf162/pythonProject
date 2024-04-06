# -*- coding : utf-8 -*-
# @Time: 2024/4/6 20:06
# @Author: yefei.wang
# @File: C.py

import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
cnt = defaultdict(list)
for _ in range(n):
    a, c = MI()
    cnt[c].append(a)

ans = 0
for k, v in cnt.items():
    ans = max(ans, min(v))
print(ans)
