# -*- coding : utf-8 -*-
# @Time: 2022/6/12 19:03
# @Author: yefei.wang
# @File: 2305_distribute_cookies.py
from typing import List


class Solution:
    def distributeCookies2(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        m = 1 << n
        ss = [0] * (1 << n)
        for i, v in enumerate(cookies):
            bit = 1 << i
            for j in range(bit):
                ss[bit | j] = ss[j] + v

        f = ss.copy()
        for _ in range(1, k):
            for j in range(m - 1, 0, -1):
                s = j
                while s:
                    v = f[j ^ s]
                    if ss[s] > v:
                        v = ss[s]
                    if v < f[j]:
                        f[j] = v
                    s = (s - 1) & j
        return f[-1]

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        m = 1 << n
        f = [[1000000000 for j in range(m)] for i in range(k)]

        ss = [0] * m
        for i, v in enumerate(cookies):
            b = 1 << i
            for j in range(b):
                ss[b | j] = ss[j] + v

        for i in range(m):
            f[0][i] = ss[i]

        for i in range(1, k):
            for j in range(m):
                s = j
                while s:
                    f[i][j] = min(f[i][j], max(f[i - 1][j ^ s], ss[s]))
                    s = (s - 1) & j
        # print(f[-1])
        return f[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    cookies = [8, 15, 10, 20, 8]
    k = 2
    ret = sol.distributeCookies(cookies, k)
    print(ret)
