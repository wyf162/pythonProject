# -*- coding : utf-8 -*-
# @Time: 2022/6/26 0:21
# @Author: yefei.wang
# @File: 6107_distinct_sequences.py
M = 10 ** 9 + 7


class Solution:
    def distinctSequences(self, n: int) -> int:
        allowed = {
            1: [2, 3, 4, 5, 6],
            2: [1, 3, 5],
            3: [1, 2, 4, 5],
            4: [1, 3, 5],
            5: [1, 2, 3, 4, 6],
            6: [1, 5]
        }

        dp = [[0 for _ in range(7)] for _ in range(7)]

        for i in range(1, 7):
            dp[0][i] = 1

        for _ in range(n - 1):
            new_dp = [[0 for _ in range(7)] for _ in range(7)]
            for i in range(7):
                for j in range(1, 7):
                    for nex in allowed[j]:
                        if nex != i:
                            new_dp[j][nex] += dp[i][j] % M
            dp = new_dp

        return sum(sum(row) for row in dp) % M


if __name__ == '__main__':
    sol = Solution()
    for i in range(2,7):
        print(sol.distinctSequences(i))
