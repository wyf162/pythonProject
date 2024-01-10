# -*- coding : utf-8 -*-
# @Time: 2023/10/21 20:50
# @Author: yefei.wang
# @File: gougou.py
import copy
import sys
from collections import Counter

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
PYL = lambda array: print(' '.join(map(str, array)))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()

    dp = [1] + [0] * 1000
    fa = [0] * 1001
    for x in a:
        ndp = copy.deepcopy(dp)
        for k in range(1000, -1, -1):
            if ndp[k] == 0 and dp[(k - x) % 1000] == 1:
                ndp[k] = 1
                fa[k] = x
        dp = ndp
        if dp[-1]:
            break
    if dp[-1] == 0:
        print(-1)
        continue

    x = sum(a) % 1000
    print(x)
    vs = []
    v = 1000
    while v:
        vs.append(fa[v])
        v = v - fa[v]
        v %= 1000

    cnt = Counter(vs)
    ans = []
    for i in range(n):
        if cnt[a[i]] > 0:
            ans.append(i + 1)
            cnt[a[i]] -= 1
    print(len(ans), end=' ')
    PYL(ans)
