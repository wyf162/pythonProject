# -*- coding : utf-8 -*-
# @Time: 2024/6/9 10:55
# @Author: yefei.wang
# @File: D.py

import sys
from typing import List

from sortedcontainers import SortedSet

sys.set_int_max_str_digits(999999999)


class Solution:
    def maxTotalReward_bf(self, rewardValues: List[int]) -> int:
        rewardValues = list(set(rewardValues))
        rewardValues.sort()
        sl = SortedSet()
        sl.add(0)
        for x in rewardValues:
            j = sl.bisect_left(x)
            for i in range(j):
                sl.add(sl[i] + x)
        ans = sl[-1]
        return ans

    def maxTotalReward(self, a: List[int]) -> int:
        a.sort()
        x = 1
        for i in a:
            x = (x & (1 << i) - 1) << i | x
        res = 0
        for i in range(max(a) * 2):
            if x >> i & 1:
                res = i
        return res

    def maxTotalReward2(self, rewardValues: List[int]) -> int:
        mx = max(rewardValues)
        MASK = (1 << (mx * 2 + 1)) - 1
        dp = 1
        for x in sorted(rewardValues):
            mask = (1 << x) - 1
            val = dp & mask
            dp |= (val << x) | (1 << x)
            dp &= MASK

        return dp.bit_length() - 1


if __name__ == '__main__':
    # rewardValues = [1, 1, 3, 3]
    # rewardValues = [1, 2, 4, 8, 16]
    # rewardValues = [10, 4, 9, 18]
    # rewardValues = [1, 6, 4, 3, 2]
    rewardValues = [i + 1 for i in range(5 * 10 ** 4)]
    # rewardValues = [random.randint(1, 10000) for _ in range(100)]
    ret1 = Solution().maxTotalReward_bf(rewardValues)
    print(ret1)
    # ret2 = Solution().maxTotalReward(rewardValues)
    # print(ret1, ret2)
