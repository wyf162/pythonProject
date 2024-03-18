# -*- coding: utf-8 -*-
# @Time: 2024/3/18 10:10
# @Author: yfwang
# @File: 3085.py

from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        nums = list(sorted(cnt.values()))
        ret = len(word)

        n = len(nums)
        for i in range(n):
            x = nums[i]
            tmp = sum(nums[:i])
            for j in range(i, n):
                if nums[j] - x > k:
                    tmp += nums[j] - (x + k)
            ret = min(ret, tmp)
        return ret
