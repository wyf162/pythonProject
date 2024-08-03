# -*- coding : utf-8 -*-
# @Time: 2024/8/3 22:54
# @Author: yefei.wang
# @File: D.py

from typing import List


class SegmentTreeMax:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.seg = [0] * (n * 4)
        self.build(nums, 0, 0, n - 1)

    def build(self, nums: List[int], node: int, s: int, e: int):
        if s == e:
            self.seg[node] = nums[s]
            return
        m = s + (e - s) // 2
        self.build(nums, node * 2 + 1, s, m)
        self.build(nums, node * 2 + 2, m + 1, e)
        self.seg[node] = max(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def update(self, index: int, val: int, node: int, s: int, e: int):
        if s == e:
            self.seg[node] = val
            return
        m = s + (e - s) // 2
        if index <= m:
            self.update(index, val, node * 2 + 1, s, m)
        else:
            self.update(index, val, node * 2 + 2, m + 1, e)
        self.seg[node] = max(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def query(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:
            return self.seg[node]
        m = s + (e - s) // 2
        if right <= m:
            return self.query(left, right, node * 2 + 1, s, m)
        if left > m:
            return self.query(left, right, node * 2 + 2, m + 1, e)
        return max(self.query(left, m, node * 2 + 1, s, m), self.query(m + 1, right, node * 2 + 2, m + 1, e))


class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        in_seq = [0] * n
        out_seq = [0] * n
        ts = 0
        stk = [(0, -1, 0)]
        parent = [-1] * n
        dfs = []
        dp = [0] * n
        dp[0] = 0
        while stk:
            x, fa, flag = stk.pop()
            dfs.append(x)
            if flag == 0:
                in_seq[x] = ts
                ts += 1
                stk.append([x, fa, 1])
                for y in g[x]:
                    if y != fa:
                        stk.append([y, x, 0])
                        parent[y] = x
                        if y % 2:
                            dp[y] = dp[x] + 1
                        else:
                            dp[y] = dp[x] + 2
            else:
                out_seq[x] = ts
                ts += 1

        print(dp)
        print(in_seq)
        print(out_seq)

        A = [0] * (2 * n)
        for i in range(n):
            A[in_seq[i]] = dp[i]
            A[out_seq[i]] = dp[i]

        Lst = SegmentTreeMax(A)

        dp2 = [0] * n
        for x in dfs:
            fa = parent[x]
            if fa == -1:
                continue
            dp2[x] = dp[fa] + 1 if fa % 2 else 2

        ans = [0] * n
        ans[0] = max(dp)
        for x in range(1, n):
            mx1 = Lst.query(in_seq[x], out_seq[x], 0, 0, 2 * n - 1)
            ret1 = mx1 - dp[x]

            ret2 = ret3 = 0
            if in_seq[x] - 1 >= 0:
                mx2 = Lst.query(0, in_seq[x] - 1, 0, 0, 2 * n - 1)
                ret2 = mx2 + dp2[x]

            if out_seq[x] + 1 <= 2 * n - 1:
                mx3 = Lst.query(out_seq[x] + 1, 2 * n - 1, 0, 0, 2 * n - 1)
                ret2 = mx3 + 1 if parent[x] % 2 else 2
            ans[x] = max(ret1, ret2, ret3)
        return ans


if __name__ == '__main__':
    sol = Solution()
    # edges = [[0, 1], [0, 2]]
    edges = [[2, 4], [0, 1], [2, 3], [0, 2]]
    # edges = [[0, 1]]
    ret = sol.timeTaken(edges)
    print(ret)
