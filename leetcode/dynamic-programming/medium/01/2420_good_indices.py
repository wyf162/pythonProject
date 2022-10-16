# _*_ coding: utf-8 _*_
# @Time : 2022/10/15 7:52 PM 
# @Author : yefe
# @File : 2420_good_indices

from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = [1] * n
        cnt = 1
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                cnt += 1
            else:
                cnt = 1
            left[i] = cnt

        right = [1] * n
        cnt = 1
        for i in range(n - 2, -1, -1):
            if nums[i + 1] >= nums[i]:
                cnt += 1
            else:
                cnt = 1
            right[i] = cnt

        print(left)
        print(right)

        rets = []
        for i in range(k, n-k):
            if left[i-1] >= k and right[i+1] >= k:
                rets.append(i)
        return rets


if __name__ == '__main__':
    sol = Solution()
    # nums = [2, 1, 1, 1, 3, 4, 1]
    # k = 2
    # nums = [878724, 201541, 179099, 98437, 35765, 327555, 475851, 598885, 849470, 943442]
    # k = 4
    nums = [440043, 276285, 336957]
    k = 1
    ans = sol.goodIndices(nums, k)
    print(ans)
