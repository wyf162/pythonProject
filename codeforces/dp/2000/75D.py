# -*- coding: utf-8 -*-
# @Time: 2024/6/19 15:13
# @Author: yfwang
# @File: 75D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
inf = 10 ** 18


def get_mx_pre_pos(nums):
    tot = sum(nums)
    pre = -inf
    suf = -inf
    cur = 0
    for x in nums:
        cur += x
        pre = max(pre, cur)
        suf = max(suf, tot - cur)

    cur = 0
    mx = -inf
    for x in nums:
        cur += x
        mx = max(mx, cur)
        cur = max(cur, 0)
    return pre, suf, tot, mx


n, m = MI()
arrs = [LI()[1:] for _ in range(n)]
seq = LGMI()
prefix = []
suffix = []
totals = []
mxs = []
for arr in arrs:
    pre, suf, tot, mx = get_mx_pre_pos(arr)
    prefix.append(pre)
    suffix.append(suf)
    totals.append(tot)
    mxs.append(mx)

ans = -inf
cur = 0
for i, r in enumerate(seq):
    if i >= 1:
        cur = max(cur, suffix[seq[i - 1]], 0)
    ans = max(ans, cur + prefix[r], mxs[r])
    cur += totals[r]

print(ans)
