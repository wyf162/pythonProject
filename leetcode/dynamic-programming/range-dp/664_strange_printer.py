# _*_ coding: utf-8 _*_
# @Time : 2022/11/11 10:27 PM 
# @Author : yefe
# @File : 664_strange_printer


# 与 312思想基本一致，枚举 k 时加一层限制
class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s: return 0
        N = len(s)
        dp = [[0] * (N) for i in range(N + 1)]
        for l in range(N):  # 区间长度
            for i in range(N - l):  # 区间起点
                j = i + l  # 区间终点
                dp[i][j] = dp[i + 1][j] + 1  # 初始化
                for k in range(i + 1, j + 1):  # 枚举分割点
                    if s[k] == s[i]:  # 首位一样可减少一次
                        dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k + 1][j])
        return dp[0][N - 1]


if __name__ == '__main__':
    sol = Solution()
    s = "ababa"
    ret = sol.strangePrinter(s)
    print(ret)
