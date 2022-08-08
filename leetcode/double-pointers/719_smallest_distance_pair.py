# -*- coding : utf-8 -*-
# @Time: 2022/8/7 15:40
# @Author: yefei.wang
# @File: 719_smallest_distance_pair.py
from typing import List
import bisect


class Solution:
    def smallestDistancePair2(self, nums: List[int], k: int) -> int:

        def count(mid: int) -> int:
            cnt = 0
            for j, num in enumerate(nums):
                i = bisect.bisect_left(nums, num - mid, 0, j)
                cnt += j - i
            return cnt

        nums.sort()

        return bisect.bisect_left(range(nums[-1] - nums[0]), k, key=count)

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # def count(mid: int) -> int:
        #     cnt = 0
        #     i, j = 0, 1
        #     while j < n and i < n:
        #         while j < n and i < n and nums[j] < nums[i] + mid:
        #             j += 1
        #         cnt += j - i
        #         i += 1
        #     return cnt

        def count(mid: int) -> int:
            cnt = 0
            i = 0
            for j, num in enumerate(nums):
                while num-nums[i]>mid:
                    i += 1
                cnt += j-i
            return cnt

        nums.sort()

        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            cnt = count(mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 3, 7]
    # k = 1
    nums = [38, 33, 57, 65, 13, 2, 86, 75, 4, 56]
    k = 26
    ret = sol.smallestDistancePair(nums, k)
    print(ret)
