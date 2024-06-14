# -*- coding : utf-8 -*-
# @Time: 2024/6/14 19:49
# @Author: yefei.wang
# @File: D.py

import sys

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

tcn = I()
for _tcn_ in range(tcn):
    n, a, b = MI()
    nums = LI()
    odd = 0
    event = 0
    for i, x in enumerate(nums):
        if x % 2 == 0:
            event += 1
        else:
            odd += 1
    # print(odd, event)
    if odd == 0 or event == 0:
        if a > 0:
            ans = a * (n - 1)
        else:
            ans = a * n * (n - 1) // 2
    else:
        if 0 <= a <= b:
            ans = a * (n - 2) + b
        elif 0 <= b <= a:
            ans = b * (n - 1)
        elif a <= 0 <= b:
            ans = a * odd * (odd - 1) // 2 + a * event * (event - 1) // 2 + b
        elif b <= 0 <= a:
            ans = b * odd * event
        else:
            ans = a * odd * (odd - 1) // 2 + a * event * (event - 1) // 2 + b * odd * event
    print(ans)
