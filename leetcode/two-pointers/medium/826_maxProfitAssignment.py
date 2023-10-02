# -*- coding : utf-8 -*-
# @Time: 2023/9/30 18:43
# @Author: yefei.wang
# @File: 826_maxProfitAssignment.py
import bisect
from collections import Counter
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        d_p = list(zip(difficulty, profit))
        d_p.sort()

        cnt = Counter()
        mp = 0
        for d, p in d_p:
            mp = max(mp, p)
            cnt[d] = mp
        ds = list(sorted(difficulty))
        ans = 0
        for w in worker:
            i = bisect.bisect_right(ds, w)
            if i >= 1:
                ans += cnt[ds[i - 1]]
        return ans
