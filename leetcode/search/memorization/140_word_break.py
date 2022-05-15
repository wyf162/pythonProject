# _*_ coding: utf-8 _*_
# @Time : 2022/2/19 下午6:26 
# @Author : wangyefei
# @File : 140_word_break.py
from typing import List
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)

        @lru_cache(None)
        def backtrack(idx):
            if idx == n:
                return [[]]
            ans = list()
            for i in range(idx + 1, n + 1):
                word = s[idx:i]
                if word in word_set:
                    next_word_breaks = backtrack(i)
                    for next_word_break in next_word_breaks:
                        ans.append([word]+next_word_break.copy())
            return ans

        word_set = set(wordDict)
        break_list = backtrack(0)
        return [" ".join(words) for words in break_list]


if __name__ == '__main__':
    sol = Solution()
    s = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    ret = sol.wordBreak(s, word_dict)
    print(ret)
