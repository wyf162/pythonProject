# -*- coding : utf-8 -*-
# @Time: 2021/12/19 14:58
# @Author: yefei.wang
# @File: 997_find_judge.py
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        is_judge = [True]*(n+1)
        for a,b in trust:
            is_judge[a]=False
        judges = []
        for i in range(1,n+1):
            if is_judge[i]:
                judges.append(i)
        return judges[0] if len(judges)==1 else -1


if __name__ == "__main__":
    sol = Solution()
    n = 4
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    print(sol.findJudge(n, trust))
