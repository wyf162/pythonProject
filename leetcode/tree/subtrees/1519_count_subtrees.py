# _*_ coding: utf-8 _*_
# @Time : 2022/11/29 9:31 PM 
# @Author : yefe
# @File : 1519_count_subtrees

from typing import List


def idx(s: str) -> int:
    return ord(s) - ord('a')


def add(arr1, arr2: List[int]):
    for i in range(len(arr1)):
        arr1[i] += arr2[i]


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = [0] * n

        def dfs(node, parent) -> List[int]:
            ret = [0] * 26
            ret[idx(labels[node])] += 1
            for child in g[node]:
                if child == parent:
                    continue
                tmp = dfs(child, node)
                add(ret, tmp)
            ans[node] = ret[idx(labels[node])]
            return ret

        dfs(0, -1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 7
    edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    labels = "abaedcd"
    rets = sol.countSubTrees(n, edges, labels)
    print(rets)
