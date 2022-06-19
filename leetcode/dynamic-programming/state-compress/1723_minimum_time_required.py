# -*- coding : utf-8 -*-
# @Time: 2022/6/12 19:16
# @Author: yefei.wang
# @File: 1723_minimum_time_required.py
from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        s = [0] * (1 << n)

        for i in range(1, 1 << n):
            x = trailing_zero(i)
            y = i - (1 << x)
            s[i] = s[y] + jobs[x]
        dp = [[0] * (1 << n) for _ in range(k)]

        for i in range(1 << n):
            dp[0][i] = s[i]

        for i in range(1, k):
            for j in range(1 << n):
                minn = 1 << 32
                x = j
                while True:
                    minn = min(minn, max(dp[i - 1][j - x], s[x]))
                    x = (x - 1) & j
                    if not x:
                        break
                dp[i][j] = minn
        return dp[k - 1][(1 << n) - 1]


def trailing_zero(x):
    s = bin(x)[2:]
    cnt = 0
    tag = False
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0':
            cnt += 1
        else:
            tag = True
            break
    return cnt if tag else 0


if __name__ == '__main__':
    sol = Solution()
    jobs = [3, 2, 3]
    k = 3
    ret = sol.minimumTimeRequired(jobs, k)
    print(ret)
