# -*- coding : utf-8 -*-
# @Time: 2022/8/7 23:25
# @Author: yefei.wang
# @File: 1782_count_pairs.py
from typing import List
from collections import defaultdict
import bisect

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        hst = [0]*n

        for u, v in edges:
            if u < v:
                hst[u-1] += 1
            else:
                hst[v-1] += 1

        print(hst)

        hst.sort()
        print(hst)

        ans = list()
        for query in queries:
            cnt = 0
            for i in range(n):
                j = bisect.bisect_left(hst, query-i)
                cnt += n-j
            ans.append(cnt)
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 4
    edges = [[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]]
    queries = [2, 3]
    ret = sol.countPairs(n, edges, queries)
    print(ret)
