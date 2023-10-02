# -*- coding : utf-8 -*-
# @Time: 2023/9/28 19:38
# @Author: yefei.wang
# @File: 1712.py
from itertools import accumulate
from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        pre = list(accumulate(nums))
        ans = 0
        for i in range(n):
            l = max(i+1,bisect_left(pre,pre[i]+pre[i]))
            r = min(n-1,bisect_right(pre,(pre[i]+pre[-1])//2))
            ans = (ans + max(0,r - l)) % mod
        return ans % mod


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1]
    ret = sol.waysToSplit(nums)
    print(ret)
