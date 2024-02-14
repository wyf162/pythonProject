# -*- coding : utf-8 -*-
# @Time: 2024/2/14 16:03
# @Author: yefei.wang
# @File: 3034.py

from typing import List


def knuth_morris_pratt(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = [0 for i in range(m)]
    i = 0
    j = 0
    # making pi table
    for i in range(1, m):
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    # finding pattern
    j = 0
    ret = []
    for i in range(n):
        while j and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                ret.append(i - m + 1)
                j = pi[j - 1]
    return ret


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        text = []
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                text.append(1)
            elif nums[i] < nums[i - 1]:
                text.append(-1)
            else:
                text.append(0)

        ret = knuth_morris_pratt(text, pattern)
        return len(ret)