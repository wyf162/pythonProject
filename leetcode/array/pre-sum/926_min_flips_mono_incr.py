# -*- coding : utf-8 -*-
# @Time: 2022/6/11 15:05
# @Author: yefei.wang
# @File: 926_min_flips_mono_incr.py


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i + 1] = dp[i] + (1 if s[i] == '1' else 0)
        print(dp)
        cnt = n
        for i in range(n):
            cnt = min(cnt, dp[i] + (n - i - 1) - (dp[-1] - dp[i+1]))
        return cnt


if __name__ == '__main__':
    sol = Solution()
    s = "11011"
    ret = sol.minFlipsMonoIncr(s)
    print(ret)
