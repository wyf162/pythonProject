# -*- coding: utf-8 -*-
# @Time: 2024/5/10 16:47
# @Author: yfwang
# @File: 1574D.py

import sys
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


def f1(nums):
    x = 0
    for i in reversed(range(n)):
        x *= N
        x += nums[i]
    return x


def f2(x):
    nums = []
    for _ in range(n):
        nums.append(x % N)
        x //= N
    return nums


def get_sum(nums):
    return sum(A[i][nums[i]] for i in range(n))


tcn = 4
for _tcn_ in range(tcn):
    n = I()
    A = [LI() for _ in range(n)]
    N = max(len(a) for a in A) + 5
    m = I()
    B = [LI() for _ in range(m)]
    st = set()
    for b in B:
        x = f1(b)
        st.add(x)

    cur = f1([a[0] for a in A])
    h = []
    heappush(h, (-get_sum(f2(cur)), cur))

    while True:
        val, cur = heappop(h)
        if cur not in st:
            ans = f2(cur)
            break
        else:
            nums = f2(cur)
            for i in range(n):
                if nums[i] > 1:
                    nums[i] -= 1
                    heappush(h, (-get_sum(nums), f1(nums)))
                    nums[i] += 1

    print(*ans)
