# -*- coding : utf-8 -*-
# @Time: 2022/1/23 16:12
# @Author: yefei.wang
# @File: 21_bit.py
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)


if __name__ == '__main__':
    sol = Solution()
    data = sol.add(19, 1999)
    print(data)