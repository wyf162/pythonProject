# -*- coding : utf-8 -*-
# @Time: 2024/6/16 11:03
# @Author: yefei.wang
# @File: A.py
from itertools import accumulate
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        n = len(hours)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (hours[j + 1] + hours[i]) % 24 == 0:
                    ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    hours = [21, 19, 3]
    ret = sol.countCompleteDayPairs(hours)
