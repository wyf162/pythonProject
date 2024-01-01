# -*- coding : utf-8 -*-
# @Time: 2023/12/31 10:48
# @Author: yefei.wang
# @File: D.py

from typing import List


class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        def idx(c):
            return ord(c) - ord('a')

        n = len(s)
        m = n // 2
        pre_sum = [0] * (m + 1)
        for i in range(m):
            pre_sum[i + 1] = pre_sum[i] + int(s[i] != s[n - 1 - i])
        f = [[0 for _ in range(26)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(26):
                f[i + 1][j] = f[i][j] + int(idx(s[i]) == j)

        ans = []
        for a, b, c, d in queries:
            d1, c1 = n - c - 1, n - d - 1
            if a < c1 < b or a < d1 < b or c1 < b < d1 or c1 < a < d1:
                l, r = min(a, c1), max(b, d1)
                if pre_sum[l] != 0 or pre_sum[m] - pre_sum[r + 1] != 0:
                    ans.append(False)
                    break
                t1 = [0] * 26
                t2 = [0] * 26
                for j in range(26):
                    t1[j] = f[r + 1][j] - f[l][j]
                    # t2[j] = f[d + 1][j] - f[c][j]
                    t2[j] = f[n - l][j] - f[n - 1 - r][j]
                ans.append(t1 == t2)
            else:
                tmp = True
                for l, r in [(a, b), (c1, d1)]:
                    # print(l+1, m, r)
                    if pre_sum[l] != 0 or pre_sum[m] - pre_sum[r + 1] != 0:
                        tmp &= False
                    t1 = [0] * 26
                    t2 = [0] * 26
                    for j in range(26):
                        t1[j] = f[r + 1][j] - f[l][j]
                        t2[j] = f[n - l][j] - f[n - 1 - r][j]
                    tmp &= (t1 == t2)
                ans.append(tmp)
        return ans


if __name__ == '__main__':
    sol = Solution()
    # s = "abcabc"
    # # queries = [[1, 1, 3, 5], [0, 2, 5, 5]]
    # s = "abbcdecbba"
    # queries = [[0, 2, 7, 9]]
    # s = "acbcab"
    # queries = [[1, 2, 4, 5]]
    # s = "bbccbb"
    # queries = [[0, 1, 4, 5]]
    # s = "cbbbbc"
    # queries = [[1, 1, 5, 5]]
    s = "odaxusaweuasuoeudxwa"
    queries = [[0, 6, 10, 14]]
    ret = sol.canMakePalindromeQueries(s, queries)
    print(ret)
