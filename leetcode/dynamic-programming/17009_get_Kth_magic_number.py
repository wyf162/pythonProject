# _*_ coding: utf-8 _*_
# @Time : 2022/04/30 12:02 PM 
# @Author : yefe
# @File : 17008_get_Kth_magic_number
import heapq


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        q = [1]
        heapq.heapify(q)
        visited = set()
        visited.add(1)
        ret = []
        while len(ret) < k:
            n = heapq.heappop(q)
            ret.append(n)
            if n * 3 not in visited:
                heapq.heappush(q, n * 3)
                visited.add(n * 3)
            if n * 5 not in visited:
                heapq.heappush(q, n * 5)
                visited.add(n * 5)
            if n * 7 not in visited:
                heapq.heappush(q, n * 7)
                visited.add(n * 7)
        return ret[-1]

    def get_kth_magic_number(self, k: int) -> int:
        dp = [1]
        p3, p5, p7 = 0, 0, 0
        for i in range(k-1):
            cur = min(dp[p3] * 3, dp[p5] * 5, dp[p7] * 7)
            if cur == dp[p3] * 3:
                p3 += 1
            if cur == dp[p5] * 5:
                p5 += 1
            if cur == dp[p7] * 7:
                p7 += 1
            dp.append(cur)
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    # ret = sol.getKthMagicNumber(5)
    ret = sol.get_kth_magic_number(10)
    print(ret)

