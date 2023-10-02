# -*- coding : utf-8 -*-
# @Time: 2023/9/28 21:53
# @Author: yefei.wang
# @File: 2246_longestPath.py

from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        e = [[] for _ in range(n)]
        for i in range(1, n):
            e[parent[i]].append(i)
        ans = 0

        # 返回节点i向下的一条合法链的最大长度（边的长度）
        def dfs(i):
            mx1, mx2 = 0, 0
            for j in e[i]:
                res = dfs(j) + 1
                # 当j不满足条件时，就无法连成一个合法的链，满足则更新
                if s[j] != s[i]:
                    if res >= mx1:
                        mx2 = mx1
                        mx1 = res
                    elif res > mx2:
                        mx2 = res
            nonlocal ans
            ans = max(ans, mx1 + mx2)
            return mx1

        dfs(0)
        # 由于需要返回节点的个数，所以需要边数+1
        return ans + 1


if __name__ == '__main__':
    sol = Solution()
    parent = [-1] + [0] * 100000
    s = "d" * 100001
    ret = sol.longestPath(parent, s)
    print(ret)
