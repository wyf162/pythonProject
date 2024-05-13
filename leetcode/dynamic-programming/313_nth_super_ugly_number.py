# _*_ coding: utf-8 _*_
# @Time : 2022/05/14 5:26 PM 
# @Author : yefe
# @File : 313_nth_super_ugly_number
from typing import List
import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * (n+1)
        m = len(primes)
        pointers = [0] * m
        nums = [1]*m

        for i in range(1, n+1):
            min_num = min(nums)
            dp[i] = min_num
            for j in range(m):
                if nums[j] == min_num:
                    pointers[j] += 1
                    nums[j] = dp[pointers[j]] * primes[j]
        return dp[n]

    def nth_super_ugly_number(self, n: int, primes: List[int]) -> int:
        q = [1]
        heapq.heapify(q)
        visited = set()
        visited.add(1)
        n -= 1
        while n:
            x = heapq.heappop(q)
            for prime in primes:
                num = x*prime
                if num not in visited:
                    visited.add(num)
                    heapq.heappush(q, num)
            n -= 1
        return heapq.heappop(q)


if __name__ == '__main__':
    sol = Solution()
    n = 12
    primes = [2, 7, 13, 19]
    # ret = sol.nthSuperUglyNumber(n, primes)
    ret = sol.nth_super_ugly_number(n, primes)
    print(ret)
