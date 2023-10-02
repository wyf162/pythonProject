# -*- coding : utf-8 -*-
# @Time: 2022/7/14 21:46
# @Author: yefei.wang
# @File: 745_WordFilter2.py

from typing import List


class TrieNode:

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.idxs = []


class WordFilter:
    def __init__(self, words: List[str]):
        self.pre_trie = TrieNode()
        self.suf_trie = TrieNode()
        for i, word in enumerate(words):
            self.add_pre(word, i)
            self.add_suf(word, i)

    def add_pre(self, pre: str, idx: int) -> None:
        rt = self.pre_trie
        for c in pre:
            i = ord(c) - ord('a')
            if rt.children[i] is None:
                rt.children[i] = TrieNode()
            rt = rt.children[i]
            rt.idxs.append(idx)

    def add_suf(self, suf: str, idx: int) -> None:
        rt = self.suf_trie
        for c in suf[::-1]:
            i = ord(c) - ord('a')
            if rt.children[i] is None:
                rt.children[i] = TrieNode()
            rt = rt.children[i]
            rt.idxs.append(idx)

    def query(self, pre: str, suf: str) -> int:
        rt1 = self.pre_trie
        rt2 = self.suf_trie
        for c in pre:
            i = ord(c) - ord('a')
            if rt1.children[i] is None:
                return -1
            rt1 = rt1.children[i]

        for c in suf[::-1]:
            i = ord(c) - ord('a')
            if rt2.children[i] is None:
                return -1
            rt2 = rt2.children[i]
        pi = len(rt1.idxs) - 1
        si = len(rt2.idxs) - 1

        while 0 <= pi and 0 <= si:
            if rt1.idxs[pi] > rt2.idxs[si]:
                pi -= 1
            elif rt1.idxs[pi] < rt2.idxs[si]:
                si -= 1
            else:
                return rt1.idxs[pi]
        return -1

    def f(self, pref: str, suff: str) -> int:
        return self.query(pref, suff)


if __name__ == '__main__':
    # words = ["abbba", "abba"]
    # parms = ["ab", "ba"]
    words = ["apple"]
    parms = ["a", "e"]
    wd = WordFilter(words)
    ret = wd.f(*parms)
    print(ret)
