# _*_ coding: utf-8 _*_
# @Time : 2022/05/25 10:03 PM 
# @Author : yefe
# @File : 1771_longest_palindrome


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        n = n1 + n2
        dp = [[0] * n for _ in range(n)]
        word = word1 + word2
        res = 2 if word[n1 - 1] == word[n1] else 0
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1):
            if word[i] == word[i + 1]:
                dp[i][i + 1] = 2
            else:
                dp[i][i + 1] = 1

        for l in range(2, n):
            for i in range(n - l):
                j = i + l
                if word[i] == word[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if i < n1 <= j:
                        res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return res


if __name__ == '__main__':
    word1 = "cacb"
    word2 = "cbba"
    ret = Solution().longestPalindrome(word1, word2)
    print(ret)
