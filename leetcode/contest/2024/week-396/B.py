# -*- coding : utf-8 -*-
# @Time: 2024/5/5 10:34
# @Author: yefei.wang
# @File: B.py

from collections import Counter


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        cnt = Counter()
        n = len(word)
        for i in range(0, n, k):
            cnt[word[i:i + k]] += 1
        ret = n // k - max(cnt.values())
        return ret
