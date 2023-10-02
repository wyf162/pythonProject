# -*- coding : utf-8 -*-
# @Time: 2022/6/19 10:29
# @Author: yefei.wang
# @File: week-298-20220619.py
from string import ascii_uppercase
from typing import List


class Solution:
    def greatestLetter(self, s: str) -> str:
        big = [0] * 26
        small = [0] * 26
        for a in s:
            if a.islower():
                idx = ord(a) - ord('a')
                small[idx] = 1
            elif a.upper():
                idx = ord(a) - ord('A')
                big[idx] = 1
        ret = ''
        for a in ascii_uppercase:
            idx = ord(a) - ord('A')
            if big[idx] and small[idx]:
                ret = a
        return ret

    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        if k == 0:
            if num % 10 == 0:
                return 1
            else:
                return -1

        d = num % 10
        i = 1
        while i <= 10:
            if d == (k * i) % 10:
                if k * i <= num:
                    return i
                else:
                    return -1
            else:
                i += 1
        return -1

    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        pre = [0]*(n+1)
        for i, a in enumerate(s):
            if a == '0':
                pre[i+1] = pre[i]+1
            else:
                pre[i+1] = pre[i]

        t = 0
        cnt = 0
        ret = 0
        for i in range(n-1, -1, -1):
            r_i = ((n-1)-i)
            v = 1 << r_i if s[i]=='1' else 0
            if t+v<=k:
                ret = max(ret, cnt+pre[i+1]+(1 if s[i]=='1' else 0))
                t += v
                cnt += 1
            else:
                return ret
        return ret

    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        hst = dict()
        for h, w, p in prices:
            hst[(h, w)] = p

        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max(hst.get((i, j), 0),
                               max((dp[i][k]+dp[i][j-k] for k in range(1, j)), default=0),
                               max((dp[k][j]+dp[i-k][j] for k in range(1, i)), default=0))

        return dp[m][n]


if __name__ == '__main__':
    sol = Solution()
    s = "1"
    k = 5
    ret = sol.longestSubsequence(s, k)
    print(ret)

    # num = 10
    # k = 1
    # # num = 37
    # # k = 2
    # ret = sol.minimumNumbers(num, k)
    # print(ret)
