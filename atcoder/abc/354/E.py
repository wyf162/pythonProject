# -*- coding : utf-8 -*-
# @Time: 2024/5/18 20:19
# @Author: yefei.wang
# @File: E.py

import sys
from functools import lru_cache
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
A = []
B = []
for i in range(n):
    a, b = MI()
    A.append(a)
    B.append(b)
mtx = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if A[i] == A[j] or B[i] == B[j]:
            mtx[i][j] = mtx[j][i] = True


@lru_cache(None)
def dfs(state):
    # print(bin(state))
    bits = []
    for b in range(n):
        if state >> b & 1:
            continue
        bits.append(b)
    # print(bits)
    ret = False
    for i1, i2 in combinations(bits, 2):
        if mtx[i1][i2]:
            ret = ret or (not dfs(state | (1 << i1) | (1 << i2)))
            if ret:
                return ret
    return ret


ans = dfs(0)
if ans:
    print('Takahashi')
else:
    print('Aoki')
