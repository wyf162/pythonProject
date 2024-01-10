# -*- coding : utf-8 -*-
# @Time: 2023/10/21 16:37
# @Author: yefei.wang
# @File: mex_gcd.py
import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()


def mex(nums):
    rst = 0
    for num in sorted(nums):
        if num == rst:
            rst += 1
    return rst


mex_a = mex(a)
if mex_a == 1:
    ans = 0
else:
    ans = mex_a

for i in range(n):
    if a[i] == 0:
        ans = max(ans, a[max(i - 1, 0)], a[min(i + 1, n - 1)])
print(ans)
