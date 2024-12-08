# _*_ coding: utf-8 _*_
# @Time : 2023/04/01 4:38 PM 
# @Author : yefe
# @File : 2601_prime_sub_operation
import math
import bisect
from typing import List


def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


primes = [2, 3]
for i in range(5, 1001):
    if is_prime(i):
        primes.append(i)


def get_less_n_prime(n):
    # 求小于n的指数
    idx = bisect.bisect_left(primes, n)
    if idx == 0:
        return None
    else:
        return primes[idx - 1]


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        x = get_less_n_prime(nums[0])
        if x:
            nums[0] -= x
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False
            else:
                x = get_less_n_prime(nums[i] - nums[i - 1])
                if x:
                    nums[i] -= x
        print(nums)
        return True


if __name__ == '__main__':
    sol = Solution()
    # nums = [4, 9, 6, 10]
    nums = [18, 12, 14, 6]
    ret = sol.primeSubOperation(nums)
    print(ret)
