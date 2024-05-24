# -*- coding : utf-8 -*-
# @Time: 2022/6/19 16:42
# @Author: yefei.wang
# @File: 1947_max_compatibility_sum.py
from typing import List
from functools import cache


class Solution:
    def maxCompatibilitySum2(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        tbl = [[0 for j in range(m)] for i in range(m)]

        def compute(s0, s1):
            cnt = 0
            for x, y in zip(s0, s1):
                cnt += 1 if x == y else 0
            return cnt

        for i in range(m):
            for j in range(m):
                tbl[i][j] = compute(students[i], mentors[j])

        ret = 0

        @cache
        def bfs(n, s, ss):
            nonlocal ret
            if n >= m:
                print(ss)
                ret = max(ret, s)
                return
            for i in range(m):
                if (1 << i) & ss:
                    continue
                else:
                    # print(i, n)
                    # print(n + 1, s + tbl[n][i], ss | (1 << i))
                    bfs(n + 1, s + tbl[n][i], ss | (1 << i))

        bfs(0, 0, 0)
        return ret

    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])
        g = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                for k in range(n):
                    g[i][j] += students[i][k] == mentors[j][k]

        f = [0] * (1 << m)
        for mask in range(1, 1 << m):
            c = bin(mask).count('1')
            for i in range(m):
                if mask & (1 << i):
                    f[mask] = max(f[mask], f[mask ^ (1 << i)] + g[c - 1][i])
        return f[-1]


if __name__ == '__main__':
    sol = Solution()
    # students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]
    # mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
    # students = [[0, 1, 0, 1, 1, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 0, 0]]
    # mentors = [[1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 1], [0, 1, 0, 0, 1, 1]]

    # 12
    students = [[1, 1, 0, 1, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 1, 0]]
    mentors = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [0, 0, 1, 1, 0], [1, 1, 0, 0, 0]]
    res = sol.maxCompatibilitySum(students, mentors)
    print(res)
