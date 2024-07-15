# -*- coding: utf-8 -*-
# @Time: 2024/7/15 13:40
# @Author: yfwang
# @File: 3218.py

from typing import List


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort()
        verticalCut.sort()
        i1, i2 = m - 2, n - 2
        ch, cv = 1, 1
        ans = 0
        while True:
            if i1 >= 0 and i2 >= 0:
                if horizontalCut[i1] > verticalCut[i2]:
                    ans += horizontalCut[i1] * cv
                    ch += 1
                    i1 -= 1
                else:
                    ans += verticalCut[i2] * ch
                    cv += 1
                    i2 -= 1
            elif i1 >= 0:
                ans += horizontalCut[i1] * cv
                ch += 1
                i1 -= 1
            elif i2 >= 0:
                ans += verticalCut[i2] * ch
                cv += 1
                i2 -= 1
            else:
                break
        return ans


if __name__ == '__main__':
    sol = Solution()
    m = 3
    n = 2
    horizontalCut = [1, 3]
    verticalCut = [5]
    ret = sol.minimumCost(m, n, horizontalCut, verticalCut)
    print(ret)














