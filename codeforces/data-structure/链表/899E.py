# -*- coding: utf-8 -*-
# @Time: 2024/7/4 11:22
# @Author: yfwang
# @File: 899E.py

import sys
from heapq import heappop, heappush, heapify

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 1
for _tcn_ in range(tcn):
    n = I()
    nums = LI()

    vals = []
    cnts = []
    last_val = 0
    cnt = 0

    for num in nums:
        if num != last_val:
            if cnt:
                vals.append(last_val)
                cnts.append(cnt)
            last_val = num
            cnt = 1
        else:
            cnt += 1

    vals.append(last_val)
    cnts.append(cnt)
    k = len(vals)
    pre = list(range(-1, k - 1))
    nex = list(range(1, k + 1))


    def delete(x):
        cnts[x] = 0
        if pre[x] >= 0:
            nex[pre[x]] = nex[x]
        if nex[x] < k:
            pre[nex[x]] = pre[x]


    h = [(-cnts[i], i) for i in range(k)]
    heapify(h)
    ans = 0
    while h:
        c, i = heappop(h)
        if -cnts[i] != c:
            continue
        ans += 1
        if pre[i] >= 0 and nex[i] < k and vals[pre[i]] == vals[nex[i]]:
            cnts[pre[i]] += cnts[nex[i]]
            delete(nex[i])
            heappush(h, (-cnts[pre[i]], pre[i]))
        delete(i)
    print(ans)
