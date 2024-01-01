# -*- coding : utf-8 -*-
# @Time: 2023/12/9 22:34
# @Author: yefei.wang
# @File: B.py


class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        ans = 0
        n = len(word)
        t = 0
        for i in range(1, n):
            if abs(ord(word[i]) - ord(word[i-1])) <= 1:
                t += 1
            else:
                ans += (t+1)//2
                t = 0
        ans += (t+1) // 2
        return ans

