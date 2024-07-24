# -*- coding : utf-8 -*-
# @Time: 2024/7/23 23:53
# @Author: yefei.wang
# @File: C.py

import sys
import math

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    mx = A[0]
    ans = 0
    for i in range(1, n):
        if A[i] == 1 and mx > A[i]:
            ans = -1
            break
    if ans == -1:
        print(ans)
        continue

    cnt = [0] * n
    for i in range(n - 1):
        f = cnt[i] + math.log2(A[i]) - math.log2(A[i + 1])
        cnt[i + 1] = max(math.ceil(f), 0)
    ans = sum(cnt)
    print(cnt)
    print(ans)
