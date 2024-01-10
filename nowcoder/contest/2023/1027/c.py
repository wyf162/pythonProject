# -*- coding : utf-8 -*-
# @Time: 2023/10/28 9:52
# @Author: yefei.wang
# @File: c.py
import sys
from collections import Counter

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m, k = MI()
a = LI()
cnt = Counter(a)

ans = [0] * m

for i in range(1, m + 1):
    if cnt[i] + k > n:
        ans[i - 1] = -1
        continue
    if cnt[i] + k == n:
        ans[i - 1] = 0
        continue

    l, r = 0, n
    while l <= r:
        mid = (l + r) // 2
        s = 0
        for j, v in cnt.items():
            if j == i:
                continue
            if v > mid:
                s += v - mid
        # s += m - 2
        if s <= k:
            ans[i - 1] = mid
            r = mid - 1
        else:
            l = mid + 1

print(' '.join(map(str, ans)))
