# -*- coding : utf-8 -*-
# @Time: 2023/12/10 10:40
# @Author: yefei.wang
# @File: D.py

from typing import List
from collections import defaultdict


class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        hst = defaultdict(list)
        for i, x in enumerate(nums):
            hst[x].append(i)

        intervals = []
        for k, v in hst.items():
            intervals.append([v[0], v[-1]])

        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                if intervals[i][1] > ans[-1][1]:
                    ans[-1][1] = intervals[i][1]
        n = len(ans)
        mod = 10**9+7
        return pow(2, n - 1,  mod)
