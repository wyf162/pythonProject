# -*- coding : utf-8 -*-
# @Time: 2023/9/30 18:31
# @Author: yefei.wang
# @File: 986.py

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        m, n = len(firstList), len(secondList)
        ans = []
        while i < m and j < n:
            if firstList[i][1] < secondList[j][0]:
                i += 1
            elif secondList[j][1] < firstList[i][0]:
                j += 1
            else:
                l = max(firstList[i][0], secondList[j][0])
                r = min(firstList[i][1], secondList[j][1])
                ans.append([l, r])
                if firstList[i][1] <= r:
                    i += 1
                elif secondList[j][1] <= r:
                    j += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    ret = sol.intervalIntersection(firstList, secondList)
    print(ret)
