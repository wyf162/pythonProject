# -*- coding : utf-8 -*-
# @Time: 2024/1/28 10:34
# @Author: yefei.wang
# @File: B.py

from collections import Counter
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        nums = sorted(cnt.keys())
        ans = 0
        vis = set()
        for num in nums:
            x = num
            if num == 1:
                if cnt[num] % 2 == 1:
                    ans = max(ans, cnt[x])
                else:
                    ans = max(ans, cnt[x] - 1)
                vis.add(x)
                continue
            if x in vis:
                continue
            c = 0
            while cnt[x]:
                vis.add(x)
                if cnt[x] >= 2:
                    c += 2
                    x *= x
                else:
                    c += 1
                    break
            if c % 2 == 1:
                ans = max(ans, c)
            else:
                ans = max(ans, c - 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums = [5, 4, 1, 2, 2]
    nums = [1, 1]
    ret = sol.maximumLength(nums)
    print(ret)
