# _*_ coding: utf-8 _*_
# @Time : 2022/10/13 10:17 PM 
# @Author : yefe
# @File : 769_max_chunks_to_sorted

from typing import List


class Solution:

    def maxChunksToSort(self, arr: List[int]):
        stk = []
        for v in arr:
            if not stk or v >= stk[-1]:
                stk.append(v)
            else:
                mx = stk.pop()
                while stk and stk[-1] > v:
                    stk.pop()
                stk.append(mx)
        return len(stk)

