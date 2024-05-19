# -*- coding : utf-8 -*-
# @Time: 2024/5/19 14:45
# @Author: yefei.wang
# @File: f_bf.py

import sys
import bisect

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
sys.stdout = open('./../../jury.txt', 'w')
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
    pre = [0] * n
    dp = []
    for x, num in enumerate(nums):
        i = bisect.bisect_left(dp, num)
        pre[x] = i
        if 0 <= i < len(dp):
            dp[i] = num
        else:
            dp.append(num)
    ceil = len(dp)
    post = [0] * n
    dp = []
    for x in range(n - 1, -1, -1):
        num = -nums[x]
        i = bisect.bisect_left(dp, num)
        post[x] = i
        if 0 <= i < len(dp):
            dp[i] = num
        else:
            dp.append(num)
    res = []
    for i in range(n):
        if pre[i] + post[i] + 1 == ceil:
            res.append(i + 1)
    print(len(res))
    print(*res)
