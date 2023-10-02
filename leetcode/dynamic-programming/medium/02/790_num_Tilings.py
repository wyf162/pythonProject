# _*_ coding: utf-8 _*_
# @Time : 2022/11/12 9:37 AM 
# @Author : yefe
# @File : 790_num_Tilings

from typing import Dict, Tuple
from collections import defaultdict
import string


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * 4 for _ in range(n + 1)]
        dp[0][3] = 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][3]
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
            dp[i][3] = (((dp[i - 1][0] + dp[i - 1][1]) % MOD + dp[i - 1][2]) % MOD + dp[i - 1][3]) % MOD
        return dp[n][3]


if __name__ == '__main__':
    sol = Solution()
    n = 3
    ret = sol.numTilings(n)
    print(ret)
