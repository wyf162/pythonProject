# _*_ coding: utf-8 _*_
# @Time : 2022/3/15 下午7:04 
# @Author : wangyefei
# @File : 2044_count_max_or_subsets.py
from typing import List
from tools.decorators import print_run_time


class Solution:
    @print_run_time
    def countMaxOrSubsets2(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        max_or_val = 0
        for num in nums:
            max_or_val |= num

        for i in range(0, 1 << n):
            ret = 0
            for j in range(n):
                if (1 << j) & i:
                    ret |= nums[j]

            if ret == max_or_val:
                res += 1
        return res

    @print_run_time
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr, cnt = 0, 0

        def dfs(pos: int, orVal: int) -> None:
            if pos == len(nums):
                nonlocal maxOr, cnt
                if orVal > maxOr:
                    maxOr, cnt = orVal, 1
                elif orVal == maxOr:
                    cnt += 1
                return
            dfs(pos + 1, orVal | nums[pos])
            dfs(pos + 1, orVal)

        dfs(0, 0)
        return cnt


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 2, 1, 5, 4, 5, 6, 7, 8, 9, 11, 23, 4, 5, 6, 8]
    res = sol.countMaxOrSubsets2(nums)
    print(res)
