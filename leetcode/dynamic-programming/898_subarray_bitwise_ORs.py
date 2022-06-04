# _*_ coding: utf-8 _*_
# @Time : 2022/05/21 8:59 PM 
# @Author : yefe
# @File : 898_subarray_bitwise_ORs
from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        s = set()
        if n < 2:
            return n
        for i in range(n):
            s.add(arr[i])
            for j in range(i - 1, -1, -1):
                if arr[j] | arr[i] == arr[j]:
                    break
                arr[j] |= arr[i]
                s.add(arr[j])
        return len(s)
