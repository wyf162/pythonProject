# -*- coding : utf-8 -*-
# @Time: 2024/6/22 22:29
# @Author: yefei.wang
# @File: D.py
# permutation


from typing import List


class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        Mod = 10 ** 9 + 7
        limit = [-1] * n
        for idx,cnt in requirements:
            limit[idx] = cnt
        if limit[0] != -1 and limit[0] != 0:
            return 0
        dp = [[0] * 401 for _ in range(n)]
        dp[0][0] = 1
        for i in range(1,n):
            for j in range(401):
                # 前面有i+1个位置可以插入
                dp[i][j] = sum(dp[i - 1][max(0,j - i):j + 1]) % Mod
            if limit[i] != -1:
                for j in range(401):
                    if limit[i] != j:
                        dp[i][j] = 0
        return sum(dp[-1])


