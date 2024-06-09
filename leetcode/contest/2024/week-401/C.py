# -*- coding : utf-8 -*-
# @Time: 2024/6/9 10:35
# @Author: yefei.wang
# @File: C.py

from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        f = [0] * (2001 * 2001)
        ans = 0
        for x in rewardValues:
            f[x] = 1
            ans = max(ans, x)
            for y in range(x):
                if f[y] == 1:
                    f[y + x] = 1
                    ans = max(ans, y + x)
        return ans


if __name__ == '__main__':
    # rewardValues = [1, 1, 3, 3]
    rewardValues = [10, 4, 9, 18]
    ret = Solution().maxTotalReward(rewardValues)
    print(ret)
