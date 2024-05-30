# -*- coding : utf-8 -*-
# @Time: 2024/5/29 21:35
# @Author: yefei.wang
# @File: 1513D.py
# mst gcd

import sys
import math

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, p = MI()
    a = LI()
    xi = [(x, i) for i, x in enumerate(a)]
    xi.sort()
    vis = [0] * n

    ans = 0
    rest = n - 1
    for x, i in xi:
        if x >= p:
            break
        if vis[i]:
            continue

        l = i - 1
        while l >= 0:
            if math.gcd(a[l], a[i]) == a[i] and not vis[l]:
                l -= 1
            else:
                break
        r = i + 1
        while r < n:
            if math.gcd(a[r], a[i]) == a[i] and not vis[r]:
                r += 1
            else:
                break
        vis[i] = 1
        for j in range(l + 2, r - 1):
            vis[j] = 1

        rest -= (r - l - 2)
        ans += (r - l - 2) * x
    ans += p * rest
    print(ans)
