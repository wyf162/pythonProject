# _*_ coding: utf-8 _*_
# @Time : 10/30/21 7:10 PM 
# @Author : wangyefei
# @File : 638_singleNumber.py
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num
        lsb = x & (-x)
        print(lsb)
        x1, x2 = 0, 0
        for num in nums:
            print(num, lsb, lsb & num)
            if lsb & num:
                x1 ^= num
            else:
                x2 ^= num
        return [x1, x2]


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 3, 5, 1, 1]
    print(sol.singleNumber(nums))
