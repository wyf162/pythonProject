# -*- coding : utf-8 -*-
# @Time: 2024/5/1 22:52
# @Author: yefei.wang
# @File: C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    n = I()
    A = LI()
    nums = []
    cur = 0
    for a in A:
        if a % 2:
            cur += 1
        else:
            if cur:
                nums.append(cur)
                cur = 0
    if cur:
        nums.append(cur)
    ans = n * (n + 1) // 2
    if nums:
        nums.sort()
        x = nums.pop()
        x -= 1
        x1 = x // 2
        x2 = x - x1
        nums.append(x1)
        nums.append(x2)
        for x in nums:
            ans -= x * (x + 1) // 2
    print(ans)
