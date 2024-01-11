# -*- coding : utf-8 -*-
# @Time: 2024/1/10 20:33
# @Author: yefei.wang
# @File: 1671D.py
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
    n, x = MI()
    A = LI()
    mi = min(A)
    mx = max(A)
    ans = 0
    for i in range(1, n):
        ans += abs(A[i] - A[i - 1])


    def func(x):
        res = min(abs(A[0] - x), abs(A[-1] - x))
        for i in range(1, n):
            res = min(res, abs(A[i] - x) + abs(A[i - 1] - x) - abs(A[i] - A[i - 1]))
        return res


    if mi > 1:
        ans += func(1)
    if mx < x:
        ans += func(x)
    print(ans)
