# -*- coding: utf-8 -*-
# @Time: 2024/4/25 17:31
# @Author: yfwang
# @File: 3121.py

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        small = [-1] * 26
        big = [-1] * 26

        for i, c in enumerate(word):
            if c.isupper():
                idx = ord(c) - ord('A')
                if big[idx] == -1:
                    big[idx] = i
            else:
                idx = ord(c) - ord('A')
                small[idx] = i

        ans = 0
        for i in range(26):
            if small[i] == -1 or big[i] == -1:
                continue
            if small[i] < big[i]:
                ans += 1
        return ans
