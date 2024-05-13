# _*_ coding: utf-8 _*_
# @Time : 2022/05/21 12:11 PM 
# @Author : yefe
# @File : 960_min_deletion_size
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        dp = [1] * n
        for j in range(n):
            for k in range(j + 1, n, 1):
                flag = True
                for i in range(m):
                    if strs[i][k] < strs[i][j]:
                        flag = False
                        break
                if flag:
                    dp[k] = max(dp[k], dp[j] + 1)
        return n - max(dp)


if __name__ == '__main__':
    strs = ["babca", "bbazb"]
    ret = Solution().minDeletionSize(strs)
    print(ret)
