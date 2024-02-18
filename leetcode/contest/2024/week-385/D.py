# -*- coding : utf-8 -*-
# @Time: 2024/2/18 10:28
# @Author: yefei.wang
# @File: D.py
from collections import Counter
from typing import List


def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        else:
            z[i] = max(0, r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    z[0] = n
    return z


class Node:
    __slots__ = 'son', 'cnt'

    def __init__(self):
        self.son = dict()
        self.cnt = 0


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        root = Node()
        ans = 0
        for word in words:
            cur = root
            z = z_function(word)
            for i, x in enumerate(z):
                c = word[i]
                if c not in cur.son:
                    cur.son[c] = Node()
                cur = cur.son[c]
                if z[-1 - i] == i + 1:
                    ans += cur.cnt
            cur.cnt += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    # words = ["a", "aba", "ababa", "aa"]
    # words = ["pa", "papa", "ma", "mama"]
    # words = ["abab", "ab"]
    # words = ["a", "a"]
    words = ["aaa", "baa", "b", "bcba"]
    ret = sol.countPrefixSuffixPairs(words)
    print(ret)
