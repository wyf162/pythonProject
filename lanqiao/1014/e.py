# -*- coding : utf-8 -*-
# @Time: 2023/10/14 19:36
# @Author: yefei.wang
# @File: e.py

from typing import Sequence, List


def knuth_morris_pratt(text: Sequence, pattern: Sequence) -> List[int]:
    """
    Given two strings text and pattern, return the list of start indexes in text that matches with the pattern
    using knuth_morris_pratt algorithm.

    Args:
        text: Text to search
        pattern: Pattern to search in the text
    Returns:
        List of indices of patterns found

    Example:
        # >>> knuth_morris_pratt('hello there hero!', 'he')
        [0, 7, 12]

    If idx is in the list, text[idx : idx + M] matches with pattern.
    Time complexity of the algorithm is O(N+M), with N and M the length of text and pattern, respectively.
    """
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
    for i in range(n * 2):
        while j and abs(ord(text[i % n]) - ord(pattern[j])) != 32:
            j = pi[j - 1]
        if abs(ord(text[i % n]) - ord(pattern[j])) == 32:
            j += 1
            if j == m:
                ret.append(i - m + 1)
                j = pi[j - 1]
    return ret


import os
import sys

# 请在此输入您的代码
sys.stdin = open('./../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
s = input()
t = input()

idxs = knuth_morris_pratt(s, t)
if not idxs:
    print('No')
else:
    print('Yes')
    print(min(idxs[0], n - idxs[0]))
