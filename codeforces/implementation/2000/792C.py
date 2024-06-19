# -*- coding: utf-8 -*-
# @Time: 2024/6/19 13:35
# @Author: yfwang
# @File: 792C.py

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

tcn = 3
for _tcn_ in range(tcn):
    nums = [int(x) for x in input()]
    n = len(nums)
    one = []
    two = []
    for i in range(n-1, -1, -1):
        if nums[i] % 3 == 1 and len(one) < 2:
            one.append(i)
        if nums[i] % 3 == 2 and len(two) < 2:
            two.append(i)

    tot = sum(nums)
    if tot % 3 == 0:
        print(''.join(str(x) for x in nums))
    elif tot % 3 == 1:
        if len(one) >= 1:
            A = nums[:]
            A.pop(one[0])
            while len(A) > 1 and A[0] == 0:
                A.pop(0)
        else:
            A = []
        if len(two) >= 2:
            B = nums[:]
            B.pop(two[0])
            B.pop(two[1])
            while len(B) > 1 and B[0] == 0:
                B.pop(0)
        else:
            B = []
        if len(A) > len(B):
            ret = A
        else:
            ret = B
        if ret:
            print(''.join(str(x) for x in ret))
        else:
            print(-1)
    elif tot % 3 == 2:
        if len(one) >= 2:
            A = nums[:]
            A.pop(one[0])
            A.pop(one[1])
            while len(A) > 1 and A[0] == 0:
                A.pop(0)
        else:
            A = []
        if len(two) >= 1:
            B = nums[:]
            B.pop(two[0])
            while len(B) > 1 and B[0] == 0:
                B.pop(0)
        else:
            B = []
        if len(A) > len(B):
            ret = A
        else:
            ret = B
        if ret:
            print(''.join(str(x) for x in ret))
        else:
            print(-1)