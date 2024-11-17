
from typing import List


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        n = len(maximumHeight)
        h = maximumHeight[0]
        tot = h
        for i in range(1, n):
            if maximumHeight[i] >= h - 1:
                tot += h - 1
            else:
                tot += maximumHeight[i]
            h = min(h - 1, maximumHeight[i])
        return tot if h > 0 else -1


if __name__ == "__main__":
    sol = Solution()
    maximumHeight = [2, 2, 1]
    ret = sol.maximumTotalSum(maximumHeight)
    print(ret)
