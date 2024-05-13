# _*_ coding: utf-8 _*_
# @Time : 2022/2/22 下午9:52 
# @Author : wangyefei
# @File : 1994_number_of_good_subsets.py
import math
from collections import Counter, defaultdict
from typing import List


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mod = 10 ** 9 + 7

        freq = Counter(nums)
        f = [0] * (1 << len(primes))
        f[0] = pow(2, freq[1], mod)

        for i, occ in freq.items():
            if i == 1:
                continue

            # 检查 i 的每个质因数是否均不超过 1 个
            subset, x = 0, i
            check = True
            for j, prime in enumerate(primes):
                if x % (prime * prime) == 0:
                    check = False
                    break
                if x % prime == 0:
                    subset |= (1 << j)

            if not check:
                continue

            # 动态规划
            for mask in range((1 << len(primes)) - 1, 0, -1):
                if (mask & subset) == subset:
                    f[mask] = (f[mask] + f[mask ^ subset] * occ) % mod

        ans = sum(f[1:]) % mod
        return ans

    def number_of_good_subsets(self, nums: List[int]) -> int:
        ct, mod = Counter(nums), 10 ** 9 + 7
        d = defaultdict(int)
        d[1] = (1 << ct[1]) % mod
        for num in [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]:
            for x in list(d):
                if math.gcd(num, x) == 1:
                    d[num * x] += ct[num] * d[x]
                    d[num * x] %= mod
        print(d)
        return (sum(d.values()) - d[1]) % mod


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,30]
    ret = sol.number_of_good_subsets(nums)
    print(ret)