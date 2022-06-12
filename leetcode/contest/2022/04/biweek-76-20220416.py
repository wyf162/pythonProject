# _*_ coding: utf-8 _*_
# @Time : 2022/4/16 下午10:28 
# @Author : wangyefei
# @File : biweek-76-20220416.py
from typing import List
from collections import defaultdict, deque


class ATM:

    def __init__(self):
        self.keys = [20, 50, 100, 200, 500]
        self.hst = {k: 0 for k in self.keys}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, cnt in enumerate(banknotesCount):
            self.hst[self.keys[i]] += cnt

    def withdraw(self, amount: int) -> List[int]:
        w_hst = dict()
        for k in reversed(self.keys):
            if self.hst[k] == 0:
                w_hst[k] = 0
                continue
            cnt = amount // k
            if cnt > self.hst[k]:
                amount = amount - k * self.hst[k]
                w_hst[k] = self.hst[k]
            else:
                w_hst[k] = cnt
                amount = amount % k
        if amount:
            return [-1]

        ret = True
        for k in self.keys:
            if self.hst[k] >= w_hst[k]:
                continue
            else:
                ret = False
                break
        if ret:
            ans = []
            for k in self.keys:
                self.hst[k] -= w_hst[k]
                ans.append(w_hst[k])
            return ans
        else:
            return [-1]


class Solution:
    def maximumScore2(self, scores: List[int], edges: List[List[int]]) -> int:
        adj_tbl = defaultdict(list)
        for u, v in edges:
            adj_tbl[u].append(v)
            adj_tbl[v].append(u)

        ans = -1
        for i in range(len(scores)):
            q = deque([[i, [i]]])
            k = 3
            while k > 0:
                for _ in range(len(q)):
                    cur, path = q.popleft()
                    for nex in adj_tbl[cur]:
                        if nex not in path:
                            q.append([nex, path + [nex]])
                k -= 1
            for cur, path in q:
                if path:
                    val = sum([scores[p] for p in path])
                    ans = max(ans, val)
                    print(path, val)
        return ans

    def maximumScore3(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        adj_tbl = defaultdict(list)
        for u, v in edges:
            adj_tbl[u].append(v)
            adj_tbl[v].append(u)

        ans = -1

        adj_tbl2 = defaultdict(list)
        adj_tbl3 = defaultdict(list)
        for i in range(n):
            for nex in adj_tbl[i]:
                adj_tbl2[i].append(nex)
            for path in adj_tbl2[i]:
                for nex in adj_tbl[path]:
                    if nex != i:
                        adj_tbl3[i].append([path, nex])

        for i in range(n):
            for s in adj_tbl[i]:
                for t in adj_tbl3[i]:
                    if s not in t:
                        ans = max(ans, scores[s] + scores[i] + scores[t[0]] + scores[t[1]])

        return ans

    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        neighbour = defaultdict(list)
        for a, b in edges:
            neighbour[a].append([scores[b], b])
            neighbour[b].append([scores[a], a])
        for k in neighbour:
            neighbour[k] = sorted(neighbour[k], reverse=True)

        to_ret = -1
        for a, b in edges:
            for s1, p1 in neighbour[a][:3]:
                for s2, p2 in neighbour[b][:3]:
                    if not len({a, b, p1, p2}) == 4:
                        continue
                    to_ret = max(to_ret, s1 + s2 + scores[a] + scores[b])
        return to_ret


if __name__ == '__main__':
    sol = Solution()
    scores = [5, 2, 9, 8, 4]
    edges = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
    ret = sol.maximumScore(scores, edges)
    print(ret)

    # atm = ATM()
    # atm.deposit([0, 10, 0, 3, 0])
    # ret = atm.withdraw(801)
    # print(ret)
