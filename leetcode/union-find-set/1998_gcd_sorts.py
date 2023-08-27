# _*_ coding: utf-8 _*_
# @Time : 2022/08/13 11:44 AM 
# @Author : yefe
# @File : 1998_gcd_sorts
from collections import defaultdict
from functools import reduce
from typing import List, Set
from math import gcd


class UnionFind:

    def __init__(self, s: Set):
        self.parent = {v: v for v in s}

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x < root_y:
            self.parent[root_y] = root_x
            return root_x
        else:
            self.parent[root_x] = root_y
            return root_y

    def are_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


N = 10 ** 5
prime = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    p, x = 2, i
    while p * p <= x:
        if x % p == 0:
            prime[i].append(p)
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        prime[i].append(x)


class Solution:

    def gcdSort(self, nums: List[int]) -> int:
        s = set(nums)
        uf = UnionFind(s)
        dic = defaultdict(list)
        for i, num in enumerate(nums):
            for p in prime[num]:
                dic[p].append(num)

        for v in dic.values():
            reduce(uf.merge, v)

        ordered_nums = sorted(nums)
        for x, y in zip(ordered_nums, nums):
            if uf.are_connected(x, y):
                continue
            else:
                # print(x, y)
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    nums = [10, 3, 9, 6, 8]
    ret = sol.gcdSort(nums)
    print(ret)
