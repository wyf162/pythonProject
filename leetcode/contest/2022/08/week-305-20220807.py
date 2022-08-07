# -*- coding : utf-8 -*-
# @Time: 2022/8/7 10:20
# @Author: yefei.wang
# @File: week-305-20220807.py
from typing import List
from collections import deque, defaultdict


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        s = set(nums)
        for num in nums:
            if num - diff in s and num + diff in s:
                ans += 1
        return ans

    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        adj_tbl = defaultdict(list)
        for u, v in edges:
            adj_tbl[v].append(u)
            adj_tbl[u].append(v)

        q = deque()
        q.append(0)
        ans = 1
        vis = set()
        vis.add(0)

        res = set(restricted)

        while q:
            u = q.popleft()
            for v in adj_tbl[u]:
                if v not in res and v not in vis:
                    q.append(v)
                    ans += 1
        return ans

    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        pre = [0] * n
        one, two, three = 0, -1, -1
        for i in range(1, n):
            d = nums[i] - nums[i - 1]
            if d > 1:
                return False
            elif d == 1:
                pre[i] = pre[i - 1] + d
                if pre[i] % 3 == 1:
                    if i - one == 1:
                        return False
                    one = i
                elif pre[i] % 3 == 2:
                    if two < 0:
                        two = i
                        continue
                    if i - two == 1:
                        return False
                    two = i
                elif pre[i] % 3 == 0:
                    if i - three == 1:
                        return False
                    three = i
        return True

    def longestIdealString2(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[0 for j in range(26)] for i in range(n + 1)]

        for i in range(n):
            j = ord(s[i]) - ord('a')
            begin = max(0, j - k)
            end = min(j + k, 25)
            for pre in range(begin, end + 1):
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][pre] + 1)
            for j in range(26):
                dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])
        return max(dp[-1])

    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0 for j in range(26)]

        for i in range(n):
            j = ord(s[i]) - ord('a')
            begin = max(0, j - k)
            end = min(j + k, 25)

            dp[j] = max(dp[x] + 1 for x in range(begin, end+1))
        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    # nums = [4, 4, 4, 5, 6]
    # nums = [1, 2, 3]
    # nums = [579611, 579611, 579611, 731172, 731172, 496074, 496074, 496074, 151416, 151416, 151416]
    # ret = sol.validPartition(nums)
    # print(ret)

    s = "acfgbd"
    k = 2
    ret = sol.longestIdealString(s, k)
    print(ret)
