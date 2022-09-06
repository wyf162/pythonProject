# _*_ coding: utf-8 _*_
# @Time : 2022/09/05 11:01 PM 
# @Author : yefe
# @File : 1425_constrained_subset_sum
import collections
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 存储动态规划结果的数组
        # 我们直接放入 f[0] 的值，防止处理边界情况
        f = [nums[0]] + [0] * (n - 1)
        # 单调队列
        # 一开始唯一的 j 为 0
        q = collections.deque([0])

        ans = nums[0]
        for i in range(1, n):
            # 如果队首的 j 与 i 的差值大于 k，则不满足要求，弹出
            while q and i - q[0] > k:
                q.popleft()
            # 此时队首的 j 即为最优的 j 值
            f[i] = max(f[q[0]], 0) + nums[i]
            ans = max(ans, f[i])
            # 维护队列的单调性，不断从队尾弹出元素
            while q and f[i] >= f[q[-1]]:
                q.pop()
            # 将 i 作为之后的新 j 值放入队尾
            q.append(i)
        return ans

