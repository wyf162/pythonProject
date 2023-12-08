# -*- coding : utf-8 -*-
# @Time: 2023/12/3 10:29
# @Author: yefei.wang
# @File: D.py
from typing import List
import math


class Combinatorics:
    def __init__(self, n, mod):
        n += 10
        self.perm = [1] * n
        self.rev = [1] * n
        self.mod = mod
        for i in range(1, n):
            # (i!) % mod
            self.perm[i] = self.perm[i - 1] * i
            self.perm[i] %= self.mod
        self.rev[-1] = self.mod_reverse(self.perm[-1], self.mod)  # equal to pow(self.perm[-1], -1, self.mod)
        for i in range(n - 2, 0, -1):
            self.rev[i] = (self.rev[i + 1] * (i + 1) % mod)  # pow(i!, -1, mod)
        self.fault = [0] * n
        self.fault_perm()
        return

    def ex_gcd(self, a, b):
        if b == 0:
            return 1, 0, a
        else:
            x, y, q = self.ex_gcd(b, a % b)
            x, y = y, (x - (a // b) * y)
            return x, y, q

    def mod_reverse(self, a, p):
        assert math.gcd(a, p) == 1
        x, y, q = self.ex_gcd(a, p)
        return (x + p) % p

    def comb(self, a, b):
        if a < b:
            return 0
        # C(a, b) % mod
        res = self.perm[a] * self.rev[b] * self.rev[a - b]
        return res % self.mod

    def factorial(self, a):
        # (a!) % mod
        res = self.perm[a]
        return res % self.mod

    def fault_perm(self):
        # number of fault combinations
        self.fault[0] = 1
        self.fault[2] = 1
        for i in range(3, len(self.fault)):
            self.fault[i] = (i - 1) * (self.fault[i - 1] + self.fault[i - 2])
            self.fault[i] %= self.mod
        return

    def inv(self, n):
        # pow(n, -1, mod)
        return self.perm[n - 1] * self.rev[n] % self.mod

    def catalan(self, n):
        return (self.comb(2 * n, n) - self.comb(2 * n, n - 1)) % self.mod


class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        mod = 10 ** 9 + 7
        nums1 = []
        nums2 = []
        if sick[0] > 0:
            nums1.append(sick[0] - 0)
        if sick[-1] < n - 1:
            nums1.append(n - 1 - sick[-1])

        for i in range(1, len(sick)):
            p = sick[i] - sick[i - 1] - 1
            if p > 0:
                nums2.append(p)

        cb = Combinatorics(10 ** 5 + 5, 10 ** 9 + 7)

        cur = 0
        rst = 1
        for people in nums1:
            rst *= cb.comb(cur + people, people)
            rst %= mod
            cur += people

        for people in nums2:
            rst *= cb.comb(cur + people, people)
            rst *= pow(2, people - 1, mod)
            rst %= mod
            cur += people
        return rst


if __name__ == '__main__':
    sol = Solution()
    n = 5
    sick = [0, 4]
    # n = 4
    # sick = [1]
    ret = sol.numberOfSequence(n, sick)
    print(ret)
