# -*- coding : utf-8 -*-
# @Time: 2022/6/12 23:46
# @Author: yefei.wang
# @File: 890_find_and_replace_pattern.py
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        rets = []
        for word in words:
            if self.is_pattern(word, pattern):
                rets.append(word)
        return rets

    @staticmethod
    def is_pattern(word, pattern):
        if len(word) != len(pattern):
            return False
        hst = dict()

        for a, b in zip(word, pattern):
            if b not in hst:
                if b not in hst.keys() and a not in hst.values():
                    hst[b] = a
                else:
                    return False
            if a==hst[b]:
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    rets = sol.findAndReplacePattern(words, pattern)
    print(rets)
