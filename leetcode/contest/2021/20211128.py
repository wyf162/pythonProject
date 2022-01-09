# _*_ coding: utf-8 _*_
# @Time : 2021/11/28 上午10:36 
# @Author : wangyefei
# @File : 20211128.py
from typing import List
import math
from collections import defaultdict, deque


class UnionFind(object):
    """并查集类"""

    def __init__(self, n):
        """长度为n的并查集"""
        self.par = [i for i in range(n)]

    def find(self, p):
        """查找p的根结点(祖先)"""
        while self.par[p] >= 0:
            p = self.par[p]
        return p

    def union(self, p, q):
        """连通p,q 让q指向p"""



class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        if n < 2 * k + 1:
            return ans
        s = sum(nums[0:2 * k + 1])
        for i in range(k, n - k):
            ans[i] = math.floor(s / (2 * k + 1))
            if i + k + 1 < n:
                s = s - nums[i - k] + nums[i + k + 1]
        return ans

    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(max(nums))
        j = nums.index(min(nums))
        print(i, j, n)
        if i > j:
            i, j = j, i
        return min(j + 1, n - i, i + 1 + n - j)

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        m = len(meetings)
        meetings.sort(key=lambda x: x[2])

        secret = [False] * n
        secret[0] = secret[firstPerson] = True

        i = 0
        while i < m:
            # meetings[i .. j] 为同一时间
            j = i
            while j + 1 < m and meetings[j + 1][2] == meetings[i][2]:
                j += 1

            vertices = set()
            edges = defaultdict(list)
            for k in range(i, j + 1):
                x, y = meetings[k][0], meetings[k][1]
                vertices.update([x, y])
                edges[x].append(y)
                edges[y].append(x)

            q = deque([u for u in vertices if secret[u]])
            while q:
                u = q.popleft()
                for v in edges[u]:
                    if not secret[v]:
                        secret[v] = True
                        q.append(v)

            i = j + 1

        ans = [i for i in range(n) if secret[i]]
        return ans


if __name__ == "__main__":
    sol = Solution()
    # nums = [2, 10, 7, 5, 4, 1, 8, 6]
    nums = [0, -4, 19, 1, 8, -2, -3, 5]
    print(sol.minimumDeletions(nums))
    # nums = [7,4,3,9,1,8,5,2,6]
    # k = 3
    # nums = [100000, 100]
    # k = 1
    # print(sol.getAverages(nums,k))
