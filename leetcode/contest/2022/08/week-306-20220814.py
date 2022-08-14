# _*_ coding: utf-8 _*_
# @Time : 2022/08/14 10:27 AM 
# @Author : yefe
# @File : week-306-20220814
import math
from collections import defaultdict, deque
from functools import cache
from typing import List
from sortedcontainers.sortedlist import SortedList


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        n = len(grid)

        mtx = [[0 for j in range(n - 2)] for i in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        mtx[i][j] = max(mtx[i][j], grid[i + 1 + dx][j + 1 + dy])
        return mtx

    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)

        scores = [0] * n
        for u, v in enumerate(edges):
            scores[v] += u

        m = max(scores)
        idx = scores.index(m)
        return idx

    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern) + 1

        hst = defaultdict(list)
        deg = [0] * n
        for idx, p in enumerate(pattern):
            if p == 'I':
                hst[idx].append(idx + 1)
                deg[idx + 1] += 1
            else:
                hst[idx + 1].append(idx)
                deg[idx] += 1

        zero_deg = list()
        for i, d in enumerate(deg):
            if d == 0:
                zero_deg.append(i)

        ans = [0] * n
        num = 1
        while zero_deg:
            zero_deg.sort()
            i = zero_deg[0]
            zero_deg.pop(0)
            ans[i] = num
            num += 1
            for nx in hst[i]:
                deg[nx] -= 1
                if deg[nx] == 0:
                    zero_deg.append(nx)
        return ''.join([str(x) for x in ans])

    def countSpecialNumbers(self, n: int) -> int:
        if n <= 9:
            return n

        nums = []
        while n > 0:
            nums.insert(0, n % 10)
            n = n // 10
        print(nums)

        #  记录数字n的位数
        c = len(nums)
        print([compute(i) for i in range(1, c)])
        base = sum([compute(i) for i in range(1, c)])
        print('base:', base)

        valid = [True] * c
        for i in range(c):
            if nums[i] not in nums[:i]:
                valid[i] = True
            else:
                valid[i] = False

        bonus = 0
        for i, num in enumerate(nums):
            if i == c - 1 and valid[i-1]:
                bonus += len([x for x in range(10) if x not in nums[:i] and x <= num])
                continue
            elif valid[i]:
                for j in range(1, num):
                    bonus += (9 - i) * math.perm(9 - i, c - i - 2)
        print('bonus:', bonus)
        return base + bonus


@cache
def compute(n):
    factors = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ret = 1
    for i in range(n):
        ret *= factors[i]
    return ret


if __name__ == '__main__':
    sol = Solution()
    for n in [233]:
        res = sol.countSpecialNumbers(n)
        print(res)
    # pattern = "IIIDIDDD"
    # ret = sol.smallestNumber(pattern)
    # print(ret)
