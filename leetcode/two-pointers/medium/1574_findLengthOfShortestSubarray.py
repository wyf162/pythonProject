# -*- coding : utf-8 -*-
# @Time: 2023/9/30 15:57
# @Author: yefei.wang
# @File: 1574_findLengthOfShortestSubarray.py
import bisect
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1
        while left + 1 < n:
            if arr[left] <= arr[left + 1]:
                left += 1
            else:
                break

        while right - 1 >= 0:
            if arr[right] >= arr[right - 1]:
                right -= 1
            else:
                break

        ans = min(n - left, right)
        while left >= 0:
            r = bisect.bisect_left(arr[right:], arr[left])
            ans = min(ans, right + r - left - 1)
            left -= 1
        return max(ans, 0)


if __name__ == '__main__':
    sol = Solution()
    # arr = [1, 2, 3, 10, 4, 2, 3, 5]
    # arr = [5, 4, 3, 2, 1]
    # arr = [1, 2, 3]
    arr = [16, 10, 0, 3, 22, 1, 14, 7, 1, 12, 15]
    ret = sol.findLengthOfShortestSubarray(arr)
    print(ret)
