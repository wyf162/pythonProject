# -*- coding : utf-8 -*-
# @Time: 2022/8/6 15:19
# @Author: yefei.wang
# @File: 1178_find_num_of_valid_puzzle.py
from typing import List
from collections import defaultdict


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        hst = defaultdict(int)
        for word in words:
            ret = self.string2int(word)
            hst[ret] += 1

        ans = []

        for puzzle in puzzles:
            pet = self.string2int(puzzle)
            an = 0
            subset = pet
            while subset:
                if subset & (1<<(ord(puzzle[0])-ord('a'))):
                    an += hst[subset]
                subset = (subset - 1) & pet

            ans.append(an)
        return ans

    @staticmethod
    def string2int(word):
        ret = 0
        for c in word:
            i = ord(c) - ord('a')
            ret = ret | (1 << i)
        return ret


if __name__ == '__main__':
    sol = Solution()
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
    ans = sol.findNumOfValidWords(words, puzzles)
    print(ans)
