# -*- coding : utf-8 -*-
# @Time: 2023/9/29 17:10
# @Author: yefei.wang
# @File: 87_isScramble.py

from collections import Counter


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        def dfs(s, t):
            n = len(s)
            if s == t:
                return True
            for i in range(1, n):
                if s[:i] == t[-i:] and s[i:] == t[:-i]:
                    return True

            ans = False
            for i in range(1, n):
                if Counter(s[:i]) == Counter(t[:i]):
                    if dfs(s[:i], t[:i]) and dfs(s[i:], t[i:]):
                        ans = True
                if Counter(s[:i]) == Counter(t[-i:]):
                    if dfs(s[:i], t[-i:]) and dfs(s[i:], t[:-i]):
                        ans = True
            return ans

        rst = dfs(s1, s2)
        return rst


if __name__ == '__main__':
    sol = Solution()
    s1 = "amcsjerqm"
    s2 = "memjrqcsa"
    ret = sol.isScramble(s1, s2)
    print(ret)
