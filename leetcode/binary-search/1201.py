# -*- coding : utf-8 -*-
# @Time: 2023/9/27 20:25
# @Author: yefei.wang
# @File: 1201.py
from math import lcm


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def check(x):
            n1 = x // a
            n2 = x // b
            n3 = x // c
            n12 = x // lcm(a, b)
            n13 = x // lcm(a, c)
            n23 = x // lcm(b, c)
            n123 = x // lcm(a, b, c)
            return n1 + n2 + n3 - n12 - n13 - n23 + n123

        l, r = 1, 2 * 10 ** 9
        ans = 0
        while l <= r:
            m = (l + r) >> 1
            k = check(m)
            if k >= n:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 3
    a = 2
    b = 3
    c = 5
    ret = sol.nthUglyNumber(n, a, b, c)
    print(ret)
