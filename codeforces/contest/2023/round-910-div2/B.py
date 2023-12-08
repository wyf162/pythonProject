# -*- coding : utf-8 -*-
# @Time: 2023/11/19 22:47
# @Author: yefei.wang
# @File: B.py
import math
import sys

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    ans = 0
    mx = a[n - 1]
    for i in range(n - 2, -1, -1):
        if a[i] <= mx:
            mx = a[i]
        else:
            k = math.ceil(a[i] / mx)
            mx = max(1, a[i] // k)
            ans += k - 1
    print(ans)
