# _*_ coding: utf-8 _*_
# @Time : 2022/10/15 10:32 PM 
# @Author : yefe
# @File : biweek-89-20221015

import re
from typing import List


class Solution:
    def countTime(self, time: str) -> int:
        hh, mm = time.split(':')

        cnt_h = 1
        cnt_m = 1

        if hh == "??":
            cnt_h = 24
        elif re.match(r"\?[0-3]", hh):
            cnt_h = 3
        elif re.match(r"\?[4-9]", hh):
            cnt_h = 2
        elif re.match(r"[0-1]\?", hh):
            cnt_h = 10
        elif re.match(r"2\?", hh):
            cnt_h = 4

        if mm == "??":
            cnt_m = 60
        elif re.match(r"[0-9]\?", mm):
            cnt_m = 10
        elif re.match(r"\?[0-9]", mm):
            cnt_m = 6

        return cnt_h * cnt_m

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        M = 10 ** 9 + 7
        powers = []
        i = 0
        while n > 0:
            k = n % 2
            n = n // 2
            if k:
                powers.append(2 ** i)
            i += 1
        print(powers)
        hst = dict()

        rets = []
        for l, r in queries:
            if (l, r) in hst:
                rets.append(hst[(l, r)])
            else:
                val = 1
                for i in range(l, r+1):
                    val *= powers[i]
                    val %= M
                rets.append(val)
                hst[(l, r)] = val
        return rets


if __name__ == '__main__':
    sol = Solution()
    n = 15
    queries = [[0, 1], [2, 2], [0, 3]]
    ret = sol.productQueries(n, queries)
    print(ret)
    # time = "?5:00"
    # ret = sol.countTime(time)
    # print(ret)
