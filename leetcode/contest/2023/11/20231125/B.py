# -*- coding : utf-8 -*-
# @Time: 2023/11/25 22:27
# @Author: yefei.wang
# @File: B.py
from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        max_h, max_v = 1, 1
        hBars.sort()
        vBars.sort()
        d = 2 if hBars else 1
        max_h = max(max_h, d)
        for i in range(1, len(hBars)):
            if hBars[i] - hBars[i - 1] == 1:
                d += 1
                max_h = max(max_h, d)
            else:
                d = 2
                max_h = max(max_h, d)

        d = 2 if vBars else 1
        max_v = max(max_v, d)
        for i in range(1, len(vBars)):
            if vBars[i] - vBars[i - 1] == 1:
                d += 1
                max_v = max(max_v, d)
            else:
                d = 2
                max_v = max(max_v, d)

        a = min(max_v, max_h)
        return a * a


if __name__ == '__main__':
    sol = Solution()
    n = 2
    m = 3
    hBars = [2, 3]
    vBars = [2, 3, 4]
    # n = 2
    # m = 1
    # hBars = [2, 3]
    # vBars = [2]

    ret = sol.maximizeSquareHoleArea(n, m, hBars, vBars)
    print(ret)
