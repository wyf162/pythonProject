# -*- coding : utf-8 -*-
# @Time: 2022/6/25 22:27
# @Author: yefei.wang
# @File: biweek-81-20220625.py
from collections import defaultdict, deque
from typing import List
from math import gcd


class Solution:
    def countAsterisks(self, s: str) -> int:
        n = len(s)
        i = 0
        st = None
        cnt = 0
        while i < n:
            if st is None and s[i] == '|':
                st = i
            elif st is not None and s[i] == '|':
                st = None
            elif st is None and s[i] == '*':
                cnt += 1

            i += 1
        return cnt

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj_tbl = defaultdict(list)
        for u, v in edges:
            adj_tbl[u].append(v)
            adj_tbl[v].append(u)

        unvis = [True] * n

        cnts = []

        for i in range(n):
            if unvis[i]:
                cnt = 0
                q = deque()
                q.append(i)
                cnt += 1
                unvis[i] = False
                while q:
                    cur = q.popleft()
                    for nx in adj_tbl[cur]:
                        if unvis[nx]:
                            q.append(nx)
                            cnt += 1
                            unvis[nx] = False
                cnts.append(cnt)
        ret = 0
        for cnt in cnts:
            ret += cnt * (n - cnt)
        return ret // 2

    def maximumXOR(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            ret &= num
        return ret

    def distinctSequences(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 1:
            return 6
        if n == 2:
            return 22

        hst = self.helper2()
        # print(hst)
        dp = [[0 for j in range(6)] for i in range(n)]
        dp[0] = [1] * 6
        dp[1] = [5, 3, 4, 3, 5, 2]
        dp[2] = [12, 11, 12, 11, 12, 8]

        for i in range(3, n):
            for j in range(6):
                for k in range(6):
                    # print(k, j, hst.get((k, j)))
                    # if hst.get((k, j)):
                    if j==k:
                        continue
                    dp[i][j] += dp[i - 2][k] * hst.get((k, j))
                dp[i][j] %= MOD
        print(dp)
        return sum(dp[-1]) % MOD

    @staticmethod
    def helper():

        def check(i, j, k, l):
            if gcd(i, j) == 1 and gcd(j, k) == 1 and gcd(k, l) == 1\
                    and i != j and i != k and j != k and j != l and k != l:
                return True
            else:
                return False

        hst = defaultdict(int)

        for i in range(1, 7):
            for j in range(1, 7):
                for k in range(1, 7):
                    for l in range(1, 7):
                        if check(i, j, k, l):
                            hst[(i-1, l-1)] += 1
        return hst

    @staticmethod
    def helper2():

        def check(i, j, k):
            if gcd(i, j) == 1 and gcd(j, k) == 1 and i != j and i != k and j != k:
                return True
            else:
                return False

        hst = defaultdict(int)

        for i in range(1, 7):
            for j in range(1, 7):
                for k in range(1, 7):
                    if check(i, j, k):
                        hst[(i-1, k-1)] += 1
        return hst


def helper2():

    def check(i, j, k):
        if gcd(i, j) == 1 and gcd(j, k) == 1 and i != j and i != k and j != k:
            return True
        else:
            return False

    hst = [0] * 6
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                if check(i, j, k):
                    hst[k-1] += 1
    return hst


if __name__ == '__main__':
    # print(helper2())

    sol = Solution()
    n = 5
    ret = sol.distinctSequences(n)
    print(ret)

    # n = 3
    # edges = [[0, 1], [0, 2], [1, 2]]
    # n = 7
    # edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
    # n = 11
    # edges = [[5, 0], [1, 0], [10, 7], [9, 8], [7, 2], [1, 3], [0, 2], [8, 5], [4, 6], [4, 2]]
    # ret = sol.countPairs(n, edges)
    # print(ret)

    # s = "l|*e*et|c**o|*de|"
    # s = "|**|*|*|**||***||"
    # ret = sol.countAsterisks(s)
    # print(ret)
