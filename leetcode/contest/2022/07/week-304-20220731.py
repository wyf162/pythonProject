# -*- coding : utf-8 -*-
# @Time: 2022/7/31 10:29
# @Author: yefei.wang
# @File: week-304-20220731.py
from typing import List
from collections import deque


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = [num for num in nums if num > 0]
        ans = 0
        while nums:
            nums.sort()
            x = nums[0]
            nums = [num for num in nums if num - x > 0]
            ans += 1
        return ans

    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        s = 0
        l = 1
        while s + l <= n:
            s += l
            l += 1
        return l - 1

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        dis1 = [-1] * n
        dis = 0
        node = node1
        while True:
            if node > -1 and dis1[node] == -1:
                dis1[node] = dis
                node = edges[node]
                dis += 1
            else:
                break

        dis2 = [-1] * n
        dis = 0
        node = node2
        while True:
            if node > -1 and dis2[node] == -1:
                dis2[node] = dis
                node = edges[node]
                dis += 1
            else:
                break

        ans = None
        ret = None
        for i in range(n):
            if dis1[i] > -1 and dis2[i] > -1:
                if ans is None:
                    ans = max(dis1[i], dis2[i])
                    ret = i
                elif max(dis1[i], dis2[i]) < ans:
                    ans = max(dis1[i], dis2[i])
                    ret = i
                elif max(dis1[i], dis2[i]) == ans and ret > i:
                    ans = max(dis1[i], dis2[i])
                    ret = i
        return ret if ret is not None else -1

    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ans = -1
        unvis = [True] * n
        dis = [-1] * n

        for i in range(n):
            if unvis[i]:
                cur = i
                cnt = i+1
                dis[i] = cnt
                while True:
                    unvis[cur] = False
                    cur = edges[cur]
                    cnt += 1
                    if cur > -1 and dis[cur] > i:
                        ans = max(ans, cnt - dis[cur])
                        break
                    elif cur > -1:
                        dis[cur] = cnt
                    else:
                        break

        return ans


if __name__ == '__main__':
    sol = Solution()

    edges = [3, 3, 4, 2, 3]
    # edges = [2, -1, 3, 1]
    # edges = [1, 0, 2, 4, 3]
    # edges = [-1, 4, -1, 2, 0, 4]
    # edges = [1, 2, 0]
    ret = sol.longestCycle(edges)
    print(ret)

    # edges = [2, 2, 3, -1]
    # node1 = 0
    # node2 = 1
    # edges = [1, 2, 0]
    # node1 = 0
    # node2 = 2
    #
    # ret = sol.closestMeetingNode(edges, node1, node2)
    # print(ret)

    # nums = [47, 2, 16, 17, 41, 4, 38, 23, 47]
    # ret = sol.maximumGroups(nums)
    # print(ret)

    # nums = [1, 5, 0, 3, 5]
    # nums = [1,2,3,5]
    # ret = sol.minimumOperations(nums)
    # print(ret)
