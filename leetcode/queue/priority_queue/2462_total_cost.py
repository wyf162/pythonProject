# _*_ coding: utf-8 _*_
# @Time : 2022/11/07 9:28 PM 
# @Author : yefe
# @File : 2462_total_cost

from typing import List
import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if candidates * 2 >= n:
            return sum(sorted(costs)[:k])

        l_pq = [(costs[i], i) for i in range(candidates)]
        r_pq = [(costs[n - j - 1], n - j - 1) for j in range(candidates)]
        heapq.heapify(l_pq)
        heapq.heapify(r_pq)
        s = 0
        i = candidates
        j = n - candidates - 1
        while i <= j and k > 0:
            if l_pq[0][0] <= r_pq[0][0]:
                s += heapq.heappop(l_pq)[0]
                heapq.heappush(l_pq, (costs[i], i))
                i += 1
            else:
                s += heapq.heappop(r_pq)[0]
                heapq.heappush(r_pq, (costs[j], j))
                j -= 1
            k -= 1

        pq = l_pq + r_pq
        heapq.heapify(pq)
        while k > 0 and pq:
            s += heapq.heappop(pq)[0]
            k -= 1
        return s


if __name__ == '__main__':
    sol = Solution()
    costs = [31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58]
    k = 11
    candidates = 2
    ret = sol.totalCost(costs, k, candidates)
    print(ret)
