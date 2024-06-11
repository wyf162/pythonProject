# -*- coding : utf-8 -*-
# @Time: 2024/6/12 0:55
# @Author: yefei.wang
# @File: C.py

import sys

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
    pre_sum = 0
    st = set()
    ans = 0
    for i in range(n):
        pre_sum += A[i]
        st.add(A[i])
        if pre_sum % 2 == 0 and pre_sum // 2 in st:
            ans += 1
    print(ans)
