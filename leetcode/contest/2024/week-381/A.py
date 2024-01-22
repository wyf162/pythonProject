# -*- coding : utf-8 -*-
# @Time: 2024/1/21 10:29
# @Author: yefei.wang
# @File: A.py

from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        freq = Counter(word)
        cur = 1
        ans = 0
        for x in sorted(cnt.values(), reverse=True):
            freq[cur] += 1
            ans += x * cur
            if freq[cur] == 8: cur += 1
        return ans