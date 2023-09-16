# _*_ coding: utf-8 _*_
# @Time : 2022/10/30 4:45 PM 
# @Author : yefe
# @File : 6222_make_integer_beautiful


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        tail = 1

        m = n
        while True:
            reminder = m % tail
            m = m + (tail-reminder if reminder else 0)
            if sum([int(i) for i in str(m)]) <= target:
                return m - n
            tail *= 10


if __name__ == '__main__':
    sol = Solution()
    n = 467
    target = 6
    ret = sol.makeIntegerBeautiful(n, target)
    print(ret)
