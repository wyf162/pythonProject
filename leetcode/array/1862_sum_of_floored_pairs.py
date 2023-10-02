# _*_ coding: utf-8 _*_
# @Time : 2022/05/28 5:03 PM 
# @Author : yefe
# @File : 1862_sum_of_floored_pairs
from _ast import List


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7

        # 元素最大值
        upper = max(nums)
        cnt = [0] * (upper + 1)
        for num in nums:
            cnt[num] += 1
        # 预处理前缀和
        pre = [0] * (upper + 1)
        for i in range(1, upper + 1):
            pre[i] = pre[i - 1] + cnt[i]

        ans = 0
        for y in range(1, upper + 1):
            # 一个小优化，如果数组中没有 y 可以跳过
            if cnt[y]:
                d = 1
                while d * y <= upper:
                    ans += cnt[y] * d * (pre[min((d + 1) * y - 1, upper)] - pre[d * y - 1])
                    d += 1
        return ans % mod

