# _*_ coding: utf-8 _*_
# @Time : 2022/08/13 10:45 PM 
# @Author : yefe
# @File : 332_find_itinerary
from typing import List
from collections import defaultdict
import heapq


class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        vec = defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)

        for key in vec:
            heapq.heapify(vec[key])

        stack = list()

        def dfs(curr: str):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        dfs("JFK")
        return stack[::-1]


if __name__ == '__main__':
    sol = Solution()
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    ret = sol.findItinerary(tickets)
    print(ret)
