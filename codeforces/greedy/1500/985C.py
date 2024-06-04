# -*- coding: utf-8 -*-
# @Time: 2024/6/4 9:29
# @Author: yfwang
# @File: 985C.py
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

tcn = 4
for _tcn_ in range(tcn):
    n, k, L = MI()
    A = LI()
    A.sort()
    if A[n - 1] - A[0] > L:
        print(0)
        continue

    j = bisect.bisect_right(A, A[0] + L)
    B = A[:j]
    i = 0
    need = n
    ans = 0
    while i < len(B):
        ans += B[i]
        need -= 1
        cur = k - 1
        i += 1
        while i < len(B) and len(B) - i > need and cur > 0:
            i += 1
            cur -= 1
    print(ans)
