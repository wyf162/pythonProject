# -*- coding : utf-8 -*-
# @Time: 2024/5/18 14:19
# @Author: yefei.wang
# @File: 1467B.py

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

    n += 4
    nums.insert(0, nums[0])
    nums.insert(0, nums[0])
    nums.append(nums[-1])
    nums.append(nums[-1])

    f = [0] * n
    for i in range(1, n - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            f[i] = 1
        if nums[i - 1] > nums[i] < nums[i + 1]:
            f[i] = 1

    f1 = [0] * n
    for i in range(1, n):
        f1[i] = f1[i - 1] + f[i]

    f2 = [0] * n
    for i in range(n - 2, -1, -1):
        f2[i] = f2[i + 1] + f[i]


    def g(arr):
        ret = 0
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1] or arr[i - 1] > arr[i] < arr[i + 1]:
                ret += 1
        return ret


    ans = n
    for i in range(2, n - 2):
        tot = f1[i - 2] + f2[i + 2]
        tmp = nums[i - 2:i + 3]
        tmp[2] = tmp[1]
        ret1 = g(tmp)
        tmp[2] = tmp[3]
        ret2 = g(tmp)
        tot += min(ret1, ret2)
        ans = min(ans, tot)
    print(ans)
