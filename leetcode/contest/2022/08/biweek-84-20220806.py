# -*- coding : utf-8 -*-
# @Time: 2022/8/6 22:32
# @Author: yefei.wang
# @File: biweek-84-20220806.py
import math
from typing import List
from collections import defaultdict, Counter
from math import comb


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hst = defaultdict(int)
        for k, v in items1:
            hst[k] += v
        for k, v in items2:
            hst[k] += v

        ans = [[k, v] for k, v in hst.items()]
        ans.sort()
        return ans

    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = comb(n, 2)
        nums = [num - i for i, num in enumerate(nums)]
        counter = Counter(nums)
        print(counter)
        for k, v in counter.items():
            ans -= comb(v, 2)
        return ans

    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        hst = defaultdict(int)
        cur = 0
        for task in tasks:
            if hst[task] == 0:
                cur += 1
                hst[task] = cur
            else:
                if hst[task] + space < cur:
                    cur += 1
                    hst[task] = cur
                else:
                    cur = hst[task] + space + 1
                    hst[task] = cur
        return cur

    def minimumReplacement(self, nums: List[int]) -> int:
        nums.reverse()
        prev = nums[0]
        res = 0
        for i in nums:
            if i <= prev:
                prev = i
            else:
                n = math.ceil(i / prev)
                res += n - 1
                prev = i // n
        return res


if __name__ == '__main__':
    sol = Solution()
    tasks = [1, 2, 1, 2, 3, 1]
    space = 3
    ret = sol.taskSchedulerII(tasks, space)
    print(ret)

    # nums = [4, 1, 3, 3]
    # nums = [1, 2, 3, 4, 5]
    # nums = [1, 2, 2]
    # ret = sol.countBadPairs(nums)
    # print(ret)
