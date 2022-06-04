# _*_ coding: utf-8 _*_
# @Time : 2022/05/25 11:14 PM 
# @Author : yefe
# @File : 516_longest_palindrome_subseq


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2
            else:
                dp[i][i+1] = 1
        for l in range(2, n):
            for i in range(n - l):
                j = i + l
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n-1]


if __name__ == '__main__':
    sol = Solution()
    # s = "bbbab"
    s = "abcdef"
    ret = sol.longestPalindromeSubseq(s)
    print(ret)
