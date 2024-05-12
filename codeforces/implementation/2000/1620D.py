# -*- coding : utf-8 -*-
# @Time: 2024/5/11 23:31
# @Author: yefei.wang
# @File: 1620D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
sys.stdout = open('../../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    x0 = x1 = x2 = -1
    have_one = False
    for num in nums:
        if num % 3 == 0:
            x0 = max(x0, num // 3)
        elif num % 3 == 1:
            x1 = max(x1, num // 3)
            if num == 1:
                have_one = True
        elif num % 3 == 2:
            x2 = max(x2, num // 3)
    # print(x0, x1, x2)
    if x0 >= 0 and x1 >= 0 and x2 >= 0:
        # 3 1 2
        ans1 = max(x0 - 1, x1, x2) + 2
        # 3 2 2
        ans2 = max(x0, x1 - 1, x2) + 2 + int(have_one)
        # 3 1 1
        ans3 = max(x0, x1, x2) + 2
        ans = min(ans1, ans2, ans3)
    elif x0 >= 0 and x1 >= 0:
        ans = max(x0, x1) + 1
    elif x0 >= 0 and x2 >= 0:
        ans = max(x0, x2) + 1
    elif x1 >= 0 and x2 >= 0:
        # 3 1 2
        ans1 = max(x1, x2) + 2
        # 3 2 2
        ans2 = max(x1 - 1, x2) + 2 + int(have_one)
        # 3 1 1
        ans3 = max(x1, x2) + 2
        ans = min(ans1, ans2, ans3)
    elif x0 >= 0:
        ans = x0
    elif x1 >= 0:
        ans = x1 + 1
    elif x2 >= 0:
        ans = x2 + 1
    else:
        ans = 0

    print(ans)
