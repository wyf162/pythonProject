# -*- coding : utf-8 -*-
# @Time: 2022/2/19 12:25
# @Author: yefei.wang
# @File: 969_packet_sort.py
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = list()
        n = len(arr)-1
        i = len(arr)-1
        nums = sorted(arr)
        while i>=0:
            if arr[i]==nums[i]:
                i = i-1
            else:
                idx = arr.index(nums[i])
                ans.append(idx+1)
                arr[:idx+1]=reversed(arr[:idx+1])
                ans.append(i+1)
                arr[:i+1]=reversed(arr[:i+1])
                i = i-1
        print(arr)
        return ans


if __name__ == '__main__':
    sol = Solution()
    arr = [3,2,4,1]
    ans = sol.pancakeSort(arr)
    print(ans)