# _*_ coding: utf-8 _*_
# @Time : 2022/09/10 1:47 PM 
# @Author : yefe
# @File : 1383_max_performance
import heapq
from typing import List


class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        v = [(s, e) for s, e in zip(speed, efficiency)]
        v.sort(key=lambda x: -x[1])

        q = list()
        ans, total = 0, 0
        for i in range(n):
            minE, totalS = v[i][1], total + v[i][0]
            ans = max(ans, minE * totalS)
            heapq.heappush(q, v[i])
            total += v[i][0]
            if len(q) == k:
                item = heapq.heappop(q)
                total -= item[0]
        return ans % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()
    n = 6
    speed = [2, 10, 3, 1, 5, 8]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 2
    ret = sol.maxPerformance(n, speed, efficiency, k)
    print(ret)
