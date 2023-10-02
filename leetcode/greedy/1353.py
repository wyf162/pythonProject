# -*- coding : utf-8 -*-
# @Time: 2023/9/29 10:17
# @Author: yefei.wang
# @File: 1353.py
import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        h = []
        ans = 0
        for i in range(1, 100001):
            while events and events[-1][0] == i:
                heapq.heappush(h, events.pop()[1])
            while h:
                cur = heapq.heappop(h)
                if cur >= i:
                    ans += 1
                    break
            if not events and not h: break
        return ans


if __name__ == '__main__':
    sol = Solution()
    # events = [[1,2],[1,2],[3,3],[1,5],[1,5]]
    events = [[1, 5], [1, 5], [1, 5], [2, 3], [2, 3]]
    ret = sol.maxEvents(events)
    print(ret)
