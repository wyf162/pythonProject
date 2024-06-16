# -*- coding : utf-8 -*-
# @Time: 2024/6/16 11:07
# @Author: yefei.wang
# @File: B.py
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = [0] * 24
        ans = 0
        for h1 in hours:
            h1 %= 24
            h2 = (24 - h1) % 24
            ans += cnt[h2]
            cnt[h1] += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    hours = [13, 11]
    ret = sol.countCompleteDayPairs(hours)
    print(ret)
