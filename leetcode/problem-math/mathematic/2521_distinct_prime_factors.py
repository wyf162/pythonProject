# _*_ coding: utf-8 _*_
# @Time : 2023/01/02 9:09 PM 
# @Author : yefe
# @File : 2521_distinct_prime_factors

from typing import List

is_prime = [True] * 1001
is_prime[0] = False
is_prime[1] = False
for i in range(2, 1001):
    j = 2
    while i * j < 1001:
        is_prime[i * j] = False
        j += 1


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = [False] * 1001
        for x in nums:
            i = 2
            while i * i <= x:
                if x % i == 0:
                    factors[i] = True
                    factors[x//i] = True
                i += 1
        ans = 0
        for i in range(1001):
            if is_prime[i] and factors[i]:
                ans += 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 4, 3, 7, 10, 6]
    ret = sol.distinctPrimeFactors(nums)
    print(ret)
