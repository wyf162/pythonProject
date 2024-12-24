from heapq import heappop, heappush
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        h = []
        ans = 0
        mx = n
        for i in range(n):
            if apples[i] != 0:
                heappush(h, (i + days[i], apples[i]))
                mx = max(mx, i + days[i])
            while h and h[0][0] <= i:
                heappop(h)
            if h:
                x, y = heappop(h)
                y -= 1
                ans += 1
                if y > 0:
                    heappush(h, (x, y))
        for i in range(n, mx + 1, 1):
            while h and h[0][0] <= i:
                heappop(h)
            if h:
                x, y = heappop(h)
                y -= 1
                ans += 1
                if y > 0:
                    heappush(h, (x, y))
        return ans


if __name__ == '__main__':
    sol = Solution()
    apples = [1, 2, 3, 5, 2]
    days = [3, 2, 1, 4, 2]
    # apples = [3, 0, 0, 0, 0, 2]
    # days = [3, 0, 0, 0, 0, 2]
    ret = sol.eatenApples(apples, days)
    print(ret)
