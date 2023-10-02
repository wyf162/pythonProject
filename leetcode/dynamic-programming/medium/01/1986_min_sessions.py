# _*_ coding: utf-8 _*_
# @Time : 2022/10/17 11:09 PM 
# @Author : yefe
# @File : 1986_min_sessions
from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        valid = [False] * (1 << n)
        for mask in range(1, 1 << n):
            needTime = 0
            for i in range(n):
                if mask & (1 << i):
                    needTime += tasks[i]
            if needTime <= sessionTime:
                valid[mask] = True

        f = [float("inf")] * (1 << n)
        f[0] = 0
        for mask in range(1, 1 << n):
            subset = mask
            while subset:
                if valid[subset]:
                    f[mask] = min(f[mask], f[mask ^ subset] + 1)
                subset = (subset - 1) & mask

        return f[(1 << n) - 1]

