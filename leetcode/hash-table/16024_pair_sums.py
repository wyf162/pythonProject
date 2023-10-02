# _*_ coding: utf-8 _*_
# @Time : 2022/05/02 9:16 PM 
# @Author : yefe
# @File : 16024_pair_sums
from typing import List
from collections import defaultdict


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        hst = defaultdict(int)
        pairs = []
        for num in nums:
            if hst[target - num] > 0:
                pairs.append([target - num, num])
                hst[target - num] -= 1
            else:
                hst[num] += 1
        return pairs


if __name__ == '__main__':
    sol = Solution()
    nums = [5, 6, 5, 6, 11]
    target = 11
    ret = sol.pairSums(nums, target)
    print(ret)
