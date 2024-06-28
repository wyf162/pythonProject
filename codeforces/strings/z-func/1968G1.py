# -*- coding : utf-8 -*-
# @Time: 2024/5/5 21:28
# @Author: yefei.wang
# @File: 1968G1.py
# https://codeforces.com/contest/1968/problem/G1

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


def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        else:
            z[i] = max(0, r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    z[0] = n
    return z


tcn = I()
for _tcn_ in range(tcn):
    n, l, r = MI()
    s = input()
    z = z_function(s)

    def check(x):
        cnt = 0
        i = 0
        while i < n:
            if z[i] >= x:
                i += x
                cnt += 1
            else:
                i += 1
        return cnt >= l
    L = 1
    R = n // l + 1
    ans = 0
    while L <= R:
        mid = (L+R)//2
        if check(mid):
            ans = mid
            L = mid + 1
        else:
            R = mid - 1
    print(ans)
