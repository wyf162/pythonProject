# _*_ coding: utf-8 _*_
# @Time : 2022/08/21 5:27 PM 
# @Author : yefe
# @File : ubi-quant-20220821

from typing import List
from collections import Counter, defaultdict
from functools import reduce
import math


class Solution:
    def numberOfPairs(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for num in nums:
            x = int(str(num)[::-1]) - num
            cnt[x] += 1

        res = 0
        for k, v in cnt.items():
            res += math.comb(v, 2)

        res %= int(1e9 + 7)
        return res

    def lakeCount(self, field: List[str]) -> int:
        m, n = len(field), len(field[0])
        unvis = [[True if field[i][j] == 'W' else False for j in range(n)] for i in range(m)]

        def dfs(x, y):
            for dx in [-1, 1, 0]:
                for dy in [-1, 1, 0]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and unvis[nx][ny] and field[nx][ny] == 'W':
                        unvis[nx][ny] = False
                        dfs(nx, ny)

        cnt = 0
        for i in range(m):
            for j in range(n):
                if field[i][j] == 'W' and unvis[i][j]:
                    cnt += 1
                    dfs(i, j)
        return cnt

    def minOperations(self, numbers: List[int]) -> int:
        if len(numbers) <= 1:
            return 0
        rets = 0
        lcms = reduce(math.lcm, numbers)
        if lcms == 1:
            return 0
        for num in numbers:
            multi = lcms // num
            if multi % 2 == 0 or multi % 3 == 0:
                while multi > 0 and multi % 2 == 0:
                    multi = multi // 2
                    rets += 1
                while multi > 0 and multi % 3 == 0:
                    multi = multi // 3
                    rets += 1
                if multi > 1:
                    return -1
            else:
                return -1
        return rets

    def chipGame(self, nums: List[int], kind: int) -> float:
        pass


if __name__ == '__main__':
    sol = Solution()

    # numbers = [50, 75, 100]
    numbers = [1, 1]
    ret = sol.minOperations(numbers)
    print(ret)

    # field = [".....W", ".W..W.", "....W.", ".W....", "W.WWW.", ".W...."]
    # ret = sol.lakeCount(field)
    # print(ret)

    # nums = [17, 28, 39, 71]
    # ret = sol.numberOfPairs(nums)
    # print(ret)
