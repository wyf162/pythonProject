# _*_ coding: utf-8 _*_
# @Time : 2022/4/2 下午10:23 
# @Author : wangyefei
# @File : biweek-75-20220402.py
import copy
from typing import List


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ret = start^goal
        return ret.bit_count()

    def triangularSum2(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nex_nums = []
            for j in range(1, len(nums)):
                nex_nums.append((nums[j-1]+nums[j]) % 10)
            nums = copy.deepcopy(nex_nums)
        return nums[0]

    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]%10
        ret = nums[0]*(n-1)%10
        for i in range(1, n-1):
            ret += nums[i]*2*(n-1)%10
            ret %= 10
        ret += nums[n-1]*(n-1)%10
        ret %= 10
        return ret

    def numberOfWays(self, s: str) -> int:
        n = len(s)
        pre_zero = [0]*(n+1)
        pre_one = [0]*(n+1)
        for i in range(n):
            if s[i]=='0':
                pre_zero[i+1]=pre_zero[i]+1
                pre_one[i+1] = pre_one[i]
            else:
                pre_one[i + 1] = pre_one[i] + 1
                pre_zero[i+1] = pre_zero[i]

        print(pre_zero)
        print(pre_one)

        cnt_one = pre_one[-1]
        cnt_zero = pre_zero[-1]

        ret = 0
        for i in range(1, n-1):
            if s[i]=='0':
                ret = ret + pre_one[i+1]*(cnt_one-pre_one[i+1])
            else:
                ret = ret + pre_zero[i+1]*(cnt_zero-pre_zero[i+1])
        return ret

    def sumScores(self, s: str) -> int:
        pass


if __name__ == '__main__':
    sol = Solution()
    # s = "001101"
    # s = "111000"
    # ret = sol.numberOfWays(s)
    # print(ret)
    nums = [1,2,3,4,5]
    ret = sol.triangularSum(nums)
    print(ret)
    # start = 3
    # goal = 4
    # print(sol.minBitFlips(start, goal))