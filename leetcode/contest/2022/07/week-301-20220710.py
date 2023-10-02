# -*- coding : utf-8 -*-
# @Time: 2022/7/10 10:29
# @Author: yefei.wang
# @File: week-301-20220710.py
from functools import cache
from typing import List
import heapq
import math


class SmallestInfiniteSet:

    def __init__(self):
        self.ps = set()
        self.p = []
        heapq.heapify(self.p)

    def popSmallest(self) -> int:
        i = 1
        while True:
            if i in self.ps:
                i += 1
            else:
                self.ps.add(i)
                return i

    def addBack(self, num: int) -> None:
        if num in self.ps:
            self.ps.remove(num)


MOD = 10**9+7


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        x, y, z = amount
        if x + y >= z:
            return (x + y + z + 1) >> 1
        else:
            return z

    def canChange(self, start: str, target: str) -> bool:

        def transform(s):
            n = len(s)
            cnt = 0
            ss = ""
            for i in range(n):
                if s[i] == 'R':
                    cnt += 1
                elif s[i] == '_':
                    ss += "_"
                else:
                    ss = ss + "R" * cnt + "L"
                    cnt = 0
            ss = ss + "R" * cnt
            s = ss
            ss = ""
            cnt = 0
            for i in range(n - 1, -1, -1):
                if s[i] == 'L':
                    cnt += 1
                elif s[i] == '_':
                    ss = "_" + ss
                else:
                    ss = "R" + "L" * cnt + ss
                    cnt = 0
            ss = "L" * cnt + ss
            return ss

        n_start = transform(start)

        n_target = transform(target)
        print(n_start)
        print(n_target)
        return n_start == n_target

    def idealArrays(self, n: int, maxValue: int) -> int:
        m = maxValue
        dp = [0]*(m+1)
        for i in range(1, m+1):
            for j in range(1,m+1):
                k = i*j
                if k<=m:
                    dp[k] += 1
                else:
                    break
        ans = 0
        for i in range(1, m+1):
            ans += f(n-1, dp[i])
            ans %= MOD
        return int(ans)



@cache
def f(n, m):
    res = 0
    u = min(n, m)
    for i in range(1, u+1):
        res += c(n-1, i-1)*c(m, i)
        res %= MOD
    return res


@cache
def c(n, k):
    return int(math.factorial(n)/(math.factorial(n-k)*math.factorial(k)))


if __name__ == '__main__':
    sol = Solution()
    # print(c(1,0))
    # print(c(6,1))
    # n, maxValue = 5, 9  # 111
    # n, maxValue = 2, 5  # 10
    n, maxValue = 5, 3  # 11

    ret = sol.idealArrays(n, maxValue)
    print(ret)
    # start = "_L__R__R_"
    # target = "L______RR"
    # start = "_R"
    # target = "R_"
    # ret = sol.canChange(start, target)
    # print(ret)
