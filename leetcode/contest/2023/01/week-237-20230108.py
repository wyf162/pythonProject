# _*_ coding: utf-8 _*_
# @Time : 2023/01/08 10:29 AM 
# @Author : yefe
# @File : week-237-20230108

from collections import Counter
from typing import List
import heapq
import math


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = []
        ans = 0
        for num in nums:
            heapq.heappush(pq, -num)
        while k > 0:
            num = heapq.heappop(pq)
            ans += num
            heapq.heappush(pq, math.ceil(num / 3))
        return ans

    def isItPossible2(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        diff12 = set(cnt1.keys()) - set(cnt2.keys())
        diff21 = set(cnt2.keys()) - set(cnt1.keys())
        same = set(cnt1.keys()) & set(cnt2.keys())

        if len(cnt1) == len(cnt2):
            return True

        if abs(len(cnt1) - len(cnt2)) == 1:
            pass

    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        if len(cnt1) < len(cnt2):
            cnt1, cnt2 = cnt2, cnt1

        ss = set(cnt1.keys()) & set(cnt2.keys())
        one_word1 = any(cnt1[k] == 1 for k in ss)
        two_word1 = any(cnt1[k] > 1 for k in ss)

        if len(cnt1) == len(cnt2):
            return True
        if len(cnt1) - len(cnt2) == 1:
            ks = set(cnt1.keys()) - set(cnt2.keys())
            for k in ks:
                if cnt1[k] == 1 and cnt2[k] == 0 and one_word1:
                    return True
                if cnt1[k] > 1 and cnt2[k] == 0 and two_word1:
                    return True
            return False

        if len(cnt1) - len(cnt2) == 2:
            ks1 = set(cnt2.keys()) - set(cnt1.keys())
            if ks1:
                return False

            ks = set(cnt1.keys()) - set(cnt2.keys())
            for k in ks:
                if cnt1[k] == 1 and cnt2[k] == 0:
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    # word1 = "bb"
    # word2 = "abbcc"
    word1 = "abcc"
    word2 = "aab"
    # word1 = "ab"
    # word2 = "abcc"
    ret = sol.isItPossible(word1, word2)
    print(ret)
