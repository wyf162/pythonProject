# _*_ coding: utf-8 _*_
# @Time : 2022/06/03 11:04 PM 
# @Author : yefe
# @File : 703_KthLargest
from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []
        heapq.heapify(self.pq)
        for num in nums:
            heapq.heappush(self.pq, num)
            if len(self.pq)>self.k:
                heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]


if __name__ == '__main__':
    cmds = ["KthLargest", "add", "add", "add", "add", "add"]
    parms = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

    kth_largest = KthLargest(*parms[0])
    for cmd, parm in zip(cmds[1:], parms[1:]):
        ret = getattr(kth_largest, cmd)(*parm)
        print(ret)
