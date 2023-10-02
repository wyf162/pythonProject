# -*- coding : utf-8 -*-
# @Time: 2022/1/16 10:38
# @Author: yefei.wang
# @File: 20220116.py
from typing import List
import heapq


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target < 3:
            return target - 1
        cnt = 0
        max_doubles = maxDoubles
        while target > 1:
            if max_doubles > 0 and target % 2 == 0:
                max_doubles -= 1
                target = target >> 1
                cnt += 1
            elif max_doubles > 0 and target % 2 == 1:
                target -= 1
                cnt += 1
            else:
                cnt += target - 1
                target = 1
        return cnt

    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        hq = list()
        for i in range(n):
            p, b = questions[i]
            dp[i] = max(dp[i - 1], p) if i > 0 else p
            heapq.heappush(hq, (i + b + 1, dp[i]))
            idx, val = hq[0]
            while idx <= i:
                idx, val = heapq.heappop(hq)
                if val + p > dp[i]:
                    dp[i] = val + p
                    heapq.heappush(hq, (i + b + 1, dp[i]))
                idx, val = hq[0]
        print(dp)
        return dp[-1]

    def most_points(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            p, b = questions[i]
            j = i + b + 1
            dp[i] = max(dp[i + 1], p + (dp[j] if j < n else 0))
        print(dp)
        return dp[0]



if __name__ == '__main__':
    # questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    # questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    # questions = [[3,1],[4,3],[4,4],[2,5]]
    # questions = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 5]]
    # 781
    questions = [[21, 2], [1, 2], [12, 5], [7, 2], [35, 3], [32, 2], [80, 2], [91, 5], [92, 3], [27, 3], [19, 1],
                 [37, 3], [85, 2], [33, 4], [25, 1], [91, 4], [44, 3], [93, 3], [65, 4], [82, 3], [85, 5], [81, 3],
                 [29, 2], [25, 1], [74, 2], [58, 1], [85, 1], [84, 2], [27, 2], [47, 5], [48, 4], [3, 2], [44, 3],
                 [60, 5], [19, 2], [9, 4], [29, 5], [15, 3], [1, 3], [60, 2], [63, 3], [79, 3], [19, 1], [7, 1],
                 [35, 1], [55, 4], [1, 4], [41, 1], [58, 5]]
    sol = Solution()
    data = sol.most_points(questions)
    print(data)
