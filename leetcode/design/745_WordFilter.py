# -*- coding : utf-8 -*-
# @Time: 2022/7/14 19:59
# @Author: yefei.wang
# @File: 745_WordFilter.py
from itertools import zip_longest
from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.weightKey = ('#', '#')
        for i, word in enumerate(words):
            cur = self.trie
            m = len(word)
            for j in range(m):
                tmp = cur
                for k in range(j, m):
                    key = (word[k], '#')
                    if key not in tmp:
                        tmp[key] = {}
                    tmp = tmp[key]
                    tmp[self.weightKey] = i
                tmp = cur
                for k in range(j, m):
                    key = ('#', word[-k - 1])
                    if key not in tmp:
                        tmp[key] = {}
                    tmp = tmp[key]
                    tmp[self.weightKey] = i
                key = (word[j], word[-j - 1])
                if key not in cur:
                    cur[key] = {}
                cur = cur[key]
                cur[self.weightKey] = i

    def f(self, pref: str, suff: str) -> int:
        cur = self.trie
        for key in zip_longest(pref, suff[::-1], fillvalue='#'):
            if key not in cur:
                return -1
            cur = cur[key]
        return cur[self.weightKey]


if __name__ == '__main__':
    words = ["apple"]
    parms = ["ap", "e"]
    wd = WordFilter(words)
    ret = wd.f(*parms)
    print(ret)
