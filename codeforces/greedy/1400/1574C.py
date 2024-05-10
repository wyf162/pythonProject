# -*- coding: utf-8 -*-
# @Time: 2024/5/10 15:58
# @Author: yfwang
# @File: 1574C.py
import bisect
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
mod = 1000000007
mod2 = 998244353

n = I()
A = LI()
A.sort()
tot = sum(A)
m = I()
for _ in range(m):
    x, y = MI()
    j = bisect.bisect_left(A, x)
    if j < n:
        if tot - A[j] >= y:
            print(0)
        else:
            ans = max(y - (tot - A[j]), 0)
            if j > 0:
                ans = min(ans, x - A[j - 1] + max(y - (tot - A[j - 1]), 0))
            print(ans)
    else:
        print(x - A[-1] + max(y - (tot - A[-1]), 0))
