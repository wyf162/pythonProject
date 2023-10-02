# _*_ coding: utf-8 _*_
# @Time : 2022/11/05 6:39 PM 
# @Author : yefe
# @File : 936_moves_to_stamp
from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        indegree = [min(m, n - i) for i in range(n - m + 1)]
        need = [set() for i in range(n)]
        deq = []
        for i in range(n - m + 1):
            for j in range(m):
                if i + j == n:
                    break
                elif target[i + j] == stamp[j]:
                    indegree[i] -= 1
                else:
                    need[i + j].add(i)
            if indegree[i] == 0:
                deq.append(i)
        res = []
        while deq:
            i = deq.pop()
            res.insert(0, i)
            for j in range(i, min(n, i + m)):
                for x in need[j]:
                    indegree[x] -= 1
                    if indegree[x] == 0:
                        deq.append(x)
                need[j] = set()
        return res if sum(indegree) == 0 else []


if __name__ == '__main__':
    sol = Solution()
    stamp = "abc"
    target = "ababc"
    ret = sol.movesToStamp(stamp, target)
    print(ret)
