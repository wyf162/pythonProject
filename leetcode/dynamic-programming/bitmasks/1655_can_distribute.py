# -*- coding : utf-8 -*-
# @Time: 2022/6/19 23:39
# @Author: yefei.wang
# @File: 1655_can_distribute.py
import collections
from typing import List


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        cache = collections.Counter(nums)
        cnt = []
        for k, v in cache.items():
            cnt.append(v)

        n, m = len(cnt), len(quantity)
        ssum = [0 for _ in range(1 << m)]
        for i in range(1, (1 << m)):
            for j in range(m):  # 遍历状态的每一位
                if (i & (1 << j)) != 0:
                    left = i - (1 << j)
                    ssum[i] = ssum[left] + quantity[j]
                    break

        dp = [[False for _ in range(1 << m)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        for i in range(n):
            for j in range(1 << m):
                if i > 0 and dp[i - 1][j]:
                    dp[i][j] = True
                    continue
                s = j
                while s:
                    prev = j - s  # 前 i-1 个元素需要满足子集 prev = j-s
                    last = (prev == 0) if i == 0 else dp[i - 1][prev]  # cnt[0..i-1] 能否满足子集 prev
                    need = ssum[s] <= cnt[i]  # cnt[i] 能否满足子集 s 构造s集合的元素均相同
                    if last and need:
                        dp[i][j] = True
                        break
                    s = (s - 1) & j  # 枚举二进制子集 O(3^m)
        return dp[n - 1][(1 << m) - 1]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4]
    quantity = [2]
    ret = sol.canDistribute(nums, quantity)
    print(ret)
