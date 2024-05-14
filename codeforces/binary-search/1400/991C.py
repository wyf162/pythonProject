# -*- coding: utf-8 -*-
# @Time: 2024/5/7 9:07
# @Author: yfwang
# @File: 991C.py
# https://codeforces.com/problemset/problem/991/C

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

N = I()


def check(n, k):
    cnt = k
    n -= k
    while n >= 10:
        n -= n // 10
        cnt += k
        n -= k
    cnt += n
    return cnt


L = 1
R = N
ans = N
while L <= R:
    mid = (L + R) // 2
    if check(N, mid) * 2 >= N:
        ans = mid
        R = mid - 1
    else:
        L = mid + 1

print(ans)
