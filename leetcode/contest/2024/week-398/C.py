# -*- coding : utf-8 -*-
# @Time: 2024/5/19 10:42
# @Author: yefei.wang
# @File: C.py

from collections import Counter
from typing import List


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        ss = [str(x) for x in nums]
        n = len(ss)
        m = len(ss[0])
        ans = 0
        for j in range(m):
            tmp = [s[j] for s in ss]
            cnt = Counter(tmp)
            for k, v in cnt.items():
                ans += v * (n-v)
        return ans // 2

