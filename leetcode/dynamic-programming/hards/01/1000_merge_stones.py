# _*_ coding: utf-8 _*_
# @Time : 2022/08/24 10:32 PM 
# @Author : yefe
# @File : 1000_merge_stones

from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:

        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1
        dp = [[[0 for _k in range(k + 1)] for j in range(n + 1)] for i in range(n + 1)]

        pres = [0]*(n+1)

        for i in range(n):
            pres[i+1] = pres[i] + stones[i]

        for i in range(n+1):
            for j in range(i, n+1):
                for m in range(2, k+1):
                    dp[i][j][m] = 0x3f3f3f3f
            dp[i][i][1] = 0

        for l in range(2, n+1):
            for i in range(1, n-l+2):
                j = i+l-1
                for m in range(2, k+1):
                    for p in range(i, j):
                        dp[i][j][m] = min(dp[i][j][m], dp[i][p][1] + dp[p+1][j][m-1])
                dp[i][j][1] = dp[i][j][k] + pres[j] - pres[i-1]
        return dp[1][n][1]


if __name__ == '__main__':
    sol = Solution()
    stones = [3,2,4,1]
    K = 2
    ret = sol.mergeStones(stones, K)
    print(ret)
