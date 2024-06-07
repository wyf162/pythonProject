# -*- coding: utf-8 -*-
# @Time: 2024/6/3 9:10
# @Author: yfwang
# @File: 1873F.py

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

# money trees

tcn = I()
for _ in range(tcn):
    n, k = MI()
    a = LI()
    h = LI()

    ans = 0 if min(a) > k else 1
    left = 0
    s = a[0]
    for right in range(1, n):
        if h[right - 1] % h[right] == 0:
            s += a[right]
            while s > k:
                s -= a[left]
                left += 1
            ans = max(right - left + 1, ans)

        else:
            left = right
            s = a[left]
            while s > k:
                s -= a[left]
                left += 1
            ans = max(right - left + 1, ans)
    print(ans)
