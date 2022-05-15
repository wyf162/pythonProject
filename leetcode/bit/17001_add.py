# _*_ coding: utf-8 _*_
# @Time : 2022/05/01 11:47 PM 
# @Author : yefe
# @File : 17001_add
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        print(0x3f)
        print(0b111111)

        a, b = a & x, b & x
        while b != 0:
            c = a & b
            a = a ^ b
            b = (c << 1) & x
        return a if a <= 0x7fffffff else ~(a ^ x)


if __name__ == '__main__':
    sol = Solution()
    a = 11
    b = 11
    c = sol.add(a, b)
    print(c)
