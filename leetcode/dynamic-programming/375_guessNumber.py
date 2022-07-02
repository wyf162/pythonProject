# _*_ coding: utf-8 _*_
# @Time : 2021/11/12 下午9:40 
# @Author : wangyefei
# @File : 375_guessNumber.py


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(n)]
        dp[0][0] = 0
        for i in range(n - 1):
            dp[i][i + 1] = i + 1
        for i in range(n - 2):
            dp[i][i + 2] = i + 2
        for k in range(3, n):
            for i in range(0, n - k):
                dp[i][i + k] = i + 1 + dp[i + 1][i + k]
                for j in range(i + 1, i + k):
                    dp[i][i + k] = min(j + 1 + max(dp[i][j - 1], dp[j + 1][i + k]), dp[i][i + k])
        for i in range(n):
            print(dp[i])
        return dp[0][9]


if __name__ == "__main__":
    sol = Solution()
    n = 10
    print(sol.getMoneyAmount(n))
