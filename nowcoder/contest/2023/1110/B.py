# -*- coding : utf-8 -*-
# @Time: 2023/11/10 19:08
# @Author: yefei.wang
# @File: B.py

import math
import sys
from collections import Counter

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, k = MI()
a = LI()
ans = 0
cnt = Counter()
for i in range(n):
    c = math.gcd(a[i], k)
    cnt[c] += 1
# print(cnt)

ans = 0
for k1, v1 in cnt.items():
    for k2, v2 in cnt.items():
        ans += (v1 * v2) * (math.gcd(k1 * k2, k) // k1)

print(ans)
