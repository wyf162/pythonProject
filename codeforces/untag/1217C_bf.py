# -*- coding: utf-8 -*-
# @Time: 2024/5/30 11:04
# @Author: yfwang
# @File: 1217C_bf.py
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
    for i in range(n):
        while j and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                ret.append(i - m + 1)
                j = pi[j - 1]
    return ret


import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
sys.stdout = open('../jury.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    s = input()
    n = len(s)
    ans = 0
    for i in range(1, n + 1):
        t = bin(i)[2:].zfill(i)
        arr = knuth_morris_pratt(s, t)
        ans += len(arr)
    print(ans)
