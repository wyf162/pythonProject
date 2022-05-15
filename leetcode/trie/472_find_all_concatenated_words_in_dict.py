# _*_ coding: utf-8 _*_
# @Time : 2022/05/14 6:11 PM 
# @Author : yefe
# @File : 472_find_all_concatenated_words_in_dict
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
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        ret = []
        for word in words:
            for i in range(1, len(word)):
                if trie.check(word[:i]) and trie.check(word[i:]):
                    ret.append(word)
                    break
        return ret


if __name__ == '__main__':
    sol = Solution()
    # words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat",
    #          "ratcatdogcat"]
    words = ["a", "b", "ab", "abc"]
    ret = sol.findAllConcatenatedWordsInADict(words)
    print(ret)
