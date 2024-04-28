# -*- coding : utf-8 -*-
# @Time: 2024/4/28 10:51
# @Author: yefei.wang
# @File: D.py

from bisect import bisect_left
from typing import List


class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        k = (n * (n + 1) // 2 + 1) // 2

        def check(upper: int) -> bool:
            cnt = l = 0
            freq = Counter()
            for r, in_ in enumerate(nums):
                freq[in_] += 1
                while len(freq) > upper:
                    out = nums[l]
                    freq[out] -= 1
                    if freq[out] == 0:
                        del freq[out]
                    l += 1
                cnt += r - l + 1
                if cnt >= k:
                    return True
            return False

        return bisect_left(range(len(set(nums))), True, 1, key=check)


if __name__ == '__main__':
    sol = Solution()
    nums = [15, 86, 69, 20, 20, 69, 86, 20, 86]
    ret = sol.medianOfUniquenessArray(nums)
    print(ret)
