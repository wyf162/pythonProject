# -*- coding : utf-8 -*-
# @Time: 2022/7/9 15:07
# @Author: yefei.wang
# @File: 873_len_longest_fib_subseq.py

from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        hst = {k: v for v, k in enumerate(arr)}
        n = len(arr)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dp[i][j] = 2

        for i in range(n):
            for j in range(i + 1, n):
                diff = arr[j] - arr[i]
                idx = hst.get(diff)
                if idx is not None and idx < i:
                    dp[i][j] = max(dp[i][j], dp[idx][i] + 1)
        max_cnt = max([max(row) for row in dp])

        return max_cnt if max_cnt > 2 else 0


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    ret = Solution().lenLongestFibSubseq(arr)
    print(ret)
