# -*- coding : utf-8 -*-
# @Time: 2024/4/13 23:20
# @Author: yefei.wang
# @File: D.py

import sys
from itertools import accumulate
from types import GeneratorType


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
A = LI()

DP = [0] * (n + 1)
FROM = [-1] * (n + 1)

for i in range(n):

    if DP[i + 1] < DP[i] + A[i]:
        DP[i + 1] = DP[i] + A[i]
        FROM[i + 1] = i

    for to in range(i, n):
        l = to - i + 1
        if DP[to + 1] < DP[i] + l * l:
            DP[to + 1] = DP[i] + l * l
            FROM[to + 1] = i


def all(l, r, x):
    # print("?",(l,r,x))
    k = 1
    for i in range(r - 1, l, -1):
        if x - k >= 0:
            all(l, i, x - k)
            k += 1
        else:
            break

    # print("!!",(l+1,r))

    if x == 0:
        if r - l == 1 and A[l] == 0:
            pass
        else:
            LIST.append((l + 1, r))
            A[l] = 0
    else:
        LIST.append((l + 1, r))
        A[l] = x


LIST = []
ANS = DP[-1]

ind = n
while ind > 0:
    x = FROM[ind]
    if x == ind - 1:
        if A[x] >= 1:
            pass
        else:
            LIST.append((x + 1, ind))
    else:
        # print("!",(x,ind,ind-x))
        if A[x] == 0:
            LIST.append((x + 1, ind))
            LIST.append((x + 1, ind))
        else:
            LIST.append((x + 1, ind))
        A[x] = 0

        # print(LIST)

        for kr in range(ind, x, -1):
            # print("!!!",(x,kr,kr-x-1))
            all(x, kr, kr - x - 1)
        LIST.append((x + 1, ind))

    ind = x

print(ANS, len(LIST))
for x, y in LIST:
    print(x, y)
