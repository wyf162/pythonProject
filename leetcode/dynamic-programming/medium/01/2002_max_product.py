# _*_ coding: utf-8 _*_
# @Time : 2022/10/15 9:34 PM 
# @Author : yefe
# @File : 2002_max_product


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        for i in range(1<<n):
            s1 = ""
            s2 = ""
            for k in range(n):
                if i&(1>>k):
                    s1 += s[i]
                else:
                    s2 += s[i]

