# _*_ coding: utf-8 _*_
# @Time : 2022/09/05 10:12 PM 
# @Author : yefe
# @File : 239_max_sliding_window

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

        rets = [nums[q[0]]]

        for i in range(k, len(nums)):

            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            while q and q[0] <= i - k:
                q.popleft()

            rets.append(nums[q[0]])

        return rets


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # k = 3
    nums = [1,-1]
    k = 1
    ans = sol.maxSlidingWindow(nums, k)
    print(ans)
