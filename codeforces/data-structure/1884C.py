# -*- coding: utf-8 -*-
# @Time: 2024/2/26 11:16
# @Author: yfwang
# @File: 1884C.py
# https://codeforces.com/problemset/problem/1884/C
import bisect
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
    n, m = MI()
    ops = [LI() for _ in range(n)]
    st = {1, m}
    for op in ops:
        l, r = op
        st.add(l)
        st.add(r)
    st = sorted(list(st))
    s1 = [0] * (len(st) + 1)
    s2 = [0] * (len(st) + 1)

    for op in ops:
        p1 = bisect.bisect_left(st, op[0])
        p2 = bisect.bisect_left(st, op[1])
        if op[0] > 1:
            s2[p1] += 1
            s2[p2 + 1] -= 1
        if op[1] < m:
            s1[p1] += 1
            s1[p2 + 1] -= 1
    for i in range(1, len(s1)):
        s1[i] += s1[i - 1]
        s2[i] += s2[i - 1]
    print(max(s1 + s2))
