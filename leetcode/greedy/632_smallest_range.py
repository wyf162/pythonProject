# _*_ coding: utf-8 _*_
# @Time : 2022/11/05 2:38 PM 
# @Author : yefe
# @File : 632_smallest_range

import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        range_left, range_right = -10**9, 10**9
        max_val = max(vec[0] for vec in nums)
        pq = [(vec[0], i, 0) for i, vec in enumerate(nums)]
        heapq.heapify(pq)

        while True:
            min_val, row, idx = heapq.heappop(pq)
            if max_val - min_val < range_right - range_left:
                range_left, range_right = min_val, max_val

            if idx == len(nums[row])-1:
                break

            max_val = max(max_val, nums[row][idx+1])
            heapq.heappush(pq, (nums[row][idx+1], row, idx+1))
        return [range_left, range_right]


if __name__ == '__main__':
    sol = Solution()
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    ret = sol.smallestRange(nums)
    print(ret)
