# _*_ coding: utf-8 _*_
# @Time : 2022/2/27 上午10:24 
# @Author : wangyefei
# @File : 20220227.py
from collections import Counter
from typing import List


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = dict(Counter(s))
        c2 = dict(Counter(t))
        cnt = 0
        keys = set(c1.keys()) | set(c2.keys())
        for k in keys:
            cnt += abs(c1.get(k, 0) - c2.get(k, 0))
        return cnt

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        l = 0
        r = time[0] * totalTrips + 1
        while l < r:
            m = (l + r) >> 1
            print(l, r, m)
            if self.check(time, m, totalTrips):
                r = m
            else:
                l = m + 1
        return l

    def check(self, time, k, total_trips):
        return sum([k // x for x in time]) >= total_trips

    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        min_sec = [float('inf')] * 18
        for f, r in tires:
            x, time, sum = 1, f, 0
            while time <= changeTime + f:
                sum += time
                min_sec[x] = min(min_sec[x], sum)
                time *= r
                x += 1
        dp = [0] * (numLaps + 1)
        dp[0] = -changeTime
        for i in range(1, numLaps + 1):
            dp[i] = changeTime + min(dp[i - j] + min_sec[j] for j in range(1, min(18, i + 1)))
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    tires = [[2, 3], [3, 4]]
    changeTime = 5
    numLaps = 4
    ret = sol.minimumFinishTime(tires, changeTime, numLaps)
    print(ret)

    # time = [1, 1]
    # totalTrips = 1
    # ret = sol.minimumTime(time, totalTrips)
    # print(ret)
    # s = "leetcode"
    # t = "leetcodeee"
    # ret = sol.minSteps(s, t)
    # print(ret)
