# _*_ coding: utf-8 _*_
# @Time : 2022/08/20 10:35 AM 
# @Author : yefe
# @File : 1224_max_equal_freq

from typing import List
from collections import Counter


class Solution:

    def maxEqualFreq(self, nums: List[int]) -> int:
        freq, count = Counter(), Counter()

        ans = max_freq = 0
        for i, num in enumerate(nums):
            if count[num]:
                freq[count[num]] -= 1
            count[num] += 1
            max_freq = max(max_freq, count[num])
            freq[count[num]] += 1
            if max_freq == 1 or \
                freq[max_freq] * max_freq + freq[max_freq - 1] * (max_freq - 1) == i + 1 and freq[max_freq] == 1 or \
                freq[max_freq] * max_freq + 1 == i + 1 and freq[1] == 1:
                ans = max(ans, i + 1)
            return ans


if __name__ == '__main__':
    res = False or True and False or False and True
    print(res)
