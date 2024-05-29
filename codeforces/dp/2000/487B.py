# -*- coding : utf-8 -*-
# @Time: 2024/5/29 20:05
# @Author: yefei.wang
# @File: 487b.py
# ST表 two points DP


import sys
from typing import List, Callable
from math import log2

input = lambda: sys.stdin.readline().strip()
inf = float('inf')


class SparseTable:
    def __init__(self, nums: List[int], merge_func: Callable[[int, int], int]) -> None:
        # merge_func: max, min

        n = len(nums)
        k = int(log2(n)) + 1

        self.merge_func = merge_func

        # st[i][j]: 长度为 2^j 的子数组 nums[i, i + 2^j - 1] 上的最值
        # 将长度为 2^j 的子数组 nums[i, i + 2^j - 1]
        # 划分为两个长度为 2^(j -1) 的子数组：
        # nums[i, i + 2^(j - 1) - 1],
        # nums[i + 2^(j - 1), 2 ^ j - 1]
        # 则有区间最值等于两个小区间最值的最值，即：
        # max(nums[i, i + 2^j - 1]) = max(
        #   max(nums[i, i + 2^(j - 1) - 1]),
        #   max(nums[i + 2^(j - 1), 2^j - 1])
        # )
        # min(nums[i, i + 2^j - 1]) = min(
        #   min(nums[i, i + 2^(j - 1) - 1]),
        #   min(nums[i + 2^(j - 1), 2^j - 1])
        # )
        self.st = [[0] * k for _ in range(n)]
        for i in range(n):
            self.st[i][0] = nums[i]

        for j in range(1, k):
            for i in range(n - (1 << j) + 1):
                self.st[i][j] = self.merge_func(
                    self.st[i][j - 1],
                    self.st[i + (1 << (j - 1))][j - 1]
                )

    def query(self, left: int, right: int) -> int:
        # 将区间 [left, right] 划分为两个长度为 2^k 的重叠区间：
        # [left, left + 2^k - 1] 和 [right - 2^k + 1, right]
        # 区间 [left, right] 上的最值，即为两个重叠区间上最值的最值，即：
        # max(nums[left, right]) = max(
        #   max(nums[left, left + 2^k - 1]),
        #   max(nums[right - 2^k + 1, right])
        # )
        # min(nums[left, right]) = min(
        #   min(nums[left, left + 2^k - 1]),
        #   min(nums[right - 2^k + 1, right])
        # )

        k = int(log2(right - left + 1))
        return self.merge_func(
            self.st[left][k],
            self.st[right - (1 << k) + 1][k]
        )


n, s, L = map(int, input().split())
a = list(map(int, input().split()))

st_max = SparseTable(a, max)
st_min = SparseTable(a, min)


def isValid(left, right):
    return st_max.query(left, right) - st_min.query(left, right) <= s


f = [inf] * (n + 1)  # f[i]: 分割前i个数的最小段数
pre = -1  # 上一个分段的右端点
f[0] = 0
for i in range(L - 1, n):
    while i - pre >= L and (not isValid(pre + 1, i) or f[pre + 1] == inf):
        pre += 1
    if i - pre >= L:
        f[i + 1] = min(f[i + 1], f[pre + 1] + 1)
print(-1 if f[n] == inf else f[n])
