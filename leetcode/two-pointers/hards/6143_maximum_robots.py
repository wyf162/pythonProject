# _*_ coding: utf-8 _*_
# @Time : 2022/09/05 10:03 PM 
# @Author : yefe
# @File : 6143_maximum_robots

from collections import deque
from typing import List


class Solution:

    def maximumRobots(self, charge_times: List[int], running_times: List[int], budget: int) -> int:
        ans = s = left = 0
        q = deque()

        for right, (t, c) in enumerate(zip(charge_times, running_times)):
            while q and t >= charge_times[q[-1]]:
                q.pop()
            q.append(right)

            s += c

            while q and charge_times[q[0]] + (right - left + 1) * s > budget:
                if q[0] == left:
                    q.popleft()
                s -= running_times[left]
                left += 1

            ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    chargeTimes = [3, 6, 1, 3, 4]
    runningCosts = [2, 1, 3, 4, 5]
    budget = 25
    ret = sol.maximumRobots(chargeTimes, runningCosts, budget)
    print(ret)
