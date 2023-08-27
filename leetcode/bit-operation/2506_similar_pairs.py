# _*_ coding: utf-8 _*_
# @Time : 2022/12/23 2:19 PM 
# @Author : yefe
# @File : 2506_similar_pairs

from collections import defaultdict
from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        hst = defaultdict(int)
        ans = 0
        for word in words:
            idx = self.word2int(word)
            ans += hst[idx]
            hst[idx] += 1

        return ans


    @staticmethod
    def word2int(word):
        ans = 0
        for w in word:
            ans |= (1 << (ord(w) - ord('a')))

        return ans


if __name__ == '__main__':
    sol = Solution()
    words = ["aba", "aabb", "abcd", "bac", "aabc"]
    ret = sol.similarPairs(words)
    print(ret)
