# _*_ coding: utf-8 _*_
# @Time : 2022/11/06 10:47 AM 
# @Author : yefe
# @File : 1526_max_num_of _substrings

from collections import Counter
from typing import List, Mapping, Tuple

# 1 <= s.length <= 10^5

Interval = Tuple[int, int]


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:

        # 1.预处理区间
        intervalMap: Mapping[str, Interval] = dict()
        for char in set(s):
            start, end = s.find(char), s.rfind(char)
            intervalMap[char] = (start, end)

        # 2.对每个字符对应的区间寻找符合题意的边界
        validIntervals: List[Interval] = []
        for (start, end) in intervalMap.values():
            startCand, endCand = start, end
            while True:
                charInInterval = set(s[startCand : endCand + 1])
                for char in charInInterval:
                    startCand = min(startCand, intervalMap[char][0])
                    endCand = max(endCand, intervalMap[char][1])
                if (startCand, endCand) == (start, end):
                    break
                start, end = startCand, endCand
            validIntervals.append((start, end))

        # 3.排序，贪心选择结束早且更短的区间，类似leetcode452、646、1353
        validIntervals.sort(key=lambda x: (x[1], x[1] - x[0]))
        res, preEnd = [], -1
        for start, end in validIntervals:
            if start >= preEnd:
                res.append(s[start : end + 1])
                preEnd = end
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "adefaddaccc"
    ret = sol.maxNumOfSubstrings(s)
    print(ret)
