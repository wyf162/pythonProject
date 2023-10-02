# _*_ coding: utf-8 _*_
# @Time : 2022/4/5 下午1:44 
# @Author : wangyefei
# @File : 17010_majority_element.py
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        return candidate if count * 2 > len(nums) else -1


if __name__ == '__main__':
    sol = Solution()
    # nums = [1,2,5,9,5,9,5,5,5]
    nums = [1, 2, 3]
    ret = sol.majorityElement(nums)
    print(ret)
