# _*_ coding: utf-8 _*_
# @Time : 2022/05/02 9:27 PM 
# @Author : yefe
# @File : 16021_find_swap_values
from typing import List


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        diff = sum(array1)-sum(array2)
        if diff % 2==1:
            return []
        diff = diff // 2
        s1 = set(array1)
        for num in array2:
            if num+diff in s1:
                return [num+diff, num]
        return []


if __name__ == '__main__':
    sol = Solution()
    array1 = [4, 1, 2, 1, 1, 2]
    array2 = [3, 6, 3, 3]
    ret = sol.findSwapValues(array1, array2)
    print(ret)
