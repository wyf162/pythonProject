# -*- coding : utf-8 -*-
# @Time: 2024/5/19 15:57
# @Author: yefei.wang
# @File: 1661C.py

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


def get(x1, x2):
    L, R = 0, 10 ** 15
    ans = R
    while L <= R:
        mid = (L + R) // 2
        y1 = (mid+1) // 2
        y2 = mid // 2
        if y1 < x1:
            L = mid + 1
        else:
            y2 += (y1 - x1) // 2
            if y2 < x2:
                L = mid + 1
            else:
                ans = mid
                R = mid - 1
    return ans


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    heights = LI()
    mx = max(heights)
    one, two = 0, 0
    for height in heights:
        diff = mx - height
        one += diff % 2
        two += diff // 2
    ans1 = get(one, two)

    one, two = 0, 0
    for height in heights:
        diff = mx - height + 1
        one += diff % 2
        two += diff // 2
    ans2 = get(one, two)
    ans = min(ans1, ans2)
    print(ans)
