# -*- coding : utf-8 -*-
# @Time: 2023/11/18 19:57
# @Author: yefei.wang
# @File: C.py

import sys
from collections import Counter

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
s = input()
cnt = Counter()
c = 1
cnt[s[0]] = 1
for i in range(1, n):
    if s[i] == s[i - 1]:
        c += 1
        cnt[s[i]] = max(cnt[s[i]], c)
    else:
        c = 1
        cnt[s[i]] = max(cnt[s[i]], c)
ans = 0
for k, v in cnt.items():
    ans += v
print(ans)
