# -*- coding : utf-8 -*-
# @Time: 2023/9/29 10:51
# @Author: yefei.wang
# @File: 1235_jobScheduling.py
import bisect
import heapq
from collections import defaultdict, Counter
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp = Counter()
        dp[0] = 0
        jobs = defaultdict(list)

        for s, e, p in zip(startTime, endTime, profit):
            jobs[s].append((e, p))

        ss = list(sorted(set(startTime)))
        h = []
        mx = 0
        for s in ss:
            while h and h[0][0] <= s:
                t, v = heapq.heappop(h)
                mx = max(mx, v)

            for e, p in jobs[s]:
                dp[e] = max(dp[e], mx + p)
                heapq.heappush(h, [e, dp[e]])

        return max(dp.values())


if __name__ == '__main__':
    sol = Solution()
    startTime = [1, 2, 3, 4, 6]
    endTime = [3, 5, 10, 6, 9]
    profit = [20, 20, 100, 70, 60]
    ret = sol.jobScheduling(startTime, endTime, profit)
    print(ret)
