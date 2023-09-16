# -*- coding : utf-8 -*-
# @Time: 2022/6/16 23:12
# @Author: yefei.wang
# @File: 532_find_pairs.py
from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hst = Counter(nums)
        cnt = 0
        for num, v in hst.items():
            if k == 0:
                cnt += 1 if hst.get(num) > 1 else 0
            else:
                cnt += 1 if hst.get(num) else 0

        return cnt
