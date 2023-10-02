# -*- coding : utf-8 -*-
# @Time: 2022/6/18 15:10
# @Author: yefei.wang
# @File: 1089_duplicate_zeros.py
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i, j = 0, 0
        n = len(arr)
        while j < n:
            if arr[i] == 0:
                j += 2
            else:
                j += 1
            i += 1
        if j>n:
            arr[-1] = 0
            k = n - 2
            i -= 2
        else:
            k = n - 1
            i -= 1

        while k >= 0:
            if arr[i] == 0:
                arr[k] = 0
                k -= 1
                arr[k] = 0
                k -= 1
            else:
                arr[k] = arr[i]
                k -= 1
            i -= 1


if __name__ == '__main__':
    sol = Solution()
    # arr = [1,0,2,3,0,4,5,0]
    arr = [8, 4, 5, 0, 0, 0, 0, 7]
    sol.duplicateZeros(arr)
    print(arr)
