# -*- coding : utf-8 -*-
# @Time: 2022/1/24 21:49
# @Author: yefei.wang
# @File: 2045_second_mimum.py
import collections
import math
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj_tbl = collections.defaultdict(list)
        for u, v in edges:
            adj_tbl[v].append(u)
            adj_tbl[u].append(v)
        unvisited = [True] * (n + 1)
        q = collections.deque()
        q.append(1)
        unvisited[1] = False
        cnts = set()
        cnt = 0

        while cnt < n:
            cnt += 1
            for i in range(len(q)):
                c = q.popleft()
                for v in adj_tbl.get(c):
                    q.append(v)
                    unvisited[v] = False
                    if v == n:
                        cnts.add(cnt)
        print(cnts)
        cnts = sorted(list(cnts))
        if len(cnts) == 1:
            cnts.append(cnts[0] + 2)
        print(cnts)
        print(n)
        m = cnts[1]
        if time>change:
            n = math.ceil(time/change)
            return n*change*(m-1)+time
        else:
            n = math.floor(change / time)
            if m <= n:
                return m * time
            else:
                k = math.ceil(m / n)-1
                return k * change + (m - n * k) * time


if __name__ == '__main__':
    sol = Solution()
    # n = 5
    # edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
    # time = 3
    # change = 5
    # n = 2
    # edges = [[1, 2]]
    # time = 1
    # change = 2
    n = 6
    edges = [[1, 2], [1, 3], [2, 4], [3, 5], [5, 4], [4, 6]]
    time = 3
    change = 100
    data = sol.secondMinimum(n, edges, time, change)
    print(data)
