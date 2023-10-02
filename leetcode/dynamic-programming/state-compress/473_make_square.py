# -*- coding : utf-8 -*-
# @Time: 2022/6/15 20:38
# @Author: yefei.wang
# @File: 473_make_square.py
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        total_len = sum(matchsticks)
        if total_len % 4:
            return False
        t_len = total_len // 4
        dp = [-1] * (1 << n)
        dp[0] = 0
        for s in range(1, len(dp)):
            for k, v in enumerate(matchsticks):
                if s & (1 << k) == 0:
                    continue
                s1 = s & ~(1 << k)
                if dp[s1] >= 0 and dp[s1] + v <= t_len:
                    dp[s] = (dp[s1] + v) % t_len
                    break
        return dp[-1] == 0


if __name__ == '__main__':
    sol = Solution()
    matchsticks = [1, 1, 2, 2, 2]
    ret = sol.makesquare(matchsticks)
    print(ret)
