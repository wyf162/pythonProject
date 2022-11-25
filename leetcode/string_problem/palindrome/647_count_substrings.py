# _*_ coding: utf-8 _*_
# @Time : 2022/11/13 4:44 PM 
# @Author : yefe
# @File : 647_count_substrings


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ret = 0
        for i in range(2 * n - 1):
            l = i // 2
            r = i // 2 + i % 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                ret += 1
        return ret
