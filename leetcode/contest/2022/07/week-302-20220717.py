# -*- coding : utf-8 -*-
# @Time: 2022/7/17 10:28
# @Author: yefei.wang
# @File: week-302-20220717.py
from typing import List
from collections import Counter, defaultdict
import math


def get_factor(num):
    factors = []
    for_times = int(math.sqrt(num))
    for i in range(1, for_times + 1):
        if num % i == 0:
            factors.append(i)
            t = int(num / i)
            if not t == i:
                factors.append(t)
    return factors


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = [0, 0]
        for k, v in cnt.items():
            ans[0] += v // 2
            ans[1] += v % 2
        return ans

    def maximumSum(self, nums: List[int]) -> int:

        hst = dict()
        ret = -1
        for num in nums:
            bit_sum = self.getSum(num)
            if bit_sum not in hst:
                hst[bit_sum] = [num]
            elif len(hst[bit_sum]) == 1:
                hst[bit_sum].append(num)
                hst[bit_sum].sort(reverse=True)
                if hst[bit_sum][0] + hst[bit_sum][1] > ret:
                    ret = hst[bit_sum][0] + hst[bit_sum][1]
                    print(ret, hst[bit_sum])
            else:
                if num >= hst[bit_sum][0]:
                    hst[bit_sum] = [num, hst[bit_sum][0]]
                elif num > hst[bit_sum][1]:
                    hst[bit_sum][1] = num
                if hst[bit_sum][0] + hst[bit_sum][1] > ret:
                    ret = hst[bit_sum][0] + hst[bit_sum][1]
                    print(ret, hst[bit_sum])
        return ret

    @staticmethod
    def getSum(num):
        s = 0
        while num > 0:
            s += num % 10
            num = num // 10
        return s

    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        hst = dict()
        for query in queries:
            k, trim = query
            if (k, trim) in hst:
                ans.append(hst[(k, trim)])
                continue
            trimed_nums = [num[-1 * trim:] for num in nums]
            trimed_idxed_nums = [(int(num), i) for i, num in enumerate(trimed_nums)]
            trimed_idxed_nums.sort()
            ans.append(trimed_idxed_nums[k - 1][1])
            hst[(k, trim)] = trimed_idxed_nums[k - 1][1]
        return ans

    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        numsDivide = list(set(numsDivide))
        fatctors_0 = get_factor(numsDivide[0])
        fatctors_1 = get_factor(numsDivide[-1])
        factors = set(fatctors_0) & set(fatctors_1)
        for i in range(1, len(numsDivide) - 1):
            divid = numsDivide[i]
            pops = set()
            for factor in factors:
                if divid % factor == 0:
                    continue
                else:
                    pops.add(factor)
            for factor in pops:
                factors.remove(factor)
            if not factors:
                break

        if not factors:
            return -1

        nums.sort()
        for i, num in enumerate(nums):
            if num in factors:
                return i
        return -1


if __name__ == '__main__':
    sol = Solution()
    # nums = [2, 3, 2, 4, 3]
    # numsDivide = [9, 6, 9, 3, 15]
    # nums = [2, 3, 3, 18, 3, 2, 3, 16]
    # numsDivide = [573595257, 616368999, 782586708, 555836748, 128826519, 10729950, 660848235, 459842193, 986538021, 509885907]
    nums = [14, 14, 8, 14, 14]
    numsDivide = [630016464, 481269348, 8818796]

    ret = sol.minOperations(nums, numsDivide)
    print(ret)


    # nums = [18, 43, 36, 13, 7]
    # ret = sol.maximumSum(nums)
    # print(ret)
    # nums = [229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401]
    # for num in nums:
    #     print(sol.getSum(num))
    #
    # ret = sol.maximumSum(nums)
    # print(ret)
    # nums = ["102", "473", "251", "814"]
    # queries = [[1, 1], [2, 3], [4, 2], [1, 2]]
    #
    # ret = sol.smallestTrimmedNumbers(nums, queries)
    # print(ret)
