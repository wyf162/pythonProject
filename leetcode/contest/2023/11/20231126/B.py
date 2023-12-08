# -*- coding : utf-8 -*-
# @Time: 2023/11/26 10:34
# @Author: yefei.wang
# @File: B.py

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + int(s[i] in 'aeiou')

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                a = j + 1 - i
                vowels = pre_sum[j + 1] - pre_sum[i]
                consonants = a - vowels
                if vowels == consonants and vowels * consonants % k == 0:
                    ans += 1
        return ans
