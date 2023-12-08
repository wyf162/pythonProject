# -*- coding : utf-8 -*-
# @Time: 2023/11/17 22:40
# @Author: yefei.wang
# @File: B.py
import sys

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    pre_sum = [0] * (n + 1)
    for i in range(n):
        pre_sum[i + 1] = pre_sum[i] + a[i]

    mx, mi = max(a), min(a)
    ans = mx - mi
    for k in range(2, n + 1):
        b = []
        if n % k == 0:
            for i in range(0, n, k):
                b.append(pre_sum[i + k] - pre_sum[i])
            mx, mi = max(b), min(b)
            ans = max(ans, mx - mi)
    print(ans)
