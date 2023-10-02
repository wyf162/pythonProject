# _*_ coding: utf-8 _*_
# @Time : 2022/04/30 8:59 PM 
# @Author : yefe
# @File : 354_max_envelopes
import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # print(envelopes)
        n = len(envelopes)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def maxEnvelopes2(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [envelopes[0][1]]
        for i in range(1, n):
            if (num := envelopes[i][1]) > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num

        return len(f)


if __name__ == '__main__':
    sol = Solution()
    # envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    envelopes = [[30, 50], [12, 2], [3, 4], [12, 15]]
    ret = sol.maxEnvelopes(envelopes)
    print(ret)
