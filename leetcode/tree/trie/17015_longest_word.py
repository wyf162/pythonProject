# _*_ coding: utf-8 _*_
# @Time : 2022/4/5 下午10:03 
# @Author : wangyefei
# @File : 17015_longest_word.py
from collections import defaultdict
from typing import List


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isEnd = False

    def insert(self, word):
        node = self
        for ch in word:
            node = node.children[ch]
        node.isEnd = True

    def check(self, word):
        if word == "":
            return True
        node = self
        for i, ch in enumerate(word):
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.isEnd and self.check(word[i + 1:]):
                return True
        return False


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        words.sort(key=lambda x: (len(x), x))
        ans = ""
        for word in words:
            if not word: continue
            if trie.check(word):
                if len(word) > len(ans):
                    ans = word
            else:
                trie.insert(word)
        return ans


if __name__ == '__main__':
    sol = Solution()
    words = ["cat","banana","dog","nana","walk","walker","dogwalker"]
    ret = sol.longestWord(words)
    print(ret)
