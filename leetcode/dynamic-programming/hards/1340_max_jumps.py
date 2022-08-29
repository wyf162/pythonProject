# _*_ coding: utf-8 _*_
# @Time : 2022/08/28 2:29 PM 
# @Author : yefe
# @File : 1340_max_jumps

from typing import List


class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n
        a = sorted([(i, arr[i]) for i in range(n)], key=lambda x: x[1])

        for i in range(n):
            cur = a[i][0]
            L = cur - 1 if cur >= 1 else 0
            R = cur + 1 if cur <= n - 2 else n - 1

            while 0 <= L:
                if arr[L] >= a[i][1]:
                    L += 1
                    if L > cur:
                        L = cur
                    break
                L -= 1
                if L < 0:
                    L = 0
                    break
                if L < cur - d:
                    L += 1
                    break

            while R < n:
                if arr[R] >= a[i][1]:
                    R -= 1
                    if R < cur:
                        R = cur
                    break
                R += 1
                if R > n - 1:
                    R = n - 1
                    break
                if R > cur + d:
                    R -= 1
                    break

            dp[cur] = max(dp[L:R + 1]) + 1

        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    arr = [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12]
    d = 2
    ret = sol.maxJumps(arr, d)
    print(ret)
