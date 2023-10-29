# -*- coding : utf-8 -*-
# @Time: 2023/10/14 22:32
# @Author: yefei.wang
# @File: biweek-115.py
import math
from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        stk = []
        prev = 0
        ans = []
        for word in words:
            if word == 'prev':
                prev += 1
                if prev < len(stk):
                    ans.append(stk[-prev])
                else:
                    ans.append(-1)
            else:
                stk.append(int(word))
                prev = 0
        return ans

    def getWordsInLongestSubsequence2(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        pre = -1
        ans = []
        for i in range(n):
            if groups[i] != pre:
                ans.append(words[i])
                pre = groups[i]
        return ans

    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        def dist(s1, s2):
            return sum(int(s1[i] != s2[i]) for i in range(len(s1)))

        dp = [1] * n
        fa = [i for i in range(n)]

        dp[0] = 1

        for i in range(1, n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and dist(words[i], words[j]) == 1:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        fa[i] = j
        mx = max(dp)
        idx = 0
        for i in range(n - 1, -1, -1):
            if dp[i] == mx:
                idx = i
                break
        ans = [''] * mx
        while mx:
            mx -= 1
            ans[mx] = words[idx]
            idx = fa[idx]
        return ans

    def countSubMultisets2(self, nums: List[int], l: int, r: int) -> int:
        mod = 10 ** 9 + 7
        hst = Counter(nums)
        ks = list(sorted(hst.keys()))

        @lru_cache(None)
        def dfs(x, i):
            if (i < len(ks) and x < ks[i]) or i == len(ks):
                return 1
            else:
                c = 0
                for j in range(hst[ks[i]] + 1):
                    if x - ks[i] * j >= 0:
                        c += dfs(x - ks[i] * j, i + 1)
                c %= mod
                return c

        c1 = dfs(l - 1, 0)
        c2 = dfs(r, 0)
        rst = c2 - c1
        if l == 0:
            rst += 1
        rst %= mod
        return rst

    def countSubMultisets3(self, nums: List[int], l: int, r: int) -> int:
        mod = 10 ** 9 + 7
        hst = Counter(nums)
        ks = list(sorted(hst.keys()))

        @lru_cache(None)
        def dfs(x, i):
            if x > r:
                return 0
            if i == len(ks):
                return int(l <= x <= r)
            c = 0
            for j in range(hst[ks[i]] + 1):
                c += dfs(x + ks[i] * j, i + 1)
                c %= mod
            c %= mod
            return c

        rst = dfs(0, 0)
        return rst

    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        mod = 10 ** 9 + 7
        cnt = Counter(nums)
        dp = [0] * (r+1)
        dp[0] = 1
        for x in cnt:
            if x:
                k = cnt[x]
                for i in range(x, r+1):
                    dp[i] += dp[i-x]
                    dp[i] %= mod
                for i in range(r, (k+1)*x-1, -1):
                    dp[i] -= dp[i-(k+1)*x]
                    dp[i] %= mod
        return sum(dp[l:]) * (cnt[0] + 1) % mod

if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 2, 1, 3, 5, 2]
    # l = 3
    # r = 5
    nums = [2, 1, 2]
    l = 2
    r = 2
    ret = sol.countSubMultisets(nums, l, r)
    print(ret)

    # n = 3
    # words = ["bab", "dab", "cab"]
    # groups = [1, 2, 2]
    # ret = sol.getWordsInLongestSubsequence(n, words, groups)
    # print(ret)
