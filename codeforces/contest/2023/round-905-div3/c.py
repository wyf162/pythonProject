# -*- coding : utf-8 -*-
# @Time: 2023/10/22 19:19
# @Author: yefei.wang
# @File: c.py

import sys

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
YN = lambda x: print('YES' if x else 'NO')

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    a = LI()
    if k == 4:
        x2 = 0
        ans = 3 if n == 1 else 2
        for i in range(n):
            if a[i] % 4 == 0:
                ans = 0
                break
            if a[i] % 2 == 0:
                x2 += 1
            ans = min(ans, k - (a[i] % k))
        if x2 == 1:
            ans = min(ans, 1)
        elif x2 >= 2:
            ans = 0
        print(ans)
        continue

    ans = k - 1
    for i in range(n):
        x = a[i] % k
        if x == 0:
            ans = 0
            break
        else:
            ans = min(ans, k - x)
    print(ans)
