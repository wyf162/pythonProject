# _*_ coding: utf-8 _*_
# @Time : 2022/08/28 10:28 AM 
# @Author : yefe
# @File : week-308-20220828

from collections import defaultdict, deque
from typing import List
import bisect


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        pres = [0] * (n + 1)
        for i in range(n):
            pres[i + 1] = pres[i] + nums[i]

        print(pres)

        answer = []
        for query in queries:
            idx = bisect.bisect_left(pres, query + 1)
            answer.append(idx - 1)

        return answer

    def removeStars(self, s: str) -> str:
        stk = []
        for a in s:
            if a != '*':
                stk.append(a)
            else:
                if stk:
                    stk.pop()

        return "".join(stk)

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        garbage_types = ['M', 'P', 'G']
        n = len(garbage)
        last_time = defaultdict(int)
        garbage_counts = defaultdict(int)
        for i in range(n):
            for garbage_type in garbage_types:
                if garbage_type in garbage[i]:
                    last_time[garbage_type] = i
                    garbage_counts[garbage_type] += garbage[i].count(garbage_type)

        pres = [0] * n
        for i in range(1, n):
            pres[i] = pres[i - 1] + travel[i - 1]

        ts = 0
        for garbage_type in garbage_types:
            ts += garbage_counts[garbage_type] + pres[last_time[garbage_type]]

        return ts

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def toposort(conditions, k):
            deg = [0] * (k + 1)
            hst = defaultdict(list)
            for u, v in conditions:
                deg[v] += 1
                hst[u].append(v)

            q = deque()
            for i in range(1, k + 1):
                if deg[i] == 0:
                    q.append(i)

            res = []

            while q:
                u = q.popleft()
                res.append(u)
                for v in hst[u]:
                    deg[v] -= 1
                    if deg[v] == 0:
                        q.append(v)
            return res

        rows = toposort(rowConditions, k)
        cols = toposort(colConditions, k)

        if len(rows) < k or len(cols) < k:
            return []

        row_hst = {v: i for i, v in enumerate(rows)}
        col_hst = {v: i for i, v in enumerate(cols)}

        mtx = [[0] * k for _ in range(k)]
        for v in range(1, k + 1):
            mtx[row_hst[v]][col_hst[v]] = v

        return mtx


if __name__ == '__main__':
    sol = Solution()
    # k = 3
    # rowConditions = [[1, 2], [3, 2]]
    # colConditions = [[2, 1], [3, 2]]
    k = 3
    rowConditions = [[1, 2], [2, 3], [3, 1], [2, 3]]
    colConditions = [[2, 1]]

    ret = sol.buildMatrix(k, rowConditions, colConditions)
    print(ret)

    # garbage = ["G", "P", "GP", "GG"]
    # travel = [2, 4, 3]
    #
    # res = sol.garbageCollection(garbage, travel)
    # print(res)

    # s = "leet**cod*e"
    # res = sol.removeStars(s)
    # print(res)

    # nums = [4, 5, 2, 1]
    # queries = [0, 10, 21]
    # rets = sol.answerQueries(nums, queries)
    # print(rets)
