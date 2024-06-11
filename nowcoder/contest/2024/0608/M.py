# -*- coding: utf-8 -*-
# @Time: 2024/6/11 13:14
# @Author: yfwang
# @File: M.py

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

n = I()
nums = LI()

nums.sort()
for i in range(n):
    nums[i] -= 2 * i

nums.sort()


def f():
    ret = 0
    d = nums[mid]
    for i in range(n):
        ret += abs(nums[i] - d) // 2
        if abs(nums[i] - d) % 2:
            ret += 100
    return ret


mid = n // 2
ans = 10 ** 18
nums[mid] -= 1
for i in range(3):
    ans = min(ans, f() + (100 if i % 2 == 0 else 0))
    nums[mid] += 1
print(ans)
