# -*- coding : utf-8 -*-
# @Time: 2024/4/12 22:46
# @Author: yefei.wang
# @File: B.py

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
    n = I()
    nums = LI()
    ans = n
    cnt = 1
    for i in range(1, n):
        if nums[i] == nums[0]:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
    ans = min(ans, cnt)
    print(ans if ans < n else -1)

