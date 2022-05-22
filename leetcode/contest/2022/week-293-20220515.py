# _*_ coding: utf-8 _*_
# @Time : 2022/05/15 10:28 AM 
# @Author : yefe
# @File : week-298-20220515
from typing import List
from collections import Counter
from sortedcontainers.sortedlist import SortedList


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ret = [words[0]]
        for i in range(1, len(words)):
            if Counter(words[i]) != Counter(words[i - 1]):
                ret.append(words[i])
        return ret

    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        ret = max(special[0] - bottom, top - special[-1])
        for i in range(1, len(special)):
            ret = max(ret, special[i] - special[i - 1] - 1)
        return ret

    def largestCombination(self, candidates: List[int]) -> int:
        hst = [0] * 25
        for candidate in candidates:
            for i in range(25):
                if candidate & 1 << i:
                    hst[i] += 1
        print(hst)
        return max(hst)


class CountIntervals:

    def __init__(self, l=1, r=10 ** 9):
        self.left = self.right = None
        self.l, self.r, self.sum = l, r, 0

    def add(self, l: int, r: int) -> None:
        if self.sum == self.r - self.l + 1: return
        if l <= self.l and self.r <= r:
            self.sum = self.r - self.l + 1
            return
        mid = (self.l + self.r) // 2
        if self.left is None: self.left = CountIntervals(self.l, mid)
        if self.right is None: self.right = CountIntervals(mid + 1, self.r)
        if l <= mid: self.left.add(l, r)
        if mid < r: self.right.add(l, r)
        self.sum = self.left.sum + self.right.sum

    def count(self) -> int:
        return self.sum


if __name__ == '__main__':

    count_intervals = CountIntervals()
    count_intervals.add(2, 3)
    count_intervals.add(7, 10)
    cnt = count_intervals.count()
    print(cnt)
    count_intervals.add(5, 8)
    cnt = count_intervals.count()
    print(cnt)


    # sol = Solution()
    # candidates = [16, 17, 71, 62, 12, 24, 14]
    # candidates = [8, 8, ]
    # ret = sol.largestCombination(candidates)
    # print(ret)

    # bottom = 6
    # top = 8
    # special = [7, 6, 8]

    # words = ["abba", "baba", "bbaa", "cd", "cd"]
    # ret = sol.removeAnagrams(words)
    # print(ret)
