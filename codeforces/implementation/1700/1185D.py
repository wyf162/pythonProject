# -*- coding: utf-8 -*-
# @Time: 2024/6/3 13:06
# @Author: yfwang
# @File: 1185D.py

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

N = int(input())
A = [int(a) for a in input().split()]
INV = {}
for i in range(N):
    INV[A[i]] = i
A = sorted(A)


def chk(k):
    X = [a for a in A]
    if k >= 0:
        del X[k]
    Y = [X[i + 1] - X[i] for i in range(len(X) - 1)]
    if max(Y) == min(Y):
        return INV[A[k]] + 1
    return -1


def solve():
    if N <= 3:
        return 1
    else:
        a = A[1] - A[0]
        b = A[2] - A[1]
        c = A[3] - A[2]

        if a == b == c:
            for i in range(len(A) - 1):
                if A[i + 1] - A[i] != a:
                    return chk(i + 1)
        return max(chk(0), chk(1), chk(2), chk(3))


print(solve())

