# -*- coding : utf-8 -*-
# @Time: 2022/1/9 10:31
# @Author: yefei.wang
# @File: 20220109.py

"""
rank 909 / 4786
"""

from typing import List
from collections import defaultdict
from sortedcontainers import SortedList


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            if len(set(matrix[i]))==n:
                continue
            else:
                return False
        for i in range(n):
            tmp=[]
            for j in range(n):
                tmp.append(matrix[i][j])
            if len(tmp)==n:
                continue
            else:
                return False
        return True

    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [0]
        for num in nums:
            presum.append(presum[-1]+num)
        cnt = presum[-1]
        for num in nums:
            presum.append(presum[-1]+num)
        ans = cnt
        for i in range(cnt, n*2):
            ans = min(ans, cnt-(presum[i]-presum[i-cnt]))
        return ans

    def sorted_string(self, s):
        return "".join(sorted(list(s)))

    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_hst = defaultdict(set)
        for startWord in startWords:
            start_hst[len(startWord)].add(startWord)
        print(start_hst)
        target_hst = defaultdict(SortedList)
        for target_word in targetWords:
            target_hst[len(target_word)].add(self.sorted_string(target_word))
        print(target_hst)
        ans = 0
        for i in range(1,26):
            for start_word in start_hst.get(i,set()):
                s = set(list(start_word))
                for j in range(26):
                    c = chr(97+j)
                    if c in s:
                        continue
                    s.add(c)
                    new_str = self.sorted_string(s)
                    while new_str in target_hst.get(i+1, set()):
                        ans += 1
                        target_hst[i+1].remove(new_str)
                    s.remove(c)
        return ans

    def word_count(self, start_words, target_words):
        s = set()
        for word in start_words:
            mask = 0
            for c in word:
                mask = mask | 1 << ord(c)-ord('a')
            s.add(mask)
        ans = 0
        for word in target_words:
            mask = 0
            for c in word:
                mask = mask | 1 << ord(c)-ord('a')
            for c in word:
                origin = mask ^ 1 << ord(c)-ord('a')
                if origin in s:
                    ans += 1
                    break
        return ans

if __name__ == '__main__':
    sol = Solution()
    # startWords = ["ant", "act", "tack"]
    # targetWords = ["tack", "act", "acti"]
    startWords = ["g", "vf", "ylpuk", "nyf", "gdj", "j", "fyqzg", "sizec"]
    targetWords = ["r", "am", "jg", "umhjo", "fov", "lujy", "b", "uz", "y"]
    # startWords = ["a"]
    # targetWords =["ab","ba"]

    ans = sol.wordCount(startWords, targetWords)
    print(ans)
    # nums = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1]
    # ans = sol.minSwaps(nums)

