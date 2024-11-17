# -*- coding : utf-8 -*-
# @Time: 2024/8/25 10:31
# @Author: yefei.wang
# @File: B.py
from collections import Counter
from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        hst = Counter()
        ans = 0
        for i in range(n):
            s = list(str(nums[i]))
            ans += hst[nums[i]]
            for i1 in range(len(s)):
                for i2 in range(i1 + 1, len(s)):
                    s[i1], s[i2] = s[i2], s[i1]
                    x = int(''.join(s))
                    if x == nums[i]:
                        s[i1], s[i2] = s[i2], s[i1]
                        continue
                    ans += hst[x]
                    s[i1], s[i2] = s[i2], s[i1]
                    # print(int(''.join(s)) == nums[i])
            hst[nums[i]] += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums = [3, 12, 30, 17, 21]
    # nums = [5, 12, 8, 5, 5, 1, 20, 3, 10, 10, 5, 5, 5, 5, 1]
    nums = [11, 13, 11, 14, 11]
    nums.sort()
    print(nums)
    ret = sol.countPairs(nums)
    print(ret)
