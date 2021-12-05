# _*_ coding: utf-8 _*_
# @Time : 2021/11/28 下午12:19 
# @Author : wangyefei
# @File : 438_findAnagrams.py

from typing import List
from copy import deepcopy

CNT = 26
OFFSET = ord('a')


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(s)
        record = [[0 for i in range(CNT)] for i in range(m + 1)]
        for i in range(m):
            idx = ord(s[i]) - OFFSET
            record[i+1] = deepcopy(record[i])
            record[i + 1][idx] = record[i][idx] + 1
        for i in range(m):
            print(record[i])
        k = len(p)
        target = [0] * CNT
        for i in range(len(p)):
            target[ord(p[i]) - OFFSET] += 1
        print(target)
        ans = []
        for i in range(0, m - k+1):
            for j in range(k, m+1):
                if self.check(record[i], record[j], target):
                    ans.append(i)
        return ans

    def check(self, arr1, arr2, target):
        for i in range(CNT):
            if arr2[i] - arr1[i] == target[i]:
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    s ="abab"
    p = "ab"
    print(sol.findAnagrams(s,p))