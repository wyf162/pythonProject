# -*- coding : utf-8 -*-
# @Time: 2022/7/24 23:20
# @Author: yefei.wang
# @File: 1851_min_interval.py

from typing import List
import bisect


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[1] - x[0])
        m = len(queries)

        qs = []
        for i, q in enumerate(queries):
            qs.append((q, i))
        qs.sort()

        fa = [_ for _ in range(m + 1)]

        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        ans = [-1] * m

        for _, p in enumerate(intervals):
            l, r = p[0], p[1]
            length = r - l + 1
            i = bisect.bisect_left(qs, l, key=lambda x: x[0])
            i = find(i)
            while i < m and qs[i][0] <= r:
                ans[qs[i][1]] = length
                fa[i] = i + 1
                i = find(i + 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
    queries = [2, 3, 4, 5]
    rets = sol.minInterval(intervals, queries)
    print(rets)
