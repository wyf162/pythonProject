# _*_ coding: utf-8 _*_
# @Time : 2022/4/16 下午2:11 
# @Author : wangyefei
# @File : 16016_subsort.py
from typing import List


class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        stk = [-1,0]
        l, r = -1,-1
        m = 0
        for i in range(len(array)):
            if array[i]>=array[m]:
                stk.append(i)
                m = i
            else:
                while len(stk)>1 and array[i]<array[stk[-1]]:
                    stk.pop()
                l = stk[-1]+1
                r = i
        return [l,r]

    def sub_sort(self, nums: List[int]) -> List[int]:
        m, n = -1, -1
        l = len(nums)
        if l<=1:
            return [m,n]

        max = nums[0]
        min = nums[-1]
        for i in range(l):
            if nums[i]<max:
                n = i
            else:
                max = nums[i]
            if nums[l-i-1]>min:
                m=l-i-1
            else:
                min = nums[l-i-1]
        return [m,n]


if __name__ == '__main__':
    sol = Solution()
    array = [1,2,4,7,10,11,7,12,6,7,16,18,19]
    ret = sol.sub_sort(array)
    print(ret)