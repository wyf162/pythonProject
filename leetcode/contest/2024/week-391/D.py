# -*- coding : utf-8 -*-
# @Time: 2024/3/31 10:29
# @Author: yefei.wang
# @File: D.py
from itertools import accumulate
from typing import List

inf = 10 ** 9


class Solution:
    def minimumDistance(self, p: List[List[int]]) -> int:
        n = len(p)
        v1 = [x + y for x, y in p]
        v2 = [x - y for x, y in p]

        v1_p_min = list(accumulate(v1, min, initial=inf))
        v1_p_max = list(accumulate(v1, max, initial=-inf))
        v2_p_min = list(accumulate(v2, min, initial=inf))
        v2_p_max = list(accumulate(v2, max, initial=-inf))

        v1.reverse()
        v2.reverse()

        v1_s_min = list(accumulate(v1, min, initial=inf))[::-1]
        v1_s_max = list(accumulate(v1, max, initial=-inf))[::-1]
        v2_s_min = list(accumulate(v2, min, initial=inf))[::-1]
        v2_s_max = list(accumulate(v2, max, initial=-inf))[::-1]

        ans = inf
        for i in range(n):
            ans = min(ans, max(max(v1_p_max[i], v1_s_max[i + 1]) - min(v1_p_min[i], v1_s_min[i + 1]),
                               max(v2_p_max[i], v2_s_max[i + 1]) - min(v2_p_min[i], v2_s_min[i + 1])))
        return ans


if __name__ == '__main__':
    sol = Solution()
    # points = [[1, 2], [8, 6], [7, 1], [10, 4], [4, 5], [5, 5], [10, 2], [3, 2], [8, 10], [9, 7]]
    points = [[10, 3], [4, 2], [8, 9], [9, 3], [4, 5], [6, 9], [9, 2], [7, 5]]
    ret = sol.minimumDistance(points)
    print(ret)
