# -*- coding: utf-8 -*-
# @Time: 2024/4/15 10:43
# @Author: yfwang
# @File: 3116.py

from typing import List
import math


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        dp = [0] * (1 << n)
        for x in range(1, 1 << n):
            y = 1
            for i in range(n):
                if x >> i & 1:
                    y = math.lcm(y, coins[i])
            dp[x] = y

        def check(val):
            cnt = 0
            for x in range(1, 1 << n):
                if x.bit_count() % 2 == 1:
                    cnt += val // dp[x]
                else:
                    cnt -= val // dp[x]
            return cnt

        ans = 0
        L, R = 0, 1 << 60
        while L <= R:
            mid = (L + R) // 2
            if check(mid) >= k:
                ans = mid
                R = mid - 1
            else:
                L = mid + 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    coins = [5, 2]
    k = 7
    ret = sol.findKthSmallest(coins, k)
    print(ret)
