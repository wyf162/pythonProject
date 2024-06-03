# -*- coding : utf-8 -*-
# @Time: 2024/6/3 21:39
# @Author: yefei.wang
# @File: 895D.py

import sys


class Factorial:
    def __init__(self, N, mod) -> None:
        N += 1
        self.mod = mod
        self.f = [1 for _ in range(N)]
        self.g = [1 for _ in range(N)]
        for i in range(1, N):
            self.f[i] = self.f[i - 1] * i % self.mod
        self.g[-1] = pow(self.f[-1], mod - 2, mod)
        for i in range(N - 2, -1, -1):
            self.g[i] = self.g[i + 1] * (i + 1) % self.mod

    def fac(self, n):
        return self.f[n]

    def fac_inv(self, n):
        return self.g[n]

    def combi(self, n, m):
        if n < m or m < 0 or n < 0: return 0
        return self.f[n] * self.g[m] % self.mod * self.g[n - m] % self.mod

    def permu(self, n, m):
        if n < m or m < 0 or n < 0: return 0
        return self.f[n] * self.g[n - m] % self.mod

    def catalan(self, n):
        return (self.combi(2 * n, n) - self.combi(2 * n, n - 1)) % self.mod

    def inv(self, n):
        return self.f[n - 1] * self.g[n] % self.mod


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007

fact = Factorial(10 ** 1, mod)

tcn = 1
for _tcn_ in range(tcn):
    s = input()
    t = input()
    nums = [0] * 26
    for c in s:
        nums[ord(c) - ord('a')] += 1
    n = len(s)
    tot = fact.fac(n)
    for j in range(26):
        tot *= fact.fac_inv(nums[j])
    print(tot)


    def f(ss, cnt):
        nums = [0] * 26
        for c in ss:
            nums[ord(c) - ord('a')] += 1

        ans = 0
        n = len(s)
        for i in range(n):
            cur = ord(s[i]) - ord('a')
            for j in range(cur):
                if nums[j] == 0:
                    continue
                ans += cnt * fact.fac(n - j - 1) * fact.fac_inv(n - j) * fact.fac(nums[j]) * fact.fac_inv(nums[j] - 1)
                ans %= mod
            cnt = cnt * fact.fac(n - i - 1) * fact.fac_inv(n - i) * fact.fac(nums[i]) * fact.fac_inv(nums[i] - 1)
            cnt %= mod
            nums[cur] -= 1
        return ans


    ans1 = f(s, tot)
    ans2 = f(s, tot)
    print(ans1, ans2)
    ans0 = ans2 - ans1 - 0
    print(ans0)
