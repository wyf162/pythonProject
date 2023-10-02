# _*_ coding: utf-8 _*_
# @Time : 2022/11/06 8:39 PM 
# @Author : yefe
# @File : 6230_maximum_subarray_sum

from collections import Counter
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = Counter(nums[:k - 1])
        s = sum(nums[:k - 1])
        for in_, out in zip(nums[k - 1:], nums):
            cnt[in_] += 1  # 移入元素
            s += in_
            if len(cnt) == k:
                ans = max(ans, s)
            cnt[out] -= 1  # 移出元素
            if cnt[out] == 0:
                del cnt[out]  # 重要：及时移除个数为 0 的数据
            s -= out
        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 5, 4, 2, 9]
    # k = 5
    # nums = [9,18,10,13,17,9,19,2,1,18]
    # k = 5
    # nums = [18, 9, 9, 12, 12, 18]
    # k = 2
    nums = [1,2,2]
    k = 2
    ret = sol.maximumSubarraySum(nums, k)
    print(ret)
