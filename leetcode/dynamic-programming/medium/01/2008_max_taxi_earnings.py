# _*_ coding: utf-8 _*_
# @Time : 2022/10/12 10:45 PM 
# @Author : yefe
# @File : 2008_max_taxi_earnings

from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:

        groups = [[] for _ in range(n+1)]
        f = [0]*(n+1)

        for start, end, tip in rides:
            groups[end].append([start, tip])

        for i in range(1, n+1):
            f[i] = f[i-1]
            for start, tip in groups[i]:
                f[i] = max(f[i], f[start]+i-start+tip)

        return f[-1]


if __name__ == '__main__':
    sol = Solution()
    n = 5
    rides = [[2, 5, 4], [1, 5, 1]]
    ret = sol.maxTaxiEarnings(n, rides)
    print(ret)
