# -*- coding : utf-8 -*-
# @Time: 2023/10/5 2:11
# @Author: yefei.wang
# @File: P4995.py

import sys

sys.stdin = open('./../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()
a.sort()

ans = 0
pre = 0
l, r = 0, n - 1
odd = 1
while l <= r:
    if odd:
        ans += (a[r] - pre) * (a[r] - pre)
        pre = a[r]
        r -= 1
    else:
        ans += (a[l] - pre) * (a[l] - pre)
        pre = a[l]
        l += 1
    odd ^= 1
print(ans)
