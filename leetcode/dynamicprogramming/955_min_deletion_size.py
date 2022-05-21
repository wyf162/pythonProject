# _*_ coding: utf-8 _*_
# @Time : 2022/05/21 1:00 PM 
# @Author : yefe
# @File : 955_min_deletion_size
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        dp = ["" for _ in range(m)]
        ret = 0
        for j in range(n):
            for i in range(1, m):
                if dp[i]==dp[i-1] and strs[i][j]<strs[i-1][j]:
                    ret += 1
                    break
            else:
                for i in range(m):
                    dp[i] += strs[i][j]
        return ret


if __name__ == '__main__':
    strs = ["xga","xfb","yfa"]
    ret = Solution().minDeletionSize(strs)
    print(ret)
