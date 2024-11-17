# -*- coding : utf-8 -*-
# @Time: 2024/9/8 10:33
# @Author: yefei.wang
# @File: B.py

from typing import List


class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        n = len(start)
        start.sort()

        def check(x):
            coord = start[0]
            for i in range(1, n):
                if start[i] >= coord + x:
                    coord = start[i]
                elif start[i] + d >= coord + x:
                    coord = coord + x
                else:
                    return False
            return True

        L, R = 0, 2 * 10 ** 9 + 5
        while L <= R:
            mid = (L + R) // 2
            if check(mid):
                ans = mid
                L = mid + 1
            else:
                R = mid - 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    start = [6, 0, 3]
    d = 2
    ret = sol.maxPossibleScore(start, d)
    print(ret)
