# _*_ coding: utf-8 _*_
# @Time : 2022/10/16 7:04 PM 
# @Author : yefe
# @File : 3054_max_two_events
from typing import List
import heapq


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        q = []

        max_val = 0
        ans = 0
        for event in events:
            start, end, val = event
            while q and q[0][0] < start:
                max_val = max(max_val, q[0][1])
                heapq.heappop(q)

            ans = max(ans, max_val + val)
            heapq.heappush(q, (end, val))

        return ans


if __name__ == '__main__':
    sol = Solution()
    events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]
    ret = sol.maxTwoEvents(events)
    print(ret)
