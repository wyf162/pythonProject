# -*- coding : utf-8 -*-
# @Time: 2022/7/24 10:19
# @Author: yefei.wang
# @File: week-303-20220724.py
from typing import List
import math


class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        cnt = [0] * 33
        nums = set(nums)
        for num in nums:
            x = bin(num).count('1')
            cnt[x] += 1

        ans = 0

        for i in range(33):
            for j in range(i, 33):
                if i + j >= k:
                    if i == j:
                        ans += math.comb(cnt[i], 2) * 2
                        ans += cnt[i]
                    else:
                        ans += cnt[i] * cnt[j] * 2

        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    ret = sol.countExcellentPairs(nums, k)
    print(ret)
