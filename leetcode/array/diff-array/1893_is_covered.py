# _*_ coding: utf-8 _*_
# @Time : 2022/05/15 8:52 PM 
# @Author : yefe
# @File : 1893_is_covered
from typing import List
from collections import defaultdict
import bisect


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52  # 差分数组
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        # 前缀和
        curr = 0
        for i in range(1, 51):
            curr += diff[i]
            if left <= i <= right and curr <= 0:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    ranges = [[1, 2], [3, 4], [5, 6]]
    left = 2
    right = 6
    ret = sol.isCovered(ranges, left, right)
    print(ret)
