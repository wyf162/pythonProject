# -*- coding : utf-8 -*-
# @Time: 2024/1/28 10:31
# @Author: yefei.wang
# @File: A.py

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        # print(s)
        ans = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                ans += 1
        return ans
