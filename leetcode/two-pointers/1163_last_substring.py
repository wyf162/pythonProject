# -*- coding : utf-8 -*-
# @Time: 2022/8/7 16:56
# @Author: yefei.wang
# @File: 1163_last_substring.py


class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        l = 0
        r = 1
        k = 0
        while r + k < n:
            if s[l] > s[r] or s[l + k] > s[r + k]:
                r += 1
                k = 0
            if r+k>=n:
                break
            elif s[l] < s[r + k]:
                l = r + k
                r = l + 1
                k = 0
            elif s[l + k] < s[r + k]:
                l = r
                r += 1
                k = 0
            else:
                k += 1
        return s[l:]


if __name__ == '__main__':
    sol = Solution()
    # s = "abab"
    s = "cacacb"
    ret = sol.lastSubstring(s)
    print(ret)
