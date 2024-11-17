
from typing import List
import typing


class DSU:
    '''
    Implement (union by size) + (path halving)

    Reference:
    Zvi Galil and Giuseppe F. Italiano,
    Data structures and algorithms for disjoint set union problems
    '''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n

        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]]
            )

        return a

    def size(self, a: int) -> int:
        assert 0 <= a < self._n

        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> typing.List[typing.List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]

        result: typing.List[typing.List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        uf = DSU(n)
        for a, b in invocations:
            g[a].append(b)
            uf.merge(a, b)

        vis = [0] * n

        def dfs(x, fa):
            vis[x] = 1
            for y in g[x]:
                if y != fa and not vis[y]:
                    dfs(y, x)

        dfs(k, -1)
        # print(vis)

        ret = []
        for group in uf.groups():
            tot = sum(vis[x] for x in group)
            if tot == 0:
                ret.extend(group)
            elif tot == len(group):
                continue
            else:
                ret = list(range(n))
                break
        return ret


if __name__ == "__main__":
    sol = Solution()
    # n = 4
    # k = 1
    # invocations = [[1, 2], [0, 1], [3, 2]]
    n = 3
    k = 2
    invocations = [[1, 2], [0, 1], [2, 0]]
    ret = sol.remainingMethods(n, k, invocations)
    print(ret)
