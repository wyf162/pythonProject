# _*_ coding: utf-8 _*_
# @Time : 2022/3/30 下午9:13 
# @Author : wangyefei
# @File : 1606_busiest_servers.py
import heapq
from typing import List


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k))
        busy = []
        requests = [0]*k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0]<=start:
                _, idx = heapq.heappop(busy)
                heapq.heappush(available, i + (idx-i)%k)
            if available:
                idx = heapq.heappop(available) % k
                requests[idx] += 1
                heapq.heappush(busy, (start+t, idx))
        max_request = max(requests)
        return [i for i, req in enumerate(requests) if req == max_request]


if __name__ == '__main__':
    sol = Solution()
    k = 3
    arrival = [1,2,3,4,5]
    load = [5,2,3,3,3]
    ret = sol.busiestServers(k, arrival, load)
    print(ret)