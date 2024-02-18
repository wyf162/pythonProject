# -*- coding : utf-8 -*-
# @Time: 2024/2/18 10:28
# @Author: yefei.wang
# @File: A.py

from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    ans += 1
        return ans