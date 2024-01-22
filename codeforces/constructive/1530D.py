# -*- coding : utf-8 -*-
# @Time: 2024/1/22 19:45
# @Author: yefei.wang
# @File: 1540D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    n = I()
    a = LI()
    cnt, b, tmp = [0] * (n + 1), [], 0
    for i in range(n):
        cnt[a[i]] += 1
    rem = [i for i in range(1, n + 1) if cnt[i] == 0]
    for i in range(n):
        if cnt[a[i]] > 1 and rem and rem[-1] != i + 1:
            b.append(rem.pop())
            cnt[a[i]] -= 1
        else:
            b.append(a[i])
            tmp += 1
    print(tmp)
    print(*b)
