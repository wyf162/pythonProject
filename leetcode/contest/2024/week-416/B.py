
from typing import List
import math


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        def check(t):

            tot = 0
            for wkt in workerTimes:
                h = math.sqrt(2 * t / wkt + 0.25) - 0.5
                tot += int(h)
            return tot

        L, R = 1, 10**18
        while L <= R:
            mid = (L+R)//2
            if check(mid) >= mountainHeight:
                ans = mid
                R = mid - 1
            else:
                L = mid + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    mountainHeight = 4
    workerTimes = [2, 1, 1]
    ret = sol.minNumberOfSeconds(mountainHeight, workerTimes)
    print(ret)
