# _*_ coding: utf-8 _*_
# @Time : 2022/05/22 3:22 PM 
# @Author : yefe
# @File : 84_largest_rectangle_area
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        stk = []
        for i in range(n):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)

        right = [n] * n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and heights[stk[-1]] > heights[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        area = 0
        for i in range(n):
            l, r = left[i] + 1, right[i] - 1
            val = heights[i] * (r - l + 1)
            area = max(area, val)
        return area


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    ret = Solution().largestRectangleArea(heights)
    print(ret)
